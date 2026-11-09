# 000945 · author · run 41243437657

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls claims/000945 paper entries attempts | head -50
```

```
<persisted-output>
Output too large (36.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/de22c3be-727e-412f-8496-f1c533ac48f3/tool-results/bced66azc.txt

Preview (first 2KB):
Sat Oct 31 21:28:09 UTC 2026
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
 "file_path": "docs/protocol.md"
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-13`. Record this version in the attempt's provenance.
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
ls; ls claims/000945 paper entries/001453-fouke-2025 claims/001453; ls attempts | tail -5
```

```
LICENSE
LICENSE-data
README.md
attempts
bunfig.toml
claims
docs
encore_science
entries
node_modules
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
pyproject.toml
questions
queue
schemas
scripts
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/000945/*.yaml; wc -c paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/000945/10.1088-1741-2552-adbb1f.yaml"
}
```

```
1	# Claims for Ramachandran, Gao, Yttri, Yu & He (2025) on dandiset 000945.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22,
3	# protocol as stated in docs/protocol.md.
4	# Source: the version of record (J Neural Eng 22(2) 026022, PMC11920894), full text as served by
5	# Europe PMC: Abstract, Introduction, Methods, Results, figure legends and Discussion. No PDF was
6	# supplied. The supplementary materials (headpiece design, surgery, training, hydrophone scanning,
7	# supplementary figures 2 and 4, supplementary table 1 of ISPTA values) were not supplied. No
8	# claim rests on them: the analysis methods and the ISPTA of each PRF condition are given in the
9	# main text (Methods 2.3 to 2.6). The paper links no analysis code (it names "custom code" in
10	# MATLAB R2019a with FieldTrip), so no code was read.
11	#
12	# Data the paper used, as it reports them. Adult male Wistar rats, awake and head-fixed, with a
13	# chronic 32-channel micro-electrode array in S1; tFUS from a 128-element array (f0 1.5 MHz,
14	# 114 kPa peak-to-peak in situ at 15 V), ultrasound duration 67 ms, one trial every 2.5 s with
15	# 10% jitter, 505 trials per parameter set, the first 5 cut (500 used). TDT recordings at 24 kHz,
16	# bandpass 300 Hz to 5 kHz, units sorted in Offline Sorter. Batch 1 (10 rats): awake PRF series
17	# at 30, 300, 1500, 3000 and 4500 Hz with 200 us tone-burst duration (TBD), at about 7 months;
18	# the same PRF series under isoflurane at 9 months; awake DC series at 1500 Hz with TBD 40, 200
19	# and 400 us (DC 6, 30 and 60%) at 10 months. Batch 2 (5 rats, 7 months): awake and anesthetized
20	# recordings at a low PRF and 1500 Hz with 200 us TBD, and a sham at 1500 Hz aimed off target at
[... 499 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l paper/10.1088-1741-2552-adbb1f.txt; sed -n 1,200p paper/10.1088-1741-2552-adbb1f.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "Methods|2\.[3-6]|Results|3\.[1-3]|Figure [3-7]" 10.1088-1741-2552-adbb1f.txt | cut -c1-150 | head -60
```

```
7:pmc J Neural Eng J Neural Eng jne JNEOBH Journal of Neural Engineering 1741-2560 1741-2552 IOP Publishing 11920894 40014879 jneadbb1f 10.1088/1741-2
17:${\text{PII}} = {\mathop \smallint \nolimits }{}\frac{{{p^2}\left( t \right)}}{{{Z_0}}}{\text{d}}t{ }$\end{document} PII = ∫ p 2 ( t ) Z 0 d t and 
26:Objective. Transcranial focused ultrasound (tFUS) is a promising neuromodulation technique able to target shallow and deep brain structures with hi
34:10.1109/TBME.2013.2244890
48:10.1109/TBME.2022.3221887
80:10.1152/JN.00923.2014
106:10.1016/J.BRS.2023.11.014
126:10.48324/dandi.000945/0.250213.2212
134:10.1111/J.1469-7793.1997.593BA.X
```

**Agent calls Bash**

```bash
cd  sed -n 7,25p paper/10.1088-1741-2552-adbb1f.txt | fold -w 4000 | grep -v '^\$' | cut -c1-40000 | head -c 70000 | sed 's/\\documentclass[^$]*\$//g' > $TMPDIR/paper.txt; wc -c $TMPDIR/paper.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
import re
t=open('paper/10.1088-1741-2552-adbb1f.txt').read()
t=re.sub(r'\\\\documentclass.*?\\\\end\{document\}','',t,flags=re.S)
i=t.find('Methods'); 
open('$TMPDIR/p.txt','w').write(t)
print(len(t))
"; fold -s -w 200 $TMPDIR/p.txt > $TMPDIR/pf.txt; wc -l $TMPDIR/pf.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pf.txt",
 "offset": 1,
 "limit": 250
}
```

```
1	DOI: 10.1088/1741-2552/adbb1f
2	Version: as served by europe_pmc
3	Source: europe_pmc+crossref (paper-text-fetcher)
4	Stored: 2026-10-20
5	Extracted: as fetched
6	------------------------------------------------------------------------
7	pmc J Neural Eng J Neural Eng jne JNEOBH Journal of Neural Engineering 1741-2560 1741-2552 IOP Publishing 11920894 40014879 jneadbb1f 10.1088/1741-2552/adbb1f adbb1f JNE-108412.R2 Paper 
8	Parameter-dependent cell-type specific effects of transcranial focused ultrasound stimulation in an awake head-fixed rodent model Ramachandran Sandhya 1 https://orcid.org/0000-0003-0860-2033 Gao Huan 
9	1 Yttri Eric 2 3 https://orcid.org/0000-0002-4778-4389 Yu Kai 1 https://orcid.org/0000-0003-2944-8602 He Bin 1 2 * [removed: an e-mail address] 1 Department of Biomedical Engineering, Carnegie Mellon 
10	University , Pittsburgh, PA, United States of America 2 Neuroscience Institute, Carnegie Mellon University , Pittsburgh, PA, United States of America 3 Department of Biological Sciences, Carnegie 
11	Mellon University , Pittsburgh, PA, United States of America * Author to whom any correspondence should be addressed. 01 4 2025 19 3 2025 22 2 026022 06 12 2024 13 2 2025 27 2 2025 22 1 2025 19 3 
12	2025 © 2025 The Author(s). Published by IOP Publishing Ltd 2025 https://creativecommons.org/licenses/by/4.0/ Original content from this work may be used under the terms of the Creative Commons 
13	Attribution 4.0 license . Any further distribution of this work must maintain attribution to the author(s) and the title of the work, journal citation and DOI. Abstract Objective. Transcranial 
14	focused ultrasound (tFUS) is a promising neuromodulation technique able to target shallow and deep brain structures with high precision. Previous studies have demonstrated that tFUS stimulation 
15	responses are cell-type specific, and specifically tFUS can elicit time-locked neural activity in regular spiking units (RSUs) that is sensitive to increases in pulse repetition fre
[... 235 more lines not kept]
```

**Agent**

Paper read; it cites DANDI version 0.250213.2212. Now the repo docs and the example entry.

**Agent calls Bash**

```bash
cd  wc -l README.md docs/design.md docs/archives.md; sed -n '/## DANDI/,/^## [A-Z]/p' docs/archives.md | head -120
```

```
139 README.md
  271 docs/design.md
  287 docs/archives.md
  697 total
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
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md | head -120
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
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat docs/design.md
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
[... 251 more lines not kept]
```

**Agent**

Now the example entry's formats.

**Agent calls Bash**

```bash
cd entries/001453-fouke-2025; cat entry.yaml requirements.in README.md; head -80 omr.py; python3 -c "
import json;nb=json.load(open('reproduce_fouke_2025.ipynb'))
for c in nb['cells'][:6]: print(c['cell_type'], c.get('metadata'), ''.join(c['source'])[:1500]); print('-----')
print(len(nb['cells']))
for c in nb['cells']: print(c['metadata'].get('tags'), ''.join(c['source'])[:80].replace('\n',' | '))
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
[... 284 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/001453-fouke-2025-01.yaml | head -150; ls schemas; ls questions | head
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
[... 144 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 150,400p attempts/001453-fouke-2025-01.yaml | grep -n -A40 "^findings" | head -60; ls questions/000945* 2>/dev/null; python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s)[:6000])"
```

```
94:findings:
95-- kind: data_missing
96-  statement: The dandiset holds only the freely swimming tracking of Figure 1 and Figure S1. The
97-    two-photon imaging and the head-fixed tail tracking behind Figures 2 to 4 are not in it, and
98-    the GitLab repository the paper names for all behavioural and imaging data holds analysis
99-    notebooks only. Nine of the paper's main findings cannot be tested.
100-- kind: metadata_insufficient
101-  statement: The stimulus codes 0 to 20 have no names or description in the files or the
102-    dandiset metadata. They can be named only from the paper's analysis notebook and the protocol
103-    file of its stimulus software.
104-- kind: code_mismatch
105-  statement: The paper's analysis notebook labels code 9 as lateral right and 11 as lateral left,
106-    while its conversion of the stimulus software's names gives the reverse (it carries a remap
107-    that swaps them). The data do not settle which is right; zebrafish barely turn to either, and
108-    Danionella turn more to the right for code 11, which fits the stimulus software's assignment
109-    only if the fish turn with lateral motion.
110-- kind: metadata_error
111-  statement: Subject ids 0 to 11 are each used for one zebrafish and one Danionella cerebrum, so
112-    subject_id does not identify an animal. The archive's summary counts 25 subjects and lists
113-    only Danio rerio; the files hold 37 fish of two species.
[... 22 more lines not kept]
```

**Agent**

Now the dataset itself.

**Agent calls Bash**

```bash
date -u; cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/000945/ | python3 -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/000945/versions/" | python3 -m json.tool | grep -E '"version"|"modified"|"status"|asset_count|size'
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; for v in 0.250213.2212 0.250829.1250; do curl -s "https://api.dandiarchive.org/api/dandisets/000945/versions/$v/assets/?page_size=200" > assets_$v.json; done; python3 -c "
import json
a=json.load(open('assets_0.250213.2212.json'))['results']; b=json.load(open('assets_0.250829.1250.json'))['results']
print(len(a),len(b))
A={x['path']:(x['blob'] if 'blob' in x else x.get('asset_id'),x['size']) for x in a}
B={x['path']:(x['blob'] if 'blob' in x else x.get('asset_id'),x['size']) for x in b}
print(a[0].keys())
for p in sorted(A): print(p, A[p][1], 'same' if A[p]==B.get(p) else ('size-same' if B.get(p) and B[p][1]==A[p][1] else 'DIFF'))
"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q env && . env/bin/activate && uv pip install -q pynwb remfile h5py dandi numpy scipy pandas statsmodels matplotlib scikit-learn 2>&1 | tail -3; python -c "import pynwb, remfile; print(pynwb.__version__)"
```

```
4.2.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > open1.py <<'EOF'
import json, h5py, remfile, pynwb, sys
a=json.load(open('assets_0.250213.2212.json'))['results']
path=sys.argv[1]
x=[r for r in a if r['path']==path][0]
url=f"https://api.dandiarchive.org/api/assets/{x['asset_id']}/download/"
f=h5py.File(remfile.File(url),'r')
def walk(g,pre=''):
    for k,v in g.items():
        if isinstance(v,h5py.Dataset): print(pre+k, v.shape, v.dtype, dict((kk,str(vv)[:80]) for kk,vv in v.attrs.items() if kk not in ('object_id','namespace')))
        else:
            print(pre+k+'/', dict((kk,str(vv)[:100]) for kk,vv in v.attrs.items() if kk not in ('object_id',)))
            walk(v,pre+'  ')
walk(f)
io=pynwb.NWBHDF5IO(file=f,load_namespaces=True); nwb=io.read()
print(nwb)
print('desc',nwb.session_description); print('exp',nwb.experiment_description); print(nwb.subject)
for k in ['identifier','session_start_time','institution','lab','notes','protocol','keywords','pharmacology','surgery','stimulus_notes','data_collection']:
    print(k, getattr(nwb,k,None))
if nwb.units is not None:
    print(nwb.units.to_dataframe().head()); print(nwb.units.colnames)
    for c in nwb.units.colnames: print(c, nwb.units[c].description)
for n,t in (nwb.intervals or {}).items():
    print(n, t.colnames); print(t.to_dataframe().head(10)); print(len(t))
    for c in t.colnames: print(c, t[c].description)
print(nwb.electrodes.to_dataframe().head() if nwb.electrodes is not None else None)
print(nwb.devices, nwb.electrode_groups)
EOF
python open1.py sub-BH497/sub-BH497_ses-20240310T143729_ecephys.nwb 2>&1 | head -250
```

```
acquisition/ {}
analysis/ {}
file_create_date (2,) object {}
general/ {}
  devices/ {}
    array/ {'description': 'A1x32-Poly3-10mm-50-177-Z32', 'manufacturer': 'Neuronexus', 'namespace': 'core', 'neurodata_type': 'Device'}
  extracellular_ephys/ {}
    electrodes/ {'colnames': "['x' 'y' 'z' 'imp' 'location' 'filtering' 'group' 'group_name']", 'description': 'all electrodes', 'namespace': 'hdmf-common', 'neurodata_type': 'DynamicTable'}
      filtering (32,) object {'description': 'my description', 'neurodata_type': 'VectorData'}
      group (32,) object {'description': 'my description', 'neurodata_type': 'VectorData'}
      group_name (32,) object {'description': 'my description', 'neurodata_type': 'VectorData'}
      id (32,) int64 {'neurodata_type': 'ElementIdentifiers'}
      imp (32,) float64 {'description': 'my description', 'neurodata_type': 'VectorData'}
      location (32,) object {'description': 'my description', 'neurodata_type': 'VectorData'}
      x (32,) float64 {'description': 'my description', 'neurodata_type': 'VectorData'}
      y (32,) float64 {'description': 'my description', 'neurodata_type': 'VectorData'}
      z (32,) float64 {'description': 'my description', 'neurodata_type': 'VectorData'}
    shank1/ {'description': 'electrode group for shank1', 'location': 'brain area', 'namespace': 'core', 'neurodata_type': 'ElectrodeGroup'}
      device/ {'description': 'A1x32-Poly3-10mm-50-177-Z32', 'manufacturer': 'Neuronexus', 'namespace': 'core', 'neurodata_type': 'Device'}
  institution () object {}
[... 156 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > survey.py <<'EOF'
import json, h5py, remfile, numpy as np, pandas as pd, hashlib
from concurrent.futures import ThreadPoolExecutor
a=json.load(open('assets_0.250213.2212.json'))['results']
def one(x):
    url=f"https://api.dandiarchive.org/api/assets/{x['asset_id']}/download/"
    f=h5py.File(remfile.File(url),'r')
    s=lambda k: f[k][()].decode() if isinstance(f[k][()],bytes) else str(f[k][()])
    lab=f['units/celltype_label'][:]
    idx=f['units/spike_times_index'][:]
    st0=f['units/spike_times'][:2000]
    tr=f['intervals/trials/start_time'][:]; sp=f['intervals/trials/stop_time'][:]
    return dict(path=x['path'], subj=s('general/subject/subject_id'), ident=s('identifier'), desc=s('session_description'),
        start=s('session_start_time'), age=s('general/subject/age'), n_units=len(lab), n_rsu=int((lab==1).sum()), n_fsu=int((lab==2).sum()),
        other_lab=str(sorted(set(lab[~np.isin(lab,[1,2])].tolist()))), n_spk=int(idx[-1]) if len(idx) else 0, n_tr=len(tr),
        tr0=round(tr[0],3), trlast=round(tr[-1],3), dur=round(float(np.median(sp-tr)),3), isi_med=round(float(np.median(np.diff(tr))),3),
        isi_min=round(float(np.min(np.diff(tr))),3), isi_max=round(float(np.max(np.diff(tr))),3),
        h=hashlib.md5(st0.tobytes()).hexdigest()[:8], htr=hashlib.md5(tr.tobytes()).hexdigest()[:8])
with ThreadPoolExecutor(12) as ex: rows=list(ex.map(one,a))
df=pd.DataFrame(rows); df.to_csv('survey.csv',index=False)
pd.set_option('display.width',300); pd.set_option('display.max_rows',100); pd.set_option('display.max_columns',30)
print(df.drop(columns=['path']).to_string())
EOF
time python survey.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/survey.py", line 18, in <module>
    with ThreadPoolExecutor(12) as ex: rows=list(ex.map(one,a))
                                            ~~~~^^^^^^^^^^^^^^^
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
  File "/tmp/claude-1001/survey.py", line 8, in one
    lab=f['units/celltype_label'][:]
[... 16 more lines not kept]
```

**Agent**

Some files lack `celltype_label`. I'll make the survey robust and record each file's column list.

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import re
s=open('survey.py').read()
s=s.replace("    lab=f['units/celltype_label'][:]\n","    ucols=f['units'].attrs['colnames']; tcols=f['intervals/trials'].attrs['colnames']\n    lab=f['units/celltype_label'][:] if 'celltype_label' in f['units'] else np.full(len(f['units/id']),np.nan)\n    other=[k for k in f.keys()]\n")
s=s.replace("htr=hashlib","ucols=' '.join(map(str,ucols)), tcols=' '.join(map(str,tcols)), acq=' '.join(f['acquisition'].keys())+'|'+' '.join(f['processing'].keys()), htr=hashlib")
open('survey.py','w').write(s)
EOF
time python survey.py
```

```
<persisted-output>
Output too large (44.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/de22c3be-727e-412f-8496-f1c533ac48f3/tool-results/bztwbprxc.txt

Preview (first 2KB):
     subj                 ident                                     desc                                  start   age  n_units  n_rsu  n_fsu                                                                                                                                                                                                                                                                                                                         other_lab    n_spk  n_tr    tr0    trlast  dur  isi_med  isi_min  isi_max         h                       ucols                 tcols acq       htr
0   BH498        BH498_1500_200             Awake S1 Stimulation by tFUS       2024-03-06T12:42:27.000000-05:00  P24W       37     25     12                                                                                                                                                                                                                                                                                                                                []   185837   500  0.298  1273.798  2.2    2.514    2.252   25.336  6f678c95  spike_times celltype_label  start_time stop_time   |  608535d6
1   BH498      BH498_1500_200_2             Awake S1 Stimulation by tFUS       2024-03-05T20:06:06.000000-05:00  P24W       64     32     32                                                                                                                                                                                                                                                                                                                                []   295768   500  0.388  1249.654  2.2    2.496    2.251    2.750  72fc47a6  spike_times celltype_label  start_time stop_
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python -c "
import pandas as pd
pd.set_option('display.width',250); pd.set_option('display.max_rows',100)
d=pd.read_csv('survey.csv')
d['other_lab']=d.other_lab.str.slice(0,30)
d['ses']=d.path.str.extract(r'ses-(\w+)_')[0]
print(d[['subj','ses','ident','desc','age','n_units','n_rsu','n_fsu','other_lab','n_spk','tr0','trlast','isi_min','isi_max','h','htr']].to_string())
print(d.ucols.value_counts()); print(d.tcols.value_counts()); print(d.acq.value_counts())
"
```

```
subj              ses                 ident                                     desc   age  n_units  n_rsu  n_fsu                       other_lab    n_spk    tr0    trlast  isi_min  isi_max         h       htr
0   BH498  20240306T124227        BH498_1500_200             Awake S1 Stimulation by tFUS  P24W       37     25     12                              []   185837  0.298  1273.798    2.252   25.336  6f678c95  608535d6
1   BH498  20240305T200606      BH498_1500_200_2             Awake S1 Stimulation by tFUS  P24W       64     32     32                              []   295768  0.388  1249.654    2.251    2.750  72fc47a6  2062af62
2   BH498  20240305T191833      BH498_4500_200_2             Awake S1 Stimulation by tFUS  P24W       64     32     32                              []   674653  0.351  1242.705    2.250    2.749  add05f61  583b8c8a
3   BH498  20230906T180913        BH498_3000_200             Awake S1 Stimulation by tFUS  P24W       72     31     41                              []   818408  0.276  1250.898    2.251    2.750  b69956bd  5681c21d
4   BH498  20240305T204552      BH498_3000_200_2             Awake S1 Stimulation by tFUS  P24W       64     36     28                              []   513001  0.375  1249.254    2.252    2.750  4dadb204  cf7ab253
5   BH506  20231026T155106        BH506_4500_200             Awake S1 Stimulation by tFUS  P24W       64     29     35                              []   798737  0.242  1253.923    2.251    2.749  dc2d5af1  9761f818
6   BH498  20240306T175805          BH498_30_200             Awake S1 Stimulation by tFUS  P24W       31     26      5                              []    35497  0.429   504.470    2.251    2.750  1fc748c7  fee36794
7   BH506  20231018T181609        BH506_1500_200             Awake S1 Stimulation by tFUS  P24W       71     37     34                              []   458136  0.273  1249.649    2.252    2.750  34796d74  29a42dd3
8   BH498  20240306T231317        BH498_4500_200             Awake S1 
[... 77 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . env/bin/activate && cat > chk.py <<'EOF'
import json, h5py, remfile, numpy as np, pandas as pd
a={r['path']:r for r in json.load(open('assets_0.250213.2212.json'))['results']}
def op(p): return h5py.File(remfile.File(f"https://api.dandiarchive.org/api/assets/{a[p]['asset_id']}/download/"),'r')
for p in ['sub-BH498/sub-BH498_ses-20240306T175805_ecephys.nwb','sub-BH508/sub-BH508_ses-20240307T002354_ecephys.nwb','sub-BH508/sub-BH508_ses-20230827T140843_ecephys.nwb','sub-BH519/sub-BH519_ses-20231022T163921_ecephys.nwb']:
    f=op(p); tr=f['intervals/trials/start_time'][:]; st=f['units/spike_times'][:]; idx=f['units/spike_times_index'][:]
    d=np.diff(tr)
    print(p, 'sorted',np.all(d>0), 'n',len(tr), 'tr range',tr[0],tr[-1], 'spk range',st.min(),st.max(), 'diff quantiles',np.round(np.quantile(d,[0,.01,.5,.99,1]),3), 'n gaps>3s',(d>3).sum())
    # per unit sortedness
    starts=np.r_[0,idx[:-1]]; uns=sum(np.any(np.diff(st[s:e])<0) for s,e in zip(starts,idx)); print(' units unsorted',uns, 'units',len(idx))
    # PSTH all units, 10ms bins around trials
    rel=[]; 
    for t in tr:
        lo,hi=np.searchsorted(st,[t-0.5,t+1.5]) if False else (None,None)
    sts=np.sort(st)
    edges=np.arange(-0.5,1.5001,0.01); h=np.zeros(len(edges)-1)
    for t in tr:
        i0,i1=np.searchsorted(sts,[t-0.5,t+1.5]); h+=np.histogram(sts[i0:i1]-t,edges)[0]
    h=h/len(tr)/0.01
    print(' pop rate per 10ms bin, -0.1..0.3 s:', np.round(h[40:80]).astype(int).tolist())
EOF
python chk.py
```

```
Sat Oct 31 21:32:27 UTC 2026
sub-BH498/sub-BH498_ses-20240306T175805_ecephys.nwb sorted True n 203 tr range 0.42860544 504.47015936 spk range 0.00233472 506.2899712 diff quantiles [2.251 2.253 2.49  2.745 2.75 ] n gaps>3s 0
 units unsorted 0 units 31
 pop rate per 10ms bin, -0.1..0.3 s: [59, 76, 70, 76, 66, 57, 52, 69, 65, 68, 59, 65, 58, 67, 53, 61, 52, 59, 51, 57, 67, 66, 59, 61, 57, 64, 74, 72, 78, 77, 75, 79, 96, 73, 88, 68, 73, 52, 71, 67]
sub-BH508/sub-BH508_ses-20240307T002354_ecephys.nwb sorted True n 203 tr range 0.42860544 504.47015936 spk range 0.00233472 506.26281472 diff quantiles [2.251 2.253 2.49  2.745 2.75 ] n gaps>3s 0
 units unsorted 0 units 26
 pop rate per 10ms bin, -0.1..0.3 s: [45, 75, 70, 68, 60, 54, 43, 67, 57, 54, 54, 59, 54, 60, 52, 52, 44, 49, 50, 55, 58, 55, 56, 56, 62, 52, 71, 71, 65, 69, 71, 84, 84, 68, 83, 61, 66, 47, 60, 62]
sub-BH508/sub-BH508_ses-20230827T140843_ecephys.nwb sorted True n 328 tr range 0.2551808 814.18825728 spk range 0.00237568 816.12632064 diff quantiles [2.25  2.254 2.482 2.743 2.749] n gaps>3s 0
 units unsorted 0 units 73
 pop rate per 10ms bin, -0.1..0.3 s: [2803, 2733, 2787, 2821, 2760, 2801, 2734, 2836, 2800, 2784, 2913, 3041, 2925, 2908, 2874, 2972, 2874, 2813, 2695, 2750, 2768, 2639, 2733, 2673, 2805, 2742, 2698, 2741, 2779, 2773, 2772, 2810, 2764, 2804, 2730, 2688, 2709, 2817, 2739, 2784]
sub-BH519/sub-BH519_ses-20231022T163921_ecephys.nwb sorted True n 500 tr range 0.27803648 1249.6664576 spk range 0.00114688 1253.40504064 diff quantiles [2.252 2.259 2.507 2.739 2.749] n gaps>3s 0
 units unsorted 0 units 82
 pop rate per 10ms bin, -0.1..0.3 s: [321, 347, 327, 314, 329, 306, 313, 287, 341, 282, 307, 342, 332, 294, 325, 284, 296, 302, 341, 326, 286, 321, 291, 286, 328, 314, 305, 336, 335, 302, 340, 308, 326, 342, 346, 352, 308, 315, 326, 289]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python -c "
import pandas as pd; d=pd.read_csv('survey.csv'); print(d[['ident','n_tr','tr0','trlast']].sort_values('n_tr').head(15).to_string()); print(d.n_tr.value_counts())
d['span']=d.trlast-d.tr0; print((d.span/(d.n_tr-1)).describe())
" ; cat >> chk2.py <<'EOF'
import json, h5py, remfile, numpy as np
a={r['path']:r for r in json.load(open('assets_0.250213.2212.json'))['results']}
def op(p): return h5py.File(remfile.File(f"https://api.dandiarchive.org/api/assets/{a[p]['asset_id']}/download/"),'r')
A=op('sub-BH498/sub-BH498_ses-20240306T175805_ecephys.nwb')['units/spike_times'][:]
B=op('sub-BH508/sub-BH508_ses-20240307T002354_ecephys.nwb')['units/spike_times'][:]
ua,ub=np.unique(np.round(A,5)),np.unique(np.round(B,5))
print(len(ua),len(ub),'shared exact',len(np.intersect1d(ua,ub)))
EOF
python chk2.py
```

```
ident  n_tr    tr0    trlast
6       BH498_30_200   203  0.429   504.470
23    BH508_30_200_2   203  0.429   504.470
19  BH508_1500_200_2   238  0.274   593.572
18    BH508_3000_200   328  0.255   814.188
21    BH508_1500_200   339  0.276   843.236
0     BH498_1500_200   500  0.298  1273.798
2   BH498_4500_200_2   500  0.351  1242.705
1   BH498_1500_200_2   500  0.388  1249.654
8     BH498_4500_200   500  0.245  1244.696
9      BH498_300_200   500  0.244  1252.356
10    BH506_3000_200   500  0.360  1248.181
11  BH506_3000_200_2   500  0.396  1251.756
3     BH498_3000_200   500  0.276  1250.898
4   BH498_3000_200_2   500  0.375  1249.254
5     BH506_4500_200   500  0.242  1253.923
n_tr
500    70
203     2
328     1
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p entries/000945-ramachandran-2025
```

```
(Bash completed with no output)
```

**Agent calls Write**

```json
{
 "file_path": "entries/000945-ramachandran-2025/tfus.py",
 "content": "\"\"\"Loading and response measures for dandiset 000945 (tFUS in awake and anesthetized rat S1).\n\nRamachandran, Gao, Yttri, Yu & He (2025), J Neural Eng 22 026022, doi:10.1088/1741-2552/adbb1f.\n\nEach NWB file holds one recording: sorted units (`units/spike_times`, and in 60 of the 75 files a\n`celltype_label`, \"1 = RSU, 2 = FSU\") and a trial table whose `start_time` is taken as the\nultrasound trigger (time 0; checked in the notebook). The condition is only in the file's\n`identifier`, as `<rat>_<PRF Hz>_<TBD us>[_2][_anes|_anes2]`. Files are streamed from the archive\nat the pinned version; nothing is written to disk.\n\nWhere the parameters come from:\n\n- PSTH from -0.5 to 1.5 s around the trigger, divided by the number of trials; baseline the 0.5 s\n  before onset; response the mean rate in a window as a percent of baseline (Methods 2.4, \"PSTHs\n  were computed from 0.5 s prior to ultrasound stimulation, until 1.5 s afterwards ... Baseline was\n  computed from the 0.5 s before tFUS onset, and the response to tFUS was characterized as the\n  normalized spike rate as a percent of baseline within the specified time span\").\n- Bin 35.7 ms (Figure 4 legend, \"bin size: 35.7 ms\"), taken as 1/28 s so that the 0.5 s baseline\n  is 14 whole bins with an edge at 0 (claims file header).\n- Windows: time-locked 0 to 67 ms (Methods 2.4, \"the response during the 67 ms ultrasound\n  stimulation\"); delayed 0.5 to 1 s awake and 0.2 to 0.7 s anesthetized (Figure 5 legend). The\n  claims file names two ways to measure a window that is not on bin edges: W1, spikes in the exact\n  window; W2, the PSTH bins that overlap it. Both are computed.\n- Delayed-response latency (Methods 2.4, \"at least three consecutive time bins in their PSTH with\n  value greater or equal to one SEM above baseline. Latency was then characterized as the time bin\n  of the first of the three\"). The SEM (S1, S2), the first bin allowed (D1, D2) and the time of a\n  bin (L1, L2) are the claims file's readings; every combination is computed.\n- A unit with no spike in the baseline cannot be normalized and is left out (claims file header, a\n  standard choice; the count is reported).\n- The 5 ms PSTH (`psth5`) is a display and clock-check choice that cannot change an outcome.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport itertools\nimport re\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nfrom dandi.dandiapi import DandiAPIClient\nfrom scipy import stats\n\nDANDISET_ID = \"000945\"\nDANDISET_VERSION = \"0.250213.2212\"   # the version the paper cites (reference 50)\n\nBIN = 1 / 28                          # 35.714 ms\nPRE, POST = 0.5, 1.5\nEDGES = np.round(np.arange(-14, 43) * BIN, 10)  # 56 bins from -0.5 to 1.5 s\nN_BASE_BINS = 14\nUS_DURATION = 0.067\nFINE = 0.005\nFINE_EDGES = np.round(np.arange(-PRE, POST + FINE / 2, FINE), 10)\n\n# Windows in seconds from the trigger. *_w2 are the bins that overlap the window.\nWINDOWS = {\n    \"base\": (-0.5, 0.0),\n    \"tl_w1\": (0.0, 0.067),\n    \"tl_w2\": (0.0, 2 * BIN),\n    \"del_awake\": (0.5, 1.0),           # on bin edges, the same under W1 and W2\n    \"del_anes_w1\": (0.2, 0.7),\n    \"del_anes_w2\": (5 * BIN, 20 * BIN),\n    # clock check: the same 67 ms window and 0.5 s baseline, 1.25 s later (mid-interval)\n    \"shift_base\": (0.75, 1.25),\n    \"shift_tl\": (1.25, 1.25 + 0.067),\n}\n\nPRF_ISPTA = {30: 0.6, 300: 6.03, 1500: 30.13, 3000: 60.26, 4500: 90.39}  # mW/cm2, Methods 2.3\nTBD_DC = {40: 6, 200: 30, 400: 60}                                       # us -> %, Methods 2.3\n\n_IDENT = re.compile(r\"^(BH\\d+)_(\\d+)_(\\d+)(_2)?(_anes2?)?$\")\n\n\ndef parse_identifier(ident: str) -> dict:\n    \"\"\"Rat, PRF, TBD, state and repeat flag from an identifier such as BH498_1500_200_2.\"\"\"\n    m = _IDENT.match(ident)\n    if not m:\n        raise ValueError(f\"unexpected identifier {ident}\")\n    rat, prf, tbd, rep, anes = m.groups()\n    return {\"rat\": rat, \"prf\": int(prf), \"tbd\": int(tbd), \"dc\": TBD_DC.get(int(tbd)),\n            \"state\": \"anesthetized\" if anes else \"awake\",\n            \"repeat\": bool(rep) or anes == \"_anes2\"}\n\n\ndef asset_list() -> list[dict]:\n    \"\"\"Path, asset id, size and streaming URL of every NWB file at the pinned version.\"\"\"\n    with DandiAPIClient() as client:\n        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)\n        return sorted(({\"path\": a.path, \"asset_id\": a.identifier, \"size\": a.size,\n                        \"url\": a.get_content_url(follow_redirects=1, strip_query=True)}\n                       for a in ds.get_assets() if a.path.endswith(\".nwb\")), key=lambda r: r[\"path\"])\n\n\ndef _str(v) -> str:\n    v = v[()] if hasattr(v, \"shape\") else v\n    return v.decode() if isinstance(v, bytes) else str(v)\n\n\ndef _counts(st: np.ndarray, tr: np.ndarray, lo: float, hi: float) -> np.ndarray:\n    \"\"\"Spikes of one unit in [t + lo, t + hi) for each trial t.\"\"\"\n    return (np.searchsorted(st, tr + hi, \"left\") - np.searchsorted(st, tr + lo, \"left\")).astype(np.int32)\n\n\ndef load_session(asset: dict) -> dict:\n    \"\"\"Read one file and reduce it to per-unit, per-trial window counts and trial-averaged PSTHs.\"\"\"\n    with h5py.File(remfile.File(asset[\"url\"]), \"r\") as f:\n        ident = _str(f[\"identifier\"])\n        meta = {\n            \"path\": asset[\"path\"], \"identifier\": ident,\n            \"subject_id\": _str(f[\"general/subject/subject_id\"]),\n            \"age\": _str(f[\"general/subject/age\"]),\n            \"session_description\": _str(f[\"session_description\"]),\n            \"session_start\": _str(f[\"session_start_time\"]),\n            \"units_colnames\": list(map(_str, f[\"units\"].attrs[\"colnames\"])),\n            \"trials_colnames\": list(map(_str, f[\"intervals/trials\"].attrs[\"colnames\"])),\n            \"acquisition\": list(f[\"acquisition\"].keys()), \"processing\": list(f[\"processing\"].keys()),\n        }\n        tr = f[\"intervals/trials/start_time\"][:]\n        stop = f[\"intervals/trials/stop_time\"][:]\n        st_all = f[\"units/spike_times\"][:]\n        idx = f[\"units/spike_times_index\"][:]\n        lab = f[\"units/celltype_label\"][:] if \"celltype_label\" in f[\"units\"] else np.full(len(idx), np.nan)\n        ids = f[\"units/id\"][:]\n    meta.update(parse_identifier(ident))\n    starts = np.r_[0, idx[:-1]].astype(int)\n    n_u, n_t = len(idx), len(tr)\n    counts = np.zeros((n_u, n_t, len(WINDOWS)), np.int32)\n    psth = np.zeros((n_u, len(EDGES) - 1))\n    psth5 = np.zeros((n_u, len(FINE_EDGES) - 1), np.float32)\n    base_bins = np.zeros((n_u, n_t), np.int32)\n    n_spikes, sorted_ok = np.zeros(n_u, int), True\n    for u, (s, e) in enumerate(zip(starts, idx.astype(int))):\n        st = st_all[s:e]\n        if np.any(np.diff(st) < 0):\n            sorted_ok = False\n            st = np.sort(st)\n        n_spikes[u] = len(st)\n        for k, (lo, hi) in enumerate(WINDOWS.values()):\n            counts[u, :, k] = _counts(st, tr, lo, hi)\n        i0 = np.searchsorted(st, tr - PRE)\n        i1 = np.searchsorted(st, tr + POST)\n        rel = np.concatenate([st[a:b] - t for a, b, t in zip(i0, i1, tr)]) if n_t else np.array([])\n        psth[u] = np.histogram(rel, EDGES)[0] / n_t\n        psth5[u] = np.histogram(rel, FINE_EDGES)[0] / n_t / FINE\n        base_bins[u] = counts[u, :, 0]\n    meta.update({\n        \"n_units\": n_u, \"n_trials\": n_t, \"trial_times\": tr, \"trial_len\": stop - tr,\n        \"spike_range\": (float(st_all.min()), float(st_all.max())) if len(st_all) else (np.nan, np.nan),\n        \"spikes_sorted\": sorted_ok, \"unit_ids\": ids, \"label\": lab, \"n_spikes\": n_spikes,\n        \"counts\": counts, \"psth\": psth, \"psth5\": psth5,\n        \"first_spikes\": st_all[:5000].copy(),\n    })\n    return meta\n\n\ndef load_all(assets: list[dict], threads: int = 12) -> list[dict]:\n    with ThreadPoolExecutor(threads) as ex:\n        return list(ex.map(load_session, assets))\n\n\ndef window_index(name: str) -> int:\n    return list(WINDOWS).index(name)\n\n\ndef unit_table(sessions: list[dict]) -> pd.DataFrame:\n    \"\"\"One row per unit: condition, cell type, baseline rate and normalized responses (% of baseline).\n\n    The response is the window's mean rate over trials divided by the baseline's mean rate, times\n    100 (the ratio in percent; claims file header).\n    \"\"\"\n    rows = []\n    for s in sessions:\n        c = s[\"counts\"].sum(axis=1)          # units x windows, summed over trials\n        n_t = s[\"n_trials\"]\n        dur = {k: hi - lo for k, (lo, hi) in WINDOWS.items()}\n        rate = {k: c[:, i] / (n_t * dur[k]) for i, k in enumerate(WINDOWS)}\n        for u in range(s[\"n_units\"]):\n            lab = s[\"label\"][u]\n            r = {\"session\": s[\"identifier\"], \"path\": s[\"path\"], \"rat\": s[\"rat\"],\n                 \"subject_id\": s[\"subject_id\"], \"state\": s[\"state\"], \"prf\": s[\"prf\"], \"tbd\": s[\"tbd\"],\n                 \"dc\": s[\"dc\"], \"repeat\": s[\"repeat\"], \"unit\": u,\n                 \"celltype\": {1.0: \"RSU\", 2.0: \"FSU\"}.get(lab, None) if not np.isnan(lab) else None,\n                 \"n_trials\": n_t, \"n_spikes\": int(s[\"n_spikes\"][u]), \"base_hz\": rate[\"base\"][u]}\n            for k in WINDOWS:\n                if k in (\"base\", \"shift_base\"):\n                    continue\n                b = rate[\"shift_base\"][u] if k.startswith(\"shift\") else rate[\"base\"][u]\n                r[k] = 100 * rate[k][u] / b if b > 0 else np.nan\n            rows.append(r)\n    return pd.DataFrame(rows)\n\n\ndef delayed_window(state: str, w: str) -> str:\n    \"\"\"Column of the delayed response for a state and window reading (W1 or W2).\"\"\"\n    if state == \"awake\":\n        return \"del_awake\"\n    return \"del_anes_w1\" if w == \"W1\" else \"del_anes_w2\"\n\n\ndef group_test(groups: dict, alpha: float = 0.05) -> tuple[dict, pd.DataFrame]:\n    \"\"\"Kruskal-Wallis over the groups, then two-sided rank-sum tests between every pair,\n    Bonferroni-corrected over all pairs (Methods 2.6; claims file header).\"\"\"\n    names = [g for g in groups if len(groups[g]) > 0]\n    vals = [np.asarray(groups[g], float) for g in names]\n    kw = stats.kruskal(*vals) if len(vals) > 1 else None\n    pairs = list(itertools.combinations(names, 2))\n    rows = []\n    for a, b in pairs:\n        x, y = np.asarray(groups[a], float), np.asarray(groups[b], float)\n        p = stats.ranksums(x, y).pvalue\n        rows.append({\"a\": a, \"b\": b, \"n_a\": len(x), \"n_b\": len(y), \"mean_a\": x.mean(), \"mean_b\": y.mean(),\n                     \"median_a\": np.median(x), \"median_b\": np.median(y), \"p\": p,\n                     \"p_bonf\": min(1.0, p * len(pairs))})\n    post = pd.DataFrame(rows)\n    if len(post):\n        post[\"sig\"] = post.p_bonf < alpha\n    out = {\"H\": kw.statistic if kw else np.nan, \"p\": kw.pvalue if kw else np.nan,\n           \"n\": {g: len(v) for g, v in zip(names, vals)},\n           \"mean\": {g: float(np.mean(v)) for g, v in zip(names, vals)},\n           \"median\": {g: float(np.median(v)) for g, v in zip(names, vals)}}\n    return out, post\n\n\ndef pair(post: pd.DataFrame, a, b) -> pd.Series:\n    \"\"\"The post hoc row for groups a and b, oriented so that mean_a is a's mean.\"\"\"\n    r = post[((post.a == a) & (post.b == b)) | ((post.a == b) & (post.b == a))].iloc[0].copy()\n    if r.a != a:\n        r[\"a\"], r[\"b\"] = a, b\n        r[\"mean_a\"], r[\"mean_b\"] = r[\"mean_b\"], r[\"mean_a\"]\n        r[\"median_a\"], r[\"median_b\"] = r[\"median_b\"], r[\"median_a\"]\n        r[\"n_a\"], r[\"n_b\"] = r[\"n_b\"], r[\"n_a\"]\n    return r\n\n\ndef latency(psth: np.ndarray, base_counts: np.ndarray, sem: str, first: str, timing: str) -> float:\n    \"\"\"Delayed-response onset of one unit (s), or nan when it has no significant delayed response.\n\n    psth: trial-averaged spikes per 1/28 s bin over -0.5 to 1.5 s (56 bins).\n    base_counts: spikes in the 0.5 s baseline of each trial.\n    sem: S1, SEM over the 14 baseline bins of the trial-averaged PSTH; S2, SEM over trials of the\n    per-trial baseline in spikes per bin. first: D1, bins starting at or after 67 ms; D2, bins\n    ending after 67 ms. timing: L1, a bin's start; L2, its centre.\n    \"\"\"\n    base = psth[:N_BASE_BINS]\n    mu = base.mean()\n    if sem == \"S1\":\n        se = base.std(ddof=1) / np.sqrt(len(base))\n    else:\n        per_bin = base_counts / N_BASE_BINS\n        se = per_bin.std(ddof=1) / np.sqrt(len(per_bin))\n    post = psth[N_BASE_BINS:]\n    starts = EDGES[N_BASE_BINS:-1]\n    ends = EDGES[N_BASE_BINS + 1:]\n    allowed = starts >= US_DURATION - 1e-12 if first == \"D1\" else ends > US_DURATION\n    above = (post >= mu + se) & allowed\n    run = 0\n    for k, a in enumerate(above):\n        run = run + 1 if a else 0\n        if run == 3:\n            j = k - 2\n            return float(starts[j] if timing == \"L1\" else starts[j] + BIN / 2)\n    return np.nan\n"
}
```

```
File created successfully at: entries/000945-ramachandran-2025/tfus.py (file state is current in your context — no need to Read it back)
```

**Agent**

Helper written. Timing it on 3 files before loading everything.

**Agent calls Bash**

```bash
cd entries/000945-ramachandran-2025 && . $TMPDIR/env/bin/activate && python -c "
import time, tfus
t=time.time(); A=tfus.asset_list(); print(len(A), time.time()-t)
sub=[a for a in A if 'BH526_ses-20231029T182226' in a['path'] or 'BH519_ses-20231022' in a['path'] or 'BH497_ses-20240310T145053' in a['path']]
print([ (a['path'],a['size']) for a in sub])
t=time.time(); S=tfus.load_all(sub); print('load', time.time()-t)
u=tfus.unit_table(S); print(u.groupby(['session','celltype'])[['tl_w1','tl_w2','del_awake','shift_tl']].median())
"
```

```
75 7.708178758621216
[('sub-BH497/sub-BH497_ses-20240310T145053_ecephys.nwb', 9352600), ('sub-BH519/sub-BH519_ses-20231022T163921_ecephys.nwb', 3451192), ('sub-BH526/sub-BH526_ses-20231029T182226_ecephys.nwb', 41549160)]
load 2.8259103298187256
                                   tl_w1       tl_w2   del_awake    shift_tl
session             celltype                                                
BH498_1500_200_anes FSU       102.195679  102.271837   99.279050   99.441293
                    RSU       102.416519  101.752886   99.264870  100.655836
BH519_1500_200      FSU       100.811731  100.676819  102.954342  106.417372
                    RSU       103.807360  104.255319  126.685393  101.521034
BH526_30_200        FSU        97.638246   97.598466   99.767776   99.083286
                    RSU        93.947676   94.276442  103.714876   94.107888
```

**Agent**

Fast (3 s for 3 files). Loading all 75 into a development cache.

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && python -c "
import time, tfus, pickle
t=time.time(); A=tfus.asset_list(); S=tfus.load_all(A); print('load', time.time()-t)
pickle.dump(S, open('$TMPDIR/S.pkl','wb'))
"; date -u
```

```
load 44.28411650657654
Sat Oct 31 21:35:08 UTC 2026
```

**Agent**

All 75 files load in 44 s. Next: deduplication rules and a first pass over every claim's numbers.

**Agent calls Bash**

```bash
cat >> tfus.py <<'EOF'


def find_duplicates(sessions: list[dict]) -> pd.DataFrame:
    """Recordings deposited more than once: files with identical trial times.

    For each group, the copy kept is the one with cell-type labels, then a non-repeat identifier,
    then the first path. Returns one row per file with `kept` and `duplicate_of`.
    """
    key = {}
    for s in sessions:
        key.setdefault(s["trial_times"].tobytes(), []).append(s)
    rows = []
    for grp in key.values():
        order = sorted(grp, key=lambda s: (np.all(np.isnan(s["label"])), s["repeat"], s["path"]))
        keep = order[0]
        for s in grp:
            rows.append({"path": s["path"], "identifier": s["identifier"], "subject_id": s["subject_id"],
                         "kept": s is keep, "duplicate_of": None if s is keep else keep["path"],
                         "group_size": len(grp)})
    return pd.DataFrame(rows)
EOF
cat > $TMPDIR/explore.py <<'EOF'
import pickle, sys, numpy as np, pandas as pd
sys.path.insert(0,'.')
import tfus
pd.set_option('display.width',250); pd.set_option('display.max_rows',300)
S=pickle.load(open(sys.argv[1] if len(sys.argv)>1 else '/tmp/claude-1001/S.pkl','rb'))
dup=tfus.find_duplicates(S); print(dup[dup.group_size>1].to_string())
kept=set(dup[dup.kept].path)
U=tfus.unit_table([s for s in S if s['path'] in kept])
print(len(U), U.celltype.value_counts(dropna=False))
print(U.groupby(['state','prf','tbd','repeat'])['session'].nunique())
U.to_pickle('/tmp/claude-1001/U.pkl')
EOF
. $TMPDIR/env/bin/activate && python $TMPDIR/explore.py
```

```
path            identifier subject_id   kept                                         duplicate_of  group_size
0   sub-BH497/sub-BH497_ses-20240310T143729_ecephys.nwb   BH498_3000_200_anes      BH497   True                                                  NaN           2
1   sub-BH498/sub-BH498_ses-20240310T143729_ecephys.nwb   BH498_3000_200_anes      BH498  False  sub-BH497/sub-BH497_ses-20240310T143729_ecephys.nwb           2
2   sub-BH497/sub-BH497_ses-20240310T145053_ecephys.nwb   BH498_1500_200_anes      BH497   True                                                  NaN           2
3   sub-BH498/sub-BH498_ses-20240310T145053_ecephys.nwb   BH498_1500_200_anes      BH498  False  sub-BH497/sub-BH497_ses-20240310T145053_ecephys.nwb           2
4   sub-BH497/sub-BH497_ses-20240310T145814_ecephys.nwb    BH498_300_200_anes      BH497   True                                                  NaN           2
5   sub-BH498/sub-BH498_ses-20240310T145814_ecephys.nwb    BH498_300_200_anes      BH498  False  sub-BH497/sub-BH497_ses-20240310T145814_ecephys.nwb           2
6   sub-BH497/sub-BH497_ses-20240310T150748_ecephys.nwb     BH498_30_200_anes      BH497   True                                                  NaN           2
7   sub-BH498/sub-BH498_ses-20240310T150748_ecephys.nwb     BH498_30_200_anes      BH498  False  sub-BH497/sub-BH497_ses-20240310T150748_ecephys.nwb           2
8   sub-BH497/sub-BH497_ses-20240310T152652_ecephys.nwb   BH498_4500_200_anes      BH497   True                                                  NaN           2
9   sub-BH498/sub-BH498_ses-20240310T152652_ecephys.nwb   BH498_4500_200_anes      BH498  False  sub-BH497/sub-BH497_ses-20240310T152652_ecephys.nwb           2
15  sub-BH498/sub-BH498_ses-20240306T175805_ecephys.nwb          BH498_30_200      BH498   True                                                  NaN           2
16  sub-BH508/sub-BH508_ses-20240307T002354_ecephys.nwb        BH508_30_200_2      BH508  False  sub-BH498/sub-BH498_se
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/ex2.py <<'EOF'
import pickle, sys, numpy as np, pandas as pd
sys.path.insert(0,'.')
import tfus
pd.set_option('display.width',250); pd.set_option('display.max_rows',300)
U=pd.read_pickle('/tmp/claude-1001/U.pkl')
print('zero baseline', U.base_hz.eq(0).sum())
L=U[U.celltype.notna() & U.base_hz.gt(0)]
prf=L[L.tbd==200]
for rep in [True, False]:
  P = prf if rep else prf[~prf.repeat]
  print('==== include repeats', rep)
  for st in ['awake','anesthetized']:
    for ct in ['RSU','FSU']:
      for col in ['tl_w1','tl_w2', tfus.delayed_window(st,'W1'), tfus.delayed_window(st,'W2')]:
        d=P[(P.state==st)&(P.celltype==ct)]
        g={p:d[d.prf==p][col].values for p in [30,300,1500,3000,4500]}
        o,post=tfus.group_test(g)
        print(st,ct,col,'KW p=%.2g'%o['p'], 'n',o['n'], 'means',{k:round(v,1) for k,v in o['mean'].items()})
        print('   sig pairs:', [(r.a,r.b,'%.1e'%r.p_bonf) for r in post.itertuples() if r.sig])
EOF
. $TMPDIR/env/bin/activate && python $TMPDIR/ex2.py
```

```
zero baseline 0
==== include repeats True
awake RSU tl_w1 KW p=3.3e-16 n {30: 255, 300: 269, 1500: 303, 3000: 334, 4500: 270} means {30: 96.8, 300: 97.6, 1500: 98.5, 3000: 108.2, 4500: 99.2}
   sig pairs: [(30, 3000, '9.2e-17'), (30, 4500, '2.8e-02'), (300, 3000, '1.1e-07'), (1500, 3000, '4.8e-06'), (3000, 4500, '1.9e-08')]
awake RSU tl_w2 KW p=6.2e-16 n {30: 255, 300: 269, 1500: 303, 3000: 334, 4500: 270} means {30: 96.4, 300: 97.4, 1500: 98.7, 3000: 107.7, 4500: 99.5}
   sig pairs: [(30, 300, '3.3e-02'), (30, 1500, '1.6e-02'), (30, 3000, '4.0e-17'), (30, 4500, '1.8e-03'), (300, 3000, '8.6e-07'), (1500, 3000, '3.1e-05'), (3000, 4500, '6.0e-07')]
awake RSU del_awake KW p=6e-20 n {30: 255, 300: 269, 1500: 303, 3000: 334, 4500: 270} means {30: 106.6, 300: 101.2, 1500: 106.7, 3000: 102.3, 4500: 100.0}
   sig pairs: [(30, 300, '5.1e-10'), (30, 3000, '1.8e-16'), (30, 4500, '2.3e-19'), (300, 1500, '2.9e-02'), (1500, 3000, '5.3e-03'), (1500, 4500, '6.1e-05')]
awake RSU del_awake KW p=6e-20 n {30: 255, 300: 269, 1500: 303, 3000: 334, 4500: 270} means {30: 106.6, 300: 101.2, 1500: 106.7, 3000: 102.3, 4500: 100.0}
   sig pairs: [(30, 300, '5.1e-10'), (30, 3000, '1.8e-16'), (30, 4500, '2.3e-19'), (300, 1500, '2.9e-02'), (1500, 3000, '5.3e-03'), (1500, 4500, '6.1e-05')]
awake FSU tl_w1 KW p=1.8e-12 n {30: 232, 300: 286, 1500: 306, 3000: 319, 4500: 393} means {30: 99.5, 300: 96.7, 1500: 101.8, 3000: 106.8, 4500: 99.5}
   sig pairs: [(30, 3000, '5.7e-07'), (300, 1500, '3.5e-03'), (300, 3000, '2.9e-11'), (1500, 3000, '4.9e-03'), (3000, 4500, '8.1e-08')]
awake FSU tl_w2 KW p=4.8e-11 n {30: 232, 300: 286, 1500: 306, 3000: 319, 4500: 393} means {30: 99.2, 300: 97.3, 1500: 101.7, 3000: 106.4, 4500: 99.6}
   sig pairs: [(30, 3000, '2.1e-07'), (300, 1500, '2.9e-02'), (300, 3000, '2.2e-09'), (1500, 3000, '4.4e-03'), (3000, 4500, '2.2e-07')]
awake FSU del_awake KW p=4.6e-12 n {30: 232, 300: 286, 1500: 306, 3000: 319, 4500: 393} means {30: 103.5, 300: 98.7, 1500: 101.8, 3000: 100.6, 4500: 
[... 52 more lines not kept]
```

**Agent**

Effects are small (normalized rates near 100%). Before reading anything into that, I'll check where in time the stimulus-locked response sits, to confirm `start_time` is the trigger.

**Agent calls Bash**

```bash
cat > $TMPDIR/ex3.py <<'EOF'
import pickle, sys, numpy as np, pandas as pd
sys.path.insert(0,'.')
import tfus
S=pickle.load(open('/tmp/claude-1001/S.pkl','rb'))
dup=tfus.find_duplicates(S); kept=set(dup[dup.kept].path)
t=tfus.FINE_EDGES[:-1]
for cond in [('awake',3000,200),('awake',1500,200),('anesthetized',1500,200),('awake',1500,400),('awake',30,200)]:
  for ct in [1.0,2.0]:
    rows=[]
    for s in S:
        if s['path'] not in kept or (s['state'],s['prf'],s['tbd'])!=cond: continue
        p=s['psth5'][s['label']==ct]; b=p[:, :100].mean(1)
        ok=b>0; rows.append(p[ok]/b[ok,None])
    if not rows: continue
    m=np.concatenate(rows).mean(0)*100
    # 25 ms bins summary
    m25=m.reshape(-1,5).mean(1)
    print(cond, {1.0:'RSU',2.0:'FSU'}[ct], 'n',sum(len(r) for r in rows))
    print('  -0.2..0.5 s by 25ms:', np.round(m25[12:48]).astype(int).tolist())
    print('  0.5..1.5 by 25ms:', np.round(m25[40:80]).astype(int).tolist())
EOF
. $TMPDIR/env/bin/activate && python $TMPDIR/ex3.py
```

```
('awake', 3000, 200) RSU n 334
  -0.2..0.5 s by 25ms: [102, 100, 101, 100, 103, 102, 99, 102, 110, 106, 106, 98, 100, 102, 103, 105, 100, 97, 97, 100, 100, 101, 99, 100, 102, 100, 104, 101, 98, 98, 98, 105, 102, 107, 108, 106]
  0.5..1.5 by 25ms: [98, 98, 98, 105, 102, 107, 108, 106, 105, 103, 106, 102, 100, 104, 102, 99, 103, 99, 103, 100, 103, 100, 104, 98, 105, 104, 103, 102, 103, 104, 102, 100, 99, 101, 103, 102, 102, 101, 98, 97]
('awake', 3000, 200) FSU n 319
  -0.2..0.5 s by 25ms: [102, 100, 98, 101, 102, 100, 101, 100, 106, 107, 107, 102, 102, 99, 99, 101, 99, 98, 97, 99, 100, 102, 99, 101, 99, 101, 102, 101, 101, 99, 101, 100, 101, 103, 102, 102]
  0.5..1.5 by 25ms: [101, 99, 101, 100, 101, 103, 102, 102, 100, 102, 98, 101, 102, 102, 101, 100, 99, 98, 100, 99, 101, 98, 103, 99, 100, 101, 101, 98, 101, 99, 97, 97, 99, 98, 100, 99, 99, 98, 99, 96]
('awake', 1500, 200) RSU n 303
  -0.2..0.5 s by 25ms: [102, 101, 102, 105, 99, 110, 104, 97, 99, 99, 99, 102, 100, 100, 102, 98, 102, 107, 100, 102, 102, 99, 111, 99, 99, 107, 102, 98, 109, 109, 104, 100, 109, 101, 108, 104]
  0.5..1.5 by 25ms: [109, 109, 104, 100, 109, 101, 108, 104, 113, 111, 109, 108, 113, 112, 108, 101, 104, 102, 101, 109, 105, 102, 99, 104, 103, 110, 100, 104, 102, 97, 100, 104, 103, 99, 105, 103, 102, 103, 107, 102]
('awake', 1500, 200) FSU n 306
  -0.2..0.5 s by 25ms: [99, 103, 99, 102, 100, 101, 100, 100, 101, 101, 103, 102, 103, 104, 105, 102, 101, 103, 105, 104, 105, 102, 107, 106, 102, 103, 100, 98, 102, 105, 100, 101, 99, 100, 102, 100]
  0.5..1.5 by 25ms: [102, 105, 100, 101, 99, 100, 102, 100, 104, 104, 103, 103, 103, 102, 102, 101, 102, 99, 100, 105, 100, 101, 102, 102, 104, 105, 99, 98, 99, 98, 100, 100, 102, 99, 99, 99, 103, 98, 101, 99]
('anesthetized', 1500, 200) RSU n 78
  -0.2..0.5 s by 25ms: [102, 101, 101, 100, 98, 99, 101, 99, 107, 109, 103, 101, 100, 100, 99, 99, 99, 101, 100, 99, 99, 101, 99, 100, 99, 100, 99, 101, 101, 99, 100, 99, 102, 102, 100, 100]
  0.5..1.5 by 25ms: [
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/ex4.py <<'EOF'
import pickle, sys, numpy as np, pandas as pd
sys.path.insert(0,'.')
import tfus
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy import stats
pd.set_option('display.width',250); pd.set_option('display.max_rows',300)
U=pd.read_pickle('/tmp/claude-1001/U.pkl')
L=U[U.celltype.notna() & U.base_hz.gt(0)].copy()
S=pickle.load(open('/tmp/claude-1001/S.pkl','rb'))
# ANOVA
P=L[L.tbd==200].copy()
for w in ['W1','W2']:
  for kind in ['tl','del']:
    for ct in ['RSU','FSU']:
      d=P[P.celltype==ct].copy()
      d['y']=[r[('tl_w1' if w=='W1' else 'tl_w2') if kind=='tl' else tfus.delayed_window(r.state,w)] for _,r in d.iterrows()]
      for form in ['y ~ C(state)*C(prf)','y ~ C(state)+C(prf)']:
        a=sm.stats.anova_lm(ols(form,d).fit(),typ=2)
        print(w,kind,ct,form,'state F=%.2f p=%.2g'%(a.loc['C(state)','F'],a.loc['C(state)','PR(>F)']), 'awake mean %.1f anes mean %.1f'%(d[d.state=='awake'].y.mean(), d[d.state=='anesthetized'].y.mean()))
# DC
D=L[(L.state=='awake')&(L.prf==1500)]
print(D.groupby(['tbd','rat']).session.unique())
for ct in ['RSU','FSU']:
  for col in ['tl_w1','tl_w2','del_awake']:
    for c1 in ['C1','C2']:
      rats=set(D[D.tbd!=200].rat)
      d=D if c1=='C2' else D[D.rat.isin(rats)]
      g={dc:d[d.dc==dc][col].values for dc in [6,30,60]}
      o,post=tfus.group_test(g)
      print(ct,col,c1,'KW p=%.2g'%o['p'],o['n'],{k:round(v,1) for k,v in o['mean'].items()},[(r.a,r.b,'%.1e'%r.p_bonf) for r in post.itertuples()])
# fig3 counts
c=U.groupby(['session','rat','state']).celltype.value_counts().unstack(fill_value=0)
c['tot']=c.sum(1); m=c[(c.FSU.sub(28).abs()<=2.8)&(c.RSU.sub(32).abs()<=3.2)&(c.tot.sub(60).abs()<=6)]
print('R1 matches\n',m)
EOF
. $TMPDIR/env/bin/activate && python $TMPDIR/ex4.py 2>&1 | grep -v Warn
```

```
c['tot']=c.sum(1); m=c[(c.FSU.sub(28).abs()<=2.8)&(c.RSU.sub(32).abs()<=3.2)&(c.tot.sub(60).abs()<=6)]
W1 tl RSU y ~ C(state)*C(prf) state F=6.47 p=0.011 awake mean 100.4 anes mean 102.9
W1 tl RSU y ~ C(state)+C(prf) state F=6.40 p=0.011 awake mean 100.4 anes mean 102.9
W1 tl FSU y ~ C(state)*C(prf) state F=0.35 p=0.56 awake mean 100.9 anes mean 101.4
W1 tl FSU y ~ C(state)+C(prf) state F=0.35 p=0.56 awake mean 100.9 anes mean 101.4
W1 del RSU y ~ C(state)*C(prf) state F=21.63 p=3.6e-06 awake mean 103.4 anes mean 99.7
W1 del RSU y ~ C(state)+C(prf) state F=21.52 p=3.8e-06 awake mean 103.4 anes mean 99.7
W1 del FSU y ~ C(state)*C(prf) state F=4.32 p=0.038 awake mean 100.9 anes mean 99.7
W1 del FSU y ~ C(state)+C(prf) state F=4.30 p=0.038 awake mean 100.9 anes mean 99.7
W2 tl RSU y ~ C(state)*C(prf) state F=5.87 p=0.015 awake mean 100.3 anes mean 102.6
W2 tl RSU y ~ C(state)+C(prf) state F=5.82 p=0.016 awake mean 100.3 anes mean 102.6
W2 tl FSU y ~ C(state)*C(prf) state F=0.34 p=0.56 awake mean 100.9 anes mean 101.4
W2 tl FSU y ~ C(state)+C(prf) state F=0.33 p=0.56 awake mean 100.9 anes mean 101.4
W2 del RSU y ~ C(state)*C(prf) state F=21.38 p=4e-06 awake mean 103.4 anes mean 99.7
W2 del RSU y ~ C(state)+C(prf) state F=21.27 p=4.3e-06 awake mean 103.4 anes mean 99.7
W2 del FSU y ~ C(state)*C(prf) state F=4.20 p=0.041 awake mean 100.9 anes mean 99.7
W2 del FSU y ~ C(state)+C(prf) state F=4.18 p=0.041 awake mean 100.9 anes mean 99.7
tbd  rat  
40   BH506                       [BH506_1500_40]
     BH521                       [BH521_1500_40]
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && uv pip install -q jupytext nbconvert ipykernel 2>&1 | tail -1; date -u; ls tools; python tools/entry.py --help 2>&1 | head -30
```

```
Sat Oct 31 21:36:56 UTC 2026
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
[... 38 more lines not kept]
```

**Agent**

The clock reads 21:36, so 4 h of analysis time remain. Writing the notebook in percent format; I'll run it once to get numbers, then write the conclusions.

**Agent calls Write**

```json
{
 "file_path": "entries/000945-ramachandran-2025/reproduce_ramachandran_2025.py",
 "content": "# %% [markdown]\n# # Reproducing Ramachandran et al. (2025) from dandiset 000945\n#\n# **Paper.** Ramachandran S, Gao H, Yttri E, Yu K, He B (2025). Parameter-dependent cell-type\n# specific effects of transcranial focused ultrasound stimulation in an awake head-fixed rodent\n# model. *J Neural Eng* 22(2) 026022.\n# [doi:10.1088/1741-2552/adbb1f](https://doi.org/10.1088/1741-2552/adbb1f). The claims file was\n# written from the version of record as served by Europe PMC (PMC11920894): main text, Methods,\n# figure legends and Discussion; the supplementary materials were not supplied, and no claim rests\n# on them.\n#\n# **Dandiset.** [DANDI:000945](https://dandiarchive.org/dandiset/000945/0.250213.2212), version\n# 0.250213.2212. This is the version the paper cites (reference 50,\n# doi:10.48324/dandi.000945/0.250213.2212). The four later published versions (0.250711.1746,\n# 0.250829.0425, 0.250829.1250) and the draft hold the same 75 files with the same blobs and\n# sizes, as the archive's asset lists show, so the choice does not change the data analysed.\n#\n# **What the dandiset holds.** Sorted units (spike times; a cell-type label in 60 of 75 files) and\n# the trial table of each recording. There are no waveforms, no raw or filtered voltage, no\n# electrode positions and no sham recordings. The condition of each recording is coded only in the\n# file's `identifier` (`<rat>_<PRF>_<TBD>[_2][_anes]`).\n#\n# | Claim | Tested here |\n# |---|---|\n# | fig3-cell-type-sorting | Counts tested with the dataset's labels; the k-means features cannot be computed (no waveforms) |\n# | fig4-rsu-time-locked-both-states | Blocked: the criterion compares with sham, and there is no sham |\n# | fig4hi-fsu-delayed-latency | Tested |\n# | fig4h-awake-latency-wider | Tested |\n# | fig5a-rsu-time-locked-prf-awake | Tested, without the sham parts |\n# | fig5c-rsu-time-locked-prf-anesth | Tested (two labelled rats), without the sham parts |\n# | rsu-time-locked-anesthesia-factor | Tested |\n# | fig5bd-fsu-time-locked-no-prf | Tested |\n# | fig5e-rsu-delayed-prf-awake | Tested, without the sham part |\n# | fig5f-fsu-delayed-prf-awake | Tested, without the sham part |\n# | fig5gh-delayed-prf-anesth | Tested |\n# | delayed-anesthesia-factor | Tested |\n# | fig6ad-time-adjacent-batch | Blocked: the second batch of five rats is not in the dandiset |\n# | fig6ef-rsu-ispta-rise-then-fall | Tested |\n# | fig6fh-fsu-ispta | Tested |\n# | fig5a-1500-highest-time-locked-mean | Tested |\n# | fig7a-rsu-time-locked-dc | Tested, without the sham part |\n# | fig7a-60-highest-time-locked-mean | Tested |\n# | fig7b-fsu-time-locked-dc | Tested |\n# | fig7c-rsu-delayed-dc | Tested, without the sham part |\n# | fig7d-fsu-delayed-dc | Tested, without the sham part |\n# | sham-no-auditory-response | Blocked: no sham recordings, and no test named |\n\n# %%\nimport time\nimport warnings\n\nimport h5py\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nimport remfile\nimport statsmodels.api as sm\nfrom scipy import stats\nfrom statsmodels.formula.api import ols\n\nimport tfus\n\npd.set_option(\"display.width\", 220)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 300)\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nstarted = time.time()\nassets = tfus.asset_list()\nsessions = tfus.load_all(assets)\nprint(f\"loaded {len(sessions)} files from dandiset {tfus.DANDISET_ID} version {tfus.DANDISET_VERSION} \"\n      f\"in {time.time() - started:.0f} s\")\n\n# %% [markdown]\n# ## Data check\n#\n# Each check of the metadata against the values is stated under its output.\n\n# %% tags=[\"sanity\"]\ninv = pd.DataFrame([{\n    \"path\": s[\"path\"], \"subject_id\": s[\"subject_id\"], \"identifier\": s[\"identifier\"], \"rat\": s[\"rat\"],\n    \"state\": s[\"state\"], \"prf\": s[\"prf\"], \"tbd\": s[\"tbd\"], \"repeat\": s[\"repeat\"],\n    \"description\": s[\"session_description\"], \"age\": s[\"age\"], \"start\": s[\"session_start\"][:16],\n    \"units\": s[\"n_units\"], \"labelled\": int((~np.isnan(s[\"label\"])).sum()), \"trials\": s[\"n_trials\"],\n    \"units_cols\": \" \".join(s[\"units_colnames\"]), \"trial_cols\": \" \".join(s[\"trials_colnames\"]),\n    \"acq_proc\": \" \".join(s[\"acquisition\"] + s[\"processing\"]) or \"-\"} for s in sessions])\nprint(\"Files:\", len(inv), \"; subject folders:\", inv.subject_id.nunique(), sorted(inv.subject_id.unique()))\nprint(\"Rats named in identifiers:\", sorted(inv.rat.unique()))\nprint(\"Files whose subject_id differs from the rat in the identifier:\")\nprint(inv[inv.subject_id != inv.rat][[\"path\", \"identifier\"]].to_string(index=False))\nprint(\"\\nUnits table columns:\", inv.units_cols.value_counts().to_dict())\nprint(\"Trials table columns:\", inv.trial_cols.value_counts().to_dict())\nprint(\"Acquisition or processing modules:\", inv.acq_proc.value_counts().to_dict())\nprint(\"Ages:\", inv.age.value_counts().to_dict())\nprint(\"Session descriptions by state in the identifier:\")\nprint(pd.crosstab(inv.description, inv.state).to_string())\nprint(\"\\nTrials per file:\", inv.trials.value_counts().to_dict())\nprint(inv[inv.trials != 500][[\"identifier\", \"trials\"]].to_string(index=False))\nprint(\"\\nLabels: files with celltype_label\", int((inv.labelled > 0).sum()), \"of\", len(inv),\n      \"; units in files without it:\", int(inv[inv.labelled == 0].units.sum()))\nprint(\"Every identifier parses as <rat>_<PRF>_<TBD>[_2][_anes|_anes2]: True (parse_identifier raised no error)\")\n\n# %% [markdown]\n# There are no waveforms, voltage traces, electrode positions or processing modules: units hold\n# only spike times and, in 60 files, a label (\"1 = RSU, 2 = FSU\"). Every file says age P24W (about\n# 5.5 months), where the Methods give 7, 9 and 10 months for the three series. The 15 files without\n# labels are all anesthetized recordings, and they are the only files whose description says\n# \"Awake Model Anes\"; the labelled anesthetized copies (subject folders BH497 and BH514) are\n# described as \"Awake S1 Stimulation\". The identifiers of those copies name rats BH498 and BH512.\n# Five files hold fewer than the 500 trials the Methods describe.\n\n# %% tags=[\"sanity\"]\ndup = tfus.find_duplicates(sessions)\nprint(\"Groups of files with identical trial times:\")\nprint(dup[dup.group_size > 1].sort_values([\"duplicate_of\", \"path\"], na_position=\"first\")\n      [[\"path\", \"identifier\", \"kept\", \"duplicate_of\"]].to_string(index=False))\nby_path = {s[\"path\"]: s for s in sessions}\nrows = []\nfor r in dup[~dup.kept].itertuples():\n    a, b = by_path[r.path], by_path[r.duplicate_of]\n    same_counts = a[\"n_units\"] == b[\"n_units\"] and np.array_equal(a[\"n_spikes\"], b[\"n_spikes\"])\n    same_first = np.array_equal(a[\"first_spikes\"], b[\"first_spikes\"])\n    rows.append({\"file\": r.identifier + \" (\" + r.subject_id + \")\", \"kept\": b[\"identifier\"] + \" (\" + b[\"subject_id\"] + \")\",\n                 \"units\": f'{a[\"n_units\"]}/{b[\"n_units\"]}', \"spikes\": f'{a[\"n_spikes\"].sum()}/{b[\"n_spikes\"].sum()}',\n                 \"same spike count per unit\": same_counts, \"same first 5000 spike times\": same_first})\nprint(pd.DataFrame(rows).to_string(index=False))\n\n\ndef shared_spikes(p1, p2):\n    out = []\n    for p in (p1, p2):\n        url = next(a[\"url\"] for a in assets if a[\"path\"] == p)\n        with h5py.File(remfile.File(url), \"r\") as f:\n            out.append(np.unique(np.round(f[\"units/spike_times\"][:], 5)))\n    return len(out[0]), len(out[1]), len(np.intersect1d(out[0], out[1]))\n\n\nn1, n2, n12 = shared_spikes(\"sub-BH498/sub-BH498_ses-20240306T175805_ecephys.nwb\",\n                            \"sub-BH508/sub-BH508_ses-20240307T002354_ecephys.nwb\")\nprint(f\"\\nBH498_30_200 and BH508_30_200_2: distinct spike times {n1} and {n2}, shared to 10 us: {n12}\")\nkept_paths = set(dup[dup.kept].path)\nkept = [s for s in sessions if s[\"path\"] in kept_paths]\nprint(\"Recordings counted once:\", len(kept), \"of\", len(sessions), \"files\")\n\n# %% [markdown]\n# Twelve files are second copies. The five anesthetized BH498 recordings are each deposited twice,\n# under BH498 without labels and under BH497 with labels; the BH512 anesthetized recordings at\n# 300, 1500, 3000 and 4500 Hz are deposited under BH512 without labels and under BH514 with labels,\n# and `BH512_1500_200_anes2` is a third copy of the 1500 Hz recording with the same trial times and\n# a different sort (21,329 fewer spikes). In each pair the trial times, the number of spikes of\n# every unit and the first spike times are identical. The labelled copy is kept, and the rat is\n# taken from the identifier (BH498, BH512), which the unlabelled copies' subject folders confirm.\n# `BH498_30_200` and `BH508_30_200_2` are filed under two rats but share all 203 trial times and\n# 18,860 spike times; they are one recording sorted twice, and only `BH498_30_200` is kept (the\n# other is a `_2` repeat). 63 recordings remain.\n\n# %% tags=[\"sanity\"]\nunits = tfus.unit_table(kept)\ncond = units.groupby([\"state\", \"prf\", \"tbd\", \"repeat\", \"rat\"]).session.first().reset_index()\nprint(\"Recordings kept, by state, PRF, TBD and rat (x = one recording; R = a `_2` repeat):\")\ncond[\"mark\"] = np.where(cond.repeat, \"R\", \"x\")\nprint(cond.pivot_table(index=[\"state\", \"prf\", \"tbd\"], columns=\"rat\", values=\"mark\",\n                       aggfunc=lambda v: \"+\".join(sorted(v))).fillna(\"\").to_string())\niti = np.concatenate([np.diff(s[\"trial_times\"]) for s in kept])\ntl = np.concatenate([s[\"trial_len\"] for s in kept])\nprint(f\"\\nInter-trial interval: {iti.min():.3f} to {iti.max():.3f} s, median {np.median(iti):.3f} \"\n      f\"(Methods: 2.5 s with 10% jitter); {int((iti > 2.75).sum())} intervals above 2.75 s\")\nprint(f\"stop_time - start_time: {tl.min():.3f} to {tl.max():.3f} s\")\ncover = [(s[\"identifier\"], s[\"trial_times\"][0], s[\"trial_times\"][-1], *s[\"spike_range\"]) for s in kept]\nbad = [c for c in cover if c[1] - 0.5 < c[3] - 1 or c[2] + 1.5 > c[4] + 1]\nprint(\"Recordings whose spikes do not span the trials from -0.5 to +1.5 s (1 s slack):\", bad or \"none\")\nprint(\"Spike times sorted within every unit:\", all(s[\"spikes_sorted\"] for s in kept))\n\n# %% [markdown]\n# The dandiset holds the awake PRF series of seven rats (BH498, BH506, BH508, BH512, BH519, BH526,\n# BH527), ten `_2` repeats of awake PRF conditions in BH498, BH506 and BH508, the awake 6% and 60%\n# DC conditions (TBD 40 and 400 us) of three rats (BH506, BH521, BH526), anesthetized PRF series\n# for BH498 (all five PRFs), BH512 (no 30 Hz) and BH521 (300, 3000 and 4500 Hz, unlabelled), and\n# anesthetized 6% and 60% DC recordings of BH512 (unlabelled). The paper describes ten rats in the\n# first batch, five more in a second batch with a sham condition, and a DC series with its own 30%\n# recordings at 10 months; none of the second batch, no sham and no separate 30% DC recording are\n# here. Intervals between trials fit the Methods' 2.5 s with 10% jitter, apart from one long gap.\n# The trial table's `stop_time` is always 2.2 s after `start_time`; the Methods give no 2.2 s\n# period, and `start_time` is taken as the trigger, which the next check supports.\n\n# %% tags=[\"sanity\"]\nlab_units = units[units.celltype.notna()]\nprint(\"Units in kept recordings:\", len(units), \"; labelled:\", len(lab_units),\n      \"; unlabelled (BH512 DC and BH521 anesthetized):\", int(units.celltype.isna().sum()))\nprint(\"Units with no baseline spike (left out):\", int((lab_units.base_hz == 0).sum()))\nprint(\"\\nBaseline rate (Hz) by label, over units: median, IQR\")\nprint(lab_units.groupby(\"celltype\").base_hz.describe(percentiles=[.25, .5, .75])[[\"count\", \"25%\", \"50%\", \"75%\", \"max\"]].round(2).to_string())\nper_ses = lab_units.groupby([\"session\", \"celltype\"]).base_hz.median().unstack()\nprint(f\"Recordings where the FSU median rate exceeds the RSU median: {(per_ses.FSU > per_ses.RSU).sum()} of {len(per_ses.dropna())}\")\nprint(\"\\nLabelled units per state and type (kept recordings):\")\nprint(pd.crosstab([lab_units.state, lab_units.tbd], lab_units.celltype).to_string())\n\n# %% [markdown]\n# The labels split the units about evenly. FSU, the putative fast-spiking interneurons, are\n# expected to fire faster; the comparison of baseline rates above says whether the labels follow\n# that (it is a consistency check, not a test of the labels).\n\n# %% tags=[\"sanity\"]\n# Clock check: the population spike count of each recording in 0-67 ms after each trial start\n# against the 0.5 s before it, at the true trial times and 1.25 s later (mid-interval).\nrows = []\nfor s in kept:\n    c = s[\"counts\"].sum(axis=0)        # trials x windows, summed over units\n    i = {k: tfus.window_index(k) for k in (\"base\", \"tl_w1\", \"shift_base\", \"shift_tl\")}\n    true = c[:, i[\"tl_w1\"]] / 0.067 - c[:, i[\"base\"]] / 0.5\n    shift = c[:, i[\"shift_tl\"]] / 0.067 - c[:, i[\"shift_base\"]] / 0.5\n    rows.append({\"session\": s[\"identifier\"], \"state\": s[\"state\"], \"prf\": s[\"prf\"], \"tbd\": s[\"tbd\"],\n                 \"t_true\": stats.ttest_1samp(true, 0).statistic, \"t_shifted\": stats.ttest_1samp(shift, 0).statistic})\nclock = pd.DataFrame(rows)\nprint(clock.round(2).sort_values([\"state\", \"tbd\", \"prf\"]).to_string(index=False))\nprint(f\"\\nRecordings with t > 3 at the true times: {(clock.t_true > 3).sum()} of {len(clock)}; \"\n      f\"at shifted times: {(clock.t_shifted > 3).sum()}\")\nprint(f\"Median t: true {clock.t_true.median():.2f}, shifted {clock.t_shifted.median():.2f}\")\n\nfig, axes = plt.subplots(1, 3, figsize=(13, 3.2), sharey=True)\nt = tfus.FINE_EDGES[:-1] + tfus.FINE / 2\nfor ax, (st, prf, tbd) in zip(axes, [(\"awake\", 1500, 400), (\"awake\", 3000, 200), (\"anesthetized\", 1500, 200)]):\n    for code, name in [(1.0, \"RSU\"), (2.0, \"FSU\")]:\n        prof = []\n        for s in kept:\n            if (s[\"state\"], s[\"prf\"], s[\"tbd\"]) != (st, prf, tbd):\n                continue\n            p = s[\"psth5\"][s[\"label\"] == code]\n            b = p[:, :100].mean(1)\n            prof.append(p[b > 0] / b[b > 0, None])\n        m = 100 * np.concatenate(prof).mean(0)\n        ax.plot(t, m, label=f\"{name} (n={len(np.concatenate(prof))}, range {m.min():.0f}-{m.max():.0f}%)\")\n    ax.axvspan(0, 0.067, color=\"0.85\")\n    ax.set_title(f\"{st} {prf} Hz, TBD {tbd} us\")\n    ax.set_xlabel(\"time from trial start (s)\")\n    ax.legend(fontsize=7)\naxes[0].set_ylabel(\"rate, % of baseline (5 ms bins)\")\nplt.tight_layout()\nplt.show()\n\n# %% [markdown]\n# Where a recording responds at all, the response begins in the first 5 ms bins after\n# `start_time` and lasts about 75 ms, the 67 ms ultrasound duration, and the same contrast 1.25 s\n# later is near zero. So `start_time` is the trigger and spikes and trials share a clock in those\n# recordings. In recordings with no time-locked response the check cannot tell; the table names\n# them (t at true times below 3).\n\n# %% [markdown]\n# ## Readings and selections used in every claim\n#\n# The claims file's header fixes the method; the dataset decides which of its readings can run.\n#\n# - **Cell type.** K0: the dataset carries labels, so they are used. K1 and K2 (k-means on the\n#   initial and after-hyperpolarization phase durations) cannot run: the files hold no waveforms.\n# - **Trials.** The files hold 500 trials, the 505 delivered less the first five (T1, Methods 2.4);\n#   T2 (all 505) cannot run. Five recordings hold 203 to 339 trials and are used as they are.\n# - **Exclusion.** E1 = E2: the dataset marks no excluded unit or interval.\n# - **Windows.** W1 (exact window) and W2 (overlapping PSTH bins) are both run.\n# - **Groups.** G1 only: there are no sham recordings, so G2 cannot run.\n# - **Repeats** (not named by the claims file; the dandiset adds them). The `_2` recordings repeat\n#   a condition in the same rat. The Methods describe one recording per parameter set per rat\n#   (\"Recordings for a single rat for each set of parameters were completed on the same day\",\n#   Methods 2.3) and count \"the total number of neurons in each group\" (Methods 2.6). Rep1 counts\n#   every recording once, repeats included; Rep2 leaves the repeats out. Both are run.\n# - **Anesthetized data.** Only two rats' anesthetized recordings carry labels (BH498 at all five\n#   PRFs, BH512 without 30 Hz); BH521's three are unlabelled and cannot enter a cell-type test.\n\n# %%\nL = units[units.celltype.notna() & (units.base_hz > 0)].copy()\nPRFS = [30, 300, 1500, 3000, 4500]\nREADINGS = [(w, r) for w in (\"W1\", \"W2\") for r in (\"Rep1\", \"Rep2\")]\n\n\ndef col(kind, state, w):\n    if kind == \"tl\":\n        return \"tl_w1\" if w == \"W1\" else \"tl_w2\"\n    return tfus.delayed_window(state, w)\n\n\ndef select(state, ct, rep, tbd=200, prf=None):\n    d = L[(L.state == state) & (L.celltype == ct) & (L.tbd == tbd)]\n    if prf is not None:\n        d = d[d.prf == prf]\n    if rep == \"Rep2\":\n        d = d[~d.repeat]\n    return d\n\n\ndef prf_test(state, ct, kind, w, rep):\n    d = select(state, ct, rep)\n    c = col(kind, state, w)\n    return tfus.group_test({p: d[d.prf == p][c].values for p in PRFS})\n\n\ndef sig(post, a, b):\n    return bool(tfus.pair(post, a, b).p_bonf < 0.05)\n\n\ndef lower(post, a, b):\n    \"\"\"a significantly below b.\"\"\"\n    r = tfus.pair(post, a, b)\n    return bool(r.p_bonf < 0.05 and r.mean_a < r.mean_b)\n\n\ndef show(o, post, label):\n    print(f\"{label}: Kruskal-Wallis H = {o['H']:.1f}, p = {o['p']:.2g}; n = {o['n']}\")\n    print(\"  means:\", {k: round(v, 1) for k, v in o[\"mean\"].items()},\n          \" medians:\", {k: round(v, 1) for k, v in o[\"median\"].items()})\n    print(post[[\"a\", \"b\", \"mean_a\", \"mean_b\", \"p\", \"p_bonf\", \"sig\"]].round(4).to_string(index=False))\n\n\ndef by_rat(state, ct, kind, w, rep, tbd=200):\n    d = select(state, ct, rep, tbd=tbd)\n    c = col(kind, state, w)\n    return d.pivot_table(index=\"rat\", columns=\"prf\" if tbd == 200 else \"dc\", values=c, aggfunc=\"mean\").round(1)\n\n\nprint(\"Labelled units with a baseline, by state and type:\", L.groupby([\"state\", \"celltype\"]).size().to_dict())\n\n# %% [markdown]\n# ## fig3-cell-type-sorting\n#\n# > Units are sorted into fast spiking units (FSU) and regular spiking units (RSU) by k-means\n# > clustering of the initial phase and after-hyperpolarization phase durations of their action\n# > potentials; in one animal's recordings this gave 28 FSU and 32 RSU, 60 in total.\n\n# %% tags=[\"claim:fig3-cell-type-sorting\"]\ncnt = units[units.celltype.notna()].groupby([\"rat\", \"session\", \"state\"]).celltype.value_counts().unstack(fill_value=0)\ncnt[\"total\"] = cnt.sum(axis=1)\nok = lambda c: (abs(c.FSU - 28) <= 2.8) & (abs(c.RSU - 32) <= 3.2) & (abs(c.total - 60) <= 6)\nprint(\"R1, one recording: recordings with all three counts in tolerance (FSU 28 +- 2.8, RSU 32 +- 3.2, total 60 +- 6)\")\nprint(cnt[ok(cnt)].to_string())\nprint(f\"({len(cnt)} labelled recordings; totals range {cnt.total.min()} to {cnt.total.max()}, FSU share \"\n      f\"{(cnt.FSU / cnt.total).min():.2f} to {(cnt.FSU / cnt.total).max():.2f})\")\nlu = units[units.celltype.notna()].copy()\nlu[\"series\"] = np.where(lu.tbd == 200, lu.state + \" PRF\", lu.state + \" DC\")\ncnt2 = lu.groupby([\"rat\", \"series\"]).celltype.value_counts().unstack(fill_value=0)\ncnt2[\"total\"] = cnt2.sum(axis=1)\nprint(\"\\nR2, all of one rat's recordings in one series:\")\nprint(cnt2.to_string())\nprint(\"R2 matches:\", cnt2[ok(cnt2)].index.tolist() or \"none\")\nprint(\"\\nThe clusters' separation on the initial phase and after-hyperpolarization durations cannot be \"\n      \"computed: the files hold no waveforms (units columns:\", sorted(set(inv.units_cols)), \")\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig4-rsu-time-locked-both-states (blocked)\n#\n# > RSUs show time-locked responses to tFUS, an increase in firing rate during the 67 ms of\n# > stimulation, in both awake and anesthetized recordings.\n#\n# The criterion compares the 1500 Hz, 200 us RSU responses with the sham sessions of each state.\n# The dandiset holds no sham recording, so the claim is blocked. The responses the criterion would\n# have compared are shown, without a test.\n\n# %% tags=[\"claim:fig4-rsu-time-locked-both-states\"]\nfor st in (\"awake\", \"anesthetized\"):\n    for w in (\"W1\", \"W2\"):\n        for rep in (\"Rep1\", \"Rep2\"):\n            d = select(st, \"RSU\", rep, prf=1500)[col(\"tl\", st, w)]\n            print(f\"{st:12s} {w} {rep}: RSU at 1500 Hz, n = {len(d)}, mean {d.mean():.1f}%, median {d.median():.1f}%, \"\n                  f\"units above 100%: {(d > 100).sum()}\")\n\n# %% [markdown]\n# ## fig4hi-fsu-delayed-latency\n#\n# > FSU delayed responses to tFUS at 1500 Hz PRF begin later in awake rats (mean onset 0.51 s,\n# > spread 0.14 s) than under anesthesia (0.24 s, spread 0.08 s), and the onset distributions\n# > differ significantly by a Wilcoxon rank-sum test.\n#\n# Sessions: FSU of the 1500 Hz, 200 us recordings. Q1 and Q2 select the same recordings here: the\n# awake 30% DC condition has no recording of its own (it is the 1500 Hz, 200 us recording), and\n# batch 2 is not in the dandiset. Every combination of S1/S2, D1/D2, L1/L2 and Rep1/Rep2 is run.\n\n# %% tags=[\"claim:fig4hi-fsu-delayed-latency\"]\nlat_rows = []\nfor s in kept:\n    if s[\"prf\"] != 1500 or s[\"tbd\"] != 200:\n        continue\n    for u in range(s[\"n_units\"]):\n        if s[\"label\"][u] != 2.0:\n            continue\n        r = {\"session\": s[\"identifier\"], \"rat\": s[\"rat\"], \"state\": s[\"state\"], \"repeat\": s[\"repeat\"]}\n        for sem in (\"S1\", \"S2\"):\n            for first in (\"D1\", \"D2\"):\n                for timing in (\"L1\", \"L2\"):\n                    r[f\"{sem}{first}{timing}\"] = tfus.latency(s[\"psth\"][u], s[\"counts\"][u, :, 0], sem, first, timing)\n        lat_rows.append(r)\nlat = pd.DataFrame(lat_rows)\ncombos = [c for c in lat.columns if c.startswith(\"S\")]\nres = []\nfor c in combos:\n    for rep in (\"Rep1\", \"Rep2\"):\n        d = lat if rep == \"Rep1\" else lat[~lat.repeat]\n        aw, an = d[d.state == \"awake\"][c].dropna(), d[d.state == \"anesthetized\"][c].dropna()\n        n_aw, n_an = (d.state == \"awake\").sum(), (d.state == \"anesthetized\").sum()\n        p = stats.ranksums(aw, an).pvalue\n        res.append({\"reading\": c + \" \" + rep, \"awake n\": f\"{len(aw)}/{n_aw}\", \"anes n\": f\"{len(an)}/{n_an}\",\n                    \"awake mean\": aw.mean(), \"awake SD\": aw.std(), \"anes mean\": an.mean(), \"anes SD\": an.std(),\n                    \"p\": p, \"anes in tol\": abs(an.mean() - 0.24) <= 0.08, \"awake in tol\": abs(aw.mean() - 0.51) <= 0.14,\n                    \"awake later, p<0.001\": bool(p < 0.001 and aw.median() > an.median())})\nlat_res = pd.DataFrame(res)\nprint(\"FSU at 1500 Hz, 200 us; n = units with a significant delayed response / FSU\")\nprint(lat_res.round(4).to_string(index=False))\nmain = lat[lat.state == \"awake\"]\nprint(\"\\nBy rat, S1D1L1 Rep1: units with a delayed response and their mean latency (s)\")\nprint(lat.groupby([\"state\", \"rat\"]).S1D1L1.agg([\"size\", \"count\", \"mean\"]).round(3).to_string())\nfor st in (\"awake\", \"anesthetized\"):\n    d = lat[lat.state == st]\n    v = d.S1D1L1.dropna()\n    print(f\"{st}: latencies range {v.min():.3f} to {v.max():.3f} s; first allowed bin (D1) holds {np.mean(v < 0.08):.2f} of them\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig4h-awake-latency-wider\n#\n# > Awake FSU delayed-response onset latencies have a wider spread than anesthetized ones and appear\n# > to have two peaks.\n\n# %% tags=[\"claim:fig4h-awake-latency-wider\"]\nprint(lat_res[[\"reading\", \"awake SD\", \"anes SD\"]].assign(wider=lambda d: d[\"awake SD\"] > d[\"anes SD\"]).round(3).to_string(index=False))\nfig, ax = plt.subplots(figsize=(6, 3))\nbins = tfus.EDGES[tfus.N_BASE_BINS:]\nfor st in (\"anesthetized\", \"awake\"):\n    v = lat[lat.state == st].S1D1L1.dropna()\n    h, _ = np.histogram(v, bins)\n    peaks = [round(bins[i], 3) for i in range(len(h)) if h[i] > 0 and (i == 0 or h[i] > h[i - 1]) and (i == len(h) - 1 or h[i] >= h[i + 1])]\n    print(f\"{st}: histogram (35.7 ms bins from 0 s) counts {h.tolist()}; local maxima at {peaks} s\")\n    ax.hist(v, bins, alpha=0.6, label=f\"{st} (n={len(v)}, {v.min():.2f}-{v.max():.2f} s)\")\nax.set_xlabel(\"onset latency (s), S1 D1 L1 Rep1\")\nax.set_ylabel(\"FSU\")\nax.legend(fontsize=8)\nplt.show()\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig5a-rsu-time-locked-prf-awake\n#\n# > In awake rats PRF is a significant factor for RSU time-locked responses; 30 Hz and 300 Hz PRF\n# > give lower responses than every higher PRF (so 30 Hz is also below 300 Hz), 1500, 3000 and\n# > 4500 Hz do not differ, and sham differs from every PRF but 30 Hz.\n#\n# Parts (5) and (6) compare with sham and cannot be tested; the claim is judged on parts (1) to (4).\n\n# %% tags=[\"claim:fig5a-rsu-time-locked-prf-awake\"]\nrows = []\nfor w, rep in READINGS:\n    o, post = prf_test(\"awake\", \"RSU\", \"tl\", w, rep)\n    if (w, rep) == (\"W1\", \"Rep1\"):\n        show(o, post, \"awake RSU 0-67 ms, W1 Rep1\")\n    rows.append({\"reading\": f\"{w} {rep}\", \"(1) KW\": o[\"p\"] < 0.05,\n                 \"(2) 30 below each\": all(lower(post, 30, b) for b in (300, 1500, 3000, 4500)),\n                 \"(3) 300 below each\": all(lower(post, 300, b) for b in (1500, 3000, 4500)),\n                 \"(4) no pair of 1500/3000/4500\": not any(sig(post, a, b) for a, b in ((1500, 3000), (1500, 4500), (3000, 4500))),\n                 \"highest mean\": max(o[\"mean\"], key=o[\"mean\"].get)})\nprint(pd.DataFrame(rows).to_string(index=False))\nprint(\"\\nMean response by rat (W1 Rep1):\")\nprint(by_rat(\"awake\", \"RSU\", \"tl\", \"W1\", \"Rep1\").to_string())\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig5c-rsu-time-locked-prf-anesth\n#\n# > Under anesthesia RSU time-locked responses depend on PRF as in the awake model, the only\n# > difference being that 30 Hz and 300 Hz do not differ significantly.\n#\n# Two labelled rats: BH498 (all five PRFs) and BH512 (no 30 Hz). The repeats reading does not apply\n# (no anesthetized repeats remain). Parts (5) and (6) compare with sham and cannot be tested.\n\n# %% tags=[\"claim:fig5c-rsu-time-locked-prf-anesth\"]\nrows = []\nfor w in (\"W1\", \"W2\"):\n    o, post = prf_test(\"anesthetized\", \"RSU\", \"tl\", w, \"Rep1\")\n    show(o, post, f\"anesthetized RSU 0-67 ms, {w}\")\n    rows.append({\"reading\": w, \"(1) KW\": o[\"p\"] < 0.05,\n                 \"(2) 30 below 1500/3000/4500\": all(lower(post, 30, b) for b in (1500, 3000, 4500)),\n                 \"(3) 300 below each\": all(lower(post, 300, b) for b in (1500, 3000, 4500)),\n                 \"(4) no pair of 1500/3000/4500\": not any(sig(post, a, b) for a, b in ((1500, 3000), (1500, 4500), (3000, 4500))),\n                 \"(7) 30 = 300\": not sig(post, 30, 300)})\nprint(pd.DataFrame(rows).to_string(index=False))\nprint(\"\\nMean response by rat (W1):\")\nprint(by_rat(\"anesthetized\", \"RSU\", \"tl\", \"W1\", \"Rep1\").to_string())\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## rsu-time-locked-anesthesia-factor\n#\n# > Anesthesia is a significant factor in the RSU time-locked response by two-way ANOVA, and it\n# > lowers the average magnitude of RSU responses.\n\n# %%\ndef anova(ct, kind, w, rep, model):\n    d = pd.concat([select(st, ct, rep) for st in (\"awake\", \"anesthetized\")])\n    d = d.assign(y=[r[col(kind, r.state, w)] for _, r in d.iterrows()])\n    form = \"y ~ C(state) * C(prf)\" if model == \"A1\" else \"y ~ C(state) + C(prf)\"\n    a = sm.stats.anova_lm(ols(form, d).fit(), typ=2)\n    return {\"reading\": f\"{model} {w} {rep}\", \"n\": len(d), \"F state\": a.loc[\"C(state)\", \"F\"], \"p state\": a.loc[\"C(state)\", \"PR(>F)\"],\n            \"awake mean\": d[d.state == \"awake\"].y.mean(), \"anes mean\": d[d.state == \"anesthetized\"].y.mean()}\n\n\ndef anova_table(ct, kind):\n    return pd.DataFrame([anova(ct, kind, w, rep, m) for m in (\"A1\", \"A2\") for w, rep in READINGS])\n\n\n# %% tags=[\"claim:rsu-time-locked-anesthesia-factor\"]\nt_rsu = anova_table(\"RSU\", \"tl\")\nprint(t_rsu.round(4).to_string(index=False))\nprint(\"\\nPer-PRF means (W1 Rep1):\")\nprint(pd.concat({st: select(st, \"RSU\", \"Rep1\").groupby(\"prf\").tl_w1.mean() for st in (\"awake\", \"anesthetized\")}, axis=1).round(1).to_string())\nprint(\"\\nVariant, the two rats with labelled anesthetized data only (BH498, BH512), W1 Rep1, A1:\")\nd = pd.concat([select(st, \"RSU\", \"Rep1\") for st in (\"awake\", \"anesthetized\")])\nd = d[d.rat.isin([\"BH498\", \"BH512\"])].assign(y=lambda x: x.tl_w1)\na = sm.stats.anova_lm(ols(\"y ~ C(state) * C(prf)\", d).fit(), typ=2)\nprint(f\"  F = {a.loc['C(state)', 'F']:.2f}, p = {a.loc['C(state)', 'PR(>F)']:.3g}; awake mean {d[d.state == 'awake'].y.mean():.1f}, \"\n      f\"anesthetized {d[d.state == 'anesthetized'].y.mean():.1f}\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig5bd-fsu-time-locked-no-prf\n#\n# > FSU time-locked responses show no significant differences across PRF levels, in either the\n# > awake or the anesthetized model.\n#\n# A claim of absence, judged on the Kruskal-Wallis across the five PRFs (G1) at 0.05 and the post\n# hoc tests at Bonferroni-corrected 0.05.\n\n# %% tags=[\"claim:fig5bd-fsu-time-locked-no-prf\"]\nrows = []\nfor st in (\"awake\", \"anesthetized\"):\n    for w, rep in READINGS:\n        if st == \"anesthetized\" and rep == \"Rep2\":\n            continue\n        o, post = prf_test(st, \"FSU\", \"tl\", w, rep)\n        if w == \"W1\" and rep == \"Rep1\":\n            show(o, post, f\"{st} FSU 0-67 ms, W1 Rep1\")\n        med = o[\"median\"]\n        rows.append({\"state\": st, \"reading\": f\"{w} {rep}\", \"KW p\": o[\"p\"], \"post hoc pairs significant\": int(post.sig.sum()),\n                     \"median range\": f\"{min(med.values()):.1f}-{max(med.values()):.1f}\",\n                     \"mean range\": f\"{min(o['mean'].values()):.1f}-{max(o['mean'].values()):.1f}\"})\nprint(pd.DataFrame(rows).round(6).to_string(index=False))\nprint(\"\\nMean response by rat, awake (W1 Rep1):\")\nprint(by_rat(\"awake\", \"FSU\", \"tl\", \"W1\", \"Rep1\").to_string())\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig5e-rsu-delayed-prf-awake\n#\n# > Awake RSU delayed responses (0.5 to 1 s) depend on PRF, are highest at 1500 Hz and 3000 Hz with\n# > lower responses at both lower and higher PRFs, and every PRF is significantly higher than sham.\n#\n# Part (3) compares with sham and cannot be tested. The 0.5 to 1 s window is on bin edges, so W1\n# and W2 are the same.\n\n# %% tags=[\"claim:fig5e-rsu-delayed-prf-awake\"]\nrows = []\nfor rep in (\"Rep1\", \"Rep2\"):\n    o, post = prf_test(\"awake\", \"RSU\", \"del\", \"W1\", rep)\n    show(o, post, f\"awake RSU 0.5-1 s, {rep}\")\n    m = o[\"mean\"]\n    top2 = sorted(m, key=m.get)[-2:]\n    rows.append({\"reading\": rep, \"(1) KW\": o[\"p\"] < 0.05,\n                 \"(2) R1: 1500 and 3000 above 30, 300, 4500\": all(lower(post, a, b) for b in (1500, 3000) for a in (30, 300, 4500)),\n                 \"(2) R2: top two means are 1500 and 3000\": sorted(top2) == [1500, 3000],\n                 \"(2) R2: both above 30 and 4500\": all(lower(post, a, b) for b in (1500, 3000) for a in (30, 4500))})\nprint(pd.DataFrame(rows).to_string(index=False))\nprint(\"\\nMean response by rat (Rep1):\")\nprint(by_rat(\"awake\", \"RSU\", \"del\", \"W1\", \"Rep1\").to_string())\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig5f-fsu-delayed-prf-awake\n#\n# > Awake FSU delayed responses depend on PRF, are strongest at 4500 Hz, differ between 30 Hz and\n# > the three highest PRFs and between 300 Hz and the two highest, and at 30 Hz and 300 Hz are not\n# > significantly higher than sham.\n#\n# Part (5) compares with sham and cannot be tested.\n\n# %% tags=[\"claim:fig5f-fsu-delayed-prf-awake\"]\nrows = []\nfor rep in (\"Rep1\", \"Rep2\"):\n    o, post = prf_test(\"awake\", \"FSU\", \"del\", \"W1\", rep)\n    show(o, post, f\"awake FSU 0.5-1 s, {rep}\")\n    rows.append({\"reading\": rep, \"(1) KW\": o[\"p\"] < 0.05, \"(2) 4500 highest\": max(o[\"mean\"], key=o[\"mean\"].get) == 4500,\n                 \"(3) 30 differs from 1500/3000/4500\": all(sig(post, 30, b) for b in (1500, 3000, 4500)),\n                 \"(4) 300 differs from 3000/4500\": all(sig(post, 300, b) for b in (3000, 4500))})\nprint(pd.DataFrame(rows).to_string(index=False))\nprint(\"\\nMean response by rat (Rep1):\")\nprint(by_rat(\"awake\", \"FSU\", \"del\", \"W1\", \"Rep1\").to_string())\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig5gh-delayed-prf-anesth\n#\n# > Under anesthesia PRF is a significant factor for the delayed responses (0.2 to 0.7 s) of both\n# > RSUs and FSUs, which broadly prefer higher PRFs.\n\n# %% tags=[\"claim:fig5gh-delayed-prf-anesth\"]\nrows = []\nfor ct in (\"RSU\", \"FSU\"):\n    for w in (\"W1\", \"W2\"):\n        o, post = prf_test(\"anesthetized\", ct, \"del\", w, \"Rep1\")\n        d = select(\"anesthetized\", ct, \"Rep1\")[[col(\"del\", \"anesthetized\", w), \"prf\"]]\n        hi = d[d.prf >= 1500].iloc[:, 0].mean()\n        lo = d[d.prf <= 300].iloc[:, 0].mean()\n        rows.append({\"type\": ct, \"reading\": w, \"KW H\": o[\"H\"], \"KW p\": o[\"p\"], \"n\": o[\"n\"],\n                     \"mean 1500-4500\": hi, \"mean 30-300\": lo, \"higher PRFs higher\": hi > lo})\nprint(pd.DataFrame(rows).round(4).to_string(index=False))\nprint(\"\\nMeans by rat and PRF, RSU W1:\")\nprint(by_rat(\"anesthetized\", \"RSU\", \"del\", \"W1\", \"Rep1\").to_string())\nprint(\"FSU W1:\")\nprint(by_rat(\"anesthetized\", \"FSU\", \"del\", \"W1\", \"Rep1\").to_string())\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## delayed-anesthesia-factor\n#\n# > Anesthesia is a significant factor in the delayed response for both RSUs and FSUs by two-way\n# > ANOVA, and it lowers the average response magnitude.\n\n# %% tags=[\"claim:delayed-anesthesia-factor\"]\nfor ct in (\"RSU\", \"FSU\"):\n    print(ct)\n    print(anova_table(ct, \"del\").round(5).to_string(index=False))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig6ad-time-adjacent-batch (blocked)\n#\n# > In the five rats recorded awake and anesthetized in the same week, time-locked responses to\n# > the low PRF and 1500 Hz differ significantly in both states, with a reduced response under\n# > anesthesia.\n#\n# The ten rats in the dandiset are the first batch's (each has awake PRF recordings), and no file\n# is from a sham or a two-PRF protocol; the five rats of the second batch are not in it. Blocked as\n# data missing; no section is run.\n\n# %% [markdown]\n# ## fig6ef-rsu-ispta-rise-then-fall\n#\n# > Awake RSU mean responses, time-locked and delayed, rise with ISPTA up to around 60 mW/cm2 and\n# > then decline.\n\n# %% tags=[\"claim:fig6ef-rsu-ispta-rise-then-fall\"]\ndef ispta_table(ct):\n    rows = []\n    for w, rep in READINGS:\n        for kind in (\"tl\", \"del\"):\n            if kind == \"del\" and w == \"W2\":\n                continue\n            d = select(\"awake\", ct, rep)\n            c = col(kind, \"awake\", w)\n            g = d.groupby(\"prf\")[c]\n            m, se = g.mean(), g.sem()\n            rows.append({\"window\": kind, \"reading\": f\"{w} {rep}\",\n                         **{f\"{p} Hz ({tfus.PRF_ISPTA[p]})\": f\"{m[p]:.1f} +- {se[p]:.1f}\" for p in PRFS},\n                         \"_m\": m})\n    return rows\n\n\nrows = ispta_table(\"RSU\")\nout = []\nfor r in rows:\n    m = r.pop(\"_m\")\n    peak = m.idxmax()\n    rise = all(m[PRFS[i]] <= m[PRFS[i + 1]] for i in range(PRFS.index(peak))) if peak in (1500, 3000) else False\n    out.append({**r, \"peak\": peak, \"peak at 1500/3000\": peak in (1500, 3000), \"rises 30 to peak\": rise,\n                \"4500 below peak\": m[4500] < m[peak]})\nprint(\"Mean +- SEM (%) by PRF (ISPTA mW/cm2):\")\nprint(pd.DataFrame(out).to_string(index=False))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig6fh-fsu-ispta\n#\n# > Awake FSUs show no time-locked response, and their delayed response increases almost linearly\n# > with ISPTA.\n#\n# The time-locked part takes the awake outcome of fig5bd-fsu-time-locked-no-prf.\n\n# %% tags=[\"claim:fig6fh-fsu-ispta\"]\nrows = []\nfor rep in (\"Rep1\", \"Rep2\"):\n    m = select(\"awake\", \"FSU\", rep).groupby(\"prf\").del_awake.mean()\n    x = [tfus.PRF_ISPTA[p] for p in PRFS]\n    y = [m[p] for p in PRFS]\n    rows.append({\"reading\": rep, **{f\"{p} Hz\": round(m[p], 1) for p in PRFS},\n                 \"Spearman rho\": stats.spearmanr(x, y)[0], \"Pearson r\": stats.pearsonr(x, y)[0]})\nprint(pd.DataFrame(rows).round(3).to_string(index=False))\no, post = prf_test(\"awake\", \"FSU\", \"tl\", \"W1\", \"Rep1\")\nprint(f\"\\nTime-locked part (from fig5bd, awake, W1 Rep1): Kruskal-Wallis p = {o['p']:.2g}, \"\n      f\"{int(post.sig.sum())} significant post hoc pairs\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig5a-1500-highest-time-locked-mean\n#\n# > Among PRFs, 1500 Hz gives the highest mean RSU time-locked response in awake rats, although not\n# > significantly above 3000 and 4500 Hz.\n\n# %% tags=[\"claim:fig5a-1500-highest-time-locked-mean\"]\nrows = []\nfor w, rep in READINGS:\n    o, post = prf_test(\"awake\", \"RSU\", \"tl\", w, rep)\n    rows.append({\"reading\": f\"{w} {rep}\", **{f\"{p} Hz\": round(o[\"mean\"][p], 1) for p in PRFS},\n                 \"highest\": max(o[\"mean\"], key=o[\"mean\"].get),\n                 \"p_bonf 1500 vs 3000\": tfus.pair(post, 1500, 3000).p_bonf, \"p_bonf 1500 vs 4500\": tfus.pair(post, 1500, 4500).p_bonf})\nprint(pd.DataFrame(rows).round(4).to_string(index=False))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## Duty cycle claims (fig7a to fig7d)\n#\n# The DC series is 1500 Hz with TBD 40, 200 and 400 us (6, 30 and 60%). The dandiset holds 6% and\n# 60% recordings for three rats (BH506, BH521, BH526) and no 30% recording of its own: the 30%\n# condition can only be the 1500 Hz, 200 us recordings of the PRF series. Two readings are run\n# (the claims file does not name them; they come from what the dandiset holds): C1, the 30%\n# recordings of the same rats (BH506 and BH526; BH521 has none), and C2, every awake 1500 Hz,\n# 200 us recording. C2 is run with and without the repeats. Parts that compare with sham cannot be\n# tested.\n\n# %%\nDCS = [6, 30, 60]\n\n\ndef dc_test(ct, kind, w, reading):\n    c = col(kind, \"awake\", w)\n    d = L[(L.state == \"awake\") & (L.prf == 1500) & (L.celltype == ct)]\n    dc_rats = set(d[d.tbd != 200].rat)\n    if reading == \"C1\":\n        d = d[d.rat.isin(dc_rats)]\n    if reading == \"C2 Rep2\":\n        d = d[~d.repeat]\n    return tfus.group_test({dc: d[d.dc == dc][c].values for dc in DCS})\n\n\nDC_READINGS = [(w, r) for w in (\"W1\", \"W2\") for r in (\"C1\", \"C2 Rep1\", \"C2 Rep2\")]\nprint(\"Recordings in the DC comparison:\")\nd = L[(L.state == \"awake\") & (L.prf == 1500)]\nprint(d.groupby([\"dc\", \"rat\"]).session.unique().to_string())\n\n# %% [markdown]\n# ## fig7a-rsu-time-locked-dc\n#\n# > Awake RSU time-locked responses at 1500 Hz PRF are significantly lower at 6% DC than at 60% DC\n# > (and, by the Figure 7A legend, than at 30% DC), and every DC is significantly higher than sham.\n\n# %% tags=[\"claim:fig7a-rsu-time-locked-dc\"]\nrows = []\nfor w, r in DC_READINGS:\n    o, post = dc_test(\"RSU\", \"tl\", w, r)\n    if (w, r) == (\"W1\", \"C1\"):\n        show(o, post, \"awake RSU 0-67 ms by DC, W1 C1\")\n    rows.append({\"reading\": f\"{w} {r}\", \"n\": o[\"n\"], **{f\"mean {k}%\": round(v, 1) for k, v in o[\"mean\"].items()},\n                 \"(1) KW\": o[\"p\"] < 0.05, \"(2) 6 below 60\": lower(post, 6, 60), \"(4) 6 below 30\": lower(post, 6, 30),\n                 \"p_bonf 6-60\": tfus.pair(post, 6, 60).p_bonf, \"p_bonf 6-30\": tfus.pair(post, 6, 30).p_bonf})\nprint(pd.DataFrame(rows).to_string(index=False))\nprint(\"\\nMean by rat and DC (W1):\")\nprint(by_rat(\"awake\", \"RSU\", \"tl\", \"W1\", \"Rep1\", tbd=40).join(by_rat(\"awake\", \"RSU\", \"tl\", \"W1\", \"Rep1\", tbd=400)).join(\n    select(\"awake\", \"RSU\", \"Rep1\", prf=1500).groupby(\"rat\").tl_w1.mean().round(1).rename(\"30 (1500 Hz, 200 us)\"), how=\"outer\").to_string())\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig7a-60-highest-time-locked-mean\n#\n# > By mean values 60% DC gives the strongest RSU time-locked response, though it is only\n# > significantly higher than 6%.\n\n# %% tags=[\"claim:fig7a-60-highest-time-locked-mean\"]\nrows = []\nfor w, r in DC_READINGS:\n    o, post = dc_test(\"RSU\", \"tl\", w, r)\n    rows.append({\"reading\": f\"{w} {r}\", **{f\"mean {k}%\": round(v, 1) for k, v in o[\"mean\"].items()},\n                 \"highest\": max(o[\"mean\"], key=o[\"mean\"].get), \"p_bonf 60 vs 30\": tfus.pair(post, 60, 30).p_bonf})\nprint(pd.DataFrame(rows).to_string(index=False))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig7b-fsu-time-locked-dc\n#\n# > FSUs show no time-locked response across DC levels; no significant differences are observed.\n#\n# A claim of absence, judged on the Kruskal-Wallis across 6, 30 and 60% (G1) at 0.05 and the post\n# hoc tests at Bonferroni-corrected 0.05.\n\n# %% tags=[\"claim:fig7b-fsu-time-locked-dc\"]\nrows = []\nfor w, r in DC_READINGS:\n    o, post = dc_test(\"FSU\", \"tl\", w, r)\n    if (w, r) == (\"W1\", \"C1\"):\n        show(o, post, \"awake FSU 0-67 ms by DC, W1 C1\")\n    rows.append({\"reading\": f\"{w} {r}\", \"n\": o[\"n\"], **{f\"median {k}%\": round(v, 1) for k, v in o[\"median\"].items()},\n                 **{f\"mean {k}%\": round(v, 1) for k, v in o[\"mean\"].items()},\n                 \"KW p\": o[\"p\"], \"significant pairs\": int(post.sig.sum())})\nprint(pd.DataFrame(rows).to_string(index=False))\nprint(\"\\nMean by rat and DC (W1):\")\nprint(by_rat(\"awake\", \"FSU\", \"tl\", \"W1\", \"Rep1\", tbd=40).join(by_rat(\"awake\", \"FSU\", \"tl\", \"W1\", \"Rep1\", tbd=400)).to_string())\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig7c-rsu-delayed-dc\n#\n# > Awake RSU delayed responses prefer 30% DC over 6% and 60%, all three DCs differ (Figure 7C\n# > legend), and at 60% DC they do not differ from sham.\n#\n# Part (3) compares with sham and cannot be tested. The window is on bin edges (W1 = W2).\n\n# %% tags=[\"claim:fig7c-rsu-delayed-dc\"]\nrows = []\nfor r in (\"C1\", \"C2 Rep1\", \"C2 Rep2\"):\n    o, post = dc_test(\"RSU\", \"del\", \"W1\", r)\n    show(o, post, f\"awake RSU 0.5-1 s by DC, {r}\")\n    rows.append({\"reading\": r, \"(1) KW\": o[\"p\"] < 0.05, \"(2) 30 above 6 and 60\": lower(post, 6, 30) and lower(post, 60, 30),\n                 \"(4) 6 and 60 differ\": sig(post, 6, 60)})\nprint(pd.DataFrame(rows).to_string(index=False))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig7d-fsu-delayed-dc\n#\n# > Awake FSU delayed responses are significantly higher at 60% DC than at 6%, and at 6% DC they do\n# > not differ from sham.\n#\n# Part (3) compares with sham and cannot be tested.\n\n# %% tags=[\"claim:fig7d-fsu-delayed-dc\"]\nrows = []\nfor r in (\"C1\", \"C2 Rep1\", \"C2 Rep2\"):\n    o, post = dc_test(\"FSU\", \"del\", \"W1\", r)\n    show(o, post, f\"awake FSU 0.5-1 s by DC, {r}\")\n    rows.append({\"reading\": r, \"(1) KW\": o[\"p\"] < 0.05, \"(2) 60 above 6\": lower(post, 6, 60)})\nprint(pd.DataFrame(rows).to_string(index=False))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## sham-no-auditory-response (blocked)\n#\n# > The off-target sham at 1500 Hz PRF produced no significant response, so the activation is not\n# > attributed to an auditory or skull-conduction confound.\n#\n# The criterion blocks this claim (the paper names no test of the sham), and the dandiset holds no\n# sham recording, so the sham's responses cannot be shown either.\n\n# %% [markdown]\n# ## Summary\n#\n# ...\n\n# %%\nprint(f\"notebook ran in {time.time() - started:.0f} s\")\n"
}
```

```
File created successfully at: entries/000945-ramachandran-2025/reproduce_ramachandran_2025.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && jupytext --to ipynb reproduce_ramachandran_2025.py -o $TMPDIR/dev.ipynb -q && cp tfus.py $TMPDIR/ && cd $TMPDIR && time jupyter nbconvert --to notebook --execute dev.ipynb --output dev_out.ipynb --ExecutePreprocessor.timeout=1200 2>&1 | tail -5
```

```
[NbConvertApp] Converting notebook dev.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 271703 bytes to dev_out.ipynb

real	1m0.124s
user	0m27.640s
sys	0m2.950s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 -c "
import json
nb=json.load(open('dev_out.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': 
        s=''.join(c['source']); 
        if s.startswith('## '): print('\n#####', s.splitlines()[0])
        continue
    for o in c.get('outputs',[]):
        if 'text' in o: print(''.join(o['text']))
        elif o.get('output_type')=='error': print('ERROR', o['ename'], o['evalue'])
" > out.txt; wc -l out.txt; head -c 20000 out.txt
```

```
726 out.txt
loaded 75 files from dandiset 000945 version 0.250213.2212 in 48 s


##### ## Data check
Files: 75 ; subject folders: 10 ['BH497', 'BH498', 'BH506', 'BH508', 'BH512', 'BH514', 'BH519', 'BH521', 'BH526', 'BH527']
Rats named in identifiers: ['BH498', 'BH506', 'BH508', 'BH512', 'BH519', 'BH521', 'BH526', 'BH527']
Files whose subject_id differs from the rat in the identifier:
                                               path          identifier
sub-BH497/sub-BH497_ses-20240310T143729_ecephys.nwb BH498_3000_200_anes
sub-BH497/sub-BH497_ses-20240310T145053_ecephys.nwb BH498_1500_200_anes
sub-BH497/sub-BH497_ses-20240310T145814_ecephys.nwb  BH498_300_200_anes
sub-BH497/sub-BH497_ses-20240310T150748_ecephys.nwb   BH498_30_200_anes
sub-BH497/sub-BH497_ses-20240310T152652_ecephys.nwb BH498_4500_200_anes
sub-BH514/sub-BH514_ses-20240309T183140_ecephys.nwb BH512_1500_200_anes
sub-BH514/sub-BH514_ses-20240309T183856_ecephys.nwb  BH512_300_200_anes
sub-BH514/sub-BH514_ses-20240309T184852_ecephys.nwb BH512_4500_200_anes
sub-BH514/sub-BH514_ses-20240309T185729_ecephys.nwb BH512_3000_200_anes

Units table columns: {'spike_times celltype_label': 60, 'spike_times': 15}
[... 276 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -n '/##### ## fig5a-rsu-time-locked-prf-awake/,$p' out.txt
```

```
##### ## fig5a-rsu-time-locked-prf-awake
awake RSU 0-67 ms, W1 Rep1: Kruskal-Wallis H = 78.7, p = 3.3e-16; n = {30: 255, 300: 269, 1500: 303, 3000: 334, 4500: 270}
  means: {30: 96.8, 300: 97.6, 1500: 98.5, 3000: 108.2, 4500: 99.2}  medians: {30: 96.5, 300: 99.5, 1500: 100.7, 3000: 104.5, 4500: 99.9}
   a    b   mean_a   mean_b      p  p_bonf   sig
  30  300  96.8249  97.6406 0.0096  0.0955 False
  30 1500  96.8249  98.4572 0.0124  0.1241 False
  30 3000  96.8249 108.2052 0.0000  0.0000  True
  30 4500  96.8249  99.1909 0.0028  0.0277  True
 300 1500  97.6406  98.4572 0.6262  1.0000 False
 300 3000  97.6406 108.2052 0.0000  0.0000  True
 300 4500  97.6406  99.1909 0.8846  1.0000 False
1500 3000  98.4572 108.2052 0.0000  0.0000  True
1500 4500  98.4572  99.1909 0.7678  1.0000 False
3000 4500 108.2052  99.1909 0.0000  0.0000  True
reading  (1) KW  (2) 30 below each  (3) 300 below each  (4) no pair of 1500/3000/4500  highest mean
W1 Rep1    True              False               False                          False          3000
W1 Rep2    True              False               False                          False          3000
W2 Rep1    True               True               False                          False          3000
W2 Rep2    True              False               False                          False          3000

[... 416 more lines not kept]
```

**Agent calls Bash**

```bash
date -u
```

```
Sat Oct 31 21:41:54 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/000945-ramachandran-2025 && python3 - <<'EOF'
p='reproduce_ramachandran_2025.py'
s=open(p).read()
s=s.replace("other is a `_2` repeat). 63 recordings remain.","other is a `_2` repeat). 64 recordings remain.")
s=s.replace("""    peaks = [round(bins[i], 3) for i""","""    peaks = [round(float(bins[i]), 3) for i""")
# delayed anesthesia: add criterion check
s=s.replace("""for ct in ("RSU", "FSU"):
    print(ct)
    print(anova_table(ct, "del").round(5).to_string(index=False))""","""tabs = {ct: anova_table(ct, "del") for ct in ("RSU", "FSU")}
for ct, t in tabs.items():
    print(ct)
    print(t.round(5).to_string(index=False))
chk = pd.DataFrame({"reading": tabs["RSU"].reading,
                    "RSU p<0.001": tabs["RSU"]["p state"] < 0.001, "FSU p<0.01": tabs["FSU"]["p state"] < 0.01,
                    "both p<0.05": (tabs["RSU"]["p state"] < 0.05) & (tabs["FSU"]["p state"] < 0.05),
                    "anes lower, both types": (tabs["RSU"]["anes mean"] < tabs["RSU"]["awake mean"]) & (tabs["FSU"]["anes mean"] < tabs["FSU"]["awake mean"])})
print(chk.to_string(index=False))
print("\\nFSU per-rat means, awake recordings with and without the repeats (0.5-1 s):")
print(select("awake", "FSU", "Rep1").groupby(["rat", "repeat"]).del_awake.agg(["size", "mean"]).round(1).to_string())""")
open(p,'w').write(s)
EOF
grep -n "Result: \.\.\." reproduce_ramachandran_2025.py | head -40
```

```
346:# **Result: ...**
416:# **Result: ...**
440:# **Result: ...**
467:# **Result: ...**
493:# **Result: ...**
528:# **Result: ...**
557:# **Result: ...**
584:# **Result: ...**
608:# **Result: ...**
633:# **Result: ...**
655:# **Result: ...**
703:# **Result: ...**
727:# **Result: ...**
745:# **Result: ...**
799:# **Result: ...**
816:# **Result: ...**
840:# **Result: ...**
860:# **Result: ...**
879:# **Result: ...**
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='reproduce_ramachandran_2025.py'
s=open(p).read()
R=[
# fig3
"""**Result: partially reproduced.** With the dataset's labels (K0), two single recordings give all
three counts within tolerance (R1): BH527_30_200 with 28 FSU, 34 RSU and 62 units, and
BH508_4500_200_2 with 28 FSU, 30 RSU and 58 units. No rat's series matches (R2; totals 77 to 616).
The labels follow the expected rate difference in 46 of 59 recordings (FSU median baseline rate
above the RSU median; 8.60 against 5.84 Hz over units). The k-means sorting itself, and the
separation of the clusters on the initial phase and after-hyperpolarization durations, cannot be
tested: the files hold no waveforms. Only the count part of the criterion could be tested, and it
holds.""",
# fig4hi
"""**Result: not reproduced.** Under none of the 16 readings do awake FSU onsets come later than
anesthetized ones at p < 0.001: rank-sum p ranges from 0.018 to 0.85, and in 8 readings the
anesthetized mean is the later one. The awake means (0.40 to 0.58 s) are within 0.51 +- 0.14 s, but
the anesthetized means (0.38 to 0.52 s) are all outside 0.24 +- 0.08 s. Most FSU qualify as having a
delayed response (193 to 265 of 306 awake, 34 or 39 of 50 anesthetized). The anesthetized FSU come
from two rats.""",
# fig4h
"""**Result: not reproduced.** The awake SD exceeds the anesthetized SD in 10 of 16 readings, and
never by more than 0.02 s (0.381 to 0.393 s awake, 0.367 to 0.406 s anesthetized); the criterion
asks for every reading. Under S1 D1 L1 Rep1 the awake histogram has its largest count in the first
allowed bin (61 of 262 at 0.071 s) and several smaller local maxima; the anesthetized histogram
(39 units) is flat with many single-count maxima.""",
# fig5a
"""**Result: not reproduced.** PRF is a significant factor (Kruskal-Wallis p = 3.3e-16, W1 Rep1),
but the post hoc pattern differs. The highest mean is at 3000 Hz (108.2%; 1500 Hz 98.5%), and
3000 Hz differs from 1500 and 4500 Hz (corrected p < 1e-4), so part (4) fails under every reading.
300 Hz is not below 1500 or 4500 Hz (part 3 fails under every reading), and 30 Hz is below every
higher PRF only under W2 Rep1 (part 2). Parts (5) and (6) need the sham and are not tested. Means
by rat vary widely (BH526 at 64 to 101%, BH506 at 100 to 130%).""",
# fig5c
"""**Result: not reproduced.** Under anesthesia (two labelled rats) the Kruskal-Wallis is
significant (p = 7.3e-08 W1, 7.7e-07 W2) and 30 Hz and 300 Hz do not differ (part 7 holds), but the
other parts do not: 1500 Hz is the peak (107.0%), 30 Hz is not below 3000 or 4500 Hz, 300 Hz is
not below 3000 or 4500 Hz, and 1500 Hz differs from 4500 Hz (and from 3000 Hz under W1). Only part
(1) and part (7) of the testable parts hold. The 1500 Hz effect comes from BH512 (110.4% against
101.7% in BH498).""",
# rsu anes factor
"""**Result: not reproduced.** Anesthesia is a significant factor (p = 0.011 to 0.018 over the eight
readings, all above 0.01), and the direction is the reverse of the claim: the anesthetized mean
(102.6 to 102.9%) is above the awake mean (100.1 to 100.4%). With only the two rats that have
labelled anesthetized data, the effect is not significant (p = 0.425).""",
# fig5bd
"""**Result: not reproduced.** By the paper's test FSU time-locked responses do differ across PRF:
Kruskal-Wallis p = 1.8e-12 awake and 5.5e-04 anesthetized (W1 Rep1), with 5 or 6 significant post
hoc pairs awake and 2 or 3 anesthetized under every reading. The effects are small: group medians
span 98.7 to 103.4% awake and 99.8 to 103.9% anesthetized; the awake 3000 Hz mean is 106.8%.""",
# fig5e
"""**Result: not reproduced.** PRF is a significant factor (p = 6e-20 Rep1, 4.5e-15 Rep2), but
the two highest means are at 1500 Hz and 30 Hz (106.7 and 106.6% Rep1; 108.8 and 106.6% Rep2),
not 1500 and 3000 Hz: 3000 Hz (102.3%) is below 1500 Hz (corrected p = 0.0053) and not above 30
Hz. Part (2) fails under both of its readings; part (3) needs the sham and is not tested.""",
# fig5f
"""**Result: not reproduced.** PRF is a significant factor (p = 4.6e-12 Rep1) and 30 Hz differs
from 1500, 3000 and 4500 Hz (part 3), but the strongest mean is at 30 Hz (103.5%), not 4500 Hz
(100.3%), and 300 Hz does not differ from 4500 Hz (corrected p = 1.0). Two of the three testable
parts after (1) fail under both readings; part (5) needs the sham and is not tested.""",
# fig5gh
"""**Result: not reproduced.** Under anesthesia PRF is not a significant factor for delayed
responses: Kruskal-Wallis p = 0.16 (W1) and 0.12 (W2) for RSU, 0.16 and 0.18 for FSU. The pooled
1500 to 4500 Hz means are above the 30 and 300 Hz means by less than one percentage point (RSU
99.97 against 99.15%, FSU 99.87 against 99.35%, W1). The data are two rats.""",
# delayed anes factor
"""**Result: reproduced, resting on an assumption.** Without the `_2` repeats (Rep2, the reading
adopted; see the readings above and the summary), anesthesia is a significant factor for both
types under all four model and window readings: RSU p < 1e-8 (F = 34.4 to 34.9) and FSU p = 0.0013
to 0.0015, with the anesthetized mean lower in both (RSU 99.7 against 104.6%, FSU 99.7 against
101.3%). With the repeats (Rep1) the RSU part holds (F = 21.3 to 21.6, p < 1e-5) but the FSU effect
is p = 0.038 to 0.041, which misses the 0.01 bound: partially reproduced under that reading.""",
# fig6ef
"""**Result: partially reproduced, resting on an assumption.** Time-locked RSU means rise from 30 Hz
(96.8%) to a peak at 3000 Hz (60.26 mW/cm2; 108.2%) and fall at 4500 Hz (99.2%) under W1 Rep1, W2
Rep1 and W2 Rep2; under W1 Rep2 the 300 Hz mean (98.2%) is 0.1 point above the 1500 Hz mean
(98.1%), against SEMs of 1.1 and 1.3. The delayed means do not rise to their peak: 106.6% at 30 Hz,
101.2% at 300 Hz and 106.7% at 1500 Hz (Rep1). The time-locked window holds under W2, the reading
adopted (responses come from the binned PSTH), and the delayed window does not.""",
# fig6fh
"""**Result: not reproduced.** The time-locked part fails (fig5bd: awake Kruskal-Wallis p =
1.8e-12). The delayed FSU means do not increase with ISPTA: 103.5, 98.7, 101.8, 100.6 and 100.3%
from 30 to 4500 Hz (Spearman rho = -0.4, Pearson r = -0.27, Rep1; rho = -0.3 Rep2).""",
# fig5a-1500
"""**Result: not reproduced.** The highest mean RSU time-locked response is at 3000 Hz under every
reading (107.7 to 108.7%), and it is significantly above 1500 Hz (corrected p = 0.0029 or less);
1500 Hz gives 98.1 to 98.7%.""",
# fig7a
"""**Result: not reproduced.** The DC effect is significant (Kruskal-Wallis p = 1.5e-22, W1 C1),
but 6% is the highest group, not the lowest: 180.8% at 6%, 147.5% at 60% and 90.5 to 98.7% at 30%
under every reading. 6% does not differ from 60% (corrected p = 1.0) and is far above 30%. The 6%
and 60% effects come mostly from BH506 (249.0 and 209.9%); BH521 and BH526 give 113 to 121%. Part
(3) needs the sham and is not tested.""",
# fig7a-60
"""**Result: not reproduced.** The highest mean is at 6% DC under every reading (176.3 to 180.8%),
with 60% at 147.1 to 147.5%. 60% is significantly above 30% (corrected p < 1e-16), where the claim
says only 6% differs from it.""",
# fig7b
"""**Result: not reproduced.** FSU time-locked responses differ across DC under every reading:
Kruskal-Wallis p = 3.5e-12 (W1 C1) or smaller, with all three pairs significant. FSU respond
strongly at 6% and 60% (means 156.8 and 205.3%, medians 115.0 and 128.6%) and not at 30% (median
100.8%); the largest responses are in BH506 (338.6 and 403.3%).""",
# fig7c
"""**Result: not reproduced, resting on an assumption.** With the 30% group taken from the same rats
as the 6% and 60% recordings (C1, the reading adopted), the DC effect on RSU delayed responses is
not significant (Kruskal-Wallis p = 0.21) and no pair differs. With every awake 1500 Hz, 200 us
recording as the 30% group (C2), the effect is significant (p = 2.2e-04 Rep1, 3.7e-05 Rep2) and 30%
is above 6% and 60%, but 6% and 60% do not differ (corrected p = 0.071): partially reproduced under
C2. Part (3) needs the sham and is not tested.""",
# fig7d
"""**Result: reproduced.** Under every reading the DC effect on FSU delayed responses is
significant (Kruskal-Wallis p = 0.011 C1, 4.5e-07 C2 Rep1, 1.4e-06 C2 Rep2) and 60% is above 6%
(corrected p = 0.015). Part (3), 6% against sham, needs the sham and is not tested. The difference
is small and both groups are below baseline (means 99.6% at 60% and 98.2% at 6%).""",
]
parts=s.split("# **Result: ...**")
assert len(parts)==len(R)+1, (len(parts),len(R))
out=parts[0]
for r,rest in zip(R,parts[1:]):
    out+="\n".join("# "+l for l in r.splitlines())+rest
open(p,'w').write(out)
EOF
grep -c "Result:" reproduce_ramachandran_2025.py
```

```
19
```

**Agent**

Checking the numbers in the conclusions against the outputs turned up a few corrections and one p-value I need printed with more digits.

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='reproduce_ramachandran_2025.py'
s=open(p).read()
rep=[("and in 8 readings the\n# anesthetized mean is the later one","and in 6 readings the\n# anesthetized mean is the later one"),
("(193 to 265 of 306 awake, 34 or 39 of 50 anesthetized)","(193 to 265 of 306 awake under Rep1, 34 or 39 of 50 anesthetized)"),
("hoc pairs awake and 2 or 3 anesthetized under every reading. The effects are small: group medians\n# span 98.7 to 103.4% awake","hoc pairs awake and 2 or 3 anesthetized under every reading. The effects are small: group medians\n# span 98.7 to 103.4% awake (W1 Rep1)"),
("(corrected p = 0.0029 or less)","(corrected p = 0.0040 or less)"),
("and 90.5 to 98.7% at 30%","and 90.4 to 98.7% at 30%"),
("print(t_rsu.round(4).to_string(index=False))","print(t_rsu.to_string(index=False, float_format=lambda v: f\"{v:.4g}\"))"),
("    print(t.round(5).to_string(index=False))","    print(t.to_string(index=False, float_format=lambda v: f\"{v:.4g}\"))"),
]
for a,b in rep:
    assert a in s, a
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
grep -n "180.8% at 6%" reproduce_ramachandran_2025.py
```

```
855:# but 6% is the highest group, not the lowest: 180.8% at 6%, 147.5% at 60% and 90.4 to 98.7% at 30%
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='reproduce_ramachandran_2025.py'
s=open(p).read()
s=s.replace("180.8% at 6%, 147.5% at 60% and 90.4 to 98.7% at 30%","180.8% at 6% and 147.5% at 60% (W1), and 90.4 to 98.7% at 30%")
old="""#   PRFs, BH512 without 30 Hz); BH521's three are unlabelled and cannot enter a cell-type test.
"""
new="""#   PRFs, BH512 without 30 Hz); BH521's three are unlabelled and cannot enter a cell-type test.
# - **Sham.** The dandiset holds no sham recording. Parts of a criterion that compare with sham
#   are reported as not tested and the claim is judged on its other parts, as the claims file's
#   header says for an anesthetized sham; the same is done for the awake sham.
#
# Where readings give different outcomes, the reading best supported by the paper is adopted as an
# assumption, and every reading is still shown: W2, as the Methods derive responses from the binned
# PSTH ("resulting in a histogram of average spikes per time bin for each neuron", Methods 2.4);
# Rep2, as the Methods describe one recording per parameter set per rat (Methods 2.3); and, for
# the duty cycle claims, C1 (defined there), as the paper's DC series compares the levels within
# the same rats.
"""
assert old in s
s=s.replace(old,new)
old="""# ## Summary
#
# ...
"""
new="""# ## Summary
#
# A failure to reproduce here may be a failure of this attempt, not of the paper: see the
# reasoning and the differences from the paper's method.
#
# | Claim | Outcome |
# |---|---|
# | fig3-cell-type-sorting | Partially reproduced: counts match in two recordings; the k-means features cannot be computed |
# | fig4-rsu-time-locked-both-states | Blocked: data missing (no sham) |
# | fig4hi-fsu-delayed-latency | Not reproduced |
# | fig4h-awake-latency-wider | Not reproduced |
# | fig5a-rsu-time-locked-prf-awake | Not reproduced |
# | fig5c-rsu-time-locked-prf-anesth | Not reproduced |
# | rsu-time-locked-anesthesia-factor | Not reproduced |
# | fig5bd-fsu-time-locked-no-prf | Not reproduced |
# | fig5e-rsu-delayed-prf-awake | Not reproduced |
# | fig5f-fsu-delayed-prf-awake | Not reproduced |
# | fig5gh-delayed-prf-anesth | Not reproduced |
# | delayed-anesthesia-factor | Reproduced (assumption: Rep2) |
# | fig6ad-time-adjacent-batch | Blocked: data missing (second batch) |
# | fig6ef-rsu-ispta-rise-then-fall | Partially reproduced (assumption: W2) |
# | fig6fh-fsu-ispta | Not reproduced |
# | fig5a-1500-highest-time-locked-mean | Not reproduced |
# | fig7a-rsu-time-locked-dc | Not reproduced |
# | fig7a-60-highest-time-locked-mean | Not reproduced |
# | fig7b-fsu-time-locked-dc | Not reproduced |
# | fig7c-rsu-delayed-dc | Not reproduced (assumption: C1) |
# | fig7d-fsu-delayed-dc | Reproduced |
# | sham-no-auditory-response | Blocked: methods underspecified, and no sham data |
#
# **How the analysis differs from the paper's.** Cell types are the dataset's labels; the k-means
# on waveform features cannot be run, as there are no waveforms. The files hold 500 trials (the
# paper's 505 less five), and five recordings hold 203 to 339. No sham recording exists, so every
# comparison with sham is left out. The anesthetized PRF series has labelled units from two rats
# (the paper: ten), and BH512 has no 30 Hz recording. The DC series has 6% and 60% recordings from
# three rats and no 30% recording of its own. Ten awake recordings are `_2` repeats the paper does
# not describe; results are shown with and without them. No unit was excluded for a fluctuating
# baseline or for movement, as the dataset marks none.
#
# **What was found about the dataset.** Twelve of the 75 files are second copies of other files:
# the anesthetized recordings of BH498 and BH512 are each deposited twice (with labels under
# subject folders BH497 and BH514, without labels under BH498 and BH512), BH512's 1500 Hz
# anesthetized recording a third time, and one 30 Hz recording is filed under both BH498 and
# BH508. The condition of a recording is coded only in its identifier; the `_2` suffix and the
# 2.2 s `stop_time` are not described. Fifteen anesthetized files have no cell-type labels. Every
# file gives age P24W, where the paper gives 7 to 10 months, and the labelled anesthetized copies
# are described as awake. The second batch of five rats, the sham condition and the 30% DC
# recordings are not in the dandiset. In most 200 us recordings no time-locked population response
# can be detected (10 of 64 recordings show one at t > 3, among them 5 of the 6 awake 40 and 400 us
# recordings), while the 6% and 60% DC recordings respond strongly, FSU included.
"""
assert old in s
s=s.replace(old,new)
open(p,'w').write(s)
EOF
date -u
```

```
Sat Oct 31 21:43:19 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='reproduce_ramachandran_2025.py'
s=open(p).read()
s=s.replace("among them 5 of the 6 awake 40 and 400 us","among them 4 of the 6 awake 40 and 400 us")
old="""        m = 100 * np.concatenate(prof).mean(0)
"""
new="""        m = 100 * np.concatenate(prof).mean(0)
        seg = {f"{a:+.3f} to {b:+.3f} s": m[(t > a) & (t < b)].mean() for a, b in ((-0.075, 0), (0, 0.075), (0.075, 0.15))}
        print(f"{st} {prf} Hz {tbd} us {name}: mean % of baseline", {k: round(v, 1) for k, v in seg.items()},
              f"; peak {m.max():.0f}% at {t[np.argmax(m)]:.4f} s")
"""
assert old in s; s=s.replace(old,new)
old="""# Where a recording responds at all, the response begins in the first 5 ms bins after
# `start_time` and lasts about 75 ms, the 67 ms ultrasound duration, and the same contrast 1.25 s
# later is near zero. So `start_time` is the trigger and spikes and trials share a clock in those
# recordings. In recordings with no time-locked response the check cannot tell; the table names
# them (t at true times below 3)."""
new="""# Ten of the 64 recordings show a population rise in the 67 ms after `start_time` (t > 3) and none
# shows one at the shifted times. In the conditions plotted, the rise is confined to the 75 ms
# after `start_time` (the values printed above), the span of the 67 ms ultrasound. So
# `start_time` is the trigger, and spikes and trials share a clock in those recordings, which
# include awake and anesthetized ones and four of the eight rats (BH498, BH506, BH512, BH521). In
# the other 54 recordings the check cannot tell a shared clock from no response."""
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
EOF
. $TMPDIR/env/bin/activate && jupytext --to ipynb reproduce_ramachandran_2025.py -o $TMPDIR/dev.ipynb -q && cp tfus.py $TMPDIR/ && cd $TMPDIR && jupyter nbconvert --to notebook --execute dev.ipynb --output dev_out.ipynb --ExecutePreprocessor.timeout=1200 2>&1 | tail -1 && python3 -c "
import json
nb=json.load(open('dev_out.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    for o in c.get('outputs',[]):
        if 'text' in o: print(''.join(o['text']))
        elif o.get('output_type')=='error': print('ERROR', o['ename'], o['evalue'])
" > out.txt; grep -n -E "mean % of baseline|ERROR|^RSU$|^FSU$" -A0 out.txt; sed -n '/^RSU$/,/repeat/p' out.txt | head -60
```

```
[NbConvertApp] Writing 288046 bytes to dev_out.ipynb
187:awake 1500 Hz 400 us RSU: mean % of baseline {'-0.075 to +0.000 s': np.float32(103.6), '+0.000 to +0.075 s': np.float32(146.3), '+0.075 to +0.150 s': np.float32(112.4)} ; peak 159% at 0.0275 s
188:awake 1500 Hz 400 us FSU: mean % of baseline {'-0.075 to +0.000 s': np.float32(101.1), '+0.000 to +0.075 s': np.float32(196.9), '+0.075 to +0.150 s': np.float32(115.1)} ; peak 228% at 0.0575 s
189:awake 3000 Hz 200 us RSU: mean % of baseline {'-0.075 to +0.000 s': np.float32(101.2), '+0.000 to +0.075 s': np.float32(107.6), '+0.075 to +0.150 s': np.float32(100.3)} ; peak 117% at 0.0225 s
190:awake 3000 Hz 200 us FSU: mean % of baseline {'-0.075 to +0.000 s': np.float32(100.6), '+0.000 to +0.075 s': np.float32(106.5), '+0.075 to +0.150 s': np.float32(101.1)} ; peak 110% at 0.0575 s
191:anesthetized 1500 Hz 200 us RSU: mean % of baseline {'-0.075 to +0.000 s': np.float32(99.8), '+0.000 to +0.075 s': np.float32(106.2), '+0.075 to +0.150 s': np.float32(100.2)} ; peak 113% at 0.0325 s
192:anesthetized 1500 Hz 200 us FSU: mean % of baseline {'-0.075 to +0.000 s': np.float32(100.2), '+0.000 to +0.075 s': np.float32(103.7), '+0.075 to +0.150 s': np.float32(102.2)} ; peak 111% at 0.5875 s
--
517:RSU
--
527:FSU
RSU
   reading    n  F state   p state  awake mean  anes mean
A1 W1 Rep1 1722    21.63 3.556e-06       103.4      99.71
A1 W1 Rep2 1464    34.93 4.243e-09       104.6      99.71
A1 W2 Rep1 1722    21.38 4.049e-06       103.4      99.73
A1 W2 Rep2 1464    34.63 4.951e-09       104.6      99.73
A2 W1 Rep1 1722    21.52 3.769e-06       103.4      99.71
A2 W1 Rep2 1464    34.68 4.818e-09       104.6      99.71
A2 W2 Rep1 1722    21.27 4.284e-06       103.4      99.73
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000945-ramachandran-2025 && python3 - <<'EOF'
p='reproduce_ramachandran_2025.py'
s=open(p).read()
s=s.replace('{k: round(v, 1) for k, v in seg.items()}','{k: round(float(v), 1) for k, v in seg.items()}')
old="""# shows one at the shifted times. In the conditions plotted, the rise is confined to the 75 ms
# after `start_time` (the values printed above), the span of the 67 ms ultrasound. So"""
new="""# shows one at the shifted times. In the conditions plotted, the mean rate is near baseline in the
# 75 ms before `start_time` (99.8 to 103.6%), rises in the 75 ms after it (103.7 to 196.9%), the
# span of the 67 ms ultrasound, and falls back in the next 75 ms (100.2 to 115.1%). So"""
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
EOF
cat > requirements.in <<'EOF'
dandi
h5py
matplotlib
numpy
pandas
remfile
scipy
statsmodels
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: 000945-ramachandran-2025
type: reproduction
title: Cell-type specific responses to tFUS in awake and anesthetized rat S1 (Ramachandran et al. 2025)
description: Tests the findings of Ramachandran, Gao, Yttri, Yu and He (2025) on dandiset 000945,
  which holds sorted units and trial times of awake and anesthetized rat somatosensory cortex
  recordings during transcranial focused ultrasound at five pulse repetition frequencies and three
  duty cycles. It compares time-locked and delayed responses of regular and fast spiking units
  across parameters and states, and the onset latency of delayed responses. The sham condition
  and the second batch of rats are not in the dandiset.
license: Apache-2.0
notebooks:
- path: reproduce_ramachandran_2025.ipynb
  title: Reproducing Ramachandran et al. (2025) from dandiset 000945
  runtime_minutes: 2
helpers:
- tfus.py
related:
- id: dandi:000945/0.250213.2212
  relation: uses_data
- id: doi:10.1088/1741-2552/adbb1f
  relation: reproduces
EOF
. $TMPDIR/env/bin/activate && jupytext --to ipynb reproduce_ramachandran_2025.py -o reproduce_ramachandran_2025.ipynb -q && rm reproduce_ramachandran_2025.py && ls && cd ../.. && python tools/entry.py lock entries/000945-ramachandran-2025 2>&1 | tail -5
```

```
__pycache__
entry.yaml
reproduce_ramachandran_2025.ipynb
requirements.in
tfus.py
wrote entries/000945-ramachandran-2025/requirements.lock.txt
```

**Agent calls Bash**

```bash
rm -rf entries/000945-ramachandran-2025/__pycache__; python tools/entry.py check entries/000945-ramachandran-2025 2>&1 | tail -20
```

```
0 error(s)
```

**Agent**

Now the attempt record and README, then the full `all` run.

**Agent calls Bash**

```bash
ls questions | grep 000945; sed -n 1,40p questions/000005.yaml; python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'));p=s['properties']
print(json.dumps(p['findings'])[:1500]); print(json.dumps(p.get('inputs'))[:500]); print(list(p))"
```

```
dandiset: "000005"
paper: doi:10.1038/nn.4412
questions:
- claim: fs-vm-touch-whisking
  asked: 2026-10-20
  question: At what resolution is dVm/dt of the touch-aligned average Vm taken for the latency rule,
    the recording's own sampling rate (10 or 20 kHz) or the average in 1 ms bins as for the spike
    PSTH? The same question applies to the laser-onset latencies of exc-thalamus-photoinhibition and
    to exc-vm-touch-whisking.
  passage: Touch latency was identified as the latency from touch onset to the time when dVm/dt
    crossed baseline (3x s.d. of the dVm/dt between 0 and 25 ms before touch). All touch-spike PSTHs
    were constructed with a bin size of 1 ms. (Online Methods, Data analysis)
  why: At the full sampling rate two of the five whole-cell FS cells cross the threshold at 0.0 and
    0.3 ms and the mean latency is 1.88 ms (not reproduced); in 1 ms bins the mean over three cells
    is 3.67 to 4.17 ms (within 4.0 +- 0.4). For the thalamic and cortical light the full rate gives
    0.1 ms for both, the 1 ms bins 5.0 and 2.0 ms.
  answer: >-
    The recording's sampling rate, not 1 ms bins. The Methods give 1 ms bins for spike PSTHs
    only ("All touch-spike PSTHs were constructed with a bin size of 1 ms"), and the paper's Vm
    latencies are not on a 1 ms grid. The FS onset has "median, 4.2 ms, n = 7 neurons" and the E
[... 23 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "attempts/000945-ramachandran-2025-01.yaml",
 "content": "schema_version: 2\nid: 000945-ramachandran-2025-01\ndataset:\n  archive: dandi\n  id: \"000945\"\n  version: 0.250213.2212\n  doi: 10.48324/dandi.000945/0.250213.2212\npaper: doi:10.1088/1741-2552/adbb1f\ndate: 2026-10-31\nentry: 000945-ramachandran-2025\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-13\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/41243437657\noutcomes:\n- claim: fig3-cell-type-sorting\n  outcome: partially_reproduced\n  notebook: reproduce_ramachandran_2025.ipynb\n  output: claim:fig3-cell-type-sorting\n  measured:\n  - 28\n  - 34\n  - 62\n  notes: With the dataset's cell-type labels (reading K0), two single recordings (reading R1) give\n    all three counts within tolerance, BH527_30_200 with 28 FSU, 34 RSU and 62 units (given as\n    measured) and BH508_4500_200_2 with 28 FSU, 30 RSU and 58 units. No rat's whole series matches\n    (R2; totals 77 to 616). FSU have the higher median baseline rate in 46 of 59 labelled\n    recordings (8.60 against 5.84 Hz over units). The k-means sorting and the separation of the\n    clusters on the initial phase and after-hyperpolarization durations cannot be tested, as the\n    files hold no waveforms; K1 and K2 could not be run. The criterion has no branch for a count\n    match with the feature part untestable; the outcome is partial because only the count part\n    could be tested and it holds.\n  deviations:\n  - Cell types are the dataset's labels (K0); the k-means of K1 and K2 cannot be run without\n    waveforms, so their agreement with the labels is not reported.\n  - The dependent claims use the labels directly; they do not need the k-means features, so they\n    are not affected by the untested part of this claim.\n- claim: fig4-rsu-time-locked-both-states\n  outcome: blocked\n  blocked_by: data_missing\n  notebook: reproduce_ramachandran_2025.ipynb\n  output: claim:fig4-rsu-time-locked-both-states\n  notes: The criterion compares the 1500 Hz, 200 us RSU time-locked responses with the sham\n    sessions of each state, and the dandiset holds no sham recording. Shown without a test, RSU\n    at 1500 Hz average 98.1 to 98.7% of baseline awake (n = 227 or 303) and 106.4 to 107.0%\n    anesthetized (n = 78, two rats).\n- claim: fig4hi-fsu-delayed-latency\n  outcome: not_reproduced\n  notebook: reproduce_ramachandran_2025.ipynb\n  output: claim:fig4hi-fsu-delayed-latency\n  measured:\n  - 0.506\n  - 0.447\n  notes: Under none of the 16 readings (S1/S2, D1/D2, L1/L2, Rep1/Rep2) are awake onsets later at\n    p < 0.001; rank-sum p is 0.018 to 0.85, and in 6 readings the anesthetized mean is the later.\n    Awake means are 0.40 to 0.58 s (within 0.51 +- 0.14), anesthetized means 0.38 to 0.52 s (all\n    outside 0.24 +- 0.08). Measured values are the S1 D1 L1 Rep1 means (anesthetized, awake).\n    193 to 265 of 306 awake FSU and 34 or 39 of 50 anesthetized FSU have a delayed response under\n    the paper's rule. The anesthetized FSU come from two rats (BH498, BH512). Q1 and Q2 select\n    the same recordings here.\n  deviations:\n  - The anesthetized FSU come from two labelled rats where the paper had ten; batch 2 is not in\n    the dandiset.\n  - T2 (505 trials) cannot be run; the files hold 500 trials, or fewer in five recordings.\n- claim: fig4h-awake-latency-wider\n  outcome: not_reproduced\n  notebook: reproduce_ramachandran_2025.ipynb\n  output: claim:fig4h-awake-latency-wider\n  notes: The awake SD exceeds the anesthetized SD in 10 of 16 readings, by at most 0.02 s (0.381 to\n    0.393 s awake, 0.367 to 0.406 s anesthetized); the criterion asks for every reading. The\n    awake histogram (S1 D1 L1 Rep1) has its largest count in the first allowed bin (61 of 262 at\n    0.071 s) and several smaller local maxima.\n- claim: fig5a-rsu-time-locked-prf-awake\n  outcome: not_reproduced\n  notebook: reproduce_ramachandran_2025.ipynb\n  output: claim:fig5a-rsu-time-locked-prf-awake\n  notes: PRF is a significant factor (Kruskal-Wallis p = 3.3e-16, W1 Rep1) but the post hoc\n    pattern differs. The highest mean is at 3000 Hz (108.2%; 1500 Hz 98.5%), and 3000 Hz differs\n    from 1500 and 4500 Hz, so part (4) fails under every reading; part (3) fails under every\n    reading; part (2) holds only under W2 Rep1. Parts (5) and (6) need the sham and were not\n    tested.\n  deviations:\n  - No sham recording exists; parts (5) and (6) are reported as not tested and the claim is judged\n    on parts (1) to (4), as the claims file's header says for an anesthetized sham.\n  - Ten awake recordings are `_2` repeats of a condition in the same rat; results are given with\n    (Rep1) and without (Rep2) them.\n- claim: fig5c-rsu-time-locked-prf-anesth\n  outcome: not_reproduced\n  notebook: reproduce_ramachandran_2025.ipynb\n  output: claim:fig5c-rsu-time-locked-prf-anesth\n  notes: The Kruskal-Wallis is significant (p = 7.3e-08 W1, 7.7e-07 W2) and 30 and 300 Hz do not\n    differ (part 7), but parts (2), (3) and (4) fail under both readings. 1500 Hz is the peak\n    (107.0%) and differs from 4500 Hz; 30 and 300 Hz are not below 3000 or 4500 Hz. The 1500 Hz\n    peak comes from BH512 (110.4% against 101.7% in BH498).\n  deviations:\n  - Two labelled rats (BH498 at five PRFs, BH512 without 30 Hz) where the paper had ten; BH521's\n    anesthetized recordings have no labels.\n  - Parts (5) and (6) need the sham and were not tested.\n- claim: rsu-time-locked-anesthesia-factor\n  outcome: not_reproduced\n  notebook: reproduce_ramachandran_2025.ipynb\n  output: claim:rsu-time-locked-anesthesia-factor\n  notes: Anesthesia is a factor at p = 0.011 to 0.018 over the eight readings (A1/A2, W1/W2,\n    Rep1/Rep2), all above the 0.01 bound, and in the reverse direction; the anesthetized mean\n    (102.6 to 102.9%) is above the awake mean (100.1 to 100.4%). With only BH498 and BH512, p =\n    0.425.\n  deviations:\n  - Anesthetized units from two rats; awake units from seven.\n- claim: fig5bd-fsu-time-locked-no-prf\n  outcome: not_reproduced\n  notebook: reproduce_ramachandran_2025.ipynb\n  output: claim:fig5bd-fsu-time-locked-no-prf\n  notes: By the paper's test FSU time-locked responses differ across PRF in both states,\n    Kruskal-Wallis p = 1.8e-12 awake and 5.5e-04 anesthetized (W1 Rep1), with 5 or 6 significant\n    post hoc pairs awake and 2 or 3 anesthetized under every reading. The effects are small;\n    group medians span 98.7 to 103.4% awake and 99.8 to 103.9% anesthetized, and the awake 3000 Hz\n    mean is 106.8%. G2 (with sham) cannot be run.\n- claim: fig5e-rsu-delayed-prf-awake\n  outcome: not_reproduced\n  notebook: reproduce_ramachandran_2025.ipynb\n  output: claim:fig5e-rsu-delayed-prf-awake\n  notes: PRF is a significant factor (p = 6e-20 Rep1) but the two highest means are 1500 and 30 Hz\n    (106.7 and 106.6%), and 3000 Hz (102.3%) is below 1500 Hz (corrected p = 0.0053); part (2)\n    fails under both of its readings and both repeat readings. Part (3) needs the sham and was\n    not tested.\n- claim: fig5f-fsu-delayed-prf-awake\n  outcome: not_reproduced\n  notebook: reproduce_ramachandran_2025.ipynb\n  output: claim:fig5f-fsu-delayed-prf-awake\n  notes: PRF is a significant factor (p = 4.6e-12) and 30 Hz differs from 1500, 3000 and 4500 Hz,\n    but the strongest mean is at 30 Hz (103.5%, 4500 Hz 100.3%) and 300 Hz does not differ from\n    4500 Hz (corrected p = 1.0), under both repeat readings. Part (5) needs the sham and was not\n    tested.\n- claim: fig5gh-delayed-prf-anesth\n  outcome: not_reproduced\n  notebook: reproduce_ramachandran_2025.ipynb\n  output: claim:fig5gh-delayed-prf-anesth\n  notes: PRF is not a significant factor for anesthetized delayed responses, Kruskal-Wallis p =\n    0.16 (W1) and 0.12 (W2) for RSU, 0.16 and 0.18 for FSU. The higher PRFs have the higher pooled\n    mean by under one point (RSU 99.97 against 99.15%, FSU 99.87 against 99.35%).\n  deviations:\n  - Two labelled rats where the paper had ten.\n- claim: delayed-anesthesia-factor\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_ramachandran_2025.ipynb\n  output: claim:delayed-anesthesia-factor\n  notes: Without the `_2` repeats (Rep2, adopted), anesthesia is a factor for RSU at p = 4.2e-09 to\n    5.6e-09 and for FSU at p = 0.0013 to 0.0015 under A1/A2 and W1/W2, and the anesthetized mean\n    is lower in both (RSU 99.7 against 104.6%, FSU 99.7 against 101.3%). With the repeats (Rep1)\n    RSU holds (p = 3.6e-06 to 4.3e-06) but FSU gives p = 0.038 to 0.041, which misses the 0.01\n    bound; that reading gives partially reproduced. The question is recorded for the paper's\n    authors.\n  deviations:\n  - Assumed that the paper's analysis did not include the `_2` repeat recordings (Rep2). Methods\n    2.3 describes one recording per parameter set per rat (\"Recordings for a single rat for each\n    set of parameters were completed on the same day\"); the dandiset holds ten awake repeats in\n    BH498, BH506 and BH508 that the paper does not mention.\n  - Anesthetized units from two rats.\n- claim: fig6ad-time-adjacent-batch\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The second batch of five rats recorded awake and anesthetized in the same week, with a\n    sham, is not in the dandiset. Its ten subject folders hold eight rats named in the\n    identifiers, all of which have recordings of the first batch's series, and no file is from a\n    two-PRF or sham protocol.\n- claim: fig6ef-rsu-ispta-rise-then-fall\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_ramachandran_2025.ipynb\n  output: claim:fig6ef-rsu-ispta-rise-then-fall\n  notes: Time-locked RSU means rise from 30 Hz (96.8%) to a peak at 3000 Hz (60.26 mW/cm2,\n    108.2%) and fall at 4500 Hz (99.2%) under W1 Rep1, W2 Rep1 and W2 Rep2; under W1 Rep2 the 300\n    Hz mean (98.2%) is 0.1 point above the 1500 Hz mean (98.1%, SEMs 1.1 and 1.3), so the rise is\n    not monotone. The delayed means do not rise to their peak (106.6% at 30 Hz, 101.2% at 300 Hz,\n    106.7% at 1500 Hz, Rep1). One window holds under W2, the reading adopted.\n  deviations:\n  - Assumed W2, a window measured from the PSTH bins that overlap it, where W1 and W2 give\n    different outcomes under Rep2. Methods 2.4 derives responses from the binned PSTH (\"resulting\n    in a histogram of average spikes per time bin for each neuron\").\n- claim: fig6fh-fsu-ispta\n  outcome: not_reproduced\n  notebook: reproduce_ramachandran_2025.ipynb\n  output: claim:fig6fh-fsu-ispta\n  notes: The time-locked part fails (fig5bd, awake Kruskal-Wallis p = 1.8e-12). Delayed FSU means\n    are 103.5, 98.7, 101.8, 100.6 and 100.3% from 30 to 4500 Hz (Spearman rho = -0.4, Pearson r =\n    -0.27, Rep1; rho = -0.3 Rep2).\n- claim: fig5a-1500-highest-time-locked-mean\n  outcome: not_reproduced\n  notebook: reproduce_ramachandran_2025.ipynb\n  output: claim:fig5a-1500-highest-time-locked-mean\n  notes: The highest mean is at 3000 Hz under every reading (107.7 to 108.7%), significantly above\n    1500 Hz (98.1 to 98.7%; corrected p = 0.0040 or less).\n- claim: fig7a-rsu-time-locked-dc\n  outcome: not_reproduced\n  notebook: reproduce_ramachandran_2025.ipynb\n  output: claim:fig7a-rsu-time-locked-dc\n  notes: The DC effect is significant (Kruskal-Wallis p = 1.5e-22, W1 C1) but 6% is the highest\n    group (180.8%; 60% 147.5%; 30% 90.4 to 98.7%) under every reading. 6% does not differ from 60%\n    (corrected p = 1.0) and is far above 30%. The 6% and 60% responses are largest in BH506 (249.0\n    and 209.9%); BH521 and BH526 give 113 to 121%. Part (3) needs the sham and was not tested.\n  deviations:\n  - The dandiset has no 30% DC recording of its own; the 30% group is the 1500 Hz, 200 us\n    recordings of the PRF series, either of the same rats (C1, BH506 and BH526) or of every rat\n    (C2, with and without repeats). Both give the same outcome here.\n  - The 6% and 60% recordings come from three rats where the paper had ten.\n- claim: fig7a-60-highest-time-locked-mean\n  outcome: not_reproduced\n  notebook: reproduce_ramachandran_2025.ipynb\n  output: claim:fig7a-60-highest-time-locked-mean\n  notes: The highest mean is at 6% under every reading (176.3 to 180.8%; 60% 147.1 to 147.5%), and\n    60% is significantly above 30% (corrected p < 1e-16).\n  deviations:\n  - The 30% group is the PRF series' 1500 Hz, 200 us recordings (C1 or C2), as for fig7a.\n- claim: fig7b-fsu-time-locked-dc\n  outcome: not_reproduced\n  notebook: reproduce_ramachandran_2025.ipynb\n  output: claim:fig7b-fsu-time-locked-dc\n  notes: FSU time-locked responses differ across DC under every reading (Kruskal-Wallis p = 3.5e-12\n    or smaller, all three pairs significant). FSU respond strongly at 6% and 60% (means 156.8 and\n    205.3%, medians 115.0 and 128.6%) and not at 30% (median 100.8%), most in BH506 (338.6 and\n    403.3%).\n  deviations:\n  - The 30% group is the PRF series' 1500 Hz, 200 us recordings (C1 or C2).\n- claim: fig7c-rsu-delayed-dc\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_ramachandran_2025.ipynb\n  output: claim:fig7c-rsu-delayed-dc\n  notes: With the 30% group from the same rats as the 6% and 60% recordings (C1, adopted) the DC\n    effect is not significant (Kruskal-Wallis p = 0.21) and no pair differs. With every awake\n    1500 Hz, 200 us recording as the 30% group (C2) the effect is significant (p = 2.2e-04 Rep1,\n    3.7e-05 Rep2) and 30% is above 6% and 60%, but 6% and 60% do not differ (corrected p =\n    0.071); that reading gives partially reproduced. Part (3) needs the sham and was not tested.\n  deviations:\n  - Assumed C1, the 1500 Hz, 200 us recordings of the rats that have 6% and 60% recordings (BH506,\n    BH526), as the 30% group. Methods 2.3 tests the three TBDs in the same rats (\"We then held PRF\n    constant at 1500 Hz and tested TBD of 40 µs, 200 µs and 400 µs\"); the dandiset has no 30%\n    recording from the DC series.\n- claim: fig7d-fsu-delayed-dc\n  outcome: reproduced\n  notebook: reproduce_ramachandran_2025.ipynb\n  output: claim:fig7d-fsu-delayed-dc\n  notes: Under every reading (C1, C2 Rep1, C2 Rep2) the DC effect is significant (Kruskal-Wallis p\n    = 0.011, 4.5e-07, 1.4e-06) and 60% is above 6% (corrected p = 0.015). The difference is small\n    and both groups are below baseline (99.6% and 98.2%). Part (3), 6% against sham, was not\n    tested.\n  deviations:\n  - No sham recording; part (3) is reported as not tested and the claim is judged on parts (1)\n    and (2), as the claims file's header says for an anesthetized sham.\n  - The 30% group is the PRF series' 1500 Hz, 200 us recordings; it enters only the\n    Kruskal-Wallis.\n- claim: sham-no-auditory-response\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notes: The criterion blocks the claim, as the paper names no test of the sham against baseline.\n    The dandiset also holds no sham recording, so the sham's responses cannot be shown either.\nfindings:\n- kind: data_missing\n  statement: The sham condition and the second batch of five rats (awake and anesthetized\n    recordings in the same week at a low PRF and 1500 Hz) are not in the dandiset. Four claims\n    cannot be tested, and every comparison with sham in the others is left out.\n- kind: data_missing\n  statement: Only part of the first batch is here. The awake PRF series covers seven rats, the\n    anesthetized PRF series three (BH498 at five PRFs, BH512 without 30 Hz, BH521 at three PRFs,\n    unlabelled), and the awake DC series three rats at 6% and 60% only, with no 30% recording of\n    its own. The paper describes ten rats for each series.\n- kind: data_missing\n  statement: The files hold no waveforms, voltage traces or electrode positions, so the cell-type\n    sorting (k-means on the initial phase and after-hyperpolarization durations) cannot be\n    repeated or checked.\n- kind: metadata_error\n  statement: Twelve files are second copies of other recordings. The five anesthetized BH498\n    recordings are deposited under BH498 without labels and under subject folder BH497 with\n    labels; four anesthetized BH512 recordings under BH512 without labels and under BH514 with\n    labels; BH512_1500_200_anes2 is a third copy of the BH512 1500 Hz anesthetized recording,\n    sorted differently. Trial times, per-unit spike counts and first spike times are identical\n    within each pair. The identifiers name BH498 and BH512.\n- kind: metadata_error\n  statement: BH498_30_200 (sub-BH498) and BH508_30_200_2 (sub-BH508) share all 203 trial times\n    and 18,860 spike times; they are one recording sorted twice and filed under two rats.\n- kind: metadata_error\n  statement: The labelled copies of anesthetized recordings (sub-BH497, sub-BH514) are described\n    as \"Awake S1 Stimulation by tFUS\". Every file gives the age P24W, where the paper gives 7, 9\n    and 10 months for the three series. Electrode columns carry placeholder descriptions (\"my\n    description\") and the location \"brain area\".\n- kind: metadata_insufficient\n  statement: The PRF, tone-burst duration and anesthesia state of a recording are coded only in\n    the file's identifier. The `_2` suffix of ten awake recordings and the trial table's\n    stop_time (always 2.2 s after start_time) are not described.\n- kind: metadata_insufficient\n  statement: Fifteen anesthetized files have no cell-type labels, among them all of BH521's and\n    BH512's DC recordings, which cannot enter any cell-type analysis.\n- kind: other\n  statement: Five recordings hold fewer than the 500 trials the Methods describe (203, 238, 328\n    and 339 trials, all from BH508 or the BH498/BH508 duplicate).\n- kind: methods_unavailable\n  statement: Were the `_2` repeat recordings (BH498, BH506, BH508) part of the paper's analysis,\n    and if not, which recording of each pair was? Methods 2.3 describes one recording per\n    parameter set per rat. The FSU part of delayed-anesthesia-factor depends on it (p = 0.0013\n    without the repeats, 0.038 with them); this attempt assumed they were left out.\n- kind: methods_unavailable\n  statement: Which recordings form the 30% DC group of Figure 7? Methods 2.3 describes a DC series\n    at 10 months with TBD 40, 200 and 400 us, and the dandiset holds no 200 us recording from it.\n    With the 1500 Hz, 200 us recordings of the same three rats, fig7c is not reproduced; with\n    those of all rats, it is partially reproduced. This attempt assumed the same rats.\n- kind: methods_unavailable\n  statement: Was a response window that does not fall on the 35.7 ms bin edges (0 to 67 ms, 0.2\n    to 0.7 s) measured from exact spike times or from the PSTH bins that overlap it? It decides\n    fig6ef-rsu-ispta-rise-then-fall without the repeats; this attempt assumed the bins (Methods\n    2.4 derives responses from the binned PSTH).\n"
}
```

```
File created successfully at: attempts/000945-ramachandran-2025-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cat > entries/000945-ramachandran-2025/README.md <<'EOF'
# Ramachandran, Gao, Yttri, Yu & He (2025) from dandiset 000945

Tests the findings of [Ramachandran et al. (2025)](https://doi.org/10.1088/1741-2552/adbb1f) on
[DANDI:000945](https://dandiarchive.org/dandiset/000945/0.250213.2212), the version the paper
cites. The dandiset holds the sorted units and trial times of awake and anesthetized recordings in
rat S1 during transcranial focused ultrasound at five pulse repetition frequencies (PRF) and three
duty cycles (DC), with a cell-type label (RSU or FSU) in most files.

| Claim | Outcome |
|---|---|
| Units sort into 28 FSU and 32 RSU in one animal (Figure 3B) | Partially reproduced |
| RSU respond during stimulation in both states, against sham (Figure 4) | Blocked: data missing |
| FSU delayed onsets are later awake than anesthetized (Figure 4H, 4I) | Not reproduced |
| Awake onset latencies are more spread (Figure 4H) | Not reproduced |
| Awake RSU time-locked responses by PRF (Figure 5A) | Not reproduced |
| Anesthetized RSU time-locked responses by PRF (Figure 5C) | Not reproduced |
| Anesthesia lowers RSU time-locked responses (two-way ANOVA) | Not reproduced |
| FSU time-locked responses do not depend on PRF (Figure 5B, 5D) | Not reproduced |
| Awake RSU delayed responses peak at 1500 and 3000 Hz (Figure 5E) | Not reproduced |
| Awake FSU delayed responses peak at 4500 Hz (Figure 5F) | Not reproduced |
| Anesthetized delayed responses depend on PRF (Figure 5G, 5H) | Not reproduced |
| Anesthesia lowers delayed responses (two-way ANOVA) | Reproduced, on an assumption |
| Time-adjacent second batch (Figure 6A to 6D) | Blocked: data missing |
| RSU responses rise with ISPTA, then fall (Figure 6E, 6G) | Partially reproduced, on an assumption |
| FSU delayed responses rise linearly with ISPTA (Figure 6F, 6H) | Not reproduced |
| 1500 Hz gives the highest RSU time-locked mean (Figure 5A) | Not reproduced |
| RSU time-locked responses by DC (Figure 7A) | Not reproduced |
| 60% DC gives the highest RSU time-locked mean (Figure 7A) | Not reproduced |
| FSU show no time-locked response across DC (Figure 7B) | Not reproduced |
| RSU delayed responses prefer 30% DC (Figure 7C) | Not reproduced, on an assumption |
| FSU delayed responses higher at 60% than 6% DC (Figure 7D) | Reproduced |
| The off-target sham gives no response | Blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The dandiset holds part of the paper's data: the awake PRF series of seven rats, labelled
anesthetized recordings of two, and 6% and 60% DC recordings of three; no sham, no second batch
and no waveforms. Twelve files are second copies of other recordings. The attempt record, with the
reasons and the differences from the paper's method, is
[`attempts/000945-ramachandran-2025-01.yaml`](../../attempts/000945-ramachandran-2025-01.yaml).

- `reproduce_ramachandran_2025.ipynb`: the analysis. It takes about two minutes, most of it
  streaming the files.
- `tfus.py`: loading the files, parsing the condition from the identifier, finding duplicate
  deposits, and the paper's response, group-test and latency measures. Other notebooks on this
  dandiset can import it.
EOF
date -u; time python tools/entry.py all entries/000945-ramachandran-2025 2>&1 | tail -15
```

```
Sat Oct 31 21:46:15 UTC 2026
Installed kernelspec registry-000945-ramachandran-2025 in executed/000945-ramachandran-2025/.venv/share/jupyter/kernels/registry-000945-ramachandran-2025
0 error(s)
pass  reproduce_ramachandran_2025.ipynb  (60 s)

real	1m7.499s
user	0m34.830s
sys	0m6.110s
```

**Agent**

The entry passes check and run (60 s). Comparing the executed copy's outputs with my development run to confirm the conclusions still match.

**Agent calls Bash**

```bash
ls executed/000945-ramachandran-2025/; python3 -c "
import json
nb=json.load(open('executed/000945-ramachandran-2025/reproduce_ramachandran_2025.ipynb'))
for c in nb['cells']:
    if c['cell_type']!='code': continue
    for o in c.get('outputs',[]):
        if 'text' in o: print(''.join(o['text']))
        elif o.get('output_type')=='error': print('ERROR', o['ename'], o['evalue'])
" > $TMPDIR/exec.txt; diff <(grep -v -E "loaded 75|notebook ran" $TMPDIR/out.txt) <(grep -v -E "loaded 75|notebook ran" $TMPDIR/exec.txt) | head -30; grep -n "mean % of baseline" $TMPDIR/exec.txt | cut -c1-200
```

```
reproduce_ramachandran_2025.ipynb
result.json
186,191c186,191
< awake 1500 Hz 400 us RSU: mean % of baseline {'-0.075 to +0.000 s': np.float32(103.6), '+0.000 to +0.075 s': np.float32(146.3), '+0.075 to +0.150 s': np.float32(112.4)} ; peak 159% at 0.0275 s
< awake 1500 Hz 400 us FSU: mean % of baseline {'-0.075 to +0.000 s': np.float32(101.1), '+0.000 to +0.075 s': np.float32(196.9), '+0.075 to +0.150 s': np.float32(115.1)} ; peak 228% at 0.0575 s
< awake 3000 Hz 200 us RSU: mean % of baseline {'-0.075 to +0.000 s': np.float32(101.2), '+0.000 to +0.075 s': np.float32(107.6), '+0.075 to +0.150 s': np.float32(100.3)} ; peak 117% at 0.0225 s
< awake 3000 Hz 200 us FSU: mean % of baseline {'-0.075 to +0.000 s': np.float32(100.6), '+0.000 to +0.075 s': np.float32(106.5), '+0.075 to +0.150 s': np.float32(101.1)} ; peak 110% at 0.0575 s
< anesthetized 1500 Hz 200 us RSU: mean % of baseline {'-0.075 to +0.000 s': np.float32(99.8), '+0.000 to +0.075 s': np.float32(106.2), '+0.075 to +0.150 s': np.float32(100.2)} ; peak 113% at 0.0325 s
< anesthetized 1500 Hz 200 us FSU: mean % of baseline {'-0.075 to +0.000 s': np.float32(100.2), '+0.000 to +0.075 s': np.float32(103.7), '+0.075 to +0.150 s': np.float32(102.2)} ; peak 111% at 0.5875 s
---
> awake 1500 Hz 400 us RSU: mean % of baseline {'-0.075 to +0.000 s': 103.6, '+0.000 to +0.075 s': 146.3, '+0.075 to +0.150 s': 112.4} ; peak 159% at 0.0275 s
> awake 1500 Hz 400 us FSU: mean % of baseline {'-0.075 to +0.000 s': 101.1, '+0.000 to +0.075 s': 196.9, '+0.075 to +0.150 s': 115.1} ; peak 228% at 0.0575 s
> awake 3000 Hz 200 us RSU: mean % of baseline {'-0.075 to +0.000 s': 101.2, '+0.000 to +0.075 s': 107.6, '+0.075 to +0.150 s': 100.3} ; peak 117% at 0.0225 s
> awake 3000 Hz 200 us FSU: mean % of baseline {'-0.075 to +0.000 s': 100.6, '+0.000 to +0.075 s': 106.5, '+0.075 to +0.150 s': 101.1} ; peak 110% at 0.0575 s
> anesthetized 1500 Hz 200 us RSU: mean % of baseline {'-0.075 to +0.000 s': 99.8, '+0.000 to +0.075 s': 106.2, '+0
[... 15 more lines not kept]
```

**Agent**

Identical apart from number formatting. Building the handover.

**Agent calls Bash**

```bash
python tools/entry.py handover entries/000945-ramachandran-2025 2>&1 | tail -5; ls executed/000945-ramachandran-2025/handover; python tools/entry.py check entries/000945-ramachandran-2025 | tail -2; git status --short; date -u
```

```
wrote executed/000945-ramachandran-2025/handover
10.1088-1741-2552-adbb1f.yaml
reproduce_ramachandran_2025.ipynb
tfus.py
0 error(s)
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
?? attempts/000945-ramachandran-2025-01.yaml
?? entries/000945-ramachandran-2025/
?? scripts
Sat Oct 31 21:47:47 UTC 2026
```

**Agent**

I've finished steps 1 to 6 for DANDI:000945. Of the 22 claims, 2 were reproduced, 2 partially reproduced, 15 not reproduced and 3 blocked. The entry passes `check` and its notebook runs clean in 60 s; the handover package is built. Nothing is committed.

### 1. Outcomes

| Claim | Outcome |
|---|---|
| fig3-cell-type-sorting | partially reproduced: two recordings match 28 FSU / 32 RSU / 60 units using the dataset's own labels; the k-means sorting can't be checked (no waveforms) |
| fig4-rsu-time-locked-both-states | blocked, data_missing (no sham) |
| fig4hi-fsu-delayed-latency | not reproduced (p = 0.018 to 0.85; anesthetized mean 0.38 to 0.52 s against 0.24 ± 0.08) |
| fig4h-awake-latency-wider | not reproduced (awake spread is wider in only 10 of 16 readings, by at most 0.02 s) |
| fig5a-rsu-time-locked-prf-awake | not reproduced (peak at 3000 Hz, not 1500 Hz) |
| fig5c-rsu-time-locked-prf-anesth | not reproduced |
| rsu-time-locked-anesthesia-factor | not reproduced (p ≈ 0.011 to 0.018, and anesthesia raises the response) |
| fig5bd-fsu-time-locked-no-prf | not reproduced (FSU do differ across PRF) |
| fig5e, fig5f, fig5gh | not reproduced |
| delayed-anesthesia-factor | reproduced, resting on assumption Rep2 |
| fig6ad-time-adjacent-batch | blocked, data_missing (second batch of rats absent) |
| fig6ef-rsu-ispta-rise-then-fall | partially reproduced, resting on assumption W2 |
| fig6fh, fig5a-1500-highest | not reproduced |
| fig7a, fig7a-60-highest, fig7b | not reproduced (6% and 60% duty cycle give strong time-locked responses, ~150 to 200%, in FSU too) |
| fig7c-rsu-delayed-dc | not reproduced, resting on assumption C1 |
| fig7d-fsu-delayed-dc | reproduced |
| sham-no-auditory-response | blocked, methods_underspecified (as the claims file says), and there is no sham data |

### 2. The dataset, assumptions and questions

**Version.** I pinned 0.250213.2212, the version the paper cites. All five published versions hold the same 75 files.

**What it holds.**
- **Contents.** Spike times, plus a cell-type label in 60 of 75 files. No waveforms or voltage traces, no sham, and none of the second batch of 5 rats.
- **Coverage.** Awake PRF series for 7 rats. Labelled anesthetized recordings for only 2 rats (BH512 has no 30 Hz). Duty-cycle recordings at 6% and 60% for 3 rats, with no 30% recording of their own.
- **Clock.** Trial `start_time` is the ultrasound trigger. Ten recordings show a stimulus-locked response and none does at shifted times; the other 54 can't tell.

**Problems found.**
- **Duplicates.** 12 files are second copies of other recordings:
  - the BH497 and BH514 folders are copies of the BH498 and BH512 anesthetized recordings, the only copies with labels;
  - `BH512_1500_200_anes2` is a third, re-sorted copy;
  - one 30 Hz recording is filed under both BH498 and BH508.
- **Undocumented metadata.** The condition is coded only in the file identifier. The `_2` suffix on 10 repeat recordings and the 2.2 s `stop_time` are not explained.
- **Missing labels.** 15 anesthetized files have no cell-type labels.
- **Metadata errors.** Every file says age P24W (the paper gives 7 to 10 months), the labelled anesthetized copies are described as awake, and electrode fields hold placeholders.
- **Short recordings.** Five recordings hold 203 to 339 trials instead of 500.

**Assumptions (each also recorded as a question for the paper's authors):**
- **Rep2:** the `_2` repeat recordings were left out, since Methods 2.3 describes one recording per condition per rat. This decides the FSU part of delayed-anesthesia-factor (p = 0.0013 without the repeats, 0.038 with them).
- **C1:** the 30% duty-cycle group is the 1500 Hz, 200 µs recordings of the same rats as the 6% and 60% recordings. This decides fig7c (not reproduced under C1, partially under all rats).
- **W2:** a window that doesn't fall on bin edges is measured from the overlapping PSTH bins, since Methods 2.4 builds responses from the binned PSTH. This decides fig6ef.

**Questions to a reader:** none.

### 3. Where the protocol was unclear
1. **A criterion part that can't be tested.** fig3's criterion has no branch for "counts match but the feature part can't be tested". Blocking it would, by the dependency rule, block every claim that uses cell types, although they only need the labels. I recorded it as partially reproduced and explained why.
2. **The sham rule only covers half the case.** The claims file's header says what to do when an anesthetized sham is missing, but not the awake sham. I applied the same rule (judge on the remaining parts) and recorded it as a deviation.
3. **Readings that come from the dataset, not the claims file.** The `_2` repeats and the missing 30% recordings forced choices (Rep1/Rep2, C1/C2) that step 1.6 covers only for gaps in the paper. I ran every reading and adopted one as an assumption.
4. **"Every reading" against "adopt the best reading".** fig4h's criterion requires the result under every reading, while step 1.6 says to adopt the best-supported reading when readings disagree. I followed the criterion.
5. **The "fewer than 500 trials" rule.** The protocol says nothing about recordings that hold fewer trials than the paper describes. I used them as they are and recorded a finding.

### 4. Runtime and failures
The run took about 23 minutes (21:25 to 21:48 UTC), and the notebook runs in 60 s. Nothing failed.

Files are in `entries/000945-ramachandran-2025/`:
- `reproduce_ramachandran_2025.ipynb`
- `tfus.py`
- `README.md`

The attempt record is `attempts/000945-ramachandran-2025-01.yaml`.

## End of run

52 turns, 20 minutes, result: success.
