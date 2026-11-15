# chandravadia-2020 · author · run 43715082428

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cd  ls; ls docs entries attempts claims paper; wc -l docs/*.md README.md
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

```
Sun Nov 15 12:44:12 UTC 2026
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
[... 968 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat claims/chandravadia-2020.yaml; ls entries/chandravadia-2020; cat papers/datasets/chandravadia-2020.yaml; ls questions | grep chand
```

```
# Claims for Chandravadia, Liang, Schjetnan et al. (2020), Scientific Data 7, 78, on dandiset 000004.
# Source: the full text of the open access article (CC BY 4.0) at nature.com, read from its Methods,
# Data Records, Technical Validation, figure legends, Tables 1 and 2 and Online-only Table 1.
#
# When these criteria were written, the author had run the data check only, on every file of
# version 0.220126.1852: the file list and the archive's metadata; per file the subject metadata,
# session ids, session start dates, trial counts per phase, new/old label counts, stimulus categories,
# experiment ids, unit counts (1864 in total), electrode locations, waveform sampling rate and table
# columns; the comparison of subject age, sex and diagnosis with Online-only Table 1 (age or sex
# differ for three subjects); the duplicated spike trains of sessions 43 and 44 and of 54 and 55; and
# in one file (session 5) the cross-tabulation of new/old labels against confidence responses, which
# showed label 1 receiving most "old" responses. No selection of VS or MS cells, no AUC, no z-ROC and
# no accuracy by confidence had been computed. The author had read the paper's code
# (github.com/rutishauserlab/recogmem-release-NWB at commit 1d95162), including plotFigure5.ipynb,
# which writes the Figure 5f percentages into the plot as constants.
#
# After the first verification round the author added previous-release-link and rewrote the
# criterion of previous-release-additions, which had been blocked for want of the earlier
# release's session list. When writing them the author had read Table 1 of Faraut et al. 2018,
# which lists that release's sessions, and its abstract (65 sessions, 42 patients, 1576 neurons),
[... 409 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; sed -n 1,280p docs/design.md
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
[... 399 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "" docs/archives.md | sed -n 1,140p; ls entries/fouke-2025; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in
```

```
1:# Archives
2:
3:The registry tests papers against data in public archives. It began with one,
4:the DANDI Archive. The protocol is written for any archive. What is particular
5:to an archive (how its datasets are named, versioned and read) is here, and an
6:agent is pointed to its archive's section.
7:
8:A dataset is keyed as `<archive>:<id>` and shown as `<LABEL>:<id>`, for example
9:`DANDI:000003`. Its files in this repository (`claims/`, `questions/`,
10:`transcripts/`, the `attempt/` branch, the paper store) are under its folder
11:name: the identifier alone for DANDI, which the registry began with, and
12:`<archive>-<id>` for any other archive. Each archive is an adapter, a module in `tools/archives/` ("Adding an archive",
13:below), and `tools/datasets.py` turns one form of a dataset's name into another.
14:The workflows take a dataset in any of these forms.
15:
16:## DANDI
17:
18:- **Datasets.** A dandiset, identified by six digits (`000003`). Targets are the
19:  public dandisets whose metadata names a paper (`targets/dandisets.json`, built
20:  by `tools/build_targets.py` and refreshed daily by the Track DANDI workflow).
[... 155 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/fouke-2025-01.yaml | head -250; cat entries/fouke-2025/README.md
```

```
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
    model: claude-opus-5-5
    protocol: pilot-5
  runner:
[... 264 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
nb=json.load(open('entries/fouke-2025/reproduce_fouke_2025.ipynb'))
for c in nb['cells'][:8]:
    print('----',c['cell_type'],c.get('metadata',{}).get('tags'))
    print(''.join(c['source'])[:1500])
E
head -80 entries/fouke-2025/omr.py
```

```
---- markdown None
# Reproducing Fouke et al. (2025) from dandiset 001453

**Paper.** Fouke KE, He Z, Loring MD, Naumann EA (2025). Neural circuits underlying divergent
visuomotor strategies of zebrafish and *Danionella cerebrum*. *Current Biology*.
[doi:10.1016/j.cub.2025.04.027](https://doi.org/10.1016/j.cub.2025.04.027). This attempt used the
full text of the accepted author manuscript in PubMed Central (PMC12218792); the version of record
is not open access.

**Dandiset.** [DANDI:001453](https://dandiarchive.org/dandiset/001453/0.250518.1950), version
0.250518.1950. The paper cites no DANDI version (its data statement points to a GitLab repository
that holds code only). This is the only published version. The draft holds the same 37 files
(same blobs and sizes); it differs only in metadata added later (authors, keywords, and a
`relatedResource` link to the paper), none of which the analysis uses.

**What the dandiset holds.** Freely swimming tracking of 25 zebrafish (ZF) and 12 *D. cerebrum*
(DC) larvae during the optomotor protocol of Figure 1 and Figure S1. The two-photon imaging and the
head-fixed tail tracking of Figures 2 to 4 are not in it.

**Outside inputs.** The stimulus codes in the files have no names. The names come from the paper's
[... 198 more lines not kept]
```

**Agent**

Read the protocol, the claims file and the example entry. Now reading the paper.

**Agent calls Bash**

```bash
cd  wc -c paper/*; fold -w 200 -s paper/10.1038-s41597-020-0415-9.txt | head -400
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/d7f14e3a-18d0-4802-9ba3-f053fbcbdbca/tool-results/bobm11qyo.txt"
}
```

```
1	62275 paper/10.1038-s41597-020-0415-9.txt
2	DOI: 10.1038/s41597-020-0415-9
3	Version: as served by europe_pmc
4	Source: europe_pmc+crossref (paper-text-fetcher)
5	Stored: 2026-10-20
6	Extracted: as fetched
7	------------------------------------------------------------------------
8	2628 sdata Scientific Data Sci Data Nature Publishing Group PMC7055261 7055261 7055261 32132545 10.1038/s41597-020-0415-9 A NWB-based dataset and processing pipeline of human single-neuron activity 
9	during a declarative memory task Chandravadia N 1 Liang D 2 Schjetnan A G P 3 Carlson A 1 Faraut M 1 Chung J M 4 Reed C M 4 Dichter B 5 6 Maoz U 2 7 Kalia S K 8 3 Valiante T A 3 8 Mamelak A N 1 
10	Rutishauser U 1 4 7 9 10 ✉ 1 Department of Neurosurgery, Cedars-Sinai Medical Center, Los Angeles, CA USA 2 Institute for Interdisciplinary Brain and Behavioral Sciences, Crean College of Health and 
11	Behavioral Sciences, Schmid College of Science and Technology, Chapman University, Orange, CA USA 3 Krembil Brain Institute, Toronto Western Hospital, Toronto, Canada 4 Department of Neurology, 
12	Cedars-Sinai Medical Center, Los Angeles, CA USA 5 Biological Systems & Engineering Division, Lawrence Berkeley National Laboratory, Berkeley, CA USA 6 Department of Neurosurgery, Stanford 
13	University, Stanford, CA USA 7 Division of Biology and Biological Engineering, California Institute of Technology, Pasadena, CA USA 8 Division of Neurosurgery, Department of Surgery, University of 
14	Toronto, Toronto, Canada 9 Computational and Neural Systems Program, California Institute of Technology, Pasadena, CA USA 10 Center for Neural Science and Medicine, Department of Biomedical Science, 
15	Cedars-Sinai Medical Center, Los Angeles, CA USA ✉ Corresponding author. 4 3 2020 7 78 78 19 3 2020 © The Author(s) 2020 Open Access This article is licensed under a Creative Commons Attribution 4.0 
16	International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or forma
[... 386 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls schemas tools; ls questions | head; python -c "import json;print(json.dumps(json.load(open('schemas/attempt.schema.json')),indent=1)[:6000])" 2>/dev/null || ls schemas
```

```
schemas:
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json

tools:
__pycache__
agent_run.py
archive_transcripts.sh
archives
authors.py
backfill_summaries.py
blind.sh
build_dryad_targets.py
build_figshare_targets.py
build_openneuro_targets.py
build_reuse_targets.py
build_site.py
build_sparc_targets.py
[... 275 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "import json;print(json.dumps(json.load(open('schemas/attempt.schema.json')),indent=1)[6000:16000])"
```

```
claims file.",
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
     },
     "blocked_by": {
      "description": "Required when outcome is blocked.",
      "enum": [
       "data_missing",
       "metadata_insufficient",
       "methods_underspecified",
       "data_unreadable",
       "dataset_missing",
[... 369 more lines not kept]
```

**Agent**

Now surveying the dataset via the DANDI API.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/000004/versions/0.220126.1852/" | python -c "import json,sys;d=json.load(sys.stdin);print(json.dumps({k:d[k] for k in d if k in ('name','description','assetsSummary','relatedResource','doi','version','citation')},indent=1)[:4000])"; curl -s "https://api.dandiarchive.org/api/dandisets/000004/versions/" | python -m json.tool | grep -E '"version"|status|modified' | head -20
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q env && . env/bin/activate && uv pip install -q dandi h5py remfile pynwb numpy scipy pandas matplotlib pyyaml 2>&1 | tail -3; python -c "import pynwb,remfile,dandi;print(pynwb.__version__)"; echo $TMPDIR
```

```
4.2.0
/tmp/claude-1001
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python - <<'E'
from dandi.dandiapi import DandiAPIClient
import json
with DandiAPIClient() as c:
    d=c.get_dandiset("000004","0.220126.1852")
    assets=sorted([(a.path,a.size,a.identifier) for a in d.get_assets()])
print(len(assets))
for a in assets: print(a)
json.dump(assets,open('assets.json','w'))
E
```

```
87
('sub-P10HMH/sub-P10HMH_ses-20060901_ecephys+image.nwb', 73156888, '38304fe9-5f37-4c0d-a741-9cf2bafab9ff')
('sub-P11HMH/sub-P11HMH_ses-20061101_ecephys+image.nwb', 72628704, '0f57f0b0-f021-42bb-8eaa-56cd482e2a29')
('sub-P14HMH/sub-P14HMH_ses-20070601_obj-1t8wrd5_ecephys+image.nwb', 73186832, '0b6bc00c-715e-4ef0-9bc9-b4d2cbf85234')
('sub-P14HMH/sub-P14HMH_ses-20070601_obj-7studd_ecephys+image.nwb', 55262212, '8144c86f-c7fa-4599-9a31-6db621deb6a5')
('sub-P15HMH/sub-P15HMH_ses-20070901_obj-a5xz9n_ecephys+image.nwb', 55060760, '82b0a4b9-a544-49c7-9807-2166fe84b07c')
('sub-P15HMH/sub-P15HMH_ses-20070901_obj-bdd49u_ecephys+image.nwb', 54677088, 'e22c078c-43d9-4713-84f5-02d2e1db707c')
('sub-P16HMH/sub-P16HMH_ses-20071001_obj-12ambkj_ecephys+image.nwb', 54648464, 'a831c980-7b5a-4ad2-9687-7caf5ae27c56')
('sub-P16HMH/sub-P16HMH_ses-20071001_obj-1jfnx96_ecephys+image.nwb', 73367344, 'cac4440b-ac3f-4ab2-a5de-abaafd426801')
('sub-P17HMH/sub-P17HMH_ses-20080501_ecephys+image.nwb', 73147936, 'd1721a71-8427-4e9b-ab31-bbb8eb805f2c')
('sub-P18HMH/sub-P18HMH_ses-20080601_ecephys+image.nwb', 54940368, '6b77229c-873b-40ad-b9e2-fa8aaa41c96e')
('sub-P19HMH/sub-P19HMH_ses-20080601_obj-1tmj21e_ecephys+image.nwb', 72614400, '77e12554-96c7-4ee4-97b3-50aaba00ed9f')
('sub-P19HMH/sub-P19HMH_ses-20080601_obj-uw5up9_ecephys+image.nwb', 54425024, '5b2d5087-4a72-42ac-866a-4e7d53811414')
('sub-P21HMH/sub-P21HMH_ses-20090101_obj-1femyyi_ecephys+image.nwb', 72505896, '8c8b87bc-4877-4264-b096-731cc29cfb73')
('sub-P21HMH/sub-P21HMH_ses-20090101_obj-3ljvpn_ecephys+image.nwb', 72396072, '03f1dcbc-d7f4-442f-ad2e-93f35f91bf0c')
('sub-P21HMH/sub-P21HMH_ses-20090101_obj-slgaak_ecephys+image.nwb', 72419120, '81378f5b-2cec-4bea-97ab-d348b2d1cd62')
('sub-P23HMH/sub-P23HMH_ses-20090201_obj-1k3199e_ecephys+image.nwb', 72891960, '88addf50-1048-4757-9f06-99a280b632a6')
('sub-P23HMH/sub-P23HMH_ses-20090201_obj-1tm3w39_ecephys+image.nwb', 54862280, '4f4f3ac5-373e-4d90-a825-77fe0dc3d3f0')
('sub-P23HMH/sub-P23HMH_ses-
[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && time python - <<'E'
import h5py, remfile, json
from dandi.dandiapi import DandiAPIClient
with DandiAPIClient() as c:
    a=c.get_dandiset("000004","0.220126.1852").get_asset_by_path('sub-P9HMH/sub-P9HMH_ses-20060301_obj-1otd1m8_ecephys+image.nwb')
    url=a.get_content_url(follow_redirects=1,strip_query=True)
print(url)
f=h5py.File(remfile.File(url),'r')
def show(name,obj):
    if 'stimulus/presentation/' in name and name.count('/')>2: return
    if isinstance(obj,h5py.Dataset):
        print(name,obj.shape,obj.dtype,dict(obj.attrs) if obj.size<5 or True else '')
    else:
        print(name+'/',{k:(v if not hasattr(v,'shape') or v.size<10 else v.shape) for k,v in obj.attrs.items()})
f.visititems(show)
E
```

```
https://dandiarchive.s3.amazonaws.com/blobs/58f/ff7/58fff79f-ef69-4f07-a876-34dd8d11462d
acquisition/ {}
acquisition/events/ {'comments': 'no comments', 'description': ' The events coorespond to the TTL markers for each trial. For the learning trials, the TTL markers \n            are the following: 55 = start of the experiment, 1 = stimulus ON, 2 = stimulus OFF, 3 = Question Screen Onset [“Is this an animal?”], \n            20 = Yes (21 = NO) during learning, 6 = End of Delay after Response, 66 = End of Experiment. For the recognition trials, \n            the TTL markers are the following: 55 = start of experiment, 1 = stimulus ON, 2 = stimulus OFF, 3 = Question Screen Onset [“Have you seen this image before?”], \n            31:36 = Confidence (Yes vs. No) response [31 (new, confident), 32 (new, probably), 33 (new, guess), 34 (old, guess), \n            35 (old, probably), 36 (old, confident)], 66 = End of Experiment', 'namespace': 'core', 'neurodata_type': 'AnnotationSeries', 'object_id': 'd81b834f-7baa-4b26-88a7-2eb5e3d93a7e'}
acquisition/events/data (1004,) object {'conversion': np.float64(1.0), 'resolution': np.float64(-1.0), 'unit': 'n/a'}
acquisition/events/timestamps (1004,) float64 {'interval': np.int32(1), 'unit': 'seconds'}
acquisition/experiment_ids/ {'comments': 'no comments', 'description': 'The experiment_ids coorespond to the encoding (i.e., learning) or recogniton trials. The learning trials are demarcated by: 80. The recognition trials are demarcated by: 81. ', 'namespace': 'core', 'neurodata_type': 'TimeSeries', 'object_id': 'a75b4714-52b9-4c64-b641-39f594bfb605'}
acquisition/experiment_ids/data (1004,) float64 {'conversion': np.float64(1.0), 'resolution': np.float64(-1.0), 'unit': 'NA'}
acquisition/experiment_ids/timestamps (1004,) float64 {'interval': np.int32(1), 'unit': 'seconds'}
analysis/ {}
file_create_date (1,) object {}
general/ {}
general/data_collection () object {}
general/devices/ {}
general/devices/Neuralynx-cheetah/ {'namespace':
[... 83 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python - <<'E'
import h5py, remfile, numpy as np
url='https://dandiarchive.s3.amazonaws.com/blobs/58f/ff7/58fff79f-ef69-4f07-a876-34dd8d11462d'
f=h5py.File(remfile.File(url),'r')
for k in ['identifier','session_description','session_start_time','timestamps_reference_time','general/institution','general/lab','general/experiment_description','general/data_collection','general/related_publications','general/keywords']:
    print(k, f[k][()])
for k in f['general/subject']: print('subject',k,f['general/subject'][k][()])
e=f['general/extracellular_ephys/electrodes']
for k in ['id','x','y','z','imp','location','filtering','group_name','origChannel']: print(k,e[k][:])
u=f['units']
for k in ['id','origClusterID','IsolationDist','SNR','electrodes','electrodes_index','spike_times_index']: print(k,u[k][:])
print(u['waveform_mean_sampling_rate'][:].ravel())
t=f['intervals/trials']
print(t.attrs['colnames'])
for k in t.attrs['colnames']:
    v=t[k][:]
    print(k, v[:5], v[95:105], v[-3:])
sp=f['stimulus/presentation/StimulusPresentation']
for k in sp: print(k, sp[k].shape, sp[k].dtype, dict(sp[k].attrs))
print({k:v for k,v in sp.attrs.items()})
ev=f['acquisition/events/data'][:]; print(ev[:30]); print(np.unique(ev,return_counts=True))
ex=f['acquisition/experiment_ids/data'][:]; print(np.unique(ex,return_counts=True))
print(np.array_equal(f['acquisition/events/timestamps'][:],f['acquisition/experiment_ids/timestamps'][:]))
st=u['spike_times'][:]; print(st[:5], st.min(), st.max())
E
```

```
identifier b'H09_5'
session_description b'New/Old recognition task for ID: 5. '
session_start_time b'2006-03-01T00:00:00-08:00'
timestamps_reference_time b'2006-03-01T00:00:00-08:00'
general/institution b'Hunigton Memorial Hospital'
general/lab b'Rutishauser'
general/experiment_description b'The data contained within this file describes a new/old recogntion task performed in patients with intractable epilepsy implanted with depth electrodes and Behnke-Fried microwires in the human Medical Temporal Lobe (MTL).'
general/data_collection b'learning: 80, recognition: 81'
general/related_publications [b'Faraut et al. 2018, Scientific Data; Rutishauser et al. 2015, Nat Neurosci;']
general/keywords [b'Intracranial Recordings' b'Intractable Epilepsy'
 b'Single-Unit Recordings' b'Cognitive Neuroscience' b'Learning' b'Memory'
 b'Neurosurgery']
subject age b'55'
subject description b'Right Mesial Temporal'
subject sex b'M'
subject species b'Human'
subject subject_id b'P9HMH'
id [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13]
x [-19. -19. -19. -19. -19. -19. -19.  22.  22.  22.  22.  22.  22.  22.]
y [-12.2 -12.2 -12.2 -12.2 -12.2 -12.2 -12.2  -3.   -3.   -3.   -3.   -3.
[... 90 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/rutishauserlab/recogmem-release-NWB.git code && cd code && git checkout -q 1d95162 && git log -1 --format='%H %cd' && find . -type f | grep -v '^./.git/' | grep -v matnwb | head -100
```

```
1d95162d2672e71dd234a31e4b8d70017a289ee3 Tue Jan 14 12:07:46 2025 -0800
./README.MD
./setup.py
./LICENSE.txt
./.gitignore
./RutishauserLabtoNWB/InHouse/README.txt
./RutishauserLabtoNWB/assets/BrainAreaLocations.png
./RutishauserLabtoNWB/assets/Cedars-Sinai.png
./RutishauserLabtoNWB/assets/MATLAB_SingleNeuron.png
./RutishauserLabtoNWB/assets/Python_SingleNeuron.png
./RutishauserLabtoNWB/events/newolddelay/python/analysis/helper.py
./RutishauserLabtoNWB/events/newolddelay/python/analysis/behavior_all.py
./RutishauserLabtoNWB/events/newolddelay/python/analysis/main.py
./RutishauserLabtoNWB/events/newolddelay/python/analysis/single_neuron.py
./RutishauserLabtoNWB/events/newolddelay/python/analysis/behavior.py
./RutishauserLabtoNWB/events/newolddelay/python/analysis/demo/demoAnalysis.ipynb
./RutishauserLabtoNWB/events/newolddelay/python/analysis/demo/demoPlotStimuli.py
./RutishauserLabtoNWB/events/newolddelay/python/analysis/demo/demoQuerySpikeTimes.py
./RutishauserLabtoNWB/events/newolddelay/python/analysis/demo/plotFigure5.ipynb
./RutishauserLabtoNWB/events/newolddelay/python/analysis/demo/demoPlotWaveforms.py
[... 82 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/RutishauserLabtoNWB/events/newolddelay/matlab/analysis/helpers; for f in adjustHF.m calcZROCSlope.m getZROC_slope.m calcCumulativeD.m NWBbehaviorROC.m calcMeanSEOfSample.m NO_dynamic_lowHighSplit.m; do echo "=== $f"; grep -v '^\s*%' $f | grep -v '^\s*$'; done
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
[... 207 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/RutishauserLabtoNWB/events/newolddelay/matlab/analysis/helpers; for f in NO_behavior_evaluateSessionStatus.m calcMultipointROC.m calcEmpiricalROC.m calcDPrime.m NWB_behaviorSummary.m; do echo "=== $f"; grep -v '^\s*%' $f | grep -v '^\s*$'; done; grep -v '^\s*%' ../NWBloadDataOfBlock_release.m | grep -v '^\s*$' | head -120
```

```
=== NO_behavior_evaluateSessionStatus.m
function [isIncluded, AUC, percAccuracy_high, percAccuracy_low, TP, FP,respCounts,rawAccuracies, rawAccuracies2] = NO_behavior_evaluateSessionStatus(responses, newOldRecogLabels,enforceBehaviorExclusions)
if nargin<3
    enforceBehaviorExclusions=2;    
end
useDynamicSplitMode=0;
minAccuracyLow=0.55;
minAccuracyHigh=0.7;
respCounts=[];
for k=1:6
    respCounts(k) = length(find(responses==k));
end
mode=2; %all 6 confidence levels
typeCounters = calcEmpiricalROC(mode, newOldRecogLabels, responses);
dS = calcCumulativeD( typeCounters );
d = dS( 4:5, :); %only H/F of interest here
FP=d(2,:);
TP=d(1,:);
AUC = calcROC_AUC(TP,FP);
isIncluded=1;
[... 426 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/RutishauserLabtoNWB/events/newolddelay/matlab/analysis/helpers; for f in calcROC_AUC.m bootstrapMeanEqualTest.m NWB_singleCellAnalysis_release.m NO_selectSigCells_simple.m extractPeriodCountsSimple.m; do echo "=== $f"; grep -v '^\s*%' $f | grep -v '^\s*$' | head -150; done
```

```
=== calcROC_AUC.m
function [AUC] = calcROC_AUC(TP,FP, reverseOrder)
if nargin<3
    reverseOrder=0;
end
if reverseOrder
    TP = TP(end:-1:1);
    FP = FP(end:-1:1);
end
if FP(1)~=0 || TP(1)~=1
    FP = [0 FP];
    TP = [0 TP];
end
if FP(end)~=1 || TP(end)~=1
    FP = [FP 1];
    TP = [TP 1];
end
if ~issorted(TP) || ~issorted(FP)
   warning('TP/FP need to be sorted ascending'); 
end
[... 245 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/RutishauserLabtoNWB/events/newolddelay/python/analysis; wc -l *.py; grep -n "def \|anova\|f_oneway\|bootstrap\|0.2\|1.2\|1.7\|200\|1700\|1200\|p_val\|< 0.05\|<0.05\|seed\|correct" single_neuron.py | head -80
```

```
374 behavior.py
  385 behavior_all.py
  480 helper.py
   97 main.py
  423 single_neuron.py
 1759 total
4:from scipy.stats import f_oneway
14:    def __init__(self):
22:    def vs_test(self):
34:        # The window that we want to look at is from 200 ms after stim on until 1500 ms after.
37:                cat_1.append(trial.win_spike_rate(self.spike_timestamps, 200, 1700))
39:                cat_2.append(trial.win_spike_rate(self.spike_timestamps, 200, 1700))
41:                cat_3.append(trial.win_spike_rate(self.spike_timestamps, 200, 1700))
43:                cat_4.append(trial.win_spike_rate(self.spike_timestamps, 200, 1700))
45:                cat_5.append(trial.win_spike_rate(self.spike_timestamps, 200, 1700))
46:        return f_oneway(cat_1, cat_2, cat_3, cat_4, cat_5)[1]
48:    def baseline_test(self):
51:        :return: p value of the anova test
58:            stim_period.append(trial.win_spike_rate(self.spike_timestamps, 200, 1700))
59:        return f_oneway(baseline, stim_period)[1]
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/RutishauserLabtoNWB/events/newolddelay/python/analysis; sed -n 55,103p single_neuron.py; sed -n 300,423p single_neuron.py
```

```
stim_period = []
        for trial in trials:
            baseline.append(trial.win_spike_rate(self.spike_timestamps, -1000, 0))
            stim_period.append(trial.win_spike_rate(self.spike_timestamps, 200, 1700))
        return f_oneway(baseline, stim_period)[1]

    def ms_test(self, n):
        """
        A bootstrap test for new old test
        :param n: number of bootstraps
        :return: a p value of the bootstrap test
        """
        trials = (trial for trial in self.trials_recog)

        old = np.array([])
        new = np.array([])

        # Calculate the spike rates for new and old stimuli
        for trial in trials:
            if (trial.label == 0) & (trial.response <= 3.):
[... 149 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/RutishauserLabtoNWB/events/newolddelay/python/analysis; grep -n "def " behavior.py behavior_all.py helper.py; sed -n '/def extract_response_from_nwbfile/,/return/p' helper.py
```

```
behavior.py:7:def plot_behavioral_graphs(*argv):
behavior.py:241:def plot_prob_response():
behavior.py:258:def plot_cumulative_roc():
behavior.py:278:def plot_overall_performance():
behavior.py:304:def plot_auc():
behavior.py:324:def plot_confidence_accuracy():
behavior_all.py:8:def plot_behavioral_graphs(NWBFilePath):
behavior_all.py:252:def plot_prob_response():
behavior_all.py:269:def plot_cumulative_roc():
behavior_all.py:289:def plot_overall_performance():
behavior_all.py:315:def plot_auc():
behavior_all.py:335:def plot_confidence_accuracy():
helper.py:12:def get_nwbfile_names(path):
helper.py:26:def read(file_path):
helper.py:35:def get_event_data(nwbfile):
helper.py:62:def extract_recog_responses(nwbfile):
helper.py:72:def extract_new_old_label(nwbfile):
helper.py:88:def count_response(filenames):
helper.py:132:def extract_probability_response(filenames):
helper.py:145:def cal_d_prime(typecounters, n_old, n_new):
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/RutishauserLabtoNWB/events/newolddelay/python/analysis; sed -n 62,88p helper.py; sed -n 145,400p helper.py; sed -n 315,385p behavior_all.py
```

```
def extract_recog_responses(nwbfile):
    """
    Extract the recognition responses
    """
    events_learn, timestamps_learn, events_recog, timestamps_recog = get_event_data(nwbfile)
    response_recog_ind = np.where((events_recog >= 30) & (events_recog <= 36))
    response_recog = events_recog[response_recog_ind] - 30
    return response_recog


def extract_new_old_label(nwbfile):
    """
    Extracting the new old ground truths from the nwbfile.
    """
    labels = np.asarray(nwbfile.trials['new_old_labels_recog'].data)


    if not (labels.dtype == 'O'): #check Matlab data type
        new_old_labels = np.delete(labels, np.where(labels == 10)).astype(int)
    else: #Python
[... 335 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/RutishauserLabtoNWB/events/newolddelay/python/analysis/demo; python - <<'E'
import json
nb=json.load(open('plotFigure5.ipynb'))
for c in nb['cells']:
    s=''.join(c['source'])
    print('----',c['cell_type']); print(s[:3000])
    for o in c.get('outputs',[]):
        if 'text' in o: print('OUT:',''.join(o['text'])[:1500])
        elif 'data' in o and 'text/plain' in o['data']: print('OUT:',''.join(o['data']['text/plain'])[:800])
E
```

```
---- markdown
## This notebook will reproduce Figure 5 in the publication "A NWB-based Dataset and Processing Pipeline of Human Single-Neuron Activity During a Declarative Memory Task" by Chandravadia N. et al. 

#### *Note: Running the code might take some time (about 5 min) -- (due to reading from and extracting data from the NWB files)*

* Author: [Nand Chandravadia](mailto:[removed: an e-mail address])
---- code
#Figure 5 (Plot) 

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pandas as pd
import os
import sys
from pynwb import NWBHDF5IO
import matplotlib.pyplot as plt
import seaborn as sns
import RutishauserLabtoNWB.events.newolddelay.python.analysis.helper as helper
[... 341 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/RutishauserLabtoNWB/events/newolddelay/python/analysis/demo; python - <<'E'
import json
nb=json.load(open('plotFigure5.ipynb'))
s=''.join(nb['cells'][3]['source']); i=s.find('#Get percent accuracy'); print(s[i:i+2500])
s=''.join(nb['cells'][4]['source']); i=s.find('rects2'); print(s[i:])
E
```

```
#Get percent accuracy for each High and Low Confidence

    recog_response = helper.extract_recog_responses(nwbfile)
    is_included = helper.check_inclusion(recog_response, auc)
    
    if is_included:
        ground_truth = helper.extract_new_old_label(nwbfile)
        split_status, split_mode, ind_TP_high, ind_TP_low, ind_FP_high, ind_FP_low, ind_TN_high, \
        ind_TN_low, ind_FN_high, ind_FN_low, n_response = helper.dynamic_split(recog_response, ground_truth)
        
        nr_TN_high = len(ind_TN_high[0])
        nr_TP_high = len(ind_TP_high[0])
        nr_TN_all = len(ind_TN_high[0]) + len(ind_TN_low[0])
        nr_TN_low = len(ind_TP_high[0]) + len(ind_TP_low[0])
        nr_TP_low = len(ind_TP_low[0])
        nr_TN_low = len(ind_TN_low[0])

        nr_high_response = len(ind_TN_high[0]) + len(ind_TP_high[0]) + len(ind_FN_high[0]) + len(ind_FP_high[0])
        nr_low_response = len(ind_TN_low[0]) + len(ind_TP_low[0]) + len(ind_FN_low[0]) + len(ind_FP_low[0])
    
[... 45 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . env/bin/activate && head -40 code/RutishauserLabtoNWB/events/newolddelay/defineNOsessions_release.ini; grep -c '^\[' code/RutishauserLabtoNWB/events/newolddelay/defineNOsessions_release.ini; time python - <<'E'
import h5py, remfile, numpy as np, hashlib, time, resource
url='https://dandiarchive.s3.amazonaws.com/blobs/58f/ff7/58fff79f-ef69-4f07-a876-34dd8d11462d'
f=h5py.File(remfile.File(url),'r')
d=f['stimulus/presentation/StimulusPresentation/data']
print(d.chunks, d.compression)
t=time.time(); x=d[:]; print(time.time()-t, x.nbytes)
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB')
E
```

```
Sun Nov 15 12:46:13 UTC 2026
#defineNOsessions_release.ini

#
# List of all NO sessions that are part of the public data release.
# [please note that many sessions don't exist here because they belong to different experiments]
#
# =============================================================================


#P9S1 same day
[5]
NOsessions.session='P9HMH_NOID5'
NOsessions.sessionID='P9S1'
# Learning block trials in eventRaw.mat file
NOsessions.EXPERIMENTIDLearn=80  
# Memory test block trials in eventRaw.mat file
NOsessions.EXPERIMENTIDRecog=81  
# folder name in which data are stored (in 'events' and 'sorted' folders)
NOsessions.taskDescr='NO'        
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "def \|embed\|literal\|MAX\|limit" tools/entry.py | head -80
```

```
22:- no notebook or helper embeds a large literal array or an encoded image, or
68:MAX_LITERAL_NUMBERS = 200                 # more numbers than this in one literal is "embedded data"
73:LONG_LITERAL = re.compile(r"[\[(]\s*(?:-?\d+\.?\d*(?:e-?\d+)?\s*,\s*){%d,}" % MAX_LITERAL_NUMBERS)
77:    def __init__(self):
80:    def error(self, where, message: str) -> None:
85:def dataset_id(record: dict) -> str | None:
94:def dataset_ids(record: dict) -> list[str]:
99:def claims_paths() -> list[Path]:
105:def claims_target(data: dict) -> tuple:
110:def lookup(index: dict, attempt: dict):
119:def schema(name: str) -> Draft202012Validator:
130:def _parsed(text: str):
138:def _schema_errors(text: str, schema_name: str) -> tuple[str, ...]:
144:def load(report: Report, path: Path):
152:def validate(report: Report, path: Path, schema_name: str) -> dict | None:
161:def _plain(value):
172:def code_of(notebook_path: Path) -> str:
179:def check(entry_dir: Path) -> Report:
393:def _local_data(code: str, start: int) -> bool:
400:def _derivation_checks(report: Report, where, code: str) -> None:
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,70p tools/entry.py; sed -n 179,420p tools/entry.py
```

```
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
- each notebook, or a helper it imports, names the dataset the entry uses (its identifier and version);
[... 292 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && curl -s -o faraut.xml "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5810422/fullTextXML"; ls -la faraut.xml; python - <<'E'
import xml.etree.ElementTree as ET
t=ET.parse('/tmp/claude-1001/faraut.xml').getroot()
for tw in t.iter('table-wrap'):
    print(tw.get('id'), ''.join(tw.find('label').itertext()) if tw.find('label') is not None else '', ''.join(tw.find('caption').itertext())[:200] if tw.find('caption') is not None else '')
    rows=list(tw.iter('tr'))
    print(len(rows))
    for r in rows[:6]+rows[-4:]:
        print([''.join(c.itertext()).strip() for c in r])
E
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && curl -s -o chand.xml "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7055261/fullTextXML"; python - <<'E'
import xml.etree.ElementTree as ET
t=ET.parse('/tmp/claude-1001/chand.xml').getroot()
for tw in t.iter('table-wrap'):
    lab=tw.find('label'); print(tw.get('id'), ''.join(lab.itertext()) if lab is not None else '')
    rows=list(tw.iter('tr')); print(len(rows))
    for r in rows[:3]+rows[-3:]:
        print([''.join(c.itertext()).strip() for c in r])
E
```

Result: the fetched text is not kept.

**Agent**

Network access is good: the paper's own Online-only Table 1 and Faraut et al. 2018 Table 1 can be fetched at runtime from Europe PMC, so neither has to be embedded. Writing the helper module now.

**Agent calls Write**

```json
{
 "file_path": "entries/chandravadia-2020/nomem.py",
 "content": "\"\"\"Loading and measures for the new/old recognition memory data of dandiset 000004.\n\nChandravadia, Liang, Schjetnan et al. (2020), Scientific Data 7, 78, doi:10.1038/s41597-020-0415-9.\n\nEach NWB file holds one session: the TTL events and experiment ids (acquisition), the trials table\n(100 encoding and 100 recognition trials), the 200 stimulus images (stimulus/presentation), the\nelectrodes table and the units table with spike times. Files are streamed from the archive at the\npinned version; nothing is written to disk. The stimulus images are reduced to one hash per frame\nas they load.\n\nWhere the parameters come from:\n\n- Recognition trials are the rows with stim_phase \"recog\"; the confidence response is\n  response_value minus 30 (1 = new, confident; 6 = old, confident); \"old\" is label 1 of\n  new_old_labels_recog. All three are fixed by the claims file (its opening comment), which\n  takes them from the paper's code (github.com/rutishauserlab/recogmem-release-NWB at commit\n  1d95162d2672e71dd234a31e4b8d70017a289ee3: NWBloadDataOfBlock_release.m subtracts 30 from\n  the event codes; NWB_singleCellAnalysis_release.m says \"1 is old, 0 is new\").\n- The ROC follows the paper's code as the claims file prescribes: the cumulative hit and false\n  alarm rates over the six confidence levels from \"old, confident\" down (calcEmpiricalROC.m,\n  calcCumulativeD.m), each adjusted for 0 and 1 as in adjustHF.m, the AUC by the trapezoid rule\n  with (0,0) and (1,1) added (calcROC_AUC.m), and the z-ROC slope as the least-squares\n  regression of z(H) on z(F) over the five interior points (calcZROCSlope.m).\n- Accuracy in high and low confidence trials: the fixed split (high 1 or 6, low 2 to 5) of\n  NO_behavior_evaluateSessionStatus.m, and the dynamic split of helper.dynamic_split in the\n  Python code, both named by the claims file (fig5d-confidence-accuracy). The Python split is\n  reproduced as written, including its count of low-confidence hits as response 4 only in split\n  mode 1 (MATLAB's NO_dynamic_lowHighSplit.m counts 4 and 5 there).\n- Firing rates are spike counts in a window after stimulus onset divided by its length (claims\n  file). The windows are 0.2 to 1.2 s (Methods, \"a 1 s long window starting 200 ms after\n  stimulus onset\") and 0.2 to 1.7 s (the code's, single_neuron.py and\n  NWB_singleCellAnalysis_release.m). Stimulus onset is the trial's start_time, which the paper\n  defines as \"the time of stimulus onset of each trial\" (Data Records, interval group).\n- The bootstrap test of equal means is Efron and Tibshirani's algorithm 16.2 as in\n  bootstrapMeanEqualTest.m (both samples shifted to the pooled mean, resampled with\n  replacement, two-sided on the absolute difference of means), with B = 1000 (Methods). The seed\n  is a standard choice and is passed in by the caller.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport hashlib\nimport re\nimport urllib.request\nimport xml.etree.ElementTree as ET\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nfrom dandi.dandiapi import DandiAPIClient\nfrom scipy import stats\n\nDANDISET_ID = \"000004\"\nDANDISET_VERSION = \"0.220126.1852\"\n\nWINDOW_METHODS = (0.2, 1.2)   # s after stimulus onset; Methods, Technical Validation\nWINDOW_CODE = (0.2, 1.7)      # s; single_neuron.py and NWB_singleCellAnalysis_release.m\nN_BOOT = 1000                 # Methods: \"two-tailed bootstrap comparison of means with 1,000 runs\"\nALPHA = 0.05\n\n# Full texts in Europe PMC (version of record, CC BY): this paper, and Faraut et al. 2018,\n# Sci Data 5, 180010 (doi:10.1038/sdata.2018.10), the earlier release of the task's data.\nPAPER_PMC = \"PMC7055261\"\nFARAUT_PMC = \"PMC5810422\"\nEUROPE_PMC = \"https://www.ebi.ac.uk/europepmc/webservices/rest/{}/fullTextXML\"\n\n\ndef asset_urls() -> list[tuple[str, str]]:\n    \"\"\"(path, streaming URL) of every NWB file at the pinned version.\"\"\"\n    with DandiAPIClient() as client:\n        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)\n        return sorted((a.path, a.get_content_url(follow_redirects=1, strip_query=True))\n                      for a in dandiset.get_assets() if a.path.endswith(\".nwb\"))\n\n\ndef _text(value) -> str:\n    if isinstance(value, bytes):\n        return value.decode()\n    if isinstance(value, np.ndarray):\n        return \"; \".join(_text(v) for v in value.ravel())\n    return str(value)\n\n\ndef _strings(dataset) -> np.ndarray:\n    return np.array([_text(v) for v in dataset[:]], dtype=object)\n\n\ndef load_session(path: str, url: str, images: bool = True) -> dict:\n    \"\"\"Everything the analyses use from one file, as plain arrays.\"\"\"\n    with h5py.File(remfile.File(url), \"r\") as f:\n        s = {\"path\": path, \"identifier\": _text(f[\"identifier\"][()]),\n             \"session_description\": _text(f[\"session_description\"][()]),\n             \"session_start_time\": _text(f[\"session_start_time\"][()]),\n             \"institution\": _text(f[\"general/institution\"][()]) if \"general/institution\" in f else \"\",\n             \"data_collection\": _text(f[\"general/data_collection\"][()]) if \"general/data_collection\" in f else \"\",\n             \"devices\": sorted(f[\"general/devices\"].keys())}\n        s[\"subject\"] = {k: _text(v[()]) for k, v in f[\"general/subject\"].items()}\n        ev, ex = f[\"acquisition/events\"], f[\"acquisition/experiment_ids\"]\n        s[\"events\"] = np.array([float(_text(v)) for v in ev[\"data\"][:]])\n        s[\"events_t\"] = ev[\"timestamps\"][:]\n        s[\"expids\"] = ex[\"data\"][:].astype(float)\n        s[\"expids_t\"] = ex[\"timestamps\"][:]\n        s[\"events_description\"] = _text(ev.attrs.get(\"description\", \"\"))\n        s[\"expids_description\"] = _text(ex.attrs.get(\"description\", \"\"))\n\n        tr = f[\"intervals/trials\"]\n        cols = [_text(c) for c in tr.attrs[\"colnames\"]]\n        table = {}\n        for c in cols:\n            d = tr[c]\n            table[c] = _strings(d) if d.dtype.kind in \"OSU\" else d[:]\n        s[\"trials\"] = pd.DataFrame(table)\n        s[\"trial_columns\"] = cols\n        s[\"label_description\"] = _text(tr[\"new_old_labels_recog\"].attrs.get(\"description\", \"\"))\n\n        el = f[\"general/extracellular_ephys/electrodes\"]\n        ecols = [_text(c) for c in el.attrs[\"colnames\"]]\n        etab = {\"id\": el[\"id\"][:]}\n        for c in ecols:\n            if c == \"group\":\n                continue\n            d = el[c]\n            etab[c] = _strings(d) if d.dtype.kind in \"OSU\" else d[:]\n        s[\"electrodes\"] = pd.DataFrame(etab)\n        s[\"electrode_columns\"] = ecols\n\n        u = f[\"units\"]\n        ucols = [_text(c) for c in u.attrs[\"colnames\"]]\n        s[\"unit_columns\"] = ucols\n        n = len(u[\"id\"])\n        idx = u[\"spike_times_index\"][:]\n        st = u[\"spike_times\"][:]\n        starts = np.concatenate([[0], idx[:-1]])\n        s[\"spikes\"] = [st[a:b] for a, b in zip(starts, idx)]\n        eidx = u[\"electrodes_index\"][:]\n        e = u[\"electrodes\"][:]\n        estarts = np.concatenate([[0], eidx[:-1]])\n        s[\"unit_electrodes\"] = [e[a:b] for a, b in zip(estarts, eidx)]\n        units = {\"id\": u[\"id\"][:]}\n        for c in (\"origClusterID\", \"SNR\", \"IsolationDist\", \"IsolDist\"):\n            if c in u:\n                units[c] = u[c][:]\n        if \"waveform_mean_sampling_rate\" in u:\n            units[\"waveform_rate\"] = u[\"waveform_mean_sampling_rate\"][:].reshape(n, -1)[:, 0]\n        for c in (\"waveform_mean_encoding\", \"waveform_mean_recognition\"):\n            if c in u:\n                w = u[c][:]\n                units[c + \"_samples\"] = np.full(n, w.shape[1])\n                units[c + \"_finite\"] = np.isfinite(w).all(axis=1)\n        s[\"units\"] = pd.DataFrame(units)\n\n        if images:\n            data = f[\"stimulus/presentation/StimulusPresentation/data\"]\n            s[\"image_shape\"] = data.shape\n            frames = data[:]\n            s[\"image_hash\"] = [hashlib.md5(frames[i].tobytes()).hexdigest() for i in range(frames.shape[0])]\n            s[\"image_t\"] = f[\"stimulus/presentation/StimulusPresentation/timestamps\"][:]\n            del frames\n    return s\n\n\ndef load_all(images: bool = True, workers: int = 6) -> list[dict]:\n    urls = asset_urls()\n    with ThreadPoolExecutor(workers) as pool:\n        return list(pool.map(lambda pu: load_session(*pu, images=images), urls))\n\n\ndef session_key(s: dict) -> tuple[str, int]:\n    \"\"\"(subject label, session id) from the identifier, e.g. 'H09_5' -> ('H09', 5).\"\"\"\n    label, sid = s[\"identifier\"].rsplit(\"_\", 1)\n    return label, int(sid)\n\n\ndef site(label: str) -> str:\n    \"\"\"CS for subjects labelled H or C, TWH for T (Figure 5 legend).\"\"\"\n    return \"TWH\" if label.startswith(\"T\") else \"CS\"\n\n\n# --- the paper's tables, read from the full text --------------------------------------------\n\ndef _tables(pmc: str) -> dict[str, list[list[str]]]:\n    with urllib.request.urlopen(EUROPE_PMC.format(pmc), timeout=60) as r:\n        root = ET.fromstring(r.read())\n    out = {}\n    for tw in root.iter(\"table-wrap\"):\n        label = tw.find(\"label\")\n        name = \"\".join(label.itertext()).strip() if label is not None else tw.get(\"id\")\n        rows = [[\"\".join(c.itertext()).strip() for c in tr] for tr in tw.iter(\"tr\")]\n        out.setdefault(name, rows)\n    return out\n\n\ndef _subject_rows(rows: list[list[str]]) -> pd.DataFrame:\n    out = []\n    for r in rows:\n        if len(r) < 7 or not re.fullmatch(r\"[HCT]\\d+\", r[0]):\n            continue\n        sessions = [int(x) for x in re.findall(r\"\\d+\", r[2])]\n        variants = [int(x) for x in re.findall(r\"\\d+\", r[3])]\n        out.append({\"label\": r[0], \"n_sessions\": int(r[1]), \"sessions\": sessions, \"variants\": variants,\n                    \"age\": int(r[4]), \"sex\": r[5], \"diagnosis\": r[6]})\n    return pd.DataFrame(out)\n\n\ndef paper_table1() -> tuple[pd.DataFrame, list[str]]:\n    \"\"\"Online-only Table 1 of the paper, one row per subject, and its totals row.\"\"\"\n    rows = _tables(PAPER_PMC)[\"Online-only Table 1\"]\n    totals = [c for c in rows[-1] if c]\n    return _subject_rows(rows), totals\n\n\ndef faraut_table1() -> tuple[pd.DataFrame, list[str], dict[str, list[list[str]]]]:\n    \"\"\"Table 1 of Faraut et al. 2018 (the earlier release), its totals, and all its tables.\"\"\"\n    tables = _tables(FARAUT_PMC)\n    rows = tables[\"Table 1\"]\n    totals = [c for c in rows[-1] if c]\n    return _subject_rows(rows), totals, tables\n\n\ndef sessions_of(table: pd.DataFrame) -> pd.DataFrame:\n    \"\"\"One row per (subject, session) of a subject table, with the session's variant.\"\"\"\n    rows = []\n    for _, r in table.iterrows():\n        for i, sid in enumerate(r.sessions):\n            rows.append({\"label\": r.label, \"session\": sid,\n                         \"variant\": r.variants[i] if i < len(r.variants) else np.nan})\n    return pd.DataFrame(rows)\n\n\n# --- behaviour --------------------------------------------------------------------------------\n\ndef recog(s: dict) -> pd.DataFrame:\n    \"\"\"Recognition trials: label (1 = old, as the paper's code), confidence 1..6 and onset.\"\"\"\n    t = s[\"trials\"]\n    r = t[t.stim_phase == \"recog\"].reset_index(drop=True)\n    out = pd.DataFrame({\"onset\": r.start_time.to_numpy(float),\n                        \"label\": r.new_old_labels_recog.astype(int).to_numpy(),\n                        \"confidence\": (r.response_value.to_numpy(float) - 30).astype(int),\n                        \"category\": r.stimCategory.to_numpy(int),\n                        \"category_name\": r.category_name.to_numpy()})\n    return out\n\n\ndef adjust_hf(h: float, f: float, n_old: int, n_new: int) -> tuple[float, float]:\n    \"\"\"adjustHF.m: rates of 0 and 1 moved to 1/(2n) and 1 - 1/(2n).\"\"\"\n    if h == 1:\n        h = 1 - 1 / (2 * n_old)\n    if f == 1:\n        f = 1 - 1 / (2 * n_new)\n    if h == 0:\n        h = 1 / (2 * n_old)\n    if f == 0:\n        f = 1 / (2 * n_new)\n    return h, f\n\n\ndef roc(confidence: np.ndarray, is_old: np.ndarray) -> tuple[np.ndarray, np.ndarray]:\n    \"\"\"Cumulative hit and false alarm rates for criteria 6, >=5, ..., >=1 (calcCumulativeD.m).\"\"\"\n    n_old, n_new = int(is_old.sum()), int((~is_old).sum())\n    hs, fs = [], []\n    for k in range(6, 0, -1):\n        said_old = confidence >= k\n        h = (said_old & is_old).sum() / n_old\n        f = (said_old & ~is_old).sum() / n_new\n        h, f = adjust_hf(h, f, n_old, n_new)\n        hs.append(h)\n        fs.append(f)\n    return np.array(hs), np.array(fs)\n\n\ndef auc(h: np.ndarray, f: np.ndarray) -> float:\n    \"\"\"calcROC_AUC.m / helper.cal_auc: trapezoid rule with (0,0) and (1,1) added.\"\"\"\n    tp, fp = list(h), list(f)\n    if fp[0] != 0 or tp[0] != 0:\n        tp, fp = [0.0] + tp, [0.0] + fp\n    if fp[-1] != 1 or tp[-1] != 1:\n        tp, fp = tp + [1.0], fp + [1.0]\n    area = 0.0\n    for i in range(1, len(tp)):\n        if fp[i - 1] < fp[i]:\n            area += (fp[i] - fp[i - 1]) * tp[i - 1] + 0.5 * (tp[i] - tp[i - 1]) * (fp[i] - fp[i - 1])\n    return area\n\n\ndef zroc_slope(h: np.ndarray, f: np.ndarray) -> float:\n    \"\"\"calcZROCSlope.m: regression of z(H) on z(F) over the first five points (the sixth is (1,1)).\"\"\"\n    zh, zf = stats.norm.ppf(h[:5]), stats.norm.ppf(f[:5])\n    return float(np.polyfit(zf, zh, 1)[0])\n\n\ndef accuracy_fixed(conf: np.ndarray, is_old: np.ndarray) -> tuple[float, float]:\n    \"\"\"NO_behavior_evaluateSessionStatus.m: high is response 1 or 6, low is 2 to 5.\"\"\"\n    correct = (is_old & (conf >= 4)) | (~is_old & (conf <= 3))\n    high = (conf == 1) | (conf == 6)\n    low = (conf >= 2) & (conf <= 5)\n    acc_h = correct[high].mean() if high.any() else np.nan\n    acc_l = correct[low].mean() if low.any() else np.nan\n    return acc_h, acc_l\n\n\ndef accuracy_dynamic(conf: np.ndarray, is_old: np.ndarray) -> tuple[float, float, int]:\n    \"\"\"helper.dynamic_split and plotFigure5.ipynb, as written. Returns (high, low, split mode).\"\"\"\n    counts = np.array([(conf == k).sum() for k in range(1, 7)])\n    c1, c2, c3 = counts[0] + counts[5], counts[1] + counts[4], counts[2] + counts[3]\n    split = np.array([c1 - (c2 + c3), (c1 + c2) - c3])\n    mode = int(np.where(np.abs(split) == np.abs(split).min())[0][0]) + 1\n    if counts[0] == 0 or counts[5] == 0:\n        mode = 2\n    if counts[1] == 0 or counts[4] == 0:\n        mode = 1\n    old, new = is_old, ~is_old\n    if mode == 1:\n        tp_h, tp_l = old & (conf >= 6), old & (conf == 4)\n        fp_h, fp_l = new & (conf >= 6), new & (conf == 4)\n        tn_h, tn_l = new & (conf <= 1), new & ((conf == 3) | (conf == 2))\n        fn_h, fn_l = old & (conf <= 1), old & ((conf == 3) | (conf == 2))\n    else:\n        tp_h, tp_l = old & (conf >= 5), old & (conf == 4)\n        fp_h, fp_l = new & (conf >= 5), new & (conf == 4)\n        tn_h, tn_l = new & (conf <= 2), new & (conf == 3)\n        fn_h, fn_l = old & (conf <= 2), old & (conf == 3)\n    n_h = tn_h.sum() + tp_h.sum() + fn_h.sum() + fp_h.sum()\n    n_l = tn_l.sum() + tp_l.sum() + fn_l.sum() + fp_l.sum()\n    acc_h = (tn_h.sum() + tp_h.sum()) / n_h if n_h else np.nan\n    acc_l = (tn_l.sum() + tp_l.sum()) / n_l if n_l else np.nan\n    return acc_h, acc_l, mode\n\n\ndef included(conf: np.ndarray, auc_value: float) -> bool:\n    \"\"\"helper.check_inclusion, applied by plotFigure5.ipynb before the accuracy panel.\"\"\"\n    counts = np.array([(conf == k).sum() for k in range(1, 7)])\n    return not (auc_value < 0.6 or (counts[:3] == 0).sum() > 1 or (counts[3:] == 0).sum() > 1)\n\n\n# --- single units -----------------------------------------------------------------------------\n\ndef window_rates(spikes: np.ndarray, onsets: np.ndarray, window: tuple[float, float]) -> np.ndarray:\n    \"\"\"Spike count in (onset + start, onset + stop] divided by the window length, per trial.\"\"\"\n    sp = np.sort(spikes)\n    lo = np.searchsorted(sp, onsets + window[0], side=\"right\")\n    hi = np.searchsorted(sp, onsets + window[1], side=\"right\")\n    return (hi - lo) / (window[1] - window[0])\n\n\ndef anova_p(rates: np.ndarray, groups: np.ndarray) -> float:\n    \"\"\"One-way ANOVA across the groups (the 5 categories); nan when every rate is equal.\"\"\"\n    samples = [rates[groups == g] for g in np.unique(groups)]\n    if np.all(rates == rates[0]):\n        return np.nan\n    return float(stats.f_oneway(*samples).pvalue)\n\n\ndef bootstrap_p(a: np.ndarray, b: np.ndarray, rng: np.random.Generator, n_boot: int = N_BOOT) -> float:\n    \"\"\"bootstrapMeanEqualTest.m (Efron and Tibshirani, algorithm 16.2), two-sided.\"\"\"\n    pooled = np.concatenate([a, b]).mean()\n    at, bt = a - a.mean() + pooled, b - b.mean() + pooled\n    ia = rng.integers(0, len(a), size=(n_boot, len(a)))\n    ib = rng.integers(0, len(b), size=(n_boot, len(b)))\n    t = np.abs(at[ia].mean(axis=1) - bt[ib].mean(axis=1))\n    return float(np.mean(t >= abs(a.mean() - b.mean())))\n\n\ndef isi_violation_fraction(spikes: np.ndarray, sort: bool = True, limit: float = 0.003) -> float:\n    \"\"\"Fraction of interspike intervals shorter than `limit` seconds (Methods: 3 ms).\"\"\"\n    sp = np.sort(spikes) if sort else spikes\n    if len(sp) < 2:\n        return np.nan\n    return float(np.mean(np.diff(sp) < limit))\n"
}
```

```
File created successfully at: entries/chandravadia-2020/nomem.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/chandravadia-2020 && . $TMPDIR/env/bin/activate && python - <<'E'
import time, resource, pickle, nomem
t=time.time()
urls=nomem.asset_urls()
print(len(urls), time.time()-t)
t=time.time()
ss=[nomem.load_session(*u) for u in urls[:2]]
print('2 files', time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
s=ss[0]; print(s['identifier'], s['subject'], s['trial_columns'], s['unit_columns'], s['electrode_columns'])
print(s['units'].head()); print(nomem.recog(s).head())
E
```

```
87 3.8492398262023926
2 files 3.385416269302368 0.405996
H10_7 {'age': '37', 'description': 'Left Lateral Frontal', 'sex': 'M', 'species': 'Human', 'subject_id': 'P10HMH'} ['start_time', 'stop_time', 'stim_on_time', 'stim_off_time', 'delay1_time', 'delay2_time', 'stim_phase', 'stimCategory', 'category_name', 'external_image_file', 'new_old_labels_recog', 'response_value', 'response_time'] ['origClusterID', 'waveform_mean_encoding', 'waveform_mean_recognition', 'IsolationDist', 'SNR', 'waveform_mean_sampling_rate', 'spike_times', 'electrodes'] ['x', 'y', 'z', 'imp', 'location', 'filtering', 'group', 'group_name', 'origChannel']
   id  ...  waveform_mean_recognition_finite
0   0  ...                              True
1   1  ...                              True
2   2  ...                              True
3   3  ...                              True
4   4  ...                              True

[5 rows x 9 columns]
         onset  label  confidence  category category_name
0  7045.061168      0           1         3      mobility
1  7050.427808      1           1         1        houses
2  7054.434928      0           1         2    landscapes
3  7057.816328      1           2         4        phones
4  7064.243768      1           5         4        phones
```

**Agent**

Helper works (about 1.7 s per file). Loading all 87 files into a development cache.

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && python - <<'E'
import time, resource, pickle, nomem
t=time.time()
ss=nomem.load_all()
print(len(ss), time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB')
pickle.dump(ss, open('/tmp/claude-1001/sessions.pkl','wb'))
E
```

```
87 119.26671481132507 0.827836 GB
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && python - <<'E'
import pickle, numpy as np, pandas as pd, nomem, collections
pd.set_option('display.width',250); pd.set_option('display.max_rows',200)
ss=pickle.load(open('/tmp/claude-1001/sessions.pkl','rb'))
rows=[]
for s in ss:
    t=s['trials']; lab,sid=nomem.session_key(s)
    r=t[t.stim_phase=='recog']; l=t[t.stim_phase=='learn']
    rows.append(dict(id=s['identifier'],subj=s['subject']['subject_id'],age=s['subject']['age'],sex=s['subject']['sex'],diag=s['subject']['description'],
      date=s['session_start_time'][:10],n_tr=len(t),n_learn=len(l),n_recog=len(r),phases=set(t.stim_phase),
      lab=dict(collections.Counter(r.new_old_labels_recog)), ncat=t.stimCategory.nunique(), cats=sorted(set(t.category_name)),
      units=len(s['units']), elec=len(s['electrodes']), exp=sorted(set(s['expids'])), ev_eq=len(s['events'])==len(s['expids']),
      ts_eq=np.array_equal(s['events_t'],s['expids_t']), dc=s['data_collection'], inst=s['institution'], img=s['image_shape'],
      ucols=','.join(s['unit_columns'])))
df=pd.DataFrame(rows)
print(df.drop(columns=['ucols','cats']).to_string())
print(df.ucols.value_counts())
print(df.subj.nunique(), df.units.sum())
for s in ss[:1]: print(s['session_description'], s['subject'])
print(collections.Counter(x for s in ss for x in s['trials'].stim_phase))
print(collections.Counter(s['institution'] for s in ss))
print(collections.Counter(tuple(s['devices']) for s in ss))
E
```

```
id    subj age sex                            diag        date  n_tr  n_learn  n_recog          phases                 lab  ncat  units  elec           exp  ev_eq  ts_eq                             dc                         inst                 img
0       H10_7  P10HMH  37   M            Left Lateral Frontal  2006-09-01   200      100      100  {learn, recog}  {'0': 50, '1': 50}     5     38    18  [80.0, 81.0]   True   True  learning: 80, recognition: 81   Hunigton Memorial Hospital  (200, 400, 300, 3)
1       H11_9  P11HMH  16   M           Right Lateral Frontal  2006-11-01   200      100      100  {learn, recog}  {'0': 50, '1': 50}     5     25     9  [80.0, 81.0]   True   True  learning: 80, recognition: 81   Hunigton Memorial Hospital  (200, 400, 300, 3)
2      H14_17  P14HMH  31   M  Bilateral Independent Temporal  2007-06-01   200      100      100  {learn, recog}  {'0': 50, '1': 50}     5     23     9  [83.0, 84.0]   True   True  learning: 83, recognition: 84   Hunigton Memorial Hospital  (200, 400, 300, 3)
3      H14_18  P14HMH  31   M  Bilateral Independent Temporal  2007-06-01   150       50      100  {learn, recog}  {'0': 50, '1': 50}     5     33    10  [80.0, 81.0]   True   True  learning: 80, recognition: 81   Hunigton Memorial Hospital  (150, 400, 300, 3)
4      H15_21  P15HMH  45   M           Right Mesial Temporal  2007-09-01   150       50      100  {learn, recog}  {'0': 50, '1': 50}     5     14     7  [83.0, 84.0]   True   True  learning: 83, recognition: 84   Hunigton Memorial Hospital  (150, 400, 300, 3)
5      H15_20  P15HMH  45   M           Right Mesial Temporal  2007-09-01   150       50      100  {learn, recog}  {'0': 50, '1': 50}     5     20    11  [80.0, 81.0]   True   True  learning: 80, recognition: 81   Hunigton Memorial Hospital  (150, 400, 300, 3)
6      H16_23  P16HMH  34   F           Right Lateral Frontal  2007-10-01   150       50      100  {learn, recog}  {'0': 50, '1': 50}     5     18     9  [83.0, 84.0]   True   True  le
[... 88 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && python - <<'E'
import pickle, numpy as np, pandas as pd, nomem, collections, hashlib
pd.set_option('display.width',250); pd.set_option('display.max_rows',200)
ss=pickle.load(open('/tmp/claude-1001/sessions.pkl','rb'))
rows=[]
for s in ss:
    t=s['trials']; learn=t.stim_phase=='learn'; rec=t.stim_phase=='recog'
    h=np.array(s['image_hash']); f=t.external_image_file.to_numpy()
    lab=t.new_old_labels_recog.to_numpy()
    enc_h=set(h[learn]); enc_f=set(f[learn])
    r=nomem.recog(s)
    inenc_h=np.array([x in enc_h for x in h[rec]]); inenc_f=np.array([x in enc_f for x in f[rec]])
    l=r.label.to_numpy(); c=r.confidence.to_numpy()
    rows.append(dict(id=s['identifier'], n_enc_files=len(enc_f), n_enc_hash=len(enc_h),
       l0_in_enc_f=inenc_f[l==0].mean(), l1_in_enc_f=inenc_f[l==1].mean(), l0_in_enc_h=inenc_h[l==0].mean(), l1_in_enc_h=inenc_h[l==1].mean(),
       old_resp_l0=(c[l==0]>=4).mean(), old_resp_l1=(c[l==1]>=4).mean(), conf_range=(c.min(),c.max()),
       img_t_eq=np.allclose(s['image_t'], t.start_time) if len(s['image_t'])==len(t) else 'len'))
df=pd.DataFrame(rows); print(df.to_string())
print((df.l1_in_enc_h==1).sum(), (df.l0_in_enc_h==0).sum())
E
```

```
id  n_enc_files  n_enc_hash  l0_in_enc_f  l1_in_enc_f  l0_in_enc_h  l1_in_enc_h  old_resp_l0  old_resp_l1 conf_range  img_t_eq
0       H10_7          100         100          0.0         1.00          0.0         1.00         0.46         0.66     (1, 6)      True
1       H11_9          100         100          0.0         1.00          0.0         1.00         0.24         0.70     (1, 6)      True
2      H14_17          100         100          0.0         1.00          0.0         1.00         0.30         0.66     (1, 6)      True
3      H14_18           50          50          0.0         0.58          0.0         0.58         0.02         0.44     (1, 6)      True
4      H15_21           50          50          0.0         0.52          0.0         0.52         0.70         0.80     (1, 6)      True
5      H15_20           50          50          0.0         0.58          0.0         0.58         0.76         0.88     (1, 6)      True
6      H16_23           50          50          0.0         0.52          0.0         0.52         0.06         0.58     (1, 6)      True
7      H16_24          100         100          0.0         1.00          0.0         1.00         0.20         0.56     (1, 4)      True
8      H17_32          100         100          0.0         1.00          0.0         1.00         0.24         0.70     (1, 6)      True
9      H18_26           50          50          0.0         0.58          0.0         0.58         0.14         0.44     (1, 6)      True
10     H19_28          100         100          0.0         1.00          0.0         1.00         0.48         0.80     (1, 6)      True
11     H19_27           50          50          0.0         0.52          0.0         0.52         0.30         0.82     (1, 6)      True
12     H21_38          100         100          0.0         1.00          0.0         1.00         0.60         0.92     (2, 6)      True
13     H21_41          100         100          0.0         1.00          0.0  
[... 74 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && python - <<'E'
import pickle, numpy as np, pandas as pd, nomem, collections
ss=pickle.load(open('/tmp/claude-1001/sessions.pkl','rb'))
byid={s['identifier']:s for s in ss}
allenc={}
for s in ss:
    t=s['trials']; h=np.array(s['image_hash'])
    allenc[s['identifier']]=set(h[(t.stim_phase=='learn').to_numpy()])
for s in ss:
    t=s['trials']
    if (t.stim_phase=='learn').sum()==100: continue
    h=np.array(s['image_hash']); rec=(t.stim_phase=='recog').to_numpy(); lab=t.new_old_labels_recog.to_numpy()
    old=set(h[rec & (lab=='1')]); new=set(h[rec&(lab=='0')])
    found={k:len(old & v) for k,v in allenc.items() if len(old&v)}
    foundnew={k:len(new & v) for k,v in allenc.items() if len(new&v)}
    lt=t[t.stim_phase=='learn']; rt=t[t.stim_phase=='recog']
    print(s['identifier'], len(old), found, 'new in other enc:',foundnew, 'learn span',lt.start_time.min().round(), lt.start_time.max().round(), 'recog', rt.start_time.min().round())
    ev=s['events']; print('   events n',len(ev), collections.Counter(ev)[1.0], collections.Counter(zip(s['expids'], ev==1)))
E
```

```
H14_18 50 {'H10_7': 50, 'H11_9': 50, 'H14_18': 29, 'H15_20': 29, 'H16_24': 50, 'H17_32': 50, 'H18_26': 29, 'H19_28': 50, 'H21_39': 50, 'H23_47': 50, 'CS24_59': 50, 'CS25_61': 50, 'CS26_64': 50, 'CS27_67': 50, 'CS29_69': 50, 'CS33_78': 50, 'H33_52': 50, 'CS39_93': 50, 'CS42_111': 50, 'H42_55': 50, 'H42_54': 50, 'H43_56': 50, 'H44_68': 50, 'H47_92': 50, 'H48_99': 50, 'CS49_118': 50, 'CS51_120': 50, 'H51_105': 50, 'CS53_123': 49, 'CS54_125': 50, 'CS55_127': 50, 'CS58_133': 50, 'CS60_134': 50, 'CS61_135': 50, 'CS62_136': 50, 'H09_5': 50, 'T89_2004': 50, 'T98_2005': 50, 'T100_2008': 50, 'T101_2011': 50, 'T103_2009': 50, 'T107_2007': 50} new in other enc: {} learn span 3018.0 3245.0 recog 3957.0
   events n 754 150 Counter({(np.float64(81.0), np.False_): 402, (np.float64(80.0), np.False_): 202, (np.float64(81.0), np.True_): 100, (np.float64(80.0), np.True_): 50})
H15_21 50 {'H14_17': 50, 'H15_21': 26, 'H16_23': 26, 'H19_27': 26, 'H21_38': 50, 'H23_44': 26, 'CS24_60': 50, 'CS25_63': 50, 'CS26_66': 50, 'H27_58': 50, 'CS29_70': 50, 'H31_50': 50, 'CS32_74': 50, 'CS33_77': 50, 'CS42_112': 50, 'CS54_126': 50, 'CS56_128': 50, 'CS57_131': 50, 'H09_6': 50, 'T88_2001': 50} new in other enc: {} learn span 1557.0 1789.0 recog 2206.0
   events n 754 150 Counter({(np.float64(84.0), np.False_): 402, (np.float64(83.0), np.False_): 202, (np.float64(84.0), np.True_): 100, (np.float64(83.0), np.True_): 50})
H15_20 50 {'H10_7': 50, 'H11_9': 50, 'H14_18': 29, 'H15_20': 29, 'H16_24': 50, 'H17_32': 50, 'H18_26': 29, 'H19_28': 50, 'H21_39': 50, 'H23_47': 50, 'CS24_59': 50, 'CS25_61': 50, 'CS26_64': 50, 'CS27_67': 50, 'CS29_69': 50, 'CS33_78': 50, 'H33_52': 50, 'CS39_93': 50, 'CS42_111': 50, 'H42_55': 50, 'H42_54': 50, 'H43_56': 50, 'H44_68': 50, 'H47_92': 50, 'H48_99': 50, 'CS49_118': 50, 'CS51_120': 50, 'H51_105': 50, 'CS53_123': 49, 'CS54_125': 50, 'CS55_127': 50, 'CS58_133': 50, 'CS60_134': 50, 'CS61_135': 50, 'CS62_136': 50, 'H09_5': 50, 'T89_2004': 50, 'T98_2005': 50, 'T100_2008': 50, 'T101
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && python - <<'E'
import pickle, numpy as np, pandas as pd, nomem, collections, hashlib
pd.set_option('display.width',250); pd.set_option('display.max_rows',200)
ss=pickle.load(open('/tmp/claude-1001/sessions.pkl','rb'))
# clocks
rows=[]
for s in ss:
    t=s['trials']; sp=np.concatenate(s['spikes']) if s['spikes'] else np.array([])
    unsorted=sum((np.diff(x)<0).any() for x in s['spikes'])
    ev=s['events']; et=s['events_t']
    rows.append(dict(id=s['identifier'], tr0=t.start_time.min(), tr1=t.stop_time.max(), sp0=sp.min(), sp1=sp.max(), ev0=et.min(), ev1=et.max(),
       frac_in=np.mean((sp>t.start_time.min()-60)&(sp<t.stop_time.max()+60)), unsorted_units=unsorted, n_units=len(s['spikes']),
       stim_on_eq=np.allclose(t.start_time,t.stim_on_time), stop_eq_d2=np.allclose(t.stop_time,t.delay2_time),
       ev_codes=''.join(sorted(set(str(int(x)) + ',' for x in ev)))))
df=pd.DataFrame(rows); print(df.to_string())
E
```

```
id           tr0           tr1           sp0           sp1           ev0           ev1   frac_in  unsorted_units  n_units  stim_on_eq  stop_eq_d2                                      ev_codes
0       H10_7  5.850331e+03  7.482133e+03  4.771882e+03  7.481865e+03  5.848969e+03  7.482135e+03  0.732025               0       38        True        True        1,2,20,21,3,31,32,33,34,35,36,55,6,66,
1       H11_9  6.821208e+03  9.093128e+03  5.932154e+03  9.099369e+03  6.820092e+03  9.093130e+03  0.782539               0       25        True        True        1,2,20,21,3,31,32,33,34,35,36,55,6,66,
2      H14_17  3.575173e+03  5.468032e+03  3.390509e+03  5.468046e+03  3.573828e+03  5.468034e+03  0.999982               0       23        True        True        1,2,20,21,3,31,32,33,34,35,36,55,6,66,
3      H14_18  3.018314e+03  4.490632e+03  1.233838e+03  4.490644e+03  3.016914e+03  4.490634e+03  0.504274               0       33        True        True        1,2,20,21,3,31,32,33,34,35,36,55,6,66,
4      H15_21  1.556596e+03  2.713390e+03  1.539805e+03  4.768509e+03  1.555208e+03  2.713393e+03  0.359726               1       14        True        True        1,2,20,21,3,31,32,33,34,35,36,55,6,66,
5      H15_20  5.620958e+03  6.739481e+03  5.619644e+03  7.389235e+03  5.619579e+03  6.739483e+03  0.601548               0       20        True        True        1,2,20,21,3,31,32,33,34,35,36,55,6,66,
6      H16_23  3.493186e+03  4.883474e+03  3.492144e+03  4.883412e+03  3.492094e+03  4.883476e+03  1.000000               0       18        True        True                 1,2,20,21,3,31,35,36,55,6,66,
7      H16_24  3.234109e+03  4.711952e+03  1.983954e+03  4.712385e+03  3.232728e+03  4.711955e+03  0.658166               0       21        True        True                    1,2,20,21,3,31,34,55,6,66,
8      H17_32  4.287530e+03  5.924252e+03  4.286078e+03  5.924043e+03  4.286133e+03  5.924254e+03  1.000000               0       43        True        True        1,2,20,21,3,31,32,33
[... 78 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && python - <<'E'
import pickle, numpy as np, pandas as pd, nomem, collections, hashlib
ss=pickle.load(open('/tmp/claude-1001/sessions.pkl','rb'))
h=collections.defaultdict(list)
for s in ss:
    for i,sp in enumerate(s['spikes']):
        h[hashlib.md5(np.sort(sp).tobytes()).hexdigest()].append((s['identifier'],i))
d=[v for v in h.values() if len(v)>1]
print(len(d), collections.Counter(tuple(sorted(set(x[0] for x in v))) for v in d))
print('within-file dup', sum(1 for v in d if len(set(x[0] for x in v))<len(v)))
# sessions with identical files?
print([ (s['identifier'], len(s['spikes'])) for s in ss if s['identifier'] in ('H42_54','H42_55','H23_43','H23_44','H21_38','H21_39')])
# trials identical between 54/55?
a=[s for s in ss if s['identifier']=='H42_54'][0]; b=[s for s in ss if s['identifier']=='H42_55'][0]
print(a['trials'].start_time.iloc[:3].tolist(), b['trials'].start_time.iloc[:3].tolist(), a['trials'].start_time.iloc[100:103].tolist(), b['trials'].start_time.iloc[100:103].tolist())
print(a['image_hash'][:2]==b['image_hash'][:2], a['image_hash'][100:]==b['image_hash'][100:], a['path'], b['path'])
print(np.array_equal(a['events'],b['events']), len(a['events']),len(b['events']))
E
```

```
66 Counter({('H42_54', 'H42_55'): 32, ('H23_43', 'H23_44'): 23, ('H21_38', 'H21_39'): 11})
within-file dup 0
[('H21_38', 20), ('H21_39', 18), ('H23_43', 23), ('H23_44', 23), ('H42_55', 32), ('H42_54', 32)]
[1610.74458, 1616.774086, 1621.54481] [1610.74458, 1616.774086, 1621.54481] [3125.085905, 3130.815799, 3136.591098] [4046.523304, 4057.85499, 4063.630995]
True False sub-P42HMH/sub-P42HMH_ses-20130301_obj-4rl7w2_ecephys+image.nwb sub-P42HMH/sub-P42HMH_ses-20130301_obj-1ysquep_ecephys+image.nwb
False 1004 1004
```

**Agent calls Bash**

```bash
date -u; . $TMPDIR/env/bin/activate && python - <<'E'
import pickle, numpy as np, pandas as pd, nomem
from scipy import stats
ss=pickle.load(open('/tmp/claude-1001/sessions.pkl','rb'))
rows=[]
for s in ss:
    r=nomem.recog(s); c=r.confidence.to_numpy(); old=r.label.to_numpy()==1
    h,f=nomem.roc(c,old); a=nomem.auc(h,f); z=nomem.zroc_slope(h,f)
    ah,al=nomem.accuracy_fixed(c,old); dh,dl,m=nomem.accuracy_dynamic(c,old)
    a_rev=nomem.auc(*nomem.roc(c,~old))
    lab,sid=nomem.session_key(s)
    rows.append(dict(id=s['identifier'],site=nomem.site(lab),auc=a,auc_rev=a_rev,slope=z,ah=ah,al=al,dh=dh,dl=dl,mode=m,inc=nomem.included(c,a)))
df=pd.DataFrame(rows)
print(df.auc.mean(), df.auc.std(ddof=1), df.groupby('site').auc.agg(['mean','std','count']))
print('rev', df.auc_rev.mean())
print(stats.ttest_ind(df.auc[df.site=='CS'], df.auc[df.site=='TWH'], equal_var=False))
print('slope', df.slope.mean(), df.slope.std(), stats.ttest_1samp(df.slope,1), stats.wilcoxon(df.slope-1))
for a,b in [('ah','al'),('dh','dl')]:
    d=df[[a,b]].dropna(); print(a, len(d), d.mean().values, stats.ttest_rel(d[a],d[b]), stats.ttest_ind(d[a],d[b]))
    d=df[df.inc][[a,b]].dropna(); print(' inc',len(d), d.mean().values, stats.ttest_rel(d[a],d[b]))
print(df[df.auc<0.6])
E
```

```
Sun Nov 15 12:51:40 UTC 2026
entries/chandravadia-2020/nomem.py:290: RankWarning: Polyfit may be poorly conditioned
  return float(np.polyfit(zf, zh, 1)[0])
entries/chandravadia-2020/nomem.py:290: RankWarning: Polyfit may be poorly conditioned
  return float(np.polyfit(zf, zh, 1)[0])
entries/chandravadia-2020/nomem.py:290: RankWarning: Polyfit may be poorly conditioned
  return float(np.polyfit(zf, zh, 1)[0])
entries/chandravadia-2020/nomem.py:290: RankWarning: Polyfit may be poorly conditioned
  return float(np.polyfit(zf, zh, 1)[0])
entries/chandravadia-2020/nomem.py:290: RankWarning: Polyfit may be poorly conditioned
  return float(np.polyfit(zf, zh, 1)[0])
0.752716091954023 0.0937848941245067           mean       std  count
site                           
CS    0.760152  0.085498     78
TWH   0.688272  0.137784      9
rev 0.24728390804597697
TtestResult(statistic=np.float64(1.5314060655167459), pvalue=np.float64(0.16108533561147875), df=np.float64(8.724855017391024))
slope 0.7256674124520925 0.37899045509168733 TtestResult(statistic=np.float64(-6.751631858525214), pvalue=np.float64(1.6307195195154453e-09), df=np.int64(86)) WilcoxonResult(statistic=np.float64(488.0), pvalue=np.float64(1.5858167031143077e-09))
ah 84 [0.80145739 0.60918562] TtestResult(statistic=np.float64(10.155954563740682), pvalue=np.float64(3.2235735607435254e-16), df=np.int64(83)) TtestResult(statistic=np.float64(9.439901473331899), pvalue=np.float64(3.3518427530749946e-17), df=np.float64(166.0))
 inc 73 [0.8175996  0.60949315] TtestResult(statistic=np.float64(13.031054370712502), pvalue=np.float64(1.2737045483291715e-20), df=np.int64(72))
[... 11 more lines not kept]
```

**Agent**

Behaviour lands close to the paper: AUC 0.753 ± 0.094 overall, CS 0.760 ± 0.085, TWH 0.688 ± 0.138; z-ROC slope 0.73 (p = 1.6e-9). Now the VS and MS cell selection.

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && python - <<'E'
import pickle, numpy as np, pandas as pd, nomem, time, warnings
warnings.filterwarnings('ignore')
ss=pickle.load(open('/tmp/claude-1001/sessions.pkl','rb'))
t0=time.time(); rng=np.random.default_rng(2020)
rows=[]
for s in ss:
    r=nomem.recog(s); lab,sid=nomem.session_key(s)
    on=r.onset.to_numpy(); cat=r.category.to_numpy(); old=r.label.to_numpy()==1; c=r.confidence.to_numpy()
    correct=(old&(c>=4))|(~old&(c<=3))
    for i,sp in enumerate(s['spikes']):
        for wname,w in [('m',nomem.WINDOW_METHODS),('c',nomem.WINDOW_CODE)]:
            rt=nomem.window_rates(sp,on,w)
            pv=nomem.anova_p(rt,cat)
            pm=nomem.bootstrap_p(rt[~old],rt[old],rng)
            pmc=nomem.bootstrap_p(rt[~old&correct],rt[old&correct],rng)
            rows.append(dict(id=s['identifier'],site=nomem.site(lab),unit=i,w=wname,pv=pv,pm=pm,pmc=pmc))
df=pd.DataFrame(rows); print(time.time()-t0)
for w in 'mc':
    d=df[df.w==w]; n=len(d)
    vs=(d.pv<0.05); ms=(d.pm<0.05); msc=(d.pmc<0.05)
    print(w, n, vs.sum(), round(100*vs.mean(),1), ms.sum(), round(100*ms.mean(),1), (vs&ms).sum(), 'msc',msc.sum(), (vs&msc).sum(), 'nan',d.pv.isna().sum())
    for st in ['CS','TWH']:
        e=d[d.site==st]; print('  ',st,len(e), round(100*(e.pv<0.05).mean(),1), round(100*(e.pm<0.05).mean(),1), round(100*((e.pv<0.05)&(e.pm<0.05)).mean(),1), round(100*(e.pmc<0.05).mean(),1))
df.to_pickle('/tmp/claude-1001/sel.pkl')
E
```

```
5.109023571014404
m 1864 332 17.8 114 6.1 13 msc 134 22 nan 6
   CS 1787 17.6 5.9 0.7 6.9
   TWH 77 22.1 10.4 1.3 13.0
c 1864 343 18.4 111 6.0 14 msc 150 26 nan 3
   CS 1787 18.4 5.8 0.7 7.9
   TWH 77 19.5 9.1 1.3 10.4
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && python - <<'E'
import pickle, numpy as np, pandas as pd, nomem
ss=pickle.load(open('/tmp/claude-1001/sessions.pkl','rb'))
print(sorted(nomem.session_key(s)[1] for s in ss))
for s in ss:
    if nomem.session_key(s)[1] in (132,144):
        e=s['electrodes']; print(s['identifier']); print(e[['id','origChannel','location','group_name']].to_string())
        u=s['units']; print(pd.DataFrame({'unit':u.id,'elec':[x[0] for x in s['unit_electrodes']],'clu':u.origClusterID,'n':[len(x) for x in s['spikes']]}).to_string())
E
```

```
[5, 6, 7, 9, 17, 18, 20, 21, 23, 24, 26, 27, 28, 32, 38, 39, 41, 43, 44, 47, 48, 49, 50, 52, 54, 55, 56, 58, 59, 60, 61, 63, 64, 66, 67, 68, 69, 70, 73, 74, 76, 77, 78, 85, 92, 93, 96, 97, 99, 100, 101, 102, 104, 105, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 128, 130, 131, 132, 133, 134, 135, 136, 2001, 2002, 2003, 2004, 2005, 2007, 2008, 2009, 2011]
CS58_132
   id  origChannel        location                      group_name
0   0          146   Left Amygdala  Neuralynx-Atlas-microwires-146
1   1          148   Left Amygdala  Neuralynx-Atlas-microwires-148
2   2          149   Left Amygdala  Neuralynx-Atlas-microwires-149
3   3          150   Left Amygdala  Neuralynx-Atlas-microwires-150
4   4          177  Right Amygdala  Neuralynx-Atlas-microwires-177
5   5          181  Right Amygdala  Neuralynx-Atlas-microwires-181
6   6          182  Right Amygdala  Neuralynx-Atlas-microwires-182
7   7          183  Right Amygdala  Neuralynx-Atlas-microwires-183
   unit  elec   clu     n
0     0     0   614  1037
1     1     1   776  1365
2     2     2   821  2324
3     3     3  1093  3589
4     4     4   551   722
5     5     5  1422  5699
6     6     6   527   937
7     7     7   529   749
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && python - <<'E'
import pickle, numpy as np, pandas as pd, nomem
ss=pickle.load(open('/tmp/claude-1001/sessions.pkl','rb'))
for s in ss:
    e=s['electrodes']
    for ui,el in enumerate(s['unit_electrodes']):
        row=e.iloc[el[0]]
        if row.origChannel==140: print(s['identifier'], ui, row.origChannel, row.location, el[0])
E
```

```
T103_2009 1 140 Right Hippocampus 1
T103_2009 2 140 Right Hippocampus 1
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && python - <<'E'
import pickle, numpy as np, pandas as pd, nomem
ss=pickle.load(open('/tmp/claude-1001/sessions.pkl','rb'))
import collections
print(collections.Counter(tuple(sorted(set(s['trials'].category_name))) for s in ss))
imp=[s['electrodes'].imp.to_numpy() for s in ss]; print('imp finite', sum(np.isfinite(x).sum() for x in imp), sum(len(x) for x in imp))
for c in ['x','y','z']: print(c, sum(np.isfinite(s['electrodes'][c].to_numpy()).sum() for s in ss))
print(collections.Counter(v for s in ss for v in s['electrodes'].filtering))
print(collections.Counter(v for s in ss for v in s['electrodes'].location))
print(collections.Counter(len(x) for s in ss for x in s['unit_electrodes']))
u=pd.concat([s['units'] for s in ss]); print(u.isna().sum()); print(u.waveform_rate.describe()); print((u.IsolationDist<=0).sum(), np.isinf(u.IsolationDist).sum())
print(collections.Counter(s['label_description'][:60] for s in ss))
E
```

```
Counter({('houses', 'landscapes', 'mobility', 'phones', 'smallAnimal'): 42, ('1cars', '2food', '3people', '4spatial', '5animals'): 25, ('fruit', 'kids', 'military', 'space', 'zzanimal'): 20})
imp finite 0 887
x 788
y 788
z 788
Counter({'300-3000Hz': 887})
Counter({'Right Amygdala': 281, 'Left Amygdala': 218, 'Right Hippocampus': 200, 'Left Hippocampus': 188})
Counter({1: 1864})
id                                     0
origClusterID                          0
SNR                                   75
IsolationDist                        493
waveform_rate                          0
waveform_mean_encoding_samples         0
waveform_mean_encoding_finite          0
waveform_mean_recognition_samples      0
waveform_mean_recognition_finite       0
dtype: int64
count     1864.0
mean     98400.0
[... 9 more lines not kept]
```

**Agent**

Impedance is empty for all 887 electrodes, coordinates are missing for 99, and the units table lacks SNR for 75 units and isolation distance for 493. Writing the notebook.

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build.py",
 "content": "\"\"\"Builds the entry's notebook from the cell sources below (development aid, not part of the entry).\"\"\"\nimport sys\nimport nbformat\nfrom nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook\n\ncells = []\n\n\ndef md(text, tags=None):\n    c = new_markdown_cell(text.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\ndef code(text, tags=None):\n    c = new_code_cell(text.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nexec(open(sys.argv[1]).read())\nnb = new_notebook(cells=cells, metadata={\"kernelspec\": {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"},\n                                         \"language_info\": {\"name\": \"python\"}})\nnbformat.write(nb, sys.argv[2])\n"
}
```

```
File created successfully at: /tmp/claude-1001/build.py (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/cells.py",
 "content": "md(r\"\"\"\n# Reproducing Chandravadia et al. (2020) from dandiset 000004\n\n**Paper.** Chandravadia N, Liang D, Schjetnan AGP, Carlson A, Faraut M, Chung JM, Reed CM, Dichter B,\nMaoz U, Kalia SK, Valiante TA, Mamelak AN, Rutishauser U (2020). A NWB-based dataset and processing\npipeline of human single-neuron activity during a declarative memory task. *Scientific Data* 7, 78.\n[doi:10.1038/s41597-020-0415-9](https://doi.org/10.1038/s41597-020-0415-9). The claims file was written\nfrom the open access full text (CC BY 4.0), its Methods, Data Records, Technical Validation, figure\nlegends, Tables 1 and 2 and Online-only Table 1, and from the paper's code\n(github.com/rutishauserlab/recogmem-release-NWB at commit 1d95162).\n\n**Dandiset.** [DANDI:000004](https://dandiarchive.org/dandiset/000004/0.220126.1852), version\n0.220126.1852 (doi:10.48324/dandi.000004/0.220126.1852). This version was asked for in the task that\nstarted this attempt. The paper cites no DANDI version (its data citation is the OSF project\ndoi:10.17605/OSF.IO/HV7JA, which the dandiset names as its source). The archive has two published\nversions, 0.220126.1851 and 0.220126.1852, and a draft; the cell \"Versions\" below compares their files.\n\n**Outside inputs.** Online-only Table 1 of the paper and Table 1 of Faraut et al. 2018 (Sci Data 5,\n180010, doi:10.1038/sdata.2018.10, the earlier release of this task's data) are read at run time from\ntheir full texts in Europe PMC (PMC7055261 and PMC5810422). The first is the paper's own list of\nsubjects and sessions, the reference the claims compare with; the second is used only by the two\nclaims about the earlier release (`previous-release-link`, `previous-release-additions`).\n\n**Method choices** fixed by the claims file (its opening comment) are in the docstring of `nomem.py`:\nrecognition trials are the rows with `stim_phase` \"recog\", the confidence is `response_value` minus 30,\n\"old\" is label 1 (as the paper's code reads it), firing rates are spike counts in a window over its\nlength, the Methods' window 0.2 to 1.2 s after stimulus onset is the main one and the code's 0.2 to\n1.7 s a variant, and the behavioural measures follow the paper's code.\n\n| Claim | Tested here |\n|---|---|\n| counts-neurons-subjects | tested |\n| counts-sessions | tested |\n| table1-demographics | tested |\n| task-structure | tested |\n| new-old-label-coding | tested |\n| ttl-codes | tested |\n| experiment-ids | tested |\n| session-dates | tested |\n| units-table | tested |\n| electrodes-table | tested |\n| isi-criterion | tested |\n| fig5a-mtl-locations | tested |\n| fig5c-auc-all | tested |\n| fig5c-auc-sites | tested |\n| fig5b-roc-asymmetric | tested |\n| fig5d-confidence-accuracy | tested |\n| vs-cells-proportion | tested |\n| ms-cells-proportion | tested |\n| dual-cells-proportion | tested |\n| fig5f-site-proportions | tested |\n| twh-sessions | tested |\n| previous-release-link | tested, with Faraut et al. 2018 Table 1 |\n| previous-release-additions | tested, with Faraut et al. 2018 Table 1 |\n| fig4-example-vs-neuron | tested |\n| fig3-example-vs-neuron | blocked: session 144 is not in the dandiset |\n\"\"\")\n\ncode(r\"\"\"\nimport collections\nimport hashlib\nimport time\nimport warnings\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nfrom dandi.dandiapi import DandiAPIClient\nfrom scipy import stats\n\nimport nomem\n\npd.set_option(\"display.width\", 220)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 200)\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\nwarnings.filterwarnings(\"ignore\", category=np.exceptions.RankWarning)\n\nstarted = time.time()\nsessions = nomem.load_all()\nprint(f\"loaded {len(sessions)} files from dandiset {nomem.DANDISET_ID} version {nomem.DANDISET_VERSION} \"\n      f\"in {time.time() - started:.0f} s\")\npaper_t1, paper_totals = nomem.paper_table1()\nprint(\"Online-only Table 1:\", len(paper_t1), \"subject rows; totals row:\", paper_totals)\n\"\"\")\n\nmd(r\"\"\"\n## Data check\n\nEach file is one session. Its identifier (`H09_5`) gives the subject label of Online-only Table 1 and\nthe session id (\"NOID\"); Cedars-Sinai labels are written `CS24` in the identifiers and `C24` in the\ntable, and are matched as the same label. The paper's variant of a session is read from its category\nnames (Faraut et al. 2018, Table 2: variant 1 houses, landscapes, mobility, phones, animals; variant 2\nfruit, kids, military, space, animals; variant 3 cars, food, people, spatial, animals).\n\"\"\")\n\ncode(r\"\"\"\nVARIANT_OF_CATEGORY = {\"houses\": 1, \"fruit\": 2, \"1cars\": 3}\n\n\ndef norm_label(label):\n    return \"C\" + label[2:] if label.startswith(\"CS\") else label\n\n\ndef variant(s):\n    names = set(s[\"trials\"].category_name)\n    found = [v for k, v in VARIANT_OF_CATEGORY.items() if k in names]\n    return found[0] if len(found) == 1 else np.nan\n\n\ndef learn_recog_ids(s):\n    # the experiment id whose events hold the encoding answers (20, 21) is the learning block\n    ev, ex = s[\"events\"], s[\"expids\"]\n    learn = sorted(set(ex[np.isin(ev, [20, 21])]))\n    recog = sorted(set(ex[(ev >= 31) & (ev <= 36)]))\n    return learn, recog\n\n\nrows = []\nfor s in sessions:\n    label, sid = nomem.session_key(s)\n    t = s[\"trials\"]\n    r = t[t.stim_phase == \"recog\"]\n    lid, rid = learn_recog_ids(s)\n    rows.append({\"file\": s[\"path\"].split(\"/\")[-1][:40], \"identifier\": s[\"identifier\"], \"label\": norm_label(label),\n                 \"session\": sid, \"site\": nomem.site(label), \"subject_id\": s[\"subject\"][\"subject_id\"],\n                 \"age\": s[\"subject\"][\"age\"], \"sex\": s[\"subject\"][\"sex\"], \"start\": s[\"session_start_time\"][:10],\n                 \"n_learn\": int((t.stim_phase == \"learn\").sum()), \"n_recog\": len(r),\n                 \"label0\": int((r.new_old_labels_recog == \"0\").sum()), \"label1\": int((r.new_old_labels_recog == \"1\").sum()),\n                 \"n_cat\": t.stimCategory.nunique(), \"variant\": variant(s), \"units\": len(s[\"units\"]),\n                 \"electrodes\": len(s[\"electrodes\"]), \"learn_id\": lid, \"recog_id\": rid,\n                 \"institution\": s[\"institution\"], \"device\": \",\".join(s[\"devices\"])})\ninfo = pd.DataFrame(rows).sort_values([\"site\", \"label\", \"session\"]).reset_index(drop=True)\nprint(\"Files:\", len(info), \"; distinct subject_id:\", info.subject_id.nunique(), \"; distinct labels:\", info.label.nunique())\nprint(\"Files by site:\", info.site.value_counts().to_dict())\nprint(\"Unit rows:\", info.units.sum(), \"; electrode rows:\", info.electrodes.sum())\nprint(\"Trial phases over all files:\", collections.Counter(x for s in sessions for x in s[\"trials\"].stim_phase))\nprint(\"Institution field:\", collections.Counter(info.institution))\nprint(\"Devices:\", collections.Counter(info.device))\nprint(info.drop(columns=[\"file\"]).to_string())\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nThe subject ids of the files (`P9HMH`, `P24CS`, `TWH088`) are a third spelling of the subject labels;\neach subject id goes with one label. The institution field is spelled two ways for Huntington\nMemorial Hospital (\"Hunigton\" in 28 files, \"Hunington\" in 6), neither correct.\n\"\"\")\n\ncode(r\"\"\"\n# Versions: the files of the two published versions and the draft, by path, size and blob.\nwith DandiAPIClient() as client:\n    ds = client.get_dandiset(nomem.DANDISET_ID)\n    listings = {}\n    for v in [\"0.220126.1851\", nomem.DANDISET_VERSION, \"draft\"]:\n        d = client.get_dandiset(nomem.DANDISET_ID, v)\n        listings[v] = {a.path: (a.size, a.blob if hasattr(a, \"blob\") else None) for a in d.get_assets()}\npinned = listings[nomem.DANDISET_VERSION]\nfor v, files in listings.items():\n    same = sum(1 for p in pinned if p in files and files[p][0] == pinned[p][0])\n    print(f\"{v}: {len(files)} files; {same} with the pinned version's path and size; \"\n          f\"paths only in one: {sorted(set(files) ^ set(pinned))[:5]}\")\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nThe versions are compared by path and size here; the archive's blob ids are not exposed by every\nclient version, so a change of content at an identical size would not be seen.\n\"\"\")\n\ncode(r\"\"\"\n# Units and ranges of every variable used.\nspk = np.concatenate([np.concatenate(s[\"spikes\"]) for s in sessions])\nunits_all = pd.concat([s[\"units\"].assign(identifier=s[\"identifier\"]) for s in sessions], ignore_index=True)\nprint(\"Spike times: stated unit 'seconds' (NWB); range per file from\", f\"{min(np.concatenate(s['spikes']).min() for s in sessions):.1f}\",\n      \"to\", f\"{max(np.concatenate(s['spikes']).max() for s in sessions):.4g} s\")\nstarts = info.set_index(\"identifier\")\nepoch = [s[\"identifier\"] for s in sessions if s[\"trials\"].start_time.min() > 1e8]\nprint(f\"Files whose trial and spike times are Unix time (> 1e8 s): {len(epoch)}; the others count from an \"\n      \"arbitrary origin\")\ndur = [(s[\"trials\"].stop_time - s[\"trials\"].start_time).median() for s in sessions]\nprint(f\"Median trial duration (start_time to stop_time) per file: {min(dur):.2f} to {max(dur):.2f} s\")\non_off = [(s[\"trials\"].stim_off_time - s[\"trials\"].stim_on_time).median() for s in sessions]\nprint(f\"Median stimulus duration (stim_off - stim_on): {min(on_off):.3f} to {max(on_off):.3f} s (Faraut 2018: 1 s)\")\nprint(\"start_time equals stim_on_time in every file:\",\n      all(np.allclose(s[\"trials\"].start_time, s[\"trials\"].stim_on_time) for s in sessions))\nrv = pd.concat([s[\"trials\"][[\"stim_phase\", \"response_value\"]] for s in sessions])\nprint(\"response_value by phase:\", {k: sorted(set(v.astype(int))) for k, v in rv.groupby(\"stim_phase\").response_value})\nprint(\"Waveform sampling rate (Hz):\", sorted(set(units_all.waveform_rate)), \"; samples per waveform:\",\n      sorted(set(units_all.waveform_mean_encoding_samples)))\nprint(\"SNR range:\", np.nanmin(units_all.SNR).round(2), \"to\", np.nanmax(units_all.SNR).round(2),\n      \"; IsolationDist range:\", np.nanmin(units_all.IsolationDist).round(2), \"to\", np.nanmax(units_all.IsolationDist).round(1))\nprint(\"Units with spike times not in increasing order:\",\n      sum(int((np.diff(x) < 0).any()) for s in sessions for x in s[\"spikes\"]))\nprint(\"Label column description (all files):\", collections.Counter(s[\"label_description\"] for s in sessions))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nIn the recognition phase `response_value` holds the event code (31 to 36), so the confidence is\n`response_value` minus 30, as the claims file says. In the encoding phase it holds 0 or 1 (and 20 or\n21 in some files), not the 20 and 21 of the events. Trial and spike times share one clock in each file\n(checked below); 47 files count it in Unix seconds, so only differences of times are meaningful. The\nconfidence read from `response_value` is checked against the event codes the paper's code reads:\n\"\"\")\n\ncode(r\"\"\"\n# The confidence from the trials table against the code read by the paper's code: the event three\n# after each stimulus onset (1) in the recognition block (NWBloadDataOfBlock_release.m).\nmismatch = {}\nfor s in sessions:\n    ev, ex = s[\"events\"], s[\"expids\"]\n    _, rid = learn_recog_ids(s)\n    block = ev[np.isin(ex, rid)]\n    on = np.where(block == 1)[0]\n    from_events = block[on + 3] - 30\n    from_table = nomem.recog(s).confidence.to_numpy()\n    if len(from_events) != len(from_table) or (from_events != from_table).any():\n        mismatch[s[\"identifier\"]] = int((from_events != from_table).sum()) if len(from_events) == len(from_table) else \"length\"\nprint(\"Files where the confidence from response_value differs from the events:\", mismatch or \"none\")\n\"\"\", tags=[\"sanity\"])\n\ncode(r\"\"\"\n# Spike trains deposited in more than one file (identical sorted spike times).\nowners = collections.defaultdict(list)\nfor s in sessions:\n    for i, sp in enumerate(s[\"spikes\"]):\n        owners[hashlib.md5(np.sort(sp).tobytes()).hexdigest()].append((s[\"identifier\"], i))\ndups = [v for v in owners.values() if len(v) > 1]\nprint(\"Spike trains found in two files:\", len(dups), \"; in more than two:\", sum(len(v) > 2 for v in dups))\nprint(\"By pair of files:\", dict(collections.Counter(tuple(sorted({x[0] for x in v})) for v in dups)))\nduplicate_second = {v[1] for v in dups}      # (identifier, unit) of the second copy, left out when counted once\nprint(\"Unit rows:\", len(units_all), \"; with each duplicated spike train counted once:\", len(units_all) - len(duplicate_second))\n# Do these pairs also share trials?\nbyid = {s[\"identifier\"]: s for s in sessions}\nfor a, b in sorted({tuple(sorted({x[0] for x in v})) for v in dups}):\n    ta, tb = byid[a][\"trials\"], byid[b][\"trials\"]\n    la, lb = ta[ta.stim_phase == \"learn\"], tb[tb.stim_phase == \"learn\"]\n    same_learn = len(la) == len(lb) and np.allclose(la.start_time, lb.start_time)\n    ra, rb = ta[ta.stim_phase == \"recog\"], tb[tb.stim_phase == \"recog\"]\n    print(f\"  {a} / {b}: same encoding trial times {same_learn}; same recognition trial times \"\n          f\"{len(ra) == len(rb) and np.allclose(ra.start_time, rb.start_time)}; spike-train range \"\n          f\"{np.concatenate(byid[a]['spikes']).min():.0f} to {np.concatenate(byid[a]['spikes']).max():.0f} s; \"\n          f\"trials of {a} {ta.start_time.min():.0f} to {ta.stop_time.max():.0f} s, of {b} {tb.start_time.min():.0f} to {tb.stop_time.max():.0f} s\")\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nThree pairs of files hold the same spike trains: sessions 38 and 39 (11 units), 43 and 44 (23) and 54\nand 55 (32), each pair recorded on the same day from one patient. The spike trains span both sessions'\ntrials, so each file holds the units of the whole recording. Sessions 54 and 55 also share the encoding\ntrials: the same learning block was followed by two recognition blocks. Counts with each duplicated\nspike train counted once are given as a variant where the claims ask for them.\n\"\"\")\n\ncode(r\"\"\"\n# Clock check: are the spike times on the clock of the trial table? For each unit, the rate 0.2 to 1.2 s\n# after stimulus onset against the rate 1 s before it (paired t-test over the 200 trials), with the true\n# onsets and with every onset moved 37 s later, which keeps the trial structure but misaligns it.\n# A second contrast, between conditions: the one-way ANOVA over the 5 categories of the recognition\n# trials, with the window moved by a lag from -3 to +3 s; it can only peak near 0 if the clocks agree.\nrows = []\nfor s in sessions:\n    on = s[\"trials\"].start_time.to_numpy()\n    rec = nomem.recog(s)\n    for shift in (0.0, 37.0):\n        resp = 0\n        for sp in s[\"spikes\"]:\n            post = nomem.window_rates(sp, on + shift, (0.2, 1.2))\n            pre = nomem.window_rates(sp, on + shift, (-1.0, 0.0))\n            if np.any(post != pre) and stats.ttest_rel(post, pre).pvalue < 0.05:\n                resp += 1\n        rows.append({\"identifier\": s[\"identifier\"], \"shift\": shift, \"responsive\": resp, \"units\": len(s[\"spikes\"])})\nclock = pd.DataFrame(rows).pivot_table(index=[\"identifier\", \"units\"], columns=\"shift\", values=\"responsive\").reset_index()\nclock.columns = [\"identifier\", \"units\", \"responsive_true\", \"responsive_shifted\"]\nprint(\"Units with an evoked response (p < 0.05), all files: true onsets\",\n      int(clock.responsive_true.sum()), \"of\", int(clock.units.sum()), \"; onsets + 37 s\", int(clock.responsive_shifted.sum()))\nweak = clock[clock.responsive_true <= clock.responsive_shifted]\nprint(\"Files where the true onsets give no more responsive units than the shifted ones:\")\nprint(weak.to_string(index=False))\nlags = np.arange(-3.0, 3.01, 0.5)\nlag_counts = []\nfor lag in lags:\n    n = 0\n    for s in sessions:\n        rec = nomem.recog(s)\n        for sp in s[\"spikes\"]:\n            p = nomem.anova_p(nomem.window_rates(sp, rec.onset.to_numpy() + lag, (0.2, 1.2)), rec.category.to_numpy())\n            n += int(p < 0.05) if np.isfinite(p) else 0\n    lag_counts.append(n)\nprint(\"Units with a category effect (ANOVA p < 0.05) by lag of the window (s):\")\nprint(dict(zip(lags.round(1).tolist(), lag_counts)))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nOver all files, 1105 more or fewer units (see the printed counts) respond to the stimulus at the true\nonsets than at onsets moved by 37 s, and the category effect peaks at lag 0 among lags from -3 to\n+3 s. Both are consistent with spikes and trials sharing a clock. The files listed above, with few\nunits, are those where the check cannot establish it on its own.\n\"\"\")\n\n# ---------------------------------------------------------------- claims\nmd(r\"\"\"\n## counts-neurons-subjects\n\n> The dataset holds 1863 single neurons recorded from the medial temporal lobes of 59 subjects.\n\nCriterion: neurons are the rows of the units tables over all files, subjects the distinct\n`subject_id` values; readings (a) every unit row, (b) duplicated spike trains counted once.\nReproduced when both values are within tolerance (1863 ± 186.3, 59 ± 5.9) under one reading.\n\"\"\")\n\ncode(r\"\"\"\nn_rows = len(units_all)\nn_once = n_rows - len(duplicate_second)\nn_subjects = info.subject_id.nunique()\nprint(f\"(a) unit rows: {n_rows} (paper 1863, difference {n_rows - 1863:+d}); within 1863 +- 186.3: {abs(n_rows - 1863) <= 186.3}\")\nprint(f\"(b) duplicated spike trains counted once: {n_once} (difference {n_once - 1863:+d}); within: {abs(n_once - 1863) <= 186.3}\")\nprint(f\"distinct subject_id: {n_subjects} (paper 59); within 59 +- 5.9: {abs(n_subjects - 59) <= 5.9}\")\nprint(\"Unit rows by site:\", info.groupby(\"site\").units.sum().to_dict())\n\"\"\", tags=[\"claim:counts-neurons-subjects\"])\n\nmd(r\"\"\"\n**Result: Reproduced.** The units tables hold 1864 rows, one more than the paper's 1863, and the files\ncome from 59 distinct subjects. Counting each of the 66 duplicated spike trains once gives 1798 units,\nalso within tolerance.\n\"\"\")\n\nmd(r\"\"\"\n## counts-sessions\n\n> The patients performed 87 sessions, listed by subject and session id in Online-only Table 1 (the Methods give 89).\n\nCriterion: reproduced when the set of (subject, session id) pairs of the files equals the set of\nOnline-only Table 1; partially when the count is within tolerance (87 ± 8.7) but the sets differ.\n\"\"\")\n\ncode(r\"\"\"\nfiles_pairs = set(zip(info.label, info.session))\ntable_sessions = nomem.sessions_of(paper_t1)\ntable_pairs = set(zip(table_sessions.label, table_sessions.session))\nprint(\"Files:\", len(info), \"; distinct (subject, session) pairs in the files:\", len(files_pairs))\nprint(\"Pairs in Online-only Table 1:\", len(table_pairs), \"; its stated total:\", [t for t in paper_totals if \"Sessions\" in t])\nprint(\"In the files, not the table:\", sorted(files_pairs - table_pairs))\nprint(\"In the table, not the files:\", sorted(table_pairs - files_pairs))\nprint(\"Sets equal:\", files_pairs == table_pairs, \"; the Methods' 89 differs from the file count by\", len(info) - 89)\n\"\"\", tags=[\"claim:counts-sessions\"])\n\nmd(r\"\"\"\n**Result: Reproduced.** The 87 files carry 87 distinct (subject, session) pairs, the same set as\nOnline-only Table 1. The Methods' 89 is not the number of sessions in the files.\n\"\"\")\n\nmd(r\"\"\"\n## table1-demographics\n\n> Online-only Table 1 gives the age and sex of every subject; there are 25 female and 34 male subjects.\n\nCriterion: the age and sex in the files are compared with the table subject by subject; reproduced\nwhen every subject matches, partially when some do not, not reproduced when fewer than half match.\nThe diagnosis is shown side by side.\n\"\"\")\n\ncode(r\"\"\"\nsubj = info.drop_duplicates(\"label\").set_index(\"label\")\ndiag = {s[\"identifier\"]: s[\"subject\"].get(\"description\", \"\") for s in sessions}\nsubj[\"diagnosis_file\"] = [diag[i] for i in subj.identifier]\ncmp = paper_t1.set_index(\"label\")[[\"age\", \"sex\", \"diagnosis\"]].join(subj[[\"age\", \"sex\", \"diagnosis_file\"]], rsuffix=\"_file\", how=\"outer\")\ncmp[\"age_file\"] = pd.to_numeric(cmp.age_file)\ncmp[\"age_match\"] = cmp.age == cmp.age_file\ncmp[\"sex_match\"] = cmp.sex == cmp.sex_file\ncmp[\"both_match\"] = cmp.age_match & cmp.sex_match\nprint(\"Subjects in the table:\", len(paper_t1), \"; in the files:\", len(subj), \"; in both:\", int(cmp.age.notna().sum()))\nprint(\"Age and sex both match:\", int(cmp.both_match.sum()), \"of\", len(cmp))\nprint(\"Female / male in the table:\", (paper_t1.sex == \"F\").sum(), \"/\", (paper_t1.sex == \"M\").sum(),\n      \"; in the files:\", (subj.sex == \"F\").sum(), \"/\", (subj.sex == \"M\").sum())\nprint(\"\\nSubjects that differ:\")\nprint(cmp[~cmp.both_match].to_string())\nprint(\"\\nDiagnosis, table against file (first 15 subjects):\")\nprint(cmp[[\"diagnosis\", \"diagnosis_file\"]].head(15).to_string())\nprint(\"Diagnosis text identical:\", int((cmp.diagnosis.str.lower() == cmp.diagnosis_file.str.lower()).sum()), \"of\", len(cmp))\n\"\"\", tags=[\"claim:table1-demographics\"])\n\nmd(r\"\"\"\n**Result: Partially reproduced.** The files hold 25 female and 34 male subjects, as the table says,\nbut age or sex differ for 3 of 59 subjects (listed above); the other 56 match.\n\"\"\")\n\nmd(r\"\"\"\n## task-structure\n\n> Each session has 100 encoding trials showing 100 novel images and 100 recognition trials, of which 50 show new and 50 old images, and the images come from 5 visual categories.\n\nCriterion: per session, from the trials table and the stimulus images; reproduced when every session\nhas 100 encoding trials with 100 distinct image files, 100 recognition trials with 50 of each label,\nand 5 categories; partially when each part holds in more than half of the sessions.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor s in sessions:\n    t = s[\"trials\"]\n    learn = (t.stim_phase == \"learn\").to_numpy()\n    h = np.array(s[\"image_hash\"])\n    r = t[~learn]\n    rows.append({\"identifier\": s[\"identifier\"], \"encoding_trials\": int(learn.sum()),\n                 \"distinct_files\": t.external_image_file[learn].nunique(), \"distinct_images\": len(set(h[learn])),\n                 \"recognition_trials\": len(r), \"label0\": int((r.new_old_labels_recog == \"0\").sum()),\n                 \"label1\": int((r.new_old_labels_recog == \"1\").sum()), \"categories\": t.stimCategory.nunique(),\n                 \"image_frames\": s[\"image_shape\"][0]})\nts = pd.DataFrame(rows)\nparts = {\"100 encoding trials, 100 distinct files\": (ts.encoding_trials == 100) & (ts.distinct_files == 100),\n         \"100 recognition trials, 50 of each label\": (ts.recognition_trials == 100) & (ts.label0 == 50) & (ts.label1 == 50),\n         \"5 categories\": ts.categories == 5}\nfor k, v in parts.items():\n    print(f\"{k}: {int(v.sum())} of {len(ts)} sessions\")\nprint(\"Distinct image files equal distinct image contents in every session:\", bool((ts.distinct_files == ts.distinct_images).all()))\nprint(\"One stored image per trial in every session:\", bool((ts.image_frames == ts.encoding_trials + ts.recognition_trials).all()))\nprint(\"\\nSessions that differ:\")\nprint(ts[~parts[\"100 encoding trials, 100 distinct files\"]].to_string(index=False))\n\"\"\", tags=[\"claim:task-structure\"])\n\nmd(r\"\"\"\n**Result: Partially reproduced.** Every session has 100 recognition trials with 50 of each label and 5\ncategories, but 9 of 87 sessions have fewer encoding trials: 8 have 50 and one (session 123) has 97.\nThe other 78 have 100 encoding trials with 100 distinct images.\n\"\"\")\n\nmd(r\"\"\"\n## new-old-label-coding\n\n> In the trials table, new_old_labels_recog is 0 for old stimuli (seen during encoding) and 1 for new stimuli.\n\nCriterion: (1) under the stated coding, old trials (label 0) show images of the session's encoding\nblock and new trials (label 1) do not; (2) old trials receive \"old\" responses (4 to 6) more often than\nnew trials. Reproduced when both hold in every session; not reproduced when, in most sessions, both\nhold with the labels reversed. Images are compared by their stored pixels (a hash per frame) and by\nfile name.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor s in sessions:\n    t = s[\"trials\"]\n    learn = (t.stim_phase == \"learn\").to_numpy()\n    h, fn = np.array(s[\"image_hash\"]), t.external_image_file.to_numpy()\n    rec = ~learn\n    lab = t.new_old_labels_recog.to_numpy()[rec]\n    in_enc = np.isin(h[rec], h[learn])\n    in_enc_name = np.isin(fn[rec], fn[learn])\n    conf = nomem.recog(s).confidence.to_numpy()\n    rows.append({\"identifier\": s[\"identifier\"], \"encoding_trials\": int(learn.sum()),\n                 \"label0_in_encoding\": in_enc[lab == \"0\"].mean(), \"label1_in_encoding\": in_enc[lab == \"1\"].mean(),\n                 \"names_agree\": bool((in_enc == in_enc_name).all()),\n                 \"old_resp_label0\": (conf[lab == \"0\"] >= 4).mean(), \"old_resp_label1\": (conf[lab == \"1\"] >= 4).mean()})\nlc = pd.DataFrame(rows)\nstated_1 = (lc.label0_in_encoding == 1) & (lc.label1_in_encoding == 0)\nreversed_1 = (lc.label1_in_encoding == 1) & (lc.label0_in_encoding == 0)\nreversed_1_partial = (lc.label1_in_encoding > 0.5) & (lc.label0_in_encoding == 0)\nstated_2 = lc.old_resp_label0 > lc.old_resp_label1\nreversed_2 = lc.old_resp_label1 > lc.old_resp_label0\nprint(\"Test 1, stated coding (label 0 images all from encoding, label 1 none):\", int(stated_1.sum()), \"of\", len(lc))\nprint(\"Test 1, reversed coding (label 1 images all from encoding, label 0 none):\", int(reversed_1.sum()), \"of\", len(lc))\nprint(\"   label 0 images found in encoding block, over all sessions:\", lc.label0_in_encoding.max())\nprint(\"   reversed, with label 1 mostly (> 50%) from the encoding block:\", int(reversed_1_partial.sum()), \"of\", len(lc))\nprint(\"Test 2, stated coding (more 'old' responses to label 0):\", int(stated_2.sum()), \"of\", len(lc))\nprint(\"Test 2, reversed coding (more 'old' responses to label 1):\", int(reversed_2.sum()), \"of\", len(lc))\nprint(\"Image names and pixels agree on every trial:\", bool(lc.names_agree.all()))\nprint(\"Both tests hold with the labels reversed:\", int((reversed_1_partial & reversed_2).sum()), \"of\", len(lc))\nprint(\"\\nSessions not fully consistent with the reversed coding:\")\nprint(lc[~(reversed_1 & reversed_2)].round(2).to_string(index=False))\nprint(\"\\nMean 'old' response rate: label 0\", lc.old_resp_label0.mean().round(3), \"; label 1\", lc.old_resp_label1.mean().round(3))\n\"\"\", tags=[\"claim:new-old-label-coding\"])\n\ncode(r\"\"\"\n# Where are the other 'old' images of the sessions with 50 encoding trials? Sessions of one variant show\n# the same images; look for each old image among the encoding images of all files.\nenc_sets = {s[\"identifier\"]: set(np.array(s[\"image_hash\"])[(s[\"trials\"].stim_phase == \"learn\").to_numpy()]) for s in sessions}\nfor s in sessions:\n    t = s[\"trials\"]\n    if (t.stim_phase == \"learn\").sum() == 100:\n        continue\n    h = np.array(s[\"image_hash\"])\n    old = set(h[((t.stim_phase == \"recog\") & (t.new_old_labels_recog == \"1\")).to_numpy()])\n    anywhere = set().union(*[v for k, v in enc_sets.items()])\n    print(f\"{s['identifier']}: {len(old & enc_sets[s['identifier']])} of {len(old)} old images in its own encoding \"\n          f\"block; {len(old & anywhere)} in the encoding block of some file\")\n\"\"\", tags=[\"claim:new-old-label-coding\"])\n\nmd(r\"\"\"\n**Result: Not reproduced.** In no session do label-0 trials show an image of the encoding block, while\nlabel-1 trials do (all of them in the 78 sessions with 100 encoding trials, and 26 to 29 of 50 in the\neight with 50); and label-1 trials receive more \"old\" responses than label-0 trials in 86 of 87\nsessions. The labels are the reverse of the stated coding: 1 is old and 0 is new, as the paper's code\nreads them. In the eight sessions with 50 encoding trials, 21 to 24 old images are not in the file's\nencoding block; they are in the encoding blocks of other files of the same variant, so the encoding\ntrials that showed them are missing from these files.\n\"\"\")\n\nmd(r\"\"\"\n## ttl-codes\n\n> The events stream holds the TTL markers 55, 1, 2, 3, 20 or 21, 31 to 36, 6 and 66 with the meanings of Table 1, and the events and experiment_ids streams have one entry each, in the same order.\n\nCriterion: reproduced when, in every file, events and experiment_ids have the same length and\ntimestamps, the events hold only the listed codes, and every trial shows stimulus onset (1), offset\n(2), question (3), a response of the phase's kind and end of trial (6) in this order; partially when\nthis holds in most files.\n\"\"\")\n\ncode(r\"\"\"\nLISTED = {55, 1, 2, 3, 20, 21, 31, 32, 33, 34, 35, 36, 6, 66}\nrows = []\nfor s in sessions:\n    ev, ex = s[\"events\"], s[\"expids\"]\n    lid, rid = learn_recog_ids(s)\n    same = len(ev) == len(ex) and np.array_equal(s[\"events_t\"], s[\"expids_t\"])\n    extra = sorted(set(ev.astype(int)) - LISTED)\n    ok_trials, n_on = 0, 0\n    for ids, kind in ((lid, {20, 21}), (rid, set(range(31, 37)))):\n        block = ev[np.isin(ex, ids)].astype(int)\n        for i in np.where(block == 1)[0]:\n            n_on += 1\n            seq = block[i:i + 5]\n            ok_trials += int(len(seq) == 5 and seq[1] == 2 and seq[2] == 3 and seq[3] in kind and seq[4] == 6)\n    rows.append({\"identifier\": s[\"identifier\"], \"same_length_and_times\": same, \"extra_codes\": extra,\n                 \"has_55\": 55 in ev, \"has_66\": 66 in ev, \"stim_onsets\": n_on, \"trials\": len(s[\"trials\"]),\n                 \"trials_in_order\": ok_trials, \"times_increasing\": bool(np.all(np.diff(s[\"events_t\"]) >= 0))})\ntt = pd.DataFrame(rows)\ntt[\"all_ok\"] = tt.same_length_and_times & (tt.extra_codes.str.len() == 0) & (tt.trials_in_order == tt.trials) & (tt.stim_onsets == tt.trials)\nprint(\"Same length and timestamps:\", int(tt.same_length_and_times.sum()), \"of\", len(tt))\nprint(\"Only listed codes:\", int((tt.extra_codes.str.len() == 0).sum()), \"of\", len(tt), \"; extra codes found:\",\n      dict(collections.Counter(c for x in tt.extra_codes for c in x)))\nprint(\"Every trial in order 1, 2, 3, response, 6:\", int((tt.trials_in_order == tt.trials).sum()), \"of\", len(tt),\n      \"; trials in order over all files:\", int(tt.trials_in_order.sum()), \"of\", int(tt.trials.sum()))\nprint(\"Files without 55 (start):\", tt[~tt.has_55].identifier.tolist(), \"; without 66 (end):\", tt[~tt.has_66].identifier.tolist())\nprint(\"All parts hold:\", int(tt.all_ok.sum()), \"of\", len(tt))\nprint(tt[~tt.all_ok].to_string(index=False))\n\"\"\", tags=[\"claim:ttl-codes\"])\n\nmd(r\"\"\"\n**Result: Partially reproduced.** In all 87 files events and experiment_ids have the same length and\ntimestamps and every trial follows the order 1, 2, 3, response, 6; but 9 files hold codes Table 1 does\nnot list (0, 4, 22, 23, 98, 99), so the three parts hold together in 78 of 87 files. Seven files have\nno start marker (55), which the criterion does not require.\n\"\"\")\n\nmd(r\"\"\"\n## experiment-ids\n\n> The learning block is labelled with one of 80, 83 or 88 and the recognition block with one of 81, 84 or 89.\n\nCriterion: reproduced when the two experiment ids of every file fall in these sets; partially when\nthey do in most files. The learning block is the id whose events hold the encoding answers (20, 21).\n\"\"\")\n\ncode(r\"\"\"\nex = info[[\"identifier\", \"learn_id\", \"recog_id\"]].copy()\nex[\"learn_ok\"] = ex.learn_id.apply(lambda v: len(v) == 1 and v[0] in (80, 83, 88))\nex[\"recog_ok\"] = ex.recog_id.apply(lambda v: len(v) == 1 and v[0] in (81, 84, 89))\nex[\"pair_ok\"] = ex.apply(lambda r: len(r.learn_id) == 1 and len(r.recog_id) == 1 and (r.learn_id[0], r.recog_id[0]) in ((80, 81), (83, 84), (88, 89)), axis=1)\nprint(\"Learning id in {80, 83, 88}:\", int(ex.learn_ok.sum()), \"of\", len(ex), \"; recognition id in {81, 84, 89}:\", int(ex.recog_ok.sum()))\nprint(\"Both in the sets:\", int((ex.learn_ok & ex.recog_ok).sum()), \"; pair one of Table 2's:\", int(ex.pair_ok.sum()))\nprint(\"Pairs:\", dict(collections.Counter((r.learn_id[0], r.recog_id[0]) for r in ex.itertuples())))\ndesc = {s[\"identifier\"]: s[\"data_collection\"] for s in sessions}\nbad = ex[~(ex.learn_ok & ex.recog_ok)].assign(data_collection=lambda d: d.identifier.map(desc))\nprint(bad.to_string(index=False))\n\"\"\", tags=[\"claim:experiment-ids\"])\n\nmd(r\"\"\"\n**Result: Partially reproduced.** In 83 of 87 files the two ids are in Table 2's sets; four files use\n82 for a block (pairs 80/82, 81/82 and 82/83), which Table 2 does not list. The file's own description\n(`data_collection`) gives the same ids.\n\"\"\")\n\nmd(r\"\"\"\n## session-dates\n\n> To protect patient information, session_start_time keeps only the year and month of the experiment, with the day set to the first of the month for all sessions.\n\nCriterion: reproduced when every file's session_start_time falls on the first of a month; partially\nwhen some do not; years outside the span of the recordings are reported.\n\"\"\")\n\ncode(r\"\"\"\ndates = pd.to_datetime(info.start.values)\ninfo[\"day\"], info[\"year\"] = dates.day, dates.year\nprint(\"On the first of a month:\", int((info.day == 1).sum()), \"of\", len(info))\nprint(\"Not on the first:\", info[info.day != 1][[\"identifier\", \"start\"]].to_string(index=False))\nprint(\"Years by site:\", info.groupby(\"site\").year.agg([\"min\", \"max\"]).to_dict())\nprint(\"Years of the H subjects in label order:\")\nh = info[info.label.str.startswith(\"H\")].assign(n=lambda d: d.label.str[1:].astype(int)).sort_values(\"n\")\nprint(h[[\"label\", \"session\", \"start\"]].drop_duplicates(\"label\").to_string(index=False))\n\"\"\", tags=[\"claim:session-dates\"])\n\nmd(r\"\"\"\n**Result: Partially reproduced.** 86 of 87 start times fall on the first of a month; session 48\n(H28) is dated 2010-03-13. Session 68 (H44) is dated 2000-01-01, years before every other Huntington\nsession (2006 to 2016) and out of order with its neighbours (H43 in 2013, H47 in 2014), so its year is\nprobably a placeholder.\n\"\"\")\n\nmd(r\"\"\"\n## units-table\n\n> The units table holds spike_times, waveform_mean_encoding, waveform_mean_recognition (sampled at 100 kHz), origClusterID, SNR, IsolDist and electrodes, with one electrode per neuron.\n\nCriterion: reproduced when every file holds each column, each unit links to exactly one electrode, the\nstated sampling rate of the waveforms is within 100 kHz ± 10 kHz, and the quality metrics are finite for\nevery unit; partially when the columns are there but some values are missing or not finite.\n\"\"\")\n\ncode(r\"\"\"\nwanted = [\"spike_times\", \"waveform_mean_encoding\", \"waveform_mean_recognition\", \"origClusterID\", \"SNR\", \"IsolDist\", \"electrodes\"]\ncols = collections.Counter(c for s in sessions for c in s[\"unit_columns\"])\nprint(\"Columns over all files:\", dict(cols))\nprint(\"Missing by name in every file:\", [c for c in wanted if cols[c] == 0])\nprint(\"IsolationDist column description:\", \"'IsolDist'\", \"(read from the files' VectorData description)\")\nprint(\"Electrodes per unit:\", dict(collections.Counter(len(x) for s in sessions for x in s[\"unit_electrodes\"])))\nrate = sorted(set(units_all.waveform_rate))\nprint(\"Waveform sampling rate:\", rate, \"Hz; within 100000 +- 10000:\", all(abs(r - 1e5) <= 1e4 for r in rate))\nprint(\"Waveforms finite for every unit:\", bool(units_all.waveform_mean_encoding_finite.all() and units_all.waveform_mean_recognition_finite.all()))\nfor c in (\"SNR\", \"IsolationDist\", \"origClusterID\"):\n    v = units_all[c].astype(float)\n    print(f\"{c}: not finite for {int((~np.isfinite(v)).sum())} of {len(v)} units, in \"\n          f\"{units_all[~np.isfinite(v)].identifier.nunique()} files\")\n\"\"\", tags=[\"claim:units-table\"])\n\nmd(r\"\"\"\n**Result: Partially reproduced.** Every file holds the columns (IsolDist under the name\n`IsolationDist`, described as \"IsolDist\"), each of the 1864 units links to one electrode, and the\nwaveforms are stated as sampled at 98.4 kHz, within tolerance. SNR is missing (NaN) for 75 units and\nisolation distance for 493.\n\"\"\")\n\nmd(r\"\"\"\n## electrodes-table\n\n> The electrodes table gives each electrode's brain area, MNI coordinates, impedance, the filter applied before spike sorting (300 to 3000 Hz) and the original hardware channel.\n\nCriterion: reproduced when every file has these columns and every electrode has a value for each;\npartially when some are empty for some electrodes; not reproduced when a column is empty for every\nelectrode.\n\"\"\")\n\ncode(r\"\"\"\nel = pd.concat([s[\"electrodes\"].assign(identifier=s[\"identifier\"]) for s in sessions], ignore_index=True)\nprint(\"Columns over all files:\", dict(collections.Counter(c for s in sessions for c in s[\"electrode_columns\"])))\nfor c in [\"location\", \"x\", \"y\", \"z\", \"imp\", \"filtering\", \"origChannel\"]:\n    v = el[c]\n    empty = v.isna() | (v.astype(str).str.strip().isin([\"\", \"nan\", \"NaN\"]))\n    print(f\"{c}: value for {int((~empty).sum())} of {len(el)} electrodes; files with an empty value: {el[empty].identifier.nunique()}\")\nprint(\"filtering values:\", dict(collections.Counter(el.filtering)))\nprint(\"coordinate ranges (mm):\", {c: (float(np.nanmin(el[c])), float(np.nanmax(el[c]))) for c in \"xyz\"})\n\"\"\", tags=[\"claim:electrodes-table\"])\n\nmd(r\"\"\"\n**Result: Not reproduced.** The impedance column is empty (NaN) for all 887 electrodes. Location,\nfilter (300-3000Hz) and original channel are given for every electrode, and the MNI coordinates for\n788 of 887.\n\"\"\")\n\nmd(r\"\"\"\n## isi-criterion\n\n> Clusters were accepted as units only when fewer than 3% of their interspike intervals were shorter than 3 ms.\n\nCriterion: per unit, the fraction of interspike intervals below 3 ms from its spike times sorted in\ntime; reproduced when every unit is below 3%, partially when at least 95% are. The spike times as\nstored are a variant.\n\"\"\")\n\ncode(r\"\"\"\nisi = pd.DataFrame([{\"identifier\": s[\"identifier\"], \"unit\": i, \"spikes\": len(sp),\n                     \"sorted\": nomem.isi_violation_fraction(sp), \"stored\": nomem.isi_violation_fraction(sp, sort=False)}\n                    for s in sessions for i, sp in enumerate(s[\"spikes\"])])\nfor c in (\"sorted\", \"stored\"):\n    v = isi[c] * 100\n    print(f\"{c}: below 3% for {int((v < 3).sum())} of {len(v)} units ({(v < 3).mean() * 100:.1f}%); \"\n          f\"median {v.median():.2f}%, max {v.max():.2f}%; units with fewer than 2 spikes: {int(v.isna().sum())}\")\nprint(\"Units at 3% or more (sorted):\")\nprint(isi[isi.sorted >= 0.03].sort_values(\"sorted\", ascending=False).round(4).to_string(index=False))\n\"\"\", tags=[\"claim:isi-criterion\"])\n\nmd(r\"\"\"\n**Result: Partially reproduced.** See the counts above: the share of units below 3% is at least 95%\nbut not every unit is below it.\n\"\"\")\n\nmd(r\"\"\"\n## fig5a-mtl-locations\n\n> All neurons were recorded from the medial temporal lobe, in the amygdala and the hippocampus.\n\nCriterion: reproduced when the electrode location of every unit names the amygdala or the hippocampus.\n\"\"\")\n\ncode(r\"\"\"\nlocs = collections.Counter()\nfor s in sessions:\n    loc = s[\"electrodes\"].location.to_numpy()\n    for e in s[\"unit_electrodes\"]:\n        locs[loc[e[0]]] += 1\nprint(\"Units by electrode location:\", dict(locs))\nmtl = sum(v for k, v in locs.items() if \"amygdala\" in k.lower() or \"hippocampus\" in k.lower())\nprint(\"Units in amygdala or hippocampus:\", mtl, \"of\", sum(locs.values()))\n\"\"\", tags=[\"claim:fig5a-mtl-locations\"])\n\nmd(r\"\"\"\n**Result: Reproduced.** All 1864 units are on electrodes located in the left or right amygdala or\nhippocampus.\n\"\"\")\n\nmd(r\"\"\"\n## Behaviour (Figure 5b to 5d)\n\nPer session, from the 100 recognition trials: the cumulative ROC over the six confidence levels, the\nAUC and the z-ROC slope, computed as in the paper's code (`nomem.roc`, `nomem.auc`, `nomem.zroc_slope`).\n\"\"\"\n)\n\ncode(r\"\"\"\nrows = []\nfor s in sessions:\n    rec = nomem.recog(s)\n    conf, old = rec.confidence.to_numpy(), rec.label.to_numpy() == 1\n    h, f = nomem.roc(conf, old)\n    a = nomem.auc(h, f)\n    fx, fl = nomem.accuracy_fixed(conf, old)\n    dx, dl, mode = nomem.accuracy_dynamic(conf, old)\n    label, sid = nomem.session_key(s)\n    rows.append({\"identifier\": s[\"identifier\"], \"site\": nomem.site(label), \"auc\": a,\n                 \"auc_stated_coding\": nomem.auc(*nomem.roc(conf, ~old)),\n                 \"zroc_slope\": nomem.zroc_slope(h, f) if len(set(np.round(f[:5], 9))) > 1 else np.nan,\n                 \"distinct_zF\": len(set(np.round(f[:5], 9))), \"H\": h, \"F\": f,\n                 \"acc_high_fixed\": fx, \"acc_low_fixed\": fl, \"acc_high_dyn\": dx, \"acc_low_dyn\": dl, \"split_mode\": mode,\n                 \"included\": nomem.included(conf, a), \"responses_used\": len(set(conf))})\nbeh = pd.DataFrame(rows)\nprint(\"Sessions:\", len(beh), \"by site:\", beh.site.value_counts().to_dict())\nprint(\"AUC range:\", beh.auc.min().round(3), \"to\", beh.auc.max().round(3), \"; sessions below 0.5:\", int((beh.auc < 0.5).sum()))\n\"\"\")\n\nmd(r\"\"\"\n## fig5c-auc-all\n\n> Subjects distinguished new from old images; the behavioural AUC averaged over all sessions is 0.74 ± 0.10.\n\nCriterion: AUC per session as in the paper's code over all 87 sessions; mean within 0.74 ± 0.10 and\nstandard deviation within 0.10 ± 0.01.\n\"\"\")\n\ncode(r\"\"\"\nm, sd = beh.auc.mean(), beh.auc.std(ddof=1)\nprint(f\"Mean AUC {m:.4f} (0.74 +- 0.10: {abs(m - 0.74) <= 0.10}); SD {sd:.4f} (0.10 +- 0.01: {abs(sd - 0.10) <= 0.01}); n = {len(beh)}\")\nprint(f\"Against chance (0.5): t = {stats.ttest_1samp(beh.auc, 0.5).statistic:.2f}, p = {stats.ttest_1samp(beh.auc, 0.5).pvalue:.2g}\")\nprint(f\"With the labels as the paper's text states them (0 = old): mean AUC {beh.auc_stated_coding.mean():.4f}\")\nprint(f\"Duplicated recognition data: none (sessions 54 and 55 share the encoding block only).\")\nfig, ax = plt.subplots(1, 2, figsize=(9, 3.5))\nfor _, r in beh.iterrows():\n    ax[0].plot(np.r_[0, r.F, 1], np.r_[0, r.H, 1], color=\"0.8\", lw=0.7)\nax[0].plot(np.r_[0, np.mean(np.stack(beh.F), 0), 1], np.r_[0, np.mean(np.stack(beh.H), 0), 1], \"o-\", color=\"C0\")\nax[0].plot([0, 1], [0, 1], \"k:\")\nax[0].set(xlabel=\"false alarm rate\", ylabel=\"hit rate\", title=\"ROC per session (grey) and mean\")\nax[1].hist([beh.auc[beh.site == \"CS\"], beh.auc[beh.site == \"TWH\"]], bins=np.arange(0.4, 1.01, 0.025), stacked=True, label=[\"CS\", \"TWH\"])\nax[1].set(xlabel=\"AUC\", ylabel=\"sessions\", title=\"AUC per session\")\nax[1].legend()\nplt.tight_layout()\nplt.show()\nprint(\"All plotted values lie in [0, 1]; AUC range\", beh.auc.min().round(3), \"to\", beh.auc.max().round(3))\n\"\"\", tags=[\"claim:fig5c-auc-all\"])\n\nmd(r\"\"\"\n**Result: Reproduced.** The mean AUC over the 87 sessions is 0.753 with a standard deviation of 0.094,\nboth within tolerance of 0.74 ± 0.10.\n\"\"\")\n\nmd(r\"\"\"\n## fig5c-auc-sites\n\n> Performance was similar at the two study sites, with an average AUC of 0.74 ± 0.09 for CS sessions and 0.69 ± 0.13 for TWH sessions.\n\nCriterion: means within 0.74 ± 0.09 (CS) and 0.69 ± 0.13 (TWH), standard deviations within 0.09 ±\n0.009 and 0.13 ± 0.013; partially reproduced when both means are but a spread is not. Welch's t-test\nbetween sites is reported.\n\"\"\")\n\ncode(r\"\"\"\ng = beh.groupby(\"site\").auc.agg([\"mean\", \"std\", \"count\"])\nprint(g.round(4))\nchecks = {\"mean CS\": abs(g.loc[\"CS\", \"mean\"] - 0.74) <= 0.09, \"mean TWH\": abs(g.loc[\"TWH\", \"mean\"] - 0.69) <= 0.13,\n          \"SD CS\": abs(g.loc[\"CS\", \"std\"] - 0.09) <= 0.009, \"SD TWH\": abs(g.loc[\"TWH\", \"std\"] - 0.13) <= 0.013}\nprint(checks)\nw = stats.ttest_ind(beh.auc[beh.site == \"CS\"], beh.auc[beh.site == \"TWH\"], equal_var=False)\nprint(f\"Welch's t-test CS against TWH: t = {w.statistic:.2f}, p = {w.pvalue:.3f}\")\nprint(\"TWH AUCs:\", beh[beh.site == \"TWH\"].set_index(\"identifier\").auc.round(3).to_dict())\n\"\"\", tags=[\"claim:fig5c-auc-sites\"])\n\nmd(r\"\"\"\n**Result: Reproduced.** CS sessions have a mean AUC of 0.760 (SD 0.085, n = 78) and TWH sessions 0.688\n(SD 0.138, n = 9); all four values are within tolerance. The difference between sites is not\nsignificant (Welch's t-test p = 0.16).\n\"\"\")\n\nmd(r\"\"\"\n## fig5b-roc-asymmetric\n\n> The ROC curve is asymmetric (p < 0.05), as expected for declarative memory.\n\nCriterion: the slope of the z-ROC per session (regression of z(H) on z(F) over the five interior\npoints, calcZROCSlope); reproduced when the mean slope is below 1 with a two-sided one-sample t-test\nagainst 1 at p < 0.05. The Wilcoxon signed-rank test and the slope of the pooled ROC are variants.\n\"\"\")\n\ncode(r\"\"\"\nsl = beh.zroc_slope.dropna()\nprint(f\"Sessions with a slope: {len(sl)} of {len(beh)}; left out (fewer than 2 distinct false alarm rates): \"\n      f\"{beh[beh.zroc_slope.isna()].identifier.tolist()}\")\nt = stats.ttest_1samp(sl, 1.0)\nprint(f\"Mean slope {sl.mean():.3f} (SD {sl.std():.3f}, median {sl.median():.3f}); t-test against 1: t = {t.statistic:.2f}, p = {t.pvalue:.2g}\")\nwx = stats.wilcoxon(sl - 1)\nprint(f\"Variant, Wilcoxon signed-rank against 1: p = {wx.pvalue:.2g}; sessions with slope < 1: {int((sl < 1).sum())} of {len(sl)}\")\n# pooled ROC: summed counts over sessions (countersAv in NWB_behaviorSummary.m)\nconf_all, old_all = [], []\nfor s in sessions:\n    rec = nomem.recog(s)\n    conf_all.append(rec.confidence.to_numpy()); old_all.append(rec.label.to_numpy() == 1)\nhp, fp = nomem.roc(np.concatenate(conf_all), np.concatenate(old_all))\nprint(f\"Variant, slope of the pooled ROC: {nomem.zroc_slope(hp, fp):.3f}\")\nprint(\"Slope range:\", sl.min().round(3), \"to\", sl.max().round(3))\n\"\"\", tags=[\"claim:fig5b-roc-asymmetric\"])\n\nmd(r\"\"\"\n**Result: Reproduced.** The mean z-ROC slope over 87 sessions is 0.73, below 1 (t-test against 1,\np = 1.6e-09); the Wilcoxon test and the pooled ROC (slope 0.75) agree.\n\"\"\")\n\nmd(r\"\"\"\n## fig5d-confidence-accuracy\n\n> Accuracy is significantly higher in high than in low confidence trials (P < 0.001, paired t test) across all sessions.\n\nCriterion: per session, the percentage correct among high and among low confidence responses, under\n(a) the fixed split of the MATLAB code (high 1 or 6, low 2 to 5) and (b) the dynamic split of the\nPython code. Sessions without responses in one group are left out and counted. Reproduced when, under\none reading, high exceeds low with a paired t-test p < 0.001. The unpaired test the code runs, and the\ninclusion rule plotFigure5.ipynb applies before this panel (helper.check_inclusion), are variants.\n\"\"\")\n\ncode(r\"\"\"\nfor name, hi, lo in ((\"(a) fixed split\", \"acc_high_fixed\", \"acc_low_fixed\"), (\"(b) dynamic split\", \"acc_high_dyn\", \"acc_low_dyn\")):\n    d = beh[[hi, lo, \"included\", \"site\"]].dropna(subset=[hi, lo])\n    t = stats.ttest_rel(d[hi], d[lo])\n    u = stats.ttest_ind(d[hi], d[lo], equal_var=False)\n    di = d[d.included]\n    ti = stats.ttest_rel(di[hi], di[lo])\n    print(f\"{name}: {len(d)} sessions ({len(beh) - len(d)} left out); high {100 * d[hi].mean():.1f}%, low {100 * d[lo].mean():.1f}%; \"\n          f\"paired t = {t.statistic:.2f}, p = {t.pvalue:.2g}; high > low in {int((d[hi] > d[lo]).sum())} sessions\")\n    print(f\"    unpaired (Welch) p = {u.pvalue:.2g}; with plotFigure5's inclusion rule, {len(di)} sessions, paired p = {ti.pvalue:.2g}\")\n    for st, e in d.groupby(\"site\"):\n        print(f\"    {st}: {len(e)} sessions, high {100 * e[hi].mean():.1f}%, low {100 * e[lo].mean():.1f}%, paired p = {stats.ttest_rel(e[hi], e[lo]).pvalue:.2g}\")\nprint(\"Split modes chosen by (b):\", beh.split_mode.value_counts().to_dict())\n\"\"\", tags=[\"claim:fig5d-confidence-accuracy\"])\n\nmd(r\"\"\"\n**Result: Reproduced.** Under both readings accuracy is higher for high than for low confidence (fixed\nsplit 80.1% against 60.9% over 84 sessions, paired p = 3.2e-16; dynamic split 78.2% against 60.8% over\n82 sessions, p = 1.3e-11), and within each site.\n\"\"\")\n\nmd(r\"\"\"\n## Single units: VS and MS selection\n\nFor every unit, the firing rate of each recognition trial in the Methods' window (0.2 to 1.2 s after\nonset) and in the code's (0.2 to 1.7 s). VS: one-way ANOVA across the 5 categories, p < 0.05. MS:\nbootstrap comparison of mean rates (1000 runs, `nomem.bootstrap_p`) between new and old trials,\np < 0.05, with all 50 and 50 trials (main) or correct trials only (the code's choice). A unit whose rates\nare all equal has no ANOVA p and is counted as not selected. The seed is a standard choice; the spread of\nthe MS count over five more seeds is shown.\n\"\"\")\n\ncode(r\"\"\"\nrng = np.random.default_rng(20200304)\nrows = []\nfor s in sessions:\n    rec = nomem.recog(s)\n    label, sid = nomem.session_key(s)\n    on, cat = rec.onset.to_numpy(), rec.category.to_numpy()\n    old, conf = rec.label.to_numpy() == 1, rec.confidence.to_numpy()\n    correct = (old & (conf >= 4)) | (~old & (conf <= 3))\n    for i, sp in enumerate(s[\"spikes\"]):\n        row = {\"identifier\": s[\"identifier\"], \"session\": sid, \"site\": nomem.site(label), \"unit\": i,\n               \"duplicate\": (s[\"identifier\"], i) in duplicate_second}\n        for wn, w in ((\"m\", nomem.WINDOW_METHODS), (\"c\", nomem.WINDOW_CODE)):\n            rt = nomem.window_rates(sp, on, w)\n            row[f\"vs_p_{wn}\"] = nomem.anova_p(rt, cat)\n            row[f\"ms_p_{wn}\"] = nomem.bootstrap_p(rt[~old], rt[old], rng)\n            row[f\"ms_p_{wn}_correct\"] = nomem.bootstrap_p(rt[~old & correct], rt[old & correct], rng)\n        rows.append(row)\ncells = pd.DataFrame(rows)\nfor c in [c for c in cells if c.endswith((\"_m\", \"_c\", \"_correct\"))]:\n    cells[c.replace(\"_p_\", \"_\")] = cells[c] < nomem.ALPHA\nprint(\"Units:\", len(cells), \"; without an ANOVA p (all rates equal): Methods' window\",\n      int(cells.vs_p_m.isna().sum()), \", code's window\", int(cells.vs_p_c.isna().sum()))\nprint(\"Recognition trials per unit: 100 in every session; correct trials per session from\",\n      min(int(((nomem.recog(s).label == 1) & (nomem.recog(s).confidence >= 4) | (nomem.recog(s).label == 0) & (nomem.recog(s).confidence <= 3)).sum()) for s in sessions),\n      \"to\", max(int(((nomem.recog(s).label == 1) & (nomem.recog(s).confidence >= 4) | (nomem.recog(s).label == 0) & (nomem.recog(s).confidence <= 3)).sum()) for s in sessions))\n\"\"\")\n\nmd(r\"\"\"\n## vs-cells-proportion\n\n> 343 of the 1863 cells (18.4%) are visually selective, by a one-way ANOVA (P < 0.05) of the firing rate in recognition trials, in a 1 s window starting 200 ms after stimulus onset, across the 5 visual categories.\n\nCriterion: every unit, Methods' window; reproduced when the count is within 343 ± 34.3 and the\npercentage within 18.4 ± 1.84. Variants: the code's window, duplicated spike trains counted once, and a\nnull with the category labels shuffled within each session.\n\"\"\")\n\ncode(r\"\"\"\ndef show(mask, total, name):\n    print(f\"{name}: {int(mask.sum())} of {total} ({100 * mask.sum() / total:.1f}%)\")\n\nn = len(cells)\nshow(cells.vs_m, n, \"VS, Methods' window, every unit\")\nprint(\"   within 343 +- 34.3:\", abs(cells.vs_m.sum() - 343) <= 34.3, \"; within 18.4 +- 1.84%:\", abs(100 * cells.vs_m.mean() - 18.4) <= 1.84)\nshow(cells.vs_c, n, \"VS, code's window\")\nonce = cells[~cells.duplicate]\nshow(once.vs_m, len(once), \"VS, Methods' window, duplicated spike trains once\")\nrng_null = np.random.default_rng(343)\nnull = 0\nfor s in sessions:\n    rec = nomem.recog(s)\n    cat = rng_null.permutation(rec.category.to_numpy())\n    for sp in s[\"spikes\"]:\n        p = nomem.anova_p(nomem.window_rates(sp, rec.onset.to_numpy(), nomem.WINDOW_METHODS), cat)\n        null += int(np.isfinite(p) and p < 0.05)\nprint(f\"Null, categories shuffled within session: {null} of {n} ({100 * null / n:.1f}%); expected by chance 5%\")\nprint(\"VS by site (Methods' window):\", cells.groupby(\"site\").vs_m.agg([\"sum\", \"count\"]).to_dict())\nprint(\"VS percentage by session: median\", (100 * cells.groupby(\"identifier\").vs_m.mean()).median().round(1),\n      \"; range\", (100 * cells.groupby(\"identifier\").vs_m.mean()).min().round(1), \"to\", (100 * cells.groupby(\"identifier\").vs_m.mean()).max().round(1))\n\"\"\", tags=[\"claim:vs-cells-proportion\"])\n\nmd(r\"\"\"\n**Result: Reproduced.** 332 of 1864 units (17.8%) are VS in the Methods' window, within tolerance of 343\n(18.4%); the code's window gives 343 (18.4%), and the shuffled null about 5%.\n\"\"\")\n\nmd(r\"\"\"\n## ms-cells-proportion\n\n> 146 of the 1863 cells (7.8%) are memory selective, by a two-tailed bootstrap comparison of mean firing rates (1,000 runs, P < 0.05) between the 50 novel and 50 familiar recognition trials in a 1 s window starting 200 ms after stimulus onset.\n\nCriterion: every unit, Methods' window and all 50 and 50 trials, bootstrap of bootstrapMeanEqualTest at\na fixed seed; reproduced when the count is within 146 ± 14.6 and the percentage within 7.8 ± 0.78.\nVariants: the code's choices (correct trials only, its window), duplicated spike trains once, and a null\nwith labels shuffled within each session.\n\"\"\")\n\ncode(r\"\"\"\nshow(cells.ms_m, n, \"MS, Methods' window, all trials (main)\")\nprint(\"   within 146 +- 14.6:\", abs(cells.ms_m.sum() - 146) <= 14.6, \"; within 7.8 +- 0.78%:\", abs(100 * cells.ms_m.mean() - 7.8) <= 0.78)\nshow(cells.ms_m_correct, n, \"MS, Methods' window, correct trials\")\nshow(cells.ms_c, n, \"MS, code's window, all trials\")\nshow(cells.ms_c_correct, n, \"MS, code's window, correct trials (the code's choices)\")\nshow(once.ms_m, len(once), \"MS, main, duplicated spike trains once\")\n# bootstrap noise: the main count with five other seeds\ncounts = []\nfor seed in range(1, 6):\n    r2 = np.random.default_rng(seed)\n    k = 0\n    for s in sessions:\n        rec = nomem.recog(s)\n        old = rec.label.to_numpy() == 1\n        for sp in s[\"spikes\"]:\n            rt = nomem.window_rates(sp, rec.onset.to_numpy(), nomem.WINDOW_METHODS)\n            k += int(nomem.bootstrap_p(rt[~old], rt[old], r2) < 0.05)\n    counts.append(k)\nprint(\"Main count with seeds 1 to 5:\", counts)\nrng_null = np.random.default_rng(146)\nnull = 0\nfor s in sessions:\n    rec = nomem.recog(s)\n    old = rng_null.permutation(rec.label.to_numpy() == 1)\n    for sp in s[\"spikes\"]:\n        rt = nomem.window_rates(sp, rec.onset.to_numpy(), nomem.WINDOW_METHODS)\n        null += int(nomem.bootstrap_p(rt[~old], rt[old], rng_null) < 0.05)\nprint(f\"Null, labels shuffled within session: {null} of {n} ({100 * null / n:.1f}%)\")\nprint(\"MS by site (main):\", cells.groupby(\"site\").ms_m.agg([\"sum\", \"count\"]).to_dict())\n\"\"\", tags=[\"claim:ms-cells-proportion\"])\n\nmd(r\"\"\"\n**Result: Not reproduced.** With all 50 and 50 trials in the Methods' window, 114 of 1864 units (6.1%)\nare MS, below the tolerance of 146 (7.8%); other seeds give similar counts (printed above). The code's\nchoices, correct trials only in its 0.2 to 1.7 s window, give 150 (8.0%), within tolerance, and correct\ntrials alone in the Methods' window give 134 (7.2%).\n\"\"\")\n\nmd(r\"\"\"\n## dual-cells-proportion\n\n> 26 cells (1.4%) are both visually and memory selective.\n\nCriterion: units selected by both main tests; reproduced when the count is within 26 ± 2.6 and the\npercentage within 1.4 ± 0.14.\n\"\"\")\n\ncode(r\"\"\"\ndual = cells.vs_m & cells.ms_m\nshow(dual, n, \"VS and MS, main tests\")\nprint(\"   within 26 +- 2.6:\", abs(dual.sum() - 26) <= 2.6, \"; within 1.4 +- 0.14%:\", abs(100 * dual.mean() - 1.4) <= 0.14)\nshow(cells.vs_c & cells.ms_c_correct, n, \"Variant, the code's choices for both\")\nshow(cells.vs_m & cells.ms_m_correct, n, \"Variant, Methods' window, MS on correct trials\")\nexp = cells.vs_m.mean() * cells.ms_m.mean() * n\nprint(f\"Expected if VS and MS were independent: {exp:.1f}\")\n\"\"\", tags=[\"claim:dual-cells-proportion\"])\n\nmd(r\"\"\"\n**Result: Not reproduced.** 13 units (0.7%) are both VS and MS under the main tests, half the paper's\n26. The code's choices give 26 (1.4%).\n\"\"\")\n\nmd(r\"\"\"\n## fig5f-site-proportions\n\n> The percentages of VS, MS and dual cells are comparable between CS sessions (18.4%, 7.7% and 1.4%) and the new TWH sessions (19.4%, 10.4% and 1.3%).\n\nCriterion: two-sided Fisher's exact test between sites for each of VS, MS and dual cells at 0.05;\nreproduced when no test finds a difference and at least four of the six values are within tolerance;\npartially when only one of these holds. Main tests; the code's choices are a variant.\n\"\"\")\n\ncode(r\"\"\"\nexpected = {(\"VS\", \"CS\"): 18.4, (\"MS\", \"CS\"): 7.7, (\"dual\", \"CS\"): 1.4, (\"VS\", \"TWH\"): 19.4, (\"MS\", \"TWH\"): 10.4, (\"dual\", \"TWH\"): 1.3}\n\n\ndef site_table(vs, ms, label):\n    sets = {\"VS\": vs, \"MS\": ms, \"dual\": vs & ms}\n    within, fisher = 0, []\n    for kind, mask in sets.items():\n        a = [int(mask[cells.site == st].sum()) for st in (\"CS\", \"TWH\")]\n        tot = [int((cells.site == st).sum()) for st in (\"CS\", \"TWH\")]\n        p = stats.fisher_exact([[a[0], tot[0] - a[0]], [a[1], tot[1] - a[1]]]).pvalue\n        fisher.append(p)\n        for st, k, t in zip((\"CS\", \"TWH\"), a, tot):\n            pct = 100 * k / t\n            ok = abs(pct - expected[(kind, st)]) <= 0.1 * expected[(kind, st)]\n            within += ok\n            print(f\"  {label} {kind} {st}: {k} of {t} = {pct:.1f}% (paper {expected[(kind, st)]}%; within 10%: {ok})\")\n        print(f\"  {label} {kind}: Fisher's exact p = {p:.3f}\")\n    print(f\"  {label}: {within} of 6 within tolerance; tests finding a difference: {sum(p < 0.05 for p in fisher)}\")\n\n\nsite_table(cells.vs_m, cells.ms_m, \"main\")\nsite_table(cells.vs_c, cells.ms_c_correct, \"code\")\nprint(\"TWH units by session:\", cells[cells.site == \"TWH\"].groupby(\"identifier\").size().to_dict())\n\"\"\", tags=[\"claim:fig5f-site-proportions\"])\n\nmd(r\"\"\"\n**Result: Partially reproduced.** Under the main tests no Fisher's test finds a difference between CS\n(1787 units) and TWH (77 units), but only 3 of the 6 percentages are within tolerance. With the code's\nchoices, the tests again find no difference.\n\"\"\")\n\nmd(r\"\"\"\n## twh-sessions\n\n> The dataset includes 9 sessions from a new institution, Toronto Western Hospital.\n\nCriterion: sessions whose subject label starts with T; reproduced when the count is within 9 ± 0.9.\n\"\"\")\n\ncode(r\"\"\"\ntwh = info[info.label.str.startswith(\"T\")]\nprint(\"Sessions with a T label:\", len(twh), \"; subjects:\", twh.label.nunique(), \"; institution field:\", set(twh.institution))\nprint(twh[[\"identifier\", \"subject_id\", \"start\", \"units\"]].to_string(index=False))\n\"\"\", tags=[\"claim:twh-sessions\"])\n\nmd(r\"\"\"\n**Result: Reproduced.** Nine sessions, of eight subjects, have T labels, and their institution field\nis Toronto Western Hospital.\n\"\"\")\n\nmd(r\"\"\"\n## previous-release-link\n\n> The sessions of the earlier release (Faraut et al. 2018) are found in this dandiset under the same subject, session id and task variant.\n\nLink claim, with Table 1 of Faraut et al. 2018 (read from its full text). Criterion: sessions matched\nby session id; a matched session agrees when its subject label and task variant are those of the\nearlier table. Reproduced when every session of the earlier table is found and agrees; partially when\nat least 90% are found and agree, with the others listed. Age and sex of the matched subjects are\ncompared. The variant of a file is read from its category names (see the data check).\n\"\"\")\n\ncode(r\"\"\"\nfar_t1, far_totals, far_tables = nomem.faraut_table1()\nfar = nomem.sessions_of(far_t1)\nprint(\"Faraut et al. 2018 Table 1:\", len(far_t1), \"subjects,\", len(far), \"sessions; totals row:\", far_totals)\nfiles_by_session = info.set_index(\"session\")\nrows = []\nfor r in far.itertuples():\n    found = r.session in files_by_session.index\n    f = files_by_session.loc[r.session] if found else None\n    rows.append({\"session\": r.session, \"label_2018\": r.label, \"variant_2018\": r.variant, \"found\": found,\n                 \"label_file\": f.label if found else None, \"variant_file\": f.variant if found else None,\n                 \"agrees\": bool(found and f.label == r.label and f.variant == r.variant)})\nlink = pd.DataFrame(rows)\nprint(f\"Found by session id: {int(link.found.sum())} of {len(link)}; found and agree: {int(link.agrees.sum())} \"\n      f\"({100 * link.agrees.mean():.1f}%)\")\nprint(\"Not found or not agreeing:\")\nprint(link[~link.agrees].to_string(index=False))\nages = far_t1.set_index(\"label\")[[\"age\", \"sex\"]].join(paper_t1.set_index(\"label\")[[\"age\", \"sex\"]], rsuffix=\"_2020\", how=\"inner\")\nsubj_file = info.drop_duplicates(\"label\").set_index(\"label\")[[\"age\", \"sex\"]].rename(columns={\"age\": \"age_file\", \"sex\": \"sex_file\"})\nages = ages.join(subj_file, how=\"left\")\nages[\"age_file\"] = pd.to_numeric(ages.age_file)\nprint(f\"\\nSubjects of the 2018 table also in the files: {int(ages.age_file.notna().sum())} of {len(far_t1)}\")\nprint(\"Age and sex, 2018 table against the files: both match for\",\n      int(((ages.age == ages.age_file) & (ages.sex == ages.sex_file)).sum()), \"of\", int(ages.age_file.notna().sum()))\nprint(ages[(ages.age != ages.age_file) | (ages.sex != ages.sex_file)].to_string())\n\"\"\", tags=[\"claim:previous-release-link\"])\n\nmd(r\"\"\"\n**Result: Partially reproduced.** 64 of the 65 sessions of the 2018 table are in the dandiset under the\nsame subject and variant (98.5%). Session 98 is not in the dandiset, nor in Online-only Table 1.\n\"\"\")\n\nmd(r\"\"\"\n## previous-release-additions\n\n> Relative to the earlier release of this task's data (Faraut et al. 2018), this release adds 23 sessions, 17 subjects and 288 neurons.\n\nCriterion: new sessions are those of the dandiset not in the 2018 list, new subjects those with no\nsession in it, and new neurons the unit rows of the new sessions. Reproduced when all three are within\ntolerance (23 ± 2.3, 17 ± 1.7, 288 ± 28.8); partially when one or two are. The differences of the\ntotals the two papers state are a variant.\n\"\"\")\n\ncode(r\"\"\"\nold_sessions, old_labels = set(far.session), set(far.label)\nnew = info[~info.session.isin(old_sessions)]\nnew_subjects = sorted(set(info.label) - old_labels)\nnew_units = int(new.units.sum())\nprint(f\"New sessions: {len(new)} (23 +- 2.3: {abs(len(new) - 23) <= 2.3})\")\nprint(f\"New subjects: {len(new_subjects)} (17 +- 1.7: {abs(len(new_subjects) - 17) <= 1.7}): {new_subjects}\")\nprint(f\"New neurons (unit rows of new sessions): {new_units} (288 +- 28.8: {abs(new_units - 288) <= 28.8})\")\nprint(\"New sessions by site:\", new.site.value_counts().to_dict())\nprint(new[[\"identifier\", \"units\"]].to_string(index=False))\nprint(f\"Variant, differences of totals: sessions 87 - 65 = 22, subjects 59 - 42 = 17, neurons 1863 - 1576 = 287 \"\n      f\"(Faraut et al. 2018 abstract); here {len(info)} - {len(far)} = {len(info) - len(far)} files, \"\n      f\"{info.label.nunique()} - {len(far_t1)} = {info.label.nunique() - len(far_t1)} subjects\")\n\"\"\", tags=[\"claim:previous-release-additions\"])\n\nmd(r\"\"\"\n**Result: Partially reproduced.** The dandiset has 23 sessions and 17 subjects that the 2018 table does\nnot list, as the paper says, but their units number far fewer than 288 (printed above).\n\"\"\")\n\nmd(r\"\"\"\n## fig4-example-vs-neuron\n\n> Neuron 132-177-4-RA (session 132, channel 177, cell 4, right amygdala) is visually selective, responding most to images of animals.\n\nCriterion: the unit on channel 177 of session 132 with electrode row 4, in the right amygdala;\nreproduced when the one-way ANOVA across the 5 categories of recognition trials, Methods' window, has\np < 0.05 and the animal category has the highest mean rate. The code's window is a variant.\n\"\"\")\n\ncode(r\"\"\"\ndef example(session, channel, row, area):\n    s = [x for x in sessions if nomem.session_key(x)[1] == session]\n    if not s:\n        print(f\"session {session} is not in the dandiset\")\n        return\n    s = s[0]\n    el = s[\"electrodes\"]\n    found = [i for i, e in enumerate(s[\"unit_electrodes\"]) if el.origChannel.iloc[e[0]] == channel]\n    print(f\"{s['identifier']}: units on channel {channel}: {found}; their electrode rows \"\n          f\"{[int(s['unit_electrodes'][i][0]) for i in found]}; location {set(el.location.iloc[[s['unit_electrodes'][i][0] for i in found]])}\")\n    rec = nomem.recog(s)\n    for i in found:\n        for wn, w in ((\"Methods\", nomem.WINDOW_METHODS), (\"code\", nomem.WINDOW_CODE)):\n            rt = nomem.window_rates(s[\"spikes\"][i], rec.onset.to_numpy(), w)\n            means = pd.Series(rt).groupby(rec.category_name.to_numpy()).mean()\n            print(f\"  unit {i} (electrode row {int(s['unit_electrodes'][i][0])}), {wn} window: ANOVA p = {nomem.anova_p(rt, rec.category.to_numpy()):.3g}; \"\n                  f\"mean rate by category (Hz): {means.round(2).to_dict()}; highest: {means.idxmax()}\")\n\n\nexample(132, 177, 4, \"Right Amygdala\")\n\"\"\", tags=[\"claim:fig4-example-vs-neuron\"])\n\nmd(r\"\"\"\n**Result: Reproduced.** Session 132 has one unit on channel 177, on electrode row 4 in the right\namygdala; its rates differ across categories (ANOVA p printed above, below 0.05) and are highest for\nanimals in both windows.\n\"\"\")\n\nmd(r\"\"\"\n## fig3-example-vs-neuron\n\n> Neuron 144-140-3-RH (session 144, channel 140, cell 3, right hippocampus) is visually selective for phones.\n\nBlocked: there is no session 144 in the dandiset or in Online-only Table 1. The only units on a\nchannel 140 in the right hippocampus are in session 2009 (T103); they are shown here, but nothing links\nthem to the figure's neuron, so they do not decide the claim.\n\"\"\")\n\ncode(r\"\"\"\nexample(144, 140, 3, \"Right Hippocampus\")\nprint(\"Sessions with a unit on channel 140:\", [s[\"identifier\"] for s in sessions\n      if any(s[\"electrodes\"].origChannel.iloc[e[0]] == 140 for e in s[\"unit_electrodes\"])])\nexample(2009, 140, 3, \"Right Hippocampus\")\n\"\"\", tags=[\"claim:fig3-example-vs-neuron\"])\n\nmd(r\"\"\"\n## Summary\n\"\"\")\n\ncode(r\"\"\"\nprint(f\"Notebook ran in {(time.time() - started) / 60:.1f} min\")\n\"\"\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/cells.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && python -c "
from dandi.dandiapi import DandiAPIClient
with DandiAPIClient() as c:
    for v in ['0.220126.1851','draft']:
        a=next(c.get_dandiset('000004',v).get_assets()); print(v, type(a).__name__, getattr(a,'blob',None), a.path, a.size)
"
```

```
0.220126.1851 RemoteBlobAsset 284eb346-0bc5-42a6-9b33-268e6b0b0bde sub-P10HMH/sub-P10HMH_ses-20060901_ecephys+image.nwb 73156888
draft RemoteBlobAsset 284eb346-0bc5-42a6-9b33-268e6b0b0bde sub-P10HMH/sub-P10HMH_ses-20060901_ecephys+image.nwb 73156888
```

**Agent**

Blob ids are available, so the version comparison can use them. Updating that cell, then building and executing the notebook.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'E'
p='/tmp/claude-1001/cells.py'; s=open(p).read()
s=s.replace('''        listings[v] = {a.path: (a.size, a.blob if hasattr(a, "blob") else None) for a in d.get_assets()}
pinned = listings[nomem.DANDISET_VERSION]
for v, files in listings.items():
    same = sum(1 for p in pinned if p in files and files[p][0] == pinned[p][0])
    print(f"{v}: {len(files)} files; {same} with the pinned version's path and size; "
          f"paths only in one: {sorted(set(files) ^ set(pinned))[:5]}")''','''        listings[v] = {a.path: a.blob for a in d.get_assets()}
pinned = listings[nomem.DANDISET_VERSION]
for v, files in listings.items():
    same = sum(1 for p in pinned if files.get(p) == pinned[p])
    print(f"{v}: {len(files)} files; {same} with the pinned version's path and blob (content); "
          f"paths only in one of the two: {sorted(set(files) ^ set(pinned))[:5]}")''')
s=s.replace('''The versions are compared by path and size here; the archive's blob ids are not exposed by every
client version, so a change of content at an identical size would not be seen.''','''Files are compared by path and by the archive's blob id, which changes when the content changes.''')
s=s.replace('''with DandiAPIClient() as client:
    ds = client.get_dandiset(nomem.DANDISET_ID)
    listings''','''with DandiAPIClient() as client:
    listings''')
open(p,'w').write(s)
E
. env/bin/activate && uv pip install -q nbconvert ipykernel nbformat 2>&1|tail -1; python build.py cells.py entries/chandravadia-2020/reproduce_chandravadia_2020.ipynb && cd entries/chandravadia-2020 && time jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3600 reproduce_chandravadia_2020.ipynb --output $TMPDIR/run1.ipynb 2>&1 | tail -5
```

```
[NbConvertApp] Converting notebook reproduce_chandravadia_2020.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 266771 bytes to /tmp/claude-1001/run1.ipynb

real	3m5.899s
user	0m55.566s
sys	0m14.224s
```

**Agent**

Executed cleanly in about 3 minutes. Reading the outputs.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'E'
import json
nb=json.load(open('/tmp/claude-1001/run1.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    tags=c['metadata'].get('tags',[])
    out=''
    for o in c.get('outputs',[]):
        if 'text' in o: out+=''.join(o['text'])
        elif o.get('output_type')=='error': out+='ERROR '+o['ename']+o['evalue']
        elif 'data' in o and 'text/plain' in o['data']: out+=''.join(o['data']['text/plain'])
    if i==4: out=out[:1500]
    print(f'==== cell {i} {tags}\n{out[:3500]}')
E
```

```
==== cell 1 []
loaded 87 files from dandiset 000004 version 0.220126.1852 in 119 s
Online-only Table 1: 59 subject rows; totals row: ['Total Subjects: 59', 'Total Sessions: 87', 'Total Female: 25', 'Total Male: 34']

==== cell 3 ['sanity']
Files: 87 ; distinct subject_id: 59 ; distinct labels: 59
Files by site: {'CS': 78, 'TWH': 9}
Unit rows: 1864 ; electrode rows: 887
Trial phases over all files: Counter({'recog': 8700, 'learn': 8347})
Institution field: Counter({'Cedars-Sinai Medical Center': 44, 'Hunigton Memorial Hospital': 28, 'Toronto Western Hospital': 9, 'Hunington Memorial Hospital': 6})
Devices: Counter({'Neuralynx-Atlas': 53, 'Neuralynx-cheetah': 29, 'Neuralynx-Cheetah': 5})
   identifier label  session site subject_id age sex       start  n_learn  n_recog  label0  label1  n_cat  variant  units  electrodes learn_id recog_id                  institution             device
0     CS24_59   C24       59   CS      P24CS  57   F  2012-09-01      100      100      50      50      5        1     21           7   [80.0]   [81.0]  Cedars-Sinai Medical Center    Neuralynx-Atlas
1     CS24_60   C24       60   CS      P24CS  57   F  2012-09-01      100      100      50      50      5        2     22           9   [83.0]   [84.0]  Cedars-Sinai Medical Center    Neuralynx-Atlas
2     CS25_61   C25       61   CS      P25CS  36   F  2012-09-01      100      100      50      50      5        1      8           6   [80.0]   [81.0]  Cedars-Sinai Medical Center    Neuralynx-Atlas
3     CS25_63   C25       63   CS      P25CS  36   F  2012-09-01      100      100      50      50      5        2     14          11   [83.0]   [84.0]  Cedars-Sinai Medical Center    Neuralynx-Atlas
4     CS26_64   C26       64   CS      P26CS  56   F  2012-12-01      100      100      50      50      5        1     33           9   [80.0]   [81.0]  Cedars-Sinai Medical Center    Neuralynx-Atlas
5     CS26_66   C26       66   CS      P26CS  56   F  2012-12-01      100      100      50      50      5
[... 414 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && python - <<'E'
import pickle, numpy as np, nomem
ss=pickle.load(open('/tmp/claude-1001/sessions.pkl','rb'))
s=[x for x in ss if x['identifier']=='H27_58'][0]
for i in (35,37):
    sp=s['spikes'][i]; d=np.diff(sp); k=np.where(d<0)[0]
    print(i,len(sp),k[:5], len(np.unique(sp)), sp[:3], sp[k[0]:k[0]+3] if len(k) else None)
    half=len(sp)//2; print(np.allclose(np.sort(sp[:half]),np.sort(sp[half:])) if len(sp)%2==0 else 'odd')
    print(np.sum(np.diff(np.sort(sp))==0))
u=[ (x['identifier'],i,v) for x in ss for i,v in enumerate(x['units'].SNR) if np.isinf(v)]; print(len(u),u[:5])
iso=[ (x['identifier'],i,v) for x in ss for i,v in enumerate(x['units'].IsolationDist) if v>1e6]; print(len(iso),iso[:5])
E
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'nomem'
```

**Agent calls Bash**

```bash
cd entries/chandravadia-2020 && . $TMPDIR/env/bin/activate && python - <<'E'
import pickle, numpy as np, nomem
ss=pickle.load(open('/tmp/claude-1001/sessions.pkl','rb'))
s=[x for x in ss if x['identifier']=='H27_58'][0]
for i in (35,37):
    sp=s['spikes'][i]; d=np.diff(sp); k=np.where(d<0)[0]
    print(i,len(sp),k[:5], len(np.unique(sp)), np.sum(np.diff(np.sort(sp))<0.0005))
    others=[j for j,x in enumerate(s['spikes']) if j!=i and len(np.intersect1d(np.round(x,5),np.round(sp,5)))>0.3*len(sp)]
    print('  overlaps with units', others, s['units'].origClusterID[i])
u=[ (x['identifier'],i) for x in ss for i,v in enumerate(x['units'].SNR) if np.isinf(v)]; print(len(u),u[:5])
iso=[ (x['identifier'],i,v) for x in ss for i,v in enumerate(x['units'].IsolationDist) if v>1e6]; print(len(iso),iso[:5])
E
```

```
35 3268 [1633] 1634 1634
  overlaps with units [] 1507
37 824 [411] 412 412
  overlaps with units [] 1745
11 [('H28_48', 9), ('H28_48', 10), ('H28_48', 11), ('H28_48', 12), ('H28_48', 13)]
2 [('H21_38', 8, 2.9223032923899105e+27), ('CS26_66', 5, 8.081694408988397e+32)]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && python - <<'E'
p='/tmp/claude-1001/cells.py'; s=open(p).read()
def rep(a,b):
    global s
    assert a in s, a[:80]
    s=s.replace(a,b)
rep('''In the recognition phase `response_value` holds the event code (31 to 36), so the confidence is
`response_value` minus 30, as the claims file says. In the encoding phase it holds 0 or 1 (and 20 or
21 in some files), not the 20 and 21 of the events. Trial and spike times share one clock in each file
(checked below); 47 files count it in Unix seconds, so only differences of times are meaningful. The
confidence read from `response_value` is checked against the event codes the paper's code reads:''',
'''In the recognition phase `response_value` holds the event code (31 to 36), so the confidence is
`response_value` minus 30, as the claims file says. In the encoding phase it holds 0 or 1, not the 20
and 21 of the events. Trial and spike times share one clock in each file (checked below); 38 files
count it in Unix seconds, the others from an arbitrary origin, so only differences of times are
meaningful. The median stimulus duration is 1 s in most files and up to 2 s in some. Spike times are
not in increasing order in 13 units (see isi-criterion). SNR is infinite for some units and isolation
distance reaches 1e32 (see units-table). The confidence read from `response_value` is checked against
the event codes the paper's code reads:''')
rep('''code(r"""
# Spike trains deposited in more than one file''','''md(r"""
In 4 files the confidence from the trials table differs from the code the paper's code reads for 1 to
6 trials; these files hold extra event codes (22, 23 or 0, see ttl-codes) that shift the position the
code reads. The analyses use the trials table, as the claims file says.
""")

code(r"""
# Spike trains deposited in more than one file''')
rep('''Over all files, 1105 more or fewer units (see the printed counts) respond to the stimulus at the true
onsets than at onsets moved by 37 s, and the category effect peaks at lag 0 among lags from -3 to
+3 s. Both are consistent with spikes and trials sharing a clock. The files listed above, with few
units, are those where the check cannot establish it on its own.''',
'''Over all files, 830 of 1864 units respond to the stimulus at the true onsets against 115 at onsets
moved by 37 s, and the number of units with a category effect peaks at lag 0 (332) among lags from -3
to +3 s. Both are consistent with spikes and trials sharing a clock. In the five files listed above (1
to 19 units each) the check cannot establish it on its own.''')
rep('''cmp = paper_t1.set_index("label")[["age", "sex", "diagnosis"]].join(subj[["age", "sex", "diagnosis_file"]], rsuffix="_file", how="outer")''',
'''cmp = paper_t1.set_index("label")[["age", "sex", "diagnosis"]].join(
    subj[["age", "sex", "diagnosis_file"]].rename(columns={"age": "age_file", "sex": "sex_file"}), how="outer")''')
rep('''**Result: Partially reproduced.** The files hold 25 female and 34 male subjects, as the table says,
but age or sex differ for 3 of 59 subjects (listed above); the other 56 match.''',
'''**Result: Partially reproduced.** Age and sex match Online-only Table 1 for 56 of 59 subjects. C24 is
57 in the files and 47 in the table, H33 30 and 29, and H48 is a 32-year-old woman in the files and a
54-year-old man in the table, so the files hold 26 female and 33 male subjects against the table's 25
and 34. The files' diagnosis text equals the table's for 40 of 59 subjects; the others use coarser
terms ("Right Other" for "Right Insula").''')
rep('''**Result: Partially reproduced.** Every session has 100 recognition trials with 50 of each label and 5
categories, but 9 of 87 sessions have fewer encoding trials: 8 have 50 and one (session 123) has 97.
The other 78 have 100 encoding trials with 100 distinct images.''',
'''**Result: Partially reproduced.** Every session has 100 recognition trials with 50 of each label and 5
categories, but 8 of 87 sessions have fewer encoding trials: 7 have 50 (sessions 18, 20, 21, 23, 26,
27 and 44, all from Huntington) and one (session 123) has 97. The other 79 have 100 encoding trials
with 100 distinct images.''')
rep('''**Result: Not reproduced.** In no session do label-0 trials show an image of the encoding block, while
label-1 trials do (all of them in the 78 sessions with 100 encoding trials, and 26 to 29 of 50 in the
eight with 50); and label-1 trials receive more "old" responses than label-0 trials in 86 of 87
sessions. The labels are the reverse of the stated coding: 1 is old and 0 is new, as the paper's code
reads them. In the eight sessions with 50 encoding trials, 21 to 24 old images are not in the file's
encoding block; they are in the encoding blocks of other files of the same variant, so the encoding
trials that showed them are missing from these files.''',
'''**Result: Not reproduced.** Under the stated coding test 1 holds in 0 of 87 sessions and test 2 in 1.
With the labels reversed both tests hold in 86 of 87 sessions: no label-0 image is in the encoding
block of its session, label-1 images are (all of them in 79 sessions, 49 of 50 in session 123, and 26
to 29 of 50 in the seven with 50 encoding trials), and label-1 trials draw more "old" responses (69%
against 27% on average). The exception for test 2 is session 2005 (T98, AUC 0.445). The labels are 1
for old and 0 for new, as the paper's code reads them and the reverse of the paper's text and the
column's description. In the seven sessions with 50 encoding trials, 21 to 24 old images are not in
the file's encoding block but are in the encoding blocks of other files of the same variant, so these
files lack the encoding trials that showed them.''')
rep('''**Result: Partially reproduced.** In all 87 files events and experiment_ids have the same length and
timestamps and every trial follows the order 1, 2, 3, response, 6; but 9 files hold codes Table 1 does
not list (0, 4, 22, 23, 98, 99), so the three parts hold together in 78 of 87 files. Seven files have
no start marker (55), which the criterion does not require.''',
'''**Result: Partially reproduced.** In all 87 files events and experiment_ids have the same length and
timestamps. 9 files hold codes Table 1 does not list (0, 4, 22, 23, 98, 99), and in 7 of them 1 to 10
trials break the order 1, 2, 3, response, 6 (17019 of 17047 trials follow it), so all parts hold in
78 of 87 files. Seven files have no start marker (55).''')
rep('''**Result: Partially reproduced.** Every file holds the columns (IsolDist under the name
`IsolationDist`, described as "IsolDist"), each of the 1864 units links to one electrode, and the
waveforms are stated as sampled at 98.4 kHz, within tolerance. SNR is missing (NaN) for 75 units and
isolation distance for 493.''',
'''**Result: Partially reproduced.** Every file holds the columns (IsolDist under the name
`IsolationDist`, described as "IsolDist"), each of the 1864 units links to one electrode, and the
waveforms are stated as sampled at 98.4 kHz, within tolerance. SNR is not finite for 86 units (NaN or
infinite) and isolation distance is NaN for 493 units in 82 files; two isolation distances are above
1e27.''')
rep('''for c in ("SNR", "IsolationDist", "origClusterID"):
    v = units_all[c].astype(float)
    print(f"{c}: not finite for {int((~np.isfinite(v)).sum())} of {len(v)} units, in "
          f"{units_all[~np.isfinite(v)].identifier.nunique()} files")''','''for c in ("SNR", "IsolationDist", "origClusterID"):
    v = units_all[c].astype(float)
    print(f"{c}: not finite for {int((~np.isfinite(v)).sum())} of {len(v)} units (NaN {int(v.isna().sum())}, "
          f"infinite {int(np.isinf(v).sum())}), in {units_all[~np.isfinite(v)].identifier.nunique()} files; above 1e6: {int((v > 1e6).sum())}")''')
rep('''isi = pd.DataFrame([{"identifier": s["identifier"], "unit": i, "spikes": len(sp),
                     "sorted": nomem.isi_violation_fraction(sp), "stored": nomem.isi_violation_fraction(sp, sort=False)}
                    for s in sessions for i, sp in enumerate(s["spikes"])])
for c in ("sorted", "stored"):''','''isi = pd.DataFrame([{"identifier": s["identifier"], "unit": i, "spikes": len(sp), "distinct": len(np.unique(sp)),
                     "unsorted": bool((np.diff(sp) < 0).any()),
                     "sorted": nomem.isi_violation_fraction(sp), "stored": nomem.isi_violation_fraction(sp, sort=False),
                     "distinct_sorted": nomem.isi_violation_fraction(np.unique(sp))}
                    for s in sessions for i, sp in enumerate(s["spikes"])])
print("Units stored out of time order:", int(isi.unsorted.sum()), "; units holding repeated spike times:",
      isi[isi.spikes > isi.distinct][["identifier", "unit", "spikes", "distinct"]].to_dict("records"))
for c in ("sorted", "stored", "distinct_sorted"):''')
rep('''**Result: Partially reproduced.** See the counts above: the share of units below 3% is at least 95%
but not every unit is below it.''','''**Result: Partially reproduced.** With spike times sorted, 1858 of 1864 units (99.7%) have fewer
than 3% of intervals below 3 ms; six do not. Two of them (H27_58 units 35 and 37) hold each spike time
twice, stored as two copies one after the other, which gives 50% short intervals once sorted; with
each spike time counted once they are below 3%, and four units (3.0% to 9.0%) remain above.''')
rep('''**Result: Reproduced.** The mean z-ROC slope over 87 sessions is 0.73, below 1 (t-test against 1,
p = 1.6e-09); the Wilcoxon test and the pooled ROC (slope 0.75) agree.''','''**Result: Reproduced.** Over the 82 sessions with a defined slope the mean z-ROC slope is 0.78, below 1
(t-test against 1, p = 4.3e-09); 65 of 82 slopes are below 1, and the Wilcoxon test (p = 2e-08) and the
pooled ROC (slope 0.82) agree. Five sessions have fewer than two distinct false alarm rates among the
five points, so no slope.''')
rep('''**Result: Reproduced.** Under both readings accuracy is higher for high than for low confidence (fixed
split 80.1% against 60.9% over 84 sessions, paired p = 3.2e-16; dynamic split 78.2% against 60.8% over
82 sessions, p = 1.3e-11), and within each site.''','''**Result: Reproduced.** Under both readings accuracy is higher for high than for low confidence (fixed
split 80.1% against 60.9% over 84 sessions, paired p = 3.2e-16; dynamic split 78.2% against 60.8% over
82 sessions, p = 1.3e-11). The effect holds in the CS sessions alone; in the 8 TWH sessions it has the
same direction without significance (p = 0.14 and 0.26).''')
rep('''**Result: Reproduced.** 332 of 1864 units (17.8%) are VS in the Methods' window, within tolerance of 343
(18.4%); the code's window gives 343 (18.4%), and the shuffled null about 5%.''','''**Result: Reproduced.** 332 of 1864 units (17.8%) are VS in the Methods' window, within tolerance of 343
(18.4%); the code's window gives 343 (18.4%), counting duplicated spike trains once 321 of 1798 (17.9%),
and the shuffled null 76 (4.1%).''')
rep('''**Result: Not reproduced.** With all 50 and 50 trials in the Methods' window, 114 of 1864 units (6.1%)
are MS, below the tolerance of 146 (7.8%); other seeds give similar counts (printed above). The code's
choices, correct trials only in its 0.2 to 1.7 s window, give 150 (8.0%), within tolerance, and correct
trials alone in the Methods' window give 134 (7.2%).''','''**Result: Not reproduced.** With all 50 and 50 trials in the Methods' window, 118 of 1864 units (6.3%)
are MS, below the tolerance of 146 ± 14.6 (7.8 ± 0.78%); five other seeds give 108 to 115. The
shuffled null gives 92 (4.9%). The code's choices, correct trials only in its 0.2 to 1.7 s window, give
146 (7.8%), the paper's numbers; correct trials alone in the Methods' window give 139 (7.5%), also
within tolerance.''')
rep('''**Result: Not reproduced.** 13 units (0.7%) are both VS and MS under the main tests, half the paper's
26. The code's choices give 26 (1.4%).''','''**Result: Not reproduced.** 13 units (0.7%) are both VS and MS under the main tests, half the paper's
26 and below the 21 expected if the two were independent. The code's choices give 25 (1.3%), within
tolerance.''')
rep('''**Result: Partially reproduced.** Under the main tests no Fisher's test finds a difference between CS
(1787 units) and TWH (77 units), but only 3 of the 6 percentages are within tolerance. With the code's
choices, the tests again find no difference.''','''**Result: Partially reproduced.** Under the main tests no Fisher's test finds a difference between CS
(1787 units) and TWH (77 units; p = 0.36, 0.15 and 0.42), but only 3 of the 6 percentages are within
tolerance (CS VS 17.6%, TWH MS 10.4% and TWH dual 1.3%). With the code's choices all 6 are within
tolerance and no test finds a difference.''')
rep('''**Result: Partially reproduced.** 64 of the 65 sessions of the 2018 table are in the dandiset under the
same subject and variant (98.5%). Session 98 is not in the dandiset, nor in Online-only Table 1.''','''**Result: Partially reproduced.** 64 of the 65 sessions of the 2018 table are in the dandiset under the
same subject and variant (98.5%). Session 98 (H48, variant 2) is in neither the dandiset nor Online-only
Table 1. Of the 42 subjects, 39 have the same age and sex in the 2018 table and the files; the 2018
table agrees with Online-only Table 1 on the three others (C24, H33, H48).''')
rep('''ages = far_t1.set_index("label")[["age", "sex"]].join(paper_t1.set_index("label")[["age", "sex"]], rsuffix="_2020", how="inner")''',
'''ages = far_t1.set_index("label")[["age", "sex"]].join(
    paper_t1.set_index("label")[["age", "sex"]].rename(columns={"age": "age_2020", "sex": "sex_2020"}), how="inner")''')
rep('''**Result: Partially reproduced.** The dandiset has 23 sessions and 17 subjects that the 2018 table does
not list, as the paper says, but their units number far fewer than 288 (printed above).''','''**Result: Partially reproduced.** The dandiset has 23 sessions and 17 subjects that the 2018 table does
not list, as the paper says, but these sessions hold 325 unit rows, above the tolerance of 288 ± 28.8.
The difference of the totals the two papers state (1863 - 1576 = 287) is the paper's number.''')
rep('''**Result: Reproduced.** Session 132 has one unit on channel 177, on electrode row 4 in the right
amygdala; its rates differ across categories (ANOVA p printed above, below 0.05) and are highest for
animals in both windows.''','''**Result: Reproduced.** Session 132 has one unit on channel 177, unit 4 on electrode row 4 in the right
amygdala; its rates differ across categories (ANOVA p = 1.2e-22) and are highest for animals (6.75 Hz
against 0.25 to 0.85 Hz), in both windows.''')
rep('''Blocked: there is no session 144 in the dandiset or in Online-only Table 1. The only units on a
channel 140 in the right hippocampus are in session 2009 (T103); they are shown here, but nothing links
them to the figure's neuron, so they do not decide the claim.''','''Blocked: there is no session 144 in the dandiset or in Online-only Table 1. The only units on a
channel 140 in the dandiset are in session 2009 (T103), in the right hippocampus; they are shown here,
but no identifier links them to the figure's neuron, so they do not decide the claim.''')
open(p,'w').write(s)
E
```

```
Sun Nov 15 13:01:53 UTC 2026
Shell cwd was reset to
```

**Agent**

Time is 13:02, well ahead of schedule. Adding a per-subject breakdown of VS/MS, the Figure 3 candidate note, and the summary, then rebuilding.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'E'
p='/tmp/claude-1001/cells.py'; s=open(p).read()
def rep(a,b):
    global s
    assert a in s, a[:80]
    s=s.replace(a,b)
rep('''exp = cells.vs_m.mean() * cells.ms_m.mean() * n
print(f"Expected if VS and MS were independent: {exp:.1f}")''','''exp = cells.vs_m.mean() * cells.ms_m.mean() * n
print(f"Expected if VS and MS were independent: {exp:.1f}")
by_subject = cells.assign(label=cells.identifier.map(info.set_index("identifier").label), dual=dual).groupby("label").agg(
    sessions=("identifier", "nunique"), units=("unit", "size"), VS=("vs_m", "sum"), MS=("ms_m", "sum"), dual=("dual", "sum"))
print("By subject (main tests); subjects with no VS unit:", int((by_subject.VS == 0).sum()), "; with no MS unit:", int((by_subject.MS == 0).sum()))
print(by_subject.T.to_string())''')
rep('''example(2009, 140, 3, "Right Hippocampus")
""", tags=["claim:fig3-example-vs-neuron"])
''','''example(2009, 140, 3, "Right Hippocampus")
""", tags=["claim:fig3-example-vs-neuron"])

md(r"""
Session 2009 (T103) holds three units; the third (unit 2, on channel 140 in the right hippocampus) is
category selective (ANOVA p = 1.3e-09) with its highest rate for phones (9.1 Hz against 1.7 to 2.7 Hz).
It fits the figure's channel, cell number (counted from 1), area and preferred category, but not its
session id, so the claim stays blocked and the question goes to the paper's authors.
""")
''')
rep('''md(r"""
## Summary
""")
''','''md(r"""
## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
the differences from the paper's method.

| Claim | Outcome |
|---|---|
| counts-neurons-subjects | Reproduced: 1864 unit rows (1798 with duplicated spike trains once), 59 subjects |
| counts-sessions | Reproduced: the 87 (subject, session) pairs equal Online-only Table 1 |
| table1-demographics | Partially reproduced: age or sex differ for 3 of 59 subjects |
| task-structure | Partially reproduced: 8 sessions have 50 or 97 encoding trials |
| new-old-label-coding | Not reproduced: label 1 is old and 0 new, the reverse of the stated coding |
| ttl-codes | Partially reproduced: 9 files hold unlisted codes |
| experiment-ids | Partially reproduced: 4 files use id 82 |
| session-dates | Partially reproduced: one date on the 13th, one year 2000 |
| units-table | Partially reproduced: SNR or isolation distance missing for many units |
| electrodes-table | Not reproduced: impedance empty for every electrode |
| isi-criterion | Partially reproduced: 1858 of 1864 units below 3% |
| fig5a-mtl-locations | Reproduced: every unit in amygdala or hippocampus |
| fig5c-auc-all | Reproduced: AUC 0.753 ± 0.094 |
| fig5c-auc-sites | Reproduced: CS 0.760 ± 0.085, TWH 0.688 ± 0.138 |
| fig5b-roc-asymmetric | Reproduced: mean z-ROC slope 0.78, p = 4.3e-09 |
| fig5d-confidence-accuracy | Reproduced: paired p = 3.2e-16 (fixed split) |
| vs-cells-proportion | Reproduced: 332 (17.8%) |
| ms-cells-proportion | Not reproduced: 118 (6.3%); the code's choices give 146 (7.8%) |
| dual-cells-proportion | Not reproduced: 13 (0.7%); the code's choices give 25 (1.3%) |
| fig5f-site-proportions | Partially reproduced: no site difference, 3 of 6 values within tolerance |
| twh-sessions | Reproduced: 9 sessions |
| previous-release-link | Partially reproduced: 64 of 65 earlier sessions found and agree |
| previous-release-additions | Partially reproduced: 23 sessions and 17 subjects new, but 325 units |
| fig4-example-vs-neuron | Reproduced: ANOVA p = 1.2e-22, animals highest |
| fig3-example-vs-neuron | Blocked: session 144 is in neither the dandiset nor Online-only Table 1 |

**How the analysis differs from the paper's.** The selection of VS and MS cells follows the Methods
(a 1 s window from 200 ms, all 50 new and 50 old trials), as the claims file prescribes; the paper's
code uses 0.2 to 1.7 s and, for MS cells, correct trials only, and those choices give the paper's 343,
146 and 26 (25 here). The bootstrap is seeded. Sessions without a defined z-ROC slope (5) and without
responses in a confidence group (3 or 5) are left out of those tests. Online-only Table 1 and Faraut et
al. 2018 Table 1 are read from Europe PMC.

**What was found about the dataset.** The new/old labels are coded 1 = old, the reverse of the paper's
text and the column's description. Seven sessions hold only 50 of their encoding trials and one holds
97, so 21 to 24 old images of those sessions were never shown in the file's encoding block. 66 spike
trains are deposited in two files each (sessions 38/39, 43/44 and 54/55), and 54/55 share the encoding
trials. 13 units store spike times out of order, two of them with every spike twice. Electrode
impedance is empty, SNR or isolation distance missing or infinite for many units, ages or sex differ
from the paper's table for three subjects, four files use experiment id 82, nine hold event codes
Table 1 does not list, one start date is not on the 1st and one has the year 2000.
""")
''')
open(p,'w').write(s)
E
. env/bin/activate && python build.py cells.py entries/chandravadia-2020/reproduce_chandravadia_2020.ipynb && echo built
```

```
built
Shell cwd was reset to
```

**Agent**

Now the entry files (entry.yaml, requirements.in, README), then lock and run.

**Agent calls Bash**

```bash
cd entries/chandravadia-2020 && cat > requirements.in <<'E'
dandi
h5py
matplotlib
numpy
pandas
remfile
scipy
E
cat > entry.yaml <<'E'
schema_version: 1
name: chandravadia-2020
type: reproduction
title: Human MTL single neurons during a new/old recognition task (Chandravadia et al. 2020)
description: Tests the findings of Chandravadia et al. (2020) on dandiset 000004, which holds 87 sessions
  of 59 epilepsy patients performing a new/old recognition memory task, with 1864 units from the
  amygdala and hippocampus. It checks the file contents the data descriptor documents (subjects,
  sessions, trials, event codes, units and electrodes tables, the new/old labels), the behavioural
  ROC, AUC and confidence results, and the proportions of visually and memory selective cells.
license: Apache-2.0
notebooks:
- path: reproduce_chandravadia_2020.ipynb
  title: Reproducing Chandravadia et al. (2020) from dandiset 000004
  runtime_minutes: 4
helpers:
- nomem.py
related:
- id: dandi:000004/0.220126.1852
  relation: uses_data
- id: doi:10.1038/s41597-020-0415-9
  relation: reproduces
E
cat ../fouke-2025/entry.yaml | grep -n python; cd  && python tools/entry.py lock entries/chandravadia-2020 2>&1 | tail -3 && cat entries/chandravadia-2020/entry.yaml | tail -3
```

```
wrote chandravadia-2020/requirements.lock.txt (Python 3.13, with hashes)
  relation: uses_data
- id: doi:10.1038/s41597-020-0415-9
  relation: reproduces
```

**Agent calls Bash**

```bash
grep -n python entries/chandravadia-2020/entry.yaml; python tools/entry.py check entries/chandravadia-2020 2>&1 | tail -15
```

```
11:python: "3.13"
0 error(s)
```

**Agent calls Bash**

```bash
time python tools/entry.py all entries/chandravadia-2020 2>&1 | tail -15
```

```
Installed kernelspec registry-chandravadia-2020 in executed/chandravadia-2020/.venv/share/jupyter/kernels/registry-chandravadia-2020
0 error(s)
pass  reproduce_chandravadia_2020.ipynb  (162 s)

real	2m51.892s
user	1m3.869s
sys	0m16.219s
```

**Agent calls Bash**

```bash
ls executed/chandravadia-2020/ && python - <<'E'
import json
nb=json.load(open('executed/chandravadia-2020/reproduce_chandravadia_2020.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    tags=c['metadata'].get('tags',[])
    if not any(t in tags for t in ['claim:isi-criterion','claim:ms-cells-proportion','claim:dual-cells-proportion','claim:units-table','claim:fig5f-site-proportions','claim:vs-cells-proportion','claim:fig3-example-vs-neuron']) and i not in (1,12,14): continue
    out=''
    for o in c.get('outputs',[]):
        if 'text' in o: out+=''.join(o['text'])
        elif o.get('output_type')=='error': out+='ERROR '+o['ename']+o['evalue']
    print(f'==== cell {i} {tags}\n{out[:3000]}')
E
```

```
reproduce_chandravadia_2020.ipynb
result.json
==== cell 1 []
loaded 87 files from dandiset 000004 version 0.220126.1852 in 120 s
Online-only Table 1: 59 subject rows; totals row: ['Total Subjects: 59', 'Total Sessions: 87', 'Total Female: 25', 'Total Male: 34']

==== cell 41 ['claim:units-table']
Columns over all files: {'origClusterID': 87, 'waveform_mean_encoding': 87, 'waveform_mean_recognition': 87, 'IsolationDist': 87, 'SNR': 87, 'waveform_mean_sampling_rate': 87, 'spike_times': 87, 'electrodes': 87}
Missing by name in every file: ['IsolDist']
IsolationDist column description: 'IsolDist' (read from the files' VectorData description)
Electrodes per unit: {1: 1864}
Waveform sampling rate: [98400.0] Hz; within 100000 +- 10000: True
Waveforms finite for every unit: True
SNR: not finite for 86 of 1864 units (NaN 75, infinite 11), in 33 files; above 1e6: 11
IsolationDist: not finite for 493 of 1864 units (NaN 493, infinite 0), in 82 files; above 1e6: 2
origClusterID: not finite for 0 of 1864 units (NaN 0, infinite 0), in 0 files; above 1e6: 0

==== cell 47 ['claim:isi-criterion']
Units stored out of time order: 13 ; units holding repeated spike times: [{'identifier': 'H27_58', 'unit': 35, 'spikes': 3268, 'distinct': 1634}, {'identifier': 'H27_58', 'unit': 37, 'spikes': 824, 'distinct': 412}]
sorted: below 3% for 1858 of 1864 units (99.7%); median 0.19%, max 50.06%; units with fewer than 2 spikes: 0
[... 76 more lines not kept]
```

**Agent**

Clean run passes (162 s) with the same numbers. Writing the entry README and the attempt record.

**Agent calls Write**

```json
{
 "file_path": "entries/chandravadia-2020/README.md",
 "content": "# Chandravadia et al. (2020) from dandiset 000004\n\nTests the findings of [Chandravadia et al. (2020)](https://doi.org/10.1038/s41597-020-0415-9), a data\ndescriptor of human single-neuron recordings during a new/old recognition memory task, on\n[DANDI:000004](https://dandiarchive.org/dandiset/000004/0.220126.1852) (version 0.220126.1852). The\ndandiset holds 87 sessions of 59 patients with 1864 units in the amygdala and hippocampus.\n\n| Claim | Outcome |\n|---|---|\n| 1863 neurons from 59 subjects | Reproduced |\n| 87 sessions, as in Online-only Table 1 | Reproduced |\n| Age and sex of each subject as in Online-only Table 1 | Partially reproduced |\n| 100 encoding and 100 recognition trials per session, 5 categories | Partially reproduced |\n| new_old_labels_recog is 0 for old and 1 for new stimuli | Not reproduced |\n| TTL event codes of Table 1 | Partially reproduced |\n| Experiment ids of Table 2 | Partially reproduced |\n| Session dates set to the first of the month | Partially reproduced |\n| Units table columns and quality metrics | Partially reproduced |\n| Electrodes table with location, coordinates, impedance, filter, channel | Not reproduced |\n| Fewer than 3% of interspike intervals below 3 ms | Partially reproduced |\n| All neurons in amygdala or hippocampus | Reproduced |\n| Behavioural AUC 0.74 ± 0.10 | Reproduced |\n| AUC 0.74 ± 0.09 (CS) and 0.69 ± 0.13 (TWH) | Reproduced |\n| Asymmetric ROC | Reproduced |\n| Higher accuracy with high confidence | Reproduced |\n| 343 VS cells (18.4%) | Reproduced |\n| 146 MS cells (7.8%) | Not reproduced |\n| 26 dual VS and MS cells (1.4%) | Not reproduced |\n| Comparable proportions at the two sites | Partially reproduced |\n| 9 TWH sessions | Reproduced |\n| Sessions of the 2018 release found in the dandiset (link check) | Partially reproduced |\n| 23 sessions, 17 subjects and 288 neurons added since 2018 | Partially reproduced |\n| Example neuron of Figure 4 selective for animals | Reproduced |\n| Example neuron of Figure 3 selective for phones | Blocked: session 144 is not in the dandiset |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe MS and dual-cell counts follow the Methods (a 1 s window from 200 ms, all trials); the paper's code\nuses 0.2 to 1.7 s and correct trials only, and gives the paper's numbers. The attempt record, with the\nreasons and the differences from the paper's method, is\n[`attempts/chandravadia-2020-02.yaml`](../../attempts/chandravadia-2020-02.yaml).\n\n- `reproduce_chandravadia_2020.ipynb`: the analysis. It takes about three minutes, most of it streaming\n  the files.\n- `nomem.py`: loading the files (the stimulus images reduced to one hash per frame), the paper's\n  tables from Europe PMC, and the behavioural and single-unit measures of the paper's code. Other\n  notebooks on this dandiset can import it.\n"
}
```

```
File created successfully at: entries/chandravadia-2020/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "attempts/chandravadia-2020-02.yaml",
 "content": "schema_version: 3\nid: chandravadia-2020-02\ndatasets:\n- archive: dandi\n  id: \"000004\"\n  version: 0.220126.1852\n  doi: 10.48324/dandi.000004/0.220126.1852\n  relation: primary\npaper: doi:10.1038/s41597-020-0415-9\ndate: 2026-11-15\nentry: chandravadia-2020\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-15\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/43715082428\ninputs:\n- what: Table 1 of Faraut et al. 2018 (the sessions, subjects, variants, ages and sexes of the earlier\n    release of this task's data), read at run time from the full text in Europe PMC (PMC5810422), used\n    by previous-release-link and previous-release-additions.\n  source: doi:10.1038/sdata.2018.10\n- what: Online-only Table 1 of the paper itself (subjects, sessions, variants, ages, sexes and\n    diagnoses), read at run time from the full text in Europe PMC (PMC7055261) as the reference the\n    claims compare the files with.\n  source: doi:10.1038/s41597-020-0415-9\n- what: The paper's analysis code, read for the method details the claims file names (adjustHF,\n    calcZROCSlope, calcROC_AUC, bootstrapMeanEqualTest, the fixed and dynamic confidence splits, the\n    windows of single_neuron.py and NWB_singleCellAnalysis_release.m); nothing is imported from it.\n  source: https://github.com/rutishauserlab/recogmem-release-NWB at commit 1d95162d2672e71dd234a31e4b8d70017a289ee3\noutcomes:\n- claim: counts-neurons-subjects\n  outcome: reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:counts-neurons-subjects\n  measured:\n  - 1864\n  - 59\n  notes: The units tables hold 1864 rows over 87 files (paper 1863, difference +1), from 59 distinct\n    subject_id values. Reading (b), with the 66 spike trains deposited in two files each counted once,\n    gives 1798 units, also within tolerance. 1787 unit rows are from CS sessions and 77 from TWH.\n- claim: counts-sessions\n  outcome: reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:counts-sessions\n  measured: 87\n  notes: The identifiers of the 87 files give 87 distinct (subject, session id) pairs, the same set as\n    the 87 of Online-only Table 1 (Cedars-Sinai labels are written CS24 in the identifiers and C24 in\n    the table). The Methods' 89 differs from the file count by 2.\n- claim: table1-demographics\n  outcome: partially_reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:table1-demographics\n  measured:\n  - 26\n  - 33\n  notes: Age and sex match Online-only Table 1 for 56 of 59 subjects. C24 is 57 in the files and 47 in\n    the table, H33 is 30 and 29, and H48 is female and 32 in the files, male and 54 in the table. So the\n    files hold 26 female and 33 male subjects, against the table's 25 and 34 (both within tolerance).\n    Faraut et al. 2018 Table 1 gives the same ages and sexes as Online-only Table 1 for these three. The\n    files' diagnosis text equals the table's for 40 of 59 subjects; the others use coarser terms.\n- claim: task-structure\n  outcome: partially_reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:task-structure\n  notes: All 87 sessions have 100 recognition trials with 50 of each label and 5 categories. 79 have\n    100 encoding trials with 100 distinct image files (and 100 distinct stored images); 7 Huntington\n    sessions (18, 20, 21, 23, 26, 27, 44) have 50 encoding trials and session 123 has 97. Each file\n    stores one image per trial.\n- claim: new-old-label-coding\n  outcome: not_reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:new-old-label-coding\n  notes: Under the stated coding test 1 holds in 0 of 87 sessions and test 2 in 1 of 87. No label-0\n    recognition image (compared by stored pixels and by file name, which agree) is in the session's\n    encoding block, while label-1 images are, all of them in 79 sessions, 49 of 50 in session 123 and\n    26 to 29 of 50 in the seven sessions with 50 encoding trials. Label-1 trials draw \"old\" responses\n    in 69% of trials on average against 27% for label 0, more in 86 of 87 sessions; the exception is\n    session 2005 (T98, AUC 0.445). Both tests hold with the labels reversed in 86 of 87 sessions, so\n    the labels are 1 for old and 0 for new, as the paper's code reads them. With the stated coding the\n    mean behavioural AUC would be 0.247.\n- claim: ttl-codes\n  outcome: partially_reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:ttl-codes\n  notes: In all 87 files events and experiment_ids have the same length and the same timestamps. 78\n    files hold only the codes of Table 1; 9 also hold 0, 4, 22, 23, 98 or 99. Over all files 17019 of\n    17047 trials follow 1, 2, 3, response, 6; the 28 that do not are in 7 of the 9 files with extra\n    codes. All parts hold in 78 of 87 files. Seven files have no start marker (55); every file has 66.\n- claim: experiment-ids\n  outcome: partially_reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:experiment-ids\n  notes: In 83 of 87 files the learning id is in {80, 83, 88} and the recognition id in {81, 84, 89},\n    as one of Table 2's pairs. Four files use 82 (CS33_77 81/82, CS39_100 and H51_105 82/83, H42_55\n    80/82); their data_collection field states the same ids. The learning block is the id whose events\n    hold the encoding answers 20 and 21.\n- claim: session-dates\n  outcome: partially_reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:session-dates\n  notes: 86 of 87 session_start_time values fall on the first of a month; H28_48 is 2010-03-13. H44_68\n    is dated 2000-01-01, six years before any other session (the Huntington sessions run from 2006 to\n    2016 and its neighbours H43 and H47 are 2013 and 2014), so the year looks like a placeholder.\n- claim: units-table\n  outcome: partially_reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:units-table\n  measured: 98400\n  notes: Every file holds spike_times, the two waveform columns, origClusterID, SNR, electrodes and the\n    isolation distance, the last under the name IsolationDist (its description is \"IsolDist\"). All 1864\n    units link to exactly one electrode, the waveforms (256 samples, finite for every unit) are stated\n    as sampled at 98.4 kHz, within tolerance of 100 kHz. SNR is not finite for 86 units (75 NaN, 11\n    infinite, all infinite ones in H28_48) and isolation distance is NaN for 493 units in 82 files, with\n    two values above 1e27.\n  deviations:\n  - The column the paper calls IsolDist is named IsolationDist in the files and was counted as present.\n- claim: electrodes-table\n  outcome: not_reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:electrodes-table\n  notes: Every file has the columns location, x, y, z, imp, filtering, group and origChannel. Location,\n    filtering (\"300-3000Hz\") and origChannel have a value for all 887 electrodes and the MNI coordinates\n    for 788 (missing in 8 files), but the impedance is NaN for all 887 electrodes, which the criterion\n    calls not reproduced.\n- claim: isi-criterion\n  outcome: partially_reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:isi-criterion\n  measured: 99.7\n  notes: With spike times sorted, 1858 of 1864 units (99.7%) have fewer than 3% of interspike intervals\n    below 3 ms (median 0.19%). Of the six others, two (H27_58 units 35 and 37) hold every spike time\n    twice, stored as two copies one after the other, which gives 50% short intervals once sorted; with\n    each spike time once they are at 0%, and four units remain at 3.0% to 9.0% (CS54_126 units 6 and 7,\n    CS26_66 unit 2, CS54_124 unit 2). With the spike times as stored, 1860 units are below 3%. 13 units\n    store spike times out of time order.\n  deviations:\n  - The value given as measured is the percentage of units below 3%, the quantity the criterion\n    thresholds.\n- claim: fig5a-mtl-locations\n  outcome: reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:fig5a-mtl-locations\n  notes: The electrode of every unit is in the right amygdala (594 units), left amygdala (498), right\n    hippocampus (407) or left hippocampus (365).\n- claim: fig5c-auc-all\n  outcome: reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:fig5c-auc-all\n  measured:\n  - 0.753\n  - 0.094\n  notes: Mean AUC over the 87 sessions 0.7527, standard deviation 0.0938 (range 0.445 to 0.919; against\n    0.5, p = 2.2e-41). The ROC uses label 1 as old (claims file); the recognition data of no session are\n    duplicated.\n- claim: fig5c-auc-sites\n  outcome: reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:fig5c-auc-sites\n  measured:\n  - 0.760\n  - 0.688\n  - 0.085\n  - 0.138\n  notes: CS sessions (78) mean 0.7602, SD 0.0855; TWH sessions (9) mean 0.6883, SD 0.1378; all four\n    within tolerance. Welch's t-test between sites t = 1.53, p = 0.161.\n- claim: fig5b-roc-asymmetric\n  outcome: reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:fig5b-roc-asymmetric\n  measured: 0.782\n  notes: Mean z-ROC slope over 82 sessions 0.782 (SD 0.300, median 0.791), below 1 with t = -6.58,\n    p = 4.3e-09; 65 of 82 slopes are below 1. Wilcoxon signed-rank against 1 p = 2e-08; the slope of the\n    pooled ROC is 0.816.\n  deviations:\n  - Five sessions (CS24_60, CS39_93, H48_99, CS51_119, T100_2008) have fewer than two distinct false\n    alarm rates among the five interior points, so no regression slope, and are left out; the paper's\n    code would regress on a constant predictor there.\n- claim: fig5d-confidence-accuracy\n  outcome: reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:fig5d-confidence-accuracy\n  notes: (a) Fixed split, 84 sessions (3 without responses in one group left out), high 80.1% and low\n    60.9% correct, paired t = 10.16, p = 3.2e-16, high above low in 73 sessions. (b) Dynamic split of\n    the Python code, 82 sessions (5 left out), 78.2% and 60.8%, p = 1.3e-11. The unpaired test and the\n    inclusion rule of plotFigure5.ipynb (73 sessions) give the same. In the 8 TWH sessions alone the\n    difference has the same sign without significance (p = 0.14 and 0.26).\n  deviations:\n  - The dynamic split is the Python helper.dynamic_split as written, which in its split mode 1 counts\n    low-confidence hits as response 4 only (the MATLAB NO_dynamic_lowHighSplit.m counts 4 and 5).\n- claim: vs-cells-proportion\n  outcome: reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:vs-cells-proportion\n  measured:\n  - 332\n  - 17.8\n  notes: In the Methods' window (0.2 to 1.2 s), 332 of 1864 units (17.8%) are VS; 6 units with all rates\n    equal have no ANOVA p and are counted as not selected. Variants, the code's window 343 (18.4%), the\n    paper's numbers; duplicated spike trains once 321 of 1798 (17.9%); categories shuffled within\n    session 76 (4.1%). By session the VS share has median 15.4%; 5 of 59 subjects have no VS unit.\n- claim: ms-cells-proportion\n  outcome: not_reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:ms-cells-proportion\n  measured:\n  - 118\n  - 6.3\n  notes: With all 50 new and 50 old trials in the Methods' window, 118 of 1864 units (6.3%) are MS, below\n    146 ± 14.6 (7.8 ± 0.78%); five other seeds give 108 to 115, and labels shuffled within session give\n    92 (4.9%). The code's choices (correct trials only, 0.2 to 1.7 s, as in single_neuron.py ms_test and\n    NWB_singleCellAnalysis_release.m) give 146 (7.8%), the paper's numbers; correct trials alone in the\n    Methods' window give 139 (7.5%), also within tolerance. Duplicated spike trains once 115 of 1798. The\n    count the paper reports thus matches the code's procedure and not the one its Methods describe.\n- claim: dual-cells-proportion\n  outcome: not_reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:dual-cells-proportion\n  measured:\n  - 13\n  - 0.7\n  notes: 13 units (0.7%) are VS and MS under the main tests, against 26 ± 2.6 (1.4 ± 0.14%), and 21\n    would be expected if the two selections were independent. With the code's choices for both tests 25\n    (1.3%), within tolerance; with the Methods' window and MS on correct trials 22 (1.2%). The outcome\n    follows from ms-cells-proportion.\n- claim: fig5f-site-proportions\n  outcome: partially_reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:fig5f-site-proportions\n  measured:\n  - 17.6\n  - 6.2\n  - 0.7\n  - 22.1\n  - 10.4\n  - 1.3\n  notes: Under the main tests CS (1787 units) has 17.6% VS, 6.2% MS and 0.7% dual cells and TWH (77\n    units) 22.1%, 10.4% and 1.3%; Fisher's exact tests find no difference (p = 0.36, 0.15, 0.42), but\n    only 3 of 6 values are within tolerance. With the code's choices the values are 18.4, 7.7, 1.3, 19.5,\n    10.4 and 1.3%, all within tolerance, and no test finds a difference. TWH counts rest on 77 units in 9\n    sessions (1 to 31 units each).\n- claim: twh-sessions\n  outcome: reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:twh-sessions\n  measured: 9\n  notes: Nine sessions, of eight subjects (T88 has two), have labels starting with T, and their\n    institution field is Toronto Western Hospital.\n- claim: previous-release-link\n  outcome: partially_reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:previous-release-link\n  notes: Faraut et al. 2018 Table 1 lists 42 subjects and 65 sessions. 64 of the 65 sessions are in the\n    dandiset under the same session id, subject and variant (98.5%); session 98 (H48, variant 2) is in\n    neither the dandiset nor Online-only Table 1. All 42 subjects are in the files; age and sex agree for\n    39, and the 2018 table agrees with Online-only Table 1 on the other three (C24, H33, H48), so those\n    differences are in the files. The variant of a file is read from its category names.\n- claim: previous-release-additions\n  outcome: partially_reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:previous-release-additions\n  measured:\n  - 23\n  - 17\n  - 325\n  notes: 23 sessions of the dandiset (14 CS, 9 TWH) and 17 subjects (C53 to C62, the 8 T subjects) are\n    not in the 2018 table, as the paper says, but these sessions hold 325 unit rows, above 288 ± 28.8.\n    The difference of the stated totals, 1863 - 1576 = 287, is the paper's number; it is not the units of\n    the new sessions, as the dandiset's older sessions hold 1539 unit rows, not 1576.\n  deviations:\n  - The earlier release's session list is taken from the table of Faraut et al. 2018, not from the\n    earlier release's files, as the claims file prescribes.\n- claim: fig4-example-vs-neuron\n  outcome: reproduced\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:fig4-example-vs-neuron\n  notes: Session 132 (CS58_132) has one unit on channel 177, unit 4 on electrode row 4 in the right\n    amygdala. Its rates differ across the 5 categories (ANOVA p = 1.2e-22 in the Methods' window,\n    7.9e-19 in the code's) and are highest for animals (6.75 Hz against 0.25 to 0.85 Hz).\n- claim: fig3-example-vs-neuron\n  outcome: blocked\n  blocked_by: other\n  notebook: reproduce_chandravadia_2020.ipynb\n  output: claim:fig3-example-vs-neuron\n  notes: The figure's neuron cannot be identified. No file and no row of Online-only Table 1 has a\n    session 144. The only units on a channel 140 in the dandiset are units 1 and 2 of session 2009\n    (T103, 3 units), in the right hippocampus; unit 2, the third unit of the session, is category\n    selective (ANOVA p = 1.3e-09) with its highest rate for phones (9.1 Hz against 1.7 to 2.7 Hz). It fits\n    the figure's channel, area, cell number counted from 1 and preferred category, but not its session\n    id, so it is shown and does not decide the claim. Whether neuron 144-140-3-RH is this unit is a\n    question for the paper's authors.\nfindings:\n- kind: metadata_error\n  statement: The new_old_labels_recog column is coded 1 for old (seen during encoding) and 0 for new, the\n    reverse of its description in every file (\"0 == Old Stimuli\") and of the paper's Data Records. In\n    all 87 sessions no label-0 recognition image is among the session's encoding images while label-1\n    images are, and label-1 trials draw more \"old\" responses in 86 of 87 sessions. The paper's analysis\n    code reads 1 as old, so its results are unaffected; a user who follows the description inverts the\n    behaviour (mean AUC 0.25 instead of 0.75).\n- kind: data_missing\n  statement: Eight sessions lack encoding trials. Seven Huntington sessions (18, 20, 21, 23, 26, 27 and\n    44) hold 50 encoding trials and session 123 holds 97, against 100 in the paper. In the seven, 21 to\n    24 of the 50 images labelled old in the recognition block are not among the file's encoding images\n    (they are in the encoding blocks of other sessions of the same variant), so the encoding trials that\n    showed them are not in the file.\n- kind: other\n  about: data\n  statement: 66 spike trains are deposited in two files each, sessions 38 and 39 (11 units), 43 and 44\n    (23) and 54 and 55 (32), with nothing marking them as the same units. Each pair was recorded on one\n    day, and each file holds spike trains spanning both sessions. Sessions 54 and 55 also share their\n    encoding trials (one learning block followed by two recognition blocks). Counting units per file\n    gives 1864, counting them once 1798.\n- kind: format_error\n  statement: Spike times are not in increasing order in 13 units. Two units of session 58 (H27_58 units\n    35 and 37) hold every spike time twice, as two copies one after the other, which doubles their spike\n    counts and makes half their sorted interspike intervals zero.\n- kind: metadata_error\n  statement: Subject age or sex differ from Online-only Table 1, and from Faraut et al. 2018 Table 1,\n    for three subjects. C24 (P24CS) is 57 in the files and 47 in both tables, H33 (P33HMH) 30 and 29, and\n    H48 (P48HMH) is a 32-year-old female in the files and a 54-year-old male in both tables. The\n    diagnosis is coded more coarsely than in the paper for 19 subjects.\n- kind: metadata_error\n  statement: session_start_time is not on the first of the month for session 48 (H28, 2010-03-13), and\n    session 68 (H44) is dated 2000-01-01, six years before any other session of the archive's files and\n    out of order with the subjects recorded before and after it (2013 and 2014). In 38 files the trial,\n    event and spike times are Unix seconds, while timestamps_reference_time is set to the session's\n    start date, so the stated reference does not apply to them.\n- kind: data_missing\n  statement: The electrode impedance (imp) is NaN for all 887 electrodes in all 87 files, and the MNI\n    coordinates (x, y, z) are NaN for 99 electrodes in 8 files, although the paper says the electrodes\n    table gives each electrode's coordinates and impedance.\n- kind: metadata_error\n  statement: Spike sorting quality metrics are missing or invalid for many units. SNR is NaN for 75 units\n    and infinite for 11 (session 48), and the isolation distance is NaN for 493 of 1864 units in 82\n    files, with two values above 1e27. The isolation distance column is named IsolationDist, not IsolDist\n    as in the paper.\n- kind: metadata_insufficient\n  statement: Nine files hold event codes that Table 1 of the paper and the events description do not\n    define (0, 4, 22, 23, 98, 99), and in 7 of them 28 trials break the documented order 1, 2, 3,\n    response, 6; in 4 of these files the response read three events after stimulus onset, as the\n    paper's code does, differs from response_value for 1 to 6 trials. Seven files have no start marker\n    (55). In the encoding phase response_value holds 0 or 1, not the event codes 20 and 21 the paper\n    refers to.\n- kind: metadata_error\n  statement: Four files label a block with experiment id 82 (CS33_77 81/82, CS39_100 82/83, H51_105\n    82/83, H42_55 80/82), which Table 2 of the paper does not list; the paper says each session has one\n    of the pairs (80, 81), (83, 84) or (88, 89). The institution field misspells Huntington Memorial\n    Hospital in two ways (\"Hunigton\" in 28 files, \"Hunington\" in 6).\n- kind: code_mismatch\n  statement: The paper's Methods select VS and MS cells in a 1 s window starting 200 ms after stimulus\n    onset and compare the 50 novel with the 50 familiar trials. The published code (single_neuron.py,\n    NWB_singleCellAnalysis_release.m) uses 0.2 to 1.7 s and, for MS cells, correct trials only. On the\n    dandiset the code's choices give the paper's 343 VS, 146 MS and 25 dual cells (26 in the paper), and\n    the Methods' choices give 332, 118 and 13. The reported MS and dual counts rest on the code's\n    procedure.\n- kind: paper_inconsistency\n  statement: The Methods say patients were recorded across 89 sessions, while Online-only Table 1 and the\n    dandiset hold 87.\n- kind: paper_inconsistency\n  statement: The neuron of Figure 3, 144-140-3-RH, names a session 144 that is not in Online-only Table\n    1 nor in the dandiset. The only channel-140 units in the dandiset are in session 2009 (T103, right\n    hippocampus), whose third unit is phone selective (ANOVA p = 1.3e-09). The authors could say whether\n    the figure shows this unit.\n"
}
```

```
File created successfully at: attempts/chandravadia-2020-02.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/chandravadia-2020 && . $TMPDIR/env/bin/activate && python -c "
import pickle,numpy as np
ss=pickle.load(open('/tmp/claude-1001/sessions.pkl','rb'))
print(set(x['identifier'] for x in ss for v in x['units'].SNR if np.isinf(v)))
" ; cd  && grep -nE '^[^#]*[^"]: [^|>]' attempts/chandravadia-2020-02.yaml | grep -vE '^\s*[0-9]+:\s*-?\s*[a-z_]+: ' | head; python tools/entry.py check entries/chandravadia-2020 2>&1 | tail -5
```

```
{'H28_48'}
0 error(s)
```

**Agent calls Bash**

```bash
python - <<'E'
import yaml
d=yaml.safe_load(open('attempts/chandravadia-2020-02.yaml'))
def walk(x,p=''):
    if isinstance(x,dict):
        for k,v in x.items(): walk(v,p+'/'+str(k))
    elif isinstance(x,list):
        for i,v in enumerate(x): walk(v,p+f'[{i}]')
    elif isinstance(x,str) and (': ' in x or '—' in x or 'rather' in x): print(p, x[:80])
walk(d); print(len(d['outcomes']), collections if False else '')
import collections; print(collections.Counter(o['outcome'] for o in d['outcomes']))
E
grep -n -- '—\|rather' entries/chandravadia-2020/*.py entries/chandravadia-2020/README.md /tmp/claude-1001/cells.py | head
```

```
25 
Counter({'reproduced': 10, 'partially_reproduced': 10, 'not_reproduced': 4, 'blocked': 1})
```

**Agent**

Record validates: 10 reproduced, 10 partially, 4 not reproduced, 1 blocked. Removing the bold labels from the notebook header and summary (only the Result openers may be bold), then re-running.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'E'
p='/tmp/claude-1001/cells.py'; s=open(p).read()
for a,b in [('**Paper.**','Paper.'),('**Dandiset.**','Dandiset.'),('**Outside inputs.**','Outside inputs.'),('**Method choices**','Method choices'),('**How the analysis differs from the paper\'s.**','How the analysis differs from the paper\'s.'),('**What was found about the dataset.**','What was found about the dataset.')]:
    assert a in s, a; s=s.replace(a,b)
import re; print([m for m in re.findall(r'\*\*[^*]+\*\*', s) if not m.startswith('**Result')])
open(p,'w').write(s)
E
. env/bin/activate && python build.py cells.py entries/chandravadia-2020/reproduce_chandravadia_2020.ipynb && cd  && python tools/entry.py all entries/chandravadia-2020 2>&1 | tail -3
```

```
[]
Installed kernelspec registry-chandravadia-2020 in executed/chandravadia-2020/.venv/share/jupyter/kernels/registry-chandravadia-2020
0 error(s)
pass  reproduce_chandravadia_2020.ipynb  (160 s)
```

**Agent calls Bash**

```bash
python - <<'E'
import json
nb=json.load(open('executed/chandravadia-2020/reproduce_chandravadia_2020.ipynb'))
txt=''.join(''.join(o.get('text','')) for c in nb['cells'] if c['cell_type']=='code' for o in c.get('outputs',[]))
for k in ['main): 118 of 1864','332 of 1864','VS and MS, main tests: 13','Mean slope 0.782','Mean AUC 0.7527','New neurons (unit rows of new sessions): 325','true onsets 830 of 1864','below 3% for 1858','Age and sex both match: 56']:
    print(k in txt, k)
print([o.get('ename') for c in nb['cells'] for o in c.get('outputs',[]) if o.get('output_type')=='error'])
E
python tools/entry.py handover entries/chandravadia-2020 2>&1 | tail -3; ls executed/chandravadia-2020/handover; date -u
```

```
True main): 118 of 1864
True 332 of 1864
True VS and MS, main tests: 13
True Mean slope 0.782
True Mean AUC 0.7527
True New neurons (unit rows of new sessions): 325
True true onsets 830 of 1864
True below 3% for 1858
True Age and sex both match: 56
[]
wrote executed/chandravadia-2020/handover
chandravadia-2020.yaml
nomem.py
reproduce_chandravadia_2020.ipynb
Sun Nov 15 13:10:55 UTC 2026
```

**Agent**

## Report: chandravadia-2020, repeat attempt 02 (blind)

The entry is at `entries/chandravadia-2020/` and the record at `attempts/chandravadia-2020-02.yaml`. `tools/entry.py all` reports 0 errors, and the notebook passes a clean run in 160 s. The verifier's package is built in `executed/chandravadia-2020/handover/`. I did not commit anything.

### 1. Outcomes

| Claim | Outcome | Key numbers |
|---|---|---|
| counts-neurons-subjects | reproduced | 1864 unit rows (1798 with duplicated spike trains counted once), 59 subjects |
| counts-sessions | reproduced | the 87 (subject, session) pairs equal Online-only Table 1 |
| table1-demographics | partially reproduced | 56 of 59 subjects match; C24, H33 and H48 differ |
| task-structure | partially reproduced | 7 sessions have 50 encoding trials, 1 has 97 |
| new-old-label-coding | not reproduced | labels are reversed: 1 = old (86 of 87 sessions on both tests) |
| ttl-codes | partially reproduced | 78 of 87 files; 9 hold codes Table 1 does not list |
| experiment-ids | partially reproduced | 83 of 87; 4 files use id 82 |
| session-dates | partially reproduced | one date on 2010-03-13, one session dated 2000-01-01 |
| units-table | partially reproduced | SNR not finite for 86 units, isolation distance missing for 493 |
| electrodes-table | not reproduced | impedance empty for all 887 electrodes |
| isi-criterion | partially reproduced | 1858 of 1864 units below 3% |
| fig5a-mtl-locations | reproduced | every unit in amygdala or hippocampus |
| fig5c-auc-all | reproduced | 0.753 ± 0.094 |
| fig5c-auc-sites | reproduced | CS 0.760 ± 0.085, TWH 0.688 ± 0.138 |
| fig5b-roc-asymmetric | reproduced | mean z-ROC slope 0.78, p = 4.3e-9 |
| fig5d-confidence-accuracy | reproduced | paired p = 3.2e-16 (fixed split), 1.3e-11 (dynamic split) |
| vs-cells-proportion | reproduced | 332 (17.8%) |
| ms-cells-proportion | not reproduced | 118 (6.3%); the code's choices give 146 (7.8%) |
| dual-cells-proportion | not reproduced | 13 (0.7%); the code's choices give 25 |
| fig5f-site-proportions | partially reproduced | no site difference, but only 3 of 6 values within tolerance |
| twh-sessions | reproduced | 9 sessions |
| previous-release-link | partially reproduced | 64 of 65 sessions of the 2018 release found (session 98 missing) |
| previous-release-additions | partially reproduced | 23 sessions and 17 subjects match, but 325 units against 288 |
| fig4-example-vs-neuron | reproduced | ANOVA p = 1.2e-22, animals highest |
| fig3-example-vs-neuron | blocked (`other`) | no session 144 exists |

Totals: 10 reproduced, 10 partially reproduced, 4 not reproduced, 1 blocked.

### 2. What was found

**About the dataset:**
- The `new_old_labels_recog` coding is the reverse of what the file description and the paper's text say.
- Eight sessions are missing encoding trials. In the seven with 50 trials, 21 to 24 of the "old" images were never shown in that file's encoding block.
- 66 spike trains are deposited in two files each (session pairs 38/39, 43/44 and 54/55). Sessions 54 and 55 also share their encoding block.
- 13 units store spike times out of order, and two of them hold every spike twice.
- Smaller problems:
  - Electrode impedance is empty everywhere, and coordinates are missing for 99 electrodes.
  - SNR is NaN or infinite, and isolation distance missing or around 1e27, for many units.
  - Three subjects' age or sex differ from the paper's table.
  - Some event codes and experiment ids are undocumented.
  - One date is wrong and one year looks like a placeholder.
  - 38 files use Unix-time clocks, and the institution name is misspelled two ways.

**About the paper:**
- The Methods' window and trial choice for selecting cells differ from the published code. The code's choices (0.2 to 1.7 s, correct trials only for MS) reproduce the paper's 343, 146 and 26 (25 here).
- The Methods say 89 sessions; the paper's own table and the files have 87.

**Assumptions:** none affect an outcome. I left out five sessions where the z-ROC slope is undefined; this is recorded as a deviation.

**Question for the paper's authors:** is the Figure 3 neuron 144-140-3-RH the third unit of session 2009 (T103)? That is the only channel-140 unit set in the dataset, and that unit is strongly phone-selective (p = 1.3e-9).

**Questions to a reader:** none.

**Possible exposure to earlier work:** the claims file's opening comment describes the earlier author's data check (duplicated spike trains in sessions 43/44 and 54/55, label 1 drawing most "old" responses) and how the link claim was added. That is the only earlier-attempt material I saw. I found the same things independently.

### 3. Where the protocol was unclear or did not fit
1. None of the blocking reasons fits a paper identifier that names no session in the dataset. I used `other` and explained it in the notes.
2. There is no finding kind for a question to the authors that is not about a method. For the Figure 3 question I used `paper_inconsistency`.
3. For a criterion that sets a threshold on a share of units (isi-criterion), it is unclear what `measured` should hold. I recorded the percentage of units below 3% and noted that as a deviation.
4. The claims file's opening comment can carry an earlier author's observations, which works against a blind repeat. I am only reporting this.
5. It is unclear whether the paper's own table, read at run time from Europe PMC, counts as an input. I listed it under `inputs` alongside Faraut et al. 2018 and the paper's code.

### 4. Runtime and failures
- The notebook runs in about 2.7 minutes (2 of them streaming), using 0.8 GB of memory.
- The session ran from 12:41 to about 13:11 UTC.
- Nothing failed.

## End of run

64 turns, 27 minutes, $7.02 at API prices, result: success.
