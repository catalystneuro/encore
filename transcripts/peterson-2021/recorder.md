# peterson-2021 · recorder · run 45657649041

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; python tools/readme_row.py peterson-2021; ls transcripts/peterson-2021/; ls docs/pilot-notes | grep -i knierim; ls summaries | head
```

```
docs/pilot-notes/amjad-2025-01.md
docs/pilot-notes/andrews-2024-01.md
docs/pilot-notes/armstrong-2026-01.md
docs/pilot-notes/asari-2009-01.md
docs/pilot-notes/asari-2009-02.md
| [000055](https://dandiarchive.org/dandiset/000055) | [Peterson et al. 2021](https://doi.org/10.1523/eneuro.0007-21.2021) | 7 (+6) | 4 (+4) | 1 | 0 (+1) | [`peterson-2021`](entries/peterson-2021) |
attempt-01
author-report.md
author-revise-1-report.md
author-revise-1.md
author-revise-2-report.md
author-revise-2.md
author-revise-3-report.md
author-revise-3.md
author.md
reconcile-report.md
reconcile.md
verifier-1-report.md
verifier-1.md
verifier-2-report.md
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for f in amjad-2025-01 andrews-2024-01 armstrong-2026-01 asari-2009-01 asari-2009-02 knierim-2000-02; do echo "== $f"; cat docs/pilot-notes/$f.md; done; head -30 README.md | grep -n "|" | head -5; cat summaries/asari-2009-02.md summaries/amjad-2025-01.md
```

```
<persisted-output>
Output too large (38.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/6ab281c4-61e1-4a57-b105-6d25b5e94023/tool-results/b3vhhc21m.txt

Preview (first 2KB):
== amjad-2025-01
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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/6ab281c4-61e1-4a57-b105-6d25b5e94023/tool-results/b3vhhc21m.txt"
}
```

```
1	== amjad-2025-01
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
[... 522 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/peterson-2021-02.yaml; ls attempts | grep peterson; ls transcripts/peterson-2021/attempt-01; python -c "
import json;d=json.load(open('targets/dandisets.json'));
items=d if isinstance(d,list) else d.get('dandisets',d)
import sys
for x in (items if isinstance(items,list) else items.values()):
  if '000055' in json.dumps(x)[:300]: print(json.dumps(x,indent=1))
"
```

```
<persisted-output>
Output too large (63.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/6ab281c4-61e1-4a57-b105-6d25b5e94023/tool-results/b435ra4mb.txt

Preview (first 2KB):
schema_version: 3
id: peterson-2021-02
datasets:
- archive: dandi
  id: "000055"
  version: 0.261123.1703
  doi: 10.48324/dandi.000055/0.261123.1703
  relation: primary
paper: doi:10.1523/eneuro.0007-21.2021
date: 2026-11-25
entry: peterson-2021
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat claims/peterson-2021.yaml
```

```
<persisted-output>
Output too large (46.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/6ab281c4-61e1-4a57-b105-6d25b5e94023/tool-results/bffiw4qne.txt

Preview (first 2KB):
# Claims for Peterson, Singh, Wang, Rao & Brunton (2021), eNeuro 8(3), ENEURO.0007-21.2021,
# "Behavioral and Neural Variability of Naturalistic Arm Movements", on dandiset 000055.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read. The version of record as served by Europe PMC (PMC8225404), from
# paper/10.1523-eneuro.0007-21.2021.txt: main text, Materials and Methods, figure legends,
# Tables 1 and 2, the legends of the Extended Data figures, and the review history. No PDF was
# supplied. The Extended Data figures (1-1, 2-1 to 2-4, 3-1, 4-1 to 4-7, 5-1, 6-1, 6-2) are
# EPS downloads and are not in the text; only their legends are. Claims that rest on them are
# taken from their legends and from the Results sentences that cite them. The per-subject
# electrode table (Extended Data Figure 1-1) and the per-subject feature confidence intervals
# (Extended Data Figures 2-3 and 2-4) could not be read.
#
# Code read. github.com/BruntonUWBio/naturalistic_arm_movements_ecog at commit
# 04c6faf2f219586fa834d10c614ef48a694cec55 (17 March 2021), Python 3.6 (MNE 0.19) and MATLAB.
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/peterson-2021; wc -c *report.md; cat author-report.md
```

```
5546 author-report.md
 3854 author-revise-1-report.md
 4355 author-revise-2-report.md
 1473 author-revise-3-report.md
 4374 reconcile-report.md
10442 verifier-1-report.md
 6052 verifier-2-report.md
 3650 verifier-3-report.md
39746 total
The attempt is complete: the entry ran from a clean environment, its checks pass, and the handover package for the verifier is built. I did not verify my own work. I did not come across any earlier attempt on this paper. Besides the paper, the claims file and the dataset, I read only the paper's own code on GitHub (commit 04c6faf) and the Figshare projection matrices it names.

## 1. Outcomes (DANDI:000055, version 0.261123.1703)

| Claim | Outcome |
|---|---|
| subject-days | reproduced |
| roi-projection-link | reproduced |
| cohort | partially reproduced (7 subjects have depth electrodes, the paper says 5) |
| fig2-event-counts | not reproduced (fewest events per subject is 210, against 151 ± 15.1) |
| fig2-features-differ-across-subjects | reproduced |
[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/peterson-2021; for f in verifier-1-report.md author-revise-1-report.md verifier-2-report.md author-revise-2-report.md verifier-3-report.md author-revise-3-report.md reconcile-report.md; do echo "=== $f"; cat $f; done
```

```
<persisted-output>
Output too large (33.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/6ab281c4-61e1-4a57-b105-6d25b5e94023/tool-results/bv2rz1g37.txt

Preview (first 2KB):
=== verifier-1-report.md
**Verifier report, round 1: Peterson et al. 2021 on DANDI:000055 (0.261123.1703)**

The claims file has 25 claims and the notebook tests all 25. My outcomes: 14 reproduced, 9 partially reproduced, 1 not reproduced, 1 blocked. I checked the archive API: the version exists and holds 55 files, 845.87 GB, which matches cell 2. I ran the helper functions on synthetic inputs and they behave as documented: the angle folding, the day-balanced splits, the band statistics, the one-hot design matrix and the Morlet bank (a sine at 11, 76 and 121 Hz peaks at its own frequency, and every wavelet spans ±0.2 s).

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| subject-days | reproduced | Cell 17: subjects 01–12 have exactly the paper's days, 55 subject-days. |
| roi-projection-link | reproduced | Cells 7–8: after the code's row rule, the rows equal the electrodes with positions in all 12 subjects. The largest-weight region is the nearest centroid for 36–55% of electrodes, against a shuffle maximum of 8–14, for every seed. For S03 and S12 the criterion's "rows = electrodes" holds only when electrodes without positions are left out (problem 6). The eight regions with density > 3 match the claims file. |
| cohort | partially_reproduced | Cell 19: six of seven quantities are within tolerance. The dataset has 7 subjects with depth-labelled groups; the paper says 5. |
| fig2-event-counts | not_reproduced | Cell 21: the minimum is 211 (reading a) and 210 (reading b) against 151 ± 15.1. The median is 770.5 under reading a (outside tolerance) and 691 under reading b (inside). |
| fig2-features-differ-across-subjects | reproduced | Cell 23: every p is below 1e-32 under both readings. |
| fig2-reach-shape | partially_repr
[... 2 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/6ab281c4-61e1-4a57-b105-6d25b5e94023/tool-results/bv2rz1g37.txt"
}
```

```
1	=== verifier-1-report.md
2	**Verifier report, round 1: Peterson et al. 2021 on DANDI:000055 (0.261123.1703)**
3	
4	The claims file has 25 claims and the notebook tests all 25. My outcomes: 14 reproduced, 9 partially reproduced, 1 not reproduced, 1 blocked. I checked the archive API: the version exists and holds 55 files, 845.87 GB, which matches cell 2. I ran the helper functions on synthetic inputs and they behave as documented: the angle folding, the day-balanced splits, the band statistics, the one-hot design matrix and the Morlet bank (a sine at 11, 76 and 121 Hz peaks at its own frequency, and every wavelet spans ±0.2 s).
5	
6	### A. Outcomes
7	
8	| Claim | My outcome | Reason |
9	|---|---|---|
10	| subject-days | reproduced | Cell 17: subjects 01–12 have exactly the paper's days, 55 subject-days. |
11	| roi-projection-link | reproduced | Cells 7–8: after the code's row rule, the rows equal the electrodes with positions in all 12 subjects. The largest-weight region is the nearest centroid for 36–55% of electrodes, against a shuffle maximum of 8–14, for every seed. For S03 and S12 the criterion's "rows = electrodes" holds only when electrodes without positions are left out (problem 6). The eight regions with density > 3 match the claims file. |
12	| cohort | partially_reproduced | Cell 19: six of seven quantities are within tolerance. The dataset has 7 subjects with depth-labelled groups; the paper says 5. |
13	| fig2-event-counts | not_reproduced | Cell 21: the minimum is 211 (reading a) and 210 (reading b) against 151 ± 15.1. The median is 770.5 under reading a (outside tolerance) and 691 under reading b (inside). |
14	| fig2-features-differ-across-subjects | reproduced | Cell 23: every p is below 1e-32 under both readings. |
15	| fig2-reach-shape | partially_reproduced | Cell 25: the duration and magnitude parts hold in 12 of 12 subjects and pooled. The angle part holds in 0 of 12: the KDE peaks sit near ±60–75°, outside the 15° window. |
16	| fig2-bimanual
[... 260 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/6ab281c4-61e1-4a57-b105-6d25b5e94023/tool-results/b435ra4mb.txt"
}
```

```
1	schema_version: 3
2	id: peterson-2021-02
3	datasets:
4	- archive: dandi
5	  id: "000055"
6	  version: 0.261123.1703
7	  doi: 10.48324/dandi.000055/0.261123.1703
8	  relation: primary
9	paper: doi:10.1523/eneuro.0007-21.2021
10	date: 2026-11-25
11	entry: peterson-2021
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-18
20	  runner:
[... 881 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/6ab281c4-61e1-4a57-b105-6d25b5e94023/tool-results/b435ra4mb.txt",
 "offset": 902
}
```

```
902	    outcome: partially_reproduced
903	    reason: Agrees with the outcome.
904	    response: No change.
905	  - claim: fig6d-upward-reaches-enhance-pattern
906	    agrees: true
907	    outcome: reproduced
908	    reason: Agrees with the outcome.
909	    response: No change.
910	  - claim: fig6d-angle-and-day-largest-coefficients
911	    agrees: true
912	    outcome: reproduced
913	    reason: Agrees with the outcome.
914	    response: No change.
915	- date: '2026-11-25'
916	  kind: agent
917	  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
918	  reviewed: Round 3. The proposed change of outcome for fig5-recording-day-effects and the analysis
919	    behind it (cells 4, 67, 68, 76 and 77 of the executed notebook of the final revision), with the
920	    paper's Methods, ECoG data processing.
921	  results:
[... 151 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -B3 -A3 "^| Dandiset\|^| \[0" README.md | head -20; sed -n 1,80p tools/readme_row.py; grep -n '"000055"' -A15 targets/dandisets.json | head -30
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
[... 76 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 764,800p targets/dandisets.json; python -c "
import yaml
c=yaml.safe_load(open('claims/peterson-2021.yaml'))
a=yaml.safe_load(open('attempts/peterson-2021-02.yaml'))
o={x['claim']:x['outcome'] for x in a['outcomes']}
for x in c['claims']: print(x['id'], x.get('kind'), x.get('data','dataset'), x.get('figure', x.get('source','')), '|', o.get(x['id']))
print(c['claims'][0].keys())
"
```

```
"papers": [
    {
     "doi": "10.1523/eneuro.0007-21.2021",
     "title": "Behavioral and Neural Variability of Naturalistic Arm Movements",
     "relation": "IsDescribedBy",
     "resource_type": "JournalArticle",
     "preprint": false
    },
    {
     "doi": "10.1016/j.jneumeth.2021.109199",
     "title": "Mining naturalistic human behaviors in long-term video and neural recordings",
     "relation": "IsDescribedBy",
     "resource_type": "JournalArticle",
     "preprint": false
    },
    {
     "doi": "10.1038/s41597-022-01280-y",
     "title": "AJILE12: Long-term naturalistic human intracranial neural recordings and pose",
     "relation": "IsDocumentedBy",
     "resource_type": "JournalArticle",
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -rn "converted by CatalystNeuro" docs/pilot-notes | head; grep -c . claims/peterson-2021.yaml; sed -n 25,60p claims/peterson-2021.yaml; cat summaries/peterson-2021-01.md 2>/dev/null; ls docs/pilot-notes | grep peterson
```

```
docs/pilot-notes/knierim-2000-03.md:56:The dataset was converted by CatalystNeuro
docs/pilot-notes/markowitz-2023-01.md:38:The dandiset was converted by CatalystNeuro (catalystneuro/datta-lab-to-nwb).
docs/pilot-notes/huszar-2022-01.md:45:The dandiset was converted by CatalystNeuro (Garrett Flynn and Cody Baker of
docs/pilot-notes/valero-2022-01.md:44:The dandiset was converted by CatalystNeuro (catalystneuro/buzsaki-lab-to-nwb).
docs/pilot-notes/fujisawa-2008-01.md:33:The dandiset was converted by CatalystNeuro (catalystneuro/buzsaki-lab-to-nwb).
docs/pilot-notes/pagan-2025-01.md:45:The dandiset was converted by CatalystNeuro
docs/pilot-notes/peterson-2021-01.md:73:The dataset was converted by CatalystNeuro (Benjamin Dichter and Micheal Scheid
docs/pilot-notes/mantas-2024-01.md:54:The dataset was converted by CatalystNeuro (catalystneuro/meletis-lab-to-nwb;
docs/pilot-notes/tingley-2018-02.md:64:The dataset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is a
docs/pilot-notes/seiler-2022-01.md:47:The dandiset was converted by CatalystNeuro (catalystneuro/lerner-lab-to-nwb).
685
#
# Spectral method fixed here (Methods, with the code where the Methods are silent). Segments
# of 10 s centred on each movement onset; segments with power below 0 dB or with power at
# 115-125 Hz more than 3 SD above all segments are dropped (Methods), and so are events marked
# false positive (code). Morlet wavelet power at 1 to 121 Hz in 5 Hz steps (1, 6, ..., 121) with
# n_cycles = frequency/4, decimated by 50 (10 Hz time bins at 500 Hz), converted to
# 10*log10 (code). Each event's power has its own mean over -1.5 to -1 s subtracted, per
# electrode and frequency (Methods give the window; code takes the mean). Projection onto
# regions (Methods and code): electrodes in MNI space, right-hemisphere ones mirrored to the
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat docs/pilot-notes/peterson-2021-01.md; sed -n 50,70p docs/pilot-notes/knierim-2000-03.md; head -3 docs/pilot-notes/tingley-2018-02.md
```

```
# 000055, Peterson et al. 2021

Seven claims reproduced (four on an assumption), four partially, one not
reproduced and none blocked; the claims that also use the paper's projection
matrices from electrodes to AAL regions on Figshare (`with_inputs`) are counted
apart, with eight reproduced (six on an assumption), two partially (one on an
assumption) and `fig3-lfb-more-widespread` blocked as methods_underspecified,
and the two link claims, `subject-days` and `roi-projection-link`, are left out,
both reproduced. The first verification round agreed with 19 of the 25 outcomes
as they stood and the second with all 25; nothing was proposed after the
second, so there was no third round. The version is 0.220127.0436, the only
published one, which the paper does not cite. The paper, Peterson, Singh, Wang,
Rao and Brunton in eNeuro (8(3), ENEURO.0007-21.2021), studies contralateral
wrist movements detected from video pose in 12 epilepsy patients with ECoG over
several days of clinical monitoring, describes ten behavioural and
environmental features of these movements, projects movement-related spectral
power onto eight AAL regions, and fits regression models of single-event power
on the features; the dandiset (AJILE12) holds 55 NWB files, one per
subject-day, 845.87 GB in all. The claims were written from the version of
record (PMC8225404) without the PDF, so the Extended Data figures were read
[... 114 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat docs/pilot-notes/tingley-2018-02.md; cat summaries/tingley-2018-02.md
```

```
# tingley-2018 again, Tingley et al. 2018

The second attempt on this paper, made blind to the first (tingley-2018-01),
under pilot-15. Eight claims reproduced, eight partially, thirteen not
reproduced and one blocked on the dandiset, `figs6-reference-frame`, as
`metadata_insufficient`, since nothing marks a maze rotation; the two claims
on data elsewhere, the Allen connectivity analysis of Figure S3 and the
spiking model of Figure 7, are blocked as `other` for lack of time and counted
apart. The attempt pins version 0.261109.2219, the latest published version.
The paper, Tingley and Buzsaki, "Transformation of a Spatial Map across the
Hippocampal-Lateral Septal Circuit" (Neuron 98, 1229-1242.e5), reports that
lateral septum (LS) neurons in rats encode position in the theta phase of
their spikes more than in their rate, while hippocampal place fields carry it
equally in both, and relates this to recording depth in the LS,
hippocampal-LS assemblies, and theta coherence and theta-gamma coupling with
CA1 and CA3. The claims file was written again by a reader who had not seen
the data, from the NIH author manuscript (PMC6605060) with its supplement and
the paper's code (DavidTingley/papers at 9f4cd48, buzcode at e615663), and
holds 32 claims. Reproduced are the LS unit and active-neuron counts (1,696
units in 62 sessions; 829 active against 840), the reliability of the LS phase
[... 87 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i "epilep\|patients\|participants\|pose\b\|video" claims/peterson-2021.yaml | head -15; sed -n 60,100p claims/peterson-2021.yaml
```

```
21:# 3 and 4, 5 and 6. It does not hold the ECoG preprocessing, the pose estimation, the event
76:# Data the paper used. 12 subjects (8 male, 4 female, 29.4 +- 7.9 years) in clinical epilepsy
83:# SD or kurtosis) and video at 30 fps. Measured variables are the pose (DeepLabCut, nine key
90:# The dandiset (AJILE12) describes ECoG at 500 Hz and pose for the same 12 participants over 55
141:    during their clinical epilepsy monitoring. Subjects were (mean ± SD) 29.4 ± 7.9 years old ...
# Methods' 90/10 is the main result and the code's 80/20 a variant. Full-model R2 is the
# coefficient of determination on the test events, averaged over splits. The Delta R2 of a
# feature is the full-model test R2 minus the test R2 of a model refit with that feature
# shuffled (all day columns shuffled together, and all time-of-day columns together, code),
# averaged over splits. Features dropped by forward selection get Delta R2 0 (code). The
# Methods score the shuffled model on the unshuffled withheld data, and the Results say the
# training labels were shuffled. The code shuffles the column in training and test events and
# scores on the shuffled test events. The Methods' version is the main result, the code's a
# variant. Coefficients are averaged over splits. Recording day and time of day are
# summarised by the SD of their one-hot coefficients (Figure 6 legend, code). Figure 6b-d
# show only models with withheld R2 > 0.05 (legend), judged per band; the code selects
# electrodes for both bands by the LFB R2, shown as a variant. The code also fits models at
# electrodes marked bad, and its Figure 6c-d box plots do not drop them (Regression_results_Fig6,
# pos_r2_inds); the Methods and the Figure 1 legend remove bad electrodes from further analysis,
# so good electrodes are the main result and the code's inclusion of bad ones a variant.
[... 26 more lines not kept]
```

**Agent**

Sources read. Writing the notes and summary now.

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/peterson-2021-02.md",
 "content": "# peterson-2021, Peterson et al. 2021, second attempt\n\nThe second attempt on this paper, made blind to the first (peterson-2021-01),\nunder pilot-18. Seven claims reproduced (four on an assumption), four\npartially, one not reproduced and none blocked on the dandiset; the claims that\nalso use the paper's projection matrices from electrodes to AAL regions on\nFigshare (`with_inputs`) are counted apart, with six reproduced and four\npartially, all on an assumption, and `fig3-lfb-more-widespread` blocked as\nmethods_underspecified; the two link claims, `subject-days` and\n`roi-projection-link`, are left out, both reproduced. The first verification\nround agreed with all 25 outcomes. In the first revision the author moved\n`fig5-recording-day-effects` from partially to not reproduced by taking the\nelectrodes good in every file of a subject; the second round agreed with the\nother 24 and left that one undecided, as the choice of electrodes decided it,\nthe author proposed partially reproduced on each file's own flags, whose 4.2 +-\n2.1 removed surface electrodes per subject are closest to the paper's 4.9 +-\n4.9, and a third round reviewed that one claim and agreed (20 of 24 pairs, the\ncriterion's threshold). The attempt pins version 0.261123.1703. The paper,\nPeterson, Singh, Wang, Rao and Brunton in eNeuro (8(3), ENEURO.0007-21.2021),\nstudies contralateral wrist movements detected from video pose in 12 subjects\nwith ECoG during clinical epilepsy monitoring over 3 to 5 days, describes ten\nbehavioural and environmental features of the movements, projects\nmovement-related spectral power onto eight AAL regions, and fits regression\nmodels of single-event power on the features. The claims file, written under\npilot-10 from the version of record (PMC8225404) without the PDF, so the\nExtended Data figures were read only from their legends, and with the paper's\ncode at commit 04c6faf, holds 25 claims. The cohort, the events and features\nof Figure 2, the spectral changes of Figures 3 and 4, the band power of Figure\n5 and Tables 1 and 2 and the regressions of Figure 6 could be tested; whether\nlow-frequency decreases are more spatially widespread could not be judged, as\nthe criterion's two readings disagree (8 against 8 regions, 36.0 against 22.2\nsignificant bins per frequency bin) and the paper gives no measure. Reproduced\nare, among others, the group decrease in low and increase in high frequency\npower, largest in postcentral, precentral and inferior parietal regions, the\ndifferences in band power across subjects, and the regressions, with a largest\nwithheld R2 of 0.177 and recording day and reach angle the most informative\nfeatures in both bands. Partial are `cohort` (seven subjects with depth\nelectrode groups against five), `fig2-reach-shape`, `extfig2-2-feature-correlations`\n(magnitude and duration r = 0.232), `fig2-days-and-waking` (S04's busiest day\nholds 0.400 of its events), `fig4-precentral-subject-variability` (two of four\nparts), `table1-subject-band-power-ci` (18 of 24 inside), the recording-day\neffects and `extfig6-2-angle-most-retained`. Not reproduced is\n`fig2-event-counts` (fewest events 210 or 211, in S09, against 151 +- 15.1).\nThe reconciliation with peterson-2021-01 found that this attempt's helper\n(`ajile.py`, `session_spectral`) reads every ECoG series from 0 s, while this\nversion sets the ECoG starting_time of sub-01 day 7, sub-04 day 3 and sub-06\nday 3 to 29240.566 to 30682.414 s, so their events were read about 8 h late;\nthis gives the day effects of S01 LFB, S01 HFB and S06 HFB where the paper has\nnone, and read from the starting_time 23 of 24 pairs agree. It traces the\nchange of `fig4-precentral-subject-variability` from reproduced to the choice\nof electrode flags, and notes that the same error touches the other ECoG claims\nfor those three files. The author asked a reader nothing at first; after round\n1 three questions went to a reader in `questions/peterson-2021.yaml`, on the\nrow rule of `roi-projection-link`, the 15 degree window of `fig2-reach-shape`\nand the 0.5 to 4 s filter of `fig2-event-counts`, and no claim was changed.\nThe author's run took about 2 h 33 min (05:06 to 07:39 UTC) and the notebook\n36.6 min at first, with peak memory 1.8 GB per worker. In the second revision\na Figshare timeout stopped the first run, after which downloads were retried,\nand the full run was marked failed for taking 63.5 minutes against the\n60-minute limit, most of it in the 3904 regression models; the notebook ran in\n1809 s after round 3.\n\nThe dataset was converted by CatalystNeuro (Benjamin Dichter and Micheal Scheid\nof CatalystNeuro are listed as contributors). The files hold 8088 movement\nevents, 211 to 996 per subject (median 770.5), where the paper analysed 151 to\n947 (median 640), and nothing marks the events the paper used or the false\npositives it removed, so the paper's event set cannot be rebuilt. The record\nsays the ECoG of sub-01 day 7, sub-04 day 3 and sub-06 day 3 ends hours before\nthe day ends, leaving 237 events without neural data; the reconciliation shows\nthat the ECoG of these files starts late, at its starting_time, and runs to\n86400 s. The good flags of the electrodes differ between a subject's files (bad\nin at least one file 3 to 32 per subject, in every file 1 to 17), and nothing\nsays which applies; the surface electrodes this removes are 12.6 +- 8.4 per\nsubject for those bad in any file, 1.2 +- 0.4 for those bad in every file and\n4.2 +- 2.1 for each file's own flags, against the paper's 4.9 +- 4.9. The ECoG\nholds undescribed stretches of NaN samples in 125 events (47 in sub-10), and in\nsub-09 and sub-10 every analysed event has runs of at least 50 ms of exact\nzeros on 1 to 15 good electrodes. The bimanual overlap is described as a\nfraction, but 1708 of 8088 values are above 1 (up to 3.83) and fit seconds; the\npose is labelled meters but holds pixels; the reach angle has no stated\nconvention and is in image coordinates, so upward reaches are negative; and\nthe low_freq_R2 and high_freq_R2 columns of the electrodes table are not\ndescribed. 24 electrodes have no position, the 16 depth electrodes of sub-03\nand 8 of sub-12. One event of sub-08 day 4 is at 40.3 s in ReachEvents and at\n86440.3 s in the reaches table. Electrode groups described as depth are in\nseven subjects, where the paper reports five, and the group descriptions\ndisagree with the data descriptor's Table 2 for sub-11 (18 depth electrodes\nagainst none) and sub-10 (78 and 48 against 86 and 40). The behavioural epochs\nare empty at 4767 of the 8088 event times, and 17 events fall in epochs\nlabelled sleep or blocklist. The subjects and days are the paper's, the\npaper's projection matrices match the electrodes of all 12 subjects, and band\npower at onset differs from that 3 s earlier in 10 of 12 subjects for LFB and 8\nof 12 for HFB, consistent with a shared clock; for sub-09 neither band differs\n(p = 0.84 and 0.87), so its alignment could not be established. Of the 13\nfindings of peterson-2021-01, three are fixed in this version (the ECoG\nstarting_time, session_start_time at midnight UTC, and sex and age, now in\nevery file) and ten are still present. Questions are put to the paper's\nauthors: how segment power is pooled for the 0 dB and 3 SD rejection rules,\nwhich measure makes low-frequency decreases more widespread, and whether bad\nelectrodes were removed per day or per subject.\n\nThe author's points on the protocol: the `roi-projection-link` criterion says\nto drop all-zero rows where the code also drops the first non-zero row, and the\ncode's rule was used as a deviation; the notebook cannot run in about 10\nminutes on about 150 GB of ECoG; running every random step under five seeds is\ntoo costly for 3904 Huber models, so only the full-model R2 of the top models\nwas refit under the extra seeds at first; the clock check did not fit an event\ntable on continuous recordings, so power at onsets was contrasted with\npseudo-onsets 3 s earlier; the `cohort` claim has no partial rule; and it is\nunclear when a small choice of event set makes an outcome rest on an\nassumption, so every spectral and regression outcome was marked assumed.\n"
}
```

```
File created successfully at: docs/pilot-notes/peterson-2021-02.md (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "summaries/peterson-2021-02.md",
 "content": "The paper's main neural findings held up in this data: at movement onset low-frequency power fell and high-frequency power rose, most in sensorimotor regions, power differed across subjects, and reach angle and recording day were the most informative features of single-event power. Day-to-day changes in power matched only in part, likely because this attempt read the neural data of three recordings about 8 h late. Per-subject event counts did not reproduce, as the files hold more events than the paper analysed and mark none as removed. Whether low-frequency decreases are more widespread could not be tested, as the paper gives no measure. Several minor details, such as per-subject band power, matched only in part.\n"
}
```

```
File created successfully at: summaries/peterson-2021-02.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  wc -w summaries/peterson-2021-02.md docs/pilot-notes/peterson-2021-02.md; grep -c "—\|rather" summaries/peterson-2021-02.md docs/pilot-notes/peterson-2021-02.md; git status --short
```

```
114 summaries/peterson-2021-02.md
1344 docs/pilot-notes/peterson-2021-02.md
1458 total
summaries/peterson-2021-02.md:0
docs/pilot-notes/peterson-2021-02.md:0
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
?? docs/pilot-notes/peterson-2021-02.md
?? scripts
?? summaries/peterson-2021-02.md
```

**Agent**

I wrote the two new files, `docs/pilot-notes/peterson-2021-02.md` and `summaries/peterson-2021-02.md`. I changed nothing else and committed nothing. The working tree also has untracked files I did not create (`.bashrc`, `.idea`, `scripts` and others); I left them alone.

The most important point is in the reconciliation: this attempt's own code reads the brain recordings of three files about 8 h late. The record reports that as "ECoG ends hours early", but the data actually start late. That error causes most of the extra recording-day effects. The notes and the summary both say this.

# peterson-2021, Peterson et al. 2021, second attempt

The second attempt on this paper, made blind to the first (peterson-2021-01), under pilot-18. Seven claims reproduced (four on an assumption), four partially, one not reproduced and none blocked on the dandiset; the claims that also use the paper's projection matrices from electrodes to AAL regions on Figshare (`with_inputs`) are counted apart, with six reproduced and four partially, all on an assumption, and `fig3-lfb-more-widespread` blocked as methods_underspecified; the two link claims, `subject-days` and `roi-projection-link`, are left out, both reproduced. The first verification round agreed with all 25 outcomes. In the first revision the author moved `fig5-recording-day-effects` from partially to not reproduced by taking the electrodes good in every file of a subject; the second round agreed with the other 24 and left that one undecided, as the choice of electrodes decided it, the author proposed partially reproduced on each file's own flags, whose 4.2 +- 2.1 removed surface electrodes per subject are closest to the paper's 4.9 +- 4.9, and a third round reviewed that one claim and agreed (20 of 24 pairs, the criterion's threshold). The attempt pins version 0.261123.1703. The paper, Peterson, Singh, Wang, Rao and Brunton in eNeuro (8(3), ENEURO.0007-21.2021), studies contralateral wrist movements detected from video pose in 12 subjects with ECoG during clinical epilepsy monitoring over 3 to 5 days, describes ten behavioural and environmental features of the movements, projects movement-related spectral power onto eight AAL regions, and fits regression models of single-event power on the features. The claims file, written under pilot-10 from the version of record (PMC8225404) without the PDF, so the Extended Data figures were read only from their legends, and with the paper's code at commit 04c6faf, holds 25 claims. The cohort, the events and features of Figure 2, the spectral changes of Figures 3 and 4, the band power of Figure 5 and Tables 1 and 2 and the regressions of Figure 6 could be tested; whether low-frequency decreases are more spatially widespread could not be judged, as the criterion's two readings disagree (8 against 8 regions, 36.0 against 22.2 significant bins per frequency bin) and the paper gives no measure. Reproduced are, among others, the group decrease in low and increase in high frequency power, largest in postcentral, precentral and inferior parietal regions, the differences in band power across subjects, and the regressions, with a largest withheld R2 of 0.177 and recording day and reach angle the most informative features in both bands. Partial are `cohort` (seven subjects with depth electrode groups against five), `fig2-reach-shape`, `extfig2-2-feature-correlations` (magnitude and duration r = 0.232), `fig2-days-and-waking` (S04's busiest day holds 0.400 of its events), `fig4-precentral-subject-variability` (two of four parts), `table1-subject-band-power-ci` (18 of 24 inside), the recording-day effects and `extfig6-2-angle-most-retained`. Not reproduced is `fig2-event-counts` (fewest events 210 or 211, in S09, against 151 +- 15.1). The reconciliation with peterson-2021-01 found that this attempt's helper (`ajile.py`, `session_spectral`) reads every ECoG series from 0 s, while this version sets the ECoG starting_time of sub-01 day 7, sub-04 day 3 and sub-06 day 3 to 29240.566 to 30682.414 s, so their events were read about 8 h late; this gives the day effects of S01 LFB, S01 HFB and S06 HFB where the paper has none, and read from the starting_time 23 of 24 pairs agree. It traces the change of `fig4-precentral-subject-variability` from reproduced to the choice of electrode flags, and notes that the same error touches the other ECoG claims for those three files. The author asked a reader nothing at first; after round 1 three questions went to a reader in `questions/peterson-2021.yaml`, on the row rule of `roi-projection-link`, the 15 degree window of `fig2-reach-shape` and the 0.5 to 4 s filter of `fig2-event-counts`, and no claim was changed. The author's run took about 2 h 33 min (05:06 to 07:39 UTC) and the notebook 36.6 min at first, with peak memory 1.8 GB per worker. In the second revision a Figshare timeout stopped the first run, after which downloads were retried, and the full run was marked failed for taking 63.5 minutes against the 60-minute limit, most of it in the 3904 regression models; the notebook ran in 1809 s after round 3.

The dataset was converted by CatalystNeuro (Benjamin Dichter and Micheal Scheid of CatalystNeuro are listed as contributors). The files hold 8088 movement events, 211 to 996 per subject (median 770.5), where the paper analysed 151 to 947 (median 640), and nothing marks the events the paper used or the false positives it removed, so the paper's event set cannot be rebuilt. The record says the ECoG of sub-01 day 7, sub-04 day 3 and sub-06 day 3 ends hours before the day ends, leaving 237 events without neural data; the reconciliation shows that the ECoG of these files starts late, at its starting_time, and runs to 86400 s. The good flags of the electrodes differ between a subject's files (bad in at least one file 3 to 32 per subject, in every file 1 to 17), and nothing says which applies; the surface electrodes this removes are 12.6 +- 8.4 per subject for those bad in any file, 1.2 +- 0.4 for those bad in every file and 4.2 +- 2.1 for each file's own flags, against the paper's 4.9 +- 4.9. The ECoG holds undescribed stretches of NaN samples in 125 events (47 in sub-10), and in sub-09 and sub-10 every analysed event has runs of at least 50 ms of exact zeros on 1 to 15 good electrodes. The bimanual overlap is described as a fraction, but 1708 of 8088 values are above 1 (up to 3.83) and fit seconds; the pose is labelled meters but holds pixels; the reach angle has no stated convention and is in image coordinates, so upward reaches are negative; and the low_freq_R2 and high_freq_R2 columns of the electrodes table are not described. 24 electrodes have no position, the 16 depth electrodes of sub-03 and 8 of sub-12. One event of sub-08 day 4 is at 40.3 s in ReachEvents and at 86440.3 s in the reaches table. Electrode groups described as depth are in seven subjects, where the paper reports five, and the group descriptions disagree with the data descriptor's Table 2 for sub-11 (18 depth electrodes against none) and sub-10 (78 and 48 against 86 and 40). The behavioural epochs are empty at 4767 of the 8088 event times, and 17 events fall in epochs labelled sleep or blocklist. The subjects and days are the paper's, the paper's projection matrices match the electrodes of all 12 subjects, and band power at onset differs from that 3 s earlier in 10 of 12 subjects for LFB and 8 of 12 for HFB, consistent with a shared clock; for sub-09 neither band differs (p = 0.84 and 0.87), so its alignment could not be established. Of the 13 findings of peterson-2021-01, three are fixed in this version (the ECoG starting_time, session_start_time at midnight UTC, and sex and age, now in every file) and ten are still present. Questions are put to the paper's authors: how segment power is pooled for the 0 dB and 3 SD rejection rules, which measure makes low-frequency decreases more widespread, and whether bad electrodes were removed per day or per subject.

The author's points on the protocol: the `roi-projection-link` criterion says to drop all-zero rows where the code also drops the first non-zero row, and the code's rule was used as a deviation; the notebook cannot run in about 10 minutes on about 150 GB of ECoG; running every random step under five seeds is too costly for 3904 Huber models, so only the full-model R2 of the top models was refit under the extra seeds at first; the clock check did not fit an event table on continuous recordings, so power at onsets was contrasted with pseudo-onsets 3 s earlier; the `cohort` claim has no partial rule; and it is unclear when a small choice of event set makes an outcome rest on an assumption, so every spectral and regression outcome was marked assumed.

---

The paper's main neural findings held up in this data: at movement onset low-frequency power fell and high-frequency power rose, most in sensorimotor regions, power differed across subjects, and reach angle and recording day were the most informative features of single-event power. Day-to-day changes in power matched only in part, likely because this attempt read the neural data of three recordings about 8 h late. Per-subject event counts did not reproduce, as the files hold more events than the paper analysed and mark none as removed. Whether low-frequency decreases are more widespread could not be tested, as the paper gives no measure. Several minor details, such as per-subject band power, matched only in part.

## End of run

20 turns, 2 minutes, $1.26 at API prices, result: success.
