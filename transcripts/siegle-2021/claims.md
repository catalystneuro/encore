# 000253 · claims · run 39991577721

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ claims/000253/ paper/ 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  awk '/^## Reader/,/^## Author/' docs/protocol.md; ls claims/001453/ claims/000253/ paper/ 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  cat claims/001453/*.yaml; wc -c paper/*.txt; head -40 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  head -c 9000 claims/001453/*.yaml | tail -c 7000; echo ----; grep -n "^- id:\|^  [a-z_]*:" claims/001453/*.yaml | awk -F: '{print $3}' | sort | uniq -c; echo; wc -c paper/*.txt; head -20 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  wc -c paper/*.txt; head -30 paper/*.txt; grep -n "expected:" -A6 claims/001453/*.yaml | head -40; grep -n "deviation\|open\b" claims/001453/*.yaml | head
```

Result: not kept, because it reads the paper's text.

**Agent**

The paper text is present (PMC author manuscript, 156 KB). Reading it now.

**Agent calls Bash**

```bash
cd  fold -s -w 200 paper/*.txt > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt; echo $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n '1,200p' claims/001453/*.yaml | sed -n '30,200p'
```

```
paper: doi:10.1016/j.cub.2025.04.027
claims:
- id: stimulus-code-link
  kind: link
  statement: The dandiset's stimulus codes can be linked to the stimuli the paper names, using
    the paper's analysis code and the protocol file of its stimulus software, and the values
    computed through that link agree with those the paper's code printed.
  source: Data and Code Availability; the paper's Fig1-S1.ipynb at GitLab commit 33a5c29
  data: with_labels
  criterion: Records are matched by the integer stimulus code. The link holds (reproduced) when
    every code the analysis uses (0 to 7, 9, 10, 11, 13 and 20) occurs in the dandiset, and the
    species' median speeds for the nine whole-field stimuli computed here are within 10% of the
    values printed in Fig1-S1.ipynb for at least 14 of the 18 species and stimulus pairs. It is
    partially reproduced for 9 to 13 pairs and not reproduced below 9. The fish cannot be
    matched one to one, as no identifier links the dandiset's subjects to the code's folders;
    the counts per species are compared instead. The sign of the zebrafish turning response
    to codes 9 and 11 is reported, as the code and the protocol file disagree on which of them
    is lateral right.
- id: fig1d-dc-faster-all-codes
  statement: Danionella cerebrum (DC) swim at a higher median velocity than zebrafish (ZF)
[... 151 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "inferred\|^checks\|kind:\|data: elsewhere\|variant\|open" claims/001453/*.yaml | head -30; tail -30 claims/001453/*.yaml; sed -n '1,80p' tools/claims_check.py
```

```
3:# from its Results, figure legends and STAR Methods. The version of record is not open access.
33:  kind: link
181:    variant, as is a test on per-fish medians.
197:    protocol file's assignment of 9 and 11 is shown as a variant.
    n: 4 ZF fish, 1887 swims
  - about: tail angle, ZF against DC, turn-inducing stimuli
    test: two-way ANOVA, Tukey post hoc
    p: 0.05
    p_relation: "<"
- id: fig4f-longer-on-duration
  statement: Swim-onset-associated neurons in DC have a longer active (ON) phase than in ZF,
    while non-motor-associated neurons have similar ON durations.
  source: Figure 4E and 4F
  quote: While the active, above baseline, ‘ON’ duration of neural activity for non-motor associated
    neurons is similar in ZF and DC, swim start-associated neurons in DC show a significantly longer
    activity phase than ZF
  statistics:
  - test: two-way ANOVA, Tukey post-hoc
    p: 0.05
    p_relation: "<"
[... 94 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"
```

```
{
 "$schema": "https://json-schema.org/draft/2020-12/schema",
 "title": "Claims proposed for one target (a dataset and one of its papers)",
 "description": "Draft. To be revised after the pilot.",
 "type": "object",
 "additionalProperties": false,
 "required": [
  "schema_version",
  "dataset",
  "paper",
  "claims"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "dataset": {
   "description": "The dataset the claims are tested on: the archive and the dataset's identifier there.",
   "type": "object",
   "additionalProperties": false,
[... 185 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1))"
```

```
{
 "expected": {
  "type": "object",
  "additionalProperties": false,
  "required": [
   "quantity",
   "value"
  ],
  "properties": {
   "quantity": {
    "type": "string"
   },
   "value": {
    "type": "number"
   },
   "tolerance": {
    "type": "number",
    "minimum": 0
   },
   "unit": {
[... 82 more lines not kept]
```

**Agent**

Now the paper.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 7,
 "limit": 250
}
```

```
7	pmc Nature Nature 319 nihpa 0410462 Nature 0028-0836 1476-4687 pmc-is-collection-domain yes pmc-collection-title NIHPA Author Manuscripts PMC10399640 PMC10399640.1 10399640 10399640 NIHMS1920814 
8	33473216 10.1038/s41586-020-03171-x NIHMS1920814 NIHPA1920814 1 Article Survey of spiking in the mouse visual system reveals functional hierarchy Siegle Joshua H. 1 6 Jia Xiaoxuan 1 6 Durand Séverine 
9	1 Gale Sam 1 Bennett Corbett 1 Graddis Nile 1 Heller Greggory 1 Ramirez Tamina K. 1 Choi Hannah 1 2 Luviano Jennifer A. 1 Groblewski Peter A. 1 Ahmed Ruweida 1 Arkhipov Anton 1 Bernard Amy 1 Billeh 
10	Yazan N. 1 Brown Dillan 1 Buice Michael A. 1 Cain Nicolas 1 Caldejon Shiella 1 Casal Linzy 1 Cho Andrew 1 Chvilicek Maggie 1 Cox Timothy C. 3 Dai Kael 1 Denman Daniel J. 1 4 de Vries Saskia E. J. 1 
11	Dietzman Roald 1 Esposito Luke 1 Farrell Colin 1 Feng David 1 Galbraith John 1 Garrett Marina 1 Gelfand Emily C. 1 Hancock Nicole 1 Harris Julie A. 1 Howard Robert 1 Hu Brian 1 Hytnen Ross 1 Iyer 
12	Ramakrishnan 1 Jessett Erika 1 Johnson Katelyn 1 Kato India 1 Kiggins Justin 1 Lambert Sophie 1 Lecoq Jerome 1 Ledochowitsch Peter 1 Lee Jung Hoon 1 Leon Arielle 1 Li Yang 1 Liang Elizabeth 1 Long 
13	Fuhui 1 Mace Kyla 1 Melchior Jose 1 Millman Daniel 1 Mollenkopf Tyler 1 Nayan Chelsea 1 Ng Lydia 1 Ngo Kiet 1 Nguyen Thuyahn 1 Nicovich Philip R. 1 North Kat 1 Ocker Gabriel Koch 1 Ollerenshaw Doug 1 
14	Oliver Michael 1 Pachitariu Marius 5 Perkins Jed 1 Reding Melissa 1 Reid David 1 Robertson Miranda 1 Ronellenfitch Kara 1 Seid Sam 1 Slaughterbeck Cliff 1 Stoecklin Michelle 1 Sullivan David 1 Sutton 
15	Ben 1 Swapp Jackie 1 Thompson Carol 1 Turner Kristen 1 Wakeman Wayne 1 Whitesell Jennifer D. 1 Williams Derric 1 Williford Ali 1 Young Rob 1 Zeng Hongkui 1 Naylor Sarah 1 Phillips John W. 1 Reid R. 
16	Clay 1 Mihalas Stefan 1 Olsen Shawn R. 1 7 Koch Christof 1 7 1 Allen Institute for Brain Science, Seattle, WA, USA. 2 Department of Applied Mathematics, University of Washington, Sea
[... 240 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 256,
 "limit": 330
}
```

```
256	Raw neural data was streamed to a compressed format for archiving, which was extracted before analysis. Videos of the eye and body were acquired at 30 Hz. The angular velocity of the running wheel 
257	was recorded at the time of each stimulus frame, at approximately 60 Hz. Synchronization signals for each frame were acquired by a dedicated computer with a National Instruments card acquiring 
258	digital inputs at 100 kHz, which was considered the master clock. A 32-bit digital ‘barcode’ was sent with an Arduino Uno (SparkFun DEV-11021) every 30 s to synchronize all devices with the neural 
259	data. Each Neuropixels probe has an independent sample rate between 29,999.90 Hz and 30,000.31 Hz, making it necessary to align the samples offline to achieve precise synchronization. The 
260	synchronization procedure used the first matching barcode between each probe and the master clock to determine the clock offset, and the last matching barcode to determine the clock scaling factor. 
261	If probe data acquisition was interrupted at any point during the experiment, each contiguous chunk of data was aligned separately. Because one LFP band sample was always acquired after every 12th 
262	spike band sample, these data streams could be synchronized automatically once the spike band clock rate has been determined. To synchronize the visual stimulus to the master clock, a silicon 
263	photodiode (PDA36A, Thorlabs) was placed on the stimulus monitor above a ‘sync square’ that flips from black to white every 60 frames. The analogue photodiode signal was thresholded and recorded as a 
264	digital event by the sync computer. Individual frame times were reconstructed by interpolating between the photodiode on/off events. Stimulus monitor. Visual stimuli were generated using custom 
265	scripts based on PsychoPy 62 and were displayed using an ASUS PA248Q LCD monitor, with 1,920 × 1,200 pixels (55.7 cm wide, 60 Hz refresh rate). Stimuli were presented monocularly, and the monitor
[... 320 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 585,
 "limit": 340
}
```

```
585	project was provided by the Allen Institute. We thank the Falconwood Foundation and the Tiny Blue Dot Foundation for additional funding. We thank the Mindscope Scientific Advisory Committee for 
586	feedback on this project. We thank J. Zhuang and Q. Wang for feedback on the manuscript and A. Zandvakili for discussions. Competing interests The authors declare no competing interests. 
587	Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41586-020-03171-x . Online content Any methods, additional references, Nature 
588	Research reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements 
589	of data and code availability are available at https://doi.org/10.1038/s41586-020-03171-x . Data availability The data from all 58 passive viewing experiments used to generate main text Figs. 1 - 3 
590	is available for download in Neurodata Without Borders (NWB) format via the AllenSDK. Example Jupyter Notebooks for accessing the data can be found at 
591	https://allensdk.readthedocs.io/en/latest/visual_coding_neuropixels.html . The Neurodata Without Borders files are also available on the DANDI Archive ( https://gui.dandiarchive.org/#/dandiset/000021 
592	; https://gui.dandiarchive.org/#/dandiset/000022 )) and as an AWS public dataset ( https://registry.opendata.aws/allen-brain-observatory/ ). The metrics table used to generate Fig. 4e - h (active 
593	behaviour experiments) is available in the GitHub repository for this manuscript ( https://github.com/AllenInstitute/neuropixels_platform_paper ). Code availability Code for the following purposes 
594	are available from these repositories: generating manuscript figures, https://github.com/AllenIn-stitute/neuropixels_platform_paper ; data pre-processing and unit metrics, 
595	https://github.com/AllenInstitute/ecephys_spike_sort-ing ;
[... 324 more lines not kept]
```

**Agent**

The text has the main text, Methods, and Extended Data legends. Now I'll check what the repo records about dandiset 000253 and look at the paper's code.

**Agent calls Bash**

```bash
cd  grep -rl "000253" --include=*.yaml --include=*.json --include=*.md --include=*.csv . 2>/dev/null | grep -v transcripts | head; ls
```

```
./targets/dandisets.json
./papers/manifest.yaml
LICENSE
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
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;d=json.load(open('targets/dandisets.json'))
items = d if isinstance(d,list) else d.get('dandisets', d)
for x in (items if isinstance(items,list) else items.values()):
    if '000253' in json.dumps(x): print(json.dumps(x,indent=1)[:4000])
"; grep -n -B3 -A15 "000253" papers/manifest.yaml | head -50
```

```
[
 {
  "dandiset": "000003",
  "name": "Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells",
  "published_version": "0.260218.2052",
  "asset_count": 101,
  "size_gb": 2559.25,
  "data_standards": [
   "Neurodata Without Borders (NWB)"
  ],
  "species": [
   "House mouse"
  ],
  "approaches": [
   "electrophysiological approach",
   "behavioral approach"
  ],
  "papers": [
   {
    "doi": "10.1016/j.neuron.2016.12.011",
[... 159 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;d=json.load(open('targets/dandisets.json'))
for x in d:
    if x['dandiset']=='000253': print(json.dumps(x,indent=1))
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 4, in <module>
    if x['dandiset']=='000253': print(json.dumps(x,indent=1))
       ~^^^^^^^^^^^^
TypeError: string indices must be integers, not 'str'
```

**Agent calls Bash**

```bash
cd  python -c "
import json;d=json.load(open('targets/dandisets.json'))
print(type(d), list(d)[:5] if isinstance(d,dict) else '')
s=json.dumps(d); i=s.find('\"000253\"'); print(s[i-50:i+2500])
"
```

```
<class 'dict'> ['schema_version', 'generated', 'source', 'counts', 'targets']
rint": true}], "catalystneuro": []}, {"dandiset": "000253", "name": "Allen Institute Openscope - Global/Local Oddball project", "published_version": "0.240923.1441", "asset_count": 98, "size_gb": 679.75, "data_standards": ["Neurodata Without Borders (NWB)"], "species": ["Mus musculus - House mouse"], "approaches": ["optogenetic approach", "electrophysiological approach"], "papers": [{"doi": "10.1038/s41586-020-03171-x", "title": "Survey of spiking in the mouse visual system reveals functional hierarchy ", "relation": "IsSupplementTo", "resource_type": null, "preprint": false}], "catalystneuro": []}, {"dandiset": "000289", "name": "Two-photon calcium imaging of EPG cells in Drosophila Melanogaster presented with cues of varying reliability", "published_version": "0.240801.1040", "asset_count": 221, "size_gb": 761.18, "data_standards": ["Neurodata Without Borders (NWB)"], "species": ["Drosophila melanogaster - Fruit fly"], "approaches": ["microscopy approach; cell population imaging", "behavioral approach"], "papers": [{"doi": "10.1101/2021.12.17.473253v4", "title": "Bayesian inference in ring attractor networks", "relation": "IsSupplementTo", "resource_type": null, "preprint": true}], "catalystneuro": []}, {"dandiset": "000294", "name": "A multi-modal fitting approach to construct single-neuron models with patch-clamp and high-density microelectrode arrays", "published_version": "0.260528.0854", "asset_count": 2, "size_gb": 18.17, "data_standards": ["Neurodata Without Borders (NWB)"], "species": ["Rattus norvegicus - Norway rat"], "approaches": ["electrophysiological approach"], "papers": [{"doi": "10.1162/neco_a_01676", "title": "A Multi-Modal Fitting Approach to Construct Single-Neuron Models with Patch-Clamp and High-Density Microelectrode Arrays", "relation": "IsDescribedBy", "resource_type": "JournalArticle", "preprint": false}], "catalystneuro": []}, {"dandiset": "000336", "name": "Al
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/000253/versions/0.240923.1441/ | python -c "import json,sys;d=json.load(sys.stdin);print(d.get('name'));print(d.get('description'));print(json.dumps(d.get('relatedResource'),indent=1)); print(d.get('keywords')); print(json.dumps(d.get('assetsSummary'),indent=1)[:1500])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/AllenInstitute/neuropixels_platform_paper.git npp 2>&1 | tail -2; cd npp && git log -1 --format='%H %cd' && find . -type f -not -path './.git/*' | head -100
```

```
4f8bcc26fa6fbec1ae687c650bacc9ea67a7036d Wed Jul 28 12:06:51 2021 -0700
./icon.png
./functions/time_to_first_spike.py
./functions/modulation_index.py
./functions/fit_exp.py
./environment.yml
./data/timescale_metrics.csv
./data/time_to_first_spike.csv
./data/processed_data/ccg_peak_offset_grating25_limit10ms_fraction.npy
./data/processed_data/ccg_peak_offset_grating25_limit10ms_final_shifted.npy
./data/processed_data/FFscore_grating_10.npy
./data/processed_data/FC_grating_dist_20_2.npy
./data/layer_info.csv
./data/decoding_data.csv
./data/decoder_accuracy_vs_number_of_cells.csv
./data/change_modulation_data.csv
./common/get_color_palette.py
./common/create_units_table.py
./README.md
./LICENSE.txt
[... 42 more lines not kept]
```

**Agent**

Cloned the paper's code (`neuropixels_platform_paper`, commit 4f8bcc2). Reading the unit selection and Figure 1, 3 and 4 scripts.

**Agent calls Bash**

```bash
cd $TMPDIR/npp; cat README.md | head -60; cat common/create_units_table.py; cat ExtDataFigure4/ExtDataFigure4.py | head -150
```

```
# Neuropixels Platform Paper

<img src="icon.png" width="400">

This repository contains code for generating the figures in the pre-print describing the scientific findings from the Allen Institute's [Neuropixels data collection platform](https://portal.brain-map.org/explore/circuits/visual-coding-neuropixels).

Most of the figures can be generated from publicly available NWB files and unit tables, available via the AllenSDK. See [the AllenSDK documentation](https://allensdk.readthedocs.io/en/latest/visual_coding_neuropixels.html) for an overview of the dataset and example notebooks for accessing it.

Each figure in the pre-print has a folder with associated code. Data required for figure generation that's not available in the October 2019 release (e.g., from the change detection experiments) is included in the `data` directory.

This repository is still a work in progress; we will continue to clean up the code and add documentation throughout the review process.


## Level of Support

We are not currently supporting this code, but simply releasing it to the community AS IS.  We are not able to provide any guarantees of support. The community is welcome to submit issues, but you should not expect an active response.


## Terms of Use

[... 229 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/npp; cat Figure3/Figure3.py
```

```
from scipy.ndimage.filters import gaussian_filter1d
from sklearn.utils import resample    

### PATH VARIABLES ##############################
cache_directory = '/mnt/nvme0/ecephys_cache_dir_2'
code_directory = '[removed: a home directory path]/GitHub/neuropixels_platform_paper'
###################################################

df = pd.read_csv(os.path.join(code_directory, 'data', 'unit_table.csv'), low_memory=False)

# %%

import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

plt.figure(14781)
plt.clf()

areas = ('LGd','VISp','VISl','VISrl','LP','VISal','VISpm','VISam')
[... 218 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/npp; cat Figure1/Figure1g.py functions/time_to_first_spike.py functions/modulation_index.py functions/fit_exp.py
```

```
from scipy.ndimage.filters import gaussian_filter1d
from scipy import stats

df = pd.read_csv(os.path.join(os.getcwd(), 'data', 'unit_table.csv'), low_memory=False)

# %%

areas = ('VISp','VISl','VISrl','VISal','VISpm','VISam','LGd', 'LP', 'HPC')

color_palette= 'seaborn'

key = 'specimen_id'

mice = df[key].unique()

values = np.zeros((len(mice), len(areas), 4))
values[:] = np.nan

np.random.seed(10)

[... 190 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/npp; cat Figure3/timescale_calculation.py Figure3/get_all_RFs.py | head -300
```

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 13:27:45 2020

@author: joshs
"""

# %%%


import os

import numpy as np
import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt
from scipy.ndimage.filters import gaussian_filter1d

from scipy.ndimage.filters import gaussian_filter1d
[... 280 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/npp; sed -n 300,500p Figure3/timescale_calculation.py; echo ======; sed -n 1,200p Figure3/get_all_RFs.py | grep -v "^\s*$" | head -150
```

```
import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

plt.rcParams.update({'font.size': 13})

# %%

from scipy.stats import linregress, spearmanr, pearsonr

metric = 'timescale_ac'

total_units = 0

plt.figure(19191)
plt.clf()

plt.subplot(3,2,1)

centers = np.zeros((8,))
[... 230 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/npp; cat Figure4/Figure4.py | grep -v "^\s*$" | head -400; head -3 data/change_modulation_data.csv data/decoding_data.csv
```

```
import os
import numpy as np
import scipy.stats
import pandas as pd
import matplotlib.pyplot as plt
#############################################################
code_directory = '[removed: a home directory path]/GitHub/neuropixels_platform_paper'
###################################################
dataDir = os.path.join(code_directory, 'data')
regions = ['LGd','V1','LM','RL','LP','AL','PM','AM']
hierScore = [-0.5150279628298357,
             -0.35733209934482374,
             -0.09388855125761343,
             -0.05987132463908328,
             0.10524780962600731,
             0.15221797920142832,
             0.32766807486511995,
             0.440986074378801]
hierColors = np.array([[217,141,194], # LGd
                       [129,116,177], # V1
[... 213 more lines not kept]
```

**Agent**

Figure 3 and 4 code read. Now the Figure 2 CCG notebooks.

**Agent calls Bash**

```bash
cd $TMPDIR/npp/Figure2; for f in compute_ccg.ipynb comparison_anatomical_functional_connectivity_final.ipynb; do echo "#### $f"; python -c "
import json,sys;nb=json.load(open('$f'))
for c in nb['cells']:
    if c['cell_type'] in('code','markdown'):
        s=''.join(c['source']); print('---',c['cell_type']); print(s[:3000])
        if c['cell_type']=='code':
            for o in c.get('outputs',[]):
                t=''.join(o.get('text',[])) or ''.join(o.get('data',{}).get('text/plain',[]))
                if t: print('>>OUT:',t[:600])
"; done > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt
```

```
175 /tmp/claude-1001/nb.txt
Shell cwd was reset to
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	#### compute_ccg.ipynb
2	--- code
3	import numpy as np
4	import pandas as pd
5	
6	import sys
7	#https://github.com/jiaxx/ccg_jitter
8	from ccg_jxx import get_ccgjitter
9	
10	import matplotlib.pyplot as plt
11	plt.style.use('default')
12	%matplotlib inline
13	--- code
14	import random
15	def simulate_spikes(dim):
16	    # dim: [neuron, ori, rep, time]
17	    # binarized
18	    X = np.random.rand(dim[0], dim[1], dim[2], dim[3])
19	    X[X>0.5]=1
20	    X[X<=0.5]=0
[... 156 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/npp; grep -v "^\s*$" ExtDataFigure1/ExtDataFigure1jk.py | head -80; echo =====; grep -v "^\s*$" ExtDataFigure10/ExtDataFigure10.py | grep -n "selection\|ranksums\|layer\|superficial\|deep\|cortical_layer\|print\|<\|>" | head -60
```

```
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
### PATH VARIABLES ##############################
cache_directory = '/mnt/nvme0/ecephys_cache_dir_2'
code_directory = '[removed: a home directory path]/GitHub/neuropixels_platform_paper'
###################################################
df = pd.read_csv(os.path.join(code_directory, 'data', 'unit_table.csv'), low_memory=False)
# %%
areas = ('VISp','VISl','VISrl','VISal','VISpm','VISam','LGd','LP') 
num_units_per_area = np.zeros((len(df.specimen_id.unique()), len(areas)))
num_overlap_per_area = np.zeros((len(df.specimen_id.unique()), len(areas), len(areas)))
min_units = 0
num_per_mouse = []
for mouse_idx, mouse in enumerate(df.specimen_id.unique()):
    selection1 =  (df.specimen_id == mouse) & \
                  (df.amplitude_cutoff < 0.1) & \
                  (df.presence_ratio > 0.95) & \
[... 112 more lines not kept]
```

**Agent**

Figure 2 code read. The CCG step calls an outside helper, `jiaxx/ccg_jitter`, which the notebook links. Checking it for bin size and peak definition.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/jiaxx/ccg_jitter.git cj 2>&1|tail -1; cd cj && git log -1 --format='%H %cd' && ls && grep -v "^\s*$" *.py | head -150
```

```
6559a4dfbc13f8e2ac8441a881bc8768bd6363a1 Mon Oct 5 13:01:35 2020 -0700
LICENSE
README.md
__pycache__
ccg_jxx.py
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 16:25:03 2017
@author: Xiaoxuan Jia
"""
###
import numpy as np
from scipy import stats
import scipy
#https://github.com/jiaxx/jitter
from jitter import jitter
def xcorrfft(a,b,NFFT):
    CCG = np.fft.fftshift(np.fft.ifft(np.multiply(np.fft.fft(a,NFFT), np.conj(np.fft.fft(b,NFFT)))))
    return CCG
def nextpow2(n):
[... 37 more lines not kept]
```

**Agent**

I have what the claims need from the text and code. Writing the claims file now.

**Agent calls Bash**

```bash
cd  grep -o "P = 0.081[^.]*" paper/*.txt | head -2; grep -o ".\{80\}1\.4%.\{40\}" paper/*.txt; grep -c "rather" paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "claims/000253/10.1038-s41586-020-03171-x.yaml",
 "content": "# Claims for Siegle, Jia et al. (2021), \"Survey of spiking in the mouse visual system reveals\n# functional hierarchy\", Nature 592, 86-92, on dandiset 000253.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-23,\n# protocol pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the NIH author manuscript in PubMed Central (PMC10399640, NIHMS1920814), as served\n# by NCBI PMC (paper/10.1038-s41586-020-03171-x.txt). It holds the main text, the Methods, the\n# legends of Figures 1 to 4 and of Extended Data Figures 1 to 10, and the data and code\n# availability statements. The version of record was not read. No PDF was available, so no\n# figure was seen: numbers shown only in figures (the p-value matrices of Extended Data Fig. 9,\n# the matrices of Extended Data Fig. 7c and 10d, the bars of Fig. 1g) could not be read. The\n# Supplementary Information of the version of record is not in the text; the results rest on the\n# main text, Methods and Extended Data, which are present.\n#\n# Code read: github.com/AllenInstitute/neuropixels_platform_paper at commit\n# 4f8bcc26fa6fbec1ae687c650bacc9ea67a7036d (the figure code the paper links). It holds one folder\n# per figure (Figure1 to Figure4, ExtDataFigure1, 4 and 10), common/create_units_table.py (the\n# unit table built from AllenSDK metrics plus data/time_to_first_spike.csv, data/layer_info.csv\n# and data/timescale_metrics.csv), functions for time to first spike, modulation index and\n# exponential fits, the precomputed CCG matrices of Fig. 2 (data/processed_data/*.npy), and the\n# per-unit and per-session metrics of the behaviour experiments (data/change_modulation_data.csv,\n# data/decoding_data.csv, data/decoder_accuracy_vs_number_of_cells.csv). Figure2/compute_ccg.ipynb\n# calls get_ccgjitter from github.com/jiaxx/ccg_jitter (read at commit\n# 6559a4dfbc13f8e2ac8441a881bc8768bd6363a1). Unit metrics (p_value_rf, area_rf, mod_idx_dg,\n# firing_rate_dg, snr) come from the AllenSDK, which the paper names as the code for stimulus\n# metrics. Choices the code settles are said in each criterion.\n#\n# The anatomical hierarchy scores are an outside input, recomputed in the paper from the\n# connectivity data of ref. 3 (Harris et al. 2019, doi:10.1038/s41586-019-1716-z). The text\n# gives only their order; the values are fixed in Figure3/Figure3.py and Figure4/Figure4.py:\n# LGN -0.515, V1 -0.357, LM -0.093, RL -0.059, LP 0.105, AL 0.152, PM 0.327, AM 0.441. Every\n# correlation with hierarchy below uses these eight values.\n#\n# Data the paper used. 58 passive viewing experiments (one session per mouse) passed quality\n# control out of 87 mice entering recording: C57BL/6J wild type (n = 30), Pvalb-IRES-Cre x Ai32\n# (8), Sst-IRES-Cre x Ai32 (12) and Vip-IRES-Cre x Ai32 (8). Up to six Neuropixels probes per\n# mouse targeted V1, LM, AL, RL, PM and AM and reached LGN (LGd) and LP; units were sorted with\n# Kilosort2 and mapped to CCFv3 structures. Each session began with receptive field mapping\n# (Gabor patches of drifting gratings at 81 locations, 250 ms each) and full-field dark or light\n# flashes (250 ms, 2 s interval), followed by one of two stimulus sets, \"Brain Observatory 1.1\"\n# (drifting gratings at 8 directions and 5 temporal frequencies, static gratings, natural\n# scenes, natural movies) or \"Functional Connectivity\" (drifting gratings at 4 directions, 2 Hz,\n# 75 repeats; contrast tuning; natural movie; dot motion; a 30 min grey screen of spontaneous\n# activity). The CCG analyses use 25 mice. Measured variables are spike times per unit, unit\n# quality metrics, stimulus tables, running speed and eye tracking. Separately, 12 mice in 21\n# sessions performed a go/no-go visual change detection task with natural images (n = 4,057\n# units), followed by passive replay of the same image sequence.\n#\n# Where the data are. The paper deposits the 58 passive viewing experiments (Figs. 1 to 3) on\n# DANDI as dandisets 000021 and 000022 and via the AllenSDK; the metrics table of the behaviour\n# experiments (Fig. 4e to h) is in the paper's GitHub repository; the raw behaviour sessions\n# are not said to be deposited anywhere. Dandiset 000253 is, by its archive title and\n# description, the \"Allen Institute Openscope - Global/Local Oddball project\", an OpenScope\n# predictive coding experiment (14 subjects, Neuropixels with optogenetics) recorded on the same\n# platform; it cites this paper as IsSupplementTo. Its title and description do not describe the\n# experiments of this paper. So every claim's data are recorded below as the paper gives them\n# (`elsewhere` with the archive, or `dataset` where the paper names no deposit), and whether\n# 000253 holds the same kind of recordings (the same receptive field mapping and flash stimuli,\n# the same areas) is for the author to find (author, step 4).\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000253\"\npaper: doi:10.1038/s41586-020-03171-x\nclaims:\n- id: methods-sessions-passing-qc\n  statement: Of 87 mice entering the recording step, 61 passed session-level quality control and\n    58 resulted in NWB files; these 58 passive viewing experiments are the ones analysed.\n  source: Results, A survey of visually evoked spiking, paragraph 2; Methods, Quality control for\n    the Neuropixels recording session; Methods, Data processing pipeline\n  quote: reducing the number of experiments analysed and presented here from 87 to 58\n  data: elsewhere\n  where: DANDI:000021 and DANDI:000022 (the paper's Data availability)\n  expected:\n  - quantity: passive viewing experiments analysed\n    value: 58\n    tolerance: 0\n  - quantity: C57BL/6J wild-type mice\n    value: 30\n    tolerance: 0\n  - quantity: Pvalb-IRES-Cre x Ai32 mice\n    value: 8\n    tolerance: 0\n  - quantity: Sst-IRES-Cre x Ai32 mice\n    value: 12\n    tolerance: 0\n  - quantity: Vip-IRES-Cre x Ai32 mice\n    value: 8\n    tolerance: 0\n  criterion: Counts of sessions and of mice by genotype, from the session metadata. The tolerance\n    is zero, not 10%, because these are counts of released sessions fixed by the release, as the\n    Methods (Mice) give them. The pipeline failures before recording cannot be tested on\n    released data and are not judged.\n- id: methods-probes-ccf\n  statement: About 5.7 probes per mouse entered the brain, and 284 of the 332 probes were mapped\n    to the CCFv3.\n  source: Methods, Neuropixels recordings, Probes; Methods, Ex vivo imaging quality control\n  quote: In total, 284 out of 332 probes were mapped to the CCFv3\n  data: elsewhere\n  where: DANDI:000021 and DANDI:000022 (the paper's Data availability)\n  expected:\n  - quantity: probes in the 58 experiments\n    value: 332\n    tolerance: 0\n  - quantity: probes mapped to the CCFv3\n    value: 284\n    tolerance: 0\n  - quantity: probes per mouse\n    value: 5.7\n    tolerance: 0.57\n  criterion: A probe counts as mapped when its units carry CCF coordinates, as\n    ExtDataFigure1/ExtDataFigure1jk.py counts it (has_ccf, a nonzero sum of anterior-posterior\n    CCF coordinates over the probe's units passing the quality filters of that script). The\n    tolerance on the two counts is zero for the reason given in methods-sessions-passing-qc.\n    The text does not say whether 332 counts probes of the 58 released experiments; 332/58 =\n    5.7 suggests so, and that reading is used, the count over all 61 sessions passing quality\n    control being shown as a variant.\n- id: ed1jk-units-per-experiment\n  statement: After quality filtering, 682 +/- 144 units were recorded per experiment, 119 +/- 48\n    per probe and 56 +/- 30 per visual area, with 6.1 +/- 1.1 visual areas sampled per\n    experiment.\n  source: Results, A survey of visually evoked spiking, paragraph 2; Extended Data Fig. 1j, k\n  quote: Overall, we recorded 682 ± 144 units per experiment, 119 ± 48 units per probe and 56 ± 30\n    units per visual area ( Extended Data Fig. 1j ), sampling 6.1 ± 1.1 visual areas per experiment\n  data: elsewhere\n  where: DANDI:000021 and DANDI:000022 (the paper's Data availability)\n  expected:\n  - quantity: units per experiment, mean\n    value: 682\n    tolerance: 144\n  - quantity: units per experiment, SD\n    value: 144\n    tolerance: 14.4\n  - quantity: units per probe, mean\n    value: 119\n    tolerance: 48\n  - quantity: units per visual area per experiment, mean\n    value: 56\n    tolerance: 30\n  - quantity: visual areas per experiment, mean\n    value: 6.1\n    tolerance: 1.1\n  criterion: Units filtered as the Extended Data Fig. 1j legend says (ISI violations < 0.5,\n    amplitude cutoff < 0.1, presence ratio > 0.95), and as ExtDataFigure1jk.py does, also\n    quality == good for the per-experiment and per-area counts but not for the per-probe count.\n    Per experiment, all structures; per area, the eight areas V1, LM, RL, AL, PM, AM, LGN and\n    LP, counting only areas with at least one unit; an area is sampled when it has at least one\n    unit. Mean and SD (numpy std) across the 58 experiments, across probes, and across\n    experiment-area pairs. The tolerance on the means is the stated spread, as the protocol\n    asks; on the SD of units per experiment, 10%.\n- id: fig1g-receptive-fields\n  statement: Units in the eight visual areas were highly visually responsive, 60% having a\n    significant spatial receptive field within the monitor, against only 1.4% of units in the\n    hippocampus (CA1, CA3 and dentate gyrus).\n  source: Results, A survey of visually evoked spiking, paragraph 3; Fig. 1g\n  quote: Units recorded in all eight cortical and thalamic visual areas were highly visually\n    responsive, with 60% displaying significant spatial receptive fields within the boundaries of\n    the monitor ... and found them in only 1.4% of units\n  data: elsewhere\n  where: DANDI:000021 and DANDI:000022 (the paper's Data availability)\n  expected:\n  - quantity: fraction of visual area units with a significant receptive field\n    value: 0.60\n    tolerance: 0.06\n  - quantity: fraction of hippocampal units with a significant receptive field\n    value: 0.014\n    tolerance: 0.0014\n  criterion: A receptive field is significant when the chi-square shuffle test of the Methods\n    (Receptive field analysis; 1,000 location shuffles, spike counts over the 250 ms Gabor\n    presentation) gives p < 0.01 (AllenSDK p_value_rf, Extended Data Fig. 4b legend). All\n    non-noise units, with no quality filter, as Figure1/Figure1g.py loads them. The 60% is the\n    pooled fraction over all units of the eight areas in all mice, as Figure1g.py computes it.\n    The code does not compute the 1.4%; the readings are (a) pooled over all CA1, CA3 and DG\n    units, (b) the mean across mice of each mouse's fraction (the quantity Fig. 1g plots).\n    Reproduced when the 60% and, under one reading, the 1.4% are within tolerance.\n- id: fig2-sharp-peak-pairs\n  statement: Jitter-corrected CCGs during drifting gratings showed a significant sharp peak\n    (within +/-10 ms and more than seven times the flank SD) for 16,119 of 2,089,890 possible\n    cortical unit pairs, 0.96% +/- 0.13% per mouse in 25 mice.\n  source: Results, A functional hierarchy of visual areas, paragraph 2; Extended Data Fig. 7b\n  quote: yielding 16,119 pairs of units out of 2,089,890 possible pairs within the cortex ( Extended\n    Data Fig. 7b ; 0.96% ± 0.13% per mouse, n = 25 mice)\n  data: elsewhere\n  where: DANDI:000021 and DANDI:000022 (the paper's Data availability)\n  expected:\n  - quantity: pairs with a significant sharp peak\n    value: 16119\n    tolerance: 1612\n  - quantity: possible cortical pairs\n    value: 2089890\n    tolerance: 208989\n  - quantity: fraction of pairs with a sharp peak per mouse, mean\n    value: 0.96\n    tolerance: 0.13\n    unit: percent\n  criterion: As the Methods (Cross-correlation analysis) give it. The 25 mice of the Functional\n    Connectivity stimulus set (75 repeats per orientation); drifting gratings at 0, 45, 90 and 135\n    degrees, 2 Hz, 0.04 cycles per degree, contrast 0.8; units of V1, LM, RL, AL, PM and AM with\n    mean rate above 2 Hz from 50 to 500 ms after onset; CCG normalized by the triangular overlap\n    and the geometric mean rate, computed per orientation and averaged over the four; jitter\n    window 25 ms, the jittered CCG being the analytical expected value of ref. 77; a peak is\n    significant when the maximum of the jitter-corrected CCG within +/-10 ms exceeds seven times\n    the SD of the flanks at 50 to 100 ms from zero. Open details. The bin width is not stated;\n    the example in Figure2/compute_ccg.ipynb uses 2,000 samples per 2 s presentation, so 1 ms,\n    and no other reading is given by the text. The CCG window is not stated; the readings are\n    (a) the 2 s presentation (the example's shape), (b) the 3 s of presentation and grey. The unit\n    quality filter is not stated in the text (Extended Data Fig. 4b was not seen); the readings\n    are (a) all non-noise units, (b) the filters of Extended Data Fig. 1j (ISI violations < 0.5,\n    amplitude cutoff < 0.1, presence ratio > 0.95). Variant from the code, shown not judged,\n    get_ccgjitter subtracts the CCG of one random jitter resample in place of the expected\n    value. Reproduced when, under one reading, the three values are within tolerance.\n- id: fig2d-v1-leads-lm-example\n  statement: In an example mouse, the CCG peak offsets between V1 and LM were shifted positive\n    against the V1-V1 distribution (median 3.9 ms), so V1 units on average lead LM units.\n  source: Results, A functional hierarchy of visual areas, paragraph 2; Fig. 2d\n  quote: the peak offset distribution between V1 and LM showed a significant positive delay\n    compared to the V1–V1 distribution ( Fig. 2d ; P = 2.6 × 10 −8 , two-sided Wilcoxon rank-sum\n    test), indicating that V1 neurons—on average—lead LM neurons\n  statistics:\n  - test: two-sided Wilcoxon rank-sum test\n    p: 2.6e-8\n    n: V1-LM against V1-V1 peak offsets in one example mouse\n  data: elsewhere\n  where: DANDI:000021 and DANDI:000022 (the paper's Data availability)\n  depends_on:\n  - fig2-sharp-peak-pairs\n  expected:\n    quantity: median V1 to LM peak offset in the example mouse\n    value: 3.9\n    tolerance: 0.39\n    unit: ms\n  criterion: Sharp peaks as in fig2-sharp-peak-pairs, V1 as source and LM as target, a positive\n    offset meaning V1 spikes lead. The example mouse is not identified in the paper or the code;\n    the readings are each of the 25 mice. Reproduced when in at least one mouse the median V1 to\n    LM offset is within tolerance and the two-sided rank-sum test against that mouse's V1-V1\n    offsets gives p < 0.05 with the V1-LM offsets higher. The result for every mouse is shown.\n- id: fig2-neighbour-offsets-across-mice\n  statement: Across 25 mice, the CCG peak offset distributions between neighbouring cortical areas\n    differ from the within-area distributions for V1-LM, LM-RL, RL-AL and PM-AM, but not for\n    AL-PM.\n  source: Methods, Cross-correlation analysis, last paragraph; Fig. 2e legend\n  quote: All between-area distributions are significantly different from the within-area\n    distributions at the 5% confidence level, except for AL–PM\n  statistics:\n  - about: V1-LM against V1-V1\n    test: Wilcoxon rank-sum per mouse, combined across mice with Fisher's method\n    p: 0\n    n: 25 mice\n  - about: LM-RL against LM-LM\n    test: Wilcoxon rank-sum per mouse, combined across mice with Fisher's method\n    p: 1.9e-5\n    n: 25 mice\n  - about: RL-AL against RL-RL\n    test: Wilcoxon rank-sum per mouse, combined across mice with Fisher's method\n    p: 2.4e-5\n    n: 25 mice\n  - about: AL-PM against AL-AL\n    test: Wilcoxon rank-sum per mouse, combined across mice with Fisher's method\n    p: 0.081\n    n: 25 mice\n  - about: PM-AM against PM-PM\n    test: Wilcoxon rank-sum per mouse, combined across mice with Fisher's method\n    p: 3.2e-4\n    n: 25 mice\n  data: elsewhere\n  where: DANDI:000021 and DANDI:000022 (the paper's Data availability)\n  depends_on:\n  - fig2-sharp-peak-pairs\n  criterion: Neighbouring areas by the anatomical hierarchy order of the cortex (V1, LM, RL, AL,\n    PM, AM), each pair compared with the within-area distribution of the lower area, as the\n    Methods list them. Per mouse, a two-sided Wilcoxon rank-sum test of the sharp peak offsets;\n    p-values combined over the mice with Fisher's method (mice lacking either distribution\n    left out, as the text does not say otherwise). Reproduced when V1-LM, LM-RL, RL-AL and PM-AM\n    give combined p < 0.05 and AL-PM gives p >= 0.05; partially reproduced when four of the five\n    pairs agree.\n- id: ed7c-v1-leads-am-follows\n  statement: On average V1 units lead the units of the other cortical areas, while AM follows\n    the other areas, placing AM at the top of the hierarchy.\n  source: Results, A functional hierarchy of visual areas, paragraph 3; Extended Data Fig. 7c\n  quote: On average, V1 units lead the activity of units in other areas ( Extended Data Fig. 7c ,\n    left column); by contrast, area AM follows other regions\n  data: elsewhere\n  where: DANDI:000021 and DANDI:000022 (the paper's Data availability)\n  depends_on:\n  - fig2-sharp-peak-pairs\n  criterion: For each mouse and ordered pair of cortical areas, the median peak offset of the\n    sharp peaks, averaged across mice (Extended Data Fig. 7c legend). Reproduced when the mean\n    median offset is positive with V1 as source for each of the five other areas as target, and\n    positive with AM as target for each of the five other areas as source; partially reproduced\n    when this holds for at least eight of the ten pairs.\n- id: fig2f-directionality-vs-anatomy\n  statement: The matrix of pairwise directionality scores between cortical areas is correlated\n    with the matrix of anatomical hierarchy score differences (Pearson r = 0.74 over 21 pairs).\n  source: Results, A functional hierarchy of visual areas, paragraph 3; Fig. 2e, f\n  quote: The matrix of pairwise directionality scores ( Fig. 2e ) between areas was very similar\n    to the matrix of anatomical hierarchy score differences ( Fig. 2b ) (Pearson’s r = 0.74, P = 1\n    × 10 −4\n  statistics:\n  - test: Pearson correlation\n    statistic: r = 0.74\n    p: 1.0e-4\n    n: 21 area pairs (lower triangle and diagonal)\n  data: elsewhere\n  where: DANDI:000021 and DANDI:000022 (the paper's Data availability)\n  depends_on:\n  - fig2-sharp-peak-pairs\n  expected:\n    quantity: Pearson r, directionality score against hierarchy score difference\n    value: 0.74\n    tolerance: 0.074\n  criterion: Directionality score DS = (C+ - C-)/(C+ + C-) for each source and target area, C+\n    and C- the numbers of sharp peaks with positive and negative lag (Methods, Directionality\n    score; zero lags enter neither count). The anatomical difference is the source score minus\n    the target score, from the scores in the opening comment. The 15 lower-triangle pairs and\n    the 6 diagonal entries, each pair taken in the same orientation in both matrices, as\n    Figure2/comparison_anatomical_functional_connectivity_final.ipynb does (it prints r = 0.74,\n    p = 1.47e-4). Open detail, how DS combines the 25 mice; the readings are (a) DS from the\n    offsets pooled over all mice (Fig. 2e legend, \"from peak offset distributions across 25\n    mice\"), (b) the mean across mice of each mouse's DS (Extended Data Fig. 10d legend, \"averaged\n    across mice\"). Reproduced when, under one reading, r is within tolerance and p < 0.05. The\n    precomputed DS matrix in data/processed_data/FFscore_grating_10.npy is shown as a variant.\n- id: ed7e-distance-does-not-explain\n  statement: The physical layout of the areas does not account for the correlation between\n    directionality and hierarchy in terms of average distance.\n  source: Results, A functional hierarchy of visual areas, paragraph 3; Extended Data Fig. 7e\n  quote: The spatial layout of areas could not account for this correlation in terms of average\n    physical distance\n  data: elsewhere\n  where: DANDI:000021 and DANDI:000022 (the paper's Data availability)\n  depends_on:\n  - fig2f-directionality-vs-anatomy\n  criterion: A claim of absence. The legend shows Pearson and Spearman coefficients of the\n    average 3D Euclidean distance between simultaneously recorded units of each pair of areas\n    (CCFv3 coordinates) against their hierarchy score difference; their values are not in the\n    text. The test is a Pearson correlation at p < 0.05 over the 21 pairs of Fig. 2f, the test\n    the paper uses for every hierarchy correlation. Open detail, whether the difference is\n    signed or absolute; the legend does not say, and both are run. Reproduced when the\n    correlation is not significant; not reproduced when it is. r is reported either way.\n- id: ed7fg-absent-in-spontaneous\n  statement: The functional hierarchy is absent during spontaneous activity (30 min grey screen),\n    which suggests it reflects activity driven by bottom-up input.\n  source: Results, A functional hierarchy of visual areas, paragraph 3; Extended Data Fig. 7f, g\n  quote: this organization was absent during spontaneous activity ( Extended Data Fig. 7f , g )\n  data: elsewhere\n  where: DANDI:000021 and DANDI:000022 (the paper's Data availability)\n  depends_on:\n  - fig2f-directionality-vs-anatomy\n  criterion: A claim of absence. Jitter-corrected CCGs and sharp peaks as in\n    fig2-sharp-peak-pairs, computed over the 30 min grey screen (Extended Data Fig. 7f legend);\n    DS averaged across mice (Extended Data Fig. 7g legend). The paper names no test for the\n    absence; the test it uses for the presence (Fig. 2f) is a Pearson correlation of DS against\n    hierarchy score difference over the 21 pairs, and that test is applied at p < 0.05.\n    Open detail, how the spontaneous period is cut into trials for the CCG; the text does not\n    say, and the readings are segments of 2 s and of 3 s matching the grating trials.\n    Reproduced when the correlation is not significant; not reproduced when it is. The number\n    of sharp peaks per mouse and r are reported either way.\n- id: ed8-total-hierarchy-score\n  statement: The measured functional network has a total hierarchy score of 0.89, close to a\n    simulated ladder-like hierarchy with feedback (0.88), above a one-to-all (0.15) or\n    three-level (0.38) network and below a strongly feedforward one (1.54).\n  source: Methods, Network model simulation; Extended Data Fig. 8\n  quote: The maximum difference of this trajectory (here between V1 and AM) is defined as the\n    total hierarchy score (THS) of the network, which is 0.89 for the measured functional network\n    in our data ... The resulting DS matrix showed a gradient very similar to the real data, with\n    a THS equal to 0.88\n  data: elsewhere\n  where: DANDI:000021 and DANDI:000022 (the paper's Data availability)\n  depends_on:\n  - fig2f-directionality-vs-anatomy\n  expected:\n    quantity: total hierarchy score of the measured network\n    value: 0.89\n    tolerance: 0.089\n  criterion: The mean DS from each source area to all target areas, and THS as the largest\n    difference of these means across areas (Methods, Network model simulation). Open details,\n    whether the mean includes the area's own diagonal entry, and how DS combines mice (the two\n    readings of fig2f-directionality-vs-anatomy); all four combinations are run. Reproduced when,\n    under one reading, THS is within tolerance and lies between the three-level value 0.38 and\n    the feedforward value 1.54. The simulations need no data and are not rerun.\n- id: fig3c-latency-hierarchy\n  statement: The mean time to first spike after a full-field flash in each area is correlated\n    with its anatomical hierarchy score.\n  source: Results, A functional hierarchy of visual areas, paragraph 4; Fig. 3a to c\n  quote: the mean visual latency of each area was correlated with its anatomical hierarchy score\n    ( Fig. 3c ; Pearson’s r = 0.95, P = 0.00025)\n  statistics:\n  - test: Pearson correlation\n    statistic: r = 0.95\n    p: 0.00025\n    n: 8 areas\n  data: elsewhere\n  where: DANDI:000021 and DANDI:000022 (the paper's Data availability)\n  expected:\n    quantity: Pearson r, mean time to first spike against hierarchy score\n    value: 0.95\n    tolerance: 0.095\n  criterion: Time to first spike per trial is the first spike from 30 ms after flash onset,\n    measured from onset; a unit's latency is the median over trials with a spike (Methods,\n    Response latency; functions/time_to_first_spike.py). Units as Figure3/Figure3.py selects\n    them, p_value_rf < 0.01, area_rf < 2500 deg2, snr > 1, firing_rate_dg > 0.1 Hz, and\n    latency < 100 ms; the area value is the mean over units; Pearson against the eight\n    hierarchy scores. The Methods exclude trials with no spike within 250 ms; the code's\n    default end is 500 ms, a variant. Open detail, which flashes; the text does not separate\n    dark and light, and the readings are (a) all flashes, (b) dark only, (c) light only. The\n    precomputed data/time_to_first_spike.csv is shown as a variant. Reproduced when, under one\n    reading, r is within tolerance and p < 0.05.\n- id: ed9a-latency-pairs\n  statement: Latencies differ significantly between all pairs of areas except LGN-V1, RL-LP,\n    LP-AL and AM-PM.\n  source: Results, A functional hierarchy of visual areas, paragraph 4; Extended Data Fig. 9a\n  quote: Statistical testing revealed significantly different latencies for all pairs of areas,\n    except for LGN–V1, RL–LP, LP–AL and AM–PM\n  statistics:\n  - test: two-sided Wilcoxon rank-sum test\n    p: 0.05\n    p_relation: \"<\"\n    corrected: Benjamini-Hochberg FDR\n    n: units of each area, 28 pairs of areas\n  data: elsewhere\n  where: DANDI:000021 and DANDI:000022 (the paper's Data availability)\n  depends_on:\n  - fig3c-latency-hierarchy\n  criterion: The unit latencies of fig3c-latency-hierarchy; for each of the 28 pairs of areas a\n    two-sided Wilcoxon rank-sum test with units as independent samples, Benjamini-Hochberg FDR\n    over the 28 at alpha 0.05 (Methods, Other statistical methods; Figure3.py, which adds 1e-5\n    to each p). Reproduced when the four named pairs are not significant and the other 24 are;\n    partially reproduced when at most two of the 28 pairs disagree.\n- id: fig3f-rf-size-hierarchy\n  statement: Receptive field size increases with anatomical hierarchy score.\n  source: Results, A functional hierarchy of visual areas, paragraph 4; Fig. 3d to f\n  quote: found a systematic increase in receptive field size with anatomical hierarchy score ( Fig.\n    3d - f ; Pearson’s r = 0.97, P = 8.3 × 10 −5 )\n  statistics:\n  - test: Pearson correlation\n    statistic: r = 0.97\n    p: 8.3e-5\n    n: 8 areas\n  data: elsewhere\n  where: DANDI:000021 and DANDI:000022 (the paper's Data availability)\n  expected:\n    quantity: Pearson r, mean receptive field area against hierarchy score\n    value: 0.97\n    tolerance: 0.097\n  criterion: Receptive field area as the Methods define it (spike counts over 250 ms at 81\n    locations, Gaussian smoothing with sigma 1, threshold max(RF) - std(RF), largest contiguous\n    region, pixels x 100 deg2; AllenSDK area_rf). Units selected as Figure3.py does\n    (p_value_rf < 0.01, area_rf < 2500, snr > 1, firing_rate_dg > 0.1); the area value is the\n    mean over units; Pearson against the eight hierarchy scores. Reproduced when r is within\n    tolerance and p < 0.05.\n- id: ed9d-rf-size-pairs\n  statement: Receptive field sizes differ significantly between all pairs of areas except LM-RL.\n  source: Results, A functional hierarchy of visual areas, paragraph 4; Extended Data Fig. 9d\n  quote: Statistical testing revealed significantly different receptive field sizes for all pairs\n    of areas, except for LM–RL\n  statistics:\n  - test: two-sided Wilcoxon rank-sum test\n    p: 0.05\n    p_relation: \"<\"\n    corrected: Benjamini-Hochberg FDR\n    n: units of each area, 28 pairs of areas\n  data: elsewhere\n  where: DANDI:000021 and DANDI:000022 (the paper's Data availability)\n  depends_on:\n  - fig3f-rf-size-hierarchy\n  criterion: The test of ed9a-latency-pairs on the unit receptive field areas of\n    fig3f-rf-size-hierarchy. Reproduced when LM-RL is not significant and the other 27 pairs are;\n    partially reproduced when at most two pairs disagree.\n- id: fig3i-modulation-index-hierarchy\n  statement: The modulation index of responses to drifting gratings is highest in LGN and\n    decreases along the hierarchy.\n  source: Results, A functional hierarchy of visual areas, paragraph 4; Fig. 3g to i\n  quote: The modulation index was highest in the LGN, whereas higher areas showed gradually less\n    phase-dependent modulation ( Fig. 3g - i , Pearson’s r = −0.89, P = 0.003)\n  statistics:\n  - test: Pearson correlation\n    statistic: r = -0.89\n    p: 0.003\n    n: 8 areas\n  data: elsewhere\n  where: DANDI:000021 and DANDI:000022 (the paper's Data availability)\n  expected:\n    quantity: Pearson r, mean modulation index against hierarchy score\n    value: -0.89\n    tolerance: 0.089\n  criterion: Modulation index as the Methods define it, from the Welch power spectrum of the\n    10 ms binned PSTH at each unit's preferred condition (AllenSDK mod_idx_dg, drifting\n    gratings). Units selected as Figure3.py does (as in fig3f-rf-size-hierarchy). Figure3.py\n    takes log10 of each unit's index and averages that; the Methods do not say, so the readings\n    are (a) the mean of log10 MI, as the code does, (b) the mean of MI. Pearson against the\n    eight hierarchy scores. Reproduced when, under one reading, r is within tolerance, p < 0.05\n    and LGN has the highest area mean.\n- id: ed9e-modulation-index-pairs\n  statement: Modulation indices differ significantly between all pairs of areas except RL-AL and\n    AM-PM.\n  source: Results, A functional hierarchy of visual areas, paragraph 4; Extended Data Fig. 9e\n  quote: Statistical tests revealed significantly different modulation indices for all pairs of\n    areas, except for RL–AL and AM–PM\n  statistics:\n  - test: two-sided Wilcoxon rank-sum test\n    p: 0.05\n    p_relation: \"<\"\n    corrected: Benjamini-Hochberg FDR\n    n: units of each area, 28 pairs of areas\n  data: elsewhere\n  where: DANDI:000021 and DANDI:000022 (the paper's Data availability)\n  depends_on:\n  - fig3i-modulation-index-hierarchy\n  criterion: The test of ed9a-latency-pairs on the unit values of\n    fig3i-modulation-index-hierarchy (log10 MI as in Figure3.py; a rank test gives the same\n    result on MI). Reproduced when RL-AL and AM-PM are not significant and the other 26 pairs\n    are; partially reproduced when at most two pairs disagree.\n- id: ed9fg-intrinsic-timescale-not-correlated\n  statement: The mean intrinsic timescale of spontaneous activity in each area is not correlated\n    with the visual hierarchy.\n  source: Results, A functional hierarchy of visual areas, paragraph 4; Extended Data Fig. 9f, g\n  quote: this mean intrinsic timescale for each area was not correlated with the visual hierarchy\n    ( Extended Data Fig. 9f , g ) (Pearson’s r = −0.24, P = 0.57)\n  statistics:\n  - test: Pearson correlation\n    statistic: r = -0.24\n    p: 0.57\n    n: 8 areas\n  data: elsewhere\n  where: DANDI:000021 and DANDI:000022 (the paper's Data availability)\n  criterion: A claim of absence, judged on the paper's test, a Pearson correlation of the area\n    means against the eight hierarchy scores at p < 0.05. Intrinsic timescale as the Methods\n    give it, the 1 s before each flash in 10 ms bins, Pearson correlation of spike counts at\n    each pair of bins, diagonals of the 100 x 100 matrix averaged, an exponential fitted to the\n    first 50 points with the timescale bounded at 1 to 1,000 ms; units kept when the SD of the\n    timescale estimate is below 100 and at least 100 spikes were used. Units as in\n    Figure3/timescale_calculation.py (p_value_rf < 0.01, area_rf < 2500, snr > 1,\n    firing_rate_dg > 0.1). Variant from the code, shown not judged, the window 1.0 to 2.0 s\n    after flash onset and the further limits 5 < timescale < 400 ms. Reproduced when p >= 0.05;\n    not reproduced when p < 0.05. r is reported either way.\n- id: fig3l-response-decay-timescale-hierarchy\n  statement: Higher-order areas have a longer response decay timescale during the flash response,\n    and the area mean correlates with hierarchy score.\n  source: Results, A functional hierarchy of visual areas, paragraph 4; Fig. 3j to l\n  quote: Higher-order areas had a longer response decay timescale, and therefore maintain\n    stimulus-evoked activity over longer temporal windows, than lower stages ... ( Fig. 3j - l ;\n    Pearson’s r = 0.86, P = 0.007)\n  statistics:\n  - test: Pearson correlation\n    statistic: r = 0.86\n    p: 0.007\n    n: 8 areas, 7,837 units from 58 mice\n  data: elsewhere\n  where: DANDI:000021 and DANDI:000022 (the paper's Data availability)\n  expected:\n    quantity: Pearson r, mean response decay timescale against hierarchy score\n    value: 0.86\n    tolerance: 0.086\n  criterion: Response decay timescale as the Methods give it, spike counts in 10 ms bins over the\n    250 ms flash presentation, a 2D autocorrelation (scipy.signal.correlate) averaged over trials,\n    an exponential fitted with the timescale bounded at 1 to 1,000 ms; units kept when the SD of\n    the estimate is below 20 and more than 50 spikes were used, and as Figure3.py also requires,\n    1 < timescale < 300 ms. Units otherwise as in fig3f-rf-size-hierarchy. Area mean, Pearson\n    against the eight hierarchy scores. The Methods and the code disagree on the window; the\n    Methods' 0 to 250 ms is the main result, and the code's 40 to 290 ms after onset\n    (timescale_calculation.py) is a variant. Reproduced when r is within tolerance and p < 0.05.\n- id: ed9h-response-decay-pairs\n  statement: Response decay timescales differ significantly between all pairs of areas except\n    LM-AL and AM-PM.\n  source: Results, A functional hierarchy of visual areas, paragraph 4; Extended Data Fig. 9h\n  quote: Statistical testing revealed significantly distinct response decay timescales for all\n    pairs of areas, except for LM–AL and AM–PM\n  statistics:\n  - test: two-sided Wilcoxon rank-sum test\n    p: 0.05\n    p_relation: \"<\"\n    corrected: Benjamini-Hochberg FDR\n    n: units of each area, 28 pairs of areas\n  data: elsewhere\n  where: DANDI:000021 and DANDI:000022 (the paper's Data availability)\n  depends_on:\n  - fig3l-response-decay-timescale-hierarchy\n  criterion: The test of ed9a-latency-pairs on the unit values of\n    fig3l-response-decay-timescale-hierarchy. Reproduced when LM-AL and AM-PM are not significant\n    and the other 26 pairs are; partially reproduced when at most two pairs disagree.\n- id: fig3-unit-counts\n  statement: The Figure 3 analyses use 15,713 units from 58 mice, and the response decay\n    timescale 7,837 units.\n  source: Fig. 3 legend\n  quote: n = 7,837 units from 58 mice ... n = 15,713 units from 58 mice unless otherwise specified\n  data: elsewhere\n  where: DANDI:000021 and DANDI:000022 (the paper's Data availability)\n  expected:\n  - quantity: units in the Figure 3 selection\n    value: 15713\n    tolerance: 1571\n  - quantity: units in the response decay timescale selection\n    value: 7837\n    tolerance: 784\n  criterion: The selection of Figure3.py over the eight areas, p_value_rf < 0.01, area_rf <\n    2500, snr > 1, firing_rate_dg > 0.1 (15,713), and with the timescale limits of\n    fig3l-response-decay-timescale-hierarchy (7,837). Reproduced when both counts are within\n    tolerance.\n- id: ed9bc-spontaneous-latency\n  statement: Time to first spike measured in the grey pre-stimulus interval is not correlated with\n    hierarchy score but is strongly negatively correlated with baseline firing rate, so firing\n    rate does not explain the latency result.\n  source: Methods, Response latency; Extended Data Fig. 9b, c\n  quote: Under these conditions, TFS for individual areas was not correlated with anatomical\n    hierarchy score (Pearson’s r = 0.57, P = 0.14), but was strongly negatively correlated with\n    their baseline firing rates (Pearson’s r = −0.98, P = 0.00001\n  statistics:\n  - about: spontaneous time to first spike against hierarchy score\n    test: Pearson correlation\n    statistic: r = 0.57\n    p: 0.14\n    n: 8 areas\n  - about: spontaneous time to first spike against baseline firing rate\n    test: Pearson correlation\n    statistic: r = -0.98\n    p: 0.00001\n    n: 8 areas\n  data: elsewhere\n  where: DANDI:000021 and DANDI:000022 (the paper's Data availability)\n  depends_on:\n  - fig3c-latency-hierarchy\n  expected:\n    quantity: Pearson r, spontaneous time to first spike against baseline firing rate\n    value: -0.98\n    tolerance: 0.098\n  criterion: The latency procedure of fig3c-latency-hierarchy applied to the 1 s grey interval\n    before each flash, with the same units. Two parts. The absence of a correlation with\n    hierarchy is judged on the paper's test, Pearson at p < 0.05 over the eight areas\n    (reproduced when p >= 0.05). The negative correlation with baseline rate is reproduced when\n    r is within tolerance and p < 0.05. Open detail, the baseline rate; the readings are (a)\n    the mean rate in the same 1 s grey interval, (b) the overall firing rate of the unit\n    table. The claim is reproduced when both parts hold, partially when one does.\n- id: ed9ij-firing-rate-not-correlated\n  statement: Overall firing rate does not correlate with hierarchy score, so the four metrics\n    do not depend on it.\n  source: Results, A functional hierarchy of visual areas, paragraph 5; Extended Data Fig. 9i, j\n  quote: These metrics are not dependent on overall firing rate, which does not correlate with\n    hierarchy score ( Extended Data Fig. 9i , j )\n  data: elsewhere\n  where: DANDI:000021 and DANDI:000022 (the paper's Data availability)\n  criterion: A claim of absence. The text names no test; the legend shows Pearson and Spearman\n    coefficients, and Figure3.py's alternative branch computes the mean of log10 firing_rate\n    per area with the unit selection of Figure 3 and its Pearson correlation with the eight\n    hierarchy scores. That test at p < 0.05 is applied. Reproduced when p >= 0.05; not\n    reproduced when p < 0.05. r is reported either way; the mean of the untransformed rate is\n    shown as a variant.\n- id: ed10b-layers\n  statement: Compared with deep layers (5 and 6), superficial layers (2/3 and 4) have an earlier\n    time to first spike, smaller receptive fields, a higher modulation index and a faster response\n    decay timescale.\n  source: Extended Data Fig. 10b legend; Results, A functional hierarchy of visual areas,\n    paragraph 5\n  quote: On average, in comparison to deep layers (5 and 6), superficial layers (2/3 and 4) had an\n    earlier time to first spike (2.59 ms difference, P = 2.7 × 10 −19 , two-sided Wilcoxon\n    rank-sum test), smaller receptive fields (109° difference, P = 1.1 × 10 −33 ), higher\n    modulation index (0.09 MI difference, P = 5.0 × 10 −23 ), and faster response decay timescale\n    (6.6 ms difference, P = 3.8 × 10 −33 )\n  statistics:\n  - about: time to first spike, superficial against deep\n    test: two-sided Wilcoxon rank-sum test\n    p: 2.7e-19\n  - about: receptive field area, superficial against deep\n    test: two-sided Wilcoxon rank-sum test\n    p: 1.1e-33\n  - about: modulation index, superficial against deep\n    test: two-sided Wilcoxon rank-sum test\n    p: 5.0e-23\n  - about: response decay timescale, superficial against deep\n    test: two-sided Wilcoxon rank-sum test\n    p: 3.8e-33\n  data: elsewhere\n  where: DANDI:000021 and DANDI:000022 (the paper's Data availability)\n  depends_on:\n  - fig3c-latency-hierarchy\n  - fig3f-rf-size-hierarchy\n  - fig3i-modulation-index-hierarchy\n  - fig3l-response-decay-timescale-hierarchy\n  expected:\n  - quantity: time to first spike, deep minus superficial\n    value: 2.59\n    tolerance: 0.259\n    unit: ms\n  - quantity: receptive field area, deep minus superficial\n    value: 109\n    tolerance: 10.9\n    unit: deg2\n  - quantity: modulation index, superficial minus deep\n    value: 0.09\n    tolerance: 0.009\n  - quantity: response decay timescale, deep minus superficial\n    value: 6.6\n    tolerance: 0.66\n    unit: ms\n  criterion: Cortical units of all six areas pooled, with the selections of the four Figure 3\n    metrics and cortical_depth > 0, layers from the CCF labels (data/layer_info.csv), split as\n    ExtDataFigure10/ExtDataFigure10.py does into layer < 5 and layer >= 5, and a two-sided\n    rank-sum test per metric. The legend's \"deg\" for the area is read as deg2. Open details. The\n    difference is not defined; the readings are (a) difference of means (the legend's \"on\n    average\"), (b) difference of medians. The modulation index enters the code as log10; the\n    readings are (a) log10 MI, (b) MI. The code's layer < 5 can include layer 1 units, while the\n    legend names 2/3 and 4; the readings are (a) layer < 5, (b) layers 2/3 and 4 only. Each part\n    is reproduced when, under one reading, the difference has the stated sign and is within\n    tolerance and p < 0.05; the claim is reproduced when all four parts are, partially when two\n    or three are.\n- id: ed10ce-superficial-lead-deep\n  statement: Within an area, superficial layers (2 to 4) are hierarchically lower than deep layers\n    (5 and 6), with superficial layers tending to drive deep layers in the CCG analysis.\n  source: Results, A functional hierarchy of visual areas, paragraph 5; Extended Data Fig. 10c to e\n  quote: Analysis of layer-wise CCG interactions indicated that superficial layers (2/3 and 4) were\n    hierarchically lower compared to deep layers (5, 6) in the same area\n  data: elsewhere\n  where: DANDI:000021 and DANDI:000022 (the paper's Data availability)\n  depends_on:\n  - fig2-sharp-peak-pairs\n  criterion: Sharp peaks as in fig2-sharp-peak-pairs, units split into superficial (layers 2 to\n    4) and deep (layers 5 and 6) per area (Extended Data Fig. 10c legend); DS averaged across mice\n    (Extended Data Fig. 10d legend). The within-area, superficial to deep DS is computed for each\n    of the six cortical areas, then averaged over areas (Extended Data Fig. 10e). Reproduced when\n    the mean DS from superficial source to deep target is positive and positive in at least four\n    of the six areas; partially reproduced when the mean is positive in fewer areas.\n- id: anatomical-hierarchy-order\n  statement: In the anatomical hierarchy recomputed from ref. 3, LGN is lowest, then V1, with LM,\n    RL, LP and AL at intermediate levels and PM and AM at the top; all areas have significantly\n    different scores except RL and LM.\n  source: Results, A functional hierarchy of visual areas, paragraph 1; Fig. 2a, b; Methods,\n    Anatomical hierarchy analysis\n  quote: The LGN sits at the bottom of the hierarchy, followed by its major target structure, V1;\n    areas LM, RL, LP and AL reside at intermediate levels, and areas PM and AM occupy the top\n    level of the areas we studied here\n  statistics:\n  - about: RL against LM, bootstrapped hierarchy scores\n    test: Wilcoxon paired signed rank-sum test\n    p: 0.08\n    n: 100 bootstrap samples of the connectivity data\n  data: elsewhere\n  where: Connectivity data of Harris et al. 2019, Nature 575, 195-202, doi:10.1038/s41586-019-1716-z (ref. 3)\n  criterion: Not tested on any recording; it rests on the anatomical tracing data of ref. 3. The\n    order is checked against the scores fixed in the paper's code (opening comment). Reproduced\n    when those scores give the stated order. The bootstrap test can only be rerun from the\n    ref. 3 data and is reported as not run if they are not used.\n- id: fig4b-behaviour-performance\n  statement: Mice performed the change detection task with high hit and low false alarm rates\n    (mean hit rate 0.78, false alarm rate 0.13, d-prime 2.0 +/- 0.1 in 12 mice, 21 sessions).\n  source: Results, A functional hierarchy of visual areas, paragraph 6; Fig. 4b\n  quote: Mice performed with high hit and low false alarm rates (mean hit rate = 0.78, mean false\n    alarm rate = 0.13, and mean detection sensitivity ( d′ ) = 2.0 ± 0.1, in 12 mice, 21 sessions\n  data: dataset\n  expected:\n  - quantity: mean hit rate\n    value: 0.78\n    tolerance: 0.078\n  - quantity: mean false alarm rate\n    value: 0.13\n    tolerance: 0.013\n  - quantity: mean d-prime\n    value: 2.0\n    tolerance: 0.1\n  criterion: Hits are licks within 750 ms of an image change, false alarms licks within 750 ms of\n    a catch (non-change) time (Methods, Behaviour training), over the 21 behaviour sessions.\n    The paper names no deposit of these sessions; whether any dataset holds them is the author's\n    to find. Open details. Aborted trials are left out (the Methods count \"contingent\n    (non-aborted) trials\"). The mean is not defined; the readings are (a) over sessions, (b) over\n    mice. The d-prime spread is read as the s.e.m. and used as its tolerance. Reproduced when,\n    under one reading, all three are within tolerance.\n- id: fig4e-behaviour-latency-hierarchy\n  statement: During behaviour the first spike latency of image responses is correlated with the\n    anatomical hierarchy score.\n  source: Results, A functional hierarchy of visual areas, paragraph 6; Fig. 4e\n  quote: the first spike latency for image responses during behaviour was correlated with the\n    anatomical hierarchy score ( Fig. 4e )\n  data: elsewhere\n  where: GitHub AllenInstitute/neuropixels_platform_paper, commit 4f8bcc26fa6fbec1ae687c650bacc9ea67a7036d, data/change_modulation_data.csv\n  criterion: As Figure4/Figure4.py computes it from the paper's metrics table, the mean of 'Time\n    To First Spike' per region over units and its Pearson correlation with the eight hierarchy\n    scores. The text gives no r; reproduced when r > 0 and p < 0.05.\n- id: fig4f-change-modulation-hierarchy\n  statement: During active behaviour the change modulation index is positive in every area and\n    increases along the hierarchy from LGN to AM, and it is larger during active behaviour than\n    during passive replay.\n  source: Results, A functional hierarchy of visual areas, paragraph 7; Fig. 4f\n  quote: During active behaviour, CMI was positive for each area ... More importantly, CMI\n    systematically increased along the hierarchy from the LGN to the AM ( Fig. 4f ; Pearson’s r =\n    0.83, P = 0.011) ... CMI values were larger during active behaviour compared with passive\n    viewing of the same stimulus sequence\n  statistics:\n  - test: Pearson correlation\n    statistic: r = 0.83\n    p: 0.011\n    n: 8 areas, 4,057 units from 12 mice\n  data: elsewhere\n  where: GitHub AllenInstitute/neuropixels_platform_paper, commit 4f8bcc26fa6fbec1ae687c650bacc9ea67a7036d, data/change_modulation_data.csv\n  expected:\n    quantity: Pearson r, mean active change modulation index against hierarchy score\n    value: 0.83\n    tolerance: 0.083\n  criterion: From the paper's metrics table, as Figure4.py computes it, the mean over units of\n    'Change Modulation Active' per region (nanmean) and its Pearson correlation with the eight\n    hierarchy scores. Three parts, (1) r within tolerance with p < 0.05, (2) the active mean\n    above zero in each of the eight areas, (3) active above passive; the paper gives no test for\n    (3), and the readings are (a) the active mean above the passive mean in every area, (b) in the\n    mean over the eight areas. Reproduced when all three hold under one reading; partially when\n    (1) holds. Recomputing the index from spikes would need the response window, which the\n    Methods do not give; it is not done.\n- id: ed9k-cmi-hit-not-miss\n  statement: The change modulation index correlates with hierarchy on hit trials but not on miss\n    trials.\n  source: Results, A functional hierarchy of visual areas, paragraph 7; Extended Data Fig. 9k\n  quote: we found a significant correlation of CMI with hierarchy on hit but not on miss trials (\n    Extended Data Fig. 9k ; hit trials, Pearson’s r = 0.85, P = 0.007; miss trials, Pearson’s r =\n    0.51, P = 0.2)\n  statistics:\n  - about: hit trials\n    test: Pearson correlation\n    statistic: r = 0.85\n    p: 0.007\n    n: 8 areas\n  - about: miss trials\n    test: Pearson correlation\n    statistic: r = 0.51\n    p: 0.2\n    n: 8 areas\n  data: elsewhere\n  where: GitHub AllenInstitute/neuropixels_platform_paper, commit 4f8bcc26fa6fbec1ae687c650bacc9ea67a7036d, data/change_modulation_data.csv\n  depends_on:\n  - fig4f-change-modulation-hierarchy\n  expected:\n    quantity: Pearson r, hit trials\n    value: 0.85\n    tolerance: 0.085\n  criterion: From the paper's metrics table, the per-region means of 'Change Modulation Hit' and\n    'Change Modulation Miss' and their Pearson correlations with the hierarchy scores, as\n    Figure4.py computes them. The hit part is reproduced when r is within tolerance and p < 0.05;\n    the miss part, a claim of absence on the same test, when p >= 0.05. Reproduced when both\n    hold, partially when one does.\n- id: ed9lmn-other-responses-not-correlated\n  statement: Baseline firing rate, the response to the pre-change image and the response to the\n    change image during the task are not correlated with hierarchy score.\n  source: Results, A functional hierarchy of visual areas, paragraph 7; Extended Data Fig. 9l to n\n  quote: Other aspects of neural activity during the task—including the baseline firing rate,\n    response to the pre-change image and the response to the change image—were not correlated\n    with hierarchy score\n  data: elsewhere\n  where: GitHub AllenInstitute/neuropixels_platform_paper, commit 4f8bcc26fa6fbec1ae687c650bacc9ea67a7036d, data/change_modulation_data.csv\n  criterion: A claim of absence. The text names no test; Figure4.py computes, for each of the\n    three measures, the per-region mean and its Pearson correlation with the hierarchy scores,\n    and that test at p < 0.05 is applied to the active ('during the task') columns. Reproduced\n    when none of the three is significant; not reproduced when any is. The passive columns,\n    which the figure also shows, are a variant; r and p are reported for all six.\n- id: fig4h-decoder-behaviour-hierarchy\n  statement: The trial-wise covariation of change decoder output with the mouse's choices\n    increases along the hierarchy, starting with no correlation in LGN.\n  source: Results, A functional hierarchy of visual areas, paragraph 8; Fig. 4g, h\n  quote: we found a strong increase in trial-wise decoder-behaviour covariation at higher levels\n    of the hierarchy, starting with no correlation at the level of the LGN ( Fig. 4h ; Pearson’s r\n    = 0.88, P = 0.004\n  statistics:\n  - test: Pearson correlation\n    statistic: r = 0.88\n    p: 0.004\n    n: 8 areas\n  data: elsewhere\n  where: GitHub AllenInstitute/neuropixels_platform_paper, commit 4f8bcc26fa6fbec1ae687c650bacc9ea67a7036d, data/decoding_data.csv\n  expected:\n    quantity: Pearson r, decoder-behaviour correlation against hierarchy score\n    value: 0.88\n    tolerance: 0.088\n  criterion: From the paper's table of per-session decoder results, the mean over sessions of\n    'Correleation of decoder prediction and mouse behavior' per region and its Pearson\n    correlation with the hierarchy scores, as Figure4.py computes it. \"No correlation\" in LGN\n    has no test in the paper; it is read from Fig. 4h's mean +/- s.e.m. across sessions, and\n    holds when that interval includes zero. Reproduced when r is within tolerance, p < 0.05 and\n    the LGN interval includes zero; partially when only the correlation holds. Recomputing the\n    decoders (random forests of 100 trees, fivefold cross validation, subsamples of 20 units) is\n    a variant.\n- id: ed9p-decoders-above-chance\n  statement: Change decoders trained on 20 units performed better than chance in all eight areas,\n    and decoder accuracy was not correlated with hierarchy score.\n  source: Results, A functional hierarchy of visual areas, paragraph 8; Extended Data Fig. 9p\n  quote: Decoders were separately trained for 20 units within each area and performed\n    significantly better than chance across trials, indicating that change trials could be read\n    out from all 8 areas\n  data: elsewhere\n  where: GitHub AllenInstitute/neuropixels_platform_paper, commit 4f8bcc26fa6fbec1ae687c650bacc9ea67a7036d, data/decoding_data.csv\n  criterion: From the per-session 'Decoder accuracy' column. Chance is 0.5 (change against\n    pre-change presentations). The paper names no test for \"better than chance\"; the readings\n    are (a) the mean minus s.e.m. across sessions (the error bars of Extended Data Fig. 9p) above\n    0.5 in each area, (b) a one-sided one-sample t-test across sessions against 0.5 at p < 0.05\n    in each area. The absence of a correlation with hierarchy (legend) is judged by the Pearson\n    test of Figure4.py at p < 0.05. Reproduced when all eight areas are above chance under one\n    reading and the correlation is not significant; partially when one of the two holds.\n- id: methods-gaze-stability\n  statement: Across 50 mice with eye tracking, 95% of gaze locations fell within 6.4 +/- 2.1\n    degrees of the mean, with a maximum of 13.6 degrees.\n  source: Methods, Eye and pupil tracking\n  quote: On average, 95% of gaze locations fell within 6.4 ± 2.1° of the mean, with a maximum of\n    13.6°\n  data: elsewhere\n  where: DANDI:000021 and DANDI:000022 (the paper's Data availability)\n  expected:\n  - quantity: radius containing 95% of gaze locations, mean across mice\n    value: 6.4\n    tolerance: 2.1\n    unit: degrees\n  - quantity: radius containing 95% of gaze locations, maximum across mice\n    value: 13.6\n    tolerance: 1.36\n    unit: degrees\n  criterion: Gaze positions in screen degrees from the AllenSDK gaze_mapping module (as the\n    Methods name it), frames with a valid ellipse fit; per mouse, the distance from the mean\n    gaze position below which 95% of frames fall; mean +/- SD and maximum across the mice with\n    processed eye tracking. The tolerance on the mean is the stated spread. Open detail, whether\n    the distance is radial (2D) or per axis; the readings are (a) radial, (b) the larger of the\n    azimuth and elevation 95th percentiles. Reproduced when, under one reading, both values are\n    within tolerance.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/000253/10.1038-s41586-020-03171-x.yaml paper/10.1038-s41586-020-03171-x.txt; echo EXIT $?; python - <<'E'
import yaml
d=yaml.safe_load(open('claims/000253/10.1038-s41586-020-03171-x.yaml'))
def walk(x,p=''):
    if isinstance(x,dict):
        for k,v in x.items(): walk(v,p+'.'+str(k))
    elif isinstance(x,list):
        for i,v in enumerate(x): walk(v,p+f'[{i}]')
    elif isinstance(x,str):
        for bad in [': ','—','rather']:
            if bad in x and not p.endswith('quote'): print(p,repr(bad))
walk(d)
print(len(d['claims']))
E
grep -n "—\|rather" claims/000253/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker passes: 35 claims, 35 quotes, 0 problems. Two quotes contain em dashes, which I'll cut out with "...". I'll also check the quotes for ": ".

**Agent calls Bash**

```bash
cd  f=claims/000253/10.1038-s41586-020-03171-x.yaml; python - <<'E'
p='claims/000253/10.1038-s41586-020-03171-x.yaml'
s=open(p).read()
s=s.replace("indicating that V1 neurons—on average—lead LM neurons","indicating that V1 neurons ... lead LM neurons")
s=s.replace("""  quote: Other aspects of neural activity during the task—including the baseline firing rate,
    response to the pre-change image and the response to the change image—were not correlated
    with hierarchy score""","""  quote: Other aspects of neural activity during the task ... including the baseline firing rate,
    response to the pre-change image and the response to the change image ... were not correlated
    with hierarchy score""")
open(p,'w').write(s)
import yaml
d=yaml.safe_load(s)
for c in d['claims']:
    if ': ' in c.get('quote',''): print(c['id'])
E
grep -c "—" $f; python tools/claims_check.py $f paper/10.1038-s41586-020-03171-x.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "
import yaml;d=yaml.safe_load(open('claims/000253/10.1038-s41586-020-03171-x.yaml'))
c=d['claims'];print(len(c),sum('statistics' in x for x in c),sum(len(x.get('statistics',[])) for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))
from collections import Counter;print(Counter(x.get('data','dataset') for x in c))"; git status --short
```

```
35 18 27 35 20
Counter({'elsewhere': 34, 'dataset': 1})
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
?? claims/000253/
?? scripts
```

**Agent**

I wrote `claims/000253/10.1038-s41586-020-03171-x.yaml`, and `tools/claims_check.py` passes it with 0 problems. But dandiset 000253 is probably not the paper's data. By its archive title and description it is the OpenScope Global/Local Oddball project (14 subjects, Neuropixels with optogenetics), recorded on the same pipeline, and it cites this paper only as "IsSupplementTo". The paper puts its 58 passive-viewing experiments in DANDI 000021 and 000022, and the Fig. 4 behaviour metrics in its GitHub repo. So 34 of the 35 claims are recorded as data `elsewhere`. Whether 000253 holds similar recordings (the same receptive-field mapping and flash stimuli, the same areas) is for the author to find.

**Text read**
- **Paper:** the NIH author manuscript in PubMed Central (PMC10399640), not the version of record. It has the main text, Methods, the Fig. 1–4 legends, the Extended Data Fig. 1–10 legends, and the data and code statements.
- **Missing:** there is no PDF, so no figure was seen. The Supplementary Information is not in the text, but the results rest on the main text, Methods and Extended Data, which are all there.
- **Code:** `AllenInstitute/neuropixels_platform_paper` at commit 4f8bcc2, plus the CCG helper `jiaxx/ccg_jitter` at 6559a4d, which the Figure 2 notebook calls. The code fixes the anatomical hierarchy scores, the unit selection, the log10 modulation index and the timescale filters; the text does not.

**Claims:** 35, all with quotes and all with criteria; 20 have expected values. 18 claims carry 27 statistics: Pearson correlations, Wilcoxon rank-sum tests (Fisher-combined across mice, or Benjamini–Hochberg corrected) and one bootstrap signed-rank test.

**Details left open, with the readings named**
- **Sharp-peak CCGs:**
  - Bin width: 1 ms, from the example in the code; the text gives no other reading.
  - CCG window: the 2 s presentation, or 3 s including the grey screen.
  - Unit quality filter: none, or the Extended Data Fig. 1j filters.
  - How the spontaneous period is cut into trials: 2 s or 3 s segments.
- **Directionality score across 25 mice:** pooled offsets, or the mean of each mouse's score. The total hierarchy score also has the area's own entry included or left out.
- **Distance control:** signed or absolute hierarchy-score difference.
- **Flash latency:** all flashes, dark only, or light only.
- **Modulation index:** mean of log10 MI (as the code does) or of raw MI.
- **Layer comparison:** difference of means or of medians; log10 or raw MI; the code's split (layer < 5, which may include layer 1) or layers 2/3 and 4 only.
- **Other counts and fractions:**
  - The 1.4% of hippocampal units with receptive fields: pooled over units, or the mean across mice.
  - Probe counts: whether 332 counts the probes of the 58 released sessions (the main reading) or of all 61 that passed quality control (a variant).
  - Baseline firing rate for the spontaneous-latency control: the rate in the grey interval, or the overall rate.
  - Gaze spread: radial, or the larger axis.
  - Hit rate and d′: averaged over sessions or over mice.
- **Decoders above chance:** mean minus s.e.m. above 0.5, or a one-sample t-test. Change modulation larger when active than passive: in every area, or in the mean over areas.
- **Exampled not identified:** the example mouse of Fig. 2d is not named, so every one of the 25 mice is a reading.

Where the Methods and the code disagree, the Methods give the main result and the code's choice is shown as a variant:
- the response decay window (0–250 ms against 40–290 ms);
- the window for the intrinsic timescale;
- the latency cutoff (250 against 500 ms);
- the jitter correction (expected value against one random resample).

**Missing for some claims**
- The change-modulation response window is not given, so that index cannot be recomputed from spikes; the claims use the paper's precomputed table.
- The behaviour sessions (hit rates, d′) have no deposit named in the paper.
- No p-values for the area pairs (Extended Data Fig. 9) or the distance-correlation values could be read, because the figures were not seen.

Nothing has been committed.

## End of run

35 turns, 8 minutes, result: success.
