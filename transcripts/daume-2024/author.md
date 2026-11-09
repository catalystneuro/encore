# 001187 · author · run 41284150060

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls claims/001187 paper entries | head -50
```

```
<persisted-output>
Output too large (36.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/067462e8-2fc2-40f0-88f7-410db8f2a5d1/tool-results/blzy11214.txt

Preview (first 2KB):
Sun Nov  1 07:21:09 UTC 2026
# Protocol for an attempt

Version: `pilot-13`. Record this version in the attempt's provenance.

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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/067462e8-2fc2-40f0-88f7-410db8f2a5d1/tool-results/blzy11214.txt"
}
```

```
1	Sun Nov  1 07:21:09 UTC 2026
2	# Protocol for an attempt
3	
4	Version: `pilot-13`. Record this version in the attempt's provenance.
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
[... 669 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md | head -80; wc -l docs/design.md docs/archives.md; ls paper; cat claims/001187/*.yaml
```

```
<persisted-output>
Output too large (55.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/067462e8-2fc2-40f0-88f7-410db8f2a5d1/tool-results/bsd9rw5av.txt

Preview (first 2KB):
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
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
ls paper; wc -c paper/*; cat claims/001187/*.yaml | head -400
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001187/*.yaml | sed -n 400,900p
```

```
test: mixed-effects GLM
    p: 0.0029
  depends_on:
  - category-neuron-counts
  expected:
  - {quantity: confidence by area beta, value: 16.88, tolerance: 1.69}
  - {quantity: LTM accuracy by area beta, value: 59.78, tolerance: 5.98}
  - {quantity: three-way interaction beta, value: -28.64, tolerance: 2.86}
  criterion: As NWB_computeGLM.m, which is the paper's code for this panel. Category neurons of C in
    both areas; one row per WM picture later shown in the LTM test; maintenance rate 0 to 2.5 s after
    maintenance onset, normalized as B (mean baseline over all the neuron's rows); then rows kept
    when the WM trial was correct and the picture is of the preferred category, with a confidence
    rating; confidence recoded as the Methods say (forgotten sure 1, unsure 2, guessing 3; remembered
    guessing 1, unsure 2, sure 3; the code maps 4, 5, 6 to 1, 2, 3 and keeps 1, 2, 3, which is the
    same under L); FR ~ LTMacc * conf * area with the random effects of G, area with amygdala as
    reference so that the interactions are hippocampus minus amygdala. Outliers O-M for the main
    result, O-C (the code) shown as a variant. Reproduced when the three interactions with area have
    p < 0.05 with the reported signs and betas within tolerance, and the main effects and the LTMacc
    by conf interaction have p >= 0.05; partially reproduced when the three interactions hold in sign
    and significance with a beta out of tolerance or a main effect significant.
[... 368 more lines not kept]
```

**Agent calls Bash**

```bash
ls entries/001453-fouke-2025/ attempts/ | tail -5; cat entries/001453-fouke-2025/entry.yaml entries/001453-fouke-2025/requirements.in; ls entries/001453-fouke-2025; grep -n "DANDI" -A60 docs/archives.md | head -120
```

```
entry.yaml
omr.py
reproduce_fouke_2025.ipynb
requirements.in
requirements.lock.txt
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
[... 140 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/001453-fouke-2025-01.yaml | head -150; cat entries/001453-fouke-2025/README.md | head -30
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
[... 159 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^findings" -A30 attempts/001453-fouke-2025-01.yaml | head -50; grep -n "blocked_by" -B3 -A8 attempts/001453-fouke-2025-01.yaml | head -30; ls schemas; python tools/entry.py --help 2>&1 | head -30
```

```
243:findings:
244-- kind: data_missing
245-  statement: The dandiset holds only the freely swimming tracking of Figure 1 and Figure S1. The
246-    two-photon imaging and the head-fixed tail tracking behind Figures 2 to 4 are not in it, and
247-    the GitLab repository the paper names for all behavioural and imaging data holds analysis
248-    notebooks only. Nine of the paper's main findings cannot be tested.
249-- kind: metadata_insufficient
250-  statement: The stimulus codes 0 to 20 have no names or description in the files or the
251-    dandiset metadata. They can be named only from the paper's analysis notebook and the protocol
252-    file of its stimulus software.
253-- kind: code_mismatch
254-  statement: The paper's analysis notebook labels code 9 as lateral right and 11 as lateral left,
255-    while its conversion of the stimulus software's names gives the reverse (it carries a remap
256-    that swaps them). The data do not settle which is right; zebrafish barely turn to either, and
257-    Danionella turn more to the right for code 11, which fits the stimulus software's assignment
258-    only if the fish turn with lateral motion.
259-- kind: metadata_error
260-  statement: Subject ids 0 to 11 are each used for one zebrafish and one Danionella cerebrum, so
261-    subject_id does not identify an animal. The archive's summary counts 25 subjects and lists
262-    only Danio rerio; the files hold 37 fish of two species.
[... 75 more lines not kept]
```

**Agent**

Now the dataset.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/001187/ | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/001187/versions/" | python -m json.tool | grep -E '"version"|"modified"|"status"|asset_count|size'
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
grep -n -i "dandi\|001187\|zenodo\|github" paper/10.1016-j.neuron.2024.09.013.txt | head; curl -s "https://api.dandiarchive.org/api/dandisets/001187/versions/0.240904.2347/assets/?page_size=100" | python -c "
import json,sys; d=json.load(sys.stdin); print(d['count'])
for a in d['results']: print(a['path'], a['size']//1e6, a['asset_id'])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q env && source env/bin/activate && uv pip install -q h5py remfile pynwb numpy pandas scipy statsmodels matplotlib nbformat nbclient ipykernel 2>&1 | tail -2; python -c "import pynwb,statsmodels;print(pynwb.__version__, statsmodels.__version__)"
```

```
4.2.0 0.15.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && cat > probe.py <<'EOF'
import h5py, remfile, requests, time
aid="0af57771-798c-46c0-a5fc-0ef7dbad1597"
url=f"https://api.dandiarchive.org/api/assets/{aid}/download/"
r=requests.head(url,allow_redirects=True); s3=r.url.split('?')[0]; print(s3)
t=time.time()
f=h5py.File(remfile.File(s3),'r')
def show(name,obj):
    if isinstance(obj,h5py.Dataset): print(name,obj.shape,obj.dtype, dict((k,v) for k,v in obj.attrs.items() if k in('unit','description')))
    else:
        d=obj.attrs.get('description'); print(name+'/', obj.attrs.get('neurodata_type'), d if d is None else str(d)[:200])
f.visititems(lambda n,o: show(n,o) if not n.startswith('stimulus/templates') or n.count('/')<3 else None)
print(time.time()-t)
EOF
python probe.py 2>&1 | grep -v "^stimulus/templates/.*/" | head -150
```

```
https://dandiarchive.s3.amazonaws.com/blobs/3df/2bc/3df2bcf0-8ab4-4fac-9834-ae4569e85224
acquisition/ None None
acquisition/events_LTM/ TimeSeries The events correspond to the TTL markers for each trial of the New-Old task. The TTL markers are the following: 2 = Fixation Cross (The first 2 signals the beginning of the New-Old Experiment, 1 = Pic
acquisition/events_LTM/data (1201,) int8 {'unit': 'NA'}
acquisition/events_LTM/timestamps (1201,) float64 {'unit': 'seconds'}
acquisition/events_WM/ TimeSeries The events correspond to the TTL markers for each trial of the Sternberg task. The TTL markers are the following: 61 = Start of the Sternberg Experiment, 11 = Fixation Cross, 1 = Picture #1 Shown, 2 =
acquisition/events_WM/data (982,) int8 {'unit': 'NA'}
acquisition/events_WM/timestamps (982,) float64 {'unit': 'seconds'}
acquisition/events_raw_LTM/ TimeSeries The events correspond to the TTL markers for the New-Old task. These are the raw events from the recording. 
acquisition/events_raw_LTM/data (1604,) int8 {'unit': 'NA'}
acquisition/events_raw_LTM/timestamps (1604,) float64 {'unit': 'seconds'}
acquisition/events_raw_WM/ TimeSeries The events correspond to the TTL markers for the Sternberg task. These are the raw events from the recording. 
acquisition/events_raw_WM/data (1263,) int8 {'unit': 'NA'}
acquisition/events_raw_WM/timestamps (1263,) float64 {'unit': 'seconds'}
analysis/ None None
file_create_date (2,) object {}
general/ None None
general/devices/ None None
general/devices/NLX-microwires-145/ Device Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electr
general/devices/NLX-microwires-146/ Device Recordings were performed with Macro-Micro Hybrid Depth Electrodes with Behnke Fried/Micro Inner Wire Bundle in which each individual microwire has a diameter of 40 microns. Likwise, each Depth Electr
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && cat > survey.py <<'EOF'
import h5py, remfile, requests, json, numpy as np, collections
from concurrent.futures import ThreadPoolExecutor
V="0.240904.2347"
assets=requests.get(f"https://api.dandiarchive.org/api/dandisets/001187/versions/{V}/assets/?page_size=100").json()['results']
def s3(aid):
    return requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=True).url.split('?')[0]
def one(a):
    f=h5py.File(remfile.File(s3(a['asset_id'])),'r')
    g=lambda p: f[p][()].decode() if isinstance(f[p][()],bytes) else f[p][()]
    out=dict(path=a['path'])
    for k in ['general/subject/subject_id','general/subject/age','general/subject/sex','general/subject/description','session_description','general/session_id','identifier','general/notes','general/experiment_description','general/institution','general/source_script']:
        try: out[k.split('/')[-1]]=str(g(k))[:300]
        except Exception as e: out[k.split('/')[-1]]=None
    loc=[x.decode() for x in f['general/extracellular_ephys/electrodes/location'][:]]
    ue=f['units/electrodes'][:]
    eid=f['general/extracellular_ephys/electrodes/id'][:]
    out['unit_locs']=dict(collections.Counter(loc[i] for i in ue))
    out['nunits']=len(ue); out['nwm']=f['intervals/WM_trials/id'].shape[0]; out['nltm']=f['intervals/LTM_trials/id'].shape[0]
    out['eid_eq_index']=bool((eid==np.arange(len(eid))).all())
    out['nspikes']=f['units/spike_times'].shape[0]
    return out
with ThreadPoolExecutor(12) as ex: res=list(ex.map(one,assets))
json.dump(res,open('survey.json','w'),indent=1)
EOF
time python survey.py && python -c "
import json; r=json.load(open('$TMPDIR/survey.json'))
print({k:v for k,v in r[0].items()})
for x in sorted(r,key=lambda x:x['path']): print(x['path'].split('/')[1][:14], x['session_id'], x['subject_id'],x['age'],x['sex'],x['nunits'],x['nwm'],x['nltm'],x['unit_locs'],x['eid_eq_index'])
"
```

```
real	0m53.854s
user	0m2.215s
sys	0m0.351s
{'path': 'sub-12/sub-12_ses-2_ecephys+image.nwb', 'subject_id': '12', 'age': 'P30Y', 'sex': 'F', 'description': 'Subject metadata', 'session_description': 'SBCAT_NO_ID: 12', 'session_id': '2', 'identifier': 'sub-12_ses-2_P70CS', 'notes': '(1) Experiment variant: 3. (2) The session start time has been set to Jan 1st of the recording year to avoid disclosure of protected health information (PHI).', 'experiment_description': 'This data contains electrophysiological recordings and behavior from the Sternberg and New-Old tasks performed in patients with intractable epilepsy implanted with depth electrodes and Behnke-Fried microwires in the human medial temporal lobe and medial frontal cortex.', 'institution': 'Cedars-Sinai Medical Center', 'source_script': 'NWB_SBCAT_NO_export_main.m', 'unit_locs': {'amygdala_left': 3, 'amygdala_right': 2, 'hippocampus_right': 1}, 'nunits': 6, 'nwm': 140, 'nltm': 161, 'eid_eq_index': True, 'nspikes': 30922}
sub-1_ses-2_ec 2 1 P59Y F 24 140 400 {'amygdala_left': 12, 'hippocampus_left': 7, 'amygdala_right': 5} True
sub-10_ses-1_e 1 10 P54Y M 23 140 400 {'hippocampus_left': 13, 'amygdala_right': 7, 'hippocampus_right': 3} True
sub-11_ses-1_e 1 11 P41Y F 15 139 400 {'amygdala_left': 6, 'hippocampus_left': 3, 'amygdala_right': 1, 'hippocampus_right': 5} True
sub-12_ses-1_e 1 12 P30Y F 15 140 400 {'amygdala_left': 2, 'amygdala_right': 12, 'hippocampus_right': 1} True
sub-12_ses-2_e 2 12 P30Y F 6 140 161 {'amygdala_left': 3, 'amygdala_right': 2, 'hippocampus_right': 1} True
sub-13_ses-1_e 1 13 P40Y M 3 140 400 {'amygdala_right': 3} True
sub-14_ses-1_e 1 14 P58Y F 22 140 400 {'amygdala_left': 5, 'amygdala_right': 12, 'hippocampus_right': 5} True
sub-15_ses-1_e 1 15 P23Y M 9 140 400 {'amygdala_right': 9} True
sub-16_ses-1_e 1 16 P24Y F 31 140 395 {'amygdala_left': 18, 'amygdala_right': 7, 'hippocampus_right': 6} True
sub-16_ses-2_e 2 16 P24Y F 4 140 400 {'amygdala_left': 2, 'amygdala_right': 2} True
sub-1
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 -c "
import json; r=json.load(open('survey.json'))
import collections
h=sum(v for x in r for k,v in x['unit_locs'].items() if k.startswith('hipp')); a=sum(v for x in r for k,v in x['unit_locs'].items() if k.startswith('amyg'))
print(len(r), sum(x['nunits'] for x in r), h, a)
print(sorted(set(k for x in r for k in x['unit_locs'])))
for x in sorted(r,key=lambda x:int(x['subject_id'])): print(x['identifier'], x['institution'][:12], x['notes'][:40])
"; grep -n "Table S1" paper/10.1016-j.neuron.2024.09.013.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "Table S1" paper/10.1016-j.neuron.2024.09.013.txt | head; grep -n -i "P54CS\|P54cs" paper/*.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 640,1100p paper/10.1016-j.neuron.2024.09.013.txt | tr '\n' '|' | head -c 9000
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/rutishauserlab/SBCAT-NO-release-NWB.git code 2>&1 | tail -2; cd code && git log --oneline | head -3; find . -name "*.m" | grep -v -i "nwb_util\|matnwb\|helpers/" | head -40
```

```
6d07204 final main
eef0227 Update LICENSE
2db71fb Delete CITATION.cff
./NWB_SBCAT_NO_analysis/NWB_SBCAT_NO_analysis_main.m
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && find . -name "*.m" | xargs ls -la | awk '{print $5, $9}' | grep -v matnwb | head -60
```

```
10119 ./NWB_SBCAT_NO_analysis/NWB_SBCAT_NO_analysis_main.m
7376 ./NWB_SBCAT_NO_analysis/helpers/3rdParty/permutationTest/permutationTest.m
1562 ./NWB_SBCAT_NO_analysis/helpers/3rdParty/randanova1/randanova1.m
2974 ./NWB_SBCAT_NO_analysis/helpers/3rdParty/sort_nat/sort_nat.m
4428 ./NWB_SBCAT_NO_analysis/helpers/3rdParty/stats/anova1_cell.m
3731 ./NWB_SBCAT_NO_analysis/helpers/3rdParty/stats/anova1rm_cell.m
8530 ./NWB_SBCAT_NO_analysis/helpers/3rdParty/stats/anova2_cell.m
6774 ./NWB_SBCAT_NO_analysis/helpers/3rdParty/stats/anova2rm_cell.m
4076 ./NWB_SBCAT_NO_analysis/helpers/3rdParty/stats/concatdata.m
9133 ./NWB_SBCAT_NO_analysis/helpers/3rdParty/stats/finputcheck.m
2648 ./NWB_SBCAT_NO_analysis/helpers/3rdParty/stats/stat_surrogate_pvals.m
24890 ./NWB_SBCAT_NO_analysis/helpers/3rdParty/stats/statcond.m
5888 ./NWB_SBCAT_NO_analysis/helpers/3rdParty/stats/surrogdistrib.m
4634 ./NWB_SBCAT_NO_analysis/helpers/3rdParty/stats/ttest2_cell.m
3107 ./NWB_SBCAT_NO_analysis/helpers/3rdParty/stats/ttest_cell.m
4378 ./NWB_SBCAT_NO_analysis/helpers/custom/NWB_SB_extractUnits.m
1479 ./NWB_SBCAT_NO_analysis/helpers/custom/NWB_SB_filter_session.m
23809 ./NWB_SBCAT_NO_analysis/helpers/custom/NWB_calcCatSelective_SB.m
3182 ./NWB_SBCAT_NO_analysis/helpers/custom/NWB_calcMemSelective_SB.m
5082 ./NWB_SBCAT_NO_analysis/helpers/custom/NWB_computeGLM.m
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/NWB_SBCAT_NO_analysis && cat helpers/internal/etc/rateFilter_units.m helpers/custom/NWB_computeGLM.m helpers/custom/NWB_calcMemSelective_SB.m helpers/custom/condenseAreas.m; grep -v "^\s*%" NWB_SBCAT_NO_analysis_main.m | grep -v "^\s*$" | head -150
```

```
function aboveRate = rateFilter_units(nwbAll,all_units,rateFilter)

aboveRate = ones(length(all_units),1);

for i = 1:length(all_units)
    SU = all_units(i);
    tsEvents_WM = nwbAll{SU.session_count}.acquisition.get('events_raw_WM').timestamps.load;
    tsEvents_LTM = nwbAll{SU.session_count}.acquisition.get('events_raw_LTM').timestamps.load;
    spike_times_WM = all_units(i).spike_times(all_units(i).spike_times<=tsEvents_WM(end));
    spike_times_LTM = all_units(i).spike_times(all_units(i).spike_times>=tsEvents_LTM(1));
    globalRate_WM = length(spike_times_WM)/(tsEvents_WM(end)-tsEvents_WM(1));
    globalRate_LTM = length(spike_times_LTM)/(tsEvents_LTM(end)-tsEvents_LTM(1));
    rateBool = globalRate_WM < rateFilter | globalRate_LTM < rateFilter;
    if rateBool % If the rate is below the filter threshold
        aboveRate(i) = 0;
    end
endfunction m = NWB_computeGLM(nwbAll, all_units, cat_cells_all, params)
%NWB_computeGLM Takes the output of NWB_SB_extractUnits and runs
% a mixed-effects GLM across all category neurons

[... 343 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/NWB_SBCAT_NO_analysis && sed -n 1,200p helpers/custom/NWB_calcCatSelective_SB.m | grep -v "^\s*$" | head -170
```

```
function [sig_cells,areasSternberg] = NWB_calcCatSelective_SB(nwbAll, all_units, params)
%NWB_CALCSELECTIVE Takes the output of NWB_SB_extractUnits and runs
%selectivity tests for the sternberg task. Optionally plots trial aligned
%spikes
if isfield(params,'rateFilter') && ~isempty(params.rateFilter) && params.rateFilter > 0
    rateFilter = params.rateFilter;
else
    rateFilter = [];
end
% Filtering for Global Rate (rateFilter should be a nonzero float)
if ~isempty(rateFilter)
    aboveRate = rateFilter_units(nwbAll,all_units,rateFilter);
else
    aboveRate = ones(length(all_units),1);
end
all_units = all_units(logical(aboveRate));
areasSternberg = cell(length(all_units),1);
cat_cells_sb = zeros(length(all_units),1); 
pref_cat = zeros(length(all_units),1); 
hzPref = zeros(length(all_units),1);
[... 151 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/NWB_SBCAT_NO_analysis/helpers/3rdParty/stats && grep -v "^\s*%" stat_surrogate_pvals.m | grep -v "^\s*$"; grep -n "stat_surrogate_pvals\|tail\|surrogdistrib(" statcond.m | head -20; grep -n "paired\|shuffle\|perm" surrogdistrib.m | head -30
```

```
function pvals = stat_surrogate_pvals(distribution,observed,tail)
numDims = myndims(distribution);
distribution = cat(numDims,distribution,observed);
numDims = myndims(distribution);
[tmp idx] = sort( distribution, numDims,'ascend');
[tmp mx]  = max( idx,[], numDims);
len = size(distribution,  numDims );
pvals = 1-(mx-0.5)/len;
if strcmpi(tail, 'both')
    pvals = min(pvals, 1-pvals);
    pvals = 2*pvals;
end;
function val = myndims(a)
if ndims(a) > 2
    val = ndims(a);
else
    if size(a,1) == 1,
        val = 2;
    elseif size(a,2) == 1,
        val = 1;
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 225,300p paper/10.1016-j.neuron.2024.09.013.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 66,140p paper/10.1016-j.neuron.2024.09.013.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/067462e8-2fc2-40f0-88f7-410db8f2a5d1/tool-results/bwd3q24u4.txt"
}
```

```
1	
2	We recorded single neuron activity from the hippocampus and the amygdala while patients performed the two tasks (Fig. 1b). In total, 883 single units across both brain areas were included in our analyses, 351 from the hippocampus and 532 from the amygdala (see Methods). The same units were recorded for both tasks. The analysis presented here is partly based on a previously published dataset34, but in that report only the WM task was analyzed. Further, more subjects were added in the present manuscript. The LTM part that is the focus of this paper is unpublished. Spike sorting results were assessed quantitatively (Fig. S2). We use the terms neuron, unit, and cell interchangeably to refer to a putative single neuron.
3	
4	Category neurons remain persistently active when their preferred category is held in WM
5	
6	We first selected for neurons whose response following stimulus onset differed significantly between the category of the images shown. We refer to such neurons as ‘category neurons’ throughout (we note that this type of cell is also referred to as visually selective (VS) in other papers36,37,39; The two terms are equivalent for purpose of this study). To select category neurons, we assessed whether the firing rate (FR) in a 200 – 1200 ms window following picture onset (encoding 1–3 & probe) was significantly correlated with the five possible picture categories (1×5 ANOVA, followed by a right-sided permutation-based t-test between the category with maximal average spike count and all other categories; if both tests were p < 0.05, we classified a neuron as a category neuron with the preferred category being the one with maximal average spike count; see Methods). As shown previously, category neurons remain persistently active during the maintenance period of the WM task when their preferred picture is held in WM34. Selecting for category neurons during picture presentation leaves their FRs during the maintenance period of the task independent for subsequen
[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/NWB_SBCAT_NO_analysis/helpers/3rdParty/stats && grep -v "^\s*%" ttest2_cell.m | grep -v "^\s*$" | sed -n 1,60p | grep -n "t =\|homogenous\|inhomogenous\|sd\|var" | head; grep -v "^\s*%" ttest_cell.m | grep -n "t =\|sd" | head; sed -n 90,140p surrogdistrib.m
```

```
1:function [tval, df] = ttest2_cell(a,b,c) % assumes equal variances
6:    homogenous = 'homogenous';
8:        homogenous = b;
11:        homogenous = c;
17:    if ~strcmpi(homogenous, 'inhomogenous') && ~strcmpi(homogenous, 'homogenous')
18:        error('Value for homogenous parameter can only be ''homogenous'' or ''inhomogenous''');
25:    if strcmpi(homogenous, 'inhomogenous')
27:        s1 = var(a,0,nd) ./ na;
28:        s2 = var(b,0,nd) ./ nb;
30:        sd = sqrt([s1.*na, s2.*nb]);
13:    sd   = mystd( tmpdiff,[], myndims(a));
14:    tval = diff./sd*sqrt(size(a, myndims(a)));
function res = supersurrogate(dat, lens, dims, bootstrapflag, pairedflag, naccu); % for increased speed only shuffle half the indices

    % recompute indices in set and target cell indices
    % ------------------------------------------------
    ncond = length(lens)-1;
    nsubj = lens(2);
    if bootstrapflag
        if pairedflag
[... 44 more lines not kept]
```

**Agent**

Survey done: the dataset (version 0.240904.2347, the one the paper cites) has 46 sessions and 950 units, matching the paper's isolated count. Now writing the helper module.

**Agent calls Bash**

```bash
mkdir -p entries/001187-daume-2024 && cat > entries/001187-daume-2024/sbcat.py <<'EOF'
"""Loading and measures for dandiset 001187 (Daume et al. 2024, Neuron 112, 3957-3968).

Sources of parameters, as cited in the claims file claims/001187/10.1016-j.neuron.2024.09.013.yaml
(shared methods S, U, L, C, M, B, O, G, P) or in the paper:

- Rate filter 0.1 Hz in both tasks, WM rate = spikes up to the last raw WM event over the time from
  the first to the last raw WM event, LTM rate = spikes from the first raw LTM event over the time
  from the first to the last (claims U; rateFilter_units.m of the paper's code).
- Area: amygdala_left/right are amygdala, the others hippocampus (claims U).
- Category selection: spike rate 0.2 to 1.2 s after every encoding picture and the probe, 1x5
  permutation ANOVA p < 0.05, then the preferred category against the rest by a two-sided
  permutation t-test at p < 0.1 (claims C; NWB_calcCatSelective_SB.m).
- Memory selection: counts 0.2 to 1.2 s after LTM picture onset, correct trials, old against new,
  two-sided permutation t-test p < 0.05 (claims M; NWB_calcMemSelective_SB.m).
- Permutation p-values follow EEGLAB statcond (unpaired: labels shuffled; paired: conditions
  swapped within a unit), with stat_surrogate_pvals.m: p = (#perm > obs + 0.5)/(N + 1), two-sided
  2*min(p, 1-p); the t statistic is the pooled-variance t (ttest2_cell.m) or the paired t
  (ttest_cell.m), the ANOVA statistic the one-way F (claims P; the paper's code). 10,000
  permutations (Methods, Statistics).
- Baseline -0.9 to -0.3 s before encoding picture 1, maintenance window 0 to 2.5 s after
  maintenance onset (claims B; NWB_computeGLM.m). Spikes are counted with strict inequalities as
  the code does.
- Mixed models: normal, identity link, maximum likelihood, random intercepts for patient and for
  neuron within patient (claims G). Fitted with statsmodels MixedLM (reml=False), which for a normal
  response with identity link is the same model fitglme fits with 'Laplace'. P-values from the
  t distribution on n - p degrees of freedom, as fitglme reports them (claims G).
- Cluster test: FieldTrip-style dependent-samples t, maxsum cluster statistic, sign-flip
  permutations, cluster-forming threshold two-sided 0.05 (FieldTrip default clusteralpha, a
  standard choice named in the claims file), significance 0.025 per one-sided cluster (Methods,
  Statistics).
- Random seeds are standard choices; each claim's section makes its own generator.
"""
import os
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from scipy import stats

DANDISET = "001187"
VERSION = "0.240904.2347"
API = "https://api.dandiarchive.org/api"
NPERM = 10000


def list_assets():
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200"
    out = []
    while url:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        d = r.json()
        out += d["results"]
        url = d["next"]
    return out


def s3_url(asset_id):
    r = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60)
    r.raise_for_status()
    return r.url.split("?")[0]


def _str(x):
    x = x[()]
    return x.decode() if isinstance(x, bytes) else str(x)


def load_session(asset):
    """Read what the analysis needs from one NWB file, streamed from S3. Waveforms and stimulus
    images are not read."""
    f = h5py.File(remfile.File(s3_url(asset["asset_id"])), "r")
    s = {"path": asset["path"]}
    s["subject_id"] = _str(f["general/subject/subject_id"])
    s["session_id"] = _str(f["general/session_id"])
    s["identifier"] = _str(f["identifier"])
    s["age"] = _str(f["general/subject/age"])
    s["sex"] = _str(f["general/subject/sex"])
    s["institution"] = _str(f["general/institution"])
    s["notes"] = _str(f["general/notes"])
    for task in ["WM", "LTM"]:
        g = f[f"intervals/{task}_trials"]
        s[task.lower()] = pd.DataFrame({k: g[k][:] for k in g.keys()
                                        if k != "id" and g[k].ndim == 1}).assign(id=g["id"][:])
        ts = f[f"acquisition/events_raw_{task}/timestamps"][:]
        s[f"raw_{task}"] = (ts[0], ts[-1])
        ev = f[f"acquisition/events_{task}"]
        s[f"events_{task}"] = pd.DataFrame({"t": ev["timestamps"][:], "code": ev["data"][:]})
        s[f"events_{task}_desc"] = _str(ev.attrs["description"]) if "description" in ev.attrs else ""
    loc = np.array([x.decode() for x in f["general/extracellular_ephys/electrodes/location"][:]])
    eid = f["general/extracellular_ephys/electrodes/id"][:]
    ue = f["units/electrodes"][:]
    st = f["units/spike_times"][:]
    idx = f["units/spike_times_index"][:]
    starts = np.r_[0, idx[:-1]]
    s["units"] = pd.DataFrame({
        "unit_id": f["units/id"][:],
        "cluster": f["units/clusterID_orig"][:],
        "location": [loc[np.where(eid == e)[0][0]] for e in ue],
        "electrode": ue,
    })
    s["spikes"] = [st[a:b] for a, b in zip(starts, idx)]
    s["units_spike_desc"] = _str(f["units/spike_times"].attrs.get("description", b""))
    f.close()
    return s


def load_all(threads=12):
    assets = sorted(list_assets(), key=lambda a: a["path"])
    with ThreadPoolExecutor(threads) as ex:
        return list(ex.map(load_session, assets))


def area_of(location):
    return "amygdala" if location in ("amygdala_left", "amygdala_right") else "hippocampus"


def count(spikes, t0, a, b):
    """Spike counts in (t0 + a, t0 + b), strict as in the paper's code; t0 an array."""
    t0 = np.asarray(t0, float)
    return (np.searchsorted(spikes, t0 + b, side="left")
            - np.searchsorted(spikes, t0 + a, side="right"))


def global_rates(spikes, raw_wm, raw_ltm):
    """Global WM and LTM rates as rateFilter_units.m computes them (claims U)."""
    wm = np.sum(spikes <= raw_wm[1]) / (raw_wm[1] - raw_wm[0])
    ltm = np.sum(spikes >= raw_ltm[0]) / (raw_ltm[1] - raw_ltm[0])
    return wm, ltm


# ---------------------------------------------------------------- permutation tests (statcond)

def _pval(null, obs, tail="both"):
    """stat_surrogate_pvals.m: p = 1 - (rank - 0.5) / (N + 1), two-sided 2*min(p, 1-p)."""
    null = np.asarray(null)
    p = (np.sum(null > obs, axis=0) + 0.5) / (null.shape[0] + 1)
    if tail == "both":
        p = 2 * np.minimum(p, 1 - p)
    return p


def t_paired(d):
    d = np.asarray(d, float)
    n = d.shape[-1]
    return d.mean(-1) / (d.std(-1, ddof=1) / np.sqrt(n))


def t_pooled(a, b):
    na, nb = a.shape[-1], b.shape[-1]
    va, vb = a.var(-1, ddof=1), b.var(-1, ddof=1)
    sp = np.sqrt(((na - 1) * va + (nb - 1) * vb) / (na + nb - 2))
    return (a.mean(-1) - b.mean(-1)) / (sp * np.sqrt(1 / na + 1 / nb))


def perm_ttest_paired(x, y, rng, nperm=NPERM):
    """Paired permutation t-test (statcond 'paired','on','perm'): returns t, p, df."""
    d = np.asarray(x, float) - np.asarray(y, float)
    t = t_paired(d)
    signs = rng.choice([-1.0, 1.0], size=(nperm, d.size))
    tn = t_paired(signs * d)
    return float(t), float(_pval(tn, t)), d.size - 1


def perm_ttest_1samp(x, mu, rng, nperm=NPERM):
    """One-sample permutation test against mu, as a paired test of x against mu."""
    return perm_ttest_paired(np.asarray(x, float), np.full(len(x), mu), rng, nperm)


def perm_ttest_unpaired(a, b, rng, nperm=NPERM):
    """Unpaired permutation t-test (statcond 'paired','off','perm'): returns t, p."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    t = t_pooled(a, b)
    x = np.r_[a, b]
    perm = np.argsort(rng.random((nperm, x.size)), axis=1)
    xp = x[perm]
    with np.errstate(invalid="ignore", divide="ignore"):
        tn = t_pooled(xp[:, :a.size], xp[:, a.size:])
    tn = np.nan_to_num(tn, nan=0.0)
    return float(t), float(_pval(tn, t))


def f_oneway_groups(x, onehot):
    """One-way F for each row of x (rows: permutations or units) with groups given by onehot
    (n x k), or a stack of onehots (P x n x k) for permuted labels."""
    n, k = onehot.shape[-2:]
    cnt = onehot.sum(-2)
    sums = x @ onehot if onehot.ndim == 2 else np.einsum("n,pnk->pk", x, onehot)
    mean_all = x.mean()
    ss_between = np.sum(sums ** 2 / cnt, -1) - n * mean_all ** 2
    ss_total = np.sum((x - mean_all) ** 2)
    ss_within = ss_total - ss_between
    with np.errstate(invalid="ignore", divide="ignore"):
        return (ss_between / (k - 1)) / (ss_within / (n - k))


# ------------------------------------------------------------------------- selections

def category_rates(sess):
    """Rates 0.2 to 1.2 s after encoding pictures 1 to 3 (where shown) and the probe of every
    WM trial, with the category as the leading digit of the picture ID (claims C)."""
    wm = sess["wm"]
    times, cats = [], []
    for ts, pid in [("timestamps_Encoding1", "PicIDs_Encoding1"),
                    ("timestamps_Encoding2", "PicIDs_Encoding2"),
                    ("timestamps_Encoding3", "PicIDs_Encoding3"),
                    ("timestamps_Probe", "PicIDs_Probe")]:
        ok = (wm[ts].values != 0) & (wm[pid].values != 0) & np.isfinite(wm[ts].values)
        times.append(wm[ts].values[ok])
        cats.append(wm[pid].values[ok] // 100)
    return np.concatenate(times), np.concatenate(cats)


def category_test(rate, cats, rng, nperm=NPERM):
    """Selection C for one unit: permutation ANOVA, then the max category against the rest.
    Returns (is_category_neuron, preferred category, p_anova, p_t)."""
    ucat = np.unique(cats)
    onehot = (cats[:, None] == ucat[None, :]).astype(float)
    F = f_oneway_groups(rate, onehot)
    means = np.array([rate[cats == c].mean() for c in ucat])
    pref = ucat[np.argmax(means)]
    if not np.isfinite(F):
        return False, pref, np.nan, np.nan
    perm = np.argsort(rng.random((nperm, rate.size)), axis=1)
    Fn = np.nan_to_num(f_oneway_groups(rate, onehot[perm]), nan=0.0)
    p_anova = float(_pval(Fn, F, tail="one"))
    if p_anova >= 0.05:
        return False, pref, p_anova, np.nan
    _, p_t = perm_ttest_unpaired(rate[cats == pref], rate[cats != pref], rng, nperm)
    return bool(p_t < 0.1), pref, p_anova, p_t


def memory_test(sess, spikes, rng, nperm=NPERM):
    """Selection M for one unit: returns (p, mean old - mean new)."""
    ltm = sess["ltm"]
    ok = ltm.response_accuracy.values == 1
    c = count(spikes, ltm.timestamps_PicOnset.values[ok], 0.2, 1.2)
    old = ltm.new_old.values[ok] == 1
    t, p = perm_ttest_unpaired(c[old], c[~old], rng, nperm)
    return p, c[old].mean() - c[~old].mean()


# ------------------------------------------------------------------------- statistics

def outliers_methods(values):
    """Rule O-M: per unit and condition value, a unit is removed when any of its values lies
    outside mean +- 3 SD of all units' values in the tested conditions. values: units x conds."""
    v = np.asarray(values, float)
    m, s = np.nanmean(v), np.nanstd(v, ddof=1)
    return np.any(np.abs(v - m) > 3 * s, axis=1)


def mixedlm(df, formula, dv="FR"):
    """Normal LMM with random intercepts for patient and neuron nested in patient, by maximum
    likelihood. Returns a table with beta, SE, t, df and p (t distribution on n - p df)."""
    import statsmodels.formula.api as smf
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        md = smf.mixedlm(f"{dv} ~ {formula}", df, groups="patient", re_formula="1",
                         vc_formula={"neuron": "0 + C(neuron)"})
        res = md.fit(reml=False, method=["lbfgs", "powell"])
    k = len(res.fe_params)
    dfree = len(df) - k
    b, se = res.fe_params, res.bse_fe
    t = b / se
    p = 2 * stats.t.sf(np.abs(t), dfree)
    out = pd.DataFrame({"beta": b, "SE": se, "t": t, "p": p})
    out.attrs.update(n=len(df), df=dfree, neurons=df.neuron.nunique(),
                     patients=df.patient.nunique(), converged=res.converged)
    return out


def cluster_test(a, b, rng, nperm=NPERM, clusteralpha=0.05):
    """Paired cluster-based permutation test across units (rows) over time (columns), FieldTrip
    style: dependent-samples t, two-sided cluster-forming threshold at clusteralpha, maxsum
    statistic, sign flips. Returns a list of clusters (sign, start index, end index, sum, p)."""
    d = np.asarray(a, float) - np.asarray(b, float)
    n = d.shape[0]
    crit = stats.t.ppf(1 - clusteralpha / 2, n - 1)

    def clusters(t):
        out = []
        for sign in (1, -1):
            above = sign * t > crit
            i = 0
            while i < len(t):
                if above[i]:
                    j = i
                    while j + 1 < len(t) and above[j + 1]:
                        j += 1
                    out.append((sign, i, j, float(np.sum(t[i:j + 1]))))
                    i = j + 1
                else:
                    i += 1
        return out

    def tstat(x):
        return x.mean(0) / (x.std(0, ddof=1) / np.sqrt(n))

    t_obs = tstat(d)
    obs = clusters(t_obs)
    maxpos, minneg = np.zeros(nperm), np.zeros(nperm)
    for k in range(nperm):
        s = rng.choice([-1.0, 1.0], size=(n, 1))
        cl = clusters(tstat(s * d))
        pos = [c[3] for c in cl if c[0] == 1]
        neg = [c[3] for c in cl if c[0] == -1]
        maxpos[k] = max(pos) if pos else 0.0
        minneg[k] = min(neg) if neg else 0.0
    res = []
    for sign, i, j, ssum in obs:
        if sign == 1:
            p = (np.sum(maxpos >= ssum) + 1) / (nperm + 1)
        else:
            p = (np.sum(minneg <= ssum) + 1) / (nperm + 1)
        res.append(dict(sign=sign, start=i, end=j, sum=ssum, p=p))
    return t_obs, res
EOF
cd $TMPDIR && source env/bin/activate && cat > dev_load.py <<'EOF'
import sys, time, pickle; sys.path.insert(0,'entries/001187-daume-2024')
import sbcat
t=time.time(); S=sbcat.load_all(); print(time.time()-t)
pickle.dump(S,open('S.pkl','wb'))
EOF
python dev_load.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/dev_load.py", line 3, in <module>
    t=time.time(); S=sbcat.load_all(); print(time.time()-t)
                     ~~~~~~~~~~~~~~^^
  File "entries/001187-daume-2024/sbcat.py", line 114, in load_all
    return list(ex.map(load_session, assets))
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/_base.py", line 625, in result_iterator
    yield _result_or_cancel(fs.pop())
          ~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/_base.py", line 318, in _result_or_cancel
    return fut.result(timeout)
           ~~~~~~~~~~^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/_base.py", line 460, in result
    return self.__get_result()
           ~~~~~~~~~~~~~~~~~^^
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/_base.py", line 402, in __get_result
    raise self._exception
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/thread.py", line 59, in run
    result = self.fn(*self.args, **self.kwargs)
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001187-daume-2024 && python - <<'EOF'
import re
s=open('sbcat.py').read()
s=s.replace('''    r = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60)
    r.raise_for_status()
    return r.url.split("?")[0]''','''    r = requests.get(f"{API}/assets/{asset_id}/download/", allow_redirects=False, timeout=60)
    r.raise_for_status()
    return r.headers["Location"].split("?")[0]''')
open('sbcat.py','w').write(s)
EOF
cd $TMPDIR && source env/bin/activate && python dev_load.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/dev_load.py", line 3, in <module>
    t=time.time(); S=sbcat.load_all(); print(time.time()-t)
                     ~~~~~~~~~~~~~~^^
  File "entries/001187-daume-2024/sbcat.py", line 114, in load_all
    return list(ex.map(load_session, assets))
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/_base.py", line 625, in result_iterator
    yield _result_or_cancel(fs.pop())
          ~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/_base.py", line 318, in _result_or_cancel
    return fut.result(timeout)
           ~~~~~~~~~~^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/_base.py", line 460, in result
    return self.__get_result()
           ~~~~~~~~~~~~~~~~~^^
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/_base.py", line 402, in __get_result
    raise self._exception
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/thread.py", line 59, in run
    result = self.fn(*self.args, **self.kwargs)
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001187-daume-2024 && python - <<'EOF'
s=open('sbcat.py').read()
s=s.replace('''def _str(x):
    x = x[()]''','''def _str(x):
    x = x[()] if isinstance(x, h5py.Dataset) else x''')
open('sbcat.py','w').write(s)
EOF
cd $TMPDIR && source env/bin/activate && python dev_load.py
```

```
61.343196630477905
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && cat > d1.py <<'EOF'
import sys, pickle, numpy as np, pandas as pd; sys.path.insert(0,'entries/001187-daume-2024')
import sbcat
S=pickle.load(open('S.pkl','rb'))
s=S[0]; print(s['events_WM_desc']); print(s['events_LTM_desc'])
print(s['wm'].head(3).T); print(s['ltm'].head(3).T)
# LTM coding
for s in S:
    l=s['ltm']; conf=l.confidence.values; old=l.new_old.values
    respold = conf>=4
    acc_pred=(respold==(old==1)).astype(int)
    mism=(acc_pred!=l.response_accuracy.values).sum()
    w=s['wm']
    print(s['identifier'], 'ltm n',len(l),'old',old.sum(),'conf vals',np.unique(conf).tolist(),'mism',mism,
      'nts',np.unique(l.num_times_shown).tolist(),'loads',np.unique(l.load).tolist(),
      'WM loads',np.bincount(w.loads)[1:].tolist(),'enc2zero',((w.timestamps_Encoding2==0)|w.timestamps_Encoding2.isna()).sum(), 'pid2zero',(w.PicIDs_Encoding2==0).sum(),
      'wmacc %.1f ltmacc %.1f'%(100*w.response_accuracy.mean(),100*l.response_accuracy.mean()))
EOF
python d1.py
```

```
The events correspond to the TTL markers for each trial of the Sternberg task. The TTL markers are the following: 61 = Start of the Sternberg Experiment, 11 = Fixation Cross, 1 = Picture #1 Shown, 2 = Picture #2 Shown, 3 = Picture #3 Shown, 5 = Transition between each picture presentation, 6 = End of Encoding Sequence / Start of Maintenance Period, 7 = Probe Stimulus, 8 = Subject Response, 60 = End of Sternberg Experiment. 
The events correspond to the TTL markers for each trial of the New-Old task. The TTL markers are the following: 2 = Fixation Cross (The first 2 signals the beginning of the New-Old Experiment, 1 = Picture shown,8 = Subject Response, 62 = End of the New-Old Experiment. 
                                   0           1           2
PicIDs_Encoding1          201.000000  202.000000  301.000000
PicIDs_Encoding2          101.000000  102.000000  401.000000
PicIDs_Encoding3          501.000000  502.000000  103.000000
PicIDs_Probe              501.000000  502.000000  301.000000
loads                       3.000000    3.000000    3.000000
probe_in_out                1.000000    1.000000    1.000000
response_accuracy           0.000000    1.000000    1.000000
response_time               2.144000    1.106000    1.647000
start_time                  0.017031   12.136589   23.200585
stop_time                  12.117714   23.182866   34.871674
timestamps_Encoding1        1.079031   13.330995   24.337428
timestamps_Encoding1_end    3.086280   15.337119   26.343740
timestamps_Encoding2        3.138249   15.453369   26.399396
timestamps_Encoding2_end    5.144373   17.459524   28.405676
timestamps_Encoding3        5.301779   17.493774   28.597989
timestamps_Encoding3_end    7.307935   19.499961   30.603738
timestamps_FixationCross    0.017031   12.136589   23.200585
[... 65 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && cat > d2.py <<'EOF'
import sys, pickle, numpy as np, pandas as pd; sys.path.insert(0,'entries/001187-daume-2024')
import sbcat
S=pickle.load(open('S.pkl','rb'))
rows=[]
for si,s in enumerate(S):
    for ui,u in s['units'].iterrows():
        sp=s['spikes'][ui]
        wm,ltm=sbcat.global_rates(sp,s['raw_WM'],s['raw_LTM'])
        rows.append(dict(si=si,ui=ui,ident=s['identifier'],area=sbcat.area_of(u.location),wm=wm,ltm=ltm,n=len(sp),sorted=bool(np.all(np.diff(sp)>=0)),
          first=sp[0] if len(sp) else np.nan,last=sp[-1] if len(sp) else np.nan, rawwm0=s['raw_WM'][0],rawwm1=s['raw_WM'][1],rawltm0=s['raw_LTM'][0],rawltm1=s['raw_LTM'][1]))
U=pd.DataFrame(rows)
U['keep']=(U.wm>=0.1)&(U.ltm>=0.1)
print(U.groupby('area').keep.agg(['size','sum']))
print('unsorted',(~U.sorted).sum())
print((U.rawltm0-U.rawwm1).describe())
# alt: rates within event range
pickle.dump(U,open('U.pkl','wb'))
EOF
python d2.py
```

```
size  sum
area                  
amygdala      570  532
hippocampus   380  351
unsorted 5
count     950.000000
mean      358.041907
std       512.768384
min       -28.971633
25%         0.000000
50%        10.080590
75%       668.772326
max      2012.924218
dtype: float64
Shell cwd was reset to
```

**Agent calls Bash**

```bash
grep -n "large\|literal\|LITERAL\|MAX_" tools/entry.py | head -20
```

```
22:- no notebook or helper embeds a large literal array or an encoded image, or
61:MAX_LITERAL_NUMBERS = 200                 # more numbers than this in one literal is "embedded data"
66:LONG_LITERAL = re.compile(r"[\[(]\s*(?:-?\d+\.?\d*(?:e-?\d+)?\s*,\s*){%d,}" % MAX_LITERAL_NUMBERS)
327:    if LONG_LITERAL.search(code):
328:        report.error(where, f"contains a literal of more than {MAX_LITERAL_NUMBERS} numbers; "
```

**Agent calls Bash**

```bash
cd entries/001187-daume-2024 && python - <<'EOF'
s=open('sbcat.py').read()
s=s.replace('''    s["spikes"] = [st[a:b] for a, b in zip(starts, idx)]''','''    raw = [st[a:b] for a, b in zip(starts, idx)]
    s["unsorted_units"] = [i for i, x in enumerate(raw) if np.any(np.diff(x) < 0)]
    s["spikes"] = [np.sort(x) for x in raw]''')
open('sbcat.py','w').write(s)
EOF
cd $TMPDIR && source env/bin/activate && cat > d3.py <<'EOF'
import sys, pickle, time, numpy as np, pandas as pd; sys.path.insert(0,'entries/001187-daume-2024')
import sbcat
S=pickle.load(open('S.pkl','rb')); U=pickle.load(open('U.pkl','rb'))
for s in S: s['spikes']=[np.sort(x) for x in s['spikes']]
rng=np.random.default_rng(1)
t=time.time()
res=[]
for si in range(3):
    s=S[si]; times,cats=sbcat.category_rates(s)
    print(s['identifier'], len(times), np.bincount(cats))
    for ui in range(len(s['spikes'])):
        r=sbcat.count(s['spikes'][ui],times,0.2,1.2)/1.0
        res.append(sbcat.category_test(r,cats,rng))
print(time.time()-t, len(res), sum(r[0] for r in res))
t=time.time()
for si in range(3):
    s=S[si]
    for ui in range(len(s['spikes'])): sbcat.memory_test(s,s['spikes'][ui],rng)
print('mem',time.time()-t)
EOF
python d3.py
```

```
sub-1_ses-2_P54CS 420 [ 0 87 85 84 81 83]
sub-10_ses-1_P68CS 420 [ 0 87 85 84 81 83]
sub-11_ses-1_P69CS 416 [ 0 86 84 84 81 81]
9.19308614730835 62 19
mem 1.90236234664917
Shell cwd was reset to
```

**Agent**

Rate filter reproduces 351/532 exactly. Writing the analysis code now.

**Agent calls Bash**

```bash
cat >> entries/001187-daume-2024/sbcat.py <<'EOF'


# ------------------------------------------------------------------------- tables

def picture_table(sess):
    """One row per encoding picture of every WM trial (slots 1 to 3 where shown), with its
    trial's load, WM accuracy and times, and, when the picture was shown in the LTM test, that
    trial's accuracy, confidence and picture onset."""
    wm, ltm = sess["wm"], sess["ltm"]
    lt = ltm.set_index("PicIDs")
    rows = []
    for i, tr in wm.iterrows():
        for slot in (1, 2, 3):
            pid = int(tr[f"PicIDs_Encoding{slot}"])
            if pid == 0:
                continue
            r = dict(trial=i, slot=slot, pic=pid, cat=pid // 100, load=int(tr.loads),
                     acc_WM=int(tr.response_accuracy), t_enc1=tr.timestamps_Encoding1,
                     t_maint=tr.timestamps_Maintenance, t_enc=tr[f"timestamps_Encoding{slot}"],
                     probe=int(tr.PicIDs_Probe))
            if pid in lt.index:
                m = lt.loc[pid]
                r.update(in_ltm=True, LTMacc=int(m.response_accuracy), conf=int(m.confidence),
                         t_ltm=float(m.timestamps_PicOnset))
            else:
                r.update(in_ltm=False, LTMacc=np.nan, conf=np.nan, t_ltm=np.nan)
            rows.append(r)
    return pd.DataFrame(rows)


def add_counts(pt, spikes):
    """Spike counts per picture row: maintenance 0 to 2.5 s, baseline -0.9 to -0.3 s before
    encoding picture 1, encoding picture 1 0 to 2 s (claims B; Methods, Relating WM maintenance
    activity to LTM formation), and LTM 0.2 to 1.2 s after the picture's LTM onset."""
    pt = pt.copy()
    pt["c_maint"] = count(spikes, pt.t_maint.values, 0.0, 2.5)
    pt["c_bsl"] = count(spikes, pt.t_enc1.values, -0.9, -0.3)
    pt["c_enc1"] = count(spikes, pt.t_enc1.values, 0.0, 2.0)
    ok = np.isfinite(pt.t_ltm.values)
    c = np.full(len(pt), np.nan)
    c[ok] = count(spikes, pt.t_ltm.values[ok], 0.2, 1.2)
    pt["c_ltm"] = c
    pt["r_maint"] = pt.c_maint / 2.5
    pt["r_bsl"] = pt.c_bsl / 0.6
    pt["r_enc1"] = pt.c_enc1 / 2.0
    return pt


def conf3_code(conf):
    """The Fig. 3a code's recoding (NWB_computeGLM.m): 4, 5, 6 to 1, 2, 3; 1, 2, 3 kept, so
    forgotten sure 1 ... guessing 3 and remembered guessing 1 ... sure 3 (claims, fig3a)."""
    conf = np.asarray(conf, float)
    return np.where(conf >= 4, conf - 3, conf)


def conf3_certainty(conf):
    """Certainty coding: sure 3 (1 or 6), unsure 2 (2 or 5), guessing 1 (3 or 4)."""
    conf = np.asarray(conf, float)
    return np.where(conf >= 4, conf - 3, 4 - conf)


def roc_auc(pos, neg, nthr=25):
    """ROC with nthr thresholds linearly spaced from the minimal to the maximal count of the
    two groups, AUC by the trapezoid rule (Methods, Single-neuron AUC analysis). pos is the
    group expected to fire more."""
    pos, neg = np.asarray(pos, float), np.asarray(neg, float)
    allv = np.r_[pos, neg]
    thr = np.linspace(allv.min(), allv.max(), nthr)
    tpr = np.array([np.mean(pos >= t) for t in thr] + [0.0])
    fpr = np.array([np.mean(neg >= t) for t in thr] + [0.0])
    order = np.argsort(fpr, kind="stable")
    return float(np.trapezoid(tpr[order], fpr[order]))
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/001187-daume-2024 && python - <<'EOF'
s=open('sbcat.py').read()
s=s.replace('''    tpr = np.array([np.mean(pos >= t) for t in thr] + [0.0])
    fpr = np.array([np.mean(neg >= t) for t in thr] + [0.0])
    order = np.argsort(fpr, kind="stable")
    return float(np.trapezoid(tpr[order], fpr[order]))''','''    tpr = np.r_[0.0, [np.mean(pos >= t) for t in thr[::-1]]]
    fpr = np.r_[0.0, [np.mean(neg >= t) for t in thr[::-1]]]
    return float(np.trapezoid(tpr, fpr))''')
open('sbcat.py','w').write(s)
EOF
date -u
```

```
Sun Nov  1 07:28:06 UTC 2026
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/nb && cat > $TMPDIR/nb/build.py <<'EOF'
"""Build an ipynb from a py file with '# %%' cell markers. '# %% md' starts a markdown cell;
'# %% tags=a,b' sets tags."""
import sys, nbformat
src = open(sys.argv[1]).read().split("\n")
cells, cur, kind, tags = [], [], None, []
def flush():
    if kind is None: return
    text = "\n".join(cur).strip("\n")
    if kind == "md":
        text = "\n".join(l[2:] if l.startswith("# ") else l[1:] if l.startswith("#") else l for l in text.split("\n"))
        c = nbformat.v4.new_markdown_cell(text)
    else:
        c = nbformat.v4.new_code_cell(text)
    if tags: c.metadata["tags"] = tags
    cells.append(c)
for line in src:
    if line.startswith("# %%"):
        flush(); cur = []; rest = line[4:].strip()
        kind = "md" if rest.startswith("md") else "code"
        tags = rest.split("tags=")[1].split(",") if "tags=" in rest else []
    else:
        cur.append(line)
flush()
nb = nbformat.v4.new_notebook(); nb.cells = cells
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nbformat.write(nb, sys.argv[2])
EOF
cat > $TMPDIR/nb/dev.py <<'EOF'
"""Run cells of notebook.py in one namespace, with the data from the dev pickle; cells
selected by index range or 'all'. Keeps state in a dill-free way: reruns from start."""
import sys, pickle, time
sys.path.insert(0, 'entries/001187-daume-2024')
src = open(sys.argv[1]).read().split("# %%")
stop = int(sys.argv[2]) if len(sys.argv) > 2 else 10**6
skip_md = True
ns = {}
for i, c in enumerate(src[1:]):
    if i >= stop: break
    if c.startswith(" md"): continue
    code = c.split("\n", 1)[1]
    code = code.replace("S = sbcat.load_all()", "S = pickle.load(open('/tmp/claude-1001/S.pkl','rb')); [s.update(spikes=[np.sort(x) for x in s['spikes']], unsorted_units=[]) for s in S]")
    t = time.time()
    exec("import pickle\n" + code, ns)
    print(f"--- cell {i} {time.time()-t:.1f}s", flush=True)
EOF
echo ok
```

```
ok
```

**Agent calls Write**

```json
{
 "file_path": "entries/001187-daume-2024/notebook.py",
 "content": "# %% md\n# # Reproducing Daume et al. (2024) from dandiset 001187\n#\n# HEADER\n\n# %%\nimport time\nimport numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nimport sbcat\n\nT0 = time.time()\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 30)\npd.set_option(\"display.max_rows\", 200)\nprint(\"dandiset\", sbcat.DANDISET, \"version\", sbcat.VERSION)\n\n# %% md\n# ## Data check\n#\n# Every NWB file of the pinned version is streamed; the trial tables, the raw event times, the\n# electrode locations and the spike times are read (not the waveforms or the stimulus images).\n\n# %%\nS = sbcat.load_all()\nprint(len(S), \"sessions loaded in\", round(time.time() - T0), \"s\")\n\n# %% tags=sanity\nrows = []\nfor si, s in enumerate(S):\n    ltm, wm = s[\"ltm\"], s[\"wm\"]\n    conf = ltm.confidence.values\n    resp_old = conf >= 4\n    rows.append(dict(\n        session=s[\"identifier\"], subject=s[\"subject_id\"], ses=s[\"session_id\"], age=s[\"age\"],\n        sex=s[\"sex\"], institution=s[\"institution\"], units=len(s[\"spikes\"]),\n        hipp=int(sum(sbcat.area_of(l) == \"hippocampus\" for l in s[\"units\"].location)),\n        amyg=int(sum(sbcat.area_of(l) == \"amygdala\" for l in s[\"units\"].location)),\n        wm_trials=len(wm), load1=int((wm.loads == 1).sum()), load3=int((wm.loads == 3).sum()),\n        ltm_trials=len(ltm), ltm_old=int((ltm.new_old == 1).sum()),\n        conf_values=\"\".join(str(v) for v in np.unique(conf)),\n        acc_mismatch=int(np.sum((resp_old == (ltm.new_old.values == 1)).astype(int)\n                                != ltm.response_accuracy.values)),\n        unsorted_units=len(s[\"unsorted_units\"]),\n        variant=s[\"notes\"].split(\"Experiment variant: \")[1][0]))\nSES = pd.DataFrame(rows)\nprint(SES.to_string())\nprint(\"\\nsessions\", len(SES), \"subjects\", SES.subject.nunique(), \"units\", SES.units.sum(),\n      \"hippocampus\", SES.hipp.sum(), \"amygdala\", SES.amyg.sum())\nprint(\"locations:\", sorted({l for s in S for l in s[\"units\"].location}))\nprint(\"institutions in the files:\", SES.institution.unique().tolist())\nprint(\"identifier suffixes:\", sorted({s.split(\"_\")[-1].rstrip(\"0123456789\").lstrip(\"P0123456789\") or s\n                                       for s in SES.session}))\nprint(\"sessions with fewer than 400 LTM trials:\",\n      SES.loc[SES.ltm_trials < 400, [\"session\", \"ltm_trials\", \"ltm_old\"]].values.tolist())\nprint(\"sessions with fewer than 140 WM trials:\",\n      SES.loc[SES.wm_trials < 140, [\"session\", \"wm_trials\"]].values.tolist())\nprint(\"confidence values outside 1 to 6:\",\n      [(s[\"identifier\"], int(v), int(np.sum(s[\"ltm\"].confidence == v)))\n       for s in S for v in np.unique(s[\"ltm\"].confidence) if v < 1 or v > 6])\nprint(\"trials whose accuracy disagrees with 'old' = confidence 4 to 6:\", SES.acc_mismatch.sum())\nprint(\"units with unsorted spike times:\", SES.unsorted_units.sum(),\n      [(s[\"identifier\"], s[\"unsorted_units\"]) for s in S if s[\"unsorted_units\"]])\nallwm = pd.concat([s[\"wm\"] for s in S])\nallltm = pd.concat([s[\"ltm\"] for s in S])\nprint(\"\\nWM response time (s): %.3f to %.3f, median %.3f\" % (allwm.response_time.min(),\n      allwm.response_time.max(), allwm.response_time.median()))\nprint(\"LTM response time (s): %.3f to %.3f, median %.3f\" % (allltm.response_time.min(),\n      allltm.response_time.max(), allltm.response_time.median()))\nprint(\"maintenance length (probe - maintenance onset, s): %.3f to %.3f\" % (\n      (allwm.timestamps_Probe - allwm.timestamps_Maintenance).min(),\n      (allwm.timestamps_Probe - allwm.timestamps_Maintenance).max()))\nenc = allwm.timestamps_Encoding1_end - allwm.timestamps_Encoding1\nprint(\"encoding picture 1 duration (s): %.3f to %.3f\" % (enc.min(), enc.max()))\nprint(\"maintenance onset - end of last picture (s): max abs %.4f\" % np.max(np.abs(\n      allwm.timestamps_Maintenance - np.where(allwm.loads == 1, allwm.timestamps_Encoding1_end,\n                                              allwm.timestamps_Encoding3_end))))\nprint(\"picture categories (leading digit):\", sorted(np.unique(allwm.PicIDs_Encoding1 // 100)))\nprint(\"LTM load values:\", sorted(allltm.load.unique()), \" num_times_shown:\",\n      sorted(allltm.num_times_shown.unique()))\nprint(\"load of new pictures:\", sorted(allltm.load[allltm.new_old == 0].unique()),\n      \" num_times_shown of new:\", sorted(allltm.num_times_shown[allltm.new_old == 0].unique()))\n\n# %% md\n# Event clock. The trial tables and the spikes are checked against each other below, by the\n# response of the units to picture onset (the category selection decodes the picture\n# category from spikes aligned to the WM table's picture onsets; shifting the onsets removes\n# it), see the cell after the category selection.\n\n# %% md\n# ## Units and the rate filter (claims U)\n\n# %%\nrows = []\nfor si, s in enumerate(S):\n    for ui, loc in enumerate(s[\"units\"].location):\n        wmr, ltmr = sbcat.global_rates(s[\"spikes\"][ui], s[\"raw_WM\"], s[\"raw_LTM\"])\n        rows.append(dict(si=si, ui=ui, session=s[\"identifier\"], patient=s[\"subject_id\"],\n                         location=loc, area=sbcat.area_of(loc), rate_wm=wmr, rate_ltm=ltmr))\nUN = pd.DataFrame(rows)\nUN[\"keep\"] = (UN.rate_wm >= 0.1) & (UN.rate_ltm >= 0.1)\nprint(\"global WM rate (Hz): %.3f to %.2f; LTM rate: %.3f to %.2f\" % (\n    UN.rate_wm.min(), UN.rate_wm.max(), UN.rate_ltm.min(), UN.rate_ltm.max()))\nprint(UN.groupby(\"area\").keep.agg([\"size\", \"sum\"]))\nK = UN[UN.keep].reset_index(drop=True)\nprint(\"kept\", len(K), \"removed\", int((~UN.keep).sum()))\n"
}
```

```
File created successfully at: entries/001187-daume-2024/notebook.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python nb/dev.py entries/001187-daume-2024/notebook.py 2>&1 | tail -40
```

```
33  sub-34_ses-1_P1802JHU      34   1  P62Y   M  Cedars-Sinai Medical Center     12    12     0        140     70     70         400      200      123456             0               0       1
34  sub-35_ses-1_P1809JHU      35   1  P45Y   M  Cedars-Sinai Medical Center      1     1     0        140     70     70         400      200        1346             0               0       2
35  sub-36_ses-1_P1811JHU      36   1  P27Y   F  Cedars-Sinai Medical Center     10    10     0        140     70     70         400      200      123456             0               0       1
36  sub-37_ses-1_P1814JHU      37   1  P48Y   M  Cedars-Sinai Medical Center      8     8     0        140     70     70         400      200      123456             0               0       1
37  sub-38_ses-1_P1903JHU      38   1  P30Y   M  Cedars-Sinai Medical Center      2     2     0        140     70     70         400      200      123456             0               0       1
38  sub-39_ses-1_P1912JHU      39   1  P49Y   M  Cedars-Sinai Medical Center     16    16     0        140     70     70         400      200      123456             0               0       1
39      sub-4_ses-1_P58CS       4   1  P32Y   F  Cedars-Sinai Medical Center     29     2    27        140     70     70         400      200      123456             0               0       1
40      sub-5_ses-1_P61CS       5   1  P52Y   F  Cedars-Sinai Medical Center     23    12    11        140     70     70         400      200      123456             0               0       1
41      sub-5_ses-2_P61CS       5   2  P52Y   F  Cedars-Sinai Medical Center      9     1     8        140     70     70         400      200      123456             0               0       2
42      sub-6_ses-1_P62CS       6   1  P25Y   F  Cedars-Sinai Medical Center     22     3    19        140     70     70         400      200      123456             0               0       1
43      sub-7_ses-1_P64CS       7   1  P63Y   F  Cedars-Sinai Medical Center    
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> entries/001187-daume-2024/sbcat.py <<'EOF'


# Table S1 of the paper (supplement, page 7 to 8), reference values for claim table-s1-counts:
# session label, WM and LTM accuracy (%), and per area category-selective / memory-selective /
# recorded counts. The two sessions marked * in the paper (P87cs, P1901jh) were excluded there
# and are not in the dandiset.
TABLE_S1 = """
P54cs_2 93.6 76.8 3/0/7 5/2/17
P55cs 97.1 72.8 0/0/1 7/3/21
P55cs_2 97.1 74.8 2/2/8 13/1/25
P57cs_2 91.4 67.5 1/0/4 14/5/24
P58cs 97.9 86.3 0/1/2 9/4/27
P61cs 87.1 68.8 6/2/12 6/2/11
P61cs_2 97.9 72.3 0/0/2 7/3/8
P62cs 97.1 80.8 0/2/3 5/0/19
P64cs 78.6 56.8 0/0/0 3/0/17
P65cs 94.3 72 5/0/9 7/3/18
P67cs 97.9 80.8 0/0/0 5/1/12
P68cs 92.1 58 3/3/16 1/0/17
P69cs 75 64.8 3/2/8 4/0/7
P70cs 98.6 68.3 0/0/1 5/7/14
P70cs_2 96.4 73.9 0/0/1 0/0/5
P71cs 96.4 69 0/0/0 0/0/3
P73cs 92.1 60.5 0/1/5 7/1/17
P74cs 97.9 73 0/0/0 6/0/9
P76cs 99.3 78.5 4/0/6 12/1/25
P76cs_2 100 90 0/0/0 0/0/4
P77cs 94.3 73 2/2/4 12/12/41
P78cs 97.1 59.8 0/1/13 0/1/14
P79cs 97.9 68.8 6/2/17 14/4/28
P79cs_2 97.1 80.5 4/0/13 9/3/19
P80cs 100 82.3 4/7/13 20/9/49
P82cs 98.6 69.5 11/2/17 12/1/24
P88T 99.3 76.3 3/1/22 0/0/6
P89T 97.1 57 7/3/22 11/0/18
P90T_2 91.4 57.8 0/0/11 0/0/2
P90T_3 90.7 55.8 0/1/13 0/0/0
P93T 83.6 62.7 0/0/4 0/0/3
P96T 90 65 4/0/6 0/0/5
P101T 100 87 6/3/16 5/0/5
P101T_2 100 90 5/3/8 5/3/6
P103T 96.4 61.5 4/2/20 3/0/11
P106T 84.3 58.3 1/0/7 6/1/14
P109T 100 85.8 1/2/15 0/0/7
P110T 99.3 64.3 0/0/6 1/0/10
P113T_2 97.1 60.8 2/2/11 1/1/7
P116T 97.9 65 4/1/9 5/0/18
P1802jh 90.7 70.3 5/1/12 0/0/0
P1809jh 75.7 57 0/1/6 0/0/0
P1811jh 76.4 61 1/0/10 0/0/0
P1814jh 90.7 76.8 1/3/8 0/0/0
P1903jh 99.3 82 0/0/2 0/0/0
P1912jh 70.7 60.5 6/3/16 0/0/0
"""


def table_s1():
    rows = []
    for line in TABLE_S1.strip().split("\n"):
        lab, wm, ltm, h, a = line.split()
        h, a = [list(map(int, x.split("/"))) for x in (h, a)]
        rows.append(dict(label=lab, wm_acc=float(wm), ltm_acc=float(ltm), h_cat=h[0], h_ms=h[1],
                         h_rec=h[2], a_cat=a[0], a_ms=a[1], a_rec=a[2]))
    return pd.DataFrame(rows)


def s1_label(identifier):
    """Table S1 label of a session from the file's identifier: sub-1_ses-2_P54CS -> P54cs_2,
    sub-22_ses-1_P088TWH -> P88T, sub-34_ses-1_P1802JHU -> P1802jh. The session suffix is the
    session number when it is not 1."""
    _, ses, pat = identifier.split("_")
    num = int("".join(ch for ch in pat[1:] if ch.isdigit()))
    site = {"CS": "cs", "TWH": "T", "JHU": "jh"}[pat.lstrip("P0123456789")]
    s = int(ses.split("-")[1])
    return f"P{num}{site}" + ("" if s == 1 else f"_{s}")
EOF
echo
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cat >> entries/001187-daume-2024/notebook.py <<'EOF'

# %% md
# Duplicate recordings. Two sessions could hold the same recording deposited twice. For every
# pair of sessions, the trial tables and the spike trains are compared.

# %%
dups = []
sig = [(s["identifier"], s["wm"].timestamps_Encoding1.values, s["wm"].PicIDs_Encoding1.values,
        [len(x) for x in s["spikes"]]) for s in S]
for i in range(len(S)):
    for j in range(i + 1, len(S)):
        same_pics = np.array_equal(sig[i][2], sig[j][2])
        same_times = len(sig[i][1]) == len(sig[j][1]) and np.allclose(sig[i][1] - sig[i][1][0],
                                                                      sig[j][1] - sig[j][1][0])
        common_counts = len(set(sig[i][3]) & set(sig[j][3]) - {0})
        if same_times or common_counts > 2:
            dups.append((sig[i][0], sig[j][0], same_pics, same_times, common_counts))
print("session pairs with identical WM timing or more than 2 units of identical spike counts:", dups)
same_order = pd.Series([tuple(s["wm"].PicIDs_Encoding1) for s in S]).duplicated(keep=False)
print("sessions sharing the same picture sequence (expected for one task variant):",
      int(same_order.sum()))
EOF
cat >> entries/001187-daume-2024/notebook.py <<'EOF'

# %% md
# ## Claim sessions-and-neurons
#
# > After excluding two sessions, 46 sessions are analysed, in which 883 single units pass the
# > 0.1 Hz rate filter, 351 in the hippocampus and 532 in the amygdala, of 950 isolated.

# %% tags=claim:sessions-and-neurons
S1 = sbcat.table_s1()
print("sessions in the dandiset:", len(S), "(Table S1 lists", len(S1), "kept sessions)")
print("isolated units:", len(UN), " Table S1 recorded total:", S1.h_rec.sum() + S1.a_rec.sum())
print("after the rate filter: hippocampus", int(K.area.eq("hippocampus").sum()),
      " amygdala", int(K.area.eq("amygdala").sum()))
print("removed by the filter:", int((~UN.keep).sum()), "(%.1f%%)" % (100 * (~UN.keep).mean()))
print("Table S1 sums: hippocampus", S1.h_rec.sum(), " amygdala", S1.a_rec.sum())

# %% md
# **Result: ...**

# %% md
# ## Claim table-s1-counts
#
# > Per session, the numbers of recorded units in the hippocampus and the amygdala are those of
# > Table S1.
#
# Sessions are matched by the label in the file identifier (P54CS with session 2 is P54cs_2).

# %% tags=claim:table-s1-counts
SES["label"] = [sbcat.s1_label(x) for x in SES.session]
kept_counts = K.groupby(["session", "area"]).size().unstack(fill_value=0)
SES["hipp_kept"] = SES.session.map(kept_counts.get("hippocampus", {})).fillna(0).astype(int)
SES["amyg_kept"] = SES.session.map(kept_counts.get("amygdala", {})).fillna(0).astype(int)
SES["wm_acc"] = [100 * s["wm"].response_accuracy.mean() for s in S]
SES["ltm_acc"] = [100 * s["ltm"].response_accuracy.mean() for s in S]
TS1 = SES.merge(S1, on="label", how="outer", indicator=True)
print("matched:", (TS1._merge == "both").sum(), " only in dandiset:",
      TS1.label[TS1._merge == "left_only"].tolist(), " only in Table S1:",
      TS1.label[TS1._merge == "right_only"].tolist())
TS1 = TS1[TS1._merge == "both"].copy()
TS1["match_before"] = (TS1.hipp == TS1.h_rec) & (TS1.amyg == TS1.a_rec)
TS1["match_after"] = (TS1.hipp_kept == TS1.h_rec) & (TS1.amyg_kept == TS1.a_rec)
TS1["match_either"] = TS1.match_before | TS1.match_after
print("sessions matching before the filter:", int(TS1.match_before.sum()), "after:",
      int(TS1.match_after.sum()), "under either:", int(TS1.match_either.sum()), "of", len(TS1))
print(TS1.loc[~TS1.match_either, ["label", "session", "hipp", "hipp_kept", "h_rec", "amyg",
                                  "amyg_kept", "a_rec"]].to_string())
print("\nbehaviour against Table S1: max |WM acc diff| %.2f, max |LTM acc diff| %.2f points" % (
    np.max(np.abs(TS1.wm_acc - TS1.wm_acc_y)) if "wm_acc_y" in TS1 else np.nan,
    np.max(np.abs(TS1.ltm_acc_x - TS1.ltm_acc_y)) if "ltm_acc_x" in TS1 else np.nan))
EOF
cd $TMPDIR && source env/bin/activate && python nb/dev.py entries/001187-daume-2024/notebook.py 2>&1 | tail -30
```

```
area                  
amygdala      570  532
hippocampus   380  351
kept 883 removed 67
--- cell 7 0.0s
session pairs with identical WM timing or more than 2 units of identical spike counts: []
sessions sharing the same picture sequence (expected for one task variant): 45
--- cell 9 0.0s
sessions in the dandiset: 46 (Table S1 lists 46 kept sessions)
isolated units: 950  Table S1 recorded total: 973
after the rate filter: hippocampus 351  amygdala 532
removed by the filter: 67 (7.1%)
Table S1 sums: hippocampus 386  amygdala 587
--- cell 11 0.0s
matched: 46  only in dandiset: []  only in Table S1: []
sessions matching before the filter: 42 after: 21 under either: 42 of 46
      label                session  hipp  hipp_kept  h_rec  amyg  amyg_kept  a_rec
9   P1809jh  sub-35_ses-1_P1809JHU     1          1      6     0          0      0
20  P61cs_2      sub-5_ses-2_P61CS     1          1      2     8          8      8
25    P68cs     sub-10_ses-1_P68CS    16         14     16     7          7     17
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001187-daume-2024 && python - <<'EOF'
s=open('notebook.py').read()
s=s.replace('''print("\\nbehaviour against Table S1: max |WM acc diff| %.2f, max |LTM acc diff| %.2f points" % (
    np.max(np.abs(TS1.wm_acc - TS1.wm_acc_y)) if "wm_acc_y" in TS1 else np.nan,
    np.max(np.abs(TS1.ltm_acc_x - TS1.ltm_acc_y)) if "ltm_acc_x" in TS1 else np.nan))''','''dwm, dltm = TS1.wm_acc_x - TS1.wm_acc_y, TS1.ltm_acc_x - TS1.ltm_acc_y
print("\\naccuracy against Table S1 (a check of the session match): max |WM diff| %.2f, "
      "max |LTM diff| %.2f points" % (dwm.abs().max(), dltm.abs().max()))
print(TS1.loc[(dwm.abs() > 0.15) | (dltm.abs() > 0.15),
              ["label", "wm_acc_x", "wm_acc_y", "ltm_acc_x", "ltm_acc_y", "ltm_trials"]].round(2).to_string())''')
open('notebook.py','w').write(s)
EOF
cd $TMPDIR && source env/bin/activate && python nb/dev.py entries/001187-daume-2024/notebook.py 2>&1 | tail -12
```

```
20  P61cs_2      sub-5_ses-2_P61CS     1          1      2     8          8      8
25    P68cs     sub-10_ses-1_P68CS    16         14     16     7          7     17
39    P82cs     sub-21_ses-1_P82CS    17         16     17    17         15     24

accuracy against Table S1 (a check of the session match): max |WM diff| 0.18, max |LTM diff| 1.52 points
    label  wm_acc_x  wm_acc_y  ltm_acc_x  ltm_acc_y  ltm_trials
2   P103T     96.43      96.4      61.65       61.5         399
26  P69cs     74.82      75.0      64.75       64.8         400
32  P76cs     99.29      99.3      78.99       78.5         395
40   P88T     99.29      99.3      77.82       76.3         257
41   P89T     97.14      97.1      56.15       57.0         187
--- cell 14 0.0s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/NWB_SBCAT_NO_analysis/helpers/internal/plotting && grep -v "^\s*%" plot_behavior.m | grep -v "^\s*$" | grep -v "plot\|set(\|ylabel\|xlabel\|title\|figure\|hold\|scatter\|errorbar\|xlim\|ylim\|line(" | head -60
```

```
nsubjects = length(nwbAll);
LTM_values = 1;
WM_values = 2;
clear RT_load1 RT_load3 acc_load1 acc_load3 acc_all
for isubj = 1:nsubjects
    clear RT acc
    RT = double(nwbAll{isubj}.intervals.values{WM_values}.vectordata.get('response_time').data.load());
    acc = double(nwbAll{isubj}.intervals.values{WM_values}.vectordata.get('response_accuracy').data.load());
    WM_load = double(nwbAll{isubj}.intervals.values{WM_values}.vectordata.get('loads').data.load());
    RT(RT>5) = nan;
    RT_load1(isubj) = nanmean(RT(WM_load == 1));
    acc_load1(isubj) = nanmean(acc(WM_load == 1));
    RT_load3(isubj) = nanmean(RT(WM_load == 3));
    acc_load3(isubj) = nanmean(acc(WM_load == 3));
    acc_all(isubj) = nanmean(acc);
end
color = {[0.8 0.2 0.7],[0.1 0.25 0.6]};
D = {acc_load1 acc_load3};
makeScatterPlot(D,0,color);
color = {[0.8 0.2 0.7],[0.1 0.25 0.6]};
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> entries/001187-daume-2024/notebook.py <<'EOF'

# %% md
# **Result: ...**

# %% md
# ## Behaviour
#
# Per session measures (claims S, L). High confidence is a rating of 1 or 6 (sure), low
# confidence 2 to 5. Sessions "with confidence ratings" leave out the one session whose ratings
# are only 1 and 6 (printed below), the patient the paper says "did not use confidence ratings"
# (Results, paragraph 2); the paper's code drops it the same way, as its low-confidence accuracy is
# undefined (plot_behavior.m).

# %%
from scipy.stats import norm
rows = []
for s in S:
    wm, ltm = s["wm"], s["ltm"]
    conf = ltm.confidence.values
    old = ltm.new_old.values == 1
    said_old = conf >= 4
    acc = ltm.response_accuracy.values.astype(float)
    hi = (conf == 1) | (conf == 6)
    unsure = (conf == 2) | (conf == 5)
    guess = (conf == 3) | (conf == 4)
    lo = ~hi
    rt = ltm.response_time.values
    rt5 = np.where(rt > 5, np.nan, rt)
    wrt = wm.response_time.values
    wrt5 = np.where(wrt > 5, np.nan, wrt)
    hit, fa = said_old[old].mean(), said_old[~old].mean()
    nh, nf = old.sum(), (~old).sum()
    hit_c = min(max(hit, 1 / (2 * nh)), 1 - 1 / (2 * nh))
    fa_c = min(max(fa, 1 / (2 * nf)), 1 - 1 / (2 * nf))
    L = ltm.load.values
    nts = ltm.num_times_shown.values
    rows.append(dict(
        session=s["identifier"], wm_acc=wm.response_accuracy.mean(), ltm_acc=acc.mean(),
        hit=hit, fa=fa, dprime=norm.ppf(hit_c) - norm.ppf(fa_c), rate_corrected=(hit != hit_c) or (fa != fa_c),
        wm_acc_l1=wm.response_accuracy[wm.loads == 1].mean(), wm_acc_l3=wm.response_accuracy[wm.loads == 3].mean(),
        wm_rt_l1=np.nanmean(wrt5[wm.loads == 1]), wm_rt_l3=np.nanmean(wrt5[wm.loads == 3]),
        wm_rt_l1_all=np.mean(wrt[wm.loads == 1]), wm_rt_l3_all=np.mean(wrt[wm.loads == 3]),
        n_hi=hi.sum(), n_unsure=unsure.sum(), n_guess=guess.sum(),
        acc_hi=acc[hi].mean() if hi.any() else np.nan,
        acc_lo_pooled=acc[lo].mean() if lo.any() else np.nan,
        acc_lo_avg=np.nanmean([acc[unsure].mean() if unsure.any() else np.nan,
                               acc[guess].mean() if guess.any() else np.nan]) if lo.any() else np.nan,
        rt_hi_all=rt[hi].mean(), rt_lo_pooled_all=rt[lo].mean() if lo.any() else np.nan,
        rt_lo_avg_all=np.nanmean([rt[unsure].mean() if unsure.any() else np.nan,
                                  rt[guess].mean() if guess.any() else np.nan]) if lo.any() else np.nan,
        rt_hi_5=np.nanmean(rt5[hi]), rt_lo_pooled_5=np.nanmean(rt5[lo]) if lo.any() else np.nan,
        rt_lo_avg_5=np.nanmean([np.nanmean(rt5[unsure]) if unsure.any() else np.nan,
                                np.nanmean(rt5[guess]) if guess.any() else np.nan]) if lo.any() else np.nan,
        hit_l1=said_old[old & (L == 1)].mean(), hit_l3=said_old[old & (L == 3)].mean(),
        hit_twice=said_old[old & (nts == 2)].mean(), hit_once=said_old[old & (nts == 1)].mean()))
BEH = pd.DataFrame(rows)
noconf = BEH.session[BEH.n_hi == [len(s["ltm"]) for s in S]].tolist()
print("sessions whose ratings are all high confidence:", noconf)
BEHC = BEH[~BEH.session.isin(noconf)]
print("sessions with confidence ratings:", len(BEHC))
print("sessions without guessing ratings:", BEHC.session[BEHC.n_guess == 0].tolist())
print(BEH.describe().T[["count", "mean", "std", "min", "max"]].round(3).to_string())

# %% md
# ## Claim behaviour-overall-accuracy
#
# > Patients answered 93.3% of WM trials and 70.3% of LTM trials correctly (d' 1.19), both above
# > the 50% chance level.

# %% tags=claim:behaviour-overall-accuracy
rng = np.random.default_rng(101)
for col, exp, tol in [("wm_acc", 93.3, 1.1), ("ltm_acc", 70.3, 1.4)]:
    v = 100 * BEH[col]
    t, p, df = sbcat.perm_ttest_1samp(v, 50, rng)
    print(f"{col}: mean {v.mean():.2f} % (SD {v.std(ddof=1):.2f}), expected {exp} +- {tol}, "
          f"within: {abs(v.mean() - exp) <= tol}; against 50%: t({df}) = {t:.2f}, perm p = {p:.5f}")
print(f"d': mean {BEH.dprime.mean():.3f} (SD {BEH.dprime.std(ddof=1):.3f}), expected 1.19 +- 0.09, "
      f"within: {abs(BEH.dprime.mean() - 1.19) <= 0.09}; sessions with a hit or FA rate of 0 or 1 "
      f"(1/(2N) applied): {int(BEH.rate_corrected.sum())}")
print("smallest p a 10,000-permutation test can give: %.5f" % (1 / 10001))

# %% md
# **Result: ...**

# %% md
# ## Claim fig1c-wm-accuracy-load
#
# > WM accuracy is higher in load 1 than in load 3 trials.

# %% tags=claim:fig1c-wm-accuracy-load
rng = np.random.default_rng(102)
t, p, df = sbcat.perm_ttest_paired(BEH.wm_acc_l1, BEH.wm_acc_l3, rng)
print(f"load 1 {100*BEH.wm_acc_l1.mean():.2f} %, load 3 {100*BEH.wm_acc_l3.mean():.2f} %; "
      f"t({df}) = {t:.2f} (paper 4.89), perm p = {p:.5f}; sessions with load 1 higher: "
      f"{int((BEH.wm_acc_l1 > BEH.wm_acc_l3).sum())}, equal {int((BEH.wm_acc_l1 == BEH.wm_acc_l3).sum())}")

# %% md
# **Result: ...**

# %% md
# ## Claim fig1d-wm-rt-load
#
# > WM responses are faster in load 1 than in load 3 trials.

# %% tags=claim:fig1d-wm-rt-load
rng = np.random.default_rng(103)
for lab, a, b in [("RT > 5 s missing (main)", "wm_rt_l1", "wm_rt_l3"),
                  ("all RTs (variant)", "wm_rt_l1_all", "wm_rt_l3_all")]:
    t, p, df = sbcat.perm_ttest_paired(BEH[a], BEH[b], rng)
    print(f"{lab}: load 1 {BEH[a].mean():.3f} s, load 3 {BEH[b].mean():.3f} s; t({df}) = {t:.2f} "
          f"(paper -4.29), perm p = {p:.5f}")
print("WM trials with RT > 5 s:", int(sum((s["wm"].response_time > 5).sum() for s in S)))

# %% md
# **Result: ...**

# %% md
# ## Claim fig1e-ltm-confidence-accuracy
#
# > LTM recognition is more accurate in high-confidence than in low-confidence trials.

# %% tags=claim:fig1e-ltm-confidence-accuracy
rng = np.random.default_rng(104)
for lab, col in [("(a) unsure and guessing pooled", "acc_lo_pooled"),
                 ("(b) mean of unsure and guessing accuracy", "acc_lo_avg")]:
    t, p, df = sbcat.perm_ttest_paired(BEHC.acc_hi, BEHC[col], rng)
    print(f"{lab}: high {100*BEHC.acc_hi.mean():.2f} %, low {100*BEHC[col].mean():.2f} %; "
          f"t({df}) = {t:.2f} (paper 8.66), perm p = {p:.5f}")

# %% md
# **Result: ...**

# %% md
# ## Claim ltm-rt-confidence
#
# > LTM responses are faster with high confidence (mean 1.83 s) than with low confidence (2.62 s).

# %% tags=claim:ltm-rt-confidence
rng = np.random.default_rng(105)
for rtr, suf in [("(a) all RTs", "all"), ("(b) RT > 5 s missing", "5")]:
    for lr, low in [("pooled", "pooled"), ("averaged", "avg")]:
        h, l = BEHC[f"rt_hi_{suf}"], BEHC[f"rt_lo_{low}_{suf}"]
        t, p, df = sbcat.perm_ttest_paired(h, l, rng)
        print(f"{rtr}, low {lr}: high {h.mean():.3f} s (SD {h.std(ddof=1):.2f}; 1.83 +- 0.085: "
              f"{abs(h.mean()-1.83) <= 0.085}), low {l.mean():.3f} s (SD {l.std(ddof=1):.2f}; 2.62 +- 0.098: "
              f"{abs(l.mean()-2.62) <= 0.098}); t({df}) = {t:.2f} (paper -11.13), perm p = {p:.5f}")

# %% md
# **Result: ...**

# %% md
# ## Claim fig1f-ltm-load
#
# > Pictures held in load 1 WM trials are later recognized better than pictures held in load 3
# > trials.

# %% tags=claim:fig1f-ltm-load
rng = np.random.default_rng(106)
t, p, df = sbcat.perm_ttest_paired(BEH.hit_l1, BEH.hit_l3, rng)
print(f"hit rate load 1 {100*BEH.hit_l1.mean():.2f} %, load 3 {100*BEH.hit_l3.mean():.2f} %; "
      f"t({df}) = {t:.2f} (paper 2.42), perm p = {p:.4f} (paper 0.018)")

# %% md
# **Result: ...**

# %% md
# ## Claim fig1g-ltm-probe
#
# > Pictures that were also used as WM probes, and so shown twice, are later recognized better
# > than pictures shown once.

# %% tags=claim:fig1g-ltm-probe
rng = np.random.default_rng(107)
t, p, df = sbcat.perm_ttest_paired(BEH.hit_twice, BEH.hit_once, rng)
print(f"hit rate shown twice {100*BEH.hit_twice.mean():.2f} %, once {100*BEH.hit_once.mean():.2f} %; "
      f"t({df}) = {t:.2f} (paper 7.25), perm p = {p:.5f}")

# %% md
# **Result: ...**
EOF
cd $TMPDIR && source env/bin/activate && python nb/dev.py entries/001187-daume-2024/notebook.py 2>&1 | sed -n '/cell 14/,$p'
```

```
--- cell 14 0.0s
<string>:39: RuntimeWarning: Mean of empty slice
sessions whose ratings are all high confidence: ['sub-11_ses-1_P69CS']
sessions with confidence ratings: 45
sessions without guessing ratings: ['sub-14_ses-1_P73CS', 'sub-19_ses-1_P79CS', 'sub-27_ses-1_P101TWH', 'sub-27_ses-2_P101TWH', 'sub-28_ses-1_P103TWH']
                  count     mean      std    min      max
wm_acc             46.0    0.933    0.076  0.707    1.000
ltm_acc            46.0    0.703    0.099  0.558    0.900
hit                46.0    0.664    0.192  0.180    0.935
fa                 46.0    0.259    0.132  0.025    0.595
dprime             46.0    1.189    0.620  0.353    2.617
wm_acc_l1          46.0    0.951    0.074  0.729    1.000
wm_acc_l3          46.0    0.916    0.085  0.671    1.000
wm_rt_l1           46.0    1.393    0.511  0.616    2.745
wm_rt_l3           46.0    1.525    0.449  0.697    2.882
wm_rt_l1_all       46.0    1.706    1.053  0.616    6.416
wm_rt_l3_all       46.0    1.689    0.658  0.697    3.625
n_hi               46.0  234.587  107.569  6.000  400.000
n_unsure           46.0   74.283   52.555  0.000  229.000
n_guess            46.0   73.739   85.247  0.000  335.000
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd entries/001187-daume-2024 && sed -i 's/perm p = {p:.5f}/perm p = {p:.6f}/g' notebook.py && grep -c "p:.6f" notebook.py
```

```
Sun Nov  1 07:30:07 UTC 2026
6
```

**Agent calls Bash**

```bash
cat >> notebook.py <<'EOF'

# %% md
# ## Category and memory-selective neurons (selections C and M)
#
# Each kept unit is tested as the paper's code does (NWB_calcCatSelective_SB.m,
# NWB_calcMemSelective_SB.m), with 10,000 permutations. Seeds are standard choices.

# %%
rng = np.random.default_rng(201)
t0 = time.time()
cat_res, mem_res = [], []
for si, s in enumerate(S):
    times, cats = sbcat.category_rates(s)
    for _, u in K[K.si == si].iterrows():
        sp = s["spikes"][u.ui]
        rate = sbcat.count(sp, times, 0.2, 1.2) / 1.0
        cat_res.append(sbcat.category_test(rate, cats, rng))
rng = np.random.default_rng(202)
for si, s in enumerate(S):
    for _, u in K[K.si == si].iterrows():
        mem_res.append(sbcat.memory_test(s, s["spikes"][u.ui], rng))
K["cat"] = [r[0] for r in cat_res]
K["pref"] = [int(r[1]) for r in cat_res]
K["p_anova"] = [r[2] for r in cat_res]
K["p_cat_t"] = [r[3] for r in cat_res]
K["p_ms"] = [r[0] for r in mem_res]
K["ms"] = K.p_ms < 0.05
K["ms_type"] = np.where(~K.ms, "", np.where([r[1] > 0 for r in mem_res], "FS", "NS"))
print("selection time %.0f s" % (time.time() - t0))
print(K.groupby("area")[["cat", "ms"]].sum())
print("units whose ANOVA was undefined (no spikes in any window):", int(K.p_anova.isna().sum()))

# %% md
# Clock check. If the trial tables share the spikes' clock, the category of the picture on the
# screen is decodable from spikes aligned to the table's onsets and not from spikes aligned to
# onsets shifted away from the picture. The same holds for old against new in the LTM task. Per
# session, the fraction of units with a parametric one-way ANOVA (WM categories) or t-test (LTM
# old against new, correct trials) at p < 0.05, for the onsets as given and shifted by -5 s
# (into the preceding trial; a contrast between labels, not an offset).

# %%
from scipy import stats as st
rows = []
for si, s in enumerate(S):
    times, cats = sbcat.category_rates(s)
    ltm = s["ltm"]
    ok = ltm.response_accuracy.values == 1
    tl, old = ltm.timestamps_PicOnset.values[ok], ltm.new_old.values[ok] == 1
    for shift in (0.0, -5.0):
        nw = nl = 0
        for _, u in K[K.si == si].iterrows():
            sp = s["spikes"][u.ui]
            r = sbcat.count(sp, times + shift, 0.2, 1.2)
            if r.std() > 0 and st.f_oneway(*[r[cats == c] for c in np.unique(cats)]).pvalue < 0.05:
                nw += 1
            c = sbcat.count(sp, tl + shift, 0.2, 1.2)
            if c.std() > 0 and st.ttest_ind(c[old], c[~old]).pvalue < 0.05:
                nl += 1
        rows.append(dict(session=s["identifier"], shift=shift, units=int((K.si == si).sum()),
                         wm_sig=nw, ltm_sig=nl))
CLK = pd.DataFrame(rows).pivot(index="session", columns="shift", values=["units", "wm_sig", "ltm_sig"])
print(CLK.to_string())
tot = pd.DataFrame(rows).groupby("shift")[["units", "wm_sig", "ltm_sig"]].sum()
print(tot)
print("sessions where the true WM onsets give no more significant units than the shifted ones:",
      CLK.index[CLK[("wm_sig", 0.0)] <= CLK[("wm_sig", -5.0)]].tolist())
print("sessions where the true LTM onsets give no more significant units than the shifted ones:",
      CLK.index[CLK[("ltm_sig", 0.0)] <= CLK[("ltm_sig", -5.0)]].tolist())

# %% md
# ## Claim category-neuron-counts
#
# > 104 hippocampal units (29.65%) and 220 amygdala units (41.35%) are category neurons.

# %% tags=claim:category-neuron-counts
for area, exp in [("hippocampus", 104), ("amygdala", 220)]:
    k = K[K.area == area]
    n = int(k.cat.sum())
    print(f"{area}: {n} of {len(k)} ({100*n/len(k):.2f} %), expected {exp} +- {0.1*exp:.1f}: "
          f"{abs(n-exp) <= 0.1*exp}")
    print("   preferred categories:", k[k.cat].pref.value_counts().sort_index().to_dict())
for area in ("hippocampus", "amygdala"):
    k = K[K.area == area]
    print(area, "with the second test at a one-sided 0.05 read as two-sided 0.05 (variant):",
          int(((k.p_anova < 0.05) & (k.p_cat_t < 0.05)).sum()))
byp = K[K.cat].groupby(["area", "patient"]).size().unstack(0, fill_value=0)
print("category neurons by patient (hippocampus, amygdala):")
print(byp.T.to_string())

# %% md
# **Result: ...**
EOF
cd $TMPDIR && source env/bin/activate && python nb/dev.py entries/001187-daume-2024/notebook.py 2>&1 | sed -n '/cell 37/,$p'
```

```
--- cell 37 0.0s
selection time 172 s
             cat  ms
area                
amygdala     222  69
hippocampus  102  53
units whose ANOVA was undefined (no spikes in any window): 0
--- cell 40 171.6s
                      units      wm_sig      ltm_sig     
shift                  -5.0  0.0   -5.0  0.0    -5.0  0.0
session                                                  
sub-10_ses-1_P68CS       21   21      1    4       0    3
sub-11_ses-1_P69CS       15   15      0    6       0    1
sub-12_ses-1_P70CS       15   15      0    5       1    6
sub-12_ses-2_P70CS        6    6      0    0       0    0
sub-13_ses-1_P71CS        3    3      1    0       0    0
sub-14_ses-1_P73CS       22   22      0    8       1    2
sub-15_ses-1_P74CS        8    8      1    6       0    0
sub-16_ses-1_P76CS       30   30      1   15       0    1
sub-16_ses-2_P76CS        4    4      0    0       0    0
[... 57 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/nb/dev.py <<'EOF'
"""Run cells [start, stop) of notebook.py; state is saved to/loaded from ns.pkl."""
import sys, pickle, time, types
sys.path.insert(0, 'entries/001187-daume-2024')
src = open(sys.argv[1]).read().split("# %%")[1:]
start = int(sys.argv[2]); stop = int(sys.argv[3]) if len(sys.argv) > 3 else 10**6
ns = {}
if start > 0:
    ns.update(pickle.load(open('/tmp/claude-1001/ns.pkl', 'rb')))
    exec("import time, numpy as np, pandas as pd, matplotlib.pyplot as plt, sbcat\nfrom scipy.stats import norm\nfrom scipy import stats as st", ns)
for i, c in enumerate(src):
    if i < start or i >= stop: continue
    if c.startswith(" md"): continue
    code = c.split("\n", 1)[1]
    code = code.replace("S = sbcat.load_all()", "import pickle; S = pickle.load(open('/tmp/claude-1001/S.pkl','rb')); [s.update(spikes=[np.sort(x) for x in s['spikes']], unsorted_units=[]) for s in S]")
    t = time.time()
    exec(code, ns)
    print(f"--- cell {i} {time.time()-t:.1f}s", flush=True)
keep = {k: v for k, v in ns.items() if not k.startswith("__") and not isinstance(v, types.ModuleType)
        and not callable(v)}
pickle.dump(keep, open('/tmp/claude-1001/ns.pkl', 'wb'))
EOF
cd $TMPDIR && source env/bin/activate && python nb/dev.py entries/001187-daume-2024/notebook.py 0 41 2>&1 | tail -3
```

```
hippocampus  102  53
units whose ANOVA was undefined (no spikes in any window): 0
--- cell 40 166.6s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat >> entries/001187-daume-2024/sbcat.py <<'EOF'


def normalize(rate, base_mean):
    """Percent change to the mean baseline rate (claims B)."""
    return (rate / base_mean - 1.0) * 100.0


def om_remove(df, conds, value="FR", unit="neuron", zero_col=None):
    """Rule O-M (Methods, Statistics) for a table of rows: per unit and condition (the
    combinations of the columns conds), the mean of value; a unit is removed when it has no
    spikes in a tested condition (zero_col summed over the condition's rows is 0) or when any
    condition mean lies outside mean +- 3 SD of all unit and condition means. Returns the set
    of removed units."""
    g = df.groupby([unit] + conds)
    m = g[value].mean()
    bad = set(m.index.get_level_values(0)[np.abs(m.values - m.mean()) > 3 * m.std()])
    if zero_col is not None:
        z = g[zero_col].sum()
        bad |= set(z.index.get_level_values(0)[z.values == 0])
    return bad


def oc_remove(df, value="FR", unit="neuron"):
    """Rule O-C (NWB_computeGLM.m): units whose mean value over all their rows exceeds 3 SD of
    the unit means, without centring and on the upper side only."""
    m = df.groupby(unit)[value].mean()
    return set(m.index[m > 3 * m.std()])
EOF
cat > $TMPDIR/t_glm.py <<'EOF'
import sys, pickle, time, numpy as np, pandas as pd
sys.path.insert(0,'entries/001187-daume-2024'); import sbcat
ns=pickle.load(open('/tmp/claude-1001/ns.pkl','rb')); K=ns['K']; S=ns['S']
PT={si: sbcat.picture_table(S[si]) for si in K.si.unique()}
rows=[]
t=time.time()
for _,u in K[K.cat & (K.area=='hippocampus')].iterrows():
    pt=sbcat.add_counts(PT[u.si], S[u.si]['spikes'][u.ui]).assign(neuron=f"{u.si}_{u.ui}", patient=u.patient, pref=lambda d:(d.cat==u.pref).astype(int))
    tr=pt.groupby('trial').agg(r_maint=('r_maint','first'),r_bsl=('r_bsl','first'),c_maint=('c_maint','first'),acc=('acc_WM','first'),load=('load','first'),pref=('pref','max'),neuron=('neuron','first'),patient=('patient','first'))
    tr['FR']=sbcat.normalize(tr.r_maint, tr.r_bsl.mean())
    rows.append(tr)
D=pd.concat(rows); D=D[np.isfinite(D.FR)]
print(len(D), time.time()-t)
d=D[D.acc==1]
t=time.time(); print(sbcat.mixedlm(d,'pref')); print(time.time()-t)
EOF
cd $TMPDIR && source env/bin/activate && python t_glm.py
```

```
Exit code 1
14278 0.35322999954223633
Traceback (most recent call last):
  File "/tmp/claude-1001/t_glm.py", line 15, in <module>
    t=time.time(); print(sbcat.mixedlm(d,'pref')); print(time.time()-t)
                         ~~~~~~~~~~~~~^^^^^^^^^^
  File "entries/001187-daume-2024/sbcat.py", line 265, in mixedlm
    md = smf.mixedlm(f"{dv} ~ {formula}", df, groups="patient", re_formula="1",
                     vc_formula={"neuron": "0 + C(neuron)"})
  File "/tmp/claude-1001/env/lib/python3.13/site-packages/statsmodels/regression/mixed_linear_model.py", line 1137, in from_formula
    mod = super().from_formula(formula, data, *args, **kwargs)
  File "/tmp/claude-1001/env/lib/python3.13/site-packages/statsmodels/base/model.py", line 243, in from_formula
    mod = cls(endog, exog, *args, **kwargs)
  File "/tmp/claude-1001/env/lib/python3.13/site-packages/statsmodels/regression/mixed_linear_model.py", line 883, in __init__
    a = self._augment_exog(i)
  File "/tmp/claude-1001/env/lib/python3.13/site-packages/statsmodels/regression/mixed_linear_model.py", line 1584, in _augment_exog
    ex = np.concatenate(ex, axis=1)
ValueError: all the input array dimensions except for the concatenation axis must match exactly, but along dimension 0, the array at index 0 has size 393 and the array at index 1 has size 37743
```

**Agent calls Bash**

```bash
cd entries/001187-daume-2024 && python - <<'EOF'
s=open('sbcat.py').read()
s=s.replace('''    import warnings
    with warnings.catch_warnings():''','''    import warnings
    df = df.reset_index(drop=True)
    with warnings.catch_warnings():''')
open('sbcat.py','w').write(s)
EOF
cd $TMPDIR && source env/bin/activate && python t_glm.py
```

```
14278 0.3540005683898926
                beta         SE         t         p
Intercept  20.579064  15.851020  1.298280  0.194213
pref       12.845319   2.943418  4.364082  0.000013
1.1226375102996826
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat >> entries/001187-daume-2024/notebook.py <<'EOF'

# %% md
# ## Tables of category neurons
#
# For each category neuron, one row per encoding picture of every WM trial with its spike
# counts in the maintenance (0 to 2.5 s after maintenance onset), baseline (-0.9 to -0.3 s
# before picture 1) and picture 1 (0 to 2 s) windows, and, for pictures shown in the LTM test,
# that trial's accuracy and confidence (sbcat.picture_table, sbcat.add_counts).

# %%
PT = {si: sbcat.picture_table(S[si]) for si in sorted(K.si.unique())}
CN = K[K.cat].copy()
CN["neuron"] = [f"{a}_{b}" for a, b in zip(CN.si, CN.ui)]
NPT = {}
for _, u in CN.iterrows():
    pt = sbcat.add_counts(PT[u.si], S[u.si]["spikes"][u.ui])
    pt["pref"] = (pt.cat == u.pref).astype(int)
    pt["neuron"], pt["patient"], pt["area"] = u.neuron, u.patient, u.area
    NPT[u.neuron] = pt
print("category neurons:", len(NPT), " picture rows per neuron:",
      sorted({len(p) for p in NPT.values()}))
print("pictures shown in the LTM test per session: %d to %d" % (
    min(p.in_ltm.sum() for p in PT.values()), max(p.in_ltm.sum() for p in PT.values())))


def trial_rows(pt):
    """One row per WM trial; pref is true when any encoding picture is of the preferred
    category."""
    return pt.groupby("trial").agg(r_maint=("r_maint", "first"), r_bsl=("r_bsl", "first"),
                                   c_maint=("c_maint", "first"), c_bsl=("c_bsl", "first"),
                                   r_enc1=("r_enc1", "first"), acc=("acc_WM", "first"),
                                   load=("load", "first"), pref=("pref", "max"),
                                   neuron=("neuron", "first"), patient=("patient", "first"),
                                   area=("area", "first")).reset_index()


def code_rows(pt):
    """The rows of the paper's code (NWB_computeGLM.m): one per encoding picture later shown
    in the LTM test, pref per picture."""
    return pt[pt.in_ltm].rename(columns={"acc_WM": "acc"}).reset_index(drop=True)


def wm_table(neurons, rows, base, value="r_maint"):
    """Normalized rates (claims B) for the given neurons. rows 'trial' or 'code'; base 'B1'
    (mean baseline over all WM trials of the neuron) or 'B2' (over the rows of the code's
    table). Neurons with a zero baseline are dropped (their values are infinite)."""
    out = []
    for n in neurons:
        pt = NPT[n]
        tr = trial_rows(pt)
        d = tr if rows == "trial" else code_rows(pt)
        b = tr.r_bsl.mean() if base == "B1" else code_rows(pt).r_bsl.mean()
        if b == 0:
            continue
        d = d.copy()
        d["FR"] = sbcat.normalize(d[value], b)
        out.append(d)
    return pd.concat(out, ignore_index=True)


def fit_readings(neurons, select, formula, conds, readings, zero_col="c_maint", value="r_maint"):
    """Fit the GLM under each reading; readings are (rows, base) pairs. Outliers by O-M
    (main) and O-C (variant, on all rows of the table before selection) and none."""
    res = []
    for rows, base in readings:
        full = wm_table(neurons, rows, base, value)
        d = select(full)
        for orule in ("O-M", "O-C", "none"):
            if orule == "O-M":
                bad = sbcat.om_remove(d, conds, zero_col=zero_col)
            elif orule == "O-C":
                bad = sbcat.oc_remove(full)
            else:
                bad = set()
            dd = d[~d.neuron.isin(bad)]
            m = sbcat.mixedlm(dd, formula)
            for term, r in m.iterrows():
                res.append(dict(rows=rows, base=base, outliers=orule, term=term, beta=r.beta,
                                SE=r.SE, p=r.p, neurons=m.attrs["neurons"], n=m.attrs["n"],
                                removed=len(bad), converged=m.attrs["converged"]))
    return pd.DataFrame(res)


def show(res, terms=None):
    r = res if terms is None else res[res.term.isin(terms)]
    print(r.round({"beta": 2, "SE": 2, "p": 6}).to_string(index=False))


HIPP_CN = CN.neuron[CN.area == "hippocampus"].tolist()
AMYG_CN = CN.neuron[CN.area == "amygdala"].tolist()
READ4 = [("trial", "B1"), ("trial", "B2"), ("code", "B1"), ("code", "B2")]

# %% md
# ## Claim fig2b-hippocampus-persistent
#
# > Hippocampal category neurons are persistently active above baseline during maintenance and
# > fire more when an image of their preferred category is held in WM.
#
# All correct WM trials, both loads; FR ~ pref with the random intercepts of G. Readings: rows
# (a) one per trial or (b) the code's rows, baseline B1 or B2; outliers O-M (main), O-C and none
# shown beside.

# %% tags=claim:fig2b-hippocampus-persistent
R2B = fit_readings(HIPP_CN, lambda d: d[d.acc == 1], "pref", ["pref"], READ4)
show(R2B)

# %% md
# **Result: ...**

# %% md
# ## Claim fig2c-hippocampus-correct-load
#
# > When the preferred category is held, hippocampal category neurons fire more in correct than
# > incorrect trials and more in load 1 than load 3 trials.
#
# Trials holding a preferred picture, correct and incorrect, both loads (one row per trial);
# acc (incorrect the reference) and l1 (load 1 against load 3). Readings: (a) main effects, (b)
# with their interaction; baseline B1 or B2.

# %% tags=claim:fig2c-hippocampus-correct-load
def pref_trials(d):
    d = d[d.pref == 1].copy()
    d["l1"] = (d.load == 1).astype(int)
    return d

R2C = pd.concat([fit_readings(HIPP_CN, pref_trials, f, ["acc", "l1"],
                              [("trial", "B1"), ("trial", "B2")]).assign(model=lab)
                 for lab, f in [("(a) main", "acc + l1"), ("(b) interaction", "acc * l1")]])
show(R2C[["model", "rows", "base", "outliers", "term", "beta", "SE", "p", "neurons", "n"]])
d = pref_trials(wm_table(HIPP_CN, "trial", "B1"))
print("rows by accuracy and load (B1):", d.groupby(["acc", "l1"]).size().to_dict())

# %% md
# **Result: ...**

# %% md
# ## Claim fig2e-amygdala-persistent
#
# > Amygdala category neurons are also persistently active during maintenance and fire more for
# > the preferred category.

# %% tags=claim:fig2e-amygdala-persistent
R2E = fit_readings(AMYG_CN, lambda d: d[d.acc == 1], "pref", ["pref"], READ4)
show(R2E)

# %% md
# **Result: ...**

# %% md
# ## Claim fig2f-amygdala-load-not-accuracy
#
# > When the preferred category is held, amygdala category neurons fire more in load 1 than load
# > 3 trials, but not more in correct than incorrect trials.

# %% tags=claim:fig2f-amygdala-load-not-accuracy
R2F = pd.concat([fit_readings(AMYG_CN, pref_trials, f, ["acc", "l1"],
                              [("trial", "B1"), ("trial", "B2")]).assign(model=lab)
                 for lab, f in [("(a) main", "acc + l1"), ("(b) interaction", "acc * l1")]])
show(R2F[["model", "rows", "base", "outliers", "term", "beta", "SE", "p", "neurons", "n"]])

# %% md
# **Result: ...**
EOF
cd $TMPDIR && source env/bin/activate && python nb/dev.py entries/001187-daume-2024/notebook.py 41 2>&1 | tail -150
```

```
category neurons by patient (hippocampus, amygdala):
patient      1  10  11  12  14  15  16  17  19   2  20  21  22  23  26  27  28  29   3  30  31  32  33  34  36  37  39   4   5  6  7  8  9
area                                                                                                                                      
amygdala     5   1   4   5   8   6  12  11  24  21  20  12   0  11   0  10   3   6  14   0   1   1   5   0   0   0   0  10  13  5  2  7  5
hippocampus  3   3   2   0   0   0   4   2  10   2   4  11   3   7   4  11   4   1   1   2   0   2   3   4   1   1   6   0   6  0  0  5  0
--- cell 44 0.0s
category neurons: 324  picture rows per neuron: [277, 280]
pictures shown in the LTM test per session: 78 to 200
--- cell 47 0.7s
 rows base outliers      term  beta    SE        p  neurons     n  removed  converged
trial   B1      O-M Intercept 15.80  8.12 0.051664       97 12782        5       True
trial   B1      O-M      pref  7.79  2.33 0.000827       97 12782        5       True
trial   B1      O-C Intercept 19.55  5.36 0.000269      100 13179        2       True
trial   B1      O-C      pref 13.12  2.60 0.000000      100 13179        2       True
trial   B1     none Intercept 20.58 15.85 0.194213      102 13414        0       True
trial   B1     none      pref 12.85  2.94 0.000013      102 13414        0       True
trial   B2      O-M Intercept 22.38  5.79 0.000113      100 13179        2       True
trial   B2      O-M      pref 11.86  2.66 0.000008      100 13179        2       True
trial   B2      O-C Intercept 22.38  5.79 0.000113      100 13179        2       True
trial   B2      O-C      pref 11.86  2.66 0.000008      100 13179        2       True
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cat > $TMPDIR/t2.py <<'EOF'
import sys, pickle, numpy as np, pandas as pd, warnings
sys.path.insert(0,'entries/001187-daume-2024'); import sbcat
warnings.simplefilter('ignore')
ns=pickle.load(open('/tmp/claude-1001/ns.pkl','rb'))
src=open('entries/001187-daume-2024/notebook.py').read().split('# %%')
g=dict(ns); exec("import numpy as np, pandas as pd, sbcat\n"+src[47].split('\n',1)[1], g)
d=g['wm_table'](g['AMYG_CN'],'trial','B1'); d=d[d.acc==1]
bad=sbcat.om_remove(d,['pref'],zero_col='c_maint'); d=d[~d.neuron.isin(bad)].reset_index(drop=True)
import statsmodels.formula.api as smf
md=smf.mixedlm("FR ~ pref", d, groups="patient", re_formula="1", vc_formula={"neuron":"0 + C(neuron)"})
for m in ["lbfgs","powell","nm","bfgs","cg"]:
    try:
        r=md.fit(reml=False, method=m); print(m, r.llf, r.fe_params.values, r.bse_fe.values, r.cov_re.values.ravel(), r.vcomp, r.converged)
    except Exception as e: print(m,e)
print(d.groupby('patient').neuron.nunique().to_dict())
EOF
cd $TMPDIR && source env/bin/activate && python t2.py
```

```
Exit code 1
Sun Nov  1 07:38:44 UTC 2026
Traceback (most recent call last):
  File "/tmp/claude-1001/t2.py", line 7, in <module>
    d=g['wm_table'](g['AMYG_CN'],'trial','B1'); d=d[d.acc==1]
      ~^^^^^^^^^^^^
KeyError: 'wm_table'
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -n "^def wm_table" -m1 entries/001187-daume-2024/notebook.py; python3 - <<'EOF'
src=open('entries/001187-daume-2024/notebook.py').read().split('# %%')[1:]
for i,c in enumerate(src):
    if 'def wm_table' in c: print(i)
EOF
```

```
492:def wm_table(neurons, rows, base, value="r_maint"):
47
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i "s/src=open(\(.*\)).read().split('# %%')$/src=open(\1).read().split('# %%')[1:]/" t2.py && source env/bin/activate && python t2.py
```

```
/tmp/claude-1001/t2.py:13: ConvergenceWarning: The Hessian matrix at the estimated parameter values is not positive definite.
  r=md.fit(reml=False, method=m); print(m, r.llf, r.fe_params.values, r.bse_fe.values, r.cov_re.values.ravel(), r.vcomp, r.converged)
category neurons: 324  picture rows per neuron: [277, 280]
pictures shown in the LTM test per session: 78 to 200
lbfgs -180767.6531458843 [9.16390802 5.43856741] [14.67229311  1.38532059] [5280.14475727] [1215.55545333] True
powell -180736.43322066878 [10.0811838   5.44414385] [2.9487794  1.38713432] [78.3826832] [868.00972284] True
nm -180736.4178139712 [10.06479801  5.44409374] [3.03283806 1.38712295] [89.62254642] [864.10267014] True
bfgs -180736.41781566312 [10.06493863  5.44409769] [3.03176204 1.38712435] [89.5039373] [863.88998918] True
cg -180736.4178127553 [10.06495092  5.44409454] [3.0320534  1.38712318] [89.5186212] [864.1106705] True
{'1': 5, '10': 1, '11': 4, '12': 5, '14': 8, '15': 6, '16': 11, '17': 11, '19': 24, '2': 21, '20': 19, '21': 11, '23': 11, '27': 10, '28': 3, '29': 6, '3': 13, '31': 1, '32': 1, '33': 5, '4': 10, '5': 13, '6': 5, '7': 2, '8': 7, '9': 5}
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/001187-daume-2024 && python - <<'EOF'
s=open('sbcat.py').read()
old='''        res = md.fit(reml=False, method=["lbfgs", "powell"])'''
new='''        # lbfgs alone can stop at a local optimum of the variance parameters; three
        # optimizers are run and the fit with the highest likelihood is kept.
        fits = []
        for m in ("bfgs", "lbfgs", "powell"):
            try:
                fits.append(md.fit(reml=False, method=m))
            except Exception:
                pass
        res = max(fits, key=lambda r: r.llf)'''
assert old in s
s=s.replace(old,new)
open('sbcat.py','w').write(s)
EOF
echo
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('sbcat.py').read()
old='''def om_remove(df, conds, value="FR", unit="neuron", zero_col=None):'''
new='''def om_remove(df, conds, value="FR", unit="neuron", zero_col=None, marginal=False):'''
s=s.replace(old,new)
old='''    g = df.groupby([unit] + conds)
    m = g[value].mean()
    bad = set(m.index.get_level_values(0)[np.abs(m.values - m.mean()) > 3 * m.std()])'''
new='''    if marginal:
        # conditions are the levels of each factor separately
        ms = [df.groupby([unit, c])[value].mean() for c in conds]
        allv = np.concatenate([m.values for m in ms])
        mu, sd = allv.mean(), allv.std(ddof=1)
        bad = set()
        for m in ms:
            bad |= set(m.index.get_level_values(0)[np.abs(m.values - mu) > 3 * sd])
    else:
        m = df.groupby([unit] + conds)[value].mean()
        bad = set(m.index.get_level_values(0)[np.abs(m.values - m.mean()) > 3 * m.std()])
    g = df.groupby([unit] + conds)'''
assert old in s
s=s.replace(old,new)
s=s.replace('''    statistic, sign flips. Returns a list''','''    statistic, sign flips. Returns the t of each time point and a list''')
s+='''

def binned_counts(spikes, t0, centres, width):
    """Spike counts in windows [c - width/2, c + width/2) around each centre, per event."""
    t0 = np.asarray(t0, float)[:, None]
    lo = t0 + np.asarray(centres)[None, :] - width / 2
    return (np.searchsorted(spikes, lo + width, side="left")
            - np.searchsorted(spikes, lo, side="left"))
'''
open('sbcat.py','w').write(s)
n=open('notebook.py').read()
old='''        for orule in ("O-M", "O-C", "none"):
            if orule == "O-M":
                bad = sbcat.om_remove(d, conds, zero_col=zero_col)'''
new='''        for orule in ("O-M", "O-M marginal", "O-C", "none"):
            if orule == "O-M marginal" and len(conds) < 2:
                continue
            if orule.startswith("O-M"):
                bad = sbcat.om_remove(d, conds, zero_col=zero_col, marginal=orule != "O-M")'''
assert old in n
n=n.replace(old,new)
n=n.replace('''    """Fit the GLM under each reading; readings are (rows, base) pairs. Outliers by O-M
    (main) and O-C (variant, on all rows of the table before selection) and none."""''','''    """Fit the GLM under each reading; readings are (rows, base) pairs. Outliers by O-M
    (main; conditions the cells of the factors, or, as a second reading, each factor's levels
    taken separately), O-C (variant, on all rows of the table before selection) and none."""''')
open('notebook.py','w').write(n)
EOF
echo
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cat >> notebook.py <<'EOF'

# %% md
# ## The table of Figure 3 (NWB_computeGLM.m)
#
# One row per WM picture later shown in the LTM test; rate 0 to 2.5 s after maintenance onset,
# normalized to the mean baseline over all the neuron's rows (B, as the code); then rows kept
# when the WM trial was correct and the picture is of the preferred category. Confidence is
# recoded as the Methods say (sbcat.conf3_code). The session whose ratings are all sure is left
# out of these confidence analyses (Results, paragraph 2); the code keeps it, shown as a
# variant. Area: hipp = 1 for hippocampus, amygdala the reference.

# %%
NOCONF_SI = [si for si, s in enumerate(S) if s["identifier"] in noconf]


def fig3_full(neurons, value="r_maint"):
    d = wm_table(neurons, "code", "B2", value)
    d["hipp"] = (d.area == "hippocampus").astype(int)
    d["conf3"] = sbcat.conf3_code(d.conf)
    d["si"] = [int(n.split("_")[0]) for n in d.neuron]
    return d


def fig3_select(d, pref=1, keep_noconf=False):
    d = d[(d.acc == 1) & (d.pref == pref) & d.conf.notna()]
    if not keep_noconf:
        d = d[~d.si.isin(NOCONF_SI)]
    return d


ALL_CN = HIPP_CN + AMYG_CN
F3FULL = fig3_full(ALL_CN)
F3 = fig3_select(F3FULL)
print("rows", len(F3), "neurons", F3.neuron.nunique(), "by area:",
      F3.groupby("area").neuron.nunique().to_dict())
print("rows by LTM accuracy and confidence:", F3.groupby(["LTMacc", "conf3"]).size().to_dict())
print("neurons dropped for a zero baseline:", len(ALL_CN) - F3FULL.neuron.nunique())
print("FR (%% change) range: %.1f to %.1f" % (F3.FR.min(), F3.FR.max()))


def fig3_fit(data_full, formula, conds, select=fig3_select, outlier_pool=None, label=""):
    """Fit under O-M (cells), O-M marginal, O-C and none. outlier_pool: the table on which
    outliers are found (default the selected data)."""
    d = select(data_full)
    pool = d if outlier_pool is None else outlier_pool
    res = []
    for orule in ("O-M", "O-M marginal", "O-C", "none"):
        if orule.startswith("O-M"):
            bad = sbcat.om_remove(pool, conds, zero_col="c_maint", marginal=orule != "O-M")
        elif orule == "O-C":
            bad = sbcat.oc_remove(data_full)
        else:
            bad = set()
        dd = d[~d.neuron.isin(bad)]
        m = sbcat.mixedlm(dd, formula)
        for term, r in m.iterrows():
            res.append(dict(reading=label, outliers=orule, term=term, beta=r.beta, SE=r.SE, p=r.p,
                            neurons=m.attrs["neurons"], n=m.attrs["n"], removed=len(bad)))
    return pd.DataFrame(res)

# %% md
# ## Claim fig3a-area-interactions
#
# > In a GLM over category neurons of both areas, no main effect of LTM accuracy, confidence or
# > area is significant, nor the LTM accuracy by confidence interaction, but every interaction
# > with area is, so the relation of maintenance activity to later memory differs between
# > hippocampus and amygdala.
#
# FR ~ LTMacc * conf3 * hipp. Expected: conf3:hipp 16.88 +- 1.69, LTMacc:hipp 59.78 +- 5.98,
# LTMacc:conf3:hipp -28.64 +- 2.86.

# %% tags=claim:fig3a-area-interactions
R3A = pd.concat([
    fig3_fit(F3FULL, "LTMacc * conf3 * hipp", ["LTMacc", "conf3"], label="main"),
    fig3_fit(F3FULL, "LTMacc * conf3 * hipp", ["LTMacc", "conf3"],
             select=lambda d: fig3_select(d, keep_noconf=True), label="with the all-sure session")])
show(R3A)

# %% md
# **Result: ...**

# %% md
# ## Claim fig3b-hippocampus-predicts-ltm
#
# > In the hippocampus, maintenance activity of category neurons for the preferred category
# > predicts later LTM accuracy and confidence, with an interaction between the two, so activity
# > is higher for pictures later remembered than forgotten.
#
# FR ~ LTMacc * conf3 on hippocampal neurons; outliers found over both areas (a) or within the
# hippocampus (b). Expected: conf3 20.30 +- 2.03, LTMacc 67.90 +- 6.79, LTMacc:conf3 -30.80 +-
# 3.08.

# %% tags=claim:fig3b-hippocampus-predicts-ltm
def area_sel(area, keep_noconf=False):
    return lambda d: fig3_select(d[d.area == area], keep_noconf=keep_noconf)

H3FULL = F3FULL[F3FULL.area == "hippocampus"]
A3FULL = F3FULL[F3FULL.area == "amygdala"]
R3B = pd.concat([
    fig3_fit(H3FULL, "LTMacc * conf3", ["LTMacc", "conf3"], select=area_sel("hippocampus"),
             outlier_pool=F3, label="(a) outliers over both areas"),
    fig3_fit(H3FULL, "LTMacc * conf3", ["LTMacc", "conf3"], select=area_sel("hippocampus"),
             label="(b) outliers within the area"),
    fig3_fit(H3FULL, "LTMacc * conf3", ["LTMacc", "conf3"],
             select=area_sel("hippocampus", True), label="(b) with the all-sure session")])
show(R3B)

# %% md
# **Result: ...**

# %% md
# ## Claim fig3b-amygdala-no-prediction
#
# > In the amygdala, maintenance activity of category neurons does not predict later LTM
# > accuracy or confidence.

# %% tags=claim:fig3b-amygdala-no-prediction
R3BA = pd.concat([
    fig3_fit(A3FULL, "LTMacc * conf3", ["LTMacc", "conf3"], select=area_sel("amygdala"),
             outlier_pool=F3, label="(a) outliers over both areas"),
    fig3_fit(A3FULL, "LTMacc * conf3", ["LTMacc", "conf3"], select=area_sel("amygdala"),
             label="(b) outliers within the area"),
    fig3_fit(A3FULL, "LTMacc * conf3", ["LTMacc", "conf3"],
             select=area_sel("amygdala", True), label="(b) with the all-sure session")])
show(R3BA)
EOF
cd $TMPDIR && source env/bin/activate && python nb/dev.py entries/001187-daume-2024/notebook.py 44 2>&1 | grep -v Warning | tail -150
```

```
main O-M marginal LTMacc:conf3:hipp -16.64  8.71 0.055992      265  9612       53
                     main          O-C         Intercept   7.49  8.30 0.366613      310 11226        8
                     main          O-C            LTMacc   0.13 11.57 0.991079      310 11226        8
                     main          O-C             conf3   3.40  4.47 0.447993      310 11226        8
                     main          O-C      LTMacc:conf3   0.26  5.56 0.963076      310 11226        8
                     main          O-C              hipp -11.49 14.52 0.428989      310 11226        8
                     main          O-C       LTMacc:hipp  56.61 21.17 0.007505      310 11226        8
                     main          O-C        conf3:hipp  16.60  7.98 0.037586      310 11226        8
                     main          O-C LTMacc:conf3:hipp -27.83 10.11 0.005927      310 11226        8
                     main         none         Intercept  17.76 13.20 0.178491      318 11500        0
                     main         none            LTMacc  -8.98 17.60 0.610130      318 11500        0
                     main         none             conf3   5.05  6.74 0.453634      318 11500        0
                     main         none      LTMacc:conf3   0.08  8.43 0.992171      318 11500        0
                     main         none              hipp -14.83 23.14 0.521539      318 11500        0
                     main         none       LTMacc:hipp 110.03 32.07 0.000604      318 11500        0
                     main         none        conf3:hipp  18.33 12.01 0.126892      318 11500        0
                     main         none LTMacc:conf3:hipp -43.78 15.31 0.004250      318 11500        0
with the all-sure session          O-M         Intercept  11.50  7.11 0.106188      271  9792       53
with the all-sure session          O-M            LTMacc  -0.13  9.90 0.989450      271  9792       53
with the all-sure session          O-M             conf3   2.33 
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python - <<'EOF' 2>/dev/null
import pickle, pandas as pd
pd.set_option('display.width',200)
ns=pickle.load(open('/tmp/claude-1001/ns.pkl','rb'))
for k in ['R2B','R2E']:
    r=ns[k]; print(k); print(r[r.outliers!='none'].round(4).to_string(index=False))
for k in ['R2C','R2F']:
    r=ns[k]; r=r[(r.term!='Intercept')&(r.outliers!='none')]; print(k); print(r[['model','base','outliers','term','beta','p','neurons']].round(4).to_string(index=False))
r=ns['R3A']; print(r[(r.reading=='main')&(r.outliers.isin(['O-M']))].round(4).to_string(index=False))
EOF
```

```
R2B
 rows base outliers      term    beta     SE      p  neurons     n  removed  converged
trial   B1      O-M Intercept 17.2883 5.1477 0.0008       97 12782        5       True
trial   B1      O-M      pref  7.7931 2.3284 0.0008       97 12782        5       True
trial   B1      O-C Intercept 19.3876 5.5618 0.0005      100 13179        2       True
trial   B1      O-C      pref 13.1173 2.5971 0.0000      100 13179        2       True
trial   B2      O-M Intercept 22.3817 5.7950 0.0001      100 13179        2       True
trial   B2      O-M      pref 11.8580 2.6572 0.0000      100 13179        2       True
trial   B2      O-C Intercept 22.3817 5.7950 0.0001      100 13179        2       True
trial   B2      O-C      pref 11.8580 2.6572 0.0000      100 13179        2       True
 code   B1      O-M Intercept 21.9286 5.3338 0.0000       99 17302        3       True
 code   B1      O-M      pref  7.0612 2.5739 0.0061       99 17302        3       True
 code   B1      O-C Intercept 21.6070 5.2883 0.0000      100 17386        2       True
 code   B1      O-C      pref  8.4765 2.5924 0.0011      100 17386        2       True
 code   B2      O-M Intercept 27.8398 6.3178 0.0000      101 17628        1       True
 code   B2      O-M      pref  6.1779 2.8879 0.0324      101 17628        1       True
 code   B2      O-C Intercept 25.4168 6.0104 0.0000      100 17496        2       True
 code   B2      O-C      pref  6.8975 2.8115 0.0142      100 17496        2       True
R2E
 rows base outliers      term    beta     SE      p  neurons     n  removed  converged
[... 90 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd entries/001187-daume-2024 && python - <<'EOF'
n=open('notebook.py').read()
old='''def fig3_fit(data_full, formula, conds, select=fig3_select, outlier_pool=None, label=""):
    """Fit under O-M (cells), O-M marginal, O-C and none. outlier_pool: the table on which
    outliers are found (default the selected data)."""
    d = select(data_full)
    pool = d if outlier_pool is None else outlier_pool
    res = []
    for orule in ("O-M", "O-M marginal", "O-C", "none"):
        if orule.startswith("O-M"):
            bad = sbcat.om_remove(pool, conds, zero_col="c_maint", marginal=orule != "O-M")'''
new='''def fig3_fit(data_full, formula, conds, select=fig3_select, outlier_pool=None, label=""):
    """Fit under O-M, O-M with confidence levels as conditions too, O-C and none. outlier_pool:
    the table on which outliers are found (default the selected data). The conditions of O-M
    are the levels of the categorical factors (conds); confidence enters the model as a
    continuous variable (Methods), so the main reading does not split by it, and the second
    reading does (cells of conds and conf3)."""
    d = select(data_full)
    pool = d if outlier_pool is None else outlier_pool
    res = []
    for orule in ("O-M", "O-M by confidence", "O-C", "none"):
        if orule.startswith("O-M"):
            cc = conds if orule == "O-M" else conds + ["conf3"]
            bad = sbcat.om_remove(pool, cc, zero_col="c_maint")'''
assert old in n
n=n.replace(old,new)
n=n.replace('"LTMacc * conf3 * hipp", ["LTMacc", "conf3"]','"LTMacc * conf3 * hipp", ["LTMacc"]')
n=n.replace('"LTMacc * conf3", ["LTMacc", "conf3"]','"LTMacc * conf3", ["LTMacc"]')
open('notebook.py','w').write(n)
EOF
grep -c '\["LTMacc"\]' notebook.py
```

```
Sun Nov  1 07:42:27 UTC 2026
8
```

**Agent calls Bash**

```bash
cat >> notebook.py <<'EOF'

# %% md
# **Result: ...**

# %% md
# ## Claims fig3c-hippocampus-high-confidence and fig3d-amygdala-no-difference
#
# > Across hippocampal category neurons, maintenance firing for the preferred category is higher
# > for pictures later remembered than forgotten with high confidence, but not with low
# > confidence.
#
# > Across amygdala category neurons, maintenance firing does not differ between later
# > remembered and forgotten pictures, with high or low confidence.
#
# Rows of the Figure 3 table (correct WM trials, preferred pictures later tested, the all-sure
# session left out). High: remembered rating 6 against forgotten rating 1; low: remembered 4 or 5
# against forgotten 2 or 3. Per neuron the mean rate per condition; neurons without rows or
# without spikes in a condition, with a zero baseline, or outside mean +- 3 SD of the neuron and
# condition values of the test (O-M) are removed; paired permutation t-test (P). Readings: (a)
# normalized rate, (b) spikes per second.

# %%
CONDS = {"high": ([6], [1]), "low": ([4, 5], [2, 3])}


def remembered_forgotten(area, level, value, rng, data=None):
    d = F3 if data is None else data
    d = d[d.area == area]
    rem, forg = CONDS[level]
    col = "FR" if value == "norm" else "r_maint"
    a = d[d.conf.isin(rem)].groupby("neuron").agg(v=(col, "mean"), c=("c_maint", "sum"))
    b = d[d.conf.isin(forg)].groupby("neuron").agg(v=(col, "mean"), c=("c_maint", "sum"))
    j = a.join(b, lsuffix="_r", rsuffix="_f", how="inner")
    n_both = len(j)
    j = j[(j.c_r > 0) & (j.c_f > 0)]
    n_spk = len(j)
    vals = j[["v_r", "v_f"]].values
    out = np.any(np.abs(vals - vals.mean()) > 3 * vals.std(ddof=1), axis=1)
    j = j[~out]
    t, p, df = sbcat.perm_ttest_paired(j.v_r, j.v_f, rng)
    return dict(area=area, level=level, value=value, with_both=n_both, with_spikes=n_spk,
                n=len(j), mean_rem=j.v_r.mean(), mean_forg=j.v_f.mean(),
                diff=(j.v_r - j.v_f).mean(), t=t, df=df, p=p), j.index.tolist()


rng = np.random.default_rng(301)
R3CD, KEEP3C = [], {}
for area in ("hippocampus", "amygdala"):
    for level in ("high", "low"):
        for value in ("norm", "Hz"):
            r, kept = remembered_forgotten(area, level, value, rng)
            R3CD.append(r)
            KEEP3C[(area, level, value)] = kept
R3CD = pd.DataFrame(R3CD)
print("category neurons with rows in the Figure 3 table: hippocampus",
      F3[F3.area == "hippocampus"].neuron.nunique(), "amygdala", F3[F3.area == "amygdala"].neuron.nunique())

# %% tags=claim:fig3c-hippocampus-high-confidence
print(R3CD[R3CD.area == "hippocampus"].round(4).to_string(index=False))
print("paper: high t(82) = 2.16, p = 0.028; low t(68) = -1.38, p = 0.17")

# %% md
# **Result: ...**

# %% tags=claim:fig3d-amygdala-no-difference
print(R3CD[R3CD.area == "amygdala"].round(4).to_string(index=False))
print("paper: high t(158) = 0.84, p = 0.41; low t(152) = 1.15, p = 0.26")

# %% md
# **Result: ...**

# %% md
# ## Claims fig3e-early-delay-cluster and fig3f-amygdala-no-cluster
#
# > In hippocampal category neurons, firing differs between pictures later remembered and
# > forgotten with high confidence early in the maintenance period, from 0 to 650 ms.
#
# > In amygdala category neurons, no period of the maintenance period shows a significant
# > difference between later remembered and forgotten pictures.
#
# Neurons and conditions of the high-confidence test of fig3c (and fig3d), per reading of the
# rate. Time-resolved rates over 0 to 2.5 s after maintenance onset: (a) 200 ms windows stepped
# by 25 ms, centres 0 to 2.5 s (windows reach 100 ms past the period at both ends), or (b) 50 ms
# bins, centres 25 ms to 2.475 s. Normalized rates use each neuron's mean baseline rate of the
# Figure 3 table. Cluster-based permutation test (sbcat.cluster_test), 10,000 sign flips,
# cluster-forming threshold two-sided 0.05, cluster p judged at 0.025.

# %%
BINNINGS = {"(a) 200/25 ms": (np.arange(0, 2.5001, 0.025), 0.2),
            "(b) 50 ms": (np.arange(0.025, 2.5, 0.05), 0.05)}
BASE3 = {n: g.r_bsl.mean() for n, g in F3FULL.groupby("neuron")}
NEURON_SPIKES = {n: S[u.si]["spikes"][u.ui] for n, u in CN.set_index("neuron").iterrows()}


def time_resolved(area, value, binning, rng):
    centres, width = BINNINGS[binning]
    neurons = KEEP3C[(area, "high", value)]
    d = F3[(F3.area == area) & F3.neuron.isin(neurons)]
    A, B = [], []
    for n in neurons:
        g = d[d.neuron == n]
        rates = []
        for confs in ([6], [1]):
            t0 = g.t_maint[g.conf.isin(confs)].values
            r = sbcat.binned_counts(NEURON_SPIKES[n], t0, centres, width).mean(0) / width
            rates.append(sbcat.normalize(r, BASE3[n]) if value == "norm" else r)
        A.append(rates[0])
        B.append(rates[1])
    t, cl = sbcat.cluster_test(np.array(A), np.array(B), rng)
    return centres, t, cl, len(neurons)


R3EF = []
t0 = time.time()
for area in ("hippocampus", "amygdala"):
    for value in ("norm", "Hz"):
        for binning in BINNINGS:
            rng = np.random.default_rng(302)
            centres, t, cl, n = time_resolved(area, value, binning, rng)
            for c in cl:
                R3EF.append(dict(area=area, value=value, binning=binning, neurons=n,
                                 sign="rem > forg" if c["sign"] == 1 else "rem < forg",
                                 start_s=centres[c["start"]], end_s=centres[c["end"]],
                                 cluster_sum=c["sum"], p=c["p"]))
            if not cl:
                R3EF.append(dict(area=area, value=value, binning=binning, neurons=n, sign="none"))
            print(area, value, binning, "neurons", n, "max |t| %.2f" % np.max(np.abs(t)),
                  "clusters", len(cl))
R3EF = pd.DataFrame(R3EF)
print("cluster tests took %.0f s" % (time.time() - t0))

# %% tags=claim:fig3e-early-delay-cluster
r = R3EF[R3EF.area == "hippocampus"]
print(r.round(4).to_string(index=False))
print("paper: 0 to 650 ms, cluster p = 0.0042")

# %% md
# **Result: ...**

# %% tags=claim:fig3f-amygdala-no-cluster
r = R3EF[R3EF.area == "amygdala"]
print(r.round(4).to_string(index=False))
print("smallest cluster p per reading:")
print(r.groupby(["value", "binning"]).p.min())

# %% md
# **Result: ...**

# %% md
# ## Claim fig3g-nonpreferred-no-effect
#
# > Maintenance activity of category neurons while non-preferred pictures are held does not
# > predict later LTM accuracy or confidence.
#
# The Figure 3a model on non-preferred rows: (a) every non-preferred picture of the code's
# table, (b) only pictures of trials that held no preferred picture.

# %% tags=claim:fig3g-nonpreferred-no-effect
trial_has_pref = {n: set(NPT[n].trial[NPT[n].pref == 1]) for n in ALL_CN}


def nonpref_b(d):
    d = fig3_select(d, pref=0)
    keep = [t not in trial_has_pref[n] for n, t in zip(d.neuron, d.trial)]
    return d[keep]


R3G = pd.concat([
    fig3_fit(F3FULL, "LTMacc * conf3 * hipp", ["LTMacc"], select=lambda d: fig3_select(d, pref=0),
             label="(a) all non-preferred pictures"),
    fig3_fit(F3FULL, "LTMacc * conf3 * hipp", ["LTMacc"], select=nonpref_b,
             label="(b) trials without a preferred picture")])
show(R3G)
r = R3G[(R3G.term != "Intercept") & (R3G.outliers.isin(["O-M", "O-M by confidence", "O-C"]))]
print("smallest p of a fixed effect other than the intercept, per reading and outlier rule:")
print(r.groupby(["reading", "outliers"]).p.min())

# %% md
# **Result: ...**

# %% md
# ## Claim fig3h-encoding-no-effect
#
# > Activity of category neurons during the presentation of the first encoding picture, for
# > preferred pictures, does not predict later LTM accuracy or confidence.
#
# Rate 0 to 2 s after the onset of encoding picture 1, normalized as B; correct WM trials;
# (a) trials whose first picture is of the preferred category, with that picture's LTM outcome,
# or (b) trials holding a preferred picture in any slot, with that picture's LTM outcome.

# %% tags=claim:fig3h-encoding-no-effect
E3FULL = fig3_full(ALL_CN, value="r_enc1")
E3FULL["c_maint"] = E3FULL["c_enc1"]  # the zero-spike rule applies to the tested window
R3H = pd.concat([
    fig3_fit(E3FULL, "LTMacc * conf3 * hipp", ["LTMacc"],
             select=lambda d: fig3_select(d[d.slot == 1]), label="(a) picture 1 preferred"),
    fig3_fit(E3FULL, "LTMacc * conf3 * hipp", ["LTMacc"], select=fig3_select,
             label="(b) preferred picture in any slot")])
show(R3H)
r = R3H[(R3H.term != "Intercept") & (R3H.outliers.isin(["O-M", "O-M by confidence", "O-C"]))]
print("smallest p of a fixed effect other than the intercept, per reading and outlier rule:")
print(r.groupby(["reading", "outliers"]).p.min())

# %% md
# **Result: ...**
EOF
cd $TMPDIR && source env/bin/activate && python nb/dev.py entries/001187-daume-2024/notebook.py 59 2>&1 | grep -v Warn | grep -v "^  " > out3.txt; grep -n "cell\|paper\|cluster tests" out3.txt | head -30
```

```
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; tail -30 out3.txt; python3 - <<'EOF'
src=open('entries/001187-daume-2024/notebook.py').read().split('# %%')[1:]
for i,c in enumerate(src):
    if 'def fig3_full' in c or 'R3A = ' in c: print(i)
EOF
```

```
Traceback (most recent call last):
NameError: name 'wm_table' is not defined
61
63
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python nb/dev.py entries/001187-daume-2024/notebook.py 46 2>&1 | grep -v Warn | grep -v "^  " > out3.txt; grep -n "^--- cell\|paper\|cluster tests\|Error" out3.txt | head -40
```

```
3:--- cell 47 0.8s
29:--- cell 49 15.7s
63:--- cell 52 9.4s
89:--- cell 55 48.2s
122:--- cell 58 24.7s
127:--- cell 61 1.3s
160:--- cell 63 14.7s
209:--- cell 66 4.8s
258:--- cell 69 13.0s
260:--- cell 72 0.1s
265:paper: high t(82) = 2.16, p = 0.028; low t(68) = -1.38, p = 0.17
266:--- cell 73 0.0s
271:paper: high t(158) = 0.84, p = 0.41; low t(152) = 1.15, p = 0.26
272:--- cell 75 0.0s
281:cluster tests took 4 s
282:--- cell 78 3.7s
299:paper: 0 to 650 ms, cluster p = 0.0042
300:--- cell 79 0.0s
313:--- cell 81 0.0s
351:--- cell 84 33.0s
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -n 127,160p out3.txt | grep -v "none\|by conf"; sed -n 258,320p out3.txt; sed -n 340,395p out3.txt | grep -v "^ *(.).*none"
```

```
--- cell 61 1.3s
with the all-sure session               O-M         Intercept  16.55  8.47 0.050900      316 11408        8
with the all-sure session               O-M            LTMacc  -7.80 11.70 0.504839      316 11408        8
with the all-sure session               O-M             conf3   0.47  4.52 0.917806      316 11408        8
with the all-sure session               O-M      LTMacc:conf3   3.52  5.64 0.532825      316 11408        8
with the all-sure session               O-M              hipp -20.05 14.77 0.174672      316 11408        8
with the all-sure session               O-M       LTMacc:hipp  52.10 21.40 0.014920      316 11408        8
with the all-sure session               O-M        conf3:hipp  18.93  8.04 0.018507      316 11408        8
with the all-sure session               O-M LTMacc:conf3:hipp -25.62 10.23 0.012286      316 11408        8
with the all-sure session               O-C         Intercept  10.26  8.20 0.210632      316 11406        8
with the all-sure session               O-C            LTMacc  -2.21 11.52 0.847672      316 11406        8
with the all-sure session               O-C             conf3   2.49  4.45 0.575987      316 11406        8
with the all-sure session               O-C      LTMacc:conf3   1.16  5.55 0.834402      316 11406        8
with the all-sure session               O-C              hipp -15.49 14.37 0.281066      316 11406        8
with the all-sure session               O-C       LTMacc:hipp  59.96 21.11 0.004511      316 11406        8
with the all-sure session               O-C        conf3:hipp  17.84  7.95 0.024898      316 11406        8
with the all-sure session               O-C LTMacc:conf3:hipp -29.16 10.10 0.003876      316 11406        8
--- cell 63 14.7s
--- cell 69 13.0s
category neurons with rows in the Figure 3 table: hippocampus 100 amygdala 218
[... 98 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python - <<'EOF' 2>/dev/null
import pickle, pandas as pd
pd.set_option('display.width',250)
ns=pickle.load(open('/tmp/claude-1001/ns.pkl','rb'))
r=ns['R3A']; print(r[(r.term.str.contains('hipp'))|(r.term.isin(['LTMacc','conf3','LTMacc:conf3']))][r.outliers!='none'].round(4).to_string(index=False))
r=ns['R3B']; print(r[(r.term!='Intercept')&(r.outliers!='none')].round(4).to_string(index=False))
r=ns['R3BA']; print(r[(r.term!='Intercept')].groupby(['reading','outliers']).p.min())
for k in ['R3G','R3H']:
    r=ns[k]; print(r[(r.term!='Intercept')].groupby(['reading','outliers']).agg(minp=('p','min'),neur=('neurons','first')))
    rr=r[(r.term!='Intercept')&(r.p<0.05)]; print(rr.round(4).to_string(index=False))
EOF
```

```
Exit code 1
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python - <<'EOF' 2>&1 | grep -v Warn
import pickle, pandas as pd
pd.set_option('display.width',250)
ns=pickle.load(open('/tmp/claude-1001/ns.pkl','rb'))
r=ns['R3A']; r=r[r.outliers!='none']; print(r[r.term!='Intercept'].round(4).to_string(index=False))
r=ns['R3B']; print(r[(r.term!='Intercept')&(r.outliers!='none')].round(4).to_string(index=False))
r=ns['R3BA']; print(r[(r.term!='Intercept')].groupby(['reading','outliers']).p.min())
for k in ['R3G','R3H']:
    r=ns[k]; print(r[(r.term!='Intercept')].groupby(['reading','outliers']).agg(minp=('p','min'),neur=('neurons','first')))
    rr=r[(r.term!='Intercept')&(r.p<0.05)]; print(rr.round(4).to_string(index=False))
EOF
```

```
reading          outliers              term     beta      SE      p  neurons     n  removed
                     main               O-M            LTMacc  -5.7579 11.7514 0.6242      310 11228        8
                     main               O-M             conf3   1.2699  4.5412 0.7798      310 11228        8
                     main               O-M      LTMacc:conf3   2.7381  5.6536 0.6282      310 11228        8
                     main               O-M              hipp -16.3815 14.9348 0.2727      310 11228        8
                     main               O-M       LTMacc:hipp  49.1825 21.4634 0.0220      310 11228        8
                     main               O-M        conf3:hipp  17.8443  8.0668 0.0270      310 11228        8
                     main               O-M LTMacc:conf3:hipp -24.4623 10.2473 0.0170      310 11228        8
                     main O-M by confidence            LTMacc   2.3035  9.8841 0.8157      265  9612       53
                     main O-M by confidence             conf3   3.2719  3.8294 0.3929      265  9612       53
                     main O-M by confidence      LTMacc:conf3  -1.2103  4.7741 0.7999      265  9612       53
                     main O-M by confidence              hipp  -2.0681 12.7384 0.8710      265  9612       53
                     main O-M by confidence       LTMacc:hipp  34.9106 18.2570 0.0559      265  9612       53
                     main O-M by confidence        conf3:hipp   7.6014  6.8322 0.2659      265  9612       53
                     main O-M by confidence LTMacc:conf3:hipp -16.6398  8.7059 0.0560      265  9612       53
                     main               O-C            LTMacc   0.1293 11.5672 0.9911      310 11226        8
                     main               O-C             conf3   3.3954  4.4747 0.4480      310 11226        8
                     main               O-C      LTMacc:conf3   0.2574  5.5604 0.9631      310 11226        8
                     main             
[... 92 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001187-daume-2024 && python - <<'EOF'
n=open('notebook.py').read()
old='''R3CD = pd.DataFrame(R3CD)'''
new='''R3CD = pd.DataFrame(R3CD)
F3ALL = fig3_select(F3FULL, keep_noconf=True)
R3CDV = pd.DataFrame([remembered_forgotten(a, l, v, np.random.default_rng(303), data=F3ALL)[0]
                      for a in ("hippocampus", "amygdala") for l in ("high", "low")
                      for v in ("norm", "Hz")])'''
n=n.replace(old,new)
n=n.replace('''print(R3CD[R3CD.area == "hippocampus"].round(4).to_string(index=False))''','''print(R3CD[R3CD.area == "hippocampus"].round(4).to_string(index=False))
print("variant with the all-sure session (as the paper's code keeps it):")
print(R3CDV[R3CDV.area == "hippocampus"].round(4).to_string(index=False))''')
n=n.replace('''print(R3CD[R3CD.area == "amygdala"].round(4).to_string(index=False))''','''print(R3CD[R3CD.area == "amygdala"].round(4).to_string(index=False))
print("variant with the all-sure session:")
print(R3CDV[R3CDV.area == "amygdala"].round(4).to_string(index=False))''')
open('notebook.py','w').write(n)
EOF
cat >> notebook.py <<'EOF'

# %% md
# ## Claim ms-neuron-counts
#
# > 53 of the 351 hippocampal units (15.10%) are memory-selective, 25 of them (47%) firing more to
# > familiar than novel pictures.

# %% tags=claim:ms-neuron-counts
for area in ("hippocampus", "amygdala"):
    k = K[K.area == area]
    print(f"{area}: {int(k.ms.sum())} of {len(k)} MS ({100*k.ms.mean():.2f} %), FS {int((k.ms_type == 'FS').sum())}, "
          f"NS {int((k.ms_type == 'NS').sum())}")
print("expected hippocampus 53 +- 5.3 MS and 25 +- 2.5 FS; amygdala 68 in Table S1 (report)")
print("MS neurons by patient (hippocampus):", K[(K.area == "hippocampus") & K.ms].patient.value_counts().to_dict())

# %% md
# **Result: ...**

# %% md
# ## Claim fig4b-ms-confidence-auc
#
# > Hippocampal memory-selective neurons separate old from new pictures better for
# > high-confidence than for low-confidence decisions (higher ROC AUC), so they carry a
# > memory-strength signal.
#
# Spike counts 0.2 to 1.2 s after LTM picture onset. FS neurons: all true negatives against
# true positives rated 6 (high) and rated 4 or 5 (low); NS neurons: all true positives against
# true negatives rated 1 (high) and 2 or 3 (low); the AUC is oriented so that the preferred
# response above 0.5 is selectivity (sbcat.roc_auc). The all-sure session is left out. Neurons
# kept: (a) at least ten correct novel and ten correct familiar trials, (b) at least ten trials in
# each group compared; a neuron needs trials in both groups of each comparison; then O-M on the
# two AUC values.

# %% tags=claim:fig4b-ms-confidence-auc
MSH = K[(K.area == "hippocampus") & K.ms].copy()
rows = []
for _, u in MSH.iterrows():
    s = S[u.si]
    ltm = s["ltm"]
    c = sbcat.count(s["spikes"][u.ui], ltm.timestamps_PicOnset.values, 0.2, 1.2)
    conf, old = ltm.confidence.values, ltm.new_old.values == 1
    tp, tn = old & (conf >= 4), ~old & (conf <= 3)
    if u.ms_type == "FS":
        fixed, high, low = c[tn], c[tp & (conf == 6)], c[tp & ((conf == 4) | (conf == 5))]
        auc = lambda grp: sbcat.roc_auc(grp, fixed)
    else:
        fixed, high, low = c[tp], c[tn & (conf == 1)], c[tn & ((conf == 2) | (conf == 3))]
        auc = lambda grp: sbcat.roc_auc(grp, fixed)
    ok = len(high) > 0 and len(low) > 0 and np.r_[fixed, high, low].max() > 0
    rows.append(dict(neuron=f"{u.si}_{u.ui}", session=u.session, type=u.ms_type,
                     n_tp=int(tp.sum()), n_tn=int(tn.sum()), n_fixed=len(fixed), n_high=len(high),
                     n_low=len(low), auc_high=auc(high) if ok else np.nan,
                     auc_low=auc(low) if ok else np.nan, noconf=u.si in NOCONF_SI))
AUC = pd.DataFrame(rows)
print("hippocampal MS neurons:", len(AUC), " in the all-sure session:", int(AUC.noconf.sum()),
      " without trials in a compared group:", int(AUC.auc_high.isna().sum()))
rng = np.random.default_rng(401)
R4B = []
for lab, sel in [("(a) >= 10 TN and >= 10 TP", lambda a: (a.n_tp >= 10) & (a.n_tn >= 10)),
                 ("(b) >= 10 in each group compared",
                  lambda a: (a.n_fixed >= 10) & (a.n_high >= 10) & (a.n_low >= 10))]:
    a = AUC[sel(AUC) & ~AUC.noconf & AUC.auc_high.notna()]
    v = a[["auc_high", "auc_low"]].values
    out = np.any(np.abs(v - v.mean()) > 3 * v.std(ddof=1), axis=1)
    a = a[~out]
    t, p, df = sbcat.perm_ttest_paired(a.auc_high, a.auc_low, rng)
    R4B.append(dict(reading=lab, neurons=len(a), outliers=int(out.sum()), FS=int((a.type == "FS").sum()),
                    auc_high=a.auc_high.mean(), auc_low=a.auc_low.mean(), t=t, df=df, p=p))
print(pd.DataFrame(R4B).round(4).to_string(index=False))
print("paper: t(40) = 2.89, p = 0.0039, 41 neurons")
print("AUC range: %.3f to %.3f" % (np.nanmin(AUC[["auc_high", "auc_low"]].values),
                                   np.nanmax(AUC[["auc_high", "auc_low"]].values)))

# %% md
# **Result: ...**

# %% md
# ## Claim fig4c-overlap-chance
#
# > 20 hippocampal neurons are both memory-selective and category neurons, an overlap no greater
# > than chance.

# %% tags=claim:fig4c-overlap-chance
rng = np.random.default_rng(402)
H = K[K.area == "hippocampus"]
obs = int((H.cat & H.ms).sum())
ncat, ms = int(H.cat.sum()), H.ms.values
null = np.array([ms[rng.choice(len(H), ncat, replace=False)].sum() for _ in range(1000)])
p = np.mean(null >= obs)
print(f"overlap {obs} (expected 20 +- 2) of {int(ms.sum())} MS and {ncat} category neurons; "
      f"null mean {null.mean():.2f}, range {null.min()} to {null.max()}; p = {p:.3f} (paper 0.11)")

# %% md
# **Result: ...**

# %% md
# ## Claim fig4d-category-no-memory-signal
#
# > During LTM retrieval, hippocampal category neurons code neither familiarity nor confidence
# > for pictures of their preferred category.
#
# LTM trials showing a picture of the neuron's preferred category; rate 0.2 to 1.2 s after
# picture onset. GLM on correct trials (all-sure session left out): FR ~ conf * old with the
# random intercepts of G. Readings: (D1) confidence coding (a) the code's or (b) certainty;
# (D2) rate (a) spikes per second or (b) normalized to the neuron's mean WM baseline (B1). The
# t-test: per neuron the mean rate of preferred old against preferred new pictures, (D3) (a)
# correct trials or (b) all trials, under both D2 readings, after O-M; paired permutation t-test.

# %%
rows = []
for n in HIPP_CN:
    u = CN.set_index("neuron").loc[n]
    s = S[u.si]
    ltm = s["ltm"]
    sel = (ltm.PicIDs.values // 100) == u.pref
    c = sbcat.count(NEURON_SPIKES[n], ltm.timestamps_PicOnset.values[sel], 0.2, 1.2)
    b = trial_rows(NPT[n]).r_bsl.mean()
    rows.append(pd.DataFrame(dict(neuron=n, patient=u.patient, si=u.si, c=c, Hz=c / 1.0,
                                  norm=sbcat.normalize(c / 1.0, b) if b > 0 else np.nan,
                                  conf=ltm.confidence.values[sel], old=ltm.new_old.values[sel],
                                  acc=ltm.response_accuracy.values[sel])))
L4 = pd.concat(rows, ignore_index=True)
L4["conf_code"] = sbcat.conf3_code(L4.conf)
L4["conf_cert"] = sbcat.conf3_certainty(L4.conf)
print("rows", len(L4), "neurons", L4.neuron.nunique(), " correct", int(L4.acc.sum()),
      " neurons with a zero WM baseline:", L4[L4.norm.isna()].neuron.nunique())

# %% tags=claim:fig4d-category-no-memory-signal
res = []
for d1 in ("conf_code", "conf_cert"):
    for d2 in ("Hz", "norm"):
        d = L4[(L4.acc == 1) & ~L4.si.isin(NOCONF_SI) & L4[d2].notna()].copy()
        d["FR"], d["confv"] = d[d2], d[d1]
        for orule in ("O-M", "O-C", "none"):
            bad = (sbcat.om_remove(d, ["old"], zero_col="c") if orule == "O-M" else
                   sbcat.oc_remove(d) if orule == "O-C" else set())
            m = sbcat.mixedlm(d[~d.neuron.isin(bad)], "confv * old")
            for term, r in m.iterrows():
                res.append(dict(D1=d1, D2=d2, outliers=orule, term=term, beta=r.beta, p=r.p,
                                neurons=m.attrs["neurons"], n=m.attrs["n"]))
R4D = pd.DataFrame(res)
print(R4D.round(4).to_string(index=False))
print("smallest p of a non-intercept effect per reading (O-M):")
print(R4D[(R4D.term != "Intercept") & (R4D.outliers == "O-M")].groupby(["D1", "D2"]).p.min())
rng = np.random.default_rng(403)
res = []
for d3 in ("correct", "all"):
    for d2 in ("Hz", "norm"):
        d = L4[L4[d2].notna()]
        if d3 == "correct":
            d = d[d.acc == 1]
        a = d[d.old == 1].groupby("neuron").agg(v=(d2, "mean"), c=("c", "sum"))
        b = d[d.old == 0].groupby("neuron").agg(v=(d2, "mean"), c=("c", "sum"))
        j = a.join(b, lsuffix="_o", rsuffix="_n", how="inner")
        j = j[(j.c_o > 0) & (j.c_n > 0)]
        v = j[["v_o", "v_n"]].values
        j = j[~np.any(np.abs(v - v.mean()) > 3 * v.std(ddof=1), axis=1)]
        t, p, df = sbcat.perm_ttest_paired(j.v_o, j.v_n, rng)
        res.append(dict(D3=d3, D2=d2, neurons=len(j), old=j.v_o.mean(), new=j.v_n.mean(), t=t, df=df, p=p))
print(pd.DataFrame(res).round(4).to_string(index=False))
print("paper: GLM confidence p = 0.28, familiarity p = 0.71, interaction p = 0.57; t(94) = -0.28, p = 0.78")

# %% md
# **Result: ...**

# %% md
# ## Claims fig4e-fs-strong-maintenance and fig4f-ns-no-effect
#
# > Familiarity-selective hippocampal neurons respond more during LTM retrieval to familiar
# > pictures that were held with strong, compared with weak, maintenance activity of a
# > simultaneously recorded category neuron.
#
# > The response of novelty-selective hippocampal neurons to familiar pictures does not depend on
# > whether the paired category neuron's maintenance activity was strong or weak.
#
# Pairs of a hippocampal MS neuron and a hippocampal category neuron of the same session. Per
# category neuron, its maintenance rates in correct WM trials holding a preferred picture later
# shown in the LTM test, median-split within load 1 and within load 3 (a rate equal to the median
# is weak). The MS neuron's rate 0.2 to 1.2 s after onset of those pictures in the LTM test.
# Readings: (E1) the random intercept within patient is (a) the MS neuron or (b) the pair; (E2)
# (a) all LTM trials of those pictures or (b) those answered old; (E3) a neuron both MS and
# category (a) paired with itself or (b) not; (E4) rate (a) spikes per second or (b) normalized to
# the MS neuron's mean WM baseline.

# %%
MSN = K[(K.area == "hippocampus") & K.ms].copy()
MSN["neuron"] = [f"{a}_{b}" for a, b in zip(MSN.si, MSN.ui)]
prow = []
for _, m in MSN.iterrows():
    sp = S[m.si]["spikes"][m.ui]
    trs = sbcat.add_counts(PT[m.si], sp)
    mbase = trs.groupby("trial").r_bsl.first().mean()
    for n in CN.neuron[(CN.area == "hippocampus") & (CN.si == m.si)]:
        pt = code_rows(NPT[n])
        pt = pt[(pt.acc == 1) & (pt.pref == 1)].copy()
        if len(pt) == 0:
            continue
        med = pt.groupby("load").r_maint.transform("median")
        pt["strong"] = (pt.r_maint > med).astype(int)
        c = sbcat.count(sp, pt.t_ltm.values, 0.2, 1.2)
        prow.append(pd.DataFrame(dict(ms=m.neuron, cat=n, pair=f"{m.neuron}|{n}", patient=m.patient,
                                      type=m.ms_type, self=m.neuron == n, strong=pt.strong.values,
                                      load=pt.load.values, LTMacc=pt.LTMacc.values, c=c, Hz=c / 1.0,
                                      norm=sbcat.normalize(c / 1.0, mbase) if mbase > 0 else np.nan)))
P4 = pd.concat(prow, ignore_index=True)
pairs = P4.drop_duplicates("pair")
print("pairs:", len(pairs), " FS:", int((pairs.type == "FS").sum()), " NS:", int((pairs.type == "NS").sum()),
      " self-pairs:", int(pairs.self.sum()), "(FS", int((pairs.self & (pairs.type == "FS")).sum()), ")")
print("without self-pairs:", int((~pairs.self).sum()), " FS:", int(((pairs.type == "FS") & ~pairs.self).sum()),
      " NS:", int(((pairs.type == "NS") & ~pairs.self).sum()))
print("rows per pair: %d to %d; strong share %.3f" % (P4.groupby("pair").size().min(),
      P4.groupby("pair").size().max(), P4.strong.mean()))
print("expected: 198 +- 20 pairs, 76 +- 8 FS pairs (paper: 122 NS)")


def pair_tests(typ, rng):
    glm, tt = [], []
    for e2 in ("all", "answered old"):
        for e3 in ("with self", "without self"):
            for e4 in ("Hz", "norm"):
                d = P4[(P4.type == typ) & P4[e4].notna()]
                if e2 == "answered old":
                    d = d[d.LTMacc == 1]
                if e3 == "without self":
                    d = d[~d.self]
                d = d.assign(FR=d[e4])
                for e1 in ("MS neuron", "pair"):
                    dd = d.assign(neuron=d.ms if e1 == "MS neuron" else d.pair)
                    bad = sbcat.om_remove(dd.assign(neuron=d.pair), ["strong"], zero_col="c")
                    m = sbcat.mixedlm(dd[~d.pair.isin(bad)], "strong")
                    glm.append(dict(E1=e1, E2=e2, E3=e3, E4=e4, beta=m.loc["strong", "beta"],
                                    p=m.loc["strong", "p"], pairs=d.pair[~d.pair.isin(bad)].nunique(),
                                    n=m.attrs["n"]))
                a = d[d.strong == 1].groupby("pair").agg(v=("FR", "mean"), c=("c", "sum"))
                b = d[d.strong == 0].groupby("pair").agg(v=("FR", "mean"), c=("c", "sum"))
                j = a.join(b, lsuffix="_s", rsuffix="_w", how="inner")
                j = j[(j.c_s > 0) & (j.c_w > 0)]
                v = j[["v_s", "v_w"]].values
                j = j[~np.any(np.abs(v - v.mean()) > 3 * v.std(ddof=1), axis=1)]
                t, p, df = sbcat.perm_ttest_paired(j.v_s, j.v_w, rng)
                tt.append(dict(E2=e2, E3=e3, E4=e4, pairs=len(j), strong=j.v_s.mean(), weak=j.v_w.mean(),
                               t=t, df=df, p=p))
    return pd.DataFrame(glm), pd.DataFrame(tt)


G4E, T4E = pair_tests("FS", np.random.default_rng(404))
G4F, T4F = pair_tests("NS", np.random.default_rng(405))

# %% tags=claim:fig4e-fs-strong-maintenance
print(G4E.round(4).to_string(index=False))
print(T4E.round(4).to_string(index=False))
print("paper: beta = 14.63, p = 0.00139; t(75) = 3.43, p = 0.0003")
print("GLM readings with strong > weak at p < 0.05:", int(((G4E.beta > 0) & (G4E.p < 0.05)).sum()), "of", len(G4E))
print("t-test readings with strong > weak at p < 0.05:", int(((T4E.t > 0) & (T4E.p < 0.05)).sum()), "of", len(T4E))

# %% md
# **Result: ...**

# %% tags=claim:fig4f-ns-no-effect
print(G4F.round(4).to_string(index=False))
print(T4F.round(4).to_string(index=False))
print("paper: beta = 0.09, p = 0.98; t(121) = -0.48, p = 0.64")
print("GLM readings with p < 0.05:", int((G4F.p < 0.05).sum()), "of", len(G4F),
      "; t-test readings with p < 0.05:", int((T4F.p < 0.05).sum()), "of", len(T4F))

# %% md
# **Result: ...**
EOF
cd $TMPDIR && source env/bin/activate && python nb/dev.py entries/001187-daume-2024/notebook.py 46 2>&1 | grep -v Warn > out4.txt; sed -n '/cell 87/,$p' out4.txt
```

```
--- cell 87 11.5s
hippocampus: 53 of 351 MS (15.10 %), FS 26, NS 27
amygdala: 69 of 532 MS (12.97 %), FS 28, NS 41
expected hippocampus 53 +- 5.3 MS and 25 +- 2.5 FS; amygdala 68 in Table S1 (report)
MS neurons by patient (hippocampus): {'20': 7, '27': 7, '10': 3, '23': 3, '37': 3, '39': 3, '17': 2, '2': 2, '21': 2, '22': 2, '24': 2, '28': 2, '30': 2, '32': 2, '5': 2, '6': 2, '11': 1, '14': 1, '18': 1, '19': 1, '33': 1, '34': 1, '4': 1}
--- cell 90 0.0s
hippocampal MS neurons: 53  in the all-sure session: 1  without trials in a compared group: 1
                         reading  neurons  outliers  FS  auc_high  auc_low      t  df      p
       (a) >= 10 TN and >= 10 TP       49         3  25    0.5975   0.5577 3.8667  48 0.0005
(b) >= 10 in each group compared       40         0  21    0.5994   0.5621 3.5480  39 0.0009
paper: t(40) = 2.89, p = 0.0039, 41 neurons
AUC range: 0.230 to 0.853
--- cell 93 0.0s
overlap 19 (expected 20 +- 2) of 53 MS and 102 category neurons; null mean 15.55, range 7 to 26; p = 0.179 (paper 0.11)
--- cell 96 0.0s
rows 3783 neurons 102  correct 2750  neurons with a zero WM baseline: 0
--- cell 99 0.3s
Traceback (most recent call last):
  File "/tmp/claude-1001/nb/dev.py", line 16, in <module>
    exec(code, ns)
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python - <<'EOF' 2>&1 | grep -v Warn | tail -5
import pickle, numpy as np, sys
sys.path.insert(0,'entries/001187-daume-2024'); import sbcat
ns=pickle.load(open('/tmp/claude-1001/ns.pkl','rb'))
L4=ns['L4']; d=L4[(L4.acc==1)].copy(); d['FR']=d.Hz; d['confv']=d.conf_code
import statsmodels.formula.api as smf
md=smf.mixedlm("FR ~ confv * old", d.reset_index(drop=True), groups="patient", re_formula="1", vc_formula={"neuron":"0 + C(neuron)"})
print(md.fit(reml=False,method='bfgs').summary())
EOF
```

```
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
KeyError: 'L4'
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('nb/dev.py').read()
s=s.replace("""    t = time.time()
    exec(code, ns)""","""    t = time.time()
    try:
        exec(code, ns)
    except Exception:
        import traceback; traceback.print_exc(); break""")
open('nb/dev.py','w').write(s)
EOF
source env/bin/activate && python nb/dev.py entries/001187-daume-2024/notebook.py 46 98 2>&1 | tail -2; python - <<'EOF' 2>&1 | grep -v Warn | tail -25
import pickle, numpy as np, sys
sys.path.insert(0,'entries/001187-daume-2024'); import sbcat
ns=pickle.load(open('/tmp/claude-1001/ns.pkl','rb'))
L4=ns['L4']; d=L4[(L4.acc==1)].copy(); d['FR']=d.Hz; d['confv']=d.conf_code
import statsmodels.formula.api as smf
md=smf.mixedlm("FR ~ confv * old", d.reset_index(drop=True), groups="patient", re_formula="1", vc_formula={"neuron":"0 + C(neuron)"})
print(md.fit(reml=False,method='bfgs').summary())
EOF
```

```
overlap 19 (expected 20 +- 2) of 53 MS and 102 category neurons; null mean 15.55, range 7 to 26; p = 0.179 (paper 0.11)
--- cell 96 0.0s
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
KeyError: 'L4'
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python nb/dev.py entries/001187-daume-2024/notebook.py 46 100 2>&1 | grep -v Warn| tail -3; python - <<'EOF' 2>&1 | grep -v Warn | tail -25
import pickle, numpy as np, sys
sys.path.insert(0,'entries/001187-daume-2024'); import sbcat
ns=pickle.load(open('/tmp/claude-1001/ns.pkl','rb'))
L4=ns['L4']; d=L4[(L4.acc==1)].copy(); d['FR']=d.Hz; d['confv']=d.conf_code
import statsmodels.formula.api as smf
md=smf.mixedlm("FR ~ confv * old", d.reset_index(drop=True), groups="patient", re_formula="1", vc_formula={"neuron":"0 + C(neuron)"})
print(md.fit(reml=False,method='bfgs').summary())
EOF
```

```
--- cell 96 0.0s
rows 3783 neurons 102  correct 2750  neurons with a zero WM baseline: 0
--- cell 99 0.3s
    ^
  File "/tmp/claude-1001/env/lib/python3.13/site-packages/scipy/optimize/_dcsrch.py", line 255, in __call__
    phi1 = self.phi(stp)
  File "/tmp/claude-1001/env/lib/python3.13/site-packages/scipy/optimize/_linesearch.py", line 92, in phi
    return f(xk + s*pk, *args)
  File "/tmp/claude-1001/env/lib/python3.13/site-packages/scipy/optimize/_differentiable_functions.py", line 394, in fun
    self._update_fun()
    ~~~~~~~~~~~~~~~~^^
  File "/tmp/claude-1001/env/lib/python3.13/site-packages/scipy/optimize/_differentiable_functions.py", line 362, in _update_fun
    fx = self._wrapped_fun(self.x)
  File "/tmp/claude-1001/env/lib/python3.13/site-packages/scipy/_lib/_util.py", line 544, in __call__
    fx = self.f(np.copy(x), *self.args)
  File "/tmp/claude-1001/env/lib/python3.13/site-packages/statsmodels/base/model.py", line 586, in f
    return -self.loglike(params, *args) / nobs
            ~~~~~~~~~~~~^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/env/lib/python3.13/site-packages/statsmodels/regression/mixed_linear_model.py", line 1625, in loglike
    fe_params, sing = self.get_fe_params(cov_re, vcomp)
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python - <<'EOF' 2>&1 | grep -v Warn | tail -25
import pickle, numpy as np, sys
sys.path.insert(0,'entries/001187-daume-2024'); import sbcat
ns=pickle.load(open('/tmp/claude-1001/ns.pkl','rb'))
L4=ns['L4']; d=L4[(L4.acc==1)].copy(); d['FR']=d.Hz; d['confv']=d.conf_code
print(d.dtypes); print(d[['confv','old']].drop_duplicates().values.tolist())
d['old']=d.old.astype(int)
print(sbcat.mixedlm(d,'confv * old'))
EOF
```

```
neuron           str
patient          str
si             int64
c              int64
Hz           float64
norm         float64
conf           uint8
old            uint8
acc            uint8
conf_code    float64
conf_cert    float64
FR           float64
confv        float64
dtype: object
[[2.0, 1.0], [1.0, 1.0], [3.0, 1.0]]
Traceback (most recent call last):
  File "<stdin>", line 7, in <module>
  File "entries/001187-daume-2024/sbcat.py", line 276, in mixedlm
    res = max(fits, key=lambda r: r.llf)
ValueError: max() iterable argument is empty
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python - <<'EOF'
import pickle, numpy as np
S=pickle.load(open('S.pkl','rb'))
for s in S[:3]+S[20:22]:
    l=s['ltm']; new=l.PicIDs[l.new_old==0].values; old=l.PicIDs[l.new_old==1].values
    print(s['identifier'], sorted(new)[:5], sorted(new)[-5:], np.unique(new//100), np.unique(old//100), len(set(new)&set(old)))
EOF
grep -rn "new_old\|PicIDs" $TMPDIR/code/NWB_SBCAT_NO_analysis/helpers/internal/plotting/plot_raster_NewOld.m | head
```

```
sub-1_ses-2_P54CS [np.uint16(1001), np.uint16(1002), np.uint16(1003), np.uint16(1004), np.uint16(1005)] [np.uint16(1196), np.uint16(1197), np.uint16(1198), np.uint16(1199), np.uint16(1200)] [10 11 12] [1 2 3 4 5] 0
sub-10_ses-1_P68CS [np.uint16(1001), np.uint16(1002), np.uint16(1003), np.uint16(1004), np.uint16(1005)] [np.uint16(1196), np.uint16(1197), np.uint16(1198), np.uint16(1199), np.uint16(1200)] [10 11 12] [1 2 3 4 5] 0
sub-11_ses-1_P69CS [np.uint16(1001), np.uint16(1002), np.uint16(1003), np.uint16(1004), np.uint16(1005)] [np.uint16(1196), np.uint16(1197), np.uint16(1198), np.uint16(1199), np.uint16(1200)] [10 11 12] [1 2 3 4 5] 0
sub-24_ses-2_P090TWH [np.uint16(1001), np.uint16(1002), np.uint16(1003), np.uint16(1004), np.uint16(1005)] [np.uint16(1196), np.uint16(1197), np.uint16(1198), np.uint16(1199), np.uint16(1200)] [10 11 12] [1 2 3 4 5] 0
sub-24_ses-3_P090TWH [np.uint16(1001), np.uint16(1002), np.uint16(1003), np.uint16(1004), np.uint16(1005)] [np.uint16(1196), np.uint16(1197), np.uint16(1198), np.uint16(1199), np.uint16(1200)] [10 11 12] [1 2 3 4 5] 0
21:old = double(nwb.intervals.get('LTM_trials').vectordata.get('new_old').data.load());
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python - <<'EOF'
import h5py, remfile, requests
aid="0af57771-798c-46c0-a5fc-0ef7dbad1597"
r=requests.get(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=False)
f=h5py.File(remfile.File(r.headers['Location'].split('?')[0]),'r')
t=f['stimulus/templates']; print(list(t.keys()))
for k in t.keys():
    g=t[k]; print(k, dict(g.attrs)); ks=list(g.keys()); print(len(ks), ks[:10], ks[-10:])
    if 'order_of_images' in g: print(g['order_of_images'][:5])
p=f['stimulus/presentation/StimulusPresentation']; print(dict(p.attrs)); print(p['data'][:20])
print(list(p.keys()))
for kk in p.keys():
    print(kk, p[kk].attrs.items() if hasattr(p[kk],'attrs') else '')
EOF
```

```
['StimulusTemplates']
StimulusTemplates {'description': 'A collection of images presented to the subject', 'namespace': 'core', 'neurodata_type': 'Images', 'object_id': '70f08149-b358-4eae-8f14-41302e83afe8'}
482 ['image_1001', 'image_1002', 'image_1003', 'image_1004', 'image_1005', 'image_1006', 'image_1007', 'image_1008', 'image_1009', 'image_101'] ['image_548', 'image_549', 'image_550', 'image_551', 'image_552', 'image_553', 'image_554', 'image_555', 'image_999', 'order_of_images']
[<HDF5 object reference> <HDF5 object reference> <HDF5 object reference>
 <HDF5 object reference> <HDF5 object reference>]
{'comments': 'no comments', 'description': "Presentation order of the stimulus. Indexes 'StimulusTemplates'.", 'namespace': 'core', 'neurodata_type': 'IndexSeries', 'object_id': 'f7a8fe58-0c2f-4fa5-81c5-c04d121ca777'}
[ 58   1 226 226  59   2 227 227 115 171   3 115 228   0   0 228 172  60
 229   3]
['data', 'indexed_images', 'timestamps']
data ItemsViewHDF5(<Attributes of HDF5 object at 135031844911792>)
indexed_images ItemsViewHDF5(<Attributes of HDF5 object at 135031844911792>)
timestamps ItemsViewHDF5(<Attributes of HDF5 object at 135031844909952>)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python - <<'EOF'
import h5py, remfile, requests
aid="0af57771-798c-46c0-a5fc-0ef7dbad1597"
r=requests.get(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=False)
f=h5py.File(remfile.File(r.headers['Location'].split('?')[0]),'r')
t=f['stimulus/templates/StimulusTemplates']
for k in ['image_1001','image_1150','image_101','image_205']:
    print(k, dict(t[k].attrs), t[k].shape)
EOF
```

```
image_1001 {'description': 'image_1001', 'namespace': 'core', 'neurodata_type': 'RGBImage', 'object_id': '95f375e5-952e-409c-96bd-850d3b283a14'} (400, 300, 3)
image_1150 {'description': 'image_1150', 'namespace': 'core', 'neurodata_type': 'RGBImage', 'object_id': 'e8168c9a-980c-4b80-82f8-a1be29d2fc40'} (400, 300, 3)
image_101 {'description': 'image_101', 'namespace': 'core', 'neurodata_type': 'RGBImage', 'object_id': '027ddf48-ac56-428d-9fb3-96c40b32f2a2'} (400, 300, 3)
image_205 {'description': 'image_205', 'namespace': 'core', 'neurodata_type': 'RGBImage', 'object_id': 'e56a4b32-ca4c-4049-9404-8d162b86aa9f'} (400, 300, 3)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && source env/bin/activate && python - <<'EOF' 2>&1 | grep -v Warn
import pickle, numpy as np, sys
sys.path.insert(0,'entries/001187-daume-2024'); import sbcat
ns=pickle.load(open('/tmp/claude-1001/ns.pkl','rb'))
K=ns['K']; S=ns['S']
for name,f in [('block40',lambda i:(i-1001)//40+1),('mod5',lambda i:(i-1001)%5+1)]:
    match=tot=0
    for _,u in K[K.cat].iterrows():
        s=S[u.si]; l=s['ltm']; new=l.new_old.values==0
        ids=l.PicIDs.values[new]; c=sbcat.count(s['spikes'][u.ui], l.timestamps_PicOnset.values[new],0.2,1.2)
        g=f(ids); m=[c[g==k].mean() if (g==k).any() else -1 for k in range(1,6)]
        match+= (np.argmax(m)+1)==u.pref; tot+=1
    print(name, match, tot, match/tot)
EOF
```

```
Sun Nov  1 07:57:55 UTC 2026
block40 188 324 0.5802469135802469
mod5 53 324 0.16358024691358025
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/001187-daume-2024 && python - <<'EOF'
n=open('notebook.py').read()
old='''# %%
rows = []
for n in HIPP_CN:
    u = CN.set_index("neuron").loc[n]
    s = S[u.si]
    ltm = s["ltm"]
    sel = (ltm.PicIDs.values // 100) == u.pref'''
new='''# %% md
# The category of a new LTM picture is not in the dataset. New pictures have IDs 1001 to 1200
# (old ones keep their WM IDs, whose leading digit is the category), and their images in the
# files are named only by ID. The cell below asks whether the IDs are in category blocks of 40
# (1001 to 1040 the first category, and so on), from the category neurons' responses: for each
# category neuron, the block with the highest mean response to new pictures is compared with
# its preferred category, against the same for old pictures and for a grouping by ID modulo 5.
# This is an inference from the neural data, not a label, so the claim is not decided on it.

# %%
def new_cat_block(ids):
    return (np.asarray(ids, int) - 1001) // 40 + 1


match = {"old pictures, category from the ID": 0, "new pictures, blocks of 40": 0,
         "new pictures, ID modulo 5": 0}
for _, u in CN.iterrows():
    s = S[u.si]
    l = s["ltm"]
    c = sbcat.count(NEURON_SPIKES[u.neuron], l.timestamps_PicOnset.values, 0.2, 1.2)
    new = l.new_old.values == 0
    ids = l.PicIDs.values.astype(int)
    for lab, sel, g in [("old pictures, category from the ID", ~new, ids // 100),
                        ("new pictures, blocks of 40", new, new_cat_block(ids)),
                        ("new pictures, ID modulo 5", new, (ids - 1001) % 5 + 1)]:
        m = [c[sel & (g == k)].mean() if np.any(sel & (g == k)) else -1 for k in range(1, 6)]
        match[lab] += int(np.argmax(m) + 1 == u.pref)
for k, v in match.items():
    print(f"{k}: the best group is the preferred category for {v} of {len(CN)} category neurons "
          f"({100*v/len(CN):.1f} %; chance 20 %)")
print("new picture IDs:", int(min(s["ltm"].PicIDs[s["ltm"].new_old == 0].min() for s in S)), "to",
      int(max(s["ltm"].PicIDs[s["ltm"].new_old == 0].max() for s in S)))

# %%
rows = []
for n in HIPP_CN:
    u = CN.set_index("neuron").loc[n]
    s = S[u.si]
    ltm = s["ltm"]
    ids = ltm.PicIDs.values.astype(int)
    cat_ltm = np.where(ltm.new_old.values == 1, ids // 100, new_cat_block(ids))
    sel = cat_ltm == u.pref'''
assert old in n
n=n.replace(old,new)
n=n.replace('''# > During LTM retrieval, hippocampal category neurons code neither familiarity nor confidence
# > for pictures of their preferred category.
#''','''# > During LTM retrieval, hippocampal category neurons code neither familiarity nor confidence
# > for pictures of their preferred category.
#
# The new pictures' categories are not in the dataset (see below); the tests here use the
# categories inferred from the ID blocks and are shown as a variant only.
#''')
n=n.replace('''        d["FR"], d["confv"] = d[d2], d[d1]''','''        d["FR"], d["confv"], d["old"] = d[d2], d[d1], d.old.astype(int)''')
open('notebook.py','w').write(n)
EOF
cd $TMPDIR && source env/bin/activate && python nb/dev.py entries/001187-daume-2024/notebook.py 46 2>&1 | grep -v Warn > out4.txt; sed -n '/cell 96/,$p' out4.txt
```

```
--- cell 96 0.0s
old pictures, category from the ID: the best group is the preferred category for 196 of 324 category neurons (60.5 %; chance 20 %)
new pictures, blocks of 40: the best group is the preferred category for 188 of 324 category neurons (58.0 %; chance 20 %)
new pictures, ID modulo 5: the best group is the preferred category for 53 of 324 category neurons (16.4 %; chance 20 %)
new picture IDs: 1001 to 1200
--- cell 100 0.1s
rows 7598 neurons 102  correct 5521  neurons with a zero WM baseline: 0
--- cell 101 0.4s
       D1   D2 outliers      term     beta      p  neurons    n
conf_code   Hz      O-M Intercept   3.5104 0.0000       94 5226
conf_code   Hz      O-M     confv   0.0391 0.6602       94 5226
conf_code   Hz      O-M       old  -0.2081 0.5398       94 5226
conf_code   Hz      O-M confv:old   0.0867 0.5588       94 5226
conf_code   Hz      O-C Intercept   3.0997 0.0000       93 5052
conf_code   Hz      O-C     confv   0.0541 0.5236       93 5052
conf_code   Hz      O-C       old  -0.2844 0.3770       93 5052
conf_code   Hz      O-C confv:old   0.1057 0.4531       93 5052
conf_code   Hz     none Intercept   3.7635 0.0000      100 5408
conf_code   Hz     none     confv   0.0515 0.5636      100 5408
conf_code   Hz     none       old  -0.2644 0.4345      100 5408
[... 118 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -A12 "cell 72\b\|^hippocampus  high\|variant with" out4.txt | head -30; date -u
```

```
--- cell 72 0.3s
       area level value  with_both  with_spikes  n  mean_rem  mean_forg     diff       t  df      p
hippocampus  high  norm         80           73 69   17.4443    10.7162   6.7281  1.1700  68 0.2551
hippocampus  high    Hz         80           73 71    3.1032     2.8906   0.2126  1.7903  70 0.0779
hippocampus   low  norm         72           68 66   25.9737    37.1657 -11.1919 -1.0855  65 0.2987
hippocampus   low    Hz         72           68 67    2.7449     3.0730  -0.3281 -1.6817  66 0.1029
variant with the all-sure session (as the paper's code keeps it):
       area level value  with_both  with_spikes  n  mean_rem  mean_forg     diff       t  df      p
hippocampus  high  norm         82           75 70   14.0844     8.6876   5.3967  1.0087  69 0.3303
hippocampus  high    Hz         82           75 73    3.1118     2.8842   0.2277  1.9608  72 0.0537
hippocampus   low  norm         72           68 66   25.9737    37.1657 -11.1919 -1.0855  65 0.2831
hippocampus   low    Hz         72           68 67    2.7449     3.0730  -0.3281 -1.6817  66 0.1021
paper: high t(82) = 2.16, p = 0.028; low t(68) = -1.38, p = 0.17
--- cell 73 0.0s
    area level value  with_both  with_spikes   n  mean_rem  mean_forg    diff       t  df      p
amygdala  high  norm        161          150 146   14.8278    15.7999 -0.9722 -0.2145 145 0.8454
amygdala  high    Hz        161          150 147    2.3857     2.4261 -0.0404 -0.5002 146 0.6370
amygdala   low  norm        158          150 146   18.8811    13.7053  5.1758  1.0248 145 0.2999
amygdala   low    Hz        158          150 146    2.4178     2.4758 -0.0580 -0.6681 145 0.5090
variant with the all-sure session:
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001187-daume-2024 && grep -c "Result: \.\.\." notebook.py; grep -n "tags=claim" notebook.py | awk -F'claim:' '{print $2}' | tr '\n' ' '
```

```
29
sessions-and-neurons table-s1-counts behaviour-overall-accuracy fig1c-wm-accuracy-load fig1d-wm-rt-load fig1e-ltm-confidence-accuracy ltm-rt-confidence fig1f-ltm-load fig1g-ltm-probe category-neuron-counts fig2b-hippocampus-persistent fig2c-hippocampus-correct-load fig2e-amygdala-persistent fig2f-amygdala-load-not-accuracy fig3a-area-interactions fig3b-hippocampus-predicts-ltm fig3b-amygdala-no-prediction fig3c-hippocampus-high-confidence fig3d-amygdala-no-difference fig3e-early-delay-cluster fig3f-amygdala-no-cluster fig3g-nonpreferred-no-effect fig3h-encoding-no-effect ms-neuron-counts fig4b-ms-confidence-auc fig4c-overlap-chance fig4d-category-no-memory-signal fig4e-fs-strong-maintenance fig4f-ns-no-effect
```

**Agent calls Bash**

```bash
cd  && python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
o=s['properties']['outcomes']['items']; print(json.dumps(o,indent=0)[:3000])
print(list(s['properties'].keys()))
print(json.dumps(s['properties'].get('verifications',{}),indent=0)[:800])
"; grep -n "claim:" tools/entry.py | head
```

```
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
],
"description": "Describes the result, not the method: whether the effect the claim states was found. Differences in method from the paper go in `deviations`."
[... 189 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001187-daume-2024 && cat > $TMPDIR/concl.py <<'PYEOF'
C = [
# sessions-and-neurons
"**Result: reproduced.** The dandiset holds 46 sessions and 950 units; the rate filter removes 67 (7.1%) and leaves 351 hippocampal and 532 amygdala units, as the paper states. The recorded counts of Table S1 sum to 973.",
# table-s1
"**Result: partially reproduced.** 42 of the 46 sessions match Table S1's recorded counts before the rate filter (21 after it). Four differ: P1809jh (1 hippocampal unit against 6), P61cs_2 (1 against 2), P68cs (7 amygdala units against 17) and P82cs (17 against 24); the 23 missing units are the difference between Table S1's 973 and the 950 of the text. The session match is confirmed by the accuracies, which differ from Table S1 by at most 0.18 points (WM) and 1.52 points (LTM, in sessions with incomplete LTM tables).",
# behaviour
"**Result: reproduced.** Mean WM accuracy 93.33% (SD 7.60), LTM accuracy 70.32% (SD 9.89) and d' 1.189 (SD 0.620) are within tolerance, and both accuracies exceed 50% at the smallest p a 10,000-permutation test gives (below 0.0001).",
# 1c
"**Result: reproduced.** Load 1 accuracy 95.09% against 91.58% for load 3, t(45) = 4.91 (paper 4.89), permutation p below 0.0001.",
# 1d
"**Result: partially reproduced.** With response times above 5 s set to missing, load 1 is faster (1.393 against 1.525 s), t(45) = -4.28 as in the paper (-4.29), but the permutation p is 0.0003, not below 0.0001 as the criterion requires for a full reproduction. With all response times (variant), there is no difference (t = 0.20).",
# 1e
"**Result: reproduced.** High-confidence accuracy 77.31% against 61.40% (pooled low, t(44) = 8.51) or 62.48% (averaged, t(44) = 7.34), both with permutation p below 0.0001, in 45 sessions.",
# ltm-rt
"**Result: reproduced.** With response times above 5 s set to missing (reading b), the means are 1.838 s (high) and 2.618 s (pooled low) or 2.659 s (averaged low), within tolerance, with t(44) = -11.37 or -11.22 (paper -11.13) and p below 0.0001. With all response times (reading a), the means are 2.205 and 3.565 s, outside tolerance, though high is still faster (p below 0.0001).",
# 1f
"**Result: reproduced.** Hit rate 68.59% for load 1 pictures against 65.77% for load 3, t(45) = 2.65, p = 0.0097 (paper t = 2.42, p = 0.018).",
# 1g
"**Result: reproduced.** Hit rate 72.10% for pictures shown twice against 63.99% for pictures shown once, t(45) = 6.80, p below 0.0001.",
# category counts
"**Result: reproduced.** 102 hippocampal (29.06%) and 222 amygdala (41.73%) category neurons, within 10% of 104 and 220.",
# 2b
"**Result: partially reproduced.** Under every reading with the Methods outlier rule (O-M) both terms are positive at p < 0.05 but one beta is outside tolerance: one row per trial with baseline B1 gives intercept 17.29 (p = 0.0008, within 17.86 +- 1.79) and preferred 7.79 (p = 0.0008, outside 12.47 +- 1.25); with B2, 22.38 and 11.86; with the code's rows, 21.93 and 7.06 (B1) or 27.84 and 6.18 (B2). The code's outlier rule (O-C) with one row per trial and B1 gives 19.39 and 13.12.",
# 2c
"**Result: not reproduced (resting on an assumption).** With one row per trial, main effects only and baseline B1 (the adopted reading), O-M removes 14 of 102 neurons and neither effect is significant (accuracy 6.88, p = 0.26; load 4.96, p = 0.14). With B2, load is significant (9.19, p = 0.030) and accuracy is not (10.76, p = 0.16), which the criterion counts as partial; with the interaction (reading b) neither main effect is significant under any baseline. The code's outlier rule (O-C), a variant, gives accuracy 18.68 (p = 0.028) and load 13.63 (p = 0.0034), the paper's pattern.",
# 2e
"**Result: partially reproduced.** Under every O-M reading the intercept and the preferred effect are positive at p < 0.05, and the preferred beta is below tolerance (4.28 to 5.44 against 6.91 +- 0.69); the intercept is within tolerance with one row per trial (10.06 with B1, 9.46 with B2).",
# 2f
"**Result: partially reproduced.** The accuracy effect is absent under every reading (p from 0.056 to 0.11 with O-M; beta -8.90 to -9.95, paper -6.13). The load effect is positive at p < 0.05 with main effects only (10.77 with B1, 8.95 with B2) but below the tolerance of 12.309 +- 1.231, and with the interaction it is not significant (p = 0.55 and 0.61).",
# 3a
"**Result: partially reproduced (resting on an assumption).** With O-M, its conditions the levels of LTM accuracy (the adopted reading), the three interactions with area are significant with the paper's signs (LTM accuracy x area 49.18, p = 0.022; confidence x area 17.84, p = 0.027; three-way -24.46, p = 0.017) and no main effect or the accuracy x confidence term is (smallest p 0.27); two betas are outside tolerance. If confidence levels are also conditions, 53 neurons are removed and the interactions miss significance (p = 0.056, 0.27, 0.056). The code's rule (O-C, variant) gives 56.61, 16.60 and -27.83, all within tolerance, and with the all-sure session kept, as the code does, 59.96, 17.84 and -29.16.",
# 3b hipp
"**Result: partially reproduced.** Under every O-M reading, confidence, LTM accuracy and their interaction are significant with the paper's signs (for example 19.18, 43.57 and -21.80, p = 0.008, 0.026 and 0.019, outliers over both areas), with the confidence beta within tolerance and the other two outside it. The code's rule (O-C) gives 21.25, 67.37 and -30.69, all within tolerance.",
# 3b amyg
"**Result: reproduced.** No effect reaches p < 0.05 in the amygdala under any reading or outlier rule (smallest p 0.34).",
# 3c
"**Result: not reproduced.** In the hippocampus, remembered and forgotten do not differ with high confidence under either reading (normalized: t(68) = 1.17, p = 0.26; spikes per second: t(70) = 1.79, p = 0.078), nor with low confidence (p = 0.30 and 0.10). Keeping the all-sure session, as the code does, gives p = 0.33 and 0.054. 69 to 73 neurons enter the high-confidence test against 83 in the paper.",
# 3d
"**Result: reproduced.** In the amygdala no comparison has p < 0.05 (high p = 0.85 and 0.64, low p = 0.30 and 0.51; 146 to 147 neurons).",
# 3e
"**Result: partially reproduced.** Under every reading a cluster with remembered above forgotten has cluster p < 0.025, but it lies from about 0.875 to 1.05 s (p = 0.0001 to 0.0196), not from 0 to 650 ms. Clusters starting at maintenance onset do not reach significance (smallest p 0.061, 0 to 0.125 s, spikes per second, 200 ms windows).",
# 3f
"**Result: reproduced.** In the amygdala no cluster has p < 0.025 under any reading (smallest cluster p 0.43).",
# 3g
"**Result: reproduced (resting on an assumption).** With O-M, its conditions the levels of LTM accuracy (the adopted reading), no fixed effect other than the intercept has p < 0.05 in either set of rows (smallest p 0.071 and 0.23), nor with O-C (0.067 and 0.11). If confidence levels are also conditions, the area main effect reaches p = 0.035 in reading (a).",
# 3h
"**Result: not reproduced (resting on an assumption).** With O-M, its conditions the levels of LTM accuracy (the adopted reading), an effect reaches p < 0.05 under both readings: the area main effect in (a) (56.58, p = 0.048) and the LTM accuracy x confidence interaction in (b) (15.63, p = 0.027). If confidence levels are also conditions (smallest p 0.0505 and 0.41), or with the code's rule (0.35 and 0.074), no effect reaches p < 0.05. No reading shows an effect of LTM accuracy or confidence alone.",
# ms counts
"**Result: reproduced.** 53 of 351 hippocampal units are memory-selective (15.10%), 26 of them familiarity-selective, within tolerance of 53 and 25.",
# 4b
"**Result: reproduced.** The AUC is higher for high than low confidence under both readings: 0.5975 against 0.5577 (t(48) = 3.87, p = 0.0005, 49 neurons) and 0.5994 against 0.5621 (t(39) = 3.55, p = 0.0009, 40 neurons; paper 41).",
# 4c
"**Result: reproduced.** 19 neurons are both memory-selective and category neurons (expected 20 +- 2); the null overlap has mean 15.55 and p = 0.179, not below 0.05.",
# 4d
"**Result: blocked (metadata insufficient).** The category of the new LTM pictures is not in the dataset, so preferred new pictures cannot be selected. Under categories inferred from ID blocks of 40, shown as a variant that decides nothing, no GLM effect (smallest p 0.079) and no old against new t-test (smallest p 0.22) reaches p < 0.05, as the paper reports.",
# 4e
"**Result: not reproduced.** In familiarity-selective pairs, MS responses after strong maintenance are not higher than after weak under any reading: the GLM betas are negative (-0.15 to -0.19 Hz, -6.5 to -9.4 normalized; p 0.059 to 0.45), and so are the paired t-tests (t from -1.06 to -1.60, p 0.11 to 0.33). There are 197 pairs (expected 198 +- 20) and 84 FS pairs (expected 76 +- 8).",
# 4f
"**Result: reproduced (resting on an assumption).** Under the adopted reading (all trials of the old pictures, self-pairs kept, spikes per second) neither test finds an effect in novelty-selective pairs (GLM p = 0.90 and 0.85; t(106) = -1.03, p = 0.31). No GLM reading reaches p < 0.05; one t-test reading does (pictures answered old, self-pairs dropped, spikes per second: t(81) = 2.04, p = 0.040).",
]
src = open("notebook.py").read()
parts = src.split("**Result: ...**")
assert len(parts) == len(C) + 1, len(parts)
out = parts[0]
for c, p in zip(C, parts[1:]):
    out += c + p
open("notebook.py", "w").write(out)
PYEOF
python $TMPDIR/concl.py && grep -c "Result: \.\.\." notebook.py; grep -n "Result: " notebook.py | awk -F: '{print $1}' | head -3
```

```
0
146
182
262
```

**Agent calls Bash**

```bash
python - <<'EOF'
n=open('notebook.py').read()
reps=[("O-M removes 14 of 102 neurons and neither","88 of 102 neurons remain after O-M and neither"),
("the intercept is within tolerance with one row per trial (10.06 with B1, 9.46 with B2).","the intercept is within tolerance in three of the four (10.06, 9.46 and 10.32; 11.99 with the code's rows and B1)."),
("with the confidence beta within tolerance and the other two outside it.","with the confidence beta within tolerance in this reading only and the other two betas outside tolerance in every O-M reading."),
("the GLM betas are negative (-0.15 to -0.19 Hz, -6.5 to -9.4 normalized; p 0.059 to 0.45), and so are the paired t-tests (t from -1.06 to -1.60, p 0.11 to 0.33)","the GLM betas are negative (-0.14 to -0.19 Hz, -6.5 to -9.4 normalized; p 0.059 to 0.45), and so are the paired t-tests (t from -1.00 to -1.60, p 0.11 to 0.33)")]
for a,b in reps:
    assert a in n, a
    n=n.replace(a,b)
open('notebook.py','w').write(n)
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
python - <<'EOF'
n=open('notebook.py').read()
header='''# # Reproducing Daume et al. (2024) from dandiset 001187
#
# Paper: Daume, Kaminski, Salimpour, Gomez Palacio Schjetnan, Anderson, Valiante, Mamelak and
# Rutishauser (2024), "Persistent activity during working memory maintenance predicts long-term
# memory formation in the human hippocampus", Neuron 112, 3957-3968,
# doi:10.1016/j.neuron.2024.09.013.
#
# Dataset: DANDI:001187, version 0.240904.2347 (doi:10.48324/dandi.001187/0.240904.2347). This is
# the version the paper cites (Data and Code Availability; key resources table), and it is the
# only published version; the draft has the same 46 assets and size.
#
# Claims: `claims/001187/10.1016-j.neuron.2024.09.013.yaml`, written from the accepted author
# manuscript in PubMed Central (PMC11624075) with its supplement (Figures S1 to S4, Table S1),
# and checked by a second reader. Method details the claims file lacks are taken from the paper
# or its code (github.com/rutishauserlab/SBCAT-NO-release-NWB, commit 6d07204) and cited where
# used, here and in `sbcat.py`.
#
# | Claim | Tested or blocked |
# |---|---|
# | sessions-and-neurons, table-s1-counts | tested |
# | behaviour-overall-accuracy, fig1c to fig1g, ltm-rt-confidence | tested |
# | category-neuron-counts, fig2b, fig2c, fig2e, fig2f | tested |
# | fig3a to fig3h (nine claims) | tested |
# | ms-neuron-counts, fig4b, fig4c, fig4e, fig4f | tested |
# | fig4d-category-no-memory-signal | blocked: the new LTM pictures have no category in the dataset |
#
# Every number below is computed from the streamed files. Seeds are fixed, one generator per
# claim section.'''
n=n.replace('''# # Reproducing Daume et al. (2024) from dandiset 001187
#
# HEADER''',header)
n=n.replace('''import matplotlib.pyplot as plt
''','')
open('notebook.py','w').write(n)
EOF
cat >> notebook.py <<'EOF'

# %% md
# ## Summary
#
# | Claim | Outcome |
# |---|---|
# | sessions-and-neurons | reproduced |
# | table-s1-counts | partially reproduced (42 of 46 sessions) |
# | behaviour-overall-accuracy | reproduced |
# | fig1c-wm-accuracy-load | reproduced |
# | fig1d-wm-rt-load | partially reproduced (p = 0.0003, not below 0.0001) |
# | fig1e-ltm-confidence-accuracy | reproduced |
# | ltm-rt-confidence | reproduced |
# | fig1f-ltm-load | reproduced |
# | fig1g-ltm-probe | reproduced |
# | category-neuron-counts | reproduced |
# | fig2b-hippocampus-persistent | partially reproduced |
# | fig2c-hippocampus-correct-load | not reproduced (assumed) |
# | fig2e-amygdala-persistent | partially reproduced |
# | fig2f-amygdala-load-not-accuracy | partially reproduced |
# | fig3a-area-interactions | partially reproduced (assumed) |
# | fig3b-hippocampus-predicts-ltm | partially reproduced |
# | fig3b-amygdala-no-prediction | reproduced |
# | fig3c-hippocampus-high-confidence | not reproduced |
# | fig3d-amygdala-no-difference | reproduced |
# | fig3e-early-delay-cluster | partially reproduced |
# | fig3f-amygdala-no-cluster | reproduced |
# | fig3g-nonpreferred-no-effect | reproduced (assumed) |
# | fig3h-encoding-no-effect | not reproduced (assumed) |
# | ms-neuron-counts | reproduced |
# | fig4b-ms-confidence-auc | reproduced |
# | fig4c-overlap-chance | reproduced |
# | fig4d-category-no-memory-signal | blocked, metadata insufficient |
# | fig4e-fs-strong-maintenance | not reproduced |
# | fig4f-ns-no-effect | reproduced (assumed) |
#
# A failure to reproduce here may be a failure of this attempt, not of the paper: see the
# reasoning and the differences from the paper's method.
#
# How the analysis differs from the paper's. The claims file makes the outlier rule of the
# Methods (O-M) the main reading and the code's rule (O-C, NWB_computeGLM.m) a variant. For the
# GLMs the Methods do not say what the "tested conditions" are; the conditions are taken as the
# levels of the model's categorical factors (confidence enters as a continuous variable), with
# confidence levels as further conditions shown as a second reading. With O-C, the GLMs of
# Figures 2c, 3a and 3b give the paper's betas within tolerance, which O-M does not. The
# session whose ratings are all sure is left out of confidence analyses, as the paper says; the
# code keeps it, shown as a variant. Mixed models are fitted by maximum likelihood in
# statsmodels, not MATLAB's fitglme. Permutation p-values follow statcond's formula.
#
# What was found about the dataset. The 46 sessions, 950 units and the 351 and 532 units after
# the rate filter match the paper. Table S1 lists 23 more units in four sessions. All files give
# Cedars-Sinai as the institution, though the identifiers (TWH, JHU) and the paper place 18
# sessions at Toronto Western and Johns Hopkins. Eight sessions have fewer than 400 LTM trials
# (161 to 399) and one has 139 WM trials. One LTM trial has confidence 7, outside the documented
# 1 to 6. The new LTM pictures (IDs 1001 to 1200) carry no category; the neural responses
# suggest blocks of 40 per category. Five units have spike times out of order in the files
# (sorted here before analysis). The confidence coding (1 to 3 new, 4 to 6 old) is not
# documented but agrees with the accuracy column in every trial.

# %%
print("notebook run time %.1f min" % ((time.time() - T0) / 60))
EOF
echo
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
python - <<'EOF'
n=open('notebook.py').read()
old='''print("identifier suffixes:", sorted({s.split("_")[-1].rstrip("0123456789").lstrip("P0123456789") or s
                                       for s in SES.session}))'''
new='''print("sessions by identifier suffix (site):",
      pd.Series([s.split("_")[-1].lstrip("P0123456789") for s in SES.session]).value_counts().to_dict())'''
assert old in n; n=n.replace(old,new)
n=n.replace("place 18\n# sessions at Toronto","place 20\n# sessions at Toronto")
old='''# %% md
# ## Claim sessions-and-neurons'''
new='''# %% md
# Checks of the description against the data, from the outputs above. The confidence column
# is described as 1 to 6 with no coding; the accuracy column agrees in every trial with 1 to 3
# meaning "new" and 4 to 6 "old" (shown). One trial has the value 7 (shown); it counts as "old"
# under that coding, which agrees with its accuracy. The LTM table's load is 0 for new
# pictures and num_times_shown 0 for new pictures (shown). Response times are in seconds
# (0.135 to 56 s in WM; up to 130 s in LTM, where the picture stays until a response). The
# maintenance period lasts 2.53 to 3.20 s (the Methods say 2.55 to 2.85 s) and starts at the end
# of the last picture. Picture 1 lasts 1.57 to 2.04 s where the Methods say 2 s. The files
# name Cedars-Sinai for every session, which the identifiers contradict (shown). No session
# pair shares its trial timing or spike counts, so no recording is deposited twice; the 45
# sessions sharing one picture sequence are the same task version. The same units are taken
# to be recorded in both tasks of a session (one sorting per session, as the Methods say). The
# clock check after the category selection supports a shared clock of spikes and trial tables
# where sessions have enough units.

# %% md
# ## Claim sessions-and-neurons'''
assert old in n; n=n.replace(old,new,1)
open('notebook.py','w').write(n)
EOF
cat > requirements.in <<'EOF'
h5py
numpy
pandas
remfile
requests
scipy
statsmodels
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: 001187-daume-2024
type: reproduction
title: Working memory maintenance and long-term memory in human hippocampus (Daume et al. 2024)
description: Tests the findings of Daume et al. (2024) on dandiset 001187, which holds the spike
  times of 950 units recorded in the hippocampus and amygdala of 39 epilepsy patients over 46
  sessions of a Sternberg working memory task and a later recognition memory test. It covers
  the behaviour, the selection of category and memory-selective neurons, the mixed-effects
  models relating maintenance activity to later memory, and the pairing of memory-selective with
  category neurons.
license: Apache-2.0
notebooks:
- path: reproduce_daume_2024.ipynb
  title: Reproducing Daume et al. (2024) from dandiset 001187
  runtime_minutes: 10
helpers:
- sbcat.py
related:
- id: dandi:001187/0.240904.2347
  relation: uses_data
- id: doi:10.1016/j.neuron.2024.09.013
  relation: reproduces
EOF
rm -f notebook.ipynb; source $TMPDIR/env/bin/activate && python $TMPDIR/nb/build.py notebook.py reproduce_daume_2024.ipynb && ls
```

```
__pycache__
entry.yaml
notebook.py
reproduce_daume_2024.ipynb
requirements.in
sbcat.py
```

**Agent calls Bash**

```bash
mv notebook.py $TMPDIR/nb/notebook.py && rm -rf __pycache__ && cd  && date -u && timeout 600 python tools/entry.py lock entries/001187-daume-2024 2>&1 | tail -5 && python tools/entry.py check entries/001187-daume-2024 2>&1 | tail -20
```

```
Sun Nov  1 08:03:47 UTC 2026
wrote entries/001187-daume-2024/requirements.lock.txt
0 error(s)
```

**Agent calls Bash**

```bash
time python tools/entry.py all entries/001187-daume-2024 2>&1 | tail -20
```

```
Installed kernelspec registry-001187-daume-2024 in executed/001187-daume-2024/.venv/share/jupyter/kernels/registry-001187-daume-2024
0 error(s)
pass  reproduce_daume_2024.ipynb  (416 s)

real	7m0.868s
user	12m48.262s
sys	0m14.625s
```

**Agent calls Bash**

```bash
ls executed/001187-daume-2024/ && python - <<'EOF' > $TMPDIR/exec_out.txt
import nbformat
nb=nbformat.read('executed/001187-daume-2024/reproduce_daume_2024.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    tags=c.metadata.get('tags',[])
    txt=''.join(o.get('text','') if o.output_type=='stream' else str(o.get('data',{}).get('text/plain','')) + o.get('evalue','') for o in c.outputs)
    print(f'=== cell {i} {tags}'); print(txt)
EOF
wc -l $TMPDIR/exec_out.txt; grep -n "Error\|Traceback" $TMPDIR/exec_out.txt | head
```

```
reproduce_daume_2024.ipynb
result.json
1066 /tmp/claude-1001/exec_out.txt
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -n '/cell 3 /,/cell 9 /p' exec_out.txt | grep -v "^[0-9]* *sub-" | head -60
```

```
=== cell 3 []
46 sessions loaded in 60 s

=== cell 4 ['sanity']
                  session subject ses   age sex                  institution  units  hipp  amyg  wm_trials  load1  load3  ltm_trials  ltm_old conf_values  acc_mismatch  unsorted_units variant

sessions 46 subjects 39 units 950 hippocampus 380 amygdala 570
locations: [np.str_('amygdala_left'), np.str_('amygdala_right'), np.str_('hippocampus_left'), np.str_('hippocampus_right')]
institutions in the files: ['Cedars-Sinai Medical Center']
sessions by identifier suffix (site): {'CS': 26, 'TWH': 14, 'JHU': 6}
sessions with fewer than 400 LTM trials: [['sub-12_ses-2_P70CS', 161, 78], ['sub-16_ses-1_P76CS', 395, 197], ['sub-17_ses-1_P77CS', 390, 197], ['sub-18_ses-1_P78CS', 384, 190], ['sub-22_ses-1_P088TWH', 257, 127], ['sub-23_ses-1_P089TWH', 187, 89], ['sub-26_ses-1_P096TWH', 228, 115], ['sub-28_ses-1_P103TWH', 399, 199]]
sessions with fewer than 140 WM trials: [['sub-11_ses-1_P69CS', 139]]
confidence values outside 1 to 6: [('sub-24_ses-2_P090TWH', 7, 1)]
trials whose accuracy disagrees with 'old' = confidence 4 to 6: 0
units with unsorted spike times: 5 [('sub-13_ses-1_P71CS', [1, 2]), ('sub-2_ses-2_P55CS', [19, 29]), ('sub-24_ses-2_P090TWH', [10])]

WM response time (s): 0.135 to 56.289, median 1.265
LTM response time (s): 0.001 to 129.615, median 1.859
maintenance length (probe - maintenance onset, s): 2.530 to 3.203
encoding picture 1 duration (s): 1.567 to 2.036
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -n "hippocampus: \|amygdala: \|overlap\|pairs: \|FS: \|t(45)\|t(44)\|matching\|mean 9\|d':" exec_out.txt | head -40; sed -n '/claim:fig2b/,/claim:fig2c/p' exec_out.txt | grep "O-M\|O-C" | head -12
```

```
96:sessions matching before the filter: 42 after: 21 under either: 42 of 46
147:wm_acc: mean 93.33 % (SD 7.60), expected 93.3 +- 1.1, within: True; against 50%: t(45) = 38.67, perm p = 0.000100
148:ltm_acc: mean 70.32 % (SD 9.89), expected 70.3 +- 1.4, within: True; against 50%: t(45) = 13.93, perm p = 0.000100
149:d': mean 1.189 (SD 0.620), expected 1.19 +- 0.09, within: True; sessions with a hit or FA rate of 0 or 1 (1/(2N) applied): 0
153:load 1 95.09 %, load 3 91.58 %; t(45) = 4.91 (paper 4.89), perm p = 0.000100; sessions with load 1 higher: 32, equal 8
156:RT > 5 s missing (main): load 1 1.393 s, load 3 1.525 s; t(45) = -4.28 (paper -4.29), perm p = 0.000300
157:all RTs (variant): load 1 1.706 s, load 3 1.689 s; t(45) = 0.20 (paper -4.29), perm p = 0.858614
161:(a) unsure and guessing pooled: high 77.31 %, low 61.40 %; t(44) = 8.51 (paper 8.66), perm p = 0.000100
162:(b) mean of unsure and guessing accuracy: high 77.31 %, low 62.48 %; t(44) = 7.34 (paper 8.66), perm p = 0.000100
165:(a) all RTs, low pooled: high 2.205 s (SD 1.13; 1.83 +- 0.085: False), low 3.565 s (SD 1.98; 2.62 +- 0.098: False); t(44) = -7.30 (paper -11.13), perm p = 0.000100
166:(a) all RTs, low averaged: high 2.205 s (SD 1.13; 1.83 +- 0.085: False), low 3.655 s (SD 2.03; 2.62 +- 0.098: False); t(44) = -7.58 (paper -11.13), perm p = 0.000100
167:(b) RT > 5 s missing, low pooled: high 1.838 s (SD 0.58; 1.83 +- 0.085: True), low 2.618 s (SD 0.65; 2.62 +- 0.098: True); t(44) = -11.37 (paper -11.13), perm p = 0.000100
168:(b) RT > 5 s missing, low averaged: high 1.838 s (SD 0.58; 1.83 +- 0.085: True), low 2.659 s (SD 0.65; 2.62 +- 0.098: True); t(44) = -11.22 (paper -11.13), perm p = 0.000100
171:hit rate load 1 68.59 %, load 3 65.77 %; t(45) = 2.65 (paper 2.42), perm p = 0.0097 (paper 0.018)
174:hit rate shown twice 72.10 %, once 63.99 %; t(45) = 6.80 (paper 7.25), perm p = 0.000100
242:hippocampus: 102 of 351 (29.06 %), expected 104 +- 10.4: True
244:amygdala: 222 of 532 (41.73 %), expected 22
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && for pat in "main               O-M       LTMacc:hipp" "(a) outliers over both areas               O-M       LTMacc" "hippocampus  high  norm" "rem > forg    0.875\|rem > forg    0.900\|rem > forg    0.925" "answered old without self   Hz     82" "(a) >= 10 TN" "(b) >= 10 in" "88 4953\|acc   6.8"; do echo "## $pat"; grep -h -- "$pat" exec_out.txt | head -4; done
```

```
## main               O-M       LTMacc:hipp
                     main               O-M       LTMacc:hipp  49.18 21.46 0.021956      310 11228        8
## (a) outliers over both areas               O-M       LTMacc
 (a) outliers over both areas               O-M       LTMacc  43.57 19.58 0.026107       97 3375        8
 (a) outliers over both areas               O-M       LTMacc  -5.68 11.27 0.614290      213 7853        8
## hippocampus  high  norm
hippocampus  high  norm         80           73 69   17.4443    10.7162   6.7281  1.1700  68 0.2551
hippocampus  high  norm         82           75 70   14.0844     8.6876   5.3967  1.0087  69 0.3303
## rem > forg    0.875\|rem > forg    0.900\|rem > forg    0.925
hippocampus  norm (a) 200/25 ms       69 rem > forg    0.900  1.050      20.1614 0.0196
hippocampus  norm     (b) 50 ms       69 rem > forg    0.875  1.025      11.1504 0.0001
hippocampus    Hz (a) 200/25 ms       71 rem > forg    0.875  1.025      23.0593 0.0187
hippocampus    Hz     (b) 50 ms       71 rem > forg    0.925  0.975       6.4498 0.0026
## answered old without self   Hz     82
answered old without self   Hz     82  1.6962  1.5375  2.0368  81 0.0395
## (a) >= 10 TN
       (a) >= 10 TN and >= 10 TP       49         3  25    0.5975   0.5577 3.8667  48 0.0005
## (b) >= 10 in
(b) >= 10 in each group compared       40         0  21    0.5994   0.5621 3.5480  39 0.0009
## 88 4953\|acc   6.8
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && sed -i 's/perm p = {p:.6f}/perm p = {p:.3g} (below 0.0001: {p < 1e-4})/g' notebook.py && grep -c "below 0.0001: {p" notebook.py && python - <<'EOF'
n=open('notebook.py').read()
n=n.replace('print("smallest p a 10,000-permutation test can give: %.5f" % (1 / 10001))','print("smallest p a 10,000-permutation test gives here: %.3g" % (2 * 0.5 / 10001))')
open('notebook.py','w').write(n)
EOF
grep -n "smallest p a" notebook.py
```

```
6
299:print("smallest p a 10,000-permutation test gives here: %.3g" % (2 * 0.5 / 10001))
302:# **Result: reproduced.** Mean WM accuracy 93.33% (SD 7.60), LTM accuracy 70.32% (SD 9.89) and d' 1.189 (SD 0.620) are within tolerance, and both accuracies exceed 50% at the smallest p a 10,000-permutation test gives (below 0.0001).
Shell cwd was reset to
```

**Agent calls Bash**

```bash
ls questions | head; f=$(ls questions/*.yaml | head -1); cat $f | head -40; ls questions/001187.yaml 2>&1
```

```
Exit code 2
000005.yaml
000006.yaml
000008.yaml
000009.yaml
000010.yaml
000011.yaml
000013.yaml
000015.yaml
000019.yaml
000023.yaml
dandiset: "000005"
paper: doi:10.1038/nn.4412
questions:
- claim: fs-vm-touch-whisking
  asked: 2026-10-20
  question: At what resolution is dVm/dt of the touch-aligned average Vm taken for the latency rule,
    the recording's own sampling rate (10 or 20 kHz) or the average in 1 ms bins as for the spike
    PSTH? The same question applies to the laser-onset latencies of exc-thalamus-photoinhibition and
    to exc-vm-touch-whisking.
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
cat > questions/001187.yaml <<'EOF'
dandiset: "001187"
paper: doi:10.1016/j.neuron.2024.09.013
questions:
- claim: fig3a-area-interactions
  asked: 2026-11-01
  question: Should the outlier rule of the paper's code (O-C, NWB_computeGLM.m) be the main reading
    for the mixed-effects GLMs, with the Methods rule (O-M) kept for the permutation t-tests? The
    same question applies to fig2b-hippocampus-persistent, fig2c-hippocampus-correct-load,
    fig2e-amygdala-persistent, fig2f-amygdala-load-not-accuracy, fig3b-hippocampus-predicts-ltm,
    fig3b-amygdala-no-prediction, fig3g-nonpreferred-no-effect and fig3h-encoding-no-effect.
  passage: Before each test, we removed neurons that had no spikes in at least one of the tested
    conditions (including the baseline period) or differed ±3 SD from the mean across all neurons
    and all tested conditions. This explains differences in degrees of freedom between
    comparisons. (STAR Methods, Statistics). The linked code computes the Fig. 3a GLM and removes
    only neurons whose mean normalized rate exceeds 3 SD of the neuron means (NWB_computeGLM.m).
  why: The Methods sentence names "tested conditions" and degrees of freedom, which fit the
    t-tests; for a GLM with a continuous confidence term the conditions are not defined, and the
    claims file makes O-M the main reading. On the dataset, O-C gives the paper's betas within
    tolerance for Fig. 3a (56.61, 16.60, -27.83; with the all-sure session kept as the code does,
    59.96, 17.84, -29.16) and Fig. 3b hippocampus (21.25, 67.37, -30.69), and the paper's pattern
    for Fig. 2c (accuracy 18.68, p = 0.028; load 13.63, p = 0.0034). O-M gives smaller betas, and
    for Fig. 2c and Fig. 3h a different outcome. The outcomes of this attempt were judged on O-M
    as the claims file says.
EOF
date -u
```

```
Sun Nov  1 08:11:24 UTC 2026
```

**Agent calls Bash**

```bash
cat > attempts/001187-daume-2024-01.yaml <<'EOF'
schema_version: 2
id: 001187-daume-2024-01
dataset:
  archive: dandi
  id: "001187"
  version: 0.240904.2347
  doi: 10.48324/dandi.001187/0.240904.2347
paper: doi:10.1016/j.neuron.2024.09.013
date: 2026-11-01
entry: 001187-daume-2024
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-13
  runner:
    platform: GitHub Actions
    url: https://github.com/catalystneuro/encore/actions/runs/41284150060
outcomes:
- claim: sessions-and-neurons
  outcome: reproduced
  notebook: reproduce_daume_2024.ipynb
  output: claim:sessions-and-neurons
  measured: [46, 950, 351, 532]
  notes: The dandiset holds 46 sessions of 39 subjects and 950 units (380 hippocampus, 570
    amygdala). The rate filter of the paper's code removes 67 units (7.1%) and leaves 351 and 532.
    Table S1's recorded counts sum to 973 (386 and 587); see table-s1-counts.
- claim: table-s1-counts
  outcome: partially_reproduced
  notebook: reproduce_daume_2024.ipynb
  output: claim:table-s1-counts
  notes: All 46 sessions are matched to Table S1 by the label in the file identifier; the WM and
    LTM accuracies agree with the table to within 0.18 and 1.52 points. 42 sessions match the
    recorded counts before the rate filter (21 after it). Four differ, P1809jh (hippocampus 1
    against 6), P61cs_2 (hippocampus 1 against 2), P68cs (amygdala 7 against 17) and P82cs
    (amygdala 17 against 24); these 23 units are the difference between Table S1's 973 and the
    950 of the text. The per-session category and MS counts were not compared.
  deviations:
  - The per-session category-selective and memory-selective counts of Table S1, which the
    criterion asks to compare as a report, are not printed per session; only totals are compared
    under category-neuron-counts and ms-neuron-counts.
- claim: behaviour-overall-accuracy
  outcome: reproduced
  notebook: reproduce_daume_2024.ipynb
  output: claim:behaviour-overall-accuracy
  measured: [93.33, 70.32, 1.189]
  notes: WM accuracy 93.33% (SD 7.60), LTM accuracy 70.32% (SD 9.89), d' 1.189 (SD 0.620); no hit
    or false-alarm rate is 0 or 1. Both accuracies exceed 50% with the smallest permutation p the
    test gives (about 1e-4, below 0.0001), t(45) = 38.67 and 13.93.
- claim: fig1c-wm-accuracy-load
  outcome: reproduced
  notebook: reproduce_daume_2024.ipynb
  output: claim:fig1c-wm-accuracy-load
  notes: Load 1 95.09%, load 3 91.58%; t(45) = 4.91 (paper 4.89), permutation p below 0.0001.
- claim: fig1d-wm-rt-load
  outcome: partially_reproduced
  notebook: reproduce_daume_2024.ipynb
  output: claim:fig1d-wm-rt-load
  notes: With response times above 5 s set to missing, load 1 1.393 s and load 3 1.525 s, t(45) =
    -4.28 (paper -4.29), permutation p = 0.0003, so faster at p < 0.05 but not at p < 0.0001 as the
    criterion requires for reproduced. The t statistic matches the paper's; the p depends on the
    permutation draw. Without the 5 s cut (variant), t = 0.20, p = 0.86.
- claim: fig1e-ltm-confidence-accuracy
  outcome: reproduced
  notebook: reproduce_daume_2024.ipynb
  output: claim:fig1e-ltm-confidence-accuracy
  notes: 45 sessions (sub-11, whose ratings are all 1 or 6, left out). High 77.31%; low 61.40%
    pooled, t(44) = 8.51 (paper 8.66), or 62.48% averaged, t(44) = 7.34; p below 0.0001 in both.
- claim: ltm-rt-confidence
  outcome: reproduced
  notebook: reproduce_daume_2024.ipynb
  output: claim:ltm-rt-confidence
  measured: [1.838, 2.618]
  notes: Reading (b), response times above 5 s set to missing, matches with low confidence pooled
    (1.838 and 2.618 s, t(44) = -11.37) and averaged (1.838 and 2.659 s, t(44) = -11.22), p below
    0.0001. Reading (a), all response times, gives 2.205 and 3.565 s, outside tolerance, with high
    still faster (t(44) = -7.30).
  deviations:
  - The paper's means match only with response times above 5 s set to missing, the code's rule
    (plot_behavior.m), which the text does not state; the criterion lists it as a reading.
- claim: fig1f-ltm-load
  outcome: reproduced
  notebook: reproduce_daume_2024.ipynb
  output: claim:fig1f-ltm-load
  notes: Hit rate 68.59% for load 1 pictures and 65.77% for load 3, t(45) = 2.65, p = 0.0097
    (paper t = 2.42, p = 0.018).
- claim: fig1g-ltm-probe
  outcome: reproduced
  notebook: reproduce_daume_2024.ipynb
  output: claim:fig1g-ltm-probe
  notes: Hit rate 72.10% for pictures shown twice, 63.99% for pictures shown once, t(45) = 6.80
    (paper 7.25), p below 0.0001.
- claim: category-neuron-counts
  outcome: reproduced
  notebook: reproduce_daume_2024.ipynb
  output: claim:category-neuron-counts
  measured: [102, 222]
  notes: 102 of 351 hippocampal (29.06%) and 222 of 532 amygdala (41.73%) units. Reading the
    second test as a two-sided p < 0.05 gives 96 and 205.
- claim: fig2b-hippocampus-persistent
  outcome: partially_reproduced
  notebook: reproduce_daume_2024.ipynb
  output: claim:fig2b-hippocampus-persistent
  measured: [17.29, 7.79]
  notes: Under all four readings with the Methods outlier rule (O-M) the intercept and the
    preferred effect are positive at p < 0.05, with one beta outside tolerance in each. One row
    per trial, baseline B1, gives intercept 17.29 (p = 0.0008) and preferred 7.79 (p = 0.0008);
    B2 gives 22.38 and 11.86; the code's rows give 21.93 and 7.06 (B1) or 27.84 and 6.18 (B2). The
    code's rule (O-C) with one row per trial and B1 gives 19.39 and 13.12. The outlier rule for
    the GLMs is asked of a reader (questions/001187.yaml).
  deviations:
  - The conditions of the O-M rule for this GLM are the levels of the preferred factor; the
    Methods do not define conditions for a GLM.
  - Mixed models are fitted by maximum likelihood with statsmodels MixedLM, not MATLAB fitglme;
    p-values from the t distribution on n - p degrees of freedom.
- claim: fig2c-hippocampus-correct-load
  outcome: not_reproduced
  assumed: true
  notebook: reproduce_daume_2024.ipynb
  output: claim:fig2c-hippocampus-correct-load
  measured: [6.88, 4.96]
  notes: Under the adopted reading (one row per trial, main effects, baseline B1, O-M) 88 of 102
    neurons remain and neither effect is significant (accuracy 6.88, p = 0.26; load 4.96, p =
    0.14). With baseline B2 load is significant (9.19, p = 0.030) and accuracy is not (10.76, p =
    0.16), which the criterion grades partial; with the interaction term, no main effect is
    significant under either baseline. The code's rule (O-C, variant) gives accuracy 18.68 (p =
    0.028) and load 13.63 (p = 0.0034), the paper's pattern with the load beta within tolerance.
    The outlier rule for the GLMs is asked of a reader.
  deviations:
  - Assumed baseline B1 (mean baseline over all WM trials of the neuron) for this trial-level
    model; the Results describe one row per trial ("all correct WM trials"), and B2, the mean
    over the rows of the code's Fig. 3a table, belongs to that table. B2 grades the claim
    partially reproduced.
  - Assumed the main-effects model (reading a), as the text names two effects.
  - O-M conditions are the cells of accuracy and load; taking each factor's levels separately
    removes the same neurons.
- claim: fig2e-amygdala-persistent
  outcome: partially_reproduced
  notebook: reproduce_daume_2024.ipynb
  output: claim:fig2e-amygdala-persistent
  measured: [10.06, 5.44]
  notes: Under all four O-M readings the intercept and preferred effect are positive at p <
    0.05 (p at most 0.0038). The preferred beta is below tolerance in every reading (4.28 to
    5.44 against 6.91 +- 0.69); the intercept is within tolerance in three (10.06, 9.46, 10.32)
    and above it with the code's rows and B1 (11.99). O-C gives preferred 5.08 to 6.88.
  deviations:
  - As fig2b-hippocampus-persistent.
- claim: fig2f-amygdala-load-not-accuracy
  outcome: partially_reproduced
  notebook: reproduce_daume_2024.ipynb
  output: claim:fig2f-amygdala-load-not-accuracy
  measured: [10.77]
  notes: The accuracy effect is absent under every reading (O-M p 0.056 to 0.11, betas -8.90 to
    -9.95; paper -6.13, p = 0.24). The load effect is positive at p < 0.05 in the main-effects
    model (10.77 with B1, 8.95 with B2) but below 12.309 +- 1.231, and not significant with the
    interaction term (p = 0.55 and 0.61). Only the accuracy part holds under every reading. O-C
    gives load 11.55 and 9.92.
  deviations:
  - As fig2c-hippocampus-correct-load, without the assumption, since all readings give the same
    grade.
- claim: fig3a-area-interactions
  outcome: partially_reproduced
  assumed: true
  notebook: reproduce_daume_2024.ipynb
  output: claim:fig3a-area-interactions
  measured: [17.84, 49.18, -24.46]
  notes: With O-M, conditions the levels of LTM accuracy (adopted), 310 neurons; confidence x
    area 17.84 (p = 0.027), LTM accuracy x area 49.18 (p = 0.022), three-way -24.46 (p = 0.017);
    main effects and accuracy x confidence p >= 0.27. Two betas are outside tolerance. With
    confidence levels also as conditions, 53 neurons are removed and the interactions give p =
    0.27, 0.056 and 0.056. The code's rule (O-C) gives 16.60, 56.61 and -27.83 (p = 0.038, 0.0075,
    0.0059), all within tolerance, and with the all-sure session kept as the code does, 17.84,
    59.96 and -29.16. The outlier rule for the GLMs is asked of a reader.
  deviations:
  - Assumed the O-M conditions of this GLM are the levels of LTM accuracy only, since confidence
    enters the model as a continuous variable (Methods, Relating WM maintenance activity to LTM
    formation); with confidence levels as conditions the outcome would be not reproduced.
  - The session whose ratings are all sure (sub-11, P69cs) is left out, as the paper says one
    patient was excluded from all confidence analyses (Results, paragraph 2); the code keeps it,
    shown as a variant.
- claim: fig3b-hippocampus-predicts-ltm
  outcome: partially_reproduced
  notebook: reproduce_daume_2024.ipynb
  output: claim:fig3b-hippocampus-predicts-ltm
  measured: [19.18, 43.57, -21.80]
  notes: Under every O-M reading the three effects are significant with the paper's signs, with
    outliers over both areas or within the area confidence 19.18 (p = 0.008), LTM accuracy 43.57
    (p = 0.026), interaction -21.80 (p = 0.019); with confidence levels as conditions 11.07 to
    13.13, 37.92 to 51.95, -18.38 to -22.63. LTM accuracy and the interaction are outside
    tolerance in every O-M reading. O-C gives 21.25, 67.37 and -30.69, all within tolerance.
  deviations:
  - As fig3a-area-interactions; the grade is the same under both O-M readings, so it rests on no
    assumption.
- claim: fig3b-amygdala-no-prediction
  outcome: reproduced
  notebook: reproduce_daume_2024.ipynb
  output: claim:fig3b-amygdala-no-prediction
  notes: No effect has p < 0.05 under any reading or outlier rule (smallest p 0.34). Under O-M
    with outliers over both areas, confidence 3.29 (p = 0.40), LTM accuracy 2.47 (p = 0.81),
    interaction -1.24 (p = 0.80).
- claim: fig3c-hippocampus-high-confidence
  outcome: not_reproduced
  notebook: reproduce_daume_2024.ipynb
  output: claim:fig3c-hippocampus-high-confidence
  notes: High confidence, remembered against forgotten, t(68) = 1.17, p = 0.26 (normalized) and
    t(70) = 1.79, p = 0.078 (spikes per second); low confidence p = 0.30 and 0.10. 80 neurons have
    both high-confidence conditions, 73 have spikes in both, 69 or 71 remain after O-M, against 83
    in the paper. Keeping the all-sure session gives p = 0.33 and 0.054 for high confidence.
  deviations:
  - The all-sure session is left out (variant shown with it).
- claim: fig3d-amygdala-no-difference
  outcome: reproduced
  notebook: reproduce_daume_2024.ipynb
  output: claim:fig3d-amygdala-no-difference
  notes: High confidence p = 0.85 and 0.64 (mean differences -0.97% and -0.04 Hz), low p = 0.30
    and 0.51; 146 to 147 neurons (paper 159 and 153).
- claim: fig3e-early-delay-cluster
  outcome: partially_reproduced
  notebook: reproduce_daume_2024.ipynb
  output: claim:fig3e-early-delay-cluster
  measured: 1050
  notes: Under all four readings (binning and rate) a cluster with remembered above forgotten has
    cluster p < 0.025, from about 0.875 to 1.05 s (p 0.0001 to 0.0196), not 0 to 650 ms. Early
    clusters exist only below significance (0 to 0.125 s, p = 0.061, spikes per second in 200 ms
    windows; 0 to 0.025 s, p = 0.25, normalized). The measured end is that of the significant
    cluster under the first reading (200 ms windows, normalized).
  deviations:
  - The cluster-forming threshold is FieldTrip's default 0.05 (two-sided), as the claims file
    names; the paper does not give it.
- claim: fig3f-amygdala-no-cluster
  outcome: reproduced
  notebook: reproduce_daume_2024.ipynb
  output: claim:fig3f-amygdala-no-cluster
  notes: No cluster has p < 0.025 under any reading; the smallest cluster p is 0.43.
- claim: fig3g-nonpreferred-no-effect
  outcome: reproduced
  assumed: true
  notebook: reproduce_daume_2024.ipynb
  output: claim:fig3g-nonpreferred-no-effect
  notes: With O-M, conditions the levels of LTM accuracy, no fixed effect other than the
    intercept has p < 0.05 in either set of rows (smallest p 0.071 and 0.23); with O-C 0.067 and
    0.11. With confidence levels also as conditions, the area main effect is 13.28 (p = 0.035)
    in reading (a) and nothing in (b).
  deviations:
  - Assumed the O-M conditions are the levels of LTM accuracy, as for fig3a-area-interactions.
- claim: fig3h-encoding-no-effect
  outcome: not_reproduced
  assumed: true
  notebook: reproduce_daume_2024.ipynb
  output: claim:fig3h-encoding-no-effect
  notes: With O-M, conditions the levels of LTM accuracy, an effect reaches p < 0.05 under both
    readings, the area main effect in (a) (56.58, p = 0.048) and LTM accuracy x confidence in (b)
    (15.63, p = 0.027). With confidence levels as conditions (smallest p 0.0505 and 0.41) or with
    O-C (0.35 and 0.074), nothing reaches p < 0.05. No reading shows an effect of LTM accuracy or
    confidence alone. The criterion counts any fixed effect, including area.
  deviations:
  - Assumed the O-M conditions are the levels of LTM accuracy, as for fig3a-area-interactions;
    the other O-M reading and the code's rule give reproduced.
  - The zero-spike rule is applied to the picture 1 window, the window tested.
- claim: ms-neuron-counts
  outcome: reproduced
  notebook: reproduce_daume_2024.ipynb
  output: claim:ms-neuron-counts
  measured: [53, 26]
  notes: 53 of 351 hippocampal units (15.10%), 26 familiarity- and 27 novelty-selective. The
    amygdala has 69 (Table S1 68).
- claim: fig4b-ms-confidence-auc
  outcome: reproduced
  notebook: reproduce_daume_2024.ipynb
  output: claim:fig4b-ms-confidence-auc
  notes: Reading (a), 49 neurons, AUC 0.5975 high against 0.5577 low, t(48) = 3.87, p = 0.0005;
    reading (b), 40 neurons (paper 41), 0.5994 against 0.5621, t(39) = 3.55, p = 0.0009.
  deviations:
  - The ROC thresholds span the counts of the two groups compared; the Methods say "the minimal
    and maximal spike count observed" without naming the trials.
  - The all-sure session is left out (one MS neuron).
- claim: fig4c-overlap-chance
  outcome: reproduced
  notebook: reproduce_daume_2024.ipynb
  output: claim:fig4c-overlap-chance
  measured: 19
  notes: 19 neurons are both MS and category neurons (of 53 and 102); the null has mean 15.55
    (7 to 26) and p = 0.179.
- claim: fig4d-category-no-memory-signal
  outcome: blocked
  blocked_by: metadata_insufficient
  notebook: reproduce_daume_2024.ipynb
  output: claim:fig4d-category-no-memory-signal
  notes: The test needs the category of new LTM pictures, and the dataset gives none. New
    pictures have IDs 1001 to 1200 and their images are named only by ID; old pictures keep
    their WM IDs, whose leading digit is the category. The category neurons' responses suggest
    blocks of 40 IDs per category (the best block is the preferred category for 188 of 324
    neurons, 58.0%, against 60.5% for old pictures and 16.4% for a grouping by ID modulo 5). Under
    that inferred mapping, shown as a variant that decides nothing, no GLM effect reaches p <
    0.05 (smallest 0.079 with O-M) and no old against new t-test does (smallest 0.22), as the
    paper reports.
- claim: fig4e-fs-strong-maintenance
  outcome: not_reproduced
  notebook: reproduce_daume_2024.ipynb
  output: claim:fig4e-fs-strong-maintenance
  measured: [197, 84, -0.17]
  notes: 197 MS and category pairs (178 without self-pairs), 84 FS pairs (74). Under all 16 GLM
    readings the maintenance beta is negative (-0.14 to -0.19 Hz, -6.5 to -9.4 normalized; p
    0.059 to 0.45), and under all 8 t-test readings strong is below weak (t -1.00 to -1.60, p 0.11
    to 0.33). The measured beta is that of the first reading, in spikes per second.
  deviations:
  - A rate equal to the category neuron's median goes to weak (a standard choice).
- claim: fig4f-ns-no-effect
  outcome: reproduced
  assumed: true
  notebook: reproduce_daume_2024.ipynb
  output: claim:fig4f-ns-no-effect
  notes: Under the adopted reading (all trials of the old pictures, self-pairs kept, spikes per
    second) the GLM gives beta 0.006 (p = 0.90) or 0.010 (p = 0.85) and the t-test t(106) = -1.03,
    p = 0.31, with 107 NS pairs (paper 122). No GLM reading reaches p < 0.05; one t-test reading
    does (pictures answered old, self-pairs dropped, spikes per second, t(81) = 2.04, p = 0.040).
  deviations:
  - Assumed reading E2 (a), all LTM trials of the old pictures, since the Results speak of the
    "familiar trials" with no restriction to correct ones, and E3 (a), self-pairs kept, since
    that gives 197 pairs against the paper's 198 (178 without); E4 (a), spikes per second, as
    the text speaks of firing rates. The readings that drop self-pairs and keep only pictures
    answered old give p = 0.040 in the t-test.
findings:
- kind: paper_inconsistency
  statement: Table S1's recorded unit counts sum to 973 (386 hippocampus, 587 amygdala), while
    the Methods say 950 units were isolated. The dandiset holds 950, and four sessions have fewer
    units than Table S1 lists (P1809jh hippocampus 1 against 6, P61cs_2 hippocampus 1 against 2,
    P68cs amygdala 7 against 17, P82cs amygdala 17 against 24).
- kind: metadata_error
  statement: Every file gives Cedars-Sinai Medical Center as the institution, though 14 sessions
    have Toronto Western identifiers (TWH) and 6 Johns Hopkins identifiers (JHU), and the paper
    says the patients were recorded at three institutions.
- kind: metadata_insufficient
  statement: The new pictures of the LTM test (IDs 1001 to 1200) carry no category, and their
    stimulus images are named only by ID, so analyses of preferred-category new pictures (Fig. 4d)
    cannot be repeated. The neural responses suggest consecutive blocks of 40 IDs per category.
- kind: metadata_insufficient
  statement: The LTM confidence column is described as 1 to 6 with no coding. The accuracy column
    agrees in every trial with 1 to 3 meaning new and 4 to 6 old, 1 and 6 being sure as the
    paper's code reads it, but the coding is not stated in the files.
- kind: metadata_error
  statement: One LTM trial of sub-24 session 2 has confidence 7, outside the documented 1 to 6.
- kind: format_error
  statement: Five units have spike times out of order in the units table (sub-13 session 1 units
    1 and 2, sub-2 session 2 units 19 and 29, sub-24 session 2 unit 10).
- kind: other
  statement: Eight sessions have fewer than 400 LTM trials (161, 187, 228, 257, 384, 390, 395, 399)
    and one has 139 WM trials, where the paper describes 400 and 140. Picture 1 lasts 1.57 to 2.04
    s and the maintenance period 2.53 to 3.20 s, where the Methods say 2 s and 2.55 to 2.85 s.
- kind: code_mismatch
  statement: The paper's code for the Fig. 3a GLM (NWB_computeGLM.m) removes outlier neurons by
    their mean normalized rate above 3 SD, without centring, where the Methods remove neurons with
    no spikes in a tested condition or outside mean +- 3 SD; and it keeps the session whose
    ratings are all sure, which the Results say was excluded from confidence analyses. With the
    code's choices the GLMs of Fig. 3a and 3b give the paper's betas within tolerance; with the
    Methods' rule they do not.
- kind: methods_unavailable
  statement: For the authors. How was the outlier rule of the Methods ("no spikes in at least one
    of the tested conditions ... or differed ±3 SD from the mean across all neurons and all tested
    conditions") applied to the mixed-effects GLMs, whose confidence term is continuous, and to
    which baseline mean were trial-level rates normalized in Fig. 2? Here the conditions were
    taken as the levels of the categorical factors and the baseline as the mean over all WM
    trials; other readings change the outcomes of Fig. 2c, 3a, 3g and 3h.
- kind: methods_unavailable
  statement: For the authors. The Methods sentence on the GLM of Fig. 4e and 4f lost its variable
    names ("with (2 levels, high vs low, categorical) as fixed effect and nested into as random
    intercept"). Which unit was the random intercept nested in patient (MS neuron or pair), were
    all LTM trials of the old pictures used or only those answered old, and was a neuron both
    MS and category paired with itself? Fig. 4f's outcome depends on these.
EOF
grep -n ": .*: " attempts/001187-daume-2024-01.yaml | grep -v "^\s*[0-9]*:\s*-\? *[a-z_]*: \[" | head
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
python - <<'EOF'
import yaml,re
t=open('attempts/001187-daume-2024-01.yaml').read()
yaml.safe_load(t)
for i,l in enumerate(t.split('\n'),1):
    s=l.strip()
    body = re.sub(r'^-?\s*[a-z_]+: ', '', s)
    if ': ' in body or body.endswith(':') and not re.match(r'^-?\s*[a-z_]+:$', s): print(i,l)
for p in ['questions/001187.yaml']:
    t=open(p).read(); yaml.safe_load(t)
    for i,l in enumerate(t.split('\n'),1):
        s=l.strip(); body=re.sub(r'^-?\s*[a-z_]+: ', '', s)
        if ': ' in body: print(p,i,l)
EOF
python tools/entry.py check entries/001187-daume-2024 2>&1 | tail
```

```
0 error(s)
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -n '/claim:fig3b-amygdala/,/=== cell/p' exec_out.txt | grep -v "none\|Intercept" | head -30
```

```
=== cell 70 ['claim:fig3b-amygdala-no-prediction']
                      reading          outliers         term   beta    SE        p  neurons    n  removed
 (a) outliers over both areas               O-M       LTMacc  -5.68 11.27 0.614290      213 7853        8
 (a) outliers over both areas               O-M        conf3   1.28  4.36 0.768497      213 7853        8
 (a) outliers over both areas               O-M LTMacc:conf3   2.72  5.42 0.616559      213 7853        8
 (a) outliers over both areas O-M by confidence       LTMacc   2.47 10.01 0.805069      182 6675       53
 (a) outliers over both areas O-M by confidence        conf3   3.29  3.90 0.398516      182 6675       53
 (a) outliers over both areas O-M by confidence LTMacc:conf3  -1.24  4.84 0.797208      182 6675       53
 (a) outliers over both areas               O-C       LTMacc  -0.22 10.38 0.983426      212 7814        6
 (a) outliers over both areas               O-C        conf3   2.62  4.01 0.513710      212 7814        6
 (a) outliers over both areas               O-C LTMacc:conf3   0.57  4.98 0.909321      212 7814        6
 (b) outliers within the area               O-M       LTMacc   0.30 10.15 0.976300      211 7777        7
 (b) outliers within the area               O-M        conf3   2.40  3.95 0.542912      211 7777        7
 (b) outliers within the area               O-M LTMacc:conf3   0.63  4.89 0.897410      211 7777        7
 (b) outliers within the area O-M by confidence       LTMacc   5.52  9.26 0.550813      181 6637       37
 (b) outliers within the area O-M by confidence        conf3   3.45  3.62 0.340270      181 6637       37
 (b) outliers within the area O-M by confidence LTMacc:conf3  -1.55  4.47 0.728568      181 6637       37
 (b) outliers within the area               O-C       LTMacc  -0.22 10.38 0.983426      212 7814        6
 (b) outliers within the area               O-C        conf3   2.62  4.01 0.513710      212 7814        6
 (b) outliers within the area            
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='attempts/001187-daume-2024-01.yaml'; t=open(p).read()
old='''(smallest p 0.34). Under O-M
    with outliers over both areas, confidence 3.29 (p = 0.40), LTM accuracy 2.47 (p = 0.81),
    interaction -1.24 (p = 0.80).'''
new='''(smallest p 0.34). Under O-M
    with outliers over both areas, confidence 1.28 (p = 0.77), LTM accuracy -5.68 (p = 0.61),
    interaction 2.72 (p = 0.62).'''
assert old in t; t=t.replace(old,new); open(p,'w').write(t)
EOF
date -u
```

```
Sun Nov  1 08:13:03 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && python - <<'EOF'
n=open('notebook.py').read()
old='''print("MS neurons by patient (hippocampus):", K[(K.area == "hippocampus") & K.ms].patient.value_counts().to_dict())'''
new=old+'''
# Table S1 per-session category and MS counts, as a report for table-s1-counts
cnt = K.groupby(["session", "area"])[["cat", "ms"]].sum().unstack(fill_value=0)
rep = TS1[["label", "session", "h_cat", "a_cat", "h_ms", "a_ms"]].copy()
rep["h_cat_here"] = rep.session.map(cnt[("cat", "hippocampus")]).fillna(0).astype(int)
rep["a_cat_here"] = rep.session.map(cnt[("cat", "amygdala")]).fillna(0).astype(int)
rep["h_ms_here"] = rep.session.map(cnt[("ms", "hippocampus")]).fillna(0).astype(int)
rep["a_ms_here"] = rep.session.map(cnt[("ms", "amygdala")]).fillna(0).astype(int)
for a in ("h_cat", "a_cat", "h_ms", "a_ms"):
    print(f"Table S1 {a}: sessions equal {int((rep[a] == rep[a + '_here']).sum())} of {len(rep)}, "
          f"total {rep[a].sum()} in the table, {rep[a + '_here'].sum()} here")'''
assert old in n; n=n.replace(old,new)
open('notebook.py','w').write(n)
EOF
python - <<'EOF'
p='attempts/001187-daume-2024-01.yaml'; t=open(p).read()
old='''    950 of the text. The per-session category and MS counts were not compared.
  deviations:
  - The per-session category-selective and memory-selective counts of Table S1, which the
    criterion asks to compare as a report, are not printed per session; only totals are compared
    under category-neuron-counts and ms-neuron-counts.
'''
new='''    950 of the text. The per-session category and MS counts, a report, are printed under
    ms-neuron-counts.
'''
assert old in t; t=t.replace(old,new); open(p,'w').write(t)
EOF
cat > entries/001187-daume-2024/README.md <<'EOF'
# Daume et al. (2024) from dandiset 001187

Tests the findings of [Daume et al. (2024)](https://doi.org/10.1016/j.neuron.2024.09.013) on
[DANDI:001187](https://dandiarchive.org/dandiset/001187/0.240904.2347), the version the paper
cites. It holds the spike times of 950 units from the hippocampus and amygdala of 39 patients
in 46 sessions of a Sternberg working memory task and a later recognition test.

| Claim | Outcome |
|---|---|
| Sessions and units (46 sessions, 950 units, 351 and 532 after the rate filter) | Reproduced |
| Per-session unit counts of Table S1 | Partially reproduced |
| Behaviour (accuracy, d', load, confidence, probe effects; five claims) | Reproduced |
| WM responses faster in load 1 | Partially reproduced |
| Category neuron counts | Reproduced |
| Persistent and preferred-category maintenance activity (Fig. 2b, 2e) | Partially reproduced |
| Accuracy and load effects for preferred trials (Fig. 2c) | Not reproduced |
| Load but not accuracy effect in amygdala (Fig. 2f) | Partially reproduced |
| Area interactions and hippocampal prediction of later memory (Fig. 3a, 3b) | Partially reproduced |
| No prediction in amygdala (Fig. 3b, 3d, 3f) | Reproduced |
| Remembered above forgotten with high confidence in hippocampus (Fig. 3c) | Not reproduced |
| Early-maintenance cluster in hippocampus (Fig. 3e) | Partially reproduced |
| No effect for non-preferred pictures (Fig. 3g) | Reproduced |
| No effect during encoding (Fig. 3h) | Not reproduced |
| Memory-selective neurons, their AUC and overlap with category neurons (Fig. 4b, 4c) | Reproduced |
| Category neurons carry no memory signal (Fig. 4d) | Blocked: metadata insufficient |
| FS neurons fire more after strong maintenance (Fig. 4e) | Not reproduced |
| NS neurons show no such effect (Fig. 4f) | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Several of the mixed-model outcomes depend on the outlier rule. The claims file makes the rule of
the Methods the main reading; the rule in the paper's code gives the paper's betas for Figures 2c,
3a and 3b, and this is asked of a reader in `questions/001187.yaml`. The new pictures of the
recognition test carry no category in the dataset, which blocks Figure 4d. The attempt record,
with the reasons and the differences from the paper's method, is
[`attempts/001187-daume-2024-01.yaml`](../../attempts/001187-daume-2024-01.yaml).
EOF
source $TMPDIR/env/bin/activate && python $TMPDIR/nb/build.py $TMPDIR/nb/notebook.py entries/001187-daume-2024/reproduce_daume_2024.ipynb && cd  && python tools/entry.py check entries/001187-daume-2024 2>&1 | tail -3
```

```
File "tools/entry.py", line 55, in <module>
    import yaml
ModuleNotFoundError: No module named 'yaml'
```

**Agent calls Bash**

```bash
python tools/entry.py check entries/001187-daume-2024 2>&1 | tail -3 && time python tools/entry.py all entries/001187-daume-2024 2>&1 | tail -3
```

```
0 error(s)
Installed kernelspec registry-001187-daume-2024 in executed/001187-daume-2024/.venv/share/jupyter/kernels/registry-001187-daume-2024
0 error(s)
pass  reproduce_daume_2024.ipynb  (416 s)

real	7m2.535s
user	12m43.791s
sys	0m14.131s
```

**Agent calls Bash**

```bash
python - <<'EOF' > $TMPDIR/exec_out2.txt
import nbformat
nb=nbformat.read('executed/001187-daume-2024/reproduce_daume_2024.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    txt=''.join(o.get('text','') if o.output_type=='stream' else str(o.get('data',{}).get('text/plain','')) + o.get('evalue','') for o in c.outputs)
    print(f'=== cell {i} {c.metadata.get("tags",[])}'); print(txt)
EOF
cd $TMPDIR && diff <(grep -v "loaded in\|took\|run time\|selection time" exec_out.txt) <(grep -v "loaded in\|took\|run time\|selection time" exec_out2.txt) | head -60
```

```
142c142
< /tmp/claude-1001/ipykernel_39/1844796046.py:38: RuntimeWarning: Mean of empty slice
---
> /tmp/claude-1001/ipykernel_29/1844796046.py:38: RuntimeWarning: Mean of empty slice
146,147c146,147
< wm_acc: mean 93.33 % (SD 7.60), expected 93.3 +- 1.1, within: True; against 50%: t(45) = 38.67, perm p = 0.000100
< ltm_acc: mean 70.32 % (SD 9.89), expected 70.3 +- 1.4, within: True; against 50%: t(45) = 13.93, perm p = 0.000100
---
> wm_acc: mean 93.33 % (SD 7.60), expected 93.3 +- 1.1, within: True; against 50%: t(45) = 38.67, perm p = 0.0001 (below 0.0001: True)
> ltm_acc: mean 70.32 % (SD 9.89), expected 70.3 +- 1.4, within: True; against 50%: t(45) = 13.93, perm p = 0.0001 (below 0.0001: True)
149c149
< smallest p a 10,000-permutation test can give: 0.00010
---
> smallest p a 10,000-permutation test gives here: 0.0001
152c152
< load 1 95.09 %, load 3 91.58 %; t(45) = 4.91 (paper 4.89), perm p = 0.000100; sessions with load 1 higher: 32, equal 8
---
> load 1 95.09 %, load 3 91.58 %; t(45) = 4.91 (paper 4.89), perm p = 0.0001 (below 0.0001: True); sessions with load 1 higher: 32, equal 8
155,156c155,156
< RT > 5 s missing (main): load 1 1.393 s, load 3 1.525 s; t(45) = -4.28 (paper -4.29), perm p = 0.000300
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && diff <(grep -v "loaded in\|took\|run time\|selection time\|Warning\|perm p\|smallest p a\|ipykernel" exec_out.txt) <(grep -v "loaded in\|took\|run time\|selection time\|Warning\|perm p\|smallest p a\|ipykernel" exec_out2.txt); grep -n "Table S1 h_\|Table S1 a_" exec_out2.txt
```

```
589a590
> category neurons with rows in the Figure 3 table: hippocampus 100 amygdala 218
606d606
< category neurons with rows in the Figure 3 table: hippocampus 100 amygdala 218
839a840,843
> Table S1 h_cat: sessions equal 42 of 46, total 104 in the table, 102 here
> Table S1 a_cat: sessions equal 40 of 46, total 220 in the table, 222 here
> Table S1 h_ms: sessions equal 40 of 46, total 53 in the table, 53 here
> Table S1 a_ms: sessions equal 44 of 46, total 68 in the table, 69 here
874:Table S1 h_cat: sessions equal 42 of 46, total 104 in the table, 102 here
875:Table S1 a_cat: sessions equal 40 of 46, total 220 in the table, 222 here
876:Table S1 h_ms: sessions equal 40 of 46, total 53 in the table, 53 here
877:Table S1 a_ms: sessions equal 44 of 46, total 68 in the table, 69 here
Shell cwd was reset to
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='attempts/001187-daume-2024-01.yaml'; t=open(p).read()
old='''The per-session category and MS counts, a report, are printed under
    ms-neuron-counts.'''
new='''As a report (printed under ms-neuron-counts), the per-session
    category counts equal Table S1's in 42 (hippocampus) and 40 (amygdala) of 46 sessions, and
    the MS counts in 40 and 44.'''
assert old in t; t=t.replace(old,new); open(p,'w').write(t)
EOF
sed -i 's/runtime_minutes: 10/runtime_minutes: 7/' entries/001187-daume-2024/entry.yaml
grep "run time" $TMPDIR/exec_out2.txt; python tools/entry.py check entries/001187-daume-2024 2>&1 | tail -2; python tools/entry.py handover entries/001187-daume-2024 2>&1 | tail -5; ls executed/001187-daume-2024/handover/
```

```
notebook run time 6.9 min
0 error(s)
wrote executed/001187-daume-2024/handover
10.1016-j.neuron.2024.09.013.yaml
reproduce_daume_2024.ipynb
sbcat.py
```

**Agent calls Bash**

```bash
git status --short; grep -c "Result:" executed/001187-daume-2024/handover/reproduce_daume_2024.ipynb; date -u
```

```
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
?? attempts/001187-daume-2024-01.yaml
?? entries/001187-daume-2024/
?? questions/001187.yaml
?? scripts
0
Sun Nov  1 08:20:49 UTC 2026
```

**Agent**

I finished steps 1 to 5 of the Author section and ran the handover (step 6) at 08:21 UTC. `python tools/entry.py all` passes: 0 errors, and the notebook runs in 6.9 min. I did not verify my own work, and nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| sessions-and-neurons | reproduced (46 sessions, 950 units; 351 and 532 after the rate filter) |
| table-s1-counts | partially reproduced (unit counts match in 42 of 46 sessions) |
| behaviour-overall-accuracy, fig1c, fig1e, ltm-rt-confidence, fig1f, fig1g | reproduced |
| fig1d-wm-rt-load | partially reproduced (t = -4.28 against the paper's -4.29, but p = 0.0003, not below 0.0001) |
| category-neuron-counts | reproduced (102 hippocampus, 222 amygdala) |
| fig2b, fig2e, fig2f | partially reproduced |
| fig2c-hippocampus-correct-load | not reproduced (rests on an assumption) |
| fig3a-area-interactions | partially reproduced (rests on an assumption) |
| fig3b-hippocampus-predicts-ltm | partially reproduced |
| fig3b-amygdala, fig3d, fig3f | reproduced |
| fig3c-hippocampus-high-confidence | not reproduced |
| fig3e-early-delay-cluster | partially reproduced (the significant cluster is at 0.875 to 1.05 s, not 0 to 650 ms) |
| fig3g-nonpreferred-no-effect | reproduced (rests on an assumption) |
| fig3h-encoding-no-effect | not reproduced (rests on an assumption) |
| ms-neuron-counts, fig4b, fig4c | reproduced |
| fig4d-category-no-memory-signal | blocked, metadata_insufficient |
| fig4e-fs-strong-maintenance | not reproduced (the effect goes the other way, not significant) |
| fig4f-ns-no-effect | reproduced (rests on an assumption) |

## 2. The dataset, assumptions and questions

**Version.** I pinned 0.240904.2347. It is the version the paper cites and the only published one.

**Dataset findings.**
- Table S1 lists 973 units against 950 in the dandiset; four sessions differ.
- Every file names Cedars-Sinai as the institution, though 20 sessions are from Toronto Western or Johns Hopkins.
- New LTM pictures (IDs 1001 to 1200) have no category. Neural responses suggest blocks of 40 IDs per category, but that is an inference, so fig4d stays blocked.
- The confidence coding is undocumented, though it agrees with the accuracy column in every trial. One trial has confidence 7.
- Five units have spike times out of order. I sorted them before analysis.
- Eight sessions have fewer than 400 LTM trials, and one has 139 WM trials.
- The paper's code removes outliers differently from the Methods and keeps the session whose ratings are all "sure".

**Assumptions.**
- For the GLMs, the Methods outlier rule's "tested conditions" are the levels of the categorical factors (confidence is continuous).
- Fig. 2c uses baseline B1, the mean over all WM trials, with the main-effects model.
- Fig. 4f uses all trials of the old pictures, keeps self-pairs, and uses spikes per second.

**Questions for the paper's authors.** Two are recorded as `methods_unavailable` findings: how the outlier rule applies to the GLMs (and which baseline Fig. 2 used), and the variable names lost from the Fig. 4e/4f GLM sentence.

**Question to a reader** (`questions/001187.yaml`). Should the code's outlier rule be the main reading for the GLMs? With it, Fig. 3a gives 56.61, 16.60 and -27.83, and with the all-sure session kept 59.96, 17.84 and -29.16; Fig. 3b hippocampus gives 21.25, 67.37 and -30.69. All are within tolerance of the paper, which the Methods rule does not achieve.

## 3. Where the protocol was unclear

1. The claims file header says to block a claim when its readings disagree; protocol step 1.6 and the prompt allow adopting the best-supported reading as an assumption. I followed the protocol and marked those outcomes `assumed: true`.
2. Neither the protocol nor the claims file says how a per-condition outlier rule applies to a GLM. I treated it as an open method detail, ran two readings, and asked a reader as well.
3. The protocol does not say how to handle reference numbers needed only for comparison, such as Table S1. I put them in the helper as a labelled text table taken from the paper.
4. The protocol does not say whether an inference from the neural data, like the picture-category blocks, may be used. I showed it as a variant only and kept the claim blocked.
5. A presigned DANDI download URL refuses HEAD requests, which `docs/archives.md` does not mention. I read the redirect `Location` header instead.

## 4. Runtime and failures

- The run took 1 h 04 min of wall time (07:17 to 08:21 UTC), and the notebook takes 6.9 min.
- The default statsmodels optimizer stopped at a poorer fit once. I now run three optimizers and keep the best fit.
- Nothing is left failing.
- Untracked dotfiles (`.bashrc` and others) and a `scripts` directory sit in the repo root. I didn't create them and left them alone.

## End of run

99 turns, 60 minutes, result: success.
