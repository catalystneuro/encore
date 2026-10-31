# 000575 · recorder · run 41149759854

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; python tools/readme_row.py 000575; ls claims/000575 transcripts/000575; cat attempts/000575-boran-2022-01.yaml
```

```
<persisted-output>
Output too large (46.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/571682e0-5645-4ea6-bf82-9e45989e1860/tool-results/b20kvlixn.txt

Preview (first 2KB):
docs/pilot-notes/000576-fedele-2020-01.md
docs/pilot-notes/000467-hart-2023-01.md
docs/pilot-notes/000541-yemini-2021-01.md
docs/pilot-notes/000489-kim-2022-01.md
docs/pilot-notes/000469-kyzar-2024-01.md
| [000575](https://dandiarchive.org/dandiset/000575) | [Boran et al. 2022](https://doi.org/10.1016/j.neuroimage.2022.119123) | 8 | 3 | 6 | 0 | [`000575-boran-2022`](entries/000575-boran-2022) |
claims/000575:
10.1016-j.neuroimage.2022.119123.yaml

transcripts/000575:
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
[... 49 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/000575-boran-2022-01.yaml; for f in docs/pilot-notes/000576-fedele-2020-01.md docs/pilot-notes/000467-hart-2023-01.md docs/pilot-notes/000541-yemini-2021-01.md docs/pilot-notes/000489-kim-2022-01.md docs/pilot-notes/000469-kyzar-2024-01.md docs/pilot-notes/001754-knierim-2000-02.md; do echo "=== $f"; cat $f; done; python -c "
import json;d=json.load(open('targets/dandisets.json'));
d=d if isinstance(d,list) else d.get('dandisets',d)
for e in (d if isinstance(d,list) else d.values()):
  if '000575' in json.dumps(e)[:200]: print(json.dumps(e,indent=1))"
```

```
<persisted-output>
Output too large (84.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/571682e0-5645-4ea6-bf82-9e45989e1860/tool-results/b4fxgse83.txt

Preview (first 2KB):
schema_version: 2
id: 000575-boran-2022-01
dataset:
  archive: dandi
  id: "000575"
  version: 0.231010.1811
  doi: 10.48324/dandi.000575/0.231010.1811
paper: doi:10.1016/j.neuroimage.2022.119123
date: 2026-10-30
entry: 000575-boran-2022
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
[... 35 more lines not kept]
```

**Agent**

Too large; read in pieces.

**Agent calls Read**

```json
{
 "file_path": "attempts/000575-boran-2022-01.yaml"
}
```

```
1	schema_version: 2
2	id: 000575-boran-2022-01
3	dataset:
4	  archive: dandi
5	  id: "000575"
6	  version: 0.231010.1811
7	  doi: 10.48324/dandi.000575/0.231010.1811
8	paper: doi:10.1016/j.neuroimage.2022.119123
9	date: 2026-10-30
10	entry: 000575-boran-2022
11	provenance:
12	  kind: agent
13	  accountable:
14	    name: CatalystNeuro
15	  agent:
16	    harness: Claude Code
17	    model: claude-opus-5-5
18	    protocol: pilot-12
19	  runner:
20	    platform: GitHub Actions
[... 762 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for f in docs/pilot-notes/000576-fedele-2020-01.md docs/pilot-notes/000467-hart-2023-01.md docs/pilot-notes/000541-yemini-2021-01.md docs/pilot-notes/000489-kim-2022-01.md docs/pilot-notes/000469-kyzar-2024-01.md docs/pilot-notes/001754-knierim-2000-02.md; do echo "=== $f"; cat $f; done; grep -n -B3 -A25 '"000575"' targets/dandisets.json | head -60
```

```
<persisted-output>
Output too large (39.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/571682e0-5645-4ea6-bf82-9e45989e1860/tool-results/bry2cdkcd.txt

Preview (first 2KB):
=== docs/pilot-notes/000576-fedele-2020-01.md
# 000576, Fedele et al. 2020

No claim reproduced, three partially, 12 not reproduced and three blocked on
the dandiset; with outside data, counted apart, one partially reproduced and
six blocked. The first verification round agreed with 20 of 25 outcomes and
the second with all 25, so there was no third round. It pins version
0.231010.1811, the only published version; the paper predates the dandiset
and cites none. The paper, Fedele, Tzovara et al. in NeuroImage, records
macroelectrode iEEG and microwire units in the 14 amygdalae of nine patients
with drug-resistant mesial temporal lobe epilepsy while they watch blocks of
dynamic fearful faces (AVERSIVE) and landscapes (NEUTRAL), and relates a
sustained delta power decrease and an onset increase in high gamma power
(HGP) to neuronal firing and to the BOLD signal of a pre-operative fMRI, with
the HGP modulation index (MI) separating amygdalae outside the seizure onset
zone (nSOZ) from those within it (SOZ). The claims were written from the
[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/571682e0-5645-4ea6-bf82-9e45989e1860/tool-results/bry2cdkcd.txt"
}
```

```
1	=== docs/pilot-notes/000576-fedele-2020-01.md
2	# 000576, Fedele et al. 2020
3	
4	No claim reproduced, three partially, 12 not reproduced and three blocked on
5	the dandiset; with outside data, counted apart, one partially reproduced and
6	six blocked. The first verification round agreed with 20 of 25 outcomes and
7	the second with all 25, so there was no third round. It pins version
8	0.231010.1811, the only published version; the paper predates the dandiset
9	and cites none. The paper, Fedele, Tzovara et al. in NeuroImage, records
10	macroelectrode iEEG and microwire units in the 14 amygdalae of nine patients
11	with drug-resistant mesial temporal lobe epilepsy while they watch blocks of
12	dynamic fearful faces (AVERSIVE) and landscapes (NEUTRAL), and relates a
13	sustained delta power decrease and an onset increase in high gamma power
14	(HGP) to neuronal firing and to the BOLD signal of a pre-operative fMRI, with
15	the HGP modulation index (MI) separating amygdalae outside the seizure onset
16	zone (nSOZ) from those within it (SOZ). The claims were written from the
17	version of record, a PDF supplied by a person; the paper links no analysis
18	code, and the data descriptor (Fedele et al. 2021) was read for the layout of
19	the data only. The iEEG and spike claims were tested; the six claims that
20	need the BOLD time courses and the muHGP claim are blocked as `data_missing`,
[... 569 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/000575; ls -la --time-style=full-iso; wc -w *-report.md; cat author-report.md
```

```
total 696
drwxr-xr-x   2 runner runner   4096 2026-10-31 00:22:26.703934567 +0000 .
drwxr-xr-x 233 runner runner   4096 2026-10-31 00:22:25.531010294 +0000 ..
-rw-r--r--   1 runner runner   1321 2026-10-31 00:22:26.701954823 +0000 answer-report.md
-rw-r--r--   1 runner runner   8570 2026-10-31 00:22:26.701954823 +0000 answer.md
-rw-r--r--   1 runner runner   3518 2026-10-31 00:22:26.701954823 +0000 author-answers-report.md
-rw-r--r--   1 runner runner  72243 2026-10-31 00:22:26.701954823 +0000 author-answers.md
-rw-r--r--   1 runner runner   5341 2026-10-31 00:22:26.701954823 +0000 author-report.md
-rw-r--r--   1 runner runner   4107 2026-10-31 00:22:26.701954823 +0000 author-revise-1-report.md
-rw-r--r--   1 runner runner 140033 2026-10-31 00:22:26.702934631 +0000 author-revise-1.md
-rw-r--r--   1 runner runner   2617 2026-10-31 00:22:26.702934631 +0000 author-revise-2-report.md
-rw-r--r--   1 runner runner  53926 2026-10-31 00:22:26.702934631 +0000 author-revise-2.md
-rw-r--r--   1 runner runner 226853 2026-10-31 00:22:26.703934567 +0000 author.md
-rw-r--r--   1 runner runner   2862 2026-10-31 00:22:25.337816107 +0000 claims-check-report.md
-rw-r--r--   1 runner runner  23895 2026-10-31 00:22:25.338493306 +0000 claims-check.md
-rw-r--r--   1 runner runner   3792 2026-10-31 00:22:25.338493306 +0000 claims-report.md
-rw-r--r--   1 runner runner  50802 2026-10-31 00:22:25.338493306 +0000 claims.md
-rw-r--r--   1 runner runner   9528 2026-10-31 00:22:26.703934567 +0000 verifier-1-report.md
-rw-r--r--   1 runner runner  25178 2026-10-31 00:22:26.703934567 +0000 verifier-1.md
-rw-r--r--   1 runner runner   7008 2026-10-31 00:22:26.703934567 +0000 verifier-2-report.md
[... 71 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/000575; for f in answer-report.md author-answers-report.md verifier-1-report.md author-revise-1-report.md verifier-2-report.md author-revise-2-report.md; do echo "=== $f"; cat $f; done
```

```
=== answer-report.md
There was one question, and I changed the claims file to answer it.

**neurons-recorded: changed.** The paper never says how a neuron is assigned to a region. Methods 2.5 says the neurons were grouped "according to their anatomical region". The Figure 1d legend shows the microwire tip locations colour-coded by region. The Table 1 legend only spells out the electrode abbreviations (AH, PH, EC, A). The claim's criterion had chosen the electrode-name rule without citing anything for it.

- **New criterion:** it now gives two readings and passes the claim if all values fall within tolerance under either one:
  - (a) by where the microwire tips sit anatomically, as Figure 1d shows them;
  - (b) by electrode name.
- **Other per-region claims:** fig2c, fig2d, fig3b and fig4d use whichever reading this claim is judged under.
- **Header:** the list of details the paper leaves open now includes the region assignment.
- **Expected values:** unchanged (809 neurons in total; 454 hippocampus, 209 entorhinal cortex, 146 amygdala).

The question has `answered: 2026-10-30`. `tools/claims_check.py` reports 0 problems. Nothing was committed or pushed. Several untracked files are in the repo root (dotfiles such as `.bashrc`, plus `.idea`, `.vscode` and `scripts/`). They aren't part of this change and I left them alone.
=== author-answers-report.md
The reader's answer changed no outcome. I re-ran every affected claim under both region readings the amended criterion names, and each claim comes out the same under both readings as it did before.

`entry.py lock` and `all` passed with 0 errors; the notebook takes about 14.5 minutes. The numbers came out the same in two clean runs, and the conclusions match the executed copy. The handover is built in `executed/000575-boran-2022/handover/`. Nothing is committed or pushed, and I did not verify my own work.

## The question: how units are assigned to regions (neurons-recorded)

[... 235 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -60 claims/000575/*.yaml; grep -n "^  - id:\|^- id:" claims/000575/*.yaml | head -30
```

```
# Claims for Boran, Hilfiker, Stieglitz, Sarnthein & Klaver (2022), NeuroImage 254, 119123, on
# dandiset 000575.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read: the version of record (paper/10.1016-j.neuroimage.2022.119123.txt, extracted from the
# publisher PDF), with its Methods, Results, figure legends and Table 1. The paper has no
# supplement and cites none. Figures 2c, 2d, 3b and 4d were read from the PDF for the per-region
# counts and accuracies that the text does not print.
#
# Code read: the paper's Data and code availability names one repository,
# https://gin.g-node.org/USZ_NCH/Human_MTL_units_visual_WM. GIN did not answer from this run;
# its listing was read from the Internet Archive snapshot of 2026-10-15 (head commit
# 5ccc2377802efec9522e3c3baa0e600419ee4383, data files at commit 798bf013ee). It holds the 16
# session files (Data_Subject_XX_Session_YY.h5, NIX format), a README and a LICENSE. The README
# describes a code_MATLAB folder with a data-loading example script only, and that folder is not
# on master. No analysis code is published, so no method detail below is settled by code. The
# dandiset is a variant form of this GIN repository (its related resources say so).
# The Methods say the recording scheme and non-task-specific analyses are "identical to Boran
# et al. (2019)" and that dPCA methods were adapted from Kaminski et al. (2017). Neither paper is
[... 57 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/000575-boran-2022-01.md",
 "content": "# 000575, Boran et al. 2022\n\nEight claims reproduced, three partially, six not reproduced and none blocked,\nand both verification rounds agreed with all 17 outcomes, so there was no\nthird round. It pins version 0.231010.1811. The paper, Boran, Hilfiker,\nStieglitz, Sarnthein and Klaver in NeuroImage, records 809 units from\nmicrowires in the hippocampus, entorhinal cortex and amygdala of 13 epilepsy\npatients over 16 sessions of a change detection task with arrays of 1, 2, 4\nor 6 coloured squares, and reports persistent firing during maintenance that\nrelates to workload and performance, with per-neuron permutation tests, dPCA\nand decoding of workload. The claims were written from the version of record;\nthe paper names a GIN repository of NIX files, of which the dandiset is a\nvariant form, and publishes no analysis code. All 17 claims were tested. The\nbehaviour, Table 1 (all 13 Kmax values and all 13 neuron counts exact), the\nfiring rates by period, the fig2c maintenance neuron counts and the dPCA speed\nclaim reproduce, as does `decode-performance-not-significant`, which carries\nlittle weight since the same pipeline does not decode workload.\n`neurons-recorded` and `fig2c-maintenance-neurons` rest on an assumption: the\n133 units whose tip contact has no MTL label are placed by the nearest contact\nof their bundle with one (a2), giving 467, 196 and 146 neurons against 454,\n209 and 146, a choice made after seeing the counts that differs from the\nelectrode-name fallback (a1) only for 28 units on PHR of participant 8; under\n(a1) the entorhinal count is 168, below the tolerance floor of 188.1.\n`behavior-rt-set-size` is partially reproduced, as F = 48.47 equals the\npaper's on per-session median RT while the slope is 68.8 to 76.2 ms/item\nagainst 118; the fit of the median RTs on the condition step (1 to 4) gives\n118.1 ms per step. `fig3b-test-neurons` and\n`fig4c-distance-largest-in-maintenance` are partial, the latter carrying\nlittle weight. Not reproduced are `spike-sorting-quality` (ISI SD 1.77 against\n1.54, SNR 5.93 against 3.81) and every claim that compares trials by their\nlabels: workload-modulated maintenance neurons (2, 0 and 2 against 10, 5 and\n6), maintenance neurons on correct against incorrect trials, the dPCA\nseparation of set sizes (variances within tolerance, but p = 0.35 against\nshuffled labels) and workload decoding (0.442 for all neurons against 87.5%).\nThe author's first run gave six reproduced, five partially and six not\nreproduced. The author asked a reader how units are assigned to regions; the\nanswer added the tip-location reading to the claims file, and the following\nauthor run changed no outcome. Round 1 agreed with all 17 outcomes then\nstated; it found that no other placement of the 133 units had been tried, that\nthe claims file's slope readings regress RT on the set size where the\ncondition step gives the paper's 118.1 ms, that decoding at k = 0 sits below\nchance with a decoder sound on synthetic data, and that the promised\n5000-permutation check of fig2c was missing. In reply neurons-recorded and\nfig2c moved to reproduced (assumed), a per-session alignment scan was added,\nand the slope reading became a second question to a reader. Round 2 agreed\nwith all 17, found (a2) acceptable but weakly grounded, and found sentences\nthe outputs did not support, among them the summary's F = 89.79 for accuracy\n(89.78 printed) and a three-trial misalignment stated for the complete\nsessions where only P03S1 and P06S1 support it, which were corrected. The\nauthor's run took about 1 h 25 min (19:31 to about 20:55 UTC) and nothing\nfailed. The notebook ran in 18 minutes at first and in about 15 to 16 minutes\nin the last runs; the verifier's run took 26.9.\n\nThe spikes may be misaligned with the trial table: workload information is at\nchance in every session with spikes paired to their own trial's label\n(p = 0.12 to 0.94), and pooled over the 7 sessions with all 192 trials it\npeaks at trial i + 3 (corrected p = 0.005), where decoding gives 0.60 against\n0.46 as deposited, but only P03S1 and P06S1 have p < .05 at that shift, the 9\nshorter sessions show no single shift, and the trial table holds no source\nnumbering, so a single offset is not established. Each unit's location is the\natlas label of the macro contact whose number equals its microwire number, so\n614 of 809 units get a label outside hippocampus, parahippocampal gyrus and\namygdala, and the dandiset holds neither the paper's assignment of units to\nregions nor the microwire tip locations of Figure 1d; five units are on\nbundles (PCL, HL, HR) that the subject descriptions do not list as implanted.\nParticipant 12's two sessions are each deposited twice, in four files with the\nsame session start time (2016-12-17 10:38), told apart only by their\nidentifiers. The response timestamps put 1385 of 3038 responses before the\ntest array; the conversion adds the trial start and a 1.7 s offset to the\nstored response time, which read that way gives response times of 0.41 to\n3.15 s from test onset, and the response series does not say what its\ntimestamps mean. Sessions hold 174 to 192 trials (3038 in all) where the paper\nand the task description state 192, and which trials were left out is not\ndocumented. Spikes are stored only inside trial windows, so the inter-trial\ninterval cannot be analysed, and the fixation period is a fixed 0.9 s where\nthe task description has a jittered dot. The paper gives the response time\nANOVA (F = 48.47) on mean response time, while on this dataset that F comes\nexactly from per-session median response times (mean gives 61.36).\n\nThe author's points on the protocol: it says to check the clock but not what\nto do when trial labels turn out misaligned, and the data were tested as\ndeposited with the three-trial shift as a variant; the claims file defined\nregions only in the neurons-recorded criterion, and that rule was applied to\nevery per-region claim; there is no rule for cutting permutation or\nresampling counts below the paper's to fit the time limit, and each cut was\nrecorded as a deviation; some criteria define no partial condition, and the\ngeneral outcome definitions were used; the `measured` rule does not cover the\ncase where no reading matches fully; there is no guidance for a reading the\ndata cannot support; and it is not clear whether code used only to interpret\nmetadata, here the conversion's 1.7 s offset, belongs under `inputs`.\n"
}
```

```
File created successfully at: docs/pilot-notes/000575-boran-2022-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  git status --short; grep -nE '—|rather|\*\*' docs/pilot-notes/000575-boran-2022-01.md
```

```
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
?? docs/pilot-notes/000575-boran-2022-01.md
?? scripts
```

**Agent**

I wrote `docs/pilot-notes/000575-boran-2022-01.md` and changed no other file. The new file contains no em dashes, no "rather" and no bold. The other untracked files in the repository root (`.bashrc`, `.idea`, `scripts` and the rest) were already there before this run, and I left them alone.

# 000575, Boran et al. 2022

Eight claims reproduced, three partially, six not reproduced and none blocked, and both verification rounds agreed with all 17 outcomes, so there was no third round. It pins version 0.231010.1811. The paper, Boran, Hilfiker, Stieglitz, Sarnthein and Klaver in NeuroImage, records 809 units from microwires in the hippocampus, entorhinal cortex and amygdala of 13 epilepsy patients over 16 sessions of a change detection task with arrays of 1, 2, 4 or 6 coloured squares, and reports persistent firing during maintenance that relates to workload and performance, with per-neuron permutation tests, dPCA and decoding of workload. The claims were written from the version of record; the paper names a GIN repository of NIX files, of which the dandiset is a variant form, and publishes no analysis code. All 17 claims were tested. The behaviour, Table 1 (all 13 Kmax values and all 13 neuron counts exact), the firing rates by period, the fig2c maintenance neuron counts and the dPCA speed claim reproduce, as does `decode-performance-not-significant`, which carries little weight since the same pipeline does not decode workload. `neurons-recorded` and `fig2c-maintenance-neurons` rest on an assumption: the 133 units whose tip contact has no MTL label are placed by the nearest contact of their bundle with one (a2), giving 467, 196 and 146 neurons against 454, 209 and 146, a choice made after seeing the counts that differs from the electrode-name fallback (a1) only for 28 units on PHR of participant 8; under (a1) the entorhinal count is 168, below the tolerance floor of 188.1. `behavior-rt-set-size` is partially reproduced, as F = 48.47 equals the paper's on per-session median RT while the slope is 68.8 to 76.2 ms/item against 118; the fit of the median RTs on the condition step (1 to 4) gives 118.1 ms per step. `fig3b-test-neurons` and `fig4c-distance-largest-in-maintenance` are partial, the latter carrying little weight. Not reproduced are `spike-sorting-quality` (ISI SD 1.77 against 1.54, SNR 5.93 against 3.81) and every claim that compares trials by their labels: workload-modulated maintenance neurons (2, 0 and 2 against 10, 5 and 6), maintenance neurons on correct against incorrect trials, the dPCA separation of set sizes (variances within tolerance, but p = 0.35 against shuffled labels) and workload decoding (0.442 for all neurons against 87.5%). The author's first run gave six reproduced, five partially and six not reproduced. The author asked a reader how units are assigned to regions; the answer added the tip-location reading to the claims file, and the following author run changed no outcome. Round 1 agreed with all 17 outcomes then stated; it found that no other placement of the 133 units had been tried, that the claims file's slope readings regress RT on the set size where the condition step gives the paper's 118.1 ms, that decoding at k = 0 sits below chance with a decoder sound on synthetic data, and that the promised 5000-permutation check of fig2c was missing. In reply neurons-recorded and fig2c moved to reproduced (assumed), a per-session alignment scan was added, and the slope reading became a second question to a reader. Round 2 agreed with all 17, found (a2) acceptable but weakly grounded, and found sentences the outputs did not support, among them the summary's F = 89.79 for accuracy (89.78 printed) and a three-trial misalignment stated for the complete sessions where only P03S1 and P06S1 support it, which were corrected. The author's run took about 1 h 25 min (19:31 to about 20:55 UTC) and nothing failed. The notebook ran in 18 minutes at first and in about 15 to 16 minutes in the last runs; the verifier's run took 26.9.

The spikes may be misaligned with the trial table: workload information is at chance in every session with spikes paired to their own trial's label (p = 0.12 to 0.94), and pooled over the 7 sessions with all 192 trials it peaks at trial i + 3 (corrected p = 0.005), where decoding gives 0.60 against 0.46 as deposited, but only P03S1 and P06S1 have p < .05 at that shift, the 9 shorter sessions show no single shift, and the trial table holds no source numbering, so a single offset is not established. Each unit's location is the atlas label of the macro contact whose number equals its microwire number, so 614 of 809 units get a label outside hippocampus, parahippocampal gyrus and amygdala, and the dandiset holds neither the paper's assignment of units to regions nor the microwire tip locations of Figure 1d; five units are on bundles (PCL, HL, HR) that the subject descriptions do not list as implanted. Participant 12's two sessions are each deposited twice, in four files with the same session start time (2016-12-17 10:38), told apart only by their identifiers. The response timestamps put 1385 of 3038 responses before the test array; the conversion adds the trial start and a 1.7 s offset to the stored response time, which read that way gives response times of 0.41 to 3.15 s from test onset, and the response series does not say what its timestamps mean. Sessions hold 174 to 192 trials (3038 in all) where the paper and the task description state 192, and which trials were left out is not documented. Spikes are stored only inside trial windows, so the inter-trial interval cannot be analysed, and the fixation period is a fixed 0.9 s where the task description has a jittered dot. The paper gives the response time ANOVA (F = 48.47) on mean response time, while on this dataset that F comes exactly from per-session median response times (mean gives 61.36).

The author's points on the protocol: it says to check the clock but not what to do when trial labels turn out misaligned, and the data were tested as deposited with the three-trial shift as a variant; the claims file defined regions only in the neurons-recorded criterion, and that rule was applied to every per-region claim; there is no rule for cutting permutation or resampling counts below the paper's to fit the time limit, and each cut was recorded as a deviation; some criteria define no partial condition, and the general outcome definitions were used; the `measured` rule does not cover the case where no reading matches fully; there is no guidance for a reading the data cannot support; and it is not clear whether code used only to interpret metadata, here the conversion's 1.7 s offset, belongs under `inputs`.

## End of run

11 turns, 1 minutes, result: success.
