# 001746 · recorder · run 41671057896

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; python tools/readme_row.py 001746; ls claims/001746/ transcripts/001746/; cat attempts/001746-liu-2026-01.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'));
d=d if isinstance(d,list) else d.get('dandisets',d)
for e in (d if isinstance(d,list) else d.values()):
  if '001746' in json.dumps(e): print(json.dumps(e,indent=1))"
```

```
<persisted-output>
Output too large (293.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/4b06ca3c-fc4a-479f-8f20-d0d513a1969a/tool-results/biajyg054.txt

Preview (first 2KB):
docs/pilot-notes/001676-skromne-carrasco-2026-01.md
docs/pilot-notes/001702-chaunsali-2025-01.md
docs/pilot-notes/001605-funamizu-2016-01.md
docs/pilot-notes/001642-ito-2015-01.md
docs/pilot-notes/001678-bellvila-2026-01.md
| [001746](https://dandiarchive.org/dandiset/001746) | [Liu et al. 2026](https://doi.org/10.1038/s41556-026-02009-4) | 4 (+1) | 8 | 1 (+1) | 6 (+1) | [`001746-liu-2026`](entries/001746-liu-2026) |
claims/001746/:
10.1038-s41556-026-02009-4.yaml

transcripts/001746/:
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
[... 48 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/001746-liu-2026-01.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'));print(type(d))
items = d if isinstance(d,list) else list(d.values())
for e in items:
  if isinstance(e,dict) and str(e.get('id',e.get('identifier','')))=='001746': print(json.dumps(e,indent=1))
" | head -50
```

```
<persisted-output>
Output too large (78.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/4b06ca3c-fc4a-479f-8f20-d0d513a1969a/tool-results/b431hftho.txt

Preview (first 2KB):
schema_version: 2
id: 001746-liu-2026-01
dataset:
  archive: dandi
  id: '001746'
  version: 0.260825.0222
  doi: 10.48324/dandi.001746/0.260825.0222
paper: doi:10.1038/s41556-026-02009-4
date: 2026-11-03
entry: 001746-liu-2026
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for f in docs/pilot-notes/001676-skromne-carrasco-2026-01.md docs/pilot-notes/001702-chaunsali-2025-01.md docs/pilot-notes/001605-funamizu-2016-01.md docs/pilot-notes/001642-ito-2015-01.md docs/pilot-notes/001678-bellvila-2026-01.md docs/pilot-notes/001754-knierim-2000-02.md; do echo "== $f"; cat $f; done
```

```
<persisted-output>
Output too large (46.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/4b06ca3c-fc4a-479f-8f20-d0d513a1969a/tool-results/bakpangtu.txt

Preview (first 2KB):
== docs/pilot-notes/001676-skromne-carrasco-2026-01.md
# 001676, Skromne Carrasco et al. 2026

Eighteen claims reproduced (14 on an assumption), six partially (two on an
assumption), three not reproduced (two on an assumption) and five blocked,
three for insufficient metadata, one for missing data and one as too large.
All 32 claims are on the dandiset. The first verification round agreed with 26
of the 32 outcomes as they stood and the second with all 32, and nothing was
proposed after the second, so there was no third round. It pins version
0.251205.2137, the version the paper cites and the only published one. The
paper, Skromne Carrasco, Viejo and Peyrache, "Months-long stability of the
head-direction system" in Nature, images head-direction (HD) cells of the
post-subiculum with a Miniscope in mice 1 to 5 over a month in one environment
(Fig. 1), over two weeks in each of four environments (Fig. 2), in a week of
probe trials (Fig. 3) and in visits in random order (Extended Data Fig. 9), and
in mice 6 to 10 over weekly and single visits (Fig. 4, Extended Data Fig. 10),
[... 13 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/4b06ca3c-fc4a-479f-8f20-d0d513a1969a/tool-results/bakpangtu.txt"
}
```

```
1	== docs/pilot-notes/001676-skromne-carrasco-2026-01.md
2	# 001676, Skromne Carrasco et al. 2026
3	
4	Eighteen claims reproduced (14 on an assumption), six partially (two on an
5	assumption), three not reproduced (two on an assumption) and five blocked,
6	three for insufficient metadata, one for missing data and one as too large.
7	All 32 claims are on the dandiset. The first verification round agreed with 26
8	of the 32 outcomes as they stood and the second with all 32, and nothing was
9	proposed after the second, so there was no third round. It pins version
10	0.251205.2137, the version the paper cites and the only published one. The
11	paper, Skromne Carrasco, Viejo and Peyrache, "Months-long stability of the
12	head-direction system" in Nature, images head-direction (HD) cells of the
13	post-subiculum with a Miniscope in mice 1 to 5 over a month in one environment
14	(Fig. 1), over two weeks in each of four environments (Fig. 2), in a week of
15	probe trials (Fig. 3) and in visits in random order (Extended Data Fig. 9), and
16	in mice 6 to 10 over weekly and single visits (Fig. 4, Extended Data Fig. 10),
17	with silicon-probe recordings in four mice (Extended Data Fig. 7). The claims
18	were written from the version of record without the Supplementary Information
19	or the Source Data, and no figure was read from the PDF; the paper's code is
20	available on request, so no code was read. Twenty-seven claims were tested.
[... 637 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/4b06ca3c-fc4a-479f-8f20-d0d513a1969a/tool-results/b431hftho.txt"
}
```

```
1	schema_version: 2
2	id: 001746-liu-2026-01
3	dataset:
4	  archive: dandi
5	  id: '001746'
6	  version: 0.260825.0222
7	  doi: 10.48324/dandi.001746/0.260825.0222
8	paper: doi:10.1038/s41556-026-02009-4
9	date: 2026-11-03
10	entry: 001746-liu-2026
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
[... 782 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/4b06ca3c-fc4a-479f-8f20-d0d513a1969a/tool-results/b431hftho.txt",
 "offset": 803
}
```

```
803	      The adopted sag ratio reading was dropped: the outcome is the one that holds under both of the criterion''s
804	      sag readings.'
805	  - claim: fig3e-phase-peak-index
806	    agrees: true
807	    outcome: blocked
808	    reason: 'Blocked (methods_underspecified). VEN median is lowest only under the first-AP reading, not
809	      under the median-over-APs reading; Dunn separates VENs from only 2 of 5 groups. aic.phase_index
810	      returns 0 when no AIS peak or shoulder is found: on synthetic APs a monophasic AP scores 0.0, a
811	      biphasic AP 0.27 and a shoulder AP 0.42, so the APs least like a saddle get the index of the most
812	      saddle-like. The Methods'' "point with the lowest derivative value" does not support 0. This rule
813	      produces the 0.0 medians of L2/3 IT and IT RORB under the median reading, which is why that reading
814	      fails. It invalidates the automatic index. Its agreement with the hand-read values is poor (Spearman
815	      0.55 first AP, 0.09 median). The code''s hand-read values would reproduce it (all Dunn p ≤ 0.001),
816	      which is a deviation from the automatic reading.'
817	    response: Outcome changed to partially reproduced. With no AIS peak or shoulder the AIS value is now
818	      the lowest dV/dt of the rising phase (the Methods' passage), so such an AP is the least saddle-like
819	      (synthetic monophasic AP 0.81), with a variant that leaves such APs out and the per-group fraction
820	      of such APs shown. Most 0.0 values came from thresholds placed at the AP peak (The AP threshold
821	      search was corrected), now corrected; such APs are on average at most 3% of a group's APs, and the first AP of up to 5 of a group's cells (corrected in round 2). Under both AP readings
822	      and both corrections the VEN median is now the lowest and Dunn's test separates VENs from L5 ET
[... 395 more lines not kept]
```

**Agent**

I've read the attempt record; now the dataset entry and the reports.

**Agent calls Bash**

```bash
cd  python -c "
import json;d=json.load(open('targets/dandisets.json'));print(list(d.keys())[:5])
def walk(x):
  if isinstance(x,dict):
    if any(str(v)=='001746' for v in x.values()): print(json.dumps(x,indent=1)); return
    for v in x.values(): walk(v)
  elif isinstance(x,list):
    for v in x: walk(v)
walk(d)"; wc -w transcripts/001746/*-report.md; ls questions/ | grep 1746
```

```
['schema_version', 'generated', 'source', 'counts', 'targets']
{
 "dandiset": "001746",
 "name": "Electrophysiological Dataset of Patch-seq Recording in non-Human Primate Anterior Insular Cortex",
 "published_version": "0.260825.0222",
 "asset_count": 462,
 "size_gb": 14.74,
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
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/001746; for f in author-report.md answer-report.md author-answers-report.md author-revise-1-report.md author-revise-2-report.md author-revise-3-report.md; do echo "== $f"; cat $f; done
```

```
== author-report.md
I finished steps 1 to 6: the entry is locked, checked and run, the attempt record is written, and the handover is built. Nothing is committed.

## 1. Outcomes (33 claims: the file's 32 plus one link claim I added)

| Claim | Outcome |
|---|---|
| patchseq-cell-table-link | Partially reproduced |
| morph-table-link (added) | Reproduced |
| patchseq-sample | Partially reproduced (10 subjects, not 12) |
| patchseq-mapping | Partially reproduced (inhibitory 30, not 34) |
| fig2a-subclass-counts | Partially reproduced (L5 IT FEZF2 125, not 143) |
| ven-map-et-ct | Reproduced (14 and 15) |
| fig6f-ven-subtype-mapping | Partially reproduced (12 VEN-L, not 10) |
| fig2d-l23it-small-tau | Reproduced, rests on an assumption |
| fig2f-l23it-narrow-ap | Partially reproduced (second-lowest median) |
| supp11-rm-itrorb-l6pc | Partially reproduced, rests on an assumption |
| supp11-l5it-threshold-latency | Reproduced |
| supp11-ven-broad-ap | Not reproduced |
| ven-firing-rate-variability | Not reproduced |
[... 167 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/001746; for f in verifier-1-report.md verifier-2-report.md verifier-3-report.md; do echo "== $f"; cat $f; done; head -c 6000 ../../claims/001746/*.yaml; cat ../../questions/001746.yaml | head -60
```

```
<persisted-output>
Output too large (32.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/4b06ca3c-fc4a-479f-8f20-d0d513a1969a/tool-results/b2spxzkbs.txt

Preview (first 2KB):
== verifier-1-report.md
**A. Outcomes** (33 claims in the claims file: 24 tested on this dandiset or blocked here, 9 with data elsewhere)

| Claim | My outcome | Reason |
|---|---|---|
| patchseq-cell-table-link | reproduced | All 462 rows find a file. Cell IDs agree 462/462 and subjects 461/462. Within 10% of the xlsx: half-width 89.5%, amplitude 90.2%, rate 98.9% (cell 12). The one subject mismatch is row 235 (n172, Mfa180730), which repeats row 110's file name; the one file no row names (s172, Mfa180730) is almost certainly the file it meant (cell 11). By the letter "labels disagree" fails on that row. |
| morph-table-link | reproduced | 166/166 rows match a file; clusters agree 163/165 = 98.8% (cell 56). |
| patchseq-sample | partially_reproduced | 462 neurons (457 distinct recordings), within tolerance. 10 subjects against 12 ± 1.2 fails; all male (cell 15). |
| patchseq-mapping | partially_reproduced | 278/307, 248/273, 17/18 and 17/17 are within tolerance. Inhibitory 30 against 34 ± 3.4 is not (cell 17). The 30% mapping-rate filter removes nothing (minimum 0.40). |
| fig2a-subclass-counts | partially_reproduced | 5 of the 6 judged counts are within tolerance (L6 IT and L6b judged together, 14/14). L5 IT FEZF2 is 125 against 143 ± 14.3 (cell 19). |
| ven-map-et-ct | reproduced | 14 VENs in DSG2 and 15 in COL24A1, none in other clusters (cell 21). |
| fig6f-ven-subtype-mapping | partially_reproduced | No VEN-L is in COL24A1 and no VEN-S in DSG2, and VEN-S is 10 (11 ± 1.1). VEN-L is 12 against 10 ± 1, outside tolerance (cell 23). |
| fig2d-l23it-small-tau | reproduced (marginal) | Methods tau median is lowest (32.7 ms). Against the pooled five, p = 0.0106: q = 0.023 in the 20-feature family, and between 0.0106 and 0.0514 in the deciding 39-feature fa
[... 2 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/4b06ca3c-fc4a-479f-8f20-d0d513a1969a/tool-results/b2spxzkbs.txt"
}
```

```
1	== verifier-1-report.md
2	**A. Outcomes** (33 claims in the claims file: 24 tested on this dandiset or blocked here, 9 with data elsewhere)
3	
4	| Claim | My outcome | Reason |
5	|---|---|---|
6	| patchseq-cell-table-link | reproduced | All 462 rows find a file. Cell IDs agree 462/462 and subjects 461/462. Within 10% of the xlsx: half-width 89.5%, amplitude 90.2%, rate 98.9% (cell 12). The one subject mismatch is row 235 (n172, Mfa180730), which repeats row 110's file name; the one file no row names (s172, Mfa180730) is almost certainly the file it meant (cell 11). By the letter "labels disagree" fails on that row. |
7	| morph-table-link | reproduced | 166/166 rows match a file; clusters agree 163/165 = 98.8% (cell 56). |
8	| patchseq-sample | partially_reproduced | 462 neurons (457 distinct recordings), within tolerance. 10 subjects against 12 ± 1.2 fails; all male (cell 15). |
9	| patchseq-mapping | partially_reproduced | 278/307, 248/273, 17/18 and 17/17 are within tolerance. Inhibitory 30 against 34 ± 3.4 is not (cell 17). The 30% mapping-rate filter removes nothing (minimum 0.40). |
10	| fig2a-subclass-counts | partially_reproduced | 5 of the 6 judged counts are within tolerance (L6 IT and L6b judged together, 14/14). L5 IT FEZF2 is 125 against 143 ± 14.3 (cell 19). |
11	| ven-map-et-ct | reproduced | 14 VENs in DSG2 and 15 in COL24A1, none in other clusters (cell 21). |
12	| fig6f-ven-subtype-mapping | partially_reproduced | No VEN-L is in COL24A1 and no VEN-S in DSG2, and VEN-S is 10 (11 ± 1.1). VEN-L is 12 against 10 ± 1, outside tolerance (cell 23). |
13	| fig2d-l23it-small-tau | reproduced (marginal) | Methods tau median is lowest (32.7 ms). Against the pooled five, p = 0.0106: q = 0.023 in the 20-feature family, and between 0.0106 and 0.0514 in the deciding 39-feature family. The upper end is reached only if none of the 19 features not computed has p < 0.0106, while 7 of the 20 computed ones do. First-sweep tau gives q ≤ 0.005 (cell 27). |
14	| fig2f-l2
[... 261 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,200p tools/readme_row.py; grep -n "001746\|(+" README.md | head; grep -n "data:\|where:\|^- id:\|kind: link" claims/001746/*.yaml | head -80
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
[... 133 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 40,108p claims/001746/*.yaml; cat transcripts/001746/claims-check-report.md | head -60
```

```
#    (Exc FEZF2 SMYD1, cluster 12, Exc HPCAL1 KANK4). Cluster 8 cells typed PC (canonical L5/6
#    CT) are left out of the six Fig. 2 groups. For the VEN subtypes (calFDR_VENsubtype_ephysio.m,
#    calFDR_ephysCmp_VEN_vs_L56CT.m), VEN-L is a VEN in cluster 16, VEN-S a VEN in cluster 8, and
#    L5/6 CT a PC in cluster 8. Tallied here from the xlsx, the six groups hold 30, 22, 122, 29,
#    17 and 13 cells; the Fig. 2 legend gives 30, 17, 119, 22, 16 and 13.
#  - calFDR_ephsio.m (Supplementary Table 2), for each feature a two-sided Wilcoxon rank-sum test
#    (ranksum) of each subclass against the other five pooled and of each pair of subclasses,
#    with Benjamini-Hochberg FDR (mafdr BHFDR) over the 39 features within each comparison.
#    createEphysioDataSupplTable.m (Supplementary Table 1) gives the mean and s.d. per subclass.
#    Fig2D_ephyFeatCmp.m plots tau (excluding values of 1 ms or less), input resistance, and AP
#    half-width (excluding values outside 1 to 5 ms, as "unreasonable").
#  - Fig3e_plotBoxplot_PeakIdx_cellTypes.m plots per-cell phase peak indices from
#    PeakIdx_Fig5e.xlsx (30, 22, 122, 29, 17, 13 cells) and runs no test. In PatchAnaLab,
#    calPhaseHeightIdx.m takes the sweep with the maximal firing rate, overlays the phase plots of
#    its APs (dV/dt smoothed over 5 samples) and has the user click the AIS peak and the SD peak;
#    the index is (SD - AIS)/(SD + AIS). The index was therefore read by hand.
#  - Fig4itop_plot_PhasePeakIdx_vs_AISd.m loads 62 neurons' AIS distances and peak indices
#    (NeuronPeakIdx_summary.mat), averages the indices in 10 um bins of AIS distance (0 to 200
#    um) and fits a line to the bin means against the bins' left edges.
#  - extFig9ad_plotVENsubtypeAP_Cmp.m loads VENsubtype_APs.mat, AP half-widths and amplitudes of
[... 70 more lines not kept]
```

**Agent**

I have everything I need. Writing the note now.

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/001746-liu-2026-01.md",
 "content": "# 001746, Liu et al. 2026\n\nFour claims reproduced, eight partially (one on an assumption), one not\nreproduced and six blocked, three as methods underspecified and three for\nmissing data; the three claims that also use inputs from outside the dataset\n(the code's morphology table and AIS distances, the 10x transcriptomes in GEO)\nare counted apart: one reproduced, one not reproduced and one blocked as\nmethods underspecified. Of the 33 claims, two are link checks, both reproduced,\nthe cell table's on an assumption, and one of them, `morph-table-link`, was\nadded by the author; nine have their data in other dandisets or archives and\nare blocked as other. The first verification round agreed with 29 of the 33\noutcomes as they stood and the second with 30, disagreeing on\n`fig3e-phase-peak-index`, `fig3d-saddle-phase-plane` and\n`fig4i-peak-index-ais-distance-real`; the author proposed blocking all three,\nand a third round, which reviewed only these, agreed with all of them. It pins\nversion 0.260825.0222, the only published version; the draft lists the same\nfiles, and the paper cites none. The paper, Liu, Huang, Shen, Shao, Jing et\nal., \"An atlas of primate insular cortex reveals a signal-processing strategy\nin von Economo neurons\" in Nature Cell Biology, profiles neurons of the\nanterior insular cortex (AIC) of macaques with Patch-seq, 462 with intrinsic\nproperties, 166 with reconstructed morphologies and 307 with transcriptomes\nmapped to a scRNA-seq atlas, and reports the electrophysiology of the\ntranscriptomic subclasses (Fig. 2, Supplementary Fig. 11), the phase peak index\nof von Economo neurons (VENs) (Fig. 3), their broader APs against L5 PCs and the\nindex against AIS distance (Fig. 4), the VEN subtypes (Fig. 6, Extended Data\nFig. 9) and the correlation of tau and RNA distances (Fig. 7). The claims were\nwritten from the version of record in Europe PMC (PMC13457102) without a PDF,\nthe Supplementary Information or the Source Data, and from the paper's code\n(AIC_proj at commit 44cd8a6 and PatchAnaLab 1.0); the check made ten\ncorrections and left three points open. Reproduced are `ven-map-et-ct` (14\nVENs in Exc FEZF2 DSG2 and 15 in Exc FEZF2 COL24A1), `fig2d-l23it-small-tau`\n(median 32.7 ms, FDR 0.034 over the 39-feature family),\n`supp11-l5it-threshold-latency`, `supp9-venl-more-distinct-from-ct` (6 of the\n39 features against 0) and `morph-more-distinct-than-ephys` (445 of 1,185\nmorphological tests against 120 of 420 physiological). Partial are\n`patchseq-sample` (10 subjects against 12), `patchseq-mapping` (30 inhibitory\nagainst 34), `fig2a-subclass-counts` (L5 IT FEZF2 125 against 143),\n`fig6f-ven-subtype-mapping` (12 VEN-L against 10), `fig2f-l23it-narrow-ap`\n(the median is the second lowest), `supp11-rm-itrorb-l6pc` (IT RORB FDR 0.087),\n`supp11-ven-broad-ap` (the VEN median is the highest, 3.03 against 2.98 ms,\nwith no significant reading) and `l5et-vs-l5it-sag-rm-rate`, which takes the\noutcome that holds under both sag readings and would be blocked if it inherits\nthe rule of `supp11-l5et-deep-sag`. Not reproduced are\n`ven-firing-rate-variability` (p = 0.092) and `fig7c-tau-rna-distance` (r =\n0.053 against 0.53). `supp11-l5et-deep-sag` is blocked because L5 ET has the\nlargest sag ratio and the smallest sag value of the six groups.\n`fig3e-phase-peak-index` is blocked because the automatic index that stands in\nfor the hand-placed peaks does not measure the saddle shape at the noise of\nthese recordings and its outcome turns on the prominence guard (0.02 gives not\nreproduced, 0.05 and 0.10 partially), and `fig3d` and `fig4i` follow it; the\ncode's hand-read values give the paper's results, and blocking goes beyond the\ncriterion's letter, which a reader is asked to confirm. The three claims on\nrecordings without RNA are blocked for missing data. The author's first run\ngave the link partially reproduced, `fig4i` blocked as metadata insufficient\nand `fig7c` blocked as too large. The author asked no questions of a reader, so\nthe answer and author-answers runs changed nothing. Round 1 disagreed with four\noutcomes and found that the phase index gave 0, the most saddle-like value,\nto an AP with no AIS peak or shoulder, that the 39-feature FDR could only be\nbounded as 19 features are defined nowhere, that `fig4i` was not run, that\ndevice was never crossed with group and that `fig7c` had no notebook cell; in\nreply a bug that put the AP threshold at the peak in 28 HEKA files was fixed,\nthe 19 features took the code's table values, `Ext.h5ad` was streamed from GEO,\n`fig4i` was run, a device crosstab was added, and seven outcomes changed. Round\n2 found that the shoulder branch, which reads 195 of the 237 first APs, places\nthe AIS value next to the SD peak under noise, that the prominence guard, the\nrow 235 reading and the sag rule were unflagged assumptions, and sentences the\noutputs did not support (the \"at most 3%\" figure, an unprinted experiment\ndescription, a run time and the first 5 GB of the archive); in reply these\nwere flagged or corrected, the Methods' selection of the 500 genes became the\nmain gene set (r 0.105 became 0.053), and three questions for a reader were\nfiled in `questions/001746.yaml`, after the reader's run. As the schema does\nnot allow `assumed` on a blocked outcome, the flag was removed from the three\nblocked claims. The author's work took about 40 minutes; the notebook ran in\n166 s at first, 246 s after the author-answers run, 7.5 min after round 1, 6.5\nminutes after round 2 (one full run in that revision took 43 minutes, 37 of\nthem for the GEO download) and 319 s at the end. Untracked dotfiles and\n`scripts` at the repository root, sandbox device mounts, were left alone.\n\nThe files carry no cell type, VEN subtype or transcriptomic type, although the\ndescription says the recordings are annotated with transcriptomic cell types;\nthese labels exist only in the code's `metaInfo_ephysio_patchSeq.csv`, matched\nby file name. Five pairs of files hold identical voltage data in every sweep\nunder different cell IDs, four of them under different subjects, and the cell\ntable gives the pair B289 and n175 different clusters (16 and 8), so the 462\nfiles hold 457 distinct recordings. The cell table names the file of cell n172\non two rows, the second with subject Mfa180730, and has no row for the file of\ncell s172. The dandiset holds 10 subjects where the paper says 12 animals, and\nonly the Patch-seq cells: the recordings without RNA (281 VENs and 306 L5 PCs\nof Fig. 4a-c, 85 VEN-L and 41 VEN-S of Extended Data Fig. 9c,d and\nSupplementary Table 8) are not in it, and the paper does not say where they\nare. The Methods put the Patch-seq recordings on a HEKA amplifier, but 139\nfiles with a transcriptomic type have the device AXON recording system; the\ndevice follows the recording year, AP half-width and tau are longer in the Axon\nfiles in every group (half-width 3.13 against 2.08 ms, tau 41 against 26 ms in\nthe paper's feature table), and the narrow APs and short tau of L2/3 IT HPCAL1\nare not significant within either set. Every file has the same placeholder\nsession start (2018-01-01 01:00 +08:00), and two session IDs carry the date of\nanother subject. The stimulus series are stated in amperes but hold pA, with a\nstarting time of NaN, and four Axon files are sampled at 25 kHz like the HEKA\nfiles and one HEKA file at 50 kHz. The 62 AIS distances and peak indices of\nFig. 4i carry no cell IDs and match none of the per-cell tables. Of the code,\nthe feature table holds the first-sweep tau where the Methods average over all\nhyperpolarizing sweeps (the Methods' tau is 26% longer), its Fig. 2 groups hold\n30, 22, 122, 29, 17 and 13 cells where the legend gives 30, 17, 119, 22, 16 and\n13, and the 10x cluster labels in GEO differ in their first marker from the\ncell table's for clusters 4, 9, 11 and 14. Questions are put to the paper's\nauthors: whether row 235 is the row of s172; which measure \"a deeper sag\"\nuses; how 19 of the 39 features are computed; and which APs were read for the\nphase peak index and how the AIS peak was placed when there was no separate\nmaximum.\n\nThe author's points on the protocol: taken literally, the link criterion fails\nover one row's subject, a duplicate row no analysis uses, which would block 18\ndependent claims; some criteria define only reproduced, and partially\nreproduced was used where the effect held in part; the supplement was under\n`paper/` for the author but not for the reader, and the protocol does not\ncover an author with more text than the reader; no `blocked_by` reason fits a\nclaim tested under another dandiset's claims file, so `other` was used; the\nschema forbids `inferred` on link claims and an author-added link has no quote,\nso the provenance was put in the criterion; it is not said whether the header\ntable may give outcomes; and \"count each recording once\" does not say what to\ndo when the two copies carry different labels, so both files were kept and the\npair reported.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  git status --short; grep -nE "—|rather|\*\*" docs/pilot-notes/001746-liu-2026-01.md; wc -w docs/pilot-notes/001746-liu-2026-01.md
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
?? docs/pilot-notes/001746-liu-2026-01.md
?? scripts
1479 docs/pilot-notes/001746-liu-2026-01.md
```

**Agent**

I wrote `docs/pilot-notes/001746-liu-2026-01.md` and changed no other file. Nothing is committed. The note is below.

# 001746, Liu et al. 2026

Four claims reproduced, eight partially (one on an assumption), one not
reproduced and six blocked, three as methods underspecified and three for
missing data; the three claims that also use inputs from outside the dataset
(the code's morphology table and AIS distances, the 10x transcriptomes in GEO)
are counted apart: one reproduced, one not reproduced and one blocked as
methods underspecified. Of the 33 claims, two are link checks, both reproduced,
the cell table's on an assumption, and one of them, `morph-table-link`, was
added by the author; nine have their data in other dandisets or archives and
are blocked as other. The first verification round agreed with 29 of the 33
outcomes as they stood and the second with 30, disagreeing on
`fig3e-phase-peak-index`, `fig3d-saddle-phase-plane` and
`fig4i-peak-index-ais-distance-real`; the author proposed blocking all three,
and a third round, which reviewed only these, agreed with all of them. It pins
version 0.260825.0222, the only published version; the draft lists the same
files, and the paper cites none. The paper, Liu, Huang, Shen, Shao, Jing et
al., "An atlas of primate insular cortex reveals a signal-processing strategy
in von Economo neurons" in Nature Cell Biology, profiles neurons of the
anterior insular cortex (AIC) of macaques with Patch-seq, 462 with intrinsic
properties, 166 with reconstructed morphologies and 307 with transcriptomes
mapped to a scRNA-seq atlas, and reports the electrophysiology of the
transcriptomic subclasses (Fig. 2, Supplementary Fig. 11), the phase peak index
of von Economo neurons (VENs) (Fig. 3), their broader APs against L5 PCs and the
index against AIS distance (Fig. 4), the VEN subtypes (Fig. 6, Extended Data
Fig. 9) and the correlation of tau and RNA distances (Fig. 7). The claims were
written from the version of record in Europe PMC (PMC13457102) without a PDF,
the Supplementary Information or the Source Data, and from the paper's code
(AIC_proj at commit 44cd8a6 and PatchAnaLab 1.0); the check made ten
corrections and left three points open. Reproduced are `ven-map-et-ct` (14
VENs in Exc FEZF2 DSG2 and 15 in Exc FEZF2 COL24A1), `fig2d-l23it-small-tau`
(median 32.7 ms, FDR 0.034 over the 39-feature family),
`supp11-l5it-threshold-latency`, `supp9-venl-more-distinct-from-ct` (6 of the
39 features against 0) and `morph-more-distinct-than-ephys` (445 of 1,185
morphological tests against 120 of 420 physiological). Partial are
`patchseq-sample` (10 subjects against 12), `patchseq-mapping` (30 inhibitory
against 34), `fig2a-subclass-counts` (L5 IT FEZF2 125 against 143),
`fig6f-ven-subtype-mapping` (12 VEN-L against 10), `fig2f-l23it-narrow-ap`
(the median is the second lowest), `supp11-rm-itrorb-l6pc` (IT RORB FDR 0.087),
`supp11-ven-broad-ap` (the VEN median is the highest, 3.03 against 2.98 ms,
with no significant reading) and `l5et-vs-l5it-sag-rm-rate`, which takes the
outcome that holds under both sag readings and would be blocked if it inherits
the rule of `supp11-l5et-deep-sag`. Not reproduced are
`ven-firing-rate-variability` (p = 0.092) and `fig7c-tau-rna-distance` (r =
0.053 against 0.53). `supp11-l5et-deep-sag` is blocked because L5 ET has the
largest sag ratio and the smallest sag value of the six groups.
`fig3e-phase-peak-index` is blocked because the automatic index that stands in
for the hand-placed peaks does not measure the saddle shape at the noise of
these recordings and its outcome turns on the prominence guard (0.02 gives not
reproduced, 0.05 and 0.10 partially), and `fig3d` and `fig4i` follow it; the
code's hand-read values give the paper's results, and blocking goes beyond the
criterion's letter, which a reader is asked to confirm. The three claims on
recordings without RNA are blocked for missing data. The author's first run
gave the link partially reproduced, `fig4i` blocked as metadata insufficient
and `fig7c` blocked as too large. The author asked no questions of a reader, so
the answer and author-answers runs changed nothing. Round 1 disagreed with four
outcomes and found that the phase index gave 0, the most saddle-like value,
to an AP with no AIS peak or shoulder, that the 39-feature FDR could only be
bounded as 19 features are defined nowhere, that `fig4i` was not run, that
device was never crossed with group and that `fig7c` had no notebook cell; in
reply a bug that put the AP threshold at the peak in 28 HEKA files was fixed,
the 19 features took the code's table values, `Ext.h5ad` was streamed from GEO,
`fig4i` was run, a device crosstab was added, and seven outcomes changed. Round
2 found that the shoulder branch, which reads 195 of the 237 first APs, places
the AIS value next to the SD peak under noise, that the prominence guard, the
row 235 reading and the sag rule were unflagged assumptions, and sentences the
outputs did not support (the "at most 3%" figure, an unprinted experiment
description, a run time and the first 5 GB of the archive); in reply these
were flagged or corrected, the Methods' selection of the 500 genes became the
main gene set (r 0.105 became 0.053), and three questions for a reader were
filed in `questions/001746.yaml`, after the reader's run. As the schema does
not allow `assumed` on a blocked outcome, the flag was removed from the three
blocked claims. The author's work took about 40 minutes; the notebook ran in
166 s at first, 246 s after the author-answers run, 7.5 min after round 1, 6.5
minutes after round 2 (one full run in that revision took 43 minutes, 37 of
them for the GEO download) and 319 s at the end. Untracked dotfiles and
`scripts` at the repository root, sandbox device mounts, were left alone.

The files carry no cell type, VEN subtype or transcriptomic type, although the
description says the recordings are annotated with transcriptomic cell types;
these labels exist only in the code's `metaInfo_ephysio_patchSeq.csv`, matched
by file name. Five pairs of files hold identical voltage data in every sweep
under different cell IDs, four of them under different subjects, and the cell
table gives the pair B289 and n175 different clusters (16 and 8), so the 462
files hold 457 distinct recordings. The cell table names the file of cell n172
on two rows, the second with subject Mfa180730, and has no row for the file of
cell s172. The dandiset holds 10 subjects where the paper says 12 animals, and
only the Patch-seq cells: the recordings without RNA (281 VENs and 306 L5 PCs
of Fig. 4a-c, 85 VEN-L and 41 VEN-S of Extended Data Fig. 9c,d and
Supplementary Table 8) are not in it, and the paper does not say where they
are. The Methods put the Patch-seq recordings on a HEKA amplifier, but 139
files with a transcriptomic type have the device AXON recording system; the
device follows the recording year, AP half-width and tau are longer in the Axon
files in every group (half-width 3.13 against 2.08 ms, tau 41 against 26 ms in
the paper's feature table), and the narrow APs and short tau of L2/3 IT HPCAL1
are not significant within either set. Every file has the same placeholder
session start (2018-01-01 01:00 +08:00), and two session IDs carry the date of
another subject. The stimulus series are stated in amperes but hold pA, with a
starting time of NaN, and four Axon files are sampled at 25 kHz like the HEKA
files and one HEKA file at 50 kHz. The 62 AIS distances and peak indices of
Fig. 4i carry no cell IDs and match none of the per-cell tables. Of the code,
the feature table holds the first-sweep tau where the Methods average over all
hyperpolarizing sweeps (the Methods' tau is 26% longer), its Fig. 2 groups hold
30, 22, 122, 29, 17 and 13 cells where the legend gives 30, 17, 119, 22, 16 and
13, and the 10x cluster labels in GEO differ in their first marker from the
cell table's for clusters 4, 9, 11 and 14. Questions are put to the paper's
authors: whether row 235 is the row of s172; which measure "a deeper sag"
uses; how 19 of the 39 features are computed; and which APs were read for the
phase peak index and how the AIS peak was placed when there was no separate
maximum.

The author's points on the protocol: taken literally, the link criterion fails
over one row's subject, a duplicate row no analysis uses, which would block 18
dependent claims; some criteria define only reproduced, and partially
reproduced was used where the effect held in part; the supplement was under
`paper/` for the author but not for the reader, and the protocol does not
cover an author with more text than the reader; no `blocked_by` reason fits a
claim tested under another dandiset's claims file, so `other` was used; the
schema forbids `inferred` on link claims and an author-added link has no quote,
so the provenance was put in the criterion; it is not said whether the header
table may give outcomes; and "count each recording once" does not say what to
do when the two copies carry different labels, so both files were kept and the
pair reported.

## End of run

15 turns, 2 minutes, $1.29 at API prices, result: success.
