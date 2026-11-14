# zhang-2021 · recorder · run 43622862530

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; echo; python tools/readme_row.py zhang-2021; echo; ls transcripts/zhang-2021/; cat attempts/zhang-2021-01.yaml; cat claims/zhang-2021.yaml
```

```
<persisted-output>
Output too large (71KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/08ba0065-1e76-4ae7-a1ef-47208a2ae0b3/tool-results/ba5ne93vz.txt

Preview (first 2KB):
docs/pilot-notes/amjad-2025-01.md
docs/pilot-notes/andrews-2024-01.md
docs/pilot-notes/armstrong-2026-01.md
docs/pilot-notes/asari-2009-01.md
docs/pilot-notes/ashworth-2025-01.md

| [CRCNS:vim-4](https://crcns.org/data-sets/vc/vim-4) | [Zhang et al. 2021](https://doi.org/10.3389/fnins.2020.565976) | 7 (+1) | 1 | 1 (+1) | 0 | [`zhang-2021`](entries/zhang-2021) |

answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
author-revise-1.md
author-revise-2-report.md
[... 49 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for f in amjad-2025-01 andrews-2024-01 armstrong-2026-01 asari-2009-01 ashworth-2025-01; do echo "=== $f"; cat docs/pilot-notes/$f.md; done; echo; head -5 docs/pilot-notes/knierim-2000-02.md
```

```
<persisted-output>
Output too large (37.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/08ba0065-1e76-4ae7-a1ef-47208a2ae0b3/tool-results/bwo0xyfca.txt

Preview (first 2KB):
=== amjad-2025-01
# 002013, Amjad et al. 2025

Seven claims reproduced, one partially and five blocked on the dandiset,
plus one claim linking the dandiset to the paper's Zenodo deposit,
reproduced (trial lists agree for 99.8 to 100% of trials); both rounds
agreed with every outcome. The paper describes microinvasive probes for
recording dopamine and electrical activity in monkeys; the beta burst,
reward and unit isolation claims reproduce, the dopamine reward effect
weakly (p = 0.023, and not in the stored trial-aligned `da`).

The dandiset was converted by CatalystNeuro (catalystneuro/schwerdt-lab-to-nwb,
the same conversion as 002014), and many findings are the same: each event
is stored about five times, once per overlapping trial window; trial
conditions are not in the trials table; the FSCV table columns carry no
units and the raw FSCV current is labelled amperes with values in the
[... 18 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/zhang-2021-01.yaml"
}
```

```
1	schema_version: 3
2	id: zhang-2021-01
3	datasets:
4	- archive: crcns
5	  id: vim-4
6	  version: unversioned
7	  doi: 10.6080/K0668BDF
8	  relation: primary
9	paper: doi:10.3389/fnins.2020.565976
10	date: 2026-11-14
11	entry: zhang-2021
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-15
20	  runner:
[... 542 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/zhang-2021.yaml"
}
```

```
1	# Claims for Zhang, Gao, Cukur & Gallant (2021), Frontiers in Neuroscience 14:565976,
2	# "Voxel-Based State Space Modeling Recovers Task-Related Cognitive States in Naturalistic fMRI
3	# Experiments", doi:10.3389/fnins.2020.565976, on CRCNS data set vim-4 (doi:10.6080/K0668BDF).
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
5	# protocol as stated in docs/protocol.md (Reader), version pilot-14.
6	#
7	# Text read: the version of record (PMC8145286, open access), as JATS XML flattened to text under
8	# paper/: main text, Materials and Methods, figure legends, Table 1, and the supplement
9	# (Data_Sheet_1.DOCX, legends of Supplementary Figures 1 to 5). No PDF was supplied. The
10	# per-subject CSI values of the attention task are printed only inside the images of
11	# Supplementary Figures 1 and 2; they were read from the images in the supplement file (S1
12	# 0.51, 0.79, 0.64; S3 0.70, 0.71, 0.05; S4 0.64, 0.69, 0.47; S5 0.66, 0.74, 0.59; S6 0.60, 0.71,
13	# 0.61, for attend-humans, attend-vehicles and passive). The images of Figures 1 to 4 of the main
14	# text were not available, so the pattern of Figure 3B is not known here. Two inconsistencies of
15	# the paper, noted where they matter. (1) The means of the six per-subject CSIs in Figure 1 and
16	# the supplement (0.64, 0.72, 0.51) are not exactly the means the Results give (0.66, 0.74, 0.53).
17	# (2) The Figure 1 legend says blue is "only humans present" and green "only vehicles present";
18	# the supplement legend and the plotted positions say the reverse (green humans, blue vehicles).
19	# The video game subjects are S1 and S7 in the text and C1 and C2 in the legends of Figure 3 and
20	# Supplementary Figure 4; C1 is S1 (CSI 0.72 in both) and C2 is S7.
[... 441 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,200p /home/runner/.claude/projects/-home-runner-work-encore-encore/08ba0065-1e76-4ae7-a1ef-47208a2ae0b3/tool-results/bwo0xyfca.txt
```

```
=== amjad-2025-01
# 002013, Amjad et al. 2025

Seven claims reproduced, one partially and five blocked on the dandiset,
plus one claim linking the dandiset to the paper's Zenodo deposit,
reproduced (trial lists agree for 99.8 to 100% of trials); both rounds
agreed with every outcome. The paper describes microinvasive probes for
recording dopamine and electrical activity in monkeys; the beta burst,
reward and unit isolation claims reproduce, the dopamine reward effect
weakly (p = 0.023, and not in the stored trial-aligned `da`).

The dandiset was converted by CatalystNeuro (catalystneuro/schwerdt-lab-to-nwb,
the same conversion as 002014), and many findings are the same: each event
is stored about five times, once per overlapping trial window; trial
conditions are not in the trials table; the FSCV table columns carry no
units and the raw FSCV current is labelled amperes with values in the
thousands; the bipolar LFP is stored in volts with a conversion factor that
makes it picovolts; and the raw ephys of one session and the spike times of
Monkey P are on different clocks from the rest of the file, by 9831.35 s and
6800.666 s, with nothing saying so. In addition, one session's trial-aligned
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 200,400p /home/runner/.claude/projects/-home-runner-work-encore-encore/08ba0065-1e76-4ae7-a1ef-47208a2ae0b3/tool-results/bwo0xyfca.txt; head -3 docs/pilot-notes/knierim-2000-02.md; grep -rl "crcns\|CRCNS" docs/pilot-notes | head; head -20 README.md | grep -n "|"
```

```
first run gave none reproduced, one partially, four not reproduced and 28
blocked. The author asked a reader nothing, so the answer and author-answers
runs changed nothing. Round 1 agreed with every outcome and found that the
nondecision time was probably set by a few very early reaction times, that no
clock-drift model had been fitted from the running-speed correlation, that the
lateral traces hid missing values, that the decoder z-scored before the
cross-validation split and that taking the first 1000 rows of 489 as Table S1's
trials was an assumption; in reply every DDM reading was fitted three ways
(all reaction times kept, a uniform mixture, reaction times below 0.1 s
dropped), a speed clock for 503 and a null for the lag search were added, a bug
that left only 212 of 513 (503) and 91 of 249 (489) trials with a value at
t = 2 s was fixed, and on the verifier's suggestion `fig1n-epoch-rates` moved
from blocked to not reproduced. The record's round-1 entry said the claims-file
header had been changed to note the SI's TTL synchronisation, which was wrong.
Round 2 agreed with all 33, found that error and sentences the outputs did not
support (a stored-onset range of 7.27 to 7.48 Hz where the outputs give 7.15 to
7.48 Hz, swapped 95th percentiles, the mixture weight called at its limit in
every fit, 0.12 s called not excluded by the likelihood profile, and "no
alignment can be found" for 489, whose best lags rise from 4.36 to 12.23 s),
and asked for a caveat that the 503 speed clock may reflect running, all
[... 194 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -B3 "asari-2009\`\|zhang" README.md | head -20; grep -n "(+" tools/readme_row.py | head; sed -n 1,60p tools/readme_row.py
```

```
63:            cells.append(f"{n} (+{m})" if m else str(n))
"""The README's table row for a paper, from its latest attempt.

    python tools/readme_row.py PAPER              # print the row (a paper key, or a dataset listed for one)

Counts are of the paper's findings on the dandiset, including those that name its codes from
elsewhere (`with_labels`); findings that also use outside data (`with_inputs`) are shown in brackets;
findings on data in other archives (`elsewhere`) and the registry's link checks (`kind: link`) are
left out, as the README says. A deprecated attempt's row has no counts.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

[... 42 more lines not kept]
```

**Agent**

Outcome counts are 7 reproduced (+1 with outside atlases), 1 partial, 1 not reproduced (+1 with outside atlases), 0 blocked. Now reading the reports and the dataset entry.

**Agent calls Bash**

```bash
cd  python -c "
import json;d=json.load(open('targets/dandisets.json'))
it = d if isinstance(d,list) else d.get('dandisets', d)
import sys
for x in (it if isinstance(it,list) else it.values()):
    if 'vim-4' in json.dumps(x): print(json.dumps(x,indent=1))
" | head -40; cd transcripts/zhang-2021; wc -w *-report.md; ls -la --time-style=full-iso *.md | awk '{print $7, $9}' | sort
```

```
152 answer-report.md
  291 author-answers-report.md
  886 author-report.md
  598 author-revise-1-report.md
  513 author-revise-2-report.md
  606 claims-check-report.md
  601 claims-report.md
 1574 verifier-1-report.md
 1316 verifier-2-report.md
 6537 total
17:46:10.344091590 claims-check-report.md
17:46:10.345810425 claims-check.md
17:46:10.345810425 claims-report.md
17:46:10.345810425 claims.md
17:46:11.699110787 answer-report.md
17:46:11.699110787 answer.md
17:46:11.699110787 author-answers-report.md
17:46:11.699110787 author-answers.md
17:46:11.699110787 author-report.md
17:46:11.699110787 author-revise-1-report.md
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "vim-4" targets/dandisets.json | head; python -c "
import json;d=json.load(open('targets/dandisets.json'));print(type(d), list(d)[:5] if isinstance(d,dict) else d[0])"
```

```
<class 'dict'> ['schema_version', 'generated', 'source', 'counts', 'targets']
```

**Agent**

The dataset has no entry in `targets/dandisets.json` (it is on CRCNS), so there is no `catalystneuro` field and no conversion sentence. Reading the reports.

**Agent calls Bash**

```bash
cd transcripts/zhang-2021; for f in author-report.md author-answers-report.md answer-report.md author-revise-1-report.md author-revise-2-report.md; do echo "=== $f"; cat $f; done
```

```
=== author-report.md
All 11 claims have an outcome, the entry passes `check` and a clean `all` run (1195 s), and the handover package is built in `executed/zhang-2021/handover/`. Nothing is committed. Work ran from 09:59 to 11:29 UTC, well before the 14:14 cutoff.

**(1) Outcomes**

| claim | outcome | key numbers (paper) |
|---|---|---|
| fig1-csi-s2 | reproduced, assumed | 0.740 / 0.718 / 0.676 (0.75 / 0.69 / 0.67); p ≤ 0.001 |
| att-csi-group | reproduced, assumed | 0.665 / 0.729 / 0.525 over 5 subjects (0.66 / 0.74 / 0.53) |
| supp-csi-per-subject | reproduced, assumed | 10 of 12 within tolerance; all significant at p < 0.01 under permutation reading (a) |
| att-passive-lower | not reproduced | 2 or 3 of 5 subjects significant at the bound 1000 permutations allow; 4 needed |
| att-classification | reproduced | 44.4 to 56.3% across the four readings (48.4 ± 7.6); chance under this procedure 7.8 to 9.1% |
| att-weights-cortex | blocked, data_missing | the paper's per-subject ROIs and localizer data are not public |
| game-csi | reproduced | 0.702 / 0.581 with single-state clusters (0.72 / 0.62) |
| game-mutual-negative-projection | reproduced, assumed | all negative, p = 5e-5, with the dataset's column order; Table 1 order fails in S7 |
| fig3b-state-relations | reproduced | under every reading |
| game-classification | partially reproduced | S1 42.8 to 54.6% (32.8 ± 3.8); S7 within tolerance with contiguous folds |
| game-weights-two-groups | blocked, data_missing | no ROIs, and no mapper for S1's game voxels |

**(2) What was found about the dataset**
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/zhang-2021; cat verifier-1-report.md | head -80; echo ======; cat verifier-2-report.md | head -70
```

```
**A. Outcomes** (11 claims in the claims file)

| claim | outcome | reason |
|---|---|---|
| fig1-csi-s2 | reproduced | Cell 15: with the code's positions (R3) S2 gives 0.740, 0.718 and 0.676, all within tolerance and above every null value under both permutation readings (p ≤ 1/1001). The R2 reading also passes. The 2-D variant fails only on attend-humans (0.664 against 0.675). |
| att-csi-group | reproduced | Cell 18, R3: the means are 0.665, 0.729 and 0.525, all within tolerance. Reading (b), the group mean above every mean null value, passes for all three conditions. Reading (a) fails for passive because S3 passive (0.061) does not exceed every null value. |
| supp-csi-per-subject | reproduced | Cell 20: R3 has 10 of 12 values within tolerance, R2 has 11 of 12, and all 12 are significant at p < 0.01 under null (a). The misses are S3 passive (0.061 against 0.05 ± 0.005) and S5 attend-humans (0.767). |
| att-passive-lower | not_reproduced | Cell 22: at most 3 of 5 subjects count at the bound (R3, matched, ii, reading b), and 4 of 5 are needed. S1 and S6 have passive CSI at or above attend-humans, so d_mean is about 0 (p 0.38 to 0.53), and this holds under every reading. The 4 of 5 in the R1/matched/i row at p < 0.05 is the variant that does not decide. |
| att-classification | reproduced | Cell 24: contiguous folds give 44.4% (Euclidean) and 53.4% (density), and random folds with Euclidean give 46.6%, all within 48.4 ± 7.6 and above every null mean. Chance under the procedure is 7.8 to 9.1%, against the paper's 8.3%. |
| att-weights-cortex | blocked (data_missing) | Cell 25: the paper's per-subject ROIs from localizers are not deposited. Part of the claim could still be tested with an fsaverage atlas (see B3). |
| game-csi | reproduced | Cell 28, reading (b): S1 0.702 and S7 0.581, both within tolerance and above every null value. Reading (a) misses for S7 (0.549 against a lower bound of 0.558), and reading (c) misses for both. The pass therefore depends on one re
[... 104 more lines not kept]
```

**Agent**

Writing the notes now.

**Agent calls Bash**

```bash
cd  mkdir -p summaries; python3 - <<'EOF'
import textwrap
paras = [
"Seven claims reproduced on the data set and one more that also uses outside atlases, one partially, one not reproduced and one more not reproduced with outside atlases, and none blocked; six outcomes rest on an assumption. The first verification round agreed with 9 of the 11 outcomes as they stood and the second with all 11; nothing was proposed after the second, so there was no third round. CRCNS data sets carry no version, so the record gives `unversioned` with the data set's DOI, 10.6080/K0668BDF. The paper, Zhang, Gao, Cukur and Gallant in Frontiers in Neuroscience (14:565976), fits a voxel-based state space to fMRI responses (an OLS regression on the task variables, denoised through 24 principal components and orthogonalized by QR) and applies it to a visual attention task, in which subjects S1 to S6 watch natural movies while attending to humans or vehicles or viewing passively, and to a Counter-Strike video game played by S1 and S7. The claims were written from the version of record (PMC8145286) with its supplement and from the paper's code, gallantlab/state-space at commit 6ffb3c30, which holds the state space but no CSI averaging, classifier, permutation test or video game analysis. Reproduced are the separation of the four presence states in S2 (cluster separation index, CSI, 0.739, 0.717 and 0.676 against 0.75, 0.69 and 0.67), over the five released subjects and per subject, the 12-label classification of attention TRs (43.7% against 48.4 +/- 7.6%), the video game CSI (0.702 and 0.582 against 0.72 and 0.62), the mutual negative projection of engage close and safe explore, and the relations between game states of Figure 3B. The attention CSI claims rest on taking the third axis the code gives, and the negative projection on entering the game variables in the data set's column order; with Table 1's order it would hold in S1 only. With atlas regions in place of the paper's ROIs, the human-presence dimension favours FFA, OFA and EBA and the vehicle-presence dimension RSC, PPA and OPA in 4 of 5 subjects with a voxel threshold from the WordNet encoding model, and in 3 of 5 without one. Not reproduced is the lower CSI under passive viewing, significant at the bound 1000 permutations reach in 2 of 5 subjects (S3, S5) where 4 are needed; in S1 and S6 attend-humans is below passive, as in the paper's own figure values. The video game classification is partial: every reading is significant, but S1 is above 32.8 +/- 3.8% under every reading (42.8 to 54.6%). The two groups of game dimensions on the cortex are not reproduced in S7, where three to five of the eight dimensions fail where one may, and S1 could not be placed on the cortex. The author's first run had both cortical claims blocked for missing data; round 1 noted that the claims file offered an fsaverage atlas through the data set's mappers, and in reply both were tested with visfAtlas and HCP-MMP1.0, att-weights-cortex moving to reproduced and game-weights-two-groups to not reproduced. Round 1 also had the code's own attention coefficients printed (about 1e-13 against about 1e2 for human and vehicle), the game analyses repeated with the labels one TR later, the S1 run structure shown and a scoring error in the game classification fixed, where a class left out of a training fold had been scored with a recall of 0. Round 2 found that the text and record gave numbers from an earlier execution on a different machine, which the rounding of the third axis moves, and that S7's game BOLD went in without the z-scoring the paper's Methods describe; the numbers were updated and S7 z-scored, with the data as stored kept as a variant, and no outcome changed. The author asked a reader nothing, so the answer and author-answers runs changed nothing. The author's run took about 1 h 30 min (09:59 to 11:29 UTC); the notebook ran in 1195 s at first, with peak memory 3.9 GB, 51 min after round 1, mostly for the WordNet model, and about 23 min at the end. In the first run supp-csi-per-subject was counted against exceeding every null value where the criterion says p < 0.01, which the author caught from the printed p-values and fixed before handover, moving it from partially reproduced to reproduced.",
"In the deconvolved attention files each attentive condition is z-scored per voxel within the condition, while the passive TRs are not. With the attention state coded -1, 0, +1 in states.hdf, its regression weight is zero (1e-14 in all five subjects), so the attention dimension of the paper's state space cannot be recovered from the deposited files; the third axis is set by rounding and the CSIs move by up to 0.1 with it. The data description does not say how that column codes the condition (-1 attend-humans, 0 passive, +1 attend-vehicles). The functional ROIs, and the localizer and retinotopic mapping data the paper used to define them, are not in the data set, so the cortical claims of Figures 2 and 4 could be tested only on public atlases. No mapper matches the S1 video game data, which have 73,594 voxels: the S1 mapper has 51,608, the voxel set of S1's attention data, and the superseded mappers in Mappers/old have 81,137 (S1), 84,038 (S5) and 86,842 (S6). The S1 video game data hold 1950 TRs (65 min at the 2.0045 s TR), six blocks of 325 TRs, where the data description and the paper say one subject played for 90 minutes in six 15-min runs; S7's 1320 TRs (44 min) match the stated 45 minutes. S7's video game BOLD is not z-scored per voxel (voxel SDs 0.094 to 1.009), unlike S1's, though the paper says responses were normalized to zero mean and unit variance, and the game state columns are not in the order of Table 1. Subject S4 of the attention task is not released. In the paper, the group CSI means (0.66, 0.74, 0.53) are not the means of its own per-subject values (0.64, 0.72, 0.51), and the Figure 1 legend gives the colours of humans and vehicles the reverse of the supplement and the plotted positions. Five questions are put to the paper's authors: how the attention dimension was defined, in what order the nine game variables entered the QR, what the passive-against-attentive test compared and how its labels were permuted, whether the game labels were shifted in time against the BOLD, and which encoding models and tests set the voxel thresholds of Figures 2 and 4.",
"The author's points on the protocol: it has no case for a method that is well defined in the paper but undefined on the deposited data, here the zero-weight attention axis, treated as an assumption with three readings; the claims file left an outside ROI source to the author while the protocol allows outside data only when the paper relies on it, and the first run followed the protocol and blocked both cortical claims; it does not say which value goes under `measured` when no reading matches, and the first reading listed was used; the permutations the criteria need (1000, and 20,000 for the Bonferroni matrix) put the run at 20 minutes against the 10-minute aim, with nothing on how to trade these off; conclusions can only be written after seeing results and every edit forces a full re-run; the schema wants `date` as a string while an unquoted YAML date parses as a date; and archives.md says CRCNS data sets are mostly zips, where this one is plain HDF5 and npy files that streamed with fsspec.",
]
out = "# zhang-2021, Zhang et al. 2021\n\n" + "\n\n".join(textwrap.fill(p, 76, break_on_hyphens=False, break_long_words=False) for p in paras) + "\n"
open("docs/pilot-notes/zhang-2021-01.md","w").write(out)
EOF
grep -c "—" docs/pilot-notes/zhang-2021-01.md; grep -ci "rather" docs/pilot-notes/zhang-2021-01.md
```

```
0
0
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import re,textwrap
p="docs/pilot-notes/zhang-2021-01.md"
t=open(p).read()
head,body=t.split("\n\n",1)
paras=[" ".join(x.split()) for x in body.strip().split("\n\n")]
old="The first verification round agreed with 9 of the 11 outcomes as they stood and the second with all 11; nothing"
new="The first verification round agreed with all 11 outcomes as they stood, though it found that the two blocked claims could be tested in part, and the second agreed with all 11, with game-weights-two-groups only conditionally; nothing"
assert old in paras[0]; paras[0]=paras[0].replace(old,new)
old2="The author's first run had both cortical claims blocked for missing data; round 1 noted"
new2="The author's first run had both cortical claims blocked for missing data; round 1 noted"
open(p,"w").write(head+"\n\n"+"\n\n".join(textwrap.fill(x,76,break_on_hyphens=False,break_long_words=False) for x in paras)+"\n")
EOF
cat docs/pilot-notes/zhang-2021-01.md; wc -w docs/pilot-notes/zhang-2021-01.md
```

```
# zhang-2021, Zhang et al. 2021

Seven claims reproduced on the data set and one more that also uses outside
atlases, one partially, one not reproduced and one more not reproduced with
outside atlases, and none blocked; six outcomes rest on an assumption. The
first verification round agreed with all 11 outcomes as they stood, though
it found that the two blocked claims could be tested in part, and the second
agreed with all 11, with game-weights-two-groups only conditionally; nothing
was proposed after the second, so there was no third round. CRCNS data sets
carry no version, so the record gives `unversioned` with the data set's DOI,
10.6080/K0668BDF. The paper, Zhang, Gao, Cukur and Gallant in Frontiers in
Neuroscience (14:565976), fits a voxel-based state space to fMRI responses
(an OLS regression on the task variables, denoised through 24 principal
components and orthogonalized by QR) and applies it to a visual attention
task, in which subjects S1 to S6 watch natural movies while attending to
humans or vehicles or viewing passively, and to a Counter-Strike video game
played by S1 and S7. The claims were written from the version of record
(PMC8145286) with its supplement and from the paper's code,
gallantlab/state-space at commit 6ffb3c30, which holds the state space but
no CSI averaging, classifier, permutation test or video game analysis.
[... 87 more lines not kept]
```

**Agent**

Now the summary.

**Agent calls Bash**

```bash
cd  cat > summaries/zhang-2021-01.md <<'EOF'
The paper's core result holds in this data: a voxel-based state space separates the task states of both the movie attention and the video game experiments, and classifies held-out time points well above chance. With public atlas regions standing in for the paper's unreleased localizer regions, the attention dimensions also map onto face, body and scene areas in 4 of 5 subjects. The finding that attention sharpens state separation over passive viewing did not reproduce (2 of 5 subjects), and the paper does not say how that test was run. The split of game dimensions into two cortical networks failed in the one player whose data could be mapped; the other player's game data match no cortical mapper.
EOF
wc -w summaries/zhang-2021-01.md; git status --short
```

```
118 summaries/zhang-2021-01.md
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
?? docs/pilot-notes/zhang-2021-01.md
?? scripts
?? summaries/zhang-2021-01.md
```

**Agent calls Bash**

```bash
cd  sed -i 's/The split of game dimensions into two cortical networks failed/The grouping of game dimensions into two sets of cortical regions failed/' summaries/zhang-2021-01.md; wc -w summaries/zhang-2021-01.md; cat summaries/zhang-2021-01.md
```

```
120 summaries/zhang-2021-01.md
The paper's core result holds in this data: a voxel-based state space separates the task states of both the movie attention and the video game experiments, and classifies held-out time points well above chance. With public atlas regions standing in for the paper's unreleased localizer regions, the attention dimensions also map onto face, body and scene areas in 4 of 5 subjects. The finding that attention sharpens state separation over passive viewing did not reproduce (2 of 5 subjects), and the paper does not say how that test was run. The grouping of game dimensions into two sets of cortical regions failed in the one player whose data could be mapped; the other player's game data match no cortical mapper.
```

**Agent calls Bash**

```bash
cd  sed -i 's/ also map onto/ map onto/; s/the other player.s game data match/the other player'"'"'s data match/' summaries/zhang-2021-01.md; wc -w summaries/zhang-2021-01.md
```

```
118 summaries/zhang-2021-01.md
```

**Agent**

I wrote two new files: `docs/pilot-notes/zhang-2021-01.md` and `summaries/zhang-2021-01.md`. No other file was changed and nothing is committed. Two things you should know:

- **No conversion sentence:** CRCNS:vim-4 has no entry in `targets/dandisets.json`, so there is no `catalystneuro` field to report. I left out the "converted by CatalystNeuro" opening.
- **Stray files in the working tree:** there are untracked files (`.bashrc`, `.idea`, `.vscode`, `scripts` and others) that I did not create. The author's report noted them too. If the workflow commits everything untracked, they may be included.

**docs/pilot-notes/zhang-2021-01.md**

# zhang-2021, Zhang et al. 2021

Seven claims reproduced on the data set and one more that also uses outside atlases, one partially, one not reproduced and one more not reproduced with outside atlases, and none blocked; six outcomes rest on an assumption. The first verification round agreed with all 11 outcomes as they stood, though it found that the two blocked claims could be tested in part, and the second agreed with all 11, with game-weights-two-groups only conditionally; nothing was proposed after the second, so there was no third round. CRCNS data sets carry no version, so the record gives `unversioned` with the data set's DOI, 10.6080/K0668BDF. The paper, Zhang, Gao, Cukur and Gallant in Frontiers in Neuroscience (14:565976), fits a voxel-based state space to fMRI responses (an OLS regression on the task variables, denoised through 24 principal components and orthogonalized by QR) and applies it to a visual attention task, in which subjects S1 to S6 watch natural movies while attending to humans or vehicles or viewing passively, and to a Counter-Strike video game played by S1 and S7. The claims were written from the version of record (PMC8145286) with its supplement and from the paper's code, gallantlab/state-space at commit 6ffb3c30, which holds the state space but no CSI averaging, classifier, permutation test or video game analysis. Reproduced are the separation of the four presence states in S2 (cluster separation index, CSI, 0.739, 0.717 and 0.676 against 0.75, 0.69 and 0.67), over the five released subjects and per subject, the 12-label classification of attention TRs (43.7% against 48.4 +/- 7.6%), the video game CSI (0.702 and 0.582 against 0.72 and 0.62), the mutual negative projection of engage close and safe explore, and the relations between game states of Figure 3B. The attention CSI claims rest on taking the third axis the code gives, and the negative projection on entering the game variables in the data set's column order; with Table 1's order it would hold in S1 only. With atlas regions in place of the paper's ROIs, the human-presence dimension favours FFA, OFA and EBA and the vehicle-presence dimension RSC, PPA and OPA in 4 of 5 subjects with a voxel threshold from the WordNet encoding model, and in 3 of 5 without one. Not reproduced is the lower CSI under passive viewing, significant at the bound 1000 permutations reach in 2 of 5 subjects (S3, S5) where 4 are needed; in S1 and S6 attend-humans is below passive, as in the paper's own figure values. The video game classification is partial: every reading is significant, but S1 is above 32.8 +/- 3.8% under every reading (42.8 to 54.6%). The two groups of game dimensions on the cortex are not reproduced in S7, where three to five of the eight dimensions fail where one may, and S1 could not be placed on the cortex. The author's first run had both cortical claims blocked for missing data; round 1 noted that the claims file offered an fsaverage atlas through the data set's mappers, and in reply both were tested with visfAtlas and HCP-MMP1.0, att-weights-cortex moving to reproduced and game-weights-two-groups to not reproduced. Round 1 also had the code's own attention coefficients printed (about 1e-13 against about 1e2 for human and vehicle), the game analyses repeated with the labels one TR later, the S1 run structure shown and a scoring error in the game classification fixed, where a class left out of a training fold had been scored with a recall of 0. Round 2 found that the text and record gave numbers from an earlier execution on a different machine, which the rounding of the third axis moves, and that S7's game BOLD went in without the z-scoring the paper's Methods describe; the numbers were updated and S7 z-scored, with the data as stored kept as a variant, and no outcome changed. The author asked a reader nothing, so the answer and author-answers runs changed nothing. The author's run took about 1 h 30 min (09:59 to 11:29 UTC); the notebook ran in 1195 s at first, with peak memory 3.9 GB, 51 min after round 1, mostly for the WordNet model, and about 23 min at the end. In the first run supp-csi-per-subject was counted against exceeding every null value where the criterion says p < 0.01, which the author caught from the printed p-values and fixed before handover, moving it from partially reproduced to reproduced.

In the deconvolved attention files each attentive condition is z-scored per voxel within the condition, while the passive TRs are not. With the attention state coded -1, 0, +1 in states.hdf, its regression weight is zero (1e-14 in all five subjects), so the attention dimension of the paper's state space cannot be recovered from the deposited files; the third axis is set by rounding and the CSIs move by up to 0.1 with it. The data description does not say how that column codes the condition (-1 attend-humans, 0 passive, +1 attend-vehicles). The functional ROIs, and the localizer and retinotopic mapping data the paper used to define them, are not in the data set, so the cortical claims of Figures 2 and 4 could be tested only on public atlases. No mapper matches the S1 video game data, which have 73,594 voxels: the S1 mapper has 51,608, the voxel set of S1's attention data, and the superseded mappers in Mappers/old have 81,137 (S1), 84,038 (S5) and 86,842 (S6). The S1 video game data hold 1950 TRs (65 min at the 2.0045 s TR), six blocks of 325 TRs, where the data description and the paper say one subject played for 90 minutes in six 15-min runs; S7's 1320 TRs (44 min) match the stated 45 minutes. S7's video game BOLD is not z-scored per voxel (voxel SDs 0.094 to 1.009), unlike S1's, though the paper says responses were normalized to zero mean and unit variance, and the game state columns are not in the order of Table 1. Subject S4 of the attention task is not released. In the paper, the group CSI means (0.66, 0.74, 0.53) are not the means of its own per-subject values (0.64, 0.72, 0.51), and the Figure 1 legend gives the colours of humans and vehicles the reverse of the supplement and the plotted positions. Five questions are put to the paper's authors: how the attention dimension was defined, in what order the nine game variables entered the QR, what the passive-against-attentive test compared and how its labels were permuted, whether the game labels were shifted in time against the BOLD, and which encoding models and tests set the voxel thresholds of Figures 2 and 4.

The author's points on the protocol: it has no case for a method that is well defined in the paper but undefined on the deposited data, here the zero-weight attention axis, treated as an assumption with three readings; the claims file left an outside ROI source to the author while the protocol allows outside data only when the paper relies on it, and the first run followed the protocol and blocked both cortical claims; it does not say which value goes under `measured` when no reading matches, and the first reading listed was used; the permutations the criteria need (1000, and 20,000 for the Bonferroni matrix) put the run at 20 minutes against the 10-minute aim, with nothing on how to trade these off; conclusions can only be written after seeing results and every edit forces a full re-run; the schema wants `date` as a string while an unquoted YAML date parses as a date; and archives.md says CRCNS data sets are mostly zips, where this one is plain HDF5 and npy files that streamed with fsspec.

**summaries/zhang-2021-01.md** (118 words)

The paper's core result holds in this data: a voxel-based state space separates the task states of both the movie attention and the video game experiments, and classifies held-out time points well above chance. With public atlas regions standing in for the paper's unreleased localizer regions, the attention dimensions map onto face, body and scene areas in 4 of 5 subjects. The finding that attention sharpens state separation over passive viewing did not reproduce (2 of 5 subjects), and the paper does not say how that test was run. The grouping of game dimensions into two sets of cortical regions failed in the one player whose data could be mapped; the other player's data match no cortical mapper.

## End of run

17 turns, 2 minutes, $1.10 at API prices, result: success.
