# 000402 · claims · run 39976635241

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ claims/000402/ paper/ 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  awk '/^## Reader/,/^## Author/' docs/protocol.md; ls claims/001453/ claims/000402/ paper/ 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  cat claims/001453/*.yaml | head -200; wc -l paper/*.txt; head -30 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/001453/10.1016-j.cub.2025.04.027.yaml",
 "limit": 250
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
[... 230 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -l paper/*.txt; ls paper/
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 250,400p claims/001453/*.yaml | grep -n "checks\|kind\|data:\|^- id" | head -40; tail -40 claims/001453/*.yaml
```

```
1:- id: fig2k-more-monocular
11:- id: fig2l-bi-ratio
21:- id: fig3e-longer-swims
31:- id: fig3cd-zf-turn-more
48:- id: fig4f-longer-on-duration
60:- id: fig4hi-vspn-lateralized
    and shorten their swims for oblique stimuli while DC do not.
  source: Figure 3C and 3D
  quote: In ZF, swims during forward last significantly longer than those during turn-inducing
    stimuli ... DC swims are less lateralized, with no significant shortening for oblique stimuli
    ... with ZF exhibiting higher angle turning than DC during turn-inducing stimuli
  statistics:
  - about: ZF swim duration, forward against turn-inducing stimuli
    test: two-way ANOVA followed by within-species one-way ANOVA
    p: 0.0001
    p_relation: "<"
    n: 4 ZF fish, 1887 swims
  - about: tail angle, ZF against DC, turn-inducing stimuli
    test: two-way ANOVA, Tukey post hoc
    p: 0.05
[... 26 more lines not kept]
```

**Agent**

I've read the protocol and the example file. Next I'm reading the paper text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41586-025-08790-w.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
t=open('paper/10.1038-s41586-025-08790-w.txt').read()
print(t[55500:100000])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/480a4c20-683b-4abd-84d9-28bb235ca726/tool-results/bxtn4q7i9.txt"
}
```

```
1	specific types of connectivity exist among different cell types of interest. Additionally, the scale of the data and the availability of exploration tools to facilitate the discovery of anomalies or contradictions to current hypotheses and provide opportunities to address and resolve them effectively. Both of these approaches can help to identify patterns and trends that would be difficult to observe using smaller datasets. However, larger datasets have limitations and challenges associated with them. When analysing the connectivity graph, it is essential to keep in mind that although, as shown by our results, the automatic segmentation of dendritic inputs is highly accurate, the automatic segmentation of axons is not as accurate. Therefore, it is essential to be aware of which processes have been proofread and to what extent. Additionally, it is worth considering that although each neuron in the dataset receives thousands of inputs, a percentage of synapses in the dataset are on detached spines. Depending on the scientific question being asked, it is worth considering whether these detached spines may create bias in the conclusions drawn, such as distinguishing between excitatory and inhibitory inputs 5 . In the functional data, it is important to recognize that photon scattering and out-of-plane fluorescence may cause signal degradation and contamination with increasing depth from the pia surface, especially given the dense GCaMP6s expression in excitatory somas and neurites 39 . Caution should be taken to disentangle true biological variation in neuronal tuning across layers from these optical artefacts, by either matching controls at the same depth, or validating the finding with a method that is less prone to these artefacts (such as electrophysiology or 2P microscopy with more sparse or targeted labelling). Furthermore, although all functional imaging was done in the same volume, it was done across several distinct imaging sessions. Technical factors as well
[... 55 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import re
t=open('paper/10.1038-s41586-025-08790-w.txt').read()
t=re.sub(r'\\\\documentclass.*?\\\\end\{document\}','[EQ]',t,flags=re.S)
open('$TMPDIR/p.txt','w').write(t)
print(len(t))"; python3 -c "
t=open('$TMPDIR/p.txt').read(); i=t.find('Ultrathin sectioning'); print(i); print(t[i:i+40000])" > $TMPDIR/part2.txt; wc -c $TMPDIR/part2.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/part2.txt"
}
```

```
1	97377
2	Ultrathin sectioning The sections were then collected at a nominal thickness of 40 nm using a modified ATUMtome 63 (RMC/Boeckeler) onto 6 reels of grid tape 45 . The knife was cleaned every 100–500 sections, occasionally leading to the loss of a very thin partial section (≪40 nm). Thermal expansion of the block as sectioning resumed post-cleaning resulted in a short series of sections substantially thicker than the nominal cutting thickness. The sectioning took place in two sessions, the first session took 8 consecutive days on a 24 h a day schedule and contained sections 1 to 14773. The loss rate on this initial session was low, but before section 7931 there were two events that led to consecutive section loss (due to these consecutive section losses we decided to not reconstruct the region containing sections 1 to 7931 even though the imagery was collected). The first event that led to consecutive section loss was due to sections being collected onto apertures with damaged films. To prevent this from happening again, we installed a camera that monitors the aperture before collection. The second event was due to an accident where the knife bumped the block and nicked a region near the edge of the ROI. At the end of this session we started seeing differential compression between the resin and the surface of the cortex. Because this could lead to severe section artefacts, we paused to trim additional empty resin from the block and also replaced the knife. The second session lasted five consecutive days and an additional 13,199 sections were cut. Due to the interruption, block shape changes and knife replacement, there are approximately 45 partial sections at the start of this session; importantly, these do not represent tissue loss (see stitching and alignment section). As will be described later, the EM dataset is subdivided into two subvolumes due to sectioning and imaging events that resulted in loss of a series of sections. TEM imaging The parallel imag
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
t=open('$TMPDIR/p.txt').read(); i=t.find('contribution to manual matching'); print(t[i:i+15000])"
```

```
contribution to manual matching of functional ROIs to EM nuclei; D. Kim for his contribution to pupil tracking; R. Raju for his contribution to parametric stimuli development; A. Mok and D. Ouzounov for their contribution to three-photon imaging development; G. McGrath for computer system administration; M. Husseini, L. Jackel and J. Jackel for project administration at Princeton University; S. Hider, T. Gion, D. Pryor, D. Kleissas, L. Rodriguez, M. Wilt and the team from the John Hopkins University Applied Physics Laboratory (APL), as well as Marysol Encarnación and Martha Cervantes from the CIRCUIT Program at APL for supporting data assessments on the neural circuit reconstruction and data infrastructure through the Brain Observatory Storage Service and Database (BossDB; https://bossdb.org/ ; NIH/NIMH R24 MH114785); F. Chance, B. Aimone and everyone at Sandia National Laboratories for their support and assistance; the ‘Connectomics at Google’ team for developing Neuroglancer and computational resource donations, in particular J. Maitin-Shepard for authoring Neuroglancer and help creating the reformatted sharded multi-resolution meshes and imagery files used to display the data; Amazon, the AWS Open Data Program, and the AWS Open Science platform for providing data and computational resources; and Intel for their assistance. The authors also thank the following individuals for their work proofreading neurons in the MICrONS dataset: N. Smith (24,101 edits), D. Panchal (19,384 edits), M. Cook (17,088 edits), C. Ordish (14,333 edits), Niyati (13,897), Z. Sorangwala (13,777 edits), Nirali (13,317 edits), Sholka (11,569 edits), K. Shah (10,570 edits), D. Patel (10,368 edits), Dhara (9,871 edits), Anuja (9,337 edits), Zeba (8,742 edits), A. Rajput (8,674 edits), C. Smith (8,281 edits), Hemal (8,084 edits), Harshil (8,022 edits), C. Knecht (7,199), S. Pal (7,036 edits), D. Rami (6,850 edits), Sweksha (6,766 edits), Priyanka (6,485 edits), Yashvi (6,306 edits), Frank (5,71
[... 1 more lines not kept]
```

**Agent**

The full text and Methods are present. The supplement holds only the Reporting Summary and the Peer Review File. Next I'll read the linked code and the dandiset's title and description.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/AllenInstitute/MicronsFunctionalConnectomics 2>&1 | tail -2; cd MicronsFunctionalConnectomics 2>/dev/null && git log -1 --format='%H %cd' && find . -type f | grep -v '^./.git/' | head -100; curl -s https://api.dandiarchive.org/api/dandisets/000402/ | python3 -c "import json,sys; d=json.load(sys.stdin); print(d['draft_version']['name'])"; curl -s https://api.dandiarchive.org/api/dandisets/000402/versions/draft/info/ | python3 -c "import json,sys; d=json.load(sys.stdin); m=d['metadata']; print(m.get('description')); print(m.get('version'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd "$TMPDIR/MicronsFunctionalConnectomics"; for f in "Fig 3/panel_f/get_data.ipynb" "Fig 3/panel_f/make_plot.ipynb" "Fig 3/panel_g/get_data.ipynb" "Fig 3/panel_g/make_plot.ipynb"; do echo "=== $f"; python3 -c "
import json,sys
nb=json.load(open(sys.argv[1]))
for c in nb['cells']:
    s=''.join(c['source'])
    print('--',c['cell_type']); print(s[:3000])
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            if 'text' in o: print('>>',''.join(o['text'])[:800])
" "$f"; done
```

```
=== Fig 3/panel_f/get_data.ipynb
-- code
import numpy as np
from scipy.interpolate import interp1d
import pandas as pd
-- code
%%capture
import datajoint as dj
nda = dj.create_virtual_module('nda', 'microns_phase3_nda')
-- markdown
# get oracle scores
-- code
oracle_rel = nda.ScanUnit() * nda.Oracle() & nda.ScanInclude()
oracle_df = pd.DataFrame(oracle_rel.proj(oracle_score='pearson').fetch())
oracle_df['oracle_decile'] = pd.qcut(oracle_df['oracle_score'], q=10, labels=np.arange(10))
-- markdown
# save 1000 oracle traces
-- code
def fetch_trial_average_oracle_raster(unit_key, desired_fps=None, average_over_repeats=True, normalize_traces=True):
    """Fetches the responses of the provided unit to the oracle trials
[... 231 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/MicronsFunctionalConnectomics"; ls -a; cat README* 2>/dev/null | head -50; for f in "Fig 6/panel_k/get_data.ipynb" "Fig 6/panel_k/make_plot.ipynb"; do echo "=== $f"; python3 -c "
import json,sys
nb=json.load(open(sys.argv[1]))
for c in nb['cells']:
    s=''.join(c['source'])
    print('--',c['cell_type']); print(s[:2500])
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            if 'text' in o: print('>>',''.join(o['text'])[:600])
            if 'data' in o and 'text/plain' in o['data']: print('>>',''.join(o['data']['text/plain'])[:600])
" "$f"; done
```

```
.
..
.git
Fig 3
Fig 6
Fig 7
LICENSE
=== Fig 6/panel_k/get_data.ipynb
-- code
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
from caveclient import CAVEclient
import datajoint as dj
-- markdown
# initialize data sources
-- code
client = CAVEclient('minnie65_phase3_v1')
client.materialize.version = 1181
-- code
[... 124 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i "with_labels\|with_inputs\|elsewhere\|kind:" docs/*.md | head -30; grep -rn "kind:" claims/ | awk '{print $NF}' | sort | uniq -c
```

```
docs/design.md:118:  elsewhere. This is the guard against a result that only looks right.
docs/pilot-notes.md:95:  with outside data (`data: dandiset` or `with_inputs`), and the dashboard
docs/pilot-notes.md:107:RDMs that are not public, are now marked `with_inputs`, and its attempt
docs/pilot-notes.md:123:  `data: with_labels`, for outside sources that only name or map codes the
docs/pilot-notes.md:162:adds a fourth data kind, `elsewhere`, for a claim whose data the dandiset
docs/pilot-notes.md:166:dandiset's claims and from `with_inputs` claims. It is never blocked with
docs/pilot-notes.md:257:link claims of step 6). They now say `kind: link` and are counted apart:
docs/protocol.md:137:     `with_labels`, `with_inputs` or `elsewhere` (step 4, and author, step
docs/protocol.md:205:4. Decide what comes from outside the dataset. Data from elsewhere may be
docs/protocol.md:214:     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
docs/protocol.md:215:     `with_inputs` and `elsewhere` claims are counted apart, each group on
docs/protocol.md:217:   - `with_labels` is for outside sources that only name or map codes the
docs/protocol.md:222:     or subjects, a claim of its own (`kind: link`) tests the link. Link
docs/protocol.md:239:   - `elsewhere` is for a claim whose data the dataset does not hold at
docs/protocol.md:248:   - The notes of a `with_inputs` claim say which side a difference comes
docs/protocol.md:259:     `data: elsewhere` instead (step 4).
    154 agent
     40 link
```

**Agent calls Bash**

```bash
cd  sed -n 200,262p docs/protocol.md; sed -n 90,170p docs/pilot-notes.md; grep -rn "kind: agent" claims | head -3; grep -rn -B3 -A8 "kind: agent" claims | head -30
```

```
3. Choose the version to pin. Pin the version the paper cites, as the claims
   file gives it. If it cites none, pin the most recent published version,
   unless an earlier one matches the claims file's description better. Say
   why in the notebook's header. If versions differ in content the analysis
   uses, show the difference.
4. Decide what comes from outside the dataset. Data from elsewhere may be
   used only when the claims file says the paper relies on it, it is public,
   and it is pinned: a DOI, or a repository at a commit. Record each under
   `inputs` in the attempt. A claim whose outside input is not public is
   blocked with `data_missing`, and its notes say where you looked.

   The registry judges the dataset, so claims that use outside data are
   kept apart:
   - Each claim says what its test uses: `data: dataset` (the default),
     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
     `with_inputs` and `elsewhere` claims are counted apart, each group on
     its own; the others count towards what is said about the dataset.
   - `with_labels` is for outside sources that only name or map codes the
     dataset already holds, such as stimulus names for its stimulus codes.
     They bring in no measurements. A link claim must confirm the names, and
[... 157 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls claims/000404/; head -60 claims/000404/*.yaml; grep -n "where:\|data: elsewhere" -A3 claims/000404/*.yaml | head -30; grep -rn "^  where:\|^  where" claims | head -5
```

```
10.1016-j.cub.2023.06.027.yaml
# Claims for Athalye, Khanna, Gowda, Orsborn, Costa & Carmena (2023), "Invariant neural dynamics
# drive commands to control different movements", Current Biology 33, 2962-2976, on dandiset 000404
# ("Monkey 2D cursor BMI").
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23, protocol
# pilot-10 as stated in docs/protocol.md (Reader, steps 1 to 4).
#
# Text read: the accepted author manuscript in PubMed Central (PMC10527529, NIHMS1910377), full text
# (paper/10.1016-j.cub.2023.06.027.txt): Summary, Results, Discussion, STAR Methods, all figure
# legends, and the supplement (NIHMS1910377-supplement-2.pdf, extracted into the same file):
# legends of Figures S1 to S6, Table S1 (comparisons with shuffled data, Figures 3 to 5) and Table
# S2 (simulation statistics, Figure 6). The columns of Tables S1 and S2 were read from the
# supplement PDF (pages 15 and 16), as the text extraction splits them into cells. The version of
# record is not open access. The bioRxiv preprint (10.1101/2021.08.27.457931, the paper the
# dandiset names) is also under paper/ and was not used; the version of record replaces it.
#
# Code read: https://github.com/pkhanna104/bmi_dynamics_code at commit 416187366f84f2b7367ac54205aa321480e1acd1
# (2023-06-04; archived as Zenodo 10.5281/zenodo.8006653). It holds the preprocessing of the HDF and
# decoder files (prelim_analysis.py, resim_ppf/ppf_pa.py), the model fitting
# (online_analysis/generate_models*.py), the analyses behind each figure (online_analysis/
[... 46 more lines not kept]
```

**Agent**

I've read the paper, the linked figure code and the format. Now I'm writing the claims file.

**Agent calls Bash**

```bash
cd  sed -n 1,60p tools/claims_check.py
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

[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));
c=s['properties']['claims']['items'] if 'items' in s['properties']['claims'] else s
print(json.dumps(c,indent=1)[:4000]); print(list(s['properties'].keys()))"
```

```
{
 "type": "object",
 "additionalProperties": false,
 "required": [
  "id",
  "statement",
  "source"
 ],
 "properties": {
  "id": {
   "description": "Stable within the file, e.g. fig2b.",
   "type": "string",
   "pattern": "^[a-z0-9]+(-[a-z0-9]+)*$"
  },
  "statement": {
   "description": "The finding in one or two sentences, in words. Not a copy of the figure.",
   "type": "string",
   "minLength": 1
  },
  "source": {
[... 118 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));
for k,v in s['\$defs'].items(): print(k, list(v.get('properties',{}).keys()), v.get('required'))"
```

```
expected ['quantity', 'value', 'tolerance', 'unit'] ['quantity', 'value']
statistic ['about', 'test', 'statistic', 'p', 'p_relation', 'corrected', 'ci', 'n'] None
```

**Agent calls Bash**

```bash
cd "$TMPDIR/MicronsFunctionalConnectomics/Fig 7"; cat Fig7abc/README.md; for f in Fig7abc/connectivity.ipynb "Minnie-Figure 7d.ipynb"; do echo "=== $f"; python3 -c "
import json,sys
nb=json.load(open(sys.argv[1]))
for c in nb['cells']:
    s=''.join(c['source'])
    print('--',c['cell_type']); print(s[:1500])
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            if 'text' in o: print('>>',''.join(o['text'])[:400])
            if 'data' in o and 'text/plain' in o['data']: print('>>',''.join(o['data']['text/plain'])[:400])
" "$f"; done 2>&1 | head -300; head -3 Fig7abc/edgelist.csv; wc -l Fig7abc/edgelist.csv
```

```
# Connectivity matrices

Requirements for `connectivity.ipynb` are specified in the pyproject.toml file.
The easiest approach to running this code would be to use `uv` to create a virtual environment and use it as the interpreter for the notebook.
This will ensure that all dependencies are met.=== Fig7abc/connectivity.ipynb
-- code
from caveclient import CAVEclient
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import tqdm

from standard_transform.datasets import minnie_ds
-- code
from matplotlib import rcParams

# Use editable fonts
rcParams['pdf.fonttype'] = 42
rcParams['ps.fonttype'] = 42
[... 266 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/MicronsFunctionalConnectomics/Fig 7"; python3 -c "
import pandas as pd; d=pd.read_csv('Fig7abc/edgelist.csv'); print(d.num_syn.sum(), len(d), d.pre_pt_root_id.nunique()); print(d.groupby(['valence_pre','valence_post']).num_syn.agg(['sum','count']))"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import pandas as pd; d=pd.read_csv('Fig7abc/edgelist.csv'); print(d.num_syn.sum(), len(d), d.pre_pt_root_id.nunique()); print(d.groupby(['valence_pre','valence_post']).num_syn.agg(['sum','count']))
    ^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pandas'
```

**Agent calls Bash**

```bash
cd "$TMPDIR/MicronsFunctionalConnectomics/Fig 7"; python3 -c "
import csv,collections
s=0;n=0;pre=set();g=collections.Counter()
for r in csv.DictReader(open('Fig7abc/edgelist.csv')):
    k=int(r['num_syn']); s+=k;n+=1;pre.add(r['pre_pt_root_id']); g[(r['valence_pre'],r['valence_post'])]+=k
print(s,n,len(pre),g)"
```

```
812686 499973 1185 Counter({('inhibitory_neuron', 'excitatory_neuron'): 412471, ('excitatory_neuron', 'excitatory_neuron'): 239046, ('excitatory_neuron', 'inhibitory_neuron'): 108727, ('inhibitory_neuron', 'inhibitory_neuron'): 52442})
Shell cwd was reset to
```

**Agent**

I've drafted the claim list (2P functional claims from the dataset, co-registration claims that need CAVE tables, EM claims held elsewhere). Writing the file now.

**Agent calls Write**

```json
{
 "file_path": "claims/000402/10.1038-s41586-025-08790-w.yaml",
 "content": "# Claims for The MICrONS Consortium (2025), \"Functional connectomics spanning multiple areas of mouse\n# visual cortex\", Nature 640, 435-447, doi:10.1038/s41586-025-08790-w, on dandiset 000402 (\"MICrONS\n# Two Photon Functional Imaging\").\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-23, protocol\n# pilot-10 as stated in docs/protocol.md (Reader, steps 1 to 4).\n#\n# Text read: the version of record, open access (CC BY), as served by Europe PMC (PMC11981939),\n# in paper/10.1038-s41586-025-08790-w.txt: main text, figure legends, Methods, the legends of\n# Extended Data Figs 1 to 5 and the captions of Extended Data Tables 1 to 3. The supplementary\n# information is a Reporting Summary and a Peer Review File; no result rests on them. The text holds\n# only the captions of the Extended Data Tables, not their cells, and no PDF is under paper/, so the\n# per-scan parameters of Extended Data Table 1 (planes, depths, frame rate and field sizes of each\n# scan) were not read. The Methods give these parameters by group of scans, and the claims use\n# those.\n#\n# Code read: https://github.com/AllenInstitute/MicronsFunctionalConnectomics at commit\n# be24e51bd7090e9fb32a9099b4e0c6025342629b (2025-02-23), the repository of the Code availability\n# statement. It holds notebooks for Fig. 3f (oracle rasters; get_data.ipynb, make_plot.ipynb), Fig.\n# 3g (Monet2 direction rasters), Fig. 6k (oracle responses of the example cell and its\n# co-registered targets), Fig. 7a to 7c (connectivity by soma depth, with the edge list it plotted,\n# Fig 7/Fig7abc/edgelist.csv) and Fig. 7d (L3a order 1 and order 2 heat maps, from two csv files).\n# The notebooks read the functional data from the DataJoint schema microns_phase3_nda and the EM\n# tables from CAVE (minnie65_phase3_v1 or minnie65_public, materialization version 1181). The\n# oracle score and the direction tuning fits are read from precomputed DataJoint tables\n# (nda.Oracle, field pearson; pipeline_radtune.VonFit), whose code is not in this repository. The\n# imaging pipeline the Methods cite (https://github.com/cajal/pipeline) was not read; no commit is\n# given for it. No code is given for the counts of the Results (masks, scans, matches, synapses,\n# proofreading).\n#\n# Data the paper used, as it reports them. One male mouse (Slc17a7-Cre x Ai162, GCaMP6s in\n# excitatory neurons), 65 days old at the start of the experiments. 2P calcium imaging with a\n# random access mesoscope (2P-RAM): 14 scans of 19 completed, over 6 days, P75 to P81 by the main\n# text (the Methods timeline gives imaging from 4 March 2018, P75, to 9 March 2018, P80). The\n# volume is about 1,200 x 1,100 x 500 um (anteroposterior x mediolateral x depth), layers 2 to 5,\n# at the junction of VISp, VISlm, VISrl and VISal. 11 scans at 6.3 Hz with 4 depths, 2 scans at\n# 8.6 Hz with 3 depths, 1 scan at 9.6 Hz with 2 depths. Somas segmented by constrained NMF in\n# CaImAn, traces deconvolved; a classifier keeps somatic masks. Each scan has about 84 min of\n# stimulus (natural videos in three categories, cinematic, Sports-1M and rendered; and the\n# parametric Monet2 and Trippy), shown to the left eye, plus periods of monitor on and monitor off\n# for spontaneous activity. Treadmill velocity (rotary encoder, about 57 to 100 Hz), and video of\n# the left eye (about 20 Hz) giving pupil position and diameter. A structural 2P stack (green and\n# red, 1,412 x 1,322 x 670 um at 0.5 pixels per um) taken after Texas Red injection is used to\n# register the scan fields; visual area labels come from a retinotopic sign map transformed into\n# the stack. The dandiset's description says it holds the 2P functional imaging, treadmill, eye\n# and pupil data, with the EM identifiers of matched cells as plane segmentation columns taken from\n# CAVE.\n#\n# The EM half of the paper (sectioning, alignment, segmentation, synapses, nuclei, proofreading,\n# cell classes, connectivity) uses data the dandiset does not hold. The paper deposits them at\n# MICrONS Explorer (https://www.microns-explorer.org/cortical-mm3) and BossDB\n# (https://bossdb.org/project/microns-minnie), with annotation tables served by CAVE. The paper\n# names no materialization version for its counts; its code uses version 1181, and the Results\n# date the proofreading edits to 16 September 2024. Those claims are data elsewhere. Claims that\n# use the co-registration tables (CAVE coregistration_manual_v4 and the automatch tables) with the\n# functional data are with_inputs; whether the dandiset's own plane segmentation columns carry the\n# same matches is the author's to find.\n#\n# Inconsistencies in the text, recorded here and not resolved. The fiducials are 2,934 in total\n# but 1,994 somata plus 942 vessels make 2,936. The Methods timeline puts the structural stack (21\n# March 2018, labelled P83) after the perfusion (16 March 2018, P87); the dates and ages do not\n# agree with the birth date of 19 December 2017 for those two entries. Imaging ends at P80 in the\n# timeline and P81 in the main text.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000402\"\npaper: doi:10.1038/s41586-025-08790-w\nclaims:\n- id: scans-14-p75-p81\n  statement: The calcium imaging data comprise 14 scans of one mouse, collected between P75 and P81,\n    spanning a volume of about 1,200 x 1,100 x 500 um.\n  source: Results, 2P calcium imaging, paragraph 1; Methods, 2P functional imaging\n  quote: The dataset contains 14 individual scans, collected between postnatal day 75 (P75) and P81,\n    spanning a volume of approximately 1,200 × 1,100 × 500 µm 3\n  expected:\n  - quantity: number of scans\n    value: 14\n    tolerance: 0\n    unit: scans\n  - quantity: number of imaging days\n    value: 6\n    tolerance: 0\n    unit: days\n  criterion: Count the distinct scans (session and scan index) and the distinct days on which they\n    were recorded. The scan count is exact, as it is a count of files the paper lists. The ages are\n    judged from the recording dates against the birth date of 19 December 2017 (Methods,\n    Timeline); P75 to P81 (main text) and P75 to P80 (Methods timeline) are both readings the paper\n    allows, and the claim holds when the dates fall within P75 to P81. The 6 days are the days of\n    imaging of the 19 completed scans (Methods, 2P functional imaging); the 14 kept scans may span\n    fewer, so a count of 6 or fewer days is consistent with the paper.\n- id: scan-configurations\n  statement: Eleven scans were imaged at 6.3 Hz with four depths (eight fields), two at 8.6 Hz with\n    three depths (six fields) and one at 9.6 Hz with two depths (four fields); in the 11 scans the\n    four planes span roughly 300 to 400 um.\n  source: Methods, 2P functional imaging, paragraph 1; Results, 2P calcium imaging, paragraph 2\n  quote: For 11 scans, imaging was performed at 6.3 Hz, collecting eight 620 × 1,100 μm fields per\n    frame ... For 2 scans, imaging was performed at 8.6 Hz, collecting six 620 × 1,100 μm fields per\n    frame ... For 1 scan, imaging was performed at 9.6 Hz, collecting four 620 × 1,000 μm fields per\n    frame\n  expected:\n  - quantity: scans at 6.3 Hz with 4 depths\n    value: 11\n    tolerance: 0\n    unit: scans\n  - quantity: scans at 8.6 Hz with 3 depths\n    value: 2\n    tolerance: 0\n    unit: scans\n  - quantity: scans at 9.6 Hz with 2 depths\n    value: 1\n    tolerance: 0\n    unit: scans\n  - quantity: depth span of the four planes in the 11 four-depth scans\n    value: 350\n    tolerance: 85\n    unit: um\n  criterion: Per scan, the imaging rate, the number of fields and of distinct depths, from the\n    dataset's imaging metadata. A scan matches a group when its rate is within 0.1 Hz of the\n    group's and its number of depths is the group's; a field is one 620 um wide strip, and two\n    fields per depth tile the field of view (Methods). The counts are exact. The depth span is the\n    range from 300 to 400 um widened by 10% of each bound (270 to 440 um), as the protocol sets for\n    a range, and is judged on the median span of the 11 scans.\n- id: masks-125413-somatic-115372\n  statement: In total 125,413 masks were segmented across the 14 scans, of which 115,372 were\n    classified as somatic by a trained classifier (8.1% excluded).\n  source: Results, 2P calcium imaging, paragraph 2; Methods, 2P functional imaging, paragraph 3\n  quote: In total, 125,413 masks were generated across 14 scans, of which 115,372 were automatically\n    classified as somatic masks by a trained classifier\n  expected:\n  - quantity: masks across 14 scans\n    value: 125413\n    tolerance: 12541\n    unit: masks\n  - quantity: somatic masks\n    value: 115372\n    tolerance: 11537\n    unit: masks\n  - quantity: fraction of masks excluded by the classifier\n    value: 8.1\n    tolerance: 0.81\n    unit: percent\n  criterion: Count all segmented masks (units) over the 14 scans, and those the dataset marks as\n    somatic. The paper does not say whether the dataset holds the non-somatic masks. The readings\n    are (a) the dataset holds all masks with a somatic label, and both counts are tested; (b) it\n    holds only the somatic masks, and only the 115,372 is tested, the total being untestable. The\n    Methods' 8.1% does not equal 1 - 115,372/125,413 (8.0%); both are within the tolerance.\n- id: unique-neurons-75909\n  statement: Consolidating masks imaged in more than one scan by their 3D position in the structural\n    stack gives an estimated 75,909 unique functionally imaged neurons.\n  source: Results, 2P calcium imaging, paragraph 4; Methods, 2P structural stack, paragraph 2\n  quote: we estimate the functional imaging volume contains 75,909 unique functionally imaged neurons\n    consolidated from 115,372 segmented somatic masks, with many neurons imaged in 2 or more scans\n  expected:\n    quantity: unique functionally imaged neurons\n    value: 75909\n    tolerance: 7591\n    unit: neurons\n  depends_on:\n  - masks-125413-somatic-115372\n  criterion: The method is from the Methods (2P structural stack). Each scan field is registered into\n    the structural stack and each somatic mask gets a 3D centroid; the closest 2 cells from\n    different scans are grouped, iteratively, until all pairs are at least 10 um apart or a further\n    join produces a mask taller than 20 um in z. The paper does not say how the height of a group\n    is measured. The readings are (a) the range in z of the centroids in the group; (b) that range\n    plus the z extent of one field's mask. It also does not say whether distances to a group are\n    taken from its mean centroid or from its nearest member; the readings are (i) mean centroid,\n    (ii) nearest member. The count is judged under each combination. If the dataset holds no stack\n    coordinates for the masks, the claim cannot be tested from it.\n- id: area-split-half-visp\n  statement: The imaging volume is roughly 50% VISp and 50% higher visual areas (VISlm, VISrl and\n    VISal), with each functional unit assigned an area from its position in the stack.\n  source: Methods, Imaging site selection, paragraph 1; Methods, 2P structural stack, paragraph 3;\n    Fig. 3a,d\n  quote: This resulted in an imaging volume that was roughly 50% VISp and 50% higher visual area (HVA)\n  expected:\n    quantity: share of unique neurons in VISp\n    value: 50\n    tolerance: 15\n    unit: percent\n  criterion: The share of units labelled VISp among units with an area label. The paper's \"roughly\"\n    gives no bound; 15 percentage points is set here, as 10% of 50 would read \"roughly\" more\n    narrowly than the word allows. The paper does not say whether the share is of volume or of\n    neurons, or which units count. The readings are (a) all somatic masks over the 14 scans; (b) one\n    per unique neuron, when the dataset identifies them; (c) the area of the field of view. The\n    claim holds when one reading is within the tolerance.\n- id: z-drift-under-10um\n  statement: All scans drifted less than 10 um in z over the recording, and most less than 5 um.\n  source: Methods, 2P structural stack, paragraph 2\n  quote: All scans had less than 10-μm drift over the 1.5-h recording, and for most of them drift was\n    limited to <5 μm\n  expected:\n  - quantity: scans with z drift below 10 um\n    value: 14\n    tolerance: 0\n    unit: scans\n  criterion: The Methods say drift was found by sequential registration of sections of each scan into\n    the structural stack; the length of a section and the registration of each are not given. The\n    readings are (a) consecutive blocks of about 10 min (the stimulus blocks); (b) the two halves of\n    the scan (the stimulus repeats one in each half). Drift is the range of the registered z of a\n    field over the sections. Reproduced when every scan's drift is below 10 um and more than half\n    of the scans are below 5 um, under one reading. If the dataset holds neither the stack nor the\n    raw frames, the claim cannot be tested from it.\n- id: structural-stack\n  statement: A two-channel structural stack (green GCaMP and red vasculature) of 1,412 x 1,322 x 670\n    um at 0.5 pixels per um was collected after Texas Red injection.\n  source: Results, 2P calcium imaging, paragraph 3; Methods, 2P structural stack, paragraph 1\n  quote: a 2-channel (green, red) 1,412 × 1,322 × 670 μm 3 (anteroposterior × mediolateral × radial\n    depth) structural stack was collected at 0.5 pixels per μm\n  expected:\n  - quantity: stack extent, anteroposterior\n    value: 1412\n    tolerance: 141\n    unit: um\n  - quantity: stack extent, mediolateral\n    value: 1322\n    tolerance: 132\n    unit: um\n  - quantity: stack extent, depth\n    value: 670\n    tolerance: 67\n    unit: um\n  - quantity: resolution\n    value: 0.5\n    tolerance: 0.05\n    unit: pixels per um\n  criterion: Reproduced when the dataset holds the stack with two channels and its extent and\n    resolution are within tolerance; the extent is the number of voxels divided by the resolution.\n- id: stimulus-composition\n  statement: Each scan's stimulus lasted about 84 min and was made of 6 oracle clips of 10 s repeated\n    10 times (10 min), 144 unique natural clips of 10 s (24 min), 90 natural clips of 10 s shown\n    twice (30 min), and 20 Trippy and 20 Monet2 seeds of 15 s each shown twice (10 min each).\n  source: Methods, Stimulus composition; Results, Behavioural tracking and visual stimulation,\n    paragraph 1\n  quote: Each scan stimulus was approximately 84 min in duration and comprised\n  expected:\n  - quantity: total stimulus duration per scan\n    value: 84\n    tolerance: 8.4\n    unit: min\n  - quantity: oracle clips\n    value: 6\n    tolerance: 0\n    unit: clips\n  - quantity: repeats of each oracle clip\n    value: 10\n    tolerance: 0\n    unit: repeats\n  - quantity: unique natural clips per scan\n    value: 144\n    tolerance: 0\n    unit: clips\n  - quantity: natural clips shown twice\n    value: 90\n    tolerance: 0\n    unit: clips\n  - quantity: Trippy seeds per scan\n    value: 20\n    tolerance: 0\n    unit: seeds\n  - quantity: Monet2 seeds per scan\n    value: 20\n    tolerance: 0\n    unit: seeds\n  criterion: Per scan, from the stimulus table, count the clips of each class and their repeats and\n    sum the durations of the stimulus presentations. Counts are exact; the duration is the\n    sum of trial durations (readings (a) trial start to trial end, as the stimulus table gives;\n    (b) the nominal 10 s or 15 s per trial). Reproduced when all 14 scans match. The share of\n    clips in each natural category (2 oracle, 48 unique and 30 repeated clips per category) is\n    tested when the dataset names the category.\n- id: stimulus-conserved-across-scans\n  statement: The oracle clips, the 90 twice-repeated clips and 10 of the 20 seeds of each parametric\n    stimulus were the same in every scan; the 144 unique clips and the other 10 seeds differed\n    between scans.\n  source: Methods, Stimulus composition; Results, Behavioural tracking and visual stimulation,\n    paragraph 2\n  quote: The stimulus composition included a mixture of unique stimuli for each scan, some that were\n    repeated across every scan, and some that were repeated within each scan\n  depends_on:\n  - stimulus-composition\n  criterion: Clips and seeds are identified by the stimulus identifiers the dataset gives (a condition\n    hash, clip name or seed). Reproduced when the 6 oracle clips and 90 repeated clips occur in all\n    14 scans, 10 Monet2 and 10 Trippy seeds occur in all 14 scans, and the remaining clips and seeds\n    each occur in one scan only. If the dataset gives no identifier for clips, the claim cannot be\n    tested from it.\n- id: oracle-same-order\n  statement: The six oracle clips were repeated in the same order ten times per scan.\n  source: Results, Behavioural tracking and visual stimulation, paragraph 2\n  quote: 6 natural film stimuli clips totalling 1 min (oracle natural videos) were repeated in the same\n    order 10 times per scan\n  depends_on:\n  - stimulus-composition\n  criterion: Per scan, find the 6 clips shown 10 times. The paper's code (Fig 3/panel_f/get_data.ipynb)\n    takes each repeat as the 6 trials that follow the first oracle clip's onset in trial order.\n    Reproduced when, in every scan, each of the 10 repeats shows the same 6 clips consecutively and\n    in the same order.\n- id: spontaneous-periods\n  statement: Each scan was preceded by 0.15 to 5.5 min with the monitor on and followed by 8.3 to 21.2\n    min with the monitor off, to record spontaneous activity.\n  source: Methods, Stimulus composition, last paragraph\n  quote: Each scan was also preceded by 0.15–5.5 min with the monitor on, and followed by 8.3–21.2 min\n    with the monitor off, in order to collect spontaneous neural activity\n  expected:\n  - quantity: monitor-on period before the stimulus, range over scans\n    value: 0.15 to 5.5\n    tolerance: 0.135 to 6.05\n    unit: min\n  - quantity: monitor-off period after the stimulus, range over scans\n    value: 8.3 to 21.2\n    tolerance: 7.47 to 23.32\n    unit: min\n  criterion: Per scan, the time from the first imaging frame to the first stimulus onset, and from the\n    last stimulus offset to the last imaging frame. Reproduced when every scan's values fall in\n    the reported ranges widened by 10% of each bound (the tolerance field gives the widened range).\n- id: monet2-directions\n  statement: Each 15 s Monet2 block holds 16 equal periods of motion, one for each of 16 directions\n    between 0 and 360 degrees, at 42.8 degrees per second.\n  source: Methods, Global directional parametric stimulus; Fig. 3g legend\n  quote: Each 15-s block consisted of 16 equal periods of motion along one of 16 unique directions of\n    motion between 0–360° with a velocity of 42.8° s −1 at the nearest point on the monitor\n  expected:\n  - quantity: directions per Monet2 block\n    value: 16\n    tolerance: 0\n    unit: directions\n  - quantity: duration of one direction period\n    value: 937.5\n    tolerance: 93.75\n    unit: ms\n  criterion: From the Monet2 trial table (directions and onsets per trial, as the code reads them in\n    Fig 3/panel_g/get_data.ipynb). Reproduced when every Monet2 trial has 16 distinct directions\n    spaced 22.5 degrees and periods within tolerance of 15 s / 16; the Fig. 3g legend gives 937 ms.\n    The speed is checked only if the dataset gives it.\n- id: fig3f-oracle-reliability\n  statement: Neurons differ in how reliably they respond to the repeated oracle clips; units with high\n    oracle scores give repeat-to-repeat responses that are consistent, and units with low scores do\n    not.\n  source: Fig. 3f; Results, Behavioural tracking and visual stimulation, paragraph 2; Methods, Oracle\n    score\n  quote: Raster of deconvolved calcium activity for three neurons to repeated stimulus trials (oracle\n    trials; ten repeats of six sequential clips, with each repeat normalized independently). Rasters\n    for high (top), medium (middle) and low (bottom) oracle scores\n  depends_on:\n  - oracle-same-order\n  criterion: The oracle score is, per unit, the jackknife mean of correlations between each oracle\n    trial and the mean of the remaining trials (Methods, Oracle score), on the deconvolved trace\n    interpolated at the scan's frame rate onto the oracle frames, with the unit's ms delay added to\n    its frame times (code, Fig 3/panel_f/get_data.ipynb). The paper's code reads the score from a\n    precomputed table, so the unit of a trial is open. The readings are (a) one trial is one\n    repeat of the 6 clips, concatenated (10 trials); (b) each clip is scored apart over its 10\n    repeats, and the 6 scores are averaged. Units at the 99th, 79th and 34th percentiles of the\n    score (the code's choices for the figure) are selected. Reproduced when, under both readings,\n    the mean pairwise Pearson correlation between single repeats is higher at the 99th than at the\n    79th percentile, and higher at the 79th than at the 34th, taking the 100 units nearest each\n    percentile.\n- id: fig3g-direction-tuning\n  statement: Monet2 drives direction-tuned responses; neurons can be found preferring each of the 16\n    directions, and their trial-averaged responses peak at their preferred direction.\n  source: Fig. 3g; Results, Behavioural tracking and visual stimulation, paragraph 2\n  quote: Trial-averaged raster (central 500 ms of trial-average raster for each direction, out of 937\n    ms) of deconvolved calcium activity for 80 neurons in 40 Monet2 trials (16 randomly ordered\n    directions) grouped by preferred direction (5 neurons per direction\n  depends_on:\n  - monet2-directions\n  criterion: From the code (Fig 3/panel_g/get_data.ipynb). Per unit, the deconvolved trace is\n    interpolated, with its ms delay, at 6.3 Hz over each direction period less (15/16 - 0.5)/2 s at\n    each end (the central 500 ms), and averaged over the 40 Monet2 trials. The code takes the\n    preferred direction from a von Mises fit (pipeline_radtune.VonFit, method 3, direction) and the\n    5 units per direction bin with the highest von_pred_adv, among units in nda.ScanInclude; the fit\n    is not described in the paper and its code is not in the repository. The readings are (a) the\n    preferred direction is the direction with the highest mean response over the central window;\n    (b) the peak of a von Mises function fitted to the 16 mean responses. Units are ranked within\n    each bin of 22.5 degrees centred on each direction by the ratio of the response at the\n    preferred direction to the mean over all directions. Reproduced when, under both readings,\n    every one of the 16 bins holds at least 5 units, and for the top 5 units of each bin the\n    trial-averaged response at the preferred direction exceeds the mean response at the other 15\n    directions in a split-half check (preferred direction from the first 20 trials, response\n    from the last 20).\n- id: behaviour-recorded\n  statement: Treadmill velocity, and the pupil position and diameter from video of the left eye, were\n    recorded throughout each scan.\n  source: Results, Behavioural tracking and visual stimulation, paragraph 1; Methods, Eye and face\n    camera; Methods, Treadmill\n  quote: Treadmill rotation (single axis) and video of the left eye were captured throughout the scan,\n    yielding locomotion velocity, eye movements and pupil diameter data\n  expected:\n  - quantity: treadmill sampling rate, range\n    value: 57 to 100\n    tolerance: 51.3 to 110\n    unit: Hz\n  - quantity: eye camera frame rate\n    value: 20\n    tolerance: 2\n    unit: Hz\n  criterion: Reproduced when all 14 scans hold treadmill velocity and pupil position and diameter\n    covering the imaging period (from the first to the last imaging frame, gaps within it allowed as\n    the Methods say untracked frames are stored as NaN), at rates within tolerance. The share of\n    eye frames with a pupil fit is reported per scan; the paper gives no value for it.\n- id: photodiode-89pct\n  statement: The binary flip code of the photodiode signal, used to align stimulus and behaviour\n    clocks, was recovered for 89% of trials.\n  source: Methods, Stimulus alignment\n  quote: The encoded binary signal was reconstructed for 89% of trials\n  expected:\n    quantity: trials with the encoded signal reconstructed\n    value: 89\n    tolerance: 8.9\n    unit: percent\n  criterion: Needs the raw photodiode signal at 10 MHz, or a per-trial flag of whether the code was\n    read. The decoding is given only in outline (a sine convolution and local peak detection on a\n    three-level signal), so if the dataset holds the raw signal the claim is tested with each of\n    (a) a flag stored by the pipeline, if present, and (b) a decode of the three-level signal by\n    peak detection, and holds when one reading is within tolerance. If the dataset holds only the\n    aligned stimulus times, the claim cannot be tested from it.\n- id: manual-coreg-19181\n  statement: Experts manually matched 19,181 functional ROIs from 14 scans to 15,439 individual EM\n    neurons.\n  source: Results, Functional–structural co-registration, paragraph 2\n  quote: we used the results of the transform to guide a group of experts to manually match 19,181\n    functional ROIs from 14 scans to 15,439 individual EM neurons\n  data: with_inputs\n  expected:\n  - quantity: functional ROIs manually matched\n    value: 19181\n    tolerance: 1918\n    unit: ROIs\n  - quantity: EM neurons manually matched\n    value: 15439\n    tolerance: 1544\n    unit: neurons\n  criterion: The match table is CAVE table coregistration_manual_v4 (Methods, Assigning manual\n    matches), matched to the dataset's units by session, scan index and unit id, as the Fig. 6k code\n    does. The paper gives no materialization version for the counts; the readings are (a) the\n    version its code uses, 1181; (b) the latest public version. Reproduced when, under one reading,\n    the counts are within tolerance and at least 95% of the table's ROIs exist in the dataset.\n    Counting the EM identifiers the dataset itself holds in its plane segmentation columns is shown\n    as a variant.\n- id: ed4-matched-higher-signal-correlation\n  statement: Units independently matched to the same EM neuron in two scans have higher signal\n    correlation than each matched unit with the nearest unmatched unit in the other scan, more\n    clearly for units with oracle score above 0.2.\n  source: Results, Functional–structural co-registration, paragraph 2; Methods, Evaluating manual\n    matches; Extended Data Fig. 4f–h\n  quote: ROIs with at least moderate visual responses that are independently matched to the same\n    neuron across multiple scans have higher signal correlations than adjacent neurons\n  data: with_inputs\n  depends_on:\n  - manual-coreg-19181\n  - oracle-same-order\n  criterion: From the Methods (Evaluating manual matches). For every EM neuron matched to at least two\n    scans, the signal correlation is the Pearson correlation between trial-averaged responses to\n    the oracle stimuli of the matched unit in scan A and the matched unit in scan B; the two\n    controls are the matched unit in scan A with the nearest unit in scan B not matched to the\n    neuron, and the converse. The paper does not define nearest (in which space) or how a neuron\n    matched in more than two scans contributes. The readings for nearest are (a) nearest by 3D\n    centroid in the structural stack; (b) nearest in the same field in 2D. Pairs are all pairs of\n    scans for the neuron. The paper reports no test; reproduced when, under both readings, the\n    matched correlation exceeds both control correlations for more than half of the pairs, and the\n    median difference is larger when both matched units have oracle score above 0.2 than over all\n    pairs. A two-sided Wilcoxon signed-rank test of matched against control is reported.\n- id: fiducial-automatch\n  statement: The fiducial-based automatch assigns 84,198 functional ROIs to 37,364 EM neurons with 83%\n    precision against manual matches; dropping the bottom 30% of separation scores gives 90%\n    precision with 59,934 ROIs and 31,042 neurons.\n  source: Results, Functional–structural co-registration, paragraph 3; Extended Data Fig. 5\n  quote: This method (referred to as the fiducial-based automatch table) resulted in 84,198 functional\n    ROIs matched to 37,364 EM neurons. Considering all matches, this method achieved 83% precision\n    relative to manual matchers, but filtering out matches in the bottom 30% of separation scores\n    yields 90% precision, while still including 59,934 functional ROIs and 31,042 EM neurons\n  data: elsewhere\n  where: CAVE tables coregistration_auto_phase3_fwd and coregistration_manual_v4, datastack\n    minnie65_phase3_v1 (MICrONS Explorer, https://www.microns-explorer.org/cortical-mm3#f-coreg); the\n    paper names no materialization version, its code uses 1181\n  expected:\n  - quantity: ROIs matched\n    value: 84198\n    tolerance: 8420\n    unit: ROIs\n  - quantity: EM neurons matched\n    value: 37364\n    tolerance: 3736\n    unit: neurons\n  - quantity: precision, all matches\n    value: 83\n    tolerance: 8.3\n    unit: percent\n  - quantity: precision, separation score above the 30th percentile\n    value: 90\n    tolerance: 9\n    unit: percent\n  - quantity: ROIs after the filter\n    value: 59934\n    tolerance: 5993\n    unit: ROIs\n  - quantity: EM neurons after the filter\n    value: 31042\n    tolerance: 3104\n    unit: neurons\n  criterion: Precision as the Methods define it (Evaluating automatch tables). Both tables are first\n    restricted to rows where the functional unit or the EM neuron was attempted by the manual\n    matchers; true positives are rows in both tables, false positives rows only in the automatch.\n    Separation scores are turned into percentiles and the threshold is a minimum (Methods). The\n    paper does not say how attempted is decided; the readings are (a) the unit or the neuron\n    occurs in the manual table; (b) the unit's scan field was attempted, any unit of a scan in the\n    manual table. Reproduced when all values are within tolerance under one reading.\n- id: vessel-automatch\n  statement: The vessel-based automatch, without fiducials, assigns 75,856 functional ROIs to 34,712\n    EM neurons with 84% precision; dropping the bottom 30% of separation scores gives 90% precision\n    with 53,248 ROIs and 28,233 neurons.\n  source: Results, Functional–structural co-registration, paragraph 4; Extended Data Fig. 5\n  quote: This table (referred to as the vessel-based automatch table) contains 75,856 functional ROIs\n    matched to 34,712 EM neurons. Remarkably, this fiducial-free method performed as well as the\n    fiducial-based method, achieving 84% precision with manual matches\n  data: elsewhere\n  where: CAVE tables apl_functional_coreg_vess_fwd and coregistration_manual_v4, datastack\n    minnie65_phase3_v1 (MICrONS Explorer, https://www.microns-explorer.org/cortical-mm3#f-coreg); the\n    paper names no materialization version, its code uses 1181\n  expected:\n  - quantity: ROIs matched\n    value: 75856\n    tolerance: 7586\n    unit: ROIs\n  - quantity: EM neurons matched\n    value: 34712\n    tolerance: 3471\n    unit: neurons\n  - quantity: precision, all matches\n    value: 84\n    tolerance: 8.4\n    unit: percent\n  - quantity: precision, separation score above the 30th percentile\n    value: 90\n    tolerance: 9\n    unit: percent\n  - quantity: ROIs after the filter\n    value: 53248\n    tolerance: 5325\n    unit: ROIs\n  - quantity: EM neurons after the filter\n    value: 28233\n    tolerance: 2823\n    unit: neurons\n  criterion: As for fiducial-automatch, with the same readings of attempted.\n- id: hybrid-automatch\n  statement: Keeping only the matches on which both automated methods agree gives 89% agreement with\n    manual matches, with 60,091 ROIs and 29,620 EM neurons.\n  source: Results, Functional–structural co-registration, paragraph 5; Methods, Generating the\n    fiducial-vessel agreement automatch table\n  quote: this hybrid automated table achieves 89% agreement with no additional filtering, yielding\n    60,091 functional ROIs and 29,620 EM neurons\n  data: elsewhere\n  where: CAVE tables coregistration_auto_phase3_fwd, apl_functional_coreg_vess_fwd and\n    coregistration_manual_v4, datastack minnie65_phase3_v1 (MICrONS Explorer); the paper names no\n    materialization version, its code uses 1181\n  expected:\n  - quantity: agreement with manual matches\n    value: 89\n    tolerance: 8.9\n    unit: percent\n  - quantity: ROIs\n    value: 60091\n    tolerance: 6009\n    unit: ROIs\n  - quantity: EM neurons\n    value: 29620\n    tolerance: 2962\n    unit: neurons\n  criterion: The two automatch tables merged on session, scan_idx, field, unit_id and target_id\n    (Methods); agreement is precision as in fiducial-automatch, with the same readings of attempted.\n- id: fiducial-transform-residual\n  statement: A co-registration transform built from 2,934 expert-matched fiducials (1,994 somata and\n    942 blood vessels) has an average residual of 3.8 um; the staged transform lowers the residual\n    from about 10 um to 5.6, 4.6, 3.9, 3.5, 3.1 and 2.9 um.\n  source: Results, Functional–structural co-registration, paragraph 1; Methods, Co-registration\n    Transform\n  quote: In the first step, we generated a co-registration transform using a set of 2,934\n    expert-matched fiducials ... The average residual was 3.8 μm\n  data: elsewhere\n  where: the fiducial points released with the MICrONS resource (MICrONS Explorer,\n    https://www.microns-explorer.org/cortical-mm3) and the 2P structural stack; the paper gives no\n    version or table name for the fiducials\n  expected:\n  - quantity: fiducials\n    value: 2934\n    tolerance: 0\n    unit: points\n  - quantity: average residual\n    value: 3.8\n    tolerance: 0.38\n    unit: um\n  criterion: Count the released fiducials by kind; the count is exact, and the inconsistency of the\n    paper (1,994 plus 942 is 2,936) is reported. The 3.8 um is not tied to a stage of the Methods'\n    transform, whose stages give 10, 5.6, 4.6, 3.9, 3.5, 3.1, 2.9 and 0.003 um. The readings are\n    (a) the leave-one-out residual of the full transform (Methods); (b) the residual after the\n    third group of transforms (3.9 um at n = 3, within tolerance). Reproduced when, applying the\n    released transform to the released fiducials, one reading gives a value within tolerance.\n- id: em-sections\n  statement: The block was cut into 27,972 sections of 40 nm, 26,652 were imaged by five autoTEMs, and\n    an 800 um region of sections 7,931 to 27,904 was processed, split into two subvolumes of about\n    35% and 65% of the sections.\n  source: Results, The EM volume, paragraphs 1 and 2\n  quote: The tissue sample was trimmed and sectioned into 27,972 serial sections (nominal thickness 40\n    nm) ... A total of 26,652 sections were imaged by 5 customized automated TEMs\n  data: elsewhere\n  where: BossDB project microns-minnie (https://bossdb.org/project/microns-minnie) and MICrONS Explorer\n    (https://www.microns-explorer.org/cortical-mm3); no version is given\n  expected:\n  - quantity: sections in the processed region\n    value: 19974\n    tolerance: 0\n    unit: sections\n  - quantity: share of the processed sections in subvolume 35\n    value: 35\n    tolerance: 3.5\n    unit: percent\n  criterion: The released imagery and its metadata give the sections of each subvolume (7,931 to\n    14,815 and 14,816 to 27,904). The processed region is 27,904 - 7,931 + 1 sections. Counts of\n    sections cut and imaged are reported if the released metadata give them.\n- id: synapse-detection\n  statement: Automated detection found 524 million synaptic clefts (186 million in subvolume 35, 337\n    million in subvolume 65), with 96% precision and 89% recall against 8,611 manually annotated\n    synapses in 70 subvolumes, and 98% partner assignment accuracy on 191 held-out synapses.\n  source: Results, Automated reconstruction, paragraph 3; Extended Data Fig. 1\n  quote: We automatically detected and associated a total of 524 million synaptic clefts across both\n    subvolumes (subvolume 35: 186 million, subvolume 65: 337 million). We manually identified\n    synapses in 70 small subvolumes ( n = 8,611 synapses) distributed across the dataset, giving the\n    automated detection an estimated precision of 96% and recall of 89%\n  data: elsewhere\n  where: CAVE synapse tables of minnie65 and minnie35 (MICrONS Explorer,\n    https://www.microns-explorer.org/cortical-mm3); the paper names no materialization version and\n    does not say whether the 8,611 manual annotations are released\n  expected:\n  - quantity: synapses in subvolume 65\n    value: 337\n    tolerance: 33.7\n    unit: million\n  - quantity: synapses in subvolume 35\n    value: 186\n    tolerance: 18.6\n    unit: million\n  - quantity: precision\n    value: 96\n    tolerance: 9.6\n    unit: percent\n  - quantity: recall\n    value: 89\n    tolerance: 8.9\n    unit: percent\n  - quantity: F1\n    value: 92\n    tolerance: 9.2\n    unit: percent\n  criterion: Counts from the released synapse tables. Precision and recall can be tested only if the\n    manual annotations of the 70 test subvolumes are public; the paper does not say how a detection\n    is matched to a manual synapse, so if they are, the readings are (a) overlap of the cleft with\n    the annotation point; (b) cleft centroid within 100 nm of the point.\n- id: nuclei-144120\n  statement: Nuclei were automatically segmented in subvolume 65, 144,120 in all.\n  source: Results, Automated reconstruction, paragraph 2\n  quote: Nuclei were also automatically segmented ( n = 144,120) within subvolume 65\n  data: elsewhere\n  where: CAVE table nucleus_detection_v0, datastack minnie65_phase3_v1 (MICrONS Explorer); the paper\n    names no materialization version\n  expected:\n    quantity: nucleus detections in subvolume 65\n    value: 144120\n    tolerance: 14412\n    unit: nuclei\n- id: cell-classification\n  statement: An SVM on nucleus features detects neurons with 96.9% precision and 99.6% recall,\n    predicting 82,247 neurons in subvolume 65, of which 69,957 have well-segmented somata; a\n    multilayer perceptron separates excitatory from inhibitory neurons with 97% accuracy (96%\n    precision and 94% recall for inhibitory calls).\n  source: Methods, Cell classification\n  quote: This model predicted 82,247 neurons detected within the larger subvolume ... We estimate from\n    this test that the classifier had an overall accuracy of 97% with an estimated 96% precision and\n    94% recall for inhibitory calls\n  data: elsewhere\n  where: CAVE tables nucleus_neuron_svm and the cell class tables of datastack minnie65_phase3_v1\n    (MICrONS Explorer); the paper names no materialization version\n  expected:\n  - quantity: predicted neurons\n    value: 82247\n    tolerance: 8225\n    unit: neurons\n  - quantity: well-segmented neurons\n    value: 69957\n    tolerance: 6996\n    unit: neurons\n  - quantity: SVM precision\n    value: 96.9\n    tolerance: 9.69\n    unit: percent\n  - quantity: SVM recall\n    value: 99.6\n    tolerance: 9.96\n    unit: percent\n  criterion: Counts from the released tables. The accuracies rest on manual labels (a 100 um column\n    and 350 further sampled cells) that the paper does not say are released; they are tested only\n    if those labels are public.\n- id: proofreading-scale\n  statement: The released segmentation holds 1,046,656 proofreading edits as of 16 September 2024;\n    1,433 neurons have proofread axons, 85 excitatory neurons have fully proofread axons and dendrites,\n    and 1,188 excitatory neurons have proofread dendrites.\n  source: Results, Proofreading, paragraphs 1 to 3\n  quote: The released segmentation now contains all 1,046,656 edits of the proofreading that had\n    occurred as of 16 September 2024\n  data: elsewhere\n  where: CAVE table proofreading_status_and_strategy and the ChunkedGraph edit history of datastack\n    minnie65_public (MICrONS Explorer); the code reads version 1181\n  expected:\n  - quantity: edits as of 16 September 2024\n    value: 1046656\n    tolerance: 104666\n    unit: edits\n  - quantity: neurons with proofread axons\n    value: 1433\n    tolerance: 143\n    unit: neurons\n  - quantity: excitatory neurons fully proofread for the functional connectomics study\n    value: 85\n    tolerance: 8.5\n    unit: neurons\n  - quantity: excitatory neurons with proofread dendrites in the columnar sample\n    value: 1188\n    tolerance: 119\n    unit: neurons\n  criterion: Neurons with proofread axons are rows with status_axon true in\n    proofreading_status_and_strategy (Methods). The readings for the version are (a) 1181, as the\n    code uses; (b) the version nearest after 16 September 2024. The 85 and 1,188 are groups of\n    other studies that the table may not label; they are tested only if a released table names\n    them.\n- id: dendrite-input-precision\n  statement: Comparing proofread with automated dendrites, 99% of inputs assigned to a postsynaptic\n    soma in the automated segmentation were correct.\n  source: Results, Proofreading, paragraph 3; Results, Integrated analysis, paragraph 5\n  quote: From the proofread dendrites, we determined that 99% of inputs were correct when assigned to a\n    postsynaptic soma in the automated segmentation\n  data: elsewhere\n  where: CAVE synapse table and proofreading_status_and_strategy, with ChunkedGraph root history,\n    datastack minnie65_public (MICrONS Explorer); no version is given\n  expected:\n    quantity: input precision of automated dendrites\n    value: 99\n    tolerance: 1\n    unit: percent\n  criterion: For neurons with status_dendrite true, the input synapses on the root before proofreading\n    against those on the proofread root; precision is the share of pre-proofreading inputs that\n    remain. The tolerance is 1 point, as the 10% rule would allow values above 100%. The paper does\n    not say which root counts as before proofreading; the readings are (a) the root at the earliest\n    materialization in which the nucleus occurs; (b) the root before the first edit in the edit\n    history.\n- id: axon-lengths\n  statement: The longest proofread excitatory axon measures 18.9 mm with 2,483 synaptic outputs;\n    inhibitory axons range from 1.1 to 32.3 mm in length with a mean of 2,754 outputs (range 99 to\n    14,019).\n  source: Results, Proofreading, paragraph 3\n  quote: the longest excitatory axon measuring 18.9 mm with 2,483 synaptic outputs and inhibitory axons\n    ranging from in length from 1.1 to 32.3 mm with a mean of 2,754 synaptic outputs (range 99–14,019)\n  data: elsewhere\n  where: CAVE tables proofreading_status_and_strategy and synapse tables, with skeletons from the\n    MICrONS release, datastack minnie65_public; no version is given\n  expected:\n  - quantity: longest excitatory axon\n    value: 18.9\n    tolerance: 1.89\n    unit: mm\n  - quantity: outputs of the longest excitatory axon\n    value: 2483\n    tolerance: 248\n    unit: synapses\n  - quantity: mean outputs of inhibitory axons\n    value: 2754\n    tolerance: 275\n    unit: synapses\n  criterion: Axon length from the skeleton of each neuron with a proofread axon, axon compartment\n    only. The paper does not say how length or the axon compartment is obtained; the readings are\n    (a) the released skeletons' axon labels; (b) NEURD's axon split. The inhibitory range is judged\n    as a range widened by 10% of each bound.\n- id: multisoma-split\n  statement: The automated segmentation had 7,050 objects merging 17,753 neurons; after manual and\n    automated splitting the total of individually segmented neurons is 84,035, and NEURD made more\n    than 164,000 edits.\n  source: Results, Proofreading, paragraph 4; Extended Data Fig. 3\n  quote: there were 7,050 segmented objects consisting of a total of 17,753 neurons that were merged\n    together (based on nucleus segmentation) ... bringing the total number of individually segmented\n    neurons to 84,035\n  data: elsewhere\n  where: CAVE tables nucleus_detection_v0 and nucleus_ref_neuron_svm, datastack minnie65_phase3_v1\n    (MICrONS Explorer); the before counts need the first materialization\n  expected:\n  - quantity: individually segmented neurons\n    value: 84035\n    tolerance: 8404\n    unit: neurons\n  criterion: A neuron is individually segmented when its root id holds one neuronal nucleus (Extended\n    Data Fig. 3 uses nucleus_ref_neuron_svm). The before counts (7,050 and 17,753) are tested only\n    if the first materialization is public.\n- id: fig6f-outputs-mapped\n  statement: Between 60% and 95% of the output synapses of proofread axons map to postsynaptic targets\n    with a known soma, depending on cell type and location.\n  source: Fig. 6f; Results, Integrated analysis, paragraph 5\n  quote: between 60 and 95% of those outputs can be accurately mapped onto their postsynaptic targets\n    with a known soma location, depending on the cell type and its spatial location in the volume\n  data: elsewhere\n  where: CAVE synapse table, nucleus_detection_v0 and proofreading_status_and_strategy, datastack\n    minnie65_public (MICrONS Explorer); no version is given\n  expected:\n    quantity: fraction of outputs onto a single soma, range over proofread neurons\n    value: 60 to 95\n    tolerance: 54 to 104.5\n    unit: percent\n  criterion: For each neuron with a proofread axon, the fraction of its output synapses whose\n    postsynaptic root holds exactly one nucleus. The paper's figure shows the spread; reproduced when\n    at least 90% of neurons fall in the widened range. The 90% is set here, as the paper gives a\n    range with no share.\n- id: fig6gh-example-cell\n  statement: For the example proofread L2/3 VISp pyramidal cell, 74.5% (1,053 of 1,412) of its output\n    synapses are onto objects with a single nucleus (275 onto inhibitory, 662 onto excitatory and 116\n    onto unclassified cells), 359 onto orphan fragments, and 365 onto functionally matched cells.\n  source: Fig. 6g,h; Results, Integrated analysis, paragraphs 5 and 6\n  quote: For this particular proofread neuron, 74.5% (1,053 out of 1,412 synapses) are onto objects\n    with a single nucleus (as determined from automated detection), with 275 synapses onto cells\n    classified as inhibitory, 662 synapses onto cells classified as excitatory, and 116 synapses onto\n    cells whose soma did not pass classification quality control\n  data: elsewhere\n  where: CAVE tables synapses_pni_2, nucleus_detection_v0 and coregistration_manual_v4, datastack\n    minnie65_phase3_v1, materialization 1181 (as in the code, Fig 6/panel_k/get_data.ipynb);\n    nucleus id 294657\n  expected:\n  - quantity: output synapses\n    value: 1412\n    tolerance: 141\n    unit: synapses\n  - quantity: share onto single-nucleus objects\n    value: 74.5\n    tolerance: 7.45\n    unit: percent\n  - quantity: synapses onto inhibitory cells\n    value: 275\n    tolerance: 28\n    unit: synapses\n  - quantity: synapses onto excitatory cells\n    value: 662\n    tolerance: 66\n    unit: synapses\n  - quantity: synapses onto functionally matched cells\n    value: 365\n    tolerance: 37\n    unit: synapses\n  criterion: Output synapses of nucleus 294657's root, excluding autapses, merged with the nucleus\n    table on the postsynaptic root (code). The code does not count classes; the class table is not\n    named, and the readings are (a) aibs_metamodel_mtypes_v661_v2, as the Fig. 7 code uses; (b) the\n    cell class table the Methods' classifier fills (Cell classification). Matched cells are those in\n    coregistration_manual_v4.\n- id: fig6k-target-responses\n  statement: The oracle responses of the example cell's functionally co-registered postsynaptic targets\n    can be retrieved from the functional data and set beside the presynaptic cell's.\n  source: Fig. 6k; Results, Integrated analysis, paragraph 6\n  quote: By filtering the synaptic targets with functionally matched neurons (Fig. 6k ), one can\n    further identify which targets have been matched to the functional experiments (365 out of\n    1,412) and use DataJoint to query the functional data or read NWB files deposited in the DANDI\n    data archive\n  data: with_inputs\n  depends_on:\n  - manual-coreg-19181\n  - oracle-same-order\n  criterion: From the code (Fig 6/panel_k/get_data.ipynb). The targets of nucleus 294657 are matched\n    to units in coregistration_manual_v4; per target nucleus, the scan with the highest oracle score\n    is kept, and targets are sorted by summed synapse size. Each unit's oracle trace is averaged over\n    the 10 repeats at 6.3 Hz and min-max normalized. Reproduced when the presynaptic cell and at\n    least 90% of the matched target nuclei of the table have units with oracle trials in the\n    dataset. The figure carries no finding beyond this; no response measure is compared.\n- id: outputs-94-axons\n  statement: From 94 proofread excitatory axons one can query 69,962 output synapses, onto 20,112\n    distinct neuron somata.\n  source: Discussion, Importance of functional connectomics, paragraph 3\n  quote: from just 94 proofread excitatory axons, one can query 69,962 output synapses, which map to\n    20,112 distinct neuron soma in the volume\n  data: elsewhere\n  where: CAVE tables proofreading_status_and_strategy, synapse table and nucleus_detection_v0,\n    datastack minnie65_public; no version is given\n  expected:\n  - quantity: output synapses\n    value: 69962\n    tolerance: 6996\n    unit: synapses\n  - quantity: distinct postsynaptic somata\n    value: 20112\n    tolerance: 2011\n    unit: neurons\n  criterion: The paper does not say which 94 axons. The readings are (a) excitatory neurons with\n    strategy_axon axon_fully_extended; (b) those with fully or partially extended axons whose count\n    is 94 at some public version. Reproduced when one reading gives 94 axons (tolerance 9) and both\n    counts within tolerance.\n- id: fig7abc-laminar-connectivity\n  statement: The outputs of proofread neurons, more than 900,000 synaptic connections, show differences\n    in interlaminar communication between excitatory and inhibitory neurons.\n  source: Fig. 7a–c; Results, Cell types, paragraph 2\n  quote: Examining the output of proofread neurons, which includes more than 900,000 synaptic\n    connections between neurons, reveals key differences in the interlaminar communication between\n    excitatory and inhibitory neurons\n  data: elsewhere\n  where: CAVE datastack minnie65_public, materialization 1181, tables proofreading_status_and_strategy\n    and aibs_metamodel_mtypes_v661_v2 and the synapse table (code, Fig 7/Fig7abc/connectivity.ipynb,\n    with the edge list it saved)\n  expected:\n    quantity: synaptic connections from proofread neurons\n    value: 900000\n    tolerance: 90000\n    unit: synapses\n  criterion: From the code. Presynaptic neurons are those with strategy_axon axon_partially_extended,\n    axon_fully_extended or axon_interareal; postsynaptic cells are those with a unique entry in\n    aibs_metamodel_mtypes_v661_v2; soma depth from the minnie_ds transform. The code's edge list\n    sums to 812,686 synapses onto typed cells, short of \"more than 900,000\". The readings of the\n    count are (a) synapses onto typed cells, as plotted; (b) all output synapses of those neurons,\n    typed or not. The paper names the differences only in the figure; the measure fixed here\n    is the share of each panel's synapses whose presynaptic and postsynaptic somata lie in the same\n    layer (layer bounds from layer_bounds_v3.npy). Reproduced when the count holds under one\n    reading and the same-layer share differs by more than 10 percentage points between at least\n    two of the three panels (E to E, E to I, I to E).\n- id: fig7d-l3-two-hop\n  statement: Seven layer 3 pyramidal cells can be followed through their first-order excitatory and\n    inhibitory targets to the second-order excitatory targets of those inhibitory cells, grouped by\n    inhibitory targeting type (DTC, PTC, ITC, STC).\n  source: Fig. 7d; Results, Cell types, paragraph 2\n  quote: we can follow a collection of layer 3 pyramidal neurons and compare their first-order\n    (direct) connectivity onto excitatory cell types and inhibitory neurons as well as the\n    second-order (two-hop) connectivity of those inhibitory neurons that are targeted by the layer 3\n    cells\n  data: elsewhere\n  where: the csv files of the paper's repository (Fig 7/Fig7-VISp-L3a-order1-E-conn.csv and\n    Fig7-VISp-L3a-Inh-conn-mastersheet.csv, github.com/AllenInstitute/MicronsFunctionalConnectomics at\n    commit be24e51) and CAVE datastack minnie65_public\n  criterion: The paper names no finding beyond the display. Reproduced when the seven cells' first\n    and second order synapse counts recomputed from CAVE (version 1181) agree with the repository's\n    csv files to within 10% per cell and type.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/claims.schema.json')); print(json.dumps(s['\$defs']['expected'],indent=0)[:1500])"; python3 tools/claims_check.py claims/000402/10.1038-s41586-025-08790-w.yaml paper/10.1038-s41586-025-08790-w.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -rn -B2 -A4 "range" claims/*/*.yaml | grep -A5 "quantity:.*range" | head -30
