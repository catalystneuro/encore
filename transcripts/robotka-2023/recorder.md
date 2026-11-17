# robotka-2023 · recorder · run 43687563267

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; ls transcripts/robotka-2023/; python tools/readme_row.py robotka-2023; grep -n -i -B3 -A15 'aa-5' targets/dandisets.json | head -60
```

```
docs/pilot-notes/amjad-2025-01.md
docs/pilot-notes/andrews-2024-01.md
docs/pilot-notes/armstrong-2026-01.md
docs/pilot-notes/asari-2009-01.md
docs/pilot-notes/ashworth-2025-01.md
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
author-revise-1.md
author-revise-2-report.md
author-revise-2.md
author.md
claims-check-report.md
claims-check.md
claims-report.md
claims.md
verifier-1-report.md
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd docs/pilot-notes; for f in amjad-2025-01 andrews-2024-01 armstrong-2026-01 asari-2009-01 ashworth-2025-01 knierim-2000-02; do echo "=== $f"; cat $f.md; done; cd ../..; grep -n -i 'robotka\|aa-5' targets/dandisets.json | head; head -c 1500 targets/dandisets.json
```

```
<persisted-output>
Output too large (41.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/aab8eaae-d5b9-4bea-9eb1-778bb491888c/tool-results/bxx85p5u2.txt

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

**Agent calls Bash**

```bash
cat attempts/robotka-2023-01.yaml claims/robotka-2023.yaml
```

```
<persisted-output>
Output too large (108.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/aab8eaae-d5b9-4bea-9eb1-778bb491888c/tool-results/ba1pi4vqw.txt

Preview (first 2KB):
schema_version: 3
id: robotka-2023-01
datasets:
- archive: crcns
  id: aa-5
  version: unversioned
  doi: 10.6080/K0TT4P5Q
  relation: primary
paper: doi:10.1016/j.celrep.2023.112034
date: 2026-11-14
entry: robotka-2023
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
[... 29 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/aab8eaae-d5b9-4bea-9eb1-778bb491888c/tool-results/bxx85p5u2.txt"
}
```

```
1	=== amjad-2025-01
2	# 002013, Amjad et al. 2025
3	
4	Seven claims reproduced, one partially and five blocked on the dandiset,
5	plus one claim linking the dandiset to the paper's Zenodo deposit,
6	reproduced (trial lists agree for 99.8 to 100% of trials); both rounds
7	agreed with every outcome. The paper describes microinvasive probes for
8	recording dopamine and electrical activity in monkeys; the beta burst,
9	reward and unit isolation claims reproduce, the dopamine reward effect
10	weakly (p = 0.023, and not in the stored trial-aligned `da`).
11	
12	The dandiset was converted by CatalystNeuro (catalystneuro/schwerdt-lab-to-nwb,
13	the same conversion as 002014), and many findings are the same: each event
14	is stored about five times, once per overlapping trial window; trial
15	conditions are not in the trials table; the FSCV table columns carry no
16	units and the raw FSCV current is labelled amperes with values in the
17	thousands; the bipolar LFP is stored in volts with a conversion factor that
18	makes it picovolts; and the raw ephys of one session and the spike times of
19	Monkey P are on different clocks from the rest of the file, by 9831.35 s and
20	6800.666 s, with nothing saying so. In addition, one session's trial-aligned
[... 609 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/aab8eaae-d5b9-4bea-9eb1-778bb491888c/tool-results/ba1pi4vqw.txt"
}
```

```
1	schema_version: 3
2	id: robotka-2023-01
3	datasets:
4	- archive: crcns
5	  id: aa-5
6	  version: unversioned
7	  doi: 10.6080/K0TT4P5Q
8	  relation: primary
9	paper: doi:10.1016/j.celrep.2023.112034
10	date: 2026-11-14
11	entry: robotka-2023
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-15
20	  runner:
[... 824 more lines not kept]
```

**Agent calls Bash**

```bash
cat tools/readme_row.py | head -120; grep -n "aa-5\|robotka" -r targets/ | head
```

```
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

ROOT = Path(__file__).resolve().parents[1]
[... 66 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/aab8eaae-d5b9-4bea-9eb1-778bb491888c/tool-results/ba1pi4vqw.txt",
 "offset": 845,
 "limit": 950
}
```

```
845	    agrees: true
846	    outcome: blocked
847	    reason: The acoustic claims are blocked as data_missing.
848	    response: No change.
849	  - claim: anesth-auditory-units
850	    agrees: true
851	    outcome: blocked
852	    reason: The aa-4 claims are blocked as other.
853	    response: No change.
854	  - claim: anesth-decoding-better
855	    agrees: true
856	    outcome: blocked
857	    reason: The aa-4 claims are blocked as other.
858	    response: No change.
859	  - claim: anesth-regressions
860	    agrees: true
861	    outcome: blocked
862	    reason: The aa-4 claims are blocked as other.
863	    response: No change.
864	  - claim: anesth-primary-secondary-rate
[... 929 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import yaml
r=yaml.safe_load(open('attempts/robotka-2023-01.yaml'))
for o in r['outcomes']: print(o['claim'],o['outcome'],o.get('assumed',''))
print(len(r['outcomes']))
print([k for k in r if k not in ('outcomes','verifications','findings')])
"; sed -n 1540,1570p targets/crcns.json; grep -n -A8 'aa-5' targets/contributors.yaml
```

```
stimulus-set-link reproduced 
paper-good-units-link partially_reproduced 
auditory-units reproduced 
inhibited-units reproduced 
fig3c-peak-call-types reproduced True
fig4a-unit-z-vs-zt reproduced 
good-units-100 not_reproduced 
fig4b-ensemble-20 reproduced True
fig4b-top-ensembles reproduced True
fig4b-confusions reproduced 
figs4-per-bird-and-sex blocked 
figs6-primary-vs-secondary blocked 
fig5e-volume reproduced True
fig5f-si-unrelated reproduced 
fig5g-entropy-selectivity reproduced 
fig5h-neural-noise partially_reproduced 
fig5-multiple-regression reproduced True
pcs-variance reproduced 
table1-snr reproduced 
figs5-region-anova blocked 
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1570,1580p targets/crcns.json; cd transcripts/robotka-2023; wc -w *-report.md; cat author-report.md
```

```
"preprint": false
    }
   ],
   "catalystneuro": []
  },
  {
   "id": "ac-3",
   "name": "High-density extracellular recordings from the primary auditory cortex in anesthetized rats listening to dynamic broadband stimuli",
   "url": "http://crcns.org/data-sets/ac/ac-3",
   "doi": "10.6080/K09021X1",
   "published_version": null,
  151 answer-report.md
  316 author-answers-report.md
  877 author-report.md
  608 author-revise-1-report.md
  542 author-revise-2-report.md
  569 claims-check-report.md
  641 claims-report.md
 1846 verifier-1-report.md
 1212 verifier-2-report.md
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/robotka-2023; for f in author-revise-1-report.md author-revise-2-report.md answer-report.md author-answers-report.md; do echo "=== $f"; cat $f; done
```

```
=== author-revise-1-report.md
I've worked through every point of the round-1 report, re-run the entry twice from a clean environment (the final run passed in 46.5 minutes), and the record's numbers match that run exactly. `check` reports 0 errors and the handover package is rebuilt. Nothing is committed.

**Outcomes changed (allowed in this round)**
- **fig5e-volume:** partially reproduced → reproduced, resting on an assumption. With the code's cross-validation, sound window and discriminant axes, R2adj is 0.094 (tolerance 0.1 ± 0.01), F(1,68) = 7.28, p = 0.0088. The criterion names the window and axes as readings, and the paper's printed F comes from the code's choices. The Methods' choices give 0.120, outside tolerance.
- **fig5-multiple-regression:** partially reproduced → reproduced, resting on an assumption. With the code's axes R2adj is 0.238 to 0.241 (tolerance 0.22 ± 0.022).
- **good-units-100:** kept not reproduced, disagreement recorded. The verifier would say partially reproduced. The criterion takes the count from one run, which gives 89 (tolerance 90 to 110), and it has no partial outcome when the total is out of tolerance.
- Every other outcome is unchanged and matches the verifier's.

**Added or corrected**
- **Cross-validation (B1):** a synthetic check shows what the code's scheme measures. With units that respond only to individual exemplars and carry no call-type signal, it scores 78.2%; the Methods' scheme scores 9.8% (chance is 10%). This is now stated in the deviation, the notes and the question for the paper's authors.
- **good-units-100 (B2):** per-bird counts for each of the 10 seeds are printed; ZF6M has 8 to 14 good units in every one, never within 16 ± 1.6. Of the paper's 91 listed units in the dataset, 29, 14, 9 and 18 per bird are good here.
- **Entropy Selectivity (B3):** this is about the claims file's reading, so I added a question to `questions/robotka-2023.yaml` and kept fig5g reproduced as the file has it. The notes say that with t
[... 65 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/robotka-2023; head -c 4000 verifier-1-report.md; echo; echo =====; head -c 3500 verifier-2-report.md; ls questions | grep -i robotka; git -C  log --format='%h %ad %s' --date=iso -- transcripts/robotka-2023 attempts/robotka-2023-01.yaml | head
```

```
**Verifier report, round 1: Robotka et al. 2023 on CRCNS aa-5**

The claims file has 30 claims. The notebook runs tests for 19 of them and treats 11 as blocked.

### A. Outcomes

| claim id | outcome | reason |
|---|---|---|
| stimulus-set-link | reproduced | Cell 14: 4 birds, 110 stimuli, and the counts per call type match the paper exactly (diff 0 for all 10). |
| paper-good-units-link | partially_reproduced | Cell 8/10: 91 of the 100 listed units are in the dataset, and all 91 are auditory with all 110 stimuli. The 9 missing units all come from the `ZF4F_2t_190613_101015.old` site folder, which is not in the archive. 91 is at least 90. |
| auditory-units | reproduced | Cell 16: 287 auditory units (292 ± 29.2). Under reading (b), counted as pickles with vocalization trials, the total is 726 (730 ± 73) and the fraction 39.5% (40.1 ± 4.01). Under (a) the SNR ≥ 5 units are 414 or 491, which is out of tolerance. |
| inhibited-units | reproduced | Cell 18: 47 of 287 = 16.4% (46 ± 4.6; 15.7 ± 1.57). |
| fig3c-peak-call-types | reproduced (code zCT reading only) | Cell 24, reading (b): Di ranks first and So second; peak counts Di 53 and So 58 are in tolerance; Ag, Be, So and Di are 4 of the top 5. Under the Methods reading (a) the ranking is So > Ag > Di, which would be not_reproduced. |
| fig4a-unit-z-vs-zt | reproduced | Cell 26: 187 units (191 ± 19.1). Every reading puts both means in tolerance; reading (a) gives Z 10.68, Z+T 12.05, paired t(186) = 7.17, p < 1e-5. |
| good-units-100 | partially_reproduced | Cell 28, reading (b): the designated single run gives 89, one below the tolerance band of 90–110. Ten other seeds give 87–101 (8 of 10 in tolerance), and 100 repetitions give 91. ZF6M has 10 good units against the paper's 16, out of tolerance in every run shown. Reading (a) gives 77. Applied strictly to the one designated run, the outcome would be not_reproduced. |
| fig4b-ensemble-20 | reproduced (code CV reading) | Cell 30, reading (b): Z+T 43.15 and Z 30.36, ris
[... 44 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/robotka-2023-01.md",
 "content": "# robotka-2023, Robotka et al. 2023\n\nThirteen claims reproduced (five on an assumption), one partially, one not\nreproduced and four blocked, with five more blocked that also use outside\ndata, the acoustic clustering claims; the two link claims, `stimulus-set-link`\n(reproduced, the paper's 110 stimuli and call-type counts exactly) and\n`paper-good-units-link` (partially reproduced, 91 of the paper's 100 listed\ngood units), and the four claims on CRCNS aa-4 are counted apart. The first\nverification round agreed with 27 of the 30 outcomes as they stood and the\nsecond with all 30; nothing was proposed after the second, so there was no\nthird round. CRCNS data sets carry no version, so the record gives\n`unversioned`. The paper, Robotka, Thomas, Yu, Wood, Elie, Gahr and Theunissen,\n\"Sparse ensemble neural code for a complete vocal repertoire\" (Cell Reports\n42, 112034), records units in the auditory pallium of four freely behaving\nzebra finches (ZF4F, ZF5M, ZF6M, ZF7F) while 110 vocalizations of 10 call\ntypes play, decodes the call type from ensembles of units with a naive Bayes\ndecoder on response strength (Z) and temporal pattern (T), relates ensemble\ndecoding to the volume its modulation receptive fields span in a discriminant\nspace of call types, to selectivity and to neural noise, and compares neural\nclusters with call types and acoustic clusters. The claims were written from\nthe version of record with its supplement and from the paper's code\n(ftheunissen/Ensemble-Code-Cell-Reports-2022 at f2d2376). Reproduced are the\nauditory and inhibited unit counts (287 of 726, 39.5%; 47 of 287), the SNR of\nTable 1, the PC variance (92.4%), the single-unit gain of Z+T over Z (10.68%\nand 12.05%, t(186) = 7.17), the confusions of Figure 4B, the absence of a\nrelation with SI (p = 0.85) and the entropy selectivity slope (p = 0.031); on\nthe code's cross-validation, an assumption, the ensembles of 20 (Z+T 43.15%,\nZ 30.36%) and the top ensembles (48.80%), and with the code's sound window and\ndiscriminant axes as well, the volume (R2adj 0.094) and the multiple\nregression (0.238); on the code's per-call-type response, also an assumption,\nthe peak call types of Figure 3C (Di 53, So 58). The neural noise relation is\npartial (R2adj 0.210 against 0.1), and `good-units-100` is not reproduced: one\nrun gives 89 good units, one below the tolerance, with 87 to 101 over 10 other\nseeds and ZF6M at 8 to 14 against 16 in every run. Blocked are the area\nclaims (no brain area per unit), the acoustic clustering claims (the lab's\nvocalization database is not public), the per-bird and sex test (ZF6M has 10\ngood units, fewer than the 16 it needs) and the aa-4 claims, not analysed in\na run that spent its time on aa-5. The author's first run had `fig5e-volume`\nand `fig5-multiple-regression` partially reproduced. Round 1 disagreed on\nthose two (reproduced on the code's choices) and on `good-units-100`\n(partially reproduced), and found that the code's cross-validation credits\nexemplar-specific responses, that the variant on the paper's listed units and\nthe call-type half of `fig6c-number-of-clusters` had not been run and that the\nstored KDE had not been checked; in reply the two regressions moved to\nreproduced on an assumption, `good-units-100` stayed not reproduced with the\ndisagreement recorded, a synthetic check gave 78.2% under the code's scheme\nagainst 9.8% under the Methods' (chance 10%), and the missing analyses were\nrun. Round 2 agreed with all 30 and found that the KDE_BW finding, that its\nvalues could only be milliseconds, had no printed output behind it, and it\nwas withdrawn. The two questions for a reader in `questions/robotka-2023.yaml`,\non the entropy selectivity reading of C11 and the threshold grid of C12, were\nwritten during the revisions, after the answer and author-answers runs had\nfound no questions file, so they are not answered. The notebook ran in 35.5\nmin at first (16.9 of them streaming the data), with peak memory 4.2 GB, 46.5\nmin after round 1 and 3,281 s at the end, and nothing failed; in the last run\nthe UMAP values moved slightly from round 1 while the Ward values did not,\nwhich the author put down to the machine without confirming it.\n\nNo file gives the brain area (Field L, CLM, CMM, NCM or the L/NCM border) of\na unit, though the paper's analyses by area use one, so the area claims\ncannot be tested; the data descriptor says only that the arrays targeted the\nprimary and secondary auditory pallium. Nine of the 100 good units the\npaper's code lists come from a site folder named\nZF4F_2t_190613_101015.old; the dataset's site ZF4F_2t_190613_101015 holds 18\nunit pickles, none with those names, so the deposited sorting of that site\ndiffers from the one the paper analysed, and the units cannot be matched by\nspike train. The other 91 listed units are in the dataset, and unit counts\nare near the paper's (726 units with vocalization trials against 730, 287\nauditory against 292, 187 with all 110 stimuli against 191). 34 of the 872\nunit pickles hold no stimulus rows (20 of them in site ZF4F_4t_190614_094759,\nwhose tar.gz is 17 KB), and 112 hold song stimuli only, which the data\ndescriptor does not say. Every site tar.gz holds an AppleDouble file\n(`._goodPlayback-...pkl`, 524 bytes) for each unit pickle, 872 in all, and the\npickles are written with pandas 1.x and need pandas' pickle compatibility\nlayer. The descriptor calls spikeKDE the time-varying rate, but its values\nare a 30 ms Gaussian KDE of the spike times scaled by the number of trials\nover 5, so it is not a per-trial rate when a stimulus has more than 5 trials.\nNo recording is deposited twice. In the paper and its code, the Methods hold\nout one exemplar per call type in the decoder's cross-validation while the\ncode holds out one random trial of every stimulus; the two differ by about 11\npoints of PCC for ensembles of 20 (32.0% against 43.2% with Z+T), and only\nthe code's scheme gives the paper's values. The Methods define the\nper-call-type response as the average of the trial z-scores, the code as\nmean(d)/sd(d) within the call type, and under the Methods' definition song,\nnot distress calls, has the highest average response. The Methods compute the\nMPS on the first 500 ms of the stimulus and use the first three discriminant\ndimensions, while the code takes 500 ms before to 500 ms after onset and\nnumpy eigh's first three eigenvectors, the smallest eigenvalues; only the\ncode's choices give the paper's R2adj of about 0.1 for the volume. The 1,746\nensembles of Figure 5 are those of the 1,800 with PCC above 30%, a filter the\nMethods do not state. Two questions are put to the paper's authors: which\ncross-validation scheme produced Figures 4 and 5, and how a count of exactly\n100 good units was obtained when the count moves from 87 to 101 between\nseeds.\n\nThe author's points on the protocol: `archives.md` covers CRCNS zip files\nonly, and this dataset's tar.gz files had to be streamed in full, four sites\nat a time; developing on a subset does not fit a dataset where every claim\nneeds a full pass, so the data were streamed once and a reduced copy kept in\n`$TMPDIR`; the protocol treats a seed as unable to change an outcome, but the\ngood-unit count crosses the tolerance edge with the seed, so it was judged on\nthe first seed with the range over 10 others reported; it is not clear\nwhether one assumption, the cross-validation scheme, may be adopted across\nmany claims, and it was adopted throughout with each outcome marked\n`assumed`; no `blocked_by` value fits public outside data not run for lack of\ntime, and `other` was used for aa-4; the claims file does not name the code's\nlist of good units as an input, so a link claim was added and the repository\nlisted under `inputs`; and the link claim's evidence spans two cells, one of\nthem a data-check cell, where the protocol expects one tagged output.\n"
}
```

```
File created successfully at: docs/pilot-notes/robotka-2023-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "summaries/robotka-2023-01.md",
 "content": "The paper's main decoding findings held up in this data, but only under the methods of the authors' code, whose cross-validation tests trials of exemplars it was trained on and is not the one the Methods describe. Under it, ensembles of 20 units decode call types at 43% (paper 42%), better with the temporal pattern of responses, and decoding rises with the volume the units' receptive fields span and falls with neural variability. Unit counts held, though fewer units passed the good-unit cut. Whether neural clusters follow call types more than acoustic clusters could not be tested, as the vocalization database is not public, nor could brain areas be compared, since no unit's area is recorded. The anesthetized dataset was not analysed.\n"
}
```

```
File created successfully at: summaries/robotka-2023-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  wc -w summaries/robotka-2023-01.md docs/pilot-notes/robotka-2023-01.md; grep -n -i '—\|rather\|\*\*' summaries/robotka-2023-01.md docs/pilot-notes/robotka-2023-01.md; git status --short
```

```
122 summaries/robotka-2023-01.md
1325 docs/pilot-notes/robotka-2023-01.md
1447 total
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
?? docs/pilot-notes/robotka-2023-01.md
?? scripts
?? summaries/robotka-2023-01.md
```

**Agent**

The summary came out at 122 words, over the 120 limit, so I'm cutting it down.

**Agent calls Write**

```json
{
 "file_path": "summaries/robotka-2023-01.md",
 "content": "The paper's main decoding findings held up in this data, but only under the methods of the authors' code, whose cross-validation tests trials of exemplars it was trained on and differs from the Methods. Under it, ensembles of 20 units decode call types at 43% (paper 42%), better with the temporal pattern of responses, and decoding rises with the volume the units' receptive fields span and falls with neural variability. Unit counts held, though fewer units passed the good-unit cut. Whether neural clusters follow call types more than acoustic clusters could not be tested, as the vocalization database is not public, nor could brain areas be compared, since no unit's area is recorded. The anesthetized dataset was not analysed.\n"
}
```

```
The file summaries/robotka-2023-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

I wrote both files and changed nothing else; nothing is committed. Two things to know:

- **Dataset entry:** aa-5 is a CRCNS dataset, so it isn't in `targets/dandisets.json`. Its entry is in `targets/crcns.json`, where `catalystneuro` is empty, so the notes don't open with the CatalystNeuro sentence.
- **Unanswered reader questions:** the two questions in `questions/robotka-2023.yaml` were written during the revisions, after the answer and author-answers runs had found no questions file. They are unanswered, and the notes say so.

**`docs/pilot-notes/robotka-2023-01.md`**

# robotka-2023, Robotka et al. 2023

Thirteen claims reproduced (five on an assumption), one partially, one not reproduced and four blocked, with five more blocked that also use outside data, the acoustic clustering claims; the two link claims, `stimulus-set-link` (reproduced, the paper's 110 stimuli and call-type counts exactly) and `paper-good-units-link` (partially reproduced, 91 of the paper's 100 listed good units), and the four claims on CRCNS aa-4 are counted apart. The first verification round agreed with 27 of the 30 outcomes as they stood and the second with all 30; nothing was proposed after the second, so there was no third round. CRCNS data sets carry no version, so the record gives `unversioned`. The paper, Robotka, Thomas, Yu, Wood, Elie, Gahr and Theunissen, "Sparse ensemble neural code for a complete vocal repertoire" (Cell Reports 42, 112034), records units in the auditory pallium of four freely behaving zebra finches (ZF4F, ZF5M, ZF6M, ZF7F) while 110 vocalizations of 10 call types play, decodes the call type from ensembles of units with a naive Bayes decoder on response strength (Z) and temporal pattern (T), relates ensemble decoding to the volume its modulation receptive fields span in a discriminant space of call types, to selectivity and to neural noise, and compares neural clusters with call types and acoustic clusters. The claims were written from the version of record with its supplement and from the paper's code (ftheunissen/Ensemble-Code-Cell-Reports-2022 at f2d2376). Reproduced are the auditory and inhibited unit counts (287 of 726, 39.5%; 47 of 287), the SNR of Table 1, the PC variance (92.4%), the single-unit gain of Z+T over Z (10.68% and 12.05%, t(186) = 7.17), the confusions of Figure 4B, the absence of a relation with SI (p = 0.85) and the entropy selectivity slope (p = 0.031); on the code's cross-validation, an assumption, the ensembles of 20 (Z+T 43.15%, Z 30.36%) and the top ensembles (48.80%), and with the code's sound window and discriminant axes as well, the volume (R2adj 0.094) and the multiple regression (0.238); on the code's per-call-type response, also an assumption, the peak call types of Figure 3C (Di 53, So 58). The neural noise relation is partial (R2adj 0.210 against 0.1), and `good-units-100` is not reproduced: one run gives 89 good units, one below the tolerance, with 87 to 101 over 10 other seeds and ZF6M at 8 to 14 against 16 in every run. Blocked are the area claims (no brain area per unit), the acoustic clustering claims (the lab's vocalization database is not public), the per-bird and sex test (ZF6M has 10 good units, fewer than the 16 it needs) and the aa-4 claims, not analysed in a run that spent its time on aa-5. The author's first run had `fig5e-volume` and `fig5-multiple-regression` partially reproduced. Round 1 disagreed on those two (reproduced on the code's choices) and on `good-units-100` (partially reproduced), and found that the code's cross-validation credits exemplar-specific responses, that the variant on the paper's listed units and the call-type half of `fig6c-number-of-clusters` had not been run and that the stored KDE had not been checked; in reply the two regressions moved to reproduced on an assumption, `good-units-100` stayed not reproduced with the disagreement recorded, a synthetic check gave 78.2% under the code's scheme against 9.8% under the Methods' (chance 10%), and the missing analyses were run. Round 2 agreed with all 30 and found that the KDE_BW finding, that its values could only be milliseconds, had no printed output behind it, and it was withdrawn. The two questions for a reader in `questions/robotka-2023.yaml`, on the entropy selectivity reading of C11 and the threshold grid of C12, were written during the revisions, after the answer and author-answers runs had found no questions file, so they are not answered. The notebook ran in 35.5 min at first (16.9 of them streaming the data), with peak memory 4.2 GB, 46.5 min after round 1 and 3,281 s at the end, and nothing failed; in the last run the UMAP values moved slightly from round 1 while the Ward values did not, which the author put down to the machine without confirming it.

No file gives the brain area (Field L, CLM, CMM, NCM or the L/NCM border) of a unit, though the paper's analyses by area use one, so the area claims cannot be tested; the data descriptor says only that the arrays targeted the primary and secondary auditory pallium. Nine of the 100 good units the paper's code lists come from a site folder named ZF4F_2t_190613_101015.old; the dataset's site ZF4F_2t_190613_101015 holds 18 unit pickles, none with those names, so the deposited sorting of that site differs from the one the paper analysed, and the units cannot be matched by spike train. The other 91 listed units are in the dataset, and unit counts are near the paper's (726 units with vocalization trials against 730, 287 auditory against 292, 187 with all 110 stimuli against 191). 34 of the 872 unit pickles hold no stimulus rows (20 of them in site ZF4F_4t_190614_094759, whose tar.gz is 17 KB), and 112 hold song stimuli only, which the data descriptor does not say. Every site tar.gz holds an AppleDouble file (`._goodPlayback-...pkl`, 524 bytes) for each unit pickle, 872 in all, and the pickles are written with pandas 1.x and need pandas' pickle compatibility layer. The descriptor calls spikeKDE the time-varying rate, but its values are a 30 ms Gaussian KDE of the spike times scaled by the number of trials over 5, so it is not a per-trial rate when a stimulus has more than 5 trials. No recording is deposited twice. In the paper and its code, the Methods hold out one exemplar per call type in the decoder's cross-validation while the code holds out one random trial of every stimulus; the two differ by about 11 points of PCC for ensembles of 20 (32.0% against 43.2% with Z+T), and only the code's scheme gives the paper's values. The Methods define the per-call-type response as the average of the trial z-scores, the code as mean(d)/sd(d) within the call type, and under the Methods' definition song, not distress calls, has the highest average response. The Methods compute the MPS on the first 500 ms of the stimulus and use the first three discriminant dimensions, while the code takes 500 ms before to 500 ms after onset and numpy eigh's first three eigenvectors, the smallest eigenvalues; only the code's choices give the paper's R2adj of about 0.1 for the volume. The 1,746 ensembles of Figure 5 are those of the 1,800 with PCC above 30%, a filter the Methods do not state. Two questions are put to the paper's authors: which cross-validation scheme produced Figures 4 and 5, and how a count of exactly 100 good units was obtained when the count moves from 87 to 101 between seeds.

The author's points on the protocol: `archives.md` covers CRCNS zip files only, and this dataset's tar.gz files had to be streamed in full, four sites at a time; developing on a subset does not fit a dataset where every claim needs a full pass, so the data were streamed once and a reduced copy kept in `$TMPDIR`; the protocol treats a seed as unable to change an outcome, but the good-unit count crosses the tolerance edge with the seed, so it was judged on the first seed with the range over 10 others reported; it is not clear whether one assumption, the cross-validation scheme, may be adopted across many claims, and it was adopted throughout with each outcome marked `assumed`; no `blocked_by` value fits public outside data not run for lack of time, and `other` was used for aa-4; the claims file does not name the code's list of good units as an input, so a link claim was added and the repository listed under `inputs`; and the link claim's evidence spans two cells, one of them a data-check cell, where the protocol expects one tagged output.

**`summaries/robotka-2023-01.md`**

The paper's main decoding findings held up in this data, but only under the methods of the authors' code, whose cross-validation tests trials of exemplars it was trained on and differs from the Methods. Under it, ensembles of 20 units decode call types at 43% (paper 42%), better with the temporal pattern of responses, and decoding rises with the volume the units' receptive fields span and falls with neural variability. Unit counts held, though fewer units passed the good-unit cut. Whether neural clusters follow call types more than acoustic clusters could not be tested, as the vocalization database is not public, nor could brain areas be compared, since no unit's area is recorded. The anesthetized dataset was not analysed.

## End of run

16 turns, 2 minutes, $1.22 at API prices, result: success.
