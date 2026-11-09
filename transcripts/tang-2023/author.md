# 000447 · author · run 40994732733

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls
```

```
<persisted-output>
Output too large (35.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/0ffbb989-b088-4de9-8bdc-0bfab9968eb8/tool-results/bdn6qu569.txt

Preview (first 2KB):
Fri Oct 30 03:01:59 UTC 2026
# Protocol for an attempt

Version: `pilot-12`. Record this version in the attempt's provenance.

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

**Agent calls Bash**

```bash
cat README.md docs/design.md docs/archives.md | head -c 60000; ls entries/001453-fouke-2025 claims/001453 claims/000447 paper 2>&1
```

```
<persisted-output>
Output too large (37.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/0ffbb989-b088-4de9-8bdc-0bfab9968eb8/tool-results/bce2s451q.txt

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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/0ffbb989-b088-4de9-8bdc-0bfab9968eb8/tool-results/bce2s451q.txt"
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
[... 695 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/000447/*.yaml
```

```
<persisted-output>
Output too large (52.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/0ffbb989-b088-4de9-8bdc-0bfab9968eb8/tool-results/bnrddlobu.txt

Preview (first 2KB):
# Claims for Tang, Shin & Jadhav (2023), Cell Reports 42, 112246, on dandiset 000447.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read. The NIH author manuscript in PubMed Central (PMC10124109, NIHMS1887302) as served by
# Europe PMC, with its STAR Methods and figure legends, and the supplement
# (NIHMS1887302-supplement-1.pdf, Figures S1 to S7 and their legends), all from
# paper/10.1016-j.celrep.2023.112246.txt. The version of record was not read. The PDF of the
# supplement was not opened; its text was enough. One value of the Methods is garbled in the
# text. The 1D Gaussian that smooths the linearized rate maps reads "(s = σ cm" with the
# number lost (Methods, Spatial fields and linearization). Criteria that use it name it as open.
#
# Code read. github.com/JadhavLab/GeometricTransformation at commit
# 5e55e69f2f089adcfd65bbfae42ec80e60e9903d (16 March 2023), MATLAB. It holds the scripts behind
# Figures 1 to 4 and S3, S5, S6, S7C-D. They are the behavioural summary, PV similarity, Bayesian
# decoding, selectivity index, path equivalence, UMAP embedding and distances, CCGP and the 35
[... 12 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/0ffbb989-b088-4de9-8bdc-0bfab9968eb8/tool-results/bnrddlobu.txt"
}
```

```
1	# Claims for Tang, Shin & Jadhav (2023), Cell Reports 42, 112246, on dandiset 000447.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
3	# protocol pilot-10 as stated in docs/protocol.md.
4	#
5	# Text read. The NIH author manuscript in PubMed Central (PMC10124109, NIHMS1887302) as served by
6	# Europe PMC, with its STAR Methods and figure legends, and the supplement
7	# (NIHMS1887302-supplement-1.pdf, Figures S1 to S7 and their legends), all from
8	# paper/10.1016-j.celrep.2023.112246.txt. The version of record was not read. The PDF of the
9	# supplement was not opened; its text was enough. One value of the Methods is garbled in the
10	# text. The 1D Gaussian that smooths the linearized rate maps reads "(s = σ cm" with the
11	# number lost (Methods, Spatial fields and linearization). Criteria that use it name it as open.
12	#
13	# Code read. github.com/JadhavLab/GeometricTransformation at commit
14	# 5e55e69f2f089adcfd65bbfae42ec80e60e9903d (16 March 2023), MATLAB. It holds the scripts behind
15	# Figures 1 to 4 and S3, S5, S6, S7C-D. They are the behavioural summary, PV similarity, Bayesian
16	# decoding, selectivity index, path equivalence, UMAP embedding and distances, CCGP and the 35
17	# dichotomies. It does not hold the code that computes rate maps (the Frank/Jadhav lab
18	# "time-filter framework" in Src_Matlab and usrlocal, not public in this repository). It also
19	# lacks the code for the rate-overlap and single-cell spatial correlation of Figure S3A, the
20	# ramping cells of Figure S4, the cell-ID shuffles of Figure 2E and the geometric random model
[... 842 more lines not kept]
```

**Agent**

Big claims file (33 claims). Now the example entry formats and the dataset.

**Agent calls Bash**

```bash
cd entries/001453-fouke-2025; cat entry.yaml requirements.in README.md; head -c 3000 omr.py; python -c "
import json;nb=json.load(open('reproduce_fouke_2025.ipynb'))
for c in nb['cells'][:6]: print(c['cell_type'], c.get('metadata'), ''.join(c['source'])[:1500]); print('-----')
print(len(nb['cells']))
"; cat ../../attempts/001453-fouke-2025-01.yaml | head -150
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
[... 350 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 150,400p attempts/001453-fouke-2025-01.yaml; ls questions schemas tools
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
[... 305 more lines not kept]
```

**Agent**

Now the dataset.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/000447/ | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/000447/versions/" | python -m json.tool | head -60
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; for v in 0.230316.2133 0.250724.2224; do echo == $v; curl -s "https://api.dandiarchive.org/api/dandisets/000447/versions/$v/assets/?page_size=100" | python -c "
import json,sys; d=json.load(sys.stdin)
for a in d['results']: print(a['asset_id'], a['path'], a['size'], a.get('blob'), a['modified'])"; done; curl -s "https://api.dandiarchive.org/api/dandisets/000447/versions/0.250724.2224/" | python -c "
import json,sys; d=json.load(sys.stdin); print(d.get('description')); print(json.dumps(d.get('relatedResource'),indent=0)); print(d.get('citation')); print(json.dumps(d.get('assetsSummary'),indent=0)[:1500])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; wc -c *.txt; grep -n -i "dandi\|000447\|data and code availability" -A3 *.txt | head -40; python -c "import pynwb,remfile,h5py,umap;print(pynwb.__version__)" 2>&1 | tail -1; which uv python; python --version
```

```
<persisted-output>
Output too large (56.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/0ffbb989-b088-4de9-8bdc-0bfab9968eb8/tool-results/brepprz1s.txt

Preview (first 2KB):
121344 10.1016-j.celrep.2023.112246.txt
7:319 nihpa Cell reports Cell Rep PMC10124109 10124109 10124109 NIHMS1887302 36924498 10.1016/j.celrep.2023.112246 Geometric transformation of cognitive maps for generalization across hippocampal-prefrontal circuits Tang Wenbo 1 2 3 * Shin Justin D 1 3 Jadhav Shantanu P 1 4 * 1 Neuroscience Program, Department of Psychology, and Volen National Center for Complex Systems, Brandeis University, Waltham, MA 02453, USA 2 Present address: Department of Neurobiology and Behavior, Cornell University, Ithaca, NY 14853, USA 3 These authors contributed equally 4 Lead contact AUTHOR CONTRIBUTIONS W.T. and S.P.J. designed the study. J.D.S. collected the data. W.T. conceptualized and performed the analysis. W.T. and S.P.J. interpreted data. W.T. visualized data. W.T. and S.P.J. wrote the paper. S.P.J. supervised the project and obtained funding. * Correspondence: [removed: an e-mail address] (W.T.), [removed: an e-mail address] (S.P.J.) 15 3 2023 42 3 112246 112246 24 4 2023 This is an open access article under the CC BY-NC-ND license ( http://creativecommons.org/licenses/by-nc-nd/4.0/ ). The publisher's version of this article is available at Cell Rep SUMMARY The ability to abstract information to guide decisions during navigation across changing environments is essential for adaptation and requires the integrity of the hippocampal-prefrontal circuitry. The hippocampus encodes navigational information in a cognitive map, but it remains unclear how cognitive maps are transformed across hippocampal-prefrontal circuits to support abstraction and generalization. Here, we simultaneously record hippocampal-prefrontal ensembles as rats generalize navigational rules across distinct environments. We find that, whereas hippocampal representational maps 
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd  fold -s -w 200 paper/10.1016-j.celrep.2023.112246.txt > $TMPDIR/paper.txt; wc -l $TMPDIR/paper.txt; grep -n -i "dandi\|available\|deposited" $TMPDIR/paper.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/paper.txt",
 "limit": 400
}
```

```
File content (28805 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/paper.txt",
 "limit": 190
}
```

```
1	DOI: 10.1016/j.celrep.2023.112246
2	Version: as served by europe_pmc
3	Source: europe_pmc+crossref (paper-text-fetcher)
4	Stored: 2026-10-20
5	Extracted: as fetched; with 1 supplement file(s) from the PMC Open Access cloud data (PMC10124109), PDFs extracted with PyMuPDF (dehyphenated, NFKC), Word files with textutil
6	------------------------------------------------------------------------
7	319 nihpa Cell reports Cell Rep PMC10124109 10124109 10124109 NIHMS1887302 36924498 10.1016/j.celrep.2023.112246 Geometric transformation of cognitive maps for generalization across 
8	hippocampal-prefrontal circuits Tang Wenbo 1 2 3 * Shin Justin D 1 3 Jadhav Shantanu P 1 4 * 1 Neuroscience Program, Department of Psychology, and Volen National Center for Complex Systems, Brandeis 
9	University, Waltham, MA 02453, USA 2 Present address: Department of Neurobiology and Behavior, Cornell University, Ithaca, NY 14853, USA 3 These authors contributed equally 4 Lead contact AUTHOR 
10	CONTRIBUTIONS W.T. and S.P.J. designed the study. J.D.S. collected the data. W.T. conceptualized and performed the analysis. W.T. and S.P.J. interpreted data. W.T. visualized data. W.T. and S.P.J. 
11	wrote the paper. S.P.J. supervised the project and obtained funding. * Correspondence: [removed: an e-mail address] (W.T.), [removed: an e-mail address] (S.P.J.) 15 3 2023 42 3 112246 112246 24 4 2023 This is an 
12	open access article under the CC BY-NC-ND license ( http://creativecommons.org/licenses/by-nc-nd/4.0/ ). The publisher's version of this article is available at Cell Rep SUMMARY The ability to 
13	abstract information to guide decisions during navigation across changing environments is essential for adaptation and requires the integrity of the hippocampal-prefrontal circuitry. The hippocampus 
14	encodes navigational information in a cognitive map, but it remains unclear how cognitive maps are transformed across hippocampal-prefrontal circuits to support abstraction and generalization. Here, 
15	we simultaneo
[... 175 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/paper.txt",
 "offset": 190,
 "limit": 210
}
```

```
190	request by contacting the lead contact. Custom code in MATLAB (R2017a) used for analyses in this study is available on GitHub at http://github.com/JadhavLab/GeometricTransformation . Any additional 
191	information required to reanalyze the data reported in this paper is available from the lead contact upon request. EXPERIMENTAL MODEL AND SUBJECT DETAILS Eight adult male Long-Evans rats (450–550 g, 
192	4–6 months) were used in this study. Animals were individually housed and kept on a on a 12-hr regular light/dark cycle. All procedures were approved by the Institutional Animal Care and Use 
193	Committee at the Brandeis University and conformed to US National Institutes of Health guidelines. METHOD DETAILS Experimental design After habituation to daily handling and resting in a high-walled, 
194	opaque sleep box (~30 × 30 cm), animals were food deprived to 85–90% of their ad libitum weight, and pre-trained to run on a linear track (~1-m long) for rewards (sweetened evaporated milk). 17 , 22 
195	For experiments on the W-maze (~80 × 80 cm with ~7-cm wide tracks), animals were food-deprived and naïve to the W-mazes and the novel experimental room ( Figure S1A ). Animals were rewarded for 
196	performing a hippocampal and PFC-dependent continuous alternation task ( Figure 1A , left) 37 – 39 : returning to the center well after visits to either side well (left or right well; inbound, IN L 
197	or IN R ), and choosing the opposite side well from the previously visited side when starting from the center (outbound, OUT R or OUT L ). Animals learned the W-track alternation rule by 
198	trial-and-error. Rewards were automatically delivered in the three reward wells (left well: L; right well: R; center well: C), triggered by crossing of an infrared beam by the animal’s nose. Each 
199	W-maze session lasted 15–20 mins, and was interleaved with rest sessions in the sleep box placed near the W-maze ( Figures 1A and S1A ). The task performance was estimated using a state-spa
[... 200 more lines not kept]
```

**Agent**

Now the NWB contents. Let me set up an environment and open the smallest file.

**Agent calls Bash**

```bash
cd $TMPDIR && python -c "import pynwb, remfile, h5py, dandi; print(pynwb.__version__, h5py.__version__)" 2>&1 | tail -2; pip list 2>/dev/null | grep -i -E "umap|scikit|scipy|statsmodels|numpy|pandas|scikit_posthocs|libsvm"
```

```
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pynwb'
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q pynwb remfile h5py dandi numpy scipy pandas statsmodels scikit-learn umap-learn scikit-posthocs matplotlib ipykernel nbformat nbclient 2>&1 | tail -3; python -c "import pynwb, umap, sklearn; print(pynwb.__version__, umap.__version__)"
```

```
4.2.0 0.5.12
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > survey.py <<'EOF'
import h5py, remfile, sys, time
from dandi.dandiapi import DandiAPIClient
t=time.time()
c=DandiAPIClient(); ds=c.get_dandiset("000447","0.250724.2224")
a=[x for x in ds.get_assets() if "AM2" in x.path][0]
url=a.get_content_url(follow_redirects=1, strip_query=True)
f=h5py.File(remfile.File(url),"r")
def visit(name,obj):
    if isinstance(obj,h5py.Dataset):
        print(name, obj.shape, obj.dtype, dict((k,(v if not hasattr(v,'shape') or v.size<5 else v.shape)) for k,v in obj.attrs.items() if k not in ('object_id','namespace')))
    else:
        at={k:v for k,v in obj.attrs.items() if k in ('neurodata_type','description','colnames')}
        print(name+'/', at)
f.visititems(lambda n,o: None if n.startswith('acquisition/e-series') else visit(n,o))
print(time.time()-t)
EOF
python survey.py 2>&1 | grep -v "^stimulus\|^general/devices" | head -300
```

```
acquisition/ {}
acquisition/ElectricalSeries/ {'description': 'no description', 'neurodata_type': 'ElectricalSeries'}
acquisition/ElectricalSeries/data (5005900, 62) float64 {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'microvolts'}
acquisition/ElectricalSeries/electrodes (62,) int64 {'description': 'all electrodes - one channel per tetrode', 'neurodata_type': 'DynamicTableRegion', 'table': <HDF5 object reference>}
acquisition/ElectricalSeries/timestamps (5005900,) float64 {'interval': np.int64(1), 'unit': 'seconds'}
analysis/ {}
file_create_date (1,) object {}
general/ {}
general/experiment_description () object {}
general/experimenter (1,) object {}
general/extracellular_ephys/ {}
general/extracellular_ephys/Tetrode1/ {'description': 'electrode group for tetrode1', 'neurodata_type': 'ElectrodeGroup'}
general/extracellular_ephys/Tetrode10/ {'description': 'electrode group for tetrode10', 'neurodata_type': 'ElectrodeGroup'}
general/extracellular_ephys/Tetrode11/ {'description': 'electrode group for tetrode11', 'neurodata_type': 'ElectrodeGroup'}
general/extracellular_ephys/Tetrode12/ {'description': 'electrode group for tetrode12', 'neurodata_type': 'ElectrodeGroup'}
general/extracellular_ephys/Tetrode13/ {'description': 'electrode group for tetrode13', 'neurodata_type': 'ElectrodeGroup'}
general/extracellular_ephys/Tetrode14/ {'description': 'electrode group for tetrode14', 'neurodata_type': 'ElectrodeGroup'}
general/extracellular_ephys/Tetrode15/ {'description': 'electrode group for tetrode15', 'neurodata_type': 'ElectrodeGroup'}
general/extracellular_ephys/Tetrode16/ {'description': 'electrode group for tetrode16', 'neurodata_type': 'ElectrodeGroup'}
general/extracellular_ephys/Tetrode17/ {'description': 'electrode group for tetrode17', 'neurodata_type': 'ElectrodeGroup'}
[... 135 more lines not kept]
```

**Agent**

The files hold spikes, LFP, 2D position, epochs and a trials table, no linearized positions or unit labels beyond electrodes. Inspecting the values.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > survey2.py <<'EOF'
import h5py, remfile, numpy as np, pandas as pd
from dandi.dandiapi import DandiAPIClient
pd.set_option("display.width",250); pd.set_option("display.max_rows",400)
c=DandiAPIClient(); ds=c.get_dandiset("000447","0.250724.2224")
a=[x for x in ds.get_assets() if "AM2" in x.path][0]
f=h5py.File(remfile.File(a.get_content_url(follow_redirects=1, strip_query=True)),"r")
for k in ['session_description','identifier','general/experiment_description','general/session_id','general/subject/subject_id','general/subject/description','general/subject/age','general/subject/sex','general/keywords','session_start_time','general/lab','general/institution','processing/behavior/Position/SpatialSeries/reference_frame']:
    print(k, f[k][()])
print(dict(f['processing/behavior/Position/SpatialSeries'].attrs))
e=f['general/extracellular_ephys/electrodes']
el=pd.DataFrame({k:[v.decode() if isinstance(v,bytes) else v for v in e[k][:]] for k in ['x','y','imp','location','descriptor','referenced','label']})
el['group']=[f[r].name for r in e['group'][:]]
print(el.to_string())
print(f['intervals/epoch intervals/start_time'][:], f['intervals/epoch intervals/stop_time'][:])
tr=pd.DataFrame({k:f['intervals/trials/'+k][:] for k in ['start_time','stop_time','correct','trajectory_type','start_well','end_well']})
print(tr.to_string())
p=f['processing/behavior/Position/SpatialSeries/data'][:]; t=f['processing/behavior/Position/SpatialSeries/timestamps'][:]
print(p[:5], t[:5], np.nanmin(p,0), np.nanmax(p,0), np.median(np.diff(t)))
ue=f['units/electrodes'][:]; idx=f['units/spike_times_index'][:]
print(ue, np.diff(np.r_[0,idx]))
st=f['units/spike_times'][:]
print(st[:5], st.min(), st.max(), f['units/id'][:])
print(f['acquisition/ElectricalSeries/timestamps'][:3], f['acquisition/ElectricalSeries/timestamps'][-3:])
EOF
python survey2.py 2>&1
```

```
session_description b'Novel familiar novel experiment'
identifier b'AM2_01'
general/experiment_description b'Microdrive tetrode recordings in behaving rats'
general/session_id b'01'
general/subject/subject_id b'JDS-NFN-AM2'
general/subject/description b'Long Evans rat (RGD_2308852)'
general/subject/age b'P32W'
general/subject/sex b'M'
general/keywords [b'Hippocampus' b'Prefrontal cortex' b'Spatial memory' b'Working memory'
 b'Sleep' b'Learning']
session_start_time b'2023-03-14T17:31:07.596000-04:00'
general/lab b'Jadhav Lab'
general/institution b'Brandeis University'
processing/behavior/Position/SpatialSeries/reference_frame b'center well'
{'comments': 'Video frames taken at 30fps - row1:xpos row2:ypos row3:velocity', 'description': 'no description', 'namespace': 'core', 'neurodata_type': 'SpatialSeries', 'object_id': '6b8617df-4d8f-4d4c-b072-fcc331b104b0'}
      x    y    imp location descriptor referenced      label                                   group
0   0.7  3.0  250.0      PFC        NaN    Ref OFF   tetrode1   /general/extracellular_ephys/Tetrode1
1   0.7  3.0  250.0      PFC        NaN     Ref ON   tetrode1   /general/extracellular_ephys/Tetrode1
2   0.7  3.0  250.0      PFC     PFCRef    Ref OFF   tetrode2   /general/extracellular_ephys/Tetrode2
3   0.7  3.0  250.0      PFC     PFCRef     Ref ON   tetrode2   /general/extracellular_ephys/Tetrode2
[... 181 more lines not kept]
```

**Agent**

Key structure: units carry only spike times and an electrode reference (region via electrode location); no linearized position, no cell numbers, no waveforms. Surveying all five files now.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > survey3.py <<'EOF'
import h5py, remfile, numpy as np, pandas as pd
from dandi.dandiapi import DandiAPIClient
c=DandiAPIClient(); ds=c.get_dandiset("000447","0.250724.2224")
for a in sorted(ds.get_assets(), key=lambda a:a.path):
    f=h5py.File(remfile.File(a.get_content_url(follow_redirects=1, strip_query=True)),"r")
    e=f['general/extracellular_ephys/electrodes']
    loc=[v.decode() for v in e['location'][:]]; lab=[v.decode() for v in e['label'][:]]
    ue=f['units/electrodes'][:]; idx=f['units/spike_times_index'][:]; n=np.diff(np.r_[0,idx])
    ep0=f['intervals/epoch intervals/start_time'][:]; ep1=f['intervals/epoch intervals/stop_time'][:]
    print(a.path, 'units',len(ue),'electrode rows',len(loc), 'epochs', np.round(ep0,1), np.round(ep1-ep0,1))
    print(' units/electrodes', ue.tolist())
    print(' locs by row', ''.join('C' if l=='CA1' else ('P' if l=='PFC' else '?') for l in loc), set(loc))
    print(' labels', lab[::2][:40])
    print(' LFP', f['processing/ecephys/LFP/ElectricalSeries/data'].shape, f['processing/ecephys/LFP/ElectricalSeries/data'].chunks, 'acq', f['acquisition/ElectricalSeries/data'].shape)
    lt=f['processing/ecephys/LFP/ElectricalSeries/timestamps']
    print(' lfp t', lt[0], lt[-1], 1/np.median(np.diff(lt[:10000])))
    print(' pos', f['processing/behavior/Position/SpatialSeries/data'].shape, ' trials', f['intervals/trials/start_time'].shape)
    print(' age', f['general/subject/age'][()], f['identifier'][()], f['session_start_time'][()])
EOF
python survey3.py 2>&1
```

```
sub-JDS-NFN-AM2/sub-JDS-NFN-AM2_behavior+ecephys.nwb units 57 electrode rows 62 epochs [ 2322.5  6273.7 10745.8] [878.4 899.1 945.6]
 units/electrodes [3, 3, 4, 4, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 8, 8, 8, 14, 14, 14, 14, 14, 14, 14, 14, 15, 17, 17, 20, 20, 20, 20, 20, 21, 21, 21, 21, 21, 21, 21, 22, 22, 24, 27, 27, 28, 28, 30, 31, 31, 31, 31, 31, 31, 31, 31, 21]
 locs by row PPPPPPPPCCCCCCCCCCCCCCCCCCCCPPPPPPPPPPPPCCCCCCCCCCPPPPPPPPPPPP {'CA1', 'PFC'}
 labels ['tetrode1', 'tetrode2', 'tetrode3', 'tetrode4', 'tetrode5', 'tetrode6', 'tetrode7', 'tetrode8', 'tetrode9', 'tetrode10', 'tetrode11', 'tetrode12', 'tetrode13', 'tetrode14', 'tetrode15', 'tetrode16', 'tetrode17', 'tetrode18', 'tetrode19', 'tetrode20', 'tetrode21', 'tetrode22', 'tetrode23', 'tetrode24', 'tetrode25', 'tetrode27', 'tetrode28', 'tetrode29', 'tetrode30', 'tetrode31', 'tetrode32']
 LFP (5005900, 62) None acq (5005900, 62)
 lfp t 2265.7484 11803.716766666666 1499.9999996944098
 pos (80087, 3)  trials (104,)
 age b'P32W' b'AM2_01' b'2023-03-14T17:31:07.596000-04:00'
sub-JDS-NFN-JS17/sub-JDS-NFN-JS17_behavior+ecephys.nwb units 97 electrode rows 64 epochs [2115.2 4917.7 9062.3] [ 944.3 1021.6 1012. ]
 units/electrodes [1, 1, 1, 1, 1, 1, 2, 2, 2, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 11, 11, 11, 11, 11, 11, 11, 11, 11, 13, 13, 13, 15, 16, 16, 16, 16, 17, 17, 17, 17, 17, 17, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 19, 19, 19, 20, 20, 20, 20, 20, 20, 22, 22, 22, 24, 24, 24, 27, 27, 28, 28, 28, 29, 29, 29, 29, 29, 29, 29, 31, 31, 31, 32, 5, 19, 22, 31, 11, 17, 17]
 locs by row PPPPPPPPCCCCCCCCCCCCCCCCPPPPPPPPPPPPPPPPCCCCCCCCCCPPPPPPPPPPPPPP {'CA1', 'PFC'}
 labels ['tetrode1', 'tetrode2', 'tetrode3', 'tetrode4', 'tetrode5', 'tetrode6', 'tetrode7', 'tetrode8', 'tetrode9', 'tetrode10', 'tetrode11', 'tetrode12', 'tetrode13', 'tetrode14', 'tetrode15', 'tetrode16', 'tetrode17', 'tetrode18', 'tetrode19', 'tetrode20', 'tetrode21', 'tetrode22', 'tetrode23', 'tetrode24', 'tetrode25', 'tetrode26', 'tetrode27
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 399,1141p $TMPDIR/paper.txt | grep -n -i "Figure S[1-7]\b\|cell samples\|sessions\|trial" | head -60
```

```
593:Figure S1. Configuration of recording rooms and memory performance in familiar-novel environments. Related to Figure 1. 
594:(A) Schematic layout of recording rooms for familiar and novel settings. De novo learning and F sessions were recorded under the 
595:setting in the familiar room (right), whereas N and N’ sessions were recorded in the novel room (left). Each room has a different size 
598:(B) Proportion correct for inbound (gray) and outbound (green) trials during the first session of de novo versus novel (N) learning of 
600:learning (****p < 0.0001, rank-sum tests). Also note that the below-chance performance of inbound trials during the first session of de 
613:Figure S2. Electrode locations and cell clusters in different environments. Related to Figure 1. 
625:across recording sessions. Also, note that Cell 3 in (G) did not fire in the novel environment, and Cell 3 in (H) did not fire in the 
633:Figure S3. Remapping properties of CA1 and PFC cells. Related to Figure 2. 
643:with Tukey’s post hoc. (D) PV similarity between novel and familiar environments over trials in the novel environment. Single-trial 
644:and session-averaged rate maps were used for the novel and familiar environment, respectively. Only trials with ≥ 80% spatially-tuned 
645:cells active were included (comparing the first and last trial, n.s., p(CA1) > 0.99, ****p(PFC) < 0.0001, one-way ANOVA with 
653:Figure S4. Reward representation in CA1 and PFC across environments. Related to Figure 2. 
656:ramping cells identified here (CA1: 81/495 = 16.4% cell samples; PFC: 115/636 = 18.1% cell samples across all sessions; each cell 
671:Figure S5. Robust path-equivalent representation that generalizes across trajectories and environments in PFC, but not in 
694:Figure S6. Distance relationship in the original high-dimensional neural space. Related to Figure 3. 
706:Figure S7. CCGP null models and decoding accuracy for all possible dichotomies. Related to Figure 4. 
716:(D) Decoding accurac
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 399,1141p $TMPDIR/paper.txt | sed -n 590,725p
```

```
Figure S1. Configuration of recording rooms and memory performance in familiar-novel environments. Related to Figure 1. 
(A) Schematic layout of recording rooms for familiar and novel settings. De novo learning and F sessions were recorded under the 
setting in the familiar room (right), whereas N and N’ sessions were recorded in the novel room (left). Each room has a different size 
and a number of prominent visual cues. Additionally, large cue cards (~4 m2) with different patterns hung on the walls of the novel 
room to enhance discriminability. 
(B) Proportion correct for inbound (gray) and outbound (green) trials during the first session of de novo versus novel (N) learning of 
the five rats shown in Figure 1. Note the higher performance for both inbound and outbound during novel learning than de novo 
learning (****p < 0.0001, rank-sum tests). Also note that the below-chance performance of inbound trials during the first session of de 
novo learning is due to perseveration, consistent with previously reported behavioral patterns1-3. Box plots show median, 75th (box), 
and 90th (whiskers) percentile. 
(C) Memory performance of familiar-novel animals (data points for individual animals, n = 3). A separate set of rats were trained on a 
F-N-F’-N’ sequence, instead of N-F-N’ shown in Figure 1, after de novo learning (STAR Methods). For both sets of animals, 
regardless of the behavioral order of novel and familiar environments, the performance in the familiar environment (blue circles) is 
significantly higher than that in the novel environment (gray circles; repeated-measures ANOVA with Tukey’s post hoc, F = 48.98, 
**p = 0.0053, ***p < 0.0005), suggesting that animals were able to remember and distinguish the two environments. 

=== page 3 ===
 
 
 
[... 113 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && git clone -q https://github.com/JadhavLab/GeometricTransformation gt 2>&1 | tail -2; cd gt && git checkout -q 5e55e69f2f089adcfd65bbfae42ec80e60e9903d && git log -1 --format=%H && find . -name "*.m" | head -80
```

```
Fri Oct 30 03:04:43 UTC 2026
5e55e69f2f089adcfd65bbfae42ec80e60e9903d
./Figure4/cal_all_dichotomies.m
./Figure4/CCGP_taskSeq.m
./Figure4/CCGP_trajPhase.m
./Figure4/decoding_CCGP_linearSVM_simple.m
./Figure4/CCGP_environment.m
./Figure4/Supplemental/decoding_dichotomy_linearSVM.m
./Figure4/Supplemental/decoding_dichotomy_main.m
./Figure2/decoding_position_PFC_novelfamiliar_trial.m
./Figure2/decoding_position_PFC_novelfamiliar_cross.m
./Figure2/decoding_position_CA1_novelfamiliar_cross.m
./Figure2/matchidx_acrossep.m
./Figure2/cal_PVsimilarity.m
./Figure2/decoding_position_novelfamiliar_batch.m
./Figure2/decoding_position_CA1_novelfamiliar_trial.m
./Figure2/DFSwb_HPexpt_placefield2_savefields_crossvalid_fun.m
./Figure2/decoding_position_novelfamiliar_templateN2_batch.m
./Figure2/decoding_position_novelfamiliar_trial_batch.m
./Figure2/cal_confusionMat_novelfamiliar.m
[... 17 more lines not kept]
```

**Agent**

Plenty of time left (started 02:59, now 03:05). Reading the key scripts the claims cite.

**Agent calls Bash**

```bash
cd $TMPDIR/gt && cat Figure2/cal_PVsimilarity.m Figure2/matchidx_acrossep.m Figure2/DFSwb_HPexpt_placefield2_savefields_crossvalid_fun.m | head -400
```

```
%---------------------------------------------------------------%
%  This is the main script for calculating population vector    %
%  (PV) similarity  -- Wenbo Tang (Jan 05, 2023)                %
%---------------------------------------------------------------%
clc
close all
clear all;
%%
% set directory
famnov_dir = '/Volumes/NovelFamiliar/';
%%
% the animal list
animal_list = {'AM2','JS17','JS21','ZT2','JS34'};
day = 1;
pos_interp = (0:0.01:1)';%position bins; 2-cm spatial bin
%%
PVcorr_all_PFC_FN = [];
PVcorr_all_CA1_FN = [];
PVcorr_all_PFC_NN = [];
PVcorr_all_CA1_NN = [];
[... 381 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/gt && cat Figure2/DFSwb_HPexpt_placefield2_savefields_crossvalid_fun.m | head -150; sed -n 1,200p Figure2/poolcells_acrossep.m | grep -v "^\s*%" | head -60
```

```
function linfields = DFSwb_HPexpt_placefield2_savefields_crossvalid_fun(animalprefix,ep,exclude_trajtime, savedir)

%---------------------------------------------------------------%
%  This is the function for calculating linearized place fields %
%  for cross-validation                                         %
%  Previously written by Shantanu, modified by Wenbo            %
%  -- Wenbo Tang (Sep 11, 2019)                                 %
%---------------------------------------------------------------%

% INPUTS:
%
%    animalprefix = animal prefix
%    ep = epoch. If multiday training is used, modifications will be needed (using day as an additional inputs).
%    exclude_trajtime = periods not used for estimation, usually the testing trial
%    savedir = directory for saving files
%
% OUTPUTS:
%
%    linfields are the estimated linearized place fields. 
%%
[... 176 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/gt && cat Figure3/cal_UMAP.m | grep -v "^\s*%" | head -220
```

```
clc
clear all
close all
animalprefix_list = {'AM2','JS17','JS21','ZT2','JS34'};% all animals
famnov_dir = '/Volumes/NovelFamiliar'; % set directory
day = 1;
ep = 6; %epoch, F = 4, N' = 6
CTXHP = 1;% CA1 = 0 , PFC = 1;
pos_interp = (0:0.005:1)';% position bins, normalized
cellthresh = 5; % minimal number of active cells per bin needed
usetemplate = 1; % a template of the UMAP transformation using N' has been save. Use it to get the exact image in the paper (=1), or run a new UMAP transformation on the data yourself (=0), which should generate a quantitatively similar result.
trialnum_all = []; % reset matrix
for theAnimal = 1:length(animalprefix_list)
    animalprefix = animalprefix_list{theAnimal};
    dir = sprintf('%s/%s_direct/',famnov_dir,animalprefix); % set directory
    trajinfo = loaddatastruct(dir, animalprefix, 'trajinfo', day); % get trajinfo
    trajbound = trajinfo{day}{ep}.trajbound;
    trajtime_raw = trajinfo{day}{ep}.trajtime;
    wellstand = trajinfo{day}{ep}.wellstend;
    traj_correct = trajinfo{day}{ep}.rewarded;
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/gt && for f in Figure3/cal_UMAP_INSeq_distance.m Figure3/cal_UMAP_TrajPhase_vs_Spatial_distance.m Figure3/cal_UMAP_FNdistance.m; do echo "=== $f"; grep -v "^\s*%" $f | grep -v "^\s*$" | sed -n '/spike_umap = run_umap\|validid\]/,$p' | grep -v "plot\|xlabel\|ylabel\|title\|figure\|xlim\|ylim\|zlim\|view\|colormap\|legend\|scatter" | head -120; done
```

```
=== Figure3/cal_UMAP_INSeq_distance.m
    spike_umap = run_umap(spike_matrix,'min_dist',0.6,'n_neighbors',50,'metric','cosine','n_components',3,'template_file','all_PFCumap_trials_ep6.mat');
else
    spike_umap = run_umap(spike_matrix,'min_dist',0.6,'n_neighbors',50,'metric','cosine','n_components',3,'template_file','all_CA1umap_trials_ep6.mat');
end
traj_label = [];
for tracknum = 1:4
    temp_label = pos_interp + tracknum -1;
    traj_label = [traj_label,temp_label];
end
umap_dist_inseq = []; % reset matrix
for track = [1,3]
    if track == 1
        alt_track = 4; %INSeq pair 1, INR-OUTL
    else
        alt_track = 2; %INSeq pair 2, INL-OUTR
    end
    trial_num1 = trialnum(track);
    trial_num2 = trialnum(alt_track);
    C_1 = repmat(1:trial_num1,trial_num2,1);
[... 276 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/gt && for f in Figure4/cal_all_dichotomies.m Figure4/CCGP_trajPhase.m Figure4/CCGP_taskSeq.m Figure4/CCGP_environment.m Figure4/decoding_CCGP_linearSVM_simple.m; do echo "=== $f"; grep -v "^\s*%" $f | grep -v "^\s*$" | grep -v "plot\|xlabel\|ylabel\|title\|figure\|xlim\|ylim\|zlim\|view\|colormap\|legend\|scatter\|adj" | head -90; done
```

```
=== Figure4/cal_all_dichotomies.m
clc
clear all
close all
animalprefix_list = {'AM2','JS17','JS21','ZT2','JS34'};% all animals
famnov_dir = '/Volumes/NovelFamiliar'; % set directory
day = 1;
ep = 6; %epoch, F = 4, N' = 6
CTXHP = 0;% CA1 = 0 , PFC = 1;
pos_interp = (0:0.005:1)';% position bins, normalized
cellthresh = 5; % minimal number of active cells per bin needed
savedata = 0; % save clusters?
trialnum_all = []; % reset matrix
for theAnimal = 1:length(animalprefix_list)
    animalprefix = animalprefix_list{theAnimal};
    dir = sprintf('%s/%s_direct/',famnov_dir,animalprefix); % set directory
    trajinfo = loaddatastruct(dir, animalprefix, 'trajinfo', day); % get trajinfo
    trajbound = trajinfo{day}{ep}.trajbound;
    trajtime_raw = trajinfo{day}{ep}.trajtime;
    wellstand = trajinfo{day}{ep}.wellstend;
[... 391 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/gt && grep -v "^\s*%" Figure4/cal_all_dichotomies.m | grep -v "^\s*$" | sed -n '/^validid/,$p' | grep -v "plot\|xlabel\|ylabel\|title\|figure\|xlim\|ylim\|zlim\|view\|colormap\|legend\|scatter\|adj" | head -60; grep -v "^\s*%" Figure4/Supplemental/decoding_dichotomy_linearSVM.m | head -50
```

```
validid = [];
for i = 1:length(spike_matrix(:,1))
    temp = spike_matrix(i,:);
    id = find(temp > 0);
    if length(id) >= cellthresh
        validid = [validid;i];
    end
end
spike_matrix = spike_matrix(validid,:);
spike_matrix_label = spike_matrix_label(validid);
rmpath(genpath('[removed: a home directory path]/Src_Matlab')) % remove the file folder that has functions with the same name as those in the UMAP toolbox
if CTXHP
    spike_umap = run_umap(spike_matrix,'min_dist',0.6,'n_neighbors',50,'metric','cosine','n_components',3,'template_file','all_PFCumap_trials_ep6.mat');
else
    spike_umap = run_umap(spike_matrix,'min_dist',0.6,'n_neighbors',50,'metric','cosine','n_components',3,'template_file','all_CA1umap_trials_ep6.mat');
end
traj1 = [255,224,224, 204,66,71]./255;
traj2 = [0,150,255, 196,242,255]./255;
traj3 = [170,245,199, 31,150,139]./255;
traj4 = [92,0,165, 188,190,221]./255;
[... 73 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/gt && grep -v "^\s*%" Figure3/cal_SI.m | grep -v "^\s*$" | grep -v "plot\|xlabel\|ylabel\|title\|figure\|xlim\|ylim\|legend\|scatter" | sed -n 1,200p | head -110
```

```
clc
clear all
close all
animalprefix_list = {'AM2','JS17','JS21','ZT2','JS34'}; % all animals
famnov_dir = '/Volumes/NovelFamiliar'; % set directory
day = 1;
eps = 4; % epochs, 2 = N, 4 = F, 6 = N'
HPCTX = 0; % HPCTX = 1, CA1; HPCTX = 0, PFC
SI_cellinfo = []; % reset matrix
for theAnimal = 1:length(animalprefix_list)
    animalprefix = animalprefix_list{theAnimal};
    dir = sprintf('%s/%s_direct/',famnov_dir,animalprefix);
    if strcmp(animalprefix,'AM2')
         exclude_list = [6,9];%AM2
    elseif strcmp(animalprefix,'JS21')
         exclude_list = [6,3;6,6;6,7;6,8;7,1;21,1;22,1;25,1];%JS21
    elseif strcmp(animalprefix,'JS17')
        exclude_list = [6,1;7,1];%JS17
    elseif strcmp(animalprefix,'ZT2')
        exclude_list = [31,1;31,5;32,2;27,1;14,10];%ZT2
[... 59 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/gt && grep -v "^\s*%" Figure3/Supplemental/cal_path_equivalence.m | grep -v "^\s*$" | grep -v "plot\|xlabel\|ylabel\|title\|figure\|xlim\|ylim\|legend\|scatter" | sed -n '/load(/,/^end/p' | head -50; grep -n "theta\|binsize\|step\|0.05\|0.2\|cellthresh\|15\|>=" Figure2/decoding_position_CA1_novelfamiliar_cross.m | head -40
```

```
load(sprintf('%s%slinfields0%d.mat',dir,animalprefix,day)); % get linearized place fields
    temp = zeros(cellnum,length(eps)); %reset matrix
    for i = 1:cellnum
          cind = cellind(i,:);
          for ep = eps
              if (length(linfields{day}{ep})>= cind(1))
                    if  (length(linfields{day}{ep}{cind(1)})>= cind(2))
                        linfield1 = linfields{day}{ep}{cind(1)}{cind(2)};
                        linfield_all = [];
                        for track = 1:4
                            temp1 = linfield1{track};
                            pos1 = temp1(:,1);
                            pos1 = pos1./max(pos1);
                            if track == 1
                                pos_match = pos1;
                            end
                            occnormrate1 = temp1(:,5);
                            a = find(~isnan(occnormrate1));
                            if ~mod(track,2) % align trajectory from the start to end
                                pos1 = 1 - pos1;
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > vcmp.py <<'EOF'
import h5py, remfile, numpy as np, hashlib
from dandi.dandiapi import DandiAPIClient
c=DandiAPIClient()
paths=['units/spike_times','units/electrodes','units/spike_times_index','intervals/trials/start_time','intervals/trials/correct','intervals/trials/start_well','intervals/trials/end_well','processing/behavior/Position/SpatialSeries/data','processing/behavior/Position/SpatialSeries/timestamps','intervals/epoch intervals/start_time']
res={}
for v in ['0.230316.2133','0.250724.2224']:
    ds=c.get_dandiset("000447",v)
    for a in ds.get_assets():
        f=h5py.File(remfile.File(a.get_content_url(follow_redirects=1, strip_query=True)),"r")
        res[(v,a.path)]=[hashlib.md5(np.ascontiguousarray(f[p][:]).tobytes()).hexdigest()[:8] for p in paths]
        res[(v,a.path)].append(str(f.attrs.get('nwb_version')))
        res[(v,a.path)].append(sorted(f['general'].keys()).__len__())
for p in sorted(set(k[1] for k in res)):
    print(p, res[('0.230316.2133',p)]==res[('0.250724.2224',p)][:len(paths)] or (res[('0.230316.2133',p)], res[('0.250724.2224',p)]))
    print('  ', res[('0.230316.2133',p)][-2:], res[('0.250724.2224',p)][-2:], res[('0.230316.2133',p)][:len(paths)]==res[('0.250724.2224',p)][:len(paths)])
EOF
python vcmp.py
```

```
sub-JDS-NFN-AM2/sub-JDS-NFN-AM2_behavior+ecephys.nwb (['fefc199c', 'f8224493', '6e90fb6e', '0730ae28', '7e4d4e6b', '6f2f13b3', 'a33d429f', 'e7909423', '81d17f00', '123ec09e', '2.6.0', 12], ['fefc199c', 'f8224493', '6e90fb6e', '0730ae28', '7e4d4e6b', '6f2f13b3', 'a33d429f', 'e7909423', '81d17f00', '123ec09e', '2.6.0', 12])
   ['2.6.0', 12] ['2.6.0', 12] True
sub-JDS-NFN-JS17/sub-JDS-NFN-JS17_behavior+ecephys.nwb (['401811b7', 'a376b1e2', '35798cff', '4b8f95c9', 'cf7343ad', '0beed701', '756dfe3b', 'c240f44a', '29dd724e', '637d8960', '2.6.0', 12], ['401811b7', 'a376b1e2', '35798cff', '4b8f95c9', 'cf7343ad', '0beed701', '756dfe3b', 'c240f44a', '29dd724e', '637d8960', '2.6.0', 12])
   ['2.6.0', 12] ['2.6.0', 12] True
sub-JDS-NFN-JS21/sub-JDS-NFN-JS21_behavior+ecephys.nwb (['64601e0d', 'c08c12ac', 'e3e19241', '5c88cdd3', '7ab22c7f', '165f170a', '3d7ad1cf', 'b127d073', '96037c1c', '4d82ceb1', '2.6.0', 12], ['64601e0d', 'c08c12ac', 'e3e19241', '5c88cdd3', '7ab22c7f', '165f170a', '3d7ad1cf', 'b127d073', '96037c1c', '4d82ceb1', '2.6.0', 12])
   ['2.6.0', 12] ['2.6.0', 12] True
sub-JDS-NFN-JS34/sub-JDS-NFN-JS34_behavior+ecephys.nwb (['b1ccb1e0', '23c8c6d2', '74749abd', 'dc84cca9', '4f901b53', 'e0985dd8', 'eb3f8a57', '01748cec', 'c40fef76', 'b6e1b384', '2.6.0', 12], ['b1ccb1e0', '23c8c6d2', '74749abd', 'dc84cca9', '4f901b53', 'e0985dd8', 'eb3f8a57', '01748cec', 'c40fef76', 'b6e1b384', '2.6.0', 12])
   ['2.6.0', 12] ['2.6.0', 12] True
sub-JDS-NFN-ZT2/sub-JDS-NFN-ZT2_behavior+ecephys.nwb (['1a5f28b3', '311db27e', '06c0a60d', '922fd63c', 'd205887a', '86c57e9d', '414bc9d1', '6ba78e30', 'b44b198e', 'a74c5167', '2.6.0', 12], ['1a5f28b3', '311db27e', '06c0a60d', '922fd63c', 'd205887a', '86c57e9d', '414bc9d1', '6ba78e30', 'b44b198e', 'a74c5167', '2.6.0', 12])
   ['2.6.0', 12] ['2.6.0', 12] True
Shell cwd was reset to
```

**Agent**

Both published versions hold identical data arrays; I'll pin the latest, 0.250724.2224. Writing the helper's loading and linearization now.

**Agent calls Write**

```json
{
 "file_path": "entries/000447-tang-2023/nfn.py",
 "content": "\"\"\"Loading and measures for dandiset 000447 (Tang, Shin & Jadhav 2023, Cell Reports 42, 112246).\n\nEach NWB file holds one rat and one day: three W-track epochs (N, F, N' in order, the dandiset's\ndescription), a trials table (one row per trajectory, with start and end well and whether it was\ncorrect), 2D position with a speed column, and sorted units with spike times. Files are streamed\nfrom the archive at the pinned version; nothing is written to disk.\n\nWhere the parameters come from (claims file claims/000447/10.1016-j.celrep.2023.112246.yaml,\n\"criterion\" of each claim, and the paper's STAR Methods, quoted as \"Methods\"):\n\n- Trajectory types follow the paper's code (cal_UMAP.m, GitHub JadhavLab/GeometricTransformation\n  at commit 5e55e69): track 1 = well 1 to 2 (OUT_L), 2 = 2 to 1 (IN_L), 3 = 1 to 3 (OUT_R),\n  4 = 3 to 1 (IN_R); well 1 is the center (the trials table says so). Linear position is the\n  distance from the center well, as in the code.\n- Linearization. The Methods project 2D positions \"onto pre-defined idealized paths along the\n  track\"; the paths are not in the dandiset. Assumption: the idealized path of a trajectory type\n  in an epoch is the pointwise median of its correct passes, each resampled to equal arc length\n  (TEMPLATE_POINTS points) over the samples where the rat moves (speed > MIN_SPEED).\n- Run periods: speed > 5 cm/s (Methods, \"locomotor periods (> 5 cm/s\"); occupancy above 20 ms\n  (Methods), which every visited bin passes at 30 frames per second. SWR times cannot be\n  excluded: the dandiset holds no ripple times (deviation).\n- Bins of 2 cm (Methods). The 1D Gaussian width is garbled in the paper's text (\"s = σ cm\");\n  SMOOTH_CM = 8 is reading (a) of the claims file (fig2d-pv-similarity); 4 and 2 cm are its\n  variants. Counts and occupancy are smoothed separately and divided, a standard choice.\n- Cell inclusion: more than 100 spikes in the epoch (Methods), CA1 mean rate below 7 Hz\n  (poolcells_acrossep.m in the paper's code). The code's per-animal interneuron lists name\n  (tetrode, cell) pairs; the files have no cell numbers, so they cannot be applied (see the\n  notebook).\n- Region of a unit: units/electrodes holds the tetrode number (see the notebook's data check),\n  and the region is the `location` of the electrode row whose label is that tetrode.\n\"\"\"\n\nfrom __future__ import annotations\n\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nfrom dandi.dandiapi import DandiAPIClient\nfrom scipy.ndimage import gaussian_filter1d\n\nDANDISET_ID = \"000447\"\nDANDISET_VERSION = \"0.250724.2224\"\nANIMALS = [\"AM2\", \"JS17\", \"JS21\", \"ZT2\", \"JS34\"]   # order of the paper's code\nEPOCHS = [\"N\", \"F\", \"N'\"]\nTRACKS = {1: \"OUT_L\", 2: \"IN_L\", 3: \"OUT_R\", 4: \"IN_R\"}\nWELLS_TO_TRACK = {(1, 2): 1, (2, 1): 2, (1, 3): 3, (3, 1): 4}\n\nMIN_SPEED = 5.0        # cm/s, Methods\nBIN_CM = 2.0           # Methods\nSMOOTH_CM = 8.0        # claims file, fig2d-pv-similarity reading (a)\nMIN_SPIKES = 100       # Methods, \"at least 100 spikes\"; the code uses > 100\nCA1_MAX_RATE = 7.0     # Hz, poolcells_acrossep.m\nPEAK_HZ = 3.0          # Methods, spatially tuned cell\nTEMPLATE_POINTS = 400  # assumption, resolution of the idealized paths (0.5 cm on a 2 m path)\nN_NORM_BINS = 101      # cal_PVsimilarity.m, (0:0.01:1)\n\n\ndef _str(v):\n    return v.decode() if isinstance(v, bytes) else str(v)\n\n\ndef asset_urls():\n    client = DandiAPIClient()\n    ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)\n    out = {}\n    for a in ds.get_assets():\n        name = a.path.split(\"/\")[0].replace(\"sub-JDS-NFN-\", \"\")\n        out[name] = (a.path, a.get_content_url(follow_redirects=1, strip_query=True))\n    return out\n\n\ndef load_animal(name, url):\n    \"\"\"Read what the analysis uses from one file: units, position, trials, epochs.\"\"\"\n    f = h5py.File(remfile.File(url), \"r\")\n    d = {\"animal\": name}\n    d[\"epochs\"] = np.c_[f[\"intervals/epoch intervals/start_time\"][:],\n                        f[\"intervals/epoch intervals/stop_time\"][:]]\n    tr = pd.DataFrame({k: f[\"intervals/trials/\" + k][:] for k in\n                       [\"start_time\", \"stop_time\", \"correct\", \"trajectory_type\", \"start_well\", \"end_well\"]})\n    tr[\"epoch\"] = [int(np.searchsorted(d[\"epochs\"][:, 0], t, side=\"right\") - 1) for t in tr.start_time]\n    tr[\"track\"] = [WELLS_TO_TRACK.get((int(a), int(b)), 0) for a, b in zip(tr.start_well, tr.end_well)]\n    d[\"trials\"] = tr\n    pos = f[\"processing/behavior/Position/SpatialSeries/data\"][:]\n    d[\"t\"] = f[\"processing/behavior/Position/SpatialSeries/timestamps\"][:]\n    d[\"x\"], d[\"y\"], d[\"speed\"] = pos[:, 0], pos[:, 1], pos[:, 2]\n    d[\"pos_comments\"] = _str(f[\"processing/behavior/Position/SpatialSeries\"].attrs.get(\"comments\", \"\"))\n    d[\"pos_unit\"] = _str(f[\"processing/behavior/Position/SpatialSeries/data\"].attrs.get(\"unit\", \"\"))\n    e = f[\"general/extracellular_ephys/electrodes\"]\n    labels = [_str(v) for v in e[\"label\"][:]]\n    locs = [_str(v) for v in e[\"location\"][:]]\n    d[\"electrode_labels\"], d[\"electrode_locations\"] = labels, locs\n    ue = f[\"units/electrodes\"][:]\n    idx = f[\"units/spike_times_index\"][:]\n    st = f[\"units/spike_times\"][:]\n    starts = np.r_[0, idx[:-1]]\n    d[\"spikes\"] = [st[a:b] for a, b in zip(starts, idx)]\n    d[\"unit_electrode_value\"] = ue\n    lab2loc = {lab: loc for lab, loc in zip(labels, locs)}\n    d[\"unit_region\"] = np.array([lab2loc.get(f\"tetrode{v}\", \"?\") for v in ue])\n    d[\"unit_region_rowreading\"] = np.array([locs[v] if v < len(locs) else \"?\" for v in ue])\n    d[\"n_units\"] = len(ue)\n    return d\n\n\ndef load_all(max_workers=5):\n    urls = asset_urls()\n    with ThreadPoolExecutor(max_workers) as ex:\n        out = list(ex.map(lambda n: load_animal(n, urls[n][1]), ANIMALS))\n    return out\n\n\n# ---------- linearization ----------\n\ndef _resample_path(xy, n):\n    seg = np.r_[0, np.cumsum(np.hypot(*np.diff(xy, axis=0).T))]\n    if seg[-1] <= 0:\n        return None\n    s = np.linspace(0, seg[-1], n)\n    return np.c_[np.interp(s, seg, xy[:, 0]), np.interp(s, seg, xy[:, 1])]\n\n\ndef build_templates(d):\n    \"\"\"Idealized path per (epoch, track): pointwise median of the correct passes (assumption).\"\"\"\n    tmpl = {}\n    tr = d[\"trials\"]\n    for ep in range(3):\n        for track in TRACKS:\n            rows = tr[(tr.epoch == ep) & (tr.track == track) & (tr.correct == 1)]\n            if len(rows) < 2:\n                rows = tr[(tr.epoch == ep) & (tr.track == track)]\n            paths = []\n            for _, r in rows.iterrows():\n                m = (d[\"t\"] >= r.start_time) & (d[\"t\"] <= r.stop_time) & (d[\"speed\"] > MIN_SPEED)\n                if m.sum() < 10:\n                    continue\n                p = _resample_path(np.c_[d[\"x\"][m], d[\"y\"][m]], TEMPLATE_POINTS)\n                if p is not None:\n                    paths.append(p)\n            if not paths:\n                continue\n            med = np.median(np.stack(paths), axis=0)\n            # re-sample the median path to equal arc length, oriented from the center well\n            med = _resample_path(med, TEMPLATE_POINTS)\n            if track in (2, 4):  # inbound: from side well to center; orient from center\n                med = med[::-1]\n            tmpl[(ep, track)] = med\n    return tmpl\n\n\ndef project(xy, path):\n    \"\"\"Arc length along `path` (from its first point) of the nearest point to each of `xy`.\"\"\"\n    seg = np.diff(path, axis=0)\n    seglen2 = (seg ** 2).sum(1)\n    cum = np.r_[0, np.cumsum(np.sqrt(seglen2))]\n    best_d = np.full(len(xy), np.inf)\n    best_s = np.zeros(len(xy))\n    for i in range(len(seg)):\n        v = xy - path[i]\n        u = np.clip((v @ seg[i]) / seglen2[i], 0, 1) if seglen2[i] > 0 else np.zeros(len(xy))\n        proj = path[i] + u[:, None] * seg[i]\n        dist = np.hypot(*(xy - proj).T)\n        better = dist < best_d\n        best_d[better] = dist[better]\n        best_s[better] = cum[i] + u[better] * np.sqrt(seglen2[i])\n    return best_s, best_d\n\n\ndef linearize(d):\n    \"\"\"Per position sample: epoch, track (0 outside the four types), linear position from the\n    center well (cm), distance to the idealized path (cm), and the trial row index.\"\"\"\n    d[\"templates\"] = build_templates(d)\n    n = len(d[\"t\"])\n    lin = np.full(n, np.nan)\n    off = np.full(n, np.nan)\n    track = np.zeros(n, int)\n    trial = np.full(n, -1)\n    epoch = np.full(n, -1)\n    for ep, (a, b) in enumerate(d[\"epochs\"]):\n        epoch[(d[\"t\"] >= a) & (d[\"t\"] <= b)] = ep\n    for i, r in d[\"trials\"].iterrows():\n        m = np.where((d[\"t\"] >= r.start_time) & (d[\"t\"] < r.stop_time))[0]\n        trial[m] = i\n        if r.track == 0 or (r.epoch, r.track) not in d[\"templates\"]:\n            continue\n        s, dist = project(np.c_[d[\"x\"][m], d[\"y\"][m]], d[\"templates\"][(r.epoch, r.track)])\n        lin[m], off[m], track[m] = s, dist, r.track\n    d[\"lin\"], d[\"lin_offset\"], d[\"track\"], d[\"trial_of_sample\"], d[\"epoch_of_sample\"] = lin, off, track, trial, epoch\n    d[\"track_length\"] = {k: float(np.sum(np.hypot(*np.diff(v, axis=0).T))) for k, v in d[\"templates\"].items()}\n    return d\n\n\n# ---------- cells ----------\n\ndef epoch_counts(d):\n    \"\"\"Spikes and mean rate (spikes over epoch duration) of every unit in every epoch.\"\"\"\n    n = np.zeros((d[\"n_units\"], 3), int)\n    for u, s in enumerate(d[\"spikes\"]):\n        for ep, (a, b) in enumerate(d[\"epochs\"]):\n            n[u, ep] = np.sum((s >= a) & (s <= b))\n    dur = d[\"epochs\"][:, 1] - d[\"epochs\"][:, 0]\n    return n, n / dur\n\n\ndef included(d, region, ep, min_spikes=MIN_SPIKES, strict=True):\n    \"\"\"Units of `region` that pass the inclusion rules in epoch `ep` (strict: > 100 spikes, as the\n    code; otherwise >= 100, as the Methods).\"\"\"\n    n, rate = epoch_counts(d)\n    ok = (n[:, ep] > min_spikes) if strict else (n[:, ep] >= min_spikes)\n    ok &= d[\"unit_region\"] == region\n    if region == \"CA1\":\n        ok &= rate[:, ep] < CA1_MAX_RATE\n    return np.where(ok)[0]\n\n\n# ---------- rate maps ----------\n\ndef _run_mask(d, ep, track=None, trial=None):\n    m = (d[\"epoch_of_sample\"] == ep) & (d[\"speed\"] > MIN_SPEED) & np.isfinite(d[\"lin\"])\n    if track is not None:\n        m &= d[\"track\"] == track\n    if trial is not None:\n        m &= d[\"trial_of_sample\"] == trial\n    return m\n\n\ndef _sample_dt(d):\n    dt = np.diff(d[\"t\"], append=d[\"t\"][-1])\n    med = np.median(dt)\n    return np.clip(dt, 0, 2 * med)\n\n\ndef rate_maps(d, ep, units, smooth_cm=SMOOTH_CM, trial=None, track_only=None):\n    \"\"\"Occupancy-normalized linearized rate maps on the four tracks for `units` in epoch `ep`.\n\n    Returns {track: (bin_centers_cm, rates[n_units, n_bins])}; NaN where occupancy is zero.\"\"\"\n    dt = _sample_dt(d)\n    out = {}\n    tracks = [track_only] if track_only else list(TRACKS)\n    for track in tracks:\n        if (ep, track) not in d[\"track_length\"]:\n            continue\n        L = d[\"track_length\"][(ep, track)]\n        edges = np.arange(0, L + BIN_CM, BIN_CM)\n        centers = edges[:-1] + BIN_CM / 2\n        m = _run_mask(d, ep, track, trial)\n        occ = np.histogram(d[\"lin\"][m], edges, weights=dt[m])[0]\n        idx = np.where(m)[0]\n        rates = np.full((len(units), len(centers)), np.nan)\n        if len(idx) == 0:\n            out[track] = (centers, rates)\n            continue\n        tt = d[\"t\"]\n        # each spike takes the sample nearest in time; it counts when that sample is in the mask\n        for k, u in enumerate(units):\n            s = d[\"spikes\"][u]\n            s = s[(s >= tt[idx[0]]) & (s <= tt[idx[-1]] + 0.05)]\n            j = np.clip(np.searchsorted(tt, s), 1, len(tt) - 1)\n            j -= (s - tt[j - 1]) < (tt[j] - s)\n            keep = m[j] & (np.abs(tt[j] - s) < 0.1)\n            cnt = np.histogram(d[\"lin\"][j[keep]], edges)[0].astype(float)\n            if smooth_cm > 0:\n                sig = smooth_cm / BIN_CM\n                cs = gaussian_filter1d(cnt, sig, mode=\"constant\")\n                os_ = gaussian_filter1d(occ, sig, mode=\"constant\")\n                with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n                    r = cs / os_\n            else:\n                with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n                    r = cnt / occ\n            r[occ <= 0.02] = np.nan\n            rates[k] = r\n        out[track] = (centers, rates)\n    return out\n\n\ndef normalized(maps, n=N_NORM_BINS, fill_nan=True):\n    \"\"\"Each track's map on `n` bins of normalized length (nearest bin, as cal_PVsimilarity.m),\n    interior NaN runs filled linearly; tracks concatenated in the order 1 to 4.\"\"\"\n    pos = np.linspace(0, 1, n)\n    cols = []\n    for track in TRACKS:\n        centers, r = maps[track]\n        r = r.copy()\n        if fill_nan:\n            for k in range(len(r)):\n                v = r[k]\n                good = np.isfinite(v)\n                if good.sum() >= 2:\n                    first, last = np.argmax(good), len(v) - 1 - np.argmax(good[::-1])\n                    inner = np.arange(first, last + 1)\n                    v[inner] = np.interp(inner, np.where(good)[0], v[good])\n        p = centers / centers.max()\n        j = np.abs(p[None, :] - pos[:, None]).argmin(1)\n        cols.append(r[:, j])\n    return np.concatenate(cols, axis=1)\n\n\ndef peak_rate(maps):\n    return np.nanmax(np.concatenate([maps[t][1] for t in TRACKS], axis=1), axis=1)\n"
}
```

```
File created successfully at: entries/000447-tang-2023/nfn.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/000447-tang-2023 && . $TMPDIR/dev/bin/activate && cat > $TMPDIR/t1.py <<'EOF'
import time, pickle, numpy as np, pandas as pd, sys
sys.path.insert(0,'.')
import nfn
t=time.time(); A=nfn.load_all(); print('load',time.time()-t)
for d in A:
    t=time.time(); nfn.linearize(d)
    n,rate=nfn.epoch_counts(d)
    tr=d['trials']
    print(d['animal'], 'linearize %.1fs'%(time.time()-t), 'units',d['n_units'], 'regions', dict(zip(*np.unique(d['unit_region'],return_counts=True))), 'row-reading', dict(zip(*np.unique(d['unit_region_rowreading'],return_counts=True))))
    print('  trials per epoch', tr.groupby('epoch').size().tolist(), 'tracks', tr.groupby(['epoch','track']).size().unstack(fill_value=0).values.tolist())
    print('  track lengths', {k:round(v) for k,v in d['track_length'].items()})
    off=d['lin_offset'][np.isfinite(d['lin_offset']) & (d['speed']>5)]
    print('  offset pct50/90/99', np.percentile(off,[50,90,99]).round(1))
    print('  speed pct', np.percentile(d['speed'],[50,90,99]).round(1), 'x range', np.nanmin(d['x']).round(), np.nanmax(d['x']).round(), 'dt', np.median(np.diff(d['t'])))
    for reg in ['CA1','PFC']:
        print('  ', reg, [len(nfn.included(d,reg,ep)) for ep in range(3)], 'any spikes', [(n[d['unit_region']==reg][:,ep]>0).sum() for ep in range(3)], '<=100', [((n[d['unit_region']==reg][:,ep]<=100)&(n[d['unit_region']==reg][:,ep]>0)).sum() for ep in range(3)])
    r=rate[d['unit_region']=='CA1']; print('   CA1 rate>=7 per epoch', (r>=7).sum(0), 'max', r.max(0).round(1))
    # appended units: ordering of electrode values
    ue=d['unit_electrode_value']; brk=np.where(np.diff(ue)<0)[0]
    print('   order breaks at', brk, 'n tail', len(ue)-brk[0]-1 if len(brk) else 0, 'tail spikes per epoch', n[brk[0]+1:].tolist() if len(brk) else '')
pickle.dump(A, open('/tmp/claude-1001/A.pkl','wb'))
EOF
python $TMPDIR/t1.py
```

```
load 6.107736349105835
AM2 linearize 1.4s units 57 regions {np.str_('CA1'): np.int64(32), np.str_('PFC'): np.int64(25)} row-reading {np.str_('CA1'): np.int64(32), np.str_('PFC'): np.int64(25)}
  trials per epoch [25, 49, 30] tracks [[10, 1, 4, 7, 3], [1, 13, 14, 11, 10], [5, 5, 6, 8, 6]]
  track lengths {(0, 1): 310, (0, 2): 220, (0, 3): 244, (0, 4): 378, (1, 1): 220, (1, 2): 205, (1, 3): 203, (1, 4): 216, (2, 1): 313, (2, 2): 202, (2, 3): 205, (2, 4): 234}
  offset pct50/90/99 [ 1.   8.1 23.2]
  speed pct [ 2.8 26.5 42.6] x range 15.0 131.0 dt 0.03040000000009968
   CA1 [29, 29, 29] any spikes [np.int64(31), np.int64(32), np.int64(32)] <=100 [np.int64(2), np.int64(3), np.int64(3)]
   PFC [25, 25, 25] any spikes [np.int64(25), np.int64(25), np.int64(25)] <=100 [np.int64(0), np.int64(0), np.int64(0)]
   CA1 rate>=7 per epoch [0 0 0] max [3.2 3.8 2.7]
   order breaks at [55] n tail 1 tail spikes per epoch [[0, 43, 35]]
JS17 linearize 2.0s units 97 regions {np.str_('CA1'): np.int64(31), np.str_('PFC'): np.int64(66)} row-reading {np.str_('CA1'): np.int64(50), np.str_('PFC'): np.int64(47)}
  trials per epoch [33, 65, 57] tracks [[8, 4, 8, 9, 4], [2, 14, 13, 18, 18], [1, 14, 13, 14, 15]]
  track lengths {(0, 1): 268, (0, 2): 260, (0, 3): 276, (0, 4): 260, (1, 1): 233, (1, 2): 225, (1, 3): 229, (1, 4): 221, (2, 1): 240, (2, 2): 209, (2, 3): 219, (2, 4): 229}
  offset pct50/90/99 [ 1.5  8.5 24.5]
  speed pct [ 2.7 34.2 49.5] x range 8.0 139.0 dt 0.030466666667052777
   CA1 [26, 25, 23] any spikes [np.int64(28), np.int64(26), np.int64(24)] <=100 [np.int64(1), np.int64(0), np.int64(0)]
   PFC [59, 60, 63] any spikes [np.int64(62), np.int64(63), np.int64(65)] <=100 [np.int64(3), np.int64(3), np.int64(2)]
   CA1 rate>=7 per epoch [1 1 1] max [33.  40.2 45.2]
   order breaks at [89 93] n tail 7 tail spikes per epoch [[0, 578, 392], [0, 1281, 1781], [0, 105, 0], [0, 61, 41], [0, 0, 1110], [0, 0, 7127], [0, 0, 3042]]
JS21 linearize 1.6s units 61 regions {np.str_('CA1'): np.int64(2
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python -c "
import pickle,numpy as np,sys; sys.path.insert(0,'.'); import nfn
A=pickle.load(open('$TMPDIR/A.pkl','rb'))
EX={'AM2':[(6,9)],'JS21':[(6,3),(6,6),(6,7),(6,8),(7,1),(21,1),(22,1),(25,1)],'JS17':[(6,1),(7,1)],'ZT2':[(31,1),(31,5),(32,2),(27,1),(14,10)],'JS34':[]}
for d in A:
    n,rate=nfn.epoch_counts(d); ue=d['unit_electrode_value']
    order=np.zeros(len(ue),int)
    for i,v in enumerate(ue): order[i]=(ue[:i]==v).sum()+1
    hi=np.where(rate.max(1)>=7)[0]
    print(d['animal'], 'high-rate units (tet, order, region, rates):', [(int(ue[i]),int(order[i]),d['unit_region'][i],rate[i].round(1).tolist()) for i in hi])
    print('   listed:', [(t,c, [ (d['unit_region'][i], rate[i].round(1).tolist()) for i in np.where((ue==t)&(order==c))[0]]) for t,c in EX[d['animal']]])
"
```

```
AM2 high-rate units (tet, order, region, rates): [(4, 2, np.str_('PFC'), [8.8, 10.2, 6.4]), (28, 1, np.str_('PFC'), [9.5, 7.8, 7.2]), (28, 2, np.str_('PFC'), [9.3, 8.4, 11.1])]
   listed: [(6, 9, [(np.str_('CA1'), [0.3, 0.4, 0.2])])]
JS17 high-rate units (tet, order, region, rates): [(1, 3, np.str_('PFC'), [23.6, 16.0, 23.7]), (1, 5, np.str_('PFC'), [10.4, 15.4, 15.6]), (4, 2, np.str_('PFC'), [6.9, 7.0, 8.1]), (6, 1, np.str_('CA1'), [33.0, 40.2, 45.2]), (13, 2, np.str_('PFC'), [8.0, 5.5, 6.0]), (13, 3, np.str_('PFC'), [4.0, 5.6, 7.6]), (16, 1, np.str_('PFC'), [13.6, 19.5, 19.7]), (16, 2, np.str_('PFC'), [9.1, 9.0, 10.9]), (18, 3, np.str_('PFC'), [3.9, 8.9, 7.8]), (19, 1, np.str_('PFC'), [20.1, 25.5, 26.1]), (20, 5, np.str_('PFC'), [5.4, 8.0, 8.8]), (28, 1, np.str_('PFC'), [33.1, 34.0, 35.0]), (17, 7, np.str_('PFC'), [0.0, 0.0, 7.0])]
   listed: [(6, 1, [(np.str_('CA1'), [33.0, 40.2, 45.2])]), (7, 1, [])]
JS21 high-rate units (tet, order, region, rates): [(1, 1, np.str_('PFC'), [9.4, 7.0, 9.1]), (6, 3, np.str_('CA1'), [14.5, 7.7, 13.3]), (6, 4, np.str_('CA1'), [26.6, 25.4, 26.5]), (6, 5, np.str_('CA1'), [15.7, 20.3, 19.7]), (6, 6, np.str_('CA1'), [39.7, 28.3, 26.6]), (7, 1, np.str_('CA1'), [24.4, 24.5, 24.9]), (20, 6, np.str_('PFC'), [8.1, 6.8, 7.0]), (20, 7, np.str_('PFC'), [8.2, 6.7, 7.0]), (25, 1, np.str_('CA1'), [30.1, 31.7, 28.9]), (30, 1, np.str_('PFC'), [6.5, 12.6, 6.1])]
   listed: [(6, 3, [(np.str_('CA1'), [14.5, 7.7, 13.3])]), (6, 6, [(np.str_('CA1'), [39.7, 28.3, 26.6])]), (6, 7, [(np.str_('CA1'), [0.0, 0.0, 0.2])]), (6, 8, [(np.str_('CA1'), [0.0, 0.0, 1.7])]), (7, 1, [(np.str_('CA1'), [24.4, 24.5, 24.9])]), (21, 1, []), (22, 1, []), (25, 1, [(np.str_('CA1'), [30.1, 31.7, 28.9])])]
ZT2 high-rate units (tet, order, region, rates): [(14, 8, np.str_('CA1'), [34.0, 40.1, 36.1]), (32, 2, np.str_('CA1'), [26.7, 33.4, 24.0]), (41, 5, np.str_('PFC'), [8.8, 9.8, 6.9]), (44, 2, np.str_('PFC'), [8.7, 18.7, 10.4]), (44, 3, np.str_('PFC'), [3.8, 6.6, 8.2]), (50, 2, np.
[... 3 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000447-tang-2023/nfn.py",
 "old_string": "def build_templates(d):\n    \"\"\"Idealized path per (epoch, track): pointwise median of the correct passes (assumption).\"\"\"\n    tmpl = {}",
 "new_string": "def well_positions(d, ep):\n    \"\"\"Median position of the rat at the end of the trajectories ending at each well.\"\"\"\n    tr = d[\"trials\"]\n    out = {}\n    for w in (1, 2, 3):\n        rows = tr[(tr.epoch == ep) & (tr.end_well == w)]\n        j = np.clip(np.searchsorted(d[\"t\"], rows.stop_time.values) - 1, 0, len(d[\"t\"]) - 1)\n        out[w] = np.array([np.nanmedian(d[\"x\"][j]), np.nanmedian(d[\"y\"][j])])\n    return out\n\n\ndef build_skeleton(d):\n    \"\"\"Idealized W paths per (epoch, track), from the well positions (assumption).\n\n    The three wells lie at the ends of three parallel arms joined by a cross bar. The arm\n    direction is perpendicular to the line from the left to the right well, pointing to where the\n    rat runs; the bar lies at the 99th percentile of run positions along that direction. Each\n    track runs center well, top of center arm, top of side arm, side well, and is oriented from\n    the center well for all four tracks (linear position = distance from the center well).\"\"\"\n    tmpl = {}\n    for ep in range(3):\n        w = well_positions(d, ep)\n        C, Lw, Rw = w[1], w[2], w[3]\n        lr = Rw - Lw\n        u = np.array([-lr[1], lr[0]]) / np.hypot(*lr)\n        m = (d[\"epoch_of_sample\"] == ep) & (d[\"speed\"] > MIN_SPEED)\n        proj = (np.c_[d[\"x\"][m], d[\"y\"][m]] - C) @ u\n        if np.nanmean(proj) < 0:\n            u, proj = -u, -proj\n        h = np.nanpercentile(proj, 99)\n        J = {k: P + (h - (P - C) @ u) * u for k, P in w.items()}\n        side = {1: 2, 2: 2, 3: 3, 4: 3}\n        for track in TRACKS:\n            s = side[track]\n            tmpl[(ep, track)] = np.array([C, J[1], J[s], w[s]])\n        d.setdefault(\"wells\", {})[ep] = w\n    return tmpl\n\n\ndef build_templates(d):\n    \"\"\"Idealized path per (epoch, track): pointwise median of the correct passes (variant).\"\"\"\n    tmpl = {}"
}
```

```
The file entries/000447-tang-2023/nfn.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000447-tang-2023/nfn.py",
 "old_string": "def linearize(d):\n    \"\"\"Per position sample: epoch, track (0 outside the four types), linear position from the\n    center well (cm), distance to the idealized path (cm), and the trial row index.\"\"\"\n    d[\"templates\"] = build_templates(d)\n    n = len(d[\"t\"])\n    lin = np.full(n, np.nan)\n    off = np.full(n, np.nan)\n    track = np.zeros(n, int)\n    trial = np.full(n, -1)\n    epoch = np.full(n, -1)\n    for ep, (a, b) in enumerate(d[\"epochs\"]):\n        epoch[(d[\"t\"] >= a) & (d[\"t\"] <= b)] = ep",
 "new_string": "def linearize(d, method=\"skeleton\"):\n    \"\"\"Per position sample: epoch, track (0 outside the four types), linear position from the\n    center well (cm), distance to the idealized path (cm), and the trial row index.\"\"\"\n    n = len(d[\"t\"])\n    epoch = np.full(n, -1)\n    for ep, (a, b) in enumerate(d[\"epochs\"]):\n        epoch[(d[\"t\"] >= a) & (d[\"t\"] <= b)] = ep\n    d[\"epoch_of_sample\"] = epoch\n    d[\"templates\"] = build_skeleton(d) if method == \"skeleton\" else build_templates(d)\n    lin = np.full(n, np.nan)\n    off = np.full(n, np.nan)\n    track = np.zeros(n, int)\n    trial = np.full(n, -1)"
}
```

```
The file entries/000447-tang-2023/nfn.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python -c "
import pickle,numpy as np,sys; sys.path.insert(0,'.'); import nfn
A=pickle.load(open('$TMPDIR/A.pkl','rb'))
for d in A:
    nfn.linearize(d)
    off=d['lin_offset'][np.isfinite(d['lin_offset']) & (d['speed']>5)]
    print(d['animal'], {k:round(v) for k,v in d['track_length'].items()}, 'offset pct50/90/99', np.percentile(off,[50,90,99]).round(1), {ep:{k:v.round() for k,v in w.items()} for ep,w in d['wells'].items()})
pickle.dump(A, open('$TMPDIR/A.pkl','wb'))
"
```

```
AM2 {(0, 1): 209, (0, 2): 209, (0, 3): 215, (0, 4): 215, (1, 1): 195, (1, 2): 195, (1, 3): 197, (1, 4): 197, (2, 1): 179, (2, 2): 179, (2, 3): 223, (2, 4): 223} offset pct50/90/99 [11.3 17.4 28.3] {0: {1: array([32., 58.]), 2: array([33., 20.]), 3: array([ 36., 101.])}, 1: {1: array([61., 87.]), 2: array([20., 88.]), 3: array([104.,  87.])}, 2: {1: array([38., 39.]), 2: array([35., 19.]), 3: array([ 38., 102.])}}
JS17 {(0, 1): 209, (0, 2): 209, (0, 3): 247, (0, 4): 247, (1, 1): 212, (1, 2): 212, (1, 3): 190, (1, 4): 190, (2, 1): 184, (2, 2): 184, (2, 3): 207, (2, 4): 207} offset pct50/90/99 [10.1 17.7 27.6] {0: {1: array([63., 96.]), 2: array([42., 96.]), 3: array([123.,  94.])}, 1: {1: array([89., 95.]), 2: array([46., 96.]), 3: array([109.,  93.])}, 2: {1: array([55., 88.]), 2: array([38., 88.]), 3: array([94., 84.])}}
JS21 {(0, 1): 190, (0, 2): 190, (0, 3): 235, (0, 4): 235, (1, 1): 228, (1, 2): 228, (1, 3): 186, (1, 4): 186, (2, 1): 213, (2, 2): 213, (2, 3): 235, (2, 4): 235} offset pct50/90/99 [ 9.7 16.9 31.3] {0: {1: array([38., 44.]), 2: array([38., 26.]), 3: array([ 40., 108.])}, 1: {1: array([88., 93.]), 2: array([27., 92.]), 3: array([107.,  92.])}, 2: {1: array([41., 50.]), 2: array([39., 11.]), 3: array([ 42., 111.])}}
ZT2 {(0, 1): 219, (0, 2): 219, (0, 3): 217, (0, 4): 217, (1, 1): 228, (1, 2): 228, (1, 3): 195, (1, 4): 195, (2, 1): 213, (2, 2): 213, (2, 3): 216, (2, 4): 216} offset pct50/90/99 [ 9.5 17.7 31. ] {0: {1: array([33., 63.]), 2: array([34., 13.]), 3: array([ 34., 112.])}, 1: {1: array([98., 93.]), 2: array([48., 94.]), 3: array([114.,  94.])}, 2: {1: array([28., 49.]), 2: array([28., 12.]), 3: array([30., 90.])}}
JS34 {(0, 1): 208, (0, 2): 208, (0, 3): 226, (0, 4): 226, (1, 1): 224, (1, 2): 224, (1, 3): 225, (1, 4): 225, (2, 1): 206, (2, 2): 206, (2, 3): 211, (2, 4): 211} offset pct50/90/99 [10.2 15.5 25.2] {0: {1: array([37., 46.]), 2: array([38., 11.]), 3: array([37., 99.])}, 1: {1: array([71., 98.]), 2: array([30., 97.]), 3: array([113., 
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python -c "
import pickle,numpy as np,sys; sys.path.insert(0,'.'); import nfn
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
A=pickle.load(open('$TMPDIR/A.pkl','rb'))
fig,ax=plt.subplots(5,3,figsize=(12,20))
for i,d in enumerate(A):
    for ep in range(3):
        m=(d['epoch_of_sample']==ep)&(d['speed']>5)
        ax[i,ep].plot(d['x'][m],d['y'][m],',',alpha=.3)
        for tr in [1,3]:
            p=d['templates'][(ep,tr)]; ax[i,ep].plot(p[:,0],p[:,1],'r-')
        ax[i,ep].set_aspect('equal'); ax[i,ep].set_title(d['animal']+str(ep))
plt.savefig('$TMPDIR/skel.png',dpi=60)
"
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/skel.png"
}
```

```
(Bash completed with no output)
```

Result: no output.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000447-tang-2023/nfn.py",
 "old_string": "    direction is perpendicular to the line from the left to the right well, pointing to where the\n    rat runs; the bar lies at the 99th percentile of run positions along that direction. Each\n    track runs center well, top of center arm, top of side arm, side well, and is oriented from\n    the center well for all four tracks (linear position = distance from the center well).\"\"\"\n    tmpl = {}\n    for ep in range(3):\n        w = well_positions(d, ep)\n        C, Lw, Rw = w[1], w[2], w[3]\n        lr = Rw - Lw\n        u = np.array([-lr[1], lr[0]]) / np.hypot(*lr)\n        m = (d[\"epoch_of_sample\"] == ep) & (d[\"speed\"] > MIN_SPEED)\n        proj = (np.c_[d[\"x\"][m], d[\"y\"][m]] - C) @ u\n        if np.nanmean(proj) < 0:\n            u, proj = -u, -proj\n        h = np.nanpercentile(proj, 99)\n        J = {k: P + (h - (P - C) @ u) * u for k, P in w.items()}",
 "new_string": "    direction is perpendicular to the line from the left to the right well, pointing to where the\n    rat runs. Each arm lies at the median lateral position of the run samples along the middle of\n    the arm (25% to 75% of its length, within 15 cm of the well), and the bar at the median\n    position, along the arms, of the run samples beyond 85% of the 99th percentile. Each track\n    runs center well, top of center arm, top of side arm, side well, and is oriented from the\n    center well for all four tracks (linear position = distance from the center well).\"\"\"\n    tmpl = {}\n    for ep in range(3):\n        w = well_positions(d, ep)\n        C, Lw, Rw = w[1], w[2], w[3]\n        lr = Rw - Lw\n        v = lr / np.hypot(*lr)\n        u = np.array([-v[1], v[0]])\n        m = (d[\"epoch_of_sample\"] == ep) & (d[\"speed\"] > MIN_SPEED)\n        xy = np.c_[d[\"x\"][m], d[\"y\"][m]] - C\n        pu, pv = xy @ u, xy @ v\n        if np.nanmean(pu) < 0:\n            u, pu = -u, -pu\n        h99 = np.nanpercentile(pu, 99)\n        h = np.nanmedian(pu[pu > 0.85 * h99])\n        w2 = {}\n        for k, P in w.items():\n            c_v, c_u = (P - C) @ v, (P - C) @ u\n            sel = (pu > 0.25 * h) & (pu < 0.75 * h) & (np.abs(pv - c_v) < 15)\n            if sel.sum() > 20:\n                c_v = np.nanmedian(pv[sel])\n            w2[k] = C + c_v * v + c_u * u\n        w = w2\n        J = {k: P + (h - (P - C) @ u) * u for k, P in w.items()}\n        C = w[1]"
}
```

```
The file entries/000447-tang-2023/nfn.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python -c "
import pickle,numpy as np,sys; sys.path.insert(0,'.'); import nfn
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
A=pickle.load(open('$TMPDIR/A.pkl','rb'))
fig,ax=plt.subplots(5,3,figsize=(12,20))
for i,d in enumerate(A):
    nfn.linearize(d)
    off=d['lin_offset'][np.isfinite(d['lin_offset']) & (d['speed']>5)]
    print(d['animal'], {k:round(v) for k,v in d['track_length'].items() if k[1] in (1,3)}, 'offset pct50/90/99', np.percentile(off,[50,90,99]).round(1))
    for ep in range(3):
        m=(d['epoch_of_sample']==ep)&(d['speed']>5)
        ax[i,ep].plot(d['x'][m],d['y'][m],',',alpha=.3)
        for tr in [1,3]:
            p=d['templates'][(ep,tr)]; ax[i,ep].plot(p[:,0],p[:,1],'r-')
        ax[i,ep].set_aspect('equal'); ax[i,ep].set_title(d['animal']+str(ep))
plt.savefig('$TMPDIR/skel.png',dpi=60)
pickle.dump(A, open('$TMPDIR/A.pkl','wb'))
"
```

```
AM2 {(0, 1): 195, (0, 3): 197, (1, 1): 183, (1, 3): 184, (2, 1): 184, (2, 3): 188} offset pct50/90/99 [ 5.1 13.  24.6]
JS17 {(0, 1): 212, (0, 3): 220, (1, 1): 199, (1, 3): 195, (2, 1): 187, (2, 3): 193} offset pct50/90/99 [ 5.4 12.6 18.9]
JS21 {(0, 1): 193, (0, 3): 199, (1, 1): 195, (1, 3): 192, (2, 1): 199, (2, 3): 202} offset pct50/90/99 [ 5.7 13.  23.3]
ZT2 {(0, 1): 195, (0, 3): 195, (1, 1): 207, (1, 3): 201, (2, 1): 199, (2, 3): 199} offset pct50/90/99 [ 5.8 13.7 21.7]
JS34 {(0, 1): 202, (0, 3): 204, (1, 1): 207, (1, 3): 205, (2, 1): 191, (2, 3): 193} offset pct50/90/99 [ 5.2 12.1 17.9]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/skel.png"
}
```

Result: no output.

**Agent**

Linearization now gives 183 to 220 cm tracks (paper: 2 m) with median 5 cm off the path. Checking the clock, then building the analyses.

**Agent calls Bash**

```bash
date -u
```

```
Fri Oct 30 03:08:59 UTC 2026
```

**Agent calls Bash**

```bash
nproc; free -g | head -2; cd $TMPDIR/gt && grep -v "^\s*%" Figure1/cal_behavperform.m | grep -v "^\s*$" | head -60; grep -n "randperm\|shuf" Figure3/cal_UMAP_FNdistance_shuffle.m | head
```

```
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          10           0           4          14
clc
clear all
close all
backprob = 1/3; %1/3 for combined performance; 0.5 for outbound vs. inbound performance
animals = {'JS34'}; % the animal name
dayfilter = '1';
runepochfilter = 'isequal($environment, ''wtrN'')'; % for novel environment only; use 'wtr2' for AM2
iterator = 'singleepochanal';
f = createfilter('animal',animals, 'days',dayfilter, 'epochs',runepochfilter, 'iterator', iterator);
f = setfilterfunction(f, 'DFAsj_calcproprewarded', {'linpos', 'pos', 'task'});
f = runfilter(f);
for a = 1:length(f)
    behavperform(1).task = 'wtr1';
    for t = 1:length(f(a).output)
        behavperform(t).reward = [];
        behavperform(t).daytrials = zeros(length(f(a).output{t}),2);
        behavperform(t).dayepoch = zeros(length(f(a).output{t}),2);
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> entries/000447-tang-2023/nfn.py <<'EOF'


# ---------- behaviour: state-space estimate of proportion correct ----------

def state_space_correct(correct, background=1 / 3, n_iter=200, tol=1e-6):
    """Smoothed probability of a correct trial (Smith et al. 2004, J Neurosci 24, 447, ref 84 of
    the paper): a random-walk state x_k with p_k = logistic(mu + x_k), mu set by the background
    probability, the noise variance and initial state fitted by EM. `background` is 1/3 for
    inbound and outbound trials together (cal_behavperform.m in the paper's code)."""
    n = np.asarray(correct, float)
    K = len(n)
    mu = np.log(background / (1 - background))
    sig2, x0 = 0.005, 0.0
    for _ in range(n_iter):
        xp, vp = np.zeros(K), np.zeros(K)
        xf, vf = np.zeros(K), np.zeros(K)
        xprev, vprev = x0, sig2
        for k in range(K):
            xp[k], vp[k] = xprev, vprev + sig2
            x = xp[k]
            for _ in range(50):  # Newton for the posterior mode
                p = 1 / (1 + np.exp(-(mu + x)))
                g = x - xp[k] - vp[k] * (n[k] - p)
                h = 1 + vp[k] * p * (1 - p)
                step = g / h
                x -= step
                if abs(step) < 1e-10:
                    break
            p = 1 / (1 + np.exp(-(mu + x)))
            xf[k], vf[k] = x, 1 / (1 / vp[k] + p * (1 - p))
            xprev, vprev = xf[k], vf[k]
        xs, vs = xf.copy(), vf.copy()
        A = np.zeros(K)
        for k in range(K - 2, -1, -1):
            A[k] = vf[k] / vp[k + 1]
            xs[k] = xf[k] + A[k] * (xs[k + 1] - xp[k + 1])
            vs[k] = vf[k] + A[k] ** 2 * (vs[k + 1] - vp[k + 1])
        cov = np.zeros(K)
        cov[1:] = A[:-1] * vs[1:]
        # initial state: x_0 before the first trial
        A0 = sig2 / (sig2 + sig2) if K else 0
        x0_s = x0 + A0 * (xs[0] - xp[0])
        v0_s = sig2 + A0 ** 2 * (vs[0] - vp[0])
        cov0 = A0 * vs[0]
        terms = vs[1:] + vs[:-1] - 2 * cov[1:] + (xs[1:] - xs[:-1]) ** 2
        t0 = vs[0] + v0_s - 2 * cov0 + (xs[0] - x0_s) ** 2
        new_sig2 = (terms.sum() + t0) / K
        new_x0 = x0_s
        done = abs(new_sig2 - sig2) < tol
        sig2, x0 = new_sig2, new_x0
        if done:
            break
    return 1 / (1 + np.exp(-(mu + xs)))


# ---------- statistics ----------

def rm_anova_tukey(values, names):
    """Repeated-measures one-way ANOVA (rows subjects, columns conditions) with Tukey's test on
    the error term of the ANOVA, as GraphPad Prism runs it after a repeated-measures ANOVA."""
    from scipy import stats
    Y = np.asarray(values, float)
    n, k = Y.shape
    gm = Y.mean()
    ss_cond = n * ((Y.mean(0) - gm) ** 2).sum()
    ss_subj = k * ((Y.mean(1) - gm) ** 2).sum()
    ss_tot = ((Y - gm) ** 2).sum()
    ss_err = ss_tot - ss_cond - ss_subj
    df_c, df_e = k - 1, (k - 1) * (n - 1)
    F = (ss_cond / df_c) / (ss_err / df_e)
    p = stats.f.sf(F, df_c, df_e)
    mse = ss_err / df_e
    rows = []
    for i in range(k):
        for j in range(i + 1, k):
            diff = Y[:, j].mean() - Y[:, i].mean()
            q = abs(diff) / np.sqrt(mse / n)
            pt = stats.studentized_range.sf(q, k, df_e)
            rows.append({"A": names[i], "B": names[j], "mean_B_minus_A": diff, "q": q, "p_tukey": pt})
    return {"F": F, "df": (df_c, df_e), "p": p}, pd.DataFrame(rows)


def anova_tukey(groups, names):
    """One-way ANOVA with Tukey's HSD."""
    from scipy import stats
    from statsmodels.stats.multicomp import pairwise_tukeyhsd
    gs = [np.asarray(g, float)[np.isfinite(g)] for g in groups]
    F, p = stats.f_oneway(*gs)
    vals = np.concatenate(gs)
    labs = np.concatenate([[nm] * len(g) for nm, g in zip(names, gs)])
    t = pairwise_tukeyhsd(vals, labs)
    df = pd.DataFrame(t._results_table.data[1:], columns=t._results_table.data[0])
    return {"F": F, "p": p, "n": [len(g) for g in gs]}, df


def kruskal_dunn(groups, names):
    """Kruskal-Wallis with Dunn's test, Bonferroni-adjusted over all pairs (GraphPad's Dunn)."""
    from scipy import stats
    import scikit_posthocs as sp
    gs = [np.asarray(g, float)[np.isfinite(g)] for g in groups]
    H, p = stats.kruskal(*gs)
    dunn = sp.posthoc_dunn(gs, p_adjust="bonferroni")
    dunn.index = names
    dunn.columns = names
    return {"H": H, "p": p, "n": [len(g) for g in gs]}, dunn


def grubbs(x):
    """Two-sided Grubbs' test for one outlier: statistic, p-value (Bonferroni bound on the
    largest studentized deviation, the usual form) and index of the most extreme value."""
    from scipy import stats
    x = np.asarray(x, float)
    x = x[np.isfinite(x)]
    n = len(x)
    sd = x.std(ddof=1)
    i = int(np.argmax(np.abs(x - x.mean())))
    G = abs(x[i] - x.mean()) / sd
    t2 = n * (n - 2) * G ** 2 / max((n - 1) ** 2 - n * G ** 2, 1e-12)
    p = min(1.0, 2 * n * stats.t.sf(np.sqrt(t2), n - 2))
    return G, p, i


def fisher_z_compare(r1, n1, r2, n2):
    from scipy import stats
    z = (np.arctanh(r1) - np.arctanh(r2)) / np.sqrt(1 / (n1 - 3) + 1 / (n2 - 3))
    return z, 2 * stats.norm.sf(abs(z))


# ---------- selectivity, path equivalence, ramping ----------

def _nearest_interp(src_x, src_y, dst_x):
    j = np.abs(src_x[None, :] - dst_x[:, None]).argmin(1)
    return src_y[j]


def selectivity(maps, k, peak_rule=">="):
    """SI(IN) and SI(OUT) of row k, as cal_SI.m: right map interpolated (nearest) to the left
    map's bins, means over bins valid on both; NaN unless the peak rate passes 3 Hz on the IN
    pair and on the OUT pair (Methods "≥ 3"; cal_SI.m "> 3" when peak_rule is ">")."""
    out = []
    for left, right in ((2, 4), (1, 3)):
        cl, rl = maps[left]
        cr, rr = maps[right]
        a = rl[k]
        b = _nearest_interp(cr / cr.max(), rr[k], cl / cl.max())
        ok = np.isfinite(a) & np.isfinite(b)
        if ok.sum() == 0:
            return np.nan, np.nan
        m1, m2 = a[ok].mean(), b[ok].mean()
        pk = max(a[ok].max(), b[ok].max())
        good = pk >= PEAK_HZ if peak_rule == ">=" else pk > PEAK_HZ
        if not good:
            return np.nan, np.nan
        out.append((m1 - m2) / (m1 + m2) if (m1 + m2) > 0 else np.nan)
    return out[0], out[1]


def path_equivalence(maps, k):
    """Median over the 6 track pairs of the Pearson r of maps aligned from start to end
    (cal_path_equivalence.m: inbound maps reversed, interpolated to the first track's bins,
    NaN bins dropped)."""
    c1 = maps[1][0]
    pm = c1 / c1.max()
    cols = []
    for track in TRACKS:
        c, r = maps[track]
        p = c / c.max()
        v = r[k]
        if track in (2, 4):
            p = 1 - p
        good = np.isfinite(v)
        if good.sum() < 2:
            return np.nan
        order = np.argsort(p[good])
        cols.append(np.interp(pm, p[good][order], v[good][order], left=np.nan, right=np.nan))
    M = np.array(cols).T
    ok = np.isfinite(M).all(1)
    rs = []
    for i in range(4):
        for j in range(i + 1, 4):
            a, b = M[ok, i], M[ok, j]
            rs.append(np.corrcoef(a, b)[0, 1] if a.std() > 0 and b.std() > 0 else np.nan)
    return np.nanmedian(rs)


def ramping(maps, k, track):
    """Ramping toward reward (Methods): Pearson r > 0.5 and p < 0.05 of rate against traversed
    position, peak rate >= 3 Hz, peak within 20 cm of the reward (the trajectory's end)."""
    from scipy import stats
    c, r = maps[track]
    v = r[k]
    traversed = c if track in (1, 3) else c.max() + BIN_CM / 2 - c
    good = np.isfinite(v)
    if good.sum() < 3 or np.nanmax(v) < PEAK_HZ or v[good].std() == 0:
        return False, np.nan, np.nan, bool(good.sum() >= 3)
    rr, p = stats.pearsonr(traversed[good], v[good])
    end = traversed.max()
    peak_at = traversed[good][np.argmax(v[good])]
    ok = (rr > 0.5) and (p < 0.05) and (end - peak_at <= 20)
    return ok, rr, p, True
EOF
cd entries/000447-tang-2023 && . $TMPDIR/dev/bin/activate && uv pip install -q scikit-posthocs && python -c "
import sys; sys.path.insert(0,'.'); import nfn, numpy as np
rng=np.random.default_rng(0); c=(rng.random(80)<np.r_[np.full(30,.3),np.full(50,.9)]).astype(int)
p=nfn.state_space_correct(c); print(p[[0,10,29,40,79]].round(2), p[:30].mean().round(2), p[30:].mean().round(2))
print(nfn.rm_anova_tukey(rng.normal(size=(5,3))+[0,1,0],['a','b','c']))
print(nfn.grubbs(np.r_[rng.normal(size=50),5]))
"
```

```
[0.43 0.32 0.54 0.88 0.62] 0.38 0.82
({'F': np.float64(3.798503395408692), 'df': (2, 8), 'p': np.float64(0.06921415210159709)},    A  B  mean_B_minus_A         q   p_tukey
0  a  b        1.785938  3.683742  0.072514
1  a  c        0.357902  0.738221  0.862969
2  b  c       -1.428037  2.945521  0.154960)
(np.float64(4.150367590296152), np.float64(0.00023343553616574257), 50)
```

**Agent calls Bash**

```bash
python - <<'EOF'
import re
s=open('nfn.py').read()
s=s.replace('def rate_maps(d, ep, units, smooth_cm=SMOOTH_CM, trial=None, track_only=None):','def rate_maps(d, ep, units, smooth_cm=SMOOTH_CM, trial=None, track_only=None, bin_cm=BIN_CM):')
s=s.replace('''        edges = np.arange(0, L + BIN_CM, BIN_CM)
        centers = edges[:-1] + BIN_CM / 2''','''        edges = np.arange(0, L + bin_cm, bin_cm)
        centers = edges[:-1] + bin_cm / 2''')
s=s.replace('''                sig = smooth_cm / BIN_CM''','''                sig = smooth_cm / bin_cm''')
open('nfn.py','w').write(s)
EOF
cat >> nfn.py <<'EOF'


# ---------- Bayesian decoding ----------

RATE_FLOOR = 1e-4  # Hz, standard choice so that log rates are finite where a template is 0


def decode_session(d, ep, units, template_maps, window=0.2, step=0.15, min_speed=MIN_SPEED,
                   well_cm=15.0, restrict_track=False, min_active=1, n_shuffles=100, rng=None):
    """Memoryless Bayesian decoder (Methods, "Bayesian decoding"): Poisson spiking, uniform prior
    over position and trajectory type, templates = `template_maps` (N' maps). Time bins of
    `window` s every `step` s in epoch `ep`; a bin is decoded when all its position samples lie
    on one trajectory type, the mean speed exceeds `min_speed`, the position is more than
    `well_cm` from a well, and at least `min_active` cells fire. The error is the distance along
    the four trajectories laid end to end (a decode onto the wrong trajectory is far), in the
    N' coordinates (the session's position scaled by the ratio of trajectory lengths); with
    `restrict_track` the decode is restricted to the current trajectory (the code's variant).
    Returns a DataFrame of bins with the error, and the errors under cell-ID shuffles of the
    templates (one shuffle, and the median over `n_shuffles`)."""
    rng = rng or np.random.default_rng(0)
    tracks = list(TRACKS)
    Ls = [template_maps[t][0].max() + BIN_CM / 2 for t in tracks]
    offsets = np.r_[0, np.cumsum(Ls)[:-1]]
    F = np.concatenate([np.nan_to_num(template_maps[t][1], nan=0.0) for t in tracks], axis=1)
    F = np.maximum(F, RATE_FLOOR)
    pos_track = np.concatenate([[t] * template_maps[t][1].shape[1] for t in tracks])
    pos_x = np.concatenate([template_maps[t][0] for t in tracks])
    pos_cat = np.concatenate([template_maps[t][0] + o for t, o in zip(tracks, offsets)])
    a, b = d["epochs"][ep]
    centers = np.arange(a + window / 2, b - window / 2, step)
    tt = d["t"]
    i0 = np.searchsorted(tt, centers - window / 2)
    i1 = np.searchsorted(tt, centers + window / 2)
    rows = []
    keep = []
    for k, (u, v) in enumerate(zip(i0, i1)):
        if v <= u:
            continue
        trk = d["track"][u:v]
        if trk[0] == 0 or not np.all(trk == trk[0]):
            continue
        if np.nanmean(d["speed"][u:v]) <= min_speed:
            continue
        lin = np.nanmean(d["lin"][u:v])
        L_ep = d["track_length"][(ep, int(trk[0]))]
        if not np.isfinite(lin) or lin < well_cm or lin > L_ep - well_cm:
            continue
        keep.append(k)
        rows.append((centers[k], int(trk[0]), lin, lin / L_ep, int(d["trial_of_sample"][u])))
    if not rows:
        return pd.DataFrame(), None
    df = pd.DataFrame(rows, columns=["t", "track", "lin", "frac", "trial"])
    edges_lo, edges_hi = df.t.values - window / 2, df.t.values + window / 2
    N = np.zeros((len(df), len(units)))
    for j, uidx in enumerate(units):
        s = d["spikes"][uidx]
        N[:, j] = np.searchsorted(s, edges_hi) - np.searchsorted(s, edges_lo)
    active = (N > 0).sum(1)
    ok = active >= min_active
    df, N = df[ok].reset_index(drop=True), N[ok]
    tri = np.array([tracks.index(t) for t in df.track])
    x_act = df.frac.values * np.array(Ls)[tri]
    act_cat = offsets[tri] + x_act

    def errors(Fm):
        ll = N @ np.log(Fm) - window * Fm.sum(0)[None, :]
        if restrict_track:
            ll = np.where(pos_track[None, :] == df.track.values[:, None], ll, -np.inf)
            j = ll.argmax(1)
            return np.abs(pos_x[j] - x_act)
        j = ll.argmax(1)
        return np.abs(pos_cat[j] - act_cat)

    df["error"] = errors(F)
    shuf = np.empty((len(df), n_shuffles))
    for s_ in range(n_shuffles):
        shuf[:, s_] = errors(F[rng.permutation(F.shape[0])])
    df["error_shuffle1"] = shuf[:, 0]
    df["error_shuffle_median"] = np.median(shuf, axis=1)
    return df, shuf


# ---------- single-trial maps and the pseudo-population ----------

def single_trial_matrix(d, ep, units, trials_by_track, n_bins=201, smooth_cm=SMOOTH_CM, bin_cm=1.0):
    """Single-trial linearized rate maps (bins of `bin_cm`) of `units`, interpolated (nearest) to
    `n_bins` bins of normalized length, as cal_UMAP.m does (NaN set to 0). Returns rows of states
    (track, trial number, bin) by cells, and their labels."""
    pos = np.linspace(0, 1, n_bins)
    X, lab = [], []
    for track, rows in trials_by_track.items():
        for tj, ti in enumerate(rows):
            m = rate_maps(d, ep, units, smooth_cm=smooth_cm, trial=ti, track_only=track, bin_cm=bin_cm)
            c, r = m[track]
            r = np.nan_to_num(r, nan=0.0)
            j = np.abs((c / c.max())[None, :] - pos[:, None]).argmin(1)
            X.append(r[:, j].T)
            lab.append(np.c_[np.full(n_bins, track), np.full(n_bins, tj), np.arange(n_bins)])
    return np.vstack(X), np.vstack(lab)


def trials_of_track(d, ep):
    tr = d["trials"]
    return {t: list(tr[(tr.epoch == ep) & (tr.track == t)].index) for t in TRACKS}
EOF
. $TMPDIR/dev/bin/activate && python -c "import sys; sys.path.insert(0,'.'); import nfn"; date -u
```

```
Fri Oct 30 03:11:23 UTC 2026
```

**Agent**

Now the first block of analyses (cell counts, PV similarity and single-cell remapping) on all five rats.

**Agent calls Bash**

```bash
cat > $TMPDIR/a1.py <<'EOF'
import pickle, sys, time, numpy as np, pandas as pd
sys.path.insert(0,'.'); import nfn
from scipy import stats
pd.set_option('display.width',200)
A=pickle.load(open('/tmp/claude-1001/A.pkl','rb'))
t=time.time()
MAPS={}
for d in A:
    allu=np.arange(d['n_units'])
    for s in (8,4,2):
        for ep in range(3):
            MAPS[(d['animal'],s,ep)]=nfn.rate_maps(d,ep,allu,smooth_cm=s)
print('maps',time.time()-t)
pickle.dump(MAPS,open('/tmp/claude-1001/MAPS.pkl','wb'))
# cells per session
rows=[]
for d in A:
    for ep in range(3):
        for reg in ['CA1','PFC']:
            rows.append(dict(animal=d['animal'],ep=nfn.EPOCHS[ep],region=reg,n=len(nfn.included(d,reg,ep))))
cnt=pd.DataFrame(rows).pivot_table(index=['animal','ep'],columns='region',values='n')
print(cnt); print(cnt.mean().round(2), cnt.std().round(2))
def pv(d,s,reg,e1,e2,rule='>='):
    cells=np.union1d(nfn.included(d,reg,e1),nfn.included(d,reg,e2))
    m1,m2=MAPS[(d['animal'],s,e1)],MAPS[(d['animal'],s,e2)]
    R1=nfn.normalized({t:(m1[t][0],m1[t][1][cells]) for t in m1})
    R2=nfn.normalized({t:(m2[t][0],m2[t][1][cells]) for t in m2})
    p1,p2=np.nanmax(R1,1),np.nanmax(R2,1)
    tuned=(p1>=3)|(p2>=3) if rule=='>=' else (p1>3)|(p2>3)
    R1,R2=np.nan_to_num(R1[tuned]),np.nan_to_num(R2[tuned])
    r=np.array([np.corrcoef(R1[:,i],R2[:,i])[0,1] if R1[:,i].std()>0 and R2[:,i].std()>0 else np.nan for i in range(R1.shape[1])])
    return r, tuned.sum()
for s in (8,4,2):
    M=[];
    for d in A:
        row=[]
        for reg in ['CA1','PFC']:
            for (e1,e2) in [(1,2),(0,2)]:
                r,n=pv(d,s,reg,e1,e2); row.append(np.nanmean(r))
        M.append(row)
    M=np.array(M)
    print('smooth',s, pd.DataFrame(M,index=nfn.ANIMALS,columns=['CA1 F-N\'','CA1 N-N\'','PFC F-N\'','PFC N-N\'']).round(3))
    a,tk=nfn.rm_anova_tukey(M,['CA1 F-N\'','CA1 N-N\'','PFC F-N\'','PFC N-N\''])
    print(a); print(tk.round(4))
EOF
cd entries/000447-tang-2023 && . $TMPDIR/dev/bin/activate && python $TMPDIR/a1.py
```

```
maps 3.4104509353637695
region      CA1   PFC
animal ep            
AM2    F   29.0  25.0
       N   29.0  25.0
       N'  29.0  25.0
JS17   F   25.0  60.0
       N   26.0  59.0
       N'  23.0  63.0
JS21   F   13.0  32.0
       N   12.0  32.0
       N'  18.0  30.0
JS34   F   36.0  12.0
       N   29.0  13.0
       N'  43.0  12.0
ZT2    F   37.0  54.0
       N   28.0  54.0
       N'  36.0  52.0
region
CA1    27.53
[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/a2.py <<'EOF'
import pickle, sys, time, numpy as np, pandas as pd
sys.path.insert(0,'.'); import nfn
from scipy import stats
pd.set_option('display.width',200)
A=pickle.load(open('/tmp/claude-1001/A.pkl','rb')); MAPS=pickle.load(open('/tmp/claude-1001/MAPS.pkl','rb'))
s=8
def norm(d,ep,cells): m=MAPS[(d['animal'],s,ep)]; return nfn.normalized({t:(m[t][0],m[t][1][cells]) for t in m})
rng=np.random.default_rng(1)
res={}
for reg in ['CA1','PFC']:
    G={'N-N\'':{'ov_a':[],'ov_b':[],'sc':[]},'F-N\'':{'ov_a':[],'ov_b':[],'sc':[]},'shuffle':{'ov_a':[],'ov_b':[],'sc':[]}}
    for d in A:
        n,rate=nfn.epoch_counts(d)
        # run-period rate: spikes during run samples / run time
        dt=nfn._sample_dt(d)
        for (e1,e2,name) in [(0,2,'N-N\''),(1,2,'F-N\''),(1,2,'shuffle')]:
            cells=np.union1d(nfn.included(d,reg,e1),nfn.included(d,reg,e2))
            R1,R2=norm(d,e1,cells),norm(d,e2,cells)
            tuned=(np.nanmax(R1,1)>=3)|(np.nanmax(R2,1)>=3)
            cells,R1,R2=cells[tuned],R1[tuned],R2[tuned]
            run=[]
            for ep in (e1,e2):
                m=nfn._run_mask(d,ep); T=dt[m].sum()
                tt=d['t']; 
                rr=[]
                for u in cells:
                    sp=d['spikes'][u]; j=np.clip(np.searchsorted(tt,sp),0,len(tt)-1); rr.append(m[j].sum()/T)
                run.append(np.array(rr))
            if name=='shuffle':
                k=len(cells); perm=np.arange(k)
                while k>1 and np.any(perm==np.arange(k)): perm=rng.permutation(k)
                R2=R2[perm]; run[1]=run[1][perm]
            ma,mb=np.nanmean(R1,1),np.nanmean(R2,1)
            G[name]['ov_a']+=list(np.minimum(ma,mb)/np.maximum(ma,mb))
            G[name]['ov_b']+=list(np.minimum(*run)/np.maximum(*run))
            for i in range(len(cells)):
                ok=np.isfinite(R1[i])&np.isfinite(R2[i])
                G[name]['sc'].append(stats.pearsonr(R1[i][ok],R2[i][ok])[0] if ok.sum()>2 and R1[i][ok].std()>0 and R2[i][ok].std()>0 else np.nan)
    for meas in ['ov_a','ov_b','sc']:
        a,t=nfn.anova_tukey([G[g][meas] for g in G],list(G))
        print(reg,meas,{g:(len(G[g][meas]),round(np.nanmedian(G[g][meas]),3)) for g in G}, 'F=%.2f p=%.2g'%(a['F'],a['p']))
        print(t)
EOF
. $TMPDIR/dev/bin/activate && python $TMPDIR/a2.py
```

```
CA1 ov_a {"N-N'": (141, np.float64(0.437)), "F-N'": (149, np.float64(0.298)), 'shuffle': (149, np.float64(0.228))} F=3.98 p=0.019
  group1   group2  meandiff   p-adj   lower   upper  reject
0   F-N'     N-N'    0.0530  0.3219 -0.0336  0.1395   False
1   F-N'  shuffle   -0.0509  0.3405 -0.1363  0.0345   False
2   N-N'  shuffle   -0.1038  0.0138 -0.1904 -0.0173    True
CA1 ov_b {"N-N'": (141, np.float64(0.486)), "F-N'": (149, np.float64(0.322)), 'shuffle': (149, np.float64(0.25))} F=3.80 p=0.023
  group1   group2  meandiff   p-adj   lower   upper  reject
0   F-N'     N-N'    0.0453  0.4544 -0.0435  0.1341   False
1   F-N'  shuffle   -0.0584  0.2611 -0.1460  0.0292   False
2   N-N'  shuffle   -0.1037  0.0173 -0.1925 -0.0148    True
CA1 sc {"N-N'": (141, np.float64(0.709)), "F-N'": (149, np.float64(-0.059)), 'shuffle': (149, np.float64(-0.096))} F=183.60 p=1.6e-55
  group1   group2  meandiff   p-adj   lower   upper  reject
0   F-N'     N-N'    0.5240  0.0000  0.4429  0.6052    True
1   F-N'  shuffle   -0.0962  0.0114 -0.1745 -0.0179    True
2   N-N'  shuffle   -0.6202  0.0000 -0.7014 -0.5390    True
PFC ov_a {"N-N'": (160, np.float64(0.697)), "F-N'": (155, np.float64(0.707)), 'shuffle': (155, np.float64(0.265))} F=73.91 p=1.3e-28
  group1   group2  meandiff   p-adj   lower   upper  reject
0   F-N'     N-N'   -0.0099  0.9419 -0.0807  0.0609   False
1   F-N'  shuffle   -0.3237  0.0000 -0.3951 -0.2524    True
2   N-N'  shuffle   -0.3138  0.0000 -0.3846 -0.2430    True
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/a3.py <<'EOF'
import pickle, sys, time, numpy as np, pandas as pd
sys.path.insert(0,'.'); import nfn
from scipy import stats
pd.set_option('display.width',200)
A=pickle.load(open('/tmp/claude-1001/A.pkl','rb')); MAPS=pickle.load(open('/tmp/claude-1001/MAPS.pkl','rb'))
def pv(d,s,reg,e1,e2):
    cells=np.union1d(nfn.included(d,reg,e1),nfn.included(d,reg,e2))
    m1,m2=MAPS[(d['animal'],s,e1)],MAPS[(d['animal'],s,e2)]
    R1=nfn.normalized({t:(m1[t][0],m1[t][1][cells]) for t in m1}); R2=nfn.normalized({t:(m2[t][0],m2[t][1][cells]) for t in m2})
    tuned=(np.nanmax(R1,1)>=3)|(np.nanmax(R2,1)>=3)
    R1,R2=np.nan_to_num(R1[tuned]),np.nan_to_num(R2[tuned])
    return np.array([np.corrcoef(R1[:,i],R2[:,i])[0,1] if R1[:,i].std()>0 and R2[:,i].std()>0 else np.nan for i in range(R1.shape[1])])
for s in (8,4,2):
  for reg in ['CA1','PFC']:
    G={nm:np.concatenate([pv(d,s,reg,e1,e2) for d in A]) for nm,(e1,e2) in {'F-N':(1,0),"F-N'":(1,2),"N-N'":(0,2)}.items()}
    a,t=nfn.anova_tukey(list(G.values()),list(G))
    print(s,reg,{k:round(np.nanmean(v),3) for k,v in G.items()},'F=%.1f p=%.2g'%(a['F'],a['p'])); print(t[['group1','group2','meandiff','p-adj']])
# S4D: per-bin mean over rats
for nm,(e1,e2) in {"F-N'":(1,2),'F-N':(1,0)}.items():
  for reg in ['CA1','PFC']:
    M=np.array([pv(d,8,reg,e1,e2) for d in A]); m=np.nanmean(M,0)
    G,p,i=nfn.grubbs(m); print(nm,reg,'all bins G=%.2f p=%.3g at bin %d'%(G,p,i), 'per track', [tuple(np.round(nfn.grubbs(m[k*101:(k+1)*101])[:2],3)) for k in range(4)], 'ends', m[[0,100,101,201,202,302,303,403]].round(2), 'mean', np.nanmean(m).round(3))
EOF
. $TMPDIR/dev/bin/activate && python $TMPDIR/a3.py
```

```
8 CA1 {'F-N': np.float64(0.062), "F-N'": np.float64(0.045), "N-N'": np.float64(0.517)} F=2372.2 p=0
  group1 group2  meandiff   p-adj
0    F-N   F-N'   -0.0174  0.0649
1    F-N   N-N'    0.4551  0.0000
2   F-N'   N-N'    0.4726  0.0000
8 PFC {'F-N': np.float64(0.774), "F-N'": np.float64(0.836), "N-N'": np.float64(0.855)} F=173.3 p=6.4e-74
  group1 group2  meandiff   p-adj
0    F-N   F-N'    0.0623  0.0000
1    F-N   N-N'    0.0813  0.0000
2   F-N'   N-N'    0.0190  0.0001
4 CA1 {'F-N': np.float64(0.061), "F-N'": np.float64(0.045), "N-N'": np.float64(0.496)} F=2110.3 p=0
  group1 group2  meandiff  p-adj
0    F-N   F-N'   -0.0162  0.098
1    F-N   N-N'    0.4343  0.000
2   F-N'   N-N'    0.4506  0.000
4 PFC {'F-N': np.float64(0.76), "F-N'": np.float64(0.825), "N-N'": np.float64(0.839)} F=165.5 p=1.1e-70
  group1 group2  meandiff   p-adj
0    F-N   F-N'    0.0654  0.0000
1    F-N   N-N'    0.0795  0.0000
2   F-N'   N-N'    0.0140  0.0075
[... 14 more lines not kept]
```

**Agent**

S3C reproduces under all three widths; S4D finds no outlier in any test. Now decoding.

**Agent calls Bash**

```bash
cat > $TMPDIR/a4.py <<'EOF'
import pickle, sys, time, numpy as np, pandas as pd
sys.path.insert(0,'.'); import nfn
from scipy import stats
pd.set_option('display.width',200)
A=pickle.load(open('/tmp/claude-1001/A.pkl','rb')); MAPS=pickle.load(open('/tmp/claude-1001/MAPS.pkl','rb'))
rng=np.random.default_rng(2)
t0=time.time()
out=[]
for d in A:
    for reg in ['CA1','PFC']:
        cells=nfn.included(d,reg,2)
        m=MAPS[(d['animal'],8,2)]
        pk=nfn.peak_rate({t:(m[t][0],m[t][1][cells]) for t in m})
        cells=cells[pk>=3]
        tm={t:(m[t][0],m[t][1][cells]) for t in m}
        for ep in (0,1):
            df,_=nfn.decode_session(d,ep,cells,tm,rng=rng)
            df['animal'],df['region'],df['env'],df['ncells']=d['animal'],reg,nfn.EPOCHS[ep],len(cells)
            out.append(df)
D=pd.concat(out); print('decode time',time.time()-t0)
print(D.groupby(['region','env','animal']).agg(n=('error','size'),ncells=('ncells','first'),med=('error','median'),shuf=('error_shuffle_median','median')).round(1))
print(D.groupby(['region','env']).agg(n=('error','size'),med=('error','median'),shuf1=('error_shuffle1','median'),shufmed=('error_shuffle_median','median')).round(1))
g={(r,e):D[(D.region==r)&(D.env==e)].error.values for r in ['CA1','PFC'] for e in ['N','F']}
a,dn=nfn.kruskal_dunn(list(g.values()),[f'{r} {e}' for r,e in g]); print(a); print(dn)
for r in ['CA1','PFC']:
    a,dn=nfn.kruskal_dunn([g[(r,'N')],g[(r,'F')]],['N','F']); print(r,a,dn.iloc[0,1])
    for e in ['N','F']:
        x=D[(D.region==r)&(D.env==e)]
        print(r,e,'wilcoxon vs shuffle1',stats.wilcoxon(x.error,x.error_shuffle1).pvalue,'vs shuffle median',stats.wilcoxon(x.error,x.error_shuffle_median).pvalue, 'median diff', np.median(x.error-x.error_shuffle_median).round(1))
D.to_pickle('/tmp/claude-1001/D.pkl')
EOF
. $TMPDIR/dev/bin/activate && python $TMPDIR/a4.py
```

```
decode time 7.489585876464844
                      n  ncells    med   shuf
region env animal                            
CA1    F   AM2     1138      23  274.5  230.4
           JS17    1227      15  179.8  213.3
           JS21     621      16  278.6  261.1
           JS34    1882      38  243.1  234.2
           ZT2     1423      32  222.3  203.0
       N   AM2      804      23  171.6  203.3
           JS17    1016      15  164.2  206.9
           JS21    1029      16  210.5  241.7
           JS34    1866      38  130.2  227.6
           ZT2     1490      32  177.7  217.0
PFC    F   AM2     1233      23  171.3  224.2
           JS17    1443      48   95.3  220.0
           JS21    1147      20  202.6  246.0
           JS34    2006      10  225.2  200.4
           ZT2     1564      39  169.5  201.9
       N   AM2      856      23   87.3  227.3
           JS17    1112      48  137.5  222.0
[... 21 more lines not kept]
```

**Agent**

Decoding errors are large even in N (CA1 median 172 cm). Checking the decoder in-sample on N' and the share of decodes onto the right trajectory.

**Agent calls Bash**

```bash
cat > $TMPDIR/a5.py <<'EOF'
import pickle, sys, time, numpy as np, pandas as pd
sys.path.insert(0,'.'); import nfn
A=pickle.load(open('/tmp/claude-1001/A.pkl','rb')); MAPS=pickle.load(open('/tmp/claude-1001/MAPS.pkl','rb'))
for d in A[:2]:
    for reg in ['CA1','PFC']:
        cells=nfn.included(d,reg,2); m=MAPS[(d['animal'],8,2)]
        pk=nfn.peak_rate({t:(m[t][0],m[t][1][cells]) for t in m}); cells=cells[pk>=3]
        tm={t:(m[t][0],m[t][1][cells]) for t in m}
        for ep in (2,0):
            for rt in (False,True):
                df,_=nfn.decode_session(d,ep,cells,tm,n_shuffles=2,restrict_track=rt)
                print(d['animal'],reg,nfn.EPOCHS[ep],'restrict' if rt else 'all','n',len(df),'median err %.1f'%df.error.median(), 'shuffle %.1f'%df.error_shuffle_median.median())
        # time-shift check: in-sample error with spikes shifted
        for sh in (-1.0,-0.2,0,0.2,1.0):
            d2=dict(d); d2['spikes']=[s+sh for s in d['spikes']]
            df,_=nfn.decode_session(d2,2,cells,tm,n_shuffles=1,restrict_track=True)
            print('   shift',sh,'median err %.1f'%df.error.median())
EOF
. $TMPDIR/dev/bin/activate && python $TMPDIR/a5.py
```

```
AM2 CA1 N' all n 1142 median err 12.8 shuffle 241.8
AM2 CA1 N' restrict n 1142 median err 6.3 shuffle 59.0
AM2 CA1 N all n 804 median err 171.6 shuffle 240.3
AM2 CA1 N restrict n 804 median err 16.6 shuffle 58.0
   shift -1.0 median err 24.4
   shift -0.2 median err 8.7
   shift 0 median err 6.3
   shift 0.2 median err 7.6
   shift 1.0 median err 24.9
AM2 PFC N' all n 1212 median err 13.0 shuffle 211.0
AM2 PFC N' restrict n 1212 median err 6.1 shuffle 60.0
AM2 PFC N all n 856 median err 87.3 shuffle 212.7
AM2 PFC N restrict n 856 median err 27.1 shuffle 58.0
   shift -1.0 median err 24.7
   shift -0.2 median err 8.3
   shift 0 median err 6.1
   shift 0.2 median err 7.9
   shift 1.0 median err 24.9
JS17 CA1 N' all n 1397 median err 15.6 shuffle 250.0
JS17 CA1 N' restrict n 1397 median err 6.4 shuffle 53.0
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/a6.py <<'EOF'
import pickle, sys, time, numpy as np, pandas as pd
sys.path.insert(0,'.'); import nfn
from scipy import stats
pd.set_option('display.width',200)
A=pickle.load(open('/tmp/claude-1001/A.pkl','rb')); MAPS=pickle.load(open('/tmp/claude-1001/MAPS.pkl','rb'))
def run(s=8, **kw):
    rng=np.random.default_rng(2); out=[]
    for d in A:
        for reg in ['CA1','PFC']:
            cells=nfn.included(d,reg,2); m=MAPS[(d['animal'],s,2)]
            pk=nfn.peak_rate({t:(m[t][0],m[t][1][cells]) for t in m}); cells=cells[pk>=3]
            tm={t:(m[t][0],m[t][1][cells]) for t in m}
            for ep in (0,1):
                df,_=nfn.decode_session(d,ep,cells,tm,rng=rng,**kw)
                df['animal'],df['region'],df['env']=d['animal'],reg,nfn.EPOCHS[ep]; out.append(df)
    return pd.concat(out)
def summ(D,label):
    g={(r,e):D[(D.region==r)&(D.env==e)] for r in ['CA1','PFC'] for e in ['N','F']}
    a,dn=nfn.kruskal_dunn([g[k].error for k in g],[f'{r} {e}' for r,e in g])
    s=[label, 'medians '+' '.join(f'{r}{e}={g[(r,e)].error.median():.0f}/{g[(r,e)].error_shuffle_median.median():.0f}' for r,e in g)]
    s.append('Dunn4 CA1 N-F p=%.2g PFC N-F p=%.2g'%(dn.loc['CA1 N','CA1 F'],dn.loc['PFC N','PFC F']))
    for r in ['CA1','PFC']:
        s.append('%s KW2 p=%.2g'%(r,stats.kruskal(g[(r,'N')].error,g[(r,'F')].error).pvalue))
        for e in ['N','F']:
            x=g[(r,e)]
            s.append('%s%s W1 p=%.2g Wmed p=%.2g meandiff=%.1f'%(r,e,stats.wilcoxon(x.error,x.error_shuffle1).pvalue,stats.wilcoxon(x.error,x.error_shuffle_median).pvalue,(x.error-x.error_shuffle_median).mean()))
    print(' | '.join(s))
summ(run(),'main')
summ(run(step=0.05),'step50')
summ(run(s=4),'s4'); summ(run(s=2),'s2')
summ(run(restrict_track=True),'restrict')
EOF
. $TMPDIR/dev/bin/activate && python $TMPDIR/a6.py
```

```
main | medians CA1N=172/222 CA1F=230/225 PFCN=149/224 PFCF=186/222 | Dunn4 CA1 N-F p=1.8e-140 PFC N-F p=7e-06 | CA1 KW2 p=1e-139 | CA1N W1 p=4e-90 Wmed p=2e-134 meandiff=-58.6 | CA1F W1 p=0.026 Wmed p=0.0092 meandiff=7.9 | PFC KW2 p=3.9e-06 | PFCN W1 p=1.8e-89 Wmed p=8.4e-73 meandiff=-41.2 | PFCF W1 p=1.1e-94 Wmed p=1.8e-30 meandiff=-25.6
step50 | medians CA1N=172/222 CA1F=230/225 PFCN=148/223 PFCF=187/221 | Dunn4 CA1 N-F p=0 PFC N-F p=1.4e-17 | CA1 KW2 p=0 | CA1N W1 p=1.3e-279 Wmed p=0 meandiff=-59.4 | CA1F W1 p=0.00098 Wmed p=1.2e-05 meandiff=7.7 | PFC KW2 p=1.1e-16 | PFCN W1 p=2.3e-264 Wmed p=1.5e-209 meandiff=-40.5 | PFCF W1 p=6.3e-275 Wmed p=6.2e-86 meandiff=-24.8
s4 | medians CA1N=175/218 CA1F=216/218 PFCN=154/222 PFCF=188/219 | Dunn4 CA1 N-F p=3e-109 PFC N-F p=9.6e-06 | CA1 KW2 p=1.2e-107 | CA1N W1 p=2.7e-87 Wmed p=2.1e-111 meandiff=-50.9 | CA1F W1 p=0.054 Wmed p=0.24 meandiff=6.2 | PFC KW2 p=4.7e-06 | PFCN W1 p=5.4e-55 Wmed p=4.8e-76 meandiff=-42.1 | PFCF W1 p=2e-23 Wmed p=2.1e-35 meandiff=-26.0
s2 | medians CA1N=182/222 CA1F=212/225 PFCN=165/230 PFCF=193/211 | Dunn4 CA1 N-F p=1.9e-88 PFC N-F p=1.6e-06 | CA1 KW2 p=9.3e-87 | CA1N W1 p=1.3e-82 Wmed p=1.1e-99 meandiff=-48.1 | CA1F W1 p=6.6e-13 Wmed p=0.0011 meandiff=-4.1 | PFC KW2 p=5.7e-07 | PFCN W1 p=1.5e-46 Wmed p=2.3e-76 meandiff=-44.2 | PFCF W1 p=4.7e-27 Wmed p=8e-17 meandiff=-15.6
restrict | medians CA1N=15/49 CA1F=57/55 PFCN=29/62 PFCF=23/62 | Dunn4 CA1 N-F p=0 PFC N-F p=6.2e-05 | CA1 KW2 p=0 | CA1N W1 p=2e-303 Wmed p=0 meandiff=-21.9 | CA1F W1 p=0.03 Wmed p=3.3e-08 meandiff=4.5 | PFC KW2 p=1.4e-05 | PFCN W1 p=6.5e-276 Wmed p=7e-303 meandiff=-25.3 | PFCF W1 p=0 Wmed p=0 meandiff=-27.9
```

**Agent calls Bash**

```bash
cat > $TMPDIR/a7.py <<'EOF'
import pickle, sys, time, numpy as np, pandas as pd
sys.path.insert(0,'.'); import nfn
from scipy import stats
pd.set_option('display.width',250)
A=pickle.load(open('/tmp/claude-1001/A.pkl','rb')); MAPS=pickle.load(open('/tmp/claude-1001/MAPS.pkl','rb'))
def run(**kw):
    rng=np.random.default_rng(3); out=[]
    for d in A:
        tr=d['trials']
        for reg in ['CA1','PFC']:
            cells=nfn.included(d,reg,2); m=MAPS[(d['animal'],8,2)]
            pk=nfn.peak_rate({t:(m[t][0],m[t][1][cells]) for t in m}); cells=cells[pk>=3]
            tm={t:(m[t][0],m[t][1][cells]) for t in m}
            for ep in (0,1):
                df,_=nfn.decode_session(d,ep,cells,tm,rng=rng,n_shuffles=1,**kw)
                ids=list(tr[tr.epoch==ep].index)
                pos={t:i for i,t in enumerate(ids)}
                df['k']=[pos.get(t,-999) for t in df.trial]; df['nk']=len(ids)
                df['animal'],df['region'],df['env']=d['animal'],reg,ep; out.append(df)
    return pd.concat(out)
def trial_test(D,reading):
    D=D.copy()
    if reading=='a':  # last 10 N trials -> -10..-1
        D['lab']=np.where(D.env==0, D.k-D.nk, D.k+1)
    else:             # code: first 10 N trials labelled -10..-1
        D['lab']=np.where(D.env==0, D.k-10, D.k+1)
    D=D[(D.lab>=-10)&(D.lab<=10)&(D.lab!=0)]
    res=[]
    for r in ['CA1','PFC']:
        x=D[D.region==r]; labs=sorted(x.lab.unique())
        a,dn=nfn.kruskal_dunn([x[x.lab==l].error for l in labs],labs)
        med=x.groupby('lab').error.median()
        res.append('%s KW p=%.2g; trial -1 median %.0f (n=%d), trial 1 median %.0f (n=%d); Dunn(-1,1) p=%.3g; uncorrected MW p=%.3g'%(r,a['p'],med[-1],(x.lab==-1).sum(),med[1],(x.lab==1).sum(),dn.loc[-1,1],stats.mannwhitneyu(x[x.lab==-1].error,x[x.lab==1].error).pvalue))
    return res
D=run()
for rd in 'ab': print('methods decoder, reading',rd, trial_test(D,rd))
D2=run(step=0.2,min_speed=-1,min_active=2,restrict_track=True)
for rd in 'ab': print('code decoder, reading',rd, trial_test(D2,rd))
EOF
. $TMPDIR/dev/bin/activate && python $TMPDIR/a7.py
```

```
methods decoder, reading a ['CA1 KW p=2.6e-67; trial -1 median 182 (n=258), trial 1 median 223 (n=191); Dunn(-1,1) p=0.00206; uncorrected MW p=4.26e-06', 'PFC KW p=8.2e-43; trial -1 median 149 (n=281), trial 1 median 200 (n=269); Dunn(-1,1) p=0.124; uncorrected MW p=0.000386']
methods decoder, reading b ['CA1 KW p=2.9e-39; trial -1 median 259 (n=114), trial 1 median 196 (n=358); Dunn(-1,1) p=0.111; uncorrected MW p=0.000703', 'PFC KW p=2.3e-19; trial -1 median 141 (n=124), trial 1 median 170 (n=449); Dunn(-1,1) p=1; uncorrected MW p=0.966']
code decoder, reading a ['CA1 KW p=3.9e-109; trial -1 median 40 (n=378), trial 1 median 46 (n=105); Dunn(-1,1) p=1; uncorrected MW p=0.00792', 'PFC KW p=1.6e-81; trial -1 median 71 (n=627), trial 1 median 48 (n=230); Dunn(-1,1) p=1; uncorrected MW p=0.000824']
code decoder, reading b ['CA1 KW p=9e-21; trial -1 median 20 (n=83), trial 1 median 27 (n=219); Dunn(-1,1) p=1; uncorrected MW p=0.0615', 'PFC KW p=1.8e-39; trial -1 median 18 (n=110), trial 1 median 41 (n=404); Dunn(-1,1) p=0.159; uncorrected MW p=0.000649']
```

**Agent**

Figure 2F depends on the reading of trial -1. Checking what the paper's code does.

**Agent calls Bash**

```bash
cd $TMPDIR/gt && grep -n "trial\|10\|-1" Figure2/decoding_position_novelfamiliar_trial_batch.m | head -40
```

```
3:%  current position using rate maps from N' in a trial-by-trial %
22:        % get trial information
26:            %----find trials-----%
30:               trajtime = trajtime(end-10+1:end,:);%last 10 trials
32:               trajtime = trajtime(1:10,:);% first 10 trials
39:                    [decodinginfo_seg,decodederror_seg] = decoding_position_PFC_novelfamiliar_trial(animalprefix,day,ep,6,current_trajtime,cellthresh);
41:                    [decodinginfo_seg,decodederror_seg] = decoding_position_CA1_novelfamiliar_trial(animalprefix,day,ep,6,current_trajtime,cellthresh);
57:    for tr = 1:10
68:tr_num = [-10:-1,1:10];
69:errorbar(tr_num,decodederror_stats(:,1),decodederror_stats(:,2)./sqrt(decodederror_stats(:,3)-1))
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/gt && sed -n 15,60p Figure2/decoding_position_novelfamiliar_trial_batch.m
```

```
cellthresh = 1; % minimal number of cells active in a time bin
%%
for theAnimal = 1:length(animalprefix_list)
    animalprefix = animalprefix_list{theAnimal};
    % set animal directory
    dir = sprintf('%s/%s_direct/',famnov_dir,animalprefix);
    for day = day_list
        % get trial information
        trajinfo = loaddatastruct(dir, animalprefix, 'trajinfo', day);
        for ep = ep_list
            disp(['Animal: ',animalprefix,' Epoch:',num2str(ep)]) % track decoding process
            %----find trials-----%
            trajbound = trajinfo{day}{ep}.trajbound;
            trajtime = trajinfo{day}{ep}.trajtime;
            if ep == 1
               trajtime = trajtime(end-10+1:end,:);%last 10 trials
            else
               trajtime = trajtime(1:10,:);% first 10 trials
            end
            
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/gt && sed -n 1,14p Figure2/decoding_position_novelfamiliar_trial_batch.m
```

```
%---------------------------------------------------------------%
%  This is the main script for get decoding error of animal's   %
%  current position using rate maps from N' in a trial-by-trial %
%  basis -- Wenbo Tang (Jan 05, 2023)                           %
%---------------------------------------------------------------%
clc
clear all
close all
%%
famnov_dir = '/Volumes/NovelFamiliar/'; % set directory
animalprefix_list = {'AM2','JS17','JS21','ZT2','JS34'};
day_list = 1;
ep_list = [2,4]; % 2 = N; 4 = F;
CTXHP = 1; % 1, PFC; 0, CA1
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat > $TMPDIR/a8.py <<'EOF'
import pickle, sys, time, numpy as np, pandas as pd
sys.path.insert(0,'.'); import nfn
from scipy import stats
pd.set_option('display.width',250)
A=pickle.load(open('/tmp/claude-1001/A.pkl','rb')); MAPS=pickle.load(open('/tmp/claude-1001/MAPS.pkl','rb'))
s=8
rows=[]
for d in A:
    for reg in ['CA1','PFC']:
        cells=np.intersect1d(np.intersect1d(nfn.included(d,reg,0),nfn.included(d,reg,1)),nfn.included(d,reg,2))
        for ep in range(3):
            m=MAPS[(d['animal'],s,ep)]
            for c in cells:
                si_in,si_out=nfn.selectivity(m,c); si_in2,si_out2=nfn.selectivity(m,c,'>')
                R=nfn.path_equivalence(m,c)
                rows.append(dict(animal=d['animal'],region=reg,unit=c,ep=ep,si_in=si_in,si_out=si_out,si_in_gt=si_in2,si_out_gt=si_out2,R=R))
S=pd.DataFrame(rows); S.to_pickle('/tmp/claude-1001/S.pkl')
print(S.groupby(['region','ep']).agg(n=('unit','size'),si=('si_in',lambda x: x.notna().sum()),R=('R',lambda x: x.notna().sum())))
def r(x,y):
    ok=np.isfinite(x)&np.isfinite(y); return stats.pearsonr(x[ok],y[ok])+(ok.sum(),)
for reg in ['CA1','PFC']:
    for nm,eps in [('pooled',[0,1,2]),("N'",[2]),('F',[1]),('N',[0])]:
        x=S[(S.region==reg)&S.ep.isin(eps)]
        rr,p,n=r(x.si_in.values,x.si_out.values); rr2,p2,n2=r(x.si_in_gt.values,x.si_out_gt.values)
        print('fig3d',reg,nm,'r=%.3f p=%.2g n=%d | >3: r=%.3f n=%d'%(rr,p,n,rr2,n2))
# fig3e: SI in F vs novel, IN and OUT pooled
for reg in ['CA1','PFC']:
    for nov in [2,0]:
        x=S[S.region==reg].pivot_table(index=['animal','unit'],columns='ep',values=['si_in','si_out'])
        a=np.r_[x[('si_in',1)],x[('si_out',1)]]; b=np.r_[x[('si_in',nov)],x[('si_out',nov)]]
        rr,p,n=r(a,b); print('fig3e',reg,'F vs',nfn.EPOCHS[nov],'r=%.3f p=%.2g n=%d'%(rr,p,n))
# path equivalence
G=[S[(S.region==reg)&(S.ep==ep)].R.dropna().values for reg in ['CA1','PFC'] for ep in range(3)]
names=[f'{reg} {nfn.EPOCHS[ep]}' for reg in ['CA1','PFC'] for ep in range(3)]
a,t=nfn.anova_tukey(G,names); print('S5D',a,{n:round(np.median(g),3) for n,g in zip(names,G)}); print(t[['group1','group2','meandiff','p-adj']])
for reg in ['CA1','PFC']:
    x=S[S.region==reg].pivot_table(index=['animal','unit'],columns='ep',values='R')
    for nov in [2,0]:
        rr,p,n=r(x[1].values,x[nov].values); print('S5E',reg,'F vs',nfn.EPOCHS[nov],'r=%.3f p=%.2g n=%d'%(rr,p,n))
for nov in [2,0]:
    xc=S[S.region=='CA1'].pivot_table(index=['animal','unit'],columns='ep',values='R'); xp=S[S.region=='PFC'].pivot_table(index=['animal','unit'],columns='ep',values='R')
    rc,_,nc=r(xc[1].values,xc[nov].values); rp,_,np_=r(xp[1].values,xp[nov].values)
    print('fisher z',nfn.EPOCHS[nov],nfn.fisher_z_compare(rp,np_,rc,nc))
# S5F
for reg in ['CA1','PFC']:
    x=S[S.region==reg]
    for col in ['si_in','si_out']:
        rr,p,n=r(x.R.values,x[col].values); ra,pa,na=r(x.R.values,np.abs(x[col].values))
        print('S5F',reg,col,'signed r=%.3f p=%.3g n=%d | abs r=%.3f p=%.3g'%(rr,p,n,ra,pa))
EOF
. $TMPDIR/dev/bin/activate && cd entries/000447-tang-2023 && python $TMPDIR/a8.py
```

```
n   si    R
region ep               
CA1    0    99   67   99
       1    99   44   99
       2    99   54   99
PFC    0   171  120  171
       1   171  110  171
       2   171  121  171
fig3d CA1 pooled r=0.284 p=0.00021 n=165 | >3: r=0.284 n=165
fig3d CA1 N' r=0.280 p=0.04 n=54 | >3: r=0.280 n=54
fig3d CA1 F r=0.127 p=0.41 n=44 | >3: r=0.127 n=44
fig3d CA1 N r=0.361 p=0.0027 n=67 | >3: r=0.361 n=67
fig3d PFC pooled r=-0.335 p=1.1e-10 n=351 | >3: r=-0.335 n=351
fig3d PFC N' r=-0.466 p=7e-08 n=121 | >3: r=-0.466 n=121
fig3d PFC F r=-0.417 p=5.8e-06 n=110 | >3: r=-0.417 n=110
fig3d PFC N r=-0.143 p=0.12 n=120 | >3: r=-0.143 n=120
fig3e CA1 F vs N' r=0.318 p=0.012 n=62
fig3e CA1 F vs N r=0.384 p=0.00086 n=72
fig3e PFC F vs N' r=0.437 p=5.2e-11 n=206
fig3e PFC F vs N r=0.363 p=2e-07 n=194
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/a9.py <<'EOF'
import pickle, sys, time, numpy as np, pandas as pd
sys.path.insert(0,'.'); import nfn
from scipy import stats
pd.set_option('display.width',250)
A=pickle.load(open('/tmp/claude-1001/A.pkl','rb')); MAPS=pickle.load(open('/tmp/claude-1001/MAPS.pkl','rb'))
rows=[]
for d in A:
    for reg in ['CA1','PFC']:
        for ep in range(3):
            m=MAPS[(d['animal'],8,ep)]
            for c in nfn.included(d,reg,ep):
                for tr in nfn.TRACKS:
                    ok,rr,p,valid=nfn.ramping(m,c,tr)
                    rows.append(dict(animal=d['animal'],region=reg,ep=ep,unit=c,track=tr,ramp=ok,valid=valid,r=rr))
R=pd.DataFrame(rows); R.to_pickle('/tmp/claude-1001/R.pkl')
for reg in ['CA1','PFC']:
    for nm,eps in [('pooled',[0,1,2]),("N'",[2])]:
        x=R[(R.region==reg)&R.ep.isin(eps)&R.valid]
        print(reg,nm,'ramping %d of %d = %.1f%%'%(x.ramp.sum(),len(x),100*x.ramp.mean()), 'all samples incl invalid', len(R[(R.region==reg)&R.ep.isin(eps)]))
# S3D trials
EOF
. $TMPDIR/dev/bin/activate && python $TMPDIR/a9.py
```

```
CA1 pooled ramping 49 of 1652 = 3.0% all samples incl invalid 1652
CA1 N' ramping 22 of 596 = 3.7% all samples incl invalid 596
PFC pooled ramping 67 of 2192 = 3.1% all samples incl invalid 2192
PFC N' ramping 22 of 728 = 3.0% all samples incl invalid 728
```

**Agent**

Ramping cell samples are 3 to 4% here, against 16 to 18% in the paper. Next, S3D (similarity over single trials).

**Agent calls Bash**

```bash
cat > $TMPDIR/a10.py <<'EOF'
import pickle, sys, time, numpy as np, pandas as pd
sys.path.insert(0,'.'); import nfn
from scipy import stats
pd.set_option('display.width',250)
A=pickle.load(open('/tmp/claude-1001/A.pkl','rb')); MAPS=pickle.load(open('/tmp/claude-1001/MAPS.pkl','rb'))
t0=time.time()
rows=[]
for d in A:
    tr=d['trials']
    for reg in ['CA1','PFC']:
        for nov_eps,name in [([0,2],'N+N\''),([0],'N'),([2],'N\'')]:
            cells=np.union1d(nfn.included(d,reg,1),np.concatenate([nfn.included(d,reg,e) for e in nov_eps]))
            mF=MAPS[(d['animal'],8,1)]
            pkF=nfn.peak_rate({t:(mF[t][0],mF[t][1][cells]) for t in mF})
            pkN=np.max([nfn.peak_rate({t:(MAPS[(d['animal'],8,e)][t][0],MAPS[(d['animal'],8,e)][t][1][cells]) for t in mF}) for e in nov_eps],0)
            cells=cells[(pkF>=3)|(pkN>=3)]
            k=0
            for e in nov_eps:
                for i in tr[(tr.epoch==e)&(tr.track>0)].index:
                    k+=1
                    track=int(tr.loc[i,'track'])
                    m=nfn.rate_maps(d,e,cells,trial=i,track_only=track)
                    c,r=m[track]
                    run=nfn._run_mask(d,e,track,i); tt=d['t'][run]
                    if len(tt)==0: continue
                    active=np.array([np.any((d['spikes'][u]>=tt[0])&(d['spikes'][u]<=tt[-1])) for u in cells])
                    frac=active.mean()
                    pos=np.linspace(0,1,101)
                    j=np.abs((c/c.max())[None,:]-pos[:,None]).argmin(1); X=np.nan_to_num(r[:,j])
                    cF,rF=mF[track]; jF=np.abs((cF/cF.max())[None,:]-pos[:,None]).argmin(1); Y=np.nan_to_num(rF[cells][:,jF])
                    pv=[np.corrcoef(X[:,b],Y[:,b])[0,1] if X[:,b].std()>0 and Y[:,b].std()>0 else np.nan for b in range(101)]
                    rows.append(dict(animal=d['animal'],region=reg,reading=name,k=k,frac=frac,pv=np.nanmean(pv),pvs=pv))
T=pd.DataFrame(rows); T.to_pickle('/tmp/claude-1001/T.pkl'); print(time.time()-t0)
print(T.groupby(['region','reading']).agg(n=('k','size'),pass80=('frac',lambda x:(x>=0.8).sum()),medfrac=('frac','median')))
for (reg,rd),x in T[T.frac>=0.8].groupby(['region','reading']):
    K=x.groupby('animal').k.max().min()
    x=x[x.k<=K]
    first=np.concatenate(x[x.k==x.k.min()].pvs.values); 
    print(reg,rd,'K',K,'animals', x.animal.nunique(), 'trial means', x.groupby('k').pv.mean().round(2).values[:5], '...', x.groupby('k').pv.mean().round(2).values[-5:])
EOF
. $TMPDIR/dev/bin/activate && python $TMPDIR/a10.py
```

```
15.541903495788574
                  n  pass80   medfrac
region reading                       
CA1    N        146      59  0.742857
       N'       252     147  0.818182
       N+N'     398     154  0.765957
PFC    N        146     146  1.000000
       N'       252     252  0.958333
       N+N'     398     396  0.929825
CA1 N K 15 animals 3 trial means [0.14 0.04 0.11 0.03 0.05] ... [0.08 0.03 0.08 0.07 0.13]
CA1 N' K 25 animals 5 trial means [0.07 0.1  0.05 0.   0.06] ... [ 0.01  0.05 -0.05  0.05 -0.03]
CA1 N+N' K 40 animals 4 trial means [0.12 0.09 0.25 0.12 0.15] ... [ 0.    0.11 -0.04  0.07 -0.05]
PFC N K 15 animals 5 trial means [0.68 0.66 0.7  0.74 0.75] ... [0.72 0.73 0.75 0.72 0.75]
PFC N' K 25 animals 5 trial means [0.74 0.74 0.78 0.77 0.76] ... [0.77 0.74 0.79 0.76 0.79]
PFC N+N' K 40 animals 5 trial means [0.69 0.67 0.71 0.74 0.75] ... [0.77 0.75 0.78 0.8  0.76]
```

**Agent calls Bash**

```bash
date -u; cat > $TMPDIR/a11.py <<'EOF'
import pickle, sys, time, numpy as np, pandas as pd
sys.path.insert(0,'.'); import nfn
from scipy import stats
import umap
pd.set_option('display.width',250)
A=pickle.load(open('/tmp/claude-1001/A.pkl','rb'))
t0=time.time()
OUT={}
for reg in ['CA1','PFC']:
    cells={d['animal']:np.intersect1d(np.intersect1d(nfn.included(d,reg,0),nfn.included(d,reg,1)),nfn.included(d,reg,2)) for d in A}
    for ep in (2,1):
        tbt={d['animal']:nfn.trials_of_track(d,ep) for d in A}
        tn={t:min(len(tbt[a][t]) for a in tbt) for t in nfn.TRACKS}
        Xs=[];lab=None
        for d in A:
            X,lab=nfn.single_trial_matrix(d,ep,cells[d['animal']],{t:tbt[d['animal']][t][:tn[t]] for t in nfn.TRACKS})
            Xs.append(X)
        X=np.hstack(Xs)
        OUT[(reg,ep)]=(X,lab,tn)
        print(reg,ep,'trialnum',tn,X.shape,'valid states',((X>0).sum(1)>=5).sum(), time.time()-t0)
pickle.dump(OUT,open('/tmp/claude-1001/ST.pkl','wb'))
for reg in ['CA1','PFC']:
    X,lab,tn=OUT[(reg,2)]; v=(X>0).sum(1)>=5
    t1=time.time()
    um=umap.UMAP(n_components=3,metric='cosine',n_neighbors=50,min_dist=0.6,random_state=0)
    E=um.fit_transform(X[v]); print('fit',reg,time.time()-t1)
    XF,labF,_=OUT[(reg,1)]; vF=(XF>0).sum(1)>=5
    t1=time.time(); EF=um.transform(XF[vF]); print('transform',time.time()-t1)
    pickle.dump((E,lab[v],EF,labF[vF],um),open(f'/tmp/claude-1001/U_{reg}.pkl','wb'))
EOF
. $TMPDIR/dev/bin/activate && python $TMPDIR/a11.py 2>&1 | grep -v Warn
```

```
Fri Oct 30 03:16:28 UTC 2026
  warn(
  warn(
CA1 2 trialnum {1: 5, 2: 6, 3: 8, 4: 6} (5025, 99) valid states 4766 0.5037851333618164
CA1 1 trialnum {1: 3, 2: 4, 3: 6, 4: 4} (3417, 99) valid states 3204 0.8127665519714355
PFC 2 trialnum {1: 5, 2: 6, 3: 8, 4: 6} (5025, 171) valid states 4807 1.5468788146972656
PFC 1 trialnum {1: 3, 2: 4, 3: 6, 4: 4} (3417, 171) valid states 3272 2.013556480407715
fit CA1 42.58614253997803
transform 51.72621965408325
fit PFC 8.770487070083618
transform 1.372758150100708
```

**Agent**

UMAP fits take under a minute. Now the manifold distances (3H, 3I, 3J) and their neural-space versions (S6).

**Agent calls Bash**

```bash
cat > $TMPDIR/a12.py <<'EOF'
import pickle, sys, time, numpy as np, pandas as pd
sys.path.insert(0,'.'); import nfn
from scipy import stats
from scipy.spatial.distance import cdist
ST=pickle.load(open('/tmp/claude-1001/ST.pkl','rb'))
def seq_dist(E,lab,tn,align):
    # lab: track, trial, bin ; mean Euclidean distance over matched bins for each trial pair
    nb=201
    idx={(int(t),int(k),int(b)):i for i,(t,k,b) in enumerate(lab)}
    out={}
    for name,pairs in {'InSeq':[(1,4),(3,2)],'OutSeq':[(1,2),(3,4)]}.items():
        vals=[]
        for a,b in pairs:
            for t1 in range(tn[a]):
                for t2 in range(tn[b]):
                    ds=[]
                    for i in range(nb):
                        j=i if align=='location' else nb-1-i
                        p,q=idx.get((a,t1,i)),idx.get((b,t2,j))
                        if p is not None and q is not None: ds.append(np.linalg.norm(E[p]-E[q]))
                    if ds: vals.append(np.mean(ds))
        out[name]=np.array(vals)
    return out
def phase_loc(E,lab,mode):
    nb=201; out={'phase':[],'location':[]}
    sel=lambda t,b: np.where((lab[:,0]==t)&(lab[:,2]==b))[0]
    for i in range(nb):
        # location: same side pairs aligned by location
        for a,b in [(1,2),(3,4)]:
            p,q=sel(a,i),sel(b,i)
            if len(p) and len(q): out['location'].append(cdist(E[p],E[q]).ravel())
        phase_pairs=[(1,4),(3,2)] if mode=='methods' else [(1,2),(3,4)]
        for a,b in phase_pairs:
            p,q=sel(a,i),sel(b,nb-1-i)
            if len(p) and len(q): out['phase'].append(cdist(E[p],E[q]).ravel())
    return {k:np.concatenate(v) for k,v in out.items()}
for reg in ['CA1','PFC']:
    E,lab,EF,labF,um=pickle.load(open(f'/tmp/claude-1001/U_{reg}.pkl','rb'))
    X,labX,tn=ST[(reg,2)]; v=(X>0).sum(1)>=5; Xv=X[v]
    XF,labXF,_=ST[(reg,1)]; vF=(XF>0).sum(1)>=5; XFv=XF[vF]
    for space,(EE,FF) in {'umap':(E,EF),'neural':(Xv,XFv)}.items():
        for align in (['location','phase'] if True else []):
            sd=seq_dist(EE,lab,tn,align)
            print(reg,space,'3H align',align,'InSeq med %.3f n=%d OutSeq med %.3f n=%d p=%.2g'%(np.median(sd['InSeq']),len(sd['InSeq']),np.median(sd['OutSeq']),len(sd['OutSeq']),stats.ranksums(sd['InSeq'],sd['OutSeq']).pvalue))
        for mode in ['methods','code']:
            pl=phase_loc(EE,lab,mode)
            print(reg,space,'3I',mode,'phase med %.3f location med %.3f p=%.2g n=%d,%d'%(np.median(pl['phase']),np.median(pl['location']),stats.ranksums(pl['phase'],pl['location']).pvalue,len(pl['phase']),len(pl['location'])))
EOF
. $TMPDIR/dev/bin/activate && python $TMPDIR/a12.py 2>&1 | grep -v -i warn
```

```
CA1 umap 3H align location InSeq med 6.420 n=78 OutSeq med 3.684 n=78 p=4.2e-27
CA1 umap 3H align phase InSeq med 7.334 n=78 OutSeq med 5.703 n=78 p=0.013
CA1 umap 3I methods phase med 6.264 location med 3.636 p=0 n=14238,14168
CA1 umap 3I code phase med 5.464 location med 3.636 p=0 n=14264,14168
CA1 neural 3H align location InSeq med 40.933 n=78 OutSeq med 37.205 n=78 p=1.2e-06
CA1 neural 3H align phase InSeq med 40.270 n=78 OutSeq med 38.961 n=78 p=0.15
CA1 neural 3I methods phase med 39.387 location med 37.299 p=2.4e-47 n=14238,14168
CA1 neural 3I code phase med 38.985 location med 37.299 p=1.1e-30 n=14264,14168
PFC umap 3H align location InSeq med 12.859 n=78 OutSeq med 13.114 n=78 p=0.068
PFC umap 3H align phase InSeq med 11.857 n=78 OutSeq med 12.068 n=78 p=0.0067
PFC umap 3I methods phase med 11.886 location med 12.197 p=5.4e-56 n=14485,14417
PFC umap 3I code phase med 11.888 location med 12.197 p=1.7e-33 n=14509,14417
PFC neural 3H align location InSeq med 99.887 n=78 OutSeq med 102.134 n=78 p=2e-05
PFC neural 3H align phase InSeq med 93.362 n=78 OutSeq med 94.973 n=78 p=3.1e-06
PFC neural 3I methods phase med 92.024 location med 102.688 p=1.9e-154 n=14485,14417
PFC neural 3I code phase med 93.641 location med 102.688 p=8.6e-92 n=14509,14417
```

**Agent**

3H and 3I reproduce in the embedding and in neural space (3H: CA1 OutSeq closer, p = 4e-27; PFC InSeq closer, p = 0.0067). Now 3J with the cell-ID shuffle.

**Agent calls Bash**

```bash
cat > $TMPDIR/a13.py <<'EOF'
import pickle, sys, time, numpy as np, pandas as pd
sys.path.insert(0,'.'); import nfn
from scipy import stats
from scipy.spatial.distance import cdist
ST=pickle.load(open('/tmp/claude-1001/ST.pkl','rb'))
def fn_dist(E,lab,EF,labF):
    key=lambda l: l[:,0]*1000+l[:,2]
    kE,kF=key(lab),key(labF)
    out=np.full(len(E),np.nan)
    for k in np.unique(kE):
        p=np.where(kE==k)[0]; q=np.where(kF==k)[0]
        if len(q): out[p]=cdist(E[p],EF[q]).mean(1)
    return out
for reg in ['CA1','PFC']:
    t0=time.time()
    E,lab,EF,labF,um=pickle.load(open(f'/tmp/claude-1001/U_{reg}.pkl','rb'))
    X,labX,tn=ST[(reg,2)]; v=(X>0).sum(1)>=5; Xv=X[v]
    rng=np.random.default_rng(5)
    Xs=Xv.copy()
    for (t,k) in {(int(a),int(b)) for a,b,_ in lab}:
        rows=np.where((lab[:,0]==t)&(lab[:,1]==k))[0]
        Xs[rows]=Xv[rows][:,rng.permutation(Xv.shape[1])]
    ES=um.transform(Xs)
    XF,labXF,_=ST[(reg,1)]; vF=(XF>0).sum(1)>=5
    real=fn_dist(E,lab,EF,labF); shuf=fn_dist(E,lab,ES,lab)
    realN=fn_dist(Xv,lab,XF[vF],labXF[vF]); shufN=fn_dist(Xv,lab,Xs,lab)
    print(reg,'3J umap real med %.3f shuffle med %.3f p=%.3g | neural real %.2f shuffle %.2f p=%.3g'%(np.nanmedian(real),np.nanmedian(shuf),stats.ranksums(real[np.isfinite(real)],shuf[np.isfinite(shuf)]).pvalue,np.nanmedian(realN),np.nanmedian(shufN),stats.ranksums(realN[np.isfinite(realN)],shufN[np.isfinite(shufN)]).pvalue), time.time()-t0)
    pickle.dump(ES,open(f'/tmp/claude-1001/ES_{reg}.pkl','wb'))
EOF
. $TMPDIR/dev/bin/activate && python $TMPDIR/a13.py 2>&1 | grep -v -i warn
```

```
CA1 3J umap real med 5.392 shuffle med 5.667 p=3.32e-36 | neural real 36.96 shuffle 40.18 p=9.18e-31 7.205430030822754
PFC 3J umap real med 11.348 shuffle med 12.381 p=3.95e-24 | neural real 93.26 shuffle 129.93 p=0 6.17099142074585
```

**Agent calls Bash**

```bash
cd $TMPDIR/gt && awk '/^for current_set = 1:length\(testing_sets/{f=1} f' Figure4/CCGP_environment.m | grep -v "^\s*%" | grep -v "plot\|scatter\|Marker\|xlabel\|ylabel" | head -75
```

```
for current_set = 1:length(testing_sets(:,1))
    Features = [];
    trajlabel = [];
    Features_test = [];
    trajlabel_test = [];
    if current_set == 1 || current_set == 3
       training_sets = testing_sets([2,4],:);
    else
       training_sets = testing_sets([1,3],:);
    end
    
    for i = 1:2
        current_tr = training_sets(i,1);
        if training_sets(i,3) < seg_id(2)
            tempid = find(spike_matrix_label_seg < (seg_id(1)+current_tr-1) & spike_matrix_label_seg >= (current_tr-1));
        else
            tempid = find(spike_matrix_label_seg < (seg_id(2)+current_tr-1) & spike_matrix_label_seg >= (seg_id(1)+current_tr-1));
        end
        current_Features = spike_umap_seg(tempid,:);
        current_trajlabel = 1*ones(length(tempid),1);
[... 55 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> nfn.py <<'EOF'


# ---------- CCGP and dichotomies ----------

EARLY_BINS = np.arange(40, 60)    # 20% to 30% of the normalized position (cal_all_dichotomies.m, id1 = 41:60)
LATE_BINS = np.arange(140, 160)   # 70% to 80% (id2 = 141:160)


def clusters(E, lab):
    """The 8 clusters: states of each track at 20-30% ('a') and 70-80% ('b') of the normalized
    position from the center well (cal_all_dichotomies.m)."""
    out = {}
    for t in TRACKS:
        for seg, bins in (("a", EARLY_BINS), ("b", LATE_BINS)):
            out[(t, seg)] = E[(lab[:, 0] == t) & np.isin(lab[:, 2], bins)]
    return out


def _phase_class(t, seg):
    # outbound: 'a' is early (1), 'b' late (2); inbound runs toward the center, so the reverse
    if t in (1, 3):
        return 1 if seg == "a" else 2
    return 2 if seg == "a" else 1


SEQ_ROWS = [(1, 3, "a"), (4, 2, "a"), (1, 3, "b"), (4, 2, "b")]   # CCGP_taskSeq.m testing_sets


def _other(seg):
    return "b" if seg == "a" else "a"


def ccgp_sets(CN, CF=None, seq_same_phase=False):
    """Training and test sets of the 16 CCGP decoders (CCGP_trajPhase.m, CCGP_taskSeq.m,
    CCGP_environment.m). With `seq_same_phase` the two clusters of a task-sequence row are taken
    at the same segment (a variant)."""
    from itertools import combinations
    sets = []

    def stack(C, items):
        X = np.vstack([C[k] for k, _ in items])
        y = np.concatenate([[c] * len(C[k]) for k, c in items])
        return X, y

    phase_train = []
    for tr in combinations(TRACKS, 3):
        test = [t for t in TRACKS if t not in tr][0]
        items = [((t, s), _phase_class(t, s)) for t in tr for s in "ab"]
        titems = [((test, s), _phase_class(test, s)) for s in "ab"]
        sets.append(("phase", f"test {TRACKS[test]}", stack(CN, items), stack(CN, titems)))
        phase_train.append((tr, items))

    def seq_items(row):
        p, q, seg = row
        return [((p, seg), 1), ((q, seg if seq_same_phase else _other(seg)), 2)]

    seq_train = []
    for i, row in enumerate(SEQ_ROWS):
        trows = [SEQ_ROWS[j] for j in ((1, 3) if i in (0, 2) else (0, 2))]
        items = sum([seq_items(r) for r in trows], [])
        sets.append(("sequence", f"test {TRACKS[row[0]]}/{TRACKS[row[1]]} {row[2]}", stack(CN, items), stack(CN, seq_items(row))))
        seq_train.append((row, items))
    if CF is not None:
        for tr, items in phase_train:
            sets.append(("environment", "phase, train " + "+".join(TRACKS[t] for t in tr), stack(CN, items), stack(CF, items)))
        for row, items in seq_train:
            sets.append(("environment", f"sequence, held out {TRACKS[row[0]]}/{TRACKS[row[1]]} {row[2]}", stack(CN, items), stack(CF, items)))
    return sets


def balanced_accuracy(y, p):
    return 0.5 * (np.mean(p[y == 1] == 1) + np.mean(p[y == 2] == 2))


def svm_ccgp(train, test, n_perm=1000, rng=None):
    """Linear C-SVM (libsvm through scikit-learn, C = 1, as `-s 0 -t 0`), balanced accuracy on
    the test set, and the trial-label permutation test of decoding_CCGP_linearSVM_simple.m
    (train and test labels shuffled; p = fraction of shuffles above the real value)."""
    from sklearn.svm import SVC
    rng = rng or np.random.default_rng(0)
    (Xtr, ytr), (Xte, yte) = train, test
    acc = balanced_accuracy(yte, SVC(kernel="linear", C=1.0).fit(Xtr, ytr).predict(Xte))
    null = np.empty(n_perm)
    for i in range(n_perm):
        m = SVC(kernel="linear", C=1.0).fit(Xtr, rng.permutation(ytr))
        null[i] = balanced_accuracy(rng.permutation(yte), m.predict(Xte))
    return acc, null, float(np.mean(null > acc))
EOF
cat > $TMPDIR/a14.py <<'EOF'
import pickle, sys, time, numpy as np
sys.path.insert(0,'.'); import nfn
for reg in ['PFC','CA1']:
    E,lab,EF,labF,um=pickle.load(open(f'/tmp/claude-1001/U_{reg}.pkl','rb'))
    CN,CF=nfn.clusters(E,lab),nfn.clusters(EF,labF)
    print(reg,{k:len(v) for k,v in CN.items()},{k:len(v) for k,v in CF.items()})
    sets=nfn.ccgp_sets(CN,CF)
    t0=time.time()
    for kind,name,tr,te in sets:
        acc,null,p=nfn.svm_ccgp(tr,te,n_perm=50)
        print(reg,kind,name,'acc %.3f null95 %.3f p %.3f'%(acc,np.percentile(null,95),p))
    print('time for 16 x 50 perms', time.time()-t0)
EOF
. $TMPDIR/dev/bin/activate && python $TMPDIR/a14.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/a14.py", line 2, in <module>
    sys.path.insert(0,'.'); import nfn
                            ^^^^^^^^^^
  File "nfn.py", line 5, in <module>
    EARLY_BINS = np.arange(40, 60)    # 20% to 30% of the normalized position (cal_all_dichotomies.m, id1 = 41:60)
                 ^^
NameError: name 'np' is not defined
```

**Agent**

The append went to a stray `nfn.py` at the repository root (the shell's directory had reset). Moving it into the entry's helper.

**Agent calls Bash**

```bash
head -3 nfn.py && cat nfn.py >> entries/000447-tang-2023/nfn.py && rm nfn.py && git status --short && cd entries/000447-tang-2023 && . $TMPDIR/dev/bin/activate && python $TMPDIR/a14.py
```

```
# ---------- CCGP and dichotomies ----------
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
?? entries/000447-tang-2023/
?? scripts
PFC {(1, 'a'): 97, (1, 'b'): 99, (2, 'a'): 119, (2, 'b'): 117, (3, 'a'): 156, (3, 'b'): 159, (4, 'a'): 119, (4, 'b'): 118} {(1, 'a'): 60, (1, 'b'): 58, (2, 'a'): 78, (2, 'b'): 79, (3, 'a'): 120, (3, 'b'): 118, (4, 'a'): 80, (4, 'b'): 78}
PFC phase test IN_R acc 0.491 null95 0.534 p 0.540
PFC phase test OUT_R acc 0.512 null95 0.544 p 0.220
PFC phase test IN_L acc 0.503 null95 0.543 p 0.360
PFC phase test OUT_L acc 0.522 null95 0.553 p 0.180
PFC sequence test OUT_L/OUT_R a acc 0.585 null95 0.540 p 0.000
PFC sequence test IN_R/IN_L a acc 0.579 null95 0.500 p 0.000
[... 29 more lines not kept]
```

**Agent**

CCGP in PFC comes out near chance (phase decoders 0.49 to 0.52), unlike the paper. Before going further, a look at the embeddings themselves.

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python -c "
import pickle,numpy as np
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
fig=plt.figure(figsize=(16,8))
for i,reg in enumerate(['CA1','PFC']):
    E,lab,EF,labF,um=pickle.load(open(f'$TMPDIR/U_{reg}.pkl','rb'))
    for j,(a,b) in enumerate([(0,1),(0,2),(1,2)]):
        ax=fig.add_subplot(2,4,i*4+j+1)
        for t,c in zip([1,2,3,4],['r','b','g','m']):
            m=lab[:,0]==t; ax.scatter(E[m,a],E[m,b],s=1,c=c,alpha=.3)
    ax=fig.add_subplot(2,4,i*4+4)
    for t,c in zip([1,2,3,4],['r','b','g','m']):
        m=lab[:,0]==t; ax.scatter(lab[m,2],E[m,0],s=1,c=c,alpha=.3)
plt.savefig('$TMPDIR/umap.png',dpi=50)
"
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/umap.png"
}
```

```
(Bash completed with no output)
```

Result: no output.

**Agent**

The PFC embedding splits into bands that do not change along the trajectory. Checking whether they are trials.

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python -c "
import pickle,numpy as np
E,lab,EF,labF,um=pickle.load(open('$TMPDIR/U_PFC.pkl','rb'))
from sklearn.cluster import KMeans
km=KMeans(8,n_init=5,random_state=0).fit(E); c=km.labels_
import pandas as pd
print(pd.crosstab(c,lab[:,1]))
print(pd.crosstab(c,lab[:,0]))
ST=pickle.load(open('$TMPDIR/ST.pkl','rb'))
X,l,tn=ST[('PFC',2)]
v=(X>0).sum(1)>=5
print('row norm by trial', pd.Series(np.linalg.norm(X[v],axis=1)).groupby(lab[:,1]).median().round(1).tolist())
"
```

```
col_0    0    1    2    3    4    5   6   7
row_0                                      
0      136  126  132  118  117   84  24  32
1      147  145  124  123  122   85  29  27
2       37   66   51   53   55   43  16   9
3        9   17   13   14   18   18   4   6
4      122  106  120  148  116   87  36  23
5      204  176  171  152  177  124  43  41
6       97  114  118  121  118   85  21  34
7       34   33   40   32   51   38   9  16
col_0    1    2    3    4
row_0                    
0      164  200  232  173
1      159  197  232  214
2       63   97   88   82
3       13   20   41   25
4      157  189  206  206
5      219  246  389  234
6      147  138  263  160
7       64   49   69   71
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python -c "
import pickle,numpy as np, pandas as pd, sys
sys.path.insert(0,'.'); import nfn
A=pickle.load(open('$TMPDIR/A.pkl','rb'))
E,lab,EF,labF,um=pickle.load(open('$TMPDIR/U_PFC.pkl','rb'))
ST=pickle.load(open('$TMPDIR/ST.pkl','rb'))
X,l,tn=ST[('PFC',2)]; v=(X>0).sum(1)>=5; X=X[v]
sizes=[len(np.intersect1d(np.intersect1d(nfn.included(d,'PFC',0),nfn.included(d,'PFC',1)),nfn.included(d,'PFC',2))) for d in A]
edges=np.r_[0,np.cumsum(sizes)]
pat=np.array([[X[:,edges[i]:edges[i+1]].sum(1)==0 for i in range(5)]]).squeeze().T
print(sizes)
key=[''.join('0' if z else '1' for z in r) for r in pat]
from sklearn.cluster import KMeans
c=KMeans(8,n_init=5,random_state=0).fit(E).labels_
print(pd.crosstab(c,np.array(key)))
"
```

```
[25, 56, 30, 48, 12]
col_0  00001  00010  00011  00100  ...  11100  11101  11110  11111
row_0                              ...                            
0          0      0     98      0  ...      0      0      0      0
1          0      0      0      0  ...      0      0    140    216
2         65      0      0      0  ...      0      0      0      0
3          0      0      0     99  ...      0      0      0      0
4          0      0      0      0  ...    134    152      0      0
5          0      0      0      0  ...      0      0    180    351
6          0    151      0      0  ...      0      0      0      0
7          0      0      0      0  ...      0      0      0      0

[8 rows x 31 columns]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000447-tang-2023/nfn.py",
 "old_string": "            c, r = m[track]\n            r = np.nan_to_num(r, nan=0.0)\n            j = np.abs((c / c.max())[None, :] - pos[:, None]).argmin(1)",
 "new_string": "            c, r = m[track]\n            if fill_gaps:\n                r = r.copy()\n                good = np.isfinite(r[0]) if len(r) else np.array([])\n                if good.sum() >= 2:\n                    first, last = np.argmax(good), len(good) - 1 - np.argmax(good[::-1])\n                    inner = np.arange(first, last + 1)\n                    for k in range(len(r)):\n                        r[k, inner] = np.interp(inner, np.where(good)[0], r[k, good])\n            r = np.nan_to_num(r, nan=0.0)\n            j = np.abs((c / c.max())[None, :] - pos[:, None]).argmin(1)"
}
```

```
The file entries/000447-tang-2023/nfn.py has been updated successfully. (note: the file had been modified on disk since you last read it — the edit applied cleanly, but the file contains other changes not in your context. Read it before edits that depend on surrounding content.)
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='entries/000447-tang-2023/nfn.py'
s=open(p).read()
s=s.replace('''def single_trial_matrix(d, ep, units, trials_by_track, n_bins=201, smooth_cm=SMOOTH_CM, bin_cm=1.0):
    """Single-trial linearized rate maps (bins of `bin_cm`) of `units`, interpolated (nearest) to
    `n_bins` bins of normalized length, as cal_UMAP.m does (NaN set to 0). Returns rows of states
    (track, trial number, bin) by cells, and their labels."""''','''def single_trial_matrix(d, ep, units, trials_by_track, n_bins=201, smooth_cm=SMOOTH_CM, bin_cm=1.0,
                        fill_gaps=True):
    """Single-trial linearized rate maps (bins of `bin_cm`, 1 cm in the Methods) of `units`,
    interpolated (nearest) to `n_bins` bins of normalized length, as cal_UMAP.m does (NaN set to
    0). In one pass many 1-cm bins hold no position sample at 30 frames per second; with
    `fill_gaps` (an assumption) the empty bins inside the visited stretch are filled linearly,
    as cal_PVsimilarity.m fills session maps, so that no animal's block of cells is set to 0 at
    a bin the rat ran through. Returns rows of states (track, trial number, bin) by cells, and
    their labels."""''')
open(p,'w').write(s)
EOF
cd entries/000447-tang-2023 && . $TMPDIR/dev/bin/activate && python $TMPDIR/a11.py 2>&1 | grep -v -i warn && python $TMPDIR/a12.py 2>&1 | grep -v -i warn && python $TMPDIR/a13.py 2>&1 | grep -v -i warn && python $TMPDIR/a14.py
```

```
CA1 2 trialnum {1: 5, 2: 6, 3: 8, 4: 6} (5025, 99) valid states 5020 0.517812967300415
CA1 1 trialnum {1: 3, 2: 4, 3: 6, 4: 4} (3417, 99) valid states 3417 0.8306879997253418
PFC 2 trialnum {1: 5, 2: 6, 3: 8, 4: 6} (5025, 171) valid states 5023 1.5874779224395752
PFC 1 trialnum {1: 3, 2: 4, 3: 6, 4: 4} (3417, 171) valid states 3417 2.078012704849243
fit CA1 33.605562925338745
transform 3.5423049926757812
fit PFC 7.804651737213135
transform 2.1185455322265625
CA1 umap 3H align location InSeq med 17.081 n=78 OutSeq med 13.831 n=78 p=0.00067
CA1 umap 3H align phase InSeq med 18.117 n=78 OutSeq med 14.137 n=78 p=0.0021
CA1 umap 3I methods phase med 17.980 location med 13.843 p=0 n=15644,15647
CA1 umap 3I code phase med 15.114 location med 13.843 p=7.7e-43 n=15647,15647
CA1 neural 3H align location InSeq med 52.149 n=78 OutSeq med 45.042 n=78 p=2.5e-12
CA1 neural 3H align phase InSeq med 47.951 n=78 OutSeq med 47.715 n=78 p=0.45
CA1 neural 3I methods phase med 48.368 location med 45.025 p=9.3e-129 n=15644,15647
CA1 neural 3I code phase med 48.013 location med 45.025 p=1.9e-124 n=15647,15647
PFC umap 3H align location InSeq med 15.253 n=78 OutSeq med 17.219 n=78 p=0.081
PFC umap 3H align phase InSeq med 14.717 n=78 OutSeq med 16.825 n=78 p=0.015
PFC umap 3I methods phase med 14.521 location med 16.910 p=4.7e-181 n=15668,15662
PFC umap 3I code phase med 17.195 location med 16.910 p=0.0058 n=15662,15662
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
date -u
```

```
Fri Oct 30 03:23:28 UTC 2026
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python -c "
import pickle,sys,numpy as np,pandas as pd; sys.path.insert(0,'.'); import nfn
A=pickle.load(open('$TMPDIR/A.pkl','rb'))
M=[];M2=[]
for d in A:
    tr=d['trials']
    nov=tr[tr.epoch.isin([0,2])]; p=nfn.state_space_correct(nov.correct.values)
    pN=p[nov.epoch.values==0].mean(); pN2=p[nov.epoch.values==2].mean()
    f=tr[tr.epoch==1]; pF=nfn.state_space_correct(f.correct.values).mean()
    M.append([pN,pF,pN2])
    M2.append([nfn.state_space_correct(tr[tr.epoch==e].correct.values).mean() for e in range(3)])
    print(d['animal'], [len(tr[tr.epoch==e]) for e in range(3)], 'raw', [tr[tr.epoch==e].correct.mean().round(3) for e in range(3)], 'ss', np.round(M[-1],3), np.round(M2[-1],3))
for MM in (M,M2):
    a,t=nfn.rm_anova_tukey(np.array(MM),['N','F',\"N'\"]); print(a); print(t.round(4))
import time; from sklearn.svm import SVC; from sklearn.model_selection import cross_val_score
X=np.random.randn(1200,3); y=np.r_[np.ones(600),2*np.ones(600)]; X[y==1]+=0.5
t=time.time(); [cross_val_score(SVC(kernel='linear'),X,np.random.permutation(y),cv=4) for _ in range(20)]; print('20 shuffled 4-fold',time.time()-t)
"
```

```
AM2 [25, 49, 30] raw [np.float64(0.56), np.float64(0.816), np.float64(0.767)] ss [0.647 0.816 0.688] [0.556 0.816 0.67 ]
JS17 [33, 65, 57] raw [np.float64(0.697), np.float64(0.831), np.float64(0.86)] ss [0.718 0.832 0.835] [0.692 0.832 0.814]
JS21 [30, 48, 38] raw [np.float64(0.6), np.float64(0.854), np.float64(0.816)] ss [0.631 0.854 0.784] [0.602 0.854 0.765]
ZT2 [42, 24, 60] raw [np.float64(0.643), np.float64(0.5), np.float64(0.817)] ss [0.683 0.401 0.784] [0.643 0.401 0.813]
JS34 [69, 82, 88] raw [np.float64(0.71), np.float64(0.78), np.float64(0.83)] ss [0.7   0.778 0.828] [0.706 0.778 0.827]
{'F': np.float64(1.0849937514811256), 'df': (2, 8), 'p': np.float64(0.38289374432093304)}
   A   B  mean_B_minus_A       q  p_tukey
0  N   F          0.0604  1.1614   0.7012
1  N  N'          0.1080  2.0785   0.3540
2  F  N'          0.0477  0.9170   0.7984
{'F': np.float64(1.6563372835097254), 'df': (2, 8), 'p': np.float64(0.25009140842101657)}
   A   B  mean_B_minus_A       q  p_tukey
0  N   F          0.0965  1.7527   0.4649
1  N  N'          0.1381  2.5088   0.2382
2  F  N'          0.0416  0.7561   0.8569
20 shuffled 4-fold 1.543086051940918
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python -c "
import h5py,remfile,numpy as np,sys; sys.path.insert(0,'.'); import nfn
u=nfn.asset_urls()
for a in ['AM2','JS34']:
    f=h5py.File(remfile.File(u[a][1]),'r')
    x=f['acquisition/ElectricalSeries/data'][1000000:1000300,:]; y=f['processing/ecephys/LFP/ElectricalSeries/data'][1000000:1000300,:]
    print(a, np.array_equal(x,y), np.abs(x-y).max(), np.array_equal(f['acquisition/ElectricalSeries/timestamps'][:1000],f['processing/ecephys/LFP/ElectricalSeries/timestamps'][:1000]), dict(f['acquisition/ElectricalSeries'].attrs).get('description'), f['acquisition/ElectricalSeries/data'].id.get_offset(), f['processing/ecephys/LFP/ElectricalSeries/data'].id.get_offset())
"
```

```
AM2 True 0.0 True no description 133944 2525787792
JS34 True 0.0 True no description 133944 2780037104
```

**Agent**

The `acquisition/ElectricalSeries` is a byte-identical second copy of the 1.5 kHz LFP (no broadband data), a finding. Adding the parallel CCGP, dichotomy and geometric-null functions to the helper.

**Agent calls Bash**

```bash
cat >> entries/000447-tang-2023/nfn.py <<'EOF'


def run_ccgp(CN, CF, n_perm=1000, seed=0, n_jobs=4, **kw):
    """All 16 decoders of one region with their permutation tests (one generator per decoder)."""
    from joblib import Parallel, delayed
    sets = ccgp_sets(CN, CF, **kw)
    res = Parallel(n_jobs=n_jobs)(delayed(svm_ccgp)(tr, te, n_perm, np.random.default_rng([seed, i]))
                                  for i, (_, _, tr, te) in enumerate(sets))
    return pd.DataFrame([{"variable": k, "decoder": nm, "ccgp": a, "null_95": np.percentile(nl, 95),
                          "null_median": np.median(nl), "p": p, "p_ge": float(np.mean(nl >= a))}
                         for (k, nm, _, _), (a, nl, p) in zip(sets, res)])


def ccgp_values(CN, CF):
    """CCGP of the 16 decoders without permutations (for the geometric null)."""
    from sklearn.svm import SVC
    out = []
    for kind, nm, (Xtr, ytr), (Xte, yte) in ccgp_sets(CN, CF):
        out.append((kind, balanced_accuracy(yte, SVC(kernel="linear", C=1.0).fit(Xtr, ytr).predict(Xte))))
    return pd.DataFrame(out, columns=["variable", "ccgp"])


def permute_noise(C, rng):
    """Geometric random model (Methods): each cluster's noise cloud (its points about the
    centroid) has the axes of its space permuted, separately for each cluster."""
    out = {}
    for k, X in C.items():
        c = X.mean(0)
        out[k] = c + (X - c)[:, rng.permutation(X.shape[1])]
    return out


def dichotomies():
    """The 35 balanced dichotomies of the 8 clusters (each split counted once)."""
    from itertools import combinations
    keys = [(t, s) for t in TRACKS for s in "ab"]
    out = []
    for comb in combinations(range(8), 4):
        if 0 in comb:
            out.append(([keys[i] for i in comb], [keys[i] for i in range(8) if i not in comb]))
    return out


def _cv_acc(X, y, rng):
    from sklearn.model_selection import StratifiedKFold, cross_val_predict
    from sklearn.svm import SVC
    order = rng.permutation(len(y))
    X, y = X[order], y[order]
    pred = cross_val_predict(SVC(kernel="linear", C=1.0), X, y, cv=StratifiedKFold(4))
    return float(np.mean(pred == y))


def decode_dichotomy(C, groups, n_perm, seed):
    """4-fold cross-validated linear C-SVM accuracy (libsvm `-v 4` reports the fraction of
    correct predictions) and the trial-label permutation test (decoding_dichotomy_linearSVM.m)."""
    rng = np.random.default_rng(seed)
    g1, g2 = groups
    X = np.vstack([C[k] for k in g1 + g2])
    y = np.concatenate([[1] * len(C[k]) for k in g1] + [[2] * len(C[k]) for k in g2])
    acc = _cv_acc(X, y, rng)
    null = np.array([_cv_acc(X, rng.permutation(y), rng) for _ in range(n_perm)])
    return acc, float(np.mean(null > acc)), null
EOF
echo ok
```

```
ok
```

**Agent**

Now writing the notebook. I'll generate it from a builder script, run it in the development environment, read the outputs, and then write the conclusions.

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build_nb.py",
 "content": "import json, sys\nimport nbformat as nbf\n\nCONCL = json.load(open('/tmp/claude-1001/conclusions.json')) if len(sys.argv) > 1 else {}\n\ncells = []\ndef md(s, tags=None):\n    c = nbf.v4.new_markdown_cell(s.strip(\"\\n\"))\n    if tags: c.metadata[\"tags\"] = tags\n    cells.append(c)\ndef code(s, tags=None):\n    c = nbf.v4.new_code_cell(s.strip(\"\\n\"))\n    if tags: c.metadata[\"tags\"] = tags\n    cells.append(c)\ndef concl(cid):\n    md(CONCL.get(cid, \"**Result: pending.**\"), tags=[\"conclusion\"])\n\nmd(open('/tmp/claude-1001/header.md').read())\n\ncode(r'''\nimport time\nimport warnings\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\n\nimport nfn\n\nwarnings.filterwarnings(\"ignore\")\npd.set_option(\"display.width\", 220)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 200)\nstarted = time.time()\nA = nfn.load_all()\nfor d in A:\n    nfn.linearize(d)\nBY = {d[\"animal\"]: d for d in A}\nSMOOTHS = (8.0, 4.0, 2.0)\nMAPS = {(d[\"animal\"], s, ep): nfn.rate_maps(d, ep, np.arange(d[\"n_units\"]), smooth_cm=s)\n        for d in A for s in SMOOTHS for ep in range(3)}\nprint(f\"loaded {len(A)} files from dandiset {nfn.DANDISET_ID} version {nfn.DANDISET_VERSION}, \"\n      f\"linearized and mapped in {time.time() - started:.0f} s\")\n''')\n\nmd(\"## Data check\\n\\nEach check of the metadata against the values is stated under its output.\")\n\ncode(r'''\nurls = nfn.asset_urls()\nrows = []\nfor d in A:\n    n, rate = nfn.epoch_counts(d)\n    tr = d[\"trials\"]\n    rows.append({\"animal\": d[\"animal\"], \"file\": urls[d[\"animal\"]][0].split(\"/\")[-1], \"units\": d[\"n_units\"],\n                 \"electrode rows\": len(d[\"electrode_labels\"]),\n                 \"tetrode labels\": len(set(d[\"electrode_labels\"])),\n                 \"max units/electrodes value\": int(d[\"unit_electrode_value\"].max()),\n                 \"CA1 units (tetrode reading)\": int((d[\"unit_region\"] == \"CA1\").sum()),\n                 \"PFC units (tetrode reading)\": int((d[\"unit_region\"] == \"PFC\").sum()),\n                 \"CA1 units (row reading)\": int((d[\"unit_region_rowreading\"] == \"CA1\").sum()),\n                 \"PFC units (row reading)\": int((d[\"unit_region_rowreading\"] == \"PFC\").sum()),\n                 \"epoch durations (s)\": np.round(d[\"epochs\"][:, 1] - d[\"epochs\"][:, 0]).astype(int).tolist(),\n                 \"trials per epoch\": tr.groupby(\"epoch\").size().tolist(),\n                 \"units with no spike in N\": int((n[:, 0] == 0).sum())})\nprint(pd.DataFrame(rows).set_index(\"animal\").T.to_string())\nspk = np.concatenate([np.concatenate(d[\"spikes\"]) for d in A])\ninside = np.concatenate([np.concatenate([((s[:, None] >= d[\"epochs\"][:, 0]) & (s[:, None] <= d[\"epochs\"][:, 1])).any(1)\n                                         for s in d[\"spikes\"]]) for d in A])\nprint(f\"\\nspikes inside the three epochs: {inside.mean():.4f} of {len(spk)}\")\nprint(\"position unit:\", A[0][\"pos_unit\"], \"| comments:\", A[0][\"pos_comments\"])\nfor d in A:\n    sp = d[\"speed\"]\n    dt = np.diff(d[\"t\"])\n    v_from_xy = np.hypot(np.diff(d[\"x\"]), np.diff(d[\"y\"])) / dt\n    ok = np.isfinite(v_from_xy) & (dt < 0.05)\n    print(f\"{d['animal']}: x {np.nanmin(d['x']):.0f} to {np.nanmax(d['x']):.0f}, y {np.nanmin(d['y']):.0f} to {np.nanmax(d['y']):.0f} cm; \"\n          f\"frame interval median {np.median(dt) * 1000:.1f} ms; speed column median {np.nanmedian(sp):.1f}, 99th pct {np.nanpercentile(sp, 99):.1f}; \"\n          f\"median speed from x, y {np.nanmedian(v_from_xy[ok]):.1f} cm/s, correlation with the speed column {np.corrcoef(sp[1:][ok], v_from_xy[ok])[0, 1]:.2f}\")\nprint(\"\\ntrajectory types per epoch (track 0 = start and end wells not one of the four types):\")\nfor d in A:\n    print(d[\"animal\"], d[\"trials\"].groupby([\"epoch\", \"track\"]).size().unstack(fill_value=0).rename(columns={0: \"other\", **nfn.TRACKS}).to_dict(\"index\"))\n''', tags=[\"sanity\"])\n\nmd(r'''\nThe units table has only spike times and an `electrodes` column. By the NWB format that column\nholds row indices of the electrodes table, but its values run up to 64 in ZT2, whose table has 128\nrows (two per tetrode), and up to 32 in the others (62 to 64 rows): the values are tetrode numbers.\nRead as tetrode numbers through the `label` column, the regions give CA1 and PFC counts close to the\npaper's (next cells, and claims cells-per-session and manifold-cell-counts); read as row indices, the\ncounts differ by up to 32 units per animal (ZT2). The tetrode reading is used throughout; the\nformat error is recorded as a finding. There are no waveforms, cell numbers within a tetrode, or\nputative interneuron labels.\n\nEach file has three epochs, read as N, F and N' in that order, as the dandiset's description\nsays. All spikes lie inside the three epochs. Positions are in cm (the W-maze is about 80 by 80 cm\nin the Methods); the third position column is the speed in cm/s, as the comment says. Some units are\nlisted after the tetrode-ordered block and have no spike in N; they were clustered only in later\nepochs.\n''')\n\ncode(r'''\n# The paper's code excludes putative interneurons by hard-coded (tetrode, cell) lists. The files\n# carry no cell numbers; numbering the units of a tetrode in their order in the file shows what the\n# lists would pick.\nEXCLUDE = {\"AM2\": [(6, 9)], \"JS21\": [(6, 3), (6, 6), (6, 7), (6, 8), (7, 1), (21, 1), (22, 1), (25, 1)],\n           \"JS17\": [(6, 1), (7, 1)], \"ZT2\": [(31, 1), (31, 5), (32, 2), (27, 1), (14, 10)], \"JS34\": []}\nfor d in A:\n    n, rate = nfn.epoch_counts(d)\n    ue = d[\"unit_electrode_value\"]\n    order = np.array([(ue[:i] == v).sum() + 1 for i, v in enumerate(ue)])\n    for tet, cell in EXCLUDE[d[\"animal\"]]:\n        hit = np.where((ue == tet) & (order == cell))[0]\n        desc = \", \".join(f\"{d['unit_region'][i]} unit, rate N/F/N' {np.round(rate[i], 1).tolist()} Hz\" for i in hit) or \"no such unit\"\n        print(f\"{d['animal']} listed ({tet},{cell}): {desc}\")\n    hi = np.where((rate >= nfn.CA1_MAX_RATE).any(1) & (d[\"unit_region\"] == \"CA1\"))[0]\n    print(f\"   {d['animal']} CA1 units at 7 Hz or more in some epoch: \"\n          + \"; \".join(f\"tetrode {ue[i]} #{order[i]} {np.round(rate[i], 1).tolist()}\" for i in hi))\n''', tags=[\"sanity\"])\n\nmd(r'''\nWhere the code's lists name a unit that exists, it is mostly a CA1 unit firing at 14 to 45 Hz\n(JS17 (6,1); JS21 (6,3), (6,6), (7,1), (25,1); ZT2 (32,2) and (27,1), the latter 14.7 Hz in F only),\nwhich supports the tetrode reading. Other entries name tetrodes without units (JS21 21 and 22, ZT2\n31) or low-rate units, so the numbering by order is not exact. The code's own rule, CA1 mean rate\nbelow 7 Hz in the epoch, removes every listed CA1 unit in the epochs where it fires at 7 Hz or more;\nZT2 (27,1) stays in N and N', where it fires at 0 and 1.4 Hz. The lists are not applied. PFC units are\nkept whatever their rate, as the code keeps every unit tagged PFC.\n''')\n\ncode(r'''\n# The acquisition ElectricalSeries and the processed LFP: are they the same recording?\nfor d in A:\n    import h5py, remfile\n    f = h5py.File(remfile.File(urls[d[\"animal\"]][1]), \"r\")\n    a = f[\"acquisition/ElectricalSeries/data\"]\n    b = f[\"processing/ecephys/LFP/ElectricalSeries/data\"]\n    ta = f[\"acquisition/ElectricalSeries/timestamps\"]\n    same = all(np.array_equal(a[i:i + 200, :], b[i:i + 200, :]) for i in (0, a.shape[0] // 2, a.shape[0] - 200))\n    rate = 1 / np.median(np.diff(ta[:20000]))\n    print(f\"{d['animal']}: shapes {a.shape} and {b.shape}, sampling {rate:.0f} Hz, identical in 3 slices: {same}, \"\n          f\"stored at different offsets: {a.id.get_offset() != b.id.get_offset()}\")\n''', tags=[\"sanity\"])\n\nmd(r'''\nThe `acquisition/ElectricalSeries` is a second, byte-identical copy of the 1.5 kHz LFP (in every\nfile, at all three slices tested), not the 30 kHz spike-band recording. The LFP is not used here:\nthe analysis needs spikes and position only, apart from the exclusion of sharp-wave ripples, which is\nnot done (see the summary).\n''')\n\ncode(r'''\n# Linearization: idealized W paths from the well positions (nfn.build_skeleton, an assumption,\n# as the paths are not in the dandiset). Paper: \"2-m-long linearized trajectories\" (Figure 2B).\nrows = []\nfor d in A:\n    for ep in range(3):\n        m = (d[\"epoch_of_sample\"] == ep) & (d[\"speed\"] > nfn.MIN_SPEED) & np.isfinite(d[\"lin_offset\"])\n        rows.append({\"animal\": d[\"animal\"], \"epoch\": nfn.EPOCHS[ep],\n                     \"OUT_L/IN_L length (cm)\": round(d[\"track_length\"][(ep, 1)]),\n                     \"OUT_R/IN_R length (cm)\": round(d[\"track_length\"][(ep, 3)]),\n                     \"run samples on a trajectory\": int(m.sum()),\n                     \"distance to path, median (cm)\": round(np.median(d[\"lin_offset\"][m]), 1),\n                     \"90th pct\": round(np.percentile(d[\"lin_offset\"][m], 90), 1),\n                     \"99th pct\": round(np.percentile(d[\"lin_offset\"][m], 99), 1)})\nprint(pd.DataFrame(rows).to_string(index=False))\nfig, axes = plt.subplots(3, 5, figsize=(16, 9))\nfor i, d in enumerate(A):\n    for ep in range(3):\n        ax = axes[ep, i]\n        m = (d[\"epoch_of_sample\"] == ep) & (d[\"speed\"] > nfn.MIN_SPEED)\n        ax.plot(d[\"x\"][m], d[\"y\"][m], \",\", alpha=0.3)\n        for t in (1, 3):\n            p = d[\"templates\"][(ep, t)]\n            ax.plot(p[:, 0], p[:, 1], \"r-\")\n        ax.set_aspect(\"equal\"); ax.set_title(f\"{d['animal']} {nfn.EPOCHS[ep]}\", fontsize=9)\nplt.tight_layout(); plt.show()\nprint(\"All run positions are plotted (none outside the axes).\")\n''', tags=[\"sanity\"])\n\nmd(r'''\nThe idealized paths follow the arms the rats ran (figure). Every trajectory is 180 to 220 cm long,\nconsistent with the paper's 2-m trajectories, and the median distance from a run position to its\npath is about 5 cm (the tracks are about 7 cm wide in the Methods).\n''')\n\ncode(r'''\n# Clock check: decode N' positions from N' spikes with N' templates (in-sample) after shifting all\n# spike times. If spikes and position share a clock the error is smallest at no shift.\nrows = []\nfor d in A:\n    for reg in (\"CA1\", \"PFC\"):\n        cells = nfn.included(d, reg, 2)\n        m = MAPS[(d[\"animal\"], 8.0, 2)]\n        cells = cells[nfn.peak_rate({t: (m[t][0], m[t][1][cells]) for t in m}) >= nfn.PEAK_HZ]\n        tm = {t: (m[t][0], m[t][1][cells]) for t in m}\n        row = {\"animal\": d[\"animal\"], \"region\": reg, \"cells\": len(cells)}\n        for sh in (-2.0, -0.5, 0.0, 0.5, 2.0):\n            d2 = dict(d); d2[\"spikes\"] = [s + sh for s in d[\"spikes\"]]\n            df, _ = nfn.decode_session(d2, 2, cells, tm, n_shuffles=1, restrict_track=True)\n            row[f\"shift {sh:+.1f} s\"] = round(df.error.median(), 1)\n        rows.append(row)\nclock = pd.DataFrame(rows)\nprint(\"Median in-sample decoding error (cm, decode restricted to the current trajectory):\")\nprint(clock.to_string(index=False))\nprint(\"Rows whose smallest error is at zero shift:\",\n      int((clock.filter(like=\"shift\").idxmin(axis=1) == \"shift +0.0 s\").sum()), \"of\", len(clock))\n''', tags=[\"sanity\"])\n\nmd(r'''\nIn every animal and region the in-sample decoding error is smallest with no shift and grows when the\nspikes are shifted by 0.5 or 2 s, so spikes and position share the clock in N'. Spikes and the trial\ntable are checked the same way by the trial-by-trial decoding of Figure 2F below, which uses the\ntrial boundaries.\n''')\n\n# ---------------- behaviour\nmd(r'''\n## Behaviour\n\n### fig1c-familiar-above-novel\n\n> In both groups of rats, performance in the familiar environment is higher than in the novel one\n> whatever the order of exposure (N-F-N' group in Figure 1C, F-N-F'-N' group in Figure S1C).\n\nThe de novo sessions and the F-N-F'-N' rats are not in the dandiset. The test is run on N, F and N'\nalone: a repeated-measures ANOVA over three sessions in place of the five of Figure 1C, with\nTukey's test on its error term. The novel curve is estimated on N and N' run together and the familiar\ncurve on F alone (cal_behavperform.m runs the novel sessions together; its familiar run would include\nthe de novo days, which are missing). The state-space model's background probability is 1/3\n(cal_behavperform.m).\n''')\ncode(r'''\nperf, perf_sep = [], []\nfor d in A:\n    tr = d[\"trials\"]\n    nov = tr[tr.epoch.isin([0, 2])]\n    p_nov = nfn.state_space_correct(nov.correct.values, background=1 / 3)\n    p_f = nfn.state_space_correct(tr[tr.epoch == 1].correct.values, background=1 / 3)\n    perf.append([p_nov[nov.epoch.values == 0].mean(), p_f.mean(), p_nov[nov.epoch.values == 2].mean()])\n    perf_sep.append([nfn.state_space_correct(tr[tr.epoch == e].correct.values, 1 / 3).mean() for e in range(3)])\nraw = pd.DataFrame([[d[\"trials\"][d[\"trials\"].epoch == e].correct.mean() for e in range(3)] for d in A],\n                   index=nfn.ANIMALS, columns=[\"N\", \"F\", \"N'\"])\nP = pd.DataFrame(perf, index=nfn.ANIMALS, columns=[\"N\", \"F\", \"N'\"])\nprint(\"Fraction of correct trials:\"); print(raw.round(3))\nprint(\"\\nMean state-space estimate per session (novel sessions estimated together):\"); print(P.round(3))\na, t = nfn.rm_anova_tukey(P.values, list(P.columns))\nprint(f\"\\nrepeated-measures ANOVA F({a['df'][0]},{a['df'][1]}) = {a['F']:.2f}, p = {a['p']:.3g}\"); print(t.round(4).to_string(index=False))\nP2 = pd.DataFrame(perf_sep, index=nfn.ANIMALS, columns=[\"N\", \"F\", \"N'\"])\na2, t2 = nfn.rm_anova_tukey(P2.values, list(P2.columns))\nprint(f\"\\nVariant, each session estimated alone: F = {a2['F']:.2f}, p = {a2['p']:.3g}\"); print(t2.round(4).to_string(index=False))\nprint(\"\\nPer rat, F minus N:\", (P[\"F\"] - P[\"N\"]).round(3).to_dict())\n''', tags=[\"claim:fig1c-familiar-above-novel\"])\nconcl(\"fig1c-familiar-above-novel\")\n\n# ---------------- cells per session\nmd(r'''\n## Cells\n\n### cells-per-session\n\n> Cells were tracked across environments, with 30.5 (SD 9.8) CA1 and 37.4 (SD 19.3) PFC cells per\n> session per animal.\n\nCells are units with more than 100 spikes in the session, CA1 units with a mean rate below 7 Hz in\nit (claims file; the Methods say \"at least 100\", which is shown as a variant).\n''')\ncode(r'''\nrows = []\nfor d in A:\n    for ep in range(3):\n        for reg in (\"CA1\", \"PFC\"):\n            rows.append({\"animal\": d[\"animal\"], \"session\": nfn.EPOCHS[ep], \"region\": reg,\n                         \"n\": len(nfn.included(d, reg, ep)), \"n_ge100\": len(nfn.included(d, reg, ep, strict=False))})\nC = pd.DataFrame(rows)\ntab = C.pivot_table(index=[\"animal\", \"session\"], columns=\"region\", values=\"n\")\nprint(tab)\nprint(\"\\nmean and SD over the 15 animal-sessions:\")\nprint(pd.DataFrame({\"mean\": tab.mean(), \"SD\": tab.std(ddof=1)}).round(2))\ntab2 = C.pivot_table(index=[\"animal\", \"session\"], columns=\"region\", values=\"n_ge100\")\nprint(\"\\nVariant, at least 100 spikes (Methods):\", tab2.mean().round(2).to_dict(), \"SD\", tab2.std(ddof=1).round(2).to_dict())\nonce = {reg: [len(np.unique(np.concatenate([nfn.included(d, reg, ep) for ep in range(3)]))) for d in A] for reg in (\"CA1\", \"PFC\")}\nprint(\"Variant, each cell counted once per animal:\", {r: (round(np.mean(v), 2), round(np.std(v, ddof=1), 2), v) for r, v in once.items()})\n''', tags=[\"claim:cells-per-session\"])\nconcl(\"cells-per-session\")\n\n# ---------------- PV similarity\nmd(r'''\n## Remapping (Figure 2, S3, S4)\n\n### fig2d-pv-similarity\n\n> PFC population-vector similarity across environments (F-N') is as high as across repeated\n> exposures to the novel environment (N-N'), while CA1 PV similarity is lower across environments\n> than within the novel environment, where the CA1 map is reinstated.\n\nAs cal_PVsimilarity.m: cells passing the inclusion rules in either session of the pair and\nspatially tuned (peak of the linearized map at least 3 Hz in either session); each track's map on\n101 bins of normalized length, interior NaN runs filled, the four tracks concatenated, NaN set to 0;\nPearson r per bin over cells; per animal the mean over bins. Smoothing 8 cm (reading a), 4 and 2 cm\n(variants).\n''')\ncode(r'''\ndef pv_cells(d, reg, e1, e2, s=8.0, rule=\">=\"):\n    cells = np.union1d(nfn.included(d, reg, e1), nfn.included(d, reg, e2))\n    m1, m2 = MAPS[(d[\"animal\"], s, e1)], MAPS[(d[\"animal\"], s, e2)]\n    R1 = nfn.normalized({t: (m1[t][0], m1[t][1][cells]) for t in m1})\n    R2 = nfn.normalized({t: (m2[t][0], m2[t][1][cells]) for t in m2})\n    p1, p2 = np.nanmax(R1, 1), np.nanmax(R2, 1)\n    tuned = ((p1 >= 3) | (p2 >= 3)) if rule == \">=\" else ((p1 > 3) | (p2 > 3))\n    return cells[tuned], R1[tuned], R2[tuned]\n\ndef pv_bins(d, reg, e1, e2, s=8.0, rule=\">=\", cells_mask=None):\n    cells, R1, R2 = pv_cells(d, reg, e1, e2, s, rule)\n    R1, R2 = np.nan_to_num(R1), np.nan_to_num(R2)\n    return np.array([np.corrcoef(R1[:, i], R2[:, i])[0, 1] if R1[:, i].std() > 0 and R2[:, i].std() > 0 else np.nan\n                     for i in range(R1.shape[1])])\n\nGROUPS = [\"CA1 N-N'\", \"CA1 F-N'\", \"PFC N-N'\", \"PFC F-N'\"]\nPAIRS = {\"N-N'\": (0, 2), \"F-N'\": (1, 2), \"F-N\": (1, 0)}\nfor s, rule in [(8.0, \">=\"), (4.0, \">=\"), (2.0, \">=\"), (8.0, \">\")]:\n    M = pd.DataFrame([[np.nanmean(pv_bins(d, g.split()[0], *PAIRS[g.split()[1]], s=s, rule=rule)) for g in GROUPS] for d in A],\n                     index=nfn.ANIMALS, columns=GROUPS)\n    ncell = pd.DataFrame([[len(pv_cells(d, g.split()[0], *PAIRS[g.split()[1]], s, rule)[0]) for g in GROUPS] for d in A],\n                         index=nfn.ANIMALS, columns=GROUPS)\n    a, t = nfn.rm_anova_tukey(M.values, GROUPS)\n    print(f\"--- smoothing {s:g} cm, peak rule {rule} 3 Hz ---\")\n    print(\"mean PV similarity per animal:\"); print(M.round(3))\n    print(\"tuned cells per animal and pair:\", ncell.to_dict(\"list\"))\n    print(f\"repeated-measures ANOVA F({a['df'][0]},{a['df'][1]}) = {a['F']:.2f}, p = {a['p']:.2g}\")\n    print(t[((t.A == \"CA1 N-N'\") & (t.B == \"CA1 F-N'\")) | ((t.A == \"PFC N-N'\") & (t.B == \"PFC F-N'\"))].round(4).to_string(index=False))\n''', tags=[\"claim:fig2d-pv-similarity\"])\nconcl(\"fig2d-pv-similarity\")\n\nmd(r'''\n### figs3a-ca1-global-remapping and figs3a-pfc-similar-ca1-lower\n\n> CA1 spatial similarity between the two environments is no different from that of cell-ID\n> shuffles, that is, CA1 remaps globally.\n\n> Single-cell rate overlap and spatial correlation of PFC cells across environments (F-N') are as\n> large as across repeated exposures to the novel environment (N-N'), whereas in CA1 they are lower\n> across environments.\n\nCells of the PV analysis (fig2d). Spatial similarity is the Pearson r of a cell's two concatenated\nnormalized maps over bins valid in both. Rate overlap is the lower over the higher mean rate, with\nthe mean rate read as (a) the mean of the linearized map or (b) spikes over run time (speed above 5\ncm/s on a trajectory). The shuffle pairs each cell's F map with another cell's N' map of the same\nanimal (a random derangement within the animal; the Methods say \"a different cell\"). One-way ANOVA\nwith Tukey's test over N-N', F-N' and shuffle, per region and measure. The shuffle is one draw; the\nresult over 200 draws is shown too.\n''')\ncode(r'''\ndef remap_measures(d, reg, e1, e2, rng=None, s=8.0):\n    cells, R1, R2 = pv_cells(d, reg, e1, e2, s)\n    dt = nfn._sample_dt(d)\n    run = []\n    for ep in (e1, e2):\n        m = nfn._run_mask(d, ep); T = dt[m].sum(); tt = d[\"t\"]\n        run.append(np.array([m[np.clip(np.searchsorted(tt, d[\"spikes\"][u]), 0, len(tt) - 1)].sum() / T for u in cells]))\n    if rng is not None:\n        k = len(cells); perm = np.arange(k)\n        while k > 1 and np.any(perm == np.arange(k)):\n            perm = rng.permutation(k)\n        R2, run[1] = R2[perm], run[1][perm]\n    ma, mb = np.nanmean(R1, 1), np.nanmean(R2, 1)\n    sc = []\n    for i in range(len(cells)):\n        ok = np.isfinite(R1[i]) & np.isfinite(R2[i])\n        sc.append(stats.pearsonr(R1[i][ok], R2[i][ok])[0] if ok.sum() > 2 and R1[i][ok].std() > 0 and R2[i][ok].std() > 0 else np.nan)\n    return pd.DataFrame({\"overlap_map\": np.minimum(ma, mb) / np.maximum(ma, mb),\n                         \"overlap_run\": np.minimum(*run) / np.maximum(*run), \"spatial_r\": sc})\n\nrng_s3a = np.random.default_rng(301)\nREMAP = {}\nfor reg in (\"CA1\", \"PFC\"):\n    REMAP[reg] = {\"N-N'\": pd.concat([remap_measures(d, reg, 0, 2) for d in A]),\n                  \"F-N'\": pd.concat([remap_measures(d, reg, 1, 2) for d in A]),\n                  \"shuffle\": pd.concat([remap_measures(d, reg, 1, 2, rng_s3a) for d in A])}\nS3A = {}\nfor reg in (\"CA1\", \"PFC\"):\n    for meas in (\"spatial_r\", \"overlap_map\", \"overlap_run\"):\n        a, t = nfn.anova_tukey([REMAP[reg][g][meas] for g in REMAP[reg]], list(REMAP[reg]))\n        S3A[(reg, meas)] = t\n        med = {g: round(float(REMAP[reg][g][meas].median()), 3) for g in REMAP[reg]}\n        n = {g: int(REMAP[reg][g][meas].notna().sum()) for g in REMAP[reg]}\n        print(f\"{reg} {meas}: medians {med}, n {n}, ANOVA F = {a['F']:.2f}, p = {a['p']:.2g}\")\n        print(t[[\"group1\", \"group2\", \"meandiff\", \"p-adj\", \"lower\", \"upper\"]].to_string(index=False))\n''')\ncode(r'''\n# figs3a-ca1-global-remapping: CA1 F-N' against shuffle, spatial similarity (the criterion's measure)\nt = S3A[(\"CA1\", \"spatial_r\")]\nrow = t[(t.group1 == \"F-N'\") & (t.group2 == \"shuffle\")].iloc[0]\nprint(f\"CA1 spatial similarity, F-N' against shuffle: mean difference {-row['meandiff']:.3f} (F-N' minus shuffle), Tukey p = {row['p-adj']:.4f}\")\nfor meas in (\"overlap_map\", \"overlap_run\"):\n    r2 = S3A[(\"CA1\", meas)]; r2 = r2[(r2.group1 == \"F-N'\") & (r2.group2 == \"shuffle\")].iloc[0]\n    print(f\"   {meas}: difference {-r2['meandiff']:.3f}, p = {r2['p-adj']:.3f}\")\nps, diffs = [], []\nrng_draws = np.random.default_rng(302)\nfor k in range(200):\n    sh = pd.concat([remap_measures(d, \"CA1\", 1, 2, rng_draws) for d in A])\n    a, t = nfn.anova_tukey([REMAP[\"CA1\"][\"N-N'\"].spatial_r, REMAP[\"CA1\"][\"F-N'\"].spatial_r, sh.spatial_r], [\"N-N'\", \"F-N'\", \"shuffle\"])\n    r = t[(t.group1 == \"F-N'\") & (t.group2 == \"shuffle\")].iloc[0]\n    ps.append(r[\"p-adj\"]); diffs.append(-r[\"meandiff\"])\nps, diffs = np.array(ps), np.array(diffs)\nprint(f\"over 200 shuffle draws: Tukey p < 0.05 in {np.mean(ps < 0.05):.2f} of draws; median p {np.median(ps):.3f}; \"\n      f\"F-N' minus shuffle mean difference median {np.median(diffs):.3f} (range {diffs.min():.3f} to {diffs.max():.3f})\")\nprint(\"per animal median spatial r, CA1 F-N':\",\n      {d[\"animal\"]: round(float(remap_measures(d, \"CA1\", 1, 2).spatial_r.median()), 3) for d in A})\n''', tags=[\"claim:figs3a-ca1-global-remapping\"])\nconcl(\"figs3a-ca1-global-remapping\")\ncode(r'''\nfor reg in (\"PFC\", \"CA1\"):\n    for meas in (\"overlap_map\", \"overlap_run\", \"spatial_r\"):\n        t = S3A[(reg, meas)]\n        r = t[(t.group1 == \"F-N'\") & (t.group2 == \"N-N'\")].iloc[0]\n        print(f\"{reg} {meas}: N-N' minus F-N' = {r['meandiff']:.3f}, Tukey p = {r['p-adj']:.4f}\")\nfor s in (4.0, 2.0):\n    out = []\n    for reg in (\"PFC\", \"CA1\"):\n        g = {\"N-N'\": pd.concat([remap_measures(d, reg, 0, 2, s=s) for d in A]), \"F-N'\": pd.concat([remap_measures(d, reg, 1, 2, s=s) for d in A]),\n             \"shuffle\": pd.concat([remap_measures(d, reg, 1, 2, np.random.default_rng(303), s=s) for d in A])}\n        for meas in (\"overlap_map\", \"overlap_run\", \"spatial_r\"):\n            a, t = nfn.anova_tukey([g[k][meas] for k in g], list(g))\n            r = t[(t.group1 == \"F-N'\") & (t.group2 == \"N-N'\")].iloc[0]\n            out.append(f\"{reg} {meas} diff {r['meandiff']:.3f} p {r['p-adj']:.3g}\")\n    print(f\"smoothing {s:g} cm:\", \"; \".join(out))\n''', tags=[\"claim:figs3a-pfc-similar-ca1-lower\"])\nconcl(\"figs3a-pfc-similar-ca1-lower\")\n\nmd(r'''\n### figs3c-pfc-assimilation\n\n> PFC PV similarity across environments grows with experience (F-N' higher than F-N), while CA1 does\n> not change (F-N against F-N' not different) and stays below N-N'.\n\nPer-bin PV similarity (fig2d), bins pooled over the five rats, one-way ANOVA per region with\nTukey's test.\n''')\ncode(r'''\nfor s in SMOOTHS:\n    for reg in (\"CA1\", \"PFC\"):\n        G = {nm: np.concatenate([pv_bins(d, reg, *PAIRS[nm], s=s) for d in A]) for nm in (\"F-N\", \"F-N'\", \"N-N'\")}\n        a, t = nfn.anova_tukey(list(G.values()), list(G))\n        print(f\"smoothing {s:g} cm, {reg}: means {({k: round(float(np.nanmean(v)), 3) for k, v in G.items()})}, \"\n              f\"bins {a['n']}, ANOVA F = {a['F']:.1f}, p = {a['p']:.2g}\")\n        print(\"   \" + t[[\"group1\", \"group2\", \"meandiff\", \"p-adj\"]].round(4).to_string(index=False).replace(\"\\n\", \"\\n   \"))\n''', tags=[\"claim:figs3c-pfc-assimilation\"])\nconcl(\"figs3c-pfc-assimilation\")\n\nmd(r'''\n### figs3d-pfc-similarity-over-trials\n\n> Over trials in the novel environment, PFC similarity to the familiar map rises from the first to\n> the last trial, while CA1 similarity does not change.\n\nSingle-trial maps (8 cm smoothing, 2-cm bins) of each trajectory pass in the novel environment\nagainst the session-averaged F maps of the same trajectory, over the tuned cells (peak at least 3 Hz\nin F or in the novel sessions); per-bin PV similarity on 101 normalized bins. A trial is kept when at\nleast 80% of these cells fire during its run samples (legend). The paper does not say how trials are\nnumbered or which is \"last\". Here the kept trials of each animal are ranked in order; trial ranks 1\nto K enter the test, K being the smallest number of kept trials over the animals that have any, and\n\"last\" is rank K (an assumption). Readings for the novel trials: (a) N then N', (b) N, (c) N'.\nOne-way ANOVA over ranks on per-bin values, Tukey's test of first against last.\n''')\ncode(r'''\nrows = []\nfor d in A:\n    tr = d[\"trials\"]\n    mF = MAPS[(d[\"animal\"], 8.0, 1)]\n    for reg in (\"CA1\", \"PFC\"):\n        for name, eps in ((\"N then N'\", [0, 2]), (\"N\", [0]), (\"N'\", [2])):\n            cells = np.union1d(nfn.included(d, reg, 1), np.concatenate([nfn.included(d, reg, e) for e in eps]))\n            pkF = nfn.peak_rate({t: (mF[t][0], mF[t][1][cells]) for t in mF})\n            pkN = np.max([nfn.peak_rate({t: (MAPS[(d[\"animal\"], 8.0, e)][t][0], MAPS[(d[\"animal\"], 8.0, e)][t][1][cells]) for t in mF}) for e in eps], 0)\n            cells = cells[(pkF >= 3) | (pkN >= 3)]\n            order = 0\n            for e in eps:\n                for i in tr[(tr.epoch == e) & (tr.track > 0)].index:\n                    order += 1\n                    track = int(tr.loc[i, \"track\"])\n                    run = nfn._run_mask(d, e, track, i)\n                    tt = d[\"t\"][run]\n                    if len(tt) == 0:\n                        continue\n                    active = np.mean([np.any((d[\"spikes\"][u] >= tt[0]) & (d[\"spikes\"][u] <= tt[-1])) for u in cells])\n                    c, r = nfn.rate_maps(d, e, cells, trial=i, track_only=track)[track]\n                    pos = np.linspace(0, 1, 101)\n                    X = np.nan_to_num(r[:, np.abs((c / c.max())[None, :] - pos[:, None]).argmin(1)])\n                    cF, rF = mF[track]\n                    Y = np.nan_to_num(rF[cells][:, np.abs((cF / cF.max())[None, :] - pos[:, None]).argmin(1)])\n                    pv = np.array([np.corrcoef(X[:, b], Y[:, b])[0, 1] if X[:, b].std() > 0 and Y[:, b].std() > 0 else np.nan for b in range(101)])\n                    rows.append({\"animal\": d[\"animal\"], \"region\": reg, \"reading\": name, \"order\": order, \"active\": active, \"pv\": pv})\nTRI = pd.DataFrame(rows)\nprint(\"passes and passes kept (at least 80% of tuned cells active):\")\nprint(TRI.groupby([\"region\", \"reading\", \"animal\"]).agg(passes=(\"order\", \"size\"), kept=(\"active\", lambda x: int((x >= 0.8).sum()))).unstack(\"animal\"))\nfor (reg, name), x in TRI[TRI.active >= 0.8].groupby([\"region\", \"reading\"]):\n    x = x.copy(); x[\"rank\"] = x.groupby(\"animal\").order.rank().astype(int)\n    K = int(x.groupby(\"animal\")[\"rank\"].max().min()); x = x[x[\"rank\"] <= K]\n    groups = [np.concatenate(x[x[\"rank\"] == k].pv.values) for k in range(1, K + 1)]\n    a, t = nfn.anova_tukey(groups, [f\"{k:02d}\" for k in range(1, K + 1)])\n    r = t[(t.group1 == \"01\") & (t.group2 == f\"{K:02d}\")]\n    means = [np.nanmean(g) for g in groups]\n    print(f\"{reg}, {name}: {x.animal.nunique()} animals, K = {K}; mean PV similarity trial 1 {means[0]:.3f}, trial K {means[-1]:.3f}; \"\n          f\"ANOVA p = {a['p']:.2g}; Tukey first against last: difference {r.meandiff.iloc[0]:.3f}, p = {r['p-adj'].iloc[0]:.4f}\"\n          f\"; Pearson r of trial mean with rank {stats.pearsonr(np.arange(K), means)[0]:.2f}\")\n''', tags=[\"claim:figs3d-pfc-similarity-over-trials\"])\nconcl(\"figs3d-pfc-similarity-over-trials\")\n\nmd(r'''\n### figs4d-reward-location-similarity\n\n> PV similarity between the environments at the reward wells is the same as at other locations, in\n> both regions.\n\nPer-bin PV similarity (fig2d, 8 cm) between F and the novel session, mean over the five rats, per\nregion; Grubbs' test (two-sided, alpha 0.05) over (a) all 404 bins of a region and (b) the 101 bins of\neach trajectory. Novel session N' (the panels' pair) or N.\n''')\ncode(r'''\nfor nm in (\"F-N'\", \"F-N\"):\n    for reg in (\"CA1\", \"PFC\"):\n        M = np.array([pv_bins(d, reg, *PAIRS[nm]) for d in A]); m = np.nanmean(M, 0)\n        G, p, i = nfn.grubbs(m)\n        per = [nfn.grubbs(m[k * 101:(k + 1) * 101]) for k in range(4)]\n        ends = {nfn.TRACKS[k + 1]: (round(m[k * 101], 2), round(m[k * 101 + 100], 2)) for k in range(4)}\n        print(f\"{nm} {reg}: all bins G = {G:.2f}, p = {p:.3g} (most extreme bin {i}); per trajectory p = {[round(x[1], 3) for x in per]}; \"\n              f\"mean {np.nanmean(m):.3f}, range {np.nanmin(m):.3f} to {np.nanmax(m):.3f}; values at the center-well and side-well ends {ends}\")\n''', tags=[\"claim:figs4d-reward-location-similarity\"])\nconcl(\"figs4d-reward-location-similarity\")\n\n# ---------------- decoding\nmd(r'''\n## Decoding (Figure 2E, 2F)\n\n### fig2e-ca1-error-familiar and fig2e-pfc-error-stable\n\n> Decoding with N' rate maps, CA1 position error is higher in F than in N, and in F no better than\n> with cell-ID shuffled templates.\n\n> Decoding with N' rate maps, PFC position error is similar in N and F, and in both well above chance\n> (below the cell-ID shuffles).\n\nDecoder of the Methods (nfn.decode_session): templates are the N' maps (8 cm) of cells included in\nN' with a peak of at least 3 Hz; 200-ms windows every 150 ms (the Methods' \"50 ms overlap\"); bins on\none trajectory, mean speed above 5 cm/s, more than 15 cm from a well, at least one cell firing; error\nalong the four trajectories laid end to end. Shuffles permute the cell identities of the templates:\n(a) one shuffle, (b) the median over 100. Wilcoxon paired test of each bin against its shuffle;\nKruskal-Wallis with Dunn's test over (a) the four groups, (b) N and F per region. Variants: a 50-ms\nstep (the code), 4 and 2 cm smoothing, and the decode restricted to the current trajectory. The\ntheta restriction of the code cannot be run (no theta times in the dandiset).\n''')\ncode(r'''\ndef decode_all(s=8.0, seed=401, **kw):\n    rng = np.random.default_rng(seed); out = []\n    for d in A:\n        for reg in (\"CA1\", \"PFC\"):\n            cells = nfn.included(d, reg, 2); m = MAPS[(d[\"animal\"], s, 2)]\n            cells = cells[nfn.peak_rate({t: (m[t][0], m[t][1][cells]) for t in m}) >= nfn.PEAK_HZ]\n            tm = {t: (m[t][0], m[t][1][cells]) for t in m}\n            for ep in (0, 1):\n                df, _ = nfn.decode_session(d, ep, cells, tm, rng=rng, **kw)\n                df[\"animal\"], df[\"region\"], df[\"env\"], df[\"cells\"] = d[\"animal\"], reg, nfn.EPOCHS[ep], len(cells)\n                out.append(df)\n    return pd.concat(out, ignore_index=True)\n\ndef decode_stats(D):\n    g = {(r, e): D[(D.region == r) & (D.env == e)] for r in (\"CA1\", \"PFC\") for e in (\"N\", \"F\")}\n    a4, dn4 = nfn.kruskal_dunn([g[k].error for k in g], [f\"{r} {e}\" for r, e in g])\n    out = {\"KW4 p\": a4[\"p\"]}\n    for r in (\"CA1\", \"PFC\"):\n        out[f\"{r} N median\"] = g[(r, \"N\")].error.median(); out[f\"{r} F median\"] = g[(r, \"F\")].error.median()\n        out[f\"{r} Dunn4 N-F p\"] = dn4.loc[f\"{r} N\", f\"{r} F\"]\n        out[f\"{r} KW2 N-F p\"] = stats.kruskal(g[(r, \"N\")].error, g[(r, \"F\")].error).pvalue\n        for e in (\"N\", \"F\"):\n            x = g[(r, e)]\n            out[f\"{r} {e} shuffle median\"] = x.error_shuffle_median.median()\n            out[f\"{r} {e} W(a) p\"] = stats.wilcoxon(x.error, x.error_shuffle1).pvalue\n            out[f\"{r} {e} W(b) p\"] = stats.wilcoxon(x.error, x.error_shuffle_median).pvalue\n            out[f\"{r} {e} mean error minus shuffle(b)\"] = (x.error - x.error_shuffle_median).mean()\n    return out\n\nDEC = decode_all()\nprint(DEC.groupby([\"region\", \"env\", \"animal\"]).agg(bins=(\"error\", \"size\"), cells=(\"cells\", \"first\"), median_error=(\"error\", \"median\"),\n                                                   shuffle_median=(\"error_shuffle_median\", \"median\")).round(1))\nVAR = {\"main (Methods, 8 cm)\": decode_stats(DEC),\n       \"step 50 ms (code)\": decode_stats(decode_all(step=0.05)),\n       \"smoothing 4 cm\": decode_stats(decode_all(s=4.0)),\n       \"smoothing 2 cm\": decode_stats(decode_all(s=2.0)),\n       \"decode restricted to the current trajectory\": decode_stats(decode_all(restrict_track=True))}\nVARDF = pd.DataFrame(VAR)\nprint(\"\\nError in cm; p-values of the tests:\")\nwith pd.option_context(\"display.float_format\", lambda v: f\"{v:.3g}\"):\n    print(VARDF)\nprint(\"\\nError range (cm), main:\", DEC.error.min(), \"to\", DEC.error.max())\n''')\ncode(r'''\nv = VARDF[\"main (Methods, 8 cm)\"]\nprint(f\"CA1: F median {v['CA1 F median']:.1f} cm against N {v['CA1 N median']:.1f}; Dunn (4 groups) p = {v['CA1 Dunn4 N-F p']:.2g}, \"\n      f\"(N and F only) p = {v['CA1 KW2 N-F p']:.2g}\")\nprint(f\"CA1 F against its shuffle: median {v['CA1 F median']:.1f} against {v['CA1 F shuffle median']:.1f} cm; \"\n      f\"mean paired difference {v['CA1 F mean error minus shuffle(b)']:.1f} cm; Wilcoxon (a) p = {v['CA1 F W(a) p']:.3g}, (b) p = {v['CA1 F W(b) p']:.3g}\")\nfor name in VARDF.columns[1:]:\n    w = VARDF[name]\n    print(f\"   {name}: CA1 F > N {w['CA1 F median'] > w['CA1 N median']} (p {w['CA1 Dunn4 N-F p']:.2g}); \"\n          f\"CA1 F against shuffle p (a) {w['CA1 F W(a) p']:.3g}, (b) {w['CA1 F W(b) p']:.3g}, mean difference {w['CA1 F mean error minus shuffle(b)']:.1f} cm\")\n''', tags=[\"claim:fig2e-ca1-error-familiar\"])\nconcl(\"fig2e-ca1-error-familiar\")\ncode(r'''\nv = VARDF[\"main (Methods, 8 cm)\"]\nprint(f\"PFC: N median {v['PFC N median']:.1f}, F median {v['PFC F median']:.1f} cm; Dunn (4 groups) p = {v['PFC Dunn4 N-F p']:.2g}, \"\n      f\"(N and F only) p = {v['PFC KW2 N-F p']:.2g}\")\nfor e in (\"N\", \"F\"):\n    print(f\"PFC {e} against shuffle: median {v[f'PFC {e} median']:.1f} against {v[f'PFC {e} shuffle median']:.1f}; mean difference \"\n          f\"{v[f'PFC {e} mean error minus shuffle(b)']:.1f} cm; Wilcoxon (a) p = {v[f'PFC {e} W(a) p']:.2g}, (b) p = {v[f'PFC {e} W(b) p']:.2g}\")\nfor name in VARDF.columns[1:]:\n    w = VARDF[name]\n    print(f\"   {name}: PFC N {w['PFC N median']:.1f}, F {w['PFC F median']:.1f} cm, Dunn p {w['PFC Dunn4 N-F p']:.2g}; \"\n          f\"below shuffle in N and F: {w['PFC N mean error minus shuffle(b)'] < 0 and w['PFC F mean error minus shuffle(b)'] < 0} \"\n          f\"(max p {max(w['PFC N W(a) p'], w['PFC N W(b) p'], w['PFC F W(a) p'], w['PFC F W(b) p']):.2g})\")\nprint(\"\\nPer animal, PFC median error N and F (cm):\")\nprint(DEC[DEC.region == \"PFC\"].groupby([\"animal\", \"env\"]).error.median().unstack().round(1))\n''', tags=[\"claim:fig2e-pfc-error-stable\"])\nconcl(\"fig2e-pfc-error-stable\")\n\nmd(r'''\n### fig2f-switch-dynamics\n\n> After the switch from N to F, CA1 decoding error rises within the first trial, while PFC decoding\n> error stays stable.\n\nBins of the decoder above, grouped by trial (a row of the trials table; bins pooled over rats).\nReadings of trial -1: (a) the last N trial, so that N trials -10 to -1 are the last ten; (b) the\ncode's batch script as it runs, which takes the first ten N trials. Trials 1 to 10 are the first ten\nF trials. Kruskal-Wallis over the 20 trials with Dunn's test (Bonferroni over all pairs). Variant\ndecoder of the code: 200-ms bins without overlap, no speed filter, at least 2 active cells, decode\nrestricted to the current trajectory.\n''')\ncode(r'''\ndef by_trial(D):\n    D = D.copy()\n    D[\"k\"] = -1\n    for d in A:\n        tr = d[\"trials\"]\n        for ep in (0, 1):\n            ids = list(tr[tr.epoch == ep].index); pos = {t: i for i, t in enumerate(ids)}\n            m = (D.animal == d[\"animal\"]) & (D.env == nfn.EPOCHS[ep])\n            D.loc[m, \"k\"] = [pos.get(t, -999) for t in D.loc[m, \"trial\"]]\n            D.loc[m, \"nk\"] = len(ids)\n    return D\n\ndef trial_tests(D, reading):\n    D = D.copy()\n    D[\"lab\"] = np.where(D.env == \"N\", (D.k - D.nk) if reading == \"a\" else (D.k - 10), D.k + 1)\n    D = D[(D.lab >= -10) & (D.lab <= 10) & (D.lab != 0)]\n    out = {}\n    for r in (\"CA1\", \"PFC\"):\n        x = D[D.region == r]; labs = sorted(x.lab.unique())\n        a, dn = nfn.kruskal_dunn([x[x.lab == l].error for l in labs], labs)\n        med = x.groupby(\"lab\").error.median()\n        out[r] = {\"KW p\": a[\"p\"], \"trial -1 median\": med[-1], \"trial 1 median\": med[1], \"n -1\": int((x.lab == -1).sum()),\n                  \"n 1\": int((x.lab == 1).sum()), \"Dunn -1 vs 1 p\": dn.loc[-1, 1]}\n    return pd.DataFrame(out)\n\nTR_M = by_trial(decode_all(seed=402, n_shuffles=1))\nTR_C = by_trial(decode_all(seed=403, n_shuffles=1, step=0.2, min_speed=-1, min_active=2, restrict_track=True))\nfor nm, D in ((\"Methods decoder\", TR_M), (\"code decoder (variant)\", TR_C)):\n    for rd in (\"a\", \"b\"):\n        print(f\"--- {nm}, reading ({rd}) ---\")\n        with pd.option_context(\"display.float_format\", lambda v: f\"{v:.3g}\"):\n            print(trial_tests(D, rd))\nx = TR_M.copy(); x[\"lab\"] = np.where(x.env == \"N\", x.k - x.nk, x.k + 1)\nprint(\"\\nMethods decoder, reading (a): median error by trial (cm)\")\nprint(x[(x.lab >= -10) & (x.lab <= 10)].groupby([\"region\", \"lab\"]).error.median().unstack().round(0))\n''', tags=[\"claim:fig2f-switch-dynamics\"])\nconcl(\"fig2f-switch-dynamics\")\n\n# ---------------- ramping\nmd(r'''\n## Reward ramping (Figure S4)\n\n### figs4-ramping-fraction\n\n> Ramping cells make up 16.4% of CA1 cell samples (81 of 495) and 18.1% of PFC cell samples (115 of\n> 636), a cell sample being one cell on one trajectory type.\n\nA session map (8 cm) of a cell on a trajectory ramps when the regression of rate on the position\ntraversed toward the reward, over the whole trajectory, has Pearson r > 0.5 and p < 0.05, its peak is\nat least 3 Hz and lies within 20 cm of the trajectory's end (Methods). Denominators: (a) cell\nsamples of the three sessions pooled, (b) N' only, each over included cells with a valid map (at\nleast 3 visited bins). Variants: 4 and 2 cm smoothing, and denominators restricted to tuned samples\n(peak at least 3 Hz).\n''')\ncode(r'''\ndef ramp_table(s):\n    rows = []\n    for d in A:\n        for reg in (\"CA1\", \"PFC\"):\n            for ep in range(3):\n                m = MAPS[(d[\"animal\"], s, ep)]\n                for c in nfn.included(d, reg, ep):\n                    for tr in nfn.TRACKS:\n                        ok, rr, p, valid = nfn.ramping(m, c, tr)\n                        pk = np.nanmax(m[tr][1][c]) if np.isfinite(m[tr][1][c]).any() else np.nan\n                        rows.append({\"animal\": d[\"animal\"], \"region\": reg, \"ep\": ep, \"unit\": c, \"track\": tr, \"ramp\": ok,\n                                     \"valid\": valid, \"r\": rr, \"tuned\": pk >= 3})\n    return pd.DataFrame(rows)\nRAMP = {s: ramp_table(s) for s in SMOOTHS}\nfor s in SMOOTHS:\n    R = RAMP[s]\n    for reg in (\"CA1\", \"PFC\"):\n        for nm, eps in ((\"(a) all sessions\", [0, 1, 2]), (\"(b) N'\", [2])):\n            x = R[(R.region == reg) & R.ep.isin(eps) & R.valid]\n            xt = x[x.tuned]\n            print(f\"smoothing {s:g} cm, {reg} {nm}: {x.ramp.sum()} of {len(x)} = {100 * x.ramp.mean():.1f}%; \"\n                  f\"of tuned samples {xt.ramp.sum()} of {len(xt)} = {100 * xt.ramp.mean():.1f}%\")\nR = RAMP[8.0]\nx = R[(R.ep == 2) & R.valid]\nprint(\"\\nN', 8 cm, ramping samples per animal and region:\")\nprint(x.groupby([\"region\", \"animal\"]).agg(samples=(\"ramp\", \"size\"), ramping=(\"ramp\", \"sum\")).unstack(\"region\"))\nprint(\"distribution of r among tuned samples (N', 8 cm):\", np.nanpercentile(x[x.tuned].r, [10, 50, 90]).round(2))\n''', tags=[\"claim:figs4-ramping-fraction\"])\nconcl(\"figs4-ramping-fraction\")\n\nmd(r'''\n### figs4-ramping-generalization\n\n> PFC ramping cells generalize their reward representation across environments, whereas CA1 ramping\n> cells remap, and the generalization of ramping cells is similar to that of other cells in each\n> region.\n\nRamping cell samples identified in N' (8 cm). Per animal and trajectory, the PV over its ramping\nsamples and the PV over the other tuned cells of the PV analysis on that trajectory, per bin (101\nnormalized bins), for N-N' and F-N'; a PV needs at least 3 cells (an assumption: a correlation over\n2 cells is always plus or minus 1). Bins pooled over rats and trajectories; Kruskal-Wallis over the 8\ngroups with Dunn's test. Variant: the ramping samples pooled over animals into one population per\ntrajectory.\n''')\ncode(r'''\nRN = RAMP[8.0]; RN = RN[(RN.ep == 2) & RN.ramp]\npos101 = np.linspace(0, 1, 101)\ndef track_norm(m, track, cells):\n    c, r = m[track]; r = r[cells]\n    out = nfn.normalized({t: (m[t][0], m[t][1][cells]) for t in m})\n    k = list(nfn.TRACKS).index(track)\n    return out[:, k * 101:(k + 1) * 101]\ndef bin_corr(X, Y):\n    X, Y = np.nan_to_num(X), np.nan_to_num(Y)\n    return np.array([np.corrcoef(X[:, b], Y[:, b])[0, 1] if X[:, b].std() > 0 and Y[:, b].std() > 0 else np.nan for b in range(X.shape[1])])\nG8 = {}; counts = []\npooled = {}\nfor reg in (\"CA1\", \"PFC\"):\n    for pair in (\"N-N'\", \"F-N'\"):\n        e1, e2 = PAIRS[pair]\n        for kind in (\"ramping\", \"other\"):\n            G8[(reg, kind, pair)] = []\n        for d in A:\n            cells_pv, _, _ = pv_cells(d, reg, e1, e2)\n            m1, m2 = MAPS[(d[\"animal\"], 8.0, e1)], MAPS[(d[\"animal\"], 8.0, e2)]\n            for track in nfn.TRACKS:\n                ramp = RN[(RN.animal == d[\"animal\"]) & (RN.region == reg) & (RN.track == track)].unit.values\n                other = np.setdiff1d(cells_pv, ramp)\n                counts.append({\"region\": reg, \"pair\": pair, \"animal\": d[\"animal\"], \"track\": track, \"ramping\": len(ramp), \"other\": len(other)})\n                for kind, cs in ((\"ramping\", ramp), (\"other\", other)):\n                    X, Y = track_norm(m1, track, cs), track_norm(m2, track, cs)\n                    pooled.setdefault((reg, kind, pair, track), []).append((X, Y))\n                    if len(cs) >= 3:\n                        G8[(reg, kind, pair)].append(bin_corr(X, Y))\nCNT = pd.DataFrame(counts)\nprint(\"ramping samples (N') per region and trajectory, summed over animals:\",\n      CNT[CNT.pair == \"N-N'\"].groupby([\"region\", \"track\"]).ramping.sum().to_dict())\nprint(\"animal-trajectory populations with at least 3 ramping cells:\",\n      CNT[(CNT.pair == \"N-N'\") & (CNT.ramping >= 3)].groupby(\"region\").size().to_dict())\nnames = [f\"{r} {k} {p}\" for r in (\"CA1\", \"PFC\") for k in (\"ramping\", \"other\") for p in (\"N-N'\", \"F-N'\")]\nvals = [np.concatenate(G8[(r, k, p)]) if G8[(r, k, p)] else np.array([]) for r in (\"CA1\", \"PFC\") for k in (\"ramping\", \"other\") for p in (\"N-N'\", \"F-N'\")]\nprint(\"bins per group:\", dict(zip(names, [int(np.isfinite(v).sum()) for v in vals])))\nprint(\"medians:\", dict(zip(names, [round(float(np.nanmedian(v)), 3) if len(v) else None for v in vals])))\ndef report(vals, names):\n    keep = [i for i, v in enumerate(vals) if np.isfinite(v).sum() > 0]\n    a, dn = nfn.kruskal_dunn([vals[i] for i in keep], [names[i] for i in keep])\n    print(f\"Kruskal-Wallis H = {a['H']:.1f}, p = {a['p']:.2g}\")\n    for r in (\"CA1\", \"PFC\"):\n        pairs = [(f\"{r} ramping N-N'\", f\"{r} ramping F-N'\"), (f\"{r} ramping N-N'\", f\"{r} other N-N'\"), (f\"{r} ramping F-N'\", f\"{r} other F-N'\")]\n        for a_, b_ in pairs:\n            if a_ in dn.index and b_ in dn.index:\n                print(f\"   Dunn {a_} vs {b_}: p = {dn.loc[a_, b_]:.3g}\")\n            else:\n                print(f\"   Dunn {a_} vs {b_}: not testable (no population of 3 ramping cells)\")\nreport(vals, names)\nprint(\"\\nVariant, ramping and other samples pooled over animals per trajectory:\")\nvals2 = []\nfor r in (\"CA1\", \"PFC\"):\n    for k in (\"ramping\", \"other\"):\n        for p in (\"N-N'\", \"F-N'\"):\n            v = []\n            for track in nfn.TRACKS:\n                X = np.vstack([x for x, y in pooled[(r, k, p, track)]]); Y = np.vstack([y for x, y in pooled[(r, k, p, track)]])\n                if len(X) >= 3:\n                    v.append(bin_corr(X, Y))\n            vals2.append(np.concatenate(v) if v else np.array([]))\nprint(\"medians:\", dict(zip(names, [round(float(np.nanmedian(v)), 3) if len(v) else None for v in vals2])))\nreport(vals2, names)\n''', tags=[\"claim:figs4-ramping-generalization\"])\nconcl(\"figs4-ramping-generalization\")\n\n# ---------------- single cell selectivity\nmd(r'''\n## Single-cell geometry (Figures 3D, 3E, S5)\n\nCells found in all three sessions (included in N, F and N'; matchidx_acrossep.m). Selectivity index\nand path-equivalent coefficient per cell and session (nfn.selectivity, nfn.path_equivalence).\n''')\ncode(r'''\ndef sc_table(s):\n    rows = []\n    for d in A:\n        for reg in (\"CA1\", \"PFC\"):\n            cells = np.intersect1d(np.intersect1d(nfn.included(d, reg, 0), nfn.included(d, reg, 1)), nfn.included(d, reg, 2))\n            for ep in range(3):\n                m = MAPS[(d[\"animal\"], s, ep)]\n                for c in cells:\n                    si_in, si_out = nfn.selectivity(m, c)\n                    si_in_g, si_out_g = nfn.selectivity(m, c, \">\")\n                    rows.append({\"animal\": d[\"animal\"], \"region\": reg, \"unit\": c, \"ep\": ep, \"si_in\": si_in, \"si_out\": si_out,\n                                 \"si_in_gt\": si_in_g, \"si_out_gt\": si_out_g, \"R\": nfn.path_equivalence(m, c)})\n    return pd.DataFrame(rows)\nSC = {s: sc_table(s) for s in SMOOTHS}\nprint(\"cells in all three sessions:\", SC[8.0][SC[8.0].ep == 0].groupby(\"region\").size().to_dict())\nprint(\"per animal:\", SC[8.0][SC[8.0].ep == 0].groupby([\"region\", \"animal\"]).size().unstack(0).to_dict())\ndef pear(x, y):\n    ok = np.isfinite(x) & np.isfinite(y)\n    r, p = stats.pearsonr(x[ok], y[ok]); return r, p, int(ok.sum())\n''')\nmd(r'''\n### fig3d-selectivity-index\n\n> Inbound and outbound trajectory selectivity indices are negatively correlated in PFC (r = -0.5),\n> reflecting task-sequence selectivity, and positively correlated in CA1 (r = 0.56), reflecting\n> spatial coverage.\n\nReadings for the sessions: (a) N, F and N' pooled, (b) N', (c) F. Variants: the code's peak rule\n(> 3 Hz), 4 and 2 cm smoothing.\n''')\ncode(r'''\nrows = []\nfor s in SMOOTHS:\n    S = SC[s]\n    for reading, eps in ((\"(a) pooled\", [0, 1, 2]), (\"(b) N'\", [2]), (\"(c) F\", [1]), (\"N (not a reading)\", [0]), (\"N and N' (not a reading)\", [0, 2])):\n        for reg in (\"PFC\", \"CA1\"):\n            x = S[(S.region == reg) & S.ep.isin(eps)]\n            r, p, n = pear(x.si_in.values, x.si_out.values)\n            rg, pg, ng = pear(x.si_in_gt.values, x.si_out_gt.values)\n            rows.append({\"smoothing\": s, \"reading\": reading, \"region\": reg, \"r\": r, \"p\": p, \"n\": n, \"r (> 3 Hz)\": rg, \"n (> 3 Hz)\": ng})\nT3D = pd.DataFrame(rows)\nwith pd.option_context(\"display.float_format\", lambda v: f\"{v:.3g}\"):\n    print(T3D.to_string(index=False))\nprint(\"\\nTolerance: PFC -0.55 to -0.45, CA1 0.504 to 0.616.\")\nfor reg in (\"PFC\", \"CA1\"):\n    x = SC[8.0][(SC[8.0].region == reg) & (SC[8.0].ep == 2)]\n    print(f\"{reg} N', per animal r:\", {a: (round(pear(g.si_in.values, g.si_out.values)[0], 2), pear(g.si_in.values, g.si_out.values)[2])\n                                       for a, g in x.groupby(\"animal\") if np.isfinite(g.si_in).sum() > 3})\n''', tags=[\"claim:fig3d-selectivity-index\"])\nconcl(\"fig3d-selectivity-index\")\n\nmd(r'''\n### fig3e-selectivity-stable\n\n> Trajectory selectivity is stable across environments for PFC cells (r = 0.49 between familiar and\n> novel) but not for CA1 cells (r = 0.12, not significant).\n\nSI(IN) and SI(OUT) pooled in one correlation per region, F against the novel session: (a) N', (b) N.\n''')\ncode(r'''\nrows = []\nfor s in SMOOTHS:\n    S = SC[s]\n    for reg in (\"PFC\", \"CA1\"):\n        x = S[S.region == reg].pivot_table(index=[\"animal\", \"unit\"], columns=\"ep\", values=[\"si_in\", \"si_out\"])\n        for nov in (2, 0):\n            a = np.r_[x[(\"si_in\", 1)], x[(\"si_out\", 1)]]; b = np.r_[x[(\"si_in\", nov)], x[(\"si_out\", nov)]]\n            r, p, n = pear(a, b)\n            rows.append({\"smoothing\": s, \"reading\": f\"F against {nfn.EPOCHS[nov]}\", \"region\": reg, \"r\": r, \"p\": p, \"n\": n})\nwith pd.option_context(\"display.float_format\", lambda v: f\"{v:.3g}\"):\n    print(pd.DataFrame(rows).to_string(index=False))\nprint(\"\\nTolerance: PFC 0.441 to 0.539, CA1 0.108 to 0.132 with p > 0.05.\")\n''', tags=[\"claim:fig3e-selectivity-stable\"])\nconcl(\"fig3e-selectivity-stable\")\n\nmd(r'''\n### figs5d-path-equivalence\n\n> PFC cells show stronger path equivalence (similar firing at the same trajectory phase across\n> trajectory types) than CA1 cells.\n\nOne-way ANOVA with Tukey's test over the six region by session groups.\n''')\ncode(r'''\nfor s in SMOOTHS:\n    S = SC[s]\n    names = [f\"{r} {nfn.EPOCHS[e]}\" for r in (\"CA1\", \"PFC\") for e in range(3)]\n    G = [S[(S.region == r) & (S.ep == e)].R.dropna().values for r in (\"CA1\", \"PFC\") for e in range(3)]\n    a, t = nfn.anova_tukey(G, names)\n    print(f\"smoothing {s:g} cm: medians {dict(zip(names, [round(float(np.median(g)), 3) for g in G]))}; n {a['n']}; F = {a['F']:.2f}, p = {a['p']:.2g}\")\n    for e in range(3):\n        r = t[(t.group1 == f\"CA1 {nfn.EPOCHS[e]}\") & (t.group2 == f\"PFC {nfn.EPOCHS[e]}\")].iloc[0]\n        print(f\"   {nfn.EPOCHS[e]}: PFC minus CA1 = {r['meandiff']:.3f}, Tukey p = {r['p-adj']:.4g}\")\nprint(\"R range:\", round(float(SC[8.0].R.min()), 3), \"to\", round(float(SC[8.0].R.max()), 3), \"; missing:\", int(SC[8.0].R.isna().sum()))\n''', tags=[\"claim:figs5d-path-equivalence\"])\nconcl(\"figs5d-path-equivalence\")\n\nmd(r'''\n### figs5e-path-equivalence-stable\n\n> The path-equivalent coefficient of PFC cells is strongly correlated between environments (r =\n> 0.64), more so than that of CA1 cells (r = 0.21).\n\nPearson r of R in F against R in the novel session ((a) N', (b) N), per region; Fisher's z for the\ndifference.\n''')\ncode(r'''\nfor s in SMOOTHS:\n    S = SC[s]\n    for nov in (2, 0):\n        res = {}\n        for reg in (\"PFC\", \"CA1\"):\n            x = S[S.region == reg].pivot_table(index=[\"animal\", \"unit\"], columns=\"ep\", values=\"R\")\n            res[reg] = pear(x[1].values, x[nov].values)\n        z, pz = nfn.fisher_z_compare(res[\"PFC\"][0], res[\"PFC\"][2], res[\"CA1\"][0], res[\"CA1\"][2])\n        print(f\"smoothing {s:g} cm, F against {nfn.EPOCHS[nov]}: PFC r = {res['PFC'][0]:.3f} (p {res['PFC'][1]:.2g}, n {res['PFC'][2]}), \"\n              f\"CA1 r = {res['CA1'][0]:.3f} (p {res['CA1'][1]:.2g}, n {res['CA1'][2]}); Fisher z = {z:.2f}, p = {pz:.2g}\")\nprint(\"Tolerance: PFC 0.576 to 0.704, CA1 0.189 to 0.231.\")\n''', tags=[\"claim:figs5e-path-equivalence-stable\"])\nconcl(\"figs5e-path-equivalence-stable\")\n\nmd(r'''\n### figs5f-path-equivalence-vs-selectivity\n\n> Path equivalence and task-sequence selectivity are uncorrelated across cells.\n\nPearson r per region of R against SI(IN) and against SI(OUT), cell samples of the three sessions\npooled; signed and absolute SI.\n''')\ncode(r'''\nfor s in SMOOTHS:\n    S = SC[s]\n    for reg in (\"CA1\", \"PFC\"):\n        for col in (\"si_in\", \"si_out\"):\n            x = S[S.region == reg]\n            r, p, n = pear(x.R.values, x[col].values); ra, pa, na = pear(x.R.values, np.abs(x[col].values))\n            print(f\"smoothing {s:g} cm, {reg} R against {col}: signed r = {r:.3f}, p = {p:.3g}; absolute r = {ra:.3f}, p = {pa:.3g} (n {n})\")\n''', tags=[\"claim:figs5f-path-equivalence-vs-selectivity\"])\nconcl(\"figs5f-path-equivalence-vs-selectivity\")\n\n# ---------------- manifold\nmd(r'''\n## Manifolds (Figure 3F to 3J, S6)\n\n### manifold-cell-counts\n\n> The pseudo-populations pooled across animals for the manifold analyses hold 98 CA1 and 171 PFC\n> cells.\n\nReadings: (a) the Methods', units included in N, F and N' with a linearized peak of at least 3 Hz\nin at least one session; (b) the code's, every unit included in all three sessions.\n''')\ncode(r'''\nPOP = {}\nfor reg in (\"CA1\", \"PFC\"):\n    b = {d[\"animal\"]: np.intersect1d(np.intersect1d(nfn.included(d, reg, 0), nfn.included(d, reg, 1)), nfn.included(d, reg, 2)) for d in A}\n    a = {}\n    for d in A:\n        cs = b[d[\"animal\"]]\n        pk = np.max([nfn.peak_rate({t: (MAPS[(d[\"animal\"], 8.0, e)][t][0], MAPS[(d[\"animal\"], 8.0, e)][t][1][cs]) for t in nfn.TRACKS}) for e in range(3)], 0)\n        a[d[\"animal\"]] = cs[pk >= 3]\n    POP[(reg, \"a\")], POP[(reg, \"b\")] = a, b\n    print(f\"{reg}: reading (a) {sum(len(v) for v in a.values())} cells {({k: len(v) for k, v in a.items()})}; \"\n          f\"reading (b) {sum(len(v) for v in b.values())} cells {({k: len(v) for k, v in b.items()})}\")\nprint(\"Expected: CA1 98 (88.2 to 107.8), PFC 171 (153.9 to 188.1).\")\n''', tags=[\"claim:manifold-cell-counts\"])\nconcl(\"manifold-cell-counts\")\n\nmd(r'''\n### The embeddings\n\nSingle-trial maps of the pseudo-population in N' (and F), as cal_UMAP.m: for each trajectory type the\nsmallest number of passes over the animals, from the first; maps at 1-cm bins (Methods, 8 cm\nsmoothing) on 201 bins of normalized length (cal_UMAP.m; about 1 cm on a 2-m trajectory), empty bins\ninside a pass filled (an assumption, see nfn.single_trial_matrix); states with fewer than 5 active\ncells dropped. UMAP (umap-learn) with 3 dimensions, cosine metric, 50 neighbours, min_dist 0.6, seed\n0; F is embedded with the N' fit (`transform`). Seeds 1 and 2 are variants.\n''')\ncode(r'''\nimport umap\nPOPSEL = {reg: POP[(reg, \"b\")] for reg in (\"CA1\", \"PFC\")}\nST = {}\nfor reg in (\"CA1\", \"PFC\"):\n    for ep in (2, 1):\n        tbt = {d[\"animal\"]: nfn.trials_of_track(d, ep) for d in A}\n        tn = {t: min(len(tbt[a][t]) for a in tbt) for t in nfn.TRACKS}\n        Xs = []\n        for d in A:\n            X, lab = nfn.single_trial_matrix(d, ep, POPSEL[reg][d[\"animal\"]], {t: tbt[d[\"animal\"]][t][:tn[t]] for t in nfn.TRACKS})\n            Xs.append(X)\n        X = np.hstack(Xs); v = (X > 0).sum(1) >= 5\n        ST[(reg, ep)] = (X[v], lab[v], tn, int((~v).sum()))\n        print(f\"{reg} {nfn.EPOCHS[ep]}: passes per trajectory {({nfn.TRACKS[k]: n for k, n in tn.items()})}; states {v.sum()} kept, {(~v).sum()} dropped (fewer than 5 active cells); cells {X.shape[1]}\")\nEMB = {}\nfor reg in (\"CA1\", \"PFC\"):\n    for seed in (0, 1, 2):\n        t0 = time.time()\n        um = umap.UMAP(n_components=3, metric=\"cosine\", n_neighbors=50, min_dist=0.6, random_state=seed)\n        E = um.fit_transform(ST[(reg, 2)][0]); EF = um.transform(ST[(reg, 1)][0])\n        EMB[(reg, seed)] = (E, EF, um)\n        print(f\"{reg} seed {seed}: fit and transform in {time.time() - t0:.0f} s\")\nfig = plt.figure(figsize=(14, 7))\nfor i, reg in enumerate((\"CA1\", \"PFC\")):\n    E, EF, _ = EMB[(reg, 0)]; lab = ST[(reg, 2)][1]\n    for j, (a_, b_) in enumerate(((0, 1), (0, 2), (1, 2))):\n        ax = fig.add_subplot(2, 4, i * 4 + j + 1)\n        for t, c in zip(nfn.TRACKS, (\"tab:red\", \"tab:blue\", \"tab:green\", \"tab:purple\")):\n            m = lab[:, 0] == t; ax.scatter(E[m, a_], E[m, b_], s=1, c=c, alpha=0.3, label=nfn.TRACKS[t])\n        ax.set_title(f\"{reg} N', dims {a_ + 1}-{b_ + 1}\", fontsize=9)\n    ax = fig.add_subplot(2, 4, i * 4 + 4)\n    sc_ = ax.scatter(E[:, 0], E[:, 1], s=1, c=lab[:, 2], cmap=\"viridis\"); ax.set_title(f\"{reg} N', colour = position\", fontsize=9)\nfig.axes[0].legend(markerscale=8, fontsize=7); plt.tight_layout(); plt.show()\nprint(\"All states are plotted (axes span the data).\")\n''')\n\nmd(r'''\n### fig3h-inseq-outseq-distance\n\n> In the PFC manifold, trajectories of the same task sequence (InSeq) are closer than trajectories\n> out of sequence (OutSeq); in the CA1 manifold, OutSeq pairs with the same spatial coverage are\n> closer than InSeq pairs.\n\nFor every pair of passes of the two types, the mean Euclidean distance over matched bins\n(cal_UMAP_INSeq_distance.m): CA1 matched by location, PFC by phase (the code); both regions by phase\nand both by location are variants. Rank-sum test per region.\n''')\ncode(r'''\nfrom scipy.spatial.distance import cdist\ndef seq_dist(E, lab, tn, align, nb=201):\n    idx = {(int(t), int(k), int(b)): i for i, (t, k, b) in enumerate(lab)}\n    out = {}\n    for name, pairs in ((\"InSeq\", [(1, 4), (3, 2)]), (\"OutSeq\", [(1, 2), (3, 4)])):\n        vals = []\n        for a_, b_ in pairs:\n            for t1 in range(tn[a_]):\n                for t2 in range(tn[b_]):\n                    ds = [np.linalg.norm(E[idx[(a_, t1, i)]] - E[idx[(b_, t2, j)]])\n                          for i in range(nb) for j in [i if align == \"location\" else nb - 1 - i]\n                          if (a_, t1, i) in idx and (b_, t2, j) in idx]\n                    if ds:\n                        vals.append(np.mean(ds))\n        out[name] = np.array(vals)\n    return out\ndef h_test(E, reg, align):\n    X, lab, tn, _ = ST[(reg, 2)]\n    sd = seq_dist(E, lab, tn, align)\n    return np.median(sd[\"InSeq\"]), np.median(sd[\"OutSeq\"]), stats.ranksums(sd[\"InSeq\"], sd[\"OutSeq\"]).pvalue, len(sd[\"InSeq\"]), len(sd[\"OutSeq\"])\nCODE_ALIGN = {\"CA1\": \"location\", \"PFC\": \"phase\"}\nfor seed in (0, 1, 2):\n    for reg in (\"CA1\", \"PFC\"):\n        E = EMB[(reg, seed)][0]\n        for align in (\"location\", \"phase\"):\n            i_, o_, p, ni, no = h_test(E, reg, align)\n            tag = \" (main)\" if (align == CODE_ALIGN[reg] and seed == 0) else \"\"\n            print(f\"seed {seed}, {reg}, aligned by {align}{tag}: InSeq median {i_:.3f} (n {ni}), OutSeq median {o_:.3f} (n {no}), rank-sum p = {p:.2g}\")\n''', tags=[\"claim:fig3h-inseq-outseq-distance\"])\nconcl(\"fig3h-inseq-outseq-distance\")\n\nmd(r'''\n### fig3i-phase-location-distance\n\n> PFC neural states at the same trajectory phase are closer than those at the same spatial location,\n> while CA1 shows the opposite.\n\nMain reading (Methods): same-phase distances from InSeq pairs aligned by phase, same-location\ndistances from same-side pairs aligned by location; all states at matched bins pooled. Variant\n(cal_UMAP_TrajPhase_vs_Spatial_distance.m): both from the same-side pairs.\n''')\ncode(r'''\ndef phase_loc(E, lab, mode, nb=201):\n    out = {\"phase\": [], \"location\": []}\n    sel = {(t, b): np.where((lab[:, 0] == t) & (lab[:, 2] == b))[0] for t in nfn.TRACKS for b in range(nb)}\n    for i in range(nb):\n        for a_, b_ in ((1, 2), (3, 4)):\n            p, q = sel[(a_, i)], sel[(b_, i)]\n            if len(p) and len(q): out[\"location\"].append(cdist(E[p], E[q]).ravel())\n        for a_, b_ in (((1, 4), (3, 2)) if mode == \"methods\" else ((1, 2), (3, 4))):\n            p, q = sel[(a_, i)], sel[(b_, nb - 1 - i)]\n            if len(p) and len(q): out[\"phase\"].append(cdist(E[p], E[q]).ravel())\n    return {k: np.concatenate(v) for k, v in out.items()}\nfor seed in (0, 1, 2):\n    for reg in (\"CA1\", \"PFC\"):\n        lab = ST[(reg, 2)][1]\n        for mode in (\"methods\", \"code\"):\n            pl = phase_loc(EMB[(reg, seed)][0], lab, mode)\n            print(f\"seed {seed}, {reg}, {mode}: phase median {np.median(pl['phase']):.3f}, location median {np.median(pl['location']):.3f}, \"\n                  f\"rank-sum p = {stats.ranksums(pl['phase'], pl['location']).pvalue:.2g} (n {len(pl['phase'])}, {len(pl['location'])})\")\n''', tags=[\"claim:fig3i-phase-location-distance\"])\nconcl(\"fig3i-phase-location-distance\")\n\nmd(r'''\n### fig3j-familiar-novel-manifold\n\n> The PFC manifold is preserved across environments (F states lie closer to N' states than cell-ID\n> shuffles do), while the distortion of the CA1 manifold is similar to that of random shuffles.\n\nFor each N' state, the mean Euclidean distance to the F states of the same trajectory type and bin\n(cal_UMAP_FNdistance.m). Chance: the N' activity with cell identities permuted, a new permutation for\neach pass, embedded with the same fit (cal_UMAP_FNdistance_shuffle.m). Rank-sum test per region.\n''')\ncode(r'''\ndef fn_dist(E, lab, EF, labF):\n    kE, kF = lab[:, 0] * 1000 + lab[:, 2], labF[:, 0] * 1000 + labF[:, 2]\n    out = np.full(len(E), np.nan)\n    for k in np.unique(kE):\n        p, q = np.where(kE == k)[0], np.where(kF == k)[0]\n        if len(q): out[p] = cdist(E[p], EF[q]).mean(1)\n    return out\ndef shuffled_activity(X, lab, rng):\n    Xs = X.copy()\n    for t, k in {(int(a_), int(b_)) for a_, b_, _ in lab}:\n        rows = np.where((lab[:, 0] == t) & (lab[:, 1] == k))[0]\n        Xs[rows] = X[rows][:, rng.permutation(X.shape[1])]\n    return Xs\nFNJ = {}\nfor seed in (0, 1, 2):\n    for reg in (\"CA1\", \"PFC\"):\n        X, lab, _, _ = ST[(reg, 2)]; XF, labF, _, _ = ST[(reg, 1)]\n        E, EF, um = EMB[(reg, seed)]\n        Xs = shuffled_activity(X, lab, np.random.default_rng([501, seed]))\n        ES = um.transform(Xs)\n        real, shuf = fn_dist(E, lab, EF, labF), fn_dist(E, lab, ES, lab)\n        FNJ[(reg, seed)] = (X, lab, XF, labF, Xs)\n        rr, ss = real[np.isfinite(real)], shuf[np.isfinite(shuf)]\n        print(f\"seed {seed}, {reg}: F-N' median {np.median(rr):.3f}, shuffle median {np.median(ss):.3f} \"\n              f\"(F-N' {100 * (np.median(rr) / np.median(ss) - 1):+.1f}%), rank-sum p = {stats.ranksums(rr, ss).pvalue:.2g} (n {len(rr)}, {len(ss)})\")\n''', tags=[\"claim:fig3j-familiar-novel-manifold\"])\nconcl(\"fig3j-familiar-novel-manifold\")\n\nmd(r'''\n### fig3fg-manifold-shapes\n\n> UMAP embeddings show that PFC population activity lies on a ring-shaped manifold, whereas the CA1\n> manifold has a double V shape resembling the W-maze.\n\nThe embeddings are shown above. The paper gives no measure of the shapes; by the criterion the\noutcome is that of fig3h-inseq-outseq-distance and fig3i-phase-location-distance.\n''')\ncode(r'''\nfor reg in (\"CA1\", \"PFC\"):\n    E = EMB[(reg, 0)][0]; lab = ST[(reg, 2)][1]\n    cent = np.array([[E[(lab[:, 0] == t) & (lab[:, 2] == b)].mean(0) for b in range(0, 201, 25)] for t in nfn.TRACKS])\n    print(f\"{reg}: mean embedded state per trajectory at normalized positions 0, 0.125, ..., 1 (dimension 1):\")\n    print(pd.DataFrame(cent[:, :, 0], index=[nfn.TRACKS[t] for t in nfn.TRACKS], columns=[f\"{b / 200:.3f}\" for b in range(0, 201, 25)]).round(2))\n''', tags=[\"claim:fig3fg-manifold-shapes\"])\nconcl(\"fig3fg-manifold-shapes\")\n\nmd(r'''\n### figs6-high-dimensional-distances\n\n> The distance relationships of Figure 3H to 3J hold in the original high-dimensional neural space.\n\nThe same tests with Euclidean distances between population vectors (cal_PV_*.m), with the main\nalignment of each test.\n''')\ncode(r'''\nfor reg in (\"CA1\", \"PFC\"):\n    X, lab, tn, _ = ST[(reg, 2)]\n    i_, o_, p, ni, no = h_test(X, reg, CODE_ALIGN[reg])\n    print(f\"{reg} 3H in neural space (aligned by {CODE_ALIGN[reg]}): InSeq {i_:.2f}, OutSeq {o_:.2f}, p = {p:.2g}\")\n    for align in (\"location\", \"phase\"):\n        if align != CODE_ALIGN[reg]:\n            i2, o2, p2, _, _ = h_test(X, reg, align); print(f\"   variant aligned by {align}: InSeq {i2:.2f}, OutSeq {o2:.2f}, p = {p2:.2g}\")\n    pl = phase_loc(X, lab, \"methods\")\n    print(f\"{reg} 3I in neural space: phase {np.median(pl['phase']):.2f}, location {np.median(pl['location']):.2f}, p = {stats.ranksums(pl['phase'], pl['location']).pvalue:.2g}\")\n    X, lab, XF, labF, Xs = FNJ[(reg, 0)]\n    real, shuf = fn_dist(X, lab, XF, labF), fn_dist(X, lab, Xs, lab)\n    rr, ss = real[np.isfinite(real)], shuf[np.isfinite(shuf)]\n    print(f\"{reg} 3J in neural space: F-N' {np.median(rr):.2f}, shuffle {np.median(ss):.2f} ({100 * (np.median(rr) / np.median(ss) - 1):+.1f}%), p = {stats.ranksums(rr, ss).pvalue:.2g}\")\n''', tags=[\"claim:figs6-high-dimensional-distances\"])\nconcl(\"figs6-high-dimensional-distances\")\n\n# ---------------- CCGP\nmd(r'''\n## Abstraction (Figure 4, S7)\n\n### fig4d-pfc-ccgp and fig4d-ca1-ccgp-chance\n\n> In PFC, the cross-condition generalization performance (CCGP) for trajectory phase, task sequence\n> and environment is high and above trial-label shuffles for every decoder.\n\n> In CA1, CCGP for trajectory phase, task sequence and environment is at or below chance by the\n> trial-label permutation test.\n\nClusters are the embedded states (seed 0) at 20-30% and 70-80% of the normalized position of each\ntrajectory (cal_all_dichotomies.m), in N' and, for the environment, in F. Decoders and permutation\ntest as nfn.ccgp_sets and nfn.svm_ccgp (1000 shuffles; p is the fraction of shuffles above the real\nCCGP, `p_ge` counts ties too). The code's task-sequence test pairs take the two clusters at different\nsegments (CCGP_taskSeq.m); taking them at the same segment is a variant. The code's environment\ntask-sequence decoders come in identical pairs (rows 1 and 3, 2 and 4 share their training set and\nF test set), as here.\n''')\ncode(r'''\nCL = {}\nCC = {}\nfor reg in (\"CA1\", \"PFC\"):\n    E, EF, _ = EMB[(reg, 0)]\n    CN, CF = nfn.clusters(E, ST[(reg, 2)][1]), nfn.clusters(EF, ST[(reg, 1)][1])\n    CL[reg] = (CN, CF)\n    print(reg, \"states per cluster, N':\", {f\"{nfn.TRACKS[t]} {s}\": len(v) for (t, s), v in CN.items()})\n    print(reg, \"states per cluster, F:\", {f\"{nfn.TRACKS[t]} {s}\": len(v) for (t, s), v in CF.items()})\n    t0 = time.time()\n    CC[reg] = nfn.run_ccgp(CN, CF, n_perm=1000, seed=601 if reg == \"PFC\" else 602)\n    print(f\"{reg}: 16 decoders with 1000 shuffles each in {time.time() - t0:.0f} s\")\n    print(CC[reg].round(3).to_string(index=False))\nCCV = {reg: nfn.run_ccgp(*CL[reg], n_perm=200, seed=603, seq_same_phase=True) for reg in (\"CA1\", \"PFC\")}\nfor reg in (\"CA1\", \"PFC\"):\n    x = CCV[reg][CCV[reg].variable != \"phase\"]\n    print(f\"variant, task-sequence clusters at the same segment, {reg}: CCGP {x.ccgp.round(3).tolist()}, p {x.p.round(3).tolist()}\")\n''')\ncode(r'''\nx = CC[\"PFC\"]\nprint(f\"PFC decoders with p < 0.001: {(x.p < 0.001).sum()} of {len(x)}; with p < 0.05: {(x.p < 0.05).sum()}\")\nprint(x.groupby(\"variable\").agg(mean_ccgp=(\"ccgp\", \"mean\"), min_ccgp=(\"ccgp\", \"min\"), n_p_below_0001=(\"p\", lambda v: int((v < 0.001).sum())), n=(\"p\", \"size\")).round(3))\nprint(\"decoders failing:\", x[x.p >= 0.001][[\"variable\", \"decoder\", \"ccgp\", \"null_95\", \"p\"]].round(3).to_string(index=False))\n''', tags=[\"claim:fig4d-pfc-ccgp\"])\nconcl(\"fig4d-pfc-ccgp\")\ncode(r'''\nx = CC[\"CA1\"]\nprint(f\"CA1 decoders with p < 0.05: {(x.p < 0.05).sum()} of {len(x)}\")\nprint(x.groupby(\"variable\").agg(mean_ccgp=(\"ccgp\", \"mean\"), max_ccgp=(\"ccgp\", \"max\"), n_p_below_005=(\"p\", lambda v: int((v < 0.05).sum())), n=(\"p\", \"size\")).round(3))\nprint(\"decoders above chance:\", x[x.p < 0.05][[\"variable\", \"decoder\", \"ccgp\", \"null_95\", \"p\", \"p_ge\"]].round(3).to_string(index=False))\n''', tags=[\"claim:fig4d-ca1-ccgp-chance\"])\nconcl(\"fig4d-ca1-ccgp-chance\")\n\nmd(r'''\n### figs7b-geometric-null\n\n> Against a geometric random model that keeps within-condition noise but destroys the geometry, PFC\n> CCGP is significant while CA1 CCGP is not.\n\nThe noise cloud of each cluster (its states about the centroid) has its axes permuted, separately per\ncluster, 100 times, and CCGP is recomputed. Readings: (a) the 3 UMAP coordinates; (b) the neuron axes\nof the cluster's population vectors, embedded with the N' fit. The CCGP of a variable is the mean\nover its decoders (an assumption; the legend plots the decoders with their median), compared with\nthe 95th percentile of the same mean under the null.\n''')\ncode(r'''\ndef cluster_rows(lab):\n    return {(t, s): (lab[:, 0] == t) & np.isin(lab[:, 2], b) for t in nfn.TRACKS for s, b in ((\"a\", nfn.EARLY_BINS), (\"b\", nfn.LATE_BINS))}\nGN = {}\nfor reg in (\"CA1\", \"PFC\"):\n    CN, CF = CL[reg]\n    real = nfn.ccgp_values(CN, CF).groupby(\"variable\").ccgp.mean()\n    rng = np.random.default_rng(701 if reg == \"CA1\" else 702)\n    null_a = pd.DataFrame([nfn.ccgp_values(nfn.permute_noise(CN, rng), nfn.permute_noise(CF, rng)).groupby(\"variable\").ccgp.mean() for _ in range(100)])\n    X, lab, _, _ = ST[(reg, 2)]; XF, labF, _, _ = ST[(reg, 1)]\n    um = EMB[(reg, 0)][2]\n    rN, rF = cluster_rows(lab), cluster_rows(labF)\n    nCN = {k: X[m] for k, m in rN.items()}; nCF = {k: XF[m] for k, m in rF.items()}\n    keys = list(nCN)\n    t0 = time.time()\n    null_b = []\n    for it in range(100):\n        pN, pF = nfn.permute_noise(nCN, rng), nfn.permute_noise(nCF, rng)\n        allN = um.transform(np.vstack([pN[k] for k in keys])); allF = um.transform(np.vstack([pF[k] for k in keys]))\n        sN = np.cumsum([0] + [len(pN[k]) for k in keys]); sF = np.cumsum([0] + [len(pF[k]) for k in keys])\n        eN = {k: allN[sN[i]:sN[i + 1]] for i, k in enumerate(keys)}; eF = {k: allF[sF[i]:sF[i + 1]] for i, k in enumerate(keys)}\n        null_b.append(nfn.ccgp_values(eN, eF).groupby(\"variable\").ccgp.mean())\n    null_b = pd.DataFrame(null_b)\n    GN[reg] = (real, null_a, null_b)\n    print(f\"{reg} (reading b in {time.time() - t0:.0f} s)\")\n    print(pd.DataFrame({\"CCGP (mean of decoders)\": real, \"null (a) 95th pct\": null_a.quantile(0.95), \"p (a)\": (null_a >= real).mean(),\n                        \"null (b) 95th pct\": null_b.quantile(0.95), \"p (b)\": (null_b >= real).mean()}).round(3))\n''', tags=[\"claim:figs7b-geometric-null\"])\nconcl(\"figs7b-geometric-null\")\n\nmd(r'''\n### figs7d-dichotomies-decodable\n\n> With traditional cross-validated decoders, most of the 35 dichotomies of the 8 clusters are decoded\n> accurately in both CA1 and PFC, with similar accuracy in the two regions.\n\nThe 35 balanced dichotomies of the 8 N' clusters, each decoded by a linear C-SVM with 4-fold\ncross-validation on the 3 UMAP coordinates. The trial-label permutation test uses 100 shuffles in\nplace of the paper's 1,000 (a deviation, for time: 1,000 would take about 45 minutes per region\nhere); p is resolved to 0.01, enough to decide p < 0.05. Rank-sum test of PFC against CA1 accuracies.\n''')\ncode(r'''\nfrom joblib import Parallel, delayed\nDI = {}\nfor reg in (\"CA1\", \"PFC\"):\n    CN = CL[reg][0]\n    t0 = time.time()\n    res = Parallel(n_jobs=4)(delayed(nfn.decode_dichotomy)(CN, g, 100, [801, i, reg == \"PFC\"]) for i, g in enumerate(nfn.dichotomies()))\n    DI[reg] = pd.DataFrame({\"accuracy\": [r[0] for r in res], \"p\": [r[1] for r in res], \"null_95\": [np.percentile(r[2], 95) for r in res]})\n    x = DI[reg]\n    print(f\"{reg} ({time.time() - t0:.0f} s): accuracy median {x.accuracy.median():.3f} (range {x.accuracy.min():.3f} to {x.accuracy.max():.3f}); \"\n          f\"p < 0.05 for {(x.p < 0.05).sum()} of 35; null 95th percentile median {x.null_95.median():.3f}\")\nprint(f\"rank-sum PFC against CA1 accuracies: p = {stats.ranksums(DI['PFC'].accuracy, DI['CA1'].accuracy).pvalue:.3g}; \"\n      f\"median difference {DI['PFC'].accuracy.median() - DI['CA1'].accuracy.median():+.3f}\")\n''', tags=[\"claim:figs7d-dichotomies-decodable\"])\nconcl(\"figs7d-dichotomies-decodable\")\n\ncode(r'''\nprint(f\"notebook ran in {(time.time() - started) / 60:.1f} min\")\n''')\n\nmd(open('/tmp/claude-1001/summary.md').read() if len(sys.argv) > 1 else \"## Summary\\n\\npending\", tags=[\"summary\"])\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"display_name\": \"Python 3\", \"language\": \"python\", \"name\": \"python3\"}\nnbf.write(nb, \"entries/000447-tang-2023/reproduce_tang_2023.ipynb\")\nprint(len(cells), \"cells\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
echo "# Reproducing Tang, Shin & Jadhav (2023) from dandiset 000447 (draft header)" > $TMPDIR/header.md; cd $TMPDIR && . dev/bin/activate && python build_nb.py && cd entries/000447-tang-2023 && date -u && time python -c "
import nbformat
from nbclient import NotebookClient
nb=nbformat.read('reproduce_tang_2023.ipynb',4)
NotebookClient(nb,timeout=3600,kernel_name='python3',resources={'metadata':{'path':'.'}}).execute()
nbformat.write(nb,'/tmp/claude-1001/dev_exec.ipynb')
" 2>&1 | tail -20
```

```
103 cells
Fri Oct 30 03:29:04 UTC 2026
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.

real	24m42.509s
user	54m2.310s
sys	0m8.020s
```

**Agent**

The notebook ran end to end but took 25 min, near the 30-min limit. Finding the slow cells.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import nbformat, datetime as dt
nb=nbformat.read('dev_exec.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    m=c.metadata.get('execution',{})
    a,b=m.get('iopub.execute_input'),m.get('shell.execute_reply')
    if a and b:
        d=(dt.datetime.fromisoformat(b.replace('Z',''))-dt.datetime.fromisoformat(a.replace('Z',''))).total_seconds()
        if d>20: print(i, round(d), c.metadata.get('tags'), c.source[:60].replace(chr(10),' '))
"
```

```
24 59 ['claim:figs3a-ca1-global-remapping'] # figs3a-ca1-global-remapping: CA1 F-N' against shuffle, spa
32 32 ['claim:figs3d-pfc-similarity-over-trials'] rows = [] for d in A:     tr = d["trials"]     mF = MAPS[(d[
38 43 None def decode_all(s=8.0, seed=401, **kw):     rng = np.random.d
73 90 None import umap POPSEL = {reg: POP[(reg, "b")] for reg in ("CA1"
81 39 ['claim:fig3j-familiar-novel-manifold'] def fn_dist(E, lab, EF, labF):     kE, kF = lab[:, 0] * 1000
90 283 None CL = {} CC = {} for reg in ("CA1", "PFC"):     E, EF, _ = EM
96 584 ['claim:figs7b-geometric-null'] def cluster_rows(lab):     return {(t, s): (lab[:, 0] == t) 
99 287 ['claim:figs7d-dichotomies-decodable'] from joblib import Parallel, delayed DI = {} for reg in ("CA
Shell cwd was reset to
```

**Agent**

The geometric null (reading b, 584 s) is the main cost; I'll run its 100 iterations in 4 parallel batches and cut the S3A shuffle draws to 100. First, reading all outputs.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import nbformat
nb=nbformat.read('dev_exec.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    out=''
    for o in c.get('outputs',[]):
        if o.output_type=='stream': out+=o.text
        elif o.output_type=='execute_result': out+=o.data.get('text/plain','')
        elif o.output_type=='error': out+='ERROR '+o.ename+' '+o.evalue
    print('=== cell',i,c.metadata.get('tags')); print(out[:6000])
" > dev_out.txt; wc -l dev_out.txt; grep -n ERROR dev_out.txt | head
```

```
754 dev_out.txt
Shell cwd was reset to
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/dev_out.txt",
 "limit": 330
}
```

```
1	=== cell 1 None
2	loaded 5 files from dandiset 000447 version 0.250724.2224, linearized and mapped in 10 s
3	
4	=== cell 3 ['sanity']
5	animal                                                        AM2                                   JS17                                   JS21                                   ZT2                                   JS34
6	file                         sub-JDS-NFN-AM2_behavior+ecephys.nwb  sub-JDS-NFN-JS17_behavior+ecephys.nwb  sub-JDS-NFN-JS21_behavior+ecephys.nwb  sub-JDS-NFN-ZT2_behavior+ecephys.nwb  sub-JDS-NFN-JS34_behavior+ecephys.nwb
7	units                                                          57                                     97                                     61                                   106                                     67
8	electrode rows                                                 62                                     64                                     64                                   128                                     64
9	tetrode labels                                                 31                                     32                                     32                                    64                                     32
10	max units/electrodes value                                     31                                     32                                     30                                    64                                     32
11	CA1 units (tetrode reading)                                    32                                     31                                     28                                    48                                     54
12	PFC units (tetrode reading)                                    25                                     66                                     33                                    58                                     13
13	CA1 units (row reading)                                        32         
[... 317 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/dev_out.txt",
 "offset": 330,
 "limit": 430
}
```

```
330	           JS17    1443     48          95.3           227.0
331	           JS21    1147     20         202.6           249.5
332	           JS34    2006     10         225.2           198.0
333	           ZT2     1564     39         169.5           203.0
334	       N   AM2      856     23          87.3           233.6
335	           JS17    1112     48         137.5           218.5
336	           JS21    1218     20         185.9           239.8
337	           JS34    1965     10         171.8           187.7
338	           ZT2     1586     39         158.5           209.0
339	
340	Error in cm; p-values of the tests:
341	                                   main (Methods, 8 cm)  step 50 ms (code)  smoothing 4 cm  smoothing 2 cm  decode restricted to the current trajectory
342	KW4 p                                          1.3e-148                  0       1.03e-115        3.54e-94                                            0
343	CA1 N median                                        172                172             175             182                                           15
344	CA1 F median                                        230                230             216             212                                         56.8
345	CA1 Dunn4 N-F p                               1.83e-140                  0       2.97e-109        1.93e-88                                            0
346	CA1 KW2 N-F p                                 1.04e-139                  0       1.19e-107        9.33e-87                                            0
347	CA1 N shuffle median                                221                221             220             224                                         48.8
348	CA1 N W(a) p                                   6.26e-94           1.3e-282        1.94e-80        4.96e-72                                            0
349	CA1 N W(b) p                                  1.12e-129                  0       8.51e-121       3.39e-114            
[... 406 more lines not kept]
```

**Agent**

All analyses ran. Before finalizing I'll check what `tools/entry.py check` enforces, so the notebook and files pass on the first go.

**Agent calls Bash**

```bash
grep -n "def \|error(\|fail\|tag\|runtime\|install" tools/entry.py | head -120
```

```
21:- each notebook has a cell tagged `sanity` that prints what was loaded;
26:notebook through a Jupyter kernel installed in that environment, in the entry
29:that takes longer than --max-minutes fails, even if it ran without error.
70:    def __init__(self):
73:    def error(self, where, message: str) -> None:
78:def dataset_id(record: dict) -> str | None:
83:def schema(name: str) -> Draft202012Validator:
94:def _parsed(text: str):
102:def _schema_errors(text: str, schema_name: str) -> tuple[str, ...]:
108:def load(report: Report, path: Path):
112:        report.error(path.relative_to(ROOT), problem)
116:def validate(report: Report, path: Path, schema_name: str) -> dict | None:
121:        report.error(path.relative_to(ROOT), message)
125:def _plain(value):
136:def code_of(notebook_path: Path) -> str:
143:def check(entry_dir: Path) -> Report:
150:        report.error(rel / "entry.yaml", f"name {entry.get('name')!r} must match the directory name")
155:        report.error(rel / name, "notebook is not listed in entry.yaml")
157:        report.error(rel / "entry.yaml", f"listed notebook {name!r} does not exist")
161:            report.error(rel / "entry.yaml", f"listed helper {name!r} does not exist")
[... 56 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,70p tools/entry.py; sed -n 313,420p tools/entry.py; date -u
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
[... 159 more lines not kept]
```

**Agent**

The clock reads 03:55, so about 3 h 20 min remain before 07:14. Testing a parallel version of the geometric null before rebuilding.

**Agent calls Bash**

```bash
cd entries/000447-tang-2023 && . $TMPDIR/dev/bin/activate && cat > $TMPDIR/t_gn.py <<'EOF'
import pickle,sys,time,numpy as np; sys.path.insert(0,'.'); import nfn
from joblib import Parallel, delayed
E,lab,EF,labF,um=pickle.load(open('/tmp/claude-1001/U_PFC.pkl','rb'))
ST=pickle.load(open('/tmp/claude-1001/ST.pkl','rb'))
X,l,tn=ST[('PFC',2)]
v=(X>0).sum(1)>=5; X=X[v]; XF,lF,_=ST[('PFC',1)]; XF=XF[(XF>0).sum(1)>=5]
rows=lambda lab:{(t,s):(lab[:,0]==t)&np.isin(lab[:,2],b) for t in nfn.TRACKS for s,b in (("a",nfn.EARLY_BINS),("b",nfn.LATE_BINS))}
nCN={k:X[m] for k,m in rows(lab).items()}; nCF={k:XF[m] for k,m in rows(labF).items()}
def batch(um,nCN,nCF,seed,n):
    import nfn, numpy as np
    rng=np.random.default_rng(seed); keys=list(nCN); out=[]
    for _ in range(n):
        pN,pF=nfn.permute_noise(nCN,rng),nfn.permute_noise(nCF,rng)
        aN=um.transform(np.vstack([pN[k] for k in keys])); aF=um.transform(np.vstack([pF[k] for k in keys]))
        sN=np.cumsum([0]+[len(pN[k]) for k in keys]); sF=np.cumsum([0]+[len(pF[k]) for k in keys])
        out.append(nfn.ccgp_values({k:aN[sN[i]:sN[i+1]] for i,k in enumerate(keys)},{k:aF[sF[i]:sF[i+1]] for i,k in enumerate(keys)}).groupby('variable').ccgp.mean())
    return out
t=time.time()
res=Parallel(n_jobs=4)(delayed(batch)(um,nCN,nCF,[1,i],3) for i in range(4))
print('12 iterations parallel',time.time()-t)
EOF
python $TMPDIR/t_gn.py 2>&1 | grep -v -i warn
```

```
12 iterations parallel 22.591719150543213
```

**Agent**

Parallel batches cut the geometric null to roughly 2.5 min per region. Updating the builder (parallel null, 100 shuffle draws in S3A) and checking the dev Python version against the entry's 3.13.

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python --version && pip list 2>/dev/null | grep -i -E "^(umap|numba|scikit-learn|numpy|scipy|pynndescent) " ; uv pip list 2>/dev/null | grep -i -E "^(umap-learn|numba|scikit-learn|numpy|scipy|pynndescent|statsmodels|pandas) "
python - <<'EOF'
p='/tmp/claude-1001/build_nb.py'
s=open(p).read()
old=s[s.index('    t0 = time.time()\n    null_b = []'):s.index('    null_b = pd.DataFrame(null_b)')]
new='''    t0 = time.time()
    batches = Parallel(n_jobs=4)(delayed(null_b_batch)(um, nCN, nCF, [703, reg == "PFC", i], 25) for i in range(4))
    null_b = [row for b in batches for row in b]
'''
s=s.replace(old,new)
s=s.replace('''def cluster_rows(lab):''','''from joblib import Parallel, delayed

def null_b_batch(um, nCN, nCF, seed, n):
    """Reading (b): permute the neuron axes of each cluster's noise cloud, embed with the N' fit."""
    rng = np.random.default_rng(seed); keys = list(nCN); out = []
    for _ in range(n):
        pN, pF = nfn.permute_noise(nCN, rng), nfn.permute_noise(nCF, rng)
        allN = um.transform(np.vstack([pN[k] for k in keys])); allF = um.transform(np.vstack([pF[k] for k in keys]))
        sN = np.cumsum([0] + [len(pN[k]) for k in keys]); sF = np.cumsum([0] + [len(pF[k]) for k in keys])
        eN = {k: allN[sN[i]:sN[i + 1]] for i, k in enumerate(keys)}; eF = {k: allF[sF[i]:sF[i + 1]] for i, k in enumerate(keys)}
        out.append(nfn.ccgp_values(eN, eF).groupby("variable").ccgp.mean())
    return out

def cluster_rows(lab):''')
s=s.replace('for k in range(200):','for k in range(100):').replace('over 200 shuffle draws','over 100 shuffle draws').replace('the result over 200 draws is shown too','the result over 100 draws is shown too')
s=s.replace('''    X, lab, _, _ = ST[(reg, 2)]; XF, labF, _, _ = ST[(reg, 1)]
    um = EMB[(reg, 0)][2]''','''    X, lab, _, _ = ST[(reg, 2)]; XF, labF, _, _ = ST[(reg, 1)]
    um = EMB[(reg, 0)][2]
    rng = np.random.default_rng(704 if reg == "CA1" else 705)''') if False else s
open(p,'w').write(s)
EOF
grep -n "null_b_batch\|range(100)\|keys = list(nCN)" /tmp/claude-1001/build_nb.py | head
```

```
Python 3.13.17
numba                     0.68.1
numpy                     2.5.4
pandas                    3.1.0
pynndescent               0.7.0
scikit-learn              1.9.1
scipy                     1.18.1
statsmodels               0.15.0
umap-learn                0.5.12
400:for k in range(100):
1254:def null_b_batch(um, nCN, nCF, seed, n):
1256:    rng = np.random.default_rng(seed); keys = list(nCN); out = []
1272:    null_a = pd.DataFrame([nfn.ccgp_values(nfn.permute_noise(CN, rng), nfn.permute_noise(CF, rng)).groupby("variable").ccgp.mean() for _ in range(100)])
1277:    keys = list(nCN)
1279:    batches = Parallel(n_jobs=4)(delayed(null_b_batch)(um, nCN, nCF, [703, reg == "PFC", i], 25) for i in range(4))
```

**Agent**

Dev environment matches the entry's Python 3.13 and current packages. Writing the entry files and the notebook header.

**Agent calls Bash**

```bash
cat > requirements.in <<'EOF'
dandi
h5py
joblib
matplotlib
numpy
pandas
remfile
scikit-learn
scikit-posthocs
scipy
statsmodels
umap-learn
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: 000447-tang-2023
type: reproduction
title: Hippocampal and prefrontal maps across a novel and a familiar W-maze (Tang, Shin and Jadhav 2023)
description: Tests the findings of Tang, Shin and Jadhav (2023) on dandiset 000447, which holds CA1
  and prefrontal units, position and trial tables of five rats running a W-maze alternation task in
  a novel, a familiar and again the novel room. It compares spatial maps across environments,
  Bayesian decoding with novel-room templates, selectivity and path equivalence of single cells,
  UMAP manifolds of the pooled populations, and cross-condition generalization. The de novo learning
  sessions and the second group of rats behind Figure 1 are not in the dandiset.
license: Apache-2.0
notebooks:
- path: reproduce_tang_2023.ipynb
  title: Reproducing Tang, Shin and Jadhav (2023) from dandiset 000447
  runtime_minutes: 20
helpers:
- nfn.py
related:
- id: dandi:000447/0.250724.2224
  relation: uses_data
- id: doi:10.1016/j.celrep.2023.112246
  relation: reproduces
EOF
python ../../tools/entry.py lock . 2>&1 | tail -2; grep -i -E "^(umap-learn|numba|scikit-learn|numpy|scipy|pynndescent|statsmodels|pandas)==" requirements.lock.txt
```

```
wrote entries/000447-tang-2023/requirements.lock.txt
numba==0.68.1
numpy==2.5.4
pandas==3.1.0
pynndescent==0.7.0
scikit-learn==1.9.1
scipy==1.18.1
statsmodels==0.15.0
umap-learn==0.5.12
```

**Agent**

Writing the header, the per-claim conclusions and the summary (from the development run; I'll check every number against the official run).

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/header.md",
 "content": "# Reproducing Tang, Shin & Jadhav (2023) from dandiset 000447\n\n**Paper.** Tang W, Shin JD, Jadhav SP (2023). Geometric transformation of cognitive maps for\ngeneralization across hippocampal-prefrontal circuits. *Cell Reports* 42, 112246.\n[doi:10.1016/j.celrep.2023.112246](https://doi.org/10.1016/j.celrep.2023.112246). The claims file\n(`claims/000447/10.1016-j.celrep.2023.112246.yaml`) was written from the NIH author manuscript in\nPubMed Central (PMC10124109) with its STAR Methods and supplement; the version of record was not\nread. Method details the claims file lacks were taken from the same text and from the paper's code,\ngithub.com/JadhavLab/GeometricTransformation at commit 5e55e69 (cited where used, in the cells and\nin `nfn.py`).\n\n**Dataset.** [DANDI:000447](https://dandiarchive.org/dandiset/000447/0.250724.2224), version\n0.250724.2224. The paper cites no version (its data statement says the data are on Brandeis\nservers, on request), so the most recent published version is pinned. The other published version,\n0.230316.2133, holds the same five files; their spike times, unit electrodes, trial tables, epochs and\npositions are identical byte for byte (checked while preparing, not re-run here), and the file sizes\ndiffer by about 169 kB of metadata.\n\n**What the dandiset holds.** One file per rat (AM2, JS17, JS21, ZT2, JS34) for the N-F-N' day: three\nW-track epochs, a trials table (start and end well, inbound or outbound, correct), 2D position with\nspeed at 30 frames per second, sorted units (spike times and a tetrode number) and the 1.5 kHz LFP.\nIt does not hold the de novo learning sessions, the three F-N-F'-N' rats, linearized positions,\nripple or theta times, waveforms, or cell labels.\n\n**Outside inputs.** None. The paper's code is read for method details only.\n\n| Claim | Tested or blocked |\n|---|---|\n| fig1b-faster-novel-learning | blocked, data missing (de novo sessions) |\n| fig1-denovo-final-performance | blocked, data missing (de novo sessions) |\n| fig1c-session-performance | blocked, data missing (de novo sessions) |\n| fig1c-familiar-above-novel | tested on N, F, N' (the F-N-F'-N' rats are missing) |\n| figs1b-first-session-inbound-outbound | blocked, data missing (de novo sessions) |\n| cells-per-session | tested |\n| figs3a-ca1-global-remapping | tested |\n| figs3a-pfc-similar-ca1-lower | tested |\n| fig2d-pv-similarity | tested |\n| fig2e-ca1-error-familiar | tested |\n| fig2e-pfc-error-stable | tested |\n| fig2f-switch-dynamics | tested |\n| figs3c-pfc-assimilation | tested |\n| figs3d-pfc-similarity-over-trials | tested |\n| figs4-ramping-fraction | tested |\n| figs4-ramping-generalization | run; blocked for too few ramping cells per population |\n| figs4d-reward-location-similarity | tested |\n| figs5d-path-equivalence | tested |\n| figs5e-path-equivalence-stable | tested |\n| figs5f-path-equivalence-vs-selectivity | run; blocked, methods underspecified (signed or absolute SI) |\n| fig3d-selectivity-index | tested |\n| fig3e-selectivity-stable | tested |\n| manifold-cell-counts | tested |\n| fig3fg-manifold-shapes | tested (through 3H and 3I) |\n| fig3h-inseq-outseq-distance | tested |\n| fig3i-phase-location-distance | tested |\n| fig3j-familiar-novel-manifold | tested |\n| figs6-high-dimensional-distances | tested |\n| fig4d-pfc-ccgp | tested |\n| fig4d-ca1-ccgp-chance | tested |\n| figs7b-geometric-null | tested |\n| figs7d-dichotomies-decodable | tested (100 shuffles in place of 1,000) |\n\nThe blocked behaviour claims need the de novo learning sessions, which the dandiset does not hold\nand which the paper says are on Brandeis servers, available on request.\n"
}
```

```
<tool_use_error>File has not been read yet. Read it first before writing to it.</tool_use_error>
```

**Agent calls Bash**

```bash
rm /tmp/claude-1001/header.md
```

```
(Bash completed with no output)
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/header.md",
 "content": "# Reproducing Tang, Shin & Jadhav (2023) from dandiset 000447\n\n**Paper.** Tang W, Shin JD, Jadhav SP (2023). Geometric transformation of cognitive maps for\ngeneralization across hippocampal-prefrontal circuits. *Cell Reports* 42, 112246.\n[doi:10.1016/j.celrep.2023.112246](https://doi.org/10.1016/j.celrep.2023.112246). The claims file\n(`claims/000447/10.1016-j.celrep.2023.112246.yaml`) was written from the NIH author manuscript in\nPubMed Central (PMC10124109) with its STAR Methods and supplement; the version of record was not\nread. Method details the claims file lacks were taken from the same text and from the paper's code,\ngithub.com/JadhavLab/GeometricTransformation at commit 5e55e69 (cited where used, in the cells and\nin `nfn.py`).\n\n**Dataset.** [DANDI:000447](https://dandiarchive.org/dandiset/000447/0.250724.2224), version\n0.250724.2224. The paper cites no version (its data statement says the data are on Brandeis\nservers, on request), so the most recent published version is pinned. The other published version,\n0.230316.2133, holds the same five files; their spike times, unit electrodes, trial tables, epochs and\npositions are identical byte for byte (checked while preparing, not re-run here), and the file sizes\ndiffer by about 169 kB of metadata.\n\n**What the dandiset holds.** One file per rat (AM2, JS17, JS21, ZT2, JS34) for the N-F-N' day: three\nW-track epochs, a trials table (start and end well, inbound or outbound, correct), 2D position with\nspeed at 30 frames per second, sorted units (spike times and a tetrode number) and the 1.5 kHz LFP.\nIt does not hold the de novo learning sessions, the three F-N-F'-N' rats, linearized positions,\nripple or theta times, waveforms, or cell labels.\n\n**Outside inputs.** None. The paper's code is read for method details only.\n\n| Claim | Tested or blocked |\n|---|---|\n| fig1b-faster-novel-learning | blocked, data missing (de novo sessions) |\n| fig1-denovo-final-performance | blocked, data missing (de novo sessions) |\n| fig1c-session-performance | blocked, data missing (de novo sessions) |\n| fig1c-familiar-above-novel | tested on N, F, N' (the F-N-F'-N' rats are missing) |\n| figs1b-first-session-inbound-outbound | blocked, data missing (de novo sessions) |\n| cells-per-session | tested |\n| figs3a-ca1-global-remapping | tested |\n| figs3a-pfc-similar-ca1-lower | tested |\n| fig2d-pv-similarity | tested |\n| fig2e-ca1-error-familiar | tested |\n| fig2e-pfc-error-stable | tested |\n| fig2f-switch-dynamics | tested |\n| figs3c-pfc-assimilation | tested |\n| figs3d-pfc-similarity-over-trials | tested |\n| figs4-ramping-fraction | tested |\n| figs4-ramping-generalization | run; blocked for too few ramping cells per population |\n| figs4d-reward-location-similarity | tested |\n| figs5d-path-equivalence | tested |\n| figs5e-path-equivalence-stable | tested |\n| figs5f-path-equivalence-vs-selectivity | run; blocked, methods underspecified (signed or absolute SI) |\n| fig3d-selectivity-index | tested |\n| fig3e-selectivity-stable | tested |\n| manifold-cell-counts | tested |\n| fig3fg-manifold-shapes | tested (through 3H and 3I) |\n| fig3h-inseq-outseq-distance | tested |\n| fig3i-phase-location-distance | tested |\n| fig3j-familiar-novel-manifold | tested |\n| figs6-high-dimensional-distances | tested |\n| fig4d-pfc-ccgp | tested |\n| fig4d-ca1-ccgp-chance | tested |\n| figs7b-geometric-null | tested |\n| figs7d-dichotomies-decodable | tested (100 shuffles in place of 1,000) |\n\nThe blocked behaviour claims need the de novo learning sessions, which the dandiset does not hold\nand which the paper says are on Brandeis servers, available on request.\n"
}
```

```
File created successfully at: /tmp/claude-1001/header.md (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/concl.py",
 "content": "import json\nC = {}\nC[\"fig1c-familiar-above-novel\"] = \"\"\"**Result: not reproduced (N-F-N' rats only).** On N, F and N' the repeated-measures ANOVA gives\nF(2,8) = 1.08, p = 0.383, and Tukey's test does not put F above N (difference 0.060, p = 0.70). F is\nabove N in four rats (0.078 to 0.222) and below it in ZT2 (-0.282), whose F session has 24 trials at\n0.50 correct. Estimating each session alone gives the same (p = 0.46). The F-N-F'-N' rats of Figure\nS1C are not in the dandiset, and the de novo sessions of the paper's five-group ANOVA are missing.\"\"\"\nC[\"cells-per-session\"] = \"\"\"**Result: reproduced.** Over the 15 animal-sessions there are 27.53 (SD 8.68) CA1 and 36.53 (SD\n18.60) PFC cells per session per animal, within the stated 30.5 (SD 9.8) and 37.4 (SD 19.3). The\nMethods' \"at least 100 spikes\" gives 27.67 and 36.53; counting each cell once per animal gives 34.8\nand 38.6.\"\"\"\nC[\"fig2d-pv-similarity\"] = \"\"\"**Result: reproduced.** With 8-cm smoothing, CA1 PV similarity is 0.419 to 0.652 within the\nnovel room (N-N') and -0.138 to 0.239 across rooms (F-N') in the five rats; PFC is 0.727 to 0.952\n(N-N') and 0.647 to 0.943 (F-N'). The repeated-measures ANOVA gives F(3,12) = 67.53, p = 8.8e-08;\nTukey's test puts CA1 F-N' below N-N' (difference 0.473, p = 0.0001) and finds no PFC difference\n(p = 0.99). The 4-cm and 2-cm widths and the code's \"> 3 Hz\" rule give the same outcome (CA1\np <= 0.0001, PFC p >= 0.99).\"\"\"\nC[\"figs3a-ca1-global-remapping\"] = \"\"\"**Result: reproduced.** For the CA1 spatial correlation, Tukey's test finds no difference\nbetween F-N' and the cell-ID shuffle (F-N' higher by 0.074, p = 0.075). The outcome depends on the\nshuffle draw: over 100 draws, p falls below 0.05 in a fraction of them printed above, with F-N' always\nhigher than the shuffle. One of five rats (JS17, median r 0.31) keeps some CA1 spatial correlation\nacross rooms.\"\"\"\nC[\"figs3a-pfc-similar-ca1-lower\"] = \"\"\"**Result: partially reproduced.** PFC F-N' does not differ from N-N' in rate overlap (map mean,\np = 0.94; run rate, p = 0.82) or spatial correlation (p = 0.52). CA1 F-N' is below N-N' in spatial\ncorrelation (difference 0.524, p < 0.0001) but not in rate overlap (p = 0.32 and 0.45), so the claim\nholds for one measure. The 4-cm and 2-cm widths give the same pattern.\"\"\"\nC[\"figs3c-pfc-assimilation\"] = \"\"\"**Result: reproduced.** With bins pooled over rats (8 cm), PFC F-N' exceeds F-N (0.836 against\n0.774, Tukey p < 0.0001), CA1 F-N and F-N' do not differ (0.062 and 0.045, p = 0.065), and CA1 F-N'\nis below N-N' (0.517, p < 0.0001). PFC F-N' is below N-N' (difference 0.019, p = 0.0001; the paper\nreports p = 0.0013). The 4-cm and 2-cm widths give the same outcome (CA1 F-N against F-N' p = 0.098\nand 0.26).\"\"\"\nC[\"figs3d-pfc-similarity-over-trials\"] = \"\"\"**Result: reproduced, resting on an assumption about which trials.** In PFC the last trial is\nabove the first under every reading: N then N' (0.688 to 0.741, Tukey p = 0.0018), N (0.684 to 0.757,\np < 0.0001) and N' (0.738 to 0.782, p = 0.0074). In CA1 first and last do not differ under N then\nN' (0.053 and 0.048, p = 1.0), but CA1 similarity falls from the first to the last trial under N\n(0.136 to 0.033, p = 0.0014) and N' (0.114 to 0.002, p < 0.0001). The readings disagree for CA1; N\nthen N', all trials in the novel environment, is the one adopted. Few CA1 trials pass the 80% rule\n(JS34 and ZT2 have none in N).\"\"\"\nC[\"figs4d-reward-location-similarity\"] = \"\"\"**Result: reproduced.** Grubbs' test finds no outlier among the bins of either region, for F-N'\nand F-N, over all bins (p = 1 in every case) or per trajectory (smallest p 0.40). The values at the\nwell ends lie inside the range of the other bins (CA1 F-N' -0.100 to 0.224, PFC 0.723 to 0.901).\"\"\"\nC[\"fig2e-ca1-error-familiar\"] = \"\"\"**Result: partially reproduced.** CA1 error is higher in F than in N (median 230 against 172 cm,\nDunn p = 1.8e-140), in every variant. In F the CA1 error is not below the shuffle; it is above it (mean\npaired difference 8.8 cm), and the Wilcoxon test finds the difference under both shuffle readings\n(p = 2.4e-08 and 0.042), so the claim of no difference fails by the paper's test. The 4-cm width\ngives p = 0.79 for reading (b), and 2 cm puts F slightly below the shuffle (-3.5 cm, p = 0.0067).\"\"\"\nC[\"fig2e-pfc-error-stable\"] = \"\"\"**Result: partially reproduced.** PFC error is below the shuffle in N (149 against 218 cm,\np = 1.3e-91 and 6.4e-67) and in F (186 against 223 cm, p = 7.8e-32 and 2.4e-35). It is not similar in\nN and F: F is higher (Dunn p = 7.0e-06; N and F alone, p = 3.9e-06), in every variant (p 6.2e-05 to\n1.4e-17). With the decode restricted to the current trajectory, F is lower than N (23.5 against 28.5\ncm). Three of five rats have higher PFC error in F.\"\"\"\nC[\"fig2f-switch-dynamics\"] = \"\"\"**Result: reproduced, resting on an assumption about trial -1.** With trial -1 as the last N trial\n(reading a, the Methods decoder), CA1 error rises from 182 to 223 cm between trial -1 and trial 1\n(Dunn p = 0.0021), and PFC does not differ (149 and 200 cm, p = 0.12). With the code's selection of\nthe first ten N trials (reading b), CA1 trial 1 is not above trial -1 (196 against 259 cm, p = 0.11).\nThe code's decoder gives no CA1 difference under either reading (p = 1). Reading (a) is adopted: the\ncode's batch script means to take the last ten N trials (its comment) but its condition never holds.\"\"\"\nC[\"figs4-ramping-fraction\"] = \"\"\"**Result: not reproduced.** Ramping samples are 3.0% of CA1 (49 of 1652) and 3.1% of PFC (67 of\n2192) cell samples over all sessions, and 3.7% (22 of 596) and 3.0% (22 of 728) in N', against 16.4%\nand 18.1%. No smoothing width or denominator gives more than 7.6%. The N' denominators (596 and 728)\nare above the stated 495 and 636 beyond tolerance.\"\"\"\nC[\"figs4-ramping-generalization\"] = \"\"\"**Result: blocked (too few ramping cells).** Only one animal-trajectory population per region has\n3 or more ramping cells, so the ramping groups are one population of 101 bins each. On it, CA1\nramping F-N' is below N-N' (p = 1.7e-22), PFC ramping does not change (p = 0.34), and ramping and\nother cells differ only for CA1 F-N' (p = 0.014). With the ramping cells pooled over animals, the CA1\nramping drop is not found (p = 1). The test rests on too few cells to decide.\"\"\"\nC[\"figs5d-path-equivalence\"] = \"\"\"**Result: reproduced.** PFC R exceeds CA1 R in every session (N: difference 0.173, Tukey\np = 0.0002; F and N': p < 0.0001), with ANOVA F = 22.97, p = 1.3e-21, over 99 CA1 and 171 PFC cells.\nThe 4-cm and 2-cm widths give the same (largest p 0.002).\"\"\"\nC[\"figs5e-path-equivalence-stable\"] = \"\"\"**Result: partially reproduced, resting on the smoothing width.** F against N' (8 cm), PFC\nr = 0.572 and CA1 r = 0.231, and Fisher's z = 3.24, p = 0.0012, puts PFC above CA1; CA1 is within\ntolerance and PFC 0.004 below it. F against N gives PFC 0.552 and CA1 0.095. With 4-cm smoothing both\nvalues are within tolerance (0.613 and 0.201, p = 6.8e-05), which would make it reproduced; 2 cm\ngives 0.647 and 0.139.\"\"\"\nC[\"figs5f-path-equivalence-vs-selectivity\"] = \"\"\"**Result: blocked, methods underspecified.** With the signed SI no correlation reaches p < 0.05\n(smallest p 0.26 at 8 cm). With the absolute SI three of four do (CA1 SI(IN) r = -0.174, p = 0.025;\nPFC SI(IN) r = -0.241 and SI(OUT) r = -0.208, p < 0.0001). The criterion makes the claim\nmethods_underspecified when only one reading finds a correlation.\"\"\"\nC[\"fig3d-selectivity-index\"] = \"\"\"**Result: not reproduced, resting on the smoothing width.** PFC SI(IN) and SI(OUT) are negatively\ncorrelated under every reading, and in N' within tolerance (r = -0.466, p = 7.0e-08). CA1 is\npositively correlated but weaker than stated: r = 0.284 pooled, 0.280 in N' (p = 0.040) and 0.127 in\nF (p = 0.41), against 0.56. As reading (c) is not significant, the partial clause does not hold. With\n2-cm smoothing CA1 F is significant (r = 0.336, p = 0.0062), which would make it partially\nreproduced.\"\"\"\nC[\"fig3e-selectivity-stable\"] = \"\"\"**Result: not reproduced, resting on the smoothing width.** PFC selectivity is correlated between\nF and the novel room (N': r = 0.437, p = 5.2e-11, just below the tolerance of 0.441; N: 0.363), but CA1\nis correlated too (N': r = 0.318, p = 0.012; N: r = 0.384, p = 0.00086). With 2-cm smoothing CA1 F\nagainst N' is not significant (r = 0.128, p = 0.20) and PFC is 0.406, which would make it partially\nreproduced.\"\"\"\nC[\"manifold-cell-counts\"] = \"\"\"**Result: reproduced.** The code's reading (units included in N, F and N') gives 99 CA1 and 171\nPFC cells, against 98 and 171. The Methods' reading (also tuned) gives 95 and 151; PFC is below the\ntolerance. The code's reading is used for the manifolds.\"\"\"\nC[\"fig3h-inseq-outseq-distance\"] = \"\"\"**Result: reproduced.** In CA1 (aligned by location), OutSeq pairs are closer than InSeq pairs\n(13.83 against 17.08, rank-sum p = 0.00067); in PFC (aligned by phase), InSeq pairs are closer (14.72\nagainst 16.83, p = 0.015). Both regions keep the direction under every alignment and seed; the\np-values vary with the UMAP seed (seed 1: CA1 p = 0.096, PFC p = 0.016).\"\"\"\nC[\"fig3i-phase-location-distance\"] = \"\"\"**Result: reproduced.** In PFC, same-phase states are closer than same-location states (14.52\nagainst 16.91, p = 4.7e-181); in CA1 the opposite holds (17.98 against 13.84, p near 0). The same\nholds for seeds 1 and 2. The code's variant (both from same-side pairs) agrees for PFC under every\nseed and for CA1 under seeds 0 and 1.\"\"\"\nC[\"fig3j-familiar-novel-manifold\"] = \"\"\"**Result: partially reproduced.** PFC F states lie closer to N' states than the shuffle does\n(11.70 against 14.56, 19.6% closer, p = 8.6e-241). CA1 F states are also closer than the shuffle,\nby less (13.65 against 13.97, 2.3% closer, p = 1.5e-25), so the claim that CA1 does not differ from the\nshuffle fails by the paper's test. Seeds 1 and 2 give the same (CA1 3.3% to 6.0% closer, PFC 16.2%\nto 24.8%).\"\"\"\nC[\"fig3fg-manifold-shapes\"] = \"\"\"**Result: reproduced (through 3H and 3I).** Both distance tests that the criterion takes as the\nmeasure of the shapes reproduce. The embeddings and the mean state per trajectory are shown; no\nmeasure of a ring or a double V is computed.\"\"\"\nC[\"figs6-high-dimensional-distances\"] = \"\"\"**Result: partially reproduced.** In the neural space, 3H holds (CA1 OutSeq closer, p = 2.5e-12;\nPFC InSeq closer, p = 4.8e-12) and 3I holds (PFC phase 65.47 against location 86.09; CA1 location\n45.02 against phase 48.37, p = 9.3e-129). For 3J, PFC F-N' is far below the shuffle (56.6% closer)\nbut CA1 F-N' is below it too (9.2% closer, p = 7.5e-78), so two of the three relationships hold.\"\"\"\nC[\"fig4d-pfc-ccgp\"] = \"\"\"**Result: partially reproduced.** Nine of the 16 PFC decoders have p < 0.001 and 12 have p < 0.05.\nThe task-sequence decoders are high (0.75 to 0.80, one at 0.50), while one trajectory-phase decoder\n(test OUT_L, 0.230) and three of the four environment phase decoders (0.385 to 0.512) are at or\nbelow chance.\"\"\"\nC[\"fig4d-ca1-ccgp-chance\"] = \"\"\"**Result: not reproduced.** The four CA1 trajectory-phase decoders are at or below chance (0.417 to\n0.500, smallest p 0.119), but six of 16 CA1 decoders have p < 0.05: one task-sequence decoder (0.596),\ntwo environment phase decoders (0.582 and 0.562) and the two environment task-sequence decoders held\nout on the inbound pair (0.642). A sixth sits at 0.500 with p = 0 under the code's strict count of\nshuffles above it (p = 1 counting ties).\"\"\"\nC[\"figs7b-geometric-null\"] = \"\"\"**Result: not reproduced.** Against the geometric random model, no PFC variable exceeds the 95th\npercentile of its null under either reading (PFC p 0.29 to 0.86 in reading a; see reading b above),\nand no CA1 variable does either. The PFC part of the claim fails.\"\"\"\nC[\"figs7d-dichotomies-decodable\"] = \"\"\"**Result: partially reproduced.** Most dichotomies are decoded above the shuffles in both regions\n(CA1 35 of 35, PFC 33 of 35), but the accuracies differ: CA1 is higher (median 0.831 against 0.660,\nrank-sum p = 5.7e-08), so the claim of similar accuracy fails by the paper's test.\"\"\"\njson.dump(C, open('/tmp/claude-1001/conclusions.json', 'w'), indent=1)\nprint(len(C))\n"
}
```

```
File created successfully at: /tmp/claude-1001/concl.py (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/summary.md",
 "content": "## Summary\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\n| Claim | Outcome |\n|---|---|\n| fig1b-faster-novel-learning | blocked: data missing |\n| fig1-denovo-final-performance | blocked: data missing |\n| fig1c-session-performance | blocked: data missing |\n| fig1c-familiar-above-novel | not reproduced (N-F-N' rats only) |\n| figs1b-first-session-inbound-outbound | blocked: data missing |\n| cells-per-session | reproduced |\n| figs3a-ca1-global-remapping | reproduced |\n| figs3a-pfc-similar-ca1-lower | partially reproduced |\n| fig2d-pv-similarity | reproduced |\n| fig2e-ca1-error-familiar | partially reproduced |\n| fig2e-pfc-error-stable | partially reproduced |\n| fig2f-switch-dynamics | reproduced (assumption: trial -1 is the last N trial) |\n| figs3c-pfc-assimilation | reproduced |\n| figs3d-pfc-similarity-over-trials | reproduced (assumption: trials of N then N') |\n| figs4-ramping-fraction | not reproduced |\n| figs4-ramping-generalization | blocked: too few ramping cells |\n| figs4d-reward-location-similarity | reproduced |\n| figs5d-path-equivalence | reproduced |\n| figs5e-path-equivalence-stable | partially reproduced (assumption: 8-cm smoothing) |\n| figs5f-path-equivalence-vs-selectivity | blocked: methods underspecified |\n| fig3d-selectivity-index | not reproduced (assumption: 8-cm smoothing) |\n| fig3e-selectivity-stable | not reproduced (assumption: 8-cm smoothing) |\n| manifold-cell-counts | reproduced |\n| fig3fg-manifold-shapes | reproduced |\n| fig3h-inseq-outseq-distance | reproduced |\n| fig3i-phase-location-distance | reproduced |\n| fig3j-familiar-novel-manifold | partially reproduced |\n| figs6-high-dimensional-distances | partially reproduced |\n| fig4d-pfc-ccgp | partially reproduced |\n| fig4d-ca1-ccgp-chance | not reproduced |\n| figs7b-geometric-null | not reproduced |\n| figs7d-dichotomies-decodable | partially reproduced |\n\n**How the analysis differs from the paper's.**\n\n- Linearization. The dandiset has no linearized positions; positions are projected onto W-shaped\n  paths built from the well positions and the run positions (an assumption; 180 to 220 cm per\n  trajectory, median 5 cm from the path).\n- The 1D smoothing width is garbled in the paper's text; 8 cm is used, with 4 and 2 cm as variants.\n  Several outcomes change with it (figs5e, fig3d, fig3e, the CA1 shuffle test of fig2e).\n- Sharp-wave ripple times are not excluded from the rate maps (no ripple times in the dandiset), and\n  the decoder's theta restriction (a variant in the code) cannot be applied (no theta times).\n- The code's per-animal interneuron lists cannot be applied (no cell numbers); the code's 7 Hz rule\n  for CA1 is.\n- Single-trial maps for the manifolds have the empty 1-cm bins inside a pass filled linearly (an\n  assumption; without it the PFC embedding splits by which animals' cells are all zero).\n- The UMAP implementation is umap-learn with fixed seeds, not the MATLAB toolbox with the paper's\n  saved templates; the manifold results vary with the seed (seeds 0 to 2 shown).\n- Figure 1 and S1 behaviour is tested only on N, F and N' of the five rats; the de novo sessions and\n  the F-N-F'-N' rats are not in the dandiset.\n- The dichotomy decoders use 100 label shuffles in place of 1,000.\n\n**What was found about the dataset.**\n\n- The units table's `electrodes` column holds tetrode numbers, not row indices of the electrodes\n  table; read as row indices, units are put in the wrong region (up to 32 units per animal).\n- Units have no cell number within a tetrode, no waveform and no interneuron label, so the paper's\n  interneuron exclusion cannot be applied; units clustered only in later epochs are appended to the\n  table with no spike in N, without a note.\n- `acquisition/ElectricalSeries` is a byte-identical second copy of the 1.5 kHz LFP; there is no\n  30 kHz recording.\n- The position's reference frame is given as \"center well\", but positions are camera coordinates in\n  which the center well sits at different places in each room. Epochs carry no names; N, F, N' are\n  known only from the description's order. Linearized positions, the idealized track paths, ripple\n  and theta times are not included.\n- The de novo learning sessions and the F-N-F'-N' rats behind Figure 1C, 1B and S1 are not in the\n  dandiset.\n"
}
```

```
File created successfully at: /tmp/claude-1001/summary.md (file state is current in your context — no need to Read it back)
```

**Agent**

Adding the session start times and the position reference frame to the data check, then building and running the entry.

**Agent calls Bash**

```bash
python - <<'EOF'
p='nfn.py'; s=open(p).read()
s=s.replace('''    d["pos_unit"] = _str(f["processing/behavior/Position/SpatialSeries/data"].attrs.get("unit", ""))''','''    d["pos_unit"] = _str(f["processing/behavior/Position/SpatialSeries/data"].attrs.get("unit", ""))
    d["reference_frame"] = _str(f["processing/behavior/Position/SpatialSeries/reference_frame"][()])
    d["session_start"] = _str(f["session_start_time"][()])''')
open(p,'w').write(s)
p='/tmp/claude-1001/build_nb.py'; s=open(p).read()
s=s.replace('''print("\\ntrajectory types per epoch''','''for d in A:
    nfn.linearize(d) if "wells" not in d else None
    print(f"{d['animal']}: session_start_time {d['session_start']}; position reference frame {d['reference_frame']!r}; center-well position (cm) per epoch "
          + ", ".join(f"{nfn.EPOCHS[ep]} ({w[1][0]:.0f}, {w[1][1]:.0f})" for ep, w in d["wells"].items()))
print("\\ntrajectory types per epoch''')
open(p,'w').write(s)
EOF
grep -n "session_start_time {d" /tmp/claude-1001/build_nb.py | head -2; cd $TMPDIR && . dev/bin/activate && python concl.py && python build_nb.py x && cd  && python tools/entry.py check entries/000447-tang-2023 2>&1 | tail -5
```

```
82:    print(f"{d['animal']}: session_start_time {d['session_start']}; position reference frame {d['reference_frame']!r}; center-well position (cm) per epoch "
28
103 cells
0 error(s)
```

**Agent**

Check passes. Running the entry from a clean environment (about 20 min).

**Agent calls Bash**

```bash
date -u; python tools/entry.py all entries/000447-tang-2023 2>&1 | tail -15; date -u
```

```
Fri Oct 30 03:58:09 UTC 2026
Installed kernelspec registry-000447-tang-2023 in executed/000447-tang-2023/.venv/share/jupyter/kernels/registry-000447-tang-2023
0 error(s)
pass  reproduce_tang_2023.ipynb  (1214 s)
Fri Oct 30 04:18:34 UTC 2026
```

**Agent**

Passed in 20 min. Comparing the executed outputs with the conclusions.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import nbformat
nb=nbformat.read('executed/000447-tang-2023/reproduce_tang_2023.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    out=''
    for o in c.get('outputs',[]):
        if o.output_type=='stream': out+=o.text
        elif o.output_type=='execute_result': out+=o.data.get('text/plain','')
        elif o.output_type=='error': out+='ERROR '+o.ename+' '+o.evalue
    print('=== cell',i,c.metadata.get('tags')); print(out[:6000])
" > off_out.txt; diff <(grep -v " s)\| in [0-9]* s\|ran in" dev_out.txt) <(grep -v " s)\| in [0-9]* s\|ran in" off_out.txt) | head -80
```

```
24a25,29
> AM2: session_start_time 2023-03-14T17:31:07.596000-04:00; position reference frame 'center well'; center-well position (cm) per epoch N (32, 52), F (73, 86), N' (38, 50)
> JS17: session_start_time 2023-03-14T17:23:13.190000-04:00; position reference frame 'center well'; center-well position (cm) per epoch N (75, 96), F (80, 96), N' (66, 87)
> JS21: session_start_time 2023-03-14T17:27:16.913000-04:00; position reference frame 'center well'; center-well position (cm) per epoch N (38, 55), F (77, 93), N' (41, 56)
> ZT2: session_start_time 2023-03-14T17:34:53.914000-04:00; position reference frame 'center well'; center-well position (cm) per epoch N (33, 64), F (88, 93), N' (28, 60)
> JS34: session_start_time 2023-03-14T17:19:13.648000-04:00; position reference frame 'center well'; center-well position (cm) per epoch N (37, 57), F (82, 98), N' (32, 56)
241c246
< over 200 shuffle draws: Tukey p < 0.05 in 0.10 of draws; median p 0.303; F-N' minus shuffle mean difference median 0.051 (range 0.009 to 0.107)
---
> over 100 shuffle draws: Tukey p < 0.05 in 0.13 of draws; median p 0.291; F-N' minus shuffle mean difference median 0.051 (range 0.014 to 0.105)
722c727
< environment                    0.520              0.568   0.72              0.584   0.66
---
> environment                    0.520              0.568   0.72              0.575   0.57
724c729
< sequence                       0.308              0.521   0.93              0.744   0.77
---
> sequence                       0.308              0.521   0.93              0.745   0.69
727,729c732,734
< environment                    0.618              0.672   0.73              0.676   0.71
[... 7 more lines not kept]
```

**Agent**

Only the expected cells changed (100 shuffle draws, the geometric null's reading b). Updating those two conclusions.

**Agent calls Bash**

```bash
grep -n -A9 "claim:figs7b" $TMPDIR/off_out.txt; grep -n "shuffle draws" $TMPDIR/off_out.txt
```

```
738:=== cell 96 ['claim:figs7b-geometric-null']
739-CA1 (reading b in 76 s)
740-             CCGP (mean of decoders)  null (a) 95th pct  p (a)  null (b) 95th pct  p (b)
741-variable                                                                                
742-environment                    0.520              0.568   0.72              0.575   0.57
743-phase                          0.479              0.513   0.94              0.507   1.00
744-sequence                       0.308              0.521   0.93              0.745   0.69
745-PFC (reading b in 97 s)
746-             CCGP (mean of decoders)  null (a) 95th pct  p (a)  null (b) 95th pct  p (b)
747-variable                                                                                
252:over 100 shuffle draws: Tukey p < 0.05 in 0.13 of draws; median p 0.291; F-N' minus shuffle mean difference median 0.051 (range 0.014 to 0.105)
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='concl.py'; s=open(p).read()
s=s.replace('''shuffle draw: over 100 draws, p falls below 0.05 in a fraction of them printed above, with F-N' always
higher than the shuffle.''','''shuffle draw: over 100 draws, p falls below 0.05 in 13 of them (median p 0.29), and F-N' is always
higher than the shuffle (by 0.014 to 0.105).''')
s=s.replace('''percentile of its null under either reading (PFC p 0.29 to 0.86 in reading a; see reading b above),
and no CA1 variable does either. The PFC part of the claim fails.''','''percentile of its null under either reading (PFC p 0.29 to 0.86 in reading a and 0.23 to 0.65 in
reading b), and no CA1 variable does either (p 0.57 to 1.00). The PFC part of the claim fails.''')
open(p,'w').write(s)
p='summary.md'; s=open(p).read()
s=s.replace('''- The position's reference frame is given as "center well", but positions are camera coordinates in
  which the center well sits at different places in each room.''','''- The position's reference frame is given as "center well", but positions are camera coordinates in
  which the center well sits at different places in each room. The five files' session start times
  fall within 16 minutes of each other on 2023-03-14, the day of the upload, not of the recordings.''')
open(p,'w').write(s)
EOF
grep -c "13 of them" concl.py; grep -c "16 minutes" summary.md
```

```
1
1
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i 's/cm). Three of five rats have higher PFC error in F./cm). Four of five rats have higher PFC median error in F (JS17 is lower)./' concl.py && grep -c "Four of five" concl.py && sed -i 's/fall within 16 minutes of each other on 2023-03-14, the day of the upload, not of the recordings./fall within 16 minutes of each other on 2023-03-14, two days before the first published version: the time of conversion, not of the recordings./' summary.md && grep -c "time of conversion" summary.md
cd entries/000447-tang-2023 && python - <<'EOF'
p='nfn.py'; s=open(p).read()
s=s.replace('''- Region of a unit: units/electrodes holds the tetrode number (see the notebook's data check),
  and the region is the `location` of the electrode row whose label is that tetrode.
"""''','''- Region of a unit: units/electrodes holds the tetrode number (see the notebook's data check),
  and the region is the `location` of the electrode row whose label is that tetrode.
- Decoding (decode_session): Methods, "Bayesian decoding" (200-ms windows moving with 50 ms
  overlap, run periods, 15 cm from the wells excluded, uniform prior, Poisson); the error along
  the four trajectories laid end to end and the bin rule follow the claims file (the code,
  decoding_position_*_novelfamiliar_cross.m). RATE_FLOOR is a standard choice.
- Manifolds: 201 normalized bins and fewer than 5 active cells dropped (cal_UMAP.m); single-trial
  maps at 1-cm bins (Methods); clusters at 20-30% and 70-80% (cal_all_dichotomies.m); CCGP
  decoders and their permutation test (CCGP_*.m, decoding_CCGP_linearSVM_simple.m); dichotomies
  with 4-fold cross-validation (decoding_dichotomy_linearSVM.m). Filling empty bins of
  single-trial maps is an assumption (single_trial_matrix).
- Statistics: the tests named in the claims file; Dunn's test with Bonferroni adjustment and
  Tukey's test after a repeated-measures ANOVA on its error term, as GraphPad Prism (the paper's
  statistics software) runs them, are standard choices.
"""''')
open(p,'w').write(s)
EOF
grep -n "Statistics: the tests" nfn.py
```

```
1
1
40:- Statistics: the tests named in the claims file; Dunn's test with Bonferroni adjustment and
```

**Agent calls Write**

```json
{
 "file_path": "entries/000447-tang-2023/README.md",
 "content": "# Tang, Shin & Jadhav (2023) from dandiset 000447\n\nTests the findings of [Tang, Shin and Jadhav (2023)](https://doi.org/10.1016/j.celrep.2023.112246)\nthat can be tested on [DANDI:000447](https://dandiarchive.org/dandiset/000447/0.250724.2224), which\nholds CA1 and prefrontal units, position and trial tables of five rats running a W-maze in a novel\n(N), a familiar (F) and again the novel room (N'). The de novo learning sessions and the second group\nof rats behind Figure 1 are not in it.\n\n| Claim | Outcome |\n|---|---|\n| Cells per session (30.5 CA1, 37.4 PFC) | Reproduced |\n| PV similarity: CA1 remaps across rooms, PFC does not (Figure 2D) | Reproduced |\n| CA1 single-cell similarity across rooms is at shuffle level (Figure S3A) | Reproduced |\n| PFC single cells similar across rooms, CA1 lower (Figure S3A) | Partially reproduced |\n| PFC similarity grows with experience, CA1 does not (Figure S3C) | Reproduced |\n| PFC similarity to F rises over novel trials (Figure S3D) | Reproduced, on an assumption |\n| Reward wells no different from other locations (Figure S4D) | Reproduced |\n| Decoding: CA1 error higher in F and at chance (Figure 2E) | Partially reproduced |\n| Decoding: PFC error similar in N and F, above chance (Figure 2E) | Partially reproduced |\n| CA1 error rises at the switch, PFC stable (Figure 2F) | Reproduced, on an assumption |\n| Ramping cells are 16.4% (CA1) and 18.1% (PFC) of cell samples | Not reproduced |\n| Ramping cells generalize like other cells (Figure S4C) | Blocked: too few ramping cells |\n| Path equivalence stronger in PFC (Figure S5D) | Reproduced |\n| Path equivalence stable across rooms in PFC (Figure S5E) | Partially reproduced, on an assumption |\n| Path equivalence and selectivity uncorrelated (Figure S5F) | Blocked: methods underspecified |\n| Selectivity indices: PFC r = -0.5, CA1 r = 0.56 (Figure 3D) | Not reproduced, on an assumption |\n| Selectivity stable across rooms in PFC only (Figure 3E) | Not reproduced, on an assumption |\n| Pseudo-populations of 98 CA1 and 171 PFC cells | Reproduced |\n| Manifold shapes (Figure 3F, 3G) | Reproduced |\n| InSeq and OutSeq distances (Figure 3H) | Reproduced |\n| Phase and location distances (Figure 3I) | Reproduced |\n| F against N' manifolds: PFC preserved, CA1 at shuffle level (Figure 3J) | Partially reproduced |\n| The same in the neural space (Figure S6) | Partially reproduced |\n| PFC CCGP above shuffles for every decoder (Figure 4D) | Partially reproduced |\n| CA1 CCGP at chance (Figure 4D) | Not reproduced |\n| CCGP against the geometric random model (Figure S7B) | Not reproduced |\n| Most dichotomies decodable, similarly in both regions (Figure S7D) | Partially reproduced |\n| Performance higher in F than in N (Figure 1C, N-F-N' rats only) | Not reproduced |\n| Figure 1B, 1C sessions and S1B, which need the de novo sessions (four claims) | Blocked: data missing |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe dandiset has no linearized positions, ripple or theta times, or cell labels, and its units\ntable stores tetrode numbers where the format expects electrode rows. The attempt record, with the\nreasons and the differences from the paper's method, is\n[`attempts/000447-tang-2023-01.yaml`](../../attempts/000447-tang-2023-01.yaml).\n\n- `reproduce_tang_2023.ipynb`: the analysis. It takes about 20 minutes, most of it in the\n  permutation tests of the decoders.\n- `nfn.py`: loading the files, the linearization, rate maps, the decoder, selectivity, path\n  equivalence, ramping, single-trial maps and the CCGP decoders. Other notebooks on this dandiset\n  can import it.\n"
}
```

```
File created successfully at: entries/000447-tang-2023/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python concl.py && python build_nb.py x && cd  && date -u && python tools/entry.py all entries/000447-tang-2023 2>&1 | tail -3; date -u
```

```
28
103 cells
Fri Oct 30 04:19:36 UTC 2026
Installed kernelspec registry-000447-tang-2023 in executed/000447-tang-2023/.venv/share/jupyter/kernels/registry-000447-tang-2023
0 error(s)
pass  reproduce_tang_2023.ipynb  (1220 s)
Fri Oct 30 04:40:08 UTC 2026
```

**Agent**

Passed again (20 min). Confirming the outputs are identical to the previous run.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import nbformat
nb=nbformat.read('executed/000447-tang-2023/reproduce_tang_2023.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    out=''
    for o in c.get('outputs',[]):
        if o.output_type=='stream': out+=o.text
        elif o.output_type=='execute_result': out+=o.data.get('text/plain','')
        elif o.output_type=='error': out+='ERROR '+o.ename+' '+o.evalue
    print('=== cell',i,c.metadata.get('tags')); print(out[:6000])
" > off2_out.txt; diff <(grep -v " s)\| in [0-9]* s\|ran in" off_out.txt) <(grep -v " s)\| in [0-9]* s\|ran in" off2_out.txt) && echo IDENTICAL; grep "ran in" off2_out.txt
```

```
IDENTICAL
notebook ran in 20.2 min
Shell cwd was reset to
```

**Agent**

Outputs are identical across runs. Now the attempt record; checking the schema first.

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
print(json.dumps(s,indent=0)[:6000])"
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
[... 258 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
p=s['properties']
for k in p:
  if k not in ('dataset','provenance','outcomes','deprecated'): print(k, json.dumps(p[k])[:1500]); print()
print(json.dumps(p['outcomes']['items']['properties'].get('data'))[:500])
"
```

```
schema_version {"const": 2}

id {"type": "string", "pattern": "^[a-z0-9]+(-[a-z0-9]+)*$"}

paper {"type": "string", "pattern": "^doi:10\\.[0-9]{4,9}/.+$"}

date {"type": "string", "format": "date"}

entry {"description": "The entry this attempt produced (its name), if any.", "type": "string"}

verifications {"type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["date", "kind", "by", "results"], "properties": {"date": {"type": "string", "format": "date"}, "kind": {"enum": ["agent", "person", "paper_author"]}, "by": {"type": "string"}, "results": {"type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["claim", "agrees"], "properties": {"claim": {"type": "string"}, "agrees": {"type": "boolean"}, "reason": {"description": "The verifier's reason, in its own words.", "type": "string"}, "response": {"description": "What the author changed or replied, kept apart from the verifier's reason.", "type": "string"}, "outcome": {"description": "The outcome the verifier would give.", "enum": ["reproduced", "partially_reproduced", "not_reproduced", "blocked"]}}}}, "reviewed": {"description": "What was reviewed, e.g. a commit, when the attempt changed afterwards.", "type": "string"}}}}

findings {"description": "What the attempt found about the dataset itself, whatever the outcomes. These roll up into the per-dataset report.", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["kind", "statement"], "properties": {"kind": {"enum": ["metadata_error", "data_missing", "identifier_missing", "metadata_insufficient", "selection_undocumented", "methods_unavailable", "format_error", "code_mismatch", "paper_inconsistency", "other"]}, "statement": {"type": "string", "minLength": 1}, "found": {"description": "How the finding was found. Unset: by the attempt itself. `on_prompt`: by the reconcile step of a repeat attempt, which checked a finding of the earlier attempt that this one, made blin
[... 6 more lines not kept]
```

**Agent**

No outside inputs are needed. Writing the attempt record (generated with PyYAML so quoting is handled).

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/attempt.py",
 "content": "import yaml\n\nNB = \"reproduce_tang_2023.ipynb\"\nSMOOTH = (\"The 1D smoothing width of the linearized maps is garbled in the paper's text (Methods, \"\n          \"Spatial fields and linearization, \\\"s = σ cm\\\"). 8 cm is used, reading (a) of the claims file \"\n          \"(fig2d-pv-similarity), the σ given for the 2D maps in the sentence before; 4 and 2 cm are run as variants.\")\nLIN = (\"Linear positions are projections onto W-shaped paths built from the well positions and the run \"\n       \"positions (nfn.build_skeleton), as the Methods' \\\"pre-defined idealized paths along the track\\\" are not \"\n       \"in the dandiset (an assumption; paths are 180 to 220 cm, median 5 cm from the run positions).\")\nSWR = (\"Rate maps use run periods above 5 cm/s with occupancy above 20 ms (Methods, Spatial fields and \"\n       \"linearization), but SWR times are not excluded, as the dandiset holds no ripple times.\")\nCELLS = (\"Cells follow the Methods (at least 100 spikes) and the code (poolcells_acrossep.m, more than 100 spikes, \"\n         \"CA1 mean rate below 7 Hz); the code's per-animal interneuron lists cannot be applied, as the files carry \"\n         \"no cell numbers.\")\nUMAPDEV = (\"UMAP is umap-learn with seed 0 (seeds 1 and 2 as variants), not the MATLAB toolbox with the paper's \"\n           \"saved templates, which are not public (a standard choice named in the claims file).\")\nFILL = (\"Empty 1-cm bins inside a pass of the single-trial maps are filled linearly, as cal_PVsimilarity.m fills \"\n        \"session maps (an assumption; without it the PFC embedding splits by which animals' cells are all zero \"\n        \"at a bin, an artefact shown while preparing, not run here).\")\n\ndef o(claim, outcome, notes, deviations=None, blocked_by=None, assumed=None, measured=None, output=True):\n    d = {\"claim\": claim, \"outcome\": outcome}\n    if blocked_by:\n        d[\"blocked_by\"] = blocked_by\n    if output:\n        d[\"notebook\"] = NB\n        d[\"output\"] = f\"claim:{claim}\"\n    if measured is not None:\n        d[\"measured\"] = measured\n    if assumed is not None:\n        d[\"assumed\"] = assumed\n    d[\"notes\"] = \" \".join(notes.split())\n    if deviations:\n        d[\"deviations\"] = [\" \".join(x.split()) for x in deviations]\n    return d\n\nDENOVO = (\"The de novo learning sessions are not in the dandiset, which holds only the N-F-N' day (three \"\n          \"epochs per file, as its description says). The paper says its raw data are on Brandeis servers, \"\n          \"available on request (Data and code availability), so they are not public.\")\n\noutcomes = [\n    o(\"fig1b-faster-novel-learning\", \"blocked\", DENOVO + \" The novel sessions are present; the comparison needs the de novo curve.\",\n      blocked_by=\"data_missing\", output=False),\n    o(\"fig1-denovo-final-performance\", \"blocked\", DENOVO, blocked_by=\"data_missing\", output=False),\n    o(\"fig1c-session-performance\", \"blocked\", DENOVO + \" Session means for N, F and N' are in the notebook under fig1c-familiar-above-novel.\",\n      blocked_by=\"data_missing\", output=False),\n    o(\"fig1c-familiar-above-novel\", \"not_reproduced\",\n      \"\"\"On N, F and N' of the five rats the repeated-measures ANOVA gives F(2,8) = 1.08, p = 0.383, and Tukey's\n      test does not put F above N (mean state-space estimate 0.73 in F against 0.68 in N, difference 0.060,\n      p = 0.70). F is above N in four rats (by 0.078 to 0.222) and below it in ZT2 (by 0.282), whose F session has\n      24 trials at 0.50 correct. Each session estimated alone gives p = 0.46. The F-N-F'-N' rats of Figure S1C,\n      which the criterion tests only if their behaviour is in the dataset, are not.\"\"\",\n      deviations=[\"The ANOVA is over N, F and N' only; the de novo sessions of the paper's five-group ANOVA of Figure 1C are not in the dandiset, so Tukey's test uses the error term of a three-group ANOVA.\",\n                  \"The novel curve is estimated on N and N' together, as cal_behavperform.m runs the novel sessions together; the familiar curve on F alone, as the de novo days the code would include are missing. Background probability 1/3 (cal_behavperform.m).\"]),\n    o(\"figs1b-first-session-inbound-outbound\", \"blocked\", DENOVO, blocked_by=\"data_missing\", output=False),\n    o(\"cells-per-session\", \"reproduced\",\n      \"\"\"27.53 (SD 8.68) CA1 and 36.53 (SD 18.60) PFC cells per session per animal over the 15 animal-sessions,\n      within the stated 30.5 (SD 9.8) and 37.4 (SD 19.3). With at least 100 spikes (Methods) 27.67 and 36.53;\n      counting each cell once per animal 34.8 and 38.6. The region of a unit is read from its tetrode number\n      (see the findings).\"\"\",\n      measured=[27.53, 36.53], deviations=[CELLS]),\n    o(\"figs3a-ca1-global-remapping\", \"reproduced\",\n      \"\"\"CA1 spatial correlation, F-N' against the cell-ID shuffle, Tukey p = 0.075 (F-N' higher by 0.074; medians\n      -0.059 and -0.064). The result depends on the shuffle draw; over 100 draws p is below 0.05 in 13, and F-N' is\n      always higher (by 0.014 to 0.105). Rate overlap does not differ either (p = 0.55 and 0.30). JS17 keeps some\n      CA1 spatial correlation across rooms (median r 0.31; the other rats -0.11 to -0.05).\"\"\",\n      deviations=[SMOOTH, LIN, SWR,\n                  \"The shuffle pairs each cell's F map with another cell's N' map of the same animal (a random derangement within the animal); the Methods say \\\"a different cell\\\" without saying whether across animals. One draw decides the outcome; 100 draws are shown.\"]),\n    o(\"figs3a-pfc-similar-ca1-lower\", \"partially_reproduced\",\n      \"\"\"PFC F-N' does not differ from N-N' in rate overlap (reading a, map mean, p = 0.94; reading b, run rate,\n      p = 0.82) or spatial correlation (p = 0.52). CA1 F-N' is below N-N' in spatial correlation (difference 0.524,\n      p < 0.0001) but not in rate overlap (p = 0.32 and 0.45), so the CA1 part holds for one measure of two. The 4-cm\n      and 2-cm widths give the same pattern.\"\"\",\n      deviations=[SMOOTH, LIN, SWR]),\n    o(\"fig2d-pv-similarity\", \"reproduced\",\n      \"\"\"Per animal, CA1 PV similarity 0.419 to 0.652 (N-N') and -0.138 to 0.239 (F-N'); PFC 0.727 to 0.952 (N-N')\n      and 0.647 to 0.943 (F-N'). Repeated-measures ANOVA F(3,12) = 67.53, p = 8.8e-08 (the paper F = 83.24);\n      Tukey CA1 F-N' below N-N' by 0.473, p = 0.0001 (the paper p = 0.01); PFC p = 0.99 (the paper 0.41). The 4-cm\n      and 2-cm widths and the code's \\\"> 3 Hz\\\" rule agree, so the outcome does not rest on the width.\"\"\",\n      deviations=[SMOOTH, LIN, SWR, CELLS]),\n    o(\"fig2e-ca1-error-familiar\", \"partially_reproduced\",\n      \"\"\"CA1 error is higher in F than in N (median 230 against 172 cm; Dunn p = 1.8e-140 over the four groups,\n      p = 1.0e-139 for N and F alone), in every variant. In F the error is not below the shuffle but above it\n      (median 230 against 226 cm, mean paired difference 8.8 cm); the Wilcoxon test finds the difference under\n      shuffle reading (a), p = 2.4e-08, and (b), p = 0.042, so the claim of no difference fails by the paper's\n      test, though the statement's \\\"no better than chance\\\" holds in direction. With 4-cm smoothing reading (b)\n      gives p = 0.79; with 2 cm F is 3.5 cm below the shuffle (p = 0.0067). Errors are large because a decode onto\n      another trajectory counts as far, as the criterion asks; restricted to the current trajectory, CA1 errors\n      are 15 cm (N) and 57 cm (F).\"\"\",\n      deviations=[SMOOTH, LIN, SWR,\n                  \"Decoding windows of 200 ms every 150 ms (Methods, \\\"moving window with 50 ms overlap\\\"); the code's 50-ms step is a variant. The code's theta restriction cannot be applied (no theta times in the dandiset).\",\n                  \"Positions of N and F are put into N' coordinates by the ratio of trajectory lengths, as each epoch has its own linearization (an assumption).\",\n                  \"Dunn's test is Bonferroni-adjusted over all pairs, as GraphPad Prism (the paper's software) does; a rate floor of 1e-4 Hz keeps log rates finite (a standard choice).\"]),\n    o(\"fig2e-pfc-error-stable\", \"partially_reproduced\",\n      \"\"\"PFC error is below the shuffles in N (149 against 218 cm; Wilcoxon p = 1.3e-91 and 6.4e-67) and in F (186\n      against 223 cm; p = 7.8e-32 and 2.4e-35). It is not similar in N and F: F is higher (Dunn p = 7.0e-06 over four\n      groups, p = 3.9e-06 for N and F alone), in every variant (p 6.2e-05 to 1.4e-17). Four of five rats have the\n      higher median in F. With the decode restricted to the current trajectory, F is lower than N (23.5 against\n      28.5 cm), still different (p = 6.2e-05).\"\"\",\n      deviations=[SMOOTH, LIN, SWR, \"Decoder as in fig2e-ca1-error-familiar.\"]),\n    o(\"fig2f-switch-dynamics\", \"reproduced\",\n      \"\"\"Reading (a), trial -1 the last N trial, Methods decoder: CA1 error rises from 182 to 223 cm between trial -1\n      and trial 1 (Dunn p = 0.0021), PFC does not differ (149 and 200 cm, p = 0.12). Reading (b), the code's first\n      ten N trials: CA1 trial 1 is not above trial -1 (196 against 259 cm, p = 0.11), PFC p = 1. The code's decoder\n      (variant) finds no CA1 difference under either reading (p = 1). The readings disagree, so the outcome rests\n      on reading (a). Question for the paper's authors: which N trials are trials -10 to -1 in Figure 2F.\"\"\",\n      assumed=True,\n      deviations=[\"Assumption. Trial -1 is the last N trial (reading a). The legend's \\\"Trial-by-trial decoding error during environment switch (N to F)\\\" and the Results' \\\"the first trial after environment switching\\\" read so, and decoding_position_novelfamiliar_trial_batch.m means it (its comment says \\\"last 10 trials\\\" for the epoch before the switch) but its condition `ep == 1` never holds for epochs 2 and 4, so as written it takes the first ten.\",\n                  SMOOTH, LIN, SWR,\n                  \"Trials are rows of the dandiset's trials table; Kruskal-Wallis over trials -10 to 10 with Dunn's test Bonferroni-adjusted over all 190 pairs (GraphPad's default for all pairs).\"]),\n    o(\"figs3c-pfc-assimilation\", \"reproduced\",\n      \"\"\"Bins pooled over rats (8 cm): PFC F-N' 0.836 against F-N 0.774 (Tukey p < 0.0001); CA1 F-N 0.062 and F-N'\n      0.045 do not differ (p = 0.065; the paper p = 0.093); CA1 F-N' below N-N' 0.517 (p < 0.0001). PFC F-N' is below\n      N-N' by 0.019 (p = 0.0001; the paper p = 0.0013). The 4-cm and 2-cm widths agree (CA1 F-N against F-N'\n      p = 0.098 and 0.26).\"\"\",\n      deviations=[SMOOTH, LIN, SWR]),\n    o(\"figs3d-pfc-similarity-over-trials\", \"reproduced\",\n      \"\"\"PFC last trial above the first under every reading: N then N' 0.688 to 0.741 (Tukey p = 0.0018), N 0.684 to\n      0.757 (p < 0.0001), N' 0.738 to 0.782 (p = 0.0074). CA1 first and last do not differ under N then N' (0.053 and\n      0.048, p = 1.0) but CA1 falls under N (0.136 to 0.033, p = 0.0014; three rats, as JS34 and ZT2 have no N trial\n      with 80% of CA1 cells active) and under N' (0.114 to 0.002, p < 0.0001). The readings disagree for CA1, so\n      the outcome rests on reading (a). Question for the paper's authors: which novel trials Figure S3D shows,\n      how they are numbered across animals, and which is the last.\"\"\",\n      assumed=True,\n      deviations=[\"Assumption. The novel trials are those of N then N' (reading a), all passes in the novel environment, which the legend's \\\"over trials in the novel environment\\\" names without a session.\",\n                  \"Assumption. The kept passes (at least 80% of tuned cells active, legend) of each animal are ranked in order, ranks 1 to K enter the test, K being the smallest number of kept passes over the animals with any, and the last trial is rank K; the paper does not say how trials are numbered.\",\n                  SMOOTH, LIN, SWR]),\n    o(\"figs4-ramping-fraction\", \"not_reproduced\",\n      \"\"\"Ramping cell samples are 3.0% of CA1 (49 of 1652) and 3.1% of PFC (67 of 2192) over the three sessions\n      (reading a), and 3.7% (22 of 596) and 3.0% (22 of 728) in N' (reading b), against 16.4% (81 of 495) and 18.1%\n      (115 of 636). The 4-cm and 2-cm widths, and denominators of tuned samples only, give at most 7.6%. The N'\n      denominators are above the stated ones beyond tolerance; the tuned N' samples (291 and 484) are below them.\n      Measured values are reading (a).\"\"\",\n      measured=[3.0, 3.1, 1652, 2192],\n      deviations=[SMOOTH, LIN, SWR,\n                  \"The regression runs over the whole trajectory, as the claims file says; the Methods' \\\"over traversed positions to reward\\\" does not say which positions. Question for the paper's authors: which positions enter the regression and which cell samples form the denominator.\"]),\n    o(\"figs4-ramping-generalization\", \"blocked\",\n      \"\"\"Too few ramping cells under the claim's own rule. Ramping samples identified in N' are 4 to 7 per region\n      and trajectory over all animals, and only one animal-trajectory population per region has 3 or more, so\n      each ramping group is a single population of 101 bins. On it, CA1 ramping F-N' is below N-N' (Dunn\n      p = 1.7e-22), PFC ramping does not change (p = 0.34), and ramping and other cells differ only for CA1 F-N'\n      (p = 0.014; CA1 N-N' p = 1, PFC p = 1 and 0.11), which would make it partially reproduced. With the ramping\n      samples pooled over animals into one population per trajectory, the CA1 ramping drop is not found (p = 1)\n      and PFC ramping and other cells differ for F-N' (p = 0.016). The result rests on too few cells to decide,\n      and the ramping selection itself did not reproduce (figs4-ramping-fraction).\"\"\",\n      blocked_by=\"other\",\n      deviations=[\"A PV is computed only over at least 3 cells (an assumption; over 2 cells a correlation is always plus or minus 1).\", SMOOTH, LIN, SWR]),\n    o(\"figs4d-reward-location-similarity\", \"reproduced\",\n      \"\"\"Grubbs' test finds no outlier among the per-bin PV similarities, mean over rats, for F-N' and F-N in both\n      regions, over all 404 bins (p = 1 in all four) or per trajectory (smallest p 0.40). The values at the well\n      ends lie inside the range of the other bins (CA1 F-N' -0.100 to 0.224, PFC 0.723 to 0.901).\"\"\",\n      deviations=[SMOOTH, LIN, SWR, \"Grubbs' p-value is the usual Bonferroni bound on the largest studentized deviation (a standard choice).\"]),\n    o(\"figs5d-path-equivalence\", \"reproduced\",\n      \"\"\"PFC R exceeds CA1 R in every session (N, PFC minus CA1 0.173, Tukey p = 0.0002; F and N', p < 0.0001), ANOVA\n      F = 22.97 (the paper 25.37), p = 1.3e-21, over 99 CA1 and 171 PFC cells found in all three sessions. Medians\n      CA1 -0.009 to 0.169, PFC 0.304 to 0.405. The 4-cm and 2-cm widths agree (largest p 0.002).\"\"\",\n      deviations=[SMOOTH, LIN, SWR, CELLS]),\n    o(\"figs5e-path-equivalence-stable\", \"partially_reproduced\",\n      \"\"\"F against N' (first reading, 8 cm): PFC r = 0.572 (p = 3e-16), CA1 r = 0.231 (p = 0.021); Fisher's z = 3.24,\n      p = 0.0012, PFC above CA1. CA1 is within tolerance (0.189 to 0.231) and PFC 0.004 below it (0.576 to 0.704).\n      F against N: PFC 0.552, CA1 0.095 (z = 4.11). With 4-cm smoothing both values are within tolerance (0.613 and\n      0.201, p = 6.8e-05), which would make it reproduced; 2 cm gives 0.647 and 0.139 (partial). The outcome rests\n      on the 8-cm width.\"\"\",\n      measured=[0.572, 0.231], assumed=True,\n      deviations=[\"Assumption. \" + SMOOTH + \" The outcome changes with it.\", LIN, SWR]),\n    o(\"figs5f-path-equivalence-vs-selectivity\", \"blocked\",\n      \"\"\"With the signed SI no correlation of R with SI(IN) or SI(OUT) reaches p < 0.05 in either region (8 cm,\n      smallest p 0.26). With the absolute SI three of four do (CA1 SI(IN) r = -0.174, p = 0.025; PFC SI(IN)\n      r = -0.241, p = 5.2e-06; PFC SI(OUT) r = -0.208, p = 8.7e-05). The criterion makes the claim\n      methods_underspecified when only one reading finds a correlation. Question for the paper's authors: whether\n      Figure S5F plots the signed or the absolute selectivity index.\"\"\",\n      blocked_by=\"methods_underspecified\",\n      deviations=[SMOOTH, LIN, SWR]),\n    o(\"fig3d-selectivity-index\", \"not_reproduced\",\n      \"\"\"PFC r < 0 under every reading, within tolerance in N' (reading b, r = -0.466, p = 7.0e-08); pooled -0.335,\n      F -0.417. CA1 r > 0 but weaker than 0.56: pooled 0.284 (p = 0.00021), N' 0.280 (p = 0.040), F 0.127 (p = 0.41).\n      No reading puts both in tolerance, and reading (c) is not significant for CA1, so the partial clause fails.\n      With 2-cm smoothing CA1 F is significant (r = 0.336, p = 0.0062), which would make it partially\n      reproduced. Per animal in N', CA1 r runs from -0.40 (JS17, 7 cells) to 0.89 (JS21, 8 cells). Measured values\n      are reading (a).\"\"\",\n      measured=[-0.335, 0.284], assumed=True,\n      deviations=[\"Assumption. \" + SMOOTH + \" The outcome changes with it.\", LIN, SWR,\n                  \"The code's \\\"> 3 Hz\\\" rule is a variant; it selects the same samples here.\"]),\n    o(\"fig3e-selectivity-stable\", \"not_reproduced\",\n      \"\"\"F against N' (8 cm): PFC r = 0.437 (p = 5.2e-11, 0.004 below the tolerance), CA1 r = 0.318 (p = 0.012). F\n      against N: PFC 0.363, CA1 0.384 (p = 0.00086). The CA1 correlation is significant under both readings, so the\n      claim fails. With 2-cm smoothing F against N' gives CA1 r = 0.128 (p = 0.20) and PFC 0.406, which would make it\n      partially reproduced. Measured values are reading N'.\"\"\",\n      measured=[0.437, 0.318], assumed=True,\n      deviations=[\"Assumption. \" + SMOOTH + \" The outcome changes with it.\", LIN, SWR]),\n    o(\"manifold-cell-counts\", \"reproduced\",\n      \"\"\"Reading (b), the code's (units included in N, F and N'), gives 99 CA1 and 171 PFC cells against 98 and 171.\n      Reading (a), the Methods' (also a peak of at least 3 Hz in a session), gives 95 and 151, PFC below tolerance.\n      Reading (b) is used for the manifolds. That the counts match supports the reading of units/electrodes as\n      tetrode numbers.\"\"\",\n      measured=[99, 171], deviations=[CELLS, SMOOTH]),\n    o(\"fig3fg-manifold-shapes\", \"reproduced\",\n      \"\"\"The criterion takes the outcome from fig3h-inseq-outseq-distance and fig3i-phase-location-distance, both\n      reproduced. The embeddings and the mean state per trajectory are shown; no measure of a ring or a double V\n      is computed, and the embeddings do not show a clean ring.\"\"\",\n      deviations=[UMAPDEV, FILL, LIN,\n                  \"Passes per trajectory are the smallest number over the animals from the first (Methods): 5, 6, 8 and 6 in N'. Maps at 1-cm bins (Methods) on 201 normalized bins (cal_UMAP.m).\"]),\n    o(\"fig3h-inseq-outseq-distance\", \"reproduced\",\n      \"\"\"Seed 0: CA1 (by location) OutSeq 13.83 against InSeq 17.08, rank-sum p = 0.00067; PFC (by phase) InSeq 14.72\n      against OutSeq 16.83, p = 0.015. Every alignment and seed keeps both directions, but p varies with the seed\n      (seed 1 CA1 p = 0.096; seed 2 CA1 p = 0.0041, PFC p = 0.004), and PFC aligned by location gives p = 0.081\n      (seed 0).\"\"\",\n      deviations=[UMAPDEV, FILL, LIN]),\n    o(\"fig3i-phase-location-distance\", \"reproduced\",\n      \"\"\"Methods reading, seed 0: PFC same-phase 14.52 against same-location 16.91 (p = 4.7e-181); CA1 location 13.84\n      against phase 17.98 (p near 0). Seeds 1 and 2 agree. The code's variant (both from same-side pairs) agrees for\n      PFC under every seed and for CA1 under seeds 0 and 1 (seed 2 reverses, p = 0.35).\"\"\",\n      deviations=[UMAPDEV, FILL, LIN]),\n    o(\"fig3j-familiar-novel-manifold\", \"partially_reproduced\",\n      \"\"\"PFC F states lie closer to N' states than the shuffle (11.70 against 14.56, 19.6% closer, rank-sum\n      p = 8.6e-241). CA1 F states are also closer than the shuffle, by less (13.65 against 13.97, 2.3% closer,\n      p = 1.5e-25), so the claim that CA1 does not differ from the shuffle fails by the paper's test; seeds 1 and 2\n      give CA1 3.3% to 6.0% and PFC 16.2% to 24.8% closer.\"\"\",\n      deviations=[UMAPDEV, FILL, LIN]),\n    o(\"figs6-high-dimensional-distances\", \"partially_reproduced\",\n      \"\"\"In the neural space 3H holds (CA1 OutSeq 45.04 against InSeq 52.15, p = 2.5e-12; PFC InSeq 64.27 against\n      OutSeq 70.61, p = 4.8e-12) and 3I holds (PFC phase 65.47 against location 86.09; CA1 location 45.02 against\n      phase 48.37, p = 9.3e-129). In 3J PFC F-N' is 56.6% below the shuffle, but CA1 is also below it (9.2%,\n      p = 7.5e-78), so two of the three relationships hold.\"\"\",\n      deviations=[FILL, LIN, SMOOTH]),\n    o(\"fig4d-pfc-ccgp\", \"partially_reproduced\",\n      \"\"\"Nine of the 16 PFC decoders have p < 0.001 and 12 have p < 0.05. The task-sequence decoders are high (0.75 to\n      0.80; one at 0.50, p = 0 under the code's count of shuffles strictly above, 1 counting ties), the\n      environment task-sequence decoders 0.587 and 0.888, but the trajectory-phase decoder tested on OUT_L is 0.230\n      and three of the four environment phase decoders are 0.385 to 0.512 (p 0.27 to 1). The effect holds for\n      the task sequence and in part for phase and environment.\"\"\",\n      deviations=[UMAPDEV, FILL,\n                  \"The task-sequence decoders follow CCGP_taskSeq.m, whose test pairs take the two clusters at different segments (20-30% for one trajectory, 70-80% for the other); taking them at the same segment is a variant and gives the same counts.\",\n                  \"Linear C-SVM through scikit-learn's libsvm (C = 1), balanced accuracy, 1,000 label shuffles (decoding_CCGP_linearSVM_simple.m).\"]),\n    o(\"fig4d-ca1-ccgp-chance\", \"not_reproduced\",\n      \"\"\"The four CA1 trajectory-phase decoders are at or below chance (0.417 to 0.500, smallest p 0.119), but 6 of\n      the 16 CA1 decoders have p < 0.05: the task-sequence decoder tested on the inbound pair at 20-30% (0.596), two\n      environment phase decoders (0.582 and 0.562), the two environment task-sequence decoders held out on the\n      inbound pair (0.642 each), and one decoder at 0.500 with p = 0 under the code's strict count (1 counting\n      ties). Two other task-sequence decoders are far below chance (0.100 and 0.035).\"\"\",\n      deviations=[UMAPDEV, FILL, \"Decoders as in fig4d-pfc-ccgp.\"]),\n    o(\"figs7b-geometric-null\", \"not_reproduced\",\n      \"\"\"No PFC variable's CCGP (the mean of its decoders: phase 0.534, sequence 0.713, environment 0.618) exceeds\n      the 95th percentile of its null under reading (a), permuted UMAP coordinates (p 0.29 to 0.86), or reading\n      (b), permuted neuron axes embedded with the N' fit (p 0.23 to 0.65). No CA1 variable does either (p 0.57 to\n      1.00). The PFC part fails; the CA1 part holds.\"\"\",\n      deviations=[\"Assumption. The CCGP of a variable is the mean over its decoders, compared with the same mean under the null; the legend plots each decoder with the median. Both readings of the space (claims file) are run; the code for the model is not public.\",\n                  UMAPDEV, FILL]),\n    o(\"figs7d-dichotomies-decodable\", \"partially_reproduced\",\n      \"\"\"Most dichotomies are decoded above their shuffles: CA1 35 of 35 (median accuracy 0.831), PFC 33 of 35 (median\n      0.660). The accuracies differ by the paper's test, CA1 above PFC (rank-sum p = 5.7e-08, median difference\n      0.171), so the similarity part fails.\"\"\",\n      deviations=[\"The label-permutation test uses 100 shuffles per dichotomy in place of the paper's 1,000, for time (1,000 would take about 45 minutes per region here, estimated from timing 20 shuffles); p is resolved to 0.01, enough to decide p < 0.05.\",\n                  UMAPDEV, FILL,\n                  \"Accuracy is the fraction correct over the 4 folds, as libsvm's -v 4 reports; folds are stratified by class (scikit-learn).\"]),\n]\n\nfindings = [\n    {\"kind\": \"format_error\", \"statement\": \"The units table's `electrodes` column holds tetrode numbers, not row indices of the electrodes table as the NWB format requires: its values run up to 64 in ZT2, whose table has 128 rows (two per tetrode), and up to 30 to 32 in the others. Read as row indices, up to 32 units per animal are put in the wrong region; read as tetrode numbers, the counts match the paper's (98 CA1 and 171 PFC cells against 99 and 171 here).\"},\n    {\"kind\": \"metadata_insufficient\", \"statement\": \"Units carry no cell number within a tetrode, no waveform and no putative-interneuron label, so the paper's interneuron exclusion (spike width and rate in the Methods, per-animal (tetrode, cell) lists in its code) cannot be applied. Units clustered only in later epochs are appended to the table with no spike in N (1 to 19 per animal), without a note.\"},\n    {\"kind\": \"other\", \"statement\": \"In every file `acquisition/ElectricalSeries` is a byte-identical second copy of the 1.5 kHz LFP in `processing/ecephys/LFP`, stored at a different offset; there is no 30 kHz spike-band recording, and the copy roughly doubles the file sizes.\"},\n    {\"kind\": \"metadata_error\", \"statement\": \"The position's reference frame is given as \\\"center well\\\", but positions are camera coordinates in which the center well lies at different places in each epoch (for example AM2 (32, 52) cm in N and (73, 86) cm in F). The five files' session start times fall within 16 minutes on 2023-03-14, two days before the first published version, which is the time of conversion, not of recording.\"},\n    {\"kind\": \"metadata_insufficient\", \"statement\": \"The files hold no linearized positions, idealized track paths or trajectory labels per position sample, no sharp-wave ripple or theta times, and the epochs carry no names (N, F and N' are known only from the dandiset description's order). The paper's rate maps, decoding and manifolds use all of these; here linear positions had to be rebuilt from the 2D positions and ripple times could not be excluded.\"},\n    {\"kind\": \"metadata_error\", \"statement\": \"In AM2 the electrode groups Tetrode26 to Tetrode31 carry the labels tetrode27 to tetrode32, so group names and labels disagree; electrode descriptions are placeholders (\\\"my description\\\", \\\"no description\\\").\"},\n    {\"kind\": \"data_missing\", \"statement\": \"The de novo learning sessions of the five rats and the behaviour of the three F-N-F'-N' rats (Figures 1B, 1C, S1B, S1C) are not in the dandiset; four claims are blocked and one is tested on the N-F-N' day only.\"},\n    {\"kind\": \"code_mismatch\", \"statement\": \"decoding_position_novelfamiliar_trial_batch.m (Figure 2F) takes the last ten trials of the pre-switch epoch only `if ep == 1`, but runs on epochs 2 and 4, so it always takes the first ten N trials, against its own comment (\\\"last 10 trials\\\") and the legend's switch from N to F. With the last N trials CA1 error rises at the switch (Dunn p = 0.0021); with the first ten it does not (p = 0.11).\"},\n    {\"kind\": \"methods_unavailable\", \"statement\": \"Question for the authors. What is the width of the 1D Gaussian that smooths the linearized rate maps? The text reads \\\"s = σ cm\\\". 8 cm (the 2D width) was assumed; figs5e, fig3d and fig3e change outcome between 8, 4 and 2 cm.\"},\n    {\"kind\": \"methods_unavailable\", \"statement\": \"Question for the authors. How were the idealized paths for linearization defined, and are the linearized positions available? They are not in the dandiset; here W-shaped paths were built from the well and run positions.\"},\n    {\"kind\": \"methods_unavailable\", \"statement\": \"Question for the authors. In Figure 2F, are trials -10 to -1 the last ten N trials (as the legend and the code's comment suggest) or the first ten (as the code runs)? The CA1 result depends on it.\"},\n    {\"kind\": \"methods_unavailable\", \"statement\": \"Question for the authors. In Figure S3D, which novel trials are shown (N, N' or both), how are trials numbered across animals with different numbers of passes, and which is the last trial? CA1 similarity falls over trials of N or of N' alone but not over N then N'.\"},\n    {\"kind\": \"methods_unavailable\", \"statement\": \"Question for the authors. Does Figure S5F use the signed or the absolute selectivity index? Path equivalence is uncorrelated with the signed SI but negatively correlated with its absolute value in PFC (p < 0.0001).\"},\n    {\"kind\": \"methods_unavailable\", \"statement\": \"Question for the authors. For the ramping cells of Figure S4, which positions enter the regression and which cell samples form the denominator (495 and 636)? The rule as written gives 3 to 8% of cell samples here, against 16.4 and 18.1%.\"},\n    {\"kind\": \"methods_unavailable\", \"statement\": \"Question for the authors. For the geometric random model of Figure S7, in which space are the axes permuted (the 3 UMAP coordinates or the neurons), and what happens to the cluster centres (the legend says rotation-translation)? Its code is not in the repository.\"},\n]\n\nrec = {\n    \"schema_version\": 2,\n    \"id\": \"000447-tang-2023-01\",\n    \"dataset\": {\"archive\": \"dandi\", \"id\": \"000447\", \"version\": \"0.250724.2224\", \"doi\": \"10.48324/dandi.000447/0.250724.2224\"},\n    \"paper\": \"doi:10.1016/j.celrep.2023.112246\",\n    \"date\": \"2026-10-30\",\n    \"entry\": \"000447-tang-2023\",\n    \"provenance\": {\"kind\": \"agent\", \"accountable\": {\"name\": \"CatalystNeuro\"},\n                   \"agent\": {\"harness\": \"Claude Code\", \"model\": \"claude-opus-5-5\", \"protocol\": \"pilot-12\"},\n                   \"runner\": {\"platform\": \"GitHub Actions\", \"url\": \"https://github.com/catalystneuro/encore/actions/runs/40994732733\"}},\n    \"outcomes\": outcomes,\n    \"findings\": findings,\n}\n\nclass D(yaml.SafeDumper):\n    pass\ndef str_rep(dumper, data):\n    return dumper.represent_scalar(\"tag:yaml.org,2002:str\", data)\nD.add_representer(str, str_rep)\nopen(\"attempts/000447-tang-2023-01.yaml\", \"w\").write(\n    yaml.dump(rec, Dumper=D, sort_keys=False, allow_unicode=True, width=100, default_flow_style=False))\nprint(len(outcomes))\n"
}
```

```
File created successfully at: /tmp/claude-1001/attempt.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='attempt.py'; s=open(p).read()
s=s.replace("""test does not put F above N (mean state-space estimate 0.73 in F against 0.68 in N, difference 0.060,
      p = 0.70).""","""test does not put F above N (difference of the means 0.060, p = 0.70).""")
s=s.replace("taking them at the same segment is a variant and gives the same counts.","taking them at the same segment is a variant and gives CCGP within 0.003 of these.")
open(p,'w').write(s)
EOF
python attempt.py && cd  && grep -n ": " attempts/000447-tang-2023-01.yaml | grep -v "^[0-9]*: *[a-z_-]*: \|^[0-9]*: *- [a-z_]*: " | head; python tools/entry.py check entries/000447-tang-2023 2>&1 | tail -5
```

```
32
170:    and in F (186 against 223 cm; p = 7.8e-32 and 2.4e-35). It is not similar in N and F: F is higher
191:    (b), the code''s first ten N trials: CA1 trial 1 is not above trial -1 (196 against 259 cm, p = 0.11),
193:    readings disagree, so the outcome rests on reading (a). Question for the paper''s authors: which N
277:    positions to reward" does not say which positions. Question for the paper''s authors: which positions
351:    it (0.576 to 0.704). F against N: PFC 0.552, CA1 0.095 (z = 4.11). With 4-cm smoothing both values
392:    pooled -0.335, F -0.417. CA1 r > 0 but weaker than 0.56: pooled 0.284 (p = 0.00021), N'' 0.280 (p
417:    (p = 0.012). F against N: PFC 0.363, CA1 0.384 (p = 0.00086). The CA1 correlation is significant under
464:  - 'Passes per trajectory are the smallest number over the animals from the first (Methods): 5, 6, 8
559:    but 6 of the 16 CA1 decoders have p < 0.05: the task-sequence decoder tested on the inbound pair at
609:    table as the NWB format requires: its values run up to 64 in ZT2, whose table has 128 rows (two per
0 error(s)
```

**Agent**

Some prose contains ": " (PyYAML quotes those, so they parse, but the instructions ask to avoid them). Rewording.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='attempt.py'; s=open(p).read()
s=s.replace('def o(claim, outcome, notes, deviations=None, blocked_by=None, assumed=None, measured=None, output=True):\n    d = {',
 'def fix(t):\n    t = " ".join(t.split())\n    t = t.replace("authors: ", "authors, ").replace(": ", ", ")\n    return t\n\ndef o(claim, outcome, notes, deviations=None, blocked_by=None, assumed=None, measured=None, output=True):\n    d = {')
s=s.replace('d["notes"] = " ".join(notes.split())','d["notes"] = fix(notes)')
s=s.replace('d["deviations"] = [" ".join(x.split()) for x in deviations]','d["deviations"] = [fix(x) for x in deviations]')
s=s.replace('rec = {\n','for f in findings:\n    f["statement"] = fix(f["statement"])\n\nrec = {\n')
open(p,'w').write(s)
EOF
python attempt.py && cd  && python -c "
import yaml,re
t=open('attempts/000447-tang-2023-01.yaml').read()
d=yaml.safe_load(t)
bad=[s for o in d['outcomes'] for s in [o.get('notes','')]+o.get('deviations',[]) if ': ' in s]+[f['statement'] for f in d['findings'] if ': ' in f['statement']]
print('strings with colon-space:',len(bad))
print('em dashes:', '—' in t, 'rather:', 'rather' in t.lower())
" ; grep -n "^    and in F\|N and F, F is\|Methods), 5" attempts/000447-tang-2023-01.yaml | head; python tools/entry.py check entries/000447-tang-2023 2>&1 | tail -2
```

```
32
strings with colon-space: 0
em dashes: False rather: False
170:    in F (186 against 223 cm; p = 7.8e-32 and 2.4e-35). It is not similar in N and F, F is higher (Dunn
464:  - Passes per trajectory are the smallest number over the animals from the first (Methods), 5, 6, 8 and
0 error(s)
```

**Agent**

Checking the notebook text and the other files for bold, em dashes and "rather".

**Agent calls Bash**

```bash
cd $TMPDIR && grep -n "\*\*" header.md summary.md | head; grep -n -i "rather\|—" header.md summary.md concl.py build_nb.py entries/000447-tang-2023/nfn.py entries/000447-tang-2023/README.md | head
```

```
header.md:3:**Paper.** Tang W, Shin JD, Jadhav SP (2023). Geometric transformation of cognitive maps for
header.md:12:**Dataset.** [DANDI:000447](https://dandiarchive.org/dandiset/000447/0.250724.2224), version
header.md:19:**What the dandiset holds.** One file per rat (AM2, JS17, JS21, ZT2, JS34) for the N-F-N' day: three
header.md:25:**Outside inputs.** None. The paper's code is read for method details only.
summary.md:41:**How the analysis differs from the paper's.**
summary.md:60:**What was found about the dataset.**
Shell cwd was reset to
```

**Agent**

Removing the bold from the header and summary, then rebuilding and re-running so the executed copy matches the committed notebook.

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i 's/^\*\*Paper\.\*\* /Paper. /; s/^\*\*Dataset\.\*\* /Dataset. /; s/^\*\*What the dandiset holds\.\*\* /What the dandiset holds. /; s/^\*\*Outside inputs\.\*\* /Outside inputs. /' header.md && sed -i 's/^\*\*How the analysis differs from the paper.s\.\*\*/### How the analysis differs from the paper'"'"'s/; s/^\*\*What was found about the dataset\.\*\*/### What was found about the dataset/' summary.md && grep -c "\*\*" header.md summary.md; grep -n "^###" summary.md; . dev/bin/activate && python build_nb.py x && cd  && date -u && python tools/entry.py all entries/000447-tang-2023 2>&1 | tail -2; date -u
```

```
header.md:0
summary.md:0
41:### How the analysis differs from the paper's
60:### What was found about the dataset
103 cells
Fri Oct 30 04:42:55 UTC 2026
0 error(s)
pass  reproduce_tang_2023.ipynb  (1229 s)
Fri Oct 30 05:03:36 UTC 2026
```

**Agent**

Passed (20.5 min). Confirming outputs are unchanged, and looking at the untracked dotfiles that appeared at the repository root.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import nbformat
nb=nbformat.read('executed/000447-tang-2023/reproduce_tang_2023.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    out=''
    for o in c.get('outputs',[]):
        if o.output_type=='stream': out+=o.text
        elif o.output_type=='execute_result': out+=o.data.get('text/plain','')
        elif o.output_type=='error': out+='ERROR '+o.ename+' '+o.evalue
    print('=== cell',i,c.metadata.get('tags')); print(out[:6000])
" > off3_out.txt; diff <(grep -v " s)\| in [0-9]* s\|ran in" off_out.txt) <(grep -v " s)\| in [0-9]* s\|ran in" off3_out.txt) && echo IDENTICAL; cd  && git status --short && ls -la .bash_profile .bashrc .gitconfig .profile .zshrc scripts .idea .vscode .mcp.json .ripgreprc .zprofile 2>&1 | head -20
```

```
IDENTICAL
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
?? attempts/000447-tang-2023-01.yaml
?? entries/000447-tang-2023/
?? scripts
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 30 02:50 .bash_profile
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 30 02:50 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 30 02:50 .gitconfig
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 30 02:50 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 30 02:50 .mcp.json
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 30 02:50 .profile
[... 5 more lines not kept]
```

**Agent**

Those are the sandbox's `/dev/null` mounts from 02:50, before this run, not files of mine. Building the verifier's handover.

**Agent calls Bash**

```bash
python tools/entry.py handover entries/000447-tang-2023 2>&1 | tail -3; ls executed/000447-tang-2023/handover/; python -c "
import nbformat
nb=nbformat.read('executed/000447-tang-2023/handover/reproduce_tang_2023.ipynb',4)
print(len(nb.cells), any(c.source.lstrip().startswith('**Result') for c in nb.cells), any('## Summary' in c.source for c in nb.cells))"; python tools/entry.py check entries/000447-tang-2023 | tail -1; date -u
```

```
wrote executed/000447-tang-2023/handover
10.1016-j.celrep.2023.112246.yaml
nfn.py
reproduce_tang_2023.ipynb
74 False False
0 error(s)
Fri Oct 30 05:04:02 UTC 2026
```

**Agent**

I did steps 1 to 6 of the Author section. The entry is in `entries/000447-tang-2023/` and the record is `attempts/000447-tang-2023-01.yaml`. `tools/entry.py all` passes with 0 check errors. The notebook runs in about 20 minutes and gives identical outputs on three clean runs. The handover is in `executed/000447-tang-2023/handover/`. Nothing is committed.

## 1. Outcomes (32 claims)

| Claim | Outcome |
|---|---|
| cells-per-session | reproduced (27.5 CA1 and 36.5 PFC cells, against 30.5 and 37.4) |
| fig2d-pv-similarity | reproduced at all three smoothing widths |
| figs3a-ca1-global-remapping | reproduced (p = 0.075; p < 0.05 in 13 of 100 shuffle draws) |
| figs3c, figs4d, figs5d | reproduced |
| fig2f-switch-dynamics | reproduced, resting on an assumption (trial -1 is the last N trial) |
| figs3d-pfc-similarity-over-trials | reproduced, resting on an assumption (trials of N then N') |
| manifold-cell-counts | reproduced (99 and 171 cells, against 98 and 171) |
| fig3fg, fig3h, fig3i | reproduced (UMAP p-values vary with the seed) |
| figs3a-pfc-similar-ca1-lower | partial (CA1 rate overlap does not drop) |
| fig2e-ca1-error-familiar, fig2e-pfc-error-stable | partial (the "no difference" parts fail the paper's tests) |
| figs5e-path-equivalence-stable | partial, resting on the 8-cm smoothing (4 cm would reproduce it) |
| fig3j, figs6 | partial (CA1 F states are also closer than the shuffle) |
| fig4d-pfc-ccgp | partial (9 of 16 decoders at p < 0.001) |
| figs7d-dichotomies-decodable | partial (most decodable, but CA1 accuracy is higher) |
| fig1c-familiar-above-novel | not reproduced (Tukey F vs N p = 0.70; N-F-N' rats only) |
| figs4-ramping-fraction | not reproduced (3 to 4% ramping, against 16 to 18%) |
| fig3d, fig3e | not reproduced, resting on the 8-cm smoothing |
| fig4d-ca1-ccgp-chance, figs7b-geometric-null | not reproduced |
| fig1b, fig1-denovo-final, fig1c-session, figs1b | blocked, data_missing (no de novo sessions) |
| figs4-ramping-generalization | blocked, other (only one population of at least 3 ramping cells per region) |
| figs5f-path-equivalence-vs-selectivity | blocked, methods_underspecified (the criterion's own rule: signed and absolute SI disagree) |

## 2. What was found about the dataset

- **Unit regions:** the units table stores tetrode numbers where NWB expects electrode-table row indices (a format error). Read as tetrode numbers, the regions match the paper's counts; read as rows, up to 32 units per animal land in the wrong region.
- **Missing unit information:** there are no cell numbers, waveforms or interneuron labels, so the paper's interneuron lists cannot be applied. Units clustered only in later epochs are appended to the table without a note.
- **Duplicate LFP:** `acquisition/ElectricalSeries` is a byte-identical second copy of the 1.5 kHz LFP; there is no 30 kHz recording.
- **Other metadata:**
  - The position reference frame says "center well", but the positions are camera coordinates.
  - The session start times are the conversion time.
  - The epochs carry no names.
  - The files hold no linearized positions, ripple times or theta times.
  - The AM2 electrode labels and group names disagree.
- **Missing data:** the de novo sessions and the F-N-F'-N' rats are not in the dandiset.
- **Paper's code:** the Figure 2F batch script's `if ep == 1` never fires on epochs 2 and 4, so it takes the first ten N trials, against its own comment "last 10 trials".
- **Version:** I pinned 0.250724.2224, the latest. The paper cites no version, and 0.230316.2133 holds the same data arrays.

**Assumptions:**
- Linearization onto W-shaped paths built from the well and run positions.
- 8-cm 1D smoothing (the width is garbled in the text).
- Trial -1 is the last N trial; for S3D, trials of N then N'.
- Empty 1-cm bins in single-trial maps are filled linearly. Without this, the PFC embedding split into clusters by which animals' cells were all zero.
- A population vector needs at least 3 cells.
- For the geometric null, a variable's CCGP is the mean over its decoders.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings): the smoothing width, the idealized track paths, the Figure 2F trials, the Figure S3D trial numbering, signed or absolute SI in Figure S5F, the ramping regression and its denominators, and the space of the geometric null model.

**Questions to a reader:** none.

## 3. Where the protocol was unclear

1. Several criteria have no partial clause, yet one part of the claim holds (fig2e, fig3j, fig4d-pfc, figs7d). I used `partially_reproduced` and said which part fails.
2. The open smoothing width affects many claims, but only fig2d's criterion says what to do when the widths disagree. For the others I adopted 8 cm with `assumed: true` and showed 4 and 2 cm.
3. Blocking for "too few units" when the minimum is my own assumption (figs4-ramping-generalization) is not covered. I blocked it as `other` and gave every result in the notes.
4. Protocol step 1.6 says to adopt the best-supported reading, but the figs5f criterion itself prescribes `methods_underspecified`. I followed the criterion.
5. The ten-minute runtime aim does not fit 1,000-shuffle SVM permutation tests. The notebook takes 20 minutes, and I cut the dichotomy shuffles to 100, recorded as a deviation.
6. The two published versions hold identical data arrays; I checked this while preparing and the header says it was not re-run in the notebook.
7. The sandbox's `/dev/null` mounts show up as untracked dotfiles at the repository root. I left them alone; the workflow should not commit them.

## 4. Runtime and failures

The run took about 2 h 05 min (02:59 to 05:04 UTC); each notebook run takes about 20 minutes. Nothing failed in the final runs. During development:
- The first median-path linearization gave 200 to 390 cm tracks, so I replaced it with the W skeleton.
- The first single-trial embeddings were artefacts of empty bins; fixed by the gap filling above.
- One shell append wrote a stray `nfn.py` at the repository root; I moved it into the helper and deleted it.

## End of run

111 turns, 123 minutes, result: success.
