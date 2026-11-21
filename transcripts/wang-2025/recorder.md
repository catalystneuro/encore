# wang-2025 · recorder · run 44859027219

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; ls transcripts/wang-2025/; python tools/readme_row.py wang-2025; cat attempts/wang-2025-01.yaml
```

```
<persisted-output>
Output too large (109.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/e26ca373-5040-46c8-9c2a-d0960f4e74ab/tool-results/buxv0gax9.txt

Preview (first 2KB):
docs/pilot-notes/amjad-2025-01.md
docs/pilot-notes/andrews-2024-01.md
docs/pilot-notes/armstrong-2026-01.md
docs/pilot-notes/asari-2009-01.md
docs/pilot-notes/asari-2009-02.md
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
[... 39 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -c attempts/wang-2025-01.yaml claims/wang-2025.yaml transcripts/wang-2025/*-report.md; grep -n -B3 "000363" README.md | head; grep -n "^|" README.md | head -3; for f in amjad-2025-01 andrews-2024-01 armstrong-2026-01 asari-2009-01 asari-2009-02; do echo "=== $f"; cat docs/pilot-notes/$f.md; done; head -5 docs/pilot-notes/knierim-2000-02.md
```

```
<persisted-output>
Output too large (35.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/e26ca373-5040-46c8-9c2a-d0960f4e74ab/tool-results/bodsrnx5f.txt

Preview (first 2KB):
111304 attempts/wang-2025-01.yaml
 64334 claims/wang-2025.yaml
  5379 transcripts/wang-2025/author-report.md
  4102 transcripts/wang-2025/author-revise-1-report.md
  3758 transcripts/wang-2025/author-revise-2-report.md
  3057 transcripts/wang-2025/claims-check-report.md
  4889 transcripts/wang-2025/claims-report.md
  8860 transcripts/wang-2025/verifier-1-report.md
  7348 transcripts/wang-2025/verifier-2-report.md
213031 total
=== amjad-2025-01
# 002013, Amjad et al. 2025

Seven claims reproduced, one partially and five blocked on the dandiset,
plus one claim linking the dandiset to the paper's Zenodo deposit,
reproduced (trial lists agree for 99.8 to 100% of trials); both rounds
[... 22 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/e26ca373-5040-46c8-9c2a-d0960f4e74ab/tool-results/bodsrnx5f.txt"
}
```

```
1	111304 attempts/wang-2025-01.yaml
2	 64334 claims/wang-2025.yaml
3	  5379 transcripts/wang-2025/author-report.md
4	  4102 transcripts/wang-2025/author-revise-1-report.md
5	  3758 transcripts/wang-2025/author-revise-2-report.md
6	  3057 transcripts/wang-2025/claims-check-report.md
7	  4889 transcripts/wang-2025/claims-report.md
8	  8860 transcripts/wang-2025/verifier-1-report.md
9	  7348 transcripts/wang-2025/verifier-2-report.md
10	213031 total
11	=== amjad-2025-01
12	# 002013, Amjad et al. 2025
13	
14	Seven claims reproduced, one partially and five blocked on the dandiset,
15	plus one claim linking the dandiset to the paper's Zenodo deposit,
16	reproduced (trial lists agree for 99.8 to 100% of trials); both rounds
17	agreed with every outcome. The paper describes microinvasive probes for
18	recording dopamine and electrical activity in monkeys; the beta burst,
19	reward and unit isolation claims reproduce, the dopamine reward effect
20	weakly (p = 0.023, and not in the stored trial-aligned `da`).
[... 494 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "Reproduced\|reproduced |" README.md | head -5; sed -n 1,80p tools/readme_row.py; grep -n -A12 '"000363"' targets/dandisets.json
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
[... 59 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n '000363' targets/dandisets.json | head; python - <<'E'
import json
d=json.load(open('targets/dandisets.json'))
items = d if isinstance(d,list) else d.get('dandisets', d)
if isinstance(items, dict): items=list(items.values()) if not '000363' in items else [items['000363']]
for x in items:
    if isinstance(x,dict) and '000363' in json.dumps(x)[:200]: print(json.dumps(x,indent=1))
E
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  head -c 600 targets/dandisets.json; echo; grep -n '363' targets/dandisets.json | head
```

```
{
 "schema_version": 1,
 "generated": "2026-11-17T15:59:44+00:00",
 "source": "https://api.dandiarchive.org/api",
 "counts": {
  "public_dandisets": 678,
  "with_a_paper": 298,
  "with_a_published_version": 256,
  "papers": 316,
  "converted_by_catalystneuro": 51
 },
 "targets": [
  {
   "dandiset": "000003",
   "name": "Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells",
   "published_version": "0.260218.2052",
   "asset_count": 101,
   "size_gb": 1922.23,
   "data_standards": [
    "Neurodata Without Borders (NWB)"
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/wang-2025; for f in author-report.md author-revise-1-report.md author-revise-2-report.md claims-check-report.md claims-report.md verifier-1-report.md verifier-2-report.md; do echo "=== $f"; cat $f; done
```

```
<persisted-output>
Output too large (36.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/e26ca373-5040-46c8-9c2a-d0960f4e74ab/tool-results/bfrk3uitj.txt

Preview (first 2KB):
=== author-report.md
I ran author steps 1 to 6 for wang-2025. Of 30 claims, 2 reproduced, 1 partially reproduced and 25 are blocked; the entry passes its checks and its clean run (1,102 s). I did not commit anything.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| link-authors-deposit (link claim I added) | reproduced: all 16 areas in the authors' area grouping match the dataset's annotations; all 106 of the authors' Fig. 6/7 sessions match dataset sessions (21 mice) |
| data-scale | reproduced: 272,227 units (154,948 `unit_quality` good, 69,453 `classification` good), in 17 areas |
| fig6e-marker-clustering | partially reproduced: Calinski-Harabasz score 5.92 against a null of 1.02 ± 0.33, p < 0.001. Both nose-dominant (3) and jaw-dominant (11) mice occur. The score is outside the paper's 12.57 ± 1.26; it is 7.63 on the authors' 106 sessions and 3.61 to 7.90 across all variants. The outcome is the same under all five seeds. |
| 25 other claims (Figs. 2 to 7, Extended Data, Supplementary autoencoder) | blocked, `too_large` |

## 2. Dataset, assumptions, questions

- **Version.** I pinned 0.230822.0128, the version the paper cites. It holds spikes, trials and the jaw, nose and tongue markers, but no video and no autoencoder embedding.
  - The later version 0.231012.2129 (65.7 TB) adds the raw video. Reading it would take about 1 h per session, about 100 h for the paper's 106 sessions, before training any network. That is why the 25 claims are blocked.
[... 6 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/e26ca373-5040-46c8-9c2a-d0960f4e74ab/tool-results/bfrk3uitj.txt"
}
```

```
1	=== author-report.md
2	I ran author steps 1 to 6 for wang-2025. Of 30 claims, 2 reproduced, 1 partially reproduced and 25 are blocked; the entry passes its checks and its clean run (1,102 s). I did not commit anything.
3	
4	## 1. Outcomes
5	
6	| Claim | Outcome |
7	|---|---|
8	| link-authors-deposit (link claim I added) | reproduced: all 16 areas in the authors' area grouping match the dataset's annotations; all 106 of the authors' Fig. 6/7 sessions match dataset sessions (21 mice) |
9	| data-scale | reproduced: 272,227 units (154,948 `unit_quality` good, 69,453 `classification` good), in 17 areas |
10	| fig6e-marker-clustering | partially reproduced: Calinski-Harabasz score 5.92 against a null of 1.02 ± 0.33, p < 0.001. Both nose-dominant (3) and jaw-dominant (11) mice occur. The score is outside the paper's 12.57 ± 1.26; it is 7.63 on the authors' 106 sessions and 3.61 to 7.90 across all variants. The outcome is the same under all five seeds. |
11	| 25 other claims (Figs. 2 to 7, Extended Data, Supplementary autoencoder) | blocked, `too_large` |
12	
13	## 2. Dataset, assumptions, questions
14	
15	- **Version.** I pinned 0.230822.0128, the version the paper cites. It holds spikes, trials and the jaw, nose and tongue markers, but no video and no autoencoder embedding.
16	  - The later version 0.231012.2129 (65.7 TB) adds the raw video. Reading it would take about 1 h per session, about 100 h for the paper's 106 sessions, before training any network. That is why the 25 claims are blocked.
17	  - Units, trials and markers are identical in both versions for 4 sessions drawn at random.
18	- **Authors' deposit.** Their Zenodo deposit has no per-frame embeddings. Their Google Drive folder is not pinned, so it cannot be used.
19	- **Critical finding.** In 5 sessions (SC011 on three days, SC022 on two, February 2019) the marker timestamps step 3.4 ms but the frames are 6.8 ms apart.
20	  - As deposited, the tongue is visible at 6 to 13% of lick events. With the timestamps
[... 286 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import yaml
r=yaml.safe_load(open('attempts/wang-2025-01.yaml'))
print(list(r.keys()))
for k in r:
    if k not in ('outcomes','findings','verifications','inputs','deviations'): print(k, r[k])
for f in r.get('findings',[]): print('---F', yaml.dump(f, width=200))
E
```

```
['schema_version', 'id', 'datasets', 'paper', 'date', 'entry', 'provenance', 'inputs', 'outcomes', 'findings', 'verifications']
schema_version 3
id wang-2025-01
datasets [{'archive': 'dandi', 'id': '000363', 'version': '0.230822.0128', 'doi': '10.48324/dandi.000363/0.230822.0128', 'relation': 'reuses'}]
paper doi:10.1038/s41593-025-02114-x
date 2026-11-20
entry wang-2025
provenance {'kind': 'agent', 'accountable': {'name': 'CatalystNeuro'}, 'agent': {'harness': 'Claude Code', 'model': 'claude-opus-5-5', 'protocol': 'pilot-18'}, 'runner': {'platform': 'GitHub Actions', 'url': 'https://github.com/catalystneuro/encore/actions/runs/44785187177'}}
---F about: data
kind: other
severity: critical
statement: In five sessions, sub-440959 (SC011) on 2019-02-24, 2019-02-25 and 2019-02-26 and sub-442571 (SC022) on 2019-02-27 and 2019-02-28, the DeepLabCut marker timestamps advance 3.4 ms per frame but
  the video frames are 6.8 ms apart. As deposited, the tongue is visible at 6 to 13% of the lick events, and no shift of the lick times within 1 s brings this above 0.49; stretching each trial's marker
  timestamps by 2 from its first frame puts the tongue at 99.9 to 100% of the licks. Their trial videos hold 934 to 946 frames (median per session), against 1864 to 1886 in the other eight sessions of the
  same two mice, although the trials last as long (median 4.83 to 4.90 s in all 13) and each video starts at its trial's start; the median over all sessions is 1904. The video in the later version holds
  the same frame counts and carries no timing (a starting time with a rate of 1.0, no timestamps), so the 6.8 ms spacing is inferred from the frame counts and the licks, not read from the video. The markers
  of these sessions are on a time base half as long as the trial table's, and nothing in the files shows it; any analysis of movement around task events in them comes out wrong.

---F about: data
kind: other
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import yaml
r=yaml.safe_load(open('attempts/wang-2025-01.yaml'))
for o in r['outcomes']:
    print('===', o['claim'], o['outcome'], o.get('blocked_by'), o.get('assumed'))
    if o['outcome']!='blocked' or o['claim'] in ('fig6-marker-vs-embedding-decoding','fig2b-medulla-vs-midbrain'):
        print(yaml.dump({k:v for k,v in o.items() if k not in('claim','outcome')}, width=200))
for v in r['verifications']:
    print('---V', {k:(v[k] if not isinstance(v[k],(list,dict)) else '...') for k in v})
E
python - <<'E'
import yaml
c=yaml.safe_load(open('claims/wang-2025.yaml'))
print({k:c[k] for k in c if k!='claims'})
for x in c['claims']: print(x['id'], '|', x.get('data'), '|', x.get('kind'),'|', x.get('figure', x.get('source','')), '|', x['statement'][:220])
E
```

```
=== link-authors-deposit reproduced None None
deviations:
- The link claim was written into the claims file by this attempt (protocol, author step 1.4), with its criterion, before the full run; it is the registry's check, not a finding of the paper.
notebook: reproduce_wang_2025.ipynb
notes: All 16 areas of area2anno.json have annotation names found among the dataset's anno_name values once commas are removed; 162 of the dataset's 294 distinct annotations fall in the map, the others
  being structures outside its 16 areas. All 106 session names of cal4cat-delay.pickle match a dataset session by mouse and date; the five SC038 days with two named sessions each have two dataset files.
  The 106 sessions come from 21 of the 28 mice; SC011, SC013, SC015, SC016, SC017, SC022 and SC023 have none.
output: claim:link-authors-deposit

=== data-scale reproduced None None
deviations:
- The 2 Hz filter uses the dataset's whole-session avg_firing_rate, not the rate over the included trials (Methods, Prediction of neural activity, 'Neurons with low firing rates (below 2 Hz) were excluded');
  the count before the filter already decides the claim.
- The paper names no quality label; both of the dataset's (unit_quality and classification) are reported, as the criterion allows. Units with unit_quality good but no CCF annotation count towards the neuron
  count and not towards any structure.
- Structures are the twelve major divisions of the Allen CCF, read from the authors' structure tree in their deposit (mousebrainontology_2.csv and mousebrainontology_heirarchy_cortexMaskExclusions21_sc.xlsx),
  with isocortex split into ALM (units on probes targeted to ALM, as the code's get_single_area_inds) and other isocortex, the level of the areas the criterion lists; each unit is counted once. A layer
  name missing from the tree takes the path of its area.
measured:
- 154948
[... 129 more lines not kept]
```

**Agent**

I have the record, claims and reports read. Checking the claims file's header for the paper's description, then writing.

**Agent calls Bash**

```bash
cd  head -30 claims/wang-2025.yaml; grep -n "title\|Nature Neuroscience\|ALM\b" claims/wang-2025.yaml | head -5
```

```
# Claims for Wang, Kurgyis, Chen, Kang, Chen, Liu, Liu, Svoboda, Li & Druckmann (2025), "Brain-wide
# analysis reveals movement encoding structured across and within brain areas", Nature Neuroscience,
# doi:10.1038/s41593-025-02114-x, on dandiset 000363 (Mesoscale Activity Map Dataset), which the
# paper reuses.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-20,
# protocol as stated in docs/protocol.md (pilot-18).
#
# Text read. The version of record (published 18 November 2025, open access), full text from the
# publisher's page: main text, figure legends, Methods, Extended Data Figs. 1 to 10 legends. The
# Supplementary Information PDF (41593_2025_2114_MOESM1_ESM.pdf; Supplementary Discussion on the
# session-independent autoencoder, Supplementary Table 1 on thalamic nuclei, Supplementary Figs. 1
# and 2) was read from its extracted text in the same file. The Reporting Summary and the three
# Supplementary Videos were not read; no claim rests on them. Figures were not opened; every
# number used below is printed in the text or a legend.
#
# Code read. github.com/druckmann-lab/MapVideoAnalysis at commit 7d27624 (7d276243db16db5af6da68a48de7720ef77007c2),
# the repository the paper links (Zenodo doi:10.5281/zenodo.16740762). It holds the package
# VideoAnalysisUtils (ridge prediction and explained variance, functions_for_r2.py; single-neuron
# choice and movement AUCs, functions_for_auc.py; area selection, nearest-neighbour and spatial
# uniformity tests, functions.py; figure classes and their statistics, plotting_utils.py, where
[... 15 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/wang-2025-01.md",
 "content": "# wang-2025, Wang et al. 2025\n\nOne claim reproduced, one partially, none not reproduced and 27 blocked, all\nfor missing data, plus one claim linking the dandiset to the authors' Zenodo\ndeposit, reproduced (all 16 areas of the deposit's area grouping are among the\ndataset's annotations, and all 106 sessions of its Fig. 6 and 7 file match a\ndataset session). The first verification round agreed with the link claim and\nwith `fig6e-marker-clustering`, would have given `data-scale` partially\nreproduced, and gave `data_missing` in place of `too_large` as the block\nreason; the author recounted the structures and changed the block reason on 27\nclaims, the second round agreed with all 30 outcomes, and nothing was proposed\nafter it, so there was no third round. The attempt pins 0.230822.0128, the\nversion the paper cites. The paper, Wang, Kurgyis, Chen et al., \"Brain-wide\nanalysis reveals movement encoding structured across and within brain areas\"\n(Nature Neuroscience), predicts the activity of neurons recorded on Neuropixels\nprobes across the mouse brain from orofacial video, by tracked markers, a\n16-dimensional autoencoder embedding and end-to-end networks, and reports that\nthe variance explained is highest in medulla and lowest in thalamus, changes\nsmoothly within thalamus, leads or follows movement by area and by depth in\nALM, and that choice can be decoded from uninstructed movements in a way\nspecific to each mouse. The claims were written from the version of record and\nthe Supplementary Information, and from the paper's code at commit 7d27624;\nthe deep-network repository could not be fetched, and the code of the choice\ndecoder of Figs. 6 and 7 is in neither repository. The claims check corrected\nnine of the 29 claims. Reproduced is the scale of the data: 154,948 units with\n`unit_quality` good, in 13 structures when each unit is counted once in its\nmajor Allen division with ALM apart from other isocortex, more than 12 by one.\nPartial is the Fig. 6e clustering of mice by single markers: a\nCalinski-Harabasz score of 6.83 against a null of 1.03 +/- 0.42 (p < 0.001),\nwith 4 nose-type and 5 jaw-type mice, where the paper gives 12.57; all 72\nvariants give 3.52 to 7.91, and the same decoder gives a response-epoch AUC of\n0.754 for the better of jaw and nose against the paper's 0.88, so the lower\nscore may come from the decoder and not from the data. The other 27 claims, on\nFigs. 2 to 7, the Extended Data and the session-independent autoencoder, need\nthe embedding, the networks or the video decoder and are blocked. The author's\nfirst run gave the same outcomes, with the blocked claims as `too_large`.\nRound 1 found that the 17 areas of `data-scale` nest inside each other, that\nonly about a third of the authors' sessions have video in any version, that\nthe marker half of `fig6-marker-vs-embedding-decoding` could be run, that the\nsession AUC pooled the folds as an unstated choice and that the authors' 106\nsessions should be the main set; in reply each unit was counted once in its\nmajor division, the 106 sessions were crossed with the video files (34 with\nvideo, 72 without), the marker half was computed, the fold-averaged AUC became\nthe main reading and the 106 sessions the main set. Round 2 found sentences\nthe outputs did not support (the read time of the video, 167 sessions where\n166 are decoded, and the 105 sessions put in the Methods), which were\ncorrected, and asked that the weaker Fig. 6e score be read as weaker under this\ndecoder. After round 2 a cell was added that checks the frame spacing of the\nflagged sessions from their frame counts; the first re-run failed for going 7 s\nover the 60-minute limit, and with six workers in place of four the second\npassed in 3589 s. The author's run took about 2 h 10 min (17:38 to about 19:46\nUTC); the notebook ran in about 18 min at first, with at most 0.5 GB of\nmemory, and in 42 min after round 1.\n\nThe version the paper cites holds no video and no autoencoder embedding, the\ninput of most of the paper's analyses. The later version 0.231012.2129\n(65.7 TB) adds the raw electrophysiology to 169 files and the raw video to 71\nof them (28.9 TB), from 16 of the 28 mice; 34 of the 106 sessions the paper\nused for Figs. 6 and 7 have video and 72 have none in any version, and the\nauthors' per-frame embeddings are in no pinned deposit. In five sessions, SC011\non 2019-02-24, 2019-02-25 and 2019-02-26 and SC022 on 2019-02-27 and\n2019-02-28, the marker timestamps advance 3.4 ms per frame but the frames are\n6.8 ms apart, rated critical: as deposited the tongue is visible at 6 to 13% of\nthe lick events, and stretching each trial's timestamps by 2 puts it at 99.9\nto 100%; their trial videos hold 934 to 946 frames against 1864 to 1886 in the\nother eight sessions of the same mice, the spacing is inferred from the frame\ncounts and the licks, and nothing in the files shows it. In SC026_080719 the\ntongue is visible at 60% of lick events, with 539 trial videos for 630 trials,\nso some videos are probably attached to the wrong trials. SC066_041321 has\nmarkers for 7 trial videos of 550 trials, and SC065_050521 lacks them for 140\nof its 354 correct trials. Only units with `classification` good carry a CCF\nannotation, so 92,769 of the 154,948 `unit_quality` good units have no\nlocation, and which label the paper's 50,000 neurons use is not said. The\nmarker timestamps step by exactly 3.4 ms, 294 Hz, where the paper states\n300 Hz. The paper's 106 sessions come from 21 of the 28 mice, and the paper\ndoes not say how they were chosen. The question put to the paper's authors is\nwhich choice decoder Fig. 6 used, with which features, penalty selection and\ntime resolution, and how the AUC of a time bin was formed from the folds.\n\nThe author's points on the protocol: it does not say which fields a link claim\ntakes; it is silent on whether the author may change a claim's `data` or\n`depends_on`; an outside list used only to select sessions fits no data\ncategory; it does not say how to block claims whose input is only in an\nunpinned later version; it does not say whether sessions that fail the clock\ncheck are left out of an analysis; the fig6e criterion has no partial rule, and\nthe general definition was used; its severities for clock problems overlap; and\nit asks for one full run while any edit forces another.\n"
}
```

```
File created successfully at: docs/pilot-notes/wang-2025-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "summaries/wang-2025-01.md",
 "content": "Most of the paper's main findings could not be tested in this data. How much movement explains activity across and within brain areas, whether neurons lead or follow movement, and decoding choice from video all need the video or its autoencoder embedding, which the cited dataset version lacks. Of the 106 sessions the paper used, 72 have no video in any version. The data do hold the stated scale of neurons and structures, and the mouse-specific pattern of choice decoding from jaw and nose markers appears, though weaker than reported. The paper does not describe its choice decoder, and the one used here was weaker, which may explain the gap.\n"
}
```

```
File created successfully at: summaries/wang-2025-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  wc -w summaries/wang-2025-01.md; grep -c "—\|rather" docs/pilot-notes/wang-2025-01.md summaries/wang-2025-01.md; git status --short
```

```
110 summaries/wang-2025-01.md
docs/pilot-notes/wang-2025-01.md:0
summaries/wang-2025-01.md:0
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
?? docs/pilot-notes/wang-2025-01.md
?? scripts
?? summaries/wang-2025-01.md
```

**Agent**

I wrote both files and changed nothing else. Two things to flag:

- **No CatalystNeuro sentence:** dandiset 000363 has no entry in `targets/dandisets.json`, so there is no `catalystneuro` field to read. The second paragraph therefore doesn't open with the CatalystNeuro sentence.
- **Untracked files I didn't create:** `git status` lists some in the repository root (`.bashrc`, `.gitconfig`, `.idea`, `scripts` and others). I left them alone.

The summary is 110 words in five sentences. Nothing is committed.

### docs/pilot-notes/wang-2025-01.md

# wang-2025, Wang et al. 2025

One claim reproduced, one partially, none not reproduced and 27 blocked, all for missing data, plus one claim linking the dandiset to the authors' Zenodo deposit, reproduced (all 16 areas of the deposit's area grouping are among the dataset's annotations, and all 106 sessions of its Fig. 6 and 7 file match a dataset session). The first verification round agreed with the link claim and with `fig6e-marker-clustering`, would have given `data-scale` partially reproduced, and gave `data_missing` in place of `too_large` as the block reason; the author recounted the structures and changed the block reason on 27 claims, the second round agreed with all 30 outcomes, and nothing was proposed after it, so there was no third round. The attempt pins 0.230822.0128, the version the paper cites. The paper, Wang, Kurgyis, Chen et al., "Brain-wide analysis reveals movement encoding structured across and within brain areas" (Nature Neuroscience), predicts the activity of neurons recorded on Neuropixels probes across the mouse brain from orofacial video, by tracked markers, a 16-dimensional autoencoder embedding and end-to-end networks, and reports that the variance explained is highest in medulla and lowest in thalamus, changes smoothly within thalamus, leads or follows movement by area and by depth in ALM, and that choice can be decoded from uninstructed movements in a way specific to each mouse. The claims were written from the version of record and the Supplementary Information, and from the paper's code at commit 7d27624; the deep-network repository could not be fetched, and the code of the choice decoder of Figs. 6 and 7 is in neither repository. The claims check corrected nine of the 29 claims. Reproduced is the scale of the data: 154,948 units with `unit_quality` good, in 13 structures when each unit is counted once in its major Allen division with ALM apart from other isocortex, more than 12 by one. Partial is the Fig. 6e clustering of mice by single markers: a Calinski-Harabasz score of 6.83 against a null of 1.03 +/- 0.42 (p < 0.001), with 4 nose-type and 5 jaw-type mice, where the paper gives 12.57; all 72 variants give 3.52 to 7.91, and the same decoder gives a response-epoch AUC of 0.754 for the better of jaw and nose against the paper's 0.88, so the lower score may come from the decoder and not from the data. The other 27 claims, on Figs. 2 to 7, the Extended Data and the session-independent autoencoder, need the embedding, the networks or the video decoder and are blocked. The author's first run gave the same outcomes, with the blocked claims as `too_large`. Round 1 found that the 17 areas of `data-scale` nest inside each other, that only about a third of the authors' sessions have video in any version, that the marker half of `fig6-marker-vs-embedding-decoding` could be run, that the session AUC pooled the folds as an unstated choice and that the authors' 106 sessions should be the main set; in reply each unit was counted once in its major division, the 106 sessions were crossed with the video files (34 with video, 72 without), the marker half was computed, the fold-averaged AUC became the main reading and the 106 sessions the main set. Round 2 found sentences the outputs did not support (the read time of the video, 167 sessions where 166 are decoded, and the 105 sessions put in the Methods), which were corrected, and asked that the weaker Fig. 6e score be read as weaker under this decoder. After round 2 a cell was added that checks the frame spacing of the flagged sessions from their frame counts; the first re-run failed for going 7 s over the 60-minute limit, and with six workers in place of four the second passed in 3589 s. The author's run took about 2 h 10 min (17:38 to about 19:46 UTC); the notebook ran in about 18 min at first, with at most 0.5 GB of memory, and in 42 min after round 1.

The version the paper cites holds no video and no autoencoder embedding, the input of most of the paper's analyses. The later version 0.231012.2129 (65.7 TB) adds the raw electrophysiology to 169 files and the raw video to 71 of them (28.9 TB), from 16 of the 28 mice; 34 of the 106 sessions the paper used for Figs. 6 and 7 have video and 72 have none in any version, and the authors' per-frame embeddings are in no pinned deposit. In five sessions, SC011 on 2019-02-24, 2019-02-25 and 2019-02-26 and SC022 on 2019-02-27 and 2019-02-28, the marker timestamps advance 3.4 ms per frame but the frames are 6.8 ms apart, rated critical: as deposited the tongue is visible at 6 to 13% of the lick events, and stretching each trial's timestamps by 2 puts it at 99.9 to 100%; their trial videos hold 934 to 946 frames against 1864 to 1886 in the other eight sessions of the same mice, the spacing is inferred from the frame counts and the licks, and nothing in the files shows it. In SC026_080719 the tongue is visible at 60% of lick events, with 539 trial videos for 630 trials, so some videos are probably attached to the wrong trials. SC066_041321 has markers for 7 trial videos of 550 trials, and SC065_050521 lacks them for 140 of its 354 correct trials. Only units with `classification` good carry a CCF annotation, so 92,769 of the 154,948 `unit_quality` good units have no location, and which label the paper's 50,000 neurons use is not said. The marker timestamps step by exactly 3.4 ms, 294 Hz, where the paper states 300 Hz. The paper's 106 sessions come from 21 of the 28 mice, and the paper does not say how they were chosen. The question put to the paper's authors is which choice decoder Fig. 6 used, with which features, penalty selection and time resolution, and how the AUC of a time bin was formed from the folds.

The author's points on the protocol: it does not say which fields a link claim takes; it is silent on whether the author may change a claim's `data` or `depends_on`; an outside list used only to select sessions fits no data category; it does not say how to block claims whose input is only in an unpinned later version; it does not say whether sessions that fail the clock check are left out of an analysis; the fig6e criterion has no partial rule, and the general definition was used; its severities for clock problems overlap; and it asks for one full run while any edit forces another.

### summaries/wang-2025-01.md

Most of the paper's main findings could not be tested in this data. How much movement explains activity across and within brain areas, whether neurons lead or follow movement, and decoding choice from video all need the video or its autoencoder embedding, which the cited dataset version lacks. Of the 106 sessions the paper used, 72 have no video in any version. The data do hold the stated scale of neurons and structures, and the mouse-specific pattern of choice decoding from jaw and nose markers appears, though weaker than reported. The paper does not describe its choice decoder, and the one used here was weaker, which may explain the gap.

## End of run

15 turns, 2 minutes, $0.85 at API prices, result: success.
