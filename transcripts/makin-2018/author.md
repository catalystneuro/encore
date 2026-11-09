# 000129 · author · run 40749995806

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls paper claims/000129 entries attempts | head -50
```

```
<persisted-output>
Output too large (36.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/c31690e9-0447-4fbb-9670-4ed8ee7db774/tool-results/bvk4smz7w.txt

Preview (first 2KB):
Wed Oct 28 19:00:21 UTC 2026
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
cat README.md | head -80; wc -l docs/design.md docs/archives.md; ls paper claims/000129; ls entries | tail -5; ls attempts | tail -3
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
[... 77 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/000129/*.yaml
```

```
<persisted-output>
Output too large (43.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/c31690e9-0447-4fbb-9670-4ed8ee7db774/tool-results/bpfluts5q.txt

Preview (first 2KB):
# Claims for Makin, O'Doherty, Cardoso & Sabes (2018), J. Neural Eng. 15 026010, on dandiset 000129.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-28,
# protocol as stated in docs/protocol.md.
#
# Text read: the version of record (PDF supplied by a person, extracted to
# paper/10.1088-1741-2552-aa9e95.txt), main text with its Methods, Results, Discussion and figure
# legends. The paper has no supplement. Two equations are garbled in the extracted text (the
# ridge penalty of equation 10 and the Wiener filter order sweep); the PDF could not be rendered
# here, and the code settles both (below).
#
# Data the paper used (Methods, Animal experiments, Data acquisition, Tasks). Three monkeys, 49
# sessions of continuous reaching in the horizontal plane. Monkey I (Sabes lab, 37 sessions,
# right hemisphere, left arm) and monkey L (Sabes lab, 10 sessions, left hemisphere, right arm):
# point-to-point reaching to targets on an 8 by 8 or 8 by 17 grid (I) or a 6 by 6 grid (L),
# 15 mm spacing, 450 ms hold, no inter-trial interval. 96-channel Utah arrays in M1 and S1;
# S1 was recorded in 7 of monkey I's 37 sessions and in all 10 of monkey L's. Spikes sorted
[... 12 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/000129/10.1088-1741-2552-aa9e95.yaml"
}
```

```
1	# Claims for Makin, O'Doherty, Cardoso & Sabes (2018), J. Neural Eng. 15 026010, on dandiset 000129.
2	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-28,
3	# protocol as stated in docs/protocol.md.
4	#
5	# Text read: the version of record (PDF supplied by a person, extracted to
6	# paper/10.1088-1741-2552-aa9e95.txt), main text with its Methods, Results, Discussion and figure
7	# legends. The paper has no supplement. Two equations are garbled in the extracted text (the
8	# ridge penalty of equation 10 and the Wiener filter order sweep); the PDF could not be rendered
9	# here, and the code settles both (below).
10	#
11	# Data the paper used (Methods, Animal experiments, Data acquisition, Tasks). Three monkeys, 49
12	# sessions of continuous reaching in the horizontal plane. Monkey I (Sabes lab, 37 sessions,
13	# right hemisphere, left arm) and monkey L (Sabes lab, 10 sessions, left hemisphere, right arm):
14	# point-to-point reaching to targets on an 8 by 8 or 8 by 17 grid (I) or a 6 by 6 grid (L),
15	# 15 mm spacing, 450 ms hold, no inter-trial interval. 96-channel Utah arrays in M1 and S1;
16	# S1 was recorded in 7 of monkey I's 37 sessions and in all 10 of monkey L's. Spikes sorted
17	# online, with an unsorted hash unit kept per channel; units below 0.5 Hz discarded, leaving
18	# 171 to 413 units per session for monkey I and 416 to 523 for L. Fingertip position from a
19	# Polhemus sensor at 250 Hz. Monkey C (Koerding lab, 2 sessions, 75 and 91 units, center-out
20	# task) came from a public dataset (Dyer et al., biorxiv 080861). The Sabes lab data are
[... 636 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,120p docs/archives.md; ls entries/001453-fouke-2025/; cat entries/001453-fouke-2025/entry.yaml entries/001453-fouke-2025/requirements.in; head -c 3000 attempts/001453-fouke-2025-01.yaml
```

```
# Archives

The registry tests papers against data in public archives. It began with one,
the DANDI Archive. The protocol is written for any archive. What is particular
to an archive (how its datasets are named, versioned and read) is here, and an
agent is pointed to its archive's section.

A dataset is keyed as `<archive>:<id>` and shown as `<LABEL>:<id>`, for example
`DANDI:000003`. Its files in this repository (`claims/`, `questions/`,
`transcripts/`, the `attempt/` branch, the paper store) are under its folder
name: the identifier alone for DANDI, which the registry began with, and
`<archive>-<id>` for any other archive. Each archive is an adapter, a module in `tools/archives/` ("Adding an archive",
below), and `tools/datasets.py` turns one form of a dataset's name into another.
The workflows take a dataset in any of these forms.

## DANDI

- **Datasets.** A dandiset, identified by six digits (`000003`). Targets are the
  public dandisets whose metadata names a paper (`targets/dandisets.json`, built
  by `tools/build_targets.py` and refreshed daily by the Track DANDI workflow).
[... 191 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^[a-z]" attempts/001453-fouke-2025-01.yaml; grep -n -A12 "^findings" attempts/001453-fouke-2025-01.yaml | head -30; grep -n -B2 -A10 "blocked_by" attempts/*.yaml | head -30; ls schemas; python -c "import pynwb,remfile,dandi" ; which uv
```

```
1:schema_version: 2
2:id: 001453-fouke-2025-01
3:dataset:
8:paper: doi:10.1016/j.cub.2025.04.027
9:date: 2026-10-14
10:entry: 001453-fouke-2025
11:provenance:
22:inputs:
34:outcomes:
243:findings:
309:verifications:
243:findings:
244-- kind: data_missing
245-  statement: The dandiset holds only the freely swimming tracking of Figure 1 and Figure S1. The
246-    two-photon imaging and the head-fixed tail tracking behind Figures 2 to 4 are not in it, and
247-    the GitLab repository the paper names for all behavioural and imaging data holds analysis
248-    notebooks only. Nine of the paper's main findings cannot be tested.
249-- kind: metadata_insufficient
250-  statement: The stimulus codes 0 to 20 have no names or description in the files or the
251-    dandiset metadata. They can be named only from the paper's analysis notebook and the protocol
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q ev && . ev/bin/activate && uv pip install -q pynwb remfile h5py numpy scipy requests matplotlib 2>&1 | tail -2; curl -s https://api.dandiarchive.org/api/dandisets/000129/ | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/000129/versions/" | python -m json.tool | grep -E '"version"|created|modified|status'
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && . ev/bin/activate && curl -s "https://api.dandiarchive.org/api/dandisets/000129/versions/0.241017.1444/" | python -c "
import json,sys; d=json.load(sys.stdin)
for k in ['name','description','citation','relatedResource','assetsSummary','doi','wasGeneratedBy','contributor']:
    print(k, json.dumps(d.get(k),indent=0)[:1500])
"; curl -s "https://api.dandiarchive.org/api/dandisets/000129/versions/0.241017.1444/assets/" | python -m json.tool | grep -E 'asset_id|path|size'
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && . ev/bin/activate && cat > insp.py <<'EOF'
import remfile,h5py,pynwb,requests,numpy as np
for aid in ["2ae6bf3c-788b-4ece-8c01-4b4a5680b25b","648a7418-98e8-4413-ba97-3772dd325ecc"]:
    url=requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=True).url
    f=h5py.File(remfile.File(url),'r'); io=pynwb.NWBHDF5IO(file=f,load_namespaces=True); nwb=io.read()
    print("=====",aid, nwb.identifier, nwb.session_description, nwb.session_start_time)
    print(nwb.subject)
    print("acq", list(nwb.acquisition)); print("proc", {k:list(v.data_interfaces) for k,v in nwb.processing.items()})
    for k,v in nwb.acquisition.items(): print(k, type(v).__name__, getattr(v,'data',None) and v.data.shape if hasattr(v,'data') else list(getattr(v,'spatial_series',{}) ))
    for k,m in nwb.processing.items():
        for n,di in m.data_interfaces.items():
            print(k,n,type(di).__name__)
            if hasattr(di,'spatial_series'):
                for s,ss in di.spatial_series.items(): print("  ",s,ss.data.shape,ss.unit,ss.rate,ss.starting_time, ss.timestamps.shape if ss.timestamps is not None else None, ss.description)
            elif hasattr(di,'data'): print("  ",di.data.shape,di.unit,di.rate,di.starting_time,di.description)
    u=nwb.units; print("units cols", u.colnames, len(u))
    df=u.to_dataframe(); print(df.drop(columns=['spike_times']).head(10).to_string()); print(df.drop(columns=['spike_times']).describe(include='all').to_string()[:2000])
    st=df.spike_times; print("nspikes",sum(len(s) for s in st), "range",min(s.min() for s in st if len(s)), max(s.max() for s in st if len(s)))
    if nwb.trials is not None:
        t=nwb.trials.to_dataframe(); print("trials",t.shape, t.columns.tolist()); print(t.head().to_string()); print(t.tail(3).to_string())
        for c in t.columns:
            if t[c].dtype==object: print(c, t[c].value_counts().head())
    print("electrodes", nwb.electrodes.to_dataframe().head().to_string() if nwb.electrodes is not None else None)
    print("intervals", list(nwb.intervals) if nwb.intervals else None)
EOF
python insp.py 2>&1 | grep -v Warn
```

```
<persisted-output>
Output too large (31KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/c31690e9-0447-4fbb-9670-4ed8ee7db774/tool-results/bv7oqz1dh.txt

Preview (first 2KB):
===== 2ae6bf3c-788b-4ece-8c01-4b4a5680b25b 7043e134-0b92-11ec-96df-0db753c69267 Data from monkey Indy performing self-paced random target reaching task. This file contains continuous segments of the full session on 2017-02-02 that can be used for training models for the Neural Latents Benchmark. 2017-02-02 00:00:00-08:00
subject pynwb.file.Subject at 0x124256565513584
Fields:
  age: P11Y
  sex: M
  species: Macaca mulatta
  subject_id: Indy

acq []
proc {'behavior': ['cursor_pos', 'finger_pos', 'finger_vel', 'target_pos']}
behavior cursor_pos SpatialSeries
   (649100, 2) meters 1000.0 0.0 The position of the cursor in Cartesian coordinates (x, y) in mm. Recorded at 250 Hz and upsampled to 1 kHz
behavior finger_pos SpatialSeries
   (649100, 3) meters 1000.0 0.0 The position of the working fingertip in Cartesian coordinates (x, y, z), as reported by the hand tracker in mm. Recorded at 250 Hz and upsampled to 1 kHz
behavior finger_vel TimeSeries
   (649100, 2) m/s 1000.0 0.0 The x and y velocity of the finger in mm/s. Calculated offline from upsampled finger position
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 25,400p /home/runner/.claude/projects/-home-runner-work-encore-encore/c31690e9-0447-4fbb-9670-4ed8ee7db774/tool-results/bv7oqz1dh.txt | cut -c1-250 | grep -v "^\s*$" | head -150
```

```
[1 rows x 8 columns]
203      True  [[0.0, 162.2], [162.3, 324.5], [324.6, 486.8], [486.9, 649.1]]       x  ...       group_name
id      ...                 
2  NaN  ...  electrode_group
[1 rows x 8 columns]
204      True  [[0.0, 162.2], [162.3, 324.5], [324.6, 486.8], [486.9, 649.1]]       x  ...       group_name
id      ...                 
2  NaN  ...  electrode_group
[1 rows x 8 columns]
301     False  [[0.0, 162.2], [162.3, 324.5], [324.6, 486.8], [486.9, 649.1]]       x  ...       group_name
id      ...                 
3  NaN  ...  electrode_group
[1 rows x 8 columns]
401     False  [[0.0, 162.2], [162.3, 324.5], [324.6, 486.8], [486.9, 649.1]]       x  ...       group_name
id      ...                 
4  NaN  ...  electrode_group
[1 rows x 8 columns]
601      True  [[0.0, 162.2], [162.3, 324.5], [324.6, 486.8], [486.9, 649.1]]       x  ...       group_name
id      ...                 
6  NaN  ...  electrode_group
[... 123 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -l paper/*.txt; grep -n -i -E "2017|2016|indy|session" paper/*.txt | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; for f in NeuralAnalysis/Indy_HC_Sessions.csv; do curl -s https://raw.githubusercontent.com/jgmakin/rbmish/700062f5118b0910411cf9a8f73498e22203731d/$f | head -60; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://raw.githubusercontent.com/jgmakin/rbmish/700062f5118b0910411cf9a8f73498e22203731d/NeuralAnalysis/Indy_HC_Sessions.csv | wc -l; curl -s https://raw.githubusercontent.com/jgmakin/rbmish/700062f5118b0910411cf9a8f73498e22203731d/NeuralAnalysis/Indy_HC_Sessions.csv | tail -5; curl -s "https://zenodo.org/api/records/583331" | python3 -c "import json,sys;d=json.load(sys.stdin);print(d['metadata']['title'],d['metadata'].get('version'),d['id']);print([f['key'] for f in d['files'] if '2017' in f['key']])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://zenodo.org/api/records/3854034" | python3 -c "
import json,sys;d=json.load(sys.stdin);print(d['metadata']['title'],d['metadata'].get('version'),d['id'], d['metadata'].get('publication_date'))
fs=sorted(f['key'] for f in d['files']); print(len(fs)); print([ (f) for f in fs if 'indy_2017' in f])
print([(f['key'],f['size']) for f in d['files'] if 'indy_2017013' in f['key'] or 'indy_201702' in f['key']])"
```

Result: the fetched text is not kept.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1088-1741-2552-aa9e95.txt",
 "offset": 195,
 "limit": 600
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; B=https://raw.githubusercontent.com/jgmakin/rbmish/700062f5118b0910411cf9a8f73498e22203731d; mkdir -p rb; for f in RBM/setLearningSchedules.m RBM/setParams.m RBM/EFH.m RBM/EFHlearn.m NeuralAnalysis/getLatentsBMI.m NeuralAnalysis/binSpikeCounts.m NeuralAnalysis/filterDecoder.m tools/WFDecoder.m NeuralAnalysis/filtersForNeuralData.m NeuralAnalysis/testEFHBMI.m NeuralAnalysis/BMImaster.m; do curl -s -o rb/$(basename $f) $B/$f; echo $f $(wc -l < rb/$(basename $f)); done; curl -s https://api.github.com/repos/jgmakin/rbmish/git/trees/700062f5118b0910411cf9a8f73498e22203731d?recursive=1 | python3 -c "import json,sys; [print(t['path']) for t in json.load(sys.stdin)['tree'] if t['path'].startswith('RBM/')]" | head -60
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/rb; cat setLearningSchedules.m; grep -n -A60 "case 'spikecounts'" setParams.m | head -90
```

```
function params = setLearningSchedules(mw0,mvb0,mhb0,GROWTH,params,mrw0,mrb0)
% setLearningSchedules  Set EFH learning-rate annealing schedules
%
% USAGES:
%   params = setLearningSchedules(500,120,120,'exp',params)
%   params = setLearningSchedules(200,200,400,'hyperbolic',params);
%   params = setLearningSchedules(500,120,120,'logistic',params);
%
% Consider the inverse of the learning rate, which we can treat as a mass.
% Then the "annealing" of the learning rate is equivalent to the mass grow-
% ing according to some dynamics.  In particular, "momentum" and "weight
% decay" of the NN parameter updates can be interpreted as facts about a
% second-order dynamical system, whose input is the gradient and whose
% output is the parameter update--see secondOrderWeightUpdate.m for
% details.  Then the mass itself grows across parameter updates.
%
% NB: if the damping coefficient, b, is set to half the initial mass (as is
% usually often down below), then oscillations can be prevented by setting
% k < m/16---at least for the continuous-time version.  In discrete time
% your margin gets slightly bigger.
[... 194 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/rb; sed -n 1215,1250p setParams.m; curl -s https://raw.githubusercontent.com/jgmakin/rbmish/700062f5118b0910411cf9a8f73498e22203731d/RBM/CDstepper.m -o CDstepper.m; curl -s https://raw.githubusercontent.com/jgmakin/rbmish/700062f5118b0910411cf9a8f73498e22203731d/RBM/dynamical/recurrentEFHtrain.m -o ret.m; wc -l CDstepper.m ret.m; grep -v "^\s*%" ret.m | grep -v "^\s*$" | head -150
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/rb; grep -v "^\s*%" EFH.m | grep -v "^\s*$"; cat CDstepper.m | grep -v "^\s*%"; curl -s https://raw.githubusercontent.com/jgmakin/rbmish/700062f5118b0910411cf9a8f73498e22203731d/RBM/secondOrderWeightUpdate.m | grep -v "^\s*%" | grep -v "^\s*$"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/rb; B=https://raw.githubusercontent.com/jgmakin/rbmish/700062f5118b0910411cf9a8f73498e22203731d; for f in RBM/dynamical/recurrentize.m RBM/reinitializeEFH.m RBM/invParamMap.m RBM/sampleT.m; do curl -s -o $(basename $f) $B/$f; echo "=== $f"; grep -v "^\s*%" $(basename $f) | grep -v "^\s*$" | head -80; done; grep -n -i "sparsitycost\|estimRate\|Ncdsteps" EFH.m setParams.m | head
```

```
=== RBM/dynamical/recurrentize.m
function [visDstrbs,visNums,inputDstrbs,inputNums,inputInd,...
    vishid,vishidinc,visbiases,visbiasinc,algorithm,Ncdsteps,...
    mwfunc,mvbfunc,bwfunc,bvbfunc,kwfunc,kvbfunc,...
    mw,mvb,bw,bvb,kw,kvb] = recurrentize(visDstrbs,visNums,...
    hidDstrbs,hidNums,vishid,vishidinc,visbiases,visbiasinc,epoch,params)
algorithm = params.algorithm;
Ncdsteps = params.Ncdsteps;
inputDstrbs = visDstrbs;
inputNums = visNums;
inputInd = sum(hidNums) + 1;
if ~strcmp(algorithm,'EFH')
    visDstrbs   = [hidDstrbs, visDstrbs];
    visNums     = [hidNums,   visNums];
    vishid = cat(1,0.005*randn([sum(hidNums),sum(hidNums)],...
        'like',vishid),vishid);
    vishidinc = cat(1,0*ones([sum(hidNums),sum(hidNums)],...
        'like',vishidinc),vishidinc);
    visbiases = cat(1,0*ones([sum(hidNums),1],...
        'like',visbiases),visbiases);
[... 172 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/rb; grep -n -i "sparse\|Ncdsteps *=" EFH.m setParams.m | head -20; grep -n "Ncdsteps" setParams.m | head -3
```

```
EFH.m:84:        Ncdsteps = 5;                   %
EFH.m:86:        Ncdsteps = params.Ncdsteps;
EFH.m:243:        % force sparse hidden units?
setParams.m:41:params.Ncdsteps     = defaulter('Ncdsteps',1,varargin{:});
setParams.m:660:                params.Ncdsteps = 25;
setParams.m:900:        params.Ncdsteps = 25;
setParams.m:976:        params.Ncdsteps = 25;
setParams.m:1138:        params.Ncdsteps = 25;
setParams.m:1204:        sparse.cost = 0.20;
setParams.m:1205:        sparse.phidNewFrac = 0.95;
setParams.m:1206:        sparse.phidTarget = defaulter('phidtarget',0.05,varargin{:});
setParams.m:1207:        params.sparse = sparse;
41:params.Ncdsteps     = defaulter('Ncdsteps',1,varargin{:});
512:            'Ncases','Nbatches','NepochsMax','Ncdsteps'};
660:                params.Ncdsteps = 25;
Shell cwd was reset to
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/rb; sed -n 30,75p EFH.m; curl -s https://api.github.com/search/code?q=estimRate+repo:jgmakin/rbmish | head -5
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/rb; B=https://raw.githubusercontent.com/jgmakin/rbmish/700062f5118b0910411cf9a8f73498e22203731d; for f in RBM/DBNtrain.m RBM/EFHrestart.m RBM/generateData.m; do curl -s -o $(basename $f) $B/$f; done; grep -n -i -B2 -A2 "sparse\|estimRate" DBNtrain.m EFHrestart.m | head -30; grep -v "^\s*%" generateData.m | grep -v "^\s*$" | head -30
```

```
DBNtrain.m-40-    Npretrain = 0;
DBNtrain.m-41-end
DBNtrain.m:42:if isfield(params,'sparse')
DBNtrain.m:43:    sparsitycost= params.sparse.cost;    
DBNtrain.m:44:    estimRate   = params.sparse.phidNewFrac;
DBNtrain.m:45:    phidTarget  = params.sparse.phidTarget;
DBNtrain.m-46-else
DBNtrain.m-47-    sparsitycost= 0;
function [R,X,Q] = generateData(Nexamples,getLatents,getData,dataclass,varargin)
[X,Q] = getLatents(Nexamples,dataclass);
[R,Q] = getData(X,Q);
end
Shell cwd was reset to
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/rb; for f in getLatentsBMI.m binSpikeCounts.m; do echo "=== $f"; grep -v "^\s*%" $f | grep -v "^\s*$"; done
```

```
=== getLatentsBMI.m
function [X,Q,bad_neurons] = getLatentsBMI(Nexamples,dataclass,T,testortrain,params,varargin)
T = defaulter('sequencelength',T,varargin{:});
trainingtime = params.trainingtime;
mods = params.mods;
datafile = params.datafile;
Fs = params.Fs;
Nmsperbin = params.Nmsperbin;
Nmspers = 1000; % fact
sperbin = (Nmsperbin/Nmspers);
Nsamplesperbin = round(Fs*sperbin);
[spikedata, St, Ndims] = loadNeuralData(dataclass,datafile,mods,Fs);
minRate = 0.5;                              % Hz.  Somewhat arbitrary
BinParams.m = Nsamplesperbin;
BinParams.dt = 1/Fs;
BinParams.Ndims = Ndims;
BinParams.Nstates = size(St(1).X,2);
BinParams.BINMETHOD = 'void';
UnitSpikesT = cell2struct(spikedata(:), 't', 2);
[R,X,~] = binSpikeCounts(St,UnitSpikesT,BinParams);
[... 235 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/rb; for f in testEFHBMI.m filterDecoder.m WFDecoder.m; do echo "=== $f"; grep -v "^\s*%" $f | grep -v "^\s*$"; done 2>&1 | cut -c1-160
```

```
=== testEFHBMI.m
function [testError,XhatStatic,RsqStatic,XhatDynamic,RsqDynamic,...
    Bv,LDSparamsObs] = testEFHBMI(Rtest,Xtest,Qtest,wts,params,varargin)
TOPLOT = 0;
if isempty(varargin)
    [Xtrain,Qtrain] = params.getLatents([],class(wts{1}),...
        'sequencelength','singlesequence');
    [Rtrain,Qtrain] = params.getData(Xtrain,Qtrain);
    SStot = sum((Xtest - mean(Xtest)).^2);
else
    [Rtrain,Xtrain,Qtrain,SStot] = deal(varargin{:});
end
Vtrain = LDSobsfxn(Rtrain,Qtrain,wts,params);
clear Rtrain Qtrain
Vtest = LDSobsfxn(Rtest,Qtest,wts,params);
clear Rtest Qtest
[XhatStatic,RsqStatic,XhatDynamic,RsqDynamic,Bv,LDSparamsObs] =...
    filterDecoder(Vtrain,Xtrain,Vtest,Xtest,1,SStot,params.Nmsperbin);
testError = mean(10*log10(1 - RsqStatic(:))); 
if TOPLOT
[... 232 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/rb; grep -v "^\s*%" filtersForNeuralData.m | grep -v "^\s*$" | cut -c1-150 | head -230
```

```
function [Rsqs,NdataTest] = filtersForNeuralData(wts,params,LDSparamsEM,...
    decodernames,TOPLOT)
if checkGPUavailability, dataclass = 'gpuArray'; else, dataclass = 'double'; end
Nsplot = 60;
Nmsperbin = params.Nmsperbin;
Nmspers = 1000; % fact
if TOPLOT, tvec = 1:ceil(Nsplot/(Nmsperbin/Nmspers)); else, tvec=[]; end
[Rtrain,Xtrain,Qtrain] = getSingleTrainingSequence(dataclass,params);
[Rtest,Xtest,Qtest] = params.getTestData(dataclass);
SStot = sum((Xtest - mean(Xtest)).^2);
NdataTest = size(Rtest,1);
if ~isempty(tvec), PosVelPlot(tvec,Xtest,1); end
if any(strcmp(decodernames,'static'))
    [~,~,RsqStatic] = staticLinearDecoder(Rtrain,Xtrain,...
        Rtest,Xtest,SStot);
    Rsqs(:,:,:,strcmp(decodernames,'static'))       = RsqStatic;
end
if any(strcmp(decodernames,'kfobs'))
    [LDSparamsObs,~,RsqKF_Obs] = ...
        fullyObservedLDSDecoder(Rtrain,Xtrain,Qtrain.T,Rtest,Xtest,SStot);
[... 206 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/rb; B=https://raw.githubusercontent.com/jgmakin/rbmish/700062f5118b0910411cf9a8f73498e22203731d; for f in tools/linregress.m RBM/dynamical/updownRDBN.m tools/learnfullyobservedLDS.m; do curl -s -o $(basename $f) $B/$f; echo "== $f"; grep -v "^\s*%" $(basename $f) | grep -v "^\s*$" | head -70; done
```

```
== tools/linregress.m
function [beta,Rsq,Yres,Yhat,p] = linregress(X,Y,varargin)
crossvalidation = defaulter('cross validate','none',varargin{:});
lambda_L2 = defaulter('L2 regularize',0,varargin{:});
pad_with_ones = defaulter('pad with ones',0,varargin{:});
Nsamples = size(Y,1);
if pad_with_ones, X = [X, ones(size(X,1),1)]; end
if lambda_L2 > 0
    Xpinv = (X'*X + lambda_L2*eye(size(X,2)))\X';
else
    Xpinv = (X'*X)\X';
end
beta = Xpinv*Y;
if nargout > 1
    switch crossvalidation
        case 'LOO'
            if Nsamples < 1000
                H = X*Xpinv;                    % hat matrix
                M = eye(Nsamples) - H;          % residual matrix
                Yres = (M*Y)./diag(M);
[... 112 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . ev/bin/activate && cat > insp2.py <<'EOF'
import remfile,h5py,requests,numpy as np
url=requests.head("https://api.dandiarchive.org/api/assets/2ae6bf3c-788b-4ece-8c01-4b4a5680b25b/download/",allow_redirects=True).url
f=h5py.File(remfile.File(url),'r')
u=f['units']; print(list(u.keys()))
ids=u['id'][:]; print(ids.tolist())
print("heldout", u['heldout'][:].sum())
st=u['spike_times'][:]; idx=u['spike_times_index'][:]
cnt=np.diff(np.r_[0,idx]); print("rates", np.sort(cnt/649.1)[:10], np.median(cnt/649.1))
b=f['processing/behavior']
for k in b: 
    d=b[k]['data'][:]; print(k, d.shape, np.isnan(d).sum(0), np.nanmin(d,0), np.nanmax(d,0), dict(b[k]['data'].attrs))
fp=b['finger_pos']['data'][:20000,:2]; print(fp[:12])
nanrows=np.where(np.isnan(b['finger_pos']['data'][:,0]))[0]; print("nan rows", len(nanrows), nanrows[:5], nanrows[-5:] if len(nanrows) else None)
# check upsampling: are 4-sample blocks constant or interpolated?
d=np.diff(fp[:,0]); print("zero diffs frac", np.mean(d==0))
cp=b['cursor_pos']['data'][:20000]; print(cp[:6]); 
print("cursor-finger offset", np.nanmean(b['cursor_pos']['data'][:]-b['finger_pos']['data'][:,:2],0), np.nanstd(b['cursor_pos']['data'][:]-b['finger_pos']['data'][:,:2],0))
print(f['general'].keys() if 'general' in f else None)
for k in ['session_description','identifier']: print(k, f[k][()])
print(dict(f['/'].attrs))
EOF
python insp2.py 2>&1 | grep -v Warn
```

```
['electrodes', 'electrodes_index', 'heldout', 'id', 'obs_intervals', 'obs_intervals_index', 'spike_times', 'spike_times_index']
[201, 203, 204, 301, 401, 601, 701, 802, 901, 1001, 1002, 1101, 1102, 1103, 1202, 1301, 1302, 1303, 1402, 1501, 1503, 1601, 1602, 1801, 1902, 1903, 2001, 2002, 2003, 2101, 2102, 2103, 2201, 2301, 2302, 2303, 2402, 2403, 2602, 2702, 2703, 2801, 3101, 3102, 3201, 3202, 3501, 3601, 3701, 3704, 3801, 3902, 4002, 4101, 4301, 4302, 4401, 4402, 4501, 4601, 4701, 4801, 4802, 4901, 5001, 5101, 5102, 5201, 5202, 5401, 5402, 5403, 5501, 5601, 5701, 5801, 5902, 6002, 6101, 6102, 6201, 6202, 6203, 6301, 6302, 6402, 6403, 6501, 6601, 6701, 6802, 6902, 7001, 7002, 7101, 7102, 7201, 7301, 7302, 7303, 7401, 7402, 7403, 7404, 7502, 7602, 7604, 7701, 7702, 7901, 7902, 7903, 8001, 8102, 8303, 8601, 8602, 8701, 8801, 8901, 9001, 9103, 9201, 9203, 9301, 9403, 9501, 9502, 9601, 9602]
heldout 32
rates [0.07702973 0.10167925 0.13403174 0.1432753  0.15097828 0.17100601
 0.17100601 0.17870898 0.18024958 0.18179017] 2.9633338468648898
cursor_pos (649100, 2) [300 300] [-65.24993512  -7.81515764] [ 71.04256397 117.94841593] {'conversion': np.float64(0.001), 'resolution': np.float64(-1.0), 'unit': 'meters'}
finger_pos (649100, 3) [300 300 300] [-63.77828213  -7.46904361  85.35383219] [ 70.5917493  117.79253365  99.70466508] {'conversion': np.float64(0.001), 'resolution': np.float64(-1.0), 'unit': 'meters'}
finger_vel (649100, 2) [300 300] [-493.14284781 -334.41491273] [470.87494072 350.91538377] {'conversion': np.float64(0.001), 'resolution': np.float64(-1.0), 'unit': 'm/s'}
target_pos (649100, 2) [300 300] [-52.5   7.5] [ 52.5 112.5] {'conversion': np.float64(0.001), 'resolution': np.float64(-1.0), 'unit': 'meters'}
[[-4.35769473 56.75806327]
 [-4.35647098 56.75569649]
 [-4.35522247 56.75329688]
 [-4.35394982 56.75086523]
 [-4.35265365 56.74840232]
 [-4.35133457 56.74590894]
 [-4.34999318 56.7433859 ]
 [-4.34863008 56.74083398]
 [-4.34724588 56.73825398]
 [-4.34584115 5
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p entries/000129-makin-2018; date -u
```

```
Wed Oct 28 19:04:41 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "entries/000129-makin-2018/makin.py",
 "content": "\"\"\"Loading and decoders for Makin, O'Doherty, Cardoso & Sabes (2018) on dandiset 000129.\n\nWhere each choice comes from is marked in the docstrings:\n  [claims]  the criterion or the header of claims/000129/10.1088-1741-2552-aa9e95.yaml\n  [paper]   a passage of the paper (Methods unless said otherwise)\n  [code]    the paper's code, https://github.com/jgmakin/rbmish at commit 700062f5\n  [assumed] an assumption, with the reason\n  [standard] a standard choice for a detail that cannot change a result\n\nThe dandiset holds one session of monkey I (Indy, M1 array only). Its training file\nholds 649.1 s of spikes and kinematics; its test file holds spikes only (the Neural\nLatents Benchmark withholds the behaviour), so only the training file is used.\n\"\"\"\nimport os\n\nimport h5py\nimport numpy as np\nimport remfile\nimport requests\nfrom scipy.signal import butter, filtfilt\n\nDANDISET = \"000129\"\nVERSION = \"0.241017.1444\"\nTRAIN_ASSET = \"sub-Indy/sub-Indy_desc-train_behavior+ecephys.nwb\"\nTEST_ASSET = \"sub-Indy/sub-Indy_desc-test_ecephys.nwb\"\nFS_KIN = 250.0  # [paper] Polhemus sampled at 250 Hz; the file upsampled it to 1 kHz\nVARS = [\"x\", \"y\", \"vx\", \"vy\", \"ax\", \"ay\"]\nDECODERS = [\"linear\", \"kfobs\", \"kflatent\", \"kflatent_kf\", \"wf\", \"ukf\", \"refh\", \"refh_kf\"]\n\n\ndef asset_url(path, version=VERSION):\n    r = requests.get(\n        f\"https://api.dandiarchive.org/api/dandisets/{DANDISET}/versions/{version}/assets/\",\n        params={\"path\": path},\n    )\n    r.raise_for_status()\n    aid = [a for a in r.json()[\"results\"] if a[\"path\"] == path][0][\"asset_id\"]\n    return f\"https://api.dandiarchive.org/api/assets/{aid}/download/\"\n\n\ndef open_asset(path):\n    return h5py.File(remfile.File(asset_url(path)), \"r\")\n\n\ndef load_session():\n    \"\"\"Stream the training file: spike times per unit, unit ids, and kinematics at 1 kHz.\"\"\"\n    f = open_asset(TRAIN_ASSET)\n    u = f[\"units\"]\n    ids = u[\"id\"][:]\n    st = u[\"spike_times\"][:]\n    idx = u[\"spike_times_index\"][:]\n    spikes = np.split(st, idx[:-1])\n    heldout = u[\"heldout\"][:].astype(bool)\n    b = f[\"processing/behavior\"]\n    d = {\n        \"unit_ids\": ids,\n        \"heldout\": heldout,\n        \"spikes\": spikes,\n        \"finger_pos\": b[\"finger_pos\"][\"data\"][:, :2],\n        \"cursor_pos\": b[\"cursor_pos\"][\"data\"][:],\n        \"target_pos\": b[\"target_pos\"][\"data\"][:],\n        \"rate\": float(b[\"finger_pos\"][\"rate\"][()]) if \"rate\" in b[\"finger_pos\"] else 1000.0,\n        \"conversion\": float(b[\"finger_pos\"][\"data\"].attrs[\"conversion\"]),\n        \"unit\": b[\"finger_pos\"][\"data\"].attrs[\"unit\"],\n        \"session_description\": f[\"session_description\"][()].decode(),\n        \"session_start_time\": f[\"session_start_time\"][()].decode(),\n        \"trials_split\": f[\"intervals/trials/split\"][:].astype(str),\n        \"trials_start\": f[\"intervals/trials/start_time\"][:],\n    }\n    st_rate = b[\"finger_pos\"].get(\"starting_time\")\n    d[\"t0\"] = float(st_rate[()]) if st_rate is not None else 0.0\n    if \"rate\" in b[\"finger_pos\"][\"starting_time\"].attrs:\n        d[\"rate\"] = float(b[\"finger_pos\"][\"starting_time\"].attrs[\"rate\"])\n    f.close()\n    return d\n\n\ndef segments(valid):\n    \"\"\"Start and stop indices of runs of True.\"\"\"\n    v = np.r_[False, valid, False].astype(int)\n    starts = np.where(np.diff(v) == 1)[0]\n    stops = np.where(np.diff(v) == -1)[0]\n    return list(zip(starts, stops))\n\n\ndef kinematics(pos_1k, reading=\"methods\"):\n    \"\"\"Position, velocity and acceleration at 250 Hz from the 1 kHz series.\n\n    reading \"methods\" [paper, Data acquisition]: fingertip position low-pass filtered\n    non-causally (4th-order Butterworth, 10 Hz), then velocity and acceleration as\n    differences times the sampling rate. reading \"code\" [code, getLatentsBMI.m]: no\n    filter. Either way the 1 kHz series is taken back to 250 Hz by keeping every 4th\n    sample [assumed: the file says the 250 Hz record was upsampled]. Each run of valid\n    samples between the file's NaN gaps is treated separately; the last difference is\n    repeated as in the code [code, getLatentsBMI.m], and the samples lost at a gap are NaN.\n    \"\"\"\n    p = pos_1k[::4].astype(float)\n    out = np.full((len(p), 6), np.nan)\n    valid = ~np.isnan(p).any(1)\n    bb, aa = butter(4, 10.0 / (FS_KIN / 2))\n    for s, e in segments(valid):\n        seg = p[s:e]\n        if reading == \"methods\":\n            seg = filtfilt(bb, aa, seg, axis=0)\n        v = np.diff(seg, axis=0) * FS_KIN\n        v = np.vstack([v, v[-1:]])\n        a = np.diff(v, axis=0) * FS_KIN\n        a = np.vstack([a, a[-1:]])\n        out[s:e] = np.hstack([seg, v, a])\n    return out\n\n\ndef bin_data(d, bin_ms=64, reading=\"methods\"):\n    \"\"\"Spike counts in non-overlapping bins from the first kinematic time stamp, and the\n    kinematic state per bin.\n\n    [code, binSpikeCounts.m] bins start at the first kinematic sample. The state is the\n    last 250 Hz sample of each bin for the Methods reading (\"subsampled\" [paper];\n    [claims] header: the last sample is the main choice) and the mean over the bin for\n    the code's reading [code]. A bin whose samples include a NaN gap gets NaN kinematics\n    and is left out of fitting and scoring (a deviation; 3 gaps of 0.1 s in the file).\n    \"\"\"\n    pos = d[\"finger_pos\"] if reading == \"methods\" else d[\"cursor_pos\"]\n    k = kinematics(pos, reading)\n    m = int(round(FS_KIN * bin_ms / 1000))\n    nb = len(k) // m\n    kk = k[: nb * m].reshape(nb, m, 6)\n    X = kk[:, -1, :] if reading == \"methods\" else kk.mean(1)\n    X[np.isnan(kk).any((1, 2))] = np.nan\n    edges = d[\"t0\"] + np.arange(nb + 1) * bin_ms / 1000.0\n    R = np.stack([np.histogram(s, edges)[0] for s in d[\"spikes\"]], 1).astype(float)\n    return R, X, edges\n\n\ndef unit_filter(R, bin_ms, ntrain):\n    \"\"\"[code, getLatentsBMI.m] drop units with mean rate <= 0.5 Hz over the session or no\n    spikes, then units whose binned counts duplicate another unit's over the training or\n    the test part. Returns a boolean mask over units.\"\"\"\n    rate = R.mean(0) / (bin_ms / 1000.0)\n    keep = (rate > 0.5) & (R.sum(0) > 0)\n    idx = np.where(keep)[0]\n    dup = set()\n    for part in (R[:ntrain], R[ntrain:]):\n        P = part[:, idx]\n        for i in range(len(idx)):\n            for j in range(i + 1, len(idx)):\n                if np.array_equal(P[:, i], P[:, j]):\n                    dup.add(idx[j])\n    keep[list(dup)] = False\n    return keep\n\n\n# ---------------------------------------------------------------- scores\n\ndef rsq(Xhat, X):\n    \"\"\"[claims] R2 = 1 - SSerr/SStot per variable, SStot about the test mean.\"\"\"\n    return 1 - ((Xhat - X) ** 2).sum(0) / ((X - X.mean(0)) ** 2).sum(0)\n\n\ndef snr(r2):\n    \"\"\"[paper, Results] SNR = -10 log10(1 - R2), in dB.\"\"\"\n    return -10 * np.log10(1 - np.asarray(r2))\n\n\n# ---------------------------------------------------------------- linear-Gaussian tools\n\ndef ridge(F, Y, lam=0.0, intercept=True):\n    \"\"\"Least squares of Y on F (with a column of ones); lam adds lam*I to F'F as in\n    [code, tools/linregress.m] (the intercept is penalized there too when it is a column).\"\"\"\n    if intercept:\n        F = np.hstack([F, np.ones((len(F), 1))])\n    G = F.T @ F + lam * np.eye(F.shape[1])\n    return np.linalg.solve(G, F.T @ Y)\n\n\ndef apply(B, F):\n    return np.hstack([F, np.ones((len(F), 1))]) @ B\n\n\ndef learn_lds(Z, Y):\n    \"\"\"Fully observed LGDS by regression [paper, KFobs]: state on its predecessor, and\n    observations on the state, each with an intercept; initial cumulants from every time\n    point [paper]. Z and Y are lists of contiguous runs (bins with NaN kinematics split runs).\"\"\"\n    Zp = np.vstack([z[:-1] for z in Z])\n    Zf = np.vstack([z[1:] for z in Z])\n    Ba = ridge(Zp, Zf)\n    A, a = Ba[:-1].T, Ba[-1]\n    Qz = np.cov((Zf - apply(Ba, Zp)).T, bias=True)\n    Za, Ya = np.vstack(Z), np.vstack(Y)\n    Bc = ridge(Za, Ya)\n    C, c = Bc[:-1].T, Bc[-1]\n    Rr = np.cov((Ya - apply(Bc, Za)).T, bias=True)\n    return dict(A=A, a=a, Q=np.atleast_2d(Qz), C=C, c=c, R=np.atleast_2d(Rr),\n                mu0=Za.mean(0), S0=np.cov(Za.T))\n\n\ndef kalman_filter(p, Y):\n    \"\"\"Kalman filter, equation (2) of the paper, in information form for the update\n    (exact; it only avoids inverting the observation covariance at each step).\"\"\"\n    A, a, Q, C, c, R = p[\"A\"], p[\"a\"], p[\"Q\"], p[\"C\"], p[\"c\"], p[\"R\"]\n    Ri = np.linalg.inv(R)\n    CtRi = C.T @ Ri\n    CtRiC = CtRi @ C\n    n = A.shape[0]\n    out = np.empty((len(Y), n))\n    m, S = p[\"mu0\"], p[\"S0\"]\n    for t in range(len(Y)):\n        if t > 0:\n            m = A @ m + a\n            S = A @ S @ A.T + Q\n        Si = np.linalg.inv(S)\n        Sp = np.linalg.inv(Si + CtRiC)\n        m = Sp @ (Si @ m + CtRi @ (Y[t] - c))\n        S = Sp\n        out[t] = m\n    return out\n\n\n# ---------------------------------------------------------------- data split\n\nclass Split:\n    \"\"\"Training and test bins [paper, Training and testing data]: train on the first\n    `train_s` seconds, test on the rest of the session. Bins with NaN kinematics are kept\n    in the spike sequence (filters run through them) and left out of fitting and scoring.\"\"\"\n\n    def __init__(self, R, X, bin_ms, train_s=320.0, test_start_s=320.0):\n        n_tr = int(np.floor(train_s / (bin_ms / 1000.0)))\n        n_te0 = int(np.floor(test_start_s / (bin_ms / 1000.0)))\n        self.bin_ms = bin_ms\n        self.Rtr, self.Xtr = R[:n_tr], X[:n_tr]\n        self.Rte, self.Xte = R[n_te0:], X[n_te0:]\n        self.oktr = ~np.isnan(self.Xtr).any(1)\n        self.okte = ~np.isnan(self.Xte).any(1)\n\n    def runs(self, A, ok):\n        return [A[s:e] for s, e in segments(ok) if e - s > 2]\n\n    def score(self, Xhat):\n        return rsq(Xhat[self.okte], self.Xte[self.okte])\n\n\ndef dynamic_map(sp, Xhat_tr, Xhat_te):\n    \"\"\"[paper, Decoding the latent-state models, eq. 10] a KF whose observations are the\n    six static reconstructions, fit by regression on the training data like KFobs.\"\"\"\n    p = learn_lds(sp.runs(sp.Xtr, sp.oktr), sp.runs(Xhat_tr, sp.oktr))\n    return kalman_filter(p, Xhat_te)\n\n\n# ---------------------------------------------------------------- decoders\n\ndef dec_linear(sp):\n    \"\"\"[paper, Results, decoder 1] static linear map on the current bin, with intercept\n    [code, staticLinearDecoder].\"\"\"\n    B = ridge(sp.Rtr[sp.oktr], sp.Xtr[sp.oktr])\n    return apply(B, sp.Rte)\n\n\ndef dec_kfobs(sp):\n    \"\"\"[paper, KFobs] LGDS with the kinematic state as latent state, fit by regression.\"\"\"\n    p = learn_lds(sp.runs(sp.Xtr, sp.oktr), sp.runs(sp.Rtr, sp.oktr))\n    return kalman_filter(p, sp.Rte)\n\n\ndef wf_design(R, p):\n    \"\"\"Current and p-1 past bins of spike counts (zeros before the start).\"\"\"\n    T, N = R.shape\n    F = np.zeros((T, N * p))\n    for k in range(p):\n        F[k:, k * N:(k + 1) * N] = R[: T - k]\n    return F\n\n\ndef dec_wf(sp, return_choice=False):\n    \"\"\"[paper, Wiener filter; code, tools/WFDecoder.m] ridge regression on 1 to\n    round(0.4 s / bin) bins of history and penalty in {0, 800, ..., 4000}; both chosen on\n    the last 20% of the training data by the mean R2 of x and y velocity, fitted on the\n    first 80%. As in the code, the filter fitted on the 80% is the one applied to the test\n    data. The penalty is added to F'F of the uncentred design with a column of ones, as\n    in [code, linregress.m].\"\"\"\n    n = len(sp.Rtr)\n    n80 = int(np.floor(0.8 * n))\n    pmax = int(round(0.4 / (sp.bin_ms / 1000.0)))\n    best = (-np.inf, None, None, None)\n    for p in range(1, pmax + 1):\n        F = wf_design(sp.Rtr, p)\n        F1 = np.hstack([F, np.ones((n, 1))])\n        tr = np.arange(n) < n80\n        oktr = sp.oktr & tr\n        okho = sp.oktr & ~tr\n        G = F1[oktr].T @ F1[oktr]\n        FY = F1[oktr].T @ sp.Xtr[oktr]\n        for lam in np.arange(0, 4001, 800):\n            B = np.linalg.solve(G + lam * np.eye(G.shape[0]), FY)\n            r = rsq(F1[okho] @ B, sp.Xtr[okho])\n            v = r[2:4].mean()\n            if v > best[0]:\n                best = (v, p, lam, B)\n    _, p, lam, B = best\n    F = wf_design(sp.Rte, p)\n    out = np.hstack([F, np.ones((len(F), 1))]) @ B\n    return (out, p, lam) if return_choice else out\n\n\ndef ukf_features(Xs):\n    \"\"\"[paper, UKF] tuning to the six states, the magnitudes of position, velocity and\n    acceleration, and the interaction terms x xdot and y ydot.\"\"\"\n    p, v, a = Xs[..., 0:2], Xs[..., 2:4], Xs[..., 4:6]\n    return np.concatenate([\n        Xs,\n        np.linalg.norm(p, axis=-1, keepdims=True),\n        np.linalg.norm(v, axis=-1, keepdims=True),\n        np.linalg.norm(a, axis=-1, keepdims=True),\n        p[..., :1] * v[..., :1],\n        p[..., 1:2] * v[..., 1:2],\n    ], -1)\n\n\ndef dec_ukf(sp):\n    \"\"\"Unscented Kalman filter with nonlinear tuning, no taps [paper, UKF; code,\n    filtersForNeuralData.m, 'ptaps' 1, 'ftaps' 0, 'htaps' 0]. Li's UKF2 package is not\n    available here; this is a re-implementation [assumed]: linear state transition fit by\n    regression; spike counts a linear function (with intercept) of the eleven tuning\n    features, fit by least squares; full noise covariances from the residuals; the\n    standard unscented transform with weights alpha 1, beta 0, kappa 0 [standard].\"\"\"\n    Z = sp.runs(sp.Xtr, sp.oktr)\n    Zp = np.vstack([z[:-1] for z in Z])\n    Zf = np.vstack([z[1:] for z in Z])\n    Ba = ridge(Zp, Zf)\n    A, a = Ba[:-1].T, Ba[-1]\n    Q = np.cov((Zf - apply(Ba, Zp)).T, bias=True)\n    Xo, Ro = sp.Xtr[sp.oktr], sp.Rtr[sp.oktr]\n    H = ridge(ukf_features(Xo), Ro)\n    Rr = np.cov((Ro - apply(H, ukf_features(Xo))).T, bias=True)\n    Ri = np.linalg.inv(Rr)\n    n = 6\n    lam = 0.0\n    wm = np.full(2 * n + 1, 1.0 / (2 * (n + lam)))\n    wm[0] = lam / (n + lam)\n    m, S = Xo.mean(0), np.cov(Xo.T)\n    out = np.empty((len(sp.Rte), n))\n    for t in range(len(sp.Rte)):\n        if t > 0:\n            m = A @ m + a\n            S = A @ S @ A.T + Q\n        L = np.linalg.cholesky((n + lam) * S + 1e-9 * np.eye(n))\n        sig = np.vstack([m, m + L.T, m - L.T])\n        Ysig = apply(H, ukf_features(sig))\n        ym = wm @ Ysig\n        dY = Ysig - ym\n        dX = sig - m\n        Pxy = (dX * wm[:, None]).T @ dY\n        # Pyy = dY' W dY + R; solve with the Woodbury identity (low-rank plus R)\n        U = dY * np.sqrt(wm)[:, None]\n        RiU = Ri @ U.T\n        M = np.eye(2 * n + 1) + U @ RiU\n        resid = sp.Rte[t] - ym\n        Pyy_inv_resid = Ri @ resid - RiU @ np.linalg.solve(M, RiU.T @ resid)\n        Pyy_inv_PxyT = Ri @ Pxy.T - RiU @ np.linalg.solve(M, RiU.T @ Pxy.T)\n        m = m + Pxy @ Pyy_inv_resid\n        S = S - Pxy @ Pyy_inv_PxyT\n        S = (S + S.T) / 2\n        out[t] = m\n    return out\n\n\ndef factor_analysis(Y, k, n_iter=200, seed=0):\n    \"\"\"Factor analysis by EM [standard], used to initialize the LGDS EM [paper, KFlatent].\"\"\"\n    rng = np.random.default_rng(seed)\n    mu = Y.mean(0)\n    Yc = Y - mu\n    Syy = Yc.T @ Yc / len(Y)\n    C = rng.standard_normal((Y.shape[1], k)) * np.sqrt(np.diag(Syy).mean() / k)\n    psi = np.diag(Syy).copy()\n    for _ in range(n_iter):\n        Pi = 1 / psi\n        G = np.linalg.inv(np.eye(k) + (C.T * Pi) @ C)\n        beta = G @ (C.T * Pi)\n        Ezz = G + beta @ Syy @ beta.T\n        C = Syy @ beta.T @ np.linalg.inv(Ezz)\n        psi = np.maximum(np.diag(Syy - C @ beta @ Syy), 1e-6)\n    Ez = Yc @ beta.T\n    return C, mu, psi, Ez\n\n\ndef lgds_em(Y, k, max_epochs=100, tol=1e-4, seed=0):\n    \"\"\"LGDS learned by EM with diagonal state and observation noise [paper, KFlatent],\n    initialized by factor analysis; stopped when the log-likelihood gain falls below 1/100\n    of a percent of the total gain so far, or at 100 epochs [paper]. Y is one sequence.\"\"\"\n    T, N = Y.shape\n    C, c, psi, Ez = factor_analysis(Y, k, seed=seed)\n    Ba = ridge(Ez[:-1], Ez[1:])\n    A, a = Ba[:-1].T, Ba[-1]\n    Q = np.diag(np.maximum(np.var(Ez[1:] - apply(Ba, Ez[:-1]), 0), 1e-6))\n    R = psi.copy()\n    mu0, S0 = Ez.mean(0), np.cov(Ez.T)\n    lls = []\n    for ep in range(max_epochs):\n        # E step: filter (information form, diagonal R) and RTS smoother\n        Ri = 1 / R\n        CtRi = C.T * Ri\n        CtRiC = CtRi @ C\n        mf = np.empty((T, k)); Sf = np.empty((T, k, k))\n        mp = np.empty((T, k)); Spr = np.empty((T, k, k))\n        m, S = mu0, S0\n        ll = 0.0\n        for t in range(T):\n            if t > 0:\n                m = A @ m + a\n                S = A @ S @ A.T + Q\n            mp[t], Spr[t] = m, S\n            Si = np.linalg.inv(S)\n            K = Si + CtRiC\n            Sn = np.linalg.inv(K)\n            e = Y[t] - C @ m - c\n            # log-likelihood of the innovation via the matrix determinant lemma\n            CtRie = CtRi @ e\n            quad = e @ (Ri * e) - CtRie @ Sn @ CtRie\n            logdet = np.sum(np.log(R)) + np.linalg.slogdet(K)[1] + np.linalg.slogdet(S)[1]\n            ll += -0.5 * (quad + logdet + N * np.log(2 * np.pi))\n            m = Sn @ (Si @ m + CtRi @ (Y[t] - c))\n            S = Sn\n            mf[t], Sf[t] = m, S\n        lls.append(ll)\n        ms = mf.copy(); Ss = Sf.copy(); Scross = np.empty((T - 1, k, k))\n        for t in range(T - 2, -1, -1):\n            J = Sf[t] @ A.T @ np.linalg.inv(Spr[t + 1])\n            ms[t] = mf[t] + J @ (ms[t + 1] - mp[t + 1])\n            Ss[t] = Sf[t] + J @ (Ss[t + 1] - Spr[t + 1]) @ J.T\n            Scross[t] = Ss[t + 1] @ J.T  # Cov(z_{t+1}, z_t)\n        if len(lls) > 2 and (lls[-1] - lls[-2]) < tol * 1e-2 * (lls[-1] - lls[0]):\n            break\n        # M step\n        Ezz = Ss + np.einsum(\"ti,tj->tij\", ms, ms)\n        Ezz1 = Scross + np.einsum(\"ti,tj->tij\", ms[1:], ms[:-1])\n        # transition with intercept: [A a] = sum E[z_{t+1} [z_t;1]'] (sum E[[z_t;1][z_t;1]'])^-1\n        P = np.zeros((k + 1, k + 1))\n        P[:k, :k] = Ezz[:-1].sum(0); P[:k, k] = ms[:-1].sum(0); P[k, :k] = ms[:-1].sum(0); P[k, k] = T - 1\n        Mx = np.zeros((k, k + 1))\n        Mx[:, :k] = Ezz1.sum(0); Mx[:, k] = ms[1:].sum(0)\n        Aa = Mx @ np.linalg.inv(P)\n        A, a = Aa[:, :k], Aa[:, k]\n        Qfull = (Ezz[1:].sum(0) - Aa @ Mx.T) / (T - 1)\n        Q = np.diag(np.maximum(np.diag(Qfull), 1e-6))\n        P2 = np.zeros((k + 1, k + 1))\n        P2[:k, :k] = Ezz.sum(0); P2[:k, k] = ms.sum(0); P2[k, :k] = ms.sum(0); P2[k, k] = T\n        My = np.zeros((N, k + 1))\n        My[:, :k] = Y.T @ ms; My[:, k] = Y.sum(0)\n        Cc = My @ np.linalg.inv(P2)\n        C, c = Cc[:, :k], Cc[:, k]\n        R = np.maximum((np.sum(Y ** 2, 0) - np.sum(Cc * My, 1)) / T, 1e-6)\n        mu0, S0 = ms[0], Ss[0] + 1e-6 * np.eye(k)\n    return dict(A=A, a=a, Q=Q, C=C, c=c, R=np.diag(R), mu0=mu0, S0=S0), len(lls), lls\n\n\ndef dec_kflatent(sp, seed=0, return_info=False):\n    \"\"\"KFlatent [paper]: LGDS with floor(N/3) latent states learned by EM, static map D by\n    regression (with intercept) from the filtered means [paper, eq. 4], and a dynamic map\n    by a second KF [paper, eq. 10]. EM runs on the training bins as one sequence.\"\"\"\n    k = sp.Rtr.shape[1] // 3\n    p, n_ep, lls = lgds_em(sp.Rtr, k, seed=seed)\n    Ztr = kalman_filter(p, sp.Rtr)\n    Zte = kalman_filter(p, sp.Rte)\n    D = ridge(Ztr[sp.oktr], sp.Xtr[sp.oktr])\n    st_tr, st_te = apply(D, Ztr), apply(D, Zte)\n    dyn = dynamic_map(sp, st_tr, st_te)\n    if return_info:\n        return st_te, dyn, dict(epochs=n_ep, k=k, ll_first=lls[0], ll_last=lls[-1])\n    return st_te, dyn\n\n\n# ---------------------------------------------------------------- rEFH\n\ndef sigmoid(x):\n    return 1 / (1 + np.exp(-x))\n\n\nclass REFH:\n    \"\"\"Recurrent exponential-family harmonium [paper, eq. 5-8; code, RBM/EFH.m,\n    RBM/setParams.m case 'spikecounts', RBM/setLearningSchedules.m 'exp',\n    RBM/secondOrderWeightUpdate.m, RBM/dynamical/recurrentize.m].\n\n    Visible units: Nhid recurrent Bernoulli units (the previous hidden means) and N\n    Poisson spike-count units ('normal' gives the standard-normal variant of figure 8).\n    Hidden units: floor(4 N) Bernoulli. CD1; mini-batches of the same time step of 40\n    random subsequences of 1000 bins, a new batch each epoch; max(floor(Ntrain/250), 20)\n    epochs; sparsity target 0.05, cost 0.2, running estimate rate 0.95 [code, DBNtrain.m];\n    weights initialized N(0, 0.005^2), biases 0; second-order (momentum and decay)\n    updates with exponentially growing masses, mw0 = mean(muR N, 0.09 Nhid) 10000/Ntrain\n    (200 for standard-normal units), recurrent mass 110, bias masses 0.55 times weights.\n    \"\"\"\n\n    def __init__(self, n_vis, units=\"poisson\", ratio=4, seed=0):\n        self.N = n_vis\n        self.H = int(np.floor(n_vis * ratio))\n        self.units = units\n        self.rng = np.random.default_rng(seed)\n\n    def vis_mean(self, eta):\n        return np.exp(np.minimum(eta, 30)) if self.units == \"poisson\" else eta\n\n    def vis_sample(self, mu):\n        if self.units == \"poisson\":\n            return self.rng.poisson(mu).astype(float)\n        return mu + self.rng.standard_normal(mu.shape)\n\n    def fit(self, Rtrain, T=1000, ncases=40):\n        rng = self.rng\n        N, H = self.N, self.H\n        ntr = len(Rtrain)\n        T = min(T, ntr)\n        ncases = int(np.floor(40000 / T))\n        nep = max(int(np.floor(ntr / 250)), 20)\n        Ts = 0.01\n        if self.units == \"poisson\":\n            mw0 = np.mean([Rtrain.mean() * N, 0.09 * H]) * 10000 / ntr\n        else:\n            mw0 = 200.0\n        mr0 = 110.0\n        wt2b = 0.55\n        m0 = dict(w=mw0, vb=mw0 * wt2b, hb=mw0 * wt2b, rw=mr0, rb=mr0 * wt2b)\n        Nv = H + N\n        W = 0.005 * rng.standard_normal((Nv, H))\n        bh = np.zeros(H)\n        bv = np.zeros(Nv)\n        Wd = np.zeros_like(W); bhd = np.zeros_like(bh); bvd = np.zeros_like(bv)\n        cost, target, rate = 0.2, 0.05, 0.95\n        est = None\n\n        def masses(ep, key):\n            m = 1.10 ** ep * m0[key] * Ts ** 2\n            b = m0[key] / 2 * Ts\n            k = m0[key] / 500000\n            return m, b, k\n\n        def upd(w, wd, u, m, b, k):\n            mm = m / Ts\n            wd = (-k / mm) * w + (0.98 - b / mm) * wd + u / mm\n            return w + Ts * wd, wd\n\n        for ep in range(1, nep + 1):\n            i0 = np.ceil((ntr - T) * rng.random(ncases)).astype(int)\n            i0 = np.clip(i0, 0, ntr - T)\n            batch = np.stack([Rtrain[i:i + T] for i in i0], 0)  # cases x T x N\n            mw, bw, kw = masses(ep, \"w\")\n            mrw, brw, krw = masses(ep, \"rw\")\n            mvb, bvb, kvb = masses(ep, \"vb\")\n            mrb, brb, krb = masses(ep, \"rb\")\n            mhb, bhb, khb = masses(ep, \"hb\")\n            zprev = np.zeros((ncases, H))\n            for t in range(T):\n                pv = np.hstack([zprev, batch[:, t, :]])\n                ph = sigmoid(pv @ W + bh)\n                zprev = ph\n                hs = (ph > rng.random(ph.shape)).astype(float)\n                eta = hs @ W.T + bv\n                qv = np.empty_like(pv)\n                rmean = sigmoid(eta[:, :H])\n                qv[:, :H] = (rmean > rng.random(rmean.shape)).astype(float)\n                qv[:, H:] = self.vis_sample(self.vis_mean(eta[:, H:]))\n                qh = sigmoid(qv @ W + bh)\n                pW = pv.T @ hs\n                ph_s = hs.sum(0)\n                pv_s = pv.sum(0)\n                gW = pW - qv.T @ qh\n                gbh = ph_s - qh.sum(0)\n                gbv = pv_s - qv.sum(0)\n                if est is None:\n                    est = [pW, ph_s, pv_s]\n                else:\n                    est = [rate * pW + (1 - rate) * est[0], rate * ph_s + (1 - rate) * est[1],\n                           rate * pv_s + (1 - rate) * est[2]]\n                gW = gW + cost * (target * est[2][:, None] - est[0])\n                gbh = gbh + cost * (ncases * target - est[1])\n                u = gW / ncases\n                W[:H], Wd[:H] = upd(W[:H], Wd[:H], u[:H], mrw, brw, krw)\n                W[H:], Wd[H:] = upd(W[H:], Wd[H:], u[H:], mw, bw, kw)\n                bh, bhd = upd(bh, bhd, gbh / ncases, mhb, bhb, khb)\n                ub = gbv / ncases\n                bv[:H], bvd[:H] = upd(bv[:H], bvd[:H], ub[:H], mrb, brb, krb)\n                bv[H:], bvd[H:] = upd(bv[H:], bvd[H:], ub[H:], mvb, bvb, kvb)\n        self.W, self.bh, self.bv = W, bh, bv\n        self.epochs = nep\n        return self\n\n    def features(self, R):\n        \"\"\"[code, testEFHBMI.m LDSobsfxn, updownRDBN.m] run the rEFH over one sequence\n        with mean propagation; return updated spike-unit means, updated recurrent-unit\n        means and hidden means.\"\"\"\n        H = self.H\n        Z = np.empty((len(R), H))\n        z = np.zeros(H)\n        Wr, Ws = self.W[:H], self.W[H:]\n        for t in range(len(R)):\n            z = sigmoid(z @ Wr + R[t] @ Ws + self.bh)\n            Z[t] = z\n        Vs = self.vis_mean(Z @ Ws.T + self.bv[H:])\n        Vr = sigmoid(Z @ Wr.T + self.bv[:H])\n        return Vs, Vr, Z\n\n\ndef refh_decode(sp, model, Rtr, Rte, hidden_only=False):\n    \"\"\"[paper, eq. 9-10; code, filterDecoder.m] static ridge map from [updated visible\n    means, hidden means] with penalty (Nunits/Nsamples)^(10/3) [claims: exponent reading\n    of eq. 10; code], then a KF on the six static outputs. hidden_only drops the updated\n    visible units (the figure 8 variant).\"\"\"\n    out = []\n    for R in (Rtr, Rte):\n        Vs, Vr, Z = model.features(R)\n        out.append(Z if hidden_only else np.hstack([Vs, Vr, Z]))\n    Ftr, Fte = out\n    nv = Ftr.shape[1] + 1\n    lam = (nv / sp.oktr.sum()) ** (10 / 3)\n    B = ridge(Ftr[sp.oktr], sp.Xtr[sp.oktr], lam=lam)\n    st_tr, st_te = apply(B, Ftr), apply(B, Fte)\n    return st_te, dynamic_map(sp, st_tr, st_te)\n\n\ndef dec_refh(sp, seed=0, units=\"poisson\", variants=False):\n    \"\"\"Train the rEFH on the training bins and decode. units 'normal' trains the\n    standard-normal variant on transformed counts (see transform_counts).\"\"\"\n    Rtr, Rte = sp.Rtr, sp.Rte\n    if units == \"normal\":\n        Rtr, Rte = transform_counts(Rtr, Rte, units_reading=variants or \"standardize\")\n    model = REFH(Rtr.shape[1], units=units, seed=seed).fit(Rtr)\n    res = {\"refh\": None, \"refh_kf\": None}\n    res[\"refh\"], res[\"refh_kf\"] = refh_decode(sp, model, Rtr, Rte)\n    if units == \"poisson\" and variants:\n        res[\"refh_hid\"], res[\"refh_hid_kf\"] = refh_decode(sp, model, Rtr, Rte, hidden_only=True)\n    res[\"epochs\"] = model.epochs\n    return res\n\n\ndef transform_counts(Rtr, Rte, units_reading=\"standardize\"):\n    \"\"\"Inputs of the standard-normal rEFH. 'standardize' [paper, Results, Variant decoders:\n    standardized counts], z-scored with the training mean and SD; 'anscombe' [code,\n    getLatentsBMI.m] 2 sqrt(R + 3/8).\"\"\"\n    if units_reading == \"anscombe\":\n        return 2 * np.sqrt(Rtr + 3 / 8), 2 * np.sqrt(Rte + 3 / 8)\n    mu, sd = Rtr.mean(0), Rtr.std(0)\n    sd[sd == 0] = 1\n    return (Rtr - mu) / sd, (Rte - mu) / sd\n\n\ndef run_all(sp, seed, decoders=DECODERS):\n    \"\"\"Fit and test the decoders on one split; returns R2 per decoder (6 variables).\"\"\"\n    out = {}\n    if \"linear\" in decoders:\n        out[\"linear\"] = sp.score(dec_linear(sp))\n    if \"kfobs\" in decoders:\n        out[\"kfobs\"] = sp.score(dec_kfobs(sp))\n    if \"kflatent\" in decoders or \"kflatent_kf\" in decoders:\n        st, dyn = dec_kflatent(sp, seed=seed)\n        out[\"kflatent\"], out[\"kflatent_kf\"] = sp.score(st), sp.score(dyn)\n    if \"wf\" in decoders:\n        out[\"wf\"] = sp.score(dec_wf(sp))\n    if \"ukf\" in decoders:\n        out[\"ukf\"] = sp.score(dec_ukf(sp))\n    if \"refh\" in decoders or \"refh_kf\" in decoders:\n        r = dec_refh(sp, seed=seed + 1)\n        out[\"refh\"], out[\"refh_kf\"] = sp.score(r[\"refh\"]), sp.score(r[\"refh_kf\"])\n    return out\n"
}
```

```
File created successfully at: entries/000129-makin-2018/makin.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . ev/bin/activate && cat > t1.py <<'EOF'
import sys,time,pickle; sys.path.insert(0,'entries/000129-makin-2018')
import numpy as np, makin as M
t=time.time(); d=M.load_session(); print("load",time.time()-t, d['rate'], d['t0'])
pickle.dump(d,open('d.pkl','wb'))
R,X,e=M.bin_data(d,64); print(R.shape,X.shape, np.isnan(X).any(1).sum())
keep=M.unit_filter(R,64,5000); print("kept",keep.sum())
sp=M.Split(R[:,keep],X,64)
for name,fn in [("linear",M.dec_linear),("kfobs",M.dec_kfobs),("wf",M.dec_wf),("ukf",M.dec_ukf)]:
    t=time.time(); r=sp.score(fn(sp)); print(name, np.round(M.snr(r),2), np.round(r,3), round(time.time()-t,1))
t=time.time(); st,dyn,info=M.dec_kflatent(sp,return_info=True); print("kflat",np.round(M.snr(sp.score(st)),2),np.round(M.snr(sp.score(dyn)),2),info,round(time.time()-t,1))
EOF
OMP_NUM_THREADS=4 python t1.py 2>&1 | grep -v Warn
```

```
load 2.495373487472534 1000.0 0.0
(10142, 130) (10142, 6) 6
kept 111
linear [0.44 1.16 1.39 1.4  0.25 0.53] [0.096 0.234 0.274 0.275 0.055 0.116] 0.0
kfobs [4.45 5.56 3.05 3.56 0.73 1.31] [0.641 0.722 0.504 0.56  0.154 0.26 ] 0.2
wf [2.75 3.16 3.08 3.42 1.06 1.61] [0.469 0.517 0.508 0.545 0.217 0.309] 0.3
ukf [4.93 6.33 3.41 4.23 0.78 1.44] [0.678 0.767 0.544 0.622 0.165 0.282] 1.0
kflat [3.58 4.58 3.03 3.36 0.71 1.26] [3.75 4.76 3.26 3.54 0.79 1.36] {'epochs': 100, 'k': 37, 'll_first': np.float64(-347649.82225245214), 'll_last': np.float64(-338758.13202463475)} 110.7
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . ev/bin/activate && cat > t2.py <<'EOF'
import sys,time,pickle; sys.path.insert(0,'entries/000129-makin-2018')
import numpy as np, makin as M
d=pickle.load(open('d.pkl','rb'))
R,X,e=M.bin_data(d,64); keep=M.unit_filter(R,64,5000); sp=M.Split(R[:,keep],X,64)
t=time.time(); r=M.dec_refh(sp,seed=1,variants=True); print("refh time",time.time()-t, r['epochs'])
for k in ['refh','refh_kf','refh_hid','refh_hid_kf']: print(k, np.round(M.snr(sp.score(r[k])),2))
EOF
OMP_NUM_THREADS=4 python t2.py 2>&1 | grep -v Warn
```

```
refh time 92.12368726730347 20
refh [0.95 2.06 4.03 4.07 1.75 2.08]
refh_kf [5.28 6.66 4.86 5.48 2.14 2.62]
refh_hid [0.96 1.95 3.87 3.85 1.43 1.77]
refh_hid_kf [5.26 6.42 4.76 5.16 2.   2.39]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
nproc; free -g | head -2; date -u
```

```
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          12           0           2          14
Wed Oct 28 19:10:30 UTC 2026
```

**Agent**

Now I'll speed up the Kalman filters (exact steady-state reuse) and the WF sweep.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000129-makin-2018/makin.py",
 "old_string": "def kalman_filter(p, Y):\n    \"\"\"Kalman filter, equation (2) of the paper, in information form for the update\n    (exact; it only avoids inverting the observation covariance at each step).\"\"\"\n    A, a, Q, C, c, R = p[\"A\"], p[\"a\"], p[\"Q\"], p[\"C\"], p[\"c\"], p[\"R\"]\n    Ri = np.linalg.inv(R)\n    CtRi = C.T @ Ri\n    CtRiC = CtRi @ C\n    n = A.shape[0]\n    out = np.empty((len(Y), n))\n    m, S = p[\"mu0\"], p[\"S0\"]\n    for t in range(len(Y)):\n        if t > 0:\n            m = A @ m + a\n            S = A @ S @ A.T + Q\n        Si = np.linalg.inv(S)\n        Sp = np.linalg.inv(Si + CtRiC)\n        m = Sp @ (Si @ m + CtRi @ (Y[t] - c))\n        S = Sp\n        out[t] = m\n    return out",
 "new_string": "def kf_pass(A, a, Q, C, c, Ri, mu0, S0, Y, loglik=False):\n    \"\"\"Kalman filter, equation (2) of the paper, with the update in information form.\n    The covariances do not depend on the data; once the predicted covariance stops\n    changing (to 1e-13 relative) its steady-state matrices are reused, which gives the\n    same result to rounding error. Ri is the inverse observation covariance, or a vector\n    for a diagonal one. Returns filtered means, predicted means, and per-step covariances\n    (filtered, predicted) up to the step where they settle, then the settled ones.\"\"\"\n    diag = Ri.ndim == 1\n    CtRi = (C.T * Ri) if diag else C.T @ Ri\n    CtRiC = CtRi @ C\n    T, n = len(Y), A.shape[0]\n    mf = np.empty((T, n)); mp = np.empty((T, n))\n    Sf, Sp = [], []\n    m, S = mu0, S0\n    ll = 0.0\n    steady = None\n    if loglik:\n        logdetR = -np.sum(np.log(Ri)) if diag else -np.linalg.slogdet(Ri)[1]\n    for t in range(T):\n        if t > 0:\n            m = A @ m + a\n            if steady is None:\n                Snew = A @ S @ A.T + Q\n                if t > 1 and np.max(np.abs(Snew - Sp[-1])) < 1e-13 * np.max(np.abs(Snew)):\n                    steady = (Sp[-1], Si, Sn, ldK)\n                S = Snew\n        mp[t] = m\n        if steady is None:\n            Si = np.linalg.inv(S)\n            K = Si + CtRiC\n            Sn = np.linalg.inv(K)\n            ldK = np.linalg.slogdet(K)[1] + np.linalg.slogdet(S)[1] if loglik else 0.0\n            Sp.append(S); Sf.append(Sn)\n        else:\n            _, Si, Sn, ldK = steady\n        e = Y[t] - c\n        if loglik:\n            r = e - C @ m\n            CtRir = CtRi @ r\n            q = (r @ (Ri * r) if diag else r @ Ri @ r) - CtRir @ Sn @ CtRir\n            ll += -0.5 * (q + logdetR + ldK + len(r) * np.log(2 * np.pi))\n        m = Sn @ (Si @ m + CtRi @ e)\n        S = Sn\n        mf[t] = m\n    return mf, mp, Sf, Sp, ll\n\n\ndef kalman_filter(p, Y):\n    \"\"\"Filtered means of the LGDS p for observations Y.\"\"\"\n    R = p[\"R\"]\n    Ri = 1 / np.diag(R) if p.get(\"diagR\") else np.linalg.inv(R)\n    return kf_pass(p[\"A\"], p[\"a\"], p[\"Q\"], p[\"C\"], p[\"c\"], Ri, p[\"mu0\"], p[\"S0\"], Y)[0]"
}
```

```
The file entries/000129-makin-2018/makin.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000129-makin-2018/makin.py",
 "old_string": "    for ep in range(max_epochs):\n        # E step: filter (information form, diagonal R) and RTS smoother\n        Ri = 1 / R\n        CtRi = C.T * Ri\n        CtRiC = CtRi @ C\n        mf = np.empty((T, k)); Sf = np.empty((T, k, k))\n        mp = np.empty((T, k)); Spr = np.empty((T, k, k))\n        m, S = mu0, S0\n        ll = 0.0\n        for t in range(T):\n            if t > 0:\n                m = A @ m + a\n                S = A @ S @ A.T + Q\n            mp[t], Spr[t] = m, S\n            Si = np.linalg.inv(S)\n            K = Si + CtRiC\n            Sn = np.linalg.inv(K)\n            e = Y[t] - C @ m - c\n            # log-likelihood of the innovation via the matrix determinant lemma\n            CtRie = CtRi @ e\n            quad = e @ (Ri * e) - CtRie @ Sn @ CtRie\n            logdet = np.sum(np.log(R)) + np.linalg.slogdet(K)[1] + np.linalg.slogdet(S)[1]\n            ll += -0.5 * (quad + logdet + N * np.log(2 * np.pi))\n            m = Sn @ (Si @ m + CtRi @ (Y[t] - c))\n            S = Sn\n            mf[t], Sf[t] = m, S\n        lls.append(ll)\n        ms = mf.copy(); Ss = Sf.copy(); Scross = np.empty((T - 1, k, k))\n        for t in range(T - 2, -1, -1):\n            J = Sf[t] @ A.T @ np.linalg.inv(Spr[t + 1])\n            ms[t] = mf[t] + J @ (ms[t + 1] - mp[t + 1])\n            Ss[t] = Sf[t] + J @ (Ss[t + 1] - Spr[t + 1]) @ J.T\n            Scross[t] = Ss[t + 1] @ J.T  # Cov(z_{t+1}, z_t)",
 "new_string": "    for ep in range(max_epochs):\n        # E step: filter (information form, diagonal R) and RTS smoother\n        mf, mp, Sf, Spr, ll = kf_pass(A, a, Q, C, c, 1 / R, mu0, S0, Y, loglik=True)\n        lls.append(ll)\n        nS = len(Sf)\n        Jl = [Sf[t] @ A.T @ np.linalg.inv(Spr[t + 1]) for t in range(min(nS - 1, T - 1))]\n        Jss = Sf[-1] @ A.T @ np.linalg.inv(Spr[-1])\n        ms = mf.copy(); Ss = np.empty((T, k, k)); Scross = np.empty((T - 1, k, k))\n        Ss[T - 1] = Sf[min(T - 1, nS - 1)]\n        for t in range(T - 2, -1, -1):\n            J = Jl[t] if t < len(Jl) else Jss\n            Sft = Sf[min(t, nS - 1)]\n            Spt = Spr[min(t + 1, nS - 1)]\n            ms[t] = mf[t] + J @ (ms[t + 1] - mp[t + 1])\n            Ss[t] = Sft + J @ (Ss[t + 1] - Spt) @ J.T\n            Scross[t] = Ss[t + 1] @ J.T  # Cov(z_{t+1}, z_t)"
}
```

```
The file entries/000129-makin-2018/makin.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000129-makin-2018/makin.py",
 "old_string": "        G = F1[oktr].T @ F1[oktr]\n        FY = F1[oktr].T @ sp.Xtr[oktr]\n        for lam in np.arange(0, 4001, 800):\n            B = np.linalg.solve(G + lam * np.eye(G.shape[0]), FY)",
 "new_string": "        G = F1[oktr].T @ F1[oktr]\n        FY = F1[oktr].T @ sp.Xtr[oktr]\n        w, V = np.linalg.eigh(G)\n        VFY = V.T @ FY\n        for lam in np.arange(0, 4001, 800):\n            B = V @ (VFY / (w + lam)[:, None])"
}
```

```
The file entries/000129-makin-2018/makin.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . ev/bin/activate && cat > t3.py <<'EOF'
import sys,time,pickle; sys.path.insert(0,'entries/000129-makin-2018')
import numpy as np, makin as M
d=pickle.load(open('d.pkl','rb'))
for bm in [64,16]:
    R,X,e=M.bin_data(d,bm); keep=M.unit_filter(R,bm,int(320000/bm)); sp=M.Split(R[:,keep],X,bm)
    for name,fn in [("kfobs",M.dec_kfobs),("wf",M.dec_wf),("ukf",M.dec_ukf)]:
        t=time.time(); r=sp.score(fn(sp)); print(bm,name, np.round(M.snr(r),2), round(time.time()-t,1))
    t=time.time(); st,dyn,info=M.dec_kflatent(sp,return_info=True); print(bm,"kflat",np.round(M.snr(sp.score(st)),2),np.round(M.snr(sp.score(dyn)),2),info,round(time.time()-t,1))
EOF
OMP_NUM_THREADS=4 python t3.py 2>&1 | grep -v Warn
```

```
64 kfobs [4.45 5.56 3.05 3.56 0.73 1.31] 0.1
64 wf [2.75 3.16 3.08 3.42 1.06 1.61] 0.3
64 ukf [4.93 6.33 3.41 4.23 0.78 1.44] 1.0
64 kflat [3.58 4.58 3.03 3.36 0.71 1.26] [3.75 4.76 3.26 3.54 0.79 1.36] {'epochs': 100, 'k': 37, 'll_first': np.float64(-347649.822252452), 'll_last': np.float64(-338758.1320246348)} 32.9
16 kfobs [3.16 5.09 2.08 2.95 0.04 0.89] 0.2
16 wf [2.83 3.42 3.13 3.47 1.12 1.66] 44.3
16 ukf [3.5  5.86 2.08 3.56 0.07 0.93] 3.7
16 kflat [0.87 2.88 1.95 2.44 0.25 0.65] [ 2.46  4.14  2.38  2.83 -0.27  0.53] {'epochs': 100, 'k': 37, 'll_first': np.float64(186808.56260584548), 'll_last': np.float64(212058.1793206255)} 112.2
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/000129-makin-2018 && python3 - <<'EOF'
s=open('makin.py').read()
s=s.replace("""        Nv = H + N
        W = 0.005 * rng.standard_normal((Nv, H))
        bh = np.zeros(H)
        bv = np.zeros(Nv)""","""        Nv = H + N
        f32 = np.float32  # single precision for speed [standard]
        W = (0.005 * rng.standard_normal((Nv, H))).astype(f32)
        bh = np.zeros(H, f32)
        bv = np.zeros(Nv, f32)
        Rtrain = Rtrain.astype(f32)""")
s=s.replace("""            zprev = np.zeros((ncases, H))
            for t in range(T):""","""            zprev = np.zeros((ncases, H), f32)
            for t in range(T):""")
s=s.replace("""                hs = (ph > rng.random(ph.shape)).astype(float)""","""                hs = (ph > rng.random(ph.shape, f32)).astype(f32)""")
s=s.replace("""                qv[:, :H] = (rmean > rng.random(rmean.shape)).astype(float)""","""                qv[:, :H] = rmean > rng.random(rmean.shape, f32)""")
s=s.replace("""            return self.rng.poisson(mu).astype(float)
        return mu + self.rng.standard_normal(mu.shape)""","""            return self.rng.poisson(mu).astype(mu.dtype)
        return mu + self.rng.standard_normal(mu.shape, mu.dtype)""")
s=s.replace("""        self.W, self.bh, self.bv = W, bh, bv
        self.epochs""","""        self.W, self.bh, self.bv = W.astype(float), bh.astype(float), bv.astype(float)
        self.epochs""")
open('makin.py','w').write(s)
EOF
grep -n "def masses" -A8 makin.py | head -3; cd $TMPDIR && . ev/bin/activate && OMP_NUM_THREADS=4 python t2.py 2>&1 | grep -v Warn
```

```
548:        def masses(ep, key):
549-            m = 1.10 ** ep * m0[key] * Ts ** 2
550-            b = m0[key] / 2 * Ts
refh time 85.37076783180237 20
refh [0.94 2.08 3.87 4.09 1.71 2.08]
refh_kf [5.34 6.4  4.83 5.35 2.11 2.55]
refh_hid [0.94 2.01 3.76 3.89 1.48 1.95]
refh_hid_kf [5.35 6.38 4.72 5.01 1.99 2.48]
Shell cwd was reset to
```

**Agent calls Read**

```json
{
 "file_path": "entries/000129-makin-2018/makin.py",
 "offset": 540,
 "limit": 70
}
```

```
540	        W = (0.005 * rng.standard_normal((Nv, H))).astype(f32)
541	        bh = np.zeros(H, f32)
542	        bv = np.zeros(Nv, f32)
543	        Rtrain = Rtrain.astype(f32)
544	        Wd = np.zeros_like(W); bhd = np.zeros_like(bh); bvd = np.zeros_like(bv)
545	        cost, target, rate = 0.2, 0.05, 0.95
546	        est = None
547	
548	        def masses(ep, key):
549	            m = 1.10 ** ep * m0[key] * Ts ** 2
550	            b = m0[key] / 2 * Ts
551	            k = m0[key] / 500000
552	            return m, b, k
553	
554	        def upd(w, wd, u, m, b, k):
555	            mm = m / Ts
556	            wd = (-k / mm) * w + (0.98 - b / mm) * wd + u / mm
557	            return w + Ts * wd, wd
558	
559	        for ep in range(1, nep + 1):
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000129-makin-2018 && python3 - <<'EOF'
s=open('makin.py').read()
old=s[s.index("            mw, bw, kw = masses(ep, \"w\")"):s.index("        self.W, self.bh, self.bv = W.astype")]
new='''            mw, bw, kw = masses(ep, "w")
            mrw, brw, krw = masses(ep, "rw")
            mvb, bvb, kvb = masses(ep, "vb")
            mrb, brb, krb = masses(ep, "rb")
            mhb, bhb, khb = masses(ep, "hb")
            # per-row coefficients of the second-order update (recurrent rows, then spike rows)
            rows = lambda r, s_: np.r_[np.full(H, r), np.full(N, s_)].astype(f32)
            cWk, cWd, cWu = (rows(-krw / (mrw / Ts), -kw / (mw / Ts))[:, None],
                             rows(0.98 - brw / (mrw / Ts), 0.98 - bw / (mw / Ts))[:, None],
                             rows(1 / (mrw / Ts), 1 / (mw / Ts))[:, None] / ncases)
            cvk, cvd, cvu = (cWk[:, 0], cWd[:, 0],
                             rows(1 / (mrb / Ts), 1 / (mvb / Ts)) / ncases)
            cvk = rows(-krb / (mrb / Ts), -kvb / (mvb / Ts))
            cvd = rows(0.98 - brb / (mrb / Ts), 0.98 - bvb / (mvb / Ts))
            mmh = mhb / Ts
            zprev = np.zeros((ncases, H), f32)
            for t in range(T):
                pv = np.hstack([zprev, batch[:, t, :]])
                ph = sigmoid(pv @ W + bh)
                zprev = ph
                hs = (ph > rng.random(ph.shape, f32)).astype(f32)
                eta = hs @ W.T + bv
                qv = np.empty_like(pv)
                rmean = sigmoid(eta[:, :H])
                qv[:, :H] = rmean > rng.random(rmean.shape, f32)
                qv[:, H:] = self.vis_sample(self.vis_mean(eta[:, H:]))
                qh = sigmoid(qv @ W + bh)
                pW = pv.T @ hs
                ph_s = hs.sum(0)
                pv_s = pv.sum(0)
                gW = pW - qv.T @ qh
                gbh = ph_s - qh.sum(0)
                gbv = pv_s - qv.sum(0)
                if est is None:
                    est = [pW.copy(), ph_s.copy(), pv_s.copy()]
                else:
                    est[0] *= (1 - rate); est[0] += rate * pW
                    est[1] = rate * ph_s + (1 - rate) * est[1]
                    est[2] = rate * pv_s + (1 - rate) * est[2]
                gW += cost * target * est[2][:, None]
                gW -= cost * est[0]
                gbh = gbh + cost * (ncases * target - est[1])
                # wdot <- -k/m w + (0.98 - b/m) wdot + u/m ;  w <- w + Ts wdot  [code]
                Wd *= cWd; Wd += cWk * W; Wd += cWu * gW
                W += Ts * Wd
                bhd = (-khb / mmh) * bh + (0.98 - bhb / mmh) * bhd + gbh / ncases / mmh
                bh = bh + Ts * bhd
                bvd = cvk * bv + cvd * bvd + cvu * gbv
                bv = bv + Ts * bvd
'''
s=s.replace(old,new)
s=s.replace('''        def upd(w, wd, u, m, b, k):
            mm = m / Ts
            wd = (-k / mm) * w + (0.98 - b / mm) * wd + u / mm
            return w + Ts * wd, wd

''','')
open('makin.py','w').write(s)
EOF
cd $TMPDIR && . ev/bin/activate && OMP_NUM_THREADS=4 python t2.py 2>&1 | grep -v Warn
```

```
refh time 87.68132662773132 20
refh [0.9  2.02 3.9  3.84 1.73 2.08]
refh_kf [5.21 6.6  4.86 5.26 2.13 2.58]
refh_hid [0.92 1.94 3.79 3.71 1.44 1.78]
refh_hid_kf [5.14 6.45 4.77 5.04 1.95 2.28]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . ev/bin/activate && cat > t4.py <<'EOF'
import sys,time,pickle; sys.path.insert(0,'entries/000129-makin-2018')
import numpy as np, makin as M, cProfile, pstats
d=pickle.load(open('d.pkl','rb'))
R,X,e=M.bin_data(d,64); keep=M.unit_filter(R,64,5000); sp=M.Split(R[:,keep],X,64)
m=M.REFH(111,seed=0)
Rt=sp.Rtr[:1250]
t=time.time(); m.fit(Rt); print("fit 1250 (20 ep)", time.time()-t)
t=time.time(); m.features(sp.Rtr); print("feat", time.time()-t)
cProfile.run('m.fit(Rt)','prof'); pstats.Stats('prof').sort_stats('tottime').print_stats(8)
EOF
OMP_NUM_THREADS=4 python t4.py 2>&1 | grep -v Warn | head -40
```

```
fit 1250 (20 ep) 86.00672125816345
feat 0.33875370025634766
Wed Oct 28 19:20:47 2026    prof

         865174 function calls in 86.102 seconds

   Ordered by: internal time
   List reduced from 62 to 8 due to restriction <8>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1   68.949   68.949   86.101   86.101 entries/000129-makin-2018/makin.py:523(fit)
    60000   10.583    0.000   10.583    0.000 entries/000129-makin-2018/makin.py:490(sigmoid)
    20000    3.236    0.000    3.652    0.000 entries/000129-makin-2018/makin.py:518(vis_sample)
    20000    1.005    0.000    1.005    0.000 entries/000129-makin-2018/makin.py:515(vis_mean)
   120002    0.808    0.000    0.808    0.000 {method 'reduce' of 'numpy.ufunc' objects}
    20000    0.762    0.000    0.872    0.000 /tmp/claude-1001/ev/lib/python3.13/site-packages/numpy/_core/shape_base.py:293(hstack)
    40145    0.208    0.000    0.208    0.000 {method 'astype' of 'numpy.ndarray' objects}
    40000    0.116    0.000    0.235    0.000 /tmp/claude-1001/ev/lib/python3.13/site-packages/numpy/_core/fromnumeric.py:86(_wrapreduction_any_all)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . ev/bin/activate && cat > t5.py <<'EOF'
import numpy as np,time
W=np.random.rand(555,444).astype(np.float32); pv=np.random.rand(40,555).astype(np.float32); hs=np.random.rand(40,444).astype(np.float32)
for name,f in [("pv@W",lambda: pv@W),("hs@W.T",lambda: hs@W.T),("pv.T@hs",lambda: pv.T@hs),("elem",lambda: W*0.5+W),("sig",lambda: 1/(1+np.exp(-hs)))]:
    t=time.time(); [f() for _ in range(1000)]; print(name,(time.time()-t))
np.show_config()
EOF
for n in 1 4; do echo threads $n; OMP_NUM_THREADS=$n OPENBLAS_NUM_THREADS=$n python t5.py 2>&1 | head -5; done
```

```
threads 1
/tmp/claude-1001/ev/lib/python3.13/site-packages/numpy/__config__.py:155: UserWarning: Install `pyyaml` for better output
  warnings.warn("Install `pyyaml` for better output", stacklevel=1)
pv@W 0.28417158126831055
hs@W.T 0.3075423240661621
pv.T@hs 0.708688497543335
threads 4
/tmp/claude-1001/ev/lib/python3.13/site-packages/numpy/__config__.py:155: UserWarning: Install `pyyaml` for better output
  warnings.warn("Install `pyyaml` for better output", stacklevel=1)
pv@W 0.1968371868133545
hs@W.T 0.20496749877929688
pv.T@hs 0.5070338249206543
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json; nb=json.load(open('entries/001453-fouke-2025/reproduce_fouke_2025.ipynb'))
print(nb['metadata'])
for c in nb['cells'][:6]: print(c['cell_type'], c.get('metadata'), ''.join(c['source'])[:300].replace('\n',' | '))
print([c.get('metadata',{}).get('tags') for c in nb['cells']])
"; cat entries/001453-fouke-2025/README.md | head -30; sed -n 1,60p tools/entry.py | head -80
```

```
{'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}}
markdown {} # Reproducing Fouke et al. (2025) from dandiset 001453 |  | **Paper.** Fouke KE, He Z, Loring MD, Naumann EA (2025). Neural circuits underlying divergent | visuomotor strategies of zebrafish and *Danionella cerebrum*. *Current Biology*. | [doi:10.1016/j.cub.2025.04.027](https://doi.org/10.1016/j.cub.2025.04
code {} import time | import warnings |  | import matplotlib.pyplot as plt | import numpy as np | import pandas as pd | import statsmodels.api as sm | from scipy import stats | from statsmodels.formula.api import ols | from statsmodels.stats.multicomp import pairwise_tukeyhsd |  | import omr |  | pd.set_option("display.width", 200) | 
markdown {} ## Data check |  | Each check of the metadata against the values is stated under its output.
code {'tags': ['sanity']} info = pd.DataFrame([{ |     "fish": omr.fish_key(s), "species": s["species"], "subject_id": s["subject_id"], "age": s["age"], |     "session_start": s["session_start"][:19], "frames": s["n_frames"], "tracked": s["n_tracked"], |     "frame_hz": round(s["frame_hz"], 1), "x_max": round(s["x_range"][1]), "y_
markdown {} The archive's summary says 25 subjects and lists only *Danio rerio*. The files hold 37 fish: | subject ids 0 to 11 are each used for one zebrafish and one *D. cerebrum*, so `subject_id` alone | does not identify an animal. Fish are named here by species and subject id. The 25 ZF are one fewer | than the 2
code {'tags': ['sanity']} fast = info.frame_hz > 100 | print("Files by frame rate (Methods: tracking at more than 150 Hz):") | print(pd.crosstab(info.species, np.where(fast, "128-171 Hz", "32-35 Hz")).to_string()) | dts = pd.DataFrame([{"fish": omr.fish_key(s), **{f"dt_{k}": v for k, v in s["dt_ms"].items()}} for s in sessions]) | p
[None, None, None, ['sanity'], None, ['sanity'], None, ['sanity'], None, ['sanity'], None, ['sanity'], None, ['sanity'], None, None, None, None, None, ['claim:stimu
[... 89 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i -B3 -A25 "^Seconds of data used for training" paper/*.txt | head -60; grep -n -A30 "^Number of neurons" paper/*.txt | head -50
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd entries/000129-makin-2018 && python3 - <<'EOF'
s=open('makin.py').read()
# simplify load_session rate handling
old=s[s.index('    st_rate = b["finger_pos"].get("starting_time")'):s.index('    f.close()\n    return d')]
new='''    sts = b["finger_pos"]["starting_time"]
    d["t0"] = float(sts[()])
    d["rate"] = float(sts.attrs["rate"])
'''
s=s.replace(old,new)
s=s.replace('''        "rate": float(b["finger_pos"]["rate"][()]) if "rate" in b["finger_pos"] else 1000.0,
''','')
# Split: allow scoring from a later start
s=s.replace('''    def score(self, Xhat):
        return rsq(Xhat[self.okte], self.Xte[self.okte])''','''    def score(self, Xhat, from_s=None):
        """R2 on the test bins; from_s scores only the test bins from that time on."""
        ok = self.okte.copy()
        if from_s is not None:
            ok[: max(0, int(np.floor(from_s / (self.bin_ms / 1000.0))) - self.n_te0)] = False
        return rsq(Xhat[ok], self.Xte[ok])''')
s=s.replace('''        self.bin_ms = bin_ms
''','''        self.bin_ms = bin_ms
        self.n_te0 = n_te0
''')
# run_all: return predictions too
old=s[s.index('def run_all('):]
new='''def run_all(sp, seed, decoders=DECODERS):
    """Fit the decoders on one split; returns test-set predictions per decoder. The
    stochastic fits (EM initialization, rEFH) take seeds derived from `seed`."""
    out = {}
    if "linear" in decoders:
        out["linear"] = dec_linear(sp)
    if "kfobs" in decoders:
        out["kfobs"] = dec_kfobs(sp)
    if "kflatent" in decoders or "kflatent_kf" in decoders:
        out["kflatent"], out["kflatent_kf"] = dec_kflatent(sp, seed=seed)
    if "wf" in decoders:
        out["wf"] = dec_wf(sp)
    if "ukf" in decoders:
        out["ukf"] = dec_ukf(sp)
    if "refh" in decoders or "refh_kf" in decoders:
        r = dec_refh(sp, seed=seed + 1)
        out["refh"], out["refh_kf"] = r["refh"], r["refh_kf"]
    return out


def prepare(d, bin_ms=64, reading="methods", train_s=320.0, fraction=1.0, test_start_s=None):
    """Bin, filter units [code, getLatentsBMI.m] and split. For f < 1 the first
    floor(f N) units in file order are kept after the rate filter [claims; code]."""
    R, X, _ = bin_data(d, bin_ms, reading)
    ntr = int(np.floor(train_s / (bin_ms / 1000.0)))
    keep = unit_filter(R, bin_ms, ntr)
    if fraction < 1:
        idx = np.where(keep)[0]
        keep[:] = False
        keep[idx[: int(np.floor(len(idx) * fraction))]] = True
    ts = train_s if test_start_s is None else test_start_s
    return Split(R[:, keep], X, bin_ms, train_s=train_s, test_start_s=ts)
'''
s=s.replace(old,new)
open('makin.py','w').write(s)
EOF
grep -n "fraction\|def unit_filter" makin.py | head
```

```
133:def unit_filter(R, bin_ms, ntrain):
693:def prepare(d, bin_ms=64, reading="methods", train_s=320.0, fraction=1.0, test_start_s=None):
699:    if fraction < 1:
702:        keep[idx[: int(np.floor(len(idx) * fraction))]] = True
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build_nb1.py",
 "content": "import nbformat as nbf\nimport sys\n\nOUT = sys.argv[1]\ncells = []\n\n\ndef md(s, tags=None):\n    c = nbf.v4.new_markdown_cell(s.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\ndef code(s, tags=None):\n    c = nbf.v4.new_code_cell(s.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nmd(r\"\"\"\n# Reproducing Makin et al. (2018) from dandiset 000129: decoders at 64 ms\n\n**Paper.** Makin JG, O'Doherty JE, Cardoso MMB, Sabes PN (2018). Superior arm-movement decoding\nfrom cortex with a new, unsupervised-learning algorithm. *J. Neural Eng.* 15, 026010.\n[doi:10.1088/1741-2552/aa9e95](https://doi.org/10.1088/1741-2552/aa9e95)\n\n**Dataset.** [DANDI:000129](https://dandiarchive.org/dandiset/000129/0.241017.1444) version\n0.241017.1444 (doi:10.48324/dandi.000129/0.241017.1444), \"MC_RTT\", streamed from the archive. The\npaper cites no version of the dandiset; 0.241017.1444 is the only published version (the draft\nholds the same two assets, 50,965,512 bytes, and differs only in its title), so it is pinned.\n\n**Claims.** `claims/000129/10.1088-1741-2552-aa9e95.yaml`, written from the version of record\n(main text, Methods and legends; the paper has no supplement) and the paper's code\n(github.com/jgmakin/rbmish at commit 700062f5).\n\n**What the dataset holds.** One session of monkey I (Indy), M1 array only, from the Neural Latents\nBenchmark: a training file with 649.1 s of sorted-unit spikes and kinematics, and a test file with\n190.3 s of spikes whose kinematics are withheld. The paper used 49 sessions from three monkeys.\nClaims judged on a mean over sessions are tested here on this one session (a deviation); claims\nthat need the bootstrap across the 49 sessions, or the per-session spread, cannot be tested.\n\nThis notebook covers the decoders at 64 ms bins with 320 s of training (figures 2, 4 and 8).\nThe notebook `binwidth_training_neurons.ipynb` covers bin widths, amounts of training data and\nfractions of neurons (figures 5 to 7).\n\n| Claim | Here |\n|---|---|\n| units-monkey-i | tested |\n| fig2-velocity-boost, fig2-kflatent-dynamic-little-effect, fig2-refh-static-vel-acc, fig2-position-dynamic-gain, fig2-sagittal-better, fig2-linear-worst, fig2-gross-failures | tested on one session |\n| fig4-vel-acc-every-session (per-session part), fig4-best-variable, kflatent-modest | tested on one session |\n| fig8-velocity-variants, fig8-gaussian-still-beats-ukf | tested on one session |\n| fig5-advantage-with-binwidth, fig5-derivative-order, fig7-affine-position, fig7-kinematic-model-saturates, advantage-grows-with-derivative | tested in `binwidth_training_neurons.ipynb` |\n| fig2-refh-kf-best, intro-gain-over-nearest, fig4-advantage-grows, fig4-position, fig5-vel-acc-all-bins, fig5-position-bins, fig6-training-time, fig7-vel-acc-neurons, fig7-position-neurons, fig8-position-variants, fig9-taps, static-refh-position-worse | blocked: bootstrap or regression across the paper's 49 sessions |\n| fig4-task-similar | blocked: monkey C's data and monkey I's other sessions |\n\"\"\")\n\ncode(r\"\"\"\nimport os\nos.environ.setdefault(\"OMP_NUM_THREADS\", \"4\")\nimport time\nimport numpy as np\nimport pandas as pd\nimport requests\nimport makin as M\n\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 30)\nT0 = time.time()\nd = M.load_session()\nprint(f\"dandiset {M.DANDISET} version {M.VERSION}\")\nprint(d[\"session_description\"])\nprint(\"session_start_time\", d[\"session_start_time\"])\n\"\"\")\n\nmd(\"## Data check\\n\\nEach check of the metadata against the values is stated under its output.\")\n\ncode(r\"\"\"\nids = d[\"unit_ids\"]\nn_spk = np.array([len(s) for s in d[\"spikes\"]])\ndur = len(d[\"finger_pos\"]) / d[\"rate\"]\nprint(f\"subjects 1 (Indy), sessions 1, units {len(ids)} ({d['heldout'].sum()} marked heldout by the benchmark)\")\nprint(f\"kinematics: {len(d['finger_pos'])} samples at {d['rate']:.0f} Hz from t0 = {d['t0']} s, duration {dur:.1f} s\")\nprint(\"finger_pos unit attribute:\", d[\"unit\"], \" conversion:\", d[\"conversion\"])\nfor k in [\"finger_pos\", \"cursor_pos\", \"target_pos\"]:\n    a = d[k]\n    print(f\"{k:11s} x {np.nanmin(a[:,0]):7.1f} to {np.nanmax(a[:,0]):6.1f}, y {np.nanmin(a[:,1]):6.1f} to {np.nanmax(a[:,1]):6.1f} (stored values); NaN samples {np.isnan(a[:,0]).sum()}\")\ngaps = M.segments(np.isnan(d[\"finger_pos\"][:, 0]))\nprint(\"NaN gaps (s):\", [(round(s / d['rate'], 3), round(e / d['rate'], 3)) for s, e in gaps])\nst_all = np.concatenate(d[\"spikes\"])\nprint(f\"spikes {len(st_all)}, times {st_all.min():.3f} to {st_all.max():.3f} s, sorted within units: {all(np.all(np.diff(s) >= 0) for s in d['spikes'])}\")\nin_gap = sum(((st_all >= s / d['rate']) & (st_all < e / d['rate'])).sum() for s, e in gaps)\nprint(\"spikes inside the NaN gaps:\", in_gap)\nprint(\"unit ids end in:\", sorted(set(int(i) % 100 for i in ids)), \"(channel*100 + unit; 0 would be the unsorted hash unit)\")\nprint(\"channels with units:\", len(set(int(i) // 100 for i in ids)))\nrate = n_spk / dur\nprint(f\"rates (Hz) min {rate.min():.2f}, median {np.median(rate):.2f}, max {rate.max():.2f}\")\nprint(\"trials table splits:\", pd.Series(d[\"trials_split\"]).value_counts().to_dict())\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nThe kinematic series are stored in mm with unit \"meters\" and conversion 0.001, which is\nconsistent (value times conversion gives meters); the values span about 135 by 125 mm, as an 8 by\n8 grid at 15 mm spacing needs (105 mm between outer targets, plus reach overshoot). The finger\nposition description says 250 Hz upsampled to 1 kHz; successive 1 kHz samples are never equal,\nso the upsampling interpolated, and taking every fourth sample recovers a 250 Hz series. Three\ngaps of 0.1 s are NaN in every behavioural series. The unit ids end in 1 to 4: no unsorted hash\nunit is in the file, though the paper kept one per channel (Methods, Data acquisition).\n\"\"\")\n\ncode(r\"\"\"\n# Is this one of the paper's sessions? The paper's session list (code, NeuralAnalysis/Indy_HC_Sessions.csv)\nCSV = (\"https://raw.githubusercontent.com/jgmakin/rbmish/700062f5118b0910411cf9a8f73498e22203731d/\"\n       \"NeuralAnalysis/Indy_HC_Sessions.csv\")\nsess = pd.read_csv(CSV, header=None, names=[\"date\", \"block\", \"n_reaches\", \"arrays\", \"grid\", \"use\"])\nprint(f\"{len(sess)} rows; dates {sess.date.min()} to {sess.date.max()}; rows with at least 300 reaches: {(sess.n_reaches >= 300).sum()}\")\nprint(\"2017-02-02 in the list:\", 20170202 in set(sess.date))\nprint(sess.tail(4).to_string(index=False))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nThe file dates the session 2017-02-02. The paper's session list ends on 2017-01-31 and does not\nhold that date, so the session in the dandiset is probably not one of the paper's 37 monkey I\nsessions (it could also be a misdated one; nothing in the file links it to the list). It\nmatches the paper's description of monkey I's later sessions: M1 array only, 8 by 8 grid.\n\"\"\")\n\ncode(r\"\"\"\n# Test file: spikes only (kinematics withheld), and whether it repeats any of the training file\nft = M.open_asset(M.TEST_ASSET)\ntid = ft[\"units/id\"][:]\ntst = np.split(ft[\"units/spike_times\"][:], ft[\"units/spike_times_index\"][:-1])\nprint(\"test file units:\", len(tid), \" behaviour in test file:\", \"processing\" in ft and len(ft[\"processing\"]) > 0)\nprint(f\"test file spikes {sum(len(s) for s in tst)}, span {min(s.min() for s in tst if len(s)):.2f} to {max(s.max() for s in tst if len(s)):.2f} s\")\n# duplicated recording check: runs of 4 inter-spike intervals (to 1 us) shared between the files, per unit\nidmap = {int(i): k for k, i in enumerate(ids)}\nshared = total = 0\nfor i, s in zip(tid, tst):\n    a = d[\"spikes\"][idmap[int(i)]]\n    keys = lambda x: set(map(tuple, np.round(np.lib.stride_tricks.sliding_window_view(np.diff(x), 4) * 1e6).astype(np.int64)))\n    kt = keys(s); total += len(kt); shared += len(kt & keys(a))\nprint(f\"4-ISI patterns in the test file {total}, also in the training file {shared}\")\nft.close()\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nThe test file holds 98 of the 130 units (the benchmark's held-in units) and no kinematics, so it\ncannot be scored; only the training file is used. Almost no run of four inter-spike intervals is\nshared between the files (a count near zero is what chance coincidence gives), so the test file\ndoes not repeat the training file.\n\"\"\")\n\ncode(r\"\"\"\n# Clock check: decode velocity from spike counts with the kinematics shifted in time.\nR, X, edges = M.bin_data(d, 64)\nkeep = M.unit_filter(R, 64, 5000)\nok = ~np.isnan(X).any(1)\nrows = []\nfor lag in range(-8, 9):  # kinematics at bin t+lag decoded from spikes at bin t\n    Xs = np.roll(X, -lag, axis=0)\n    okl = ok & np.roll(ok, -lag) & (np.arange(len(X)) >= 8) & (np.arange(len(X)) < len(X) - 8)\n    tr = okl & (np.arange(len(X)) < 5000); te = okl & (np.arange(len(X)) >= 5000)\n    B = M.ridge(R[tr][:, keep], Xs[tr])\n    r2 = M.rsq(M.apply(B, R[te][:, keep]), Xs[te])\n    rows.append(dict(lag_ms=lag * 64, R2_vx=r2[2], R2_vy=r2[3], R2_x=r2[0]))\nlagdf = pd.DataFrame(rows)\nprint(lagdf.round(3).to_string(index=False))\nbest = lagdf.loc[lagdf[[\"R2_vx\", \"R2_vy\"]].mean(1).idxmax(), \"lag_ms\"]\nprint(\"best lag for velocity (ms):\", best)\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nVelocity is decoded best when the kinematics lag the spikes by about one to two bins, and the\nfit falls off on both sides; the spikes lead the movement, as motor cortex does, so the spike\ntimes and the kinematics share one clock. The paper's decoders use no offset (Methods, KFobs),\nand neither does this attempt.\n\"\"\")\n\ncode(r\"\"\"\nprint(f\"bins of 64 ms: {len(X)}; training bins (first 320 s) 5000; test bins {len(X) - 5000}\")\nprint(f\"bins with NaN kinematics: {(~ok).sum()} (training {(~ok[:5000]).sum()}, test {(~ok[5000:]).sum()})\")\nrate64 = R.mean(0) / 0.064\ndup = (rate64 > 0.5).sum() - keep.sum()\nprint(f\"units: {R.shape[1]} in file, {(rate64 > 0.5).sum()} above 0.5 Hz, {dup} dropped as duplicates, {keep.sum()} used\")\nXk = X[ok]\nfor i, v in enumerate(M.VARS):\n    print(f\"{v:2s}: {Xk[:, i].min():9.1f} to {Xk[:, i].max():8.1f}  (mm, mm/s, mm/s^2); test SD {np.nanstd(X[5000:, i]):.1f}\")\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\n## Decoders at 64 ms\n\nAll eight decoders of the paper are fitted on the first 320 s and tested on the remaining 329 s\n(the Methods, \"Training and testing data\"). The decoders and where each detail comes from are in\nthe docstrings of `makin.py`. The kinematics are the Methods reading (fingertip, 10 Hz\nButterworth, last sample of each bin); the code's reading (cursor, no filter, bin means) is run\nas a variant below. Scores: R2 per variable on the test bins, and SNR = -10 log10(1 - R2) in dB.\n\"\"\")\n\ncode(r\"\"\"\ndef fit_config(seed=0, **kw):\n    sp = M.prepare(d, **kw)\n    t = time.time()\n    pred = M.run_all(sp, seed)\n    r2 = pd.DataFrame({k: sp.score(v) for k, v in pred.items()}, index=M.VARS).T.loc[M.DECODERS]\n    return sp, pred, r2, time.time() - t\n\nsp, pred, r2, secs = fit_config(seed=0)\nprint(f\"fitted in {secs:.0f} s; units {sp.Rtr.shape[1]}, training bins {len(sp.Rtr)} ({sp.oktr.sum()} scored), test bins {len(sp.Rte)} ({sp.okte.sum()} scored)\")\nsnr = M.snr(r2)\nprint(\"R2:\"); print(r2.round(3).to_string())\nprint(\"\\nSNR (dB):\"); print(snr.round(2).to_string())\n\"\"\")\n\ncode(r\"\"\"\ndef summary(snr):\n    # SNR averaged over x and y per kinematic variable (Results: summaries average x and y)\n    return pd.DataFrame({\"pos\": snr[[\"x\", \"y\"]].mean(1), \"vel\": snr[[\"vx\", \"vy\"]].mean(1),\n                         \"acc\": snr[[\"ax\", \"ay\"]].mean(1)})\nS = summary(snr)\nprint(S.round(2).to_string())\n\"\"\")\n\nmd(r\"\"\"\n### Variants run for every claim of this notebook\n\nThe rEFH and the EM of KFlatent are stochastic and the paper reports one training run per\nsession; seed 0 is the main run (a standard choice, as the claims file says). Two more rEFH\nseeds show how much a claim depends on the run. The code's kinematics (cursor position, no\nfilter, bin means) are the variant the claims file names.\n\"\"\")\n\ncode(r\"\"\"\nvariants = {}\nfor s in (1, 2):\n    sp_s = M.prepare(d)\n    t = time.time()\n    r = M.dec_refh(sp_s, seed=10 * s + 1)\n    v = r2.copy()\n    v.loc[\"refh\"], v.loc[\"refh_kf\"] = sp_s.score(r[\"refh\"]), sp_s.score(r[\"refh_kf\"])\n    variants[f\"rEFH seed {s}\"] = M.snr(v)\n    print(f\"rEFH seed {s}: {time.time() - t:.0f} s\")\nsp_c, pred_c, r2_c, secs = fit_config(seed=0, reading=\"code\")\nvariants[\"code kinematics\"] = M.snr(r2_c)\nprint(f\"code kinematics: {secs:.0f} s\")\nfor k, v in variants.items():\n    print(f\"\\n{k}, SNR averaged over x and y:\"); print(summary(v).round(2).to_string())\n\"\"\")\n\nmd(\"## units-monkey-i\\n\\n> After units firing below 0.5 Hz were discarded, monkey I's sessions had between 171 and 413 units, the range reflecting that only 7 of 37 sessions included the S1 array.\")\n\ncode(r\"\"\"\nrate_session = n_spk / dur\nn_cut = int((rate_session > 0.5).sum())\nprint(f\"units in the file {len(ids)}; above 0.5 Hz over the session {n_cut}; at or below 0.5 Hz {len(ids) - n_cut}\")\nprint(f\"criterion range 153.9 to 454.3; inside: {153.9 <= n_cut <= 454.3}\")\nprint(\"hash units in the file: 0 (no unit id ends in 00); channels with sorted units:\", len(set(int(i) // 100 for i in ids)))\nfor thr in (0.25, 0.5, 1.0):\n    print(f\"  threshold {thr} Hz: {(rate_session > thr).sum()} units\")\n\"\"\", tags=[\"claim:units-monkey-i\"])\n\nmd(\"**Result: not reproduced.** RESULT_UNITS\", tags=None)\n\n\nmd(\"## fig2-velocity-boost\\n\\n> Relative to the static linear map, the rEFH (+KF) raises velocity SNR by more than twice as much as KFobs and nearly twice as much as the UKF.\")\n\ncode(r\"\"\"\ndef velocity_boost(snr):\n    S = summary(snr)\n    g = S[\"vel\"] - S.loc[\"linear\", \"vel\"]\n    rk, ru = g[\"refh_kf\"] / g[\"kfobs\"], g[\"refh_kf\"] / g[\"ukf\"]\n    return dict(gain_refh_kf=g[\"refh_kf\"], gain_kfobs=g[\"kfobs\"], gain_ukf=g[\"ukf\"], ratio_kfobs=rk, ratio_ukf=ru,\n                kfobs_part=rk > 2, ukf_part=1.5 <= ru <= 2.2)\nrows = {\"main\": velocity_boost(snr), **{k: velocity_boost(v) for k, v in variants.items()}}\nprint(pd.DataFrame(rows).T.round(2).to_string())\n\"\"\", tags=[\"claim:fig2-velocity-boost\"])\n\nmd(\"**Result: RESULT_VB**\")\n\nmd(\"## fig2-kflatent-dynamic-little-effect\\n\\n> Adding the dynamic mapping (a second Kalman filter) to KFlatent changes its reconstruction little.\")\n\ncode(r\"\"\"\ndef kfl_dyn(snr):\n    S = summary(snr)\n    dd = S.loc[\"kflatent_kf\"] - S.loc[\"kflatent\"]\n    return {**{f\"diff_{k}\": v for k, v in dd.items()}, \"all_below_0.5\": bool((dd.abs() < 0.5).all())}\nrows = {\"main\": kfl_dyn(snr), **{k: kfl_dyn(v) for k, v in variants.items() if k == \"code kinematics\"}}\nprint(pd.DataFrame(rows).T.round(2).to_string())\nprint(\"per axis, main (dB):\"); print((snr.loc[\"kflatent_kf\"] - snr.loc[\"kflatent\"]).round(2).to_string())\n\"\"\", tags=[\"claim:fig2-kflatent-dynamic-little-effect\"])\n\nmd(\"**Result: RESULT_KFL**\")\n\nmd(\"## fig2-refh-static-vel-acc\\n\\n> Under the static mapping alone, velocity and acceleration are reconstructed better from the rEFH than from any other filter.\")\n\ncode(r\"\"\"\nOTHERS = [\"linear\", \"kfobs\", \"kflatent\", \"kflatent_kf\", \"wf\", \"ukf\"]\ndef static_refh(snr):\n    S = summary(snr)\n    out = {}\n    for v in (\"vel\", \"acc\"):\n        best = S.loc[OTHERS, v].idxmax()\n        out[f\"{v}_refh\"] = S.loc[\"refh\", v]; out[f\"{v}_best_other\"] = f\"{best} {S.loc[best, v]:.2f}\"\n        out[f\"{v}_margin\"] = S.loc[\"refh\", v] - S.loc[best, v]\n    out[\"holds\"] = bool(out[\"vel_margin\"] > 0 and out[\"acc_margin\"] > 0)\n    return out\nrows = {\"main\": static_refh(snr), **{k: static_refh(v) for k, v in variants.items()}}\nprint(pd.DataFrame(rows).T.to_string())\n\"\"\", tags=[\"claim:fig2-refh-static-vel-acc\"])\n\nmd(\"**Result: RESULT_STATIC**\")\n\nmd(\"## fig2-position-dynamic-gain\\n\\n> Position is reconstructed much more accurately from the rEFH with the dynamic than with the static mapping, by about 3 dB of SNR.\")\n\ncode(r\"\"\"\ndef pos_gain(snr):\n    S = summary(snr)\n    g = S.loc[\"refh_kf\", \"pos\"] - S.loc[\"refh\", \"pos\"]\n    return dict(static=S.loc[\"refh\", \"pos\"], dynamic=S.loc[\"refh_kf\", \"pos\"], gain=g,\n                gain_x=snr.loc[\"refh_kf\", \"x\"] - snr.loc[\"refh\", \"x\"], gain_y=snr.loc[\"refh_kf\", \"y\"] - snr.loc[\"refh\", \"y\"],\n                within_3_pm_0_5=abs(g - 3) <= 0.5)\nrows = {\"main\": pos_gain(snr), **{k: pos_gain(v) for k, v in variants.items()}}\nprint(pd.DataFrame(rows).T.round(2).to_string())\n\"\"\", tags=[\"claim:fig2-position-dynamic-gain\"])\n\nmd(\"**Result: RESULT_POSGAIN**\")\n\nmd(\"## fig2-sagittal-better\\n\\n> For each decoder and each derivative order, the sagittal (y) component is decoded better than the lateral (x) component.\")\n\ncode(r\"\"\"\ndef sagittal(snr):\n    diff = pd.DataFrame({\"pos\": snr[\"y\"] - snr[\"x\"], \"vel\": snr[\"vy\"] - snr[\"vx\"], \"acc\": snr[\"ay\"] - snr[\"ax\"]})\n    return diff, int((diff > 0).values.sum())\ndiff, n = sagittal(snr)\nprint(\"SNR y minus x (dB), main:\"); print(diff.round(2).to_string())\nprint(f\"pairs with y > x: {n} of 24\")\nfor k, v in variants.items():\n    dv, nv = sagittal(v)\n    print(f\"{k}: {nv} of 24; pairs with x >= y: {[(i, c) for i in dv.index for c in dv.columns if dv.loc[i, c] <= 0]}\")\n\"\"\", tags=[\"claim:fig2-sagittal-better\"])\n\nmd(\"**Result: RESULT_SAG**\")\n\nmd(\"## fig2-linear-worst\\n\\n> Static linear regression reconstructs much worse than the other decoders.\")\n\ncode(r\"\"\"\ndef linear_worst(snr):\n    m = snr.drop(index=\"linear\") - snr.loc[\"linear\"]\n    return m, bool((m > 0).values.all())\nm, holds = linear_worst(snr)\nprint(\"SNR of each decoder minus linear regression (dB), main:\"); print(m.round(2).to_string())\nprint(\"every decoder above linear regression for every variable:\", holds, \"; smallest margin\", round(m.values.min(), 2))\nfor k, v in variants.items():\n    mv, hv = linear_worst(v)\n    print(f\"{k}: holds {hv}, smallest margin {mv.values.min():.2f} dB ({mv.stack().idxmin()})\")\n\"\"\", tags=[\"claim:fig2-linear-worst\"])\n\nmd(\"**Result: RESULT_LIN**\")\n\nmd(\"## fig2-gross-failures\\n\\n> Gross failures (negative coefficients of determination) occur only for the UKF and KFlatent (+KF), in a few sessions.\")\n\ncode(r\"\"\"\ndef gross(r2):\n    neg = [(i, c, round(r2.loc[i, c], 3)) for i in r2.index for c in r2.columns if r2.loc[i, c] < 0]\n    return neg, all(i in (\"ukf\", \"kflatent_kf\") for i, _, _ in neg)\nneg, holds = gross(r2)\nprint(\"negative R2, main:\", neg, \"; only UKF or KFlatent (+KF):\", holds)\nprint(\"lowest R2 per decoder, main:\"); print(r2.min(1).round(3).to_string())\nneg_c, holds_c = gross(r2_c)\nprint(\"negative R2, code kinematics:\", neg_c, holds_c)\n\"\"\", tags=[\"claim:fig2-gross-failures\"])\n\nmd(\"**Result: RESULT_GROSS**\")\n\nmd(\"## fig4-vel-acc-every-session\\n\\n> For velocity and acceleration, the rEFH (+KF) is better than KFobs and the UKF in every one of the 196 session, variable and axis combinations, and significantly so across sessions.\")\n\ncode(r\"\"\"\ndef every(snr):\n    cols = [\"vx\", \"vy\", \"ax\", \"ay\"]\n    m = pd.DataFrame({r: snr.loc[\"refh_kf\", cols] - snr.loc[r, cols] for r in (\"kfobs\", \"ukf\")}).T\n    return m, int((m > 0).values.sum())\nm, n = every(snr)\nprint(\"SNR rEFH (+KF) minus rival (dB), main:\"); print(m.round(2).to_string())\nprint(f\"comparisons favouring the rEFH (+KF): {n} of 8\")\nfor k, v in variants.items():\n    mv, nv = every(v)\n    print(f\"{k}: {nv} of 8, smallest margin {mv.values.min():.2f} dB\")\n\"\"\", tags=[\"claim:fig4-vel-acc-every-session\"])\n\nmd(\"**Result: RESULT_EVERY**\")\n\nmd(\"## fig4-best-variable\\n\\n> The best-decoded kinematic variable is velocity for the rEFH (+KF), but position for KFobs and the UKF.\")\n\ncode(r\"\"\"\ndef best_var(snr):\n    S = summary(snr)\n    b = S.loc[[\"refh_kf\", \"kfobs\", \"ukf\"]].idxmax(1)\n    return S.loc[[\"refh_kf\", \"kfobs\", \"ukf\"]], b, bool(b[\"refh_kf\"] == \"vel\" and b[\"kfobs\"] == \"pos\" and b[\"ukf\"] == \"pos\")\nSb, b, holds = best_var(snr)\nprint(Sb.round(2).to_string()); print(\"best variable:\", b.to_dict(), \"; holds:\", holds)\nfor k, v in variants.items():\n    _, bv, hv = best_var(v)\n    print(f\"{k}: {bv.to_dict()} holds {hv}\")\n\"\"\", tags=[\"claim:fig4-best-variable\"])\n\nmd(\"**Result: RESULT_BEST**\")\n\nmd(\"## kflatent-modest\\n\\n> KFlatent is only modestly better than the standard Kalman filter; nonlinear tuning (the UKF) improves on the standard filter more.\")\n\ncode(r\"\"\"\ndef kfl_modest(snr):\n    S = summary(snr)\n    reads = {\"a velocity\": [\"vel\"], \"b velocity and acceleration\": [\"vel\", \"acc\"], \"c all three\": [\"pos\", \"vel\", \"acc\"]}\n    out = {}\n    for name, cols in reads.items():\n        kfl = max(S.loc[\"kflatent\", cols].mean(), S.loc[\"kflatent_kf\", cols].mean())\n        kfo, ukf = S.loc[\"kfobs\", cols].mean(), S.loc[\"ukf\", cols].mean()\n        out[name] = dict(kflatent_better_minus_kfobs=kfl - kfo, ukf_minus_kfobs=ukf - kfo,\n                         holds=bool(kfl > kfo and (ukf - kfo) > (kfl - kfo)))\n    return pd.DataFrame(out).T\nprint(\"main:\"); print(kfl_modest(snr).to_string())\nfor k, v in variants.items():\n    if k == \"code kinematics\":\n        print(f\"{k}:\"); print(kfl_modest(v).to_string())\nprint(\"per variable, main (dB):\"); print(summary(snr).loc[[\"kfobs\", \"kflatent\", \"kflatent_kf\", \"ukf\"]].round(2).to_string())\n\"\"\", tags=[\"claim:kflatent-modest\"])\n\nmd(\"**Result: RESULT_KFLMOD**\")\n\nmd(r\"\"\"\n## fig8-velocity-variants\n\n> Under the static mapping, about 0.7 dB of the rEFH's velocity advantage over the UKF is lost\n> when the updated visible units are left out of decoding, and 0.4 dB when standard-normal\n> visible units replace Poisson ones; Kalman filtering does not remove these differences.\n\nThe variant without visible units decodes the canonical rEFH from its hidden means alone. The\nstandard-normal rEFH is trained on standardized counts (the Results, \"Variant decoders\"); the\ncode's transform 2 sqrt(R + 3/8) is the variant the criterion names.\n\"\"\")\n\ncode(r\"\"\"\nt = time.time()\nsp8 = M.prepare(d)\ncanon = M.dec_refh(sp8, seed=1, variants=True)          # seed 1 is the main rEFH run (run_all uses seed + 1)\nnorm_std = M.dec_refh(sp8, seed=1, units=\"normal\", variants=\"standardize\")\nnorm_ans = M.dec_refh(sp8, seed=1, units=\"normal\", variants=\"anscombe\")\nprint(f\"variants fitted in {time.time() - t:.0f} s\")\nv8 = pd.DataFrame({\n    \"canonical\": sp8.score(canon[\"refh\"]), \"canonical +KF\": sp8.score(canon[\"refh_kf\"]),\n    \"hidden only\": sp8.score(canon[\"refh_hid\"]), \"hidden only +KF\": sp8.score(canon[\"refh_hid_kf\"]),\n    \"std normal (standardized)\": sp8.score(norm_std[\"refh\"]), \"std normal (standardized) +KF\": sp8.score(norm_std[\"refh_kf\"]),\n    \"std normal (code transform)\": sp8.score(norm_ans[\"refh\"]), \"std normal (code transform) +KF\": sp8.score(norm_ans[\"refh_kf\"]),\n    \"ukf\": r2.loc[\"ukf\"].values}, index=M.VARS).T\nS8 = summary(M.snr(v8))\nprint(S8.round(2).to_string())\nvel = S8[\"vel\"]\nloss_hid = vel[\"canonical\"] - vel[\"hidden only\"]\nloss_std = vel[\"canonical\"] - vel[\"std normal (standardized)\"]\nloss_ans = vel[\"canonical\"] - vel[\"std normal (code transform)\"]\nprint(f\"\\nstatic velocity loss, hidden only: {loss_hid:.2f} dB (text 0.7 +- 0.07; figure about 0.3)\")\nprint(f\"static velocity loss, standard normal (standardized): {loss_std:.2f} dB (text 0.4 +- 0.04; figure about 0.4)\")\nprint(f\"static velocity loss, standard normal (code transform): {loss_ans:.2f} dB\")\nprint(\"advantage of canonical static over UKF, velocity:\", round(vel[\"canonical\"] - vel[\"ukf\"], 2))\nfor nm in [\"hidden only +KF\", \"std normal (standardized) +KF\", \"std normal (code transform) +KF\"]:\n    print(f\"dynamic velocity, canonical +KF minus {nm}: {vel['canonical +KF'] - vel[nm]:.2f} dB\")\n\"\"\", tags=[\"claim:fig8-velocity-variants\"])\n\nmd(\"**Result: RESULT_FIG8V**\")\n\nmd(\"## fig8-gaussian-still-beats-ukf\\n\\n> The rEFH keeps an advantage over the UKF when its visible units are standard normal instead of Poisson, so the noise model accounts for only part of its advantage.\")\n\ncode(r\"\"\"\nfor nm in [\"std normal (standardized) +KF\", \"std normal (code transform) +KF\"]:\n    dv = S8.loc[nm] - S8.loc[\"ukf\"]\n    print(f\"{nm} minus UKF (dB): vel {dv['vel']:.2f}, acc {dv['acc']:.2f}, pos {dv['pos']:.2f}; vel and acc above UKF: {bool(dv['vel'] > 0 and dv['acc'] > 0)}\")\n\"\"\", tags=[\"claim:fig8-gaussian-still-beats-ukf\"])\n\nmd(\"**Result: RESULT_GAUSS**\")\n\nmd(\"## Summary\\n\\nSUMMARY\")\n\ncode(r\"\"\"\nprint(f\"notebook run time {(time.time() - T0) / 60:.1f} min\")\n\"\"\")\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata = {\"kernelspec\": {\"display_name\": \"Python 3\", \"language\": \"python\", \"name\": \"python3\"}}\nnbf.write(nb, OUT)\n"
}
```

```
File created successfully at: /tmp/claude-1001/build_nb1.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . ev/bin/activate && uv pip install -q nbformat nbconvert ipykernel pandas 2>&1 | tail -1; python build_nb1.py entries/000129-makin-2018/reproduce_makin_2018.ipynb && mkdir -p dev && cp entries/000129-makin-2018/makin.py dev/ && cp entries/000129-makin-2018/reproduce_makin_2018.ipynb dev/ && cd dev && (time timeout 3000 jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=2400 reproduce_makin_2018.ipynb --output nb1_out.ipynb) > nb1.log 2>&1 &
sleep 5; date -u
```

```
Wed Oct 28 19:24:02 UTC 2026
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build_nb2.py",
 "content": "import nbformat as nbf\nimport sys\n\nOUT = sys.argv[1]\ncells = []\n\n\ndef md(s, tags=None):\n    c = nbf.v4.new_markdown_cell(s.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\ndef code(s, tags=None):\n    c = nbf.v4.new_code_cell(s.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nmd(r\"\"\"\n# Reproducing Makin et al. (2018) from dandiset 000129: bin width, training data and neurons\n\n**Paper.** Makin JG, O'Doherty JE, Cardoso MMB, Sabes PN (2018). Superior arm-movement decoding\nfrom cortex with a new, unsupervised-learning algorithm. *J. Neural Eng.* 15, 026010.\n[doi:10.1088/1741-2552/aa9e95](https://doi.org/10.1088/1741-2552/aa9e95)\n\n**Dataset.** [DANDI:000129](https://dandiarchive.org/dandiset/000129/0.241017.1444) version\n0.241017.1444, streamed. It is the only published version; the draft holds the same two assets\nand differs only in its title. The claims file, `claims/000129/10.1088-1741-2552-aa9e95.yaml`, was\nwritten from the version of record and the paper's code (jgmakin/rbmish at commit 700062f5).\n\nThe dataset holds one session of monkey I (M1 only, 649.1 s with kinematics); the paper used 49\nsessions. This notebook refits all eight decoders on that session at bin widths of 16, 32, 64 and\n128 ms (figure 5), with 80, 160 and 320 s of training data (figure 6), and with fractions 1/8,\n1/4, 1/2 and 1 of the units (figure 7). The data checks and the decoders at 64 ms are in\n`reproduce_makin_2018.ipynb`.\n\n| Claim | Here |\n|---|---|\n| fig5-advantage-with-binwidth, fig5-derivative-order | tested on one session |\n| advantage-grows-with-derivative | tested on one session |\n| fig7-affine-position, fig7-kinematic-model-saturates | tested on one session |\n| fig5-vel-acc-all-bins, fig5-position-bins, fig6-training-time, fig7-vel-acc-neurons, fig7-position-neurons | blocked: bootstrap across the paper's 49 sessions |\n| all others | see `reproduce_makin_2018.ipynb` |\n\"\"\")\n\ncode(r\"\"\"\nimport os\nos.environ.setdefault(\"OMP_NUM_THREADS\", \"4\")\nimport time\nimport numpy as np\nimport pandas as pd\nimport makin as M\n\npd.set_option(\"display.width\", 200)\nT0 = time.time()\nd = M.load_session()\nprint(f\"dandiset {M.DANDISET} version {M.VERSION}; {d['session_description'][:80]}\")\n\"\"\")\n\nmd(\"## Data check\")\n\ncode(r\"\"\"\nprint(f\"units {len(d['unit_ids'])}; kinematic samples {len(d['finger_pos'])} at {d['rate']:.0f} Hz; NaN samples {np.isnan(d['finger_pos'][:, 0]).sum()}\")\nrows = []\nfor bms in (16, 32, 64, 128):\n    R, X, _ = M.bin_data(d, bms)\n    ntr = int(320 / (bms / 1000))\n    keep = M.unit_filter(R, bms, ntr)\n    rows.append(dict(bin_ms=bms, bins=len(X), train_bins=ntr, test_bins=len(X) - ntr, nan_bins=int(np.isnan(X).any(1).sum()),\n                     units_used=int(keep.sum()), mean_count=R[:, keep].mean().round(3),\n                     speed_max=np.nanmax(np.hypot(X[:, 2], X[:, 3])).round(0)))\nprint(pd.DataFrame(rows).to_string(index=False))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nThe number of training bins is 320 s divided by the bin width (20,000, 10,000, 5,000 and 2,500, as\nthe Methods give), and the same units pass the 0.5 Hz filter at every width.\n\"\"\")\n\nmd(r\"\"\"\n## Fits\n\nEach configuration fits the eight decoders with seed 0 (a standard choice: one training run, as\nthe paper reports one per session). The rEFH is trained for max(floor(Ntrain/250), 20) epochs\n(80 at 16 ms, 40 at 32 ms, 20 at 64 and 128 ms; Methods and code). For 80 and 160 s of training\nthe paper does not say which bins are tested; the code (getLatentsBMI.m, getTestBins) tests on\nevery bin after the training bins, and this is the main reading; scoring only the bins after\n320 s, the same test set as for 320 s, is shown as a variant.\n\"\"\")\n\ncode(r\"\"\"\ndef summary(snr):\n    return pd.DataFrame({\"pos\": snr[[\"x\", \"y\"]].mean(1), \"vel\": snr[[\"vx\", \"vy\"]].mean(1),\n                         \"acc\": snr[[\"ax\", \"ay\"]].mean(1)})\n\nresults, results_320 = {}, {}\nconfigs = [(\"bin\", 16, dict(bin_ms=16)), (\"bin\", 32, dict(bin_ms=32)), (\"bin\", 64, dict(bin_ms=64)),\n           (\"bin\", 128, dict(bin_ms=128)), (\"train\", 80, dict(train_s=80.0)), (\"train\", 160, dict(train_s=160.0)),\n           (\"frac\", 1 / 8, dict(fraction=1 / 8)), (\"frac\", 1 / 4, dict(fraction=1 / 4)), (\"frac\", 1 / 2, dict(fraction=1 / 2))]\nfor kind, val, kw in configs:\n    t = time.time()\n    sp = M.prepare(d, **kw)\n    pred = M.run_all(sp, seed=0)\n    r2 = pd.DataFrame({k: sp.score(v) for k, v in pred.items()}, index=M.VARS).T.loc[M.DECODERS]\n    results[(kind, val)] = r2\n    if kind == \"train\":\n        results_320[(kind, val)] = pd.DataFrame({k: sp.score(v, from_s=320.0) for k, v in pred.items()}, index=M.VARS).T.loc[M.DECODERS]\n    print(f\"{kind} {val}: units {sp.Rtr.shape[1]}, train bins {len(sp.Rtr)}, test bins {sp.okte.sum()}, \"\n          f\"negative R2 {int((r2.values < 0).sum())}, {time.time() - t:.0f} s\")\nresults[(\"train\", 320)] = results[(\"bin\", 64)]\nresults_320[(\"train\", 320)] = results[(\"bin\", 64)]\nresults[(\"frac\", 1.0)] = results[(\"bin\", 64)]\nSNR = {k: summary(M.snr(v)) for k, v in results.items()}\nfor k, v in SNR.items():\n    print(f\"\\n{k}, SNR (dB) averaged over x and y:\"); print(v.round(2).to_string())\n\"\"\")\n\nmd(r\"\"\"\n## fig5-advantage-with-binwidth\n\n> Reconstruction improves with bin width, and so does the relative advantage of the rEFH (+KF).\n\"\"\")\n\ncode(r\"\"\"\nOTHERS = [\"linear\", \"kfobs\", \"kflatent\", \"kflatent_kf\", \"wf\", \"ukf\"]\nwidths = [16, 32, 64, 128]\ndef advantage(S, v):\n    best = S.loc[OTHERS, v].max()\n    return S.loc[\"refh_kf\", v] - best, 100 * (S.loc[\"refh_kf\", v] - best) / best, S.loc[OTHERS, v].idxmax()\nrows = []\nfor w in widths:\n    S = SNR[(\"bin\", w)]\n    for v in (\"vel\", \"acc\"):\n        db, pc, who = advantage(S, v)\n        rows.append(dict(width=w, var=v, refh_kf=S.loc[\"refh_kf\", v], best_other=who, adv_dB=db, adv_pct=pc))\nA = pd.DataFrame(rows)\nprint(A.round(2).to_string(index=False))\ndef rises(vals, tol):\n    vals = np.asarray(vals)\n    return bool(vals[-1] > vals[0] and np.all(np.diff(vals) >= -tol))\nverdict = {}\nfor reading, col, tol in ((\"a dB\", \"adv_dB\", 0.2), (\"b percent\", \"adv_pct\", 2.0)):\n    ok = True\n    for v in (\"vel\", \"acc\"):\n        sub = A[A[\"var\"] == v]\n        snr_ok, adv_ok = rises(sub.refh_kf, 0.2), rises(sub[col], tol)\n        print(f\"reading {reading}, {v}: rEFH (+KF) SNR rises {snr_ok}; advantage rises {adv_ok}\")\n        ok &= snr_ok and adv_ok\n    verdict[reading] = ok\nprint(\"reproduced under:\", [k for k, v in verdict.items() if v])\nprint(\"SNR of every decoder by width (velocity):\"); print(pd.DataFrame({w: SNR[(\"bin\", w)][\"vel\"] for w in widths}).round(2).to_string())\n\"\"\", tags=[\"claim:fig5-advantage-with-binwidth\"])\n\nmd(\"**Result: RESULT_F5A**\")\n\nmd(r\"\"\"\n## fig5-derivative-order\n\n> With increasing derivative order reconstruction quality declines (except that the rEFH is best\n> at velocity), while the relative advantage of the rEFH (+KF) increases.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor w in widths:\n    S = SNR[(\"bin\", w)]\n    mean_other = S.loc[OTHERS].mean()\n    pct = {v: advantage(S, v)[1] for v in (\"pos\", \"vel\", \"acc\")}\n    q = mean_other[\"pos\"] > mean_other[\"vel\"] > mean_other[\"acc\"]\n    a = pct[\"pos\"] < pct[\"vel\"] < pct[\"acc\"]\n    rows.append(dict(width=w, mean6_pos=mean_other[\"pos\"], mean6_vel=mean_other[\"vel\"], mean6_acc=mean_other[\"acc\"],\n                     adv_pct_pos=pct[\"pos\"], adv_pct_vel=pct[\"vel\"], adv_pct_acc=pct[\"acc\"], quality_declines=q,\n                     advantage_rises=a, both=q and a, refh_kf_best_var=S.loc[\"refh_kf\"].idxmax()))\nD = pd.DataFrame(rows)\nprint(D.round(2).to_string(index=False))\nprint(\"widths where both hold:\", int(D.both.sum()), \"of 4\")\n\"\"\", tags=[\"claim:fig5-derivative-order\"])\n\nmd(\"**Result: RESULT_F5D**\")\n\nmd(r\"\"\"\n## advantage-grows-with-derivative\n\n> At 64 ms and with each amount of training data, the relative advantage of the rEFH (+KF) over\n> the other decoders increases from position to velocity to acceleration.\n\"\"\")\n\ncode(r\"\"\"\nfor label, res in ((\"test on all bins after training (main)\", results), (\"test on bins after 320 s (variant)\", results_320)):\n    rows = []\n    for tr in (80, 160, 320):\n        S = summary(M.snr(res[(\"train\", tr)]))\n        pct = {v: advantage(S, v)[1] for v in (\"pos\", \"vel\", \"acc\")}\n        rows.append(dict(train_s=tr, adv_pct_pos=pct[\"pos\"], adv_pct_vel=pct[\"vel\"], adv_pct_acc=pct[\"acc\"],\n                         best_other_pos=advantage(S, \"pos\")[2], rises=pct[\"pos\"] < pct[\"vel\"] < pct[\"acc\"]))\n    print(label); print(pd.DataFrame(rows).round(2).to_string(index=False))\nfor tr in (80, 160):\n    print(f\"\\nSNR (dB), {tr} s of training, main test set:\"); print(summary(M.snr(results[('train', tr)])).round(2).to_string())\n\"\"\", tags=[\"claim:advantage-grows-with-derivative\"])\n\nmd(\"**Result: RESULT_ADV**\")\n\nmd(r\"\"\"\n## fig7-affine-position\n\n> Position SNR of the decoders without a learned kinematic model (linear regression, static\n> KFlatent, WF, static rEFH) is close to an affine function of the fraction of neurons, with\n> correlations 0.999, 0.95, 0.98 and 1.000; static KFlatent is the most curved.\n\"\"\")\n\ncode(r\"\"\"\nfr = [1 / 8, 1 / 4, 1 / 2, 1.0]\nP = pd.DataFrame({f: SNR[(\"frac\", f)][\"pos\"] for f in fr})\nP.columns = [\"1/8\", \"1/4\", \"1/2\", \"1\"]\nprint(\"position SNR (dB), averaged over x and y:\"); print(P.round(2).to_string())\nstatic = [\"linear\", \"kflatent\", \"wf\", \"refh\"]\nexpected = dict(linear=0.999, kflatent=0.95, wf=0.98, refh=1.0)\nout = {}\nfor reading, xs in ((\"a f\", np.array(fr)), (\"b log2 f\", np.log2(fr))):\n    rho = {k: np.corrcoef(xs, P.loc[k].values)[0, 1] for k in static}\n    within = {k: abs(rho[k] - expected[k]) <= 0.1 * expected[k] for k in static}\n    lowest = min(rho, key=rho.get)\n    out[reading] = dict(**{f\"rho_{k}\": rho[k] for k in static}, all_within=all(within.values()), lowest=lowest,\n                        holds=all(within.values()) and lowest == \"kflatent\")\nprint(pd.DataFrame(out).T.to_string())\n\"\"\", tags=[\"claim:fig7-affine-position\"])\n\nmd(\"**Result: RESULT_F7A**\")\n\nmd(r\"\"\"\n## fig7-kinematic-model-saturates\n\n> Position SNR of the four decoders that learn a kinematic state-transition model (KFobs,\n> KFlatent (+KF), UKF, rEFH (+KF)) rises much faster at first with added neurons, then saturates.\n\"\"\")\n\ncode(r\"\"\"\ndyn = [\"kfobs\", \"kflatent_kf\", \"ukf\", \"refh_kf\"]\nPf = pd.DataFrame({f: SNR[(\"frac\", f)][\"pos\"] for f in fr})\nprint(Pf.round(2).to_string())\nlate = (Pf[1.0] - Pf[0.5]) / 0.5\nres = {}\nfor reading, (f0, f1) in ((\"a 1/8 to 1/4\", (1 / 8, 1 / 4)), (\"b 1/8 to 1/2\", (1 / 8, 1 / 2))):\n    init = (Pf[f1] - Pf[f0]) / (f1 - f0)\n    tab = pd.DataFrame({\"initial_slope\": init, \"late_slope\": late})\n    max_static_init = init[static].max()\n    ok = {k: bool(init[k] > late[k] and init[k] > max_static_init) for k in dyn}\n    print(f\"\\nreading {reading} (dB per unit f):\"); print(tab.round(2).to_string())\n    print(f\"largest initial slope among the static decoders: {max_static_init:.2f}; per dynamic decoder: {ok}\")\n    res[reading] = all(ok.values())\nprint(\"\\nreproduced under:\", [k for k, v in res.items() if v])\n\"\"\", tags=[\"claim:fig7-kinematic-model-saturates\"])\n\nmd(\"**Result: RESULT_F7S**\")\n\nmd(\"## Summary\\n\\nSUMMARY\")\n\ncode(r\"\"\"\nprint(f\"notebook run time {(time.time() - T0) / 60:.1f} min\")\n\"\"\")\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata = {\"kernelspec\": {\"display_name\": \"Python 3\", \"language\": \"python\", \"name\": \"python3\"}}\nnbf.write(nb, OUT)\n"
}
```

```
File created successfully at: /tmp/claude-1001/build_nb2.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
sleep 240; cat $TMPDIR/dev/nb1.log; date -u
```

```
[NbConvertApp] Converting notebook reproduce_makin_2018.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
Wed Oct 28 19:28:45 UTC 2026
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json; s=json.load(open('schemas/attempt.schema.json')); print(json.dumps(s,indent=0)[:6000])"
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
[... 258 more lines not kept]
```

**Agent**

Writing entry files while the dev run goes.

**Agent calls Bash**

```bash
cd entries/000129-makin-2018; cat > requirements.in <<'EOF'
h5py
numpy
pandas
remfile
requests
scipy
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: 000129-makin-2018
type: reproduction
title: Arm-movement decoding with the rEFH and seven other decoders (Makin et al. 2018)
description: Tests the findings of Makin, O'Doherty, Cardoso and Sabes (2018) on dandiset 000129,
  which holds one session of monkey I (M1 array, 649 s of sorted-unit spikes with fingertip and
  cursor kinematics) from the Neural Latents Benchmark. It re-implements the paper's eight decoders
  (linear regression, KFobs, KFlatent static and dynamic, Wiener filter, UKF, rEFH static and
  dynamic) from its Methods and code, and compares them at four bin widths, three amounts of
  training data and four fractions of the units. The paper's tests across its 49 sessions cannot be
  run on one session.
license: Apache-2.0
notebooks:
- path: reproduce_makin_2018.ipynb
  title: Decoders at 64 ms on dandiset 000129 (figures 2, 4 and 8)
  runtime_minutes: 12
- path: binwidth_training_neurons.ipynb
  title: Bin width, training data and number of neurons (figures 5 to 7)
  runtime_minutes: 17
helpers:
- makin.py
related:
- id: dandi:000129/0.241017.1444
  relation: uses_data
- id: doi:10.1088/1741-2552/aa9e95
  relation: reproduces
EOF
python3 $TMPDIR/build_nb2.py binwidth_training_neurons.ipynb; ls; sleep 120; cat $TMPDIR/dev/nb1.log | tail -3
```

```
__pycache__
binwidth_training_neurons.ipynb
entry.yaml
makin.py
reproduce_makin_2018.ipynb
requirements.in
[NbConvertApp] Converting notebook reproduce_makin_2018.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
```

**Agent calls Bash**

```bash
rm -rf entries/000129-makin-2018/__pycache__; sleep 270; tail -3 $TMPDIR/dev/nb1.log; date -u
```

```
[NbConvertApp] Converting notebook reproduce_makin_2018.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
Wed Oct 28 19:35:26 UTC 2026
```

**Agent calls Bash**

```bash
sleep 200; tail -5 $TMPDIR/dev/nb1.log; date -u
```

```
[NbConvertApp] Converting notebook reproduce_makin_2018.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
Wed Oct 28 19:38:47 UTC 2026
```

**Agent calls Bash**

```bash
sleep 180; tail -5 $TMPDIR/dev/nb1.log; ps aux | grep -c ipykernel; date -u
```

```
[NbConvertApp] Converting notebook reproduce_makin_2018.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
3
Wed Oct 28 19:41:49 UTC 2026
```

**Agent calls Bash**

```bash
sleep 240; tail -2 $TMPDIR/dev/nb1.log; ls -la $TMPDIR/dev; date -u
```

```
[NbConvertApp] Converting notebook reproduce_makin_2018.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
total 84
drwxr-xr-x 3 runner runner  4096 Oct 28 19:24 .
drwx-----T 8 runner runner  4096 Oct 28 19:41 ..
drwxr-xr-x 2 runner runner  4096 Oct 28 19:24 __pycache__
-rw-r--r-- 1 runner runner 29623 Oct 28 19:23 makin.py
-rw-r--r-- 1 runner runner   357 Oct 28 19:24 nb1.log
-rw-r--r-- 1 runner runner 33705 Oct 28 19:23 reproduce_makin_2018.ipynb
Wed Oct 28 19:45:52 UTC 2026
```

**Agent calls Bash**

```bash
top -b -n1 | head -15; py-spy --version 2>/dev/null
```

```
Exit code 127
top - 19:45:54 up 50 min,  0 users,  load average: 0.06, 0.13, 0.54
Tasks:   4 total,   1 running,   3 sleeping,   0 stopped,   0 zombie
%Cpu(s):  2.3 us,  2.3 sy,  0.0 ni, 93.2 id,  2.3 wa,  0.0 hi,  0.0 si,  0.0 st 
MiB Mem :  15983.1 total,  12235.2 free,   1155.2 used,   2985.3 buff/cache     
MiB Swap:   3072.0 total,   3072.0 free,      0.0 used.  14827.8 avail Mem 

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
      1 runner    20   0    3804   1492   1256 S   0.0   0.0   0:00.06 bwrap
      2 runner    20   0    9772   5568   3468 S   0.0   0.0   0:00.02 bash
      4 runner    20   0   11000   5292   3244 R   0.0   0.0   0:00.00 top
      5 runner    20   0   17596   7520   6104 S   0.0   0.0   0:00.00 head
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev && . ../ev/bin/activate && cp entries/000129-makin-2018/makin.py . && time jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 reproduce_makin_2018.ipynb --output nb1_out.ipynb 2>&1 | grep -v WARNING | tail -20; date -u
```

```
kflatent_kf  0.579  0.666  0.528  0.557  0.166  0.269
wf           0.469  0.517  0.508  0.545  0.217  0.309
ukf          0.678  0.767  0.544  0.622  0.165  0.282
refh         0.186  0.372  0.592  0.587  0.328  0.381
refh_kf      0.699  0.781  0.673  0.702  0.388  0.448

SNR (dB):
------------------

[31m---------------------------------------------------------------------------[39m
[31mAttributeError[39m                            Traceback (most recent call last)
[36mCell[39m[36m [39m[32mIn[7][39m[32m, line 12[39m
[32m      8[39m sp, pred, r2, secs = fit_config(seed=[32m0[39m)
[32m      9[39m print(f"fitted in {secs:.0f} s; units {sp.Rtr.shape[[32m1[39m]}, training bins {len(sp.Rtr)} ({sp.oktr.sum()} scored), test bins {len(sp.Rte)} ({sp.okte.sum()} scored)")
[32m     10[39m snr = M.snr(r2)
[32m     11[39m print([33m"R2:"[39m); print(r2.round([32m3[39m).to_string())
[32m---> [39m[32m12[39m print([33m"\nSNR (dB):"[39m); print(snr.round([32m2[39m).to_string())

[31mAttributeError[39m: 'numpy.ndarray' object has no attribute 'to_string'

[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000129-makin-2018 && python3 - <<'EOF'
s=open('makin.py').read()
s=s.replace('''    return -10 * np.log10(1 - np.asarray(r2))''','''    if not hasattr(r2, "values"):
        r2 = np.asarray(r2)
    return -10 * np.log10(1 - r2)''')
open('makin.py','w').write(s)
EOF
cd $TMPDIR/dev && . ../ev/bin/activate && cp entries/000129-makin-2018/makin.py . && time jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 reproduce_makin_2018.ipynb --output nb1_out.ipynb 2>&1 | grep -v WARNING | tail -20; date -u
```

```
[NbConvertApp] Converting notebook reproduce_makin_2018.ipynb to notebook
[NbConvertApp] Writing 65085 bytes to nb1_out.ipynb

real	10m5.367s
user	37m6.973s
sys	0m4.437s
Wed Oct 28 19:58:18 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev && python3 -c "
import json; nb=json.load(open('nb1_out.ipynb'))
for c in nb['cells']:
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            t=o.get('text') or ''.join(o.get('data',{}).get('text/plain',''))
            print(''.join(t) if isinstance(t,list) else t)
        print('-----')
"
```

```
dandiset 000129 version 0.241017.1444
Data from monkey Indy performing self-paced random target reaching task. This file contains continuous segments of the full session on 2017-02-02 that can be used for training models for the Neural Latents Benchmark.
session_start_time 2017-02-02T00:00:00-08:00

-----
subjects 1 (Indy), sessions 1, units 130 (32 marked heldout by the benchmark)
kinematics: 649100 samples at 1000 Hz from t0 = 0.0 s, duration 649.1 s
finger_pos unit attribute: meters  conversion: 0.001
finger_pos  x   -63.8 to   70.6, y   -7.5 to  117.8 (stored values); NaN samples 300
cursor_pos  x   -65.2 to   71.0, y   -7.8 to  117.9 (stored values); NaN samples 300
target_pos  x   -52.5 to   52.5, y    7.5 to  112.5 (stored values); NaN samples 300
NaN gaps (s): [(np.float64(162.2), np.float64(162.3)), (np.float64(324.5), np.float64(324.6)), (np.float64(486.8), np.float64(486.9))]
spikes 339874, times 0.002 to 649.096 s, sorted within units: True
spikes inside the NaN gaps: 0
unit ids end in: [1, 2, 3, 4] (channel*100 + unit; 0 would be the unsorted hash unit)
channels with units: 82
rates (Hz) min 0.08, median 2.96, max 19.51
trials table splits: {'train': 810, 'val': 270}

-----
[... 353 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i 's/\.mean(1)/.mean(axis=1)/g; s/\.min(1)/.min(axis=1)/g; s/\.idxmax(1)/.idxmax(axis=1)/g' build_nb1.py build_nb2.py && grep -c "axis=1" build_nb1.py build_nb2.py && . ev/bin/activate && python build_nb2.py dev/binwidth_training_neurons.ipynb && cd dev && time jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 binwidth_training_neurons.ipynb --output nb2_out.ipynb 2>&1 | grep -v WARNING | tail -20; date -u
```

```
build_nb1.py:5
build_nb2.py:2
[NbConvertApp] Converting notebook binwidth_training_neurons.ipynb to notebook
[NbConvertApp] Writing 32256 bytes to nb2_out.ipynb

real	21m51.594s
user	73m33.997s
sys	0m15.235s
Wed Oct 28 20:20:36 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev && python3 -c "
import json; nb=json.load(open('nb2_out.ipynb'))
for c in nb['cells']:
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            t=o.get('text') or ''.join(o.get('data',{}).get('text/plain',''))
            print(''.join(t) if isinstance(t,list) else t)
        print('-----')
" | grep -v Warning | grep -v "return pd.DataFrame\|\"acc\": snr"
```

```
dandiset 000129 version 0.241017.1444; Data from monkey Indy performing self-paced random target reaching task. This fi

-----
units 130; kinematic samples 649100 at 1000 Hz; NaN samples 300

 bin_ms  bins  train_bins  test_bins  nan_bins  units_used  mean_count  speed_max
     16 40568       20000      20568        21         111       0.075      546.0
     32 20284       10000      10284        12         111       0.150      546.0
     64 10142        5000       5142         6         111       0.299      546.0
    128  5071        2500       2571         3         111       0.598      512.0

-----
bin 16: units 111, train bins 20000, test bins 20554, negative R2 2, 513 s

bin 32: units 111, train bins 10000, test bins 10276, negative R2 0, 244 s

bin 64: units 111, train bins 5000, test bins 5138, negative R2 0, 124 s

bin 128: units 111, train bins 2500, test bins 2569, negative R2 0, 110 s

[... 257 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('build_nb1.py').read()
R={
'md("**Result: not reproduced.** RESULT_UNITS", tags=None)': '''md("**Result: not reproduced.** 111 of the 130 units in the file fire above 0.5 Hz over the session, below the 153.9 to 454.3 range. The file holds sorted units only (no unit id ends in 00), on 82 channels. The paper's counts include an unsorted hash unit for each channel (Methods, Data acquisition), up to 96 more here, so the shortfall is consistent with the missing hash units.")''',
'md("**Result: RESULT_VB**")': '''md("**Result: not reproduced, resting on the Methods reading of the kinematics.** The rEFH (+KF) raises velocity SNR over linear regression by 3.67 dB, KFobs by 1.91 dB and the UKF by 2.42 dB. That is 1.92 times KFobs's gain, where the criterion needs more than 2, and 1.51 times the UKF's, inside 1.5 to 2.2. With the code's kinematics the ratios are 2.05 and 1.70 and the claim holds. The other two rEFH seeds give KFobs ratios of 1.93 and 1.95.")''',
'md("**Result: RESULT_KFL**")': '''md("**Result: reproduced.** The dynamic map changes KFlatent's SNR by 0.18 dB for position, 0.21 for velocity and 0.09 for acceleration, all below 0.5 dB. With the code's kinematics the changes are 0.29, 0.45 and 0.22 dB.")''',
'md("**Result: RESULT_STATIC**")': '''md("**Result: reproduced.** Among the decoders other than the rEFH (+KF), the static rEFH has the highest velocity SNR (3.87 dB against the UKF's 3.82) and acceleration SNR (1.90 against the WF's 1.34). The velocity margin is small: 0.05 dB here, 0.08 and 0.17 dB with the other seeds, and 0.09 dB over KFlatent (+KF) with the code's kinematics. The claim holds in all four runs.")''',
'md("**Result: RESULT_POSGAIN**")': '''md("**Result: not reproduced.** The dynamic mapping raises the rEFH's position SNR from 1.46 to 5.91 dB, a gain of 4.45 dB (4.32 for x, 4.58 for y), outside 3 +- 0.5 dB. The gain is larger than the paper's, from 4.22 to 4.52 dB across the other seeds and the code's kinematics.")''',
'md("**Result: RESULT_SAG**")': '''md("**Result: partially reproduced.** The sagittal component has the higher SNR in 23 of the 24 decoder and variable pairs. The exception is the static rEFH's velocity, where y minus x is -0.06 dB. With rEFH seed 2 all 24 pairs hold; with seed 1 and with the code's kinematics 23 hold, with the same exception. Linear regression's velocity margin is 0.01 dB.")''',
'md("**Result: RESULT_LIN**")': '''md("**Result: reproduced.** Every decoder has a higher SNR than linear regression for each of the six variables. The smallest margin is 0.45 dB (static rEFH, x position), and the claim holds in every variant (smallest margin 0.20 dB, with the code's kinematics).")''',
'md("**Result: RESULT_GROSS**")': '''md("**Result: reproduced, with no failures to count.** No decoder has a negative R2 at 64 ms in this session; the lowest is linear regression's 0.055. The criterion, that every negative R2 belongs to the UKF or KFlatent (+KF), therefore holds trivially. Whether failures occur in a few sessions cannot be tested on one session.")''',
'md("**Result: RESULT_EVERY**")': '''md("**Result: reproduced for this session.** The rEFH (+KF) beats KFobs and the UKF in all 8 velocity and acceleration comparisons, by 1.04 to 1.81 dB, and in every variant (smallest margin 1.05 dB). The bootstrap across the paper's 49 sessions cannot be run on one session.")''',
'md("**Result: RESULT_BEST**")': '''md("**Result: not reproduced.** Position is the best-decoded variable for all three decoders. The rEFH (+KF) has 5.91 dB for position against 5.06 for velocity; KFobs and the UKF have position highest, as the paper says. The ordering is the same with the other seeds and the code's kinematics.")''',
'md("**Result: RESULT_KFLMOD**")': '''md("**Result: reproduced.** On velocity (reading a), the better KFlatent decoder exceeds KFobs by 0.10 dB while the UKF exceeds it by 0.51 dB; on velocity and acceleration (reading b) by 0.08 and 0.30 dB. Over all three variables (reading c) KFlatent is 0.20 dB below KFobs. With the code's kinematics readings a and b fail (KFlatent ahead of KFobs by 0.49 and 0.39 dB, more than the UKF's 0.38 and 0.22) and reading c holds (0.07 against 0.32 dB). Under either kinematics the claim holds under one reading.")''',
'md("**Result: RESULT_FIG8V**")': '''md("**Result: not reproduced.** Leaving the updated visible units out costs 0.11 dB of static velocity SNR (the text says 0.7 dB, figure 8 about 0.3). The standard-normal rEFH trained on standardized counts gains 0.08 dB (a loss of -0.08 dB against the text's 0.4). Trained on the code's transform, 2 sqrt(R + 3/8), it loses 2.11 dB. Under the dynamic mapping the canonical rEFH (+KF) still exceeds the variants, by 0.15, 0.15 and 1.68 dB. The static rEFH's own velocity advantage over the UKF is only 0.05 dB here.")''',
'md("**Result: RESULT_GAUSS**")': '''md("**Result: reproduced, resting on the standardized-counts reading.** Trained on standardized counts, the standard-normal rEFH (+KF) exceeds the UKF by 1.09 dB for velocity and 1.17 dB for acceleration. Trained on the code's transform it is 0.43 dB below the UKF for velocity (0.12 dB above for acceleration), and the claim fails.")''',
}
for k,v in R.items():
    assert k in s, k
    s=s.replace(k,v)
summ='''md(r"""
## Summary

| Claim | Outcome |
|---|---|
| units-monkey-i | not reproduced (111 units; no hash units in the file) |
| fig2-velocity-boost | not reproduced, resting on the Methods kinematics (reproduced with the code's) |
| fig2-kflatent-dynamic-little-effect | reproduced |
| fig2-refh-static-vel-acc | reproduced |
| fig2-position-dynamic-gain | not reproduced (gain 4.45 dB, not about 3) |
| fig2-sagittal-better | partially reproduced (23 of 24) |
| fig2-linear-worst | reproduced |
| fig2-gross-failures | reproduced (no negative R2 at all) |
| fig4-vel-acc-every-session | reproduced for this session (bootstrap not run) |
| fig4-best-variable | not reproduced (the rEFH (+KF) decodes position best) |
| kflatent-modest | reproduced |
| fig8-velocity-variants | not reproduced |
| fig8-gaussian-still-beats-ukf | reproduced, resting on standardized counts |
| fig5-advantage-with-binwidth, fig5-derivative-order, advantage-grows-with-derivative, fig7-affine-position, fig7-kinematic-model-saturates | see `binwidth_training_neurons.ipynb` |
| fig2-refh-kf-best, intro-gain-over-nearest, fig4-advantage-grows, fig4-position, fig5-vel-acc-all-bins, fig5-position-bins, fig6-training-time, fig7-vel-acc-neurons, fig7-position-neurons, fig8-position-variants, fig9-taps, static-refh-position-worse, fig4-task-similar | blocked: they need the paper's other sessions |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

**How the analysis differs from the paper's.** One session in place of 49, so every mean over
sessions is this session's value and no bootstrap is run. The session is dated 2017-02-02, which
is not in the paper's session list. Sorted units only (111 above 0.5 Hz), without the hash units
the paper kept. The test part is the last 329 s of the training file; the test file's kinematics
are withheld. Six bins that overlap the file's three 0.1 s gaps are left out of fitting and
scoring. All decoders are re-implemented in Python from the Methods and the paper's code; the
UKF re-implements Li's UKF2, whose fitting code is not in the paper's repository. The rEFH is
trained in single precision. EM for KFlatent ran the full 100 epochs without meeting the
convergence criterion, as the Methods allow.

**What was found about the dataset.** The dandiset holds one of the paper's three monkeys and one
session, which the paper's session list does not include. It has no hash units. Three 0.1 s gaps
split the training file into four segments, with NaN kinematics and no spikes, and nothing says
what was cut. The test file's 190 s have no kinematics. The units and the kinematics share one
clock: velocity is best decoded from spikes 64 ms earlier.
""")'''
s=s.replace('md("## Summary\\n\\nSUMMARY")', summ)
assert 'SUMMARY' not in s and 'RESULT_' not in s
open('build_nb1.py','w').write(s)

s=open('build_nb2.py').read()
R={
'md("**Result: RESULT_F5A**")':'''md("**Result: reproduced.** The rEFH (+KF) velocity SNR rises from 3.01 dB at 16 ms to 5.46 dB at 128 ms and acceleration from 0.96 to 2.39 dB, with no fall between neighbouring widths. Its advantage over the best other decoder rises from -0.29 to 1.60 dB for velocity and from -0.44 to 1.14 dB for acceleration (-8.9 to 41.6% and -31.3 to 92.0%), so the claim holds under both readings. At 16 ms the WF beats the rEFH (+KF) for both variables. Not every decoder improves with width: the WF's velocity SNR falls from 3.30 to 3.18 dB.")''',
'md("**Result: RESULT_F5D**")':'''md("**Result: partially reproduced.** The mean SNR of the six other decoders falls from position to velocity to acceleration at all four widths (at 64 ms 3.79, 3.06 and 0.99 dB). The percent advantage of the rEFH (+KF) rises from position to velocity to acceleration at 32, 64 and 128 ms (at 64 ms 4.9, 32.6 and 76.5%), but not at 16 ms, where it is negative and falls (-6.2, -8.9 and -31.3%). Both parts hold at 3 of 4 widths. The claim's exception does not hold here: the rEFH (+KF) decodes position best at every width.")''',
'md("**Result: RESULT_ADV**")':'''md("**Result: reproduced.** The percent advantage of the rEFH (+KF) rises from position to velocity to acceleration with 80 s (-26.1, 10.9 and 76.4%), 160 s (2.4, 32.5 and 71.3%) and 320 s (4.9, 32.6 and 76.5%) of training. It also rises at each amount when the shorter trainings are scored on the bins after 320 s only.")''',
'md("**Result: RESULT_F7A**")':'''md("**Result: not reproduced.** The correlations of position SNR with f are 0.995 (linear regression), 0.995 (static KFlatent), 0.986 (WF) and 0.991 (static rEFH), and with log2 f 0.956, 0.948, 0.954 and 0.914; all are within 10% of the paper's values. But static KFlatent does not have the lowest correlation under either reading (the WF has with f, the static rEFH with log2 f), so the ordering condition fails. At f = 1/8 and 1/4 (13 and 27 units) the position SNR of these four decoders is within 0.33 dB of zero.")''',
'md("**Result: RESULT_F7S**")':'''md("**Result: reproduced, under reading b.** From f = 1/8 to 1/2 the position SNR of KFobs, KFlatent (+KF), the UKF and the rEFH (+KF) rises 6.67, 207.33, 6.93 and 6.22 dB per unit f. That is faster than from 1/2 to 1 (3.79, 6.27, 4.95 and 5.79) and faster than any static decoder's initial rise (largest 5.00, static KFlatent). Under reading a (1/8 to 1/4) only KFlatent (+KF) passes: KFobs, the UKF and the rEFH (+KF) decode position slightly worse at 1/4 than at 1/8. KFlatent (+KF)'s large initial slope comes from a filter that diverges at f = 1/8 (position SNR -76.63 dB), a gross failure.")''',
}
for k,v in R.items():
    assert k in s, k
    s=s.replace(k,v)
summ='''md(r"""
## Summary

| Claim | Outcome |
|---|---|
| fig5-advantage-with-binwidth | reproduced |
| fig5-derivative-order | partially reproduced (3 of 4 widths; not at 16 ms) |
| advantage-grows-with-derivative | reproduced |
| fig7-affine-position | not reproduced (correlations within tolerance; static KFlatent not the most curved) |
| fig7-kinematic-model-saturates | reproduced under reading b |
| fig5-vel-acc-all-bins, fig5-position-bins, fig6-training-time, fig7-vel-acc-neurons, fig7-position-neurons | blocked: bootstrap across the paper's 49 sessions |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

**How the analysis differs from the paper's.** One session (dated 2017-02-02, not in the paper's
session list) in place of 49, so each mean over sessions is this session's value. Sorted units
only, 111 above 0.5 Hz, without hash units; a fraction f keeps the first floor(111 f) of them
(13, 27 and 55 units). For 80 and 160 s of training the test bins are all bins after the
training bins, as in the paper's code; the paper does not say. The decoders are the same
re-implementations as in `reproduce_makin_2018.ipynb`.

**What was found about the dataset.** As in `reproduce_makin_2018.ipynb`: one session, no hash
units, three undocumented 0.1 s gaps, and a test file without kinematics. The same 111 units pass
the rate filter at every bin width.
""")'''
s=s.replace('md("## Summary\\n\\nSUMMARY")', summ)
assert 'SUMMARY' not in s and 'RESULT_' not in s
open('build_nb2.py','w').write(s)
EOF
. ev/bin/activate; cd entries/000129-makin-2018 && python $TMPDIR/build_nb1.py reproduce_makin_2018.ipynb && python $TMPDIR/build_nb2.py binwidth_training_neurons.ipynb && date -u
```

```
Wed Oct 28 20:22:26 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
s=open('makin.py').read()
s=s.replace('''    sts = b["finger_pos"]["starting_time"]''','''    loc = f["general/extracellular_ephys/electrodes/location"][:]
    d["electrode_locations"] = [x.decode() if isinstance(x, bytes) else str(x) for x in loc]
    sts = b["finger_pos"]["starting_time"]''')
open('makin.py','w').write(s)
EOF
cd $TMPDIR && python3 - <<'EOF'
s=open('build_nb1.py').read()
old='''print("unit ids end in:"'''
new='''print("electrode locations:", pd.Series(d["electrode_locations"]).value_counts().to_dict())
print("successive 1 kHz finger samples that are equal:", int((np.diff(d["finger_pos"][:, 0]) == 0).sum()))
print("target x positions (stored):", np.unique(d["target_pos"][~np.isnan(d["target_pos"][:, 0]), 0]))
print("unit ids end in:"'''
assert old in s; s=s.replace(old,new,1)
old='''Almost no run of four inter-spike intervals is
shared between the files (a count near zero is what chance coincidence gives), so the test file
does not repeat the training file.'''
new='''No run of four inter-spike intervals is shared
between the files, so the test file does not repeat the training file.'''
assert old in s; s=s.replace(old,new)
old='''values span about 135 by 125 mm, as an 8 by
8 grid at 15 mm spacing needs (105 mm between outer targets, plus reach overshoot).'''
new='''values span about 135 by 125 mm, and the targets sit
at eight x positions 15 mm apart, as the 8 by 8 grid of the description and of the paper's later
monkey I sessions has. All electrodes are labelled M1.'''
assert old in s; s=s.replace(old,new)
open('build_nb1.py','w').write(s)
EOF
cd $TMPDIR && . ev/bin/activate && python -c "
import sys; sys.path.insert(0,'entries/000129-makin-2018'); import makin as M, numpy as np, pandas as pd
d=M.load_session(); print(pd.Series(d['electrode_locations']).value_counts().to_dict()); print(np.unique(d['target_pos'][~np.isnan(d['target_pos'][:,0]),0]), np.unique(d['target_pos'][~np.isnan(d['target_pos'][:,0]),1]))
" 2>&1 | grep -v Warn; cd entries/000129-makin-2018 && python $TMPDIR/build_nb1.py reproduce_makin_2018.ipynb
```

```
{'M1': 96}
[-52.5 -37.5 -22.5  -7.5   7.5  22.5  37.5  52.5] [  7.5  22.5  37.5  52.5  67.5  82.5  97.5 112.5]
```

**Agent calls Bash**

```bash
cd  && . $TMPDIR/ev/bin/activate && uv pip install -q pyyaml jsonschema 2>&1|tail -1; python tools/entry.py lock entries/000129-makin-2018 2>&1 | tail -3; python tools/entry.py check entries/000129-makin-2018 2>&1 | tail -15
```

```
wrote entries/000129-makin-2018/requirements.lock.txt
0 error(s)
```

**Agent calls Bash**

```bash
. $TMPDIR/ev/bin/activate && date -u && time python tools/entry.py all entries/000129-makin-2018 2>&1 | grep -v WARNING | tail -15; date -u
```

```
Wed Oct 28 20:23:24 UTC 2026
Installed kernelspec registry-000129-makin-2018 in executed/000129-makin-2018/.venv/share/jupyter/kernels/registry-000129-makin-2018
0 error(s)
pass  reproduce_makin_2018.ipynb  (604 s)
pass  binwidth_training_neurons.ipynb  (1301 s)

real	32m16.074s
user	110m20.307s
sys	0m22.436s
Wed Oct 28 20:55:40 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import json,re
def outs(p):
    nb=json.load(open(p)); r=[]
    for c in nb['cells']:
        if c['cell_type']=='code':
            t=''
            for o in c.get('outputs',[]):
                if o.get('name')=='stderr': continue
                x=o.get('text') or o.get('data',{}).get('text/plain','')
                t+=''.join(x) if isinstance(x,list) else x
            r.append(t)
    return r
import os
for dev,ex in [('/tmp/claude-1001/dev/nb1_out.ipynb','executed/000129-makin-2018/reproduce_makin_2018.ipynb'),('/tmp/claude-1001/dev/nb2_out.ipynb','executed/000129-makin-2018/binwidth_training_neurons.ipynb')]:
    a=[re.sub(r'\d+ s\b|fitted in \d+|run time [\d.]+','',x) for x in outs(dev)]; b=[re.sub(r'\d+ s\b|fitted in \d+|run time [\d.]+','',x) for x in outs(ex)]
    sa=set(l for x in a for l in x.splitlines()); sb=set(l for x in b for l in x.splitlines())
    print(ex, "lines only in executed:"); [print("  +",l) for l in sorted(sb-sa)]
    print("lines only in dev:"); [print("  -",l) for l in sorted(sa-sb)][:40]
EOF
```

```
executed/000129-makin-2018/reproduce_makin_2018.ipynb lines only in executed:
  + electrode locations: {'M1': 96}
  + successive 1 kHz finger samples that are equal: 0
  + target x positions (stored): [-52.5 -37.5 -22.5  -7.5   7.5  22.5  37.5  52.5]
lines only in dev:
executed/000129-makin-2018/binwidth_training_neurons.ipynb lines only in executed:
lines only in dev:
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json; s=json.load(open('schemas/attempt.schema.json'))['properties']
for k in ['inputs','findings','verifications']:
  print(k, json.dumps(s.get(k),indent=0)[:1500])
"
```

```
inputs {
"description": "Everything the attempt used that is not in the dataset.",
"type": "array",
"items": {
"type": "object",
"additionalProperties": false,
"required": [
"what",
"source"
],
"properties": {
"what": {
"type": "string",
"minLength": 1
},
"source": {
"description": "A DOI, or a repository URL with the commit read.",
"type": "string",
"minLength": 1
}
[... 110 more lines not kept]
```

**Agent**

Now the attempt record.

**Agent calls Write**

```json
{
 "file_path": "attempts/000129-makin-2018-01.yaml",
 "content": "schema_version: 2\nid: 000129-makin-2018-01\ndataset:\n  archive: dandi\n  id: \"000129\"\n  version: 0.241017.1444\n  doi: 10.48324/dandi.000129/0.241017.1444\npaper: doi:10.1088/1741-2552/aa9e95\ndate: 2026-10-28\nentry: 000129-makin-2018\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-12\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/40749995806\ninputs:\n- what: The paper's list of monkey I sessions (NeuralAnalysis/Indy_HC_Sessions.csv), read only to\n    check whether the dandiset's session is one of the paper's. The decoders follow the same\n    repository's code where the Methods are silent (cited in makin.py), but no file of it is\n    loaded.\n  source: https://github.com/jgmakin/rbmish at commit 700062f5118b0910411cf9a8f73498e22203731d\noutcomes:\n- claim: units-monkey-i\n  outcome: not_reproduced\n  notebook: reproduce_makin_2018.ipynb\n  output: claim:units-monkey-i\n  measured: [111, 111]\n  notes: 111 of the 130 units in the file fire above 0.5 Hz over the 649.1 s session, below the\n    criterion's range of 153.9 to 454.3. The file holds sorted units only (unit ids end in 1 to\n    4, none in 00), on 82 channels; the paper's counts include one unsorted hash unit per channel\n    (Methods, Data acquisition), up to 96 more on this array, so the shortfall is consistent with\n    the missing hash units. With thresholds of 0.25 and 1 Hz the count is 117 and 94. No unit is a\n    duplicate of another.\n  deviations:\n  - One session, the only one in the dataset (dated 2017-02-02, not in the paper's session list),\n    for a range over 37 sessions.\n  - The rate is taken over the training file (649.1 s); the test file holds 190.3 s more of 98 of\n    the units.\n- claim: fig2-refh-kf-best\n  outcome: blocked\n  blocked_by: too_large\n  notes: The criterion needs the bootstrap of the session-weighted mean SNR difference over the\n    paper's 49 sessions. The dandiset holds one session, which is not in the paper's list; the\n    paper's 47 Sabes-lab sessions are public on Zenodo (doi:10.5281/zenodo.583331, 10.5281/zenodo.3854034)\n    and monkey C's two sessions come from Dyer et al. without an archive identifier. Here the\n    eight decoders at 64 ms take 124 s on one session of 111 units. The rEFH's cost grows with the\n    square of the number of units and the EM of KFlatent with its cube, and the paper's sessions\n    have 171 to 523 units, so the 64 ms decoders on the 47 sessions are estimated at several\n    hours, beyond the 30 min notebook limit and the time of this run; they were not run. On the\n    one session the rEFH (+KF) has the highest mean SNR for position, velocity and acceleration\n    (5.91, 5.06 and 2.36 dB), which does not decide the outcome.\n- claim: intro-gain-over-nearest\n  outcome: blocked\n  blocked_by: too_large\n  notes: The criterion needs the bootstrap over the 49 sessions for the position gain (p >= 0.01);\n    see fig2-refh-kf-best for the data and the estimate. On the one session the gains of the rEFH\n    (+KF) over the UKF are 0.28, 1.24 and 1.25 dB for position, velocity and acceleration (reading\n    b), which does not decide the outcome.\n- claim: fig2-velocity-boost\n  outcome: not_reproduced\n  notebook: reproduce_makin_2018.ipynb\n  output: claim:fig2-velocity-boost\n  assumed: true\n  notes: Velocity SNR gains over linear regression are 3.67 dB for the rEFH (+KF), 1.91 for KFobs\n    and 2.42 for the UKF. The rEFH's gain is 1.92 times KFobs's (the criterion needs more than 2)\n    and 1.51 times the UKF's (inside 1.5 to 2.2), so only the UKF part holds, which the criterion\n    does not grade as partial. With the code's kinematics (cursor, no filter, bin means) the\n    ratios are 2.05 and 1.70 and the claim is reproduced. With rEFH seeds 1 and 2 the KFobs ratio is\n    1.93 and 1.95. The outcome rests on the kinematics reading. Question for the paper's authors\n    (finding below) was the decoded kinematic state the fingertip position filtered at 10 Hz and\n    subsampled, as the Methods say, or the unfiltered cursor position averaged over each bin, as\n    getLatentsBMI.m and binSpikeCounts.m do?\n  deviations:\n  - One session in place of 49; the session-weighted means are this session's values.\n  - The kinematics follow the Methods (fingertip, 4th-order Butterworth at 10 Hz, last sample of\n    each bin), as the claims file makes its main reading; the code's reading changes the outcome,\n    and this reading is adopted as the one the paper's text states.\n  - Sorted units only (111), without the hash units the paper used.\n  - The UKF is a re-implementation of Li's UKF2; its fitting code is not in the paper's repository.\n- claim: fig2-kflatent-dynamic-little-effect\n  outcome: reproduced\n  notebook: reproduce_makin_2018.ipynb\n  output: claim:fig2-kflatent-dynamic-little-effect\n  notes: KFlatent (+KF) minus static KFlatent is 0.18, 0.21 and 0.09 dB for position, velocity and\n    acceleration, all below 0.5 dB; with the code's kinematics 0.29, 0.45 and 0.22 dB. EM ran the\n    full 100 epochs without meeting the convergence criterion.\n  deviations:\n  - One session in place of 49.\n  - Sorted units only (111); EM convergence judged on the log-likelihood, which the Methods'\n    cross-entropy criterion is equivalent to up to a constant.\n- claim: fig2-refh-static-vel-acc\n  outcome: reproduced\n  notebook: reproduce_makin_2018.ipynb\n  output: claim:fig2-refh-static-vel-acc\n  notes: The static rEFH has 3.87 dB velocity SNR against the best other decoder's 3.82 (UKF), and\n    1.90 dB acceleration SNR against 1.34 (WF). The velocity margin is small, 0.05 dB here, 0.08 and\n    0.17 dB with rEFH seeds 1 and 2, and 0.09 dB over KFlatent (+KF) with the code's kinematics;\n    the claim holds in all four runs.\n  deviations:\n  - One session in place of 49.\n  - Sorted units only (111); the UKF is a re-implementation of Li's UKF2.\n- claim: fig2-position-dynamic-gain\n  outcome: not_reproduced\n  notebook: reproduce_makin_2018.ipynb\n  output: claim:fig2-position-dynamic-gain\n  measured: 4.45\n  notes: The dynamic mapping raises the rEFH's position SNR from 1.46 to 5.91 dB, a gain of 4.45\n    dB (4.32 for x, 4.58 for y), outside 3 +- 0.5 dB. The effect is present and larger than the\n    paper's; it is 4.22 to 4.52 dB with the other seeds and the code's kinematics.\n  deviations:\n  - One session in place of 49.\n  - Sorted units only (111).\n- claim: fig2-sagittal-better\n  outcome: partially_reproduced\n  notebook: reproduce_makin_2018.ipynb\n  output: claim:fig2-sagittal-better\n  notes: y has the higher SNR in 23 of 24 decoder and variable pairs; the exception is the static\n    rEFH's velocity (y minus x -0.06 dB). Linear regression's velocity margin is 0.01 dB. With rEFH\n    seed 2 all 24 hold; with seed 1 and with the code's kinematics 23, with the same exception, so\n    the outcome depends on the training run.\n  deviations:\n  - One session in place of 49; the per-session comparison is this session's.\n  - Sorted units only (111).\n- claim: fig2-linear-worst\n  outcome: reproduced\n  notebook: reproduce_makin_2018.ipynb\n  output: claim:fig2-linear-worst\n  notes: Every other decoder exceeds linear regression for each of the six variables; the smallest\n    margin is 0.45 dB (static rEFH, x position). It holds in every variant (smallest 0.20 dB, KFobs\n    x acceleration, code kinematics).\n  deviations:\n  - One session in place of 49.\n  - Sorted units only (111).\n- claim: fig2-gross-failures\n  outcome: reproduced\n  notebook: reproduce_makin_2018.ipynb\n  output: claim:fig2-gross-failures\n  notes: No decoder has a negative R2 at 64 ms in this session (the lowest is 0.055, linear\n    regression), so the criterion holds trivially; the claim's \"in a few sessions\" cannot be tested\n    on one session. Outside the criterion's 64 ms, the second notebook prints negative R2 at 16 ms,\n    with 80 or 160 s of training and with fractions of the units; at f = 1/8 KFlatent (+KF) diverges\n    (position SNR -76.63 dB).\n  deviations:\n  - One session in place of 49.\n  - Sorted units only (111).\n- claim: fig4-vel-acc-every-session\n  outcome: reproduced\n  notebook: reproduce_makin_2018.ipynb\n  output: claim:fig4-vel-acc-every-session\n  notes: In this session the rEFH (+KF) beats KFobs and the UKF in all 8 velocity and acceleration\n    comparisons, by 1.04 to 1.81 dB, and in every variant (smallest margin 1.05 dB). The criterion's\n    second part, the bootstrap across sessions at p < 0.01, cannot be run on one session; the\n    outcome rests on the per-session part, which the claims file names as testable on one\n    session.\n  deviations:\n  - One session in place of 49; the bootstrap part of the criterion is not tested.\n  - Sorted units only (111); the UKF is a re-implementation of Li's UKF2.\n- claim: fig4-advantage-grows\n  outcome: blocked\n  blocked_by: too_large\n  notes: The regression of rEFH (+KF) SNR on KFobs SNR runs over all sessions and both axes; one\n    session gives two points and no degrees of freedom for the F-test. See fig2-refh-kf-best for\n    the other sessions and the estimate.\n- claim: fig4-position\n  outcome: blocked\n  blocked_by: too_large\n  notes: Needs the bootstrap over the 49 sessions; see fig2-refh-kf-best. On the one session the\n    rEFH (+KF) position SNR exceeds KFobs's by 0.91 dB and the UKF's by 0.28 dB, which does not\n    decide the outcome.\n- claim: fig4-best-variable\n  outcome: not_reproduced\n  notebook: reproduce_makin_2018.ipynb\n  output: claim:fig4-best-variable\n  notes: Position is the best-decoded variable for all three decoders. The rEFH (+KF) has 5.91 dB\n    for position against 5.06 for velocity and 2.36 for acceleration; KFobs (5.00, 3.30, 1.02) and\n    the UKF (5.63, 3.82, 1.11) have position highest, as the paper says. The ordering is the same\n    with the other rEFH seeds and the code's kinematics, and at every bin width in the second\n    notebook.\n  deviations:\n  - One session in place of 49.\n  - Sorted units only (111).\n- claim: fig4-task-similar\n  outcome: blocked\n  blocked_by: too_large\n  notes: The comparison is of monkey C's two sessions with the range of monkey I's 37 sessions; the\n    dandiset holds one monkey I session, not among the 37. Monkey I's sessions are on Zenodo (see\n    fig2-refh-kf-best for the estimate); monkey C's data are named only by the preprint (Dyer et\n    al., biorxiv 080861), with no archive identifier to pin, so they could not be used either.\n- claim: fig5-vel-acc-all-bins\n  outcome: blocked\n  blocked_by: too_large\n  notes: Needs the bootstrap over the 49 sessions at four bin widths; the decoders at 16 ms alone\n    took 513 s on this session's 111 units. See fig2-refh-kf-best. On the one session the WF\n    exceeds the rEFH (+KF) at 16 ms for velocity (by 0.29 dB) and acceleration (0.44 dB), which\n    does not decide the outcome.\n- claim: fig5-position-bins\n  outcome: blocked\n  blocked_by: too_large\n  notes: Needs the pairwise bootstrap over the 49 sessions at four bin widths; see\n    fig2-refh-kf-best and fig5-vel-acc-all-bins.\n- claim: fig5-advantage-with-binwidth\n  outcome: reproduced\n  notebook: binwidth_training_neurons.ipynb\n  output: claim:fig5-advantage-with-binwidth\n  notes: The rEFH (+KF) SNR rises from 3.01 to 5.46 dB (velocity) and 0.96 to 2.39 dB\n    (acceleration) from 16 to 128 ms, with no fall between neighbouring widths. Its advantage over\n    the best decoder other than the two rEFH decoders rises from -0.29 to 1.60 dB (velocity) and\n    -0.44 to 1.14 dB (acceleration), and in percent from -8.9 to 41.6% and -31.3 to 92.0%, so the\n    claim holds under both readings. The WF's velocity SNR does not improve with width (3.30 to\n    3.18 dB); the criterion tests only the rEFH (+KF).\n  deviations:\n  - One session in place of 49.\n  - Sorted units only (111); the UKF is a re-implementation of Li's UKF2.\n- claim: fig5-derivative-order\n  outcome: partially_reproduced\n  notebook: binwidth_training_neurons.ipynb\n  output: claim:fig5-derivative-order\n  notes: The mean SNR of the six non-rEFH decoders falls from position to velocity to acceleration\n    at all four widths (64 ms, 3.79, 3.06 and 0.99 dB). The percent advantage of the rEFH (+KF)\n    rises from position to velocity to acceleration at 32, 64 and 128 ms (64 ms, 4.9, 32.6 and\n    76.5%) but not at 16 ms, where it is -6.2, -8.9 and -31.3%. Both parts hold at 3 of 4 widths,\n    which the criterion grades as partial. The statement's exception (the rEFH best at velocity)\n    does not hold; the rEFH (+KF) decodes position best at every width.\n  deviations:\n  - One session in place of 49.\n  - Sorted units only (111).\n- claim: fig6-training-time\n  outcome: blocked\n  blocked_by: too_large\n  notes: Parts (ii) and (iii) need the bootstrap over the 49 sessions; see fig2-refh-kf-best. On\n    the one session, with 80 s of training KFlatent (+KF) has a higher position SNR than the rEFH\n    (+KF) (3.43 against 2.54 dB), and the rEFH (+KF) has the highest velocity and acceleration SNR\n    at 80, 160 and 320 s, which does not decide the outcome.\n- claim: fig7-vel-acc-neurons\n  outcome: blocked\n  blocked_by: too_large\n  notes: Needs the bootstrap over the 49 sessions at each fraction; see fig2-refh-kf-best.\n- claim: fig7-position-neurons\n  outcome: blocked\n  blocked_by: too_large\n  notes: Needs the bootstrap over the 49 sessions at each fraction; see fig2-refh-kf-best.\n- claim: fig7-affine-position\n  outcome: not_reproduced\n  notebook: binwidth_training_neurons.ipynb\n  output: claim:fig7-affine-position\n  measured: [0.995, 0.995, 0.986, 0.991]\n  notes: Correlations of position SNR with f are 0.995 (linear regression), 0.995 (static KFlatent),\n    0.986 (WF) and 0.991 (static rEFH) under reading a, and 0.956, 0.948, 0.954 and 0.914 with log2\n    f (reading b); all are within tolerance. Static KFlatent does not have the lowest correlation\n    under either reading (the WF has under a, the static rEFH under b), so the ordering condition\n    fails under both. At f = 1/8 and 1/4 (13 and 27 units) the position SNR of these decoders is\n    within 0.33 dB of zero, so the correlations rest mostly on f = 1/2 and 1.\n  deviations:\n  - One session in place of 49; fractions of 111 sorted units (13, 27, 55 and 111).\n- claim: fig7-kinematic-model-saturates\n  outcome: reproduced\n  notebook: binwidth_training_neurons.ipynb\n  output: claim:fig7-kinematic-model-saturates\n  notes: Under reading b (1/8 to 1/2) the position SNR of KFobs, KFlatent (+KF), the UKF and the\n    rEFH (+KF) rises 6.67, 207.33, 6.93 and 6.22 dB per unit f, faster than from 1/2 to 1 (3.79,\n    6.27, 4.95, 5.79) and faster than the largest initial slope of the static decoders (5.00,\n    static KFlatent). Under reading a (1/8 to 1/4) it fails for KFobs, the UKF and the rEFH (+KF),\n    whose position SNR is slightly lower at 1/4 than at 1/8. KFlatent (+KF)'s large slope comes\n    from its filter diverging at f = 1/8 (-76.63 dB).\n  deviations:\n  - One session in place of 49; fractions of 111 sorted units.\n- claim: fig8-velocity-variants\n  outcome: not_reproduced\n  notebook: reproduce_makin_2018.ipynb\n  output: claim:fig8-velocity-variants\n  measured: [0.11, -0.08]\n  notes: Static velocity SNR is 0.11 dB lower without the updated visible units (text 0.7, figure 8\n    about 0.3) and 0.08 dB higher, not lower, with standard-normal units on standardized counts\n    (text 0.4). With the code's transform 2 sqrt(R + 3/8) the standard-normal rEFH loses 2.11 dB.\n    Under the dynamic mapping the canonical rEFH (+KF) exceeds the variants by 0.15, 0.15 and 1.68\n    dB, so that part holds. The static rEFH's own velocity advantage over the UKF is 0.05 dB in\n    this session, against about 0.94 dB in figure 8. Neither standard-normal reading matches.\n  deviations:\n  - One session in place of 49.\n  - Sorted units only (111).\n  - The standard-normal rEFH uses the code's learning rate for such units (mw0 = 200, setParams.m).\n- claim: fig8-position-variants\n  outcome: blocked\n  blocked_by: too_large\n  notes: The dynamic part needs the bootstrap over the 49 sessions; see fig2-refh-kf-best. On the\n    one session the canonical static rEFH has a higher position SNR (1.46 dB) than both variants\n    (1.43 and 1.38), which does not decide the outcome.\n- claim: fig8-gaussian-still-beats-ukf\n  outcome: reproduced\n  notebook: reproduce_makin_2018.ipynb\n  output: claim:fig8-gaussian-still-beats-ukf\n  assumed: true\n  notes: Trained on standardized counts, the standard-normal rEFH (+KF) exceeds the UKF by 1.09 dB\n    for velocity and 1.17 dB for acceleration. Trained on the code's transform it is 0.43 dB below\n    the UKF for velocity and 0.12 dB above for acceleration, so the claim fails under the code's\n    reading. Question for the paper's authors (finding below) were the standard-normal visible\n    units fed standardized counts, as the Results say, or 2 sqrt(R + 3/8), as getLatentsBMI.m\n    does?\n  deviations:\n  - One session in place of 49.\n  - The input of the standard-normal rEFH is the standardized counts the Results name (z-scored\n    with the training mean and SD), as the claims file makes its main reading; the code's\n    transform changes the outcome.\n  - The UKF is a re-implementation of Li's UKF2.\n- claim: fig9-taps\n  outcome: blocked\n  blocked_by: too_large\n  notes: Part (ii) needs the bootstrap over the 49 sessions at three bin widths; see\n    fig2-refh-kf-best. The tapped decoders were not implemented in this run.\n- claim: kflatent-modest\n  outcome: reproduced\n  notebook: reproduce_makin_2018.ipynb\n  output: claim:kflatent-modest\n  notes: Reading a (velocity), the better KFlatent decoder exceeds KFobs by 0.10 dB and the UKF by\n    0.51 dB; reading b (velocity and acceleration) 0.08 and 0.30 dB; reading c (all three) KFlatent\n    is 0.20 dB below KFobs. With the code's kinematics readings a and b fail (0.49 and 0.39 dB for\n    KFlatent against 0.38 and 0.22 for the UKF) and reading c holds (0.07 against 0.32 dB), so the\n    claim holds under one reading with either kinematics.\n  deviations:\n  - One session in place of 49.\n  - Sorted units only (111); the UKF is a re-implementation of Li's UKF2.\n- claim: advantage-grows-with-derivative\n  outcome: reproduced\n  notebook: binwidth_training_neurons.ipynb\n  output: claim:advantage-grows-with-derivative\n  notes: The percent advantage of the rEFH (+KF) over the best non-rEFH decoder rises from position\n    to velocity to acceleration with 80 s (-26.1, 10.9, 76.4%), 160 s (2.4, 32.5, 71.3%) and 320 s\n    (4.9, 32.6, 76.5%) of training. It also rises at each amount when the shorter trainings are\n    scored only on the bins after 320 s.\n  deviations:\n  - One session in place of 49.\n  - For 80 and 160 s of training the paper does not say which bins are tested; the code tests on\n    every bin after the training bins (getLatentsBMI.m, getTestBins), and this is the main reading.\n    Scoring on the bins after 320 s gives the same outcome.\n- claim: static-refh-position-worse\n  outcome: blocked\n  blocked_by: too_large\n  notes: Needs the bootstrap over the 49 sessions, and depends on fig4-position, which is blocked;\n    see fig2-refh-kf-best. On the one session the static rEFH's position SNR is 4.17 dB below the\n    UKF's (1.46 against 5.63), which does not decide the outcome.\nfindings:\n- kind: data_missing\n  statement: The dandiset holds one session of one of the paper's three monkeys (monkey I, M1 array,\n    649.1 s with kinematics), released for the Neural Latents Benchmark. The paper used 49 sessions.\n    The file dates the session 2017-02-02, which is not in the paper's list of monkey I sessions\n    (NeuralAnalysis/Indy_HC_Sessions.csv, ending 2017-01-31) nor among the files of the Zenodo\n    record the paper cites (doi:10.5281/zenodo.583331), so it is probably not one of the paper's\n    sessions, though the dandiset names the paper as describing it. The paper's tests across\n    sessions cannot be run on the dandiset.\n- kind: data_missing\n  statement: The units table holds sorted units only (ids are channel times 100 plus 1 to 4). The\n    paper kept an unsorted hash unit for every channel and counted them among its 171 to 413 units\n    per monkey I session; without them 111 units pass the 0.5 Hz cut.\n- kind: selection_undocumented\n  statement: The training file has three gaps of 0.1 s (162.2 to 162.3, 324.5 to 324.6 and 486.8 to\n    486.9 s) where every behavioural series is NaN and no unit has a spike, splitting it into four\n    segments; neither the file nor the dandiset says what was removed. The test file (190.3 s, 98\n    units) has no kinematics, so it cannot be used to score decoding.\n- kind: code_mismatch\n  statement: The Methods decode the fingertip position low-pass filtered at 10 Hz and subsampled\n    per bin; the paper's code (getLatentsBMI.m, binSpikeCounts.m) decodes the cursor position with\n    the filter commented out and averages each bin. The two readings change the outcome of\n    fig2-velocity-boost. Question for the paper's authors, which kinematics were decoded?\n- kind: code_mismatch\n  statement: The Results say the standard-normal rEFH variant was trained on standardized spike\n    counts; the code (getLatentsBMI.m) feeds it 2 sqrt(R + 3/8). The two readings change the outcome\n    of fig8-gaussian-still-beats-ukf. Question for the paper's authors, which input was used for\n    figure 8?\n- kind: methods_unavailable\n  statement: The UKF follows Li's UKF2 package (fit_ar_ukf_hist_rrcv.m, ar_ukf_hist.m), which the\n    paper's repository calls but does not hold; the attempt re-implemented it from the paper's\n    description (linear state transition, tuning to the six states, their magnitudes and the\n    position-velocity products, regression with full noise covariances, standard unscented\n    transform). Question for the paper's authors, can the UKF2 code and its ridge setting be\n    published with the paper's code?\n"
}
```

```
File created successfully at: attempts/000129-makin-2018-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
. $TMPDIR/ev/bin/activate && python -c "
import yaml; a=yaml.safe_load(open('attempts/000129-makin-2018-01.yaml')); print(len(a['outcomes']))
c=yaml.safe_load(open('claims/000129/10.1088-1741-2552-aa9e95.yaml')); ids=[x['id'] for x in c['claims']]; o=[x['claim'] for x in a['outcomes']]
print(len(ids), set(ids)-set(o), set(o)-set(ids))
from collections import Counter; print(Counter(x['outcome'] for x in a['outcomes']))
"; python tools/entry.py check entries/000129-makin-2018 2>&1 | tail -5; date -u
```

```
31
31 set() set()
Counter({'blocked': 13, 'reproduced': 10, 'not_reproduced': 6, 'partially_reproduced': 2})
0 error(s)
Wed Oct 28 20:57:46 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='attempts/000129-makin-2018-01.yaml'; s=open(p).read()
old='''    (NeuralAnalysis/Indy_HC_Sessions.csv, ending 2017-01-31) nor among the files of the Zenodo
    record the paper cites (doi:10.5281/zenodo.583331), so it is probably not one of the paper's
    sessions, though the dandiset names the paper as describing it.'''
new='''    (NeuralAnalysis/Indy_HC_Sessions.csv, ending 2017-01-31), so it is probably not one of the
    paper's sessions, though the dandiset names the paper as describing it. The paper's own
    sessions are on Zenodo (doi:10.5281/zenodo.583331).'''
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
p='entries/000129-makin-2018/entry.yaml'; s=open(p).read()
s=s.replace('runtime_minutes: 12','runtime_minutes: 10').replace('runtime_minutes: 17','runtime_minutes: 22'); open(p,'w').write(s)
EOF
cat > entries/000129-makin-2018/README.md <<'EOF'
# Makin, O'Doherty, Cardoso & Sabes (2018) from dandiset 000129

Tests the findings of [Makin et al. (2018)](https://doi.org/10.1088/1741-2552/aa9e95) that can be
tested on [DANDI:000129](https://dandiarchive.org/dandiset/000129/0.241017.1444), which holds one
session of monkey I (M1 array, 649 s of sorted-unit spikes with kinematics) from the Neural Latents
Benchmark. The paper compared eight decoders over 49 sessions from three monkeys; the session in
the dandiset is dated 2017-02-02, which is not in the paper's session list. All eight decoders are
re-implemented here from the paper's Methods and code (`makin.py`).

| Claim | Outcome |
|---|---|
| Units per monkey I session after the 0.5 Hz cut, 171 to 413 | Not reproduced (111; no hash units in the file) |
| rEFH (+KF) velocity gain over linear regression, more than twice KFobs's and nearly twice the UKF's | Not reproduced (rests on the Methods kinematics) |
| The dynamic map changes KFlatent little | Reproduced |
| The static rEFH decodes velocity and acceleration best among the other decoders | Reproduced |
| The dynamic map adds about 3 dB to the rEFH's position SNR | Not reproduced (4.45 dB) |
| y is decoded better than x for every decoder and variable | Partially reproduced (23 of 24) |
| Linear regression is the worst decoder | Reproduced |
| Negative R2 only for the UKF and KFlatent (+KF) | Reproduced (no negative R2 at 64 ms) |
| rEFH (+KF) beats KFobs and the UKF for velocity and acceleration in every session | Reproduced for this session |
| Velocity is the rEFH's best-decoded variable | Not reproduced (position is) |
| KFlatent only modestly better than KFobs, the UKF more | Reproduced |
| Velocity losses of the rEFH variants, 0.7 and 0.4 dB | Not reproduced |
| The standard-normal rEFH still beats the UKF | Reproduced (rests on standardized counts) |
| The rEFH's advantage grows with bin width | Reproduced |
| Quality falls and the advantage grows with derivative order | Partially reproduced (3 of 4 widths) |
| The advantage grows with derivative order for each amount of training data | Reproduced |
| Static decoders' position SNR is affine in the fraction of neurons, KFlatent the most curved | Not reproduced |
| Decoders with a kinematic model rise faster, then saturate | Reproduced |
| Tests across the paper's 49 sessions (13 claims) | Blocked: too large |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Most of the paper's findings are averages or bootstrap tests over its 49 sessions. Here they are
tested on the one session the dandiset holds, and those that need the bootstrap are blocked. The
attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000129-makin-2018-01.yaml`](../../attempts/000129-makin-2018-01.yaml).
EOF
. $TMPDIR/ev/bin/activate && python tools/entry.py check entries/000129-makin-2018 2>&1 | tail -3 && python tools/entry.py handover entries/000129-makin-2018 2>&1 | tail -5; ls executed/000129-makin-2018/handover; git status --short
```

```
0 error(s)
wrote executed/000129-makin-2018/handover
10.1088-1741-2552-aa9e95.yaml
binwidth_training_neurons.ipynb
makin.py
reproduce_makin_2018.ipynb
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
?? attempts/000129-makin-2018-01.yaml
?? entries/000129-makin-2018/
?? scripts
```

**Agent calls Bash**

```bash
ls -la .bash_profile .bashrc .gitconfig .idea .mcp.json .profile .ripgreprc .vscode .zprofile .zshrc scripts 2>&1 | head -20; ls entries/000129-makin-2018
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 28 18:55 .bash_profile
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 28 18:55 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 28 18:55 .gitconfig
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 28 18:55 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 28 18:55 .mcp.json
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 28 18:55 .profile
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 28 18:55 .ripgreprc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 28 18:55 .vscode
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 28 18:55 .zprofile
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 28 18:55 .zshrc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 28 18:55 scripts
README.md
__pycache__
binwidth_training_neurons.ipynb
entry.yaml
makin.py
reproduce_makin_2018.ipynb
requirements.in
requirements.lock.txt
```

**Agent calls Bash**

```bash
rm -rf entries/000129-makin-2018/__pycache__; . $TMPDIR/ev/bin/activate && python tools/entry.py check entries/000129-makin-2018 2>&1 | tail -1; date -u
```

```
0 error(s)
Wed Oct 28 20:59:23 UTC 2026
```

**Agent**

I've finished steps 1 to 6 of the Author section. The entry `entries/000129-makin-2018/` passes `entry.py check`, both notebooks ran from a clean environment, and the handover package is in `executed/000129-makin-2018/handover/`. The record is `attempts/000129-makin-2018-01.yaml`. Of 31 claims, 10 are reproduced, 2 partially reproduced, 6 not reproduced and 13 blocked. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| units-monkey-i | not reproduced: 111 units, and the file has no hash units |
| fig2-velocity-boost | not reproduced, assumed: KFobs ratio 1.92, needs more than 2; the code's kinematics give 2.05 |
| fig2-kflatent-dynamic-little-effect | reproduced |
| fig2-refh-static-vel-acc | reproduced (velocity margin only 0.05 dB) |
| fig2-position-dynamic-gain | not reproduced: 4.45 dB against 3 ± 0.5 |
| fig2-sagittal-better | partially reproduced: 23 of 24 pairs (24 of 24 with one other rEFH seed) |
| fig2-linear-worst | reproduced |
| fig2-gross-failures | reproduced, but only because no R2 is negative at 64 ms |
| fig4-vel-acc-every-session | reproduced for the per-session part; the bootstrap can't run on one session |
| fig4-best-variable | not reproduced: the rEFH (+KF) decodes position best |
| kflatent-modest | reproduced (holds under one reading with either kinematics) |
| fig8-velocity-variants | not reproduced: losses of 0.11 and −0.08 dB against 0.7 and 0.4 |
| fig8-gaussian-still-beats-ukf | reproduced, assumed (standardized counts); fails with the code's transform |
| fig5-advantage-with-binwidth | reproduced |
| fig5-derivative-order | partially reproduced: 3 of 4 widths, fails at 16 ms |
| advantage-grows-with-derivative | reproduced |
| fig7-affine-position | not reproduced: correlations within tolerance, but static KFlatent is not the lowest |
| fig7-kinematic-model-saturates | reproduced under reading b only |
| 13 claims needing the bootstrap or regression across 49 sessions, plus fig4-task-similar | blocked, `too_large` |

## 2. Dataset, assumptions, questions

**Dataset**
- Only one published version exists, 0.241017.1444, so I pinned it. The draft holds the same two assets and differs only in its title.
- It holds one monkey I session, M1 only. The file dates it 2017-02-02, which is not in the paper's session list (`Indy_HC_Sessions.csv` ends 2017-01-31).
- The units are sorted only; the hash units the paper counted are missing.
- Three 0.1 s gaps in the training file have NaN kinematics and no spikes, and nothing documents them.
- The test file (190 s) has no kinematics, so only the 649 s training file is usable.
- The test file does not repeat the training file. Spikes and kinematics share one clock: velocity decodes best from spikes 64 ms earlier.

**Assumptions** (both are the main readings the claims file already chose; the alternative changes the outcome, so the outcome is marked `assumed`)
- Kinematics: the Methods' filtered fingertip position, not the code's unfiltered cursor position. This decides fig2-velocity-boost.
- Standard-normal rEFH input: standardized counts as the Results say, not the code's 2√(R+3/8). This decides fig8-gaussian-still-beats-ukf.

**Questions for the paper's authors** (recorded as findings)
- Which kinematics were decoded: filtered fingertip or unfiltered cursor?
- Which input did the standard-normal variant use?
- Can Li's UKF2 fitting code be published? It is called by the repository but not in it, so I re-implemented the UKF.

I asked no reader any questions.

## 3. Where the protocol was unclear

1. **Blocked reason for claims needing the other sessions.** The paper's sessions are public on Zenodo, so `data_missing` doesn't fit, and the claims are `data: dataset`, not `elsewhere`. I used `too_large`, with an estimate scaled from timing this one session, not a timed run on a larger one.
2. **A criterion where only one part can be tested** (per-session plus bootstrap, in fig4-vel-acc-every-session). The protocol doesn't say how to grade this. I graded the testable part and listed the untested part as a deviation.
3. **A criterion that holds trivially** (fig2-gross-failures, no failures at all). I recorded it as reproduced and said so in the notes.
4. **Several claims share one costly fit**, so "each claim's section its own generator" doesn't fit. I seeded each fit configuration instead and showed two extra rEFH seeds as a variant.
5. **Seeds can change an outcome** (fig2-sagittal-better), but the protocol treats a seed as a detail that can't. I kept seed 0 and reported the others.

## 4. Runtime and failures

- **Clean run:** 604 s for the 64 ms notebook and 1301 s for the bin-width/training/neuron notebook. The second is under the 30-minute limit, but not by much.
- **Background run lost:** my first background development run was killed with its sandbox, costing about 20 minutes; everything after ran in the foreground.
- **Small fixes:** one code bug (the SNR helper returned an array) was fixed before the clean run.
- **Not run:** the tapped decoders for fig9-taps (that claim is blocked anyway).

The run finished at 21:00 UTC.

## End of run

74 turns, 119 minutes, result: success.
