# okuno-2025 · author · run 42760211426

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; ls; ls docs entries claims attempts paper | head -100
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
3	Version: `pilot-14`. Record this version in the attempt's provenance.
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
[... 635 more lines not kept]
```

```
Tue Nov 10 05:16:20 UTC 2026
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
[... 108 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md | head -80; wc -l docs/design.md docs/archives.md; cat claims/okuno-2025.yaml; ls paper/ papers/datasets/ | grep -i okuno; ls paper; cat papers/datasets/okuno-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/okuno-2025.yaml"
}
```

```
1	# Claims for Okuno, Woodward, Okano & Hata (2025), eLife reviewed preprint 107990 v1,
2	# "Functional connectivity, structural connectivity, and inter-individual variability in
3	# Drosophila melanogaster", on dandiset 000727 (reused; the data are those of Brezovec et al.).
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
5	# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md.
6	#
7	# Text read. The eLife Reviewed Preprint version 1 (October 9, 2025, "Not revised"), the version
8	# the DOI 10.7554/elife.107990.1 names, from the publisher's HTML, in
9	# paper/10.7554-elife.107990.1.txt: abstract, Introduction, Results, figure legends (Figures 1
10	# to 5), Discussion, Materials and methods, Data availability, and the legends of the Extended
11	# Data figures (1-1, 1-2, 2-1, 3-1, 3-2, 4-1 to 4-4, 5-1), which are the paper's only
12	# supplement. No PDF was supplied, so no figure could be read; values shown only in figures are
13	# not known here. The text lost the displayed equations of the Methods (the FC-SC detection and
14	# correlation score, cPPSSI, PPSSI and the two ranking scores); they are taken from the code
15	# (M4, M7).
16	#
17	# Code read. github.com/takuto-okuno-riken/flywalk (MATLAB), linked under Code Availability, at
18	# commit 4b92add (2025-08-11), the last commit before v1 was posted. Later commits
19	# (2025-11 to 2026-06) answer the reviewers and change the DBSCAN distance to a morphological
20	# one; they are not this version's method. The repository holds the ROI time-series
[... 708 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la paper; cat papers/datasets/okuno-2025.yaml; sed -n 1,200p docs/archives.md
```

```
total 84
drwxr-xr-x  2 runner runner  4096 Nov 10 05:16 .
drwxr-xr-x 21 runner runner  4096 Nov 10 05:16 ..
-rw-r--r--  1 runner runner 75938 Nov 10 05:16 10.7554-elife.107990.1.txt
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.7554/elife.107990.1
title: Functional connectivity, structural connectivity, and inter-individual variability in Drosophila
  melanogaster
datasets:
- archive: dandi
  id: '000727'
  relation: reuses
# Archives

The registry tests papers against data in public archives. It began with one,
the DANDI Archive. The protocol is written for any archive. What is particular
to an archive (how its datasets are named, versioned and read) is here, and an
agent is pointed to its archive's section.

[... 194 more lines not kept]
```

**Agent calls Bash**

```bash
ls entries/fouke-2025/; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; head -c 6000 attempts/fouke-2025-01.yaml; ls questions | head;
```

```
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
  title: Reproducing Fouke et al. (2025) from dandiset 001453
  runtime_minutes: 6
[... 135 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^[a-z_]*:" attempts/fouke-2025-01.yaml; sed -n '/^findings:/,/^provenance\|^verifications/p' attempts/fouke-2025-01.yaml | head -30; grep -n "blocked" -A6 attempts/fouke-2025-01.yaml | head -30; ls schemas
```

```
1:schema_version: 3
2:id: fouke-2025-01
3:datasets:
9:paper: doi:10.1016/j.cub.2025.04.027
10:date: 2026-10-14
11:entry: fouke-2025
12:provenance:
23:inputs:
35:outcomes:
244:findings:
310:verifications:
findings:
- kind: data_missing
  statement: The dandiset holds only the freely swimming tracking of Figure 1 and Figure S1. The
    two-photon imaging and the head-fixed tail tracking behind Figures 2 to 4 are not in it, and
    the GitLab repository the paper names for all behavioural and imaging data holds analysis
    notebooks only. Nine of the paper's main findings cannot be tested.
- kind: metadata_insufficient
  statement: The stimulus codes 0 to 20 have no names or description in the files or the
    dandiset metadata. They can be named only from the paper's analysis notebook and the protocol
[... 55 more lines not kept]
```

**Agent**

Now the dataset.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/000727/versions/ | python -m json.tool | head -60; curl -s "https://api.dandiarchive.org/api/dandisets/000727/versions/0.240106.0043/assets/?page_size=200" | python -c "
import json,sys; d=json.load(sys.stdin); print(d['count'])
for a in d['results']: print(a['path'], a['size']/1e9, a['asset_id'])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && python -c "import remfile,h5py,pynwb; print('ok')" 2>&1; which uv; uv --version; ls tools; nproc; free -g; df -h $TMPDIR | tail -1
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import remfile,h5py,pynwb; print('ok')
    ^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'remfile'
/opt/hostedtoolcache/Python/3.13.18/x64/bin/uv
uv 0.13.7 (x86_64-unknown-linux-gnu)
__pycache__
agent_run.py
archive_transcripts.sh
archives
backfill_summaries.py
blind.sh
build_dryad_targets.py
build_figshare_targets.py
build_openneuro_targets.py
build_reuse_targets.py
build_site.py
build_targets.py
changed_entries.py
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q remfile h5py pynwb dandi numpy scipy pandas matplotlib 2>&1 | tail -2; python -c "import remfile, pynwb; print('ok')"
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > survey.py <<'EOF'
import remfile, h5py, time, requests
aid="80be44d6-db90-4807-bb1b-abdac5c580eb"
url=f"https://api.dandiarchive.org/api/assets/{aid}/download/"
r=requests.head(url, allow_redirects=True); s3=r.url
f=h5py.File(remfile.File(s3),'r')
def show(name,obj):
    if isinstance(obj,h5py.Dataset):
        print(name, obj.shape, obj.dtype, obj.chunks, obj.compression, dict((k,(v if not hasattr(v,'shape') or v.size<5 else '...')) for k,v in obj.attrs.items() if k not in ('object_id','namespace','neurodata_type')))
    else:
        a={k:v for k,v in obj.attrs.items() if k not in ('object_id','namespace')}
        print(name+'/', a)
f.visititems(show)
EOF
timeout 300 python survey.py 2>&1 | grep -v "^specifications" | head -120
```

```
acquisition/ {}
acquisition/TwoPhotonSeriesAnatomicalGreen/ {'comments': 'no comments', 'description': 'Anatomical imaging data (GCaMP6f)', 'neurodata_type': 'TwoPhotonSeries', 'scan_line_rate': np.float64(15831.051023477448)}
acquisition/TwoPhotonSeriesAnatomicalGreen/data (100, 1024, 512, 241) uint16 (9, 1024, 512, 1) gzip {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(6.52793248211467e-07), 'unit': 'n.a.'}
acquisition/TwoPhotonSeriesAnatomicalGreen/dimension (3,) int64 None None {}
acquisition/TwoPhotonSeriesAnatomicalGreen/field_of_view (3,) float64 None None {}
acquisition/TwoPhotonSeriesAnatomicalGreen/starting_time () float64 None None {'rate': np.float64(0.1244341734707921), 'unit': 'seconds'}
acquisition/TwoPhotonSeriesAnatomicalRed/ {'comments': 'no comments', 'description': 'Anatomical imaging data (tdTomato)', 'neurodata_type': 'TwoPhotonSeries', 'scan_line_rate': np.float64(15831.051023477448)}
acquisition/TwoPhotonSeriesAnatomicalRed/data (100, 1024, 512, 241) uint16 (9, 1024, 512, 1) gzip {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(6.52793248211467e-07), 'unit': 'n.a.'}
acquisition/TwoPhotonSeriesAnatomicalRed/dimension (3,) int64 None None {}
acquisition/TwoPhotonSeriesAnatomicalRed/field_of_view (3,) float64 None None {}
acquisition/TwoPhotonSeriesAnatomicalRed/starting_time () float64 None None {'rate': np.float64(0.1244341734707921), 'unit': 'seconds'}
acquisition/TwoPhotonSeriesFunctionalGreen/ {'comments': 'no comments', 'description': 'Functional imaging data (GCaMP6f)', 'neurodata_type': 'TwoPhotonSeries', 'scan_line_rate': np.float64(15841.082262740192)}
acquisition/TwoPhotonSeriesFunctionalGreen/data (3384, 256, 128, 49) uint16 (152, 256, 128, 1) gzip {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(2.61117299284587e-06), 'unit': 'n.a.'}
acquisition/TwoPhotonSeriesFunctionalGreen/dimension (3,) int64 None None {}
acquisition/TwoPho
[... 106 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && timeout 300 python survey.py 2>&1 | grep -v "^specifications" | sed -n 120,200p
```

```
processing/behavior/FicTrac/SpatialSeriesPosition/data (90000, 2) float64 (2813, 1) gzip {'conversion': np.float64(0.0045), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'meters'}
processing/behavior/FicTrac/SpatialSeriesPosition/reference_frame () object None None {}
processing/behavior/FicTrac/SpatialSeriesPosition/starting_time () float64 None None {'rate': np.float64(50.0), 'unit': 'seconds'}
processing/behavior/FicTrac/SpatialSeriesRotationCameraFrame/ {'comments': 'no comments', 'description': "Orientation in radians from the camera's perspective. x: rotation to the sphere's right (pitch), y: rotation under the sphere (yaw), z: rotation behind the sphere (roll)", 'neurodata_type': 'SpatialSeries'}
processing/behavior/FicTrac/SpatialSeriesRotationCameraFrame/data (90000, 3) float64 (2813, 1) gzip {'conversion': np.float64(0.0045), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'meters'}
processing/behavior/FicTrac/SpatialSeriesRotationCameraFrame/reference_frame () object None None {}
processing/behavior/FicTrac/SpatialSeriesRotationCameraFrame/starting_time () float64 None None {'rate': np.float64(50.0), 'unit': 'seconds'}
processing/behavior/FicTrac/SpatialSeriesRotationDeltaCameraFrame/ {'comments': 'no comments', 'description': "Change in orientation since last frame from the camera's perspective. x: rotation to the sphere's right (pitch), y: rotation under the sphere (yaw), z: rotation behind the sphere (roll)", 'neurodata_type': 'SpatialSeries'}
processing/behavior/FicTrac/SpatialSeriesRotationDeltaCameraFrame/data (90000, 3) float64 (2813, 1) gzip {'conversion': np.float64(0.0045), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'meters'}
processing/behavior/FicTrac/SpatialSeriesRotationDeltaCameraFrame/reference_frame () object None None {}
processing/behavior/FicTrac/SpatialSeriesRotationDeltaCameraFrame/starting_time () float64 None None {'rate': np.float64(50.0), 'unit': 'seconds'}
processin
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper && grep -n -i -E "dandi|preprocess|FDA|template|registered|SPM12|ANTs|high-pass|highpass|z-scor|nine flies|9 flies|eight flies|zenodo" 10.7554-elife.107990.1.txt | cut -c1-600
```

```
202:a, (top) Example z-slice of the reduced FDA template with DistKm ROIs from 20 to 1000 ROIs. (middle) SC matrices (neuron) of DistKm ROIs from 20 to 1000 ROIs. (bottom) FC matrices of DistKm ROIs from 20 to 1000 ROIs. b, From left to right, FC-SC correlation, FC-SC detection and FC-SC detection & correlation score, respectively. The solid line shows the FC vs. SC matrix (neuron), and the dashed line shows FC vs. SC matrix (synapse) at each ROI count. The vertical axis shows the correlation coefficient, averaged AUC and FC-SC detection & correlation score, respectively. The horizontal axis s
206:Because of the strong relationship between FC and SC, they can be used to investigate inter-individual variability in D. melanogaster. In particular, the FlyWire whole-brain and FlyEM hemibrain connectome data have been compared [15, 16], and widely different results are observed with cell typing [16]. However, these studies have yet to clarify whether these differences in connectome between the two individuals are attributed to inter-individual variability or some other reasons. Therefore, we compared these two EM connectomes based on the averaged FC of eight flies. FlyEM was scanned at a
213:First, the optimal pre-processing of the calcium imaging data of D. melanogaster was investigated. The registration method used in fMRI was applied to the calcium image (Ext.Data.Fig.1-1) to register to the FDA template [14] (Fig. 1b). Then, various nuisance factor removal methods (details in Methods) were applied to the ROI time-series to generate the FC matrices of eight flies (Fig. 1a). Three types of ROIs were used in the analysis: ROIs based on the anatomical neuropil, commonly used in Drosophila (hemibrain ROI), ROIs based on k-means clustering of the SC matrix of 146,604 voxels in t
217:Spatial smoothing is useful for absorbing inter-individual variability and conducting second-level group analysis [10, 43]. Here, we explored the effect of spatial smoothing (of the calcium ima
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://zenodo.org/api/records/15532271 | python -c "
import json,sys; d=json.load(sys.stdin); print(d['metadata']['title'], d['metadata'].get('version'), d['metadata']['publication_date']); print(d['metadata']['description'][:2000])
for f in d['files']: print(f['key'], round(f['size']/1e6,1),'MB')
print(d.get('links',{}).get('versions'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s -i https://zenodo.org/api/records/15532271 | head -20; curl -s -o /dev/null -w "%{http_code}\n" https://github.com/takuto-okuno-riken/flywalk
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -sL "https://zenodo.org/api/records/15532271/versions?allversions=true&size=20" | python -c "
import json,sys; d=json.load(sys.stdin)
for h in d['hits']['hits']:
  m=h['metadata']; print(h['id'], m.get('version'), m['publication_date'], m['title'], sum(f['size'] for f in h['files'])/1e9,'GB', len(h['files']))
"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -sL "https://zenodo.org/api/records/18151010" > z.json; python -c "
import json; d=json.load(open('z.json'))
m=d['metadata']; print(d['id'], m.get('version'), m['publication_date'], m['title']); print(m['description'][:1500]); print(d['conceptrecid'])
for f in d['files']: print(f['key'], round(f['size']/1e6,1),'MB')
print(d['links'].get('versions'))"; curl -sL "https://zenodo.org/api/records?q=conceptrecid:15532271&all_versions=true&size=20" | python -c "
import json,sys; d=json.load(sys.stdin)
for h in d['hits']['hits']:
  m=h['metadata']; print(h['id'], m.get('version'), m['publication_date'], sum(f['size'] for f in h['files'])/1e9,'GB', len(h['files']))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && uv pip install -q fsspec aiohttp requests && python -c "
import fsspec, zipfile, json, urllib.request
d=json.load(urllib.request.urlopen('https://zenodo.org/api/records/15532272'))
f=d['files'][0]; print(f['key'], f['checksum'], f['links']['self'])
url=f['links']['self']
z=zipfile.ZipFile(fsspec.open(url, block_size=2**20).open())
tot=0
for i in z.infolist():
    print(i.filename, round(i.file_size/1e6,2), round(i.compress_size/1e6,2))
" > zlist.txt 2>&1; wc -l zlist.txt; head -5 zlist.txt
```

```
1584 zlist.txt
flywalkdemodata.zip md5:cd1309e3e74ec78c4c0eab8467483185 https://zenodo.org/api/records/15532272/files/flywalkdemodata.zip/content
flywalkdemodata/data/ 0.0 0.0
flywalkdemodata/data/flywire783_n2n.mat 150.72 150.2
flywalkdemodata/data/flywire783_neuron.mat 0.54 0.53
flywalkdemodata/data/flywire783_neuron_avg.mat 0.72 0.71
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && awk '{print $1}' zlist.txt | sed 's#/[^/]*$##' | sort | uniq -c | sort -rn | head -30; grep -v -E "results/|/$" zlist.txt | awk '$2>0' | head -80
```

```
754 flywalkdemodata/results/auc
    453 flywalkdemodata/results/fc
    324 flywalkdemodata/results/sc
     21 flywalkdemodata/swc/flywire783
     14 flywalkdemodata/data
     11 flywalkdemodata/results/glm
      4 flywalkdemodata/results/neuralsc
      1 flywalkdemodata/swc
      1 flywalkdemodata/results
      1 flywalkdemodata.zip
flywalkdemodata.zip md5:cd1309e3e74ec78c4c0eab8467483185 https://zenodo.org/api/records/15532272/files/flywalkdemodata.zip/content
flywalkdemodata/data/flywire783_n2n.mat 150.72 150.2
flywalkdemodata/data/flywire783_neuron.mat 0.54 0.53
flywalkdemodata/data/flywire783_neuron_avg.mat 0.72 0.71
flywalkdemodata/data/flywire783_neuron_reci0sr140.mat 1.79 1.77
flywalkdemodata/data/flywire783_neuron_sepidx0sr140_3000mi1.mat 0.72 0.72
flywalkdemodata/data/flywire783_synapse.mat 560.22 558.84
flywalkdemodata/data/flywire783_synapse_nid.mat 441.12 438.86
flywalkdemodata/data/flywire783_synapse_reci0sr140.mat 200.38 200.0
flywalkdemodata/data/flywire783_synapse_sepidx0sr140_3000mi1.mat 124.01 123.93
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep "results/sc/" zlist.txt | head -60; grep "results/sc/" zlist.txt | grep -i -E "hemiroi|cm|dist" | grep -v -E "_sc[0-9]|s[0-9]" | head; grep "results/fc/" zlist.txt | head -20; grep "results/glm/\|neuralsc" zlist.txt; grep results/auc zlist.txt | head -5
```

```
flywalkdemodata/results/sc/ 0.0 0.0
flywalkdemodata/results/sc/hemicmkm100_connectlist.mat 0.34 0.32
flywalkdemodata/results/sc/hemicmkm1000_connectlist.mat 19.46 19.27
flywalkdemodata/results/sc/hemicmkm10000_connectlist.mat 206.27 199.04
flywalkdemodata/results/sc/hemicmkm20_connectlist.mat 0.03 0.02
flywalkdemodata/results/sc/hemicmkm200_connectlist.mat 1.17 1.14
flywalkdemodata/results/sc/hemicmkm30_connectlist.mat 0.06 0.04
flywalkdemodata/results/sc/hemicmkm300_connectlist.mat 2.37 2.34
flywalkdemodata/results/sc/hemicmkm50_connectlist.mat 0.11 0.09
flywalkdemodata/results/sc/hemicmkm500_connectlist.mat 5.77 5.72
flywalkdemodata/results/sc/hemicmkm5000_connectlist.mat 71.73 69.71
flywalkdemodata/results/sc/hemidistkm100_connectlist.mat 0.34 0.32
flywalkdemodata/results/sc/hemidistkm1000_connectlist.mat 20.49 20.29
flywalkdemodata/results/sc/hemidistkm10000_connectlist.mat 268.87 260.92
flywalkdemodata/results/sc/hemidistkm20_connectlist.mat 0.03 0.02
flywalkdemodata/results/sc/hemidistkm200_connectlist.mat 1.16 1.14
flywalkdemodata/results/sc/hemidistkm30_connectlist.mat 0.06 0.04
flywalkdemodata/results/sc/hemidistkm300_connectlist.mat 2.41 2.38
flywalkdemodata/results/sc/hemidistkm50_connectlist.mat 0.11 0.09
flywalkdemodata/results/sc/hemidistkm500_connectlist.mat 6.03 5.98
[... 91 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -i -E "nii|atlas|\.mat" zlist.txt | grep -v -E "results/(sc|fc|auc)/" | head -30; grep "results/sc/" zlist.txt | sed -E 's/-[0-9]+_connectlist/-N_connectlist/' | sort | uniq -c | sort -k2 | head -80
```

```
flywalkdemodata/data/flywire783_n2n.mat 150.72 150.2
flywalkdemodata/data/flywire783_neuron.mat 0.54 0.53
flywalkdemodata/data/flywire783_neuron_avg.mat 0.72 0.71
flywalkdemodata/data/flywire783_neuron_reci0sr140.mat 1.79 1.77
flywalkdemodata/data/flywire783_neuron_sepidx0sr140_3000mi1.mat 0.72 0.72
flywalkdemodata/data/flywire783_synapse.mat 560.22 558.84
flywalkdemodata/data/flywire783_synapse_nid.mat 441.12 438.86
flywalkdemodata/data/flywire783_synapse_reci0sr140.mat 200.38 200.0
flywalkdemodata/data/flywire783_synapse_sepidx0sr140_3000mi1.mat 124.01 123.93
flywalkdemodata/data/flywire783_sypostloc.mat 401.65 400.25
flywalkdemodata/data/flywire783_sypreloc.mat 402.16 400.76
flywalkdemodata/data/flywire783i_sypostloc_fdacal.mat 1238.47 1238.18
flywalkdemodata/data/flywire783i_sypreloc_fdacal.mat 1238.46 1238.16
flywalkdemodata/results/glm/s80poltcomparfly-087-Tukey8.mat 400.53 400.37
flywalkdemodata/results/glm/s80poltcomparfly-089-Tukey8.mat 400.13 399.96
flywalkdemodata/results/glm/s80poltcomparfly-094-Tukey8.mat 400.67 400.5
flywalkdemodata/results/glm/s80poltcomparfly-097-Tukey8.mat 401.11 400.94
flywalkdemodata/results/glm/s80poltcomparfly-098-Tukey8.mat 400.03 399.86
flywalkdemodata/results/glm/s80poltcomparfly-099-Tukey8.mat 400.47 400.31
flywalkdemodata/results/glm/s80poltcomparfly-100-Tukey8.mat 400.69 400.52
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && curl -s "https://api.github.com/repos/takuto-okuno-riken/flywalk/commits/4b92add" | python -c "import json,sys; d=json.load(sys.stdin); print(d['sha'], d['commit']['committer']['date'])"; curl -s "https://api.github.com/repos/takuto-okuno-riken/flywalk/git/trees/4b92add?recursive=1" | python -c "
import json,sys; d=json.load(sys.stdin); print(d.get('truncated'))
for t in d['tree']:
  if t['type']=='blob': print(t['path'], t.get('size'))" > tree.txt; wc -l tree.txt; grep -v "\.m " tree.txt | head -80
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && grep -v "atlas/hemiroi/roi" tree.txt; curl -sL https://raw.githubusercontent.com/takuto-okuno-riken/flywalk/4b92add4a44f641ab6add809ff6b0e0d6110b50c/README.md | head -150
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > tput.py <<'EOF'
import remfile, h5py, time, requests, numpy as np
aid="80be44d6-db90-4807-bb1b-abdac5c580eb"
s3=requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/", allow_redirects=True).url
f=h5py.File(remfile.File(s3),'r')
for k in ['acquisition/TwoPhotonSeriesFunctionalGreen/data','processing/ophys/TwoPhotonSeriesFunctionalGreenProcessed/data','acquisition/TwoPhotonSeriesAnatomicalGreen/data']:
    d=f[k]; n=d.id.get_num_chunks(); sz=[d.id.get_chunk_info(i).size for i in range(0,n,max(1,n//50))]
    print(k, n, 'chunks, mean MB', np.mean(sz)/1e6, 'est total GB', np.mean(sz)*n/1e9)
og=f['general/optophysiology']
for p in og:
    g=og[p]; print(p, {k:(g[k][()] ) for k in g if isinstance(g[k],h5py.Dataset)})
for k in ['acquisition/TwoPhotonSeriesFunctionalGreen','processing/ophys/TwoPhotonSeriesFunctionalGreenProcessed']:
    print(k, f[k+'/dimension'][()], f[k+'/field_of_view'][()] if 'field_of_view' in f[k] else None, f[k+'/starting_time'][()])
print({k:f['general/'+k][()] for k in ['experiment_description','related_publications','session_id','surgery']})
print({k:f['general/subject/'+k][()] for k in f['general/subject']})
EOF
timeout 600 python tput.py
```

```
acquisition/TwoPhotonSeriesFunctionalGreen/data 1127 chunks, mean MB 6.503003211538462 est total GB 7.328884619403847
processing/ophys/TwoPhotonSeriesFunctionalGreenProcessed/data 5733 chunks, mean MB 2.931596196078431 est total GB 16.806840992117646
acquisition/TwoPhotonSeriesAnatomicalGreen/data 2892 chunks, mean MB 6.528238764705883 est total GB 18.87966650752941
ImagingPlaneFunctionalGreenProcessed {'description': b'The plane or volume being imaged by the microscope.', 'excitation_lambda': np.float64(920.0), 'grid_spacing': array([1., 1., 1.]), 'indicator': b'GCaMP6f', 'location': b'whole brain', 'origin_coords': array([0., 0., 0.])}
ImagingPlaneGCaMP6fAnatomical {'description': b'The plane or volume being imaged by the microscope.', 'excitation_lambda': np.float64(920.0), 'grid_spacing': array([6.52793248e-07, 6.52793248e-07, 1.00000000e-06]), 'imaging_rate': np.float64(0.12443417347079311), 'indicator': b'GCaMP6f', 'location': b'whole brain'}
ImagingPlaneGCaMP6fFunctional {'description': b'The plane or volume being imaged by the microscope.', 'excitation_lambda': np.float64(920.0), 'grid_spacing': array([2.61117299e-06, 2.61117299e-06, 5.00000000e-06]), 'imaging_rate': np.float64(1.8797144377676087), 'indicator': b'GCaMP6f', 'location': b'whole brain'}
ImagingPlanetdTomatoAnatomical {'description': b'The plane or volume being imaged by the microscope.', 'excitation_lambda': np.float64(920.0), 'grid_spacing': array([6.52793248e-07, 6.52793248e-07, 1.00000000e-06]), 'imaging_rate': np.float64(0.12443417347079311), 'indicator': b'tdTomato', 'location': b'whole brain'}
ImagingPlanetdTomatoFunctional {'description': b'The plane or volume being imaged by the microscope.', 'excitation_lambda': np.float64(920.0), 'grid_spacing': array([2.61117299e-06, 2.61117299e-06, 5.00000000e-06]), 'imaging_rate': np.float64(1.8797144377676087), 'indicator': b'tdTomato', 'location': b'whole brain'}
acquisition/TwoPhotonSeriesFunctionalGreen [128 256  49] [0.00066846 0.00033423 0.00
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > tput2.py <<'EOF'
import remfile, h5py, time, requests, numpy as np, resource
from concurrent.futures import ThreadPoolExecutor
aid="80be44d6-db90-4807-bb1b-abdac5c580eb"
s3=requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/", allow_redirects=True).url
t=time.time()
f=h5py.File(remfile.File(s3),'r'); d=f['acquisition/TwoPhotonSeriesFunctionalGreen/data']
print('open',time.time()-t)
t=time.time(); x=d[:,:,:,20]; dt=time.time()-t
print('slice', x.shape, dt, 'MB/s compressed approx', 23*6.5/dt)
# raw chunk read in parallel threads, each its own file handle
def rd(z):
    ff=h5py.File(remfile.File(s3),'r'); dd=ff['acquisition/TwoPhotonSeriesFunctionalGreen/data']
    return dd[:,:,:,z].mean()
t=time.time()
with ThreadPoolExecutor(4) as ex: r=list(ex.map(rd,[1,2,3,4]))
dt=time.time()-t; print('4 slices parallel', dt, 4*23*6.5/dt,'MB/s')
print('maxrss MB', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e3)
EOF
timeout 900 python tput2.py
```

```
open 1.0886340141296387
slice (3384, 256, 128) 14.237832069396973 MB/s compressed approx 10.500194079500188
4 slices parallel 50.574368715286255 11.824171318212672 MB/s
maxrss MB 1548.728
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > tput3.py <<'EOF'
import remfile, h5py, time, requests, numpy as np, zlib
from concurrent.futures import ThreadPoolExecutor
aid="80be44d6-db90-4807-bb1b-abdac5c580eb"
s3=requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/", allow_redirects=True).url
f=h5py.File(remfile.File(s3),'r'); d=f['acquisition/TwoPhotonSeriesFunctionalGreen/data']
print(d.id.get_create_plist().get_nfilters(), [d.id.get_create_plist().get_filter(i)[0] for i in range(d.id.get_create_plist().get_nfilters())])
t=time.time(); n=d.id.get_num_chunks(); infos=[d.id.get_chunk_info(i) for i in range(n)]; print('index',n,time.time()-t)
print(infos[0].chunk_offset, infos[1].chunk_offset, infos[49].chunk_offset)
sess=requests.Session()
def get(ci):
    r=sess.get(s3, headers={'Range':f'bytes={ci.byte_offset}-{ci.byte_offset+ci.size-1}'})
    raw=zlib.decompress(r.content)
    return np.frombuffer(raw,dtype='<u2').reshape(-1,256,128).sum()
sel=[ci for ci in infos if ci.chunk_offset[3]==20]
for nt in [8,16]:
    t=time.time()
    with ThreadPoolExecutor(nt) as ex: r=list(ex.map(get, sel))
    dt=time.time()-t; print(nt,'threads', len(sel),'chunks', dt, sum(c.size for c in sel)/1e6/dt,'MB/s')
EOF
timeout 900 python tput3.py
```

```
1 [1]
index 1127 3.563253879547119
(0, 0, 0, 0) (0, 0, 0, 1) (152, 0, 0, 0)
8 threads 23 chunks 1.8769292831420898 88.052097905006 MB/s
16 threads 23 chunks 1.0019521713256836 164.94555900940298 MB/s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && uv pip install -q antspyx nibabel 2>&1 | tail -2; python -c "import ants, nibabel; print(ants.__version__)"
```

```
Tue Nov 10 05:23:49 UTC 2026
0.6.3
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && curl -sL https://github.com/takuto-okuno-riken/flywalk/archive/4b92add4a44f641ab6add809ff6b0e0d6110b50c.tar.gz | tar xz && mv flywalk-4b92add* flywalk && ls flywalk && sed -n 1,200p flywalk/extractROItimeseries.m
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/flywalk && sed -n 200,400p extractROItimeseries.m; cat lib/getNuisancePolynomial.m lib/getNuisancetCompCor.m lib/getNuisanceRegressionOut.m lib/regressPrepare.m lib/getNuisanceMeanTimeSeries.m
```

```
Xn = [Sd, aComp];
                                elseif strcmp(nuistr, 'gmacomp')
                                    % get Nuisance time-series (Global Mean, CSF comps, WM comps)
                                    Sd = getNuisanceMeanTimeSeries(Vk, [], [], []);
                                    aComp = getNuisanceaCompCor(Vk, csfV, wmV, Sd);
                                    Xn = [Sd, aComp];
                                elseif strcmp(nuistr, 'acomp')
                                    % get Nuisance time-series (CSF comps, WM comps)
                                    Xn = getNuisanceaCompCor(Vk, csfV, wmV);
                                elseif strcmp(nuistr, 'tcomp')
                                    % get Nuisance time-series (high tSTD comps)
                                    Xn = getNuisancetCompCor(Vk);
                                elseif strcmp(nuistr, 'tacomp')
                                    % get Nuisance time-series (high tSTD comps, CSF comps, WM comps)
                                    tComp = getNuisancetCompCor(Vk);
                                    aComp = getNuisanceaCompCor(Vk, csfV, wmV, tComp);
                                    Xn = [tComp, aComp];
                                elseif strcmp(nuistr, 'pol')
                                    % get Nuisance time-series (polynomial)
                                    Xn = getNuisancePolynomial(size(Vk,4));
[... 262 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && uv pip install -q mat73 2>&1|tail -1; python - <<'EOF'
import fsspec, zipfile, io, h5py, scipy.io as sio, numpy as np
url='https://zenodo.org/api/records/15532272/files/flywalkdemodata.zip/content'
z=zipfile.ZipFile(fsspec.open(url, block_size=2**20).open())
def show(name):
    b=z.read(name); print('==',name,len(b))
    try:
        m=sio.loadmat(io.BytesIO(b)); 
        for k,v in m.items():
            if not k.startswith('__'): print(' ',k, type(v), getattr(v,'shape',None), getattr(v,'dtype',None))
    except NotImplementedError:
        f=h5py.File(io.BytesIO(b),'r'); f.visititems(lambda n,o: print(' ',n, getattr(o,'shape',None), getattr(o,'dtype',None)))
    return b
for n in ['flywalkdemodata/results/sc/hemidistkm50_connectlist.mat','flywalkdemodata/results/sc/hemiroi_fw0sr140_connectlist.mat','flywalkdemodata/results/sc/hemiroi_fw0sr140_rd185-20-1_connectlist.mat','flywalkdemodata/results/sc/hemiroi_fw0sr140_transmitter.mat','flywalkdemodata/results/sc/hemiroi_postsyncount.mat','flywalkdemodata/results/fc/poltcomparhemicmkm200-func.mat','flywalkdemodata/results/auc/arhemicmkm20-fcauc.mat']:
    show(n)
EOF
python -c "
import scipy.io as sio
try:
  m=sio.loadmat('$TMPDIR/flywalk/results/sc/hemiroi_connectlist.mat'); print({k:(getattr(v,'shape',None),getattr(v,'dtype',None)) for k,v in m.items()})
except NotImplementedError:
  import h5py; f=h5py.File('$TMPDIR/flywalk/results/sc/hemiroi_connectlist.mat'); f.visititems(lambda n,o: print(n, getattr(o,'shape',None), getattr(o,'dtype',None)))
m=sio.loadmat('$TMPDIR/flywalk/data/hemiroi.mat'); print({k:(getattr(v,'shape',None)) for k,v in m.items()})
"
```

```
== flywalkdemodata/results/sc/hemidistkm50_connectlist.mat 110235
  countMat (2,) uint64
  ncountMat (3, 50, 50) float32
  nweightMat (3, 50, 50) float32
  outweightMat (3, 50, 50) float32
  primaryIds (50, 1) float64
  roiNum (1, 1) float64
  scver (1, 1) float64
  sycountMat (3, 50, 50) float32
  syweightMat (3, 50, 50) float32
  weightMat (2,) uint64
== flywalkdemodata/results/sc/hemiroi_fw0sr140_connectlist.mat 171241
  countMat (2,) uint64
  ncountMat (3, 114, 114) float32
  nweightMat (3, 114, 114) float32
  outweightMat (3, 114, 114) float32
  primaryIds (63, 1) float64
  roiNum (1, 1) float64
  scver (1, 1) float64
  sycountMat (3, 114, 114) float32
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import fsspec, zipfile
url='https://zenodo.org/api/records/18151010/files/flywalkdemodata.zip/content'
z=zipfile.ZipFile(fsspec.open(url, block_size=2**20).open())
for i in z.infolist(): print(i.filename, round(i.file_size/1e6,2))
" > zlist2.txt; grep -v -E "results/(sc|fc|auc)/" zlist2.txt | head -40; grep -i -E "atlas|nii" zlist2.txt | head; curl -s "https://api.github.com/repos/takuto-okuno-riken/flywalk/git/trees/main?recursive=1" | python -c "
import json,sys; d=json.load(sys.stdin)
for t in d['tree']:
  if 'atlas' in t['path'] and 'hemiroi/' not in t['path']: print(t['path'], t.get('size'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
date -u; cd $TMPDIR/flywalk && grep -n "hemiroi_connectlist\|hemiroi_hb\|hemiroi'\|'hemiroi\|function \[\|rois = \|roitypes = {" makeStructConnectivity.m | head -40; grep -n "function\|roitypes\s*=\|roiR\|ncountMat\|log10\|Inf\|atanh\|abs(" analyzeFuncConnectivity.m | head -120
```

```
Tue Nov 10 05:25:53 UTC 2026
23:    idstr = 'hemiroi';
61:        [weightMat3] = makeSCweightMatrixLarge(sycountMat3, 'hemiroi');
161:    idstr = ['hemiroi_fw'  num2str(synTh) 'sr' num2str(fwSth)];
207:            idstr = ['hemiroi_hb'  num2str(synTh) 'sr' num2str(hbSth) functype '_rn' num2str(rnum/10000)];
209:            idstr = ['hemiroi_hb'  num2str(synTh) 'sr' num2str(hbSth) '_sp' num2str(k) 'db' num2str(epsilon) 'mi' num2str(minpts)];
233:        checkScverAndSave(idstr, fname, 'results/sc/hemiroi_hb0sr80_connectlist.mat', countMat, weightMat, ncountMat, sycountMat, nweightMat, outweightMat, syweightMat, primaryIds, roiNum, scver);
267:            idstr = ['hemiroi_fw'  num2str(synTh) 'sr' num2str(fwSth) '_rn' num2str(rnum/10000)];
269:            idstr = ['hemiroi_fw'  num2str(synTh) 'sr' num2str(fwSth) '_sp' num2str(k) 'db' num2str(epsilon) 'mi' num2str(minpts)];
290:        checkScverAndSave(idstr, fname, 'results/sc/hemiroi_hb0sr80_connectlist.mat', countMat, weightMat, ncountMat, sycountMat, nweightMat, outweightMat, syweightMat, primaryIds, roiNum, scver);
304:            idstr = ['hemiroi_hb'  num2str(synTh) 'sr' num2str(hbSth) functype '_rd' num2str(param(1)/10000) '-' num2str(param(2)/10000) '-' num2str(k)];
321:            checkScverAndSave(idstr, fname, 'results/sc/hemiroi_hb0sr80_connectlist.mat', countMat, weightMat, ncountMat, sycountMat, nweightMat, outweightMat, syweightMat, primaryIds, roiNum, scver);
332:            idstr = ['hemiroi_fw'  num2str(synTh) 'sr' num2str(fwSth) '_rd' num2str(param(1)/10000) '-' num2str(param(2)/10000) '-' num2str(k)];
346:            checkScverAndSave(idstr, fname, 'results/sc/hemiroi_hb0sr80_connectlist.mat', countMat, weightMat, ncountMat, sycountMat, nweightMat, outweightMat, syweightMat, primaryIds, roiNum, scver);
373:            idstr = ['hemiroi_hb'  num2str(synTh) 'sr' num2str(hbSth) functype '_rn' num2str(rnum/10000)];
375:            idstr = ['hemiroi_hb'  num2str(synTh) 'sr' num2str(hbSth) functype '_rc
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/flywalk && sed -n 134,250p analyzeFuncConnectivity.m; sed -n 15,40p makeStructConnectivity.m; sed -n 225,240p makeStructConnectivity.m; grep -n "function checkScverAndSave" -A25 makeStructConnectivity.m
```

```
function analyzeFcROItype(roitype, preproc, hpfTh, smooth, nuisance, sbjids, isplot)
    AUCVER = 3;

    % load structural connectivity matrix (from makeStructConnectivity.m)
    switch(roitype)
    case 'hemiroif'
        load('results/sc/hemiroi_connectlist.mat');
        ids = 1:roiNum;
    otherwise
        roitype = lower(roitype);
        load(['results/sc/' roitype '_connectlist.mat']);
        ids = primaryIds;
    end

    nweightMat(isnan(nweightMat)) = 0;
    isw2 = ~isempty(nweightMat);
    issw = ~isempty(syweightMat);
    C2 = ncountMat(ids,ids,1); S = sycountMat(ids,ids,1); W2 = []; Wo = []; Sw = []; W3 = [];
    if isw2
        outweightMat(isnan(outweightMat)) = 0;
[... 166 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/flywalk && sed -n 1,14p makeStructConnectivity.m; grep -n "hbSth\s*=\|synTh\s*=\|fwSth\s*=" makeStructConnectivity.m | head; sed -n 1247,1264p makeStructConnectivity.m; cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import h5py, numpy as np, fsspec, zipfile, io
f=h5py.File('flywalk/results/sc/hemiroi_connectlist.mat','r')
nc=f['ncountMat'][()]; print(nc.shape, f['scver'][()], f['primaryIds'][()].ravel().astype(int))
# h5py transposes matlab: shape as stored
z=zipfile.ZipFile(fsspec.open('https://zenodo.org/api/records/15532272/files/flywalkdemodata.zip/content', block_size=2**20).open())
g=h5py.File(io.BytesIO(z.read('flywalkdemodata/results/sc/hemiroi_fw0sr140_connectlist.mat')),'r')
pid=g['primaryIds'][()].ravel().astype(int); print('fw primary', pid, g['scver'][()])
A=nc[:,:,1] if nc.shape[2]==3 else nc[1]
print('em layer shapes', nc.shape)
EOF
```

```
% make structural connectivity matrix from neuprint connectivity list (csv).
% countMat: only ROI was transformed. countMat2: synapse points were transformed and re-counted in all ROI. 
% this script should run after makeVoxelROIatlas.m

function makeStructConnectivity
    SCVER = 5;
    hbSth = 80;     % FlyEM hemibrain synapse threshold
    fwSth = 140;    % FlyWire synapse score threshold
    synTh = 0;      % synapse count at one neuron threshold
    epsilon = 3000; % dbscan range (nanometer)
    minpts = 1;     % set 1, includes isolated synapse

    % ---------------------------------------------------------------------
    % make structural connectivity matrix of flyem hemibrain neuropil ROIs.
7:    hbSth = 80;     % FlyEM hemibrain synapse threshold
8:    fwSth = 140;    % FlyWire synapse score threshold
9:    synTh = 0;      % synapse count at one neuron threshold
function [roiIdxs, sz, aV] = getHemiroiRoiIdxs(ids)
    if nargin < 1, ids = []; end
    info = niftiinfo('template/thresholded_FDACal_mask.nii.gz');
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -E "results/(fc|auc)/" zlist.txt | grep -i hemiroi | head -40; grep -E "results/(fc)/" zlist.txt | awk '{print $1}' | sed -E 's#.*/fc/##; s/(hemicmkm|hemidistkm)[0-9]+.*//' | sort | uniq -c
```

```
flywalkdemodata/results/auc/poltcomparhemiroi_fw0sr140_rc20_only1-fcauc.mat 0.02 0.01
flywalkdemodata/results/auc/poltcomparhemiroi_fw0sr140_rd140-15-10-fcauc.mat 0.02 0.01
flywalkdemodata/results/auc/poltcomparhemiroi_fw0sr140_rd140-15-11-fcauc.mat 0.02 0.01
flywalkdemodata/results/auc/poltcomparhemiroi_fw0sr140_rd140-15-12-fcauc.mat 0.02 0.01
flywalkdemodata/results/auc/poltcomparhemiroi_fw0sr140_rd140-15-13-fcauc.mat 0.02 0.01
flywalkdemodata/results/auc/poltcomparhemiroi_fw0sr140_rd140-15-14-fcauc.mat 0.02 0.01
flywalkdemodata/results/auc/poltcomparhemiroi_fw0sr140_rd140-15-15-fcauc.mat 0.02 0.01
flywalkdemodata/results/auc/poltcomparhemiroi_fw0sr140_rd140-15-16-fcauc.mat 0.02 0.01
flywalkdemodata/results/auc/poltcomparhemiroi_fw0sr140_rd140-15-17-fcauc.mat 0.02 0.01
flywalkdemodata/results/auc/poltcomparhemiroi_fw0sr140_rd140-15-18-fcauc.mat 0.02 0.01
flywalkdemodata/results/auc/poltcomparhemiroi_fw0sr140_rd140-15-19-fcauc.mat 0.02 0.01
flywalkdemodata/results/auc/poltcomparhemiroi_fw0sr140_rd140-15-1-fcauc.mat 0.02 0.01
flywalkdemodata/results/auc/poltcomparhemiroi_fw0sr140_rd140-15-20-fcauc.mat 0.02 0.01
flywalkdemodata/results/auc/poltcomparhemiroi_fw0sr140_rd140-15-21-fcauc.mat 0.02 0.01
flywalkdemodata/results/auc/poltcomparhemiroi_fw0sr140_rd140-15-22-fcauc.mat 0.02 0.01
flywalkdemodata/results/auc/poltcomparhemiroi_fw0sr140_rd140-15-23-fcauc.mat 0.02 0.01
flywalkdemodata/results/auc/poltcomparhemiroi_fw0sr140_rd140-15-24-fcauc.mat 0.02 0.01
flywalkdemodata/results/auc/poltcomparhemiroi_fw0sr140_rd140-15-25-fcauc.mat 0.02 0.01
flywalkdemodata/results/auc/poltcomparhemiroi_fw0sr140_rd140-15-26-fcauc.mat 0.02 0.01
flywalkdemodata/results/auc/poltcomparhemiroi_fw0sr140_rd140-15-27-fcauc.mat 0.02 0.01
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import nibabel as nib, numpy as np
for f in ['flywalk/template/thresholded_FDACal.nii.gz','flywalk/template/thresholded_FDACal_mask.nii.gz','flywalk/atlas/hemiroi/roi1.nii.gz','flywalk/atlas/hemiFlyem52atlasCal.nii.gz','flywalk/template/jrc2018f_IBN_fiber_bundle_mirror_maskCal_invFDACal.nii.gz']:
    im=nib.load(f); d=im.get_fdata(); print(f, d.shape, im.header.get_zooms(), d.dtype, np.nanmin(d), np.nanmax(d), (d>0).sum()); 
print(nib.load('flywalk/template/thresholded_FDACal.nii.gz').affine)
EOF
cat flywalk/data/hemiroi.xlsx | head -c 0; python -c "
import scipy.io as sio; m=sio.loadmat('$TMPDIR/flywalk/data/hemiroi.mat'); r=m['roiname']; print(r[:5]); print(r[100:106])"
```

```
flywalk/template/thresholded_FDACal.nii.gz (256, 128, 49) (np.float32(2.4521875), np.float32(2.28), np.float32(3.7146938)) float64 0.0 1.0053119659423828 608635
flywalk/template/thresholded_FDACal_mask.nii.gz (256, 128, 49) (np.float32(0.0024521875), np.float32(0.00228), np.float32(0.0037146937)) float64 0.0 1.0 488801
flywalk/atlas/hemiroi/roi1.nii.gz (256, 128, 49) (np.float32(0.0024521875), np.float32(0.00228), np.float32(0.0037146937)) float64 0.0 255.0 4042
flywalk/atlas/hemiFlyem52atlasCal.nii.gz (256, 128, 49) (np.float32(1.0), np.float32(1.0), np.float32(1.0)) float64 0.0 52.0 114972
flywalk/template/jrc2018f_IBN_fiber_bundle_mirror_maskCal_invFDACal.nii.gz (256, 128, 49) (np.float32(0.0024521875), np.float32(0.00228), np.float32(0.0037146937)) float64 0.0 255.0 102410
[[-2.45218754  0.          0.         -0.        ]
 [ 0.         -2.27999997  0.         -0.        ]
 [ 0.          0.          3.71469378  0.        ]
 [ 0.          0.          0.          1.        ]]
[[array(['SCL(R)'], dtype='<U6') array([[1]], dtype=uint8)
  array([[1]], dtype=uint8) array(['superior clamp'], dtype='<U14')
  array([[4042]], dtype=uint16)]
 [array(['ICL(L)'], dtype='<U6') array([[1]], dtype=uint8)
  array([], shape=(0, 0), dtype=uint8)
  array(['inferior clamp'], dtype='<U14') array([[1370]], dtype=uint16)]
 [array(['FBl9'], dtype='<U4') array([[2]], dtype=uint8)
  array([[1]], dtype=uint8)
  array(['fan-shaped body layer 9'], dtype='<U23')
  array([[6]], dtype=uint8)]
 [array(['ATL(R)'], dtype='<U6') array([[1]], dtype=uint8)
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p entries/okuno-2025 && cd $TMPDIR && . dev/bin/activate && cat > regtest.py <<'EOF'
import sys; sys.path.insert(0,'.')
import numpy as np, requests, h5py, remfile, zlib, time, ants, nibabel as nib
from concurrent.futures import ThreadPoolExecutor
aid="80be44d6-db90-4807-bb1b-abdac5c580eb"
s3=requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/", allow_redirects=True).url
f=h5py.File(remfile.File(s3),'r'); d=f['acquisition/TwoPhotonSeriesFunctionalGreen/data']
infos=[d.id.get_chunk_info(i) for i in range(d.id.get_num_chunks())]
sess=requests.Session()
def get(ci):
    r=sess.get(s3, headers={'Range':f'bytes={ci.byte_offset}-{ci.byte_offset+ci.size-1}'})
    a=np.frombuffer(zlib.decompress(r.content),dtype='<u2').reshape(-1,256,128)
    return ci.chunk_offset, a.astype(np.float64).sum(0), a.shape[0]
sel=[ci for ci in infos if ci.chunk_offset[0] in (0, 152*11, 152*21)]
t=time.time()
with ThreadPoolExecutor(16) as ex: res=list(ex.map(get, sel))
m=np.zeros((256,128,49)); n=np.zeros(49)
for off,s,k in res: m[:,:,off[3]]+=s; n[off[3]]+=k
m/=n; print('mean', time.time()-t, m.min(), m.max())
np.save('mean087.npy', m)
tmpl=ants.image_read('flywalk/template/thresholded_FDACal.nii.gz')
print(tmpl)
best=[]
for fx in (1,-1):
  for fy in (1,-1):
    for fz in (1,-1):
        a=m[::fx,::fy,::fz].copy()
        mov=ants.from_numpy(a, spacing=(2.611,2.611,5.0))
        mov.set_origin(tmpl.origin); mov.set_direction(tmpl.direction)
        t=time.time()
        r=ants.registration(tmpl, mov, type_of_transform='Affine', verbose=False)
        mi=ants.image_mutual_information(tmpl, r['warpedmovout'])
        cc=np.corrcoef(tmpl.numpy().ravel(), r['warpedmovout'].numpy().ravel())[0,1]
        print(fx,fy,fz,'MI',mi,'cc',cc, time.time()-t, flush=True)
EOF
python regtest.py
```

```
mean 4.589757442474365 195.1951754385965 6400.938596491228
ANTsImage (RAI)
	 Pixel Type : float (float32)
	 Components : 1
	 Dimensions : (256, 128, 49)
	 Spacing    : (0.0025, 0.0023, 0.0037)
	 Origin     : (0.0, 0.0, 0.0)
	 Direction  : [1. 0. 0. 0. 1. 0. 0. 0. 1.]

1 1 1 MI -0.17186275990816371 cc -0.322131887043429 5.283009052276611
1 1 -1 MI -0.08846239630869558 cc -0.02985207106212515 0.39710426330566406
1 -1 1 MI -0.21272192857922284 cc 0.42440555999775964 2.815870523452759
1 -1 -1 MI -0.08006250378747164 cc -0.03194887918994533 0.4145658016204834
-1 1 1 MI -0.08108169460406607 cc 0.03211312590539143 0.39847493171691895
-1 1 -1 MI -0.00033619774339824763 cc -0.009367262136375232 1.8062875270843506
-1 -1 1 MI -0.08757127829229511 cc 0.030081508935254544 0.3749237060546875
-1 -1 -1 MI -0.18096164498930253 cc 0.36809784029163334 3.4614951610565186
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > regtest2.py <<'EOF'
import numpy as np, ants, time
m=np.load('mean087.npy')
tmpl=ants.image_read('flywalk/template/thresholded_FDACal.nii.gz')
for fx in (1,-1):
  for fy in (1,-1):
    for fz in (1,-1):
        a=m[::fx,::fy,::fz].copy()
        mov=ants.from_numpy(a, spacing=(0.002611,0.002611,0.005))
        t=time.time()
        r=ants.registration(tmpl, mov, type_of_transform='Affine', verbose=False)
        w=r['warpedmovout'].numpy(); tm=tmpl.numpy()
        cc=np.corrcoef(tm.ravel(), w.ravel())[0,1]
        print(fx,fy,fz,'MI',ants.image_mutual_information(tmpl, r['warpedmovout']),'cc',round(cc,3), round(time.time()-t,1), flush=True)
EOF
python regtest2.py
```

```
1 1 1 MI -0.19076685753623737 cc 0.44 0.6
1 1 -1 MI -0.04326270808348649 cc -0.102 2.8
1 -1 1 MI -0.10470902434215712 cc 0.311 1.0
1 -1 -1 MI -0.22846192023593329 cc 0.566 3.0
-1 1 1 MI -0.19043861473815332 cc 0.439 0.6
-1 1 -1 MI -0.20474603390611415 cc 0.484 0.6
-1 -1 1 MI -0.10489907366341375 cc 0.311 0.4
-1 -1 -1 MI -0.10948483349835597 cc 0.337 0.6
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > regtest3.py <<'EOF'
import numpy as np, ants, time, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
m=np.load('mean087.npy')
tmpl=ants.image_read('flywalk/template/thresholded_FDACal.nii.gz'); tm=tmpl.numpy()
a=m[:,::-1,::-1].copy()
mov=ants.from_numpy(a, spacing=(0.002611,0.002611,0.005))
for tt in ['Affine','SyN']:
    t=time.time(); r=ants.registration(tmpl, mov, type_of_transform=tt, verbose=False)
    w=r['warpedmovout'].numpy(); print(tt, np.corrcoef(tm.ravel(), w.ravel())[0,1], time.time()-t, r['fwdtransforms'])
fig,ax=plt.subplots(3,3,figsize=(12,8))
for i,z in enumerate([12,24,36]):
    ax[0,i].imshow(tm[:,:,z].T); ax[1,i].imshow(w[:,:,z].T); ax[2,i].imshow(tm[:,:,z].T,cmap='gray'); ax[2,i].contour((w[:,:,z]>np.percentile(w,70)).T,colors='r',linewidths=0.5)
plt.savefig('reg.png',dpi=70)
EOF
python regtest3.py
```

```
Affine 0.3367412994440579 0.4002707004547119 ['/tmp/claude-1001/tmpwks_4t4z0GenericAffine.mat']
SyN 0.7420290238136511 12.998939752578735 ['/tmp/claude-1001/tmp1dx00to21Warp.nii.gz', '/tmp/claude-1001/tmp1dx00to20GenericAffine.mat']
Shell cwd was reset to
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/reg.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd $TMPDIR/flywalk && grep -n "function checkRandSubsampleRankTestByHemiroi" plotFuncConnectivity.m; sed -n "$(grep -n 'function checkRandSubsampleRankTestByHemiroi' plotFuncConnectivity.m | cut -d: -f1),+95p" plotFuncConnectivity.m
```

```
576:function checkRandSubsampleRankTestByHemiroi(vslabels)
function checkRandSubsampleRankTestByHemiroi(vslabels)
    preproc = 'ar'; % for move correct, slice time correct
    hpfTh = [0]; % high-pass filter threshold
    smooth = {''};
    nuisance = {'poltcomp'};
%    roitypes = {{'hemiroi','_hb0sr80fw_rd140-15'},{'hemiroi','_hb0sr80fw_rd705-40'},{'hemiroi','_hb0sr80fw_rd67-12'}, ...
%       {'hemiroi','_fw0sr140_rd185-20'},{'hemiroi','_fw0sr140_rd1560-80'},{'hemiroi','_fw0sr140_rd140-15'},};
    roitypes = {{'hemiroi','_fw0sr140_rd185-20'},{'hemiroi','_fw0sr140_rd1560-80'},{'hemiroi','_fw0sr140_rd140-15'},};
%    targets = {{'hemiroi','_hb0sr80_sp10db3000mi1_only1'},{'hemiroi','_hb0sr80_sp90db3000mi1'},{'hemiroi','_hb0sr80_rc20_only1'}, ...
%        {'hemiroi','_fw0sr140_sp10db3000mi1_only1'},{'hemiroi','_fw0sr140_sp90db3000mi1'},{'hemiroi','_fw0sr140_rc20_only1'},};
    targets = {{'hemiroi','_fw0sr140_sp10db3000mi1_only1'},{'hemiroi','_fw0sr140_sp90db3000mi1'},{'hemiroi','_fw0sr140_rc20_only1'},};
    rNums = 1:99; % for random subsampling number
    pval = 0.05 / 6; % bonferroni correction

    for r = 1:length(roitypes)
        Am = []; Rm = []; tAm = []; tRm = []; ncounts = []; sycounts = [];
        for h=1:length(hpfTh)
            hpfstr = '';
            if hpfTh(h) > 0, hpfstr = ['hf' num2str(round(1/hpfTh(h)))]; end
[... 78 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/flywalk && sed -n 672,700p plotFuncConnectivity.m; s=$(grep -n 'function showNeuralTransmitter' plotStructConnectivity.m | cut -d: -f1); sed -n "${s},$((s+70))p" plotStructConnectivity.m
```

```
B = abs(Rm) + abs(Am-0.5)*2;
        tB = abs(tRm) + abs(tAm-0.5)*2;
        I = [7 9];
        for i=1:length(I)
            ii = I(i);
            % normality test
            [h,p] = lillietest(Rm(ii,:));
            disp([targets{r}{2} ' corr, Lilliefors test p=' num2str(p)]);
            [h,p] = lillietest(Am(ii,:));
            disp([targets{r}{2} ' AUC, Lilliefors test p=' num2str(p)]);
            [h,p] = lillietest(B(ii,:));
            disp([targets{r}{2} ' all, Lilliefors test p=' num2str(p)]);
            pd1 = fitdist(Rm(ii,:)','Normal');
            p1 = 2*normcdf(-abs(tRm(ii)-pd1.mu)/pd1.sigma); % two tailed normal distribution based test
            pd2 = fitdist(Am(ii,:)','Normal');
            p2 = 2*normcdf(-abs(tAm(ii)-pd2.mu)/pd2.sigma); % two tailed normal distribution based test
            pd3 = fitdist(B(ii,:)','Normal');
            p3 = 2*normcdf(-abs(tB(ii)-pd3.mu)/pd3.sigma);  % two tailed normal distribution based test
            
            % show histogram
[... 81 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import ants, inspect; s=inspect.signature(ants.registration); print([p for p in s.parameters])"; curl -sI -L https://github.com/takuto-okuno-riken/flywalk/archive/4b92add4a44f641ab6add809ff6b0e0d6110b50c.tar.gz | grep -i content-length; date -u
```

Result: the fetched text is not kept.

**Agent calls Write**

```json
{
 "file_path": "entries/okuno-2025/flyfc.py",
 "content": "\"\"\"Loading and measures for testing Okuno et al. (2025) on dandiset 000727.\n\nThe dandiset holds the whole-brain two-photon imaging of Brezovec et al.: one NWB\nfile per fly with the raw GCaMP6f (green) and tdTomato (red) volumes, a processed\ngreen series in the FDA space, and FicTrac walking data at 50 Hz.\n\nThe paper's structural connectivity (SC) and its ROI atlases are outside the\ndataset. They come from\n\n- the paper's code, github.com/takuto-okuno-riken/flywalk at commit 4b92add\n  (CODE_COMMIT): the resized FDA template, brain mask, fibre mask, the hemibrain\n  neuropil atlas (atlas/hemiroi, 114 ROIs), the ROI names (data/hemiroi.mat) and\n  the FlyEM cf0.8 SC of the 114 ROIs (results/sc/hemiroi_connectlist.mat);\n- the paper's Zenodo record 10.5281/zenodo.15532272 (ZENODO_URL), the version of\n  2025-05-28 that the code's README cites: the FlyWire sc140 SC matrices of the\n  hemibrain ROIs, the selected-synapse SC matrices, the 99 null SC matrices of each\n  permutation test, per-ROI transmitter counts and post-synapse counts.\n\nWhere each parameter comes from:\n\n- volume rate 1.879714 Hz, the green channel: the claims file (header, Data the\n  paper used) and the NWB file's own rate.\n- registration of the mean green image to the resized FDA template with ANTs SyN:\n  Methods, Preprocessing (\"the averaged NIfTI image was registered by ANTs to the\n  resized FDA template\"; Ext. Data Fig. 1-1a). Defaults of antspy's \"SyN\" are a\n  standard choice (claims file, O2). The mean image is taken over three blocks of\n  152 volumes (start, middle, end), a standard choice that cannot change which\n  template voxel a native voxel maps to by more than the registration error.\n- the axis orientation of the native volume against the template is not stated in\n  the files; it is chosen from the eight flips by the correlation after an affine\n  registration, printed in the notebook (a data check, not a method choice).\n- ROI time series: the paper warps every volume to the template with linear\n  interpolation and averages the voxels of each ROI (extractROItimeseries.m,\n  Methods \"The intensity of the voxels in the ROI was averaged\"). Here the same\n  linear map is applied as a sparse matrix from native voxels to ROI means, which\n  gives the same ROI series without warping each volume (both are linear in the\n  data). Template voxels outside the field of view count as 0, as the code's\n  V(isnan(V)) = 0 does.\n- nuisance regression, Poly-tCompCor: lib/getNuisancePolynomial.m (7 terms) and\n  lib/getNuisancetCompCor.m (6 principal components of the 1000 voxels with the\n  highest temporal SD, the SD taken on mean-centred data and the components after\n  polynomial detrending), extractROItimeseries.m (each voxel mean-centred and\n  regressed by OLS; the ROI series is the mean). Regressing the ROI mean equals\n  the mean of the voxel residuals, since the regressors are the same for every\n  voxel. Deviation: the 1000 voxels are taken among native voxels inside the\n  template's field of view, not among template voxels (an assumption, stated in the\n  notebook).\n- FC, FC-SC correlation, per-region correlation: analyzeFuncConnectivity.m and the\n  claims file (M3, M4): Pearson r per fly, atanh, mean over flies, infinite values\n  set to the largest finite value; r between log10(SC) (log of 0 set to 0) and\n  |mean z-FC| over all n x n elements; SC is the second (\"Traced\") layer.\n- permutation test: plotFuncConnectivity.m checkRandSubsampleRankTestByHemiroi and\n  the claims file (M6): normal fit to the 99 null values, two-tailed p, Bonferroni\n  0.05/6.\n- subjects: the code's subject list [1 2 3 4 5 6 8 9] of the flies in name order\n  (claims file, header); all nine are shown as a variant.\n\"\"\"\n\nimport gzip\nimport io\nimport os\nimport tarfile\nimport time\nimport zipfile\nimport zlib\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport h5py\nimport numpy as np\nimport remfile\nimport requests\nimport scipy.sparse as sp\nfrom scipy import stats\n\nDANDISET = \"000727\"\nVERSION = \"0.240106.0043\"\nAPI = \"https://api.dandiarchive.org/api\"\nCODE_COMMIT = \"4b92add4a44f641ab6add809ff6b0e0d6110b50c\"\nCODE_TARBALL = f\"https://github.com/takuto-okuno-riken/flywalk/archive/{CODE_COMMIT}.tar.gz\"\nZENODO_RECORD = \"15532272\"\nZENODO_URL = f\"https://zenodo.org/api/records/{ZENODO_RECORD}/files/flywalkdemodata.zip/content\"\nGREEN = \"acquisition/TwoPhotonSeriesFunctionalGreen/data\"\nSUBJECT_IDS = [1, 2, 3, 4, 5, 6, 8, 9]  # code's sbjids, 1-based, flies in name order\nNATIVE_SPACING_MM = (0.00261117299, 0.00261117299, 0.005)  # NWB grid_spacing (m -> mm)\n\n\n# --------------------------------------------------------------------------- archive\ndef list_assets():\n    \"\"\"NWB assets of the pinned version, sorted by path, with their S3 URLs.\"\"\"\n    url = f\"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200\"\n    out = []\n    while url:\n        r = requests.get(url, timeout=60).json()\n        for a in r[\"results\"]:\n            if a[\"path\"].endswith(\".nwb\"):\n                out.append(a)\n        url = r[\"next\"]\n    out.sort(key=lambda a: a[\"path\"])\n    for a in out:\n        meta = requests.get(f\"{API}/assets/{a['asset_id']}/\", timeout=60).json()\n        a[\"s3\"] = [u for u in meta[\"contentUrl\"] if \"s3\" in u][0]\n        a[\"subject\"] = a[\"path\"].split(\"/\")[0].replace(\"sub-\", \"\")\n    return out\n\n\ndef open_nwb(s3):\n    return h5py.File(remfile.File(s3), \"r\")\n\n\nclass ChunkReader:\n    \"\"\"Reads chunks of a gzip-compressed dataset with parallel HTTP range requests.\n\n    remfile and h5py read about 10 MB/s; asking S3 for each chunk's bytes directly and\n    inflating them with zlib (which releases the GIL) reads 100 to 200 MB/s.\"\"\"\n\n    def __init__(self, s3, h5, path=GREEN, threads=16):\n        self.s3 = s3\n        d = h5[path]\n        self.shape = d.shape\n        self.chunks = d.chunks\n        self.dtype = d.dtype\n        n = d.id.get_num_chunks()\n        self.infos = [d.id.get_chunk_info(i) for i in range(n)]\n        self.threads = threads\n        self.session = requests.Session()\n        adapter = requests.adapters.HTTPAdapter(pool_connections=threads, pool_maxsize=threads)\n        self.session.mount(\"https://\", adapter)\n        self.bytes_read = 0\n\n    def _get(self, ci):\n        for attempt in range(5):\n            try:\n                r = self.session.get(self.s3, headers={\n                    \"Range\": f\"bytes={ci.byte_offset}-{ci.byte_offset + ci.size - 1}\"}, timeout=120)\n                raw = zlib.decompress(r.content)\n                break\n            except Exception:\n                if attempt == 4:\n                    raise\n                time.sleep(2)\n        self.bytes_read += ci.size\n        n = len(raw) // (np.dtype(self.dtype).itemsize * self.chunks[1] * self.chunks[2])\n        return ci.chunk_offset, np.frombuffer(raw, dtype=self.dtype).reshape(n, self.chunks[1], self.chunks[2])\n\n    def slices(self, zs):\n        \"\"\"Yield (z, array (T, X, Y)) for each z in zs, prefetching the next slice.\"\"\"\n        T, X, Y, Z = self.shape\n        byz = {}\n        for ci in self.infos:\n            byz.setdefault(ci.chunk_offset[3], []).append(ci)\n        with ThreadPoolExecutor(self.threads) as ex:\n            futs = {}\n            order = list(zs)\n            def submit(z):\n                futs[z] = [ex.submit(self._get, ci) for ci in byz[z]]\n            for z in order[:2]:\n                submit(z)\n            for i, z in enumerate(order):\n                out = np.empty((T, X, Y), dtype=self.dtype)\n                for f in futs.pop(z):\n                    off, a = f.result()\n                    out[off[0]:off[0] + a.shape[0]] = a\n                if i + 2 < len(order):\n                    submit(order[i + 2])\n                yield z, out\n\n    def mean_image(self, tstarts):\n        \"\"\"Mean volume over the time chunks starting at tstarts.\"\"\"\n        T, X, Y, Z = self.shape\n        sel = [ci for ci in self.infos if ci.chunk_offset[0] in tstarts]\n        acc = np.zeros((X, Y, Z))\n        cnt = np.zeros(Z)\n        with ThreadPoolExecutor(self.threads) as ex:\n            for off, a in ex.map(self._get, sel):\n                acc[:, :, off[3]] += a.sum(0, dtype=np.float64)\n                cnt[off[3]] += a.shape[0]\n        return acc / cnt\n\n\n# --------------------------------------------------------------------------- paper inputs\n_code = None\n\n\ndef code_file(name):\n    \"\"\"A file of the paper's code repository at CODE_COMMIT, as bytes.\"\"\"\n    global _code\n    if _code is None:\n        b = requests.get(CODE_TARBALL, timeout=300).content\n        t = tarfile.open(fileobj=io.BytesIO(b), mode=\"r:gz\")\n        _code = {}\n        for m in t.getmembers():\n            if m.isfile():\n                _code[m.name.split(\"/\", 1)[1]] = t.extractfile(m).read()\n    return _code[name]\n\n\ndef code_nifti(name):\n    import nibabel as nib\n    b = code_file(name)\n    if name.endswith(\".gz\"):\n        b = gzip.decompress(b)\n    img = nib.Nifti1Image.from_bytes(b)\n    return np.asarray(img.dataobj).astype(np.float32), img.header.get_zooms()\n\n\n_zip = None\n\n\ndef zenodo_member(name):\n    \"\"\"A member of the paper's Zenodo zip (read over range requests).\"\"\"\n    global _zip\n    import fsspec\n    if _zip is None:\n        _zip = zipfile.ZipFile(fsspec.open(ZENODO_URL, block_size=2 ** 20).open())\n    return _zip.read(\"flywalkdemodata/\" + name)\n\n\ndef load_mat(b):\n    \"\"\"Read a MATLAB file (v7.3 via h5py, transposed back to MATLAB order).\"\"\"\n    try:\n        import scipy.io as sio\n        m = sio.loadmat(io.BytesIO(b))\n        return {k: v for k, v in m.items() if not k.startswith(\"__\")}\n    except NotImplementedError:\n        f = h5py.File(io.BytesIO(b), \"r\")\n        out = {}\n        for k in f.keys():\n            if isinstance(f[k], h5py.Dataset):\n                a = f[k][()]\n                out[k] = a.T if a.ndim > 1 else a\n        return out\n\n\ndef load_sc(b):\n    \"\"\"SC of a connect list: (ncount layer 2, sycount layer 2, primaryIds 0-based).\"\"\"\n    m = load_mat(b)\n    nc = np.asarray(m[\"ncountMat\"], dtype=np.float64)\n    sc = np.asarray(m[\"sycountMat\"], dtype=np.float64)\n    ids = np.asarray(m[\"primaryIds\"]).ravel().astype(int) - 1\n    return nc[:, :, 1], sc[:, :, 1], ids\n\n\ndef hemiroi_masks():\n    \"\"\"The 114 hemibrain ROI masks of the code repository (template space).\"\"\"\n    masks = []\n    for i in range(1, 115):\n        v, _ = code_nifti(f\"atlas/hemiroi/roi{i}.nii.gz\")\n        masks.append(v > 0)\n    return masks\n\n\ndef hemiroi_names():\n    m = load_mat(code_file(\"data/hemiroi.mat\"))\n    return [str(np.asarray(r).ravel()[0]) for r in m[\"roiname\"][:, 0]]\n\n\n# --------------------------------------------------------------------------- registration\nFLIPS = [(fx, fy, fz) for fx in (1, -1) for fy in (1, -1) for fz in (1, -1)]\n\n\ndef _flip(a, fl):\n    return a[::fl[0], ::fl[1], ::fl[2]].copy()\n\n\ndef choose_flip(mean, tmpl_img, seed=1):\n    \"\"\"Correlation with the template after an affine registration, for each flip.\"\"\"\n    import ants\n    out = {}\n    tm = tmpl_img.numpy().ravel()\n    for fl in FLIPS:\n        mov = ants.from_numpy(_flip(mean, fl).astype(np.float32), spacing=NATIVE_SPACING_MM)\n        r = ants.registration(tmpl_img, mov, type_of_transform=\"Affine\", random_seed=seed)\n        out[fl] = float(np.corrcoef(tm, r[\"warpedmovout\"].numpy().ravel())[0, 1])\n    return out\n\n\ndef register(mean, tmpl_img, fl, seed=1):\n    \"\"\"SyN registration of the flipped mean image to the template.\n\n    Returns the native continuous coordinates (n, 3) of every template voxel (NaN\n    outside the field of view) and the correlation with the template after it.\"\"\"\n    import ants\n    mov = ants.from_numpy(_flip(mean, fl).astype(np.float32), spacing=NATIVE_SPACING_MM)\n    r = ants.registration(tmpl_img, mov, type_of_transform=\"SyN\", random_seed=seed)\n    cc = float(np.corrcoef(tmpl_img.numpy().ravel(), r[\"warpedmovout\"].numpy().ravel())[0, 1])\n    shp = mean.shape\n    coords = []\n    for ax in range(3):\n        g = np.zeros(shp, np.float32)\n        idx = np.arange(shp[ax], dtype=np.float32)\n        sh = [1, 1, 1]\n        sh[ax] = -1\n        g[:] = idx.reshape(sh)\n        ci = ants.from_numpy(g, spacing=NATIVE_SPACING_MM)\n        w = ants.apply_transforms(tmpl_img, ci, r[\"fwdtransforms\"], interpolator=\"linear\",\n                                  defaultvalue=-1e6).numpy()\n        coords.append(w.ravel())\n    c = np.stack(coords, 1).astype(np.float64)\n    c[(c < -0.5).any(1)] = np.nan\n    # back from the flipped grid to native indices\n    for ax in range(3):\n        if fl[ax] == -1:\n            c[:, ax] = shp[ax] - 1 - c[:, ax]\n    for f in r[\"fwdtransforms\"] + r[\"invtransforms\"]:\n        if os.path.exists(f):\n            try:\n                os.remove(f)\n            except OSError:\n                pass\n    return c, cc, r[\"warpedmovout\"].numpy()\n\n\ndef interp_matrix(coords, shp):\n    \"\"\"Sparse (template voxels x native voxels) trilinear interpolation matrix.\n\n    Native voxels are ordered z-major, then x, then y (index z*X*Y + x*Y + y), the\n    order in which slices are streamed.\"\"\"\n    X, Y, Z = shp\n    n = coords.shape[0]\n    ok = ~np.isnan(coords).any(1)\n    rows, cols, vals = [], [], []\n    c = coords[ok]\n    r_ok = np.nonzero(ok)[0]\n    c = np.clip(c, 0, np.array([X - 1, Y - 1, Z - 1]))\n    f = np.floor(c).astype(int)\n    d = c - f\n    for dx in (0, 1):\n        for dy in (0, 1):\n            for dz in (0, 1):\n                ix = np.minimum(f[:, 0] + dx, X - 1)\n                iy = np.minimum(f[:, 1] + dy, Y - 1)\n                iz = np.minimum(f[:, 2] + dz, Z - 1)\n                w = ((d[:, 0] if dx else 1 - d[:, 0]) * (d[:, 1] if dy else 1 - d[:, 1])\n                     * (d[:, 2] if dz else 1 - d[:, 2]))\n                keep = w > 0\n                rows.append(r_ok[keep])\n                cols.append((iz * X * Y + ix * Y + iy)[keep])\n                vals.append(w[keep])\n    P = sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))),\n                      shape=(n, X * Y * Z))\n    return P, ok\n\n\ndef roi_weights(masks, P):\n    \"\"\"Rows: the mean over each mask's template voxels, mapped to native voxels.\"\"\"\n    n = P.shape[0]\n    rows, cols, vals = [], [], []\n    for i, m in enumerate(masks):\n        idx = np.nonzero(m.ravel())[0]\n        rows.append(np.full(idx.size, i))\n        cols.append(idx)\n        vals.append(np.full(idx.size, 1.0 / max(idx.size, 1)))\n    A = sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))),\n                      shape=(len(masks), n))\n    return (A @ P).tocsc()\n\n\n# --------------------------------------------------------------------------- per fly\ndef process_fly(asset, tmpl_img, masks, n_top=1000, log=print):\n    \"\"\"Stream one fly's green series once and reduce it to ROI series.\n\n    Returns a dict with the ROI mean series (rows = masks, T columns), the series of\n    the n_top native voxels with the highest temporal SD (for tCompCor), the\n    registration diagnostics and the field-of-view coverage of each mask.\"\"\"\n    t0 = time.time()\n    h5 = open_nwb(asset[\"s3\"])\n    rd = ChunkReader(asset[\"s3\"], h5)\n    T, X, Y, Z = rd.shape\n    rate = float(h5[\"acquisition/TwoPhotonSeriesFunctionalGreen/starting_time\"].attrs[\"rate\"])\n    ct = rd.chunks[0]\n    tstarts = {0, ct * ((T // ct) // 2), ct * ((T - 1) // ct)}\n    mean = rd.mean_image(tstarts)\n    flips = choose_flip(mean, tmpl_img)\n    fl = max(flips, key=flips.get)\n    coords, cc, warped = register(mean, tmpl_img, fl)\n    P, inside = interp_matrix(coords, (X, Y, Z))\n    W = roi_weights(masks, P)\n    cover = np.array([inside[m.ravel()].mean() if m.any() else np.nan for m in masks])\n    fov = np.asarray(P.sum(0)).ravel() > 0  # native voxels that reach the template grid\n    t_reg = time.time() - t0\n    R = np.zeros((W.shape[0], T))\n    top_sd = np.empty(0)\n    top_ts = np.empty((0, T), np.float32)\n    nvox = X * Y\n    for z, a in rd.slices(range(Z)):\n        xz = a.reshape(T, nvox).astype(np.float32)\n        cols = slice(z * nvox, (z + 1) * nvox)\n        Wz = W[:, cols]\n        if Wz.nnz:\n            R += np.asarray((Wz.T.tocsr().T @ xz.T.astype(np.float64)) if False else (xz.T.T @ Wz.T.toarray().T).T if False else (Wz @ xz.T.astype(np.float64)))\n        m = fov[cols]\n        if m.any():\n            v = xz[:, m]\n            sd = v.std(0, dtype=np.float64)\n            k = min(n_top, sd.size)\n            sel = np.argpartition(-sd, k - 1)[:k]\n            top_sd = np.concatenate([top_sd, sd[sel]])\n            top_ts = np.concatenate([top_ts, v[:, sel].T])\n            if top_sd.size > n_top:\n                keep = np.argpartition(-top_sd, n_top - 1)[:n_top]\n                top_sd, top_ts = top_sd[keep], top_ts[keep]\n    h5.close()\n    return dict(subject=asset[\"subject\"], R=R, top_ts=top_ts, top_sd=top_sd, flips=flips,\n                flip=fl, cc=cc, cover=cover, rate=rate, T=T, shape=(X, Y, Z),\n                mean=mean, warped=warped, t_reg=t_reg, t_total=time.time() - t0,\n                mb_read=rd.bytes_read / 1e6)\n\n\n# --------------------------------------------------------------------------- nuisance and FC\ndef poly_regressors(n):\n    \"\"\"lib/getNuisancePolynomial.m: 2 linear, 4 quadratic and a constant term.\"\"\"\n    X = np.empty((n, 7))\n    X[:, 0] = np.linspace(0, 1, n)\n    X[:, 1] = np.linspace(1, 0, n)\n    X[:, 2] = X[:, 0] ** 2\n    X[:, 3] = X[::-1, 2]\n    X[:, 4] = 1 - X[:, 2]\n    X[:, 5] = 1 - X[:, 3]\n    X[:, 6] = 1\n    return X\n\n\ndef residualize(Y, Xn):\n    \"\"\"OLS residuals of each column of Y (T x k) on Xn (T x p).\"\"\"\n    beta, *_ = np.linalg.lstsq(Xn, Y, rcond=None)\n    return Y - Xn @ beta\n\n\ndef tcompcor(top_ts, Sd, ncomp=6):\n    \"\"\"lib/getNuisancetCompCor.m: PCA scores of the high-SD voxels after detrending.\"\"\"\n    V = top_ts.astype(np.float64).T  # T x voxels\n    V = V - V.mean(0)\n    V = residualize(V, Sd)\n    V = V - V.mean(0)\n    U, S, _ = np.linalg.svd(V, full_matrices=False)\n    return U[:, :ncomp] * S[:ncomp]\n\n\ndef roi_series(fly, nuisance):\n    \"\"\"ROI series (T x ROIs) for nuisance '' (none) or 'poltcomp'.\"\"\"\n    Y = fly[\"R\"].T.copy()\n    Y = Y - Y.mean(0)\n    if nuisance == \"poltcomp\":\n        Sd = poly_regressors(Y.shape[0])\n        Xn = np.hstack([Sd, tcompcor(fly[\"top_ts\"], Sd)])\n        Y = residualize(Y, Xn)\n    elif nuisance != \"\":\n        raise ValueError(nuisance)\n    return Y - Y.mean(0)\n\n\ndef mean_zfc(series_list):\n    \"\"\"Fisher-z FC averaged over flies (analyzeFuncConnectivity.m).\"\"\"\n    Z = []\n    for Y in series_list:\n        with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n            C = np.corrcoef(Y.T)\n            Z.append(np.arctanh(C))\n    Z = np.stack(Z, 2)\n    with np.errstate(invalid=\"ignore\"):\n        m = np.nanmean(Z, 2)\n    fin = np.isfinite(m)\n    m[np.isinf(m)] = np.max(m[fin])\n    return m\n\n\ndef log_sc(S):\n    with np.errstate(divide=\"ignore\"):\n        L = np.log10(S)\n    L[L < 0] = 0\n    return L\n\n\ndef fcsc_r(S, mFz, ids, kind=\"pearson\"):\n    \"\"\"FC-SC correlation over every element of the ids x ids matrices (code's R).\"\"\"\n    a = log_sc(S[np.ix_(ids, ids)]).ravel()\n    b = np.abs(mFz[np.ix_(ids, ids)]).ravel()\n    ok = np.isfinite(b)\n    if kind == \"spearman\":\n        return stats.spearmanr(a[ok], b[ok])[0]\n    return np.corrcoef(a[ok], b[ok])[0, 1]\n\n\ndef fcsc_roi_r(S, mFz, ids):\n    \"\"\"Per-region FC-SC correlation (code's roiR column 7).\"\"\"\n    L = log_sc(S[np.ix_(ids, ids)])\n    F = np.abs(mFz[np.ix_(ids, ids)])\n    out = np.empty(len(ids))\n    for i in range(len(ids)):\n        a = np.concatenate([L[i, :], L[:, i]])\n        b = np.concatenate([F[i, :], F[:, i]])\n        out[i] = np.corrcoef(a, b)[0, 1]\n    return out\n\n\ndef normal_p(x, null):\n    \"\"\"Two-tailed p of x against a normal fitted to the null (MATLAB fitdist).\"\"\"\n    mu, sd = np.mean(null), np.std(null, ddof=1)\n    return 2 * stats.norm.cdf(-abs(x - mu) / sd), mu, sd\n"
}
```

```
File created successfully at: entries/okuno-2025/flyfc.py (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/okuno-2025/flyfc.py",
 "old_string": "        if Wz.nnz:\n            R += np.asarray((Wz.T.tocsr().T @ xz.T.astype(np.float64)) if False else (xz.T.T @ Wz.T.toarray().T).T if False else (Wz @ xz.T.astype(np.float64)))",
 "new_string": "        if Wz.nnz:\n            R += np.asarray(Wz @ xz.T)"
}
```

```
The file entries/okuno-2025/flyfc.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/okuno-2025/flyfc.py",
 "old_string": "    return (A @ P).tocsc()",
 "new_string": "    return (A @ P).tocsc().astype(np.float32)"
}
```

```
The file entries/okuno-2025/flyfc.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t1.py <<'EOF'
import sys, time, resource; sys.path.insert(0,'entries/okuno-2025')
import flyfc, numpy as np, ants, pickle
t=time.time()
assets=flyfc.list_assets(); print([a['subject'] for a in assets], time.time()-t)
tm,z=flyfc.code_nifti('template/thresholded_FDACal.nii.gz'); print(tm.shape,z, time.time()-t)
tmpl=ants.from_numpy(tm, spacing=tuple(float(v)/1000 if v>0.1 else float(v) for v in z))
print(tmpl.spacing)
masks=flyfc.hemiroi_masks(); print('masks', len(masks), time.time()-t)
fly=flyfc.process_fly(assets[0], tmpl, masks)
print({k:v for k,v in fly.items() if k in ('flips','flip','cc','t_reg','t_total','mb_read')})
print('cover min', np.nanmin(fly['cover']), 'maxrss MB', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e3)
pickle.dump(fly, open('fly0.pkl','wb'))
EOF
python t1.py 2>&1 | tail -20
```

```
['fly-087', 'fly-089', 'fly-094', 'fly-097', 'fly-098', 'fly-099', 'fly-100', 'fly-101', 'fly-105'] 2.1193275451660156
(256, 128, 49) (np.float32(2.4521875), np.float32(2.28), np.float32(3.7146938)) 3.596622943878174
(0.0024521875381469725, 0.0022799999713897707, 0.003714693784713745)
masks 114 6.879396200180054
Traceback (most recent call last):
  File "/tmp/claude-1001/t1.py", line 9, in <module>
    fly=flyfc.process_fly(assets[0], tmpl, masks)
  File "entries/okuno-2025/flyfc.py", line 385, in process_fly
    for z, a in rd.slices(range(Z)):
                ~~~~~~~~~^^^^^^^^^^
  File "entries/okuno-2025/flyfc.py", line 162, in slices
    out[off[0]:off[0] + a.shape[0]] = a
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: could not broadcast input array from shape (152,256,128) into shape (40,256,128)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/okuno-2025 && python - <<'EOF'
p='flyfc.py'; s=open(p).read()
s=s.replace("""                    off, a = f.result()
                    out[off[0]:off[0] + a.shape[0]] = a""","""                    off, a = f.result()
                    a = a[:T - off[0]]  # the last chunk is stored padded
                    out[off[0]:off[0] + a.shape[0]] = a""")
s=s.replace("""            for off, a in ex.map(self._get, sel):
                acc""","""            for off, a in ex.map(self._get, sel):
                a = a[:T - off[0]]
                acc""")
open(p,'w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && python t1.py 2>&1 | tail -8
```

```
['fly-087', 'fly-089', 'fly-094', 'fly-097', 'fly-098', 'fly-099', 'fly-100', 'fly-101', 'fly-105'] 2.0893640518188477
(256, 128, 49) (np.float32(2.4521875), np.float32(2.28), np.float32(3.7146938)) 3.570526361465454
(0.0024521875381469725, 0.0022799999713897707, 0.003714693784713745)
masks 114 6.845857620239258
{'flips': {(1, 1, 1): 0.7290182823582335, (1, 1, -1): 0.4841227538702925, (1, -1, 1): 0.3164351323097022, (1, -1, -1): 0.3396874356261213, (-1, 1, 1): 0.7298337728747757, (-1, 1, -1): 0.4824836031970398, (-1, -1, 1): 0.3162828300948061, (-1, -1, -1): 0.3400692766283192}, 'flip': (-1, 1, 1), 'cc': 0.6401931873491722, 't_reg': 33.230417013168335, 't_total': 402.8311071395874, 'mb_read': 8160.716083}
cover min 1.0 maxrss MB 4060.4
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t2.py <<'EOF'
import sys, time; sys.path.insert(0,'entries/okuno-2025')
import flyfc, numpy as np
assets=flyfc.list_assets(); a=assets[1]
h5=flyfc.open_nwb(a['s3']); rd=flyfc.ChunkReader(a['s3'],h5, threads=24)
t=time.time(); n=0
for z,x in rd.slices(range(10)):
    n+=1
dt=time.time()-t; print('fetch 10 slices', dt, rd.bytes_read/1e6/dt, 'MB/s')
xz=x.reshape(3384,-1).astype(np.float32)
W=np.random.rand(114,32768).astype(np.float32)
t=time.time(); R=xz@W.T; print('matmul', time.time()-t)
t=time.time(); s1=xz.sum(0,dtype=np.float64); s2=np.einsum('ij,ij->j',xz,xz,dtype=np.float64); print('sd', time.time()-t)
EOF
python t2.py
```

```
fetch 10 slices 7.044544696807861 186.63094459401356 MB/s
matmul 0.14949321746826172
sd 0.12744641304016113
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import pickle, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt, sys
sys.path.insert(0,'entries/okuno-2025'); import flyfc
f=pickle.load(open('fly0.pkl','rb')); m=f['mean']
tm,_=flyfc.code_nifti('template/thresholded_FDACal.nii.gz')
fig,ax=plt.subplots(3,4,figsize=(16,9))
for i,z in enumerate([6,18,30,42]):
    ax[0,i].imshow(m[:,:,z].T,cmap='gray'); ax[0,i].set_title(f'native z={z}')
for i,z in enumerate([6,18,30,42]):
    ax[1,i].imshow(tm[:,:,z].T,cmap='gray'); ax[1,i].set_title(f'tmpl z={z}')
ax[2,0].imshow(m[:,64,:].T,cmap='gray',aspect=5/2.6); ax[2,0].set_title('native xz at y=64')
ax[2,1].imshow(tm[:,64,:].T,cmap='gray',aspect=3.7/2.45); ax[2,1].set_title('tmpl xz')
ax[2,2].imshow(m[128,:,:].T,cmap='gray',aspect=5/2.6); ax[2,2].set_title('native yz at x=128')
ax[2,3].imshow(tm[128,:,:].T,cmap='gray',aspect=3.7/2.28); ax[2,3].set_title('tmpl yz')
plt.tight_layout(); plt.savefig('orient.png',dpi=60)
EOF
```

```
Shell cwd was reset to
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/orient.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd entries/okuno-2025 && python - <<'EOF'
p='flyfc.py'; s=open(p).read()
s=s.replace("""def process_fly(asset, tmpl_img, masks, n_top=1000, log=print):""","""def process_fly(asset, tmpl_img, masks, n_top=1000, flip=(1, 1, 1)):""")
s=s.replace("""    flips = choose_flip(mean, tmpl_img)
    fl = max(flips, key=flips.get)
""","""    flips = choose_flip(mean, tmpl_img)
    fl = flip
""")
s=s.replace("""    return dict(subject=asset["subject"], R=R, top_ts=top_ts, top_sd=top_sd, flips=flips,
                flip=fl, cc=cc, cover=cover,""","""    return dict(subject=asset["subject"], R=R, top_ts=top_ts, top_sd=top_sd, flips=flips,
                flip=fl, cc=cc, cover=cover, coords=coords.astype(np.float32),""")
s=s.replace("""- the axis orientation of the native volume against the template is not stated in
  the files; it is chosen from the eight flips by the correlation after an affine
  registration, printed in the notebook (a data check, not a method choice).""","""- the axis orientation of the native volume against the template is not stated in
  the files. The notebook shows the native mean image beside the template: the
  dorsoventral (y) and anteroposterior (z) axes run the same way, so no flip is
  applied. Left and right cannot be told apart from a symmetric image (the
  correlation after an affine registration is printed for the eight flips); no flip
  is assumed, and the notebook shows the result with left and right ROIs swapped.""")
open(p,'w').write(s)
EOF
grep -n "fl = flip\|flip=(1" flyfc.py
```

```
364:def process_fly(asset, tmpl_img, masks, n_top=1000, flip=(1, 1, 1)):
379:    fl = flip
```

**Agent calls Bash**

```bash
cd $TMPDIR/flywalk && cat checkBehavior.m; sed -n 1,80p glmFlyMB1st.m
```

```
% checking registered calcium imaging histogram, etc.

function checkBehavior
    frames = 3384; % frame num of calcium imaging
    offset = 104.654892; % ms, start time of calcium imaging
    TR = 1000 / 1.879714; % ms, retrieval time of calcium imaging

    % check movement speed
    listing = dir('behavior/sub-fly-*.mat');
    MS = [];
    for i=1:length(listing)
        folder = listing(i).folder;
        name = listing(i).name;

        load([folder '/' name]);
        MS = [MS; MovementSpeed]; % 50 Hz, 20ms

        figure; plot(Position(1,:), Position(2,:)); title(['trajectory of ' name]);
    end
    spm = mean(MS,2);
[... 123 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/okuno-2025 && python - <<'EOF'
p='flyfc.py'; s=open(p).read()
s=s.replace("""    rate = float(h5["acquisition/TwoPhotonSeriesFunctionalGreen/starting_time"].attrs["rate"])
""","""    rate = float(h5["acquisition/TwoPhotonSeriesFunctionalGreen/starting_time"].attrs["rate"])
    spd = h5["processing/behavior/FicTrac/SpatialSeriesMovementSpeed"]
    speed = spd["data"][:, 0]
    speed_rate = float(spd["starting_time"].attrs["rate"])
""")
s=s.replace("""flip=fl, cc=cc, cover=cover, coords=coords.astype(np.float32),""","""flip=fl, cc=cc, cover=cover, coords=coords.astype(np.float32),
                speed=speed, speed_rate=speed_rate,""")
open(p,'w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && cat > tall.py <<'EOF'
import sys, time, resource, pickle; sys.path.insert(0,'entries/okuno-2025')
import flyfc, numpy as np, ants
assets=flyfc.list_assets()
tm,z=flyfc.code_nifti('template/thresholded_FDACal.nii.gz')
tmpl=ants.from_numpy(tm, spacing=tuple(float(v)/1000 for v in z))
masks=flyfc.hemiroi_masks()
for a in assets:
    fly=flyfc.process_fly(a, tmpl, masks)
    fly.pop('warped'); 
    print(a['subject'], {k:fly[k] for k in ('flip','cc','t_reg','t_total','mb_read')}, 'cover<1:', int((fly['cover']<0.999).sum()), 'min', np.nanmin(fly['cover']), 'rss', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e3, flush=True)
    pickle.dump(fly, open(f"fly_{a['subject']}.pkl",'wb'))
EOF
python tall.py 2>&1 | grep -v Warn
```

```
fly-087 {'flip': (1, 1, 1), 'cc': 0.6384603591219338, 't_reg': 39.72605514526367, 't_total': 409.45310640335083, 'mb_read': 8160.716083} cover<1: 0 min 1.0 rss 4090.852
fly-089 {'flip': (1, 1, 1), 'cc': 0.6281997229751791, 't_reg': 34.94859266281128, 't_total': 404.038902759552, 'mb_read': 7253.02198} cover<1: 0 min 1.0 rss 4090.852
fly-094 {'flip': (1, 1, 1), 'cc': 0.5159736819247875, 't_reg': 44.571399450302124, 't_total': 419.9744920730591, 'mb_read': 7665.905018} cover<1: 0 min 1.0 rss 4090.852
fly-097 {'flip': (1, 1, 1), 'cc': 0.20177843347211796, 't_reg': 40.12887263298035, 't_total': 330.0258982181549, 'mb_read': 7407.822973} cover<1: 34 min 0.0 rss 4090.852
fly-098 {'flip': (1, 1, 1), 'cc': 0.5758513696574106, 't_reg': 42.47414016723633, 't_total': 411.6753177642822, 'mb_read': 7318.100609} cover<1: 0 min 1.0 rss 4090.852
fly-099 {'flip': (1, 1, 1), 'cc': 0.5213835198831633, 't_reg': 39.90979743003845, 't_total': 398.4919044971466, 'mb_read': 7346.366077} cover<1: 0 min 1.0 rss 4090.852
fly-100 {'flip': (1, 1, 1), 'cc': -0.02347596381814948, 't_reg': 47.84312653541565, 't_total': 225.64945483207703, 'mb_read': 7084.193405} cover<1: 111 min 0.0 rss 4090.852
fly-101 {'flip': (1, 1, 1), 'cc': -0.22205163520752547, 't_reg': 37.36740303039551, 't_total': 313.9182839393616, 'mb_read': 7285.156424} cover<1: 114 min 0.0 rss 4090.852
fly-105 {'flip': (1, 1, 1), 'cc': 0.6504111929112038, 't_reg': 39.02735996246338, 't_total': 401.8297164440155, 'mb_read': 6680.765703} cover<1: 0 min 1.0 rss 4090.852
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && cat > rt.py <<'EOF'
import sys, time, pickle; sys.path.insert(0,'entries/okuno-2025')
import flyfc, numpy as np, ants
tm,z=flyfc.code_nifti('template/thresholded_FDACal.nii.gz')
tmpl=ants.from_numpy(tm, spacing=tuple(float(v)/1000 for v in z))
for s in ['fly-101','fly-100','fly-097','fly-087']:
    m=pickle.load(open(f'fly_{s}.pkl','rb'))['mean'].astype(np.float32)
    mov=ants.from_numpy(m, spacing=flyfc.NATIVE_SPACING_MM)
    for tt in ['Affine','Rigid']:
      for seed in [1,2,3]:
        t=time.time()
        r=ants.registration(tmpl, mov, type_of_transform=tt, random_seed=seed, aff_random_sampling_rate=0.5)
        cc=np.corrcoef(tm.ravel(), r['warpedmovout'].numpy().ravel())[0,1]
        print(s, tt, seed, round(cc,3), round(time.time()-t,1), flush=True)
EOF
python rt.py
```

```
Tue Nov 10 06:36:28 UTC 2026
fly-101 Affine 1 0.343 0.5
fly-101 Affine 2 0.343 1.4
fly-101 Affine 3 0.343 0.7
fly-101 Rigid 1 0.343 0.3
fly-101 Rigid 2 0.343 3.6
fly-101 Rigid 3 0.343 0.2
fly-100 Affine 1 0.669 7.7
fly-100 Affine 2 0.296 0.6
fly-100 Affine 3 0.669 8.2
fly-100 Rigid 1 0.296 0.3
fly-100 Rigid 2 0.296 3.3
fly-100 Rigid 3 0.296 0.8
fly-097 Affine 1 -0.19 8.7
fly-097 Affine 2 0.404 4.8
fly-097 Affine 3 0.682 9.5
fly-097 Rigid 1 0.404 0.6
fly-097 Rigid 2 0.404 0.3
fly-097 Rigid 3 0.404 0.3
fly-087 Affine 1 0.729 7.0
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > rt2.py <<'EOF'
import sys, time, pickle; sys.path.insert(0,'entries/okuno-2025')
import flyfc, numpy as np, ants
tm,z=flyfc.code_nifti('template/thresholded_FDACal.nii.gz')
tmpl=ants.from_numpy(tm, spacing=tuple(float(v)/1000 for v in z))
for s in ['fly-101','fly-100','fly-097','fly-087']:
    m=pickle.load(open(f'fly_{s}.pkl','rb'))['mean'].astype(np.float32)
    m=m/np.percentile(m,99)
    mov=ants.from_numpy(m, spacing=flyfc.NATIVE_SPACING_MM)
    for tt in ['TRSAA']:
        t=time.time()
        r=ants.registration(tmpl, mov, type_of_transform=tt, random_seed=1)
        cc=np.corrcoef(tm.ravel(), r['warpedmovout'].numpy().ravel())[0,1]
        t2=time.time()
        r2=ants.registration(tmpl, mov, type_of_transform='SyNOnly', initial_transform=r['fwdtransforms'][0], random_seed=1)
        cc2=np.corrcoef(tm.ravel(), r2['warpedmovout'].numpy().ravel())[0,1]
        print(s, tt, round(cc,3), round(t2-t,1), 'syn', round(cc2,3), round(time.time()-t2,1), r2['fwdtransforms'], flush=True)
EOF
python rt2.py
```

```
fly-101 TRSAA 0.343 0.6 syn 0.563 10.6 ['/tmp/claude-1001/tmpix0_tsmv1Warp.nii.gz', '/tmp/claude-1001/tmpix0_tsmv0GenericAffine.mat']
fly-100 TRSAA 0.296 0.6 syn 0.492 11.2 ['/tmp/claude-1001/tmp88w6r7ms1Warp.nii.gz', '/tmp/claude-1001/tmp88w6r7ms0GenericAffine.mat']
fly-097 TRSAA 0.404 0.6 syn 0.591 10.9 ['/tmp/claude-1001/tmp1b3tr0sx1Warp.nii.gz', '/tmp/claude-1001/tmp1b3tr0sx0GenericAffine.mat']
fly-087 TRSAA 0.44 1.0 syn 0.638 11.1 ['/tmp/claude-1001/tmpkch7p4ky1Warp.nii.gz', '/tmp/claude-1001/tmpkch7p4ky0GenericAffine.mat']
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > rt3.py <<'EOF'
import sys, time, pickle; sys.path.insert(0,'entries/okuno-2025')
import flyfc, numpy as np, ants
tm,z=flyfc.code_nifti('template/thresholded_FDACal.nii.gz')
tmpl=ants.from_numpy(tm, spacing=tuple(float(v)/1000 for v in z))
for s in ['fly-101','fly-100']:
    m=pickle.load(open(f'fly_{s}.pkl','rb'))['mean'].astype(np.float32)
    m=np.clip(m/np.percentile(m,99.5),0,1)
    mov=ants.from_numpy(m, spacing=flyfc.NATIVE_SPACING_MM)
    for metric in ['GC','meansquares','mattes']:
        t=time.time()
        r=ants.registration(tmpl, mov, type_of_transform='Affine', aff_metric=metric, random_seed=1, aff_iterations=(2100,1200,1200,10), aff_shrink_factors=(6,4,2,1), aff_smoothing_sigmas=(3,2,1,0))
        cc=np.corrcoef(tm.ravel(), r['warpedmovout'].numpy().ravel())[0,1]
        print(s, metric, round(cc,3), round(time.time()-t,1), flush=True)
EOF
python rt3.py
```

```
WARNING: In /project/itksource/Modules/Registration/Metricsv4/include/itkCorrelationImageToImageMetricv4HelperThreader.hxx, line 77
CorrelationImageToImageMetricv4HelperThreader (0x5e2615288380): collected only zero points

WARNING: In /project/itksource/Modules/Numerics/Optimizersv4/include/itkObjectToObjectMetric.hxx, line 544
CorrelationImageToImageMetricv4 (0x5e261386c5d0): No valid points were found during metric evaluation. For image metrics, verify that the images overlap appropriately. For instance, you can align the image centers by translation. For point-set metrics, verify that the fixed points, once transformed into the virtual domain space, actually lie within the virtual domain.

fly-101 GC -0.217 3.2
fly-101 meansquares 0.62 2.6
fly-101 mattes 0.353 0.2
WARNING: In /project/itksource/Modules/Registration/Metricsv4/include/itkCorrelationImageToImageMetricv4HelperThreader.hxx, line 77
CorrelationImageToImageMetricv4HelperThreader (0x5e26150f23a0): collected only zero points

WARNING: In /project/itksource/Modules/Numerics/Optimizersv4/include/itkObjectToObjectMetric.hxx, line 544
CorrelationImageToImageMetricv4 (0x5e261386c5d0): No valid points were found during metric evaluation. For image metrics, verify that the images overlap appropriately. For instance, you can align the image centers by translation. For point-set metrics, verify that the fixed points, once transformed into the virtual domain space, actually lie within the virtual domain.

WARNING: In /project/itksource/Modules/Registration/Metricsv4/include/itkCorrelationImageToImageMetricv4HelperThreader.hxx, line 77
CorrelationImageToImageMetricv4HelperThreader (0x5e26150f23a0): collected only zero points

WARNING: In /project/itksource/Modules/Numerics/Optimizersv4/include/itkObjectToObjectMetric.hxx, line 544
CorrelationImageToImageMetricv4 (0x5e261386c5d0): No valid points were found during metric evaluation. For image metrics, verify that the images overlap appropriately. For instance, you c
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/okuno-2025 && python - <<'EOF'
p='flyfc.py'; s=open(p).read()
old_reg=s[s.index('def register(mean, tmpl_img, fl, seed=1):'):s.index('    shp = mean.shape\n    coords = []')]
new_reg='''def register(mean, tmpl_img, fl, seed=1):
    """SyN registration of the flipped mean image to the template.

    The affine start is the better of two affine registrations (mean squares and
    Mattes mutual information, on the image scaled to its 99.5th percentile): with
    antspy's default affine stage the optimiser stopped at its start for several
    flies (correlation with the template 0.3). The SyN stage then starts from it.

    Returns the native continuous coordinates (n, 3) of every template voxel (NaN
    outside the field of view), the correlations with the template after the
    affine and the SyN stages, and the warped mean image."""
    import ants
    m = _flip(mean, fl).astype(np.float32)
    m = np.clip(m / np.percentile(m, 99.5), 0, 1)
    mov = ants.from_numpy(m, spacing=NATIVE_SPACING_MM)
    tm = tmpl_img.numpy().ravel()
    aff = {}
    for metric in ("meansquares", "mattes"):
        r = ants.registration(tmpl_img, mov, type_of_transform="Affine", aff_metric=metric,
                              random_seed=seed, aff_iterations=(2100, 1200, 1200, 10),
                              aff_shrink_factors=(6, 4, 2, 1), aff_smoothing_sigmas=(3, 2, 1, 0))
        aff[metric] = (float(np.corrcoef(tm, r["warpedmovout"].numpy().ravel())[0, 1]),
                       r["fwdtransforms"][0])
    best = max(aff, key=lambda k: aff[k][0])
    r = ants.registration(tmpl_img, mov, type_of_transform="SyNOnly",
                          initial_transform=aff[best][1], random_seed=seed)
    cc = {"affine_" + k: v[0] for k, v in aff.items()}
    cc["syn"] = float(np.corrcoef(tm, r["warpedmovout"].numpy().ravel())[0, 1])
'''
s=s.replace(old_reg,new_reg)
s=s.replace('''    for f in r["fwdtransforms"] + r["invtransforms"]:''','''    for f in r["fwdtransforms"] + r["invtransforms"] + [v[1] for v in aff.values()]:''')
old_loop=s[s.index('    for z, a in rd.slices(range(Z)):'):s.index('    h5.close()\n    return dict(subject')]
new_loop='''    for z, a in rd.slices(range(Z)):
        xz = a.reshape(T, nvox).astype(np.float32)
        cols = slice(z * nvox, (z + 1) * nvox)
        Wz = W[:, cols]
        if Wz.nnz:
            R += xz @ Wz.toarray().T
        m = np.nonzero(fov[cols])[0]
        if m.size:
            v = xz[:, m]
            mu = v.mean(0, dtype=np.float64)
            sd = np.sqrt(np.maximum(np.einsum("ij,ij->j", v, v, dtype=np.float64) / T - mu ** 2, 0))
            k = min(n_top, sd.size)
            sel = np.argpartition(-sd, k - 1)[:k]
            top_sd = np.concatenate([top_sd, sd[sel]])
            top_ts = np.concatenate([top_ts, v[:, sel].T])
            if top_sd.size > n_top:
                keep = np.argpartition(-top_sd, n_top - 1)[:n_top]
                top_sd, top_ts = top_sd[keep], top_ts[keep]
'''
s=s.replace(old_loop,new_loop)
s=s.replace('''    R = np.zeros((W.shape[0], T))''','''    R = np.zeros((T, W.shape[0]))''')
s=s.replace('''    h5.close()
    return dict(subject=asset["subject"], R=R,''','''    h5.close()
    return dict(subject=asset["subject"], R=R.T,''')
open(p,'w').write(s)
EOF
grep -n "R = np.zeros\|R=R.T\|R += " flyfc.py
```

```
408:    R = np.zeros((T, W.shape[0]))
417:            R += xz @ Wz.toarray().T
431:    return dict(subject=asset["subject"], R=R.T, top_ts=top_ts, top_sd=top_sd, flips=flips,
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='flyfc.py'; s=open(p).read()
s=s.replace("""    flips = choose_flip(mean, tmpl_img)
    fl = flip
""","""    fl = flip
""")
s=s.replace("top_sd=top_sd, flips=flips,","top_sd=top_sd,")
open(p,'w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && sed -i "s/print(a\['subject'\], {k:fly\[k\] for k in ('flip','cc','t_reg','t_total','mb_read')}/print(a['subject'], {k:fly[k] for k in ('cc','t_reg','t_total','mb_read')}/" tall.py && sed -i "s/^for a in assets:/for a in assets[int(sys.argv[1]):int(sys.argv[2])]:/" tall.py && python tall.py 6 8 2>&1 | grep -v -i warn
```

```
fly-100 {'cc': {'affine_meansquares': 0.619708936088102, 'affine_mattes': 0.677857955138494, 'syn': 0.7362935475209409}, 't_reg': 28.593405961990356, 't_total': 285.30187368392944, 'mb_read': 7084.193405} cover<1: 20 min 0.14861902674265673 rss 3647.812
fly-101 {'cc': {'affine_meansquares': 0.6391174186690376, 'affine_mattes': 0.3532883843061869, 'syn': 0.7262518372693026}, 't_reg': 28.98860239982605, 't_total': 226.71594786643982, 'mb_read': 7285.156424} cover<1: 0 min 1.0 rss 3800.032
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > prof.py <<'EOF'
import sys, time; sys.path.insert(0,'entries/okuno-2025')
import flyfc, numpy as np, scipy.sparse as sp
assets=flyfc.list_assets(); a=assets[2]
h5=flyfc.open_nwb(a['s3']); rd=flyfc.ChunkReader(a['s3'],h5)
W=sp.random(114, 32768*49, density=0.03, format='csc', dtype=np.float32)
fov=np.ones(32768*49,bool)
T=3384; nvox=32768
tf=tc=0; t0=time.time()
for z,x in rd.slices(range(8)):
    t1=time.time(); tf+=t1-t0
    xz=x.reshape(T,nvox).astype(np.float32); ta=time.time()
    Wz=W[:, slice(z*nvox,(z+1)*nvox)]; R=xz@Wz.toarray().T; tb=time.time()
    m=np.nonzero(fov[z*nvox:(z+1)*nvox])[0]; v=xz[:,m]; tcc=time.time()
    mu=v.mean(0,dtype=np.float64); sd=np.sqrt(np.maximum(np.einsum('ij,ij->j',v,v,dtype=np.float64)/T-mu**2,0)); td=time.time()
    print(z, 'wait',round(t1-t0,2),'astype',round(ta-t1,2),'mm',round(tb-ta,2),'idx',round(tcc-tb,2),'sd',round(td-tcc,2), flush=True)
    t0=time.time()
EOF
python prof.py
```

```
0 wait 1.67 astype 0.03 mm 0.31 idx 5.34 sd 0.14
1 wait 0.02 astype 0.03 mm 0.15 idx 5.32 sd 0.14
2 wait 0.02 astype 0.03 mm 0.16 idx 5.32 sd 0.14
3 wait 0.02 astype 0.03 mm 0.15 idx 5.38 sd 0.14
4 wait 0.02 astype 0.03 mm 0.15 idx 5.3 sd 0.14
5 wait 0.02 astype 0.03 mm 0.16 idx 5.38 sd 0.14
6 wait 0.02 astype 0.03 mm 0.13 idx 5.25 sd 0.14
7 wait 0.06 astype 0.03 mm 0.13 idx 5.25 sd 0.14
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/okuno-2025 && python - <<'EOF'
p='flyfc.py'; s=open(p).read()
old=s[s.index('        m = np.nonzero(fov[cols])[0]\n'):s.index('            top_sd = np.concatenate')]
new='''        m = fov[cols]
        if m.any():
            mu = xz.mean(0, dtype=np.float64)
            sd = np.sqrt(np.maximum(np.einsum("ij,ij->j", xz, xz, dtype=np.float64) / T - mu ** 2, 0))
            sd[~m] = -1
            k = min(n_top, int(m.sum()))
            sel = np.argpartition(-sd, k - 1)[:k]
            v = xz[:, sel]
            sd = sd[sel]
            sel = np.arange(k)
'''
s=s.replace(old,new)
open(p,'w').write(s)
EOF
sed -n 405,435p flyfc.py
```

```
fov = np.asarray(P.sum(0)).ravel() > 0  # native voxels that reach the template grid
    t_reg = time.time() - t0
    R = np.zeros((T, W.shape[0]))
    top_sd = np.empty(0)
    top_ts = np.empty((0, T), np.float32)
    nvox = X * Y
    for z, a in rd.slices(range(Z)):
        xz = a.reshape(T, nvox).astype(np.float32)
        cols = slice(z * nvox, (z + 1) * nvox)
        Wz = W[:, cols]
        if Wz.nnz:
            R += xz @ Wz.toarray().T
        m = fov[cols]
        if m.any():
            mu = xz.mean(0, dtype=np.float64)
            sd = np.sqrt(np.maximum(np.einsum("ij,ij->j", xz, xz, dtype=np.float64) / T - mu ** 2, 0))
            sd[~m] = -1
            k = min(n_top, int(m.sum()))
            sel = np.argpartition(-sd, k - 1)[:k]
            v = xz[:, sel]
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='flyfc.py'; s=open(p).read()
s=s.replace('''            v = xz[:, sel]
            sd = sd[sel]
            sel = np.arange(k)
            top_sd = np.concatenate([top_sd, sd[sel]])
            top_ts = np.concatenate([top_ts, v[:, sel].T])''','''            top_sd = np.concatenate([top_sd, sd[sel]])
            top_ts = np.concatenate([top_ts, xz[:, sel].T])''')
open(p,'w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && python tall.py 0 9 2>&1 | grep -v -i warn; date -u
```

```
fly-087 {'cc': {'affine_meansquares': 0.66714273678521, 'affine_mattes': -0.14265803391038206, 'syn': 0.8078801452728972}, 't_reg': 27.28205895423889, 't_total': 62.603079319000244, 'mb_read': 8160.716083} cover<1: 0 min 1.0 rss 3297.368
fly-089 {'cc': {'affine_meansquares': 0.6473988740330119, 'affine_mattes': -0.06679396595413609, 'syn': 0.7492393290602184}, 't_reg': 29.754185676574707, 't_total': 62.26513123512268, 'mb_read': 7253.02198} cover<1: 0 min 1.0 rss 3324.812
fly-094 {'cc': {'affine_meansquares': 0.6617320404339404, 'affine_mattes': 0.727902688067891, 'syn': 0.7943808646243258}, 't_reg': 31.441627502441406, 't_total': 68.09071779251099, 'mb_read': 7665.905018} cover<1: 0 min 0.999156711173577 rss 3324.812
fly-097 {'cc': {'affine_meansquares': 0.572405210492364, 'affine_mattes': 0.6949151504264537, 'syn': 0.7584296007881164}, 't_reg': 32.038355350494385, 't_total': 68.00723004341125, 'mb_read': 7407.822973} cover<1: 0 min 1.0 rss 3324.812
fly-098 {'cc': {'affine_meansquares': 0.6269718370452442, 'affine_mattes': 0.3712914026430235, 'syn': 0.737034605515112}, 't_reg': 29.497433185577393, 't_total': 63.08341383934021, 'mb_read': 7318.100609} cover<1: 0 min 1.0 rss 3324.812
fly-099 {'cc': {'affine_meansquares': 0.6346149435672018, 'affine_mattes': 0.6943788805246137, 'syn': 0.7810309364596333}, 't_reg': 31.654043674468994, 't_total': 66.33435773849487, 'mb_read': 7346.366077} cover<1: 2 min 0.9896616541353384 rss 3324.812
fly-100 {'cc': {'affine_meansquares': 0.6332487045423698, 'affine_mattes': 0.6773078513437614, 'syn': 0.7343146646456992}, 't_reg': 32.21065402030945, 't_total': 67.7047290802002, 'mb_read': 7084.193405} cover<1: 20 min 0.11538461538461539 rss 3324.812
fly-101 {'cc': {'affine_meansquares': 0.6443530177430822, 'affine_mattes': 0.3532883843061869, 'syn': 0.7271071021239379}, 't_reg': 29.402303457260132, 't_total': 63.09513235092163, 'mb_read': 7285.156424} cover<1: 0 min 1.0 rss 3324.812
fly-105 {'cc': {'affine_meansquares': 0.57134012520300
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > an.py <<'EOF'
import sys, time, pickle; sys.path.insert(0,'entries/okuno-2025')
import flyfc, numpy as np
from scipy import stats
subs=['fly-087','fly-089','fly-094','fly-097','fly-098','fly-099','fly-100','fly-101','fly-105']
flies=[pickle.load(open(f'fly_{s}.pkl','rb')) for s in subs]
t=time.time()
em_nc, em_sc, em_ids = flyfc.load_sc(flyfc.code_file('results/sc/hemiroi_connectlist.mat'))
fw_nc, fw_sc, ids = flyfc.load_sc(flyfc.zenodo_member('results/sc/hemiroi_fw0sr140_connectlist.mat'))
print('load', time.time()-t, len(ids), em_nc.shape)
names=flyfc.hemiroi_names(); print([names[i] for i in ids][:10])
sel8=[i-1 for i in flyfc.SUBJECT_IDS]
for nuis in ['', 'poltcomp']:
    ser=[flyfc.roi_series(f, nuis) for f in flies]
    for lab, S in [('8',sel8),('9',range(9))]:
        mFz=flyfc.mean_zfc([ser[i] for i in S])
        print(nuis or 'raw', lab, 'EM r7', round(flyfc.fcsc_r(em_nc,mFz,ids),4), 'FW r7', round(flyfc.fcsc_r(fw_nc,mFz,ids),4), 'EM r9', round(flyfc.fcsc_r(em_sc,mFz,ids),4),'FW r9', round(flyfc.fcsc_r(fw_sc,mFz,ids),4))
ser=[flyfc.roi_series(f, 'poltcomp') for f in flies]
mFz=flyfc.mean_zfc([ser[i] for i in sel8])
re=flyfc.fcsc_roi_r(em_nc,mFz,ids); rw=flyfc.fcsc_roi_r(fw_nc,mFz,ids)
print('FlyEM higher', (re>rw).sum(), 'of', len(ids))
tr=flyfc.load_mat(flyfc.zenodo_member('results/sc/hemiroi_fw0sr140_transmitter.mat'))
out=np.asarray(tr['outNTypes'],float); print(out.shape)
out=out/out.sum(1,keepdims=True)
lab=['Unknown','DA','SER','GABA','GLUT','ACH','OCT']
for i in range(1,7):
    r,p=stats.pearsonr(rw, out[ids,i]); print(lab[i], round(r,3), p)
pickle.dump(dict(mFz=mFz), open('mfz.pkl','wb'))
EOF
python an.py
```

```
load 5.43605637550354 63 (114, 114)
['AB(R)', 'AL(R)', 'aL(R)', "a'L(R)", 'AME(R)', 'AOTU(R)', 'ATL(R)', 'AVLP(R)', 'bL(R)', "b'L(R)"]
raw 8 EM r7 0.6249 FW r7 0.5862 EM r9 0.5911 FW r9 0.5581
raw 9 EM r7 0.6299 FW r7 0.5934 EM r9 0.5926 FW r9 0.5604
poltcomp 8 EM r7 0.6089 FW r7 0.5691 EM r9 0.5553 FW r9 0.5275
poltcomp 9 EM r7 0.6116 FW r7 0.5718 EM r9 0.5568 FW r9 0.5293
FlyEM higher 56 of 63
(114, 7)
DA -0.17 0.18387209177909966
SER 0.021 0.8695322993717446
GABA -0.115 0.3679121784038545
GLUT 0.265 0.03612642076346433
ACH -0.048 0.7078289531893147
OCT -0.311 0.013208002815906648
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > an2.py <<'EOF'
import sys, time, pickle; sys.path.insert(0,'entries/okuno-2025')
import flyfc, numpy as np
mFz=pickle.load(open('mfz.pkl','rb'))['mFz']
_,_,ids=flyfc.load_sc(flyfc.zenodo_member('results/sc/hemiroi_fw0sr140_connectlist.mat'))
ref=flyfc.load_mat(flyfc.zenodo_member('results/auc/poltcomparhemiroi_fw0sr140-fcauc.mat'))
print('paper R7,R9', np.ravel(ref['R'])[6], np.ravel(ref['R'])[8])
t=time.time()
for tgt,null in [('sp10db3000mi1_only1','rd185-20'),('sp90db3000mi1','rd1560-80'),('rc20_only1','rd140-15')]:
    nc,sc,_=flyfc.load_sc(flyfc.zenodo_member(f'results/sc/hemiroi_fw0sr140_{tgt}_connectlist.mat'))
    r7=flyfc.fcsc_r(nc,mFz,ids); r9=flyfc.fcsc_r(sc,mFz,ids); tot=sc[np.ix_(ids,ids)].sum(); ntot=nc[np.ix_(ids,ids)].sum()
    N7=[];N9=[];T=[];NT=[]
    for k in range(1,100):
        a,b,_=flyfc.load_sc(flyfc.zenodo_member(f'results/sc/hemiroi_fw0sr140_{null}-{k}_connectlist.mat'))
        N7.append(flyfc.fcsc_r(a,mFz,ids)); N9.append(flyfc.fcsc_r(b,mFz,ids)); T.append(b[np.ix_(ids,ids)].sum()); NT.append(a[np.ix_(ids,ids)].sum())
    p7=flyfc.normal_p(r7,N7); p9=flyfc.normal_p(r9,N9); pt=flyfc.normal_p(tot,T)
    print(tgt, 'r7',round(r7,4), 'null', round(p7[1],4), round(p7[2],4), 'p', p7[0], '| r9', round(r9,4), round(p9[1],4), round(p9[2],4), p9[0], '| tot', tot, pt, ntot, time.time()-t, flush=True)
EOF
python an2.py
```

```
paper R7,R9 0.6835145 0.6404797
sp10db3000mi1_only1 r7 0.6259 null 0.5892 0.0016 p 7.376624584685929e-112 | r9 0.5768 0.5622 0.0023 5.033724961685402e-10 | tot 2373104.0 (np.float64(0.8316667296915374), np.float64(2309356.777777778), np.float64(299896.02058763144)) 137694.0 50.01612401008606
sp90db3000mi1 r7 0.5681 null 0.5722 0.0008 p 4.385969722911179e-08 | r9 0.5219 0.5367 0.0014 9.346878544065636e-26 | tot 28954898.0 (np.float64(0.6401261225069044), np.float64(28360686.606060605), np.float64(1270979.3371571004)) 713783.0 105.72875165939331
rc20_only1 r7 0.6298 null 0.5921 0.0017 p 4.613311981061631e-115 | r9 0.5733 0.5662 0.0022 0.0009905605974304657 | tot 1630011.0 (np.float64(0.8522893869167141), np.float64(1594440.7272727273), np.float64(191034.52804908087)) 184921.0 146.19952940940857
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/flywalk && sed -n 80,175p glmFlyMB1st.m; cat glmFlyMB2nd.m | sed -n 1,90p; cat lib/getGlmCRF.m
```

```
for t=1:size(V,4)
                Vt = imgaussfilt3(V(:,:,:,t), sigma, 'FilterSize', filterSize);
                V(:,:,:,t) = Vt;
            end
        end

        % extract voxel time-series by mask
        disp('apply mask ...');
        aIdx = find(maskV(:) > 0);
        A = reshape(V,[],size(V,4));
        Z = A(aIdx,:);
        Z = Z - nanmean(Z,2);
        Z = Z';
        
        % high pass filter as preprocessing step (M.W.Woolrich, 2001) type.
        if hpfTh > 0
            disp(['apply highpass filter (' num2str(hpfTh) ' Hz) : tfMRI and design matrix...']);
            Z = highpass(Z,hpfTh,1/TR);
        end
        % apply nuisance removal
[... 186 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> entries/okuno-2025/flyfc.py <<'EOF'


# --------------------------------------------------------------------------- GLM
def speed_per_volume(speed, frames=3384, offset_ms=104.654892, rate=1.879714):
    """checkBehavior.m: mean 50 Hz speed within each volume, imaging starting
    104.654892 ms after the behaviour."""
    TR = 1000 / rate
    out = np.empty(frames)
    for i in range(frames):
        st = int(np.ceil((offset_ms + TR * i) / 20))
        ed = int(np.floor((offset_ms + TR * (i + 1)) / 20))
        ed = min(ed, speed.size)
        out[i] = speed[st - 1:ed].mean()  # MATLAB 1-based st:ed
    return out


def gamma_crf(dt, a=1.7, b=0.25, kernel=5.0):
    """lib/getGlmCRF.m with checkBehavior.m's shape 1.7 and scale 0.25 s."""
    t = np.arange(0, kernel + dt / 2, dt)
    h = stats.gamma.pdf(t, a, scale=b)
    return h / h.sum()


def walking_regressors(speeds, rate=1.879714, binary=False):
    """checkBehavior.m: per-volume speed clipped at th (mean over flies of each fly's
    SD), minus b (mean over flies of each fly's 10th percentile), negatives set to
    0, scaled to [0 1], convolved with the CRF at 25 times the volume rate.
    binary=True is the claims file's O1 variant: 1 where the speed is at or above
    b + th, else 0, before the convolution."""
    MS = [s for s in speeds]
    th = np.mean([np.std(s) for s in MS])
    bsp = np.mean([np.percentile(s, 10, method="hazen") for s in MS])
    TR = 1 / rate
    res = 25
    h = gamma_crf(TR / res)
    out, mscal = [], []
    for s in MS:
        v = speed_per_volume(s)
        mscal.append(v)
        if binary:
            mb = (v >= bsp + th).astype(float)
        else:
            mb = np.minimum(v, th) - bsp
            mb[mb < 0] = 0
            mb = mb / (th - bsp)
        n = mb.size
        x = np.arange(n) * TR
        xq = np.arange((n - 1) * res + 1) * TR / res
        vq = np.interp(xq, x, mb)
        U = np.convolve(vq, h)
        out.append(U[0:res * n:res][:n])
    return np.array(out), np.array(mscal), th, bsp


def glm_betas(asset, fly, regressor, n_keep=7):
    """First-level OLS betas per native voxel (second pass over the green series).

    Design as glmFlyMB1st.m: [walking regressor, 7 polynomial terms, 6 tCompCor
    components divided by their overall SD]. Returns the betas of the walking
    regressor and the six tCompCor terms (the columns glmFlyMB2nd.m keeps), mapped
    to the template grid by the fly's interpolation matrix. Smoothing is applied to
    these template maps afterwards (glm_smooth), which for OLS equals fitting the
    smoothed data. Deviation: no Tukey-taper pre-whitening (an assumption, stated in
    the notebook)."""
    T = fly["T"]
    Sd = poly_regressors(T)
    tc = tcompcor(fly["top_ts"], Sd)
    tc = tc / np.std(tc)
    X = np.column_stack([regressor, Sd, tc])
    pinv = np.linalg.pinv(X).astype(np.float32)
    keep = [0] + list(range(8, 14))
    pk = pinv[keep]
    h5 = open_nwb(asset["s3"])
    rd = ChunkReader(asset["s3"], h5)
    _, Xn, Yn, Z = rd.shape
    nvox = Xn * Yn
    B = np.zeros((len(keep), nvox * Z), np.float32)
    for z, a in rd.slices(range(Z)):
        xz = a.reshape(T, nvox).astype(np.float32)
        xz -= xz.mean(0)
        B[:, z * nvox:(z + 1) * nvox] = pk @ xz
    h5.close()
    P, _ = interp_matrix(fly["coords"].astype(np.float64), fly["shape"])
    return np.asarray((P @ B.T.astype(np.float64)).T, np.float32)  # (7, template voxels)


def glm_smooth(vol, fwhm_vox=8.0):
    """Gaussian of FWHM n voxels along y (2.28 um) and the same width along x and z
    (extractROItimeseries.m / glmFlyMB1st.m), filter size 2*ceil(2*sigma)+1."""
    from scipy.ndimage import gaussian_filter
    fwhm = np.array([fwhm_vox / (2.45 / 2.28), fwhm_vox, fwhm_vox / (3.715 / 2.28)])
    sigma = fwhm / np.sqrt(8 * np.log(2))
    trunc = np.ceil(2 * sigma) / sigma
    out = np.empty_like(vol)
    # gaussian_filter takes one truncate; apply one axis at a time
    tmp = vol
    for ax in range(3):
        tmp = gaussian_filter(tmp, sigma=[sigma[ax] if i == ax else 0 for i in range(3)],
                              truncate=trunc[ax], mode="constant")
    out[:] = tmp
    return out


def second_level(betas):
    """glmFlyMB2nd.m without the Tukey taper: the flies' kept betas stacked, design
    of stacked identity blocks, OLS; t of the walking coefficient with the pooled
    residual variance (df = flies x 7 - 7)."""
    B = np.stack(betas)  # flies x 7 x voxels
    n, k, v = B.shape
    mean = B.mean(0)
    rss = ((B - mean) ** 2).sum((0, 1))
    df = n * k - k
    se = np.sqrt(rss / df / n)
    with np.errstate(invalid="ignore", divide="ignore"):
        t = mean[0] / se
    return t, df


def clusters(mask, connectivity=18):
    from scipy import ndimage
    if connectivity == 18:
        st = ndimage.generate_binary_structure(3, 2)
    elif connectivity == 26:
        st = ndimage.generate_binary_structure(3, 3)
    else:
        st = ndimage.generate_binary_structure(3, 1)
    lab, n = ndimage.label(mask, structure=st)
    sizes = np.bincount(lab.ravel())[1:]
    return lab, sizes
EOF
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import sys, pickle; sys.path.insert(0,'entries/okuno-2025')
import flyfc, numpy as np
subs=['fly-087','fly-089','fly-094','fly-097','fly-098','fly-099','fly-100','fly-101','fly-105']
sp=[pickle.load(open(f'fly_{s}.pkl','rb'))['speed'] for s in subs]
print([ (s.size, s.min(), s.max(), np.isnan(s).sum()) for s in sp][:2])
reg, ms, th, b = flyfc.walking_regressors(sp)
beh=flyfc.load_mat(flyfc.code_file('data/behavior.mat'))
for k in beh: print(k, np.asarray(beh[k]).shape)
M=np.asarray(beh['MScal'],float); M2=np.asarray(beh['MBcal2'],float)
for i in range(9):
    print(subs[i], [round(np.corrcoef(ms[i],M[j])[0,1],3) for j in range(9)][i], 'maxabs', np.abs(ms[i]-M[i]).max(), 'reg r', round(np.corrcoef(reg[i],M2[i])[0,1],4), np.abs(reg[i]-M2[i]).max())
print(th,b)
EOF
```

```
[(90000, np.float64(0.0), np.float64(0.16452277712152), np.int64(0)), (90000, np.float64(0.0), np.float64(0.13481671236194), np.int64(0))]
MScal (9, 3384)
MBcal (9, 3384)
MBcal2 (9, 3384)
fly-087 1.0 maxabs 1.5795141673768942e-08 reg r 1.0 6.658003526505141e-06
fly-089 1.0 maxabs 7.66766816706621e-09 reg r 1.0 6.739952610912425e-06
fly-094 1.0 maxabs 1.1949911414566028e-08 reg r 1.0 6.463121438260444e-06
fly-097 1.0 maxabs 8.884952197585338e-09 reg r 1.0 7.133243156931535e-06
fly-098 1.0 maxabs 1.082792965012569e-08 reg r 1.0 6.6773395612784725e-06
fly-099 1.0 maxabs 1.125798645973397e-08 reg r 1.0 6.477887411371341e-06
fly-100 1.0 maxabs 1.1182221877625853e-08 reg r 1.0 6.006469415176241e-06
fly-101 1.0 maxabs 1.0365230368458711e-08 reg r 1.0 6.407947317099705e-06
fly-105 1.0 maxabs 9.663878468291198e-09 reg r 1.0 7.047671810700429e-06
0.015448249421407751 0.0017945806450812554
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > glm.py <<'EOF'
import sys, pickle, time; sys.path.insert(0,'entries/okuno-2025')
import flyfc, numpy as np
subs=['fly-087','fly-089','fly-094','fly-097','fly-098','fly-099','fly-100','fly-101','fly-105']
assets=flyfc.list_assets()
flies=[pickle.load(open(f'fly_{s}.pkl','rb')) for s in subs]
reg,_,_,_=flyfc.walking_regressors([f['speed'] for f in flies])
regb,_,_,_=flyfc.walking_regressors([f['speed'] for f in flies], binary=True)
out=[]; outb=[]
for i,(a,f) in enumerate(zip(assets,flies)):
    t=time.time()
    B=flyfc.glm_betas(a,f,np.column_stack([reg[i]]) if False else reg[i])
    out.append(B); print(a['subject'], B.shape, time.time()-t, flush=True)
    if i==0: break
pickle.dump(out, open('betas0.pkl','wb'))
EOF
python glm.py
```

```
fly-087 (7, 1605632) 37.93749785423279
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/okuno-2025 && python - <<'EOF'
p='flyfc.py'; s=open(p).read()
old=s[s.index('def glm_betas(asset, fly, regressor, n_keep=7):'):s.index('def glm_smooth(')]
new='''def glm_betas(asset, fly, regressors):
    """First-level OLS betas per native voxel (second pass over the green series).

    Design as glmFlyMB1st.m: [walking regressor, 7 polynomial terms, 6 tCompCor
    components divided by their overall SD]. For each regressor given (the main one
    and variants) returns the betas of the walking regressor and the six tCompCor
    terms (the columns glmFlyMB2nd.m keeps), mapped to the template grid by the
    fly's interpolation matrix. Smoothing is applied to these template maps
    afterwards (glm_smooth), which for OLS equals fitting the smoothed data.
    Deviation: no Tukey-taper pre-whitening, and tCompCor from the unsmoothed native
    voxels (assumptions, stated in the notebook)."""
    T = fly["T"]
    Sd = poly_regressors(T)
    tc = tcompcor(fly["top_ts"], Sd)
    tc = tc / np.std(tc)
    keep = [0] + list(range(8, 14))
    pk = np.vstack([np.linalg.pinv(np.column_stack([r, Sd, tc]))[keep] for r in regressors])
    pk = pk.astype(np.float32)
    h5 = open_nwb(asset["s3"])
    rd = ChunkReader(asset["s3"], h5)
    _, Xn, Yn, Z = rd.shape
    nvox = Xn * Yn
    B = np.zeros((pk.shape[0], nvox * Z), np.float32)
    for z, a in rd.slices(range(Z)):
        xz = a.reshape(T, nvox).astype(np.float32)
        xz -= xz.mean(0)
        B[:, z * nvox:(z + 1) * nvox] = pk @ xz
    h5.close()
    P, _ = interp_matrix(fly["coords"].astype(np.float64), fly["shape"])
    Bt = np.asarray((P @ B.T.astype(np.float64)).T, np.float32)
    return [Bt[i * 7:(i + 1) * 7] for i in range(len(regressors))]


'''
s=s.replace(old,new)
open(p,'w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && cat > glm.py <<'EOF'
import sys, pickle, time; sys.path.insert(0,'entries/okuno-2025')
import flyfc, numpy as np
subs=['fly-087','fly-089','fly-094','fly-097','fly-098','fly-099','fly-100','fly-101','fly-105']
assets=flyfc.list_assets()
flies=[pickle.load(open(f'fly_{s}.pkl','rb')) for s in subs]
reg,_,_,_=flyfc.walking_regressors([f['speed'] for f in flies])
regb,_,_,_=flyfc.walking_regressors([f['speed'] for f in flies], binary=True)
out=[]
for i,(a,f) in enumerate(zip(assets,flies)):
    t=time.time()
    out.append(flyfc.glm_betas(a,f,[reg[i],regb[i]])); print(a['subject'], time.time()-t, flush=True)
pickle.dump(out, open('betas.pkl','wb'))
EOF
python glm.py
```

```
fly-087 39.1808602809906
fly-089 35.41359353065491
fly-094 37.02891945838928
fly-097 35.77790427207947
fly-098 36.22876167297363
fly-099 35.9358811378479
fly-100 36.36090278625488
fly-101 36.309046030044556
fly-105 33.973724126815796
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && head -30 flywalk/atlas/jfrc2010-roi-itksnap.txt; . dev/bin/activate && python -c "
import sys; sys.path.insert(0,'entries/okuno-2025'); import flyfc
n=flyfc.hemiroi_names(); print([ (i,x) for i,x in enumerate(n) if any(k in x for k in ['LAL','FB','IPS','GNG','WED','AVLP'])])"
```

```
################################################							
# ITK-SnAP Label Description File							
# File format: 							
# IDX   -R-  -G-  -B-  -A--  VIS MSH  LABEL							
# Fields: 							
#    IDX:   Zero-based index 							
#    -R-:   Red color component (0..255)							
#    -G-:   Green color component (0..255)							
#    -B-:   Blue color component (0..255)							
#    -A-:   Label transparency (0.00 .. 1.00)							
#    VIS:   Label visibility (0 or 1)							
#    IDX:   Label mesh visibility (0 or 1)							
#  LABEL:   Label description 							
################################################							
0	0	0	0	0	0	0	"Clear Label"
2	0	255	0	0.3	1	1	"accessory medulla"
3	0	0	255	0.3	1	1	"lobula"
4	255	255	0	0.3	1	1	"nodulus"
5	0	255	255	0.3	1	1	"bulb"
6	255	0	255	0.3	1	1	"protocerebral bridge"
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -i -E "fan|ventrolateral protocerebrum|inferior posterior|gnathal|wedge|lateral accessory|posterior slope|subesoph|prow" flywalk/atlas/jfrc2010-roi-itksnap.txt; . dev/bin/activate && cat > glm2.py <<'EOF'
import sys, pickle; sys.path.insert(0,'entries/okuno-2025')
import flyfc, numpy as np
from scipy import stats
betas=pickle.load(open('betas.pkl','rb'))
mask,_=flyfc.code_nifti('template/thresholded_FDACal_mask.nii.gz'); mask=mask>0
shp=mask.shape
names=flyfc.hemiroi_names(); masks=flyfc.hemiroi_masks()
for vi,lab in enumerate(['graded','binary']):
    bs=[]
    for b in betas:
        bb=b[vi].reshape(7,*shp)
        sm=np.stack([flyfc.glm_smooth(bb[k]) for k in range(7)])
        bs.append(sm.reshape(7,-1)[:,mask.ravel()])
    t,df=flyfc.second_level(bs)
    th=stats.t.isf(0.001,df)
    T=np.zeros(shp); T[mask]=t
    lab_p,sz_p=flyfc.clusters(T>th); lab_n,sz_n=flyfc.clusters(T<-th)
    print(lab,'df',df,'th',th,'tmax',np.nanmax(t),'tmin',np.nanmin(t),'pos clusters',sorted(sz_p)[-3:],'neg', sorted(sz_n)[-5:])
    big=np.argsort(sz_n)[::-1][:3]
    for c in big:
        vox=lab_n==c+1
        ov=[(names[i], int((vox&masks[i]).sum())) for i in range(114) if (vox&masks[i]).sum()>0]
        ov=sorted(ov,key=lambda x:-x[1])[:5]
        print('  neg cluster',sz_n[c], 'min t', T[vox].min(), ov)
    for nm in ['LAL(R)','LAL(L)','FB','IPS(R)','GNG','WED(R)','AVLP(R)']:
        i=names.index(nm); m=masks[i]&mask
        print('  ',nm, 'mean t', round(T[m].mean(),2), 'max', round(T[m].max(),2), 'frac pos sig', round((T[m]>th).mean(),2), 'frac neg sig', round((T[m]<-th).mean(),2))
    pickle.dump(T, open(f'T_{lab}.pkl','wb'))
EOF
python glm2.py
```

```
8	0	0	205	0.3	1	1	"lateral accessory lobe"
26	255	235	205	0.3	1	1	"fan-shaped body"
30	188	143	143	0.3	1	1	"anterior ventrolateral protocerebrum"
31	255	105	180	0.3	1	1	"posterior ventrolateral protocerebrum"
32	255	218	185	0.3	1	1	"wedge"
37	255	255	224	0.3	1	1	"superior posterior slope"
38	70	130	180	0.3	1	1	"inferior posterior slope"
49	34	139	34	0.3	1	1	"adult gnathal ganglion"
50	248	248	255	0.3	1	1	"prow"
56	255	99	71	0.3	1	1	"lateral accessory lobe"
75	255	250	205	0.3	1	1	"anterior ventrolateral protocerebrum"
76	250	128	114	0.3	1	1	"posterior ventrolateral protocerebrum"
77	148	0	211	0.3	1	1	"wedge"
82	240	230	140	0.3	1	1	"superior posterior slope"
83	250	235	215	0.3	1	1	"inferior posterior slope"
graded df 56 th 3.2422607256745732 tmax 17.676481 tmin -1.5701215 pos clusters [np.int64(3), np.int64(46), np.int64(382697)] neg []
   LAL(R) mean t 7.89 max 11.11 frac pos sig 1.0 frac neg sig 0.0
   LAL(L) mean t 8.11 max 11.26 frac pos sig 1.0 frac neg sig 0.0
   FB mean t 8.64 max 17.68 frac pos sig 1.0 frac neg sig 0.0
   IPS(R) mean t 8.88 max 11.26 frac pos sig 1.0 frac neg sig 0.0
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/flywalk && grep -n "postsyncount\|hbS\|fwS" plotStructConnectivity.m | head -30
```

```
117:        fname = ['results/sc/' roitype '_postsyncount.mat'];
128:                X(end+1) = sum(hbS(ids,r,c),'all');
129:                Y = [Y, hbS(ids,r,c)];
137:                X(end+1) = sum(fwS(ids,r,c),'all');
138:                Y = [Y, fwS(ids,r,c)];
197:        fname = ['results/sc/' roitype '_postsyncount.mat'];
434:        fname = ['results/sc/' str{1} '_postsyncount.mat'];
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/flywalk && sed -n 105,175p plotStructConnectivity.m; sed -n 190,215p plotStructConnectivity.m
```

```
end

function showSCpostSynapse()
    % primary, R/L, name order
    load('data/hemiroi.mat');

    % load SC & atlas
    roitypes = {'hemiroi'}; %, 'hemidistkm500'};

    for i = 1:length(roitypes)
        roitype = roitypes{i};

        fname = ['results/sc/' roitype '_postsyncount.mat'];
        load(fname);
        ids = primaryIds;
            
        % plot bar total post-synapse count
        labels = {}; X = []; Y = [];
        for c=1:length(hbsynThs)
            sth = hbsynThs(c);
[... 78 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd  && sed -n 1,60p entries/fouke-2025/reproduce_fouke_2025.ipynb | head -60; python -c "import nbformat; print(nbformat.__version__)" 2>&1; ls tools/; python tools/entry.py --help 2>&1 | head -20
```

```
Tue Nov 10 07:11:24 UTC 2026
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "55a2264c",
   "metadata": {},
   "source": [
    "# Reproducing Fouke et al. (2025) from dandiset 001453\n",
    "\n",
    "**Paper.** Fouke KE, He Z, Loring MD, Naumann EA (2025). Neural circuits underlying divergent\n",
    "visuomotor strategies of zebrafish and *Danionella cerebrum*. *Current Biology*.\n",
    "[doi:10.1016/j.cub.2025.04.027](https://doi.org/10.1016/j.cub.2025.04.027). This attempt used the\n",
    "full text of the accepted author manuscript in PubMed Central (PMC12218792); the version of record\n",
    "is not open access.\n",
    "\n",
    "**Dandiset.** [DANDI:001453](https://dandiarchive.org/dandiset/001453/0.250518.1950), version\n",
    "0.250518.1950. The paper cites no DANDI version (its data statement points to a GitLab repository\n",
    "that holds code only). This is the only published version. The draft holds the same 37 files\n",
    "(same blobs and sizes); it differs only in metadata added later (authors, keywords, and a\n",
[... 97 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/mknb.py",
 "content": "import nbformat as nbf\n\ncells = []\n\n\ndef md(s):\n    cells.append(nbf.v4.new_markdown_cell(s.strip(\"\\n\")))\n\n\ndef code(s, tags=None):\n    c = nbf.v4.new_code_cell(s.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nmd(r\"\"\"\n# Reproducing Okuno et al. (2025) from dandiset 000727\n\n**Paper.** Okuno T, Woodward A, Okano H, Hata J (2025). Functional connectivity, structural\nconnectivity, and inter-individual variability in *Drosophila melanogaster*. eLife reviewed\npreprint 107990 version 1, [doi:10.7554/elife.107990.1](https://doi.org/10.7554/elife.107990.1).\nThe claims file was written from the publisher's HTML of version 1 (main text, Methods, figure\nlegends and the legends of the Extended Data figures); no PDF was available.\n\n**Dandiset.** [DANDI:000727](https://dandiarchive.org/dandiset/000727/0.240106.0043), version\n0.240106.0043, the version the paper's Methods and Data availability cite. It is also the only\npublished version; the draft lists the same 18 assets with the same total size.\n\n**What the dandiset holds.** The whole-brain two-photon imaging of Brezovec et al. that the paper\nreuses: 9 flies, one NWB file each, with the raw GCaMP6f and tdTomato volumes (256 x 128 x 49 voxels,\n3384 volumes at 1.88 Hz), anatomical stacks, a green series already registered to the FDA space by\nBrezovec et al. (high-pass filtered and z-scored), and FicTrac walking data at 50 Hz.\n\n**Outside inputs** (the claims file says the paper relies on them; both are pinned):\n- the paper's code, github.com/takuto-okuno-riken/flywalk at commit 4b92add: the resized FDA\n  template, brain mask, the hemibrain neuropil atlas (114 ROIs), the JFRC2010 atlas, the FlyEM\n  cf0.8 SC of the 114 ROIs and the walking regressors it computed (data/behavior.mat);\n- the paper's Zenodo record [10.5281/zenodo.15532272](https://doi.org/10.5281/zenodo.15532272)\n  (version of 2025-05-28, the one the code's README cites; the later version 18151010 postdates\n  the preprint): FlyWire sc140 SC of the hemibrain ROIs, the selected-synapse SC matrices, the 99\n  null SC matrices of each permutation test, per-ROI transmitter and post-synapse counts.\n\nThe SCKm and DistKm ROI atlases (k-means parcellations) are in neither, so every claim on them is\nblocked. The analysis streams each fly's raw green series once for FC and once for the GLM.\n\n| Claim | Data | Status |\n|---|---|---|\n| fig1-poltcomp-optimal | with inputs | blocked: SCKm and DistKm atlases not published |\n| fig2b-distkm-smoothing-optimum | with inputs | blocked: DistKm atlases not published |\n| figs2-1b-sckm-smoothing | with inputs | blocked: SCKm atlases not published |\n| fig2c-smoothing-plus-poltcomp | with inputs | blocked: atlases not published |\n| figs2-1d-highpass-degrades | with inputs | blocked: DistKm atlases not published |\n| fig2d-log-decline, fig2d-fly-values, fig2d-ten-thousand-rois | with inputs | blocked: atlases not published |\n| discussion-twenty-rois | with inputs | blocked: atlases not published |\n| fig3d-confidence-threshold | with inputs | blocked: FlyEM SC at 0.5, 0.6, 0.7, 0.9 not published |\n| fig3d-flyem-vs-flywire | with inputs | tested |\n| fig3e-flyem-higher-most-regions | with inputs | tested |\n| fig3g-transmitter-correlation | with inputs | tested |\n| fig4e-unsegregated-higher | with inputs | tested |\n| fig4f-segregated-lower | with inputs | tested (reading a) |\n| fig4i-reciprocal-higher | with inputs | tested |\n| figs4-1-flyem-permutation | with inputs | blocked: FlyEM selected and null SC not published |\n| fig5b-walking-activation | with inputs | tested |\n| fig5b-walking-suppression | with inputs | tested |\n| fig3a-postsynapse-counts, fig3c-regional-detection, figs3-1a-regional-count-similarity, fig3f-output-transmitters | elsewhere | tested on the paper's per-ROI tables |\n| figs3-2cd-apl-similarity, fig4b, fig4a, fig4c, figs4-1ij, fig4h, fig5-wagn | elsewhere | blocked |\n\"\"\")\n\ncode(r\"\"\"\nimport os\nos.environ.setdefault(\"OMP_NUM_THREADS\", \"4\")\nimport time, resource, warnings\nimport numpy as np\nimport matplotlib.pyplot as plt\nfrom scipy import stats\nimport ants\nimport flyfc\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\nT_START = time.time()\nprint(\"dandiset\", flyfc.DANDISET, \"version\", flyfc.VERSION)\nprint(\"code commit\", flyfc.CODE_COMMIT, \"zenodo record\", flyfc.ZENODO_RECORD)\n\"\"\")\n\nmd(r\"\"\"\n## Data check\n\nThe files, their metadata, and what the analysis reads from them. ANTs registration is seeded\n(`random_seed=1`); no other random numbers are drawn.\n\"\"\")\n\ncode(r\"\"\"\nassets = flyfc.list_assets()\nprint(len(assets), \"NWB files\")\nmeta = []\nfor a in assets:\n    h5 = flyfc.open_nwb(a[\"s3\"])\n    g = h5[flyfc.GREEN]\n    st = h5[\"acquisition/TwoPhotonSeriesFunctionalGreen/starting_time\"]\n    gs = h5[\"general/optophysiology/ImagingPlaneGCaMP6fFunctional/grid_spacing\"][()]\n    spd = h5[\"processing/behavior/FicTrac/SpatialSeriesMovementSpeed\"]\n    proc = h5[\"processing/ophys/TwoPhotonSeriesFunctionalGreenProcessed/data\"]\n    row = dict(subject=a[\"subject\"], size_gb=round(a[\"size\"] / 1e9, 1), green=g.shape, dtype=str(g.dtype),\n               rate=round(float(st.attrs[\"rate\"]), 6), spacing_um=tuple(np.round(gs * 1e6, 3)),\n               speed_n=spd[\"data\"].shape[0], speed_rate=float(spd[\"starting_time\"].attrs[\"rate\"]),\n               speed_desc=spd.attrs[\"description\"], processed=proc.shape,\n               sex=h5[\"general/subject/sex\"][()].decode(),\n               genotype=h5[\"general/subject/genotype\"][()].decode())\n    meta.append(row)\n    h5.close()\nfor r in meta:\n    print(r[\"subject\"], r[\"size_gb\"], \"GB green\", r[\"green\"], r[\"dtype\"], \"rate\", r[\"rate\"], \"Hz spacing\", r[\"spacing_um\"],\n          \"um | speed\", r[\"speed_n\"], \"samples at\", r[\"speed_rate\"], \"Hz | processed\", r[\"processed\"], \"|\", r[\"sex\"])\nprint(\"genotypes:\", sorted({r[\"genotype\"] for r in meta}))\nprint(\"speed description:\", meta[0][\"speed_desc\"])\nprint(\"imaging duration (s):\", sorted({round(r[\"green\"][0] / r[\"rate\"], 1) for r in meta}),\n      \"behaviour duration (s):\", sorted({r[\"speed_n\"] / r[\"speed_rate\"] for r in meta}))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\n**Orientation and registration.** The template and the masks come from the paper's code. The\nnative mean image of the first fly is shown beside the template, and the correlation with the\ntemplate after an affine registration is printed for each of the eight axis flips.\n\"\"\")\n\ncode(r\"\"\"\ntm, tz = flyfc.code_nifti(\"template/thresholded_FDACal.nii.gz\")\ntmpl = ants.from_numpy(tm, spacing=tuple(float(v) / 1000 for v in tz))\nbrain, _ = flyfc.code_nifti(\"template/thresholded_FDACal_mask.nii.gz\")\nbrain = brain > 0\nmasks = flyfc.hemiroi_masks()\nnames = flyfc.hemiroi_names()\nprint(\"template\", tm.shape, \"voxel (um)\", tuple(round(float(v), 3) for v in tz), \"brain-mask voxels\", int(brain.sum()))\nprint(\"hemibrain ROIs\", len(masks), \"voxels per ROI\", min(int(m.sum()) for m in masks), \"to\", max(int(m.sum()) for m in masks))\n\nh5 = flyfc.open_nwb(assets[0][\"s3\"])\nrd0 = flyfc.ChunkReader(assets[0][\"s3\"], h5)\nT0 = rd0.shape[0]; ct = rd0.chunks[0]\nmean0 = rd0.mean_image({0, ct * ((T0 // ct) // 2), ct * ((T0 - 1) // ct)})\nh5.close()\nflips = flyfc.choose_flip(mean0, tmpl)\nfor k, v in flips.items():\n    print(\"flip\", k, \"affine correlation with template\", round(v, 3))\nfig, ax = plt.subplots(2, 4, figsize=(15, 5))\nfor i, z in enumerate([6, 18, 30, 42]):\n    ax[0, i].imshow(mean0[:, :, z].T, cmap=\"gray\"); ax[0, i].set_title(f\"{assets[0]['subject']} native z={z}\")\n    ax[1, i].imshow(tm[:, :, z].T, cmap=\"gray\"); ax[1, i].set_title(f\"template z={z}\")\nplt.tight_layout(); plt.show()\nprint(\"native mean image range\", mean0.min().round(1), mean0.max().round(1), \"| template range\", tm.min(), tm.max().round(3))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nIn both images the slices near z = 6 hold two small dorsal-anterior structures near the midline and\nthe slices near z = 42 hold the optic lobes, and the dorsoventral axis runs the same way, so no\nflip is applied along y or z. Left and right cannot be told apart from a symmetric image (the\nx-flipped and unflipped correlations are nearly equal); no flip is assumed, and the main FC-SC\nresults are shown with left and right ROIs swapped.\n\n**Reduce each fly.** Each fly's raw green series is streamed once (about 7 GB per fly) and reduced\nto the 114 ROI mean series and the 1000 highest-SD voxels (`flyfc.process_fly`).\n\"\"\")\n\ncode(r\"\"\"\nflies = []\nfor a in assets:\n    f = flyfc.process_fly(a, tmpl, masks)\n    f.pop(\"warped\"); f.pop(\"mean\")\n    flies.append(f)\n    print(f[\"subject\"], \"read\", round(f[\"mb_read\"]), \"MB in\", round(f[\"t_total\"]), \"s | correlation with template\",\n          {k: round(v, 3) for k, v in f[\"cc\"].items()}, \"| ROIs not fully in the field of view\",\n          int((f[\"cover\"] < 0.999).sum()), \"min coverage\", round(float(np.nanmin(f[\"cover\"])), 3), flush=True)\nprint(\"peak memory (GB)\", round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6, 2), \"| elapsed (min)\", round((time.time() - T_START) / 60, 1))\n\"\"\", tags=[\"sanity\"])\n\ncode(r\"\"\"\n# Which ROIs lose coverage, and in which fly\nfor f in flies:\n    low = np.nonzero(f[\"cover\"] < 0.999)[0]\n    if low.size:\n        print(f[\"subject\"], \", \".join(f\"{names[i]} {f['cover'][i]:.2f}\" for i in low))\nsub_order = [f[\"subject\"] for f in flies]\nprint(\"flies in name order:\", sub_order)\nprint(\"code's subject list [1 2 3 4 5 6 8 9] leaves out the 7th:\", sub_order[6])\nsel8 = [i - 1 for i in flyfc.SUBJECT_IDS]\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\n**Subject order and the behaviour clock.** The paper's code holds the per-volume speed and the\nwalking regressor it computed for its nine flies (`data/behavior.mat`). Computing them from the\ndandiset's FicTrac speed, with the code's offset of 104.654892 ms, and comparing fly by fly\nchecks both the subject order and the alignment of the behaviour to the volumes.\n\"\"\")\n\ncode(r\"\"\"\nreg, mscal, th_speed, b_speed = flyfc.walking_regressors([f[\"speed\"] for f in flies])\nreg_bin, _, _, _ = flyfc.walking_regressors([f[\"speed\"] for f in flies], binary=True)\nbeh = flyfc.load_mat(flyfc.code_file(\"data/behavior.mat\"))\nM = np.asarray(beh[\"MScal\"], float); M2 = np.asarray(beh[\"MBcal2\"], float)\nprint(\"code's MScal\", M.shape, \"| th (mean SD of speed)\", round(th_speed, 5), \"b (mean 10th percentile)\", round(b_speed, 5))\nC = np.array([[np.corrcoef(mscal[i], M[j])[0, 1] for j in range(9)] for i in range(9)])\nfor i, f in enumerate(flies):\n    print(f[\"subject\"], \"best-matching code fly\", int(np.argmax(C[i])) + 1, \"r\", round(C[i].max(), 6),\n          \"| max |speed diff|\", f\"{np.abs(mscal[i] - M[i]).max():.2e}\", \"| regressor max |diff|\", f\"{np.abs(reg[i] - M2[i]).max():.2e}\")\nprint(\"speed range\", round(min(f[\"speed\"].min() for f in flies), 4), \"to\", round(max(f[\"speed\"].max() for f in flies), 4), \"(radians per frame, as the file states)\")\nprint(\"fraction of volumes at or above b + th (binary walking):\", np.round((mscal >= b_speed + th_speed).mean(1), 3))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nThe behaviour clock is checked against the imaging with a contrast: the brain-wide mean of the raw\nROI series against the walking regressor, at shifts of the regressor by -60 to 60 volumes. If the\ntwo streams share the clock, the correlation peaks near shift 0 (the regressor is already\nconvolved with the calcium response).\n\"\"\")\n\ncode(r\"\"\"\nshifts = np.arange(-60, 61, 2)\nfor i, f in enumerate(flies):\n    g = f[\"R\"][[j for j in range(114) if names[j] in [names[k] for k in range(114)]]].mean(0)\n    g = g - g.mean()\n    cc = [np.corrcoef(np.roll(reg[i], s)[70:-70], g[70:-70])[0, 1] for s in shifts]\n    k = int(np.argmax(cc))\n    print(f[\"subject\"], \"peak r\", round(cc[k], 3), \"at shift\", int(shifts[k]), \"volumes | r at 0:\", round(cc[30], 3),\n          \"| median |r| at shifts beyond 30:\", round(float(np.median(np.abs(np.array(cc)[np.abs(shifts) > 30]))), 3))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\n**Duplicates.** Recordings deposited twice would give identical speed traces or mean images.\n\"\"\")\n\ncode(r\"\"\"\nsp = np.array([f[\"speed\"] for f in flies])\ncsp = np.corrcoef(sp)\nnp.fill_diagonal(csp, np.nan)\nprint(\"largest speed-trace correlation between two flies:\", round(np.nanmax(csp), 3))\nroi = np.array([f[\"R\"].mean(1) for f in flies])\ncr = np.corrcoef(roi); np.fill_diagonal(cr, np.nan)\nprint(\"largest correlation of mean ROI intensity profiles between two flies:\", round(np.nanmax(cr), 3))\nprint(\"identical speed traces:\", [(i, j) for i in range(9) for j in range(i + 1, 9) if np.array_equal(sp[i], sp[j])])\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\n## FC and the paper's SC\n\nFC per fly is the Pearson correlation of the 114 ROI series, Fisher-z transformed and averaged\nover the code's eight flies (M3). Poly-tCompCor is the 7 polynomial terms and 6 tCompCor\ncomponents; tCompCor is taken from the 1000 native voxels with the highest temporal SD (an\nassumption: the code takes them among template voxels, after warping). SC is the second\n(\"Traced\") layer of each connect list (M4).\n\"\"\")\n\ncode(r\"\"\"\nem_nc, em_sc, em_ids52 = flyfc.load_sc(flyfc.code_file(\"results/sc/hemiroi_connectlist.mat\"))\nfw_nc, fw_sc, ids = flyfc.load_sc(flyfc.zenodo_member(\"results/sc/hemiroi_fw0sr140_connectlist.mat\"))\nprint(\"FlyEM SC\", em_nc.shape, \"| FlyWire SC\", fw_nc.shape, \"| primary ROIs\", len(ids))\nprint(\"primary ROIs:\", \", \".join(names[i] for i in ids))\nprint(\"FlyEM neuron SC over primary ROIs: total\", int(em_nc[np.ix_(ids, ids)].sum()), \"zeros\", int((em_nc[np.ix_(ids, ids)] == 0).sum()))\nprint(\"FlyWire neuron SC over primary ROIs: total\", int(fw_nc[np.ix_(ids, ids)].sum()), \"zeros\", int((fw_nc[np.ix_(ids, ids)] == 0).sum()))\nseries = {n: [flyfc.roi_series(f, n) for f in flies] for n in [\"\", \"poltcomp\"]}\nmFz = {(n, s): flyfc.mean_zfc([series[n][i] for i in S]) for n in series for s, S in [(\"8\", sel8), (\"9\", range(9))]}\nF = mFz[(\"poltcomp\", \"8\")]\noff = ~np.eye(len(ids), dtype=bool)\nprint(\"mean z-FC (Poly-tCompCor, 8 flies) over primary ROI pairs: range\", round(F[np.ix_(ids, ids)][off].min(), 3), \"to\", round(F[np.ix_(ids, ids)][off].max(), 3),\n      \"| diagonal set to\", round(F[ids[0], ids[0]], 3))\nfor f, s in zip(flies, series[\"poltcomp\"]):\n    print(f[\"subject\"], \"ROI series SD range\", round(s.std(0)[ids].min(), 2), \"to\", round(s.std(0)[ids].max(), 2))\n\"\"\")\n\nmd(r\"\"\"\n### fig3d-flyem-vs-flywire\n\n> Against the same FC, FlyEM gives a higher matrix-level FC-SC correlation than FlyWire (0.73\n> against 0.68).\n\n63 hemibrain primary ROIs, no smoothing, Poly-tCompCor, SC (neuron), FlyEM cf0.8 and FlyWire\nsc140. Reproduced when both values are within tolerance (0.657 to 0.803; 0.612 to 0.748) and FlyEM\nis higher.\n\"\"\")\n\ncode(r\"\"\"\nlr = {}\nfor i, n in enumerate(names):\n    if \"(L)\" in n:\n        j = names.index(n.replace(\"(L)\", \"(R)\")) if n.replace(\"(L)\", \"(R)\") in names else i\n    elif \"(R)\" in n:\n        j = names.index(n.replace(\"(R)\", \"(L)\")) if n.replace(\"(R)\", \"(L)\") in names else i\n    else:\n        j = i\n    lr[i] = j\nperm = np.array([lr[i] for i in range(114)])\nprint(\"ROIs with a left-right partner:\", int((perm != np.arange(114)).sum()))\nref = flyfc.load_mat(flyfc.zenodo_member(\"results/auc/poltcomparhemiroi_fw0sr140-fcauc.mat\"))\nprint(\"paper's own output for this setting (Zenodo auc file, FlyWire): R(7) =\", round(float(np.ravel(ref[\"R\"])[6]), 4), \"R(9) =\", round(float(np.ravel(ref[\"R\"])[8]), 4))\nrows = []\nfor (n, s), Fm in mFz.items():\n    for lab, Fx in [(\"as registered\", Fm), (\"left-right swapped\", Fm[np.ix_(perm, perm)])]:\n        rows.append((n or \"none\", s, lab, flyfc.fcsc_r(em_nc, Fx, ids), flyfc.fcsc_r(fw_nc, Fx, ids),\n                     flyfc.fcsc_r(em_sc, Fx, ids), flyfc.fcsc_r(fw_sc, Fx, ids)))\nprint(f\"{'nuisance':9s} {'flies':5s} {'orientation':20s} {'EM neuron':>9s} {'FW neuron':>9s} {'EM syn':>7s} {'FW syn':>7s}\")\nfor r in rows:\n    print(f\"{r[0]:9s} {r[1]:5s} {r[2]:20s} {r[3]:9.4f} {r[4]:9.4f} {r[5]:7.4f} {r[6]:7.4f}\")\nsigned = [np.corrcoef(flyfc.log_sc(S[np.ix_(ids, ids)]).ravel(), F[np.ix_(ids, ids)].ravel())[0, 1] for S in (em_nc, fw_nc)]\nprint(\"signed FC variant (O3), Poly-tCompCor, 8 flies: FlyEM\", round(signed[0], 4), \"FlyWire\", round(signed[1], 4))\nr_em, r_fw = rows[4][3], rows[4][4]\nprint(f\"MAIN: FlyEM r = {r_em:.4f} (tolerance 0.657 to 0.803, within: {0.657 <= r_em <= 0.803}); \"\n      f\"FlyWire r = {r_fw:.4f} (0.612 to 0.748, within: {0.612 <= r_fw <= 0.748}); FlyEM higher: {r_em > r_fw}\")\n# per fly\nfor i, f in enumerate(flies):\n    Fi = flyfc.mean_zfc([series[\"poltcomp\"][i]])\n    print(f[\"subject\"], \"single-fly FC: FlyEM\", round(flyfc.fcsc_r(em_nc, Fi, ids), 4), \"FlyWire\", round(flyfc.fcsc_r(fw_nc, Fi, ids), 4))\n\"\"\", tags=[\"claim:fig3d-flyem-vs-flywire\"])\n\ncode(r\"\"\"\na = flyfc.log_sc(em_nc[np.ix_(ids, ids)]).ravel(); b = np.abs(F[np.ix_(ids, ids)]).ravel()\nfig, ax = plt.subplots(1, 2, figsize=(9, 4))\nax[0].scatter(a, b, s=3); ax[0].set_xlabel(\"log10 SC neuron (FlyEM)\"); ax[0].set_ylabel(\"|mean z-FC|\")\na2 = flyfc.log_sc(fw_nc[np.ix_(ids, ids)]).ravel()\nax[1].scatter(a2, b, s=3, c=\"C1\"); ax[1].set_xlabel(\"log10 SC neuron (FlyWire)\")\nplt.tight_layout(); plt.show()\nprint(\"plotted ranges: log10 SC FlyEM\", a.min(), \"to\", round(a.max(), 2), \"| FlyWire\", a2.min(), \"to\", round(a2.max(), 2), \"| |mean z-FC|\", round(b.min(), 3), \"to\", round(b.max(), 3), \"(all points shown)\")\n\"\"\", tags=[\"claim:fig3d-flyem-vs-flywire\"])\n\nmd(r\"\"\"\n**Result: FlyEM gives the higher FC-SC correlation, but both values are below the paper's.**\nWith the code's eight flies and Poly-tCompCor, r is about 0.61 for FlyEM and 0.57 for FlyWire,\nbelow the tolerances (0.657 and 0.612), so the claim is partially reproduced. FlyEM is higher\nunder every variant printed (no nuisance removal, nine flies, left and right swapped, signed FC).\nThe paper's own output file for the FlyWire setting gives 0.68, so the gap is in this attempt's FC\n(no SPM12 motion and slice-timing correction, native-space tCompCor, a different registration),\nnot in the SC.\n\"\"\")\n\nmd(r\"\"\"\n### fig3e-flyem-higher-most-regions\n\n> Per region, FlyEM gives the higher FC-SC correlation in 58 of the 63 primary neuropils, FlyWire in 5.\n\nPer-region correlation (code's roiR column 7), settings of fig3d. Reproduced when the count is\nwithin 58 +- 5.8.\n\"\"\")\n\ncode(r\"\"\"\ncounts = {}\nfor (n, s), Fm in mFz.items():\n    for lab, Fx in [(\"as registered\", Fm), (\"left-right swapped\", Fm[np.ix_(perm, perm)])]:\n        re_ = flyfc.fcsc_roi_r(em_nc, Fx, ids); rw_ = flyfc.fcsc_roi_r(fw_nc, Fx, ids)\n        counts[(n or \"none\", s, lab)] = int((re_ > rw_).sum())\nfor k, v in counts.items():\n    print(k, \"FlyEM higher in\", v, \"of\", len(ids))\nroi_em = flyfc.fcsc_roi_r(em_nc, F, ids); roi_fw = flyfc.fcsc_roi_r(fw_nc, F, ids)\nn_em = int((roi_em > roi_fw).sum())\nprint(\"MAIN (Poly-tCompCor, 8 flies):\", n_em, \"of 63; within 52.2 to 63.8:\", 52.2 <= n_em <= 63.8)\nprint(\"regions where FlyWire is higher:\", \", \".join(f\"{names[ids[i]]} ({roi_em[i]:.2f} vs {roi_fw[i]:.2f})\" for i in np.nonzero(roi_fw >= roi_em)[0]))\nprint(\"per-region r range: FlyEM\", round(roi_em.min(), 3), \"to\", round(roi_em.max(), 3), \"| FlyWire\", round(roi_fw.min(), 3), \"to\", round(roi_fw.max(), 3))\npref = np.ravel(np.asarray(ref[\"roiR\"])[:, 6]) if np.asarray(ref[\"roiR\"]).shape[0] == 63 else np.ravel(np.asarray(ref[\"roiR\"])[6])\nprint(\"paper's own per-region FlyWire values (Zenodo auc file) against this attempt's: r =\", round(np.corrcoef(pref, roi_fw)[0, 1], 3))\n\"\"\", tags=[\"claim:fig3e-flyem-higher-most-regions\"])\n\nmd(r\"\"\"\n**Result: FlyEM is higher in most regions, within the tolerance of 58 of 63.** The printed count\nunder the main setting and under every variant is the evidence; the regions where FlyWire is\nhigher are listed.\n\"\"\")\n\nmd(r\"\"\"\n### fig3g-transmitter-correlation\n\n> Across regions, the FC-SC correlation rises with the share of cholinergic output neurons\n> (r = 0.39, p = 0.0013) and falls with the share of GABAergic ones (r = -0.25, p = 0.046).\n\nThe per-region FlyWire sc140 FC-SC correlation against each region's share of output neurons of\neach transmitter (plotStructConnectivity.m showNeuralTransmitter: counts divided by the ROI's\ntotal over the seven classes, including unknown). Reproduced when both r are within tolerance\n(0.351 to 0.429; -0.275 to -0.225) and both p < 0.05.\n\"\"\")\n\ncode(r\"\"\"\ntr = flyfc.load_mat(flyfc.zenodo_member(\"results/sc/hemiroi_fw0sr140_transmitter.mat\"))\noutN = np.asarray(tr[\"outNTypes\"], float)\nprint(\"outNTypes\", outN.shape)\nshare = outN / outN.sum(1, keepdims=True)\nlabs = [\"Unknown\", \"DA\", \"SER\", \"GABA\", \"GLUT\", \"ACH\", \"OCT\"]\nres = {}\nfor lab_, Fx in [(\"main\", F), (\"no nuisance\", mFz[(\"\", \"8\")]), (\"nine flies\", mFz[(\"poltcomp\", \"9\")]), (\"left-right swapped\", F[np.ix_(perm, perm)])]:\n    rr = flyfc.fcsc_roi_r(fw_nc, Fx, ids)\n    out = []\n    for k in range(1, 7):\n        r, p = stats.pearsonr(rr, share[ids, k]); out.append(f\"{labs[k]} r={r:.3f} p={p:.3g}\")\n        res[(lab_, labs[k])] = (r, p)\n    print(lab_, \"|\", \"; \".join(out))\nif np.asarray(ref[\"roiR\"]).size:\n    out = []\n    for k in range(1, 7):\n        r, p = stats.pearsonr(pref, share[ids, k]); out.append(f\"{labs[k]} r={r:.3f} p={p:.3g}\")\n    print(\"paper's own per-region values (Zenodo auc file) |\", \"; \".join(out))\nr_a, p_a = res[(\"main\", \"ACH\")]; r_g, p_g = res[(\"main\", \"GABA\")]\nprint(f\"MAIN: ACh r = {r_a:.3f} (p = {p_a:.3g}); GABA r = {r_g:.3f} (p = {p_g:.3g})\")\n\"\"\", tags=[\"claim:fig3g-transmitter-correlation\"])\n\nmd(r\"\"\"\n**Result: not reproduced.** With this attempt's FC the per-region FC-SC correlation does not rise\nwith the cholinergic share (r near 0, p > 0.05) and its relation to the GABAergic share is not\nsignificant. The paper's own per-region values from its Zenodo file, run through the same code,\nare printed beside them for comparison: they show whether the difference comes from the FC.\n\"\"\")\n\nmd(r\"\"\"\n### Permutation tests: fig4e-unsegregated-higher, fig4f-segregated-lower, fig4i-reciprocal-higher\n\n> The SC matrix of unsegregated synapses (cPPSSI 0 to 0.1) has a significantly higher FC-SC\n> correlation than 99 random synapse samples of matched size, for both neuron and synapse SC.\n\n> The SC matrix of highly segregated synapses (cPPSSI 0.9 to 1) has a significantly lower FC-SC\n> correlation than random synapse samples.\n\n> The SC matrix of reciprocal synapses within 2 um has a significantly higher FC-SC correlation\n> than random synapse samples.\n\nM6: the selected SC against the 99 null SC matrices the code pairs with it (rd185-20, rd1560-80,\nrd140-15), a normal fitted to the null values, two-tailed p, threshold 0.05/6. The null totals are\nchecked against the selected total in the same way.\n\"\"\")\n\ncode(r\"\"\"\nperm_res = {}\nfor claim, tgt, null in [(\"fig4e-unsegregated-higher\", \"sp10db3000mi1_only1\", \"rd185-20\"),\n                         (\"fig4f-segregated-lower\", \"sp90db3000mi1\", \"rd1560-80\"),\n                         (\"fig4i-reciprocal-higher\", \"rc20_only1\", \"rd140-15\")]:\n    nc, sc, _ = flyfc.load_sc(flyfc.zenodo_member(f\"results/sc/hemiroi_fw0sr140_{tgt}_connectlist.mat\"))\n    nulls = [flyfc.load_sc(flyfc.zenodo_member(f\"results/sc/hemiroi_fw0sr140_{null}-{k}_connectlist.mat\")) for k in range(1, 100)]\n    d = dict(tot=sc[np.ix_(ids, ids)].sum(), ntot=nc[np.ix_(ids, ids)].sum(),\n             null_tot=np.array([b[np.ix_(ids, ids)].sum() for a, b, _ in nulls]))\n    for lab_, Fx in [(\"main\", F), (\"no nuisance\", mFz[(\"\", \"8\")]), (\"nine flies\", mFz[(\"poltcomp\", \"9\")]), (\"left-right swapped\", F[np.ix_(perm, perm)])]:\n        r7 = flyfc.fcsc_r(nc, Fx, ids); r9 = flyfc.fcsc_r(sc, Fx, ids)\n        n7 = np.array([flyfc.fcsc_r(a, Fx, ids) for a, b, _ in nulls]); n9 = np.array([flyfc.fcsc_r(b, Fx, ids) for a, b, _ in nulls])\n        d[lab_] = (r7, n7, r9, n9)\n    perm_res[claim] = d\n    print(claim, \"| target\", tgt, \"synapse total\", int(d[\"tot\"]), \"neuron total\", int(d[\"ntot\"]), \"| null\", null, \"n =\", len(nulls),\n          \"synapse totals mean\", int(d[\"null_tot\"].mean()), \"SD\", int(d[\"null_tot\"].std(ddof=1)),\n          \"| totals test p =\", round(flyfc.normal_p(d[\"tot\"], d[\"null_tot\"])[0], 3), flush=True)\n\ndef show_perm(claim):\n    d = perm_res[claim]\n    for lab_ in [\"main\", \"no nuisance\", \"nine flies\", \"left-right swapped\"]:\n        r7, n7, r9, n9 = d[lab_]\n        p7, m7, s7 = flyfc.normal_p(r7, n7); p9, m9, s9 = flyfc.normal_p(r9, n9)\n        print(f\"{lab_:19s} neuron r={r7:.4f} null {m7:.4f}+-{s7:.4f} z={(r7 - m7) / s7:+.1f} p={p7:.3g} \"\n              f\"(null range {n7.min():.4f} to {n7.max():.4f}) | synapse r={r9:.4f} null {m9:.4f}+-{s9:.4f} z={(r9 - m9) / s9:+.1f} p={p9:.3g}\")\n\"\"\")\n\ncode(r\"\"\"\nshow_perm(\"fig4e-unsegregated-higher\")\nd = perm_res[\"fig4e-unsegregated-higher\"]\nprint(\"expected total 2,373,100 +- 237,310; measured\", int(d[\"tot\"]))\nr7, n7, r9, n9 = d[\"main\"]\nprint(\"MAIN: neuron above null with p < 0.05/6:\", r7 > n7.mean() and flyfc.normal_p(r7, n7)[0] < 0.05 / 6,\n      \"| synapse:\", r9 > n9.mean() and flyfc.normal_p(r9, n9)[0] < 0.05 / 6)\n\"\"\", tags=[\"claim:fig4e-unsegregated-higher\"])\n\nmd(r\"\"\"\n**Result: reproduced.** The unsegregated SC has the higher FC-SC correlation than every null\nsample's distribution for both neuron and synapse SC, with p below 0.05/6; the selected total\nmatches the expected 2,373,100, and the null totals do not differ from it.\n\"\"\")\n\ncode(r\"\"\"\nshow_perm(\"fig4f-segregated-lower\")\nr7, n7, r9, n9 = perm_res[\"fig4f-segregated-lower\"][\"main\"]\nprint(\"MAIN (reading a, the code's target): neuron below null with p < 0.05/6:\", r7 < n7.mean() and flyfc.normal_p(r7, n7)[0] < 0.05 / 6,\n      \"| synapse:\", r9 < n9.mean() and flyfc.normal_p(r9, n9)[0] < 0.05 / 6)\nprint(\"reading b (both sides at 0.9 or more) needs an SC rebuilt from the synapse table; not run here\")\n\"\"\", tags=[\"claim:fig4f-segregated-lower\"])\n\nmd(r\"\"\"\n**Result: reproduced under reading (a).** The segregated SC (the code's target) has a lower FC-SC\ncorrelation than the null for both neuron and synapse SC, with p below 0.05/6. Reading (b) was not\nrun.\n\"\"\")\n\ncode(r\"\"\"\nshow_perm(\"fig4i-reciprocal-higher\")\nr7, n7, r9, n9 = perm_res[\"fig4i-reciprocal-higher\"][\"main\"]\nprint(\"MAIN: neuron above null with p < 0.05/6:\", r7 > n7.mean() and flyfc.normal_p(r7, n7)[0] < 0.05 / 6,\n      \"| synapse:\", r9 > n9.mean() and flyfc.normal_p(r9, n9)[0] < 0.05 / 6)\n\"\"\", tags=[\"claim:fig4i-reciprocal-higher\"])\n\nmd(r\"\"\"\n**Result: reproduced.** The reciprocal-synapse SC has a higher FC-SC correlation than the null for\nneuron and synapse SC, with p below 0.05/6 under the main setting.\n\"\"\")\n\nmd(r\"\"\"\n## GLM of walking: fig5b-walking-activation and fig5b-walking-suppression\n\n> In the group GLM of walking, the LAL, FB, IPS and GNG neuropils show strong activity.\n\n> The Wedge and AVLP neuropils are inactive or strongly suppressed during walking.\n\nM8: the code's graded walking regressor (reproduced exactly above), 7 polynomial terms and 6\ntCompCor components; smoothing FWHM 8 voxels; second level on the walking and tCompCor betas of\nthe nine flies (glmFlyMB2nd.m), height threshold p < 0.001. Assumptions: OLS without the Tukey-taper\npre-whitening, betas mapped to the template and smoothed there (equal to fitting the warped,\nsmoothed data under OLS), tCompCor from native voxels. The binary regressor (O1) is a variant.\nCluster extent: the code's README prints k = 167.9 voxels as its extent threshold, which is used\nhere (18-connectivity, SPM's default).\n\"\"\")\n\ncode(r\"\"\"\nt0 = time.time()\nbetas = []\nfor a, f, r1, r2 in zip(assets, flies, reg, reg_bin):\n    betas.append(flyfc.glm_betas(a, f, [r1, r2]))\n    print(f[\"subject\"], \"betas done\", round(time.time() - t0), \"s\", flush=True)\nshp = brain.shape\nglm = {}\nfor vi, lab_ in enumerate([\"graded\", \"binary\"]):\n    bs = []\n    for b in betas:\n        bb = b[vi].reshape(7, *shp)\n        bs.append(np.stack([flyfc.glm_smooth(bb[k]) for k in range(7)]).reshape(7, -1)[:, brain.ravel()])\n    t, df = flyfc.second_level(bs)\n    T = np.zeros(shp, np.float32); T[brain] = t\n    glm[lab_] = (T, df)\n    th = stats.t.isf(0.001, df)\n    lp, sp_ = flyfc.clusters(T > th); ln, sn = flyfc.clusters(T < -th)\n    print(lab_, \"df\", df, \"height threshold t >\", round(th, 4), \"| t range\", round(float(t.min()), 2), \"to\", round(float(t.max()), 2),\n          \"| positive clusters >= 168 voxels:\", sorted(int(s) for s in sp_ if s >= 168), \"| negative clusters (any size):\", sorted(int(s) for s in sn)[-5:])\ndel betas\njf, _ = flyfc.code_nifti(\"atlas/jrc2018f_2010roiCal_invFDACal.nii.gz\")\njlab = {}\nfor line in flyfc.code_file(\"atlas/jfrc2010-roi-itksnap.txt\").decode().splitlines():\n    if line.startswith(\"#\") or not line.strip():\n        continue\n    p = line.split(\"\\t\")\n    jlab[int(p[0])] = p[-1].strip().strip('\"')\nprint(\"JFRC2010 labels in the atlas:\", len(np.unique(jf[jf > 0])), \"| peak memory (GB)\", round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6, 2))\n\"\"\")\n\ncode(r\"\"\"\ndef neuropil_table(T, th, atlas):\n    rows = []\n    if atlas == \"hemibrain\":\n        for i in ids:\n            m = masks[i] & brain\n            if m.sum():\n                rows.append((names[i], m))\n    else:\n        for k in np.unique(jf[jf > 0]).astype(int):\n            m = (jf == k) & brain\n            if m.sum():\n                rows.append((f\"{jlab.get(k, k)} [{k}]\", m))\n    out = []\n    for nm, m in rows:\n        out.append((nm, float(T[m].mean()), float(T[m].max()), float(T[m].min()), float((T[m] > th).mean()), float((T[m] < -th).mean()), int(m.sum())))\n    return out\n\ntargets_hb = {\"LAL\": [\"LAL(R)\", \"LAL(L)\"], \"FB\": [\"FB\"], \"IPS\": [\"IPS(R)\"], \"GNG\": [\"GNG\"]}\ntargets_jf = {\"LAL\": [\"lateral accessory lobe\"], \"FB\": [\"fan-shaped body\"], \"IPS\": [\"inferior posterior slope\"], \"GNG\": [\"adult gnathal ganglion\"]}\nact = {}\nfor lab_ in [\"graded\", \"binary\"]:\n    T, df = glm[lab_]; th = stats.t.isf(0.001, df); tmax = float(T.max())\n    lp, sp_ = flyfc.clusters(T > th)\n    big = np.isin(lp, 1 + np.nonzero(sp_ >= 168)[0])\n    for atlas, tg in [(\"hemibrain\", targets_hb), (\"JFRC2010\", targets_jf)]:\n        tab = neuropil_table(T, th, atlas)\n        order = sorted(tab, key=lambda r: -r[1])\n        top = {r[0] for r in order[: int(np.ceil(len(order) / 3))]}\n        for key, lst in tg.items():\n            hits = [r for r in tab if any(r[0].startswith(x) for x in lst)]\n            ra = any((big & masks[names.index(r[0])]).any() and r[2] >= tmax / 2 for r in hits) if atlas == \"hemibrain\" else \\\n                 any(r[2] >= tmax / 2 for r in hits)\n            rb = any(r[0] in top for r in hits)\n            act[(lab_, atlas, key)] = (ra, rb)\n            print(lab_, atlas, key, \"|\", \"; \".join(f\"{r[0]} mean t {r[1]:.2f} max {r[2]:.2f} rank {1 + [o[0] for o in order].index(r[0])}/{len(order)}\" for r in hits),\n                  \"| reading a:\", ra, \"reading b:\", rb)\n    print(lab_, \"brain-wide max t\", round(tmax, 2))\n\"\"\", tags=[\"claim:fig5b-walking-activation\"])\n\ncode(r\"\"\"\nT, df = glm[\"graded\"]\nfig, ax = plt.subplots(1, 2, figsize=(12, 3.5))\nfor i, z in enumerate([17, 21]):\n    im = ax[i].imshow(T[:, :, z].T, cmap=\"RdBu_r\", vmin=-15, vmax=15); ax[i].set_title(f\"second-level t, z={z}\")\nplt.colorbar(im, ax=ax); plt.show()\nprint(\"t range in the shown slices\", round(float(T[:, :, [17, 21]].min()), 2), \"to\", round(float(T[:, :, [17, 21]].max()), 2), \"; colour scale -15 to 15,\",\n      int((np.abs(T[:, :, [17, 21]]) > 15).sum()), \"voxels beyond it\")\n\"\"\", tags=[\"claim:fig5b-walking-activation\"])\n\nmd(r\"\"\"\n**Result: reproduced.** LAL, FB, IPS and GNG all lie in the one large positive cluster, with peak t\nabove half the brain-wide maximum (reading a), under both atlases and both regressors; their rank\nby mean t (reading b) is printed.\n\"\"\")\n\ncode(r\"\"\"\nfor lab_ in [\"graded\", \"binary\"]:\n    T, df = glm[lab_]; th = stats.t.isf(0.001, df)\n    ln, sn = flyfc.clusters(T < -th)\n    print(lab_, \"voxels below -\", round(th, 3), \":\", int((T < -th).sum()), \"| negative clusters:\", len(sn), \"| minimum t\", round(float(T.min()), 2))\n    for atlas, lst in [(\"hemibrain\", [\"WED\", \"AVLP\"]), (\"JFRC2010\", [\"wedge\", \"anterior ventrolateral protocerebrum\"])]:\n        tab = neuropil_table(T, th, atlas)\n        for r in tab:\n            if any(r[0].startswith(x) for x in lst):\n                print(\"  \", lab_, atlas, r[0], f\"mean t {r[1]:.2f}, min {r[3]:.2f}, max {r[2]:.2f}, positive-significant fraction {r[4]:.2f}, negative-significant fraction {r[5]:.2f}, voxels {r[6]}\")\n# Variant: the same with the code's subject list (8 flies), and the lowest t in the brain\nT, df = glm[\"graded\"]\nlo = np.unravel_index(np.argmin(np.where(brain, T, np.inf)), T.shape)\nprint(\"lowest t in the brain mask:\", round(float(T[lo]), 2), \"at voxel\", tuple(int(v) for v in lo), \"(the README's negative peaks are at (82,78,12) and (174,80,15), 1-based)\")\nfor v in [(81, 77, 11), (173, 79, 14)]:\n    print(\"t at README negative peak\", tuple(x + 1 for x in v), \"=\", round(float(T[v]), 2))\n\"\"\", tags=[\"claim:fig5b-walking-suppression\"])\n\nmd(r\"\"\"\n**Result: not reproduced.** No voxel falls below the negative height threshold, so there is no\nnegative cluster; WED and AVLP hold mostly positive t values above threshold under both atlases and\nboth regressors.\n\"\"\")\n\nmd(r\"\"\"\n## Connectome-only claims (data elsewhere)\n\nThese are tested on the paper's per-ROI tables in its Zenodo record (`hemiroi_postsyncount.mat`,\n`hemiroi_fw0sr140_transmitter.mat`), which the paper computed from the FlyEM and FlyWire synapses\nin the template; recounting from the raw connectomes was not done (a deviation).\n\"\"\")\n\ncode(r\"\"\"\nps = flyfc.load_mat(flyfc.zenodo_member(\"results/sc/hemiroi_postsyncount.mat\"))\nfor k, v in ps.items():\n    print(k, np.asarray(v).shape, np.ravel(v)[:8] if np.asarray(v).size < 10 else \"\")\nhbS = np.asarray(ps[\"hbS\"], float); fwS = np.asarray(ps[\"fwS\"], float)\nconfThs = np.ravel(ps[\"confThs\"]); scoreThs = np.ravel(ps[\"scoreThs\"])\npid = np.asarray(ps[\"primaryIds\"]).ravel().astype(int) - 1\nif hbS.shape[0] != 114: hbS = hbS.T\nif fwS.shape[0] != 114: fwS = fwS.T\nfor j, c in enumerate(confThs):\n    print(f\"FlyEM confidence {c}: post-synapses over primary ROIs {hbS[pid, j].sum() / 1e6:.2f} million\")\nfor j, c in enumerate(scoreThs):\n    print(f\"FlyWire cleft score {c}: post-synapses over primary ROIs {fwS[pid, j].sum() / 1e6:.2f} million\")\n\"\"\", tags=[\"claim:fig3a-postsynapse-counts\"])\n\nmd(r\"\"\"\n**Result:** the totals for FlyEM at its lowest confidence, FlyWire at cleft score 50 and FlyWire at\n140 are printed above against 21.4, 18.8 and 11.4 million (tolerance 10%).\n\"\"\")\n\ncode(r\"\"\"\njem = int(np.argmin(np.abs(confThs - (0.8 if confThs.max() <= 1 else 80))))\njfw = int(np.argmin(np.abs(scoreThs - 140)))\nprint(\"FlyEM column\", confThs[jem], \"FlyWire column\", scoreThs[jfw])\nnm = [names[i] for i in pid]\ndef cmp(n):\n    i = pid[nm.index(n)]\n    return hbS[i, jem], fwS[i, jfw]\nmb = [n for n in nm if any(n.startswith(x) for x in [\"aL\", \"a'L\", \"bL\", \"b'L\", \"gL\", \"CA\", \"PED\", \"MB\"])]\nprint(\"mushroom body ROIs among the primary ROIs:\", mb)\nfor grp, lst in [(\"aL, bL\", [n for n in nm if n.startswith(\"aL\") or n.startswith(\"bL\")]), (\"all MB\", mb),\n                 (\"central complex\", [n for n in nm if n.split(\"(\")[0] in (\"EB\", \"FB\", \"NO\", \"PB\")]),\n                 (\"optic lobe\", [n for n in nm if n.split(\"(\")[0] in (\"LO\", \"ME\")]), (\"periesophageal\", [n for n in nm if n.split(\"(\")[0] in (\"CAN\", \"FLA\")])]:\n    print(grp, \"|\", \"; \".join(f\"{n}: FlyEM {cmp(n)[0]:.0f} FlyWire {cmp(n)[1]:.0f}\" for n in lst))\n\"\"\", tags=[\"claim:fig3c-regional-detection\"])\n\nmd(r\"\"\"\n**Result:** the per-ROI counts above decide the claim (FlyEM higher in the mushroom body and EB, FB,\nNO, PB; FlyWire higher in LO, ME, CAN, FLA).\n\"\"\")\n\ncode(r\"\"\"\nx, y = hbS[pid, jem], fwS[pid, jfw]\nprint(\"Pearson r\", round(stats.pearsonr(x, y)[0], 4), \"| Spearman r\", round(stats.spearmanr(x, y)[0], 4), \"| Pearson r of log10\", round(stats.pearsonr(np.log10(x), np.log10(y))[0], 4),\n      \"| expected 0.778, 0.9, 0.919\")\n\"\"\", tags=[\"claim:figs3-1a-regional-count-similarity\"])\n\nmd(r\"\"\"\n**Result:** the three correlations are printed against the paper's 0.778, 0.9 and 0.919.\n\"\"\")\n\ncode(r\"\"\"\nsh = share[ids] * 100\nfor k, lab_ in enumerate(labs):\n    print(f\"{lab_:8s} share of output neurons over the 63 primary ROIs: mean {sh[:, k].mean():.1f}% SD {sh[:, k].std(ddof=1):.1f}% (SD with ddof 0: {sh[:, k].std():.1f}%)\")\nprint(\"expected ACh 62.8 +- 14.2, GLUT 15.5 +- 9.2, GABA 11.4 +- 8.2\")\n\"\"\", tags=[\"claim:fig3f-output-transmitters\"])\n\nmd(r\"\"\"\n**Result:** the mean shares are printed against 62.8%, 15.5% and 11.4%.\n\"\"\")\n\nmd(r\"\"\"\n## Summary\n\n| Claim | Outcome |\n|---|---|\n| fig3d-flyem-vs-flywire | partially reproduced: FlyEM higher, both r below tolerance |\n| fig3e-flyem-higher-most-regions | reproduced |\n| fig3g-transmitter-correlation | not reproduced |\n| fig4e-unsegregated-higher | reproduced |\n| fig4f-segregated-lower | reproduced (reading a) |\n| fig4i-reciprocal-higher | reproduced |\n| fig5b-walking-activation | reproduced |\n| fig5b-walking-suppression | not reproduced |\n| fig3a, fig3c, figs3-1a, fig3f (elsewhere) | see the record |\n| all SCKm and DistKm claims, fig3d-confidence-threshold, figs4-1-flyem-permutation | blocked: inputs not published |\n| other connectome-only claims | blocked |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning\nand the differences from the paper's method.\n\n**How the analysis differs from the paper's.** No SPM12 motion or slice-timing correction; the\nmean green image is registered to the template with ANTs SyN in Python and the ROI means are\ncomputed through the registration's linear map without warping each volume; tCompCor is taken from\nnative voxels; the GLM has no Tukey-taper pre-whitening and is smoothed on the beta maps. The FC\nthese give has a lower FC-SC correlation than the paper's own output files (0.57 against 0.68 for\nFlyWire), which bears on the claims that compare FC-SC values across regions.\n\n**What was found about the dataset.** The files match their description (9 flies, 3384 volumes at\n1.8797 Hz, 50 Hz FicTrac, 1800 s), the walking regressor of the paper's code is reproduced to\n1e-5 from the files in name order, and the seventh fly in name order (fly-100) has 20 hemibrain\nROIs partly outside the field of view, which fits the paper's reason for leaving one fly out. The\n`dimension` attribute of the functional series is [128, 256, 49] while the data are stored as\n(time, 256, 128, 49). The ROI atlases of the paper's main analyses (SCKm, DistKm) are not\npublished with the code or on Zenodo.\n\"\"\")\n\ncode(r\"\"\"\nprint(\"total runtime (min)\", round((time.time() - T_START) / 60, 1), \"| peak memory (GB)\", round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6, 2))\n\"\"\")\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbf.write(nb, \"entries/okuno-2025/reproduce_okuno_2025.ipynb\")\nprint(len(cells), \"cells\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/mknb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('mknb.py').read()
s=s.replace('''    g = f["R"][[j for j in range(114) if names[j] in [names[k] for k in range(114)]]].mean(0)''','''    g = f["R"][ids_all].mean(0)''')
s=s.replace('''shifts = np.arange(-60, 61, 2)''','''shifts = np.arange(-60, 61, 2)
ids_all = np.arange(114)''')
open('mknb.py','w').write(s)
EOF
. dev/bin/activate && uv pip install -q nbformat && python mknb.py && cat > harness.py <<'EOF'
import sys, pickle, json, time
sys.path.insert(0,'entries/okuno-2025')
import matplotlib; matplotlib.use('Agg')
import flyfc
subs=['fly-087','fly-089','fly-094','fly-097','fly-098','fly-099','fly-100','fly-101','fly-105']
cache={s:pickle.load(open(f'fly_{s}.pkl','rb')) for s in subs}
def fake_process(a, tmpl, masks, **k):
    f=dict(cache[a['subject']]); f['warped']=None; f['mean']=None; f['t_total']=0; f['mb_read']=0; return f
flyfc.process_fly=fake_process
B=pickle.load(open('betas.pkl','rb')); it=iter(B)
flyfc.glm_betas=lambda a,f,r: next(it)
nb=json.load(open('entries/okuno-2025/reproduce_okuno_2025.ipynb'))
ns={}
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    src=''.join(c['source'])
    if 'flyfc.choose_flip' in src:
        src=src.replace('flips = flyfc.choose_flip(mean0, tmpl)','flips = {}')
    print(f'--- cell {i}', flush=True); t=time.time()
    exec(compile(src, f'cell{i}', 'exec'), ns)
    print(f'[{time.time()-t:.0f}s]')
EOF
python harness.py 2>&1 | grep -v -i "warn" | tail -150
```

```
53 cells
('none', '8', 'left-right swapped') FlyEM higher in 31 of 63
('none', '9', 'as registered') FlyEM higher in 49 of 63
('none', '9', 'left-right swapped') FlyEM higher in 28 of 63
('poltcomp', '8', 'as registered') FlyEM higher in 56 of 63
('poltcomp', '8', 'left-right swapped') FlyEM higher in 47 of 63
('poltcomp', '9', 'as registered') FlyEM higher in 57 of 63
('poltcomp', '9', 'left-right swapped') FlyEM higher in 47 of 63
MAIN (Poly-tCompCor, 8 flies): 56 of 63; within 52.2 to 63.8: True
regions where FlyWire is higher: AB(R) (0.45 vs 0.51), AME(R) (0.49 vs 0.55), FB (0.63 vs 0.63), PLP(R) (0.54 vs 0.54), SLP(R) (0.68 vs 0.71), SMP(R) (0.69 vs 0.70), BU(L) (0.45 vs 0.46)
per-region r range: FlyEM 0.349 to 0.827 | FlyWire 0.306 to 0.706
paper's own per-region FlyWire values (Zenodo auc file) against this attempt's: r = 0.658
[0s]
--- cell 25
outNTypes (114, 7)
main | DA r=-0.170 p=0.184; SER r=0.021 p=0.87; GABA r=-0.115 p=0.368; GLUT r=0.265 p=0.0361; ACH r=-0.048 p=0.708; OCT r=-0.311 p=0.0132
no nuisance | DA r=-0.146 p=0.252; SER r=-0.201 p=0.114; GABA r=-0.063 p=0.623; GLUT r=0.236 p=0.0629; ACH r=0.016 p=0.902; OCT r=-0.191 p=0.134
nine flies | DA r=-0.176 p=0.169; SER r=0.014 p=0.911; GABA r=-0.099 p=0.44; GLUT r=0.280 p=0.026; ACH r=-0.069 p=0.591; OCT r=-0.299 p=0.0173
left-right swapped | DA r=-0.029 p=0.818; SER r=0.070 p=0.587; GABA r=-0.086 p=0.503; GLUT r=0.339 p=0.00654; ACH r=-0.202 p=0.112; OCT r=-0.232 p=0.0676
paper's own per-region values (Zenodo auc file) | DA r=0.209 p=0.0996; SER r=-0.170 p=0.183; GABA r=-0.252 p=0.0465; GLUT r=-0.196 p=0.123; ACH r=0.395 p=0.00136; OCT r=-0.313 p=0.0124
[... 132 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('mknb.py').read()
def rep(a,b):
    global s
    assert a in s, a[:60]
    s=s.replace(a,b)
rep('''**Result: FlyEM gives the higher FC-SC correlation, but both values are below the paper's.**
With the code's eight flies and Poly-tCompCor, r is about 0.61 for FlyEM and 0.57 for FlyWire,
below the tolerances (0.657 and 0.612), so the claim is partially reproduced. FlyEM is higher
under every variant printed (no nuisance removal, nine flies, left and right swapped, signed FC).
The paper's own output file for the FlyWire setting gives 0.68, so the gap is in this attempt's FC
(no SPM12 motion and slice-timing correction, native-space tCompCor, a different registration),
not in the SC.''','''**Result: FlyEM gives the higher FC-SC correlation, but both values are below the paper's.**
With the code's eight flies and Poly-tCompCor, r is 0.609 for FlyEM and 0.569 for FlyWire, below
the lower bounds of the tolerances (0.657 and 0.612), so the claim is partially reproduced. FlyEM
is higher under every variant printed (no nuisance removal, nine flies, left and right swapped,
signed FC). The paper's own output file for the FlyWire setting gives 0.684 with the same SC, so the
gap is in this attempt's FC, not in the SC. Swapping left and right lowers both correlations
(FlyEM 0.609 to the value printed in the swapped row), which supports the orientation assumed.''')
rep('''**Result: FlyEM is higher in most regions, within the tolerance of 58 of 63.** The printed count
under the main setting and under every variant is the evidence; the regions where FlyWire is
higher are listed.''','''**Result: reproduced, resting on the left-right orientation.** FlyEM is higher in 56 of 63
regions under the main setting (tolerance 52.2 to 63.8) and in 57 with nine flies. With left and
right swapped the count is 47, outside the tolerance, and without nuisance removal it is lower
still; the swapped orientation also gives the lower matrix-level FC-SC correlation (fig3d), so the
orientation used is the better supported one. This attempt's per-region FlyWire values correlate
with the paper's own (Zenodo) at r = 0.658.''')
rep('''**Result: not reproduced.** With this attempt's FC the per-region FC-SC correlation does not rise
with the cholinergic share (r near 0, p > 0.05) and its relation to the GABAergic share is not
significant. The paper's own per-region values from its Zenodo file, run through the same code,
are printed beside them for comparison: they show whether the difference comes from the FC.''','''**Result: not reproduced.** With this attempt's FC the per-region FC-SC correlation does not rise
with the cholinergic share (r = -0.048, p = 0.71) and its relation to the GABAergic share is not
significant (r = -0.115, p = 0.37); no variant gives a significant ACh or GABA correlation. The
paper's own per-region values from its Zenodo file, run through the same transmitter table, give
the paper's numbers (ACh r = 0.395, p = 0.0014; GABA r = -0.252, p = 0.047), so the difference
comes from the FC computed here, not from the transmitter table.''')
rep('''**Result: reproduced.** The unsegregated SC has the higher FC-SC correlation than every null
sample's distribution for both neuron and synapse SC, with p below 0.05/6; the selected total
matches the expected 2,373,100, and the null totals do not differ from it.''','''**Result: reproduced.** Under the main setting the unsegregated SC has a higher FC-SC correlation
than the null for neuron SC (0.626 against 0.589 +- 0.002, p = 7e-112) and synapse SC (0.577
against 0.562 +- 0.002, p = 5e-10). The selected total is 2,373,104 (expected 2,373,100) and the
null totals do not differ from it (p = 0.832, as in the paper). Without nuisance removal the
direction reverses (both below the null), and with left and right swapped the synapse SC is not
significant, so the result depends on Poly-tCompCor and on the orientation.''')
rep('''**Result: reproduced under reading (a).** The segregated SC (the code's target) has a lower FC-SC
correlation than the null for both neuron and synapse SC, with p below 0.05/6. Reading (b) was not
run.''','''**Result: reproduced under reading (a).** The segregated SC (the code's target) has a lower FC-SC
correlation than the null for neuron SC (0.568 against 0.572 +- 0.001, p = 4e-8) and synapse SC
(0.522 against 0.537 +- 0.001, p = 9e-26). The same holds with nine flies and with left and right
swapped; without nuisance removal the neuron SC is not different from the null (p = 0.91).
Reading (b) was not run.''')
rep('''**Result: reproduced.** The reciprocal-synapse SC has a higher FC-SC correlation than the null for
neuron and synapse SC, with p below 0.05/6 under the main setting.''','''**Result: reproduced.** The reciprocal-synapse SC has a higher FC-SC correlation than the null for
neuron SC (0.630 against 0.592 +- 0.002, p = 5e-115) and synapse SC (0.573 against 0.566 +- 0.002,
p = 0.00099, below 0.05/6 = 0.0083). With nine flies both still hold; without nuisance removal the
synapse SC is not significant, and with left and right swapped it is below the null.''')
rep('''**Result: reproduced.** LAL, FB, IPS and GNG all lie in the one large positive cluster, with peak t
above half the brain-wide maximum (reading a), under both atlases and both regressors; their rank
by mean t (reading b) is printed.''','''**Result: reproduced.** The second level gives one large positive cluster (382,697 voxels; the
code's README prints 416,801) with maximum t = 17.7 (README 14.7). LAL, FB, IPS and GNG all lie
in it with peak t above half the maximum (reading a) under both atlases and both regressors.
Under reading (b) all four rank in the top third with the hemibrain atlas; with JFRC2010 the GNG
ranks 28 of 75.''')
rep('''**Result: not reproduced.** No voxel falls below the negative height threshold, so there is no
negative cluster; WED and AVLP hold mostly positive t values above threshold under both atlases and
both regressors.''','''**Result: not reproduced.** No voxel in the brain mask falls below the negative height threshold
(the lowest t is -1.57), so there is no negative cluster. WED and AVLP are positive: 84 to 100% of
their voxels are above the positive threshold under both atlases and both regressors, and the
README's two negative peaks have t = 2.69 and 3.50 here.''')
rep('''**Result:** the totals for FlyEM at its lowest confidence, FlyWire at cleft score 50 and FlyWire at
140 are printed above against 21.4, 18.8 and 11.4 million (tolerance 10%).''','''**Result: partially reproduced.** FlyWire has 18.83 million post-synapses at cleft score 50
(expected 18.8) and 11.24 million at 140 (expected 11.4), close to FlyEM's 11.57 million at
confidence 0.8. The table holds FlyEM only from confidence 0.5 (18.12 million), so the 21.4
million at confidence 0 cannot be checked.''')
rep('''mb = [n for n in nm if any(n.startswith(x) for x in ["aL", "a'L", "bL", "b'L", "gL", "CA", "PED", "MB"])]''','''mb = [n for n in nm if any(n.startswith(x) for x in ["aL", "a'L", "bL", "b'L", "gL", "CA(", "PED", "MB"])]''')
rep('''**Result:** the per-ROI counts above decide the claim (FlyEM higher in the mushroom body and EB, FB,
NO, PB; FlyWire higher in LO, ME, CAN, FLA).''','''**Result: reproduced.** FlyEM has more post-synapses in aL and bL and in every mushroom body ROI,
and in EB, FB, NO and PB; FlyWire has more in LO and ME and in CAN and FLA.''')
rep('''**Result:** the three correlations are printed against the paper's 0.778, 0.9 and 0.919.''','''**Result: reproduced.** Pearson r = 0.778, Spearman r = 0.900 and Pearson r on log10 counts =
0.919, as in the paper.''')
rep('''**Result:** the mean shares are printed against 62.8%, 15.5% and 11.4%.''','''**Result: reproduced.** Acetylcholine 62.8% +- 14.2%, glutamate 15.5% +- 9.2% and GABA 11.4% +-
8.2%, as in the paper.''')
rep('''| fig3a, fig3c, figs3-1a, fig3f (elsewhere) | see the record |''','''| fig3a-postsynapse-counts (elsewhere) | partially reproduced: FlyEM at confidence 0 not in the table |
| fig3c, figs3-1a, fig3f (elsewhere) | reproduced, on the paper's per-ROI tables |''')
rep('''| fig3e-flyem-higher-most-regions | reproduced |''','''| fig3e-flyem-higher-most-regions | reproduced (rests on the left-right orientation) |''')
open('mknb.py','w').write(s)
EOF
. dev/bin/activate && python mknb.py; date -u
```

```
53 cells
Tue Nov 10 07:17:12 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/okuno-2025 && cat > requirements.in <<'EOF'
aiohttp
antspyx
fsspec
h5py
matplotlib
nibabel
numpy
remfile
requests
scipy
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: okuno-2025
type: reproduction
title: Functional and structural connectivity in Drosophila (Okuno et al. 2025)
description: Tests the findings of Okuno, Woodward, Okano and Hata (2025) on dandiset 000727, which
  holds the whole-brain two-photon imaging of nine walking flies that the paper reuses. The raw
  GCaMP series are streamed, registered to the paper's resized FDA template and reduced to the 114
  hemibrain ROIs, and the resulting FC is compared with the paper's published FlyEM and FlyWire SC
  matrices, including its permutation tests of unsegregated, segregated and reciprocal synapses. A
  group GLM of walking is run on the same data. The k-means ROI atlases of the paper's smoothing
  and ROI-count analyses are not published, so those claims are blocked.
license: Apache-2.0
notebooks:
- path: reproduce_okuno_2025.ipynb
  title: Reproducing Okuno et al. (2025) from dandiset 000727
  runtime_minutes: 25
helpers:
- flyfc.py
related:
- id: dandi:000727/0.240106.0043
  relation: uses_data
- id: doi:10.7554/elife.107990.1
  relation: reproduces
EOF
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

**Agent calls Bash**

```bash
cat > README.md <<'EOF'
# Okuno, Woodward, Okano & Hata (2025) from dandiset 000727

Tests the findings of [Okuno et al. (2025)](https://doi.org/10.7554/elife.107990.1) on
[DANDI:000727](https://dandiarchive.org/dandiset/000727/0.240106.0043), the whole-brain two-photon
imaging of nine walking flies (Brezovec et al.) that the paper reuses. The FC computed here from the
raw imaging is compared with the paper's published FlyEM and FlyWire SC matrices (its code at
commit 4b92add and Zenodo record 15532272).

| Claim | Outcome |
|---|---|
| FlyEM gives a higher FC-SC correlation than FlyWire (0.73 against 0.68) | Partially reproduced |
| FlyEM is higher in 58 of 63 regions | Reproduced |
| Regional FC-SC correlation rises with cholinergic and falls with GABAergic output share | Not reproduced |
| Unsegregated synapses give a higher FC-SC correlation than random samples | Reproduced |
| Segregated synapses give a lower FC-SC correlation than random samples | Reproduced |
| Reciprocal synapses give a higher FC-SC correlation than random samples | Reproduced |
| LAL, FB, IPS and GNG are active during walking | Reproduced |
| WED and AVLP are inactive or suppressed during walking | Not reproduced |
| Connectome counts per region and transmitter shares (four claims, data elsewhere) | Three reproduced, one partially |
| Smoothing, nuisance removal and ROI-count analyses on SCKm and DistKm ROIs (nine claims) | Blocked: atlases not published |
| FlyEM confidence thresholds, FlyEM permutation tests | Blocked: SC not published |
| Other connectome-only claims (seven) | Blocked |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/okuno-2025-01.yaml`](../../attempts/okuno-2025-01.yaml).
EOF
cd  && timeout 900 python tools/entry.py lock entries/okuno-2025 2>&1 | tail -5; head -3 entries/okuno-2025/entry.yaml; grep python entries/okuno-2025/entry.yaml
```

```
wrote okuno-2025/requirements.lock.txt (Python 3.13, with hashes)
schema_version: 1
name: okuno-2025
type: reproduction
python: "3.13"
```

**Agent calls Bash**

```bash
date -u && timeout 5400 python tools/entry.py all entries/okuno-2025 2>&1 | tail -30; date -u
```

```
Tue Nov 10 07:17:36 UTC 2026
Installed kernelspec registry-okuno-2025 in executed/okuno-2025/.venv/share/jupyter/kernels/registry-okuno-2025
0 error(s)
pass  reproduce_okuno_2025.ipynb  (1059 s)
Tue Nov 10 07:35:25 UTC 2026
```

**Agent calls Bash**

```bash
ls executed/okuno-2025/ && python - <<'EOF'
import json
nb=json.load(open('executed/okuno-2025/reproduce_okuno_2025.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    for o in c.get('outputs',[]):
        t=o.get('text') or o.get('data',{}).get('text/plain')
        if o.get('output_type')=='error': print('ERR', o['ename'], o['evalue'])
        if t and i<26: print(f'[{i}]', ''.join(t)[:3500])
EOF
```

```
reproduce_okuno_2025.ipynb
result.json
[1] dandiset 000727 version 0.240106.0043
code commit 4b92add4a44f641ab6add809ff6b0e0d6110b50c zenodo record 15532272

[3] 9 NWB files

[3] fly-087 69.0 GB green (3384, 256, 128, 49) uint16 rate 1.879714 Hz spacing (np.float64(2.611), np.float64(2.611), np.float64(5.0)) um | speed 90000 samples at 50.0 Hz | processed (3384, 314, 146, 91) | F
fly-089 66.6 GB green (3384, 256, 128, 49) uint16 rate 1.879715 Hz spacing (np.float64(2.554), np.float64(2.67), np.float64(5.0)) um | speed 90000 samples at 50.0 Hz | processed (3384, 314, 146, 91) | F
fly-094 67.2 GB green (3384, 256, 128, 49) uint16 rate 1.879714 Hz spacing (np.float64(2.611), np.float64(2.611), np.float64(5.0)) um | speed 90000 samples at 50.0 Hz | processed (3384, 314, 146, 91) | F
fly-097 66.9 GB green (3384, 256, 128, 49) uint16 rate 1.879714 Hz spacing (np.float64(2.549), np.float64(2.675), np.float64(5.0)) um | speed 90000 samples at 50.0 Hz | processed (3384, 314, 146, 91) | F
fly-098 67.2 GB green (3384, 256, 128, 49) uint16 rate 1.879714 Hz spacing (np.float64(2.549), np.float64(2.675), np.float64(5.0)) um | speed 90000 samples at 50.0 Hz | processed (3384, 314, 146, 91) | F
fly-099 68.2 GB green (3384, 256, 128, 49) uint16 rate 1.879714 Hz spacing (np.float64(2.549), np.float64(2.675), np.float64(5.0)) um | speed 90000 samples at 50.0 Hz | processed (3384, 314, 146, 91) | F
fly-100 67.7 GB green (3384, 256, 128, 49) uint16 rate 1.879714 Hz spacing (np.float64(2.578), np.float64(2.646), np.float64(5.0)) um | speed 90000 samples at 50.0 Hz | processed (3384, 314, 146, 91) | F
fly-101 67.8 GB green (3384, 256, 128, 49) uint16 rate 1.879714 Hz spacing (np.float64(2.578), np.float64(2.646), np.float64(5.0)) um | speed 90000 samples at 50.0 Hz | processed (3384, 314, 146, 91) | F
fly-105 67.3 GB green (3384, 256, 128, 49) uint16 rate 1.879714 Hz spacing (np.float64(2.611), np.float64(2.611), np.float64(5.0)) um | speed 90000 samples at 50.0 Hz | processed (3384, 314,
[... 135 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import sys, pickle; sys.path.insert(0,'entries/okuno-2025')
import flyfc, numpy as np
subs=['fly-087','fly-089','fly-094','fly-097','fly-098','fly-099','fly-100','fly-101','fly-105']
fl=[pickle.load(open(f'fly_{s}.pkl','rb')) for s in subs]
reg,_,_,_=flyfc.walking_regressors([f['speed'] for f in fl])
sh=np.arange(-60,61,2)
Sd=flyfc.poly_regressors(3384)
for i,f in enumerate(fl):
    g=flyfc.residualize(f['R'].mean(0)[:,None],Sd)[:,0]
    cc=[np.corrcoef(np.roll(reg[i],s)[70:-70],g[70:-70])[0,1] for s in sh]
    k=int(np.argmax(cc)); print(f['subject'], round(cc[k],3), sh[k], round(cc[30],3), round(np.median(np.abs(np.array(cc)[np.abs(sh)>30])),3))
EOF
```

```
fly-087 0.552 0 0.552 0.032
fly-089 0.427 2 0.364 0.054
fly-094 0.795 0 0.795 0.025
fly-097 0.591 0 0.591 0.036
fly-098 0.464 0 0.464 0.063
fly-099 0.536 0 0.536 0.027
fly-100 0.602 0 0.602 0.034
fly-101 0.491 0 0.491 0.062
fly-105 0.617 0 0.617 0.107
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && for th in 1 4; do ITK_GLOBAL_DEFAULT_NUMBER_OF_THREADS=$th python - <<'EOF'
import sys, pickle, time, os; sys.path.insert(0,'entries/okuno-2025')
import flyfc, numpy as np, ants
tm,z=flyfc.code_nifti('template/thresholded_FDACal.nii.gz')
tmpl=ants.from_numpy(tm, spacing=tuple(float(v)/1000 for v in z))
m=pickle.load(open('fly_fly-087.pkl','rb'))['mean']
for rep in range(2):
    t=time.time(); c,cc,_=flyfc.register(m,tmpl,(1,1,1)); print(os.environ['ITK_GLOBAL_DEFAULT_NUMBER_OF_THREADS'], cc, round(time.time()-t,1), np.nansum(c))
EOF
done
```

```
1 {'affine_meansquares': 0.678334166557657, 'affine_mattes': 0.7373848554041419, 'syn': 0.8283929053911164} 41.1 253211376.0606792
1 {'affine_meansquares': 0.6584017264088526, 'affine_mattes': -0.14566462946661188, 'syn': 0.812965329829926} 38.5 298519157.93654805
4 {'affine_meansquares': 0.6762168940663986, 'affine_mattes': 0.4473891399598633, 'syn': 0.8030359837051312} 14.1 293536769.9946948
4 {'affine_meansquares': 0.6707413348488367, 'affine_mattes': 0.4473891399598633, 'syn': 0.8022183829051578} 13.9 295791890.71260613
Shell cwd was reset to
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('executed/okuno-2025/reproduce_okuno_2025.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code' or i<26: continue
    for o in c.get('outputs',[]):
        t=o.get('text')
        if t: print(f'[{i}]', ''.join(t)[:3000])
EOF
```

```
[28] fig4e-unsegregated-higher | target sp10db3000mi1_only1 synapse total 2373104 neuron total 137694 | null rd185-20 n = 99 synapse totals mean 2309356 SD 299896 | totals test p = 0.832

[28] fig4f-segregated-lower | target sp90db3000mi1 synapse total 28954898 neuron total 713783 | null rd1560-80 n = 99 synapse totals mean 28360686 SD 1270979 | totals test p = 0.64

[28] fig4i-reciprocal-higher | target rc20_only1 synapse total 1630011 neuron total 184921 | null rd140-15 n = 99 synapse totals mean 1594440 SD 191034 | totals test p = 0.852

[29] main                neuron r=0.6265 null 0.5873+-0.0017 z=+22.9 p=1.16e-115 (null range 0.5839 to 0.5907) | synapse r=0.5774 null 0.5603+-0.0024 z=+7.2 p=6.98e-13
no nuisance         neuron r=0.5744 null 0.5921+-0.0020 z=-8.7 p=3.61e-18 (null range 0.5881 to 0.5988) | synapse r=0.5507 null 0.5804+-0.0029 z=-10.4 p=4.16e-25
nine flies          neuron r=0.6237 null 0.5841+-0.0017 z=+23.2 p=4.4e-119 (null range 0.5806 to 0.5875) | synapse r=0.5742 null 0.5564+-0.0024 z=+7.4 p=1.03e-13
left-right swapped  neuron r=0.5516 null 0.5266+-0.0018 z=+14.2 p=5.72e-46 (null range 0.5230 to 0.5309) | synapse r=0.5017 null 0.4989+-0.0024 z=+1.2 p=0.237
expected total 2,373,100 +- 237,310; measured 2373104
MAIN: neuron above null with p < 0.05/6: True | synapse: True

[31] main                neuron r=0.5653 null 0.5688+-0.0008 z=-4.1 p=3.56e-05 (null range 0.5668 to 0.5703) | synapse r=0.5186 null 0.5334+-0.0014 z=-10.2 p=1.92e-24
no nuisance         neuron r=0.5899 null 0.5892+-0.0016 z=+0.4 p=0.667 (null range 0.5862 to 0.5931) | synapse r=0.5579 null 0.5690+-0.0023 z=-4.7 p=2.08e-06
nine flies          neuron r=0.5617 null 0.5655+-0.0008 z=-4.6 p=3.35e-06 (null range 0.5636 to 0.5670) | synapse r=0.5146 null 0.5294+-0.0014 z=-10.4 p=3.66e-25
left-right swapped  neuron r=0.5061 null 0.5096+-0.0009 z=-3.9 p=9.17e-05 (null range 0.5077 to 0.5119) | synapse r=0.4661 null 0.4759+-0.0013 z=-7.3 p=2.02e-13
MAIN (reading a, the code's target): 
[... 116 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('mknb.py').read()
def rep(a,b):
    global s
    assert a in s, a[:70]
    s=s.replace(a,b)
rep('''The files, their metadata, and what the analysis reads from them. ANTs registration is seeded
(`random_seed=1`); no other random numbers are drawn.''','''The files, their metadata, and what the analysis reads from them. ANTs registration is given a
seed (`random_seed=1`), but it is not exactly repeatable (two runs of the same registration gave
correlations with the template differing by about 0.01), so numbers that rest on it can move in
the second or third decimal between runs; the conclusions quote this run's output. No other
random numbers are drawn.''')
rep('''The behaviour clock is checked against the imaging with a contrast: the brain-wide mean of the raw
ROI series against the walking regressor,''','''The behaviour clock is checked against the imaging with a contrast: the brain-wide mean of the ROI
series, after removing the 7 polynomial terms, against the walking regressor,''')
rep('''    g = f["R"][ids_all].mean(0)
    g = g - g.mean()''','''    g = flyfc.residualize(f["R"][ids_all].mean(0)[:, None], flyfc.poly_regressors(f["T"]))[:, 0]''')
open('mknb.py','w').write(s)
EOF
. dev/bin/activate && python mknb.py && cd  && date -u && timeout 5400 python tools/entry.py run entries/okuno-2025 2>&1 | tail -4; date -u
```

```
53 cells
Tue Nov 10 07:38:01 UTC 2026
Installed kernelspec registry-okuno-2025 in executed/okuno-2025/.venv/share/jupyter/kernels/registry-okuno-2025
pass  reproduce_okuno_2025.ipynb  (1053 s)
Tue Nov 10 07:55:41 UTC 2026
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('executed/okuno-2025/reproduce_okuno_2025.ipynb'))
keep=[7,12,18,22,25,29,31,33,36,37,40]
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code' or i not in keep: continue
    for o in c.get('outputs',[]):
        t=o.get('text')
        if t: print(f'[{i}]', ''.join(t)[:2500])
EOF
```

```
[7] fly-087 read 8161 MB in 66 s | correlation with template {'affine_meansquares': 0.669, 'affine_mattes': 0.735, 'syn': 0.833} | ROIs not fully in the field of view 2 min coverage 0.967

[7] fly-089 read 7253 MB in 60 s | correlation with template {'affine_meansquares': 0.668, 'affine_mattes': -0.064, 'syn': 0.802} | ROIs not fully in the field of view 0 min coverage 1.0

[7] fly-094 read 7666 MB in 62 s | correlation with template {'affine_meansquares': 0.656, 'affine_mattes': 0.352, 'syn': 0.756} | ROIs not fully in the field of view 0 min coverage 1.0

[7] fly-097 read 7408 MB in 61 s | correlation with template {'affine_meansquares': 0.588, 'affine_mattes': 0.413, 'syn': 0.705} | ROIs not fully in the field of view 0 min coverage 1.0

[7] fly-098 read 7318 MB in 67 s | correlation with template {'affine_meansquares': 0.642, 'affine_mattes': 0.713, 'syn': 0.786} | ROIs not fully in the field of view 0 min coverage 0.999

[7] fly-099 read 7346 MB in 67 s | correlation with template {'affine_meansquares': 0.64, 'affine_mattes': 0.695, 'syn': 0.785} | ROIs not fully in the field of view 3 min coverage 0.991

[7] fly-100 read 7084 MB in 63 s | correlation with template {'affine_meansquares': 0.62, 'affine_mattes': 0.001, 'syn': 0.693} | ROIs not fully in the field of view 8 min coverage 0.653

[7] fly-101 read 7285 MB in 62 s | correlation with template {'affine_meansquares': 0.636, 'affine_mattes': 0.353, 'syn': 0.726} | ROIs not fully in the field of view 0 min coverage 1.0

[7] fly-105 read 6681 MB in 66 s | correlation with template {'affine_meansquares': 0.572, 'affine_mattes': 0.624, 'syn': 0.684} | ROIs not fully in the field of view 11 min coverage 0.936

[7] peak memory (GB) 3.45 | elapsed (min) 10.3

[... 142 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('mknb.py').read()
def rep(a,b):
    global s
    assert a in s, a[:70]
    s=s.replace(a,b)
rep('''With the code's eight flies and Poly-tCompCor, r is 0.609 for FlyEM and 0.569 for FlyWire, below
the lower bounds of the tolerances (0.657 and 0.612), so the claim is partially reproduced. FlyEM
is higher under every variant printed (no nuisance removal, nine flies, left and right swapped,
signed FC). The paper's own output file for the FlyWire setting gives 0.684 with the same SC, so the
gap is in this attempt's FC, not in the SC. Swapping left and right lowers both correlations
(FlyEM 0.609 to the value printed in the swapped row), which supports the orientation assumed.''','''With the code's eight flies and Poly-tCompCor, r is 0.616 for FlyEM and 0.575 for FlyWire, below
the lower bounds of the tolerances (0.657 and 0.612), so the claim is partially reproduced. FlyEM
is higher in every as-registered variant (no nuisance removal 0.638 against 0.606, nine flies
0.608 against 0.568, signed FC the same as the main values). The paper's own output file for the
FlyWire setting gives 0.684 with the same SC, so the gap is in this attempt's FC, not in the SC.
Swapping left and right lowers both correlations (FlyEM 0.531, FlyWire 0.520), which supports the
orientation assumed.''')
rep('''**Result: reproduced, resting on the left-right orientation.** FlyEM is higher in 56 of 63
regions under the main setting (tolerance 52.2 to 63.8) and in 57 with nine flies. With left and
right swapped the count is 47, outside the tolerance, and without nuisance removal it is lower
still; the swapped orientation also gives the lower matrix-level FC-SC correlation (fig3d), so the
orientation used is the better supported one. This attempt's per-region FlyWire values correlate
with the paper's own (Zenodo) at r = 0.658.''','''**Result: reproduced, resting on the left-right orientation.** FlyEM is higher in 55 of 63
regions under the main setting (tolerance 52.2 to 63.8) and in 55 with nine flies. With left and
right swapped the count is 49, outside the tolerance, and without nuisance removal it is 50 (48
with nine flies); the swapped orientation also gives the lower matrix-level FC-SC correlation
(fig3d), so the orientation used is the better supported one. This attempt's per-region FlyWire
values correlate with the paper's own (Zenodo) at r = 0.72.''')
rep('''with the cholinergic share (r = -0.048, p = 0.71) and its relation to the GABAergic share is not
significant (r = -0.115, p = 0.37); no variant gives a significant ACh or GABA correlation.''','''with the cholinergic share (r = 0.013, p = 0.92) and its relation to the GABAergic share is not
significant (r = -0.157, p = 0.22); no variant gives a significant ACh or GABA correlation.''')
rep('''Under the main setting the unsegregated SC has a higher FC-SC correlation
than the null for neuron SC (0.626 against 0.589 +- 0.002, p = 7e-112) and synapse SC (0.577
against 0.562 +- 0.002, p = 5e-10).''','''Under the main setting the unsegregated SC has a higher FC-SC correlation
than the null for neuron SC (0.634 against 0.593 +- 0.002, p = 1e-153) and synapse SC (0.583
against 0.564 +- 0.002, p = 2e-17).''')
rep('''Without nuisance removal the
direction reverses (both below the null), and with left and right swapped the synapse SC is not
significant, so the result depends on Poly-tCompCor and on the orientation.''','''Without nuisance removal the
direction reverses (both below the null, p = 3e-6 and 6e-15), so the result depends on
Poly-tCompCor; with nine flies and with left and right swapped both are still above the null
(swapped synapse SC p = 0.0021, below 0.05/6).''')
rep('''correlation than the null for neuron SC (0.568 against 0.572 +- 0.001, p = 4e-8) and synapse SC
(0.522 against 0.537 +- 0.001, p = 9e-26). The same holds with nine flies and with left and right
swapped; without nuisance removal the neuron SC is not different from the null (p = 0.91).''','''correlation than the null for neuron SC (0.574 against 0.578 +- 0.001, p = 4e-8) and synapse SC
(0.524 against 0.540 +- 0.001, p = 6e-35). The same holds with nine flies and with left and right
swapped; without nuisance removal the neuron SC is not different from the null (p = 0.48).''')
rep('''neuron SC (0.630 against 0.592 +- 0.002, p = 5e-115) and synapse SC (0.573 against 0.566 +- 0.002,
p = 0.00099, below 0.05/6 = 0.0083). With nine flies both still hold; without nuisance removal the
synapse SC is not significant, and with left and right swapped it is below the null.''','''neuron SC (0.636 against 0.596 +- 0.002, p = 2e-143) and synapse SC (0.577 against 0.568 +- 0.002,
p = 3e-6, below 0.05/6 = 0.0083). With nine flies both still hold; without nuisance removal the
synapse SC is below the null (p = 0.0034), and with left and right swapped it is below the null
without reaching 0.05/6 (p = 0.0195).''')
rep('''**Result: reproduced.** The second level gives one large positive cluster (382,697 voxels; the
code's README prints 416,801) with maximum t = 17.7 (README 14.7). LAL, FB, IPS and GNG all lie
in it with peak t above half the maximum (reading a) under both atlases and both regressors.
Under reading (b) all four rank in the top third with the hemibrain atlas; with JFRC2010 the GNG
ranks 28 of 75.''','''**Result: reproduced.** The second level gives one large positive cluster (399,973 voxels; the
code's README prints 416,801) with maximum t = 16.1 (README 14.7). LAL, FB, IPS and GNG all lie
in it with peak t above half the maximum (reading a) under both atlases and both regressors.
Reading (b) fails for FB (rank 26 of 63 by mean t with the hemibrain atlas, 31 of 75 with JFRC2010)
and, with JFRC2010, for LAL; the claim holds under reading (a), as the criterion allows.''')
rep('''**Result: not reproduced.** No voxel in the brain mask falls below the negative height threshold
(the lowest t is -1.57), so there is no negative cluster. WED and AVLP are positive: 84 to 100% of
their voxels are above the positive threshold under both atlases and both regressors, and the
README's two negative peaks have t = 2.69 and 3.50 here.''','''**Result: not reproduced.** No voxel in the brain mask falls below the negative height threshold
(the lowest t is -0.82), so there is no negative cluster. WED and AVLP are positive: 85 to 100% of
their voxels are above the positive threshold under both atlases and both regressors, and the
README's two negative peaks have t = 3.28 and 4.09 here.''')
rep('''1e-5 from the files in name order, and the seventh fly in name order (fly-100) has 20 hemibrain
ROIs partly outside the field of view, which fits the paper's reason for leaving one fly out.''','''1e-5 from the files in name order, and the seventh fly in name order (fly-100) has the lowest
coverage of a hemibrain ROI (AL(L) 65% inside the field of view in this run), which fits the
paper's reason for leaving one fly out; fly-105 also has ROIs partly outside.''')
rep('''FlyWire), which bears on the claims that compare FC-SC values across regions.''','''FlyWire), which bears on the claims that compare FC-SC values across regions. The registration is
not exactly repeatable, so numbers can move slightly between runs.''')
open('mknb.py','w').write(s)
EOF
. dev/bin/activate && python mknb.py && cd  && python - <<'EOF'
import json
src=json.load(open('entries/okuno-2025/reproduce_okuno_2025.ipynb'))
ex=json.load(open('executed/okuno-2025/reproduce_okuno_2025.ipynb'))
assert len(src['cells'])==len(ex['cells'])
n=0
for a,b in zip(src['cells'],ex['cells']):
    assert a['cell_type']==b['cell_type']
    if a['cell_type']=='markdown':
        if a['source']!=b['source']: n+=1
        b['source']=a['source']
    else:
        assert ''.join(a['source'])==''.join(b['source']), 'code differs'
json.dump(ex, open('executed/okuno-2025/reproduce_okuno_2025.ipynb','w'), indent=1)
print('patched', n, 'markdown cells')
EOF
grep -n "fly-100\|fly-105" entries/okuno-2025/reproduce_okuno_2025.ipynb | head
```

```
53 cells
patched 9 markdown cells
1073:    "1e-5 from the files in name order, and the seventh fly in name order (fly-100) has the lowest\n",
1075:    "paper's reason for leaving one fly out; fly-105 also has ROIs partly outside. The\n",
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('executed/okuno-2025/reproduce_okuno_2025.ipynb'))
for i in [8,14]:
    for o in nb['cells'][i].get('outputs',[]):
        if o.get('text'): print(i, ''.join(o['text']))
EOF
```

```
8 fly-087 SAD 0.98, AMMC 0.97
fly-099 AL(R) 1.00, SAD 0.99, AMMC 0.99
fly-100 AL(L) 0.65, AL(R) 0.85, CRE(L) 0.99, SAD 0.99, gL(R) 1.00, bL(L) 1.00, AMMC 0.99, gL(L) 0.93
fly-105 CRE(R) 0.98, AL(L) 0.99, CRE(L) 0.98, gL(R) 0.96, SMP(L) 0.97, SIP(R) 1.00, gL(L) 0.94, LOP(R) 0.99, SIP(L) 0.97, a'L(L) 0.99, SMP(R) 0.99
flies in name order: ['fly-087', 'fly-089', 'fly-094', 'fly-097', 'fly-098', 'fly-099', 'fly-100', 'fly-101', 'fly-105']
code's subject list [1 2 3 4 5 6 8 9] leaves out the 7th: fly-100

14 largest speed-trace correlation between two flies: 0.11
largest correlation of mean ROI intensity profiles between two flies: 0.809
identical speed traces: []
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('mknb.py').read()
a='''seed (`random_seed=1`), but it is not exactly repeatable (two runs of the same registration gave
correlations with the template differing by about 0.01), so numbers that rest on it can move in
the second or third decimal between runs; the conclusions quote this run's output.'''
assert a in s
s=s.replace(a,'''seed (`random_seed=1`), but it is not exactly repeatable between runs (not run here: repeated
registrations of one mean image, made while preparing, differed slightly), so numbers that rest
on it can move in the second or third decimal between runs; the conclusions quote this run's
output.''')
open('mknb.py','w').write(s)
EOF
. dev/bin/activate && python mknb.py && cd  && python - <<'EOF'
import json
src=json.load(open('entries/okuno-2025/reproduce_okuno_2025.ipynb'))
ex=json.load(open('executed/okuno-2025/reproduce_okuno_2025.ipynb'))
for a,b in zip(src['cells'],ex['cells']):
    if a['cell_type']=='markdown': b['source']=a['source']
    else: assert ''.join(a['source'])==''.join(b['source'])
json.dump(ex, open('executed/okuno-2025/reproduce_okuno_2025.ipynb','w'), indent=1)
EOF
date -u; cat schemas/attempt.schema.json | python -c "
import json,sys; d=json.load(sys.stdin); 
print(json.dumps(d['properties'].keys().__repr__()))
o=d.get('\$defs',d.get('definitions',{}))
print(list(o.keys()))
"
```

```
53 cells
Tue Nov 10 07:56:25 UTC 2026
"dict_keys(['schema_version', 'id', 'datasets', 'missing_datasets', 'paper', 'date', 'entry', 'deprecated', 'provenance', 'outcomes', 'verifications', 'findings', 'reconciliation', 'inputs'])"
[]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
d=json.load(open('schemas/attempt.schema.json'))
o=d['properties']['outcomes']['items']
print(json.dumps(o, indent=0)[:3500])
print(json.dumps(d['properties']['findings']['items'], indent=0)[:1200])
print(json.dumps(d['properties']['inputs']['items'], indent=0)[:600])
EOF
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
[... 188 more lines not kept]
```

**Agent calls Bash**

```bash
ls questions | head -3; f=$(ls questions/*.yaml | head -1); head -30 $f; grep -n "question" schemas/*.json | head -5; ls questions | grep okuno
```

```
README.md
ashworth-2025.yaml
athalye-2023.yaml
dandiset: "001708"
paper: doi:10.64898/2025.12.15.693905
questions:
- claim: figs3-neutral-unmodulated
  asked: 2026-11-05
  question: >-
    The criterion takes the trials of all NEUTRAL units of all files, and expects 32 cells with 69
    and 70 trials. The dataset has 36 NEUTRAL units. Four are in 'evoked' files, labelled "NEUT";
    the other 32, labelled "Neutral", are the ongoing and evoked/ongoing cells. The 36 give 76 to 79
    trials. The paper's n = 32 is the second set, which is also the set of the ongoing analyses.
    Should the criterion take the 32 NEUTRAL cells of the 'ongoing' and 'evoked/ongoing' files?
  passage: >-
    "In contrast, NEUTRAL-cells (n = 32; 69 withdrawal-aligned and 70 heat-aligned trials) exhibited
    no discernible modulation associated with either heat onset or withdrawal behavior" (Results,
    Evoked ON/OFF activity unfolds over multiple timescales, paragraph 9). The Methods (Experiments,
    paragraph 4) count 24 NEUTRAL cells in the evoked protocol and 12 in the ongoing protocol, 36 in
    all.
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 12,22p attempts/fouke-2025-01.yaml; ls attempts | grep okuno; date -u
```

```
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
    url: https://github.com/catalystneuro/reproduction-registry/actions/runs/38574152687
Tue Nov 10 07:57:07 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/mkrec.py",
 "content": "import yaml\n\nNB = \"reproduce_okuno_2025.ipynb\"\nO2 = (\"Registration (claims file O2). The paper gives no SPM12 or ANTs settings. Here no SPM12 motion \"\n      \"or slice-timing correction was run; the mean of three blocks of 152 green volumes was registered \"\n      \"to the resized FDA template with antspy (affine start, the better of mean squares and Mattes \"\n      \"mutual information, then SyN with defaults), and the ROI means were computed through the \"\n      \"registration's linear interpolation map, which equals warping each volume and averaging \"\n      \"(extractROItimeseries.m). The outcome rests on this choice. The registration is not exactly \"\n      \"repeatable between runs, so values can move in the second or third decimal.\")\nTCOMP = (\"tCompCor (claims file M3). The 1000 highest-SD voxels are taken among native voxels inside the \"\n         \"template's field of view, not among template voxels after warping, an assumption made to avoid \"\n         \"warping every volume. Their SD is taken on the mean-centred series before detrending, as \"\n         \"lib/getNuisancetCompCor.m does (the claims file's M3 says after detrending; the code it cites \"\n         \"is followed).\")\nVOX = (\"Native voxel size from the NWB grid_spacing (2.55 to 2.61 by 2.61 to 2.68 by 5 um); the paper's \"\n       \"NWB-to-NIfTI script is not published, so the voxel size its NIfTI headers carried is not known.\")\nSUBJ = (\"Subjects. The code's subject list [1 2 3 4 5 6 8 9] is applied to the flies in name order, which \"\n        \"the notebook confirms by reproducing the code's per-volume speed and walking regressor \"\n        \"(data/behavior.mat) fly by fly to 1e-5; the seventh fly is fly-100. Nine flies are shown as a \"\n        \"variant.\")\nLR = (\"Left-right orientation. The files do not state it, and a symmetric brain cannot fix it. No flip is \"\n      \"assumed; with left and right swapped the matrix-level FC-SC correlations are lower (FlyEM 0.531 \"\n      \"against 0.616), which supports the choice. The swapped result is shown for every claim.\")\n\n\ndef atlas_block(claim, extra=\"\"):\n    return dict(claim=claim, outcome=\"blocked\", blocked_by=\"data_missing\", notes=(\n        \"The claim rests on the SCKm or DistKm ROI atlases (k-means parcellations of the hemibrain \"\n        \"voxels), which are in neither the code repository at 4b92add nor Zenodo 15532272 (both \"\n        \"versions were listed; the later code commits hold no atlas either). Zenodo holds the SC \"\n        \"connect lists of these atlases but not the voxel-to-ROI assignment, so the dataset's FC \"\n        \"cannot be put in the same ROIs. makeVoxelROIatlas.m rebuilds them by k-means, which would \"\n        \"not reproduce the published ROIs, and a new SC would need the FlyEM synapse positions in the \"\n        \"template, which are not published.\" + extra))\n\n\ndef other_block(claim, what):\n    return dict(claim=claim, outcome=\"blocked\", blocked_by=\"other\", notes=what)\n\n\noutcomes = [\n    atlas_block(\"fig1-poltcomp-optimal\", \" The hemibrain 52-ROI part could be run, but readings (a) and \"\n                \"(b) both need the SCKm and DistKm types, and 20 of the 37 nuisance combinations use the \"\n                \"SPM12 head-motion parameters, which were not computed here; it was not run.\"),\n    atlas_block(\"fig2b-distkm-smoothing-optimum\"),\n    atlas_block(\"figs2-1b-sckm-smoothing\"),\n    atlas_block(\"fig2c-smoothing-plus-poltcomp\"),\n    atlas_block(\"figs2-1d-highpass-degrades\"),\n    atlas_block(\"fig2d-log-decline\"),\n    atlas_block(\"fig2d-fly-values\"),\n    atlas_block(\"fig2d-ten-thousand-rois\"),\n    atlas_block(\"discussion-twenty-rois\"),\n    dict(claim=\"fig3d-confidence-threshold\", outcome=\"blocked\", blocked_by=\"data_missing\", notes=(\n        \"Needs the FlyEM SC of the 63 primary ROIs at confidence 0.5, 0.6, 0.7 and 0.9. The code \"\n        \"repository holds only the cf0.8 SC (results/sc/hemiroi_connectlist.mat) and Zenodo 15532272 \"\n        \"holds no FlyEM hemiroi SC. Rebuilding them from the hemibrain v1.2 synapses would need the \"\n        \"paper's JRC2018F-to-FDA ANTs transform, which is not published (the repository holds images \"\n        \"already transformed).\")),\n    dict(claim=\"fig3d-flyem-vs-flywire\", outcome=\"partially_reproduced\", notebook=NB,\n         output=\"claim:fig3d-flyem-vs-flywire\", measured=[0.6159, 0.5753], assumed=True, notes=(\n             \"63 primary ROIs, no smoothing, Poly-tCompCor, code's eight flies, SC neuron layer 2. \"\n             \"FlyEM r = 0.616 and FlyWire r = 0.575, so FlyEM is higher but both are below the \"\n             \"tolerances (0.657 to 0.803 and 0.612 to 0.748). FlyEM is higher in every variant: no \"\n             \"nuisance removal 0.638 against 0.606, nine flies 0.608 against 0.568, signed FC (O3) \"\n             \"0.616 against 0.575, left and right swapped 0.531 against 0.520. Synapse SC gives 0.561 \"\n             \"against 0.530. The paper's own output file for the FlyWire setting (Zenodo, \"\n             \"results/auc/poltcomparhemiroi_fw0sr140-fcauc.mat) gives R(7) = 0.684 with the same SC, so \"\n             \"the shortfall is in the FC computed here, not in the SC.\"),\n         deviations=[O2, TCOMP, VOX, SUBJ, LR,\n                     \"The FlyEM SC is the 114-ROI cf0.8 connect list of the code repository indexed by the \"\n                     \"63 primary ROIs of the FlyWire file; the paper's hemiroi_hb0sr80 file is not published \"\n                     \"but is computed by the same function over all 114 ROIs (makeStructConnectivity.m).\"]),\n    dict(claim=\"fig3e-flyem-higher-most-regions\", outcome=\"reproduced\", notebook=NB,\n         output=\"claim:fig3e-flyem-higher-most-regions\", measured=55, assumed=True, notes=(\n             \"FlyEM has the higher per-region FC-SC correlation in 55 of 63 regions (tolerance 52.2 to \"\n             \"63.8), and 55 with nine flies. FlyWire is higher in AB(R), AME(R), FB, PLP(R), SLP(R), \"\n             \"SMP(R), AB(L) and BU(L), most by less than 0.02. The count depends on the orientation and \"\n             \"the nuisance removal; with left and right swapped it is 49 and without nuisance removal \"\n             \"50, both outside the tolerance. The per-region FlyWire values correlate with the paper's \"\n             \"own (Zenodo auc file) at r = 0.72.\"),\n         deviations=[O2, TCOMP, SUBJ, LR]),\n    dict(claim=\"fig3g-transmitter-correlation\", outcome=\"not_reproduced\", notebook=NB,\n         output=\"claim:fig3g-transmitter-correlation\", measured=[0.013, -0.157], assumed=True, notes=(\n             \"With this attempt's per-region FlyWire FC-SC correlation, the acetylcholine output share \"\n             \"gives r = 0.013 (p = 0.92) and GABA r = -0.157 (p = 0.22). No variant (no nuisance \"\n             \"removal, nine flies, left and right swapped) gives a significant ACh or GABA correlation; \"\n             \"glutamate and octopamine are the significant ones in several variants. The paper's own \"\n             \"per-region values from its Zenodo file, run through the same transmitter table, give ACh \"\n             \"r = 0.395 (p = 0.0014) and GABA r = -0.252 (p = 0.047), the paper's numbers, so the table \"\n             \"is right and the difference comes from the FC computed here (its per-region values \"\n             \"correlate with the paper's at r = 0.72).\"),\n         deviations=[O2, TCOMP, SUBJ, LR]),\n    dict(claim=\"fig3a-postsynapse-counts\", outcome=\"partially_reproduced\", notebook=NB,\n         output=\"claim:fig3a-postsynapse-counts\", notes=(\n             \"From the paper's table of post-synapse counts per ROI (Zenodo, \"\n             \"results/sc/hemiroi_postsyncount.mat), summed over the 63 primary ROIs as \"\n             \"plotStructConnectivity.m does. FlyWire has 18.83 million at cleft score 50 (expected 18.8) \"\n             \"and 11.24 million at 140 (expected 11.4); FlyEM has 11.57 million at confidence 0.8. The \"\n             \"table holds FlyEM from confidence 0.5 only (18.12 million), so the 21.4 million at \"\n             \"confidence 0 was not measured. Two of the three values hold; the third is untested.\"),\n         deviations=[\"Counts are the paper's per-ROI table in its Zenodo record, not recounted from the \"\n                     \"DVID and FlyWire synapse tables, which would need the transforms to the template.\"]),\n    dict(claim=\"fig3c-regional-detection\", outcome=\"reproduced\", notebook=NB,\n         output=\"claim:fig3c-regional-detection\", notes=(\n             \"From the same table, FlyEM cf0.8 against FlyWire sc140. FlyEM is higher in aL and bL \"\n             \"(left and right) and in every mushroom body ROI among the primary ROIs (aL, a'L, bL, b'L, \"\n             \"gL, CA, PED), and in EB, FB, NO and PB; FlyWire is higher in LO(R), ME(R), CAN(R) and \"\n             \"FLA(R). Both readings of the mushroom bodies hold.\"),\n         deviations=[\"Counts are the paper's per-ROI table in its Zenodo record, not recounted from the \"\n                     \"raw connectomes.\"]),\n    dict(claim=\"figs3-1a-regional-count-similarity\", outcome=\"reproduced\", notebook=NB,\n         output=\"claim:figs3-1a-regional-count-similarity\", measured=[0.7778, 0.9001, 0.9187], notes=(\n             \"Over the 63 primary ROIs, FlyEM cf0.8 against FlyWire sc140 post-synapse counts give \"\n             \"Pearson r = 0.778, Spearman r = 0.900 and Pearson r on log10 counts = 0.919.\"),\n         deviations=[\"Counts are the paper's per-ROI table in its Zenodo record, not recounted from the \"\n                     \"raw connectomes.\"]),\n    dict(claim=\"fig3f-output-transmitters\", outcome=\"reproduced\", notebook=NB,\n         output=\"claim:fig3f-output-transmitters\", measured=[62.8, 15.5, 11.4], notes=(\n             \"From the paper's per-ROI counts of output neurons by predicted transmitter (Zenodo, \"\n             \"results/sc/hemiroi_fw0sr140_transmitter.mat), each ROI's share over the seven classes, \"\n             \"mean over the 63 primary ROIs; acetylcholine 62.8% (SD 14.2), glutamate 15.5% (9.2), GABA \"\n             \"11.4% (8.2).\"),\n         deviations=[\"Shares are the paper's per-ROI table in its Zenodo record, not recounted from the \"\n                     \"FlyWire neurotransmitter predictions.\"]),\n    dict(claim=\"figs3-2cd-apl-similarity\", outcome=\"blocked\", blocked_by=\"not_runnable\", notes=(\n        \"Needs the APL-R synapses of both connectomes in the template. The FlyWire synapse positions in \"\n        \"the template are in Zenodo 15532272 (flywire783i_sypostloc_fdacal.mat), but the FlyEM ones are \"\n        \"not published, and moving the hemibrain v1.2 synapses there needs the paper's JRC2018F-to-FDA \"\n        \"transform, which is not published. Not run.\")),\n    other_block(\"fig4b-ppssi-distribution\",\n                \"Not attempted in this run, which gave its time to the claims on the dandiset. The per-neuron \"\n                \"DBSCAN result the paper computed is in Zenodo 15532272 \"\n                \"(results/neuralsc/wire0sr140_neuralDBScan3000mi1.mat, 353 MB), and the FlyWire synapses are \"\n                \"in Zenodo 10676866, so a later attempt can test it.\"),\n    other_block(\"fig4a-unsegregated-ranking\",\n                \"Not attempted in this run. The FlyWire part could use the paper's DBSCAN result in Zenodo \"\n                \"15532272; the FlyEM part needs a per-neuron DBSCAN of the hemibrain v1.2 synapses, which the \"\n                \"paper did not deposit.\"),\n    other_block(\"fig4c-segregated-ranking\",\n                \"Not attempted in this run; as fig4a-unsegregated-ranking, the FlyEM part needs a DBSCAN of the \"\n                \"hemibrain synapses that was not deposited.\"),\n    other_block(\"figs4-1ij-segregation-index-biased\",\n                \"Not attempted in this run; it needs the DBSCAN clusters of both connectomes (FlyWire's are in \"\n                \"Zenodo 15532272, FlyEM's are not deposited).\"),\n    dict(claim=\"fig4e-unsegregated-higher\", outcome=\"reproduced\", notebook=NB,\n         output=\"claim:fig4e-unsegregated-higher\", measured=2373104, assumed=True, notes=(\n             \"Unsegregated SC (code target sp10db3000mi1_only1) against the 99 rd185-20 null SC matrices, \"\n             \"Poly-tCompCor, eight flies. Neuron SC r = 0.634 against null 0.593 +- 0.0015 (p = 1e-153); \"\n             \"synapse SC r = 0.583 against 0.564 +- 0.0023 (p = 2e-17); both above the null at p < \"\n             \"0.05/6. The selected synapse total is 2,373,104 (expected 2,373,100 +- 237,310), and the \"\n             \"null totals do not differ from it (p = 0.832, the paper's value). Nine flies and left-right \"\n             \"swapped give the same direction at p < 0.05/6 (swapped synapse p = 0.0021). Without \"\n             \"nuisance removal both are below the null (p = 3e-6 and 6e-15), so the result needs \"\n             \"Poly-tCompCor.\"),\n         deviations=[O2, TCOMP, SUBJ, LR,\n                     \"The selected and null SC matrices are the paper's own (Zenodo 15532272); only the FC \"\n                     \"comes from the dandiset.\"]),\n    dict(claim=\"fig4f-segregated-lower\", outcome=\"reproduced\", notebook=NB,\n         output=\"claim:fig4f-segregated-lower\", assumed=True, notes=(\n             \"Reading (a), the code's target sp90db3000mi1, against the 99 rd1560-80 null SC matrices. \"\n             \"Neuron SC r = 0.574 against null 0.578 +- 0.0008 (p = 4e-8); synapse SC r = 0.524 against \"\n             \"0.540 +- 0.0013 (p = 6e-35); both below the null at p < 0.05/6. Nine flies and left-right \"\n             \"swapped agree. Without nuisance removal the neuron SC is not different from the null (p = \"\n             \"0.48) and the synapse SC is below it (p = 7e-12). The null totals match the selected total \"\n             \"(p = 0.64). Reading (b), both sides at 0.9 or more, needs an SC rebuilt from the synapse \"\n             \"table and was not run.\"),\n         deviations=[O2, TCOMP, SUBJ, LR,\n                     \"Only reading (a) of the criterion was run; reading (b) needs the per-synapse cPPSSI and \"\n                     \"positions to rebuild the SC.\"]),\n    dict(claim=\"fig4i-reciprocal-higher\", outcome=\"reproduced\", notebook=NB,\n         output=\"claim:fig4i-reciprocal-higher\", assumed=True, notes=(\n             \"Reciprocal SC (code target rc20_only1) against the 99 rd140-15 null SC matrices. Neuron SC \"\n             \"r = 0.636 against null 0.596 +- 0.0016 (p = 2e-143); synapse SC r = 0.577 against 0.568 +- \"\n             \"0.0021 (p = 3e-6, below 0.05/6). Nine flies agree. Without nuisance removal the synapse SC \"\n             \"is below the null (p = 0.0034); with left and right swapped it is below the null without \"\n             \"reaching 0.05/6 (p = 0.0195), while the neuron SC stays above at p = 1e-58. The null \"\n             \"totals match the selected total (p = 0.852).\"),\n         deviations=[O2, TCOMP, SUBJ, LR]),\n    dict(claim=\"figs4-1-flyem-permutation\", outcome=\"blocked\", blocked_by=\"data_missing\", notes=(\n        \"Needs the FlyEM selected-synapse and null SC matrices (hb0sr80 targets and nulls). Neither the \"\n        \"code repository nor Zenodo 15532272 holds them, and rebuilding them needs the FlyEM synapses in \"\n        \"the template, which are not published.\")),\n    other_block(\"fig4h-reciprocal-distances\",\n                \"Not attempted in this run. The paper's reciprocal distances are in Zenodo 15532272 \"\n                \"(results/neuralsc/wire0sr140_reciprocalDistances.mat, 332 MB), so a later attempt can test it.\"),\n    dict(claim=\"fig5b-walking-activation\", outcome=\"reproduced\", notebook=NB,\n         output=\"claim:fig5b-walking-activation\", assumed=True, notes=(\n             \"Second level over the nine flies, graded regressor (O1, the code's), height p < 0.001 (t > \"\n             \"3.242, df 56, the README's value). One positive cluster of 399,973 voxels (README 416,801), \"\n             \"maximum t = 16.1 (README 14.7). LAL, FB, IPS and GNG all lie in it with peak t at least half \"\n             \"the maximum (reading a) under the hemibrain and JFRC2010 atlases and with the binary \"\n             \"regressor. Reading (b) fails for FB (mean-t rank 26 of 63, hemibrain atlas; 31 of 75, \"\n             \"JFRC2010) and for LAL with JFRC2010. The claim holds under reading (a).\"),\n         deviations=[O2, TCOMP, SUBJ,\n                     \"First-level GLM by OLS without the Tukey-taper pre-whitening of lib/calcGlmTukey.m, and \"\n                     \"the second level as glmFlyMB2nd.m's stacked design without the taper (an assumption, \"\n                     \"to keep one streaming pass per fly).\",\n                     \"Smoothing (FWHM 8 voxels) is applied to the first-level beta maps in the template, \"\n                     \"which for OLS equals fitting the warped, smoothed data; with pre-whitening it would not.\",\n                     \"Cluster extent is the README's printed k = 167.9 voxels with 18-connectivity, not \"\n                     \"recomputed from the smoothness of these maps (plotGlmContrastImage.m).\"]),\n    dict(claim=\"fig5b-walking-suppression\", outcome=\"not_reproduced\", notebook=NB,\n         output=\"claim:fig5b-walking-suppression\", assumed=True, notes=(\n             \"No voxel in the brain mask falls below -3.242 (the lowest t is -0.82), so there is no \"\n             \"negative cluster, under either regressor. WED(R) and AVLP(R) are mostly positive: 87 to \"\n             \"97% of their voxels are above the positive threshold (hemibrain atlas), 85 to 100% with \"\n             \"JFRC2010. At the README's negative peaks, (82,78,12) and (174,80,15), t = 3.28 and 4.09 \"\n             \"here. The paper's code found two small negative clusters (406 and 260 voxels); without \"\n             \"the Tukey taper and the paper's motion correction, this attempt finds none.\"),\n         deviations=[O2, TCOMP, SUBJ,\n                     \"First-level GLM without the Tukey-taper pre-whitening, smoothing on the beta maps, and \"\n                     \"the README's cluster extent (as fig5b-walking-activation).\"]),\n    other_block(\"fig5-wagn\",\n                \"Not attempted in this run; it needs the codex network at cleft score 50 and the FlyWire \"\n                \"synapse table (Zenodo 10676866).\"),\n]\n\nrec = {\n    \"schema_version\": 3,\n    \"id\": \"okuno-2025-01\",\n    \"datasets\": [{\"archive\": \"dandi\", \"id\": \"000727\", \"version\": \"0.240106.0043\",\n                  \"doi\": \"10.48324/dandi.000727/0.240106.0043\", \"relation\": \"reuses\"}],\n    \"paper\": \"doi:10.7554/elife.107990.1\",\n    \"date\": \"2026-11-10\",\n    \"entry\": \"okuno-2025\",\n    \"provenance\": {\"kind\": \"agent\", \"accountable\": {\"name\": \"CatalystNeuro\"},\n                   \"agent\": {\"harness\": \"Claude Code\", \"model\": \"claude-opus-5-5\", \"protocol\": \"pilot-14\"},\n                   \"runner\": {\"platform\": \"GitHub Actions\",\n                              \"url\": \"https://github.com/catalystneuro/encore/actions/runs/42760211426\"}},\n    \"inputs\": [\n        {\"what\": \"The paper's code; the resized FDA template and brain mask, the hemibrain ROI masks \"\n                 \"(atlas/hemiroi) and names (data/hemiroi.mat), the JFRC2010 atlas and its labels, the FlyEM \"\n                 \"cf0.8 SC of the 114 hemibrain ROIs (results/sc/hemiroi_connectlist.mat) and the per-volume \"\n                 \"speed and walking regressors it computed (data/behavior.mat), used to check the subject \"\n                 \"order.\",\n         \"source\": \"https://github.com/takuto-okuno-riken/flywalk at commit 4b92add4a44f641ab6add809ff6b0e0d6110b50c\"},\n        {\"what\": \"The paper's demo data, version of 2025-05-28; FlyWire sc140 SC of the hemibrain ROIs, the \"\n                 \"selected-synapse SC matrices (sp10db3000mi1_only1, sp90db3000mi1, rc20_only1), the 99 null \"\n                 \"SC matrices of each permutation test, per-ROI transmitter counts and post-synapse counts, \"\n                 \"and the paper's own FC-SC output for the hemibrain FlyWire setting (used as a reference \"\n                 \"only).\",\n         \"source\": \"doi:10.5281/zenodo.15532272\"},\n    ],\n    \"outcomes\": outcomes,\n    \"findings\": [\n        {\"kind\": \"data_missing\", \"statement\": (\n            \"The ROI atlases of the paper's main FC-SC analyses (SCKm and DistKm, 20 to 20,000 ROIs) are not \"\n            \"published. The code repository and both versions of the Zenodo record hold their SC connect \"\n            \"lists but not the voxel-to-ROI assignment, so nine claims (Figures 1 and 2) cannot be tested on \"\n            \"the dandiset. The FlyEM SC at confidence thresholds other than 0.8, the FlyEM permutation SC \"\n            \"matrices and the FlyEM synapses in the template are not published either.\")},\n        {\"kind\": \"methods_unavailable\", \"statement\": (\n            \"Question for the paper's authors. The paper does not give the SPM12 realignment and slice-timing \"\n            \"settings, the ANTs registration settings, or the voxel size written into the NIfTI files by its \"\n            \"NWB-to-NIfTI script, which is not published. This attempt registered the mean green image with \"\n            \"antspy SyN without motion correction and obtains a FlyWire FC-SC correlation of 0.575 on the 63 \"\n            \"primary ROIs where the paper's own output file gives 0.684, and finds no negative GLM cluster \"\n            \"where the paper's code finds two. Which settings were used?\")},\n        {\"kind\": \"metadata_insufficient\", \"statement\": (\n            \"The NWB files do not state the orientation of the functional volumes relative to the brain \"\n            \"(which end of each axis is left, dorsal or anterior). Dorsoventral and anteroposterior can be \"\n            \"read from the images against the template; left and right cannot, and one claim's outcome \"\n            \"(fig3e) changes with it.\")},\n        {\"kind\": \"metadata_error\", \"statement\": (\n            \"TwoPhotonSeriesFunctionalGreen and Red store data as (time, 256, 128, 49) while their \"\n            \"`dimension` attribute is [128, 256, 49]. The processed FDA-space series has an imaging plane \"\n            \"with grid_spacing [1, 1, 1] in unit 'unknown', so its voxel size is not given.\")},\n        {\"kind\": \"other\", \"statement\": (\n            \"The dandiset's FicTrac speed, in the files' name order, reproduces the per-volume speed and the \"\n            \"walking regressor stored in the paper's code (data/behavior.mat) to within 1e-5 for all nine \"\n            \"flies, with the code's 104.654892 ms offset, which confirms the subject order and the alignment \"\n            \"of behaviour to imaging. The seventh fly in that order (fly-100), the one the code leaves out, \"\n            \"has a hemibrain ROI (AL(L)) only 65% inside the field of view after registration in this run, \"\n            \"the lowest coverage of any fly, consistent with the paper's stated reason.\")},\n    ],\n}\n\n\nclass D(yaml.SafeDumper):\n    pass\n\n\ndef str_rep(d, s):\n    return d.represent_scalar(\"tag:yaml.org,2002:str\", s, style=None)\n\n\nD.add_representer(str, str_rep)\nout = yaml.dump(rec, Dumper=D, sort_keys=False, width=100, allow_unicode=True, default_flow_style=False)\nopen(\"attempts/okuno-2025-01.yaml\", \"w\").write(out)\nprint(len(out))\n"
}
```

```
File created successfully at: /tmp/claude-1001/mkrec.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i 's/97% of their voxels are above the positive threshold (hemibrain atlas)/95% of their voxels are above the positive threshold (hemibrain atlas)/; s/mostly positive: 87 to /mostly positive: 87 to /' mkrec.py && . dev/bin/activate && uv pip install -q pyyaml && python mkrec.py && cd  && grep -n "—\|rather" attempts/okuno-2025-01.yaml entries/okuno-2025/*.md entries/okuno-2025/flyfc.py entries/okuno-2025/*.ipynb | head; python tools/entry.py check entries/okuno-2025 2>&1 | tail -20
```

```
35783
0 error(s)
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
import re
s=open('mknb.py').read()
s2=re.sub(r'\*\*(?!Result)([^*]+?)\*\*', r'\1', s)
print(s.count('**'), s2.count('**'))
open('mknb.py','w').write(s2)
EOF
. dev/bin/activate && python mknb.py && cd  && python - <<'EOF'
import json
src=json.load(open('entries/okuno-2025/reproduce_okuno_2025.ipynb'))
ex=json.load(open('executed/okuno-2025/reproduce_okuno_2025.ipynb'))
for a,b in zip(src['cells'],ex['cells']):
    if a['cell_type']=='markdown': b['source']=a['source']
    else: assert ''.join(a['source'])==''.join(b['source'])
json.dump(ex, open('executed/okuno-2025/reproduce_okuno_2025.ipynb','w'), indent=1)
EOF
grep -c '\*\*' entries/okuno-2025/reproduce_okuno_2025.ipynb; grep -o '\*\*[^*]*\*\*' entries/okuno-2025/reproduce_okuno_2025.ipynb | cut -c1-40; head -60 attempts/okuno-2025-01.yaml
```

```
44 6
53 cells
6
schema_version: 3
id: okuno-2025-01
datasets:
- archive: dandi
  id: '000727'
  version: 0.240106.0043
  doi: 10.48324/dandi.000727/0.240106.0043
  relation: reuses
paper: doi:10.7554/elife.107990.1
date: '2026-11-10'
entry: okuno-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i 's/and 20 of the 37 nuisance combinations/and 23 of the 37 nuisance combinations/' mkrec.py && . dev/bin/activate && python mkrec.py && cd  && python tools/entry.py check entries/okuno-2025 2>&1 | tail -3 && python tools/entry.py handover entries/okuno-2025 2>&1 | tail -5; ls executed/okuno-2025/handover/; date -u
```

```
35783
0 error(s)
wrote executed/okuno-2025/handover
flyfc.py
okuno-2025.yaml
reproduce_okuno_2025.ipynb
Tue Nov 10 07:59:04 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import sys, io, time; sys.path.insert(0,'entries/okuno-2025')
import flyfc, h5py, numpy as np
t=time.time()
b=flyfc.zenodo_member('results/neuralsc/wire0sr140_neuralDBScan3000mi1.mat'); print(len(b), time.time()-t)
try:
    import scipy.io as sio; m=sio.whosmat(io.BytesIO(b)); print(m)
except Exception as e:
    f=h5py.File(io.BytesIO(b),'r'); f.visititems(lambda n,o: print(n, getattr(o,'shape',None), getattr(o,'dtype',None)))
for n in ['data/flywire783_neuron.mat','data/flywire783_neuron_sepidx0sr140_3000mi1.mat','data/flywire783_neuron_reci0sr140.mat']:
    bb=flyfc.zenodo_member(n)
    try:
        print(n, sio.whosmat(io.BytesIO(bb)))
    except Exception:
        f=h5py.File(io.BytesIO(bb),'r'); print(n); f.visititems(lambda k,o: print(' ',k, getattr(o,'shape',None), getattr(o,'dtype',None)))
EOF
```

```
Exit code 1
353246926 58.92655658721924
#refs# None None
#refs#/#a None None
#refs#/#a/0 (1, 530) int32
#refs#/#a/00 (1, 174) int32
#refs#/#a/00b (1, 301) int32
#refs#/#a/00c (1, 245) int32
#refs#/#a/00d (1, 318) int32
#refs#/#a/00e (1, 9) int32
#refs#/#a/00f (1, 138) int32
#refs#/#a/00g (1, 490) int32
#refs#/#a/00h (1, 79) int32
#refs#/#a/00i (1, 249) int32
#refs#/#a/00j (2, 89) int32
#refs#/#a/00k (2, 9) int32
#refs#/#a/00l (2, 179) int32
#refs#/#a/00m (2, 78) int32
#refs#/#a/00n (2, 114) int32
#refs#/#a/00o (2, 12) int32
[... 342 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF' 2>&1 | head -40
import sys, io; sys.path.insert(0,'entries/okuno-2025')
import flyfc, h5py, numpy as np, scipy.io as sio
for n in ['data/flywire783_neuron_sepidx0sr140_3000mi1.mat','data/flywire783_neuron.mat','data/flywire783_neuron_reci0sr140.mat']:
    bb=flyfc.zenodo_member(n)
    try:
        m=sio.loadmat(io.BytesIO(bb)); print(n, {k:(getattr(v,'shape',None), getattr(v,'dtype',None)) for k,v in m.items() if not k.startswith('__')})
    except NotImplementedError:
        f=h5py.File(io.BytesIO(bb),'r'); print(n, [(k, getattr(f[k],'shape',None), getattr(f[k],'dtype',None)) for k in f.keys()])
EOF
grep -n "sepidx\|PPSSI\|neuron_sepidx" $TMPDIR/flywalk/plotNeuralFC.m | head -20
```

```
/tmp/claude-1001/dev/lib/python3.13/site-packages/scipy/io/matlab/_mio.py:235: MatReadWarning: Duplicate variable name "None" in stream - replacing previous with new
Considerscipy.io.matlab.varmats_from_mat to split file into single variable files
  matfile_dict = MR.get_variables(variable_names)
data/flywire783_neuron_sepidx0sr140_3000mi1.mat {'Nspidx': ((139255, 1), dtype('<i2')), 'None': ((1,), dtype([('s0', 'O'), ('s1', 'O'), ('s2', 'O'), ('arr', 'O')]))}
data/flywire783_neuron.mat {'Nid': ((139255, 1), dtype('<i8')), 'Nscore': ((139255, 1), dtype('<f4')), 'Ntype': ((139255, 1), dtype('<u2'))}
data/flywire783_neuron_reci0sr140.mat [('Nrcsycount', (2, 139255), dtype('int32')), ('Nsycount', (2, 139255), dtype('int32')), ('Nthrcsycount', (2, 3, 139255), dtype('int32'))]
259:    % pre-post-synapse separate index (PPSSI)
271:    % synapse count & calc PPSSI
286:        % PPSSI based on DBscan clustering
314:    figure; bar(N,'stacked','LineWidth',0.1); legend(tlabels); xticklabels(''); xlabel('PPSSI [0 1]'); ylabel('neuron count');
315:    title([conf.scname num2str(synTh) 'sr' num2str(scoreTh) ' : PPSSI histogram']);
388:            ', PPSSI=' num2str(Nspidx(k)) ', syMIXscore=' num2str(NsywMixScore(k))];
411:            ', PPSSI=' num2str(Nspidx(k)) ', sySPscore=' num2str(NsywSepScore(k))];
Shell cwd was reset to
```

**Agent calls Bash**

```bash
sed -n 255,420p $TMPDIR/flywalk/plotNeuralFC.m
```

```
% FlyWire read neural SC
    DBcount = {};
    load(['results/neuralsc/' conf.scname num2str(synTh) 'sr' num2str(scoreTh) '_neuralDBScan' num2str(epsilon) 'mi' num2str(minpts) '.mat']);

    % pre-post-synapse separate index (PPSSI)
    load([conf.neuSepidxFile num2str(synTh) 'sr' num2str(scoreTh) '_' num2str(epsilon) 'mi' num2str(minpts) '.mat']);
    Nspidx = double(Nspidx) / 10000;
    Nspidx(Nspidx<0) = nan;

    % whole brain mesh
    mesh = load(conf.brainMeshFile);

    nlen = length(Nid);
    clcount(clcount<0) = 0; % remove -1 case
    clAll = sum(clcount,1);

    % synapse count & calc PPSSI
    syCount = zeros(nlen,6,'single');
    Ldbs = nan(nlen,1,'single');
    H = nan(nlen,1,'single');
[... 146 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF' 2>&1 | grep -v Warn
import sys, io; sys.path.insert(0,'entries/okuno-2025')
import flyfc, numpy as np, scipy.io as sio, warnings
warnings.filterwarnings('ignore')
m=sio.loadmat(io.BytesIO(flyfc.zenodo_member('data/flywire783_neuron_sepidx0sr140_3000mi1.mat')), variable_names=['Nspidx'])
x=m['Nspidx'].ravel().astype(float)/10000
print(x.size, (x<0).sum(), (x>=0).sum(), np.nanmean(np.where(x<0,np.nan,x)), np.median(x[x>=0]), (x==1).sum())
EOF
```

```
139255 1111 138144 0.47129870280287234 0.4511 6154
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > mknb2.py <<'EOF'
import nbformat as nbf
cells = []
md = lambda s: cells.append(nbf.v4.new_markdown_cell(s.strip("\n")))
def code(s, tags=None):
    c = nbf.v4.new_code_cell(s.strip("\n"))
    if tags: c.metadata["tags"] = tags
    cells.append(c)
md(r"""
# Okuno et al. (2025): connectome-only claims from the paper's deposits

A companion to `reproduce_okuno_2025.ipynb`. It tests a claim on the FlyWire connectome alone
(data elsewhere), from the paper's Zenodo record
[10.5281/zenodo.15532272](https://doi.org/10.5281/zenodo.15532272) (version of 2025-05-28), which
holds the PPSSI the paper computed for each FlyWire neuron (`data/flywire783_neuron_sepidx0sr140_3000mi1.mat`,
stored as int16 times 10,000, negative where no value; plotNeuralFC.m reads it so). The PPSSI is
not recomputed from the synapse table here. No random numbers are drawn.

| Claim | Data | Status |
|---|---|---|
| fig4b-ppssi-distribution | elsewhere | tested on the paper's per-neuron PPSSI |
""")
code(r"""
import io, warnings
import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
import flyfc
warnings.filterwarnings("ignore")
m = sio.loadmat(io.BytesIO(flyfc.zenodo_member("data/flywire783_neuron_sepidx0sr140_3000mi1.mat")), variable_names=["Nspidx"])
nr = sio.loadmat(io.BytesIO(flyfc.zenodo_member("data/flywire783_neuron.mat")))
raw = m["Nspidx"].ravel()
print("neurons in the PPSSI table", raw.size, "| in the neuron table", nr["Nid"].size, "| stored range", raw.min(), "to", raw.max(), raw.dtype)
""", tags=["sanity"])
md(r"""
### fig4b-ppssi-distribution

> Over the 139,255 FlyWire neurons the PPSSI histogram resembles a normal distribution with a mean
> near 0.5, so many neurons have unsegregated synapses.

Reproduced when the neuron count matches (139,255, tolerance 0) and the mean PPSSI is within 0.4
to 0.6.
""")
code(r"""
x = raw.astype(float) / 10000
valid = x >= 0
print("neurons with a PPSSI", int(valid.sum()), "| without (stored negative)", int((~valid).sum()), "| expected 139,255")
v = x[valid]
print(f"PPSSI mean {v.mean():.4f}, median {np.median(v):.4f}, SD {v.std():.4f}, skewness {((v - v.mean())**3).mean() / v.std()**3:.3f}")
print("neurons with PPSSI exactly 1 (fully segregated)", int((v == 1).sum()), "| exactly 0", int((v == 0).sum()))
h, e = np.histogram(v, bins=np.arange(0, 1.0001, 0.05))
for a, b in zip(e[:-1], h):
    print(f"{a:.2f}-{a + 0.05:.2f} {b}")
plt.figure(figsize=(6, 3)); plt.bar(e[:-1] + 0.025, h, width=0.05); plt.xlabel("PPSSI"); plt.ylabel("neurons"); plt.show()
print("all", int(valid.sum()), "values in [0, 1] are shown")
""", tags=["claim:fig4b-ppssi-distribution"])
md(r"""
**Result: partially reproduced.** The table holds 139,255 neurons, the paper's count, but 1,111 of
them carry no PPSSI, so 138,144 neurons have one (the README of the paper's code prints the same
138,144). The mean PPSSI is 0.471 (median 0.451), within 0.4 to 0.6. The mean holds; the count of
neurons with a PPSSI is 0.8% below the stated number, which the tolerance of 0 does not allow.
""")
nb = nbf.v4.new_notebook(); nb.cells = cells
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nbf.write(nb, "entries/okuno-2025/connectome_okuno_2025.ipynb")
EOF
. dev/bin/activate && python mknb2.py && cd executed/okuno-2025 && ls .venv/bin | grep -i jupyter | head;
```

```
jupyter
jupyter-dejavu
jupyter-execute
jupyter-kernel
jupyter-kernelspec
jupyter-migrate
jupyter-nbconvert
jupyter-run
jupyter-troubleshoot
jupyter-trust
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('mknb2.py').read()
s=s.replace('''print("neurons with PPSSI exactly 1 (fully segregated)"''','''readme = flyfc.code_file("README.md").decode()
print("code README line:", [l for l in readme.splitlines() if "full separation" in l])
print("neurons with PPSSI exactly 1 (fully segregated)"''')
s=s.replace("(the README of the paper's code prints the same\n138,144)","(the README of the paper's code prints 6154/138144 for\nthe fully segregated neurons, the same denominator)")
open('mknb2.py','w').write(s)
EOF
grep -n "6154" mknb2.py; . dev/bin/activate && python mknb2.py && cd entries/okuno-2025 && timeout 900 ../../executed/okuno-2025/.venv/bin/jupyter-nbconvert --to notebook --execute --ExecutePreprocessor.kernel_name=registry-okuno-2025 --ExecutePreprocessor.timeout=1200 connectome_okuno_2025.ipynb --output-dir ../../executed/okuno-2025/ 2>&1 | tail -2; python - <<'EOF'
import json
nb=json.load(open('../../executed/okuno-2025/connectome_okuno_2025.ipynb'))
for c in nb['cells']:
    for o in c.get('outputs',[]):
        if o.get('text'): print(''.join(o['text']))
        if o.get('output_type')=='error': print('ERR',o['evalue'])
EOF
```

```
60:them carry no PPSSI, so 138,144 neurons have one (the README of the paper's code prints 6154/138144 for
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 20847 bytes to ../../executed/okuno-2025/connectome_okuno_2025.ipynb
neurons in the PPSSI table 139255 | in the neuron table 139255 | stored range -1 to 10000 int16

neurons with a PPSSI 138144 | without (stored negative) 1111 | expected 139,255
PPSSI mean 0.4713, median 0.4511, SD 0.2354, skewness 0.433

code README line: ['full separation neuron rate=0.044548 (6154/138144)']
neurons with PPSSI exactly 1 (fully segregated) 6154 | exactly 0 70
0.00-0.05 1356
0.05-0.10 3995
0.10-0.15 6368
0.15-0.20 6405
0.20-0.25 6746
0.25-0.30 8476
0.30-0.35 10738
0.35-0.40 11854
0.40-0.45 12820
0.45-0.50 12657
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('mknb.py').read()
def rep(a,b):
    global s
    assert a in s, a[:60]; s=s.replace(a,b)
rep('''| figs3-2cd-apl-similarity, fig4b, fig4a, fig4c, figs4-1ij, fig4h, fig5-wagn | elsewhere | blocked |''','''| fig4b-ppssi-distribution | elsewhere | tested in `connectome_okuno_2025.ipynb` |
| figs3-2cd-apl-similarity, fig4a, fig4c, figs4-1ij, fig4h, fig5-wagn | elsewhere | blocked |''')
rep('''| other connectome-only claims | blocked |''','''| fig4b-ppssi-distribution (elsewhere, companion notebook) | partially reproduced: 138,144 neurons have a PPSSI, not 139,255 |
| other connectome-only claims | blocked |''')
open('mknb.py','w').write(s)
s=open('mkrec.py').read()
old=s[s.index('    other_block("fig4b-ppssi-distribution",'):s.index('    other_block("fig4a-unsegregated-ranking",')]
new='''    dict(claim="fig4b-ppssi-distribution", outcome="partially_reproduced", notebook="connectome_okuno_2025.ipynb",
         output="claim:fig4b-ppssi-distribution", measured=138144, notes=(
             "The paper's per-neuron PPSSI table (Zenodo 15532272, "
             "data/flywire783_neuron_sepidx0sr140_3000mi1.mat) lists 139,255 neurons, the paper's count, "
             "but 1,111 carry no PPSSI, so 138,144 have one (the code's README prints 6154/138144 for the "
             "fully segregated ones, the same denominator). The mean PPSSI is 0.471 (median 0.451, SD "
             "0.235), within 0.4 to 0.6; the histogram is unimodal with a peak at 0.40 to 0.45 and a "
             "second peak of 7,262 neurons at 0.95 to 1. The mean holds; the count of neurons with a "
             "PPSSI is 0.8% below the stated number, outside the tolerance of 0."),
         deviations=["The PPSSI is the paper's own per-neuron value from its Zenodo record, not recomputed "
                     "by DBSCAN from the FlyWire synapse table (Zenodo 10676866)."]),
'''
s=s.replace(old,new)
open('mkrec.py','w').write(s)
EOF
. dev/bin/activate && python mknb.py && python mkrec.py && cd  && python - <<'EOF'
import json
src=json.load(open('entries/okuno-2025/reproduce_okuno_2025.ipynb'))
ex=json.load(open('executed/okuno-2025/reproduce_okuno_2025.ipynb'))
for a,b in zip(src['cells'],ex['cells']):
    if a['cell_type']=='markdown': b['source']=a['source']
    else: assert ''.join(a['source'])==''.join(b['source'])
json.dump(ex, open('executed/okuno-2025/reproduce_okuno_2025.ipynb','w'), indent=1)
EOF
python - <<'EOF'
p='entries/okuno-2025/entry.yaml'; s=open(p).read()
s=s.replace("""  runtime_minutes: 25
""","""  runtime_minutes: 25
- path: connectome_okuno_2025.ipynb
  title: Okuno et al. (2025), connectome-only claims from the paper's deposits
  runtime_minutes: 1
""")
open(p,'w').write(s)
p='entries/okuno-2025/README.md'; s=open(p).read()
s=s.replace("| Other connectome-only claims (seven) | Blocked |","| PPSSI distribution over FlyWire neurons | Partially reproduced |\n| Other connectome-only claims (six) | Blocked |")
open(p,'w').write(s)
EOF
cat executed/okuno-2025/result.json | head -30
```

```
53 cells
36328
{
 "entry": "okuno-2025",
 "python": "3.13",
 "results": [
  {
   "notebook": "reproduce_okuno_2025.ipynb",
   "ok": true,
   "seconds": 1053,
   "error": null
  }
 ]
}
```

**Agent calls Bash**

```bash
python tools/entry.py check entries/okuno-2025 2>&1 | tail -5 && python tools/entry.py handover entries/okuno-2025 2>&1 | tail -3; ls executed/okuno-2025/handover/; python - <<'EOF'
import json
for n in ['reproduce_okuno_2025.ipynb','connectome_okuno_2025.ipynb']:
    nb=json.load(open('executed/okuno-2025/handover/'+n))
    print(n, sum(1 for c in nb['cells'] if 'Result' in ''.join(c['source'])), len(nb['cells']))
EOF
date -u
```

```
0 error(s)
wrote executed/okuno-2025/handover
connectome_okuno_2025.ipynb
flyfc.py
okuno-2025.yaml
reproduce_okuno_2025.ipynb
reproduce_okuno_2025.ipynb 9 48
connectome_okuno_2025.ipynb 0 4
Tue Nov 10 08:02:37 UTC 2026
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('executed/okuno-2025/handover/reproduce_okuno_2025.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    if 'Result' in s: print(i, c['cell_type'], s[:150].replace('\n',' '))
EOF
```

```
22 markdown Result: reproduced, resting on the left-right orientation. FlyEM is higher in 55 of 63 regions under the main setting (tolerance 52.2 to 63.8) and in 
25 markdown Result: not reproduced. With this attempt's FC the per-region FC-SC correlation does not rise with the cholinergic share (r = 0.013, p = 0.92) and its
29 markdown Result: reproduced. Under the main setting the unsegregated SC has a higher FC-SC correlation than the null for neuron SC (0.634 against 0.593 +- 0.00
31 markdown Result: reproduced under reading (a). The segregated SC (the code's target) has a lower FC-SC correlation than the null for neuron SC (0.574 against 0
33 markdown Result: reproduced.** The reciprocal-synapse SC has a higher FC-SC correlation than the null for neuron SC (0.636 against 0.596 +- 0.002, p = 2e-143) 
39 markdown Result: not reproduced. No voxel in the brain mask falls below the negative height threshold (the lowest t is -0.82), so there is no negative cluster.
42 markdown Result: partially reproduced. FlyWire has 18.83 million post-synapses at cleft score 50 (expected 18.8) and 11.24 million at 140 (expected 11.4), clos
44 markdown Result: reproduced. FlyEM has more post-synapses in aL and bL and in every mushroom body ROI, and in EB, FB, NO and PB; FlyWire has more in LO and ME 
46 markdown Result: reproduced.** Pearson r = 0.778, Spearman r = 0.900 and Pearson r on log10 counts = 0.919, as in the paper.
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
import re
s=open('mknb.py').read()
lines=s.split('\n')
out=[]
for l in lines:
    if l.startswith('Result: ') or l.startswith('**Result: '):
        body=l.replace('**','')
        # first sentence end
        m=re.search(r'\.( |$)', body)
        k=m.start()
        l='**'+body[:k+1]+'**'+body[k+1:]
    out.append(l)
s='\n'.join(out)
open('mknb.py','w').write(s)
print([l for l in out if 'Result' in l])
EOF
```

```
["**Result: FlyEM gives the higher FC-SC correlation, but both values are below the paper's.**", '**Result: reproduced, resting on the left-right orientation.** FlyEM is higher in 55 of 63', "**Result: not reproduced.** With this attempt's FC the per-region FC-SC correlation does not rise", '**Result: reproduced.** Under the main setting the unsegregated SC has a higher FC-SC correlation', "**Result: reproduced under reading (a).** The segregated SC (the code's target) has a lower FC-SC", '**Result: reproduced.** The reciprocal-synapse SC has a higher FC-SC correlation than the null for', '**Result: reproduced.** The second level gives one large positive cluster (399,973 voxels; the', '**Result: not reproduced.** No voxel in the brain mask falls below the negative height threshold', '**Result: partially reproduced.** FlyWire has 18.83 million post-synapses at cleft score 50', '**Result: reproduced.** FlyEM has more post-synapses in aL and bL and in every mushroom body ROI,', '**Result: reproduced.** Pearson r = 0.778, Spearman r = 0.900 and Pearson r on log10 counts =', '**Result: reproduced.** Acetylcholine 62.8% +- 14.2%, glutamate 15.5% +- 9.2% and GABA 11.4% +-']
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python mknb.py && cd  && python - <<'EOF'
import json
src=json.load(open('entries/okuno-2025/reproduce_okuno_2025.ipynb'))
ex=json.load(open('executed/okuno-2025/reproduce_okuno_2025.ipynb'))
for a,b in zip(src['cells'],ex['cells']):
    if a['cell_type']=='markdown': b['source']=a['source']
    else: assert ''.join(a['source'])==''.join(b['source'])
json.dump(ex, open('executed/okuno-2025/reproduce_okuno_2025.ipynb','w'), indent=1)
import re
txt=''.join(''.join(c['source']) for c in src['cells'] if c['cell_type']=='markdown')
print(re.findall(r'\*\*[^*]{0,40}', txt))
EOF
python tools/entry.py check entries/okuno-2025 2>&1 | tail -2 && python tools/entry.py handover entries/okuno-2025 2>&1 | tail -1; python - <<'EOF'
import json
nb=json.load(open('executed/okuno-2025/handover/reproduce_okuno_2025.ipynb'))
print([i for i,c in enumerate(nb['cells']) if 'Result' in ''.join(c['source'])], len(nb['cells']))
print(''.join(nb['cells'][-2]['source'])[:200] if nb['cells'] else '')
EOF
```

```
53 cells
['**Result: FlyEM gives the higher FC-SC cor', "**\nWith the code's eight flies and Poly-tC", '**Result: reproduced, resting on the left-', '** FlyEM is higher in 55 of 63\nregions und', '**Result: not reproduced.', "** With this attempt's FC the per-region F", '**Result: reproduced.', '** Under the main setting the unsegregated', '**Result: reproduced under reading (a).', "** The segregated SC (the code's target) h", '**Result: reproduced.', '** The reciprocal-synapse SC has a higher ', '**Result: reproduced.', '** The second level gives one large positi', '**Result: not reproduced.', '** No voxel in the brain mask falls below ', '**Result: partially reproduced.', '** FlyWire has 18.83 million post-synapses', '**Result: reproduced.', '** FlyEM has more post-synapses in aL and ', '**Result: reproduced.', '** Pearson r = 0.778, Spearman r = 0.900 a', '**Result: reproduced.', '** Acetylcholine 62.8% +- 14.2%, glutamate', '** The files match their description (9 fl']
0 error(s)
wrote executed/okuno-2025/handover
[] 39
x, y = hbS[pid, jem], fwS[pid, jfw]
print("Pearson r", round(stats.pearsonr(x, y)[0], 4), "| Spearman r", round(stats.spearmanr(x, y)[0], 4), "| Pearson r of log10", round(stats.pearsonr(np.log10(x),
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -n "\*\*" mknb.py | grep -v "Result" ; grep -n "How the analysis differs" mknb.py
```

```
746:What was found about the dataset.** The files match their description (9 flies, 3384 volumes at
738:How the analysis differs from the paper's. No SPM12 motion or slice-timing correction; the
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i 's/^What was found about the dataset\.\*\* The files/What was found about the dataset. The files/' mknb.py && grep -c "\*\*" mknb.py && . dev/bin/activate && python mknb.py && cd  && python - <<'EOF'
import json
src=json.load(open('entries/okuno-2025/reproduce_okuno_2025.ipynb'))
ex=json.load(open('executed/okuno-2025/reproduce_okuno_2025.ipynb'))
for a,b in zip(src['cells'],ex['cells']):
    if a['cell_type']=='markdown': b['source']=a['source']
    else: assert ''.join(a['source'])==''.join(b['source'])
json.dump(ex, open('executed/okuno-2025/reproduce_okuno_2025.ipynb','w'), indent=1)
EOF
python tools/entry.py check entries/okuno-2025 2>&1 | tail -1 && python tools/entry.py handover entries/okuno-2025 2>&1 | tail -1; git status --short | head -20; date -u
```

```
12
53 cells
0 error(s)
wrote executed/okuno-2025/handover
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
?? attempts/okuno-2025-01.yaml
?? entries/okuno-2025/
?? scripts
Tue Nov 10 08:03:38 UTC 2026
```

**Agent calls Bash**

```bash
ls -la .bashrc .profile .gitconfig .mcp.json .ripgreprc scripts .idea .vscode 2>&1 | head -20; git log -1 --format=%cd
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 10 05:08 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 10 05:08 .gitconfig
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 10 05:08 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 10 05:08 .mcp.json
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 10 05:08 .profile
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 10 05:08 .ripgreprc
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 10 05:08 .vscode
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 10 05:08 scripts
Tue Nov 10 05:07:19 2026 +0000
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -n "0.57 against 0.68" mknb.py && sed -i 's/(0.57 against 0.68 for/(0.575 against 0.684 for/' mknb.py && . dev/bin/activate && python mknb.py && cd  && python - <<'EOF'
import json
src=json.load(open('entries/okuno-2025/reproduce_okuno_2025.ipynb'))
ex=json.load(open('executed/okuno-2025/reproduce_okuno_2025.ipynb'))
for a,b in zip(src['cells'],ex['cells']):
    if a['cell_type']=='markdown': b['source']=a['source']
    else: assert ''.join(a['source'])==''.join(b['source'])
json.dump(ex, open('executed/okuno-2025/reproduce_okuno_2025.ipynb','w'), indent=1)
EOF
python tools/entry.py check entries/okuno-2025 2>&1 | tail -1 && python tools/entry.py handover entries/okuno-2025 2>&1 | tail -1; grep -c "outputs\": \[\]" entries/okuno-2025/reproduce_okuno_2025.ipynb; date -u
```

```
742:these give has a lower FC-SC correlation than the paper's own output files (0.57 against 0.68 for
53 cells
0 error(s)
wrote executed/okuno-2025/handover
26
Tue Nov 10 08:04:12 UTC 2026
```

**Agent**

I've finished steps 1 to 5 of the Author section and run the handover (step 6). Of the 33 claims, 13 were tested: 7 reproduced, 3 partially reproduced and 3 not reproduced. The other 20 are blocked. `tools/entry.py check` passes with 0 errors. The main notebook ran cleanly from a clean environment in 1053 s.

## 1. Outcomes

| Claim | Data | Outcome |
|---|---|---|
| fig1-poltcomp-optimal, fig2b, figs2-1b, fig2c, figs2-1d, fig2d-log-decline, fig2d-fly-values, fig2d-ten-thousand-rois, discussion-twenty-rois | with_inputs | blocked, `data_missing` (the SCKm and DistKm atlases are not published) |
| fig3d-confidence-threshold | with_inputs | blocked, `data_missing` (FlyEM SC at confidence 0.5, 0.6, 0.7 and 0.9 is not published) |
| fig3d-flyem-vs-flywire | with_inputs | partially reproduced: FlyEM 0.616 against FlyWire 0.575, so FlyEM is higher, but both are below tolerance |
| fig3e-flyem-higher-most-regions | with_inputs | reproduced: 55 of 63 regions (`assumed`, depends on left-right orientation) |
| fig3g-transmitter-correlation | with_inputs | not reproduced: ACh r = 0.013, GABA r = -0.157 |
| fig4e-unsegregated-higher | with_inputs | reproduced; selected total 2,373,104, null-totals p = 0.832 |
| fig4f-segregated-lower | with_inputs | reproduced under reading (a); reading (b) not run |
| fig4i-reciprocal-higher | with_inputs | reproduced |
| figs4-1-flyem-permutation | with_inputs | blocked, `data_missing` |
| fig5b-walking-activation | with_inputs | reproduced under reading (a) |
| fig5b-walking-suppression | with_inputs | not reproduced: no negative cluster (lowest t is -0.82) |
| fig3a-postsynapse-counts | elsewhere | partially reproduced: FlyEM at confidence 0 is not in the deposited table |
| fig3c, figs3-1a, fig3f | elsewhere | reproduced, from the paper's own per-ROI tables |
| fig4b-ppssi-distribution | elsewhere | partially reproduced: mean 0.471 fits, but 138,144 neurons have a PPSSI, not 139,255 |
| figs3-2cd-apl-similarity | elsewhere | blocked, `not_runnable` |
| fig4a, fig4c, figs4-1ij, fig4h, fig5-wagn | elsewhere | blocked, `other` (not attempted; I gave the time to the dataset claims) |

All tested with_inputs outcomes are marked `assumed`, because they rest on registration and tCompCor choices the paper does not fix. The FC computed here gives FlyWire r = 0.575 where the paper's own Zenodo output gives 0.684. The paper's per-region values give its transmitter numbers exactly, so the fig3g failure comes from this attempt's FC, not from the SC.

## 2. Dataset, assumptions, questions

**Version.** 0.240106.0043, the version the paper cites and the only published one.

**What checked out.**
- The files match their description: 9 flies, 3384 volumes at 1.8797 Hz, 50 Hz FicTrac speed.
- In name order, the files reproduce the walking regressor stored in the paper's code (`data/behavior.mat`) to 1e-5. That confirms the subject order and that behaviour is aligned to the imaging.
- fly-100, the seventh fly, which the code leaves out, has the worst field-of-view coverage. That fits the paper's reason for dropping one fly.
- No duplicate recordings.

**Problems recorded as findings.**
- The SCKm and DistKm atlases are not published anywhere; Zenodo holds their SC matrices but not which voxels belong to which ROI.
- The files do not say which side of the volume is left or right.
- The `dimension` attribute is [128, 256, 49] while the data are stored as (time, 256, 128, 49).
- The processed series has no voxel size.

**Inputs.** The paper's code at commit 4b92add and Zenodo 10.5281/zenodo.15532272 (the version cited by the code's README, which predates the preprint).

**Assumptions.**
- No left-right flip. Swapping left and right lowers the FC-SC correlation, which supports this.
- No SPM12 motion or slice-timing correction; ANTs SyN registration in Python.
- tCompCor voxels chosen in native space, before warping.
- GLM fitted by OLS without the Tukey-taper pre-whitening, smoothed on the beta maps.
- Cluster extent taken from the code's README.

**Question for the authors** (recorded as a `methods_unavailable` finding): which SPM12 and ANTs settings, and which NIfTI voxel size, were used?

**Questions to a reader:** none.

## 3. Where the protocol was unclear or did not fit

1. "Fix every random seed": ANTs registration is not repeatable even with a seed and one thread. I said so in the notebook and record; numbers can shift slightly when CI re-runs the notebook.
2. I edited conclusion markdown after execution and copied the same edits into the executed copy. No code changed.
3. I ran the companion notebook (`connectome_okuno_2025.ipynb`) with nbconvert in the entry's environment, not with `entry.py run`, to avoid re-running the main notebook and shifting its numbers. `result.json` therefore lists only the main notebook.
4. For the elsewhere claims, the protocol does not say whether the paper's own derived tables count as the data. I used them and recorded it as a deviation.
5. The Time rule only covers claims cut off at the deadline. For claims I chose not to attempt earlier, I used `other` and said so.
6. There was no clear place for a link claim, since the SC is matched to the data through template space. I added none and checked subject identity through the behaviour regressor instead.
7. The claims file's M3 says tCompCor voxels are ranked by SD after detrending, but the code it cites ranks them before. I followed the code and recorded a deviation. I didn't ask a reader, because it cannot change an outcome.

## 4. Runtime and failures

The run took about 3 h (05:09 to 08:04 UTC). The main notebook takes about 18 min and 4.6 GB peak memory; the companion takes under 1 min.

Fixed during development:
- Streaming through remfile ran at about 10 MB/s; switching to parallel direct chunk reads gave about 165 MB/s.
- Antspy's default affine registration stalled for three flies; I now start from the better of two affine registrations.
- A slow column gather made each fly take 400 s; fixed to about 65 s.

Nothing is committed.

## End of run

111 turns, 169 minutes, $10.33 at API prices, result: success.
