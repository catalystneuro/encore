# 001262 · author · run 41311677966

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md
```

```
<persisted-output>
Output too large (35.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/4d0748f9-9817-4f0d-8943-3e865e048c1d/tool-results/bx85kjk3y.txt

Preview (first 2KB):
Sun Nov  1 13:36:05 UTC 2026
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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/4d0748f9-9817-4f0d-8943-3e865e048c1d/tool-results/bx85kjk3y.txt"
}
```

```
1	Sun Nov  1 13:36:05 UTC 2026
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
[... 594 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md | head -150; echo ----; cat docs/design.md | head -200; echo ----; cat docs/archives.md
```

```
<persisted-output>
Output too large (33.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/4d0748f9-9817-4f0d-8943-3e865e048c1d/tool-results/bsrfqewxi.txt

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

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/4d0748f9-9817-4f0d-8943-3e865e048c1d/tool-results/bsrfqewxi.txt"
}
```

```
1	# Encore Science: the registry
2	
3	Encore Science checks datasets against the papers they came from. This repository holds its public record, the Encore registry, served at <https://encorescience.org>, and the `encore` command that runs the same check on your own data ([docs/encore.md](docs/encore.md)). It is developed by [CatalystNeuro](https://www.catalystneuro.com).
4	
5	Agents, and people, try to reproduce the key findings of papers from the open
6	data in public archives, starting with the [DANDI Archive](https://dandiarchive.org), and register the result
7	here: the notebooks when it works, and the reason when it does not.
8	
9	- **For the archive:** evidence of whether each dandiset is complete and
10	  accurate enough to support the findings of its paper.
11	- **For analysts:** working notebooks to build new analyses on.
12	
13	Status: pilot. All eight pilot targets have been attempted and checked by an
14	independent agent.
15	
16	**Dashboard:** <https://encorescience.org/>
17	
18	## Reading the outcomes
19	
20	An outcome says what one attempt could recover from the data in a dandiset,
[... 609 more lines not kept]
```

**Agent**

Now the example entry and the claims file.

**Agent calls Bash**

```bash
ls entries/001453-fouke-2025/ claims/001453/ claims/001262/ paper/; cat claims/001262/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/001262/10.1038-s41597-024-03259-3.yaml"
}
```

```
1	# Claims for Heeringa (2024), Scientific Data 11, 411, on dandiset 001262.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22,
3	# protocol pilot-10 as stated in docs/protocol.md.
4	#
5	# Text read: the version of record (open access, PMC11035566), as served by Europe PMC, in
6	# paper/10.1038-s41597-024-03259-3.txt: Background & Summary, Methods, Data Records, Technical
7	# Validation, Usage Notes, Code availability, Table 1 and the figure legends. The paper is a
8	# Data Descriptor and has no supplement. The PDF was not needed.
9	#
10	# Code read: the software toolbox the paper links, Zenodo record 10370064
11	# (doi:10.5281/zenodo.10370064, the only version, published 2024-04-15), 21 MATLAB files:
12	# check_dataset_metadata.m (Table 1, Fig. 3, metadata.csv), check_dataset_units.m (all panels
13	# of Figs. 6 and 7), check_dataset_animal.m, checkAN.m (Fig. 4), makePSTH.m (Fig. 5b),
14	# call_extract_func.m and the analysis functions BFextract_func.m, RLFextract_func.m,
15	# getDrivenRatesRLF.m, PHextract_func.m, TytoView_calcVS.m, CFextract_func.m, getQ10dB.m,
16	# Clickextract_func.m, getFSL2bins.m, getFSLpoisson.m, SRextract_func.m, getSpikeCounts.m,
17	# and bandwidthBF.m, getQ10dB_withCF.m, getRasterData3.m, which no criterion uses.
18	# Details the code settles, used in the criteria below:
19	#   - Age groups (both scripts): young adult age <= 365 days, middle aged > 365 and <= 1095
20	#     days, old > 1095 days; months are days / (365/12). Table 1 statistics are over animals.
[... 506 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001453-fouke-2025/; cat entry.yaml requirements.in README.md; head -c 3000 omr.py; cat ../../attempts/001453-fouke-2025-01.yaml | head -250
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
[... 348 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 250,400p attempts/001453-fouke-2025-01.yaml; ls schemas; ls questions | head
```

```
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
- kind: metadata_error
  statement: f0_vtheta is stated in radians/s but holds the heading change per frame in radians,
    and f0_vx and f0_vy are stated in pixels/s but are per frame. In most Danionella files the sum
    of f0_vtheta over a trial does not match the change of f0_theta (median ratios 0.09 to 0.89).
- kind: other
  statement: 18 of 25 zebrafish files and 1 of 12 Danionella files are sampled at 32 to 35 Hz,
    where the Methods state tracking at more than 150 Hz. Their timestamp intervals are regular
[... 145 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;nb=json.load(open('entries/001453-fouke-2025/reproduce_fouke_2025.ipynb'))
print(nb['metadata'])
for c in nb['cells'][:8]: print(c['cell_type'],c['metadata'],''.join(c['source'])[:1500]);print('=====')
print(len(nb['cells']))
for c in nb['cells'][-3:]: print(c['cell_type'],c['metadata'],''.join(c['source'])[:1500]);print('=====')
"
```

```
{'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}}
markdown {} # Reproducing Fouke et al. (2025) from dandiset 001453

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
[... 167 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -c paper/*.txt; cat paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/4d0748f9-9817-4f0d-8943-3e865e048c1d/tool-results/bs1xgtiuw.txt"
}
```

```
1	70616 paper/10.1038-s41597-024-03259-3.txt
2	DOI: 10.1038/s41597-024-03259-3
3	Version: as served by europe_pmc
4	Source: europe_pmc+crossref (paper-text-fetcher)
5	Stored: 2026-10-20
6	Extracted: as fetched
7	------------------------------------------------------------------------
8	pmc Sci Data Sci Data 2628 sdata 101640192 Scientific Data 2052-4463 Nature Publishing Group PMC11035566 PMC11035566.1 11035566 11035566 38649691 10.1038/s41597-024-03259-3 3259 1 Data Descriptor Single-unit data for sensory neuroscience: Responses from the auditory nerve of young-adult and aging gerbils http://orcid.org/0000-0002-8391-0581 Heeringa Amarins N. [removed: an e-mail address] https://ror.org/033n9gh91 grid.5560.6 0000 0001 1009 3608 Research Centre Neurosensory Science and Cluster of Excellence “Hearing4all”, Department of Neuroscience, School of Medicine and Health Science, Carl von Ossietzky University Oldenburg, Carl von Ossietzky Straße 9-11, 26129 Oldenburg, Germany 22 4 2024 2024 11 452200 411 15 12 2023 12 4 2024 22 04 2024 23 04 2024 23 03 2026 © The Author(s) 2024 https://creativecommons.org/licenses/by/4.0/ Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/ . This da
[... 51 more lines not kept]
```

**Agent**

Now the dataset.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/001262/ | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/001262/versions/" | python -m json.tool
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/001262/versions/0.241205.0959/ > meta.json; python -c "
import json;m=json.load(open('meta.json'))
for k in ['description','citation','relatedResource','assetsSummary','wasGeneratedBy','keywords','doi']: print(k, json.dumps(m.get(k),indent=1)[:3000])
"; curl -s https://api.dandiarchive.org/api/dandisets/001262/versions/0.241205.0929/ > meta29.json; python -c "
import json;a=json.load(open('$TMPDIR/meta.json'));b=json.load(open('$TMPDIR/meta29.json'))
for k in set(a)|set(b):
  if a.get(k)!=b.get(k): print('DIFF',k, str(a.get(k))[:300], '|||', str(b.get(k))[:300])
"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; python - <<'EOF'
import json, urllib.request
def assets(v):
    out=[];url=f"https://api.dandiarchive.org/api/dandisets/001262/versions/{v}/assets/?page_size=1000"
    while url:
        d=json.load(urllib.request.urlopen(url)); out+=d['results']; url=d['next']
    return out
a=assets('0.241205.0959'); b=assets('0.241205.0929')
json.dump(a,open('assets.json','w'))
print(len(a),len(b)); print(a[0]); 
pa={x['path']:(x['blob'] if 'blob' in x else x.get('asset_id'), x['size']) for x in a}
pb={x['path']:(x['blob'] if 'blob' in x else x.get('asset_id'), x['size']) for x in b}
print('same paths', set(pa)==set(pb), 'same sizes', all(pa[p][1]==pb[p][1] for p in pa))
for x in a[:10]: print(x['path'], x['size'])
import collections
subs=collections.Counter(x['path'].split('/')[0] for x in a); print(len(subs)); print(sorted(subs.items())[:10])
sz=[x['size'] for x in a]; import statistics; print(min(sz),statistics.median(sz),max(sz))
EOF
```

```
1160 1160
{'asset_id': '0874747b-cdfb-4ef6-b111-7770f9de7d10', 'blob': '2638abe7-1cad-47a4-8996-fe2bf612a82e', 'zarr': None, 'path': 'sub-G150730/sub-G150730_ses-G150730-2P-780nm_icephys.nwb', 'size': 5409288, 'created': '2024-12-04T07:05:13.736479Z', 'modified': '2024-12-05T09:29:28.212828Z'}
same paths True same sizes True
sub-G150730/sub-G150730_ses-G150730-2P-780nm_icephys.nwb 5409288
sub-G150730/sub-G150730_ses-G150730-1P-675nm_icephys.nwb 9914536
sub-G150730/sub-G150730_ses-G150730-6P-1035nm_icephys.nwb 9094152
sub-G150730/sub-G150730_ses-G150730-6P-1365nm_icephys.nwb 9913712
sub-G150730/sub-G150730_ses-G150730-1P-465nm_icephys.nwb 36566120
sub-G150730/sub-G150730_ses-G150730-6P-1545nm_icephys.nwb 9090688
sub-G150730/sub-G150730_ses-G150730-2P-975nm_icephys.nwb 77338640
sub-G150730/sub-G150730_ses-G150730-6P-975nm_icephys.nwb 9089632
sub-G150717/sub-G150717_ses-G150717-1P-588nm_icephys.nwb 99109200
sub-G150730/sub-G150730_ses-G150730-6P-1420nm_icephys.nwb 49244184
104
[('sub-G150717', 1), ('sub-G150730', 13), ('sub-G150805', 4), ('sub-G150921', 6), ('sub-G150922', 21), ('sub-G150929', 2), ('sub-G151001', 24), ('sub-G151104', 9), ('sub-G151110', 2), ('sub-G151126', 25)]
2180256 17353768.0 528741648
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; python -c "import pynwb,remfile,h5py,dandi;print(pynwb.__version__,h5py.__version__)" ; uv --version
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pynwb,remfile,h5py,dandi;print(pynwb.__version__,h5py.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pynwb'
uv 0.13.6 (x86_64-unknown-linux-gnu)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; uv venv -q env && . env/bin/activate && uv pip install -q pynwb h5py remfile numpy pandas scipy matplotlib dandi 2>&1 | tail -3; python -c "import pynwb;print(pynwb.__version__)"
```

```
4.2.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; . env/bin/activate; python - <<'EOF'
import json,h5py,remfile,time
a=json.load(open('assets.json'))
x=[x for x in a if x['path'].startswith('sub-G150730')][0]
url=f"https://api.dandiarchive.org/api/assets/{x['asset_id']}/download/"
import requests
r=requests.head(url,allow_redirects=True); s3=r.url; print(s3)
t=time.time()
f=h5py.File(remfile.File(s3),'r')
def show(name,obj):
    if isinstance(obj,h5py.Dataset):
        print('D',name,obj.shape,obj.dtype, dict(obj.attrs) if len(obj.attrs)<6 else list(obj.attrs))
    else:
        print('G',name,{k:(v if not hasattr(v,'shape') or v.size<5 else '...') for k,v in obj.attrs.items()})
f.visititems(show)
print(time.time()-t)
EOF
```

```
<persisted-output>
Output too large (51.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/4d0748f9-9817-4f0d-8943-3e865e048c1d/tool-results/bn5r0yjzo.txt

Preview (first 2KB):
https://dandiarchive.s3.amazonaws.com/blobs/263/8ab/2638abe7-1cad-47a4-8996-fe2bf612a82e?response-content-disposition=attachment%3B%20filename%3D%22sub-G150730_ses-G150730-2P-780nm_icephys.nwb%22&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=[removed: an AWS key]%2F20261101%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Date=20261101T133656Z&X-Amz-Expires=21600&X-Amz-SignedHeaders=host&X-Amz-Signature=becf9b13b52606dc83b2d26cf13713a91a7146785bdcccc845f2cd6b57edb30b
G acquisition {}
G acquisition/BF_FREQ1000_rep1 {'comments': 'no comments', 'description': 'recorded voltage trace', 'namespace': 'core', 'neurodata_type': 'VoltageClampStimulusSeries', 'object_id': '57660a58-4f20-4a39-9f5a-efc2537ddded', 'stimulus_description': 'N/A'}
D acquisition/BF_FREQ1000_rep1/data (9765,) float64 {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'volts'}
D acquisition/BF_FREQ1000_rep1/gain () float64 {}
D acquisition/BF_FREQ1000_rep1/starting_time () float64 {'rate': np.float64(48828.125), 'unit': 'seconds'}
G acquisition/BF_FREQ1000_rep2 {'comments': 'no comments', 'description': 'recorded voltage trace', 'namespace': 'core', 'neurodata_type': 'VoltageClampStimulusSeries', 'object_id': '185495ea-cbac-4047-936a-6a32ffb05390', 'stimulus_description': 'N/A'}
D acquisition/BF_FREQ1000_rep2/data (9765,) float64 {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'volts'}
D acquisition/BF_FREQ1000_rep2/gain () float64 {}
D acquisition/BF_FREQ1000_rep2/starting_time () float64 {'rate': np.float64(48828.125), 'unit': 'seconds'}
G acquisition/BF_FREQ1000_rep3 {'comments': 'no comments', 'description': 'recorded voltage trace', 'namespace': 'core', 'neurodata_type': 'VoltageClampStimulusSer
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
grep -v "^[GD] acquisition/" /home/runner/.claude/projects/-home-runner-work-encore-encore/4d0748f9-9817-4f0d-8943-3e865e048c1d/tool-results/bn5r0yjzo.txt | cut -c1-600; grep -c "^G acquisition/" /home/runner/.claude/projects/-home-runner-work-encore-encore/4d0748f9-9817-4f0d-8943-3e865e048c1d/tool-results/bn5r0yjzo.txt; grep "^G acquisition/" /home/runner/.claude/projects/-home-runner-work-encore-encore/4d0748f9-9817-4f0d-8943-3e865e048c1d/tool-results/bn5r0yjzo.txt | cut -d' ' -f2 | sed 's/_rep.*//' | sort | uniq -c | head -50
```

```
https://dandiarchive.s3.amazonaws.com/blobs/263/8ab/2638abe7-1cad-47a4-8996-fe2bf612a82e?response-content-disposition=attachment%3B%20filename%3D%22sub-G150730_ses-G150730-2P-780nm_icephys.nwb%22&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=[removed: an AWS key]%2F20261101%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Date=20261101T133656Z&X-Amz-Expires=21600&X-Amz-SignedHeaders=host&X-Amz-Signature=becf9b13b52606dc83b2d26cf13713a91a7146785bdcccc845f2cd6b57edb30b
G acquisition {}
G analysis {}
G analysis/analysis_table {'colnames': array(['experiment', 'results_bf', 'results_sr', 'results_threshold'],
      dtype=object), 'description': 'here the analysis results are stored', 'namespace': 'hdmf-common', 'neurodata_type': 'DynamicTable', 'object_id': 'fdb4377d-42f0-417f-9385-72c72fc508ba'}
D analysis/analysis_table/experiment (1,) object {'description': 'name of the experiment the results refer to', 'namespace': 'hdmf-common', 'neurodata_type': 'VectorData', 'object_id': '1b9066cc-cfe6-4228-8400-22064d7df72d'}
D analysis/analysis_table/id (1,) int64 {'namespace': 'hdmf-common', 'neurodata_type': 'ElementIdentifiers', 'object_id': '68d1a907-f191-4bbb-a3d3-b0f55accd85d'}
D analysis/analysis_table/results_bf (1,) float64 {'description': 'estimated best frequency', 'namespace': 'hdmf-common', 'neurodata_type': 'VectorData', 'object_id': '6916db04-2532-4135-b383-04e9a80f2283'}
D analysis/analysis_table/results_sr (1,) float64 {'description': 'estimated spontaneous spike rate', 'namespace': 'hdmf-common', 'neurodata_type': 'VectorData', 'object_id': '1b9b2011-6f0b-4a81-8a67-12579968f84f'}
D analysis/analysis_table/results_threshold (1,) float64 {'description': 'estimated threshold', 'namespace': 'hdmf-common', 'neurodata_type': 'VectorData', 'object_id': '58b82d47-e7da-42dd-8a97-f167518cfe03'}
D file_create_date (1,) object {}
G general {}
G general/devices {}
G general/devices/device {'description': 'extracellular sharp glass electrode filled with 3M KCI', 'namespace': 'core'
[... 99 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . env/bin/activate; cat > peek.py <<'EOF'
import json,h5py,remfile,time,sys,requests
a=json.load(open('assets.json'))
def url(x):
    return requests.head(f"https://api.dandiarchive.org/api/assets/{x['asset_id']}/download/",allow_redirects=True).url
def dec(v):
    v=v[()] if hasattr(v,'shape') else v
    if isinstance(v,bytes): return v.decode()
    return v
def peek(x, full=False):
    f=h5py.File(remfile.File(url(x)),'r')
    print('==',x['path'])
    for k in ['identifier','session_description','session_start_time','general/experiment_description','general/notes','general/surgery','general/session_id','general/keywords','general/lab','general/institution','general/experimenter','general/subject/age','general/subject/description','general/subject/sex','general/subject/species','general/subject/subject_id','general/subject/weight','general/intracellular_ephys/electrode0/cell_id','general/intracellular_ephys/electrode0/description','general/intracellular_ephys/electrode0/filtering','general/devices/device']:
        if k in f:
            o=f[k]
            print(k,':',dec(o) if isinstance(o,h5py.Dataset) else dict(o.attrs))
    at=f['analysis/analysis_table']
    print({c:dec(at[c][:]) for c in ['experiment','results_bf','results_sr','results_threshold']})
    sr=f['general/intracellular_ephys/sequential_recordings']
    print('stimulus_type', [dec(s) for s in sr['stimulus_type'][:]])
    st=f['general/intracellular_ephys/intracellular_recordings/stimuli']
    import numpy as np
    for c in st.keys():
        if c in ('stimulus',): continue
        v=st[c][:]
        print(c, v[:8], len(v))
    print('units tag', f['units/tag'][:8])
    print('stim', f['stimulus/presentation/stimulus/data'][:], dict(f['stimulus/presentation/stimulus'].attrs))
    return f
if __name__=='__main__':
    for p in sys.argv[1:]:
        x=[x for x in a if p in x['path']][0]; peek(x)
EOF
python peek.py sub-G150730_ses-G150730-2P-780nm
```

```
== sub-G150730/sub-G150730_ses-G150730-2P-780nm_icephys.nwb
identifier : G150730:2P_780nm
session_description : gerbil auditory nerve fiber recordings
session_start_time : [b'2015-07-30T21:41:20.000000+02:00']
general/experiment_description : extracellular in vivo auditory nerve fiber recordings, DOI:https://doi.org/10.1038/s41597-024-03259-3
general/notes : ABR: stimulus: Chirp, 0.3-10 kHz, 4.2 ms; threshold (db SPL): 
general/surgery : anesthesia drugs: ketamine/xylazine, oxygen: no
general/session_id : G150730:2P_780nm
general/keywords : [b'Mongolian gerbil' b'auditory nerve fiber' b'single-unit recording'
 b'glass electrode']
general/lab : Koeppl lab
general/institution : Carl von Ossietzky Universität Oldenburg
general/experimenter : [b'Zhang, Lichun']
general/subject/age : P85D
general/subject/description : Mongolian gerbil
general/subject/sex : M
general/subject/species : Meriones unguiculatus
general/subject/subject_id : G150730
general/subject/weight : 65g
general/intracellular_ephys/electrode0/cell_id : electrode0
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . env/bin/activate; python - <<'EOF'
import json
a=json.load(open('assets.json'))
a.sort(key=lambda x:-x['size'])
for x in a[:5]: print(x['path'],x['size'])
# G220908 3p_181
print([x['path'] for x in a if 'G220908' in x['path'] and '181' in x['path']])
print([x['path'] for x in a if 'G220922' in x['path']][:30])
EOF
```

```
sub-G170512/sub-G170512_ses-G170512-10P-301_icephys.nwb 528741648
sub-G170512/sub-G170512_ses-G170512-2P-820_icephys.nwb 485466208
sub-G170512/sub-G170512_ses-G170512-6P-192_icephys.nwb 460268432
sub-G171211/sub-G171211_ses-G171211-473_icephys.nwb 409802376
sub-G180710/sub-G180710_ses-G180710-575_icephys.nwb 402883896
['sub-G220908/sub-G220908_ses-G220908-3p-181_icephys.nwb']
['sub-G220922/sub-G220922_ses-G220922-4p-599_icephys.nwb', 'sub-G220922/sub-G220922_ses-G220922-3p-607_icephys.nwb', 'sub-G220922/sub-G220922_ses-G220922-3p-489_icephys.nwb', 'sub-G220922/sub-G220922_ses-G220922-3p-223_icephys.nwb', 'sub-G220922/sub-G220922_ses-G220922-2p-622_icephys.nwb', 'sub-G220922/sub-G220922_ses-G220922-2p-414_icephys.nwb', 'sub-G220922/sub-G220922_ses-G220922-2p-436_icephys.nwb', 'sub-G220922/sub-G220922_ses-G220922-1p-268_icephys.nwb', 'sub-G220922/sub-G220922_ses-G220922-4p-790_icephys.nwb', 'sub-G220922/sub-G220922_ses-G220922-4p-793_icephys.nwb', 'sub-G220922/sub-G220922_ses-G220922-2p-55_icephys.nwb', 'sub-G220922/sub-G220922_ses-G220922-4p-765_icephys.nwb', 'sub-G220922/sub-G220922_ses-G220922-3p-364_icephys.nwb', 'sub-G220922/sub-G220922_ses-G220922-4p-569_icephys.nwb', 'sub-G220922/sub-G220922_ses-G220922-2p-425_icephys.nwb', 'sub-G220922/sub-G220922_ses-G220922-3p-307_icephys.nwb', 'sub-G220922/sub-G220922_ses-G220922-4p-545_icephys.nwb', 'sub-G220922/sub-G220922_ses-G220922-3p-150_icephys.nwb']
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; . env/bin/activate; python - <<'EOF'
from peek import *
import numpy as np, collections
for p in ['G170512-10P-301','G220908-3p-181']:
    x=[x for x in a if p in x['path']][0]
    f=h5py.File(remfile.File(url(x)),'r')
    print('==',x['path'])
    for k in ['general/notes','general/surgery','general/subject/age','general/subject/sex','general/subject/weight']: print(k, dec(f[k]))
    at=f['analysis/analysis_table']; print({c:dec(at[c][:]) for c in at.keys()})
    sr=f['general/intracellular_ephys/sequential_recordings']
    st=[dec(s) for s in sr['stimulus_type'][:]]
    print(collections.Counter(s.split('_')[0] for s in st), st[:5], st[-5:])
    stim=f['general/intracellular_ephys/intracellular_recordings/stimuli']
    en=[dec(s) for s in stim['experiment_name'][:]]
    print(collections.Counter(en))
    print(collections.Counter(dec(s) for s in stim['stimtype'][:]))
    print('stim', f['stimulus/presentation/stimulus/data'].shape, dict(f['stimulus/presentation/stimulus'].attrs).get('description'))
    tags=[dec(t) for t in f['units/tag'][:]]
    idx=f['units/spike_times_index'][:]; stt=f['units/spike_times'][:]
    print(len(tags), tags[:3], 'spikes', len(stt), stt[:10], idx[:5])
    print(list(f['stimulus'].keys()), list(f['stimulus/templates'].keys())[:5], list(f['processing'].keys()), list(f['intervals'].keys()), list(f['scratch'].keys()))
    print(list(f['acquisition'].keys())[:3], f['acquisition'][list(f['acquisition'].keys())[0]]['starting_time'][()])
EOF
```

```
== sub-G170512/sub-G170512_ses-G170512-10P-301_icephys.nwb
general/notes ABR: stimulus: Chirp, 0.3-10 kHz, 4.2 ms; threshold (db SPL): 
general/surgery anesthesia drugs: ketamine/xylazine, oxygen: yes
general/subject/age P264D
general/subject/sex F
general/subject/weight 6.110000e+01g
{'experiment': array([b'BF', b'PH', b'RLF', b'NOISE', b'SPS'], dtype=object), 'id': array([0, 1, 2, 3, 4]), 'results_bf': array([1239.,   nan,   nan,   nan,   nan]), 'results_sr': array([ 0., nan,  0., nan, nan]), 'results_threshold': array([        nan,         nan, 35.67302685,         nan,         nan])}
Counter({'RLF': 29, 'BF': 24, 'SPS': 16, 'PH': 7, 'NOISE': 2}) ['BF_FREQ400', 'BF_FREQ450', 'BF_FREQ500', 'BF_FREQ550', 'BF_FREQ600'] ['SPS_Schroeder_phase_f0_200_c_025', 'SPS_Schroeder_phase_f0_400_c_1', 'SPS_Schroeder_phase_f0_400_c_075', 'SPS_Schroeder_phase_f0_400_c_05', 'SPS_Schroeder_phase_f0_400_c_025']
Counter({'SPS': 480, 'RLF': 290, 'PH': 280, 'BF': 120, 'NOISE': 120})
Counter({'TONE': 690, '': 600})
stim (2,) acoustic stimulus, presentation: closed field, speaker:IE 800
1290 ['BF_FREQ400_rep1', 'BF_FREQ400_rep2', 'BF_FREQ400_rep3'] spikes 38166 [       nan 0.01185792 0.02146304 0.06242304 0.06346752        nan
        nan        nan        nan        nan] [1 5 6 7 8]
['presentation', 'templates'] [] [] [] []
['BF_FREQ1000_rep1', 'BF_FREQ1000_rep2', 'BF_FREQ1000_rep3'] 0.0
== sub-G220908/sub-G220908_ses-G220908-3p-181_icephys.nwb
general/notes ABR: stimulus: Chirp, 0.3-10 kHz, 4.2 ms; threshold (db SPL): 
general/surgery anesthesia drugs: ketamine/xylazine, oxygen: yes
general/subject/age P112D
general/subject/sex F
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR; curl -s -m 20 https://zenodo.org/api/records/10370064 | python -c "import json,sys;d=json.load(sys.stdin);print(d['metadata']['title']);[print(f['key'],f['size'],f['links']['self']) for f in d['files']]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/code; cd $TMPDIR/code; for f in check_dataset_metadata.m check_dataset_units.m PHextract_func.m TytoView_calcVS.m CFextract_func.m Clickextract_func.m getFSL2bins.m checkAN.m SRextract_func.m RLFextract_func.m getDrivenRatesRLF.m getSpikeCounts.m BFextract_func.m; do curl -s -o $f https://zenodo.org/api/records/10370064/files/$f/content; done; ls -la; cat check_dataset_metadata.m
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/code; cat check_dataset_units.m | head -250
```

```
% Script to investigate the full, compressed dataset, which does not 
% contain raw waveforms. 
% Filename = 'all_AN_data.mat', variablename = 'all_exp' 
% DRYAD dataset link: https://doi.org/10.5061/dryad.qv9s4mwn4

% This script uses the full dataset to plot the analyzed outcomes of all 
% animals. 

% By: Amarins Heeringa, September 5, 2023
% Revised: March 28, 2024 - ANH


%% Load the data and prepare variables

clear; close all

% load the all_AN_data.mat file
[file, path] = uigetfile('*_data.mat','Select the all_AN_data.mat file ...');
load(strcat(path,file))

[... 232 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code; sed -n 250,500p check_dataset_units.m | grep -v "^\s*$" | grep -iv "set(gca\|xlabel\|ylabel\|xlim\|ylim\|box off\|legend\|title"
```

```
end
% plot the data
figure;
scatter(srs(yo),thr(yo),sz-40,'k',yo_sym,'filled')
hold on
plot(SRra(11:end),THra(11:end),'color','r','linewidth',3)
%% SR vs BF - Fig 6C
% set limitations and ticks of the two axes
xl = [0.3 20];
yl = [0 200];
xt = [0.2 0.5 1 2 5 10 20];
% plot the data
figure
plot([3.5 3.5],yl,'--','LineWidth',3,'Color',[0,78,158]/256)
hold on
scatter(bfs(yo)/1000,srs(yo),sz,'k',yo_sym, 'LineWidth', 1)
text(3.9,190,'BF > 3.5 kHz','Color',[0,78,158]/256,'FontSize',19)
%% BF vs phase locking - Fig 6D
% set limitations and ticks of the two axes
xl = [0.3 6]; 
[... 142 more lines not kept]
```

**Agent**

Now the analysis functions the recomputations would need (PH, CF, CLICK, checkAN).

**Agent calls Bash**

```bash
cd $TMPDIR/code; for f in PHextract_func.m TytoView_calcVS.m; do echo "=== $f"; grep -v "^\s*$" $f | grep -v "^\s*%" ; done
```

```
=== PHextract_func.m
function [freq, lvlVec, vs, prob, vsVec, pVec, erVec, msp] = PHextract_func(curvedata, curvesettings)
tlen = curvesettings.stim.Duration; 
dur = curvesettings.tdt.AcqDuration; 
StartTime = curvesettings.stim.Delay;
EndTime = StartTime + tlen;
binSize = 0.001; % set binsize for PSTH
tmpfreq = sort(unique(vertcat(curvesettings.stimcache.Freq{:})));
if curvesettings.curve.Spont
    freq = tmpfreq(2); % tmpfreq(1) should be spont (-99999)
else
    freq = tmpfreq(1);
end
tmplvl = sort(unique(vertcat(curvesettings.stimcache.ABI(:))));
if curvesettings.curve.Spont
    lvlVec = tmplvl(2:end);
else
    lvlVec = tmplvl;
end
x1 = curvedata.depvars_sort(:,1,1);
[... 239 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code; for f in CFextract_func.m Clickextract_func.m getFSL2bins.m checkAN.m SRextract_func.m; do echo "=== $f"; grep -v "^\s*$" $f | grep -v "^\s*%" | grep -iv "xlabel\|ylabel\|title(\|set(gca\|xlim\|ylim\|box on\|hold on\|legend" ; done
```

```
=== CFextract_func.m
function [CF, thr, Q10, msp] = CFextract_func(curvedata, curvesettings)
[~,~,~,~,nwSpikRat]=getSpikeCounts(curvedata,curvesettings);
x1 = curvedata.depvars_sort(:,1,1);
x2 = curvedata.depvars_sort(:,1,2);
y = nwSpikRat;
m1 = mean(y,2);  % average wrt 2nd index
s1 = std(y,1,2); % std wrt 2nd index 
j = (curvedata.isspont(:,1)==0); % find out non-spont trials
jsp = (curvedata.isspont(:,1)==1); % find out spont trials
msp = m1(jsp);
ssp = s1(jsp);
if curvesettings.stimcache.nloopvars == 2 
    v1 = sort(unique(x1(j)));
    v2 = sort(unique(x2(j)));
    m = zeros(length(v1),length(v2));
    s = zeros(length(v1),length(v2));
    for i2 = 1:length(v2)
        m(:,i2) = m1( x2==v2(i2) );
        s(:,i2) = s1( x2==v2(i2) );
[... 234 more lines not kept]
```

**Agent**

Plan is clear. Next: a survey loader that reads only metadata, the analysis table, the trial table and spike times (no voltage traces). Timing it on a subset first.

**Agent calls Bash**

```bash
mkdir -p entries/001262-heeringa-2024; cd $TMPDIR; . env/bin/activate; cat > survey_test.py <<'EOF'
import json,h5py,remfile,time,requests,numpy as np,collections
from concurrent.futures import ThreadPoolExecutor
a=json.load(open('assets.json'))
def dec(v):
    v=v[()] if hasattr(v,'shape') and not isinstance(v,np.ndarray) else v
    return v.decode() if isinstance(v,bytes) else v
def read(x):
    t=time.time()
    u=f"https://api.dandiarchive.org/api/assets/{x['asset_id']}/download/"
    s3=requests.head(u,allow_redirects=True).url
    f=h5py.File(remfile.File(s3),'r')
    st=f['general/intracellular_ephys/intracellular_recordings/stimuli']
    d=dict(path=x['path'])
    d['exp']=[dec(v) for v in st['experiment_name'][:]]
    d['tags']=[dec(v) for v in f['units/tag'][:]]
    d['lvl_idx']=st['level_dBSPL_index'][:]
    d['nlvl']=len(st['level_dBSPL'])
    sp=f['units/spike_times'][:]; idx=f['units/spike_times_index'][:]
    d['nsp']=len(sp)
    at=f['analysis/analysis_table']; d['an']=[dec(v) for v in at['experiment'][:]]
    d['bf']=at['results_bf'][:]; d['notes']=dec(f['general/notes'][()])
    d['t']=time.time()-t
    return d
import random; random.seed(1); sub=random.sample(a,24)
t=time.time()
with ThreadPoolExecutor(12) as ex: res=list(ex.map(read,sub))
print('wall',time.time()-t)
for d in res: print(d['path'].split('/')[1][:40], round(d['t'],1), collections.Counter(d['exp']), d['an'], d['nlvl'], len(d['lvl_idx']), d['nsp'], d['notes'][-30:])
EOF
python survey_test.py
```

```
wall 28.444788932800293
sub-G171023_ses-G171023-3P-807_icephys.n 14.6 Counter({'PH': 200, 'BF': 85, 'NOISE': 60}) ['BF', 'PH', 'NOISE'] 345 345 16470  4.2 ms; threshold (db SPL): K
sub-G151203_ses-G151203-3P-755nm_icephys 14.4 Counter({'CLICK': 500, 'CF': 408, 'PH': 320, 'RLF': 250, 'BF': 160}) ['BF', 'CF', 'PH', 'CLICK', 'RLF'] 1638 1638 11507 .2 ms; threshold (db SPL): NaN
sub-G190617_ses-G190617-3p-65_icephys.nw 12.6 Counter({'RLF': 250, 'BF': 100}) ['BF', 'RLF'] 350 350 2840  4.2 ms; threshold (db SPL): 
sub-G170512_ses-G170512-3P-863_icephys.n 14.4 Counter({'RLF': 290, 'BF': 95, 'SPS': 60}) ['BF', 'RLF', 'SPS'] 445 445 9416  4.2 ms; threshold (db SPL): 
sub-G220901_ses-G220901-1p-314_icephys.n 14.4 Counter({'RLF': 250, 'BF': 110}) ['BF', 'RLF'] 360 360 3857  4.2 ms; threshold (db SPL): 
sub-G211221_ses-G211221-2p-354_icephys.n 14.6 Counter({'BF': 60}) ['BF'] 60 60 131  4.2 ms; threshold (db SPL): 2
sub-G220301_ses-G220301-1p-221_icephys.n 14.4 Counter({'RLF': 250, 'BF': 75}) ['BF', 'RLF'] 325 325 3476  4.2 ms; threshold (db SPL): 

sub-G201001_ses-G201001-3p-863_icephys.n 14.6 Counter({'RLF': 190, 'CVC': 120, 'BF': 60}) ['BF', 'RLF', 'CVC'] 370 370 19041  4.2 ms; threshold (db SPL): -
sub-G190411_ses-G190411-37_icephys.nwb 14.6 Counter({'CLICK': 500, 'RLF': 220, 'BF': 70, 'NOISE': 60}) ['BF', 'CLICK', 'RLF', 'NOISE'] 850 850 23338  4.2 ms; threshold (db SPL): 
sub-G160817_ses-G160817-2P-504_icephys.n 21.9 Counter({'BF': 260}) ['BF'] 260 260 3171  4.2 ms; threshold (db SPL): #
sub-G220609_ses-G220609-1p-577_icephys.n 14.6 Counter({'CLICK': 300, 'RLF': 190, 'CVC': 120, 'BF': 110, 'SR': 10}) ['BF', 'CLICK', 'RLF', 'SR', 'CVC'] 730 730 18407  4.2 ms; threshold (db SPL): (
sub-G151001_ses-G151001-1P-692nm_icephys 14.4 Counter({'RLF': 290, 'BF': 170, 'PH': 140}) ['BF', 'PH', 'RLF'] 600 600 10985 .2 ms; threshold (db SPL): NaN
sub-G201103_ses-G201103-2p-46_icephys.nw 11.9 Counter({'CLICK': 300, 'RLF': 250, 'BF': 120, 'SR': 10}) ['BF', 'CLICK', 'RLF', 'SR'] 680 680
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . env/bin/activate; python - <<'EOF'
from peek import *
import numpy as np
for p in ['G151203-3P-755nm','G171023-3P-807','G220609-1p-577','G211221-2p-354','G160817-2P-504']:
    x=[x for x in a if p in x['path']][0]
    f=h5py.File(remfile.File(url(x)),'r')
    at=f['analysis/analysis_table']
    print(p, {c:at[c][:] for c in at.keys() if c!='id'})
    n=f['general/notes'][()]
    print(repr(n), [ord(c) for c in n.decode()[-3:]] if isinstance(n,bytes) else None)
    stim=f['general/intracellular_ephys/intracellular_recordings/stimuli']
    en=np.array([dec(s) for s in stim['experiment_name'][:]])
    for e in sorted(set(en)):
        m=en==e
        print('  ',e, 'freqs',np.unique(stim['frequency'][:][m])[:6], 'lv', np.unique(np.round(stim['level_dBSPL'][:][m],1))[:8], 'delay',np.unique(stim['delay'][:][m]), 'dur',np.unique(stim['duration'][:][m]), 'pol',set(dec(s) for s in stim['click_polarity'][:][m]), 'stimtype', set(dec(s) for s in stim['stimtype'][:][m]))
EOF
```

```
G151203-3P-755nm {'experiment': array([b'BF', b'CF', b'PH', b'CLICK', b'RLF'], dtype=object), 'results_bf': array([1559.,   nan,   nan,   nan,   nan]), 'results_sr': array([52.5, 80. ,  nan,  nan, 82.5]), 'results_threshold': array([        nan, 29.78178203,         nan,         nan, 18.78178203])}
b'ABR: stimulus: Chirp, 0.3-10 kHz, 4.2 ms; threshold (db SPL): NaN' [78, 97, 78]
   BF freqs [-99999.   1000.   1050.   1100.   1150.   1200.] lv [-9.9999e+04  2.9800e+01] delay [0.00775] dur [0.05] pol {''} stimtype {'TONE'}
   CF freqs [-99999.   1000.   1200.   1400.   1600.   1800.] lv [-9.9999e+04  9.8000e+00  1.4800e+01  1.9800e+01  2.4800e+01  2.9800e+01
  3.4800e+01  3.9800e+01] delay [0.00775] dur [0.05] pol {''} stimtype {'TONE'}
   CLICK freqs [nan] lv [nan] delay [nan] dur [nan] pol {'COND'} stimtype {'CLICK'}
   PH freqs [1600.] lv [ 9.8 19.8 29.8 39.8 49.8 59.8 69.8 79.8] delay [0.00775] dur [0.05] pol {''} stimtype {'TONE'}
   RLF freqs [-99999.   1600.] lv [-9.9999e+04  9.8000e+00  1.2800e+01  1.4800e+01  1.5800e+01  1.8800e+01
  1.9800e+01  2.1800e+01] delay [0.00775] dur [0.05] pol {''} stimtype {'TONE'}
G171023-3P-807 {'experiment': array([b'BF', b'PH', b'NOISE'], dtype=object), 'results_bf': array([4091.,   nan,   nan]), 'results_sr': array([ 0., nan, nan]), 'results_threshold': array([nan, nan, nan])}
b'ABR: stimulus: Chirp, 0.3-10 kHz, 4.2 ms; threshold (db SPL): K' [58, 32, 75]
   BF freqs [-99999.   2700.   2800.   2900.   3000.   3100.] lv [-9.9999e+04  7.1400e+01] delay [0.00775] dur [0.05] pol {''} stimtype {'TONE'}
   NOISE freqs [nan] lv [91.7] delay [nan] dur [3.038] pol {''} stimtype {''}
   PH freqs [4100.] lv [56.4 66.4 76.4 86.4 96.4] delay [0.00775] dur [0.05] pol {''} stimtype {'TONE'}
G220609-1p-577 {'experiment': array([b'BF', b'CLICK', b'RLF', b'SR', b'CVC'], dtype=object), 'results_bf': array([5361.,   nan,   nan,   nan,   nan]), 'results_sr': array([62.5       ,         nan, 78.75      , 75.20672892,         nan]), 'results_thresh
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . env/bin/activate; python - <<'EOF'
from peek import *
import numpy as np
x=[x for x in a if 'G220609-1p-577' in x['path']][0]
f=h5py.File(remfile.File(url(x)),'r')
tags=[dec(t) for t in f['units/tag'][:]]
sp=f['units/spike_times'][:]; idx=f['units/spike_times_index'][:]
starts=np.r_[0,idx[:-1]]
ck=[i for i,t in enumerate(tags) if t.startswith('CLICK')]
print(tags[ck[0]], tags[ck[-1]], len(ck))
allsp=np.concatenate([sp[starts[i]:idx[i]] for i in ck]); allsp=allsp[~np.isnan(allsp)]
print(len(allsp), allsp.min(), allsp.max())
h,e=np.histogram(allsp,bins=np.arange(0,0.03,0.0002))
for i in range(0,60): print(round(e[i]*1000,2), h[i], end='; ')
print()
acq=[k for k in f['acquisition'].keys() if k.startswith('CLICK')][:2]
for k in acq:
    g=f['acquisition'][k]; print(k, g['data'].shape, dict(g['starting_time'].attrs), dict(g.attrs).get('description'), dict(g.attrs).get('stimulus_description'))
d=f['acquisition'][acq[0]]['data'][:]
print(np.round(d[:400:10]*1e3,3))
print(f['stimulus/presentation/stimulus/data'].shape)
sr=[i for i,t in enumerate(tags) if t.startswith('SR')]; print([tags[i] for i in sr][:3], len(sr))
g=f['acquisition'][[k for k in f['acquisition'].keys() if k.startswith('SR')][0]]; print(g['data'].shape)
stim=f['general/intracellular_ephys/intracellular_recordings/stimuli']
en=np.array([dec(s) for s in stim['experiment_name'][:]])
print([dec(s) for s in f['general/intracellular_ephys/sequential_recordings/stimulus_type'][:]])
print('isi',np.unique(stim['isi'][:][en=='CLICK']), 'pres', stim['presentation_number'][:][en=='CLICK'][:10])
EOF
```

```
CLICK_CLICK_rep1 CLICK_CLICK_rep300 300
548 0.00016384 0.01972224
0.0 3; 0.2 4; 0.4 8; 0.6 3; 0.8 3; 1.0 6; 1.2 7; 1.4 2; 1.6 5; 1.8 6; 2.0 3; 2.2 6; 2.4 2; 2.6 4; 2.8 7; 3.0 7; 3.2 4; 3.4 1; 3.6 4; 3.8 4; 4.0 2; 4.2 2; 4.4 3; 4.6 7; 4.8 4; 5.0 3; 5.2 5; 5.4 3; 5.6 3; 5.8 3; 6.0 4; 6.2 3; 6.4 7; 6.6 4; 6.8 3; 7.0 6; 7.2 4; 7.4 2; 7.6 4; 7.8 8; 8.0 6; 8.2 8; 8.4 4; 8.6 55; 8.8 89; 9.0 40; 9.2 10; 9.4 14; 9.6 9; 9.8 11; 10.0 5; 10.2 1; 10.4 0; 10.6 1; 10.8 1; 11.0 1; 11.2 0; 11.4 1; 11.6 4; 11.8 4; 
CLICK_CLICK_rep1 (976,) {'rate': np.float64(48828.125), 'unit': 'seconds'} recorded voltage trace N/A
CLICK_CLICK_rep10 (976,) {'rate': np.float64(48828.125), 'unit': 'seconds'} recorded voltage trace N/A
[   0.       3.111    1.088  -17.141   11.356  -93.084  -36.668  -65.025
 -104.925  -97.098 -112.651  -99.694 -105.19     9.301  119.448    7.105
  -84.948 -118.238 -122.919 -121.571  -55.809  -42.677   29.264  -12.981
   29.647   47.941   49.572   71.702   43.459   84.403  156.651  119.842
  111.831  112.738  128.003  130.461  115.892   74.779   64.288   36.576]
(2,)
['SR_EXTERN_rep1', 'SR_EXTERN_rep2', 'SR_EXTERN_rep3'] 10
(117190,)
['BF_FREQ4000', 'BF_FREQ4150', 'BF_FREQ4300', 'BF_FREQ4450', 'BF_FREQ4600', 'BF_FREQ4750', 'BF_FREQ4900', 'BF_FREQ5050', 'BF_FREQ5200', 'BF_FREQ5350', 'BF_FREQ5500', 'BF_FREQ5650', 'BF_FREQ5800', 'BF_FREQ5950', 'BF_FREQ6100', 'BF_FREQ6250', 'BF_FREQ6400', 'BF_FREQ6550', 'BF_FREQ6700', 'BF_FREQ6850', 'BF_FREQ7000', 'BF_silent', 'CLICK_CLICK', 'RLF_ABI30', 'RLF_ABI33', 'RLF_ABI36', 'RLF_ABI39', 'RLF_ABI42', 'RLF_ABI45', 'RLF_ABI48', 'RLF_ABI51', 'RLF_ABI54', 'RLF_ABI57', 'RLF_ABI60', 'RLF_ABI63', 'RLF_ABI66', 'RLF_ABI69', 'RLF_ABI72', 'RLF_ABI75', 'RLF_ABI78', 'RLF_ABI81', 'RLF_silent', 'SR_EXTERN', 'CVC_behb_S01F_2_5SNR_pilot2_A_dB_SPL', 'CVC_behb_S01F_2_5SNR_pilot2_P_dB_SPL']
isi [nan] pres [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/code; curl -s -o getQ10dB.m https://zenodo.org/api/records/10370064/files/getQ10dB.m/content; for f in getSpikeCounts.m getQ10dB.m RLFextract_func.m; do echo "=== $f"; grep -v "^\s*$" $f | grep -v "^\s*%" | grep -iv "xlabel\|ylabel\|title(\|set(gca\|xlim\|ylim\|box on\|hold on\|legend\|plot\|errorbar\|text(" ; done; date -u
```

Result: the fetched text is not kept.

**Agent**

I have what I need from the code. Writing the helper module (loader plus the recomputations that follow the paper's MATLAB functions).

**Agent calls Write**

```json
{
 "file_path": "entries/001262-heeringa-2024/gerbil_an.py",
 "content": "\"\"\"Loading and measures for dandiset 001262, single auditory nerve fibres of gerbils.\n\nHeeringa (2024), Scientific Data 11, 411, doi:10.1038/s41597-024-03259-3.\n\nEach NWB file holds one single unit (fibre) of one gerbil. A file holds, per trial, the spike\ntimes (`units`, one row per trial, tagged `<TYPE>_<condition>_rep<n>`), the trial's stimulus\n(`intracellular_recordings/stimuli`: recording type, frequency, level, delay, duration), the raw\nvoltage trace (`acquisition`, not read here), and a small analysis table with one row per\nrecording type (`results_bf`, `results_sr`, `results_threshold`). Animal metadata are in\n`general/subject` (age, sex, weight), `general/surgery` (oxygen) and `general/notes` (ABR).\nFiles are streamed from the archive at the pinned version; nothing is written to disk. The\nvoltage traces are not read: no claim tested here needs them.\n\nWhere the parameters come from:\n\n- Age groups: young adult <= 365 days, middle aged > 365 and <= 1095, old > 1095; months are\n  days / (365/12). Claims file, from check_dataset_metadata.m and check_dataset_units.m\n  (Zenodo 10.5281/zenodo.10370064).\n- Best estimate of spontaneous rate: the SR recording, else PH, else RLF, else BF (claims file,\n  from check_dataset_units.m; Methods, \"Calculating spike rate\": \"For units without data in the\n  'SR' field, the author advises choosing ... the PH recording ..., followed by the RLF\n  recording\"). Low-SR is SR < 18 spikes/s (Fig. 6d legend).\n- `vector_strength_by_level` follows PHextract_func.m and TytoView_calcVS.m (Zenodo record\n  above), which the Methods name (\"The analysis procedures were carried out by the function\n  PHextract_func.m\"): spikes between stimulus onset and offset (strict inequalities), pooled\n  over the repetitions of a level; vs = |mean(exp(i 2 pi f t))|; p = exp(-N vs^2); p is NaN\n  when N <= 50 (the code's `ntot > 50`; the Methods say \"When N < 50, the p-value is NaN\").\n  Significant when p < 0.001 (Methods). The silent trials are left out (the code also computes\n  a value for them; it is not a tone level).\n- `cf_from_cf_recording` follows CFextract_func.m, getSpikeCounts.m and getQ10dB.m, which the\n  Methods name: rates in the stimulus window per trial, mean over repetitions per frequency and\n  level; response criterion T = mean + 1.2 x SD (population SD, `std(y,1,2)`) of the rates of\n  the silent trials, and also above 15 spikes/s; a frequency's threshold is the lower level of\n  the first pair of adjacent suprathreshold levels, or the only suprathreshold level; CF is the\n  mean of the frequencies at the lowest threshold. The code then asks the experimenter to accept\n  T and the CF or type new ones (\"T could be manually adjusted when needed\", Methods); those\n  manual choices are not in the dataset, so this is the automatic first pass only.\n- `click_latency_2bins` follows Clickextract_func.m and getFSL2bins.m, named by the Methods:\n  only recordings with more than 75 spikes are analysed; the PSTH of all spikes has\n  round(trial duration / 0.05 ms) bins spanning the first to the last spike (MATLAB `hist`);\n  the reference is the largest bin before the click, leaving out the first 10 bins; the\n  latency is the centre of the first of two consecutive bins after the click that exceed it,\n  minus the click delay. The click delay is not in the files (the trial table gives NaN), so it\n  is a parameter: `CLICK_DELAY_S` is an assumption, the 7.75 ms delay that every tone recording\n  in the dataset uses, and the notebook shows another value.\n- Inter-spike intervals: within a trial, between successive spike times, as checkAN.m computes\n  them (`diff(spT)` per trial); the 0.6 ms limit is the Technical Validation's.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport re\nimport time\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nimport requests\n\nDANDISET_ID = \"001262\"\nDANDISET_VERSION = \"0.241205.0959\"\nAPI = \"https://api.dandiarchive.org/api\"\n\nYOUNG_MAX_DAYS = 365\nMIDDLE_MAX_DAYS = 3 * 365\nDAYS_PER_MONTH = 365 / 12\nLOW_SR_CUTOFF = 18.0          # spikes/s, Fig. 6d legend\nVS_P_SIGNIFICANT = 0.001      # Methods\nVS_MIN_SPIKES = 50            # TytoView_calcVS.m: p only when N > 50\nCF_SD_FACTOR = 1.2            # Methods and CFextract_func.m\nCF_MIN_RATE = 15.0            # CFextract_func.m (m > 15)\nCLICK_MIN_SPIKES = 75         # Clickextract_func.m\nCLICK_BIN_S = 0.00005         # 0.05 ms, Methods\nCLICK_DELAY_S = 0.00775       # assumption, see the module docstring\nSHORT_ISI_S = 0.0006          # Technical Validation\nSPONT = -99999.0              # frequency and level of silent trials\n\n\ndef age_group(days):\n    if days <= YOUNG_MAX_DAYS:\n        return \"young\"\n    if days <= MIDDLE_MAX_DAYS:\n        return \"middle\"\n    return \"old\"\n\n\ndef list_assets(version=DANDISET_VERSION):\n    \"\"\"Assets of the pinned version: path, asset id, blob id and size.\"\"\"\n    out, url = [], f\"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/?page_size=1000\"\n    while url:\n        page = requests.get(url, timeout=60).json()\n        out += page[\"results\"]\n        url = page[\"next\"]\n    return pd.DataFrame([{\"path\": a[\"path\"], \"asset_id\": a[\"asset_id\"], \"blob\": a.get(\"blob\"),\n                          \"size\": a[\"size\"]} for a in out])\n\n\ndef blob_url(blob):\n    return f\"https://dandiarchive.s3.amazonaws.com/blobs/{blob[:3]}/{blob[3:6]}/{blob}\"\n\n\ndef _s(v):\n    if isinstance(v, np.ndarray) and v.shape == ():\n        v = v[()]\n    if isinstance(v, bytes):\n        return v.decode(\"utf-8\", \"surrogateescape\")\n    return v\n\n\ndef read_unit(asset):\n    \"\"\"Read one file's metadata, analysis table, trial table and spike times (no traces).\"\"\"\n    with h5py.File(remfile.File(blob_url(asset[\"blob\"])), \"r\") as f:\n        g = f[\"general\"]\n        d = {\"path\": asset[\"path\"], \"blob\": asset[\"blob\"], \"size\": asset[\"size\"]}\n        for key, name in [(\"subject_id\", \"subject/subject_id\"), (\"age\", \"subject/age\"),\n                          (\"sex\", \"subject/sex\"), (\"weight\", \"subject/weight\"),\n                          (\"species\", \"subject/species\"), (\"notes\", \"notes\"),\n                          (\"surgery\", \"surgery\"), (\"session_id\", \"session_id\")]:\n            d[key] = _s(g[name][()]) if name in g else None\n        d[\"identifier\"] = _s(f[\"identifier\"][()])\n        d[\"session_start\"] = _s(f[\"session_start_time\"][0])\n        d[\"stimulus_description\"] = _s(f[\"stimulus/presentation/stimulus\"].attrs.get(\"description\"))\n        at = f[\"analysis/analysis_table\"]\n        d[\"analysis\"] = pd.DataFrame({\n            \"experiment\": [_s(v) for v in at[\"experiment\"][:]],\n            \"bf\": at[\"results_bf\"][:], \"sr\": at[\"results_sr\"][:],\n            \"threshold\": at[\"results_threshold\"][:]})\n        st = f[\"general/intracellular_ephys/intracellular_recordings/stimuli\"]\n        lv, lvi = st[\"level_dBSPL\"][:], st[\"level_dBSPL_index\"][:]\n        lv_start = np.r_[0, lvi[:-1]]\n        first_level = np.array([lv[a] if b > a else np.nan for a, b in zip(lv_start, lvi)])\n        n_levels = lvi - lv_start\n        tags = [_s(v) for v in f[\"units/tag\"][:]]\n        trials = pd.DataFrame({\n            \"tag\": tags,\n            \"experiment\": [_s(v) for v in st[\"experiment_name\"][:]],\n            \"frequency\": st[\"frequency\"][:], \"level\": first_level, \"n_levels\": n_levels,\n            \"delay\": st[\"delay\"][:], \"duration\": st[\"duration\"][:],\n            \"click_polarity\": [_s(v) for v in st[\"click_polarity\"][:]],\n        })\n        d[\"sequential_types\"] = [_s(v) for v in\n                                 f[\"general/intracellular_ephys/sequential_recordings/stimulus_type\"][:]]\n        sp = f[\"units/spike_times\"][:]\n        idx = f[\"units/spike_times_index\"][:]\n        starts = np.r_[0, idx[:-1]]\n        spikes = [sp[a:b] for a, b in zip(starts, idx)]\n        d[\"n_nan_spikes\"] = int(sum(np.isnan(s).sum() for s in spikes))\n        d[\"spikes\"] = [s[~np.isnan(s)] for s in spikes]\n        trials[\"n_spikes\"] = [len(s) for s in d[\"spikes\"]]\n        # trial length per recording type, from the shape of its first voltage trace\n        acq = f[\"acquisition\"]\n        trial_s = {}\n        for exp in trials.experiment.unique():\n            tag = trials.tag[trials.experiment == exp].iloc[0]\n            if tag in acq:\n                ser = acq[tag]\n                rate = ser[\"starting_time\"].attrs[\"rate\"]\n                trial_s[exp] = ser[\"data\"].shape[0] / rate\n        trials[\"trial_s\"] = trials.experiment.map(trial_s)\n        d[\"acq_rate\"] = float(acq[tags[0]][\"starting_time\"].attrs[\"rate\"]) if tags[0] in acq else np.nan\n        d[\"acq_unit\"] = _s(acq[tags[0]][\"data\"].attrs.get(\"unit\")) if tags[0] in acq else None\n        d[\"trials\"] = trials\n    return d\n\n\ndef load_all(assets, threads=32, retries=3):\n    \"\"\"Read every file in `assets` (a DataFrame from list_assets) with a thread pool.\"\"\"\n    def one(row):\n        for attempt in range(retries):\n            try:\n                return read_unit(row)\n            except Exception as err:  # network errors: retry\n                last = err\n                time.sleep(2 * (attempt + 1))\n        raise last\n    rows = [r for _, r in assets.iterrows()]\n    with ThreadPoolExecutor(threads) as ex:\n        return list(ex.map(one, rows))\n\n\n# --- metadata parsing --------------------------------------------------------------------\n\ndef age_days(age):\n    m = re.fullmatch(r\"P(\\d+(?:\\.\\d+)?)D\", age or \"\")\n    return float(m.group(1)) if m else np.nan\n\n\ndef weight_g(weight):\n    m = re.fullmatch(r\"\\s*([0-9.eE+-]+)\\s*g\\s*\", weight or \"\")\n    return float(m.group(1)) if m else np.nan\n\n\ndef oxygen(surgery):\n    m = re.search(r\"oxygen:\\s*(\\w+)\", surgery or \"\")\n    return m.group(1) if m else None\n\n\ndef speaker(stimulus_description):\n    m = re.search(r\"speaker:\\s*(.+)$\", stimulus_description or \"\")\n    return m.group(1).strip() if m else None\n\n\ndef abr_field(notes):\n    \"\"\"The text after 'threshold (db SPL): ' in the notes.\"\"\"\n    m = re.search(r\"threshold \\(db SPL\\): (.*)$\", notes or \"\", flags=re.S)\n    return m.group(1) if m else None\n\n\ndef abr_decoded(field):\n    \"\"\"The ABR field holds one character whose code point is the threshold (see notebook).\n\n    Returns the code point of a single character, NaN for 'NaN' or an empty field.\n    \"\"\"\n    if field is None or field == \"\" or field == \"NaN\":\n        return np.nan\n    if len(field) == 1:\n        return float(ord(field))\n    try:\n        return float(field)\n    except ValueError:\n        return np.nan\n\n\n# --- measures from spike times ------------------------------------------------------------\n\ndef trials_of(unit, experiment):\n    t = unit[\"trials\"]\n    idx = np.flatnonzero(t.experiment.values == experiment)\n    return t.iloc[idx], [unit[\"spikes\"][i] for i in idx]\n\n\ndef vs_calc(spike_times_s, freq):\n    \"\"\"TytoView_calcVS.m: vector strength and p (NaN when N <= 50).\"\"\"\n    n = len(spike_times_s)\n    if n == 0:\n        return np.nan, np.nan, 0\n    ph = 2 * np.pi * freq * spike_times_s\n    vs = float(np.hypot(np.cos(ph).mean(), np.sin(ph).mean()))\n    p = float(np.exp(-n * vs * vs)) if n > VS_MIN_SPIKES else np.nan\n    return vs, p, n\n\n\ndef vector_strength_by_level(unit):\n    \"\"\"PHextract_func.m: vector strength and p per tone level of the PH recording.\"\"\"\n    t, sp = trials_of(unit, \"PH\")\n    if len(t) == 0:\n        return None\n    tone = t.frequency.values != SPONT\n    freqs = np.unique(t.frequency.values[tone])\n    rows = []\n    for lvl in np.unique(t.level.values[tone]):\n        sel = np.flatnonzero(tone & (t.level.values == lvl))\n        start, dur = t.delay.values[sel[0]], t.duration.values[sel[0]]\n        s = np.concatenate([sp[i] for i in sel]) if len(sel) else np.array([])\n        s = s[(s > start) & (s < start + dur)]\n        vs, p, n = vs_calc(s, freqs[0])\n        rows.append({\"level\": lvl, \"frequency\": freqs[0], \"n_freqs\": len(freqs), \"vs\": vs, \"p\": p,\n                     \"n_spikes\": n})\n    return pd.DataFrame(rows)\n\n\ndef max_significant_vs(unit):\n    \"\"\"check_dataset_units.m: largest vs over levels with p not NaN and < 0.001.\"\"\"\n    v = vector_strength_by_level(unit)\n    if v is None:\n        return np.nan\n    ok = v.p.notna() & (v.p < VS_P_SIGNIFICANT)\n    return float(v.vs[ok].max()) if ok.any() else np.nan\n\n\ndef _rates(t, sp):\n    start, dur = t.delay.values, t.duration.values\n    return np.array([np.sum((s > a) & (s < a + d)) / d for s, a, d in zip(sp, start, dur)])\n\n\ndef cf_from_cf_recording(unit, level_from=\"tag\"):\n    \"\"\"CFextract_func.m, automatic first pass: (CF in Hz, threshold, tuning curve).\"\"\"\n    t, sp = trials_of(unit, \"CF\")\n    if len(t) == 0:\n        return np.nan, np.nan, None\n    t = t.copy()\n    t[\"rate\"] = _rates(t, sp)\n    if level_from == \"tag\":\n        # nominal attenuator level (ABI) from the tag, as the code's depvars use\n        abi = t.tag.str.extract(r\"ABI(-?\\d+(?:\\.\\d+)?)\")[0].astype(float)\n        if abi.notna().sum() == (t.frequency != SPONT).sum():\n            t[\"lv\"] = abi.where(t.frequency != SPONT, SPONT)\n        else:\n            t[\"lv\"] = t.level\n    else:\n        t[\"lv\"] = t.level\n    spont = t[t.frequency == SPONT]\n    if len(spont) == 0:\n        return np.nan, np.nan, None\n    resp = spont.rate.mean() + CF_SD_FACTOR * spont.rate.std(ddof=0)\n    m = t[t.frequency != SPONT].groupby([\"frequency\", \"lv\"]).rate.mean().unstack(\"lv\").sort_index()\n    m = m.reindex(columns=sorted(m.columns))\n    levels = np.array(m.columns, dtype=float)\n    tc = np.full(len(m), np.nan)\n    for i, row in enumerate(m.values):\n        xi = np.flatnonzero((row > resp) & (row > CF_MIN_RATE))\n        if len(xi) > 1:\n            xn = np.flatnonzero(np.diff(xi) == 1)\n            tc[i] = levels[xi[xn[0]]] if len(xn) else np.nan\n        elif len(xi) == 1:\n            tc[i] = levels[xi[0]]\n    if np.all(np.isnan(tc)):\n        return np.nan, np.nan, pd.Series(tc, index=m.index)\n    thr = np.nanmin(tc)\n    cf = float(np.mean(np.array(m.index)[tc == thr]))\n    return cf, float(thr), pd.Series(tc, index=m.index)\n\n\ndef _matlab_hist(x, nbin):\n    \"\"\"MATLAB hist(x, nbin): nbin equal bins from min(x) to max(x); returns counts, centres.\"\"\"\n    lo, hi = float(np.min(x)), float(np.max(x))\n    if hi == lo:\n        lo, hi = lo - 0.5, hi + 0.5\n    edges = np.linspace(lo, hi, nbin + 1)\n    counts, _ = np.histogram(x, edges)\n    return counts, (edges[:-1] + edges[1:]) / 2\n\n\ndef click_latency_2bins(unit, delay=CLICK_DELAY_S):\n    \"\"\"Clickextract_func.m and getFSL2bins.m on the unit's CLICK trials (seconds).\"\"\"\n    t, sp = trials_of(unit, \"CLICK\")\n    if len(t) == 0:\n        return np.nan\n    n_sp = sum(len(s) for s in sp)\n    if n_sp <= CLICK_MIN_SPIKES:\n        return np.nan\n    dur = float(t.trial_s.iloc[0])\n    nbin = int(round(dur / CLICK_BIN_S))\n    allsp = np.concatenate(sp)\n    counts, cent = _matlab_hist(allsp, nbin)\n    rate = counts / len(t) / CLICK_BIN_S\n    sfr = cent < delay\n    sfr[:10] = False\n    efr = np.flatnonzero(cent > delay)\n    thr = rate[sfr].max() if sfr.any() else 1.0\n    high = efr[rate[efr] > thr]\n    consec = np.flatnonzero(np.diff(high) == 1)\n    if len(consec) == 0:\n        return np.nan\n    return float(cent[high[consec[0]]] - delay)\n\n\ndef short_isis(unit, limit=SHORT_ISI_S):\n    \"\"\"Per recording type: number of within-trial ISIs below `limit`, and of all ISIs.\"\"\"\n    out = {}\n    t = unit[\"trials\"]\n    for exp in t.experiment.unique():\n        idx = np.flatnonzero(t.experiment.values == exp)\n        isis = [np.diff(np.sort(unit[\"spikes\"][i])) for i in idx]\n        isis = np.concatenate(isis) if isis else np.array([])\n        out[exp] = (int(np.sum(isis < limit)), len(isis))\n    return out\n\n\ndef rlf_rates(unit):\n    \"\"\"Mean and SD of the rate per level of the RLF recording (stimulus window), spont apart.\"\"\"\n    t, sp = trials_of(unit, \"RLF\")\n    if len(t) == 0:\n        return None\n    t = t.copy()\n    t[\"rate\"] = _rates(t, sp)\n    return t[t.frequency != SPONT].groupby(\"level\").rate.agg([\"mean\", \"std\", \"size\"])\n"
}
```

```
File created successfully at: entries/001262-heeringa-2024/gerbil_an.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/001262-heeringa-2024; . $TMPDIR/env/bin/activate; python - <<'EOF'
import time, gerbil_an as g, numpy as np, pandas as pd
A=g.list_assets(); print(len(A))
sub=A.sample(48, random_state=0)
t=time.time(); U=g.load_all(sub, threads=32); print('48 files', time.time()-t)
import pickle; pickle.dump(U, open(__import__('os').environ['TMPDIR']+'/sub48.pkl','wb'))
for u in U[:48]:
    t=u['trials']
    ok=all(tag.startswith(e+'_') for tag,e in zip(t.tag,t.experiment))
    vs=g.max_significant_vs(u); cf=g.cf_from_cf_recording(u)[0]; lat=g.click_latency_2bins(u)
    print(u['subject_id'], u['identifier'], u['age'], g.abr_decoded(g.abr_field(u['notes'])), ok, list(u['analysis'].experiment), 'vs',round(vs,3) if vs==vs else vs, 'cf',cf, 'lat', lat, 'bf', u['analysis'].bf.max())
EOF
```

```
1160
48 files 109.61337924003601
G201112 G201112:1p_392 P107D 15.0 True ['BF', 'RLF'] vs nan cf nan lat nan bf 7498.0
G190912 G190912:32 P1105D 35.0 True ['BF', 'CLICK', 'RLF'] vs nan cf nan lat 0.002513449600000002 bf 871.0
G220222 G220222:4p_281 P178D 15.0 True ['BF', 'RLF'] vs nan cf nan lat nan bf 13263.0
G160609 G160609:1118 P249D 15.0 True ['BF', 'PH', 'RLF'] vs 0.573 cf nan lat nan bf 1514.0
G191115 G191115:2p_381 P163D 15.0 True ['BF', 'PH', 'CLICK', 'RLF', 'SR', 'CVC'] vs 0.678 cf nan lat 0.0016494496000000018 bf 1830.0
G190704 G190704:430 P156D 25.0 True ['BF', 'PH', 'RLF'] vs 0.648 cf nan lat nan bf 919.0
G220331 G220331:1p_655 P1178D 80.0 True ['BF', 'PH', 'CLICK', 'RLF', 'SR'] vs nan cf nan lat 0.0013912992000000013 bf 2614.0
G151210 G151210:777 P829D nan True ['BF', 'CF', 'PH', 'CLICK', 'RLF'] vs 0.114 cf 4000.0 lat 0.0013261215999999989 bf 3819.0
G201215 G201215:3p_283 P137D 15.0 True ['BF', 'CLICK', 'RLF', 'SR'] vs nan cf nan lat 0.0007246240000000018 bf 8238.0
G201001 G201001:1p_123 P1157D 45.0 True ['BF', 'RLF', 'CVC'] vs nan cf nan lat nan bf 4944.0
G201215 G201215:2p_190 P137D 15.0 True ['BF', 'RLF'] vs nan cf nan lat nan bf 5566.0
G190603 G190603:1p_374 P125D 25.0 True ['BF', 'CF', 'RLF', 'NOISE'] vs nan cf 6400.0 lat nan bf 7310.0
G190617 G190617:3p_124 P139D 25.0 True ['BF', 'RLF', 'NOISE'] vs nan cf nan lat nan bf 8929.0
G190912 G190912:360 P1105D 35.0 True ['BF', 'CLICK', 'RLF'] vs nan cf nan lat 0.0007215008000000002 bf 8989.0
G230511 G230511:2p_185 P1146D 35.0 True ['BF', 'CLICK', 'RLF', 'SR'] vs nan cf nan lat 0.0009724319999999988 bf 7314.0
G190411 G190411:578 P144D 15.0 True ['BF', 'PH', 'RLF'] vs 0.722 cf nan lat nan bf 1299.0
G170512 G170512:8P_288 P264D 20.0 True ['BF', 'PH', 'RLF', 'SPS'] vs 0.882 cf nan lat nan bf 428.0
G150717 G150717:1P_588nm P83D 10.0 True ['BF', 'CF', 'PH', 'CLICK', 'RLF'] vs 0.508 cf 1500.0 lat 0.0019002784000000002 bf 1661.0
[... 30 more lines not kept]
```

**Agent**

h5py serialises on a global lock, so threads give little; switching to a process pool and timing again.

**Agent calls Bash**

```bash
cd entries/001262-heeringa-2024; python - <<'EOF'
import re
p='gerbil_an.py'; s=open(p).read()
s=s.replace("from concurrent.futures import ThreadPoolExecutor","from concurrent.futures import ProcessPoolExecutor")
old=s[s.index("def load_all("):s.index("# --- metadata parsing")]
new='''def _read_with_retries(asset, retries=4):
    for attempt in range(retries):
        try:
            return read_unit(asset)
        except Exception as err:  # network errors: retry
            last = err
            time.sleep(3 * (attempt + 1))
    raise last


def load_all(assets, workers=24):
    """Read every file in `assets` (a DataFrame from list_assets) with a process pool.

    h5py holds a global lock, so threads do not read files in parallel; processes do.
    """
    rows = [dict(r) for _, r in assets.iterrows()]
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(_read_with_retries, rows, chunksize=1))


'''
s=s.replace(old,new)
open(p,'w').write(s)
EOF
. $TMPDIR/env/bin/activate; nproc; python - <<'EOF'
import time, gerbil_an as g
A=g.list_assets(); sub=A.sample(48, random_state=1)
t=time.time(); U=g.load_all(sub, workers=24); print('48 files', time.time()-t, sub['size'].sum()/1e9)
EOF
```

```
4
48 files 6.4516942501068115 1.966089928
```

**Agent**

6.5 s for 48 files, so the full dataset loads in about 3 minutes. Loading everything once into a scratch cache for development.

**Agent calls Bash**

```bash
cd entries/001262-heeringa-2024; . $TMPDIR/env/bin/activate; python - <<'EOF'
import time, gerbil_an as g, pickle, os
A=g.list_assets()
t=time.time(); U=g.load_all(A, workers=24); print('all', len(U), time.time()-t)
pickle.dump((A,U), open(os.environ['TMPDIR']+'/all.pkl','wb'))
EOF
date -u
```

```
all 1160 106.60050177574158
Sun Nov  1 13:45:58 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/001262-heeringa-2024; . $TMPDIR/env/bin/activate; python - <<'EOF'
import pickle, os, collections, numpy as np, pandas as pd, gerbil_an as g, hashlib
A,U=pickle.load(open(os.environ['TMPDIR']+'/all.pkl','rb'))
rows=[]
for u in U:
    an=u['analysis']; t=u['trials']
    rows.append(dict(path=u['path'], subj=u['subject_id'], ident=u['identifier'], age=u['age'], sex=u['sex'], weight=u['weight'],
     abrf=g.abr_field(u['notes']), surg=u['surgery'], spk=g.speaker(u['stimulus_description']), species=u['species'],
     an=tuple(an.experiment), types=tuple(sorted(t.experiment.unique())), seq=tuple(sorted(collections.Counter(s.split('_')[0] for s in u['sequential_types']).items())),
     nnan=u['n_nan_spikes'], ntr=len(t), start=u['session_start'], acq_unit=u['acq_unit'], rate=u['acq_rate'],
     h=hashlib.md5(np.concatenate(u['spikes']+[np.zeros(1)]).tobytes()).hexdigest()))
D=pd.DataFrame(rows)
print(D.subj.nunique(), D.species.value_counts().to_dict(), D.acq_unit.value_counts().to_dict(), D.rate.value_counts().to_dict())
print('dupe spike hashes', D.h.duplicated().sum())
print('subject path vs id mismatch', (D.path.str.split('/').str[0]!='sub-'+D.subj).sum())
print(collections.Counter(D.an.map(lambda x: tuple(sorted(collections.Counter(x).items())))).most_common(5))
print('an rows dup types', D.an.map(lambda x: len(x)!=len(set(x))).sum())
print('types in trials', collections.Counter(e for x in D.types for e in x))
print('an vs trial types differ', (D.an.map(lambda x: tuple(sorted(set(x))))!=D.types).sum())
print('seq types', collections.Counter(k for x in D.seq for k,v in x))
print('seq repeated CLICK', collections.Counter(dict(x).get('CLICK') for x in D.seq))
# per subject consistency
for c in ['age','sex','weight','abrf','surg','spk']:
    print(c, 'subjects with >1 value', (D.groupby('subj')[c].nunique(dropna=False)>1).sum())
print(D.abrf.map(repr).value_counts().head(30))
print(D.surg.value_counts())
print(D.spk.value_counts())
print(D.sex.value_counts())
print(D.weight.head(20).tolist())
D.to_pickle(os.environ['TMPDIR']+'/D.pkl')
EOF
```

```
104 {'Meriones unguiculatus': 1160} {'volts': 1160} {48828.125: 1160}
dupe spike hashes 0
subject path vs id mismatch 0
[((('BF', 1), ('RLF', 1)), 371), ((('BF', 1),), 167), ((('BF', 1), ('CLICK', 1), ('RLF', 1), ('SR', 1)), 55), ((('BF', 1), ('PH', 1), ('RLF', 1)), 50), ((('BF', 1), ('CVC', 1), ('RLF', 1)), 47)]
an rows dup types 0
types in trials Counter({'BF': 1152, 'RLF': 952, 'PH': 281, 'CLICK': 275, 'SR': 203, 'NOISE': 143, 'CVC': 135, 'CF': 119, 'SPS': 22})
an vs trial types differ 0
seq types Counter({'BF': 1152, 'RLF': 952, 'PH': 281, 'CLICK': 275, 'SR': 203, 'NOISE': 143, 'CVC': 135, 'CF': 119, 'SPS': 22})
seq repeated CLICK Counter({None: 885, 1: 275})
age subjects with >1 value 0
sex subjects with >1 value 0
weight subjects with >1 value 0
abrf subjects with >1 value 0
surg subjects with >1 value 0
spk subjects with >1 value 0
abrf
'\x0f'    286
'\x14'    178
'\x19'    133
'NaN'     132
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001262-heeringa-2024; . $TMPDIR/env/bin/activate; python - <<'EOF'
import pickle, os, collections, numpy as np, pandas as pd, gerbil_an as g
A,U=pickle.load(open(os.environ['TMPDIR']+'/all.pkl','rb'))
D=pd.read_pickle(os.environ['TMPDIR']+'/D.pkl')
D['days']=D.age.map(g.age_days); D['w']=D.weight.map(g.weight_g); D['abr']=D.abrf.map(g.abr_decoded); D['oxy']=D.surg.map(g.oxygen)
D['grp']=D.days.map(g.age_group)
an=animals=D.groupby('subj').agg(days=('days','first'),sex=('sex','first'),w=('w','first'),abr=('abr','first'),oxy=('oxy','first'),grp=('grp','first'),n=('path','size'))
print(len(an), an.grp.value_counts().to_dict(), an.groupby('grp').sex.apply(lambda s:(s=='F').sum()).to_dict(), D.grp.value_counts().to_dict())
for c in ['days','abr','w']:
    v=an[c]/(g.DAYS_PER_MONTH if c=='days' else 1)
    print(c, an.assign(v=v).groupby('grp').v.agg(['mean','std','min','max','count']).round(2).to_dict('index'))
print('oxygen', an.oxy.value_counts().to_dict())
# complex stimuli experiments
for t in ['NOISE','SPS','CVC']:
    print(t, D[D.types.map(lambda x:t in x)].subj.nunique())
# bf
bf=[]; 
for u in U:
    a=u['analysis']; r=a.set_index('experiment')
    b=r.bf.get('BF',np.nan)
    sr=np.nan
    for k in ['SR','PH','RLF','BF']:
        if k in r.index and not np.isnan(r.sr[k]): sr=r.sr[k]; break
    bf.append(dict(path=u['path'],bf=b, thr=r.threshold.get('RLF',np.nan), cfthr=r.threshold.get('CF',np.nan), sr=sr, sr_SR=r.sr.get('SR',np.nan)))
B=pd.DataFrame(bf); D=D.merge(B,on='path')
print('BF nan', D.bf.isna().sum(), 'units without BF rec', (~D.types.map(lambda x:'BF' in x)).sum())
print(D.groupby('grp').bf.agg(['min','max','count']))
print('SR non-nan', D.sr_SR.notna().sum())
print('middle with SR/SPS/CVC', D[D.grp=='middle'].types.map(lambda x: [t for t in x if t in ('SR','SPS','CVC')]).map(len).sum(), 'SPS by grp', D[D.types.map(lambda x:'SPS' in x)].grp.value_counts().to_dict())
D.to_pickle(os.environ['TMPDIR']+'/D2.pkl')
EOF
```

```
104 {'young': 60, 'old': 31, 'middle': 13} {'middle': 7, 'old': 11, 'young': 32} {'young': 759, 'old': 314, 'middle': 87}
days {'middle': {'mean': 22.49, 'std': 6.22, 'min': 12.56, 'max': 33.17, 'count': 13}, 'old': {'mean': 38.33, 'std': 1.7, 'min': 36.03, 'max': 41.72, 'count': 31}, 'young': {'mean': 5.55, 'std': 2.03, 'min': 2.73, 'max': 11.41, 'count': 60}}
abr {'middle': {'mean': 34.17, 'std': 10.19, 'min': 20.0, 'max': 50.0, 'count': 12}, 'old': {'mean': 49.03, 'std': 18.0, 'min': 20.0, 'max': 85.0, 'count': 31}, 'young': {'mean': 18.1, 'std': 5.33, 'min': 10.0, 'max': 30.0, 'count': 50}}
w {'middle': {'mean': 83.35, 'std': 12.67, 'min': 66.8, 'max': 103.0, 'count': 13}, 'old': {'mean': 86.41, 'std': 11.6, 'min': 60.0, 'max': 120.0, 'count': 31}, 'young': {'mean': 74.61, 'std': 11.07, 'min': 51.2, 'max': 100.0, 'count': 60}}
oxygen {'yes': 78, 'no': 26}
NOISE 21
SPS 5
CVC 17
BF nan 9 units without BF rec 8
          min      max  count
grp                          
middle  350.0  15091.0     87
old     620.0  15762.0    313
young   428.0  15825.0    751
SR non-nan 203
middle with SR/SPS/CVC 0 SPS by grp {'young': 22}
```

**Agent**

Table 1 matches exactly, including the decoded ABR means and SDs (18.1, 34.2, 49.0). Now the figure claims.

**Agent calls Bash**

```bash
cd entries/001262-heeringa-2024; . $TMPDIR/env/bin/activate; python - <<'EOF'
import pickle, os, collections, numpy as np, pandas as pd, gerbil_an as g
from scipy import stats
A,U=pickle.load(open(os.environ['TMPDIR']+'/all.pkl','rb'))
D=pd.read_pickle(os.environ['TMPDIR']+'/D2.pkl')
Um={u['path']:u for u in U}
print(D[~D.types.map(lambda x:'BF' in x)][['path','types']])
# fig6a
y=D[D.grp=='young']
edges=np.logspace(np.log10(0.3),np.log10(20),25)
k=y.bf/1000
rows=[]
for i in range(24):
    m=(k>edges[i])&(k<=edges[i+1])
    rows.append((round(edges[i],2),round(edges[i+1],2), m.sum(), y.thr[m].notna().sum(), round(y.thr[m].mean(),1)))
for r in rows: print(r)
# fig6b
e=np.logspace(np.log10(200),np.log10(20000),25)
h,_=np.histogram(y.bf.dropna(),e)
print(list(zip(np.round(e[:-1]).astype(int),h)))
# fig6c
for name,m in [('low',y.bf<=3500),('high',y.bf>3500)]:
    h,_=np.histogram(y.sr[m].dropna(),np.arange(0,205,5)); print(name, m.sum(), y.sr[m].notna().sum(), list(h[:30]))
EOF
```

```
path                 types
16   sub-G150730/sub-G150730_ses-G150730-6P-1425nm_...  (CF, CLICK, PH, RLF)
29   sub-G150922/sub-G150922_ses-G150922-1P-695nm_i...         (CF, PH, RLF)
103  sub-G151126/sub-G151126_ses-G151126-903nm_icep...         (CF, PH, RLF)
107  sub-G151126/sub-G151126_ses-G151126-893nm_icep...  (CF, CLICK, PH, RLF)
114  sub-G151203/sub-G151203_ses-G151203-1P-1104nm_...  (CF, CLICK, PH, RLF)
223  sub-G170508/sub-G170508_ses-G170508-750_icephy...             (PH, RLF)
244  sub-G170512/sub-G170512_ses-G170512-4P-321_ice...          (NOISE, RLF)
307  sub-G180205/sub-G180205_ses-G180205-820nm_icep...                (RLF,)
(np.float64(0.3), np.float64(0.36), np.int64(0), np.int64(0), nan)
(np.float64(0.36), np.float64(0.43), np.int64(0), np.int64(0), nan)
(np.float64(0.43), np.float64(0.51), np.int64(6), np.int64(4), np.float64(31.3))
(np.float64(0.51), np.float64(0.6), np.int64(9), np.int64(5), np.float64(31.8))
(np.float64(0.6), np.float64(0.72), np.int64(6), np.int64(3), np.float64(36.7))
(np.float64(0.72), np.float64(0.86), np.int64(21), np.int64(18), np.float64(28.7))
(np.float64(0.86), np.float64(1.02), np.int64(36), np.int64(26), np.float64(29.1))
(np.float64(1.02), np.float64(1.22), np.int64(36), np.int64(31), np.float64(28.9))
(np.float64(1.22), np.float64(1.45), np.int64(36), np.int64(31), np.float64(26.5))
(np.float64(1.45), np.float64(1.73), np.int64(33), np.int64(25), np.float64(20.9))
(np.float64(1.73), np.float64(2.06), np.int64(33), np.int64(22), np.float64(21.8))
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001262-heeringa-2024; . $TMPDIR/env/bin/activate; python - <<'EOF'
import pickle, os, collections, numpy as np, pandas as pd, gerbil_an as g, time
from scipy import stats
A,U=pickle.load(open(os.environ['TMPDIR']+'/all.pkl','rb'))
D=pd.read_pickle(os.environ['TMPDIR']+'/D2.pkl')
Um={u['path']:u for u in U}
t=time.time()
D['vs']=[g.max_significant_vs(Um[p]) for p in D.path]
D['cf']=[g.cf_from_cf_recording(Um[p])[0] for p in D.path]
D['cf_lvl']=[g.cf_from_cf_recording(Um[p],level_from='level')[0] for p in D.path]
D['lat']=[g.click_latency_2bins(Um[p]) for p in D.path]
D['lat5']=[g.click_latency_2bins(Um[p],delay=0.005) for p in D.path]
print('time', time.time()-t)
ph=D[D.types.map(lambda x:'PH' in x)]
print('PH units', len(ph), 'with sig vs', ph.vs.notna().sum())
for grp in ['young','middle','old']:
    s=ph[(ph.grp==grp)&ph.vs.notna()]
    print(grp, 'max BF with sig vs', s.bf.max(), 'n', len(s), s.sort_values('bf').bf.tail(4).tolist())
yv=ph[(ph.grp=='young')&ph.vs.notna()]
top=yv.sort_values('vs').tail(5); print(top[['bf','sr','vs']])
for name,s in [('young',yv),('all',ph[ph.vs.notna()])]:
    grpk=np.where(s.bf<1500,'lowBF','highBF')+'_'+np.where(s.sr<18,'lowSR','highSR')
    print(name, s.groupby(grpk).vs.agg(['median','size','max']).round(3).to_dict('index'), 'top unit', s.loc[s.vs.idxmax(),['bf','sr','vs']].tolist())
cf=D[D.types.map(lambda x:'CF' in x)]
print('CF units', len(cf), 'cf nonnan', cf.cf.notna().sum(), 'cf_lvl nonnan', cf.cf_lvl.notna().sum(), 'both cf&bf', (cf.cf.notna()&cf.bf.notna()).sum())
c=cf[cf.cf.notna()&cf.bf.notna()]
print('pearson', stats.pearsonr(np.log(c.cf),np.log(c.bf)), 'spearman', stats.spearmanr(c.cf,c.bf), 'median ratio', np.exp(np.median(np.log(c.cf/c.bf))))
print('diff cf vs cf_lvl', (cf.cf!=cf.cf_lvl).sum())
ck=D[D.types.map(lambda x:'CLICK' in x)]
print('CLICK units', len(ck), 'lat nonnan', ck.lat.notna().sum(), ck.lat5.notna().sum())
k=ck[ck.lat.notna()&ck.bf.notna()]
print('lat pearson', stats.pearsonr(k.lat,np.log(k.bf)), stats.spearmanr(k.lat,k.bf), k.lat.describe())
k=ck[ck.lat5.notna()&ck.bf.notna()]
print('lat5 pearson', stats.pearsonr(k.lat5,np.log(k.bf)), stats.spearmanr(k.lat5,k.bf))
# ntrials per click
print(collections.Counter(len(g.trials_of(Um[p],'CLICK')[0]) for p in ck.path))
D.to_pickle(os.environ['TMPDIR']+'/D3.pkl')
EOF
```

```
time 4.551948308944702
PH units 281 with sig vs 193
young max BF with sig vs 4598.0 n 131 [nan, nan, nan, nan]
middle max BF with sig vs 3819.0 n 23 [2218.0, 2339.0, 3707.0, 3819.0]
old max BF with sig vs 3272.0 n 39 [3097.0, 3120.0, 3272.0, nan]
         bf     sr        vs
6     723.0  78.25  0.829914
247   794.0  12.50  0.836599
259  1188.0  10.00  0.838311
158  1342.0  52.50  0.845805
251   428.0   1.25  0.882459
young {'highBF_highSR': {'median': 0.474, 'size': 67, 'max': 0.767}, 'highBF_lowSR': {'median': 0.402, 'size': 7, 'max': 0.703}, 'lowBF_highSR': {'median': 0.695, 'size': 51, 'max': 0.846}, 'lowBF_lowSR': {'median': 0.821, 'size': 6, 'max': 0.882}} top unit [428.0, 1.25, 0.8824585017938534]
all {'highBF_highSR': {'median': 0.474, 'size': 83, 'max': 0.767}, 'highBF_lowSR': {'median': 0.402, 'size': 21, 'max': 0.728}, 'lowBF_highSR': {'median': 0.702, 'size': 70, 'max': 0.863}, 'lowBF_lowSR': {'median': 0.804, 'size': 19, 'max': 0.882}} top unit [428.0, 1.25, 0.8824585017938534]
CF units 119 cf nonnan 119 cf_lvl nonnan 119 both cf&bf 114
pearson PearsonRResult(statistic=np.float64(0.9732858390461456), pvalue=np.float64(2.070501783654902e-73)) spearman SignificanceResult(statistic=np.float64(0.964303798222702), pvalue=np.float64(1.8129180620087383e-66)) median ratio 1.0028279393862238
diff cf vs cf_lvl 0
CLICK units 275 lat nonnan 271 272
lat pearson PearsonRResult(statistic=np.float64(-0.8821216502743667), pvalue=np.float64(5.915246895082599e-89)) SignificanceResult(statistic=np.float64(-0.8640743321266), pvalue=np.float64(2.835940449943214e-81)) count    268.000000
mean       0.001186
std        0.000452
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001262-heeringa-2024; . $TMPDIR/env/bin/activate; python - <<'EOF'
import pickle, os, collections, numpy as np, pandas as pd, gerbil_an as g, time
from scipy import stats
A,U=pickle.load(open(os.environ['TMPDIR']+'/all.pkl','rb'))
D=pd.read_pickle(os.environ['TMPDIR']+'/D3.pkl')
Um={u['path']:u for u in U}
t=time.time()
isi={p:g.short_isis(Um[p]) for p in D.path}
print('isi time', time.time()-t)
a=sum(any(v[0]>=2 for v in d.values()) for d in isi.values())
b=sum(sum(v[0] for v in d.values())>=2 for d in isi.values())
c=sum(d.get('BF',(0,0))[0]>=2 for d in isi.values())
any1=sum(sum(v[0] for v in d.values())>=1 for d in isi.values())
print('a',a,'b',b,'c',c,'any>=1',any1)
tot=pd.Series({p:sum(v[0] for v in d.values()) for p,d in isi.items()})
print(tot.value_counts().sort_index().head(20), tot.max())
print('by type', collections.Counter(k for d in isi.values() for k,v in d.items() if v[0]>=2))
# unsorted spikes?
uns=sum(any(np.any(np.diff(s)<0) for s in Um[p]['spikes']) for p in D.path); print('files with unsorted spikes in a trial', uns)
zero=sum(sum(np.sum(np.diff(s)==0) for s in Um[p]['spikes'])>0 for p in D.path); print('files with zero ISI', zero)
# min ISI distribution
mins=pd.Series({p:min([np.diff(s).min() for s in Um[p]['spikes'] if len(s)>1] or [np.nan]) for p in D.path})
print((mins*1000).describe(), ((mins<0.0006)).sum())
# representative sampling
yb=np.log(D[D.grp=='young'].bf.dropna()); ab=np.log(D.bf.dropna())
for name,s in [('CF',D[D.types.map(lambda x:'CF' in x)]),('CLICK',D[D.lat.notna()]),('CLICKany',D[D.types.map(lambda x:'CLICK' in x)])]:
    x=np.log(s.bf.dropna())
    for rn,ref in [('young',yb),('all',ab)]:
        print(name, rn, len(x), stats.ks_2samp(x,ref), np.exp(np.median(x)), np.exp(np.median(ref)), np.exp(np.median(x))/np.exp(np.median(ref)))
EOF
```

```
isi time 3.772245168685913
a 370 b 391 c 148 any>=1 538
0     622
1     147
2      79
3      36
4      32
5      16
6      19
7      16
8      17
9       7
10      7
11      5
12      8
13      9
14      3
15      4
16      2
17      3
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "def \|tags\|claim:\|sanity\|install\|pip\|Result" tools/entry.py | head -80
```

```
21:- each notebook has a cell tagged `sanity` that prints what was loaded;
26:notebook through a Jupyter kernel installed in that environment, in the entry
33:markdown cell that begins "**Result:" and everything from the "## Summary"
70:    def __init__(self):
73:    def error(self, where, message: str) -> None:
78:def dataset_id(record: dict) -> str | None:
83:def schema(name: str) -> Draft202012Validator:
94:def _parsed(text: str):
102:def _schema_errors(text: str, schema_name: str) -> tuple[str, ...]:
108:def load(report: Report, path: Path):
116:def validate(report: Report, path: Path, schema_name: str) -> dict | None:
125:def _plain(value):
136:def code_of(notebook_path: Path) -> str:
143:def check(entry_dir: Path) -> Report:
196:        if not any("sanity" in c.metadata.get("tags", []) for c in nb.cells if c.cell_type == "code"):
197:            report.error(rel / name, "no code cell tagged `sanity` (the data check; see docs/protocol.md)")
258:        # tested on may already have been replaced (docs/pipeline.md), so it is not held to the current one.
308:                if not any(tag in c.metadata.get("tags", []) for c in nb.cells):
313:def _local_data(code: str, start: int) -> bool:
320:def _derivation_checks(report: Report, where, code: str) -> None:
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,40p tools/entry.py; sed -n 143,335p tools/entry.py
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
[... 213 more lines not kept]
```

**Agent**

Writing the notebook now (generated with nbformat so cell tags are set).

**Agent calls Bash**

```bash
date -u
```

```
Sun Nov  1 13:48:34 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude/build_nb.py",
 "content": "import nbformat as nbf\nimport sys\n\ncells = []\n\n\ndef md(text, tags=None):\n    c = nbf.v4.new_markdown_cell(text.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\ndef code(text, tags=None):\n    c = nbf.v4.new_code_cell(text.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nmd(r\"\"\"\n# Reproducing Heeringa (2024) from dandiset 001262\n\n**Paper.** Heeringa AN (2024). Single-unit data for sensory neuroscience: Responses from the\nauditory nerve of young-adult and aging gerbils. *Scientific Data* 11, 411.\n[doi:10.1038/s41597-024-03259-3](https://doi.org/10.1038/s41597-024-03259-3). The claims file\nwas written from the version of record (open access, PMC11035566), which has no supplement, and\nfrom the paper's MATLAB toolbox on Zenodo (doi:10.5281/zenodo.10370064).\n\n**Dandiset.** [DANDI:001262](https://dandiarchive.org/dandiset/001262/0.241205.0959), version\n0.241205.0959. The paper cites no DANDI version: its data statement points to the Dryad deposit\n(doi:10.5061/dryad.qv9s4mwn4), which the dandiset lists as a variant form. Two versions were\npublished on 2024-12-05, 30 minutes apart; this is the more recent. The data check below shows\nthat both hold the same 1160 files (same blobs), so the choice changes no number; the later one\nadds metadata only (the paper as `relatedResource` and `protocol`, keywords, funder, ethics).\n\n**What the dandiset holds.** One NWB file per single unit, 1160 units from 104 gerbils, with per\ntrial the spike times, the stimulus (frequency, level, delay, duration), the raw voltage trace,\nand per recording type one row of analysed outcomes (best frequency, spontaneous rate,\nthreshold). The other analysed outcomes the paper describes (characteristic frequency, vector\nstrength and its p-value, click latencies) are not in the files, so they are recomputed here from\nthe spike times with the paper's own functions (named in its Methods), as described in the helper\n`gerbil_an.py`. Raw voltage traces are not read.\n\n**Outside inputs.** None. Method details come from the paper's Methods and from its code\n(Zenodo record 10370064), as cited in the helper and under each claim.\n\n| Claim | Tested |\n|---|---|\n| table1-animals-units | tested |\n| table1-age-abr-weight | tested |\n| table1-bf-range | tested |\n| fig3-abr-age | tested |\n| females-fewer-in-old | tested |\n| oxygen-78 | tested |\n| complex-stimuli-experiments | tested |\n| recording-type-counts | tested |\n| fig7-sampling-by-age | tested |\n| isi-exclusion | tested |\n| no-prepotentials | blocked (methods underspecified) |\n| rlf-monotonic | blocked (methods underspecified); description shown |\n| fig5b-example | tested |\n| fig6a-young-two-sensitive-regions | tested |\n| fig6b-young-bf-gap | tested |\n| fig6c-sr-distributions | tested |\n| fig6d-max-phase-locking-bf | tested |\n| fig6d-highest-vs-low-bf-low-sr | tested |\n| fig7a-cf-matches-bf | tested |\n| fig7b-click-latency-bf | tested |\n| fig7ab-representative-sampling | tested |\n| old-success-rate | blocked (data missing) |\n| psth-primary-like | blocked (methods underspecified) |\n\"\"\")\n\ncode(r\"\"\"\nimport time\nimport warnings\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\n\nimport gerbil_an as g\n\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 200)\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nstarted = time.time()\nassets = g.list_assets()\nunits = g.load_all(assets)\nprint(f\"read {len(units)} files of dandiset {g.DANDISET_ID} version {g.DANDISET_VERSION} \"\n      f\"in {time.time() - started:.0f} s\")\n\"\"\")\n\nmd(r\"\"\"\n## Data check\n\nOne row per unit, with the animal metadata parsed from the file and the analysed outcomes from\nits analysis table. Each check of the metadata against the values is stated under its output.\n\"\"\")\n\ncode(r\"\"\"\nearlier = g.list_assets(\"0.241205.0929\")\nsame = (set(zip(assets.path, assets.blob)) == set(zip(earlier.path, earlier.blob)))\nprint(f\"Versions 0.241205.0929 and {g.DANDISET_VERSION}: {len(earlier)} and {len(assets)} files; \"\n      f\"same paths and blobs: {same}\")\nmeta = requests_meta = __import__(\"requests\").get(\n    f\"{g.API}/dandisets/{g.DANDISET_ID}/versions/{g.DANDISET_VERSION}/\", timeout=60).json()\nsumm = meta[\"assetsSummary\"]\nprint(\"Archive summary: subjects\", summ[\"numberOfSubjects\"], \"; files\", summ[\"numberOfFiles\"],\n      \"; species\", [s[\"name\"] for s in summ[\"species\"]],\n      \"; variableMeasured\", summ[\"variableMeasured\"],\n      \"; measurementTechnique\", [m[\"name\"] for m in summ[\"measurementTechnique\"]])\n\"\"\", tags=[\"sanity\"])\n\ncode(r\"\"\"\nrows = []\nfor u in units:\n    a = u[\"analysis\"].set_index(\"experiment\")\n    sr_best, sr_source = np.nan, None\n    for k in [\"SR\", \"PH\", \"RLF\", \"BF\"]:          # best estimate of SR, check_dataset_units.m\n        if k in a.index and not np.isnan(a.sr[k]):\n            sr_best, sr_source = a.sr[k], k\n            break\n    t = u[\"trials\"]\n    rows.append({\n        \"path\": u[\"path\"], \"animal\": u[\"subject_id\"], \"unit\": u[\"identifier\"].split(\":\", 1)[1],\n        \"age_days\": g.age_days(u[\"age\"]), \"sex\": u[\"sex\"], \"weight_g\": g.weight_g(u[\"weight\"]),\n        \"abr_field\": g.abr_field(u[\"notes\"]), \"oxygen\": g.oxygen(u[\"surgery\"]),\n        \"speaker\": g.speaker(u[\"stimulus_description\"]),\n        \"types\": tuple(sorted(t.experiment.unique())),\n        \"analysis_rows\": tuple(u[\"analysis\"].experiment),\n        \"bf\": a.bf.get(\"BF\", np.nan), \"rlf_threshold\": a.threshold.get(\"RLF\", np.nan),\n        \"sr_best\": sr_best, \"sr_source\": sr_source, \"sr_SR\": a.sr.get(\"SR\", np.nan),\n        \"n_trials\": len(t), \"n_spikes\": int(t.n_spikes.sum()), \"nan_placeholders\": u[\"n_nan_spikes\"],\n        \"tags_match\": bool(all(tag.startswith(e + \"_\") for tag, e in zip(t.tag, t.experiment))),\n    })\nU = pd.DataFrame(rows)\nU[\"abr\"] = U.abr_field.map(g.abr_decoded)\nU[\"group\"] = U.age_days.map(g.age_group)\nby_path = {u[\"path\"]: u for u in units}\nprint(\"Units:\", len(U), \"; animals:\", U.animal.nunique(), \"; species in files:\",\n      sorted({u[\"species\"] for u in units}))\nprint(\"Each file's subject folder matches its subject_id:\",\n      bool((U.path.str.split(\"/\").str[0] == \"sub-\" + U.animal).all()))\nprint(\"Animal metadata constant within each animal (age, sex, weight, ABR, oxygen, speaker):\",\n      bool((U.groupby(\"animal\")[[\"age_days\", \"sex\", \"weight_g\", \"abr_field\", \"oxygen\", \"speaker\"]]\n            .nunique(dropna=False) <= 1).all().all()))\nprint(\"Every trial's tag starts with its recording type:\", bool(U.tags_match.all()))\nprint(\"Recording types in the analysis table and in the trials agree:\",\n      bool((U.analysis_rows.map(lambda x: tuple(sorted(x))) == U.types).all()),\n      \"; analysis rows with a repeated type:\", int(U.analysis_rows.map(lambda x: len(x) != len(set(x))).sum()))\nprint(\"Units per recording type:\")\nprint(pd.Series([t for ts in U.types for t in ts]).value_counts().to_string())\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nEvery file opens, every subject folder matches the file's `subject_id`, and the animal metadata\nare the same in all files of an animal, so animals are counted by `subject_id`. The archive's\nsummary of 104 subjects matches. Each unit is in one file, so no unit has to be matched across\nfiles. The trial table and the spike-time table have one row per trial in the same order (every\ntag begins with the trial's recording type), and each recording type appears once per unit in\nthe analysis table.\n\"\"\")\n\ncode(r\"\"\"\nprint(\"Ages (days), by group:\")\nprint(U.groupby(\"group\").age_days.agg([\"min\", \"max\", \"size\"]).to_string())\nprint(\"\\nRaw weight strings, examples:\", U.drop_duplicates(\"animal\").weight_g.head(3).tolist(),\n      [by_path[p][\"weight\"] for p in U.drop_duplicates(\"animal\").path.head(3)])\nprint(\"Weights (g): min\", U.weight_g.min(), \"max\", U.weight_g.max(), \"; unparsed:\", int(U.weight_g.isna().sum()))\nprint(\"Sex values:\", U.drop_duplicates(\"animal\").sex.value_counts().to_dict())\nprint(\"Oxygen field per animal:\", U.drop_duplicates(\"animal\").oxygen.value_counts().to_dict())\nprint(\"Speaker per animal:\", U.drop_duplicates(\"animal\").speaker.value_counts().to_dict())\nprint(\"\\nNotes field, example:\", repr(units[0][\"notes\"]))\nab = U.drop_duplicates(\"animal\")\nprint(\"\\nABR field after 'threshold (db SPL): ' per animal (repr), with its code point:\")\nprint(ab.abr_field.map(lambda s: (repr(s), ord(s) if len(s) == 1 else None)).value_counts().to_string())\ndec = ab.abr.dropna()\nprint(\"Decoded thresholds: values\", sorted(dec.unique().tolist()), \"; all multiples of 5:\",\n      bool((dec % 5 == 0).all()), \"; animals with 'NaN':\", int((ab.abr_field == \"NaN\").sum()))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nThe ABR threshold is not readable as written. In every file `general/notes` ends with\n\"threshold (db SPL): \" followed by a single character, or by \"NaN\". Read as code points, the\ncharacters are 10 to 85 in steps of 5 (for example \"#\" is 35 and \"K\" is 75; some are control\ncharacters such as a line feed, 10), which is the range Table 1 gives (10 to 85 dB SPL). The\nnumber appears to have been written as a character in the conversion to NWB. This is a format\nerror in the files; the claims that use the ABR threshold read it as the character's code point,\nan interpretation the data support (the values are multiples of 5 and in the paper's range) but\ndo not prove. 11 animals have \"NaN\". Ages are given in days (`P85D`), weights as text with a unit\n(`65g`, `6.110000e+01g`), and oxygen as \"yes\" or \"no\" in `general/surgery`.\n\"\"\")\n\ncode(r\"\"\"\nprint(\"BF (stored, Hz): min\", U.bf.min(), \"max\", U.bf.max(), \"; units with a BF recording:\",\n      int(U.types.map(lambda x: \"BF\" in x).sum()), \"; BF NaN:\", int(U.bf.isna().sum()))\nprint(\"RLF threshold (stored, dB SPL): min\", round(U.rlf_threshold.min(), 1), \"max\", round(U.rlf_threshold.max(), 1),\n      \"; non-NaN\", int(U.rlf_threshold.notna().sum()), \"of\", int(U.types.map(lambda x: \"RLF\" in x).sum()), \"RLF units\")\nprint(\"SR best estimate (spikes/s): min\", U.sr_best.min(), \"max\", round(U.sr_best.max(), 1),\n      \"; source:\", U.sr_source.value_counts(dropna=False).to_dict())\nprint(\"Spike-time NaN placeholders (trials with no spike):\", int(U.nan_placeholders.sum()),\n      \"; trials:\", int(U.n_trials.sum()))\nallt = pd.concat([u[\"trials\"].assign(path=u[\"path\"]) for u in units], ignore_index=True)\nprint(\"\\nTrial parameters by recording type:\")\nsummary = allt.groupby(\"experiment\").agg(\n    trials=(\"tag\", \"size\"), delay_ms=(\"delay\", lambda x: sorted(set(np.round(x.dropna() * 1000, 2)))),\n    duration_ms=(\"duration\", lambda x: sorted(set(np.round(x.dropna() * 1000, 1)))[:4]),\n    trial_ms=(\"trial_s\", lambda x: sorted(set(np.round(x.dropna() * 1000, 1)))[:6]),\n    level_min=(\"level\", lambda x: x[x > -99999].min()), level_max=(\"level\", \"max\"),\n    delay_nan=(\"delay\", lambda x: int(x.isna().sum())))\nprint(summary.to_string())\nlate = []\nfor u in units:\n    for (_, tr), s in zip(u[\"trials\"].iterrows(), u[\"spikes\"]):\n        if len(s) and (s.min() < 0 or s.max() > tr.trial_s + 1e-9):\n            late.append(u[\"path\"])\n            break\nprint(\"\\nUnits with a spike outside [0, trial length]:\", len(late))\nsrt = sum(any(np.any(np.diff(s) < 0) for s in u[\"spikes\"]) for u in units)\nprint(\"Units with unsorted spike times within a trial:\", srt)\ndups = U.assign(h=[hash(np.concatenate(u[\"spikes\"] + [np.zeros(1)]).tobytes()) for u in units]).h.duplicated().sum()\nprint(\"Units whose spike times duplicate another unit's:\", int(dups))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nSpike times are in seconds from the start of each trial: tone trials start the tone at 7.75 ms\nand last 50 ms, and no spike falls outside its trial's length (taken from the length of the voltage\ntrace at 48,828.125 Hz, the rate the Methods give). Spike times are sorted within trials, and no\nunit's spike train duplicates another's, so no recording was deposited twice. Empty trials hold a\nsingle NaN. The CLICK trials, and the SR, NOISE and CVC trials, carry no delay (NaN): the click's\nonset in the trial is not in the files.\n\nThe next cell checks that spikes and the trial table share a clock, with a contrast between\nconditions: the rate in tone trials minus the rate in the interleaved silent trials, in 5 ms\nwindows from the start of the trial, over the BF and RLF recordings. If the clock is shared, the\ndifference is near zero before 7.75 ms and large from a few milliseconds after it. It then checks\nthat the stored best frequency agrees with the frequency of the highest tone-evoked rate computed\nfrom the spike times.\n\"\"\")\n\ncode(r\"\"\"\nedges = np.arange(0, 0.0801, 0.005)\ndiff_rows = []\nfor u in units:\n    t = u[\"trials\"]\n    for exp in [\"BF\", \"RLF\"]:\n        idx = np.flatnonzero(t.experiment.values == exp)\n        if len(idx) == 0:\n            continue\n        tone = [u[\"spikes\"][i] for i in idx if t.frequency.values[i] != g.SPONT]\n        sil = [u[\"spikes\"][i] for i in idx if t.frequency.values[i] == g.SPONT]\n        if not tone or not sil:\n            continue\n        rt = np.histogram(np.concatenate(tone), edges)[0] / len(tone) / 0.005\n        rs = np.histogram(np.concatenate(sil), edges)[0] / len(sil) / 0.005\n        diff_rows.append(rt - rs)\ndiff = np.array(diff_rows)\nprint(f\"{len(diff)} BF and RLF recordings with tone and silent trials\")\nprint(\"Window (ms)  median(tone - silent)  fraction of recordings with tone > silent\")\nfor i in range(len(edges) - 1):\n    print(f\"{edges[i]*1000:5.0f}-{edges[i+1]*1000:<5.0f}  {np.median(diff[:, i]):10.1f}  {np.mean(diff[:, i] > 0):10.2f}\")\n\n# stored BF against the frequency of the highest mean tone-evoked rate in the BF recording\ncmp = []\nfor u in units:\n    t, sp = g.trials_of(u, \"BF\")\n    b = U.loc[U.path == u[\"path\"], \"bf\"].iloc[0]\n    if len(t) == 0 or np.isnan(b):\n        continue\n    t = t.assign(rate=[np.sum((s > a) & (s < a + d)) / d for s, a, d in zip(sp, t.delay, t.duration)])\n    m = t[t.frequency != g.SPONT].groupby(\"frequency\").rate.mean()\n    cmp.append(np.log2(m.idxmax() / b))\ncmp = np.array(cmp)\nprint(f\"\\nStored BF against the raw peak of the frequency-response curve, {len(cmp)} units: \"\n      f\"median |log2 ratio| {np.median(np.abs(cmp)):.3f} octaves; within 0.25 octave {np.mean(np.abs(cmp) <= 0.25):.2f}\")\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nBefore the tone (0 to 5 ms) the tone and silent trials do not differ; from 10 ms the tone trials\nfire far more, in almost every recording, and the difference falls back after the tone ends\n(57.75 ms). The spikes and the trial table share a clock in the BF and RLF recordings, the ones\nwhose timing matters for the claims (PH and CF use the same delay and duration). The stored BF is\nclose to the raw peak of the spike-time frequency-response curve (the stored value is the peak of\na smoothing spline, Methods), so the analysis table and the spike times describe the same\nrecordings.\n\"\"\")\n\n# ---------------------------------------------------------------- claims\nmd(r\"\"\"\n## table1-animals-units\n\n> The dataset holds 104 experiments (gerbils) with 1160 single auditory nerve fibres; 60\n> young-adult (32 female), 13 middle-aged (7 female) and 31 old (11 female) gerbils, with 759, 87\n> and 314 single units.\n\nAnimals by `subject_id`, age groups by age in days as the code defines them (young <= 365,\nmiddle > 365 and <= 1095, old > 1095).\n\"\"\")\n\ncode(r\"\"\"\nA = U.groupby(\"animal\").agg(age_days=(\"age_days\", \"first\"), sex=(\"sex\", \"first\"),\n                            weight_g=(\"weight_g\", \"first\"), abr=(\"abr\", \"first\"),\n                            oxygen=(\"oxygen\", \"first\"), group=(\"group\", \"first\"), units=(\"path\", \"size\"))\ntable = pd.DataFrame({\n    \"animals\": A.groupby(\"group\").size(),\n    \"females\": A[A.sex == \"F\"].groupby(\"group\").size(),\n    \"units\": U.groupby(\"group\").size()}).loc[[\"young\", \"middle\", \"old\"]]\nprint(table.to_string())\nprint(\"Total animals:\", len(A), \"; total units:\", len(U))\npaper = {\"young\": (60, 32, 759), \"middle\": (13, 7, 87), \"old\": (31, 11, 314)}\nmatch = all(tuple(table.loc[k]) == v for k, v in paper.items()) and len(A) == 104 and len(U) == 1160\nprint(\"Paper: 60 (32) 759; 13 (7) 87; 31 (11) 314; totals 104 and 1160. All eleven counts match:\", match)\nprint(\"Units per animal: min\", A.units.min(), \"median\", A.units.median(), \"max\", A.units.max())\n\"\"\", tags=[\"claim:table1-animals-units\"])\n\nmd(r\"\"\"\n**Result: reproduced.** 104 animals and 1160 units; 60 young adults (32 female) with 759 units,\n13 middle aged (7 female) with 87, and 31 old (11 female) with 314. All eleven counts match.\n\"\"\")\n\nmd(r\"\"\"\n## table1-age-abr-weight\n\n> Mean ages of the groups are 5.5, 22.5 and 38.3 months, mean ABR thresholds 18.1, 34.2 and 49.0\n> dB SPL, and mean weights 74.6, 83.4 and 86.4 g (young adult, middle aged, old).\n\nOver animals, missing values left out, months = days / (365/12) (check_dataset_metadata.m). The\nABR threshold is the code point of the character in the notes (data check above).\n\"\"\")\n\ncode(r\"\"\"\nA[\"age_months\"] = A.age_days / g.DAYS_PER_MONTH\nrows = []\nexpected = {\"age_months\": (5.5, 22.5, 38.3), \"abr\": (18.1, 34.2, 49.0), \"weight_g\": (74.6, 83.4, 86.4)}\nfor var, exp in expected.items():\n    for grp, e in zip([\"young\", \"middle\", \"old\"], exp):\n        v = A.loc[A.group == grp, var].dropna()\n        rows.append({\"variable\": var, \"group\": grp, \"n\": len(v), \"mean\": round(v.mean(), 2), \"sd\": round(v.std(), 2),\n                     \"min\": round(v.min(), 1), \"max\": round(v.max(), 1), \"paper_mean\": e,\n                     \"within_10pct\": abs(v.mean() - e) <= 0.1 * e})\nres = pd.DataFrame(rows)\nprint(res.to_string(index=False))\nprint(\"Means within tolerance:\", int(res.within_10pct.sum()), \"of 9\")\nprint(\"Animals without an ABR threshold, by group:\", A[A.abr.isna()].group.value_counts().to_dict())\n\"\"\", tags=[\"claim:table1-age-abr-weight\"])\n\nmd(r\"\"\"\n**Result: reproduced.** All nine means are within tolerance and equal the paper's after rounding:\nages 5.55, 22.49 and 38.33 months, ABR thresholds 18.10, 34.17 and 49.03 dB SPL, weights 74.61,\n83.35 and 86.41 g. The SDs and ranges printed also match Table 1 (for example ABR SD 5.33, 10.19\nand 18.00, range 20 to 85 in old animals). The ABR values rest on reading the notes' character as\nits code point; 10 young adults and 1 middle-aged animal have no ABR threshold, and the paper's\nmeans are also over fewer animals than the group sizes if they omit the same ones, which the match\nsuggests.\n\"\"\")\n\nmd(r\"\"\"\n## table1-bf-range\n\n> Best frequencies range from 428 to 15,825 Hz in young adults, 350 to 15,091 Hz in middle-aged and\n> 620 to 15,762 Hz in old gerbils.\n\nA unit's BF is its stored BF, or its CF when it has no BF recording (check_dataset_metadata.m).\nThe CF is not stored in the files, so it is recomputed from the CF recording (helper,\n`cf_from_cf_recording`).\n\"\"\")\n\ncode(r\"\"\"\nU[\"cf\"] = [g.cf_from_cf_recording(by_path[p])[0] for p in U.path]\nno_bf = U[~U.types.map(lambda x: \"BF\" in x)]\nprint(\"Units without a BF recording:\", len(no_bf))\nprint(no_bf[[\"animal\", \"unit\", \"group\", \"types\", \"cf\"]].to_string(index=False))\nU[\"bf_or_cf\"] = U.bf.where(U.types.map(lambda x: \"BF\" in x), U.cf)\nrng = U.groupby(\"group\").agg(min_bf=(\"bf_or_cf\", \"min\"), max_bf=(\"bf_or_cf\", \"max\"), n=(\"bf_or_cf\", \"count\"),\n                             min_stored=(\"bf\", \"min\"), max_stored=(\"bf\", \"max\")).loc[[\"young\", \"middle\", \"old\"]]\nrng[\"paper\"] = [\"428-15825\", \"350-15091\", \"620-15762\"]\nprint(rng.to_string())\npaper = {\"young\": (428, 15825), \"middle\": (350, 15091), \"old\": (620, 15762)}\nok = {k: abs(rng.loc[k, \"min_bf\"] - lo) <= 0.1 * lo and abs(rng.loc[k, \"max_bf\"] - hi) <= 0.1 * hi\n      for k, (lo, hi) in paper.items()}\nprint(\"Within 10% of both bounds:\", ok)\n\"\"\", tags=[\"claim:table1-bf-range\"])\n\nmd(r\"\"\"\n**Result: reproduced.** The ranges are 428 to 15,825 Hz (young), 350 to 15,091 Hz (middle aged) and\n620 to 15,762 Hz (old), the paper's values exactly, with or without the recomputed CF of the units\nthat have no BF recording (none of those CFs is outside the range).\n\"\"\")\n\nmd(r\"\"\"\n## fig3-abr-age\n\n> ABR thresholds rise with age, and hearing loss varies widely among the old animals.\n\nOver animals; reproduced when the mean ABR threshold increases from young to middle aged to old\nand the SD of old animals is the largest of the three.\n\"\"\")\n\ncode(r\"\"\"\ns = A.groupby(\"group\").abr.agg([\"mean\", \"std\", \"min\", \"max\", \"count\"]).loc[[\"young\", \"middle\", \"old\"]].round(2)\nprint(s.to_string())\ninc = s[\"mean\"].is_monotonic_increasing\nprint(\"Mean increases young < middle < old:\", inc, \"; old SD the largest:\", s[\"std\"].idxmax() == \"old\")\nrho = stats.spearmanr(A.age_days, A.abr, nan_policy=\"omit\")\nprint(f\"Spearman correlation of age with ABR threshold over {A.abr.notna().sum()} animals: \"\n      f\"rho = {rho.statistic:.2f}, p = {rho.pvalue:.2g}\")\nfor sex in [\"F\", \"M\"]:\n    sub = A[A.sex == sex].groupby(\"group\").abr.mean().loc[[\"young\", \"middle\", \"old\"]].round(1)\n    print(f\"Mean ABR by group, {sex}:\", sub.to_dict())\nfig, ax = plt.subplots(figsize=(5, 3.5))\nfor sex, col in [(\"F\", \"tab:green\"), (\"M\", \"tab:purple\")]:\n    d = A[A.sex == sex]\n    ax.scatter(d.age_days / g.DAYS_PER_MONTH, d.abr, s=18, color=col, label=sex)\nax.set_xlabel(\"Age (months)\"); ax.set_ylabel(\"ABR threshold (dB SPL)\"); ax.legend()\nprint(\"Plotted ranges: age\", round(A.age_days.min() / g.DAYS_PER_MONTH, 1), \"to\",\n      round(A.age_days.max() / g.DAYS_PER_MONTH, 1), \"months; ABR\", A.abr.min(), \"to\", A.abr.max(), \"dB SPL\")\n\"\"\", tags=[\"claim:fig3-abr-age\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Mean ABR thresholds are 18.1, 34.2 and 49.0 dB SPL in young, middle-aged and\nold animals, and the SD of the old animals is the largest (18.0, against 5.3 and 10.2), with old\nthresholds from 20 to 85 dB SPL. Over animals, age and threshold correlate (Spearman rho printed\nabove). It rests on reading the ABR character as its code point.\n\"\"\")\n\nmd(r\"\"\"\n## females-fewer-in-old\n\n> Old gerbils are skewed towards males (11 of 31 female), which the paper attributes to ovarian\n> cancer and early death of old females.\n\"\"\")\n\ncode(r\"\"\"\nfrac = A.groupby(\"group\").apply(lambda d: pd.Series({\"female\": int((d.sex == \"F\").sum()), \"animals\": len(d)}))\nfrac[\"fraction_female\"] = (frac.female / frac.animals).round(3)\nprint(frac.loc[[\"young\", \"middle\", \"old\"]].to_string())\nold_f, young_f = frac.loc[\"old\", \"fraction_female\"], frac.loc[\"young\", \"fraction_female\"]\nprint(\"Old fraction below one half:\", old_f < 0.5, \"; below young adults:\", old_f < young_f)\nf = stats.fisher_exact([[frac.loc[\"old\", \"female\"], frac.loc[\"old\", \"animals\"] - frac.loc[\"old\", \"female\"]],\n                        [frac.loc[\"young\", \"female\"], frac.loc[\"young\", \"animals\"] - frac.loc[\"young\", \"female\"]]])\nprint(f\"Fisher's exact test, old against young (not part of the criterion): odds ratio {f.statistic:.2f}, p = {f.pvalue:.3f}\")\n\"\"\", tags=[\"claim:females-fewer-in-old\"])\n\nmd(r\"\"\"\n**Result: reproduced.** 11 of 31 old animals are female (0.355), below one half and below the\nyoung adults (32 of 60, 0.533). The difference from young adults is not significant by Fisher's\nexact test (printed above), which the paper does not claim. The cause is not tested.\n\"\"\")\n\nmd(r\"\"\"\n## oxygen-78\n\n> Of the 104 gerbils, 78 received additional oxygen throughout the experiment.\n\nCounted once per animal from \"oxygen: yes|no\" in `general/surgery`.\n\"\"\")\n\ncode(r\"\"\"\nprint(A.oxygen.value_counts().to_string())\nprint(\"By group:\", A.groupby(\"group\").oxygen.apply(lambda s: int((s == \"yes\").sum())).to_dict())\n\"\"\", tags=[\"claim:oxygen-78\"])\n\nmd(r\"\"\"\n**Result: reproduced.** 78 of 104 animals have \"oxygen: yes\".\n\"\"\")\n\nmd(r\"\"\"\n## complex-stimuli-experiments\n\n> Responses to paired noise bursts were recorded in 21 of 104 experiments, Schroeder-phase stimuli\n> in 5, and consonant-vowel-consonant logatomes in 17.\n\nAn experiment counts when at least one of its units has a NOISE, SPS or CVC recording.\n\"\"\")\n\ncode(r\"\"\"\nfor t in [\"NOISE\", \"SPS\", \"CVC\"]:\n    has = U[U.types.map(lambda x: t in x)]\n    print(f\"{t}: {has.animal.nunique()} experiments, {len(has)} units; by group of animals:\",\n          has.drop_duplicates(\"animal\").group.value_counts().to_dict())\n\"\"\", tags=[\"claim:complex-stimuli-experiments\"])\n\nmd(r\"\"\"\n**Result: reproduced.** NOISE in 21, SPS in 5 and CVC in 17 of the 104 experiments.\n\"\"\")\n\nmd(r\"\"\"\n## recording-type-counts\n\n> CF recordings were obtained for 119 fibres, CLICK for 261, SR for 203, NOISE for 143, SPS for 22\n> and CVC for 135.\n\nReading 1 (as check_dataset_units.m prints them): CF, units with a non-NaN CF; CLICK, units with\nexactly one CLICK recording and a non-NaN 2-bin latency; SR, units with a non-NaN SR from an SR\nrecording; NOISE, SPS and CVC, units with a recording of that type. Reading 2: units with any\nrecording of the type. The stored CF and click latency are not in the files; reading 1 uses the\nvalues recomputed with the paper's functions (helper). The click delay is not in the files: the\nlatency uses 7.75 ms (assumption, helper docstring), with 5 ms shown as a variant.\n\"\"\")\n\ncode(r\"\"\"\nU[\"click_latency\"] = [g.click_latency_2bins(by_path[p]) for p in U.path]\nU[\"click_latency_d5\"] = [g.click_latency_2bins(by_path[p], delay=0.005) for p in U.path]\nn_click_seq = pd.Series([sum(s.split(\"_\")[0] == \"CLICK\" for s in by_path[p][\"sequential_types\"]) for p in U.path])\nhas = {t: U.types.map(lambda x, t=t: t in x) for t in [\"CF\", \"CLICK\", \"SR\", \"NOISE\", \"SPS\", \"CVC\"]}\nclick_spikes = pd.Series([sum(len(s) for s in g.trials_of(by_path[p], \"CLICK\")[1]) for p in U.path])\nprint(\"CLICK sequential recordings per unit:\", n_click_seq[has[\"CLICK\"]].value_counts().to_dict(),\n      \"; trials per CLICK recording:\",\n      pd.Series([len(g.trials_of(by_path[p], \"CLICK\")[0]) for p in U.path[has[\"CLICK\"]]]).value_counts().to_dict())\nprint(\"CLICK units with 75 spikes or fewer (not analysed by Clickextract_func.m):\", int((has[\"CLICK\"] & (click_spikes <= 75)).sum()))\ncounts = pd.DataFrame({\n    \"paper\": [119, 261, 203, 143, 22, 135],\n    \"reading_1\": [int(U.cf.notna().sum()), int((has[\"CLICK\"] & (n_click_seq == 1) & U.click_latency.notna()).sum()),\n                  int(U.sr_SR.notna().sum()), int(has[\"NOISE\"].sum()), int(has[\"SPS\"].sum()), int(has[\"CVC\"].sum())],\n    \"reading_2\": [int(has[t].sum()) for t in [\"CF\", \"CLICK\", \"SR\", \"NOISE\", \"SPS\", \"CVC\"]],\n}, index=[\"CF\", \"CLICK\", \"SR\", \"NOISE\", \"SPS\", \"CVC\"])\ncounts[\"click_delay_5ms\"] = counts.reading_1\ncounts.loc[\"CLICK\", \"click_delay_5ms\"] = int((has[\"CLICK\"] & U.click_latency_d5.notna()).sum())\nprint(counts.to_string())\nfor r in [\"reading_1\", \"reading_2\"]:\n    print(f\"{r}: {int((counts[r] == counts.paper).sum())} of 6 match\")\n\"\"\", tags=[\"claim:recording-type-counts\"])\n\nmd(r\"\"\"\n**Result: partially reproduced.** Five of six counts match under both readings: CF 119, SR 203,\nNOISE 143, SPS 22 and CVC 135. CLICK does not: 275 units have a CLICK recording (each one\nrecording), and 271 of them give a 2-bin latency with the paper's function (272 with a 5 ms\nclick delay), against 261 in the Fig. 7 legend. The 10 or 14 extra units cannot be traced: the\nfiles carry no stored latency, so it cannot be told whether the paper's latencies were NaN for\nthem, or whether some of these units had a second CLICK recording in the MATLAB files that the\ncode would leave out.\n\"\"\")\n\nmd(r\"\"\"\n## fig7-sampling-by-age\n\n> No SR, SPS or CVC recordings were obtained in middle-aged gerbils, and SPS responses were recorded\n> only in young adults.\n\"\"\")\n\ncode(r\"\"\"\ntab = pd.DataFrame({t: U[has[t]].group.value_counts() for t in [\"CF\", \"CLICK\", \"SR\", \"NOISE\", \"SPS\", \"CVC\"]}\n                   ).reindex([\"young\", \"middle\", \"old\"]).fillna(0).astype(int)\nprint(\"Units with a recording of each type, by age group:\")\nprint(tab.to_string())\nok = tab.loc[\"middle\", [\"SR\", \"SPS\", \"CVC\"]].sum() == 0 and tab.loc[[\"middle\", \"old\"], \"SPS\"].sum() == 0\nprint(\"No middle-aged SR, SPS or CVC, and SPS only in young adults:\", ok)\n\"\"\", tags=[\"claim:fig7-sampling-by-age\"])\n\nmd(r\"\"\"\n**Result: reproduced.** No middle-aged unit has an SR, SPS or CVC recording, and all 22 SPS units\nare from young adults.\n\"\"\")\n\nmd(r\"\"\"\n## isi-exclusion\n\n> Units with multiple inter-spike intervals below 0.6 ms, the absolute refractoriness of auditory\n> nerve fibres, were excluded from the dataset.\n\nWithin-trial ISIs (checkAN.m). Readings: (a) any recording of the unit with two or more ISIs\n< 0.6 ms; (b) two or more pooled over all the unit's recordings; (c) as (a) for the BF recording\nonly. A recording here is a recording type of the unit (each type occurs once per unit, data\ncheck).\n\"\"\")\n\ncode(r\"\"\"\nisi = {p: g.short_isis(by_path[p]) for p in U.path}\nU[\"short_total\"] = [sum(v[0] for v in isi[p].values()) for p in U.path]\nU[\"short_max_rec\"] = [max(v[0] for v in isi[p].values()) for p in U.path]\nU[\"short_bf\"] = [isi[p].get(\"BF\", (0, 0))[0] for p in U.path]\nU[\"isi_total\"] = [sum(v[1] for v in isi[p].values()) for p in U.path]\nfail = {\"a\": int((U.short_max_rec >= 2).sum()), \"b\": int((U.short_total >= 2).sum()), \"c\": int((U.short_bf >= 2).sum())}\nprint(\"Units failing (two or more ISIs < 0.6 ms):\", fail, \"of\", len(U))\nprint(\"Units with at least one ISI < 0.6 ms:\", int((U.short_total >= 1).sum()))\nprint(\"\\nDistribution of a unit's count of short ISIs (pooled):\")\nprint(U.short_total.value_counts().sort_index().pipe(lambda s: pd.concat([s[s.index <= 10], pd.Series({\">10\": s[s.index > 10].sum()})])).to_string())\nfrac = U.short_total / U.isi_total.where(U.isi_total > 0)\nprint(f\"\\nShort ISIs as a fraction of all ISIs, among failing units (b): median {frac[U.short_total >= 2].median():.4f}, \"\n      f\"max {frac[U.short_total >= 2].max():.3f}\")\nprint(\"Failing units (a) by age group:\", U[U.short_max_rec >= 2].group.value_counts().to_dict(),\n      \"; by animal: in\", U[U.short_max_rec >= 2].animal.nunique(), \"of\", U.animal.nunique(), \"animals\")\nshort = np.concatenate([np.diff(s)[np.diff(s) < g.SHORT_ISI_S] for u in units for s in u[\"spikes\"] if len(s) > 1])\nprint(f\"\\nAll short ISIs: {len(short)}; in ms, quantiles 0, 0.25, 0.5, 0.75, 1:\",\n      np.round(np.quantile(short * 1000, [0, 0.25, 0.5, 0.75, 1]), 3).tolist())\nprint(\"Of them below 0.1 ms:\", int((short < 0.0001).sum()), \"; 0.1 to 0.3 ms:\", int(((short >= 0.0001) & (short < 0.0003)).sum()),\n      \"; 0.3 to 0.6 ms:\", int((short >= 0.0003).sum()))\nfor lim in [0.0003, 0.0001]:\n    n = sum(any(sum(int(np.sum(np.diff(s) < lim)) for s in g.trials_of(by_path[p], e)[1]) >= 2\n                for e in by_path[p][\"trials\"].experiment.unique()) for p in U.path)\n    print(f\"Variant limit {lim*1000:.1f} ms, reading (a): {n} units fail\")\n\"\"\", tags=[\"claim:isi-exclusion\"])\n\nmd(r\"\"\"\n**Result: not reproduced.** Units with two or more within-trial ISIs below 0.6 ms are in the\ndataset under every reading: 370 of 1160 under (a), 391 under (b) and 148 under (c); 538 units\nhave at least one. Most such units have a few short ISIs among thousands (the median fraction is\nprinted above), and many short ISIs are below 0.1 ms, two or three samples apart, which looks like\none spike detected twice. The paper's check was visual and its rule (\"multiple\") may have meant\nmore than two; the outputs show that with any of the three readings the dataset holds units the\nstated rule would exclude.\n\"\"\")\n\nmd(r\"\"\"\n## no-prepotentials\n\n> No median spike waveform showed a prepotential, which would mark a ventral cochlear nucleus bushy\n> cell.\n\n**Blocked: methods underspecified.** The check was a visual inspection of the median spike\nwaveform (checkAN.m); neither the paper nor its code gives a rule for a prepotential, so no\ncriterion fixed from the paper can judge it (claims file). The raw voltage traces are in the files\n(`acquisition`), so the waveforms could be inspected; they are not read here.\n\"\"\")\n\nmd(r\"\"\"\n## rlf-monotonic\n\n> Rate-level functions were checked for atypical shapes ..., and units whose rate-level function was\n> nonmonotonic at levels below 80 dB SPL were excluded.\n\n**Blocked: methods underspecified.** The check was visual and the paper gives no rule for\nnonmonotonicity. As a description only (claims file): the stored rates and SDs are not in the\nfiles, so the rate per level is computed from the spike times in the stimulus window (helper,\n`rlf_rates`), and the units are counted whose mean rate falls between successive levels below\n80 dB SPL by more than the SD at the lower level.\n\"\"\")\n\ncode(r\"\"\"\ndrops, n_rlf = [], 0\nfor p in U.path[U.types.map(lambda x: \"RLF\" in x)]:\n    r = g.rlf_rates(by_path[p])\n    if r is None or len(r) < 2:\n        continue\n    n_rlf += 1\n    r = r[r.index < 80]\n    d = r[\"mean\"].diff().shift(-1)            # next level minus this level\n    drops.append(int(((-d) > r[\"std\"]).sum()))\ndrops = np.array(drops)\nprint(f\"RLF recordings: {n_rlf}; with a drop larger than the SD below 80 dB SPL: {int((drops >= 1).sum())} \"\n      f\"({np.mean(drops >= 1):.2f}); with two or more such drops: {int((drops >= 2).sum())}\")\n\"\"\", tags=[\"claim:rlf-monotonic\"])\n\nmd(r\"\"\"\n## fig5b-example\n\n> The example fibre of Fig. 5b (animal G220908, unit 3p_181) had a best frequency of 7.6 kHz and a\n> threshold of 19 dB SPL.\n\"\"\")\n\ncode(r\"\"\"\nrow = U[(U.animal == \"G220908\") & (U.unit == \"3p_181\")]\nprint(row[[\"path\", \"group\", \"bf\", \"rlf_threshold\", \"sr_best\", \"types\"]].to_string(index=False))\nu = by_path[row.path.iloc[0]]\nt = u[\"trials\"]\nbf_t = t[(t.experiment == \"BF\") & (t.frequency != g.SPONT)]\nrlf_t = t[(t.experiment == \"RLF\") & (t.frequency != g.SPONT)]\nprint(\"BF recording: levels (dB SPL)\", sorted(np.round(bf_t.level.unique(), 1)), \"; repetitions per frequency\",\n      sorted(bf_t.groupby(\"frequency\").size().unique()))\nprint(\"RLF recording: frequency\", sorted(rlf_t.frequency.unique()), \"; levels\", sorted(np.round(rlf_t.level.unique(), 1)),\n      \"; repetitions per level\", sorted(rlf_t.groupby(\"level\").size().unique()))\nprint(\"BF within 10% of 7.6 kHz:\", abs(row.bf.iloc[0] / 1000 - 7.6) <= 0.76,\n      \"; threshold within 10% of 19 dB:\", abs(row.rlf_threshold.iloc[0] - 19) <= 1.9)\n\"\"\", tags=[\"claim:fig5b-example\"])\n\nmd(r\"\"\"\n**Result: reproduced.** The unit's stored BF is 7620 Hz and its RLF threshold 19 dB SPL. Its BF\nrecording has 5 repetitions per frequency at one level, and its RLF recording 10 repetitions per\nlevel, as the legend says; the levels are printed above (the legend's 30 dB SPL for the BF\nrecording and 40 dB SPL for the RLF recording are the levels of the PSTH, 20 dB above threshold\nfor makePSTH.m's TestLevel).\n\"\"\")\n\nmd(r\"\"\"\n## fig6a-young-two-sensitive-regions\n\n> Fibres of young-adult gerbils show two regions of best sensitivity separated by a region around\n> 3 to 4 kHz with higher thresholds and fewer fibres; the highest thresholds are at 3.5 kHz.\n\nYoung-adult units with a stored BF and RLF threshold; mean threshold in 24 logarithmic BF bins\nfrom 0.3 to 20 kHz (a bin includes its upper edge), each plotted at its upper edge\n(check_dataset_units.m). Readings: (a) the largest bin mean over all bins; (b) the largest bin\nmean between the two sensitive regions, a local maximum with lower bin means on each side.\n\"\"\")\n\ncode(r\"\"\"\ny = U[U.group == \"young\"]\ne = np.logspace(np.log10(0.3), np.log10(20), 25)\nk = y.bf / 1000\nbins = []\nfor i in range(24):\n    m = (k > e[i]) & (k <= e[i + 1])\n    bins.append({\"lower_khz\": round(e[i], 2), \"plotted_at_khz\": round(e[i + 1], 2), \"units\": int(m.sum()),\n                 \"with_threshold\": int(y.rlf_threshold[m].notna().sum()), \"mean_threshold\": y.rlf_threshold[m].mean()})\nB6a = pd.DataFrame(bins)\nprint(B6a.round(1).to_string(index=False))\nfilled = B6a[B6a.mean_threshold.notna()].reset_index(drop=True)\na_top = filled.loc[filled.mean_threshold.idxmax()]\nprint(f\"\\nReading (a): highest bin mean {a_top.mean_threshold:.1f} dB at {a_top.plotted_at_khz} kHz (n = {a_top.with_threshold})\")\n# the two sensitive regions: the lowest bin mean below 3.48 kHz and the lowest above it\nlow = filled[filled.plotted_at_khz < 3.48]; high = filled[filled.plotted_at_khz > 3.48]\nlo_min, hi_min = low.mean_threshold.idxmin(), high.mean_threshold.idxmin()\nmid = filled.loc[lo_min + 1:hi_min - 1]\nb_top = mid.mean_threshold.idxmax()\nprint(f\"Sensitive regions: lowest means {filled.mean_threshold[lo_min]:.1f} dB at {filled.plotted_at_khz[lo_min]} kHz and \"\n      f\"{filled.mean_threshold[hi_min]:.1f} dB at {filled.plotted_at_khz[hi_min]} kHz\")\nprint(f\"Reading (b): highest mean between them {filled.mean_threshold[b_top]:.1f} dB at {filled.plotted_at_khz[b_top]} kHz; \"\n      f\"neighbours {filled.mean_threshold[b_top-1]:.1f} and {filled.mean_threshold[b_top+1]:.1f} dB\")\nprint(\"Units per bin around it (2.06 to 4.93 kHz):\", B6a[(B6a.plotted_at_khz > 2) & (B6a.plotted_at_khz < 5)].units.tolist())\nfig, ax = plt.subplots(figsize=(5, 3.5))\nfor grp, col in [(\"young\", \"b\"), (\"middle\", \"orange\"), (\"old\", \"r\")]:\n    d = U[U.group == grp]\n    ax.scatter(d.bf / 1000, d.rlf_threshold, s=6, color=col, alpha=0.5, label=grp)\nax.plot(B6a.plotted_at_khz, B6a.mean_threshold, \"b-\")\nax.set_xscale(\"log\"); ax.set_xlim(0.3, 20); ax.set_ylim(0, 100)\nax.set_xlabel(\"Best frequency (kHz)\"); ax.set_ylabel(\"Threshold (dB SPL)\"); ax.legend(fontsize=7)\nout = U[(U.rlf_threshold.notna()) & ((U.bf / 1000 < 0.3) | (U.bf / 1000 > 20) | (U.rlf_threshold > 100) | (U.rlf_threshold < 0))]\nprint(\"Points outside the axes:\", len(out), \"; thresholds range\", round(U.rlf_threshold.min(), 1), \"to\", round(U.rlf_threshold.max(), 1))\n\"\"\", tags=[\"claim:fig6a-young-two-sensitive-regions\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Under reading (b) the young-adult mean threshold between the two sensitive\nregions is highest in the bin plotted at 3.48 kHz (27.6 dB SPL), with lower means on both sides\n(25.4 and 24.4 dB), and the two regions of best sensitivity have their lowest means at 1.73 kHz\n(20.9 dB) and 8.34 kHz (21.2 dB). Under reading (a) the highest bin mean of all is 36.7 dB at\n0.72 kHz, from 3 units. The bins from 2.06 to 4.14 kHz hold 30 to 34 units, fewer than the bins\nabove 4.14 kHz (43 to 83) but not fewer than those from 0.86 to 2.06 kHz (31 to 36).\n\"\"\")\n\nmd(r\"\"\"\n## fig6b-young-bf-gap\n\n> Among young-adult fibres, the fewest best frequencies fall in the bin bordered by 2.5 and 3.0 kHz.\n\nHistogram of young-adult stored BFs, edges logspace(log10(200), log10(20000), 25) Hz; the named bin\nis 2423 to 2936 Hz. Readings: (a) fewest of all bins between the lowest and highest non-empty\nbins (ties allowed); (b) fewer units than both neighbours.\n\"\"\")\n\ncode(r\"\"\"\ne = np.logspace(np.log10(200), np.log10(20000), 25)\nh, _ = np.histogram(y.bf.dropna(), e)\nH = pd.DataFrame({\"lower_hz\": np.round(e[:-1]).astype(int), \"upper_hz\": np.round(e[1:]).astype(int), \"units\": h})\nprint(H.to_string(index=False))\ni = int(np.flatnonzero(H.lower_hz == 2423)[0])\nnz = np.flatnonzero(h)\nspan = h[nz[0]:nz[-1] + 1]\nprint(f\"\\nBin 2423-2936 Hz: {h[i]} units; neighbours {h[i-1]} and {h[i+1]}\")\nprint(f\"Reading (a): fewest in the non-empty span is {span.min()} (bin {H.lower_hz[nz[0] + span.argmin()]} Hz); holds: {h[i] == span.min()}\")\nprint(f\"Reading (b): fewer than both neighbours: {h[i] < h[i-1] and h[i] < h[i+1]}\")\nmid = H[(H.lower_hz >= 1363) & (H.upper_hz <= 4309)]\nprint(\"Bins from 1363 to 4309 Hz:\", mid.units.tolist(), \"; the fewest there:\", mid.units.min(),\n      \"in bins\", mid[mid.units == mid.units.min()].lower_hz.tolist())\nprint(\"Total young units with a BF:\", int(h.sum()), \"; plotted range\", int(y.bf.min()), \"to\", int(y.bf.max()), \"Hz\")\n\"\"\", tags=[\"claim:fig6b-young-bf-gap\"])\n\nmd(r\"\"\"\n**Result: not reproduced.** The bin from 2423 to 2936 Hz holds 34 young-adult units. It is not the\nfewest of the non-empty span (the lowest bin, 356 Hz, holds 1, and the bins below 766 Hz hold 1 to\n11), and it is not a local minimum: its neighbours hold 34 and 35. Among the bins from 1363 to\n4309 Hz it ties for the fewest (34) with two others, so the dip in the histogram is shallow; with\nthe code's bins the stated bin is not the one with the fewest fibres.\n\"\"\")\n\nmd(r\"\"\"\n## fig6c-sr-distributions\n\n> Among high-frequency fibres (BF above 3.5 kHz) there is a cluster with low spontaneous rates,\n> and low-frequency fibres have a bimodal distribution of spontaneous rate with modes near 5 and 60\n> spikes/s.\n\nYoung-adult units, SR as the code's best estimate, split at BF 3.5 kHz, histogram of 5 spikes/s\nbins from 0 to 200. A mode is a local maximum (more units than both neighbours, or the first bin\nwhen it exceeds the second); the two largest are taken, separated by a bin with fewer units than\nboth.\n\"\"\")\n\ncode(r\"\"\"\ndef local_maxima(h):\n    out = []\n    for i in range(len(h)):\n        left = h[i - 1] if i > 0 else -1\n        right = h[i + 1] if i < len(h) - 1 else -1\n        if h[i] > left and h[i] > right:\n            out.append(i)\n    return out\n\nedges = np.arange(0, 205, 5)\nres6c = {}\nfor name, m in [(\"low BF (<= 3.5 kHz)\", y.bf <= 3500), (\"high BF (> 3.5 kHz)\", y.bf > 3500)]:\n    h, _ = np.histogram(y.sr_best[m].dropna(), edges)\n    lm = local_maxima(h)\n    top2 = sorted(sorted(lm, key=lambda i: -h[i])[:2])\n    res6c[name] = (h, lm, top2)\n    print(f\"{name}: {int(m.sum())} units, {int(y.sr_best[m].notna().sum())} with an SR; counts per 5 spikes/s bin (0 to 150):\")\n    print(\"  \", h[:30].tolist())\n    print(\"   local maxima (bin start, count):\", [(int(edges[i]), int(h[i])) for i in lm])\n    print(\"   two largest:\", [(int(edges[i]), int(h[i])) for i in top2],\n          \"; fewest between them:\", int(h[top2[0]:top2[1] + 1].min()) if len(top2) == 2 else None)\nh, lm, top2 = res6c[\"low BF (<= 3.5 kHz)\"]\nlow_ok = len(top2) == 2 and edges[top2[0]] in (0, 5) and 50 <= edges[top2[1]] and edges[top2[1] + 1] <= 70 \\\n    and h[top2[0]:top2[1] + 1].min() < min(h[top2[0]], h[top2[1]])\nhh, lmh, _ = res6c[\"high BF (> 3.5 kHz)\"]\nlargest_high = max(lmh, key=lambda i: hh[i])\nhigh_ok = edges[largest_high + 1] <= 18\nprint(\"\\nLow BF bimodal with modes in 0-10 and 50-70 spikes/s:\", low_ok)\nprint(f\"High BF largest local maximum at {int(edges[largest_high])}-{int(edges[largest_high+1])} spikes/s, below 18: {high_ok}\")\nprint(\"Fraction below 18 spikes/s: low BF\", round(float((y.sr_best[y.bf <= 3500] < 18).mean()), 3),\n      \"; high BF\", round(float((y.sr_best[y.bf > 3500] < 18).mean()), 3))\nprint(\"SR range (young):\", y.sr_best.min(), \"to\", round(y.sr_best.max(), 1), \"; above 200:\", int((y.sr_best > 200).sum()))\n\"\"\", tags=[\"claim:fig6c-sr-distributions\"])\n\nmd(r\"\"\"\n**Result: reproduced.** In low-BF young-adult units the two largest modes of spontaneous rate are\nthe bins 0 to 5 spikes/s (27 units) and 55 to 60 spikes/s (21 units), separated by bins of fewer\nunits; both lie in the bins the criterion allows. In high-BF units the largest local maximum is\nthe 0 to 5 spikes/s bin (66 units), below the 18 spikes/s cutoff.\n\"\"\")\n\nmd(r\"\"\"\n## fig6d-max-phase-locking-bf\n\n> The highest best frequency at which significant phase locking was recorded in young-adult gerbils\n> was 4.6 kHz.\n\nVector strength and its p-value per level of the PH recording, recomputed from the spike times\nwith PHextract_func.m and TytoView_calcVS.m (helper); significant when p is not NaN and < 0.001.\n\"\"\")\n\ncode(r\"\"\"\nU[\"max_vs\"] = [g.max_significant_vs(by_path[p]) for p in U.path]\nph = U[U.types.map(lambda x: \"PH\" in x)]\nnfreq = pd.Series([g.vector_strength_by_level(by_path[p]).n_freqs.max() for p in ph.path])\nprint(\"Units with a PH recording:\", len(ph), \"; PH recordings with more than one tone frequency:\", int((nfreq > 1).sum()))\nprint(\"With a significant vector strength:\", int(ph.max_vs.notna().sum()), \"; by group:\",\n      ph[ph.max_vs.notna()].group.value_counts().to_dict())\nsig = ph[ph.max_vs.notna() & ph.bf.notna()]\nfor grp in [\"young\", \"middle\", \"old\"]:\n    s = sig[sig.group == grp].sort_values(\"bf\")\n    print(f\"{grp}: highest BF with significant phase locking {s.bf.max():.0f} Hz; next highest {s.bf.iloc[-4:-1].tolist()}\")\nys = ph[ph.group == \"young\"]\nprint(\"Young PH units with BF above 4.6 kHz:\", ys[ys.bf > 4600][[\"bf\", \"max_vs\"]].to_dict(\"records\"))\ntop = sig[sig.group == \"young\"].bf.max() / 1000\nprint(f\"Within 10% of 4.6 kHz: {abs(top - 4.6) <= 0.46}\")\nfor p_lim in [0.01, 0.0001]:\n    alt = []\n    for p in ph.path[ph.group == \"young\"]:\n        v = g.vector_strength_by_level(by_path[p])\n        if ((v.p < p_lim) & v.p.notna()).any():\n            alt.append(U.loc[U.path == p, \"bf\"].iloc[0])\n    print(f\"Variant p < {p_lim}: highest young BF {np.nanmax(alt):.0f} Hz\")\n\"\"\", tags=[\"claim:fig6d-max-phase-locking-bf\"])\n\nmd(r\"\"\"\n**Result: reproduced.** With vector strength recomputed by the paper's function, the highest BF of a\nyoung-adult unit with significant phase locking (p < 0.001) is 4598 Hz, 4.6 kHz. The value is the\nsame with p < 0.01 or p < 0.0001.\n\"\"\")\n\nmd(r\"\"\"\n## fig6d-highest-vs-low-bf-low-sr\n\n> The highest vector strengths are found among fibres with low best frequencies (below 1.5 kHz) and\n> low spontaneous rates (below 18 spikes/s).\n\nMaximum significant vector strength per unit, SR best estimate, stored BF. Readings, for young\nadults and for all ages: (a) the unit with the largest maximum vector strength has BF < 1.5 kHz\nand SR < 18; (b) of the four groups the two cutoffs form, the median is highest in low-BF low-SR.\n\"\"\")\n\ncode(r\"\"\"\nres = []\nfor name, s in [(\"young\", sig[sig.group == \"young\"]), (\"all ages\", sig)]:\n    grp4 = np.where(s.bf < 1500, \"BF<1.5k\", \"BF>=1.5k\") + \" / \" + np.where(s.sr_best < 18, \"SR<18\", \"SR>=18\")\n    tab = s.groupby(grp4).max_vs.agg([\"median\", \"max\", \"size\"]).round(3)\n    topu = s.loc[s.max_vs.idxmax()]\n    ra = bool(topu.bf < 1500 and topu.sr_best < 18)\n    rb = tab[\"median\"].idxmax() == \"BF<1.5k / SR<18\"\n    res.append((name, ra, rb))\n    print(f\"{name}:\\n{tab.to_string()}\")\n    print(f\"  largest: vs {topu.max_vs:.3f}, BF {topu.bf:.0f} Hz, SR {topu.sr_best} spikes/s; reading (a) holds: {ra}; reading (b) holds: {rb}\")\n    print(\"  five largest:\", s.nlargest(5, \"max_vs\")[[\"bf\", \"sr_best\", \"max_vs\"]].round(3).to_dict(\"records\"))\nlow = sig[(sig.group == \"young\")]\nlo = low[(low.bf < 1500) & (low.sr_best < 18)].max_vs; hi = low[(low.bf < 1500) & (low.sr_best >= 18)].max_vs\nprint(f\"Young, BF < 1.5 kHz: low-SR against high-SR, Mann-Whitney p = {stats.mannwhitneyu(lo, hi).pvalue:.3g} \"\n      f\"(n {len(lo)} and {len(hi)}; not part of the criterion)\")\nprint(\"All readings hold:\", all(a and b for _, a, b in res))\n\"\"\", tags=[\"claim:fig6d-highest-vs-low-bf-low-sr\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Under all four readings the highest vector strengths are in low-BF,\nlow-SR fibres: the largest maximum vector strength (0.882) is from a unit with BF 428 Hz and SR\n1.25 spikes/s, and the median is highest in the low-BF low-SR group (0.821 in 6 young-adult\nunits, 0.804 in 19 over all ages), above low-BF high-SR (0.695 and 0.702). The low-SR group is\nsmall; the comparison of its values with the low-BF high-SR group is printed above.\n\"\"\")\n\nmd(r\"\"\"\n## fig7a-cf-matches-bf\n\n> Characteristic frequency from the CF recordings correlates strongly with best frequency from the\n> BF recordings, with no systematic deviation towards higher or lower frequencies.\n\nCF recomputed from the CF recording (helper; the automatic first pass of CFextract_func.m, without\nthe experimenter's manual corrections, which are not in the files); BF stored. Pearson correlation\nof log CF with log BF (Spearman as a variant), median log2(CF/BF) with a 95% bootstrap interval\n(10,000 resamples, seed 1).\n\"\"\")\n\ncode(r\"\"\"\nrng = np.random.default_rng(1)\nc = U[U.cf.notna() & U.bf.notna()]\npr = stats.pearsonr(np.log(c.cf), np.log(c.bf)); sp = stats.spearmanr(c.cf, c.bf)\nl2 = np.log2(c.cf / c.bf).values\nboot = np.median(rng.choice(l2, size=(10000, len(l2))), axis=1)\nlo, hi = np.percentile(boot, [2.5, 97.5])\nprint(f\"Units with a CF and a BF: {len(c)} (CF units {int(has['CF'].sum())}, of which without BF {int((has['CF'] & U.bf.isna()).sum())})\")\nprint(f\"Pearson r(log CF, log BF) = {pr.statistic:.3f}, p = {pr.pvalue:.2g}; Spearman rho = {sp.statistic:.3f}, p = {sp.pvalue:.2g}\")\nprint(f\"Median log2(CF/BF) = {np.median(l2):.4f} (95% CI {lo:.4f} to {hi:.4f}); median ratio {2**np.median(l2):.4f}\")\nprint(f\"Units with CF above BF: {int((l2 > 0).sum())}, below: {int((l2 < 0).sum())}, equal: {int((l2 == 0).sum())}\")\nprint(f\"|log2(CF/BF)| > 0.5 octave: {int((np.abs(l2) > 0.5).sum())}\")\nprint(\"By group:\", c.assign(l2=l2).groupby(\"group\").l2.agg([\"median\", \"size\"]).round(3).to_dict(\"index\"))\nfig, ax = plt.subplots(figsize=(4, 4))\nax.scatter(c.bf / 1000, c.cf / 1000, s=10)\nax.plot([0.3, 20], [0.3, 20], \"k--\"); ax.set_xscale(\"log\"); ax.set_yscale(\"log\")\nax.set_xlabel(\"BF (kHz)\"); ax.set_ylabel(\"CF, recomputed (kHz)\")\nprint(\"Plotted ranges: BF\", c.bf.min(), \"to\", c.bf.max(), \"Hz; CF\", c.cf.min(), \"to\", c.cf.max(), \"Hz\")\n\"\"\", tags=[\"claim:fig7a-cf-matches-bf\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Over 114 units with a recomputed CF and a stored BF, log CF and log BF\ncorrelate with r = 0.973 (p = 2.1e-73; Spearman 0.964), and the median CF/BF ratio is 1.003, within\n10% of 1, with its bootstrap interval printed above. The CF is the automatic first pass of the\npaper's function; the experimenter's manual corrections are not in the files.\n\"\"\")\n\nmd(r\"\"\"\n## fig7b-click-latency-bf\n\n> Click latency is strongly negatively correlated with best frequency, reflecting the travelling\n> wave delay along the cochlea.\n\nUnits with one CLICK recording, a 2-bin latency recomputed with the paper's function, and a\nstored BF; Pearson correlation of latency with log BF, Spearman as a variant. The click delay is\nnot in the files; the main reading assumes 7.75 ms, the delay of every tone recording, and 5 ms is\nshown as a variant.\n\"\"\")\n\ncode(r\"\"\"\nfor col, label in [(\"click_latency\", \"delay 7.75 ms\"), (\"click_latency_d5\", \"delay 5 ms\")]:\n    k = U[U[col].notna() & U.bf.notna()]\n    pr = stats.pearsonr(k[col], np.log(k.bf)); sp = stats.spearmanr(k[col], k.bf)\n    print(f\"{label}: {len(k)} units; latency {k[col].min()*1000:.2f} to {k[col].max()*1000:.2f} ms \"\n          f\"(median {k[col].median()*1000:.2f}); Pearson r = {pr.statistic:.3f}, p = {pr.pvalue:.2g}; \"\n          f\"Spearman rho = {sp.statistic:.3f}, p = {sp.pvalue:.2g}\")\nk = U[U.click_latency.notna() & U.bf.notna()]\nprint(\"Median latency (ms) by BF band:\",\n      k.groupby(pd.cut(k.bf, [0, 1000, 2000, 4000, 8000, 20000])).click_latency.median().mul(1000).round(2).to_dict())\nprint(\"By age group, Pearson r:\", {grp: round(stats.pearsonr(d.click_latency, np.log(d.bf)).statistic, 3)\n                                  for grp, d in k.groupby(\"group\") if len(d) > 3})\nfig, ax = plt.subplots(figsize=(5, 3.5))\nax.scatter(k.bf / 1000, k.click_latency * 1000, s=8)\nax.set_xscale(\"log\"); ax.set_xlim(0.3, 20); ax.set_ylim(0, 3.5)\nax.set_xlabel(\"BF (kHz)\"); ax.set_ylabel(\"Click latency, 2-bin (ms)\")\nprint(\"Points outside the axes:\", int(((k.click_latency * 1000 > 3.5) | (k.bf < 300) | (k.bf > 20000)).sum()))\n\"\"\", tags=[\"claim:fig7b-click-latency-bf\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Over 268 units the recomputed 2-bin click latency falls with BF: Pearson\nr = -0.882 with log BF (p = 5.9e-89), Spearman -0.864. With a 5 ms click delay the correlations\nare -0.662 and -0.820, both negative with p < 0.05. With 7.75 ms the latencies span 0.42 to 2.78\nms, inside the 0 to 3.5 ms axis of Fig. 7b, which is consistent with the assumed delay.\n\"\"\")\n\nmd(r\"\"\"\n## fig7ab-representative-sampling\n\n> The best-frequency distributions of the units with CF and with CLICK recordings are\n> representative of the distribution of the full dataset.\n\nReference (i) young-adult BFs or (ii) all units' BFs; comparison (a) two-sample KS test of log BF,\nno difference at p < 0.05, or (b) the subset's median BF within 10% of the reference's. Stored\nBFs. The CF subset is the units with a CF recording; the CLICK subset is the units with a\nrecomputed latency (reading 1 of recording-type-counts), with all CLICK units as a variant.\n\"\"\")\n\ncode(r\"\"\"\nrefs = {\"(i) young\": np.log(U[U.group == \"young\"].bf.dropna()), \"(ii) all\": np.log(U.bf.dropna())}\nsubsets = {\"CF\": U[has[\"CF\"]].bf.dropna(), \"CLICK\": U[U.click_latency.notna()].bf.dropna(),\n           \"CLICK, any recording\": U[has[\"CLICK\"]].bf.dropna()}\nrows = []\nfor sname, s in subsets.items():\n    for rname, r in refs.items():\n        ks = stats.ks_2samp(np.log(s), r)\n        ratio = np.exp(np.median(np.log(s))) / np.exp(np.median(r))\n        rows.append({\"subset\": sname, \"n\": len(s), \"reference\": rname, \"ks_D\": round(ks.statistic, 3),\n                     \"ks_p\": round(ks.pvalue, 4), \"(a) holds\": ks.pvalue >= 0.05,\n                     \"median_subset_hz\": round(float(np.exp(np.median(np.log(s))))),\n                     \"median_ref_hz\": round(float(np.exp(np.median(r)))), \"ratio\": round(ratio, 3),\n                     \"(b) holds\": abs(ratio - 1) <= 0.1})\nR = pd.DataFrame(rows)\nprint(R.to_string(index=False))\nfor reading in [\"(a) holds\", \"(b) holds\"]:\n    for rname in refs:\n        both = R[(R.reference == rname) & R.subset.isin([\"CF\", \"CLICK\"])][reading].all()\n        print(f\"Reading {reading[:3]} with reference {rname}: holds for both CF and CLICK: {both}\")\nprint(\"\\nCF units by age group:\", U[has[\"CF\"]].group.value_counts().to_dict(),\n      \"; BF quartiles (Hz) CF\", np.percentile(subsets[\"CF\"], [25, 50, 75]).round().tolist(),\n      \"all\", np.percentile(U.bf.dropna(), [25, 50, 75]).round().tolist())\n\"\"\", tags=[\"claim:fig7ab-representative-sampling\"])\n\nmd(r\"\"\"\n**Result: not reproduced.** No reading holds for both subsets. The CF units' BFs differ from the\nreference under both readings: KS p = 0.018 against young adults and 0.003 against all units, and\ntheir median BF (3454 Hz) is 0.75 times the reference's (4589 and 4592 Hz). The CLICK units'\nBFs do not differ by the KS test (p = 0.20 and 0.45), but their median (5180 Hz) is 1.13 times\nthe reference's, outside 10%. The CF part fails every reading, so the outcome does not depend on\nthe choice among them; whether the paper meant a visual likeness that a shift of this size would\nnot contradict cannot be told from its text.\n\"\"\")\n\nmd(r\"\"\"\n## old-success-rate\n\n> Successful single-fibre recordings were obtained in 43% of old gerbils that were tried, against\n> 88% of young adults.\n\n**Blocked: data missing.** The denominators are the animals operated on, including those that gave\nno single units. The dataset holds only animals with recorded units (every one of the 104 subjects\nhas at least one unit file, data check), and neither the files nor the dandiset's metadata list\nthe animals that gave none.\n\"\"\")\n\ncode(r\"\"\"\nprint(\"Animals in the dataset with no unit file:\", int((A.units == 0).sum()), \"; animals:\", len(A))\nprint(\"Dandiset description mentions unsuccessful experiments:\",\n      any(w in meta[\"description\"].lower() for w in [\"unsuccessful\", \"success\", \"failed\"]))\n\"\"\", tags=[\"claim:old-success-rate\"])\n\nmd(r\"\"\"\n## psth-primary-like\n\n> Responses to tones at 20 and 30 dB above threshold were examined for non-primary-like shapes ...\n> and units with clearly non-primary-like responses were excluded.\n\n**Blocked: methods underspecified.** The check was visual; the paper and its code give no rule\nfor a non-primary-like shape (claims file).\n\"\"\")\n\ncode(r\"\"\"\nprint(f\"Notebook run time: {(time.time() - started) / 60:.1f} min\")\n\"\"\")\n\nmd(r\"\"\"\n## Summary\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning\nand the differences from the paper's method.\n\n| Claim | Outcome |\n|---|---|\n| table1-animals-units | reproduced |\n| table1-age-abr-weight | reproduced (ABR read as character code) |\n| table1-bf-range | reproduced |\n| fig3-abr-age | reproduced (ABR read as character code) |\n| females-fewer-in-old | reproduced |\n| oxygen-78 | reproduced |\n| complex-stimuli-experiments | reproduced |\n| recording-type-counts | partially reproduced (CLICK 271 or 275, not 261) |\n| fig7-sampling-by-age | reproduced |\n| isi-exclusion | not reproduced |\n| no-prepotentials | blocked: methods underspecified |\n| rlf-monotonic | blocked: methods underspecified |\n| fig5b-example | reproduced |\n| fig6a-young-two-sensitive-regions | reproduced (reading b) |\n| fig6b-young-bf-gap | not reproduced |\n| fig6c-sr-distributions | reproduced |\n| fig6d-max-phase-locking-bf | reproduced (recomputed vector strength) |\n| fig6d-highest-vs-low-bf-low-sr | reproduced (recomputed vector strength) |\n| fig7a-cf-matches-bf | reproduced (recomputed CF) |\n| fig7b-click-latency-bf | reproduced (recomputed latency, assumed click delay) |\n| fig7ab-representative-sampling | not reproduced |\n| old-success-rate | blocked: data missing |\n| psth-primary-like | blocked: methods underspecified |\n\n**How the analysis differs from the paper's.** The paper's scripts read stored analysed outcomes\nfrom the MATLAB files. The NWB files keep only the best frequency, spontaneous rate and threshold\nper recording, so the characteristic frequency, vector strength and click latency are recomputed\nfrom the spike times with the paper's functions, without the experimenter's manual corrections\nfor the CF. The click delay is not in the files and is assumed to be 7.75 ms. The ABR threshold is\nread from a character code.\n\n**What was found about the dataset.** All 1160 units and 104 animals of Table 1 are there, with\nages, sexes, weights, oxygen, and the recording types of Fig. 7, and every count and mean of\nTable 1 matches. The ABR threshold is stored as a single character whose code point is the\nthreshold. The CF, vector strength with its p-value, and click latencies that the paper describes\nas stored outcomes are not in the NWB files, and the click delay is missing from the trial table.\nMany units have within-trial inter-spike intervals below 0.6 ms, often below 0.1 ms. The archive's\nsummary lists the recordings as voltage clamp, while they are extracellular recordings of\nsingle fibres.\n\"\"\")\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"display_name\": \"Python 3\", \"language\": \"python\", \"name\": \"python3\"}\nnbf.write(nb, sys.argv[1])\n"
}
```

```
File created successfully at: /tmp/claude/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/001262-heeringa-2024; . $TMPDIR/env/bin/activate; uv pip install -q nbformat nbconvert ipykernel 2>&1|tail -2; python /tmp/claude/build_nb.py reproduce_heeringa_2024.ipynb && cp reproduce_heeringa_2024.ipynb $TMPDIR/dev.ipynb && cd $TMPDIR && cp entries/001262-heeringa-2024/gerbil_an.py . && time jupyter nbconvert --to notebook --execute dev.ipynb --output dev_out.ipynb --ExecutePreprocessor.timeout=3000 2>&1 | tail -5
```

```
[NbConvertApp] Converting notebook dev.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 235993 bytes to dev_out.ipynb

real	3m22.006s
user	2m55.173s
sys	0m11.551s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; python - <<'EOF'
import json
nb=json.load(open('dev_out.ipynb'))
for c in nb['cells']:
    if c['cell_type']=='code':
        tags=c['metadata'].get('tags',[])
        print('-----', tags)
        for o in c.get('outputs',[]):
            if o['output_type']=='stream': print(''.join(o['text'])[:6000])
            elif o['output_type']=='error': print('ERROR', o['ename'], o['evalue'])
EOF
```

```
----- []
read 1160 files of dandiset 001262 version 0.241205.0959 in 110 s

----- ['sanity']
Versions 0.241205.0929 and 0.241205.0959: 1160 and 1160 files; same paths and blobs: True

Archive summary: subjects 104 ; files 1160 ; species ['Meriones unguiculatus'] ; variableMeasured ['VoltageClampStimulusSeries', 'Units'] ; measurementTechnique ['voltage clamp technique', 'spike sorting technique']

----- ['sanity']
Units: 1160 ; animals: 104 ; species in files: ['Meriones unguiculatus']
Each file's subject folder matches its subject_id: True
Animal metadata constant within each animal (age, sex, weight, ABR, oxygen, speaker): True
Every trial's tag starts with its recording type: True
Recording types in the analysis table and in the trials agree: True ; analysis rows with a repeated type: 0
Units per recording type:
BF       1152
RLF       952
PH        281
CLICK     275
SR        203
[... 377 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude; python - <<'EOF'
p='build_nb.py'; s=open(p).read()
rep=[
("""fire far more, in almost every recording, and the difference falls back after the tone ends
(57.75 ms).""","""fire far more (median difference 147 spikes/s at 10 to 15 ms, with tone above silent in 96% of
recordings), and after the tone ends (57.75 ms) the tone trials fall below the silent ones, the
offset suppression expected of auditory nerve fibres."""),
("""print(B6a.round(1).to_string(index=False))""","""print(B6a.round({"mean_threshold": 1}).to_string(index=False))"""),
("""**Result: reproduced.** The unit's stored BF is 7620 Hz and its RLF threshold 19 dB SPL. Its BF
recording has 5 repetitions per frequency at one level, and its RLF recording 10 repetitions per
level, as the legend says; the levels are printed above (the legend's 30 dB SPL for the BF
recording and 40 dB SPL for the RLF recording are the levels of the PSTH, 20 dB above threshold
for makePSTH.m's TestLevel).""","""**Result: reproduced.** The unit's stored BF is 7620 Hz and its RLF threshold 19 dB SPL. As the
legend says, its BF recording is at 30 dB SPL with 5 repetitions per frequency, and its RLF
recording (at 7700 Hz) has 10 repetitions per level and includes 40 dB SPL."""),
("""**Result: not reproduced.** Units with two or more within-trial ISIs below 0.6 ms are in the
dataset under every reading: 370 of 1160 under (a), 391 under (b) and 148 under (c); 538 units
have at least one. Most such units have a few short ISIs among thousands (the median fraction is
printed above), and many short ISIs are below 0.1 ms, two or three samples apart, which looks like
one spike detected twice. The paper's check was visual and its rule ("multiple") may have meant
more than two; the outputs show that with any of the three readings the dataset holds units the
stated rule would exclude.""","""**Result: not reproduced.** Units with two or more within-trial ISIs below 0.6 ms are in the
dataset under every reading: 370 of 1160 under (a), 391 under (b) and 148 under (c), from 79 of
the 104 animals; 538 units have at least one. In the failing units the short ISIs are a small
fraction of all ISIs (median 0.0013, largest 0.223), and 162 units have more than 10. Of the
13,904 short ISIs, 10,192 are between 0.3 and 0.6 ms and 1171 below 0.1 ms. With a limit of
0.3 ms, 140 units still fail under (a); with 0.1 ms, 5 do. The paper's check was visual and does
not say what "multiple" means; under the three readings the claims file names, the dataset holds
units the stated rule would exclude."""),
("""**Result: reproduced.** With vector strength recomputed by the paper's function, the highest BF of a
young-adult unit with significant phase locking (p < 0.001) is 4598 Hz, 4.6 kHz. The value is the
same with p < 0.01 or p < 0.0001.""","""**Result: reproduced.** With vector strength recomputed by the paper's function, the highest BF of a
young-adult unit with significant phase locking (p < 0.001, the Methods' threshold) is 4598 Hz,
4.6 kHz; the next highest are 4121 to 4377 Hz. The value depends on the threshold: with p < 0.01
it is 6539 Hz, with p < 0.0001 it is 4377 Hz. No young unit with a higher BF (27 PH units from
4718 to 12,359 Hz) reaches p < 0.001."""),
("""ages 5.55, 22.49 and 38.33 months, ABR thresholds 18.10, 34.17 and 49.03 dB SPL, weights 74.61,
83.35 and 86.41 g. The SDs and ranges printed also match Table 1 (for example ABR SD 5.33, 10.19
and 18.00, range 20 to 85 in old animals). The ABR values rest on reading the notes' character as
its code point; 10 young adults and 1 middle-aged animal have no ABR threshold, and the paper's
means are also over fewer animals than the group sizes if they omit the same ones, which the match
suggests.""","""ages 5.55, 22.49 and 38.33 months, ABR thresholds 18.10, 34.17 and 49.03 dB SPL, weights 74.61,
83.35 and 86.41 g. The SDs and ranges printed also match Table 1 (for example ABR SD 5.33, 10.19
and 18.00, range 20 to 85 in old animals). The ABR values rest on reading the notes' character as
its code point; 10 young adults and 1 middle-aged animal have "NaN" and are left out, as the
code's `mean(..., 'omitnan')` does."""),
("""old thresholds from 20 to 85 dB SPL. Over animals, age and threshold correlate (Spearman rho printed
above). It rests on reading the ABR character as its code point.""","""old thresholds from 20 to 85 dB SPL. Over 93 animals, age and threshold correlate (Spearman
rho = 0.85, p = 5.7e-27). It rests on reading the ABR character as its code point."""),
("""young adults (32 of 60, 0.533). The difference from young adults is not significant by Fisher's
exact test (printed above), which the paper does not claim. The cause is not tested.""","""young adults (32 of 60, 0.533). The difference from young adults is not significant by Fisher's
exact test (p = 0.125), which the paper does not claim. The cause is not tested."""),
("""correlate with r = 0.973 (p = 2.1e-73; Spearman 0.964), and the median CF/BF ratio is 1.003, within
10% of 1, with its bootstrap interval printed above.""","""correlate with r = 0.973 (p = 2.1e-73; Spearman 0.964), and the median CF/BF ratio is 1.003
(log2 0.0041, 95% interval -0.0111 to 0.0398), within 10% of 1; 58 units have CF above BF and 56
below, and 13 differ by more than half an octave."""),
("""r = -0.882 with log BF (p = 5.9e-89), Spearman -0.864. With a 5 ms click delay the correlations
are -0.662 and -0.820, both negative with p < 0.05.""","""r = -0.882 with log BF (p = 5.9e-89), Spearman -0.864, and in each age group (-0.78 to -0.92);
the median latency falls from 2.09 ms below 1 kHz to 0.73 ms above 8 kHz. With a 5 ms click delay
the correlations are -0.662 and -0.820 over 269 units, both negative with p < 0.05."""),
]
for a,b in rep:
    assert a in s, a[:60]
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
cd entries/001262-heeringa-2024; . $TMPDIR/env/bin/activate; python /tmp/claude/build_nb.py reproduce_heeringa_2024.ipynb; date -u
```

```
Traceback (most recent call last):
  File "<stdin>", line 62, in <module>
AssertionError: old thresholds from 20 to 85 dB SPL. Over animals, age and t
Sun Nov  1 13:56:05 UTC 2026
```

**Agent calls Bash**

```bash
grep -n "Over animals, age" -A2 -B2 /tmp/claude/build_nb.py
```

```
425-**Result: reproduced.** Mean ABR thresholds are 18.1, 34.2 and 49.0 dB SPL in young, middle-aged and
426-old animals, and the SD of the old animals is the largest (18.0, against 5.3 and 10.2), with old
427:thresholds from 20 to 85 dB SPL. Over animals, age and threshold correlate (Spearman rho printed
428-above). It rests on reading the ABR character as its code point.
429-""")
```

**Agent calls Bash**

```bash
cd /tmp/claude; python - <<'EOF'
p='build_nb.py'; s=open(p).read()
s=s.replace("""thresholds from 20 to 85 dB SPL. Over animals, age and threshold correlate (Spearman rho printed
above). It rests on reading the ABR character as its code point.""","""thresholds from 20 to 85 dB SPL. Over 93 animals, age and threshold correlate (Spearman
rho = 0.85, p = 5.7e-27). It rests on reading the ABR character as its code point.""")
open(p,'w').write(s)
EOF
grep -c "rho = 0.85" build_nb.py
```

```
1
Shell cwd was reset to
```

**Agent**

Now the other replacements (rerun without the fig3 pair).

**Agent calls Bash**

```bash
cd /tmp/claude; python - <<'EOF'
p='build_nb.py'; s=open(p).read()
rep=[
("""fire far more, in almost every recording, and the difference falls back after the tone ends
(57.75 ms).""","""fire far more (median difference 147 spikes/s at 10 to 15 ms, with tone above silent in 96% of
recordings), and after the tone ends (57.75 ms) the tone trials fall below the silent ones, the
offset suppression expected of auditory nerve fibres."""),
("""print(B6a.round(1).to_string(index=False))""","""print(B6a.round({"mean_threshold": 1}).to_string(index=False))"""),
("""**Result: reproduced.** The unit's stored BF is 7620 Hz and its RLF threshold 19 dB SPL. Its BF
recording has 5 repetitions per frequency at one level, and its RLF recording 10 repetitions per
level, as the legend says; the levels are printed above (the legend's 30 dB SPL for the BF
recording and 40 dB SPL for the RLF recording are the levels of the PSTH, 20 dB above threshold
for makePSTH.m's TestLevel).""","""**Result: reproduced.** The unit's stored BF is 7620 Hz and its RLF threshold 19 dB SPL. As the
legend says, its BF recording is at 30 dB SPL with 5 repetitions per frequency, and its RLF
recording (at 7700 Hz) has 10 repetitions per level and includes 40 dB SPL."""),
("""**Result: not reproduced.** Units with two or more within-trial ISIs below 0.6 ms are in the
dataset under every reading: 370 of 1160 under (a), 391 under (b) and 148 under (c); 538 units
have at least one. Most such units have a few short ISIs among thousands (the median fraction is
printed above), and many short ISIs are below 0.1 ms, two or three samples apart, which looks like
one spike detected twice. The paper's check was visual and its rule ("multiple") may have meant
more than two; the outputs show that with any of the three readings the dataset holds units the
stated rule would exclude.""","""**Result: not reproduced.** Units with two or more within-trial ISIs below 0.6 ms are in the
dataset under every reading: 370 of 1160 under (a), 391 under (b) and 148 under (c), from 79 of
the 104 animals; 538 units have at least one. In the failing units the short ISIs are a small
fraction of all ISIs (median 0.0013, largest 0.223), and 162 units have more than 10. Of the
13,904 short ISIs, 10,192 are between 0.3 and 0.6 ms and 1171 below 0.1 ms. With a limit of
0.3 ms, 140 units still fail under (a); with 0.1 ms, 5 do. The paper's check was visual and does
not say what "multiple" means; under the three readings the claims file names, the dataset holds
units the stated rule would exclude."""),
("""**Result: reproduced.** With vector strength recomputed by the paper's function, the highest BF of a
young-adult unit with significant phase locking (p < 0.001) is 4598 Hz, 4.6 kHz. The value is the
same with p < 0.01 or p < 0.0001.""","""**Result: reproduced.** With vector strength recomputed by the paper's function, the highest BF of a
young-adult unit with significant phase locking (p < 0.001, the Methods' threshold) is 4598 Hz,
4.6 kHz; the next highest are 4121 to 4377 Hz. The value depends on the threshold: with p < 0.01
it is 6539 Hz, with p < 0.0001 it is 4377 Hz. No young unit with a higher BF (27 PH units from
4718 to 12,359 Hz) reaches p < 0.001."""),
("""ages 5.55, 22.49 and 38.33 months, ABR thresholds 18.10, 34.17 and 49.03 dB SPL, weights 74.61,
83.35 and 86.41 g. The SDs and ranges printed also match Table 1 (for example ABR SD 5.33, 10.19
and 18.00, range 20 to 85 in old animals). The ABR values rest on reading the notes' character as
its code point; 10 young adults and 1 middle-aged animal have no ABR threshold, and the paper's
means are also over fewer animals than the group sizes if they omit the same ones, which the match
suggests.""","""ages 5.55, 22.49 and 38.33 months, ABR thresholds 18.10, 34.17 and 49.03 dB SPL, weights 74.61,
83.35 and 86.41 g. The SDs and ranges printed also match Table 1 (for example ABR SD 5.33, 10.19
and 18.00, range 20 to 85 in old animals). The ABR values rest on reading the notes' character as
its code point; 10 young adults and 1 middle-aged animal have "NaN" and are left out, as the
code's `mean(..., 'omitnan')` does."""),
("""young adults (32 of 60, 0.533). The difference from young adults is not significant by Fisher's
exact test (printed above), which the paper does not claim. The cause is not tested.""","""young adults (32 of 60, 0.533). The difference from young adults is not significant by Fisher's
exact test (p = 0.125), which the paper does not claim. The cause is not tested."""),
("""correlate with r = 0.973 (p = 2.1e-73; Spearman 0.964), and the median CF/BF ratio is 1.003, within
10% of 1, with its bootstrap interval printed above.""","""correlate with r = 0.973 (p = 2.1e-73; Spearman 0.964), and the median CF/BF ratio is 1.003
(log2 0.0041, 95% interval -0.0111 to 0.0398), within 10% of 1; 58 units have CF above BF and 56
below, and 13 differ by more than half an octave."""),
("""r = -0.882 with log BF (p = 5.9e-89), Spearman -0.864. With a 5 ms click delay the correlations
are -0.662 and -0.820, both negative with p < 0.05.""","""r = -0.882 with log BF (p = 5.9e-89), Spearman -0.864, and in each age group (-0.78 to -0.92);
the median latency falls from 2.09 ms below 1 kHz to 0.73 ms above 8 kHz. With a 5 ms click delay
the correlations are -0.662 and -0.820 over 269 units, both negative with p < 0.05."""),
]
for a,b in rep:
    assert a in s, a[:60]
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
cd entries/001262-heeringa-2024 && . $TMPDIR/env/bin/activate && python /tmp/claude/build_nb.py reproduce_heeringa_2024.ipynb && echo ok
```

```
ok
```

**Agent**

Fixing one more Fig. 6a sentence against the printed bin counts, then writing entry.yaml, requirements.in and README.

**Agent calls Bash**

```bash
cd /tmp/claude; python - <<'EOF'
p='build_nb.py'; s=open(p).read()
a="""0.72 kHz, from 3 units. The bins from 2.06 to 4.14 kHz hold 30 to 34 units, fewer than the bins
above 4.14 kHz (43 to 83) but not fewer than those from 0.86 to 2.06 kHz (31 to 36)."""
b="""0.72 kHz, from 3 units. The bins plotted at 2.06 to 4.14 kHz hold 30 to 34 units, fewer than those
plotted at 4.93 to 11.83 kHz (43 to 83) but about as many as those plotted at 1.02 to 1.73 kHz
(33 to 36)."""
assert a in s; s=s.replace(a,b); open(p,'w').write(s)
EOF
cd entries/001262-heeringa-2024 && . $TMPDIR/env/bin/activate && python /tmp/claude/build_nb.py reproduce_heeringa_2024.ipynb
cat > requirements.in <<'EOF'
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
name: 001262-heeringa-2024
type: reproduction
title: Auditory nerve fibres of young-adult and aging gerbils (Heeringa 2024)
description: Tests the findings of the data descriptor by Heeringa (2024) on dandiset 001262, which
  holds 1160 single auditory nerve fibres from 104 gerbils, one NWB file per fibre. It checks the
  counts and animal characteristics of Table 1, the recording types per age group, the exclusion of
  units with short inter-spike intervals, and the physiological properties of Figures 6 and 7
  (thresholds and spontaneous rates across best frequency, phase locking, characteristic frequency
  and click latency, the last three recomputed from the spike times with the paper's functions).
license: Apache-2.0
notebooks:
- path: reproduce_heeringa_2024.ipynb
  title: Reproducing Heeringa (2024) from dandiset 001262
  runtime_minutes: 4
helpers:
- gerbil_an.py
related:
- id: dandi:001262/0.241205.0959
  relation: uses_data
- id: doi:10.1038/s41597-024-03259-3
  relation: reproduces
EOF
cd  && python tools/entry.py lock entries/001262-heeringa-2024 && python tools/entry.py check entries/001262-heeringa-2024; date -u
```

```
wrote entries/001262-heeringa-2024/requirements.lock.txt
0 error(s)
Sun Nov  1 13:56:45 UTC 2026
```

**Agent calls Bash**

```bash
cd /tmp/claude; python - <<'EOF'
p='build_nb.py'; s=open(p).read()
s=s.replace('meta = requests_meta = __import__("requests").get(','meta = requests.get(')
s=s.replace("import pandas as pd\nfrom scipy import stats\n\nimport gerbil_an as g","import pandas as pd\nimport requests\nfrom scipy import stats\n\nimport gerbil_an as g")
open(p,'w').write(s)
EOF
grep -n "import requests\|meta = requests" build_nb.py; cd entries/001262-heeringa-2024 && . $TMPDIR/env/bin/activate && python /tmp/claude/build_nb.py reproduce_heeringa_2024.ipynb && deactivate && cd  && time python tools/entry.py all entries/001262-heeringa-2024 2>&1 | tail -15
```

```
82:import requests
111:meta = requests.get(
Installed kernelspec registry-001262-heeringa-2024 in executed/001262-heeringa-2024/.venv/share/jupyter/kernels/registry-001262-heeringa-2024
0 error(s)
pass  reproduce_heeringa_2024.ipynb  (201 s)

real	3m27.196s
user	3m4.841s
sys	0m14.688s
```

**Agent**

Entry passes check and runs in 201 s from a clean environment. Confirming the executed copy's numbers match the conclusions.

**Agent calls Bash**

```bash
cd  ls executed/001262-heeringa-2024/; python - <<'EOF'
import json
nb=json.load(open('executed/001262-heeringa-2024/reproduce_heeringa_2024.ipynb'))
txt=''
for c in nb['cells']:
    for o in c.get('outputs',[]):
        if o['output_type']=='stream': txt+=''.join(o['text'])
        if o['output_type']=='error': print('ERROR',o['evalue'])
for key in ['95% CI','Pearson r(log','delay 7.75','delay 5 ms','Variant p <','Units failing','Fisher','Spearman correlation of age','with a drop','reading_1:','reading_2:','10-15','Notebook run time','Of them below','fraction of all ISIs']:
    for line in txt.splitlines():
        if key in line: print(line)
EOF
```

```
reproduce_heeringa_2024.ipynb
result.json
Median log2(CF/BF) = 0.0041 (95% CI -0.0111 to 0.0398); median ratio 1.0028
Pearson r(log CF, log BF) = 0.973, p = 2.1e-73; Spearman rho = 0.964, p = 1.8e-66
delay 7.75 ms: 268 units; latency 0.42 to 2.78 ms (median 1.05); Pearson r = -0.882, p = 5.9e-89; Spearman rho = -0.864, p = 2.8e-81
delay 5 ms: 269 units; latency 0.34 to 5.53 ms (median 3.78); Pearson r = -0.662, p = 3.1e-35; Spearman rho = -0.820, p = 8.9e-67
Variant p < 0.01: highest young BF 6539 Hz
Variant p < 0.0001: highest young BF 4377 Hz
Units failing (two or more ISIs < 0.6 ms): {'a': 370, 'b': 391, 'c': 148} of 1160
Fisher's exact test, old against young (not part of the criterion): odds ratio 0.48, p = 0.125
Spearman correlation of age with ABR threshold over 93 animals: rho = 0.85, p = 5.7e-27
RLF recordings: 952; with a drop larger than the SD below 80 dB SPL: 249 (0.26); with two or more such drops: 104
reading_1: 5 of 6 match
reading_2: 5 of 6 match
   10-15          147.3        0.96
Notebook run time: 3.2 min
Of them below 0.1 ms: 1171 ; 0.1 to 0.3 ms: 2541 ; 0.3 to 0.6 ms: 10192
Short ISIs as a fraction of all ISIs, among failing units (b): median 0.0013, max 0.223
```

**Agent**

All numbers match the text. Checking the attempt schema before writing the record.

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
print(json.dumps(s['properties'],indent=0)[:2500]); print(s.get('required'))
d=s.get('\$defs',s.get('definitions',{}))
for k,v in d.items(): print('##',k, json.dumps(v)[:1500])
"; ls questions | grep 001262
```

```
{
"schema_version": {
"const": 2
},
"id": {
"type": "string",
"pattern": "^[a-z0-9]+(-[a-z0-9]+)*$"
},
"dataset": {
"description": "The dataset the attempt tested: the archive and the dataset's identifier there.",
"type": "object",
"additionalProperties": false,
"required": [
"archive",
"id",
"version"
],
"properties": {
"archive": {
"description": "The archive that holds the dataset, in lower case: dandi, ebrains, openneuro, dryad, zenodo, figshare and so on.",
[... 103 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
p=s['properties']
print(json.dumps(p['provenance']['properties']['agent'])[:800]); print(json.dumps(p['provenance']['properties'].get('runner'))[:500])
print(json.dumps(p['outcomes'])[:3000]); print(json.dumps(p['findings'])[:1500])
"
```

```
{"description": "Required when kind is agent.", "type": "object", "additionalProperties": false, "required": ["harness", "model", "protocol"], "properties": {"harness": {"type": "string"}, "model": {"type": "string"}, "protocol": {"description": "Version of the reproduction protocol the agent followed.", "type": "string"}}}
{"description": "Where the attempt was run: the platform, and the run that wrote this record. Its other runs (verification rounds, revisions) are linked from their transcripts.", "type": "object", "additionalProperties": false, "required": ["platform"], "properties": {"platform": {"description": "The platform that ran it, e.g. GitHub Actions, or local for a person's machine.", "type": "string", "minLength": 1}, "url": {"description": "The run that wrote the record, e.g. https://github.com/<owner
{"description": "One per claim attempted.", "type": "array", "minItems": 1, "items": {"type": "object", "additionalProperties": false, "required": ["claim", "outcome"], "properties": {"claim": {"description": "Claim id from the target's claims file.", "type": "string"}, "outcome": {"enum": ["reproduced", "partially_reproduced", "not_reproduced", "blocked"], "description": "Describes the result, not the method: whether the effect the claim states was found. Differences in method from the paper go in `deviations`."}, "blocked_by": {"description": "Required when outcome is blocked.", "enum": ["data_missing", "metadata_insufficient", "methods_underspecified", "data_unreadable", "too_large", "not_runnable", "other"]}, "notes": {"description": "What differs, or what was missing, stated factually.", "type": "string"}, "notebook": {"description": "Path of the notebook within the entry.", "type": "string"}, "output": {"description": "Which output shows the result, e.g. a cell tag.", "type": "string"}, "measured": {"description": "The values obtained, for claims with expected values: one number, or one per expected value, in the same order.", "oneOf": [{"type": "nu
[... 1 more lines not kept]
```

**Agent**

Writing the attempt record (generated with PyYAML so the scalars are valid) and the entry README.

**Agent calls Bash**

```bash
mkdir -p /tmp/claude && cat > /tmp/claude/attempt.py <<'PYEOF'
import yaml

NB = "reproduce_heeringa_2024.ipynb"
ABR_DEV = ("The ABR threshold is not readable as written; general/notes ends with one character, or NaN. "
           "It is read as the character's code point (for example '#' is 35), an interpretation the data "
           "support (all values are multiples of 5 from 10 to 85 dB SPL, the range of Table 1, and the "
           "group means and SDs then equal Table 1's) but do not prove.")
CLICK_DEV = ("The click delay is not in the files (the trial table gives NaN for CLICK trials). The 2-bin "
             "latency of Clickextract_func.m and getFSL2bins.m needs it; 7.75 ms, the delay of every tone "
             "recording in the dataset, is assumed, and 5 ms is shown as a variant.")
CF_DEV = ("The stored CF is not in the NWB files. CF is recomputed from the CF recording's spike times "
          "with CFextract_func.m, getSpikeCounts.m and getQ10dB.m (named in the Methods, 'The analysis "
          "procedures were carried out by the function CFextract_func.m'), automatic first pass only. "
          "The code asks the experimenter to accept or change the response criterion and the CF ('T could "
          "be manually adjusted when needed', Methods); those manual choices are not in the files.")
VS_DEV = ("Vector strength and its p-value are not in the NWB files. They are recomputed per level of "
          "the PH recording with PHextract_func.m and TytoView_calcVS.m (Methods, 'The analysis "
          "procedures were carried out by the function PHextract_func.m'), spikes between tone onset and "
          "offset, p = exp(-N vs^2), NaN when N is 50 or fewer (the code's ntot > 50; the Methods say "
          "N < 50). The silent trials' value, which the code also stores, is left out.")

outcomes = [
 dict(claim="table1-animals-units", outcome="reproduced", notebook=NB, output="claim:table1-animals-units",
      measured=[104, 1160, 60, 32, 13, 7, 31, 11, 759, 87, 314],
      notes="All eleven counts match. Animals are counted by subject_id (each subject's metadata is the "
            "same in all its files), age groups by age in days as the paper's code defines them."),
 dict(claim="table1-age-abr-weight", outcome="reproduced", notebook=NB, output="claim:table1-age-abr-weight",
      measured=[5.55, 22.49, 38.33, 18.10, 34.17, 49.03, 74.61, 83.35, 86.41], assumed=True,
      notes="All nine means are within tolerance and equal Table 1 after rounding; the SDs and ranges also "
            "match (ABR SD 5.33, 10.19 and 18.00). 10 young adults and 1 middle-aged animal have NaN for "
            "the ABR threshold and are left out, as the code's omitnan does. The ABR means rest on reading "
            "the stored character as its code point.",
      deviations=[ABR_DEV]),
 dict(claim="table1-bf-range", outcome="reproduced", notebook=NB, output="claim:table1-bf-range",
      notes="428 to 15,825 Hz, 350 to 15,091 Hz and 620 to 15,762 Hz, the paper's values exactly. 8 units "
            "have no BF recording; 5 of them have a CF recording, and their recomputed CFs (700 to 4000 Hz) "
            "lie inside the young-adult range, so the ranges are the same with or without them.",
      deviations=["The CF of units without a BF recording is recomputed (see fig7a-cf-matches-bf); it does "
                  "not change any bound."]),
 dict(claim="fig3-abr-age", outcome="reproduced", notebook=NB, output="claim:fig3-abr-age", assumed=True,
      notes="Mean ABR threshold 18.1, 34.2 and 49.0 dB SPL from young to old; the old animals' SD (18.0) "
            "is the largest (5.3 and 10.2 in the others), with old thresholds from 20 to 85 dB SPL. Over 93 "
            "animals age and threshold correlate (Spearman rho 0.85, p = 5.7e-27).",
      deviations=[ABR_DEV]),
 dict(claim="females-fewer-in-old", outcome="reproduced", notebook=NB, output="claim:females-fewer-in-old",
      notes="11 of 31 old animals are female (0.355), against 32 of 60 young adults (0.533). Fisher's exact "
            "test, which the paper does not report, gives p = 0.125. The cause is not tested."),
 dict(claim="oxygen-78", outcome="reproduced", notebook=NB, output="claim:oxygen-78", measured=78,
      notes="78 of 104 animals have 'oxygen yes' in general/surgery (41 young, 6 middle aged, 31 old)."),
 dict(claim="complex-stimuli-experiments", outcome="reproduced", notebook=NB,
      output="claim:complex-stimuli-experiments", measured=[21, 5, 17],
      notes="NOISE in 21, SPS in 5 and CVC in 17 of 104 experiments (143, 22 and 135 units)."),
 dict(claim="recording-type-counts", outcome="partially_reproduced", notebook=NB,
      output="claim:recording-type-counts", measured=[119, 271, 203, 143, 22, 135],
      notes="Five of six counts match under both readings (CF 119, SR 203, NOISE 143, SPS 22, CVC 135). "
            "CLICK does not; 275 units have one CLICK recording each, and 271 give a recomputed 2-bin "
            "latency (272 with a 5 ms click delay), against 261. The files hold no stored latency, so it "
            "cannot be told which 10 units had none in the paper, or whether some had a second CLICK "
            "recording in the MATLAB files that the code would leave out. 1 CLICK unit has 75 spikes or "
            "fewer.",
      deviations=["The stored CF and click latency are not in the files; reading 1 uses the values "
                  "recomputed with the paper's functions.", CLICK_DEV]),
 dict(claim="fig7-sampling-by-age", outcome="reproduced", notebook=NB, output="claim:fig7-sampling-by-age",
      notes="No middle-aged unit has an SR, SPS or CVC recording; all 22 SPS units are from young adults."),
 dict(claim="isi-exclusion", outcome="not_reproduced", notebook=NB, output="claim:isi-exclusion",
      notes="Units with two or more within-trial ISIs below 0.6 ms are in the dataset under every reading, "
            "370 of 1160 under (a), 391 under (b), 148 under (c), from 79 of 104 animals; 538 units have at "
            "least one. In failing units short ISIs are a median 0.13% of all ISIs (largest 22.3%), and 162 "
            "units have more than 10. Of 13,904 short ISIs, 10,192 are 0.3 to 0.6 ms and 1171 below 0.1 ms. "
            "With a 0.3 ms limit 140 units fail under (a), with 0.1 ms 5 do. Spike times are sorted within "
            "trials and no spike train is duplicated. The paper's check was visual (checkAN.m plots the "
            "count); it does not say how many short ISIs 'multiple' allows.",
      deviations=["A recording is taken as a recording type of the unit; each type occurs once per unit in "
                  "the files."]),
 dict(claim="no-prepotentials", outcome="blocked", blocked_by="methods_underspecified",
      notes="The check was a visual inspection of the median spike waveform (checkAN.m); neither the paper "
            "nor its code gives a rule for a prepotential, so no criterion fixed from the paper can judge "
            "it, as the claims file says. The raw voltage traces are in the files (acquisition), so the "
            "waveforms are available; they were not read."),
 dict(claim="rlf-monotonic", outcome="blocked", blocked_by="methods_underspecified", notebook=NB,
      output="claim:rlf-monotonic",
      notes="The check was visual and the paper gives no rule for nonmonotonicity. As a description only, "
            "with rates per level computed from the spike times in the stimulus window (the stored rates "
            "are not in the files), 249 of 952 RLF recordings have a fall in mean rate between successive "
            "levels below 80 dB SPL larger than the SD at the lower level, and 104 have two or more."),
 dict(claim="fig5b-example", outcome="reproduced", notebook=NB, output="claim:fig5b-example",
      measured=[7.62, 19.0],
      notes="Stored BF 7620 Hz and RLF threshold 19 dB SPL. The BF recording is at 30 dB SPL with 5 "
            "repetitions per frequency, and the RLF recording (7700 Hz) has 10 repetitions per level and "
            "includes 40 dB SPL, as the legend says."),
 dict(claim="fig6a-young-two-sensitive-regions", outcome="reproduced", notebook=NB,
      output="claim:fig6a-young-two-sensitive-regions",
      notes="Under reading (b) the highest young-adult mean threshold between the two sensitive regions is "
            "27.6 dB SPL in the bin plotted at 3.48 kHz, with 25.4 and 24.4 dB in the neighbouring bins; "
            "the sensitive regions have their lowest means at 1.73 kHz (20.9 dB) and 8.34 kHz (21.2 dB). "
            "Under reading (a) the highest mean of all bins is 36.7 dB at 0.72 kHz, from 3 units. The "
            "criterion is met under one reading, as it requires. The bins plotted at 2.06 to 4.14 kHz hold "
            "30 to 34 units, fewer than at 4.93 to 11.83 kHz (43 to 83) and about as many as at 1.02 to "
            "1.73 kHz (33 to 36).",
      deviations=["The two readings of 'highest' differ; the claims file's criterion takes the claim as "
                  "reproduced under either, and only (b) holds."]),
 dict(claim="fig6b-young-bf-gap", outcome="not_reproduced", notebook=NB, output="claim:fig6b-young-bf-gap",
      notes="The bin from 2423 to 2936 Hz holds 34 young-adult units. It is not the fewest of the non-empty "
            "span (the 356 Hz bin holds 1, and the bins below 766 Hz hold 1 to 11), nor fewer than both "
            "neighbours (34 and 35). Among the bins from 1363 to 4309 Hz it ties for the fewest (34) with "
            "the 1363 and 2000 Hz bins."),
 dict(claim="fig6c-sr-distributions", outcome="reproduced", notebook=NB, output="claim:fig6c-sr-distributions",
      measured=[2.5, 57.5],
      notes="Measured values are bin centres. Low-BF young-adult units (314) have their two largest modes "
            "of spontaneous rate in the bins 0 to 5 (27 units) and 55 to 60 spikes/s (21), separated by a "
            "bin of 5. High-BF units (437) have their largest local maximum at 0 to 5 spikes/s (66), "
            "below 18. 26.1% of high-BF and 18.5% of low-BF units are below 18 spikes/s."),
 dict(claim="fig6d-max-phase-locking-bf", outcome="reproduced", notebook=NB,
      output="claim:fig6d-max-phase-locking-bf", measured=4.598,
      notes="The highest BF of a young-adult unit with significant phase locking (p < 0.001) is 4598 Hz; "
            "the next are 4121 to 4377 Hz. No young PH unit with a higher BF (27 units, 4718 to 12,359 Hz) "
            "reaches p < 0.001. The value depends on the threshold, 6539 Hz with p < 0.01 and 4377 Hz with "
            "p < 0.0001; the Methods fix 0.001.",
      deviations=[VS_DEV]),
 dict(claim="fig6d-highest-vs-low-bf-low-sr", outcome="reproduced", notebook=NB,
      output="claim:fig6d-highest-vs-low-bf-low-sr",
      notes="All four readings hold. The largest maximum vector strength (0.882) is from a unit with BF "
            "428 Hz and SR 1.25 spikes/s, and the median is highest in the low-BF low-SR group (0.821 over "
            "6 young adults, 0.804 over 19 units of all ages; low-BF high-SR 0.695 and 0.702). Young adults "
            "with BF below 1.5 kHz, low-SR against high-SR, Mann-Whitney p = 0.0039 (6 and 51 units).",
      deviations=[VS_DEV]),
 dict(claim="fig7a-cf-matches-bf", outcome="reproduced", notebook=NB, output="claim:fig7a-cf-matches-bf",
      notes="Over 114 units with a recomputed CF and a stored BF, Pearson r(log CF, log BF) = 0.973 "
            "(p = 2.1e-73), Spearman 0.964; median CF/BF 1.003 (log2 0.0041, 95% bootstrap interval "
            "-0.0111 to 0.0398); 58 units above and 56 below; 13 differ by more than half an octave.",
      deviations=[CF_DEV]),
 dict(claim="fig7b-click-latency-bf", outcome="reproduced", notebook=NB, output="claim:fig7b-click-latency-bf",
      assumed=True,
      notes="Over 268 units, Pearson r(latency, log BF) = -0.882 (p = 5.9e-89), Spearman -0.864; negative "
            "in each age group (-0.78 to -0.92). Latencies span 0.42 to 2.78 ms, inside Fig. 7b's 0 to "
            "3.5 ms axis. With a 5 ms click delay, r = -0.662 and Spearman -0.820 over 269 units, so the "
            "outcome is the same under both delays.",
      deviations=["The stored 2-bin latency is not in the files; it is recomputed with Clickextract_func.m "
                  "and getFSL2bins.m (named in the Methods).", CLICK_DEV]),
 dict(claim="fig7ab-representative-sampling", outcome="not_reproduced", notebook=NB,
      output="claim:fig7ab-representative-sampling",
      notes="No reading holds for both subsets. The CF units' BFs differ from both references (KS p = 0.018 "
            "against young adults, 0.003 against all units; median 3454 Hz, 0.75 times the references' 4589 "
            "and 4592 Hz). The CLICK units' BFs do not differ by KS (p = 0.20 and 0.45) but their median "
            "(5180 Hz) is 1.13 times the references'. The criterion says not reproduced 'when none does'; "
            "this record reads 'a reading holds' as holding for both CF and CLICK, as the criterion's "
            "reproduced case does. Under the other reading of 'none' (no reading holds for either subset) "
            "the claim would be blocked as methods_underspecified, since the CLICK KS reading holds.",
      deviations=["The claims file's criterion can be read two ways when the CF and CLICK subsets give "
                  "different results; the reading taken is stated in the notes."]),
 dict(claim="old-success-rate", outcome="blocked", blocked_by="data_missing", notebook=NB,
      output="claim:old-success-rate",
      notes="The denominators are the animals operated on, including those that gave no single units. "
            "Every one of the 104 subjects has at least one unit file, and neither the files, the dandiset "
            "metadata nor its description list animals that gave none. The paper names no other deposit "
            "of them."),
 dict(claim="psth-primary-like", outcome="blocked", blocked_by="methods_underspecified",
      notes="The check was visual; the paper and its code (makePSTH.m) give no rule for a "
            "non-primary-like shape, as the claims file says."),
]

findings = [
 dict(kind="format_error", statement=(
  "The ABR threshold in general/notes ('threshold (db SPL) ...') is written as a single character whose "
  "code point is the threshold, for example '#' for 35 and 'K' for 75, and control characters such as a "
  "line feed for 10; 11 animals have 'NaN'. Read as code points, the values give Table 1's means and SDs "
  "exactly, so the number appears to have been converted to a character in the conversion to NWB.")),
 dict(kind="data_missing", statement=(
  "The analysed outcomes the paper describes as stored with each recording (exp.data.[type].analysis) are "
  "in the NWB files only as best frequency, spontaneous rate and threshold per recording type. The "
  "characteristic frequency, Q10, vector strength with its p-value and levels, the click latencies and "
  "first-spike statistics, and the rate-level and frequency-response rates are not there. Most can be "
  "recomputed from the spike times with the paper's code, but the manual corrections the code allows "
  "(CF and response criterion, RLF threshold) cannot.")),
 dict(kind="metadata_insufficient", statement=(
  "The CLICK trials carry no delay (NaN in the trial table), so the click's onset within the trial, "
  "needed for click latencies, is not in the files. The SR, NOISE, SPS and CVC trials also have no delay.")),
 dict(kind="methods_unavailable", statement=(
  "Question for the paper's author. What was the click delay (curvesettings.delay) of the CLICK "
  "recordings, and was it the same in all of them? This attempt assumed 7.75 ms, the delay of every tone "
  "recording, which gives latencies of 0.42 to 2.78 ms; the correlation with best frequency is negative "
  "under 7.75 or 5 ms.")),
 dict(kind="other", statement=(
  "370 of 1160 units have two or more within-trial inter-spike intervals below 0.6 ms in one recording "
  "(391 pooled over recordings, 148 in the BF recording alone), although the paper says units with "
  "multiple such intervals were excluded. Most short intervals are 0.3 to 0.6 ms; 1171 of 13,904 are "
  "below 0.1 ms, which suggests double detection of one spike.")),
 dict(kind="other", statement=(
  "275 units have a CLICK recording, one each, and 271 give a 2-bin latency with the paper's function, "
  "where the Fig. 7 legend counts 261 units with a CLICK recording. Without the stored latencies the "
  "difference cannot be traced.")),
 dict(kind="metadata_error", statement=(
  "The recordings are extracellular single-unit recordings with a glass electrode (as the file's own "
  "device description says), but they are stored as intracellular (icephys) VoltageClampStimulusSeries, "
  "and the archive's summary lists the measurement technique as 'voltage clamp technique'.")),
 dict(kind="data_missing", statement=(
  "The dataset holds only the 104 animals with recorded units. The animals operated on without a "
  "successful recording, which the paper's success rates (43% of old and 88% of young-adult gerbils) "
  "count, are not listed in the files or the metadata.")),
]

rec = dict(
 schema_version=2, id="001262-heeringa-2024-01",
 dataset=dict(archive="dandi", id="001262", version="0.241205.0959", doi="10.48324/dandi.001262/0.241205.0959"),
 paper="doi:10.1038/s41597-024-03259-3", date="2026-11-01", entry="001262-heeringa-2024",
 provenance=dict(kind="agent", accountable=dict(name="CatalystNeuro"),
                 agent=dict(harness="Claude Code", model="claude-opus-5-5", protocol="pilot-13"),
                 runner=dict(platform="GitHub Actions",
                             url="https://github.com/catalystneuro/encore/actions/runs/41311677966")),
 outcomes=outcomes, findings=findings)

class D(yaml.SafeDumper):
    pass
D.add_representer(str, lambda d, s: d.represent_scalar("tag:yaml.org,2002:str", s))
out = yaml.dump(rec, Dumper=D, sort_keys=False, width=100, allow_unicode=True)
open("attempts/001262-heeringa-2024-01.yaml", "w").write(out)
PYEOF
cd  && python /tmp/claude/attempt.py && grep -n '^  *[a-z_]*: ".*\|: [^"]*: ' attempts/001262-heeringa-2024-01.yaml | head; head -30 attempts/001262-heeringa-2024-01.yaml
```

```
schema_version: 2
id: 001262-heeringa-2024-01
dataset:
  archive: dandi
  id: '001262'
  version: 0.241205.0959
  doi: 10.48324/dandi.001262/0.241205.0959
paper: doi:10.1038/s41597-024-03259-3
date: '2026-11-01'
entry: 001262-heeringa-2024
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
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > entries/001262-heeringa-2024/README.md <<'EOF'
# Heeringa (2024) from dandiset 001262

Tests the findings of [Heeringa (2024)](https://doi.org/10.1038/s41597-024-03259-3), a data
descriptor, on [DANDI:001262](https://dandiarchive.org/dandiset/001262/0.241205.0959), which holds
1160 single auditory nerve fibres from 104 gerbils, one NWB file per fibre.

| Claim | Outcome |
|---|---|
| Table 1 counts of animals, females and units | Reproduced |
| Table 1 mean age, ABR threshold and weight | Reproduced (ABR read from a character code) |
| Table 1 best-frequency ranges | Reproduced |
| ABR thresholds rise with age, widest spread in old animals | Reproduced |
| Fewer females among old animals | Reproduced |
| 78 of 104 animals received oxygen | Reproduced |
| Experiments with NOISE, SPS and CVC (21, 5, 17) | Reproduced |
| Units per recording type (Fig. 7) | Partially reproduced (CLICK 271, not 261) |
| No SR, SPS or CVC in middle-aged animals | Reproduced |
| Units with short inter-spike intervals were excluded | Not reproduced |
| Example fibre of Fig. 5b | Reproduced |
| Fig. 6a highest young-adult thresholds at 3.5 kHz | Reproduced |
| Fig. 6b fewest young-adult BFs at 2.5 to 3.0 kHz | Not reproduced |
| Fig. 6c spontaneous rate distributions | Reproduced |
| Fig. 6d phase locking up to 4.6 kHz; highest in low-BF low-SR fibres | Reproduced (two claims) |
| Fig. 7a CF matches BF | Reproduced |
| Fig. 7b click latency falls with BF | Reproduced (click delay assumed) |
| Fig. 7a,b CF and CLICK units represent the full BF distribution | Not reproduced |
| Prepotentials, rate-level shapes, PSTH shapes (visual checks) | Blocked: methods underspecified |
| Success rate of recordings in old and young animals | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The NWB files keep only best frequency, spontaneous rate and threshold of the paper's analysed
outcomes, so characteristic frequency, vector strength and click latency are recomputed from the
spike times with the paper's own MATLAB functions (Zenodo 10.5281/zenodo.10370064). The ABR
threshold is stored as a character whose code point is the threshold. The attempt record, with
the reasons and the differences from the paper's method, is
[`attempts/001262-heeringa-2024-01.yaml`](../../attempts/001262-heeringa-2024-01.yaml).

- `reproduce_heeringa_2024.ipynb`: the analysis. It takes about four minutes, most of it reading
  the 1160 files' metadata and spike times (the voltage traces are not read).
- `gerbil_an.py`: loading the files in parallel, parsing the animal metadata, and the measures of
  the paper's code (vector strength, CF, 2-bin click latency, inter-spike intervals). Other
  notebooks on this dandiset can import it.
EOF
grep -n "—\|rather" entries/001262-heeringa-2024/* attempts/001262-heeringa-2024-01.yaml /tmp/claude/build_nb.py | head; python tools/entry.py check entries/001262-heeringa-2024
```

```
grep: entries/001262-heeringa-2024/__pycache__: Is a directory
0 error(s)
```

**Agent**

Removing bold outside the Result openers (header labels, blocked notes, summary) and the stray `__pycache__`, then re-running.

**Agent calls Bash**

```bash
cd /tmp/claude; python - <<'EOF'
import re
p='build_nb.py'; s=open(p).read()
for lab in ["Paper.","Dandiset.","What the dandiset holds.","Outside inputs.","How the analysis differs from the paper's.","What was found about the dataset.","Blocked: methods underspecified.","Blocked: data missing."]:
    s=s.replace("**"+lab+"**", lab)
open(p,'w').write(s)
print(re.findall(r"\*\*[^*]{0,40}", s)[:40])
EOF
rm -rf entries/001262-heeringa-2024/__pycache__; cd entries/001262-heeringa-2024 && . $TMPDIR/env/bin/activate && python /tmp/claude/build_nb.py reproduce_heeringa_2024.ipynb && deactivate && cd  && python tools/entry.py all entries/001262-heeringa-2024 2>&1 | tail -3; rm -rf entries/001262-heeringa-2024/__pycache__; git status --short; date -u
```

```
['**Result: reproduced.', '** 104 animals and 1160 units; 60 young ad', '**Result: reproduced.', '** All nine means are within tolerance and', '**Result: reproduced.', '** The ranges are 428 to 15,825 Hz (young)', '**Result: reproduced.', '** Mean ABR thresholds are 18.1, 34.2 and ', '**Result: reproduced.', '** 11 of 31 old animals are female (0.355)', '**Result: reproduced.', '** 78 of 104 animals have "oxygen: yes".\n"', '**Result: reproduced.', '** NOISE in 21, SPS in 5 and CVC in 17 of ', '**Result: partially reproduced.', '** Five of six counts match under both rea', '**Result: reproduced.', '** No middle-aged unit has an SR, SPS or C', '**Result: not reproduced.', '** Units with two or more within-trial ISI', '**Result: reproduced.', "** The unit's stored BF is 7620 Hz and its", '**Result: reproduced.', '** Under reading (b) the young-adult mean ', '**Result: not reproduced.', '** The bin from 2423 to 2936 Hz holds 34 y', '**Result: reproduced.', '** In low-BF young-adult units the two lar', '**Result: reproduced.', '** With vector strength recomputed by the ', '**Result: reproduced.', '** Under all four readings the highest vec', '**np.median(l2):.4f}")\nprint(f"Units with ', '**Result: reproduced.', '** Over 114 units with a recomputed CF and', '**Result: reproduced.', '** Over 268 units the recomputed 2-bin cli', '**Result: not reproduced.', '** No reading holds for both subsets. The ']
Installed kernelspec registry-001262-heeringa-2024 in executed/001262-heeringa-2024/.venv/share/jupyter/kernels/registry-001262-heeringa-2024
0 error(s)
pass  reproduce_heeringa_2024.ipynb  (201 s)
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
?? attempts/001262-heeringa-2024-01.yaml
?? entries/001262-heeringa-2024/
?? scripts
Sun Nov  1 14:05:38 UTC 2026
```

**Agent**

Run passes again (201 s). Some untracked dotfiles appeared at the repository root that I did not write; checking what they are before touching anything.

**Agent calls Bash**

```bash
cd  ls -la .bash_profile .bashrc .gitconfig .mcp.json .profile .ripgreprc .zprofile .zshrc; ls -la .idea .vscode scripts | head
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  1 13:30 .bash_profile
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  1 13:30 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  1 13:30 .gitconfig
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  1 13:30 .mcp.json
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  1 13:30 .profile
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  1 13:30 .ripgreprc
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  1 13:30 .zprofile
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  1 13:30 .zshrc
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  1 13:30 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  1 13:30 .vscode
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  1 13:30 scripts
```

**Agent**

Those are sandbox device mounts (/dev/null), not files; leaving them alone. Building the handover.

**Agent calls Bash**

```bash
cd  python tools/entry.py handover entries/001262-heeringa-2024 && ls executed/001262-heeringa-2024/handover/; git status --short entries attempts questions claims
```

```
wrote executed/001262-heeringa-2024/handover
10.1038-s41597-024-03259-3.yaml
gerbil_an.py
reproduce_heeringa_2024.ipynb
?? attempts/001262-heeringa-2024-01.yaml
?? entries/001262-heeringa-2024/
```

**Agent**

I've finished steps 1 to 5 of the Author section and run the handover (step 6). The entry passes `tools/entry.py all` and runs in 201 s from a clean environment. I did not verify my own work, and nothing is committed.

The files are `entries/001262-heeringa-2024/` (notebook, `gerbil_an.py`, README, lock files) and `attempts/001262-heeringa-2024-01.yaml`. I pinned version 0.241205.0959, the newer of the two published versions. The paper cites only the Dryad deposit, and both versions hold the same 1160 files, so the choice changes no number.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| table1-animals-units | reproduced (all 11 counts) |
| table1-age-abr-weight | reproduced, assumed (ABR decoding) |
| table1-bf-range | reproduced (exact) |
| fig3-abr-age | reproduced, assumed (ABR decoding) |
| females-fewer-in-old | reproduced |
| oxygen-78 | reproduced |
| complex-stimuli-experiments | reproduced (21, 5, 17) |
| recording-type-counts | partially reproduced (5 of 6 match; CLICK is 271 or 275, paper says 261) |
| fig7-sampling-by-age | reproduced |
| isi-exclusion | not reproduced (370, 391 and 148 units fail under readings a, b, c) |
| no-prepotentials | blocked, methods_underspecified |
| rlf-monotonic | blocked, methods_underspecified (description shown) |
| fig5b-example | reproduced (7620 Hz, 19 dB) |
| fig6a-young-two-sensitive-regions | reproduced (holds under reading b only) |
| fig6b-young-bf-gap | not reproduced (the named bin holds 34 units; its neighbours hold 34 and 35) |
| fig6c-sr-distributions | reproduced |
| fig6d-max-phase-locking-bf | reproduced (4598 Hz; recomputed vector strength) |
| fig6d-highest-vs-low-bf-low-sr | reproduced |
| fig7a-cf-matches-bf | reproduced (r = 0.973, median CF/BF 1.003; recomputed CF) |
| fig7b-click-latency-bf | reproduced, assumed (r = -0.88; click delay assumed) |
| fig7ab-representative-sampling | not reproduced (the CF units' BFs differ from the full set under every reading) |
| old-success-rate | blocked, data_missing |
| psth-primary-like | blocked, methods_underspecified |

**2. What was found about the dataset**
- **ABR threshold.** It is stored as a single character in `general/notes`, and the character's code point is the threshold ("#" is 35). Decoded this way, the values reproduce Table 1's means and SDs exactly. I recorded it as a format error.
- **Missing analysed values.** The NWB files keep only the best frequency, spontaneous rate and threshold per recording. The characteristic frequency, vector strength and its p-value, and the click latencies are missing, so I recomputed them from the spike times with the paper's own MATLAB functions (Zenodo 10370064). The CF uses only the code's automatic pass; the manual corrections it allows are not in the data.
- **Click delay.** The CLICK trials have no delay in the files.
- **Short inter-spike intervals.** Many units have intervals below 0.6 ms, though the paper says such units were excluded.
- **Recording technique.** The extracellular recordings are stored as intracellular voltage-clamp series, and the archive summary lists the technique as "voltage clamp".
- **Unsuccessful experiments.** Animals operated on without a successful recording are not listed anywhere, so the success rates can't be checked.
- **Assumptions** (marked `assumed: true` on those three claims):
  - The ABR character is read as its code point.
  - The click delay is 7.75 ms, the delay of every tone recording. The result is the same with 5 ms.
- **Question for the paper's author:** what was the click delay in the CLICK recordings, and was it the same in all of them? It is recorded as a `methods_unavailable` finding.
- **Questions to a reader:** none.

**3. Points where the protocol was unclear or missing something**
1. Neither the protocol nor the claims file says what to do when the criteria name stored values the dataset lacks but which the paper's code can recompute from the raw data. I recomputed them, cited the functions, and recorded deviations.
2. `assumed` is defined for methods the paper leaves open. The ABR decoding is a reading of the data, not a method, but I marked the outcomes `assumed` so it is visible.
3. The fig7ab criterion ("not reproduced when none does") is ambiguous when the CF and CLICK subsets give different results. I took "a reading holds" to mean it holds for both subsets, and the notes give the other reading, under which the claim would be blocked.
4. The protocol does not say whether a blocked claim may have outputs. For rlf-monotonic and old-success-rate I added tagged cells with the description the criterion asks for.
5. The protocol does not say whether code read only for method details goes under `inputs`. I left `inputs` empty and cited the Zenodo code in the helper and the deviations.
6. Step 2's clock check is phrased as decoding a task variable. I used a contrast instead: rate in tone trials minus rate in silent trials, in 5 ms windows from trial start.

**4. Runtime and failures**
The run took from 13:32 to about 14:07 UTC. The notebook takes 3.3 min, mostly reading the 1160 files in parallel with processes; threads were slow because h5py holds a global lock. Nothing failed. The only error on the way was a text substitution in my notebook build script, which I fixed and re-ran.

## End of run

61 turns, 30 minutes, result: success.
