# 001751 · recorder · run 41694747003

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; python tools/readme_row.py 001751; ls claims/001751 transcripts/001751; cat attempts/001751-liu-2026-01.yaml
```

```
<persisted-output>
Output too large (70.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/34d9b9b1-b5a1-41d1-8c07-b4f59657261c/tool-results/b69xrlpye.txt

Preview (first 2KB):
docs/pilot-notes/001750-liu-2026-01.md
docs/pilot-notes/001773-fujimoto-2026-01.md
docs/pilot-notes/001683-gao-2026-01.md
docs/pilot-notes/001687-xiao-2026-01.md
docs/pilot-notes/001746-liu-2026-01.md
| [001751](https://dandiarchive.org/dandiset/001751) | [Liu et al. 2026](https://doi.org/10.1038/s41556-026-02009-4) | 2 | 4 | 2 | 1 (+1) | [`001751-liu-2026`](entries/001751-liu-2026) |
claims/001751:
10.1038-s41556-026-02009-4.yaml

transcripts/001751:
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat docs/pilot-notes/001750-liu-2026-01.md docs/pilot-notes/001773-fujimoto-2026-01.md docs/pilot-notes/001683-gao-2026-01.md docs/pilot-notes/001687-xiao-2026-01.md docs/pilot-notes/001746-liu-2026-01.md; wc -c attempts/001751-liu-2026-01.yaml claims/001751/* transcripts/001751/*report.md; python -c "
import json;d=json.load(open('targets/dandisets.json'))
d=d if isinstance(d,list) else d.get('dandisets',d)
for e in (d if isinstance(d,list) else d.values()):
  if '001751' in json.dumps(e): print(json.dumps(e,indent=1))"
```

```
<persisted-output>
Output too large (260.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/34d9b9b1-b5a1-41d1-8c07-b4f59657261c/tool-results/b8ku414jg.txt

Preview (first 2KB):
# 001750, Liu et al. 2026

No claim on the dandiset reproduced: all three are blocked, two as methods
underspecified and one for missing data. Of the 34 claims, one is a link check,
`na-cell-table-link`, partially reproduced, and 30 have their data elsewhere,
in the paper's code repository, MetaboLights, other dandisets, GEO,
NeuroMorpho.org or the model, and are counted apart: three reproduced, one
partially, one not reproduced and 25 blocked. The first verification round
agreed with 32 of the 34 outcomes as they stood and the second with all 34, and
nothing was proposed after the second, so there was no third round. It pins
version 0.260825.0222, the only published version; the paper cites none. The
paper, Liu, Huang, Shen, Shao, Jing et al., "An atlas of primate insular cortex
reveals a signal-processing strategy in von Economo neurons" in Nature Cell
Biology, has its main Patch-seq recordings in DANDI:001746; this dandiset holds only its
outside-out recordings of somatic Na+ currents, 35 patches from one macaque in
two sessions, for the Fig. 4d finding that the currents are lower in von
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -w docs/pilot-notes/001750-liu-2026-01.md docs/pilot-notes/001773-fujimoto-2026-01.md docs/pilot-notes/001683-gao-2026-01.md docs/pilot-notes/001687-xiao-2026-01.md docs/pilot-notes/001746-liu-2026-01.md; wc -c attempts/001751-liu-2026-01.yaml claims/001751/* transcripts/001751/*report.md; python -c "
import json;d=json.load(open('targets/dandisets.json'))
print(type(d), list(d)[:5] if isinstance(d,dict) else d[0].keys())"
```

```
1548 docs/pilot-notes/001750-liu-2026-01.md
 1509 docs/pilot-notes/001773-fujimoto-2026-01.md
 1535 docs/pilot-notes/001683-gao-2026-01.md
 1648 docs/pilot-notes/001687-xiao-2026-01.md
 1479 docs/pilot-notes/001746-liu-2026-01.md
 7719 total
 71634 attempts/001751-liu-2026-01.yaml
 49353 claims/001751/10.1038-s41556-026-02009-4.yaml
   528 transcripts/001751/answer-report.md
  2102 transcripts/001751/author-answers-report.md
  5581 transcripts/001751/author-report.md
  4455 transcripts/001751/author-revise-1-report.md
  2900 transcripts/001751/author-revise-2-report.md
  3153 transcripts/001751/claims-check-report.md
  3935 transcripts/001751/claims-report.md
 11612 transcripts/001751/verifier-1-report.md
  6213 transcripts/001751/verifier-2-report.md
161466 total
<class 'dict'> ['schema_version', 'generated', 'source', 'counts', 'targets']
```

**Agent calls Read**

```json
{
 "file_path": "docs/pilot-notes/001750-liu-2026-01.md"
}
```

```
1	# 001750, Liu et al. 2026
2	
3	No claim on the dandiset reproduced: all three are blocked, two as methods
4	underspecified and one for missing data. Of the 34 claims, one is a link check,
5	`na-cell-table-link`, partially reproduced, and 30 have their data elsewhere,
6	in the paper's code repository, MetaboLights, other dandisets, GEO,
7	NeuroMorpho.org or the model, and are counted apart: three reproduced, one
8	partially, one not reproduced and 25 blocked. The first verification round
9	agreed with 32 of the 34 outcomes as they stood and the second with all 34, and
10	nothing was proposed after the second, so there was no third round. It pins
11	version 0.260825.0222, the only published version; the paper cites none. The
12	paper, Liu, Huang, Shen, Shao, Jing et al., "An atlas of primate insular cortex
13	reveals a signal-processing strategy in von Economo neurons" in Nature Cell
14	Biology, has its main Patch-seq recordings in DANDI:001746; this dandiset holds only its
15	outside-out recordings of somatic Na+ currents, 35 patches from one macaque in
16	two sessions, for the Fig. 4d finding that the currents are lower in von
17	Economo neurons (VENs, n = 14) than in L5 PCs (n = 21). The claims were written
18	from the version of record in Europe PMC (PMC13457102) without a PDF, the
19	Supplementary Information or the Source Data, and from the paper's code
20	(AIC_proj at commit 44cd8a6 and PatchAnaLab 1.0); the check made nine changes,
[... 107 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/pilot-notes/001746-liu-2026-01.md"
}
```

```
1	# 001746, Liu et al. 2026
2	
3	Four claims reproduced, eight partially (one on an assumption), one not
4	reproduced and six blocked, three as methods underspecified and three for
5	missing data; the three claims that also use inputs from outside the dataset
6	(the code's morphology table and AIS distances, the 10x transcriptomes in GEO)
7	are counted apart: one reproduced, one not reproduced and one blocked as
8	methods underspecified. Of the 33 claims, two are link checks, both reproduced,
9	the cell table's on an assumption, and one of them, `morph-table-link`, was
10	added by the author; nine have their data in other dandisets or archives and
11	are blocked as other. The first verification round agreed with 29 of the 33
12	outcomes as they stood and the second with 30, disagreeing on
13	`fig3e-phase-peak-index`, `fig3d-saddle-phase-plane` and
14	`fig4i-peak-index-ais-distance-real`; the author proposed blocking all three,
15	and a third round, which reviewed only these, agreed with all of them. It pins
16	version 0.260825.0222, the only published version; the draft lists the same
17	files, and the paper cites none. The paper, Liu, Huang, Shen, Shao, Jing et
18	al., "An atlas of primate insular cortex reveals a signal-processing strategy
19	in von Economo neurons" in Nature Cell Biology, profiles neurons of the
20	anterior insular cortex (AIC) of macaques with Patch-seq, 462 with intrinsic
[... 104 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;d=json.load(open('targets/dandisets.json'))
t=d['targets']
for e in (t if isinstance(t,list) else t.values()):
  if '001751' in json.dumps(e)[:200]: print(json.dumps(e,indent=1))"
```

```
{
 "dandiset": "001751",
 "name": "Electrophysiological Dataset of Local Neuronal Microcircuits in the Primate Anterior Insular Cortex",
 "published_version": "0.260825.0222",
 "asset_count": 301,
 "size_gb": 6.96,
 "data_standards": [
  "Neurodata Without Borders (NWB)"
 ],
 "species": [
  "Macaca fascicularis - Cynomolgus monkeys"
 ],
 "approaches": [
  "electrophysiological approach"
 ],
 "papers": [
  {
   "doi": "10.1038/s41556-026-02009-4",
   "title": "Cell Atlas and Novel Signal Processing Strategy in Primate Insular Cortex",
   "relation": "IsSourceOf",
[... 6 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/001751-liu-2026-01.yaml"
}
```

```
1	schema_version: 2
2	id: 001751-liu-2026-01
3	dataset:
4	  archive: dandi
5	  id: '001751'
6	  version: 0.260825.0222
7	  doi: 10.48324/dandi.001751/0.260825.0222
8	paper: doi:10.1038/s41556-026-02009-4
9	date: '2026-11-03'
10	entry: 001751-liu-2026
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
[... 762 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/001751-liu-2026-01.yaml",
 "offset": 783,
 "limit": 300
}
```

```
783	    outcome: blocked
784	    reason: 'Blocked (other): data elsewhere; not attempted in this run.'
785	    response: No change of outcome.
786	  - claim: fig4ac-ap-width-amplitude
787	    agrees: true
788	    outcome: blocked
789	    reason: 'Blocked (other): data elsewhere; not attempted in this run.'
790	    response: No change of outcome.
791	  - claim: fig4i-peak-index-ais-distance
792	    agrees: true
793	    outcome: blocked
794	    reason: 'Blocked (other): data elsewhere; not attempted in this run.'
795	    response: No change of outcome.
796	  - claim: fig4g-model-ais-distance-ap-shape
797	    agrees: true
798	    outcome: blocked
799	    reason: 'Blocked (other): data elsewhere; not attempted in this run.'
800	    response: No change of outcome.
801	  - claim: model-ven-fires-more
802	    agrees: true
[... 274 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,80p tools/readme_row.py; grep -n "^| Dandiset\|^| ---" README.md | head; cd transcripts/001751; for f in author-report.md claims-report.md claims-check-report.md answer-report.md author-answers-report.md verifier-1-report.md author-revise-1-report.md verifier-2-report.md author-revise-2-report.md; do echo "=== $f"; cat $f; done
```

```
<persisted-output>
Output too large (42.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/34d9b9b1-b5a1-41d1-8c07-b4f59657261c/tool-results/br288q07f.txt

Preview (first 2KB):
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

[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import yaml
d=yaml.safe_load(open('claims/001751/10.1038-s41556-026-02009-4.yaml'))
print({k:v for k,v in d.items() if k!='claims'})
for c in d['claims']: print(c['id'], c.get('kind'), c.get('data'))
"
```

```
{'schema_version': 2, 'dataset': {'archive': 'dandi', 'id': '001751'}, 'paper': 'doi:10.1038/s41556-026-02009-4', 'checks': [{'date': datetime.date(2026, 10, 21), 'kind': 'agent', 'model': 'claude-opus-5-5', 'ready': True, 'changes': ['Checker. 33 claims, 33 quotes, 8 statistical values, 0 problems before this check; rerun after the changes below.', 'The Fig. 5d-i claims (this dataset) were checked against the Results paragraph, the Fig. 5 legend and the Methods on multi-patch recording; counts, rates, distances, the sum 24 + 1 + 2 + 4 = 31 and the reference 50 (Seeman et al. 2018) agree with the paper. The code details of the opening comment (metadata_multiPatch.xlsx tallies, Fig5fg_plotConn.m) could not be checked here, as the code was not opened in this check.', 'fig5-pair-distances. The quote lacked the sentences that give the PC-IN and VEN-IN distances the statement and expected values use; added them.', 'fig5fg-example-slice. The statement gave the types of all six cells, which come from the code, not the paper (the legend types only cells 2, 4 and 6); moved them to the criterion with their source.', "fig5c-psc-amplitude. The criterion said per-cell mean amplitude; the paper does not say how a cell's events are summarized. Named mean and median as readings.", 'fig4ac-ap-width-amplitude. One statistics entry stood for two tests (the legend gives P < 0.001 for both amplitude and width); split into two.', 'fig4i-peak-index-ais-distance. Noted that F(1, 93) = 1.07 gives p of about 0.30, matching neither printed P, so the term it belongs to is open.', "fig4g-model-ais-distance-ap-shape. Added the Extended Data Fig. 7b slope tests as statistics, and noted that the PC model's AP also widens slightly (p = 0.0013), so only amplitude separates the models.", "fig4j-eepsp-latency and fig4j-eepsp-amplitude. Added the Methods' selection of monosynaptic eEPSPs (monotonic amplitude with current, constant latency, polysynaptic and AP-evoking responses excluded), which the crit
[... 35 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/34d9b9b1-b5a1-41d1-8c07-b4f59657261c/tool-results/br288q07f.txt",
 "offset": 100
}
```

```
100	| fig3c-ais-distance-length, patchseq-mapping | elsewhere | blocked: metadata insufficient |
101	| fig4j-eepsp-latency | elsewhere | blocked: other (the table has no latencies) |
102	| ven-firing-rate-variability | elsewhere | blocked: methods underspecified (its own criterion) |
103	| 11 others (sequencing reads, morphology, NEURON models, DANDI:001746) | elsewhere | blocked: other, not attempted |
104	
105	**2. The dataset, assumptions and questions**
106	- **Version:** I pinned 0.260825.0222, the only published version; it has the same content as the draft.
107	- **Metadata errors:**
108	  - Responses are stated at 1 Hz; the data are at 25 kHz.
109	  - The stimulus rate unit is "millisecond".
110	  - The stimulus amplitude is stored as 2 "amperes"; the Methods say 2 nA.
111	  - Every file names Elec_8 as the stimulated electrode, but the cell that actually fires is on channel 8 in only 35 of 301 files.
112	  - Every file has the same placeholder start time, 2018-01-01.
113	- **Repeated recordings:** none found.
114	- **Code table against the files:**
115	  - 13 dandiset files are not in the table.
116	  - 6 pairs are listed twice and 7 cells have two different types.
117	  - 2 connections have projection labels that don't match their channels, and the stated connection count disagrees with the annotations in 4 of 52 slices.
118	- **Sweeps:** only 119 of 301 files have more than the 20 sweeps the Methods require.
119	- **Other code tables differ in size from the paper:** 23 eEPSP pairs (paper 26), 558 metabolites (581), 120 and 500 AIS values (108 and 430), 14 and 15 VEN subtypes (10 and 11).
[... 306 more lines not kept]
```

**Agent**

Now the start of the author report and the other three notes for shape.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/34d9b9b1-b5a1-41d1-8c07-b4f59657261c/tool-results/br288q07f.txt",
 "offset": 80,
 "limit": 20
}
```

```
80	I tested 13 of the 35 claims on this dataset (including one I added) and blocked the other two; 21 claims on other archives' data were tested or blocked. The entry passes `entry.py all` with 0 errors (the notebook runs in about 3 minutes), and the handover package is built in `executed/001751-liu-2026/handover/`. The dataset alone can't test Fig. 5: its files have no cell types, connection labels or soma positions. Those come from a table in the paper's code (`metadata_multiPatch.xlsx`, AIC_proj at commit 44cd8a6), and that table's counts disagree with the paper's.
81	
82	**1. Outcomes**
83	
84	| Claim | Data | Outcome |
85	|---|---|---|
86	| code-table-link (added by me) | dataset + code's labels | reproduced |
87	| fig5d-connectivity-totals | same | not reproduced (26 connections against 31; 295 cells against 377; 1,416 pairs, within tolerance) |
88	| fig5-pc-to-pc | same | not reproduced (18 of 743 against 24 of 503) |
89	| fig5-ven-outputs-absent | same | not reproduced (the table marks one VEN-to-PC connection, with a 1 mV response in the data) |
90	| fig5-pc-to-ven | same | partially reproduced (1 connection as stated, but 145 pairs against 200) |
91	| fig5-pc-in | same | partially reproduced (2 and 4 connections as stated, but 84 and 86 pairs against 65) |
92	| fig5-in-to-ven-absent | same | reproduced |
93	| fig5i-ven-sparse-local-connectivity | same | partially reproduced (every VEN rate is lower, but no rate is within tolerance) |
94	| fig5fg-example-slice | same | reproduced |
95	| fig5-pair-distances | same | blocked: data missing |
96	| fig5-pc-rate-comparable-primate | with outside inputs | blocked: methods underspecified (its own criterion says so) |
97	| fig5b-psc-frequency, fig5c-psc-amplitude, fig3e-phase-peak-index, fig4j-eepsp-amplitude, ven-map-et-ct | elsewhere | reproduced |
98	| fig4d-sodium-current | elsewhere (DANDI:001750) | reproduced, resting on an assumption |
99	| fig8a-metabolite-gradient, fig8de-glycolytic-bias, fig6f-g-ven-subtyp
[... 1 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/pilot-notes/001773-fujimoto-2026-01.md"
}
```

```
1	# 001773, Fujimoto et al. 2026
2	
3	Twenty-seven claims reproduced (11 on an assumption), none partially, one not
4	reproduced and four blocked, two as methods underspecified and two for missing
5	data. All 32 claims are on the dandiset. The first verification round agreed
6	with all 32 outcomes as they stood and so did the second, and nothing was
7	proposed after the second, so there was no third round. It pins version
8	0.260416.1939, the version the paper cites; the latest version, 0.260615.1838,
9	has identical asset ids. The paper, Fujimoto, Fujimoto, Elorette et al., "Deep
10	brain stimulation induces white matter remodeling and functional changes to
11	brain-wide networks" in Nature Neuroscience, implants an SCC-DBS lead in
12	monkeys N and T, stimulated for 6 weeks, and in monkey D, never stimulated, with
13	nonsurgical controls B, W and H, and reports home-cage behaviour (Extended Data
14	Fig. 1), FA of the white matter tracts (Fig. 2, Extended Data Fig. 2),
15	CC1-positive oligodendrocytes and EM g-ratios (Fig. 3, Extended Data Figs. 5
16	and 6), the whole-brain connectome (Fig. 4), seed connectivity of area 25 by
17	ROI and network (Fig. 5, Extended Data Figs. 7 and 9) and the same measures in
18	monkey D (Fig. 6, Extended Data Fig. 10). The claims were written from the
19	version of record in Europe PMC (PMC13337501) and the Supplementary
20	Information, without a PDF of the main article or the Source Data; the paper's
[... 107 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -c 6000 claims/001751/10.1038-s41556-026-02009-4.yaml; sed -n 1,79p /home/runner/.claude/projects/-home-runner-work-encore-encore/34d9b9b1-b5a1-41d1-8c07-b4f59657261c/tool-results/br288q07f.txt | grep -v "^\s*$" | tail -5
```

```
# Claims for Liu, Huang, Shen, Shao, Jing et al. (2026), "An atlas of primate insular cortex
# reveals a signal-processing strategy in von Economo neurons", Nature Cell Biology 28,
# 1742-1757, doi:10.1038/s41556-026-02009-4 (named on the archive "Cell Atlas and Novel Signal
# Processing Strategy in Primate Insular Cortex"), on dandiset 001751.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21,
# protocol as stated in docs/protocol.md (version pilot-10).
#
# Text read: the version of record, open access, as served by Europe PMC (PMC13457102), stored
# under paper/: main text, figure legends, Extended Data figure legends, Methods, Data and Code
# availability. No PDF was available, so values printed only inside figures could not be read.
# The Supplementary Information (Supplementary Figs. 1 to 17, Supplementary Tables 1 to 12) and
# the Source Data files were not in the text read. Supplementary Table 5 ("Number of neurons and
# tested neuron pairs of potential connectivities") bears on the claims this dataset can test,
# but every count those claims rest on is printed in the Results and the Fig. 5 legend, which
# were read; claims that cite other supplementary items rest on the main text and say so.
#
# Code read: github.com/RFLiu2021/AIC_proj at commit 44cd8a6dfbb1f1ce363d73742e4f3652086b0f9d
# (2026-07-05), and PatchAnaLab 1.0 (Zenodo doi:10.5281/zenodo.19995355), the paper's analysis
# package. AIC_proj holds MATLAB and Python scripts per figure (file names follow an older figure
# numbering) and small data tables; its processed data are in Zenodo doi:10.5281/zenodo.18814764
[... 58 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/001751-liu-2026-01.md",
 "content": "# 001751, Liu et al. 2026\n\nTwo claims reproduced, four partially, two not reproduced and one blocked for\nmissing data; the one claim that also uses inputs from outside the dataset,\n`fig5-pc-rate-comparable-primate`, is counted apart and blocked as methods\nunderspecified, by its own criterion. Of the 35 claims, one is a link check,\n`code-table-link`, added by the author and reproduced, and 24 have their data\nelsewhere, in the paper's code repository, other dandisets, GEO, MetaboLights,\nNeuroMorpho.org or the model, and are counted apart: six reproduced (two on an\nassumption), three partially and 15 blocked. The first verification round\nagreed with 31 of the 35 outcomes as they stood and the second with 34,\ndisagreeing on `patchseq-mapping`, which was kept blocked with the disagreement\nrecorded, and nothing was proposed after the second, so there was no third\nround. It pins version 0.260825.0222, the only published version, with the\nsame file count and bytes as the draft; the paper cites none. The paper, Liu,\nHuang, Shen, Shao, Jing et al., \"An atlas of primate insular cortex reveals a\nsignal-processing strategy in von Economo neurons\" in Nature Cell Biology, has\nits Patch-seq, Na+ current and postsynaptic current recordings in DANDI:001746,\n001750 and 001752; this dandiset holds the multi-patch recordings of Fig. 5d-i,\n301 files of up to eight layer 5b neurons, for the finding that von Economo\nneurons (VENs) are sparsely connected in the local circuit (377 neurons, 1,292\npairs and 31 connections in the paper). The claims were written from the\nversion of record in Europe PMC (PMC13457102) without a PDF, the Supplementary\nInformation or the Source Data, and from the paper's code (AIC_proj at commit\n44cd8a6 and PatchAnaLab 1.0); the check made thirteen changes, one of them a\nnew claim, and left four points open. Every Fig. 5 claim rests on the cell\ntypes and connection annotations of the code's table metadata_multiPatch.xlsx,\nreading (b) of the criteria, as the files carry none. Reproduced are\n`fig5-in-to-ven-absent` (0 of 54 pairs, against 55 +/- 5.5) and\n`fig5fg-example-slice`. Not reproduced are `fig5d-connectivity-totals` (26\nannotated connections against 31 +/- 3.1, with 1,403 pairs within 1,292 +/-\n129, 298 cells in the table outside 377 +/- 38 and 410 channels holding a cell\nin the files) and `fig5-pc-to-pc` (18 of 743, 2.42%, against 24 of 503,\n4.77%). Partial are `fig5-ven-outputs-absent` (0 of 59 VEN-to-VEN and 0 of 54\nVEN-to-IN, but one VEN-to-PC connection in 146 pairs), `fig5-pc-to-ven` (1\nconnection as in the paper, in 139 pairs against 200 +/- 20), `fig5-pc-in` (2\nand 4 connections, in 83 and 86 pairs against 65 +/- 6.5) and\n`fig5i-ven-sparse-local-connectivity` (every VEN rate is below the PC rate of\nthe same partner class, but none of the four rates, 2.42, 2.41, 0.72 and\n4.65%, is within tolerance of 4.77, 3.08, 0.5 and 6.15%, and the Fisher\nvariants give p = 0.159 to 0.636). `fig5-pair-distances` is blocked as no file\nholds a soma position. Of the claims on other data, `fig5b-psc-frequency` (p =\n0.0068, 0.0093, 0.0281 and 0.0102), `fig5c-psc-amplitude` (none below 0.05),\n`fig3e-phase-peak-index` (VEN median 0.116, Kruskal-Wallis p = 6.5e-08),\n`ven-map-et-ct` (14 and 15) and, on an assumption, `fig4j-eepsp-amplitude`\n(cell type p = 0.0056 and 0.0065 against the paper's 0.0034, on 23 pairs\nagainst 26) are reproduced on the per-cell tables in the code repository, and\n`fig4d-sodium-current` is reproduced on the 35 files of DANDI:001750 on the\nassumption of a 1 kHz low-pass (VEN median -17.3 against PC -31.5 pA, p =\n0.0010, r = 0.99 with the code's max_Na_current). `fig8a-metabolite-gradient`\n(179 and 85, with AIC-V1 below 228 +/- 23 under every reading),\n`fig8de-glycolytic-bias` (2-ketobutyric acid 0.59, p = 0.18) and\n`fig6f-g-ven-subtype-mapping` (14 and 15 against 10 +/- 1 and 11 +/- 1.1) are\npartial. `fig3c-ais-distance-length` and `patchseq-mapping` are blocked as\nmetadata insufficient, `fig4j-eepsp-latency` as other, as its table holds no\nlatencies, `ven-firing-rate-variability` as methods underspecified, and 11\nclaims on sequencing reads, morphologies, the NEURON models and DANDI:001746 as\nother, not attempted in this run. The author's first run gave the same outcomes\nexcept that `fig5-ven-outputs-absent` was not reproduced. The author asked no\nquestions of a reader, so the answer and author-answers runs changed nothing.\nRound 1 disagreed on `fig5-ven-outputs-absent`, which it gave partially\nreproduced and which was changed, on `fig4d-sodium-current` (partially), on\n`fig8a-metabolite-gradient` (not reproduced) and on `patchseq-mapping`\n(partially), and found that filling the table down put 39 rows under the wrong\nfile, that the presynaptic rule added a -30 mV condition the criterion lacks,\nthat \"no positions\" was printed as a fixed string, that the Na+ peaks agreed\nwith the code's values at only r = 0.40 to 0.90, that fig8a used the code's 558\nmetabolites, not the MetaboLights deposit, and that the response measure picks\nup pulse-locked artefacts; in reply the table was filled within each\npresynaptic block, 8 of the 10 blocks without a file name were matched by the\nfiring channel, the rule followed the criterion with -30 mV as a variant, every\ngroup and electrode field of the 301 files was printed, 40 readings of the Na+\npeak were run and the 1 kHz low-pass adopted, the metabolite claims were tested\non the deposit pinned by sha256, peaks on the first sample of the window were\nflagged, `fig4d` and `fig8a` were kept and `patchseq-mapping` kept blocked with\nthe disagreements recorded, and a question on Supplementary Table 5 was filed\nin `questions/001751.yaml`, after the reader's run. Round 2 agreed with 34 and\nfound sentences the outputs did not support (296 of 296 files where the table\nnames 288, a stale 281 of 288 in a finding, r = 0.99 holding only for steps up\nto 0 mV, \"the only published version\" and \"the only revision\", the code's use\nof filter_1000Lowpass and the README's run time); in reply these were printed\nor corrected, and the PDFs under `paper/` were rendered with PyMuPDF, none of\nthem holding Supplementary Table 5. The author's run took about 1 h 50 min\n(13:41 to about 15:30 UTC); during development a clash between a column name\nand a pingouin method and a header-row offset in the AIS table were fixed, and\nin the round 2 revision ftp.ebi.ac.uk refused connections on the first re-run,\nso a retry was added to the MetaboLights download. The notebook ran in about 3\nminutes at first, 165 s after the author-answers run, 209 s after round 1 and\n304 s at the end. Untracked dotfiles and a `scripts` entry, a character device,\nwere left alone.\n\nThe files carry no cell type, no connection label and no soma position, so none\nof the Fig. 5 counts can be made from the dandiset alone; types and connections\nexist only in the code's table metadata_multiPatch.xlsx, which links to the\nfiles by name, and neither the paper nor its code gives a rule for calling a\nconnection. The table disagrees with the paper: it lists 298 cells, 1,416\nordered pairs (1,403 in files of the dandiset) and 26 connections, where the\npaper reports 377 neurons, 1,292 pairs and 31 connections, PC-to-PC 18 of 743\nagainst 24 of 503, one VEN-to-PC connection (190315s2, channel 4 to 6,\nExcellent, with a 1 mV response in the data) where the paper reports none, and\npair counts that differ from the paper's by more than 10% in 6 of 8 classes. It\nis also inconsistent with itself and with the files: ten of its presynaptic\nblocks name no NWB file (8 match a file by the firing channel; 190315s2 channel\n7 and 20241014HS2 channel 8, 13 rows, match none), it gives 5 cells two types,\nlabels 2 connections with a projection that names another postsynaptic channel,\nits Nr_Conn disagrees with its annotations in 4 of 53 slices, six of its pairs\nname channels that read 0 mV (slice 190314s1, channels 6 and 7), eight of its\nInh connections come from a PC and 6 of its 12 Inh connections have a positive\naveraged response; 5 files of slice 20240912HS2 are not in it. Annotated\nconnections have a median peak to baseline s.d. ratio of 8.7 against 2.8 for\nother pairs, while 333 of 1,377 pairs not annotated exceed 5. Every response\nseries states a rate of 1 Hz where the data are sampled at 25 kHz, and the\nstimulus series gives its rate of 25,000 with the unit millisecond; the\nstimulus amplitude is stored as 2 (2.5 or 3 in 14 files) with the unit amperes\nwhere the Methods inject 2 nA; every file names electrode Elec_8 as the\nstimulated one, while the cell that fires is on channel 8 in only 35 of 301\nfiles and is the table's presynaptic channel in 286 of the 288 files it names;\nand all 301 files have the session start 2018-01-01T01:00+08:00 although the\nslices are named for dates in 2019 and 2024, with every subject of age\nP4Y/P6Y and sex M. The Methods average over more than 20 sweeps, and 119 of 301\nfiles hold more than 20 (median 20, range 1 to 30). Of the other data,\nsumData_StimWM.xlsx holds 23 VEN-PC pairs where the paper states 26,\nAIScmp_PCvsVEN_Fig5c.xlsx 120 VENs and 500 PCs against 108 and 430, with no\nslice or animal for the legend's two-way ANOVA, the Patch-seq mapping results\n14 VEN-L and 15 VEN-S against 10 and 11 and 17 excitatory clusters against 18,\nwith the inhibitory mapping not saved, and PeakIdx_Fig5e.xlsx 32 VENs against\nthe legend's 22. The MetaboLights deposit MTBLS13927 holds 558 identified\nmetabolites where the paper quantifies 581, the same as the code's\nMetabolic_data.xlsx, which swaps the labels of two V1 samples; the deposit\nnames the first AIC sample A1C-1-Q and stores the run mode in its charge\ncolumn. For the Na+ currents, unfiltered peaks separate VENs from PCs up to 3\nms after the step (p = 0.0074) and not up to 5 or 10 ms (p = 0.077 and 0.067),\nwhile after a 1 kHz low-pass they match the code's values (r = 0.99). Questions\nare put to the paper's authors: whether connections were called by eye on\naveraged traces, with which criteria for Excellent, Good and OK quality,\nwhether the 31 connections include the OK ones and which pairs and cells make\nup the 1,292 pairs and 377 neurons; and which filter and window gave\nmax_Na_current.\n\nThe author's points on the protocol: it does not say whether marking claims\n`data: with_labels` and adding `depends_on` counts as changing the claims\nfile, and both were done with statements, expected values and criteria\nunchanged; connection annotations are expert judgements, yet had to be counted\nas `with_labels`, so it was recorded that they decide the outcome; claims on\ndata elsewhere not tried for lack of scope have no fitting block reason, so\n`other` was used with a note on each; some such claims name a raw archive while\nthe paper's code holds per-cell tables of the same data, which were used and\nrecorded as a deviation; there is no rule for a claim only partly testable, so\n`patchseq-mapping` was blocked with the excitatory numbers in its notes; and it\nis not clear when unmatched denominators make an outcome partial, so partial\nwas used where the connection counts matched and only the pair counts were\noff.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  wc -w docs/pilot-notes/001751-liu-2026-01.md; grep -c "—\|rather" docs/pilot-notes/001751-liu-2026-01.md; git status --short
```

```
1853 docs/pilot-notes/001751-liu-2026-01.md
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
?? docs/pilot-notes/001751-liu-2026-01.md
?? scripts
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/001751-liu-2026-01.md",
 "old_string": "averaged response; 5 files of slice 20240912HS2 are not in it. Annotated\nconnections have a median peak to baseline s.d. ratio of 8.7 against 2.8 for\nother pairs, while 333 of 1,377 pairs not annotated exceed 5. Every response",
 "new_string": "averaged response; 5 files of slice 20240912HS2 are not in it. Every response"
}
```

```
The file docs/pilot-notes/001751-liu-2026-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/001751-liu-2026-01.md",
 "old_string": "column. For the Na+ currents, unfiltered peaks separate VENs from PCs up to 3\nms after the step (p = 0.0074) and not up to 5 or 10 ms (p = 0.077 and 0.067),\nwhile after a 1 kHz low-pass they match the code's values (r = 0.99). Questions",
 "new_string": "column. Questions"
}
```

```
The file docs/pilot-notes/001751-liu-2026-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/001751-liu-2026-01.md",
 "old_string": "presynaptic block, 8 of the 10 blocks without a file name were matched by the\nfiring channel, the rule followed the criterion with -30 mV as a variant, every\ngroup and electrode field of the 301 files was printed, 40 readings of the Na+\npeak were run and the 1 kHz low-pass adopted, the metabolite claims were tested\non the deposit pinned by sha256, peaks on the first sample of the window were\nflagged, `fig4d` and `fig8a` were kept and `patchseq-mapping` kept blocked with\nthe disagreements recorded, and a question on Supplementary Table 5 was filed",
 "new_string": "presynaptic block, the rule followed the criterion, every group and electrode\nfield of the 301 files was printed, 40 readings of the Na+ peak were run and\nthe 1 kHz low-pass adopted, the metabolite claims were tested on the deposit,\npeaks on the first sample of the window were flagged, the other three outcomes\nwere kept with the disagreements recorded, and a question on Supplementary\nTable 5 was filed"
}
```

```
The file docs/pilot-notes/001751-liu-2026-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/001751-liu-2026-01.md",
 "old_string": "`patchseq-mapping` (partially), and found that filling the table down put 39 rows under the wrong",
 "new_string": "`patchseq-mapping` (partially), and found that filling the table down put 39 rows under the wrong"
}
```

```
<tool_use_error>No changes to make: old_string and new_string are exactly the same.</tool_use_error>
```

**Agent calls Bash**

```bash
cd  wc -w docs/pilot-notes/001751-liu-2026-01.md; cat docs/pilot-notes/001751-liu-2026-01.md
```

```
1753 docs/pilot-notes/001751-liu-2026-01.md
# 001751, Liu et al. 2026

Two claims reproduced, four partially, two not reproduced and one blocked for
missing data; the one claim that also uses inputs from outside the dataset,
`fig5-pc-rate-comparable-primate`, is counted apart and blocked as methods
underspecified, by its own criterion. Of the 35 claims, one is a link check,
`code-table-link`, added by the author and reproduced, and 24 have their data
elsewhere, in the paper's code repository, other dandisets, GEO, MetaboLights,
NeuroMorpho.org or the model, and are counted apart: six reproduced (two on an
assumption), three partially and 15 blocked. The first verification round
agreed with 31 of the 35 outcomes as they stood and the second with 34,
disagreeing on `patchseq-mapping`, which was kept blocked with the disagreement
recorded, and nothing was proposed after the second, so there was no third
round. It pins version 0.260825.0222, the only published version, with the
same file count and bytes as the draft; the paper cites none. The paper, Liu,
Huang, Shen, Shao, Jing et al., "An atlas of primate insular cortex reveals a
signal-processing strategy in von Economo neurons" in Nature Cell Biology, has
its Patch-seq, Na+ current and postsynaptic current recordings in DANDI:001746,
001750 and 001752; this dandiset holds the multi-patch recordings of Fig. 5d-i,
[... 128 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/001751-liu-2026-01.md",
 "old_string": "were kept with the disagreements recorded, and a question on Supplementary\nTable 5 was filed\nin `questions/001751.yaml`, after the reader's run.",
 "new_string": "were kept with the disagreements recorded, and a question on Supplementary\nTable 5 was filed in `questions/001751.yaml`, after the reader's run."
}
```

```
The file docs/pilot-notes/001751-liu-2026-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/001751-liu-2026-01.md",
 "old_string": "names the first AIC sample A1C-1-Q and stores the run mode in its charge\ncolumn. Questions\nare put to the paper's authors: whether connections were called by eye on\naveraged traces, with which criteria for Excellent, Good and OK quality,\nwhether the 31 connections include the OK ones and which pairs and cells make\nup the 1,292 pairs and 377 neurons; and which filter and window gave\nmax_Na_current.",
 "new_string": "names the first AIC sample A1C-1-Q and stores the run mode in its charge\ncolumn. Questions are put to the paper's authors: whether connections were\ncalled by eye on averaged traces, with which criteria for Excellent, Good and\nOK quality, whether the 31 connections include the OK ones and which pairs and\ncells make up the 1,292 pairs and 377 neurons; and which filter and window gave\nmax_Na_current."
}
```

```
The file docs/pilot-notes/001751-liu-2026-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/001751-liu-2026-01.md",
 "old_string": "new claim, and left four points open. Every Fig. 5 claim rests on the cell",
 "new_string": "new claim, and left four points open. The Fig. 5 claims rest on the cell"
}
```

```
The file docs/pilot-notes/001751-liu-2026-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  cat docs/pilot-notes/001751-liu-2026-01.md; git status --short | grep -v "^?? \."
```

```
# 001751, Liu et al. 2026

Two claims reproduced, four partially, two not reproduced and one blocked for
missing data; the one claim that also uses inputs from outside the dataset,
`fig5-pc-rate-comparable-primate`, is counted apart and blocked as methods
underspecified, by its own criterion. Of the 35 claims, one is a link check,
`code-table-link`, added by the author and reproduced, and 24 have their data
elsewhere, in the paper's code repository, other dandisets, GEO, MetaboLights,
NeuroMorpho.org or the model, and are counted apart: six reproduced (two on an
assumption), three partially and 15 blocked. The first verification round
agreed with 31 of the 35 outcomes as they stood and the second with 34,
disagreeing on `patchseq-mapping`, which was kept blocked with the disagreement
recorded, and nothing was proposed after the second, so there was no third
round. It pins version 0.260825.0222, the only published version, with the
same file count and bytes as the draft; the paper cites none. The paper, Liu,
Huang, Shen, Shao, Jing et al., "An atlas of primate insular cortex reveals a
signal-processing strategy in von Economo neurons" in Nature Cell Biology, has
its Patch-seq, Na+ current and postsynaptic current recordings in DANDI:001746,
001750 and 001752; this dandiset holds the multi-patch recordings of Fig. 5d-i,
301 files of up to eight layer 5b neurons, for the finding that von Economo
[... 127 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/001751-liu-2026-01.md",
 "old_string": "Table 5 was filed in `questions/001751.yaml`, after the reader's run. Round 2 agreed with 34 and\nfound sentences the outputs did not support (296 of 296 files where the table",
 "new_string": "Table 5 was filed in `questions/001751.yaml`, after the reader's run. Round 2\nagreed with 34 and found sentences the outputs did not support (296 of 296 files where the table"
}
```

```
The file docs/pilot-notes/001751-liu-2026-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

I wrote the notes in `docs/pilot-notes/001751-liu-2026-01.md` and changed no other file. Nothing is committed. The `catalystneuro` field for 001751 is empty, so the second paragraph does not open with the CatalystNeuro sentence. At about 1,750 words, the note is a little longer than the five recent ones (about 1,480 to 1,650).

# 001751, Liu et al. 2026

Two claims reproduced, four partially, two not reproduced and one blocked for missing data; the one claim that also uses inputs from outside the dataset, `fig5-pc-rate-comparable-primate`, is counted apart and blocked as methods underspecified, by its own criterion. Of the 35 claims, one is a link check, `code-table-link`, added by the author and reproduced, and 24 have their data elsewhere, in the paper's code repository, other dandisets, GEO, MetaboLights, NeuroMorpho.org or the model, and are counted apart: six reproduced (two on an assumption), three partially and 15 blocked. The first verification round agreed with 31 of the 35 outcomes as they stood and the second with 34, disagreeing on `patchseq-mapping`, which was kept blocked with the disagreement recorded, and nothing was proposed after the second, so there was no third round. It pins version 0.260825.0222, the only published version, with the same file count and bytes as the draft; the paper cites none. The paper, Liu, Huang, Shen, Shao, Jing et al., "An atlas of primate insular cortex reveals a signal-processing strategy in von Economo neurons" in Nature Cell Biology, has its Patch-seq, Na+ current and postsynaptic current recordings in DANDI:001746, 001750 and 001752; this dandiset holds the multi-patch recordings of Fig. 5d-i, 301 files of up to eight layer 5b neurons, for the finding that von Economo neurons (VENs) are sparsely connected in the local circuit (377 neurons, 1,292 pairs and 31 connections in the paper). The claims were written from the version of record in Europe PMC (PMC13457102) without a PDF, the Supplementary Information or the Source Data, and from the paper's code (AIC_proj at commit 44cd8a6 and PatchAnaLab 1.0); the check made thirteen changes, one of them a new claim, and left four points open. The Fig. 5 claims rest on the cell types and connection annotations of the code's table metadata_multiPatch.xlsx, reading (b) of the criteria, as the files carry none. Reproduced are `fig5-in-to-ven-absent` (0 of 54 pairs, against 55 +/- 5.5) and `fig5fg-example-slice`. Not reproduced are `fig5d-connectivity-totals` (26 annotated connections against 31 +/- 3.1, with 1,403 pairs within 1,292 +/- 129, 298 cells in the table outside 377 +/- 38 and 410 channels holding a cell in the files) and `fig5-pc-to-pc` (18 of 743, 2.42%, against 24 of 503, 4.77%). Partial are `fig5-ven-outputs-absent` (0 of 59 VEN-to-VEN and 0 of 54 VEN-to-IN, but one VEN-to-PC connection in 146 pairs), `fig5-pc-to-ven` (1 connection as in the paper, in 139 pairs against 200 +/- 20), `fig5-pc-in` (2 and 4 connections, in 83 and 86 pairs against 65 +/- 6.5) and `fig5i-ven-sparse-local-connectivity` (every VEN rate is below the PC rate of the same partner class, but none of the four rates, 2.42, 2.41, 0.72 and 4.65%, is within tolerance of 4.77, 3.08, 0.5 and 6.15%, and the Fisher variants give p = 0.159 to 0.636). `fig5-pair-distances` is blocked as no file holds a soma position. Of the claims on other data, `fig5b-psc-frequency` (p = 0.0068, 0.0093, 0.0281 and 0.0102), `fig5c-psc-amplitude` (none below 0.05), `fig3e-phase-peak-index` (VEN median 0.116, Kruskal-Wallis p = 6.5e-08), `ven-map-et-ct` (14 and 15) and, on an assumption, `fig4j-eepsp-amplitude` (cell type p = 0.0056 and 0.0065 against the paper's 0.0034, on 23 pairs against 26) are reproduced on the per-cell tables in the code repository, and `fig4d-sodium-current` is reproduced on the 35 files of DANDI:001750 on the assumption of a 1 kHz low-pass (VEN median -17.3 against PC -31.5 pA, p = 0.0010, r = 0.99 with the code's max_Na_current). `fig8a-metabolite-gradient` (179 and 85, with AIC-V1 below 228 +/- 23 under every reading), `fig8de-glycolytic-bias` (2-ketobutyric acid 0.59, p = 0.18) and `fig6f-g-ven-subtype-mapping` (14 and 15 against 10 +/- 1 and 11 +/- 1.1) are partial. `fig3c-ais-distance-length` and `patchseq-mapping` are blocked as metadata insufficient, `fig4j-eepsp-latency` as other, as its table holds no latencies, `ven-firing-rate-variability` as methods underspecified, and 11 claims on sequencing reads, morphologies, the NEURON models and DANDI:001746 as other, not attempted in this run. The author's first run gave the same outcomes except that `fig5-ven-outputs-absent` was not reproduced. The author asked no questions of a reader, so the answer and author-answers runs changed nothing. Round 1 disagreed on `fig5-ven-outputs-absent`, which it gave partially reproduced and which was changed, on `fig4d-sodium-current` (partially), on `fig8a-metabolite-gradient` (not reproduced) and on `patchseq-mapping` (partially), and found that filling the table down put 39 rows under the wrong file, that the presynaptic rule added a -30 mV condition the criterion lacks, that "no positions" was printed as a fixed string, that the Na+ peaks agreed with the code's values at only r = 0.40 to 0.90, that fig8a used the code's 558 metabolites, not the MetaboLights deposit, and that the response measure picks up pulse-locked artefacts; in reply the table was filled within each presynaptic block, the rule followed the criterion, every group and electrode field of the 301 files was printed, 40 readings of the Na+ peak were run and the 1 kHz low-pass adopted, the metabolite claims were tested on the deposit, peaks on the first sample of the window were flagged, the other three outcomes were kept with the disagreements recorded, and a question on Supplementary Table 5 was filed in `questions/001751.yaml`, after the reader's run. Round 2 agreed with 34 and found sentences the outputs did not support (296 of 296 files where the table names 288, a stale 281 of 288 in a finding, r = 0.99 holding only for steps up to 0 mV, "the only published version" and "the only revision", the code's use of filter_1000Lowpass and the README's run time); in reply these were printed or corrected, and the PDFs under `paper/` were rendered with PyMuPDF, none of them holding Supplementary Table 5. The author's run took about 1 h 50 min (13:41 to about 15:30 UTC); during development a clash between a column name and a pingouin method and a header-row offset in the AIS table were fixed, and in the round 2 revision ftp.ebi.ac.uk refused connections on the first re-run, so a retry was added to the MetaboLights download. The notebook ran in about 3 minutes at first, 165 s after the author-answers run, 209 s after round 1 and 304 s at the end. Untracked dotfiles and a `scripts` entry, a character device, were left alone.

The files carry no cell type, no connection label and no soma position, so none of the Fig. 5 counts can be made from the dandiset alone; types and connections exist only in the code's table metadata_multiPatch.xlsx, which links to the files by name, and neither the paper nor its code gives a rule for calling a connection. The table disagrees with the paper: it lists 298 cells, 1,416 ordered pairs (1,403 in files of the dandiset) and 26 connections, where the paper reports 377 neurons, 1,292 pairs and 31 connections, PC-to-PC 18 of 743 against 24 of 503, one VEN-to-PC connection (190315s2, channel 4 to 6, Excellent, with a 1 mV response in the data) where the paper reports none, and pair counts that differ from the paper's by more than 10% in 6 of 8 classes. It is also inconsistent with itself and with the files: ten of its presynaptic blocks name no NWB file (8 match a file by the firing channel; 190315s2 channel 7 and 20241014HS2 channel 8, 13 rows, match none), it gives 5 cells two types, labels 2 connections with a projection that names another postsynaptic channel, its Nr_Conn disagrees with its annotations in 4 of 53 slices, six of its pairs name channels that read 0 mV (slice 190314s1, channels 6 and 7), eight of its Inh connections come from a PC and 6 of its 12 Inh connections have a positive averaged response; 5 files of slice 20240912HS2 are not in it. Every response series states a rate of 1 Hz where the data are sampled at 25 kHz, and the stimulus series gives its rate of 25,000 with the unit millisecond; the stimulus amplitude is stored as 2 (2.5 or 3 in 14 files) with the unit amperes where the Methods inject 2 nA; every file names electrode Elec_8 as the stimulated one, while the cell that fires is on channel 8 in only 35 of 301 files and is the table's presynaptic channel in 286 of the 288 files it names; and all 301 files have the session start 2018-01-01T01:00+08:00 although the slices are named for dates in 2019 and 2024, with every subject of age P4Y/P6Y and sex M. The Methods average over more than 20 sweeps, and 119 of 301 files hold more than 20 (median 20, range 1 to 30). Of the other data, sumData_StimWM.xlsx holds 23 VEN-PC pairs where the paper states 26, AIScmp_PCvsVEN_Fig5c.xlsx 120 VENs and 500 PCs against 108 and 430, with no slice or animal for the legend's two-way ANOVA, the Patch-seq mapping results 14 VEN-L and 15 VEN-S against 10 and 11 and 17 excitatory clusters against 18, with the inhibitory mapping not saved, and PeakIdx_Fig5e.xlsx 32 VENs against the legend's 22. The MetaboLights deposit MTBLS13927 holds 558 identified metabolites where the paper quantifies 581, the same as the code's Metabolic_data.xlsx, which swaps the labels of two V1 samples; the deposit names the first AIC sample A1C-1-Q and stores the run mode in its charge column. Questions are put to the paper's authors: whether connections were called by eye on averaged traces, with which criteria for Excellent, Good and OK quality, whether the 31 connections include the OK ones and which pairs and cells make up the 1,292 pairs and 377 neurons; and which filter and window gave max_Na_current.

The author's points on the protocol: it does not say whether marking claims `data: with_labels` and adding `depends_on` counts as changing the claims file, and both were done with statements, expected values and criteria unchanged; connection annotations are expert judgements, yet had to be counted as `with_labels`, so it was recorded that they decide the outcome; claims on data elsewhere not tried for lack of scope have no fitting block reason, so `other` was used with a note on each; some such claims name a raw archive while the paper's code holds per-cell tables of the same data, which were used and recorded as a deviation; there is no rule for a claim only partly testable, so `patchseq-mapping` was blocked with the excitatory numbers in its notes; and it is not clear when unmatched denominators make an outcome partial, so partial was used where the connection counts matched and only the pair counts were off.

## End of run

27 turns, 3 minutes, $1.44 at API prices, result: success.
