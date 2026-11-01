# 000946 · recorder · run 41260230692

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; ls transcripts/000946/ claims/000946/; python tools/readme_row.py 000946; cat attempts/000946-gao-2025-01.yaml
```

```
<persisted-output>
Output too large (64.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/6082e966-f5d3-4f8f-b852-059d29cf1e59/tool-results/bm6cv4z8x.txt

Preview (first 2KB):
docs/pilot-notes/000773-hart-2024-01.md
docs/pilot-notes/000945-ramachandran-2025-01.md
docs/pilot-notes/000774-hickman-2026-01.md
docs/pilot-notes/000689-li-2022-01.md
docs/pilot-notes/000943-clark-2024-01.md
claims/000946/:
10.1523-jneurosci.2218-24.2025.yaml

transcripts/000946/:
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
author-revise-1.md
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^| Dataset\|^| Dandiset\|^|---" README.md | head; grep -n "outcome:" attempts/000946-gao-2025-01.yaml | sort | uniq -c | head; for f in $(git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5); do echo "=== $f"; cat $f; done; cat docs/pilot-notes/001754-knierim-2000-02.md | head -3
```

```
<persisted-output>
Output too large (42.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/6082e966-f5d3-4f8f-b852-059d29cf1e59/tool-results/bcg7jr79r.txt

Preview (first 2KB):
      1 100:  outcome: blocked
      1 110:  outcome: blocked
      1 122:  outcome: not_reproduced
      1 145:  outcome: blocked
      1 153:  outcome: blocked
      1 161:  outcome: blocked
      1 169:  outcome: blocked
      1 177:  outcome: blocked
      1 185:  outcome: blocked
      1 194:  outcome: blocked
=== docs/pilot-notes/000773-hart-2024-01.md
# 000773, Hart et al. 2024

Two claims reproduced, one partially, none not reproduced and three blocked
on the dataset, with one more reproduced, two more partially, five more not
reproduced and one more blocked that also need outside data. The first
[... 20 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/6082e966-f5d3-4f8f-b852-059d29cf1e59/tool-results/bcg7jr79r.txt"
}
```

```
1	      1 100:  outcome: blocked
2	      1 110:  outcome: blocked
3	      1 122:  outcome: not_reproduced
4	      1 145:  outcome: blocked
5	      1 153:  outcome: blocked
6	      1 161:  outcome: blocked
7	      1 169:  outcome: blocked
8	      1 177:  outcome: blocked
9	      1 185:  outcome: blocked
10	      1 194:  outcome: blocked
11	=== docs/pilot-notes/000773-hart-2024-01.md
12	# 000773, Hart et al. 2024
13	
14	Two claims reproduced, one partially, none not reproduced and three blocked
15	on the dataset, with one more reproduced, two more partially, five more not
16	reproduced and one more blocked that also need outside data. The first
17	verification round agreed with 19 of the 22 outcomes and the second with all
18	22, so there was no third round. It pins version 0.261004.1511, the only
19	published version; the paper cites none. The paper, Hart, Lopes, Frank and
20	Kronauer in Current Biology, counts young and old clonal raider ants leaving
[... 597 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "| Reproduced\|Partial\|Not reproduced" README.md | head -5; sed -n 1,80p tools/readme_row.py; python - <<'E'
import json;d=json.load(open('targets/dandisets.json'))
it = d if isinstance(d,list) else d.get('dandisets', d)
for x in (it if isinstance(it,list) else it.values()):
    if '000946' in json.dumps(x)[:200]: print(json.dumps(x,indent=1))
E
```

```
"""The README's table row for a dataset, from its latest attempt.

    python tools/readme_row.py DATASET            # print the row

Counts are of the paper's findings on the dandiset, including those that name its codes from
elsewhere (`with_labels`); findings that also use outside data (`with_inputs`) are shown in brackets;
findings on data in other archives (`elsewhere`) and the registry's link checks (`kind: link`) are
left out, as the README says. A deprecated attempt's row has no counts.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
[... 58 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -B2 -A12 '"000946"' targets/dandisets.json | head -40; wc -l attempts/000946-gao-2025-01.yaml claims/000946/*.yaml transcripts/000946/*-report.md
```

```
3914-  },
3915-  {
3916:   "dandiset": "000946",
3917-   "name": "Neural Pathways Modulation in the Anesthetized Rat Elicited by Trials of Transcranial Focused Ultrasound Stimulation",
3918-   "published_version": "0.250829.1249",
3919-   "asset_count": 1920,
3920-   "size_gb": 65.16,
3921-   "data_standards": [
3922-    "Neurodata Without Borders (NWB)"
3923-   ],
3924-   "species": [
3925-    "Rattus norvegicus - Norway rat"
3926-   ],
3927-   "approaches": [
3928-    "electrophysiological approach"
   922 attempts/000946-gao-2025-01.yaml
  1079 claims/000946/10.1523-jneurosci.2218-24.2025.yaml
     7 transcripts/000946/answer-report.md
    22 transcripts/000946/author-answers-report.md
    61 transcripts/000946/author-report.md
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 3928,3950p targets/dandisets.json; cd transcripts/000946; for f in author-report.md answer-report.md author-answers-report.md verifier-1-report.md author-revise-1-report.md verifier-2-report.md author-revise-2-report.md; do echo "=== $f"; cat $f; done
```

```
"electrophysiological approach"
   ],
   "papers": [
    {
     "doi": "10.1523/jneurosci.2218-24.2025",
     "title": "Transcranial Focused Ultrasound Modulates Feedforward and Feedback Cortico-Thalamo-Cortical Pathways by Selectively Activating Excitatory Neurons",
     "relation": "IsDescribedBy",
     "resource_type": null,
     "preprint": false,
     "source": "description"
    }
   ],
   "catalystneuro": []
  },
  {
   "dandiset": "000947",
   "name": "Reach-related Single Unit Activity in the Parkinsonian Macaque",
   "published_version": "0.240510.2211",
   "asset_count": 378,
   "size_gb": 1048.82,
[... 262 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/000946-gao-2025-01.yaml"
}
```

```
1	schema_version: 2
2	id: 000946-gao-2025-01
3	dataset:
4	  archive: dandi
5	  id: 000946
6	  version: 0.250829.1249
7	  doi: 10.48324/dandi.000946/0.250829.1249
8	paper: doi:10.1523/jneurosci.2218-24.2025
9	date: '2026-10-31'
10	entry: 000946-gao-2025
11	provenance:
12	  kind: agent
13	  accountable:
14	    name: CatalystNeuro
15	  agent:
16	    harness: Claude Code
17	    model: claude-opus-5-5
18	    protocol: pilot-13
19	  runner:
20	    platform: GitHub Actions
[... 749 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,80p claims/000946/*.yaml; cat transcripts/000946/claims-report.md transcripts/000946/claims-check-report.md
```

```
# Claims for Gao, Ramachandran, Yu & He (2025) on dandiset 000946.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22,
# protocol pilot-10 as stated in docs/protocol.md.
# Source: the version of record (J Neurosci 45(23) e2218242025, PMC12139594), full text as served
# by PMC: Abstract, Introduction, Materials and Methods, Results, figure legends and Discussion.
# The paper has no supplement (no Extended Data is cited). No PDF was supplied. The equation that
# defines the directional spike time tiling coefficient (dSTTC) is missing from the text read; only
# its description in words survives (Methods, Directional spike time tiling coefficient), and the
# symbols in that description are stripped. The paper links no analysis code, so no code was read.
#
# Data the paper used, as it reports them. Male Wistar rats under isoflurane (2%). Group 1 (N = 16):
# two 32-channel NeuroNexus probes, one in S1 (AP -2, ML 2.5, 1 to 1.3 mm deep, layers III to V)
# and one in POm (AP -4.5, ML 2.6, 5.8 mm). Group 2 (N = 12): S1 and auditory cortex (AC, AP -4.5,
# ML 6.5). tFUS from a 128-element array (1.5 MHz) aimed at S1, about 88 kPa in situ. Each session
# is one parameter set: 500 trials, ultrasound duration (UD) 67 ms, intersonication interval 2.5 s
# with 10% jitter, order of conditions randomized. PRFs 30, 300, 1500, 3000, 4500 Hz; duty cycles
# (DC) 0.6, 6, 30, 60, 90%; DC = PRF x pulse duration (PD). The PRF series uses PD 200 us, so 30,
# 300, 1500, 3000 and 4500 Hz are 0.6, 6, 30, 60 and 90% DC. DC series at 3000 Hz and at 30 Hz,
# and a PRF series at 60% DC. Sham sessions have no tFUS; control sessions aim tFUS at cingulate
# cortex (CG1, AP 3, ML 0). The dandiset description says each session's identifier holds the PRF
[... 127 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 770,923p attempts/000946-gao-2025-01.yaml | grep -v "^    reason\|^      \|^    response\|^    agrees\|^    outcome\|^  - claim"; git log --format='%h %s' -- transcripts/000946 | head -20; ls entries/000946-gao-2025 2>/dev/null; grep -n "pinned\|version" transcripts/000946/author-report.md | head
```

```
365f3db6d Agent run on 000946: author-revise-2 (success)
d3a36f4e2 Agent run on 000946: verifier-2 (success)
797a90f93 Agent run on 000946: author-revise-1 (success)
f6b640aa8 Agent run on 000946: verifier-1 (success)
e64dd2bb0 Agent run on 000946: author-answers (success)
60d1977c0 Agent run on 000946: answer (success)
68c31081b Agent run on 000946: author (success)
ae36cfe63 Claims for DANDI:000946, checked
README.md
entry.yaml
reproduce_gao_2025.ipynb
requirements.in
requirements.lock.txt
tfus.py
35:- **Version:** I pinned 0.250829.1249, the latest. The paper cites the dandiset without a version, and all six versions list the same files.
48:4. **Header in the notebook:** the protocol does not name a header field for the reason the version was chosen. I put it in the notebook header.
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/000946-gao-2025-01.md",
 "content": "# 000946, Gao et al. 2025\n\nNo claims reproduced, none partially, two not reproduced and 31 blocked. The\nfirst verification round agreed with 30 of the 33 outcomes and the second with\nall 33, so there was no third round. It pins version 0.250829.1249, the\nlatest; the paper cites the dandiset without a version, and all six versions\nlist the same files. The paper, Gao, Ramachandran, Yu and He in the Journal of\nNeuroscience, records sorted units in isoflurane-anesthetized rats with\n32-channel probes in S1 and POm (16 rats) or in S1 and auditory cortex (AC, 12\nrats) during transcranial focused ultrasound (tFUS) aimed at S1, types the S1\nand POm units as regular spiking (RSU) or fast spiking (FSU) by k-means on the\ninitial phase and afterhyperpolarization of the spike waveform, and relates\ntheir responses and the directional spike time tiling coefficient (dSTTC)\nbetween areas to pulse repetition frequency (PRF), duty cycle and pulse\nduration (PD), with sham and CG1-aimed controls. The claims were written from\nthe version of record in PubMed Central (PMC12139594), which has no\nsupplement, without a PDF, so the dSTTC equation is missing and was\nreconstructed as reading D1; the paper links no code. Only the two unit count\nclaims and `fig11b-ac-responses` were tested: 28 claims are blocked as\n`data_missing` for want of cell types, and `pathway-follows-local-prf` and\n`auditory-confound-low-prf` as depending on blocked claims.\n`fig4-unit-counts` and `fig6-unit-counts` are not reproduced: the k-means puts\nevery unit in one of its two clusters, so RSU + FSU is the number of units\nwith more than 2000 spikes under every typing reading, and POm has 352 units\n(339 without the BH499 POM_S1BF recording) against 250 at 3000 Hz, 315\nagainst 232 at 30 Hz and 1470 (1447) against 1019 over the five PRFs, while\none S1 selection matches at 3000 Hz and another at 30 Hz but none both.\n`fig11b-ac-responses` is blocked as `methods_underspecified`, as the four\nreadings of normalization and baseline sample give different outcomes: N1\nwith B1 is partial, 4500 Hz also being above baseline during sonication\n(108.0 +/- 1.5%), N1 with B2 is not reproduced, 300 Hz also being above\nbaseline (99.7%, corrected p = 6.29e-03), and N2 with either is not\nreproduced (Kruskal-Wallis p = 0.0213 during sonication); with one rat left\nout, N1 with B1 gives anything from reproduced (without BH537) to not\nreproduced (without BH539 or BH547), and 300 Hz has the lowest mean in both\nwindows in all twelve runs. The author's first run gave fig11b as partially\nreproduced on the assumption of N1 with B1 and both count claims as blocked.\nThe author asked a reader no questions, so the answer run and the following\nauthor run changed nothing. Round 1 disagreed with the two count claims,\nwhose printed totals already rule out the reproduced and the partial outcome\nunder any split, and with fig11b, whose readings disagree and so fall under\nthe header's rule; it also found that N2 is biased low (49.8 to 61.7% at trial\nstarts shifted by 1 s, where N1 gives 94.3 to 99.0%), that under N1 the B1\nsample is 100% for every unit, that the Kruskal-Wallis across PRFs mixes PRF\nwith rat, each PRF coming from 3 or 4 of 6 rats, and that the recordings with\nsuffixed identifiers were never checked. In reply the three were changed as\nround 1 gave, the totals were printed by selection, rat and suffix, SEMs and\nthe leave-one-rat-out run were added, and two questions were put to a reader,\non whether N2 and B1 are readings of the paper. Round 2 agreed with all 33 and\nfound sentences the outputs did not support (22 claims in the README where\nthere are 18, the normalization readings said to disagree where N1 with B1\nand N1 with B2 differ only in the baseline sample, the POm totals said to\nexceed the paper's under every selection where leaving out BH511 and BH513\ngives 227, 241 and 1052, a PD range printed only for AC recordings, single\nrecordings of S1BF where there are 3, 60 sessions given as all two-area\nsessions where they are only those checked, and the BH500 and\ndata_collection counts printed nowhere), which were corrected; the totals at\nother spike counts and every pair of POm rats whose removal fits were added,\nand a third question was put to a reader, on the count criteria's \"under one\nreading\" against the header's rule. The author's run finished its steps at\n23:51 UTC, about 1 h 10 min into the window; a first survey of the files with\nthreads took 28 min, as h5py runs one call at a time across threads, and the\nhelper uses processes instead, and one early notebook run failed on a pandas\ntype error, which was fixed. The notebook ran in 258 s at first, 267 s after\nthe answer and 264 s after round 1.\n\nNo file holds spike waveforms or the paper's cell types: the units tables hold\nspike_times and celltype_label only, acquisition, analysis and processing are\nempty in all 1550 unit files, and celltype_label, described as label 1 = RSU,\nlabel 2 = FSU, is 0 in all 1516 files that have it and absent from the other\n34, so 30 of the 33 claims cannot be tested. 734 of the 1550 unit files are\nsecond (or third) copies of another file, with identical spike times and\ntrial starts and the same identifier, under session start times up to 57 s\napart and different file names; 816 distinct recordings remain, and counting\nthe files as they are would double most unit counts. No recording is marked\nas sham or as tFUS aimed at CG1, the controls of Figure 5, and the dataset has\n10 rats with POm recordings and 7 with AC recordings, where the paper reports\n16 and 12, 20 rats in all. Even so it holds more units than the paper: the AC\nrecordings at PD 200 us give 633 units with more than 2000 spikes (112, 89,\n138, 167 and 127 at 30 to 4500 Hz) against Figure 11's 453 (83, about 59, 107,\n104 and 100), and the POm totals exceed the paper's RSU + FSU counts by 36 to\n44% under every selection of recordings by identifier. They come within 10%\nonly if two of the POm rats are left out (9 of the 45 pairs, for example BH511\nand BH513, which nothing marks for exclusion) or if only units with more than\n8000 spikes are counted (242, 230 and 1031), and with more than 4000 spikes\nthe AC count is 445, inside 453 +/- 45.3, so the paper's unit rule or spike\ncounting may differ from more than 2000 spikes over the whole file. The\nseventh AC rat, BH532, has no PD 200 us recording, and the AC_1 and AC_2\nfiles of BH538 are at 1500 Hz and PD 40 us. The dataset also holds recordings\nof M1 and sessions with tFUS aimed at M1 (152 distinct recordings) or at POm\n(65), and a few recordings labelled S1BF (3), VPM (1), S1_R, S1_1, M1_R (1\neach) and AC_1, AC_2 (1 each), none of which the paper describes. In the 60\nsessions at PD 200 us with tFUS at S1 that have files from two of S1, POm and\nAC, both files have identical trial start times but different\nsession_start_time values (median 15.5 min, up to 3964 min apart). The\nrecorded area and the tFUS target are given only in free text in\ngeneral/notes, in two spellings, the electrodes table has location unknown\nand the electrode group location is 'brain area'; five recordings of BH500\nleave the area empty, and general/data_collection, which carries the PRF and\nPD, is empty in 33 recordings (BH494 25, BH499 6, BH500 2), where the\nidentifier gives them and agrees in the 782 recordings that give both. The\narrays of the 370 STTC files have no dimension for the nine dt values their\ndescriptions list (for example 10 x 499 x 20 x 9) and name no units. Firing\nchanges after the trial starts and not when they are shifted by 1 s, so the\ntrial times share the spike clock. A question is put to the paper's authors:\nwhether the normalized rate was the ratio of mean rates over trials or a\nper-trial ratio averaged over trials, and what the baseline sample of the post\nhoc Wilcoxon test was.\n\nThe author's points on the protocol: it does not address a dataset where one\nmissing variable, the cell type, blocks nearly every claim, and each claim was\nblocked as `data_missing` with untyped results shown as variants that decide\nnothing; step 1.6 says to run every reading, but one of the claims file's\nreadings is biased by construction, and it was run, its bias shown against\nshifted trial starts and the other reading adopted as an assumption in the\nfirst run; there is no rule for a dataset holding experiments the paper does\nnot describe, and an `other` finding was recorded; no header field is named\nfor the reason the version was chosen, and it went in the notebook header;\nand untracked files at the repository root (`.bashrc`, `scripts` and others)\nare sandbox device mounts created before the run, which were left alone and\nwhich the workflow should not commit.\n"
}
```

```
File created successfully at: docs/pilot-notes/000946-gao-2025-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  grep -n "—\|rather\|\*\*" docs/pilot-notes/000946-gao-2025-01.md; git status --short
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
?? docs/pilot-notes/000946-gao-2025-01.md
?? scripts
```

**Agent**

I wrote the notes in `docs/pilot-notes/000946-gao-2025-01.md` and changed no other file. Nothing is committed. The other untracked files at the repository root (`.bashrc`, `scripts` and others) were already there before this run; the author's report says they are sandbox mounts. The text is:

# 000946, Gao et al. 2025

No claims reproduced, none partially, two not reproduced and 31 blocked. The first verification round agreed with 30 of the 33 outcomes and the second with all 33, so there was no third round. It pins version 0.250829.1249, the latest; the paper cites the dandiset without a version, and all six versions list the same files. The paper, Gao, Ramachandran, Yu and He in the Journal of Neuroscience, records sorted units in isoflurane-anesthetized rats with 32-channel probes in S1 and POm (16 rats) or in S1 and auditory cortex (AC, 12 rats) during transcranial focused ultrasound (tFUS) aimed at S1, types the S1 and POm units as regular spiking (RSU) or fast spiking (FSU) by k-means on the initial phase and afterhyperpolarization of the spike waveform, and relates their responses and the directional spike time tiling coefficient (dSTTC) between areas to pulse repetition frequency (PRF), duty cycle and pulse duration (PD), with sham and CG1-aimed controls. The claims were written from the version of record in PubMed Central (PMC12139594), which has no supplement, without a PDF, so the dSTTC equation is missing and was reconstructed as reading D1; the paper links no code. Only the two unit count claims and `fig11b-ac-responses` were tested: 28 claims are blocked as `data_missing` for want of cell types, and `pathway-follows-local-prf` and `auditory-confound-low-prf` as depending on blocked claims. `fig4-unit-counts` and `fig6-unit-counts` are not reproduced: the k-means puts every unit in one of its two clusters, so RSU + FSU is the number of units with more than 2000 spikes under every typing reading, and POm has 352 units (339 without the BH499 POM_S1BF recording) against 250 at 3000 Hz, 315 against 232 at 30 Hz and 1470 (1447) against 1019 over the five PRFs, while one S1 selection matches at 3000 Hz and another at 30 Hz but none both. `fig11b-ac-responses` is blocked as `methods_underspecified`, as the four readings of normalization and baseline sample give different outcomes: N1 with B1 is partial, 4500 Hz also being above baseline during sonication (108.0 +/- 1.5%), N1 with B2 is not reproduced, 300 Hz also being above baseline (99.7%, corrected p = 6.29e-03), and N2 with either is not reproduced (Kruskal-Wallis p = 0.0213 during sonication); with one rat left out, N1 with B1 gives anything from reproduced (without BH537) to not reproduced (without BH539 or BH547), and 300 Hz has the lowest mean in both windows in all twelve runs. The author's first run gave fig11b as partially reproduced on the assumption of N1 with B1 and both count claims as blocked. The author asked a reader no questions, so the answer run and the following author run changed nothing. Round 1 disagreed with the two count claims, whose printed totals already rule out the reproduced and the partial outcome under any split, and with fig11b, whose readings disagree and so fall under the header's rule; it also found that N2 is biased low (49.8 to 61.7% at trial starts shifted by 1 s, where N1 gives 94.3 to 99.0%), that under N1 the B1 sample is 100% for every unit, that the Kruskal-Wallis across PRFs mixes PRF with rat, each PRF coming from 3 or 4 of 6 rats, and that the recordings with suffixed identifiers were never checked. In reply the three were changed as round 1 gave, the totals were printed by selection, rat and suffix, SEMs and the leave-one-rat-out run were added, and two questions were put to a reader, on whether N2 and B1 are readings of the paper. Round 2 agreed with all 33 and found sentences the outputs did not support (22 claims in the README where there are 18, the normalization readings said to disagree where N1 with B1 and N1 with B2 differ only in the baseline sample, the POm totals said to exceed the paper's under every selection where leaving out BH511 and BH513 gives 227, 241 and 1052, a PD range printed only for AC recordings, single recordings of S1BF where there are 3, 60 sessions given as all two-area sessions where they are only those checked, and the BH500 and data_collection counts printed nowhere), which were corrected; the totals at other spike counts and every pair of POm rats whose removal fits were added, and a third question was put to a reader, on the count criteria's "under one reading" against the header's rule. The author's run finished its steps at 23:51 UTC, about 1 h 10 min into the window; a first survey of the files with threads took 28 min, as h5py runs one call at a time across threads, and the helper uses processes instead, and one early notebook run failed on a pandas type error, which was fixed. The notebook ran in 258 s at first, 267 s after the answer and 264 s after round 1.

No file holds spike waveforms or the paper's cell types: the units tables hold spike_times and celltype_label only, acquisition, analysis and processing are empty in all 1550 unit files, and celltype_label, described as label 1 = RSU, label 2 = FSU, is 0 in all 1516 files that have it and absent from the other 34, so 30 of the 33 claims cannot be tested. 734 of the 1550 unit files are second (or third) copies of another file, with identical spike times and trial starts and the same identifier, under session start times up to 57 s apart and different file names; 816 distinct recordings remain, and counting the files as they are would double most unit counts. No recording is marked as sham or as tFUS aimed at CG1, the controls of Figure 5, and the dataset has 10 rats with POm recordings and 7 with AC recordings, where the paper reports 16 and 12, 20 rats in all. Even so it holds more units than the paper: the AC recordings at PD 200 us give 633 units with more than 2000 spikes (112, 89, 138, 167 and 127 at 30 to 4500 Hz) against Figure 11's 453 (83, about 59, 107, 104 and 100), and the POm totals exceed the paper's RSU + FSU counts by 36 to 44% under every selection of recordings by identifier. They come within 10% only if two of the POm rats are left out (9 of the 45 pairs, for example BH511 and BH513, which nothing marks for exclusion) or if only units with more than 8000 spikes are counted (242, 230 and 1031), and with more than 4000 spikes the AC count is 445, inside 453 +/- 45.3, so the paper's unit rule or spike counting may differ from more than 2000 spikes over the whole file. The seventh AC rat, BH532, has no PD 200 us recording, and the AC_1 and AC_2 files of BH538 are at 1500 Hz and PD 40 us. The dataset also holds recordings of M1 and sessions with tFUS aimed at M1 (152 distinct recordings) or at POm (65), and a few recordings labelled S1BF (3), VPM (1), S1_R, S1_1, M1_R (1 each) and AC_1, AC_2 (1 each), none of which the paper describes. In the 60 sessions at PD 200 us with tFUS at S1 that have files from two of S1, POm and AC, both files have identical trial start times but different session_start_time values (median 15.5 min, up to 3964 min apart). The recorded area and the tFUS target are given only in free text in general/notes, in two spellings, the electrodes table has location unknown and the electrode group location is 'brain area'; five recordings of BH500 leave the area empty, and general/data_collection, which carries the PRF and PD, is empty in 33 recordings (BH494 25, BH499 6, BH500 2), where the identifier gives them and agrees in the 782 recordings that give both. The arrays of the 370 STTC files have no dimension for the nine dt values their descriptions list (for example 10 x 499 x 20 x 9) and name no units. Firing changes after the trial starts and not when they are shifted by 1 s, so the trial times share the spike clock. A question is put to the paper's authors: whether the normalized rate was the ratio of mean rates over trials or a per-trial ratio averaged over trials, and what the baseline sample of the post hoc Wilcoxon test was.

The author's points on the protocol: it does not address a dataset where one missing variable, the cell type, blocks nearly every claim, and each claim was blocked as `data_missing` with untyped results shown as variants that decide nothing; step 1.6 says to run every reading, but one of the claims file's readings is biased by construction, and it was run, its bias shown against shifted trial starts and the other reading adopted as an assumption in the first run; there is no rule for a dataset holding experiments the paper does not describe, and an `other` finding was recorded; no header field is named for the reason the version was chosen, and it went in the notebook header; and untracked files at the repository root (`.bashrc`, `scripts` and others) are sandbox device mounts created before the run, which were left alone and which the workflow should not commit.

## End of run

12 turns, 2 minutes, result: success.
