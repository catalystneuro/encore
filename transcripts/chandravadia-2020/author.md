# chandravadia-2020 · author · run 43689559719

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cd  ls; ls docs entries attempts claims paper; wc -l docs/*.md README.md
```

```
Sun Nov 15 07:27:15 UTC 2026
LICENSE
LICENSE-data
README.md
attempts
bunfig.toml
claims
docs
encore_science
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
[... 966 more lines not kept]
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
3	Version: `pilot-15`. Record this version in the attempt's provenance.
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
[... 657 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/chandravadia-2020.yaml"
}
```

```
1	# Claims for Chandravadia, Liang, Schjetnan et al. (2020), Scientific Data 7, 78, on dandiset 000004.
2	# Source: the full text of the open access article (CC BY 4.0) at nature.com, read from its Methods,
3	# Data Records, Technical Validation, figure legends, Tables 1 and 2 and Online-only Table 1.
4	#
5	# When these criteria were written, the author had run the data check only, on every file of
6	# version 0.220126.1852: the file list and the archive's metadata; per file the subject metadata,
7	# session ids, session start dates, trial counts per phase, new/old label counts, stimulus categories,
8	# experiment ids, unit counts (1864 in total), electrode locations, waveform sampling rate and table
9	# columns; the comparison of subject age, sex and diagnosis with Online-only Table 1 (age or sex
10	# differ for three subjects); the duplicated spike trains of sessions 43 and 44 and of 54 and 55; and
11	# in one file (session 5) the cross-tabulation of new/old labels against confidence responses, which
12	# showed label 1 receiving most "old" responses. No selection of VS or MS cells, no AUC, no z-ROC and
13	# no accuracy by confidence had been computed. The author had read the paper's code
14	# (github.com/rutishauserlab/recogmem-release-NWB at commit 1d95162), including plotFigure5.ipynb,
15	# which writes the Figure 5f percentages into the plot as constants.
16	#
17	# After the first verification round the author added previous-release-link and rewrote the
18	# criterion of previous-release-additions, which had been blocked for want of the earlier
19	# release's session list. When writing them the author had read Table 1 of Faraut et al. 2018,
20	# which lists that release's sessions, and its abstract (65 sessions, 42 patients, 1576 neurons),
[... 402 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md | head -80; ls entries/fouke-2025 entries/chandravadia-2020; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; cat attempts/fouke-2025-01.yaml; cat papers/datasets/chandravadia-2020.yaml; ls questions | grep chand; ls transcripts | grep chand
```

```
<persisted-output>
Output too large (40.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/6c898745-4103-4792-a3f3-1899c84e389e/tool-results/bva2jea8p.txt

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
cd  ls entries/fouke-2025 entries/chandravadia-2020; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; cat papers/datasets/chandravadia-2020.yaml; ls questions | grep chand; ls transcripts | grep chand; ls executed 2>/dev/null | head
```

```
ls: cannot access 'entries/chandravadia-2020': No such file or directory
entries/fouke-2025:
README.md
entry.yaml
omr.py
reproduce_fouke_2025.ipynb
requirements.in
requirements.lock.txt
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
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls -la transcripts/chandravadia-2020; mkdir -p entries/chandravadia-2020; cat attempts/fouke-2025-01.yaml | head -150
```

```
total 16
drwxr-xr-x   2 runner runner  4096 Nov 15 07:27 .
drwxr-xr-x 288 runner runner 12288 Nov 15 07:21 ..
schema_version: 3
id: fouke-2025-01
datasets:
- archive: dandi
  id: "001453"
  version: 0.250518.1950
  doi: 10.48324/dandi.001453/0.250518.1950
  relation: primary
paper: doi:10.1016/j.cub.2025.04.027
date: 2026-10-14
entry: fouke-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
[... 133 more lines not kept]
```

**Agent**

The transcripts folder for this paper is empty, so nothing from the earlier attempts is visible. Next I'll read the record format, the DANDI notes and the paper.

**Agent calls Bash**

```bash
cd  sed -n '/^findings:/,$p' attempts/fouke-2025-01.yaml | head -60; grep -n "outcome: blocked" -A6 attempts/*.yaml | head -20; ls schemas; ls tools
```

```
findings:
- kind: data_missing
  statement: The dandiset holds only the freely swimming tracking of Figure 1 and Figure S1. The
    two-photon imaging and the head-fixed tail tracking behind Figures 2 to 4 are not in it, and
    the GitLab repository the paper names for all behavioural and imaging data holds analysis
    notebooks only. Nine of the paper's main findings cannot be tested.
- kind: metadata_insufficient
  statement: The stimulus codes 0 to 20 have no names or description in the files or the
    dandiset metadata. They can be named only from the paper's analysis notebook and the protocol
    file of its stimulus software.
- kind: code_mismatch
  statement: The paper's analysis notebook labels code 9 as lateral right and 11 as lateral left,
    while its conversion of the stimulus software's names gives the reverse (it carries a remap
    that swaps them). The data do not settle which is right; zebrafish barely turn to either, and
    Danionella turn more to the right for code 11, which fits the stimulus software's assignment
    only if the fish turn with lateral motion.
- kind: metadata_error
  statement: Subject ids 0 to 11 are each used for one zebrafish and one Danionella cerebrum, so
    subject_id does not identify an animal. The archive's summary counts 25 subjects and lists
    only Danio rerio; the files hold 37 fish of two species.
[... 103 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n '/## DANDI/,/^## [A-Z]/p' docs/archives.md | head -120; python3 -c "import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s['properties'],indent=0)[:6000])"
```

```
## DANDI

- **Datasets.** A dandiset, identified by six digits (`000003`). Targets are the
  public dandisets whose metadata names a paper (`targets/dandisets.json`, built
  by `tools/build_targets.py` and refreshed daily by the Track DANDI workflow).
- **Versions.** A published version (`0.220126.1855`) is fixed and has a DOI,
  `10.48324/dandi.<id>/<version>`. The draft can change. Pin the version the
  paper cites, or the latest published one. For a draft, record its
  modification time under `dataset: modified` in the attempt.
- **Reading.** List the assets and read metadata with the DANDI REST API
  (`https://api.dandiarchive.org/api/dandisets/<id>/versions/<version>/` and its
  `assets/` endpoint). Read NWB files by streaming them: open each asset's S3
  URL with `remfile` and `h5py`, and read it with `pynwb`. Do not download files
  to disk.
- **In an entry.** The entry names the dataset as `dandi:<id>/<version>` under
  `related`. The helper module keeps the version in one constant.

## CRCNS
{
"schema_version": {
[... 283 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -c paper/*; python3 - <<'E'
import json;s=json.load(open('schemas/attempt.schema.json'));p=s['properties']
for k in ['findings','inputs','verifications','reconciliation']:
  print(k, json.dumps(p.get(k),indent=0)[:1500])
E
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41597-020-0415-9.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  curl -s -o /dev/null -w "%{http_code}\n" https://api.dandiarchive.org/api/dandisets/000004/versions/0.220126.1852/; curl -s -o /dev/null -w "%{http_code}\n" https://api.github.com/repos/rutishauserlab/recogmem-release-NWB/commits/1d95162; curl -s -o /dev/null -w "%{http_code}\n" "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5810422/fullTextXML"; which python python3 uv; python3 --version; head -60 entries/fouke-2025/omr.py
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q dandi pynwb h5py remfile scipy pandas numpy matplotlib nbclient nbformat ipykernel requests 2>&1 | tail -3; python -c "import pynwb,dandi;print(pynwb.__version__)"
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/000004/versions/0.220126.1852/" > ver.json; python3 -c "
import json;d=json.load(open('ver.json'));m=d.get('metadata',d)
print(json.dumps({k:m.get(k) for k in ['name','description','assetsSummary','relatedResource','version','doi','citation','dateModified']},indent=1)[:4000])"; curl -s "https://api.dandiarchive.org/api/dandisets/000004/versions/0.220126.1852/assets/?page_size=200" > assets.json; python3 -c "
import json;d=json.load(open('assets.json'));print(d['count']);
for a in d['results']: print(a['path'],a['size'],a['asset_id'])" | head -120
```

```
4.2.0
Shell cwd was reset to
```

Result: the fetched text is not kept.

**Agent**

The dandiset version holds 87 files (6.2 GB, mostly stimulus images). I'll open one file and list its full contents.

**Agent calls Bash**

```bash
cd $TMPDIR; . dev/bin/activate; cat > probe.py <<'E'
import h5py, remfile, time, json
from dandi.dandiapi import DandiAPIClient
t=time.time()
c=DandiAPIClient(); ds=c.get_dandiset("000004","0.220126.1852")
a=ds.get_asset_by_path("sub-P9HMH/sub-P9HMH_ses-20060301_obj-1otd1m8_ecephys+image.nwb")
url=a.get_content_url(follow_redirects=1,strip_query=True); print(url)
f=h5py.File(remfile.File(url),'r')
def v(name,obj):
    if isinstance(obj,h5py.Dataset):
        if 'stimulus/presentation' in name and not name.endswith('stimuli_recog_1/data') : return
        print(name,obj.shape,obj.dtype,dict(obj.attrs).get('description','')[:150] if obj.attrs.get('description') is not None else '')
f.visititems(v)
for k in ['session_description','identifier','session_start_time','experiment_description','institution','lab','notes','data_collection','related_publications','experimenter','keywords','surgery','pharmacology','protocol','stimulus']:
  if k in f: print(k, f[k][()])
for k in f['general']: 
  o=f['general'][k]
  if isinstance(o,h5py.Dataset): print('general',k,o[()])
for k in f['general/subject']: print('subject',k,f['general/subject'][k][()])
print(list(f['stimulus/presentation'].keys())[:5], len(f['stimulus/presentation']))
print(time.time()-t)
E
python probe.py 2>&1 | grep -v "^stimulus/presentation/stimuli_" | head -150
```

```
https://dandiarchive.s3.amazonaws.com/blobs/58f/ff7/58fff79f-ef69-4f07-a876-34dd8d11462d
acquisition/events/data (1004,) object 
acquisition/events/timestamps (1004,) float64 
acquisition/experiment_ids/data (1004,) float64 
acquisition/experiment_ids/timestamps (1004,) float64 
file_create_date (1,) object 
general/data_collection () object 
general/experiment_description () object 
general/extracellular_ephys/electrodes/filtering (14,) object description of hardware filtering
general/extracellular_ephys/electrodes/group (14,) object a reference to the ElectrodeGroup this electrode is a part of
general/extracellular_ephys/electrodes/group_name (14,) object the name of the ElectrodeGroup this electrode is a part of
general/extracellular_ephys/electrodes/id (14,) int32 
general/extracellular_ephys/electrodes/imp (14,) float64 the impedance of the channel
general/extracellular_ephys/electrodes/location (14,) object the location of channel within the subject e.g. brain region
general/extracellular_ephys/electrodes/origChannel (14,) uint16 The original channel ID for the channel
general/extracellular_ephys/electrodes/x (14,) float64 the x coordinate of the channel location
general/extracellular_ephys/electrodes/y (14,) float64 the y coordinate of the channel location
general/extracellular_ephys/electrodes/z (14,) float64 the z coordinate of the channel location
general/institution () object 
general/keywords (7,) object 
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . dev/bin/activate; cat > probe2.py <<'E'
import h5py, remfile, numpy as np
from dandi.dandiapi import DandiAPIClient
c=DandiAPIClient(); ds=c.get_dandiset("000004","0.220126.1852")
a=ds.get_asset_by_path("sub-P9HMH/sub-P9HMH_ses-20060301_obj-1otd1m8_ecephys+image.nwb")
f=h5py.File(remfile.File(a.get_content_url(follow_redirects=1,strip_query=True)),'r')
for g in ['general','general/subject']:
  for k in f[g]:
    o=f[g][k]
    if isinstance(o,h5py.Dataset): print(g,k,o[()])
print('root attrs',dict(f.attrs))
for p in ['acquisition/events','acquisition/experiment_ids','units','intervals/trials','general/extracellular_ephys/electrodes']:
  print(p,dict(f[p].attrs))
  for k in f[p]:
    print('  ',k,{a:f[p][k].attrs[a] for a in f[p][k].attrs if a not in ('namespace','object_id')})
print(list(f['general/extracellular_ephys'].keys()), list(f['general/devices'].keys()) if 'general/devices' in f else None)
for k in f['general/extracellular_ephys']:
  o=f['general/extracellular_ephys'][k]
  if isinstance(o,h5py.Group) and k!='electrodes': print(k,dict(o.attrs), list(o.keys()))
print(f['acquisition/events/data'][:30]); print(f['acquisition/events/timestamps'][:10]); print(np.unique(f['acquisition/experiment_ids/data'][:],return_counts=True))
import pandas as pd
T={k:f['intervals/trials'][k][:] for k in f['intervals/trials'] }
df=pd.DataFrame(T); pd.set_option('display.width',250); pd.set_option('display.max_columns',30); print(df.head(3).T); print(df.iloc[100:103].T)
E=f['general/extracellular_ephys/electrodes']
print(pd.DataFrame({k:E[k][:] for k in E if k!='group'}))
print(f['units/electrodes'][:], f['units/electrodes_index'][:], f['units/waveform_mean_sampling_rate'][:3].ravel(), f['units/id'][:])
print(f['units/SNR'][:5], f['units/IsolationDist'][:5])
sp=f['stimulus/presentation']; k=list(sp.keys()); print(len(k),k[:3]); s=sp[k[0]]; print(dict(s.attrs), list(s.keys()), s['data'].shape)
E
python probe2.py 2>&1 | head -200
```

```
general data_collection b'learning: 80, recognition: 81'
general experiment_description b'The data contained within this file describes a new/old recogntion task performed in patients with intractable epilepsy implanted with depth electrodes and Behnke-Fried microwires in the human Medical Temporal Lobe (MTL).'
general institution b'Hunigton Memorial Hospital'
general keywords [b'Intracranial Recordings' b'Intractable Epilepsy'
 b'Single-Unit Recordings' b'Cognitive Neuroscience' b'Learning' b'Memory'
 b'Neurosurgery']
general lab b'Rutishauser'
general related_publications [b'Faraut et al. 2018, Scientific Data; Rutishauser et al. 2015, Nat Neurosci;']
general/subject age b'55'
general/subject description b'Right Mesial Temporal'
general/subject sex b'M'
general/subject species b'Human'
general/subject subject_id b'P9HMH'
root attrs {'namespace': 'core', 'neurodata_type': 'NWBFile', 'nwb_version': '2.1.0', 'object_id': '59211a0b-38e7-4dcf-98a3-756ca16dba37'}
acquisition/events {'comments': 'no comments', 'description': ' The events coorespond to the TTL markers for each trial. For the learning trials, the TTL markers \n            are the following: 55 = start of the experiment, 1 = stimulus ON, 2 = stimulus OFF, 3 = Question Screen Onset [“Is this an animal?”], \n            20 = Yes (21 = NO) during learning, 6 = End of Delay after Response, 66 = End of Experiment. For the recognition trials, \n            the TTL markers are the following: 55 = start of experiment, 1 = stimulus ON, 2 = stimulus OFF, 3 = Question Screen Onset [“Have you seen this image before?”], \n            31:36 = Confidence (Yes vs. No) response [31 (new, confident), 32 (new, probably), 33 (new, guess), 34 (old, guess), \n            35 (old, probably), 36 (old, confident)], 66 = End of Experiment', 'namespace': 'core', 'neurodata_type': 'AnnotationSeries', 'object_id': 'd81b834f-7baa-4b26-88a7-2eb5e3d93a7e'}
   data {'conversion': np.float64(1.0), 'resolution': np.float64(-1.0), 'unit': 'n/
[... 120 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; git clone -q https://github.com/rutishauserlab/recogmem-release-NWB code 2>&1|tail -2; cd code; git checkout -q 1d95162 && git log -1 --format='%H %ad'; git ls-files | grep -v -i matnwb | head -150
```

```
1d95162d2672e71dd234a31e4b8d70017a289ee3 Tue Jan 14 12:07:46 2025 -0800
.gitignore
LICENSE.txt
MANIFEST.IN
README.MD
RutishauserLabtoNWB/InHouse/README.txt
RutishauserLabtoNWB/NWBData/README.txt
RutishauserLabtoNWB/__init__.py
RutishauserLabtoNWB/assets/BrainAreaLocations.png
RutishauserLabtoNWB/assets/Cedars-Sinai.png
RutishauserLabtoNWB/assets/MATLAB_SingleNeuron.png
RutishauserLabtoNWB/assets/Python_SingleNeuron.png
RutishauserLabtoNWB/events/newolddelay/defineNOsessions_release.ini
RutishauserLabtoNWB/events/newolddelay/matlab/analysis/EpilepticSitesExclusion.m
RutishauserLabtoNWB/events/newolddelay/matlab/analysis/NWBloadDataOfBlock_release.m
RutishauserLabtoNWB/events/newolddelay/matlab/analysis/NWBneural_main.m
RutishauserLabtoNWB/events/newolddelay/matlab/analysis/NWBneural_main_addpath.m
RutishauserLabtoNWB/events/newolddelay/matlab/analysis/helpers/NO_behavior_evaluateSessionStatus.m
RutishauserLabtoNWB/events/newolddelay/matlab/analysis/helpers/NO_behavioralExclusionCriteria.m
RutishauserLabtoNWB/events/newolddelay/matlab/analysis/helpers/NO_dynamic_lowHighSplit.m
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/RutishauserLabtoNWB/events/newolddelay/matlab/analysis/helpers; for f in adjustHF.m calcZROCSlope.m getZROC_slope.m calcCumulativeD.m calcROC_AUC.m calcMeanSEOfSample.m NO_dynamic_lowHighSplit.m bootstrapMeanEqualTest.m NWB_behaviorSummary.m; do echo "=== $f"; grep -v '^\s*%' $f | grep -v '^\s*$'; done
```

```
=== adjustHF.m
function [H,F] = adjustHF(H,F, nOLD, nNEW)
for i=1:length(H)
    if H(i)==1
        H(i) = 1 - 1/(2*nOLD);
    end
    if F(i)==1
        F(i) = 1 - 1/(2*nNEW);
    end
    if H(i)==0
        H(i) = 1/(2*nOLD);
    end
    if F(i)==0
        F(i) = 1/(2*nNEW);
    end
end
=== calcZROCSlope.m
function [b, d2, s, da, Rsquare] = calcZROCSlope( typeCounters )
d = calcCumulativeD( typeCounters );
d = d(2:3, 1:end-1); %remove d' value, eliminate last datapoint (is always in right upper corner)
[... 411 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/RutishauserLabtoNWB/events/newolddelay/matlab/analysis/helpers; for f in calcDPrime.m NO_behavior_evaluateSessionStatus.m NWBbehaviorROC_prepare.m NWBbehaviorROC.m determineRecogState.m; do echo "=== $f"; grep -v '^\s*%' $f | grep -v '^\s*$'; done
```

```
=== calcDPrime.m
function [d, zH, zF,H,F, se] = calcDPrime(typeCounters, nOLD, nNEW)
H=0;
F=0;
if nOLD>0
    H = typeCounters(1)/nOLD;
end
if nNEW>0
    F = typeCounters(4)/nNEW;
end
[H,F] = adjustHF(H,F, nOLD, nNEW);
zH=norminv(H);
zF=norminv(F);
d = zH - zF; 
Hterm=H*(1-H)/(nOLD*phi(H)^2);
Fterm=F*(1-F)/(nNEW*phi(F)^2);
stdErr = Hterm + Fterm;
se = sqrt(stdErr);
function p = phi(p)
p=1/sqrt(2*pi)*exp(-1/2*norminv(p)^2);
[... 216 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/RutishauserLabtoNWB/events/newolddelay/; grep -v '^\s*%' matlab/analysis/helpers/calcEmpiricalROC.m | grep -v '^\s*$'; grep -v '^\s*%' matlab/analysis/NWBloadDataOfBlock_release.m | grep -v '^\s*$' | head -80; wc -l python/analysis/*.py
```

```
function typeCounters = calcEmpiricalROC(mode, recogState, responses)
typeCounters=[];
if mode==1
    for k=1:3
        indsOLD = find( responses == 6 - k + 1 );
        indsNEW = find( responses == k  );
        nTP = length( find( recogState(indsOLD)==1 ) );
        nFN = length( find( recogState(indsNEW)==1 ) );
        nTN = length( find( recogState(indsNEW)==0 ) );
        nFP = length( find( recogState(indsOLD)==0 ) );
        typeCounters(:,k) = [nTP nFN nTN nFP]';
    end
end
if mode==2
    for k=1:6
        if k<=3
            inds = find( responses == 6 - k + 1 );
        else
            inds = find( responses == 6 - k + 1 );
        end
[... 94 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/RutishauserLabtoNWB/events/newolddelay/python/analysis; grep -n "def \|anova\|f_oneway\|bootstrap\|ttest\|200\|1700\|1200\|window\|0.2\|1.7\|p_val\|< 0.05\|<0.05\|correct\|std\|sem" single_neuron.py helper.py behavior_all.py | head -120
```

```
single_neuron.py:4:from scipy.stats import f_oneway
single_neuron.py:14:    def __init__(self):
single_neuron.py:22:    def vs_test(self):
single_neuron.py:34:        # The window that we want to look at is from 200 ms after stim on until 1500 ms after.
single_neuron.py:37:                cat_1.append(trial.win_spike_rate(self.spike_timestamps, 200, 1700))
single_neuron.py:39:                cat_2.append(trial.win_spike_rate(self.spike_timestamps, 200, 1700))
single_neuron.py:41:                cat_3.append(trial.win_spike_rate(self.spike_timestamps, 200, 1700))
single_neuron.py:43:                cat_4.append(trial.win_spike_rate(self.spike_timestamps, 200, 1700))
single_neuron.py:45:                cat_5.append(trial.win_spike_rate(self.spike_timestamps, 200, 1700))
single_neuron.py:46:        return f_oneway(cat_1, cat_2, cat_3, cat_4, cat_5)[1]
single_neuron.py:48:    def baseline_test(self):
single_neuron.py:51:        :return: p value of the anova test
single_neuron.py:58:            stim_period.append(trial.win_spike_rate(self.spike_timestamps, 200, 1700))
single_neuron.py:59:        return f_oneway(baseline, stim_period)[1]
single_neuron.py:61:    def ms_test(self, n):
single_neuron.py:63:        A bootstrap test for new old test
single_neuron.py:64:        :param n: number of bootstraps
single_neuron.py:65:        :return: a p value of the bootstrap test
single_neuron.py:75:                new = np.append(new, trial.win_spike_rate(self.spike_timestamps, 200, 1700))
single_neuron.py:77:                old = np.append(old, trial.win_spike_rate(self.spike_timestamps, 200, 1700))
[... 86 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/RutishauserLabtoNWB/events/newolddelay/python/analysis; sed -n 20,103p single_neuron.py; sed -n 315,423p single_neuron.py; sed -n 35,90p helper.py; sed -n 145,415p helper.py; sed -n 100,170p behavior_all.py; sed -n 335,385p behavior_all.py
```

```
self.spike_timestamps = None

    def vs_test(self):
        """
        Perform statistical test to see if the neuron is a visually selective neuron
        :return: p value
        """
        trials = (trial for trial in self.trials_recog)
        cat_1 = []
        cat_2 = []
        cat_3 = []
        cat_4 = []
        cat_5 = []

        # The window that we want to look at is from 200 ms after stim on until 1500 ms after.
        for trial in trials:
            if trial.category_id == 1:
                cat_1.append(trial.win_spike_rate(self.spike_timestamps, 200, 1700))
            elif trial.category_id == 2:
                cat_2.append(trial.win_spike_rate(self.spike_timestamps, 200, 1700))
[... 623 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/RutishauserLabtoNWB/events/newolddelay/; python3 - <<'E'
import json
nb=json.load(open('python/analysis/demo/plotFigure5.ipynb'))
for c in nb['cells']:
    if c['cell_type']=='code':
        s=''.join(c['source'])
        if any(k in s for k in ['VS','MS','percent','auc','AUC','ttest','18.4','19.4']): print('-----');print(s[:2500])
E
grep -c "^\[" events/newolddelay/defineNOsessions_release.ini 2>/dev/null; head -40 defineNOsessions_release.ini; grep -c "NOID" defineNOsessions_release.ini
```

```
-----

#initialze the ConfigParser() class
config = configparser.ConfigParser()

#Get the path to the configuration file
subjects_ini = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(single_neuron.__file__))),
                                'defineNOsessions_release.ini')

filename = subjects_ini
#Read the config file
try:
    config.read(filename)
    #print ('This file was successfully read: {}\n'.format(filename))
except:
    print ('Failed to read the config file..')
    print ('Does this file exist: {}'.format(os.path.exists(filename)))


#Read the headers of the configuration file
[... 186 more lines not kept]
```

**Agent**

Paper's code read. Now the Faraut et al. 2018 Table 1 (outside input for the two `with_inputs` claims), fetched from Europe PMC.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5810422/fullTextXML" > faraut.xml; wc -c faraut.xml; python3 - <<'E'
import xml.etree.ElementTree as ET
r=ET.parse('faraut.xml').getroot()
for tw in r.iter('table-wrap'):
    lab=tw.find('label'); cap=tw.find('caption')
    print('==',tw.get('id'), lab.text if lab is not None else None, ''.join(cap.itertext())[:200] if cap is not None else '')
    rows=list(tw.iter('tr'))
    print(len(rows))
    for tr in rows[:8]+rows[-4:]:
        print([''.join(td.itertext()).strip() for td in tr])
E
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7055261/fullTextXML" > chandra.xml; wc -c chandra.xml; python3 - <<'E'
import xml.etree.ElementTree as ET
r=ET.parse('chandra.xml').getroot()
for tw in r.iter('table-wrap'):
    lab=tw.find('label');
    rows=list(tw.iter('tr'))
    print('==',tw.get('id'), lab.text if lab is not None else None, len(rows))
    for tr in rows[:4]+rows[-3:]:
        print([''.join(td.itertext()).strip() for td in tr])
E
```

Result: the fetched text is not kept.

**Agent**

I have what I need from the paper, its code, and both papers' patient tables. Now writing the helper module and surveying all 87 files.

**Agent calls Write**

```json
{
 "file_path": "entries/chandravadia-2020/recogmem.py",
 "content": "\"\"\"Loading and measures for the human MTL recognition memory data of dandiset 000004.\n\nChandravadia, Liang, Schjetnan et al. (2020), Scientific Data 7, 78, doi:10.1038/s41597-020-0415-9.\n\nEach NWB file holds one session: a trials table (100 encoding and 100 recognition trials),\nthe TTL event markers and the experiment id of each marker, the electrodes table, the units\ntable (spike times, mean waveforms, quality metrics) and the stimulus images. Files are\nstreamed from the archive at the pinned version; nothing is written to disk, and the\nstimulus images are not read (only their shape).\n\nWhere the parameters come from:\n\n- Recognition trials are the rows with stim_phase \"recog\"; the confidence response is\n  response_value minus 30 (claims file, opening comment). The paper's code reads it from the\n  events (events of the recognition experiment id between 30 and 36, minus 30;\n  helper.extract_recog_responses in rutishauserlab/recogmem-release-NWB at commit 1d95162);\n  `check_responses_against_events` compares the two.\n- \"Old\" is new_old_labels_recog == 1, as in the paper's code (claims file; tested in claim\n  new-old-label-coding).\n- Firing rate: spikes strictly inside (onset + start, onset + end) divided by the window\n  length, as `Trial.win_spike_rate` in single_neuron.py of the paper's code. The Methods'\n  window is 0.2 to 1.2 s after stimulus onset (Technical Validation, \"a 1 s long window\n  starting 200 ms after stimulus onset\"); the code's is 0.2 to 1.7 s (single_neuron.py,\n  vs_test and ms_test). Stimulus onset is the trial's start_time, as in the code\n  (extract_neuron_data_from_nwb).\n- VS cells: one-way ANOVA (scipy f_oneway) of the recognition-trial rates across the\n  stimCategory values, P < 0.05 (Technical Validation; single_neuron.py vs_test).\n- MS cells: the bootstrap test of the paper's code (single_neuron.py ms_test, the same as\n  bootstrapMeanEqualTest.m mode 1 without variance correction, Efron and Tibshirani\n  algorithm 16.2): both groups shifted to the pooled mean, each resampled with replacement\n  within itself, 1000 runs, p = fraction of runs with |mean difference| >= the observed one.\n  The seed is a standard choice (it cannot change a result beyond the resampling noise).\n- Behaviour: cumulative ROC over the six confidence levels from \"old, confident\" down,\n  hit and false alarm rates adjusted for 0 and 1 (adjustHF), AUC by the trapezoid rule with\n  (0,0) and (1,1) added (helper.cal_cumulative_d, cal_auc; calcROC_AUC.m), z-ROC slope by\n  regressing z(H) on z(F) over the five interior points (calcZROCSlope.m). High/low\n  confidence accuracy by the fixed split of NO_behavior_evaluateSessionStatus.m (high = 1\n  or 6, low = 2 to 5) and the dynamic split of helper.dynamic_split (claims file).\n\"\"\"\n\nfrom __future__ import annotations\n\nimport re\nimport xml.etree.ElementTree as ET\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nimport requests\nfrom dandi.dandiapi import DandiAPIClient\nfrom scipy import stats\n\nDANDISET_ID = \"000004\"\nDANDISET_VERSION = \"0.220126.1852\"\n\nMETHODS_WINDOW = (0.2, 1.2)   # s after stimulus onset; Technical Validation\nCODE_WINDOW = (0.2, 1.7)      # s; single_neuron.py vs_test / ms_test\nN_BOOT = 1000                 # Technical Validation, \"bootstrap comparison of means with 1,000 runs\"\nALPHA = 0.05\n\n# The paper's patient tables, read from Europe PMC's copy of the open access full texts.\nPAPER_PMC = \"PMC7055261\"      # this paper, doi:10.1038/s41597-020-0415-9, Online-only Table 1\nFARAUT_PMC = \"PMC5810422\"     # Faraut et al. 2018, doi:10.1038/sdata.2018.10, Table 1\n\n\ndef _s(x):\n    if isinstance(x, bytes):\n        return x.decode()\n    if isinstance(x, np.ndarray) and x.shape == ():\n        return _s(x[()])\n    return x\n\n\ndef list_assets():\n    \"\"\"Paths and S3 URLs of the dandiset's NWB files at the pinned version.\"\"\"\n    client = DandiAPIClient()\n    ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)\n    out = []\n    for a in ds.get_assets():\n        if a.path.endswith(\".nwb\"):\n            out.append((a.path, a.get_content_url(follow_redirects=1, strip_query=True), a.size))\n    return sorted(out)\n\n\ndef dandiset_metadata():\n    client = DandiAPIClient()\n    return client.get_dandiset(DANDISET_ID, DANDISET_VERSION).get_raw_metadata()\n\n\ndef _table(g, skip=()):\n    cols = {}\n    for k in g:\n        if k in skip or k == \"id\" or k.endswith(\"_index\"):\n            continue\n        d = g[k]\n        if not isinstance(d, h5py.Dataset) or d.ndim != 1:\n            continue\n        v = d[:]\n        if v.dtype.kind in \"OS\":\n            v = np.array([_s(x) for x in v], dtype=object)\n        cols[k] = v\n    df = pd.DataFrame(cols)\n    df.index = g[\"id\"][:]\n    return df\n\n\ndef load_session(path, url):\n    \"\"\"Read one file: everything the analyses use, without the stimulus images.\"\"\"\n    with h5py.File(remfile.File(url), \"r\") as f:\n        s = {\"path\": path}\n        for k in [\"identifier\", \"session_description\", \"session_start_time\"]:\n            s[k] = _s(f[k][()])\n        for k in [\"data_collection\", \"experiment_description\", \"institution\", \"lab\"]:\n            s[k] = _s(f[\"general\"][k][()]) if k in f[\"general\"] else None\n        subj = f[\"general/subject\"]\n        s[\"subject\"] = {k: _s(subj[k][()]) for k in subj}\n        s[\"nwb_version\"] = _s(f.attrs.get(\"nwb_version\"))\n        ev = f[\"acquisition/events\"]\n        s[\"events\"] = np.array([float(_s(x)) for x in ev[\"data\"][:]])\n        s[\"events_t\"] = ev[\"timestamps\"][:]\n        s[\"events_description\"] = _s(ev.attrs.get(\"description\"))\n        ex = f[\"acquisition/experiment_ids\"]\n        s[\"expids\"] = ex[\"data\"][:]\n        s[\"expids_t\"] = ex[\"timestamps\"][:]\n        s[\"expids_description\"] = _s(ex.attrs.get(\"description\"))\n        s[\"trials\"] = _table(f[\"intervals/trials\"])\n        s[\"trials_columns\"] = [_s(c) for c in f[\"intervals/trials\"].attrs[\"colnames\"]]\n        el = f[\"general/extracellular_ephys/electrodes\"]\n        s[\"electrodes\"] = _table(el, skip=(\"group\",))\n        s[\"electrodes_columns\"] = [_s(c) for c in el.attrs[\"colnames\"]]\n        u = f[\"units\"]\n        s[\"units_columns\"] = [_s(c) for c in u.attrs[\"colnames\"]]\n        s[\"units_datasets\"] = sorted(u.keys())\n        s[\"unit_ids\"] = u[\"id\"][:]\n        st = u[\"spike_times\"][:]\n        idx = u[\"spike_times_index\"][:]\n        s[\"spikes\"] = np.split(st, idx[:-1])\n        eidx = u[\"electrodes_index\"][:]\n        s[\"unit_electrodes\"] = np.split(u[\"electrodes\"][:], eidx[:-1])\n        for k in [\"origClusterID\", \"SNR\", \"IsolationDist\", \"IsolDist\"]:\n            if k in u:\n                s[k] = u[k][:]\n        s[\"waveform_rate\"] = u[\"waveform_mean_sampling_rate\"][:].ravel() if \"waveform_mean_sampling_rate\" in u else None\n        for k in [\"waveform_mean_encoding\", \"waveform_mean_recognition\"]:\n            s[k + \"_shape\"] = u[k].shape if k in u else None\n        pres = f[\"stimulus/presentation\"] if \"stimulus/presentation\" in f else {}\n        s[\"stimulus_series\"] = {k: (pres[k][\"data\"].shape if \"data\" in pres[k] else None) for k in pres}\n    m = re.match(r\"([A-Z]+)(\\d+)_(\\d+)$\", s[\"identifier\"])\n    s[\"label\"] = m.group(1) + m.group(2)\n    s[\"session_id\"] = int(m.group(3))\n    m2 = re.search(r\"ID:\\s*(\\d+)\", s[\"session_description\"] or \"\")\n    s[\"session_id_description\"] = int(m2.group(1)) if m2 else None\n    return s\n\n\ndef load_all(assets, workers=6):\n    with ThreadPoolExecutor(workers) as ex:\n        sessions = list(ex.map(lambda a: load_session(a[0], a[1]), assets))\n    return sorted(sessions, key=lambda s: s[\"session_id\"])\n\n\ndef site(label):\n    \"\"\"CS (labels H or C) or TWH (labels T), as the Figure 5 legend defines.\"\"\"\n    return \"TWH\" if label.startswith(\"T\") else \"CS\"\n\n\n# --- the paper's patient tables ------------------------------------------------------------\n\ndef pmc_table(pmc, label):\n    \"\"\"Rows of the table with this label in Europe PMC's full-text XML of an article.\"\"\"\n    r = requests.get(f\"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmc}/fullTextXML\", timeout=60)\n    r.raise_for_status()\n    root = ET.fromstring(r.content)\n    for tw in root.iter(\"table-wrap\"):\n        lab = tw.find(\"label\")\n        if lab is not None and lab.text and lab.text.strip() == label:\n            return [[\"\".join(td.itertext()).strip() for td in tr] for tr in tw.iter(\"tr\")]\n    raise ValueError(f\"{label} not found in {pmc}\")\n\n\ndef patient_table(pmc, label):\n    \"\"\"Subject rows of a patient table: one row per (subject, session) with variant, age, sex, diagnosis.\"\"\"\n    rows = []\n    for r in pmc_table(pmc, label):\n        if len(r) < 7 or not re.match(r\"^[HCT]\\d+$\", r[0]):\n            continue\n        sids = [int(x) for x in re.findall(r\"\\d+\", r[2])]\n        vars_ = [int(x) for x in re.findall(r\"\\d+\", r[3])]\n        for i, sid in enumerate(sids):\n            rows.append({\"label\": r[0], \"n_sessions\": int(r[1]), \"session_id\": sid,\n                         \"variant\": vars_[i] if i < len(vars_) else None,\n                         \"age\": int(r[4]), \"sex\": r[5], \"diagnosis\": r[6]})\n    return pd.DataFrame(rows)\n\n\ndef table_label(label):\n    \"\"\"File labels are P9HMH, P24CS, TWH088; the tables write H09, C24, T88.\"\"\"\n    m = re.match(r\"P(\\d+)(HMH|CS)$\", label)\n    if m:\n        return (\"H\" if m.group(2) == \"HMH\" else \"C\") + f\"{int(m.group(1)):02d}\"\n    m = re.match(r\"TWH(\\d+)$\", label)\n    if m:\n        return f\"T{int(m.group(1))}\"\n    return label\n\n\n# --- trials and behaviour ------------------------------------------------------------------\n\ndef recog_trials(s):\n    t = s[\"trials\"]\n    r = t[t[\"stim_phase\"] == \"recog\"].copy()\n    r[\"conf\"] = r[\"response_value\"] - 30\n    r[\"label\"] = pd.to_numeric(r[\"new_old_labels_recog\"], errors=\"coerce\")\n    return r\n\n\ndef check_responses_against_events(s):\n    \"\"\"The responses the paper's code reads from the events (recognition experiment id, codes 30 to 36).\"\"\"\n    ids = np.unique(s[\"expids\"])\n    recog_id = ids[1] if len(ids) > 1 else np.nan\n    ev = s[\"events\"][(s[\"expids\"] == recog_id) & (s[\"events\"] >= 30) & (s[\"events\"] <= 36)] - 30\n    return ev\n\n\ndef typecounters(label, conf):\n    \"\"\"Counts of old (label 1) and new (label 0) trials at each confidence, from 6 ('old, confident') down.\"\"\"\n    old = np.array([np.sum((conf == c) & (label == 1)) for c in range(6, 0, -1)])\n    new = np.array([np.sum((conf == c) & (label == 0)) for c in range(6, 0, -1)])\n    return old, new\n\n\ndef adjust_hf(h, f, n_old, n_new):\n    \"\"\"adjustHF.m: rates of 0 or 1 moved by half a trial.\"\"\"\n    h = np.where(h == 1, 1 - 1 / (2 * n_old), h)\n    f = np.where(f == 1, 1 - 1 / (2 * n_new), f)\n    h = np.where(h == 0, 1 / (2 * n_old), h)\n    f = np.where(f == 0, 1 / (2 * n_new), f)\n    return h, f\n\n\ndef cumulative_roc(label, conf):\n    \"\"\"Hit and false alarm rates at the six cumulative criteria (helper.cal_cumulative_d).\"\"\"\n    old, new = typecounters(label, conf)\n    n_old, n_new = old.sum(), new.sum()\n    h = np.cumsum(old) / n_old\n    f = np.cumsum(new) / n_new\n    return adjust_hf(h, f, n_old, n_new)\n\n\ndef auc(h, f):\n    \"\"\"helper.cal_auc / calcROC_AUC.m: trapezoid rule with (0,0) and (1,1) added.\"\"\"\n    tp, fp = list(h), list(f)\n    if tp[0] != 0 or fp[0] != 0:\n        tp, fp = [0.0] + tp, [0.0] + fp\n    if tp[-1] != 1 or fp[-1] != 1:\n        tp, fp = tp + [1.0], fp + [1.0]\n    a = 0.0\n    for i in range(1, len(tp)):\n        a += (fp[i] - fp[i - 1]) * tp[i - 1] + 0.5 * (tp[i] - tp[i - 1]) * (fp[i] - fp[i - 1])\n    return a\n\n\ndef zroc_slope(h, f):\n    \"\"\"calcZROCSlope.m: regression of z(H) on z(F) over the first five cumulative points.\"\"\"\n    zh, zf = stats.norm.ppf(h[:5]), stats.norm.ppf(f[:5])\n    return np.polyfit(zf, zh, 1)[0]\n\n\ndef accuracy_fixed_split(label, conf):\n    \"\"\"NO_behavior_evaluateSessionStatus.m (useDynamicSplitMode=0): high = 1 or 6, low = 2 to 5.\n    Returns percent correct among high and among low confidence responses (nan when none).\"\"\"\n    correct = ((conf <= 3) & (label == 0)) | ((conf >= 4) & (label == 1))\n    hi = (conf == 1) | (conf == 6)\n    lo = (conf >= 2) & (conf <= 5)\n    f = lambda m: 100 * correct[m].mean() if m.sum() else np.nan\n    return f(hi), f(lo)\n\n\ndef accuracy_dynamic_split(label, conf):\n    \"\"\"helper.dynamic_split and its use in behavior_all.py, as the Python code has it.\n    Mode 1 is high = 1 or 6, low = 2, 3 or 4 (the Python code's low old responses are 4 only;\n    NO_dynamic_lowHighSplit.m has 4 or 5); mode 2 is high = 1, 2, 5, 6, low = 3 or 4.\"\"\"\n    counts = np.array([np.sum(conf == k) for k in range(1, 7)])\n    c1, c2, c3 = counts[0] + counts[5], counts[1] + counts[4], counts[2] + counts[3]\n    split = np.array([c1 - (c2 + c3), (c1 + c2) - c3])\n    mode = int(np.where(np.abs(split) == np.min(np.abs(split)))[0][0]) + 1\n    if counts[0] == 0 or counts[5] == 0:\n        mode = 2\n    if counts[1] == 0 or counts[4] == 0:\n        mode = 1\n    old, new = label == 1, label == 0\n    if mode == 1:\n        hi_old, lo_old = conf >= 6, conf == 4\n        hi_new, lo_new = conf <= 1, (conf == 2) | (conf == 3)\n    else:\n        hi_old, lo_old = conf >= 5, conf == 4\n        hi_new, lo_new = conf <= 2, conf == 3\n    tp_hi, tp_lo = (old & hi_old).sum(), (old & lo_old).sum()\n    tn_hi, tn_lo = (new & hi_new).sum(), (new & lo_new).sum()\n    n_hi = ((old | new) & (hi_old | hi_new)).sum()\n    n_lo = ((old | new) & (lo_old | lo_new)).sum()\n    hi = 100 * (tp_hi + tn_hi) / n_hi if n_hi else np.nan\n    lo = 100 * (tp_lo + tn_lo) / n_lo if n_lo else np.nan\n    return hi, lo, mode\n\n\n# --- single neurons ------------------------------------------------------------------------\n\ndef window_rates(spikes, onsets, window):\n    \"\"\"Spike counts strictly inside (onset + start, onset + end), divided by the window length.\"\"\"\n    sp = np.sort(spikes)\n    lo = np.searchsorted(sp, onsets + window[0], side=\"right\")\n    hi = np.searchsorted(sp, onsets + window[1], side=\"left\")\n    return (hi - lo) / (window[1] - window[0])\n\n\ndef vs_p(rates, categories):\n    groups = [rates[categories == c] for c in np.unique(categories)]\n    if len(groups) < 2 or all(np.all(g == g[0]) for g in groups if len(g)):\n        return np.nan\n    return stats.f_oneway(*groups).pvalue\n\n\ndef bootstrap_p(a, b, rng, n_boot=N_BOOT):\n    \"\"\"Two-tailed bootstrap test of equal means (single_neuron.py ms_test; bootstrapMeanEqualTest.m).\"\"\"\n    a, b = np.asarray(a, float), np.asarray(b, float)\n    if len(a) == 0 or len(b) == 0:\n        return np.nan\n    m = np.mean(np.concatenate([a, b]))\n    at, bt = a - a.mean() + m, b - b.mean() + m\n    ia = rng.integers(0, len(a), size=(n_boot, len(a)))\n    ib = rng.integers(0, len(b), size=(n_boot, len(b)))\n    t = np.abs(at[ia].mean(1) - bt[ib].mean(1))\n    return np.mean(t >= abs(a.mean() - b.mean()))\n\n\ndef isi_violation_fraction(spikes, sort=True, limit=0.003):\n    sp = np.sort(spikes) if sort else np.asarray(spikes)\n    if len(sp) < 2:\n        return np.nan\n    return np.mean(np.diff(sp) < limit)\n"
}
```

```
File created successfully at: entries/chandravadia-2020/recogmem.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR; . dev/bin/activate; cat > survey.py <<'E'
import sys,time,pickle,resource
sys.path.insert(0,'entries/chandravadia-2020')
import recogmem as rm
t=time.time(); A=rm.list_assets(); print(len(A), time.time()-t)
t=time.time(); s=rm.load_session(*A[0][:2]); print('one',time.time()-t)
t=time.time(); S=rm.load_all([a[:2] for a in A], workers=8); print('all',time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB')
pickle.dump(S,open('S.pkl','wb'))
E
python survey.py
```

```
87 9.343132972717285
one 1.0396764278411865
all 62.97884559631348 0.27444 GB
Shell cwd was reset to
```

**Agent**

All 87 files load in about a minute (0.3 GB peak). Surveying contents:

**Agent calls Bash**

```bash
cd $TMPDIR; . dev/bin/activate; cat > s2.py <<'E'
import sys,pickle,numpy as np,pandas as pd,collections
sys.path.insert(0,'entries/chandravadia-2020')
import recogmem as rm
S=pickle.load(open('S.pkl','rb'))
pd.set_option('display.width',250); pd.set_option('display.max_rows',200)
rows=[]
for s in S:
    t=s['trials']; r=rm.recog_trials(s)
    rows.append(dict(id=s['identifier'],sid=s['session_id'],sid_d=s['session_id_description'],label=s['label'],date=s['session_start_time'][:10],
      ntr=len(t),nlearn=(t.stim_phase=='learn').sum(),nrec=(t.stim_phase=='recog').sum(),
      lab=dict(collections.Counter(r.new_old_labels_recog)), ncat=t.stimCategory.nunique(), cats=tuple(sorted(t.stimCategory.unique())),
      nunits=len(s['unit_ids']), nel=len(s['electrodes']), age=s['subject'].get('age'), sex=s['subject'].get('sex'),
      expids=tuple(np.unique(s['expids']).astype(int)), dc=s['data_collection'], wr=tuple(np.unique(s['waveform_rate'])), stim=s['stimulus_series'],
      cols=len(s['trials_columns']), ucols=tuple(s['units_columns'])))
df=pd.DataFrame(rows); print(df.drop(columns=['stim','ucols','dc']).to_string())
print(df.nunits.sum(), df.label.nunique(), len(df))
print(collections.Counter(df.ucols)); print(collections.Counter(map(str,df.stim)))
print(collections.Counter(df.dc))
print(collections.Counter(tuple(s['trials_columns']) for s in S))
print(collections.Counter(tuple(s['electrodes_columns']) for s in S))
print(S[0]['subject'])
E
python s2.py
```

```
id   sid  sid_d label        date  ntr  nlearn  nrec                 lab  ncat             cats  nunits  nel age sex    expids          wr  cols
0       H09_5     5      5   H09  2006-03-01  200     100   100  {'0': 50, '1': 50}     5  (1, 2, 3, 4, 5)      24   14  55   M  (80, 81)  (98400.0,)    13
1       H09_6     6      6   H09  2006-03-01  200     100   100  {'0': 50, '1': 50}     5  (1, 2, 3, 4, 5)      19   13  55   M  (83, 84)  (98400.0,)    13
2       H10_7     7      7   H10  2006-09-01  200     100   100  {'0': 50, '1': 50}     5  (1, 2, 3, 4, 5)      38   18  37   M  (80, 81)  (98400.0,)    13
3       H11_9     9      9   H11  2006-11-01  200     100   100  {'0': 50, '1': 50}     5  (1, 2, 3, 4, 5)      25    9  16   M  (80, 81)  (98400.0,)    13
4      H14_17    17     17   H14  2007-06-01  200     100   100  {'0': 50, '1': 50}     5  (1, 2, 3, 4, 5)      23    9  31   M  (83, 84)  (98400.0,)    13
5      H14_18    18     18   H14  2007-06-01  150      50   100  {'0': 50, '1': 50}     5  (1, 2, 3, 4, 5)      33   10  31   M  (80, 81)  (98400.0,)    13
6      H15_20    20     20   H15  2007-09-01  150      50   100  {'0': 50, '1': 50}     5  (1, 2, 3, 4, 5)      20   11  45   M  (80, 81)  (98400.0,)    13
7      H15_21    21     21   H15  2007-09-01  150      50   100  {'0': 50, '1': 50}     5  (1, 2, 3, 4, 5)      14    7  45   M  (83, 84)  (98400.0,)    13
8      H16_23    23     23   H16  2007-10-01  150      50   100  {'0': 50, '1': 50}     5  (1, 2, 3, 4, 5)      18    9  34   F  (83, 84)  (98400.0,)    13
9      H16_24    24     24   H16  2007-10-01  200     100   100  {'0': 50, '1': 50}     5  (1, 2, 3, 4, 5)      21   18  34   F  (80, 81)  (98400.0,)    13
10     H18_26    26     26   H18  2008-06-01  150      50   100  {'0': 50, '1': 50}     5  (1, 2, 3, 4, 5)      33   16  40   M  (80, 81)  (98400.0,)    13
11     H19_27    27     27   H19  2008-06-01  150      50   100  {'0': 50, '1': 50}     5  (1, 2, 3, 4, 5)      16    6  34   M  (83, 84)  
[... 83 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . dev/bin/activate; cat > s3.py <<'E'
import sys,pickle,numpy as np,pandas as pd,collections,hashlib
sys.path.insert(0,'entries/chandravadia-2020')
import recogmem as rm
S=pickle.load(open('S.pkl','rb'))
# duplicates
h=collections.defaultdict(list)
for s in S:
    for i,sp in enumerate(s['spikes']):
        h[hashlib.md5(np.asarray(sp).tobytes()).hexdigest()].append((s['session_id'],i))
d=[v for v in h.values() if len(v)>1]; print('dup trains',len(d), collections.Counter(tuple(sorted(set(x[0] for x in v))) for v in d))
# responses vs events
bad=0
for s in S:
    r=rm.recog_trials(s); ev=rm.check_responses_against_events(s)
    if len(ev)!=len(r) or not np.array_equal(ev, r.conf.values): bad+=1; print('resp mismatch',s['session_id'],len(ev),len(r), collections.Counter(r.conf))
print('resp mismatches',bad)
print(collections.Counter(np.concatenate([rm.recog_trials(s).conf.values for s in S])))
print(collections.Counter(np.concatenate([s['trials'][s['trials'].stim_phase=='learn'].response_value.values for s in S])))
# label coding check
for s in S[:3]+S[-2:]:
    t=s['trials']; L=set(t[t.stim_phase=='learn'].external_image_file); r=rm.recog_trials(s)
    inL=r.external_image_file.isin(L)
    print(s['session_id'], pd.crosstab(r.label, inL).values.tolist(), pd.crosstab(r.label, r.conf>=4).values.tolist())
# electrodes completeness
for col in ['x','y','z','imp','location','filtering','origChannel']:
    vals=np.concatenate([s['electrodes'][col].values.astype(object) for s in S])
    nn=sum(1 for v in vals if v is None or (isinstance(v,float) and np.isnan(v)) or v=='')
    print(col, len(vals), 'missing',nn, collections.Counter(vals).most_common(4) if col in('location','filtering') else '')
locs=collections.Counter()
for s in S:
    for e in s['unit_electrodes']: locs[s['electrodes']['location'].values[e[0]] if len(e) else None]+=1
print(locs)
print('units n electrodes', collections.Counter(len(e) for s in S for e in s['unit_electrodes']))
for k in ['SNR','IsolationDist','origClusterID']:
    v=np.concatenate([s[k] for s in S]); print(k, len(v), np.isfinite(v).sum(), np.nanmin(v), np.nanmax(v))
uns=sum(1 for s in S for sp in s['spikes'] if np.any(np.diff(sp)<0)); print('unsorted trains',uns)
isi=np.array([rm.isi_violation_fraction(sp) for s in S for sp in s['spikes']]); print('isi', np.nanmax(isi), np.mean(isi<0.03), np.sum(isi>=0.03), np.sum(np.isnan(isi)))
isi2=np.array([rm.isi_violation_fraction(sp,sort=False) for s in S for sp in s['spikes']]); print('isi stored', np.mean(isi2<0.03))
# events codes
allc=collections.Counter(np.concatenate([s['events'] for s in S])); print(sorted(allc.items()))
print([ (s['session_id'], len(s['events']), len(s['expids']), np.array_equal(s['events_t'],s['expids_t'])) for s in S if len(s['events'])!=len(s['expids']) or not np.array_equal(s['events_t'],s['expids_t'])])
E
python s3.py
```

```
dup trains 66 Counter({(54, 55): 32, (43, 44): 23, (38, 39): 11})
resp mismatches 0
Counter({np.float64(1.0): 2544, np.float64(6.0): 2527, np.float64(2.0): 1039, np.float64(3.0): 933, np.float64(5.0): 894, np.float64(4.0): 763})
Counter({np.float64(1.0): 6570, np.float64(0.0): 1777})
5 [[50, 0], [0, 50]] [[37, 13], [15, 35]]
6 [[50, 0], [0, 50]] [[34, 16], [14, 36]]
7 [[50, 0], [0, 50]] [[27, 23], [17, 33]]
2009 [[50, 0], [0, 50]] [[16, 34], [7, 43]]
2011 [[50, 0], [0, 50]] [[43, 7], [7, 43]]
x 887 missing 99 
y 887 missing 99 
z 887 missing 99 
imp 887 missing 887 
location 887 missing 0 [('Right Amygdala', 281), ('Left Amygdala', 218), ('Right Hippocampus', 200), ('Left Hippocampus', 188)]
filtering 887 missing 0 [('300-3000Hz', 887)]
origChannel 887 missing 0 
Counter({'Right Amygdala': 594, 'Left Amygdala': 498, 'Right Hippocampus': 407, 'Left Hippocampus': 365})
units n electrodes Counter({1: 1864})
SNR 1864 1778 0.3787592753889356 inf
IsolationDist 1864 1371 4.513248116413887 8.081694408988397e+32
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR; . dev/bin/activate; cat > s4.py <<'E'
import sys,pickle,numpy as np,pandas as pd,collections
sys.path.insert(0,'entries/chandravadia-2020')
import recogmem as rm
S={s['session_id']:s for s in pickle.load(open('S.pkl','rb'))}
s=S[132]; print(s['electrodes']); print([ (u, e.tolist(), c) for u,e,c in zip(s['unit_ids'], s['unit_electrodes'], s['origClusterID'])])
print(144 in S)
for a,b in [(54,55),(43,44),(38,39)]:
    ta,tb=S[a]['trials'],S[b]['trials']
    print(a,b,len(ta),len(tb), np.array_equal(ta.start_time.values[:min(len(ta),len(tb))], tb.start_time.values[:min(len(ta),len(tb))]), np.array_equal(S[a]['events'],S[b]['events']) if len(S[a]['events'])==len(S[b]['events']) else 'difflen', (ta.external_image_file.values[:5], tb.external_image_file.values[:5]))
    print(S[a]['electrodes'].origChannel.tolist(), S[b]['electrodes'].origChannel.tolist(), S[a]['events_t'][:2], S[b]['events_t'][:2])
for sid,s in S.items():
    c=collections.Counter(s['events'])
    odd={k:v for k,v in c.items() if k not in (1,2,3,6,20,21,31,32,33,34,35,36,55,66)}
    if odd or c[55]!=2 or c[66]!=2: print(sid, odd, c[55], c[66])
E
python s4.py
```

```
Sun Nov 15 07:32:11 UTC 2026
    filtering                      group_name  imp  ...      x     y      z
0  300-3000Hz  Neuralynx-Atlas-microwires-146  NaN  ... -18.26 -3.03 -17.02
1  300-3000Hz  Neuralynx-Atlas-microwires-148  NaN  ... -18.26 -3.03 -17.02
2  300-3000Hz  Neuralynx-Atlas-microwires-149  NaN  ... -18.26 -3.03 -17.02
3  300-3000Hz  Neuralynx-Atlas-microwires-150  NaN  ... -18.26 -3.03 -17.02
4  300-3000Hz  Neuralynx-Atlas-microwires-177  NaN  ...  22.10 -5.13 -15.40
5  300-3000Hz  Neuralynx-Atlas-microwires-181  NaN  ...  22.10 -5.13 -15.40
6  300-3000Hz  Neuralynx-Atlas-microwires-182  NaN  ...  22.10 -5.13 -15.40
7  300-3000Hz  Neuralynx-Atlas-microwires-183  NaN  ...  22.10 -5.13 -15.40

[8 rows x 8 columns]
[(np.int32(0), [0], np.int32(614)), (np.int32(1), [1], np.int32(776)), (np.int32(2), [2], np.int32(821)), (np.int32(3), [3], np.int32(1093)), (np.int32(4), [4], np.int32(551)), (np.int32(5), [5], np.int32(1422)), (np.int32(6), [6], np.int32(527)), (np.int32(7), [7], np.int32(529))]
False
54 55 200 200 False False (<StringArray>
['newolddelay\smallAnimal\7.jpg',     'newolddelay\phones\34.jpg',
 'newolddelay\landscapes\31.jpg',   'newolddelay\mobility\30.jpg',
   'newolddelay\mobility\13.jpg']
Length: 5, dtype: str, <StringArray>
['newolddelay\smallAnimal\7.jpg',     'newolddelay\phones\34.jpg',
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s "https://api.osf.io/v2/nodes/hv7ja/files/osfstorage/" | python3 -c "
import json,sys; d=json.load(sys.stdin)
for x in d.get('data',[]): print(x['attributes']['kind'], x['attributes']['name'], x['attributes'].get('size'), x['relationships']['files']['links']['related']['href'] if x['attributes']['kind']=='folder' else '')
print(d.get('links',{}).get('meta'))" 2>&1 | head -30
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; . dev/bin/activate; timeout 300 python - <<'E'
import requests, zipfile, remfile, json
d=requests.get("https://api.osf.io/v2/nodes/hv7ja/files/osfstorage/").json()
for x in d['data']:
    if x['attributes']['name'].endswith('.zip'):
        url=x['links']['download']; r=requests.head(url,allow_redirects=True); print(x['attributes']['name'], r.status_code, r.headers.get('Accept-Ranges'), r.url[:80])
        try:
            z=zipfile.ZipFile(remfile.File(r.url)); n=z.namelist(); print(len(n)); print([m for m in n if m.endswith('.nwb')][:100]); print([m for m in n if '144' in m][:10])
        except Exception as e: print('err',e)
E
```

```
NativeData.zip 200 None https://files.osf.io/v1/resources/hv7ja/providers/osfstorage/5df7a4899a7ce3000c6
2244
[]
[]
NWBData.zip 200 None https://files.osf.io/v1/resources/hv7ja/providers/osfstorage/5ed9d16408aad3002d4
88
['NWBData/P10HMH_NOID7.nwb', 'NWBData/P11HMH_NOID9.nwb', 'NWBData/P14HMH_NOID17.nwb', 'NWBData/P14HMH_NOID18.nwb', 'NWBData/P15HMH_NOID20.nwb', 'NWBData/P15HMH_NOID21.nwb', 'NWBData/P16HMH_NOID23.nwb', 'NWBData/P16HMH_NOID24.nwb', 'NWBData/P17HMH_NOID32.nwb', 'NWBData/P18HMH_NOID26.nwb', 'NWBData/P19HMH_NOID27.nwb', 'NWBData/P19HMH_NOID28.nwb', 'NWBData/P21HMH_NOID38.nwb', 'NWBData/P21HMH_NOID39.nwb', 'NWBData/P21HMH_NOID41.nwb', 'NWBData/P23HMH_NOID43.nwb', 'NWBData/P23HMH_NOID44.nwb', 'NWBData/P23HMH_NOID47.nwb', 'NWBData/P24CS_NOID59.nwb', 'NWBData/P24CS_NOID60.nwb', 'NWBData/P25CS_NOID61.nwb', 'NWBData/P25CS_NOID63.nwb', 'NWBData/P26CS_NOID64.nwb', 'NWBData/P26CS_NOID66.nwb', 'NWBData/P27CS_NOID67.nwb', 'NWBData/P27HMH_NOID58.nwb', 'NWBData/P28HMH_NOID48.nwb', 'NWBData/P29CS_NOID69.nwb', 'NWBData/P29CS_NOID70.nwb', 'NWBData/P29HMH_NOID49.nwb', 'NWBData/P31CS_NOID73.nwb', 'NWBData/P31HMH_NOID50.nwb', 'NWBData/P32CS_NOID74.nwb', 'NWBData/P33CS_NOID76.nwb', 'NWBData/P33CS_NOID77.nwb', 'NWBData/P33CS_NOID78.nwb', 'NWBData/P33HMH_NOID52.nwb', 'NWBData/P34CS_NOID85.nwb', 'NWBData/P37CS_NOID96.nwb', 'NWBData/P38CS_NOID102.nwb', 'NWBData/P39CS_NOID100.nwb', 'NWBData/P39CS_NOID93.nwb', 'NWBData/P40CS_NOID101.nwb', 'NWBData/P42CS_NOID111.nwb', 'NWBData/P42CS_NOID112.nwb', 'NWBData/P42HMH_NOID54.nwb', 'NWBData/P42HMH_NOID55.nwb', 'NWBData/P43CS_NOID113.nwb', 'NWBData/P43HMH_NOID56.nwb', 'NWBData/P44CS_NOID114.nwb', 'NWBData/P44HMH_NOID68.nwb', 'NWBData/P47CS_NOID115.nwb', 'NWBData/P47HMH_NOID92.nwb', 'NWBData/P47HMH_NOID97.nwb', 'NWBData/P48CS_NOID116.nwb', 'NWBData/P48HMH_NOID99.nwb', 'NWBData/P49CS_NOID117.nwb', 'NWBData/P49CS_NOID118.nwb', 'NWBData/P51CS_NOID119.nwb', 'NWBData/P51CS_NOID120.nwb', 'NWBData/P51HMH_NOID104.nwb', 'NWBData/P51HMH_NOID105.nwb
[... 2 more lines not kept]
```

**Agent**

OSF's NWBData.zip lists the same 87 sessions; session 144 (the Figure 3 example neuron) is in neither deposit. Now prototyping the behavioural and single-neuron analyses on the cached survey data.

**Agent calls Bash**

```bash
cd $TMPDIR; . dev/bin/activate; cat > s5.py <<'E'
import sys,pickle,numpy as np,pandas as pd,collections,time
sys.path.insert(0,'entries/chandravadia-2020')
import recogmem as rm
from scipy import stats
S=pickle.load(open('S.pkl','rb'))
rows=[]
for s in S:
    r=rm.recog_trials(s); L=r.label.values; C=r.conf.values
    h,f=rm.cumulative_roc(L,C)
    hi,lo=rm.accuracy_fixed_split(L,C); dh,dl,mode=rm.accuracy_dynamic_split(L,C)
    rows.append(dict(sid=s['session_id'],site=rm.site(s['label']),auc=rm.auc(h,f),slope=rm.zroc_slope(h,f),hi=hi,lo=lo,dhi=dh,dlo=dl,mode=mode))
B=pd.DataFrame(rows)
print(B.auc.mean(), B.auc.std(ddof=1), B.groupby('site').auc.agg(['mean','std','count']))
print(stats.ttest_ind(B.auc[B.site=='CS'],B.auc[B.site=='TWH'],equal_var=False))
print(B.slope.mean(), stats.ttest_1samp(B.slope,1), stats.wilcoxon(B.slope-1))
x=B.dropna(subset=['hi','lo']); print(len(x), x.hi.mean(), x.lo.mean(), stats.ttest_rel(x.hi,x.lo))
x=B.dropna(subset=['dhi','dlo']); print(len(x), x.dhi.mean(), x.dlo.mean(), stats.ttest_rel(x.dhi,x.dlo))
# reversed label AUC
t=time.time()
rng=np.random.default_rng(0)
U=[]
for s in S:
    r=rm.recog_trials(s); on=r.start_time.values; cat=r.stimCategory.values; L=r.label.values; C=r.conf.values
    corr=((C<=3)&(L==0))|((C>=4)&(L==1))
    for i,sp in enumerate(s['spikes']):
        d=dict(sid=s['session_id'],site=rm.site(s['label']),unit=i)
        for wn,w in [('m',rm.METHODS_WINDOW),('c',rm.CODE_WINDOW)]:
            fr=rm.window_rates(sp,on,w)
            d['vs_'+wn]=rm.vs_p(fr,cat)
            d['ms_'+wn]=rm.bootstrap_p(fr[L==0],fr[L==1],rng)
            d['msc_'+wn]=rm.bootstrap_p(fr[(L==0)&corr],fr[(L==1)&corr],rng)
        U.append(d)
U=pd.DataFrame(U); print(time.time()-t)
for c in ['vs_m','vs_c','ms_m','ms_c','msc_m','msc_c']: print(c,(U[c]<0.05).sum(), 100*(U[c]<0.05).mean(), U[c].isna().sum())
print('dual', ((U.vs_m<.05)&(U.ms_m<.05)).sum(), ((U.vs_c<.05)&(U.msc_c<.05)).sum())
for st,g in U.groupby('site'): print(st,len(g), 100*(g.vs_m<.05).mean(),100*(g.ms_m<.05).mean(),100*((g.vs_m<.05)&(g.ms_m<.05)).mean(), '| code',100*(g.vs_c<.05).mean(),100*(g.msc_c<.05).mean(),100*((g.vs_c<.05)&(g.msc_c<.05)).mean())
E
python s5.py
```

```
entries/chandravadia-2020/recogmem.py:268: RankWarning: Polyfit may be poorly conditioned
  return np.polyfit(zf, zh, 1)[0]
entries/chandravadia-2020/recogmem.py:268: RankWarning: Polyfit may be poorly conditioned
  return np.polyfit(zf, zh, 1)[0]
entries/chandravadia-2020/recogmem.py:268: RankWarning: Polyfit may be poorly conditioned
  return np.polyfit(zf, zh, 1)[0]
entries/chandravadia-2020/recogmem.py:268: RankWarning: Polyfit may be poorly conditioned
  return np.polyfit(zf, zh, 1)[0]
entries/chandravadia-2020/recogmem.py:268: RankWarning: Polyfit may be poorly conditioned
  return np.polyfit(zf, zh, 1)[0]
0.7527160919540228 0.09378489412450672           mean       std  count
site                           
CS    0.760152  0.085498     78
TWH   0.688272  0.137784      9
TtestResult(statistic=np.float64(1.5314060655167412), pvalue=np.float64(0.1610853356114797), df=np.float64(8.724855017391024))
0.7256674124520925 TtestResult(statistic=np.float64(-6.751631858525214), pvalue=np.float64(1.6307195195154453e-09), df=np.int64(86)) WilcoxonResult(statistic=np.float64(488.0), pvalue=np.float64(1.5858167031143077e-09))
84 80.14573931366803 60.91856233209954 TtestResult(statistic=np.float64(10.155954563740682), pvalue=np.float64(3.2235735607435254e-16), df=np.int64(83))
82 78.20024196067665 60.79976974408238 TtestResult(statistic=np.float64(7.8773885215430175), pvalue=np.float64(1.3095510871498402e-11), df=np.int64(81))
3.1998677253723145
vs_m 332 17.811158798283262 6
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/chandravadia-2020; cat >> recogmem.py <<'E'


# --- checks of the files -------------------------------------------------------------------

def variant_from_images(s):
    """Task variant from the image directory of the trials (newolddelay, newolddelay2, newolddelay3),
    the directories of Table 2 of Faraut et al. 2018."""
    dirs = {re.split(r"[\\/]", p)[0].lower() for p in s["trials"]["external_image_file"]}
    out = {"newolddelay": 1, "newolddelay2": 2, "newolddelay3": 3}
    v = {out.get(d) for d in dirs}
    return v.pop() if len(v) == 1 else None


def trial_event_order(s, learn_codes=(20, 21), recog_codes=tuple(range(31, 37))):
    """For each stimulus onset (1) in the events, whether the next four codes are offset (2),
    question (3), a response of the phase's kind and end of trial (6). Returns (n onsets, n bad)."""
    ids = np.unique(s["expids"])
    n, bad = 0, 0
    for k, eid in enumerate(ids):
        ev = s["events"][s["expids"] == eid]
        resp = learn_codes if k == 0 else recog_codes
        for i in np.where(ev == 1)[0]:
            n += 1
            nxt = ev[i + 1:i + 5]
            ok = len(nxt) == 4 and nxt[0] == 2 and nxt[1] == 3 and nxt[2] in resp and nxt[3] == 6
            bad += not ok
    return n, bad


def duplicated_trains(sessions):
    """Units whose spike trains are identical to a unit of an earlier file (by session id).
    Returns a set of (session_id, unit index) to drop when each train is counted once, and the
    pairs of sessions that share trains with their counts."""
    seen, drop, pairs = {}, set(), {}
    for s in sessions:
        for i, sp in enumerate(s["spikes"]):
            key = (len(sp), np.asarray(sp).tobytes())
            if key in seen:
                drop.add((s["session_id"], i))
                p = (seen[key][0], s["session_id"])
                pairs[p] = pairs.get(p, 0) + 1
            else:
                seen[key] = (s["session_id"], i)
    return drop, pairs
E
```

```
(Bash completed with no output)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/chandravadia-2020/recogmem.py",
 "old_string": "    zh, zf = stats.norm.ppf(h[:5]), stats.norm.ppf(f[:5])\n    return np.polyfit(zf, zh, 1)[0]",
 "new_string": "    zh, zf = stats.norm.ppf(h[:5]), stats.norm.ppf(f[:5])\n    if np.unique(zf).size < 2:\n        return np.nan\n    return stats.linregress(zf, zh).slope"
}
```

```
The file entries/chandravadia-2020/recogmem.py has been updated successfully.
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build_nb.py",
 "content": "import nbformat as nbf\nimport sys\n\ncells = []\n\n\ndef md(s, tags=None):\n    c = nbf.v4.new_markdown_cell(s.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\ndef code(s, tags=None):\n    c = nbf.v4.new_code_cell(s.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nexec(open(sys.argv[1]).read())\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbf.write(nb, sys.argv[2])\n"
}
```

```
File created successfully at: /tmp/claude-1001/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
echo $TMPDIR; date -u
```

```
/tmp/claude-1001
Sun Nov 15 07:33:52 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/cells.py",
 "content": "R = globals().get(\"RESULTS\", {})\n\n\ndef result(cid):\n    return R.get(cid, \"**Result: TODO**\")\n\n\nmd(r\"\"\"\n# Reproducing Chandravadia et al. (2020) from dandiset 000004\n\nPaper: Chandravadia, Liang, Schjetnan et al. (2020), \"A NWB-based dataset and processing pipeline of\nhuman single-neuron activity during a declarative memory task\", Scientific Data 7, 78,\ndoi:10.1038/s41597-020-0415-9.\n\nDataset: DANDI:000004, version **0.220126.1852** (doi:10.48324/dandi.000004/0.220126.1852). This version\nwas asked for by the run's prompt; it is the version the claims file was written against, and the\ndandiset's only published version holding the 87 sessions of the paper's Online-only Table 1. The\nfiles are streamed from the archive; the stimulus images are not read.\n\nThe claims file (`claims/chandravadia-2020.yaml`) was written from the open access full text of the\nversion of record (Methods, Data Records, Technical Validation, legends, Tables 1 and 2 and Online-only\nTable 1). Method details it lacks are taken from the paper's code,\nhttps://github.com/rutishauserlab/recogmem-release-NWB at commit 1d95162d2672e71dd234a31e4b8d70017a289ee3,\nas cited in the helper module `recogmem.py`.\n\nOutside inputs, read at run time from Europe PMC's copy of the open access full texts: Online-only\nTable 1 of this paper (PMC7055261), the reference list of sessions and subjects for several claims;\nand Table 1 of Faraut et al. 2018 (doi:10.1038/sdata.2018.10, PMC5810422), the earlier release, for\nthe two `with_inputs` claims. For the block of fig3-example-vs-neuron the file list of the paper's own\ndeposit on OSF (doi:10.17605/OSF.IO/HV7JA) is searched.\n\n| Claim | Tested here |\n|---|---|\n| counts-neurons-subjects | tested |\n| counts-sessions | tested |\n| table1-demographics | tested |\n| task-structure | tested |\n| new-old-label-coding | tested |\n| ttl-codes | tested |\n| experiment-ids | tested |\n| session-dates | tested |\n| units-table | tested |\n| electrodes-table | tested |\n| isi-criterion | tested |\n| fig5a-mtl-locations | tested |\n| fig5c-auc-all | tested |\n| fig5c-auc-sites | tested |\n| fig5b-roc-asymmetric | tested |\n| fig5d-confidence-accuracy | tested |\n| vs-cells-proportion | tested |\n| ms-cells-proportion | tested |\n| dual-cells-proportion | tested |\n| fig5f-site-proportions | tested |\n| twh-sessions | tested |\n| previous-release-link | tested (with Faraut et al. 2018, Table 1) |\n| previous-release-additions | tested (with Faraut et al. 2018, Table 1) |\n| fig4-example-vs-neuron | tested |\n| fig3-example-vs-neuron | blocked: session 144 is not in the dandiset (data_missing) |\n\"\"\")\n\ncode(r\"\"\"\nimport collections, time, warnings\nimport numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nfrom scipy import stats\nimport recogmem as rm\n\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_rows\", 200)\npd.set_option(\"display.max_columns\", 30)\nt0 = time.time()\nassets = rm.list_assets()\nS = rm.load_all([(p, u) for p, u, _ in assets])\nSID = {s[\"session_id\"]: s for s in S}\nprint(f\"{len(assets)} NWB files, {sum(a[2] for a in assets)/1e9:.2f} GB on the archive; loaded in {time.time()-t0:.0f} s\")\n\"\"\")\n\nmd(\"## Data check\")\n\ncode(r\"\"\"\nmeta = rm.dandiset_metadata()\nprint(\"Dandiset:\", meta[\"name\"])\nprint(\"Version:\", meta[\"version\"], \" DOI:\", meta.get(\"doi\"))\nprint(\"Archive summary:\", {k: meta[\"assetsSummary\"].get(k) for k in [\"numberOfFiles\", \"numberOfSubjects\", \"numberOfBytes\"]})\nprint(\"Related:\", [(r.get(\"relation\"), r.get(\"identifier\")) for r in meta.get(\"relatedResource\", [])])\n\npaper_t1 = rm.patient_table(rm.PAPER_PMC, \"Online-only Table 1\")\nfaraut_t1 = rm.patient_table(rm.FARAUT_PMC, \"Table 1\")\nprint(f\"Online-only Table 1 (this paper): {paper_t1.label.nunique()} subjects, {len(paper_t1)} sessions\")\nprint(f\"Table 1 of Faraut et al. 2018: {faraut_t1.label.nunique()} subjects, {len(faraut_t1)} sessions\")\n\nrows = []\nfor s in S:\n    t = s[\"trials\"]\n    r = rm.recog_trials(s)\n    rows.append({\n        \"file\": s[\"path\"].split(\"/\")[1][:40], \"identifier\": s[\"identifier\"], \"label\": s[\"label\"],\n        \"table_label\": rm.table_label(s[\"subject\"][\"subject_id\"]), \"session\": s[\"session_id\"],\n        \"site\": rm.site(s[\"label\"]), \"start\": s[\"session_start_time\"][:10],\n        \"learn\": (t.stim_phase == \"learn\").sum(), \"recog\": (t.stim_phase == \"recog\").sum(),\n        \"old(1)\": (r.label == 1).sum(), \"new(0)\": (r.label == 0).sum(), \"cats\": t.stimCategory.nunique(),\n        \"units\": len(s[\"unit_ids\"]), \"electrodes\": len(s[\"electrodes\"]),\n        \"exp_ids\": tuple(int(x) for x in np.unique(s[\"expids\"])), \"variant\": rm.variant_from_images(s),\n    })\nF = pd.DataFrame(rows)\nprint(F.to_string())\n\"\"\", tags=[\"sanity\"])\n\ncode(r\"\"\"\nprint(\"Files per site:\", F.site.value_counts().to_dict(), \" subjects per site:\", F.groupby(\"site\").label.nunique().to_dict())\nprint(\"Units per site:\", F.groupby(\"site\").units.sum().to_dict(), \" total\", F.units.sum())\nprint(\"Identifier label agrees with subject_id:\", (F.label.str.replace(\"CS\", \"C\") == F.table_label).all())\nprint(\"Session id in identifier equals the one in session_description:\",\n      all(s[\"session_id\"] == s[\"session_id_description\"] for s in S))\nprint(\"Trials table columns:\", collections.Counter(tuple(s[\"trials_columns\"]) for s in S).most_common())\nprint(\"Units table columns:\", collections.Counter(tuple(s[\"units_columns\"]) for s in S).most_common())\nprint(\"Electrodes table columns:\", collections.Counter(tuple(s[\"electrodes_columns\"]) for s in S).most_common())\nprint(\"Stimulus series (name, shape):\", collections.Counter(str(s[\"stimulus_series\"]) for s in S).most_common())\nprint(\"NWB versions:\", collections.Counter(s[\"nwb_version\"] for s in S))\n\nR = pd.concat([rm.recog_trials(s).assign(session=s[\"session_id\"]) for s in S])\nprint(\"Recognition response_value - 30:\", dict(sorted(collections.Counter(R.conf).items())))\nL = pd.concat([s[\"trials\"][s[\"trials\"].stim_phase == \"learn\"] for s in S])\nprint(\"Learning response_value:\", dict(collections.Counter(L.response_value)))\nprint(\"new_old_labels_recog in learning rows:\", dict(collections.Counter(L.new_old_labels_recog)))\nmism = [s[\"session_id\"] for s in S if not np.array_equal(rm.check_responses_against_events(s), rm.recog_trials(s).conf.values)]\nprint(\"Sessions where response_value - 30 differs from the event codes 30 to 36 the paper's code reads:\", mism)\n\nallt = pd.concat([s[\"trials\"] for s in S])\nprint(\"Stimulus duration stop - start (s): %.3f to %.3f, median %.3f\" % ((allt.stop_time - allt.start_time).min(),\n      (allt.stop_time - allt.start_time).max(), (allt.stop_time - allt.start_time).median()))\nprint(\"start_time == stim_on_time in every row:\", np.allclose(allt.start_time, allt.stim_on_time))\nrt = R.response_time - R.delay1_time\nprint(\"Recognition response after question onset (s): median %.2f, range %.2f to %.2f\" % (rt.median(), rt.min(), rt.max()))\n\"\"\", tags=[\"sanity\"])\n\ncode(r\"\"\"\n# Clocks: trial times against the event timestamps, and spikes against trials.\nrows = []\nfor s in S:\n    t = s[\"trials\"]\n    on_ev = s[\"events_t\"][s[\"events\"] == 1]\n    match = np.isin(np.round(t.start_time.values, 6), np.round(on_ev, 6)).mean()\n    spk = np.concatenate(s[\"spikes\"]) if len(s[\"spikes\"]) else np.array([])\n    rows.append({\"session\": s[\"session_id\"], \"onsets_in_events\": match,\n                 \"trials_s\": (t.start_time.min(), t.stop_time.max()),\n                 \"spikes_s\": (spk.min(), spk.max()) if len(spk) else None})\nC = pd.DataFrame(rows)\nprint(\"Fraction of trial start_time values found among the timestamps of event code 1: min %.3f, median %.3f\" %\n      (C.onsets_in_events.min(), C.onsets_in_events.median()))\nprint(\"Sessions where not all trial onsets are event timestamps:\", C[C.onsets_in_events < 1].session.tolist())\ncover = [(r.session) for r in C.itertuples() if r.spikes_s is None or r.spikes_s[0] > r.trials_s[0] or r.spikes_s[1] < r.trials_s[1]]\nprint(\"Sessions whose spikes do not span the trial period:\", cover)\nprint(\"Trial period (s) range of starts: %.0f to %.0f\" % (min(c[0] for c in C.trials_s), max(c[0] for c in C.trials_s)))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nThe spikes share the clock of the trials table if units respond to stimulus onset and to the stimulus\ncategory at the stated onsets and not at shifted ones. The test: for each unit, the rate 0.2 to 1.2 s\nafter onset against 1 s before onset (Wilcoxon signed-rank over the 100 recognition trials), and the\nVS ANOVA, with the true onsets and with all onsets shifted by +3 s and -3 s (into the inter-trial\nperiod). The shift is a standard choice for this check.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor s in S:\n    r = rm.recog_trials(s)\n    on, cat = r.start_time.values, r.stimCategory.values\n    for i, sp in enumerate(s[\"spikes\"]):\n        d = {\"session\": s[\"session_id\"]}\n        for name, shift in [(\"true\", 0.0), (\"+3s\", 3.0), (\"-3s\", -3.0)]:\n            post = rm.window_rates(sp, on + shift, rm.METHODS_WINDOW)\n            pre = rm.window_rates(sp, on + shift, (-1.0, 0.0))\n            diff = post - pre\n            d[\"resp_\" + name] = stats.wilcoxon(post, pre).pvalue < 0.05 if np.any(diff != 0) else False\n            d[\"vs_\" + name] = rm.vs_p(post, cat) < 0.05\n        rows.append(d)\nCK = pd.DataFrame(rows)\nprint(\"Units responsive to onset (p<0.05):\", {k: int(CK[\"resp_\" + k].sum()) for k in [\"true\", \"+3s\", \"-3s\"]}, \"of\", len(CK))\nprint(\"Units category selective (p<0.05):\", {k: int(CK[\"vs_\" + k].sum()) for k in [\"true\", \"+3s\", \"-3s\"]})\nper = CK.groupby(\"session\")[[\"resp_true\", \"resp_+3s\", \"resp_-3s\"]].sum()\nbetter = (per[\"resp_true\"] > per[[\"resp_+3s\", \"resp_-3s\"]].max(axis=1))\nprint(f\"Sessions with more responsive units at the true onsets than at either shift: {better.sum()} of {len(per)}\")\nprint(\"Sessions where this does not hold (units, responsive true/+3/-3):\")\nprint(per[~better].join(F.set_index(\"session\").units).to_string())\n\"\"\", tags=[\"sanity\"])\n\ncode(r\"\"\"\ndrop, pairs = rm.duplicated_trains(S)\nprint(\"Spike trains identical to a train of an earlier file:\", len(drop))\nfor (a, b), n in pairs.items():\n    sa, sb = SID[a], SID[b]\n    same_events = len(sa[\"events\"]) == len(sb[\"events\"]) and np.array_equal(sa[\"events\"], sb[\"events\"]) and np.allclose(sa[\"events_t\"], sb[\"events_t\"])\n    ta, tb = sa[\"trials\"], sb[\"trials\"]\n    same_trials = len(ta) == len(tb) and np.allclose(ta.start_time, tb.start_time)\n    same_imgs = len(ta) == len(tb) and (ta.external_image_file.values == tb.external_image_file.values).all()\n    print(f\"  sessions {a} ({sa['label']}, {len(sa['spikes'])} units) and {b} ({sb['label']}, {len(sb['spikes'])} units): \"\n          f\"{n} identical trains; identical events {same_events}, identical trial onsets {same_trials}, identical image list {same_imgs}\")\n    if len(ta) == len(tb):\n        dt = (tb.start_time.values - ta.start_time.values)\n        print(f\"     onset difference b - a: {dt.min():.3f} to {dt.max():.3f} s; responses equal in {np.mean(ta.response_value.values == tb.response_value.values):.2f} of trials\")\n\"\"\", tags=[\"sanity\"])\n\n# ---------------------------------------------------------------- counts\nmd(r\"\"\"\n## counts-neurons-subjects\n\n> The dataset holds 1863 single neurons recorded from the medial temporal lobes of 59 subjects.\n\nCriterion: neurons are the unit rows of all files, subjects the distinct subject_id values; reading\n(a) every unit row, (b) spike trains deposited in two files counted once.\n\"\"\")\ncode(r\"\"\"\nn_units = sum(len(s[\"unit_ids\"]) for s in S)\nn_subj = len({s[\"subject\"][\"subject_id\"] for s in S})\nprint(f\"(a) unit rows: {n_units} (expected 1863 +/- 186.3, difference {n_units-1863:+d}); subjects: {n_subj} (expected 59 +/- 5.9)\")\nprint(f\"(b) trains counted once: {n_units-len(drop)} (difference {n_units-len(drop)-1863:+d})\")\nprint(\"Units per subject: min %d, median %d, max %d\" % tuple(F.groupby(\"label\").units.sum().agg([\"min\", \"median\", \"max\"])))\nprint(\"Dandiset metadata numberOfSubjects:\", meta[\"assetsSummary\"][\"numberOfSubjects\"])\n\"\"\", tags=[\"claim:counts-neurons-subjects\"])\nmd(result(\"counts-neurons-subjects\"))\n\nmd(r\"\"\"\n## counts-sessions\n\n> The patients performed 87 sessions, listed by subject and session id in Online-only Table 1 (the Methods give 89).\n\nCriterion: the set of (subject, session id) pairs in the files against Online-only Table 1.\n\"\"\")\ncode(r\"\"\"\nfiles_set = set(zip(F.table_label, F.session))\ntable_set = set(zip(paper_t1.label, paper_t1.session_id))\nprint(f\"Files: {len(files_set)} (subject, session) pairs; Online-only Table 1: {len(table_set)}; Methods text: 89\")\nprint(\"In the files, not in the table:\", sorted(files_set - table_set))\nprint(\"In the table, not in the files:\", sorted(table_set - files_set))\nv = paper_t1.set_index(\"session_id\").variant\nF[\"table_variant\"] = F.session.map(v)\nprint(\"Variant from the image directories equals the table's variant in\", (F.variant == F.table_variant).sum(), \"of\", len(F), \"sessions\")\nprint(F[F.variant != F.table_variant][[\"session\", \"table_label\", \"variant\", \"table_variant\"]].to_string())\n\"\"\", tags=[\"claim:counts-sessions\"])\nmd(result(\"counts-sessions\"))\n\nmd(r\"\"\"\n## table1-demographics\n\n> Online-only Table 1 gives the age and sex of every subject; there are 25 female and 34 male subjects.\n\"\"\")\ncode(r\"\"\"\nsubj = pd.DataFrame([{\"table_label\": rm.table_label(s[\"subject\"][\"subject_id\"]), \"file_age\": s[\"subject\"].get(\"age\"),\n                      \"file_sex\": s[\"subject\"].get(\"sex\"), \"file_diagnosis\": s[\"subject\"].get(\"description\"),\n                      \"session\": s[\"session_id\"]} for s in S])\nper_subj = subj.groupby(\"table_label\").agg(file_age=(\"file_age\", lambda x: sorted(set(x))), file_sex=(\"file_sex\", lambda x: sorted(set(x))),\n                                           file_diagnosis=(\"file_diagnosis\", lambda x: sorted(set(x))))\ntab = paper_t1.groupby(\"label\").first()[[\"age\", \"sex\", \"diagnosis\"]]\ncmp_ = per_subj.join(tab, how=\"outer\")\ncmp_[\"age_ok\"] = [len(a) == 1 and str(a[0]) == str(b) for a, b in zip(cmp_.file_age, cmp_.age)]\ncmp_[\"sex_ok\"] = [len(a) == 1 and a[0] == b for a, b in zip(cmp_.file_sex, cmp_.sex)]\nprint(f\"Subjects: {len(cmp_)}; age matches {cmp_.age_ok.sum()}, sex matches {cmp_.sex_ok.sum()}, both {(cmp_.age_ok & cmp_.sex_ok).sum()}\")\nprint(\"Subjects that differ:\")\nprint(cmp_[~(cmp_.age_ok & cmp_.sex_ok)][[\"file_age\", \"age\", \"file_sex\", \"sex\"]].to_string())\nfs = per_subj.file_sex.map(lambda x: x[0]).value_counts().to_dict()\nprint(\"Files, subjects by sex:\", fs, \"  table:\", tab.sex.value_counts().to_dict(), \" (expected F 25, M 34)\")\nprint(\"Diagnosis, file against table (first 12 subjects):\")\nprint(cmp_[[\"file_diagnosis\", \"diagnosis\"]].head(12).to_string())\nprint(\"Distinct diagnosis values in files:\", sorted({d for x in per_subj.file_diagnosis for d in x}))\nprint(\"Diagnosis text equal to the table's in\", sum(len(a) == 1 and a[0] == b for a, b in zip(cmp_.file_diagnosis, cmp_.diagnosis)), \"of\", len(cmp_))\n\"\"\", tags=[\"claim:table1-demographics\"])\nmd(result(\"table1-demographics\"))\n\nmd(r\"\"\"\n## task-structure\n\n> Each session has 100 encoding trials showing 100 novel images and 100 recognition trials, of which 50\n> show new and 50 old images, and the images come from 5 visual categories.\n\"\"\")\ncode(r\"\"\"\nrows = []\nfor s in S:\n    t = s[\"trials\"]\n    le, rc = t[t.stim_phase == \"learn\"], t[t.stim_phase == \"recog\"]\n    rows.append({\"session\": s[\"session_id\"], \"learn\": len(le), \"learn_distinct_images\": le.external_image_file.nunique(),\n                 \"recog\": len(rc), \"label0\": (rc.new_old_labels_recog == \"0\").sum(), \"label1\": (rc.new_old_labels_recog == \"1\").sum(),\n                 \"categories\": t.stimCategory.nunique(), \"images_stored\": list(s[\"stimulus_series\"].values())[0][0]})\nT = pd.DataFrame(rows)\nT[\"enc_ok\"] = (T.learn == 100) & (T.learn_distinct_images == 100)\nT[\"rec_ok\"] = (T.recog == 100) & (T.label0 == 50) & (T.label1 == 50)\nT[\"cat_ok\"] = T.categories == 5\nprint(\"Sessions with 100 encoding trials of 100 distinct images:\", T.enc_ok.sum(), \"of\", len(T))\nprint(\"Sessions with 100 recognition trials, 50 of each label:\", T.rec_ok.sum())\nprint(\"Sessions with 5 categories:\", T.cat_ok.sum())\nprint(\"Sessions with stored images equal to the number of trials:\", (T.images_stored == T.learn + T.recog).sum())\nprint(T[~(T.enc_ok & T.rec_ok & T.cat_ok)].to_string())\n\"\"\", tags=[\"claim:task-structure\"])\nmd(result(\"task-structure\"))\n\nmd(r\"\"\"\n## new-old-label-coding\n\n> In the trials table, new_old_labels_recog is 0 for old stimuli (seen during encoding) and 1 for new stimuli.\n\nCriterion: per session, (1) whether label-0 trials show images of the session's encoding block and\nlabel-1 trials do not, and (2) whether label-0 trials receive \"old\" responses (4 to 6) more often.\n\"\"\")\ncode(r\"\"\"\nrows = []\nfor s in S:\n    t = s[\"trials\"]\n    enc = set(t[t.stim_phase == \"learn\"].external_image_file)\n    r = rm.recog_trials(s)\n    seen = r.external_image_file.isin(enc)\n    oldresp = r.conf >= 4\n    rows.append({\"session\": s[\"session_id\"],\n                 \"label0_seen\": seen[r.label == 0].mean(), \"label1_seen\": seen[r.label == 1].mean(),\n                 \"label0_oldresp\": oldresp[r.label == 0].mean(), \"label1_oldresp\": oldresp[r.label == 1].mean()})\nN = pd.DataFrame(rows)\nstated = (N.label0_seen == 1) & (N.label1_seen == 0) & (N.label0_oldresp > N.label1_oldresp)\nreversed_ = (N.label1_seen == 1) & (N.label0_seen == 0) & (N.label1_oldresp > N.label0_oldresp)\nprint(f\"Both tests hold under the stated coding (0 = old) in {stated.sum()} of {len(N)} sessions; with the labels reversed in {reversed_.sum()}\")\nprint(\"Fraction of label-0 trials showing an encoding image: %.2f to %.2f; label-1: %.2f to %.2f\" %\n      (N.label0_seen.min(), N.label0_seen.max(), N.label1_seen.min(), N.label1_seen.max()))\nprint(\"Fraction of 'old' responses, label 0: median %.2f; label 1: median %.2f\" % (N.label0_oldresp.median(), N.label1_oldresp.median()))\nprint(\"Sessions where label 1 gets fewer 'old' responses than label 0:\", N[N.label1_oldresp <= N.label0_oldresp].session.tolist())\nprint(\"Column description:\", repr(SID[5][\"trials\"].attrs.get(\"description\", \"\")) if hasattr(SID[5][\"trials\"], \"attrs\") else \"\")\n\"\"\", tags=[\"claim:new-old-label-coding\"])\nmd(result(\"new-old-label-coding\"))\n\nmd(r\"\"\"\n## ttl-codes\n\n> The events stream holds the TTL markers 55, 1, 2, 3, 20 or 21, 31 to 36, 6 and 66 with the meanings\n> of Table 1, and the events and experiment_ids streams have one entry each, in the same order.\n\"\"\")\ncode(r\"\"\"\nlisted = {55, 1, 2, 3, 20, 21, 31, 32, 33, 34, 35, 36, 6, 66}\nrows = []\nfor s in S:\n    same = len(s[\"events\"]) == len(s[\"expids\"]) and np.array_equal(s[\"events_t\"], s[\"expids_t\"])\n    other = collections.Counter(c for c in s[\"events\"] if c not in listed)\n    n, bad = rm.trial_event_order(s)\n    rows.append({\"session\": s[\"session_id\"], \"same_len_ts\": same, \"other_codes\": dict(other), \"onsets\": n, \"bad_order\": bad,\n                 \"n55\": int(np.sum(s[\"events\"] == 55)), \"n66\": int(np.sum(s[\"events\"] == 66))})\nE = pd.DataFrame(rows)\nE[\"ok\"] = E.same_len_ts & (E.other_codes.map(len) == 0) & (E.bad_order == 0)\nprint(\"Files with equal length and timestamps of events and experiment_ids:\", E.same_len_ts.sum(), \"of\", len(E))\nprint(\"Files holding only the listed codes:\", (E.other_codes.map(len) == 0).sum())\nprint(\"Files where every trial shows 1, 2, 3, response, 6 in order:\", (E.bad_order == 0).sum(), \"; trials out of order:\", E.bad_order.sum(), \"of\", E.onsets.sum())\nprint(\"Files meeting all three:\", E.ok.sum(), \"of\", len(E))\nprint(\"Code counts over all files:\", dict(sorted(collections.Counter(np.concatenate([s['events'] for s in S])).items())))\nprint(E[~E.ok].to_string())\nprint(\"Files with 55 not twice:\", E[E.n55 != 2].session.tolist(), \" with 66 not twice:\", E[E.n66 != 2].session.tolist())\n\"\"\", tags=[\"claim:ttl-codes\"])\nmd(result(\"ttl-codes\"))\n\nmd(r\"\"\"\n## experiment-ids\n\n> The learning block is labelled with one of 80, 83 or 88 and the recognition block with one of 81, 84 or 89.\n\nThe learning block is the experiment id of the trials with stim_phase \"learn\" (the id of the events\naround their onsets), the recognition block that of the \"recog\" trials.\n\"\"\")\ncode(r\"\"\"\nrows = []\nfor s in S:\n    t = s[\"trials\"]\n    ids = []\n    for ph in [\"learn\", \"recog\"]:\n        on = t[t.stim_phase == ph].start_time.values\n        k = np.searchsorted(s[\"expids_t\"], on)\n        k = np.clip(k, 0, len(s[\"expids_t\"]) - 1)\n        ids.append(tuple(sorted(set(s[\"expids\"][k].astype(int)))))\n    rows.append({\"session\": s[\"session_id\"], \"learn_id\": ids[0], \"recog_id\": ids[1], \"data_collection\": s[\"data_collection\"]})\nX = pd.DataFrame(rows)\nX[\"ok\"] = X.learn_id.map(lambda x: len(x) == 1 and x[0] in (80, 83, 88)) & X.recog_id.map(lambda x: len(x) == 1 and x[0] in (81, 84, 89))\nX[\"pair_ok\"] = [(l[0], r[0]) in [(80, 81), (83, 84), (88, 89)] if len(l) == 1 and len(r) == 1 else False for l, r in zip(X.learn_id, X.recog_id)]\nprint(\"Files whose two ids fall in the stated sets:\", X.ok.sum(), \"of\", len(X), \"; whose pair is one of Table 2's:\", X.pair_ok.sum())\nprint(collections.Counter(zip(X.learn_id, X.recog_id)))\nprint(X[~X.ok].to_string())\n\"\"\", tags=[\"claim:experiment-ids\"])\nmd(result(\"experiment-ids\"))\n\nmd(r\"\"\"\n## session-dates\n\n> To protect patient information, session_start_time keeps only the year and month of the experiment,\n> with the day set to the first of the month for all sessions.\n\"\"\")\ncode(r\"\"\"\nD = pd.DataFrame({\"session\": [s[\"session_id\"] for s in S], \"label\": [s[\"label\"] for s in S],\n                  \"start\": [s[\"session_start_time\"] for s in S]})\nD[\"date\"] = pd.to_datetime(D.start.str[:10])\nprint(\"Files on the first of a month:\", (D.date.dt.day == 1).sum(), \"of\", len(D))\nprint(D[D.date.dt.day != 1].to_string())\nprint(\"Years:\", dict(sorted(collections.Counter(D.date.dt.year).items())))\nprint(\"Time of day and offsets:\", collections.Counter(D.start.str[10:]))\nprint(\"Sessions of the same subject as session 68, and sessions 67 to 69:\")\nprint(D[D.session.isin([67, 68, 69])].to_string())\n\"\"\", tags=[\"claim:session-dates\"])\nmd(result(\"session-dates\"))\n\nmd(r\"\"\"\n## units-table\n\n> The units table holds spike_times, waveform_mean_encoding, waveform_mean_recognition (sampled at\n> 100 kHz), origClusterID, SNR, IsolDist and electrodes, with one electrode per neuron.\n\"\"\")\ncode(r\"\"\"\nneed = [\"spike_times\", \"waveform_mean_encoding\", \"waveform_mean_recognition\", \"origClusterID\", \"SNR\", \"IsolDist\", \"electrodes\"]\npresent = collections.Counter()\nfor s in S:\n    for c in need:\n        present[c] += c in s[\"units_datasets\"]\npresent[\"IsolationDist (in place of IsolDist)\"] = sum(\"IsolationDist\" in s[\"units_datasets\"] for s in S)\nprint(\"Files holding each column:\", dict(present), \"of\", len(S))\nprint(\"Units linked to exactly one electrode:\", sum(len(e) == 1 for s in S for e in s[\"unit_electrodes\"]), \"of\", n_units)\nrates = np.concatenate([s[\"waveform_rate\"] for s in S])\nprint(\"Waveform sampling rate (Hz):\", dict(collections.Counter(rates)), \"; expected 100000 +/- 10000\")\nprint(\"Waveform shapes:\", collections.Counter(s[\"waveform_mean_encoding_shape\"][1] for s in S))\nfor c in [\"SNR\", \"IsolationDist\", \"origClusterID\"]:\n    v = np.concatenate([s[c] for s in S]).astype(float)\n    fin = np.isfinite(v)\n    print(f\"{c}: finite for {fin.sum()} of {len(v)} units (nan {np.isnan(v).sum()}, inf {np.isinf(v).sum()}); finite range {v[fin].min():.3g} to {v[fin].max():.3g}\")\niso = np.concatenate([s[\"IsolationDist\"] for s in S])\nprint(\"IsolationDist above 1e6:\", int(np.sum(iso[np.isfinite(iso)] > 1e6)))\nprint(\"Sessions with any non-finite SNR or IsolationDist:\", sum(not (np.isfinite(s[\"SNR\"]).all() and np.isfinite(s[\"IsolationDist\"]).all()) for s in S))\n\"\"\", tags=[\"claim:units-table\"])\nmd(result(\"units-table\"))\n\nmd(r\"\"\"\n## electrodes-table\n\n> The electrodes table gives each electrode's brain area, MNI coordinates, impedance, the filter applied\n> before spike sorting (300 to 3000 Hz) and the original hardware channel.\n\"\"\")\ncode(r\"\"\"\nEL = pd.concat([s[\"electrodes\"].assign(session=s[\"session_id\"]) for s in S])\ndef empty(v):\n    return v is None or (isinstance(v, float) and np.isnan(v)) or (isinstance(v, str) and v.strip() == \"\")\nfor c in [\"location\", \"x\", \"y\", \"z\", \"imp\", \"filtering\", \"origChannel\"]:\n    e = EL[c].map(empty)\n    print(f\"{c:12s} empty for {e.sum():4d} of {len(EL)} electrodes, in {EL[e].session.nunique()} sessions\")\nprint(\"Filtering values:\", dict(collections.Counter(EL.filtering)))\nprint(\"Sessions with empty coordinates:\", sorted(EL[EL.x.map(empty)].session.unique()))\n\"\"\", tags=[\"claim:electrodes-table\"])\nmd(result(\"electrodes-table\"))\n\nmd(r\"\"\"\n## isi-criterion\n\n> Clusters were accepted as units only when fewer than 3% of their interspike intervals were shorter than 3 ms.\n\"\"\")\ncode(r\"\"\"\nrows = []\nfor s in S:\n    for i, sp in enumerate(s[\"spikes\"]):\n        rows.append({\"session\": s[\"session_id\"], \"unit\": i, \"n_spikes\": len(sp),\n                     \"isi_sorted\": rm.isi_violation_fraction(sp, sort=True),\n                     \"isi_stored\": rm.isi_violation_fraction(sp, sort=False),\n                     \"unsorted\": bool(np.any(np.diff(sp) < 0)), \"dup_spikes\": int(np.sum(np.diff(np.sort(sp)) == 0))})\nI = pd.DataFrame(rows)\nfor c in [\"isi_sorted\", \"isi_stored\"]:\n    print(f\"{c}: below 3% for {np.sum(I[c] < 0.03)} of {len(I)} units ({100*np.mean(I[c] < 0.03):.2f}%); median {100*I[c].median():.2f}%, max {100*I[c].max():.1f}%\")\nprint(\"Units with spike times not sorted in time:\", I.unsorted.sum(), \" in sessions\", sorted(I[I.unsorted].session.unique()))\nprint(\"Units with repeated identical spike times:\", (I.dup_spikes > 0).sum())\nprint(\"Units at or above 3% (sorted):\")\nprint(I[I.isi_sorted >= 0.03].to_string())\n\"\"\", tags=[\"claim:isi-criterion\"])\nmd(result(\"isi-criterion\"))\n\nmd(r\"\"\"\n## fig5a-mtl-locations\n\n> All neurons were recorded from the medial temporal lobe, in the amygdala and the hippocampus.\n\"\"\")\ncode(r\"\"\"\nloc = collections.Counter(s[\"electrodes\"].location.values[e[0]] for s in S for e in s[\"unit_electrodes\"])\nprint(\"Units by electrode location:\", dict(loc))\nok = sum(v for k, v in loc.items() if \"amygdala\" in k.lower() or \"hippocampus\" in k.lower())\nprint(f\"Units in the amygdala or hippocampus: {ok} of {sum(loc.values())}\")\n\"\"\", tags=[\"claim:fig5a-mtl-locations\"])\nmd(result(\"fig5a-mtl-locations\"))\n\n# ---------------------------------------------------------------- behaviour\nmd(r\"\"\"\n## Behaviour: ROC per session\n\nAUC, z-ROC slope and accuracy by confidence, per session, as the helper describes (paper's code).\n\"\"\")\ncode(r\"\"\"\nrows = []\nfor s in S:\n    r = rm.recog_trials(s)\n    lab, conf = r.label.values, r.conf.values\n    h, f = rm.cumulative_roc(lab, conf)\n    hi, lo = rm.accuracy_fixed_split(lab, conf)\n    dhi, dlo, mode = rm.accuracy_dynamic_split(lab, conf)\n    a = rm.auc(h, f)\n    rows.append({\"session\": s[\"session_id\"], \"label\": s[\"label\"], \"site\": rm.site(s[\"label\"]), \"auc\": a,\n                 \"auc_reversed_labels\": rm.auc(*rm.cumulative_roc(1 - lab, conf)),\n                 \"slope\": rm.zroc_slope(h, f), \"acc_high\": hi, \"acc_low\": lo, \"dyn_high\": dhi, \"dyn_low\": dlo, \"dyn_mode\": mode,\n                 \"H\": h, \"F\": f})\nB = pd.DataFrame(rows)\nprint(B.drop(columns=[\"H\", \"F\"]).describe().round(3).to_string())\n\"\"\")\n\nmd(r\"\"\"\n## fig5c-auc-all\n\n> Subjects distinguished new from old images; the behavioural AUC averaged over all sessions is 0.74 ± 0.10.\n\"\"\")\ncode(r\"\"\"\nm, sd = B.auc.mean(), B.auc.std(ddof=1)\nprint(f\"AUC over {len(B)} sessions: mean {m:.3f} (expected 0.74 +/- 0.10), SD {sd:.3f} (expected 0.10 +/- 0.01); range {B.auc.min():.3f} to {B.auc.max():.3f}\")\nprint(f\"Sessions with AUC above 0.5: {(B.auc > 0.5).sum()}; one-sample t-test against 0.5: p = {stats.ttest_1samp(B.auc, 0.5).pvalue:.2e}\")\nprint(f\"With the stated label coding (0 = old) the mean AUC would be {B.auc_reversed_labels.mean():.3f}\")\ndd = B[~B.session.isin([b for (a, b) in pairs])]\nprint(f\"Without the second file of each pair sharing spike trains ({len(dd)} sessions): mean {dd.auc.mean():.3f}, SD {dd.auc.std(ddof=1):.3f}\")\nfig, ax = plt.subplots(1, 2, figsize=(9, 3.5))\nfor h, f in zip(B.H, B.F):\n    ax[0].plot(np.r_[0, f, 1], np.r_[0, h, 1], color=\"0.8\", lw=0.7)\nax[0].plot(np.r_[0, np.mean(np.stack(B.F), 0), 1], np.r_[0, np.mean(np.stack(B.H), 0), 1], \"o-\", color=\"C0\")\nax[0].plot([0, 1], [0, 1], \"k:\")\nax[0].set(xlabel=\"false alarm rate\", ylabel=\"hit rate\", title=\"ROC per session (all points in [0, 1])\")\nax[1].hist([B.auc[B.site == \"CS\"], B.auc[B.site == \"TWH\"]], bins=15, label=[\"CS\", \"TWH\"], stacked=True)\nax[1].set(xlabel=\"AUC\", ylabel=\"sessions\", title=f\"AUC, range {B.auc.min():.2f} to {B.auc.max():.2f}\")\nax[1].legend()\nplt.tight_layout()\n\"\"\", tags=[\"claim:fig5c-auc-all\"])\nmd(result(\"fig5c-auc-all\"))\n\nmd(r\"\"\"\n## fig5c-auc-sites\n\n> Performance was similar at the two study sites, with an average AUC of 0.74 ± 0.09 for CS sessions and\n> 0.69 ± 0.13 for TWH sessions.\n\"\"\")\ncode(r\"\"\"\ng = B.groupby(\"site\").auc.agg([\"count\", \"mean\", \"std\"])\nprint(g.round(3).to_string())\nprint(\"Expected: CS 0.74 +/- 0.09 (SD 0.09 +/- 0.009); TWH 0.69 +/- 0.13 (SD 0.13 +/- 0.013)\")\nw = stats.ttest_ind(B.auc[B.site == \"CS\"], B.auc[B.site == \"TWH\"], equal_var=False)\nprint(f\"Welch's t-test CS against TWH: t = {w.statistic:.2f}, p = {w.pvalue:.3f}; difference of means {g.loc['CS','mean']-g.loc['TWH','mean']:.3f}\")\n\"\"\", tags=[\"claim:fig5c-auc-sites\"])\nmd(result(\"fig5c-auc-sites\"))\n\nmd(r\"\"\"\n## fig5b-roc-asymmetric\n\n> The ROC curve is asymmetric (p < 0.05), as expected for declarative memory.\n\nCriterion: z-ROC slope per session (calcZROCSlope), mean below 1 with a two-sided one-sample t-test\nagainst 1 at p < 0.05; Wilcoxon and the pooled ROC's slope are variants.\n\"\"\")\ncode(r\"\"\"\nsl = B.slope.dropna()\nprint(f\"z-ROC slope over {len(sl)} sessions ({B.slope.isna().sum()} without two distinct false alarm points): mean {sl.mean():.3f}, SD {sl.std():.3f}, median {sl.median():.3f}, range {sl.min():.2f} to {sl.max():.2f}\")\nt = stats.ttest_1samp(sl, 1.0)\nprint(f\"t-test against 1: t = {t.statistic:.2f}, p = {t.pvalue:.2e}; sessions with slope below 1: {(sl < 1).sum()}\")\nwx = stats.wilcoxon(sl - 1)\nprint(f\"Wilcoxon signed-rank against 1: p = {wx.pvalue:.2e}\")\nlab_all = np.concatenate([rm.recog_trials(s).label.values for s in S]); conf_all = np.concatenate([rm.recog_trials(s).conf.values for s in S])\nold, new = rm.typecounters(lab_all, conf_all)\nhp, fp = np.cumsum(old) / old.sum(), np.cumsum(new) / new.sum()\nprint(f\"Pooled ROC (all trials): z-ROC slope {rm.zroc_slope(hp, fp):.3f}\")\n\"\"\", tags=[\"claim:fig5b-roc-asymmetric\"])\nmd(result(\"fig5b-roc-asymmetric\"))\n\nmd(r\"\"\"\n## fig5d-confidence-accuracy\n\n> Accuracy is significantly higher in high than in low confidence trials (P < 0.001, paired t test) across all sessions.\n\nReadings: (a) fixed split (high 1 or 6, low 2 to 5; NO_behavior_evaluateSessionStatus.m), (b) the\ndynamic split of the Python code (helper.dynamic_split). Sessions without responses in a group are left\nout. The unpaired tests the code runs (ttest2 in MATLAB, Welch's in Python) are variants, and so is\nthe code's session inclusion (check_inclusion: AUC at least 0.6 and at most one unused level per side).\n\"\"\")\ncode(r\"\"\"\nfor name, hcol, lcol in [(\"(a) fixed split\", \"acc_high\", \"acc_low\"), (\"(b) dynamic split\", \"dyn_high\", \"dyn_low\")]:\n    x = B.dropna(subset=[hcol, lcol])\n    pt = stats.ttest_rel(x[hcol], x[lcol])\n    ut = stats.ttest_ind(x[hcol], x[lcol])\n    wt = stats.ttest_ind(x[hcol], x[lcol], equal_var=False)\n    print(f\"{name}: {len(x)} sessions ({len(B)-len(x)} left out); high {x[hcol].mean():.1f}%, low {x[lcol].mean():.1f}%, \"\n          f\"difference {np.mean(x[hcol]-x[lcol]):.1f} points; high > low in {(x[hcol] > x[lcol]).sum()} sessions\")\n    print(f\"    paired t = {pt.statistic:.2f}, p = {pt.pvalue:.1e}; unpaired p = {ut.pvalue:.1e}; Welch p = {wt.pvalue:.1e}\")\n    for site_, gg in x.groupby(\"site\"):\n        print(f\"    {site_}: {len(gg)} sessions, high {gg[hcol].mean():.1f}% (SD {gg[hcol].std():.1f}), low {gg[lcol].mean():.1f}% (SD {gg[lcol].std():.1f})\")\nprint(\"Sessions left out under (a):\", B[B[[\"acc_high\", \"acc_low\"]].isna().any(axis=1)].session.tolist())\nprint(\"Dynamic split modes:\", dict(collections.Counter(B.dyn_mode)))\nincl = []\nfor s in S:\n    conf = rm.recog_trials(s).conf.values\n    cnt = np.array([np.sum(conf == k) for k in range(1, 7)])\n    incl.append(not ((np.sum(cnt[:3] == 0) > 1) or (np.sum(cnt[3:] == 0) > 1)))\ninc = B[np.array(incl) & (B.auc >= 0.6)].dropna(subset=[\"dyn_high\", \"dyn_low\"])\nprint(f\"Code's inclusion, dynamic split: {len(inc)} sessions, high {inc.dyn_high.mean():.1f}%, low {inc.dyn_low.mean():.1f}%, \"\n      f\"paired p = {stats.ttest_rel(inc.dyn_high, inc.dyn_low).pvalue:.1e}, Welch p = {stats.ttest_ind(inc.dyn_high, inc.dyn_low, equal_var=False).pvalue:.1e}\")\n\"\"\", tags=[\"claim:fig5d-confidence-accuracy\"])\nmd(result(\"fig5d-confidence-accuracy\"))\n\n# ---------------------------------------------------------------- neurons\nmd(r\"\"\"\n## Single neurons: VS and MS tests\n\nFor every unit: firing rates in the recognition trials in the Methods' window (0.2 to 1.2 s) and the\ncode's (0.2 to 1.7 s); the VS one-way ANOVA across the stimCategory values; the MS bootstrap between\nlabel-0 and label-1 trials, (i) all 50 and 50 trials (Methods) and (ii) correct trials only, as the\ncode's ms_test. The bootstrap uses its own generator (seed 20200304, a standard choice); the spread\nover five other seeds is shown below. Nulls: the category labels, or the new/old labels, shuffled within\neach session (one permutation per session, applied to all its units; 10 permutations).\n\"\"\")\ncode(r\"\"\"\ndef unit_tests(rng, shuffle_rng=None):\n    rows = []\n    for s in S:\n        r = rm.recog_trials(s)\n        on, cat, lab, conf = r.start_time.values, r.stimCategory.values, r.label.values, r.conf.values\n        if shuffle_rng is not None:\n            cat = shuffle_rng.permutation(cat)\n            lab = shuffle_rng.permutation(lab)\n        correct = ((conf <= 3) & (lab == 0)) | ((conf >= 4) & (lab == 1))\n        for i, sp in enumerate(s[\"spikes\"]):\n            d = {\"session\": s[\"session_id\"], \"unit\": i, \"site\": rm.site(s[\"label\"]), \"dup\": (s[\"session_id\"], i) in drop}\n            for wn, w in [(\"M\", rm.METHODS_WINDOW), (\"C\", rm.CODE_WINDOW)]:\n                fr = rm.window_rates(sp, on, w)\n                d[\"vs_\" + wn] = rm.vs_p(fr, cat)\n                d[\"ms_all_\" + wn] = rm.bootstrap_p(fr[lab == 0], fr[lab == 1], rng)\n                d[\"ms_cor_\" + wn] = rm.bootstrap_p(fr[(lab == 0) & correct], fr[(lab == 1) & correct], rng)\n            d[\"rate_M\"] = rm.window_rates(sp, on, rm.METHODS_WINDOW).mean()\n            rows.append(d)\n    return pd.DataFrame(rows)\n\nt1 = time.time()\nU = unit_tests(np.random.default_rng(20200304))\nprint(f\"Tests on {len(U)} units in {time.time()-t1:.0f} s\")\nprint(\"Units with no spike in any recognition window (Methods window):\", int((U.rate_M == 0).sum()))\nprint(\"Units whose ANOVA could not be computed (all rates equal):\", int(U.vs_M.isna().sum()), \"(Methods window),\", int(U.vs_C.isna().sum()), \"(code window)\")\nseeds = {}\nfor sd in [1, 2, 3, 4, 5]:\n    u2 = unit_tests(np.random.default_rng(sd))\n    seeds[sd] = {c: int((u2[c] < 0.05).sum()) for c in [\"ms_all_M\", \"ms_cor_M\", \"ms_all_C\", \"ms_cor_C\"]}\n    seeds[sd][\"dual_main\"] = int(((u2.vs_M < 0.05) & (u2.ms_all_M < 0.05)).sum())\n    seeds[sd][\"dual_code\"] = int(((u2.vs_C < 0.05) & (u2.ms_cor_C < 0.05)).sum())\nprint(\"MS and dual counts under five other bootstrap seeds:\")\nprint(pd.DataFrame(seeds).T.to_string())\nnulls = []\nprng = np.random.default_rng(7)\nfor k in range(10):\n    un = unit_tests(np.random.default_rng(100 + k), shuffle_rng=prng)\n    nulls.append({c: int((un[c] < 0.05).sum()) for c in [\"vs_M\", \"vs_C\", \"ms_all_M\", \"ms_cor_C\"]})\nNU = pd.DataFrame(nulls)\nprint(\"Shuffled-label nulls (10 permutations): mean (min to max) units at p < 0.05\")\nprint(pd.DataFrame({\"mean\": NU.mean(), \"min\": NU.min(), \"max\": NU.max()}).to_string())\n\"\"\")\n\nmd(r\"\"\"\n## vs-cells-proportion\n\n> 343 of the 1863 cells (18.4%) are visually selective, by a one-way ANOVA (P < 0.05) of the firing rate in\n> recognition trials, in a 1 s window starting 200 ms after stimulus onset, across the 5 visual categories.\n\"\"\")\ncode(r\"\"\"\ndef show(col, label):\n    a = U[col] < 0.05\n    nd = U[~U.dup]\n    print(f\"{label}: {a.sum()} of {len(U)} ({100*a.mean():.1f}%); trains counted once: {(nd[col] < 0.05).sum()} of {len(nd)} ({100*(nd[col] < 0.05).mean():.1f}%)\")\nshow(\"vs_M\", \"VS, Methods window (main)\")\nshow(\"vs_C\", \"VS, code window\")\nprint(\"Expected 343 +/- 34.3 cells and 18.4 +/- 1.84 %; null (shuffled categories) mean %.1f units (Methods window)\" % NU.vs_M.mean())\nprint(\"VS by site (Methods window):\", U.groupby(\"site\").vs_M.apply(lambda p: f\"{(p<0.05).sum()} of {len(p)}\").to_dict())\n\"\"\", tags=[\"claim:vs-cells-proportion\"])\nmd(result(\"vs-cells-proportion\"))\n\nmd(r\"\"\"\n## ms-cells-proportion\n\n> 146 of the 1863 cells (7.8%) are memory selective, by a two-tailed bootstrap comparison of mean firing\n> rates (1,000 runs, P < 0.05) between the 50 novel and 50 familiar recognition trials in a 1 s window\n> starting 200 ms after stimulus onset.\n\"\"\")\ncode(r\"\"\"\nshow(\"ms_all_M\", \"MS, Methods window, all trials (main)\")\nshow(\"ms_cor_M\", \"MS, Methods window, correct trials\")\nshow(\"ms_all_C\", \"MS, code window, all trials\")\nshow(\"ms_cor_C\", \"MS, code window, correct trials (the code's choices)\")\nprint(\"Expected 146 +/- 14.6 cells and 7.8 +/- 0.78 %\")\nprint(\"Null (shuffled new/old labels): mean %.1f units (main), %.1f (code's choices)\" % (NU.ms_all_M.mean(), NU.ms_cor_C.mean()))\n\"\"\", tags=[\"claim:ms-cells-proportion\"])\nmd(result(\"ms-cells-proportion\"))\n\nmd(r\"\"\"\n## dual-cells-proportion\n\n> 26 cells (1.4%) are both visually and memory selective.\n\"\"\")\ncode(r\"\"\"\nfor name, v, m_ in [(\"main (Methods window, all trials)\", \"vs_M\", \"ms_all_M\"), (\"code's choices (1.7 s window, correct trials)\", \"vs_C\", \"ms_cor_C\"),\n                    (\"Methods window, correct trials\", \"vs_M\", \"ms_cor_M\")]:\n    d = (U[v] < 0.05) & (U[m_] < 0.05)\n    print(f\"Dual, {name}: {d.sum()} of {len(U)} ({100*d.mean():.2f}%); trains counted once {(d & ~U.dup).sum()}\")\nprint(\"Expected 26 +/- 2.6 cells and 1.4 +/- 0.14 %\")\n\"\"\", tags=[\"claim:dual-cells-proportion\"])\nmd(result(\"dual-cells-proportion\"))\n\nmd(r\"\"\"\n## fig5f-site-proportions\n\n> The percentages of VS, MS and dual cells are comparable between CS sessions (18.4%, 7.7% and 1.4%) and\n> the new TWH sessions (19.4%, 10.4% and 1.3%).\n\nCriterion: two-sided Fisher's exact test between sites for each cell type; at least four of the six\nvalues within tolerance.\n\"\"\")\ncode(r\"\"\"\nexpected = {(\"CS\", \"VS\"): 18.4, (\"CS\", \"MS\"): 7.7, (\"CS\", \"dual\"): 1.4, (\"TWH\", \"VS\"): 19.4, (\"TWH\", \"MS\"): 10.4, (\"TWH\", \"dual\"): 1.3}\nfor name, v, m_ in [(\"main (Methods window, all trials)\", \"vs_M\", \"ms_all_M\"), (\"code's choices\", \"vs_C\", \"ms_cor_C\")]:\n    sel = {\"VS\": U[v] < 0.05, \"MS\": U[m_] < 0.05, \"dual\": (U[v] < 0.05) & (U[m_] < 0.05)}\n    print(name)\n    within = 0\n    for typ, a in sel.items():\n        cnt = {st: (int(a[U.site == st].sum()), int((U.site == st).sum())) for st in [\"CS\", \"TWH\"]}\n        tab_ = [[cnt[\"CS\"][0], cnt[\"CS\"][1] - cnt[\"CS\"][0]], [cnt[\"TWH\"][0], cnt[\"TWH\"][1] - cnt[\"TWH\"][0]]]\n        p = stats.fisher_exact(tab_).pvalue\n        line = []\n        for st in [\"CS\", \"TWH\"]:\n            pc = 100 * cnt[st][0] / cnt[st][1]\n            ok = abs(pc - expected[(st, typ)]) <= 0.1 * expected[(st, typ)] + 1e-9\n            within += ok\n            line.append(f\"{st} {cnt[st][0]}/{cnt[st][1]} = {pc:.1f}% (exp {expected[(st, typ)]}, {'within' if ok else 'outside'})\")\n        print(f\"  {typ}: \" + \"; \".join(line) + f\"; Fisher p = {p:.3f}\")\n    print(f\"  values within tolerance: {within} of 6\")\n\"\"\", tags=[\"claim:fig5f-site-proportions\"])\nmd(result(\"fig5f-site-proportions\"))\n\nmd(r\"\"\"\n## twh-sessions\n\n> The dataset includes 9 sessions from a new institution, Toronto Western Hospital.\n\"\"\")\ncode(r\"\"\"\ntwh = F[F.label.str.startswith(\"T\")]\nprint(f\"Sessions with a subject label starting with T: {len(twh)} (expected 9 +/- 0.9), subjects {twh.label.nunique()}, units {twh.units.sum()}\")\nprint(twh[[\"session\", \"label\", \"units\"]].to_string())\nprint(\"Institution field of these files:\", collections.Counter(SID[k][\"institution\"] for k in twh.session))\n\"\"\", tags=[\"claim:twh-sessions\"])\nmd(result(\"twh-sessions\"))\n\nmd(r\"\"\"\n## previous-release-link\n\n> The sessions of the earlier release (Faraut et al. 2018) are found in this dandiset under the same\n> subject, session id and task variant.\n\nMatched by session id; a match agrees when the subject label and the variant (from the image\ndirectory, Table 2 of Faraut et al.) are the table's.\n\"\"\")\ncode(r\"\"\"\nfv = F.set_index(\"session\")\nrows = []\nfor r in faraut_t1.itertuples():\n    found = r.session_id in fv.index\n    d = {\"session\": r.session_id, \"label\": r.label, \"variant\": r.variant, \"age\": r.age, \"sex\": r.sex, \"found\": found}\n    if found:\n        x = fv.loc[r.session_id]\n        sj = SID[r.session_id][\"subject\"]\n        d.update({\"file_label\": x.table_label, \"file_variant\": x.variant, \"file_age\": sj.get(\"age\"), \"file_sex\": sj.get(\"sex\")})\n    rows.append(d)\nLK = pd.DataFrame(rows)\nLK[\"agrees\"] = LK.found & (LK.label == LK.file_label) & (LK.variant == LK.file_variant)\nprint(f\"Sessions in Faraut et al. Table 1: {len(LK)}; found by session id: {LK.found.sum()}; agree on subject and variant: {LK.agrees.sum()} ({100*LK.agrees.mean():.1f}%)\")\nprint(\"Not found or not agreeing:\")\nprint(LK[~LK.agrees].to_string())\nm_ = LK[LK.found]\nprint(f\"Age equal: {(m_.age.astype(str) == m_.file_age.astype(str)).sum()} of {len(m_)}; sex equal: {(m_.sex == m_.file_sex).sum()}\")\nprint(m_[(m_.age.astype(str) != m_.file_age.astype(str)) | (m_.sex != m_.file_sex)][[\"session\", \"label\", \"age\", \"file_age\", \"sex\", \"file_sex\"]].to_string())\n\"\"\", tags=[\"claim:previous-release-link\"])\nmd(result(\"previous-release-link\"))\n\nmd(r\"\"\"\n## previous-release-additions\n\n> Relative to the earlier release of this task's data (Faraut et al. 2018), this release adds 23\n> sessions, 17 subjects and 288 neurons.\n\"\"\")\ncode(r\"\"\"\nold_sessions = set(faraut_t1.session_id)\nold_labels = set(faraut_t1.label)\nnew = F[~F.session.isin(old_sessions)]\nnew_subj = set(F.table_label) - old_labels\nprint(f\"New sessions: {len(new)} (expected 23 +/- 2.3): {new.session.tolist()}\")\nprint(f\"New subjects: {len(new_subj)} (expected 17 +/- 1.7): {sorted(new_subj)}\")\nprint(f\"New neurons (unit rows of new sessions): {new.units.sum()} (expected 288 +/- 28.8); trains counted once: {new.units.sum() - sum(1 for d in drop if d[0] in set(new.session))}\")\nprint(f\"Variant, differences of totals: sessions {len(F)} - {len(faraut_t1)} = {len(F)-len(faraut_t1)}; \"\n      f\"subjects {F.table_label.nunique()} - {faraut_t1.label.nunique()} = {F.table_label.nunique()-faraut_t1.label.nunique()}; \"\n      f\"neurons {n_units} - 1576 (Faraut et al. abstract) = {n_units-1576}\")\nprint(\"Sessions of new subjects:\", F[F.table_label.isin(new_subj)].session.tolist())\n\"\"\", tags=[\"claim:previous-release-additions\"])\nmd(result(\"previous-release-additions\"))\n\nmd(r\"\"\"\n## fig4-example-vs-neuron\n\n> Neuron 132-177-4-RA (session 132, channel 177, cell 4, right amygdala) is visually selective, responding most to images of animals.\n\"\"\")\ncode(r\"\"\"\ns = SID[132]\nel = s[\"electrodes\"]\nprint(el[[\"origChannel\", \"location\"]].to_string())\ncand = [i for i, e in enumerate(s[\"unit_electrodes\"]) if el.origChannel.values[e[0]] == 177]\nprint(\"Units on channel 177:\", cand, \" electrode rows:\", [int(s[\"unit_electrodes\"][i][0]) for i in cand],\n      \" origClusterID:\", [int(s[\"origClusterID\"][i]) for i in cand])\nr = rm.recog_trials(s)\nfor i in cand:\n    print(f\"Unit {i}: location {el.location.values[s['unit_electrodes'][i][0]]}, {len(s['spikes'][i])} spikes\")\n    for wn, w in [(\"Methods 0.2-1.2 s\", rm.METHODS_WINDOW), (\"code 0.2-1.7 s\", rm.CODE_WINDOW)]:\n        fr = rm.window_rates(s[\"spikes\"][i], r.start_time.values, w)\n        means = pd.Series(fr).groupby(r.category_name.values).mean().sort_values(ascending=False)\n        print(f\"  {wn}: ANOVA p = {rm.vs_p(fr, r.stimCategory.values):.2e}; mean rate by category (Hz): \" +\n              \", \".join(f\"{k} {v:.2f}\" for k, v in means.items()))\nprint(\"Category names and ids in this session:\", sorted(set(zip(r.stimCategory, r.category_name))))\n\"\"\", tags=[\"claim:fig4-example-vs-neuron\"])\nmd(result(\"fig4-example-vs-neuron\"))\n\nmd(r\"\"\"\n## fig3-example-vs-neuron (blocked)\n\n> Neuron 144-140-3-RH (session 144, channel 140, cell 3, right hippocampus) is visually selective for phones.\n\nSession 144 is not among the dandiset's sessions, nor in Online-only Table 1. The paper's own deposit on\nOSF (doi:10.17605/OSF.IO/HV7JA) is searched below by listing the NWB files in its NWBData.zip.\n\"\"\")\ncode(r\"\"\"\nimport requests, zipfile, remfile\nprint(\"Session 144 in the dandiset:\", 144 in SID, \"; in Online-only Table 1:\", 144 in set(paper_t1.session_id),\n      \"; in Faraut et al. Table 1:\", 144 in set(faraut_t1.session_id))\nosf = requests.get(\"https://api.osf.io/v2/nodes/hv7ja/files/osfstorage/\", timeout=60).json()\nfor x in osf[\"data\"]:\n    name = x[\"attributes\"][\"name\"]\n    if name == \"NWBData.zip\":\n        url = requests.head(x[\"links\"][\"download\"], allow_redirects=True, timeout=60).url\n        names = [n for n in zipfile.ZipFile(remfile.File(url)).namelist() if n.endswith(\".nwb\")]\n        ids = sorted(int(n.split(\"NOID\")[1].split(\".\")[0]) for n in names)\n        print(f\"OSF NWBData.zip: {len(names)} NWB files; session 144 among them: {144 in ids}; same session ids as the dandiset: {set(ids) == set(SID)}\")\n\"\"\")\n\nmd(r\"\"\"\n## Summary\n\nSUMMARY_TODO\n\"\"\")\nmd(result(\"summary\"))\n"
}
```

```
File created successfully at: /tmp/claude-1001/cells.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001; python3 - <<'E'
p='cells.py'; s=open(p).read()
s=s.replace('''print("Column description:", repr(SID[5]["trials"].attrs.get("description", "")) if hasattr(SID[5]["trials"], "attrs") else "")''','''print("Column description in the files:", collections.Counter(s["label_description"] for s in S).most_common())''')
s=s.replace('''md(r"""
## Summary

SUMMARY_TODO
""")
md(result("summary"))''','''md(result("summary"))''')
open(p,'w').write(s)
E
cd entries/chandravadia-2020; python3 - <<'E'
p='recogmem.py'; s=open(p).read()
s=s.replace('''        s["trials_columns"] = [_s(c) for c in f["intervals/trials"].attrs["colnames"]]''','''        s["trials_columns"] = [_s(c) for c in f["intervals/trials"].attrs["colnames"]]
        s["label_description"] = " ".join(_s(f["intervals/trials/new_old_labels_recog"].attrs.get("description", "")).split())''')
open(p,'w').write(s)
E
cat > requirements.in <<'E'
dandi
h5py
matplotlib
numpy
pandas
remfile
requests
scipy
E
cd /tmp/claude-1001; . dev/bin/activate; python build_nb.py cells.py entries/chandravadia-2020/reproduce_chandravadia_2020.ipynb && cd entries/chandravadia-2020 && time jupyter nbconvert --version 2>/dev/null; pip list 2>/dev/null | grep -i -E "nbconvert|nbclient|ipykernel"
```

```
real	0m0.062s
user	0m0.051s
sys	0m0.010s
```

**Agent**

Notebook drafted. Running it in the dev environment (streaming all files) to see the outputs before writing conclusions.

**Agent calls Bash**

```bash
cd /tmp/claude-1001; . dev/bin/activate; cat > runnb.py <<'E'
import nbformat, sys, time
from nbclient import NotebookClient
nb=nbformat.read(sys.argv[1],4); t=time.time()
NotebookClient(nb, timeout=3600, kernel_name='python3', resources={'metadata':{'path':sys.argv[3]}}).execute()
nbformat.write(nb, sys.argv[2]); print('ran in', time.time()-t)
E
python runnb.py entries/chandravadia-2020/reproduce_chandravadia_2020.ipynb out.ipynb entries/chandravadia-2020 2>&1 | tail -20
```

```
print("VS by site (Methods window):", U.groupby("site").vs_M.apply(lambda p: f"{(p<0.05).sum()} of {len(p)}").to_dict())
------------------

----- stdout -----
VS, Methods window (main): 332 of 1864 (17.8%); trains counted once: 326 of 1798 (18.1%)
VS, code window: 343 of 1864 (18.4%); trains counted once: 340 of 1798 (18.9%)
------------------

[31m---------------------------------------------------------------------------[39m
[31mValueError[39m                                Traceback (most recent call last)
[36mCell[39m[36m [39m[32mIn[25][39m[32m, line 7[39m
[32m      3[39m     nd = U[~U.dup]
[32m      4[39m     print(f"{label}: {a.sum()} of {len(U)} ({[32m100[39m*a.mean():.1f}%); trains counted once: {(nd[col] < [32m0.05[39m).sum()} of {len(nd)} ({[32m100[39m*(nd[col] < [32m0.05[39m).mean():.1f}%)")
[32m      5[39m show([33m"vs_M"[39m, [33m"VS, Methods window (main)"[39m)
[32m      6[39m show([33m"vs_C"[39m, [33m"VS, code window"[39m)
[32m----> [39m[32m7[39m print([33m"Expected 343 +/- 34.3 cells and 18.4 +/- 1.84 %; null (shuffled categories) mean %.1f units (Methods window)"[39m % NU.vs_M.mean())
[32m      8[39m print([33m"VS by site (Methods window):"[39m, U.groupby([33m"site"[39m).vs_M.apply([38;5;28;01mlambda[39;00m p: f"{(p<[32m0.05[39m).sum()} of {len(p)}").to_dict())

[31mValueError[39m: unsupported format character ';' (0x3b) at index 47
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001; python3 - <<'E'
p='cells.py'; s=open(p).read()
s=s.replace('''print("Expected 343 +/- 34.3 cells and 18.4 +/- 1.84 %; null (shuffled categories) mean %.1f units (Methods window)" % NU.vs_M.mean())''','''print(f"Expected 343 +/- 34.3 cells and 18.4 +/- 1.84 %; null (shuffled categories) mean {NU.vs_M.mean():.1f} units (Methods window), {NU.vs_C.mean():.1f} (code window)")''')
open(p,'w').write(s)
E
. dev/bin/activate; python build_nb.py cells.py entries/chandravadia-2020/reproduce_chandravadia_2020.ipynb && python runnb.py entries/chandravadia-2020/reproduce_chandravadia_2020.ipynb out.ipynb entries/chandravadia-2020 2>&1 | tail -5; python - <<'E'
import nbformat
nb=nbformat.read('/tmp/claude-1001/out.ipynb',4)
for c in nb.cells:
    if c.cell_type=='code':
        for o in c.outputs:
            if o.output_type=='stream': print(o.text[:6000])
            elif o.output_type=='error': print('ERR', o.ename, o.evalue)
        print('=====')
E
```

```
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
ran in 137.5100827217102
87 NWB files, 6.20 GB on the archive; loaded in 73 s

=====
Dandiset: A NWB-based dataset and processing pipeline of human single-neuron activity during a declarative memory task
Version: 0.220126.1852  DOI: 10.48324/dandi.000004/0.220126.1852
Archive summary: {'numberOfFiles': 87, 'numberOfSubjects': 59, 'numberOfBytes': 6197474020}
Related: [('dcite:IsDerivedFrom', 'DOI:10.17605/OSF.IO/HV7JA'), ('dcite:IsDescribedBy', 'DOI:10.1038/s41597-020-0415-9')]

Online-only Table 1 (this paper): 59 subjects, 87 sessions
Table 1 of Faraut et al. 2018: 42 subjects, 65 sessions
                                        file identifier label table_label  session site       start  learn  recog  old(1)  new(0)  cats  units  electrodes   exp_ids  variant
0   sub-P9HMH_ses-20060301_obj-1otd1m8_eceph      H09_5   H09         H09        5   CS  2006-03-01    100    100      50      50     5     24          14  (80, 81)        1
1   sub-P9HMH_ses-20060301_obj-2arzt6_ecephy      H09_6   H09         H09        6   CS  2006-03-01    100    100      50      50     5     19          13  (83, 84)        2
2   sub-P10HMH_ses-20060901_ecephys+image.nw      H10_7   H10         H10        7   CS  2006-09-01    100    100      50      50     5     38          18  (80, 81)        1
3   sub-P11HMH_ses-20061101_ecephys+image.nw      H11_9   H11         H11        9   CS  2006-11-01    100    100      50      50     5     25           9  (80, 81)        1
4   sub-P14HMH_ses-20070601_obj-1t8wrd5_ecep     H14_17   H14         H14       17   CS  2007-06-01    100    100      50      50     5     23           9  (83, 84)        2
5   sub-P14HMH_ses-20070601_obj-7studd_eceph     H14_18   H14         H14 
[... 382 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001; . dev/bin/activate; python - <<'E'
import sys,pickle,numpy as np,pandas as pd
sys.path.insert(0,'entries/chandravadia-2020')
S=pickle.load(open('S.pkl','rb'))
t=pd.concat([s['trials'].assign(sid=s['session_id']) for s in S])
print(np.mean(np.isclose(t.stop_time,t.delay2_time)), np.mean(np.isclose(t.stop_time,t.stim_off_time)))
d=t.stim_off_time-t.stim_on_time; print(d.describe())
print(t[(t.stop_time-t.start_time<0)|(t.stop_time-t.start_time>100)][['sid','stim_phase','start_time','stim_off_time','delay1_time','response_time','delay2_time','stop_time']])
x=[(s['session_id'], s['trials'].start_time.min()) for s in S if s['trials'].start_time.min()>1e6]; print(x)
E
```

```
1.0 0.44676482665571654
count    17047.000000
mean         1.522082
std          0.500188
min          0.980490
25%          1.003162
50%          1.997660
75%          2.005592
max          2.066093
dtype: float64
     sid stim_phase  ...   delay2_time     stop_time
108   66      recog  ...  2.777819e+03  2.777819e+03
0    123      learn  ...  1.510232e+09  1.510232e+09
1    123      learn  ...  1.510232e+09  1.510232e+09
2    123      learn  ...  1.510232e+09  1.510232e+09
3    123      learn  ...  1.510232e+09  1.510232e+09
..   ...        ...  ...           ...           ...
92   123      learn  ...  1.510232e+09  1.510232e+09
93   123      learn  ...  1.510232e+09  1.510232e+09
94   123      learn  ...  1.510232e+09  1.510232e+09
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001; python3 - <<'E'
p='cells.py'; s=open(p).read()
old='''print("Stimulus duration stop - start (s): %.3f to %.3f, median %.3f" % ((allt.stop_time - allt.start_time).min(),
      (allt.stop_time - allt.start_time).max(), (allt.stop_time - allt.start_time).median()))
print("start_time == stim_on_time in every row:", np.allclose(allt.start_time, allt.stim_on_time))'''
new='''print("start_time == stim_on_time in every row:", np.allclose(allt.start_time, allt.stim_on_time))
print("stop_time == delay2_time (end of trial) in %.3f of rows; stop_time == stim_off_time in %.3f" %
      (np.mean(np.isclose(allt.stop_time, allt.delay2_time)), np.mean(np.isclose(allt.stop_time, allt.stim_off_time))))
dur = allt.stim_off_time - allt.stim_on_time
print("Stimulus duration stim_off_time - stim_on_time (s): %.3f to %.3f; within 0.1 s of 1 s: %d, of 2 s: %d trials" %
      (dur.min(), dur.max(), np.sum(np.abs(dur - 1) < 0.1), np.sum(np.abs(dur - 2) < 0.1)))
epoch = [s["session_id"] for s in S if s["trials"].start_time.min() > 1e8]
print(f"Sessions whose times are Unix timestamps (seconds since 1970) in place of seconds from the start of the recording: {len(epoch)}", epoch)'''
assert old in s; s=s.replace(old,new)
old=s[s.index('''    spk = np.concatenate(s["spikes"])'''):s.index('''""", tags=["sanity"])''', s.index('''    spk = np.concatenate(s["spikes"])'''))]
new='''    spk = np.concatenate(s["spikes"])
    inside = np.mean((t.start_time.values >= spk.min()) & (t.start_time.values <= spk.max()))
    rows.append({"session": s["session_id"], "onsets_in_events": match, "onsets_within_spikes": inside})
C = pd.DataFrame(rows)
print("Fraction of trial start_time values found among the timestamps of event code 1: min %.3f, median %.3f" %
      (C.onsets_in_events.min(), C.onsets_in_events.median()))
print("Sessions where not all trial onsets are event timestamps:", C[C.onsets_in_events < 1].session.tolist())
print("Fraction of trial onsets between the first and last spike of the session: min %.3f; sessions below 1:" % C.onsets_within_spikes.min(),
      C[C.onsets_within_spikes < 1][["session", "onsets_within_spikes"]].round(2).values.tolist())
'''
s=s.replace(old,new)
s=s.replace('''        if shuffle_rng is not None:
            cat = shuffle_rng.permutation(cat)
            lab = shuffle_rng.permutation(lab)''','''        if shuffle_rng is not None:
            # permute the trials' category, label and response together, so that rates lose their trial labels
            perm = shuffle_rng.permutation(len(lab))
            cat, lab, conf = cat[perm], lab[perm], conf[perm]''')
s=s.replace("each session (one permutation per session, applied to all its units; 10 permutations).","each session, category, label and response together (one permutation per session, applied to all its units; 10 permutations). The selection's false-positive rate is 5%, %d units of 1864." .replace("%d","93"))
s=s.replace('''print("Shuffled-label nulls (10 permutations): mean (min to max) units at p < 0.05")''','''print(f"Shuffled-trial nulls (10 permutations): units at p < 0.05 (false-positive rate 5% gives {0.05*len(U):.0f})")''')
old='''print(f"Variant, differences of totals: sessions {len(F)} - {len(faraut_t1)} = {len(F)-len(faraut_t1)}; "
      f"subjects {F.table_label.nunique()} - {faraut_t1.label.nunique()} = {F.table_label.nunique()-faraut_t1.label.nunique()}; "
      f"neurons {n_units} - 1576 (Faraut et al. abstract) = {n_units-1576}")'''
new='''t3 = rm.pmc_table(rm.FARAUT_PMC, "Table 3")
faraut_cells = {r[0]: int(r[1]) for r in t3 if r and r[0] in ("Hippocampus", "Amygdala")}
nf = sum(faraut_cells.values())
print("Faraut et al. Table 3, cells recorded:", faraut_cells, "total", nf)
print(f"Variant, differences of totals: sessions {len(F)} - {len(faraut_t1)} = {len(F)-len(faraut_t1)}; "
      f"subjects {F.table_label.nunique()} - {faraut_t1.label.nunique()} = {F.table_label.nunique()-faraut_t1.label.nunique()}; "
      f"neurons {n_units} - {nf} = {n_units-nf}")
old_units = F[~F.session.isin(new.session)].units.sum()
print(f"Unit rows of the {len(F)-len(new)} sessions of the earlier release in this dandiset: {old_units}, against {nf} in Faraut et al.")'''
assert old in s; s=s.replace(old,new)
old='''print("Sessions of the same subject as session 68, and sessions 67 to 69:")'''
new='''rows = []
for s in S:
    t0_ = s["trials"].start_time.min()
    if t0_ > 1e8:
        rows.append({"session": s["session_id"], "start": s["session_start_time"][:10],
                     "first_trial_utc": pd.to_datetime(t0_, unit="s")})
EP = pd.DataFrame(rows)
EP["same_year_month"] = EP.start.str[:7] == EP.first_trial_utc.dt.strftime("%Y-%m")
print(f"Sessions whose trial times are Unix timestamps: {len(EP)}; their first trial falls in the year and month of session_start_time in {EP.same_year_month.sum()}")
print(f"Days of the month these timestamps give (first trial, UTC): {sorted(EP.first_trial_utc.dt.day.unique().tolist())}")
print(EP[~EP.same_year_month].to_string())
print("Sessions of the same subject as session 68, and sessions 67 to 69:")'''
assert old in s; s=s.replace(old,new)
old='''    print(f"  sessions {a} ({sa['label']}, {len(sa['spikes'])} units) and {b} ({sb['label']}, {len(sb['spikes'])} units): "'''
new='''    ra = (ta.start_time.min(), ta.stop_time.max()); rb = (tb.start_time.min(), tb.stop_time.max())
    print(f"  sessions {a} ({sa['label']}, {len(sa['spikes'])} units) and {b} ({sb['label']}, {len(sb['spikes'])} units): "
          f"trials of {a} {ra[0]:.0f} to {ra[1]:.0f} s, of {b} {rb[0]:.0f} to {rb[1]:.0f} s; "'''
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
E
grep -n "false-positive rate 5%" cells.py | head
```

```
672:print(f"Shuffled-trial nulls (10 permutations): units at p < 0.05 (false-positive rate 5% gives {0.05*len(U):.0f})")
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001; grep -n "response together" cells.py; . dev/bin/activate; python build_nb.py cells.py entries/chandravadia-2020/reproduce_chandravadia_2020.ipynb && python runnb.py entries/chandravadia-2020/reproduce_chandravadia_2020.ipynb out.ipynb entries/chandravadia-2020 2>&1 | grep -v WARNING | tail -3; python - <<'E'
import nbformat
nb=nbformat.read('/tmp/claude-1001/out.ipynb',4)
want=[1,2,3,4,5,14,25,27,29,31,33,37,39,41,43]
for i,c in enumerate(nb.cells):
    if c.cell_type=='code':
        txt=''.join(o.get('text','') for o in c.outputs if o.output_type=='stream')
        err=[o for o in c.outputs if o.output_type=='error']
        if err: print(i,'ERR',err[0].evalue)
        if any(k in txt for k in ['Unix','onsets between','identical trains','Shuffled-trial','Faraut et al. Table 3','MS, ','Dual,','values within','stop_time']): print(i, txt[:3000]); print('====')
E
```

```
629:each session, category, label and response together (one permutation per session, applied to all its units; 10 permutations). The selection's false-positive rate is 5%, 93 units of 1864.
638:            # permute the trials' category, label and response together, so that rates lose their trial labels
ran in 142.95121884346008
4 Files per site: {'CS': 78, 'TWH': 9}  subjects per site: {'CS': 51, 'TWH': 8}
Units per site: {'CS': 1787, 'TWH': 77}  total 1864
Identifier label agrees with subject_id: True
Session id in identifier equals the one in session_description: True
Trials table columns: [(('start_time', 'stop_time', 'stim_on_time', 'stim_off_time', 'delay1_time', 'delay2_time', 'stim_phase', 'stimCategory', 'category_name', 'external_image_file', 'new_old_labels_recog', 'response_value', 'response_time'), 87)]
Units table columns: [(('origClusterID', 'waveform_mean_encoding', 'waveform_mean_recognition', 'IsolationDist', 'SNR', 'waveform_mean_sampling_rate', 'spike_times', 'electrodes'), 87)]
Electrodes table columns: [(('x', 'y', 'z', 'imp', 'location', 'filtering', 'group', 'group_name', 'origChannel'), 87)]
Stimulus series (name, shape): [("{'StimulusPresentation': (200, 400, 300, 3)}", 79), ("{'StimulusPresentation': (150, 400, 300, 3)}", 7), ("{'StimulusPresentation': (197, 400, 300, 3)}", 1)]
NWB versions: Counter({'2.1.0': 87})
Recognition response_value - 30: {1.0: 2544, 2.0: 1039, 3.0: 933, 4.0: 763, 5.0: 894, 6.0: 2527}
Learning response_value: {1.0: 6570, 0.0: 1777}
new_old_labels_recog in learning rows: {'NA': 8347}
Sessions where response_value - 30 differs from the event codes 30 to 36 the paper's code reads: []
start_time == stim_on_time in every row: True
stop_time == delay2_time (end of trial) in 1.000 of rows; stop_time == stim_off_time in 0.447
Stimulus duration stim_off_time - stim_on_time (s): 0.980 to 2.066; within 0.1 s of 1 s: 8250, of 2 s: 8797 trials
Sessions whose times are Unix timestamps (seconds since 1970) in place of seconds fr
[... 87 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd  sed -n 1,80p tools/entry.py | head -80; grep -n "def cmd_\|add_parser" tools/entry.py | head -30
```

```
Sun Nov 15 07:45:12 UTC 2026
"""Lock, check and run one entry. This is the whole local workflow for a deposit.

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
tied to the data:

- every notebook in the directory is listed in entry.yaml, and exists;
- notebooks are committed without outputs;
- the lock file is present and newer requirements are not left unlocked;
[... 61 more lines not kept]
```

**Agent**

Analysis complete (07:45). Writing the conclusions, each backed by printed numbers.

**Agent calls Bash**

```bash
cd /tmp/claude-1001; python3 - <<'E'
p='cells.py'; s=open(p).read()
s=s.replace('''print("Null (shuffled new/old labels): mean %.1f units (main), %.1f (code's choices)" % (NU.ms_all_M.mean(), NU.ms_cor_C.mean()))''','''print("Null (trials shuffled): mean %.1f units (main), %.1f (code's choices)" % (NU.ms_all_M.mean(), NU.ms_cor_C.mean()))''')
s=s.replace('''print(f"Expected 343 +/- 34.3 cells and 18.4 +/- 1.84 %; null (shuffled categories) mean''','''print(f"Expected 343 +/- 34.3 cells and 18.4 +/- 1.84 %; null (trials shuffled) mean''')
s='exec(open("/tmp/claude-1001/results.py").read())\n'+s
s=s.replace('R = globals().get("RESULTS", {})','R = RESULTS')
open(p,'w').write(s)
E
grep -n "RESULTS" cells.py | head
```

```
2:R = RESULTS
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/results.py",
 "content": "RESULTS = {\n\"counts-neurons-subjects\": \"\"\"**Result: reproduced.** The files hold 1864 unit rows (one more than the paper's 1863) from 59 subjects,\nboth within tolerance under reading (a). Counting the 66 spike trains that appear in two files once\ngives 1798, also within tolerance.\"\"\",\n\n\"counts-sessions\": \"\"\"**Result: reproduced.** The 87 (subject, session id) pairs of the files are exactly those of Online-only\nTable 1, and the task variant read from the image directories equals the table's in all 87. The\nMethods' 89 sessions is not what the files hold.\"\"\",\n\n\"table1-demographics\": \"\"\"**Result: partially reproduced.** Age and sex match Online-only Table 1 for 56 of 59 subjects. C24 is 57\nin the files and 47 in the table, H33 30 and 29, and H48 is 32 and female in the files, 54 and male in\nthe table; Faraut et al. 2018 gives the same values as the table for these three (previous-release-link).\nThe files count 26 female and 33 male subjects, against 25 and 34. The diagnosis in the files is a\ncoarser coding; its text equals the table's for 40 of 59 subjects.\"\"\",\n\n\"task-structure\": \"\"\"**Result: partially reproduced.** All 87 sessions have 100 recognition trials with 50 of each label and\n5 categories, but 8 sessions have fewer encoding trials: 7 have 50 (18, 20, 21, 23, 26, 27, 44) and\nsession 123 has 97. Each part holds in more than half of the sessions.\"\"\",\n\n\"new-old-label-coding\": \"\"\"**Result: not reproduced.** The labels are reversed in the files: label 0 trials never show an image of\nthe encoding block (fraction 0.00 in every session) and label 1 trials do, and label 1 trials receive\n\"old\" responses more often (median 0.70 against 0.24). Both tests hold with the labels reversed in 78 of\n87 sessions and under the stated coding in none. In the sessions with 50 encoding trials only part of\nthe label-1 images is in the encoding block (lowest 0.52), and in session 2005 label 1 does not get\nmore \"old\" responses. The column's description in the files states the same reversed coding as the\npaper; the paper's code treats 1 as old.\"\"\",\n\n\"ttl-codes\": \"\"\"**Result: partially reproduced.** In all 87 files events and experiment_ids have the same length and\ntimestamps. 78 files meet every part of the criterion. Nine files hold codes that Table 1 does not list\n(0, 4, 22, 23, 98, 99; 15 events in all), and 28 of 17047 trials in 7 files do not show the order\n1, 2, 3, response, 6. Eight files have no start of experiment marker (55) twice.\"\"\",\n\n\"experiment-ids\": \"\"\"**Result: partially reproduced.** The experiment ids of 83 of 87 files are one of Table 2's pairs. Four\nfiles use other ids: session 55 (80, 82), 77 (81, 82), 100 and 105 (82, 83); the data_collection field\nof each file states the same ids.\"\"\",\n\n\"session-dates\": \"\"\"**Result: partially reproduced.** 86 of 87 files start on the first of a month; session 48 starts on\n2010-03-13. Session 68 (H44) is dated 2000-01-01, six years before the earliest other session (2006),\nand between sessions dated 2013. The trial and event times of 38 files are Unix timestamps; they fall\nin the year and month of session_start_time in all 38, and they give the day of each of these\nrecordings (first trials on 23 different days of the month), which the date field was set to hide.\"\"\",\n\n\"units-table\": \"\"\"**Result: partially reproduced.** Every file holds the listed columns, with IsolDist named IsolationDist;\nevery unit links to one electrode; the waveform sampling rate is 98400 Hz in every file, within\ntolerance of 100 kHz. The quality metrics are not finite for every unit: SNR is missing or infinite\nfor 86 of 1864 units (75 nan, 11 inf), IsolationDist is nan for 493, and two IsolationDist values\nexceed 1e6 (largest 8.08e32). 84 of 87 files have a unit with a non-finite metric.\"\"\",\n\n\"electrodes-table\": \"\"\"**Result: not reproduced.** Location, filtering (300-3000Hz) and origChannel are filled for all 887\nelectrodes, but impedance is empty for every electrode in every file, which the criterion counts as not\nreproduced. The x, y, z coordinates are empty for 99 electrodes in 8 sessions.\"\"\",\n\n\"isi-criterion\": \"\"\"**Result: partially reproduced.** With spike times sorted, 1858 of 1864 units (99.68%) have fewer than 3%\nof intervals below 3 ms; four units are at 3.0 to 9.0% (sessions 66, 124, 126) and two units of session\n58 at 50%, because every spike of these two is stored twice (1634 and 412 repeated times) and the train\nis not sorted. Stored order gives 1860 of 1864. 13 units in 7 sessions have spike times not sorted in\ntime.\"\"\",\n\n\"fig5a-mtl-locations\": \"\"\"**Result: reproduced.** All 1864 units are on electrodes in the left or right amygdala (1092) or\nhippocampus (772).\"\"\",\n\n\"fig5c-auc-all\": \"\"\"**Result: reproduced.** The mean AUC over the 87 sessions is 0.753 with SD 0.094 (expected 0.74 and\n0.10), and 86 sessions are above 0.5. With the paper's stated label coding the mean would be 0.247,\nwhich is how the reversed labels show in behaviour.\"\"\",\n\n\"fig5c-auc-sites\": \"\"\"**Result: reproduced.** CS sessions (78) have a mean AUC of 0.760 with SD 0.085, TWH sessions (9) 0.688\nwith SD 0.138; all four values are within tolerance. The sites do not differ by Welch's t-test\n(p = 0.161).\"\"\",\n\n\"fig5b-roc-asymmetric\": \"\"\"**Result: reproduced.** The mean z-ROC slope over 82 sessions is 0.782, below 1 by a two-sided t-test\n(p = 4.3e-09); 65 sessions have a slope below 1, the Wilcoxon test gives p = 2.0e-08 and the pooled ROC\nhas slope 0.816. Five sessions have fewer than two distinct false alarm points and no slope.\"\"\",\n\n\"fig5d-confidence-accuracy\": \"\"\"**Result: reproduced.** With the fixed split, accuracy is 80.1% for high and 60.9% for low confidence\nover 84 sessions (paired t-test p = 3.2e-16); with the Python code's dynamic split 78.2% and 60.8% over\n82 sessions (p = 1.3e-11). The unpaired tests and the code's session inclusion also give p below 1e-10.\"\"\",\n\n\"vs-cells-proportion\": \"\"\"**Result: reproduced.** With the Methods' window 332 of 1864 units (17.8%) are visually selective, within\ntolerance of 343 (18.4%); the code's window gives 343 (18.4%). Shuffling the trials gives 86.8 units on\naverage, so the count is well above chance.\"\"\",\n\n\"ms-cells-proportion\": \"\"\"**Result: not reproduced.** With the Methods' window and all 50 and 50 trials, 112 units (6.0%) are memory\nselective, below the tolerance of 146 (131.4 to 160.6); five other seeds give 108 to 117. The\nshuffled-trial null gives 92.4 on average. With the paper's code's choices, correct trials only and the\n0.2 to 1.7 s window, 151 units (8.1%) are selected, within tolerance, and 141 to 153 over the five\nseeds. The paper's numbers follow its code, not its Methods text.\"\"\",\n\n\"dual-cells-proportion\": \"\"\"**Result: not reproduced.** With the main tests 12 units (0.64%) are both VS and MS, against 26 (1.4%).\nWith the code's choices exactly 26 units (1.39%) are, and 24 to 26 over five other seeds.\"\"\",\n\n\"fig5f-site-proportions\": \"\"\"**Result: partially reproduced.** With the main tests no Fisher test finds a difference between the sites\n(p = 0.360, 0.133, 0.398), but only 3 of the 6 percentages are within tolerance: CS 17.6, 5.8 and 0.6%,\nTWH 22.1, 10.4 and 1.3%. With the code's choices all six are within tolerance (CS 18.4, 8.0, 1.4%;\nTWH 19.5, 10.4, 1.3%) and no test finds a difference.\"\"\",\n\n\"twh-sessions\": \"\"\"**Result: reproduced.** Nine sessions, of 8 subjects with 77 units, have labels starting with T, and their\ninstitution field is Toronto Western Hospital.\"\"\",\n\n\"previous-release-link\": \"\"\"**Result: partially reproduced.** Of the 65 sessions in Table 1 of Faraut et al. 2018, 64 (98.5%) are in\nthe dandiset under the same subject and variant. Session 98 (H48, variant 2) is not in it, nor in\nOnline-only Table 1. Of the matched sessions, age differs for 4 (sessions 52, 59, 60, 99) and sex for 1\n(99), the same three subjects that differ from Online-only Table 1.\"\"\",\n\n\"previous-release-additions\": \"\"\"**Result: partially reproduced.** The dandiset has 23 sessions and 17 subjects that are not in the\nearlier release, as stated, but the new sessions hold 325 unit rows, outside the tolerance of 288. The\ndifference of the totals is exactly 288 (1864 - 1576), so the 64 earlier sessions hold 1539 units here\nagainst the 1576 cells of Faraut et al. Table 3: the paper's 288 matches a difference of totals, not\nthe units of the new sessions.\"\"\",\n\n\"fig4-example-vs-neuron\": \"\"\"**Result: reproduced.** Session 132 has one unit on channel 177, unit 4 on electrode row 4, in the right\namygdala. Its rate differs across the 5 categories (ANOVA p = 1.2e-22, Methods' window; 7.9e-19, code's\nwindow), and it fires most to animals (6.75 Hz against at most 0.85 Hz for the other categories).\"\"\",\n\n\"summary\": \"\"\"## Summary\n\n| Claim | Outcome |\n|---|---|\n| counts-neurons-subjects | reproduced |\n| counts-sessions | reproduced |\n| table1-demographics | partially reproduced |\n| task-structure | partially reproduced |\n| new-old-label-coding | not reproduced |\n| ttl-codes | partially reproduced |\n| experiment-ids | partially reproduced |\n| session-dates | partially reproduced |\n| units-table | partially reproduced |\n| electrodes-table | not reproduced |\n| isi-criterion | partially reproduced |\n| fig5a-mtl-locations | reproduced |\n| fig5c-auc-all | reproduced |\n| fig5c-auc-sites | reproduced |\n| fig5b-roc-asymmetric | reproduced |\n| fig5d-confidence-accuracy | reproduced |\n| vs-cells-proportion | reproduced |\n| ms-cells-proportion | not reproduced |\n| dual-cells-proportion | not reproduced |\n| fig5f-site-proportions | partially reproduced |\n| twh-sessions | reproduced |\n| previous-release-link | partially reproduced (with Faraut et al. 2018) |\n| previous-release-additions | partially reproduced (with Faraut et al. 2018) |\n| fig4-example-vs-neuron | reproduced |\n| fig3-example-vs-neuron | blocked (data_missing) |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and\nthe differences from the paper's method.\n\nHow the analysis differs from the paper's: the behaviour and the cell selections follow the paper's\ncode (see `recogmem.py`); the MS and dual claims are judged on the Methods' description (1 s window,\nall trials), as the claims file fixes, and the code's choices (1.5 s window, correct trials only), which\ngive the paper's numbers, are shown as variants. Firing rates use the trial's start_time as stimulus\nonset, as the code does. The bootstrap seed is a standard choice; the spread over seeds is shown.\n\nWhat was found about the dataset:\n\n- new_old_labels_recog is 1 for old and 0 for new stimuli, the reverse of the paper's text and of the\n  column's own description.\n- The electrodes' impedance is empty in every file; coordinates are empty in 8 sessions.\n- SNR or IsolationDist is not finite for many units, and IsolDist is named IsolationDist.\n- Three subjects have an age or sex that differs from both papers' patient tables.\n- 8 sessions have 50 or 97 encoding trials, not 100.\n- Four files use experiment ids outside Table 2, and nine hold event codes outside Table 1.\n- 38 files store times as Unix timestamps, which give the exact day of recording that\n  session_start_time was set to hide; session 48 is dated on the 13th and session 68 in 2000.\n- stop_time is the end of the trial, not the stimulus offset as the paper describes; stim_off_time\n  holds the offset.\n- The same spike trains are in two files for sessions 38 and 39 (11 units), 43 and 44 (23) and 54 and\n  55 (32): sessions recorded in one continuous recording, whose units are the same neurons.\n- Two units of session 58 store every spike twice, and 13 units have spike times out of order.\n- Session 144, of the Figure 3 example neuron, is in neither the dandiset nor the paper's OSF deposit.\n\"\"\",\n}\n"
}
```

```
File created successfully at: /tmp/claude-1001/results.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001; python3 - <<'E'
p='results.py'; s=open(p).read()
s=s.replace("(0, 4, 22, 23, 98, 99; 15 events in all)","(0, 4, 22, 23, 98, 99; 14 events in all)")
s=s.replace("Eight files have no start of experiment marker (55) twice.","Eight files do not hold the start of experiment marker (55) twice, and one holds the end marker (66) three times.")
open(p,'w').write(s)
p='cells.py'; s=open(p).read()
s=s.replace('''print("Sessions where label 1 gets fewer 'old' responses than label 0:", N[N.label1_oldresp <= N.label0_oldresp].session.tolist())''','''print("Sessions where label 1 gets fewer 'old' responses than label 0:", N[N.label1_oldresp <= N.label0_oldresp].session.tolist())
print("Sessions where not every label-1 image is in the encoding block (fraction):", N[N.label1_seen < 1][["session", "label1_seen"]].round(2).values.tolist())''')
open(p,'w').write(s)
E
. dev/bin/activate; python build_nb.py cells.py entries/chandravadia-2020/reproduce_chandravadia_2020.ipynb && echo ok
```

```
ok
Shell cwd was reset to
```

**Agent**

Now entry.yaml, README, and lock + run via the registry tool.

**Agent calls Bash**

```bash
cd entries/chandravadia-2020; cat > entry.yaml <<'E'
schema_version: 1
name: chandravadia-2020
type: reproduction
title: Human MTL single neurons during recognition memory (Chandravadia et al. 2020)
description: Tests the claims of Chandravadia, Liang, Schjetnan et al. (2020) on dandiset 000004, which
  holds 87 sessions of single neurons recorded in the amygdala and hippocampus of 59 epilepsy patients
  during a new/old recognition memory task. It checks the file contents against the data descriptor
  (trials, event markers, units and electrodes tables, subject metadata), the behavioural ROC analysis,
  the proportions of visually and memory selective cells, and the link to the earlier release of
  Faraut et al. (2018).
license: Apache-2.0
notebooks:
- path: reproduce_chandravadia_2020.ipynb
  title: Reproducing Chandravadia et al. (2020) from dandiset 000004
  runtime_minutes: 4
helpers:
- recogmem.py
related:
- id: dandi:000004/0.220126.1852
  relation: uses_data
- id: doi:10.1038/s41597-020-0415-9
  relation: reproduces
E
cat ../fouke-2025/README.md | head -30
```

```
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
| DC turn less than ZF to monocular stimuli | Reproduced |
| ZF swim in bouts, DC continuously | Reproduced |
| Values from representative trials (Figure 1C, E, F) | Blocked: metadata insufficient |
[... 9 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/chandravadia-2020/README.md",
 "content": "# Chandravadia, Liang, Schjetnan et al. (2020) from dandiset 000004\n\nTests the claims of [Chandravadia et al. (2020)](https://doi.org/10.1038/s41597-020-0415-9), a data\ndescriptor, on [DANDI:000004](https://dandiarchive.org/dandiset/000004/0.220126.1852), which holds 87\nsessions of single neurons recorded in the human amygdala and hippocampus during a new/old recognition\nmemory task.\n\n| Claim | Outcome |\n|---|---|\n| 1863 neurons from 59 subjects | Reproduced |\n| 87 sessions, as listed in Online-only Table 1 | Reproduced |\n| Age and sex of each subject as in Online-only Table 1 | Partially reproduced |\n| 100 encoding and 100 recognition trials (50 new, 50 old), 5 categories per session | Partially reproduced |\n| new_old_labels_recog is 0 for old and 1 for new | Not reproduced |\n| TTL event codes and their order | Partially reproduced |\n| Experiment ids of the learning and recognition blocks | Partially reproduced |\n| session_start_time set to the first of the month | Partially reproduced |\n| Units table columns and quality metrics | Partially reproduced |\n| Electrodes table: location, coordinates, impedance, filter, channel | Not reproduced |\n| Fewer than 3% of interspike intervals below 3 ms | Partially reproduced |\n| All neurons in the amygdala or hippocampus | Reproduced |\n| Mean behavioural AUC 0.74 ± 0.10 | Reproduced |\n| AUC by site, CS 0.74 ± 0.09 and TWH 0.69 ± 0.13 | Reproduced |\n| Asymmetric ROC | Reproduced |\n| Higher accuracy at high confidence | Reproduced |\n| 343 VS cells (18.4%) | Reproduced |\n| 146 MS cells (7.8%) | Not reproduced |\n| 26 cells both VS and MS (1.4%) | Not reproduced |\n| Comparable proportions at the two sites | Partially reproduced |\n| 9 sessions from Toronto Western Hospital | Reproduced |\n| Sessions of the earlier release (Faraut et al. 2018) are in the dandiset | Partially reproduced |\n| 23 sessions, 17 subjects and 288 neurons added to the earlier release | Partially reproduced |\n| Example VS neuron 132-177-4-RA prefers animals | Reproduced |\n| Example VS neuron 144-140-3-RH prefers phones | Blocked: data missing |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and\nthe differences from the paper's method.\n\nThe MS and dual counts are judged on the Methods' description (a 1 s window, all trials); the paper's\ncode (a 1.5 s window, correct trials only) gives the paper's numbers, shown as a variant. The new/old\nlabels in the files are the reverse of the stated coding. The attempt record, with the reasons and the\ndifferences from the paper's method, is\n[`attempts/chandravadia-2020-02.yaml`](../../attempts/chandravadia-2020-02.yaml).\n"
}
```

```
File created successfully at: entries/chandravadia-2020/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python -c "import yaml,jsonschema,nbformat" 2>&1; python tools/entry.py lock entries/chandravadia-2020 2>&1 | tail -5; python tools/entry.py check entries/chandravadia-2020 2>&1 | tail -20
```

```
wrote chandravadia-2020/requirements.lock.txt (Python 3.13, with hashes)
0 error(s)
```

**Agent calls Bash**

```bash
cd  date -u; time python tools/entry.py all entries/chandravadia-2020 2>&1 | tail -15
```

```
Sun Nov 15 07:46:32 UTC 2026
Installed kernelspec registry-chandravadia-2020 in executed/chandravadia-2020/.venv/share/jupyter/kernels/registry-chandravadia-2020
0 error(s)
pass  reproduce_chandravadia_2020.ipynb  (144 s)

real	2m32.364s
user	1m8.776s
sys	0m3.246s
```

**Agent**

Clean run passes in 144 s. Checking the executed copy against the conclusions:

**Agent calls Bash**

```bash
cd  ls executed/chandravadia-2020/; python - <<'E'
import nbformat,glob
p=glob.glob('executed/chandravadia-2020/*.ipynb')[0]
nb=nbformat.read(p,4)
for c in nb.cells:
    if c.cell_type=='code':
        t=''.join(o.get('text','') for o in c.outputs if o.output_type=='stream')
        e=[o for o in c.outputs if o.output_type=='error']
        if e: print('ERR',e[0].evalue)
        for k in ['label-1 image','Both tests hold','MS, Methods window, all','Dual, main','values within','VS, Methods','New neurons','z-ROC slope over','(a) fixed','AUC over','loaded in','Units responsive','Sessions with more']:
            for line in t.splitlines():
                if k in line: print(line)
E
```

```
reproduce_chandravadia_2020.ipynb
result.json
87 NWB files, 6.20 GB on the archive; loaded in 71 s
Units responsive to onset (p<0.05): {'true': 671, '+3s': 255, '-3s': 343} of 1864
Sessions with more responsive units at the true onsets than at either shift: 68 of 87
Sessions where not every label-1 image is in the encoding block (fraction): [[18.0, 0.58], [20.0, 0.58], [21.0, 0.52], [23.0, 0.52], [26.0, 0.58], [27.0, 0.52], [44.0, 0.52], [123.0, 0.98]]
Both tests hold under the stated coding (0 = old) in 0 of 87 sessions; with the labels reversed in 78
AUC over 87 sessions: mean 0.753 (expected 0.74 +/- 0.10), SD 0.094 (expected 0.10 +/- 0.01); range 0.445 to 0.919
z-ROC slope over 82 sessions (5 without two distinct false alarm points): mean 0.782, SD 0.300, median 0.791, range 0.00 to 1.67
(a) fixed split: 84 sessions (3 left out); high 80.1%, low 60.9%, difference 19.2 points; high > low in 73 sessions
VS, Methods window (main): 332 of 1864 (17.8%); trains counted once: 326 of 1798 (18.1%)
MS, Methods window, all trials (main): 112 of 1864 (6.0%); trains counted once: 106 of 1798 (5.9%)
Dual, main (Methods window, all trials): 12 of 1864 (0.64%); trains counted once 11
  values within tolerance: 3 of 6
  values within tolerance: 6 of 6
New neurons (unit rows of new sessions): 325 (expected 288 +/- 28.8); trains counted once: 325
```

**Agent**

Executed outputs match the conclusions. Writing the attempt record.

**Agent calls Write**

```json
{
 "file_path": "attempts/chandravadia-2020-02.yaml",
 "content": "schema_version: 3\nid: chandravadia-2020-02\ndatasets:\n- archive: dandi\n  id: \"000004\"\n  version: 0.220126.1852\n  doi: 10.48324/dandi.000004/0.220126.1852\n  relation: primary\npaper: doi:10.1038/s41597-020-0415-9\ndate: 2026-11-15\nentry: chandravadia-2020\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-15\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/43689559719\ninputs:\n- what: Online-only Table 1 of the paper (subjects, session ids, variants, age, sex, diagnosis), read\n    at run time from Europe PMC's full text of the open access article (PMC7055261); the reference\n    list for counts-sessions, table1-demographics and the previous-release claims.\n  source: doi:10.1038/s41597-020-0415-9\n- what: Table 1 (sessions, subjects, variants, age and sex) and Table 3 (cells recorded per area) of\n    Faraut et al. 2018, the earlier release, read at run time from Europe PMC (PMC5810422); used by\n    previous-release-link and previous-release-additions.\n  source: doi:10.1038/sdata.2018.10\n- what: The paper's analysis code (single_neuron.py, helper.py, behavior_all.py, plotFigure5.ipynb and\n    the MATLAB helpers adjustHF.m, calcROC_AUC.m, calcZROCSlope.m, bootstrapMeanEqualTest.m,\n    NO_behavior_evaluateSessionStatus.m), read for method details; nothing is imported from it.\n  source: https://github.com/rutishauserlab/recogmem-release-NWB at commit 1d95162d2672e71dd234a31e4b8d70017a289ee3\n- what: The file list of NWBData.zip in the paper's OSF deposit, searched for session 144 (the block of\n    fig3-example-vs-neuron).\n  source: doi:10.17605/OSF.IO/HV7JA\noutcomes:\n- claim: counts-neurons-subjects\n  outcome: reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:counts-neurons-subjects\n  measured:\n  - 1864\n  - 59\n  notes: Reading (a), every unit row of the 87 files, gives 1864 units (one more than 1863) from 59\n    subject_id values. Reading (b), with the 66 spike trains that appear in two files counted once,\n    gives 1798, also within tolerance.\n- claim: counts-sessions\n  outcome: reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:counts-sessions\n  measured: 87\n  notes: The 87 (subject, session id) pairs of the files equal those of Online-only Table 1, and the\n    variant read from each file's image directory equals the table's in all 87. The Methods' 89 does\n    not match the files or the table.\n  deviations:\n  - The file labels (P9HMH, P24CS, TWH088) are mapped to the table's (H09, C24, T88); the identifier\n    field of each file already uses the table's form for H and T and CS for C.\n- claim: table1-demographics\n  outcome: partially_reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:table1-demographics\n  measured:\n  - 26\n  - 33\n  notes: Age and sex match for 56 of 59 subjects. C24 is 57 in the files and 47 in the table, H33 30\n    and 29, H48 32 and female in the files against 54 and male in the table; Faraut et al. 2018 agrees\n    with the table for all three. The files count 26 female and 33 male subjects (expected 25 and 34,\n    both within tolerance). The files' diagnosis uses a coarser coding (for example Right Other for\n    Right Insula); its text equals the table's for 40 of 59 subjects.\n- claim: task-structure\n  outcome: partially_reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:task-structure\n  notes: All 87 sessions have 100 recognition trials with 50 of each label and 5 categories. 79 have\n    100 encoding trials of 100 distinct images; sessions 18, 20, 21, 23, 26, 27 and 44 have 50 and\n    session 123 has 97. The stored image series has one image per trial in every file. The paper's\n    code handles 150 and 197 trial sessions, so these sessions are known to it.\n- claim: new-old-label-coding\n  outcome: not_reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:new-old-label-coding\n  notes: The labels are reversed. In every session no label-0 trial shows an image of the encoding\n    block, while label-1 trials do (all of them in 79 sessions, 0.52 to 0.98 in the 8 sessions with\n    fewer encoding trials). Label 1 receives more \"old\" responses (median fraction 0.70 against 0.24),\n    except in session 2005. Both tests hold with the labels reversed in 78 of 87 sessions and under the\n    stated coding in none. The column description in the files states the same coding as the paper\n    (0 old); the paper's code uses 1 as old, as does every other claim here.\n- claim: ttl-codes\n  outcome: partially_reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:ttl-codes\n  notes: Events and experiment_ids have the same length and timestamps in all 87 files. 78 files meet\n    every part. Nine files (43, 58, 93, 123, 127, 128, 2001, 2002, 2003) hold 14 events with codes\n    not in Table 1 (0, 4, 22, 23, 98, 99), and 28 of 17047 trials in 7 of them do not show 1, 2, 3,\n    response, 6 in order. Eight files do not hold the start marker 55 twice, and session 2001 holds 66\n    three times.\n- claim: experiment-ids\n  outcome: partially_reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:experiment-ids\n  notes: 83 of 87 files use one of Table 2's pairs. Session 55 uses (80, 82), 77 (81, 82), 100 and 105\n    (82, 83), as their data_collection fields also state.\n  deviations:\n  - Each block's id is read from the experiment_ids entry at the time of its trials' onsets.\n- claim: session-dates\n  outcome: partially_reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:session-dates\n  notes: 86 of 87 files start on the first of a month; session 48 starts on 2010-03-13. Session 68\n    (H44) is dated 2000-01-01, while the other sessions span 2006 to 2019 and sessions 67 and 69 are\n    dated 2013. In 38 files the trial and event times are Unix timestamps; the first trial falls in the\n    year and month of session_start_time in all 38, and the timestamps give the day of each recording\n    (23 different days of the month), the detail the date field was set to protect.\n- claim: units-table\n  outcome: partially_reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:units-table\n  measured: 98400\n  notes: Every file has the listed columns, with IsolDist named IsolationDist (taken as the same\n    column); every unit links to one electrode; waveform_mean_sampling_rate is 98400 Hz for every unit,\n    within tolerance. SNR is nan for 75 units and inf for 11, IsolationDist nan for 493 of 1864, and two\n    IsolationDist values exceed 1e6 (up to 8.08e32); 84 of 87 files have such a unit.\n- claim: electrodes-table\n  outcome: not_reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:electrodes-table\n  notes: Location, filtering (300-3000Hz) and origChannel are filled for all 887 electrodes. The imp\n    column is empty (nan) for every electrode in every file, which the criterion counts as not\n    reproduced. x, y and z are empty for 99 electrodes in sessions 7, 20, 21, 23, 24, 50, 52 and 2004.\n- claim: isi-criterion\n  outcome: partially_reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:isi-criterion\n  measured: 99.68\n  notes: With spike times sorted, 1858 of 1864 units (99.68%) have fewer than 3% of intervals below\n    3 ms (median 0.19%). Four units are at 3.0 to 9.0% (sessions 66, 124, 126); two units of session\n    58 are at 50% because every spike is stored twice. With the stored order 1860 units pass. 13 units\n    in 7 sessions have spike times out of order.\n- claim: fig5a-mtl-locations\n  outcome: reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:fig5a-mtl-locations\n  notes: All 1864 units are on electrodes labelled left or right amygdala (1092) or hippocampus (772).\n- claim: fig5c-auc-all\n  outcome: reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:fig5c-auc-all\n  measured:\n  - 0.753\n  - 0.094\n  notes: AUC over 87 sessions, mean 0.753 and SD 0.094, range 0.445 to 0.919; 86 sessions above 0.5.\n    Under the stated label coding (0 old) the mean would be 0.247. Without the second file of each\n    pair that shares spike trains, mean 0.753 and SD 0.095.\n  deviations:\n  - The confidence response is response_value minus 30; it equals the event codes the paper's code\n    reads in every session.\n- claim: fig5c-auc-sites\n  outcome: reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:fig5c-auc-sites\n  measured:\n  - 0.760\n  - 0.688\n  - 0.085\n  - 0.138\n  notes: CS (78 sessions) mean 0.760 and SD 0.085; TWH (9 sessions) mean 0.688 and SD 0.138; all\n    within tolerance. Welch's t-test between sites t = 1.53, p = 0.161.\n- claim: fig5b-roc-asymmetric\n  outcome: reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:fig5b-roc-asymmetric\n  measured: 0.782\n  notes: Mean z-ROC slope 0.782 over 82 sessions (SD 0.300), below 1 by a two-sided t-test (t = -6.58,\n    p = 4.3e-09); 65 sessions below 1. Wilcoxon p = 2.0e-08; pooled ROC slope 0.816. Five sessions\n    have fewer than two distinct false alarm points among the five interior points and no slope.\n- claim: fig5d-confidence-accuracy\n  outcome: reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:fig5d-confidence-accuracy\n  notes: Fixed split (reading a), 84 sessions (93, 99 and 2008 have no responses in one group), high\n    80.1% and low 60.9%, paired t = 10.16, p = 3.2e-16; dynamic split (reading b), 82 sessions, 78.2%\n    and 60.8%, p = 1.3e-11. Unpaired and Welch tests give p of 3.4e-17 to 8.3e-14, and the code's\n    session inclusion (73 sessions) p = 2.4e-13 paired.\n  deviations:\n  - The Python code's dynamic split, used as written, counts only response 4 as low-confidence \"old\"\n    in its mode 1, where NO_dynamic_lowHighSplit.m counts 4 or 5.\n- claim: vs-cells-proportion\n  outcome: reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:vs-cells-proportion\n  measured:\n  - 332\n  - 17.8\n  notes: Methods' window (0.2 to 1.2 s), 332 of 1864 units (17.8%); code window (0.2 to 1.7 s) 343\n    (18.4%); trains counted once 326 of 1798 (18.1%). Shuffling trials within sessions gives 86.8 units\n    on average (76 to 102). The spikes and trial onsets share a clock in 68 of 87 sessions by the onset\n    response contrast in the data check; in the other 19, mostly with few units, it could not be shown.\n  deviations:\n  - Stimulus onset is the trial's start_time and the rate counts spikes strictly inside the window, as\n    single_neuron.py does (extract_neuron_data_from_nwb, win_spike_rate).\n  - The ANOVA groups trials by stimCategory (values 1 to 5 in every session), as vs_test does.\n- claim: ms-cells-proportion\n  outcome: not_reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:ms-cells-proportion\n  measured:\n  - 112\n  - 6.0\n  notes: Methods' window and all 50 and 50 trials give 112 units (6.0%), outside 146 +/- 14.6; five\n    other seeds give 108 to 117, and the shuffled-trial null 92.4 on average (78 to 104), against 93\n    expected by the 5% false-positive rate. The code's choices (correct trials only, 0.2 to 1.7 s, as\n    ms_test in single_neuron.py) give 151 (8.1%), within tolerance, 141 to 153 over the five seeds;\n    correct trials in the Methods' window give 137 (7.3%); all trials in the code's window 105.\n  deviations:\n  - The bootstrap follows ms_test and bootstrapMeanEqualTest.m (groups shifted to the pooled mean,\n    resampled within group, 1000 runs, two-tailed); the seed is a standard choice and the spread over\n    seeds is shown.\n- claim: dual-cells-proportion\n  outcome: not_reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:dual-cells-proportion\n  measured:\n  - 12\n  - 0.64\n  notes: With the main VS and MS tests 12 units (0.64%) are both, outside 26 +/- 2.6 (12 to 14 over\n    five other seeds). With the code's choices exactly 26 units (1.39%), 24 to 26 over the seeds.\n    It follows from the MS result.\n- claim: fig5f-site-proportions\n  outcome: partially_reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:fig5f-site-proportions\n  measured:\n  - 17.6\n  - 5.8\n  - 0.6\n  - 22.1\n  - 10.4\n  - 1.3\n  notes: With the main tests no Fisher test differs between sites (VS p = 0.360, MS 0.133, dual 0.398),\n    but only 3 of 6 values are within tolerance (CS VS 17.6%, TWH MS 10.4%, TWH dual 1.3%). With the\n    code's choices all six are (CS 18.4, 8.0, 1.4%; TWH 19.5, 10.4, 1.3%) and no test differs\n    (p 0.397 to 1.0). TWH has 77 units, so one cell moves its percentages by 1.3 points.\n- claim: twh-sessions\n  outcome: reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:twh-sessions\n  measured: 9\n  notes: Nine sessions (2001 to 2011, 8 subjects, 77 units) have labels starting with T; their\n    institution field is Toronto Western Hospital.\n- claim: previous-release-link\n  outcome: partially_reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:previous-release-link\n  notes: Of 65 sessions in Table 1 of Faraut et al. 2018, 64 (98.5%) are found by session id with the\n    same subject and variant. Session 98 (H48, variant 2) is in neither the dandiset nor Online-only\n    Table 1. Of the matched sessions, age differs for 52 (H33, 29 against 30), 59 and 60 (C24, 47\n    against 57) and 99 (H48, 54 against 32), and sex for 99 (M against F).\n  deviations:\n  - The variant of a file is read from the directory of its image files (newolddelay, newolddelay2,\n    newolddelay3), the directories Table 2 of Faraut et al. names for the three variants.\n- claim: previous-release-additions\n  outcome: partially_reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:previous-release-additions\n  measured:\n  - 23\n  - 17\n  - 325\n  notes: 23 new sessions (122 to 136 and 2001 to 2011) and 17 new subjects, as stated; the new\n    sessions hold 325 unit rows, outside 288 +/- 28.8. The differences of the totals are 22 sessions,\n    17 subjects and exactly 288 neurons (1864 against the 1576 cells of Faraut et al. Table 3); the 64\n    earlier sessions hold 1539 units here. The partial link (session 98 missing) does not change the\n    new counts, since session 98 is not in the dandiset.\n  depends_on_note: previous-release-link is partially reproduced.\n- claim: fig4-example-vs-neuron\n  outcome: reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:fig4-example-vs-neuron\n  notes: Session 132 has one unit on channel 177, unit 4 on electrode row 4, right amygdala,\n    origClusterID 551. ANOVA across the 5 categories p = 1.2e-22 (Methods' window) and 7.9e-19 (code's\n    window); mean rate 6.75 Hz for animals against 0.25 to 0.85 Hz for the other categories.\n- claim: fig3-example-vs-neuron\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Session 144 is not in the dandiset, nor in Online-only Table 1 or Faraut et al. Table 1. The\n    paper's OSF deposit (NWBData.zip) holds the same 87 sessions as the dandiset, without 144 (listed\n    in the notebook); NativeData.zip was listed while preparing and holds no file with 144 in its name.\nfindings:\n- kind: metadata_error\n  statement: new_old_labels_recog is 1 for old stimuli (shown in the encoding block) and 0 for new\n    ones in every session, the reverse of the column's description in the files (\"0 == Old Stimuli\")\n    and of the paper's Data Records. The responses agree with 1 as old (median fraction of \"old\"\n    responses 0.70 for label 1 against 0.24 for label 0).\n- kind: data_missing\n  statement: The electrodes' impedance (imp) is empty for all 887 electrodes of all 87 files, and the\n    MNI coordinates are empty for 99 electrodes in sessions 7, 20, 21, 23, 24, 50, 52 and 2004, though\n    the paper describes both as part of the electrodes table.\n- kind: metadata_error\n  statement: The units' quality metrics are often not usable. SNR is nan for 75 units and inf for 11,\n    IsolationDist is nan for 493 of 1864 units and reaches 8.08e32 in one, and 84 of 87 files have a\n    unit with a non-finite metric. The column the paper calls IsolDist is named IsolationDist.\n- kind: metadata_error\n  statement: Age or sex of three subjects differs from both Online-only Table 1 and Faraut et al. 2018\n    Table 1. C24 is 57 in the files and 47 in both tables, H33 30 against 29, and H48 is 32 and female\n    in the files against 54 and male. The files therefore count 26 female and 33 male subjects, against\n    25 and 34.\n- kind: other\n  about: data\n  statement: Eight sessions do not have the 100 encoding trials the paper describes for every session.\n    Sessions 18, 20, 21, 23, 26, 27 and 44 have 50 and session 123 has 97; in these sessions some of\n    the 50 old recognition images are not among the encoding trials.\n- kind: metadata_error\n  statement: Four files use experiment ids outside Table 2 (session 55 uses 80 and 82, 77 uses 81 and\n    82, 100 and 105 use 82 and 83). Nine files hold 14 event codes not in Table 1 (0, 4, 22, 23, 98,\n    99), 28 trials in 7 files break the order onset, offset, question, response, end, and eight files\n    do not hold the start marker 55 twice.\n- kind: metadata_error\n  statement: In 38 files (sessions 93 to 136 and all TWH sessions) the trial and event times are Unix\n    timestamps, not seconds from the start of the experiment as the paper states, and they give the\n    exact day of each recording, the detail the paper says session_start_time was set to hide.\n    Session 48's session_start_time is on the 13th of the month, and session 68 is dated 2000-01-01,\n    six years before the earliest other session.\n- kind: metadata_error\n  statement: The trials' stop_time equals delay2_time, the end of the trial, in every row; the paper\n    describes it as the stimulus offset. The offset is in stim_off_time, 1 s or 2 s after onset.\n- kind: other\n  about: data\n  statement: Identical spike trains are deposited in two files for sessions 38 and 39 (11 units), 43\n    and 44 (all 23) and 54 and 55 (all 32). The trials of each pair fall in different parts of one\n    timeline, so these are the same neurons recorded across two sessions of one recording. Nothing in\n    the files says so, and the unit count of 1864 counts them twice (1798 once).\n- kind: format_error\n  statement: Two units of session 58 (units 35 and 37) store every spike time twice, and 13 units in\n    sessions 21, 58, 68, 70, 73, 77 and 128 have spike times out of order.\n- kind: data_missing\n  statement: Session 144, which holds the example neuron of the paper's Figure 3 (144-140-3-RH), is in\n    neither the dandiset nor the paper's OSF deposit, and session 98 of the earlier release (Faraut et\n    al. 2018, H48, variant 2) is not in the dandiset or in Online-only Table 1.\n- kind: code_mismatch\n  statement: The paper's MS and dual counts (146 and 26) and its per-site percentages follow its code,\n    not its text. The Technical Validation describes a 1 s window and all 50 novel and 50 familiar\n    trials; single_neuron.py (ms_test and vs_test) uses 0.2 to 1.7 s, with a comment saying 1500 ms,\n    and only correctly answered trials for the MS test. With the code's choices this attempt finds 151\n    MS and 26 dual cells; with the text's, 112 and 12.\n- kind: paper_inconsistency\n  statement: The Methods give 89 sessions where Online-only Table 1 and the files hold 87. The 288 new\n    neurons the paper states equal the difference of the totals of the two releases (1864 - 1576), but\n    the 23 new sessions hold 325 units, as the 64 earlier sessions hold 1539 units here against 1576\n    in Faraut et al. 2018.\n- kind: code_mismatch\n  statement: The Python dynamic split of high and low confidence (helper.dynamic_split) counts only\n    response 4 as low-confidence \"old\" in its first mode, where the MATLAB NO_dynamic_lowHighSplit.m\n    counts 4 or 5.\n"
}
```

```
File created successfully at: attempts/chandravadia-2020-02.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python3 - <<'E'
p='attempts/chandravadia-2020-02.yaml'; s=open(p).read()
s=s.replace("""    new counts, since session 98 is not in the dandiset.
  depends_on_note: previous-release-link is partially reproduced.""","""    new counts, since session 98 is not in the dandiset.""")
open(p,'w').write(s)
import yaml; d=yaml.safe_load(s)
for l in s.splitlines():
    st=l.strip()
    if ': ' in st.split(':',1)[1] if ':' in st else False:
        k,v=st.split(':',1)
        if ': ' in v and not v.strip().startswith(('"',"'")): print('COLON',l)
print(len(d['outcomes']), len(d['findings']))
E
python tools/entry.py check entries/chandravadia-2020 2>&1 | tail; date -u
```

```
25 14
0 error(s)
Sun Nov 15 07:50:43 UTC 2026
```

**Agent calls Bash**

```bash
cd  grep -nE ": " attempts/chandravadia-2020-02.yaml | grep -vE "^[0-9]+:\s*(- )?[a-z_]+: " | head; grep -nE "^\s*(- )?[a-z_]+: .*: " attempts/chandravadia-2020-02.yaml | head
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  python tools/entry.py all entries/chandravadia-2020 2>&1 | tail -4; python tools/entry.py handover entries/chandravadia-2020 2>&1 | tail -5; ls executed/chandravadia-2020/handover
```

```
0 error(s)
pass  reproduce_chandravadia_2020.ipynb  (144 s, reused)
reused the executed copies of 2026-11-15 07:49 UTC: nothing the run reads has changed since (hash 930ddab2bfae). Nothing was executed and no environment was built; --fresh runs it again.
wrote executed/chandravadia-2020/handover
chandravadia-2020.yaml
recogmem.py
reproduce_chandravadia_2020.ipynb
```

**Agent**

I've finished steps 1 to 6 for `chandravadia-2020` on DANDI:000004 version 0.220126.1852. The entry is in `entries/chandravadia-2020/` and the record is `attempts/chandravadia-2020-02.yaml`. `lock`, `check` and `all` passed with 0 errors, the notebook ran clean in 144 s, and `handover` wrote `executed/chandravadia-2020/handover/`. Nothing was committed.

On blindness: `transcripts/chandravadia-2020/` was still in the checkout. I listed it and it was empty, so I saw nothing from the earlier attempts.

**1. Outcomes (25 claims)**

| Claim | Outcome |
|---|---|
| counts-neurons-subjects | reproduced (1864 units, 59 subjects) |
| counts-sessions | reproduced (the 87 sessions are exactly those of Online-only Table 1) |
| table1-demographics | partially (56 of 59 subjects match) |
| task-structure | partially (8 sessions have 50 or 97 encoding trials) |
| new-old-label-coding | not reproduced (labels reversed in the files) |
| ttl-codes | partially (78 of 87 files) |
| experiment-ids | partially (83 of 87 files) |
| session-dates | partially (86 of 87 on the 1st) |
| units-table | partially (many SNR/IsolationDist values not finite) |
| electrodes-table | not reproduced (impedance empty everywhere) |
| isi-criterion | partially (99.68% of units pass) |
| fig5a-mtl-locations | reproduced |
| fig5c-auc-all | reproduced (0.753 ± 0.094) |
| fig5c-auc-sites | reproduced |
| fig5b-roc-asymmetric | reproduced (z-ROC slope 0.78, p = 4e-9) |
| fig5d-confidence-accuracy | reproduced |
| vs-cells-proportion | reproduced (332, 17.8%) |
| ms-cells-proportion | not reproduced (112 cells; the code's choices give 151) |
| dual-cells-proportion | not reproduced (12 cells; the code's choices give exactly 26) |
| fig5f-site-proportions | partially (3 of 6 values within tolerance; the code's choices give 6 of 6) |
| twh-sessions | reproduced |
| previous-release-link | partially (64 of 65 sessions found) |
| previous-release-additions | partially (23 sessions and 17 subjects match; the new sessions hold 325 neurons, not 288) |
| fig4-example-vs-neuron | reproduced |
| fig3-example-vs-neuron | blocked, data_missing (session 144 is in neither the dandiset nor the paper's OSF deposit) |

**2. What I found**

About the data (11 findings in the record):
- `new_old_labels_recog` is 1 for old and 0 for new, the reverse of both the paper and the column's own description.
- Impedance is empty for every electrode; MNI coordinates are empty in 8 sessions.
- Quality metrics are often unusable (SNR not finite for 86 units, IsolationDist missing for 493), and the paper's `IsolDist` column is named `IsolationDist`.
- Three subjects' age or sex differ from both papers' patient tables.
- 8 sessions have fewer than 100 encoding trials.
- Four files use experiment ids outside Table 2, and nine hold event codes outside Table 1.
- **Privacy:** in 38 files the trial and event times are Unix timestamps. They reveal the exact day of each recording, which the paper says `session_start_time` was set to hide. Separately, session 48 is dated the 13th and session 68 is dated 2000.
- `stop_time` is the end of the trial, not the stimulus offset the paper describes.
- Identical spike trains appear in two files for sessions 38/39, 43/44 and 54/55: the same neurons recorded across two sessions of one recording.
- Two units in session 58 store every spike twice, and 13 units have spike times out of order.
- Session 144 (the Figure 3 neuron) and session 98 of the earlier release are missing.

About the paper:
- The paper's MS and dual counts follow its code (0.2 to 1.7 s window, correct trials only), not its text (1 s window, all trials). The code's choices reproduce 343 VS, 151 MS and 26 dual cells, and all six per-site percentages.
- The Methods say 89 sessions; the table and files hold 87.
- The stated 288 new neurons is the difference of the two releases' totals; the new sessions themselves hold 325.
- The Python and MATLAB versions of the dynamic confidence split differ.

I made no assumptions (no `assumed` outcomes), so there are no questions for the paper's authors. I asked no reader questions.

**3. Points where the protocol was unclear**
1. Shared-clock check: the suggested decoding test didn't fit this data. I compared onset responses at the true onsets against onsets shifted ±3 s. This holds in 68 of 87 sessions; the other 19, mostly with few units, could not be established and are named in the notebook.
2. Duplicated recordings: the protocol says to count each once, but the claims file's main reading counts per file. I followed the claims file and showed both counts.
3. No outcome fits "the criterion's method fails, but the paper's own code reproduces the number exactly". I recorded not_reproduced, kept the code's result as a variant, and added a `code_mismatch` finding.
4. Nulls for a selection that conditions on correct trials: shuffling the labels alone is not a null (it gave about 144 units). I permuted label, response and category together per session (about 105).
5. Whether the paper's own Online-only Table 1 counts as an outside input is not said. I read it at run time from Europe PMC, to avoid embedding numbers, and listed it under `inputs`.
6. There is no finding kind for exposed patient information; I used `metadata_error`.
7. The OSF deposit's NativeData.zip was listed while preparing, outside the notebook. The notes say so; the block rests on the NWBData.zip listing, which the notebook prints.

**4. Runtime and failures**
The work took about 30 minutes (07:21 to 07:52 UTC). The notebook runs in 144 s (71 s of that is loading), with about 0.3 GB peak memory in development. Nothing failed in the final run. Two earlier dev runs failed: one on a string-formatting error, which I fixed, and one gave a label-only null that was invalid, which I replaced.

## End of run

57 turns, 24 minutes, $5.56 at API prices, result: success.