```

```
claims/000045/10.7554-elife.63711.yaml:189:  - quantity: Lab 2 interquartile range of days to proficiency
claims/000045/10.7554-elife.63711.yaml-190-    value: 8
claims/000045/10.7554-elife.63711.yaml-191-    tolerance: 0.8
claims/000045/10.7554-elife.63711.yaml-192-    unit: days
claims/000045/10.7554-elife.63711.yaml:193:  - quantity: Lab 6 interquartile range of days to proficiency
claims/000045/10.7554-elife.63711.yaml-194-    value: 22
claims/000045/10.7554-elife.63711.yaml-195-    tolerance: 2.2
claims/000045/10.7554-elife.63711.yaml-196-    unit: days
claims/000045/10.7554-elife.63711.yaml-197-  depends_on:
--
--
claims/000402/10.1038-s41586-025-08790-w.yaml:303:  - quantity: monitor-on period before the stimulus, range over scans
claims/000402/10.1038-s41586-025-08790-w.yaml-304-    value: 0.15 to 5.5
claims/000402/10.1038-s41586-025-08790-w.yaml-305-    tolerance: 0.135 to 6.05
claims/000402/10.1038-s41586-025-08790-w.yaml-306-    unit: min
claims/000402/10.1038-s41586-025-08790-w.yaml:307:  - quantity: monitor-off period after the stimulus, range over scans
claims/000402/10.1038-s41586-025-08790-w.yaml-308-    value: 8.3 to 21.2
claims/000402/10.1038-s41586-025-08790-w.yaml-309-    tolerance: 7.47 to 23.32
claims/000402/10.1038-s41586-025-08790-w.yaml-310-    unit: min
claims/000402/10.1038-s41586-025-08790-w.yaml-311-  criterion: Per scan, the time from the first imaging frame to the first stimulus onset, and from the
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
p='claims/000402/10.1038-s41586-025-08790-w.yaml'
t=open(p).read()
rep={
"""  - quantity: monitor-on period before the stimulus, range over scans
    value: 0.15 to 5.5
    tolerance: 0.135 to 6.05
    unit: min
  - quantity: monitor-off period after the stimulus, range over scans
    value: 8.3 to 21.2
    tolerance: 7.47 to 23.32
    unit: min
""":"""  - quantity: monitor-on period before the stimulus, lower bound of the range over scans
    value: 0.15
    tolerance: 0.015
    unit: min
  - quantity: monitor-on period before the stimulus, upper bound of the range over scans
    value: 5.5
    tolerance: 0.55
    unit: min
  - quantity: monitor-off period after the stimulus, lower bound of the range over scans
    value: 8.3
    tolerance: 0.83
    unit: min
  - quantity: monitor-off period after the stimulus, upper bound of the range over scans
    value: 21.2
    tolerance: 2.12
    unit: min
""",
"""    the reported ranges widened by 10% of each bound (the tolerance field gives the widened range).""":
"""    the reported ranges widened by 10% of each bound (0.135 to 6.05 min and 7.47 to 23.32 min).""",
"""  - quantity: treadmill sampling rate, range
    value: 57 to 100
    tolerance: 51.3 to 110
    unit: Hz
""":"""  - quantity: treadmill sampling rate, lower bound of the range over scans
    value: 57
    tolerance: 5.7
    unit: Hz
  - quantity: treadmill sampling rate, upper bound of the range over scans
    value: 100
    tolerance: 10
    unit: Hz
""",
"""covering the imaging period (from the first to the last imaging frame, gaps within it allowed as
    the Methods say untracked frames are stored as NaN), at rates within tolerance.""":
"""covering the imaging period (from the first to the last imaging frame, gaps within it allowed as
    the Methods say untracked frames are stored as NaN), with every scan's treadmill rate in 51.3 to
    110 Hz (the range widened by 10% of each bound) and the eye camera rate within tolerance.""",
"""  expected:
    quantity: fraction of outputs onto a single soma, range over proofread neurons
    value: 60 to 95
    tolerance: 54 to 104.5
    unit: percent
""":"""  expected:
  - quantity: fraction of outputs onto a single soma, lower bound of the range over neurons
    value: 60
    tolerance: 6
    unit: percent
  - quantity: fraction of outputs onto a single soma, upper bound of the range over neurons
    value: 95
    tolerance: 5
    unit: percent
""",
"""figure shows the spread; reproduced when
    at least 90% of neurons fall in the widened range.""":"""figure shows the spread; reproduced when
    at least 90% of neurons fall in the range widened by 10% of each bound (54 to 100%, as a
    fraction cannot pass 100%).""",
"""  quote: We automatically detected and associated a total of 524 million synaptic clefts across both
    subvolumes (subvolume 35: 186 million, subvolume 65: 337 million). We manually identified
    synapses""":"""  quote: We automatically detected and associated a total of 524 million synaptic clefts across both
    subvolumes ... We manually identified synapses""",
}
for a,b in rep.items():
    assert a in t, a[:60]
    t=t.replace(a,b)
