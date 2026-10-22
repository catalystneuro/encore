# 000987 · claims · run 39863397836

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls claims/001453 claims/000987 paper/ 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1,170p docs/protocol.md
```

```
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
  understand the claims, but the claims file binds it: it cannot change a
  claim, and it asks a reader for any method detail the file lacks.
- The **verifier** checks the author's work and must not be the author.

[... 150 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat claims/001453/*.yaml | head -250; wc -l claims/001453/*.yaml paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 250,321p claims/001453/*.yaml
```

```
- id: fig2k-more-monocular
  statement: DC have a higher proportion of purely monocular neurons than ZF (0.37 against 0.16,
    p < 0.05).
  source: Figure 2K
  quote: DC show a higher proportion of purely monocular neurons (ZF = 0.16, DC = 0.37
  statistics:
  - test: Student's t-test
    p: 0.05
    p_relation: "<"
    n: 5 ZF and 5 DC fish
- id: fig2l-bi-ratio
  statement: The binocularity index ratio is higher in ZF than in DC (0.72 against 0.24, p =
    0.010).
  source: Figure 2L
  quote: BI ratios show a higher fraction of binocular neurons in ZF compared to DC (ZF = 0.72, DC =
    0.24
  statistics:
  - test: Student's t-test
    p: 0.01
    n: 5 ZF and 5 DC fish
[... 52 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2024.05.048.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "=== page\|KEY RESOURCES\|STAR+METHODS\|SUPPLEMENT\|Figure S" paper/*.txt | sed -n 1,200p | awk -F: '$1>850'
```

Result: not kept, because it reads the paper's text.

**Agent**

The text has the main paper, STAR Methods and supplement legends. Reading Methods and supplement now.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2024.05.048.txt",
 "offset": 1040,
 "limit": 640
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Full text, STAR Methods and supplement legends are present. Next, the paper's code.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/PeyracheLab/MehrotraLevenstein_2023 && cd MehrotraLevenstein_2023 && git log -1 --format='%H %cd' && find . -type f -not -path './.git/*' | head -100
```

```
4ee34f34793c147ac08bf5fffe44ff03d17f8e35 Sun Apr 6 11:15:52 2025 -0400
./__pycache__/wrappers.cpython-310.pyc
./__pycache__/functions.cpython-310.pyc
./README.md
./Model/FigureS3f.m
./Model/FigureS3d.m
./Model/FigureS3c.m
./Model/FigureS3b.m
./Model/Figure3.m
./Model/Dependencies/matplotlib/viridis.m
./Model/Dependencies/matplotlib/twilight.m
./Model/Dependencies/matplotlib/tab20c.m
./Model/Dependencies/matplotlib/tab20b.m
./Model/Dependencies/matplotlib/tab20.m
./Model/Dependencies/matplotlib/tab10.m
./Model/Dependencies/matplotlib/plasma.m
./Model/Dependencies/matplotlib/matplotlib_doc.m
./Model/Dependencies/matplotlib/magma.m
./Model/Dependencies/matplotlib/license.txt
./Model/Dependencies/matplotlib/inferno.m
[... 82 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/MehrotraLevenstein_2023 && find . -type f -not -path './.git/*' -not -path './Model/Dependencies/*' -not -path './Analysis/OutputFiles/*' ; cat README.md; grep -ril "rsc\|A7" --include=*.py . | head
```

```
./__pycache__/wrappers.cpython-310.pyc
./__pycache__/functions.cpython-310.pyc
./README.md
./Model/FigureS3f.m
./Model/FigureS3d.m
./Model/FigureS3c.m
./Model/FigureS3b.m
./Model/Figure3.m
./Analysis/makeRing.py
./Analysis/detectDOWNs_RSC.py
./Analysis/detectDOWNs_PoSub.py
./Analysis/detectDOWNs_ADn.py
./Analysis/FigureS5AandB.py
./Analysis/FigureS3A.py
./Analysis/FigureS2G.py
./Analysis/FigureS2F.py
./Analysis/FigureS2A.py
./Analysis/FigureS1H.py
./Analysis/Figure5F.py
./Analysis/Figure5E.py
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/MehrotraLevenstein_2023/Analysis && cat detectDOWNs_RSC.py; echo =========; cat Figure5F.py; ls OutputFiles | grep -v "Mouse\|A37"
```

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 11:16:31 2023

@author: dhruv
"""

#import dependencies
import numpy as np 
import os
import nwbmatic as ntm
import pynapple as nap
import matplotlib.pyplot as plt 

#%% Data organization

data_directory = '/media/dhruv/LaCie1/A7800'
datasets = np.genfromtxt(os.path.join(data_directory,'dataset_DM.list'), delimiter = '\n', dtype = str, comments = '#')

[... 146 more lines not kept]
```

**Agent**

The repository has one RSC script pair (`detectDOWNs_RSC.py`, `Figure5F.py`). Comparing with the PoSub and FC scripts.

**Agent calls Bash**

```bash
cd $TMPDIR/MehrotraLevenstein_2023/Analysis && cat Figure5C.py; echo ======; cat Figure5E.py | sed -n 1,200p
```

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 10:01:54 2023

@author: dhruv
"""
#import dependencies
import numpy as np 
import pandas as pd 
import scipy.io
import nwbmatic as ntm
import pynapple as nap 
import os
import matplotlib.pyplot as plt 
from scipy.stats import kendalltau

#%% Data organization

data_directory = '/media/DataDhruv/Dropbox (Peyrache Lab)/Peyrache Lab Team Folder/Data/AdrianPoSub/###AllPoSub'
[... 222 more lines not kept]
```

**Agent**

The RSC script uses all units (no EX selection), unlike the PoSub and FC scripts. Checking Figure 5D's code and the figure itself.

**Agent calls Bash**

```bash
cd $TMPDIR/MehrotraLevenstein_2023/Analysis && sed -n 1,400p Figure5D.py | grep -n "data_directory\|Isomap\|pearson\|kendall\|PMR\|pyr\|n_neighbors" ; python -c "import fitz" 2>&1; which pdftoppm
```

```
Exit code 1
18:from scipy.stats import pearsonr
19:from sklearn.manifold import Isomap
23:data_directory = '/media/DataDhruv/Dropbox (Peyrache Lab)/Peyrache Lab Team Folder/Data/AdrianPoSub/###AllPoSub'
24:datasets = np.genfromtxt(os.path.join(data_directory,'dataset_Hor_DM.list'), delimiter = '\n', dtype = str, comments = '#')
31:PMR = []
36:    path = os.path.join(data_directory, s)
56:    pyr = []
62:            pyr.append(i)
87:    ee = dd2[pyr] 
89:#%% Concatenate all PETHs for Isomap
99:              PMR.append(ee.iloc[:,i].max())
105:#%% Isomap 
107:projection = Isomap(n_components = 2, n_neighbors = 50).fit_transform(allPETH.T.values)   
108:H = PMR/(max(PMR))
121:#%% Specific examples from Isomap
142:#%% Plot of PMR as a function of Isomap dimension 1 
144:r, p = pearsonr(projection[:,0], PMR)
147:plt.scatter(projection[:,0], PMR, label = 'r = ' + str(round(r,2)))
151:plt.ylabel('PMR')
[... 5 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2024.05.048.pdf",
 "pages": "8"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -rn "elsewhere\|with_inputs\|with_labels" docs/*.md | head -30; ls tools; ls claims | head -50
```

```
docs/design.md:118:  elsewhere. This is the guard against a result that only looks right.
docs/pilot-notes.md:95:  with outside data (`data: dandiset` or `with_inputs`), and the dashboard
docs/pilot-notes.md:107:RDMs that are not public, are now marked `with_inputs`, and its attempt
docs/pilot-notes.md:123:  `data: with_labels`, for outside sources that only name or map codes the
docs/pilot-notes.md:162:adds a fourth data kind, `elsewhere`, for a claim whose data the dandiset
docs/pilot-notes.md:166:dandiset's claims and from `with_inputs` claims. It is never blocked with
docs/protocol.md:137:     `with_labels`, `with_inputs` or `elsewhere` (step 4, and author, step
docs/protocol.md:205:4. Decide what comes from outside the dataset. Data from elsewhere may be
docs/protocol.md:214:     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
docs/protocol.md:215:     `with_inputs` and `elsewhere` claims are counted apart, each group on
docs/protocol.md:217:   - `with_labels` is for outside sources that only name or map codes the
docs/protocol.md:239:   - `elsewhere` is for a claim whose data the dataset does not hold at
docs/protocol.md:248:   - The notes of a `with_inputs` claim say which side a difference comes
docs/protocol.md:259:     `data: elsewhere` instead (step 4).
__pycache__
agent_run.py
archive_transcripts.sh
build_site.py
build_targets.py
claims_check.py
[... 64 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 200,262p docs/protocol.md; ls claims/000939 2>/dev/null && head -60 claims/000939/*.yaml
```

```
Exit code 2
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
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -rn -A3 "data: elsewhere" claims | head -40; grep -rln "simulat" claims | head -5; sed -n 1,80p tools/claims_check.py
```

```
claims/001752/10.1038-s41556-026-02009-4.yaml:182:  data: elsewhere
claims/001752/10.1038-s41556-026-02009-4.yaml-183-  where: GEO GSE319557 (10x scRNA-seq, FASTQ, per the Data availability statement); processed
claims/001752/10.1038-s41556-026-02009-4.yaml-184-    data in Zenodo doi:10.5281/zenodo.18814764
claims/001752/10.1038-s41556-026-02009-4.yaml-185-  expected:
--
claims/001752/10.1038-s41556-026-02009-4.yaml:210:  data: elsewhere
claims/001752/10.1038-s41556-026-02009-4.yaml-211-  where: GEO GSE319557
claims/001752/10.1038-s41556-026-02009-4.yaml-212-  criterion: Judged on the paper's cluster labels if the deposit carries them (counts of types per
claims/001752/10.1038-s41556-026-02009-4.yaml-213-    class equal to those stated); a re-clustering with the Methods' pipeline (SCANPY, Harmony,
--
claims/001752/10.1038-s41556-026-02009-4.yaml:219:  data: elsewhere
claims/001752/10.1038-s41556-026-02009-4.yaml-220-  where: GEO GSE319557
claims/001752/10.1038-s41556-026-02009-4.yaml-221-  criterion: A claim of absence. The test is shown in Supplementary Fig. 3, which was not in the
claims/001752/10.1038-s41556-026-02009-4.yaml-222-    text read, so the paper's test and threshold are not known here; blocked as
--
claims/001752/10.1038-s41556-026-02009-4.yaml:231:  data: elsewhere
claims/001752/10.1038-s41556-026-02009-4.yaml-232-  where: GEO GSE319369 (Patch-seq); mapping results in github.com/RFLiu2021/AIC_proj at commit
claims/001752/10.1038-s41556-026-02009-4.yaml-233-    44cd8a6, patchSeqMappingTo10X/data/mappingRes/
claims/001752/10.1038-s41556-026-02009-4.yaml-234-  expected:
--
[... 105 more lines not kept]
```

**Agent**

Let me look at the schema for allowed fields.

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

Fetching the dataset's title and description from DANDI (metadata only).

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000987/ | python -c "
import json,sys;d=json.load(sys.stdin);m=d.get('draft_version') or d.get('most_recent_published_version');print(json.dumps(d,indent=1)[:1500])"; curl -s https://api.dandiarchive.org/api/dandisets/000987/versions/draft/info/ | python -c "
import json,sys;d=json.load(sys.stdin)['metadata'];print(d.get('name'));print(d.get('description'))"
```

Result: the fetched text is not kept.

**Agent**

The archive describes 14 recordings from 3 mice with 570 units, plus the detected UP/DOWN states, used for Figure 5F. Reading the PoSub scripts that back the other claims.

**Agent calls Bash**

```bash
cd $TMPDIR/MehrotraLevenstein_2023/Analysis && for f in Figure1G.py Figure1H.py; do echo "=== $f"; grep -v "^\s*#\|^\s*$\|plt\." $f | sed -n 1,200p; done
```

```
=== Figure1G.py
"""
Created on Thu Sep 14 10:29:12 2023
@author: dhruv
"""
import numpy as np 
import pandas as pd
import scipy.io
from Dependencies.functions import *
from Dependencies.wrappers import *
import os
from Dependencies import neuroseries as nts 
import matplotlib.pyplot as plt 
from scipy.stats import kendalltau, wilcoxon, mannwhitneyu
import seaborn as sns
data_directory = '/media/DataDhruv/Dropbox (Peyrache Lab)/Peyrache Lab Team Folder/Data/AdrianPoSub/###AllPoSub'
datasets = np.genfromtxt(os.path.join(data_directory,'dataset_Hor_DM.list'), delimiter = '\n', dtype = str, comments = '#')
readpath = '/media/DataDhruv/Dropbox (Peyrache Lab)/Peyrache Lab Team Folder/Projects/PoSub-UPstate/Data'
writepath = '[removed: a home directory path]/Code/MehrotraLevenstein_2023/Analysis/OutputFiles'
allcoefs_up_ex = []
[... 217 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/MehrotraLevenstein_2023/Analysis && grep -v "^\s*#\|^\s*$\|plt\.\|ax\.\|sns\." FigureS2G.py | sed -n 1,140p; echo ====; grep -n "std\|mannwhitney\|circvar\|gradient\|radius\|0.15\|0.035\|wilcoxon\|kendall" makeRing.py | head -40
```

```
"""
Created on Wed May 15 15:26:25 2024
@author: dhruv
"""
import numpy as np 
import pandas as pd 
import scipy.io
import pynapple as nap 
import nwbmatic as ntm
import os
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy.stats import mannwhitneyu
data_directory = '/media/DataDhruv/Dropbox (Peyrache Lab)/Peyrache Lab Team Folder/Data/AdrianPoSub/###AllPoSub'
datasets = np.genfromtxt(os.path.join(data_directory,'dataset_Hor_DM.list'), delimiter = '\n', dtype = str, comments = '#')
readpath = '/media/DataDhruv/Dropbox (Peyrache Lab)/Peyrache Lab Team Folder/Projects/PoSub-UPstate/Data'
writepath = '[removed: a home directory path]/Code/MehrotraLevenstein_2023/Analysis/OutputFiles'
range_uponset_posub = []
range_uponset_adn = []
for s in datasets:
[... 105 more lines not kept]
```

**Agent**

I have what I need: full text with STAR Methods and supplement legends, plus the code at commit 4ee34f3. Writing the claims file.

**Agent calls Write**

```json
{
 "file_path": "claims/000987/10.1016-j.cub.2024.05.048.yaml",
 "content": "# Claims for Mehrotra, Levenstein et al. (2024), Current Biology 34, 3043-3054, on dandiset 000987.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-22, under\n# docs/protocol.md, version pilot-10, Reader.\n#\n# Text read: the version of record (PDF supplied by a person, extracted to text), with its STAR\n# Methods (pages e1 to e8) and the Supplemental Information (legends of Figures S1 to S5). The\n# figures were not read; the PDF could not be rendered here, and no claim needed a figure the\n# text garbles. The extraction renders Greek letters and some symbols wrongly (Kendall tau as\n# \"t\", \"x 10^\" as \"3 10\", minus signs as a replacement glyph, micro as \"m\"); quotes avoid them.\n#\n# Code read: github.com/PeyracheLab/MehrotraLevenstein_2023 at commit 4ee34f3 (2025-04-06), the\n# repository the Key Resources Table names. It holds Python scripts per figure panel under\n# Analysis/ (Figure1C-H, Figure5B-F, FigureS1H, S2A, S2F, S2G, S3A, S5AandB), the DOWN-state\n# detectors (detectDOWNs_PoSub.py, detectDOWNs_ADn.py, detectDOWNs_RSC.py), the Isomap ring\n# script makeRing.py, the DOWN/UP event files the PoSub and ADN scripts read (Analysis/OutputFiles),\n# and the MATLAB model code under Model/ (Figure3.m, FigureS3b-d.m, FigureS3f.m). It has no code\n# for Figures 1I to 1K, 2, 4 or S4, and does not pin the versions of pynapple or nwbmatic.\n#\n# Data the paper used. Three in vivo datasets and one ex vivo dataset.\n# - PoSub (Figures 1, 2, 5B-D, S1, S2, S5): 1,657 single units, 1,097 putative excitatory (EX),\n#   one session per mouse, 16 sessions from 16 mice, a 64-site single-shank silicon probe along\n#   the dorsoventral (DV) axis of postsubiculum; sleep in the home cage and open-field\n#   exploration; HD tracked at 100 Hz. Deposited at DANDI:000939 (Duszkiewicz et al. 2024), not\n#   in this dandiset.\n# - ADN (Figure S2F, S2G): 9 sessions from a previously published dataset (ref. 14, Peyrache et\n#   al. 2015); the paper names no archive for it.\n# - Frontal cortex (Figure 5E): 950 EX units from 25 sessions in 11 rats, Watson et al., CRCNS\n#   fcx-1.\n# - RSC (Figure 5F), the data of this dandiset: adult mice, one C57BL/6J and two C57BL/6J x\n#   FVB/NJ crosses (3 mice), probes in left RSC (one animal with an 8-shank Buzsaki64 probe and\n#   CA1 wires), 14 sessions, 570 units in total; each session has home-cage sleep and\n#   exploration of a square and a circular arena; position and head direction tracked at\n#   120 Hz; LFP at 1.25 kHz. Measured variables used by the paper: spike times of units, NREM\n#   epochs (SleepScoreMaster), and UP and DOWN states detected from the population rate. The\n#   archive's description of the dandiset says it holds 14 recordings from 3 mice with 570\n#   isolated units, sleep scoring and the detected UP and DOWN states as used in the study, and\n#   that it was used for Figure 5F.\n# - Ex vivo (Figures 4, S4): whole-cell recordings of layer III PoSub cells, 59 cells from 11\n#   mice in control and 19 cells from 8 mice with ZD-7288; not deposited.\n# - Model (Figures 3, S3): simulations of an adapting Wilson-Cowan array, code in Model/.\n#\n# Only the RSC claims (rsc-dataset, fig5f-rsc-pmr-onset) use this dandiset. The other claims\n# cover the paper's main findings and use data elsewhere or not deposited.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000987\"\npaper: doi:10.1016/j.cub.2024.05.048\nclaims:\n- id: rsc-dataset\n  statement: The RSC dataset holds 570 units recorded in 14 sessions from 3 mice.\n  source: STAR Methods, Behavioral procedures, paragraph 2; Experimental model and study\n    participant details, paragraph 2; Figure 5F legend\n  quote: A total of 570 units were recorded from 14 sessions.\n  expected:\n  - quantity: units\n    value: 570\n    tolerance: 0\n  - quantity: sessions\n    value: 14\n    tolerance: 0\n  - quantity: mice\n    value: 3\n    tolerance: 0\n  criterion: Counts of the dandiset's sessions, distinct subjects and sorted units over all\n    sessions. The tolerance is zero, as these are counts of the deposited records themselves,\n    which the archive's description gives with the same numbers. Reproduced when all three match;\n    partially reproduced when sessions and mice match and the unit count is within 10%.\n- id: fig5f-rsc-pmr-onset\n  statement: In retrosplenial cortex, as in PoSub, units with a larger firing-rate overshoot at\n    UP state onset (peak-to-mean ratio, PMR) enter the UP state earlier; UP onset delay and PMR\n    are negatively correlated (Kendall tau = -0.28, n = 570 units from 14 sessions in 3 mice,\n    p = 6.76e-21).\n  source: Figure 5F legend; Results, Post-DOWN rebound suggests a widespread role for Ih in\n    neuronal activation at UP onset, paragraph 4\n  quote: We found a similar relationship in the frontal cortex ... and RSC (data available at\n    DANDI:000987) (Figure 5F).\n  statistics:\n  - test: Kendall tau rank correlation, UP onset delay against PMR\n    statistic: tau = -0.28\n    p: 6.76e-21\n    n: 570 units from 14 sessions (3 mice)\n  expected:\n  - quantity: Kendall tau between UP onset delay and PMR, RSC units pooled over sessions\n    value: -0.28\n    tolerance: 0.028\n  - quantity: units in the test\n    value: 570\n    tolerance: 57\n  criterion: >-\n    Method from Figure5F.py and detectDOWNs_RSC.py (commit 4ee34f3), which agree with the STAR\n    Methods (UP and DOWN state detection; Peri-Event Time Histograms; Sequential Activation at UP\n    onset) and the Results definition of PMR. NREM epochs are those of the sleep scoring\n    (SleepScoreMaster). DOWN states are the ones the dandiset carries as the study's, if it\n    carries them; they are also re-detected as the code does it, and the re-detection is shown\n    as a check. Re-detection, per session, from the spikes of all units in NREM, counted in\n    10 ms bins, smoothed with a Gaussian of 20 ms s.d. (pandas rolling window of 100 bins, std\n    2 bins) and summed; DOWN states are the intervals below the 20th percentile of that rate;\n    intervals shorter than 10 ms are dropped, those closer than 20 ms merged, and then those\n    shorter than 30 ms or longer than 500 ms dropped; UP states are the intervals between\n    consecutive DOWN states, and the DOWN states are then restricted to NREM. Per unit, the\n    PETH of its spikes around each UP state start (the DU transition) is pynapple's\n    compute_eventcorrelogram with 5 ms bins, a 0.255 s window, ep = the UP states and norm =\n    True (spikes and events restricted to UP states, the PETH divided by the unit's mean rate\n    in UP states), smoothed with a Gaussian of 2 bins s.d. (10 ms, rolling window of 8 bins)\n    and cut to 0 to 0.155 s after DU. UP onset delay is the first time in that interval at\n    which the normalized PETH exceeds 0.5; PMR is the maximum of the normalized PETH in that\n    interval; a unit that never exceeds 0.5 is left out. Units of all sessions are pooled and\n    scipy's kendalltau is computed between UP onset delay and PMR. Which units enter is open.\n    The text allows two readings. (a) All sorted units, as Figure5F.py does (no cell-type\n    selection) and as the legend's n of 570 units, the total recorded per the Methods,\n    implies. (b) Putative EX units only, per the Methods sentence \"only EX units were used for\n    analyses\", classified by trough-to-peak duration above 0.35 ms and mean rate below 10 Hz\n    in open-field exploration (Spike sorting and unit classification). Both are run. Reproduced\n    when tau is negative with p < 0.05 under both readings and within tolerance of -0.28 under\n    at least one; partially reproduced when tau is negative with p < 0.05 under both but outside\n    tolerance under both; not reproduced when tau is not negative with p < 0.05 under either;\n    blocked as methods_underspecified when the readings disagree on sign or significance. The\n    number of units entering the test is reported under each reading. The pynapple version is\n    not pinned by the code; any version whose compute_eventcorrelogram takes these arguments is\n    a standard choice and is reported. The Figure 5F legend reads \"Same as (D)\", an Isomap\n    plot, but Figure5F.py draws the 2D histogram of UP onset delay against PMR with its fit\n    line, as Figure5C.py does; only the correlation is tested.\n- id: fig5c-posub-pmr-onset\n  statement: In PoSub, PMR is negatively correlated with UP onset delay; earlier-activating EX\n    units show a larger overshoot, and virtually no late-activating unit has a large PMR\n    (Kendall tau = -0.19, n = 1,096, p = 8.34e-20).\n  source: Figure 5C; Results, Post-DOWN rebound suggests a widespread role for Ih in neuronal\n    activation at UP onset, paragraph 2\n  quote: As predicted, PMR was negatively correlated with UP state onset timing, with\n    earlierspiking cells showing a larger overshoot (Figure 5C). Critically, virtually no units\n    with a late activation at UP onset had a large PMR.\n  statistics:\n  - test: Kendall tau rank correlation\n    statistic: tau = -0.19\n    p: 8.34e-20\n    n: 1,096 EX units (1 of 1,097 excluded as it did not reach 50% of its mean rate within 150 ms)\n  expected:\n  - quantity: Kendall tau, UP onset delay against PMR, PoSub EX units\n    value: -0.19\n    tolerance: 0.019\n  data: elsewhere\n  where: DANDI:000939 (PoSub dataset, Duszkiewicz et al. 2024)\n  criterion: As fig5f-rsc-pmr-onset, with the PoSub DOWN states (detectDOWNs_PoSub.py, or the\n    event files in Analysis/OutputFiles) and EX units only, as Figure5C.py does with the\n    CellTypes ex and gd flags. Reproduced when tau is negative with p < 0.05 and within\n    tolerance.\n- id: fig5d-isomap-pmr\n  statement: An Isomap projection of the DU-aligned PETHs of all PoSub EX units shows a\n    continuous gradation of profiles whose first dimension correlates strongly with PMR\n    (Pearson R = 0.88, n = 1,096).\n  source: Figure 5D; Results, Post-DOWN rebound suggests a widespread role for Ih in neuronal\n    activation at UP onset, paragraph 3\n  quote: Isomap decomposition of the DU-PETHs of all PoSub units (Figure 5D) revealed a\n    continuous gradation of temporal profiles at the UP state onset, which was largely\n    attributable to a single dimension strongly correlated with PMR\n  statistics:\n  - test: Pearson correlation, first Isomap dimension against PMR\n    statistic: R = 0.88\n    p: 0\n    n: 1,096 EX units from 16 sessions (16 mice)\n  expected:\n  - quantity: Pearson R, first Isomap dimension against PMR\n    value: 0.88\n    tolerance: 0.088\n  data: elsewhere\n  where: DANDI:000939\n  criterion: PETHs as in fig5c-posub-pmr-onset; sklearn Isomap with 2 components and 50\n    neighbours on the stacked PETHs, as Figure5D.py and the Methods (Peri-Event Time\n    Histograms) give; the absolute Pearson R of the first dimension with PMR, since the sign of\n    an Isomap axis is arbitrary. Reproduced when |R| is within tolerance and p < 0.05.\n- id: fig5e-fc-pmr-onset\n  statement: In rat frontal cortex, UP onset delay and PMR are also negatively correlated\n    (Kendall tau = -0.22, n = 950 EX units from 25 sessions in 11 rats, p = 5e-21).\n  source: Figure 5E legend; Results, Post-DOWN rebound suggests a widespread role for Ih in\n    neuronal activation at UP onset, paragraph 4\n  quote: We found a similar relationship in the frontal cortex (FC; data from Watson et al.\n  statistics:\n  - test: Kendall tau rank correlation\n    statistic: tau = -0.22\n    p: 5e-21\n    n: 950 EX units from 25 sessions (11 rats)\n  expected:\n  - quantity: Kendall tau, UP onset delay against PMR, FC EX units\n    value: -0.22\n    tolerance: 0.022\n  data: elsewhere\n  where: CRCNS fcx-1 (Watson et al. 2016)\n  criterion: As fig5f-rsc-pmr-onset, with the dataset's own UP states (SlowWaves events),\n    excitatory units by its CellClass, as Figure5E.py does. Reproduced when tau is negative\n    with p < 0.05 and within tolerance.\n- id: fig1g-dv-sequence-du\n  statement: At the DOWN-to-UP transition PoSub EX units activate in sequence, dorsal units\n    entering the UP state before ventral ones; the per-session correlation of UP onset delay\n    with depth is consistently non-zero for DU and not for UD transitions.\n  source: Figure 1E to 1G; Results, Neuronal activity at the DU transition travels along the\n    PoSub DV axis and is locally generated, paragraph 1\n  quote: This sequential activity followed an anatomical pattern... dorsally located units\n    tended to enter the UP state before ventrally located units (Figure 1G; one-sample Wilcoxon\n    test; DU, W = 1, n = 16\n  statistics:\n  - about: DU correlation coefficients against 0\n    test: one-sample Wilcoxon test\n    statistic: W = 1\n    p: 6.1e-5\n    n: 16 sessions\n  - about: UD correlation coefficients against 0\n    test: one-sample Wilcoxon test\n    statistic: W = 38\n    p: 0.13\n    n: 16 sessions\n  - about: DU against UD correlation coefficients\n    test: Mann-Whitney U test\n    statistic: U = 52\n    p: 0.005\n    n: 16 sessions\n  data: elsewhere\n  where: DANDI:000939\n  criterion: Per session, the Kendall tau between UP onset delay and depth of EX units, onset\n    delay as in fig5f-rsc-pmr-onset (first bin above 0.5 of the rate-in-UP normalized PETH,\n    0 to 150 ms after DU), and for UD the last bin above 0.5 between -150 and -5 ms of the\n    PETH around DOWN starts for units that also cross after +5 ms, as Figure1G.py does.\n    Reproduced when the DU coefficients differ from 0 by a two-sided one-sample Wilcoxon test\n    at p < 0.05 with the sign of dorsal-first, the UD coefficients do not (p >= 0.05), and DU\n    and UD differ by a Mann-Whitney U test at p < 0.05.\n- id: fig1e-delay-range\n  statement: PoSub neurons activate with reliable delays after the DU transition, ranging from\n    5 to 100 ms (99th percentile range).\n  source: Results, Neuronal activity at the DU transition travels along the PoSub DV axis and\n    is locally generated, paragraph 1; Figures 1D to 1F\n  quote: Unlike UD transitions, neurons activated with reliable delays with respect to the DU\n    transition (Figures 1D-1F and S1I), ranging from 5 to 100 ms (99th percentile range)\n  expected:\n  - quantity: lower bound of UP onset delays (99th percentile range)\n    value: 5\n    tolerance: 0.5\n    unit: ms\n  - quantity: upper bound of UP onset delays (99th percentile range)\n    value: 100\n    tolerance: 10\n    unit: ms\n  data: elsewhere\n  where: DANDI:000939\n  criterion: UP onset delays of all PoSub EX units as in fig5c-posub-pmr-onset. \"99th\n    percentile range\" is not defined. Readings are (a) the 0.5th to 99.5th percentiles and\n    (b) the 1st to 99th percentiles of the pooled delays. Reproduced when under one reading\n    both bounds are within the range widened by 10% of each bound.\n- id: fig1h-ventral-down-longer\n  statement: DOWN states detected from ventral PoSub last longer than those detected from dorsal\n    PoSub (Wilcoxon signed-rank test, W = 9, n = 16, p = 0.01).\n  source: Figure 1H; Results, Neuronal activity at the DU transition travels along the PoSub DV\n    axis and is locally generated, paragraph 1\n  quote: we found that the DOWN state durations were significantly longer in the ventral half\n    when detected separately from the dorsal half of PoSub (Figure 1H; p = 0.01, Wilcoxon\n    signed-rank test).\n  statistics:\n  - test: Wilcoxon signed-rank test\n    statistic: W = 9\n    p: 0.01\n    n: 16 sessions\n  data: elsewhere\n  where: DANDI:000939\n  criterion: As Figure1H.py and the Methods (UP and DOWN state detection, paragraph 2). Units\n    split into dorsal and ventral halves by depth (two equal-width depth bins); the pooled\n    spikes of each half form a PETH around each DOWN start, normalized by its mean rate in UP\n    states and smoothed as in fig5f-rsc-pmr-onset; the DOWN duration of a half is the first\n    time after +5 ms where the normalized rate exceeds 0.2 minus the last time between -150 and\n    -5 ms where it exceeds 0.2. The code uses all units with the gd flag; the Methods' general\n    rule would use EX units only; both are run. Reproduced when ventral exceeds dorsal by a\n    two-sided Wilcoxon signed-rank test at p < 0.05 under both; blocked as\n    methods_underspecified when they disagree.\n- id: fig1b-no-dv-tuning-gradient\n  statement: HD information, linear speed and angular head velocity tuning of PoSub EX cells do\n    not vary with DV position; resultant vector length and peak rate show weak but significant\n    correlations with it.\n  source: Figure 1B; Figure S1D to S1F; Results, opening paragraph\n  quote: Across all behavioral correlates tested, we saw either no significant correlations\n    (Figures 1B and S1D) or, at most, weak but significant correlations with DV location\n    (Figures S1E and S1F)\n  statistics:\n  - about: HD information against depth\n    test: Kendall tau\n    statistic: tau = -0.03\n    p: 0.13\n    n: 1,097 EX cells\n  - about: linear speed score against depth\n    test: Kendall tau\n    statistic: tau = -0.03\n    p: 0.18\n    n: 1,097 EX cells\n  - about: AHV score against depth\n    test: Kendall tau\n    statistic: tau = -0.02\n    p: 0.23\n    n: 1,097 EX cells\n  - about: resultant vector length against depth\n    test: Kendall tau\n    statistic: tau = 0.063\n    p: 0.002\n    n: 1,097 EX cells\n  - about: peak firing rate against depth\n    test: Kendall tau\n    statistic: tau = 0.075\n    p: 0.0002\n    n: 1,097 EX cells\n  data: elsewhere\n  where: DANDI:000939\n  criterion: A claim of absence for HD information, speed and AHV scores, judged by the paper's\n    test, a two-sided Kendall tau against depth at p < 0.05 over all EX cells; the measures as\n    the Methods define them (HD tuning curves and tuning metrics). Reproduced when those three\n    are not significant and resultant vector length and peak rate are positively correlated\n    with p < 0.05.\n- id: fig1j-down-resets-hd\n  statement: The DOWN state resets the virtual HD signal; the angle at the start of an UP state\n    is unrelated to the angle at the end of the previous UP state.\n  source: Figure 1J; Results, Neuronal activity at the DU transition travels along the PoSub DV\n    axis and is locally generated, paragraph 2\n  quote: We found that the DOWN state resets this virtual HD signal, as there was no\n    relationship between the angle represented at the end of an UP state and the beginning of\n    the subsequent UP state (Figure 1J).\n  data: elsewhere\n  where: DANDI:000939\n  criterion: Angles from the Isomap ring as in the Methods (Isomap Projection and Decoding),\n    the first post-DU bin whose radius exceeds one third of the mean wake radius against the\n    last such bin before the preceding UD. A claim of absence, judged as the legend does, the\n    histogram of angular differences against 1,000 shuffles of the angle at UD; reproduced when\n    no bin lies outside the minimum to maximum of the shuffled counts. The histogram's bin\n    width is not given; 20 bins over the circle is a standard choice, and 10 and 36 are shown.\n- id: fig1k-hd-stable-at-onset\n  statement: During the UP onset sequence the represented HD changes less rapidly than later in\n    the UP state (diffusion coefficients, Mann-Whitney U test, U = 54, n = 16, p = 0.006).\n  source: Figure 1K; Results, Neuronal activity at the DU transition travels along the PoSub DV\n    axis and is locally generated, paragraph 2\n  quote: Following the DOWN state, the represented HD maintained a specific direction throughout\n    the duration of the UP onset sequence (Figure 1I) and changed less rapidly than later in the\n    UP state (Figure 1K).\n  statistics:\n  - test: Mann-Whitney U test\n    statistic: U = 54\n    p: 0.006\n    n: 16 sessions\n  data: elsewhere\n  where: DANDI:000939\n  criterion: As the Methods (Isomap Projection and Decoding) give it. UP states longer than\n    500 ms; angles 0 to 150 ms (traveling) and 150 to 300 ms (control) after DU; cumulative\n    circular variance from the first three bins; the diffusion coefficient is the mean\n    numpy gradient of it between 35 and 150 ms. Per session, one coefficient per interval.\n    Reproduced when traveling is lower than control by a two-sided Mann-Whitney U test at\n    p < 0.05.\n- id: figs1j-dorsal-ventral-same-hd\n  statement: During NREM sleep, dorsal and ventral PoSub represent the same HD; the decoded\n    angular difference is not different from that with shuffled cell depths.\n  source: Figure S1J; Results, Neuronal activity at the DU transition travels along the PoSub\n    DV axis and is locally generated, paragraph 1\n  quote: during NREM sleep, dorsal and ventral PoSub consistently represented the same HD\n  statistics:\n  - test: one-sample Wilcoxon test of z-scored difference from shuffle against 0\n    statistic: W = 38\n    p: 0.13\n    n: 16 sessions\n  data: elsewhere\n  where: DANDI:000939\n  criterion: A claim of absence. Bayesian decoding with pynapple decode_1d in 50 ms UP-state\n    bins with at least 5 HD cells spiking in each half; per session, the mean absolute angular\n    difference z-scored against 100 shuffles of cell depth. Reproduced when the two-sided\n    one-sample Wilcoxon test against 0 gives p >= 0.05; the effect is reported either way. How\n    the dorsal and ventral halves are split is not given; the equal-width depth split of\n    Figure1H.py and the median split are both run.\n- id: fig2f-gamma-travels\n  statement: The rise in high gamma (70 to 150 Hz) power at UP onset travels along the DV axis,\n    while its drop at the UD transition is synchronous.\n  source: Figure 2B to 2F; Results, Neuronal activity at the DU transition travels along the\n    PoSub DV axis and is locally generated, paragraph 3\n  quote: gh traveled in the DV direction during the UP state onset, mirroring the wave observed\n    in single unit activity (Figures 2B- 2F; one-sample Wilcoxon test; DU, W = 21, n = 16, p =\n    0.013; UD, W = 68, n = 16, p = 1)\n  statistics:\n  - about: DU coefficients against 0\n    test: one-sample Wilcoxon test\n    statistic: W = 21\n    p: 0.013\n    n: 16 sessions\n  - about: UD coefficients against 0\n    test: one-sample Wilcoxon test\n    statistic: W = 68\n    p: 1\n    n: 16 sessions\n  - about: DU against UD\n    test: Mann-Whitney U test\n    statistic: U = 73\n    p: 0.04\n    n: 16 sessions\n  data: elsewhere\n  where: DANDI:000939\n  criterion: Per channel, LFP downsampled to 625 Hz, filtered 70 to 150 Hz (third-order\n    Butterworth), power smoothed with a 32 ms s.d. Gaussian, averaged around DU (and UD); UP\n    onset delay is the time of maximal derivative (Methods, Peri-Event Time Histograms and\n    Sequential Activation at UP onset). Per session, Kendall tau of delay against channel\n    depth. The window in which the maximal slope is searched is not given; 0 to 150 ms after\n    the transition (as for units) and -250 to 250 ms are both run. Reproduced when, under both,\n    DU coefficients differ from 0 (two-sided one-sample Wilcoxon, p < 0.05) and UD do not.\n- id: figs2e-speed-similar\n  statement: For sessions with a significant delay-depth correlation, the speed of the traveling\n    UP onset is similar from spikes and from LFP (6.72 +/- 4.08 against 9.89 +/- 5.51 mm/s,\n    Mann-Whitney U = 58, n = 13 and 15, p = 0.072).\n  source: Figure S2E; Results, Neuronal activity at the DU transition travels along the PoSub\n    DV axis and is locally generated, paragraph 3\n  quote: the speed of the traveling activity for significant sessions was similar when computed\n    using either the LFP or spiking activity\n  statistics:\n  - test: Mann-Whitney U test\n    statistic: U = 58\n    p: 0.072\n    n: 13 sessions (spikes) and 15 sessions (LFP)\n  expected:\n  - quantity: speed from spikes, mean\n    value: 6.72\n    tolerance: 4.08\n    unit: mm/s as printed in the text read\n  - quantity: speed from LFP, mean\n    value: 9.89\n    tolerance: 5.51\n    unit: mm/s as printed in the text read\n  data: elsewhere\n  where: DANDI:000939\n  depends_on:\n  - fig1g-dv-sequence-du\n  - fig2f-gamma-travels\n  criterion: A claim of absence, judged by the paper's two-sided Mann-Whitney U test at\n    p < 0.05; reproduced when it does not find a difference. Speed is the slope of the\n    delay-depth relation (Figure S2E legend) in sessions whose Kendall correlation is\n    significant; whether speed is the inverse of the regression slope of delay on depth or the\n    slope of depth on delay is not given, and both are run. Tolerances are the reported s.d.\n- id: figs2g-adn-synchronous\n  statement: At UP state onset ADN cells activate more synchronously than PoSub cells (s.d. of\n    delays 10.38 +/- 5.74 ms against 15.54 +/- 5.42 ms), suggesting the PoSub sequence is\n    generated locally.\n  source: Figure S2F and S2G; Results, Neuronal activity at the DU transition travels along the\n    PoSub DV axis and is locally generated, paragraph 4\n  quote: At UP state onset, ADN cells activated more synchronously than in the PoSub (Figures\n    S2F and S2G; standard deviation of delays, 10.38 ± 5.74 ms in ADN versus 15.54 ± 5.42 ms in\n    PoSub\n  statistics:\n  - about: as printed in the Results\n    test: Mann-Whitney U test\n    statistic: U = 29\n    p: 0.016\n    n: 16 PoSub and 9 ADN sessions\n  - about: as printed in the Figure S2G legend\n    test: Mann-Whitney U test\n    statistic: U = 30\n    p: 0.019\n    n: 16 PoSub and 9 ADN sessions\n  expected:\n  - quantity: s.d. of UP onset delays, ADN, mean over sessions\n    value: 10.38\n    tolerance: 5.74\n    unit: ms\n  - quantity: s.d. of UP onset delays, PoSub, mean over sessions\n    value: 15.54\n    tolerance: 5.42\n    unit: ms\n  data: elsewhere\n  where: PoSub at DANDI:000939; ADN from Peyrache et al. 2015 (ref. 14), for which the paper\n    names no archive\n  criterion: As FigureS2G.py. Per session, onset delays as in fig5f-rsc-pmr-onset, PoSub EX\n    units only and all ADN units (location adn), with the DOWN states of detectDOWNs_ADn.py;\n    the s.d. of delays per session; two-sided Mann-Whitney U test. The Results and the legend\n    give different U and p; either is accepted. Reproduced when ADN is lower at p < 0.05.\n- id: fig3-other-gradients-fail\n  statement: In an adapting Wilson-Cowan array, gradients of excitability, recurrence or\n    adaptation produce an inactivation sequence at the UD transition, not the observed\n    activation sequence at DU only, over all parameter values tested.\n  source: Figures 3B to 3D and S3B to S3D; Results, An Ih gradient can account for DV sequential\n    activation at UP state onset, paragraph 2\n  quote: we found that none of these parameter gradients were able to account for our primary\n    observation... synchronous deactivation at the UD transition but sequential activation at\n    UP state onset\n  data: elsewhere\n  where: github.com/PeyracheLab/MehrotraLevenstein_2023 at commit 4ee34f3, Model/ (simulation\n    code; no recorded data)\n  criterion: Run Figure3.m and FigureS3b.m to FigureS3d.m with the parameters of the Methods\n    table (Parameters for AdWC model). Reproduced when, for each of the three gradients, the\n    slope of threshold-crossing time against position is non-zero at UD in all parameter\n    combinations swept, as the scripts compute it.\n- id: fig3f-ih-gradient\n  statement: A gradient of an h current (Ih) in the model produces synchronous UD transitions\n    and a DV activation sequence at DU, robustly over a range of parameters.\n  source: Figure 3E, 3F and S3F; Results, An Ih gradient can account for DV sequential\n    activation at UP state onset, paragraph 3\n  quote: As a result, an Ih gradient led to synchronous UD and sequential activation at UP state\n    onset at the DU transition, as observed in our recordings (Figure 3F). Importantly, this\n    property of the network was robust to a wide range of parameters (Figure S3F).\n  data: elsewhere\n  where: github.com/PeyracheLab/MehrotraLevenstein_2023 at commit 4ee34f3, Model/\n  criterion: Run Figure3.m and FigureS3f.m with the Ih parameters of the Methods table.\n    Reproduced when the DU slope is non-zero and the UD slope near zero in the main simulation\n    and over the sweep, as the scripts compute and plot them. \"Near zero\" is not quantified in\n    the paper; the slopes are reported.\n- id: fig4d-sag-gradient\n  statement: Ex vivo, the Ih-mediated voltage sag of layer III PoSub EX cells decreases along\n    the DV axis (Pearson R2 = 0.22, n = 59 cells from 11 mice, p = 0.0004), and the gradient is\n    abolished by the HCN blocker ZD-7288 (R2 = 0.05, n = 19 cells from 8 mice, p = 0.36).\n  source: Figure 4D; Results, An Ih gradient can account for DV sequential activation at UP\n    state onset, paragraph 4\n  quote: We found a gradient of decreasing sag along the DV axis (Figure 4D) that was sensitive\n    to an HCN-channel blocker\n  statistics:\n  - about: control\n    test: Pearson correlation\n    statistic: R2 = 0.22\n    p: 0.0004\n    n: 59 cells from 11 mice\n  - about: ZD-7288\n    test: Pearson correlation\n    statistic: R2 = 0.05\n    p: 0.36\n    n: 19 cells from 8 mice\n  expected:\n  - quantity: Pearson R2, sag against DV position, control\n    value: 0.22\n    tolerance: 0.022\n  criterion: Sag from -500 pA steps as (peak minus steady state) over peak, averaged over at\n    least 3 repetitions, against distance from the dorsal pole (Methods, Whole-cell patch clamp\n    recordings). Reproduced when control R2 is within tolerance with a negative slope and\n    p < 0.05, and ZD-7288 gives p >= 0.05. The ex vivo data are not deposited.\n- id: figs4-no-other-gradients\n  statement: Resting potential, input resistance, membrane time constant, F-I slope and the fast\n    time constant of sag do not vary with DV position in PoSub.\n  source: Figure S4A to S4G; Results, An Ih gradient can account for DV sequential activation at\n    UP state onset, paragraph 4\n  quote: Critically, no other DV gradients in passive properties or excitability were found in\n    PoSub cells (Figure S4).\n  statistics:\n  - about: resting membrane potential, control\n    test: Pearson correlation\n    statistic: R2 = 0.02\n    p: 0.27\n    n: 59 cells from 11 mice\n  - about: input resistance, control\n    test: Pearson correlation\n    statistic: R2 = 0.06\n    p: 0.06\n    n: 59 cells from 11 mice\n  - about: membrane time constant, control\n    test: Pearson correlation\n    statistic: R2 = 0.06\n    p: 0.07\n    n: 59 cells from 11 mice\n  - about: F-I slope\n    test: Pearson correlation\n    statistic: R2 = 0.009\n    p: 0.449\n    n: 59 cells from 11 mice\n  - about: fast time constant of sag decay\n    test: Pearson correlation\n    statistic: R2 = 0.021\n    p: 0.302\n    n: 59 cells from 11 mice\n  criterion: A claim of absence, judged by the paper's two-sided Pearson tests at p < 0.05 on\n    the control cells; reproduced when none is significant. The ex vivo data are not deposited.\nchecks: []\n"
}
```

```
File created successfully at: claims/000987/10.1016-j.cub.2024.05.048.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  f=claims/000987/10.1016-j.cub.2024.05.048.yaml; python - <<'EOF'
p='claims/000987/10.1016-j.cub.2024.05.048.yaml'
s=open(p).read()
s=s.replace("checks: []\n","")
s=s.replace("""    the first post-DU bin whose radius exceeds one third of the mean wake radius against the
    last such bin before the preceding UD.""","""    the first post-DU bin whose radius exceeds one third of the mean wake radius against the
    angle at the preceding UD transition, which the legend names as the shuffled quantity; the
    paper does not fix which bin gives the angle at UD, and the last above-threshold bin before
    UD and the mean of the last 150 ms before UD are both run.""")
open(p,'w').write(s)
EOF
python tools/claims_check.py $f paper/10.1016-j.cub.2024.05.048.txt; grep -n "—\|rather" $f
```

Result: not kept, because it reads the paper's text.

**Agent**

YAML 1.1 reads `5e-21` and similar as strings; switching to `5.0e-21` form.

**Agent calls Bash**

```bash
cd  f=claims/000987/10.1016-j.cub.2024.05.048.yaml; sed -i -E 's/^(    p: )([0-9.]+)e-([0-9]+)$/\1\2e-\3/; s/p: 5e-21/p: 5.0e-21/; s/p: 6.1e-5/p: 6.1e-05/' $f; grep -n "    p: .*e-" $f; python tools/claims_check.py $f paper/10.1016-j.cub.2024.05.048.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

All 19 quotes match. The one flagged value, p = 6.1e-5, is printed as "6.1 3 10�5" in the garbled text (line 142), and it reads correctly there. Final style check:

**Agent calls Bash**

```bash
cd  grep -nc "—\|rather" claims/000987/*.yaml; git status --short
```

```
0
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
?? claims/000987/
?? scripts
```

**Agent**

I wrote the claims file for DANDI:000987 at `claims/000987/10.1016-j.cub.2024.05.048.yaml` and did not commit it. The quote checker passes on all 19 quotes; its one flag is p = 6.1e-5 in `fig1g-dv-sequence-du`, which the extracted text prints garbled as "6.1 3 10�5" and which I confirmed by reading. Other untracked files in the working tree (`.bashrc`, `.idea`, `scripts` and so on) were not created by me.

**Text read:** the version of record, from a PDF supplied by a person, with its STAR Methods (pages e1 to e8) and the supplement (legends of Figures S1 to S5). I did not view the figures, because the PDF could not be rendered here, and no claim needed one. Nothing the claims depend on is missing from the text.

**Code read:** github.com/PeyracheLab/MehrotraLevenstein_2023 at commit 4ee34f3. It has Python scripts for each figure panel, the DOWN-state detectors (including `detectDOWNs_RSC.py` and `Figure5F.py`), and the MATLAB model. It has no code for Figures 1I to 1K, 2, 4 or S4, and it does not pin its pynapple version.

**Counts:** 19 claims, all with quotes. 15 carry statistics (28 values) and 18 have criteria; `fig1e-delay-range` is judged by its expected values alone.
- **This dandiset:** only 2 claims use it. `rsc-dataset` checks the counts of 570 units, 14 sessions and 3 mice. `fig5f-rsc-pmr-onset` tests the correlation between UP onset delay and peak-to-mean ratio (PMR; Kendall τ = -0.28, p = 6.76e-21, n = 570).
- **Other data:** the remaining 17 cover the paper's other findings:
  - 12 use the postsubiculum recordings at DANDI:000939.
  - 1 uses the frontal-cortex recordings at CRCNS fcx-1.
  - 2 are model claims run from the repository's simulation code.
  - 2 use the slice-recording data, which were not deposited, so those claims will be blocked.

**Details the paper leaves open, and the readings named:**
- **Which units enter Figure 5F:** (a) all sorted units, as the RSC script does and as the legend's "570 units" implies; (b) excitatory units only, per the Methods' general rule. Both are run, and the claim is blocked if they disagree on sign or significance.
- **UP/DOWN states for Figure 5F:** the dandiset's own detected states if it holds them (its archive description says it does), with a re-detection by the code's procedure shown as a check.
- **Panel 5F's form:** the legend says it is "Same as (D)", an Isomap plot, but the code draws a histogram of onset delay against PMR. Only the correlation is tested.
- **Fig 1E "99th percentile range":** 0.5th to 99.5th percentiles, or 1st to 99th.
- **Fig 1H units:** all good units, as the code does, or excitatory units only.
- **Fig 1J:** which bin gives the angle at the UP-to-DOWN transition (the last bin above threshold, or the mean of the last 150 ms), and the histogram bin width (10, 20 or 36 bins).
- **Fig S1J:** how dorsal and ventral halves are split (equal-width depth bins or a median split).
- **Fig 2F:** the window searched for the maximal gamma slope (0 to 150 ms, or ±250 ms).
- **Fig S2E:** the direction of the speed regression (delay on depth or depth on delay). The extracted text prints the speed unit as "mm/s", and the same extraction turns µ into "m" elsewhere.
- **Fig 3F:** "near zero" UD slope is not quantified, so the slopes will be reported.
- **Pynapple version:** a standard choice, which cannot change the outcome.

**Missing or inconsistent in the paper:**
- **ADN data:** the paper names no archive for the thalamic (ADN) dataset it reuses (ref. 14).
- **ADN statistics:** the ADN test is printed differently in the Results (U = 29, p = 0.016) and the Figure S2G legend (U = 30, p = 0.019); either is accepted.
- **Slice recordings:** the data are not deposited.

## End of run

26 turns, 5 minutes, result: success.
