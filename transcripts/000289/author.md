# 000289 · author · run 40969113892

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cd  ls; ls docs paper claims/000289 entries | head -50; wc -l docs/*.md README.md
```

```
Thu Oct 29 22:56:58 UTC 2026
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
[... 67 more lines not kept]
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

**Agent calls Read**

```json
{
 "file_path": "claims/000289/10.1073-pnas.2210622120.yaml"
}
```

```
1	# Claims for Kutschireiter, Basnak, Wilson & Drugowitsch (2023), "Bayesian inference in ring
2	# attractor networks", PNAS 120, e2210622120, on dandiset 000289.
3	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
4	# protocol pilot-10 as stated in docs/protocol.md.
5	#
6	# Text read: the version of record as served by Europe PMC (PMC9992764, CC BY-NC-ND), main text,
7	# figure legends and Materials and Methods, with the SI Appendix (Appendix 01, PDF, extracted to
8	# text in the same file): SI sections 1 to 6 and Figs. S1 to S5. The bioRxiv preprint version 1
9	# (10.1101/2021.12.17.473253v1) is also under paper/; it was not used for the claims.
10	#
11	# Code read: Zenodo doi:10.5281/zenodo.7615975, "DrugowitschLab/BayesianRingAttractor: Code as used
12	# in 2023 PNAS paper" v1.0 (GitHub DrugowitschLab/BayesianRingAttractor, tag v1.0, commit a9db6f9),
13	# the deposit the Data Availability statement names. It holds the filters and the
14	# single-population network (circularFiltering.py: generateData, vM_Projection_Run for the circKF,
15	# vM_Projection_quad_Run for its quadratic approximation, no_uncertainty_filter_Run for the
16	# conventional (fixed kappa*) attractor, RNN_filter_Run, PF_run), the Drosophila-like network
17	# (network_filter.py), the scan scripts (performance_scan_figure2i, 3d, 3f, 4g, S2), one notebook
18	# per figure, and the processed scan outputs the figures are drawn from (data_processed/
19	# figure2i.npz, figure3d.npz, figure3f/sigma=*.npz, figure4g.npz, figureS2.npz,
20	# vonMises_q_stats.npz). data_raw/ is empty. The code holds no imaging analysis and no
[... 397 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; cat docs/archives.md
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
[... 406 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat docs/design.md | head -271; ls entries/001453-fouke-2025/ ; cat entries/001453-fouke-2025/entry.yaml entries/001453-fouke-2025/requirements.in; cat attempts/001453-fouke-2025-01.yaml | head -200
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
[... 486 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 200,400p attempts/001453-fouke-2025-01.yaml; ls schemas; ls paper; ls questions | head
```

```
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
  blocked_by: data_missing
[... 198 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s,indent=1)[:9000])"
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
[... 357 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));p=s['properties'];print(json.dumps({k:p[k] for k in p if k in ('inputs','findings')},indent=1))"; grep -n "data\b\|where\|elsewhere\|with_inputs" tools/entry.py | head -40
```

```
{
 "findings": {
  "description": "What the attempt found about the dataset itself, whatever the outcomes. These roll up into the per-dataset report.",
  "type": "array",
  "items": {
   "type": "object",
   "additionalProperties": false,
   "required": [
    "kind",
    "statement"
   ],
   "properties": {
    "kind": {
     "enum": [
      "metadata_error",
      "data_missing",
      "identifier_missing",
      "metadata_insufficient",
      "selection_undocumented",
      "methods_unavailable",
[... 83 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/000289/ | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/000289/versions/" | python -m json.tool | head -60; curl -s https://zenodo.org/api/records/7615975 | python -c "import json,sys;d=json.load(sys.stdin);print(d['metadata']['title'],d['metadata'].get('version'));[print(f['key'],f['size'],f['links']['self']) for f in d['files']]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/000289/versions/0.240801.1040/ > meta.json; python -c "
import json;d=json.load(open('meta.json'));
for k in ['description','relatedResource','assetsSummary','contributor','citation','wasGeneratedBy','keywords','about','ethicsApproval','protocol']:
  print(k, json.dumps(d.get(k),indent=0)[:2500])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; python - <<'EOF'
import json,urllib.request
url="https://api.dandiarchive.org/api/dandisets/000289/versions/0.240801.1040/assets/?page_size=1000"
d=json.load(urllib.request.urlopen(url))
json.dump(d['results'],open('assets.json','w'))
print(d['count'])
for a in d['results'][:300]: print(a['path'], round(a['size']/1e9,2))
EOF
```

```
221
sub-13/sub-13_ses-20201201T000000_behavior+ophys.nwb 8.68
sub-12/sub-12_ses-20201201T000000_behavior+ophys.nwb 8.68
sub-15/sub-15_ses-20201208T000000_behavior+ophys.nwb 8.68
sub-14/sub-14_ses-20201203T000000_behavior+ophys.nwb 8.68
sub-17/sub-17_ses-20210129T151248_behavior+ophys.nwb 8.67
sub-16/sub-16_ses-20210127T122834_behavior+ophys.nwb 8.67
sub-10/sub-10_ses-20201127T000000_behavior+ophys.nwb 8.68
sub-1/sub-1_ses-20201019T000000_behavior+ophys.nwb 8.68
sub-11/sub-11_ses-20201130T000000_behavior+ophys.nwb 8.68
sub-19/sub-19_ses-20210204T105459_behavior+ophys.nwb 8.67
sub-18/sub-18_ses-20210202T103436_behavior+ophys.nwb 8.67
sub-2/sub-2_ses-20201020T000000_behavior+ophys.nwb 8.68
sub-24/sub-24_ses-20210216T125551_behavior+ophys.nwb 8.67
sub-25/sub-25_ses-20210216T165850_behavior+ophys.nwb 8.67
sub-23/sub-23_ses-20210216T111909_behavior+ophys.nwb 8.67
sub-26/sub-26_ses-20210218T134033_behavior+ophys.nwb 8.67
sub-27/sub-27_ses-20210219T120646_behavior+ophys.nwb 8.67
sub-22/sub-22_ses-20210211T144219_behavior+ophys.nwb 8.67
sub-3/sub-3_ses-20201020T000000_behavior+ophys.nwb 8.68
[... 203 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -sL -o bra.zip https://zenodo.org/api/records/7615975/files/DrugowitschLab/BayesianRingAttractor-v1.0.zip/content; md5sum bra.zip; unzip -o -q bra.zip -d bra; find bra -type f | head -80; curl -s https://zenodo.org/api/records/7615975 | python -c "import json,sys;d=json.load(sys.stdin);print(d['files'][0]['checksum'], d['doi'], d['metadata'].get('related_identifiers'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; python -c "import pynwb,remfile,h5py,dandi;print(pynwb.__version__)" 2>&1; which uv
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pynwb,remfile,h5py,dandi;print(pynwb.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pynwb'
/opt/hostedtoolcache/Python/3.13.17/x64/bin/uv
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; uv venv -q venv && . venv/bin/activate && uv pip install -q pynwb remfile h5py numpy scipy pandas matplotlib requests 2>&1 | tail -2; python -c "import pynwb;print(pynwb.__version__)"
```

```
4.2.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; cat > survey.py <<'EOF'
import json,sys,remfile,h5py,urllib.request
assets=json.load(open('assets.json'))
def url(path):
    a=[a for a in assets if a['path']==path][0]
    d=json.load(urllib.request.urlopen(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/"))
    return [u for u in d['contentUrl'] if 's3' in u][0]
path=sys.argv[1]
f=h5py.File(remfile.File(url(path)),'r')
def show(name,obj):
    if isinstance(obj,h5py.Dataset):
        v=''
        if obj.size<6: v=obj[()]
        print(name,obj.shape,obj.dtype,dict((k,obj.attrs[k]) for k in obj.attrs if k in('unit','description','conversion','rate','neurodata_type')),v)
    else:
        print(name+'/',dict((k,obj.attrs[k]) for k in obj.attrs if k in('neurodata_type','description','colnames')))
f.visititems(show)
EOF
python survey.py sub-62/sub-62_ses-20210609T145805_behavior+ophys.nwb 2>&1 | head -150
```

```
<persisted-output>
Output too large (112.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/ded2df56-8766-46fa-8bd7-3df5acc38577/tool-results/b2o63tl41.txt

Preview (first 2KB):
acquisition/ {}
acquisition/TwoPhotonSeries/ {'description': 'no description', 'neurodata_type': 'TwoPhotonSeries'}
acquisition/TwoPhotonSeries/data (276, 12, 256, 128) int16 {'conversion': np.float64(1.0), 'unit': 'n.a.'} 
acquisition/TwoPhotonSeries/timestamps (276,) float64 {'unit': 'seconds'} 
analysis/ {}
file_create_date (1,) object {} [b'2022-08-28T19:06:00.637000-04:00']
general/ {}
general/devices/ {}
general/devices/Device/ {'neurodata_type': 'Device'}
general/experimenter (1,) object {} [b'Melanie Basnak']
general/extracellular_ephys/ {}
general/institution () object {} b'Harvard University'
general/intracellular_ephys/ {}
general/optogenetics/ {}
general/optophysiology/ {}
general/optophysiology/imaging_plane/ {'neurodata_type': 'ImagingPlane'}
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; grep -v "specifications/" /home/runner/.claude/projects/-home-runner-work-encore-encore/ded2df56-8766-46fa-8bd7-3df5acc38577/tool-results/b2o63tl41.txt | sed -n 36,200p
```

```
processing/behavior/Position/ {'neurodata_type': 'CompassDirection'}
processing/behavior/Position/SpatialSeries/ {'description': 'no description', 'neurodata_type': 'SpatialSeries'}
processing/behavior/Position/SpatialSeries/data (276,) float64 {'conversion': np.float64(1.0), 'unit': 'radians'} 
processing/behavior/Position/SpatialSeries/reference_frame () object {} b'0 means the cue is right in front of the fly'
processing/behavior/Position/SpatialSeries/timestamps (276,) float64 {'unit': 'seconds'} 
processing/ophys/ {'description': 'contains optical physiology data', 'neurodata_type': 'ProcessingModule'}
processing/ophys/Fluorescence/ {'neurodata_type': 'Fluorescence'}
processing/ophys/Fluorescence/RoiResponseSeries/ {'description': 'DF/F associated with each of the coordinates of the PB midline', 'neurodata_type': 'RoiResponseSeries'}
processing/ophys/Fluorescence/RoiResponseSeries/data (276, 32) float64 {'conversion': np.float64(1.0), 'unit': 'na'} 
processing/ophys/Fluorescence/RoiResponseSeries/rois (32,) int8 {'description': 'midline_rois', 'neurodata_type': 'DynamicTableRegion'} 
processing/ophys/Fluorescence/RoiResponseSeries/timestamps (276,) float64 {'unit': 'seconds'} 
processing/ophys/ImageSegmentation/ {'neurodata_type': 'ImageSegmentation'}
processing/ophys/ImageSegmentation/PlaneSegmentation/ {'colnames': array(['image_mask'], dtype=object), 'description': 'contains rois', 'neurodata_type': 'PlaneSegmentation'}
processing/ophys/ImageSegmentation/PlaneSegmentation/id (32,) int8 {'neurodata_type': 'ElementIdentifiers'} 
processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask (32, 256, 128) int32 {'description': 'segmented of the PB midline that the DF/F traces are associated with', 'neurodata_type': 'VectorData'} 
processing/ophys/ImageSegmentation/PlaneSegmentation/reference_images/ {}
scratch/ {}
session_description () object {} b'fly presented with a bright visual cue rotating in open loop'
session_start_time () object {} b'2021-06-09T14:58
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; cat > survey_all.py <<'EOF'
import json,remfile,h5py,urllib.request
from concurrent.futures import ThreadPoolExecutor
assets=json.load(open('assets.json'))
def one(a):
    try:
        u=f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"
        f=h5py.File(remfile.File(u),'r')
        r={'path':a['path'],'size':a['size']}
        r['desc']=f['session_description'][()].decode()
        r['start']=f['session_start_time'][()].decode()
        r['subj']=f['general/subject/subject_id'][()].decode()
        r['sdesc']=f['general/subject/description'][()].decode()
        r['geno']=f['general/subject/genotype'][()].decode()
        r['tps']=f['acquisition/TwoPhotonSeries/data'].shape
        r['dff']=f['processing/ophys/Fluorescence/RoiResponseSeries/data'].shape
        r['dffdesc']=f['processing/ophys/Fluorescence/RoiResponseSeries'].attrs['description']
        ts=f['processing/ophys/Fluorescence/RoiResponseSeries/timestamps'][:]
        r['t']=(float(ts[0]),float(ts[-1]),float((ts[-1]-ts[0])/(len(ts)-1)))
        r['rate']=float(f['general/optophysiology/imaging_plane/imaging_rate'][()])
        r['beh']=sorted(f['processing/behavior'].keys())
        r['behsub']={k:sorted(f['processing/behavior'][k].keys()) for k in f['processing/behavior'].keys()}
        r['ophys']=sorted(f['processing/ophys'].keys())
        r['acq']=sorted(f['acquisition'].keys())
        r['intervals']=sorted(f['intervals'].keys())
        r['stim']=sorted(f['stimulus/presentation'].keys())
        r['analysis']=sorted(f['analysis'].keys())
        r['notes']=f['general/notes'][()].decode() if 'notes' in f['general'] else None
        r['plane']=f['general/optophysiology/imaging_plane/description'][()].decode()
        return r
    except Exception as e:
        return {'path':a['path'],'err':repr(e)}
with ThreadPoolExecutor(16) as ex: res=list(ex.map(one,assets))
json.dump(res,open('survey.json','w'),indent=0)
EOF
time python survey_all.py; python -c "
import json,collections;r=json.load(open('survey.json'))
print(sum('err' in x for x in r)); 
print(collections.Counter(x.get('desc') for x in r))
print(collections.Counter(str(x.get('beh'))+str(x.get('behsub')) for x in r))
print(collections.Counter(str(x.get('ophys'))+str(x.get('acq'))+str(x.get('intervals'))+str(x.get('stim'))+str(x.get('analysis')) for x in r))
print(collections.Counter(x.get('geno') for x in r)); print(collections.Counter(x.get('notes') for x in r));print(collections.Counter(x.get('plane') for x in r));print(collections.Counter(x.get('dffdesc') for x in r))
"
```

```
real	7m14.134s
user	0m7.985s
sys	0m1.159s
0
Counter({'fly presented with a bright visual cue rotating in open loop': 93, 'fly presented with an initial block of a closed-loop visual cue': 17, 'fly presented with a final block of a closed-loop visual cue': 17, 'fly presented with a final block of a closed-loop wind cue': 17, 'fly presented with an initial block of a closed-loop wind cue': 17, 'fly presented with both cues in closed-loop': 17, 'fly presented with visual cues of varying contrast': 15, 'fly presented with a bright visual cue of varying gain': 14, 'fly presented with a a bright visual cue and a wind cue, with one cue being shifted every 5 min': 14})
Counter({"['Position']{'Position': ['SpatialSeries']}": 221})
Counter({"['Fluorescence', 'ImageSegmentation']['TwoPhotonSeries'][][][]": 178, "['Fluorescence', 'ImageSegmentation']['TwoPhotonSeries']['trials'][][]": 43})
Counter({'60D05/GCaMP7f': 221})
Counter({None: 221})
Counter({'EPG imaging in the PB': 221})
Counter({'DF/F associated with each of the coordinates of the PB midline': 221})
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; date -u; python -c "
import json,collections;r=json.load(open('survey.json'))
for x in sorted(r,key=lambda x:(x['desc'],int(x['subj']))):
  if 'open loop' in x['desc']: continue
  print(x['desc'][:45],x['path'].split('/')[1][:40],x['dff'],x['t'][0:2],round(x['t'][2],4),x['rate'],x['intervals'])
" | head -140
```

```
Thu Oct 29 23:05:18 UTC 2026
fly presented with a a bright visual cue and  sub-48_ses-20211228T121405_behavior+ophy [33045, 21] [0.0, 3599.9800000000005] 0.1089 9.18 ['trials']
fly presented with a a bright visual cue and  sub-49_ses-20211229T110202_behavior+ophy [33055, 21] [0.0, 3599.9800000000005] 0.1089 9.18 ['trials']
fly presented with a a bright visual cue and  sub-50_ses-20211229T143805_behavior+ophy [33052, 22] [0.0, 3599.9800000000005] 0.1089 9.18 ['trials']
fly presented with a a bright visual cue and  sub-51_ses-20211230T115615_behavior+ophy [33045, 21] [0.0, 3599.9800000000005] 0.1089 9.18 ['trials']
fly presented with a a bright visual cue and  sub-52_ses-20211231T095659_behavior+ophy [33058, 22] [0.0, 3599.9800000000005] 0.1089 9.18 ['trials']
fly presented with a a bright visual cue and  sub-53_ses-20220105T145617_behavior+ophy [33056, 20] [0.0, 3599.9800000000005] 0.1089 9.18 ['trials']
fly presented with a a bright visual cue and  sub-54_ses-20220126T164552_behavior+ophy [33049, 23] [0.0, 3599.9800000000005] 0.1089 9.18 ['trials']
fly presented with a a bright visual cue and  sub-55_ses-20220127T150558_behavior+ophy [33054, 20] [0.0, 3599.9800000000005] 0.1089 9.18 ['trials']
fly presented with a a bright visual cue and  sub-56_ses-20220128T144854_behavior+ophy [33055, 21] [0.0, 3599.9800000000005] 0.1089 9.18 ['trials']
fly presented with a a bright visual cue and  sub-57_ses-20220201T145726_behavior+ophy [33054, 20] [0.0, 3599.9800000000005] 0.1089 9.18 ['trials']
fly presented with a a bright visual cue and  sub-58_ses-20220203T134033_behavior+ophy [33053, 22] [0.0, 3599.9800000000005] 0.1089 9.18 ['trials']
fly presented with a a bright visual cue and  sub-59_ses-20220203T150920_behavior+ophy [33045, 19] [0.0, 3599.9800000000005] 0.1089 9.18 ['trials']
fly presented with a a bright visual cue and  sub-60_ses-20220204T144141_behavior+ophy [33052, 23] [0.0, 3599.9800000000005] 0.1089 9.18 ['trials']
fly presented with a a bright visual cue and  s
[... 115 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; python - <<'EOF'
import json,remfile,h5py,numpy as np
assets=json.load(open('assets.json'))
for p in ['sub-1/sub-1_ses-20201019T000000_behavior+ophys.nwb','sub-16/sub-16_ses-20210127T122834_behavior+ophys.nwb','sub-48/sub-48_ses-20211228T121405_behavior+ophys.nwb']:
    a=[a for a in assets if a['path']==p][0]
    f=h5py.File(remfile.File(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"),'r')
    t=f['intervals/trials']
    print(p, dict(t.attrs))
    for k in t.keys():
        d=t[k]; print(' ',k,d.shape,d.dtype,dict(d.attrs).get('description'), d[:] if d.size<60 else d[:20])
    pos=f['processing/behavior/Position/SpatialSeries']
    x=pos['data'][:]; ts=pos['timestamps'][:]
    print(' pos',x.shape,np.nanmin(x),np.nanmax(x),ts[:3],ts[-1], dict(pos.attrs))
    d=f['processing/ophys/Fluorescence/RoiResponseSeries/data'][:]
    print(' dff',d.shape,np.nanmin(d),np.nanmax(d),np.nanmean(d),np.isnan(d).sum())
    print(' rois',f['processing/ophys/Fluorescence/RoiResponseSeries/rois'][:])
EOF
```

```
sub-1/sub-1_ses-20201019T000000_behavior+ophys.nwb {'colnames': array(['start_time', 'stop_time', 'cue_contrast'], dtype=object), 'description': 'trial data and properties', 'namespace': 'core', 'neurodata_type': 'TimeIntervals', 'object_id': 'b1e17713-3aa4-499e-940e-ced7e5e44658'}
  cue_contrast (6,) float64 visual cue contrast (where 1 = zero contrast, 2 = low contrast, 3 = high contrast [2. 1. 3. 1. 2. 3.]
  id (6,) int64 None [0 1 2 3 4 5]
  start_time (6,) float64 start time of trial [  0.   195.04 394.98 594.92 794.98 995.02]
  stop_time (6,) float64 end of each trial [ 195.04  394.98  594.92  794.98  995.02 1199.98]
 pos (11020,) 0.0023984272511159625 6.280877959758508 [0.   0.1  0.22] 1199.9800000000002 {'comments': 'no comments', 'description': 'no description', 'namespace': 'core', 'neurodata_type': 'SpatialSeries', 'object_id': 'a190f2dd-99f3-42c2-aec2-46effbfe9e9f'}
 dff (11020, 37) -0.46525681244694017 3.903237992848777 0.5038195032023541 0
 rois [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36]
sub-16/sub-16_ses-20210127T122834_behavior+ophys.nwb {'colnames': array(['start_time', 'stop_time', 'cue_gain'], dtype=object), 'description': 'trial data and properties', 'namespace': 'core', 'neurodata_type': 'TimeIntervals', 'object_id': 'cb7ce5f3-d5c6-4310-88d9-fd76b080d432'}
  cue_gain (3,) float64 gain of the visual cue (where 1 = normal gain, 2 = inverted gain [1. 2. 1.]
  id (3,) int64 None [0 1 2]
  start_time (3,) float64 start time of trial [  0.   199.94 999.92]
  stop_time (3,) float64 end of each trial [ 199.94  999.92 1199.98]
 pos (11020,) 0.00019325586616825103 6.282198518129052 [0.   0.1  0.22] 1199.9800000000002 {'comments': 'no comments', 'description': 'no description', 'namespace': 'core', 'neurodata_type': 'SpatialSeries', 'object_id': 'a5472bdf-c8bf-412e-b5cc-608221f39f95'}
 dff (11020, 27) -0.42474346077636277 3.7308365256547282 0.44111100895217076 0
 rois [ 0  1  2  3  4  5
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; curl -sI https://storage.googleapis.com/hemibrain/v1.2/exported-traced-adjacencies-v1.2.tar.gz | head -5; curl -s -o /dev/null -w "%{http_code}\n" https://neuprint.janelia.org/api/dbmeta/datasets; python - <<'EOF'
import json,remfile,h5py
assets=json.load(open('assets.json'))
a=[a for a in assets if a['path'].startswith('sub-1/')][0]
f=h5py.File(remfile.File(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"),'r')
d=f['acquisition/TwoPhotonSeries/data']; print(d.shape,d.chunks,d.compression,d.dtype)
print(f['processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask'].shape)
EOF
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s https://neuprint.janelia.org/api/dbmeta/datasets | head -c 600; echo; curl -s -X POST -H "Content-Type: application/json" -d '{"cypher":"MATCH (n:Neuron) WHERE n.type=\"PEN_a(PEN1)\" RETURN n.bodyId, n.instance LIMIT 3","dataset":"hemibrain:v1.2.1"}' https://neuprint.janelia.org/api/custom/custom | head -c 500
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -sI https://storage.googleapis.com/hemibrain/v1.2/exported-traced-adjacencies-v1.2.tar.gz | grep -i -E "content-length|x-goog-hash|last-modified"; curl -s "https://storage.googleapis.com/storage/v1/b/hemibrain/o?prefix=v1.2&fields=items(name,size,updated)" | head -c 1500; curl -s "https://storage.googleapis.com/storage/v1/b/hemibrain-release/o?prefix=neuprint&fields=items(name,size)" | head -c 1500
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/bra/DrugowitschLab-BayesianRingAttractor-a9db6f9; wc -l *.py; cat README.md; grep -n "^def \|^    return" circularFiltering.py | head -60
```

```
620 circularFiltering.py
  185 network_filter.py
   89 performance_scan_figure2i.py
   71 performance_scan_figure3d.py
   78 performance_scan_figure3f.py
   68 performance_scan_figure4g.py
   73 performance_scan_figureS2.py
 1184 total
# Code for "Bayesian inference in ring attractor networks"

This repo contains the code for simulations and figures in

Anna Kutschireiter, Melanie A Basnak, Rachel I Wilson, and Jan Drugowitsch (2023). Bayesian inference in ring attractor networks. Proceedings of the National Academy of Sciences.


## Code structure and environment setup
* `root` - python scripts and jupyter notebooks containing the main code to reproduce figures
* `/data_processed` - `analysed' artificial data
* `/data_raw` - raw data, empty. 

[... 126 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/bra/DrugowitschLab-BayesianRingAttractor-a9db6f9; sed -n 1,520p circularFiltering.py
```

```
"""
Modified on Tue Jan 17 2023

@author: akutschireiter

"""

import numpy as np
from scipy.stats import vonmises
from scipy.special import i0, i1
from scipy.optimize import root_scalar
from numpy.core.numeric import isscalar


##### Helper functions #####

def A_Bessel(kappa): 
    """Computes the ratio of Bessel functions."""
    r = i1(kappa)/i0(kappa)
    return r
[... 498 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/bra/DrugowitschLab-BayesianRingAttractor-a9db6f9; python3 - <<'EOF'
import json
for nb in ['Figure2h.ipynb','Figure2i.ipynb','Figure3b,c,e,d_FigureS3.ipynb']:
    d=json.load(open(nb))
    print('=====',nb)
    for c in d['cells']:
        if c['cell_type']=='code':
            s=''.join(c['source'])
            if 'plt.' in s and len(s)>1500: s=s[:1500]+'\n...[plot]'
            print('---');print(s)
EOF
```

```
===== Figure2h.ipynb
---
%load_ext autoreload
%autoreload 2

import numpy as np
import matplotlib.pyplot as plt
import circularFiltering as flt
import matplotlib
matplotlib.rcParams.update({'font.size': 14,
                            'pdf.fonttype': 42,
                            'ps.fonttype': 42})
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
---
####### simulation parameters
np.random.seed(42)
T = 15
dt = 0.01
t = np.arange(0,T,dt)
[... 594 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/bra/DrugowitschLab-BayesianRingAttractor-a9db6f9; python3 - <<'EOF'
import json
for nb in ['Figure3f_FigureS4.ipynb','Figure4g,h.ipynb','FigureS2.ipynb']:
    d=json.load(open(nb))
    print('=====',nb)
    for c in d['cells']:
        if c['cell_type']=='code':
            s=''.join(c['source'])
            if 'plt.' in s and len(s)>1200: s=s[:1200]+'\n...[plot]'
            print('---');print(s)
EOF
cat performance_scan_figure3f.py performance_scan_figureS2.py
```

```
===== Figure3f_FigureS4.ipynb
---
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import circularFiltering as flt
from scipy.stats import norm
import matplotlib
import glob
import os
import re
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
---
mu_perf = 0.5
sig_perf = 1

def objective(rMSE,mu=0,sigma=0.5):
    x = np.log(kappa_z_array)
    dx = np.diff(x)
[... 369 more lines not kept]
```

**Agent**

Let me see the full Fig 3F processing cell, which got truncated.

**Agent calls Bash**

```bash
cd $TMPDIR/bra/DrugowitschLab-BayesianRingAttractor-a9db6f9; python3 - <<'EOF'
import json
d=json.load(open('Figure3f_FigureS4.ipynb'))
cs=[c for c in d['cells'] if c['cell_type']=='code']
print(''.join(cs[3]['source']))
EOF
python3 -c "
import numpy as np,glob
for f in sorted(glob.glob('data_processed/*.npz'))+['data_processed/figure3f/sigma=0.0.npz','data_processed/figure3f/sigma=10.0.npz']:
    d=np.load(f); print(f,{k:d[k].shape for k in d.files})
"
```

```
Exit code 1
kappa_star_array = np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,
                            1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 
                            2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 
                            3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2, 4.4, 4.6, 4.8, 5.0])
beta_array = np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9, 1, 2 ,4 ,8])
kappa_z_array = np.array([1.e-02, 3.e-02, 1.e-01, 2.e-01, 3.e-01, 4.e-01, 5.e-01, 6.e-01,
       7.e-01, 8.e-01, 9.e-01, 1.e+00, 2.e+00, 3.e+00, 4.e+00, 5.e+00,
       6.e+00, 7.e+00, 8.e+00, 9.e+00, 1.e+01, 3.e+01, 1.e+02])

N = 64

sigmaN_array = np.array([0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,15,20])
max_MSE = np.zeros(len(sigmaN_array))
noretuning_MSE = np.zeros(len(sigmaN_array))
sig_to_noise = np.zeros(len(sigmaN_array))
noretuning_sig_to_noise = np.zeros(len(sigmaN_array))

# parameters for colorbar (comparable across levels)
vmin = 0.25
[... 55 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/bra/DrugowitschLab-BayesianRingAttractor-a9db6f9; . $TMPDIR/venv/bin/activate; python -c "
import numpy as np,glob
for f in sorted(glob.glob('data_processed/*.npz'))+['data_processed/figure3f/sigma=0.0.npz','data_processed/figure3f/sigma=10.0.npz']:
    d=np.load(f); print(f,{k:d[k].shape for k in d.files})
d=np.load('data_processed/figure2i.npz'); print(d['vonMises_stats'][0,:,1].round(3)); print(d['vonMises_q_stats'][0,:,1].round(3)); print(d['vonMises_stats'][0,:,2].round(2)); print(d['vonMises_q_stats'][0,:,2].round(2)); print(d['noUncert_stats'][:,:,1].round(3)[:5]); print(d['PF_stats'][0,:,1].round(3))
"
```

```
data_processed/figure2i.npz {'vonMises_stats': (33, 23, 3), 'vonMises_q_stats': (33, 23, 3), 'PF_stats': (33, 23, 3), 'noUncert_stats': (33, 23, 2)}
data_processed/figure3d.npz {'stats': (23, 3), 'MSE_array': (25, 13)}
data_processed/figure4g.npz {'vonMises_stats': (23, 3), 'vonMises_q_stats': (23, 3), 'CX_stats': (23, 3)}
data_processed/figureS2.npz {'MSE_array': (7, 23)}
data_processed/vonMises_q_stats.npz {'stats': (23, 3)}
data_processed/figure3f/sigma=0.0.npz {'MSE_array': (40, 13), 'avg_network_activity': (40, 13)}
data_processed/figure3f/sigma=10.0.npz {'MSE_array': (40, 13), 'avg_network_activity': (40, 13)}
[0.102 0.153 0.273 0.355 0.422 0.468 0.506 0.536 0.568 0.581 0.609 0.631
 0.727 0.778 0.814 0.832 0.847 0.861 0.868 0.88  0.884 0.937 0.965]
[0.029 0.069 0.216 0.321 0.397 0.459 0.495 0.529 0.566 0.58  0.608 0.63
 0.728 0.779 0.814 0.832 0.847 0.861 0.868 0.88  0.884 0.937 0.965]
[ 0.18  0.31  0.56  0.79  0.98  1.12  1.27  1.39  1.48  1.56  1.67  1.76
  2.42  2.86  3.26  3.57  3.89  4.15  4.4   4.62  4.82  7.85 13.6 ]
[ 1.    1.    1.05  1.16  1.27  1.36  1.46  1.55  1.62  1.68  1.77  1.84
  2.39  2.8   3.18  3.49  3.8   4.07  4.32  4.54  4.75  7.82 13.58]
[[0.07  0.081 0.088 0.081 0.093 0.078 0.076 0.098 0.092 0.09  0.085 0.103
  0.121 0.155 0.16  0.181 0.189 0.214 0.22  0.23  0.249 0.386 0.632]
 [0.057 0.129 0.199 0.245 0.244 0.265 0.261 0.266 0.26  0.267 0.282 0.267
  0.282 0.278 0.265 0.249 0.249 0.268 0.281 0.29  0.289 0.435 0.663]
 [0.044 0.066 0.18  0.284 0.358 0.414 0.446 0.489 0.489 0.516 0.534 0.539
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; curl -s -o hb.tgz https://storage.googleapis.com/hemibrain/v1.2/exported-traced-adjacencies-v1.2.tar.gz; tar tzvf hb.tgz; tar xzf hb.tgz; python - <<'EOF'
import pandas as pd,glob
d=glob.glob('exported-traced-adjacencies-v1.2/*')
print(d)
n=pd.read_csv('exported-traced-adjacencies-v1.2/traced-neurons.csv')
print(n.columns.tolist(), len(n))
for t in ['EPG','Delta7','PEN_a(PEN1)','PEN_a','PEN1']:
    s=n[n.type==t]; print(t,len(s)); print(s.instance.value_counts().sort_index().to_string()[:1500])
print(n[n.type.str.contains('PEN',na=False)].type.value_counts())
EOF
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; python - <<'EOF'
import pandas as pd,numpy as np
n=pd.read_csv('exported-traced-adjacencies-v1.2/traced-neurons.csv')
c=pd.read_csv('exported-traced-adjacencies-v1.2/traced-total-connections.csv')
print(c.columns.tolist())
n['g']=n.instance.str.extract(r'_([LR]\d)')[0]
types={'EPG':'EPG','PEN_a(PEN1)':'PEN1','Delta7':'D7'}
s=n[n.type.isin(types)].copy(); s['t']=s.type.map(types)
c=c.merge(s[['bodyId','t','instance','g']],left_on='bodyId_pre',right_on='bodyId').merge(s[['bodyId','t','instance','g']],left_on='bodyId_post',right_on='bodyId',suffixes=('_pre','_post'))
order=[f'L{k}' for k in range(9,0,-1)]+[f'R{k}' for k in range(1,10)]
for a,b in [('EPG','PEN1'),('PEN1','EPG')]:
    m=c[(c.t_pre==a)&(c.t_post==b)].pivot_table(index='g_pre',columns='g_post',values='weight',aggfunc='sum',fill_value=0)
    m=m.reindex(index=[o for o in order if o in m.index],columns=[o for o in order if o in m.columns])
    print(a,'->',b); print(m.to_string())
EOF
```

```
Exit code 1
['bodyId_pre', 'bodyId_post', 'weight']
Traceback (most recent call last):
  File "<stdin>", line 8, in <module>
  File "/tmp/claude-1001/venv/lib/python3.13/site-packages/pandas/core/frame.py", line 16192, in merge
    return merge(
        self,
    ...<10 lines>...
        validate=validate,
    )
  File "/tmp/claude-1001/venv/lib/python3.13/site-packages/pandas/core/reshape/merge.py", line 405, in merge
    return op.get_result()
           ~~~~~~~~~~~~~^^
  File "/tmp/claude-1001/venv/lib/python3.13/site-packages/pandas/core/reshape/merge.py", line 1139, in get_result
    result = self._reindex_and_concat(join_index, left_indexer, right_indexer)
  File "/tmp/claude-1001/venv/lib/python3.13/site-packages/pandas/core/reshape/merge.py", line 1090, in _reindex_and_concat
    llabels, rlabels = _items_overlap_with_suffix(
                       ~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self.left._info_axis, self.right._info_axis, self.suffixes
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; python - <<'EOF'
import pandas as pd,numpy as np
n=pd.read_csv('exported-traced-adjacencies-v1.2/traced-neurons.csv')
c=pd.read_csv('exported-traced-adjacencies-v1.2/traced-total-connections.csv')
n['g']=n.instance.str.extract(r'_([LR]\d)')[0]
types={'EPG':'EPG','PEN_a(PEN1)':'PEN1','Delta7':'D7'}
s=n[n.type.isin(types)].copy(); s['t']=s.type.map(types)
pre=s.rename(columns={'bodyId':'bodyId_pre','t':'t_pre','g':'g_pre','instance':'i_pre'})[['bodyId_pre','t_pre','g_pre','i_pre']]
post=s.rename(columns={'bodyId':'bodyId_post','t':'t_post','g':'g_post','instance':'i_post'})[['bodyId_post','t_post','g_post','i_post']]
c=c.merge(pre,on='bodyId_pre').merge(post,on='bodyId_post')
c.to_pickle('cx.pkl')
order=[f'L{k}' for k in range(9,0,-1)]+[f'R{k}' for k in range(1,10)]
for a,b in [('EPG','PEN1'),('PEN1','EPG')]:
    m=c[(c.t_pre==a)&(c.t_post==b)].pivot_table(index='g_pre',columns='g_post',values='weight',aggfunc='sum',fill_value=0)
    m=m.reindex(index=[o for o in order if o in m.index],columns=[o for o in order if o in m.columns])
    print(a,'->',b); print(m.to_string())
m=c[(c.t_pre=='EPG')&(c.t_post=='D7')].pivot_table(index='g_pre',columns='i_post',values='weight',aggfunc='sum',fill_value=0)
print(m.reindex(index=[o for o in order if o in m.index]).to_string())
EOF
```

```
EPG -> PEN1
g_post   L9  L8  L7   L6  L5   L4  L3  L2  R2   R3   R4  R5   R6   R7   R8  R9
g_pre                                                                         
L8      104  74   1    0   0    0   1  35  23  122   11   0    0    0    0   1
L7       35  57  55    0   0    0   0   1   0   45  106   8    0    0    0   0
L6        4  23  53   75   0    0   0   0   0    0   33  57    5    0    0   0
L5        0   0  15   80  82    6   0   0   0    0    0  35   87    5    0   0
L4        0   0   0   33  65  154   3   0   0    0    0   0   34   71    0   0
L3        0   0   0    1  34  103  88   5   0    0    0   0    4   32   88   3
L2        0   0   0    0   0   37  46  78   7    0    0   0    0    0   23  49
L1        7   0   0    0   0    3  42  90  73    1    0   0    0    0    1  42
R1       33   0   0    0   0    0   4  53  67   28    2   0    0    0    0   8
R2       38  26   0    0   0    0   0   9  54   73   33   0    0    0    0   0
R3       15  86  43    1   0    0   0   0   3  101  141  39    2    0    0   0
R4        0  10  89   35   1    0   0   0   0    1   89  79   46    0    0   0
R5        0   0   4  122  24    0   0   0   0    0    0  81  106   38    0   0
R6        0   0   0   10  72   35   1   0   0    0    0   4  125   63   34   1
R7        0   0   0    0   2   89  47   1   4    0    0   0    3  108   89  31
R8        1   0   0    0   0   22  77  27  35    0    0   0    0   10  126  71
PEN1 -> EPG
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; python - <<'EOF'
import json,remfile,h5py,numpy as np,time
assets=json.load(open('assets.json'))
for s in ['sub-1/','sub-4/','sub-7/']:
    a=[a for a in assets if a['path'].startswith(s)][0]
    f=h5py.File(remfile.File(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"),'r')
    d=f['processing/ophys/Fluorescence/RoiResponseSeries/data'][:]
    n=d.shape[1]
    F=np.abs(np.fft.rfft(d-d.mean(1,keepdims=True),axis=1)).mean(0)
    print(s,n,'peak freq idx',F.argmax(),'period',n/F.argmax(), F.round(2)[:8])
    m=f['processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask'][:]
    print(' mask sums',m.reshape(n,-1).sum(1)[:10], m.max())
    ts=f['acquisition/TwoPhotonSeries/timestamps'][:5]; print(ts)
    t0=time.time(); x=f['acquisition/TwoPhotonSeries/data'][0:50]; print('50 vols',time.time()-t0,'s', x.shape, x.mean())
EOF
```

```
sub-1/ 37 peak freq idx 2 period 18.5 [0.   2.46 9.07 2.26 3.11 1.75 1.65 1.62]
 mask sums [5 6 6 7 6 7 5 7 6 8] 1
[0.   0.1  0.22 0.32 0.44]
50 vols 1.0221083164215088 s (50, 12, 256, 128) 46.6588112894694
sub-4/ 41 peak freq idx 2 period 20.5 [ 0.    2.7  16.65  2.83  5.25  2.48  1.92  2.01]
 mask sums [7 6 6 5 5 5 5 8 9 7] 1
[0.   0.12 0.26 0.38 0.5 ]
50 vols 1.0956168174743652 s (50, 14, 256, 128) 97.93391274588448
sub-7/ 47 peak freq idx 2 period 23.5 [ 0.    4.09 10.98  2.99  3.8   2.11  2.    2.1 ]
 mask sums [6 6 6 8 6 6 6 5 5 6] 1
[0.   0.1  0.22 0.32 0.44]
50 vols 1.0197176933288574 s (50, 12, 256, 128) 47.22262191772461
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  grep -n -i "bump amplitude\|cue reliab\|salient\|Simulation parameters\|Performance measures\|P = 5\|decoder\|hemibrain\|total synapse\|sorted" paper/10.1073-pnas.2210622120.txt | head -40; wc -c paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  for p in "Second, we predict" "visual landmark" "Fig. 4 B" "spatial position" "Simulation parameters" "Performance measures" "Neural noise"; do echo "== $p"; grep -o -i ".\{0,400\}$p.\{0,600\}" paper/10.1073-pnas.2210622120.txt | head -3; done
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
date -u; mkdir -p entries/000289-kutschireiter-2023
```

```
Thu Oct 29 23:24:45 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "entries/000289-kutschireiter-2023/bra.py",
 "content": "\"\"\"Helpers for testing Kutschireiter, Basnak, Wilson & Drugowitsch (2023), \"Bayesian inference in\nring attractor networks\" (PNAS 120, e2210622120), with dandiset 000289.\n\nThe paper holds no recorded data. Its simulation claims are tested on the paper's own code and\nprocessed outputs (Zenodo doi:10.5281/zenodo.7615975, BayesianRingAttractor v1.0, commit a9db6f9),\nits connectome claim on the hemibrain connectome, and its one prediction about cue reliability on\nthe imaging data of dandiset 000289. Every source is read into memory; nothing is written to disk.\n\nWhere each parameter comes from:\n- The claims file (claims/000289/10.1073-pnas.2210622120.yaml) gives every criterion: the\n  information rates, the readings for unquantified words, the network parameters of the noise test,\n  the decoder for bump amplitude.\n- The paper's code fixes the rest: the objective() weighting (mean 0.5, SD 1 over log rate), the\n  particle-filter reference, the Figure 2H simulation (run from the released notebook's own cells).\n- Two patches are needed to run the released code, both named in the claims file's header:\n  RNN_filter_Run gets a `z=None` argument (it uses z but has no such parameter), and the notebook\n  Figure2h.ipynb calls vM_Projection_Run with `kappa_y=`, which the function names `kappa_v`.\n- Standard choices that set only precision or speed are marked as such where they are made.\n\"\"\"\nimport hashlib\nimport io\nimport json\nimport re\nimport tarfile\nimport types\nimport zipfile\n\nimport numpy as np\nimport requests\nfrom scipy.stats import norm\n\n# ---------------------------------------------------------------------------------------------\n# Pinned sources\nDANDISET = \"000289\"\nVERSION = \"0.240801.1040\"  # the only published version (2024-08-01); see the notebook header\nDANDI_API = \"https://api.dandiarchive.org/api\"\n\nZENODO_URL = (\"https://zenodo.org/api/records/7615975/files/\"\n              \"DrugowitschLab/BayesianRingAttractor-v1.0.zip/content\")\nZENODO_MD5 = \"c3f0574b98eef0c6c67d139f0d20a1ae\"\nCODE_ROOT = \"DrugowitschLab-BayesianRingAttractor-a9db6f9/\"\n\n# Public export of the hemibrain v1.2 connectome (Scheffer et al. 2020), traced neurons and total\n# synapse counts per pair. neuPrint, which serves v1.2.1, now needs a personal token for all data.\nHEMIBRAIN_URL = \"https://storage.googleapis.com/hemibrain/v1.2/exported-traced-adjacencies-v1.2.tar.gz\"\nHEMIBRAIN_MD5 = \"ec1e076d15442f368fa5978b00f4a61c\"\n\n# Information rates of every scan (performance_scan_figure2i.py and the figure notebooks)\nRATES = np.array([0.01, 0.03, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 2, 3, 4, 5, 6, 7, 8,\n                  9, 10, 30, 100])\n# kappa* grid of the fixed-certainty filter (Figure3b,c,e,d_FigureS3.ipynb)\nKAPPA_FIXED = np.array([0.1, 0.3, 0.9, 1., 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2., 2.1, 2.2,\n                        2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3., 4., 5., 6., 7., 8., 9., 10., 30., 100.])\n# Figure 3D grid (same notebook)\nKSTAR_3D = np.round(np.arange(1, 26) * 0.1, 1)\nBETA_GRID = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 2, 4, 8])\n# Figure 3F grid (Figure3f_FigureS4.ipynb)\nKSTAR_3F = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6,\n                     1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.2, 3.4,\n                     3.6, 3.8, 4.0, 4.2, 4.4, 4.6, 4.8, 5.0])\nSIGMAS_3F = np.array([0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10., 15, 20])\nN_3F = 64\nREF_PF_3F = 0.6912447327304075  # Figure3f_FigureS4.ipynb, \"performance of particle filter as reference\"\nN_S2 = np.array([3, 4, 8, 16, 32, 64, 128])  # FigureS2.ipynb, N_array\n\n\ndef _get(url, md5):\n    data = requests.get(url, timeout=600).content\n    got = hashlib.md5(data).hexdigest()\n    if got != md5:\n        raise ValueError(f\"{url}: md5 {got}, expected {md5}\")\n    return data\n\n\n# ---------------------------------------------------------------------------------------------\n# The paper's code and processed outputs\nclass Code:\n    \"\"\"The Zenodo deposit, held in memory.\"\"\"\n\n    def __init__(self):\n        self.zip = zipfile.ZipFile(io.BytesIO(_get(ZENODO_URL, ZENODO_MD5)))\n        self.names = [n[len(CODE_ROOT):] for n in self.zip.namelist() if n.startswith(CODE_ROOT)]\n        self.patches = []\n        self.flt = self._module()\n\n    def read(self, name):\n        return self.zip.read(CODE_ROOT + name)\n\n    def npz(self, name):\n        return np.load(io.BytesIO(self.read(\"data_processed/\" + name)))\n\n    def notebook_cells(self, name):\n        nb = json.loads(self.read(name))\n        return [\"\".join(c[\"source\"]) for c in nb[\"cells\"] if c[\"cell_type\"] == \"code\"]\n\n    def _module(self):\n        src = self.read(\"circularFiltering.py\").decode()\n        old = \"I_ext=0,stoch_corr=0,dy=None\"\n        assert src.count(old) == 1\n        src = src.replace(old, \"I_ext=0,stoch_corr=0,z=None,dy=None\")\n        self.patches.append(\"RNN_filter_Run: added z=None to the signature (it uses z and has no such \"\n                            \"parameter; claims file header)\")\n        # numpy 2 moved numpy.core.numeric; isscalar is the same function at the top level\n        src = src.replace(\"from numpy.core.numeric import isscalar\", \"from numpy import isscalar\")\n        self.patches.append(\"import of isscalar from numpy, not numpy.core.numeric (numpy 2)\")\n        mod = types.ModuleType(\"circularFiltering\")\n        exec(compile(src, \"circularFiltering.py\", \"exec\"), mod.__dict__)\n        return mod\n\n\ndef objective(values, mu=0.5, sigma=1.0, rates=RATES):\n    \"\"\"Prior-weighted average over log rate, trapezoidal rule; objective() of the figure notebooks\n    with mu_perf = 0.5 and sig_perf = 1 (Methods, Performance measures; claims file).\"\"\"\n    x = np.log(rates)\n    f = np.asarray(values) * norm.pdf(x, loc=mu, scale=sigma)\n    return np.sum(0.5 * (f[1:] + f[:-1]) * np.diff(x))\n\n\n# ---------------------------------------------------------------------------------------------\n# Figure 2H: run the released notebook's own cells\ndef run_figure2h(code, rate=15):\n    \"\"\"Executes the simulation cells of Figure2h.ipynb (seed 42, T = 15, N = 80, cue off from 5 to\n    10 s). `rate` replaces the notebook's information rate of 15 (the Methods say 10/s; claims\n    file). The only other change is the keyword kappa_y -> kappa_v (claims file header).\"\"\"\n    cells = code.notebook_cells(\"Figure2h.ipynb\")\n    sim = [c for c in cells if \"np.random.seed(42)\" in c][0]\n    assert \"kappa_z = 15 \" in sim\n    sim = sim.replace(\"kappa_z = 15 \", f\"kappa_z = {rate} \")\n    kf = [c for c in cells if \"vM_Projection_Run\" in c][0].replace(\"kappa_y=kappa_v\", \"kappa_v=kappa_v\")\n    net = [c for c in cells if \"Single population network\" in c][0]\n    ns = {\"np\": np, \"flt\": code.flt}\n    for c in (sim, kf, net):\n        exec(c, ns)\n    return ns\n\n\ndef circ_diff(a, b):\n    return np.angle(np.exp(1j * (np.asarray(a) - np.asarray(b))))\n\n\n# ---------------------------------------------------------------------------------------------\n# Neural noise: a batched copy of RNN_filter_Run, checked against it in the notebook\ndef rnn_batch(rng, runs, T, N, sigma_N, w_even, w_quad, tau=1.0, kappa_0=1.0, phi_0=0.0, dt=0.01,\n              noise=None):\n    \"\"\"RNN_filter_Run (circularFiltering.py) for `runs` independent runs at once, with no angular\n    velocity input (w_odd = 0, dy = 0), no HD input (I_ext = 0) and stoch_corr = 0 (claims file).\n    Same update, term by term: decay, even recurrence (2/N w_even cos), quadratic inhibition\n    (pi/N sum of rectified rates), additive noise sigma_N sqrt(dt) N(0,1). `noise` may pass the\n    standard normal draws (steps x runs x N) to reproduce a given run.\"\"\"\n    steps = int(T / dt)\n    phi_r = np.linspace(-np.pi, np.pi - 2 * np.pi / N, N)\n    W = 2 / N * w_even * np.cos(phi_r[:, None] - phi_r[None, :])\n    A = np.array([np.cos(phi_r), np.sin(phi_r)])\n    r = np.tile(kappa_0 * np.cos(phi_r - phi_0), (runs, 1))\n    mu = np.zeros((steps, runs))\n    kappa = np.zeros((steps, runs))\n\n    def decode(r):\n        th = 2 / N * r @ A.T\n        return np.arctan2(th[:, 1], th[:, 0]), np.hypot(th[:, 0], th[:, 1])\n\n    mu[0], kappa[0] = decode(r)\n    for i in range(1, steps):\n        inh = w_quad * (np.pi / N) * np.maximum(r, 0).sum(1, keepdims=True)\n        dW = (noise[i] if noise is not None else rng.standard_normal((runs, N))) * np.sqrt(dt)\n        r = r - r / tau * dt + (r @ W.T) * dt - inh * r * dt + sigma_N * dW\n        mu[i], kappa[i] = decode(r)\n    return mu, kappa\n\n\n# ---------------------------------------------------------------------------------------------\n# Hemibrain connectome\ndef hemibrain():\n    \"\"\"Traced neurons (bodyId, type, instance) and total synapse counts per pair, hemibrain v1.2.\"\"\"\n    import pandas as pd\n    tf = tarfile.open(fileobj=io.BytesIO(_get(HEMIBRAIN_URL, HEMIBRAIN_MD5)), mode=\"r:gz\")\n    base = \"exported-traced-adjacencies-v1.2/\"\n    neurons = pd.read_csv(tf.extractfile(base + \"traced-neurons.csv\"))\n    conns = pd.read_csv(tf.extractfile(base + \"traced-total-connections.csv\"))\n    return neurons, conns\n\n\n# Reading (a) of the sort: the PB glomerulus in the instance name, L9 to R9 (claims file)\nPB_ORDER = [f\"L{k}\" for k in range(9, 0, -1)] + [f\"R{k}\" for k in range(1, 10)]\n\n\ndef pb_glomerulus(instance):\n    m = re.search(r\"_([LR][1-9])$\", instance)\n    return m.group(1) if m else None\n\n\n# ---------------------------------------------------------------------------------------------\n# Dandiset 000289\ndef assets():\n    url = f\"{DANDI_API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=1000\"\n    out = []\n    while url:\n        d = requests.get(url, timeout=120).json()\n        out += d[\"results\"]\n        url = d.get(\"next\")\n    return out\n\n\ndef open_nwb(asset):\n    \"\"\"Streams one NWB file with remfile and h5py (no download).\"\"\"\n    import h5py\n    import remfile\n    url = f\"{DANDI_API}/assets/{asset['asset_id']}/download/\"\n    return h5py.File(remfile.File(url), \"r\")\n\n\ndef read_session(f):\n    \"\"\"dF/F per PB midline ROI, the cue position, the trials table, and metadata.\"\"\"\n    rrs = f[\"processing/ophys/Fluorescence/RoiResponseSeries\"]\n    pos = f[\"processing/behavior/Position/SpatialSeries\"]\n    out = {\n        \"description\": f[\"session_description\"][()].decode(),\n        \"subject\": f[\"general/subject/subject_id\"][()].decode(),\n        \"rate_meta\": float(f[\"general/optophysiology/imaging_plane/imaging_rate\"][()]),\n        \"dff\": rrs[\"data\"][:],\n        \"t\": rrs[\"timestamps\"][:],\n        \"cue\": pos[\"data\"][:],\n        \"t_cue\": pos[\"timestamps\"][:],\n        \"cue_unit\": pos[\"data\"].attrs.get(\"unit\"),\n        \"tps_shape\": f[\"acquisition/TwoPhotonSeries/data\"].shape,\n        \"t_tps\": f[\"acquisition/TwoPhotonSeries/timestamps\"][:],\n        \"masks\": f[\"processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask\"][:],\n    }\n    if \"trials\" in f[\"intervals\"]:\n        tr = f[\"intervals/trials\"]\n        out[\"trials\"] = {k: tr[k][:] for k in tr.keys() if k != \"id\"}\n        out[\"trial_desc\"] = {k: tr[k].attrs.get(\"description\") for k in tr.keys() if k != \"id\"}\n    return out\n\n\ndef fourier(act, k=2):\n    \"\"\"Population vector of the activity at spatial frequency k across the ROIs, ordered along the\n    PB midline (k = 2: the two copies of the bump across the bridge; the frequency is checked in the\n    notebook as the peak of the spatial spectrum). Each ROI's preferred HD is 2 pi k j / n, the\n    decoder A = (cos phi, sin phi) of the Methods, scaled by 2/n as in the paper's code (Figure2h:\n    theta = 2/N A r). Returns (phase, amplitude) per frame.\"\"\"\n    n = act.shape[1]\n    ph = 2 * np.pi * k * np.arange(n) / n\n    z = 2 / n * act @ np.exp(-1j * ph)\n    return np.angle(z), np.abs(z)\n\n\ndef spectrum(act):\n    a = act - act.mean(1, keepdims=True)\n    return np.abs(np.fft.rfft(a, axis=1)).mean(0)\n\n\ndef raw_roi_fluorescence(f, frames, masks, projection=\"mean\"):\n    \"\"\"Raw fluorescence per ROI from the TwoPhotonSeries for the given frame blocks: the volume is\n    projected over planes (`projection`) and averaged over each ROI's 2D mask. The projection is not\n    stated in the files; the notebook picks it by agreement with the stored dF/F.\"\"\"\n    d = f[\"acquisition/TwoPhotonSeries/data\"]\n    m = masks.reshape(masks.shape[0], -1).astype(float)\n    m /= m.sum(1, keepdims=True)\n    out = []\n    for a, b in frames:\n        v = d[a:b].astype(np.float32)\n        p = v.mean(1) if projection == \"mean\" else v.max(1)\n        out.append(p.reshape(p.shape[0], -1) @ m.T)\n    return np.concatenate(out)\n"
}
```

```
File created successfully at: entries/000289-kutschireiter-2023/bra.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR; md5sum hb.tgz; python3 -c "import base64;print(base64.b64decode('7B4HbRVELzaPpZeLAPSmHA==').hex())"
```

```
ec1e076d15442f368fa5978b00f4a61c  hb.tgz
ec1e076d15442f368fa5978b00f4a61c
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/000289-kutschireiter-2023; . $TMPDIR/venv/bin/activate; cat > $TMPDIR/proto1.py <<'EOF'
import numpy as np, time, sys
sys.path.insert(0,'.')
import bra
t0=time.time()
code=bra.Code(); flt=code.flt
print('load',time.time()-t0)
# fig1
for g in (1,10):
    a=flt.xi_fun_inv(g*0.01)
    for k in (1,2,5):
        conf=abs(k+a); opp=abs(k-a)
        _,kc=flt.vM_Projection(0.,k,1.,z=0.,kappa_z=a,dy=0.,kappa_v=1.)
        _,ko=flt.vM_Projection(0.,k,1.,z=np.pi,kappa_z=a,dy=0.,kappa_v=1.)
        _,kn=flt.vM_Projection(0.,k,1.,z=0.,kappa_z=0,dy=0.,kappa_v=1.)
        print(g,round(a,4),k,conf,opp,kc,ko,kn)
# fig2h
for rate in (15,10):
    ns=bra.run_figure2h(code,rate)
    phi,muK,kK,muN,kN=ns['phi'],ns['mu_ProF'],ns['kappa_ProF'],ns['mu_NN'],ns['kappa_NN']
    t=ns['t']; cue=(t<5)|(t>=10)
    a=np.mean(np.abs(bra.circ_diff(muN,muK))); e=np.mean(np.abs(bra.circ_diff(muK,phi)))
    r=np.corrcoef(kN[cue],kK[cue])[0,1]
    print(rate,a,e,r,kN[500],kN[999],kN[499],kK[500],kK[999])
print(time.time()-t0)
EOF
python $TMPDIR/proto1.py
```

```
load 2.318730115890503
1 0.1416 1 1.1415983170283326 0.8584016829716674 1.137768138946217 0.8558487835159901 0.9968506069984072
1 0.1416 2 2.1415983170283326 1.8584016829716674 2.1292708939876834 1.849293656916505 1.9893776478042313
1 0.1416 5 5.141598317028333 4.858401682971667 5.038751317768872 4.768420751979219 4.903688515357737
10 0.4529 1 1.4528618311292025 0.5471381688707975 1.4471670720989342 0.5456667009477799 0.9968506069984072
10 0.4529 2 2.4528618311292023 1.5471381688707975 2.436052845294755 1.5407601328837957 1.9893776478042313
10 0.4529 5 5.452861831129202 4.547138168870798 5.334936537926399 4.470341091776428 4.903688515357737
15 0.016266424166045793 0.48304502424718077 0.9936241715765087 7.214148129564657 1.2201412773248126 7.386990966261592 7.270836029855926 0.8810759468015427
10 0.021309934005413672 0.49062610330547507 0.9931296446606996 5.888199772182238 1.2117963802455993 6.000919881315169 5.955797843189847 0.8624402431556586
2.4036858081817627
```

**Agent calls Bash**

```bash
cd entries/000289-kutschireiter-2023; . $TMPDIR/venv/bin/activate; cat > $TMPDIR/proto2.py <<'EOF'
import numpy as np, sys
sys.path.insert(0,'.')
import bra
code=bra.Code(); flt=code.flt; R=bra.RATES
d=code.npz('figure2i.npz'); vm,vq,pf,nu=d['vonMises_stats'],d['vonMises_q_stats'],d['PF_stats'],d['noUncert_stats']
accK,accB=vm[0,:,1],vq[0,:,1]; kK,kB=vm[0,:,2],vq[0,:,2]
diff=accB-accK
for thr in (1,3):
    s=R>=thr; print('fig2i reliable>=',thr,'max|diff|',np.abs(diff[s]).max())
low=R<=0.1; print('low acc diff',diff[low], 'cert',kB[low]-kK[low])
# fig3b
mse=np.array([bra.objective(nu[i,:,1]) for i in range(len(bra.KAPPA_FIXED))]); ib=mse.argmax(); print('best kappa*',bra.KAPPA_FIXED[ib])
dB=accB-nu[ib,:,1]; print('fig3b diffs',dB.round(4)); print('min diff idx',R[np.argsort(dB)[:3]])
# fig3c
for name,dt,w in [('i',0.01,lambda a,k:np.arctan(a/k)/np.pi),('ii',0.1,lambda a,k:np.arctan2(a,k)/(np.pi/2))]:
    al=np.array([flt.xi_fun_inv(r*dt) for r in R])
    wd=np.abs(w(al,kK)-w(al,kB)); print('fig3c',name,'max>=1',wd[R>=1].max(),'argmax rate',R[wd.argmax()],wd.max())
# fig3d
ref=bra.objective(pf[0,:,1]); print('refPF',ref, bra.REF_PF_3F)
m=code.npz('figure3d.npz')['MSE_array']/ref
i,j=np.unravel_index(np.nanargmax(m),m.shape); print('best k*,beta',bra.KSTAR_3D[i],bra.BETA_GRID[j],m[i,j]); ib_=list(bra.KSTAR_3D).index(1.0); jb=list(bra.BETA_GRID).index(0.5); print('bayes',m[ib_,jb],(m[i,j]-m[ib_,jb])/m[i,j])
print('max over k* per beta',np.nanmax(m,0).round(4)); print('argmax k*',bra.KSTAR_3D[np.nanargmax(m,0)])
# fig3f
res=[]
for s in bra.SIGMAS_3F:
    z=code.npz(f'figure3f/sigma={s}.npz'); res.append((z['MSE_array'],z['avg_network_activity']))
M0=res[0][0]/bra.REF_PF_3F; idx_ref=np.unravel_index(np.nanargmax(M0),M0.shape); print('ref idx',bra.KSTAR_3F[idx_ref[0]],bra.BETA_GRID[idx_ref[1]])
for s,(M,A) in zip(bra.SIGMAS_3F,res):
    Mn=M/bra.REF_PF_3F; idx=np.unravel_index(np.nanargmax(Mn),Mn.shape)
    mx=Mn[idx]; nr=Mn[idx_ref]
    snr=A[idx]/s*np.sqrt(32) if s>0 else np.nan; snr0=A[idx_ref]/s*np.sqrt(32) if s>0 else np.nan
    print(s, round(mx*100,2), round(nr*100,2), 'legend-norm', round(mx/M0[idx_ref]*100,2), round(nr/M0[idx_ref]*100,2), 'snr',snr,snr0, bra.KSTAR_3F[idx[0]],bra.BETA_GRID[idx[1]])
# fig4g
g=code.npz('figure4g.npz'); print('fig4g',np.abs(g['CX_stats'][:,1]-g['vonMises_q_stats'][:,1]).round(4))
# S2
s2=code.npz('figureS2.npz')['MSE_array']; ref2=code.npz('vonMises_q_stats.npz')['stats'][:,1]
for n,row in zip(bra.N_S2,s2): print('S2',n,np.nanmax(np.abs(row-ref2)).round(4), np.isnan(row).sum())
EOF
python $TMPDIR/proto2.py
```

```
fig2i reliable>= 1 max|diff| 0.0010343336173694873
fig2i reliable>= 3 max|diff| 0.00028481229589294443
low acc diff [-0.07285335 -0.08351574 -0.05726449] cert [0.82423122 0.69375458 0.49236579]
best kappa* 1.7
fig3b diffs [0.0115 0.0358 0.0907 0.1226 0.1179 0.1173 0.0945 0.0787 0.0795 0.0668
 0.0609 0.0623 0.0343 0.0349 0.0481 0.0515 0.0563 0.0635 0.0676 0.0675
 0.0762 0.1091 0.131 ]
min diff idx [0.01 2.   3.  ]
fig3c i max>=1 0.0010218475140976388 argmax rate 0.01 0.020973883049453235
fig3c ii max>=1 0.0061841250243150625 argmax rate 0.01 0.12969277743164437
refPF 0.6912447327304075 0.6912447327304075
best k*,beta 0.7 0.3 1.0011760866106045
bayes 0.9955068117349586 0.005662615149787276
max over k* per beta [0.9992 0.9986 1.0012 0.9981 0.9968 0.9947 0.9934 0.9942 0.988  0.9893
 0.9725 0.9525 0.9322]
argmax k* [0.3 0.5 0.7 0.8 0.8 0.9 1.1 1.1 1.1 1.  1.2 1.6 1.5]
ref idx 0.5 0.2
0.0 100.08 100.08 legend-norm 100.0 100.0 snr nan nan 0.5 0.2
1.0 99.45 99.15 legend-norm 99.36 99.07 snr 14.497152433308951 13.859604869179158 0.3 0.1
2.0 97.78 97.35 legend-norm 97.7 97.27 snr 7.848664029087684 6.758288309661715 0.9 0.3
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000289-kutschireiter-2023; . $TMPDIR/venv/bin/activate; cat > $TMPDIR/proto3.py <<'EOF'
import numpy as np, sys, time
sys.path.insert(0,'.')
import bra
code=bra.Code(); flt=code.flt
# validation vs released function
N=16; T=0.5; steps=50
np.random.seed(3)
r,mu,ka=flt.RNN_filter_Run(T,N=N,dt=0.01,w_even=1.5,w_quad=0.5,tau=1,I_ext=0,stoch_corr=0,phi_0=0,kappa_0=1,sigma_N=1.0)
np.random.seed(3); noise=np.random.randn(steps,N)[:,None,:]
mb,kb=bra.rnn_batch(None,1,T,N,1.0,1.5,0.5,noise=noise)
print('max diff',np.abs(mb[:,0]-mu).max(),np.abs(kb[:,0]-ka).max())
t0=time.time()
rng=np.random.default_rng(0)
for N in (64,256):
    m0,k0=bra.rnn_batch(rng,1,5,N,0.0,1.5,0.5)
    for s in (1.,2.):
        t1=time.time()
        m,k=bra.rnn_batch(rng,2000,5,N,s,1.5,0.5)
        dmu=bra.circ_diff(m[-1],m[0]); se=dmu.std()/np.sqrt(len(dmu))
        var=[np.var(bra.circ_diff(m[int(t/0.01)-1],m[0])) for t in (1,2,3,4,5)]
        inc=np.diff(k,axis=0).std()
        print(N,s,'mean dmu',dmu.mean(),'se',se,'var',np.round(var,4),'kend',k[-1].mean(),'k0end',k0[-1,0],'incSD',inc,time.time()-t1)
EOF
python $TMPDIR/proto3.py
```

```
max diff 1.1102230246251565e-16 4.440892098500626e-16
64 1.0 mean dmu -0.013878013012653186 se 0.010961170864789201 var [0.0339 0.0717 0.1184 0.1784 0.2403] kend 0.8312365157255054 k0end 1.0007380059659816 incSD 0.017710283348546203 0.9548275470733643
64 2.0 mean dmu -0.03164136486335941 se 0.03144269752762406 var [0.1677 0.5982 1.0588 1.6015 1.9773] kend 0.6262132772112348 k0end 1.0007380059659816 incSD 0.03530563027650571 0.8755621910095215
256 1.0 mean dmu 0.00430003595343758 se 0.005046308862961418 var [0.008  0.0174 0.0279 0.0374 0.0509] kend 0.8142591552674958 k0end 1.0000460865535006 incSD 0.008851143675042738 3.8408143520355225
256 2.0 mean dmu -0.04661508603311908 se 0.019658971720774025 var [0.0375 0.1107 0.2593 0.4613 0.773 ] kend 0.42238359218580235 k0end 1.0000460865535006 incSD 0.017694767477457147 3.8301615715026855
```

**Agent calls Bash**

```bash
cd entries/000289-kutschireiter-2023; . $TMPDIR/venv/bin/activate; cat > $TMPDIR/proto4.py <<'EOF'
import numpy as np, sys, pandas as pd
sys.path.insert(0,'.')
import bra
neu,con=bra.hemibrain()
types={'EPG':'EPG','PEN_a(PEN1)':'PEN1','Delta7':'D7'}
s=neu[neu.type.isin(types)].copy(); s['t']=s.type.map(types); s['g']=s.instance.map(bra.pb_glomerulus)
print(s.groupby('t').g.apply(lambda x:x.isna().sum()))
s['x']=s.g.map({g:i for i,g in enumerate(bra.PB_ORDER)})
pre=s.add_suffix('_pre').rename(columns={'bodyId_pre':'bodyId_pre'}); post=s.add_suffix('_post')
c=con.merge(s[['bodyId','t','g','x']].add_suffix('_pre'),on='bodyId_pre').merge(s[['bodyId','t','g','x']].add_suffix('_post'),on='bodyId_post')
def cmean(x,w):  # circular mean of within-side index, period 8
    z=np.sum(w*np.exp(2j*np.pi*x/8))/np.sum(w); return np.angle(z)*8/(2*np.pi)
rows=[]
for b,p in s[s.t=='PEN1'].set_index('bodyId').iterrows():
    side=p.g[0]
    inp=c[(c.bodyId_post==b)&(c.t_pre=='EPG')]; out=c[(c.bodyId_pre==b)&(c.t_post=='EPG')]
    for sel,name in [(lambda d,col: d[d[col].str[0]==side],'same'),(lambda d,col:d,'both')]:
        i=sel(inp,'g_pre'); o=sel(out,'g_post')
        off=cmean(o.x_post.values,o.weight.values)-cmean(i.x_pre.values,i.weight.values)
        off=(off+4)%8-4
        rows.append(dict(body=b,g=p.g,side=side,sel=name,off=off,nin=i.weight.sum(),nout=o.weight.sum()))
r=pd.DataFrame(rows); print(r.groupby(['sel','side']).off.describe())
print(r[r.sel=='same'].sort_values('g')[['g','off']].T.round(2).to_string())
# D7 breadth
for b,p in s[s.t=='D7'].set_index('bodyId').iterrows():
    i=c[(c.bodyId_post==b)&(c.t_pre=='EPG')].groupby('g_pre').weight.sum(); o=c[(c.bodyId_pre==b)&(c.t_post=='EPG')].groupby('g_post').weight.sum()
    print(p.instance, (i>0).sum(), (o>0).sum(), (i>=5).sum(),(o>=5).sum(), i.sum(),o.sum())
EOF
python $TMPDIR/proto4.py
```

```
t
D7      42
EPG      0
PEN1     0
Name: g, dtype: int64
           count      mean       std  ...       50%       75%       max
sel  side                             ...                              
both L      10.0  0.373726  0.173869  ...  0.359703  0.454528  0.670424
     R      10.0 -0.345720  0.148729  ... -0.350772 -0.300978  0.003823
same L      10.0  0.564189  0.203242  ...  0.570288  0.697644  0.775538
     R      10.0 -0.477437  0.201690  ... -0.530229 -0.460616  0.018885

[4 rows x 8 columns]
           6         34        16        12        38        32        10        0         26       30        20        4         36        2         18        8         14        22        24        28
g          L2        L3        L4        L4        L5        L6        L6        L7        L8       L9        R2        R3        R4        R4        R5        R6        R6        R7        R8        R9
off  0.543006  0.706446  0.775538  0.702345  0.597569  0.683542  0.530065  0.536741  0.520249  0.04639 -0.509455 -0.551002 -0.319775 -0.453441 -0.610842 -0.575456 -0.482142 -0.689948 -0.601195  0.018885
Delta7(PB15)_L6R3_L 16 13 15 5 376 175
Delta7(PB15)_L5R4_L 16 12 12 4 428 140
Delta7(PB15)_L5R4_L 15 9 14 5 411 138
Delta7(PB15)_L4R5_R 16 10 12 3 390 146
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd entries/000289-kutschireiter-2023; . $TMPDIR/venv/bin/activate; cat > $TMPDIR/proto5.py <<'EOF'
import numpy as np, sys, time
sys.path.insert(0,'.')
import bra
A=bra.assets()
con=[a for a in A if int(a['path'].split('/')[0][4:]) <= 15]
print(len(con))
a=[x for x in con if x['path'].startswith('sub-1/')][0]
f=bra.open_nwb(a); s=bra.read_session(f)
print(s['description'],s['dff'].shape,s['tps_shape'],np.abs(s['t']-s['t_tps']).max(), np.abs(s['t']-s['t_cue']).max())
# raw F check on a block
t0=time.time()
blocks=[(i,i+25) for i in range(0,s['tps_shape'][0]-25,250)]
idx=np.concatenate([np.arange(a,b) for a,b in blocks])
for proj in ('mean','max'):
    F=bra.raw_roi_fluorescence(f,blocks[:8],s['masks'],proj)
    d=s['dff'][idx[:F.shape[0]]]
    F0=np.percentile(F,10,axis=0); dff=(F-F0)/F0
    cc=[np.corrcoef(F[:,j],d[:,j])[0,1] for j in range(F.shape[1])]
    print(proj,np.median(cc),np.min(cc),time.time()-t0)
EOF
python $TMPDIR/proto5.py
```

```
Thu Oct 29 23:27:11 UTC 2026
15
fly presented with visual cues of varying contrast (11020, 37) (11020, 12, 256, 128) 0.0 0.0
mean 0.6407634890667254 0.1506638379062059 5.237341403961182
max 0.5838491199749517 0.0789383844920825 5.315242052078247
```

**Agent calls Bash**

```bash
cd entries/000289-kutschireiter-2023; . $TMPDIR/venv/bin/activate; cat > $TMPDIR/proto6.py <<'EOF'
import numpy as np, sys, time
from scipy.ndimage import uniform_filter, gaussian_filter
sys.path.insert(0,'.')
import bra
A=bra.assets()
a=[x for x in A if x['path'].startswith('sub-1/')][0]
f=bra.open_nwb(a); s=bra.read_session(f)
d=f['acquisition/TwoPhotonSeries/data']
V=np.concatenate([d[i:i+25].astype(np.float32) for i in range(0,2500,250)])  # 250 vols
idx=np.concatenate([np.arange(i,i+25) for i in range(0,2500,250)])
D=s['dff'][idx]
m=s['masks'].reshape(s['masks'].shape[0],-1).astype(float); m/=m.sum(1,keepdims=True)
def cc(F): return np.median([np.corrcoef(F[:,j],D[:,j])[0,1] for j in range(F.shape[1])])
for p in range(V.shape[1]):
    print('plane',p,round(cc(V[:,p].reshape(len(V),-1)@m.T),3), V[:,p].mean().round(1))
for sig in (1,2,4):
    P=gaussian_filter(V.mean(1),(0,sig,sig)); print('mean proj smoothed',sig,round(cc(P.reshape(len(V),-1)@m.T),3))
# temporal smoothing of F?
F=V.mean(1).reshape(len(V),-1)@m.T
print('mask centers', [np.argwhere(s['masks'][j]).mean(0).round(1) for j in (0,10,20,36)])
EOF
python $TMPDIR/proto6.py
```

```
plane 0 0.048 19.5
plane 1 0.223 32.4
plane 2 0.232 38.0
plane 3 0.165 40.2
plane 4 0.149 43.3
plane 5 0.263 47.8
plane 6 0.271 53.6
plane 7 0.296 57.6
plane 8 0.352 57.6
plane 9 0.247 54.7
plane 10 0.145 51.8
plane 11 0.105 49.1
mean proj smoothed 1 0.843
mean proj smoothed 2 0.894
mean proj smoothed 4 0.925
mask centers [array([34.2, 32. ]), array([57.5, 70. ]), array([133. ,  74.1]), array([231.,  42.])]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000289-kutschireiter-2023/bra.py",
 "old_string": "def raw_roi_fluorescence(f, frames, masks, projection=\"mean\"):\n    \"\"\"Raw fluorescence per ROI from the TwoPhotonSeries for the given frame blocks: the volume is\n    projected over planes (`projection`) and averaged over each ROI's 2D mask. The projection is not\n    stated in the files; the notebook picks it by agreement with the stored dF/F.\"\"\"\n    d = f[\"acquisition/TwoPhotonSeries/data\"]\n    m = masks.reshape(masks.shape[0], -1).astype(float)\n    m /= m.sum(1, keepdims=True)\n    out = []\n    for a, b in frames:\n        v = d[a:b].astype(np.float32)\n        p = v.mean(1) if projection == \"mean\" else v.max(1)\n        out.append(p.reshape(p.shape[0], -1) @ m.T)\n    return np.concatenate(out)",
 "new_string": "def raw_roi_fluorescence(f, frames, masks, projection=\"mean\", smooth=4.0):\n    \"\"\"Raw fluorescence per ROI from the TwoPhotonSeries for the given frame blocks: the volume is\n    projected over planes (`projection`), smoothed in the plane with a Gaussian of SD `smooth`\n    pixels, and averaged over each ROI's 2D mask (5 to 9 pixels on the PB midline). Neither the\n    projection nor the extent of an ROI is stated in the files; the notebook picks them by agreement\n    with the stored dF/F, and shows the alternatives.\"\"\"\n    from scipy.ndimage import gaussian_filter\n    d = f[\"acquisition/TwoPhotonSeries/data\"]\n    m = masks.reshape(masks.shape[0], -1).astype(float)\n    m /= m.sum(1, keepdims=True)\n    out = []\n    for a, b in frames:\n        v = d[a:b].astype(np.float32)\n        p = v.mean(1) if projection == \"mean\" else v.max(1)\n        if smooth:\n            p = gaussian_filter(p, (0, smooth, smooth))\n        out.append(p.reshape(p.shape[0], -1) @ m.T)\n    return np.concatenate(out)"
}
```

```
The file entries/000289-kutschireiter-2023/bra.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/000289-kutschireiter-2023; . $TMPDIR/venv/bin/activate; cat > $TMPDIR/proto7.py <<'EOF'
import numpy as np, sys, time
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0,'.')
import bra
A=bra.assets()
con=sorted([a for a in A if int(a['path'].split('/')[0][4:]) <= 15],key=lambda a:int(a['path'].split('/')[0][4:]))
def one(a):
    f=bra.open_nwb(a); s=bra.read_session(f); return s
t0=time.time()
with ThreadPoolExecutor(8) as ex: S=list(ex.map(one,con))
print('load',time.time()-t0)
for s in S:
    tr=s['trials']; sp=bra.spectrum(s['dff'])
    ph,amp=bra.fourier(s['dff'])
    res={}
    for c in (1,2,3):
        m=np.zeros(len(s['t']),bool)
        for st,en,cc in zip(tr['start_time'],tr['stop_time'],tr['cue_contrast']):
            if cc==c: m|=(s['t']>=st)&(s['t']<en)
        res[c]=amp[m].mean()
        # cue-phase coupling
    print(s['subject'],s['dff'].shape[1],sp.argmax(),tr['cue_contrast'],{k:round(v,3) for k,v in res.items()}, np.round(np.diff(np.r_[tr['start_time'],tr['stop_time'][-1]]),1))
EOF
python $TMPDIR/proto7.py
```

```
load 45.096795320510864
1 37 2 [2. 1. 3. 1. 2. 3.] {1: np.float64(0.471), 2: np.float64(0.461), 3: np.float64(0.538)} [195.  199.9 199.9 200.1 200.  205. ]
2 38 2 [3. 1. 2. 1. 2.] {1: np.float64(0.572), 2: np.float64(0.567), 3: np.float64(0.722)} [194.8 199.9 200.1 200.  405.1]
3 39 2 [1. 2. 1. 3. 2. 3.] {1: np.float64(0.631), 2: np.float64(0.667), 3: np.float64(0.68)} [194.9 200.  199.9 200.1 199.9 205.1]
4 41 2 [1. 2. 1. 3. 2. 3.] {1: np.float64(0.802), 2: np.float64(0.823), 3: np.float64(0.812)} [195.3 200.  200.  200.  200.  204.8]
5 42 2 [3. 1. 2. 1. 2. 3.] {1: np.float64(0.301), 2: np.float64(0.292), 3: np.float64(0.327)} [195.4 200.  200.  199.9 200.1 204.6]
6 43 2 [2. 1. 3. 1. 2. 3.] {1: np.float64(0.838), 2: np.float64(0.748), 3: np.float64(0.678)} [195.4 200.  200.  199.9 200.1 204.6]
7 47 2 [1. 2. 1. 3. 2. 3.] {1: np.float64(0.393), 2: np.float64(0.456), 3: np.float64(0.552)} [195.8 199.9 200.1 199.9 200.1 204.2]
8 41 2 [3. 1. 2. 1. 2. 3.] {1: np.float64(0.536), 2: np.float64(0.536), 3: np.float64(0.6)} [196.1 199.9 200.  199.9 200.1 203.9]
9 44 2 [2. 1. 3. 1. 2. 3.] {1: np.float64(0.486), 2: np.float64(0.433), 3: np.float64(0.553)} [195.3 199.9 200.1 199.9 200.  204.7]
10 44 2 [2. 1. 3. 1. 2. 3.] {1: np.float64(0.646), 2: np.float64(0.674), 3: np.float64(0.473)} [195.9 200.  200.1 200.  200.  204. ]
11 42 2 [3. 1. 2. 1. 2. 3.] {1: np.float64(0.516), 2: np.float64(0.503), 3: np.float64(0.57)} [194.9 199.9 200.  199.9 200.1 205.1]
12 43 2 [1. 2. 1. 3. 2. 3.] {1: np.float64(0.539), 2: np.float64(0.616), 3: np.float64(0.703)} [195.4 200.  200.  199.9 200.1 204.6]
13 42 2 [3. 1. 2. 1. 2. 3.] {1: np.float64(0.731), 2: np.float64(0.89), 3: np.float64(0.779)} [195.9 200.  199.9 200.1 200.  204. ]
14 44 2 [1. 2. 1. 3. 2. 3.] {1: np.float64(0.409), 2: np.float64(0.597), 3: np.float64(0.545)} [195.  199.9 200.1 199.9 200.  205. ]
15 41 2 [2. 1. 3. 1. 2. 3.] {1: np.float64(0.721), 2: np.float64(0.655), 3: np.float64(0.71)} [195.4 200.  200.  199.9 200.1 204.6]
```

**Agent calls Bash**

```bash
cd entries/000289-kutschireiter-2023; . $TMPDIR/venv/bin/activate; python -c "
import sys;sys.path.insert(0,'.');import bra,numpy as np
c=bra.Code();s2=c.npz('figureS2.npz')['MSE_array'];ref=c.npz('vonMises_q_stats.npz')['stats'][:,1]
np.set_printoptions(linewidth=200)
print((s2-ref).round(3))
g=c.npz('figure4g.npz');print(g['CX_stats'][:,1].round(3));print(g['vonMises_q_stats'][:,1].round(3)); print(ref.round(3)); print(c.npz('figure2i.npz')['vonMises_q_stats'][0,:,1].round(3))
"; date -u
```

```
[[-0.002 -0.002 -0.01  -0.01  -0.007 -0.     0.003  0.003 -0.007  0.008 -0.005 -0.004  0.003 -0.001 -0.001  0.001  0.003  0.005  0.002  0.002  0.001  0.    -0.   ]
 [-0.012 -0.012 -0.019  0.01   0.005 -0.     0.005  0.003  0.001 -0.004 -0.005  0.001  0.002 -0.003  0.     0.003  0.002  0.004  0.004 -0.003  0.    -0.001  0.   ]
 [-0.005  0.001 -0.018  0.005 -0.005  0.009  0.001  0.01  -0.002  0.001 -0.009 -0.012 -0.001  0.002 -0.003  0.004 -0.    -0.001  0.003 -0.001  0.002 -0.002  0.   ]
 [ 0.003 -0.009 -0.041 -0.004 -0.002  0.007 -0.001  0.01  -0.008  0.009  0.003 -0.013  0.005  0.008 -0.002  0.003 -0.     0.     0.004 -0.001  0.001 -0.002  0.001]
 [-0.002  0.009 -0.002  0.004  0.008 -0.004  0.004 -0.002 -0.     0.007  0.002  0.001  0.005  0.006  0.004 -0.001  0.005 -0.003  0.006 -0.004  0.    -0.     0.   ]
 [ 0.002  0.    -0.014  0.012  0.011 -0.007  0.004  0.007  0.004  0.01   0.003 -0.013  0.009  0.007 -0.002 -0.003  0.004  0.     0.002 -0.001  0.001 -0.003  0.001]
 [ 0.     0.008 -0.013 -0.001  0.006 -0.009 -0.     0.001 -0.007  0.001 -0.    -0.004  0.005  0.01  -0.005 -0.002  0.     0.005  0.004 -0.    -0.    -0.002    nan]]
[0.029 0.078 0.213 0.33  0.422 0.455 0.496 0.526 0.558 0.589 0.596 0.641 0.732 0.787 0.811 0.828 0.845 0.858 0.867 0.875 0.883 0.932 0.962]
[0.023 0.072 0.194 0.316 0.412 0.451 0.492 0.524 0.556 0.588 0.598 0.641 0.734 0.789 0.814 0.831 0.848 0.86  0.869 0.877 0.884 0.934 0.963]
[0.029 0.069 0.216 0.321 0.397 0.459 0.495 0.529 0.566 0.58  0.608 0.63  0.728 0.779 0.814 0.832 0.847 0.861 0.868 0.88  0.884 0.937 0.965]
[0.029 0.069 0.216 0.321 0.397 0.459 0.495 0.529 0.566 0.58  0.608 0.63  0.728 0.779 0.814 0.832 0.847 0.861 0.868 0.88  0.884 0.937 0.965]
Thu Oct 29 23:29:03 UTC 2026
```

**Agent calls Bash**

```bash
cd  sed -n 1,80p entries/001453-fouke-2025/README.md; python -c "
import json;nb=json.load(open('entries/001453-fouke-2025/reproduce_fouke_2025.ipynb'));
for c in nb['cells'][:4]: print(c['cell_type'],c['metadata'],''.join(c['source'])[:1500]); print('-----')
"; grep -n "install\|requirements" tools/entry.py | head -20
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
[... 96 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 125,210p tools/entry.py; sed -n 270,330p tools/entry.py
```

```
def _plain(value):
    """YAML dates as strings, so JSON Schema's string formats apply."""
    if isinstance(value, dict):
        return {k: _plain(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_plain(v) for v in value]
    if hasattr(value, "isoformat"):
        return value.isoformat()
    return value


def code_of(notebook_path: Path) -> str:
    nb = nbformat.read(notebook_path, as_version=4)
    return "\n".join(c.source for c in nb.cells if c.cell_type == "code")


# --- check --------------------------------------------------------------------

def check(entry_dir: Path) -> Report:
    report = Report()
[... 126 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build_nb.py",
 "content": "import nbformat as nbf\n\ncells = []\n\n\ndef md(s):\n    cells.append(nbf.v4.new_markdown_cell(s.strip(\"\\n\")))\n\n\ndef code(s, tags=None):\n    c = nbf.v4.new_code_cell(s.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nmd(r\"\"\"\n# Testing Kutschireiter et al. (2023) with dandiset 000289\n\n**Paper.** Kutschireiter A, Basnak MA, Wilson RI, Drugowitsch J (2023). Bayesian inference in ring\nattractor networks. *PNAS* 120, e2210622120.\n[doi:10.1073/pnas.2210622120](https://doi.org/10.1073/pnas.2210622120). The claims file was written\nfrom the version of record (Europe PMC, PMC9992764) with its SI Appendix.\n\n**Dandiset.** [DANDI:000289](https://dandiarchive.org/dandiset/000289/0.240801.1040), version\n0.240801.1040, \"Two-photon calcium imaging of EPG cells in Drosophila Melanogaster presented with\ncues of varying reliability\" (Basnak and Wilson). The paper cites no dandiset version. This is the\nonly published version and the most recent; the draft has the same 221 assets and size, so the\npublished version is pinned.\n\n**What the dandiset holds, and what the paper uses.** The paper is a theory paper: every result is\na simulation, apart from a connectome comparison and one prediction. The dandiset holds two-photon\nimaging of EPG neurons in the protocerebral bridge, with the cue position and trial tables, from a\nseparate study (Basnak et al., \"Uncertainty and learning in a biological ring attractor\", named in\nthe dandiset's description). So, as the claims file sets out:\n\n- twelve claims are `data: elsewhere`: they are tested on the paper's own code and processed\n  outputs, Zenodo [doi:10.5281/zenodo.7615975](https://doi.org/10.5281/zenodo.7615975)\n  (BayesianRingAttractor v1.0, commit a9db6f9), and, for Fig. 4B, on the hemibrain connectome;\n- one claim, the Discussion's prediction that bump amplitude is higher with a reliable cue, is\n  tested on the dandiset: 15 flies shown a visual cue at zero, low and high contrast.\n\nAll sources are read into memory; nothing is downloaded to disk.\n\n| Claim | Data | Tested |\n|---|---|---|\n| fig1-conflict-decreases-certainty | paper's code | tested |\n| fig2h-bump-tracks-circkf | paper's code (Figure2h.ipynb, run) | tested |\n| fig2i-accuracy-and-certainty-vs-reliability | figure2i.npz | tested |\n| fig3b-bayesian-beats-conventional | figure2i.npz | tested |\n| fig3c-update-weights | figure2i.npz | tested |\n| fig3d-best-network-slow-decay | figure3d.npz | tested |\n| fig3f-noise-drop-below-70 | figure3f/sigma=*.npz | tested |\n| fig3f-retuning-reduces-drop | figure3f/sigma=*.npz | tested |\n| noise-effects-on-mu-and-kappa | paper's code (RNN_filter_Run) | tested |\n| fig4b-connectome-motifs | hemibrain v1.2 export | tested (sorting reading (a) only) |\n| fig4gh-drosophila-network-matches | figure4g.npz | tested |\n| figs2-performance-independent-of-n | figureS2.npz | tested |\n| prediction-bump-amplitude-cue-reliability | dandiset 000289 | tested |\n\nNo claim is blocked.\n\"\"\")\n\ncode(r\"\"\"\nimport time\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport bra\n\npd.set_option(\"display.width\", 220)\npd.set_option(\"display.max_columns\", 40)\nnp.set_printoptions(linewidth=200, suppress=True)\nstarted = time.time()\n\ncode = bra.Code()          # the paper's Zenodo deposit, in memory, md5 checked\nflt = code.flt             # circularFiltering.py, with the patches listed below\nR = bra.RATES\nprint(\"Zenodo deposit doi:10.5281/zenodo.7615975, files:\", len(code.names))\nprint(\"\\n\".join(n for n in code.names if n.endswith((\".py\", \".ipynb\", \".npz\"))))\nprint(\"\\nPatches to the released code:\", *code.patches, sep=\"\\n- \")\n\"\"\")\n\nmd(r\"\"\"\n## Data check\n\nThe paper's processed outputs, the connectome export, and the 15 imaging sessions of the\ncue-contrast experiment are loaded and described. Each check of a description against the values is\nstated below the output.\n\"\"\")\n\ncode(r\"\"\"\n# --- the paper's processed outputs\nfor name in [\"figure2i.npz\", \"figure3d.npz\", \"figure4g.npz\", \"figureS2.npz\", \"vonMises_q_stats.npz\",\n             \"figure3f/sigma=0.0.npz\"]:\n    z = code.npz(name)\n    print(name, {k: z[k].shape for k in z.files})\nf2i = code.npz(\"figure2i.npz\")\nvm, vq, pf, nu = f2i[\"vonMises_stats\"], f2i[\"vonMises_q_stats\"], f2i[\"PF_stats\"], f2i[\"noUncert_stats\"]\nprint(\"\\nfigure2i.npz: axis 0 is the 33 kappa* of the fixed-certainty filter, axis 1 the 23 information rates\",\n      len(bra.KAPPA_FIXED), len(R))\nprint(\"accuracy |m1| range over all filters and rates: %.3f to %.3f (must lie in 0..1)\" %\n      (min(vm[0, :, 1].min(), vq[0, :, 1].min(), nu[:, :, 1].min()),\n       max(vm[0, :, 1].max(), vq[0, :, 1].max(), nu[:, :, 1].max())))\nprint(\"mean final certainty, circKF: %.2f to %.2f; Bayesian ring attractor: %.2f to %.2f\" %\n      (vm[0, :, 2].min(), vm[0, :, 2].max(), vq[0, :, 2].min(), vq[0, :, 2].max()))\nref_pf = bra.objective(pf[0, :, 1])\nprint(\"particle filter reference, objective(PF accuracy) = %.10f; Figure3f_FigureS4.ipynb hard-codes %.10f\"\n      % (ref_pf, bra.REF_PF_3F))\nprint(\"rows of figure2i.npz beyond the first, vonMises_stats all zero:\", bool(np.all(vm[1:] == 0)))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nThe processed outputs have the shapes the figure notebooks expect, accuracies lie in 0 to 1, and the\nparticle filter reference computed from `figure2i.npz` equals the constant hard-coded in\n`Figure3f_FigureS4.ipynb`, so the two notebooks normalize alike. The certainty stored for the\nBayesian ring attractor never falls below 1, its baseline kappa* (Methods), while the circKF's falls\nto 0.18.\n\"\"\")\n\ncode(r\"\"\"\n# --- the hemibrain connectome export (v1.2): neurons of the three types and their names\nneurons, conns = bra.hemibrain()\ntypes = {\"EPG\": \"EPG\", \"PEN_a(PEN1)\": \"PEN1\", \"Delta7\": \"Delta7\"}\ncx = neurons[neurons.type.isin(types)].copy()\ncx[\"t\"] = cx.type.map(types)\ncx[\"g\"] = cx.instance.map(bra.pb_glomerulus)\nprint(\"traced neurons:\", len(neurons), \"; connections:\", len(conns), \"; total synapses:\", conns.weight.sum())\nprint(cx.groupby(\"t\").agg(n=(\"bodyId\", \"size\"), with_glomerulus=(\"g\", lambda s: s.notna().sum())).to_string())\nfor t in [\"EPG\", \"PEN1\", \"Delta7\"]:\n    print(t, \"instances:\", sorted(cx[cx.t == t].instance.unique())[:6], \"...\")\nprint(\"glomeruli named: EPG\", sorted(cx[cx.t == 'EPG'].g.unique(), key=bra.PB_ORDER.index),\n      \"\\n                 PEN1\", sorted(cx[cx.t == 'PEN1'].g.unique(), key=bra.PB_ORDER.index))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\n46 EPG, 20 PEN1 and 42 Delta7 neurons. Every EPG and PEN1 instance names one protocerebral bridge\nglomerulus (EPG L8 to R8, PEN1 L9 to L2 and R2 to R9), which is reading (a) of the claim's sort.\nNo instance names an ellipsoid body or gall position, so reading (b) cannot be formed from the\nnames. Delta7 names list the glomeruli the neuron spans, not one position.\n\"\"\")\n\ncode(r\"\"\"\n# --- dandiset 000289: every asset, and the cue-contrast sessions\nassets = bra.assets()\nprint(\"dandiset\", bra.DANDISET, \"version\", bra.VERSION, \": assets\", len(assets),\n      \"; total size %.0f GB\" % (sum(a[\"size\"] for a in assets) / 1e9))\nsubj = lambda a: int(a[\"path\"].split(\"/\")[0][4:])\ncontrast_assets = sorted([a for a in assets if subj(a) <= 15], key=subj)\n\ndef load(a):\n    f = bra.open_nwb(a)\n    s = bra.read_session(f)\n    s[\"path\"] = a[\"path\"]\n    return s\n\nwith ThreadPoolExecutor(8) as ex:\n    sessions = list(ex.map(load, contrast_assets))\nprint(\"loaded %d sessions in %.0f s\" % (len(sessions), time.time() - started))\nrows = []\nfor s in sessions:\n    tr = s[\"trials\"]\n    dt = np.diff(s[\"t\"])\n    rows.append(dict(sub=s[\"subject\"], description=s[\"description\"][:45], rois=s[\"dff\"].shape[1],\n                     frames=s[\"dff\"].shape[0], planes=s[\"tps_shape\"][1], dur_s=round(s[\"t\"][-1] - s[\"t\"][0], 1),\n                     frame_hz=round(1 / dt.mean(), 2), meta_hz=s[\"rate_meta\"],\n                     dff_min=round(s[\"dff\"].min(), 2), dff_max=round(s[\"dff\"].max(), 2),\n                     cue_min=round(s[\"cue\"].min(), 3), cue_max=round(s[\"cue\"].max(), 3),\n                     same_clock=bool(np.array_equal(s[\"t\"], s[\"t_cue\"]) and np.array_equal(s[\"t\"], s[\"t_tps\"])),\n                     blocks=\"\".join(str(int(c)) for c in tr[\"cue_contrast\"]),\n                     block_s=\" \".join(str(round(b - a)) for a, b in zip(tr[\"start_time\"], tr[\"stop_time\"]))))\ninfo = pd.DataFrame(rows)\nprint(info.to_string(index=False))\nprint(\"\\nsession descriptions:\", info.description.unique())\nprint(\"trial column descriptions:\", sessions[0][\"trial_desc\"])\nprint(\"cue position unit:\", sessions[0][\"cue_unit\"])\n# recordings deposited twice? compare the dF/F of every pair of sessions with the same shape\ndups = [(a[\"sub\"], b[\"sub\"]) for i, a in enumerate(rows) for b in rows[i + 1:]\n        if sessions[i][\"dff\"].shape == sessions[[r[\"sub\"] for r in rows].index(b[\"sub\"])][\"dff\"].shape\n        and np.allclose(sessions[i][\"dff\"], sessions[[r[\"sub\"] for r in rows].index(b[\"sub\"])][\"dff\"])]\nprint(\"identical dF/F pairs among the 15 sessions:\", dups)\nprint(\"identical cue traces:\", [(rows[i][\"sub\"], rows[j][\"sub\"]) for i in range(15) for j in range(i + 1, 15)\n                                if sessions[i][\"cue\"].shape == sessions[j][\"cue\"].shape\n                                and np.allclose(sessions[i][\"cue\"], sessions[j][\"cue\"])])\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nThe cue-contrast experiment is subjects 1 to 15, one session each (\"fly presented with visual cues\nof varying contrast\"), with a trials table whose `cue_contrast` is 1 = zero, 2 = low and\n3 = high contrast. Each session is 1200 s of 37 to 47 dF/F traces along the PB midline. The dF/F,\nthe cue position and the raw imaging share one timestamp array. The cue position lies in 0 to 2 pi,\nas its unit (radians) says. No session duplicates another.\n\nTwo disagreements with the metadata: sub-4 and sub-10 have a frame interval of 0.127 s (7.87 Hz)\nand 14 planes, while `imaging_rate` says 9.18 Hz for every file; and sub-2 has five blocks (high,\nzero, low, zero, then 405 s labelled low), so it has one high-contrast block where every other fly\nhas two, and its last block is twice as long as the protocol's 200 s.\n\"\"\")\n\ncode(r\"\"\"\n# --- does the bump follow the cue on the session's clock? Bump phase (frequency 2 across the PB)\n# against the cue position, with the cue trace shifted in time, in each contrast.\ndef contrast_mask(s, c, shift_blocks=0):\n    tr = s[\"trials\"]\n    labels = np.roll(tr[\"cue_contrast\"], shift_blocks)\n    m = np.zeros(len(s[\"t\"]), bool)\n    for a, b, l in zip(tr[\"start_time\"], tr[\"stop_time\"], labels):\n        if l == c:\n            m |= (s[\"t\"] >= a) & (s[\"t\"] < b)\n    return m\n\nlags = np.arange(-30, 31, 5)\ncoh = {c: [] for c in (1, 2, 3)}\npeak = []\nfor s in sessions:\n    phase, _ = bra.fourier(s[\"dff\"])\n    for c in (1, 2, 3):\n        m = contrast_mask(s, c)\n        coh[c].append([np.abs(np.mean(np.exp(1j * (phase - np.roll(s[\"cue\"], L)))[m])) for L in lags])\n    peak.append(lags[np.argmax(coh[3][-1])])\nfor c, name in [(1, \"zero\"), (2, \"low\"), (3, \"high\")]:\n    print(\"%-4s contrast, phase-cue coherence by lag (frames):\" % name,\n          dict(zip(lags.tolist(), np.round(np.median(coh[c], 0), 3))))\nprint(\"lag of peak coherence in high contrast, per fly (frames):\", peak)\n# the trial table's clock: coherence in high-contrast frames with true and shifted block labels\ntrue = [np.abs(np.mean(np.exp(1j * (bra.fourier(s[\"dff\"])[0] - s[\"cue\"]))[contrast_mask(s, 3)])) for s in sessions]\nshift = [np.abs(np.mean(np.exp(1j * (bra.fourier(s[\"dff\"])[0] - s[\"cue\"]))[contrast_mask(s, 3, 1)])) for s in sessions]\nprint(\"median coherence in frames labelled high contrast: true labels %.3f, labels shifted one block %.3f\"\n      % (np.median(true), np.median(shift)))\nprint(\"flies where the true labels give the higher coherence: %d of 15\" % np.sum(np.array(true) > np.array(shift)))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nThe bump phase locks to the cue position at high contrast and not in darkness, and the coupling\npeaks within a few frames of lag 0 (printed per fly), so the dF/F and the cue position share a\nclock. Frames the trials table labels high contrast show stronger coupling than the same frames\nwith the labels shifted by one block, which is consistent with the trials table being on the same\nclock. This is consistent with the data, not a proof.\n\"\"\")\n\n# ---------------------------------------------------------------- claims\nmd(r\"\"\"\n## fig1-conflict-decreases-certainty\n\n> In the circular Kalman filter, an HD observation consistent with the current estimate increases\n> certainty, while one that strongly conflicts with it (opposite direction) decreases certainty.\n\nThe code's circKF step, `vM_Projection` (kappa_phi = 1, kappa_v = 1, dt = 0.01), from mu = 0 at\nkappa_t = 1, 2, 5, with the per-step reliability xi_fun_inv(gamma_z dt) for gamma_z = 1/s and 10/s.\n(a) is the vector addition alone (the code's update on the natural parameters); (b) is the full\nstep against the same step with no observation.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor gz in (1, 10):\n    alpha = flt.xi_fun_inv(gz * 0.01)\n    for k in (1, 2, 5):\n        upd_conf = abs(k * np.exp(0j) + alpha * np.exp(0j))           # observation at z = mu\n        upd_opp = abs(k * np.exp(0j) + alpha * np.exp(1j * np.pi))     # observation at z = mu + pi\n        _, full_conf = flt.vM_Projection(0., k, 1., z=0., kappa_z=alpha, dy=0., kappa_v=1., dt=0.01)\n        _, full_opp = flt.vM_Projection(0., k, 1., z=np.pi, kappa_z=alpha, dy=0., kappa_v=1., dt=0.01)\n        _, full_none = flt.vM_Projection(0., k, 1., z=0., kappa_z=0, dy=0., kappa_v=1., dt=0.01)\n        rows.append(dict(gamma_z=gz, alpha=round(alpha, 4), kappa_t=k, a_conf=upd_conf, a_opp=upd_opp,\n                         b_conf=full_conf, b_none=full_none, b_opp=full_opp,\n                         a_holds=upd_conf > k > upd_opp, b_holds=full_conf > full_none > full_opp))\nfig1 = pd.DataFrame(rows)\nprint(fig1.round(4).to_string(index=False))\nprint(\"\\n(a) holds in %d of 6 cases, (b) in %d of 6\" % (fig1.a_holds.sum(), fig1.b_holds.sum()))\n\"\"\", tags=[\"claim:fig1-conflict-decreases-certainty\"])\n\nmd(r\"\"\"\n**Result: reproduced.** In all six cases (three certainties, two reliabilities) a confirmatory\nobservation raises the certainty and an opposite one lowers it, both for the observation update\nalone and for the full step against the step without observation.\n\"\"\")\n\nmd(r\"\"\"\n## fig2h-bump-tracks-circkf\n\n> In a simulated Bayesian ring attractor of 80 neurons, the bump position tracks HD about as\n> accurately as the circular Kalman filter, the bump amplitude tracks the filter's certainty, and\n> when the visual cue is removed the amplitude decays toward its baseline.\n\nThe simulation cells of `Figure2h.ipynb` are executed as released (seed 42, T = 15, N = 80, cue off\nfrom 5 to 10 s, rate 15) and with the Methods' rate of 10/s. (a) mean absolute circular difference\nnetwork to circKF against the circKF's own mean absolute error; (b) Pearson correlation of bump\namplitude and circKF certainty over the cue periods; decay over the darkness.\n\"\"\")\n\ncode(r\"\"\"\nf2h = {}\nfor rate in (15, 10):\n    ns = bra.run_figure2h(code, rate)\n    t, phi = ns[\"t\"], ns[\"phi\"]\n    muK, kK, muN, kN = ns[\"mu_ProF\"], ns[\"kappa_ProF\"], ns[\"mu_NN\"], ns[\"kappa_NN\"]\n    cue = (t < 5) | (t >= 10)\n    i0, i1 = ns[\"ind_off\"], ns[\"ind_on\"] - 1\n    f2h[rate] = dict(\n        net_vs_kf=np.mean(np.abs(bra.circ_diff(muN, muK))), kf_err=np.mean(np.abs(bra.circ_diff(muK, phi))),\n        net_err=np.mean(np.abs(bra.circ_diff(muN, phi))), r_cue=np.corrcoef(kN[cue], kK[cue])[0, 1],\n        amp_dark_start=kN[i0], amp_dark_end=kN[i1], kf_dark_start=kK[i0], kf_dark_end=kK[i1],\n        amp_range=f\"{kN.min():.2f} to {kN.max():.2f}\")\n    d = f2h[rate]\n    d[\"a\"] = d[\"net_vs_kf\"] < d[\"kf_err\"]\n    d[\"b\"] = d[\"r_cue\"] >= 0.9\n    d[\"decay\"] = (d[\"amp_dark_end\"] < d[\"amp_dark_start\"]) and abs(d[\"amp_dark_end\"] - 1) < abs(d[\"amp_dark_start\"] - 1)\nprint(pd.DataFrame(f2h).T.to_string())\n\"\"\", tags=[\"claim:fig2h-bump-tracks-circkf\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Under both cue strengths the network's position differs from the circKF's by\na mean of 0.016 to 0.021 rad, against a circKF error to the true HD of 0.48 to 0.49 rad. Bump\namplitude and circKF certainty correlate at r = 0.99 over the cue periods. In darkness the amplitude\nfalls from 7.2 (rate 15) or 5.9 (rate 10) to 1.22 or 1.21, near the baseline of 1.\n\"\"\")\n\nmd(r\"\"\"\n## fig2i-accuracy-and-certainty-vs-reliability\n\n> The Bayesian ring attractor tracks HD with the same accuracy as the circular Kalman filter when HD\n> observations are reliable and with slightly lower accuracy when they are unreliable; in the\n> unreliable regime its certainty stays near its baseline and overestimates the filter's certainty.\n\"\"\")\n\ncode(r\"\"\"\naccK, accB, kK, kB = vm[0, :, 1], vq[0, :, 1], vm[0, :, 2], vq[0, :, 2]\nprint(pd.DataFrame(dict(rate=R, acc_circKF=accK, acc_attractor=accB, diff=accB - accK,\n                        cert_circKF=kK, cert_attractor=kB)).round(4).to_string(index=False))\nres = {}\nfor lo in (1, 3):\n    for bound in (0.01, 0.02):\n        res[(lo, bound)] = np.abs(accB - accK)[R >= lo].max() <= bound\n        print(\"reliable = rates >= %g/s: max |diff| = %.4f; within %.2f: %s\" %\n              (lo, np.abs(accB - accK)[R >= lo].max(), bound, res[(lo, bound)]))\nlow = R <= 0.1\nprint(\"rates 0.01 to 0.1: attractor accuracy below circKF at all:\", bool(np.all(accB[low] < accK[low])),\n      (accB - accK)[low].round(4))\nprint(\"rates 0.01 to 0.1: attractor certainty above circKF at all:\", bool(np.all(kB[low] > kK[low])),\n      (kB - kK)[low].round(3))\n\"\"\", tags=[\"claim:fig2i-accuracy-and-certainty-vs-reliability\"])\n\nmd(r\"\"\"\n**Result: reproduced.** At rates of 1/s and above the accuracies differ by at most 0.0010, so all\nfour combinations hold. At 0.01 to 0.1/s the attractor is less accurate (by 0.057 to 0.084) and\nits mean certainty is higher than the circKF's (by 0.49 to 0.82).\n\"\"\")\n\nmd(r\"\"\"\n## fig3b-bayesian-beats-conventional\n\n> A conventional ring attractor (fast decay to a fixed bump amplitude, with that amplitude optimized)\n> is less accurate than the Bayesian ring attractor at every HD observation reliability, and reaches\n> its accuracy only when observations are highly unreliable.\n\"\"\")\n\ncode(r\"\"\"\nscore = np.array([bra.objective(nu[i, :, 1]) for i in range(len(bra.KAPPA_FIXED))])\nib = int(np.argmax(score))\nprint(\"weighted accuracy of the fixed-certainty filter by kappa*:\",\n      dict(zip(bra.KAPPA_FIXED[:15].tolist(), np.round(score[:15], 4))), \"...\")\nprint(\"optimal kappa* = %g (weighted accuracy %.4f; Bayesian attractor %.4f)\" %\n      (bra.KAPPA_FIXED[ib], score[ib], bra.objective(accB)))\ndB = accB - nu[ib, :, 1]\nprint(pd.DataFrame(dict(rate=R, bayes=accB, conventional=nu[ib, :, 1], diff=dB)).round(4).to_string(index=False))\nmid = (R >= 0.1) & (R <= 10)\nprint(\"Bayesian >= conventional at all 23 rates:\", bool(np.all(dB >= 0)), \"; min diff %.4f\" % dB.min())\nprint(\"strictly above at every rate 0.1 to 10:\", bool(np.all(dB[mid] > 0)), \"; min there %.4f\" % dB[mid].min())\nprint(\"three smallest differences at rates:\", R[np.argsort(dB)[:3]], np.sort(dB)[:3].round(4))\n\"\"\", tags=[\"claim:fig3b-bayesian-beats-conventional\"])\n\nmd(r\"\"\"\n**Result: reproduced.** With the optimal kappa* = 1.7, the Bayesian attractor is more accurate than\nthe conventional one at all 23 rates (smallest difference 0.0115, at 0.01/s), and strictly so from\n0.1 to 10/s. The reported, not judged, part: the difference is smallest at 0.01/s, but at 0.03/s\n(0.036) it is larger than at 2 and 3/s (0.034 and 0.035), so \"only once highly unreliable\" holds at\nthe lowest rate only.\n\"\"\")\n\nmd(r\"\"\"\n## fig3c-update-weights\n\n> The weight given to a new HD observation by the Bayesian ring attractor depends on both the\n> observation's reliability and the current certainty and is close to that of the circular Kalman\n> filter, deviating only for very uninformative observations; a conventional attractor weights\n> observations by their reliability alone.\n\"\"\")\n\ncode(r\"\"\"\nweights = {\"i\": (0.01, lambda a, k: np.arctan(a / k) / np.pi),\n           \"ii\": (0.1, lambda a, k: np.arctan2(a, k) / (np.pi / 2))}\nok = {}\nfor name, (dt, w) in weights.items():\n    alpha = np.array([flt.xi_fun_inv(r * dt) for r in R])\n    wK, wB = w(alpha, kK), w(alpha, kB)\n    d = np.abs(wK - wB)\n    print(\"reading (%s), dt = %g: weights circKF %.4f to %.4f, attractor %.4f to %.4f\" % (name, dt, wK.min(), wK.max(), wB.min(), wB.max()))\n    print(\"   |diff| by rate:\", dict(zip(R.tolist(), d.round(4))))\n    for bound in (0.02, 0.05):\n        ok[(name, bound)] = d[R >= 1].max() <= bound\n        print(\"   max |diff| at rates >= 1: %.4f, within %.2f: %s\" % (d[R >= 1].max(), bound, ok[(name, bound)]))\n    print(\"   largest |diff| %.4f at rate %g (below 1/s: %s)\" % (d.max(), R[d.argmax()], R[d.argmax()] < 1))\n\"\"\", tags=[\"claim:fig3c-update-weights\"])\n\nmd(r\"\"\"\n**Result: reproduced.** At rates of 1/s and above the weights under the two models' certainties\ndiffer by at most 0.0010 (Methods' weight) and 0.0062 (notebook's weight), inside both bounds, and\nthe largest difference (0.021 and 0.130) falls at the lowest rate, 0.01/s.\n\"\"\")\n\nmd(r\"\"\"\n## fig3d-best-network-slow-decay\n\n> Across ring attractors with different bump decay speeds and baseline amplitudes, the best network\n> has a slow decay (low beta) and performs about as well as the Bayesian ring attractor; performance\n> drops as decay speed increases, which a larger baseline amplitude partly offsets.\n\"\"\")\n\ncode(r\"\"\"\nm3d = code.npz(\"figure3d.npz\")[\"MSE_array\"] / ref_pf\ni, j = np.unravel_index(np.nanargmax(m3d), m3d.shape)\nkb, bb = bra.KSTAR_3D[i], bra.BETA_GRID[j]\nbay = m3d[list(bra.KSTAR_3D).index(1.0), list(bra.BETA_GRID).index(0.5)]\nprint(\"normalized performance range %.4f to %.4f, NaN cells %d\" % (np.nanmin(m3d), np.nanmax(m3d), np.isnan(m3d).sum()))\nprint(\"best network: kappa* = %g, beta = %g, performance %.4f; Bayesian (1, 0.5): %.4f, %.2f%% below the best\"\n      % (kb, bb, m3d[i, j], bay, 100 * (m3d[i, j] - bay) / m3d[i, j]))\nabove = bra.BETA_GRID > bb\nbest_per_beta = np.nanmax(m3d, 0)\nkstar_per_beta = bra.KSTAR_3D[np.nanargmax(m3d, 0)]\nprint(pd.DataFrame(dict(beta=bra.BETA_GRID, max_over_kstar=best_per_beta, best_kstar=kstar_per_beta)).round(4).T.to_string())\nsteps = np.diff(best_per_beta[j:])\nc = {1: bb <= 1, 2: (kb, bb) != (1.0, 0.5), 3: (m3d[i, j] - bay) / m3d[i, j] <= 0.10,\n     4: bool(np.all(steps < 0)), 5: bool(np.all(kstar_per_beta[above] >= kb))}\nprint(\"conditions:\", c)\nprint(\"steps of the maximum for beta above the best:\", steps.round(4), \"; rises:\", int((steps > 0).sum()), \"of\", len(steps))\nrho = stats.spearmanr(bra.BETA_GRID[j:], best_per_beta[j:])\nprint(\"variant, not judged: Spearman rho of beta and the maximum, beta >= best: %.3f (p = %.2g); drop from beta %g to 8: %.4f\"\n      % (rho.statistic, rho.pvalue, bb, best_per_beta[j] - best_per_beta[-1]))\n\"\"\", tags=[\"claim:fig3d-best-network-slow-decay\"])\n\nmd(r\"\"\"\n**Result: partially reproduced.** The best network (kappa* = 0.7, beta = 0.3) decays slowly, differs\nfrom the Bayesian attractor's parameters, and the Bayesian attractor is 0.57% below it. Above the\nbest beta the kappa* that maximizes performance is always at least 0.7, rising to 1.5 or 1.6. The\nmaximum over kappa* falls overall from 1.0012 to 0.9322 (Spearman rho printed above), but not at\nevery step: it rises twice, by 0.0008 (beta 0.7 to 0.8) and 0.0013 (0.9 to 1), so condition (4)\nfails as written.\n\"\"\")\n\nmd(r\"\"\"\n## fig3f-noise-drop-below-70\n\n> In a network of 64 neurons with additive neural noise, inference accuracy drops below 70% of its\n> noise-free value once the noise is large enough.\n\"\"\")\n\ncode(r\"\"\"\ngrids = {s: code.npz(f\"figure3f/sigma={s}.npz\") for s in bra.SIGMAS_3F}\nM0 = grids[0.0][\"MSE_array\"] / bra.REF_PF_3F\nidx_ref = np.unravel_index(np.nanargmax(M0), M0.shape)\nprint(\"noise-free optimum: kappa* = %g, beta = %g\" % (bra.KSTAR_3F[idx_ref[0]], bra.BETA_GRID[idx_ref[1]]))\nrows = []\nfor s in bra.SIGMAS_3F:\n    M, act = grids[s][\"MSE_array\"] / bra.REF_PF_3F, grids[s][\"avg_network_activity\"]\n    idx = np.unravel_index(np.nanargmax(M), M.shape)\n    rows.append(dict(sigma=s, retuned_pf=100 * M[idx], untuned_pf=100 * M[idx_ref],\n                     retuned_self=100 * M[idx] / M0[idx_ref], untuned_self=100 * M[idx_ref] / M0[idx_ref],\n                     snr_retuned=act[idx] / s * np.sqrt(bra.N_3F / 2) if s else np.nan,\n                     snr_untuned=act[idx_ref] / s * np.sqrt(bra.N_3F / 2) if s else np.nan,\n                     best_kstar=bra.KSTAR_3F[idx[0]], best_beta=bra.BETA_GRID[idx[1]], nan_cells=int(np.isnan(M).sum())))\nf3f = pd.DataFrame(rows).set_index(\"sigma\")\nprint(f3f.round(3).to_string())\nfor norm_ in (\"pf\", \"self\"):\n    for smax in (10, 20):\n        v = f3f.loc[float(smax), \"untuned_\" + norm_]\n        print(\"normalization %-4s, largest SD %d: untuned performance %.2f%% -> below 70%%: %s\" % (norm_, smax, v, v < 70))\n\"\"\", tags=[\"claim:fig3f-noise-drop-below-70\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Without retuning, the network's relative performance at noise SD 10 is\n63.1% under both normalizations and at SD 20 it is 38.1%, below 70% under all four combinations.\n\"\"\")\n\nmd(r\"\"\"\n## fig3f-retuning-reduces-drop\n\n> Retuning the bump decay speed and baseline amplitude for each noise level reduces the drop in\n> inference accuracy by about 35% compared with the network tuned for noise-free performance, and\n> raises the signal-to-noise ratio.\n\nExpected: reduction of the drop 35 +/- 3.5%.\n\"\"\")\n\ncode(r\"\"\"\nred = {}\nfor norm_ in (\"pf\", \"self\"):\n    drop_r = 100 - f3f[\"retuned_\" + norm_]\n    drop_u = 100 - f3f[\"untuned_\" + norm_]\n    r_ = 100 * (1 - drop_r / drop_u)\n    red[(norm_, \"a: SD 10\")] = r_.loc[10.0]\n    red[(norm_, \"b: SD 20\")] = r_.loc[20.0]\n    red[(norm_, \"c: mean SD 1-10\")] = r_.loc[1.0:10.0].mean()\n    print(\"normalization\", norm_, \"reduction by SD:\", r_.round(2).to_dict())\nred = pd.Series(red)\nprint(\"\\nreadings of the 35%:\\n\", red.round(2).to_string())\nprint(\"readings within 31.5 to 38.5%:\", list(red[(red >= 31.5) & (red <= 38.5)].index))\nsnr_ok = bool(np.all(f3f.snr_retuned.iloc[1:] >= f3f.snr_untuned.iloc[1:]))\nprint(\"retuned S/N >= untuned at every SD > 0:\", snr_ok, \"; ratio range %.2f to %.2f\"\n      % ((f3f.snr_retuned / f3f.snr_untuned).iloc[1:].min(), (f3f.snr_retuned / f3f.snr_untuned).iloc[1:].max()))\nprint(\"Fig. S4, reported only: best kappa* by SD\", f3f.best_kstar.to_dict(), \"\\n best beta by SD\", f3f.best_beta.to_dict())\n\"\"\", tags=[\"claim:fig3f-retuning-reduces-drop\"])\n\nmd(r\"\"\"\n**Result: reproduced.** At noise SD 10 retuning reduces the drop by 34.6% (both normalizations),\ninside 31.5 to 38.5%; the other readings give 23.9% (mean over SD 1 to 10) and 29.7% (SD 20),\noutside the range. The retuned signal-to-noise ratio is above the untuned one at every noise level.\nFor Fig. S4, the best kappa* grows with the noise up to SD 10 (0.5 to 4.8), while the best beta\ndoes not grow steadily (0.1 to 2.0, then 0.4 and 0.1 at SD 15 and 20).\n\"\"\")\n\nmd(r\"\"\"\n## noise-effects-on-mu-and-kappa\n\n> Neural noise makes the bump position diffuse without bias and makes the bump amplitude drift\n> upward and diffuse, which leads to overconfidence; for additive noise, a four-fold larger network\n> halves the noise's effective SD.\n\n`RNN_filter_Run` at kappa* = 1, beta = 0.5, tau = 1 (w_even = 1.5, w_quad = 0.5), no inputs,\nstoch_corr = 0, from a bump of amplitude 1, 2,000 runs of T = 5, noise SD 1 and 2, N = 64 and 256.\nThe runs use a batched copy of the function (`bra.rnn_batch`), first checked against the released\nfunction on the same noise.\n\"\"\")\n\ncode(r\"\"\"\n# the batched copy against the released RNN_filter_Run, same noise draws\nnp.random.seed(3)\n_, mu_ref, k_ref = flt.RNN_filter_Run(0.5, N=16, dt=0.01, w_even=1.5, w_quad=0.5, tau=1, I_ext=0,\n                                      stoch_corr=0, phi_0=0, kappa_0=1, sigma_N=1.0)\nnp.random.seed(3)\nnoise = np.random.randn(50, 16)[:, None, :]\nmu_b, k_b = bra.rnn_batch(None, 1, 0.5, 16, 1.0, 1.5, 0.5, noise=noise)\nprint(\"batched vs released, max abs difference: position %.2e, amplitude %.2e\"\n      % (np.abs(mu_b[:, 0] - mu_ref).max(), np.abs(k_b[:, 0] - k_ref).max()))\n\nrng = np.random.default_rng(289)\nnoise_res, kmean_t = {}, {}\nfor N in (64, 256):\n    _, k0 = bra.rnn_batch(rng, 1, 5, N, 0.0, 1.5, 0.5)\n    for sig in (1.0, 2.0):\n        mu, k = bra.rnn_batch(rng, 2000, 5, N, sig, 1.5, 0.5)\n        dmu = bra.circ_diff(mu[-1], mu[0])\n        var_t = [np.var(bra.circ_diff(mu[int(t / 0.01) - 1], mu[0])) for t in (1, 2, 3, 4, 5)]\n        kmean_t[(N, sig)] = [k[int(t / 0.01) - 1].mean() for t in (0.1, 0.5, 1, 2, 3, 4, 5)]\n        noise_res[(N, sig)] = dict(mean_dmu=dmu.mean(), se=dmu.std(ddof=1) / np.sqrt(len(dmu)),\n                                   z=dmu.mean() / (dmu.std(ddof=1) / np.sqrt(len(dmu))),\n                                   var_t1_to_t5=np.round(var_t, 4), var_grows=bool(np.all(np.diff(var_t) > 0)),\n                                   amp_end=k[-1].mean(), amp_end_sd=k[-1].std(), amp_noise_free=k0[-1, 0],\n                                   inc_sd=np.diff(k, axis=0).std())\nnr = pd.DataFrame(noise_res).T\nprint(nr.to_string())\nprint(\"\\nmean amplitude at t = 0.1, 0.5, 1, 2, 3, 4, 5 s:\")\nfor key, v in kmean_t.items():\n    print(key, np.round(v, 3))\nratio = {sig: noise_res[(256, sig)][\"inc_sd\"] / noise_res[(64, sig)][\"inc_sd\"] for sig in (1.0, 2.0)}\nc1 = all(abs(v[\"z\"]) <= 2 and v[\"var_grows\"] for v in noise_res.values())\nc2 = all(v[\"amp_end\"] > v[\"amp_noise_free\"] for v in noise_res.values())\nc3 = all(0.45 <= r_ <= 0.55 for r_ in ratio.values())\nprint(\"\\n(1) unbiased and growing variance in all four:\", c1, [round(v[\"z\"], 2) for v in noise_res.values()])\nprint(\"(2) mean end amplitude above noise-free in all four:\", c2)\nprint(\"(3) increment SD ratio N=256/N=64:\", {k_: round(v, 4) for k_, v in ratio.items()}, c3)\n\"\"\", tags=[\"claim:noise-effects-on-mu-and-kappa\"])\n\nmd(r\"\"\"\n**Result: partially reproduced.** The batched network matches the released function to rounding\nerror. The position diffuses with a variance that grows at every second in all four settings, and\nits mean change is within 2 standard errors of 0 in three of them; at N = 256 with noise SD 2 it\nis -0.047 rad, 2.4 standard errors. The SD of the one-step amplitude increments at N = 256 is half\nthat at N = 64 (ratios 0.50 for both noise levels). But the mean amplitude does not drift upward:\nat the end it is below the noise-free value of 1.0 in all four settings (0.42 to 0.83), and it\nfalls throughout the run. In this network the noise also enters the rectified sum of the global\ninhibition, which grows with the noise, which may be why the network's amplitude falls where the SI\nderivation predicts a rise.\n\"\"\")\n\nmd(r\"\"\"\n## fig4b-connectome-motifs\n\n> The connectivity among EPG, Delta7 and PEN1 neurons in the hemibrain connectome resembles the\n> connectivity of a network that implements the approximate circular Kalman filter, with shifted\n> PEN1 to EPG projections and broad EPG to Delta7 to EPG inhibition.\n\nTotal synapse count per pair, from the public hemibrain v1.2 export (the paper used v1.2.1 in\nneuPrint, which now needs a personal token). Neurons are sorted by the PB glomerulus in their\nname, L9 to R9 (reading (a)); reading (b), by ellipsoid body or gall position in the name, cannot\nbe formed because no name holds that position. (1) For each PEN1 neuron, the synapse-weighted\ncircular mean position (period 8 glomeruli) of its EPG targets minus that of its EPG inputs, among\nEPG neurons on the same side of the bridge; the claim holds when the offsets of left and right\nPEN1 neurons have opposite signs. (2) The number of the 16 EPG glomeruli from which each Delta7\nreceives, and to which it sends, at least one synapse.\n\"\"\")\n\ncode(r\"\"\"\npos = {g: k for k, g in enumerate(bra.PB_ORDER)}\ncx[\"x\"] = cx.g.map(pos)\npre = cx[[\"bodyId\", \"t\", \"g\", \"x\"]].add_suffix(\"_pre\")\npost = cx[[\"bodyId\", \"t\", \"g\", \"x\"]].add_suffix(\"_post\")\ncc = conns.merge(pre, on=\"bodyId_pre\").merge(post, on=\"bodyId_post\")\n\ndef cmean(x, w):\n    return np.angle(np.sum(w * np.exp(2j * np.pi * x / 8)) / np.sum(w)) * 8 / (2 * np.pi)\n\nrows = []\nfor b, p in cx[cx.t == \"PEN1\"].set_index(\"bodyId\").iterrows():\n    side = p.g[0]\n    inp = cc[(cc.bodyId_post == b) & (cc.t_pre == \"EPG\")]\n    out = cc[(cc.bodyId_pre == b) & (cc.t_post == \"EPG\")]\n    for sel in (\"same side\", \"both sides\"):\n        i_ = inp[inp.g_pre.str[0] == side] if sel == \"same side\" else inp\n        o_ = out[out.g_post.str[0] == side] if sel == \"same side\" else out\n        off = (cmean(o_.x_post.values, o_.weight.values) - cmean(i_.x_pre.values, i_.weight.values) + 4) % 8 - 4\n        rows.append(dict(glomerulus=p.g, side=side, partners=sel, offset=off,\n                         syn_in=i_.weight.sum(), syn_out=o_.weight.sum()))\npen = pd.DataFrame(rows)\nprint(pen[pen.partners == \"same side\"].sort_values(\"glomerulus\", key=lambda s: s.map(pos)).round(3).to_string(index=False))\nsumm = pen.groupby([\"partners\", \"side\"]).offset.agg([\"mean\", \"median\", \"min\", \"max\", lambda s: int((s > 0).sum()), \"size\"])\nprint(summ.round(3).to_string())\nfor sel in (\"same side\", \"both sides\"):\n    L = pen[(pen.partners == sel) & (pen.side == \"L\")].offset\n    Rr = pen[(pen.partners == sel) & (pen.side == \"R\")].offset\n    print(\"%s: left mean %+.3f (Wilcoxon vs 0 p = %.3g), right mean %+.3f (p = %.3g); opposite signs: %s\"\n          % (sel, L.mean(), stats.wilcoxon(L).pvalue, Rr.mean(), stats.wilcoxon(Rr).pvalue, np.sign(L.mean()) != np.sign(Rr.mean())))\n\nrows = []\nfor b, p in cx[cx.t == \"Delta7\"].set_index(\"bodyId\").iterrows():\n    i_ = cc[(cc.bodyId_post == b) & (cc.t_pre == \"EPG\")].groupby(\"g_pre\").weight.sum()\n    o_ = cc[(cc.bodyId_pre == b) & (cc.t_post == \"EPG\")].groupby(\"g_post\").weight.sum()\n    rows.append({\"instance\": p.instance, **{f\"in>={th}\": int((i_ >= th).sum()) for th in (1, 3, 5)},\n                 **{f\"out>={th}\": int((o_ >= th).sum()) for th in (1, 3, 5)}, \"syn_in\": i_.sum(), \"syn_out\": o_.sum()})\nd7 = pd.DataFrame(rows)\nprint(\"\\nEPG glomeruli (of 16) connected to each Delta7, by minimum synapse count per glomerulus:\")\nprint(d7.describe().loc[[\"min\", \"50%\", \"max\"]].round(1).to_string())\nfor th in (1, 3, 5):\n    print(\"threshold %d synapse(s): Delta7 with more than 8 input glomeruli %d of %d, more than 8 output glomeruli %d of %d\"\n          % (th, (d7[f\"in>={th}\"] > 8).sum(), len(d7), (d7[f\"out>={th}\"] > 8).sum(), len(d7)))\n\"\"\", tags=[\"claim:fig4b-connectome-motifs\"])\n\nmd(r\"\"\"\n**Result: reproduced, under the one sort the names allow (reading (a)) and with any synapse\ncounted.** Left PEN1 neurons send their EPG output a mean of +0.56 glomeruli from their EPG input\n(9 of 10 positive) and right ones -0.48 (9 of 10 negative), opposite directions, both different from\n0 (Wilcoxon, printed above); with partners from both sides, +0.37 and -0.35. Every Delta7 receives EPG\ninput from at least 13 of the 16 glomeruli and sends output to EPG neurons in at least 9. The output\nside depends on the threshold: counting only glomeruli with at least 3 or 5 synapses, Delta7\noutputs reach fewer than half the glomeruli (printed above).\n\"\"\")\n\nmd(r\"\"\"\n## fig4gh-drosophila-network-matches\n\n> A Drosophila-like multipopulation network, constrained by the connectome, tracks HD with an\n> accuracy indistinguishable from the idealized Bayesian ring attractor across observation\n> reliabilities.\n\"\"\")\n\ncode(r\"\"\"\ng4 = code.npz(\"figure4g.npz\")\ncxa, bqa = g4[\"CX_stats\"][:, 1], g4[\"vonMises_q_stats\"][:, 1]\nd4 = np.abs(cxa - bqa)\nprint(pd.DataFrame(dict(rate=R, drosophila=cxa, bayes=bqa, abs_diff=d4,\n                        cert_drosophila=g4[\"CX_stats\"][:, 2], cert_bayes=g4[\"vonMises_q_stats\"][:, 2])).round(4).to_string(index=False))\nfor bound in (0.01, 0.02):\n    print(\"max |diff| %.4f; within %.2f at every rate: %s; rates outside: %s\"\n          % (d4.max(), bound, bool(np.all(d4 <= bound)), R[d4 > bound].tolist()))\n\"\"\", tags=[\"claim:fig4gh-drosophila-network-matches\"])\n\nmd(r\"\"\"\n**Result: partially reproduced.** The Drosophila-like network's accuracy is within 0.02 of the\nBayesian ring attractor's at every rate (largest 0.019, at 0.1/s), but not within 0.01: it differs\nby 0.019, 0.014 and 0.010 at 0.1, 0.2 and 0.3/s. Since the criterion requires both readings, the\nclaim holds in part.\n\"\"\")\n\nmd(r\"\"\"\n## figs2-performance-independent-of-n\n\n> The Bayesian ring attractor's inference accuracy depends little on its number of neurons.\n\"\"\")\n\ncode(r\"\"\"\ns2 = code.npz(\"figureS2.npz\")[\"MSE_array\"]\nref2 = code.npz(\"vonMises_q_stats.npz\")[\"stats\"][:, 1]\nprint(\"vonMises_q_stats.npz equals the attractor's accuracy in figure2i.npz:\", np.allclose(ref2, accB))\ndev = pd.DataFrame(np.abs(s2 - ref2), index=bra.N_S2, columns=R)\nprint(\"missing values (NaN) per N:\", dict(zip(bra.N_S2.tolist(), np.isnan(s2).sum(1).tolist())))\nprint(\"max |diff| per N:\", dev.max(1).round(4).to_dict())\nprint(\"cells above 0.02:\", [(int(n), float(r)) for n in dev.index for r in dev.columns if dev.loc[n, r] > 0.02])\nfor nmin in (8, 16):\n    sub = dev.loc[dev.index >= nmin]\n    print(\"N >= %d: max |diff| %.4f, within 0.02 at every rate: %s\" % (nmin, np.nanmax(sub.values), bool(np.nanmax(sub.values) <= 0.02)))\nprint(\"N = 3 and 4, reported: max |diff| %.4f and %.4f\" % (dev.loc[3].max(), dev.loc[4].max()))\n\"\"\", tags=[\"claim:figs2-performance-independent-of-n\"])\n\nmd(r\"\"\"\n**Result: partially reproduced.** Of the 7 x 23 values, one is more than 0.02 from the reference:\nN = 16 at 0.1/s, 0.041 below it. All others, N = 3 and 4 included, are within 0.019. Both readings\n(N of 8 and more, N of 16 and more) include N = 16, so neither holds as written, although the\naccuracy is close to the reference at every other network size and rate. One value (N = 128 at\n100/s) is missing in the stored array.\n\"\"\")\n\nmd(r\"\"\"\n## prediction-bump-amplitude-cue-reliability\n\n> The paper predicts that the bump amplitude in the HD system is higher in the presence of reliable\n> external HD cues, such as salient visual landmarks. The paper does not test this.\n\nBump amplitude is the length of the population vector at the bump's spatial frequency across the\nPB midline ROIs (two bump copies across the bridge, frequency 2, the peak of every fly's spatial\nspectrum), scaled by 2/n as in the paper's code. More reliable cue = high contrast, less reliable =\nlow contrast, as the trials table labels them. Per fly, the mean amplitude over all frames of each\ncontrast. Signal (i) is the stored dF/F. Signal (ii) is raw fluorescence minus baseline: the\nTwoPhotonSeries averaged over planes, smoothed in the plane (Gaussian SD 4 pixels) and averaged in\neach ROI mask, minus each ROI's 10th percentile over the session, read in blocks of 25 volumes every\n250 (10% of the frames, about 0.9 GB per fly). The projection and smoothing were chosen by their\nagreement with the stored dF/F, shown first.\n\"\"\")\n\ncode(r\"\"\"\nprint(\"spatial frequency of the peak of the dF/F spectrum, per fly:\",\n      [int(bra.spectrum(s[\"dff\"]).argmax()) for s in sessions])\n# which projection reproduces the stored dF/F? sub-1, 10 blocks of 25 volumes\ns1 = sessions[0]\nf1 = bra.open_nwb(contrast_assets[0])\nblocks = [(a, a + 25) for a in range(0, 2500, 250)]\nidx = np.concatenate([np.arange(a, b) for a, b in blocks])\nfor proj, sm in [(\"mean\", 0), (\"max\", 0), (\"mean\", 2), (\"mean\", 4), (\"max\", 4)]:\n    F = bra.raw_roi_fluorescence(f1, blocks, s1[\"masks\"], proj, sm)\n    r_ = [np.corrcoef(F[:, j], s1[\"dff\"][idx, j])[0, 1] for j in range(F.shape[1])]\n    print(\"projection %-4s smoothing %d px: median correlation with stored dF/F over ROIs %.3f (min %.3f)\"\n          % (proj, sm, np.median(r_), np.min(r_)))\n\"\"\", tags=[\"claim:prediction-bump-amplitude-cue-reliability\"])\n\ncode(r\"\"\"\ndef amplitude_by_contrast(s, act, t):\n    _, amp = bra.fourier(act)\n    out = {}\n    for c in (1, 2, 3):\n        m = np.zeros(len(t), bool)\n        for a, b, l in zip(s[\"trials\"][\"start_time\"], s[\"trials\"][\"stop_time\"], s[\"trials\"][\"cue_contrast\"]):\n            if l == c:\n                m |= (t >= a) & (t < b)\n        out[c] = amp[m].mean()\n    return out\n\ndef raw_signal(a, s):\n    f = bra.open_nwb(a)\n    n = s[\"tps_shape\"][0]\n    blocks = [(i, min(i + 25, n)) for i in range(0, n, 250)]\n    F = bra.raw_roi_fluorescence(f, blocks, s[\"masks\"], \"mean\", 4.0)\n    t = s[\"t\"][np.concatenate([np.arange(i, j) for i, j in blocks])]\n    return F - np.percentile(F, 10, axis=0), t\n\nt1 = time.time()\nwith ThreadPoolExecutor(4) as ex:\n    raws = list(ex.map(raw_signal, contrast_assets, sessions))\nprint(\"raw fluorescence read in %.0f s\" % (time.time() - t1))\nrows = []\nfor s, (F, tF) in zip(sessions, raws):\n    a_d = amplitude_by_contrast(s, s[\"dff\"], s[\"t\"])\n    a_r = amplitude_by_contrast(s, F, tF)\n    rows.append(dict(fly=s[\"subject\"], dff_zero=a_d[1], dff_low=a_d[2], dff_high=a_d[3],\n                     raw_zero=a_r[1], raw_low=a_r[2], raw_high=a_r[3]))\namp = pd.DataFrame(rows).set_index(\"fly\")\nprint(amp.round(3).to_string())\npred = {}\nfor sig in (\"dff\", \"raw\"):\n    hi, lo, ze = amp[sig + \"_high\"], amp[sig + \"_low\"], amp[sig + \"_zero\"]\n    n_hi = int((hi > lo).sum())\n    w = stats.wilcoxon(hi, lo, alternative=\"greater\")\n    pred[(sig, \"a\")] = n_hi > len(amp) / 2\n    pred[(sig, \"b\")] = w.pvalue < 0.05\n    print(\"\\n%s: high > low in %d of %d flies; median high/low ratio %.3f; median difference %.3f; one-sided Wilcoxon W = %g, p = %.4f\"\n          % (sig, n_hi, len(amp), np.median(hi / lo), np.median(hi - lo), w.statistic, w.pvalue))\n    w0 = stats.wilcoxon(hi, ze, alternative=\"greater\")\n    print(\"   variant, high against zero contrast: %d of %d flies higher, median ratio %.3f, p = %.4f\"\n          % (int((hi > ze).sum()), len(amp), np.median(hi / ze), w0.pvalue))\n    w1 = stats.wilcoxon(lo, ze, alternative=\"greater\")\n    print(\"   variant, low against zero contrast: %d of %d flies higher, p = %.4f\" % (int((lo > ze).sum()), len(amp), w1.pvalue))\n    print(\"   without sub-2 (one high block): high > low in %d of 14, p = %.4f\"\n          % (int((hi.drop(\"2\") > lo.drop(\"2\")).sum()), stats.wilcoxon(hi.drop(\"2\"), lo.drop(\"2\"), alternative=\"greater\").pvalue))\nprint(\"\\nreadings:\", pred)\n\"\"\", tags=[\"claim:prediction-bump-amplitude-cue-reliability\"])\n\nmd(r\"\"\"\n**Result: blocked (methods_underspecified).** The readings disagree (printed above): under reading\n(a), the per-fly majority, bump amplitude is higher at high than at low contrast in most flies\nwith both signals, but the one-sided Wilcoxon test over the 15 flies (reading (b)) does not reach\np < 0.05 with either signal. The criterion blocks the claim when its readings differ. High against\nzero contrast, a variant, is shown above.\n\"\"\")\n\nmd(r\"\"\"\n## Summary\n\n| Claim | Outcome |\n|---|---|\n| fig1-conflict-decreases-certainty | reproduced |\n| fig2h-bump-tracks-circkf | reproduced |\n| fig2i-accuracy-and-certainty-vs-reliability | reproduced |\n| fig3b-bayesian-beats-conventional | reproduced |\n| fig3c-update-weights | reproduced |\n| fig3d-best-network-slow-decay | partially reproduced |\n| fig3f-noise-drop-below-70 | reproduced |\n| fig3f-retuning-reduces-drop | reproduced (34.6%) |\n| noise-effects-on-mu-and-kappa | partially reproduced |\n| fig4b-connectome-motifs | reproduced, assumed (one sort, any synapse) |\n| fig4gh-drosophila-network-matches | partially reproduced |\n| figs2-performance-independent-of-n | partially reproduced |\n| prediction-bump-amplitude-cue-reliability | blocked, methods underspecified |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning\nand the differences from the paper's method.\n\n**How the analysis differs from the paper's.** Twelve claims are tested on the paper's own released\noutputs and code, not on the dandiset, as the claims file sets out. The scan scripts were not\nre-run (10,000 trajectories per setting is beyond the time limit). The noise test uses a batched\ncopy of `RNN_filter_Run`, checked against it. The connectome is the public v1.2 export, not\nv1.2.1 in neuPrint, and only the PB-glomerulus sort can be formed from its names. The prediction is\ntested on the dandiset's cue-contrast experiment, from a different study; the raw-fluorescence signal\nis read on 10% of the frames.\n\n**What was found about the dataset.** The dandiset holds no data of this paper, which is a theory\npaper; its related resources point to a bioRxiv preprint of this paper (version 4) for a study whose\ndata it holds (Basnak et al., in preparation). In the cue-contrast experiment, `imaging_rate` says\n9.18 Hz for every file, while sub-4 and sub-10 are imaged at 7.87 Hz (0.127 s frames, 14 planes);\nsub-2 has one high-contrast block, not two, and a last block of 405 s labelled low contrast. The\nROI masks are 5 to 9 pixels on the PB midline, and the stored dF/F agrees with the raw imaging\nonly after spatial smoothing, which the files do not describe.\n\"\"\")\n\ncode(r\"\"\"\nprint(\"notebook ran in %.1f min\" % ((time.time() - started) / 60))\n\"\"\")\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbf.write(nb, \"entries/000289-kutschireiter-2023/reproduce_kutschireiter_2023.ipynb\")\nprint(\"written\", len(cells))\n"
}
```

```
File created successfully at: /tmp/claude-1001/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/000289-kutschireiter-2023; cat > requirements.in <<'EOF'
h5py
matplotlib
numpy
pandas
remfile
requests
scipy
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: 000289-kutschireiter-2023
type: reproduction
title: Bayesian inference in ring attractor networks (Kutschireiter et al. 2023)
description: Tests the findings of Kutschireiter, Basnak, Wilson and Drugowitsch (2023), a theory
  paper. Its simulation findings are tested on the paper's released code and processed outputs
  (Zenodo), its connectome finding on the hemibrain connectome, and its prediction that bump
  amplitude is higher with a reliable cue on dandiset 000289, which holds two-photon imaging of EPG
  neurons in flies shown a visual cue at three contrasts, from a separate study by the same lab.
license: Apache-2.0
notebooks:
- path: reproduce_kutschireiter_2023.ipynb
  title: Testing Kutschireiter et al. (2023) with dandiset 000289
  runtime_minutes: 8
helpers:
- bra.py
related:
- id: dandi:000289/0.240801.1040
  relation: uses_data
- id: doi:10.1073/pnas.2210622120
  relation: reproduces
EOF
. $TMPDIR/venv/bin/activate; uv pip install -q nbconvert ipykernel nbformat 2>&1|tail -1; python $TMPDIR/build_nb.py; date -u; time jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 --output $TMPDIR/run1.ipynb reproduce_kutschireiter_2023.ipynb 2>&1 | tail -5
```

```
written 53
Thu Oct 29 23:32:09 UTC 2026
[NbConvertApp] Converting notebook reproduce_kutschireiter_2023.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 95318 bytes to /tmp/claude-1001/run1.ipynb

real	9m2.014s
user	2m26.147s
sys	0m16.604s
```

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; python - <<'EOF'
import json
nb=json.load(open('run1.ipynb'))
for c in nb['cells']:
    if c['cell_type']!='code': continue
    tags=c['metadata'].get('tags',[])
    out=''
    for o in c.get('outputs',[]):
        if 'text' in o: out+=''.join(o['text'])
        elif o.get('output_type')=='error': out+='ERROR '+o['ename']+o['evalue']
        elif 'data' in o and 'text/plain' in o['data']: out+=''.join(o['data']['text/plain'])
    print('=====',tags); print(out[-6000:])
EOF
```

```
===== []
Zenodo deposit doi:10.5281/zenodo.7615975, files: 49
Figure2a,c_FigureS1.ipynb
Figure2h.ipynb
Figure2i.ipynb
Figure3b,c,e,d_FigureS3.ipynb
Figure3f_FigureS4.ipynb
Figure4g,h.ipynb
FigureS2.ipynb
circularFiltering.py
data_processed/figure2i.npz
data_processed/figure3d.npz
data_processed/figure3f/sigma=0.0.npz
data_processed/figure3f/sigma=1.0.npz
data_processed/figure3f/sigma=10.0.npz
data_processed/figure3f/sigma=15.0.npz
data_processed/figure3f/sigma=2.0.npz
data_processed/figure3f/sigma=20.0.npz
data_processed/figure3f/sigma=3.0.npz
data_processed/figure3f/sigma=4.0.npz
[... 362 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR; python3 - <<'EOF'
p='build_nb.py'; s=open(p).read()
old_noise=s[s.index('**Result: partially reproduced.** The batched network'):s.index('derivation predicts a rise.')+len('derivation predicts a rise.')]
new_noise='''**Result: partially reproduced.** The batched network matches the released function to rounding
error. The position diffuses without bias: its mean change is within 2 standard errors of 0 in all
four settings (z = -0.74 to 0.82) and its variance grows at every second. The SD of the one-step
amplitude increments at N = 256 is half that at N = 64 (ratios 0.500 and 0.501). But the mean
amplitude does not drift upward: it falls throughout the run and ends below the noise-free value of
1.0 in all four settings (0.42 to 0.83), so condition (2) fails. In this network the noise also
enters the rectified sum that drives the global inhibition, which may be why the amplitude falls
where the SI derivation predicts a rise; this is not tested here.'''
s=s.replace(old_noise,new_noise)
old_ret=s[s.index('**Result: reproduced.** At noise SD 10 retuning'):s.index('then 0.4 and 0.1 at SD 15 and 20).')+len('then 0.4 and 0.1 at SD 15 and 20).')]
new_ret='''**Result: reproduced.** At noise SD 10 retuning reduces the drop by 34.6% under both
normalizations, and the mean over SD 1 to 10 is 31.7% with the particle filter normalization, all
inside 31.5 to 38.5%; the other readings give 31.2% (mean, legend normalization) and 29.8% (SD 20),
outside it. The retuned signal-to-noise ratio is above the untuned one at every noise level (ratio
1.05 to 3.00). For Fig. S4, reported only: the best kappa* grows with the noise from SD 1 to 10 (0.3
to 4.8), while the best beta does not grow steadily (0.1 to 2.0, then 0.4 and 0.1 at SD 15 and 20).'''
s=s.replace(old_ret,new_ret)
s=s.replace('dev.max(1).round(4)','dev.max(axis=1).round(4)')
s=s.replace('''The bump phase locks to the cue position at high contrast and not in darkness, and the coupling
peaks within a few frames of lag 0 (printed per fly), so the dF/F and the cue position share a
clock.''','''The bump phase locks to the cue position at high contrast (median coherence 0.79) and barely in
darkness (0.13), and in every fly the coupling peaks at lag 0 or 5 frames (0 to 0.55 s), the
lags closest to 0 that were tested, so the dF/F and the cue position share a clock.''')
s=s.replace('''which is consistent with the trials table being on the same
clock.''','''(median 0.79 against 0.39, 12 of 15 flies), which is consistent with the trials table being on
the same clock.''')
old_pred=s[s.index('**Result: blocked (methods_underspecified).**'):s.index('zero contrast, a variant, is shown above.')+len('zero contrast, a variant, is shown above.')]
new_pred='''**Result: blocked (methods_underspecified).** The readings disagree. Bump amplitude is higher at
high than at low contrast in 10 of 15 flies with dF/F and in 12 of 15 with raw fluorescence minus
baseline, so reading (a) holds for both signals. The one-sided Wilcoxon test over flies (reading
(b)) gives p = 0.021 with raw fluorescence but p = 0.138 with dF/F (median high/low ratio 1.12 and
1.11). The criterion blocks the claim when its readings differ. Variants: against zero contrast, the
high-contrast amplitude is higher in 12 (dF/F, p = 0.047) and 13 of 15 flies (raw, p = 0.006); low
contrast is not above zero contrast (7 of 15 flies with either signal).'''
s=s.replace(old_pred,new_pred)
s=s.replace('''The ROI masks are 5 to 9 pixels on the PB midline, and the stored dF/F agrees with the raw imaging
only after spatial smoothing, which the files do not describe.''','''The ROI masks are a few pixels each on the PB midline, and the stored dF/F agrees with the raw
imaging averaged in those masks only after spatial smoothing (median correlation 0.66 without, 0.93
with a 4-pixel Gaussian), which the files do not describe. The cue position and dF/F share a clock
(the bump phase follows the cue with a peak at lag 0 to 5 frames).

**Question for the paper's authors.** The prediction gives no experimental method: which activity
signal, which comparison of cue conditions and which test would test it. With this dandiset the
answer depends on the choice.''')
open(p,'w').write(s)
EOF
grep -c "Result:" build_nb.py
```

```
Thu Oct 29 23:41:40 UTC 2026
13
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
p='build_nb.py'; s=open(p).read()
old="All sources are read into memory; nothing is downloaded to disk."
new="""The dandiset's other 206 files (subjects 16 to 68) hold other experiments of that study: a cue
rotating in open loop, a cue of inverted gain, visual and wind cues in closed loop, and cues shifted
every 5 minutes (from the session descriptions and trial tables, read file by file while preparing
this attempt). No claim uses them.

All sources are read into memory; nothing is downloaded to disk."""
assert old in s; s=s.replace(old,new,1); open(p,'w').write(s)
EOF
. venv/bin/activate; python build_nb.py; cd  python tools/entry.py lock entries/000289-kutschireiter-2023 2>&1 | tail -3; python tools/entry.py check entries/000289-kutschireiter-2023 2>&1 | tail -10
```

```
written 53
  File "tools/entry.py", line 55, in <module>
    import yaml
ModuleNotFoundError: No module named 'yaml'
Traceback (most recent call last):
  File "tools/entry.py", line 55, in <module>
    import yaml
ModuleNotFoundError: No module named 'yaml'
```

**Agent calls Bash**

```bash
cd  . $TMPDIR/venv/bin/activate; uv pip install -q pyyaml jsonschema nbformat 2>&1|tail -1; python tools/entry.py lock entries/000289-kutschireiter-2023 2>&1 | tail -3; python tools/entry.py check entries/000289-kutschireiter-2023 2>&1 | tail -10
```

```
wrote entries/000289-kutschireiter-2023/requirements.lock.txt
0 error(s)
```

**Agent calls Bash**

```bash
cd  . $TMPDIR/venv/bin/activate; date -u; time python tools/entry.py all entries/000289-kutschireiter-2023 2>&1 | tail -15; date -u
```

```
Thu Oct 29 23:41:53 UTC 2026
Installed kernelspec registry-000289-kutschireiter-2023 in executed/000289-kutschireiter-2023/.venv/share/jupyter/kernels/registry-000289-kutschireiter-2023
0 error(s)
pass  reproduce_kutschireiter_2023.ipynb  (514 s)

real	8m39.593s
user	2m27.999s
sys	0m16.370s
Thu Oct 29 23:50:32 UTC 2026
```

**Agent calls Bash**

```bash
cd  ls executed/000289-kutschireiter-2023/; python3 - <<'EOF'
import json,glob
p=glob.glob('executed/000289-kutschireiter-2023/*.ipynb')[0]
nb=json.load(open(p))
for c in nb['cells']:
    if c['cell_type']!='code': continue
    tags=c['metadata'].get('tags',[])
    out=''.join(''.join(o.get('text','')) for o in c.get('outputs',[]))
    if any(t.startswith('claim:noise') or t.startswith('claim:pred') or t.startswith('claim:fig3f-ret') for t in tags) or (tags==['sanity'] and 'coherence' in out):
        print(tags, out[-1500:])
EOF
```

```
reproduce_kutschireiter_2023.ipynb
result.json
['sanity'] zero contrast, phase-cue coherence by lag (frames): {-30: np.float64(0.078), -25: np.float64(0.084), -20: np.float64(0.093), -15: np.float64(0.103), -10: np.float64(0.106), -5: np.float64(0.116), 0: np.float64(0.13), 5: np.float64(0.124), 10: np.float64(0.112), 15: np.float64(0.115), 20: np.float64(0.102), 25: np.float64(0.104), 30: np.float64(0.104)}
low  contrast, phase-cue coherence by lag (frames): {-30: np.float64(0.375), -25: np.float64(0.38), -20: np.float64(0.396), -15: np.float64(0.42), -10: np.float64(0.436), -5: np.float64(0.463), 0: np.float64(0.533), 5: np.float64(0.532), 10: np.float64(0.483), 15: np.float64(0.457), 20: np.float64(0.442), 25: np.float64(0.428), 30: np.float64(0.403)}
high contrast, phase-cue coherence by lag (frames): {-30: np.float64(0.513), -25: np.float64(0.538), -20: np.float64(0.568), -15: np.float64(0.602), -10: np.float64(0.658), -5: np.float64(0.714), 0: np.float64(0.79), 5: np.float64(0.762), 10: np.float64(0.694), 15: np.float64(0.659), 20: np.float64(0.621), 25: np.float64(0.577), 30: np.float64(0.542)}
lag of peak coherence in high contrast, per fly (frames): [np.int64(0), np.int64(5), np.int64(0), np.int64(0), np.int64(0), np.int64(5), np.int64(5), np.int64(0), np.int64(0), np.int64(5), np.int64(0), np.int64(5), np.int64(5), np.int64(5), np.int64(0)]
median coherence in frames labelled high contrast: true labels 0.790, labels shifted one block 0.390
flies where the true labels give the higher coherence: 12 of 15

['claim:fig3f-retuning-reduces-drop'] normalization pf reduction by SD: {0.0: 0.0, 1.0: 34.35, 2.0: 16.4, 3.0: 30.37, 4.0: 33.05, 5.0: 33.2, 6.0: 33.12, 7.0: 33.86, 8.0: 34.28, 9.0: 33.46, 10.0: 34.64, 15.0: 32.25, 20.0: 29.8}
normalization self reduction by SD: {0.0: nan, 1.0: 31.33, 2.0: 15.91, 3.0: 30.0, 4.0: 32.8, 5.0: 33.02, 6.0: 32.99, 7.0: 33.75, 8.0: 34.19, 9.0: 33.38, 10.0: 34.56, 15.0: 32.2, 20.0: 29.76}

readings of the 35%:
 pf    a: SD 10      
[... 57 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/000289-kutschireiter-2023/README.md",
 "content": "# Kutschireiter, Basnak, Wilson & Drugowitsch (2023) with dandiset 000289\n\nTests the findings of [Kutschireiter et al. (2023)](https://doi.org/10.1073/pnas.2210622120),\n\"Bayesian inference in ring attractor networks\", a theory paper. The dandiset it is linked to,\n[DANDI:000289](https://dandiarchive.org/dandiset/000289/0.240801.1040), holds two-photon imaging of\nEPG neurons from a separate study of the same lab (Basnak et al.), which this paper does not analyse.\n\n- Twelve claims are simulation or connectome results. They are tested on the paper's released code\n  and processed outputs ([Zenodo 7615975](https://doi.org/10.5281/zenodo.7615975)) and on the public\n  hemibrain v1.2 connectome export, not on the dandiset.\n- One claim, the Discussion's prediction that bump amplitude is higher with a reliable cue, is\n  tested on the dandiset's cue-contrast experiment (15 flies, visual cue at zero, low and high\n  contrast).\n\n| Claim | Outcome |\n|---|---|\n| A conflicting HD observation lowers the circKF's certainty, a confirming one raises it | Reproduced |\n| An 80-neuron Bayesian ring attractor tracks the circKF, and its amplitude decays in darkness | Reproduced |\n| The attractor matches the circKF's accuracy for reliable cues, not for unreliable ones | Reproduced |\n| The Bayesian attractor beats the optimized conventional one at every reliability | Reproduced |\n| The attractor's update weights are close to the circKF's | Reproduced |\n| The best network decays slowly; performance falls with decay speed | Partially reproduced |\n| Neural noise drops accuracy below 70% without retuning | Reproduced |\n| Retuning reduces the drop by about 35% | Reproduced |\n| Neural noise: unbiased position diffusion, upward amplitude drift, 1/sqrt(N) scaling | Partially reproduced |\n| Connectome motifs: shifted PEN1 projections, broad Delta7 inhibition | Reproduced (assumed) |\n| The Drosophila-like network matches the Bayesian attractor | Partially reproduced |\n| Accuracy depends little on the number of neurons | Partially reproduced |\n| Prediction: higher bump amplitude with a reliable cue (dandiset) | Blocked: methods underspecified |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe attempt record, with the reasons and the differences from the paper's method, is\n[`attempts/000289-kutschireiter-2023-01.yaml`](../../attempts/000289-kutschireiter-2023-01.yaml).\n\n- `reproduce_kutschireiter_2023.ipynb`: the analysis. It takes about nine minutes, most of it\n  streaming 10% of the raw imaging of 15 sessions.\n- `bra.py`: loading the paper's Zenodo deposit in memory (with the two patches its code needs), the\n  hemibrain export, and the dandiset's sessions; the bump decoder; a batched copy of the paper's\n  single-population network.\n"
}
```

```
File created successfully at: entries/000289-kutschireiter-2023/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "attempts/000289-kutschireiter-2023-01.yaml",
 "content": "schema_version: 2\nid: 000289-kutschireiter-2023-01\ndataset:\n  archive: dandi\n  id: \"000289\"\n  version: 0.240801.1040\n  doi: 10.48324/dandi.000289/0.240801.1040\npaper: doi:10.1073/pnas.2210622120\ndate: 2026-10-29\nentry: 000289-kutschireiter-2023\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-12\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/40969113892\ninputs:\n- what: >-\n    The paper's code and processed simulation outputs (circularFiltering.py, the figure notebooks,\n    data_processed/*.npz), read into memory from the deposit zip (md5\n    c3f0574b98eef0c6c67d139f0d20a1ae). Used for every claim except the prediction.\n  source: >-\n    doi:10.5281/zenodo.7615975 (DrugowitschLab/BayesianRingAttractor v1.0, GitHub tag v1.0, commit\n    a9db6f9)\n- what: >-\n    Hemibrain connectome, traced neurons (bodyId, type, instance) and total synapse counts per\n    neuron pair, version 1.2 export (md5 ec1e076d15442f368fa5978b00f4a61c, dated 2020-12-22). Used\n    for fig4b-connectome-motifs.\n  source: >-\n    https://storage.googleapis.com/hemibrain/v1.2/exported-traced-adjacencies-v1.2.tar.gz (Scheffer\n    et al. 2020, doi:10.7554/eLife.57443)\noutcomes:\n- claim: fig1-conflict-decreases-certainty\n  outcome: reproduced\n  notebook: reproduce_kutschireiter_2023.ipynb\n  output: claim:fig1-conflict-decreases-certainty\n  notes: >-\n    With the code's vM_Projection (kappa_phi 1, kappa_v 1, dt 0.01), for kappa_t 1, 2 and 5 and\n    per-step reliabilities 0.1416 (gamma_z 1/s) and 0.4529 (10/s), a confirmatory observation raises\n    and an opposite one lowers the certainty in all 6 cases, both for the observation update alone\n    (for example kappa_t 1, 10/s, 1.453 and 0.547) and for the full step against the step without\n    observation (1.447 and 0.546 against 0.997).\n- claim: fig2h-bump-tracks-circkf\n  outcome: reproduced\n  notebook: reproduce_kutschireiter_2023.ipynb\n  output: claim:fig2h-bump-tracks-circkf\n  notes: >-\n    The simulation cells of Figure2h.ipynb were run from the deposit. With rate 15 (notebook) and 10/s\n    (Methods), the network's position differs from the circKF's by a mean of 0.016 and 0.021 rad,\n    against a circKF error to the true HD of 0.483 and 0.491 rad. Bump amplitude and circKF certainty\n    correlate at r 0.994 and 0.993 over the cue periods. In darkness (5 to 10 s) the amplitude falls\n    from 7.21 to 1.22 (rate 15) and from 5.89 to 1.21 (rate 10), closer to the baseline of 1 than at\n    its start.\n  deviations:\n  - >-\n    The notebook calls vM_Projection_Run with the keyword kappa_y, which the function names kappa_v;\n    the keyword was renamed (claims file header). Nothing else in the cells was changed except the\n    rate for the second reading.\n- claim: fig2i-accuracy-and-certainty-vs-reliability\n  outcome: reproduced\n  notebook: reproduce_kutschireiter_2023.ipynb\n  output: claim:fig2i-accuracy-and-certainty-vs-reliability\n  notes: >-\n    From figure2i.npz, the accuracies of the circKF and the Bayesian ring attractor differ by at most\n    0.0010 at rates of 1/s and above and 0.0003 at 3/s and above, so all four combinations hold. At\n    0.01, 0.03 and 0.1/s the attractor is less accurate (by 0.073, 0.084 and 0.057) and its mean\n    certainty is higher (1.00 to 1.05 against 0.18 to 0.56).\n- claim: fig3b-bayesian-beats-conventional\n  outcome: reproduced\n  notebook: reproduce_kutschireiter_2023.ipynb\n  output: claim:fig3b-bayesian-beats-conventional\n  notes: >-\n    The optimal kappa* of the fixed-certainty filter is 1.7 (weighted accuracy 0.626 against 0.687\n    for the Bayesian attractor). The Bayesian attractor is more accurate at all 23 rates (smallest\n    difference 0.0115 at 0.01/s, largest 0.131 at 100/s) and strictly so from 0.1 to 10/s (smallest\n    0.034). The reported part, not judged, holds only in part. The difference is smallest at 0.01/s,\n    but at 0.03/s (0.036) it is larger than at 2 and 3/s (0.034 and 0.035).\n- claim: fig3c-update-weights\n  outcome: reproduced\n  notebook: reproduce_kutschireiter_2023.ipynb\n  output: claim:fig3c-update-weights\n  notes: >-\n    At rates of 1/s and above, the weights computed with the circKF's and the attractor's mean\n    certainty differ by at most 0.0010 with the Methods' weight (dt 0.01) and 0.0062 with the\n    notebook's weight (dt 0.1), inside both bounds (0.02, 0.05). The largest difference, 0.021 and\n    0.130, falls at the lowest rate, 0.01/s.\n- claim: fig3d-best-network-slow-decay\n  outcome: partially_reproduced\n  notebook: reproduce_kutschireiter_2023.ipynb\n  output: claim:fig3d-best-network-slow-decay\n  notes: >-\n    Normalized by the particle filter reference, the best network is kappa* 0.7, beta 0.3\n    (1.0012). Conditions 1, 2, 3 and 5 hold. The best beta is at most 1, the best network differs\n    from (1, 0.5), the Bayesian attractor is 0.57% below the best, and above the best beta the\n    maximizing kappa* is 0.8 to 1.6, never below 0.7. Condition 4 fails as written. The maximum over\n    kappa* falls from 1.0012 (beta 0.3) to 0.9322 (beta 8), Spearman rho -0.98, but rises twice, by\n    0.0008 (beta 0.7 to 0.8) and 0.0014 (0.9 to 1). The two rises are smaller than the falls around\n    them and may be sampling noise of the scan; this was not tested.\n- claim: fig3f-noise-drop-below-70\n  outcome: reproduced\n  notebook: reproduce_kutschireiter_2023.ipynb\n  output: claim:fig3f-noise-drop-below-70\n  notes: >-\n    The noise-free optimum is kappa* 0.5, beta 0.2. Kept at those values, the network's relative\n    performance is 63.1% at noise SD 10 and 38.1% at SD 20, under the notebook's normalization\n    (particle filter) and the legend's (same network at SD 0, 63.07% and 38.06%), below 70% under all\n    four combinations. It first falls below 70% at SD 9 (67.4%).\n- claim: fig3f-retuning-reduces-drop\n  outcome: reproduced\n  notebook: reproduce_kutschireiter_2023.ipynb\n  output: claim:fig3f-retuning-reduces-drop\n  measured: 34.64\n  notes: >-\n    The reduction of the drop by retuning is 34.64% at SD 10 with the particle filter normalization\n    (the first reading, given as measured) and 34.56% with the legend's, and 31.67% for the mean\n    over SD 1 to 10 with the particle filter normalization, inside 31.5 to 38.5%. The other readings\n    are outside it, 31.19% (mean, legend normalization) and 29.80 and 29.76% (SD 20). The retuned\n    signal-to-noise ratio is above the untuned one at every noise SD above 0 (ratio 1.05 to 3.00).\n    Fig. S4, reported only, the best kappa* grows from 0.3 to 4.8 between SD 1 and 10, and the best\n    beta from 0.1 to 2.0 but not steadily, and both fall again at SD 15 and 20.\n  deviations:\n  - >-\n    The paper does not say at which noise level the 35% is taken; the claims file names six\n    readings, three of them match, and all are shown.\n- claim: noise-effects-on-mu-and-kappa\n  outcome: partially_reproduced\n  notebook: reproduce_kutschireiter_2023.ipynb\n  output: claim:noise-effects-on-mu-and-kappa\n  notes: >-\n    2,000 runs of T 5 per setting, noise SD 1 and 2, N 64 and 256. (1) holds. The mean change of\n    position is within 2 standard errors of 0 in all four settings (z -0.74 to 0.82) and its\n    variance grows at each second (for N 64, SD 1, 0.034 at 1 s to 0.232 at 5 s). (3) holds. The SD\n    of the one-step amplitude increments at N 256 is 0.500 and 0.501 times that at N 64. (2) fails.\n    The mean amplitude falls throughout the run and ends at 0.83, 0.65, 0.82 and 0.42, all below the\n    noise-free 1.00, so there is no upward drift and no overconfidence in this network. In\n    RNN_filter_Run the noise also enters the rectified sum that drives the global inhibition, which\n    may explain the fall; the SI derivation is not checked here.\n  deviations:\n  - >-\n    The runs use a batched copy of RNN_filter_Run (bra.rnn_batch), the same update term by term; on\n    the same noise draws it matches the released function to 4e-16.\n  - >-\n    The released RNN_filter_Run has no z parameter and raises NameError; z=None was added to its\n    signature, as the claims file says.\n- claim: fig4b-connectome-motifs\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_kutschireiter_2023.ipynb\n  output: claim:fig4b-connectome-motifs\n  notes: >-\n    Sorted by the PB glomerulus in the name (reading (a)), left PEN1 neurons send their EPG output a\n    mean of +0.56 glomeruli from their EPG input (10 of 10 positive, Wilcoxon p 0.002) and right PEN1\n    neurons -0.48 (9 of 10 negative, p 0.004), among same-side EPG neurons; with partners on both\n    sides, +0.37 and -0.35. The two edge neurons (L9, R9) have offsets near 0. Every Delta7 receives\n    EPG input from 13 to 16 of the 16 EPG glomeruli and sends output to EPG neurons in 9 to 15,\n    more than half. Counting only glomeruli with at least 3 (or 5) synapses, inputs still reach more\n    than half for all 42 Delta7, but outputs do for 7 (or 0) of 42, so the breadth of the\n    Delta7 to EPG side depends on the threshold. Reading (b), by ellipsoid body or gall position,\n    could not be run.\n  deviations:\n  - >-\n    The criterion asks for two sorts. Reading (b), by the ellipsoid body or gall position in the\n    neuron's name, cannot be formed: hemibrain instance names give only the PB glomerulus (EPG(PB08)_L1,\n    PEN_a(PB06a)_R2). The outcome rests on reading (a) alone.\n  - >-\n    Assumed, as the Fig. 4B legend counts \"the total number of synaptic connections between each\n    cell pair\" with no threshold, that a connection is any synapse; the counts at 3 and 5 synapses\n    are shown.\n  - >-\n    Assumed a measure of the offset, since the paper gives none. For each PEN1 neuron, it is the\n    synapse-weighted circular mean position (period 8 glomeruli) of its EPG targets minus that of\n    its EPG inputs, among same-side EPG neurons, with both sides shown.\n  - >-\n    The connectome is the public hemibrain v1.2 export, not v1.2.1 as in the legend. neuPrint, which\n    serves v1.2.1, now requires a personal API token for all data.\n- claim: fig4gh-drosophila-network-matches\n  outcome: partially_reproduced\n  notebook: reproduce_kutschireiter_2023.ipynb\n  output: claim:fig4gh-drosophila-network-matches\n  notes: >-\n    From figure4g.npz, the Drosophila-like network's accuracy is within 0.02 of the Bayesian ring\n    attractor's at all 23 rates (largest 0.019 at 0.1/s), so reading (b) holds, but it exceeds 0.01\n    at 0.1, 0.2 and 0.3/s (0.019, 0.014, 0.010), so reading (a) fails; the criterion needs both. At\n    0.4/s and above the difference is at most 0.004. Mean certainties, reported only, are lower in\n    the Drosophila-like network at every rate (0.88 against 1.00 at 0.01/s, 13.8 against 14.5 at\n    100/s).\n- claim: figs2-performance-independent-of-n\n  outcome: partially_reproduced\n  notebook: reproduce_kutschireiter_2023.ipynb\n  output: claim:figs2-performance-independent-of-n\n  notes: >-\n    Of the 161 values in figureS2.npz (7 network sizes, 23 rates), one is more than 0.02 from the\n    quadratic circKF reference, N 16 at 0.1/s (0.041 below). Every other value, N 3 and 4 included,\n    is within 0.019. Both readings include N 16, so neither holds as written. One value (N 128 at\n    100/s) is missing (NaN) in the stored array.\n- claim: prediction-bump-amplitude-cue-reliability\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_kutschireiter_2023.ipynb\n  output: claim:prediction-bump-amplitude-cue-reliability\n  notes: >-\n    Tested on the 15 flies of the dandiset's cue-contrast experiment, high (more reliable) against\n    low contrast, with bump amplitude the length of the population vector at the bump's spatial\n    frequency across the PB midline ROIs (frequency 2, the spectral peak in every fly). The readings\n    disagree, and the criterion blocks the claim when they do. With dF/F, amplitude is higher at high\n    contrast in 10 of 15 flies (reading (a) holds) but the one-sided Wilcoxon test gives p 0.138\n    (reading (b) fails). With raw fluorescence minus baseline, 12 of 15 flies (a) and p 0.021 (b).\n    Median high to low ratio 1.12 (dF/F) and 1.11 (raw). Variants, high against zero contrast give\n    12 of 15 flies (p 0.047) and 13 of 15 (p 0.006), and low contrast is not above zero contrast\n    (7 of 15 with either signal). Without sub-2, which has one high-contrast block, dF/F gives 9 of\n    14 (p 0.21) and raw 11 of 14 (p 0.034). Question for the paper's authors (finding below). The\n    Discussion gives no experimental method for the prediction (which activity signal, which cue\n    conditions are compared, which test). With these data the answer depends on the signal and the\n    test, and no reading has more support in the paper than another.\n  deviations:\n  - >-\n    The dandiset holds data of a separate study, not of this paper; the paper does not test its\n    prediction.\n  - >-\n    Raw fluorescence is read from 10% of the frames (25 volumes every 250), averaged over planes and\n    smoothed in the plane (Gaussian SD 4 pixels) before averaging in each ROI mask; the baseline is\n    each ROI's 10th percentile. The projection and the smoothing were chosen as those that best\n    reproduce the stored dF/F (median correlation over ROIs 0.93, against 0.66 without smoothing).\nfindings:\n- kind: metadata_error\n  statement: >-\n    The dandiset's related resources name the bioRxiv preprint \"Bayesian inference in ring attractor\n    networks\" (10.1101/2021.12.17.473253 version 4) as the paper it supplements, but its\n    description says the data belong to \"Uncertainty and learning in a biological ring attractor\"\n    (Basnak et al., in preparation). The linked paper, published as Kutschireiter et al. 2023 (PNAS),\n    is a theory paper that analyses none of these data, so the dandiset links no paper that uses them.\n- kind: metadata_error\n  statement: >-\n    imaging_rate is 9.18 Hz in every file, but sub-4 and sub-10 (cue-contrast experiment) are imaged\n    at 7.87 Hz (0.127 s frame interval, 9446 frames in 1200 s) with 14 planes, against 9.18 Hz and\n    12 planes in the other 13 sessions.\n- kind: other\n  statement: >-\n    In sub-2 the trials table has five blocks (high, zero, low, zero, low) where every other fly of\n    the cue-contrast experiment has six with two of each contrast. The last block lasts 405 s\n    against about 200 s in the protocol, so it may hold a low and a high block labelled as one.\n- kind: metadata_insufficient\n  statement: >-\n    The processing behind the stored dF/F is not described (which planes, the extent of each ROI,\n    the baseline). The ROI masks are a few pixels each on the PB midline, and the dF/F agrees with\n    the raw imaging averaged in those masks only after spatial smoothing (median correlation over\n    ROIs 0.66 without, 0.93 with a 4-pixel Gaussian, sub-1). The RoiResponseSeries unit is \"na\".\n- kind: methods_unavailable\n  statement: >-\n    Question for the paper's authors. The Discussion predicts higher bump amplitude with reliable\n    external HD cues but gives no experimental method. Which activity signal (dF/F or raw\n    fluorescence), which comparison of cue conditions and which test would test it? On this\n    dandiset's cue-contrast experiment, high contrast exceeds low contrast in most flies with either\n    signal, but a one-sided Wilcoxon test over 15 flies gives p 0.021 with raw fluorescence and\n    p 0.138 with dF/F.\n- kind: methods_unavailable\n  statement: >-\n    Question for the paper's authors. Fig. 4B sorts neurons \"by their spatial position as a proxy for\n    their preferred HD\". Which position was used? The hemibrain names give only the PB glomerulus\n    for EPG and PEN1 neurons. This attempt sorted by it and counted any synapse as a connection.\n- kind: code_mismatch\n  statement: >-\n    The released code does not run as published. RNN_filter_Run (circularFiltering.py) uses z but\n    has no z parameter, and Figure2h.ipynb and the scan scripts pass kappa_y to functions whose\n    parameter is kappa_v. One NaN remains in figureS2.npz (N 128 at 100/s).\n- kind: code_mismatch\n  statement: >-\n    In the released single-population network (RNN_filter_Run) at the Bayesian ring attractor's\n    parameters, additive neural noise lowers the mean bump amplitude (from 1.00 to 0.42 to 0.83\n    after 5 s, N 64 and 256, noise SD 1 and 2). The Results and SI Appendix section 5 say the noise\n    causes a positive drift of the amplitude.\n"
}
```

```
File created successfully at: attempts/000289-kutschireiter-2023-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR; grep -n "9 of 10 positive\|0.0013 (0.9 to 1)" build_nb.py; sed -i 's/(9 of 10 positive) and right ones/(10 of 10 positive) and right ones/; s/and 0.0013 (0.9 to 1)/and 0.0014 (0.9 to 1)/' build_nb.py; grep -n "10 of 10 positive\|0.0014 (0.9" build_nb.py; . venv/bin/activate; python build_nb.py; cd  date -u; python tools/entry.py all entries/000289-kutschireiter-2023 2>&1 | tail -3; date -u
```

```
453:every step: it rises twice, by 0.0008 (beta 0.7 to 0.8) and 0.0013 (0.9 to 1), so condition (4)
657:(9 of 10 positive) and right ones -0.48 (9 of 10 negative), opposite directions, both different from
453:every step: it rises twice, by 0.0008 (beta 0.7 to 0.8) and 0.0014 (0.9 to 1), so condition (4)
657:(10 of 10 positive) and right ones -0.48 (9 of 10 negative), opposite directions, both different from
written 53
Thu Oct 29 23:52:07 UTC 2026
Installed kernelspec registry-000289-kutschireiter-2023 in executed/000289-kutschireiter-2023/.venv/share/jupyter/kernels/registry-000289-kutschireiter-2023
0 error(s)
pass  reproduce_kutschireiter_2023.ipynb  (512 s)
Fri Oct 30 00:00:45 UTC 2026
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json
nb=json.load(open('executed/000289-kutschireiter-2023/reproduce_kutschireiter_2023.ipynb'))
out=''.join(''.join(o.get('text','')) for c in nb['cells'] if c['cell_type']=='code' for o in c.get('outputs',[]))
for k in ['p = 0.1384','p = 0.0206','34.64','0.0008','0.0014','min diff 0.0115','0.9936','12 of 15','raw fluorescence read in','notebook ran in']:
    i=out.find(k); print(k, i>=0, out[i:i+60].replace('\n',' ') if i>=0 else '')
EOF
grep -n "—\|rather\|\*\*" attempts/000289-kutschireiter-2023-01.yaml entries/000289-kutschireiter-2023/README.md entries/000289-kutschireiter-2023/bra.py | head; python3 -c "
import json;nb=json.load(open('entries/000289-kutschireiter-2023/reproduce_kutschireiter_2023.ipynb'))
import re
for c in nb['cells']:
    s=''.join(c['source'])
    for m in re.findall(r'\*\*[^*]+\*\*',s):
        if not m.startswith('**Result'): print(m)
    if '—' in s or 'rather' in s: print('BAD',s[:80])
"
```

```
p = 0.1384 True p = 0.1384    variant, high against zero contrast: 12 of 15 
p = 0.0206 True p = 0.0206    variant, high against zero contrast: 13 of 15 
34.64 True 34.64, 15.0: 32.25, 20.0: 29.8} normalization self reduction
0.0008 True 0.0008 -0.0062  0.0014 -0.0168 -0.02   -0.0203] ; rises: 2 o
0.0014 True 0.0014 -0.0168 -0.02   -0.0203] ; rises: 2 of 10 variant, no
min diff 0.0115 True min diff 0.0115 strictly above at every rate 0.1 to 10: True
0.9936 True 0.993624       7.214148     1.220141      7.270836    0.8810
12 of 15 True 12 of 15  gamma_z  alpha  kappa_t  a_conf  a_opp  b_conf  b_
raw fluorescence read in True raw fluorescence read in 438 s      dff_zero  dff_low  dff_h
notebook ran in True notebook ran in 8.5 min 
**Paper.**
**Dandiset.**
**What the dandiset holds, and what the paper uses.**
**{f"in>={th}": int((i_ >= th).sum()) for th in (1, 3, 5)},
                 **
**How the analysis differs from the paper's.**
**What was found about the dataset.**
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
import re
p='build_nb.py'; s=open(p).read()
for lab in ["Paper.","Dandiset.","What the dandiset holds, and what the paper uses.","How the analysis differs from the paper's.","What was found about the dataset.","Question for the paper's authors."]:
    s=s.replace("**"+lab+"**",lab)
open(p,'w').write(s)
print(re.findall(r'\*\*[A-Z][^*\n]{0,40}\*\*',s))
EOF
. venv/bin/activate; python build_nb.py; cd  date -u; python tools/entry.py all entries/000289-kutschireiter-2023 2>&1 | tail -2; date -u
```

```
['**Result: reproduced.**', '**Result: reproduced.**', '**Result: reproduced.**', '**Result: reproduced.**', '**Result: reproduced.**', '**Result: partially reproduced.**', '**Result: reproduced.**', '**Result: reproduced.**', '**Result: partially reproduced.**', '**Result: partially reproduced.**', '**Result: partially reproduced.**', '**Result: blocked (methods_underspecified).**']
written 53
Fri Oct 30 00:00:56 UTC 2026
0 error(s)
pass  reproduce_kutschireiter_2023.ipynb  (530 s)
Fri Oct 30 00:09:52 UTC 2026
```

**Agent calls Bash**

```bash
cd  . $TMPDIR/venv/bin/activate; python tools/entry.py handover entries/000289-kutschireiter-2023 2>&1 | tail -5; ls executed/000289-kutschireiter-2023/handover/; python tools/entry.py check entries/000289-kutschireiter-2023 | tail -2; git status --short
```

```
wrote executed/000289-kutschireiter-2023/handover
10.1073-pnas.2210622120.yaml
bra.py
reproduce_kutschireiter_2023.ipynb
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
?? attempts/000289-kutschireiter-2023-01.yaml
?? entries/000289-kutschireiter-2023/
?? scripts
```

**Agent calls Bash**

```bash
cd  ls -a entries/000289-kutschireiter-2023/; git check-ignore -v executed scripts 2>&1 | head; date -u
```

```
.
..
.claude
README.md
__pycache__
bra.py
entry.yaml
reproduce_kutschireiter_2023.ipynb
requirements.in
requirements.lock.txt
.gitignore:6:executed/	executed
Fri Oct 30 00:10:06 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/000289-kutschireiter-2023; ls -la .claude; git check-ignore -v __pycache__ .claude; rm -rf __pycache__
```

```
total 12
drwxr-xr-x 3 runner runner 4096 Oct 29 23:25 .
drwxr-xr-x 4 runner runner 4096 Oct 29 23:50 ..
drwx------ 2 runner runner 4096 Oct 29 23:25 .cc-writes
.gitignore:1:__pycache__/	__pycache__
```

**Agent**

I've finished steps 1 to 5 and the handover (step 6), in about 1 h 20 min (22:52 to 00:10 UTC). The entry passes `python tools/entry.py all` with 0 errors and the notebook runs in about 9 minutes.

### 1. Outcomes

| Claim | Outcome |
|---|---|
| fig1-conflict-decreases-certainty | reproduced |
| fig2h-bump-tracks-circkf | reproduced |
| fig2i-accuracy-and-certainty-vs-reliability | reproduced |
| fig3b-bayesian-beats-conventional | reproduced |
| fig3c-update-weights | reproduced |
| fig3d-best-network-slow-decay | partially reproduced: condition (4) fails, with two small rises (0.0008 and 0.0014) |
| fig3f-noise-drop-below-70 | reproduced (63.1% at noise SD 10) |
| fig3f-retuning-reduces-drop | reproduced: measured 34.64% (expected 35 ± 3.5) |
| noise-effects-on-mu-and-kappa | partially reproduced: bump amplitude falls under noise instead of drifting up |
| fig4b-connectome-motifs | reproduced, resting on an assumption (`assumed: true`) |
| fig4gh-drosophila-network-matches | partially reproduced: holds within 0.02, not within 0.01 |
| figs2-performance-independent-of-n | partially reproduced: one value (N 16 at 0.1/s) is 0.041 off |
| prediction-bump-amplitude-cue-reliability | blocked, `methods_underspecified` (the claim's readings disagree) |

### 2. The dataset, assumptions and questions

**What the dataset is.** The paper is a theory paper. The dandiset holds imaging of EPG neurons from a separate study by the same lab (Basnak et al.), and the paper uses none of it. Twelve claims are tested on the paper's Zenodo code and outputs (doi:10.5281/zenodo.7615975) and on the public hemibrain v1.2 export. The prediction claim is tested on the dandiset's cue-contrast experiment (subjects 1 to 15).

**Version.** I pinned 0.240801.1040. It is the only published version, and the draft is identical in assets and size.

**Findings recorded:**
- **Wrong paper link.** The dandiset links this paper's preprint, which uses none of its data.
- **Wrong imaging rate.** `imaging_rate` says 9.18 Hz for every file, but sub-4 and sub-10 are imaged at 7.87 Hz.
- **Odd trial table.** sub-2 has one high-contrast block where every other fly has two, and a 405 s final block labelled low.
- **dF/F not described.** The stored dF/F matches the raw imaging only after spatial smoothing (correlation 0.66 without, 0.93 with), and the files don't say how it was made.
- **Paper's code issues.** Two code issues block running it as released (a missing `z` argument, a `kappa_y`/`kappa_v` keyword mismatch). Its network's amplitude falls under noise, against what the SI predicts.
- **Clock check.** The bump phase follows the cue position with peak coupling at lag 0 to 5 frames, so the dF/F and the cue share a clock.

**Assumptions (fig4b):**
- I sorted neurons by protocerebral bridge glomerulus only. The other sort the criterion names can't be formed because hemibrain names carry no ellipsoid body position.
- Any synapse counts as a connection.
- I defined the PEN1 offset as a synapse-weighted circular mean, since the paper gives no measure.

**Questions for the paper's authors (recorded as `methods_unavailable` findings):**
- Which signal, comparison and test should test the bump-amplitude prediction? Here the answer changes with the choice: raw fluorescence gives p 0.021, dF/F gives p 0.138.
- Which spatial position was used to sort neurons in Fig. 4B?

**Questions to a reader:** none.

### 3. Where the protocol was unclear

1. **Theory paper.** The protocol assumes the dataset holds the paper's data; here it doesn't. I tested the twelve `elsewhere` claims on the paper's Zenodo deposit, held in memory and pinned by DOI and md5.
2. **A named reading that can't be run.** The protocol doesn't cover the case where one of the criterion's readings can't be formed from the data (fig4b's second sort). I judged on the reading that can be run and marked the outcome as resting on an assumption.
3. **"All readings" versus "any reading".** The claims file requires every reading to hold for unquantified words (fig4gh, figs2), while the protocol lets a number be reproduced under any reading. I followed the claims file, so both are partially reproduced.
4. **Block versus adopt an assumption.** The prediction's criterion says to block when the readings differ, while step 1.6 allows adopting the best-supported reading. I followed the claims file and blocked.
5. **What counts as public.** neuPrint, which serves the v1.2.1 connectome the paper used, now needs a personal token. I used the public v1.2 export and recorded the difference as a deviation.
6. **Scope of the duplicate check.** I compared traces only among the 15 sessions the analysis uses. The other 206 files were surveyed by metadata only.
7. **Streaming outside inputs.** The streaming rule is written for the dataset; I read the 0.8 MB zip and the 46 MB tar whole into memory, never to disk.
8. **Partial versus not reproduced.** When one condition of a multi-condition criterion fails but the effect is present (fig3d, the noise claim), I recorded `partially_reproduced`.

### 4. Runtime and failures

- The notebook runs in about 8.5 to 9 minutes, most of it streaming 10% of the raw imaging for the 15 sessions.
- Nothing failed. The paper's large simulation scans (10,000 trajectories per setting) were not re-run; the claims are judged on the stored outputs, as the claims file says.
- I left untracked files I didn't create (`.bashrc`, `.idea`, `scripts`, and others) in the repository root untouched.

Files are in `entries/000289-kutschireiter-2023/`:
- `reproduce_kutschireiter_2023.ipynb`
- `bra.py`
- `README.md`
- `entry.yaml`

The attempt record is `attempts/000289-kutschireiter-2023-01.yaml`, and the verifier package is in `executed/000289-kutschireiter-2023/handover/`.

## End of run

65 turns, 74 minutes, result: success.