open(p,'w').write(t)
EOF
python3 tools/claims_check.py claims/000402/10.1038-s41586-025-08790-w.yaml paper/10.1038-s41586-025-08790-w.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -i "rather\|—" claims/000402/*.yaml; grep -c "^  data:" claims/000402/*.yaml; grep "^  data:" claims/000402/*.yaml | sort | uniq -c; git status --short
```

```
20
     17   data: elsewhere
      3   data: with_inputs
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
?? claims/000402/
?? scripts
```

**Agent calls Bash**

```bash
cd  f=claims/000402/*.yaml; grep -c "^  criterion:" $f; grep -c "^  expected:" $f; grep -c "^  statistics:" $f
```

```
35
29
0
```

**Agent**

I've written `claims/000402/10.1038-s41586-025-08790-w.yaml`. The quote checker reports 36 claims, 36 quotes and 0 problems. Nothing is committed.

**Text read.** I read the version of record (open access, from Europe PMC, PMC11981939): main text, figure legends, Methods, the legends of Extended Data Figs 1 to 5, and the captions of Extended Data Tables 1 to 3. The supplement is only a Reporting Summary and a Peer Review File, and no result rests on it.

**Code read.** github.com/AllenInstitute/MicronsFunctionalConnectomics at commit be24e51bd7090e9fb32a9099b4e0c6025342629b. It holds only the notebooks for Figs 3f, 3g, 6k and 7a to 7d.

**Claims.** There are 36, all with quotes. 35 have criteria and 29 have expected values. None has statistics: the paper reports no statistical test.
- **16 from the dataset:** the scans and their settings, the mask and unique-neuron counts, the VISp/higher-area split, z drift, the structural stack, the stimulus makeup and repeats, the spontaneous periods, Monet2 directions, oracle reliability (Fig 3f), direction tuning (Fig 3g), the behaviour recordings, and the photodiode decoding.
- **3 with inputs:** they need the CAVE co-registration tables (manual matches, the Extended Data Fig 4 signal-correlation check, Fig 6k).
- **17 elsewhere:** all EM and connectivity claims, plus the automatch and fiducial claims. Their data are at MICrONS Explorer, BossDB and CAVE.

**Details left open, with the readings named:**
- **Neuron consolidation:** how a group's height in z is measured (centroid range, or range plus one mask's height); distance to a group taken from its mean centroid or its nearest member.
- **Masks:** whether the dataset holds all masks with a somatic label, or only the somatic ones.
- **VISp share:** counted over masks, over unique neurons, or as share of the field of view. "Roughly" gets a ±15-point bound that the file sets itself.
- **z drift:** the sections are 10-min blocks or the two halves of the scan.
- **Stimulus duration:** stimulus-table trial times, or nominal clip lengths.
- **Oracle score:** whether a trial is one repeat of the 6 clips together, or each clip is scored apart. The paper's code reads the score from a precomputed table.
- **Fig 3g preferred direction:** the direction with the highest mean response, or the peak of a von Mises fit. The code's fit (radtune VonFit method 3) is not described and its code is not public.
- **Photodiode:** a stored flag, or my own decoding of the signal.
- **Extended Data Fig 4:** "nearest unit" by 3D centroid or within the 2D field.
- **CAVE version:** 1181 (what the code uses) or the latest public one.
- **Automatch precision:** the meaning of "attempted" (the unit or neuron is in the manual table, or its scan was).
- **Fiducial residual:** the 3.8 µm is a leave-one-out residual, or the residual after the third stage of the transform.
- **Synapse matching:** overlap with the annotation, or within 100 nm.
- **"Before proofreading" root:** the earliest materialization, or the root before the first edit.
- **Axon length:** from the released skeleton labels, or from NEURD.
- **Fig 6h cell classes:** which class table is meant.
- **The 94 axons:** fully extended only, or fully or partially extended.
- **"More than 900,000" connections:** synapses onto typed cells (the code's edge list sums to 812,686), or all output synapses.
- **Fig 6f and Fig 7a to c:** the paper gives a range with no share and names no measure. The 90% share and the same-layer measure are bounds the file sets itself, and it says so.

**Missing from the paper:**
- **Extended Data Table 1:** its cells (per-scan parameters) are not in the text and there is no PDF, so the scan claims use the Methods' figures for each group of scans.
- **No code** for the oracle score, the direction fits, or any count in the Results.
- **No materialization version** is given for the EM counts.
- **Not said to be released:** the 8,611 manual synapse annotations and the manual cell-class labels, so those accuracy figures are testable only if they are public.

**Inconsistencies in the paper,** noted in the file's opening comment and left unresolved:
- 1,994 somata plus 942 vessels make 2,936 fiducials, not the stated 2,934.
- Imaging ends at P80 in the Methods timeline and P81 in the main text.
- The timeline puts the structural stack after the perfusion.
- The 8.1% of masks excluded differs from the 8.0% the counts give.

## End of run

31 turns, 6 minutes, result: success.
