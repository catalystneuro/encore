# 001444 · author · run 41486399888

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls
```

```
<persisted-output>
Output too large (35.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/4c89dc14-2bdb-46fc-a88e-53626ecd4fc1/tool-results/bxsx6t7nu.txt

Preview (first 2KB):
Mon Nov  2 16:59:39 UTC 2026
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

**Agent calls Bash**

```bash
cat README.md docs/design.md docs/archives.md
```

```
<persisted-output>
Output too large (37.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/4c89dc14-2bdb-46fc-a88e-53626ecd4fc1/tool-results/bt26f4m13.txt

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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/4c89dc14-2bdb-46fc-a88e-53626ecd4fc1/tool-results/bxsx6t7nu.txt"
}
```

```
1	Mon Nov  2 16:59:39 UTC 2026
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
[... 619 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/4c89dc14-2bdb-46fc-a88e-53626ecd4fc1/tool-results/bt26f4m13.txt"
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
[... 678 more lines not kept]
```

**Agent calls Bash**

```bash
ls paper claims/001444 entries/001453-fouke-2025 claims/001453 questions | head -50; cat claims/001444/*.yaml
```

```
<persisted-output>
Output too large (51.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/4c89dc14-2bdb-46fc-a88e-53626ecd4fc1/tool-results/bm25qu74i.txt

Preview (first 2KB):
claims/001444:
10.1038-s41531-025-01070-4.yaml

claims/001453:
10.1016-j.cub.2025.04.027.yaml

entries/001453-fouke-2025:
README.md
entry.yaml
omr.py
reproduce_fouke_2025.ipynb
requirements.in
requirements.lock.txt

paper:
10.1038-s41531-025-01070-4.txt
[... 52 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/001444/10.1038-s41531-025-01070-4.yaml"
}
```

```
1	# Claims for Doherty, Chen, Smith, Wichmann, Chu & Lytton (2025), npj Parkinson's Disease 11, 230,
2	# "Enhanced beta power emerges from simulated parkinsonian primary motor cortex", on dandiset 001444.
3	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21, protocol
4	# pilot-10 as stated in docs/protocol.md.
5	#
6	# Text read: the version of record as served by Europe PMC (PMC12325672), main text, figure legends
7	# and Methods. The supplement (Supplementary Tables 1 to 3, Supplementary Figs. 1 to 5) was not in
8	# the text supplied and was not read. The main text reports every result below from one set of
9	# simulations; the supplement holds the analyses of the three other sets (Supplementary Table 2),
10	# the PT5B current-frequency curves (Supplementary Fig. 1) and the conductance changes
11	# (Supplementary Table 3). The bioRxiv preprint (doi:10.1101/2024.05.23.595566) was also supplied;
12	# it is an earlier version with another title and was not used for claims.
13	#
14	# Code read: github.com/suny-downstate-medical-center/pd_m1_6ohda at commit 0a1f0e8 (2025-08-20, the
15	# head of main; the paper cites Zenodo 10.5281/zenodo.12399983). It holds the NetPyNE simulation
16	# (sim/cfg.py, sim/netParams.py, cells, mechanisms) and four notebooks that stream one file each
17	# from dandiset 001444 and plot the LFP, a raster and five PT5B voltage traces. It holds no code for
18	# rates, statistics, CV, duty cycle, spectrograms, coincidences or unitary events. The README gives
19	# the four parameter settings (control or parkinsonian PT5B BK and NaT conductances; rest or
20	# activated Ih factor and thalamic rates).
[... 903 more lines not kept]
```

**Agent**

Claims file has ~42 claims. Now the example entry formats.

**Agent calls Bash**

```bash
cd entries/001453-fouke-2025; cat entry.yaml requirements.in README.md; head -c 3000 omr.py; python -c "
import json;nb=json.load(open('reproduce_fouke_2025.ipynb'))
for c in nb['cells'][:8]: print(c['cell_type'],c.get('metadata'),''.join(c['source'])[:1500]); print('-----')
print(len(nb['cells']))
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
[... 237 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/001453-fouke-2025-01.yaml | head -150; ls questions | grep 1453; cat tools/entry.py | head -80
```

```
cat: attempts/001453-fouke-2025-01.yaml: No such file or directory
ls: cannot access 'questions': No such file or directory
cat: tools/entry.py: No such file or directory
```

**Agent calls Bash**

```bash
cd  cat attempts/001453-fouke-2025-01.yaml | head -200; ls questions | grep -E "1453|1444"; grep -n "def \|argparse\|add_parser" tools/entry.py | head -60
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
[... 201 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 200,400p attempts/001453-fouke-2025-01.yaml; sed -n 143,312p tools/entry.py
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
[... 349 more lines not kept]
```

**Agent**

Now the dataset.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/001444/ | python -m json.tool | head -40; curl -s https://api.dandiarchive.org/api/dandisets/001444/versions/ | python -m json.tool
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; V=0.250805.2002; curl -s "https://api.dandiarchive.org/api/dandisets/001444/versions/$V/assets/?page_size=100" | python -c "
import json,sys; d=json.load(sys.stdin)
for a in d['results']: print(a['asset_id'], a['path'], a['size'], a['blob'] if 'blob' in a else '')
"; curl -s "https://api.dandiarchive.org/api/dandisets/001444/versions/$V/" | python -c "
import json,sys; d=json.load(sys.stdin)
print(d['description']); print(d.get('relatedResource')); print(d.get('assetsSummary')); print(d.get('doi'))"; grep -n "paper cites\|dandi\|DANDI\|001444" paper/10.1038-s41531-025-01070-4.txt | head
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n 17,20p /home/runner/.claude/projects/-home-runner-work-encore-encore/4c89dc14-2bdb-46fc-a88e-53626ecd4fc1/tool-results/b69ywbn6t.txt | cut -c1-3000
```

```
376510a2-a951-47f6-a8ab-b99129b373a6 sub-001/sub-001_ses-sM1-12-12-2023-04.nwb 33802860 2e65e938-ed36-48c6-90f6-c069396aa742
Each simulation produced 4 files and we collected 4 sets of simulations for a total of 16 files. Each simulation included a control and parkinsonian condition in the rest (quiet wakefulness) and in the activated (movement) state. Parkinsonian M1 simulations were different from controls in that their PT5B neurons had reduced excitability as found in cortical slices of 6-OHDA treated mice.Each MWB file includes a local field potential trace, spike train data from all 10,073 neurons, and membrane potential traces from 400 of the layer 5B pyramidal tract (PT5B) neurons. Simulations were 4.3 seconds in duration. Full information available in our paper https://doi.org/10.1101/2024.05.23.595566
[]
{'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 7376447744, 'numberOfFiles': 17, 'numberOfSubjects': 1, 'variableMeasured': ['Units'], 'measurementTechnique': [{'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}]}
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd paper; wc -c *; grep -n -i "supplementary table 2\|dandi\|sM1\|zenodo\|github" 10.1038-s41531-025-01070-4.txt | head -30
```

```
<persisted-output>
Output too large (76.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/4c89dc14-2bdb-46fc-a88e-53626ecd4fc1/tool-results/b0w5ep3i9.txt

Preview (first 2KB):
 96177 10.1038-s41531-025-01070-4.txt
 43359 10.1101-2024.05.23.595566.txt
139536 total
7:pmc NPJ Parkinsons Dis NPJ Parkinsons Dis NPJ Parkinson's Disease 2373-8057 Nature Publishing Group UK London 12325672 40764619 1070 10.1038/s41531-025-01070-4 Article Enhanced beta power emerges from simulated parkinsonian primary motor cortex Doherty Donald W. [removed: an e-mail address] 1 2 Chen Liqiang 2 3 Smith Yoland 2 4 Wichmann Thomas 2 4 Chu Hong-Yuan 2 3 Lytton William W. 1 2 5 1 https://ror.org/0041qmd21 grid.262863.b 0000 0001 0693 2202 Department of Physiology & Pharmacology, SUNY Downstate Medical Center, Brooklyn, NY 11203 USA 2 grid.513948.2 0000 0005 0380 6410 Aligning Science Across Parkinson’s (ASAP) Collaborative Research Network, Chevy Chase, MD 20815 USA 3 https://ror.org/00hjz7x27 grid.411667.3 0000 0001 2186 0438 Department of Pharmacology and Physiology, Georgetown University Medical Center, Washington D.C., USA 4 https://ror.org/03czfpz43 grid.189967.8 0000 0001 0941 6502 Emory National Primate Research Center, Department of Neurology, Udall Center of Excellence for Parkinson’s Disease Research, Emory University, School of Medicine, Atlanta, GA 30329 USA 5 https://ror.org/02emy8e21 grid.415345.2 0000 0004 0451 974X Kings County Hospital, Brooklyn, NY 11203 USA 5 8 2025 5 8 2025 2025 11 230 18 3 2025 6 7 2025 © The Author(s) 2025 2025 https://creativecommons.org/licenses/by/4.0/ Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made.
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; fold -s -w 200 10.1038-s41531-025-01070-4.txt > $TMPDIR/paper.txt; wc -l $TMPDIR/paper.txt
```

```
776 /tmp/claude-1001/paper.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/paper.txt",
 "offset": 1,
 "limit": 420
}
```

```
File content (32842 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/paper.txt",
 "offset": 1,
 "limit": 280
}
```

```
1	DOI: 10.1038/s41531-025-01070-4
2	Version: as served by europe_pmc
3	Source: europe_pmc+crossref (paper-text-fetcher)
4	Stored: 2026-10-21
5	Extracted: as fetched
6	------------------------------------------------------------------------
7	pmc NPJ Parkinsons Dis NPJ Parkinsons Dis NPJ Parkinson's Disease 2373-8057 Nature Publishing Group UK London 12325672 40764619 1070 10.1038/s41531-025-01070-4 Article Enhanced beta power emerges 
8	from simulated parkinsonian primary motor cortex Doherty Donald W. [removed: an e-mail address] 1 2 Chen Liqiang 2 3 Smith Yoland 2 4 Wichmann Thomas 2 4 Chu Hong-Yuan 2 3 Lytton William W. 
9	1 2 5 1 https://ror.org/0041qmd21 grid.262863.b 0000 0001 0693 2202 Department of Physiology & Pharmacology, SUNY Downstate Medical Center, Brooklyn, NY 11203 USA 2 grid.513948.2 0000 0005 0380 6410 
10	Aligning Science Across Parkinson’s (ASAP) Collaborative Research Network, Chevy Chase, MD 20815 USA 3 https://ror.org/00hjz7x27 grid.411667.3 0000 0001 2186 0438 Department of Pharmacology and 
11	Physiology, Georgetown University Medical Center, Washington D.C., USA 4 https://ror.org/03czfpz43 grid.189967.8 0000 0001 0941 6502 Emory National Primate Research Center, Department of Neurology, 
12	Udall Center of Excellence for Parkinson’s Disease Research, Emory University, School of Medicine, Atlanta, GA 30329 USA 5 https://ror.org/02emy8e21 grid.415345.2 0000 0004 0451 974X Kings County 
13	Hospital, Brooklyn, NY 11203 USA 5 8 2025 5 8 2025 2025 11 230 18 3 2025 6 7 2025 © The Author(s) 2025 2025 https://creativecommons.org/licenses/by/4.0/ Open Access This article is licensed under a 
14	Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the 
15	original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party m
[... 265 more lines not kept]
```

**Agent**

Paper read. Now opening a file of set 12-12-2023 to list its contents.

**Agent calls Bash**

```bash
date -u; python -c "import pynwb, remfile, h5py, numpy, scipy; print(pynwb.__version__, h5py.__version__, numpy.__version__, scipy.__version__)"; which uv python; python --version
```

```
Mon Nov  2 17:00:22 UTC 2026
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pynwb, remfile, h5py, numpy, scipy; print(pynwb.__version__, h5py.__version__, numpy.__version__, scipy.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pynwb'
/opt/hostedtoolcache/Python/3.13.17/x64/bin/uv
/opt/hostedtoolcache/Python/3.13.17/x64/bin/python
Python 3.13.17
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q venv && . venv/bin/activate && uv pip install -q pynwb remfile h5py numpy scipy pandas matplotlib dandi elephant quantities neo 2>&1 | tail -3; python -c "import pynwb, elephant; print(pynwb.__version__, elephant.__version__)"
```

```
4.2.0 1.2.1
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && cat > survey.py <<'EOF'
import h5py, remfile, requests, time
V="0.250805.2002"
r=requests.get(f"https://api.dandiarchive.org/api/dandisets/001444/versions/{V}/assets/",params={"page_size":100}).json()
assets={a['path']:a['asset_id'] for a in r['results']}
p="sub-001/sub-001_ses-sM1-12-12-2023-01.nwb"
url=f"https://api.dandiarchive.org/api/assets/{assets[p]}/download/"
t=time.time()
f=h5py.File(remfile.File(requests.head(url,allow_redirects=True).url),'r')
def visit(name,obj):
    if isinstance(obj,h5py.Dataset):
        print(name, obj.shape, obj.dtype, dict((k,(v if not hasattr(v,'shape') or v.size<5 else v.shape)) for k,v in obj.attrs.items() if k not in ('namespace','object_id')))
    else:
        a={k:v for k,v in obj.attrs.items() if k not in ('namespace','object_id')}
        print("G",name,a)
f.visititems(visit)
print(time.time()-t)
EOF
python survey.py 2>&1 | head -150
```

```
G acquisition {}
G acquisition/Segment 0 LFP 0 {'comments': '{"block": "block0", "segment": "Segment 0"}', 'description': 'no description', 'neurodata_type': 'TimeSeries'}
acquisition/Segment 0 LFP 0/data (172000, 1) float64 {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'mV'}
acquisition/Segment 0 LFP 0/starting_time () float64 {'rate': np.float64(40000.0), 'unit': 'seconds'}
G acquisition/Segment 0 PT5B 5201 1 {'comments': '{"block": "block0", "segment": "Segment 0"}', 'description': 'no description', 'neurodata_type': 'TimeSeries'}
acquisition/Segment 0 PT5B 5201 1/data (172000, 1) float64 {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'mV'}
acquisition/Segment 0 PT5B 5201 1/starting_time () float64 {'rate': np.float64(40000.0), 'unit': 'seconds'}
G acquisition/Segment 0 PT5B 5202 2 {'comments': '{"block": "block0", "segment": "Segment 0"}', 'description': 'no description', 'neurodata_type': 'TimeSeries'}
acquisition/Segment 0 PT5B 5202 2/data (172000, 1) float64 {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'mV'}
acquisition/Segment 0 PT5B 5202 2/starting_time () float64 {'rate': np.float64(40000.0), 'unit': 'seconds'}
G acquisition/Segment 0 PT5B 5301 3 {'comments': '{"block": "block0", "segment": "Segment 0"}', 'description': 'no description', 'neurodata_type': 'TimeSeries'}
acquisition/Segment 0 PT5B 5301 3/data (172000, 1) float64 {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'mV'}
acquisition/Segment 0 PT5B 5301 3/starting_time () float64 {'rate': np.float64(40000.0), 'unit': 'seconds'}
G acquisition/Segment 0 PT5B 5302 4 {'comments': '{"block": "block0", "segment": "Segment 0"}', 'description': 'no description', 'neurodata_type': 'TimeSeries'}
acquisition/Segment 0 PT5B 5302 4/data (172000, 1) float64 {'conversion': np.float64(1.0), 'offset': np.floa
[... 112 more lines not kept]
```

**Agent**

The 12-12-2023 files hold one LFP trace and 20 PT5B voltage traces. Listing the unit names and metadata.

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && cat > survey2.py <<'EOF'
import h5py, remfile, requests, time, numpy as np, collections, sys
V="0.250805.2002"
r=requests.get(f"https://api.dandiarchive.org/api/dandisets/001444/versions/{V}/assets/",params={"page_size":100}).json()
assets={a['path']:a['asset_id'] for a in r['results']}
p=sys.argv[1]
url=f"https://api.dandiarchive.org/api/assets/{assets[p]}/download/"
f=h5py.File(remfile.File(requests.head(url,allow_redirects=True).url),'r')
for k in ['general/experiment_description','general/experimenter','general/institution','general/keywords','general/lab','general/related_publications','general/session_id','general/subject/age','general/subject/description','general/subject/sex','general/subject/species','general/subject/subject_id','identifier','session_description','session_start_time','timestamps_reference_time','file_create_date']:
    print(k, f[k][()])
names=f['units/_name'][:].astype(str)
pops=collections.Counter(n.rsplit(' ',1)[0] for n in names)
print(pops)
print(collections.Counter(f['units/segment'][:].astype(str)), collections.Counter(f['units/block'][:].astype(str)))
oi=f['units/obs_intervals'][:]; print('obs', np.unique(oi,axis=0)[:5])
st=f['units/spike_times'][:]; idx=f['units/spike_times_index'][:]
print('spike times range', st.min(), st.max(), len(st))
print(names[:5], names[-5:])
ids=f['units/id'][:]; print(ids[:5], ids[-5:])
print([k for k in f['acquisition']][:3], len(f['acquisition']))
EOF
python survey2.py sub-001/sub-001_ses-sM1-12-12-2023-01.nwb
```

```
general/experiment_description b'Simulated mouse primary motor cortex in control and 6-OHDA induced parkinsonism.'
general/experimenter [b'Doherty, Donald']
general/institution b'SUNY Downstate Health Sciences University'
general/keywords [b"Parkinson's disease" b'mouse' b'primary motor cortex' b'M1' b'beta']
general/lab b'NeuroSim Lab'
general/related_publications [b'https://doi.org/10.1101/2024.05.23.595566']
general/session_id b'sM1_12-12-2023_01'
general/subject/age b'P16W'
general/subject/description b'simulated mouse'
general/subject/sex b'O'
general/subject/species b'Mus musculus'
general/subject/subject_id b'001'
identifier b'0d130e68-8e73-4cd7-938d-e72258705b1d'
session_description b'control, quiet wakefulness'
session_start_time b'2023-12-12T15:23:00-05:00'
timestamps_reference_time b'2023-12-12T15:23:00-05:00'
file_create_date [b'2025-07-05T22:47:21.557510-04:00']
Counter({'PT5B': 1435, 'OC': 955, 'TPO': 953, 'S1': 951, 'S2': 937, 'M2': 929, 'IT6': 914, 'cM1': 897, 'TVL': 894, 'IT5B': 816, 'PV5B': 445, 'IT5A': 239, 'IT2': 137, 'SOM2': 125, 'SOM6': 89, 'PV5A': 89, 'SOM5B': 66, 'CT6': 53, 'SOM5A': 40, 'PV2': 13, 'IT4': 11, 'PV6': 8})
Counter({np.str_('Segment 0'): 10996}) Counter({np.str_('block0'): 10996})
obs [[0.  4.3]]
[... 5 more lines not kept]
```

**Agent**

Key finding: the units table holds only 4,480 M1 units (of 10,073), apparently only neurons that spiked. Checking whether the gids in the unit names reveal the full population ranges.

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && cat > survey3.py <<'EOF'
import h5py, remfile, requests, numpy as np, collections, sys
V="0.250805.2002"
r=requests.get(f"https://api.dandiarchive.org/api/dandisets/001444/versions/{V}/assets/",params={"page_size":100}).json()
assets={a['path']:a['asset_id'] for a in r['results']}
for p in sys.argv[1:]:
    url=f"https://api.dandiarchive.org/api/assets/{assets[p]}/download/"
    f=h5py.File(remfile.File(requests.head(url,allow_redirects=True).url),'r')
    names=f['units/_name'][:].astype(str)
    idx=f['units/spike_times_index'][:]; n=np.diff(np.r_[0,idx])
    pop=np.array([x.rsplit(' ',1)[0] for x in names]); gid=np.array([int(x.rsplit(' ',1)[1]) for x in names])
    print(p, len(names), 'zero-spike units', (n==0).sum(), 'dup names', len(names)-len(set(names)))
    rows=[]
    for q in sorted(set(pop), key=lambda q: gid[pop==q].min()):
        g=gid[pop==q]; rows.append((q, g.min(), g.max(), g.max()-g.min()+1, len(g)))
    for r_ in rows: print('  ',r_)
    print('  acq', len(f['acquisition']), [k for k in f['acquisition'] if 'LFP' in k], f['acquisition/Segment 0 LFP 0/data'].shape)
EOF
python survey3.py sub-001/sub-001_ses-sM1-12-12-2023-01.nwb sub-001/sub-001_ses-sM1-12-12-2023-03.nwb
```

```
sub-001/sub-001_ses-sM1-12-12-2023-01.nwb 10996 zero-spike units 0 dup names 0
   (np.str_('IT2'), np.int64(2), np.int64(1729), np.int64(1728), 137)
   (np.str_('SOM2'), np.int64(1730), np.int64(1856), np.int64(127), 125)
   (np.str_('PV2'), np.int64(1858), np.int64(2086), np.int64(229), 13)
   (np.str_('IT4'), np.int64(2134), np.int64(2867), np.int64(734), 11)
   (np.str_('IT5A'), np.int64(2886), np.int64(3517), np.int64(632), 239)
   (np.str_('SOM5A'), np.int64(3525), np.int64(3580), np.int64(56), 40)
   (np.str_('PV5A'), np.int64(3582), np.int64(3693), np.int64(112), 89)
   (np.str_('IT5B'), np.int64(3695), np.int64(5129), np.int64(1435), 816)
   (np.str_('PT5B'), np.int64(5130), np.int64(6564), np.int64(1435), 1435)
   (np.str_('SOM5B'), np.int64(6565), np.int64(6810), np.int64(246), 66)
   (np.str_('PV5B'), np.int64(6816), np.int64(7326), np.int64(511), 445)
   (np.str_('IT6'), np.int64(7327), np.int64(8562), np.int64(1236), 914)
   (np.str_('CT6'), np.int64(8571), np.int64(9766), np.int64(1196), 53)
   (np.str_('SOM6'), np.int64(9799), np.int64(9888), np.int64(90), 89)
   (np.str_('PV6'), np.int64(9932), np.int64(10064), np.int64(133), 8)
   (np.str_('TPO'), np.int64(10073), np.int64(11072), np.int64(1000), 953)
   (np.str_('TVL'), np.int64(11073), np.int64(12072), np.int64(1000), 894)
   (np.str_('S1'), np.int64(12073), np.int64(13072), np.int64(1000), 951)
   (np.str_('S2'), np.int64(13073), np.int64(14072), np.int64(1000), 937)
[... 29 more lines not kept]
```

**Agent**

Units table holds only neurons that spiked; input gids start at 10073, so M1 gids are 0 to 10072. Now surveying a file of the larger sets.

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && cat > survey4.py <<'EOF'
import h5py, remfile, requests, numpy as np, collections, sys
V="0.250805.2002"
r=requests.get(f"https://api.dandiarchive.org/api/dandisets/001444/versions/{V}/assets/",params={"page_size":100}).json()
assets={a['path']:a['asset_id'] for a in r['results']}
for p in sys.argv[1:]:
    url=f"https://api.dandiarchive.org/api/assets/{assets[p]}/download/"
    f=h5py.File(remfile.File(requests.head(url,allow_redirects=True).url),'r')
    acq=list(f['acquisition'])
    print(p, f['session_description'][()], f['general/session_id'][()], f['session_start_time'][()], 'units', len(f['units/_name']), 'acq', len(acq))
    print('  LFP:', [k for k in acq if 'LFP' in k], ' other non-PT5B:', [k for k in acq if 'PT5B' not in k and 'LFP' not in k][:5])
    k=[k for k in acq if 'PT5B' in k]; print('  ', k[:3], k[-2:], f['acquisition'][k[0]]['data'].shape, f['acquisition'][k[0]]['data'].chunks, f['acquisition'][k[0]]['data'].compression)
    print('  keys', list(f.keys()), list(f['processing']), list(f['analysis']))
EOF
python survey4.py sub-001/sub-001_ses-sM1-04-22-2024-01.nwb sub-001/sub-001.nwb
```

```
sub-001/sub-001_ses-sM1-04-22-2024-01.nwb b'control, quiet wakefulness' b'sM1_04-22-2024_01' b'2024-04-22T11:09:00-05:00' units 11228 acq 401
  LFP: ['Segment 0 LFP 0']  other non-PT5B: []
   ['Segment 0 PT5B 5130 1', 'Segment 0 PT5B 5131 2', 'Segment 0 PT5B 5132 3'] ['Segment 0 PT5B 5528 399', 'Segment 0 PT5B 5529 400'] (172000, 1) None None
  keys ['acquisition', 'analysis', 'file_create_date', 'general', 'identifier', 'processing', 'session_description', 'session_start_time', 'specifications', 'stimulus', 'timestamps_reference_time', 'units'] [] []
sub-001/sub-001.nwb b'control, quiet wakefulness' b'sM1_04-22-2024_01' b'2024-04-22T11:09:00-05:00' units 11228 acq 401
  LFP: ['Segment 0 LFP 0']  other non-PT5B: []
   ['Segment 0 PT5B 5130 1', 'Segment 0 PT5B 5131 2', 'Segment 0 PT5B 5132 3'] ['Segment 0 PT5B 5528 399', 'Segment 0 PT5B 5529 400'] (172000, 1) None None
  keys ['acquisition', 'analysis', 'file_create_date', 'general', 'identifier', 'processing', 'session_description', 'session_start_time', 'specifications', 'stimulus', 'timestamps_reference_time', 'units'] [] []
Shell cwd was reset to
```

**Agent**

Other sets hold 400 PT5B traces and one LFP; `sub-001.nwb` is the same blob as `04-22-2024-01`. Fetching NetPyNE 1.0.5 source to see its spectrogram method (reading S1).

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && pip download -q netpyne==1.0.5 --no-deps -d nd 2>&1 | tail -2; ls nd; cd nd && unzip -q -o *.whl -d src 2>/dev/null || tar xzf *.tar.gz -C .; ls; find . -name morlet.py; find . -path "*analysis*" -name "*lfp*"
```

```
netpyne-1.0.5-py2.py3-none-any.whl
netpyne-1.0.5-py2.py3-none-any.whl
src
./src/netpyne/support/morlet.py
./src/netpyne/analysis/lfp_orig.py
./src/netpyne/analysis/lfp.py
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/nd/src/netpyne; cat support/morlet.py; grep -n "def prepareSpectrogram" -A 120 analysis/lfp.py | head -170
```

```
"""
Module with support for Morlet wavelets

Time-frequency representation using Morlet wavelets

 Original version written by Shane Lee (Brown University)
 Modified by Sam Neymotin (NKI; added phase calculations, saving/passing in Morlet, specifying different
 frequency steps and frequencies used for calculations (e.g. logarithmic frequency instead of linear)
 don't detrend the signal > 1 time; don't waste RAM by copying/storing time-series in MorletSpec class;
 subtract mean from time series within the wavelet class)
"""

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from __future__ import absolute_import

import numpy as np
import scipy.signal as sps
import matplotlib.pyplot as plt
[... 216 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nd/src/netpyne; sed -n 393,420p analysis/lfp.py; grep -n "def prepareLFP" -A 80 analysis/lfp.py | grep -n "timeRange\|lfp = \|recordStep\|electrodes\|avg\|normSignal\|filtFreq" | head -30
```

```
lfp_elec,
                fs=fs,
                window='hanning',
                detrend=mlab.detrend_none,
                nperseg=nperseg,
                noverlap=noverlap,
                nfft=NFFT,
                mode='psd',
            )
            x_mesh, y_mesh = np.meshgrid(t_spec * 1000.0, f[f < maxFreq])
            spect_data['fft'].append(10 * np.log10(x_spec[f < maxFreq]))

        vmin = np.array(spect_data['fft']).min()
        vmax = np.array(spect_data['fft']).max()

        spect_data['vmin'] = vmin
        spect_data['vmax'] = vmax

        spect_data['xmesh'] = x_mesh
        spect_data['ymesh'] = y_mesh
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && cat > survey5.py <<'EOF'
import h5py, remfile, requests, numpy as np, collections, time
V="0.250805.2002"
r=requests.get(f"https://api.dandiarchive.org/api/dandisets/001444/versions/{V}/assets/",params={"page_size":100}).json()
assets={a['path']:a['asset_id'] for a in r['results']}
allg=collections.defaultdict(set)
for p in sorted(assets):
    t=time.time()
    url=f"https://api.dandiarchive.org/api/assets/{assets[p]}/download/"
    f=h5py.File(remfile.File(requests.head(url,allow_redirects=True).url),'r')
    names=f['units/_name'][:].astype(str); idx=f['units/spike_times_index'][:]
    for x in names:
        q,g=x.rsplit(' ',1); allg[q].add(int(g))
    m1=[x for x in names if int(x.rsplit(' ',1)[1])<10073]
    print(p, f['session_description'][()].decode(), 'units',len(names),'M1',len(m1),'spikes',idx[-1], 'Vm', len(f['acquisition'])-1, f'{time.time()-t:.1f}s')
order=sorted(allg,key=lambda q:min(allg[q]))
for a,b in zip(order,order[1:]+[None]):
    print(a, min(allg[a]), max(allg[a]), len(allg[a]), 'next min', min(allg[b]) if b else None)
EOF
python survey5.py
```

```
sub-001/sub-001.nwb control, quiet wakefulness units 11228 M1 4714 spikes 212347 Vm 400 10.9s
sub-001/sub-001_ses-sM1-04-22-2024-01.nwb control, quiet wakefulness units 11228 M1 4714 spikes 212347 Vm 400 9.7s
sub-001/sub-001_ses-sM1-04-22-2024-02.nwb parkinsonian, quiet wakefulness units 10306 M1 3792 spikes 242831 Vm 400 10.7s
sub-001/sub-001_ses-sM1-04-22-2024-03.nwb control, movement units 10332 M1 3725 spikes 393444 Vm 400 11.9s
sub-001/sub-001_ses-sM1-04-22-2024-04.nwb parkinsonian, movement units 10213 M1 3606 spikes 390429 Vm 400 12.1s
sub-001/sub-001_ses-sM1-04-25-2024-01.nwb control, quiet wakefulness units 10341 M1 3826 spikes 250158 Vm 400 11.1s
sub-001/sub-001_ses-sM1-04-25-2024-02.nwb parkinsonian, quiet wakefulness units 9663 M1 3148 spikes 293774 Vm 400 10.9s
sub-001/sub-001_ses-sM1-04-25-2024-03.nwb control, movement units 9660 M1 3060 spikes 409246 Vm 400 10.7s
sub-001/sub-001_ses-sM1-04-25-2024-04.nwb parkinsonian, movement units 9713 M1 3113 spikes 409133 Vm 400 9.6s
sub-001/sub-001_ses-sM1-04-26-2024-01.nwb control, quiet wakefulness units 10444 M1 3979 spikes 263720 Vm 400 10.5s
sub-001/sub-001_ses-sM1-04-26-2024-02.nwb parkinsonian, quiet wakefulness units 9586 M1 3121 spikes 295477 Vm 400 11.7s
sub-001/sub-001_ses-sM1-04-26-2024-03.nwb control, movement units 9432 M1 2848 spikes 399894 Vm 400 10.7s
sub-001/sub-001_ses-sM1-04-26-2024-04.nwb parkinsonian, movement units 9349 M1 2765 spikes 404006 Vm 400 11.3s
sub-001/sub-001_ses-sM1-12-12-2023-01.nwb control, quiet wakefulness units 10996 M1 4480 spikes 213007 Vm 20 1.4s
sub-001/sub-001_ses-sM1-12-12-2023-02.nwb parkinsonian, quiet wakefulness units 9747 M1 3231 spikes 208550 Vm 20 1.3s
sub-001/sub-001_ses-sM1-12-12-2023-03.nwb control, movement units 9536 M1 2919 spikes 385529 Vm 20 1.4s
sub-001/sub-001_ses-sM1-12-12-2023-04.nwb parkinsonian, movement units 9534 M1 2917 spikes 388355 Vm 20 1.3s
IT2 1 1729 726 next min 1730
SOM2 1730 1856 127 next min 1857
PV2 1857 2113 175 next min 2114
[... 20 more lines not kept]
```

**Agent**

Population blocks are nearly exact from the data (ambiguities of 1 to 8 gids at four boundaries). Now writing the helper module.

**Agent calls Bash**

```bash
date -u; cd  ls entries | head; cat schemas/attempt*.json | python -c "import json,sys; d=json.load(sys.stdin); print(json.dumps(d['properties']['outcomes'],indent=0)[:3000])"
```

```
Mon Nov  2 17:05:53 UTC 2026
000003-senzai-2017
000004-chandravadia-2020
000005-yu-2016
000006-economo-2018
000008-scala-2021
000009-guo-2017
000010-li-2015
000011-li-2016
000013-hires-2015
000015-chen-2017
{
"description": "One per claim attempted.",
"type": "array",
"minItems": 1,
"items": {
"type": "object",
"additionalProperties": false,
"required": [
"claim",
[... 149 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/001444-doherty-2025/m1sim.py",
 "content": "\"\"\"Loading and measures for the simulated mouse M1 of dandiset 001444.\n\nDoherty, Chen, Smith, Wichmann, Chu & Lytton (2025), npj Parkinson's Disease 11, 230,\ndoi:10.1038/s41531-025-01070-4. Claims: claims/001444/10.1038-s41531-025-01070-4.yaml.\n\nEach NWB file is one 4.3 s NetPyNE simulation. It holds a units table whose `_name` is\n\"<population> <gid>\" (M1 cells and the Poisson input generators), one LFP trace\n(\"Segment 0 LFP 0\", 40 kHz, mV) and somatic membrane potentials of some PT5B cells\n(\"Segment 0 PT5B <gid> <n>\", 40 kHz, mV). Spike times are in seconds. Files are streamed from\nthe archive at the pinned version; nothing is written to disk.\n\nWhere the parameters come from:\n\n- `WINDOW` (2.0 to 4.3 s): the claims file's window W, from the Fig. 2C and 5C legends (\"the\n  last 2.3 s of 4.3 s simulation\") and the Fig. 3 and 6 legends (\"2.3 s of activity starting\n  2 s after simulation initiation\").\n- `SCH_BIN` (2 ms): the PT5B spike count histogram of the Fig. 2 and 5 legends (\"2 ms bins\").\n- `M1_POPS` and their order: the 15 M1 populations of the model (claims file, cfg.py allpops).\n  The files hold only cells that fired (data check), so the size of each population is taken\n  from the data: gids are numbered in contiguous blocks per population (NetPyNE), and\n  `population_blocks` bounds each block by the gids seen in all 16 files. Where a few gids\n  between two blocks were never seen, the lower and upper sizes are both kept.\n- Rate readings R1 (all cells of a population) and R2 (cells with a spike in W), and test\n  readings T1 to T4: the claims file's definitions.\n- `welch_peak`: Welch's method with 1 s segments, the claims file's standard choice.\n- `morlet_spec`: a copy of netpyne/support/morlet.py of NetPyNE 1.0.5 (the version the Methods\n  name), with the defaults of netpyne.analysis.lfp.prepareSpectrogram (1 to 100 Hz in 1 Hz\n  steps, 7 cycles; the signal has its mean removed and is linearly detrended). Reading S1.\n- `stft_spec`: reading S2. NetPyNE's fft option with its defaults (nperseg 256 at 40 kHz) has a\n  frequency step of 156 Hz and cannot resolve any band of the claims, so S2 uses a 250 ms Hann\n  window with 90% overlap (4 Hz steps), a standard choice stated in the notebook.\n- `band_bursts`: the claims file's burst reading, epochs where band power is above halfway\n  between its minimum and maximum in W (the half-height convention of Methods, Duty cycle).\n- `duty_cycles`: Results, Control simulations, paragraph 4, and Methods, Duty cycle, with the\n  readings of the claims file (half-height global or per period; mean of periods or total).\n- `coincident_fraction`: Results, Control simulations, paragraph 7 (\"within a 1 ms time window\"),\n  readings (a) another PT5B spike within 1 ms either side and (b) the same 1 ms bin.\n- `unitary_events`: Methods, Identifying synchronous spiking, and the Fig. 4 and 7 legends\n  (joint-surprise test, p < 0.05, \"100 ms firing rate window\"), readings of the claims file. The\n  expected number of coincidences in a window assumes independent Poisson cells at the rates\n  of that window (Grun et al. 2002); coincidence bins are 1 ms (Results).\n\"\"\"\n\nfrom __future__ import annotations\n\nfrom functools import lru_cache\n\nimport h5py\nimport numpy as np\nimport remfile\nimport requests\nimport scipy.signal as sps\nfrom scipy import stats\n\nDANDISET_ID = \"001444\"\nDANDISET_VERSION = \"0.250805.2002\"\nAPI = \"https://api.dandiarchive.org/api\"\n\nPAPER_SET = \"sM1-12-12-2023\"\nCONDITIONS = {\"01\": \"control rest\", \"02\": \"parkinsonian rest\",\n              \"03\": \"control activated\", \"04\": \"parkinsonian activated\"}\nSETS = [\"sM1-12-12-2023\", \"sM1-04-22-2024\", \"sM1-04-25-2024\", \"sM1-04-26-2024\"]\n\nDURATION = 4.3\nWINDOW = (2.0, 4.3)\nSCH_BIN = 0.002\nFS = 40000.0\nM1_POPS = [\"IT2\", \"SOM2\", \"PV2\", \"IT4\", \"IT5A\", \"SOM5A\", \"PV5A\", \"IT5B\", \"PT5B\", \"SOM5B\",\n           \"PV5B\", \"IT6\", \"CT6\", \"SOM6\", \"PV6\"]\nEXCITATORY = [\"IT2\", \"IT4\", \"IT5A\", \"IT5B\", \"PT5B\", \"IT6\", \"CT6\"]\nFIRST_INPUT_GID = 10073\n\n\n# ---------------------------------------------------------------- loading\n\n@lru_cache(maxsize=1)\ndef assets() -> dict:\n    \"\"\"Path -> (asset id, blob id, size) for the pinned version.\"\"\"\n    out, url = {}, f\"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/\"\n    params = {\"page_size\": 200}\n    while url:\n        page = requests.get(url, params=params, timeout=60).json()\n        for a in page[\"results\"]:\n            out[a[\"path\"]] = (a[\"asset_id\"], a.get(\"blob\"), a[\"size\"])\n        url, params = page.get(\"next\"), None\n    return out\n\n\ndef path_of(set_name: str, cond: str) -> str:\n    return f\"sub-001/sub-001_ses-{set_name}-{cond}.nwb\"\n\n\ndef open_nwb(path: str) -> h5py.File:\n    asset_id = assets()[path][0]\n    s3 = requests.head(f\"{API}/assets/{asset_id}/download/\", allow_redirects=True, timeout=60).url\n    return h5py.File(remfile.File(s3), \"r\")\n\n\ndef read_units(f: h5py.File) -> dict:\n    \"\"\"Spike trains by gid, with population names. Times in seconds.\"\"\"\n    names = f[\"units/_name\"][:].astype(str)\n    st = f[\"units/spike_times\"][:]\n    idx = f[\"units/spike_times_index\"][:]\n    starts = np.r_[0, idx[:-1]]\n    pops = np.array([n.rsplit(\" \", 1)[0] for n in names])\n    gids = np.array([int(n.rsplit(\" \", 1)[1]) for n in names])\n    trains = {int(g): np.sort(st[a:b]) for g, a, b in zip(gids, starts, idx)}\n    return {\"pop\": dict(zip(gids.tolist(), pops.tolist())), \"trains\": trains,\n            \"unsorted\": int(sum(np.any(np.diff(st[a:b]) < 0) for a, b in zip(starts, idx))),\n            \"obs_intervals\": np.unique(f[\"units/obs_intervals\"][:], axis=0)}\n\n\ndef read_meta(f: h5py.File) -> dict:\n    g = lambda k: f[k][()].decode() if isinstance(f[k][()], bytes) else f[k][()]\n    return {\"session_id\": g(\"general/session_id\"), \"description\": g(\"session_description\"),\n            \"start\": g(\"session_start_time\")}\n\n\ndef vm_names(f: h5py.File) -> list[str]:\n    return [k for k in f[\"acquisition\"] if \" PT5B \" in k]\n\n\ndef read_series(f: h5py.File, name: str, window=None) -> tuple[np.ndarray, float, str]:\n    ts = f[\"acquisition\"][name]\n    rate = float(ts[\"starting_time\"].attrs[\"rate\"])\n    t0 = float(ts[\"starting_time\"][()])\n    d = ts[\"data\"]\n    if window is None:\n        x = d[:, 0]\n    else:\n        a, b = int(round((window[0] - t0) * rate)), int(round((window[1] - t0) * rate))\n        x = d[a:b, 0]\n    return np.asarray(x, float), rate, ts[\"data\"].attrs[\"unit\"]\n\n\ndef load_file(set_name: str, cond: str, lfp=True, vm=True) -> dict:\n    path = path_of(set_name, cond)\n    f = open_nwb(path)\n    out = {\"path\": path, \"set\": set_name, \"cond\": cond, **read_meta(f), **read_units(f)}\n    if lfp:\n        out[\"lfp\"], out[\"lfp_rate\"], out[\"lfp_unit\"] = read_series(f, \"Segment 0 LFP 0\")\n        out[\"lfp_t0\"] = float(f[\"acquisition/Segment 0 LFP 0/starting_time\"][()])\n    names = vm_names(f)\n    out[\"vm_gids\"] = [int(n.split()[3]) for n in names]\n    if vm:\n        out[\"vm\"] = {int(n.split()[3]): read_series(f, n)[0] for n in names}\n    out[\"n_acquisition\"] = len(f[\"acquisition\"])\n    return out\n\n\n# ---------------------------------------------------------------- populations\n\ndef population_blocks(pop_maps: list[dict]) -> dict:\n    \"\"\"Bound each M1 population's gid block from the gids seen in any file.\n\n    Returns pop -> (low_start, high_start, low_end, high_end, n_min, n_max): the block starts\n    somewhere in [low_start, high_start] and ends in [low_end, high_end].\n    \"\"\"\n    seen = {}\n    for m in pop_maps:\n        for g, p in m.items():\n            if p in M1_POPS:\n                lo, hi = seen.get(p, (g, g))\n                seen[p] = (min(lo, g), max(hi, g))\n    order = sorted(seen, key=lambda p: seen[p][0])\n    assert order == M1_POPS, order\n    out = {}\n    for i, p in enumerate(order):\n        lo, hi = seen[p]\n        prev_hi = seen[order[i - 1]][1] if i else -1\n        next_lo = seen[order[i + 1]][0] if i + 1 < len(order) else FIRST_INPUT_GID\n        out[p] = (prev_hi + 1, lo, hi, next_lo - 1, hi - lo + 1, next_lo - prev_hi - 1)\n    return out\n\n\ndef rates(d: dict, pop: str, blocks: dict, window=WINDOW, size=\"max\") -> dict:\n    \"\"\"Per-cell rates (spikes/s) in `window`.\n\n    R1: every gid of the block, silent cells at 0 (block of the largest size if `size`=\"max\",\n    smallest if \"min\"). R2: only cells with at least one spike in the window.\n    \"\"\"\n    b = blocks[pop]\n    lo, hi = (b[0], b[3]) if size == \"max\" else (b[1], b[2])\n    dur = window[1] - window[0]\n    gids = np.arange(lo, hi + 1)\n    r = np.zeros(len(gids))\n    for i, g in enumerate(gids):\n        t = d[\"trains\"].get(int(g))\n        if t is not None and d[\"pop\"][int(g)] == pop:\n            r[i] = np.count_nonzero((t >= window[0]) & (t < window[1])) / dur\n    return {\"gid\": gids, \"R1\": r, \"R2_mask\": r > 0}\n\n\ndef summary(r: np.ndarray) -> tuple[float, float, int]:\n    return (float(np.mean(r)) if len(r) else np.nan,\n            float(np.std(r, ddof=1)) if len(r) > 1 else np.nan, len(r))\n\n\ndef tests(a: np.ndarray, b: np.ndarray, paired_ok=True) -> dict:\n    \"\"\"T1 Wilcoxon signed-rank (paired), T2 paired t, T3 Mann-Whitney U, T4 Welch t; two-sided.\"\"\"\n    out = {}\n    if paired_ok:\n        diff = a - b\n        out[\"T1 Wilcoxon\"] = stats.wilcoxon(a, b).pvalue if np.any(diff != 0) else 1.0\n        out[\"T2 paired t\"] = stats.ttest_rel(a, b).pvalue\n    out[\"T3 Mann-Whitney\"] = stats.mannwhitneyu(a, b, alternative=\"two-sided\").pvalue\n    out[\"T4 Welch t\"] = stats.ttest_ind(a, b, equal_var=False).pvalue\n    return out\n\n\n# ---------------------------------------------------------------- spectra\n\ndef pop_spikes(d: dict, pop: str) -> np.ndarray:\n    return np.sort(np.concatenate([t for g, t in d[\"trains\"].items() if d[\"pop\"][g] == pop]\n                                  or [np.array([])]))\n\n\ndef sch(spikes: np.ndarray, window=WINDOW, bin_s=SCH_BIN) -> tuple[np.ndarray, np.ndarray]:\n    edges = np.arange(window[0], window[1] + bin_s / 2, bin_s)\n    counts, _ = np.histogram(spikes, edges)\n    return edges[:-1], counts.astype(float)\n\n\ndef welch_peak(x: np.ndarray, fs: float, fmin: float = 0.0, fmax: float = 100.0,\n               seg_s: float = 1.0) -> tuple[float, np.ndarray, np.ndarray]:\n    f, p = sps.welch(x - np.mean(x), fs=fs, nperseg=int(seg_s * fs))\n    sel = (f > fmin) & (f <= fmax)\n    return float(f[sel][np.argmax(p[sel])]), f, p\n\n\ndef morlet(sampr, freq, width=7.0):\n    # netpyne/support/morlet.py (NetPyNE 1.0.5), Morlet()\n    dt = 1.0 / sampr\n    sf = freq / width\n    st = 1.0 / (2.0 * np.pi * sf)\n    t = np.arange(-3.5 * st, 3.5 * st, dt)\n    a = 1.0 / (st * np.sqrt(2.0 * np.pi))\n    return a * np.exp(-(t ** 2.0) / (2.0 * st ** 2.0)) * np.exp(1.0j * 2.0 * np.pi * freq * t)\n\n\ndef morlet_vec(sig, sampr, freq, width=7.0):\n    # netpyne/support/morlet.py (NetPyNE 1.0.5), MorletVec()\n    m = morlet(sampr, freq, width)\n    y = sps.fftconvolve(sig, m)\n    y = (2.0 * abs(y) / sampr) ** 2.0\n    i_lower = int(np.ceil(len(m) / 2.0))\n    i_upper = int(len(y) - np.floor(len(m) / 2.0) + 1)\n    return y[i_lower:i_upper]\n\n\ndef morlet_spec(x: np.ndarray, fs: float, fmin=1, fmax=100, step=1, width=7.0):\n    \"\"\"Reading S1: MorletSpec of NetPyNE 1.0.5 with prepareSpectrogram's defaults.\"\"\"\n    sig = sps.detrend(x - np.mean(x))\n    f = np.arange(fmin, fmax + 1, step)\n    tfr = np.zeros((len(f), len(sig)))\n    for j, fr in enumerate(f):\n        tfr[j, :] = morlet_vec(sig, fs, fr, width)[: len(sig)]\n    t = np.arange(len(sig)) / fs\n    return f.astype(float), t, tfr\n\n\ndef stft_spec(x: np.ndarray, fs: float, win_s=0.25, overlap=0.9):\n    \"\"\"Reading S2: Hann-window spectrogram (standard choice; see module docstring).\"\"\"\n    n = int(win_s * fs)\n    f, t, s = sps.spectrogram(x - np.mean(x), fs=fs, window=\"hann\", nperseg=n,\n                              noverlap=int(n * overlap), mode=\"psd\")\n    sel = f <= 100\n    return f[sel], t, s[sel]\n\n\ndef band_power(f, tfr, band):\n    sel = (f >= band[0]) & (f <= band[1])\n    return tfr[sel].mean(axis=0)\n\n\ndef above_runs(x: np.ndarray, thr: float) -> list[tuple[int, int]]:\n    \"\"\"Index runs [start, stop) where x > thr.\"\"\"\n    on = np.r_[False, x > thr, False].astype(int)\n    d = np.diff(on)\n    return list(zip(np.flatnonzero(d == 1), np.flatnonzero(d == -1)))\n\n\ndef band_bursts(t: np.ndarray, power: np.ndarray, dt: float) -> dict:\n    \"\"\"Bursts as epochs above halfway between min and max of band power over the window.\"\"\"\n    thr = (power.min() + power.max()) / 2\n    runs = above_runs(power, thr)\n    dur = np.array([(b - a) * dt for a, b in runs])\n    span = len(power) * dt\n    return {\"n\": len(runs), \"rate\": len(runs) / span, \"durations\": dur,\n            \"median_ms\": float(np.median(dur) * 1e3) if len(dur) else np.nan,\n            \"frac_above\": float(np.mean(power > thr))}\n\n\n# ---------------------------------------------------------------- PT5B patterns\n\ndef cv_isi(trains: list[np.ndarray], min_isi: int) -> np.ndarray:\n    out = []\n    for t in trains:\n        isi = np.diff(t)\n        if len(isi) >= min_isi:\n            out.append(np.std(isi) / np.mean(isi))\n    return np.array(out)\n\n\ndef duty_cycles(counts: np.ndarray, local: bool) -> dict:\n    \"\"\"Duty cycles of a spike count histogram.\n\n    Periods run from one rising crossing of the global half-height (halfway between the\n    histogram's minimum and maximum) to the next. With `local`, the half-height is recomputed\n    within each period from its own trough and peak. Returns the mean of per-period duty cycles\n    (x) and the total time above over total time of complete periods (y).\n    \"\"\"\n    thr = (counts.min() + counts.max()) / 2\n    above = counts > thr\n    rises = np.flatnonzero(~above[:-1] & above[1:]) + 1\n    per, on_total, len_total = [], 0, 0\n    for a, b in zip(rises[:-1], rises[1:]):\n        seg = counts[a:b]\n        th = (seg.min() + seg.max()) / 2 if local else thr\n        on = np.count_nonzero(seg > th)\n        per.append(on / len(seg))\n        on_total += on\n        len_total += len(seg)\n    per = np.array(per)\n    return {\"n_periods\": len(per), \"mean\": float(per.mean() * 100) if len(per) else np.nan,\n            \"total\": float(on_total / len_total * 100) if len_total else np.nan,\n            \"threshold\": thr, \"median_period_ms\": float(np.median(np.diff(rises)) * SCH_BIN * 1e3)\n            if len(rises) > 1 else np.nan}\n\n\ndef coincident_fraction(d: dict, pop: str, window, reading: str) -> tuple[float, int]:\n    \"\"\"Share of `pop` spikes in `window` coincident with a spike of another cell of `pop`.\n\n    (a) another cell fires within 1 ms either side; (b) another cell fires in the same 1 ms bin\n    (bins aligned to the window start).\n    \"\"\"\n    ts, ids = [], []\n    for g, t in d[\"trains\"].items():\n        if d[\"pop\"][g] == pop:\n            t = t[(t >= window[0]) & (t < window[1])]\n            ts.append(t)\n            ids.append(np.full(len(t), g))\n    t = np.concatenate(ts)\n    g = np.concatenate(ids)\n    o = np.argsort(t, kind=\"stable\")\n    t, g = t[o], g[o]\n    n = len(t)\n    if reading == \"a\":\n        coinc = np.zeros(n, bool)\n        lo = np.searchsorted(t, t - 0.001, side=\"left\")\n        hi = np.searchsorted(t, t + 0.001, side=\"right\")\n        for i in range(n):\n            if hi[i] - lo[i] > 1 and np.any(g[lo[i]:hi[i]] != g[i]):\n                coinc[i] = True\n    else:\n        b = np.floor((t - window[0]) / 0.001).astype(int)\n        # a spike is coincident when its bin holds a spike of another cell\n        coinc = np.zeros(n, bool)\n        starts = np.r_[0, np.flatnonzero(np.diff(b)) + 1]\n        stops = np.r_[starts[1:], n]\n        for a, c in zip(starts, stops):\n            if c - a > 1 and len(np.unique(g[a:c])) > 1:\n                coinc[a:c] = True\n    return float(coinc.mean() * 100), n\n\n\ndef unitary_events(d: dict, pop: str, span, step_s: float, win_s=0.1, bin_s=0.001,\n                   alpha=0.05) -> dict:\n    \"\"\"Population coincidences (bins of `bin_s` holding 2 or more spikes of distinct cells) in\n    windows of `win_s` moved by `step_s`; expected count from independent Poisson cells at each\n    cell's rate in the window; joint-surprise p = P(N >= observed | expected). Returns the\n    significant windows' union (total duration and clusters).\"\"\"\n    edges = np.arange(span[0], span[1] + bin_s / 2, bin_s)\n    nb = len(edges) - 1\n    cells = [t[(t >= span[0]) & (t < span[1])] for g, t in d[\"trains\"].items() if d[\"pop\"][g] == pop]\n    # per-bin count of distinct cells firing\n    occ = np.zeros(nb)\n    per_cell_counts = []\n    for t in cells:\n        c, _ = np.histogram(t, edges)\n        occ += c > 0\n        per_cell_counts.append(c)\n    coinc = occ >= 2\n    C = np.array(per_cell_counts)  # cells x bins\n    w = int(round(win_s / bin_s))\n    s = int(round(step_s / bin_s))\n    sig = np.zeros(nb, bool)\n    starts = np.arange(0, nb - w + 1, s)\n    pvals, obs_all, exp_all = [], [], []\n    cs = np.cumsum(np.c_[np.zeros((C.shape[0], 1)), C], axis=1)\n    cco = np.r_[0, np.cumsum(coinc)]\n    for a in starts:\n        lam = (cs[:, a + w] - cs[:, a]) / w          # spikes per bin, per cell\n        p1 = np.clip(lam, 0, 1)\n        # probability that 2 or more distinct cells fire in a bin\n        log0 = np.sum(np.log1p(-p1[p1 < 1]))\n        p0 = np.exp(log0)\n        p1sum = p0 * np.sum(p1[p1 < 1] / (1 - p1[p1 < 1]))\n        pc = max(0.0, 1 - p0 - p1sum)\n        expct = pc * w\n        obs = cco[a + w] - cco[a]\n        p = stats.poisson.sf(obs - 1, expct) if expct > 0 else (0.0 if obs > 0 else 1.0)\n        pvals.append(p)\n        obs_all.append(obs)\n        exp_all.append(expct)\n        if p < alpha:\n            sig[a:a + w] = True\n    runs = above_runs(sig.astype(float), 0.5)\n    dur = np.array([(b - a) * bin_s for a, b in runs])\n    return {\"total_s\": float(sig.sum() * bin_s), \"clusters_ms\": dur * 1e3, \"runs\": runs,\n            \"n_windows\": len(starts), \"n_sig_windows\": int(np.sum(np.array(pvals) < alpha)),\n            \"obs\": np.array(obs_all), \"exp\": np.array(exp_all), \"sig\": sig, \"edges\": edges,\n            \"coinc_share_bins\": float(coinc.mean())}\n\n\ndef periodicity(spikes: np.ndarray, runs, span, bin_s=SCH_BIN, reading=\"x\", fmin=5.0) -> list:\n    \"\"\"Periodicity of the PT5B SCH within each significant period (index runs in 1 ms bins).\n\n    (x) the frequency of the largest peak of the periodogram of the SCH within the period,\n    above `fmin`; (y) the inverse of the mean interval between SCH peaks (scipy find_peaks on the\n    SCH, peaks at least 20 ms apart, a standard choice).\"\"\"\n    out = []\n    for a, b in runs:\n        t0, t1 = span[0] + a * 0.001, span[0] + b * 0.001\n        if t1 - t0 < 0.05:\n            continue\n        _, c = sch(spikes, (t0, t1), bin_s)\n        if reading == \"x\":\n            n = max(len(c), int(1.0 / bin_s))  # zero-pad to 1 Hz steps\n            f = np.fft.rfftfreq(n, bin_s)\n            p = np.abs(np.fft.rfft(c - c.mean(), n)) ** 2\n            sel = (f > fmin) & (f <= 100)\n            out.append(float(f[sel][np.argmax(p[sel])]))\n        else:\n            pk, _ = sps.find_peaks(c, distance=int(0.02 / bin_s))\n            if len(pk) > 1:\n                out.append(float(1.0 / (np.mean(np.diff(pk)) * bin_s)))\n    return out\n"
}
```

```
File created successfully at: entries/001444-doherty-2025/m1sim.py (file state is current in your context — no need to Read it back)
```

**Agent**

Now an exploratory run on the paper's set to see the main numbers.

**Agent calls Bash**

```bash
cd entries/001444-doherty-2025 && . $TMPDIR/venv/bin/activate && cat > $TMPDIR/explore.py <<'EOF'
import time, numpy as np, m1sim as m
t=time.time()
D={c:m.load_file(m.PAPER_SET,c) for c in m.CONDITIONS}
print('load', time.time()-t)
blocks=m.population_blocks([d['pop'] for d in D.values()])
for p,b in blocks.items(): print(p,b)
for c,d in D.items():
    print(c, d['description'], d['session_id'], 'vm gids', d['vm_gids'][:6], 'unsorted', d['unsorted'], d['obs_intervals'])
    for pop in ['IT2','IT4','IT5A','IT5B','PT5B','IT6','CT6','PV5B','SOM2']:
        r=m.rates(d,pop,blocks); r1=r['R1']; r2=r1[r['R2_mask']]
        print(f'   {pop}: R1 {m.summary(r1)}  R2 {m.summary(r2)}')
    s=m.pop_spikes(d,'PT5B'); tt,cnt=m.sch(s)
    print('   SCH peak >0', m.welch_peak(cnt,500)[0], '>5', m.welch_peak(cnt,500,5)[0])
    x=d['lfp'][int(2.0*m.FS):]
    print('   LFP peak >0', m.welch_peak(x,m.FS)[0], '>5', m.welch_peak(x,m.FS,5)[0], 'lfp range', x.min(), x.max())
EOF
python $TMPDIR/explore.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/explore.py", line 1, in <module>
    import time, numpy as np, m1sim as m
ModuleNotFoundError: No module named 'm1sim'
```

**Agent calls Bash**

```bash
cd entries/001444-doherty-2025 && . $TMPDIR/venv/bin/activate && PYTHONPATH=. python $TMPDIR/explore.py
```

```
load 12.372761726379395
IT2 (0, 2, 1729, 1729, 1728, 1730)
SOM2 (1730, 1730, 1856, 1856, 127, 127)
PV2 (1857, 1857, 2112, 2121, 256, 265)
IT4 (2113, 2122, 2879, 2885, 758, 773)
IT5A (2880, 2886, 3517, 3524, 632, 645)
SOM5A (3518, 3525, 3580, 3580, 56, 63)
PV5A (3581, 3581, 3693, 3694, 113, 114)
IT5B (3694, 3695, 5129, 5129, 1435, 1436)
PT5B (5130, 5130, 6564, 6564, 1435, 1435)
SOM5B (6565, 6565, 6815, 6815, 251, 251)
PV5B (6816, 6816, 7326, 7326, 511, 511)
IT6 (7327, 7327, 8562, 8570, 1236, 1244)
CT6 (8563, 8571, 9766, 9798, 1196, 1236)
SOM6 (9767, 9799, 9888, 9904, 90, 138)
PV6 (9889, 9905, 10064, 10072, 160, 184)
01 control, quiet wakefulness sM1_12-12-2023_01 vm gids [5201, 5202, 5301, 5302, 5401, 5402] unsorted 0 [[0.  4.3]]
   IT2: R1 (0.09525006282985675, 0.5652135729178097, 1730)  R2 (1.554552912223134, 1.7234783373420262, 106)
   IT4: R1 (0.036559986500928066, 0.6238762647231857, 773)  R2 (3.140096618357488, 5.157160390915388, 9)
   IT5A: R1 (1.2059319177620493, 2.8792824744057706, 645)  R2 (3.568009573195054, 4.017041287796344, 218)
[... 44 more lines not kept]
```

**Agent**

PT5B rates under R1 match the paper to the decimal (11.69±9.40, 14.24±7.13, 26.76±18.17, 29.68±12.67). The IT populations are off under both readings. Checking NetPyNE's own rate statistic.

**Agent calls Bash**

```bash
cd $TMPDIR/nd/src/netpyne; grep -rn "includeRate0\|def plotSpikeStats" analysis/*.py plotting/*.py | head; grep -n "def plotSpikeStats" -A 140 analysis/spikes.py | grep -n "rate\|Rate0\|timeRange\|cellGids\|isicv\|ISI\|len(spkt" | head -50
```

```
analysis/interactive.py:3105:    includeRate0=False,
analysis/interactive.py:3171:    includeRate0 : bool
analysis/interactive.py:3172:        <Short description of includeRate0>
analysis/interactive.py:3334:                    if includeRate0:
analysis/spikes_legacy.py:1221:def plotSpikeStats(
analysis/spikes_legacy.py:1232:    includeRate0=False,
analysis/spikes_legacy.py:1311:    includeRate0 : bool
analysis/spikes_legacy.py:1488:                    if includeRate0:
analysis/spikes_legacy.py:1500:                    if includeRate0:
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/nd/src/netpyne; sed -n 1440,1560p analysis/spikes_legacy.py
```

```
spkinds, spkts = list(
                            zip(
                                *[
                                    (spkgid, spkt)
                                    for spkgid, spkt in zip(sim.allSimData['spkid'], sim.allSimData['spkt'])
                                    if spkgid in cellGids
                                ]
                            )
                        )
                    except:
                        spkinds, spkts = [], []
                else:
                    spkinds, spkts = [], []

                # Add NetStim spikes
                spkts, spkinds = list(spkts), list(spkinds)
                numNetStims = 0
                if 'stims' in sim.allSimData:
                    for netStimLabel in netStimLabels:
                        netStimSpks = [
[... 102 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001444-doherty-2025 && . $TMPDIR/venv/bin/activate && cat > $TMPDIR/explore2.py <<'EOF'
import time, numpy as np, m1sim as m
D={c:m.load_file(m.PAPER_SET,c, vm=False) for c in m.CONDITIONS}
for c,d in D.items():
    pt=[t for g,t in d['trains'].items() if d['pop'][g]=='PT5B']
    for wname,w in [('W',m.WINDOW),('all',(0,4.3))]:
        tr=[t[(t>=w[0])&(t<w[1])] for t in pt]
        for mi in [2,1,11]:
            cv=m.cv_isi(tr,mi); print(c,'CV',wname,'min isi',mi, round(cv.mean(),3), round(cv.std(ddof=1),3), round(100*np.mean(cv<=0.5),1), len(cv))
    s=m.pop_spikes(d,'PT5B')
    for wname,w in [('250ms',(2.0,2.25)),('W',m.WINDOW)]:
        _,cnt=m.sch(s,w)
        for loc in [False,True]:
            r=m.duty_cycles(cnt,loc); print(c,'duty',wname,'local' if loc else 'global', {k:(round(v,2) if isinstance(v,float) else v) for k,v in r.items()})
    for rd in 'ab':
        for wn,w in [('W',m.WINDOW),('0.3-4.3',(0.3,4.3)),('0-4',(0,4.0))]:
            print(c,'coinc',rd,wn, m.coincident_fraction(d,'PT5B',w,rd))
EOF
PYTHONPATH=. python $TMPDIR/explore2.py
```

```
01 CV W min isi 2 0.611 0.354 45.9 1221
01 CV W min isi 1 0.59 0.365 47.8 1265
01 CV W min isi 11 0.55 0.335 55.0 951
01 CV all min isi 2 0.797 0.48 37.0 1420
01 CV all min isi 1 0.788 0.485 37.7 1435
01 CV all min isi 11 0.739 0.451 41.2 1162
01 duty 250ms global {'n_periods': 7, 'mean': 37.53, 'total': 27.88, 'threshold': np.float64(41.5), 'median_period_ms': 34.0}
01 duty 250ms local {'n_periods': 7, 'mean': 41.49, 'total': 36.54, 'threshold': np.float64(41.5), 'median_period_ms': 34.0}
01 duty W global {'n_periods': 101, 'mean': 40.57, 'total': 24.09, 'threshold': np.float64(41.5), 'median_period_ms': 10.0}
01 duty W local {'n_periods': 101, 'mean': 45.5, 'total': 39.61, 'threshold': np.float64(41.5), 'median_period_ms': 10.0}
01 coinc a W (100.0, 38590)
01 coinc a 0.3-4.3 (100.0, 66392)
01 coinc a 0-4 (99.99565601424827, 69061)
01 coinc b W (100.0, 38590)
01 coinc b 0.3-4.3 (100.0, 66392)
01 coinc b 0-4 (99.99276002374712, 69061)
02 CV W min isi 2 0.343 0.267 80.4 1342
02 CV W min isi 1 0.339 0.267 80.6 1357
02 CV W min isi 11 0.308 0.226 85.2 1243
02 CV all min isi 2 0.483 0.389 66.5 1431
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/venv/bin/activate && cat > $TMPDIR/explore3.py <<'EOF'
import time, numpy as np, m1sim as m
D={c:m.load_file(m.PAPER_SET,c, vm=False) for c in m.CONDITIONS}
for c,d in D.items():
    x=d['lfp'][int(2.0*m.FS):int(4.3*m.FS)]
    t=time.time(); f,tt,S1=m.morlet_spec(x,m.FS); print('morlet time', time.time()-t, S1.shape)
    f2,t2,S2=m.stft_spec(x,m.FS)
    for name,(ff,ts,S,dt) in {'S1':(f,tt,S1,1/m.FS),'S2':(f2,t2,S2,t2[1]-t2[0])}.items():
        tm=S.mean(axis=1)
        loc=[ff[i] for i in range(1,len(ff)-1) if tm[i]>tm[i-1] and tm[i]>tm[i+1] and 1<=ff[i]<=3]
        print(c,name,'2Hz local max', loc, 'peak', ff[np.argmax(tm)], 'p15', tm[np.argmin(abs(ff-15))], 'p14-16', m.band_power(ff,S,(14,16)).mean(), 'p15-20', m.band_power(ff,S,(15,20)).mean(), 'p20-35', m.band_power(ff,S,(20,35)).mean())
        for band in [(15,25),(14,16),(25,35),(20,35)]:
            b=m.band_bursts(ts,m.band_power(ff,S,band),dt)
            print('    ',band, 'n',b['n'],'rate',round(b['rate'],2),'median ms',round(b['median_ms'],1),'range', np.round(b['durations'].min()*1e3) if b['n'] else None, np.round(b['durations'].max()*1e3) if b['n'] else None,'frac',round(b['frac_above'],2))
    for step in [0.001, 0.1]:
        for span in [(0.3,4.3),(0,4.0)]:
            t=time.time(); u=m.unitary_events(d,'PT5B',span,step)
            print(c,'UE step',step,span,'total',u['total_s'],'clusters',len(u['clusters_ms']), 'sigwin',u['n_sig_windows'],'/',u['n_windows'], 'obs/exp median', np.median(u['obs']), np.median(u['exp']), 'coinc bins', round(u['coinc_share_bins'],3), round(time.time()-t,1),'s')
EOF
PYTHONPATH=. python $TMPDIR/explore3.py
```

```
morlet time 0.5955286026000977 (100, 92000)
01 S1 2Hz local max [] peak 1.0 p15 8.046411379856546e-06 p14-16 8.249784691118976e-06 p15-20 1.3748586555753019e-05 p20-35 7.97338279827819e-06
     (15, 25) n 3 rate 1.3 median ms 122.6 range 67.0 151.0 frac 0.15
     (14, 16) n 5 rate 2.17 median ms 90.1 range 33.0 163.0 frac 0.22
     (25, 35) n 4 rate 1.74 median ms 59.6 range 22.0 69.0 frac 0.09
     (20, 35) n 4 rate 1.74 median ms 61.1 range 48.0 144.0 frac 0.14
01 S2 2Hz local max [] peak 4.0 p15 1.3246668130102626e-06 p14-16 1.3246668130102626e-06 p15-20 1.3565946939780706e-06 p20-35 7.025459126230452e-07
     (15, 25) n 2 rate 0.96 median ms 150.0 range 125.0 175.0 frac 0.14
     (14, 16) n 3 rate 1.45 median ms 75.0 range 25.0 125.0 frac 0.11
     (25, 35) n 4 rate 1.93 median ms 75.0 range 50.0 175.0 frac 0.18
     (20, 35) n 2 rate 0.96 median ms 162.5 range 100.0 225.0 frac 0.16
01 UE step 0.001 (0.3, 4.3) total 0.0 clusters 0 sigwin 0 / 3901 obs/exp median 100.0 99.99985784521921 coinc bins 1.0 0.6 s
01 UE step 0.001 (0, 4.0) total 0.0 clusters 0 sigwin 0 / 3901 obs/exp median 100.0 99.99988207270266 coinc bins 0.965 0.6 s
01 UE step 0.1 (0.3, 4.3) total 0.0 clusters 0 sigwin 0 / 40 obs/exp median 100.0 99.99984815832543 coinc bins 1.0 0.1 s
01 UE step 0.1 (0, 4.0) total 0.0 clusters 0 sigwin 0 / 40 obs/exp median 100.0 99.9998727699295 coinc bins 0.965 0.2 s
morlet time 0.5622804164886475 (100, 92000)
02 S1 2Hz local max [np.float64(2.0)] peak 15.0 p15 0.0010380260532136018 p14-16 0.0009154362363536418 p15-20 0.0004829731037342477 p20-35 4.226806000159217e-05
     (15, 25) n 6 rate 2.61 median ms 158.8 range 109.0 372.0 frac 0.52
     (14, 16) n 3 rate 1.3 median ms 678.2 range 311.0 913.0 frac 0.83
     (25, 35) n 4 rate 1.74 median ms 83.6 range 42.0 160.0 frac 0.16
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 334,425p tools/entry.py; date -u
```

```
def lock(entry_dir: Path) -> int:
    r = subprocess.run(["uv", "pip", "compile", "--quiet", "--python-version", PYTHON_VERSION,
                        "requirements.in", "-o", "requirements.lock.txt"], cwd=entry_dir)
    if r.returncode == 0:
        print(f"wrote {(entry_dir / 'requirements.lock.txt').relative_to(ROOT)}")
    return r.returncode


def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float) -> int:
    entry = yaml.safe_load((entry_dir / "entry.yaml").read_text())
    output_dir.mkdir(parents=True, exist_ok=True)
    venv = (output_dir / ".venv").resolve()
    python = venv / "bin" / "python"
    # A kernel of the entry's own environment, under a name no other kernel on the machine has, so
    # nbconvert cannot pick up some other "python3" kernel (a user's or a conda install's).
    kernel = f"registry-{entry_dir.name}"
    for cmd in (["uv", "venv", "--quiet", "--clear", "--python", PYTHON_VERSION, str(venv)],
                ["uv", "pip", "install", "--quiet", "--python", str(python),
                 "-r", str(entry_dir / "requirements.lock.txt"), *HARNESS],
                [str(python), "-m", "ipykernel", "install", "--prefix", str(venv), "--name", kernel]):
[... 73 more lines not kept]
```

**Agent**

Adding the R3 mask and a Vm spike detector to the helper.

**Agent calls Bash**

```bash
cd entries/001444-doherty-2025 && python - <<'EOF'
p='m1sim.py'; s=open(p).read()
s=s.replace('''    smallest if "min"). R2: only cells with at least one spike in the window.
    """''','''    smallest if "min"). R2: only cells with at least one spike in the window. R3 (a variant
    found in the data, not a reading of the claims file): the cells the file holds, which are
    the cells that fired at least once in the 4.3 s simulation.
    """''')
s=s.replace('''    return {"gid": gids, "R1": r, "R2_mask": r > 0}''','''    in_file = np.array([d["pop"].get(int(g)) == pop for g in gids])
    return {"gid": gids, "R1": r, "R2_mask": r > 0, "R3_mask": in_file}''')
s=s.replace('''# ---------------------------------------------------------------- spectra''','''def vm_spikes(v: np.ndarray, rate: float = FS, thr: float = 0.0) -> np.ndarray:
    """Times (s) of upward crossings of `thr` mV in a membrane potential trace."""
    up = np.flatnonzero((v[:-1] < thr) & (v[1:] >= thr)) + 1
    return up / rate


# ---------------------------------------------------------------- spectra''')
s=s.replace('''- Rate readings R1 (all cells of a population) and R2 (cells with a spike in W), and test
  readings T1 to T4: the claims file's definitions.''','''- Rate readings R1 (all cells of a population) and R2 (cells with a spike in W), and test
  readings T1 to T4: the claims file's definitions. R3 (the cells the file holds, those that
  fired at least once in the simulation) is a variant found in the data, shown beside them.''')
open(p,'w').write(s)
EOF
grep -n "R3" m1sim.py
```

```
24:  readings T1 to T4: the claims file's definitions. R3 (the cells the file holds, those that
181:    smallest if "min"). R2: only cells with at least one spike in the window. R3 (a variant
195:    return {"gid": gids, "R1": r, "R2_mask": r > 0, "R3_mask": in_file}
```

**Agent calls Bash**

```bash
cd  sed -n 300,334p tools/entry.py; grep -n "HARNESS\|PYTHON_VERSION =" tools/entry.py | head
```

```
if outcome.get("claim") not in known:
                report.error(path.relative_to(ROOT), f"claim {outcome.get('claim')!r} is not in the claims file")
            notebook = outcome.get("notebook")
            if notebook and notebook not in listed:
                report.error(path.relative_to(ROOT), f"notebook {notebook!r} is not in the entry")
            tag = outcome.get("output")
            if notebook in present and tag:
                nb = nbformat.read(entry_dir / notebook, as_version=4)
                if not any(tag in c.metadata.get("tags", []) for c in nb.cells):
                    report.error(path.relative_to(ROOT), f"no cell tagged {tag!r} in {notebook}")
    return report


def _local_data(code: str, start: int) -> bool:
    """Whether a local path in the code is inside the dataset directory `encore check` gave (ENCORE_LOCAL_DATA):
    the one local path an entry on a local dataset may name."""
    allowed = os.environ.get("ENCORE_LOCAL_DATA", "").rstrip("/")
    return bool(allowed) and code.startswith(allowed, start) and code[start + len(allowed):start + len(allowed) + 1] in ("/", "'", '"')


[... 19 more lines not kept]
```

**Agent**

Writing the notebook builder.

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build_nb.py",
 "content": "import nbformat as nbf\nimport sys\n\ncells = []\n\n\ndef md(s, tags=None):\n    c = nbf.v4.new_markdown_cell(s.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\ndef code(s, tags=None):\n    c = nbf.v4.new_code_cell(s.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\ndef result(cid):\n    md(CONCL.get(cid, \"**Result: to be written.**\"))\n\n\nCONCL = {}\nexec(open(sys.argv[2]).read()) if len(sys.argv) > 2 else None\n\nmd(open(sys.argv[3]).read() if len(sys.argv) > 3 else \"# header\")\n\ncode(r'''\nimport time\nimport warnings\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nimport requests\n\nimport m1sim as m\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 30)\npd.set_option(\"display.max_rows\", 200)\n\nstarted = time.time()\nD = {c: m.load_file(m.PAPER_SET, c) for c in m.CONDITIONS}\nOTHER = {(s, c): m.load_file(s, c, vm=False) for s in m.SETS[1:] for c in m.CONDITIONS}\nprint(f\"loaded {len(D) + len(OTHER)} files of dandiset {m.DANDISET_ID} version {m.DANDISET_VERSION} \"\n      f\"in {time.time() - started:.0f} s\")\nBLOCKS = m.population_blocks([d[\"pop\"] for d in list(D.values()) + list(OTHER.values())])\n''')\n\nmd(r'''\n## Data check\n\nEach check of the description against the values is stated under its output. The archive's\ndescription of the dandiset says each file holds \"a local field potential trace, spike train data\nfrom all 10,073 neurons, and membrane potential traces from 400 of the layer 5B pyramidal tract\n(PT5B) neurons\", and that simulations last 4.3 s.\n''')\n\ncode(r'''\nA = m.assets()\nlisting = pd.DataFrame([{\"path\": p, \"size_MB\": round(v[2] / 1e6, 1), \"blob\": v[1]} for p, v in sorted(A.items())])\nprint(listing.to_string(index=False))\ndup = listing[listing.duplicated(\"blob\", keep=False)]\nprint(\"\\nAssets sharing one blob (byte-identical files):\")\nprint(dup.to_string(index=False))\ndraft = requests.get(f\"{m.API}/dandisets/{m.DANDISET_ID}/versions/draft/assets/\", params={\"page_size\": 200}).json()[\"results\"]\nsame = sorted((a[\"path\"], a[\"blob\"]) for a in draft) == sorted((p, v[1]) for p, v in A.items())\nprint(\"\\nDraft holds the same paths and blobs as the pinned version:\", same)\nversions = requests.get(f\"{m.API}/dandisets/{m.DANDISET_ID}/versions/\").json()[\"results\"]\nprint(\"Versions on the archive:\", [v[\"version\"] for v in versions])\nmeta = requests.get(f\"{m.API}/dandisets/{m.DANDISET_ID}/versions/{m.DANDISET_VERSION}/\").json()\nprint(\"relatedResource:\", meta.get(\"relatedResource\"))\nprint(\"assetsSummary measurementTechnique:\", [t[\"name\"] for t in meta[\"assetsSummary\"].get(\"measurementTechnique\", [])])\n''', [\"sanity\"])\n\nmd(r'''\nThe version holds 17 assets: four sets of four simulations, named by set and number, and\n`sub-001/sub-001.nwb`, which is the same blob as `sub-001_ses-sM1-04-22-2024-01.nwb` (a recording\ndeposited twice; it is counted once and not read again). The archive lists no related resource,\nand its summary gives \"spike sorting technique\" as the measurement technique of a simulation.\n''')\n\ncode(r'''\nrows = []\nfor (s, c), d in [((m.PAPER_SET, c), d) for c, d in D.items()] + list(OTHER.items()):\n    m1 = [g for g in d[\"pop\"] if g < m.FIRST_INPUT_GID]\n    rows.append({\"set\": s, \"file\": c, \"session_id\": d[\"session_id\"], \"description\": d[\"description\"],\n                 \"start\": d[\"start\"][:19], \"units\": len(d[\"pop\"]), \"M1 units\": len(m1),\n                 \"input units\": len(d[\"pop\"]) - len(m1),\n                 \"spikes\": sum(len(t) for t in d[\"trains\"].values()),\n                 \"first spike\": min(t[0] for t in d[\"trains\"].values() if len(t)),\n                 \"last spike\": max(t[-1] for t in d[\"trains\"].values() if len(t)),\n                 \"silent units\": sum(len(t) == 0 for t in d[\"trains\"].values()),\n                 \"unsorted trains\": d[\"unsorted\"], \"obs_intervals\": d[\"obs_intervals\"].tolist(),\n                 \"Vm traces\": len(d[\"vm_gids\"]), \"LFP samples\": len(d[\"lfp\"]), \"LFP Hz\": d[\"lfp_rate\"],\n                 \"LFP unit\": d[\"lfp_unit\"]})\ninfo = pd.DataFrame(rows)\nprint(info.drop(columns=[\"obs_intervals\"]).to_string(index=False))\nprint(\"\\nobs_intervals in every file:\", {str(x) for x in info.obs_intervals})\nprint(\"Expected order of the numbered files (claims file): \", m.CONDITIONS)\n''', [\"sanity\"])\n\nmd(r'''\nThe session descriptions confirm the numbering of the claims file: -01 control rest (\"quiet\nwakefulness\"), -02 parkinsonian rest, -03 control activated (\"movement\"), -04 parkinsonian\nactivated, in every set. Spike times run from 0 to 4.3 s and are in seconds; no unit has zero\nspikes, and every train is sorted. The LFP has 172,000 samples at 40 kHz, 4.3 s. The files of the\npaper's set (sM1-12-12-2023) hold 20 PT5B membrane potentials, not 400 as the description says;\nthe other sets hold 400. Each file holds one LFP trace, \"LFP 0\", where the model records 11\nelectrodes (claims file, cfg.recordLFP); no file says at which depth it was taken.\n''')\n\ncode(r'''\nprint(\"Units in the paper's set, by population (M1 populations, then inputs):\")\npops = sorted({p for d in D.values() for p in d[\"pop\"].values()},\n              key=lambda p: min(g for d in D.values() for g, q in d[\"pop\"].items() if q == p))\ntab = pd.DataFrame({m.CONDITIONS[c]: pd.Series(list(d[\"pop\"].values())).value_counts() for c, d in D.items()}).reindex(pops).fillna(0).astype(int)\nprint(tab.to_string())\nprint(\"\\nM1 units per file:\", {c: int(tab.loc[m.M1_POPS, m.CONDITIONS[c]].sum()) for c in D})\nprint(\"Lowest input gid:\", min(g for d in D.values() for g in d[\"pop\"] if g >= m.FIRST_INPUT_GID),\n      \"; highest M1 gid:\", max(g for d in D.values() for g in d[\"pop\"] if g < m.FIRST_INPUT_GID))\nprint(\"\\nPopulation gid blocks bounded from the gids seen in all 16 files \"\n      \"(start in [low, high], end in [low, high], size min and max):\")\nbl = pd.DataFrame(BLOCKS, index=[\"start_low\", \"start_high\", \"end_low\", \"end_high\", \"n_min\", \"n_max\"]).T\nprint(bl.to_string())\nprint(\"Sum of the largest sizes:\", int(bl.n_max.sum()), \"; the blocks overlap nowhere:\",\n      all(BLOCKS[a][3] < BLOCKS[b][0] for a, b in zip(m.M1_POPS, m.M1_POPS[1:])))\nsame_map = all(D[c][\"pop\"].get(g, p) == p for c in D for g, p in D[\"01\"][\"pop\"].items())\nprint(\"A gid has the same population in all four files of the set:\", same_map)\n''', [\"sanity\"])\n\nmd(r'''\nThe units table holds only cells that fired: 2,917 to 4,480 M1 units per file of the paper's set,\nnot 10,073, and input generators that did not fire are missing too (fewer than 1,000 per input\nregion). The cell names carry NetPyNE's gids, numbered in one block per population; the inputs\nstart at gid 10073, so the M1 cells are gids 0 to 10072, which is consistent with 10,073 cells.\nThe size of each population is bounded from the gids seen in any of the 16 files; for the\npopulations the claims use the bounds differ by at most 15 cells (IT4, IT5A, IT6), and both are\nshown below where it matters. PT5B has 1,435 cells and all fired in every file.\n''')\n\ncode(r'''\n# Clock and labels: spikes detected in each membrane potential trace against the spike times of\n# the unit with the same gid.\nrows = []\nfor c, d in D.items():\n    for g in d[\"vm_gids\"]:\n        v = d[\"vm\"][g]\n        sv = m.vm_spikes(v)\n        su = d[\"trains\"].get(g, np.array([]))\n        n = min(len(sv), len(su))\n        lag = (su[:n] - sv[:n]) * 1e3 if n else np.array([np.nan])\n        rows.append({\"file\": c, \"gid\": g, \"pop\": d[\"pop\"].get(g), \"Vm spikes\": len(sv), \"unit spikes\": len(su),\n                     \"median lag ms\": np.median(lag), \"max |lag| ms\": np.max(np.abs(lag)),\n                     \"Vm min\": v.min(), \"Vm max\": v.max()})\nvmchk = pd.DataFrame(rows)\nprint(vmchk.groupby(\"file\").agg(traces=(\"gid\", \"size\"), all_PT5B=(\"pop\", lambda s: bool((s == \"PT5B\").all())),\n      same_count=(\"Vm spikes\", lambda s: int((s.values == vmchk.loc[s.index, \"unit spikes\"].values).sum())),\n      median_lag_ms=(\"median lag ms\", \"median\"), max_abs_lag_ms=(\"max |lag| ms\", \"max\"),\n      vm_min=(\"Vm min\", \"min\"), vm_max=(\"Vm max\", \"max\")).to_string())\nprint(\"PT5B gids with Vm, same in all four files:\", all(D[c][\"vm_gids\"] == D[\"01\"][\"vm_gids\"] for c in D),\n      D[\"01\"][\"vm_gids\"])\n''', [\"sanity\"])\n\nmd(r'''\nEvery trace belongs to a PT5B unit of the same gid, and its upward crossings of 0 mV fall on that\nunit's spike times, within the lag printed (the unit times are NetPyNE's threshold crossings), so\nthe membrane potentials and the spike times share one clock and one labelling. The potentials\nrange over the values printed, in mV.\n''')\n\ncode(r'''\n# LFP against the PT5B spike count histogram: the Results say the LFP and the PT5B SCH oscillate in\n# antiphase. Correlation at lags from -50 to 50 ms (2 ms bins) in W; a shared clock puts the\n# extreme near lag 0, and the contrast between rest (beta) and activated (gamma) shows in the lag\n# of the next opposite extreme.\nlags = np.arange(-25, 26)\nrows = []\nfor c, d in D.items():\n    _, cnt = m.sch(m.pop_spikes(d, \"PT5B\"))\n    x = d[\"lfp\"][int(m.WINDOW[0] * m.FS):int(m.WINDOW[1] * m.FS)]\n    lfp2 = x[: len(cnt) * 80].reshape(len(cnt), 80).mean(axis=1)\n    a, b = (cnt - cnt.mean()) / cnt.std(), (lfp2 - lfp2.mean()) / lfp2.std()\n    r = np.array([np.mean(a[max(0, -k):len(a) - max(0, k)] * b[max(0, k):len(b) - max(0, -k)]) for k in lags])\n    i = np.argmin(r)\n    rows.append({\"file\": m.CONDITIONS[c], \"r at lag 0\": r[25], \"most negative r\": r[i], \"its lag ms\": lags[i] * 2,\n                 \"most positive r\": r.max(), \"its lag ms \": lags[np.argmax(r)] * 2})\n    # shifted control: LFP shifted by 1 s\n    sh = np.roll(b, 500)\n    rows[-1][\"r at lag 0, LFP shifted 1 s\"] = np.mean(a * sh)\nprint(pd.DataFrame(rows).round(3).to_string(index=False))\n''', [\"sanity\"])\n\nmd(r'''\nIn every file the LFP and the PT5B SCH are most strongly anticorrelated at a lag of a few ms, and\nthe correlation is near zero when the LFP is shifted by 1 s, consistent with the antiphase the\nResults describe and with one clock for the LFP and the spikes. The lag of the opposite extreme is\nshorter in the activated files (gamma) than at rest (beta).\n''')\n\n# ---------------------------------------------------------------- helpers in the notebook\ncode(r'''\nEXP = {}   # expected values of each claim, from the claims file, as (value, tolerance)\n\ndef within(x, e):\n    return abs(x - e[0]) <= e[1] + 1e-9\n\ndef rate_rows(pop, conds):\n    \"\"\"Mean, sd and n of a population's rates in W under R1 (largest and smallest block), R2 and R3.\"\"\"\n    rows = []\n    for c in conds:\n        r = m.rates(D[c], pop, BLOCKS)\n        rmin = m.rates(D[c], pop, BLOCKS, size=\"min\")\n        for name, x in [(\"R1\", r[\"R1\"]), (\"R1 (smallest block)\", rmin[\"R1\"]), (\"R2\", r[\"R1\"][r[\"R2_mask\"]]),\n                        (\"R3 (variant)\", r[\"R1\"][r[\"R3_mask\"]])]:\n            mu, sd, n = m.summary(x)\n            rows.append({\"file\": c, \"condition\": m.CONDITIONS[c], \"pop\": pop, \"reading\": name,\n                         \"mean\": mu, \"sd\": sd, \"n\": n})\n    return pd.DataFrame(rows)\n\ndef compare(pop, c1, c2):\n    \"\"\"p-values of T1 to T4 for rates of `pop` in files c1 and c2, under R1, R2 and R3. Cells are paired\n    by gid (same network in all four files of a set); under R2 and R3 the paired tests use the cells\n    kept in both files and the unpaired tests the cells kept in each.\"\"\"\n    a, b = m.rates(D[c1], pop, BLOCKS), m.rates(D[c2], pop, BLOCKS)\n    out = []\n    for name, ka, kb in [(\"R1\", np.ones(len(a[\"R1\"]), bool), np.ones(len(b[\"R1\"]), bool)),\n                         (\"R2\", a[\"R2_mask\"], b[\"R2_mask\"]), (\"R3 (variant)\", a[\"R3_mask\"], b[\"R3_mask\"])]:\n        both = ka & kb\n        row = {\"reading\": name, \"mean 1\": a[\"R1\"][ka].mean() if ka.any() else np.nan,\n               \"mean 2\": b[\"R1\"][kb].mean() if kb.any() else np.nan, \"n paired\": int(both.sum())}\n        if both.sum() > 1:\n            p = m.tests(a[\"R1\"][both], b[\"R1\"][both])\n            row.update({k: p[k] for k in [\"T1 Wilcoxon\", \"T2 paired t\"]})\n        if ka.sum() > 1 and kb.sum() > 1:\n            p = m.tests(a[\"R1\"][ka], b[\"R1\"][kb], paired_ok=False)\n            row.update(p)\n        out.append(row)\n    return pd.DataFrame(out)\n\ndef check_rates(cid, pop, conds, keys, stat=(\"mean\", \"sd\")):\n    t = rate_rows(pop, conds)\n    print(t.round(3).to_string(index=False))\n    print()\n    for reading in [\"R1\", \"R1 (smallest block)\", \"R2\", \"R3 (variant)\"]:\n        sub = t[t.reading == reading].set_index(\"file\")\n        vals, ok = [], []\n        for (c, s), e in zip(keys, EXP[cid]):\n            v = sub.loc[c, s]\n            vals.append(round(float(v), 3))\n            ok.append(bool(within(v, e)) if np.isfinite(v) else False)\n        print(f\"{reading:22s} values {vals}  expected {[e[0] for e in EXP[cid]]}  within tolerance {ok}  all: {all(ok)}\")\n''')\n\nmd(r'''\n## Claims\n\nRates are spikes in W (2.0 to 4.3 s) over 2.3 s. Readings R1 (all cells of the population, silent\nones at 0) and R2 (cells with a spike in W) are the claims file's; R3 (the cells the file holds,\ni.e. those that fired at least once in 0 to 4.3 s) is a variant shown beside them, and does not\ndecide an outcome (see the question to a reader in the attempt record). Test readings T1 to T4 are\ntwo-sided.\n''')\n\n# ---- fig1\nmd(r'''\n### fig1-network-size\n\n> The simulated M1 network is composed of 10,073 neurons of seven excitatory pyramidal cell types\n> (IT, PT5B, CT) and two interneuron cell types (PV, SOM).\n\nCriterion: count the units of the 15 M1 populations in each file of set sM1_12-12-2023; reproduced\nwhen the count is 10,073 in each.\n''')\ncode(r'''\ncounts = {m.CONDITIONS[c]: sum(1 for g, p in d[\"pop\"].items() if p in m.M1_POPS) for c, d in D.items()}\nprint(\"M1 units per file:\", counts, \"; expected 10073 in each:\", all(v == 10073 for v in counts.values()))\nprint(\"Variant, gid range: lowest input gid\", min(g for d in D.values() for g in d[\"pop\"] if g >= m.FIRST_INPUT_GID),\n      \"so M1 gids are 0 to\", m.FIRST_INPUT_GID - 1, \"=\", m.FIRST_INPUT_GID, \"cells; sum of block sizes\", int(bl.n_max.sum()))\nprint(\"Populations present:\", [p for p in m.M1_POPS if p in tab.index], len([p for p in m.M1_POPS if p in tab.index]))\n''', [\"claim:fig1-network-size\"])\nresult(\"fig1-network-size\")\n\n# ---- model\nmd(r'''\n### model-pt5b-excitability-decrease (blocked)\n\n> In the parkinsonian condition the PT5B neuron model was changed (BK and NaT conductances) so that\n> its spike count across current injections fell by 64%, as in 6-OHDA mouse slices.\n\nThe dandiset holds only the 16 network simulations (data check); there are no single-cell\ncurrent-injection simulations, so the claim is not tested.\n''')\ncode(r'''\nprint(\"Acquisition series in the files: LFP 0 and PT5B membrane potentials only;\",\n      \"files:\", len(A), \"; any asset outside the four sets:\", [p for p in A if \"ses-sM1\" not in p])\n''', [\"claim:model-pt5b-excitability-decrease\"])\n\n# ---- robustness\nmd(r'''\n### robustness-four-sets (blocked, measures reported)\n\n> The results hold across four sets of four simulations with different random seeds; set\n> sM1_12-12-2023 is a typical example and the other three sets are analysed in Supplementary Table 2.\n\nThe claims file gives no measures or values for this claim (Supplementary Table 2 was not\navailable), so it is blocked. As the criterion allows, the measures of the claims below are\nreported for each set, without an outcome.\n''')\ncode(r'''\nrows = []\nfor s in m.SETS:\n    for c in m.CONDITIONS:\n        d = D[c] if s == m.PAPER_SET else OTHER[(s, c)]\n        pt = [t for g, t in d[\"trains\"].items() if d[\"pop\"][g] == \"PT5B\"]\n        r = np.array([np.count_nonzero((t >= 2.0) & (t < 4.3)) / 2.3 for t in pt])\n        cv = m.cv_isi([t[(t >= 2.0) & (t < 4.3)] for t in pt], 1)\n        _, cnt = m.sch(m.pop_spikes(d, \"PT5B\"))\n        x = d[\"lfp\"][int(2.0 * m.FS):int(4.3 * m.FS)]\n        f1, t1, s1 = m.morlet_spec(x, m.FS)\n        rows.append({\"set\": s, \"cond\": m.CONDITIONS[c], \"PT5B n\": len(pt), \"PT5B rate\": r.mean(), \"sd\": r.std(ddof=1),\n                     \"CV mean\": cv.mean(), \"CV<=0.5 %\": 100 * np.mean(cv <= 0.5),\n                     \"SCH peak Hz\": m.welch_peak(cnt, 1 / m.SCH_BIN, 0)[0],\n                     \"LFP Morlet 14-16 Hz power\": m.band_power(f1, s1, (14, 16)).mean()})\nrob = pd.DataFrame(rows)\nprint(rob.round(4).to_string(index=False))\nr15 = rob.pivot(index=\"set\", columns=\"cond\", values=\"LFP Morlet 14-16 Hz power\")\nprint(\"\\nParkinsonian over control 14-16 Hz LFP power at rest, per set:\")\nprint((r15[\"parkinsonian rest\"] / r15[\"control rest\"]).round(1).to_string())\n''', [\"claim:robustness-four-sets\"])\n\n# ---- dominant frequency claims\nmd(r'''\n### Dominant frequencies: fig2-control-rest-beta, fig2-control-activated-gamma, fig5-pd-rest-beta, fig5-pd-activated-gamma\n\n> fig2-control-rest-beta: In the control condition at rest, M1 activity is dominated by beta-band\n> activity of about 20 Hz, particularly clear in the PT5B spike count histogram.\n>\n> fig2-control-activated-gamma: In the control condition, the activated state shifts M1 activity to\n> gamma-band activity of about 44 Hz.\n>\n> fig5-pd-rest-beta: In the parkinsonian condition at rest, M1 activity shows focused beta-band\n> activity at 15 Hz.\n>\n> fig5-pd-activated-gamma: In the parkinsonian condition the activated state shifts M1 activity to\n> gamma-band activity of about 43 Hz.\n\nCriterion: the frequency of the largest peak of the Welch spectrum (1 s segments) in W of the\nPT5B SCH (2 ms bins), searched above 0 Hz and above 5 Hz; the LFP is a variant. The claims file's\nelectrode readings are E1 (electrode 0) and E2 (mean of 11 electrodes); the files hold one trace,\n\"LFP 0\", taken here as E1, and E2 cannot be computed.\n''')\ncode(r'''\nEXP_PEAK = {\"01\": (20, 2), \"03\": (44, 4.4), \"02\": (15, 1.5), \"04\": (43, 4.3)}\nID = {\"01\": \"fig2-control-rest-beta\", \"03\": \"fig2-control-activated-gamma\", \"02\": \"fig5-pd-rest-beta\", \"04\": \"fig5-pd-activated-gamma\"}\nSPEC = {}\nrows = []\nfor c, d in D.items():\n    _, cnt = m.sch(m.pop_spikes(d, \"PT5B\"))\n    x = d[\"lfp\"][int(2.0 * m.FS):int(4.3 * m.FS)]\n    row = {\"claim\": ID[c], \"condition\": m.CONDITIONS[c], \"expected\": f\"{EXP_PEAK[c][0]} +/- {EXP_PEAK[c][1]}\"}\n    for lo in (0, 5):\n        pk, f, p = m.welch_peak(cnt, 1 / m.SCH_BIN, lo)\n        row[f\"SCH peak >{lo} Hz\"] = pk\n        row[f\"SCH ok >{lo}\"] = within(pk, EXP_PEAK[c])\n        SPEC[c] = (f, p)\n        pk2, f2, p2 = m.welch_peak(x, m.FS, lo)\n        row[f\"LFP E1 peak >{lo} Hz (variant)\"] = pk2\n    # the three largest local maxima of the SCH spectrum above 5 Hz, for context\n    f, p = SPEC[c]\n    sel = (f > 5) & (f <= 100)\n    fi, pi = f[sel], p[sel]\n    loc = [i for i in range(1, len(pi) - 1) if pi[i] > pi[i - 1] and pi[i] > pi[i + 1]]\n    top = sorted(loc, key=lambda i: -pi[i])[:3]\n    row[\"SCH top local maxima Hz (power ratio to largest)\"] = [(float(fi[i]), round(float(pi[i] / pi[top[0]]), 2)) for i in top]\n    rows.append(row)\npeaks = pd.DataFrame(rows)\nprint(peaks.to_string(index=False))\nfig, ax = plt.subplots(1, 4, figsize=(14, 3))\nfor k, c in enumerate(D):\n    f, p = SPEC[c]\n    ax[k].semilogy(f[(f > 0) & (f <= 100)], p[(f > 0) & (f <= 100)])\n    ax[k].set_title(m.CONDITIONS[c]); ax[k].set_xlabel(\"Hz\")\n    print(m.CONDITIONS[c], \"plotted SCH power range\", p[(f > 0) & (f <= 100)].min(), p[(f > 0) & (f <= 100)].max())\nplt.tight_layout(); plt.show()\n''', [\"claim:fig2-control-rest-beta\", \"claim:fig2-control-activated-gamma\", \"claim:fig5-pd-rest-beta\", \"claim:fig5-pd-activated-gamma\"])\nfor cid in [\"fig2-control-rest-beta\", \"fig2-control-activated-gamma\", \"fig5-pd-rest-beta\", \"fig5-pd-activated-gamma\"]:\n    result(cid)\n\n# ---- rate claims, within condition\ndef rate_claim(cid, quote, crit, pop, conds, keys, exp, cmp=None, alpha=None):\n    md(f\"### {cid}\\n\\n> {quote}\\n\\n{crit}\")\n    src = f'EXP[\"{cid}\"] = {exp}\\ncheck_rates(\"{cid}\", \"{pop}\", {conds}, {keys})\\n'\n    if cmp:\n        src += f'cmpt = compare(\"{pop}\", \"{cmp[0]}\", \"{cmp[1]}\")\\nprint()\\nprint(cmpt.to_string(index=False))\\n'\n        src += f'ps = cmpt.set_index(\"reading\")[[\"T1 Wilcoxon\", \"T2 paired t\", \"T3 Mann-Whitney\", \"T4 Welch t\"]]\\n'\n        src += f'print(\"\\\\nAll four tests below p = {alpha}, per reading:\", (ps < {alpha}).all(axis=1).to_dict())\\n'\n    code(src, [f\"claim:{cid}\"])\n    result(cid)\n\nrate_claim(\"fig2c-control-pt5b-rate-activated\",\n           \"In the control condition PT5B neurons fire more in the activated state than at rest (11.7 +/- 9.4 against 26.8 +/- 18.2 spikes/s, p < 0.001).\",\n           \"Criterion: files -01 and -03, R1 and R2; reproduced when under one rate reading all four values are within tolerance and the activated rates are higher with p < 0.001 under every test reading.\",\n           \"PT5B\", [\"01\", \"03\"], [(\"01\", \"mean\"), (\"01\", \"sd\"), (\"03\", \"mean\"), (\"03\", \"sd\")],\n           [(11.7, 1.17), (9.4, 0.94), (26.8, 2.68), (18.2, 1.82)], (\"01\", \"03\"), 0.001)\nrate_claim(\"fig2c-control-it23-rate-activated\",\n           \"In the control condition IT2/3 neurons fire more in the activated state than at rest (1.2 +/- 1.6 against 6.7 +/- 8.9 spikes/s, p < 0.001).\",\n           \"Criterion: files -01 and -03, population IT2, R1 and R2; as above, p < 0.001.\",\n           \"IT2\", [\"01\", \"03\"], [(\"01\", \"mean\"), (\"01\", \"sd\"), (\"03\", \"mean\"), (\"03\", \"sd\")],\n           [(1.2, 0.12), (1.6, 0.16), (6.7, 0.67), (8.9, 0.89)], (\"01\", \"03\"), 0.001)\nrate_claim(\"fig2c-control-it6-rate-activated\",\n           \"In the control condition IT6 neurons fire less in the activated state than at rest (5.8 +/- 5.8 against 3.5 +/- 5.2 spikes/s, p < 0.001).\",\n           \"Criterion: files -01 and -03, R1 and R2; reproduced when under one reading all four values are within tolerance and the activated rates are lower with p < 0.001 under every test.\",\n           \"IT6\", [\"01\", \"03\"], [(\"01\", \"mean\"), (\"01\", \"sd\"), (\"03\", \"mean\"), (\"03\", \"sd\")],\n           [(5.8, 0.58), (5.8, 0.58), (3.5, 0.35), (5.2, 0.52)], (\"01\", \"03\"), 0.001)\n\nmd(r'''\n### control-it5-silenced-activated\n\n> In the control condition IT5A and IT5B neurons fire at about 3 spikes/s at rest (3.3 and 3.1\n> spikes/s) and stop firing (0 spikes/s) in the activated state.\n\nCriterion: files -01 and -03, reading R1; R2 a variant where defined. Tolerance 0.05 spikes/s for\nthe zero rates.\n''')\ncode(r'''\ndef it5(cid, rest, act, exp):\n    EXP[cid] = exp\n    t = pd.concat([rate_rows(\"IT5A\", [rest, act]), rate_rows(\"IT5B\", [rest, act])])\n    print(t.round(3).to_string(index=False))\n    for reading in [\"R1\", \"R1 (smallest block)\", \"R2\", \"R3 (variant)\"]:\n        s = t[t.reading == reading].set_index([\"pop\", \"file\"])[\"mean\"]\n        vals = [s[(\"IT5A\", rest)], s[(\"IT5B\", rest)], s[(\"IT5A\", act)], s[(\"IT5B\", act)]]\n        ok = [bool(within(v, e)) if np.isfinite(v) else False for v, e in zip(vals, exp)]\n        print(f\"{reading:22s} values {np.round(vals, 3).tolist()} expected {[e[0] for e in exp]} within {ok} all: {all(ok)}\")\n    for c in (act,):\n        for p in (\"IT5A\", \"IT5B\"):\n            n = sum(1 for g, q in D[c][\"pop\"].items() if q == p)\n            sp = sum(len(t) for g, t in D[c][\"trains\"].items() if D[c][\"pop\"][g] == p)\n            last = max((t[-1] for g, t in D[c][\"trains\"].items() if D[c][\"pop\"][g] == p), default=np.nan)\n            print(f\"{m.CONDITIONS[c]}: {p} units in the file {n}, spikes in 0-4.3 s {sp}, last spike at {last:.3f} s\")\nit5(\"control-it5-silenced-activated\", \"01\", \"03\", [(3.3, 0.33), (3.1, 0.31), (0, 0.05), (0, 0.05)])\n''', [\"claim:control-it5-silenced-activated\"])\nresult(\"control-it5-silenced-activated\")\n\nrate_claim(\"control-it4-rate-activated\",\n           \"In the control condition the IT4 population rate rises from 2.6 spikes/s at rest to 4.7 spikes/s in the activated state.\",\n           \"Criterion: files -01 and -03, R1 and R2; reproduced when under one reading both means are within tolerance. The paper reports no test.\",\n           \"IT4\", [\"01\", \"03\"], [(\"01\", \"mean\"), (\"03\", \"mean\")], [(2.6, 0.26), (4.7, 0.47)])\n\nmd(r'''\n### pt5b-highest-rate\n\n> PT5B neurons have the highest mean spike rate of any population in the control rest state and in\n> both the parkinsonian rest and activated states.\n\nCriterion: files -01, -02 and -04, mean rates in W of every M1 population, population readings (a)\nall 15 and (b) the seven excitatory types; reproduced when PT5B is highest in all three under one\nrate reading and both population readings; blocked as methods_underspecified when the population\nreadings disagree.\n''')\ncode(r'''\nrows = []\nfor c in [\"01\", \"02\", \"04\"]:\n    for pop in m.M1_POPS:\n        r = m.rates(D[c], pop, BLOCKS)\n        rows.append({\"file\": c, \"pop\": pop, \"R1\": r[\"R1\"].mean(), \"R2\": r[\"R1\"][r[\"R2_mask\"]].mean() if r[\"R2_mask\"].any() else np.nan,\n                     \"R3 (variant)\": r[\"R1\"][r[\"R3_mask\"]].mean() if r[\"R3_mask\"].any() else np.nan})\nhr = pd.DataFrame(rows)\nfor reading in [\"R1\", \"R2\", \"R3 (variant)\"]:\n    piv = hr.pivot(index=\"pop\", columns=\"file\", values=reading).reindex(m.M1_POPS)\n    print(f\"\\n{reading} mean rates (spikes/s):\")\n    print(piv.round(2).T.to_string())\n    for label, popset in [(\"(a) all 15\", m.M1_POPS), (\"(b) excitatory\", m.EXCITATORY)]:\n        top = {m.CONDITIONS[c]: piv.loc[popset, c].idxmax() for c in piv.columns}\n        print(f\"  {label}: highest {top}; PT5B highest in all three: {all(v == 'PT5B' for v in top.values())}\")\n''', [\"claim:pt5b-highest-rate\"])\nresult(\"pt5b-highest-rate\")\n\n# ---- CV\nmd(r'''\n### control-cv-isi and pd-cv-isi\n\n> control-cv-isi: In the control condition PT5B interspike-interval CV is highly variable at rest\n> (0.59 +/- 0.37; 47.8% regular with CV <= 0.5, 52.2% irregular) and mainly irregular in the\n> activated state (0.61 +/- 0.30; 25.7% regular, 74.3% irregular).\n>\n> pd-cv-isi: In the parkinsonian condition PT5B spiking is mainly regular at rest (CV 0.34 +/- 0.27;\n> 80.6% with CV <= 0.5) and more regular in the activated state (CV 0.18 +/- 0.19; 93.8% regular).\n\nCriterion: CV of each PT5B cell's ISIs; mean and standard deviation over cells, share with CV <=\n0.5; readings window (a) W or (b) 0 to 4.3 s, cells (i) with at least two ISIs or (ii) at least one.\nThe ISI-CV statistic of NetPyNE 1.0.5 (plotSpikeStats, cells with more than 10 spikes in the time\nrange) is shown as a variant (iii).\n''')\ncode(r'''\nEXP[\"control-cv-isi\"] = [(0.59, 0.059), (0.37, 0.037), (47.8, 4.78), (0.61, 0.061), (0.30, 0.030), (25.7, 2.57)]\nEXP[\"pd-cv-isi\"] = [(0.34, 0.034), (0.27, 0.027), (80.6, 8.06), (0.18, 0.018), (0.19, 0.019), (93.8, 9.38)]\nCV = {}\nfor cid, (rest, act) in {\"control-cv-isi\": (\"01\", \"03\"), \"pd-cv-isi\": (\"02\", \"04\")}.items():\n    print(cid)\n    for wname, w in [(\"(a) W\", m.WINDOW), (\"(b) 0-4.3 s\", (0.0, 4.3))]:\n        for cname, k in [(\"(i) >=2 ISIs\", 2), (\"(ii) >=1 ISI\", 1), (\"(iii) >10 spikes, variant\", 10)]:\n            vals = []\n            for c in (rest, act):\n                pt = [t[(t >= w[0]) & (t < w[1])] for g, t in D[c][\"trains\"].items() if D[c][\"pop\"][g] == \"PT5B\"]\n                cv = m.cv_isi(pt, k)\n                vals += [cv.mean(), cv.std(ddof=1), 100 * np.mean(cv <= 0.5)]\n                n = len(cv)\n            ok = [bool(within(v, e)) for v, e in zip(vals, EXP[cid])]\n            CV[(cid, wname, cname)] = vals\n            print(f\"  {wname:12s} {cname:26s} {np.round(vals, 3).tolist()}  within {ok} all: {all(ok)}  (n cells activated {n})\")\n    print(\"  expected\", [e[0] for e in EXP[cid]])\n''', [\"claim:control-cv-isi\", \"claim:pd-cv-isi\"])\nresult(\"control-cv-isi\")\nresult(\"pd-cv-isi\")\n\n# ---- subthreshold\nmd(r'''\n### control-subthreshold-oscillations and pd-no-subthreshold-oscillations (blocked)\n\n> control-subthreshold-oscillations: In the control condition subthreshold membrane-potential\n> oscillations appear in 57.4% of PT5B neurons in the activated state and not at rest.\n>\n> pd-no-subthreshold-oscillations: No subthreshold membrane-potential oscillations are seen in PT5B\n> neurons in the parkinsonian rest or activated states.\n\nThe claims file finds no detection rule in the paper or its code and blocks both claims as\nmethods_underspecified; it asks for the number of PT5B cells with a recorded potential.\n''')\ncode(r'''\nfor c, d in D.items():\n    print(m.CONDITIONS[c], \": PT5B cells with a membrane potential\", len(d[\"vm_gids\"]), \"of\", BLOCKS[\"PT5B\"][5])\nprint(\"57.4% of 20 cells would be\", 0.574 * 20, \"cells; of 1435,\", round(0.574 * 1435, 1))\n''', [\"claim:control-subthreshold-oscillations\", \"claim:pd-no-subthreshold-oscillations\"])\n\n# ---- Vm\nmd(r'''\n### pd-activated-vm-more-negative\n\n> In the activated state, PT5B membrane potential is on average more negative in the parkinsonian\n> than in the control condition, which the paper gives as the reason the EPSPs look larger.\n\nCriterion: files -03 and -04, the PT5B cells recorded in both, in W; readings (a) the mean of each\ntrace and (b) its median; reproduced when the mean over cells is lower in the parkinsonian file\nunder both.\n''')\ncode(r'''\nrows = []\na, b = int(2.0 * m.FS), int(4.3 * m.FS)\nfor g in D[\"03\"][\"vm_gids\"]:\n    if g in D[\"04\"][\"vm\"]:\n        v3, v4 = D[\"03\"][\"vm\"][g][a:b], D[\"04\"][\"vm\"][g][a:b]\n        rows.append({\"gid\": g, \"ctrl mean\": v3.mean(), \"pd mean\": v4.mean(), \"ctrl median\": np.median(v3), \"pd median\": np.median(v4),\n                     \"ctrl spikes\": len(m.vm_spikes(v3)), \"pd spikes\": len(m.vm_spikes(v4))})\nvm = pd.DataFrame(rows)\nvm[\"diff mean\"] = vm[\"pd mean\"] - vm[\"ctrl mean\"]\nvm[\"diff median\"] = vm[\"pd median\"] - vm[\"ctrl median\"]\nprint(vm.round(2).to_string(index=False))\nfrom scipy import stats\nfor k in [\"mean\", \"median\"]:\n    print(f\"({'a' if k == 'mean' else 'b'}) {k}: control {vm['ctrl ' + k].mean():.2f} mV, parkinsonian {vm['pd ' + k].mean():.2f} mV, \"\n          f\"difference {vm['diff ' + k].mean():.2f} mV; cells lower in parkinsonian {(vm['diff ' + k] < 0).sum()} of {len(vm)}; \"\n          f\"Wilcoxon p = {stats.wilcoxon(vm['diff ' + k]).pvalue:.3g}\")\n''', [\"claim:pd-activated-vm-more-negative\"])\nresult(\"pd-activated-vm-more-negative\")\n\n# ---- duty cycle\nmd(r'''\n### control-duty-cycle and pd-duty-cycle\n\n> control-duty-cycle: In the control condition the PT5B duty cycle, the share of each oscillation\n> period with activity above half-height, is 31% at rest and 48% in the activated state.\n>\n> pd-duty-cycle: In the parkinsonian condition the PT5B duty cycle is 29% at rest and 25% in the\n> activated state.\n\nCriterion: PT5B SCH, 2 ms bins, unsmoothed; periods from one rising crossing of half-height to the\nnext; readings half-height (a) halfway between the minimum and maximum of the window or (b) of\neach period; window (i) 2.0 to 2.25 s or (ii) W; summary (x) mean of per-period duty cycles or (y)\ntotal time above over total time of complete periods. Reproduced when under one combination both\nvalues of a claim are within tolerance.\n''')\ncode(r'''\nEXP[\"control-duty-cycle\"] = [(31, 3.1), (48, 4.8)]\nEXP[\"pd-duty-cycle\"] = [(29, 2.9), (25, 2.5)]\nDUTY = {}\nfor cid, (rest, act) in {\"control-duty-cycle\": (\"01\", \"03\"), \"pd-duty-cycle\": (\"02\", \"04\")}.items():\n    print(cid, \"expected\", [e[0] for e in EXP[cid]])\n    for hname, local in [(\"(a) window\", False), (\"(b) period\", True)]:\n        for wname, w in [(\"(i) 2.0-2.25 s\", (2.0, 2.25)), (\"(ii) W\", m.WINDOW)]:\n            res = [m.duty_cycles(m.sch(m.pop_spikes(D[c], \"PT5B\"), w)[1], local) for c in (rest, act)]\n            for sname, key in [(\"(x) mean\", \"mean\"), (\"(y) total\", \"total\")]:\n                vals = [r[key] for r in res]\n                ok = [bool(within(v, e)) for v, e in zip(vals, EXP[cid])]\n                DUTY[(cid, hname, wname, sname)] = vals\n                print(f\"  {hname:11s} {wname:15s} {sname:10s} {np.round(vals, 2).tolist()} within {ok} both: {all(ok)}\"\n                      f\"   periods {[r['n_periods'] for r in res]}, median period ms {[r['median_period_ms'] for r in res]}\")\n''', [\"claim:control-duty-cycle\", \"claim:pd-duty-cycle\"])\nresult(\"control-duty-cycle\")\nresult(\"pd-duty-cycle\")\n\n# ---- spectrograms\nmd(r'''\n### LFP spectrograms: fig3a, fig3b, fig6a, fig6b\n\n> fig3a-control-rest-spectrogram: In the control rest state the LFP spectrogram shows virtually\n> continuous power around 2 Hz and 15 to 25 Hz beta bursts recurring every 600 ms (1.7 Hz).\n>\n> fig3b-control-activated-spectrogram: In the control activated state the 2 Hz activity disappears,\n> 15 to 20 Hz power is no longer visible except 15 Hz bursts of about 100 to 500 ms at about 1.5 Hz,\n> and brief (about 50 ms) 25 to 35 Hz bursts occur at about 1 Hz.\n>\n> fig6a-pd-rest-spectrogram: In the parkinsonian rest state the LFP spectrogram shows continuous\n> high-power 15 Hz beta with 25 to 35 Hz bursts of about 50 to 250 ms recurring about every 200 ms\n> (about 5 Hz).\n>\n> fig6b-pd-activated-spectrogram: In the parkinsonian activated state the LFP spectrogram shows 20\n> to 35 Hz bursts of about 25 to 100 ms recurring every 50 to 100 ms (about 10 to 20 Hz).\n\nReadings S1 (NetPyNE 1.0.5 Morlet spectrogram, its defaults) and S2 (short-time Fourier transform),\non \"LFP 0\" (E1; E2 cannot be computed). NetPyNE's own fft option with its defaults (256 samples at\n40 kHz) has a frequency step of 156 Hz, printed below, so S2 uses a 250 ms Hann window with 90%\noverlap (4 Hz steps), a standard choice. Bursts are epochs where the band's power is above halfway\nbetween its minimum and maximum in W (claims file). \"Power around 2 Hz\" is a local maximum of the\ntime-averaged spectrum within 1 to 3 Hz.\n''')\ncode(r'''\nimport scipy.signal as sps\nf_default = sps.spectrogram(np.zeros(92000), fs=m.FS, nperseg=256, noverlap=128, nfft=256)[0]\nprint(\"NetPyNE fft defaults: frequency step\", f_default[1], \"Hz; bins below 100 Hz:\", f_default[f_default < 100].tolist())\n\nTF = {}\nfor c, d in D.items():\n    x = d[\"lfp\"][int(2.0 * m.FS):int(4.3 * m.FS)]\n    f1, t1, s1 = m.morlet_spec(x, m.FS)\n    f2, t2, s2 = m.stft_spec(x, m.FS)\n    TF[(c, \"S1\")] = (f1, t1, s1, 1 / m.FS)\n    TF[(c, \"S2\")] = (f2, t2, s2, t2[1] - t2[0])\n\ndef spec_row(c, s, bands):\n    f, t, S, dt = TF[(c, s)]\n    tm = S.mean(axis=1)\n    loc = [float(f[i]) for i in range(1, len(f) - 1) if tm[i] > tm[i - 1] and tm[i] > tm[i + 1] and 1 <= f[i] <= 3]\n    row = {\"file\": m.CONDITIONS[c], \"reading\": s, \"local max 1-3 Hz\": loc,\n           \"mean 15-20 Hz power\": m.band_power(f, S, (15, 20)).mean()}\n    for band in bands:\n        b = m.band_bursts(t, m.band_power(f, S, band), dt)\n        row[f\"{band} n\"] = b[\"n\"]\n        row[f\"{band} rate Hz\"] = round(b[\"rate\"], 2)\n        row[f\"{band} median ms\"] = round(b[\"median_ms\"], 1)\n        row[f\"{band} min-max ms\"] = (round(b[\"durations\"].min() * 1e3), round(b[\"durations\"].max() * 1e3)) if b[\"n\"] else None\n        row[f\"{band} frac above\"] = round(b[\"frac_above\"], 2)\n    return row\n\nfig, ax = plt.subplots(1, 4, figsize=(16, 3))\nfor k, c in enumerate(D):\n    f, t, S, dt = TF[(c, \"S1\")]\n    ax[k].imshow(S[:, ::400], aspect=\"auto\", origin=\"lower\", extent=[2.0, 4.3, f[0], f[-1]], cmap=\"jet\")\n    ax[k].set_title(m.CONDITIONS[c] + \" (S1)\"); ax[k].set_xlabel(\"s\"); ax[k].set_ylabel(\"Hz\")\n    print(m.CONDITIONS[c], \"S1 plotted power range\", S.min(), S.max())\nplt.tight_layout(); plt.show()\n''', [\"claim:fig3a-control-rest-spectrogram\", \"claim:fig3b-control-activated-spectrogram\",\n      \"claim:fig6a-pd-rest-spectrogram\", \"claim:fig6b-pd-activated-spectrogram\"])\n\nmd(\"#### fig3a-control-rest-spectrogram\\n\\nReproduced when the 2 Hz peak is present and the 15 to 25 Hz burst rate is within 1.7 +/- 0.17 Hz under every reading.\")\ncode(r'''\nt3a = pd.DataFrame([spec_row(\"01\", s, [(15, 25)]) for s in (\"S1\", \"S2\")])\nprint(t3a.to_string(index=False))\nfor _, r in t3a.iterrows():\n    print(r[\"reading\"], \"2 Hz peak present:\", len(r[\"local max 1-3 Hz\"]) > 0, \"; burst rate within 1.53-1.87:\", within(r[\"(15, 25) rate Hz\"], (1.7, 0.17)))\n''', [\"claim:fig3a-control-rest-spectrogram\"])\nresult(\"fig3a-control-rest-spectrogram\")\n\nmd(\"#### fig3b-control-activated-spectrogram\\n\\nReproduced when, under every reading, the activated spectrum has no local maximum within 1 to 3 Hz, mean 15 to 20 Hz power is lower than at rest, the 14 to 16 Hz burst rate is 1.5 +/- 0.15 Hz, the 25 to 35 Hz burst rate 1.0 +/- 0.1 Hz, its median duration 50 +/- 5 ms, and the 14 to 16 Hz burst durations fall within 90 to 550 ms.\")\ncode(r'''\nt3b = pd.DataFrame([spec_row(\"03\", s, [(14, 16), (25, 35)]) for s in (\"S1\", \"S2\")])\nprint(t3b.to_string(index=False))\nfor _, r in t3b.iterrows():\n    s = r[\"reading\"]\n    rest15 = spec_row(\"01\", s, [])[\"mean 15-20 Hz power\"]\n    f, t, S, dt = TF[(\"03\", s)]\n    d15 = m.band_bursts(t, m.band_power(f, S, (14, 16)), dt)[\"durations\"] * 1e3\n    parts = {\"no 1-3 Hz max\": len(r[\"local max 1-3 Hz\"]) == 0, \"15-20 Hz lower than rest\": r[\"mean 15-20 Hz power\"] < rest15,\n             \"15 Hz burst rate\": within(r[\"(14, 16) rate Hz\"], (1.5, 0.15)), \"25-35 Hz burst rate\": within(r[\"(25, 35) rate Hz\"], (1.0, 0.1)),\n             \"25-35 Hz median duration\": within(r[\"(25, 35) median ms\"], (50, 5)),\n             \"15 Hz durations in 90-550 ms\": bool(np.all((d15 >= 90) & (d15 <= 550)))}\n    print(s, f\"15-20 Hz power activated/rest = {r['mean 15-20 Hz power'] / rest15:.2f};\", parts)\n''', [\"claim:fig3b-control-activated-spectrogram\"])\nresult(\"fig3b-control-activated-spectrogram\")\n\nmd(\"#### fig6a-pd-rest-spectrogram\\n\\nReproduced when the 25 to 35 Hz burst rate is 5.0 +/- 0.5 Hz and the burst durations fall within 45 to 275 ms under every reading; the share of time the 14 to 16 Hz power is above half-height is reported.\")\ncode(r'''\nt6a = pd.DataFrame([spec_row(\"02\", s, [(25, 35), (14, 16)]) for s in (\"S1\", \"S2\")])\nprint(t6a.to_string(index=False))\nfor _, r in t6a.iterrows():\n    s = r[\"reading\"]\n    f, t, S, dt = TF[(\"02\", s)]\n    d = m.band_bursts(t, m.band_power(f, S, (25, 35)), dt)[\"durations\"] * 1e3\n    print(s, \"rate within 4.5-5.5:\", within(r[\"(25, 35) rate Hz\"], (5.0, 0.5)), \"; durations in 45-275 ms:\", bool(np.all((d >= 45) & (d <= 275))),\n          \"; 14-16 Hz above half-height for\", r[\"(14, 16) frac above\"])\n''', [\"claim:fig6a-pd-rest-spectrogram\"])\nresult(\"fig6a-pd-rest-spectrogram\")\n\nmd(\"#### fig6b-pd-activated-spectrogram\\n\\nReproduced when, under every reading, the 20 to 35 Hz burst rate is within 9 to 22 Hz and the median burst duration within 22.5 to 110 ms.\")\ncode(r'''\nt6b = pd.DataFrame([spec_row(\"04\", s, [(20, 35)]) for s in (\"S1\", \"S2\")])\nprint(t6b.to_string(index=False))\nfor _, r in t6b.iterrows():\n    print(r[\"reading\"], \"rate in 9-22 Hz:\", 9 <= r[\"(20, 35) rate Hz\"] <= 22, \"; median in 22.5-110 ms:\", 22.5 <= r[\"(20, 35) median ms\"] <= 110)\n''', [\"claim:fig6b-pd-activated-spectrogram\"])\nresult(\"fig6b-pd-activated-spectrogram\")\n\n# ---- coincidences\nmd(r'''\n### control-coincident-spikes and pd-coincident-spikes\n\n> control-coincident-spikes: In the control condition 1% of PT5B spikes are coincident with another\n> PT5B spike within 1 ms at rest, and 3% in the activated state.\n>\n> pd-coincident-spikes: In the parkinsonian condition 2% of PT5B spikes are coincident (2 or more\n> spikes in 1 ms) at rest and 3% in the activated state.\n\nReadings (a) a spike of another PT5B cell within 1 ms either side or (b) in the same 1 ms bin;\nwindows (i) W, (ii) 0.3 to 4.3 s, (iii) 0 to 4.0 s. Reproduced when under one combination both\nvalues are within tolerance. As a variant, not a reading of the claims file, the same share among\nthe 20 PT5B cells whose potentials are recorded.\n''')\ncode(r'''\nEXP[\"control-coincident-spikes\"] = [(1, 0.1), (3, 0.3)]\nEXP[\"pd-coincident-spikes\"] = [(2, 0.2), (3, 0.3)]\nCOINC = {}\nfor cid, (rest, act) in {\"control-coincident-spikes\": (\"01\", \"03\"), \"pd-coincident-spikes\": (\"02\", \"04\")}.items():\n    print(cid, \"expected\", [e[0] for e in EXP[cid]])\n    for rd in \"ab\":\n        for wn, w in [(\"(i) W\", m.WINDOW), (\"(ii) 0.3-4.3 s\", (0.3, 4.3)), (\"(iii) 0-4.0 s\", (0.0, 4.0))]:\n            res = [m.coincident_fraction(D[c], \"PT5B\", w, rd) for c in (rest, act)]\n            vals = [r[0] for r in res]\n            COINC[(cid, rd, wn)] = vals\n            print(f\"  ({rd}) {wn:15s} {np.round(vals, 3).tolist()} %  spikes {[r[1] for r in res]}  within {[bool(within(v, e)) for v, e in zip(vals, EXP[cid])]}\")\n    for c in (rest, act):\n        sub = dict(D[c]); sub[\"pop\"] = {g: (\"SUB\" if g in D[c][\"vm_gids\"] else p) for g, p in D[c][\"pop\"].items()}\n        print(f\"  variant, the 20 recorded cells, {m.CONDITIONS[c]}: (a) W {m.coincident_fraction(sub, 'SUB', m.WINDOW, 'a')[0]:.2f}%, \"\n              f\"(b) W {m.coincident_fraction(sub, 'SUB', m.WINDOW, 'b')[0]:.2f}%\")\nrate_ms = {m.CONDITIONS[c]: round(len(m.pop_spikes(D[c], 'PT5B')) / 4300, 1) for c in D}\nprint(\"PT5B spikes per ms over the whole population:\", rate_ms)\n''', [\"claim:control-coincident-spikes\", \"claim:pd-coincident-spikes\"])\nresult(\"control-coincident-spikes\")\nresult(\"pd-coincident-spikes\")\n\n# ---- unitary events\nmd(r'''\n### Unitary events: fig4-control-unitary-events, fig7-pd-unitary-events, rest-synchrony-increase\n\n> fig4-control-unitary-events: In the control condition, PT5B coincident firing above that expected\n> from rate-matched Poisson processes occurs at rest in 100 to 275 ms clusters with 15 to 24 Hz\n> periodicity (mean 19 Hz), totalling 0.7 of 4.0 s (17.5%), and in the activated state in more\n> frequent 125 to 250 ms clusters totalling 1.1 of 4.0 s (27.5%).\n>\n> fig7-pd-unitary-events: In the parkinsonian condition, significant PT5B coincident firing occurs\n> at rest in 400 to 1100 ms clusters of 6 to 16 periods at 14 to 15 Hz (mean 15 Hz), totalling 3.1\n> of 4.0 s (77.5%), and in the activated state in 100 to 350 ms epochs totalling 1.4 of 4.0 s (35.0%).\n>\n> rest-synchrony-increase: At rest, PT5B spike synchrony is substantially larger in the\n> parkinsonian than in the control condition (significant synchrony 3.1 against 0.7 of 4.0 s).\n\nMethod of the claims file: coincidences are 1 ms bins with 2 or more PT5B spikes; expected count\nfrom Poisson cells at their rates in the 100 ms window; a window is significant when the\njoint-surprise p < 0.05; significant periods are the union of significant windows. Readings:\nwindows (a) slid in 1 ms steps or (b) non-overlapping; span (i) 0.3 to 4.3 s or (ii) 0 to 4.0 s;\nperiodicity (x) SCH spectral peak or (y) inverse mean interval between SCH peaks.\n''')\ncode(r'''\nEXP[\"fig4-control-unitary-events\"] = [(0.7, 0.07), (1.1, 0.11), (19, 1.9)]\nEXP[\"fig7-pd-unitary-events\"] = [(3.1, 0.31), (1.4, 0.14), (15, 1.5)]\nUE = {}\nfor c in D:\n    for sname, step in [(\"(a) 1 ms steps\", 0.001), (\"(b) non-overlapping\", 0.1)]:\n        for spname, span in [(\"(i) 0.3-4.3 s\", (0.3, 4.3)), (\"(ii) 0-4.0 s\", (0.0, 4.0))]:\n            u = m.unitary_events(D[c], \"PT5B\", span, step)\n            per = {r: m.periodicity(m.pop_spikes(D[c], \"PT5B\"), u[\"runs\"], span, reading=r) for r in \"xy\"}\n            UE[(c, sname, spname)] = (u, per)\nrows = []\nfor (c, sname, spname), (u, per) in UE.items():\n    rows.append({\"file\": m.CONDITIONS[c], \"windows\": sname, \"span\": spname, \"significant s\": u[\"total_s\"],\n                 \"clusters\": len(u[\"clusters_ms\"]), \"significant windows\": f\"{u['n_sig_windows']}/{u['n_windows']}\",\n                 \"share of 1 ms bins with >=2 spikes\": round(u[\"coinc_share_bins\"], 3),\n                 \"median observed per window\": np.median(u[\"obs\"]), \"median expected\": round(float(np.median(u[\"exp\"])), 2),\n                 \"periodicity x\": np.mean(per[\"x\"]) if per[\"x\"] else np.nan, \"periodicity y\": np.mean(per[\"y\"]) if per[\"y\"] else np.nan})\nuet = pd.DataFrame(rows)\nprint(uet.to_string(index=False))\nfor cid, (rest, act) in {\"fig4-control-unitary-events\": (\"01\", \"03\"), \"fig7-pd-unitary-events\": (\"02\", \"04\")}.items():\n    print(cid, \"expected\", [e[0] for e in EXP[cid]])\n    for sname in [\"(a) 1 ms steps\", \"(b) non-overlapping\"]:\n        for spname in [\"(i) 0.3-4.3 s\", \"(ii) 0-4.0 s\"]:\n            for pr in \"xy\":\n                ur, pr_r = UE[(rest, sname, spname)]\n                ua, _ = UE[(act, sname, spname)]\n                vals = [ur[\"total_s\"], ua[\"total_s\"], np.mean(pr_r[pr]) if pr_r[pr] else np.nan]\n                print(f\"  {sname:20s} {spname:14s} ({pr}) {vals} within {[bool(within(v, e)) if np.isfinite(v) else False for v, e in zip(vals, EXP[cid])]}\")\n''', [\"claim:fig4-control-unitary-events\", \"claim:fig7-pd-unitary-events\"])\nresult(\"fig4-control-unitary-events\")\nresult(\"fig7-pd-unitary-events\")\n\nmd(\"#### rest-synchrony-increase\\n\\nReproduced when the total duration of significant synchrony at rest is larger in the parkinsonian file under every reading.\")\ncode(r'''\nfor sname in [\"(a) 1 ms steps\", \"(b) non-overlapping\"]:\n    for spname in [\"(i) 0.3-4.3 s\", \"(ii) 0-4.0 s\"]:\n        a, b = UE[(\"01\", sname, spname)][0][\"total_s\"], UE[(\"02\", sname, spname)][0][\"total_s\"]\n        print(f\"{sname:20s} {spname:14s} control {a} s, parkinsonian {b} s, parkinsonian larger: {b > a}\")\n''', [\"claim:rest-synchrony-increase\"])\nresult(\"rest-synchrony-increase\")\n\n# ---- PD rate claims\nrate_claim(\"fig5c-pd-pt5b-rate-activated\",\n           \"In the parkinsonian condition PT5B neurons fire more in the activated state than at rest (14.2 +/- 7.1 against 29.7 +/- 12.7 spikes/s, p < 0.001).\",\n           \"Criterion: files -02 and -04, R1 and R2; as fig2c-control-pt5b-rate-activated.\",\n           \"PT5B\", [\"02\", \"04\"], [(\"02\", \"mean\"), (\"02\", \"sd\"), (\"04\", \"mean\"), (\"04\", \"sd\")],\n           [(14.2, 1.42), (7.1, 0.71), (29.7, 2.97), (12.7, 1.27)], (\"02\", \"04\"), 0.001)\nrate_claim(\"fig5c-pd-it23-rate-activated\",\n           \"In the parkinsonian condition IT2/3 neurons fire more in the activated state than at rest (0.78 +/- 1.1 against 4.3 +/- 7.1 spikes/s, p < 0.001).\",\n           \"Criterion: files -02 and -04, population IT2, R1 and R2; p < 0.001.\",\n           \"IT2\", [\"02\", \"04\"], [(\"02\", \"mean\"), (\"02\", \"sd\"), (\"04\", \"mean\"), (\"04\", \"sd\")],\n           [(0.78, 0.078), (1.1, 0.11), (4.3, 0.43), (7.1, 0.71)], (\"02\", \"04\"), 0.001)\n\nmd(r'''\n### pd-it5-silenced-activated\n\n> In the parkinsonian condition IT5A and IT5B neurons fire at 2.2 and 1.2 spikes/s at rest and stop\n> firing (0 spikes/s) in the activated state.\n\nCriterion: files -02 and -04, as control-it5-silenced-activated.\n''')\ncode(r'''\nit5(\"pd-it5-silenced-activated\", \"02\", \"04\", [(2.2, 0.22), (1.2, 0.12), (0, 0.05), (0, 0.05)])\n''', [\"claim:pd-it5-silenced-activated\"])\nresult(\"pd-it5-silenced-activated\")\n\nmd(r'''\n### pd-it6-rate-unchanged\n\n> In the parkinsonian condition the IT6 firing rate does not change with activation (6.0 spikes/s at\n> rest and in the activated state).\n\nA claim of absence. Criterion: files -02 and -04, R1 and R2; reproduced when both means are within\ntolerance under one rate reading and no test reading finds a difference at p < 0.05; not reproduced\nwhen a test does.\n''')\ncode(r'''\nEXP[\"pd-it6-rate-unchanged\"] = [(6.0, 0.6), (6.0, 0.6)]\ncheck_rates(\"pd-it6-rate-unchanged\", \"IT6\", [\"02\", \"04\"], [(\"02\", \"mean\"), (\"04\", \"mean\")])\ncmpt = compare(\"IT6\", \"02\", \"04\")\nprint(); print(cmpt.to_string(index=False))\nps = cmpt.set_index(\"reading\")[[\"T1 Wilcoxon\", \"T2 paired t\", \"T3 Mann-Whitney\", \"T4 Welch t\"]]\nprint(\"\\nAny test finds a difference at p < 0.05, per reading:\", (ps < 0.05).any(axis=1).to_dict())\nprint(\"Difference of means (activated - rest), per reading:\", (cmpt[\"mean 2\"] - cmpt[\"mean 1\"]).round(3).tolist())\n''', [\"claim:pd-it6-rate-unchanged\"])\nresult(\"pd-it6-rate-unchanged\")\n\n# ---- PD vs control\nmd(r'''\n### rest-pt5b-rate-pd-vs-control\n\n> At rest, PT5B firing rate is higher and less variable in the parkinsonian than in the control\n> condition (14.2 +/- 7.1 against 11.7 +/- 9.4 spikes/s, p < 0.001), a paradoxical increase given the\n> reduced PT5B excitability.\n\nCriterion: files -01 and -02, R1 and R2; reproduced when under one reading the four rest values are\nwithin tolerance, the parkinsonian mean is higher with p < 0.001 under every test (paired by gid),\nand the parkinsonian standard deviation is lower.\n''')\ncode(r'''\nEXP[\"rest-pt5b-rate-pd-vs-control\"] = [(11.7, 1.17), (9.4, 0.94), (14.2, 1.42), (7.1, 0.71)]\ncheck_rates(\"rest-pt5b-rate-pd-vs-control\", \"PT5B\", [\"01\", \"02\"], [(\"01\", \"mean\"), (\"01\", \"sd\"), (\"02\", \"mean\"), (\"02\", \"sd\")])\ncmpt = compare(\"PT5B\", \"01\", \"02\")\nprint(); print(cmpt.to_string(index=False))\nps = cmpt.set_index(\"reading\")[[\"T1 Wilcoxon\", \"T2 paired t\", \"T3 Mann-Whitney\", \"T4 Welch t\"]]\nprint(\"\\nAll four tests below p = 0.001, per reading:\", (ps < 0.001).all(axis=1).to_dict())\nt = rate_rows(\"PT5B\", [\"01\", \"02\"]).set_index([\"reading\", \"file\"])\nprint(\"Parkinsonian sd lower, per reading:\", {r: bool(t.loc[(r, \"02\"), \"sd\"] < t.loc[(r, \"01\"), \"sd\"]) for r in [\"R1\", \"R2\", \"R3 (variant)\"]})\n''', [\"claim:rest-pt5b-rate-pd-vs-control\"])\nresult(\"rest-pt5b-rate-pd-vs-control\")\n\nrate_claim(\"rest-it4-rate-pd-vs-control\",\n           \"At rest, IT4 firing rate is higher in the parkinsonian than in the control condition (14.1 against 2.6 spikes/s, p < 0.05).\",\n           \"Criterion: files -01 and -02, R1 and R2; reproduced when under one reading both means are within tolerance and the parkinsonian rate is higher with p < 0.05 under every test.\",\n           \"IT4\", [\"01\", \"02\"], [(\"01\", \"mean\"), (\"02\", \"mean\")], [(2.6, 0.26), (14.1, 1.41)], (\"01\", \"02\"), 0.05)\nrate_claim(\"rest-it5a-rate-pd-vs-control\",\n           \"At rest, IT5A firing rate is lower in the parkinsonian than in the control condition (2.2 against 3.3 spikes/s, p < 0.01).\",\n           \"Criterion: files -01 and -02, R1 and R2; reproduced when under one reading both means are within tolerance and the parkinsonian rate is lower with p < 0.01 under every test.\",\n           \"IT5A\", [\"01\", \"02\"], [(\"01\", \"mean\"), (\"02\", \"mean\")], [(3.3, 0.33), (2.2, 0.22)], (\"01\", \"02\"), 0.01)\n\nmd(r'''\n### activated-pt5b-rate-pd-vs-control\n\n> In the activated state, PT5B firing rate is higher and less variable in the parkinsonian than in\n> the control condition (29.7 +/- 12.7 against 26.8 +/- 18.2 spikes/s, p < 0.001).\n\nCriterion: files -03 and -04, as rest-pt5b-rate-pd-vs-control. The Discussion says there was no\nsignificant change in the activated state; the outcome under every test is reported for both.\n''')\ncode(r'''\nEXP[\"activated-pt5b-rate-pd-vs-control\"] = [(26.8, 2.68), (18.2, 1.82), (29.7, 2.97), (12.7, 1.27)]\ncheck_rates(\"activated-pt5b-rate-pd-vs-control\", \"PT5B\", [\"03\", \"04\"], [(\"03\", \"mean\"), (\"03\", \"sd\"), (\"04\", \"mean\"), (\"04\", \"sd\")])\ncmpt = compare(\"PT5B\", \"03\", \"04\")\nprint(); print(cmpt.to_string(index=False))\nps = cmpt.set_index(\"reading\")[[\"T1 Wilcoxon\", \"T2 paired t\", \"T3 Mann-Whitney\", \"T4 Welch t\"]]\nprint(\"\\nAll four tests below p = 0.001, per reading:\", (ps < 0.001).all(axis=1).to_dict())\nprint(\"Any test at p < 0.05 (the Discussion's 'no significant change'), per reading:\", (ps < 0.05).any(axis=1).to_dict())\nt = rate_rows(\"PT5B\", [\"03\", \"04\"]).set_index([\"reading\", \"file\"])\nprint(\"Parkinsonian sd lower, per reading:\", {r: bool(t.loc[(r, \"04\"), \"sd\"] < t.loc[(r, \"03\"), \"sd\"]) for r in [\"R1\", \"R2\", \"R3 (variant)\"]})\n''', [\"claim:activated-pt5b-rate-pd-vs-control\"])\nresult(\"activated-pt5b-rate-pd-vs-control\")\n\nrate_claim(\"activated-it6-rate-pd-vs-control\",\n           \"In the activated state, IT6 firing rate is higher in the parkinsonian than in the control condition (6.0 against 3.5 spikes/s, p < 0.001).\",\n           \"Criterion: files -03 and -04, R1 and R2; reproduced when under one reading both means are within tolerance and the parkinsonian rate is higher with p < 0.001 under every test.\",\n           \"IT6\", [\"03\", \"04\"], [(\"03\", \"mean\"), (\"04\", \"mean\")], [(3.5, 0.35), (6.0, 0.6)], (\"03\", \"04\"), 0.001)\n\n# ---- power comparisons\nmd(r'''\n### rest-beta-power-order-of-magnitude\n\n> At rest, LFP beta power around 15 Hz is an order of magnitude larger in the parkinsonian than in\n> the control condition.\n\nCriterion: files -01 and -02, LFP in W, readings S1, S2 (E1 only); power (a) at 15 Hz and (b) mean\nover 14 to 16 Hz; ratio of time-averaged parkinsonian to control power; reproduced when the ratio is\nin 3.16 to 31.6 under every reading, not reproduced when below 3.16 under every reading. As a\nvariant, the ratio of the spectrograms' maxima (the colour bars of Figs. 3 and 6 are x 10^-5 and x\n10^-4).\n''')\ncode(r'''\nrows = []\nfor s in (\"S1\", \"S2\"):\n    f1, _, S1c, _ = TF[(\"01\", s)]\n    f2, _, S2p, _ = TF[(\"02\", s)]\n    at15 = lambda f, S: S[np.argmin(np.abs(f - 15))].mean()\n    for name, fn in [(\"(a) at 15 Hz\", at15), (\"(b) 14-16 Hz\", lambda f, S: m.band_power(f, S, (14, 16)).mean())]:\n        a, b = fn(f1, S1c), fn(f2, S2p)\n        rows.append({\"reading\": s, \"measure\": name, \"control\": a, \"parkinsonian\": b, \"ratio\": b / a,\n                     \"log10 ratio\": np.log10(b / a), \"in 3.16-31.6\": 10 ** 0.5 <= b / a <= 10 ** 1.5})\n    rows.append({\"reading\": s, \"measure\": \"variant, max over the spectrogram\", \"control\": S1c.max(), \"parkinsonian\": S2p.max(),\n                 \"ratio\": S2p.max() / S1c.max(), \"log10 ratio\": np.log10(S2p.max() / S1c.max()),\n                 \"in 3.16-31.6\": 10 ** 0.5 <= S2p.max() / S1c.max() <= 10 ** 1.5})\nprint(pd.DataFrame(rows).to_string(index=False))\n''', [\"claim:rest-beta-power-order-of-magnitude\"])\nresult(\"rest-beta-power-order-of-magnitude\")\n\nmd(r'''\n### activated-20-35hz-power-pd-vs-control\n\n> In the activated state, the parkinsonian condition shows more power at 20 to 35 Hz than the\n> control condition.\n\nCriterion: files -03 and -04, LFP readings S1, S2 (E1) and the PT5B SCH spectrum; reproduced when\nmean 20 to 35 Hz power is higher in the parkinsonian file under every reading.\n''')\ncode(r'''\nrows = []\nfor s in (\"S1\", \"S2\"):\n    a = m.band_power(TF[(\"03\", s)][0], TF[(\"03\", s)][2], (20, 35)).mean()\n    b = m.band_power(TF[(\"04\", s)][0], TF[(\"04\", s)][2], (20, 35)).mean()\n    rows.append({\"reading\": f\"LFP {s}\", \"control\": a, \"parkinsonian\": b, \"ratio\": b / a, \"higher\": b > a})\nf, p3 = SPEC[\"03\"]; _, p4 = SPEC[\"04\"]\nsel = (f >= 20) & (f <= 35)\nrows.append({\"reading\": \"PT5B SCH (Welch)\", \"control\": p3[sel].mean(), \"parkinsonian\": p4[sel].mean(), \"ratio\": p4[sel].mean() / p3[sel].mean(), \"higher\": p4[sel].mean() > p3[sel].mean()})\nprint(pd.DataFrame(rows).to_string(index=False))\n''', [\"claim:activated-20-35hz-power-pd-vs-control\"])\nresult(\"activated-20-35hz-power-pd-vs-control\")\n\ncode(r'''\nprint(f\"notebook ran in {time.time() - started:.0f} s\")\n''')\n\nmd(open(sys.argv[4]).read() if len(sys.argv) > 4 else \"## Summary\\n\\nTo be written.\")\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbf.write(nb, sys.argv[1])\nprint(\"cells\", len(cells))\n"
}
```

```
File created successfully at: /tmp/claude-1001/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/001444-doherty-2025 && . $TMPDIR/venv/bin/activate && uv pip install -q nbformat nbconvert ipykernel pyyaml 2>&1|tail -1; python $TMPDIR/build_nb.py reproduce_doherty_2025.ipynb && date -u && time jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 --output-dir $TMPDIR/exec --output dev.ipynb reproduce_doherty_2025.ipynb 2>&1 | tail -5
```

```
cells 119
Mon Nov  2 17:13:29 UTC 2026
[NbConvertApp] Making directory /tmp/claude-1001/exec
[NbConvertApp] Converting notebook reproduce_doherty_2025.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 606664 bytes to /tmp/claude-1001/exec/dev.ipynb

real	3m7.241s
user	0m39.333s
sys	0m3.015s
```

**Agent**

Notebook runs end to end in about 3 minutes. Reading the outputs.

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && python - <<'EOF' > out.txt
import nbformat
nb=nbformat.read('exec/dev.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type=='code':
        print(f'=== cell {i} tags={c.metadata.get("tags")}')
        for o in c.outputs:
            if 'text' in o: print(o['text'])
            elif o.get('output_type')=='error': print('ERROR', o['ename'], o['evalue'])
            elif 'data' in o and 'text/plain' in o['data'] and 'image/png' not in o['data']: print(o['data']['text/plain'])
EOF
wc -l out.txt; head -c 20000 out.txt
```

```
733 out.txt
=== cell 1 tags=None
loaded 16 files of dandiset 001444 version 0.250805.2002 in 152 s

=== cell 3 tags=['sanity']
                                     path  size_MB                                 blob
                      sub-001/sub-001.nwb    556.5 8125364f-e0cb-4584-aeb1-14d505e18d09
sub-001/sub-001_ses-sM1-04-22-2024-01.nwb    556.5 8125364f-e0cb-4584-aeb1-14d505e18d09
sub-001/sub-001_ses-sM1-04-22-2024-02.nwb    556.6 d0e92d4e-ce77-42ce-9876-a11663d27840
sub-001/sub-001_ses-sM1-04-22-2024-03.nwb    557.8 944813cb-df12-47bc-9991-743c723042af
sub-001/sub-001_ses-sM1-04-22-2024-04.nwb    557.8 ae4f13b6-9a5e-4ced-b49a-60dbfac10321
sub-001/sub-001_ses-sM1-04-25-2024-01.nwb    556.7 f5039f11-0d99-43e7-b254-7f4dd7177a0f
sub-001/sub-001_ses-sM1-04-25-2024-02.nwb    556.9 6c934e64-5133-4e4b-9513-93e46fd20c20
sub-001/sub-001_ses-sM1-04-25-2024-03.nwb    557.8 c8d09983-a7c5-4ebc-b00c-e06881a3dd6d
sub-001/sub-001_ses-sM1-04-25-2024-04.nwb    557.9 2af975f3-d0ae-47b0-ac51-5c8dda9f460e
sub-001/sub-001_ses-sM1-04-26-2024-01.nwb    556.8 d4c1a688-fe85-45ab-80a6-eb5dcf5fd652
sub-001/sub-001_ses-sM1-04-26-2024-02.nwb    556.9 b4a799af-402b-44bc-9c89-20e003abaf10
sub-001/sub-001_ses-sM1-04-26-2024-03.nwb    557.7 235430d3-bde8-468c-8251-a53321d7323f
sub-001/sub-001_ses-sM1-04-26-2024-04.nwb    557.8 94944c71-c9de-4f2e-83b3-62f9a96f3834
sub-001/sub-001_ses-sM1-12-12-2023-01.nwb     32.6 e87d848d-916d-47b3-beba-93d07c0e2d6f
[... 208 more lines not kept]
```

**Agent**

Two fixes needed: the block-overlap check counts ambiguous gids twice, and the Vm-to-unit spike check pairs spikes badly. Inspecting one trace.

**Agent calls Bash**

```bash
cd entries/001444-doherty-2025 && . $TMPDIR/venv/bin/activate && PYTHONPATH=. python -c "
import m1sim as m, numpy as np
d=m.load_file(m.PAPER_SET,'01')
for g in d['vm_gids'][:4]:
    v=d['vm'][g]; su=d['trains'][g]
    for thr in [0,-20,-10]:
        sv=m.vm_spikes(v,thr=thr); print(g,thr,len(sv),len(su))
    sv=m.vm_spikes(v,thr=-20)
    print(np.round(sv[:8],5)); print(np.round(su[:8],5))
    # nearest lags
    lag=[(s-sv[np.argmin(abs(sv-s))])*1e3 for s in su]; print('lags ms', np.round(np.percentile(lag,[0,50,100]),3))
"
```

```
5201 0 13 22
5201 -20 13 22
5201 -10 13 22
[0.03712 0.11162 0.1316  0.1889  0.52165 0.5857  0.65307 0.71075]
[0.03718 0.11165 0.13165 0.18893 0.5217  0.58575 0.65313 0.7108 ]
lags ms [-7.89725e+02  5.00000e-02  5.63650e+02]
5202 0 96 97
5202 -20 96 97
5202 -10 96 97
[0.03775 0.10732 0.12868 0.1843  0.23705 0.27535 0.30755 0.34005]
[0.0378  0.10738 0.1287  0.18435 0.2371  0.2754  0.30758 0.3401 ]
lags ms [-40.85   0.05  35.4 ]
5301 0 23 33
5301 -20 23 33
5301 -10 23 33
[0.0387  0.10995 0.12765 0.1859  0.29263 0.48728 0.93535 1.00248]
[0.03875 0.11    0.1277  0.18595 0.29268 0.48732 0.92593 0.9932 ]
lags ms [-2.4760e+02  5.0000e-02  2.3935e+02]
5302 0 97 94
5302 -20 97 94
[... 4 more lines not kept]
```

**Agent**

Vm crossings match the unit spikes early in the run (lag 0.05 ms) and then drift apart. Quantifying the match over time, in the paper's set and in another set.

**Agent calls Bash**

```bash
. $TMPDIR/venv/bin/activate && PYTHONPATH=. python -c "
import m1sim as m, numpy as np
def match(d, gids):
    out=[]
    for g in gids:
        v=d['vm'][g]; su=d['trains'].get(g,np.array([])); sv=m.vm_spikes(v)
        if len(su)==0 or len(sv)==0: continue
        near=np.array([np.min(abs(sv-s)) for s in su])<0.0005
        out.append([np.mean(near[su<0.5]) if (su<0.5).any() else np.nan, np.mean(near[(su>=0.5)&(su<2)]) if ((su>=0.5)&(su<2)).any() else np.nan, np.mean(near[su>=2]) if (su>=2).any() else np.nan, len(sv), len(su)])
    a=np.array(out); return np.nanmean(a[:,:3],axis=0), a[:,3].sum(), a[:,4].sum()
for c in ['01','02','03','04']:
    d=m.load_file(m.PAPER_SET,c); print('paper set',c, match(d,d['vm_gids']))
d=m.load_file('sM1-04-22-2024','01'); print('04-22 01', match(d,d['vm_gids'][:60]))
"
```

```
paper set 01 (array([1.        , 0.34978577, 0.01530027]), np.float64(1112.0), np.float64(1123.0))
paper set 02 (array([1.        , 0.848855  , 0.03695059]), np.float64(1241.0), np.float64(1228.0))
paper set 03 (array([1.        , 0.56314693, 0.05573433]), np.float64(3123.0), np.float64(3092.0))
paper set 04 (array([0.94790782, 0.05768922, 0.03878194]), np.float64(2777.0), np.float64(2812.0))
04-22 01 (array([1., 1., 1.]), np.float64(3077.0), np.float64(3077.0))
```

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n '/cell 35/,$p' out.txt | head -c 30000
```

```
<persisted-output>
Output too large (29.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/4c89dc14-2bdb-46fc-a88e-53626ecd4fc1/tool-results/toolu_01XXreUyjR8gKsyLLd3v1Laf.txt

Preview (first 2KB):
=== cell 35 tags=['claim:fig2c-control-it6-rate-activated']
file         condition pop             reading  mean    sd    n
  01      control rest IT6                  R1 4.276 5.577 1244
  01      control rest IT6 R1 (smallest block) 4.304 5.584 1236
  01      control rest IT6                  R2 6.273 5.754  848
  01      control rest IT6        R3 (variant) 5.820 5.775  914
  03 control activated IT6                  R1 0.952 3.126 1244
  03 control activated IT6 R1 (smallest block) 0.958 3.136 1236
  03 control activated IT6                  R2 4.874 5.569  243
  03 control activated IT6        R3 (variant) 3.473 5.192  341

R1                     values [4.276, 5.577, 0.952, 3.126]  expected [5.8, 5.8, 3.5, 5.2]  within tolerance [False, True, False, False]  all: False
R1 (smallest block)    values [4.304, 5.584, 0.958, 3.136]  expected [5.8, 5.8, 3.5, 5.2]  within tolerance [False, True, False, False]  all: False
R2                     values [6.273, 5.754, 4.874, 5.569]  expected [5.8, 5.8, 3.5, 5.2]  within tolerance [True, True, False, True]  all: False
R3 (variant)           values [5.82, 5.775, 3.473, 5.192]  expected [5.8, 5.8, 3.5, 5.2]  within tolerance [True, True, True, True]  all: True

[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/4c89dc14-2bdb-46fc-a88e-53626ecd4fc1/tool-results/toolu_01XXreUyjR8gKsyLLd3v1Laf.txt",
 "offset": 25
}
```

```
25	file         condition  pop             reading  mean    sd    n
26	  01      control rest IT5A                  R1 1.208 2.881  644
27	  01      control rest IT5A R1 (smallest block) 1.210 2.883  643
28	  01      control rest IT5A                  R2 3.568 4.017  218
29	  01      control rest IT5A        R3 (variant) 3.255 3.967  239
30	  03 control activated IT5A                  R1 0.000 0.000  644
31	  03 control activated IT5A R1 (smallest block) 0.000 0.000  643
32	  03 control activated IT5A                  R2   NaN   NaN    0
33	  03 control activated IT5A        R3 (variant) 0.000   NaN    1
34	  01      control rest IT5B                  R1 1.749 3.296 1435
35	  01      control rest IT5B R1 (smallest block) 1.749 3.296 1435
36	  01      control rest IT5B                  R2 3.584 3.962  700
37	  01      control rest IT5B        R3 (variant) 3.075 3.877  816
38	  03 control activated IT5B                  R1 0.000 0.000 1435
39	  03 control activated IT5B R1 (smallest block) 0.000 0.000 1435
40	  03 control activated IT5B                  R2   NaN   NaN    0
41	  03 control activated IT5B        R3 (variant) 0.000 0.000    2
42	R1                     values [1.208, 1.749, 0.0, 0.0] expected [3.3, 3.1, 0, 0] within [False, False, True, True] all: False
43	R1 (smallest block)    values [1.21, 1.749, 0.0, 0.0] expected [3.3, 3.1, 0, 0] within [False, False, True, True] all: False
44	R2                     values [3.568, 3.584, nan, nan] expected [3.3, 3.1, 0, 0] within [True, False, False, False] all: False
[... 291 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/4c89dc14-2bdb-46fc-a88e-53626ecd4fc1/tool-results/toolu_01XXreUyjR8gKsyLLd3v1Laf.txt",
 "offset": 334
}
```

```
334	  02      parkinsonian r
335	Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n '/cell 91 /,$p' out.txt | sed -n '30,200p'
```

```
02      parkinsonian rest IT6                  R2 6.792 6.731  243
  02      parkinsonian rest IT6        R3 (variant) 6.002 6.691  275
  04 parkinsonian activated IT6                  R1 1.729 4.493 1244
  04 parkinsonian activated IT6 R1 (smallest block) 1.740 4.506 1236
  04 parkinsonian activated IT6                  R2 6.637 6.710  324
  04 parkinsonian activated IT6        R3 (variant) 5.990 6.671  359

R1                     values [1.327, 1.729]  expected [6.0, 6.0]  within tolerance [False, False]  all: False
R1 (smallest block)    values [1.335, 1.74]  expected [6.0, 6.0]  within tolerance [False, False]  all: False
R2                     values [6.792, 6.637]  expected [6.0, 6.0]  within tolerance [False, False]  all: False
R3 (variant)           values [6.002, 5.99]  expected [6.0, 6.0]  within tolerance [True, True]  all: True


     reading   mean 1   mean 2  n paired  T1 Wilcoxon  T2 paired t  T3 Mann-Whitney  T4 Welch t
          R1 1.326716 1.728645      1244     0.002497     0.002185         0.000172    0.018653
          R2 6.791913 6.637144       126     0.884203     0.926040         0.624164    0.786253
R3 (variant) 6.001581 5.990069       148     0.605208     0.487498         0.995801    0.982857

Any test finds a difference at p < 0.05, per reading: {'R1': True, 'R2': False, 'R3 (variant)': False}
Difference of means (activated - rest), per reading: [0.402, -0.155, -0.012]
[... 143 more lines not kept]
```

**Agent**

Nearly every IT-population number matches the paper under R3. Checking the cut-off `pd-it5` output, then fixing the data-check cells.

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n '/cell 91 /,/cell 94/p' out.txt | tail -12; date -u
```

```
04 parkinsonian activated IT5B                  R1 0.000 0.000 1435
  04 parkinsonian activated IT5B R1 (smallest block) 0.000 0.000 1435
  04 parkinsonian activated IT5B                  R2   NaN   NaN    0
  04 parkinsonian activated IT5B        R3 (variant) 0.000 0.000   11
R1                     values [0.471, 0.47, 0.0, 0.0] expected [2.2, 1.2, 0, 0] within [False, False, True, True] all: False
R1 (smallest block)    values [0.471, 0.47, 0.0, 0.0] expected [2.2, 1.2, 0, 0] within [False, False, True, True] all: False
R2                     values [2.568, 2.188, nan, nan] expected [2.2, 1.2, 0, 0] within [False, False, False, False] all: False
R3 (variant)           values [2.165, 1.246, 0.0, 0.0] expected [2.2, 1.2, 0, 0] within [True, True, True, True] all: True
parkinsonian activated: IT5A units in the file 1, spikes in 0-4.3 s 1, last spike at 0.041 s
parkinsonian activated: IT5B units in the file 11, spikes in 0-4.3 s 11, last spike at 0.044 s

=== cell 94 tags=['claim:pd-it6-rate-unchanged']
Mon Nov  2 17:19:09 UTC 2026
Shell cwd was reset to
```

**Agent**

Adding a Vm-subset loader and a spike-match measure to the helper.

**Agent calls Bash**

```bash
cd entries/001444-doherty-2025 && python - <<'EOF'
p='m1sim.py'; s=open(p).read()
s=s.replace('''# ---------------------------------------------------------------- populations''','''def load_vm_subset(set_name: str, cond: str, n: int, window=None) -> dict:
    """The first `n` PT5B membrane potentials of a file (gid -> trace), optionally in a window."""
    f = open_nwb(path_of(set_name, cond))
    return {int(k.split()[3]): read_series(f, k, window)[0] for k in vm_names(f)[:n]}


def vm_match(vm: dict, trains: dict, t0: float = 0.0, spans=((0, 0.5), (0.5, 2.0), (2.0, 4.3)),
             tol: float = 0.0005) -> list[dict]:
    """For each trace, the share of the same gid's unit spikes that have an upward 0 mV crossing
    of the trace within `tol` s, in each span of time. `t0` is the time of the trace's first
    sample."""
    rows = []
    for g, v in vm.items():
        sv = vm_spikes(v) + t0
        su = trains.get(g, np.array([]))
        row = {"gid": g, "Vm spikes": len(sv), "unit spikes": len(su)}
        for a, b in spans:
            u = su[(su >= a) & (su < b)]
            if len(u) and len(sv):
                row[f"{a}-{b} s"] = float(np.mean([np.min(np.abs(sv - x)) < tol for x in u]))
            else:
                row[f"{a}-{b} s"] = np.nan
        rows.append(row)
    return rows


# ---------------------------------------------------------------- populations''')
open(p,'w').write(s)
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
. $TMPDIR/venv/bin/activate && PYTHONPATH=. python -c "
import time, m1sim as m
t=time.time(); v=m.load_vm_subset('sM1-04-22-2024','03',40,(2.0,4.3)); print(len(v), time.time()-t)
t=time.time(); v=m.load_vm_subset('sM1-04-22-2024','01',20); print(len(v), time.time()-t)
"
```

```
40 14.273926258087158
20 12.894898176193237
```

**Agent**

About 14 s per file; the added reads bring the notebook to roughly 5 to 6 minutes. Editing the builder.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='build_nb.py'; s=open(p).read()
old_blk='''print("Sum of the largest sizes:", int(bl.n_max.sum()), "; the blocks overlap nowhere:",
      all(BLOCKS[a][3] < BLOCKS[b][0] for a, b in zip(m.M1_POPS, m.M1_POPS[1:])))'''
new_blk='''unseen = sum(BLOCKS[b][1] - BLOCKS[a][2] - 1 for a, b in zip(m.M1_POPS, m.M1_POPS[1:])) + BLOCKS["IT2"][1] + (m.FIRST_INPUT_GID - 1 - BLOCKS["PV6"][2])
print("Observed gid ranges of the populations overlap nowhere:",
      all(BLOCKS[a][2] < BLOCKS[b][1] for a, b in zip(m.M1_POPS, m.M1_POPS[1:])),
      "; gids never seen, between blocks:", unseen, "; sum of smallest sizes + unseen gids:", int(bl.n_min.sum()) + unseen)'''
assert old_blk in s; s=s.replace(old_blk,new_blk)
i=s.index("# Clock and labels: spikes detected")
j=s.index("''', [\"sanity\"])", i)
new_vm='''# Clock and labels: upward 0 mV crossings of each membrane potential trace against the spike
# times of the unit with the same gid: the share of unit spikes with a crossing within 0.5 ms, by
# span of time. The paper's set (20 traces per file) and, for comparison, the first 20 traces of
# each file of set sM1-04-22-2024.
rows = []
for c, d in D.items():
    for r in m.vm_match(d["vm"], d["trains"]):
        rows.append({"set": m.PAPER_SET, "file": c, "pop": d["pop"].get(r["gid"]), **r,
                     "Vm min": d["vm"][r["gid"]].min(), "Vm max": d["vm"][r["gid"]].max()})
VM_OTHER = {c: m.load_vm_subset("sM1-04-22-2024", c, 20) for c in m.CONDITIONS}
for c, vmd in VM_OTHER.items():
    d = OTHER[("sM1-04-22-2024", c)]
    for r in m.vm_match(vmd, d["trains"]):
        rows.append({"set": "sM1-04-22-2024", "file": c, "pop": d["pop"].get(r["gid"]), **r,
                     "Vm min": vmd[r["gid"]].min(), "Vm max": vmd[r["gid"]].max()})
vmchk = pd.DataFrame(rows)
print(vmchk.groupby(["set", "file"]).agg(traces=("gid", "size"), all_PT5B=("pop", lambda s: bool((s == "PT5B").all())),
      Vm_spikes=("Vm spikes", "sum"), unit_spikes=("unit spikes", "sum"),
      matched_0_05s=("0-0.5 s", "mean"), matched_05_2s=("0.5-2.0 s", "mean"), matched_2_43s=("2.0-4.3 s", "mean"),
      vm_min=("Vm min", "min"), vm_max=("Vm max", "max")).round(3).to_string())
print("PT5B gids with Vm in the paper's set, same in all four files:", all(D[c]["vm_gids"] == D["01"]["vm_gids"] for c in D),
      D["01"]["vm_gids"])
print("Per-trace share matched in W, paper's set, range:", vmchk[vmchk.set == m.PAPER_SET]["2.0-4.3 s"].min(),
      "to", vmchk[vmchk.set == m.PAPER_SET]["2.0-4.3 s"].max())
'''
s=s[:i]+new_vm+s[j:]
old_md='''Every trace belongs to a PT5B unit of the same gid, and its upward crossings of 0 mV fall on that
unit's spike times, within the lag printed (the unit times are NetPyNE's threshold crossings), so
the membrane potentials and the spike times share one clock and one labelling. The potentials
range over the values printed, in mV.'''
new_md='''Every trace belongs to a PT5B unit of the same gid. In set sM1-04-22-2024 the trace's 0 mV
crossings fall on that unit's spike times throughout the 4.3 s, so there the potentials and the
spikes share one clock and one labelling. In the paper's set they do only at the start: the
crossings match the unit's spikes in the first 0.5 s, less from 0.5 to 2 s, and hardly at all in W
(shares printed above), while the numbers of spikes stay similar. The potentials of the paper's set
therefore come from a run that diverged from the one whose spikes are stored, with the same cells
and the same start; that cannot be established from the files and is recorded as a finding. The
potentials range over the values printed, in mV.'''
assert old_md in s; s=s.replace(old_md,new_md)
# Vm variant in pd-activated-vm claim
old_v='''print(vm.round(2).to_string(index=False))
from scipy import stats'''
new_v='''print(vm.round(2).to_string(index=False))
from scipy import stats
# Variant: the first 40 PT5B traces of files -03 and -04 of the other three sets, whose potentials
# match their spikes (data check); not the paper's set.
var = []
for s_ in m.SETS[1:]:
    v3 = m.load_vm_subset(s_, "03", 40, m.WINDOW)
    v4 = m.load_vm_subset(s_, "04", 40, m.WINDOW)
    g = [k for k in v3 if k in v4]
    dmean = np.array([v4[k].mean() - v3[k].mean() for k in g])
    dmed = np.array([np.median(v4[k]) - np.median(v3[k]) for k in g])
    var.append({"set": s_, "cells": len(g), "mean diff mV": dmean.mean(), "lower (mean)": int((dmean < 0).sum()),
                "median diff mV": dmed.mean(), "lower (median)": int((dmed < 0).sum())})
print("\\nVariant, other sets:")
print(pd.DataFrame(var).round(2).to_string(index=False))'''
assert old_v in s; s=s.replace(old_v,new_v)
open(p,'w').write(s)
EOF
echo done
```

```
done
Shell cwd was reset to
```

**Agent**

Now the header, conclusions and summary.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='build_nb.py'; s=open(p).read()
old='''populations the claims use the bounds differ by at most 15 cells (IT4, IT5A, IT6), and both are
shown below where it matters.'''
new='''populations the claims use the bounds differ by at most 8 cells (IT6; IT2, IT4 and IT5A by 1),
and the rates under both bounds are shown below.'''
assert old in s; s=s.replace(old,new)
old='''Results describe and with one clock for the LFP and the spikes. The lag of the opposite extreme is
shorter in the activated files (gamma) than at rest (beta).'''
new='''Results describe and with one clock for the LFP and the spikes in W.'''
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
EOF
cat > $TMPDIR/header.md <<'EOF'
# Reproducing Doherty et al. (2025) from dandiset 001444

**Paper.** Doherty DW, Chen L, Smith Y, Wichmann T, Chu H-Y, Lytton WW (2025). Enhanced beta power
emerges from simulated parkinsonian primary motor cortex. *npj Parkinson's Disease* 11, 230.
[doi:10.1038/s41531-025-01070-4](https://doi.org/10.1038/s41531-025-01070-4).

**Claims.** `claims/001444/10.1038-s41531-025-01070-4.yaml`, written from the version of record
(Europe PMC, PMC12325672: main text, legends and Methods; the supplement was not available) and
checked by a second reader. The claims file decides what is tested and how.

**Dandiset.** [DANDI:001444](https://dandiarchive.org/dandiset/001444/0.250805.2002), version
0.250805.2002. The paper's data statement names the dandiset without a version. This is the only
published version, and the draft holds the same 17 assets with the same blobs (data check), so
the pinned version holds what the paper deposited.

**What the dandiset holds.** Four sets of four NetPyNE simulations of a 10,073-cell model of mouse
M1, 4.3 s each: control and parkinsonian, rest and activated, per set. The paper's results come
from set sM1_12-12-2023 (Methods, paragraph 2), files `sub-001_ses-sM1-12-12-2023-01` to `-04`.
Each file holds spike times of the cells that fired, one LFP trace and somatic potentials of 20
(paper's set) or 400 (other sets) PT5B cells. One asset, `sub-001/sub-001.nwb`, is a second copy
of `sub-001_ses-sM1-04-22-2024-01.nwb`.

**Outside inputs.** None. The spectrogram of reading S1 is a copy of NetPyNE 1.0.5's Morlet
method in the helper; it is software the Methods name, not data.

| Claim | Tested |
|---|---|
| fig1-network-size | tested |
| model-pt5b-excitability-decrease | blocked: data_missing (no current-injection simulations) |
| robustness-four-sets | blocked: methods_underspecified (measures reported per set) |
| fig2-control-rest-beta, fig2-control-activated-gamma, fig5-pd-rest-beta, fig5-pd-activated-gamma | tested |
| fig2c-control-pt5b-rate-activated, fig2c-control-it23-rate-activated, fig2c-control-it6-rate-activated | tested |
| control-it5-silenced-activated, control-it4-rate-activated, pt5b-highest-rate | tested |
| control-cv-isi, pd-cv-isi | tested |
| control-subthreshold-oscillations, pd-no-subthreshold-oscillations | blocked: methods_underspecified (no detection rule) |
| control-duty-cycle, pd-duty-cycle | tested |
| fig3a, fig3b, fig6a, fig6b spectrogram claims | tested |
| control-coincident-spikes, pd-coincident-spikes | tested |
| fig4-control-unitary-events, fig7-pd-unitary-events, rest-synchrony-increase | tested |
| fig5c-pd-pt5b-rate-activated, fig5c-pd-it23-rate-activated, pd-it5-silenced-activated, pd-it6-rate-unchanged | tested |
| pd-activated-vm-more-negative | tested |
| rest-pt5b-rate-pd-vs-control, rest-it4-rate-pd-vs-control, rest-it5a-rate-pd-vs-control | tested |
| activated-pt5b-rate-pd-vs-control, activated-it6-rate-pd-vs-control | tested |
| rest-beta-power-order-of-magnitude, activated-20-35hz-power-pd-vs-control | tested |
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/concl.py",
 "content": "CONCL = {\n\"fig1-network-size\": \"**Result: not reproduced.** The files of set sM1_12-12-2023 hold 4,480, 3,231, 2,919 and 2,917 M1 units, not 10,073, because only cells that fired are stored. The criterion's count fails for that reason; the gids are consistent with the paper, since the input generators start at gid 10073 and the 15 M1 populations are all present.\",\n\"fig2-control-rest-beta\": \"**Result: reproduced.** The largest peak of the control rest PT5B SCH spectrum is at 19 Hz searched above 0 Hz and above 5 Hz, within 18 to 22 Hz. The LFP variant peaks at 1 Hz above 0 Hz and at 19 Hz above 5 Hz.\",\n\"fig2-control-activated-gamma\": \"**Result: reproduced.** The control activated PT5B SCH spectrum peaks at 44 Hz under both search ranges, within 39.6 to 48.4 Hz. The LFP variant peaks at 1 Hz and 13 Hz.\",\n\"fig5-pd-rest-beta\": \"**Result: reproduced.** The parkinsonian rest PT5B SCH spectrum peaks at 15 Hz under both search ranges, within 13.5 to 16.5 Hz; the LFP variant also peaks at 15 Hz.\",\n\"fig5-pd-activated-gamma\": \"**Result: not reproduced.** The parkinsonian activated PT5B SCH spectrum peaks at 27 Hz under both search ranges, outside 38.7 to 47.3 Hz; its next local maxima are at 30 and 21 Hz. The LFP variant also peaks at 27 Hz.\",\n\"fig2c-control-pt5b-rate-activated\": \"**Result: reproduced.** Under R1, PT5B rates are 11.69 +/- 9.40 spikes/s at rest and 26.76 +/- 18.17 activated, all four within tolerance, and all four tests give p below 1e-98. R2 gives 30.60 +/- 16.13 activated, outside tolerance.\",\n\"fig2c-control-it23-rate-activated\": \"**Result: not reproduced.** Under R1, IT2 rates are 0.095 +/- 0.565 and 0.262 +/- 2.172 spikes/s; under R2, 1.555 +/- 1.723 and 8.883 +/- 9.220; neither reading has all four values within tolerance, and under neither are all four tests below 0.001 (R1 Wilcoxon p = 0.69). The R3 variant, the cells the file holds, gives 1.203 +/- 1.649 and 6.662 +/- 8.858, all four within tolerance, with the unpaired tests below 0.001 and the paired ones at 0.016 and 0.011.\",\n\"fig2c-control-it6-rate-activated\": \"**Result: not reproduced.** Under R1, IT6 rates are 4.28 +/- 5.58 at rest and 0.95 +/- 3.13 activated; under R2, 6.27 +/- 5.75 and 4.87 +/- 5.57; neither has all four values within tolerance, though every test gives p below 0.001 under both. The R3 variant gives 5.82 +/- 5.78 and 3.47 +/- 5.19, all four within tolerance, with every test below 1e-10.\",\n\"control-it5-silenced-activated\": \"**Result: not reproduced.** IT5A and IT5B fire no spike in W in the activated file (the one IT5A and two IT5B units present fired before 0.05 s), so the zero rates hold, but the rest rates are 1.21 and 1.75 spikes/s under R1 and 3.57 and 3.58 under R2, against 3.3 and 3.1. The R3 variant gives 3.25 and 3.08, within tolerance.\",\n\"control-it4-rate-activated\": \"**Result: not reproduced.** IT4 rates are 0.037 and 0.586 spikes/s under R1 and 3.14 and 8.18 under R2, against 2.6 and 4.7. The R3 variant gives 2.57 and 4.74, within tolerance.\",\n\"pt5b-highest-rate\": \"**Result: blocked (methods_underspecified), as the criterion directs when the population readings disagree.** Among the seven excitatory types PT5B has the highest mean rate in all three files under R1, R2 and R3. Among all 15 populations PV5A is higher in all three under every reading (R1 22.51, 22.79 and 42.10 against PT5B 11.69, 14.24 and 29.68 spikes/s), and PV5B too under R1.\",\n\"control-cv-isi\": \"**Result: reproduced.** In W with cells of at least one ISI, the PT5B CV is 0.590 +/- 0.365 with 47.8% at or below 0.5 at rest and 0.610 +/- 0.301 with 25.7% activated; with at least two ISIs, 0.611 +/- 0.354 (45.9%) and 0.618 +/- 0.295 (24.7%). All six values are within tolerance under both. Over the whole 4.3 s no value is within tolerance.\",\n\"pd-cv-isi\": \"**Result: reproduced.** In W with cells of at least one ISI, the parkinsonian PT5B CV is 0.339 +/- 0.267 with 80.6% at or below 0.5 at rest and 0.184 +/- 0.191 with 93.8% activated; with at least two ISIs, 0.343 +/- 0.267 (80.4%) and 0.185 +/- 0.191 (93.8%). All six are within tolerance under both readings in W.\",\n\"pd-activated-vm-more-negative\": \"**Result: reproduced.** In W the mean PT5B potential over the 20 recorded cells is -60.84 mV in the control and -66.46 mV in the parkinsonian activated file (difference -5.62 mV), and the median -63.98 against -71.11 mV; every one of the 20 cells is lower in the parkinsonian file under both readings. The potentials of this set do not match its stored spikes in W (data check); in the other three sets, whose potentials do, the variant gives the same sign (table above).\",\n\"control-duty-cycle\": \"**Result: not reproduced.** No combination of readings puts both control values within tolerance. The closest, global half-height in 2.0 to 2.25 s with the total summary, gives 27.88% at rest (tolerance 27.9 to 34.1) and 46.49% activated (within). Over W the unsmoothed 2 ms SCH crosses half-height every 10 ms (median period), far shorter than the beta and gamma periods.\",\n\"pd-duty-cycle\": \"**Result: not reproduced.** No combination puts both parkinsonian values within tolerance; global half-height in 2.0 to 2.25 s with the total summary gives 26.42% at rest (within 26.1 to 31.9) but 36.45% activated (tolerance 22.5 to 27.5), and every other combination gives 34% or more for the activated state.\",\n\"fig3a-control-rest-spectrogram\": \"**Result: not reproduced.** Neither spectrogram reading has a local maximum of time-averaged power within 1 to 3 Hz (S1 decreases from 1 Hz), and the 15 to 25 Hz burst rate is 1.30 Hz (S1) and 0.96 Hz (S2), outside 1.53 to 1.87 Hz.\",\n\"fig3b-control-activated-spectrogram\": \"**Result: not reproduced.** Two parts hold under both readings: no 1 to 3 Hz maximum, and 15 to 20 Hz power lower than at rest (ratio 0.42 under S1, 0.57 under S2). The 14 to 16 Hz burst rate is 1.30 and 2.89 Hz (expected 1.5 +/- 0.15), the 25 to 35 Hz burst rate 1.30 and 0.96 Hz (within only under S2), its median duration 66.9 and 100 ms (expected 50 +/- 5), and 15 Hz bursts as short as 155 and 50 ms fall below 90 ms or as long as 557 ms above 550 ms.\",\n\"fig6a-pd-rest-spectrogram\": \"**Result: not reproduced.** The 25 to 35 Hz burst rate is 1.74 Hz (S1) and 1.45 Hz (S2), against 4.5 to 5.5 Hz, and burst durations reach outside 45 to 275 ms (42 ms under S1, 425 ms under S2). The 14 to 16 Hz power is above its half-height 83% of the time under S1 and 36% under S2.\",\n\"fig6b-pd-activated-spectrogram\": \"**Result: not reproduced.** The 20 to 35 Hz burst rate is 2.61 Hz (S1) and 2.89 Hz (S2), outside 9 to 22 Hz; the median burst duration, 65.1 and 75 ms, is within 22.5 to 110 ms.\",\n\"control-coincident-spikes\": \"**Result: not reproduced.** Under every reading 99.99% to 100% of control PT5B spikes have a spike of another PT5B cell within 1 ms, against 1% and 3%: the 1,435 PT5B cells fire 17 to 42 spikes per ms together. Among only the 20 recorded cells the share is still 24.8% to 72.8%. The paper's 1% to 3% cannot come from all PT5B cells with this definition.\",\n\"pd-coincident-spikes\": \"**Result: not reproduced.** Under every reading 99.95% to 100% of parkinsonian PT5B spikes are coincident, against 2% and 3%; among the 20 recorded cells, 27.0% to 72.2%.\",\n\"fig4-control-unitary-events\": \"**Result: not reproduced.** Under every reading no 100 ms window is significant (0 of 3,901 slid and 0 of 40 non-overlapping windows), so the significant duration is 0 s at rest and activated, against 0.7 and 1.1 s. In 95% to 100% of 1 ms bins two or more PT5B cells fire, so observed and expected coincidence counts are both about 100 per window and the test cannot find excess; the paper's analysis must have used fewer cells or another definition.\",\n\"fig7-pd-unitary-events\": \"**Result: not reproduced.** As for the control files, no window is significant under any reading (0 s against 3.1 and 1.4 s), with two or more PT5B spikes in 95% to 100% of 1 ms bins.\",\n\"rest-synchrony-increase\": \"**Result: not reproduced.** The significant synchrony at rest is 0 s in both the control and the parkinsonian file under every reading, so it is not larger in the parkinsonian file. The outcome follows from the two unitary-event claims, whose method finds nothing on these data.\",\n\"fig5c-pd-pt5b-rate-activated\": \"**Result: reproduced.** Under R1 parkinsonian PT5B rates are 14.24 +/- 7.13 at rest and 29.68 +/- 12.67 spikes/s activated, and under R2 14.70 +/- 6.76 and 30.57 +/- 11.75; all four are within tolerance under both, and every test gives p below 1e-200.\",\n\"fig5c-pd-it23-rate-activated\": \"**Result: not reproduced.** Under R1 parkinsonian IT2 rates are 0.025 +/- 0.239 and 0.164 +/- 1.598, under R2 1.163 +/- 1.173 and 6.163 +/- 7.769; neither reading has all four values within tolerance, and under R2 the paired tests give p = 0.26 and 0.18 (12 cells). The R3 variant gives 0.783 +/- 1.105 and 4.295 +/- 7.066, all four within tolerance, but only the Welch test is below 0.001 (Mann-Whitney 0.0018, paired 0.60 and 0.21 on 22 cells).\",\n\"pd-it5-silenced-activated\": \"**Result: not reproduced.** No IT5A or IT5B spike falls in W in the parkinsonian activated file, so the zero rates hold, but the rest rates are 0.47 and 0.47 spikes/s under R1 and 2.57 and 2.19 under R2, against 2.2 and 1.2. The R3 variant gives 2.17 and 1.25, within tolerance.\",\n\"pd-it6-rate-unchanged\": \"**Result: not reproduced.** Under R1 the IT6 rates are 1.33 and 1.73 spikes/s, outside tolerance, and three tests find a difference at p < 0.05 (Wilcoxon p = 0.0025, Mann-Whitney 0.00017, Welch 0.019); under R2 no test finds a difference (p 0.62 to 0.93, difference -0.155 spikes/s) but the means, 6.79 and 6.64, are outside 5.4 to 6.6. The R3 variant gives 6.00 and 5.99 with no test below 0.05 (smallest p 0.49).\",\n\"rest-pt5b-rate-pd-vs-control\": \"**Result: reproduced.** Under R1 the rest PT5B rate is 11.69 +/- 9.40 in the control and 14.24 +/- 7.13 spikes/s in the parkinsonian file, all four within tolerance; every test gives p below 1e-15, and the standard deviation is lower in the parkinsonian file. R2 also meets the criterion.\",\n\"rest-it4-rate-pd-vs-control\": \"**Result: not reproduced.** Under R1 both IT4 means are 0.037 spikes/s; under R2 they are 3.14 (9 cells) and 14.13 (2 cells), the control one outside tolerance; no reading has every test below 0.05 (R2 Wilcoxon p = 1.0, Welch 0.32). The R3 variant gives 2.57 and 14.13, within tolerance, but the parkinsonian value rests on 2 cells and no test reaches p < 0.05 (smallest 0.077).\",\n\"rest-it5a-rate-pd-vs-control\": \"**Result: not reproduced.** Under R1 the rest IT5A rates are 1.21 and 0.47 spikes/s; under R2 3.57 and 2.57, the parkinsonian value outside 1.98 to 2.42, and the unpaired tests give 0.017 and 0.012. The R3 variant gives 3.25 and 2.16, within tolerance, with every test below 0.01 (largest 0.0027).\",\n\"activated-pt5b-rate-pd-vs-control\": \"**Result: partially reproduced.** Under R1 the activated PT5B rate is 26.76 +/- 18.17 in the control and 29.68 +/- 12.67 spikes/s in the parkinsonian file, all four within tolerance, and the standard deviation is lower; the Wilcoxon, paired t and Welch tests give p from 1.6e-08 to 6.5e-07, but the Mann-Whitney test gives 0.0052, above 0.001. Under R2 the means are 30.60 and 30.57 and no test is below 0.05. The Discussion's statement of no significant change in the activated state holds under R2 and not under R1.\",\n\"activated-it6-rate-pd-vs-control\": \"**Result: not reproduced.** Under R1 the activated IT6 rates are 0.95 and 1.73 spikes/s, under R2 4.87 and 6.64, outside tolerance under both, though the rate is higher in the parkinsonian file (R1 tests p below 3e-05). The R3 variant gives 3.47 and 5.99, within tolerance, with every test below 1e-07.\",\n\"rest-beta-power-order-of-magnitude\": \"**Result: partially reproduced.** Parkinsonian rest LFP power around 15 Hz is far larger than control under every reading, but by more than the criterion's order of magnitude: the ratio is 129 (S1, at 15 Hz), 111 (S1, 14 to 16 Hz) and 65 (S2, both), above 31.6, so neither the criterion's reproduced range (3.16 to 31.6) nor its not-reproduced range (below 3.16) applies. The ratio of the spectrograms' maxima, a variant, is 21.2 under S1 and 3.0 under S2.\",\n\"activated-20-35hz-power-pd-vs-control\": \"**Result: reproduced.** Mean 20 to 35 Hz power is higher in the parkinsonian activated file under every reading: by a factor 4.55 for the LFP under S1, 4.71 under S2, and 11.8 for the PT5B SCH spectrum.\",\n}\n"
}
```

```
File created successfully at: /tmp/claude-1001/concl.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='concl.py'; s=open(p).read()
old="and 15 Hz bursts as short as 155 and 50 ms fall below 90 ms or as long as 557 ms above 550 ms."
new="and the 14 to 16 Hz burst durations span 155 to 557 ms under S1 and 50 to 300 ms under S2, each outside 90 to 550 ms at one end."
assert old in s; s=s.replace(old,new)
old="and three tests find a difference at p < 0.05 (Wilcoxon p = 0.0025, Mann-Whitney 0.00017, Welch 0.019)"
new="and all four tests find a difference at p < 0.05 (p 0.00017 to 0.019)"
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
EOF
cat > $TMPDIR/summary.md <<'EOF'
## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

| Claim | Outcome |
|---|---|
| fig1-network-size | not reproduced (only cells that fired are stored) |
| model-pt5b-excitability-decrease | blocked: data_missing |
| robustness-four-sets | blocked: methods_underspecified |
| fig2-control-rest-beta | reproduced |
| fig2-control-activated-gamma | reproduced |
| fig2c-control-pt5b-rate-activated | reproduced |
| fig2c-control-it23-rate-activated | not reproduced (matches under the R3 variant) |
| fig2c-control-it6-rate-activated | not reproduced (matches under R3) |
| control-it5-silenced-activated | not reproduced (matches under R3) |
| control-it4-rate-activated | not reproduced (matches under R3) |
| pt5b-highest-rate | blocked: methods_underspecified (population readings disagree) |
| control-cv-isi | reproduced |
| control-subthreshold-oscillations | blocked: methods_underspecified |
| control-duty-cycle | not reproduced |
| fig3a-control-rest-spectrogram | not reproduced |
| fig3b-control-activated-spectrogram | not reproduced |
| control-coincident-spikes | not reproduced |
| fig4-control-unitary-events | not reproduced |
| fig5-pd-rest-beta | reproduced |
| fig5-pd-activated-gamma | not reproduced |
| fig5c-pd-pt5b-rate-activated | reproduced |
| fig5c-pd-it23-rate-activated | not reproduced (values match under R3) |
| pd-it5-silenced-activated | not reproduced (matches under R3) |
| pd-it6-rate-unchanged | not reproduced (matches under R3) |
| pd-cv-isi | reproduced |
| pd-no-subthreshold-oscillations | blocked: methods_underspecified |
| pd-activated-vm-more-negative | reproduced |
| pd-duty-cycle | not reproduced |
| fig6a-pd-rest-spectrogram | not reproduced |
| fig6b-pd-activated-spectrogram | not reproduced |
| pd-coincident-spikes | not reproduced |
| fig7-pd-unitary-events | not reproduced |
| rest-pt5b-rate-pd-vs-control | reproduced |
| rest-it4-rate-pd-vs-control | not reproduced |
| rest-it5a-rate-pd-vs-control | not reproduced (matches under R3) |
| activated-pt5b-rate-pd-vs-control | partially reproduced |
| activated-it6-rate-pd-vs-control | not reproduced (matches under R3) |
| rest-beta-power-order-of-magnitude | partially reproduced |
| activated-20-35hz-power-pd-vs-control | reproduced |
| rest-synchrony-increase | not reproduced |

**How the analysis differs from the paper's.** The files hold one LFP trace, so only electrode
reading E1 was run, taking "LFP 0" as electrode 0; E2 (mean of 11 electrodes) could not be. The
spectrogram reading S2 uses a 250 ms window, since NetPyNE's own fft defaults cannot resolve
below 156 Hz. Population sizes for R1 come from the gid blocks, since silent cells are not stored.
The paper's IT rates match exactly when the denominator is the cells the file holds (R3, those
that fired at any time in the simulation); that reading is not among the claims file's, so it
does not decide an outcome here, and a reader is asked about it. The coincidence and
unitary-event analyses follow the claims file's definitions over all PT5B cells; with 17 to 42
PT5B spikes per ms these saturate, so the paper must have used another set of cells or another
definition, which it does not state.

**What was found about the dataset.** The units table holds only the cells that fired (2,917 to
4,480 of 10,073 M1 cells in the paper's set), where the description says spike trains of all
10,073 neurons. The paper's set holds 20 PT5B potentials per file, not 400, and those potentials
match their cells' stored spikes only in the first half second; in W they come from a run that
diverged from the stored spikes. `sub-001/sub-001.nwb` duplicates
`sub-001_ses-sM1-04-22-2024-01.nwb`. Each file holds one LFP trace with no electrode position.
The files' related publication is the preprint, the dandiset lists no related resource, and its
summary names spike sorting as the technique of a simulation.
EOF
cd entries/001444-doherty-2025 && . $TMPDIR/venv/bin/activate && python $TMPDIR/build_nb.py reproduce_doherty_2025.ipynb $TMPDIR/concl.py $TMPDIR/header.md $TMPDIR/summary.md && time jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 --output-dir $TMPDIR/exec --output dev.ipynb reproduce_doherty_2025.ipynb 2>&1 | tail -2
```

```
cells 119
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 628375 bytes to /tmp/claude-1001/exec/dev.ipynb

real	5m5.173s
user	0m42.297s
sys	0m3.308s
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && python - <<'EOF' > out2.txt
import nbformat
nb=nbformat.read('exec/dev.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type=='code':
        print(f'=== cell {i} tags={c.metadata.get("tags")}')
        for o in c.outputs:
            if 'text' in o: print(o['text'])
            elif o.get('output_type')=='error': print('ERROR', o['ename'], o['evalue'])
EOF
grep -n "ERROR" out2.txt; sed -n '/cell 7 /,/cell 13 /p' out2.txt | grep -v "^IT\|^SOM\|^PV\|^TPO\|^TVL\|^S[12] \|^cM1\|^M2\|^OC\|^CT6"; sed -n '/cell 53 /,/cell 56 /p' out2.txt | tail -12
```

```
=== cell 7 tags=['sanity']
Units in the paper's set, by population (M1 populations, then inputs):
       control rest  parkinsonian rest  control activated  parkinsonian activated
PT5B           1435               1435               1435                    1435

M1 units per file: {'01': 4480, '02': 3231, '03': 2919, '04': 2917}
Lowest input gid: 10073 ; highest M1 gid: 10064

Population gid blocks bounded from the gids seen in all 16 files (start in [low, high], end in [low, high], size min and max):
       start_low  start_high  end_low  end_high  n_min  n_max
PT5B        5130        5130     6564      6564   1435   1435
Observed gid ranges of the populations overlap nowhere: True ; gids never seen, between blocks: 24 ; sum of smallest sizes + unseen gids: 10073
A gid has the same population in all four files of the set: True

=== cell 9 tags=['sanity']
                     traces  all_PT5B  Vm_spikes  unit_spikes  matched_0_05s  matched_05_2s  matched_2_43s  vm_min  vm_max
set            file                                                                                                       
sM1-04-22-2024 01        20      True       1064         1064          1.000          1.000          1.000 -80.591  27.187
               02        20      True       1530         1530          1.000          1.000          1.000 -86.646  32.775
               03        20      True       2700         2700          1.000          1.000          1.000 -79.751  27.612
[... 29 more lines not kept]
```

**Agent**

All outputs as expected. Updating the Vm conclusion with the variant numbers, then writing the entry files.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='concl.py'; s=open(p).read()
old="in the other three sets, whose potentials do, the variant gives the same sign (table above)."
new="in the other three sets, whose potentials do, the parkinsonian potential is lower in 39, 39 and 40 of 40 cells by the mean (by 4.98 to 5.67 mV) and in 40 of 40 by the median."
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
EOF
cd entries/001444-doherty-2025
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
name: 001444-doherty-2025
type: reproduction
title: Simulated parkinsonian mouse M1 (Doherty et al. 2025)
description: Tests the findings of Doherty, Chen, Smith, Wichmann, Chu and Lytton (2025) on dandiset
  001444, which holds four sets of four NetPyNE simulations of mouse primary motor cortex in the
  control and parkinsonian conditions, at rest and activated. It compares firing rates, ISI
  variability, dominant frequencies, duty cycles, LFP spectrograms, PT5B coincident firing and
  membrane potentials between conditions, on the set the paper reports.
license: Apache-2.0
notebooks:
- path: reproduce_doherty_2025.ipynb
  title: Reproducing Doherty et al. (2025) from dandiset 001444
  runtime_minutes: 6
helpers:
- m1sim.py
related:
- id: dandi:001444/0.250805.2002
  relation: uses_data
- id: doi:10.1038/s41531-025-01070-4
  relation: reproduces
EOF
. $TMPDIR/venv/bin/activate && python $TMPDIR/build_nb.py reproduce_doherty_2025.ipynb $TMPDIR/concl.py $TMPDIR/header.md $TMPDIR/summary.md; cd  && python tools/entry.py lock entries/001444-doherty-2025 && python tools/entry.py check entries/001444-doherty-2025 2>&1 | tail -20; date -u
```

```
cells 119
wrote entries/001444-doherty-2025/requirements.lock.txt
0 error(s)
Mon Nov  2 17:27:17 UTC 2026
```

**Agent**

Entry check passes. Running the entry from a clean environment.

**Agent calls Bash**

```bash
time python tools/entry.py all entries/001444-doherty-2025 2>&1 | tail -8
```

```
Installed kernelspec registry-001444-doherty-2025 in executed/001444-doherty-2025/.venv/share/jupyter/kernels/registry-001444-doherty-2025
0 error(s)
pass  reproduce_doherty_2025.ipynb  (320 s)

real	5m26.697s
user	0m51.630s
sys	0m6.124s
```

**Agent**

Passes in 320 s. Confirming the executed copy's numbers match the development run.

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && python - <<'EOF' > out3.txt
import nbformat
nb=nbformat.read('executed/001444-doherty-2025/reproduce_doherty_2025.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type=='code':
        print(f'=== cell {i} tags={c.metadata.get("tags")}')
        for o in c.outputs:
            if 'text' in o: print(o['text'])
            elif o.get('output_type')=='error': print('ERROR', o['ename'], o['evalue'])
EOF
diff out2.txt out3.txt | head -20
```

```
317a318
> 
329d329
< 
619d618
< 
700d698
< 
743c741
< notebook ran in 301 s
---
> notebook ran in 311 s
Shell cwd was reset to
```

**Agent**

Identical. Now the questions file and the attempt record; checking the questions format.

**Agent calls Bash**

```bash
cd  ls schemas; head -40 questions/000005.yaml; python -c "import json;d=json.load(open('schemas/questions.schema.json'));print(json.dumps(d,indent=0)[:2500])" 2>/dev/null || ls schemas
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
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
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;d=json.load(open('schemas/attempt.schema.json'))
print(d.get('required')); 
for k,v in d['properties'].items():
  if k!='outcomes': print(k, json.dumps(v)[:600])
"
```

```
['schema_version', 'id', 'dataset', 'paper', 'date', 'provenance', 'outcomes']
schema_version {"const": 2}
id {"type": "string", "pattern": "^[a-z0-9]+(-[a-z0-9]+)*$"}
dataset {"description": "The dataset the attempt tested: the archive and the dataset's identifier there.", "type": "object", "additionalProperties": false, "required": ["archive", "id", "version"], "properties": {"archive": {"description": "The archive that holds the dataset, in lower case: dandi, ebrains, openneuro, dryad, zenodo, figshare and so on.", "type": "string", "pattern": "^[a-z][a-z0-9-]*$"}, "id": {"description": "The dataset's identifier in that archive, e.g. 000003 on DANDI.", "type": "string", "minLength": 1}, "version": {"description": "The version the attempt read, e.g. 0.220127.0436,
paper {"type": "string", "pattern": "^doi:10\\.[0-9]{4,9}/.+$"}
date {"type": "string", "format": "date"}
entry {"description": "The entry this attempt produced (its name), if any.", "type": "string"}
deprecated {"description": "Set when the attempt no longer stands, for example because its claims were written without the paper's full text. The record is kept as it was; its outcomes are shown but not counted.", "type": "object", "additionalProperties": false, "required": ["date", "reason"], "properties": {"date": {"type": "string", "format": "date"}, "reason": {"type": "string", "minLength": 1}, "superseded_by": {"description": "The id of the attempt that replaces it, once there is one.", "type": "string"}}}
provenance {"type": "object", "additionalProperties": false, "required": ["kind", "accountable"], "properties": {"kind": {"enum": ["agent", "person"]}, "accountable": {"description": "The person or organisation responsible for this attempt.", "type": "object", "additionalProperties": false, "required": ["name"], "properties": {"name": {"type": "string"}, "orcid": {"type": "string", "pattern": "^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]$"}, "ror": {"type": "string"}}}, "agent": {"description": "Requir
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;d=json.load(open('schemas/attempt.schema.json'))
print(json.dumps(d['properties']['provenance'])[600:2000])"
```

```
"protocol"], "properties": {"harness": {"type": "string"}, "model": {"type": "string"}, "protocol": {"description": "Version of the reproduction protocol the agent followed.", "type": "string"}}}, "runner": {"description": "Where the attempt was run: the platform, and the run that wrote this record. Its other runs (verification rounds, revisions) are linked from their transcripts.", "type": "object", "additionalProperties": false, "required": ["platform"], "properties": {"platform": {"description": "The platform that ran it, e.g. GitHub Actions, or local for a person's machine.", "type": "string", "minLength": 1}, "url": {"description": "The run that wrote the record, e.g. https://github.com/<owner>/<repo>/actions/runs/<id>.", "type": "string", "pattern": "^https://"}}}}}
```

**Agent**

Writing the question for a reader (the R3 denominator) and the attempt record.

**Agent calls Write**

```json
{
 "file_path": "questions/001444.yaml",
 "content": "dandiset: \"001444\"\npaper: doi:10.1038/s41531-025-01070-4\nquestions:\n- claim: fig2c-control-it23-rate-activated\n  asked: 2026-11-02\n  question: The claims file reads the population rates in two ways, R1 (all cells of the\n    population, silent ones at 0) and R2 (cells with at least one spike in the last 2.3 s). Does\n    the paper's text also allow a third reading, R3, the cells that fired at least once in the\n    4.3 s simulation, with rates over the last 2.3 s? If so, should R3 be added to the readings of\n    the rate claims? The same question applies to fig2c-control-it6-rate-activated,\n    control-it5-silenced-activated, control-it4-rate-activated, fig5c-pd-it23-rate-activated,\n    pd-it5-silenced-activated, pd-it6-rate-unchanged, rest-it4-rate-pd-vs-control,\n    rest-it5a-rate-pd-vs-control, activated-it6-rate-pd-vs-control and pt5b-highest-rate.\n  passage: Statistically significant change was found for firing rates for excitatory cell types\n    going from rest to activated ... (mean, std dev, range shown; *** p < 0.001; #, truncated\n    maximum rate 73 spikes/s; calculated from the last 2.3 s of 4.3 s simulation to avoid\n    initialization transients). (Fig. 2C legend; also Fig. 5C legend.) The paper does not say\n    which cells enter a population's mean, and the dandiset's units tables hold only the cells that\n    fired at some time in the simulation.\n  why: Under R1 and R2 none of the IT claims has its values within tolerance (for example IT2 at\n    control rest, 0.095 and 1.555 spikes/s against 1.2). Under R3 every IT value the claims give\n    is matched to the printed decimal, including the standard deviations (IT2 1.203 +/- 1.649 and\n    6.662 +/- 8.858 against 1.2 +/- 1.6 and 6.7 +/- 8.9; IT6 5.82, IT5A 3.25, IT5B 3.08, IT4 2.57,\n    parkinsonian IT2 0.783 +/- 1.105 and 4.295 +/- 7.066). For PT5B all 1,435 cells fire, so R1\n    and R3 coincide and match. Eleven claims are not reproduced under R1 and R2 and would be\n    decided again under R3; their tests under R3 are in the notebook.\n"
}
```

```
File created successfully at: questions/001444.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='questions/001444.yaml'; s=open(p).read()
s=s.replace("  passage: Statistically","  passage: >-\n    Statistically")
open(p,'w').write(s)
import yaml; d=yaml.safe_load(open(p)); print(d['questions'][0]['passage'][:400])
EOF
```

```
Statistically significant change was found for firing rates for excitatory cell types going from rest to activated ... (mean, std dev, range shown; *** p < 0.001; #, truncated maximum rate 73 spikes/s; calculated from the last 2.3 s of 4.3 s simulation to avoid initialization transients). (Fig. 2C legend; also Fig. 5C legend.) The paper does not say which cells enter a population's mean, and the d
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='questions/001444.yaml'; s=open(p).read()
old="""and R3 coincide and match. Eleven claims are not reproduced under R1 and R2 and would be
    decided again under R3; their tests under R3 are in the notebook."""
new="""and R3 coincide and match. Ten claims are not reproduced under R1 and R2, and
    pt5b-highest-rate is blocked; they would be decided again under R3, whose values and tests are
    in the notebook as a variant."""
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
import yaml; yaml.safe_load(open(p))
EOF
date -u
```

```
Mon Nov  2 17:33:54 UTC 2026
```

**Agent**

Now the attempt record.

**Agent calls Write**

```json
{
 "file_path": "attempts/001444-doherty-2025-01.yaml",
 "content": "schema_version: 2\nid: 001444-doherty-2025-01\ndataset:\n  archive: dandi\n  id: \"001444\"\n  version: 0.250805.2002\n  doi: 10.48324/dandi.001444/0.250805.2002\npaper: doi:10.1038/s41531-025-01070-4\ndate: 2026-11-02\nentry: 001444-doherty-2025\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-13\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/41486399888\ninputs:\n- what: The Morlet spectrogram of NetPyNE 1.0.5 (netpyne/support/morlet.py) and the defaults of\n    netpyne.analysis.lfp.prepareSpectrogram, copied into the helper for spectrogram reading S1.\n    Software the Methods name, not data.\n  source: https://pypi.org/project/netpyne/1.0.5/ (netpyne-1.0.5-py2.py3-none-any.whl)\noutcomes:\n- claim: fig1-network-size\n  outcome: not_reproduced\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:fig1-network-size\n  measured: 4480\n  notes: The four files of set sM1_12-12-2023 hold 4,480, 3,231, 2,919 and 2,917 M1 units, against\n    10,073, because the units table stores only cells that fired. All 15 M1 populations are\n    present and the input generators start at gid 10073, so the gid numbering is consistent with\n    10,073 M1 cells (gids 0 to 10072); the gid blocks seen in all 16 files account for 10,049 cells\n    with 24 gids never seen between blocks. The model's size is not in doubt; the dataset does not\n    hold the silent cells the criterion counts.\n  deviations:\n  - The claims file's count assumes the files hold every cell, as the dandiset description says;\n    they do not, so the gid range is shown as a variant.\n- claim: model-pt5b-excitability-decrease\n  outcome: blocked\n  blocked_by: data_missing\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:model-pt5b-excitability-decrease\n  notes: The dandiset holds only the 16 network simulations (and one duplicate); no single-cell\n    current-injection simulations of the control or parkinsonian PT5B model are in it, and the\n    supplement that gives the protocol (Supplementary Fig. 1) was not available.\n- claim: robustness-four-sets\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:robustness-four-sets\n  notes: The claims file gives no measures, values or rule for this claim (Supplementary Table 2 was\n    not available), so it is blocked as its criterion says. The measures are reported per set\n    without an outcome. In the other three sets, PT5B rates are 11.3 to 13.4 spikes/s at control\n    rest, 19.1 to 24.6 at parkinsonian rest, 25.7 to 26.6 control activated and 29.1 to 30.7\n    parkinsonian activated; the PT5B SCH peaks at 17 to 19 Hz at control rest, 15 to 16 Hz at\n    parkinsonian rest, 40 to 42 Hz control activated and 28 to 31 Hz parkinsonian activated; the\n    parkinsonian over control ratio of 14 to 16 Hz LFP power at rest (S1) is 65.5, 11.5 and 7.0,\n    against 111.0 in the paper's set.\n- claim: fig2-control-rest-beta\n  outcome: reproduced\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:fig2-control-rest-beta\n  measured: 19\n  notes: The PT5B SCH spectrum in W peaks at 19 Hz searched above 0 Hz and above 5 Hz. The LFP\n    variant peaks at 1 Hz above 0 Hz and at 19 Hz above 5 Hz.\n  deviations:\n  - The files hold one LFP trace (\"LFP 0\"), taken as electrode 0 (reading E1); the mean over 11\n    electrodes (E2) cannot be computed. The LFP is a variant here.\n- claim: fig2-control-activated-gamma\n  outcome: reproduced\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:fig2-control-activated-gamma\n  measured: 44\n  notes: The PT5B SCH spectrum in W peaks at 44 Hz under both search ranges. The LFP variant peaks\n    at 1 Hz and 13 Hz.\n  deviations:\n  - Only one LFP trace (E1) is in the files; E2 cannot be computed.\n- claim: fig2c-control-pt5b-rate-activated\n  outcome: reproduced\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:fig2c-control-pt5b-rate-activated\n  measured:\n  - 11.69\n  - 9.40\n  - 26.76\n  - 18.17\n  notes: Under R1, 11.69 +/- 9.40 spikes/s at rest and 26.76 +/- 18.17 activated, all within\n    tolerance; T1 to T4 give p from 2.7e-116 down to 5.4e-147 (Mann-Whitney 2.2e-99). Under R2 the\n    activated values (30.60 +/- 16.13) are outside tolerance. All 1,435 PT5B cells are in every\n    file.\n  deviations:\n  - R1 needs the population size, which the files do not state; PT5B is the gid block 5130 to 6564\n    (1,435 cells), bounded exactly by the gids seen.\n- claim: fig2c-control-it23-rate-activated\n  outcome: not_reproduced\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:fig2c-control-it23-rate-activated\n  measured:\n  - 0.095\n  - 0.565\n  - 0.262\n  - 2.172\n  notes: Under R1 IT2 rates are 0.095 +/- 0.565 and 0.262 +/- 2.172 spikes/s, under R2 1.555 +/-\n    1.723 and 8.883 +/- 9.220; neither reading has all four values within tolerance, and neither\n    has all four tests below 0.001 (R1 Wilcoxon 0.69). The R3 variant (cells the file holds, those\n    that fired at least once in the simulation) gives 1.203 +/- 1.649 and 6.662 +/- 8.858, all\n    within tolerance; there the unpaired tests give 3.5e-05 and 3.6e-06 and the paired ones 0.016\n    and 0.011 (25 cells in both files). Whether R3 should be a reading is asked of a reader\n    (questions/001444.yaml).\n  deviations:\n  - R1 uses the IT2 gid block bounded from the data (1,729 or 1,730 cells); both bounds give the\n    same values to three decimals.\n- claim: fig2c-control-it6-rate-activated\n  outcome: not_reproduced\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:fig2c-control-it6-rate-activated\n  measured:\n  - 4.28\n  - 5.58\n  - 0.95\n  - 3.13\n  notes: Under R1 IT6 rates are 4.28 +/- 5.58 and 0.95 +/- 3.13, under R2 6.27 +/- 5.75 and 4.87 +/-\n    5.57, so no reading has the four values within tolerance, though every test finds the decrease\n    at p below 0.001 under both. The R3 variant gives 5.82 +/- 5.78 and 3.47 +/- 5.19, all four\n    within tolerance, every test below 1e-10. Asked of a reader (questions/001444.yaml).\n- claim: control-it5-silenced-activated\n  outcome: not_reproduced\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:control-it5-silenced-activated\n  measured:\n  - 1.21\n  - 1.75\n  - 0\n  - 0\n  notes: No IT5A or IT5B spike falls in W in the activated file (the one IT5A and two IT5B units in\n    it fired before 0.05 s), so the activated zeros hold. The rest rates are 1.21 and 1.75 spikes/s\n    under R1 and 3.57 and 3.58 under R2, against 3.3 and 3.1. The R3 variant gives 3.25 and 3.08,\n    within tolerance. Asked of a reader.\n- claim: control-it4-rate-activated\n  outcome: not_reproduced\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:control-it4-rate-activated\n  measured:\n  - 0.037\n  - 0.586\n  notes: IT4 rates are 0.037 and 0.586 spikes/s under R1 and 3.14 (9 cells) and 8.18 (55 cells)\n    under R2. The R3 variant gives 2.57 (11 cells) and 4.74 (95 cells), within tolerance. Asked of\n    a reader.\n- claim: pt5b-highest-rate\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:pt5b-highest-rate\n  notes: The criterion blocks the claim when its two population readings disagree, and they do.\n    Among the seven excitatory types PT5B has the highest mean in control rest, parkinsonian rest\n    and parkinsonian activated under R1, R2 and R3. Among all 15 populations PV5A is higher in all\n    three under every reading (R1 22.51, 22.79 and 42.10 spikes/s against PT5B 11.69, 14.24 and\n    29.68), and PV5B also under R1 (16.66, 17.37 and 36.16). The Results' context (rates of\n    excitatory cell types in Figs. 2C and 5C) supports the excitatory reading, but the paper does\n    not say which populations \"any\" covers; the question is for the authors (findings).\n- claim: control-cv-isi\n  outcome: reproduced\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:control-cv-isi\n  measured:\n  - 0.611\n  - 0.354\n  - 45.9\n  - 0.618\n  - 0.295\n  - 24.7\n  notes: In W, with cells of at least two ISIs, 0.611 +/- 0.354 (45.9% regular) at rest and 0.618\n    +/- 0.295 (24.7%) activated; with at least one ISI, 0.590 +/- 0.365 (47.8%) and 0.610 +/- 0.301\n    (25.7%), the paper's values to the printed decimal. Both readings in W have all six values\n    within tolerance; over 0 to 4.3 s none is. NetPyNE's own statistic (cells with more than 10\n    spikes, a variant) misses one value (54.4% regular at rest).\n- claim: control-subthreshold-oscillations\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:control-subthreshold-oscillations\n  notes: Neither the paper nor its code gives a rule for detecting a subthreshold oscillation or the\n    cells over which the 57.4% is taken (claims file). The paper's set holds the potentials of 20\n    of the 1,435 PT5B cells per file; 57.4% of 20 is 11.48, not a whole number of cells, so the\n    percentage was not taken over these 20. In W these potentials also do not match the stored\n    spikes of the same cells (findings).\n- claim: control-duty-cycle\n  outcome: not_reproduced\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:control-duty-cycle\n  measured:\n  - 37.53\n  - 44.99\n  notes: Under none of the eight combinations are both values within tolerance. Measured is the\n    first combination (global half-height, 2.0 to 2.25 s, mean of periods). The closest is global\n    half-height in 2.0 to 2.25 s with the total summary, 27.88% at rest (tolerance from 27.9) and\n    46.49% activated (within). On the unsmoothed 2 ms SCH the half-height is crossed every 10 ms\n    (median period over W), much shorter than a beta or gamma period, so the duty cycles depend on\n    noise in the histogram; the paper does not say whether it smoothed it.\n- claim: fig3a-control-rest-spectrogram\n  outcome: not_reproduced\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:fig3a-control-rest-spectrogram\n  measured: 1.30\n  notes: Neither reading has a local maximum of time-averaged power in 1 to 3 Hz (under S1 power\n    falls from 1 Hz), and the 15 to 25 Hz burst rate is 1.30 Hz (S1, 3 bursts) and 0.96 Hz (S2),\n    outside 1.53 to 1.87 Hz. The paper does not define a burst; the half-height reading is the\n    claims file's.\n  deviations:\n  - Only one LFP trace (E1) is in the files; E2 cannot be computed.\n  - S2 uses a 250 ms Hann window with 90% overlap, a standard choice; NetPyNE's fft defaults\n    (256 samples at 40 kHz) have a 156 Hz frequency step and cannot resolve the bands.\n- claim: fig3b-control-activated-spectrogram\n  outcome: not_reproduced\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:fig3b-control-activated-spectrogram\n  measured:\n  - 1.30\n  - 1.30\n  - 66.9\n  notes: Two parts hold under both readings, no 1 to 3 Hz maximum and lower 15 to 20 Hz power than\n    at rest (ratio 0.42 under S1, 0.57 under S2). The 14 to 16 Hz burst rate is 1.30 and 2.89 Hz,\n    the 25 to 35 Hz burst rate 1.30 and 0.96 Hz (within only under S2), its median duration 66.9\n    and 100 ms against 50 +/- 5, and the 14 to 16 Hz bursts last 155 to 557 ms (S1) and 50 to 300\n    ms (S2), outside 90 to 550 ms. Measured values are under S1.\n  deviations:\n  - Only one LFP trace (E1) is in the files; S2 uses a 250 ms window (see fig3a).\n- claim: control-coincident-spikes\n  outcome: not_reproduced\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:control-coincident-spikes\n  measured:\n  - 100.0\n  - 100.0\n  notes: Under all six combinations 99.99% to 100% of PT5B spikes have a spike of another PT5B cell\n    within 1 ms, against 1% and 3%. The 1,435 PT5B cells fire 17.0 (rest) and 42.3 (activated)\n    spikes per ms together, so with the paper's definition over the whole population nearly every\n    spike is coincident. Among the 20 cells with recorded potentials (a variant) the share is 24.8%\n    to 72.8%. The paper's 1% to 3% must come from a smaller set of cells or another definition,\n    which it does not state (findings).\n- claim: fig4-control-unitary-events\n  outcome: not_reproduced\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:fig4-control-unitary-events\n  notes: Under all eight combinations no 100 ms window is significant (0 of 3,901 slid windows, 0\n    of 40 non-overlapping), so the significant duration is 0 s at rest and activated, against 0.7\n    and 1.1 s, and no periodicity can be measured. Two or more PT5B cells fire in 96.5% to 100% of\n    1 ms bins, so the observed and expected coincidence counts are both about 100 per window. The\n    method of the claims file cannot find excess synchrony over the whole PT5B population; the\n    paper does not say which cells it analysed (findings).\n- claim: fig5-pd-rest-beta\n  outcome: reproduced\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:fig5-pd-rest-beta\n  measured: 15\n  notes: The PT5B SCH spectrum peaks at 15 Hz under both search ranges; the LFP variant also at 15\n    Hz.\n  deviations:\n  - Only one LFP trace (E1) is in the files; E2 cannot be computed.\n- claim: fig5-pd-activated-gamma\n  outcome: not_reproduced\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:fig5-pd-activated-gamma\n  measured: 27\n  notes: The parkinsonian activated PT5B SCH spectrum peaks at 27 Hz under both search ranges,\n    outside 38.7 to 47.3 Hz; its next local maxima are 30 Hz (0.43 of the peak's power) and 21 Hz\n    (0.39). The LFP variant also peaks at 27 Hz. In the other three sets the parkinsonian activated\n    SCH peaks at 28 to 31 Hz.\n  deviations:\n  - Only one LFP trace (E1) is in the files; E2 cannot be computed.\n- claim: fig5c-pd-pt5b-rate-activated\n  outcome: reproduced\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:fig5c-pd-pt5b-rate-activated\n  measured:\n  - 14.24\n  - 7.13\n  - 29.68\n  - 12.67\n  notes: Under R1 14.24 +/- 7.13 and 29.68 +/- 12.67 spikes/s, under R2 14.70 +/- 6.76 and 30.57 +/-\n    11.75, all within tolerance under both; every test gives p below 1e-200.\n- claim: fig5c-pd-it23-rate-activated\n  outcome: not_reproduced\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:fig5c-pd-it23-rate-activated\n  measured:\n  - 0.025\n  - 0.239\n  - 0.164\n  - 1.598\n  notes: Under R1 0.025 +/- 0.239 and 0.164 +/- 1.598, under R2 1.163 +/- 1.173 and 6.163 +/- 7.769;\n    neither has all four within tolerance, and under R2 the paired tests give 0.26 and 0.18 (12\n    cells). The R3 variant gives 0.783 +/- 1.105 and 4.295 +/- 7.066, all within tolerance, but\n    only the Welch test is below 0.001 there (1.7e-04; Mann-Whitney 0.0018, paired 0.60 and 0.21 on\n    22 cells). Asked of a reader.\n- claim: pd-it5-silenced-activated\n  outcome: not_reproduced\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:pd-it5-silenced-activated\n  measured:\n  - 0.47\n  - 0.47\n  - 0\n  - 0\n  notes: No IT5A or IT5B spike falls in W in the parkinsonian activated file, so the zeros hold; the\n    rest rates are 0.47 and 0.47 under R1 and 2.57 and 2.19 under R2, against 2.2 and 1.2. The R3\n    variant gives 2.17 and 1.25, within tolerance. Asked of a reader.\n- claim: pd-it6-rate-unchanged\n  outcome: not_reproduced\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:pd-it6-rate-unchanged\n  measured:\n  - 1.33\n  - 1.73\n  notes: A claim of absence. Under R1 the means, 1.33 and 1.73 spikes/s, are outside tolerance and\n    all four tests find a difference at p < 0.05 (0.00017 to 0.019; activated higher by 0.40\n    spikes/s). Under R2 no test finds a difference (p 0.62 to 0.93, difference -0.155) but the\n    means, 6.79 and 6.64, are outside 5.4 to 6.6. The R3 variant gives 6.00 and 5.99 with no test\n    below 0.05 (smallest 0.49), which would meet the criterion. Asked of a reader.\n  deviations:\n  - The paper names no test or threshold for this absence; the claims file's p < 0.05 under T1 to\n    T4 is used.\n- claim: pd-cv-isi\n  outcome: reproduced\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:pd-cv-isi\n  measured:\n  - 0.343\n  - 0.267\n  - 80.4\n  - 0.185\n  - 0.191\n  - 93.8\n  notes: In W with at least two ISIs 0.343 +/- 0.267 (80.4% regular) and 0.185 +/- 0.191 (93.8%);\n    with at least one ISI 0.339 +/- 0.267 (80.6%) and 0.184 +/- 0.191 (93.8%). All six values are\n    within tolerance under both readings in W.\n- claim: pd-no-subthreshold-oscillations\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:pd-no-subthreshold-oscillations\n  notes: Depends on control-subthreshold-oscillations, blocked for want of a detection rule; the\n    same 20 PT5B potentials per file are available.\n- claim: pd-activated-vm-more-negative\n  outcome: reproduced\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:pd-activated-vm-more-negative\n  notes: In W the mean potential over the 20 recorded PT5B cells is -60.84 mV in the control and\n    -66.46 mV in the parkinsonian activated file (difference -5.62 mV), and the median -63.98 and\n    -71.11 mV (difference -7.13); all 20 cells are lower in the parkinsonian file under both\n    readings (Wilcoxon p = 1.9e-06). The potentials of this set do not match the stored spikes in W\n    (findings); in the three other sets, whose potentials do, the first 40 cells are lower in the\n    parkinsonian file in 39, 39 and 40 of 40 by the mean (by 4.98 to 5.67 mV) and 40 of 40 by the\n    median.\n  deviations:\n  - The paper's set holds 20 PT5B potentials, not the 400 the dandiset describes.\n- claim: pd-duty-cycle\n  outcome: not_reproduced\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:pd-duty-cycle\n  measured:\n  - 48.53\n  - 41.51\n  notes: No combination puts both values within tolerance. Measured is the first combination\n    (global half-height, 2.0 to 2.25 s, mean of periods). Global half-height in 2.0 to 2.25 s with\n    the total summary gives 26.42% at rest (within 26.1 to 31.9) and 36.45% activated (tolerance\n    22.5 to 27.5); every combination gives 36% or more for the activated state.\n- claim: fig6a-pd-rest-spectrogram\n  outcome: not_reproduced\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:fig6a-pd-rest-spectrogram\n  measured: 1.74\n  notes: The 25 to 35 Hz burst rate is 1.74 Hz (S1) and 1.45 Hz (S2), against 4.5 to 5.5 Hz; burst\n    durations run 42 to 160 ms (S1) and 50 to 425 ms (S2), each outside 45 to 275 ms at one end.\n    The 14 to 16 Hz power is above its half-height 83% of the time under S1 and 36% under S2.\n  deviations:\n  - Only one LFP trace (E1) is in the files; S2 uses a 250 ms window (see fig3a).\n- claim: fig6b-pd-activated-spectrogram\n  outcome: not_reproduced\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:fig6b-pd-activated-spectrogram\n  notes: The 20 to 35 Hz burst rate is 2.61 Hz (S1) and 2.89 Hz (S2), outside 9 to 22 Hz; the median\n    burst duration, 65.1 and 75 ms, is within 22.5 to 110 ms.\n  deviations:\n  - Only one LFP trace (E1) is in the files; S2 uses a 250 ms window (see fig3a).\n- claim: pd-coincident-spikes\n  outcome: not_reproduced\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:pd-coincident-spikes\n  measured:\n  - 100.0\n  - 100.0\n  notes: Under all six combinations 99.95% to 100% of parkinsonian PT5B spikes are coincident,\n    against 2% and 3% (19.9 and 42.5 PT5B spikes per ms). Among the 20 recorded cells the share is\n    27.0% to 72.2%. See control-coincident-spikes.\n- claim: fig7-pd-unitary-events\n  outcome: not_reproduced\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:fig7-pd-unitary-events\n  notes: As for the control files, no window is significant under any combination (0 s against 3.1\n    and 1.4 s), with two or more PT5B spikes in 95.2% to 100% of 1 ms bins. See\n    fig4-control-unitary-events.\n- claim: rest-pt5b-rate-pd-vs-control\n  outcome: reproduced\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:rest-pt5b-rate-pd-vs-control\n  notes: Under R1 11.69 +/- 9.40 (control) and 14.24 +/- 7.13 spikes/s (parkinsonian), all within\n    tolerance, every test p below 1e-15 (paired by gid, 1,435 cells), and the standard deviation is\n    lower in the parkinsonian file. R2 also meets the criterion.\n- claim: rest-it4-rate-pd-vs-control\n  outcome: not_reproduced\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:rest-it4-rate-pd-vs-control\n  measured:\n  - 0.037\n  - 0.037\n  notes: Under R1 both means are 0.037 spikes/s; under R2 3.14 (9 cells) and 14.13 (2 cells), the\n    control value outside tolerance; no reading has every test below 0.05. The R3 variant gives\n    2.57 and 14.13, within tolerance, but the parkinsonian value rests on 2 cells and no test\n    reaches 0.05 (smallest 0.077), so it would still fail.\n- claim: rest-it5a-rate-pd-vs-control\n  outcome: not_reproduced\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:rest-it5a-rate-pd-vs-control\n  measured:\n  - 1.21\n  - 0.47\n  notes: Under R1 1.21 and 0.47 spikes/s (every test below 0.01); under R2 3.57 and 2.57, the\n    parkinsonian value outside 1.98 to 2.42, unpaired tests 0.017 and 0.012. The R3 variant gives\n    3.25 and 2.16, within tolerance, with every test below 0.01 (largest 0.0027). Asked of a reader.\n- claim: activated-pt5b-rate-pd-vs-control\n  outcome: partially_reproduced\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:activated-pt5b-rate-pd-vs-control\n  notes: Under R1 26.76 +/- 18.17 (control) and 29.68 +/- 12.67 spikes/s (parkinsonian), all four\n    within tolerance, standard deviation lower; Wilcoxon, paired t and Welch give p 3.2e-07, 1.6e-08\n    and 6.5e-07, but Mann-Whitney gives 0.0052, above the 0.001 the criterion asks under every\n    test. The increase is present, with one of four tests weaker than the paper's bound. Under R2\n    the means are 30.60 and 30.57 and no test is below 0.05. The Discussion's statement of no\n    significant change in the activated state holds under R2 and not under R1.\n- claim: activated-it6-rate-pd-vs-control\n  outcome: not_reproduced\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:activated-it6-rate-pd-vs-control\n  measured:\n  - 0.95\n  - 1.73\n  notes: Under R1 0.95 and 1.73 spikes/s, under R2 4.87 and 6.64, outside tolerance under both,\n    though the parkinsonian rate is higher (R1 tests p below 3e-05). The R3 variant gives 3.47 and\n    5.99, within tolerance, with every test below 1e-07. Asked of a reader.\n- claim: rest-beta-power-order-of-magnitude\n  outcome: partially_reproduced\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:rest-beta-power-order-of-magnitude\n  notes: The parkinsonian over control ratio of rest LFP power is 129 (S1, at 15 Hz), 111 (S1, 14 to\n    16 Hz) and 65 (S2, both measures), above the criterion's 3.16 to 31.6 under every reading. The\n    criterion names a range for reproduced and one for not reproduced (below 3.16) and none for a\n    larger increase; the increase is present and about two orders of magnitude, so the outcome is\n    partially reproduced. The ratio of the spectrograms' maxima (the colour bars of Figs. 3 and 6),\n    a variant, is 21.2 under S1 and 3.0 under S2. In the other three sets the S1 ratio at 14 to 16\n    Hz is 65.5, 11.5 and 7.0.\n  deviations:\n  - Only one LFP trace (E1) is in the files; S2 uses a 250 ms window (see fig3a).\n  - The criterion leaves ratios above 31.6 without an outcome; partially reproduced was chosen\n    because the claimed direction holds and its size does not.\n- claim: activated-20-35hz-power-pd-vs-control\n  outcome: reproduced\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:activated-20-35hz-power-pd-vs-control\n  notes: Mean 20 to 35 Hz power is higher in the parkinsonian activated file under every reading,\n    by a factor of 4.55 (LFP, S1), 4.71 (LFP, S2) and 11.8 (PT5B SCH).\n  deviations:\n  - Only one LFP trace (E1) is in the files; S2 uses a 250 ms window (see fig3a).\n- claim: rest-synchrony-increase\n  outcome: not_reproduced\n  notebook: reproduce_doherty_2025.ipynb\n  output: claim:rest-synchrony-increase\n  notes: The significant synchrony at rest is 0 s in both files under every reading, so it is not\n    larger in the parkinsonian file. It follows from fig4-control-unitary-events and\n    fig7-pd-unitary-events, whose method finds no significant window on these data.\nfindings:\n- kind: metadata_error\n  statement: The dandiset description says each file holds spike trains of all 10,073 neurons. The\n    units tables hold only the cells that fired, 2,917 to 4,480 M1 cells per file in set\n    sM1_12-12-2023 and 2,765 to 4,714 in the others, and input generators that did not fire are\n    missing too. The size of each population is not stated and can be recovered only from the gid\n    blocks in the unit names (24 gids between blocks are never seen).\n- kind: metadata_error\n  statement: The dandiset description says each file holds membrane potentials of 400 PT5B\n    neurons. The four files of the paper's set, sM1_12-12-2023, hold 20 each (gids 5201 to 6502);\n    the other twelve hold 400 (gids 5130 to 5529).\n- kind: other\n  statement: In the paper's set the PT5B membrane potentials do not belong to the run whose spikes\n    are stored. Their 0 mV crossings match the same gid's unit spikes in the first 0.5 s (95% to\n    100%) but only 1.5% to 5.6% of unit spikes in 2.0 to 4.3 s, while spike counts stay similar. In\n    set sM1-04-22-2024 the potentials match the spikes throughout. The potentials of the paper's\n    set seem to come from a run that diverged from the stored one.\n- kind: other\n  statement: sub-001/sub-001.nwb is the same blob as sub-001/sub-001_ses-sM1-04-22-2024-01.nwb, so\n    one simulation is deposited twice under two names.\n- kind: metadata_insufficient\n  statement: Each file holds one LFP trace, \"Segment 0 LFP 0\", with no electrode position, where\n    the model records 11 electrodes at 200 to 1200 um depth. Which electrode it is cannot be told\n    from the files, and the mean over electrodes cannot be computed.\n- kind: metadata_error\n  statement: The files name the bioRxiv preprint as their related publication, the dandiset lists\n    no related resource for the published paper, and the archive's summary gives \"spike sorting\n    technique\" as the measurement technique of a simulation, with \"Units\" as the only variable\n    measured though the files hold LFP and membrane potentials.\n- kind: data_missing\n  statement: The single-cell current-injection simulations of the control and parkinsonian PT5B\n    models behind the 64% decrease in excitability (Supplementary Fig. 1) are not in the dandiset.\n- kind: methods_unavailable\n  statement: Question for the authors. Over which cells is a population's mean rate taken? The\n    paper's IT rates match exactly when the cells are those that fired at least once in the 4.3 s\n    simulation, with rates over the last 2.3 s (IT2 1.203 +/- 1.649 at control rest against 1.2 +/-\n    1.6), and not when all cells or only cells active in the last 2.3 s are counted. Which test\n    gave the rate p-values? Under that reading the Welch t-test meets every printed bound except\n    for IT4 at rest (two parkinsonian cells, p = 0.31), while paired tests do not for IT2.\n- kind: methods_unavailable\n  statement: Question for the authors. Which PT5B cells, and what definition, gave 1% to 3% of\n    spikes coincident within 1 ms and the unitary-event durations of Figs. 4 and 7? Over all 1,435\n    PT5B cells (17 to 42 spikes per ms) nearly every spike has another PT5B spike within 1 ms, two\n    or more cells fire in 95% to 100% of 1 ms bins, and a joint-surprise test against rate-matched\n    Poisson cells finds no significant 100 ms window.\n- kind: methods_unavailable\n  statement: Question for the authors. How were LFP bursts (Figs. 3 and 6) defined, which\n    spectrogram parameters and electrode were used, and was the PT5B spike count histogram smoothed\n    before the duty cycle was measured? Unsmoothed 2 ms histograms cross half-height every 10 ms,\n    and a half-height rule on band power gives burst rates of 1 to 3 Hz where the paper reports 5\n    Hz and 10 to 20 Hz.\n- kind: methods_unavailable\n  statement: Question for the authors. Does \"highest spike rate of any neuron population\" cover\n    interneurons? PV5A (22.5 to 42.1 spikes/s by all cells) fires faster than PT5B (11.7 to 29.7)\n    in control rest and both parkinsonian states; among excitatory types PT5B is highest.\n- kind: methods_unavailable\n  statement: Question for the authors. How were subthreshold membrane-potential oscillations\n    detected, and over which cells is the 57.4% taken? The paper's set holds 20 PT5B potentials per\n    file, and 57.4% of 20 is not a whole number.\n- kind: paper_inconsistency\n  statement: The Results report a significant increase in PT5B rate from control to parkinsonian in\n    the activated state (p < 0.001), while the Discussion says there was no significant change in\n    PT5B population firing rate in the activated state. On the data, counting all PT5B cells, three\n    tests give p below 1e-06 and the Mann-Whitney test 0.0052.\n"
}
```

```
File created successfully at: attempts/001444-doherty-2025-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent**

Fixing two numbers in the record that were not printed as stated.

**Agent calls Bash**

```bash
python - <<'EOF'
p='attempts/001444-doherty-2025-01.yaml'; s=open(p).read()
for old,new in [("""10,073 M1 cells (gids 0 to 10072); the gid blocks seen in all 16 files account for 10,049 cells
    with 24 gids never seen between blocks.""","""10,073 M1 cells (gids 0 to 10072); the smallest gid blocks seen in all 16 files and the 24 gids
    never seen between them sum to 10,073."""),
("in the first 0.5 s (95% to\n    100%)","in the first 0.5 s (94.8% to\n    100%)")]:
    assert old in s, old; s=s.replace(old,new)
open(p,'w').write(s)
EOF
grep -n ": .*: " attempts/001444-doherty-2025-01.yaml | grep -v "^\s*[0-9]*:\s*- \|^[0-9]*:  *[a-z_]*: [^:]*$" | head
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
python - <<'EOF'
import yaml
for p in ['attempts/001444-doherty-2025-01.yaml','questions/001444.yaml']:
    d=yaml.safe_load(open(p))
    def walk(x,path=''):
        if isinstance(x,dict):
            for k,v in x.items(): walk(v,path+'/'+str(k))
        elif isinstance(x,list):
            for i,v in enumerate(x): walk(v,path+f'[{i}]')
        elif isinstance(x,str):
            if ': ' in x or '—' in x or 'rather' in x or '**' in x: print(p,path,repr(x[:120]))
    walk(d)
print('ok')
EOF
grep -n "—\|rather" entries/001444-doherty-2025/*.py entries/001444-doherty-2025/*.ipynb $TMPDIR/header.md $TMPDIR/summary.md $TMPDIR/concl.py | head
```

```
questions/001444.yaml /questions[0]/passage 'Statistically significant change was found for firing rates for excitatory cell types going from rest to activated ... ('
ok
```

**Agent calls Bash**

```bash
python -c "
import yaml;d=yaml.safe_load(open('questions/001444.yaml'));s=d['questions'][0]['passage'];i=s.index(': ');print(s[i-60:i+40])"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import yaml;d=yaml.safe_load(open('questions/001444.yaml'));s=d['questions'][0]['passage'];i=s.index(': ');print(s[i-60:i+40])
                                                                                                 ~~~~~~~^^^^^^
ValueError: substring not found
```

**Agent**

The flag was the `***` in the quoted legend, inside a block scalar, which is fine. Writing the entry README and running the checks.

**Agent calls Bash**

```bash
cat > entries/001444-doherty-2025/README.md <<'EOF'
# Doherty, Chen, Smith, Wichmann, Chu & Lytton (2025) from dandiset 001444

Tests the findings of [Doherty et al. (2025)](https://doi.org/10.1038/s41531-025-01070-4) on
[DANDI:001444](https://dandiarchive.org/dandiset/001444/0.250805.2002), which holds four sets of
four NetPyNE simulations of a 10,073-cell model of mouse M1 (control and parkinsonian, rest and
activated). The paper reports set sM1_12-12-2023, and the claims are tested on it.

| Claims | Outcome |
|---|---|
| Dominant frequencies at control rest (19 Hz), control activated (44 Hz) and parkinsonian rest (15 Hz) | Reproduced |
| PT5B rates and their changes, except the control against parkinsonian activated comparison | Reproduced |
| PT5B ISI CV in both conditions | Reproduced |
| More negative PT5B potential in the parkinsonian activated state; more 20 to 35 Hz power | Reproduced |
| PT5B activated rate, parkinsonian against control (one test of four above p = 0.001) | Partially reproduced |
| Order-of-magnitude increase of 15 Hz power at rest (the ratio is 65 to 129) | Partially reproduced |
| IT2, IT4, IT5A, IT5B and IT6 rates (ten claims) | Not reproduced under the claims file's readings; matched by a variant, asked of a reader |
| Parkinsonian activated dominant frequency (27 Hz against 43) | Not reproduced |
| Duty cycles, LFP burst rates, coincident spikes, unitary events (eleven claims) | Not reproduced |
| Network size (the files store only cells that fired) | Not reproduced |
| Highest PT5B rate (PV5A fires faster) | Blocked: methods underspecified |
| Robustness over four sets; subthreshold oscillations (three claims) | Blocked: methods underspecified |
| PT5B current-injection excitability | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The units tables hold only cells that fired; the paper's IT rates match exactly when the mean is
taken over those cells, a reading the claims file does not list. The paper's set holds 20 PT5B
potentials per file (not 400), and in the analysis window they do not match the stored spikes of
the same cells. The attempt record, with the reasons and the differences from the paper's method,
is [`attempts/001444-doherty-2025-01.yaml`](../../attempts/001444-doherty-2025-01.yaml).

- `reproduce_doherty_2025.ipynb`: the analysis. It takes about six minutes, most of it streaming
  the files.
- `m1sim.py`: loading the files, population sizes from the gid blocks, rates, spectra (with
  NetPyNE 1.0.5's Morlet spectrogram), duty cycles, coincidences and unitary events. Other
  notebooks on this dandiset can import it.
EOF
python tools/entry.py check entries/001444-doherty-2025 2>&1 | tail -20
```

```
0 error(s)
```

**Agent calls Bash**

```bash
sed -i 's/| Not reproduced under the claims file.s readings; matched by a variant, asked of a reader |/| Not reproduced under the claims file'"'"'s readings; the values match under a variant reading, asked of a reader |/' entries/001444-doherty-2025/README.md; grep -n "variant reading" entries/001444-doherty-2025/README.md; python tools/entry.py handover entries/001444-doherty-2025 && ls executed/001444-doherty-2025/handover; git status --short; date -u
```

```
16:| IT2, IT4, IT5A, IT5B and IT6 rates (ten claims) | Not reproduced under the claims file's readings; the values match under a variant reading, asked of a reader |
wrote executed/001444-doherty-2025/handover
10.1038-s41531-025-01070-4.yaml
m1sim.py
reproduce_doherty_2025.ipynb
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
?? attempts/001444-doherty-2025-01.yaml
?? entries/001444-doherty-2025/
?? questions/001444.yaml
?? scripts
Mon Nov  2 17:36:34 UTC 2026
```

**Agent**

Handover built. Removing the `__pycache__` my development runs left in the entry, and confirming the handover has no conclusion cells.

**Agent calls Bash**

```bash
ls -a entries/001444-doherty-2025; rm -rf entries/001444-doherty-2025/__pycache__; python -c "
import nbformat;nb=nbformat.read('executed/001444-doherty-2025/handover/reproduce_doherty_2025.ipynb',4)
print(sum(c.source.lstrip().startswith('**Result') for c in nb.cells), any(c.source.startswith('## Summary') for c in nb.cells), len(nb.cells))"; python tools/entry.py check entries/001444-doherty-2025 | tail -1
```

```
.
..
.claude
README.md
__pycache__
entry.yaml
m1sim.py
reproduce_doherty_2025.ipynb
requirements.in
requirements.lock.txt
0 False 82
0 error(s)
```

**Agent calls Bash**

```bash
ls -laR entries/001444-doherty-2025/.claude | head; git -C  check-ignore -v entries/001444-doherty-2025/.claude || echo "not ignored"
```

```
entries/001444-doherty-2025/.claude:
total 12
drwxr-xr-x 3 runner runner 4096 Nov  2 17:07 .
drwxr-xr-x 3 runner runner 4096 Nov  2 17:36 ..
drwx------ 2 runner runner 4096 Nov  2 17:07 .cc-writes

entries/001444-doherty-2025/.claude/.cc-writes:
total 8
drwx------ 2 runner runner 4096 Nov  2 17:07 .
drwxr-xr-x 3 runner runner 4096 Nov  2 17:07 ..
not ignored
```

**Agent**

I did steps 1 to 6 of the Author section. The entry runs from a clean environment in 320 s, `entry.py check` reports 0 errors, and the handover is in `executed/001444-doherty-2025/handover/`. Nothing is committed. I pinned version 0.250805.2002: the paper cites no version, it is the only published one, and the draft has the same 17 assets and blobs. Run time was about 40 minutes (16:58 to 17:37 UTC).

## 1. Outcomes (40 claims)

| Outcome | Claims |
|---|---|
| Reproduced (10) | fig2-control-rest-beta (19 Hz), fig2-control-activated-gamma (44 Hz), fig5-pd-rest-beta (15 Hz), fig2c-control-pt5b-rate-activated, fig5c-pd-pt5b-rate-activated, rest-pt5b-rate-pd-vs-control, control-cv-isi, pd-cv-isi, pd-activated-vm-more-negative, activated-20-35hz-power-pd-vs-control |
| Partially reproduced (2) | activated-pt5b-rate-pd-vs-control (Mann-Whitney p = 0.0052, the criterion needs < 0.001); rest-beta-power-order-of-magnitude (ratio 65 to 129, above the criterion's 3.16 to 31.6) |
| Not reproduced (23) | the IT rate claims (fig2c-control-it23, fig2c-control-it6, control-it5-silenced, control-it4, fig5c-pd-it23, pd-it5-silenced, pd-it6-unchanged, rest-it4, rest-it5a, activated-it6); fig1-network-size; fig5-pd-activated-gamma (27 Hz); control-duty-cycle and pd-duty-cycle; fig3a, fig3b, fig6a, fig6b; control-coincident-spikes and pd-coincident-spikes; fig4 and fig7 unitary events; rest-synchrony-increase |
| Blocked (5) | model-pt5b-excitability-decrease (data_missing); robustness-four-sets, pt5b-highest-rate, control-subthreshold-oscillations, pd-no-subthreshold-oscillations (methods_underspecified) |

## 2. Dataset, assumptions and questions

**Findings about the dataset:**
- **Only cells that fired are stored.** The units tables hold 2,917 to 4,480 of the 10,073 M1 cells per file, not all of them as the description says. I took population sizes from the gid blocks in the unit names.
- **Fewer potentials in the paper's set.** Its files hold 20 PT5B membrane potentials each, not 400.
- **Those potentials don't match the stored spikes.** They agree with the same cells' spikes for the first 0.5 s, but only 1.5 to 5.6% from 2 s on. In set 04-22-2024 they match throughout, so the paper's-set traces seem to come from a run that diverged from the stored one.
- **Duplicate file.** `sub-001.nwb` is the same blob as `sub-001_ses-sM1-04-22-2024-01.nwb`.
- **One LFP trace, position unknown.** Each file has a single LFP trace with no electrode position, where the model records 11.
- **Metadata.** The files link the preprint, not the paper; the dandiset lists no related resource; the archive summary gives "spike sorting" as the technique.
- **Other numbers in the paper's set.** PT5B rates and CVs match the paper to the printed decimal. Coincidence and unitary-event measures over all PT5B cells saturate: 17 to 42 spikes per ms give about 100% coincident spikes and no significant window.

**Assumptions:** no outcome is marked `assumed`. Choices recorded as deviations:
- "LFP 0" is taken as electrode 0 (reading E1). E2, the mean over 11 electrodes, cannot be computed.
- The short-time Fourier reading (S2) uses a 250 ms window, because NetPyNE's default FFT has a 156 Hz frequency step.
- I classed rest-beta-power-order-of-magnitude as partially reproduced, because its criterion gives no outcome for a ratio above 31.6.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- Which cells enter a population's mean rate, and which test gave the rate p-values?
- Which cells and definition gave the coincidence and unitary-event numbers?
- How were LFP bursts defined, and was the spike count histogram smoothed for the duty cycle?
- Does "any neuron population" include interneurons? PV5A fires faster than PT5B.
- How were subthreshold oscillations detected?

**Question to a reader** (`questions/001444.yaml`): every IT value matches the paper to the printed decimal under a third reading, R3. R3 averages over the cells the file holds (those that fired at any time in the run) with rates over the last 2.3 s. For example, IT2 at control rest gives 1.203 ± 1.649 against the paper's 1.2 ± 1.6. The claims file lists only R1 (all cells) and R2 (cells active in the last 2.3 s). I tested on R1 and R2 as written and showed R3 as a variant. Ten not-reproduced claims and pt5b-highest-rate would be decided again under R3; rest-it4 would still fail its tests.

## 3. Protocol gaps

1. **Readings found after the analysis.** The protocol does not say what to do when the data show a reading the claims file missed that matches the paper exactly. I asked a reader, kept the outcomes on the file's readings, and showed R3 as a variant.
2. **Gaps in a criterion.** rest-beta-power gives outcomes only for ratios in 3.16 to 31.6 or below 3.16, and nothing above. I chose partially reproduced and recorded the reason.
3. **Readings that can't be computed.** Readings the dataset cannot support (E2 needs 11 electrodes) have no rule. I ran the readings that could be run and recorded a deviation.
4. **Results that show the method differs.** When a result shows the paper's procedure must differ (100% coincident against 1%), the protocol only says `methods_underspecified` for chance levels. I recorded not reproduced, with the reason and a question for the authors.
5. **Format files.** To learn the questions-file format I opened `questions/000005.yaml`, from another dataset. It is not an attempt record, but it falls outside the files the prompt pointed me to.

## 4. Runtime and failures

The notebook takes about 5.5 minutes, nearly all of it streaming the files. Nothing failed. Untracked dotfiles (`.bashrc`, `.idea`, `scripts`, and others) appeared at the repository root during the run. They are not mine and I left them alone.

## End of run

73 turns, 38 minutes, $7.37 at API prices, result: success.
