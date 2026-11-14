# chandravadia-2020 · author · run 43597317395

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cd  ls; ls docs entries attempts claims paper tools; wc -l docs/*.md README.md
```

```
Sat Nov 14 13:04:16 UTC 2026
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
[... 986 more lines not kept]
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
cd  cat README.md | head -80; sed -n 1,280p docs/design.md | head -120
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
[... 179 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls -la entries/fouke-2025 entries/chandravadia-2020; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; cat attempts/fouke-2025-01.yaml | head -250
```

```
ls: cannot access 'entries/chandravadia-2020': No such file or directory
entries/fouke-2025:
total 132
drwxr-xr-x   2 runner runner  4096 Nov 14 12:57 .
drwxr-xr-x 292 runner runner 12288 Nov 14 13:04 ..
-rw-r--r--   1 runner runner  2144 Nov 14 12:57 README.md
-rw-r--r--   1 runner runner   907 Nov 14 12:57 entry.yaml
-rw-r--r--   1 runner runner 16218 Nov 14 12:57 omr.py
-rw-r--r--   1 runner runner 79403 Nov 14 12:57 reproduce_fouke_2025.ipynb
-rw-r--r--   1 runner runner    61 Nov 14 12:57 requirements.in
-rw-r--r--   1 runner runner  5989 Nov 14 12:57 requirements.lock.txt
schema_version: 1
name: fouke-2025
type: reproduction
title: Optomotor swimming of zebrafish and Danionella cerebrum (Fouke et al. 2025)
description: Tests the freely swimming findings of Fouke, He, Loring and Naumann (2025) on dandiset
  001453, which holds the tracking data of 25 zebrafish and 12 Danionella cerebrum larvae during the
  optomotor protocol. It compares swimming speed, turning and angular acceleration between species
  and stimuli, the response to monocular stimuli, and how steady the swimming is. The imaging and
  head-fixed tail tracking of the paper's Figures 2 to 4 are not in the dandiset.
[... 270 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -l "protocol: pilot-1[45]" attempts/* | head; ls schemas; sed -n '/^## DANDI/,/^## [A-Z]/p' docs/archives.md | head -100
```

```
attempts/andrews-2024-01.yaml
attempts/asari-2009-01.yaml
attempts/brinke-2017-01.yaml
attempts/brudner-2026-01.yaml
attempts/burman-2023-01.yaml
attempts/dana-2016-01.yaml
attempts/danish-2017-01.yaml
attempts/dijk-2018-01.yaml
attempts/elie-2019-01.yaml
attempts/gao-2018-01.yaml
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
## DANDI

- **Datasets.** A dandiset, identified by six digits (`000003`). Targets are the
  public dandisets whose metadata names a paper (`targets/dandisets.json`, built
  by `tools/build_targets.py` and refreshed daily by the Track DANDI workflow).
- **Versions.** A published version (`0.220126.1855`) is fixed and has a DOI,
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls -t attempts | head -3; grep -l "protocol: pilot-15" attempts/* | head -3; f=$(grep -l "protocol: pilot-15" attempts/* | head -1); echo $f; head -60 $f; grep -n "assumed\|methods_unavailable\|found:" $f | head; ls entries/$(basename $f -01.yaml)
```

```
zhuang-2025-01.yaml
zhu-2022-01.yaml
zhai-2025-01.yaml
attempts/asari-2009-01.yaml
attempts/dana-2016-01.yaml
attempts/danish-2017-01.yaml
attempts/asari-2009-01.yaml
schema_version: 3
id: asari-2009-01
datasets:
- archive: crcns
  id: ac-1
  version: unversioned
  doi: 10.6080/K0KW5CXR
  relation: primary
paper: doi:10.1152/jn.00577.2009
date: '2026-11-13'
entry: asari-2009
provenance:
  kind: agent
[... 65 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 540,620p attempts/asari-2009-01.yaml; cat entries/asari-2009/entry.yaml entries/asari-2009/README.md; python -c "import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s,indent=1)[:6000])"
```

```
- kind: data_missing
  statement: The example recording of Figure 7 (a natural sound probe after DMRs in 0.625-2.5, 2.5-10 and 10-40 kHz) is not in the data
    set; no recording has DMR conditioning stimuli in those single bands. The DMR frequency variants in it are 2-octave bands from 0.25
    to 32 kHz in 1-octave steps.
- kind: other
  about: data
  statement: The data set holds 145 A1 whole-cell cells and 14 MGB cells, against the 194 current-clamp and 16 MGB cells the paper recorded.
    Its natural sound and MGB groups hold exactly the 39 cells with 305 probes and the 14 cells with 93 probes the paper analysed. The
    synthetic sound group holds 96 cells; with the natural sound group, 133 cells meet the paper's rule for analysis against its 123,
    and the ensembles split differently from the paper's list (DMR 15 cells against 6, MHT 26 against 39, and 14 cells with SoundTrans
    variants of natural sounds).
- kind: metadata_insufficient
  statement: 'Which conditioning stimuli of a synthetic sound recording vary which sound property (the sets behind Table 1 and Figure
    8) is listed in the notes of only the 19-stimulus MHT recordings. For the others it has to be rebuilt from the stimulus parameters
    and descriptions. Rebuilt with one test per set for AM and FM, the sets give the five probe totals of Table 1, but the split by
    probe type does not match: 82 of the 96 AM tests and all 82 FM tests have a natural sound probe, and only 2 recordings have MHT
    probes, where Table 1 gives 71 and 57 MHT-probe tests.'
- kind: metadata_error
  statement: Summary.mat lists two cells, 20060314-ha1-001 and 20060320-ha3-003, in both the natural sound and the synthetic sound group,
    so their tuning-curve files are named twice. The recordings are the same files; no two files hold identical traces.
[... 374 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
nb=json.load(open('entries/asari-2009/reproduce_asari_2009.ipynb'))
print(nb['metadata'])
for c in nb['cells'][:6]:
    print(c['cell_type'],c.get('metadata'),''.join(c['source'])[:1500]);print('----')
E
grep -n "def \|tag\|sanity" tools/entry.py | head -80
```

```
{'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}}
markdown {} # Reproducing Asari & Zador (2009) from CRCNS ac-1

**Paper.** Asari H, Zador AM (2009). Long-lasting context dependence constrains neural encoding
models in rodent auditory cortex. *J Neurophysiol* 102:2638-2656.
[doi:10.1152/jn.00577.2009](https://doi.org/10.1152/jn.00577.2009). The claims file
(`claims/asari-2009.yaml`) was written from the version of record; the online supplement was not
available to its readers.

**Data set.** CRCNS ac-1 (Asari, Wehr, Machens & Zador 2009),
[doi:10.6080/K0KW5CXR](https://doi.org/10.6080/K0KW5CXR), read from the public bucket
`crcnsarchive` (`ac-1/`). CRCNS data sets are not versioned: the version is recorded as
`unversioned`, and the MD5 sums the data set publishes in `checksums.md5` for the three zip files
read here are printed below, so that a later change can be detected. There is no other version to
choose; the paper cites the data set by no version.

**What the data set holds.** Asari's recordings: whole-cell current-clamp recordings in A1 and
cell-attached recordings in MGB, one MATLAB file per recording, with the analysis code the
paper used (`asari/Tools/CxtDep.m`). Wehr's recordings of Machens et al. (2004) are in the same
data set. No voltage-clamp recording is in it (checked below).
[... 112 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,75p tools/entry.py; sed -n 179,420p tools/entry.py; sed -n 600,640p tools/entry.py
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
[... 337 more lines not kept]
```

**Agent**

Now the paper.

**Agent calls Bash**

```bash
cd  wc -c paper/*; cat paper/10.1038-s41597-020-0415-9.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/ce3dc8ea-96db-4b0d-ab7a-348e333948cf/tool-results/bq8xusi0h.txt"
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
8	2628 sdata Scientific Data Sci Data Nature Publishing Group PMC7055261 7055261 7055261 32132545 10.1038/s41597-020-0415-9 A NWB-based dataset and processing pipeline of human single-neuron activity during a declarative memory task Chandravadia N 1 Liang D 2 Schjetnan A G P 3 Carlson A 1 Faraut M 1 Chung J M 4 Reed C M 4 Dichter B 5 6 Maoz U 2 7 Kalia S K 8 3 Valiante T A 3 8 Mamelak A N 1 Rutishauser U 1 4 7 9 10 ✉ 1 Department of Neurosurgery, Cedars-Sinai Medical Center, Los Angeles, CA USA 2 Institute for Interdisciplinary Brain and Behavioral Sciences, Crean College of Health and Behavioral Sciences, Schmid College of Science and Technology, Chapman University, Orange, CA USA 3 Krembil Brain Institute, Toronto Western Hospital, Toronto, Canada 4 Department of Neurology, Cedars-Sinai Medical Center, Los Angeles, CA USA 5 Biological Systems & Engineering Division, Lawrence Berkeley National Laboratory, Berkeley, CA USA 6 Department of Neurosurgery, Stanford University, Stanford, CA USA 7 Division of Biology and Biological Engineering, California Institute of Technology, Pasadena, CA USA 8 Division of Neurosurgery, Department of Surgery, University of Toronto, Toronto, Canada 9 Computational and Neural Systems Program, California Institute of Technology, Pasadena, CA USA 10 Center for Neural Science and Medicine, Department of Biomedical Science, Cedars-Sinai Medical Center, Los Angeles, CA USA ✉ Corresponding author. 4 3 2020 7 78 78 19 3 2020 © The Author(s) 2020 Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropri
[... 123 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat papers/datasets/chandravadia-2020.yaml; ls questions | grep chand; ls transcripts | grep chand; ls executed 2>/dev/null | head; curl -s -m 20 "https://api.dandiarchive.org/api/dandisets/000004/versions/0.220126.1852/" | head -c 3000
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/000004/versions/0.220126.1852/assets/?page_size=200" > assets.json; python -c "
import json;d=json.load(open('assets.json'));print(d['count']);
tot=0
for a in d['results']: print(a['path'],a['size'],a['asset_id']); tot+=a['size']
print(tot/1e9)"; curl -s "https://api.dandiarchive.org/api/dandisets/000004/versions/0.220126.1852/" | python -c "import json,sys;d=json.load(sys.stdin);print(d['description']);print(d.get('relatedResource'));print(d['assetsSummary'])"; curl -s "https://api.dandiarchive.org/api/dandisets/000004/versions/" | python -m json.tool | grep -E '"version"|"modified"|"created"'
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  which python uv; python --version; python -c "import pynwb, remfile, h5py; print(pynwb.__version__)" 2>&1; ls .venv 2>/dev/null | head
```

```
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
/opt/hostedtoolcache/Python/3.13.18/x64/bin/uv
Python 3.13.18
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pynwb, remfile, h5py; print(pynwb.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pynwb'
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q pynwb remfile h5py numpy pandas scipy matplotlib requests statsmodels 2>&1 | tail -3; python -c "import pynwb;print(pynwb.__version__)"
```

```
4.2.0
Shell cwd was reset to
```

**Agent**

Environment ready; I'm now surveying one NWB file's full contents (step 1.1).

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > survey.py <<'E'
import h5py, remfile, requests, time, sys
aid=sys.argv[1]
t=time.time()
url=requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=True).url
f=h5py.File(remfile.File(url),'r')
def show(name,obj):
    if isinstance(obj,h5py.Dataset):
        if name.startswith('stimulus/presentation/') and not name.endswith(('stimuli_learn_1/data','stimuli_recog_1/data')): return
        print(name,obj.shape,obj.dtype,dict(obj.attrs) if obj.size<5 or 'data' in name else {k:v for k,v in obj.attrs.items() if k in('description','unit','conversion','rate','neurodata_type')})
    else:
        if name.startswith('stimulus/presentation/') and not name.endswith(('stimuli_learn_1','stimuli_recog_1','presentation')): return
        print('G',name,{k:v for k,v in obj.attrs.items() if k not in ('object_id',)})
f.visititems(show)
for k in ['session_description','identifier','session_start_time','experiment_description','institution','lab']:
    print(k, f[k][()] if k in f else None)
print(time.time()-t)
E
python survey.py 757c3982-8e4c-466d-9a9f-73793262268c 2>&1 | head -150
```

```
G acquisition {}
G acquisition/events {'comments': 'no comments', 'description': ' The events coorespond to the TTL markers for each trial. For the learning trials, the TTL markers \n            are the following: 55 = start of the experiment, 1 = stimulus ON, 2 = stimulus OFF, 3 = Question Screen Onset [“Is this an animal?”], \n            20 = Yes (21 = NO) during learning, 6 = End of Delay after Response, 66 = End of Experiment. For the recognition trials, \n            the TTL markers are the following: 55 = start of experiment, 1 = stimulus ON, 2 = stimulus OFF, 3 = Question Screen Onset [“Have you seen this image before?”], \n            31:36 = Confidence (Yes vs. No) response [31 (new, confident), 32 (new, probably), 33 (new, guess), 34 (old, guess), \n            35 (old, probably), 36 (old, confident)], 66 = End of Experiment', 'namespace': 'core', 'neurodata_type': 'AnnotationSeries'}
acquisition/events/data (1004,) object {'conversion': np.float64(1.0), 'resolution': np.float64(-1.0), 'unit': 'n/a'}
acquisition/events/timestamps (1004,) float64 {'unit': 'seconds'}
G acquisition/experiment_ids {'comments': 'no comments', 'description': 'The experiment_ids coorespond to the encoding (i.e., learning) or recogniton trials. The learning trials are demarcated by: 80. The recognition trials are demarcated by: 81. ', 'namespace': 'core', 'neurodata_type': 'TimeSeries'}
acquisition/experiment_ids/data (1004,) float64 {'conversion': np.float64(1.0), 'resolution': np.float64(-1.0), 'unit': 'NA'}
acquisition/experiment_ids/timestamps (1004,) float64 {'unit': 'seconds'}
G analysis {}
file_create_date (1,) object {}
G general {}
general/data_collection () object {}
G general/devices {}
G general/devices/Neuralynx-cheetah {'namespace': 'core', 'neurodata_type': 'Device'}
general/experiment_description () object {}
G general/extracellular_ephys {}
G general/extracellular_ephys/Neuralynx-cheetah-microwires-1 {'description': 'Behnke Fried/Micro Inner Wire Bundle (Behnke-F
[... 85 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'E'
import h5py, remfile, requests, numpy as np
aid="757c3982-8e4c-466d-9a9f-73793262268c"
url=requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=True).url
f=h5py.File(remfile.File(url),'r')
for g in ['stimulus/presentation','stimulus/templates']:
    ks=list(f[g].keys()); print(g,len(ks),ks[:5])
    if ks:
        o=f[g][ks[0]]; print(o, dict(o.attrs)); 
        if isinstance(o,h5py.Group):
            for k in o: print(' ',k,o[k].shape if hasattr(o[k],'shape') else '', o[k].dtype if hasattr(o[k],'dtype') else '', o[k].chunks if hasattr(o[k],'chunks') else '', o[k].compression if hasattr(o[k],'compression') else '')
for k in ['general/subject/age','general/subject/description','general/subject/sex','general/subject/species','general/subject/subject_id','general/keywords','general/related_publications','general/data_collection','general/experiment_description','general/institution','general/lab','timestamps_reference_time','file_create_date']:
    print(k, f[k][()])
t=f['intervals/trials']
import pandas as pd
d={k:t[k][()] for k in t if k!='id'}
df=pd.DataFrame({k:[x.decode() if isinstance(x,bytes) else x for x in v] for k,v in d.items()})
pd.set_option('display.width',250); pd.set_option('display.max_columns',20)
print(df.head(5)); print(df.iloc[100:105])
print(df.stim_phase.value_counts(), df.category_name.value_counts(), df.new_old_labels_recog.value_counts(), df.response_value.value_counts())
print(f['general/extracellular_ephys/electrodes/filtering'][:3], f['general/extracellular_ephys/electrodes/location'][:], f['general/extracellular_ephys/electrodes/imp'][:], f['general/extracellular_ephys/electrodes/origChannel'][:], f['general/extracellular_ephys/electrodes/x'][:])
print(f['units/waveform_mean_sampling_rate'][:5].ravel(), f['units/electrodes'][:], f['units/electrodes_index'][:], f['units/IsolationDist'][:], f['units/SNR'][:])
ev=f['acquisition/events/data'][:]; print(ev[:30]); print(f['acquisition/experiment_ids/data'][:5], np.unique(f['acquisition/experiment_ids/data'][:]))
E
```

```
stimulus/presentation 1 ['StimulusPresentation']
<HDF5 group "/stimulus/presentation/StimulusPresentation" (7 members)> {'comments': 'no comments', 'description': 'no description', 'namespace': 'core', 'neurodata_type': 'OpticalSeries', 'object_id': 'fec796c7-3bf7-40de-b5d4-01de89c01734'}
  data (200, 400, 300, 3) uint8 None None
  dimension (3,) int32 None None
  distance () float64 None None
  field_of_view (3,) float64 None None
  format () object None None
  orientation () object None None
  timestamps (200,) float64 None None
stimulus/templates 0 []
general/subject/age b'55'
general/subject/description b'Right Mesial Temporal'
general/subject/sex b'M'
general/subject/species b'Human'
general/subject/subject_id b'P9HMH'
general/keywords [b'Intracranial Recordings' b'Intractable Epilepsy'
 b'Single-Unit Recordings' b'Cognitive Neuroscience' b'Learning' b'Memory'
 b'Neurosurgery']
general/related_publications [b'Faraut et al. 2018, Scientific Data; Rutishauser et al. 2015, Nat Neurosci;']
general/data_collection b'learning: 80, recognition: 81'
[... 57 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/rutishauserlab/recogmem-release-NWB.git code && cd code && git checkout -q 1d95162 && git log -1 --format='%H %cd' && find . -type f \( -name "*.py" -o -name "*.m" -o -name "*.ipynb" -o -name "*.ini" \) | grep -v matnwb | head -100
```

```
1d95162d2672e71dd234a31e4b8d70017a289ee3 Tue Jan 14 12:07:46 2025 -0800
./setup.py
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
./RutishauserLabtoNWB/events/newolddelay/python/export/trial.py
./RutishauserLabtoNWB/events/newolddelay/python/export/cell.py
./RutishauserLabtoNWB/events/newolddelay/python/export/data.py
./RutishauserLabtoNWB/events/newolddelay/python/export/no2nwb_main.py
./RutishauserLabtoNWB/events/newolddelay/python/export/no2nwb.py
./RutishauserLabtoNWB/events/newolddelay/python/export/demo/demoExportEvents.py
./RutishauserLabtoNWB/events/newolddelay/python/export/demo/export.py
./RutishauserLabtoNWB/events/newolddelay/python/export/demo/demoImport.py
[... 82 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/RutishauserLabtoNWB/events/newolddelay/python/analysis && wc -l *.py && cat behavior.py helper.py | head -500
```

```
374 behavior.py
  385 behavior_all.py
  480 helper.py
   97 main.py
  423 single_neuron.py
 1759 total
import RutishauserLabtoNWB.events.newolddelay.python.analysis.helper as helper
import scipy.stats as stats
import logging
import matplotlib.pyplot as plt
import numpy as np

def plot_behavioral_graphs(*argv):

    """
    Input: Variable number of NWB sessions in the '~~~.nwb' format

    Output:

    Behavioral analysis, plotting six graphs:
[... 487 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/RutishauserLabtoNWB/events/newolddelay/python/analysis && sed -n 200,480p helper.py
```

```
F = 1 - 1/(2*n_new)
    if H == 0:
        H = 1/(2*n_old)
    if F == 0:
        F = 1/(2*n_new)

    return H, F

def cal_cumulative_d(nwbfile):
    """
    calculate cummulative d' values as well as z-transformed hit/false alarm rates. used to construct empirical ROCs constructed using different
    confidence ratings.

    the format of C is described in calcEmpiricalROC.m

    statsAll: each column is a confidence level. each row is d', zH, zF, H, F

    urut/oct06
    """
    typecounter = cal_typecounter(nwbfile)
[... 260 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/RutishauserLabtoNWB/events/newolddelay/python/analysis && sed -n 150,207p helper.py; cd ../../matlab/analysis/helpers; cat adjustHF.m calcZROCSlope.m calcMeanSEOfSample.m bootstrapMeanEqualTest.m NO_dynamic_lowHighSplit.m | grep -v "^\s*$"
```

```
according to Macmillan&Creelman, Eq 1.1, 1.2, 1.5;
    error estimation of d' is: Eq 13.4, 13.5

    """
    H = 0
    F = 0
    if n_old > 0:
        H = typecounters[0]/n_old
    if n_new > 0:
        F = typecounters[3]/n_new

    # % adjust
    # for perfect(1) and 0(all misses)
    # % acc
    # to
    # pp8
    H, F = adjustHF(H, F, n_new, n_old)

    zH = norm.ppf(H)
    zF = norm.ppf(F)
[... 260 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/RutishauserLabtoNWB/events/newolddelay/matlab/analysis/helpers && grep -v "^\s*$" NWB_behaviorSummary.m | head -250
```

```
% plots summary of new/old task behavior.
%
%doPlot: 0 no, 1 summary plot, 2 z-ROC plots
%
%urut/march09
%urut/aug18 split out from NO_DM_behaviorSummary.m and simplified.
function [T,allSlopes, AUC, isIncluded_exclMode1, accuracyHighLow, typeCountersSame] = NWB_behaviorSummary(NWBsessions, allLearnSessionsToUse, modeBehavior, doPlot, basepath, modeExcludeSlowRT)
T=[]; %decision threshold for each session. T(j)>= is OLD
Thigh=[];%decision threshold for a stimulus to be of high confidence
nrT=[];
allConfCountsTP=[]; %for each session, probability of each confidence button press
countersAv=[];
TP_FP_chosen=[]; %TP/FP at the picked decision point
Tp_FP_HighLowConf=[]; %TP/FP at the picked low/high confidence decision point
allSlopes=[]; % slope of line fit in z-ROC space
countersHistory=[]; %store all for later use in plotting
fitHistory=[];
errorRatesLearn=[]; %animal yes/no perc correct during learning
sessionCounters=[0 0 0]; %all, exclMode1, exclMode2
accuracyHighLow = []; % inclusionStatus high low
[... 222 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/RutishauserLabtoNWB/events/newolddelay/matlab/analysis/helpers && grep -v "^\s*$" NO_behavior_evaluateSessionStatus.m | head -80; grep -v "^\s*$" calcROC_AUC.m | head -40
```

```
%
% evaluates whether a particular session should be included or not for NO retrieval analysis
%
%newOldRecogLabels: ground truth. 0-new, 1-old
%
% AUC behavioral AUC
% respCounts raw response (1-6) to each trial
%
% enforceBehaviorExclusions : 0 include all; 1 include all with valid behavior; 2 include only those that distinguished high/low correctly
%
% rawAccuracies: high med low; accuracy separately for each conf level, without applying a high/low split
% rawAccuracies2: accuracy separately for high/low and for new/old.   order: Old high, Old med, Old low, New low, New med, New High
%
%urut/CSMC/oct13
function [isIncluded, AUC, percAccuracy_high, percAccuracy_low, TP, FP,respCounts,rawAccuracies, rawAccuracies2] = NO_behavior_evaluateSessionStatus(responses, newOldRecogLabels,enforceBehaviorExclusions)
if nargin<3
    enforceBehaviorExclusions=2;    
end
useDynamicSplitMode=0;
minAccuracyLow=0.55;
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/RutishauserLabtoNWB/events/newolddelay/matlab/analysis/helpers && grep -v "^\s*$" NWB_singleCellAnalysis_release.m | head -120; grep -v "^\s*$" extractPeriodCountsSimple.m | head -60; grep -v "^\s*$" NO_selectSigCells_simple.m | head -60
```

```
%
% Simplified version of the per-cell analysis function used for the new/old task using the NWB data format.
% This cell is a callback function for NWBrunForAllCellsInSession.m
%
%
%urut/aug16
function params = NWB_singleCellAnalysis_release( timestampsOfCell, figNr, brainAreaOfCell, plabel, params, varargin )
params.nrProcessed = params.nrProcessed+1;
%% parameters used
stepsize = 250;
normalizeCounts = 1; % convert to Hz (spikes/sec)
alphaLim = 0.01; % sig limit to trigger plotting
analysisMode = params.analysisMode;   % 1 is recog, 2 is learn  (which part of the task is analyzed)
%% prepare trial indices
stimOnset = 1000; %relative to begin of trial,when does the stimulus come on.
stimLength = 1000; 
delayPeriod = 500; %how long till the question comes on
trialLength = stimOnset + stimLength + delayPeriod;
if analysisMode==1
    %Recognition part
[... 157 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/RutishauserLabtoNWB/events/newolddelay/matlab/analysis && grep -n -i "minRate\|minNrTrials\|enforceBehav\|alphaLim\|NO_selectSigCells\|areaToProcess\|sessions\b" NWBneural_main.m helpers/NWBneural_loopOverSessions_release.m | head -40; cd ../../python/analysis; grep -n "def \|anova\|f_oneway\|bootstrap\|0.2\|1.2\|1.7\|200\|1700" single_neuron.py | head -40
```

```
NWBneural_main.m:22:%List of sessions to analyze (for testing purposes)
NWBneural_main.m:25:runAllAvailableSesssions = 0 ; % enable to process all available sessions (not just the one(s) specified above). Uses NWB_listOf_allUsable
NWBneural_main.m:29:%% Section 2: Which sessions to process 
NWBneural_main.m:48:    [NWBsessions] = convertIni2NOsessions(keys);  
NWBneural_main.m:49:    %Get list of all usable sessions to use (see defineNOsessions_release.ini)
NWBneural_main.m:72:%-- behavior summary figure (all sessions)
NWBneural_main.m:73:if length(allSessionsToUse)>1    % only works if at least two sessions are analyzed
NWBneural_main.m:77:    decisionThresholds = NWB_behaviorSummary(NWBsessions, allSessionsToUse, modeBehavior, doPlot_behavior, basepathData, modeExcludeSlowRT);
NWBneural_main.m:92:[totStats,cellStatsAll] = NWBneural_loopOverSessions_release(allSessionsToUse, NWBsessions, basepathData,analysisMode, paramsInPreset ); 
helpers/NWBneural_loopOverSessions_release.m:2:% For all sessions, run cell selection
helpers/NWBneural_loopOverSessions_release.m:6:% totStats and cellStatsAll contain results over all processed sessions
helpers/NWBneural_loopOverSessions_release.m:9:function [totStats,cellStatsAll] = NWBneural_loopOverSessions_release(allRecogSessionsToUse, NOsessions, basepath, analysisMode, paramsInPreset ) 
helpers/NWBneural_loopOverSessions_release.m:17:    NOsessionRecog = NOsessions(NOind);
helpers/NWBneural_loopOverSessions_release.m:30:    paramsIn.diagnosisCode = NOsessions(NOind).diagnosisCode;
helpers/NWBneural_loopOverSessions_release.m:38:    % aggregate results across sessions for later analysis
4:from scipy.stats import f_oneway
14:    def __init__(self):
22:    def vs_test(self):
34:        # The window that we want to look at is from 200 ms after stim on until 1500 ms after.
37:                cat_1.append(trial.win_spike_rate(self.spike_timestamps, 200, 1700))
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/RutishauserLabtoNWB/events/newolddelay; sed -n 60,103p python/analysis/single_neuron.py; sed -n 300,423p python/analysis/single_neuron.py; sed -n 20,70p matlab/analysis/NWBneural_main.m
```

```
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
                new = np.append(new, trial.win_spike_rate(self.spike_timestamps, 200, 1700))
            elif (trial.label == 1) & (trial.response >= 4.):
                old = np.append(old, trial.win_spike_rate(self.spike_timestamps, 200, 1700))

        # Ready for bootstrapping
        m_ = len(new)
[... 199 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR/code/RutishauserLabtoNWB/events/newolddelay; python3 -c "
import json;nb=json.load(open('python/analysis/demo/plotFigure5.ipynb'))
for c in nb['cells']:
    s=''.join(c['source'])
    if any(k in s for k in ['VS','MS','18.4','19.4','percent','AUC','ttest','auc']): print('---',s[:1500])
" | head -150; head -40 defineNOsessions_release.ini; grep -c "^\[" defineNOsessions_release.ini
```

```
Sat Nov 14 13:06:18 UTC 2026
--- 
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
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s -m 30 "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5810422/fullTextXML" -o faraut.xml; ls -la faraut.xml; python3 - <<'E'
import xml.etree.ElementTree as ET
r=ET.parse('faraut.xml').getroot()
for tw in r.iter('table-wrap'):
    lab=tw.find('label'); cap=tw.find('caption')
    print(tw.get('id'), lab.text if lab is not None else None, ''.join(cap.itertext())[:200] if cap is not None else None)
    rows=list(tw.iter('tr')); print(len(rows))
    for tr in rows[:6]: print([''.join(td.itertext()) for td in tr])
E
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s -m 30 "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7055261/fullTextXML" -o chand.xml; ls -la chand.xml; python3 - <<'E'
import xml.etree.ElementTree as ET
r=ET.parse('chand.xml').getroot()
for tw in r.iter('table-wrap'):
    lab=tw.find('label'); 
    print(tw.get('id'), lab.text if lab is not None else None)
    rows=list(tw.iter('tr')); print(len(rows))
    for tr in rows[:4]+rows[-5:]: print([''.join(td.itertext()) for td in tr])
E
```

Result: the fetched text is not kept.

**Agent**

Paper code and reference tables are reachable. Now writing the helper module's loader and surveying all 87 files.

**Agent calls Bash**

```bash
mkdir -p entries/chandravadia-2020; cd $TMPDIR && . dev/bin/activate && python - <<'E'
import h5py, remfile, requests, numpy as np
aid="757c3982-8e4c-466d-9a9f-73793262268c"
url=requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=True).url
f=h5py.File(remfile.File(url),'r')
st=f['units/spike_times'][:]; idx=f['units/spike_times_index'][:]
print(st[:5], st.min(), st.max(), f['intervals/trials/start_time'][[0,-1]], f['intervals/trials/stop_time'][-1])
ev=f['acquisition/events/timestamps'][:]; print(ev[:3], ev[-1])
print(np.all(np.diff(st[:idx[0]])>=0))
print(f['intervals/trials/stim_on_time'][:3], f['intervals/trials/start_time'][:3])
print(f['units/electrodes'].attrs['table'], f['units/electrodes'].attrs.keys())
print(f['stimulus/presentation/StimulusPresentation/timestamps'][:3])
print(f['intervals/trials/response_value'][100:110])
E
```

```
[4236.206722 4236.664002 4236.682842 4236.687362 4236.698042] 4234.706802 5609.797242 [4218.311402 5614.392922] 5617.406322
[4217.079282 4218.311402 4219.308442] 5617.408682
True
[4218.311402 4222.039402 4226.937522] [4218.311402 4222.039402 4226.937522]
<HDF5 object reference> <KeysViewHDF5 ['description', 'namespace', 'neurodata_type', 'object_id', 'table']>
[4218.311402 4222.039402 4226.937522]
[31. 36. 31. 31. 36. 36. 31. 35. 32. 31.]
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "entries/chandravadia-2020/chandravadia.py",
 "content": "\"\"\"Loading and measures for dandiset 000004 (Chandravadia et al. 2020, Scientific Data 7, 78).\n\nThe dandiset holds one NWB file per session of the new/old recognition memory task: the\ntrials table, the TTL events and experiment ids, the electrodes table, the units table with\nspike times and mean waveforms, and the 200 stimulus images. Files are streamed from the\narchive with remfile and h5py; the images are never read, as nothing here needs their pixels.\n\nWhere each parameter comes from:\n\n- Recognition trials are the rows with stim_phase \"recog\"; the confidence response is\n  response_value minus 30 (1 = new, confident; 6 = old, confident); \"old\" is label 1. These\n  are the claims file's method choices (its opening comment). The notebook checks the\n  response against the TTL codes 31 to 36 of the events stream, which is what the paper's\n  code reads (helper.extract_recog_responses).\n- Firing rates are spike counts in a window divided by its length (claims file). The main\n  window is 200 to 1200 ms after stimulus onset, from the paper (\"a 1 s long window starting\n  200 ms after stimulus onset\", Technical Validation, proportion of selective cells,\n  paragraph 2). The code's window, 200 to 1700 ms (single_neuron.py, vs_test and ms_test;\n  NWB_singleCellAnalysis_release.m, countStimulus_long), is a variant. Spikes are counted in\n  the half-open interval (start, end], as extractPeriodCountsSimple.m does; this is a\n  standard choice that cannot change a result at the precision of the spike times.\n- The ROC follows the paper's code (helper.cal_cumulative_d, cal_typecounter, adjustHF and\n  cal_auc in recogmem-release-NWB at commit 1d95162): cumulative hit and false alarm rates\n  from confidence 6 down to 1, rates of 0 or 1 adjusted to 1/(2n) or 1 - 1/(2n), AUC by the\n  trapezoid rule with (0,0) and (1,1) added (claims file).\n- The z-ROC slope is the regression of z(H) on z(F) over the five interior points\n  (calcZROCSlope.m; claims file).\n- The fixed confidence split is that of NO_behavior_evaluateSessionStatus.m (high = 1 or\n  6, low = 2 to 5); the dynamic split is helper.dynamic_split of the Python code, and the\n  MATLAB NO_dynamic_lowHighSplit.m, which differs from it in split mode 1, is a variant.\n- The bootstrap test of equal means is bootstrapMeanEqualTest.m (Efron and Tibshirani,\n  algorithm 16.2), two-sided, 1000 resamples, with the generator the notebook passes in\n  (a fixed seed is a standard choice that cannot change a result beyond resampling noise).\n\"\"\"\n\nfrom __future__ import annotations\n\nimport re\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nimport requests\nfrom scipy import stats\n\nDANDISET = \"000004\"\nVERSION = \"0.220126.1852\"\nAPI = \"https://api.dandiarchive.org/api\"\nEUROPEPMC = \"https://www.ebi.ac.uk/europepmc/webservices/rest/{}/fullTextXML\"\nPAPER_PMC = \"PMC7055261\"       # this paper, doi:10.1038/s41597-020-0415-9\nFARAUT_PMC = \"PMC5810422\"      # Faraut et al. 2018, doi:10.1038/sdata.2018.10\n\nWINDOW_METHODS = (0.2, 1.2)    # paper, Technical Validation, proportion of selective cells\nWINDOW_CODE = (0.2, 1.7)       # paper's code, single_neuron.py and NWB_singleCellAnalysis_release.m\n\n\ndef list_assets() -> pd.DataFrame:\n    \"\"\"Every asset of the pinned version, with its path, size and identifier.\"\"\"\n    url = f\"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200\"\n    rows = []\n    while url:\n        page = requests.get(url, timeout=60).json()\n        rows += [dict(path=a[\"path\"], size=a[\"size\"], asset_id=a[\"asset_id\"]) for a in page[\"results\"]]\n        url = page.get(\"next\")\n    return pd.DataFrame(rows).sort_values(\"path\").reset_index(drop=True)\n\n\ndef version_metadata() -> dict:\n    return requests.get(f\"{API}/dandisets/{DANDISET}/versions/{VERSION}/\", timeout=60).json()\n\n\ndef asset_url(asset_id: str) -> str:\n    return requests.head(f\"{API}/assets/{asset_id}/download/\", allow_redirects=True, timeout=60).url\n\n\ndef _str(x):\n    return x.decode() if isinstance(x, bytes) else x\n\n\ndef _strs(a):\n    return np.array([_str(x) for x in a], dtype=object)\n\n\ndef read_session(asset_id: str) -> dict:\n    \"\"\"Read everything the analysis uses from one file: metadata, trials, events, electrodes, units.\n\n    The stimulus images are not read; only their array shape is recorded.\"\"\"\n    f = h5py.File(remfile.File(asset_url(asset_id)), \"r\")\n    out = {\"asset_id\": asset_id}\n    for k in [\"identifier\", \"session_description\", \"session_start_time\", \"timestamps_reference_time\"]:\n        out[k] = _str(f[k][()])\n    for k in [\"data_collection\", \"experiment_description\", \"institution\", \"lab\"]:\n        out[k] = _str(f[\"general/\" + k][()]) if \"general/\" + k in f else None\n    out[\"subject\"] = {k: _str(f[\"general/subject/\" + k][()]) for k in f[\"general/subject\"]}\n    out[\"devices\"] = list(f[\"general/devices\"].keys())\n\n    t = f[\"intervals/trials\"]\n    out[\"trial_columns\"] = [_str(c) for c in t.attrs[\"colnames\"]]\n    cols = {}\n    for k in t:\n        if k == \"id\":\n            continue\n        v = t[k][()]\n        cols[k] = _strs(v) if v.dtype.kind in \"OS\" else v\n    out[\"trials\"] = pd.DataFrame(cols)\n    out[\"trial_descriptions\"] = {k: _str(t[k].attrs.get(\"description\", \"\")) for k in t if k != \"id\"}\n\n    ev = f[\"acquisition/events\"]\n    out[\"events\"] = np.array([float(_str(x)) for x in ev[\"data\"][()]])\n    out[\"events_t\"] = ev[\"timestamps\"][()]\n    out[\"events_description\"] = _str(ev.attrs.get(\"description\", \"\"))\n    ex = f[\"acquisition/experiment_ids\"]\n    out[\"expids\"] = ex[\"data\"][()]\n    out[\"expids_t\"] = ex[\"timestamps\"][()]\n    out[\"expids_description\"] = _str(ex.attrs.get(\"description\", \"\"))\n\n    e = f[\"general/extracellular_ephys/electrodes\"]\n    out[\"electrode_columns\"] = [_str(c) for c in e.attrs[\"colnames\"]]\n    ecols = {}\n    for k in e:\n        if k == \"group\":\n            continue\n        v = e[k][()]\n        ecols[k] = _strs(v) if v.dtype.kind in \"OS\" else v\n    out[\"electrodes\"] = pd.DataFrame(ecols)\n\n    u = f[\"units\"]\n    out[\"unit_columns\"] = [_str(c) for c in u.attrs[\"colnames\"]]\n    out[\"unit_datasets\"] = sorted(u.keys())\n    st, si = u[\"spike_times\"][()], u[\"spike_times_index\"][()]\n    starts = np.r_[0, si[:-1]]\n    out[\"spikes\"] = [st[a:b] for a, b in zip(starts, si)]\n    units = pd.DataFrame({\"id\": u[\"id\"][()]})\n    for k in [\"origClusterID\", \"IsolationDist\", \"IsolDist\", \"SNR\"]:\n        if k in u:\n            units[k] = u[k][()]\n    if \"waveform_mean_sampling_rate\" in u:\n        sr = u[\"waveform_mean_sampling_rate\"][()]\n        units[\"waveform_sampling_rate\"] = sr.reshape(len(sr), -1)[:, 0]\n    for k in [\"waveform_mean_encoding\", \"waveform_mean_recognition\"]:\n        if k in u:\n            w = u[k][()]\n            units[k + \"_samples\"] = w.shape[1] if w.ndim > 1 else 0\n            units[k + \"_finite\"] = np.isfinite(w).all(axis=1) if w.ndim > 1 else False\n    eidx, el = u[\"electrodes_index\"][()], u[\"electrodes\"][()]\n    estarts = np.r_[0, eidx[:-1]]\n    units[\"n_electrodes\"] = eidx - estarts\n    units[\"electrode_row\"] = [el[a] if b - a >= 1 else -1 for a, b in zip(estarts, eidx)]\n    units[\"n_spikes\"] = [len(s) for s in out[\"spikes\"]]\n    out[\"units\"] = units\n    p = \"stimulus/presentation\"\n    out[\"stimulus_series\"] = {k: f[p][k][\"data\"].shape for k in f[p] if \"data\" in f[p][k]}\n    f.close()\n    return out\n\n\ndef read_all(asset_ids, workers: int = 6) -> list[dict]:\n    with ThreadPoolExecutor(workers) as ex:\n        return list(ex.map(read_session, asset_ids))\n\n\ndef parse_identifier(identifier: str) -> tuple[str, int]:\n    \"\"\"'H09_5' -> ('H09', 5): the subject label and the session id (NOID).\"\"\"\n    label, sid = identifier.rsplit(\"_\", 1)\n    return label, int(sid)\n\n\ndef table_label(subject_id: str) -> str:\n    \"\"\"The dandiset's subject_id in the paper's notation: P9HMH -> H09, P24CS -> C24, TWH088 -> T88.\"\"\"\n    m = re.fullmatch(r\"P(\\d+)(HMH|CS)\", subject_id)\n    if m:\n        return (\"H\" if m[2] == \"HMH\" else \"C\") + f\"{int(m[1]):02d}\"\n    m = re.fullmatch(r\"TWH(\\d+)\", subject_id)\n    if m:\n        return f\"T{int(m[1])}\"\n    return subject_id\n\n\ndef variant_of(paths) -> set:\n    \"\"\"Task variant from the image folder of external_image_file (newolddelay, newolddelay2, newolddelay3).\"\"\"\n    out = set()\n    for p in paths:\n        folder = re.split(r\"[\\\\/]\", str(p))[0].lower()\n        m = re.fullmatch(r\"newolddelay(\\d?)\", folder)\n        out.add(int(m[1]) if m and m[1] else (1 if m else folder))\n    return out\n\n\n# --- tables from the papers (Europe PMC full text) ------------------------------------------\n\ndef europepmc_tables(pmc: str) -> dict:\n    \"\"\"The tables of an open access article, by label, as lists of rows of cell texts.\"\"\"\n    import xml.etree.ElementTree as ET\n    root = ET.fromstring(requests.get(EUROPEPMC.format(pmc), timeout=120).content)\n    out = {}\n    for tw in root.iter(\"table-wrap\"):\n        lab = tw.find(\"label\")\n        rows = [[\"\".join(td.itertext()).strip() for td in tr] for tr in tw.iter(\"tr\")]\n        if lab is not None and lab.text not in out:\n            out[lab.text.strip()] = rows\n    return out\n\n\ndef session_table(rows) -> pd.DataFrame:\n    \"\"\"One row per (subject, session) from a patients table: ID, session IDs, variants, age, sex, diagnosis.\"\"\"\n    recs = []\n    for r in rows:\n        if len(r) < 7 or not re.fullmatch(r\"[HCT]\\d+\", r[0]):\n            continue\n        sids = [int(s) for s in re.findall(r\"\\d+\", r[2])]\n        vars_ = [int(s) for s in re.findall(r\"\\d+\", r[3])]\n        for k, s in enumerate(sids):\n            recs.append(dict(label=r[0], session=s, variant=vars_[k] if k < len(vars_) else np.nan,\n                             n_sessions=int(r[1]), age=int(r[4]), sex=r[5], diagnosis=r[6]))\n    return pd.DataFrame(recs)\n\n\n# --- behaviour --------------------------------------------------------------------------------\n\ndef recog(trials: pd.DataFrame) -> pd.DataFrame:\n    \"\"\"Recognition trials with the confidence response (1-6) and the label (1 = old under the code's reading).\"\"\"\n    r = trials[trials.stim_phase == \"recog\"].copy()\n    r[\"conf\"] = r.response_value - 30\n    r[\"label\"] = pd.to_numeric(r.new_old_labels_recog, errors=\"coerce\")\n    return r\n\n\ndef adjust_hf(H, F, n_old, n_new):\n    if H == 1:\n        H = 1 - 1 / (2 * n_old)\n    if F == 1:\n        F = 1 - 1 / (2 * n_new)\n    if H == 0:\n        H = 1 / (2 * n_old)\n    if F == 0:\n        F = 1 / (2 * n_new)\n    return H, F\n\n\ndef cumulative_roc(conf, is_old):\n    \"\"\"Hit and false alarm rates cumulated from confidence 6 down to 1 (helper.cal_cumulative_d).\"\"\"\n    conf, is_old = np.asarray(conf), np.asarray(is_old, bool)\n    n_old, n_new = is_old.sum(), (~is_old).sum()\n    H, F = [], []\n    for c in range(6, 0, -1):\n        sel = conf >= c\n        h, f = adjust_hf((sel & is_old).sum() / n_old, (sel & ~is_old).sum() / n_new, n_old, n_new)\n        H.append(h)\n        F.append(f)\n    return np.array(H), np.array(F)\n\n\ndef auc(H, F):\n    \"\"\"Trapezoid AUC with (0,0) and (1,1) added (helper.cal_auc).\"\"\"\n    TP, FP = list(H), list(F)\n    if TP[0] != 0 or FP[0] != 0:\n        TP, FP = [0] + TP, [0] + FP\n    if TP[-1] != 1 or FP[-1] != 1:\n        TP, FP = TP + [1], FP + [1]\n    a = 0.0\n    for i in range(1, len(TP)):\n        a += (FP[i] - FP[i - 1]) * TP[i - 1] + 0.5 * (TP[i] - TP[i - 1]) * (FP[i] - FP[i - 1])\n    return a\n\n\ndef zroc_slope(H, F):\n    \"\"\"Slope of z(H) on z(F) over the five interior points (calcZROCSlope.m).\"\"\"\n    x, y = stats.norm.ppf(F[:5]), stats.norm.ppf(H[:5])\n    return np.polyfit(x, y, 1)[0]\n\n\ndef accuracy_fixed(conf, is_old):\n    \"\"\"High = 1 or 6, low = 2 to 5 (NO_behavior_evaluateSessionStatus.m, fixed threshold).\"\"\"\n    conf, is_old = np.asarray(conf), np.asarray(is_old, bool)\n    high, low = (conf == 1) | (conf == 6), (conf >= 2) & (conf <= 5)\n    correct = ((conf <= 3) & ~is_old) | ((conf >= 4) & is_old)\n    ah = (correct & high).sum() / high.sum() if high.sum() else np.nan\n    al = (correct & low).sum() / low.sum() if low.sum() else np.nan\n    return ah, al, int(high.sum()), int(low.sum())\n\n\ndef accuracy_dynamic(conf, is_old, flavour=\"python\"):\n    \"\"\"Dynamic split: helper.dynamic_split (python) or NO_dynamic_lowHighSplit.m (matlab).\n\n    Mode 1 is 1 | 2,3 | 4,5 | 6 and mode 2 is 1,2 | 3 | 4 | 5,6. In mode 1 the Python code\n    counts only response 4 (not 4 and 5) among the low old responses; the MATLAB code counts both.\"\"\"\n    conf, is_old = np.asarray(conf), np.asarray(is_old, bool)\n    rc = np.array([(conf == k).sum() for k in range(1, 7)])\n    s1 = rc[0] + rc[5] - (rc[1] + rc[4] + rc[2] + rc[3])\n    s2 = rc[0] + rc[5] + rc[1] + rc[4] - (rc[2] + rc[3])\n    mode = int(np.argmin(np.abs([s1, s2]))) + 1\n    if rc[0] == 0 or rc[5] == 0:\n        mode = 2\n    if rc[1] == 0 or rc[4] == 0:\n        mode = 1\n    if mode == 1:\n        high = (conf == 1) | (conf == 6)\n        low_old = (conf == 4) if flavour == \"python\" else ((conf == 4) | (conf == 5))\n        low = ((conf == 2) | (conf == 3)) | low_old\n    else:\n        high = (conf <= 2) | (conf >= 5)\n        low = (conf == 3) | (conf == 4)\n    correct = ((conf <= 3) & ~is_old) | ((conf >= 4) & is_old)\n    ah = (correct & high).sum() / high.sum() if high.sum() else np.nan\n    al = (correct & low).sum() / low.sum() if low.sum() else np.nan\n    return ah, al, mode, int(high.sum()), int(low.sum())\n\n\ndef code_inclusion(conf, a):\n    \"\"\"The Python code's inclusion rule for the accuracy analysis (helper.check_inclusion):\n    AUC at least 0.6, and at most one of the three new and one of the three old levels unused.\"\"\"\n    rc = np.array([(np.asarray(conf) == k).sum() for k in range(1, 7)])\n    return bool(a >= 0.6 and (rc[:3] == 0).sum() <= 1 and (rc[3:] == 0).sum() <= 1)\n\n\n# --- single neurons ---------------------------------------------------------------------------\n\ndef window_rates(spikes, onsets, window):\n    \"\"\"Spike counts in (onset + a, onset + b], divided by b - a (Hz), one per onset.\"\"\"\n    a, b = window\n    s = np.sort(spikes)\n    lo = np.searchsorted(s, onsets + a, side=\"right\")\n    hi = np.searchsorted(s, onsets + b, side=\"right\")\n    return (hi - lo) / (b - a)\n\n\ndef anova_p(rates, groups):\n    \"\"\"One-way ANOVA across groups; NaN when every rate is equal (no variance).\"\"\"\n    gs = [rates[groups == g] for g in np.unique(groups)]\n    if np.allclose(rates, rates[0]):\n        return np.nan\n    return stats.f_oneway(*gs).pvalue\n\n\ndef bootstrap_mean_equal(z, y, B, rng):\n    \"\"\"Two-sided bootstrap test of equal means (bootstrapMeanEqualTest.m, mode 1, no variance correction).\"\"\"\n    z, y = np.asarray(z, float), np.asarray(y, float)\n    n, m = len(z), len(y)\n    xm = np.r_[z, y].mean()\n    zt, yt = z - z.mean() + xm, y - y.mean() + xm\n    zs = zt[rng.integers(0, n, size=(B, n))].mean(axis=1)\n    ys = yt[rng.integers(0, m, size=(B, m))].mean(axis=1)\n    t = np.abs(zs - ys)\n    tob = z.mean() - y.mean()\n    return np.mean(t >= abs(tob))\n\n\ndef isi_fraction(spikes, limit=0.003, sort=True):\n    s = np.sort(spikes) if sort else np.asarray(spikes)\n    if len(s) < 2:\n        return np.nan\n    return np.mean(np.diff(s) < limit)\n"
}
```

```
File created successfully at: entries/chandravadia-2020/chandravadia.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > load.py <<'E'
import sys, time, pickle, resource
sys.path.insert(0,'entries/chandravadia-2020')
import chandravadia as C
t=time.time()
a=C.list_assets()
s=C.read_all(a.asset_id[:4]); print('4 files', time.time()-t)
t=time.time()
s=C.read_all(a.asset_id)
print('all', time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB')
pickle.dump((a,s),open('sessions.pkl','wb'))
E
python load.py
```

```
4 files 5.272508859634399
all 89.39168119430542 0.244108 GB
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'E'
import sys, pickle, numpy as np, pandas as pd, collections, hashlib
sys.path.insert(0,'entries/chandravadia-2020')
import chandravadia as C
a,S=pickle.load(open('sessions.pkl','rb'))
pd.set_option('display.width',250); pd.set_option('display.max_rows',200); pd.set_option('display.max_columns',30)
rows=[]
for p,s in zip(a.path,S):
    lab,sid=C.parse_identifier(s['identifier'])
    r=C.recog(s['trials'])
    rows.append(dict(path=p.split('/')[1][:45], ident=s['identifier'], desc=s['session_description'][:40], subj=s['subject']['subject_id'], tl=C.table_label(s['subject']['subject_id']), lab=lab, sid=sid,
      age=s['subject'].get('age'), sex=s['subject'].get('sex'), diag=s['subject'].get('description'), start=s['session_start_time'][:10], nunits=len(s['units']), ntr=len(s['trials']),
      nlearn=(s['trials'].stim_phase=='learn').sum(), nrec=len(r), var=C.variant_of(s['trials'].external_image_file), dc=s['data_collection'], expid=tuple(np.unique(s['expids'])), cats=s['trials'].stimCategory.nunique(), inst=s['institution'], stim=list(s['stimulus_series'].values())))
df=pd.DataFrame(rows); print(df.drop(columns=['path']).to_string())
print(df.nunits.sum(), df.subj.nunique(), df.lab.nunique())
print((df.tl!=df.lab).sum())
E
```

```
ident                                     desc    subj    tl   lab   sid age sex                            diag       start  nunits  ntr  nlearn  nrec  var                             dc         expid  cats                         inst                  stim
0       H10_7     New/Old recognition task for ID: 7.   P10HMH   H10   H10     7  37   M            Left Lateral Frontal  2006-09-01      38  200     100   100  {1}  learning: 80, recognition: 81  (80.0, 81.0)     5   Hunigton Memorial Hospital  [(200, 400, 300, 3)]
1       H11_9     New/Old recognition task for ID: 9.   P11HMH   H11   H11     9  16   M           Right Lateral Frontal  2006-11-01      25  200     100   100  {1}  learning: 80, recognition: 81  (80.0, 81.0)     5   Hunigton Memorial Hospital  [(200, 400, 300, 3)]
2      H14_17    New/Old recognition task for ID: 17.   P14HMH   H14   H14    17  31   M  Bilateral Independent Temporal  2007-06-01      23  200     100   100  {2}  learning: 83, recognition: 84  (83.0, 84.0)     5   Hunigton Memorial Hospital  [(200, 400, 300, 3)]
3      H14_18    New/Old recognition task for ID: 18.   P14HMH   H14   H14    18  31   M  Bilateral Independent Temporal  2007-06-01      33  150      50   100  {1}  learning: 80, recognition: 81  (80.0, 81.0)     5   Hunigton Memorial Hospital  [(150, 400, 300, 3)]
4      H15_21    New/Old recognition task for ID: 21.   P15HMH   H15   H15    21  45   M           Right Mesial Temporal  2007-09-01      14  150      50   100  {2}  learning: 83, recognition: 84  (83.0, 84.0)     5   Hunigton Memorial Hospital  [(150, 400, 300, 3)]
5      H15_20    New/Old recognition task for ID: 20.   P15HMH   H15   H15    20  45   M           Right Mesial Temporal  2007-09-01      20  150      50   100  {1}  learning: 80, recognition: 81  (80.0, 81.0)     5   Hunigton Memorial Hospital  [(150, 400, 300, 3)]
6      H16_23    New/Old recognition task for ID: 23.   P16HMH   H16   H16    23  34   F           Right Lateral Frontal  2007-10-01      1
[... 83 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'E'
import sys, pickle, numpy as np, pandas as pd, collections, hashlib
sys.path.insert(0,'entries/chandravadia-2020')
import chandravadia as C
a,S=pickle.load(open('sessions.pkl','rb'))
# duplicates of spike trains
h=collections.defaultdict(list)
for s in S:
    for i,sp in enumerate(s['spikes']):
        h[hashlib.md5(np.asarray(sp).tobytes()).hexdigest()].append((s['identifier'],i))
d=[v for v in h.values() if len(v)>1]; print('dup trains',len(d)); print(collections.Counter(tuple(sorted({x[0] for x in v})) for v in d))
# trials table identical?
for x,y in [('H42_54','H42_55'),('H23_43','H23_44')]:
    sx=[s for s in S if s['identifier']==x][0]; sy=[s for s in S if s['identifier']==y][0]
    print(x,y,'units',len(sx['units']),len(sy['units']), 'trials equal', sx['trials'].equals(sy['trials']), 'events equal', np.array_equal(sx['events_t'],sy['events_t']) if len(sx['events_t'])==len(sy['events_t']) else 'len differ', len(sx['events_t']),len(sy['events_t']))
    print(sx['trials'].start_time.values[:3], sy['trials'].start_time.values[:3])
# response checks
for s in S:
    r=C.recog(s['trials']); tr=s['trials']
    bad=set(r.conf.unique())-set(range(1,7))
    ev=s['events']; ex=s['expids']
    lab,sid=C.parse_identifier(s['identifier'])
    lv=r.label.value_counts().to_dict()
    resp_ev=ev[(ev>=31)&(ev<=36)]-30
    msg=[]
    if bad: msg.append(f'conf vals {bad}')
    if len(resp_ev)!=len(r) or not np.array_equal(resp_ev, r.conf.values): msg.append(f'ev resp {len(resp_ev)} vs {len(r)} eq={np.array_equal(resp_ev[:len(r)], r.conf.values[:len(resp_ev)])}')
    if lv!={0:50,1:50}: msg.append(f'labels {lv}')
    if len(ev)!=len(ex) or not np.array_equal(s['events_t'],s['expids_t']): msg.append('ev/ex mismatch')
    codes=set(np.unique(ev))-{55,1,2,3,20,21,31,32,33,34,35,36,6,66}
    if codes: msg.append(f'codes {codes}')
    learn=tr[tr.stim_phase=='learn']
    if learn.external_image_file.nunique()!=len(learn): msg.append(f'learn files {learn.external_image_file.nunique()}/{len(learn)}')
    # old trials in encoding
    enc=set(learn.external_image_file)
    old0=r[r.label==0].external_image_file.isin(enc).mean(); old1=r[r.label==1].external_image_file.isin(enc).mean()
    msg.append(f'inEnc l0={old0:.2f} l1={old1:.2f}')
    # responses old
    o0=(r[r.label==0].conf>=4).mean(); o1=(r[r.label==1].conf>=4).mean()
    msg.append(f'oldresp l0={o0:.2f} l1={o1:.2f}')
    print(s['identifier'], '; '.join(msg))
E
```

```
dup trains 66
Counter({('H42_54', 'H42_55'): 32, ('H23_43', 'H23_44'): 23, ('H21_38', 'H21_39'): 11})
H42_54 H42_55 units 32 32 trials equal False events equal False 1004 1004
[1610.74458  1616.774086 1621.54481 ] [1610.74458  1616.774086 1621.54481 ]
H23_43 H23_44 units 23 23 trials equal False events equal len differ 1006 754
[3292.277446 3297.167333 3300.267657] [1495.130874 1502.55728  1508.527651]
H10_7 inEnc l0=0.00 l1=1.00; oldresp l0=0.46 l1=0.66
H11_9 inEnc l0=0.00 l1=1.00; oldresp l0=0.24 l1=0.70
H14_17 inEnc l0=0.00 l1=1.00; oldresp l0=0.30 l1=0.66
H14_18 inEnc l0=0.00 l1=0.58; oldresp l0=0.02 l1=0.44
H15_21 inEnc l0=0.00 l1=0.52; oldresp l0=0.70 l1=0.80
H15_20 inEnc l0=0.00 l1=0.58; oldresp l0=0.76 l1=0.88
H16_23 inEnc l0=0.00 l1=0.52; oldresp l0=0.06 l1=0.58
H16_24 inEnc l0=0.00 l1=1.00; oldresp l0=0.20 l1=0.56
H17_32 inEnc l0=0.00 l1=1.00; oldresp l0=0.24 l1=0.70
H18_26 inEnc l0=0.00 l1=0.58; oldresp l0=0.14 l1=0.44
H19_28 inEnc l0=0.00 l1=1.00; oldresp l0=0.48 l1=0.80
H19_27 inEnc l0=0.00 l1=0.52; oldresp l0=0.30 l1=0.82
H21_38 inEnc l0=0.00 l1=1.00; oldresp l0=0.60 l1=0.92
H21_41 inEnc l0=0.00 l1=1.00; oldresp l0=0.36 l1=0.80
[... 74 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && python - <<'E'
import sys, pickle, numpy as np, pandas as pd, collections
sys.path.insert(0,'entries/chandravadia-2020')
import chandravadia as C
a,S=pickle.load(open('sessions.pkl','rb'))
print(collections.Counter(tuple(s['unit_columns']) for s in S))
print(collections.Counter(tuple(s['electrode_columns']) for s in S))
E=pd.concat([s['electrodes'].assign(sess=s['identifier']) for s in S])
print(E.dtypes); print(E.isna().sum()); print(E.filtering.value_counts()); print(E.location.value_counts()); print(E.imp.describe())
U=pd.concat([s['units'].assign(sess=s['identifier']) for s in S])
print(U.isna().sum()); print(U.waveform_sampling_rate.value_counts()); print(U.n_electrodes.value_counts()); print(U[['IsolationDist','SNR']].describe())
print(U.waveform_mean_encoding_finite.value_counts(), U.waveform_mean_recognition_finite.value_counts(), U.waveform_mean_encoding_samples.value_counts())
# unit location
locs=[]
for s in S:
    e=s['electrodes']; u=s['units']
    locs+=list(e.location.values[u.electrode_row.values])
print(collections.Counter(locs))
# ISI
isi=[C.isi_fraction(sp) for s in S for sp in s['spikes']]; isi=np.array(isi)
print('isi', np.nanmax(isi), (isi<0.03).mean(), np.isnan(isi).sum())
uns=[C.isi_fraction(sp,sort=False) for s in S for sp in s['spikes']]; print('unsorted', (np.array(uns)<0.03).mean())
print('sorted spikes', sum(np.all(np.diff(sp)>=0) for s in S for sp in s['spikes']))
# example neurons
for sid,ch in [(132,177),(144,140)]:
    for s in S:
        if C.parse_identifier(s['identifier'])[1]==sid:
            e=s['electrodes']; u=s['units']
            print(s['identifier'], e[['id','origChannel','location']].to_string())
            print(u.assign(ch=e.origChannel.values[u.electrode_row.values])[['id','origClusterID','electrode_row','ch','n_spikes']].to_string())
    print(sid, [s['identifier'] for s in S if C.parse_identifier(s['identifier'])[1]==sid])
E
```

```
Sat Nov 14 13:10:38 UTC 2026
/tmp/claude-1001/dev/lib/python3.13/site-packages/pandas/core/nanops.py:1324: RuntimeWarning: invalid value encountered in subtract
  sqr = (avg - values) ** 2
Counter({('origClusterID', 'waveform_mean_encoding', 'waveform_mean_recognition', 'IsolationDist', 'SNR', 'waveform_mean_sampling_rate', 'spike_times', 'electrodes'): 87})
Counter({('x', 'y', 'z', 'imp', 'location', 'filtering', 'group', 'group_name', 'origChannel'): 87})
filtering          str
group_name         str
id               int32
imp            float64
location           str
origChannel     uint16
x              float64
y              float64
z              float64
sess               str
dtype: object
filtering        0
group_name       0
id               0
imp            887
[... 86 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > beh.py <<'E'
import sys, pickle, numpy as np, pandas as pd, collections, time
sys.path.insert(0,'entries/chandravadia-2020')
import chandravadia as C
from scipy import stats
a,S=pickle.load(open('sessions.pkl','rb'))
rows=[]
for s in S:
    r=C.recog(s['trials']); lab,sid=C.parse_identifier(s['identifier'])
    H,F=C.cumulative_roc(r.conf, r.label==1)
    Hr,Fr=C.cumulative_roc(r.conf, r.label==0)
    A=C.auc(H,F); sl=C.zroc_slope(H,F)
    fh,fl,nh,nl=C.accuracy_fixed(r.conf,r.label==1)
    dh,dl,mode,dnh,dnl=C.accuracy_dynamic(r.conf,r.label==1)
    mh,ml,mm,_,_=C.accuracy_dynamic(r.conf,r.label==1,'matlab')
    rows.append(dict(sess=s['identifier'],sid=sid,site='TWH' if lab.startswith('T') else 'CS',auc=A,auc_rev=C.auc(Hr,Fr),slope=sl,fh=fh,fl=fl,dh=dh,dl=dl,mh=mh,ml=ml,mode=mode,incl=C.code_inclusion(r.conf,A)))
d=pd.DataFrame(rows)
print(d.auc.mean(), d.auc.std(ddof=1), d.auc_rev.mean())
print(d.groupby('site').auc.agg(['mean','std','count']))
print(stats.ttest_ind(d.auc[d.site=='CS'],d.auc[d.site=='TWH'],equal_var=False))
print('slope', d.slope.mean(), d.slope.std(), stats.ttest_1samp(d.slope,1), stats.wilcoxon(d.slope-1))
for h,l in [('fh','fl'),('dh','dl'),('mh','ml')]:
    x=d[[h,l]].dropna(); print(h, len(x), x.mean().values, stats.ttest_rel(x[h],x[l]), stats.ttest_ind(x[h],x[l],equal_var=False))
    x=d[d.incl][[h,l]].dropna(); print(' incl', len(x), x.mean().values, stats.ttest_rel(x[h],x[l]))
E
python beh.py
```

```
entries/chandravadia-2020/chandravadia.py:271: RankWarning: Polyfit may be poorly conditioned
  return np.polyfit(x, y, 1)[0]
entries/chandravadia-2020/chandravadia.py:271: RankWarning: Polyfit may be poorly conditioned
  return np.polyfit(x, y, 1)[0]
entries/chandravadia-2020/chandravadia.py:271: RankWarning: Polyfit may be poorly conditioned
  return np.polyfit(x, y, 1)[0]
entries/chandravadia-2020/chandravadia.py:271: RankWarning: Polyfit may be poorly conditioned
  return np.polyfit(x, y, 1)[0]
entries/chandravadia-2020/chandravadia.py:271: RankWarning: Polyfit may be poorly conditioned
  return np.polyfit(x, y, 1)[0]
0.752716091954023 0.0937848941245067 0.24728390804597697
          mean       std  count
site                           
CS    0.760152  0.085498     78
TWH   0.688272  0.137784      9
TtestResult(statistic=np.float64(1.5314060655167459), pvalue=np.float64(0.16108533561147875), df=np.float64(8.724855017391024))
slope 0.7256674124520925 0.37899045509168733 TtestResult(statistic=np.float64(-6.751631858525214), pvalue=np.float64(1.6307195195154453e-09), df=np.int64(86)) WilcoxonResult(statistic=np.float64(488.0), pvalue=np.float64(1.5858167031143077e-09))
fh 84 [0.80145739 0.60918562] TtestResult(statistic=np.float64(10.155954563740682), pvalue=np.float64(3.2235735607435254e-16), df=np.int64(83)) TtestResult(statistic=np.float64(9.439901473331899), pvalue=np.float64(4.388547568221284e-17), df=np.float64(159.6565887544402))
 incl 73 [0.8175996  0.60949315] TtestResult(statistic=np.float64(13.031054370712502), pvalue=np.float64(1.2737045483291715e-20), df=np.int64(72))
dh 82 [0.78200242 0.6079977 ] TtestResult(statistic=np.float64(7.8773885215430175), pvalue=np.float64(1.3095510871498402e-11), df=np.int64(81)) TtestResult(statistic=np.float64(8.231350635446585), pvalue=np.float64(8.337760567650721e-14), df=np.float64(149.90853588354327))
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > neu.py <<'E'
import sys, pickle, numpy as np, pandas as pd, collections, time, warnings
warnings.filterwarnings('ignore')
sys.path.insert(0,'entries/chandravadia-2020')
import chandravadia as C
from scipy import stats
a,S=pickle.load(open('sessions.pkl','rb'))
for s in S:
    r=C.recog(s['trials']); H,F=C.cumulative_roc(r.conf, r.label==1)
    x=stats.norm.ppf(F[:5])
    if np.ptp(x)<1e-9 or np.ptp(stats.norm.ppf(H[:5]))<1e-9: print('degenerate', s['identifier'], H[:5].round(3), F[:5].round(3))
rng=np.random.default_rng(1)
t=time.time(); rows=[]
for s in S:
    r=C.recog(s['trials']); lab,sid=C.parse_identifier(s['identifier'])
    on=r.start_time.values; cat=r.stimCategory.values; old=(r.label==1).values
    correct=(((r.conf<=3)&~old)|((r.conf>=4)&old)).values
    for i,sp in enumerate(s['spikes']):
        res=dict(sess=s['identifier'],site='TWH' if lab.startswith('T') else 'CS',unit=i)
        for wn,w in [('m',C.WINDOW_METHODS),('c',C.WINDOW_CODE)]:
            rt=C.window_rates(sp,on,w)
            res['vs_'+wn]=C.anova_p(rt,cat)
            res['ms_'+wn]=C.bootstrap_mean_equal(rt[old],rt[~old],1000,rng)
            res['msc_'+wn]=C.bootstrap_mean_equal(rt[old&correct],rt[~old&correct],1000,rng)
        rows.append(res)
d=pd.DataFrame(rows); print(time.time()-t)
N=len(d)
for c in ['vs_m','vs_c','ms_m','ms_c','msc_m','msc_c']:
    print(c, (d[c]<0.05).sum(), round(100*(d[c]<0.05).mean(),2), (d[c]<=0.05).sum(), d[c].isna().sum())
print('dual', ((d.vs_m<0.05)&(d.ms_m<0.05)).sum(), ((d.vs_c<0.05)&(d.msc_c<0.05)).sum())
for site,g in d.groupby('site'):
    print(site,len(g), 100*(g.vs_m<0.05).mean(), 100*(g.ms_m<0.05).mean(), 100*((g.vs_m<0.05)&(g.ms_m<0.05)).mean())
pickle.dump(d,open('neu.pkl','wb'))
E
python neu.py
```

```
degenerate CS24_60 [0.66 0.68 0.7  0.7  0.7 ] [0.16 0.16 0.16 0.16 0.16]
degenerate CS24_59 [0.88 0.88 0.88 0.88 0.88] [0.18 0.18 0.2  0.2  0.2 ]
degenerate CS39_93 [0.4 0.4 0.4 0.4 0.4] [0.38 0.38 0.38 0.38 0.38]
degenerate H48_99 [0.72 0.72 0.72 0.72 0.72] [0.08 0.08 0.08 0.08 0.08]
degenerate CS51_119 [0.84 0.86 0.86 0.86 0.86] [0.16 0.16 0.16 0.16 0.16]
degenerate T100_2008 [0.72 0.72 0.72 0.72 0.72] [0.24 0.24 0.24 0.24 0.24]
5.176551103591919
vs_m 332 17.81 332 6
vs_c 343 18.4 343 3
ms_m 115 6.17 118 0
ms_c 107 5.74 108 0
msc_m 145 7.78 145 0
msc_c 145 7.78 149 0
dual 12 24
CS 1787 17.62730833799664 5.987688864017907 0.6155567991046447
TWH 77 22.07792207792208 10.38961038961039 1.2987012987012987
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'E'
import sys, pickle, numpy as np, pandas as pd, warnings
sys.path.insert(0,'entries/chandravadia-2020')
import chandravadia as C
a,S=pickle.load(open('sessions.pkl','rb'))
pd.set_option('display.width',250); pd.set_option('display.max_rows',200)
T=C.session_table(C.europepmc_tables(C.PAPER_PMC)['Online-only Table 1'])
FT=C.session_table(C.europepmc_tables(C.FARAUT_PMC)['Table 1'])
print(len(T), T.label.nunique(), len(FT), FT.label.nunique())
D=pd.DataFrame([dict(label=C.table_label(s['subject']['subject_id']), idlabel=C.parse_identifier(s['identifier'])[0], session=C.parse_identifier(s['identifier'])[1], variant=min(C.variant_of(s['trials'].external_image_file)), age=int(s['subject']['age']), sex=s['subject']['sex'], diag=s['subject']['description'], nunits=len(s['units'])) for s in S])
m=D.merge(T,on='session',how='outer',suffixes=('_d','_t'),indicator=True)
print(m[m._merge!='both'])
mm=m[m._merge=='both']; print(mm[(mm.label_d!=mm.label_t)|(mm.variant_d!=mm.variant_t)|(mm.age_d!=mm.age_t)|(mm.sex_d!=mm.sex_t)][['session','label_d','label_t','variant_d','variant_t','age_d','age_t','sex_d','sex_t']])
f=D.merge(FT,on='session',how='outer',suffixes=('_d','_f'),indicator=True)
print(f[f._merge!='both'][['session','label_d','label_f','_merge','nunits']])
fb=f[f._merge=='both']; print(fb[(fb.label_d!=fb.label_f)|(fb.variant_d!=fb.variant_f)][['session','label_d','label_f','variant_d','variant_f','age_d','age_f','sex_d','sex_f']])
new=f[f._merge=='left_only']; print('new sessions',len(new),'new subj', len(set(new.label_d)-set(fb.label_d)), 'new neurons', new.nunits.sum())
E
```

```
87 59 65 42
Empty DataFrame
Columns: [label_d, idlabel, session, variant_d, age_d, sex_d, diag, nunits, label_t, variant_t, n_sessions, age_t, sex_t, diagnosis, _merge]
Index: []
    session label_d label_t  variant_d  variant_t  age_d  age_t sex_d sex_t
23       52     H33     H33          1          1     30     29     M     M
28       59     C24     C24          1          1     57     47     F     F
29       60     C24     C24          2          2     57     47     F     F
48       99     H48     H48          1          1     32     54     F     M
    session label_d label_f      _merge  nunits
48       98     NaN     H48  right_only     NaN
65      122     C53     NaN   left_only    27.0
66      123     C53     NaN   left_only     6.0
67      124     C54     NaN   left_only    43.0
68      125     C54     NaN   left_only    46.0
69      126     C54     NaN   left_only    34.0
70      127     C55     NaN   left_only     8.0
71      128     C56     NaN   left_only     7.0
72      130     C57     NaN   left_only    16.0
73      131     C57     NaN   left_only    11.0
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/chandravadia-2020 && python - <<'E'
p='chandravadia.py'; s=open(p).read()
s=s.replace('''def zroc_slope(H, F):
    """Slope of z(H) on z(F) over the five interior points (calcZROCSlope.m)."""
    x, y = stats.norm.ppf(F[:5]), stats.norm.ppf(H[:5])
    return np.polyfit(x, y, 1)[0]''','''def zroc_slope(H, F):
    """Slope of z(H) on z(F) over the five interior points (calcZROCSlope.m).

    NaN when the five false alarm rates are all equal, as the regression then has no slope."""
    x, y = stats.norm.ppf(F[:5]), stats.norm.ppf(H[:5])
    if np.ptp(x) < 1e-12:
        return np.nan
    return stats.linregress(x, y).slope''')
s=s.replace('''def table_label(subject_id: str) -> str:''','''def ident_label(label: str) -> str:
    """The identifier's subject label in the paper's notation: CS24 -> C24 (H09 and T88 are unchanged)."""
    return re.sub(r"^CS", "C", label)


def table_label(subject_id: str) -> str:''')
open(p,'w').write(s)
E
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && uv pip install -q nbformat nbconvert ipykernel 2>&1 | tail -1; date -u
```

```
Sat Nov 14 13:12:14 UTC 2026
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build_nb.py",
 "content": "\"\"\"Builds entries/chandravadia-2020/reproduce_chandravadia_2020.ipynb (development tool, not part of the entry).\"\"\"\nimport nbformat as nbf\nimport sys\n\nOUT = \"entries/chandravadia-2020/reproduce_chandravadia_2020.ipynb\"\ncells = []\n\n\ndef md(s):\n    cells.append(nbf.v4.new_markdown_cell(s.strip(\"\\n\")))\n\n\ndef code(s, tag=None):\n    c = nbf.v4.new_code_cell(s.strip(\"\\n\"))\n    if tag:\n        c.metadata[\"tags\"] = [tag]\n    cells.append(c)\n\n\nmd(r\"\"\"\n# Reproducing Chandravadia et al. (2020) from dandiset 000004\n\n**Paper.** Chandravadia N, Liang D, Schjetnan AGP, et al. (2020). A NWB-based dataset and processing\npipeline of human single-neuron activity during a declarative memory task. *Scientific Data* 7, 78.\n[doi:10.1038/s41597-020-0415-9](https://doi.org/10.1038/s41597-020-0415-9). The claims file\n(`claims/chandravadia-2020.yaml`) was written from the full text of the open access version of record\n(Methods, Data Records, Technical Validation, figure legends, Tables 1 and 2 and Online-only Table 1).\n\n**Dataset.** DANDI:000004, version **0.220126.1852**\n([doi:10.48324/dandi.000004/0.220126.1852](https://doi.org/10.48324/dandi.000004/0.220126.1852)).\nThis version was asked for in the instructions for this attempt. The paper cites the data on the Open\nScience Framework (doi:10.17605/OSF.IO/HV7JA), not a DANDI version; 0.220126.1852 is the most recent\npublished version, created a few seconds after 0.220126.1851 on 2022-01-26. Earlier versions were not\ncompared. Every file is streamed from the archive; the stimulus images, which make up most of each file,\nare never read.\n\n**Other inputs.** Online-only Table 1 of this paper and Table 1 of Faraut et al. (2018,\ndoi:10.1038/sdata.2018.10), which lists the sessions of the earlier release, are read from the Europe PMC\nfull text of the two open access articles (PMC7055261 and PMC5810422). The method details follow the\nclaims file, and where it is silent, the paper and its code (github.com/rutishauserlab/recogmem-release-NWB\nat commit 1d95162); `chandravadia.py` says where each comes from.\n\n| Claim | Tested here |\n|---|---|\n| counts-neurons-subjects | tested |\n| counts-sessions | tested |\n| table1-demographics | tested |\n| task-structure | tested |\n| new-old-label-coding | tested |\n| ttl-codes | tested |\n| experiment-ids | tested |\n| session-dates | tested |\n| units-table | tested |\n| electrodes-table | tested |\n| isi-criterion | tested |\n| fig5a-mtl-locations | tested |\n| fig5c-auc-all | tested |\n| fig5c-auc-sites | tested |\n| fig5b-roc-asymmetric | tested |\n| fig5d-confidence-accuracy | tested |\n| vs-cells-proportion | tested |\n| ms-cells-proportion | tested |\n| dual-cells-proportion | tested |\n| fig5f-site-proportions | tested |\n| twh-sessions | tested |\n| previous-release-link | tested (uses Table 1 of Faraut et al. 2018) |\n| previous-release-additions | tested (uses Table 1 of Faraut et al. 2018) |\n| fig4-example-vs-neuron | tested |\n| fig3-example-vs-neuron | blocked: session 144 is not in the dandiset |\n\"\"\")\n\ncode(r\"\"\"\nimport time\nimport resource\nimport hashlib\nimport warnings\nfrom collections import Counter\n\nimport numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nfrom scipy import stats\n\nimport chandravadia as C\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\npd.set_option(\"display.width\", 220)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 200)\nstarted = time.time()\n\"\"\")\n\nmd(\"## The files and what they hold\")\n\ncode(r\"\"\"\nmeta = C.version_metadata()\nassets = C.list_assets()\nprint(f\"dandiset {C.DANDISET} version {C.VERSION}, doi {meta['doi']}\")\nprint(\"assets:\", len(assets), \" total size %.2f GB\" % (assets['size'].sum() / 1e9))\nprint(\"archive's summary: subjects\", meta[\"assetsSummary\"][\"numberOfSubjects\"], \" files\", meta[\"assetsSummary\"][\"numberOfFiles\"])\nt0 = time.time()\nsessions = C.read_all(assets.asset_id)\nprint(f\"read {len(sessions)} files in {time.time() - t0:.0f} s; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\nfor s, p in zip(sessions, assets.path):\n    s[\"path\"] = p\n    lab, sid = C.parse_identifier(s[\"identifier\"])\n    s[\"label\"], s[\"sid\"] = C.ident_label(lab), sid\n    s[\"site\"] = \"TWH\" if s[\"label\"].startswith(\"T\") else \"CS\"\ns0 = sessions[0]\nprint(\"\\nOne file,\", s0[\"path\"])\nprint(\"  trials columns:\", s0[\"trial_columns\"])\nprint(\"  electrodes columns:\", s0[\"electrode_columns\"])\nprint(\"  units columns:\", s0[\"unit_columns\"])\nprint(\"  subject fields:\", s0[\"subject\"])\nprint(\"  stimulus series:\", s0[\"stimulus_series\"], \" devices:\", s0[\"devices\"])\nprint(\"  data_collection:\", repr(s0[\"data_collection\"]))\nprint(\"  new_old_labels_recog description:\", repr(s0[\"trial_descriptions\"][\"new_old_labels_recog\"]))\nprint(\"  every file has the same trials, electrodes and units columns:\",\n      len({tuple(s[\"trial_columns\"]) for s in sessions}) == 1, len({tuple(s[\"electrode_columns\"]) for s in sessions}) == 1,\n      len({tuple(s[\"unit_columns\"]) for s in sessions}) == 1)\n\"\"\")\n\nmd(\"\"\"\n## Data check\n\nCounts by site, subject and session, the trial and unit counts, and the ranges and units of every\nvariable the analysis uses. The checks of the description against the values follow the table.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor s in sessions:\n    tr = s[\"trials\"]\n    r = C.recog(tr)\n    rows.append(dict(file=s[\"path\"].split(\"/\")[1][:48], identifier=s[\"identifier\"], subject_id=s[\"subject\"][\"subject_id\"],\n                     label=s[\"label\"], session=s[\"sid\"], site=s[\"site\"], start=s[\"session_start_time\"][:10],\n                     n_trials=len(tr), n_learn=int((tr.stim_phase == \"learn\").sum()), n_recog=len(r),\n                     n_units=len(s[\"units\"]), n_electrodes=len(s[\"electrodes\"]),\n                     variant=\",\".join(map(str, sorted(C.variant_of(tr.external_image_file)))),\n                     exp_ids=\",\".join(str(int(x)) for x in np.unique(s[\"expids\"]))))\nsess = pd.DataFrame(rows)\nprint(sess.drop(columns=\"file\").to_string())\nprint(\"\\nfiles\", len(sess), \" distinct subject_id\", sess.subject_id.nunique(), \" distinct (subject, session)\",\n      len(set(zip(sess.label, sess.session))))\nprint(\"by site:\", sess.groupby(\"site\").agg(files=(\"session\", \"size\"), subjects=(\"label\", \"nunique\"), units=(\"n_units\", \"sum\")).to_dict(\"index\"))\nprint(\"subject_id agrees with the identifier's label in every file:\",\n      all(C.table_label(a) == b for a, b in zip(sess.subject_id, sess.label)))\nprint(\"trials per file:\", sess.n_trials.value_counts().to_dict(), \" learn:\", sess.n_learn.value_counts().to_dict(),\n      \" recog:\", sess.n_recog.value_counts().to_dict())\nprint(\"units per file: min\", sess.n_units.min(), \" median\", sess.n_units.median(), \" max\", sess.n_units.max(), \" total\", sess.n_units.sum())\n\nallr = pd.concat([C.recog(s[\"trials\"]).assign(identifier=s[\"identifier\"]) for s in sessions])\nalll = pd.concat([s[\"trials\"][s[\"trials\"].stim_phase == \"learn\"] for s in sessions])\nprint(\"\\nrecognition response_value:\", sorted(allr.response_value.unique()), \" learning response_value:\", sorted(alll.response_value.unique()))\nprint(\"new_old_labels_recog values, recognition:\", allr.new_old_labels_recog.value_counts().to_dict(),\n      \" learning:\", alll.new_old_labels_recog.value_counts().to_dict())\nprint(\"stimCategory values:\", sorted(allr.stimCategory.unique()), \" category names:\", sorted(pd.concat([s[\"trials\"].category_name for s in sessions]).unique()))\nprint(\"stim_phase values:\", sorted(pd.concat([s[\"trials\"].stim_phase for s in sessions]).unique()))\ndur = pd.concat([s[\"trials\"].stop_time - s[\"trials\"].start_time for s in sessions])\nprint(\"stimulus duration stop_time - start_time (s): %.3f to %.3f, median %.3f\" % (dur.min(), dur.max(), dur.median()))\nprint(\"start_time equals stim_on_time in every trial:\", all(np.allclose(s[\"trials\"].start_time, s[\"trials\"].stim_on_time) for s in sessions))\n\nspk_rng = []\nfor s in sessions:\n    allsp = np.concatenate([x for x in s[\"spikes\"] if len(x)])\n    spk_rng.append((allsp.min() - s[\"trials\"].start_time.min(), allsp.max() - s[\"trials\"].delay2_time.max()))\nspk_rng = np.array(spk_rng)\nprint(\"\\nspike times (s, the file's clock): first spike minus first trial onset %.1f to %.1f s; last spike minus last trial end %.1f to %.1f s\"\n      % (spk_rng[:, 0].min(), spk_rng[:, 0].max(), spk_rng[:, 1].min(), spk_rng[:, 1].max()))\nU = pd.concat([s[\"units\"].assign(identifier=s[\"identifier\"]) for s in sessions])\nrates = np.array([len(sp) / (s[\"trials\"].delay2_time.max() - s[\"trials\"].start_time.min()) for s in sessions for sp in s[\"spikes\"]])\nprint(\"mean firing rate over the task (Hz): median %.2f, range %.3f to %.1f\" % (np.median(rates), rates.min(), rates.max()))\nprint(\"waveform sampling rate (Hz):\", U.waveform_sampling_rate.value_counts().to_dict(), \" samples per waveform:\",\n      U.waveform_mean_encoding_samples.value_counts().to_dict())\nE = pd.concat([s[\"electrodes\"].assign(identifier=s[\"identifier\"]) for s in sessions])\nprint(\"electrode locations:\", E.location.value_counts().to_dict())\nprint(\"electrode filtering:\", E.filtering.value_counts().to_dict())\nprint(\"MNI x range %.1f to %.1f mm, y %.1f to %.1f, z %.1f to %.1f; impedance non-missing: %d of %d\"\n      % (E.x.min(), E.x.max(), E.y.min(), E.y.max(), E.z.min(), E.z.max(), E.imp.notna().sum(), len(E)))\n\"\"\", tag=\"sanity\")\n\nmd(\"\"\"\nChecks of the description against the data, from the output above and the cells below:\n\n- The archive lists 87 files and 59 subjects; the files hold 87 distinct (subject, session) pairs and 59\n  subject_ids, and each file's subject_id names the same subject as its identifier.\n- The paper says each session has 100 encoding and 100 recognition trials; the counts above show\n  sessions with 50 or 97 learning trials (claim task-structure).\n- The response codes, the label coding, the TTL codes and the experiment ids are checked in their claims.\n- Spike times are in seconds on the clock of the trial table: they start within seconds of the first trial\n  and end with the task. The next cell checks the alignment with the trials.\n\"\"\")\n\nmd(\"\"\"\n### Do the spikes share the clock of the trial table?\n\nTwo checks. First, the TTL stimulus onsets (code 1) of the events stream are compared with the trials'\nstart times. Second, a contrast that an offset would destroy: the fraction of units whose recognition\nfiring rate differs across the 5 categories (one-way ANOVA, p < 0.05) in 1 s windows starting at\ndifferent times relative to stimulus onset. If the spikes and the trials share a clock, the fraction is\nnear the 5% false positive rate before onset and rises after it.\n\"\"\")\n\ncode(r\"\"\"\nmism = []\nfor s in sessions:\n    on_ev = s[\"events_t\"][s[\"events\"] == 1]\n    st = s[\"trials\"].start_time.values\n    n = min(len(on_ev), len(st))\n    mism.append(dict(identifier=s[\"identifier\"], ttl1=len(on_ev), trials=len(st),\n                     max_abs_diff_ms=1000 * np.max(np.abs(on_ev[:n] - st[:n])) if n else np.nan))\nmism = pd.DataFrame(mism)\nprint(\"files whose TTL-1 count equals the trial count:\", (mism.ttl1 == mism.trials).sum(), \"of\", len(mism))\nprint(\"largest |TTL-1 time - start_time| over files where counts agree: %.3f ms\" % mism[mism.ttl1 == mism.trials].max_abs_diff_ms.max())\nprint(mism[mism.ttl1 != mism.trials].to_string())\n\noffsets = np.arange(-2.0, 2.01, 0.25)\nfrac = []\nper_session = []\nfor s in sessions:\n    r = C.recog(s[\"trials\"])\n    on, cat = r.start_time.values, r.stimCategory.values\n    ps = np.array([[C.anova_p(C.window_rates(sp, on, (o, o + 1.0)), cat) for o in offsets] for sp in s[\"spikes\"]])\n    frac.append(ps)\n    pre = np.nansum(ps[:, offsets == -1.25] < 0.05)\n    post = np.nansum(ps[:, np.isclose(offsets, 0.25)] < 0.05)\n    per_session.append(dict(identifier=s[\"identifier\"], units=len(ps), sel_pre=int(pre), sel_post=int(post)))\nfrac = np.vstack(frac)\nprint(\"\\nfraction of units category selective, by window start relative to onset (window 1 s):\")\nprint(pd.Series(np.nanmean(frac < 0.05, axis=0).round(3), index=offsets).to_string())\nps_df = pd.DataFrame(per_session)\nprint(\"\\nper session, units selective in the window -1.25 to -0.25 s against 0.25 to 1.25 s:\")\nprint(\"  sessions with more selective units after onset:\", (ps_df.sel_post > ps_df.sel_pre).sum(),\n      \" equal:\", (ps_df.sel_post == ps_df.sel_pre).sum(), \" fewer:\", (ps_df.sel_post < ps_df.sel_pre).sum(), \" of\", len(ps_df))\nprint(\"  sessions where the contrast cannot show alignment (no selective unit after onset):\",\n      ps_df[ps_df.sel_post == 0].identifier.tolist())\nfig, ax = plt.subplots(figsize=(5, 3))\nax.plot(offsets, np.nanmean(frac < 0.05, axis=0), \"o-\")\nax.axhline(0.05, color=\"k\", lw=0.5)\nax.set_xlabel(\"window start relative to stimulus onset (s)\")\nax.set_ylabel(\"fraction category selective\")\nplt.show()\n\"\"\")\n\nmd(\"\"\"\n### Recordings deposited more than once\n\nEvery unit's spike train is hashed, and trains found in more than one file are listed by pair of files.\nThe trial tables and events of each pair are compared too.\n\"\"\")\n\ncode(r\"\"\"\nowners = {}\nfor s in sessions:\n    for i, sp in enumerate(s[\"spikes\"]):\n        owners.setdefault(hashlib.md5(np.asarray(sp).tobytes()).hexdigest(), []).append((s[\"identifier\"], i))\ndups = [v for v in owners.values() if len(v) > 1]\npairs = Counter(tuple(sorted({x[0] for x in v})) for v in dups)\nbyid = {s[\"identifier\"]: s for s in sessions}\nfor (a, b), n in pairs.items():\n    sa, sb = byid[a], byid[b]\n    same_trials = len(sa[\"trials\"]) == len(sb[\"trials\"]) and np.allclose(sa[\"trials\"].start_time, sb[\"trials\"].start_time)\n    same_resp = len(sa[\"trials\"]) == len(sb[\"trials\"]) and np.array_equal(sa[\"trials\"].response_value, sb[\"trials\"].response_value)\n    print(f\"{a} ({len(sa['units'])} units) and {b} ({len(sb['units'])} units): {n} identical spike trains;\"\n          f\" same trial onsets {same_trials}, same responses {same_resp}, variants {sorted(C.variant_of(sa['trials'].external_image_file))}\"\n          f\" and {sorted(C.variant_of(sb['trials'].external_image_file))}\")\ndup_keys = {k for k, v in owners.items() if len(v) > 1}\nn_dup_rows = sum(len(v) - 1 for v in dups)\nprint(\"unit rows:\", sum(len(s[\"spikes\"]) for s in sessions), \" distinct spike trains:\", len(owners), \" rows that repeat another file's train:\", n_dup_rows)\n# the unit rows kept when duplicated trains are counted once: the first occurrence\nseen, keep = set(), {}\nfor s in sessions:\n    ks = []\n    for sp in s[\"spikes\"]:\n        h = hashlib.md5(np.asarray(sp).tobytes()).hexdigest()\n        ks.append(h not in seen)\n        seen.add(h)\n    keep[s[\"identifier\"]] = np.array(ks)\n\"\"\")\n\nmd(\"\"\"\n## Reference tables from the papers\n\nOnline-only Table 1 of this paper (subjects, sessions, variants, age, sex, diagnosis) and Table 1 of\nFaraut et al. (2018), the earlier release, read from the Europe PMC full text.\n\"\"\")\n\ncode(r\"\"\"\npaper_tables = C.europepmc_tables(C.PAPER_PMC)\nT1 = C.session_table(paper_tables[\"Online-only Table 1\"])\nprint(\"Online-only Table 1:\", len(T1), \"sessions,\", T1.label.nunique(), \"subjects; totals row:\",\n      [c for c in paper_tables[\"Online-only Table 1\"][-1]])\nfaraut_tables = C.europepmc_tables(C.FARAUT_PMC)\nF1 = C.session_table(faraut_tables[\"Table 1\"])\nprint(\"Faraut et al. 2018 Table 1:\", len(F1), \"sessions,\", F1.label.nunique(), \"subjects\")\nprint(T1.head(3).to_string())\n\"\"\")\n\n# ---------------------------------------------------------------- claims\n\nmd(\"\"\"\n## counts-neurons-subjects\n\n> The dataset holds 1863 single neurons recorded from the medial temporal lobes of 59 subjects.\n\nCriterion: neurons are the unit rows over all files, subjects the distinct subject_id values; reading (a)\nevery row, (b) spike trains deposited in two files counted once. Both within 10% under one reading.\n\"\"\")\n\ncode(r\"\"\"\nn_rows = int(sess.n_units.sum())\nn_once = int(sum(k.sum() for k in keep.values()))\nn_subj = sess.subject_id.nunique()\nprint(f\"(a) unit rows: {n_rows} (expected 1863 +/- 186.3; difference {n_rows - 1863:+d})\")\nprint(f\"(b) duplicated trains counted once: {n_once} (difference {n_once - 1863:+d})\")\nprint(f\"subjects (distinct subject_id): {n_subj} (expected 59 +/- 5.9)\")\nprint(\"units by subject: min\", sess.groupby(\"label\").n_units.sum().min(), \" max\", sess.groupby(\"label\").n_units.sum().max())\n\"\"\", tag=\"claim:counts-neurons-subjects\")\n\nmd(\"\"\"\n**Result: reproduced.** Under reading (a) the files hold 1864 unit rows, one more than the paper's 1863,\nand 59 subjects. Counting the 66 duplicated spike trains once gives 1798, also within tolerance.\n\"\"\")\n\nmd(\"\"\"\n## counts-sessions\n\n> The patients performed 87 sessions, listed by subject and session id in Online-only Table 1 (the\n> Methods give 89).\n\nCriterion: the set of (subject, session id) pairs from the file identifiers against Online-only Table 1.\n\"\"\")\n\ncode(r\"\"\"\nfiles_set = set(zip(sess.label, sess.session))\ntable_set = set(zip(T1.label, T1.session))\nprint(\"pairs in the files:\", len(files_set), \" in Online-only Table 1:\", len(table_set))\nprint(\"in the files only:\", sorted(files_set - table_set), \" in the table only:\", sorted(table_set - files_set))\nprint(\"sets equal:\", files_set == table_set, \"; the Methods' 89 differs from the count by\", 89 - len(files_set))\n\"\"\", tag=\"claim:counts-sessions\")\n\nmd(\"\"\"\n**Result: reproduced.** The 87 (subject, session) pairs of the files are exactly the 87 of Online-only\nTable 1. The Methods' 89 is two more than either.\n\"\"\")\n\nmd(\"\"\"\n## table1-demographics\n\n> Online-only Table 1 gives the age and sex of every subject; there are 25 female and 34 male subjects.\n\nCriterion: age and sex compared subject by subject; reproduced when every subject matches.\n\"\"\")\n\ncode(r\"\"\"\nsubj_files = pd.DataFrame([dict(label=s[\"label\"], age=s[\"subject\"][\"age\"], sex=s[\"subject\"][\"sex\"],\n                                diagnosis_file=s[\"subject\"][\"description\"]) for s in sessions])\nper_subj_files = subj_files.groupby(\"label\").agg(age_file=(\"age\", lambda x: \",\".join(sorted(set(x)))),\n                                                 sex_file=(\"sex\", lambda x: \",\".join(sorted(set(x)))),\n                                                 diagnosis_file=(\"diagnosis_file\", lambda x: \",\".join(sorted(set(x)))))\nper_subj_table = T1.groupby(\"label\").agg(age_table=(\"age\", \"first\"), sex_table=(\"sex\", \"first\"), diagnosis_table=(\"diagnosis\", \"first\"))\ncmp = per_subj_files.join(per_subj_table, how=\"outer\")\ncmp[\"age_match\"] = cmp.age_file == cmp.age_table.astype(str)\ncmp[\"sex_match\"] = cmp.sex_file == cmp.sex_table\nprint(\"files with more than one age or sex for a subject:\", int(cmp.age_file.str.contains(\",\").sum() + cmp.sex_file.str.contains(\",\").sum()))\nprint(\"subjects:\", len(cmp), \" age matches:\", int(cmp.age_match.sum()), \" sex matches:\", int(cmp.sex_match.sum()),\n      \" both:\", int((cmp.age_match & cmp.sex_match).sum()))\nprint(cmp[~(cmp.age_match & cmp.sex_match)][[\"age_file\", \"age_table\", \"sex_file\", \"sex_table\"]].to_string())\nprint(\"\\nfemale/male in the files:\", (cmp.sex_file == \"F\").sum(), (cmp.sex_file == \"M\").sum(),\n      \"; in the table:\", (cmp.sex_table == \"F\").sum(), (cmp.sex_table == \"M\").sum(), \"(expected 25 and 34)\")\nprint(\"\\ndiagnosis, side by side (first 12 subjects and every one that differs in words):\")\ndiff_diag = cmp[cmp.diagnosis_file.str.lower() != cmp.diagnosis_table.str.lower()]\nprint(cmp[[\"diagnosis_file\", \"diagnosis_table\"]].head(12).to_string())\nprint(\"subjects whose diagnosis text differs:\", len(diff_diag), \"of\", len(cmp))\nprint(diff_diag[[\"diagnosis_file\", \"diagnosis_table\"]].to_string())\n\"\"\", tag=\"claim:table1-demographics\")\n\nmd(\"\"\"\n**Result: partially reproduced.** 56 of 59 subjects match the table in age and sex. H33 is 30 in the files\nand 29 in the table, C24 is 57 against 47, and H48 is a 32-year-old woman in the files against a\n54-year-old man in the table (32 F is C48's entry). The files count 26 female and 33 male subjects, the\ntable 25 and 34, both within tolerance. The diagnoses differ in wording for many subjects (printed\nabove), as the files use a coarser coding.\n\"\"\")\n\nmd(\"\"\"\n## task-structure\n\n> Each session has 100 encoding trials showing 100 novel images and 100 recognition trials, of which 50\n> show new and 50 old images, and the images come from 5 visual categories.\n\nCriterion: per session, 100 encoding trials with 100 distinct image files (external_image_file), 100\nrecognition trials with 50 of each label, and 5 categories; partially reproduced when each part holds in\nmore than half of the sessions.\n\"\"\")\n\ncode(r\"\"\"\nts = []\nfor s in sessions:\n    tr = s[\"trials\"]\n    learn = tr[tr.stim_phase == \"learn\"]\n    r = C.recog(tr)\n    ts.append(dict(identifier=s[\"identifier\"], n_learn=len(learn), learn_files=learn.external_image_file.nunique(),\n                   n_recog=len(r), n_label0=int((r.label == 0).sum()), n_label1=int((r.label == 1).sum()),\n                   n_cat=tr.stimCategory.nunique(), n_cat_names=tr.category_name.nunique()))\nts = pd.DataFrame(ts)\nts[\"enc_ok\"] = (ts.n_learn == 100) & (ts.learn_files == 100)\nts[\"rec_ok\"] = (ts.n_recog == 100) & (ts.n_label0 == 50) & (ts.n_label1 == 50)\nts[\"cat_ok\"] = (ts.n_cat == 5) & (ts.n_cat_names == 5)\nprint(\"sessions:\", len(ts), \" encoding part holds:\", int(ts.enc_ok.sum()), \" recognition part:\", int(ts.rec_ok.sum()),\n      \" 5 categories:\", int(ts.cat_ok.sum()), \" all three:\", int((ts.enc_ok & ts.rec_ok & ts.cat_ok).sum()))\nprint(ts[~(ts.enc_ok & ts.rec_ok & ts.cat_ok)].to_string())\nprint(\"encoding trials whose image file repeats within the block, all sessions:\", int((ts.n_learn - ts.learn_files).sum()))\n\"\"\", tag=\"claim:task-structure\")\n\nmd(\"\"\"\n**Result: partially reproduced.** 79 of 87 sessions hold 100 encoding trials with 100 distinct images,\n100 recognition trials with 50 of each label, and 5 categories. In 7 sessions the trial table holds only\n50 encoding trials (150 trials in all), and in CS53_123 97. Every session has 100 recognition trials with\n50 of each label and 5 categories, so each part holds in more than half of the sessions.\n\"\"\")\n\nmd(\"\"\"\n## new-old-label-coding\n\n> In the trials table, new_old_labels_recog is 0 for old stimuli (seen during encoding) and 1 for new\n> stimuli.\n\nCriterion, per session: (1) under the stated coding, label 0 trials show image files from the session's\nencoding block and label 1 trials do not; (2) label 0 (old) trials receive \"old\" responses (4 to 6) more\noften than label 1 trials. Reproduced when both hold in every session; not reproduced when, in most\nsessions, both hold with the labels reversed.\n\"\"\")\n\ncode(r\"\"\"\nlc = []\nfor s in sessions:\n    tr = s[\"trials\"]\n    enc = set(tr[tr.stim_phase == \"learn\"].external_image_file)\n    r = C.recog(tr)\n    in0 = r[r.label == 0].external_image_file.isin(enc).mean()\n    in1 = r[r.label == 1].external_image_file.isin(enc).mean()\n    old0 = (r[r.label == 0].conf >= 4).mean()\n    old1 = (r[r.label == 1].conf >= 4).mean()\n    lc.append(dict(identifier=s[\"identifier\"], n_learn=int((tr.stim_phase == \"learn\").sum()), label0_in_encoding=in0,\n                   label1_in_encoding=in1, label0_old_resp=old0, label1_old_resp=old1))\nlc = pd.DataFrame(lc)\nlc[\"stated_1\"] = (lc.label0_in_encoding == 1) & (lc.label1_in_encoding == 0)\nlc[\"stated_2\"] = lc.label0_old_resp > lc.label1_old_resp\nlc[\"reversed_1\"] = (lc.label1_in_encoding > 0) & (lc.label0_in_encoding == 0)\nlc[\"reversed_1_full\"] = (lc.label1_in_encoding == 1) & (lc.label0_in_encoding == 0)\nlc[\"reversed_2\"] = lc.label1_old_resp > lc.label0_old_resp\nprint(\"sessions where both tests hold under the stated coding (0 = old):\", int((lc.stated_1 & lc.stated_2).sum()), \"of\", len(lc))\nprint(\"sessions where both hold reversed (1 = old):\", int((lc.reversed_1 & lc.reversed_2).sum()),\n      \"; with every label-1 image in the encoding block:\", int((lc.reversed_1_full & lc.reversed_2).sum()))\nprint(\"label-1 images found in the encoding block: median %.2f, min %.2f; label-0 images: max %.2f\"\n      % (lc.label1_in_encoding.median(), lc.label1_in_encoding.min(), lc.label0_in_encoding.max()))\nprint(\"'old' responses, median over sessions: label 1 %.2f, label 0 %.2f\" % (lc.label1_old_resp.median(), lc.label0_old_resp.median()))\nprint(\"\\nsessions where not every label-1 image is in the encoding block, or the response test fails:\")\nprint(lc[~(lc.reversed_1_full & lc.reversed_2)].round(2).to_string())\n\"\"\", tag=\"claim:new-old-label-coding\")\n\nmd(\"\"\"\n**Result: not reproduced.** The coding is reversed: label 1 marks old images. In no session do label 0\ntrials show encoding images, and in all 87 sessions label 1 trials do and receive more \"old\" responses\n(86 of 87 hold both tests reversed; in T98_2005 the response test fails, 0.68 against 0.72). In the 7\nsessions whose trial table holds only 50 encoding trials, about half of the label 1 images (0.52 to 0.58)\nare in the stored encoding block. The paper's code also treats 1 as old.\n\"\"\")\n\nmd(\"\"\"\n## ttl-codes\n\n> The events stream holds the TTL markers 55, 1, 2, 3, 20 or 21, 31 to 36, 6 and 66 with the meanings of\n> Table 1, and the events and experiment_ids streams have one entry each, in the same order.\n\nCriterion: in every file, events and experiment_ids have the same length and timestamps, the events hold\nonly the listed codes, and every trial shows 1, 2, 3, a response of its phase's kind and 6 in this order;\npartially reproduced when this holds in most files. A trial's events are those from its start_time to its\ndelay2_time (the end of the trial), with 1 ms of slack.\n\"\"\")\n\ncode(r\"\"\"\nlisted = {55, 1, 2, 3, 20, 21, 31, 32, 33, 34, 35, 36, 6, 66}\ntt = []\nfor s in sessions:\n    ev, et = s[\"events\"], s[\"events_t\"]\n    same = len(ev) == len(s[\"expids\"]) and np.allclose(et, s[\"expids_t\"])\n    extra = sorted(set(np.unique(ev).astype(int)) - listed)\n    bad = 0\n    for _, row in s[\"trials\"].iterrows():\n        sel = (et >= row.start_time - 1e-3) & (et <= row.delay2_time + 1e-3)\n        seq = ev[sel].astype(int).tolist()\n        resp = {20, 21} if row.stim_phase == \"learn\" else {31, 32, 33, 34, 35, 36}\n        ok = len(seq) == 5 and seq[:3] == [1, 2, 3] and seq[3] in resp and seq[4] == 6\n        bad += not ok\n    tt.append(dict(identifier=s[\"identifier\"], n_events=len(ev), n_expids=len(s[\"expids\"]), same_length_and_times=same,\n                   extra_codes=extra, trials=len(s[\"trials\"]), trials_bad_sequence=bad,\n                   starts_55=int(ev[0]) == 55, ends_66=int(ev[-1]) == 66))\ntt = pd.DataFrame(tt)\ntt[\"ok\"] = tt.same_length_and_times & (tt.extra_codes.str.len() == 0) & (tt.trials_bad_sequence == 0)\nprint(\"files where events and experiment_ids have the same length and timestamps:\", int(tt.same_length_and_times.sum()), \"of\", len(tt))\nprint(\"files with only the listed codes:\", int((tt.extra_codes.str.len() == 0).sum()))\nprint(\"files where every trial has the sequence 1, 2, 3, response, 6:\", int((tt.trials_bad_sequence == 0).sum()))\nprint(\"files meeting all three:\", int(tt.ok.sum()))\nprint(\"files starting with 55:\", int(tt.starts_55.sum()), \" ending with 66:\", int(tt.ends_66.sum()))\nprint(tt[~tt.ok].to_string())\nprint(\"\\ncounts of the unlisted codes over all files:\",\n      dict(Counter(int(x) for s in sessions for x in s[\"events\"] if int(x) not in listed)))\n\"\"\", tag=\"claim:ttl-codes\")\n\nmd(\"\"\"\n**Result: partially reproduced.** In all 87 files the two streams have the same length and timestamps. 77\nfiles meet the whole criterion; 10 files hold codes not in Table 1 (0, 4, 22, 23, 98 and 99, listed above),\nand in those files some trials do not show the full sequence. The criterion holds in most files.\n\"\"\")\n\nmd(\"\"\"\n## experiment-ids\n\n> The learning block is labelled with one of 80, 83 or 88 and the recognition block with one of 81, 84 or 89.\n\nThe learning block's id is the experiment id at the TTL-1 events of the learning trials, the recognition\nblock's at those of the recognition trials.\n\"\"\")\n\ncode(r\"\"\"\nei = []\nfor s in sessions:\n    ev, ex = s[\"events\"], s[\"expids\"]\n    on_idx = np.where(ev == 1)[0]\n    phase = s[\"trials\"].stim_phase.values\n    n = min(len(on_idx), len(phase))\n    learn_ids = sorted(set(ex[on_idx[:n]][phase[:n] == \"learn\"].astype(int)))\n    recog_ids = sorted(set(ex[on_idx[:n]][phase[:n] == \"recog\"].astype(int)))\n    ei.append(dict(identifier=s[\"identifier\"], learn=learn_ids, recog=recog_ids, all_ids=sorted(set(ex.astype(int))),\n                   data_collection=s[\"data_collection\"],\n                   variant=\",\".join(map(str, sorted(C.variant_of(s[\"trials\"].external_image_file))))))\nei = pd.DataFrame(ei)\nei[\"ok\"] = ei.apply(lambda r: len(r.learn) == 1 and len(r.recog) == 1 and r.learn[0] in (80, 83, 88) and r.recog[0] in (81, 84, 89), axis=1)\nei[\"pair_ok\"] = ei.apply(lambda r: r.ok and (r.learn[0], r.recog[0]) in ((80, 81), (83, 84), (88, 89)), axis=1)\nprint(\"files whose two ids fall in the sets:\", int(ei.ok.sum()), \"of\", len(ei), \"; whose pair is one of Table 2's:\", int(ei.pair_ok.sum()))\nprint(ei[~ei.ok].to_string())\nprint(\"\\npairs used:\", Counter((tuple(a), tuple(b)) for a, b in zip(ei.learn, ei.recog)))\nprint(\"pair against task variant:\", pd.crosstab(ei.variant, ei.learn.astype(str)).to_dict())\n\"\"\", tag=\"claim:experiment-ids\")\n\nmd(\"\"\"\n**Result: partially reproduced.** In 83 of 87 files both ids fall in the stated sets and form one of\nTable 2's pairs. CS33_77 uses 81 and 82, CS39_100 and H51_105 82 and 83, and H42_55 80 and 82. The ids\ndo not follow the task variant: most variant 2 and 3 sessions recorded at Cedars-Sinai use 80 and 81.\n\"\"\")\n\nmd(\"\"\"\n## session-dates\n\n> session_start_time keeps only the year and month of the experiment, with the day set to the first of\n> the month for all sessions.\n\"\"\")\n\ncode(r\"\"\"\nsd = pd.DataFrame([dict(identifier=s[\"identifier\"], start=s[\"session_start_time\"]) for s in sessions])\nsd[\"date\"] = pd.to_datetime(sd.start.str[:10])\nsd[\"first\"] = sd.date.dt.day == 1\nprint(\"files whose session_start_time falls on the first of a month:\", int(sd[\"first\"].sum()), \"of\", len(sd))\nprint(sd[~sd[\"first\"]].to_string())\nyears = sd.date.dt.year\nprint(\"years:\", years.min(), \"to\", years.max(), \"; by year:\", years.value_counts().sort_index().to_dict())\nprint(\"files dated before 2006 (the earliest file name otherwise):\", sd[years < 2006].identifier.tolist())\nprint(\"all session_start_time values carry the time 00:00:00:\", sd.start.str[11:19].eq(\"00:00:00\").all())\n\"\"\", tag=\"claim:session-dates\")\n\nmd(\"\"\"\n**Result: partially reproduced.** 86 of 87 files are dated on the first of a month; H28_48 is dated\n2010-03-13. H44_68 is dated 2000-01-01, six years before any other file and before the Huntington\nrecordings that surround it in the session numbering (2006 to 2016), so its year is likely a default.\n\"\"\")\n\nmd(\"\"\"\n## units-table\n\n> The units table holds spike_times, waveform_mean_encoding, waveform_mean_recognition (sampled at 100 kHz),\n> origClusterID, SNR, IsolDist and electrodes, with one electrode per neuron.\n\nThe column the paper calls IsolDist is named IsolationDist in the files, with the description \"IsolDist\";\nit is taken as that column, as the names differ only in spelling.\n\"\"\")\n\ncode(r\"\"\"\nneed = [\"spike_times\", \"waveform_mean_encoding\", \"waveform_mean_recognition\", \"origClusterID\", \"SNR\", \"electrodes\"]\nhas_cols = [all(c in s[\"unit_columns\"] for c in need) and (\"IsolDist\" in s[\"unit_columns\"] or \"IsolationDist\" in s[\"unit_columns\"]) for s in sessions]\nprint(\"files holding every column (IsolDist as IsolationDist):\", sum(has_cols), \"of\", len(sessions),\n      \"; files with a column named exactly IsolDist:\", sum(\"IsolDist\" in s[\"unit_columns\"] for s in sessions))\nprint(\"units linked to exactly one electrode:\", int((U.n_electrodes == 1).sum()), \"of\", len(U))\nprint(\"waveform sampling rate stated:\", U.waveform_sampling_rate.unique(), \"Hz (expected 100000 +/- 10000)\")\nfor c in [\"SNR\", \"IsolationDist\"]:\n    v = U[c]\n    print(f\"{c}: NaN {int(v.isna().sum())}, infinite {int(np.isinf(v).sum())}, finite {int(np.isfinite(v).sum())} of {len(v)};\"\n          f\" finite range {v[np.isfinite(v)].min():.3g} to {v[np.isfinite(v)].max():.3g}\")\nprint(\"units with a non-finite SNR or IsolationDist:\", int((~np.isfinite(U.SNR) | ~np.isfinite(U.IsolationDist)).sum()),\n      \"; in files:\", int(U[~np.isfinite(U.SNR) | ~np.isfinite(U.IsolationDist)].identifier.nunique()))\nprint(\"IsolationDist above 1e6:\", int((U.IsolationDist > 1e6).sum()))\nprint(\"waveforms finite in every unit:\", bool(U.waveform_mean_encoding_finite.all() and U.waveform_mean_recognition_finite.all()))\n\"\"\", tag=\"claim:units-table\")\n\nmd(\"\"\"\n**Result: partially reproduced.** Every file holds the columns (IsolDist under the name IsolationDist),\nevery unit has one electrode, and the stated waveform sampling rate is 98.4 kHz, within tolerance. The\nquality metrics are not finite for every unit: IsolationDist is NaN for 493 of 1864 units and SNR for 75,\nSNR is infinite for some units, and a few isolation distances are above 1e6, which is not a plausible\nvalue.\n\"\"\")\n\nmd(\"\"\"\n## electrodes-table\n\n> The electrodes table gives each electrode's brain area, MNI coordinates, impedance, the filter applied\n> before spike sorting (300 to 3000 Hz) and the original hardware channel.\n\"\"\")\n\ncode(r\"\"\"\ndef empty(col):\n    v = E[col]\n    if v.dtype == object:\n        return v.isna() | v.astype(str).str.strip().isin([\"\", \"nan\", \"NaN\", \"None\"])\n    return v.isna()\n\nec = pd.DataFrame({c: dict(present_in_files=sum(c in s[\"electrode_columns\"] for s in sessions),\n                           empty=int(empty(c).sum()), electrodes=len(E))\n                   for c in [\"location\", \"x\", \"y\", \"z\", \"imp\", \"filtering\", \"origChannel\"]}).T\nprint(ec.to_string())\nprint(\"filtering values:\", E.filtering.value_counts().to_dict())\nxyz_missing = E[E.x.isna()]\nprint(\"files with missing coordinates:\", xyz_missing.identifier.nunique(), \"; electrodes\", len(xyz_missing))\n\"\"\", tag=\"claim:electrodes-table\")\n\nmd(\"\"\"\n**Result: not reproduced.** The impedance column is empty (NaN) for all 887 electrodes. Location,\nfiltering (300-3000Hz) and origChannel are filled for every electrode, and the MNI coordinates are\nmissing for 99 electrodes.\n\"\"\")\n\nmd(\"\"\"\n## isi-criterion\n\n> Clusters were accepted as units only when fewer than 3% of their interspike intervals were shorter than 3 ms.\n\"\"\")\n\ncode(r\"\"\"\nisi_sorted = np.array([C.isi_fraction(sp, sort=True) for s in sessions for sp in s[\"spikes\"]])\nisi_stored = np.array([C.isi_fraction(sp, sort=False) for s in sessions for sp in s[\"spikes\"]])\nunsorted = [(s[\"identifier\"], i) for s in sessions for i, sp in enumerate(s[\"spikes\"]) if np.any(np.diff(sp) < 0)]\nprint(\"units:\", len(isi_sorted), \" with fewer than 2 spikes:\", int(np.isnan(isi_sorted).sum()))\nprint(\"sorted: below 3%%: %d (%.2f%%); at or above: %d\" % ((isi_sorted < 0.03).sum(), 100 * np.nanmean(isi_sorted < 0.03), (isi_sorted >= 0.03).sum()))\nprint(\"ISI<3ms fraction, sorted: median %.4f, 95th percentile %.4f, max %.3f\" % (np.nanmedian(isi_sorted), np.nanpercentile(isi_sorted, 95), np.nanmax(isi_sorted)))\nfor thr in (0.01, 0.02, 0.03, 0.05):\n    print(f\"  units below {thr:.0%}: {(isi_sorted < thr).sum()}\")\nprint(\"variant, as stored: below 3%%: %d; at or above: %d\" % ((isi_stored < 0.03).sum(), (isi_stored >= 0.03).sum()))\nprint(\"units whose stored spike times are not in time order:\", len(unsorted), unsorted)\nUU = U.assign(isi=isi_sorted)\nprint(UU[UU.isi >= 0.03][[\"identifier\", \"id\", \"n_spikes\", \"isi\"]].to_string())\n\"\"\", tag=\"claim:isi-criterion\")\n\nmd(\"\"\"\n**Result: partially reproduced.** With spike times sorted, 1858 of 1864 units (99.7%) have fewer than 3% of\nintervals below 3 ms; 6 units do not, one with 50%. That is at least 95%, the partial threshold. The spike\ntimes of 13 units are not stored in time order; as stored, 1860 units fall below 3%.\n\"\"\")\n\nmd(\"\"\"\n## fig5a-mtl-locations\n\n> All neurons were recorded from the medial temporal lobe, in the amygdala and the hippocampus.\n\"\"\")\n\ncode(r\"\"\"\nunit_loc = pd.Series([s[\"electrodes\"].location.values[r] for s in sessions for r in s[\"units\"].electrode_row.values])\nprint(unit_loc.value_counts().to_string())\nmtl = unit_loc.str.contains(\"Amygdala|Hippocampus\", case=False)\nprint(\"units in amygdala or hippocampus:\", int(mtl.sum()), \"of\", len(unit_loc))\n\"\"\", tag=\"claim:fig5a-mtl-locations\")\n\nmd(\"\"\"\n**Result: reproduced.** The electrode of every one of the 1864 units is in the left or right amygdala or\nhippocampus.\n\"\"\")\n\nmd(\"\"\"\n## fig5c-auc-all\n\n> Subjects distinguished new from old images; the behavioural AUC averaged over all sessions is 0.74 ± 0.10.\n\nAUC per session as in the paper's code: label 1 as old (claims file), cumulative ROC over the six\nconfidence levels, rates adjusted for 0 and 1, trapezoid AUC; mean and standard deviation over the 87\nsessions. The confidence response is response_value minus 30; it is checked here against the TTL codes.\n\"\"\")\n\ncode(r\"\"\"\nresp_check = [np.array_equal(s[\"events\"][(s[\"events\"] >= 31) & (s[\"events\"] <= 36)] - 30, C.recog(s[\"trials\"]).conf.values) for s in sessions]\nprint(\"files where response_value - 30 equals the TTL 31-36 codes of the events stream, in order:\", sum(resp_check), \"of\", len(sessions))\nbeh = []\nfor s in sessions:\n    r = C.recog(s[\"trials\"])\n    H, F = C.cumulative_roc(r.conf, r.label == 1)\n    Hs, Fs = C.cumulative_roc(r.conf, r.label == 0)\n    a = C.auc(H, F)\n    beh.append(dict(identifier=s[\"identifier\"], label=s[\"label\"], site=s[\"site\"], auc=a, auc_stated_coding=C.auc(Hs, Fs),\n                    slope=C.zroc_slope(H, F), H=H, F=F, conf=r.conf.values, old=(r.label == 1).values))\nbeh = pd.DataFrame(beh)\nprint(\"AUC over %d sessions: mean %.3f, SD %.3f (expected 0.74 +/- 0.10 and 0.10 +/- 0.01); range %.3f to %.3f\"\n      % (len(beh), beh.auc.mean(), beh.auc.std(ddof=1), beh.auc.min(), beh.auc.max()))\nprint(\"sessions with AUC below 0.5:\", beh[beh.auc < 0.5].identifier.tolist())\nprint(\"with the stated coding (0 = old) the mean AUC would be %.3f\" % beh.auc_stated_coding.mean())\nonce = beh[[keep[i].any() for i in beh.identifier]]\nprint(\"variant, the second file of each fully duplicated pair left out (%d sessions): mean %.3f, SD %.3f\" % (len(once), once.auc.mean(), once.auc.std(ddof=1)))\nfig, ax = plt.subplots(figsize=(4, 3))\nax.hist(beh.auc, bins=20)\nax.set_xlabel(\"AUC\")\nax.set_ylabel(\"sessions\")\nplt.show()\n\"\"\", tag=\"claim:fig5c-auc-all\")\n\nmd(\"\"\"\n**Result: reproduced.** The mean AUC over the 87 sessions is 0.753 with a standard deviation of 0.094,\nboth within tolerance. The confidence responses equal the TTL codes in every file.\n\"\"\")\n\nmd(\"\"\"\n## fig5c-auc-sites\n\n> Performance was similar at the two study sites, with an average AUC of 0.74 ± 0.09 for CS sessions and\n> 0.69 ± 0.13 for TWH sessions.\n\nCS sessions are those of subjects labelled H or C, TWH those labelled T (Figure 5 legend).\n\"\"\")\n\ncode(r\"\"\"\ng = beh.groupby(\"site\").auc.agg([\"count\", \"mean\", lambda x: x.std(ddof=1)])\ng.columns = [\"sessions\", \"mean\", \"sd\"]\nprint(g.round(3).to_string())\nprint(\"expected CS 0.74 +/- 0.09 (SD 0.09 +/- 0.009), TWH 0.69 +/- 0.13 (SD 0.13 +/- 0.013)\")\nw = stats.ttest_ind(beh.auc[beh.site == \"CS\"], beh.auc[beh.site == \"TWH\"], equal_var=False)\nprint(\"Welch's t-test CS against TWH: t = %.2f, p = %.3f, difference of means %.3f\" % (w.statistic, w.pvalue, g.loc[\"CS\", \"mean\"] - g.loc[\"TWH\", \"mean\"]))\nprint(\"TWH sessions by subject:\", beh[beh.site == \"TWH\"][[\"identifier\", \"auc\"]].round(3).to_dict(\"records\"))\n\"\"\", tag=\"claim:fig5c-auc-sites\")\n\nmd(\"\"\"\n**Result: reproduced.** CS sessions average 0.760 (SD 0.085, 78 sessions) and TWH sessions 0.688 (SD 0.138,\n9 sessions); all four values are within tolerance. The sites do not differ by Welch's t-test (p = 0.16).\n\"\"\")\n\nmd(\"\"\"\n## fig5b-roc-asymmetric\n\n> The ROC curve is asymmetric (p < 0.05), as expected for declarative memory.\n\nCriterion: the z-ROC slope per session (regression of z(H) on z(F) over the five interior points), mean\nbelow 1 with a two-sided one-sample t-test against 1 at p < 0.05. Sessions whose five false alarm rates\nare all equal have no slope and are left out and counted. Variants: Wilcoxon signed-rank test, and the\nslope of the pooled ROC (the counts summed over sessions, as the code's countersAv).\n\"\"\")\n\ncode(r\"\"\"\nsl = beh.slope\nleft_out = beh[sl.isna()].identifier.tolist()\nx = sl.dropna()\nt = stats.ttest_1samp(x, 1.0)\nwz = stats.wilcoxon(x - 1.0)\nprint(\"sessions with a slope: %d; left out (all five false alarm rates equal): %d %s\" % (len(x), len(left_out), left_out))\nprint(\"z-ROC slope: mean %.3f, SD %.3f, median %.3f, range %.3f to %.3f; below 1 in %d of %d sessions\"\n      % (x.mean(), x.std(ddof=1), x.median(), x.min(), x.max(), (x < 1).sum(), len(x)))\nprint(\"one-sample t-test against 1: t = %.2f, p = %.2g\" % (t.statistic, t.pvalue))\nprint(\"variant, Wilcoxon signed-rank against 1: p = %.2g\" % wz.pvalue)\nconf_all = np.concatenate(beh.conf.values)\nold_all = np.concatenate(beh.old.values)\nHp, Fp = C.cumulative_roc(conf_all, old_all)\nprint(\"variant, pooled ROC over all trials: slope %.3f; H %s; F %s\" % (C.zroc_slope(Hp, Fp), Hp.round(3), Fp.round(3)))\nfor site, gg in beh.groupby(\"site\"):\n    y = gg.slope.dropna()\n    print(f\"  {site}: {len(y)} sessions, mean slope {y.mean():.3f}, t-test against 1 p = {stats.ttest_1samp(y, 1.0).pvalue:.2g}\")\n\"\"\", tag=\"claim:fig5b-roc-asymmetric\")\n\nmd(\"\"\"\n**Result: reproduced.** Over the 82 sessions with a slope, the mean z-ROC slope is 0.726, below 1\n(t-test against 1, p = 1e-9; Wilcoxon p = 2e-9). The pooled ROC has a slope of 0.84. Five sessions with\nequal false alarm rates at every criterion were left out.\n\"\"\")\n\nmd(\"\"\"\n## fig5d-confidence-accuracy\n\n> Accuracy is significantly higher in high than in low confidence trials (P < 0.001, paired t test) across\n> all sessions.\n\nReadings of the split: (a) the fixed split of the MATLAB code, high = 1 or 6 and low = 2 to 5; (b) the\ndynamic split of the Python code (helper.dynamic_split). Sessions without responses in one group are left\nout and counted. Variants: the unpaired Welch test the Python code runs, the code's session inclusion rule\n(AUC at least 0.6 and both high and low responses used for new and old), and the MATLAB dynamic split.\n\"\"\")\n\ncode(r\"\"\"\nacc = []\nfor _, b in beh.iterrows():\n    fh, fl, nh, nl = C.accuracy_fixed(b.conf, b.old)\n    dh, dl, mode, dnh, dnl = C.accuracy_dynamic(b.conf, b.old, \"python\")\n    mh, ml, mmode, _, _ = C.accuracy_dynamic(b.conf, b.old, \"matlab\")\n    acc.append(dict(identifier=b.identifier, site=b.site, fixed_high=fh, fixed_low=fl, n_high=nh, n_low=nl,\n                    dyn_high=dh, dyn_low=dl, mode=mode, mat_high=mh, mat_low=ml, included=C.code_inclusion(b.conf, b.auc)))\nacc = pd.DataFrame(acc)\nfor name, h, l in [(\"(a) fixed split\", \"fixed_high\", \"fixed_low\"), (\"(b) Python dynamic split\", \"dyn_high\", \"dyn_low\"),\n                   (\"variant, MATLAB dynamic split\", \"mat_high\", \"mat_low\")]:\n    d = acc[[h, l, \"included\"]].dropna()\n    pt = stats.ttest_rel(d[h], d[l])\n    wt = stats.ttest_ind(d[h], d[l], equal_var=False)\n    di = d[d.included]\n    pti = stats.ttest_rel(di[h], di[l])\n    print(f\"{name}: {len(d)} sessions ({len(acc) - len(d)} left out for an empty group); high {100 * d[h].mean():.1f}% vs low {100 * d[l].mean():.1f}%;\"\n          f\" high > low in {(d[h] > d[l]).sum()}; paired t = {pt.statistic:.2f}, p = {pt.pvalue:.2g};\"\n          f\" Welch p = {wt.pvalue:.2g}; code's inclusion ({len(di)} sessions) paired p = {pti.pvalue:.2g}\")\nprint(\"sessions left out under (a):\", acc[acc.fixed_high.isna() | acc.fixed_low.isna()].identifier.tolist())\nprint(\"split modes chosen by the Python code:\", acc[\"mode\"].value_counts().to_dict())\nfor site, gg in acc.groupby(\"site\"):\n    d = gg[[\"fixed_high\", \"fixed_low\"]].dropna()\n    print(f\"  {site} (fixed): {len(d)} sessions, high {100 * d.fixed_high.mean():.1f}% vs low {100 * d.fixed_low.mean():.1f}%, paired p = {stats.ttest_rel(d.fixed_high, d.fixed_low).pvalue:.2g}\")\n\"\"\", tag=\"claim:fig5d-confidence-accuracy\")\n\nmd(\"\"\"\n**Result: reproduced.** Under the fixed split, accuracy is 80.1% in high and 60.9% in low confidence\ntrials over 84 sessions (paired t-test p = 3e-16); under the Python dynamic split 78.2% against 60.8% over\n82 sessions (p = 1e-11). The unpaired tests, the code's inclusion rule and the MATLAB split all give\np below 0.001.\n\"\"\")\n\nmd(\"\"\"\n## Selection of VS and MS cells\n\nFiring rates of every unit in the 100 recognition trials, in the Methods' window (200 to 1200 ms after\nstimulus onset) and the code's (200 to 1700 ms). VS: one-way ANOVA across the 5 categories, p < 0.05.\nMS: two-tailed bootstrap of equal means (bootstrapMeanEqualTest.m, 1000 resamples), old (label 1)\nagainst new (label 0) trials, p < 0.05; all 50 and 50 trials (Methods) and the code's correct trials only\n(old answered 4 to 6, new answered 1 to 3). The bootstrap uses its own generator, seeded once (seed 2020).\nThe nulls shuffle the category labels, or the new/old labels, within each session (seed 7).\n\"\"\")\n\ncode(r\"\"\"\nrng_ms = np.random.default_rng(2020)\nrows = []\nt0 = time.time()\nfor s in sessions:\n    r = C.recog(s[\"trials\"])\n    on, cat = r.start_time.values, r.stimCategory.values\n    old = (r.label == 1).values\n    correct = (((r.conf <= 3) & ~old) | ((r.conf >= 4) & old)).values\n    for i, sp in enumerate(s[\"spikes\"]):\n        row = dict(identifier=s[\"identifier\"], label=s[\"label\"], site=s[\"site\"], unit=i, kept_once=keep[s[\"identifier\"]][i])\n        for wn, w in ((\"m\", C.WINDOW_METHODS), (\"c\", C.WINDOW_CODE)):\n            rt = C.window_rates(sp, on, w)\n            row[\"vs_\" + wn] = C.anova_p(rt, cat)\n            row[\"ms_\" + wn] = C.bootstrap_mean_equal(rt[old], rt[~old], 1000, rng_ms)\n            row[\"msc_\" + wn] = C.bootstrap_mean_equal(rt[old & correct], rt[~old & correct], 1000, rng_ms)\n        row[\"n_old_correct\"], row[\"n_new_correct\"] = int((old & correct).sum()), int((~old & correct).sum())\n        rows.append(row)\ncells = pd.DataFrame(rows)\nprint(f\"{len(cells)} units in {time.time() - t0:.0f} s\")\nprint(\"units with the same rate in every trial (ANOVA undefined, counted as not VS): Methods' window\",\n      int(cells.vs_m.isna().sum()), \", code's window\", int(cells.vs_c.isna().sum()))\n\nrng_null = np.random.default_rng(7)\nnull = []\nfor s in sessions:\n    r = C.recog(s[\"trials\"])\n    on = r.start_time.values\n    cat = rng_null.permutation(r.stimCategory.values)\n    old = rng_null.permutation((r.label == 1).values)\n    for sp in s[\"spikes\"]:\n        rt = C.window_rates(sp, on, C.WINDOW_METHODS)\n        null.append(dict(vs=C.anova_p(rt, cat), ms=C.bootstrap_mean_equal(rt[old], rt[~old], 1000, rng_null)))\nnull = pd.DataFrame(null)\nprint(\"nulls (labels shuffled within session, Methods' window): VS %.2f%%, MS %.2f%%\" % (100 * (null.vs < 0.05).mean(), 100 * (null.ms < 0.05).mean()))\n\"\"\")\n\nmd(\"\"\"\n## vs-cells-proportion\n\n> 343 of the 1863 cells (18.4%) are visually selective, by a one-way ANOVA (P < 0.05) of the firing rate in\n> recognition trials, in a 1 s window starting 200 ms after stimulus onset, across the 5 visual categories.\n\"\"\")\n\ncode(r\"\"\"\nN = len(cells)\ndef show(mask, label, n=None):\n    n = len(mask) if n is None else n\n    print(f\"  {label}: {int(mask.sum())} of {n} ({100 * mask.sum() / n:.2f}%)\")\nprint(\"VS cells (expected 343 +/- 34.3 and 18.4% +/- 1.84):\")\nshow(cells.vs_m < 0.05, \"Methods' window, every unit\")\nshow(cells.vs_c < 0.05, \"variant, code's window\")\nk = cells[cells.kept_once]\nshow(k.vs_m < 0.05, \"variant, duplicated trains counted once\")\nshow(null.vs < 0.05, \"null, categories shuffled within session\")\nprint(\"by threshold (Methods' window):\", {a: int((cells.vs_m < a).sum()) for a in (0.01, 0.05, 0.1)})\nby_subj = cells.groupby(\"label\").agg(units=(\"unit\", \"size\"), vs=(\"vs_m\", lambda p: int((p < 0.05).sum())))\nprint(\"by subject: VS fraction median %.2f, range %.2f to %.2f; subjects with no VS cell: %d of %d\"\n      % ((by_subj.vs / by_subj.units).median(), (by_subj.vs / by_subj.units).min(), (by_subj.vs / by_subj.units).max(), (by_subj.vs == 0).sum(), len(by_subj)))\n\"\"\", tag=\"claim:vs-cells-proportion\")\n\nmd(\"\"\"\n**Result: reproduced.** In the Methods' window 332 of 1864 units (17.8%) are VS cells, within tolerance of\n343 and 18.4%. The code's window gives 343 (18.4%), and the shuffled null 5%.\n\"\"\")\n\nmd(\"\"\"\n## ms-cells-proportion\n\n> 146 of the 1863 cells (7.8%) are memory selective, by a two-tailed bootstrap comparison of mean firing\n> rates (1,000 runs, P < 0.05) between the 50 novel and 50 familiar recognition trials in a 1 s window\n> starting 200 ms after stimulus onset.\n\nCriterion: every unit, the Methods' window and all 50 and 50 trials. The code's choices are variants.\nThe bootstrap is repeated with four other seeds to show its resampling spread.\n\"\"\")\n\ncode(r\"\"\"\nprint(\"MS cells (expected 146 +/- 14.6 and 7.8% +/- 0.78):\")\nshow(cells.ms_m < 0.05, \"Methods' window, all 50 and 50 trials\")\nshow(cells.ms_m <= 0.05, \"  the same with p <= 0.05, as the code's selection compares\")\nshow(cells.msc_m < 0.05, \"variant, correct trials only, Methods' window\")\nshow(cells.ms_c < 0.05, \"variant, all trials, code's window\")\nshow(cells.msc_c < 0.05, \"variant, correct trials only, code's window (the code's choices)\")\nshow(k.ms_m < 0.05, \"variant, duplicated trains counted once\")\nshow(null.ms < 0.05, \"null, new/old labels shuffled within session\")\nprint(\"correct trials per session: old %d to %d, new %d to %d\"\n      % (cells.n_old_correct.min(), cells.n_old_correct.max(), cells.n_new_correct.min(), cells.n_new_correct.max()))\nseeds = []\nfor seed in (1, 2, 3, 4):\n    rg = np.random.default_rng(seed)\n    n_ms = 0\n    for s in sessions:\n        r = C.recog(s[\"trials\"])\n        old = (r.label == 1).values\n        for sp in s[\"spikes\"]:\n            rt = C.window_rates(sp, r.start_time.values, C.WINDOW_METHODS)\n            n_ms += C.bootstrap_mean_equal(rt[old], rt[~old], 1000, rg) < 0.05\n    seeds.append(int(n_ms))\nprint(\"main reading with seeds 1 to 4:\", seeds)\nfor site, gg in cells.groupby(\"site\"):\n    print(f\"  {site}: {int((gg.ms_m < 0.05).sum())} of {len(gg)} ({100 * (gg.ms_m < 0.05).mean():.1f}%)\")\n\"\"\", tag=\"claim:ms-cells-proportion\")\n\nmd(\"\"\"\n**Result: not reproduced.** With all 50 and 50 trials in the Methods' window, 115 of 1864 units (6.2%) are\nMS cells, below the tolerance of 146 (131 to 161); other seeds give 113 to 121. The paper's code compares\nonly correctly answered trials, and with that selection 145 units (7.8%) qualify in either window, a\nmatch. The shuffled null gives 5%.\n\"\"\")\n\nmd(\"\"\"\n## dual-cells-proportion\n\n> 26 cells (1.4%) are both visually and memory selective.\n\"\"\")\n\ncode(r\"\"\"\nprint(\"dual cells (expected 26 +/- 2.6 and 1.4% +/- 0.14):\")\nshow((cells.vs_m < 0.05) & (cells.ms_m < 0.05), \"both main tests\")\nshow((cells.vs_c < 0.05) & (cells.msc_c < 0.05), \"variant, the code's choices for both\")\nshow((cells.vs_m < 0.05) & (cells.msc_m < 0.05), \"variant, Methods' window, MS on correct trials\")\nshow((null.vs < 0.05) & (null.ms < 0.05), \"null\")\nprint(\"expected by independence from the main counts: %.1f\" % ((cells.vs_m < 0.05).mean() * (cells.ms_m < 0.05).mean() * N))\n\"\"\", tag=\"claim:dual-cells-proportion\")\n\nmd(\"\"\"\n**Result: not reproduced.** 12 units (0.64%) are selected by both main tests, against 26 (1.4%). With the\ncode's choices for both tests 24 units (1.29%) qualify, within tolerance.\n\"\"\")\n\nmd(\"\"\"\n## fig5f-site-proportions\n\n> The percentages of VS, MS and dual cells are comparable between CS sessions (18.4%, 7.7% and 1.4%) and the\n> new TWH sessions (19.4%, 10.4% and 1.3%).\n\nCriterion: two-sided Fisher's exact test between sites for each type at 0.05; reproduced when no test finds\na difference and at least four of the six values are within tolerance; partially reproduced when only one\nof these holds.\n\"\"\")\n\ncode(r\"\"\"\nexpected = {(\"CS\", \"VS\"): 18.4, (\"CS\", \"MS\"): 7.7, (\"CS\", \"dual\"): 1.4, (\"TWH\", \"VS\"): 19.4, (\"TWH\", \"MS\"): 10.4, (\"TWH\", \"dual\"): 1.3}\ndef site_table(vs, ms, label):\n    sel = {\"VS\": vs, \"MS\": ms, \"dual\": vs & ms}\n    out, fisher = [], {}\n    for typ, m in sel.items():\n        tab = []\n        for site in (\"CS\", \"TWH\"):\n            mm = m[cells.site == site]\n            pct = 100 * mm.mean()\n            e = expected[(site, typ)]\n            out.append(dict(site=site, type=typ, n=int(mm.sum()), units=len(mm), pct=round(pct, 2), expected=e,\n                            within=abs(pct - e) <= 0.1 * e))\n            tab.append([int(mm.sum()), int(len(mm) - mm.sum())])\n        fisher[typ] = stats.fisher_exact(tab).pvalue\n    out = pd.DataFrame(out)\n    print(label)\n    print(out.to_string(index=False))\n    print(\"  Fisher's exact p:\", {k: round(v, 3) for k, v in fisher.items()}, \"; values within tolerance:\", int(out.within.sum()), \"of 6\")\n    return out, fisher\nmain_site, main_fisher = site_table(cells.vs_m < 0.05, cells.ms_m < 0.05, \"main (Methods' window, all trials):\")\nsite_table(cells.vs_c < 0.05, cells.msc_c < 0.05, \"variant, the code's choices:\")\nsite_table(cells.vs_m < 0.05, cells.msc_m < 0.05, \"variant, Methods' window, MS on correct trials:\")\nprint(\"TWH units by session:\", sess[sess.site == \"TWH\"].set_index(\"identifier\").n_units.to_dict())\n\"\"\", tag=\"claim:fig5f-site-proportions\")\n\nmd(\"\"\"\n**Result: partially reproduced.** No Fisher's exact test finds a difference between the sites (p from 0.3\nto 0.5 in the main reading), but only 3 of the 6 percentages are within tolerance: CS has 17.6% VS, 6.0% MS\nand 0.62% dual cells, TWH 22.1%, 10.4% and 1.3%. TWH has 77 units, so one cell moves its percentages by 1.3\npoints. With the code's choices 4 of 6 are within tolerance and no test finds a difference.\n\"\"\")\n\nmd(\"\"\"\n## twh-sessions\n\n> The dataset includes 9 sessions from a new institution, Toronto Western Hospital.\n\"\"\")\n\ncode(r\"\"\"\ntwh = sess[sess.label.str.startswith(\"T\")]\nprint(\"sessions with a subject label starting with T:\", len(twh), \"(expected 9 +/- 0.9)\")\nprint(twh[[\"identifier\", \"subject_id\", \"start\", \"n_units\"]].to_string(index=False))\nprint(\"institution field of these files:\", sorted({s[\"institution\"] for s in sessions if s[\"label\"].startswith(\"T\")}))\n\"\"\", tag=\"claim:twh-sessions\")\n\nmd(\"\"\"\n**Result: reproduced.** Nine sessions, from eight subjects, have subject labels starting with T, and their\nfiles name Toronto Western Hospital as the institution.\n\"\"\")\n\nmd(\"\"\"\n## previous-release-link\n\n> The sessions of the earlier release (Faraut et al. 2018) are found in this dandiset under the same subject,\n> session id and task variant.\n\nCriterion: sessions matched by session id; a matched session agrees when its subject label and task variant\n(from the image folder of external_image_file) are those of Faraut et al.'s Table 1. Reproduced when every\nsession is found and agrees; partially reproduced when at least 90% are.\n\"\"\")\n\ncode(r\"\"\"\ndandi_sess = pd.DataFrame([dict(session=s[\"sid\"], label_d=s[\"label\"], variant_d=sorted(C.variant_of(s[\"trials\"].external_image_file)),\n                                age_d=int(s[\"subject\"][\"age\"]), sex_d=s[\"subject\"][\"sex\"], units=len(s[\"units\"])) for s in sessions])\nlk = F1.merge(dandi_sess, on=\"session\", how=\"left\")\nlk[\"found\"] = lk.label_d.notna()\nlk[\"agrees\"] = lk.found & (lk.label == lk.label_d) & lk.apply(lambda r: r.found and r.variant_d == [r.variant], axis=1)\nprint(\"sessions in Faraut et al. Table 1:\", len(lk), \"; found:\", int(lk.found.sum()), \"; found and agree:\", int(lk.agrees.sum()),\n      \"(%.1f%%)\" % (100 * lk.agrees.mean()))\nprint(\"not found or not agreeing:\")\nprint(lk[~lk.agrees][[\"label\", \"session\", \"variant\", \"age\", \"sex\", \"label_d\", \"variant_d\"]].to_string(index=False))\nfa = lk[lk.found]\nprint(\"matched sessions whose age differs:\", fa[fa.age != fa.age_d][[\"label\", \"session\", \"age\", \"age_d\"]].to_dict(\"records\"))\nprint(\"matched sessions whose sex differs:\", fa[fa.sex != fa.sex_d][[\"label\", \"session\", \"sex\", \"sex_d\"]].to_dict(\"records\"))\nprint(\"Faraut's table against this paper's Online-only Table 1, for H48:\", F1[F1.label == \"H48\"][[\"session\", \"variant\", \"age\", \"sex\"]].to_dict(\"records\"),\n      T1[T1.label == \"H48\"][[\"session\", \"variant\", \"age\", \"sex\"]].to_dict(\"records\"))\n\"\"\", tag=\"claim:previous-release-link\")\n\nmd(\"\"\"\n**Result: partially reproduced.** 64 of the 65 sessions of the earlier release are found under the same\nsubject and variant (98.5%). Session 98 of subject H48 is not in the dandiset, nor in this paper's\nOnline-only Table 1. Among matched sessions, ages differ for C24 (47 against 57) and H33, and H48's\nsession 99 is a 32-year-old woman in the file against a 54-year-old man in both papers.\n\"\"\")\n\nmd(\"\"\"\n## previous-release-additions\n\n> Relative to the earlier release of this task's data (Faraut et al. 2018), this release adds 23 sessions,\n> 17 subjects and 288 neurons.\n\nCriterion: new sessions are the dandiset's sessions not in Faraut et al.'s Table 1, new subjects those with\nno session in it, new neurons the unit rows of the new sessions. Reproduced when all three are within 10%;\npartially reproduced when one or two are.\n\"\"\")\n\ncode(r\"\"\"\nnew_s = dandi_sess[~dandi_sess.session.isin(F1.session)]\nold_labels = set(dandi_sess[dandi_sess.session.isin(F1.session)].label_d)\nnew_subj = sorted(set(new_s.label_d) - old_labels)\nprint(\"new sessions:\", len(new_s), \"(expected 23 +/- 2.3):\", sorted(new_s.session))\nprint(\"new subjects:\", len(new_subj), \"(expected 17 +/- 1.7):\", new_subj)\nprint(\"new neurons (unit rows of new sessions):\", int(new_s.units.sum()), \"(expected 288 +/- 28.8)\")\nprint(\"  by site:\", new_s.assign(site=np.where(new_s.label_d.str.startswith(\"T\"), \"TWH\", \"CS\")).groupby(\"site\").units.sum().to_dict())\nn_old_rel = dandi_sess[dandi_sess.session.isin(F1.session)].units.sum()\nprint(\"unit rows of the sessions shared with the earlier release:\", int(n_old_rel), \"(Faraut et al. abstract: 1576 neurons)\")\nprint(\"variant, differences of the stated totals: sessions 87 - 65 =\", 87 - 65, \"; subjects 59 - 42 =\", 59 - 42, \"; neurons 1863 - 1576 =\", 1863 - 1576)\nprint(\"variant, differences of the counts here: sessions\", len(dandi_sess) - len(F1), \"; subjects\", dandi_sess.label_d.nunique() - F1.label.nunique(),\n      \"; neurons\", int(dandi_sess.units.sum()) - 1576)\n\"\"\", tag=\"claim:previous-release-additions\")\n\nmd(\"\"\"\n**Result: partially reproduced.** The dandiset adds 23 sessions and 17 subjects to the earlier release, as\nstated, but those sessions hold 325 unit rows, above the tolerance of 288 (259 to 317). The sessions shared\nwith the earlier release hold 1539 unit rows, 37 fewer than its stated 1576 neurons.\n\"\"\")\n\nmd(\"\"\"\n## fig4-example-vs-neuron\n\n> Neuron 132-177-4-RA (session 132, channel 177, cell 4, right amygdala) is visually selective, responding\n> most to images of animals.\n\nCriterion: the unit on channel 177 of session 132 with electrode row 4, in the right amygdala; ANOVA across\nthe 5 categories of recognition trials p < 0.05 (Methods' window) with animals the highest mean rate. The\ncode's window is a variant.\n\"\"\")\n\ncode(r\"\"\"\ns132 = [s for s in sessions if s[\"sid\"] == 132][0]\ne, u = s132[\"electrodes\"], s132[\"units\"]\nu = u.assign(channel=e.origChannel.values[u.electrode_row.values], location=e.location.values[u.electrode_row.values])\nprint(s132[\"identifier\"], \"units:\")\nprint(u[[\"id\", \"origClusterID\", \"electrode_row\", \"channel\", \"location\", \"n_spikes\"]].to_string(index=False))\ncand = u[(u.channel == 177) & (u.electrode_row == 4)]\nprint(\"units on channel 177 with electrode row 4:\", len(cand))\ni = int(cand.index[0])\nr = C.recog(s132[\"trials\"])\nnames = dict(zip(r.stimCategory, r.category_name))\nfor wl, w in ((\"Methods' window\", C.WINDOW_METHODS), (\"code's window\", C.WINDOW_CODE)):\n    rt = C.window_rates(s132[\"spikes\"][i], r.start_time.values, w)\n    p = C.anova_p(rt, r.stimCategory.values)\n    means = pd.Series(rt).groupby(r.stimCategory.values).mean().rename(index=names)\n    print(f\"{wl}: ANOVA p = {p:.2g}; mean rate by category (Hz): {means.round(2).to_dict()}; highest: {means.idxmax()}\")\n\"\"\", tag=\"claim:fig4-example-vs-neuron\")\n\nmd(\"\"\"\n**Result: reproduced.** Session 132 (CS58_132) holds one unit on channel 177, at electrode row 4 in the right\namygdala. Its recognition rate differs across categories (ANOVA p printed above, below 0.05 in both windows)\nand is highest for animals.\n\"\"\")\n\nmd(\"\"\"\n## fig3-example-vs-neuron\n\n> Neuron 144-140-3-RH (session 144, channel 140, cell 3, right hippocampus) is visually selective for phones.\n\"\"\")\n\ncode(r\"\"\"\nprint(\"session 144 among the dandiset's sessions:\", 144 in set(sess.session), \"; in Online-only Table 1:\", 144 in set(T1.session),\n      \"; in Faraut et al. Table 1:\", 144 in set(F1.session))\nprint(\"highest session id below 2000 in the dandiset:\", sess[sess.session < 2000].session.max())\n\"\"\", tag=\"claim:fig3-example-vs-neuron\")\n\nmd(\"\"\"\n**Result: blocked (data missing).** Session 144 is not in the dandiset, nor in either paper's session table,\nso the neuron cannot be found.\n\"\"\")\n\nmd(\"## Summary\")\n\ncode(r\"\"\"\nprint(\"notebook ran in %.1f min; peak memory %.2f GB\" % ((time.time() - started) / 60, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6))\n\"\"\")\n\nmd(\"\"\"\n| Claim | Outcome |\n|---|---|\n| counts-neurons-subjects | reproduced (1864 unit rows, 59 subjects) |\n| counts-sessions | reproduced (the 87 sessions of Online-only Table 1) |\n| table1-demographics | partially reproduced (3 of 59 subjects differ in age or sex) |\n| task-structure | partially reproduced (8 sessions lack encoding trials) |\n| new-old-label-coding | not reproduced (label 1 is old) |\n| ttl-codes | partially reproduced (10 files hold unlisted codes) |\n| experiment-ids | partially reproduced (4 files use other ids) |\n| session-dates | partially reproduced (one file on the 13th; one dated 2000) |\n| units-table | partially reproduced (quality metrics missing or not finite) |\n| electrodes-table | not reproduced (impedance empty for every electrode) |\n| isi-criterion | partially reproduced (6 of 1864 units at or above 3%) |\n| fig5a-mtl-locations | reproduced |\n| fig5c-auc-all | reproduced (0.753 ± 0.094) |\n| fig5c-auc-sites | reproduced (CS 0.760 ± 0.085, TWH 0.688 ± 0.138) |\n| fig5b-roc-asymmetric | reproduced (mean z-ROC slope 0.73) |\n| fig5d-confidence-accuracy | reproduced (paired p below 0.001 under both splits) |\n| vs-cells-proportion | reproduced (332, 17.8%) |\n| ms-cells-proportion | not reproduced (115, 6.2%; the code's correct-trial selection gives 145) |\n| dual-cells-proportion | not reproduced (12; the code's choices give 24) |\n| fig5f-site-proportions | partially reproduced (no difference between sites; 3 of 6 values within tolerance) |\n| twh-sessions | reproduced (9) |\n| previous-release-link | partially reproduced (64 of 65 sessions) |\n| previous-release-additions | partially reproduced (23 sessions and 17 subjects; 325 neurons) |\n| fig4-example-vs-neuron | reproduced |\n| fig3-example-vs-neuron | blocked: session 144 is not in the dandiset |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the\ndifferences from the paper's method.\n\nHow the analysis differs from the paper's: the AUC, z-ROC and accuracy computations follow the paper's code,\nwith label 1 taken as old as the code does. The MS test follows the Methods (all 50 and 50 trials) as the\nclaims file asks; the paper's code uses correct trials only, and that variant matches the paper's counts.\nEvery unit row is counted, as the paper counts neurons per session; the units of the duplicated sessions\nare shown counted once as a variant.\n\nWhat was found about the dataset: the new/old label coding is the reverse of the paper's text and the\ncolumn's description; the impedance column is empty; IsolationDist and SNR are missing or not finite for\nmany units; 8 sessions hold fewer than 100 encoding trials; some event streams hold codes outside Table 1\nand four files use experiment ids outside Table 2; two session dates break the stated rule; the spike times\nof 13 units are not in time order; sessions 43 and 44 and sessions 54 and 55 hold the same spike trains for\nevery unit, and sessions 38 and 39 share 11 of their units; the subject metadata of H48 (32, F) disagrees\nwith both papers (54, M); and session 98 of the earlier release is not in the dandiset.\n\"\"\")\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"display_name\": \"Python 3\", \"language\": \"python\", \"name\": \"python3\"}\nnbf.write(nb, OUT)\nprint(\"wrote\", OUT, len(cells), \"cells\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && echo $TMPDIR && . dev/bin/activate && python build_nb.py && cd entries/chandravadia-2020 && time jupyter nbconvert --to notebook --execute reproduce_chandravadia_2020.ipynb --output-dir $TMPDIR/exec --ExecutePreprocessor.timeout=3000 2>&1 | tail -5
```

```
/tmp/claude-1001
wrote entries/chandravadia-2020/reproduce_chandravadia_2020.ipynb 93 cells
[NbConvertApp] Making directory /tmp/claude-1001/exec
[NbConvertApp] Converting notebook reproduce_chandravadia_2020.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 188543 bytes to /tmp/claude-1001/exec/reproduce_chandravadia_2020.ipynb

real	2m7.720s
user	0m39.126s
sys	0m1.211s
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'E'
import json
nb=json.load(open('exec/reproduce_chandravadia_2020.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    out=''
    for o in c.get('outputs',[]):
        if 'text' in o: out+=''.join(o['text'])
        elif o.get('output_type')=='error': out+='ERROR '+o['ename']+o['evalue']
        elif 'data' in o and 'text/plain' in o['data'] and 'image/png' not in o['data']: out+=''.join(o['data']['text/plain'])
    print(f'=== cell {i} {c["metadata"].get("tags","")}'); print(out[:6000])
E
```

```
<persisted-output>
Output too large (34.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/ce3dc8ea-96db-4b0d-ab7a-348e333948cf/tool-results/b12uq2lr2.txt

Preview (first 2KB):
=== cell 1 

=== cell 3 
dandiset 000004 version 0.220126.1852, doi 10.48324/dandi.000004/0.220126.1852
assets: 87  total size 6.20 GB
archive's summary: subjects 59  files 87
read 87 files in 89 s; peak memory 0.28 GB

One file, sub-P10HMH/sub-P10HMH_ses-20060901_ecephys+image.nwb
  trials columns: ['start_time', 'stop_time', 'stim_on_time', 'stim_off_time', 'delay1_time', 'delay2_time', 'stim_phase', 'stimCategory', 'category_name', 'external_image_file', 'new_old_labels_recog', 'response_value', 'response_time']
  electrodes columns: ['x', 'y', 'z', 'imp', 'location', 'filtering', 'group', 'group_name', 'origChannel']
  units columns: ['origClusterID', 'waveform_mean_encoding', 'waveform_mean_recognition', 'IsolationDist', 'SNR', 'waveform_mean_sampling_rate', 'spike_times', 'electrodes']
  subject fields: {'age': '37', 'description': 'Left Lateral Frontal', 'sex': 'M', 'species': 'Human', 'subject_id': 'P10HMH'}
  stimulus series: {'StimulusPresentation': (200, 400, 300, 3)}  devices: ['Neuralynx-cheetah']
  data_collection: 'learning: 80, recognition: 81'
  new_old_labels_recog description: "The Ground truth Labels for New or Old Stimulus. 0 == Old Stimuli \n                            (presented during the learning phase), 1 = New Stimuli (not seen )'during learning phase"
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/=== cell 5/,$p' /home/runner/.claude/projects/-home-runner-work-encore-encore/ce3dc8ea-96db-4b0d-ab7a-348e333948cf/tool-results/b12uq2lr2.txt | grep -v "^ *[0-9]\+ \+[A-Z]\+[0-9]\+_[0-9]\+ \+P[0-9]\|^ *[0-9]\+ \+T[0-9]\+_" | head -400
```

```
Permission for this tool use was denied. It requires approval, and this session has no approval surface — nobody can answer a permission prompt here — so it was denied automatically. The action was NOT performed; do not claim it succeeded, and do not retry it: this action, and anything else that requires approval, will be denied the same way for the rest of this session. Tell the user what was blocked and why you needed it, then continue with the parts of the task that do not require approval. What required approval: This Bash command contains multiple operations. The following part requires approval: sed -n '/=== cell 5/,$p' /home/runner/.claude/projects/-home-runner-work-encore-encore/ce3dc8ea-96db-4b0d-ab7a-348e333948cf/tool-results/b12uq2lr2.txt
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/ce3dc8ea-96db-4b0d-ab7a-348e333948cf/tool-results/b12uq2lr2.txt",
 "offset": 110
}
```

```
110	1   H09        6        2           2   55   M  Right Mesial Temporal
111	2   H10        7        1           1   37   M           Left Frontal
112	
113	=== cell 14 ['claim:counts-neurons-subjects']
114	(a) unit rows: 1864 (expected 1863 +/- 186.3; difference +1)
115	(b) duplicated trains counted once: 1798 (difference -65)
116	subjects (distinct subject_id): 59 (expected 59 +/- 5.9)
117	units by subject: min 1  max 123
118	
119	=== cell 17 ['claim:counts-sessions']
120	pairs in the files: 87  in Online-only Table 1: 87
121	in the files only: []  in the table only: []
122	sets equal: True ; the Methods' 89 differs from the count by 2
123	
124	=== cell 20 ['claim:table1-demographics']
125	files with more than one age or sex for a subject: 0
126	subjects: 59  age matches: 56  sex matches: 58  both: 56
127	      age_file  age_table sex_file sex_table
128	label                                       
129	C24         57         47        F         F
[... 343 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'E'
import sys, pickle, numpy as np, pandas as pd, collections
sys.path.insert(0,'entries/chandravadia-2020')
import chandravadia as C
a,S=pickle.load(open('sessions.pkl','rb'))
cnt=collections.Counter()
for s in S:
    ev,et=s['events'],s['events_t']
    for k,row in s['trials'].iterrows():
        sel=(et>=row.start_time-1e-3)&(et<=row.delay2_time+1e-3)
        seq=ev[sel].astype(int).tolist()
        resp={20,21} if row.stim_phase=='learn' else set(range(31,37))
        ok=len(seq)==5 and seq[:3]==[1,2,3] and seq[3] in resp and seq[4]==6
        if not ok:
            i0=np.searchsorted(et,row.start_time-1e-3)
            ctx=list(zip(ev[max(0,i0-2):i0+8].astype(int), np.round(et[max(0,i0-2):i0+8]-row.start_time,3)))
            cnt[(row.stim_phase, k in (0,99,100,199,len(s['trials'])-1), tuple(seq))]+=1
            if s['identifier'] in ('CS42_111','T88_2002','CS38_102') : print(s['identifier'],k,row.stim_phase, seq, ctx, round(row.delay2_time-row.start_time,3))
for k,v in cnt.most_common(30): print(v,k)
E
```

```
CS38_102 99 learn [1, 2, 3, 21, 6, 66] [(np.int64(21), np.float64(-1.065)), (np.int64(6), np.float64(-0.062)), (np.int64(1), np.float64(0.0)), (np.int64(2), np.float64(2.004)), (np.int64(3), np.float64(2.546)), (np.int64(21), np.float64(3.222)), (np.int64(6), np.float64(4.224)), (np.int64(66), np.float64(4.225)), (np.int64(55), np.float64(309.39)), (np.int64(1), np.float64(310.374))] 4.224
CS38_102 199 recog [1, 2, 3, 31, 6, 66] [(np.int64(36), np.float64(-1.065)), (np.int64(6), np.float64(-0.062)), (np.int64(1), np.float64(0.0)), (np.int64(2), np.float64(2.004)), (np.int64(3), np.float64(2.559)), (np.int64(31), np.float64(4.453)), (np.int64(6), np.float64(5.456)), (np.int64(66), np.float64(5.457))] 5.456
CS42_111 63 learn [1, 2, 3, 20, 6, 1] [(np.int64(21), np.float64(-1.036)), (np.int64(6), np.float64(-0.033)), (np.int64(1), np.float64(0.0)), (np.int64(2), np.float64(2.003)), (np.int64(3), np.float64(2.518)), (np.int64(20), np.float64(3.2)), (np.int64(6), np.float64(4.203)), (np.int64(1), np.float64(4.203)), (np.int64(2), np.float64(6.237)), (np.int64(3), np.float64(6.756))] 4.203
CS42_111 64 learn [6, 1, 2, 3, 21, 6] [(np.int64(3), np.float64(-1.684)), (np.int64(20), np.float64(-1.003)), (np.int64(6), np.float64(0.0)), (np.int64(1), np.float64(0.0)), (np.int64(2), np.float64(2.034)), (np.int64(3), np.float64(2.553)), (np.int64(21), np.float64(2.553)), (np.int64(6), np.float64(4.267)), (np.int64(1), np.float64(4.299)), (np.int64(2), np.float64(6.302))] 4.267
CS42_111 65 learn [1, 2, 3, 21, 6, 1] [(np.int64(21), np.float64(-1.746)), (np.int64(6), np.float64(-0.032)), (np.int64(1), np.float64(0.0)), (np.int64(2), np.float64(2.003)), (np.int64(3), np.float64(2.517)), (np.int64(21), np.float64(3.313)), (np.int64(6), np.float64(4.316)), (np.int64(1), np.float64(4.316)), (np.int64(2), np.float64(6.36)), (np.int64(3), np.float64(6.873))] 4.316
CS42_111 66 learn [6, 1, 2, 3, 21, 6] [(np.int64(3), np.float64(-1.798)), (np.int64(21), np.float64(-1.003)), (np.int64(6), np.fl
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'E'
import sys, pickle, numpy as np, pandas as pd, collections
sys.path.insert(0,'entries/chandravadia-2020')
import chandravadia as C
a,S=pickle.load(open('sessions.pkl','rb'))
cnt=collections.Counter(); per={}
for s in S:
    ev=s['events'].astype(int); keep=~np.isin(ev,[55,66]); e=ev[keep]
    starts=np.where(e==1)[0]; segs=[e[a:b].tolist() for a,b in zip(starts, list(starts[1:])+[len(e)])]
    pre=e[:starts[0]].tolist() if len(starts) else e.tolist()
    ph=s['trials'].stim_phase.values
    bad=0
    for k,seg in enumerate(segs):
        resp={20,21} if (k<len(ph) and ph[k]=='learn') else set(range(31,37))
        ok=len(seg)==5 and seg[:3]==[1,2,3] and seg[3] in resp and seg[4]==6
        if not ok: bad+=1; cnt[tuple(seg)]+=1
    per[s['identifier']]=(len(segs),len(ph),bad,pre, ev[:2].tolist(), int((ev==55).sum()), int((ev==66).sum()))
for k,v in per.items():
    if v[0]!=v[1] or v[2] or v[3] or v[5]!=2 or v[6]!=2: print(k,v)
print(cnt.most_common(20))
E
```

```
H23_43 (200, 200, 1, [], [55, 1], 2, 2)
H27_58 (200, 200, 1, [], [55, 1], 2, 2)
CS37_96 (200, 200, 0, [], [1, 2], 0, 2)
CS39_93 (200, 200, 1, [99], [99, 1], 0, 2)
CS39_100 (200, 200, 0, [], [1, 2], 0, 2)
CS40_101 (200, 200, 0, [], [1, 2], 0, 2)
H47_92 (200, 200, 0, [], [1, 2], 0, 2)
H47_97 (200, 200, 0, [], [1, 2], 0, 2)
H48_99 (200, 200, 0, [], [1, 2], 0, 2)
CS53_123 (197, 197, 1, [21, 6], [21, 6], 1, 2)
CS55_127 (200, 200, 1, [], [55, 1], 2, 2)
CS56_128 (200, 200, 1, [], [55, 1], 2, 2)
T88_2001 (200, 200, 7, [], [55, 1], 2, 3)
T88_2002 (200, 200, 10, [], [55, 1], 2, 2)
T90_2003 (200, 200, 7, [], [55, 1], 2, 2)
[((1, 3, 2, 3, 21, 6), 6), ((1, 2, 3, 21, 23, 6), 4), ((1, 3, 2, 3, 33, 6), 4), ((1, 3, 2, 3, 34, 6), 2), ((1, 3, 2, 3, 31, 6), 2), ((1, 3, 2, 3, 36, 6), 2), ((1, 2, 3, 21, 6, 99, 98), 1), ((1, 2, 3, 23, 21, 6), 1), ((1, 2, 3, 21, 6, 99), 1), ((1, 2, 3, 32, 0, 6), 1), ((1, 0, 2, 3, 35, 6), 1), ((1, 2, 3, 36, 4, 6), 1), ((1, 2, 3, 20, 22, 6), 1), ((1, 3, 2, 3, 21, 23, 6), 1), ((1, 3, 2, 3, 32, 6), 1), ((1, 3, 2, 3, 35, 6), 1)]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'E'
p='build_nb.py'; s=open(p).read()
old_start=s.index('listed = {55, 1, 2, 3, 20, 21')
old_end=s.index('""", tag="claim:ttl-codes")')
new='''listed = {55, 1, 2, 3, 20, 21, 31, 32, 33, 34, 35, 36, 6, 66}
tt = []
for s in sessions:
    ev, et = s["events"].astype(int), s["events_t"]
    same = len(ev) == len(s["expids"]) and np.allclose(et, s["expids_t"])
    extra = sorted(set(np.unique(ev)) - listed)
    # trial events: the stream without the experiment markers 55 and 66, cut at each stimulus onset (1)
    e = ev[~np.isin(ev, [55, 66])]
    starts = np.where(e == 1)[0]
    segs = [e[a:b].tolist() for a, b in zip(starts, list(starts[1:]) + [len(e)])]
    phase = s["trials"].stim_phase.values
    bad, examples = 0, []
    for k, seg in enumerate(segs):
        resp = {20, 21} if k < len(phase) and phase[k] == "learn" else {31, 32, 33, 34, 35, 36}
        if not (len(seg) == 5 and seg[:3] == [1, 2, 3] and seg[3] in resp and seg[4] == 6):
            bad += 1
            examples.append(seg)
    tt.append(dict(identifier=s["identifier"], n_events=len(ev), same_length_and_times=same, extra_codes=extra,
                   trials=len(phase), onsets=len(segs), events_before_first_onset=e[:starts[0]].tolist() if len(starts) else e.tolist(),
                   trials_bad_sequence=bad, n55=int((ev == 55).sum()), n66=int((ev == 66).sum()),
                   example=examples[0] if examples else None))
tt = pd.DataFrame(tt)
tt["ok"] = (tt.same_length_and_times & (tt.extra_codes.str.len() == 0) & (tt.trials_bad_sequence == 0)
            & (tt.onsets == tt.trials) & (tt.events_before_first_onset.str.len() == 0))
print("files where events and experiment_ids have the same length and timestamps:", int(tt.same_length_and_times.sum()), "of", len(tt))
print("files with only the listed codes:", int((tt.extra_codes.str.len() == 0).sum()))
print("files with one stimulus onset per trial:", int((tt.onsets == tt.trials).sum()))
print("files where every trial has the sequence 1, 2, 3, response of its phase, 6:", int(((tt.trials_bad_sequence == 0) & (tt.events_before_first_onset.str.len() == 0)).sum()))
print("files meeting the whole criterion:", int(tt.ok.sum()))
print("trials failing the sequence, all files:", int(tt.trials_bad_sequence.sum()), "of", int(tt.trials.sum()))
print(tt[~tt.ok].drop(columns=["ok"]).to_string())
print("\\ncounts of the unlisted codes over all files:", dict(Counter(int(x) for s in sessions for x in s["events"] if int(x) not in listed)))
print("files with two 55 markers:", int((tt.n55 == 2).sum()), "; with none:", tt[tt.n55 == 0].identifier.tolist(), "; with one:", tt[tt.n55 == 1].identifier.tolist())
print("files with two 66 markers:", int((tt.n66 == 2).sum()), "; others:", tt[tt.n66 != 2][["identifier", "n66"]].to_dict("records"))
'''
s=s[:old_start]+new+s[old_end:]
s=s.replace('''delay2_time (the end of the trial), with 1 ms of slack.''','''next stimulus onset, with the experiment markers 55 and 66 set aside (the k-th onset is the k-th trial).''')
s=s.replace('''partially reproduced when this holds in most files. A trial's events are those from its start_time to its
''','''partially reproduced when this holds in most files. A trial's events are those from its stimulus onset (1) to the
''')
# ms seeds
old_start=s.index('seeds = []\nfor seed in (1, 2, 3, 4):')
old_end=s.index('for site, gg in cells.groupby("site"):\n    print(f"  {site}: {int((gg.ms_m')
new='''def n_ms(seed, window, correct_only):
    rg = np.random.default_rng(seed)
    n = 0
    for s in sessions:
        r = C.recog(s["trials"])
        old = (r.label == 1).values
        use = (((r.conf <= 3) & ~old) | ((r.conf >= 4) & old)).values if correct_only else np.ones(len(r), bool)
        for sp in s["spikes"]:
            rt = C.window_rates(sp, r.start_time.values, window)
            n += C.bootstrap_mean_equal(rt[old & use], rt[~old & use], 1000, rg) < 0.05
    return int(n)
for label, w, co in (("main reading", C.WINDOW_METHODS, False), ("correct trials, Methods' window", C.WINDOW_METHODS, True),
                     ("the code's choices", C.WINDOW_CODE, True)):
    print(f"{label}, seeds 1 to 4:", [n_ms(seed, w, co) for seed in (1, 2, 3, 4)])
'''
s=s[:old_start]+new+s[old_end:]
open(p,'w').write(s)
E
grep -n "seeds 1 to 4\|onsets == tt.trials" build_nb.py | head
```

```
507:            & (tt.onsets == tt.trials) & (tt.events_before_first_onset.str.len() == 0))
510:print("files with one stimulus onset per trial:", int((tt.onsets == tt.trials).sum()))
954:    print(f"{label}, seeds 1 to 4:", [n_ms(seed, w, co) for seed in (1, 2, 3, 4)])
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python build_nb.py && cd entries/chandravadia-2020 && jupyter nbconvert --to notebook --execute reproduce_chandravadia_2020.ipynb --output-dir $TMPDIR/exec --ExecutePreprocessor.timeout=3000 2>&1 | tail -1; cd $TMPDIR && python3 - <<'E'
import json
nb=json.load(open('exec/reproduce_chandravadia_2020.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    tags=c['metadata'].get('tags',[])
    if not any(t in ('claim:ttl-codes','claim:ms-cells-proportion','claim:dual-cells-proportion','claim:fig5f-site-proportions','claim:vs-cells-proportion') for t in tags) and i not in (62,91): continue
    out=''
    for o in c.get('outputs',[]):
        if 'text' in o: out+=''.join(o['text'])
        elif o.get('output_type')=='error': out+='ERROR '+o['ename']+o['evalue']
    print(f'=== cell {i} {tags}'); print(out[:5000])
E
```

```
wrote entries/chandravadia-2020/reproduce_chandravadia_2020.ipynb 93 cells
[NbConvertApp] Writing 187092 bytes to /tmp/claude-1001/exec/reproduce_chandravadia_2020.ipynb
=== cell 29 ['claim:ttl-codes']
files where events and experiment_ids have the same length and timestamps: 87 of 87
files with only the listed codes: 78
files with one stimulus onset per trial: 87
files where every trial has the sequence 1, 2, 3, response of its phase, 6: 78
files meeting the whole criterion: 78
trials failing the sequence, all files: 30 of 17047
   identifier  n_events  same_length_and_times extra_codes  trials  onsets events_before_first_onset  trials_bad_sequence  n55  n66                   example
15     H23_43      1006                   True    [98, 99]     200     200                        []                    1    2    2  [1, 2, 3, 21, 6, 99, 98]
25     H27_58      1005                   True        [23]     200     200                        []                    1    2    2      [1, 2, 3, 23, 21, 6]
40    CS39_93      1004                   True        [99]     200     200                      [99]                    1    0    2      [1, 2, 3, 21, 6, 99]
62   CS53_123       991                   True         [0]     197     197                   [21, 6]                    1    1    2       [1, 2, 3, 32, 0, 6]
67   CS55_127      1005                   True         [0]     200     200                        []                    1    2    2       [1, 0, 2, 3, 35, 6]
68   CS56_128      1005                   True         [4]     200     200                        []                    1    2    2       [1, 2, 3, 36, 4, 6]
78   T88_2001      1013                   True    [22, 23]     200     200                        []                    7    2    3       [1, 3, 2, 3, 21, 6]
79   T88_2002      1014                   True        [23]     200     200                        []                   10    2    2      [1, 2, 3, 21, 23, 6]
81   T90_2003      1011                   
[... 76 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'E'
p='build_nb.py'; s=open(p).read()
reps=[
('''**Result: partially reproduced.** In all 87 files the two streams have the same length and timestamps. 77
files meet the whole criterion; 10 files hold codes not in Table 1 (0, 4, 22, 23, 98 and 99, listed above),
and in those files some trials do not show the full sequence. The criterion holds in most files.''',
'''**Result: partially reproduced.** In all 87 files the two streams have the same length and timestamps, and 78
files meet the whole criterion. Nine files hold codes not in Table 1 (0, 4, 22, 23, 98 and 99), and 30 of
17047 trials, all in those files, break the sequence: in T88_2001, T88_2002 and T90_2003 a second 3 comes
before the 2, and CS53_123 starts in the middle of a trial. Seven files have no 55 marker, which the
criterion does not require.'''),
('''**Result: reproduced.** Over the 82 sessions with a slope, the mean z-ROC slope is 0.726, below 1
(t-test against 1, p = 1e-9; Wilcoxon p = 2e-9). The pooled ROC has a slope of 0.84. Five sessions with
equal false alarm rates at every criterion were left out.''',
'''**Result: reproduced.** Over the 82 sessions with a slope, the mean z-ROC slope is 0.782, below 1
(t-test against 1, p = 4e-9; Wilcoxon p = 2e-8). The pooled ROC has a slope of 0.816. Five sessions with
equal false alarm rates at every criterion were left out.'''),
('''**Result: not reproduced.** With all 50 and 50 trials in the Methods' window, 115 of 1864 units (6.2%) are
MS cells, below the tolerance of 146 (131 to 161); other seeds give 113 to 121. The paper's code compares
only correctly answered trials, and with that selection 145 units (7.8%) qualify in either window, a
match. The shuffled null gives 5%.''',
'''**Result: not reproduced.** With all 50 and 50 trials in the Methods' window, 110 of 1864 units (5.9%) are
MS cells, below the tolerance of 146 (131 to 161); four other seeds give 109 to 111. With the paper's code's
choices (correct trials only, 200 to 1700 ms) 147 units (7.9%) qualify, 143 to 147 over the other seeds, a
match. Correct trials in the Methods' window give 132 to 147 depending on the seed. The shuffled null gives
4.4%.'''),
('''**Result: not reproduced.** 12 units (0.64%) are selected by both main tests, against 26 (1.4%). With the
code's choices for both tests 24 units (1.29%) qualify, within tolerance.''',
'''**Result: not reproduced.** 12 units (0.64%) are selected by both main tests, against 26 (1.4%). With the
code's choices for both tests 26 units (1.39%) qualify, as the paper states.'''),
('''**Result: partially reproduced.** No Fisher's exact test finds a difference between the sites (p from 0.3
to 0.5 in the main reading), but only 3 of the 6 percentages are within tolerance: CS has 17.6% VS, 6.0% MS
and 0.62% dual cells, TWH 22.1%, 10.4% and 1.3%. TWH has 77 units, so one cell moves its percentages by 1.3
points. With the code's choices 4 of 6 are within tolerance and no test finds a difference.''',
'''**Result: partially reproduced.** No Fisher's exact test finds a difference between the sites (p = 0.36,
0.46 and 1.0 in the main reading), but only 1 of the 6 percentages is within tolerance: CS has 17.6% VS,
5.8% MS and 0.67% dual cells, TWH 22.1%, 7.8% and 0%. TWH has 77 units, so one cell moves its percentages by
1.3 points. With the code's choices all 6 values are within tolerance (CS 18.35%, 7.78%, 1.40%; TWH 19.48%,
10.39%, 1.30%) and no test finds a difference.'''),
('''| ttl-codes | partially reproduced (10 files hold unlisted codes) |''','''| ttl-codes | partially reproduced (9 files hold unlisted codes) |'''),
('''| fig5b-roc-asymmetric | reproduced (mean z-ROC slope 0.73) |''','''| fig5b-roc-asymmetric | reproduced (mean z-ROC slope 0.78) |'''),
('''| ms-cells-proportion | not reproduced (115, 6.2%; the code's correct-trial selection gives 145) |''','''| ms-cells-proportion | not reproduced (110, 5.9%; the code's choices give 147) |'''),
('''| dual-cells-proportion | not reproduced (12; the code's choices give 24) |''','''| dual-cells-proportion | not reproduced (12; the code's choices give 26) |'''),
('''| fig5f-site-proportions | partially reproduced (no difference between sites; 3 of 6 values within tolerance) |''','''| fig5f-site-proportions | partially reproduced (no difference between sites; 1 of 6 values within tolerance) |'''),
('''with label 1 taken as old as the code does. The MS test follows the Methods (all 50 and 50 trials) as the
claims file asks; the paper's code uses correct trials only, and that variant matches the paper's counts.''',
'''with label 1 taken as old as the code does. The VS and MS tests follow the Methods (a 1 s window, and all 50
and 50 trials for MS) as the claims file asks; the paper's code uses a 1.5 s window and correct trials only
for MS, and with those choices the counts and the per-site percentages of Figure 5f are matched.'''),
]
for a,b in reps:
    assert a in s, a[:60]
    s=s.replace(a,b)
open(p,'w').write(s)
E
```

```
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'E'
p='build_nb.py'; s=open(p).read()
reps=[
('''trials show encoding images, and in all 87 sessions label 1 trials do and receive more "old" responses
(86 of 87 hold both tests reversed; in T98_2005 the response test fails, 0.68 against 0.72).''',
'''trials show encoding images; label 1 trials do in all 87 sessions, and receive more "old" responses in 86
(both tests hold reversed in 86 of 87; in T98_2005 the response test fails, 0.68 against 0.72).'''),
('''do not follow the task variant: most variant 2 and 3 sessions recorded at Cedars-Sinai use 80 and 81.''',
'''do not follow the task variant: 7 of the 20 variant 2 sessions and 18 of the 25 variant 3 sessions use 80
and 81.'''),
('''SNR is infinite for some units, and a few isolation distances are above 1e6, which is not a plausible
value.''','''SNR is infinite for 11 units, and 2 isolation distances are above 1e6, which is not a plausible value.'''),
('''intervals below 3 ms; 6 units do not, one with 50%.''','''intervals below 3 ms; 6 units do not, two of them with about 50%.'''),
('''The code's window gives 343 (18.4%), and the shuffled null 5%.''','''The code's window gives 343 (18.4%), and the shuffled null 4.8%.'''),
]
for a,b in reps:
    assert a in s, a[:60]
    s=s.replace(a,b)
open(p,'w').write(s)
E
date -u
```

```
Sat Nov 14 13:22:10 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'E'
p='build_nb.py'; s=open(p).read()
a='''print("archive's summary: subjects", meta["assetsSummary"]["numberOfSubjects"], " files", meta["assetsSummary"]["numberOfFiles"])
'''
b=a+'''other = C.list_assets("0.220126.1851")
same = set(zip(other.path, other["size"], other.asset_id)) == set(zip(assets.path, assets["size"], assets.asset_id))
print("version 0.220126.1851, published the same day:", len(other), "assets; same paths, sizes and asset ids as", C.VERSION, ":", same)
'''
assert a in s; s=s.replace(a,b)
s=s.replace('''published version, created a few seconds after 0.220126.1851 on 2022-01-26. Earlier versions were not
compared.''','''published version, created a few seconds after 0.220126.1851 on 2022-01-26; the notebook shows that the two
versions list the same assets.''')
a='''**Result: reproduced.** Session 132 (CS58_132) holds one unit on channel 177, at electrode row 4 in the right
amygdala. Its recognition rate differs across categories (ANOVA p printed above, below 0.05 in both windows)
and is highest for animals.'''
b='''**Result: reproduced.** Session 132 (CS58_132) holds one unit on channel 177, at electrode row 4 in the right
amygdala. Its recognition rate differs across categories (ANOVA p = 1.2e-22 in the Methods' window, 7.9e-19
in the code's) and is highest for animals (6.75 Hz, against 0.85 Hz or less for the other categories).'''
assert a in s; s=s.replace(a,b)
open(p,'w').write(s)
p='entries/chandravadia-2020/chandravadia.py'; s=open(p).read()
a='''def list_assets() -> pd.DataFrame:
    """Every asset of the pinned version, with its path, size and identifier."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200"'''
b='''def list_assets(version: str = VERSION) -> pd.DataFrame:
    """Every asset of a version (the pinned one by default), with its path, size and identifier."""
    url = f"{API}/dandisets/{DANDISET}/versions/{version}/assets/?page_size=200"'''
assert a in s; s=s.replace(a,b); open(p,'w').write(s)
E
```

```
Shell cwd was reset to
```

**Agent**

Now the entry files.

**Agent calls Bash**

```bash
cd entries/chandravadia-2020 && cat > requirements.in <<'E'
h5py
matplotlib
numpy
pandas
remfile
requests
scipy
E
cat > entry.yaml <<'E'
schema_version: 1
name: chandravadia-2020
type: reproduction
title: Human MTL single neurons during a recognition memory task (Chandravadia et al. 2020)
description: Tests the claims of Chandravadia et al. (2020) on dandiset 000004, which holds 87
  sessions of single-neuron recordings from the human amygdala and hippocampus during a new/old
  recognition memory task. It checks the file contents against the data descriptor (sessions,
  subjects, trials, event codes, units and electrode tables), the behavioural ROC analyses, and
  the proportions of visually and memory selective cells.
license: Apache-2.0
notebooks:
- path: reproduce_chandravadia_2020.ipynb
  title: Reproducing Chandravadia et al. (2020) from dandiset 000004
  runtime_minutes: 3
helpers:
- chandravadia.py
related:
- id: dandi:000004/0.220126.1852
  relation: uses_data
- id: doi:10.1038/s41597-020-0415-9
  relation: reproduces
E
cd $TMPDIR && . dev/bin/activate && python build_nb.py && cd  && python tools/entry.py lock entries/chandravadia-2020 2>&1 | tail -3 && cat entries/chandravadia-2020/entry.yaml | grep python
```

```
wrote entries/chandravadia-2020/reproduce_chandravadia_2020.ipynb 93 cells
  File "tools/entry.py", line 59, in <module>
    import yaml
ModuleNotFoundError: No module named 'yaml'
```

**Agent calls Bash**

```bash
ls .venv 2>/dev/null; grep -n "dependencies" -A12 pyproject.toml | head -20
```

```
12:dependencies = [
13-  "pyyaml",
14-  "jsonschema",
15-  "nbformat",
16-  "uv",
17-  "pymupdf",
18-]
19-
20-[project.urls]
21-Homepage = "https://encorescience.org"
22-Source = "https://github.com/catalystneuro/encore"
23-
24-[project.scripts]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q tools && . tools/bin/activate && uv pip install -q pyyaml jsonschema nbformat 2>&1|tail -1; cd  && python tools/entry.py lock entries/chandravadia-2020 2>&1 | tail -3 && grep python entries/chandravadia-2020/entry.yaml
```

```
wrote chandravadia-2020/requirements.lock.txt (Python 3.13, with hashes)
python: "3.13"
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
o=s['properties']['outcomes']['items']; print(json.dumps(o['properties'],indent=0)[:3500]); print(o.get('required'))
f=s['properties']['findings']['items']; print(json.dumps(f,indent=0)[:2500])
print(json.dumps(s['properties']['inputs'],indent=0)[:800])
"
```

```
{
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
},
"blocked_by": {
"description": "Required when outcome is blocked.",
"enum": [
"data_missing",
"metadata_insufficient",
"methods_underspecified",
[... 156 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/make_attempt.py",
 "content": "import yaml\n\nNB = \"reproduce_chandravadia_2020.ipynb\"\n\n\ndef o(claim, outcome, notes, measured=None, deviations=None, blocked_by=None):\n    d = {\"claim\": claim, \"outcome\": outcome}\n    if blocked_by:\n        d[\"blocked_by\"] = blocked_by\n    d[\"notebook\"] = NB\n    d[\"output\"] = f\"claim:{claim}\"\n    if measured is not None:\n        d[\"measured\"] = measured\n    d[\"notes\"] = notes\n    if deviations:\n        d[\"deviations\"] = deviations\n    return d\n\n\noutcomes = [\n    o(\"counts-neurons-subjects\", \"reproduced\",\n      \"Reading (a), every unit row of every file, gives 1864 neurons, one more than 1863, and the files hold 59 distinct \"\n      \"subject_id values. Reading (b), with the 66 spike trains deposited in two files counted once, gives 1798, also within \"\n      \"tolerance. Units per subject range from 1 to 123.\",\n      [1864, 59]),\n    o(\"counts-sessions\", \"reproduced\",\n      \"The 87 (subject, session id) pairs of the file identifiers are exactly the 87 pairs of Online-only Table 1, read from the \"\n      \"Europe PMC full text. The Methods' 89 is 2 more than either.\",\n      87,\n      [\"The identifiers label Cedars-Sinai subjects CS24 and so on, where the table writes C24; the labels were mapped by this \"\n       \"spelling difference.\"]),\n    o(\"table1-demographics\", \"partially_reproduced\",\n      \"56 of 59 subjects match the table in both age and sex. C24 is 57 in the files against 47 in the table, H33 30 against 29, \"\n      \"and H48 is 32 and female in the files against 54 and male in the table (32 F is the table's entry for C48). The files count \"\n      \"26 female and 33 male subjects, the table 25 and 34; both counts are within tolerance. The diagnosis text differs in \"\n      \"wording for 19 of 59 subjects, as the files use a coarser coding.\",\n      [26, 33]),\n    o(\"task-structure\", \"partially_reproduced\",\n      \"79 of 87 sessions meet every part. All 87 have 100 recognition trials with 50 of each label and 5 categories. The encoding \"\n      \"part fails in 8 sessions, whose trial tables hold 50 encoding trials (H14_18, H15_20, H15_21, H16_23, H18_26, H19_27, \"\n      \"H23_44) or 97 (CS53_123); no image file repeats within any encoding block. Each part holds in more than half of the \"\n      \"sessions.\"),\n    o(\"new-old-label-coding\", \"not_reproduced\",\n      \"The coding is the reverse of the statement. Under the stated coding (0 = old) both tests hold in 0 of 87 sessions. With \"\n      \"the labels reversed, label 1 images are in the encoding block in all 87 sessions (all of them in 79; 52 to 58% in the 7 \"\n      \"sessions whose table holds 50 encoding trials, 98% in CS53_123) and label 0 images in none, and label 1 trials receive \"\n      \"more old responses in 86 of 87 (median 0.70 against 0.24; T98_2005 is the exception, 0.68 against 0.72, AUC 0.445). \"\n      \"Both tests hold reversed in 86 of 87 sessions. The paper's code also treats 1 as old.\"),\n    o(\"ttl-codes\", \"partially_reproduced\",\n      \"In all 87 files events and experiment_ids have the same length and timestamps, and every file has one stimulus onset per \"\n      \"trial. 78 files meet the whole criterion. Nine files (H23_43, H27_58, CS39_93, CS53_123, CS55_127, CS56_128, T88_2001, \"\n      \"T88_2002, T90_2003) hold codes outside Table 1 (99 three times, 23 six times, 0 twice, 98, 22 and 4 once each), and 30 of \"\n      \"17047 trials, all in those files, break the sequence; in T88_2001, T88_2002 and T90_2003 a second 3 comes before the 2, \"\n      \"and CS53_123 starts in the middle of a trial (its first events are 21 and 6). Seven files have no 55 marker and T88_2001 \"\n      \"has three 66 markers, which the criterion does not test.\",\n      deviations=[\"A trial's events were taken as those from its stimulus onset (1) to the next onset, with the experiment \"\n                  \"markers 55 and 66 set aside; the claims file does not say how trials are cut from the stream. Cutting at \"\n                  \"the trial table's start and end times gives more failures, from 55 and 66 markers and next-trial onsets \"\n                  \"that share a timestamp with a trial's end; this was seen while preparing and is not in the notebook.\"]),\n    o(\"experiment-ids\", \"partially_reproduced\",\n      \"In 83 of 87 files the learning and recognition ids fall in the stated sets, and all 83 use one of Table 2's pairs (80 and \"\n      \"81 in 65 files, 83 and 84 in 14, 88 and 89 in 4). CS33_77 uses 81 and 82, CS39_100 and H51_105 82 and 83, and H42_55 80 \"\n      \"and 82; their data_collection fields state these ids. The ids do not follow the task variant; 7 of 20 variant 2 and 18 \"\n      \"of 25 variant 3 sessions use 80 and 81.\",\n      deviations=[\"Each block's id was read at the TTL-1 events of its trials (learning or recognition by stim_phase), a \"\n                  \"standard choice; every file has exactly two ids.\"]),\n    o(\"session-dates\", \"partially_reproduced\",\n      \"86 of 87 files have a session_start_time on the first of a month; H28_48 is dated 2010-03-13. H44_68 is dated \"\n      \"2000-01-01, six years before any other file (the others span 2006 to 2019), so its year looks like a default.\"),\n    o(\"units-table\", \"partially_reproduced\",\n      \"Every file holds the columns, with IsolDist named IsolationDist (described as 'IsolDist'); every one of the 1864 units \"\n      \"links to exactly one electrode; the stated waveform sampling rate is 98400 Hz, within tolerance. The quality metrics are \"\n      \"not finite for every unit. IsolationDist is NaN for 493 units and SNR for 75, SNR is infinite for 11, and 2 isolation \"\n      \"distances exceed 1e6 (up to 8.1e32); 568 units in 84 files have a non-finite metric. The waveforms are finite.\",\n      98400,\n      [\"The column named IsolationDist is taken as the paper's IsolDist; the names differ only in spelling.\"]),\n    o(\"electrodes-table\", \"not_reproduced\",\n      \"The impedance column (imp) is NaN for all 887 electrodes of all 87 files, so one column is empty for every electrode. \"\n      \"Location, filtering (300-3000Hz) and origChannel are filled for every electrode; the MNI coordinates are missing for 99 \"\n      \"electrodes in 8 files.\"),\n    o(\"isi-criterion\", \"partially_reproduced\",\n      \"With spike times sorted, 1858 of 1864 units (99.68%) have fewer than 3% of interspike intervals below 3 ms; 6 do not \"\n      \"(CS26_66 unit 2 at 6.5%, CS54_126 units 6 and 7 at 9.0% and 3.8%, CS54_124 unit 2 at 3.0%, and H27_58 units 35 and 37 at \"\n      \"50%). This is at least 95%. The median fraction is 0.19%. As stored, 1860 units fall below 3%; the spike times of 13 \"\n      \"units are not in time order.\"),\n    o(\"fig5a-mtl-locations\", \"reproduced\",\n      \"All 1864 units are on electrodes located in the amygdala or hippocampus (right amygdala 594, left amygdala 498, right \"\n      \"hippocampus 407, left hippocampus 365).\"),\n    o(\"fig5c-auc-all\", \"reproduced\",\n      \"Mean AUC over 87 sessions 0.753, standard deviation 0.094 (range 0.445 to 0.919). The confidence response (response_value \"\n      \"minus 30) equals the TTL 31 to 36 codes in every file. With label 0 taken as old, as the paper's text states, the mean \"\n      \"AUC would be 0.247. Leaving out the second file of each fully duplicated pair gives 0.752 and 0.094.\",\n      [0.753, 0.094]),\n    o(\"fig5c-auc-sites\", \"reproduced\",\n      \"CS (78 sessions) 0.760 with SD 0.085; TWH (9 sessions) 0.688 with SD 0.138. All four values are within tolerance. \"\n      \"Welch's t-test between sites t = 1.53, p = 0.161, difference 0.072.\",\n      [0.760, 0.688, 0.085, 0.138]),\n    o(\"fig5b-roc-asymmetric\", \"reproduced\",\n      \"Mean z-ROC slope over 82 sessions 0.782 (SD 0.300, median 0.791), below 1 in 65 of 82; one-sample t-test against 1 \"\n      \"t = -6.58, p = 4.3e-09. Wilcoxon signed-rank p = 2e-08; the pooled ROC has slope 0.816. By site, CS 0.773 (74 sessions, \"\n      \"p = 1.6e-08) and TWH 0.861 (8 sessions, p = 0.14).\",\n      deviations=[\"Five sessions (CS24_60, CS39_93, H48_99, CS51_119, T100_2008) whose five interior false alarm rates are all \"\n                  \"equal have no regression slope and were left out; the claims file does not say how such sessions are \"\n                  \"treated. This is a standard choice that cannot change the outcome at p = 4e-09.\"]),\n    o(\"fig5d-confidence-accuracy\", \"reproduced\",\n      \"Reading (a), the fixed split, 84 sessions (3 left out for an empty group; CS39_93, H48_99, T100_2008): high 80.1% \"\n      \"against low 60.9%, high above low in 73, paired t = 10.16, p = 3.2e-16. Reading (b), the Python dynamic split, 82 \"\n      \"sessions: 78.2% against 60.8%, p = 1.3e-11. The unpaired Welch tests (p = 4.4e-17 and 8.3e-14), the code's inclusion \"\n      \"rule (73 sessions, p = 1.3e-20 and 2.4e-13) and the MATLAB dynamic split (p = 1.2e-13) also give p below 0.001. By site \"\n      \"under (a), CS 81.1% against 61.0% (p = 7e-16) and TWH 70.7% against 60.3% (8 sessions, p = 0.14).\"),\n    o(\"vs-cells-proportion\", \"reproduced\",\n      \"In the Methods' window 332 of 1864 units (17.81%) are VS cells. The code's window gives 343 (18.40%), the duplicated \"\n      \"trains counted once 321 of 1798 (17.85%), and the null with categories shuffled within session 90 (4.83%). At p < 0.01 \"\n      \"160 units, at p < 0.1 478. Six units with the same rate in every trial have no ANOVA and are counted as not VS. Five of \"\n      \"59 subjects have no VS cell.\",\n      [332, 17.81],\n      [\"The denominator is the 1864 unit rows of the files, where the paper has 1863.\"]),\n    o(\"ms-cells-proportion\", \"not_reproduced\",\n      \"Under the criterion's method (Methods' window, all 50 and 50 trials, bootstrap of bootstrapMeanEqualTest.m) 110 of 1864 \"\n      \"units (5.90%) are MS cells, below the tolerance of 146 +/- 14.6; four other seeds give 109 to 111, and p <= 0.05 gives \"\n      \"111. The null with labels shuffled within session gives 81 (4.35%). The variants differ: all trials in the code's window \"\n      \"108; correct trials only in the Methods' window 132 (137 to 147 over four other seeds); the code's choices, correct trials \"\n      \"in 200 to 1700 ms, 147 (7.89%; 143 to 147 over other seeds), which matches the paper. The paper's count is reached with \"\n      \"the code's trial selection and not with the Methods' 50 and 50 trials.\",\n      [110, 5.90],\n      [\"The denominator is the 1864 unit rows of the files, where the paper has 1863.\",\n       \"The bootstrap seed is a standard choice; the spread over five seeds is shown (109 to 111 for the main reading).\"]),\n    o(\"dual-cells-proportion\", \"not_reproduced\",\n      \"12 units (0.64%) are selected by both main tests, against 26 +/- 2.6 (1.4%); 19.6 would be expected if the two \"\n      \"selections were independent. With the code's choices for both tests 26 units (1.39%) qualify, and with MS on correct \"\n      \"trials in the Methods' window 24 (1.29%). The shuffled nulls give 6.\",\n      [12, 0.64]),\n    o(\"fig5f-site-proportions\", \"partially_reproduced\",\n      \"Under the main tests, no two-sided Fisher's exact test finds a difference between sites (VS p = 0.36, MS p = 0.46, dual \"\n      \"p = 1.0), but only 1 of 6 values is within tolerance; CS has 17.63% VS, 5.82% MS and 0.67% dual cells (1787 units), TWH \"\n      \"22.08%, 7.79% and 0% (77 units). With the code's choices all 6 values are within tolerance (CS 18.35%, 7.78%, 1.40%; TWH \"\n      \"19.48%, 10.39%, 1.30%), equal to the figure's values to the second decimal, and no Fisher test finds a difference \"\n      \"(p = 0.77, 0.39, 1.0). TWH has 77 units, so one cell moves its percentages by 1.3 points.\",\n      [17.63, 5.82, 0.67, 22.08, 7.79, 0.0]),\n    o(\"twh-sessions\", \"reproduced\",\n      \"Nine sessions (from eight subjects, T88 with two) have subject labels starting with T; their files name Toronto Western \"\n      \"Hospital as the institution.\",\n      9),\n    o(\"previous-release-link\", \"partially_reproduced\",\n      \"Of the 65 sessions of Table 1 of Faraut et al. (2018), 64 are found by session id with the same subject label and task \"\n      \"variant (98.5%). Session 98 of H48 (variant 2) is not in the dandiset, nor in this paper's Online-only Table 1. Among the \"\n      \"matched sessions, ages differ for C24 (47 against 57 in the files, sessions 59 and 60), H33 (29 against 30) and H48 \"\n      \"session 99 (54 against 32), and H48's sex differs (M against F in the file).\",\n      deviations=[\"The task variant of a file is read from the image folder in external_image_file (newolddelay, \"\n                  \"newolddelay2, newolddelay3), the folder names Table 2 of Faraut et al. gives for the three variants.\"]),\n    o(\"previous-release-additions\", \"partially_reproduced\",\n      \"Relative to Faraut et al.'s Table 1 the dandiset adds 23 sessions and 17 subjects, as stated, but the new sessions hold \"\n      \"325 unit rows (CS 248, TWH 77), above 288 +/- 28.8. The sessions shared with the earlier release hold 1539 unit rows, \"\n      \"where its abstract states 1576 neurons. The differences of the stated totals are 22 sessions, 17 subjects and 287 \"\n      \"neurons; of the counts here 22, 17 and 288.\",\n      [23, 17, 325]),\n    o(\"fig4-example-vs-neuron\", \"reproduced\",\n      \"Session 132 is CS58_132. One unit is on channel 177, at electrode row 4 (origClusterID 551, 722 spikes), in the right \"\n      \"amygdala. One-way ANOVA across the 5 categories p = 1.2e-22 in the Methods' window (7.9e-19 in the code's); mean rate \"\n      \"6.75 Hz for animals against 0.25 to 0.85 Hz for cars, food, people and spatial.\"),\n    o(\"fig3-example-vs-neuron\", \"blocked\",\n      \"Session 144 is not in the dandiset (its highest session id below 2000 is 136), nor in Online-only Table 1 or in Table 1 \"\n      \"of Faraut et al. (2018), so the neuron cannot be found.\",\n      blocked_by=\"data_missing\"),\n]\n\nfindings = [\n    dict(kind=\"metadata_error\", statement=(\n        \"new_old_labels_recog is described in the files, and in the paper, as 0 for old and 1 for new stimuli, but the data use \"\n        \"the reverse. In all 87 sessions the label 1 recognition trials show images from the session's encoding block and the \"\n        \"label 0 trials never do, and in 86 of 87 sessions label 1 trials receive more old responses. The paper's analysis code \"\n        \"treats 1 as old; a user following the description would obtain a mean behavioural AUC of 0.25 in place of 0.75.\")),\n    dict(kind=\"data_missing\", statement=(\n        \"The impedance column (imp) of the electrodes table is NaN for all 887 electrodes in all 87 files, although the paper \"\n        \"lists impedance among the electrode information. The MNI coordinates (x, y, z) are missing for 99 electrodes in 8 \"\n        \"files.\")),\n    dict(kind=\"data_missing\", statement=(\n        \"Eight sessions hold fewer than the 100 encoding trials the paper describes. The trial tables of H14_18, H15_20, H15_21, \"\n        \"H16_23, H18_26, H19_27 and H23_44 hold 50 encoding trials (150 trials, and 150 stimulus images), and only about half of \"\n        \"their old recognition images are among them; CS53_123 holds 97, and its event stream starts in the middle of a \"\n        \"trial.\")),\n    dict(kind=\"other\", about=\"data\", statement=(\n        \"Recordings are deposited more than once. Sessions 54 and 55 (H42) hold the same 32 spike trains and the same trial \"\n        \"onsets; sessions 43 and 44 (H23) hold the same 23 spike trains with different trial tables and task variants; sessions \"\n        \"38 and 39 (H21) share 11 of their 20 and 18 units, with different trials. 66 unit rows repeat another file's spike \"\n        \"train; counted once, the dataset holds 1798 distinct spike trains.\")),\n    dict(kind=\"format_error\", statement=(\n        \"The spike times of 13 units are not stored in increasing order (H15_21 unit 9, H27_58 units 35 to 38, CS29_70 units 18, \"\n        \"25 and 27, CS31_73 unit 3, CS33_77 units 3 and 21, H44_68 unit 9, CS56_128 unit 2).\")),\n    dict(kind=\"metadata_error\", statement=(\n        \"The unit quality metrics are incomplete or implausible. IsolationDist (the paper's IsolDist) is NaN for 493 of 1864 \"\n        \"units and SNR for 75, SNR is infinite for 11 units, and two isolation distances exceed 1e6 (up to 8.1e32). Two units \"\n        \"of H27_58 have half of their interspike intervals below 3 ms, and 6 units in all break the paper's 3% refractory \"\n        \"criterion.\")),\n    dict(kind=\"metadata_error\", statement=(\n        \"The event streams of 9 files hold TTL codes that Table 1 and the events description do not define (0, 4, 22, 23, 98, \"\n        \"99), and in T88_2001, T88_2002 and T90_2003 some trials have a second question-screen code (3) before the stimulus \"\n        \"offset (2). Seven files have no start-of-experiment marker (55) and T88_2001 has three end markers (66).\")),\n    dict(kind=\"metadata_error\", statement=(\n        \"Four files use experiment ids outside Table 2 of the paper (CS33_77 81 and 82; CS39_100 and H51_105 82 and 83; H42_55 \"\n        \"80 and 82), so an id of 81, 82 or 83 can mark either block. The ids do not follow the task variant as the paper's \"\n        \"Table 2 pairs suggest (most variant 3 sessions use 80 and 81).\")),\n    dict(kind=\"metadata_error\", statement=(\n        \"Two session dates break the paper's rule of the first of the month and the recording span. H28_48 is dated \"\n        \"2010-03-13, and H44_68 is dated 2000-01-01, six years before any other session.\")),\n    dict(kind=\"metadata_error\", statement=(\n        \"Subject metadata disagree with the paper's Online-only Table 1 and with Faraut et al. (2018). H48 is a 32-year-old \"\n        \"female in the file and a 54-year-old male in both papers (32 F is C48's entry), C24 is 57 against 47, and H33 is 30 \"\n        \"against 29.\")),\n    dict(kind=\"data_missing\", statement=(\n        \"Session 98 of subject H48, listed in the earlier release (Faraut et al. 2018, Table 1), is not in the dandiset, and \"\n        \"session 144, whose neuron 144-140-3-RH is the example of Figure 3, is not in the dandiset either.\")),\n    dict(kind=\"other\", about=\"data\", statement=(\n        \"The 23 sessions added since the earlier release hold 325 unit rows, where the paper states 288 added neurons, and the \"\n        \"64 sessions shared with that release hold 1539, where it stated 1576. The files hold 1864 unit rows against the \"\n        \"paper's 1863.\")),\n    dict(kind=\"code_mismatch\", statement=(\n        \"The paper's Methods select MS cells by comparing all 50 novel and 50 familiar trials in a 1 s window from 200 ms after \"\n        \"onset, and VS cells in the same window; the paper's code (single_neuron.py and NWB_singleCellAnalysis_release.m at \"\n        \"commit 1d95162) uses 200 to 1700 ms and, for MS cells, correctly answered trials only. On the dandiset the code's \"\n        \"choices give the paper's numbers (343 VS, 147 MS, 26 dual cells, and every percentage of Figure 5f), while the Methods' \"\n        \"give 332 VS, 110 MS and 12 dual cells.\")),\n    dict(kind=\"paper_inconsistency\", statement=(\n        \"The Methods state that patients were recorded across 89 sessions, while Online-only Table 1 lists 87, as the dandiset \"\n        \"holds.\")),\n]\n\nrec = {\n    \"schema_version\": 3,\n    \"id\": \"chandravadia-2020-02\",\n    \"datasets\": [{\"archive\": \"dandi\", \"id\": \"000004\", \"version\": \"0.220126.1852\",\n                  \"doi\": \"10.48324/dandi.000004/0.220126.1852\", \"relation\": \"primary\"}],\n    \"paper\": \"doi:10.1038/s41597-020-0415-9\",\n    \"date\": \"2026-11-14\",\n    \"entry\": \"chandravadia-2020\",\n    \"provenance\": {\"kind\": \"agent\", \"accountable\": {\"name\": \"CatalystNeuro\"},\n                   \"agent\": {\"harness\": \"Claude Code\", \"model\": \"claude-opus-5-5\", \"protocol\": \"pilot-15\"},\n                   \"runner\": {\"platform\": \"GitHub Actions\",\n                              \"url\": \"https://github.com/catalystneuro/encore/actions/runs/43597317395\"}},\n    \"inputs\": [\n        {\"what\": \"Online-only Table 1 of the paper (subjects, session ids, variants, age, sex, diagnosis), read from the Europe \"\n                 \"PMC full text PMC7055261, as the reference for counts-sessions and table1-demographics.\",\n         \"source\": \"doi:10.1038/s41597-020-0415-9\"},\n        {\"what\": \"Table 1 of Faraut et al. (2018), the session list of the earlier release, read from the Europe PMC full text \"\n                 \"PMC5810422, for previous-release-link and previous-release-additions.\",\n         \"source\": \"doi:10.1038/sdata.2018.10\"},\n        {\"what\": \"The paper's analysis code, read for method details the claims file cites (adjustHF, cal_auc, calcZROCSlope, \"\n                 \"dynamic_split, NO_behavior_evaluateSessionStatus, bootstrapMeanEqualTest, the code's window and trial \"\n                 \"selection); no data or numbers are taken from it.\",\n         \"source\": \"https://github.com/rutishauserlab/recogmem-release-NWB at commit 1d95162d2672e71dd234a31e4b8d70017a289ee3\"},\n    ],\n    \"outcomes\": outcomes,\n    \"findings\": findings,\n}\n\nwith open(\"attempts/chandravadia-2020-02.yaml\", \"w\") as f:\n    yaml.safe_dump(rec, f, sort_keys=False, width=110, allow_unicode=True)\nprint(\"ok\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/make_attempt.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . tools/bin/activate && python make_attempt.py && grep -c "claim:" attempts/chandravadia-2020-02.yaml
```

```
ok
50
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "entries/chandravadia-2020/README.md",
 "content": "# Chandravadia et al. (2020) from dandiset 000004\n\nTests the claims of [Chandravadia et al. (2020)](https://doi.org/10.1038/s41597-020-0415-9), a data\ndescriptor of 1863 single neurons recorded in the human amygdala and hippocampus during a new/old\nrecognition memory task, on [DANDI:000004](https://dandiarchive.org/dandiset/000004/0.220126.1852)\nversion 0.220126.1852. The claims cover the file contents the paper describes (sessions, subjects,\ntrials, event codes, units and electrode tables), the behavioural ROC analyses of Figure 5, and the\nproportions of visually and memory selective cells.\n\n| Claim | Outcome |\n|---|---|\n| 1863 neurons from 59 subjects | Reproduced (1864 unit rows) |\n| 87 sessions of Online-only Table 1 | Reproduced |\n| Age and sex of every subject | Partially reproduced (3 subjects differ) |\n| 100 encoding and 100 recognition trials per session, 5 categories | Partially reproduced (8 sessions lack encoding trials) |\n| new_old_labels_recog is 0 for old, 1 for new | Not reproduced (the coding is reversed) |\n| TTL codes of Table 1 | Partially reproduced |\n| Experiment ids of Table 2 | Partially reproduced |\n| Session dates on the first of the month | Partially reproduced |\n| Units table columns and metrics | Partially reproduced (metrics missing or not finite) |\n| Electrodes table, including impedance | Not reproduced (impedance empty) |\n| Refractory criterion (< 3% of ISIs below 3 ms) | Partially reproduced (6 units fail) |\n| All units in amygdala or hippocampus | Reproduced |\n| Behavioural AUC 0.74 ± 0.10 | Reproduced |\n| AUC by site | Reproduced |\n| Asymmetric ROC | Reproduced |\n| Accuracy higher with high confidence | Reproduced |\n| 343 VS cells (18.4%) | Reproduced (332) |\n| 146 MS cells (7.8%) | Not reproduced (110; the code's trial selection gives 147) |\n| 26 dual cells (1.4%) | Not reproduced (12; the code's choices give 26) |\n| VS, MS and dual percentages by site | Partially reproduced |\n| 9 TWH sessions | Reproduced |\n| Link to the earlier release (Faraut et al. 2018) | Partially reproduced (64 of 65 sessions) |\n| 23 sessions, 17 subjects and 288 neurons added | Partially reproduced (325 neurons) |\n| Figure 4 example neuron | Reproduced |\n| Figure 3 example neuron | Blocked: session 144 is not in the dandiset |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe attempt record, with the reasons and the differences from the paper's method, is\n[`attempts/chandravadia-2020-02.yaml`](../../attempts/chandravadia-2020-02.yaml).\n\n- `reproduce_chandravadia_2020.ipynb`: the analysis. It streams the trials, events, electrodes and\n  units of all 87 files (not the stimulus images) and takes about 3 minutes.\n- `chandravadia.py`: reading the files, the paper's session tables from Europe PMC, the ROC, z-ROC\n  and accuracy measures of the paper's code, window firing rates, the ANOVA and the bootstrap test.\n  Other notebooks on this dataset can import it.\n"
}
```

```
File created successfully at: entries/chandravadia-2020/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
. $TMPDIR/tools/bin/activate && date -u && python tools/entry.py all entries/chandravadia-2020 2>&1 | tail -20; date -u
```

```
Sat Nov 14 13:24:20 UTC 2026
Installed kernelspec registry-chandravadia-2020 in executed/chandravadia-2020/.venv/share/jupyter/kernels/registry-chandravadia-2020
0 error(s)
pass  reproduce_chandravadia_2020.ipynb  (153 s)
Sat Nov 14 13:27:02 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'E'
import json
def outs(p):
    nb=json.load(open(p)); d={}
    for c in nb['cells']:
        if c['cell_type']!='code': continue
        t=''.join(''.join(o.get('text','')) for o in c.get('outputs',[]))
        d[len(d)]=t
    return d
a=outs('executed/chandravadia-2020/reproduce_chandravadia_2020.ipynb'); b=outs('/tmp/claude-1001/exec/reproduce_chandravadia_2020.ipynb')
import difflib
for k in a:
    if a[k]!=b.get(k):
        for l in difflib.unified_diff(b.get(k,'').splitlines(), a[k].splitlines(), lineterm='',n=0): print(l)
E
```

```
--- 
+++ 
@@ -4 +4,2 @@
-read 87 files in 89 s; peak memory 0.28 GB
+version 0.220126.1851, published the same day: 87 assets; same paths, sizes and asset ids as 0.220126.1852 : True
+read 87 files in 89 s; peak memory 0.30 GB
--- 
+++ 
@@ -1 +1 @@
-notebook ran in 2.2 min; peak memory 0.30 GB
+notebook ran in 2.4 min; peak memory 0.31 GB
```

**Agent calls Bash**

```bash
. $TMPDIR/tools/bin/activate && python tools/entry.py handover entries/chandravadia-2020 && ls executed/chandravadia-2020/handover/ && python tools/entry.py check entries/chandravadia-2020 | tail -2; ls entries/chandravadia-2020; date -u
```

```
wrote executed/chandravadia-2020/handover
chandravadia-2020.yaml
chandravadia.py
reproduce_chandravadia_2020.ipynb
0 error(s)
README.md
__pycache__
chandravadia.py
entry.yaml
reproduce_chandravadia_2020.ipynb
requirements.in
requirements.lock.txt
Sat Nov 14 13:27:30 UTC 2026
```

**Agent calls Bash**

```bash
sed -n 506,525p tools/entry.py
```

```
def file_hash(path: Path) -> str:
    import hashlib
    return hashlib.sha256(path.read_bytes()).hexdigest()


def entry_hash(entry_dir: Path) -> str:
    """A hash of everything a run of the entry's notebooks reads from the repository: every file of the entry (its
    notebooks, helpers, lock and entry.yaml, which names the Python and the dataset versions), the packages `run`
    adds, and RUN_VERSION. Two runs from the same hash execute the same code on the same data versions."""
    import hashlib
    h = hashlib.sha256(f"run {RUN_VERSION}; harness {' '.join(HARNESS)}; python {python_of(entry_dir)}\n".encode())
    for path in sorted(p for p in entry_dir.rglob("*") if p.is_file()):
        rel = path.relative_to(entry_dir)
        if any(part in ("__pycache__", ".ipynb_checkpoints", ".venv") or part.endswith(".pyc") for part in rel.parts):
            continue
        h.update(f"{rel.as_posix()}\0{file_hash(path)}\n".encode())
    return h.hexdigest()


def reusable(entry_dir: Path, output_dir: Path, max_minutes: float) -> dict | None:
```

**Agent calls Bash**

```bash
rm -rf entries/chandravadia-2020/__pycache__; python3 - <<'E'
import json
nb=json.load(open('executed/chandravadia-2020/reproduce_chandravadia_2020.ipynb'))
c=[c for c in nb['cells'] if c['cell_type']=='code'][3:6]
for x in c: print(''.join(''.join(o.get('text','')) for o in x.get('outputs',[]))[-2500:])
E
```

```
files whose TTL-1 count equals the trial count: 87 of 87
largest |TTL-1 time - start_time| over files where counts agree: 0.000 ms
Empty DataFrame
Columns: [identifier, ttl1, trials, max_abs_diff_ms]
Index: []

fraction of units category selective, by window start relative to onset (window 1 s):
-2.00    0.053
-1.75    0.044
-1.50    0.049
-1.25    0.042
-1.00    0.049
-0.75    0.054
-0.50    0.081
-0.25    0.116
 0.00    0.164
 0.25    0.185
 0.50    0.149
 0.75    0.130
 1.00    0.106
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'E'
import sys, pickle, numpy as np
sys.path.insert(0,'entries/chandravadia-2020')
import chandravadia as C
a,S=pickle.load(open('sessions.pkl','rb')); by={s['identifier']:s for s in S}
for x,y in [('H42_54','H42_55'),('H23_43','H23_44'),('H21_38','H21_39')]:
    for ph in ['learn','recog']:
        tx=by[x]['trials']; ty=by[y]['trials']
        a_=tx[tx.stim_phase==ph]; b_=ty[ty.stim_phase==ph]
        n=min(len(a_),len(b_))
        print(x,y,ph,len(a_),len(b_), 'onsets equal', np.allclose(a_.start_time.values[:n], b_.start_time.values[:n]), 'resp equal', np.array_equal(a_.response_value.values[:n], b_.response_value.values[:n]), 'files equal', np.array_equal(a_.external_image_file.values[:n], b_.external_image_file.values[:n]), a_.start_time.values[[0,-1]].round(1), b_.start_time.values[[0,-1]].round(1))
    sx=np.concatenate(by[x]['spikes']); print('  spikes span', sx.min().round(1), sx.max().round(1))
E
```

```
H42_54 H42_55 learn 100 100 onsets equal True resp equal True files equal True [1610.7 2059.8] [1610.7 2059.8]
H42_54 H42_55 recog 100 100 onsets equal False resp equal False files equal False [3125.1 3622. ] [4046.5 4519.7]
  spikes span 1610.0 4525.0
H23_43 H23_44 learn 100 50 onsets equal False resp equal False files equal False [3292.3 3647.1] [1495.1 1708.5]
H23_43 H23_44 recog 100 100 onsets equal False resp equal False files equal False [4033.6 4474.4] [2431.6 3030.2]
  spikes span 1494.4 4477.7
H21_38 H21_39 learn 100 100 onsets equal False resp equal False files equal False [4682.9 5077.5] [6985.3 7309.1]
H21_38 H21_39 recog 100 100 onsets equal False resp equal False files equal False [6330.4 6695.8] [7909.4 8303.8]
  spikes span 4682.2 8307.1
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'E'
p='build_nb.py'; s=open(p).read()
a='''    sa, sb = byid[a], byid[b]
    same_trials = len(sa["trials"]) == len(sb["trials"]) and np.allclose(sa["trials"].start_time, sb["trials"].start_time)
    same_resp = len(sa["trials"]) == len(sb["trials"]) and np.array_equal(sa["trials"].response_value, sb["trials"].response_value)
    print(f"{a} ({len(sa['units'])} units) and {b} ({len(sb['units'])} units): {n} identical spike trains;"
          f" same trial onsets {same_trials}, same responses {same_resp}, variants {sorted(C.variant_of(sa['trials'].external_image_file))}"
          f" and {sorted(C.variant_of(sb['trials'].external_image_file))}")'''
b='''    sa, sb = byid[a], byid[b]
    print(f"{a} ({len(sa['units'])} units) and {b} ({len(sb['units'])} units): {n} identical spike trains;"
          f" variants {sorted(C.variant_of(sa['trials'].external_image_file))} and {sorted(C.variant_of(sb['trials'].external_image_file))}")
    for ph in ("learn", "recog"):
        ta, tb = sa["trials"][sa["trials"].stim_phase == ph], sb["trials"][sb["trials"].stim_phase == ph]
        same = len(ta) == len(tb) and np.allclose(ta.start_time, tb.start_time) and np.array_equal(ta.external_image_file, tb.external_image_file)
        print(f"  {ph}: {a} {ta.start_time.min():.0f} to {ta.start_time.max():.0f} s, {b} {tb.start_time.min():.0f} to {tb.start_time.max():.0f} s;"
              f" identical trials (onsets and images): {same}")
    shared = np.concatenate([sp for sp in sa["spikes"] if hashlib.md5(np.asarray(sp).tobytes()).hexdigest() in
                             {hashlib.md5(np.asarray(x).tobytes()).hexdigest() for x in sb["spikes"]}])
    print(f"  the shared spike trains span {shared.min():.0f} to {shared.max():.0f} s")'''
assert a in s; s=s.replace(a,b)
a='''Every unit's spike train is hashed, and trains found in more than one file are listed by pair of files.
The trial tables and events of each pair are compared too.'''
b='''Every unit's spike train is hashed, and trains found in more than one file are listed by pair of files.
The trial tables of each pair are compared by phase, and the time span of the shared spike trains is given.'''
assert a in s; s=s.replace(a,b)
a='''dup_keys = {k for k, v in owners.items() if len(v) > 1}'''
assert a in s
s=s.replace(a, a)
# markdown after duplicates cell: add interpretation
a='''md("""
## Reference tables from the papers'''
b='''md("""
The three pairs are consecutive sessions of one subject on one clock: the shared spike trains span both
sessions' trials. In H42_54 and H42_55 the encoding block is the same and the recognition blocks differ; in
the other two pairs both blocks differ. So these are the same neurons recorded during two sessions, each
deposited with both. They are counted per file, as the paper counts neurons per session, and counted once
as a variant.
""")

md("""
## Reference tables from the papers'''
assert a in s; s=s.replace(a,b)
s=s.replace('''of 13 units are not in time order; sessions 43 and 44 and sessions 54 and 55 hold the same spike trains for
every unit, and sessions 38 and 39 share 11 of their units;''','''of 13 units are not in time order; sessions 43 and 44 and sessions 54 and 55 hold the same spike trains for
every unit, and sessions 38 and 39 share 11 of their units, each pair from one continuous recording of two
sessions;''')
open(p,'w').write(s)
p='make_attempt.py'; s=open(p).read()
a='''        "Recordings are deposited more than once. Sessions 54 and 55 (H42) hold the same 32 spike trains and the same trial "
        "onsets; sessions 43 and 44 (H23) hold the same 23 spike trains with different trial tables and task variants; sessions "
        "38 and 39 (H21) share 11 of their 20 and 18 units, with different trials. 66 unit rows repeat another file's spike "
        "train; counted once, the dataset holds 1798 distinct spike trains.")),'''
b='''        "Units are deposited in two files without saying so. Sessions 54 and 55 (H42) hold the same 32 spike trains, sessions "
        "43 and 44 (H23) the same 23, and sessions 38 and 39 (H21) share 11 of their 20 and 18 units. In each pair the shared "
        "spike trains span the trials of both sessions, so they are the same neurons recorded continuously through two "
        "consecutive sessions; sessions 54 and 55 also share their encoding block (identical trials) and differ in the "
        "recognition block. 66 unit rows repeat another file's spike train; counted once, the dataset holds 1798 distinct "
        "spike trains. Nothing in the files marks these units as the same.")),'''
assert a in s; s=s.replace(a,b); open(p,'w').write(s)
E
grep -n "duplicated" make_attempt.py | head
```

```
92:      "AUC would be 0.247. Leaving out the second file of each fully duplicated pair gives 0.752 and 0.094.",
112:      "In the Methods' window 332 of 1864 units (17.81%) are VS cells. The code's window gives 343 (18.40%), the duplicated "
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i 's/variant, the second file of each fully duplicated pair left out/variant, the two sessions whose every unit repeats another file left out/' build_nb.py && sed -i "s/Leaving out the second file of each fully duplicated pair gives 0.752 and 0.094./Leaving out the two sessions whose every unit repeats another file gives 0.752 and 0.094./" make_attempt.py && grep -c "two sessions whose every unit" build_nb.py make_attempt.py && . dev/bin/activate && python build_nb.py && . tools/bin/activate && python make_attempt.py && cd  && python tools/entry.py all entries/chandravadia-2020 2>&1 | tail -3 && python tools/entry.py handover entries/chandravadia-2020; rm -rf entries/chandravadia-2020/__pycache__; date -u
```

```
build_nb.py:1
make_attempt.py:1
wrote entries/chandravadia-2020/reproduce_chandravadia_2020.ipynb 94 cells
ok
Installed kernelspec registry-chandravadia-2020 in executed/chandravadia-2020/.venv/share/jupyter/kernels/registry-chandravadia-2020
0 error(s)
pass  reproduce_chandravadia_2020.ipynb  (169 s)
wrote executed/chandravadia-2020/handover
Sat Nov 14 13:31:28 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'E'
import json
nb=json.load(open('executed/chandravadia-2020/reproduce_chandravadia_2020.ipynb'))
cs=[c for c in nb['cells'] if c['cell_type']=='code']
print(''.join(''.join(o.get('text','')) for o in cs[5].get('outputs',[])))
errs=[o for c in cs for o in c.get('outputs',[]) if o.get('output_type')=='error' or o.get('name')=='stderr']
print('errors/stderr:', len(errs))
for c in cs:
    if 'claim:fig5c-auc-all' in c['metadata'].get('tags',[]): print(''.join(''.join(o.get('text','')) for o in c['outputs']))
E
```

```
Online-only Table 1: 87 sessions, 59 subjects; totals row: ['Total Subjects: 59', 'Total Sessions: 87', 'Total Female: 25', 'Total Male: 34']
Faraut et al. 2018 Table 1: 65 sessions, 42 subjects
  label  session  variant  n_sessions  age sex              diagnosis
0   H09        5        1           2   55   M  Right Mesial Temporal
1   H09        6        2           2   55   M  Right Mesial Temporal
2   H10        7        1           1   37   M           Left Frontal

errors/stderr: 0
files where response_value - 30 equals the TTL 31-36 codes of the events stream, in order: 87 of 87
AUC over 87 sessions: mean 0.753, SD 0.094 (expected 0.74 +/- 0.10 and 0.10 +/- 0.01); range 0.445 to 0.919
sessions with AUC below 0.5: ['T98_2005']
with the stated coding (0 = old) the mean AUC would be 0.247
variant, the two sessions whose every unit repeats another file left out (85 sessions): mean 0.752, SD 0.094
```

**Agent calls Bash**

```bash
python3 - <<'E'
import json
nb=json.load(open('executed/chandravadia-2020/reproduce_chandravadia_2020.ipynb'))
cs=[c for c in nb['cells'] if c['cell_type']=='code']
print(''.join(''.join(o.get('text','')) for o in cs[4].get('outputs',[])))
E
. $TMPDIR/tools/bin/activate; python tools/entry.py check entries/chandravadia-2020 | tail -1; ls entries/chandravadia-2020
```

```
H21_38 (20 units) and H21_39 (18 units): 11 identical spike trains; variants [2] and [1]
  learn: H21_38 4683 to 5077 s, H21_39 6985 to 7309 s; identical trials (onsets and images): False
  recog: H21_38 6330 to 6696 s, H21_39 7909 to 8304 s; identical trials (onsets and images): False
  the shared spike trains span 4682 to 8307 s
H23_43 (23 units) and H23_44 (23 units): 23 identical spike trains; variants [3] and [2]
  learn: H23_43 3292 to 3647 s, H23_44 1495 to 1709 s; identical trials (onsets and images): False
  recog: H23_43 4034 to 4474 s, H23_44 2432 to 3030 s; identical trials (onsets and images): False
  the shared spike trains span 1494 to 4478 s
H42_54 (32 units) and H42_55 (32 units): 32 identical spike trains; variants [1] and [1]
  learn: H42_54 1611 to 2060 s, H42_55 1611 to 2060 s; identical trials (onsets and images): True
  recog: H42_54 3125 to 3622 s, H42_55 4047 to 4520 s; identical trials (onsets and images): False
  the shared spike trains span 1610 to 4525 s
unit rows: 1864  distinct spike trains: 1798  rows that repeat another file's train: 66

0 error(s)
README.md
chandravadia.py
entry.yaml
reproduce_chandravadia_2020.ipynb
requirements.in
[... 1 more lines not kept]
```

**Agent**

I've finished the attempt, run the handover, and the entry passes its checks: `python tools/entry.py all` gave 0 errors and a clean-environment run of 169 s. Nothing is committed. The record is `attempts/chandravadia-2020-02.yaml` and the entry is in `entries/chandravadia-2020/`.

**(1) Outcomes**

| Claim | Outcome | Key number |
|---|---|---|
| counts-neurons-subjects | reproduced | 1864 unit rows, 59 subjects |
| counts-sessions | reproduced | same 87 (subject, session) pairs as Online-only Table 1 |
| table1-demographics | partially reproduced | 56 of 59 subjects match; C24, H33 and H48 differ |
| task-structure | partially reproduced | 8 sessions have 50 or 97 encoding trials |
| new-old-label-coding | not reproduced | label 1 is old in all 87 sessions |
| ttl-codes | partially reproduced | 78 of 87 files pass |
| experiment-ids | partially reproduced | 83 of 87 files pass |
| session-dates | partially reproduced | H28_48 dated the 13th; H44_68 dated 2000 |
| units-table | partially reproduced | IsolationDist NaN for 493 units, SNR NaN for 75 and infinite for 11 |
| electrodes-table | not reproduced | impedance empty for all 887 electrodes |
| isi-criterion | partially reproduced | 6 units at or above 3% |
| fig5a-mtl-locations | reproduced | all units in amygdala or hippocampus |
| fig5c-auc-all | reproduced | 0.753 ± 0.094 |
| fig5c-auc-sites | reproduced | CS 0.760 ± 0.085, TWH 0.688 ± 0.138 |
| fig5b-roc-asymmetric | reproduced | mean slope 0.782, p = 4e-9 |
| fig5d-confidence-accuracy | reproduced | p < 0.001 under both splits |
| vs-cells-proportion | reproduced | 332 cells (17.8%) |
| ms-cells-proportion | not reproduced | 110 cells (5.9%); the code's choices give 147 |
| dual-cells-proportion | not reproduced | 12 cells; the code's choices give 26 |
| fig5f-site-proportions | partially reproduced | no site difference, but only 1 of 6 values in tolerance |
| twh-sessions | reproduced | 9 |
| previous-release-link | partially reproduced | 64 of 65 earlier sessions found |
| previous-release-additions | partially reproduced | 23 sessions, 17 subjects, but 325 neurons |
| fig4-example-vs-neuron | reproduced | p = 1e-22, animals highest |
| fig3-example-vs-neuron | blocked (data_missing) | session 144 is not in the dandiset |

**(2) What the dataset showed**
- **Label coding is reversed:** label 1 marks old images, against the paper and the column description. Read as described, the mean AUC would be 0.25.
- **Missing values:** impedance is empty everywhere, and coordinates are missing for 99 electrodes.
- **Short sessions:** 8 sessions lack encoding trials, and CS53_123 starts mid-trial.
- **Event codes and ids:** 9 files hold codes not in Table 1, and 4 files use experiment ids not in Table 2.
- **Unsorted spikes:** the spike times of 13 units are not in time order.
- **Shared units:** three pairs of sessions (43/44, 54/55, 38/39) share 66 spike trains. Each pair is one continuous recording through two consecutive sessions, so these are the same neurons, and nothing in the files says so.
- **Subject metadata:** H48 is 32 and female in the file but 54 and male in both papers.
- **Missing sessions:** session 98 of the earlier release and session 144 (the Figure 3 neuron) are absent.
- **Methods versus code:** the paper's code (200 to 1700 ms window, correct trials only for MS cells) gives exactly the paper's counts, including every value of Figure 5f. The Methods' 1 s window and all 50 and 50 trials do not. I recorded this as a code_mismatch finding.
- I made no assumptions (no outcome is marked `assumed`), added no questions for the authors, and asked the reader nothing.

**(3) Where the protocol or claims file was unclear**
1. **Possible break in blindness:** the claims file's opening comment describes an earlier author's data checks: the duplicated sessions 43/44 and 54/55, label 1 receiving most "old" responses, three subjects whose age or sex differ, and 1864 units. I read it because it is part of the claims file I was told to use. I found no other trace of the earlier attempts.
2. **Reading the files:** docs/archives.md says to read NWB files with pynwb. I read them with h5py over remfile, which is faster and gives the same data, and I never read the images.
3. **The paper's own tables:** the protocol does not say how to use the paper's tables as reference values. I fetched Online-only Table 1 (and Faraut et al.'s Table 1) from Europe PMC in the notebook and listed both under `inputs`.
4. **Clock check:** a per-session check cannot establish alignment in sessions with few units. I named the 15 such sessions in the notebook.
5. **ttl-codes:** the criterion does not say how to cut trials out of the event stream. I cut at each stimulus onset and recorded that as a deviation.
6. **Duplicate rule versus counting:** the protocol says to count each recording once. The claims file instead counts units per file and treats counting once as a variant. I followed the claims file.

**(4) Runtime and failures**
- The notebook runs in about 2.5 to 3 minutes (169 s in the clean environment), peak memory 0.31 GB. The whole session took about 35 minutes of the 5 hours.
- Nothing failed. One permission-gated `sed` command was denied, and I read the same file another way.

## End of run

71 turns, 28 minutes, $7.12 at API prices, result: success.
