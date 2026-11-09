# 000019 · author · run 39692741052

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls; ls entries claims attempts paper tools docs
```

```
<persisted-output>
Output too large (31.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/4544e543-8570-4bcd-a333-9e060eca429b/tool-results/bsiy19qhe.txt

Preview (first 2KB):
# Protocol for an attempt

Version: `pilot-10`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
- The **author** tests the claims on the dataset. It reads the paper to
[... 23 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/4544e543-8570-4bcd-a333-9e060eca429b/tool-results/bsiy19qhe.txt"
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-10`. Record this version in the attempt's provenance.
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
18	  claim, and it asks a reader for any method detail the file lacks.
19	- The **verifier** checks the author's work and must not be the author.
20	
[... 778 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md docs/design.md docs/archives.md | head -c 60000
```

```
<persisted-output>
Output too large (36.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/4544e543-8570-4bcd-a333-9e060eca429b/tool-results/bjjhzd5de.txt

Preview (first 2KB):
# Reproduction registry (working name)

Agents, and people, try to reproduce the key findings of papers from the open
data on the [DANDI Archive](https://dandiarchive.org), and register the result
here: the notebooks when it works, and the reason when it does not.

- **For the archive:** evidence of whether each dandiset is complete and
  accurate enough to support the findings of its paper.
- **For analysts:** working notebooks to build new analyses on.

Status: pilot. All eight pilot targets have been attempted and checked by an
independent agent.

**Dashboard:** <https://catalystneuro.github.io/reproduction-registry/>

## Reading the outcomes
[... 24 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/4544e543-8570-4bcd-a333-9e060eca429b/tool-results/bjjhzd5de.txt"
}
```

```
1	# Reproduction registry (working name)
2	
3	Agents, and people, try to reproduce the key findings of papers from the open
4	data on the [DANDI Archive](https://dandiarchive.org), and register the result
5	here: the notebooks when it works, and the reason when it does not.
6	
7	- **For the archive:** evidence of whether each dandiset is complete and
8	  accurate enough to support the findings of its paper.
9	- **For analysts:** working notebooks to build new analyses on.
10	
11	Status: pilot. All eight pilot targets have been attempted and checked by an
12	independent agent.
13	
14	**Dashboard:** <https://catalystneuro.github.io/reproduction-registry/>
15	
16	## Reading the outcomes
17	
18	An outcome says what one attempt could recover from the data in a dandiset,
19	with the methods available to it. **A "not reproduced" or "partially
20	reproduced" outcome is not a finding that the paper is wrong.** It can come
[... 558 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/000019 claims/001453 entries/001453-fouke-2025 questions | head -50; cat claims/000019/*.yaml
```

```
<persisted-output>
Output too large (47.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/4544e543-8570-4bcd-a333-9e060eca429b/tool-results/bz1yiu115.txt

Preview (first 2KB):
claims/000019:
10.1038-nature11911.yaml

claims/001453:
10.1016-j.cub.2025.04.027.yaml

entries/001453-fouke-2025:
README.md
entry.yaml
omr.py
reproduce_fouke_2025.ipynb
requirements.in
requirements.lock.txt

questions:
000005.yaml
[... 32 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/4544e543-8570-4bcd-a333-9e060eca429b/tool-results/bz1yiu115.txt"
}
```

```
1	claims/000019:
2	10.1038-nature11911.yaml
3	
4	claims/001453:
5	10.1016-j.cub.2025.04.027.yaml
6	
7	entries/001453-fouke-2025:
8	README.md
9	entry.yaml
10	omr.py
11	reproduce_fouke_2025.ipynb
12	requirements.in
13	requirements.lock.txt
14	
15	questions:
16	000005.yaml
17	000008.yaml
18	000009.yaml
19	000010.yaml
20	000061.yaml
[... 737 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001453-fouke-2025; cat entry.yaml requirements.in README.md; head -c 6000 omr.py; python -c "
import json;nb=json.load(open('reproduce_fouke_2025.ipynb'))
for c in nb['cells'][:12]: print(c['cell_type'],c.get('metadata'),''.join(c['source'])[:1500]); print('----')
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
[... 349 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -150 attempts/001453-fouke-2025-01.yaml; grep -n "^[a-z]" attempts/001453-fouke-2025-01.yaml; cat questions/README.md; head -40 questions/000005.yaml
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
[... 187 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 150,420p attempts/001453-fouke-2025-01.yaml
```

```
notebook: reproduce_fouke_2025.ipynb
  output: claim:fig1h-zf-higher-angular-acceleration
  notes: With angular acceleration as the Methods define it, DC are higher than ZF for all nine
    stimuli (medians 143 to 191 against 55.4 to 66.4 deg/s2, Kruskal-Wallis p below 0.05/9 for
    each), the reverse of the claim. Per-fish medians, and the files at 128 to 171 Hz alone
    (ZF 84.9, DC 178.6 deg/s2, p = 6.3e-05), give the same. The quantity Fig1-S1.ipynb computes
    gives ZF higher with p below 0.05/9 for 7 of 9 stimuli; it divides the heading change per
    frame by the file's mean frame interval, which in DC files is a median 8.73 times the frame
    interval (ZF 1.37), as DC files hold only trial frames. Part of the DC values may be tracking
    noise. In the 3 s stationary phase the DC median is 205 deg/s2, higher than the 171 during
    motion (per fish median ratio 1.24, p = 0.016), but ZF are also higher at rest (66.9 and 60.8,
    ratio 1.07, p = 0.00012), so this does not separate the species. In frames where the fish is
    still (below 1 mm/s) DC are higher than ZF (per-fish medians 72.4 and 34.9 deg/s2, Mann-Whitney
    p = 0.00014), and DC are higher in every speed band (at 5 mm/s or more, 207 and 85.8). The
    outputs cannot say whether the higher values in moving DC are noise or turning during
    continuous swimming. With the heading from the unwrapped `f0_theta` DC are higher still (218
    to 278 against ZF 61.8 to 77.3 deg/s2, 0 of 9). The reversal should not be read as evidence
    against the paper.
  deviations:
  - Follows the Methods' definition (degrees per second squared) on heading resampled to 30 Hz;
[... 251 more lines not kept]
```

**Agent**

Now the dataset.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/000019/ | python -m json.tool | head -40; curl -s https://api.dandiarchive.org/api/dandisets/000019/versions/ | python -m json.tool
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/000019/versions/0.220126.2148/ > meta.json; python -c "
import json;m=json.load(open('meta.json'))
for k in ['description','citation','relatedResource','assetsSummary','keywords','contributor','license','doi','wasGeneratedBy']: print(k, json.dumps(m.get(k),indent=0)[:2500])
"; curl -s "https://api.dandiarchive.org/api/dandisets/000019/versions/0.220126.2148/assets/?page_size=100" | python -c "
import json,sys;d=json.load(sys.stdin)
for a in d['results']: print(a['asset_id'],a['path'],a['size'])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
python -c "import pynwb, remfile, h5py, dandi; print(pynwb.__version__)"; which uv python; python --version
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pynwb, remfile, h5py, dandi; print(pynwb.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pynwb'
/opt/hostedtoolcache/Python/3.13.16/x64/bin/uv
/opt/hostedtoolcache/Python/3.13.16/x64/bin/python
Python 3.13.16
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q work && . work/bin/activate && uv pip install -q pynwb remfile h5py dandi numpy scipy pandas scikit-learn matplotlib 2>&1 | tail -3; python -c "import pynwb;print(pynwb.__version__)"; echo $TMPDIR
```

```
4.2.0
/tmp/claude-1001
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && cat > probe.py <<'EOF'
import h5py, remfile, sys
from dandi.dandiapi import DandiAPIClient
path=sys.argv[1]
with DandiAPIClient() as c:
    a=c.get_dandiset("000019","0.220126.2148").get_asset_by_path(path)
    url=a.get_content_url(follow_redirects=1, strip_query=True)
print(url)
f=h5py.File(remfile.File(url),'r')
def show(name,obj):
    if isinstance(obj,h5py.Dataset):
        print(name, obj.shape, obj.dtype, dict((k,(v if not hasattr(v,'shape') or v.size<5 else v.shape)) for k,v in obj.attrs.items() if k not in('namespace','object_id')))
    else:
        print(name+'/', dict((k,v) for k,v in obj.attrs.items() if k in ('neurodata_type','description','comments','rate')))
f.visititems(show)
EOF
python probe.py sub-EC2/sub-EC2_ses-EC2-B1.nwb 2>&1 | head -200
```

```
https://dandiarchive.s3.amazonaws.com/blobs/256/1e8/2561e839-2df1-4458-9758-5868f4c82d23
acquisition/ {}
acquisition/ElectricalSeries/ {'comments': 'no comments', 'description': 'all Wav data', 'neurodata_type': 'ElectricalSeries'}
acquisition/ElectricalSeries/data (1974488, 256) float32 {'conversion': np.float64(0.001), 'resolution': np.float64(0.0), 'unit': 'volt'}
acquisition/ElectricalSeries/electrodes (256,) int64 {'description': 'ECoG electrodes on brain', 'help': 'a subset (i.e. slice or region) of a DynamicTable', 'neurodata_type': 'DynamicTableRegion', 'table': <HDF5 object reference>}
acquisition/ElectricalSeries/starting_time () float64 {'rate': np.float64(3051.7578), 'unit': 'Seconds'}
analysis/ {}
file_create_date (1,) object {}
general/ {}
general/devices/ {}
general/devices/L256Grid/ {'neurodata_type': 'Device'}
general/extracellular_ephys/ {}
general/extracellular_ephys/L256Grid electrodes/ {'description': 'L256Grid', 'neurodata_type': 'ElectrodeGroup'}
general/extracellular_ephys/electrodes/ {'description': 'metadata about extracellular electrodes', 'neurodata_type': 'DynamicTable'}
general/extracellular_ephys/electrodes/bad (256,) bool {'description': 'electrode identified as too noisy', 'help': 'Values for a list of elements', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/filtering (256,) object {'description': 'description of hardware filtering', 'help': 'Values for a list of elements', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/group (256,) object {'description': 'a reference to the ElectrodeGroup this electrode is a part of', 'help': 'Values for a list of elements', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/group_name (256,) object {'description': 'the name of the ElectrodeGroup this electrode is a part of', 'help': 'Values for a list of elements', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/id (256,) int64 {'help': 'unique identifiers f
[... 64 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && cat > probe2.py <<'EOF'
import h5py, remfile, sys, numpy as np, collections
from dandi.dandiapi import DandiAPIClient
path=sys.argv[1]
with DandiAPIClient() as c:
    a=c.get_dandiset("000019","0.220126.2148").get_asset_by_path(path)
    url=a.get_content_url(follow_redirects=1, strip_query=True)
f=h5py.File(remfile.File(url),'r')
def s(x): return x.decode() if isinstance(x,bytes) else x
for k in ['identifier','session_description','session_start_time','general/session_id','general/institution','general/lab','general/subject/subject_id','general/subject/species','timestamps_reference_time']:
    print(k, s(f[k][()]))
E=f['general/extracellular_ephys/electrodes']
loc=[s(x) for x in E['location'][:]]
print('locations', collections.Counter(loc))
print('bad', E['bad'][:].sum(), np.where(E['bad'][:])[0])
print('ids', E['id'][:10], E['id'][-3:])
for c in 'xyz': v=E[c][:]; print(c, np.nanmin(v), np.nanmax(v), v[:8])
print('imp', E['imp'][:5], 'filtering', set(s(x) for x in E['filtering'][:]))
ES=f['acquisition/ElectricalSeries/data']; print('chunks', ES.chunks, ES.compression, ES.shape)
print('electrodes region', f['acquisition/ElectricalSeries/electrodes'][:5])
T=f['intervals/trials']
cond=[s(x) for x in T['condition'][:]]
print('n trials', len(cond), 'speak', collections.Counter(T['speak'][:]))
print(collections.Counter(cond).most_common(80))
st,sp,cv=T['start_time'][:],T['stop_time'][:],T['cv_transition_time'][:]
print(np.c_[st[:8],cv[:8],sp[:8]])
print('cv-st', np.percentile(cv-st,[0,50,100]), 'sp-cv', np.percentile(sp-cv,[0,50,100]))
ep=f['intervals/epochs']; print('epochs', [s(x) for x in ep['label'][:]], ep['start_time'][:], ep['stop_time'][:])
iv=f['intervals/invalid_times']; print('invalid', np.c_[iv['start_time'][:], iv['stop_time'][:]], [s(x) for x in iv['tags'][:]])
print('spec freq', f['processing/ecephys/spectrum/frequencies'][[0,1,-1]])
print('dur', ES.shape[0]/3051.7578)
EOF
python probe2.py sub-EC2/sub-EC2_ses-EC2-B1.nwb 2>&1
```

```
identifier EC2_B1
session_description EC2_B1
session_start_time 1900-01-01T08:00:00+00:00
general/session_id EC2_B1
general/institution University of California, San Francisco
general/lab Chang Lab
general/subject/subject_id EC2
general/subject/species Homo sapiens
timestamps_reference_time 1900-01-01T08:00:00+00:00
locations Counter({'superiortemporal': 51, 'postcentral': 44, 'precentral': 44, 'middletemporal': 37, 'supramarginal': 27, 'parsopercularis': 27, 'caudalmiddlefrontal': 26})
bad 0 []
ids [0 1 2 3 4 5 6 7 8 9] [253 254 255]
x -62.637284523534554 -34.5606204546375 [-55.6642956  -58.77371675 -61.28863618 -61.50003911 -61.67092412
 -61.82299338 -61.54322607 -61.12515643]
y -37.47 28.35 [-32.82 -33.13 -33.44 -33.75 -34.06 -34.37 -34.68 -34.99]
z -19.02 53.98 [-19.02       -14.64933333 -10.27866667  -5.908       -1.53733333
   2.83333333   7.204       11.57466667]
imp [nan nan nan nan nan] filtering {'none'}
chunks (15426, 2) gzip (1974488, 256)
electrodes region [0 1 2 3 4]
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && for p in sub-EC9/sub-EC9_ses-EC9-B15.nwb sub-GP31/sub-GP31_ses-GP31-B1.nwb sub-GP33/sub-GP33_ses-GP33-B1.nwb; do echo "=== $p"; python probe2.py $p 2>&1 | grep -v "^\[\|^ \[" ; done
```

```
=== sub-EC9/sub-EC9_ses-EC9-B15.nwb
/tmp/claude-1001/probe2.py:16: RuntimeWarning: All-NaN slice encountered
  for c in 'xyz': v=E[c][:]; print(c, np.nanmin(v), np.nanmax(v), v[:8])
identifier EC9_B15
session_description EC9_B15
session_start_time 1900-01-01T08:00:00+00:00
general/session_id EC9_B15
general/institution University of California, San Francisco
general/lab Chang Lab
general/subject/subject_id EC9
general/subject/species Homo sapiens
timestamps_reference_time 1900-01-01T08:00:00+00:00
locations Counter({'': 177, 'precentral': 41, 'postcentral': 38})
bad 0 []
ids [ 1  2  3  4  5  6  7  8  9 10] [254 255 256]
x nan nan [nan nan nan nan nan nan nan nan]
y nan nan [nan nan nan nan nan nan nan nan]
z nan nan [nan nan nan nan nan nan nan nan]
imp [nan nan nan nan nan] filtering {'none'}
chunks (9299, 4) gzip (595093, 256)
[... 99 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; wc -c *.txt; grep -n -i "EC2\|EC9\|GP3\|EC3[13]\|hemisphere\|256\|baseline\|bad channel\|artifact" 10.1038-nature11911.txt | head -40; pdftotext -v 2>&1 | head -1
```

```
<persisted-output>
Output too large (51.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/4544e543-8570-4bcd-a333-9e060eca429b/tool-results/baf87ezp9.txt

Preview (first 2KB):
94143 10.1038-nature11911.txt
7:Nature Nature 319 nihpa 0410462 Nature 0028-0836 1476-4687 pmc-is-collection-domain yes pmc-collection-title NIHPA Author Manuscripts PMC3606666 PMC3606666.1 3606666 3606666 NIHMS436351 23426266 10.1038/nature11911 NIHMS436351 NIHPA436351 1 Article Functional Organization of Human Sensorimotor Cortex for Speech Articulation Bouchard Kristofer E. 1 2 Mesgarani Nima 1 2 Johnson Keith 3 Chang Edward F. 1 2 4 1 Departments of Neurological Surgery and Physiology, University of California, San Francisco 2 Center for Integrative Neuroscience, University of California, San Francisco 3 Department of Linguistics, University of California, Berkeley 4 UCSF Epilepsy Center, University of California, San Francisco Correspondence and requests for materials should be addressed to E.F.C. ( [removed: an e-mail address] ) 20 2 2013 21 3 2013 495 7441 221018 327 332 24 01 2013 21 09 2013 21 09 2013 11 10 2026 Users may view, print, copy, download and text and data- mine the content in such documents, for the purposes of academic research, subject always to the full Conditions of use: http://www.nature.com/authors/editorial_policies/license.html#terms Speaking is one of the most complex actions we perform, yet nearly all of us learn to do it effortlessly. Production of fluent speech requires the precise, coordinated movement of multiple articulators (e.g., lips, jaw, tongue, larynx) over rapid time scales. Here, we used high-resolution, multi-electrode cortical recordings during the production of consonant-vowel syllables to determine the organization of speech sensorimotor cortex in humans. We found speech articulator representations that were somatotopically arranged on ventral pre- and post-central gyri and parti
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; fold -s -w 200 10.1038-nature11911.txt > $TMPDIR/paper.txt; wc -l $TMPDIR/paper.txt; which pdftotext; pdftotext -layout 10.1038-nature11911.supp.pdf $TMPDIR/supp.txt && wc -l $TMPDIR/supp.txt
```

```
Exit code 127
1034 /tmp/claude-1001/paper.txt
/bin/bash: line 1: pdftotext: command not found
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/paper.txt"
}
```

```
1	DOI: 10.1038/nature11911
2	Version: as served by ncbi_pmc
3	Source: ncbi_pmc+crossref (paper-text-fetcher)
4	Stored: 2026-10-20
5	Extracted: as fetched; with 1 supplement file(s) from the PMC Open Access cloud data (PMC3606666), PDFs extracted with PyMuPDF (dehyphenated, NFKC), Word files with textutil
6	------------------------------------------------------------------------
7	Nature Nature 319 nihpa 0410462 Nature 0028-0836 1476-4687 pmc-is-collection-domain yes pmc-collection-title NIHPA Author Manuscripts PMC3606666 PMC3606666.1 3606666 3606666 NIHMS436351 23426266 
8	10.1038/nature11911 NIHMS436351 NIHPA436351 1 Article Functional Organization of Human Sensorimotor Cortex for Speech Articulation Bouchard Kristofer E. 1 2 Mesgarani Nima 1 2 Johnson Keith 3 Chang 
9	Edward F. 1 2 4 1 Departments of Neurological Surgery and Physiology, University of California, San Francisco 2 Center for Integrative Neuroscience, University of California, San Francisco 3 
10	Department of Linguistics, University of California, Berkeley 4 UCSF Epilepsy Center, University of California, San Francisco Correspondence and requests for materials should be addressed to E.F.C. ( 
11	[removed: an e-mail address] ) 20 2 2013 21 3 2013 495 7441 221018 327 332 24 01 2013 21 09 2013 21 09 2013 11 10 2026 Users may view, print, copy, download and text and data- mine the content in such 
12	documents, for the purposes of academic research, subject always to the full Conditions of use: http://www.nature.com/authors/editorial_policies/license.html#terms Speaking is one of the most complex 
13	actions we perform, yet nearly all of us learn to do it effortlessly. Production of fluent speech requires the precise, coordinated movement of multiple articulators (e.g., lips, jaw, tongue, larynx) 
14	over rapid time scales. Here, we used high-resolution, multi-electrode cortical recordings during the production of consonant-vowel syllables to determine the organization of speech sensorimotor 
15	cortex in
[... 422 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/paper.txt",
 "offset": 437,
 "limit": 600
}
```

```
437	=== page 3 ===
438	 
439	3 
440	 
441	 
442	Supplementary Figure 2.  Spatial topographic organization of articulator representations in 
443	vSMC for individual subjects. 
444	 
445	a-c) Topographic organization of articulator weightings for each subject.  The optimal weighting 
446	assigned to each articulator (Lips, Jaw, Tongue, and Larynx) by the general linear model analysis 
447	presented as a heat map in Cartesian space, defined by distance from Central Sulcus (ordinate) and 
448	Sylvian Fissure (azimuth). Dashed vertical gray line corresponds to the Central Sulcus.   
449	 
450	 
451	 
452	 
453	 
454	 
455	 
456	
[... 579 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && cat > scan.py <<'EOF'
import h5py, remfile, numpy as np, collections, json
from concurrent.futures import ThreadPoolExecutor
from dandi.dandiapi import DandiAPIClient
with DandiAPIClient() as c:
    ds=c.get_dandiset("000019","0.220126.2148")
    assets=sorted((a.path,a.get_content_url(follow_redirects=1, strip_query=True)) for a in ds.get_assets())
def s(x): return x.decode() if isinstance(x,bytes) else x
def one(pu):
    p,u=pu
    f=h5py.File(remfile.File(u),'r')
    E=f['general/extracellular_ephys/electrodes']; T=f['intervals/trials']; ES=f['acquisition/ElectricalSeries']
    d=dict(path=p, n=ES['data'].shape[0], rate=float(ES['starting_time'].attrs['rate']), t0=float(ES['starting_time'][()]),
      bad=np.where(E['bad'][:])[0].tolist(), loc=collections.Counter(s(x) for x in E['location'][:]),
      hascoord=bool(np.isfinite(E['x'][:]).any()), cond=[s(x) for x in T['condition'][:]],
      speak=int(T['speak'][:].sum()), rest=[ (float(a),float(b)) for a,b in zip(f['intervals/epochs/start_time'][:],f['intervals/epochs/stop_time'][:])],
      inval=('invalid_times' in f['intervals']) and len(f['intervals/invalid_times/start_time']),
      ids=E['id'][[0,-1]].tolist(), xsign=float(np.nanmean(E['x'][:])) if np.isfinite(E['x'][:]).any() else None,
      cvmax=float(T['cv_transition_time'][:].max()), stmin=float(T['start_time'][:].min()))
    return d
with ThreadPoolExecutor(8) as ex: res=list(ex.map(one,assets))
json.dump(res,open('scan.json','w'))
for d in res:
    print(d['path'], d['n'], round(d['n']/d['rate'],1), d['rate'], d['t0'], 'bad',d['bad'], 'ntr',len(d['cond']), 'rest',d['rest'], 'inv',d['inval'], d['ids'], d['xsign'], round(d['stmin'],1), round(d['cvmax'],1))
EOF
python scan.py
```

```
sub-EC2/sub-EC2_ses-EC2-B1.nwb 1974488 647.0 3051.7578 0.0 bad [] ntr 387 rest [(593.0, 634.0)] inv 6 [0, 255] -57.09744185944955 4.6 563.9
sub-EC2/sub-EC2_ses-EC2-B105.nwb 2127076 697.0 3051.7578 0.0 bad [] ntr 311 rest [(686.0, 696.0)] inv 5 [0, 255] -57.09744185944955 29.2 684.1
sub-EC2/sub-EC2_ses-EC2-B15.nwb 1754761 575.0 3051.7578 0.0 bad [48, 112, 113, 114, 115, 123, 127] ntr 382 rest [(516.0, 573.0)] inv 7 [0, 255] -57.09744185944955 3.4 473.8
sub-EC2/sub-EC2_ses-EC2-B76.nwb 2050782 672.0 3051.7578 0.0 bad [48, 112, 113, 114, 115, 123, 127, 192, 238, 240] ntr 389 rest [(606.0, 663.0)] inv 28 [0, 255] -57.09744185944955 3.4 594.5
sub-EC2/sub-EC2_ses-EC2-B8.nwb 1834107 601.0 3051.7578 0.0 bad [48, 112, 113, 114, 115, 123, 127] ntr 384 rest [(515.0, 530.0)] inv 4 [0, 255] -57.09744185944955 3.6 508.6
sub-EC2/sub-EC2_ses-EC2-B89.nwb 1831055 600.0 3051.7578 0.0 bad [48, 112, 113, 114, 115, 123, 127, 192, 238, 240] ntr 397 rest [(533.0, 594.0)] inv 11 [0, 255] -57.09744185944955 25.2 500.8
sub-EC2/sub-EC2_ses-EC2-B9.nwb 1724244 565.0 3051.7578 0.0 bad [48, 112, 113, 114, 115, 123, 127, 192, 240] ntr 378 rest [(516.0, 561.0)] inv 13 [0, 255] -57.09744185944955 8.0 499.9
sub-EC9/sub-EC9_ses-EC9-B15.nwb 595093 195.0 3051.7578 0.0 bad [] ntr 70 rest [(0.0, 7.0)] inv 25 [1, 256] None 14.2 183.4
sub-EC9/sub-EC9_ses-EC9-B39.nwb 2859497 937.0 3051.7578 0.0 bad [89] ntr 280 rest [(0.0, 6.0)] inv 12 [1, 256] None 7.2 925.5
sub-EC9/sub-EC9_ses-EC9-B46.nwb 2914429 955.0 3051.7578 0.0 bad [89] ntr 227 rest [(674.0, 684.0)] inv 1 [1, 256] None 26.4 878.3
sub-EC9/sub-EC9_ses-EC9-B49.nwb 2859497 937.0 3051.7578 0.0 bad [89, 244, 245, 255] ntr 254 rest [(642.0, 666.0)] inv False [1, 256] None 29.9 877.4
sub-EC9/sub-EC9_ses-EC9-B53.nwb 2890015 947.0 3051.7578 0.0 bad [64, 65, 66, 89, 255] ntr 274 rest [(318.0, 334.0)] inv 17 [1, 256] None 25.0 928.2
sub-EC9/sub-EC9_ses-EC9-B60.nwb 2911377 954.0 3051.7578 0.0 bad [89, 255] ntr 275 rest [(660.0, 673.0)] inv 9 [1, 256] None 21.5 940.7
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && python -c "
import json,collections
r=json.load(open('scan.json'))
subs=collections.defaultdict(collections.Counter); locs={}
for d in r:
    s=d['path'].split('/')[0]; subs[s].update(d['cond']); locs.setdefault(s,[]).append(d['loc'])
for s,c in subs.items():
    vows=collections.Counter(k[-2:] for k in c)
    cons=sorted(set(k[:-2] for k in c))
    print(s,'trials',sum(c.values()),'distinct',len(c),'cons',len(cons),cons,'vowels',vows)
    print('  min/max per CV',min(c.values()),max(c.values()), sorted(c.items(), key=lambda x:x[1])[:6])
    print('  loc per file identical:', all(l==locs[s][0] for l in locs[s]), locs[s][0])
"
```

```
sub-EC2 trials 2628 distinct 58 cons 19 ['b', 'd', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'sh', 't', 'th', 'v', 'w', 'y', 'z'] vowels Counter({'aa': 19, 'ee': 19, 'oo': 19, 'he': 1})
  min/max per CV 2 58 [('she', 2), ('thee', 10), ('boo', 38), ('moo', 39), ('poo', 40), ('voo', 43)]
  loc per file identical: True {'middletemporal': 37, 'superiortemporal': 51, 'supramarginal': 27, 'postcentral': 44, 'precentral': 44, 'parsopercularis': 27, 'caudalmiddlefrontal': 26}
sub-EC9 trials 1653 distinct 70 cons 24 ['', 'b', 'ch', 'd', 'dh', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'sh', 'sk', 't', 'th', 'v', 'w', 'y', 'z'] vowels Counter({'ee': 23, 'oo': 21, 'aa': 21, 'ya': 1, 'ha': 1, 'ay': 1, 'he': 1, '': 1})
  min/max per CV 1 46 [('skee', 1), ('ya', 1), ('ha', 1), ('kay', 1), ('she', 1), ('chaa', 1)]
  loc per file identical: False {'': 177, 'precentral': 41, 'postcentral': 38}
sub-GP31 trials 5285 distinct 55 cons 19 ['b', 'd', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'sh', 't', 'th', 'v', 'w', 'y', 'z'] vowels Counter({'ee': 19, 'aa': 18, 'oo': 18})
  min/max per CV 2 107 [('thee', 2), ('zaa', 66), ('foo', 66), ('faa', 67), ('fee', 67), ('zoo', 67)]
  loc per file identical: True {'middletemporal': 54, 'superiortemporal': 59, 'supramarginal': 22, 'postcentral': 44, 'precentral': 42, 'parsopercularis': 24, 'caudalmiddlefrontal': 11}
sub-GP33 trials 1458 distinct 58 cons 20 ['', 'b', 'd', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'sh', 't', 'th', 'v', 'w', 'y', 'z'] vowels Counter({'aa': 19, 'ee': 19, 'oo': 19, 'ha': 1})
  min/max per CV 2 28 [('ha', 2), ('koo', 22), ('baa', 23), ('poo', 23), ('see', 23), ('yoo', 24)]
  loc per file identical: True {'caudalmiddlefrontal': 52, 'precentral': 77, 'postcentral': 26, 'parsopercularis': 58, 'superiortemporal': 43}
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && uv pip install -q fsspec aiohttp requests pymupdf && cat > bench.py <<'EOF'
import h5py, remfile, time, numpy as np, fsspec
url="https://dandiarchive.s3.amazonaws.com/blobs/256/1e8/2561e839-2df1-4458-9758-5868f4c82d23"
t=time.time()
f=h5py.File(remfile.File(url),'r'); d=f['acquisition/ElectricalSeries/data']
x=d[:15426*4,:]; print('remfile 20s', time.time()-t, x.nbytes/1e6)
dsid=d.id
t=time.time()
infos=[dsid.get_chunk_info(i) for i in range(0,600)]
print('chunkinfo 600', time.time()-t)
for i in infos[:6]+infos[126:132]: print(i.chunk_offset, i.byte_offset, i.size)
EOF
python bench.py
```

```
remfile 20s 3.664109945297241 63.184896
chunkinfo 600 33.038508892059326
(0, 0) 6080 109205
(0, 2) 115285 111254
(0, 4) 226539 109842
(0, 6) 336381 112539
(0, 8) 448920 113324
(0, 10) 562244 112542
(0, 252) 13838877 109784
(0, 254) 13948661 109636
(15426, 0) 14058297 108976
(15426, 2) 14167273 111940
(15426, 4) 14279213 110118
(15426, 6) 14389331 112668
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && cat > bench2.py <<'EOF'
import h5py, remfile, time, numpy as np, requests, zlib
from concurrent.futures import ThreadPoolExecutor
print(h5py.version.hdf5_version)
url="https://dandiarchive.s3.amazonaws.com/blobs/256/1e8/2561e839-2df1-4458-9758-5868f4c82d23"
t=time.time()
f=h5py.File(remfile.File(url),'r'); d=f['acquisition/ElectricalSeries/data']
info=[]
d.id.chunk_iter(lambda c: info.append((c.chunk_offset, c.byte_offset, c.size, c.filter_mask)))
print('chunk_iter', len(info), time.time()-t)
print(d.id.get_create_plist().get_nfilters(), [d.id.get_create_plist().get_filter(i) for i in range(d.id.get_create_plist().get_nfilters())])
info.sort(key=lambda c:c[1])
# contiguous?
gaps=[info[i+1][1]-(info[i][1]+info[i][2]) for i in range(len(info)-1)]
print('gaps nonzero', sum(g!=0 for g in gaps), min(gaps), max(gaps))
start,end=info[0][1], info[-1][1]+info[-1][2]
print('span MB', (end-start)/1e6)
S=requests.Session()
a=requests.adapters.HTTPAdapter(pool_maxsize=32); S.mount('https://',a)
def get(r):
    resp=S.get(url, headers={'Range':f'bytes={r[0]}-{r[1]-1}'}); return resp.content
blk=32*2**20
ranges=[(s,min(s+blk,end)) for s in range(start,start+blk*24,blk)]
for nt in (8,16):
    t=time.time()
    with ThreadPoolExecutor(nt) as ex: out=list(ex.map(get,ranges))
    dt=time.time()-t; print(nt,'threads', sum(map(len,out))/1e6/dt,'MB/s')
buf=out[0]
t=time.time(); n=0
for c in info:
    if c[1]+c[2]>start+blk: break
    raw=zlib.decompress(buf[c[1]-start:c[1]-start+c[2]]); n+=len(raw)
print('decompress MB/s', n/1e6/(time.time()-t))
EOF
python bench2.py
```

```
2.0.0
chunk_iter 16384 32.17613935470581
1 [(1, 1, (4,), b'deflate')]
gaps nonzero 288 0 7848
span MB 1797.849022
8 threads 339.25540182969854 MB/s
16 threads 402.96282993908636 MB/s
decompress MB/s 290.0424280360975
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && python -c "import remfile,inspect;print(inspect.signature(remfile.File.__init__))" && cat > bench3.py <<'EOF'
import h5py, time, fsspec, remfile
url="https://dandiarchive.s3.amazonaws.com/blobs/256/1e8/2561e839-2df1-4458-9758-5868f4c82d23"
for bs in (2**20, 8*2**20):
    t=time.time()
    fs=fsspec.filesystem('http')
    fo=fs.open(url,'rb',block_size=bs,cache_type='blockcache', cache_options={'maxblocks':4096})
    f=h5py.File(fo,'r'); d=f['acquisition/ElectricalSeries/data']
    info=[]
    d.id.chunk_iter(lambda c: info.append(c.byte_offset))
    print('fsspec blockcache',bs, len(info), time.time()-t)
t=time.time()
f=h5py.File(remfile.File(url, min_chunk_size=8*2**20) if 'min_chunk_size' in str(__import__('inspect').signature(remfile.File.__init__)) else remfile.File(url),'r')
d=f['acquisition/ElectricalSeries/data']; info=[]
d.id.chunk_iter(lambda c: info.append(c.byte_offset)); print('remfile', time.time()-t)
EOF
python bench3.py
```

```
Exit code 1
(self, url: Union[str, Any], *, verbose: bool = False, disk_cache: Optional[remfile.DiskCache.DiskCache] = None, _min_chunk_size: int = 102400, _max_cache_size: int = 1000000000.0, _chunk_increment_factor: int = 1.7, _bytes_per_thread: int = 4194304, _max_threads: int = 1, _max_chunk_size: int = 104857600, _impose_request_failures_for_testing: bool = False, _size: Optional[int] = None, _use_session: bool = True)
fsspec blockcache 1048576 16384 32.44215440750122
fsspec blockcache 8388608 16384 44.64584970474243
Traceback (most recent call last):
  File "/tmp/claude-1001/bench3.py", line 12, in <module>
    f=h5py.File(remfile.File(url, min_chunk_size=8*2**20) if 'min_chunk_size' in str(__import__('inspect').signature(remfile.File.__init__)) else remfile.File(url),'r')
                ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: RemFile.__init__() got an unexpected keyword argument 'min_chunk_size'. Did you mean '_min_chunk_size'?
```

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && python -c "
import fitz
d=fitz.open('paper/10.1038-nature11911.supp.pdf')
print(len(d))
for p in (1,14):
    pg=d[p]; pix=pg.get_pixmap(dpi=150); pix.save(f'page{p+1}.png'); print(pg.rect)
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/page2.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && python -c "
import fitz
d=fitz.open('paper/10.1038-nature11911.supp.pdf')
pg=d[1]
clip=fitz.Rect(50,280,480,365)
pg.get_pixmap(dpi=400,clip=clip).save('matrix1.png')
print([ (i[0], i[1]) for i in pg.get_images()][:5])
" 2>/dev/null
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/matrix1.png"
}
```

Result: no output.

## Prompt

[Image: original 2390x473, displayed at 2000x396. Multiply coordinates by 1.20 to map to original image.]

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && python -c "
from PIL import Image; import numpy as np
im=np.asarray(Image.open('matrix1.png').convert('RGB')).astype(float)
g=im.mean(2)
# find grid lines: dark grey columns in row band
H,W=g.shape; print(H,W)
band=g[130:370]
dark=(band<140).mean(0)
xs=np.where(dark>0.9)[0]; print(xs[:10], xs[-10:])
rowband=g[:, 600:610].mean(1); print([ (i,int(v)) for i,v in enumerate(rowband) if v<150][:80])
" 2>&1 | tail -5
```

```
473 2390
[218 222 223] [218 222 223]
[(50, 148), (51, 145), (69, 148), (70, 143), (71, 143), (85, 99), (86, 31), (87, 0), (88, 0), (89, 9), (90, 71), (104, 65), (105, 72), (106, 118), (107, 125), (108, 140), (109, 57), (110, 18), (111, 18), (112, 18), (113, 18), (114, 18), (115, 18), (116, 18), (117, 18), (118, 18), (119, 18), (120, 18), (121, 18), (122, 18), (123, 18), (124, 18), (125, 18), (126, 18), (127, 18), (128, 18), (129, 18), (130, 18), (131, 18), (132, 18), (133, 18), (134, 18), (135, 18), (136, 18), (137, 18), (138, 18), (139, 18), (140, 18), (141, 18), (142, 18), (143, 18), (144, 18), (145, 18), (146, 18), (147, 18), (148, 18), (149, 34), (150, 87), (151, 125), (152, 122), (153, 105), (195, 144), (196, 125), (197, 132), (240, 137), (241, 125), (242, 125), (243, 60), (244, 18), (245, 18), (246, 18), (247, 18), (248, 18), (249, 18), (250, 18), (251, 18), (252, 18), (253, 18), (254, 18), (255, 18)]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && python -c "
from PIL import Image; import numpy as np
im=np.asarray(Image.open('matrix1.png').convert('RGB')).astype(float); g=im.mean(2)
# refine right edge: last dark vertical line
col=(g[150:350]<150).mean(0); xs=np.where(col>0.8)[0]; print('vlines',xs.min(),xs.max(), len(xs))
row=(g[:,300:2200]<150).mean(1); ys=np.where(row>0.8)[0]; print('hlines',ys)
"
```

```
vlines 218 2302 167
hlines [ 89  90 104 105 106 107 108 109 110 151 152 153 195 196 197 240 241 242
 285 286 287 331 376]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && python -c "
from PIL import Image; import numpy as np
im=np.asarray(Image.open('matrix1.png').convert('RGB')).astype(float); g=im.mean(2)
L,R=220,2304; T,B=108,377
cw=(R-L)/57; rh=(B-T)/6
cons='b d f g h k l m n p r s sh t th v w y z'.split()
names=['Lips','Tongue','Larynx','Jaw','Back','High']
M=np.zeros((6,57)); S=np.zeros((6,57))
for r in range(6):
  for c in range(57):
    x=int(L+(c+.5)*cw); y=int(T+(r+.5)*rh)
    p=im[y-6:y+6,x-6:x+6].reshape(-1,3); M[r,c]=p.mean(); S[r,c]=p.std(0).mean()+abs(p[:,0]-p[:,2]).mean()
for r in range(6):
  print(f'{names[r]:7s}', ' '.join(''.join('1' if M[r,3*i+v]>120 else '0' for v in range(3)) for i in range(19)))
print('        ', ' '.join(f'{c:3s}' for c in cons))
print('sat cols', [c for c in range(57) if S[:,c].mean()>20])
print(np.round(M[:, :6]))
"
```

```
Lips    111 000 111 000 000 000 000 111 000 111 000 000 000 000 000 111 111 000 000
Tongue  000 111 000 111 000 111 111 000 111 000 111 111 111 111 111 000 111 111 111
Larynx  111 111 000 111 000 000 111 111 111 000 111 000 000 000 000 111 111 111 111
Jaw     111 111 111 000 000 000 111 111 111 111 111 111 111 111 111 111 111 111 111
Back    101 101 101 101 101 101 101 101 101 101 101 101 101 101 101 101 101 101 101
High    011 011 011 011 011 011 011 011 011 011 011 011 011 011 011 011 011 011 011
         b   d   f   g   h   k   l   m   n   p   r   s   sh  t   th  v   w   y   z  
sat cols [0, 28, 35]
[[202. 201. 201.  19.  19.  19.]
 [114.  19.  19. 201. 201. 201.]
 [202. 201. 201. 201. 201. 201.]
 [202. 201. 201. 201. 201. 201.]
 [213.  28. 228. 228.  28. 228.]
 [113. 228. 228.  28. 228. 228.]]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && python -c "
import fitz
d=fitz.open('paper/10.1038-nature11911.supp.pdf')
pg=d[14]; pg.get_pixmap(dpi=100).save('page15.png')
" 2>/dev/null
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/page15.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && python -c "
import fitz
d=fitz.open('paper/10.1038-nature11911.supp.pdf')
pg=d[14]; pg.get_pixmap(dpi=500,clip=fitz.Rect(100,125,570,285)).save('feat.png')
from PIL import Image; import numpy as np
im=np.asarray(Image.open('feat.png').convert('L')).astype(float); print(im.shape)
" 2>/dev/null
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/feat.png"
}
```

Result: no output.

**Message**

[Image: original 3265x1112, displayed at 2000x681. Multiply coordinates by 1.63 to map to original image.]

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && python -c "
from PIL import Image; import numpy as np
g=np.asarray(Image.open('feat.png').convert('L')).astype(float)
L,R,T,B=62,3167,49,1069
# refine with dark/edge detection: find outer border columns
col=(g[100:1000]<200).mean(0); print('first dark cols', np.where(col>0.95)[0][:5], np.where(col>0.95)[0][-5:])
cw=(R-L)/57; rh=(B-T)/19
cons='b d f g h k l m n p r s sh t th v w y z'.split()
names='Bilabial SecLabial Labiodental Dental Alveolar PostAlv Velar Voiced Mandibular OralStop Fricative Approx Nasal Lateral Rhotic Back High Round JawOpen'.split()
for r in range(19):
  vals=[]
  for c in range(57):
    x=int(L+(c+.5)*cw); y=int(T+(r+.5)*rh); vals.append(np.median(g[y-8:y+8,x-8:x+8])>128)
  print(f'{names[r]:11s}', ' '.join(''.join('1' if vals[3*i+v] else '0' for v in range(3)) for i in range(19)))
print(' '*11, ' '.join(f'{c:3s}' for c in cons))
"
```

```
first dark cols [56 57 58 59 60] [3164 3165 3166 3167 3168]
Bilabial    111 000 000 000 000 000 000 111 000 111 000 000 000 000 000 000 111 000 000
SecLabial   000 000 000 000 000 000 000 000 000 000 111 000 111 000 000 000 000 000 000
Labiodental 000 000 111 000 000 000 000 000 000 000 000 000 000 000 000 111 000 000 000
Dental      000 000 000 000 000 000 000 000 000 000 000 000 000 000 111 000 000 000 000
Alveolar    000 111 000 000 000 000 111 000 111 000 000 111 000 111 000 000 000 000 111
PostAlv     000 000 000 000 000 000 000 000 000 000 111 000 111 000 000 000 000 111 000
Velar       000 000 000 111 000 111 000 000 000 000 000 000 000 000 000 000 111 000 000
Voiced      111 111 000 111 000 000 111 111 111 000 111 000 000 000 000 111 111 111 111
Mandibular  111 111 111 000 000 000 111 111 111 111 111 111 111 111 111 111 111 111 111
OralStop    111 111 000 111 000 111 000 111 111 111 000 000 000 111 000 000 000 000 000
Fricative   000 000 111 000 000 000 000 000 000 000 000 111 111 000 111 111 000 000 111
Approx      000 000 000 000 000 000 000 000 000 000 111 000 000 000 000 000 111 111 000
Nasal       000 000 000 000 000 000 000 111 111 000 000 000 000 000 000 000 000 000 000
Lateral     000 000 000 000 000 000 111 000 000 000 000 000 000 000 000 000 000 000 000
Rhotic      000 000 000 000 000 000 000 000 000 000 111 000 000 000 000 000 000 000 000
Back        101 101 101 101 101 101 101 101 101 101 101 101 101 101 101 101 101 101 101
High        011 011 011 011 011 011 011 011 011 011 011 011 011 011 011 011 011 011 011
Round       001 001 001 001 001 001 001 001 001 001 001 001 001 001 001 001 001 001 001
JawOpen     100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,80p tools/entry.py; grep -n "def \|embedded\|literal\|MAX\|limit" tools/entry.py | head -60
```

```
"""Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
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
- each notebook has a cell tagged `sanity` that prints what was loaded;
[... 80 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p entries/000019-bouchard-2013 && free -g && nproc
```

```
total        used        free      shared  buff/cache   available
Mem:              15           1           9           0           5          13
Swap:              2           0           2
4
```

**Agent calls Write**

```json
{
 "file_path": "entries/000019-bouchard-2013/bouchard.py",
 "content": "\"\"\"Loading, high gamma and shared measures for dandiset 000019 (Bouchard et al. 2013).\n\nBouchard KE, Mesgarani N, Johnson K, Chang EF (2013). Functional organization of human\nsensorimotor cortex for speech articulation. Nature 495, 327-332. doi:10.1038/nature11911.\n\nThe dandiset holds, per recording block, raw ECoG from a 256-channel grid at 3051.76 Hz, a trial\ntable (syllable spoken, start, consonant-to-vowel transition and stop times), a `bad` flag per\nelectrode, an anatomical label per electrode, and a rest period. It has no audio and no high gamma,\nso high gamma is computed here from the raw voltage.\n\nFiles are streamed from the archive at the pinned version: each file's bytes are fetched into\nmemory with parallel HTTP range requests and opened with h5py from memory. Nothing is written to\ndisk. The files are 0.6 to 2.8 GB and every sample is needed (common average reference over all\ngood channels, and trials cover the whole block), so reading the whole file in large requests is\nmuch faster than h5py's chunk-by-chunk reads over the network.\n\nWhere the parameters come from:\n\n- Bad channels are the dataset's `bad` flags; the claims file's header says to use them. The\n  common average reference is over the remaining channels (Methods, via the claims header).\n- High gamma: eight Gaussian band-pass filters with centres log-spaced from 85 to 175 Hz (Methods)\n  and standard deviations 0.39 * sqrt(centre) Hz, which grow semi-logarithmically. The paper gives\n  no widths; the claims header calls the bank of Mesgarani and Chang (2012) the standard choice,\n  and this form is the one used in the Chang lab's published preprocessing code. It is a standard\n  choice that is not expected to change an outcome. The analytic amplitude is taken in the\n  frequency domain (filter, keep positive frequencies, inverse transform), which is the Hilbert\n  transform of the filtered signal. The inverse transform is taken on the bins below 400 Hz, which\n  gives the amplitude sampled at about 400 Hz without aliasing (the filters fall to zero well below\n  400 Hz); this is a computational shortcut, not a change of method. The mean amplitude over the\n  eight bands is interpolated onto a 200 Hz grid (5 ms steps, Methods).\n- z-scoring per channel against baseline data (Methods). The claims file leaves the baseline open\n  and names two readings, both computed: `pre`, the 500 ms windows from -1000 to -500 ms before each\n  C-V transition, pooled over the block's trials; `whole`, the whole block. The dataset's rest\n  period (`rest`) is computed as a variant only. Statistics are per block and channel.\n- Epoch -500 to +750 ms around the C-V transition (claims header), 251 samples at 5 ms.\n- Syllable labels: the dataset spells syllables as consonant + `aa`, `ee` or `oo` (/a/, /i/, /u/),\n  and /j/ as `y`. Two labels differ only in spelling (`she` for `shee`, `ha` for `haa`) and are\n  merged. Labels with no consonant (vowels alone) are not CV syllables and are left out.\n- The articulator state matrix (Supplementary Figure 1d) and the phonetic feature matrix\n  (Supplementary Figure 12) are given only as figures in the supplement; they are transcribed\n  below from the supplement PDF (light cells 1, dark cells 0 in Supplementary Figure 1d, whose\n  /b/ row has Lips light and Tongue dark; white 1 and black 0 in Supplementary Figure 12, as its\n  legend says). They are the paper's definitions of its variables, not data.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport io\nimport re\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport h5py\nimport numpy as np\nimport requests\nimport scipy.fft\nfrom dandi.dandiapi import DandiAPIClient\n\nDANDISET_ID = \"000019\"\nDANDISET_VERSION = \"0.220126.2148\"\nSUBJECTS = [\"EC2\", \"GP31\", \"GP33\"]   # EC9 is in the dandiset but not in the paper\n\nHG_CENTRES = np.logspace(np.log10(85.0), np.log10(175.0), 8)\nHG_SDS = 10 ** (np.log10(0.39) + 0.5 * np.log10(HG_CENTRES))\nENVELOPE_HZ = 400.0\nHG_HZ = 200.0\nEPOCH_MS = np.arange(-500, 751, 5)          # analysis epoch\nPRE_MS = (-1000, -500)                      # baseline reading `pre`\nBASELINES = (\"pre\", \"whole\", \"rest\")\nVSMC_LABELS = (\"precentral\", \"postcentral\")\n\nCONSONANTS = [\"b\", \"d\", \"f\", \"g\", \"h\", \"k\", \"l\", \"m\", \"n\", \"p\", \"r\", \"s\", \"sh\", \"t\", \"th\", \"v\",\n              \"w\", \"y\", \"z\"]\nVOWELS = {\"aa\": \"a\", \"ee\": \"i\", \"oo\": \"u\"}\nSPELLING = {\"she\": \"shee\", \"ha\": \"haa\"}\n\n# Supplementary Figure 1d, consonant part: one string per articulator, one digit per consonant\n# in the order of CONSONANTS (the figure's three vowel columns of a consonant are identical).\nARTICULATORS = [\"Lips\", \"Tongue\", \"Larynx\", \"Jaw\"]\n_ARTIC_ROWS = {\n    \"Lips\":   \"1010000101000001100\",\n    \"Tongue\": \"0101011010111110111\",\n    \"Larynx\": \"1101001110100001111\",\n    \"Jaw\":    \"1110001111111111111\",\n}\n# Vowel part of Supplementary Figure 1d.\nVOWEL_ARTICULATORS = [\"Back Tongue\", \"High Tongue\"]\n_VOWEL_ROWS = {\"Back Tongue\": {\"a\": 1, \"i\": 0, \"u\": 1}, \"High Tongue\": {\"a\": 0, \"i\": 1, \"u\": 1}}\n\n# Supplementary Figure 12: nine constriction location, six degree/shape and four vowel features.\nLOCATION = [\"Bilabial\", \"Secondary Labial\", \"Labiodental\", \"Dental\", \"Alveolar\", \"Post Alveolar\",\n            \"Velar\", \"Voiced\", \"Mandibular\"]\nDEGREE = [\"Oral Stop\", \"Fricative\", \"Approximate\", \"Nasal Stop\", \"Lateral\", \"Rhotic\"]\nVOWEL_FEATURES = [\"Back Tongue\", \"High Tongue\", \"Lip Rounding\", \"Jaw Open\"]\n_FEATURE_ROWS = {\n    \"Bilabial\":         \"1000000101000000100\",\n    \"Secondary Labial\": \"0000000000101000000\",\n    \"Labiodental\":      \"0010000000000001000\",\n    \"Dental\":           \"0000000000000010000\",\n    \"Alveolar\":         \"0100001010010100001\",\n    \"Post Alveolar\":    \"0000000000101000010\",\n    \"Velar\":            \"0001010000000000100\",\n    \"Voiced\":           \"1101001110100001111\",\n    \"Mandibular\":       \"1110001111111111111\",\n    \"Oral Stop\":        \"1101010111000100000\",\n    \"Fricative\":        \"0010000000011011001\",\n    \"Approximate\":      \"0000000000100000110\",\n    \"Nasal Stop\":       \"0000000110000000000\",\n    \"Lateral\":          \"0000001000000000000\",\n    \"Rhotic\":           \"0000000000100000000\",\n}\n_VOWEL_FEATURE_ROWS = {\"Back Tongue\": {\"a\": 1, \"i\": 0, \"u\": 1}, \"High Tongue\": {\"a\": 0, \"i\": 1, \"u\": 1},\n                       \"Lip Rounding\": {\"a\": 0, \"i\": 0, \"u\": 1}, \"Jaw Open\": {\"a\": 1, \"i\": 0, \"u\": 0}}\n\n# Major oral articulator of each consonant, read from the constriction location features\n# (claims header). Reading (a) leaves /h/, /r/, /w/ and /j/ out; reading (b) puts /r/ with the\n# coronal, /w/ with the labial and /j/ with the dorsal consonants, and leaves /h/ out.\n_MAJOR_A = {\"labial\": [\"b\", \"p\", \"m\", \"f\", \"v\"],\n            \"coronal\": [\"d\", \"t\", \"n\", \"l\", \"s\", \"z\", \"th\", \"sh\"],\n            \"dorsal\": [\"g\", \"k\"]}\nMAJOR = {\"a\": {c: k for k, cs in _MAJOR_A.items() for c in cs}}\nMAJOR[\"b\"] = {**MAJOR[\"a\"], \"r\": \"coronal\", \"w\": \"labial\", \"y\": \"dorsal\"}\nSIBILANTS = [\"s\", \"z\", \"sh\"]   # Fig. 5a legend groups: labial, coronal tongue, dorsal tongue, sibilant\n\n\ndef parse_label(label: str) -> tuple[str, str] | None:\n    \"\"\"(consonant, vowel) of a trial label, or None if it is not a CV syllable of the task.\"\"\"\n    label = SPELLING.get(label, label)\n    m = re.fullmatch(r\"([a-z]*?)(aa|ee|oo)\", label)\n    if not m or m.group(1) not in CONSONANTS:\n        return None\n    return m.group(1), VOWELS[m.group(2)]\n\n\ndef articulator_matrix(cvs: list[tuple[str, str]]) -> np.ndarray:\n    \"\"\"(n CV, 6) binary matrix: Lips, Tongue, Larynx, Jaw, Back Tongue, High Tongue.\"\"\"\n    rows = []\n    for c, v in cvs:\n        i = CONSONANTS.index(c)\n        rows.append([int(_ARTIC_ROWS[a][i]) for a in ARTICULATORS]\n                    + [_VOWEL_ROWS[a][v] for a in VOWEL_ARTICULATORS])\n    return np.array(rows, dtype=float)\n\n\ndef feature_matrix(cvs: list[tuple[str, str]], which: str) -> np.ndarray:\n    \"\"\"Phonetic features of each CV: `location`, `degree` or `vowel` (Supplementary Figure 12).\"\"\"\n    rows = []\n    for c, v in cvs:\n        i = CONSONANTS.index(c)\n        if which == \"vowel\":\n            rows.append([_VOWEL_FEATURE_ROWS[f][v] for f in VOWEL_FEATURES])\n        else:\n            names = LOCATION if which == \"location\" else DEGREE\n            rows.append([int(_FEATURE_ROWS[f][i]) for f in names])\n    return np.array(rows, dtype=float)\n\n\n# ----------------------------------------------------------------------------------------------\n# Reading the archive\n\ndef assets() -> list[dict]:\n    \"\"\"Path, size and streaming URL of every file at the pinned version.\"\"\"\n    with DandiAPIClient() as client:\n        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)\n        return sorted(({\"path\": a.path, \"size\": a.size,\n                        \"url\": a.get_content_url(follow_redirects=1, strip_query=True)}\n                       for a in ds.get_assets()), key=lambda a: a[\"path\"])\n\n\ndef dandiset_metadata() -> dict:\n    with DandiAPIClient() as client:\n        return client.get_dandiset(DANDISET_ID, DANDISET_VERSION).get_raw_metadata()\n\n\n_session = requests.Session()\n_session.mount(\"https://\", requests.adapters.HTTPAdapter(pool_maxsize=32))\n\n\ndef fetch(url: str, size: int, block: int = 32 * 2**20, threads: int = 16) -> bytes:\n    \"\"\"The whole file, into memory, by parallel range requests.\"\"\"\n    ranges = [(s, min(s + block, size) - 1) for s in range(0, size, block)]\n\n    def get(r):\n        for attempt in range(5):\n            try:\n                resp = _session.get(url, headers={\"Range\": f\"bytes={r[0]}-{r[1]}\"}, timeout=120)\n                resp.raise_for_status()\n                if len(resp.content) == r[1] - r[0] + 1:\n                    return resp.content\n            except requests.RequestException:\n                if attempt == 4:\n                    raise\n        raise OSError(f\"short read of {url} at {r}\")\n\n    buf = bytearray(size)\n    with ThreadPoolExecutor(threads) as ex:\n        for (s, e), part in zip(ranges, ex.map(get, ranges)):\n            buf[s:e + 1] = part\n    return bytes(buf)\n\n\ndef _text(x):\n    return x.decode() if isinstance(x, bytes) else str(x)\n\n\ndef read_metadata(h5: h5py.File) -> dict:\n    \"\"\"Everything but the voltage: electrodes, trials, rest period, invalid times.\"\"\"\n    E = h5[\"general/extracellular_ephys/electrodes\"]\n    T = h5[\"intervals/trials\"]\n    ES = h5[\"acquisition/ElectricalSeries\"]\n    meta = {\n        \"subject\": _text(h5[\"general/subject/subject_id\"][()]),\n        \"session\": _text(h5[\"general/session_id\"][()]),\n        \"rate\": float(ES[\"starting_time\"].attrs[\"rate\"]),\n        \"t0\": float(ES[\"starting_time\"][()]),\n        \"n_samples\": ES[\"data\"].shape[0],\n        \"n_channels\": ES[\"data\"].shape[1],\n        \"unit\": _text(ES[\"data\"].attrs[\"unit\"]),\n        \"conversion\": float(ES[\"data\"].attrs[\"conversion\"]),\n        \"electrode_ids\": E[\"id\"][:],\n        \"location\": np.array([_text(x) for x in E[\"location\"][:]]),\n        \"bad\": E[\"bad\"][:].astype(bool),\n        \"x\": E[\"x\"][:], \"y\": E[\"y\"][:], \"z\": E[\"z\"][:],\n        \"condition\": np.array([_text(x) for x in T[\"condition\"][:]]),\n        \"speak\": T[\"speak\"][:],\n        \"start\": T[\"start_time\"][:], \"stop\": T[\"stop_time\"][:], \"cv\": T[\"cv_transition_time\"][:],\n        \"rest\": [(float(a), float(b)) for a, b in zip(h5[\"intervals/epochs/start_time\"][:],\n                                                    h5[\"intervals/epochs/stop_time\"][:])],\n        \"rest_labels\": [_text(x) for x in h5[\"intervals/epochs/label\"][:]],\n    }\n    if \"invalid_times\" in h5[\"intervals\"]:\n        I = h5[\"intervals/invalid_times\"]\n        meta[\"invalid\"] = np.c_[I[\"start_time\"][:], I[\"stop_time\"][:]]\n    else:\n        meta[\"invalid\"] = np.zeros((0, 2))\n    return meta\n\n\n# ----------------------------------------------------------------------------------------------\n# High gamma\n\ndef high_gamma(raw: np.ndarray, rate: float, good: np.ndarray, batch: int = 32) -> tuple[np.ndarray, float]:\n    \"\"\"High-gamma amplitude of every good channel, sampled at about 400 Hz.\n\n    raw is (samples, channels). Returns (envelope, envelope_rate); bad channels are NaN.\n    \"\"\"\n    n, nch = raw.shape\n    car = raw[:, good].mean(axis=1, dtype=np.float64).astype(np.float32)\n    freqs = np.fft.rfftfreq(n, 1.0 / rate)\n    k = int(np.ceil(n * ENVELOPE_HZ / rate))\n    gauss = np.exp(-0.5 * ((freqs[:k, None] - HG_CENTRES[None, :]) / HG_SDS[None, :]) ** 2)\n    env = np.full((k, nch), np.nan, dtype=np.float32)\n    idx = np.where(good)[0]\n    for s in range(0, len(idx), batch):\n        ch = idx[s:s + batch]\n        x = raw[:, ch] - car[:, None]\n        X = scipy.fft.rfft(x, axis=0, workers=4)[:k]\n        acc = np.zeros((k, len(ch)), dtype=np.float32)\n        for b in range(len(HG_CENTRES)):\n            acc += np.abs(scipy.fft.ifft(X * gauss[:, b:b + 1].astype(np.float32), axis=0, workers=4))\n        env[:, ch] = acc / len(HG_CENTRES)\n    return env, k * rate / n\n\n\ndef resample_to(env: np.ndarray, env_rate: float, times: np.ndarray) -> np.ndarray:\n    \"\"\"Linear interpolation of the envelope (samples, channels) at the given times (s).\"\"\"\n    pos = np.clip(times * env_rate, 0, env.shape[0] - 1.000001)\n    i0 = np.floor(pos).astype(int)\n    w = (pos - i0).astype(np.float32)\n    shape = times.shape + (env.shape[1],)\n    a = env[i0.ravel()].reshape(shape)\n    b = env[(i0 + 1).ravel()].reshape(shape)\n    return a + (b - a) * w[..., None]\n\n\ndef process_block(asset: dict) -> dict:\n    \"\"\"One block: metadata, and per trial the z-scored high gamma in the epoch, per baseline.\n\n    Returns metadata plus `epochs[baseline]` (trials, channels, 251) float32 for the trials whose\n    window from -1000 to +750 ms lies inside the recording, `kept` (their trial indices), and\n    `hg_stats` (per-channel baseline mean and SD of the 200 Hz high gamma, per baseline).\n    \"\"\"\n    buf = fetch(asset[\"url\"], asset[\"size\"])\n    with h5py.File(io.BytesIO(buf), \"r\") as h5:\n        meta = read_metadata(h5)\n        raw = h5[\"acquisition/ElectricalSeries/data\"][:]\n    del buf\n    good = ~meta[\"bad\"]\n    env, env_rate = high_gamma(raw, meta[\"rate\"], good)\n    duration = raw.shape[0] / meta[\"rate\"]\n    del raw\n    grid = np.arange(0, duration, 1 / HG_HZ)\n    hg = resample_to(env, env_rate, grid)                  # whole block at 200 Hz\n    cv = meta[\"cv\"] - meta[\"t0\"]\n    kept = np.where((cv + PRE_MS[0] / 1000 >= 0) & (cv + EPOCH_MS[-1] / 1000 < duration))[0]\n    pre_t = cv[kept, None] + np.arange(PRE_MS[0], PRE_MS[1], 5)[None, :] / 1000\n    pre = resample_to(env, env_rate, pre_t)                # (trials, 100, channels)\n    ep_t = cv[kept, None] + EPOCH_MS[None, :] / 1000\n    ep = resample_to(env, env_rate, ep_t)                  # (trials, 251, channels)\n    stats = {\n        \"pre\": (np.nanmean(pre, axis=(0, 1)), np.nanstd(pre, axis=(0, 1))),\n        \"whole\": (np.nanmean(hg, axis=0), np.nanstd(hg, axis=0)),\n    }\n    rest = np.zeros(len(grid), bool)\n    for a, b in meta[\"rest\"]:\n        rest |= (grid >= a - meta[\"t0\"]) & (grid < b - meta[\"t0\"])\n    stats[\"rest\"] = (np.nanmean(hg[rest], axis=0), np.nanstd(hg[rest], axis=0))\n    epochs = {}\n    for name, (m, s) in stats.items():\n        epochs[name] = ((ep - m) / s).transpose(0, 2, 1).astype(np.float32)\n    meta.update(epochs=epochs, kept=kept, hg_stats=stats, duration=duration,\n                rest_seconds=float(rest.sum() / HG_HZ), env_rate=env_rate)\n    return meta\n\n\ndef load_subject(blocks: list[dict]) -> dict:\n    \"\"\"Pool the blocks of one subject into per-syllable mean z-scored high gamma.\n\n    Electrodes flagged bad in any block are left out of the subject's analyses (`good`). Returns\n    `cvs` (sorted (consonant, vowel) pairs), `counts` (renditions per CV), `H[baseline]`\n    (CV, channel, 251) means over renditions, and the electrode metadata of the first block.\n    \"\"\"\n    first = blocks[0]\n    good = ~np.any([b[\"bad\"] for b in blocks], axis=0)\n    labels, chunks = [], {name: [] for name in BASELINES}\n    for b in blocks:\n        for j, i in enumerate(b[\"kept\"]):\n            p = parse_label(b[\"condition\"][i])\n            labels.append(p)\n        for name in BASELINES:\n            chunks[name].append(b[\"epochs\"][name])\n    cvs = sorted({p for p in labels if p is not None},\n                 key=lambda p: (CONSONANTS.index(p[0]), \"aiu\".index(p[1])))\n    index = {p: k for k, p in enumerate(cvs)}\n    lab = np.array([index[p] if p is not None else -1 for p in labels])\n    H = {}\n    for name in BASELINES:\n        allz = np.concatenate(chunks[name])\n        H[name] = np.stack([allz[lab == k].mean(axis=0) for k in range(len(cvs))])\n    return {\n        \"subject\": first[\"subject\"], \"cvs\": cvs, \"counts\": np.bincount(lab[lab >= 0], minlength=len(cvs)),\n        \"n_unparsed\": int((lab < 0).sum()), \"H\": H, \"good\": good,\n        \"location\": first[\"location\"], \"x\": first[\"x\"], \"y\": first[\"y\"], \"z\": first[\"z\"],\n        \"electrode_ids\": first[\"electrode_ids\"],\n        \"vsmc\": np.where(good & np.isin(first[\"location\"], VSMC_LABELS))[0],\n    }\n"
}
```

```
File created successfully at: entries/000019-bouchard-2013/bouchard.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/000019-bouchard-2013 && python - <<'EOF'
s=open('bouchard.py').read()
old_start=s.index('    epochs = {}\n')
old_end=s.index('def load_subject')
new='''    labels = [parse_label(c) for c in meta["condition"][kept]]
    sums = {}
    keys = sorted({p for p in labels if p is not None})
    for name, (m, s) in stats.items():
        z = ((ep - m) / s).transpose(0, 2, 1)
        sums[name] = {p: z[[i for i, q in enumerate(labels) if q == p]].sum(axis=0, dtype=np.float64)
                      for p in keys}
    meta.update(sums=sums, labels=labels, kept=kept, hg_stats=stats, duration=duration,
                rest_seconds=float(rest.sum() / HG_HZ), env_rate=env_rate)
    return meta


'''
s=s[:old_start]+new+s[old_end:]
# replace load_subject body
i=s.index('def load_subject')
s=s[:i]+'''def load_subject(blocks: list[dict]) -> dict:
    """Pool the blocks of one subject into per-syllable mean z-scored high gamma.

    Electrodes flagged bad in any block are left out of the subject's analyses (`good`). Returns
    `cvs` (sorted (consonant, vowel) pairs), `counts` (renditions per CV), `H[baseline]`
    (CV, channel, 251) means over renditions, and the electrode metadata of the first block.
    """
    first = blocks[0]
    good = ~np.any([b["bad"] for b in blocks], axis=0)
    cvs = sorted({p for b in blocks for p in b["labels"] if p is not None},
                 key=lambda p: (CONSONANTS.index(p[0]), "aiu".index(p[1])))
    counts = np.array([sum(q == p for b in blocks for q in b["labels"]) for p in cvs])
    H = {}
    for name in BASELINES:
        total = np.zeros((len(cvs), first["n_channels"], len(EPOCH_MS)))
        for b in blocks:
            for p, v in b["sums"][name].items():
                total[cvs.index(p)] += np.nan_to_num(v)
        H[name] = (total / counts[:, None, None]).astype(np.float32)
        H[name][:, ~good] = np.nan
    return {
        "subject": first["subject"], "cvs": cvs, "counts": counts,
        "n_unparsed": int(sum(q is None for b in blocks for q in b["labels"])), "H": H, "good": good,
        "location": first["location"], "x": first["x"], "y": first["y"], "z": first["z"],
        "electrode_ids": first["electrode_ids"],
        "vsmc": np.where(good & np.isin(first["location"], VSMC_LABELS))[0],
    }
'''
open('bouchard.py','w').write(s)
EOF
cd $TMPDIR && . work/bin/activate && cat > t1.py <<'EOF'
import sys,time; sys.path.insert(0,'entries/000019-bouchard-2013')
import bouchard as B, numpy as np, resource
A=B.assets(); a=[x for x in A if x['path'].endswith('EC2-B1.nwb')][0]
t=time.time(); buf=B.fetch(a['url'],a['size']); print('fetch',time.time()-t); del buf
t=time.time(); b=B.process_block(a); print('block',time.time()-t, 'maxrss GB',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
print(b['env_rate'], len(b['kept']), {k:(np.nanmean(v[0]),np.nanmean(v[1])) for k,v in b['hg_stats'].items()})
S=B.load_subject([b]); H=S['H']['pre']; print(H.shape, S['vsmc'].size, np.nanmax(H[:,S['vsmc']]), np.nanmean(H[:,S['vsmc'],:20]))
import pickle; pickle.dump(b,open('blockEC2B1.pkl','wb'))
EOF
python t1.py
```

```
fetch 6.887590646743774
block 32.12029314041138 maxrss GB 4.222008
400.0014030968028 387 {'pre': (np.float32(4.079292e-06), np.float32(9.800635e-07)), 'whole': (np.float32(4.095093e-06), np.float32(1.0249269e-06)), 'rest': (np.float32(4.094848e-06), np.float32(9.3538813e-07))}
(57, 256, 251) 88 4.5447383 -0.123265356
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/000019-bouchard-2013 && python - <<'EOF'
s=open('bouchard.py').read()
s=s.replace('''def process_block(asset: dict) -> dict:''','''def process_block(asset: dict, buf: bytes | None = None) -> dict:''')
s=s.replace('''    buf = fetch(asset["url"], asset["size"])
    with h5py''','''    if buf is None:
        buf = fetch(asset["url"], asset["size"])
    with h5py''')
s=s.replace('''def load_subject(''','''def process_blocks(block_assets: list[dict], log=print) -> list[dict]:
    """process_block over several files, fetching the next file while one is processed."""
    out = []
    with ThreadPoolExecutor(1) as ex:
        nxt = ex.submit(fetch, block_assets[0]["url"], block_assets[0]["size"])
        for i, a in enumerate(block_assets):
            buf = nxt.result()
            if i + 1 < len(block_assets):
                nxt = ex.submit(fetch, block_assets[i + 1]["url"], block_assets[i + 1]["size"])
            out.append(process_block(a, buf))
            del buf
            log(f"{a['path']}: {len(out[-1]['kept'])} trials")
    return out


def load_subject(''')
open('bouchard.py','w').write(s)
EOF
cd $TMPDIR && . work/bin/activate && cat > t2.py <<'EOF'
import sys,time,pickle; sys.path.insert(0,'entries/000019-bouchard-2013')
import bouchard as B, numpy as np
A=B.assets(); t=time.time()
subs={}
for s in B.SUBJECTS:
    blocks=B.process_blocks([a for a in A if a['path'].startswith(f'sub-{s}/')], log=lambda m: print(m, round(time.time()-t)))
    for b in blocks: b.pop('sums_trial',None)
    subs[s]=B.load_subject(blocks)
    pickle.dump((subs[s],[{k:v for k,v in b.items() if k!='sums'} for b in blocks]),open(f'sub_{s}.pkl','wb'))
print('total',time.time()-t)
EOF
python t2.py
```

```
entries/000019-bouchard-2013/bouchard.py:301: RuntimeWarning: Mean of empty slice
  "pre": (np.nanmean(pre, axis=(0, 1)), np.nanstd(pre, axis=(0, 1))),
/tmp/claude-1001/work/lib/python3.13/site-packages/numpy/lib/_nanfunctions_impl.py:1997: RuntimeWarning: Degrees of freedom <= 0 for slice.
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
entries/000019-bouchard-2013/bouchard.py:302: RuntimeWarning: Mean of empty slice
  "whole": (np.nanmean(hg, axis=0), np.nanstd(hg, axis=0)),
entries/000019-bouchard-2013/bouchard.py:307: RuntimeWarning: Mean of empty slice
  stats["rest"] = (np.nanmean(hg[rest], axis=0), np.nanstd(hg[rest], axis=0))
sub-EC2/sub-EC2_ses-EC2-B1.nwb: 387 trials 37
sub-EC2/sub-EC2_ses-EC2-B105.nwb: 311 trials 70
sub-EC2/sub-EC2_ses-EC2-B15.nwb: 382 trials 97
sub-EC2/sub-EC2_ses-EC2-B76.nwb: 389 trials 122
sub-EC2/sub-EC2_ses-EC2-B8.nwb: 384 trials 147
sub-EC2/sub-EC2_ses-EC2-B89.nwb: 397 trials 175
sub-EC2/sub-EC2_ses-EC2-B9.nwb: 378 trials 197
sub-GP31/sub-GP31_ses-GP31-B1.nwb: 236 trials 222
sub-GP31/sub-GP31_ses-GP31-B2.nwb: 315 trials 244
sub-GP31/sub-GP31_ses-GP31-B21.nwb: 237 trials 264
sub-GP31/sub-GP31_ses-GP31-B4.nwb: 224 trials 285
sub-GP31/sub-GP31_ses-GP31-B6.nwb: 377 trials 307
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && cat > a1.py <<'EOF'
import sys,pickle,numpy as np; sys.path.insert(0,'entries/000019-bouchard-2013')
import bouchard as B
for s in B.SUBJECTS:
    S,blocks=pickle.load(open(f'sub_{s}.pkl','rb'))
    v=S['vsmc']
    print(s,'nCV',len(S['cvs']),'vsmc',len(v),'good',S['good'].sum(),'counts',S['counts'].min(),S['counts'].max(), [ (''.join(S['cvs'][i]),S['counts'][i]) for i in np.argsort(S['counts'])[:3]])
    for base in B.BASELINES:
        H=S['H'][base][:,v]
        print('  ',base,'max',np.nanmax(H).round(2),'active>2',(H.max(axis=(0,2))>2).sum(),'|.|>2',(np.abs(H).max(axis=(0,2))>2).sum(), 'pre-mean', np.nanmean(H[:,:,:20]).round(2))
    print('  missing CVs', [c+v for c in B.CONSONANTS for v in 'aiu' if (c,v) not in S['cvs']])
EOF
python a1.py
```

```
EC2 nCV 57 vsmc 86 good 246 counts 10 58 [('thi', np.int64(10)), ('bu', np.int64(38)), ('mu', np.int64(39))]
   pre max 4.21 active>2 15 |.|>2 15 pre-mean -0.1
   whole max 3.38 active>2 15 |.|>2 15 pre-mean -0.13
   rest max 5.96 active>2 30 |.|>2 30 pre-mean 0.03
  missing CVs []
GP31 nCV 55 vsmc 83 good 242 counts 2 107 [('thi', np.int64(2)), ('fu', np.int64(66)), ('za', np.int64(66))]
   pre max 3.98 active>2 49 |.|>2 49 pre-mean -0.02
   whole max 3.57 active>2 43 |.|>2 43 pre-mean -0.04
   rest max 7.12 active>2 51 |.|>2 51 pre-mean 0.07
  missing CVs ['tha', 'thu']
GP33 nCV 57 vsmc 99 good 229 counts 22 28 [('ku', np.int64(22)), ('ba', np.int64(23)), ('pu', np.int64(23))]
   pre max 3.1 active>2 9 |.|>2 9 pre-mean -0.02
   whole max 2.82 active>2 6 |.|>2 6 pre-mean -0.06
   rest max 3.71 active>2 21 |.|>2 21 pre-mean 0.07
  missing CVs []
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && python -c "
import h5py,remfile,numpy as np
u='https://dandiarchive.s3.amazonaws.com/blobs/256/1e8/2561e839-2df1-4458-9758-5868f4c82d23'
f=h5py.File(remfile.File(u),'r'); P=f['processing/ecephys/spectrum/power'][:]; F=f['processing/ecephys/spectrum/frequencies'][:]
m=np.median(P,axis=1)
for c in [60,100,110,119,120,121,130,150,170,180]:
    i=np.argmin(abs(F-c)); print(c, m[i-2:i+3].max().round(8), np.median(m[(F>c-5)&(F<c+5)]).round(8))
"
```

```
60 0.0 0.0
100 0.0 0.0
110 0.0 0.0
119 0.0 0.0
120 0.0 0.0
121 0.0 0.0
130 0.0 0.0
150 0.0 0.0
170 0.0 0.0
180 0.0 0.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && python -c "
import h5py,remfile,numpy as np
u='https://dandiarchive.s3.amazonaws.com/blobs/256/1e8/2561e839-2df1-4458-9758-5868f4c82d23'
f=h5py.File(remfile.File(u),'r'); P=f['processing/ecephys/spectrum/power'][:]; F=f['processing/ecephys/spectrum/frequencies'][:]
m=np.median(P,axis=1); print(m.max(), P.dtype)
for c in [10,60,100,119.5,120,120.5,130,150,170,180]:
    i=np.argmin(abs(F-c)); print(c, '%.3g'%m[i-3:i+4].max(), '%.3g'%np.median(m[(F>c-5)&(F<c+5)]))
"
```

```
3.7830707e-11 float32
10 2.45e-11 2.34e-11
60 5.22e-13 6.41e-13
100 2e-13 1.41e-13
119.5 2.74e-13 1.9e-13
120 1.98e-13 1.91e-13
120.5 1.21e-13 1.91e-13
130 7.79e-14 1.26e-13
150 1.33e-13 8.21e-14
170 2.62e-14 4.68e-14
180 6.89e-14 3.37e-14
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/000019-bouchard-2013 && cat >> bouchard.py <<'EOF'


# ----------------------------------------------------------------------------------------------
# Measures (the claim each comes from is named; the claims file cites the paper for each)

def ms_index(ms) -> np.ndarray:
    """Index into EPOCH_MS of a time or array of times in ms."""
    return np.searchsorted(EPOCH_MS, np.asarray(ms))


def _residuals(y: np.ndarray, X: np.ndarray) -> np.ndarray:
    """Residuals of least-squares regression of y (n, ...) on X (n, p) with an intercept."""
    X1 = np.c_[np.ones(len(X)), X]
    beta, *_ = np.linalg.lstsq(X1, y.reshape(len(y), -1), rcond=None)
    return (y.reshape(len(y), -1) - X1 @ beta).reshape(y.shape)


def partial_correlation(H: np.ndarray, A: np.ndarray) -> np.ndarray:
    """Methods Eq. 4. H (CV, electrode, time), A (CV, k). Returns rho (electrode, k, time)."""
    out = np.empty((H.shape[1], A.shape[1], H.shape[2]))
    for i in range(A.shape[1]):
        others = np.delete(A, i, axis=1)
        rh = _residuals(H, others)
        ra = _residuals(A[:, i], others)
        num = np.einsum("c,cet->et", ra, rh)
        out[:, i] = num / (np.sqrt((ra ** 2).sum()) * np.sqrt((rh ** 2).sum(axis=0)))
    return out


def timing(rho_e: np.ndarray, level: float) -> tuple[float, float, float]:
    """Onset, peak and offset times (ms) of one electrode's rho time course: the peak, and the
    first and last times of the contiguous run around it that stays above `level`."""
    p = int(np.argmax(rho_e))
    above = rho_e > level
    a = p
    while a > 0 and above[a - 1]:
        a -= 1
    b = p
    while b < len(rho_e) - 1 and above[b + 1]:
        b += 1
    return float(EPOCH_MS[a]), float(EPOCH_MS[p]), float(EPOCH_MS[b])


def glm(H: np.ndarray, Ac: np.ndarray):
    """Methods Eq. 2 by least squares at each electrode and time.

    H (CV, electrode, time), Ac (CV, 4). Returns beta (electrode, 4, time), the F-test p of the
    whole model (electrode, time), each coefficient's t-test p (electrode, 4, time) and R2.
    """
    from scipy import stats
    n, k = Ac.shape
    X = np.c_[np.ones(n), Ac]
    Y = H.reshape(n, -1)
    XtX_inv = np.linalg.inv(X.T @ X)
    beta = XtX_inv @ X.T @ Y
    resid = Y - X @ beta
    sse = (resid ** 2).sum(0)
    sst = ((Y - Y.mean(0)) ** 2).sum(0)
    df = n - k - 1
    r2 = 1 - sse / sst
    F = (r2 / k) / ((1 - r2) / df)
    pF = stats.f.sf(F, k, df)
    se = np.sqrt(np.outer(np.diag(XtX_inv), sse / df))
    pt = 2 * stats.t.sf(np.abs(beta / se), df)
    shape = H.shape[1:]
    return (beta[1:].reshape(k, *shape).transpose(1, 0, 2), pF.reshape(shape),
            pt[1:].reshape(k, *shape).transpose(1, 0, 2), r2.reshape(shape))


def zscore_for_pca(Hv: np.ndarray, mode: str) -> np.ndarray:
    """Hv (CV, electrode, time). `row`: each electrode's concatenated (CV x time) series z-scored;
    `time`: each electrode z-scored across syllables at each time."""
    if mode == "row":
        m = Hv.mean(axis=(0, 2), keepdims=True)
        s = Hv.std(axis=(0, 2), keepdims=True)
    else:
        m = Hv.mean(axis=0, keepdims=True)
        s = Hv.std(axis=0, keepdims=True)
    return (Hv - m) / s


def state_space(Hv: np.ndarray, mode: str, window=(EPOCH_MS[0], EPOCH_MS[-1]), n_pc: int = 9):
    """PCA of the (electrode x concatenated CV-time) matrix (Methods, PCA and Cortical-State
    Space). Returns M (electrode, n_pc), the fraction of variance of every PC, and the states
    K (CV, n_pc, time) of every CV at every epoch time."""
    Z = zscore_for_pca(Hv, mode)
    sel = (EPOCH_MS >= window[0]) & (EPOCH_MS <= window[1])
    X = Z[:, :, sel].transpose(1, 0, 2).reshape(Z.shape[1], -1)
    U, s, _ = np.linalg.svd(X, full_matrices=False)
    frac = s ** 2 / (s ** 2).sum()
    M = U[:, :n_pc]
    K = np.einsum("ep,cet->cpt", M, Z)
    return M, frac, K


def kmeans(X: np.ndarray, k: int, seed: int, n_init: int = 100) -> np.ndarray:
    """k-means labels, Euclidean, best of n_init random starts (a standard choice)."""
    from sklearn.cluster import KMeans
    return KMeans(k, n_init=n_init, random_state=seed).fit_predict(X)


def co_clustering(nc: np.ndarray, ac: np.ndarray) -> np.ndarray:
    """Supplementary Methods Eq. 1 for every token: 1 - |NC delta AC| / (|NC| + |AC|), with NC
    and AC the other members of the token's cluster in each assignment."""
    same_n = nc[:, None] == nc[None, :]
    same_a = ac[:, None] == ac[None, :]
    np.fill_diagonal(same_n, False)
    np.fill_diagonal(same_a, False)
    sym = (same_n ^ same_a).sum(1)
    tot = same_n.sum(1) + same_a.sum(1)
    with np.errstate(invalid="ignore", divide="ignore"):
        return 1 - sym / tot


def separability(D: np.ndarray, labels: np.ndarray, weights: np.ndarray | None = None) -> np.ndarray:
    """Mean between-cluster distance minus mean within-cluster distance (Methods, Cluster
    Separability). D (time, n, n) pairwise distances; labels per token, per time when 2-D
    (time, n). weights (B, n) are bootstrap counts of each token; returns (B, time) then."""
    n = D.shape[1]
    lab = labels if labels.ndim == 2 else np.broadcast_to(labels, (D.shape[0], n))
    same = lab[:, :, None] == lab[:, None, :]
    if weights is None:
        weights = np.ones((1, n))
    out = np.empty((len(weights), D.shape[0]))
    for b, w in enumerate(weights):
        W = np.outer(w, w) - np.diag(w)
        within = (W * same * D).sum((1, 2)) / (W * same).sum((1, 2))
        between = (W * ~same * D).sum((1, 2)) / (W * ~same).sum((1, 2))
        out[b] = between - within
    return out
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/000019-bouchard-2013 && python - <<'EOF'
s=open('bouchard.py').read()
i=s.index('    n = D.shape[1]\n    lab = labels')
s=s[:i]+'''    n = D.shape[1]
    lab = labels if labels.ndim == 2 else np.broadcast_to(labels, (D.shape[0], n))
    same = (lab[:, :, None] == lab[:, None, :]).astype(float)
    if weights is None:
        weights = np.ones((1, n))
    w = np.asarray(weights, float)
    total_pairs = w.sum(1) ** 2 - w.sum(1)                          # (B,)
    within_pairs = np.einsum("bi,tij,bj->bt", w, same, w) - w.sum(1)[:, None]
    within_sum = np.einsum("bi,tij,bj->bt", w, same * D, w)
    all_sum = np.einsum("bi,tij,bj->bt", w, D, w)
    between = (all_sum - within_sum) / (total_pairs[:, None] - within_pairs)
    return between - within_sum / within_pairs
'''
open('bouchard.py','w').write(s)
EOF
echo done
```

```
/bin/bash: line 1: cd: entries/000019-bouchard-2013: No such file or directory
done
```

**Agent calls Bash**

```bash
pwd; python - <<'EOF'
s=open('bouchard.py').read()
i=s.index('    n = D.shape[1]\n    lab = labels')
s=s[:i]+'''    n = D.shape[1]
    lab = labels if labels.ndim == 2 else np.broadcast_to(labels, (D.shape[0], n))
    same = (lab[:, :, None] == lab[:, None, :]).astype(float)
    if weights is None:
        weights = np.ones((1, n))
    w = np.asarray(weights, float)
    total_pairs = w.sum(1) ** 2 - w.sum(1)                          # (B,)
    within_pairs = np.einsum("bi,tij,bj->bt", w, same, w) - w.sum(1)[:, None]
    within_sum = np.einsum("bi,tij,bj->bt", w, same * D, w)
    all_sum = np.einsum("bi,tij,bj->bt", w, D, w)
    between = (all_sum - within_sum) / (total_pairs[:, None] - within_pairs)
    return between - within_sum / within_pairs
'''
open('bouchard.py','w').write(s)
EOF
tail -5 bouchard.py
```

```
entries/000019-bouchard-2013
    within_pairs = np.einsum("bi,tij,bj->bt", w, same, w) - w.sum(1)[:, None]
    within_sum = np.einsum("bi,tij,bj->bt", w, same * D, w)
    all_sum = np.einsum("bi,tij,bj->bt", w, D, w)
    between = (all_sum - within_sum) / (total_pairs[:, None] - within_pairs)
    return between - within_sum / within_pairs
```

**Agent calls Bash**

```bash
sed -i 's/, w, same, w)/, w, same, w, optimize=True)/; s/, w, same \* D, w)/, w, same * D, w, optimize=True)/; s/, w, D, w)$/, w, D, w, optimize=True)/' bouchard.py && grep -n optimize bouchard.py && cd $TMPDIR && . work/bin/activate && cat > a2.py <<'EOF'
import sys,pickle,numpy as np, itertools; sys.path.insert(0,'entries/000019-bouchard-2013')
import bouchard as B
from scipy import stats
S={s:pickle.load(open(f'sub_{s}.pkl','rb'))[0] for s in B.SUBJECTS}
names=B.ARTICULATORS+B.VOWEL_ARTICULATORS
for base in ('pre','whole'):
    rho={s:B.partial_correlation(S[s]['H'][base][:,S[s]['vsmc']], B.articulator_matrix(S[s]['cvs'])) for s in B.SUBJECTS}
    for subj_mode, art_mode, onset_mode, anova in itertools.product(('per','pooled'),('all','per'),('thr','half'),('onset','peak')):
        rows=[]
        for s in B.SUBJECTS:
            for a in range(6):
                pool = np.concatenate([rho[x] for x in B.SUBJECTS]) if subj_mode=='pooled' else rho[s]
                vals = pool if art_mode=='all' else pool[:,a]
                thr=vals.mean()+2.5*vals.std()
                for e in range(rho[s].shape[0]):
                    r=rho[s][e,a]
                    if r.max()>thr:
                        on,pk,off=B.timing(r, thr if onset_mode=='thr' else r.max()/2)
                        rows.append((s,a,on,pk,off))
        rows=np.array(rows,dtype=object)
        a_=rows[:,1].astype(int); on=rows[:,2].astype(float); pk=rows[:,3].astype(float)
        val = on if anova=='onset' else pk
        F,p=stats.f_oneway(*[val[a_==a] for a in range(6)])
        mon=[on[a_==a].mean() for a in range(6)]; mpk=[pk[a_==a].mean() for a in range(6)]
        n=[(a_==a).sum() for a in range(6)]
        print(base,subj_mode,art_mode,onset_mode,anova,'n',len(rows),n,'F %.1f p %.1e'%(F,p),'onsets',np.round(mon),'peaks',np.round(mpk))
EOF
python a2.py
```

```
487:    within_pairs = np.einsum("bi,tij,bj->bt", w, same, w, optimize=True) - w.sum(1)[:, None]
488:    within_sum = np.einsum("bi,tij,bj->bt", w, same * D, w, optimize=True)
489:    all_sum = np.einsum("bi,tij,bj->bt", w, D, w, optimize=True)
pre per all thr onset n 175 [np.int64(31), np.int64(5), np.int64(18), np.int64(34), np.int64(38), np.int64(49)] F 22.5 p 3.0e-17 onsets [-173.  160.  -13. -136.  165.  224.] peaks [-111.  181.   22.  -74.  235.  305.]
pre per all thr peak n 175 [np.int64(31), np.int64(5), np.int64(18), np.int64(34), np.int64(38), np.int64(49)] F 27.2 p 4.1e-20 onsets [-173.  160.  -13. -136.  165.  224.] peaks [-111.  181.   22.  -74.  235.  305.]
pre per all half onset n 175 [np.int64(31), np.int64(5), np.int64(18), np.int64(34), np.int64(38), np.int64(49)] F 27.3 p 3.6e-20 onsets [-233.   93.  -91. -260.  112.  166.] peaks [-111.  181.   22.  -74.  235.  305.]
pre per all half peak n 175 [np.int64(31), np.int64(5), np.int64(18), np.int64(34), np.int64(38), np.int64(49)] F 27.2 p 4.1e-20 onsets [-233.   93.  -91. -260.  112.  166.] peaks [-111.  181.   22.  -74.  235.  305.]
pre per per thr onset n 224 [np.int64(33), np.int64(43), np.int64(39), np.int64(31), np.int64(38), np.int64(40)] F 10.6 p 3.9e-09 onsets [ -83.   89.   55. -134.  234.  211.] peaks [-21. 108.  94. -75. 297. 278.]
pre per per thr peak n 224 [np.int64(33), np.int64(43), np.int64(39), np.int64(31), np.int64(38), np.int64(40)] F 11.6 p 6.2e-10 onsets [ -83.   89.   55. -134.  234.  211.] peaks [-21. 108.  94. -75. 297. 278.]
pre per per half onset n 224 [np.int64(33), np.int64(43), np.int64(39), np.int64(31), np.int64(38), np.int64(40)] F 13.9 p 9.1e-12 onsets [-132.   52.   12. -270.  183.  147.] peaks [-21. 108.  94. -75. 297. 278.]
pre per per half peak n 224 [np.int64(33), np.int64(43), np.int64(39), np.int64(31), np.int64(38), np.int64(40)] F 11.6 p 6.2e-10 onsets [-132.   52.   12. -270.  183.  147.] peaks [-21. 108.  94. -75. 297. 278.]
pre pooled all thr onset n 176 
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && cat > common.py <<'EOF'
import sys,pickle,numpy as np, itertools; sys.path.insert(0,'entries/000019-bouchard-2013')
import bouchard as B
from scipy import stats
S={s:pickle.load(open(f'sub_{s}.pkl','rb'))[0] for s in B.SUBJECTS}
TIMING_READINGS=list(itertools.product(('per','pooled'),('all','per'),('thr','half')))
def timing_table(rho):
    out={}
    for subj_mode, art_mode, onset_mode in TIMING_READINGS:
        rows=[]
        for s in B.SUBJECTS:
            pool = np.concatenate([rho[x] for x in B.SUBJECTS]) if subj_mode=='pooled' else rho[s]
            for a in range(6):
                vals = pool if art_mode=='all' else pool[:,a]
                thr=vals.mean()+2.5*vals.std()
                for e in range(rho[s].shape[0]):
                    r=rho[s][e,a]
                    if r.max()>thr:
                        on,pk,off=B.timing(r, thr if onset_mode=='thr' else r.max()/2)
                        rows.append(dict(subject=s,art=a,electrode=e,onset=on,peak=pk,offset=off))
        out[(subj_mode,art_mode,onset_mode)]=rows
    return out
def windows(rows):
    T={}
    for s in B.SUBJECTS:
        for a in range(4):
            r=[x for x in rows if x['subject']==s and x['art']==a]
            T[(s,a)]=(np.mean([x['onset'] for x in r]),np.mean([x['offset'] for x in r])) if r else None
    return T
EOF
cat > a3.py <<'EOF'
from common import *
for base in ('pre','whole'):
    rho={s:B.partial_correlation(S[s]['H'][base][:,S[s]['vsmc']], B.articulator_matrix(S[s]['cvs'])) for s in B.SUBJECTS}
    tt=timing_table(rho)
    G={s:B.glm(S[s]['H'][base][:,S[s]['vsmc']], B.articulator_matrix(S[s]['cvs'])[:,:4]) for s in B.SUBJECTS}
    for key,rows in tt.items():
        T=windows(rows)
        for pmode in ('F','t'):
            res=[]
            for s in B.SUBJECTS:
                beta,pF,pt,r2=G[s]
                keep=np.zeros(beta.shape[0],bool); W=np.full((beta.shape[0],4),np.nan)
                for a in range(4):
                    if T[(s,a)] is None: continue
                    idx=(B.EPOCH_MS>=T[(s,a)][0])&(B.EPOCH_MS<=T[(s,a)][1])
                    p=(pF[:,idx] if pmode=='F' else pt[:,a,idx]).mean(1)
                    keep|=p<0.05
                    W[:,a]=beta[:,a,idx].mean(1)
                res.append((s,keep.sum(),np.isnan(W).any()))
            print(base,key,pmode,res, {k:(None if v is None else tuple(np.round(v))) for k,v in T.items()})
EOF
python a3.py 2>&1 | head -40
```

```
pre ('per', 'all', 'thr') F [('EC2', np.int64(36), np.False_), ('GP31', np.int64(36), np.True_), ('GP33', np.int64(31), np.False_)] {('EC2', 0): (np.float64(-122.0), np.float64(53.0)), ('EC2', 1): (np.float64(-225.0), np.float64(-75.0)), ('EC2', 2): (np.float64(172.0), np.float64(227.0)), ('EC2', 3): (np.float64(-130.0), np.float64(45.0)), ('GP31', 0): (np.float64(-229.0), np.float64(-42.0)), ('GP31', 1): None, ('GP31', 2): (np.float64(0.0), np.float64(77.0)), ('GP31', 3): (np.float64(-178.0), np.float64(-146.0)), ('GP33', 0): (np.float64(50.0), np.float64(117.0)), ('GP33', 1): (np.float64(256.0), np.float64(268.0)), ('GP33', 2): (np.float64(-94.0), np.float64(-44.0)), ('GP33', 3): (np.float64(-125.0), np.float64(-23.0))}
pre ('per', 'all', 'thr') t [('EC2', np.int64(35), np.False_), ('GP31', np.int64(35), np.True_), ('GP33', np.int64(33), np.False_)] {('EC2', 0): (np.float64(-122.0), np.float64(53.0)), ('EC2', 1): (np.float64(-225.0), np.float64(-75.0)), ('EC2', 2): (np.float64(172.0), np.float64(227.0)), ('EC2', 3): (np.float64(-130.0), np.float64(45.0)), ('GP31', 0): (np.float64(-229.0), np.float64(-42.0)), ('GP31', 1): None, ('GP31', 2): (np.float64(0.0), np.float64(77.0)), ('GP31', 3): (np.float64(-178.0), np.float64(-146.0)), ('GP33', 0): (np.float64(50.0), np.float64(117.0)), ('GP33', 1): (np.float64(256.0), np.float64(268.0)), ('GP33', 2): (np.float64(-94.0), np.float64(-44.0)), ('GP33', 3): (np.float64(-125.0), np.float64(-23.0))}
pre ('per', 'all', 'half') F [('EC2', np.int64(26), np.False_), ('GP31', np.int64(27), np.True_), ('GP33', np.int64(29), np.False_)] {('EC2', 0): (np.float64(-207.0), np.float64(95.0)), ('EC2', 1): (np.float64(-320.0), np.float64(40.0)), ('EC2', 2): (np.float64(63.0), np.float64(355.0)), ('EC2', 3): (np.float64(-274.0), np.float64(157.0)), ('GP31', 0): (np.float64(-281.0), np.float64(52.0)), ('GP31', 1): None, ('GP31', 2): (np.float64(-77.0), np.float64(103.0)), ('GP31', 3): (np.float64(-333.0), np.float64(-23.0)), ('GP33', 0): (n
[... 30 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb.py",
 "content": "# %% [markdown]\n# # Reproducing Bouchard et al. (2013) from dandiset 000019\n#\n# **Paper.** Bouchard KE, Mesgarani N, Johnson K, Chang EF (2013). Functional organization of\n# human sensorimotor cortex for speech articulation. *Nature* 495, 327-332.\n# [doi:10.1038/nature11911](https://doi.org/10.1038/nature11911). The claims file\n# (`claims/000019/10.1038-nature11911.yaml`) was written from the NIH author manuscript in PubMed\n# Central (PMC3606666) with its supplement, and checked by a second reader.\n#\n# **Dandiset.** [DANDI:000019](https://dandiarchive.org/dandiset/000019/0.220126.2148),\n# \"Human ECoG speaking consonant-vowel syllables\", version 0.220126.2148. The paper cites no\n# version of the dandiset (it predates it). This is the only published version; the draft has the\n# same 31 assets and the same size, so the published version is pinned.\n#\n# **What the dandiset holds.** Raw ECoG (256 channels, 3051.76 Hz) of 31 recording blocks from four\n# subjects (EC2, EC9, GP31, GP33), with a trial table per block (syllable, start, C-V transition\n# and stop times), a `bad` flag and an anatomical label per electrode, 3-D electrode coordinates for\n# two subjects, and a rest period per block. The microphone signal was removed (dandiset\n# description), and no high gamma is stored, so high gamma is computed here from the raw voltage.\n# The paper's subjects are EC2, EC33 and EC31; EC2, GP33 and GP31 are taken to be them (see the data\n# check). EC9 is not in the paper and is not analysed.\n#\n# **Readings.** Where the claims file leaves a method detail open it names readings, and every\n# reading is run; a claim's outcome is the one all its method readings give. Two readings are added\n# here as questions to the reader (`questions/000019.yaml`): how the state-space input is z-scored\n# (`row`: each electrode's concatenated series; `time`: each electrode at each time across\n# syllables), and the dataset's rest period as a baseline (shown as a variant only).\n#\n# | Claim | Tested here |\n# |---|---|\n# | data-composition | tested |\n# | active-electrodes | tested |\n# | fig1c-e-articulator-electrodes | tested |\n# | fig1f-h-phonetic-contrasts | tested |\n# | fig2a-lips-dorsal | blocked: metadata_insufficient (no positions relative to the central sulcus and Sylvian fissure) |\n# | fig2b-somatotopic-sequence | blocked: metadata_insufficient |\n# | suppfig3b-spatial-clustering | blocked: metadata_insufficient |\n# | suppfig3d-cross-subject | blocked: metadata_insufficient |\n# | suppfig3f-dv-sequence | blocked: metadata_insufficient |\n# | suppfig5-intermediate-organization | blocked: metadata_insufficient |\n# | suppfig6-mixed-tuning | tested |\n# | fig3d-timing-sequence | tested |\n# | suppfig7-no-latency-difference | blocked: metadata_insufficient |\n# | pca-nine-components | tested |\n# | fig4a-consonant-clusters | tested |\n# | suppfig11-co-clustering | tested |\n# | fig4c-d-hierarchy | tested |\n# | fig4ef-feature-correlations | tested |\n# | fig5c-separability-timing | tested |\n# | fig5d-separability-coupling | tested |\n# | suppfig13-consonant-vowel-distance | tested |\n# | suppfig9-pc-articulator-weights | tested |\n\n# %%\nimport itertools\nimport time\nimport warnings\n\nimport h5py\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nimport remfile\nfrom scipy import stats\nfrom scipy.cluster.hierarchy import fcluster, linkage\nfrom scipy.spatial.distance import pdist, squareform\nfrom sklearn.metrics import silhouette_score\n\nimport bouchard as B\n\npd.set_option(\"display.width\", 220)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 300)\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\nstarted = time.time()\n\n# %%\n# Metadata of every file (EC9 included), and a fingerprint of its first samples, read by streaming.\nASSETS = B.assets()\nmeta_rows = []\nfor a in ASSETS:\n    with h5py.File(remfile.File(a[\"url\"]), \"r\") as h5:\n        m = B.read_metadata(h5)\n        m[\"fingerprint\"] = h5[\"acquisition/ElectricalSeries/data\"][:2000, :4].copy()\n    m[\"path\"], m[\"size\"] = a[\"path\"], a[\"size\"]\n    meta_rows.append(m)\nprint(f\"read metadata of {len(meta_rows)} files of dandiset {B.DANDISET_ID} version {B.DANDISET_VERSION} \"\n      f\"in {time.time() - started:.0f} s\")\n\n# %%\n# High gamma of the three subjects of the paper: every block is streamed into memory and processed.\nblocks = {}\nfor s in B.SUBJECTS:\n    blocks[s] = B.process_blocks([a for a in ASSETS if a[\"path\"].startswith(f\"sub-{s}/\")],\n                                 log=lambda msg: None)\nS = {s: B.load_subject(blocks[s]) for s in B.SUBJECTS}\nprint(f\"processed {sum(len(v) for v in blocks.values())} blocks in {time.time() - started:.0f} s\")\n\n# %% [markdown]\n# ## Data check\n\n# %% tags=[\"sanity\"]\nmd = B.dandiset_metadata()\nprint(\"Dandiset:\", md[\"name\"], \"| version\", B.DANDISET_VERSION, \"| DOI\", md.get(\"doi\"))\nprint(\"Related resource:\", [(r.get(\"relation\"), r.get(\"identifier\"), r.get(\"url\")) for r in md.get(\"relatedResource\", [])])\nprint(\"Assets summary: subjects\", md[\"assetsSummary\"].get(\"numberOfSubjects\"), \"| files\", md[\"assetsSummary\"].get(\"numberOfFiles\"))\nfiles = pd.DataFrame([{\n    \"file\": m[\"path\"].split(\"/\")[1], \"subject\": m[\"subject\"], \"rate_hz\": m[\"rate\"],\n    \"minutes\": m[\"n_samples\"] / m[\"rate\"] / 60, \"channels\": m[\"n_channels\"], \"unit\": m[\"unit\"],\n    \"conversion\": m[\"conversion\"], \"trials\": len(m[\"condition\"]), \"speak\": int(m[\"speak\"].sum()),\n    \"bad\": int(m[\"bad\"].sum()), \"rest_s\": sum(b - a for a, b in m[\"rest\"]),\n    \"invalid_intervals\": len(m[\"invalid\"]), \"has_xyz\": bool(np.isfinite(m[\"x\"]).any()),\n    \"mean_x\": np.nanmean(m[\"x\"]) if np.isfinite(m[\"x\"]).any() else np.nan,\n    \"electrode_ids\": f\"{m['electrode_ids'][0]}-{m['electrode_ids'][-1]}\"} for m in meta_rows])\nprint(files.round(2).to_string(index=False))\nprint(\"\\nFiles and trials per subject:\")\nprint(files.groupby(\"subject\").agg(files=(\"file\", \"size\"), trials=(\"trials\", \"sum\"), minutes=(\"minutes\", \"sum\")).round(1).to_string())\nprint(\"\\nSampling rates found:\", sorted(files.rate_hz.unique()), \"(Methods: 3052 Hz)\")\nprint(\"Every trial is marked speak=True:\", bool((files.trials == files.speak).all()))\nprint(\"Microphone or other acquisition series in any file: none (only acquisition/ElectricalSeries is present)\")\n\n# %% tags=[\"sanity\"]\n# Duplicates: blocks with the same length, the same trial table, or the same first samples.\npairs = []\nfor i, j in itertools.combinations(range(len(meta_rows)), 2):\n    a, b = meta_rows[i], meta_rows[j]\n    same_n = a[\"n_samples\"] == b[\"n_samples\"]\n    same_trials = len(a[\"cv\"]) == len(b[\"cv\"]) and np.allclose(a[\"cv\"], b[\"cv\"])\n    same_data = np.array_equal(a[\"fingerprint\"], b[\"fingerprint\"])\n    if same_n or same_trials or same_data:\n        pairs.append((a[\"path\"], b[\"path\"], same_n, same_trials, same_data))\nprint(\"Pairs sharing sample count, trial times or first 2000 samples of 4 channels:\")\nfor p in pairs:\n    print(\"  \", p)\n\n# %% tags=[\"sanity\"]\n# Syllables per subject, from the trial labels.\nlabel_rows = []\nfor m in meta_rows:\n    for c in m[\"condition\"]:\n        label_rows.append({\"subject\": m[\"subject\"], \"label\": c, \"cv\": B.parse_label(c)})\nlabels = pd.DataFrame(label_rows)\nfor s, g in labels.groupby(\"subject\"):\n    unparsed = g[g.cv.isna()].label.value_counts().to_dict()\n    cv = g.dropna().cv\n    cons = sorted({c for c, v in cv}, key=B.CONSONANTS.index)\n    counts = cv.value_counts()\n    print(f\"{s}: {len(g)} trials, {counts.size} distinct CVs, {len(cons)} consonants; renditions per CV \"\n          f\"{counts.min()} to {counts.max()}; labels that are not CVs of the task: {unparsed}\")\n    missing = [c + v for c in B.CONSONANTS for v in \"aiu\" if (c, v) not in set(cv)]\n    print(f\"    CVs missing: {missing}; CVs with fewer than 15 renditions: \"\n          f\"{ {''.join(k): int(n) for k, n in counts.items() if n < 15} }; more than 100: \"\n          f\"{ {''.join(k): int(n) for k, n in counts.items() if n > 100} }\")\nprint(\"Spellings merged: 'she' -> 'shee', 'ha' -> 'haa'. Paper: 19, 19 and 18 consonants, 168 CVs (57 + 57 + 54), 15 to 100 renditions each.\")\n\n# %% tags=[\"sanity\"]\n# Electrodes: labels, bad flags, coordinates.\nfor s in [\"EC2\", \"EC9\", \"GP31\", \"GP33\"]:\n    ms = [m for m in meta_rows if m[\"subject\"] == s]\n    same_loc = all(np.array_equal(m[\"location\"], ms[0][\"location\"]) for m in ms)\n    loc = pd.Series(ms[0][\"location\"]).replace(\"\", \"(none)\").value_counts().to_dict()\n    badsets = sorted({tuple(np.where(m[\"bad\"])[0]) for m in ms}, key=len)\n    print(f\"{s}: labels identical in all blocks {same_loc}; labels {loc}\")\n    print(f\"    bad-channel sets over blocks: {[list(b) for b in badsets]}\")\n    x = ms[0][\"x\"]\n    if np.isfinite(x).any():\n        print(f\"    x {np.nanmin(x):.1f} to {np.nanmax(x):.1f}, y {np.nanmin(ms[0]['y']):.1f} to {np.nanmax(ms[0]['y']):.1f}, \"\n              f\"z {np.nanmin(ms[0]['z']):.1f} to {np.nanmax(ms[0]['z']):.1f} (no unit or frame given); \"\n              f\"neighbour spacing median {np.median(np.linalg.norm(np.diff(np.c_[x, ms[0]['y'], ms[0]['z']], axis=0), axis=1)):.2f}\")\n    else:\n        print(\"    no coordinates (x, y, z are NaN)\")\nfor s in B.SUBJECTS:\n    print(f\"{s}: vSMC (precentral or postcentral, good in every block) {len(S[s]['vsmc'])} electrodes; \"\n          f\"electrodes bad in any block {int((~S[s]['good']).sum())}\")\nprint(\"vSMC electrodes over the three subjects:\", sum(len(S[s][\"vsmc\"]) for s in B.SUBJECTS), \"(Supplementary Figure 9: n = 266)\")\n\n# %% [markdown]\n# The archive's summary counts four subjects. EC2 matches the paper's EC2 by name. GP31 and GP33\n# are not names the paper uses; the paper's other two subjects are EC31 (left hemisphere) and\n# EC33 (right). GP31's coordinates have negative x in every electrode, which fits a left\n# hemisphere if x is the usual left-right axis; GP33 has no coordinates, so its hemisphere cannot be\n# checked. That GP31 is EC31 and GP33 is EC33 is an assumption the data are consistent with, not\n# shown by them. EC9 has 24 consonant labels (including /ch/, /dh/, /j/, /sk/), labels on only 79 of\n# 256 electrodes and no coordinates; it is not one of the paper's subjects and is left out.\n\n# %% tags=[\"sanity\"]\n# Trials kept, trials in invalid intervals, rest periods, and the high-gamma statistics.\nrows = []\nfor s in B.SUBJECTS:\n    for b in blocks[s]:\n        cv = b[\"cv\"]\n        inv = sum(((cv[b[\"kept\"]] + 0.75 > a0) & (cv[b[\"kept\"]] - 0.5 < a1)).sum() for a0, a1 in b[\"invalid\"])\n        g = ~b[\"bad\"]\n        rows.append({\"subject\": s, \"block\": b[\"session\"], \"trials\": len(cv), \"kept\": len(b[\"kept\"]),\n                     \"kept_in_invalid\": int(inv), \"rest_s\": round(b[\"rest_seconds\"], 1),\n                     \"hg_whole_mean_uV\": float(np.nanmedian(b[\"hg_stats\"][\"whole\"][0][g]) * 1e6),\n                     \"hg_whole_sd_over_mean\": float(np.nanmedian(b[\"hg_stats\"][\"whole\"][1][g] / b[\"hg_stats\"][\"whole\"][0][g])),\n                     \"pre_mean_over_whole\": float(np.nanmedian(b[\"hg_stats\"][\"pre\"][0][g] / b[\"hg_stats\"][\"whole\"][0][g])),\n                     \"rest_mean_over_whole\": float(np.nanmedian(b[\"hg_stats\"][\"rest\"][0][g] / b[\"hg_stats\"][\"whole\"][0][g])),\n                     \"env_rate\": round(b[\"env_rate\"], 3)})\nblk = pd.DataFrame(rows)\nprint(blk.round(3).to_string(index=False))\nprint(\"\\nTrials dropped (epoch -1000 to +750 ms outside the recording):\", int((blk.trials - blk.kept).sum()))\nprint(\"Kept trials whose epoch overlaps an 'ECoG artifact' invalid interval (not excluded; the claims file does not say to):\",\n      int(blk.kept_in_invalid.sum()), \"of\", int(blk.kept.sum()))\nprint(\"Raw values: unit 'volt' with conversion 0.001, so stored values are mV; high-gamma amplitudes above are in uV after conversion.\")\nfor s in B.SUBJECTS:\n    for base in B.BASELINES:\n        H = S[s][\"H\"][base][:, S[s][\"vsmc\"]]\n        print(f\"{s} {base:5s}: per-CV mean z over vSMC electrodes, range {np.nanmin(H):.2f} to {np.nanmax(H):.2f}; \"\n              f\"mean over -500 to -400 ms {np.nanmean(H[:, :, :21]):.2f}\")\n\n# %% [markdown]\n# Units: the raw series says volts with a conversion of 0.001, so the stored values are mV; the\n# high-gamma amplitude is a few uV, which is consistent with ECoG. Only the z-scores are used.\n# Sampling rate 3051.7578 Hz in all files, the TDT rate the Methods round to 3052 Hz. The `pre`\n# baseline (-1000 to -500 ms before each C-V transition) is close to the whole-block level, and the\n# rest period is lower than both in most blocks (the ratios above), so z-scores against the rest\n# period are larger; that variant is shown where it matters.\n\n# %% tags=[\"sanity\"]\n# Clock check: the trial times and the ECoG share a clock if the high gamma tells syllables apart\n# at the times the paper says, and not before speech. Leave-one-out nearest-centroid classification\n# of the vowel (/a/, /i/, /u/) and of the major oral articulator of the consonant (labial, coronal,\n# dorsal; reading (a) of the labels) from the vSMC high-gamma pattern of each CV, at each time.\ndef loo_accuracy(X, y):\n    ok = 0\n    for i in range(len(y)):\n        mask = np.arange(len(y)) != i\n        cents = {c: X[mask & (y == c)].mean(0) for c in np.unique(y[mask])}\n        pred = min(cents, key=lambda c: np.linalg.norm(X[i] - cents[c]))\n        ok += pred == y[i]\n    return ok / len(y)\n\nclock = []\nfor s in B.SUBJECTS:\n    H = S[s][\"H\"][\"pre\"][:, S[s][\"vsmc\"]]\n    vow = np.array([v for c, v in S[s][\"cvs\"]])\n    maj = np.array([B.MAJOR[\"a\"].get(c, \"\") for c, v in S[s][\"cvs\"]])\n    lab = maj != \"\"\n    for t in range(0, len(B.EPOCH_MS), 5):\n        clock.append({\"subject\": s, \"t_ms\": B.EPOCH_MS[t], \"vowel\": loo_accuracy(H[:, :, t], vow),\n                      \"consonant\": loo_accuracy(H[lab][:, :, t], maj[lab])})\nclock = pd.DataFrame(clock)\nsummary = clock.groupby(\"t_ms\")[[\"vowel\", \"consonant\"]].mean()\nprint(\"Mean accuracy over subjects (chance 1/3 for vowels; 0.5 to 0.53 for consonants, the largest class share):\")\nprint(summary.iloc[::4].round(2).T.to_string())\nfor col in [\"vowel\", \"consonant\"]:\n    print(f\"{col}: peak {summary[col].max():.2f} at {summary[col].idxmax()} ms; mean before -400 ms {summary[col][summary.index < -400].mean():.2f}\")\nfig, ax = plt.subplots(figsize=(6, 3))\nsummary.plot(ax=ax)\nax.axvline(0, color=\"k\", lw=0.5)\nax.set_xlabel(\"time from C-V transition (ms)\"); ax.set_ylabel(\"LOO accuracy\")\nplt.show()\n\n# %% [markdown]\n# The consonant's articulator is decoded best before the C-V transition and the vowel after it,\n# and neither is decoded above chance level at the start of the epoch (numbers above). This is\n# consistent with the trial times and the ECoG sharing a clock in every subject, with the\n# annotations marking the C-V transition; it does not show the alignment to the millisecond.\n\n# %% [markdown]\n# ## Shared computations\n#\n# The partial correlations and the GLM (Methods Eqs. 2 to 4) are computed once per baseline, and\n# the state space (Methods Eq. 5) once per baseline and z-scoring reading. The articulator windows\n# T_A come from the timing analysis under each of its eight readings (claim fig3d-timing-sequence:\n# threshold set per subject or pooled, over all six articulators or per articulator, and onset at the\n# threshold or at half the peak).\n\n# %%\nBASES = (\"pre\", \"whole\")\nZMODES = (\"row\", \"time\")\nART6 = B.ARTICULATORS + B.VOWEL_ARTICULATORS\nTIMING_READINGS = list(itertools.product((\"per subject\", \"pooled\"), (\"all six\", \"per articulator\"), (\"threshold\", \"half peak\")))\nAM = {s: B.articulator_matrix(S[s][\"cvs\"]) for s in B.SUBJECTS}\nHV = {(s, base): S[s][\"H\"][base][:, S[s][\"vsmc\"]] for s in B.SUBJECTS for base in B.BASELINES}\nRHO = {(s, base): B.partial_correlation(HV[s, base], AM[s]) for s in B.SUBJECTS for base in BASES}\nGLM = {(s, base): B.glm(HV[s, base], AM[s][:, :4]) for s in B.SUBJECTS for base in BASES}\n\n\ndef timing_rows(base, reading):\n    subj_mode, art_mode, onset_mode = reading\n    rows = []\n    for s in B.SUBJECTS:\n        pool = np.concatenate([RHO[x, base] for x in B.SUBJECTS]) if subj_mode == \"pooled\" else RHO[s, base]\n        for a in range(6):\n            vals = pool if art_mode == \"all six\" else pool[:, a]\n            thr = vals.mean() + 2.5 * vals.std()\n            for e in range(RHO[s, base].shape[0]):\n                r = RHO[s, base][e, a]\n                if r.max() > thr:\n                    on, pk, off = B.timing(r, thr if onset_mode == \"threshold\" else r.max() / 2)\n                    rows.append({\"subject\": s, \"articulator\": ART6[a], \"electrode\": e, \"onset\": on,\n                                 \"peak\": pk, \"offset\": off, \"threshold\": thr})\n    return pd.DataFrame(rows)\n\n\nTIMING = {(base, r): timing_rows(base, r) for base in BASES for r in TIMING_READINGS}\n\n\ndef articulator_windows(base, reading):\n    \"\"\"T_A per subject: mean onset to mean offset of the subject's electrodes for A (None if none).\"\"\"\n    t = TIMING[base, reading]\n    out = {}\n    for s in B.SUBJECTS:\n        for a in B.ARTICULATORS:\n            g = t[(t.subject == s) & (t.articulator == a)]\n            out[s, a] = (g.onset.mean(), g.offset.mean()) if len(g) else None\n    return out\n\n\ndef weights(base, reading, pmode):\n    \"\"\"Per subject: W (vSMC electrode, 4), NaN for an articulator without a window, and the\n    electrodes kept by the GLM rule (mean p over T_A below 0.05 for any articulator).\"\"\"\n    T = articulator_windows(base, reading)\n    out = {}\n    for s in B.SUBJECTS:\n        beta, pF, pt, r2 = GLM[s, base]\n        keep = np.zeros(beta.shape[0], bool)\n        W = np.full((beta.shape[0], 4), np.nan)\n        for a, name in enumerate(B.ARTICULATORS):\n            if T[s, name] is None:\n                continue\n            idx = (B.EPOCH_MS >= T[s, name][0]) & (B.EPOCH_MS <= T[s, name][1])\n            p = (pF[:, idx] if pmode == \"F-test\" else pt[:, a, idx]).mean(1)\n            keep |= p < 0.05\n            W[:, a] = beta[:, a, idx].mean(1)\n        out[s] = {\"W\": W, \"keep\": keep, \"windows\": {a: T[s, a] for a in B.ARTICULATORS}}\n    return out\n\n\nW_READINGS = [(base, r, p) for base in BASES for r in TIMING_READINGS for p in (\"F-test\", \"t-test\")]\nWEIGHTS = {k: weights(*k) for k in W_READINGS}\nSTATE = {(s, base, z, w): B.state_space(HV[s, base], z, w)\n         for s in B.SUBJECTS for base in BASES for z in ZMODES\n         for w in [(-500, 750), (-375, 620)]}\nSS_READINGS = [(base, z) for base in BASES for z in ZMODES]\nprint(f\"shared computations done at {time.time() - started:.0f} s\")\n\n# %% [markdown]\n# ## data-composition\n#\n# > Three subjects with high-density ECoG (two left, one right hemisphere) read aloud CV syllables\n# > made of 18 or 19 consonants followed by /a/, /i/ or /u/, each CV produced 15 to 100 times, with\n# > the microphone recorded with the ECoG at 3052 Hz.\n\n# %% tags=[\"claim:data-composition\"]\ncomp = []\nfor s in B.SUBJECTS:\n    n = S[s][\"counts\"]\n    comp.append({\"subject\": s, \"CVs\": len(S[s][\"cvs\"]), \"consonants\": len({c for c, v in S[s][\"cvs\"]}),\n                 \"vowels\": len({v for c, v in S[s][\"cvs\"]}), \"min_renditions\": int(n.min()), \"max_renditions\": int(n.max()),\n                 \"CVs_below_15\": int((n < 15).sum()), \"CVs_above_100\": int((n > 100).sum()),\n                 \"consonants_with_all_3_vowels_and_15+\": len([c for c in B.CONSONANTS if all((c, v) in S[s][\"cvs\"] and n[S[s][\"cvs\"].index((c, v))] >= 15 for v in \"aiu\")]),\n                 \"hemisphere_from_x\": (\"left\" if np.nanmean(S[s][\"x\"]) < 0 else \"right\") if np.isfinite(S[s][\"x\"]).any() else \"unknown\"})\ncomp = pd.DataFrame(comp)\nprint(comp.to_string(index=False))\nprint(\"Subjects in the dandiset:\", sorted(files.subject.unique()), \"| of the paper's (EC2, EC31, EC33), by assumed correspondence: 3\")\nprint(\"Distinct CVs over the three subjects:\", comp.CVs.sum(), \"(paper 168); with CVs of fewer than 15 renditions left out:\",\n      int((comp.CVs - comp.CVs_below_15).sum()))\nprint(\"ECoG sampling rate:\", sorted(files.rate_hz.unique()), \"Hz (3052 +- 1)\")\nprint(\"Audio in the files: none (removed for HIPAA, dandiset description)\")\n\n# %% [markdown]\n# **Result: partially reproduced.** The dandiset holds the three subjects (taking GP31 and GP33 to\n# be EC31 and EC33) and a fourth one, EC9, that is not in the paper. The ECoG rate is 3051.76 Hz.\n# The counts differ from the paper's: 57, 55 and 57 CVs (169 in all, against 168), each subject with\n# 19 consonants, and renditions of 2 to 107 per CV (EC2's /thi/ 10, GP31's /thi/ 2, GP31 up to 107).\n# Leaving out CVs with fewer than 15 renditions gives 56 + 54 + 57 = 167, still not the paper's\n# split. The audio is not in the dandiset, and GP33's hemisphere cannot be checked.\n\n# %% [markdown]\n# ## active-electrodes\n#\n# > About 30 active vSMC electrodes were found per subject during syllable articulation, an\n# > electrode being active when its high-gamma z-score changed by more than 2 for any syllable.\n\n# %% tags=[\"claim:active-electrodes\"]\nact = []\nfor base in B.BASELINES:\n    for s in B.SUBJECTS:\n        H = HV[s, base]\n        act.append({\"baseline\": base, \"subject\": s, \"vSMC\": H.shape[1],\n                    \"(a) z > 2\": int((np.nanmax(H, axis=(0, 2)) > 2).sum()),\n                    \"(b) |z| > 2\": int((np.nanmax(np.abs(H), axis=(0, 2)) > 2).sum())})\nact = pd.DataFrame(act)\nprint(act.to_string(index=False))\nprint(\"\\nMean over subjects (criterion 27 to 33):\")\nprint(act.groupby(\"baseline\")[[\"(a) z > 2\", \"(b) |z| > 2\"]].mean().round(2).to_string())\nfor thr in (1.5, 2, 2.5, 3):\n    print(f\"threshold {thr}: mean active per subject, pre {np.mean([(np.nanmax(HV[s, 'pre'], axis=(0, 2)) > thr).sum() for s in B.SUBJECTS]):.1f}, \"\n          f\"whole {np.mean([(np.nanmax(HV[s, 'whole'], axis=(0, 2)) > thr).sum() for s in B.SUBJECTS]):.1f}\")\n\n# %% [markdown]\n# **Result: not reproduced.** Under both baseline readings the mean count is below 27: 24.3 per\n# subject with the `pre` baseline (EC2 15, GP31 49, GP33 9) and 21.3 with the whole block, the same\n# under either reading of the change, as no electrode passes on a decrease alone. With the dataset's\n# rest period as baseline (a variant) the mean is 34.0. The count moves with the threshold (table),\n# and the subjects differ widely.\n\n# %% [markdown]\n# ## fig1c-e-articulator-electrodes\n#\n# > In one subject, dorsal electrodes (e124, e108) were active for /b/ (lips), mid vSMC electrodes\n# > (e129, e133, e105) for /d/ (front tongue), and a more ventral electrode (e104) was most active\n# > for /g/ (back tongue).\n\n# %% tags=[\"claim:fig1c-e-articulator-electrodes\"]\nNAMED = {\"b\": [124, 108], \"d\": [129, 133, 105], \"g\": [104]}\nf1 = []\nfor s in B.SUBJECTS:\n    for numbering, offset in ((\"(a) from 1\", 1), (\"(b) from 0\", 0)):\n        idx = {k: [n - offset for n in v] for k, v in NAMED.items()}\n        all_idx = sum(idx.values(), [])\n        on_vsmc = all(i in S[s][\"vsmc\"] for i in all_idx)\n        for base in BASES:\n            for measure in (\"(i) at -25 ms\", \"(ii) peak\"):\n                H = S[s][\"H\"][base]\n                resp = {}\n                for c in \"bdg\":\n                    k = S[s][\"cvs\"].index((c, \"a\"))\n                    resp[c] = H[k, :, B.ms_index(-25)] if measure.startswith(\"(i)\") else np.nanmax(H[k], axis=1)\n                prefers = {i: max(\"bdg\", key=lambda c: resp[c][i]) for i in all_idx}\n                ok = [prefers[i] == c for c, ii in idx.items() for i in ii]\n                f1.append({\"subject\": s, \"numbering\": numbering, \"baseline\": base, \"measure\": measure,\n                           \"all named on vSMC\": on_vsmc, \"labels\": \",\".join(S[s][\"location\"][i][:4] for i in all_idx),\n                           \"preferences (b b d d d g)\": \" \".join(prefers[i] for i in all_idx),\n                           \"named electrodes preferring their syllable\": f\"{sum(ok)} of 6\"})\nf1 = pd.DataFrame(f1)\nprint(f1.to_string(index=False))\nprint(\"\\nSubject and numbering pairs that put all six named electrodes on vSMC:\",\n      f1[f1[\"all named on vSMC\"]][[\"subject\", \"numbering\"]].drop_duplicates().values.tolist())\n\n# %% [markdown]\n# **Result: blocked (metadata_insufficient) or not reproduced, by subject.** In GP33, counted from 1\n# or from 0, all six named electrodes are vSMC electrodes; in EC2 and GP31 at least one is not\n# (table). Where they are, the preferences printed above decide the activity part; the order by\n# distance from the Sylvian fissure cannot be judged, as the dataset gives no such distance. See the\n# summary for the outcome.\n\n# %% [markdown]\n# ## fig1f-h-phonetic-contrasts\n#\n# > Fricatives with different tongue-tip constriction locations engaged different electrodes;\n# > front-tongue consonants of different manner engaged overlapping electrodes with different\n# > magnitudes; for /ja/, /ji/, /ju/ the activity was similar before the C-V transition, while a\n# > dorsal electrode was active during /u/ only.\n#\n# The judged part: in at least one subject, a vSMC electrode with a positive lips weight (from the\n# GLM electrodes of claim fig2a-lips-dorsal) has mean high gamma above 2 at +250 ms for /ju/ and\n# below 2 for /ja/ and /ji/. The lips weights are computed without electrode positions, which are\n# only needed for fig2a's spatial judgement; see the summary for how the dependency is treated.\n\n# %% tags=[\"claim:fig1f-h-phonetic-contrasts\"]\nt250 = B.ms_index(250)\nfh = []\nfor key in W_READINGS:\n    base = key[0]\n    hits = {}\n    for s in B.SUBJECTS:\n        cvs = S[s][\"cvs\"]\n        Hj = {v: HV[s, base][cvs.index((\"y\", v)), :, t250] for v in \"aiu\"}\n        w = WEIGHTS[key][s]\n        cand = w[\"keep\"] & (w[\"W\"][:, 0] > 0)\n        hit = cand & (Hj[\"u\"] > 2) & (Hj[\"a\"] < 2) & (Hj[\"i\"] < 2)\n        hits[s] = (int(cand.sum()), int(hit.sum()))\n    fh.append({\"baseline\": base, \"timing reading\": \" / \".join(key[1]), \"p-value\": key[2],\n               **{f\"{s} lips+ / hits\": f\"{hits[s][0]} / {hits[s][1]}\" for s in B.SUBJECTS},\n               \"holds\": any(h[1] > 0 for h in hits.values())})\nfh = pd.DataFrame(fh)\nprint(fh.to_string(index=False))\nprint(\"\\nReadings where it holds:\", int(fh.holds.sum()), \"of\", len(fh))\n# The /ja/ /ji/ /ju/ traces at the electrode with the largest /ju/ minus /ja/,/ji/ difference among\n# lips-positive electrodes (first reading), per subject.\nfig, axes = plt.subplots(1, 3, figsize=(12, 3), sharey=True)\nkey0 = W_READINGS[0]\nfor ax, s in zip(axes, B.SUBJECTS):\n    cvs = S[s][\"cvs\"]\n    H = HV[s, \"pre\"]\n    w = WEIGHTS[key0][s]\n    cand = np.where(w[\"keep\"] & (w[\"W\"][:, 0] > 0))[0]\n    if len(cand):\n        d = H[cvs.index((\"y\", \"u\")), cand, t250] - np.maximum(H[cvs.index((\"y\", \"a\")), cand, t250], H[cvs.index((\"y\", \"i\")), cand, t250])\n        e = cand[np.argmax(d)]\n        for v in \"aiu\":\n            ax.plot(B.EPOCH_MS, H[cvs.index((\"y\", v)), e], label=f\"/j{v}/\")\n        ax.set_title(f\"{s} vSMC electrode {S[s]['vsmc'][e]}\")\n        print(f\"{s}: plotted electrode {S[s]['vsmc'][e]}, z at +250 ms: \"\n              + \", \".join(f\"/j{v}/ {H[cvs.index(('y', v)), e, t250]:.2f}\" for v in \"aiu\")\n              + f\"; plotted range {H[[cvs.index(('y', v)) for v in 'aiu'], e].min():.2f} to {H[[cvs.index(('y', v)) for v in 'aiu'], e].max():.2f}\")\n    ax.axvline(0, color=\"k\", lw=0.5); ax.axhline(2, color=\"grey\", lw=0.5, ls=\"--\")\naxes[0].legend(); axes[0].set_ylabel(\"z (pre baseline)\")\nplt.show()\n\n# %% [markdown]\n# **Result: see the summary.** The table gives, per reading, the number of GLM electrodes with a\n# positive lips weight and the number that meet the /ju/ rule in each subject.\n\n# %% [markdown]\n# ## Spatial claims (blocked)\n#\n# fig2a-lips-dorsal, fig2b-somatotopic-sequence, suppfig3b-spatial-clustering,\n# suppfig3d-cross-subject, suppfig3f-dv-sequence, suppfig5-intermediate-organization and\n# suppfig7-no-latency-difference all need each electrode's anterior-posterior distance from the\n# central sulcus and dorsal-ventral distance from the Sylvian fissure (Methods). The dandiset gives\n# neither. EC2 and GP31 have x, y, z coordinates with no unit, frame or description; GP33, one of\n# the three subjects, has none. The labels say precentral or postcentral, not how far from either\n# sulcus, and no electrode is labelled as on the guenon. These claims are blocked as\n# metadata_insufficient.\n#\n# The GLM electrode selection and weights of fig2a-lips-dorsal do not need positions and are\n# computed above. For information only (not an outcome), the median z coordinate of the top 10%\n# of lips and tongue weights in the two subjects that have coordinates:\n\n# %%\nkey0 = W_READINGS[0]\nfor s in (\"EC2\", \"GP31\"):\n    w = WEIGHTS[key0][s]\n    z = S[s][\"z\"][S[s][\"vsmc\"]]\n    kept = np.where(w[\"keep\"])[0]\n    out = []\n    for a, name in enumerate(B.ARTICULATORS):\n        if np.isnan(w[\"W\"][kept, a]).all():\n            out.append(f\"{name} no window\"); continue\n        top = kept[np.argsort(-w[\"W\"][kept, a])[:max(1, len(kept) // 10)]]\n        out.append(f\"{name} {np.median(z[top]):.1f}\")\n    print(f\"{s} (reading {key0}): {len(kept)} GLM electrodes; median z of top 10% weights: \" + \", \".join(out))\n\n# %% [markdown]\n# ## suppfig6-mixed-tuning\n#\n# > Single electrodes show a clear preferred articulator and also carry weights for other\n# > articulators.\n\n# %% tags=[\"claim:suppfig6-mixed-tuning\"]\ns6 = []\nfor key in W_READINGS:\n    Wk = np.concatenate([WEIGHTS[key][s][\"W\"][WEIGHTS[key][s][\"keep\"]] for s in B.SUBJECTS])\n    Wk = np.nan_to_num(Wk, nan=-np.inf)\n    pos = np.where(Wk > 0, Wk, 0)\n    has = pos.sum(1) > 0\n    pct = 100 * pos[has] / pos[has].sum(1, keepdims=True)\n    pref = np.argmax(Wk[has], axis=1)\n    groups, ok = {}, True\n    for a in range(4):\n        g = pct[pref == a]\n        if len(g) == 0:\n            groups[B.ARTICULATORS[a]] = \"none\"\n            continue\n        m = g.mean(0)\n        good = np.argmax(m) == a and (np.delete(m, a) > 0).any()\n        ok &= good\n        groups[B.ARTICULATORS[a]] = f\"n={len(g)} \" + \"/\".join(f\"{x:.0f}\" for x in m)\n    s6.append({\"baseline\": key[0], \"timing reading\": \" / \".join(key[1]), \"p-value\": key[2],\n               \"electrodes\": int(len(Wk)), \"no positive weight\": int((~has).sum()), **groups, \"holds\": ok})\ns6 = pd.DataFrame(s6)\nprint(\"Group means of positive weights as % (Lips/Tongue/Larynx/Jaw), electrodes grouped by largest W:\")\nprint(s6.to_string(index=False))\nprint(\"\\nReadings where it holds:\", int(s6.holds.sum()), \"of\", len(s6))\n\n# %% [markdown]\n# **Result: see the summary.**\n\n# %% [markdown]\n# ## fig3d-timing-sequence\n#\n# > Articulator correlations follow a staggered sequence consistent across subjects; lip and tongue\n# > correlations begin well before sound onset, jaw and larynx align to the C-V transition, and the\n# > high and back tongue vowel features peak near the vowel midpoint (~250 ms).\n#\n# Acoustic onset: the dandiset has no audio, so the onset of each CV is taken from the hand-marked\n# syllable start of the trial table (mean over renditions, then over CVs). This replaces the\n# prototype and thresholding of the Methods (a deviation, asked as a question).\n\n# %% tags=[\"claim:fig3d-timing-sequence\"]\nonsets = []\nfor s in B.SUBJECTS:\n    for b in blocks[s]:\n        k = b[\"kept\"]\n        for lab, st, cv in zip(b[\"condition\"][k], b[\"start\"][k], b[\"cv\"][k]):\n            p = B.parse_label(lab)\n            if p:\n                onsets.append({\"subject\": s, \"cv\": p, \"onset_ms\": 1000 * (st - cv)})\nonsets = pd.DataFrame(onsets)\nper_cv = onsets.groupby([\"subject\", \"cv\"]).onset_ms.mean()\nACOUSTIC_ONSET = per_cv.mean()\nprint(f\"Acoustic onset from the annotations: mean over {len(per_cv)} CVs {ACOUSTIC_ONSET:.1f} ms \"\n      f\"(per subject {per_cv.groupby(level=0).mean().round(1).to_dict()}; CV range {per_cv.min():.0f} to {per_cv.max():.0f} ms)\")\nf3 = []\nfor base in BASES:\n    for reading in TIMING_READINGS:\n        t = TIMING[base, reading]\n        for anova in (\"onset\", \"peak\"):\n            F, p = stats.f_oneway(*[t[t.articulator == a][anova] for a in ART6])\n            mo = t.groupby(\"articulator\").onset.mean()\n            mp = t.groupby(\"articulator\").peak.mean()\n            c1 = mo[\"Lips\"] < ACOUSTIC_ONSET and mo[\"Tongue\"] < ACOUSTIC_ONSET\n            c2 = min(mo[\"Jaw\"], mo[\"Larynx\"]) > max(mo[\"Lips\"], mo[\"Tongue\"])\n            c3 = all(abs(mp[a] - 250) <= 25 for a in B.VOWEL_ARTICULATORS)\n            n_ok = c1 + c2 + c3\n            outcome = (\"reproduced\" if p < 1e-10 and n_ok == 3 else\n                       \"partially\" if p < 1e-10 and n_ok == 2 else \"not reproduced\")\n            f3.append({\"baseline\": base, \"timing reading\": \" / \".join(reading), \"ANOVA on\": anova,\n                       \"n\": len(t), **{f\"n {a[:6]}\": int((t.articulator == a).sum()) for a in ART6},\n                       \"F\": round(F, 1), \"p\": p, **{f\"onset {a[:6]}\": round(mo.get(a, np.nan)) for a in ART6},\n                       \"peak Back\": round(mp[\"Back Tongue\"]), \"peak High\": round(mp[\"High Tongue\"]),\n                       \"lips,tongue < acoustic\": c1, \"jaw,larynx later\": c2, \"vowel peaks 250+-25\": c3,\n                       \"outcome\": outcome})\nf3 = pd.DataFrame(f3)\nprint(f3.to_string(index=False))\nprint(\"\\nOutcomes over the readings:\", f3.outcome.value_counts().to_dict())\nprint(\"Total electrodes over articulators and subjects: from\", f3.n.min(), \"to\", f3.n.max(), \"(paper 211 +- 21)\")\nfig, ax = plt.subplots(figsize=(6, 3))\nt = TIMING[\"pre\", TIMING_READINGS[0]]\nfor i, a in enumerate(ART6):\n    g = t[t.articulator == a]\n    ax.errorbar(g.onset.mean(), i, xerr=g.onset.sem(), fmt=\"<\", color=\"C0\")\n    ax.errorbar(g.peak.mean(), i, xerr=g.peak.sem(), fmt=\"o\", color=\"C1\")\n    ax.errorbar(g.offset.mean(), i, xerr=g.offset.sem(), fmt=\">\", color=\"C2\")\nax.axvline(ACOUSTIC_ONSET, color=\"grey\", ls=\"--\"); ax.axvline(0, color=\"k\", lw=0.5)\nax.set_yticks(range(6)); ax.set_yticklabels(ART6); ax.set_xlabel(\"ms (first reading, pre baseline)\")\nplt.show()\n\n# %% [markdown]\n# **Result: see the summary.**\n\n# %% [markdown]\n# ## pca-nine-components\n#\n# > The cortical state-space has nine spatial PCs in every subject, the eigenvalues falling fast up\n# > to the ninth and slowly after, together explaining about 60% of the variance.\n\n# %% tags=[\"claim:pca-nine-components\"]\npc = []\nfor base in BASES:\n    for z in ZMODES:\n        for w in [(-500, 750), (-375, 620)]:\n            fr = {s: STATE[s, base, z, w][1] for s in B.SUBJECTS}\n            pc.append({\"baseline\": base, \"z-scoring\": z, \"window\": f\"{w[0]} to {w[1]}\",\n                       **{s: round(fr[s][:9].sum(), 3) for s in B.SUBJECTS},\n                       \"mean\": round(np.mean([fr[s][:9].sum() for s in B.SUBJECTS]), 3)})\npc = pd.DataFrame(pc)\npc[\"within 0.54-0.66\"] = pc[\"mean\"].between(0.54, 0.66)\nprint(pc.to_string(index=False))\nprint(\"\\nRest-baseline variant (row, epoch):\", {s: round(B.state_space(HV[s, \"rest\"], \"row\")[1][:9].sum(), 3) for s in B.SUBJECTS})\nfig, axes = plt.subplots(1, 2, figsize=(10, 3))\nfor ax, z in zip(axes, ZMODES):\n    for s in B.SUBJECTS:\n        ax.plot(np.arange(1, 21), 100 * STATE[s, \"pre\", z, (-500, 750)][1][:20], \"o-\", ms=3, label=s)\n    ax.axvline(9, color=\"grey\", ls=\"--\"); ax.set_title(f\"pre baseline, {z} z-scoring\"); ax.set_xlabel(\"PC\"); ax.set_ylabel(\"% variance\")\naxes[0].legend(); plt.show()\nprint(\"% variance of PCs 1 to 12, pre baseline, epoch:\")\nfor z in ZMODES:\n    for s in B.SUBJECTS:\n        print(z, s, np.round(100 * STATE[s, \"pre\", z, (-500, 750)][1][:12], 1))\n\n# %% [markdown]\n# **Result: see the summary.**\n\n# %% [markdown]\n# ## fig4a-consonant-clusters\n#\n# > At the consonant time (-25 ms) k-means clustering of the cortical state-space groups syllables\n# > by major oral articulator, and three clusters are more parsimonious than two or four (mean\n# > silhouette 0.47 against 0.45 and 0.43).\n\n# %% tags=[\"claim:fig4a-consonant-clusters\"]\nrng_seed = 4\ntc, tv = B.ms_index(-25), B.ms_index(250)\nsil = []\nfor base, z in SS_READINGS:\n    for s in B.SUBJECTS:\n        K = STATE[s, base, z, (-500, 750)][2][:, :, tc]\n        row = {\"baseline\": base, \"z-scoring\": z, \"subject\": s}\n        for k in (2, 3, 4):\n            row[f\"k={k}\"] = silhouette_score(K, B.kmeans(K, k, seed=rng_seed + k))\n        sil.append(row)\nsil = pd.DataFrame(sil)\nprint(sil.round(3).to_string(index=False))\nmeans = sil.groupby([\"baseline\", \"z-scoring\"])[[\"k=2\", \"k=3\", \"k=4\"]].mean()\nmeans[\"k=3 highest\"] = means.idxmax(axis=1) == \"k=3\"\nmeans[\"all within 10%\"] = (abs(means[\"k=2\"] - 0.45) <= 0.045) & (abs(means[\"k=3\"] - 0.47) <= 0.047) & (abs(means[\"k=4\"] - 0.43) <= 0.043)\nprint(\"\\nMean over subjects (paper 0.45, 0.47, 0.43):\")\nprint(means.round(3).to_string())\n\n# %% [markdown]\n# **Result: see the summary.**\n\n# %% [markdown]\n# ## suppfig11-co-clustering\n#\n# > Clusters of the cortical state-space match the major articulators at the consonant time\n# > (median co-clustering 0.50 against 0.32 by chance) and the vowels at the vowel time (0.65\n# > against 0.37), across subjects.\n\n# %% tags=[\"claim:suppfig11-co-clustering\"]\nrng = np.random.default_rng(11)\ncc = []\nfor base, z in SS_READINGS:\n    obs = {\"cons a\": [], \"cons b\": [], \"vowel\": []}\n    null = {\"cons a\": [], \"cons b\": [], \"vowel\": []}\n    for s in B.SUBJECTS:\n        K = STATE[s, base, z, (-500, 750)][2]\n        nc_c = B.kmeans(K[:, :, tc], 3, seed=21)\n        nc_v = B.kmeans(K[:, :, tv], 3, seed=22)\n        for name, nc, labs in ((\"cons a\", nc_c, [B.MAJOR[\"a\"].get(c) for c, v in S[s][\"cvs\"]]),\n                               (\"cons b\", nc_c, [B.MAJOR[\"b\"].get(c) for c, v in S[s][\"cvs\"]]),\n                               (\"vowel\", nc_v, [v for c, v in S[s][\"cvs\"]])):\n            keep = np.array([l is not None for l in labs])\n            ac = np.array([l for l in labs if l is not None])\n            ncs = nc[keep]\n            obs[name].append(B.co_clustering(ncs, ac))\n            perm = np.mean([B.co_clustering(ncs, rng.permutation(ac)) for _ in range(1000)], axis=0)\n            null[name].append(perm)\n    for name in obs:\n        o, n = np.concatenate(obs[name]), np.concatenate(null[name])\n        w = stats.wilcoxon(o, n)\n        cc.append({\"baseline\": base, \"z-scoring\": z, \"labels\": name, \"n CVs\": len(o),\n                   \"median observed\": round(np.median(o), 3), \"median null\": round(np.median(n), 3),\n                   \"Wilcoxon p\": w.pvalue, \"observed > null\": np.median(o - n) > 0})\ncc = pd.DataFrame(cc)\nprint(cc.to_string(index=False))\nprint(\"Expected: consonants 0.50 +- 0.05 against 0.32 +- 0.032; vowels 0.65 +- 0.065 against 0.37 +- 0.037; p < 1e-10\")\n\n# %% [markdown]\n# **Result: see the summary.**\n\n# %% [markdown]\n# ## fig4c-d-hierarchy\n#\n# > Hierarchical clustering of the state-space puts the major oral articulator at the top tier for\n# > consonants; for vowels the first split is lip rounding (/u/ against /a/ and /i/).\n\n# %% tags=[\"claim:fig4c-d-hierarchy\"]\nhc = []\nfor base, z in SS_READINGS:\n    for s in B.SUBJECTS:\n        K = STATE[s, base, z, (-500, 750)][2]\n        cons_cut = fcluster(linkage(K[:, :, tc], \"ward\"), 3, \"maxclust\")\n        vow_cut = fcluster(linkage(K[:, :, tv], \"ward\"), 2, \"maxclust\")\n        row = {\"baseline\": base, \"z-scoring\": z, \"subject\": s}\n        for lr in (\"a\", \"b\"):\n            labs = np.array([B.MAJOR[lr].get(c, \"\") for c, v in S[s][\"cvs\"]])\n            lab = labs != \"\"\n            maj_of_cluster = {k: pd.Series(labs[lab & (cons_cut == k)]).mode().tolist() for k in (1, 2, 3)}\n            distinct = len({tuple(v) for v in maj_of_cluster.values()}) == 3 and all(len(v) == 1 for v in maj_of_cluster.values())\n            home = {a: pd.Series(cons_cut[lab & (labs == a)]).mode()[0] for a in (\"labial\", \"coronal\", \"dorsal\")}\n            purity = np.mean([cons_cut[i] == home[labs[i]] for i in np.where(lab)[0]])\n            row[f\"cons ({lr}) majorities\"] = \"/\".join(v[0] if len(v) == 1 else \"tie\" for v in maj_of_cluster.values())\n            row[f\"cons ({lr}) in home cluster\"] = round(purity, 2)\n            row[f\"cons ({lr}) holds\"] = bool(distinct and purity >= 2 / 3)\n            row[f\"cons ({lr}) co-clustering median\"] = round(np.median(B.co_clustering(cons_cut[lab], labs[lab])), 2)\n        vow = np.array([v for c, v in S[s][\"cvs\"]])\n        ok = False\n        for ku in (1, 2):\n            other = 3 - ku\n            ok |= (vow_cut[vow == \"u\"] == ku).mean() > 0.5 and (vow_cut[vow != \"u\"] == other).mean() > 0.5\n        row[\"vowel: u in one, a+i in other\"] = \"/\".join(f\"{(vow_cut[vow == v] == 1).mean():.2f}\" for v in \"aiu\")\n        row[\"vowel holds\"] = bool(ok)\n        hc.append(row)\nhc = pd.DataFrame(hc)\nprint(hc.to_string(index=False))\nprint(\"(vowel column: fraction of /a/, /i/, /u/ CVs in cluster 1 of the two-cluster cut)\")\n\n# %% [markdown]\n# **Result: see the summary.**\n\n# %% [markdown]\n# ## fig4ef-feature-correlations\n#\n# > Over early times (-375 to 120 ms) constriction location correlates with the state-space\n# > structure more than constriction degree, which correlates more than the upcoming vowel; over\n# > later times (125 to 620 ms) vowel configuration correlates most.\n\n# %% tags=[\"claim:fig4ef-feature-correlations\"]\nFEATS = (\"location\", \"degree\", \"vowel\")\n\n\ndef feature_r(base, z, metric=\"euclidean\"):\n    \"\"\"R(t) per subject and feature set (Methods Eq. 7): (subject, set, time).\"\"\"\n    out = {}\n    for s in B.SUBJECTS:\n        K = STATE[s, base, z, (-500, 750)][2]\n        dK = np.array([pdist(K[:, :, t]) for t in range(K.shape[2])])\n        for f in FEATS:\n            dP = pdist(B.feature_matrix(S[s][\"cvs\"], f), metric)\n            out[s, f] = np.array([np.corrcoef(d, dP)[0, 1] for d in dK])\n    return out\n\n\nearly = (B.EPOCH_MS >= -375) & (B.EPOCH_MS < 120)\nlate = (B.EPOCH_MS >= 125) & (B.EPOCH_MS < 620)\nRT = {(base, z): feature_r(base, z) for base, z in SS_READINGS}\nfe = []\nfor (base, z), R in RT.items():\n    for metric in (\"euclidean\", \"hamming\"):\n        Rm = R if metric == \"euclidean\" else feature_r(base, z, \"hamming\")\n        e = {f: np.concatenate([Rm[s, f][early] for s in B.SUBJECTS]) for f in FEATS}\n        l = {f: np.concatenate([Rm[s, f][late] for s in B.SUBJECTS]) for f in FEATS}\n        tests = {\"early loc>deg\": (e[\"location\"], e[\"degree\"]), \"early deg>vow\": (e[\"degree\"], e[\"vowel\"]),\n                 \"late vow>loc\": (l[\"vowel\"], l[\"location\"]), \"late vow>deg\": (l[\"vowel\"], l[\"degree\"])}\n        row = {\"baseline\": base, \"z-scoring\": z, \"distance\": metric, \"n\": len(e[\"location\"])}\n        for name, (a, b) in tests.items():\n            p = stats.wilcoxon(a, b).pvalue\n            row[name] = f\"{np.median(a - b):+.3f} p={p:.1e}\"\n            row[name + \" ok\"] = bool(np.median(a - b) > 0 and p < 1e-10)\n        row[\"medians early L/D/V\"] = \"/\".join(f\"{np.median(e[f]):.2f}\" for f in FEATS)\n        row[\"medians late L/D/V\"] = \"/\".join(f\"{np.median(l[f]):.2f}\" for f in FEATS)\n        fe.append(row)\nfe = pd.DataFrame(fe)\nprint(fe.to_string(index=False))\n\n# %% [markdown]\n# **Result: see the summary.**\n\n# %% [markdown]\n# ## fig5c-separability-timing\n#\n# > Cluster separability, averaged over subjects, rises from about -300 ms and peaks about 200 ms\n# > before the C-V transition for consonants, and rises from about 50 ms and peaks at +250 ms for\n# > vowels.\n\n# %% tags=[\"claim:fig5c-separability-timing\"]\nrng5 = np.random.default_rng(5)\nN_BOOT = 1000\n\n\ndef cluster_labels(s, K, which, kind):\n    \"\"\"Labels per CV (or per time and CV for k-means); -1 for CVs left out.\"\"\"\n    cvs = S[s][\"cvs\"]\n    if kind == \"kmeans\":\n        return np.array([B.kmeans(K[:, :, t], 3, seed=1000 + t, n_init=20) for t in range(K.shape[2])])\n    if which == \"vowel\":\n        return np.array([\"aiu\".index(v) for c, v in cvs])\n    lr = kind[-1]\n    names = {\"labial\": 0, \"coronal\": 1, \"dorsal\": 2}\n    out = []\n    for c, v in cvs:\n        m = B.MAJOR[lr].get(c)\n        if kind.startswith(\"four\") and c in B.SIBILANTS:\n            out.append(3)\n        else:\n            out.append(names[m] if m else -1)\n    return np.array(out)\n\n\nSEP_KINDS = {\"consonant\": [\"groups a\", \"groups b\", \"four a\", \"four b\", \"kmeans\"],\n             \"vowel\": [\"groups\", \"kmeans\"]}\n\n\ndef separability_curves(base, z):\n    out = {}\n    for which, kinds in SEP_KINDS.items():\n        for kind in kinds:\n            curves, boots = [], []\n            for s in B.SUBJECTS:\n                K = STATE[s, base, z, (-500, 750)][2]\n                lab = cluster_labels(s, K, which, kind)\n                keep = (lab >= 0) if lab.ndim == 1 else np.ones(K.shape[0], bool)\n                Ks = K[keep]\n                labk = lab[keep] if lab.ndim == 1 else lab[:, keep]\n                D = np.array([squareform(pdist(Ks[:, :, t])) for t in range(Ks.shape[2])])\n                curves.append(B.separability(D, labk)[0])\n                wts = rng5.multinomial(len(Ks), np.ones(len(Ks)) / len(Ks), size=N_BOOT)\n                boots.append(B.separability(D, labk, wts))\n            out[which, kind] = (np.mean(curves, 0), np.mean(boots, 0).std(0), curves)\n    return out\n\n\nSEP = {(base, z): separability_curves(base, z) for base, z in SS_READINGS}\n\n\ndef onset_peak(curve, se):\n    p = int(np.argmax(curve))\n    above = np.where(curve[:p + 1] > curve[0] + 2 * se[:p + 1])[0]\n    on_a = B.EPOCH_MS[above[0]] if len(above) else np.nan\n    below = np.where(curve[:p + 1] < curve[p] / 2)[0]\n    on_b = B.EPOCH_MS[below[-1] + 1] if len(below) else np.nan\n    return B.EPOCH_MS[p], on_a, on_b\n\n\nsp = []\nfor (base, z), d in SEP.items():\n    for ck in SEP_KINDS[\"consonant\"]:\n        for vk in SEP_KINDS[\"vowel\"]:\n            if (ck == \"kmeans\") != (vk == \"kmeans\"):\n                continue\n            cpk, con_a, con_b = onset_peak(d[\"consonant\", ck][0], d[\"consonant\", ck][1])\n            vpk, von_a, von_b = onset_peak(d[\"vowel\", vk][0], d[\"vowel\", vk][1])\n            peaks_ok = abs(cpk + 200) <= 20 and abs(vpk - 250) <= 25\n            ons = {\"(a) 2 s.e.\": (con_a, von_a), \"(b) half peak\": (con_b, von_b)}\n            ons_ok = {k: abs(v[0] + 300) <= 30 and abs(v[1] - 50) <= 10 for k, v in ons.items()}\n            sp.append({\"baseline\": base, \"z-scoring\": z, \"clusters\": f\"{ck} | {vk}\",\n                       \"cons peak\": cpk, \"cons onset a\": con_a, \"cons onset b\": con_b,\n                       \"vowel peak\": vpk, \"vowel onset a\": von_a, \"vowel onset b\": von_b,\n                       \"peaks ok\": peaks_ok, \"onsets ok (a)\": ons_ok[\"(a) 2 s.e.\"], \"onsets ok (b)\": ons_ok[\"(b) half peak\"],\n                       \"outcome\": \"reproduced\" if peaks_ok and any(ons_ok.values()) else (\"partially\" if peaks_ok else \"not reproduced\")})\nsp = pd.DataFrame(sp)\nprint(sp.to_string(index=False))\nprint(\"Expected: consonant peak -200 +- 20, onset -300 +- 30; vowel peak 250 +- 25, onset 50 +- 10 ms\")\nfig, axes = plt.subplots(1, 2, figsize=(11, 3))\nfor ax, (base, z) in zip(axes, [(\"pre\", \"row\"), (\"pre\", \"time\")]):\n    d = SEP[base, z]\n    for (which, kind), (c, se, _) in d.items():\n        ax.plot(B.EPOCH_MS, c, label=f\"{which} {kind}\")\n    ax.axvline(0, color=\"k\", lw=0.5); ax.set_title(f\"{base}, {z}\"); ax.set_xlabel(\"ms\")\naxes[0].legend(fontsize=7); axes[0].set_ylabel(\"separability\")\nplt.show()\nfor (base, z), d in SEP.items():\n    print(base, z, \"curve ranges:\", {f\"{w} {k}\": (round(c.min(), 2), round(c.max(), 2)) for (w, k), (c, se, _) in d.items()})\n\n# %% [markdown]\n# **Result: see the summary.**\n\n# %% [markdown]\n# ## fig5d-separability-coupling\n#\n# > Cluster separability and the correlation of the state-space with phonetic features are tightly\n# > linked over time for consonants and vowels in each subject (R2 0.42 to 0.98, all P < 1e-10).\n\n# %% tags=[\"claim:fig5d-separability-coupling\"]\nc5 = []\nfor (base, z), d in SEP.items():\n    R = RT[base, z]\n    for ck in SEP_KINDS[\"consonant\"]:\n        for vk in SEP_KINDS[\"vowel\"]:\n            if (ck == \"kmeans\") != (vk == \"kmeans\"):\n                continue\n            for rmode in (\"(a) matching set\", \"(b) mean of three\"):\n                vals = []\n                for i, s in enumerate(B.SUBJECTS):\n                    for which, kind, fset in ((\"consonant\", ck, \"location\"), (\"vowel\", vk, \"vowel\")):\n                        sepc = d[which, kind][2][i]\n                        r = R[s, fset] if rmode.startswith(\"(a)\") else np.mean([R[s, f] for f in FEATS], 0)\n                        res = stats.pearsonr(sepc, r)\n                        vals.append((res.statistic ** 2, res.pvalue, res.statistic))\n                r2 = np.array([v[0] for v in vals]); ps = np.array([v[1] for v in vals]); rs = np.array([v[2] for v in vals])\n                ok = bool((r2 >= 0.378).all() and (ps < 1e-10).all() and (rs > 0).all())\n                part = bool((rs > 0).all() and (ps < 1e-10).all())\n                c5.append({\"baseline\": base, \"z-scoring\": z, \"clusters\": f\"{ck} | {vk}\", \"R\": rmode,\n                           \"R2 (EC2 c,v GP31 c,v GP33 c,v)\": \" \".join(f\"{x:.2f}\" for x in r2),\n                           \"max p\": ps.max(), \"min r\": round(rs.min(), 2),\n                           \"outcome\": \"reproduced\" if ok else (\"partially\" if part else \"not reproduced\")})\nc5 = pd.DataFrame(c5)\nprint(c5.to_string(index=False))\nprint(\"\\nOutcomes over readings:\", c5.outcome.value_counts().to_dict())\n\n# %% [markdown]\n# **Result: see the summary.**\n\n# %% [markdown]\n# ## suppfig13-consonant-vowel-distance\n#\n# > Consonant and vowel representations occupy distinct regions of the state-space;\n# > consonant-vowel distances are larger than consonant-consonant and vowel-vowel distances, and\n# > consonant-consonant distances are larger than vowel-vowel ones.\n\n# %% tags=[\"claim:suppfig13-consonant-vowel-distance\"]\ncvd = []\nfor base, z in SS_READINGS:\n    for reading in (\"(a) mean of cross pairings\", \"(b) i at -25, j at +250\"):\n        CC, VV, CVd = [], [], []\n        for s in B.SUBJECTS:\n            K = STATE[s, base, z, (-500, 750)][2]\n            Kc, Kv = K[:, :, tc], K[:, :, tv]\n            i, j = np.triu_indices(len(Kc), 1)\n            CC.append(np.linalg.norm(Kc[i] - Kc[j], axis=1))\n            VV.append(np.linalg.norm(Kv[i] - Kv[j], axis=1))\n            d1 = np.linalg.norm(Kc[i] - Kv[j], axis=1)\n            d2 = np.linalg.norm(Kc[j] - Kv[i], axis=1)\n            CVd.append((d1 + d2) / 2 if reading.startswith(\"(a)\") else d1)\n        CC, VV, CVd = map(np.concatenate, (CC, VV, CVd))\n        row = {\"baseline\": base, \"z-scoring\": z, \"CV distance\": reading, \"pairs\": len(CC),\n               \"median CC\": round(np.median(CC), 2), \"median VV\": round(np.median(VV), 2), \"median CV\": round(np.median(CVd), 2)}\n        ok = True\n        for name, (a, b) in {\"CV>CC\": (CVd, CC), \"CV>VV\": (CVd, VV), \"CC>VV\": (CC, VV)}.items():\n            p = min(1.0, 3 * stats.wilcoxon(a, b).pvalue)\n            row[name] = f\"{np.median(a - b):+.2f} p={p:.1e}\"\n            ok &= bool(np.median(a - b) > 0 and p < 1e-10)\n        row[\"orderings hold\"] = ok\n        cvd.append(row)\ncvd = pd.DataFrame(cvd)\nprint(cvd.to_string(index=False))\nprint(\"Pairs within subjects:\", {s: len(S[s][\"cvs\"]) * (len(S[s][\"cvs\"]) - 1) // 2 for s in B.SUBJECTS}, \"(paper n = 4623)\")\n\n# %% [markdown]\n# **Result: see the summary.**\n\n# %% [markdown]\n# ## suppfig9-pc-articulator-weights\n#\n# > The first three PCs are weighted toward tongue over lips, and toward lips over jaw and larynx,\n# > while jaw and larynx do not differ.\n\n# %% tags=[\"claim:suppfig9-pc-articulator-weights\"]\npairs6 = list(itertools.combinations(range(4), 2))\ns9 = []\nfor (base, reading, pmode) in W_READINGS:\n    for z in ZMODES:\n        for eset in (\"all vSMC\", \"GLM electrodes\"):\n            if eset == \"all vSMC\" and pmode == \"t-test\":\n                continue    # the p-value reading only changes which electrodes are kept\n            vals = []\n            for s in B.SUBJECTS:\n                w = WEIGHTS[base, reading, pmode][s]\n                M = STATE[s, base, z, (-500, 750)][0]\n                sel = w[\"keep\"] if eset == \"GLM electrodes\" else np.ones(len(w[\"keep\"]), bool)\n                vals.append(np.log10(np.abs(M[sel, :3, None] * w[\"W\"][sel, None, :])))\n            V = np.concatenate(vals)            # (electrode, PC, articulator)\n            V = V[np.isfinite(V).all(axis=(1, 2))]\n            per_pc = []\n            for pci in range(3):\n                p = {}\n                for a, b in pairs6:\n                    d = V[:, pci, a] - V[:, pci, b]\n                    p[a, b] = (np.median(d), min(1.0, 6 * stats.wilcoxon(V[:, pci, a], V[:, pci, b]).pvalue))\n                L, T, X, J = 0, 1, 2, 3\n                def greater(a, b, alpha):\n                    m, pv = p[(a, b)] if (a, b) in p else (-p[(b, a)][0], p[(b, a)][1])\n                    return m > 0 and pv < alpha\n                tl = greater(T, L, 0.05)\n                ra = greater(L, J, 0.001) and greater(L, X, 0.001)\n                rb = ra and greater(T, J, 0.001) and greater(T, X, 0.001)\n                jx = p[(X, J)][1] > 0.05\n                per_pc.append(bool(tl and (ra or rb) and jx))\n            n_ok = sum(per_pc)\n            s9.append({\"baseline\": base, \"timing reading\": \" / \".join(reading), \"p-value\": pmode, \"z-scoring\": z,\n                       \"electrodes\": eset, \"n\": len(V), \"PCs holding\": \"\".join(\"Y\" if x else \"n\" for x in per_pc),\n                       \"outcome\": \"reproduced\" if n_ok == 3 else (\"partially\" if n_ok else \"not reproduced\")})\ns9 = pd.DataFrame(s9)\nprint(s9.to_string(index=False))\nprint(\"\\nOutcomes over readings:\", s9.outcome.value_counts().to_dict())\n# One reading in full: medians of log10|PCw| per articulator and corrected p of every pair.\nbase, reading, pmode, z = \"pre\", TIMING_READINGS[0], \"F-test\", \"row\"\nV = np.concatenate([np.log10(np.abs(STATE[s, base, z, (-500, 750)][0][:, :3, None] * WEIGHTS[base, reading, pmode][s][\"W\"][:, None, :])) for s in B.SUBJECTS])\nV = V[np.isfinite(V).all(axis=(1, 2))]\nfor pci in range(3):\n    med = {B.ARTICULATORS[a]: round(np.median(V[:, pci, a]), 2) for a in range(4)}\n    ps = {f\"{B.ARTICULATORS[a][:2]}-{B.ARTICULATORS[b][:2]}\": f\"{min(1, 6 * stats.wilcoxon(V[:, pci, a], V[:, pci, b]).pvalue):.1e}\" for a, b in pairs6}\n    print(f\"PC{pci + 1} ({base}, {reading}, all vSMC, n={len(V)}): medians {med}; corrected p {ps}\")\n\n# %% [markdown]\n# **Result: see the summary.**\n\n# %% [markdown]\n# ## Summary\n\n# %%\nprint(f\"notebook ran in {(time.time() - started) / 60:.1f} min\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > conv.py <<'EOF'
import re, sys, nbformat
src=open(sys.argv[1]).read()
parts=re.split(r'^# %%(.*)$', src, flags=re.M)
cells=[]
for i in range(1,len(parts),2):
    hdr, body = parts[i], parts[i+1].strip('\n')
    if '[markdown]' in hdr:
        lines=[l[2:] if l.startswith('# ') else l.lstrip('#') for l in body.split('\n')]
        cells.append(nbformat.v4.new_markdown_cell('\n'.join(lines)))
    else:
        c=nbformat.v4.new_code_cell(body)
        m=re.search(r'tags=(\[.*\])',hdr)
        if m: c.metadata['tags']=eval(m.group(1))
        cells.append(c)
nb=nbformat.v4.new_notebook(cells=cells)
nb.metadata['kernelspec']={'name':'python3','display_name':'Python 3','language':'python'}
nbformat.write(nb, sys.argv[2])
EOF
cat > devrun.py <<'EOF'
# Execute nb.py cells with cached data in place of streaming.
import re, sys, pickle, os, time
sys.path.insert(0,'entries/000019-bouchard-2013')
os.chdir('/tmp/claude-1001')
import matplotlib; matplotlib.use('Agg')
src=open('nb.py').read()
parts=re.split(r'^# %%(.*)$', src, flags=re.M)
cells=[(parts[i],parts[i+1]) for i in range(1,len(parts),2) if '[markdown]' not in parts[i]]
start=int(sys.argv[1]) if len(sys.argv)>1 else 0
g={}
for k,(h,body) in enumerate(cells):
    if 'B.process_blocks' in body:
        body="import pickle\nS={}\nblocks={}\nfor s in B.SUBJECTS:\n    S[s],blocks[s]=pickle.load(open(f'sub_{s}.pkl','rb'))\n"
    if 'ASSETS = B.assets()' in body and os.path.exists('meta_rows.pkl'):
        body="import pickle\nASSETS=B.assets()\nmeta_rows=pickle.load(open('meta_rows.pkl','rb'))\n"
    t=time.time()
    print(f'===== cell {k} {h.strip()}'); sys.stdout.flush()
    exec(compile(body,f'cell{k}','exec'),g)
    if 'meta_rows' in g and not os.path.exists('meta_rows.pkl'): pickle.dump(g['meta_rows'],open('meta_rows.pkl','wb'))
    print(f'----- {time.time()-t:.1f}s'); sys.stdout.flush()
EOF
. work/bin/activate && python devrun.py 2>&1 | tail -150
```

```
pre      time groups b | groups  (a) matching set  0.92 0.97 0.65 0.97 0.40 0.92 4.407971e-29   0.63     reproduced
     pre      time groups b | groups (b) mean of three  0.00 0.64 0.72 0.19 0.02 0.29 5.124998e-01  -0.44 not reproduced
     pre      time   four a | groups  (a) matching set  0.78 0.97 0.72 0.97 0.59 0.92 9.214609e-50   0.77     reproduced
     pre      time   four a | groups (b) mean of three  0.04 0.64 0.73 0.19 0.02 0.29 4.232537e-02  -0.44 not reproduced
     pre      time   four b | groups  (a) matching set  0.78 0.97 0.68 0.97 0.52 0.92 2.242277e-41   0.72     reproduced
     pre      time   four b | groups (b) mean of three  0.03 0.64 0.72 0.19 0.02 0.29 3.959789e-02  -0.44 not reproduced
     pre      time   kmeans | kmeans  (a) matching set  0.25 0.01 0.22 0.05 0.10 0.01 2.462009e-01  -0.46 not reproduced
     pre      time   kmeans | kmeans (b) mean of three  0.12 0.12 0.10 0.10 0.04 0.04 1.212783e-03  -0.31 not reproduced
   whole       row groups a | groups  (a) matching set  0.89 0.94 0.87 0.97 0.56 0.87 9.930735e-47   0.75     reproduced
   whole       row groups a | groups (b) mean of three  0.17 0.27 0.82 0.30 0.14 0.12 2.172713e-08  -0.55 not reproduced
   whole       row groups b | groups  (a) matching set  0.87 0.94 0.86 0.97 0.48 0.87 1.024428e-36   0.69     reproduced
   whole       row groups b | groups (b) mean of three  0.16 0.27 0.85 0.30 0.10 0.12 2.374137e-07  -0.55 not reproduced
   whole       row   four a | groups  (a) matching set  0.84 0.94 0.87 0.97 0.67 0.87 4.037112e-61   0.82     reproduced
   whole       row   four a | groups (b) mean of three  0.12 0.27 0.82 0.30 0.10 0.12 2.758712e-07  -0.55 not reproduced
   whole       row   four b | groups  (a) matching set  0.83 0.94 0.84 0.97 0.58 0.87 4.945629e-49   0.76     reproduced
   whole       row   four b | groups (b) mean of three  0.12 0.27 0.85 0.30 0.09 0.12 2.074469e-06  -0.55 not reproduced
   whole       row   kmeans | kmeans  (a) matching set  0.65 0.02 0.0
[... 134 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && python devrun.py > dev.out 2>&1; grep -n "=====" dev.out | head -40; wc -l dev.out
```

```
1:===== cell 0 
3:===== cell 1 
5:===== cell 2 
7:===== cell 3 tags=["sanity"]
56:===== cell 4 tags=["sanity"]
60:===== cell 5 tags=["sanity"]
71:===== cell 6 tags=["sanity"]
89:===== cell 7 tags=["sanity"]
129:===== cell 8 tags=["sanity"]
137:===== cell 9 
140:===== cell 10 tags=["claim:data-composition"]
150:===== cell 11 tags=["claim:active-electrodes"]
173:===== cell 12 tags=["claim:fig1c-e-articulator-electrodes"]
202:===== cell 13 tags=["claim:fig1f-h-phonetic-contrasts"]
242:===== cell 14 
246:===== cell 15 tags=["claim:suppfig6-mixed-tuning"]
284:===== cell 16 tags=["claim:fig3d-timing-sequence"]
323:===== cell 17 tags=["claim:pca-nine-components"]
343:===== cell 18 tags=["claim:fig4a-consonant-clusters"]
366:===== cell 19 tags=["claim:suppfig11-co-clustering"]
[... 9 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/dev.out",
 "limit": 250
}
```

```
1	===== cell 0 
2	----- 1.2s
3	===== cell 1 
4	----- 3.4s
5	===== cell 2 
6	----- 0.1s
7	===== cell 3 tags=["sanity"]
8	Dandiset: Human ECoG speaking consonant-vowel syllables | version 0.220126.2148 | DOI 10.48324/dandi.000019/0.220126.2148
9	Related resource: [('dcite:IsDescribedBy', 'DOI:0.1038/nature11911', 'https://doi.org/10.1038/nature11911')]
10	Assets summary: subjects 4 | files 31
11	                     file subject  rate_hz  minutes  channels unit  conversion  trials  speak  bad  rest_s  invalid_intervals  has_xyz  mean_x electrode_ids
12	   sub-EC2_ses-EC2-B1.nwb     EC2  3051.76    10.78       256 volt         0.0     387    387    0   41.00                  6     True   -57.1         0-255
13	 sub-EC2_ses-EC2-B105.nwb     EC2  3051.76    11.62       256 volt         0.0     311    311    0   10.00                  5     True   -57.1         0-255
14	  sub-EC2_ses-EC2-B15.nwb     EC2  3051.76     9.58       256 volt         0.0     382    382    7   57.00                  7     True   -57.1         0-255
15	  sub-EC2_ses-EC2-B76.nwb     EC2  3051.76    11.20       256 volt         0.0     389    389   10   57.00                 28     True   -57.1         0-255
16	   sub-EC2_ses-EC2-B8.nwb     EC2  3051.76    10.02       256 volt         0.0     384    384    7   15.00                  4     True   -57.1         0-255
17	  sub-EC2_ses-EC2-B89.nwb     EC2  3051.76    10.00       256 volt         0.0     397    397   10   61.00                 11     True   -57.1         0-255
18	   sub-EC2_ses-EC2-B9.nwb     EC2  3051.76     9.42       256 volt         0.0     378    378    9   45.00                 13     True   -57.1         0-255
19	  sub-EC9_ses-EC9-B15.nwb     EC9  3051.76     3.25       256 volt         0.0      70     70    0    7.00                 25    False     NaN         1-256
20	  sub-EC9_ses-EC9-B39.nwb     EC9  3051.76    15.62       256 volt         0.0     280    278    1    6.00                 12    False     NaN         1-256
[... 230 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/dev.out",
 "offset": 250,
 "limit": 240
}
```

```
250	     pre         per subject / all six / threshold  t-test         103                   0  n=29 76/1/5/18   n=8 0/83/6/11  n=14 9/10/68/13   n=52 7/7/5/82   True
251	     pre         per subject / all six / half peak  F-test          82                   0  n=26 73/1/4/22    n=6 1/85/7/8    n=9 13/8/71/8  n=41 10/9/2/79   True
252	     pre         per subject / all six / half peak  t-test          62                   0  n=22 75/1/3/21   n=3 3/85/2/10   n=5 17/2/70/11  n=32 10/7/2/81   True
253	     pre per subject / per articulator / threshold  F-test         110                   0 n=30 65/10/6/19 n=14 16/65/8/12  n=13 5/16/68/12  n=53 8/10/4/77   True
254	     pre per subject / per articulator / threshold  t-test          92                   0 n=23 63/14/4/19  n=10 20/68/5/6  n=12 4/12/71/13  n=47 6/11/3/80   True
255	     pre per subject / per articulator / half peak  F-test          75                   0  n=24 69/9/3/18   n=7 4/74/5/16   n=7 15/14/63/8  n=37 9/14/5/72   True
256	     pre per subject / per articulator / half peak  t-test          58                   0 n=18 67/13/4/16  n=5 25/53/5/16   n=6 12/12/67/9  n=29 7/13/3/76   True
257	     pre              pooled / all six / threshold  F-test         101                   0  n=31 71/1/4/24    n=4 0/91/4/6   n=14 5/2/75/18   n=52 9/5/5/82   True
258	     pre              pooled / all six / threshold  t-test          99                   0  n=24 74/0/4/22   n=5 2/82/4/12   n=11 6/1/81/12  n=59 10/4/4/83   True
259	     pre              pooled / all six / half peak  F-test          76                   0  n=26 73/1/3/23    n=4 0/92/3/4    n=8 11/4/75/9   n=38 8/6/2/84   True
260	     pre              pooled / all six / half peak  t-test          62                   0  n=21 75/0/3/22   n=3 5/79/2/14     n=5 9/1/81/9   n=33 9/4/3/84   True
261	     pre      pooled / per articulator / threshold  F-test         108                   0  n=28 68/8/5/19   n=12 8/77/8/7  n=14 13/6/65/16  n=54 11/8/6/75   T
[... 228 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('nb.py').read()
rep=[
# shared computations
('''AM = {s: B.articulator_matrix(S[s]["cvs"]) for s in B.SUBJECTS}
HV = {(s, base): S[s]["H"][base][:, S[s]["vsmc"]] for s in B.SUBJECTS for base in B.BASELINES}
RHO = {(s, base): B.partial_correlation(HV[s, base], AM[s]) for s in B.SUBJECTS for base in BASES}
GLM = {(s, base): B.glm(HV[s, base], AM[s][:, :4]) for s in B.SUBJECTS for base in BASES}
''','''CVSETS = ("all", "15+")    # every CV, or only CVs with at least 15 renditions (a question to the reader)
CVIDX = {(s, cs): np.where(S[s]["counts"] >= (15 if cs == "15+" else 0))[0] for s in B.SUBJECTS for cs in CVSETS}
CVS = {k: [S[k[0]]["cvs"][i] for i in v] for k, v in CVIDX.items()}
AM = {k: B.articulator_matrix(v) for k, v in CVS.items()}
HV = {(s, base, cs): S[s]["H"][base][CVIDX[s, cs]][:, S[s]["vsmc"]]
      for s in B.SUBJECTS for base in B.BASELINES for cs in CVSETS}
RHO = {(s, base, cs): B.partial_correlation(HV[s, base, cs], AM[s, cs]) for s in B.SUBJECTS for base in BASES for cs in CVSETS}
GLM = {(s, base, cs): B.glm(HV[s, base, cs], AM[s, cs][:, :4]) for s in B.SUBJECTS for base in BASES for cs in CVSETS}
'''),
('''def timing_rows(base, reading):
    subj_mode, art_mode, onset_mode = reading
    rows = []
    for s in B.SUBJECTS:
        pool = np.concatenate([RHO[x, base] for x in B.SUBJECTS]) if subj_mode == "pooled" else RHO[s, base]
        for a in range(6):
            vals = pool if art_mode == "all six" else pool[:, a]
            thr = vals.mean() + 2.5 * vals.std()
            for e in range(RHO[s, base].shape[0]):
                r = RHO[s, base][e, a]''','''def timing_rows(base, cs, reading):
    subj_mode, art_mode, onset_mode = reading
    rows = []
    for s in B.SUBJECTS:
        pool = np.concatenate([RHO[x, base, cs] for x in B.SUBJECTS]) if subj_mode == "pooled" else RHO[s, base, cs]
        for a in range(6):
            vals = pool if art_mode == "all six" else pool[:, a]
            thr = vals.mean() + 2.5 * vals.std()
            for e in range(RHO[s, base, cs].shape[0]):
                r = RHO[s, base, cs][e, a]'''),
('''TIMING = {(base, r): timing_rows(base, r) for base in BASES for r in TIMING_READINGS}


def articulator_windows(base, reading):
    """T_A per subject: mean onset to mean offset of the subject's electrodes for A (None if none)."""
    t = TIMING[base, reading]''','''TIMING = {(base, cs, r): timing_rows(base, cs, r) for base in BASES for cs in CVSETS for r in TIMING_READINGS}


def articulator_windows(base, cs, reading):
    """T_A per subject: mean onset to mean offset of the subject's electrodes for A (None if none)."""
    t = TIMING[base, cs, reading]'''),
('''def weights(base, reading, pmode):''','''def weights(base, cs, reading, pmode):'''),
('''    T = articulator_windows(base, reading)
    out = {}
    for s in B.SUBJECTS:
        beta, pF, pt, r2 = GLM[s, base]''','''    T = articulator_windows(base, cs, reading)
    out = {}
    for s in B.SUBJECTS:
        beta, pF, pt, r2 = GLM[s, base, cs]'''),
('''W_READINGS = [(base, r, p) for base in BASES for r in TIMING_READINGS for p in ("F-test", "t-test")]
WEIGHTS = {k: weights(*k) for k in W_READINGS}
STATE = {(s, base, z, w): B.state_space(HV[s, base], z, w)
         for s in B.SUBJECTS for base in BASES for z in ZMODES
         for w in [(-500, 750), (-375, 620)]}
SS_READINGS = [(base, z) for base in BASES for z in ZMODES]''','''W_READINGS = [(base, cs, r, p) for base in BASES for cs in CVSETS for r in TIMING_READINGS for p in ("F-test", "t-test")]
WEIGHTS = {k: weights(*k) for k in W_READINGS}
STATE = {(s, base, z, cs, w): B.state_space(HV[s, base, cs], z, w)
         for s in B.SUBJECTS for base in BASES for z in ZMODES for cs in CVSETS
         for w in [(-500, 750), (-375, 620)]}
SS_READINGS = list(itertools.product(BASES, ZMODES, CVSETS))
EP = (-500, 750)'''),
]
for a,b in rep:
    assert a in s, a[:60]
    s=s.replace(a,b)
open('nb.py','w').write(s)
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('nb.py').read()
i=s.index('# %% [markdown]\n# ## active-electrodes')
open('nb_head.py','w').write(s[:i])
print(len(s[:i].splitlines()))
EOF
```

```
377
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_tail.py",
 "content": "# %% [markdown]\n# ## active-electrodes\n#\n# > About 30 active vSMC electrodes were found per subject during syllable articulation, an\n# > electrode being active when its high-gamma z-score changed by more than 2 for any syllable.\n\n# %% tags=[\"claim:active-electrodes\"]\ndef overall(outcomes):\n    \"\"\"The outcome all method readings give, or methods_underspecified when they differ.\"\"\"\n    u = sorted(set(outcomes))\n    return u[0] if len(u) == 1 else \"differ by reading: \" + \", \".join(f\"{o} {list(outcomes).count(o)}\" for o in u)\n\n\nact = []\nfor base in B.BASELINES:\n    for cs in CVSETS:\n        for s in B.SUBJECTS:\n            H = HV[s, base, cs]\n            act.append({\"baseline\": base, \"CVs\": cs, \"subject\": s, \"vSMC\": H.shape[1],\n                        \"(a) z > 2\": int((np.nanmax(H, axis=(0, 2)) > 2).sum()),\n                        \"(b) |z| > 2\": int((np.nanmax(np.abs(H), axis=(0, 2)) > 2).sum())})\nact = pd.DataFrame(act)\nprint(act.to_string(index=False))\nam = act.groupby([\"baseline\", \"CVs\"])[[\"(a) z > 2\", \"(b) |z| > 2\"]].mean().round(2)\nam[\"within 27-33 (a or b)\"] = am.apply(lambda r: 27 <= r[\"(a) z > 2\"] <= 33 or 27 <= r[\"(b) |z| > 2\"] <= 33, axis=1)\nprint(\"\\nMean over subjects (criterion 27 to 33; rest is a variant, not a reading):\")\nprint(am.to_string())\nfor thr in (1.5, 2, 2.5, 3):\n    print(f\"threshold {thr} (all CVs): mean active per subject, pre {np.mean([(np.nanmax(HV[s, 'pre', 'all'], axis=(0, 2)) > thr).sum() for s in B.SUBJECTS]):.1f}, \"\n          f\"whole {np.mean([(np.nanmax(HV[s, 'whole', 'all'], axis=(0, 2)) > thr).sum() for s in B.SUBJECTS]):.1f}\")\nres = am.loc[list(BASES)]\nprint(\"Outcome over readings:\", overall([\"reproduced\" if all(res.xs(cs, level=1)[\"within 27-33 (a or b)\"]) else\n                                         (\"partially\" if any(res.xs(cs, level=1)[\"within 27-33 (a or b)\"]) else \"not reproduced\")\n                                         for cs in CVSETS]))\n\n# %% [markdown]\n# **Result: not reproduced.** With every CV, the mean count is 24.3 per subject with the `pre`\n# baseline (EC2 15, GP31 49, GP33 9) and 21.3 with the whole block; with only the CVs of 15 or more\n# renditions it is lower still (table). Both are below 27 under either reading of the change, as no\n# electrode passes on a decrease alone. With the dataset's rest period as baseline (a variant) the\n# mean is 34.0 with every CV. The subjects differ widely, and the count moves with the threshold.\n\n# %% [markdown]\n# ## fig1c-e-articulator-electrodes\n#\n# > In one subject, dorsal electrodes (e124, e108) were active for /b/ (lips), mid vSMC electrodes\n# > (e129, e133, e105) for /d/ (front tongue), and a more ventral electrode (e104) was most active\n# > for /g/ (back tongue).\n\n# %% tags=[\"claim:fig1c-e-articulator-electrodes\"]\nNAMED = {\"b\": [124, 108], \"d\": [129, 133, 105], \"g\": [104]}\nf1 = []\nfor s in B.SUBJECTS:\n    for numbering, offset in ((\"(a) from 1\", 1), (\"(b) from 0\", 0)):\n        idx = {k: [n - offset for n in v] for k, v in NAMED.items()}\n        all_idx = sum(idx.values(), [])\n        on_vsmc = [i in S[s][\"vsmc\"] for i in all_idx]\n        for base in BASES:\n            for measure in (\"(i) at -25 ms\", \"(ii) peak\"):\n                H = S[s][\"H\"][base]\n                resp = {}\n                for c in \"bdg\":\n                    k = S[s][\"cvs\"].index((c, \"a\"))\n                    resp[c] = H[k, :, B.ms_index(-25)] if measure.startswith(\"(i)\") else np.nanmax(H[k], axis=1)\n                prefers = {i: max(\"bdg\", key=lambda c: resp[c][i]) for i in all_idx}\n                ok = [prefers[i] == c for c, ii in idx.items() for i in ii]\n                f1.append({\"subject\": s, \"numbering\": numbering, \"baseline\": base, \"measure\": measure,\n                           \"named on vSMC\": f\"{sum(on_vsmc)} of 6\",\n                           \"labels\": \",\".join(S[s][\"location\"][i][:4] + (\"\" if S[s][\"good\"][i] else \"(bad)\") for i in all_idx),\n                           \"preferences (b b d d d g)\": \" \".join(prefers[i] for i in all_idx),\n                           \"prefer their syllable\": f\"{sum(ok)} of 6\"})\nf1 = pd.DataFrame(f1)\nprint(f1.to_string(index=False))\nprint(\"\\nSubject and numbering pairs that put all six named electrodes on vSMC:\",\n      f1[f1[\"named on vSMC\"] == \"6 of 6\"][[\"subject\", \"numbering\"]].drop_duplicates().values.tolist())\n\n# %% [markdown]\n# **Result: blocked (metadata_insufficient).** No subject, counted from 1 or from 0, has all six\n# named electrodes on vSMC (at most 4 of 6, in EC2 and GP31; some named electrodes are labelled\n# middle or superior temporal, or pars opercularis). The criterion blocks the claim in that case:\n# the dataset does not say which subject Fig. 1 shows or how the paper numbered electrodes. For\n# information, in EC2 counted from 1, five of the six named electrodes prefer their syllable under\n# both measures and both baselines.\n\n# %% [markdown]\n# ## fig1f-h-phonetic-contrasts\n#\n# > Fricatives with different tongue-tip constriction locations engaged different electrodes;\n# > front-tongue consonants of different manner engaged overlapping electrodes with different\n# > magnitudes; for /ja/, /ji/, /ju/ the activity was similar before the C-V transition, while a\n# > dorsal electrode was active during /u/ only.\n#\n# The judged part: in at least one subject, a vSMC electrode with a positive lips weight (from the\n# GLM electrodes of claim fig2a-lips-dorsal) has mean high gamma above 2 at +250 ms for /ju/ and\n# below 2 for /ja/ and /ji/. The lips weights and the GLM electrodes are computed without electrode\n# positions, which are only needed for fig2a's spatial judgement (see the summary).\n\n# %% tags=[\"claim:fig1f-h-phonetic-contrasts\"]\nt250 = B.ms_index(250)\nfh = []\nfor key in W_READINGS:\n    base, cs = key[0], key[1]\n    hits = {}\n    for s in B.SUBJECTS:\n        cvs = CVS[s, cs]\n        Hj = {v: HV[s, base, cs][cvs.index((\"y\", v)), :, t250] for v in \"aiu\"}\n        w = WEIGHTS[key][s]\n        cand = w[\"keep\"] & (w[\"W\"][:, 0] > 0)\n        hit = cand & (Hj[\"u\"] > 2) & (Hj[\"a\"] < 2) & (Hj[\"i\"] < 2)\n        hits[s] = (int(cand.sum()), int(hit.sum()), float(Hj[\"u\"][cand].max()) if cand.any() else np.nan)\n    fh.append({\"baseline\": base, \"CVs\": cs, \"timing reading\": \" / \".join(key[2]), \"p-value\": key[3],\n               **{f\"{s} lips+ / hits / max /ju/\": f\"{hits[s][0]} / {hits[s][1]} / {hits[s][2]:.2f}\" for s in B.SUBJECTS},\n               \"holds\": any(h[1] > 0 for h in hits.values())})\nfh = pd.DataFrame(fh)\nprint(fh.to_string(index=False))\nprint(\"\\nReadings where it holds:\", int(fh.holds.sum()), \"of\", len(fh))\nprint(\"Outcome over readings:\", overall([\"reproduced\" if h else \"not reproduced\" for h in fh.holds]))\nfig, axes = plt.subplots(1, 3, figsize=(12, 3), sharey=True)\nkey0 = W_READINGS[0]\nfor ax, s in zip(axes, B.SUBJECTS):\n    cvs = CVS[s, \"all\"]\n    H = HV[s, \"pre\", \"all\"]\n    w = WEIGHTS[key0][s]\n    cand = np.where(w[\"keep\"] & (w[\"W\"][:, 0] > 0))[0]\n    d = H[cvs.index((\"y\", \"u\")), cand, t250] - np.maximum(H[cvs.index((\"y\", \"a\")), cand, t250], H[cvs.index((\"y\", \"i\")), cand, t250])\n    e = cand[np.argmax(d)]\n    tr = H[[cvs.index((\"y\", v)) for v in \"aiu\"], e]\n    for v, row in zip(\"aiu\", tr):\n        ax.plot(B.EPOCH_MS, row, label=f\"/j{v}/\")\n    ax.set_title(f\"{s} electrode {S[s]['vsmc'][e]}\")\n    print(f\"{s}: plotted electrode {S[s]['vsmc'][e]} (largest /ju/ minus /ja/,/ji/ at +250 ms among lips+ GLM electrodes), z at +250 ms: \"\n          + \", \".join(f\"/j{v}/ {row[t250]:.2f}\" for v, row in zip(\"aiu\", tr)) + f\"; plotted range {tr.min():.2f} to {tr.max():.2f}; \"\n          f\"mean |difference| between the three before 0 ms {np.abs(tr[:, B.EPOCH_MS < 0] - tr[:, B.EPOCH_MS < 0].mean(0)).mean():.2f}\")\n    ax.axvline(0, color=\"k\", lw=0.5); ax.axhline(2, color=\"grey\", lw=0.5, ls=\"--\")\naxes[0].legend(); axes[0].set_ylabel(\"z (pre baseline)\")\nplt.show()\n\n# %% [markdown]\n# **Result: not reproduced.** Under all 64 readings no GLM electrode with a positive lips weight\n# reaches z = 2 for /ju/ at +250 ms in any subject; the largest /ju/ value among them is below 2\n# in every reading (table). The /ju/ responses of the plotted electrodes are larger than /ja/ and\n# /ji/ at +250 ms, but well under the paper's activity threshold. The other parts of the claim are\n# not judged (no measure in the paper).\n\n# %% [markdown]\n# ## Spatial claims (blocked)\n#\n# fig2a-lips-dorsal, fig2b-somatotopic-sequence, suppfig3b-spatial-clustering,\n# suppfig3d-cross-subject, suppfig3f-dv-sequence, suppfig5-intermediate-organization and\n# suppfig7-no-latency-difference all need each electrode's anterior-posterior distance from the\n# central sulcus and dorsal-ventral distance from the Sylvian fissure (Methods). The dandiset gives\n# neither. EC2 and GP31 have x, y, z coordinates with no unit, frame or description; GP33, one of\n# the three subjects, has none. The labels say precentral or postcentral, not how far from either\n# sulcus, and no electrode is labelled as on the guenon. These claims are blocked as\n# metadata_insufficient.\n#\n# The GLM electrode selection and weights of fig2a-lips-dorsal do not need positions and are\n# computed above. For information only (not an outcome, and not a reading of the claim), the median\n# z coordinate of the top 10% of each articulator's weights in the two subjects that have\n# coordinates, under the first reading:\n\n# %%\nkey0 = W_READINGS[0]\nprint(\"reading:\", key0)\nfor s in (\"EC2\", \"GP31\"):\n    w = WEIGHTS[key0][s]\n    z = S[s][\"z\"][S[s][\"vsmc\"]]\n    kept = np.where(w[\"keep\"])[0]\n    out = []\n    for a, name in enumerate(B.ARTICULATORS):\n        if np.isnan(w[\"W\"][kept, a]).all():\n            out.append(f\"{name} no window\"); continue\n        top = kept[np.argsort(-w[\"W\"][kept, a])[:max(1, len(kept) // 10)]]\n        out.append(f\"{name} {np.median(z[top]):.1f}\")\n    print(f\"{s}: {len(kept)} GLM electrodes; median z of top 10% weights: \" + \", \".join(out))\n\n# %% [markdown]\n# ## suppfig6-mixed-tuning\n#\n# > Single electrodes show a clear preferred articulator and also carry weights for other\n# > articulators.\n\n# %% tags=[\"claim:suppfig6-mixed-tuning\"]\ns6 = []\nfor key in W_READINGS:\n    Wk = np.concatenate([WEIGHTS[key][s][\"W\"][WEIGHTS[key][s][\"keep\"]] for s in B.SUBJECTS])\n    no_window = int(np.isnan(Wk).any(1).sum())\n    Wk = np.nan_to_num(Wk, nan=-np.inf)\n    pos = np.where(Wk > 0, Wk, 0)\n    has = pos.sum(1) > 0\n    pct = 100 * pos[has] / pos[has].sum(1, keepdims=True)\n    pref = np.argmax(Wk[has], axis=1)\n    groups, ok = {}, True\n    for a in range(4):\n        g = pct[pref == a]\n        if len(g) == 0:\n            groups[B.ARTICULATORS[a]] = \"none\"\n            continue\n        m = g.mean(0)\n        ok &= bool(np.argmax(m) == a and (np.delete(m, a) > 0).any())\n        groups[B.ARTICULATORS[a]] = f\"n={len(g)} \" + \"/\".join(f\"{x:.0f}\" for x in m)\n    s6.append({\"baseline\": key[0], \"CVs\": key[1], \"timing reading\": \" / \".join(key[2]), \"p-value\": key[3],\n               \"electrodes\": int(len(Wk)), \"with an articulator lacking T_A\": no_window,\n               \"no positive weight\": int((~has).sum()), **groups, \"holds\": ok})\ns6 = pd.DataFrame(s6)\nprint(\"Group means of positive weights as % (Lips/Tongue/Larynx/Jaw), electrodes grouped by largest W:\")\nprint(s6.to_string(index=False))\nprint(\"\\nReadings where it holds:\", int(s6.holds.sum()), \"of\", len(s6))\nprint(\"Outcome over readings:\", overall([\"reproduced\" if h else \"not reproduced\" for h in s6.holds]))\n\n# %% [markdown]\n# **Result: reproduced.** Under every reading each group's preferred articulator has the largest\n# mean share of positive weight (Lips about 63 to 77%, Tongue 53 to 96%, Larynx 61 to 84%, Jaw 72 to\n# 84%), and the other articulators keep a non-zero share (table). In readings where an articulator\n# has no window T_A in a subject (GP31's tongue, in the \"all six\" threshold readings), that\n# articulator's weight is missing for the subject's electrodes; the count is in the table.\n\n# %% [markdown]\n# ## fig3d-timing-sequence\n#\n# > Articulator correlations follow a staggered sequence consistent across subjects; lip and tongue\n# > correlations begin well before sound onset, jaw and larynx align to the C-V transition, and the\n# > high and back tongue vowel features peak near the vowel midpoint (~250 ms).\n#\n# Acoustic onset: the dandiset has no audio, so the onset of each CV is taken from the hand-marked\n# syllable start of the trial table (mean over renditions, then over CVs). This replaces the\n# prototype and thresholding of the Methods (a deviation, asked as a question).\n\n# %% tags=[\"claim:fig3d-timing-sequence\"]\nonsets = []\nfor s in B.SUBJECTS:\n    for b in blocks[s]:\n        k = b[\"kept\"]\n        for lab, st, cv in zip(b[\"condition\"][k], b[\"start\"][k], b[\"cv\"][k]):\n            p = B.parse_label(lab)\n            if p:\n                onsets.append({\"subject\": s, \"cv\": p, \"onset_ms\": 1000 * (st - cv)})\nonsets = pd.DataFrame(onsets)\nper_cv = onsets.groupby([\"subject\", \"cv\"]).onset_ms.mean()\nACOUSTIC_ONSET = per_cv.mean()\nprint(f\"Acoustic onset from the annotations: mean over {len(per_cv)} CVs {ACOUSTIC_ONSET:.1f} ms \"\n      f\"(per subject {per_cv.groupby(level=0).mean().round(1).to_dict()}; CV range {per_cv.min():.0f} to {per_cv.max():.0f} ms)\")\nf3 = []\nfor base in BASES:\n    for cs in CVSETS:\n        for reading in TIMING_READINGS:\n            t = TIMING[base, cs, reading]\n            for anova in (\"onset\", \"peak\"):\n                F, p = stats.f_oneway(*[t[t.articulator == a][anova] for a in ART6])\n                mo = t.groupby(\"articulator\").onset.mean()\n                mp = t.groupby(\"articulator\").peak.mean()\n                c1 = mo[\"Lips\"] < ACOUSTIC_ONSET and mo[\"Tongue\"] < ACOUSTIC_ONSET\n                c2 = min(mo[\"Jaw\"], mo[\"Larynx\"]) > max(mo[\"Lips\"], mo[\"Tongue\"])\n                c3 = all(abs(mp[a] - 250) <= 25 for a in B.VOWEL_ARTICULATORS)\n                n_ok = c1 + c2 + c3\n                outcome = (\"reproduced\" if p < 1e-10 and n_ok == 3 else\n                           \"partially\" if p < 1e-10 and n_ok == 2 else \"not reproduced\")\n                f3.append({\"baseline\": base, \"CVs\": cs, \"timing reading\": \" / \".join(reading), \"ANOVA on\": anova,\n                           \"n\": len(t), **{f\"n {a[:6]}\": int((t.articulator == a).sum()) for a in ART6},\n                           \"F\": round(F, 1), \"p\": p, **{f\"onset {a[:6]}\": round(mo.get(a, np.nan)) for a in ART6},\n                           \"peak Back\": round(mp[\"Back Tongue\"]), \"peak High\": round(mp[\"High Tongue\"]),\n                           \"lips,tongue < acoustic\": c1, \"jaw,larynx later\": c2, \"vowel peaks 250+-25\": c3,\n                           \"outcome\": outcome})\nf3 = pd.DataFrame(f3)\nprint(f3.to_string(index=False))\nprint(\"\\nOutcome over readings:\", overall(f3.outcome))\nprint(\"Total electrodes over articulators and subjects: from\", f3.n.min(), \"to\", f3.n.max(), \"(paper 211 +- 21)\")\nprint(\"Per subject, first reading (pre, all CVs):\", TIMING[\"pre\", \"all\", TIMING_READINGS[0]].groupby([\"subject\", \"articulator\"]).size().unstack().to_dict(\"index\"))\nfor s in B.SUBJECTS:\n    t = TIMING[\"pre\", \"all\", TIMING_READINGS[0]]\n    print(s, \"mean onsets (ms):\", t[t.subject == s].groupby(\"articulator\").onset.mean().round().to_dict())\nfig, ax = plt.subplots(figsize=(6, 3))\nt = TIMING[\"pre\", \"all\", TIMING_READINGS[0]]\nfor i, a in enumerate(ART6):\n    g = t[t.articulator == a]\n    ax.errorbar(g.onset.mean(), i, xerr=g.onset.sem(), fmt=\"<\", color=\"C0\")\n    ax.errorbar(g.peak.mean(), i, xerr=g.peak.sem(), fmt=\"o\", color=\"C1\")\n    ax.errorbar(g.offset.mean(), i, xerr=g.offset.sem(), fmt=\">\", color=\"C2\")\nax.axvline(ACOUSTIC_ONSET, color=\"grey\", ls=\"--\"); ax.axvline(0, color=\"k\", lw=0.5)\nax.set_yticks(range(6)); ax.set_yticklabels(ART6); ax.set_xlabel(\"ms (first reading, pre baseline, all CVs)\")\nplt.show()\n\n# %% [markdown]\n# **Result: not reproduced.** Under every one of the 64 readings, at most one of the three order\n# conditions holds, and none holds in most: the lips correlations begin before the annotated\n# acoustic onset (about -110 ms) but the tongue correlations begin after the C-V transition (mean\n# onsets -26 to +213 ms), the jaw begins as early as the lips, not later, and the high-tongue peak\n# lies beyond 275 ms in most readings. The ANOVA across articulators is significant (F 9.9 to 29.5),\n# with p below 1e-10 in some readings and not in others. Electrode counts are 173 to 226 (paper 211).\n\n# %% [markdown]\n# ## pca-nine-components\n#\n# > The cortical state-space has nine spatial PCs in every subject, the eigenvalues falling fast up\n# > to the ninth and slowly after, together explaining about 60% of the variance.\n\n# %% tags=[\"claim:pca-nine-components\"]\npc = []\nfor base in BASES:\n    for z in ZMODES:\n        for cs in CVSETS:\n            for w in [(-500, 750), (-375, 620)]:\n                fr = {s: STATE[s, base, z, cs, w][1] for s in B.SUBJECTS}\n                pc.append({\"baseline\": base, \"z-scoring\": z, \"CVs\": cs, \"window\": f\"{w[0]} to {w[1]}\",\n                           **{s: round(fr[s][:9].sum(), 3) for s in B.SUBJECTS},\n                           \"mean\": round(np.mean([fr[s][:9].sum() for s in B.SUBJECTS]), 3)})\npc = pd.DataFrame(pc)\npc[\"within 0.54-0.66\"] = pc[\"mean\"].between(0.54, 0.66)\nprint(pc.to_string(index=False))\nprint(\"\\nOutcome over readings:\", overall([\"reproduced\" if x else \"not reproduced\" for x in pc[\"within 0.54-0.66\"]]))\nprint(\"Rest-baseline variant (row, all CVs, epoch):\", {s: round(float(B.state_space(HV[s, \"rest\", \"all\"], \"row\")[1][:9].sum()), 3) for s in B.SUBJECTS})\nfig, axes = plt.subplots(1, 2, figsize=(10, 3))\nfor ax, z in zip(axes, ZMODES):\n    for s in B.SUBJECTS:\n        ax.plot(np.arange(1, 21), 100 * STATE[s, \"pre\", z, \"all\", EP][1][:20], \"o-\", ms=3, label=s)\n    ax.axvline(9, color=\"grey\", ls=\"--\"); ax.set_title(f\"pre baseline, {z} z-scoring, all CVs\"); ax.set_xlabel(\"PC\"); ax.set_ylabel(\"% variance\")\naxes[0].legend(); plt.show()\nprint(\"% variance of PCs 1 to 12, pre baseline, all CVs, epoch (all values plotted are within 0 to 40%):\")\nfor z in ZMODES:\n    for s in B.SUBJECTS:\n        print(z, s, np.round(100 * STATE[s, \"pre\", z, \"all\", EP][1][:12], 1))\n\n# %% [markdown]\n# **Result: blocked (methods_underspecified).** With each electrode's concatenated series z-scored\n# (`row`), the first nine PCs explain a mean of 0.62 to 0.65 over subjects under every baseline, CV\n# set and window, within 0.54 to 0.66. With each electrode z-scored across syllables at each time\n# (`time`), the mean is 0.53 to 0.55, below the tolerance in most readings. The two readings of the\n# z-scoring give different outcomes. The spectra show no sharp change at the ninth eigenvalue in\n# any subject (printed values); that part is not judged.\n\n# %% [markdown]\n# ## fig4a-consonant-clusters\n#\n# > At the consonant time (-25 ms) k-means clustering of the cortical state-space groups syllables\n# > by major oral articulator, and three clusters are more parsimonious than two or four (mean\n# > silhouette 0.47 against 0.45 and 0.43).\n\n# %% tags=[\"claim:fig4a-consonant-clusters\"]\ntc, tv = B.ms_index(-25), B.ms_index(250)\nsil = []\nfor base, z, cs in SS_READINGS:\n    for s in B.SUBJECTS:\n        K = STATE[s, base, z, cs, EP][2][:, :, tc]\n        row = {\"baseline\": base, \"z-scoring\": z, \"CVs\": cs, \"subject\": s}\n        for k in (2, 3, 4):\n            row[f\"k={k}\"] = silhouette_score(K, B.kmeans(K, k, seed=40 + k))\n        sil.append(row)\nsil = pd.DataFrame(sil)\nprint(sil.round(3).to_string(index=False))\nmeans = sil.groupby([\"baseline\", \"z-scoring\", \"CVs\"])[[\"k=2\", \"k=3\", \"k=4\"]].mean()\nmeans[\"k=3 highest\"] = means.idxmax(axis=1) == \"k=3\"\nmeans[\"all within 10%\"] = (abs(means[\"k=2\"] - 0.45) <= 0.045) & (abs(means[\"k=3\"] - 0.47) <= 0.047) & (abs(means[\"k=4\"] - 0.43) <= 0.043)\nprint(\"\\nMean over subjects (paper 0.45, 0.47, 0.43):\")\nprint(means.round(3).to_string())\nprint(\"Outcome over readings:\", overall([\"reproduced\" if h and w else \"partially\" if h else \"not reproduced\"\n                                         for h, w in zip(means[\"k=3 highest\"], means[\"all within 10%\"])]))\n\n# %% [markdown]\n# **Result: not reproduced.** Three clusters do not have the highest mean silhouette under any\n# reading, and the silhouettes are lower than the paper's (k = 3: 0.18 to 0.28 against 0.47). With\n# every CV, GP31's k = 2 silhouette is near 0.8 because its /thi/, with two renditions, stands\n# apart from all other CVs; with only CVs of 15 or more renditions this goes away, and k = 3 is\n# still not the most parsimonious.\n\n# %% [markdown]\n# ## suppfig11-co-clustering\n#\n# > Clusters of the cortical state-space match the major articulators at the consonant time\n# > (median co-clustering 0.50 against 0.32 by chance) and the vowels at the vowel time (0.65\n# > against 0.37), across subjects.\n\n# %% tags=[\"claim:suppfig11-co-clustering\"]\nrng = np.random.default_rng(11)\ncc = []\nfor base, z, cs in SS_READINGS:\n    obs = {\"cons a\": [], \"cons b\": [], \"vowel\": []}\n    null = {\"cons a\": [], \"cons b\": [], \"vowel\": []}\n    for s in B.SUBJECTS:\n        K = STATE[s, base, z, cs, EP][2]\n        nc_c = B.kmeans(K[:, :, tc], 3, seed=21)\n        nc_v = B.kmeans(K[:, :, tv], 3, seed=22)\n        for name, nc, labs in ((\"cons a\", nc_c, [B.MAJOR[\"a\"].get(c) for c, v in CVS[s, cs]]),\n                               (\"cons b\", nc_c, [B.MAJOR[\"b\"].get(c) for c, v in CVS[s, cs]]),\n                               (\"vowel\", nc_v, [v for c, v in CVS[s, cs]])):\n            keep = np.array([l is not None for l in labs])\n            ac = np.array([l for l in labs if l is not None])\n            ncs = nc[keep]\n            obs[name].append(B.co_clustering(ncs, ac))\n            null[name].append(np.mean([B.co_clustering(ncs, rng.permutation(ac)) for _ in range(1000)], axis=0))\n    row = {\"baseline\": base, \"z-scoring\": z, \"CVs\": cs}\n    ok_tests, ok_med = True, True\n    for name in obs:\n        o, n = np.concatenate(obs[name]), np.concatenate(null[name])\n        p = stats.wilcoxon(o, n).pvalue\n        row[f\"{name}: n, obs, null, p\"] = f\"{len(o)}, {np.median(o):.3f}, {np.median(n):.3f}, {p:.1e}\"\n        ok_tests &= bool(p < 1e-10 and np.median(o - n) > 0)\n    for cons in (\"cons a\", \"cons b\"):\n        mo = {k: np.median(np.concatenate(obs[k])) for k in (cons, \"vowel\")}\n        mn = {k: np.median(np.concatenate(null[k])) for k in (cons, \"vowel\")}\n        within = abs(mo[cons] - 0.50) <= 0.05 and abs(mn[cons] - 0.32) <= 0.032 and abs(mo[\"vowel\"] - 0.65) <= 0.065 and abs(mn[\"vowel\"] - 0.37) <= 0.037\n        row[f\"outcome ({cons[-1]})\"] = \"reproduced\" if ok_tests and within else (\"partially\" if ok_tests else \"not reproduced\")\n    cc.append(row)\ncc = pd.DataFrame(cc)\nprint(cc.to_string(index=False))\nprint(\"Expected: consonants 0.50 +- 0.05 against 0.32 +- 0.032; vowels 0.65 +- 0.065 against 0.37 +- 0.037; p < 1e-10\")\nprint(\"Outcome over readings:\", overall(list(cc[\"outcome (a)\"]) + list(cc[\"outcome (b)\"])))\n\n# %% [markdown]\n# **Result: see the summary.**\n\n# %% [markdown]\n# ## fig4c-d-hierarchy\n#\n# > Hierarchical clustering of the state-space puts the major oral articulator at the top tier for\n# > consonants; for vowels the first split is lip rounding (/u/ against /a/ and /i/).\n\n# %% tags=[\"claim:fig4c-d-hierarchy\"]\nhc = []\nfor base, z, cs in SS_READINGS:\n    for s in B.SUBJECTS:\n        K = STATE[s, base, z, cs, EP][2]\n        cons_cut = fcluster(linkage(K[:, :, tc], \"ward\"), 3, \"maxclust\")\n        vow_cut = fcluster(linkage(K[:, :, tv], \"ward\"), 2, \"maxclust\")\n        row = {\"baseline\": base, \"z-scoring\": z, \"CVs\": cs, \"subject\": s}\n        for lr in (\"a\", \"b\"):\n            labs = np.array([B.MAJOR[lr].get(c, \"\") for c, v in CVS[s, cs]])\n            lab = labs != \"\"\n            maj = {k: pd.Series(labs[lab & (cons_cut == k)]).mode().tolist() for k in (1, 2, 3)}\n            distinct = all(len(v) == 1 for v in maj.values()) and len({v[0] for v in maj.values()}) == 3\n            home = {a: pd.Series(cons_cut[lab & (labs == a)]).mode()[0] for a in (\"labial\", \"coronal\", \"dorsal\")}\n            purity = np.mean([cons_cut[i] == home[labs[i]] for i in np.where(lab)[0]])\n            row[f\"cons ({lr}) majorities\"] = \"/\".join(v[0] if len(v) == 1 else \"tie\" for v in maj.values())\n            row[f\"cons ({lr}) in home\"] = round(purity, 2)\n            row[f\"cons ({lr}) holds\"] = bool(distinct and purity >= 2 / 3)\n            row[f\"cons ({lr}) co-clust\"] = round(np.median(B.co_clustering(cons_cut[lab], labs[lab])), 2)\n        vow = np.array([v for c, v in CVS[s, cs]])\n        ok = any((vow_cut[vow == \"u\"] == ku).mean() > 0.5 and (vow_cut[vow != \"u\"] == 3 - ku).mean() > 0.5 for ku in (1, 2))\n        row[\"a/i/u in cluster 1\"] = \"/\".join(f\"{(vow_cut[vow == v] == 1).mean():.2f}\" for v in \"aiu\")\n        row[\"vowel holds\"] = bool(ok)\n        hc.append(row)\nhc = pd.DataFrame(hc)\nprint(hc.to_string(index=False))\noc = []\nfor (base, z, cs), g in hc.groupby([\"baseline\", \"z-scoring\", \"CVs\"]):\n    for lr in (\"a\", \"b\"):\n        both = g[f\"cons ({lr}) holds\"] & g[\"vowel holds\"]\n        oc.append({\"baseline\": base, \"z-scoring\": z, \"CVs\": cs, \"labels\": lr, \"subjects with both\": int(both.sum()),\n                   \"outcome\": \"reproduced\" if both.all() else (\"partially\" if both.any() else \"not reproduced\")})\noc = pd.DataFrame(oc)\nprint(oc.to_string(index=False))\nprint(\"Outcome over readings:\", overall(oc.outcome))\n\n# %% [markdown]\n# **Result: see the summary.**\n\n# %% [markdown]\n# ## fig4ef-feature-correlations\n#\n# > Over early times (-375 to 120 ms) constriction location correlates with the state-space\n# > structure more than constriction degree, which correlates more than the upcoming vowel; over\n# > later times (125 to 620 ms) vowel configuration correlates most.\n\n# %% tags=[\"claim:fig4ef-feature-correlations\"]\nFEATS = (\"location\", \"degree\", \"vowel\")\n\n\ndef feature_r(base, z, cs, metric=\"euclidean\"):\n    \"\"\"R(t) per subject and feature set (Methods Eq. 7): {(subject, set): R over epoch times}.\"\"\"\n    out = {}\n    for s in B.SUBJECTS:\n        K = STATE[s, base, z, cs, EP][2]\n        dK = np.array([pdist(K[:, :, t]) for t in range(K.shape[2])])\n        for f in FEATS:\n            dP = pdist(B.feature_matrix(CVS[s, cs], f), metric)\n            out[s, f] = np.array([np.corrcoef(d, dP)[0, 1] for d in dK])\n    return out\n\n\nearly = (B.EPOCH_MS >= -375) & (B.EPOCH_MS < 120)\nlate = (B.EPOCH_MS >= 125) & (B.EPOCH_MS < 620)\nRT = {k: feature_r(*k) for k in SS_READINGS}\nfe = []\nfor (base, z, cs), R in RT.items():\n    for metric in (\"euclidean\", \"hamming\"):\n        Rm = R if metric == \"euclidean\" else feature_r(base, z, cs, \"hamming\")\n        e = {f: np.concatenate([Rm[s, f][early] for s in B.SUBJECTS]) for f in FEATS}\n        l = {f: np.concatenate([Rm[s, f][late] for s in B.SUBJECTS]) for f in FEATS}\n        tests = {\"early loc>deg\": (e[\"location\"], e[\"degree\"]), \"early deg>vow\": (e[\"degree\"], e[\"vowel\"]),\n                 \"late vow>loc\": (l[\"vowel\"], l[\"location\"]), \"late vow>deg\": (l[\"vowel\"], l[\"degree\"])}\n        row = {\"baseline\": base, \"z-scoring\": z, \"CVs\": cs, \"distance\": metric, \"n\": len(e[\"location\"])}\n        n_ok = 0\n        for name, (a, b) in tests.items():\n            p = stats.wilcoxon(a, b).pvalue\n            ok = bool(np.median(a - b) > 0 and p < 1e-10)\n            row[name] = f\"{np.median(a - b):+.3f} p={p:.0e} {'Y' if ok else 'n'}\"\n            n_ok += ok\n        row[\"med early L/D/V\"] = \"/\".join(f\"{np.median(e[f]):.2f}\" for f in FEATS)\n        row[\"med late L/D/V\"] = \"/\".join(f\"{np.median(l[f]):.2f}\" for f in FEATS)\n        row[\"outcome\"] = \"reproduced\" if n_ok == 4 else (\"partially\" if n_ok else \"not reproduced\")\n        fe.append(row)\nfe = pd.DataFrame(fe)\nprint(fe.to_string(index=False))\nprint(\"Outcome over readings (Euclidean; Hamming is a variant):\", overall(fe[fe.distance == \"euclidean\"].outcome))\n\n# %% [markdown]\n# **Result: partially reproduced.** In the early window, constriction location correlates with the\n# state-space distances more than constriction degree, and degree more than the vowel, with\n# p < 1e-10 under every reading (n = 297, 99 times x 3 subjects). In the late window, vowel\n# configuration does not correlate most: location correlates more than the vowel features in every\n# reading, and vowel exceeds degree with p < 1e-10 in a few readings only (table). With Hamming\n# distances the result is the same.\n\n# %% [markdown]\n# ## fig5c-separability-timing\n#\n# > Cluster separability, averaged over subjects, rises from about -300 ms and peaks about 200 ms\n# > before the C-V transition for consonants, and rises from about 50 ms and peaks at +250 ms for\n# > vowels.\n\n# %% tags=[\"claim:fig5c-separability-timing\"]\nrng5 = np.random.default_rng(5)\nN_BOOT = 1000\n\n\ndef cluster_labels(s, cs, K, which, kind):\n    \"\"\"Labels per CV (per time and CV for k-means); -1 for CVs without a label.\"\"\"\n    cvs = CVS[s, cs]\n    if kind == \"kmeans\":\n        return np.array([B.kmeans(K[:, :, t], 3, seed=1000 + t, n_init=10) for t in range(K.shape[2])])\n    if which == \"vowel\":\n        return np.array([\"aiu\".index(v) for c, v in cvs])\n    lr = kind[-1]\n    names = {\"labial\": 0, \"coronal\": 1, \"dorsal\": 2}\n    out = []\n    for c, v in cvs:\n        m = B.MAJOR[lr].get(c)\n        out.append(3 if kind.startswith(\"four\") and c in B.SIBILANTS else (names[m] if m else -1))\n    return np.array(out)\n\n\nSEP_KINDS = {\"consonant\": [\"groups a\", \"groups b\", \"four a\", \"four b\", \"kmeans\"], \"vowel\": [\"groups\", \"kmeans\"]}\n\n\ndef separability_curves(base, z, cs):\n    out = {}\n    kmeans_cache = {}\n    for which, kinds in SEP_KINDS.items():\n        for kind in kinds:\n            curves, boots = [], []\n            for s in B.SUBJECTS:\n                K = STATE[s, base, z, cs, EP][2]\n                if kind == \"kmeans\":\n                    if s not in kmeans_cache:\n                        kmeans_cache[s] = cluster_labels(s, cs, K, which, kind)\n                    lab = kmeans_cache[s]\n                else:\n                    lab = cluster_labels(s, cs, K, which, kind)\n                keep = (lab >= 0) if lab.ndim == 1 else np.ones(K.shape[0], bool)\n                Ks = K[keep]\n                labk = lab[keep] if lab.ndim == 1 else lab[:, keep]\n                D = np.array([squareform(pdist(Ks[:, :, t])) for t in range(Ks.shape[2])])\n                curves.append(B.separability(D, labk)[0])\n                wts = rng5.multinomial(len(Ks), np.ones(len(Ks)) / len(Ks), size=N_BOOT)\n                boots.append(B.separability(D, labk, wts))\n            out[which, kind] = (np.mean(curves, 0), np.mean(boots, 0).std(0), curves)\n    return out\n\n\nSEP = {k: separability_curves(*k) for k in SS_READINGS}\n\n\ndef onset_peak(curve, se):\n    \"\"\"Peak time, onset (a) first time above the level at -500 ms by 2 bootstrap s.e., onset (b)\n    first time of the run up to the peak above half the peak value.\"\"\"\n    p = int(np.argmax(curve))\n    above = np.where(curve[:p + 1] > curve[0] + 2 * se[:p + 1])[0]\n    on_a = B.EPOCH_MS[above[0]] if len(above) else np.nan\n    below = np.where(curve[:p + 1] < curve[p] / 2)[0]\n    on_b = B.EPOCH_MS[below[-1] + 1] if len(below) else np.nan\n    return B.EPOCH_MS[p], on_a, on_b\n\n\nsp = []\nfor (base, z, cs), d in SEP.items():\n    for ck in SEP_KINDS[\"consonant\"]:\n        vk = \"kmeans\" if ck == \"kmeans\" else \"groups\"\n        cpk, con_a, con_b = onset_peak(d[\"consonant\", ck][0], d[\"consonant\", ck][1])\n        vpk, von_a, von_b = onset_peak(d[\"vowel\", vk][0], d[\"vowel\", vk][1])\n        peaks_ok = abs(cpk + 200) <= 20 and abs(vpk - 250) <= 25\n        ons_ok = {\"a\": abs(con_a + 300) <= 30 and abs(von_a - 50) <= 10, \"b\": abs(con_b + 300) <= 30 and abs(von_b - 50) <= 10}\n        sp.append({\"baseline\": base, \"z-scoring\": z, \"CVs\": cs, \"clusters\": f\"{ck} | {vk}\",\n                   \"cons peak\": cpk, \"cons onset a\": con_a, \"cons onset b\": con_b,\n                   \"vowel peak\": vpk, \"vowel onset a\": von_a, \"vowel onset b\": von_b,\n                   \"peaks ok\": peaks_ok, \"onset ok a\": ons_ok[\"a\"], \"onset ok b\": ons_ok[\"b\"],\n                   \"outcome\": \"reproduced\" if peaks_ok and any(ons_ok.values()) else (\"partially\" if peaks_ok else \"not reproduced\")})\nsp = pd.DataFrame(sp)\nprint(sp.to_string(index=False))\nprint(\"Expected: consonant peak -200 +- 20, onset -300 +- 30; vowel peak 250 +- 25, onset 50 +- 10 ms\")\nprint(\"Outcome over readings:\", overall(sp.outcome))\nfig, axes = plt.subplots(1, 2, figsize=(11, 3))\nfor ax, key in zip(axes, [(\"pre\", \"row\", \"all\"), (\"pre\", \"time\", \"all\")]):\n    for (which, kind), (c, se, _) in SEP[key].items():\n        if kind != \"kmeans\":\n            ax.plot(B.EPOCH_MS, c, label=f\"{which} {kind}\")\n    ax.axvline(0, color=\"k\", lw=0.5); ax.set_title(\", \".join(key)); ax.set_xlabel(\"ms\")\naxes[0].legend(fontsize=7); axes[0].set_ylabel(\"separability\")\nplt.show()\nfor key, d in SEP.items():\n    print(key, \"curve ranges:\", {f\"{w} {k}\": (round(float(c.min()), 2), round(float(c.max()), 2)) for (w, k), (c, se, _) in d.items()})\n\n# %% [markdown]\n# **Result: not reproduced.** Under no reading are both peaks near the paper's. With the phonetic\n# groups the consonant separability peaks between -145 and +10 ms (paper -200 ms) and the vowel\n# separability at 200 to 230 ms; with k-means at each time a single curve peaks near +300 ms for\n# both. The consonant onsets (-185 to -280 ms) are close to the paper's -300 ms under some readings,\n# and the vowel onsets (75 to 110 ms) later than its 50 ms.\n\n# %% [markdown]\n# ## fig5d-separability-coupling\n#\n# > Cluster separability and the correlation of the state-space with phonetic features are tightly\n# > linked over time for consonants and vowels in each subject (R2 0.42 to 0.98, all P < 1e-10).\n\n# %% tags=[\"claim:fig5d-separability-coupling\"]\nc5 = []\nfor (base, z, cs), d in SEP.items():\n    R = RT[base, z, cs]\n    for ck in SEP_KINDS[\"consonant\"]:\n        vk = \"kmeans\" if ck == \"kmeans\" else \"groups\"\n        for rmode in (\"(a) matching set\", \"(b) mean of three\"):\n            vals = []\n            for i, s in enumerate(B.SUBJECTS):\n                for which, kind, fset in ((\"consonant\", ck, \"location\"), (\"vowel\", vk, \"vowel\")):\n                    r = R[s, fset] if rmode.startswith(\"(a)\") else np.mean([R[s, f] for f in FEATS], 0)\n                    res = stats.pearsonr(d[which, kind][2][i], r)\n                    vals.append((res.statistic ** 2, res.pvalue, res.statistic))\n            r2 = np.array([v[0] for v in vals]); ps = np.array([v[1] for v in vals]); rs = np.array([v[2] for v in vals])\n            ok = bool((r2 >= 0.378).all() and (ps < 1e-10).all() and (rs > 0).all())\n            part = bool((rs > 0).all() and (ps < 1e-10).all())\n            c5.append({\"baseline\": base, \"z-scoring\": z, \"CVs\": cs, \"clusters\": f\"{ck} | {vk}\", \"R\": rmode,\n                       \"R2 (EC2 c,v GP31 c,v GP33 c,v)\": \" \".join(f\"{x:.2f}\" for x in r2),\n                       \"max p\": ps.max(), \"min r\": round(rs.min(), 2),\n                       \"outcome\": \"reproduced\" if ok else (\"partially\" if part else \"not reproduced\")})\nc5 = pd.DataFrame(c5)\nprint(c5.to_string(index=False))\nprint(\"\\nOutcome over readings:\", overall(c5.outcome))\nprint(\"Outcomes by reading of the clusters and of R:\")\nprint(c5.groupby([\"clusters\", \"R\"]).outcome.value_counts().unstack(fill_value=0).to_string())\n\n# %% [markdown]\n# **Result: blocked (methods_underspecified).** With the phonetic groups as clusters and the\n# matching feature set for R (constriction location for consonants, vowel features for vowels),\n# all six R2 values lie within 0.38 to 1 with p < 1e-10 in every baseline, z-scoring and CV\n# reading. With the mean of the three feature sets, or with k-means clusters at each time, the\n# coupling fails (R2 near 0 in some subjects, negative r). The readings of the claim give different\n# outcomes.\n\n# %% [markdown]\n# ## suppfig13-consonant-vowel-distance\n#\n# > Consonant and vowel representations occupy distinct regions of the state-space;\n# > consonant-vowel distances are larger than consonant-consonant and vowel-vowel distances, and\n# > consonant-consonant distances are larger than vowel-vowel ones.\n\n# %% tags=[\"claim:suppfig13-consonant-vowel-distance\"]\ncvd = []\nfor base, z, cs in SS_READINGS:\n    for reading in (\"(a) mean of cross pairings\", \"(b) i at -25, j at +250\"):\n        CC, VV, CVd = [], [], []\n        for s in B.SUBJECTS:\n            K = STATE[s, base, z, cs, EP][2]\n            Kc, Kv = K[:, :, tc], K[:, :, tv]\n            i, j = np.triu_indices(len(Kc), 1)\n            CC.append(np.linalg.norm(Kc[i] - Kc[j], axis=1))\n            VV.append(np.linalg.norm(Kv[i] - Kv[j], axis=1))\n            d1 = np.linalg.norm(Kc[i] - Kv[j], axis=1)\n            d2 = np.linalg.norm(Kc[j] - Kv[i], axis=1)\n            CVd.append((d1 + d2) / 2 if reading.startswith(\"(a)\") else d1)\n        CC, VV, CVd = map(np.concatenate, (CC, VV, CVd))\n        row = {\"baseline\": base, \"z-scoring\": z, \"CVs\": cs, \"CV distance\": reading, \"pairs\": len(CC),\n               \"median CC\": round(np.median(CC), 2), \"median VV\": round(np.median(VV), 2), \"median CV\": round(np.median(CVd), 2)}\n        ok = True\n        for name, (a, b) in {\"CV>CC\": (CVd, CC), \"CV>VV\": (CVd, VV), \"CC>VV\": (CC, VV)}.items():\n            p = min(1.0, 3 * stats.wilcoxon(a, b).pvalue)\n            row[name] = f\"{np.median(a - b):+.2f} p={p:.0e}\"\n            ok &= bool(np.median(a - b) > 0 and p < 1e-10)\n        row[\"orderings hold\"] = ok\n        row[\"outcome\"] = (\"reproduced\" if ok and len(CC) == 4623 else \"partially\" if ok else \"not reproduced\")\n        cvd.append(row)\ncvd = pd.DataFrame(cvd)\nprint(cvd.to_string(index=False))\nprint(\"Pairs within subjects (all CVs):\", {s: len(CVS[s, 'all']) * (len(CVS[s, 'all']) - 1) // 2 for s in B.SUBJECTS},\n      \"| 15+ CVs:\", {s: len(CVS[s, '15+']) * (len(CVS[s, '15+']) - 1) // 2 for s in B.SUBJECTS}, \"(paper n = 4623)\")\nprint(\"Outcome over readings:\", overall(cvd.outcome))\n\n# %% [markdown]\n# **Result: blocked (methods_underspecified).** With `row` z-scoring, consonant-vowel distances\n# exceed consonant-consonant ones, which exceed vowel-vowel ones, with corrected p < 1e-10 under\n# every other reading; with `time` z-scoring the consonant-vowel distances are shorter than the\n# consonant-consonant ones. The number of pairs is 4677 with every CV and 4560 with CVs of 15 or\n# more renditions, never the paper's 4623, so the `row` readings would give a partial outcome and\n# the `time` readings not reproduced.\n\n# %% [markdown]\n# ## suppfig9-pc-articulator-weights\n#\n# > The first three PCs are weighted toward tongue over lips, and toward lips over jaw and larynx,\n# > while jaw and larynx do not differ.\n#\n# Note on the method: by Methods Eq. 6, log10|PCw_ij| = log10|M_ij| + log10|W_jA|, so for a given\n# electrode the PC term is the same for every articulator and cancels in the paired comparisons;\n# the tests give the same result in every PC.\n\n# %% tags=[\"claim:suppfig9-pc-articulator-weights\"]\npairs6 = list(itertools.combinations(range(4), 2))\ns9 = []\nfor (base, cs, reading, pmode) in W_READINGS:\n    for z in ZMODES:\n        for eset in (\"all vSMC\", \"GLM electrodes\"):\n            if eset == \"all vSMC\" and pmode == \"t-test\":\n                continue    # the p-value reading only changes which electrodes are kept\n            vals = []\n            for s in B.SUBJECTS:\n                w = WEIGHTS[base, cs, reading, pmode][s]\n                M = STATE[s, base, z, cs, EP][0]\n                sel = w[\"keep\"] if eset == \"GLM electrodes\" else np.ones(len(w[\"keep\"]), bool)\n                vals.append(np.log10(np.abs(M[sel, :3, None] * w[\"W\"][sel, None, :])))\n            V = np.concatenate(vals)            # (electrode, PC, articulator)\n            V = V[np.isfinite(V).all(axis=(1, 2))]\n            per_pc, meds = [], []\n            for pci in range(3):\n                p = {(a, b): (np.median(V[:, pci, a] - V[:, pci, b]), min(1.0, 6 * stats.wilcoxon(V[:, pci, a], V[:, pci, b]).pvalue))\n                     for a, b in pairs6}\n\n                def greater(a, b, alpha):\n                    m, pv = p[(a, b)] if (a, b) in p else (-p[(b, a)][0], p[(b, a)][1])\n                    return bool(m > 0 and pv < alpha)\n                L, T, X, J = 0, 1, 2, 3\n                ra = greater(L, J, 0.001) and greater(L, X, 0.001)\n                rb = ra and greater(T, J, 0.001) and greater(T, X, 0.001)\n                per_pc.append(greater(T, L, 0.05) and (ra or rb) and p[(X, J)][1] > 0.05)\n                meds.append(\"/\".join(f\"{np.median(V[:, pci, a]):.2f}\" for a in range(4)))\n            n_ok = sum(per_pc)\n            s9.append({\"baseline\": base, \"CVs\": cs, \"timing reading\": \" / \".join(reading), \"p-value\": pmode, \"z-scoring\": z,\n                       \"electrodes\": eset, \"n\": len(V), \"PC1 medians L/T/X/J\": meds[0], \"PCs holding\": \"\".join(\"Y\" if x else \"n\" for x in per_pc),\n                       \"outcome\": \"reproduced\" if n_ok == 3 else (\"partially\" if n_ok else \"not reproduced\")})\ns9 = pd.DataFrame(s9)\nprint(s9.to_string(index=False))\nprint(\"\\nOutcome over readings:\", overall(s9.outcome))\nbase, cs, reading, pmode, z = \"pre\", \"all\", TIMING_READINGS[2], \"F-test\", \"row\"\nV = np.concatenate([np.log10(np.abs(STATE[s, base, z, cs, EP][0][:, :3, None] * WEIGHTS[base, cs, reading, pmode][s][\"W\"][:, None, :])) for s in B.SUBJECTS])\nV = V[np.isfinite(V).all(axis=(1, 2))]\nfor pci in range(3):\n    ps = {f\"{B.ARTICULATORS[a][:2]}-{B.ARTICULATORS[b][:2]}\": f\"{np.median(V[:, pci, a] - V[:, pci, b]):+.2f} p={min(1, 6 * stats.wilcoxon(V[:, pci, a], V[:, pci, b]).pvalue):.0e}\" for a, b in pairs6}\n    print(f\"PC{pci + 1} ({base}, {cs}, {reading}, all vSMC, n={len(V)}): median paired differences and corrected p {ps}\")\n\n# %% [markdown]\n# **Result: not reproduced.** Under every reading, tongue weights are not larger than lips weights;\n# the lips weights are the larger (median paired difference of log10 weights for tongue minus lips\n# negative, printed above), so the first condition fails in all three PCs. Jaw and larynx also\n# differ in most readings.\n\n# %% [markdown]\n# ## Summary\n\n# %%\nprint(f\"notebook ran in {(time.time() - started) / 60:.1f} min\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb_tail.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('nb_head.py').read()
a='''print("Every trial is marked speak=True:", bool((files.trials == files.speak).all()))'''
b='''print("Trials not marked speak=True, per subject:", (files.trials - files.speak).groupby(files.subject).sum().to_dict())'''
assert a in s; s=s.replace(a,b)
open('nb.py','w').write(s+open('nb_tail.py').read())
EOF
. work/bin/activate && python devrun.py > dev.out 2>&1; grep -n "=====\|Outcome over\|Error\|Traceback" dev.out | head -80; tail -3 dev.out
```

```
1:===== cell 0 
3:===== cell 1 
5:===== cell 2 
7:===== cell 3 tags=["sanity"]
56:===== cell 4 tags=["sanity"]
60:===== cell 5 tags=["sanity"]
71:===== cell 6 tags=["sanity"]
89:===== cell 7 tags=["sanity"]
129:===== cell 8 tags=["sanity"]
137:===== cell 9 
140:===== cell 10 tags=["claim:data-composition"]
150:===== cell 11 tags=["claim:active-electrodes"]
184:Outcome over readings: not reproduced
186:===== cell 12 tags=["claim:fig1c-e-articulator-electrodes"]
215:===== cell 13 tags=["claim:fig1f-h-phonetic-contrasts"]
283:Outcome over readings: not reproduced
288:===== cell 14 
293:===== cell 15 tags=["claim:suppfig6-mixed-tuning"]
362:Outcome over readings: reproduced
364:===== cell 16 tags=["claim:fig3d-timing-sequence"]
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -n 150,186p dev.out; sed -n 439,458p dev.out; sed -n 488,506p dev.out; sed -n 508,600p dev.out
```

```
===== cell 11 tags=["claim:active-electrodes"]
baseline CVs subject  vSMC  (a) z > 2  (b) |z| > 2
     pre all     EC2    86         15           15
     pre all    GP31    83         49           49
     pre all    GP33    99          9            9
     pre 15+     EC2    86         14           14
     pre 15+    GP31    83          9            9
     pre 15+    GP33    99          9            9
   whole all     EC2    86         15           15
   whole all    GP31    83         43           43
   whole all    GP33    99          6            6
   whole 15+     EC2    86         15           15
   whole 15+    GP31    83          0            0
   whole 15+    GP33    99          6            6
    rest all     EC2    86         30           30
    rest all    GP31    83         51           51
    rest all    GP33    99         21           21
    rest 15+     EC2    86         29           29
    rest 15+    GP31    83         31           31
    rest 15+    GP33    99         21           21
[... 150 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -n 600,640p dev.out; sed -n 700,760p dev.out; grep -n "max /ju/" -A3 dev.out | head -5; awk 'NR>=215 && NR<=283' dev.out | awk '{print $NF, $(NF-1)}' | sort | uniq -c | head; sed -n 364,372p dev.out; sed -n 425,438p dev.out
```

```
pre      time all   four a | groups        -95        -275.0        -270.0         225           75.0          100.0     False       False       False not reproduced
     pre      time all   four b | groups       -145        -285.0        -275.0         225           75.0          100.0     False       False       False not reproduced
     pre      time all   kmeans | kmeans        310           NaN         240.0         310            NaN          240.0     False       False       False not reproduced
     pre      time 15+ groups a | groups          5        -255.0        -240.0         235           60.0          100.0     False       False       False not reproduced
     pre      time 15+ groups b | groups        -65        -280.0        -265.0         235           60.0          100.0     False        True       False not reproduced
     pre      time 15+   four a | groups        -90        -295.0        -280.0         235           60.0          100.0     False        True       False not reproduced
     pre      time 15+   four b | groups        -95        -305.0        -285.0         235           60.0          100.0     False        True       False not reproduced
     pre      time 15+   kmeans | kmeans        330         325.0           NaN         330            NaN            NaN     False       False       False not reproduced
   whole       row all groups a | groups          5        -235.0        -180.0         205          100.0           95.0     False       False       False not reproduced
   whole       row all groups b | groups          5        -260.0        -195.0         205          100.0           95.0     False       False       False not reproduced
   whole       row all   four a | groups        -70        -260.0        -210.0         205          100.0           95.0     False       False       False not reproduced
   whole       row all   four b | groups        -75        -270.0        -230.0         205          100.0           95.0   
[... 129 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('nb.py').read()
rep=[
('''print("\\nReadings where it holds:", int(fh.holds.sum()), "of", len(fh))''',
'''print("\\nReadings where it holds:", int(fh.holds.sum()), "of", len(fh))
print("Largest /ju/ z at +250 ms among lips-positive GLM electrodes, over all readings and subjects:",
      max(float(v.split(" / ")[2]) for c in fh.columns if "max /ju/" in c for v in fh[c]))'''),
('''print("\\nOutcome over readings:", overall(f3.outcome))
print("Total electrodes''','''print("\\nOutcome over readings:", overall(f3.outcome))
print("Ranges over readings: mean onset Lips", f3["onset Lips"].min(), "to", f3["onset Lips"].max(),
      "| Tongue", f3["onset Tongue"].min(), "to", f3["onset Tongue"].max(), "| Jaw", f3["onset Jaw"].min(), "to", f3["onset Jaw"].max(),
      "| Larynx", f3["onset Larynx"].min(), "to", f3["onset Larynx"].max(), "| peak Back", f3["peak Back"].min(), "to", f3["peak Back"].max(),
      "| peak High", f3["peak High"].min(), "to", f3["peak High"].max())
print("ANOVA F", f3.F.min(), "to", f3.F.max(), "| readings with p < 1e-10:", int((f3.p < 1e-10).sum()), "of", len(f3),
      "| conditions holding per reading:", (f3["lips,tongue < acoustic"].astype(int) + f3["jaw,larynx later"] + f3["vowel peaks 250+-25"]).value_counts().to_dict())
print("Total electrodes'''),
('''print("Outcome over readings:", overall(sp.outcome))''','''print("Outcome over readings:", overall(sp.outcome))
g = sp[~sp.clusters.str.startswith("kmeans")]
print("Phonetic-group readings: consonant peak", g["cons peak"].min(), "to", g["cons peak"].max(), "| vowel peak", g["vowel peak"].min(), "to", g["vowel peak"].max(),
      "| consonant onset (a)", g["cons onset a"].min(), "to", g["cons onset a"].max(), "| (b)", g["cons onset b"].min(), "to", g["cons onset b"].max(),
      "| vowel onset (a)", g["vowel onset a"].min(), "to", g["vowel onset a"].max(), "| (b)", g["vowel onset b"].min(), "to", g["vowel onset b"].max())
g = sp[sp.clusters.str.startswith("kmeans")]
print("k-means readings: peak of the single curve", g["cons peak"].min(), "to", g["cons peak"].max())'''),
]
for a,b in rep:
    assert a in s, a[:50]; s=s.replace(a,b)
open('nb.py','w').write(s)
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && python devrun.py > dev.out 2>&1; grep -n "Largest /ju/\|Ranges over\|ANOVA F\|Phonetic-group\|k-means readings\|Traceback\|Error" dev.out
```

```
283:Largest /ju/ z at +250 ms among lips-positive GLM electrodes, over all readings and subjects: 1.19
434:Ranges over readings: mean onset Lips -270 to -54 | Tongue -26 to 220 | Jaw -270 to -116 | Larynx -111 to 112 | peak Back 235 to 301 | peak High 276 to 317
435:ANOVA F 9.9 to 39.2 | readings with p < 1e-10: 51 of 64 | conditions holding per reading: {0: 64}
633:Phonetic-group readings: consonant peak -145 to 10 | vowel peak 200 to 235 | consonant onset (a) -305.0 to -230.0 | (b) -285.0 to -180.0 | vowel onset (a) 60.0 to 100.0 | (b) 90.0 to 105.0
634:k-means readings: peak of the single curve -135 to 360
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('nb.py').read()
def sub(a,b):
    global s
    assert s.count(a)>=1, a[:60]
    s=s.replace(a,b,1)
# fig1f-h
sub('''# **Result: not reproduced.** Under all 64 readings no GLM electrode with a positive lips weight
# reaches z = 2 for /ju/ at +250 ms in any subject; the largest /ju/ value among them is below 2
# in every reading (table).''','''# **Result: not reproduced.** Under all 64 readings no GLM electrode with a positive lips weight
# reaches z = 2 for /ju/ at +250 ms in any subject; the largest /ju/ value among them, over all
# readings and subjects, is 1.19.''')
# fig3d
sub('''# **Result: not reproduced.** Under every one of the 64 readings, at most one of the three order
# conditions holds, and none holds in most: the lips correlations begin before the annotated
# acoustic onset (about -110 ms) but the tongue correlations begin after the C-V transition (mean
# onsets -26 to +213 ms), the jaw begins as early as the lips, not later, and the high-tongue peak
# lies beyond 275 ms in most readings. The ANOVA across articulators is significant (F 9.9 to 29.5),
# with p below 1e-10 in some readings and not in others. Electrode counts are 173 to 226 (paper 211).''',
'''# **Result: not reproduced.** Under every one of the 64 readings none of the three order conditions
# holds. The lips correlations begin before the annotated acoustic onset (-110 ms; mean lips onset
# -270 to -54 ms) but the tongue correlations begin at or after the C-V transition (-26 to +220 ms);
# the jaw begins as early as the lips (-270 to -116 ms), not later; and the high-tongue peak is at
# 276 to 317 ms, outside 250 +- 25 ms. The ANOVA across the six articulators has F = 9.9 to 39.2,
# with p below 1e-10 in 51 of the 64 readings. Electrode counts are 162 to 226 (paper 211).''')
# pca
sub('''# **Result: blocked (methods_underspecified).** With each electrode's concatenated series z-scored
# (`row`), the first nine PCs explain a mean of 0.62 to 0.65 over subjects under every baseline, CV
# set and window, within 0.54 to 0.66. With each electrode z-scored across syllables at each time
# (`time`), the mean is 0.53 to 0.55, below the tolerance in most readings.''','''# **Result: blocked (methods_underspecified).** With each electrode's concatenated series z-scored
# (`row`), the first nine PCs explain a mean of 0.60 to 0.64 over subjects under every baseline, CV
# set and window, within 0.54 to 0.66. With each electrode z-scored across syllables at each time
# (`time`), the mean is 0.49 to 0.55, below the tolerance in seven of eight readings.''')
sub('''# **Result: not reproduced.** Three clusters do not have the highest mean silhouette under any
# reading, and the silhouettes are lower than the paper's (k = 3: 0.18 to 0.28 against 0.47).''','''# **Result: not reproduced.** Three clusters do not have the highest mean silhouette under any
# reading, and the silhouettes are lower than the paper's (k = 3: 0.19 to 0.28 against 0.47).''')
# suppfig11
sub('''# %% [markdown]
# **Result: see the summary.**

# %% [markdown]
# ## fig4c-d-hierarchy''','''# %% [markdown]
# **Result: blocked (methods_underspecified).** The state-space clusters match the major
# articulators and the vowels more than chance under every reading (p from 1e-20 to 4e-16 for
# consonants). The observed consonant medians (0.60 to 0.78) are above the paper's 0.50 +- 0.05,
# and the vowel medians (0.41 to 0.65) mostly below its 0.65; so with every CV the outcome is
# partially reproduced under each reading. With only CVs of 15 or more renditions and `row`
# z-scoring, the vowel test gives p = 5e-08 and 3e-08, which misses the p < 1e-10 bound, so those
# readings give not reproduced.

# %% [markdown]
# ## fig4c-d-hierarchy''')
# fig4c-d
sub('''# %% [markdown]
# **Result: see the summary.**

# %% [markdown]
# ## fig4ef-feature-correlations''','''# %% [markdown]
# **Result: blocked (methods_underspecified).** The rule (both the consonant and the vowel split hold
# in a subject) holds only in EC2, and only with every CV and `row` z-scoring (partially
# reproduced, 4 readings). Under the other 12 readings no subject meets both, mostly because one
# Ward cluster takes most of the CVs; the vowel split (/u/ against /a/ and /i/) holds in EC2 under
# most readings, and in GP31 under none.

# %% [markdown]
# ## fig4ef-feature-correlations''')
sub('''# **Result: partially reproduced.** In the early window, constriction location correlates with the
# state-space distances more than constriction degree, and degree more than the vowel, with
# p < 1e-10 under every reading (n = 297, 99 times x 3 subjects). In the late window, vowel
# configuration does not correlate most: location correlates more than the vowel features in every
# reading, and vowel exceeds degree with p < 1e-10 in a few readings only (table). With Hamming
# distances the result is the same.''','''# **Result: blocked (methods_underspecified).** In the early window, constriction location
# correlates with the state-space distances more than constriction degree, and degree more than the
# vowel, with p < 1e-10 under every reading with Euclidean distances (n = 297, 99 times x 3
# subjects). In the late window the result depends on the CV set: with every CV, location
# correlates more than the vowel features (partially reproduced); with only CVs of 15 or more
# renditions the vowel features correlate more than location in every reading, and more than
# degree with p < 1e-10 under `time` z-scoring (reproduced) but not under `row` (partially). With
# Hamming distances (a variant), the early location-over-degree test misses 1e-10 with 15+ CVs.''')
sub('''# **Result: not reproduced.** Under no reading are both peaks near the paper's. With the phonetic
# groups the consonant separability peaks between -145 and +10 ms (paper -200 ms) and the vowel
# separability at 200 to 230 ms; with k-means at each time a single curve peaks near +300 ms for
# both. The consonant onsets (-185 to -280 ms) are close to the paper's -300 ms under some readings,
# and the vowel onsets (75 to 110 ms) later than its 50 ms.''','''# **Result: not reproduced.** Under no reading are both peaks within tolerance. With the phonetic
# groups the consonant separability peaks at -145 to +10 ms (paper -200 +- 20) and the vowel
# separability at 200 to 235 ms (paper 250 +- 25, so within it in some readings); with k-means at
# each time there is one curve for both, peaking anywhere from -135 to 360 ms. The consonant onsets
# (-305 to -180 ms) reach the paper's -300 +- 30 ms under some readings, and the vowel onsets (60
# to 105 ms) are later than its 50 +- 10 ms.''')
sub('''# **Result: not reproduced.** Under every reading, tongue weights are not larger than lips weights;
# the lips weights are the larger (median paired difference of log10 weights for tongue minus lips
# negative, printed above), so the first condition fails in all three PCs. Jaw and larynx also
# differ in most readings.''','''# **Result: not reproduced.** Under every reading the condition fails in all three PCs. In the
# reading printed in full, the lips weights are larger than the tongue weights (the median paired
# difference of log10 weights, lips minus tongue, is positive with corrected p = 8e-05), and jaw and
# larynx differ (corrected p = 3e-06).''')
open('nb.py','w').write(s)
EOF
grep -n "PC1 (pre" $TMPDIR/dev.out | head -2
```

```
959:PC1 (pre, all, ('per subject', 'per articulator', 'threshold'), all vSMC, n=268): median paired differences and corrected p {'Li-To': '+0.03 p=1e+00', 'Li-La': '+0.13 p=1e-03', 'Li-Ja': '-0.08 p=1e-01', 'To-La': '+0.09 p=3e-02', 'To-Ja': '-0.14 p=2e-04', 'La-Ja': '-0.28 p=5e-11'}
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('nb.py').read()
a='''# reading printed in full, the lips weights are larger than the tongue weights (the median paired
# difference of log10 weights, lips minus tongue, is positive with corrected p = 8e-05), and jaw and
# larynx differ (corrected p = 3e-06).'''
b='''# reading printed in full (all 268 vSMC electrodes), the tongue weights are not larger than the
# lips weights (median paired difference of log10 weights, lips minus tongue, +0.03, corrected
# p = 1), and jaw and larynx differ (corrected p = 5e-11).'''
assert a in s; s=s.replace(a,b); open('nb.py','w').write(s)
EOF
sed -n '/cell 19/,/Outcome over readings/p' dev.out
```

```
===== cell 19 tags=["claim:suppfig11-co-clustering"]
baseline z-scoring CVs    cons a: n, obs, null, p    cons b: n, obs, null, p     vowel: n, obs, null, p    outcome (a)    outcome (b)
     pre       row all 133, 0.750, 0.395, 2.2e-16 160, 0.667, 0.385, 1.0e-17 169, 0.486, 0.386, 3.8e-11      partially      partially
     pre       row 15+ 131, 0.750, 0.338, 2.5e-19 158, 0.711, 0.336, 2.6e-20 167, 0.444, 0.383, 4.7e-08 not reproduced not reproduced
     pre      time all 133, 0.720, 0.355, 5.5e-16 160, 0.645, 0.350, 8.3e-16 169, 0.512, 0.354, 2.8e-16      partially      partially
     pre      time 15+ 131, 0.706, 0.350, 1.6e-18 158, 0.595, 0.345, 1.0e-18 167, 0.583, 0.349, 1.9e-18      partially      partially
   whole       row all 133, 0.783, 0.390, 1.3e-17 160, 0.667, 0.384, 1.9e-19 169, 0.493, 0.390, 1.6e-11      partially      partially
   whole       row 15+ 131, 0.750, 0.346, 2.9e-19 158, 0.651, 0.337, 3.0e-20 167, 0.409, 0.388, 2.8e-08 not reproduced not reproduced
   whole      time all 133, 0.720, 0.349, 4.6e-17 160, 0.645, 0.368, 4.1e-18 169, 0.512, 0.358, 3.2e-16      partially      partially
   whole      time 15+ 131, 0.720, 0.341, 3.7e-19 158, 0.636, 0.344, 1.7e-19 167, 0.650, 0.356, 1.6e-19      partially      partially
Expected: consonants 0.50 +- 0.05 against 0.32 +- 0.032; vowels 0.65 +- 0.065 against 0.37 +- 0.037; p < 1e-10
Outcome over readings: differ by reading: not reproduced 4, partially 12
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('nb.py').read()
a=s[s.index('# **Result: blocked (methods_underspecified).** The state-space clusters match'):s.index('# readings give not reproduced.')+len('# readings give not reproduced.')]
b='''# **Result: blocked (methods_underspecified).** The state-space clusters match the major
# articulators more than chance under every reading (p from 3e-20 to 6e-16 for consonants). The
# observed consonant medians (0.60 to 0.78) are above the paper's 0.50 +- 0.05, and the vowel
# medians (0.41 to 0.65) are below its 0.65 +- 0.065 in most readings, so 12 of the 16 readings
# give partially reproduced. With only CVs of 15 or more renditions and `row` z-scoring, the vowel
# test gives p = 5e-08 and 3e-08, which misses the p < 1e-10 bound, and those 4 readings give not
# reproduced.'''
s=s.replace(a,b); open('nb.py','w').write(s)
EOF
grep -n "Result: see the summary" $TMPDIR/nb.py
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('nb.py').read()
i=s.index('# %% [markdown]\n# ## Summary')
s=s[:i]+'''# %% [markdown]
# ## Summary
#
# | Claim | Outcome |
# |---|---|
# | data-composition | partially reproduced |
# | active-electrodes | not reproduced |
# | fig1c-e-articulator-electrodes | blocked: metadata_insufficient |
# | fig1f-h-phonetic-contrasts | not reproduced |
# | fig2a-lips-dorsal | blocked: metadata_insufficient |
# | fig2b-somatotopic-sequence | blocked: metadata_insufficient |
# | suppfig3b-spatial-clustering | blocked: metadata_insufficient |
# | suppfig3d-cross-subject | blocked: metadata_insufficient |
# | suppfig3f-dv-sequence | blocked: metadata_insufficient |
# | suppfig5-intermediate-organization | blocked: metadata_insufficient |
# | suppfig6-mixed-tuning | reproduced |
# | fig3d-timing-sequence | not reproduced |
# | suppfig7-no-latency-difference | blocked: metadata_insufficient |
# | pca-nine-components | blocked: methods_underspecified |
# | fig4a-consonant-clusters | not reproduced |
# | suppfig11-co-clustering | blocked: methods_underspecified |
# | fig4c-d-hierarchy | blocked: methods_underspecified |
# | fig4ef-feature-correlations | blocked: methods_underspecified |
# | fig5c-separability-timing | not reproduced |
# | fig5d-separability-coupling | blocked: methods_underspecified |
# | suppfig13-consonant-vowel-distance | blocked: methods_underspecified |
# | suppfig9-pc-articulator-weights | not reproduced |
#
# A failure to reproduce here may be a failure of this attempt, not of the paper: see the
# reasoning and the differences from the paper's method.
#
# **How the analysis differs from the paper's.** High gamma is computed here from the raw ECoG, as
# the Methods describe, with a filter bank whose widths the paper does not give (a standard choice)
# and with the dataset's bad-channel flags in place of the paper's inspection. The baseline for the
# z-scores is not given by the paper; both readings of the claims file are run. vSMC electrodes are
# those labelled precentral or postcentral (268, against the paper's 266). The acoustic onset of
# fig3d is the hand-marked syllable start, as the audio is not in the dandiset. Two method details
# the claims file does not fix are run under both readings and asked as questions: how the
# state-space input is z-scored, and whether CVs with fewer than 15 renditions are kept. Most of the
# blocked outcomes for the state-space claims come from these readings giving different results,
# and an answer could settle them. The GLM weights used by fig1f-h, suppfig6 and suppfig9 come from
# claim fig2a-lips-dorsal, which is blocked for its spatial judgement only; the weights need no
# positions, so these claims are tested.
#
# **What was found about the dataset.** It holds four subjects; EC2, GP31 and GP33 fit the paper's
# EC2, EC31 and EC33 (assumed, not shown), and EC9 is not in the paper. The audio was removed. No
# electrode has a position relative to the central sulcus or the Sylvian fissure, and one of the
# three subjects (GP33) has no coordinates at all, so seven spatial findings cannot be tested. The
# coordinates of EC2 and GP31 have no unit or frame. GP31 has two renditions of /thi/ and none of
# /tha/ or /thu/, and up to 107 renditions of other CVs; EC2 has 10 of /thi/; the paper states 15 to
# 100 per CV. Two labels are misspelt (`she`, `ha`). Electrode ids start at 0 in EC2 and GP31 and at 1
# in GP33 and EC9. 177 kept trials overlap intervals marked as ECoG artefacts.

# %%
print(f"notebook ran in {(time.time() - started) / 60:.1f} min")
'''
open('nb.py','w').write(s)
EOF
grep -c "" $TMPDIR/nb.py
```

```
1221
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('nb.py').read()
a='''print("Spellings merged: 'she' -> 'shee', 'ha' -> 'haa'.'''
b='''print("Labels merged as misspellings:", labels[labels.label.isin(list(B.SPELLING))].groupby(["subject", "label"]).size().to_dict())
print("Spellings merged: 'she' -> 'shee', 'ha' -> 'haa'.'''
assert a in s; s=s.replace(a,b); open('nb.py','w').write(s)
EOF
. work/bin/activate && python conv.py nb.py entries/000019-bouchard-2013/reproduce_bouchard_2013.ipynb && cd entries/000019-bouchard-2013 && cat > requirements.in <<'EOF'
dandi
h5py
matplotlib
numpy
pandas
remfile
requests
scikit-learn
scipy
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: 000019-bouchard-2013
type: reproduction
title: Speech articulation in human sensorimotor cortex (Bouchard et al. 2013)
description: Tests the findings of Bouchard, Mesgarani, Johnson and Chang (2013) on dandiset 000019,
  which holds raw ECoG and syllable annotations of subjects reading consonant-vowel syllables. High
  gamma is computed from the raw voltage. It tests the active electrodes, the articulator timing,
  the mixed tuning of electrodes and the cortical state-space analyses. The spatial maps cannot be
  tested, as the dandiset gives no electrode positions relative to the central sulcus and Sylvian
  fissure.
license: Apache-2.0
notebooks:
- path: reproduce_bouchard_2013.ipynb
  title: Reproducing Bouchard et al. (2013) from dandiset 000019
  runtime_minutes: 18
helpers:
- bouchard.py
related:
- id: dandi:000019/0.220126.2148
  relation: uses_data
- id: doi:10.1038/nature11911
  relation: reproduces
EOF
cd ../.. && python tools/entry.py lock entries/000019-bouchard-2013 2>&1 | tail -3 && python tools/entry.py check entries/000019-bouchard-2013 2>&1 | tail -10
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/conv.py", line 1, in <module>
    import re, sys, nbformat
ModuleNotFoundError: No module named 'nbformat'
python: can't open file '//tools/entry.py': [Errno 2] No such file or directory
python: can't open file '//tools/entry.py': [Errno 2] No such file or directory
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001 && python conv.py nb.py entries/000019-bouchard-2013/reproduce_bouchard_2013.ipynb && cd  && ls entries/000019-bouchard-2013 && python tools/entry.py lock entries/000019-bouchard-2013 2>&1 | tail -3 && python tools/entry.py check entries/000019-bouchard-2013 2>&1 | tail -10
```

```
__pycache__
bouchard.py
reproduce_bouchard_2013.ipynb
                [--max-minutes MAX_MINUTES]
                {lock,check,run,all,handover} entry
entry.py: error: entries/000019-bouchard-2013 has no entry.yaml
usage: entry.py [-h] [--output-dir OUTPUT_DIR] [--timeout TIMEOUT]
                [--max-minutes MAX_MINUTES]
                {lock,check,run,all,handover} entry
entry.py: error: entries/000019-bouchard-2013 has no entry.yaml
```

**Agent calls Write**

```json
{
 "file_path": "entries/000019-bouchard-2013/entry.yaml",
 "content": "schema_version: 1\nname: 000019-bouchard-2013\ntype: reproduction\ntitle: Speech articulation in human sensorimotor cortex (Bouchard et al. 2013)\ndescription: Tests the findings of Bouchard, Mesgarani, Johnson and Chang (2013) on dandiset 000019,\n  which holds raw ECoG and syllable annotations of subjects reading consonant-vowel syllables. High\n  gamma is computed from the raw voltage. It tests the active electrodes, the articulator timing,\n  the mixed tuning of electrodes and the cortical state-space analyses. The spatial maps cannot be\n  tested, as the dandiset gives no electrode positions relative to the central sulcus and Sylvian\n  fissure.\nlicense: Apache-2.0\nnotebooks:\n- path: reproduce_bouchard_2013.ipynb\n  title: Reproducing Bouchard et al. (2013) from dandiset 000019\n  runtime_minutes: 18\nhelpers:\n- bouchard.py\nrelated:\n- id: dandi:000019/0.220126.2148\n  relation: uses_data\n- id: doi:10.1038/nature11911\n  relation: reproduces\n"
}
```

```
File created successfully at: entries/000019-bouchard-2013/entry.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "entries/000019-bouchard-2013/requirements.in",
 "content": "dandi\nh5py\nmatplotlib\nnumpy\npandas\nremfile\nrequests\nscikit-learn\nscipy\n"
}
```

```
File created successfully at: entries/000019-bouchard-2013/requirements.in (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
rm -rf entries/000019-bouchard-2013/__pycache__; python tools/entry.py lock entries/000019-bouchard-2013 2>&1 | tail -3 && python tools/entry.py check entries/000019-bouchard-2013 2>&1 | tail -10
```

```
wrote entries/000019-bouchard-2013/requirements.lock.txt
0 error(s)
```

**Agent calls Bash**

```bash
time python tools/entry.py all entries/000019-bouchard-2013 2>&1 | tail -15
```

```
Installed kernelspec registry-000019-bouchard-2013 in executed/000019-bouchard-2013/.venv/share/jupyter/kernels/registry-000019-bouchard-2013
0 error(s)
pass  reproduce_bouchard_2013.ipynb  (873 s)

real	14m48.884s
user	24m27.978s
sys	3m42.406s
```

**Agent calls Bash**

```bash
ls executed/000019-bouchard-2013/; python - <<'EOF'
import nbformat
nb=nbformat.read('executed/000019-bouchard-2013/reproduce_bouchard_2013.ipynb',4)
for c in nb.cells:
    if c.cell_type!='code': continue
    out=''.join(o.get('text','') for o in c.get('outputs',[]) if o.get('output_type')=='stream')
    err=[o for o in c.get('outputs',[]) if o.get('output_type')=='error']
    keys=['Outcome over','Largest','Ranges over','ANOVA F','Phonetic-group','k-means readings','notebook ran','processed','read metadata','Labels merged','Mean over subjects','Pairs sharing','vowel: peak','consonant: peak','Subject and numbering']
    for l in out.splitlines():
        if any(k in l for k in keys): print(l[:300])
    if err: print('ERROR', err)
EOF
```

```
reproduce_bouchard_2013.ipynb
result.json
read metadata of 31 files of dandiset 000019 version 0.220126.2148 in 40 s
processed 24 blocks in 661 s
Pairs sharing sample count, trial times or first 2000 samples of 4 channels:
Labels merged as misspellings: {('EC2', np.str_('she')): 2, ('EC9', np.str_('ha')): 1, ('EC9', np.str_('she')): 1, ('GP33', np.str_('ha')): 2}
vowel: peak 0.83 at 250 ms; mean before -400 ms 0.39
consonant: peak 0.89 at -75 ms; mean before -400 ms 0.59
Mean over subjects (criterion 27 to 33; rest is a variant, not a reading):
Outcome over readings: not reproduced
Subject and numbering pairs that put all six named electrodes on vSMC: []
Largest /ju/ z at +250 ms among lips-positive GLM electrodes, over all readings and subjects: 1.19
Outcome over readings: not reproduced
Outcome over readings: reproduced
Outcome over readings: not reproduced
Ranges over readings: mean onset Lips -270 to -54 | Tongue -26 to 220 | Jaw -270 to -116 | Larynx -111 to 112 | peak Back 235 to 301 | peak High 276 to 317
ANOVA F 9.9 to 39.2 | readings with p < 1e-10: 51 of 64 | conditions holding per reading: {0: 64}
Outcome over readings: differ by reading: not reproduced 7, reproduced 9
Mean over subjects (paper 0.45, 0.47, 0.43):
Outcome over readings: not reproduced
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
sed -i 's/runtime_minutes: 18/runtime_minutes: 15/' entries/000019-bouchard-2013/entry.yaml; ls schemas; python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s,indent=1)[:5000])"; head -60 questions/000009.yaml
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
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
[... 244 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));p=s['properties']
print(json.dumps(p['outcomes']['items'],indent=0)[:3500]); print(json.dumps({k:v for k,v in p.items() if k in ('inputs','findings','verifications')},indent=0)[:2500])"
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
[... 228 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "questions/000019.yaml",
 "content": "# Questions from attempt 000019-bouchard-2013-01 (author, 2026-10-22) about the claims file\n# claims/000019/10.1038-nature11911.yaml. Each is asked under docs/protocol.md, Author, step 1.6; the\n# attempt runs every reading it can see and records the claims whose outcome depends on the answer.\ndandiset: \"000019\"\npaper: doi:10.1038/nature11911\nquestions:\n- claim: pca-nine-components\n  also: [fig4a-consonant-clusters, suppfig11-co-clustering, fig4c-d-hierarchy, fig4ef-feature-correlations,\n    fig5c-separability-timing, fig5d-separability-coupling, suppfig13-consonant-vowel-distance,\n    suppfig9-pc-articulator-weights]\n  asked: 2026-10-22\n  question: Before the PCA, is each electrode's high gamma z-scored over its whole concatenated (CV x\n    time) series (`row`), or across syllables separately at each time point (`time`)? The second\n    removes the mean time course shared by all syllables. Is the same z-scored input projected onto\n    the PCs to give the state K(s, t)?\n  passage: Methods, PCA and Cortical-State Space, \"Each electrode's time series was z-scored across\n    syllables to normalize response variability across electrodes.\"\n  why: With `row` the nine PCs explain 0.60 to 0.64 of the variance (within 0.6 +- 0.06), with `time`\n    0.49 to 0.55 (mostly outside). Consonant-vowel distances exceed consonant-consonant distances\n    under `row` and not under `time` (suppfig13), and the hierarchy and late feature-correlation\n    results also change. The attempt runs both, and these claims are blocked as\n    methods_underspecified where they differ.\n- claim: data-composition\n  also: [active-electrodes, fig1f-h-phonetic-contrasts, suppfig6-mixed-tuning, fig3d-timing-sequence,\n    pca-nine-components, fig4a-consonant-clusters, suppfig11-co-clustering, fig4c-d-hierarchy,\n    fig4ef-feature-correlations, fig5c-separability-timing, fig5d-separability-coupling,\n    suppfig13-consonant-vowel-distance, suppfig9-pc-articulator-weights]\n  asked: 2026-10-22\n  question: The dandiset has CVs with fewer than 15 renditions (EC2 /thi/ 10, GP31 /thi/ 2) and GP31\n    lacks /tha/ and /thu/. Should CVs with fewer than 15 renditions be left out of the per-syllable\n    averages, as the paper's range of 15 to 100 renditions suggests, or kept?\n  passage: Methods, Subjects and Experimental Task, \"Each CV was produced between 15 and 100 times.\"\n    The paper's 168 CVs (57 + 57 + 54, Fig. 3c legend) match neither choice (169 kept, 167 left out).\n  why: GP31's /thi/ mean over two renditions is an outlier in the state space; with it the k = 2\n    silhouette of GP31 is 0.78, without it 0.24 to 0.27. The active-electrode count of GP31 falls\n    from 49 to 9 (pre baseline). Co-clustering, the hierarchy and the late feature correlations\n    change outcome with the choice. The attempt runs both.\n- claim: fig3d-timing-sequence\n  asked: 2026-10-22\n  question: The dandiset has no audio, so the acoustic onset cannot be taken from the cochlear\n    spectrogram of the prototype rendition. Is the hand-marked syllable start of the trial table\n    (`start_time`, \"the start ... of each syllable\" in the dandiset description) an acceptable\n    acoustic onset for the condition \"lip and tongue correlations began well before sound onset\"?\n  passage: Methods, Acoustic Analysis, \"The onset, peak, and offset of acoustic power were extracted\n    for each syllable prototype using a thresholding procedure.\"\n  why: The annotated onset is -110 ms on average (CV range -257 to -11 ms). It does not decide the\n    outcome here, since the tongue correlations begin after the C-V transition in every reading,\n    but it would for a dataset where the lips and tongue onsets fall near it.\n- claim: active-electrodes\n  also: [fig1f-h-phonetic-contrasts, fig3d-timing-sequence, pca-nine-components]\n  asked: 2026-10-22\n  question: The dandiset marks a rest period per block, \"when the subject was silent, which can be\n    used as a baseline\". Does the paper's \"baseline data\" allow this reading, besides the two the\n    claims file names (a window before each utterance, and the whole recording)?\n  passage: Methods, Data acquisition and Signal Processing, \"High-γ power was z-scored relative to\n    the mean and standard deviation of baseline data for each channel.\"\n  why: The rest period has lower high gamma than the rest of the block in most blocks, so z-scores\n    are larger. The mean active-electrode count is 34.0 per subject with every CV and 27.0 with CVs\n    of 15 or more renditions (paper about 30, tolerance 27 to 33), against 7.0 to 24.3 under the\n    claims file's readings. The attempt shows it as a variant, not a reading.\n- claim: fig2a-lips-dorsal\n  also: [fig2b-somatotopic-sequence, suppfig3b-spatial-clustering, suppfig3d-cross-subject,\n    suppfig3f-dv-sequence, suppfig5-intermediate-organization, suppfig7-no-latency-difference,\n    fig1c-e-articulator-electrodes]\n  asked: 2026-10-22\n  question: The dandiset gives no electrode positions relative to the central sulcus or the Sylvian\n    fissure. EC2 and GP31 have x, y, z coordinates with no unit or frame (spacing about 4 mm), GP33\n    has none, and the labels are atlas gyri (precentral, postcentral and others; none marks the\n    guenon). Does the paper give any way to obtain the anterior-posterior and dorsal-ventral\n    distances from such data, for example from the grid geometry?\n  passage: Methods, Spatial Organization Derived from a General Linear Model, \"We used a Cartesian\n    plane defined by the Anterior-Posterior distance from the Central Sulcus (ordinate) and the\n    Dorsal-Ventral distance from the Sylvian Fissure (azimuth).\"\n  why: Without them the seven spatial claims are blocked as metadata_insufficient. For information\n    only, the median z coordinate of the top lips weights lies above that of the tongue weights in\n    EC2 and GP31 (36.6 against 15.6 in EC2 under the first reading).\n"
}
```

```
File created successfully at: questions/000019.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python - <<'EOF'
import nbformat
nb=nbformat.read('executed/000019-bouchard-2013/reproduce_bouchard_2013.ipynb',4)
for c in nb.cells:
    if 'claim:fig4a-consonant-clusters' in c.metadata.get('tags',[]):
        out=''.join(o.get('text','') for o in c.outputs if 'text' in o)
        print('\n'.join(l for l in out.splitlines() if 'GP31' in l))
EOF
```

```
pre       row all    GP31 0.782 0.410 0.252
     pre       row 15+    GP31 0.370 0.239 0.227
     pre      time all    GP31 0.759 0.326 0.223
     pre      time 15+    GP31 0.303 0.209 0.210
   whole       row all    GP31 0.801 0.377 0.249
   whole       row 15+    GP31 0.329 0.228 0.219
   whole      time all    GP31 0.776 0.307 0.230
   whole      time 15+    GP31 0.244 0.201 0.201
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "questions/000019.yaml",
 "old_string": "silhouette of GP31 is 0.78, without it 0.24 to 0.27.",
 "new_string": "silhouette of GP31 is 0.76 to 0.80, without it 0.24 to 0.37."
}
```

```
The file questions/000019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python - <<'EOF'
import nbformat
nb=nbformat.read('executed/000019-bouchard-2013/reproduce_bouchard_2013.ipynb',4)
for c in nb.cells:
    t=c.metadata.get('tags',[])
    if any(x in t for x in ['claim:fig4c-d-hierarchy','claim:fig5d-separability-coupling']):
        out=''.join(o.get('text','') for o in c.outputs if 'text' in o)
        print(out[:200] if 'fig5d' in str(t) else '\n'.join(l for l in out.splitlines() if 'vowel' in l or 'True' in l)[:3000])
EOF
```

```
baseline z-scoring CVs subject     cons (a) majorities  cons (a) in home  cons (a) holds  cons (a) co-clust     cons (b) majorities  cons (b) in home  cons (b) holds  cons (b) co-clust a/i/u in cluster 1  vowel holds
     pre       row all     EC2   coronal/labial/dorsal              0.98            True               0.98   coronal/labial/dorsal              0.93            True               0.92     0.74/0.58/0.11         True
     pre       row all    GP33  coronal/coronal/labial              0.64           False               0.70  coronal/coronal/labial              0.63           False               0.67     0.53/0.84/0.26         True
     pre       row 15+     EC2  labial/coronal/coronal              0.80           False               0.63  labial/coronal/coronal              0.81           False               0.61     0.58/0.56/0.11         True
     pre       row 15+    GP33  coronal/coronal/labial              0.64           False               0.70  coronal/coronal/labial              0.63           False               0.67     0.53/0.84/0.26         True
     pre      time all     EC2  coronal/labial/coronal              0.73           False               0.67  coronal/labial/coronal              0.74           False               0.67     0.00/0.00/0.89         True
     pre      time 15+     EC2  coronal/labial/coronal              0.73           False               0.65  coronal/labial/coronal              0.74           False               0.65     0.00/0.00/0.84         True
     pre      time 15+    GP31  labial/coronal/coronal              0.69           False               0.67   labial/dorsal/coronal              0.69            True               0.65     0.94/1.00/1.00        False
   whole       row all     EC2   coronal/labial/dorsal              0.98            True               0.98   coronal/labial/dorsal              0.93            True               0.92     0.84/0.79/0.21         True
   whole       row 15+     EC2  labial/coronal/
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001 && python - <<'EOF'
s=open('nb.py').read()
a='''# reproduced, 4 readings). Under the other 12 readings no subject meets both, mostly because one
# Ward cluster takes most of the CVs; the vowel split'''
b='''# reproduced, 4 readings). Under the other 12 readings no subject meets both; in most rows of the
# table two of the three consonant clusters have a coronal majority. The vowel split'''
assert a in s; s=s.replace(a,b); open('nb.py','w').write(s)
EOF
python conv.py nb.py entries/000019-bouchard-2013/reproduce_bouchard_2013.ipynb && echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001 && . work/bin/activate && python -c "
import pickle,numpy as np
for s in ['EC2','GP31','GP33']:
    S,bl=pickle.load(open(f'sub_{s}.pkl','rb'))
    print(s,[round(float(np.nanmedian(b['hg_stats']['rest'][1][~b['bad']]/b['hg_stats']['whole'][1][~b['bad']])),2) for b in bl])
"
```

```
EC2 [0.95, 1.07, 0.94, 1.21, 1.07, 0.95, 1.01]
GP31 [0.94, 0.94, 1.08, 0.98, 1.25, 0.3, 0.98, 1.16, 0.98, 1.0, 0.91, 0.95, 0.9, 1.11]
GP33 [0.91, 0.85, 1.02]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001 && python - <<'EOF'
s=open('nb.py').read()
a='''                     "rest_mean_over_whole": float(np.nanmedian(b["hg_stats"]["rest"][0][g] / b["hg_stats"]["whole"][0][g])),'''
b='''                     "rest_mean_over_whole": float(np.nanmedian(b["hg_stats"]["rest"][0][g] / b["hg_stats"]["whole"][0][g])),
                     "rest_sd_over_whole": float(np.nanmedian(b["hg_stats"]["rest"][1][g] / b["hg_stats"]["whole"][1][g])),'''
assert a in s; s=s.replace(a,b)
a=s[s.index('# Sampling rate 3051.7578 Hz in all files'):s.index('# rest period as baseline;')] if '# rest period as baseline;' in s else None
i=s.index('# Sampling rate 3051.7578 Hz in all files'); j=s.index('\n\n',i)
s=s[:i]+'''# Sampling rate 3051.7578 Hz in all files, the TDT rate the Methods round to 3052 Hz. The `pre`
# baseline (-1000 to -500 ms before each C-V transition) has a median mean within a few percent of
# the whole block's. The rest periods are short (3.3 to 78 s per block) and their statistics differ
# from the whole block's in both directions by block (median ratios above); z-scores against them
# reach higher maxima (ranges above). That variant is shown where it matters.'''+s[j:]
open('nb.py','w').write(s)
EOF
grep -n "Sampling rate 3051.7578 Hz" -A6 nb.py | head -12
```

```
218:# Sampling rate 3051.7578 Hz in all files, the TDT rate the Methods round to 3052 Hz. The `pre`
219-# baseline (-1000 to -500 ms before each C-V transition) has a median mean within a few percent of
220-# the whole block's. The rest periods are short (3.3 to 78 s per block) and their statistics differ
221-# from the whole block's in both directions by block (median ratios above); z-scores against them
222-# reach higher maxima (ranges above). That variant is shown where it matters.
223-
224-# %% tags=["sanity"]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001 && . work/bin/activate && python -c "
import pickle,numpy as np
m=pickle.load(open('meta_rows.pkl','rb'))
for r in m[:3]+m[14:15]+m[28:29]: print(r['path'], np.std(r['fingerprint'],0), r['conversion'])
"
```

```
sub-EC2/sub-EC2_ses-EC2-B1.nwb [5.0183167e-05 4.0462990e-05 3.7388840e-05 3.3211472e-05] 0.001
sub-EC2/sub-EC2_ses-EC2-B105.nwb [3.3590197e-05 3.2238240e-05 2.9079656e-05 2.6356765e-05] 0.001
sub-EC2/sub-EC2_ses-EC2-B15.nwb [3.0265299e-05 2.0156896e-05 1.9348621e-05 2.0048697e-05] 0.001
sub-GP31/sub-GP31_ses-GP31-B1.nwb [6.4667634e-05 5.8113543e-05 6.7546964e-05 6.1574421e-05] 0.001
sub-GP33/sub-GP33_ses-GP33-B1.nwb [3.3091881e-05 3.6298872e-05 4.5955338e-05 4.6731475e-05] 0.001
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001 && python - <<'EOF'
s=open('nb.py').read()
a='''print("Raw values: unit 'volt' with conversion 0.001, so stored values are mV; high-gamma amplitudes above are in uV after conversion.")'''
b='''sd_raw = {s: float(np.median([np.std(m["fingerprint"], axis=0).mean() for m in meta_rows if m["subject"] == s])) for s in B.SUBJECTS}
print("Raw series: unit", meta_rows[0]["unit"], "with conversion", meta_rows[0]["conversion"],
      "| median SD of the stored values over the first 2000 samples of 4 channels:", {k: f"{v:.1e}" for k, v in sd_raw.items()})
print("hg_whole_mean_uV above is the stored high-gamma amplitude x 1e6, without the conversion factor.")'''
assert a in s; s=s.replace(a,b)
a='''# Units: the raw series says volts with a conversion of 0.001, so the stored values are mV; the
# high-gamma amplitude is a few uV, which is consistent with ECoG. Only the z-scores are used.'''
b='''# Units: the raw series says volts with a conversion factor of 0.001, so by NWB the stored values
# times 0.001 are volts. The stored values have an SD of a few 1e-5 (printed above): read as volts
# this is tens of microvolts, a usual ECoG amplitude, while with the factor it would be tens of
# nanovolts. The data are consistent with values already in volts and a wrong conversion factor;
# this does not affect the analysis, which uses z-scores only.'''
assert a in s; s=s.replace(a,b)
open('nb.py','w').write(s)
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001 && python - <<'EOF'
s=open('nb.py').read()
a='''# The consonant's articulator is decoded best before the C-V transition and the vowel after it,
# and neither is decoded above chance level at the start of the epoch (numbers above).'''
b='''# The consonant's articulator is decoded best before the C-V transition (0.89 at -75 ms) and the
# vowel after it (0.83 at 250 ms), and both are near chance at the start of the epoch (vowel 0.39
# against 1/3; consonant 0.59 against a largest-class share of about 0.5).'''
assert a in s; s=s.replace(a,b)
a='''# %% tags=["sanity"]
# Syllables per subject, from the trial labels.'''
b='''# %% [markdown]
# Only one pair of files shares a property (two EC9 blocks with the same number of samples); their
# trial times and first samples differ, so no recording was deposited twice.

# %% tags=["sanity"]
# Syllables per subject, from the trial labels.'''
assert a in s; s=s.replace(a,b)
open('nb.py','w').write(s)
EOF
python conv.py nb.py entries/000019-bouchard-2013/reproduce_bouchard_2013.ipynb && echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "entries/000019-bouchard-2013/README.md",
 "content": "# Bouchard, Mesgarani, Johnson & Chang (2013) from dandiset 000019\n\nTests the findings of [Bouchard et al. (2013)](https://doi.org/10.1038/nature11911) that can be\ntested on [DANDI:000019](https://dandiarchive.org/dandiset/000019/0.220126.2148), which holds raw\nECoG and hand-marked syllable annotations of subjects reading consonant-vowel syllables. High gamma\nis computed here from the raw voltage. The audio and the electrode positions relative to the\ncentral sulcus and Sylvian fissure are not in the dandiset.\n\n| Claim | Outcome |\n|---|---|\n| Data composition (subjects, syllables, renditions, rate) | Partially reproduced |\n| About 30 active vSMC electrodes per subject | Not reproduced |\n| Named electrodes of Fig. 1c-e | Blocked: metadata insufficient |\n| Lips electrode active for /ju/ only (Fig. 1h) | Not reproduced |\n| Spatial maps and their statistics (Fig. 2, Supplementary Figures 3, 5 and 7; seven claims) | Blocked: metadata insufficient |\n| Mixed tuning at single electrodes | Reproduced |\n| Timing sequence of articulator correlations | Not reproduced |\n| Nine PCs explain about 60% of variance | Blocked: methods underspecified |\n| Three k-means clusters most parsimonious | Not reproduced |\n| Co-clustering with articulators and vowels | Blocked: methods underspecified |\n| Hierarchical clustering | Blocked: methods underspecified |\n| Feature correlations, early and late | Blocked: methods underspecified |\n| Separability timing | Not reproduced |\n| Separability coupled to feature correlations | Blocked: methods underspecified |\n| Consonant-vowel distances | Blocked: methods underspecified |\n| PC articulator weights | Not reproduced |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nMost claims blocked as methods underspecified depend on two details the claims file does not fix\nand that were asked as questions (`questions/000019.yaml`): how the state-space input is z-scored,\nand whether syllables with fewer than 15 renditions are kept. The attempt record, with the reasons\nand the differences from the paper's method, is\n[`attempts/000019-bouchard-2013-01.yaml`](../../attempts/000019-bouchard-2013-01.yaml).\n\n- `reproduce_bouchard_2013.ipynb`: the analysis. It takes about 15 minutes, 11 of them streaming\n  about 42 GB of raw ECoG and computing high gamma.\n- `bouchard.py`: streaming the files, high gamma, the paper's articulator and phonetic feature\n  matrices, and the measures (partial correlation, GLM, state space, co-clustering, separability).\n  Other notebooks on this dandiset can import it.\n"
}
```

```
File created successfully at: entries/000019-bouchard-2013/README.md (file state is current in your context — no need to Read it back)
```

**Agent**

Now the attempt record.

**Agent calls Write**

```json
{
 "file_path": "attempts/000019-bouchard-2013-01.yaml",
 "content": "schema_version: 2\nid: 000019-bouchard-2013-01\ndataset:\n  archive: dandi\n  id: \"000019\"\n  version: 0.220126.2148\n  doi: 10.48324/dandi.000019/0.220126.2148\npaper: doi:10.1038/nature11911\ndate: 2026-10-21\nentry: 000019-bouchard-2013\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code (GitHub Actions)\n    model: claude-opus-5-5\n    protocol: pilot-10\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/reproduction-registry/actions/runs/39692741052\ninputs:\n- what: The articulator state matrix (Supplementary Figure 1d) and the phonetic feature matrix\n    (Supplementary Figure 12), transcribed from the figures of the paper's supplement. They define\n    the paper's variables for each syllable; they hold no measurements.\n  source: doi:10.1038/nature11911 (supplement, NIHMS436351-supplement-1.pdf, pages 2 and 15)\noutcomes:\n- claim: data-composition\n  outcome: partially_reproduced\n  notebook: reproduce_bouchard_2013.ipynb\n  output: claim:data-composition\n  measured:\n  - 3\n  - 169\n  - 3051.76\n  notes: The dandiset holds four subjects (EC2, EC9, GP31, GP33); EC2, GP31 and GP33 are taken to be\n    the paper's EC2, EC31 and EC33, and EC9 is not in the paper. The rate is 3051.76 Hz. The three\n    subjects have 57, 55 and 57 CVs (169, paper 168), each with 19 consonants, and 2 to 107\n    renditions per CV (EC2 /thi/ 10, GP31 /thi/ 2, 33 GP31 CVs above 100); leaving out CVs below 15\n    renditions gives 56 + 54 + 57 = 167. The audio was removed. EC2 and GP31 have negative x\n    coordinates (left hemisphere if x is the usual axis); GP33 has no coordinates, so the right\n    hemisphere of EC33 cannot be checked.\n  deviations:\n  - The correspondence of GP31 and GP33 to the paper's EC31 and EC33 is an assumption; no metadata\n    links them.\n- claim: active-electrodes\n  outcome: not_reproduced\n  notebook: reproduce_bouchard_2013.ipynb\n  output: claim:active-electrodes\n  measured: 24.33\n  notes: Mean active vSMC electrodes per subject, every CV, 24.3 with the pre-utterance baseline\n    (EC2 15, GP31 49, GP33 9) and 21.3 with the whole block; with only CVs of 15 or more renditions\n    10.7 and 7.0. Both readings of the change (z above 2, absolute z above 2) give the same counts.\n    None is within 27 to 33. With the dataset's rest period as baseline (a variant, asked as a\n    question) the means are 34.0 and 27.0. The count depends strongly on the threshold (41.7 at\n    1.5, 11.7 at 2.5, pre baseline).\n  deviations:\n  - High gamma computed from the raw ECoG with a filter bank whose widths the paper does not give\n    (standard choice); bad channels from the dataset's flags.\n  - vSMC taken as the electrodes labelled precentral or postcentral, good in every block (268 over\n    the three subjects, paper 266); no label marks the guenon.\n  - CVs with fewer than 15 renditions kept and left out, as two readings (asked as a question).\n- claim: fig1c-e-articulator-electrodes\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notebook: reproduce_bouchard_2013.ipynb\n  output: claim:fig1c-e-articulator-electrodes\n  notes: No subject, numbering from 1 or from 0, puts all six named electrodes on vSMC (at most 4 of\n    6); some are labelled middle or superior temporal or pars opercularis. The criterion blocks the\n    claim in that case. The dataset does not say how the paper numbered electrodes, and gives no\n    distance from the Sylvian fissure for the order part. For information, in EC2 counted from 1,\n    five of the six named electrodes prefer their syllable under both measures and baselines.\n- claim: fig1f-h-phonetic-contrasts\n  outcome: not_reproduced\n  notebook: reproduce_bouchard_2013.ipynb\n  output: claim:fig1f-h-phonetic-contrasts\n  notes: Under all 64 readings (2 baselines, 2 CV sets, 8 timing readings for T_A, 2 p-value\n    readings) no GLM electrode with a positive lips weight has z above 2 for /ju/ at +250 ms in any\n    subject; the largest such /ju/ value is 1.19. The plotted electrodes respond more to /ju/ than\n    to /ja/ and /ji/ at +250 ms, but below the paper's activity threshold. The fricative and manner\n    contrasts are not judged, as the claims file says.\n  deviations:\n  - The lips weights come from the GLM of fig2a-lips-dorsal, which is blocked for its spatial\n    judgement only; the weights and electrode selection need no positions and are computed, so this\n    claim is tested.\n- claim: fig2a-lips-dorsal\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notebook: reproduce_bouchard_2013.ipynb\n  notes: The claim judges where the lips and tongue weights lie as dorsal-ventral distance from the\n    Sylvian fissure. The dandiset gives no electrode position relative to the Sylvian fissure or the\n    central sulcus. EC2 and GP31 have x, y, z coordinates with no unit or frame; GP33 has none.\n    Asked as a question. The GLM electrodes and weights are computed (they need no positions) and\n    used by fig1f-h, suppfig6 and suppfig9. For information only, the median z coordinate of the top\n    10% of lips weights is above that of the tongue weights in EC2 (36.6 against 15.6) and GP31.\n- claim: fig2b-somatotopic-sequence\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: Needs positions relative to the central sulcus and Sylvian fissure in all three subjects\n    (see fig2a-lips-dorsal).\n- claim: suppfig3b-spatial-clustering\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: Needs the smoothed maps in the plane of distances from the central sulcus and Sylvian\n    fissure (see fig2a-lips-dorsal).\n- claim: suppfig3d-cross-subject\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: Needs maps in a common frame across subjects, from distances to the central sulcus and\n    Sylvian fissure (see fig2a-lips-dorsal); GP33 has no coordinates at all.\n- claim: suppfig3f-dv-sequence\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: Needs the maps of suppfig3b-spatial-clustering (see fig2a-lips-dorsal).\n- claim: suppfig5-intermediate-organization\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: Needs Euclidean distances in mm between electrodes in the paper's plane (see\n    fig2a-lips-dorsal). The EC2 and GP31 coordinates have no stated unit or frame, and GP33 has\n    none.\n- claim: suppfig6-mixed-tuning\n  outcome: reproduced\n  notebook: reproduce_bouchard_2013.ipynb\n  output: claim:suppfig6-mixed-tuning\n  notes: Under all 64 readings, each group of GLM electrodes (grouped by largest weight) has its\n    preferred articulator with the largest mean share of positive weight (lips about 63 to 77%,\n    tongue 53 to 96%, larynx 61 to 84%, jaw 72 to 84%) and non-zero shares of the others. Groups hold\n    53 to 110 electrodes over the three subjects. In the readings where GP31 has no tongue window\n    T_A, its tongue weights are missing.\n  deviations:\n  - Uses the GLM weights of fig2a-lips-dorsal, which is blocked for its spatial judgement only.\n- claim: fig3d-timing-sequence\n  outcome: not_reproduced\n  notebook: reproduce_bouchard_2013.ipynb\n  output: claim:fig3d-timing-sequence\n  measured:\n  - 175\n  - 270\n  notes: Under all 64 readings (2 baselines, 2 CV sets, threshold per subject or pooled and over all\n    articulators or per articulator, onset at threshold or half peak, ANOVA on onset or peak) none\n    of the three order conditions holds. Mean lips onsets are -270 to -54 ms, before the annotated\n    acoustic onset (-110 ms), but tongue onsets are -26 to +220 ms; jaw onsets are -270 to -116 ms,\n    as early as the lips; high-tongue peaks are 276 to 317 ms. The ANOVA has F = 9.9 to 39.2 with p\n    below 1e-10 in 51 of 64 readings. Electrodes 162 to 226 (paper 211). Measured values are from the\n    first reading (175 electrodes; mean of back and high tongue peaks, 235 and 305 ms).\n  deviations:\n  - The acoustic onset is the hand-marked syllable start of the trial table, as the audio is not\n    in the dandiset (asked as a question); it does not decide the outcome, since the tongue onsets\n    follow the C-V transition.\n- claim: suppfig7-no-latency-difference\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: Needs electrodes within 10 mm anterior and posterior of the central sulcus and the guenon's\n    boundary; the dandiset gives no distances to the central sulcus and no guenon label.\n- claim: pca-nine-components\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_bouchard_2013.ipynb\n  output: claim:pca-nine-components\n  measured: 0.625\n  notes: With each electrode's concatenated series z-scored (`row`), nine PCs explain a mean of 0.60\n    to 0.64 over subjects under every baseline, CV set and window (within 0.54 to 0.66); with each\n    electrode z-scored across syllables at each time (`time`), 0.49 to 0.55, outside in seven of\n    eight readings. The z-scoring is not fixed by the claims file and was asked as a question. No\n    sharp change at the ninth eigenvalue is seen; not judged. Measured is the first reading (pre,\n    row, every CV, epoch).\n  deviations:\n  - Two readings of the z-scoring added, as the claims file's description allows both (asked as a\n    question).\n- claim: fig4a-consonant-clusters\n  outcome: not_reproduced\n  notebook: reproduce_bouchard_2013.ipynb\n  output: claim:fig4a-consonant-clusters\n  measured:\n  - 0.281\n  - 0.4\n  - 0.231\n  notes: Under all 8 readings (baseline, z-scoring, CV set) k = 3 does not have the highest mean\n    silhouette; k = 3 gives 0.19 to 0.28 against the paper's 0.47. With every CV, GP31's k = 2\n    silhouette is 0.76 to 0.80 because its /thi/ (2 renditions) stands apart; without it 0.24 to\n    0.37. Measured values are the first reading (pre, row, every CV) for k = 3, 2 and 4.\n- claim: suppfig11-co-clustering\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_bouchard_2013.ipynb\n  output: claim:suppfig11-co-clustering\n  measured:\n  - 0.75\n  - 0.395\n  - 0.486\n  - 0.386\n  notes: Clusters match the major articulators beyond chance in every reading (p 3e-20 to 6e-16).\n    Observed consonant medians 0.60 to 0.78 (paper 0.50 +- 0.05), vowel medians 0.41 to 0.65 (paper\n    0.65 +- 0.065), nulls 0.34 to 0.40. Twelve of 16 readings give partially reproduced; with only\n    CVs of 15 or more renditions and row z-scoring the vowel test gives p = 5e-08 and 3e-08, above\n    1e-10, and not reproduced. The readings that differ come from the two questions asked.\n    Measured is the first reading (pre, row, every CV, labels a).\n- claim: fig4c-d-hierarchy\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_bouchard_2013.ipynb\n  output: claim:fig4c-d-hierarchy\n  notes: Both splits hold together only in EC2, with every CV and row z-scoring (partially reproduced\n    in 4 of 16 readings); under the others no subject meets both, often because two of the three\n    consonant clusters have a coronal majority. The vowel split holds in EC2 in most readings and in\n    GP31 in none. The purity rule of two thirds is the claims file's own.\n- claim: fig4ef-feature-correlations\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_bouchard_2013.ipynb\n  output: claim:fig4ef-feature-correlations\n  notes: Early window, location over degree over vowel with p < 1e-10 under every Euclidean reading\n    (n = 297). Late window, with every CV location correlates more than the vowel features\n    (partially reproduced); with only CVs of 15 or more renditions the vowel features correlate most,\n    with p < 1e-10 against both other sets under time z-scoring (reproduced) and not against degree\n    under row (partially). Hamming distances (variant) agree, except that the early location test\n    misses 1e-10 with 15+ CVs.\n- claim: fig5c-separability-timing\n  outcome: not_reproduced\n  notebook: reproduce_bouchard_2013.ipynb\n  output: claim:fig5c-separability-timing\n  measured:\n  - 5\n  - -240\n  - 200\n  - 100\n  notes: Under all 40 readings (8 baseline, z-scoring and CV readings by five cluster readings) the\n    peaks are not both within tolerance. With phonetic groups the consonant peak is at -145 to +10\n    ms (paper -200) and the vowel peak at 200 to 235 ms; with k-means at each time one curve serves\n    both, peaking between -135 and 360 ms. Consonant onsets are -305 to -180 ms, vowel onsets 60 to\n    105 ms. Measured is the first reading (pre, row, every CV, groups a; onset reading a).\n  deviations:\n  - The onset reading (a) takes the curve's value at -500 ms as its pre-epoch level, the earliest\n    time of the epoch.\n- claim: fig5d-separability-coupling\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_bouchard_2013.ipynb\n  output: claim:fig5d-separability-coupling\n  notes: With phonetic-group clusters and the matching feature set (location for consonants, vowel\n    for vowels), all six R2 lie within 0.38 to 1 with p < 1e-10 in all 32 such readings (R2 0.40 to\n    0.98). With the mean of the three feature sets, or with k-means clusters, the coupling fails (R2\n    near 0 in some subjects). The claims file's own readings give different outcomes.\n- claim: suppfig13-consonant-vowel-distance\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_bouchard_2013.ipynb\n  output: claim:suppfig13-consonant-vowel-distance\n  notes: With row z-scoring, consonant-vowel distances exceed consonant-consonant ones, which exceed\n    vowel-vowel ones, with corrected p < 1e-10 under every other reading; with time z-scoring the\n    consonant-vowel distances are shorter than the consonant-consonant ones. The pairs number 4677\n    (every CV) or 4567 (15+ CVs), not 4623, so row readings give partially reproduced and time\n    readings not reproduced.\n- claim: suppfig9-pc-articulator-weights\n  outcome: not_reproduced\n  notebook: reproduce_bouchard_2013.ipynb\n  output: claim:suppfig9-pc-articulator-weights\n  measured: 268\n  notes: Under all 96 readings the condition fails in all three PCs; tongue weights are not larger\n    than lips weights. In the reading printed in full (268 vSMC electrodes) lips minus tongue has a\n    median paired difference of +0.03 in log10 (corrected p = 1), and jaw and larynx differ\n    (corrected p = 5e-11). By Methods Eq. 6 the PC term cancels in paired comparisons of one\n    electrode's articulators, so the three PCs give the same tests.\n  deviations:\n  - Uses the GLM weights of fig2a-lips-dorsal, which is blocked for its spatial judgement only.\nfindings:\n- kind: metadata_insufficient\n  statement: No electrode has a position relative to the central sulcus or the Sylvian fissure, the\n    frame of the paper's spatial analyses. EC2 and GP31 have x, y, z coordinates with no unit or\n    coordinate frame described; GP33 and EC9 have none. No electrode is labelled as on the guenon.\n    Seven spatial findings of the paper cannot be tested.\n- kind: data_missing\n  statement: The microphone recordings were removed (dandiset description), so the acoustic onset,\n    peak and offset of each syllable used by the paper cannot be computed; only hand-marked start,\n    C-V transition and stop times are given.\n- kind: identifier_missing\n  statement: Subjects GP31 and GP33 do not carry the paper's names (EC31, EC33), and nothing links\n    them. GP31's coordinates fit a left hemisphere, as the paper's EC31; GP33 has no coordinates, so\n    the right hemisphere of EC33 cannot be checked.\n- kind: other\n  statement: The dandiset holds a fourth subject, EC9 (7 blocks, 1653 trials), that is not in the\n    paper. It has extra syllables (/ch/, /dh/, /j/, /sk/), labels on 79 of 256 electrodes and no\n    coordinates.\n- kind: selection_undocumented\n  statement: Renditions per syllable range from 2 to 107 (GP31 /thi/ 2, EC2 /thi/ 10, GP31 up to 107)\n    against the paper's 15 to 100, and GP31 lacks /tha/ and /thu/. The three subjects have 169\n    distinct syllables against the paper's 168 (57 + 57 + 54). The dandiset does not say which\n    trials or syllables the paper used.\n- kind: metadata_error\n  statement: The raw ElectricalSeries gives unit volt with a conversion factor of 0.001, but the\n    stored values have an SD of a few 1e-5, which is a usual ECoG amplitude if read as volts and tens\n    of nanovolts with the factor; the data are consistent with values already in volts.\n- kind: metadata_error\n  statement: Two syllable labels are misspelt (`she` for `shee` in EC2 and EC9, `ha` for `haa` in\n    GP33 and EC9). Electrode ids start at 0 in EC2 and GP31 and at 1 in GP33 and EC9.\n- kind: other\n  statement: The archive summary counts four subjects and 31 files; bad-channel flags differ between\n    blocks of one subject (EC2 has none in two blocks and up to 10 in others), and 177 of 9370\n    analysed trials overlap intervals marked as ECoG artefacts.\n"
}
```

```
File created successfully at: attempts/000019-bouchard-2013-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
sed -i 's/2026-10-22/2026-10-21/g' questions/000019.yaml; python - <<'EOF'
import nbformat,re
nb=nbformat.read('executed/000019-bouchard-2013/reproduce_bouchard_2013.ipynb',4)
def out(tag):
    for c in nb.cells:
        if tag in c.metadata.get('tags',[]): return ''.join(o.get('text','') for o in c.outputs if 'text' in o)
o=out('claim:suppfig6-mixed-tuning')
import collections
r=collections.defaultdict(list); n=[]
for l in o.splitlines():
    m=re.findall(r'n=(\d+) (\d+)/(\d+)/(\d+)/(\d+)',l)
    for k,mm in enumerate(m): r[k].append(int(mm[1+k]))
    t=l.split()
    if len(t)>6 and t[0] in('pre','whole'):
        nums=[x for x in t if x.isdigit()]; n.append(int(nums[0]) if nums else None)
print({k:(min(v),max(v)) for k,v in r.items()}, min(n),max(n))
o=out('claim:fig5d-separability-coupling')
v=[]
for l in o.splitlines():
    if 'matching' in l and 'kmeans' not in l:
        v+= [float(x) for x in re.search(r'matching set\s+([\d. ]+?)\s+\d\.\d+e',l).group(1).split()]
print('fig5d R2', min(v), max(v))
o=out('claim:suppfig9-pc-articulator-weights'); print(o.splitlines()[-5:-3])
EOF
```

```
Exit code 1
{0: (63, 79), 1: (53, 96), 2: (59, 84), 3: (72, 84)} 53 117
Traceback (most recent call last):
  File "<stdin>", line 20, in <module>
AttributeError: 'NoneType' object has no attribute 'group'
```

**Agent calls Bash**

```bash
python - <<'EOF'
import nbformat,re
nb=nbformat.read('executed/000019-bouchard-2013/reproduce_bouchard_2013.ipynb',4)
def out(tag):
    for c in nb.cells:
        if tag in c.metadata.get('tags',[]): return ''.join(o.get('text','') for o in c.outputs if 'text' in o)
o=out('claim:fig5d-separability-coupling'); v=[]
for l in o.splitlines():
    if 'matching' in l and 'kmeans' not in l:
        t=l.split('matching set')[1].split(); v+=[float(x) for x in t[:6]]
print('fig5d R2', min(v), max(v), len(v)/6)
o=out('claim:suppfig9-pc-articulator-weights'); print([l for l in o.splitlines() if 'Outcome' in l])
print(o.count('not reproduced'))
EOF
```

```
fig5d R2 0.0 8.0 33.333333333333336
['Outcome over readings: not reproduced']
193
```

**Agent calls Bash**

```bash
python - <<'EOF'
import nbformat
nb=nbformat.read('executed/000019-bouchard-2013/reproduce_bouchard_2013.ipynb',4)
def out(tag):
    for c in nb.cells:
        if tag in c.metadata.get('tags',[]): return ''.join(o.get('text','') for o in c.outputs if 'text' in o)
o=out('claim:fig5d-separability-coupling'); v=[];n=0
for l in o.splitlines():
    if l.strip().split()[:1] and l.split()[0] in('pre','whole') and 'matching' in l and 'kmeans' not in l:
        n+=1; v+=[float(x) for x in l.split('matching set')[1].split()[:6]]
print('fig5d R2', min(v), max(v), n)
o=out('claim:suppfig9-pc-articulator-weights'); print(sum(1 for l in o.splitlines() if l.split()[:1] and l.split()[0] in ('pre','whole')))
EOF
```

```
fig5d R2 0.4 0.98 32
192
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='attempts/000019-bouchard-2013-01.yaml'; s=open(p).read()
for a,b in [('(lips about 63 to 77%,\n    tongue 53 to 96%, larynx 61 to 84%, jaw 72 to 84%)','(lips 63 to 79%, tongue\n    53 to 96%, larynx 59 to 84%, jaw 72 to 84%)'),
            ('Groups hold\n    53 to 110 electrodes over the three subjects.','The GLM\n    electrodes number 53 to 117 over the three subjects.'),
            ('Under all 96 readings','Under all 192 readings')]:
    assert a in s,a; s=s.replace(a,b)
open(p,'w').write(s)
p='/tmp/claude-1001/nb.py'; s=open(p).read()
a='''# mean share of positive weight (Lips about 63 to 77%, Tongue 53 to 96%, Larynx 61 to 84%, Jaw 72 to
# 84%), and the other articulators keep a non-zero share (table).'''
b='''# mean share of positive weight (Lips 63 to 79%, Tongue 53 to 96%, Larynx 59 to 84%, Jaw 72 to
# 84%), and the other articulators keep a non-zero share (table).'''
assert a in s; s=s.replace(a,b); open(p,'w').write(s)
EOF
cd /tmp/claude-1001 && python conv.py nb.py entries/000019-bouchard-2013/reproduce_bouchard_2013.ipynb && cd - >/dev/null && python tools/entry.py check entries/000019-bouchard-2013 | tail -3
```

```
0 error(s)
```

**Agent calls Bash**

```bash
for f in attempts/000019-bouchard-2013-01.yaml questions/000019.yaml entries/000019-bouchard-2013/entry.yaml; do python -c "import yaml,sys;yaml.safe_load(open('$f'))" && echo "$f ok"; grep -nE "^\s+[^:]*:\s.*: " $f | grep -v "^\s*-\s*claim" | head; grep -nE "^\s{3,}[^-a-z].*: |^\s{4,}[a-z].*[a-z]: " $f | head; done; grep -n "—\|rather\|\*\*" attempts/000019-bouchard-2013-01.yaml questions/000019.yaml entries/000019-bouchard-2013/README.md | grep -v "Result" | head
```

```
attempts/000019-bouchard-2013-01.yaml ok
14:    name: CatalystNeuro
16:    harness: Claude Code (GitHub Actions)
17:    model: claude-opus-5-5
18:    protocol: pilot-10
20:    platform: GitHub Actions
21:    url: https://github.com/catalystneuro/reproduction-registry/actions/runs/39692741052
questions/000019.yaml ok
entries/000019-bouchard-2013/entry.yaml ok
```

**Agent calls Bash**

```bash
grep -n "—\|rather" /tmp/claude-1001/nb.py entries/000019-bouchard-2013/bouchard.py; grep -n "\*\*" /tmp/claude-1001/nb.py | grep -v "Result:" | head
```

```
4:# **Paper.** Bouchard KE, Mesgarani N, Johnson K, Chang EF (2013). Functional organization of
10:# **Dandiset.** [DANDI:000019](https://dandiarchive.org/dandiset/000019/0.220126.2148),
15:# **What the dandiset holds.** Raw ECoG (256 channels, 3051.76 Hz) of 31 recording blocks from four
23:# **Readings.** Where the claims file leaves a method detail open it names readings, and every
503:               **{f"{s} lips+ / hits / max /ju/": f"{hits[s][0]} / {hits[s][1]} / {hits[s][2]:.2f}" for s in B.SUBJECTS},
597:               "no positive weight": int((~has).sum()), **groups, "holds": ok})
652:                           "n": len(t), **{f"n {a[:6]}": int((t.articulator == a).sum()) for a in ART6},
653:                           "F": round(F, 1), "p": p, **{f"onset {a[:6]}": round(mo.get(a, np.nan)) for a in ART6},
704:                           **{s: round(fr[s][:9].sum(), 3) for s in B.SUBJECTS},
1054:                    vals.append((res.statistic ** 2, res.pvalue, res.statistic))
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001 && python - <<'EOF'
import re
s=open('nb.py').read()
s2=re.sub(r'^# \*\*(?!Result)([^*]+?)\*\*', r'# \1', s, flags=re.M)
print([l for l in s2.splitlines() if '**' in l and l.startswith('#') and 'Result' not in l])
open('nb.py','w').write(s2)
EOF
python conv.py nb.py entries/000019-bouchard-2013/reproduce_bouchard_2013.ipynb; grep -c "Result:" nb.py
```

```
[]
15
Shell cwd was reset to
```

**Agent calls Bash**

```bash
time python tools/entry.py all entries/000019-bouchard-2013 2>&1 | tail -4
```

```
Installed kernelspec registry-000019-bouchard-2013 in executed/000019-bouchard-2013/.venv/share/jupyter/kernels/registry-000019-bouchard-2013
0 error(s)
pass  reproduce_bouchard_2013.ipynb  (879 s)

real	14m56.568s
user	24m35.290s
sys	3m46.222s
```

**Agent calls Bash**

```bash
python - <<'EOF'
import nbformat
nb=nbformat.read('executed/000019-bouchard-2013/reproduce_bouchard_2013.ipynb',4)
keys=['Outcome over','Largest','Ranges over','ANOVA F','Phonetic-group','k-means readings','notebook ran','median SD of the stored','Pairs sharing','  (']
for c in nb.cells:
    if c.cell_type!='code': continue
    for o in c.get('outputs',[]):
        if o.get('output_type')=='error': print('ERROR',o['ename'])
        for l in o.get('text','').splitlines():
            if any(l.startswith(k) or k in l[:30] for k in keys[:-1]): print(l[:250])
EOF
python tools/entry.py handover entries/000019-bouchard-2013 | tail -3; ls executed/000019-bouchard-2013/handover; git status --short
```

```
Pairs sharing sample count, trial times or first 2000 samples of 4 channels:
Outcome over readings: not reproduced
Largest /ju/ z at +250 ms among lips-positive GLM electrodes, over all readings and subjects: 1.19
Outcome over readings: not reproduced
Outcome over readings: reproduced
Outcome over readings: not reproduced
Ranges over readings: mean onset Lips -270 to -54 | Tongue -26 to 220 | Jaw -270 to -116 | Larynx -111 to 112 | peak Back 235 to 301 | peak High 276 to 317
ANOVA F 9.9 to 39.2 | readings with p < 1e-10: 51 of 64 | conditions holding per reading: {0: 64}
Outcome over readings: differ by reading: not reproduced 7, reproduced 9
Outcome over readings: not reproduced
Outcome over readings: differ by reading: not reproduced 4, partially 12
Outcome over readings: differ by reading: not reproduced 12, partially 4
Outcome over readings (Euclidean; Hamming is a variant): differ by reading: partially 6, reproduced 2
Outcome over readings: not reproduced
Phonetic-group readings: consonant peak -145 to 10 | vowel peak 200 to 235 | consonant onset (a) -305.0 to -230.0 | (b) -285.0 to -180.0 | vowel onset (a) 60.0 to 100.0 | (b) 90.0 to 105.0
k-means readings: peak of the single curve -135 to 360
Outcome over readings: differ by reading: not reproduced 48, reproduced 32
Outcome over readings: differ by reading: not reproduced 8, partially 8
Outcome over readings: not reproduced
notebook ran in 14.5 min
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la .bash_profile .bashrc .gitconfig .profile .ripgreprc .zprofile .zshrc .mcp.json; ls -la .idea .vscode scripts | head
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 21 23:18 .bash_profile
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 21 23:18 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 21 23:18 .gitconfig
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 21 23:18 .mcp.json
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 21 23:18 .profile
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 21 23:18 .ripgreprc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 21 23:18 .zprofile
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 21 23:18 .zshrc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 21 23:18 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 21 23:18 .vscode
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 21 23:18 scripts
```

**Agent calls Bash**

```bash
ls -a entries/000019-bouchard-2013; rm -rf entries/000019-bouchard-2013/__pycache__; python tools/entry.py check entries/000019-bouchard-2013 | tail -1
```

```
.
..
.claude
README.md
__pycache__
bouchard.py
entry.yaml
reproduce_bouchard_2013.ipynb
requirements.in
requirements.lock.txt
0 error(s)
```

**Agent calls Bash**

```bash
ls -la entries/000019-bouchard-2013/.claude; find entries/000019-bouchard-2013/.claude | head
```

```
total 12
drwxr-xr-x 3 runner runner 4096 Oct 21 23:47 .
drwxr-xr-x 3 runner runner 4096 Oct 22 00:43 ..
drwx------ 2 runner runner 4096 Oct 21 23:47 .cc-writes
entries/000019-bouchard-2013/.claude
entries/000019-bouchard-2013/.claude/.cc-writes
```

**Agent calls Bash**

```bash
rmdir entries/000019-bouchard-2013/.claude/.cc-writes entries/000019-bouchard-2013/.claude 2>&1; ls -a entries/000019-bouchard-2013
```

```
Permission for this tool use was denied. It requires approval, and this session has no approval surface — nobody can answer a permission prompt here — so it was denied automatically. The action was NOT performed; do not claim it succeeded, and do not retry it: this action, and anything else that requires approval, will be denied the same way for the rest of this session. Tell the user what was blocked and why you needed it, then continue with the parts of the task that do not require approval. What required approval: Claude requested permissions to edit entries/000019-bouchard-2013/.claude/.cc-writes which is a sensitive file.
```

**Agent**

I did steps 1 to 5 of the Author section and ran the handover (step 6); `python tools/entry.py all` passes with 0 errors. Of the 22 claims, 1 is reproduced, 1 partially reproduced, 7 not reproduced and 13 blocked. The entry is `entries/000019-bouchard-2013/`, with `attempts/000019-bouchard-2013-01.yaml` and `questions/000019.yaml`; nothing is committed.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| data-composition | partially reproduced |
| active-electrodes | not reproduced (about 24 per subject, against 27 to 33) |
| fig1c-e-articulator-electrodes | blocked: metadata_insufficient (no subject has all six named electrodes on vSMC) |
| fig1f-h-phonetic-contrasts | not reproduced (largest /ju/ z is 1.19, below the threshold of 2) |
| fig2a, fig2b, suppfig3b, suppfig3d, suppfig3f, suppfig5, suppfig7 (spatial) | blocked: metadata_insufficient |
| suppfig6-mixed-tuning | reproduced |
| fig3d-timing-sequence | not reproduced (tongue correlations begin after the C-V transition) |
| pca-nine-components | blocked: methods_underspecified |
| fig4a-consonant-clusters | not reproduced |
| suppfig11-co-clustering | blocked: methods_underspecified |
| fig4c-d-hierarchy | blocked: methods_underspecified |
| fig4ef-feature-correlations | blocked: methods_underspecified |
| fig5c-separability-timing | not reproduced |
| fig5d-separability-coupling | blocked: methods_underspecified (the claims file's own readings disagree) |
| suppfig13-consonant-vowel-distance | blocked: methods_underspecified |
| suppfig9-pc-articulator-weights | not reproduced |

**2. The dataset and the questions asked**

- **Version:** I pinned 0.220126.2148, the only published version; the paper cites none.
- **What it holds:** raw 256-channel ECoG at 3051.76 Hz, trial tables with C-V transition times, bad-channel flags, anatomical labels and rest periods. There is no audio and no high gamma, so high gamma is computed from about 42 GB of raw data, streamed into memory.
- **Subjects:** four (EC2, EC9, GP31, GP33). I assumed GP31 and GP33 are the paper's EC31 and EC33; nothing in the files links them. EC9 is not in the paper and is left out.
- **Positions:** no electrode position relative to the central sulcus or Sylvian fissure. EC2 and GP31 have x, y, z coordinates with no unit or frame; GP33 has none. This blocks the seven spatial claims.
- **Syllable counts:** 2 to 107 renditions per syllable against the paper's 15 to 100, and 169 syllables against 168.
- **Units:** the conversion factor (0.001) looks wrong; the stored values look like volts already.
- **Labels and ids:** two syllable labels are misspelt, and electrode ids start at 0 in some subjects and at 1 in others.
- **Duplicates:** none found.

I asked five questions:
- How the state-space input is z-scored: over each electrode's whole series, or at each time across syllables.
- Whether syllables with fewer than 15 renditions are kept. Together with the z-scoring question, this decides most of the methods_underspecified outcomes.
- Whether the hand-marked syllable start can stand in for the acoustic onset, since the audio is missing.
- Whether the dataset's rest period counts as a baseline.
- Whether the paper gives any way to get the spatial coordinates it uses.

**3. Where the protocol was unclear, wrong or missing something**

1. A claim depending on a blocked claim is blocked, but fig1f-h, suppfig6 and suppfig9 only use fig2a's weights, which need no positions. I tested them and recorded why.
2. Readings I add through a question multiply every other reading. I ran all of them, so several claims are blocked only because those readings disagree.
3. Rest period as baseline: it comes from the dataset, not the paper's text, so I showed it as a variant, not a reading.
4. The protocol's notebook header template uses bold labels, which conflicts with your no-bold rule. I removed the bold.
5. The archives doc says to stream with remfile, which reads these files chunk by chunk too slowly. I fetched each whole file into memory with parallel range requests; nothing was written to disk.
6. The articulator and phonetic feature matrices exist only as figures in the supplement. I transcribed them from the PDF into the helper module and listed them under `inputs`.
7. The protocol has no format for a claims file that leaves "pre-epoch level" undefined (fig5c). I read it as the value at -500 ms and recorded that as a deviation.

**4. Runtime and failures**

- The notebook runs in about 14.5 minutes, 11 of them streaming and computing high gamma. That is over the 10-minute aim and under the 30-minute limit.
- I could not remove an empty `.claude/.cc-writes` directory the harness created inside the entry: the permission was denied. Git does not track empty directories, so it will not be committed.
- The `.bashrc`-style entries in `git status` are sandbox device mounts, not files.

## End of run

104 turns, 81 minutes, result: success.
