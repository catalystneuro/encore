# openneuro-ds000228 · author-revise-1 · run 40734370292

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/openneuro-ds000228/verifier-1-report.md; ls entries/openneuro-ds000228-richardson-2018 entries/openneuro-ds000228-richardson-2018/*
```

```
Wed Oct 28 17:20:52 UTC 2026
**A. Outcomes**

The claims file has 42 claims. I judge 40 of them and agree that 2 are blocked.

| Claim | Outcome | Reason |
|---|---|---|
| participants | reproduced | Cell 12: every count matches exactly (122, 33, 64, 20, 17/14/34/23/34). Mean child age is 6.71. |
| supp-table1-behavior-by-age | reproduced | Cell 14: all five means are within 10%, and the FB split 4/4/9, 3/7/4, 23/9/2 matches exactly. |
| beh-tom-age | reproduced | Cell 16: tau-b is .665 (p 5e-26) for ToM score and .198 (p .048) for DCCS. |
| beh-tom-dccs | reproduced | Cell 18: partial tau .186, p .031. |
| beh-fb-groups | reproduced | Cell 20: groups 30/20/15 with 15/13/6 female. Recomputing from FB_Composite gives the same groups. |
| beh-fb-tom | reproduced | Cell 22, reading (a): means .546/.572/.753 and H = 22.95. Tukey p values are 3.8e-5, 7.8e-5 and .85, and the z-scale diffs are 1.24/1.08/.16, as in the paper. |
| beh-fb-age | reproduced | Cell 23: means 4.08/4.75/5.23. Tukey p values are 4.3e-6, .015 and .047, all on the paper's side. |
| beh-fb-dccs | reproduced | Cell 24: means 1.73/2.26/2.33, H = 7.56 (p .023), Pass vs Fail p .012. |
| motion-child-adult | reproduced | Cell 26: means 10.51 and 2.82, Welch t(137.7) = 6.49. |
| motion-not-age-tom | reproduced | Cell 28: p values .86 and .94. |
| motion-not-fb | reproduced | Cell 30: p values .90 and .24. |
| irc-adult | partially_reproduced | Cell 35: both paired tests are p < 1e-18 and within > across. The means (.604, .398, -.051) are outside the ±.02 tolerance under every reading. |
| irc-age-within | not_reproduced | Cell 38: within-ToM rs is .31 to .32 with p ≥ 2.9e-4, which misses the paper's p < .00005 bound. Within-Pain rs is .46 to .47 against .28±.028. |
[... 71 more lines not kept]
```

**Agent calls Bash**

```bash
cat docs/protocol.md | head -c 60000
```

**Agent calls Bash**

```bash
cd entries/openneuro-ds000228-richardson-2018; cat entry.yaml | head -c 30000; wc -c *; cat README.md | head -50
```

```
<persisted-output>
Output too large (35.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/a87ec6ba-bb72-4a07-9f33-8ea95c808298/tool-results/be5cgugc1.txt

Preview (first 2KB):
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
- The **author** tests the claims on the dataset. It reads the paper to
[... 19 more lines not kept]
```

```
schema_version: 1
name: openneuro-ds000228-richardson-2018
type: reproduction
title: Development of the social brain from age three to twelve (Richardson et al. 2018)
description: Tests the findings of Richardson, Lisandrelli, Riobueno-Naylor and Saxe (2018) on
  OpenNeuro ds000228, which holds movie-viewing fMRI of 122 children aged 3 to 12 and 33 adults,
  with the paper's preprocessed images, artifact and CompCor regressors, group ROIs and
  behavioural scores. It covers the behavioural results, motion, inter-region correlations within
  and across the ToM and pain networks, reverse correlation of network timecourses, functional
  maturity, and the face-region analyses.
license: Apache-2.0
notebooks:
- path: reproduce_richardson_2018.ipynb
  title: Reproducing Richardson et al. (2018) from OpenNeuro ds000228
  runtime_minutes: 3
helpers:
- social_brain.py
related:
- id: openneuro:ds000228/1.1.1
  relation: uses_data
[... 41 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/a87ec6ba-bb72-4a07-9f33-8ea95c808298/tool-results/be5cgugc1.txt"
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
cd  wc -l attempts/openneuro-ds000228-richardson-2018-01.yaml; cat attempts/openneuro-ds000228-richardson-2018-01.yaml; ls questions/ | grep ds000228; ls claims/openneuro-ds000228/; ls paper/; ls executed/ 2>/dev/null
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 100,330p attempts/openneuro-ds000228-richardson-2018-01.yaml
```

**Agent calls Bash**

```bash
cd  sed -n 330,420p attempts/openneuro-ds000228-richardson-2018-01.yaml
```

```
output: claim:motion-not-age-tom
  notes: Spearman with age .017, p = .86; Kendall with ToM score -.005, p = .94. Neither is
    significant.
- claim: motion-not-fb
  outcome: reproduced
  notebook: reproduce_richardson_2018.ipynb
  output: claim:motion-not-fb
  notes: FB group (fail coded 1, n = 45), t = .12, p = .90, z-scaled b = .039; DCCS (n = 64), t =
    1.17, p = .24, z-scaled b = .148. Neither is significant.
- claim: irc-adult
  outcome: partially_reproduced
  notebook: reproduce_richardson_2018.ipynb
  output: claim:irc-adult
  measured: [0.604, 0.398, -0.051, 19.1, 21.8]
  notes: Main reading (O1 all voxels of the deposited masks, O2a, O3a). Adult means within-ToM
    .604, within-Pain .398, across -.051; paired t within-ToM against across 19.1 and within-Pain
    against across 21.8, both p < 1e-18. The two t values are in tolerance under three of the
    four O2 and O3 readings; the three means are out of tolerance under all. O1 with only voxels
    with data gives identical values. Variants outside the paper's method (no high-pass, 50 s
    high-pass, no CompCor) give adult means from .556 to .645 within-ToM and -.051 to .059
[... 211 more lines not kept]
```

```
notes: Magnitudes at the 19 Supplementary Table 3 peak TRs. Under O7a (either O6 span), T02 (rs
    = .325), T07 (.352), P04 (.324) and T03 (.274) pass p < .0026; of the paper's five, P01 (rs =
    .193, p = .038), T01 (.270, p = .0036) and P08 (.019, p = .84) do not. Under O7b no event
    passes. 1 to 8 children per event are left out for an artifact at the peak TR.
- claim: rc-t04-tom
  outcome: not_reproduced
  notebook: reproduce_richardson_2018.ipynb
  output: claim:rc-t04-tom
  measured: 1.18
  notes: T04 magnitude on ToM score, age and motion (n = 114), t = 1.18, p = .24 (O7a, z over TRs
    11 to 168); 1.14 and .71 under the other readings. No ToM event reaches p < .007 under any
    reading (smallest p = .061).
- claim: rc-fb-no-difference
  outcome: reproduced
  assumed: true
  notebook: reproduce_richardson_2018.ipynb
  output: claim:rc-fb-no-difference
  notes: Passers against failers, with age and motion, per ToM event. Under O7a no event differs
    (smallest p = .091, T05, with O6a; .072 with O6b); T03 permutation p = .72 (5000 permutations
    of the group labels). Under O7b T05 has p = .0497.
[... 71 more lines not kept]
```

**Agent calls Bash**

```bash
cd  f=claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml; wc -l $f; grep -n "Rule S\|^- id:\|^  - id:\|id: " $f | head -80
```

```
1427 claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml
105:# counts of the same people. Rule S, used by many criteria: a claim is reproduced when every
120:  id: ds000228
124:- id: participants
167:- id: supp-table1-behavior-by-age
193:  criterion: Rule S on the five means; the nine false-belief group counts by age must match exactly
196:- id: beh-tom-age
221:  criterion: Rule S. Kendall tau-b with its normal-approximation p-value (the paper names the test,
223:- id: beh-tom-dccs
238:  criterion: Rule S, partial tau as in O8.
239:- id: beh-fb-groups
260:- id: beh-fb-tom
300:    18 items of the 24 that are not false-belief items; (b) the full ToM score. Rule S under either
303:- id: beh-fb-age
335:  criterion: Rule S, Tukey diffs reported under both scales of O9.
336:- id: beh-fb-dccs
365:  criterion: Rule S on the means, the Kruskal-Wallis test and the Pass against Fail Tukey test. The Inc
368:- id: motion-child-adult
385:  criterion: Artifact timepoints as P2 (and O2 for the composite motion measure). Rule S.
386:- id: motion-not-age-tom
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd  f=claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml; sed -n 1,123p $f
```

```
# Claims for Richardson, Lisandrelli, Riobueno-Naylor & Saxe (2018), "Development of the social
# brain from age three to twelve years", Nature Communications 9, 1027,
# doi:10.1038/s41467-018-03399-2, on OpenNeuro dataset ds000228 ("MRI data of 3-12 year old children
# and adults during viewing of a short animated film"), snapshot 1.1.1
# (doi:10.18112/openneuro.ds000228.v1.1.1).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-28,
# protocol pilot-12 as stated in docs/protocol.md (Reader).
#
# Text read: the version of record (Nature Communications, open access, CC BY 4.0) as supplied
# under paper/ (text extracted from the PDF), with the main text, figure legends, Methods and the
# Supplementary Information (Supplementary Figures 1 to 8, Tables 1 to 4, Note 1). The four
# supplementary tables are images in the supplement PDF and are missing from the text; they were
# read from the PDF (pages 10 to 13), and their numbers are used below. The Peer Review File was
# not supplied and is not needed.
# Code: none linked. Code availability says the analysis code "is available from the
# corresponding author upon request", so no repository was read and no open detail is settled by
# code. The ToM behavioral battery is on OSF (https://osf.io/G5ZPV/, doi:10.17605/OSF.IO/G5ZPV).
#
# Data the paper used (Methods, Participants and fMRI sections; Supplementary Table 1).
# - 122 children aged 3.5 to 12 years (M 6.7, s.d. 2.3; 64 female) and 33 adults aged 18 to 39
[... 103 more lines not kept]
```

**Agent calls Bash**

```bash
cd  f=claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml; sed -n 615,675p $f; sed -n 794,877p $f; sed -n 934,996p $f
```

```
- id: irc-williams
  statement: The age correlations of within-ToM and within-Pain are stronger than those of within-Face
    and within-V1, not stronger than within-Scene and within-M1, and the across ToM-Pain decline is
    stronger than across Face-Scene and across M1-V1.
  source: Supplementary Figure 3 legend
  quote: Positive correlations between within-ToM and within-Pain correlations and age were
    significantly stronger than within-Face and within-V1 correlations, but not significantly stronger
    than within-Scene and within-M1 correlations
  statistics:
  - about: within-Face against within-ToM
    test: Williams' test of differences in age correlations
    statistic: z = 2.69
    p: 0.01
  - about: within-Face against within-Pain
    test: Williams' test
    statistic: z = 2.66
    p: 0.01
  - about: within-Scene against within-ToM
    test: Williams' test
    statistic: z = 1.33
[... 188 more lines not kept]
```

**Agent calls Bash**

```bash
cd  f=claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml; sed -n 1146,1260p $f; sed -n 1379,1427p $f
```

```
- id: rc-fb-no-difference
  statement: Responses at the seven ToM event peaks do not differ between false-belief passers and
    failers.
  source: Results, Reverse correlation analysis, paragraph 3; Figure 3c; Methods, fMRI data analysis,
    paragraph 11
  quote: Response magnitude during ToM events did not differ significantly between children who pass
    and fail explicit falsebelief tasks
  statistics:
  - test: linear regressions of response magnitude on FB-Group, age and motion
    p: 0.08
    p_relation: '>'
    n: Pass 30, Fail 15
  depends_on:
  - rc-events
  - beh-fb-groups
  criterion: A claim of absence, judged on the paper's tests at p < .05, one linear regression per ToM
    event, and for T03 a permutation test of the group effect (Methods, paragraph 11, R lmPerm).
    Reproduced when no event shows a significant FB-group effect; not reproduced when any does.
- id: rc-3yo-events
  statement: Reverse correlation on the 3-year-olds alone finds 4 of the 12 adult pain events and 1 of
[... 144 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/openneuro-ds000228-richardson-2018; python -c "
import json
nb=json.load(open('reproduce_richardson_2018.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    print('=====',i,c['cell_type'],c.get('metadata',{}).get('tags'), len(s))
    print(s[:300])
"
```

```
<persisted-output>
Output too large (34.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/a87ec6ba-bb72-4a07-9f33-8ea95c808298/tool-results/b91pdyklt.txt

Preview (first 2KB):
===== 0 markdown None 2852
# Richardson et al. (2018) on OpenNeuro ds000228, snapshot 1.1.1

Paper: Richardson, Lisandrelli, Riobueno-Naylor & Saxe (2018), "Development of the social brain
from age three to twelve years", Nature Communications 9, 1027,
[doi:10.1038/s41467-018-03399-2](https://doi.org/10.1038/s41467-018-03399-
===== 1 code None 605
import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import matplotlib.pyplot as plt
import social_brain as sb

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 40)
[... 33 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/a87ec6ba-bb72-4a07-9f33-8ea95c808298/tool-results/b91pdyklt.txt"
}
```

```
1	===== 0 markdown None 2852
2	# Richardson et al. (2018) on OpenNeuro ds000228, snapshot 1.1.1
3	
4	Paper: Richardson, Lisandrelli, Riobueno-Naylor & Saxe (2018), "Development of the social brain
5	from age three to twelve years", Nature Communications 9, 1027,
6	[doi:10.1038/s41467-018-03399-2](https://doi.org/10.1038/s41467-018-03399-
7	===== 1 code None 605
8	import numpy as np
9	import pandas as pd
10	from scipy import stats
11	from statsmodels.stats.multicomp import pairwise_tukeyhsd
12	import matplotlib.pyplot as plt
13	import social_brain as sb
14	
15	pd.set_option("display.width", 200)
16	pd.set_option("display.max_columns", 40)
17	print("dataset", sb.DATASET_ID, "snapshot",
18	===== 2 code None 585
19	# The files read whole, with their checksums (OpenNeuro `id`); the per-participant files read are
20	# the swrf BOLD image and the nuisance-regressor file of each participant, listed after extraction.
[... 559 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i "Fig. 2\|Figure 2\|fisher\|high-pass\|CompCor\|nuisance\|M1\b" paper/*.txt | head -50
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 420,440p paper/*.txt; sed -n 1340,1420p paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd entries/openneuro-ds000228-richardson-2018; cat social_brain.py
```

```
"""Loading and measures for OpenNeuro ds000228, snapshot 1.1.1 (Richardson et al. 2018).

Richardson, Lisandrelli, Riobueno-Naylor & Saxe (2018), "Development of the social brain from
age three to twelve years", Nature Communications 9, 1027, doi:10.1038/s41467-018-03399-2.

The snapshot holds, for 155 participants, the raw BOLD and T1 images and the paper's own
preprocessed data under derivatives/preprocessed_data (SPM8, normalized to MNI, 2 mm voxels,
5 mm smoothing; `*_swrf_bold.nii.gz`), with the ART artifact indicators and five CompCor
regressors of each run (`*_ART_and_CompCor_nuisance_regressors.mat`, matrix R, one row per
regressor), and the group ROIs under derivatives/ROIs. Behaviour and demographics are in
participants.tsv. Every file is read from its URL pinned to the snapshot (urls[0] of the
OpenNeuro GraphQL listing) into memory; nothing is written to disk.

Where the parameters come from (claims file: claims/openneuro-ds000228/; the labels P1 to P9
and O1 to O9 are those of its header):

- ROI voxels: the masks deposited in derivatives/ROIs (reading O1a), in MNI mm; their sizes
  equal those of Supplementary Table 2. M1 (right_primotor, left_primotor), V1 (right_CS,
  left_CS), face (rSTS_masked, lSTS, rOFA, lOFA, rFFA, lFFA) and scene (rRSC, lRSC, rTOS, lTOS,
  rPPA, lPPA) are named as in derivatives/README.txt.
[... 410 more lines not kept]
```

**Agent calls Bash**

```bash
cd  f=claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml; sed -n 877,934p $f; grep -n "def handover" -A60 tools/entry.py | grep -n -i "summary\|result\|strip\|heading"
```

```
- id: rc-events
  statement: Reverse correlation on the adult network timecourses finds seven ToM events (68 s, mean
    length 9.7 s) and twelve pain events (86 s, mean length 7.2 s), at the times of Supplementary
    Table 3.
  source: Results, Reverse correlation analysis, paragraph 2; Figure 4a; Supplementary Figure 5;
    Supplementary Table 3
  quote: In adults, the reverse correlation analysis produced seven theory of mind events (68 s total,
    M(s.d.) length 9.7(4.2) s) and twelve pain events (86 s total, M(s.d.) length 7.2(4.7)s)
  expected:
  - quantity: ToM events
    value: 7
    tolerance: 0
  - quantity: pain events
    value: 12
    tolerance: 0
  - quantity: ToM event time
    value: 68
    tolerance: 6.8
    unit: s
  - quantity: pain event time
[... 39 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "def strip_conclusions" -A30 tools/entry.py; cd entries/openneuro-ds000228-richardson-2018; python -c "
import json
nb=json.load(open('reproduce_richardson_2018.ipynb'))
for i in [43,47,65,81,85,88,89,101,118]:
    print('=====',i); print(''.join(nb['cells'][i]['source']))
"
```

```
364:def strip_conclusions(nb):
365-    """The notebook without the author's conclusions, for a verifier's first round."""
366-    kept = []
367-    for cell in nb.cells:
368-        text = cell.source.lstrip()
369-        if cell.cell_type == "markdown" and text.startswith("## Summary"):
370-            break
371-        if cell.cell_type == "markdown" and text.startswith("**Result:"):
372-            continue
373-        kept.append(cell)
374-    nb.cells = kept
375-    return nb
376-
377-
378-def handover(entry_dir: Path, output_dir: Path) -> int:
379-    entry = yaml.safe_load((entry_dir / "entry.yaml").read_text())
380-    target = output_dir / "handover"
381-    target.mkdir(parents=True, exist_ok=True)
382-    for notebook in entry["notebooks"]:
383-        executed = output_dir / notebook["path"]
[... 257 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls; ls executed 2>&1 | head; which python; python -c "import nibabel, h5py, statsmodels; print('ok')"; grep -n "def run\|venv\|uv " tools/entry.py | head -20
```

```
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
scripts
targets
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd  date -u; time python tools/entry.py all entries/openneuro-ds000228-richardson-2018 2>&1 | tail -15; date -u
```

```
Wed Oct 28 17:22:24 UTC 2026
Installed kernelspec registry-openneuro-ds000228-richardson-2018 in executed/openneuro-ds000228-richardson-2018/.venv/share/jupyter/kernels/registry-openneuro-ds000228-richardson-2018
0 error(s)
pass  reproduce_richardson_2018.ipynb  (218 s)

real	4m11.472s
user	5m40.204s
sys	1m58.784s
Wed Oct 28 17:26:36 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/openneuro-ds000228-richardson-2018; PY=executed/openneuro-ds000228-richardson-2018/.venv/bin/python; cat > $TMPDIR/ext.py <<'EOF'
import pickle, sys, os
sys.path.insert(0, '.')
import social_brain as sb
p = sb.participants()
sel = p[(p.Child_Adult == 'adult') | (p.AgeGroup == '3yo')].participant_id.tolist()
D = sb.extract_all(sel, 8)
pickle.dump((p, D), open(os.environ['TMPDIR'] + '/D.pkl', 'wb'))
print(len(D))
EOF
time $PY $TMPDIR/ext.py
```

```
50

real	0m49.258s
user	1m10.504s
sys	0m38.286s
```

**Agent calls Bash**

```bash
cd entries/openneuro-ds000228-richardson-2018; PY=executed/openneuro-ds000228-richardson-2018/.venv/bin/python; cat > $TMPDIR/var.py <<'EOF'
import pickle, sys, os
import numpy as np
sys.path.insert(0, '.')
import social_brain as sb
p, D = pickle.load(open(os.environ['TMPDIR'] + '/D.pkl', 'rb'))
p = p.set_index('participant_id')
TP = sb.TOM_ROIS + sb.PAIN_ROIS
ad = [s for s in D if p.loc[s, 'Child_Adult'] == 'adult']; y3 = [s for s in D if s not in ad]
def m1(s):
    r, l = D[s]['rois']['right_primotor'], D[s]['rois']['left_primotor']
    return (r['all']*r['n_vox'] + l['all']*l['n_vox'])/(r['n_vox']+l['n_vox'])
def run(fn, idx, agg='z'):
    v = []
    for s in idx:
        tc = {r: fn(s, r) for r in TP}
        m = sb.irc_matrix(tc, TP)
        if agg == 'r': m = np.tanh(m)
        v.append([sb.within(m, sb.TOM_ROIS), sb.within(m, sb.PAIN_ROIS), sb.across(m, sb.TOM_ROIS, sb.PAIN_ROIS)])
    return np.round(np.mean(v, 0), 3)
d = lambda s, r, extra=None: sb.clean(D[s]['rois'][r]['all'], D[s]['artifacts'], D[s]['compcor'], extra)
print('base', run(lambda s, r: d(s, r, m1(s)), ad), run(lambda s, r: d(s, r, m1(s)), y3))
print('mean r', run(lambda s, r: d(s, r, m1(s)), ad, 'r'), run(lambda s, r: d(s, r, m1(s)), y3, 'r'))
two = lambda s: np.column_stack([D[s]['rois']['right_primotor']['all'], D[s]['rois']['left_primotor']['all']])
print('M1 two regs', run(lambda s, r: d(s, r, two(s)), ad), run(lambda s, r: d(s, r, two(s)), y3))
gs = lambda s: np.mean([D[s]['rois'][r]['all'] for r in sb.ALL_ROIS], 0)
print('M1+mean of all 29 ROIs', run(lambda s, r: d(s, r, np.column_stack([m1(s), gs(s)])), ad), run(lambda s, r: d(s, r, np.column_stack([m1(s), gs(s)])), y3))
tpm = lambda s: np.mean([D[s]['rois'][r]['all'] for r in TP], 0)
print('M1+mean ToM/Pain', run(lambda s, r: d(s, r, np.column_stack([m1(s), tpm(s)])), ad), run(lambda s, r: d(s, r, np.column_stack([m1(s), tpm(s)])), y3))
# compcor stats
s = ad[0]
print('compcor shape', D[s]['compcor'].shape, 'art', D[s]['artifacts'].shape)
cc = D[s]['compcor']; print('compcor mean/std per row', cc.mean(1).round(3), cc.std(1).round(3))
# correlation of compcor with roi mean
x = D[s]['rois']['RTPJ']['all']; print('r RTPJ with compcor', [round(np.corrcoef(x, c)[0,1],3) for c in cc])
EOF
$PY $TMPDIR/var.py
```

```
base [ 0.604  0.398 -0.051] [0.326 0.179 0.074]
mean r [ 0.519  0.354 -0.049] [0.291 0.159 0.068]
M1 two regs [ 0.599  0.39  -0.037] [0.323 0.177 0.073]
M1+mean of all 29 ROIs [ 0.394  0.306 -0.257] [ 0.11   0.099 -0.083]
M1+mean ToM/Pain [ 0.286  0.258 -0.382] [ 0.029  0.035 -0.168]
compcor shape (5, 168) art (0, 168)
compcor mean/std per row [-0. -0. -0. -0. -0.] [0.997 0.997 0.997 0.997 0.997]
r RTPJ with compcor [np.float64(0.334), np.float64(0.055), np.float64(-0.068), np.float64(0.175), np.float64(0.196)]
```

**Agent calls Bash**

```bash
cd entries/openneuro-ds000228-richardson-2018; PY=executed/openneuro-ds000228-richardson-2018/.venv/bin/python; cat >> $TMPDIR/var.py <<'EOF'
def simul(s, r):
    dd = D[s]; bad = sb.artifact_index(dd['artifacts'])
    y = sb.nearest_neighbour_fill(dd['rois'][r]['all'], bad) if len(bad) else dd['rois'][r]['all'].copy()
    parts = [dd['compcor'].T, m1(s)[:, None], sb.dct_highpass_basis()] + ([dd['artifacts'].T] if len(bad) else [])
    y = sb.residualize(y, np.column_stack(parts)); y[bad] = np.nan; return y
print('simultaneous HP', run(simul, ad), run(simul, y3))
def m1clean(s, r):
    return d(s, r, sb.nearest_neighbour_fill(m1(s), sb.artifact_index(D[s]['artifacts'])) if len(sb.artifact_index(D[s]['artifacts'])) else m1(s))
print('M1 interpolated', run(m1clean, ad), run(m1clean, y3))
EOF
$PY $TMPDIR/var.py 2>&1 | tail -2
```

```
simultaneous HP [ 0.593  0.393 -0.086] [0.317 0.195 0.07 ]
M1 interpolated [ 0.604  0.398 -0.051] [0.326 0.179 0.074]
```

**Agent calls Bash**

```bash
cd  grep -l "^verifications:" attempts/*.yaml | head -3; f=$(grep -l "^verifications:" attempts/*.yaml | head -1); sed -n '/^verifications:/,$p' $f | head -60; grep -n "verifications" -A40 schemas/*attempt* | grep -v "^--$" | head -80
```

```
attempts/000003-senzai-2017-01.yaml
attempts/000004-chandravadia-2020-01.yaml
attempts/000005-yu-2016-01.yaml
verifications:
- date: '2026-10-16'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: Round 1. The first executed notebook with the conclusion cells and the summary removed, the
    helper module and the claims file, with the paper. The verifier queried the archive metadata and tested
    helper functions on synthetic inputs. Its report had no attempt record and gave its own outcome for
    each claim; all 31 agree with the record.
  results:
  - claim: unit-counts
    agrees: true
    outcome: partially_reproduced
    reason: GC 609 is inside 527 to 645, but MC 568 is outside 450 to 550.
    response: No change needed.
  - claim: first-stage-labels
    agrees: true
    outcome: partially_reproduced
[... 84 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/openneuro-ds000228-richardson-2018/social_brain.py",
 "old_string": "    out = {\"shape\": img.shape, \"zooms\": img.header.get_zooms(), \"affine\": img.affine,\n           \"dtype\": str(data.dtype)}",
 "new_string": "    slope, inter = img.header.get_slope_inter()\n    out = {\"shape\": img.shape, \"zooms\": img.header.get_zooms(), \"affine\": img.affine,\n           \"dtype\": str(data.dtype), \"scl_slope\": slope, \"scl_inter\": inter,\n           \"range\": (float(np.nanmin(data)), float(np.nanmax(data)))}"
}
```

```
The file entries/openneuro-ds000228-richardson-2018/social_brain.py has been updated successfully.
```

**Agent calls Bash**

```bash
cd entries/openneuro-ds000228-richardson-2018; python -c "
import json
nb=json.load(open('reproduce_richardson_2018.ipynb'))
for i in [8,42,46,48,59,62,86,90,99,102,106]:
    print('=====',i); print(''.join(nb['cells'][i]['source']))
"
```

```
===== 8
shapes = {tuple(D[s]["shape"]) for s in subs}
zooms = {tuple(float(z) for z in D[s]["zooms"][:3]) for s in subs}
print("preprocessed image shapes:", shapes, "voxel sizes (mm):", zooms, "dtype:", {D[s]["dtype"] for s in subs})
print("affines identical:", all(np.allclose(D[s]["affine"], D[subs[0]]["affine"]) for s in subs))
print("168 volumes in every image (TR 2 s from task-pixar_bold.json):", all(D[s]["shape"][3] == sb.N_TR for s in subs))
print("artifact indicator rows each flag one timepoint:", all((D[s]["artifacts"].sum(axis=1) == 1).all() for s in subs))
print("CompCor rows per participant:", {D[s]["compcor"].shape for s in subs})
print("artifact timepoints per participant: max %d of 168 (%.2f; Methods drop at one third)" % (p.n_art.max(), p.n_art.max() / 168))
print(p.groupby("AgeGroup").n_art.agg(["mean", "std", "min", "max"]).round(2).to_string())
roi_size = pd.Series({r: D[subs[0]]["rois"][r]["n_vox"] for r in sb.ALL_ROIS})
print("ROI sizes (voxels):", roi_size.to_dict())
print("Supplementary Table 2 sizes: RTPJ 376 LTPJ 368 PC 382 DMPFC 217 MMPFC 275 VMPFC 198; RS2 368 LS2 269 RInsula 309 LInsula 240 RMFG 142 LMFG 256 AMCC 249; RFFA 1019 LFFA 531")
cover = pd.DataFrame({s: {r: D[s]["rois"][r]["n_with_data"] for r in sb.ALL_ROIS} for s in subs}).T
print("participants with any ROI voxel without data (zero or non-finite at some timepoint), per ROI:")
print((cover < roi_size).sum().to_string())
print("fewest voxels with data in a face ROI:", int(cover[sb.FACE_ROIS].min().min()),
      "(Supplementary Fig. 4: every participant had at least 100 voxels in every face ROI)")
face_incomplete = (cover[sb.FACE_ROIS] < roi_size[sb.FACE_ROIS]).any(axis=1)
print("participants with incomplete face-ROI coverage:", int(face_incomplete.sum()),
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd executed/openneuro-ds000228-richardson-2018; python -c "
import json
nb=json.load(open('reproduce_richardson_2018.ipynb'))
for i in [3]:
    for o in nb['cells'][i]['outputs']: print(o.get('text','')[:6000])
" | grep -n -i -B3 -A25 "replicat\|event" | head -120
```

```
1:['Derivatives\n', '\n', 'fMRI Prep\n', 'sub-[]_task-pixar_run-001_swrf_bold.nii.gz\n', 'BOLD images collected during movie viewing. FMRI data were analyzed using SPM8 (http://www.fil.ion.ucl.ac.uk/spm) and custom software written in Matlab. Functional images were registered to the first image of the run; that image was registered to each participant’s anatomical image, and each participant’s anatomical image was normalized to the Montreal Neurological Institute (MNI) template. Registration of each individual’s brain to the MNI template was visually inspected, including checking the match of the cortical envelope and internal features like the AC-PC and major sulci. All data were smoothed using a Gaussian filter (5mm kernel).\n', '\n', 'As participants were initially recruited for different studies, there are small differences in voxel size and slice gaps across participants (3.13 mm isotropic with no slice gap (n=5 adults, n=3 7yos, n=20 8-12yo); 3.13 mm isotropic with 10% slice gap (n=28 adults), 3 mm isotropic with 20% slice gap (n=1 3yo, n=3 4yo, n=2 7yo, n=1 9yo); 3 mm isotropic with 10% slice gap (all remaining participants)); all functional data were subsequently upsampled in normalized space to 2mm isotropic voxels. \n', '\n', 'IPS = 168 TRs; 1 TR = 2s\n', 'TR 1-5: Rest (black screen)\n', 'TR 6-10: Pixar and Disney logos\n', 'TR 11-end: Movie\n', '\n', 'sub-[]_normed_anat.nii.gz\n', 'Individual subject anatomical image, normalized to the Montreal Neurological Institute (MNI) template.\n', '\n', 'sub-[]_analysis_mask.nii.gz\n', 'Individual subject skull-stripped whole-brain mask. \n', '\n', 'sub-[]_CompCor_mask.nii.gz\n', 'Individual subject white matter mask, normalized in MNI space, and eroded by two voxels in every direction (in order to avoid partial voluming with grey matter). This white matter mask was used for creation of CompCor regressors.\n', '\n', 'sub-[]_task-pixar_run-001_ART_and_CompCor_nuisance_regressors.mat\n', 'Individual subject artifact t
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd executed/openneuro-ds000228-richardson-2018; python -c "
import json
nb=json.load(open('reproduce_richardson_2018.ipynb'))
print(''.join(nb['cells'][2]['source']))
for o in nb['cells'][2]['outputs']: print(''.join(o.get('text',''))[:12000])
" | grep -n -i -A40 "reverse\|replicat" | head -90
```

```
52:  - Renamed preprocessed data folder to make clear that data were not preprocessed through fmriprep, but rather were preprocessed in SPM8. Clarified timing of reverse correlation events, and provided timings for modeling conditions based on these events, accounting for the hemodynamic lag. Updated paper reference/acknowledgements.
53-
54-1.0.0	2019-04-03
55-
56-	- Initial snapshot
57-
58-
59-Experiment Details
60-Participants watched Disney Pixar’s “Partly Cloudy” while lying in the scanner. There was no task; participants were simply instructed to lie still and watch the movie. The movie began after 10s of rest (black screen; TRs 1-5). The first 10s of the movie are the opening credits (disney castle, pixar logo; TRs 6-10). 
61-
62-IPS = 168 TRs
63-TR = 2s
64-Experiment length: 5.6 minutes
65-
66:Pixar Movie Reverse Correlation Events
67:Events defined by conducting reverse correlation analysis in two separate adult samples, using the average response in ToM brain regions (ToM events) and in the pain matrix (Pain events). Events listed are those that replicated across the two samples.  Onsets and Durations are noted in TRs (1 TR = 2s); scanner trigger = TR 1.
68-
69-Event types: Theory of Mind (ToM), Physical Sensation/Pain (Pain)
70-TRs identified by RC analysis, as reported in Richardson et al. 2018
71-ToM Event Onsets; Durations 
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/openneuro-ds000228-richardson-2018; cat > $TMPDIR/edit.py <<'PYEOF'
import json
P = 'reproduce_richardson_2018.ipynb'
nb = json.load(open(P))
C = nb['cells']
def src(i): return ''.join(C[i]['source'])
def setsrc(i, s): C[i]['source'] = s.splitlines(keepends=True)
def code(s, tags=None):
    c = {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": s.splitlines(keepends=True)}
    if tags: c["metadata"]["tags"] = tags
    return c
def md(s): return {"cell_type": "markdown", "metadata": {}, "source": s.splitlines(keepends=True)}

assert src(118).startswith("## Blocked claims")
blocked, summary = src(118).split("## Summary", 1)
# 118: blocked claims, README check, summary in its own cell (so the handover drops it)
setsrc(118, blocked.rstrip() + "\n")
readme_cell = code('''# replication-sample: the dataset's README lists the events "that replicated across the two
# samples" (onset TR; duration in TRs). Which Supplementary Table 3 events each overlaps. This
# restates the authors' result; it is not the second sample's data.
import re
readme = sb.text("README")
blk = readme.split("TRs identified by RC analysis")[1].split("TIMING OF EVENTS")[0]
tom_txt, pain_txt = blk.split("Pain Event Onsets")
def parse(s):
    return [tuple(int(v) for v in line.split(";")) for line in s.splitlines() if re.fullmatch(r"\\s*\\d+;\\s*\\d+\\s*", line)]
for net, part in [("ToM", tom_txt), ("Pain", pain_txt)]:
    listed = parse(part)
    tab = sb.SUPP_TABLE3[sb.SUPP_TABLE3.network == net]
    hit = {ev: [(o, d) for o, d in listed if set(range(o, o + d)) & set(trs)] for ev, trs in zip(tab.event, tab.trs)}
    print(f"{net}: {len(listed)} replicated events listed in the README:", listed)
    print("   table events overlapped:", [ev for ev, h in hit.items() if h], "; not overlapped:", [ev for ev, h in hit.items() if not h])
''')
C.insert(119, readme_cell)
C.insert(120, md("## Summary" + summary))

# 106 maturity-across, 90 rc-child-adult-timecourse, 59 irc-williams: result text rewritten after the run (placeholders)
# 89: the paper's p bounds per bin
setsrc(89, '''EXP_TP = {"ToM": [.28, .31, .60, .72, .82], "Pain": [.60, .56, .73, .83, .89]}
# The paper's bounds (claims file statistics): ToM every bin p < .0005 (3yo exact p = .00046);
# Pain every bin p < 1e-13, 3yo p < 1e-15. Bonferroni alpha .01 for five bins.
BOUND = {"ToM": [.0005] * 5, "Pain": [1e-15, 1e-13, 1e-13, 1e-13, 1e-13]}
for net, e in EXP_TP.items():
    g = gr[(gr.network == net) & gr.group.isin(sb.AGE_GROUPS)].copy(); g["expected"] = e
    g["in tolerance"] = [tol(a, b, .1 * b) for a, b in zip(g.r, g.expected)]
    g["paper bound"] = BOUND[net]
    g["meets bound"] = g.p < g["paper bound"]
    g["p < .01"] = g.p < .01
    print(g.to_string(index=False, float_format=lambda x: f"{x:.3g}"))
''')

# 85: reading (b) as 159-TR timecourses
s = src(85)
old = '''{"(a) 158 TRs": (158 - nt, 158 - np_), "(b) paper's zeros 125, 116": (125, 116)}'''
assert old in s
s = s.replace(old, '''{"(a) 158 TRs": (158 - nt, 158 - np_), "(b) 159 TRs": (159 - nt, 159 - np_)}''')
s = s.replace("rng = np.random.default_rng(20180301)\n", "rng = np.random.default_rng(20180301)\n# Reading (b): 159-TR timecourses, the length implied by the paper's zeros (125 and 116) and\n# event totals (34 and 43 TRs); with the Supplementary Table 3 events it gives 125 and 116 zeros.\n")
setsrc(85, s)

# 65: ranking under every reading
setsrc(65, '''for r in READINGS:
    M = pd.DataFrame(np.mean([IRC[r][1][s].values for s in y3], axis=0), index=TP, columns=TP)
    print(reading_name(r))
    for net, rois, homol in [("ToM", sb.TOM_ROIS, ("RTPJ", "LTPJ")), ("Pain", sb.PAIN_ROIS, ("RInsula", "LInsula"))]:
        pairs = sorted([(M.loc[a, b], a, b) for i, a in enumerate(rois) for b in rois[i + 1:]], reverse=True)
        rank = [i for i, (v, a, b) in enumerate(pairs) if {a, b} == set(homol)][0] + 1
        print(f"  {net} pairs by 3yo mean z:", ", ".join(f"{a}-{b} {v:.3f}" for v, a, b in pairs[:5]),
              f"| {homol[0]}-{homol[1]} ranks {rank} of {len(pairs)}")
M = pd.DataFrame(np.mean([IRC[MAIN][1][s].values for s in y3], axis=0), index=TP, columns=TP)
fig, ax = plt.subplots(figsize=(5, 4.5))
im = ax.imshow(M.values, vmin=-0.6, vmax=0.6, cmap="RdBu_r"); ax.set_xticks(range(13), TP, rotation=90); ax.set_yticks(range(13), TP)
plt.colorbar(im, label="mean Fisher z, 3yo"); plt.tight_layout(); plt.show()
print("matrix range (off-diagonal):", round(np.nanmin(M.values), 3), "to", round(np.nanmax(M.values), 3), "; colour scale -0.6 to 0.6")
''')

# after 47: matrices and diagnostic variants
diag = code('''# Where the offset from the paper lies. The mean 13 x 13 matrices (main reading) of adults and
# 3-year-olds; Fig. 2 shows these matrices as colours only, with no numbers, so a pair-by-pair
# comparison with the paper is not possible.
for name, idx in [("adults", adults.index), ("3yo", y3_idx)]:
    M = pd.DataFrame(np.mean([IRC[MAIN][1][s].values for s in idx], axis=0), index=TP, columns=TP)
    print(f"mean Fisher z, {name} (n = {len(idx)}), main reading:")
    print(M.round(2).to_string())
    print()
# Diagnostic variants, none of them the paper's stated method: averaging r in place of Fisher z;
# the high-pass basis in the same regression as the nuisance covariates (as in an SPM GLM); left
# and right M1 as two regressors; and, to test whether a shared signal accounts for the offset,
# the mean ToM and Pain signal added as a regressor.
def diag_variant(kind):
    def f(s, r):
        d = D[s]; bad = sb.artifact_index(d["artifacts"])
        y = sb.nearest_neighbour_fill(d["rois"][r]["all"], bad) if len(bad) else d["rois"][r]["all"].copy()
        art = [d["artifacts"].T] if len(bad) else []
        m1 = np.column_stack([d["rois"][k]["all"] for k in sb.M1_ROIS]) if kind == "M1 left and right" else m1_of(s)[:, None]
        extra = [m1]
        if kind == "plus mean ToM and Pain signal":
            extra.append(np.mean([d["rois"][k]["all"] for k in TP], axis=0)[:, None])
        hp = sb.dct_highpass_basis()
        if kind == "high-pass in the nuisance regression":
            y = sb.residualize(y, np.column_stack([d["compcor"].T] + art + extra + [hp]))
        else:
            y = sb.residualize(y, np.column_stack([d["compcor"].T] + art + extra))
            y = y - hp @ np.linalg.lstsq(hp, y, rcond=None)[0]
        y[bad] = np.nan
        return y
    return f
def mean_r(idx):
    v = [[sb.within(np.tanh(IRC[MAIN][1][s]), sb.TOM_ROIS), sb.within(np.tanh(IRC[MAIN][1][s]), sb.PAIN_ROIS),
          sb.across(np.tanh(IRC[MAIN][1][s]), sb.TOM_ROIS, sb.PAIN_ROIS)] for s in idx]
    return np.round(np.mean(v, axis=0), 3)
print(f"{'mean of r, not z':40s} adults (wToM, wPain, across) {mean_r(adults.index)}   3yo {mean_r(y3_idx)}")
for kind in ["high-pass in the nuisance regression", "M1 left and right", "plus mean ToM and Pain signal"]:
    fn = diag_variant(kind)
    print(f"{kind:40s} adults (wToM, wPain, across) {means_with(fn, adults.index)}   3yo {means_with(fn, y3_idx)}")
print("paper: adults .48, .35, -.17; 3yo .21, .23, .05")
''', ["claim:irc-adult"])
C.insert(48, diag)

# 42: rule for readings in absence claims
setsrc(42, src(42).rstrip() + '''

Where the readings of a pipeline detail give different outcomes, the outcome is taken under the
reading the paper best supports, adopted as an assumption (protocol, author step 1.6), and every
reading is shown. This applies to the claims of absence too (irc-tom-behavior-age, irc-fb-across,
maturity-within, rc-fb-no-difference): the claims file names one test for each, but not the
pipeline readings, so the assumed readings decide (O2a and O3a for the inter-region measures, O7a
for event magnitudes), and the outcome is marked as resting on them.
''')

# 8: header and ROI centroid checks appended
setsrc(8, src(8).rstrip() + '''
print("NIfTI scl_slope, scl_inter:", {(str(D[s]["scl_slope"]), str(D[s]["scl_inter"])) for s in subs})
rng_img = pd.DataFrame({s: D[s]["range"] for s in subs}, index=["min", "max"]).T
print("image value range: minimum %.1f to %.1f, maximum %.1f to %.1f over participants; %s %s" % (
    rng_img["min"].min(), rng_img["min"].max(), rng_img["max"].min(), rng_img["max"].max(), subs[0], D[subs[0]]["range"]))
# ROI coordinates: centroid and largest distance from the stated center, to check that the masks
# are in MNI mm (derivatives/README.txt and Supplementary Table 2 centers; M1 and V1 from Methods).
STATED = {"RTPJ": (48, -60, 30), "LTPJ": (-48, -62, 30), "PC": (0, -54, 34), "DMPFC": (-6, 54, 36), "MMPFC": (-4, 58, 16),
          "VMPFC": (-4, 56, -16), "RS2": (60, -28, 38), "LS2": (-62, -32, 34), "RInsula": (42, 6, -6), "LInsula": (-42, -2, -4),
          "RMFG": (50, 42, 12), "LMFG": (-46, 36, 14), "AMCC": (0, 2, 42), "rFFA": (38, -42, -22), "lFFA": (-40, -52, -18),
          "right_primotor": (38, -24, 58), "left_primotor": (-38, -20, 58), "right_CS": (10, -86, 2), "left_CS": (-10, -86, 2)}
cen = []
for r in sb.ALL_ROIS:
    xyz = sb.all_roi_mm()[r]
    row = {"roi": r, "n": xyz.shape[1], "centroid": tuple(np.round(xyz.mean(axis=1), 1))}
    if r in STATED:
        dist = np.linalg.norm(xyz - np.array(STATED[r])[:, None], axis=0)
        row.update({"stated center": STATED[r], "centroid to center mm": round(float(np.linalg.norm(xyz.mean(axis=1) - STATED[r])), 1),
                    "max distance mm": round(float(dist.max()), 1)})
    cen.append(row)
print(pd.DataFrame(cen).to_string(index=False))
''')
json.dump(nb, open(P, 'w'), indent=1, ensure_ascii=False)
open(P, 'a').write('\n')
PYEOF
python $TMPDIR/edit.py && git diff --stat
```

```
.../reproduce_richardson_2018.ipynb                | 137 +++++++++++++++++++--
 .../social_brain.py                                |   4 +-
 2 files changed, 129 insertions(+), 12 deletions(-)
```

**Agent calls Bash**

```bash
cd  git diff entries/ | tail -20; git show HEAD:entries/openneuro-ds000228-richardson-2018/reproduce_richardson_2018.ipynb | tail -c 200 | od -c | tail -3
```

```
+   "source": [
     "## Summary\n",
     "\n",
     "A failure to reproduce here may be a failure of this attempt, not of the paper: see the\n",
diff --git a/entries/openneuro-ds000228-richardson-2018/social_brain.py b/entries/openneuro-ds000228-richardson-2018/social_brain.py
index dc37f3a95..2db97e8f1 100644
--- a/entries/openneuro-ds000228-richardson-2018/social_brain.py
+++ b/entries/openneuro-ds000228-richardson-2018/social_brain.py
@@ -184,8 +184,10 @@ def extract_subject(sub: str) -> dict:
     img = nib.Nifti1Image.from_bytes(raw)
     data = np.asanyarray(img.dataobj)
     inv = np.linalg.inv(img.affine)
+    slope, inter = img.header.get_slope_inter()
     out = {"shape": img.shape, "zooms": img.header.get_zooms(), "affine": img.affine,
-           "dtype": str(data.dtype)}
+           "dtype": str(data.dtype), "scl_slope": slope, "scl_inter": inter,
+           "range": (float(np.nanmin(data)), float(np.nanmax(data)))}
     rois = {}
     for name, mm in all_roi_mm().items():
         vox = np.rint(inv[:3, :3] @ mm + inv[:3, 3:4]).astype(int)
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd  date -u; python tools/entry.py all entries/openneuro-ds000228-richardson-2018 2>&1 | tail -8; date -u
```

```
Wed Oct 28 17:29:50 UTC 2026
/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/site-packages/nbformat/validator.py:434: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbformat 5.1.4). Previous versions of nbformat are fixing this issue transparently, and will stop doing so in the future.
  _validate(nbdict, ref, version, version_minor, relax_add_props)
Installed kernelspec registry-openneuro-ds000228-richardson-2018 in executed/openneuro-ds000228-richardson-2018/.venv/share/jupyter/kernels/registry-openneuro-ds000228-richardson-2018
0 error(s)
pass  reproduce_richardson_2018.ipynb  (216 s)
Wed Oct 28 17:33:58 UTC 2026
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('entries/openneuro-ds000228-richardson-2018/reproduce_richardson_2018.ipynb'))
print([('id' in c) for c in nb['cells']][:5], sum('id' in c for c in nb['cells']), len(nb['cells']))
ex=json.load(open('executed/openneuro-ds000228-richardson-2018/reproduce_richardson_2018.ipynb'))
for i in [8,48,66,86,90,120]:
    print('=====',i, ''.join(ex['cells'][i]['source'])[:80])
    for o in ex['cells'][i].get('outputs',[]):
        t=''.join(o.get('text','')) if 'text' in o else ''.join(o.get('data',{}).get('text/plain',''))
        print(t[-6000:] if i==8 else t)
EOF
```

```
[True, True, True, True, True] 119 122
===== 8 shapes = {tuple(D[s]["shape"]) for s in subs}
zooms = {tuple(float(z) for z in D
preprocessed image shapes: {(79, 95, 68, 168)} voxel sizes (mm): {(2.0, 2.0, 2.0)} dtype: {'int16'}
affines identical: True
168 volumes in every image (TR 2 s from task-pixar_bold.json): True
artifact indicator rows each flag one timepoint: True
CompCor rows per participant: {(5, 168)}
artifact timepoints per participant: max 48 of 168 (0.29; Methods drop at one third)
           mean    std  min  max
AgeGroup                        
3yo        9.82  12.59    0   39
4yo        9.36   8.52    0   26
5yo       13.06  12.62    0   48
7yo        8.91   8.68    0   31
8-12yo     9.85   9.35    0   35
Adult      2.82   4.00    0   15
ROI sizes (voxels): {'RTPJ': 376, 'LTPJ': 368, 'PC': 382, 'DMPFC': 217, 'MMPFC': 275, 'VMPFC': 198, 'RS2': 368, 'LS2': 269, 'RInsula': 309, 'LInsula': 240, 'RMFG': 142, 'LMFG': 256, 'AMCC': 249, 'rSTS_masked': 2503, 'lSTS': 844, 'rOFA': 790, 'lOFA': 211, 'rFFA': 1019, 'lFFA': 531, 'rRSC': 1741, 'lRSC': 1063, 'rTOS': 251, 'lTOS': 133, 'rPPA': 553, 'lPPA': 732, 'right_primotor': 515, 'left_primotor': 515, 'right_CS': 515, 'left_CS': 515}
Supplementary Table 2 sizes: RTPJ 376 LTPJ 368 PC 382 DMPFC 217 MMPFC 275 VMPFC 198; RS2 368 LS2 269 RInsula 309 LInsula 240 RMFG 142 LMFG 256 AMCC 249; RFFA 1019 LFFA 531
participants with any ROI voxel without data (zero or non-finite at some timepoint), per ROI:
[... 171 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
ex=json.load(open('executed/openneuro-ds000228-richardson-2018/reproduce_richardson_2018.ipynb'))
for i,c in enumerate(ex['cells']):
    tags=c.get('metadata',{}).get('tags',[])
    if any(t in tags for t in ['claim:irc-williams','claim:maturity-across']):
        print('=====',i)
        for o in c.get('outputs',[]):
            print(''.join(o.get('text','')))
EOF
```

```
===== 59
               williams                  pair  r age x  r age y    r xy     t      p_t     z      p_z  paper significant  as paper
0   a (partial, motion)         wToM vs wFace    0.367    0.106   0.265  2.51   0.0134  2.47   0.0137               True      True
1   a (partial, motion)        wPain vs wFace    0.525    0.106   0.167  4.08 8.11e-05  3.92 8.97e-05               True      True
2   a (partial, motion)        wToM vs wScene    0.367    0.288   0.222 0.752    0.454  0.75    0.453              False      True
3   a (partial, motion)       wPain vs wScene    0.525    0.288   0.342  2.62  0.00982  2.58  0.00996              False     False
4   a (partial, motion)           wToM vs wM1    0.367    0.227   0.222  1.32    0.191  1.31     0.19              False      True
5   a (partial, motion)          wPain vs wM1    0.525    0.227   0.167  2.92  0.00425  2.86  0.00428              False     False
6   a (partial, motion)           wToM vs wV1    0.367  -0.0686  -0.134  3.36  0.00104  3.27  0.00107               True      True
7   a (partial, motion)          wPain vs wV1    0.525  -0.0686  -0.092  5.03 1.73e-06  4.76 1.97e-06               True      True
8   a (partial, motion)  across vs aFaceScene   -0.247   0.0654   0.277 -2.95  0.00384 -2.87  0.00409               True      True
9   a (partial, motion)       across vs aM1V1   -0.247      0.2   0.158    -4 0.000109 -3.82 0.000132               True      True
10     b (no covariate)         wToM vs wFace    0.366    0.103   0.269  2.53   0.0127  2.48    0.013               True      True
11     b (no covariate)        wPain vs wFace    0.524    0.103   0.154  4.07 8.59e-05   3.9 9.44e-05               True      True
12     b (no covariate)        wToM vs wScene    0.366    0.276   0.227 0.849    0.398 0.847    0.397              False      True
13     b (no covariate)       wPain vs wScene    0.524    0.276   0.311  2.68  0.00847  2.63  0.00859              False     False
14     b (no covariate)   
[... 42 more lines not kept]
```

**Agent**

Now the result texts, cell ids, and summary table.

**Agent calls Bash**

```bash
cd entries/openneuro-ds000228-richardson-2018; cat > $TMPDIR/edit2.py <<'PYEOF'
import json, uuid
P = 'reproduce_richardson_2018.ipynb'
nb = json.load(open(P))
C = nb['cells']
for c in C:
    if 'id' not in c: c['id'] = uuid.uuid4().hex[:8]
def find(prefix, after=None):
    hits = [i for i, c in enumerate(C) if ''.join(c['source']).startswith(prefix) and (after is None or after in ''.join(C[i - 1]['source']))]
    assert len(hits) == 1, (prefix, hits); return hits[0]
def setsrc(i, s): C[i]['source'] = s.splitlines(keepends=True)

i = find("**Result: partially reproduced.** Within-ToM and within-Pain correlations are strongly positive in adults")
s = ''.join(C[i]['source']).rstrip()
setsrc(i, s + " The adult and 3yo mean matrices are printed above; Fig. 2 gives them only as colours, so the offset cannot be traced pair by pair. The masks are in MNI mm (centroids of the 9 mm spheres within 3.7 mm of the stated centers and every voxel within 8.9 mm; M1 and V1 centered exactly, radius 10 mm), and the images are int16 with no scaling (values up to 931 to 4081). Of the diagnostic variants, averaging r in place of z gives adults .519, .354, -.049, the high-pass in the nuisance regression .593, .393, -.086, and left and right M1 as two regressors .599, .390, -.037; only adding the mean ToM and Pain signal as a regressor moves the across-network value past the paper's (.286, .258, -.382). A shared signal that the paper's processing removed and this one does not would give an offset in this direction, but no step of the Methods' pipeline accounts for it.\n")

i = find("**Result: partially reproduced.** The six differences the paper finds significant")
setsrc(i, "**Result: not reproduced.** The six differences the paper finds significant are significant in the same direction under both readings (Face and V1 against ToM and Pain, t = 2.51 to 5.03; across ToM-Pain against Face-Scene and M1-V1, t = -2.95 and -4.0, main reading, reading a). Of the four the paper finds not significant, ToM against Scene (t = .75) and ToM against M1 (t = 1.32) are not, but Pain against Scene (t = 2.62, p = .0098) and Pain against M1 (t = 2.92, p = .0043) are, so the within-Pain age effect is stronger than the Scene and M1 effects, unlike the paper. 8 of 10 comparisons follow the paper under every reading. The criterion requires all ten and states no partial outcome, and two of the paper's tests (p = .19 and .47) come out on the other side of .05, which Rule S counts as failed tests.\n")

i = find("**Result: partially reproduced.** Every age group's mean timecourse correlates with the adult mean")
setsrc(i, "**Result: not reproduced.** Every age group's mean timecourse correlates with the adult mean at p < .01 (the paper's Bonferroni alpha): ToM r = .212, .329, .564, .703, .785 and Pain .531, .516, .701, .797, .862. 8 of 10 values are within 10%; ToM 3yo (.212 against .28) and Pain 3yo (.531 against .60) are below. Three correlations miss the paper's bounds: ToM 3yo p = .0076 against p < .0005 (the paper's exact p is .00046), Pain 3yo p = 7.1e-13 against p < 1e-15, and Pain 4yo p = 4.0e-12 against p < 1e-13. The criterion's partial outcome needs every r significant at the paper's bounds, so it does not apply. Judged only at the Bonferroni alpha of .01, every r is significant and the claim would be partially reproduced.\n")

i = find("**Result: partially reproduced.** With age and motion in the model, a stronger across-network anti-correlation")
setsrc(i, "**Result: not reproduced.** With age and motion in the model, a stronger across-network anti-correlation predicts a more adult-like timecourse in both networks (ToM t = -4.52, p = 1.5e-05; Pain t = -3.55, p = .00055), with the paper's sign, but both t values are out of tolerance (-5.5 and -7.4; -4.37 to -4.85 and -3.55 to -4.10 under the readings). Within-ToM does not predict ToM maturity (t = 1.53, p = .13), as in the paper, but within-Pain does predict Pain maturity (t = 2.40, p = .018; p = .0054 to .018 under every reading), where the paper's effect was not significant (p = .06). The criterion requires the within-network effects to be not significant, so the claim is not reproduced.\n")

i = find("**Result: partially reproduced.** The ToM and pain events found (O5a)")
setsrc(i, "**Result: partially reproduced.** The ToM and pain events found (O5a) do not overlap at all (0 TRs, where the paper has 1), which is less than chance: 2 of 1000 permutations have as little overlap under reading (a), 158 TRs (p = .002, mean permuted overlap 11.9 TRs), and none under (b), 159 TRs (p < .001, mean 11.9). Under O5b and O5c the overlap is also 0, p = .019 to .049. The overlap count differs from the paper's by one timepoint. With the paper's own events from Supplementary Table 3 the overlap is 1 TR (the last of T05 and first of P05), p = .002 (a) and .008 (b).\n")

i = find("## Summary")
s = ''.join(C[i]['source'])
for claim, old, new in [("irc-williams", "partially reproduced", "not reproduced"),
                        ("rc-child-adult-timecourse", "partially reproduced", "not reproduced"),
                        ("maturity-across", "partially reproduced", "not reproduced")]:
    o = f"| {claim} | {old} |"; assert o in s; s = s.replace(o, f"| {claim} | {new} |")
setsrc(i, s)
json.dump(nb, open(P, 'w'), indent=1, ensure_ascii=False)
open(P, 'a').write('\n')
PYEOF
python $TMPDIR/edit2.py && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/openneuro-ds000228-richardson-2018; sed -i 's/(values up to 931 to 4081)/(maximum value 931 to 4081 across participants)/' reproduce_richardson_2018.ipynb; grep -c "931 to 4081 across" reproduce_richardson_2018.ipynb; python -c "
import json
nb=json.load(open('reproduce_richardson_2018.ipynb'))
print(''.join(nb['cells'][0]['source']))"
```

```
1
# Richardson et al. (2018) on OpenNeuro ds000228, snapshot 1.1.1

Paper: Richardson, Lisandrelli, Riobueno-Naylor & Saxe (2018), "Development of the social brain
from age three to twelve years", Nature Communications 9, 1027,
[doi:10.1038/s41467-018-03399-2](https://doi.org/10.1038/s41467-018-03399-2).

Dataset: [OpenNeuro ds000228](https://openneuro.org/datasets/ds000228/versions/1.1.1), snapshot
`1.1.1`, DOI 10.18112/openneuro.ds000228.v1.1.1. The paper cites the dataset on OpenfMRI
without a version; the claims file names snapshot 1.1.1, which is also the latest published
snapshot. Its CHANGES file says 1.1.1 only updated the citation to the paper (2023), so the
pinned snapshot holds the same data as 1.1.0. It is pinned because the claims file gives it and
the protocol pins the latest published version when the paper cites none.

Claims: `claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml`, written from the version of
record and its Supplementary Information (Supplementary Tables 1 to 4 read from the PDF). Its
header labels the shared pipeline P1 to P9 and the open details O1 to O9; this notebook uses the
same labels.

What the snapshot holds (listed below from the archive): for all 155 participants the raw BOLD
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/openneuro-ds000228-richardson-2018; cat > $TMPDIR/edit3.py <<'PYEOF'
import json, uuid
P = 'reproduce_richardson_2018.ipynb'
nb = json.load(open(P)); C = nb['cells']
i = [k for k, c in enumerate(C) if ''.join(c['source']).startswith("# replication-sample: the dataset's README")][0]
C.insert(i + 1, {"cell_type": "markdown", "id": uuid.uuid4().hex[:8], "metadata": {}, "source": [
 "The README's replicated events overlap all seven ToM events and nine of the twelve pain events of\n",
 "Supplementary Table 3, all but P08, P09 and P11, as the replication-sample claim states, and they\n",
 "are consistent with the onset mapping (stimulus seconds / 2 + 8) used for the table. This restates\n",
 "the authors' result and does not test it on the second sample's data, so the claim stays blocked.\n"]})
j = [k for k, c in enumerate(C) if ''.join(c['source']).startswith("## Summary")][0]
s = ''.join(C[j]['source'])
old = "The deposited ROI masks have the sizes of Supplementary Table 2,"
assert old in s
s = s.replace(old, "The deposited ROI masks have the sizes of Supplementary Table 2 and are in MNI mm, centered on the stated coordinates,")
C[j]['source'] = s.splitlines(keepends=True)
json.dump(nb, open(P, 'w'), indent=1, ensure_ascii=False); open(P, 'a').write('\n')
PYEOF
python $TMPDIR/edit3.py; cd  date -u; python tools/entry.py all entries/openneuro-ds000228-richardson-2018 2>&1 | tail -3; date -u
```

```
Wed Oct 28 17:34:57 UTC 2026
Installed kernelspec registry-openneuro-ds000228-richardson-2018 in executed/openneuro-ds000228-richardson-2018/.venv/share/jupyter/kernels/registry-openneuro-ds000228-richardson-2018
0 error(s)
pass  reproduce_richardson_2018.ipynb  (223 s)
Wed Oct 28 17:39:13 UTC 2026
```

**Agent calls Bash**

```bash
cd executed/openneuro-ds000228-richardson-2018; grep -o "found (all, a p<.05)  (b) 159 TRs[^\"]*" reproduce_richardson_2018.ipynb; grep -o "plus mean ToM and Pain signal  [^\"]*" reproduce_richardson_2018.ipynb; grep -o "P08', 'P09', 'P11'\]" reproduce_richardson_2018.ipynb
```

```
found (all, a p<.05)  (b) 159 TRs                     0                  0  0.000             11.945\n
plus mean ToM and Pain signal            adults (wToM, wPain, across) [ 0.286  0.258 -0.382]   3yo [ 0.029  0.035 -0.168]\n
P08', 'P09', 'P11']
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/openneuro-ds000228-richardson-2018-01.yaml",
 "old_string": "    high-pass, no CompCor) give adult means from .556 to .645 within-ToM and -.051 to .059\n    across, none near the paper's.",
 "new_string": "    high-pass, no CompCor) give adult means from .556 to .645 within-ToM and -.051 to .059\n    across, none near the paper's. Further diagnostic variants, adults (within-ToM, within-Pain,\n    across), are mean r in place of z .519, .354, -.049; the high-pass basis in the nuisance\n    regression .593, .393, -.086; left and right M1 as two regressors .599, .390, -.037; and the\n    mean ToM and Pain signal as an added regressor .286, .258, -.382. Only the last, which is not\n    the paper's method, moves the across value past the paper's, so the offset is in the direction\n    of a shared signal removed in the paper's processing and not here, which no step of the\n    Methods accounts for. The ROI masks are in MNI mm (9 mm sphere centroids within 3.7 mm of the\n    stated centers, every voxel within 8.9 mm), and the images are int16 with no scaling. Fig. 2\n    shows the mean matrices only as colours, so the offset cannot be traced pair by pair; the\n    adult and 3yo mean matrices are printed in the notebook."
}
```

```
The file attempts/openneuro-ds000228-richardson-2018-01.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/openneuro-ds000228-richardson-2018-01.yaml",
 "old_string": "- claim: irc-williams\n  outcome: partially_reproduced",
 "new_string": "- claim: irc-williams\n  outcome: not_reproduced"
}
```

```
The file attempts/openneuro-ds000228-richardson-2018-01.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/openneuro-ds000228-richardson-2018-01.yaml",
 "old_string": "    effect is stronger than Scene and M1, unlike the paper. 8 of 10 comparisons follow the paper.\n    The criterion states only the reproduced outcome; the partial outcome is the protocol's\n    \"holds only in part\".",
 "new_string": "    effect is stronger than Scene and M1, unlike the paper. 8 of 10 comparisons follow the paper\n    under every reading. The criterion requires all ten and states no partial outcome, and two of\n    the paper's tests (p = .19 and .47) come out on the other side of .05, which Rule S counts as\n    failed tests, so the claim is not reproduced."
}
```

```
The file attempts/openneuro-ds000228-richardson-2018-01.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/openneuro-ds000228-richardson-2018-01.yaml",
 "old_string": "    fourth, so neither reading holds for ToM. O3b gives the same order.",
 "new_string": "    fourth, so neither reading holds for ToM. RTPJ-LTPJ ranks fourth and RInsula-LInsula first\n    under all eight O1, O2 and O3 readings."
}
```

```
The file attempts/openneuro-ds000228-richardson-2018-01.yaml has been updated successfully.
```

**Agent**

Now rc-overlap, rc-child-adult-timecourse, maturity-across, replication-sample.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/openneuro-ds000228-richardson-2018-01.yaml",
 "old_string": "  notes: The found events (O5a) overlap at no timepoint, against 1 in the paper; permutation p =\n    .002 under both readings of the zero counts (mean permuted overlap 11.9 and 11.1 TRs). Under\n    O5b and O5c the overlap is also 0, p = .019 to .036.",
 "new_string": "  notes: The found events (O5a) overlap at no timepoint, against 1 in the paper; permutation p =\n    .002 under reading (a), 158 TRs, and p < .001 (0 of 1000) under reading (b), 159 TRs (mean\n    permuted overlap 11.9 TRs under both). Under O5b and O5c the overlap is also 0, p = .019 to\n    .049."
}
```

```
The file attempts/openneuro-ds000228-richardson-2018-01.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/openneuro-ds000228-richardson-2018-01.yaml",
 "old_string": "    draw after one zero between events, a reading of Methods paragraph 10, which says only \"a\n    random proportion of zeros between events\".",
 "new_string": "    draw after one zero between events, a reading of Methods paragraph 10, which says only \"a\n    random proportion of zeros between events\".\n  - Reading (b) of the criterion is run as 159-TR timecourses (159 minus each network's event\n    TRs as zeros), the length implied by the paper's zeros (125, 116) and event totals (34, 43\n    TRs); with the Supplementary Table 3 events it gives 125 and 116 zeros."
}
```

```
The file attempts/openneuro-ds000228-richardson-2018-01.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/openneuro-ds000228-richardson-2018-01.yaml",
 "old_string": "- claim: rc-child-adult-timecourse\n  outcome: partially_reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:rc-child-adult-timecourse\n  measured: [0.212, 0.329, 0.564, 0.703, 0.785, 0.531, 0.516, 0.701, 0.797, 0.862]\n  notes: Every r is significant at the paper's Bonferroni alpha of .01 (ToM 3yo p = .0076, all\n    others p < 3e-05); 8 of 10 are within 10%, ToM 3yo (.212 against .28) and Pain 3yo (.531\n    against .60) are below. ToM 3yo has an exact p in the paper (.00046), judged on the side of\n    the corrected alpha.",
 "new_string": "- claim: rc-child-adult-timecourse\n  outcome: not_reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:rc-child-adult-timecourse\n  measured: [0.212, 0.329, 0.564, 0.703, 0.785, 0.531, 0.516, 0.701, 0.797, 0.862]\n  notes: Every r is significant at the paper's Bonferroni alpha of .01 (ToM 3yo p = .0076, all\n    others p < 3e-05); 8 of 10 are within 10%, ToM 3yo (.212 against .28) and Pain 3yo (.531\n    against .60) are below. Three correlations miss the paper's bounds, ToM 3yo p = .0076 against\n    p < .0005 (the paper's exact p is .00046), Pain 3yo p = 7.1e-13 against p < 1e-15 and Pain 4yo\n    p = 4.0e-12 against p < 1e-13. The criterion's partial outcome needs every r significant at\n    the paper's bounds, so the claim is not reproduced. Judged only at the Bonferroni alpha it\n    would be partially reproduced."
}
```

```
The file attempts/openneuro-ds000228-richardson-2018-01.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/openneuro-ds000228-richardson-2018-01.yaml",
 "old_string": "- claim: maturity-across\n  outcome: partially_reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:maturity-across\n  measured: [-4.52, -3.55]\n  notes: Maturity on across, within, age and motion (n = 122). Across effect ToM t = -4.52, p =\n    1.5e-05; Pain t = -3.55, p = .00055; both negative and significant but out of tolerance under\n    every reading. Within-ToM t = 1.53, p = .13, not significant, as in the paper; within-Pain t =\n    2.40, p = .018, significant, where the paper has p = .06. z-scaled b across -.34 and -.28.",
 "new_string": "- claim: maturity-across\n  outcome: not_reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:maturity-across\n  measured: [-4.52, -3.55]\n  notes: Maturity on across, within, age and motion (n = 122). Across effect ToM t = -4.52, p =\n    1.5e-05; Pain t = -3.55, p = .00055; both negative and significant but out of tolerance under\n    every reading. Within-ToM t = 1.53, p = .13, not significant, as in the paper; within-Pain t =\n    2.40, p = .018 (.0054 to .018 under every reading), significant, where the paper has p = .06.\n    The criterion requires the within-network effects to be not significant, so the claim is not\n    reproduced. z-scaled b across -.34 and -.28."
}
```

```
The file attempts/openneuro-ds000228-richardson-2018-01.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/openneuro-ds000228-richardson-2018-01.yaml",
 "old_string": "    does not allow for an `elsewhere` claim.",
 "new_string": "    does not allow for an `elsewhere` claim. The dataset's README lists the events that\n    replicated across the two adult samples; they overlap all seven ToM events and the pain events\n    of Supplementary Table 3 except P08, P09 and P11, as the claim states. This restates the\n    authors' result and is not the second sample's data, so the claim stays blocked."
}
```

```
The file attempts/openneuro-ds000228-richardson-2018-01.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cd  tail -5 attempts/openneuro-ds000228-richardson-2018-01.yaml; grep -n "^[a-z_]*:" attempts/openneuro-ds000228-richardson-2018-01.yaml; sed -n '/"results"/,/^        }/p' schemas/*attempt*.json | grep -o '"[a-z_]*": {' | head -20
```

```
ventral coverage (12 aged 8-12, 2 adults, one each 3, 4 and 7 years); the minimum of 101 voxels
    with data agrees with its "at least 100 voxels". The coverage criterion may differ.
- kind: other
  statement: The independent sample of 20 adults that defined the ToM and pain ROIs and replicated
    the events is not deposited anywhere; the ROIs it produced are in the dataset.
1:schema_version: 2
2:id: openneuro-ds000228-richardson-2018-01
3:dataset:
8:paper: doi:10.1038/s41467-018-03399-2
9:date: 2026-10-28
10:entry: openneuro-ds000228-richardson-2018
11:provenance:
22:outcomes:
466:findings:
"properties": {
"date": {
"kind": {
"by": {
"results": {
"items": {
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat >> attempts/openneuro-ds000228-richardson-2018-01.yaml <<'EOF'
verifications:
- date: '2026-10-28'
  kind: agent
  by: Independent agent run by CatalystNeuro (verifier-1, same harness, separate context, did not
    write the notebook)
  reviewed: Round 1. The executed notebook with the conclusion cells removed, the helper module and
    the claims file, with the paper. The summary cell was not removed by the handover, as it shared
    a cell with the blocked claims, and the verifier read it after forming most of its outcomes. It
    queried the archive's file list for the blocked claims and tested the helper functions on
    synthetic inputs. Of 42 claims it agreed with 39 outcomes and disagreed on irc-williams,
    rc-child-adult-timecourse and maturity-across.
  results:
  - claim: participants
    agrees: true
    outcome: reproduced
    reason: Every count matches exactly (122, 33, 64, 20, 17/14/34/23/34). Mean child age is 6.71.
    response: No change needed.
  - claim: supp-table1-behavior-by-age
    agrees: true
    outcome: reproduced
    reason: All five means are within 10%, and the FB split 4/4/9, 3/7/4, 23/9/2 matches exactly.
    response: No change needed.
  - claim: beh-tom-age
    agrees: true
    outcome: reproduced
    reason: tau-b is .665 (p 5e-26) for ToM score and .198 (p .048) for DCCS.
    response: No change needed.
  - claim: beh-tom-dccs
    agrees: true
    outcome: reproduced
    reason: Partial tau .186, p .031.
    response: No change needed.
  - claim: beh-fb-groups
    agrees: true
    outcome: reproduced
    reason: Groups 30/20/15 with 15/13/6 female. Recomputing from FB_Composite gives the same groups.
    response: No change needed.
  - claim: beh-fb-tom
    agrees: true
    outcome: reproduced
    reason: Reading (a), means .546/.572/.753 and H = 22.95. Tukey p values are 3.8e-5, 7.8e-5 and
      .85, and the z-scale diffs are 1.24/1.08/.16, as in the paper.
    response: No change needed.
  - claim: beh-fb-age
    agrees: true
    outcome: reproduced
    reason: Means 4.08/4.75/5.23. Tukey p values are 4.3e-6, .015 and .047, all on the paper's side.
    response: No change needed.
  - claim: beh-fb-dccs
    agrees: true
    outcome: reproduced
    reason: Means 1.73/2.26/2.33, H = 7.56 (p .023), Pass vs Fail p .012.
    response: No change needed.
  - claim: motion-child-adult
    agrees: true
    outcome: reproduced
    reason: Means 10.51 and 2.82, Welch t(137.7) = 6.49.
    response: No change needed. The verifier could not check per-participant artifact counts
      against the ART thresholds; recomputing ART from the raw images is outside this attempt, and
      only the deposited indicators are used, as stated.
  - claim: motion-not-age-tom
    agrees: true
    outcome: reproduced
    reason: p values .86 and .94.
    response: No change needed.
  - claim: motion-not-fb
    agrees: true
    outcome: reproduced
    reason: p values .90 and .24.
    response: No change needed.
  - claim: irc-adult
    agrees: true
    outcome: partially_reproduced
    reason: Both paired tests are p < 1e-18 and within > across. The means (.604, .398, -.051) are
      outside the ±.02 tolerance under every reading. The IRC values have a systematic offset from
      the paper that is never explained, and no output localizes it.
    response: Added the adult and 3yo mean 13 x 13 matrices (Fig. 2 has no numbers to set beside
      them), the NIfTI scaling and value range (int16, no scaling), each ROI's centroid and largest
      distance from its stated center (the masks are in MNI mm), and diagnostic variants (mean r,
      high-pass in the nuisance regression, left and right M1 regressors, a shared-signal
      regressor). None of the stated pipeline's choices closes the gap; only a shared-signal
      regressor outside the paper's method moves the across value past the paper's. The offset
      stays unexplained, as the notes say. Outcome kept.
  - claim: irc-age-within
    agrees: true
    outcome: not_reproduced
    reason: Within-ToM rs is .31 to .32 with p ≥ 2.9e-4, which misses the paper's p < .00005 bound.
      Within-Pain rs is .46 to .47 against .28±.028.
    response: No change needed.
  - claim: irc-age-across
    agrees: true
    outcome: not_reproduced
    reason: rs is -.26 to -.27 (tolerance -.315 to -.385) and p .003 to .004 against the paper's p
      < .0001. The direction holds.
    response: No change needed.
  - claim: irc-adult-vs-child
    agrees: true
    outcome: partially_reproduced
    reason: All three group effects are significant with the paper's signs. The t values (-6.5,
      -6.7, 4.5) are outside tolerance, and the motion effect on within-ToM is n.s. where the paper
      has t = -4.3.
    response: No change needed.
  - claim: irc-control-networks
    agrees: true
    outcome: partially_reproduced
    reason: Within-ToM (.367) and across (-.247) are in tolerance. Within-Pain (.525), Scene and M1
      are out of tolerance. The across M1-V1 absence fails (p .017 to .034).
    response: No change needed. The verifier asked for ROI centroids to settle whether the face,
      scene, M1 and V1 masks are in mm; they are now printed, and M1 and V1 are centered exactly on
      the stated coordinates with radius 10 mm.
  - claim: irc-williams
    agrees: false
    outcome: not_reproduced
    reason: Under both Williams readings, within-Pain vs Scene (p .010) and within-Pain vs M1 (p
      .004) come out significant where the paper has n.s. That is 8/10 comparisons as in the paper,
      and the criterion has no partial clause.
    response: Changed to not_reproduced. The criterion states only the reproduced outcome, and two
      of the paper's listed tests come out on the other side of .05, which Rule S counts as failed
      tests.
  - claim: irc-3yo-distinct
    agrees: true
    outcome: not_reproduced
    reason: All four values are out of tolerance (within-ToM .326, within-Pain .179, t 8.4 and 4.5).
      The Pain test p is 3e-4 against the paper's p < .00001. Within > across holds.
    response: No change needed.
  - claim: irc-3yo-not-anticorrelated
    agrees: true
    outcome: partially_reproduced
    reason: The mean is .074, not negative but outside .05±.02. It is significantly above 0 (p
      .002).
    response: No change needed.
  - claim: irc-3yo-homologous
    agrees: true
    outcome: not_reproduced
    reason: RTPJ-LTPJ ranks 4th among ToM pairs. The Pain half holds (the three homologous pairs are
      the top three). The ranking is shown for only 2 of the 8 readings.
    response: The ranking is now printed for all eight readings; RTPJ-LTPJ ranks fourth and
      RInsula-LInsula first under each. Outcome kept.
  - claim: irc-3yo-nonbilateral
    agrees: true
    outcome: partially_reproduced
    reason: Under reading (b) both tests hold (p 1e-6 and .008) but the values are out of
      tolerance. Under reading (a) the Pain test fails (p .2).
    response: No change needed.
  - claim: irc-tom-behavior
    agrees: true
    outcome: partially_reproduced
    reason: Within-ToM tau .246 is in tolerance. Across tau -.125 is out of tolerance, with p .03 to
      .05 (on the same side of .05 as the paper).
    response: No change needed.
  - claim: irc-tom-behavior-age
    agrees: true
    outcome: not_reproduced
    reason: Under O3a the ToM-score effect on within-ToM is significant (p .044 and .048). Under O3b
      it is not (p .069 and .088). The absence claim flips between readings and a verdict needs a
      stated rule; the verifier used the main reading (O2a, O3a).
    response: The notebook now states the rule. Where readings of a pipeline detail disagree, an
      absence claim is judged under the reading the paper best supports, adopted as an assumption
      (protocol, author step 1.6), with every reading shown; here O2a and O3a. Outcome kept,
      marked as assumed.
  - claim: irc-fb-within
    agrees: true
    outcome: not_reproduced
    reason: t .60 to .71, p ≥ .48.
    response: No change needed.
  - claim: irc-fb-within-dccs
    agrees: true
    outcome: not_reproduced
    reason: p .59 to .69, outside the .05 to .10 band.
    response: No change needed.
  - claim: irc-fb-across
    agrees: true
    outcome: not_reproduced
    reason: A significant group effect under 3 of 4 readings (p .034 to .047). Only O2a+O3b gives p
      .051. The absence claim flips between readings; the verifier used the main reading.
    response: The rule for absence claims under several readings is now stated in the notebook, as
      for irc-tom-behavior-age. Outcome kept, marked as assumed.
  - claim: rc-events
    agrees: true
    outcome: partially_reproduced
    reason: No reading gives 7 ToM and 12 pain events within the time tolerance. At p < .05 all 7
      ToM events and 10 of 12 pain events are found (68 s ToM is out at 80 s).
    response: No change needed.
  - claim: rc-overlap
    agrees: true
    outcome: partially_reproduced
    reason: 0 overlapping TRs against the paper's 1 (tolerance 0), with permutation p .002 to .004.
      In reading (b) the paper's zero counts are combined with this attempt's event lengths, so the
      two permuted series differ in length and are truncated, which is not the claims file's 159-TR
      reading.
    response: Reading (b) now uses 159-TR timecourses (159 minus each network's event TRs as
      zeros). Under it the found events give p < .001 (0 of 1000), and the table events, which have
      125 and 116 zeros, p = .008 as before. Outcome kept.
  - claim: rc-child-adult-timecourse
    agrees: false
    outcome: not_reproduced
    reason: ToM 3yo r .212 (p .0076) and Pain 3yo .531 are out of tolerance. The 3yo ToM p misses
      the paper's "all p < .0005" bound, and Pain 3yo/4yo miss its "p < 1e-13" bound. All are
      significant at the Bonferroni α .01, so a laxer reading of the criterion would give partial.
      The notebook checks every bin only against p < .0005.
    response: Changed to not_reproduced. The notebook now checks each bin against the paper's bound
      (ToM p < .0005, Pain p < 1e-13, Pain 3yo p < 1e-15); three bins miss it, so the criterion's
      partial outcome, which needs every r significant at the paper's bounds, does not apply.
  - claim: supp-table4-other-networks
    agrees: true
    outcome: not_reproduced
    reason: 17 of 25 values are in tolerance, below the 20 required for partial.
    response: No change needed.
  - claim: rc-age-events
    agrees: true
    outcome: not_reproduced
    reason: The passing events are T02, T03, T07 and P04. Only 2 of the paper's 5 pass; P08 has rs
      .02.
    response: No change needed.
  - claim: rc-t04-tom
    agrees: true
    outcome: not_reproduced
    reason: T04 t 0.7 to 1.2, p ≥ .24 under every reading.
    response: No change needed.
  - claim: rc-fb-no-difference
    agrees: true
    outcome: reproduced
    reason: Under O7a no event is significant (min p .072, T03 permutation p .66 to .72). It is
      fragile; under O7b, T05 gives p = .0497.
    response: The rule for absence claims under several readings is now stated in the notebook;
      the outcome rests on O7a, marked as assumed. Outcome kept.
  - claim: rc-3yo-events
    agrees: true
    outcome: partially_reproduced
    reason: Under the reading (all, p<.05) the cross-overlaps hold (6 s of pain events in T04, 4 s of
      ToM events in P01), but the counts and times differ. The O6 tie-break toward all 168 TRs is
      the author's choice, defensible from Methods paragraph 9; under O6a the P01 overlap is 0 and
      the claim would be not reproduced.
    response: No change. The dependence on O6 is recorded as an assumption, with the O6a result, in
      the notes and deviations.
  - claim: maturity-across
    agrees: false
    outcome: not_reproduced
    reason: The across-network effects hold (t -4.5 and -3.6, out of tolerance). The within-Pain
      effect is significant under every reading (p .005 to .018), which fails the criterion's
      condition.
    response: Changed to not_reproduced. The criterion requires the within-network effects to be
      not significant, and within-Pain is significant under every reading.
  - claim: maturity-within
    agrees: true
    outcome: reproduced
    reason: Maturity effects are n.s. under the main reading (p .41 and .075). Under O2b+O3b the
      Pain effect has p .040.
    response: The rule for absence claims under several readings is now stated in the notebook.
      Outcome kept, marked as assumed.
  - claim: maturity-tom-behavior
    agrees: true
    outcome: reproduced
    reason: Partial rs .498 (p 6e-9). In the regression the ToM-score effect has p .97 and age has p
      1.8e-5.
    response: No change needed.
  - claim: maturity-fb
    agrees: true
    outcome: reproduced
    reason: p .13.
    response: No change needed.
  - claim: face-rc
    agrees: true
    outcome: not_reproduced
    reason: 3yo r .589 is outside .72±.072, and no reading gives 7 adult events or 4 3yo events / 18
      s. The age absence holds.
    response: No change needed.
  - claim: face-overlap
    agrees: true
    outcome: reproduced
    reason: Every reading has p ≥ .052 for ToM and ≥ .94 for pain.
    response: No change needed.
  - claim: replication-sample
    agrees: true
    outcome: blocked
    reason: The archive has no data for the 20 independent adults (API file list, only sub-pixar*,
      ROIs, mriqc). The deposited README lists the 7 ToM and 9 pain events that replicated, which
      map onto all Supplementary Table 3 events except P08, P09 and P11; this restates the
      authors' result, not data, and the notebook could have reported the check.
    response: Added the check to the notebook (the README events overlap all table events except
      P08, P09 and P11) and to the notes. Kept blocked with blocked_by other, since the checker does
      not allow data_missing on an `elsewhere` claim, as the notes say.
  - claim: hand-coded-events
    agrees: true
    outcome: blocked
    reason: The Jacoby et al. 2016 coding is not in the snapshot. It exists in an unpinned Saxe-lab
      script (movloc.zip); as the notebook's reason is that it is unpinned, "other" fits better than
      "data_missing". The claim becomes partly testable if an unpinned outside input is accepted.
    response: No change needed; the record already gives blocked_by other for this reason. The
      protocol allows only pinned outside inputs, so the script is not used.
EOF
python tools/entry.py check entries/openneuro-ds000228-richardson-2018 2>&1 | tail -20
```

```
0 error(s)
```

**Agent calls Bash**

```bash
cd  ls tools; grep -rn "attempts/" tools/*.py | grep -i "valid\|schema\|check" | head
```

```
__pycache__
agent_run.py
archive_transcripts.sh
archives
blind.sh
build_dryad_targets.py
build_figshare_targets.py
build_openneuro_targets.py
build_site.py
build_targets.py
claims_check.py
conversion_issue.py
datasets.py
entry.py
flagged.py
get_papers.sh
notify.py
papers_manifest.py
progress.py
readme_row.py
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "attempt" tools/entry.py | head -30; ls tests | head
```

```
12:`check` validates entry.yaml, and the claims and attempt files that mention
77:    """The identifier of the dataset a claims file or attempt record is about, in its archive."""
189:    # Claims and attempts that go with this entry.
203:    mine = [p for p in sorted((ROOT / "attempts").glob("*.yaml"))
205:    for path in sorted((ROOT / "attempts").glob("*.yaml")):
206:        attempt = load(report, path)
207:        if not isinstance(attempt, dict) or attempt.get("entry") != entry["name"]:
209:        validate(report, path, "attempt")
211:        pinned = versions.get(dataset_id(attempt))
212:        version = (attempt.get("dataset") or {}).get("version")
213:        # The entry streams the version of its latest attempt; earlier attempts keep the version they used.
216:        # A repeat attempt's reconciliation points into the earlier record's findings and its own by number.
217:        rec = attempt.get("reconciliation")
219:            earlier = load(Report(), ROOT / "attempts" / f"{rec.get('earlier')}.yaml")
221:                report.error(where, f"reconciliation: no attempt record {rec.get('earlier')!r}")
223:                n_then, n_now = len(earlier.get("findings") or []), len(attempt.get("findings") or [])
235:        # A deprecated attempt no longer stands: its claims are being read again, and the claims file it was
237:        if attempt.get("deprecated"):
239:        known = claims_by_target.get((dataset_id(attempt), attempt.get("paper")))
240:        if labels_used.get((dataset_id(attempt), attempt.get("paper"))):
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import yaml,collections
a=yaml.safe_load(open('attempts/openneuro-ds000228-richardson-2018-01.yaml'))
g=collections.defaultdict(collections.Counter)
for o in a['outcomes']:
    c=o['claim']; k=c.split('-')[0]
    g[k][o['outcome']]+=1
for k,v in g.items(): print(k, dict(v))
"
```

```
participants {'reproduced': 1}
supp {'reproduced': 1, 'not_reproduced': 1}
beh {'reproduced': 6}
motion {'reproduced': 3}
irc {'partially_reproduced': 6, 'not_reproduced': 9}
rc {'partially_reproduced': 3, 'not_reproduced': 3, 'reproduced': 1}
maturity {'not_reproduced': 1, 'reproduced': 3}
face {'not_reproduced': 1, 'reproduced': 1}
replication {'blocked': 1}
hand {'blocked': 1}
```

**Agent calls Bash**

```bash
cd entries/openneuro-ds000228-richardson-2018; python - <<'EOF'
p='README.md'; s=open(p).read()
for a,b in [("| Inter-region correlations (15 claims) | 7 partially reproduced, 8 not reproduced |","| Inter-region correlations (15 claims) | 6 partially reproduced, 9 not reproduced |"),
            ("| Reverse correlation (8 claims) | 1 reproduced, 4 partially reproduced, 3 not reproduced |","| Reverse correlation (8 claims) | 1 reproduced, 3 partially reproduced, 4 not reproduced |"),
            ("| Functional maturity (4 claims) | 3 reproduced, 1 partially reproduced |","| Functional maturity (4 claims) | 3 reproduced, 1 not reproduced |")]:
    assert a in s; s=s.replace(a,b)
open(p,'w').write(s)
EOF
cd  python tools/entry.py check entries/openneuro-ds000228-richardson-2018 | tail -2; grep -n "—\|rather" attempts/openneuro-ds000228-richardson-2018-01.yaml entries/openneuro-ds000228-richardson-2018/README.md | head; python -c "
import json
nb=json.load(open('entries/openneuro-ds000228-richardson-2018/reproduce_richardson_2018.ipynb'))
import re
for c in nb['cells']:
    s=''.join(c['source'])
    if '—' in s or re.search(r'\brather\b', s): print('BAD', s[:80])
print(all(not c.get('outputs') for c in nb['cells'] if c['cell_type']=='code'))
"; git status --short
```

```
0 error(s)
True
 M attempts/openneuro-ds000228-richardson-2018-01.yaml
 M entries/openneuro-ds000228-richardson-2018/README.md
 M entries/openneuro-ds000228-richardson-2018/reproduce_richardson_2018.ipynb
 M entries/openneuro-ds000228-richardson-2018/social_brain.py
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
?? scripts
```

**Agent calls Bash**

```bash
cd  python tools/entry.py handover entries/openneuro-ds000228-richardson-2018 2>&1 | tail -2; grep -c "## Summary\|| irc-williams |" executed/openneuro-ds000228-richardson-2018/handover/reproduce_richardson_2018.ipynb; date -u
```

```
wrote executed/openneuro-ds000228-richardson-2018/handover
0
Wed Oct 28 17:42:06 UTC 2026
```

**Agent**

I've changed three outcomes to agree with the verifier and added the outputs it asked for. The entry was re-run with `python tools/entry.py all` (0 errors, notebook passes in 223 s), and `entry.py check` passes on the updated record. Nothing is committed.

**Outcome changes** (the verifier was right in each case):
- **irc-williams**: partially reproduced → not reproduced. The criterion has no partial outcome. Two tests the paper reports as not significant come out significant here: within-Pain against Scene (p = .0098) and within-Pain against M1 (p = .0043).
- **rc-child-adult-timecourse**: partially reproduced → not reproduced. Three correlations miss the paper's p bounds: ToM 3yo (.0076 against < .0005), Pain 3yo (7.1e-13 against < 1e-15) and Pain 4yo (4.0e-12 against < 1e-13). The notebook now checks each age group against its own bound. Judged only at the Bonferroni alpha of .01 it would be partially reproduced, and the notes say so.
- **maturity-across**: partially reproduced → not reproduced. Within-Pain significantly predicts Pain maturity under every reading (p = .0054 to .018), and the criterion requires it not to.

Totals now: inter-region correlations 6 partially reproduced and 9 not; reverse correlation 1 reproduced, 3 partially and 4 not; functional maturity 3 reproduced and 1 not. The README and the notebook's summary table show these counts.

**Added or corrected:**
- **Offset in the inter-region correlations (problem 1).** It is still unexplained. The new outputs show:
  - The ROI masks are in MNI mm, centred on the stated coordinates.
  - The images are int16 with no scaling.
  - Of the diagnostic variants (adult means printed in the notebook), none within the paper's described method closes the gap.
  - Only adding a shared ToM and Pain signal as a regressor, which is not the paper's method, pushes the across-network value past the paper's (to -.382). So the offset points to a shared signal the paper's processing removed and this one does not.
  - The adult and 3-year-old mean 13×13 matrices are printed; Fig. 2 shows them only as colours, so a pair-by-pair comparison isn't possible.
- **Absence claims that flip between readings (problem 3).** The notebook now states the rule: such a claim is judged under the reading the paper best supports, marked as assumed, with every reading shown. This is the same main reading the verifier used, so those four outcomes stay as they were.
- **rc-overlap reading (b)** now uses 159-TR timecourses as the claims file says. The found events give p < .001 (0 of 1000 permutations), and the outcome is unchanged.
- **irc-3yo-homologous**: the ranking is printed for all eight readings. RTPJ-LTPJ ranks fourth under each.
- **Summary cell**: it is now its own cell, so the handover removes it. I checked that it does.
- **replication-sample**: added the README check. Its replicated events cover every table event except P08, P09 and P11. The claim stays blocked.
- The `verifications` round is recorded for all 42 claims (39 agreed, 3 disagreed), with the verifier's reasons and my responses.

**Not done:**
- I added no reader questions, because the report names no place where the claims file misreads the paper.
- rc-3yo-events stays partially reproduced, resting on the assumption that z-normalization spans all 168 TRs. The verifier agreed with that outcome but noted it would be not reproduced under the other reading; the notes record this.
- Per-participant ART artifact counts were not recomputed from the raw images; only the deposited indicators are used.
- hand-coded-events already had `blocked_by: other`, as the verifier suggested.

## End of run

54 turns, 21 minutes, result: success.
