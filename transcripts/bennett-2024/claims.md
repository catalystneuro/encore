# 001051 · claims · run 39844005630

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -50; ls claims/001453/ claims/001051/ 2>&1; ls paper/
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "limit": 170
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
[... 150 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/001453/10.1016-j.cub.2025.04.027.yaml"
}
```

```
1	# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.
2	# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read
3	# from its Results, figure legends and STAR Methods. The version of record is not open access.
4	#
5	# When these criteria were written, the author had seen the data check only: the file list,
6	# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and
7	# the extent of positions. No claim's analysis had been run. The author had also read the
8	# outputs printed in the paper's own analysis notebook (Fig1-S1.ipynb, GitLab commit 33a5c29),
9	# which include per-stimulus median speeds and angular velocities and its statistics.
10	#
11	# The dandiset holds only the freely swimming tracking data of Figure 1 and Figure S1. Its
12	# stimulus codes 0 to 20 carry no names. The names come from the paper's code and from the
13	# stimulus software's protocol file (see stimulus-code-link), so the claims that need them
14	# use outside data and depend on that claim.
15	#
16	# Method choices fixed here, from the paper's Fig1-S1.ipynb where the Methods are silent: a
17	# trial is one stim_index; tracked frames only; positions smoothed with a Savitzky-Golay filter
18	# (21 frames, order 2); trials rejected when the absolute cumulative heading change exceeds
19	# 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or the mean speed exceeds
20	# 100 mm/s; measures taken from 3 s to 35 s after the first frame (the 3 s stationary phase is
[... 302 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l paper/*.txt; head -30 paper/*.txt; grep -n -i "github\|zenodo\|dandi\|supplement\|figure s" paper/*.txt | head -60
```

Result: not kept, because it reads the paper's text.

**Agent**

The text includes Methods and supplement. Reading it in full.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2024.06.015.txt",
 "limit": 1080
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2024.06.015.txt",
 "offset": 1500,
 "limit": 660
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Full text, STAR Methods and supplement legends are present. Next, the linked code.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/AllenInstitute/SHIELD_Dynamic_Gating_Analysis 2>&1 | tail -3; cd SHIELD_Dynamic_Gating_Analysis 2>/dev/null && git log -1 --format='%H %cd' && find . -type f -not -path './.git/*' | head -100
```

```
3c09a0dc2972381f06393ddf5c000e16462c7037 Mon Jul 22 10:08:06 2024 -0700
./tutorials/dynamic_gating_quickstart.ipynb
./tutorials/dynamic_gating_lfp.ipynb
./tutorials/README.md
./metadata_tables/units_table.csv
./metadata_tables/probes_table.csv
./metadata_tables/master_stim_trials_table.csv
./metadata_tables/dynamic_gating_session_metadata.csv
./metadata_tables/channels_table.csv
./metadata_tables/VBN_units_table.csv
./metadata_tables/VBN_sessions.csv
./analysis_code/requirements.txt
./analysis_code/ccf_structure_tree_2017.csv
./analysis_code/batch_processing/vbn_utils.py
./analysis_code/batch_processing/run_rfs_dg.py
./analysis_code/batch_processing/run_rf_arrays.py
./analysis_code/batch_processing/run_im115_responses.py
./analysis_code/batch_processing/run_4Hz_bursts.py
./analysis_code/batch_processing/run_4Hz_analysis.py
./analysis_code/batch_processing/plot_utils.py
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/SHIELD_Dynamic_Gating_Analysis && wc -c analysis_code/*/* README.md tutorials/* | sort -n | tail -30; cat README.md analysis_code/batch_processing/README.md; head -3 metadata_tables/dynamic_gating_session_metadata.csv; wc -l metadata_tables/*.csv
```

```
106 tutorials/README.md
    624 analysis_code/batch_processing/README.md
   1173 README.md
   1195 analysis_code/batch_processing/run_rfs_dg.py
   1488 analysis_code/batch_processing/dg_plot_firing_rate_drift_over_session.py
   1746 analysis_code/batch_processing/run_rf_arrays.py
   2290 analysis_code/batch_processing/run_im115_responses.py
   2317 analysis_code/batch_processing/ccf_utils.py
   2348 analysis_code/analysis_notebooks/ccf_utils.py
   2483 analysis_code/batch_processing/make_dg_unit_tensor.py
   3078 analysis_code/batch_processing/run_4Hz_bursts.py
   3127 analysis_code/analysis_notebooks/lfp_filters.py
   3445 analysis_code/batch_processing/make_dg_unit_tensor_4Hz_events.py
   3547 analysis_code/analysis_notebooks/tensor_utils.py
   3970 analysis_code/batch_processing/analysis_utils.py
   4418 analysis_code/analysis_notebooks/analysis_utils.py
   4462 analysis_code/batch_processing/plot_utils.py
   6094 analysis_code/batch_processing/run_4Hz_analysis.py
  10678 analysis_code/batch_processing/vbn_utils.py
  20251 tutorials/dynamic_gating_quickstart.ipynb
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/SHIELD_Dynamic_Gating_Analysis/analysis_code && for nb in analysis_notebooks/*.ipynb; do python3 -c "
import json,sys
nb=json.load(open('$nb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    outs=''
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            if 'text' in o: outs+=''.join(o['text'])[:600]
            elif 'data' in o and 'text/plain' in o['data']: outs+=''.join(o['data']['text/plain'])[:400]
    print(f'## [{i}] {c[\"cell_type\"]}'); print(src); 
    if outs: print('>>OUT:',outs)
" > $TMPDIR/$(basename $nb .ipynb).txt; wc -l $TMPDIR/$(basename $nb .ipynb).txt; done
```

```
1014 /tmp/claude-1001/DynamicGating_4hz_analysis.txt
784 /tmp/claude-1001/DynamicGating_ephys_metrics.txt
Shell cwd was reset to
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/DynamicGating_ephys_metrics.txt"
}
```

```
1	## [0] code
2	from allensdk.brain_observatory.ecephys.dynamic_gating_ecephys_session import DynamicGatingEcephysSession
3	## [1] code
4	from matplotlib import pyplot as plt
5	import numpy as np
6	import pandas as pd
7	import os, glob
8	
9	import matplotlib as mpl
10	import os
11	from ccf_utils import *
12	mpl.rcParams['pdf.fonttype'] = 42
13	## [2] markdown
14	## Make Trial raster for example experiment
15	## [3] code
16	session = DynamicGatingEcephysSession.from_nwb_path(r"\\allen\programs\mindscope\workgroups\dynamicrouting\dynamic_gating\nwbs\1179670730\1179670730.nwb")
17	## [4] code
18	stimulus_presentations = session.stimulus_presentations
19	eye_tracking = session.eye_tracking
20	running_speed = session.running_speed
[... 765 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/DynamicGating_4hz_analysis.txt"
}
```

```
1	## [0] code
2	from allensdk.brain_observatory.ecephys.dynamic_gating_ecephys_session import DynamicGatingEcephysSession
3	## [1] code
4	from matplotlib import pyplot as plt
5	import numpy as np
6	import pandas as pd
7	import os, glob
8	import scipy.signal
9	import matplotlib as mpl
10	import os
11	mpl.rcParams['pdf.fonttype'] = 42
12	## [2] code
13	import ccf_utils
14	import analysis_utils
15	
16	%load_ext autoreload
17	%autoreload 2
18	## [3] code
19	structure_tree = pd.read_csv(r"..\ccf_structure_tree_2017.csv")
20	## [4] code
[... 995 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/SHIELD_Dynamic_Gating_Analysis/analysis_code && for f in batch_processing/run_4Hz_bursts.py batch_processing/run_4Hz_analysis.py batch_processing/analysis_utils.py analysis_notebooks/analysis_utils.py analysis_notebooks/tensor_utils.py batch_processing/run_rfs_dg.py batch_processing/run_rf_arrays.py batch_processing/make_dg_unit_tensor_4Hz_events.py batch_processing/make_dg_unit_tensor.py analysis_notebooks/lfp_filters.py; do echo "=== $f"; cat $f; done
```

```
<persisted-output>
Output too large (32.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/485c4096-8dc1-4ec0-91ba-1c4551a7c0ff/tool-results/bhriu2cgg.txt

Preview (first 2KB):
=== batch_processing/run_4Hz_bursts.py
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import argparse
from vbn_utils import *
from allensdk.brain_observatory.ecephys.dynamic_gating_ecephys_session import DynamicGatingEcephysSession

from ccf_utils import *
import analysis_utils
import plot_utils

save_dir = "/allen/programs/mindscope/workgroups/dynamicrouting/dynamic_gating/derived_table_info/4Hz_bursts/all_areas_using_minima_125window"
structure_tree = pd.read_csv('../ccf_structure_tree_2017.csv')

[... 42 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/485c4096-8dc1-4ec0-91ba-1c4551a7c0ff/tool-results/bhriu2cgg.txt"
}
```

```
1	=== batch_processing/run_4Hz_bursts.py
2	import matplotlib.pyplot as plt
3	import numpy as np
4	import pandas as pd
5	import os
6	import argparse
7	from vbn_utils import *
8	from allensdk.brain_observatory.ecephys.dynamic_gating_ecephys_session import DynamicGatingEcephysSession
9	
10	from ccf_utils import *
11	import analysis_utils
12	import plot_utils
13	
14	save_dir = "/allen/programs/mindscope/workgroups/dynamicrouting/dynamic_gating/derived_table_info/4Hz_bursts/all_areas_using_minima_125window"
15	structure_tree = pd.read_csv('../ccf_structure_tree_2017.csv')
16	
17	
18	def find_4Hz_bursts(session, save_location=save_dir):
19	
20	    sess_id = session.metadata['ecephys_session_id']
[... 841 more lines not kept]
```

**Agent**

Read the two notebooks and the batch scripts. Checking the remaining scripts, the RF columns in the repo's metadata tables, and the archive's description of the dataset.

**Agent calls Bash**

```bash
cd $TMPDIR/SHIELD_Dynamic_Gating_Analysis && cat analysis_code/batch_processing/run_im115_responses.py; grep -n "def \|p_value\|0\.0[15]" analysis_code/batch_processing/vbn_utils.py | head -40; head -1 metadata_tables/units_table.csv | tr ',' '\n' | nl | head -80; head -1 metadata_tables/master_stim_trials_table.csv
```

```
import numpy as np
import os
import argparse

from allensdk.brain_observatory.ecephys.dynamic_gating_ecephys_session import DynamicGatingEcephysSession

save_dir = '/allen/programs/mindscope/workgroups/dynamicrouting/dynamic_gating/derived_table_info/im115_r_responses'

def makePSTH(spikes, startTimes, windowDur, binSize=0.001):
    bins = np.arange(0,windowDur+binSize,binSize)
    counts = np.zeros(bins.size-1)
    for i,start in enumerate(startTimes):
        startInd = np.searchsorted(spikes, start)
        endInd = np.searchsorted(spikes, start+windowDur)
        counts = counts + np.histogram(spikes[startInd:endInd]-start, bins)[0]
    
    counts = counts/startTimes.size
    return counts/binSize, bins


[... 114 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/001051/ | python3 -c "import json,sys; d=json.load(sys.stdin); print(json.dumps({k:d.get(k) for k in ['identifier','draft_version','most_recent_published_version']},indent=1)[:1500])"; curl -s https://api.dandiarchive.org/api/dandisets/001051/versions/draft/info/ | python3 -c "import json,sys; d=json.load(sys.stdin); m=d['metadata']; print(m.get('name')); print(m.get('description')); print(m.get('version'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/SHIELD_Dynamic_Gating_Analysis/metadata_tables && python3 -c "
import pandas as pd
u=pd.read_csv('units_table.csv',usecols=['p_value_rf','is_sig_rf','quality','isi_label','structure_acronym'])
print(u['is_sig_rf'].value_counts(dropna=False))
s=u[u.is_sig_rf==True]['p_value_rf']; n=u[u.is_sig_rf==False]['p_value_rf']
print('sig max p',s.max(),'nonsig min p',n.min())
print(u['quality'].value_counts())
"; sed -n 1,3p probes_table.csv; cat ../tutorials/README.md
```

```
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import pandas as pd
ModuleNotFoundError: No module named 'pandas'
,Unnamed: 0,id,name,location,sampling_rate,lfp_sampling_rate,has_lfp_data,session,inserted
0,0,541,probeA,See electrode locations,30000.11232138625,,False,1232725697,True
1,1,543,probeB,See electrode locations,29999.93315139914,,False,1232725697,True
Folder that holds code for getting familiar with dynamic gating dataset and analysis performed on dataset
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/SHIELD_Dynamic_Gating_Analysis/metadata_tables && python3 -c "
import csv
r=csv.DictReader(open('units_table.csv'))
smax=-1;nmin=2;cnt={}
for row in r:
    k=row['is_sig_rf']; cnt[k]=cnt.get(k,0)+1
    try: p=float(row['p_value_rf'])
    except: continue
    if k=='True': smax=max(smax,p)
    elif k=='False': nmin=min(nmin,p)
print(cnt,'sig max p',smax,'nonsig min p',nmin)
"
```

```
{'False': 163661, 'True': 37859} sig max p 0.009 nonsig min p 0.01
Shell cwd was reset to
```

**Agent**

is_sig_rf in the repo's tables is p < 0.01, as the Methods say; the Fig 4E notebook uses 0.05. Now the checker and schema.

**Agent calls Bash**

```bash
sed -n 1,60p tools/claims_check.py; ls docs/ schema* 2>/dev/null; grep -rn "elsewhere\|with_inputs\|kind:" docs/*.md | head -20
```

```
"""Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

Validates the file against schemas/claims.schema.json, checks every quote word for word
(fragments split on "...", found in order) and looks for every recorded p-value and
confidence-interval bound in the text. The text may be plain text, HTML or JATS XML; several
files (a paper and its supplement) are searched together. A value printed in a form the
checker does not know (a garbled PDF glyph, "p = 0.04, 0.05 and 0.16") is reported, to be
confirmed by reading. Exits non-zero on any problem.
"""

from __future__ import annotations

import html
import re
import sys
import unicodedata
from pathlib import Path

[... 77 more lines not kept]
```

**Agent calls Bash**

```bash
cat schemas/claims.schema.json; sed -n 175,276p docs/protocol.md | grep -n -i "with_inputs\|with_labels\|elsewhere\|dataset"
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
[... 347 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 196,
 "limit": 60
}
```

```
196	   uses, show the difference.
197	4. Decide what comes from outside the dataset. Data from elsewhere may be
198	   used only when the claims file says the paper relies on it, it is public,
199	   and it is pinned: a DOI, or a repository at a commit. Record each under
200	   `inputs` in the attempt. A claim whose outside input is not public is
201	   blocked with `data_missing`, and its notes say where you looked.
202	
203	   The registry judges the dataset, so claims that use outside data are
204	   kept apart:
205	   - Each claim says what its test uses: `data: dataset` (the default),
206	     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
207	     `with_inputs` and `elsewhere` claims are counted apart, each group on
208	     its own; the others count towards what is said about the dataset.
209	   - `with_labels` is for outside sources that only name or map codes the
210	     dataset already holds, such as stimulus names for its stimulus codes.
211	     They bring in no measurements. A link claim must confirm the names, and
212	     the missing names are recorded as a finding (`metadata_insufficient`).
213	   - When outside data has to be matched to the dataset's cells, sessions
214	     or subjects, a claim of its own (`kind: link`) tests the link. Link
215	     claims are the registry's checks, not findings of the paper, so the
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1180,1240p paper/10.1016-j.neuron.2024.06.015.txt | grep -n -B2 -A3 "dandi\|^35\.\|^29\.\|^18\.\|^28\.\|^37\."
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^35\. \|^36\. \|^37\. \|^18\. \|^80\. \|^42\. " paper/10.1016-j.neuron.2024.06.015.txt; grep -n -A3 "^35\. " paper/10.1016-j.neuron.2024.06.015.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR/SHIELD_Dynamic_Gating_Analysis/analysis_code/batch_processing && cat dg_plot_firing_rate_drift_over_session.py; grep -n "def " plot_utils.py ccf_utils.py
```

```
import numpy as np
import pandas as pd
import os
import argparse

from allensdk.brain_observatory.ecephys.dynamic_gating_ecephys_session import DynamicGatingEcephysSession


import warnings
warnings.filterwarnings('ignore')
save_dir = "/allen/programs/mindscope/workgroups/dynamicrouting/dynamic_gating/firing_rate_drift"

def firing_rate_drift(session, save_dir=save_dir):
    
    session_id = session.metadata['ecephys_session_id']

    units = session.get_units()

    spike_times = session.spike_times

[... 40 more lines not kept]
```

**Agent**

Paper text is complete (version of record, STAR Methods, supplement legends S1 to S6). Code read: AllenInstitute/SHIELD_Dynamic_Gating_Analysis at commit 3c09a0d. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/001051/10.1016-j.neuron.2024.06.015.yaml",
 "content": "# Claims for Bennett, Ouellette, Ramirez et al. (2024), \"SHIELD: Skull-shaped hemispheric implants\n# enabling large-scale electrophysiology datasets in the mouse brain\", Neuron 112, 2869-2885, on\n# dandiset 001051.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-22, protocol\n# pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the version of record (PDF supplied by a person, extracted to paper/...txt), main text,\n# figure legends, STAR Methods (pages e1 to e8) and the supplemental information (legends of Figures\n# S1 to S6). The supplement holds figure legends only; its numbers are quoted from those legends.\n#\n# Code read: https://github.com/AllenInstitute/SHIELD_Dynamic_Gating_Analysis at commit 3c09a0dc\n# (2024-07-22; Zenodo doi:10.5281/zenodo.11494005 per the paper). It holds\n#   analysis_notebooks/DynamicGating_ephys_metrics.ipynb (Figures 1C, 4C to 4G, S4A; the list of 87\n#     sessions passing ephys QC in cell 26, the counts 25 mice, 87 experiments, 467 insertions),\n#   analysis_notebooks/DynamicGating_4hz_analysis.ipynb (Figures 7B to 7F and 8D to 8F),\n#   batch_processing/run_4Hz_bursts.py and run_4Hz_analysis.py (alpha-event detection, CCGs, PSTHs,\n#     pupil and running around events, random times), analysis_utils.py (event detector, CCG),\n#   make_dg_unit_tensor*.py (spike tensors for image flashes and VISp events), run_im115_responses.py\n#     (Figure 4G), run_rfs_dg.py (RF metrics via brain_observatory_utilities ReceptiveFieldMapping_VBN),\n#     dg_plot_firing_rate_drift_over_session.py (Figure S4I counts),\n#   metadata_tables/ (sessions, probes, channels, units with RF p values, and VBN units and sessions).\n# In units_table.csv the column is_sig_rf is p_value_rf < 0.01, as the Methods say. No code was found\n# for Figures 3 (surgery, MRI, histology, training), 4B trajectories, 5, 6, S3, S4B, S4D to S4H, or S6.\n#\n# Data the paper used, as it reports them. Electrophysiology in 27 mice (Methods, Mice): C57BL/6J\n# (n = 7), VGAT-ChR2 (n = 1), Sst-IRES-Cre;Ai32 (n = 14), Vip-IRES-Cre;Ai32 (n = 4), Vglut2-IRES-Cre\n# (n = 1); 18 males, 9 females. The behaving-mouse analyses use 25 mice, 87 experiments (sessions)\n# and 467 probe insertions (Discussion; code cell 34; the code's mice are 14 Sst;Ai32, 6 wild type,\n# 4 Vip;Ai32, 1 Ai32, 18 M and 7 F). Up to six Neuropixels 1.0 probes per session through a\n# single-hemisphere SHIELD implant over the left hemisphere, up to four consecutive recording days\n# per mouse (session types EPHYS_1 to EPHYS_4 in the code). Mice performed a visual change detection\n# task (8 natural images, 250 ms flash then 500 ms gray; lick on image change for water) and saw a\n# receptive-field mapping stimulus (20 degree Gabors on a 9 x 9 grid spaced 10 degrees, 3\n# orientations, 4 Hz, 0.08 cycles per degree, 250 ms, 15 repeats). Measured: spikes sorted with\n# Kilosort2 and unit quality metrics, unit CCF locations (cortical units relabelled from ISI maps),\n# LFP, running wheel speed, eye tracking (pupil) at 60 Hz, licks and rewards. Optogenetics used one\n# VGAT-ChR2 mouse (cortical silencing) and one Vglut2-Cre mouse with ChrimsonR in MRN, recorded with\n# Dura-Gel. Comparison data for the 5-mm window come from the Allen Visual Behavior Neuropixels (VBN)\n# dataset, DANDI:000713 version 0.240702.1725 (reference 29), used through VBN_units_table.csv and\n# VBN_sessions.csv in the code's metadata_tables; claims using it are with_inputs. Naive-mouse MRI\n# comes from Qiu et al. 2018 (reference 35). Surgery records, ISI maps, MRI, histology and training\n# histories are described but the dandiset's description (99 change-detection sessions with a\n# no-reward block, session and LFP NWBs) does not mention them; whether it holds them is for the\n# author to find.\n#\n# Shared method for the alpha-event claims (Figures 7, 8 and S6), from the Methods (Identification\n# of alpha events; Cross-correlograms and coherence; Quality metric criteria) and the code named.\n#   Units. QC criteria isi_violations < 0.5, amplitude_cutoff < 0.1, presence_ratio > 0.95, and not\n#     noise (quality good) (Methods; run_4Hz_bursts.py). Figure 8 code instead keeps presence_ratio >\n#     0.9 with no noise filter (tensor_utils.apply_good_units_filter); that is a variant.\n#   Area membership (open, readings L1 and L2). L1, the Methods, units labelled with the area (for\n#     cortex the ISI-based label supersedes the CCF label, Methods, Probe track annotation). L2, the\n#     code, units whose channel structure_acronym contains the area's acronym as a substring\n#     (region_psth uses str.contains, so VISp also takes VISpm, VISpl and VISpor).\n#   Population rate. Spikes of the area's units in 10 ms bins, averaged over units, smoothed with a\n#     symmetrical exponential filter of tau 10 ms (Methods; the code's filter is scipy's exponential\n#     window of 10 samples, tau 1 sample, symmetric, normalised to sum 1). Areas with fewer than 20\n#     units are excluded (Methods; the code requires more than 20, a variant).\n#   Candidate events. Local maxima of the inverted trace with scipy.signal.find_peaks, prominence 5,\n#     height -1, width 100 to 300 ms (Methods), searched in 1.25 s windows stepped by 0.25 s from time\n#     0 to the end of the last stimulus (code). Event rule (open, readings E1 and E2). E1, the\n#     Methods, at least four maxima at successive intervals between 125 and 350 ms in the window. E2,\n#     the code, a window with at least four maxima of which three successive maxima have both\n#     intervals in [125, 350) ms. The event time is the first of those maxima (code). A refractory\n#     period of 2 s follows each event (Methods, code).\n#   Qualifying events. The autocorrelogram of the area's population rate in a 2 s window centred on\n#     the event (Methods give 2 s for CCGs; the notebook's stored CCGs have 200 samples; the batch\n#     script in the repository uses 4 s, a variant), computed as scipy.signal.correlate (mode same)\n#     of the mean-subtracted traces divided by the square root of the product of their sums of\n#     squares (code crosscorrelogram), band-passed 3 to 7 Hz with a 2nd-order Butterworth filter run\n#     forward and back at 100 Hz, squared; the event is kept when the maximum exceeds 0.1 (Methods\n#     threshold; code get_qualifying_autoccgs).\n#   Random times. As many as the events, uniform between the start of the first and the end of the\n#     last active-behavior stimulus (code run_4Hz_analysis.py). The code sets no seed; any seed is a\n#     standard choice, and the result is to be shown for it.\n#   Coherence. Multi-taper coherence (nitime MTCoherenceAnalyzer, default settings) at 100 Hz on 4 s\n#     windows centred on each event (Methods), each trace mean-subtracted, the spectrum smoothed with\n#     a 4-bin boxcar (code); the 3 to 7 Hz band is the frequencies from the first at or above 3 Hz to\n#     the last below 7 Hz (code searchsorted). Random-time coherence is subtracted (Methods); how it\n#     is formed is open (readings R1 and R2). R1, the Methods read plainly, both areas at the same\n#     random time. R2, the code, the reference area at the event time against the other area at the\n#     random time.\n#   Pair test (Figure 7F legend; code cells 21 to 23). Sessions with more than 5 qualifying events;\n#     pairs with at least 25 pooled events; per pair the per-event band mean of (event minus random)\n#     coherence tested against zero with the Wilcoxon signed-rank test, Benjamini-Hochberg across the\n#     regions of each reference area, alpha 0.05.\n#   The code printed 50 sessions with 1653 qualifying VISp events and 14 sessions with 113 MOp\n#   events (cell 12). These are code outputs, not values the paper reports.\n#   Every alpha claim is judged under each combination of the open readings; when they disagree the\n#   claim is methods_underspecified.\n#\n# Session set. The Figure 4 analyses use the 87 sessions listed as passing ephys QC in\n# DynamicGating_ephys_metrics.ipynb cell 26; the paper names no list. The alpha analyses use every\n# session the batch scripts processed (no list in the code); readings are (a) the 87 sessions and\n# (b) all sessions in the dandiset.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001051\"\npaper: doi:10.1016/j.neuron.2024.06.015\nclaims:\n- id: fig3b-surgical-outcomes\n  statement: Of 106 mice entering SHIELD surgery, 79 passed all quality checks, 14 passed after a flag\n    that resolved and 13 failed, a final passing rate of 87.7%, on par with 90% (122 of 135) for the\n    earlier 5-mm cranial window surgery.\n  source: Results, Installation of SHIELD implant and QC evaluation, paragraph 3; Figure 3B\n  quote: Of the 106 mice entering surgery for this study, 79 passed all quality checks with no issues,\n    14 passed with a flag that eventually resolved, and 13 mice failed ... The final passing rate of\n    87.7% is on par with the success rate for our previous 5 mm cranial window surgery\n  expected:\n  - quantity: mice passing with no issues\n    value: 79\n    tolerance: 7.9\n  - quantity: mice passing after a resolved flag\n    value: 14\n    tolerance: 1.4\n  - quantity: mice failed\n    value: 13\n    tolerance: 1.3\n  - quantity: final passing rate\n    value: 87.7\n    tolerance: 8.77\n    unit: \"%\"\n  criterion: Counts of surgical outcomes from the paper's surgery records. The Methods list failures\n    as 4 detached headposts, 1 recurring seizures, 2 implant issues, 1 brain health, 3 unexpected\n    deaths (11, not 13); both totals are reported. The earlier-surgery rate (122 of 135) is from\n    references 18 and 28 and is not tested.\n- id: fig3c-isi-through-implant\n  statement: Intrinsic signal imaging through the implant maps the retinotopic boundaries of VISp and\n    many higher visual areas.\n  source: Results, Installation of SHIELD implant and QC evaluation, paragraph 4; Figure 3C\n  quote: We found that standard procedures successfully mapped retinotopic boundaries of VISp and many\n    higher visual cortical areas (Figure 3C)\n  criterion: Sign maps computed as in the Methods (Intrinsic signal imaging) from at least three\n    averaged trials show VISp and higher visual areas as contiguous regions. Shown in the paper by\n    example only; the paper gives no count of mice.\n- id: fig3d-histology-intact\n  statement: The implanted left hemisphere shows little GFAP activation or loss of DAPI and NeuN\n    staining compared with the unaltered right hemisphere (6 mice, 56 days after surgery).\n  source: Results, Installation of SHIELD implant and QC evaluation, paragraph 5; Figures 3D and S3E\n  quote: found little evidence of GFAP activation or cell loss, indicating that the implant did not\n    compromise the underlying tissue\n  criterion: The paper shows example sections only and reports no measure or test. Open. Readings\n    (a) visual comparison of the two hemispheres as in Figure 3D; (b) GFAP, DAPI and NeuN intensity or\n    cell density, implanted against control hemisphere per mouse, by the Wilcoxon signed-rank test\n    (the Methods' default paired test), reproduced when no difference at p < 0.05.\n- id: tracks-rare-bleeding\n  statement: Inserted probes rarely caused significant intracranial bleeding, in 3 of 547 tracks.\n  source: Results, Installation of SHIELD implant and QC evaluation, paragraph 5\n  quote: We found that inserted probes rarely caused significant intracranial bleeding (3/547 tracks).\n  expected:\n  - quantity: tracks with significant bleeding\n    value: 3\n    tolerance: 0.3\n  - quantity: tracks examined\n    value: 547\n    tolerance: 54.7\n- id: fig3fh-mri-deformation\n  statement: In MRI, the 5-mm cranial window deforms the brain under the window, while the brain\n    under SHIELD implants (250 and 400 micrometre inserts) is close to naive mice; the thicker insert\n    trended toward less deformation.\n  source: Results, Installation of SHIELD implant and QC evaluation, paragraphs 5 and 6; Figures 3F to\n    3H\n  quote: revealed clear brain deformation for the non-contoured 5-mm window over the visual cortex ...\n    the area between surface contours for SHIELD mice was more similar to naive mice ... though the\n    thicker design trended toward less deformation\n  statistics:\n  - test: Wilcoxon rank-sum test, area between contours summed over the 4 most posterior sections\n    p: 0.05\n    p_relation: \"<\"\n    corrected: Benjamini-Hochberg\n    n: naive 3, SHIELD 250 4, SHIELD 400 5, 5-mm window 5 mice\n  data: with_inputs\n  criterion: Area between the mirrored right and the left brain surface contours at ten coronal\n    planes, summed over the 4 most posterior, per mouse (Methods, Magnetic resonance imaging; Figure\n    3H legend). The naive volumes are from Qiu et al. 2018 (reference 35). The legend does not say\n    which pairs carry the asterisk; open. Readings (a) each implant group against naive; (b) all six\n    pairs. Reproduced when, after Benjamini-Hochberg, the 5-mm window group is larger than naive at p\n    < 0.05 and neither SHIELD group differs from naive at p < 0.05. The 250 against 400 trend is\n    reported only.\n- id: fig3i-learning-similar\n  statement: SHIELD mice and 5-mm window mice learn the change detection task at similar rates\n    (median sessions to criterion 12.5 against 14, p = 0.17).\n  source: Results, Installation of SHIELD implant and QC evaluation, paragraph 7; Figure 3I\n  quote: \"Mice with either implant had similar learning rates (Figure 3I; median number of sessions to\n    criterion: SHIELD 12.5 ± 2; 5-mm window 14 ± 3; p = 0.17, Wilcoxon rank-sum test)\"\n  statistics:\n  - test: Wilcoxon rank-sum test\n    p: 0.17\n  expected:\n  - quantity: SHIELD median sessions to criterion\n    value: 12.5\n    tolerance: 2\n  - quantity: 5-mm window median sessions to criterion\n    value: 14\n    tolerance: 3\n  data: with_inputs\n  criterion: A claim of absence, judged on the paper's test, a Wilcoxon rank-sum test of sessions to\n    criterion between the groups at p < 0.05; reproduced when it is not significant. Criterion and\n    training stages as in references 36 and 37. The paper does not say where the 5-mm window mice's\n    training records are, nor how many mice each group has. Tolerances are the paper's stated\n    spread.\n- id: fig4b-units-areas-per-session\n  statement: A typical 6-probe session records 1,821 non-noise units (SD 341.9) from 28.1 areas (SD\n    5.1).\n  source: Results, High-quality multi-Neuropixels recordings, paragraph 2; Figure 4B\n  quote: we recorded activity from over 1,800 units spanning ... 25 brain areas (this includes all\n    non-noise units, as described in STAR Methods; 1,821 ± 341.9 units; 28.1 ± 5.1 areas, mean ± SD\n  expected:\n  - quantity: non-noise units per 6-probe session, mean\n    value: 1821\n    tolerance: 341.9\n  - quantity: areas per 6-probe session, mean\n    value: 28.1\n    tolerance: 5.1\n  criterion: As in DynamicGating_ephys_metrics.ipynb cells 36 to 39, over the 87 QC-passing sessions.\n    Units in an annotated area (structure_acronym not No Area, out of brain or Track not annotated);\n    6-probe sessions are those whose such units come from exactly six probes; units counted are\n    non-noise (quality good); areas counted are distinct structure_acronym values among all such\n    units. Mean and SD across sessions. Tolerances are the paper's stated SD.\n- id: figs4ab-insertions-per-mouse\n  statement: Across recording days each mouse received about 20 probe insertions (SD 4.1) into about\n    10 implant holes (10.4, SD 2.3).\n  source: Results, High-quality multi-Neuropixels recordings, paragraph 2; Figures S4A and S4B\n  quote: we typically made ... probe insertions (20 ± 4.1, mean ± SD; Figure S4A) targeting ... implant\n    holes (10.4 ± 2.3, mean ± SD; Figure S4B)\n  expected:\n  - quantity: insertions per mouse, mean\n    value: 20\n    tolerance: 4.1\n  - quantity: implant holes targeted per mouse, mean\n    value: 10.4\n    tolerance: 2.3\n  criterion: Insertions per mouse are the distinct probe insertions with units across the mouse's\n    QC-passing sessions (code cell 32, distinct probe_id per mouse_id). Holes per mouse need the\n    implant hole of each insertion; no code. Tolerances are the paper's stated SD.\n- id: scale-mice-sessions-insertions\n  statement: Stable recordings were made from 25 mice in 87 experiments with 467 probe insertions.\n  source: Discussion, paragraph 2\n  quote: high-quality recordings from 25 mice, totaling 87 experiments and 467 probe insertions\n  expected:\n  - quantity: mice\n    value: 25\n    tolerance: 2.5\n  - quantity: experiments\n    value: 87\n    tolerance: 8.7\n  - quantity: probe insertions\n    value: 467\n    tolerance: 46.7\n  criterion: Counted over the 87 QC-passing sessions of code cell 26 (code cell 34). The dandiset's\n    description lists 99 sessions; the 12 others are reported.\n- id: penetration-success\n  statement: On average 5.46 of the 6 intended probes per session were successfully inserted.\n  source: STAR Methods, Neuropixels recordings, Probe insertion, paragraph 2\n  quote: Overall, we achieved a penetration success of 5.46 probes per session\n  expected:\n    quantity: probes inserted per session, mean\n    value: 5.46\n    tolerance: 0.546\n  criterion: Insertions with recorded units divided by sessions. The code's counts give 467 over 87\n    (5.37); which insertions or sessions give 5.46 is not stated. Readings (a) over the 87 QC-passing\n    sessions; (b) over all sessions in the dandiset.\n- id: fig4b-trajectory-consistency\n  statement: Insertions along the same trajectory (same hole and probe orientation) enter the brain at\n    similar CCF locations, with a median absolute deviation of 150 micrometres medial-lateral and 200\n    micrometres anterior-posterior over 15 trajectories.\n  source: Results, High-quality multi-Neuropixels recordings, paragraph 3; Figure 4B\n  quote: for 15 unique trajectories, we found the median absolute deviation in CCF coordinates was 150\n    mm in the medial-lateral axis and 200 mm in the anterior-posterior axis\n  expected:\n  - quantity: unique trajectories\n    value: 15\n    tolerance: 1.5\n  - quantity: median over trajectories of the medial-lateral median absolute deviation\n    value: 150\n    tolerance: 15\n    unit: micrometre\n  - quantity: median over trajectories of the anterior-posterior median absolute deviation\n    value: 200\n    tolerance: 20\n    unit: micrometre\n  criterion: Per trajectory, the median absolute deviation across its insertions of the entry\n    point's CCF coordinate; the median across trajectories. No code. How the entry point is located\n    is open. Readings (a) the CCF coordinate of the most superficial channel in a brain structure;\n    (b) the most superficial channel with units. Which insertions share a trajectory needs the hole\n    and orientation of each insertion.\n- id: fig4c-drift-discontinuities-rare\n  statement: Discontinuous or abrupt shifts in unit depth in the drift map occurred in 5.1% of\n    insertions (23 of 454).\n  source: Results, High-quality multi-Neuropixels recordings, paragraph 4; Figure 4C\n  quote: We rarely observed discontinuous or abrupt shifts in the depth of units in the drift map (5.1%\n    of insertions; 23/ 454)\n  expected:\n  - quantity: fraction of insertions with discontinuous shifts\n    value: 5.1\n    tolerance: 0.51\n    unit: \"%\"\n  - quantity: insertions examined\n    value: 454\n    tolerance: 45.4\n  criterion: The paper judged drift maps by eye and gives no rule for an abrupt shift, and no code.\n    Open; the only reading the paper allows is inspection of drift maps (unit depth against time,\n    marker intensity by amplitude).\n- id: fig4d-unit-drift\n  statement: Unit drift with SHIELD is only slightly higher than with the 5-mm window (median 25.1\n    against 22.82 micrometres).\n  source: Results, High-quality multi-Neuropixels recordings, paragraph 4; Figure 4D\n  quote: \"found it was only slightly higher than that observed in our previous recordings using the\n    5-mm insertion window method (SHIELD: 25.1 ± 0.1 mm, 5-mm window: 22.82 ± 0.05; median ± SEM\"\n  expected:\n  - quantity: SHIELD median unit drift\n    value: 25.1\n    tolerance: 0.1\n    unit: micrometre\n  - quantity: 5-mm window median unit drift\n    value: 22.82\n    tolerance: 0.05\n    unit: micrometre\n  data: with_inputs\n  criterion: The max_drift metric of all non-noise units (quality good) of the 87 QC-passing sessions\n    (143,828 units) against VBN non-noise units (262,177), as in code cells 41 and 46; median of each.\n    Tolerances are the paper's SEM. VBN units come from DANDI:000713 (reference 29).\n- id: fig4d-qc-metrics-comparable\n  statement: The distributions of unit quality metrics (presence ratio, amplitude cutoff, ISI\n    violations, SNR, isolation distance, drift, amplitude) are comparable for SHIELD and the 5-mm\n    window.\n  source: Results, High-quality multi-Neuropixels recordings, paragraph 5; Figure 4D\n  quote: We found that the distribution of QC metrics was comparable with both surgical preparations\n    (Figure 4D).\n  data: with_inputs\n  criterion: Non-noise units as in fig4d-unit-drift, seven metrics as in code cell 46. The paper\n    reports no test or measure of comparability. Open. Readings (a) the code's two-sided Mann-Whitney\n    U test per metric (its printed output gives p = 1.4e-156 for presence ratio and 6.0e-18 for\n    amplitude cutoff), comparable when not significant at 0.05; (b) each SHIELD median within 10% of\n    the 5-mm window median. Both readings are run and every median and p value shown.\n- id: qc-pass-fraction-similar\n  statement: The fraction of units passing the standard quality filter is very similar for SHIELD\n    (41.1%) and the 5-mm window (40.7%).\n  source: Results, High-quality multi-Neuropixels recordings, paragraph 5\n  quote: \"the percentage of units passing our standard quality metrics filter (see STAR Methods) was\n    very similar for the SHIELD versus 5-mm window implants (% units passing quality metrics criteria:\n    SHIELD: 41.1, 5-mm window: 40.7)\"\n  expected:\n  - quantity: SHIELD units passing QC, percent of non-noise units\n    value: 41.1\n    tolerance: 4.11\n    unit: \"%\"\n  - quantity: 5-mm window units passing QC, percent of non-noise units\n    value: 40.7\n    tolerance: 4.07\n    unit: \"%\"\n  data: with_inputs\n  criterion: Passing means isi_violations < 0.5, amplitude_cutoff < 0.1 and presence_ratio > 0.95\n    (Methods), as a fraction of non-noise units (code cell 42).\n- id: fig4e-unit-yield-stable\n  statement: About 300 units are recorded per probe on each day, and unit yield does not differ\n    across the four recording days with SHIELD (p = 0.48).\n  source: Results, High-quality multi-Neuropixels recordings, paragraph 6; Figure 4E\n  quote: On each recording day, we measured the activity of roughly 300 units from each probe (Figure\n    4E). ... unit yield was not significantly different across days for SHIELD mice (p = 0.48,\n    Kruskal-Wallis H test)\n  statistics:\n  - test: Kruskal-Wallis H test\n    p: 0.48\n    n: 129, 126, 121 and 91 insertions on days 1 to 4\n  expected:\n    quantity: median non-noise units per insertion, each day\n    value: 300\n    tolerance: 30\n  criterion: Non-noise units per insertion (mouse, probe and session type EPHYS_1 to EPHYS_4), over the\n    87 QC-passing sessions, as in code cells 48 and 49. A claim of absence, judged on the paper's\n    Kruskal-Wallis test across the four days at p < 0.05; reproduced when not significant and each\n    day's median is within tolerance. The insertion counts in the figure are 129, 126, 121, 91.\n- id: fig4e-vbn-yield-drops\n  statement: With the 5-mm window, unit yield decreased on the second recording day (p = 6e-22).\n  source: Results, High-quality multi-Neuropixels recordings, paragraph 6; Figure 4E\n  quote: In contrast to the 5-mm window preparation, for which unit yield decreased on the second\n    recording day (p = 6e–22, Kruskal-Wallis H test)\n  statistics:\n  - test: Kruskal-Wallis H test\n    p: 6.0e-22\n    n: 459 and 446 VBN insertions on days 1 and 2\n  data: with_inputs\n  criterion: VBN non-noise units per insertion by session number (code cell 47). The code's p =\n    6e-22 is a Kruskal-Wallis test over six groups (two VBN days and four SHIELD days, cell 51), not\n    VBN day 1 against day 2. Readings (a) VBN day 1 against day 2; (b) the code's six groups.\n    Reproduced when p < 0.05 under a reading and the VBN day-2 median is below day 1.\n- id: fig4e-firing-rate-stable\n  statement: The average firing rate of recorded units is similar across the four recording days (p\n    = 0.21).\n  source: Results, High-quality multi-Neuropixels recordings, paragraph 6; Figure 4E\n  quote: Additionally, the average firing rate of recorded units was similar across days (p = 0.21\n    Kruskal-Wallis H test).\n  statistics:\n  - test: Kruskal-Wallis H test\n    p: 0.21\n    n: 23, 24, 22 and 18 sessions on days 1 to 4\n  criterion: Per session the median firing rate of non-noise units; Kruskal-Wallis across session\n    types EPHYS_1 to EPHYS_4 (code cells 54 and 55). A claim of absence on that test; reproduced when\n    p >= 0.05. The code's output and the figure give p = 0.26, the text 0.21; both are reported.\n- id: fig4ef-rf-fraction-stable\n  statement: A consistent fraction of VISp units has significant spatial receptive fields on each of\n    the four recording days (p = 0.38).\n  source: Results, High-quality multi-Neuropixels recordings, paragraph 7; Figures 4E and 4F\n  quote: we measured a consistent fraction of units with well-defined spatial receptive fields (RFs)\n    (Figure 4E and 4F; p = 0.38 Kruskal-Wallis H test)\n  statistics:\n  - test: Kruskal-Wallis H test\n    p: 0.38\n    n: 12, 11, 12 and 11 sessions on days 1 to 4\n  criterion: Per session the fraction of QC-passing units labelled VISp (ISI label) whose receptive\n    field is significant, a chi-square test on the 9 x 9 spike-count map at p < 0.01 (Methods,\n    Receptive Field Mapping; the code's units table uses 0.01); Kruskal-Wallis across days. The\n    Figure 4E code uses p < 0.05 (cell 58); shown as a variant. A claim of absence; reproduced when\n    p >= 0.05 under the Methods threshold.\n- id: fig4f-rf-match-retinotopy\n  statement: VISp receptive fields recorded through adjacent holes on successive days lie where the\n    ISI-based retinotopic map predicts.\n  source: Results, High-quality multi-Neuropixels recordings, paragraph 7; Figure 4F\n  quote: the region of visual space preferred on each day matched the expected location indicated by\n    the ISI-based retinotopic map\n  criterion: Shown for one example mouse. Open; the paper gives no measure. Reading, the RF centres of\n    significant VISp units per day move across days in the direction of the retinotopic axes given\n    by the insertion sites (nasal to temporal with anterior to posterior is not stated in the text;\n    the figure's axes are used). Requires the ISI maps.\n- id: fig4g-visual-responses-similar\n  statement: The population response of VISp units to an image is highly similar across the four\n    recording days.\n  source: Results, High-quality multi-Neuropixels recordings, paragraph 7; Figure 4G\n  quote: In addition, the stimulusevoked temporal dynamics were highly similar across the 4 recording\n    days (Figure 4G).\n  expected:\n  - quantity: VISp units with significant RF, day 1\n    value: 595\n    tolerance: 59.5\n  - quantity: VISp units with significant RF, day 2\n    value: 482\n    tolerance: 48.2\n  - quantity: VISp units with significant RF, day 3\n    value: 536\n    tolerance: 53.6\n  - quantity: VISp units with significant RF, day 4\n    value: 446\n    tolerance: 44.6\n  criterion: Units with significant RFs labelled VISp, PSTHs at 1 ms to active-behavior presentations\n    of image im115_r (run_im115_responses.py; that script keeps presence_ratio > 0.9 and\n    ephys_metrics cell 64 then applies the 0.95 filter); day means baseline-subtracted by the 10 ms\n    before onset and divided by their maximum (cell 66). The paper gives no measure of similarity.\n    Open. Readings take the paper's test for stability across days (Kruskal-Wallis, Figure 4E) on\n    per-unit (a) mean baseline-subtracted response 0 to 250 ms and (b) time of peak response 0 to\n    250 ms; reproduced when neither differs across days at p < 0.05.\n- id: behavior-stable-across-days\n  statement: Task performance is stable across the four recording days despite repeated insertions\n    (median rewards 59.5, 63.5, 56.5, 60.5; p = 0.96).\n  source: Results, High-quality multi-Neuropixels recordings, paragraph 8\n  quote: \"we found that mouse behavioral performance on the visual task was stable across the 4\n    recording days despite repeated probe insertions (median rewards received: day 1, 59.5; day 2,\n    63.5; day 3, 56.5; day 4, 60.5; Kruskal-Wallis test: p = 0.96)\"\n  statistics:\n  - test: Kruskal-Wallis test\n    p: 0.96\n  expected:\n  - quantity: median rewards received, day 1\n    value: 59.5\n    tolerance: 5.95\n  - quantity: median rewards received, day 2\n    value: 63.5\n    tolerance: 6.35\n  - quantity: median rewards received, day 3\n    value: 56.5\n    tolerance: 5.65\n  - quantity: median rewards received, day 4\n    value: 60.5\n    tolerance: 6.05\n  criterion: Rewards per session, median across sessions of each session type EPHYS_1 to EPHYS_4,\n    Kruskal-Wallis across days; a claim of absence, reproduced when p >= 0.05. No code. Which rewards\n    count is open. Readings (a) all rewards delivered; (b) rewards earned by hits, auto-rewards left\n    out. Sessions are the 87 QC-passing ones; all sessions as a variant.\n- id: figs4i-insertion-suppression\n  statement: Activity is transiently suppressed after probe insertion and recovers with a time\n    constant of 25 to 30 minutes.\n  source: STAR Methods, Neuropixels recordings, Probe insertion, paragraph 1; Figure S4I\n  quote: we find that activity is transiently suppressed directly after probe insertion and gradually\n    recovers with a time constant of 25-30 minutes (Figure S4I)\n  expected:\n    quantity: recovery time constant\n    value: 27.5\n    tolerance: 5.5\n    unit: minute\n  criterion: Reported as the range 25 to 30 min; the claim holds inside 22.5 to 33 min. Spikes of\n    QC-passing non-noise units summed in 1 s bins from the first stimulus onset per session\n    (dg_plot_firing_rate_drift_over_session.py); the S4I legend plots the mean change across 85\n    SHIELD experiments. The normalisation and fit are not given. Open. Readings (a) each session's\n    rate divided by its mean, averaged across sessions, fitted with a - b exp(-t / tau); (b) the\n    same with rates divided by the mean of the last 10 minutes. The 5-mm comparison (103 experiments)\n    needs VBN data and is a variant.\n- id: figs4de-retraction-reduces-drift\n  statement: Retracting probes 100 micrometres after insertion reduces unit drift (unit means 24.48\n    against 30.25 micrometres; session means 24.23 against 30.56).\n  source: Figure S4D and S4E legends; STAR Methods, Probe insertion, paragraph 1\n  quote: Units from sessions where probes were retracted had lower drift (mean = 24.48 μm) than those\n    from sessions where probes were not retracted (mean = 30.25 μm; Kolmogrov-Smirnov test, p < .001)\n  statistics:\n  - about: unit drift, retracted against not retracted sessions\n    test: Kolmogorov-Smirnov test\n    p: 0.001\n    p_relation: \"<\"\n    n: 25,896 and 76,851 units\n  expected:\n  - quantity: mean unit drift, retracted sessions\n    value: 24.48\n    tolerance: 2.448\n    unit: micrometre\n  - quantity: mean unit drift, not retracted\n    value: 30.25\n    tolerance: 3.025\n    unit: micrometre\n  - quantity: mean of session drift, retracted sessions (n = 23)\n    value: 24.23\n    tolerance: 2.423\n    unit: micrometre\n  - quantity: mean of session drift, not retracted (n = 60)\n    value: 30.56\n    tolerance: 3.056\n    unit: micrometre\n  criterion: Which sessions were retracted (23 per the Methods) must be found in the dandiset. The\n    drift measure is the legend's point-to-point drift per unit over the session; open. Readings (a)\n    max_drift; (b) cumulative_drift. The unit set (102,747 units over 83 sessions) is smaller than\n    all non-noise units; readings (a) QC-passing units; (b) non-noise units. Reproduced when the KS\n    test gives p < 0.001 with retracted lower, and the means are within tolerance.\n- id: figs4f-retraction-yield-similar\n  statement: Retracted and non-retracted sessions record similar numbers of good units (means 1125\n    against 1280, p = 0.318).\n  source: Figure S4F legend\n  quote: Number of good units recorded per session is similar across retracted and non-retracted\n    sessions. ... Distributions did not differ significantly (Kolmogrov-Smirnov test, p = 0.318).\n  statistics:\n  - test: Kolmogorov-Smirnov test\n    p: 0.318\n  expected:\n  - quantity: mean good units per session, retracted\n    value: 1125\n    tolerance: 112.5\n  - quantity: mean good units per session, not retracted\n    value: 1280\n    tolerance: 128\n  criterion: A claim of absence on the paper's KS test at p < 0.05. Good units read as (a)\n    QC-passing units (Methods); (b) non-noise units.\n- id: figs4gh-sharpened-probes\n  statement: Sharpened probes show drift comparable to unsharpened probes and a lower insertion\n    failure rate (p = 0.0004).\n  source: Figure S4G and S4H legends\n  quote: Sharpened Neuropixels probes show comparable drift to unsharpened probes. ... Sharpened\n    Neuropixels probes have a lower insertion fail rate than unsharpened probes (p = 0.0004, Fisher’s\n    exact test).\n  statistics:\n  - about: insertion failure rate, sharpened against unsharpened\n    test: Fisher's exact test\n    p: 0.0004\n    n: 32 insertions before and 112 after sharpening\n  criterion: Needs which probes were sharpened and the failed insertion attempts; no code. Drift\n    comparison has no test in the paper; reported as medians (21,894 and 80,673 units).\n- id: figs3d-duragel-yield-stable\n  statement: Dura-Gel can stay on the implant for at least 2 weeks without visible brain deterioration\n    or a drop in unit yield.\n  source: Results, Dual-hemisphere SHIELD implant, paragraph 2; Figures S3B and S3D\n  quote: Dura-Gel can remain in place for at least 2 weeks without visible signs of brain\n    deterioration (Figure S3B) or a drop in unit yield (Figure S3D).\n  criterion: A claim of absence on the paper's test, the Wald test for a nonzero slope of unit yield\n    against days since Dura-Gel application over 24 insertions (S3D legend); reproduced when the\n    slope is not significantly negative at p < 0.05. The unit set for yield is not stated; readings\n    (a) non-noise units; (b) QC-passing units.\n- id: fig5-bilateral-recordings\n  statement: Simultaneous Neuropixels recordings from both hemispheres are feasible with the\n    dual-hemisphere implant.\n  source: Results, Dual-hemisphere SHIELD implant, paragraph 1; Figures 5C and 5D\n  quote: In preliminary experiments, we demonstrate the feasibility of simultaneous, bilateral\n    Neuropixels recordings with the SHIELD method (Figures 5C and 5D).\n  criterion: Reproduced when a session recorded through a dual-hemisphere implant has units on probes\n    in both hemispheres (cortex and striatum, Figure 5D). Two sessions in the paper.\n- id: fig6bc-cortical-silencing\n  statement: Blue light through the implant in a VGAT-ChR2 mouse silences visually evoked activity of\n    VISp regular-spiking units at the recording site, with activity near baseline 2 mm away, and the\n    effect depends on distance and power.\n  source: Results, SHIELD is compatible with optogenetics, paragraph 2; Figures 6B and 6C\n  quote: Stimulusevoked activity of regular spiking (RS) units in VISp was silenced when a 2-mW laser\n    spot was targeted to the recording location but returned to near baseline at a distance of 2 mm\n    (Figure 6B). The dependence of this silencing effect on distance and laser power (Figure 6C)\n  criterion: RS units are VISp units with peak-to-trough duration > 0.4 ms; laser at 1, 2 and 12 mW\n    at 0, 0.5, 1 and 2 mm anterior, with a 500 ms grating (Methods, Optogenetic silencing). The\n    measure is not given. Open. Readings (a) mean rate in the 500 ms stimulus window; (b) the same\n    minus the pre-stimulus rate. Reproduced when, with 2 mW at 0 mm, the RS population response is\n    below the no-laser response by the Wilcoxon signed-rank test across units (the Methods' default\n    paired test) at p < 0.05, and at 2 mm it is not different at p < 0.05; the dependence on\n    distance and power is reported.\n- id: fig6ef-optotagging-mrn\n  statement: Red light through the implant evokes reliable short-latency spikes from ChrimsonR-tagged\n    Vglut2 midbrain units, found up to 4 mm below the brain surface.\n  source: Results, SHIELD is compatible with optogenetics, paragraph 3; Figures 6E and 6F\n  quote: Photo-stimulation with pulses (10 ms) of red light (638 nm) evoked reliable, short-latency\n    spiking responses from units recorded in the midbrain (Figure 6E). Such optotagged units were found\n    up to 4 mm below the surface of the brain\n  expected:\n    quantity: depth of the deepest tagged unit below the brain surface\n    value: 4\n    tolerance: 0.4\n    unit: mm\n  criterion: Tagged units show a significant increase (p < 0.05) in rate during all five 10 ms pulses\n    at 20 Hz (Methods, Optotagging in the midbrain); the test is not named; open. Readings (a)\n    Wilcoxon signed-rank across trials of the count in each pulse against an equal pre-train window\n    (the Methods' default paired test); (b) the same on the 10 ms after each pulse onset. Reproduced\n    when tagged units exist and the deepest is within tolerance.\n- id: fig7a-mop-higher-frequency\n  statement: VISp alpha events are rhythmic at 3 to 5 Hz, and MOp events occur in a slightly higher\n    band, 5 to 7 Hz.\n  source: Results, SHIELD recordings reveal multi-regional subnetworks, paragraphs 3 and 4; Figure 7A\n  quote: we observed rhythmic 3–5 Hz waves of activity in VISp (Figure 7A, left) ... These MOp\n    alpha-like events occurred in a slightly higher frequency band (5–7 Hz)\n  criterion: Qualifying events as in the header. No method is given for the frequency. Open. Readings\n    (a) the inverse of the median interval between successive detected maxima in each event; (b) the\n    peak frequency of the event's autocorrelogram spectrum. Reproduced when, under a reading, the\n    median VISp frequency lies in 2.7 to 5.5 Hz, the median MOp frequency in 4.5 to 7.7 Hz (the\n    ranges widened by 10% of each bound), and MOp is higher by the Wilcoxon rank-sum test (the\n    Methods' default unpaired test) at p < 0.05.\n- id: fig7b-low-arousal\n  statement: VISp and MOp alpha events occur when the mouse is immobile and the pupil constricted,\n    with pupil diameter about 25% smaller than at random session times.\n  source: Results, SHIELD recordings reveal multi-regional subnetworks, paragraph 5; Figure 7B\n  quote: VISp and MOp events tended to occur during periods of lower arousal, when the animal was\n    immobile and the pupil was constricted (during alpha events, pupil diameter was ... 25% smaller\n    relative to randomly chosen session times)\n  expected:\n    quantity: change in pupil size during events relative to random times\n    value: -25\n    tolerance: 2.5\n    unit: \"%\"\n  criterion: As in DynamicGating_4hz_analysis.ipynb cells 13 to 15, on qualifying events (header).\n    Pupil (blinks removed) and running speed resampled at 10 ms with forward fill; event value the\n    mean over 0 to 1 s after event onset, windows with fewer than 1000 samples dropped. Pupil change\n    is (event value minus the session's mean over random times) over that mean, pooled over events,\n    Wilcoxon signed-rank against zero; running at events against running at random times by the\n    Wilcoxon rank-sum test (code). The code uses pupil area while the text says diameter; open.\n    Readings (a) pupil area; (b) diameter, the square root of area. The summary of the pooled\n    changes is not stated; readings (c) mean; (d) median. Reproduced, for each of VISp and MOp, when\n    pupil is smaller and running lower at events at p < 0.05 and the VISp change is within tolerance\n    under a reading.\n- id: fig7b-visp-offset-locked\n  statement: VISp alpha events are often triggered by the offset of visual stimuli, while the timing\n    of MOp events is not related to visual stimuli.\n  source: Results, SHIELD recordings reveal multi-regional subnetworks, paragraph 5; Figure 7B, right\n  quote: The VISp events were often triggered by the offset of visual stimulation (Figure 7B) ... The\n    timing of MOp events was not related to visual stimuli (Figure 7B).\n  criterion: As in code cell 12, for each qualifying event the last stimulus presentation starting\n    before it; onset minus that stimulus's end time, histogram 0 to 0.5 s in 50 ms bins. The paper\n    reports no test. Open. Readings (a) chi-square goodness of fit of the ten bins against uniform;\n    (b) Kolmogorov-Smirnov against uniform on [0, 0.5) s. Reproduced when, under a reading, VISp\n    differs from uniform at p < 0.05 with the largest bin in the first 250 ms after offset, and MOp\n    does not differ at p < 0.05.\n- id: figs6-replay\n  statement: Activity during post-stimulus VISp alpha events is correlated with activity during the\n    preceding stimulus (r = 0.77, p = 1.8e-6), as if events replay recent stimulation.\n  source: Results, SHIELD recordings reveal multi-regional subnetworks, paragraph 5; Figure S6\n  quote: Activity during post-stimulus alpha events was weakly but significantly correlated with\n    activity during the preceding stimulus, indicating that alpha events tend to replay recent sensory\n    stimulation (Figure S6; r = 0.77\n  statistics:\n  - test: correlation\n    statistic: r = 0.77\n    p: 1.8e-6\n  expected:\n    quantity: correlation of stimulus tuning and alpha-event tuning\n    value: 0.77\n    tolerance: 0.077\n  criterion: No code. Per S6 legends, for each VISp unit the mean response to each of the four stimuli\n    of the session and the response during the alpha event following each stimulus (event assigned\n    to the last stimulus before it, as in code cell 12); rows normalised; per session the column\n    average over units; Pearson correlation across sessions with four points per session (S6F inset).\n    Open details and readings. Evoked window (a) 0 to 250 ms after onset (image duration, Methods);\n    (b) 0 to 500 ms. Event window (c) 0 to 1 s after onset (as the code's pupil window); (d) the\n    event's 1.25 s detection window. Which four stimuli is not stated; the sessions' stimulus names\n    must show it. A per-unit correlation (S6E) is shown as a variant.\n- id: fig7cd-visp-coupling\n  statement: During VISp events, VISp is tightly coupled to LP and VISl (sharp CCG peaks near zero lag\n    and a 3 to 7 Hz coherence peak), but not to PO or SSp.\n  source: Results, SHIELD recordings reveal multi-regional subnetworks, paragraph 6; Figures 7C and 7D\n  quote: During VISp events, VISp activity was tightly coupled to the secondary visual thalamus (LP)\n    and higher-order lateral visual cortex (VISl), as evidenced by sharp peaks in the CCG at near-zero\n    lag. VISp was not strongly coupled to somatosensory thalamus (PO) or SSp. Indeed, coherence\n    analysis revealed a prominent peak in the 3–7 Hz band between VISp population spiking activity and\n    LP and VISl, but not PO or SSp (Figure 7D)\n  criterion: Header method. Coherence part, the pair test, reproduced when VISp-LP and VISp-VISl are\n    significant with positive band coherence and VISp-PO and VISp-SSp are not (the absence on the\n    same test). CCG part, the mean of event CCGs pooled across sessions; near zero is not defined;\n    open. Readings (a) peak within 20 ms of zero lag; (b) within 50 ms. Reproduced when the CCG\n    peaks of LP and VISl lie near zero and are higher than those of PO and SSp.\n- id: fig7cd-mop-coupling\n  statement: During MOp events, MOp is coupled to PO and SSp but not to LP or VISl.\n  source: Results, SHIELD recordings reveal multi-regional subnetworks, paragraph 6; Figures 7C and 7D\n  quote: \"Conversely, MOp showed the opposite pattern: strong coupling to PO and SSp, but not to LP or\n    VISl.\"\n  criterion: As fig7cd-visp-coupling with MOp as reference. Reproduced when MOp-PO and MOp-SSp are\n    significant with positive band coherence and MOp-LP and MOp-VISl are not, and the CCG peaks of\n    PO and SSp lie near zero and are higher than those of LP and VISl.\n- id: fig7e-lags-straddle-zero\n  statement: In the 3 to 7 Hz band, time lags between VISp or MOp and their associated regions\n    straddle zero; neither consistently leads or follows.\n  source: Results, Fine-scale alpha rhythm coupling, paragraph 1 (first lines of page 13); Figure 7E\n  quote: Time lags between VISp and MOp and their associated regions in the 3–7 Hz band straddled zero\n    lag, indicating that these areas did not consistently lead or follow activity in the other network\n    nodes (Figure 7E).\n  criterion: As in code cell 26, per qualifying event the median over 3 to 7 Hz frequency bins of the\n    phase delay (nitime CoherenceAnalyzer, default settings) between the reference population rate and\n    the other area's, both at the event, for VISp with VISl, VISal, LGd, LP, CP and MOp with SSp, PO,\n    those significant in fig7f. A claim of absence. The paper's text names no test; the code tests\n    lags against zero with the Wilcoxon signed-rank test and Benjamini-Hochberg, and its printed\n    output gives p from 2.4e-49 to 0.010 for all seven pairs. Judged on that test at 0.05;\n    reproduced for a pair when not significant. The median lag and the fraction of positive lags are\n    reported for each pair.\n- id: fig7f-visp-network\n  statement: Beyond visual cortex and thalamus, VISp alpha events enhance coherence of VISp with ACA,\n    RSP and CP.\n  source: Results, Fine-scale alpha rhythm coupling, paragraph 2 (page 13); Figure 7F\n  quote: In addition to visual corticothalamic regions, VISp alpha events enhanced coherence between\n    VISp and medial cortical structures anterior cingulate area (ACA) and RSP, as well as CP\n  statistics:\n  - test: Wilcoxon signed-rank test, event against random coherence\n    p: 0.05\n    p_relation: \"<\"\n    corrected: Benjamini/Hochberg\n    n: 34 CCF regions\n  criterion: The header's pair test with VISp as reference. Areas are the units' structure_acronym\n    values with at least 20 units, so ACA and RSP appear as ACAd, ACAv, RSPd, RSPv and so on; readings\n    (a) any subdivision significant; (b) all recorded subdivisions significant. Reproduced when ACA,\n    RSP, CP, LGd, LP and VISl are each significant with positive band coherence.\n- id: fig7f-mop-network\n  statement: MOp alpha events enhance coherence of MOp with SSp, PO, MRN and the intermediate layers of\n    the superior colliculus (SCiw).\n  source: Results, Fine-scale alpha rhythm coupling, paragraph 2 (page 13); Figure 7F\n  quote: Conversely, MOp events enhanced coherence between MOp and SSp/PO, as well as motor-related\n    midbrain structures MRN and deep layers of the superior colliculus (SCiw).\n  statistics:\n  - test: Wilcoxon signed-rank test, event against random coherence\n    p: 0.05\n    p_relation: \"<\"\n    corrected: Benjamini/Hochberg\n    n: 34 CCF regions\n  criterion: The header's pair test with MOp as reference. Reproduced when SSp, PO, MRN and SCiw are\n    each significant with positive band coherence (SSp under the same subdivision readings as\n    fig7f-visp-network).\n- id: fig7-hippocampus-not-engaged\n  statement: Neither VISp nor MOp alpha events engage the hippocampus.\n  source: Results, SHIELD recordings reveal multi-regional subnetworks, paragraph 4; Figures 7A and 7F\n  quote: Neither visual nor motor events appeared to engage the hippocampus.\n  criterion: A claim of absence, judged on the pair test of the header (the paper's test for\n    engagement, Figure 7F) for every hippocampal formation region recorded (CA1, CA2, CA3, DG, SUB,\n    ProS and the like, by the CCF tree in the code's ccf_structure_tree_2017.csv). Reproduced when\n    none is significant with positive band coherence for either reference area.\n- id: fig8bc-cp-rf-location\n  statement: CP units with significant spatial receptive fields lie mostly in the medial dorsal\n    striatum, midway along the anterior-posterior extent of CP.\n  source: Results, Fine-scale alpha rhythm coupling between visual cortex and striatum, paragraph 2;\n    Figures 8B and 8C\n  quote: These units were biased toward the medial dorsal striatum mid-way along the anteriorposterior\n    extent of the CP\n  criterion: CP units (structure_acronym CP) passing QC, split by RF significance (chi-square, p <\n    0.01, Methods). The paper gives no test. Open. Reading, CCF medial-lateral and dorsal-ventral\n    coordinates of CP-RF against CP-noRF units by the Wilcoxon rank-sum test (the Methods' default\n    unpaired test); reproduced when CP-RF units are more medial and more dorsal at p < 0.05. The\n    anterior-posterior part is reported as the CP-RF median against the CP extent sampled; the paper\n    notes the lateral and posterior striatum were not sampled.\n- id: fig8d-cp-rf-larger-response\n  statement: CP units with receptive fields respond more strongly to the task's full-field images than\n    CP units without receptive fields.\n  source: Results, Fine-scale alpha rhythm coupling between visual cortex and striatum, paragraph 3;\n    Figure 8D\n  quote: CP-RF units showed significantly larger visual responses to this stimulus compared with CPnoRF\n    units (Figure 8D).\n  statistics:\n  - test: Wilcoxon rank-sum test per time point\n    p: 0.05\n    p_relation: \"<\"\n    corrected: Benjamini-Hochberg\n    n: 80 CP-RF and 205 CP-noRF units\n  expected:\n  - quantity: CP-RF units\n    value: 80\n    tolerance: 8\n  - quantity: CP-noRF units\n    value: 205\n    tolerance: 20.5\n  - quantity: VISp units\n    value: 239\n    tolerance: 23.9\n  criterion: As in code cells 31 to 35, the five sessions 1182628226, 1182871514, 1183071525, 1194850630\n    and 1195036753; spikes at 1 ms from 250 ms before to 500 ms after every active-behavior image\n    presentation (make_dg_unit_tensor.py); the group's mean over -50 to 0 ms subtracted; exponential\n    smoothing with tau 2 ms; mean over presentations per unit; per 1 ms bin a Wilcoxon rank-sum test of\n    CP-RF against CP-noRF units, Benjamini-Hochberg (Figure 8D legend). Units passing QC (Methods);\n    the code's presence_ratio > 0.9 filter is a variant. Reproduced when significant bins occur\n    within 250 ms after onset with CP-RF higher in all of them.\n- id: fig8d-response-latencies\n  statement: CP-RF responses lag VISp by about 20 ms, and CP-noRF responses lag CP-RF by about another\n    20 ms.\n  source: Results, Fine-scale alpha rhythm coupling between visual cortex and striatum, paragraph 3;\n    Figure 8D\n  quote: CP-RF lagged behind VISp responses by ... 20 ms, whereas CP-noRF had slower responses that\n    lagged behind CP-RF units by an additional 20 ms\n  depends_on:\n  - fig8d-cp-rf-larger-response\n  expected:\n  - quantity: CP-RF latency minus VISp latency\n    value: 20\n    tolerance: 5\n    unit: ms\n  - quantity: CP-noRF latency minus CP-RF latency\n    value: 20\n    tolerance: 5\n    unit: ms\n  criterion: Population mean responses as in fig8d-cp-rf-larger-response. Tolerance 5 ms because the\n    paper gives the lags as approximate and to the nearest 10 ms. The latency measure is not given;\n    open. Readings (a) time of the population peak; (b) time at which the population mean first\n    reaches half its peak.\n- id: fig8e-cp-rf-more-modulated\n  statement: Triggered on VISp alpha events, CP-RF firing rates are more modulated than CP-noRF rates,\n    particularly in the troughs of the oscillation.\n  source: Results, Fine-scale alpha rhythm coupling between visual cortex and striatum, paragraph 4;\n    Figure 8E\n  quote: We found that CP-RF firing rates were significantly more modulated, particularly during the\n    troughs of the oscillation when the visual thalamo-cortical network is suppressed.\n  statistics:\n  - test: Wilcoxon rank-sum test per time point\n    p: 0.05\n    p_relation: \"<\"\n    corrected: Benjamini-Hochberg\n    n: 439 events\n  criterion: Qualifying VISp events (header) in sessions with CP recorded (code cell 37); per event the\n    CP-RF and CP-noRF population mean rate in 10 ms bins from -0.5 to 2 s, exponential smoothing tau\n    one bin (cell 39). Per bin test, the legend's Wilcoxon rank-sum with Benjamini-Hochberg; the\n    code's paired signed-rank test is a variant. More modulated is not defined; open. Readings (a) the\n    peak-to-trough range of the event-triggered mean over 0 to 1 s is larger for CP-RF; (b) the same\n    on rates divided by each group's mean over -0.5 to 0 s. Reproduced when significant bins exist at\n    the troughs of the VISp rate and the range is larger for CP-RF under a reading.\n- id: fig8f-cp-rf-higher-coherence\n  statement: During VISp alpha events, CP-RF units are more coherent with VISp in the 3 to 7 Hz band\n    than CP-noRF units (p = 3.8e-14, 439 events).\n  source: Results, Fine-scale alpha rhythm coupling between visual cortex and striatum, paragraph 4;\n    Figure 8F\n  quote: As predicted, CP-RF units displayed higher coherence with VISp in the 3–7 Hz band, indicating\n    that alpha events coordinate functionally related cortico-striatal subnetworks.\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 3.8e-14\n    n: 439 events\n  expected:\n    quantity: VISp events in sessions with CP\n    value: 439\n    tolerance: 43.9\n  criterion: As in code cells 37 and 38, per qualifying VISp event (header) the coherence of each CP\n    group's population rate (10 ms bins, 4 s) with the VISp population rate minus the random-time\n    coherence (readings R1 and R2), mean over 3 to 7 Hz; paired Wilcoxon signed-rank of CP-RF against\n    CP-noRF over events. Reproduced when CP-RF is higher at p < 0.05.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001051/10.1016-j.neuron.2024.06.015.yaml paper/10.1016-j.neuron.2024.06.015.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd claims/001051 && f=10.1016-j.neuron.2024.06.015.yaml && python3 - "$f" <<'EOF'
import sys,re
p=sys.argv[1]; s=open(p).read()
rep=[
("  source: Results, Installation of SHIELD implant and QC evaluation, paragraphs 5 and 6; Figures 3F to\n    3H","  source: Results, Installation of SHIELD implant and QC evaluation, paragraph 6; Figures 3F to 3H"),
("  source: Results, Dual-hemisphere SHIELD implant, paragraph 2; Figures S3B and S3D","  source: Results, Dual-hemisphere SHIELD implant, paragraph 1 (end, page 10); Figures S3B and S3D"),
("  source: Results, Fine-scale alpha rhythm coupling, paragraph 1 (first lines of page 13); Figure 7E","  source: Results, SHIELD recordings reveal multi-regional subnetworks, paragraph 7 (top of page 13);\n    Figure 7E"),
("  source: Results, Fine-scale alpha rhythm coupling, paragraph 2 (page 13); Figure 7F","  source: Results, SHIELD recordings reveal multi-regional subnetworks, paragraph 8 (page 13; the text\n    cites it as Figure 6F); Figure 7F"),
("""  criterion: Shown for one example mouse. Open; the paper gives no measure. Reading, the RF centres of
    significant VISp units per day move across days in the direction of the retinotopic axes given
    by the insertion sites (nasal to temporal with anterior to posterior is not stated in the text;
    the figure's axes are used). Requires the ISI maps.""","""  criterion: Shown for one example mouse; the paper gives no measure. Open. Reading, the RF centres
    (azimuth, elevation) of significant VISp units on each day against the retinotopic location the
    ISI sign map predicts at that day's insertion site. Needs the ISI maps and insertion images."""),
]
for a,b in rep:
    n=s.count(a); assert n>=1,(a[:60],n); s=s.replace(a,b)
open(p,'w').write(s)
EOF
grep -n -i "rather\|—" $f; grep -n "Fine-scale alpha rhythm coupling, paragraph" $f | head; python3 -c "
import yaml,sys
d=yaml.safe_load(open('$f'))
for c in d['claims']:
  for k,v in c.items():
    if isinstance(v,str) and ': ' in v and k!='quote': print(c['id'],k)
"
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  && f=claims/001051/10.1016-j.neuron.2024.06.015.yaml && python3 -c "
import yaml
d=yaml.safe_load(open('$f'))
raw=open('$f').read()
for c in d['claims']:
  q=c.get('quote','')
  if ': ' in q:
    i=raw.find('- id: '+c['id']); j=raw.find('quote:',i); print(c['id'], raw[j:j+9])
" ; python tools/claims_check.py $f paper/10.1016-j.neuron.2024.06.015.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  && python3 -c "
import yaml
d=yaml.safe_load(open('claims/001051/10.1016-j.neuron.2024.06.015.yaml'))['claims']
print(len(d), sum('quote' in c for c in d), sum('statistics' in c for c in d), sum(len(c.get('statistics',[])) for c in d), sum('expected' in c for c in d), sum('criterion' in c for c in d))
from collections import Counter; print(Counter(c.get('data','dataset') for c in d))
"; git status --short
```

```
45 45 16 16 23 44
Counter({'dataset': 39, 'with_inputs': 6})
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
?? claims/001051/
?? scripts
```

**Agent**

I wrote the claims file for DANDI:001051 at `claims/001051/10.1016-j.neuron.2024.06.015.yaml`. The quote checker passes except for one p-value. In the text, the p-value of Figure S6 prints as "p = 1.8e�6" (line 711), because the minus sign was garbled in extraction. I read it there and confirmed it is 1.8e-6. Nothing is committed.

**Text read:** the version of record, from a PDF supplied by a person. It has the main text, figure legends, STAR Methods (pages e1 to e8) and the supplement. The supplement holds only the legends of Figures S1 to S6, so its numbers are quoted from those legends. Nothing the claims need is missing from the text. The full text, Methods and supplement are all there.

**Code read:** AllenInstitute/SHIELD_Dynamic_Gating_Analysis at commit 3c09a0dc. It covers Figures 4C to 4G, 7B to 7F, 8D to 8F and the S4I counts, plus metadata tables. In the units table, receptive-field significance is p < 0.01, as the Methods say. I found no code for Figures 3, 4B (trajectories), 5, 6, S3, S4B, S4D to S4H or S6.

**Claims:**
- **Count:** 45 claims, all with quotes. 16 claims carry one statistics entry each (16 entries in all), 23 have expected values and 44 have criteria.
- **Data:** 39 claims use the dataset. 6 are `with_inputs`:
  - five compare against the 5-mm window, using the Visual Behavior Neuropixels dataset (DANDI:000713, version 0.240702.1725);
  - the MRI claim uses naive-mouse scans from Qiu et al. 2018.
- **Possibly not in the dataset:** surgery records, ISI maps, MRI, histology, training records, retraction and sharpening logs, and the optogenetics and Dura-Gel sessions. The dataset's description does not mention any of them; the author has to check.

**Details the paper leaves open, with the readings named:**
- **Alpha events** (written once in the file's header):
  - which units belong to an area: by the area's label (Methods) or by any label containing the acronym (code; for VISp this also takes VISpm, VISpl, VISpor);
  - the event rule: four maxima with three intervals of 125 to 350 ms (Methods) or the code's looser rule;
  - the random-time coherence: both areas at a random time (Methods) or the reference area at the event against the other at a random time (code);
  - the session set: the 87 sessions passing QC or all 99.
- **Pupil (Fig 7B):** pupil area (code) or diameter (text), and the mean or median change.
- **Lags (Fig 7E):** the paper's own code finds significant nonzero lags for all seven pairs (p from 2.4e-49 to 0.010). That runs against the text's "straddled zero". The claim is judged on that code test.
- **QC metrics "comparable" (Fig 4D):** the code's Mann-Whitney test or medians within 10%. The code's printed tests are significant for at least presence ratio and amplitude cutoff.
- **5-mm window yield drop (p = 6e-22):** day 1 against day 2, or the code's test across six groups.
- **RF threshold (Fig 4E):** p < 0.01 (Methods); the code's 0.05 is a variant.
- **Firing rate across days:** the text gives p = 0.21, the code and figure 0.26. Both are recorded.
- **Unit filter in Fig 8:** the Methods' presence ratio above 0.95; the code's 0.9 is a variant.
- **Fig 8 tests:** the legend's rank-sum test for 8E, with the code's signed-rank test as a variant. For 8E, "more modulated" is read on raw or baseline-normalised rates. For 8D, latency is time to peak or to half-peak.
- **Rewards across days:** all rewards, or hits only.
- **Retraction drift:** max_drift or cumulative_drift, and QC-passing or non-noise units.
- **Recovery after insertion (S4I):** the normalisation and fit for the time constant.
- **Probe entry point (trajectory consistency):** where on the probe it is taken.
- **Stimulus-offset timing (Fig 7B):** chi-square or KS test against uniform.
- **MOp against VISp frequency:** measured from inter-peak intervals or from the autocorrelogram spectrum.
- **Fig S6:** the response windows.
- **Similarity across days (Fig 4G):** taken from the paper's Kruskal-Wallis test, run on response size and on peak latency.

**Missing or inconsistent in the paper:**
- No method or code for Figure S6 (r = 0.77), the trajectory deviation, the drift-map discontinuities (judged by eye), the reward counts, or the silencing and optotagging measures.
- The failure causes the Methods list add up to 11 failed mice, against 13 in the Results.
- The code's 467 insertions over 87 sessions give 5.37 probes per session, against the 5.46 the Methods report.
- The text cites Figure 6F where it means 7F.

## End of run

29 turns, 10 minutes, result: success.
