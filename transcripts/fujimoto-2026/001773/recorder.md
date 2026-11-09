# 001773 · recorder · run 41688593846

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; ls claims/001773 transcripts/001773; python tools/readme_row.py 001773; cat attempts/001773-fujimoto-2026-01.yaml
```

```
<persisted-output>
Output too large (59.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/ab98eab5-639b-4e59-a026-279b00279397/tool-results/bl9k12j6a.txt

Preview (first 2KB):
docs/pilot-notes/001683-gao-2026-01.md
docs/pilot-notes/001687-xiao-2026-01.md
docs/pilot-notes/001746-liu-2026-01.md
docs/pilot-notes/001676-skromne-carrasco-2026-01.md
docs/pilot-notes/001702-chaunsali-2025-01.md
claims/001773:
10.1038-s41593-026-02301-4.yaml

transcripts/001773:
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
author-revise-1.md
[... 51 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for f in 001683-gao-2026-01 001687-xiao-2026-01 001746-liu-2026-01 001676-skromne-carrasco-2026-01 001702-chaunsali-2025-01; do echo "=== $f"; cat docs/pilot-notes/$f.md; done; head -n 5 docs/pilot-notes/001754-knierim-2000-02.md
```

```
<persisted-output>
Output too large (44.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/ab98eab5-639b-4e59-a026-279b00279397/tool-results/bgdxi8y38.txt

Preview (first 2KB):
=== 001683-gao-2026-01
# 001683, Gao et al. 2026

Seven claims reproduced (three on an assumption), five partially (two on an
assumption), eight not reproduced (four on an assumption) and two blocked, one
as methods underspecified and one for missing data. All 22 claims are on the
dandiset. The first verification round agreed with 19 of the 22 outcomes as
they stood and the second with all 22, and nothing was proposed after the
second, so there was no third round. It pins version 0.260109.2104, the only
published version; the paper cites none. The paper, Gao, Frake, Durand and He,
"Transcranial Focused Ultrasound Stimulation Targeting White Matter Inhibits
Seizures in a Rat Model of Epilepsy" in IEEE Transactions on Neural Systems and
Rehabilitation Engineering, applies tFUS to the corpus callosum of rats with
seizures induced by 4-AP in right S1, 10 tFUS and 6 sham, and reports the
seizure metrics of the sham group (Fig. 2) and of both groups (Fig. 3), band
power and the asymmetry index (AI) of the EEG (Fig. 4, Figures S4 and S5), the
[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/ab98eab5-639b-4e59-a026-279b00279397/tool-results/bgdxi8y38.txt"
}
```

```
1	=== 001683-gao-2026-01
2	# 001683, Gao et al. 2026
3	
4	Seven claims reproduced (three on an assumption), five partially (two on an
5	assumption), eight not reproduced (four on an assumption) and two blocked, one
6	as methods underspecified and one for missing data. All 22 claims are on the
7	dandiset. The first verification round agreed with 19 of the 22 outcomes as
8	they stood and the second with all 22, and nothing was proposed after the
9	second, so there was no third round. It pins version 0.260109.2104, the only
10	published version; the paper cites none. The paper, Gao, Frake, Durand and He,
11	"Transcranial Focused Ultrasound Stimulation Targeting White Matter Inhibits
12	Seizures in a Rat Model of Epilepsy" in IEEE Transactions on Neural Systems and
13	Rehabilitation Engineering, applies tFUS to the corpus callosum of rats with
14	seizures induced by 4-AP in right S1, 10 tFUS and 6 sham, and reports the
15	seizure metrics of the sham group (Fig. 2) and of both groups (Fig. 3), band
16	power and the asymmetry index (AI) of the EEG (Fig. 4, Figures S4 and S5), the
17	evoked potentials and phase lag index (PLI) of all 23 rats before 4-AP (Fig.
18	5) and the PLI of the epileptic rats (Fig. 6, Figure S7). The claims were
19	written from the NIH author manuscript in Europe PMC (PMC12848950) and its
20	supplement, without a PDF of the main paper, so the significance marks inside
[... 604 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/001773-fujimoto-2026-01.yaml; wc -c claims/001773/* transcripts/001773/*report.md; python -c "
import json;d=json.load(open('targets/dandisets.json'))
it=d if isinstance(d,list) else d.get('dandisets',d)
for e in (it if isinstance(it,list) else it.values()):
  if '001773' in json.dumps(e): print(json.dumps(e,indent=1))
"
```

```
<persisted-output>
Output too large (273.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/ab98eab5-639b-4e59-a026-279b00279397/tool-results/b1jsj9kmx.txt

Preview (first 2KB):
schema_version: 2
id: 001773-fujimoto-2026-01
dataset:
  archive: dandi
  id: "001773"
  version: 0.260416.1939
  doi: 10.48324/dandi.001773/0.260416.1939
paper: doi:10.1038/s41593-026-02301-4
date: 2026-11-03
entry: 001773-fujimoto-2026
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -l attempts/001773-fujimoto-2026-01.yaml claims/001773/* transcripts/001773/*report.md; grep -n "^[a-z_]*:" attempts/001773-fujimoto-2026-01.yaml; grep -n "^- claim:\|^  outcome:\|^  assumed" attempts/001773-fujimoto-2026-01.yaml
```

```
1003 attempts/001773-fujimoto-2026-01.yaml
   940 claims/001773/10.1038-s41593-026-02301-4.yaml
    15 transcripts/001773/answer-report.md
    33 transcripts/001773/author-answers-report.md
    35 transcripts/001773/author-report.md
    19 transcripts/001773/author-revise-1-report.md
    23 transcripts/001773/author-revise-2-report.md
    26 transcripts/001773/claims-check-report.md
    40 transcripts/001773/claims-report.md
    64 transcripts/001773/verifier-1-report.md
    45 transcripts/001773/verifier-2-report.md
  2243 total
1:schema_version: 2
2:id: 001773-fujimoto-2026-01
3:dataset:
8:paper: doi:10.1038/s41593-026-02301-4
9:date: 2026-11-03
10:entry: 001773-fujimoto-2026
11:provenance:
22:outcomes:
[... 77 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/001773-fujimoto-2026-01.yaml",
 "offset": 40,
 "limit": 470
}
```

```
40	- claim: ed1-monkey-d-no-change
41	  outcome: not_reproduced
42	  notebook: reproduce_fujimoto_2026.ipynb
43	  output: claim:ed1-monkey-d-no-change
44	  notes: By the criterion's test, a one-way ANOVA of monkey D's 120 bins on condition, movement
45	    does not differ (0.383 pre, 0.267 post, F(1,118) = 1.86, P = 0.175) but foraging does (11 of 60
46	    bins before, 3 of 60 after, 0.183 to 0.050, F(1,118) = 5.32, P = 0.023; Fisher exact P =
47	    0.043). The paper reports no test for monkey D (its Extended Data Fig. 1 legend analyses only
48	    N and T), so the test is the claims file's reading of the Methods applied to one animal. The
49	    deposited FigE1 script (135 lines) runs its only test calls, anovan (lines 18 and 19) and
50	    multcompare (24 and 26), on the rows of group 1 (N and T); monkey D's rows (monkey 3, group 2)
51	    enter only the means, standard errors and sample sizes of lines 35 to 125. The deposited script
52	    therefore runs no test for monkey D. The change in monkey D is a decrease, opposite to the
53	    increase of the DBS animals.
54	  deviations:
55	  - The paper reports no test for monkey D; the criterion applies the Methods' ANOVA to its bins.
56	- claim: fig2a-cb-fa-increase
57	  outcome: reproduced
58	  notebook: reproduce_fujimoto_2026.ipynb
59	  output: claim:fig2a-cb-fa-increase
[... 450 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat transcripts/001773/author-report.md transcripts/001773/answer-report.md transcripts/001773/author-answers-report.md transcripts/001773/author-revise-1-report.md transcripts/001773/author-revise-2-report.md transcripts/001773/verifier-1-report.md transcripts/001773/verifier-2-report.md
```

```
<persisted-output>
Output too large (29.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/ab98eab5-639b-4e59-a026-279b00279397/tool-results/b1jmpe8f6.txt

Preview (first 2KB):
I've finished steps 1 to 6 for DANDI:001773: the entry `entries/001773-fujimoto-2026/`, the record `attempts/001773-fujimoto-2026-01.yaml`, one reader question in `questions/001773.yaml`, and the handover package. Lock, check and run all pass, and the notebook runs in 32 s from a clean environment. Nothing is committed.

**(1) Outcome per claim** (32 claims)

| Outcome | Claims |
|---|---|
| reproduced (27) | ed1-behavior-increase, fig2a-cb-fa-increase, fig2a-no-change-other-tracts, ed2-cb-both-monkeys, fig2b-mcc-cb-fa-increase, fig3c-cc1-dapi-ratio, ed5-cc1-count-dapi-unchanged, ed6-dacc-ufm-no-oligodendrocyte-change, fig3f-g-ratio-decrease, fig4a-cortical-down-subcortical-up, fig4b-roi-changes-counts (rests on an assumption), fig4-nonsurgical-no-pattern, fig5a-pre-scc-connectivity, fig5b-scc-decreases, fig5b-scc-increases, ed9-control-hemisphere-changes, ed9-no-change-motor-mcc, ed7-decreases-both-monkeys, fig5c-dmn-lim-cen-decrease, fig5c-smn-increase, fig5c-vis-no-change, fig5c-san-rebalanced, fig6a-monkey-d-cb-fa-decrease, fig6b-monkey-d-dacc-cb-decrease, fig6c-monkey-d-cc1-no-change, ed10c-monkey-d-subcortical-decrease, ed10d-monkey-d-roi-changes |
| not reproduced (1) | ed1-monkey-d-no-change: monkey D's foraging falls from 0.183 to 0.050, P = 0.023 |
| blocked (4) | fig4c-network-sorted-reduction (methods_underspecified: the connectome ROIs have no names or network assignment); fig5a-nonsurgical-no-reduction and fig6d-monkey-d-scc-local-increase (data_missing); fig6e-monkey-d-no-network-reduction (methods_underspecified: it was run, its readings disagree, and the criterion says to block in that case) |

**(2) The dataset**
- **Contents:** no NWB. It holds 34 Excel sheets of derived values and 18 MATLAB scripts. I pinned 0.260416.1939, the version
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,60p claims/001773/*.yaml; grep -n "^  - id:\|^- id:\|data:\|where:" claims/001773/*.yaml | head -80; grep -n "001773" -A15 targets/dandisets.json | head -40
```

```
# Claims for Fujimoto, Fujimoto, Elorette et al. (2026), "Deep brain stimulation induces white
# matter remodeling and functional changes to brain-wide networks", Nature Neuroscience,
# doi:10.1038/s41593-026-02301-4, on dandiset 001773.
#
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21, as
# the reader of docs/protocol.md (version pilot-10).
#
# Text read: the version of record (open access, PMC13337501, as served by Europe PMC), main
# text, figure legends, Methods and Extended Data legends 1 to 10, together with the
# Supplementary Information PDF (Supplementary Methods 1 to 7 and Supplementary Tables 1 to 11),
# all in paper/10.1038-s41593-026-02301-4.txt. No PDF of the main article was available; no
# figure needed to be read from one. The Nature "Source Data" files (statistical source data for
# Figs. 2 to 6 and Extended Data Figs. 1, 4, 5, 6, 9 and 10) are cited by the paper but were not
# under paper/ and no claim relies on them.
#
# Code: the paper says its custom MATLAB scripts for the functional MRI analysis are deposited in
# the dandiset itself (Code availability, doi 10.48324/dandi.001773/0.260416.1939). A reader may
# not open the dataset's files, so this code was NOT read. Every criterion below rests on the
# Methods, legends and supplement. Where a detail is named open, the author should check whether
# that code settles it and ask a reader (protocol, author step 6).
[... 89 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 7347,7370p targets/dandisets.json
```

```
"resource_type": null,
     "preprint": false,
     "source": "description"
    }
   ],
   "catalystneuro": []
  },
  {
   "dandiset": "001777",
   "name": "Astrocytes mediate the dopaminergic modulation of tonic GABAergic signaling in Substanta nigra",
   "published_version": "0.260521.2201",
   "asset_count": 412,
   "size_gb": 18.19,
   "data_standards": [
    "Neurodata Without Borders (NWB)"
   ],
   "species": [
    "Mus musculus - House mouse"
   ],
   "approaches": [
[... 4 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/ab98eab5-639b-4e59-a026-279b00279397/tool-results/b1jmpe8f6.txt"
}
```

```
1	I've finished steps 1 to 6 for DANDI:001773: the entry `entries/001773-fujimoto-2026/`, the record `attempts/001773-fujimoto-2026-01.yaml`, one reader question in `questions/001773.yaml`, and the handover package. Lock, check and run all pass, and the notebook runs in 32 s from a clean environment. Nothing is committed.
2	
3	**(1) Outcome per claim** (32 claims)
4	
5	| Outcome | Claims |
6	|---|---|
7	| reproduced (27) | ed1-behavior-increase, fig2a-cb-fa-increase, fig2a-no-change-other-tracts, ed2-cb-both-monkeys, fig2b-mcc-cb-fa-increase, fig3c-cc1-dapi-ratio, ed5-cc1-count-dapi-unchanged, ed6-dacc-ufm-no-oligodendrocyte-change, fig3f-g-ratio-decrease, fig4a-cortical-down-subcortical-up, fig4b-roi-changes-counts (rests on an assumption), fig4-nonsurgical-no-pattern, fig5a-pre-scc-connectivity, fig5b-scc-decreases, fig5b-scc-increases, ed9-control-hemisphere-changes, ed9-no-change-motor-mcc, ed7-decreases-both-monkeys, fig5c-dmn-lim-cen-decrease, fig5c-smn-increase, fig5c-vis-no-change, fig5c-san-rebalanced, fig6a-monkey-d-cb-fa-decrease, fig6b-monkey-d-dacc-cb-decrease, fig6c-monkey-d-cc1-no-change, ed10c-monkey-d-subcortical-decrease, ed10d-monkey-d-roi-changes |
8	| not reproduced (1) | ed1-monkey-d-no-change: monkey D's foraging falls from 0.183 to 0.050, P = 0.023 |
9	| blocked (4) | fig4c-network-sorted-reduction (methods_underspecified: the connectome ROIs have no names or network assignment); fig5a-nonsurgical-no-reduction and fig6d-monkey-d-scc-local-increase (data_missing); fig6e-monkey-d-no-network-reduction (methods_underspecified: it was run, its readings disagree, and the criterion says to block in that case) |
10	
11	**(2) The dataset**
12	- **Contents:** no NWB. It holds 34 Excel sheets of derived values and 18 MATLAB scripts. I pinned 0.260416.1939, the version the paper cites; the latest version, 0.260615.1838, has identical asset ids.
13	- **Match to the paper:** with the scripts' models, almost every F value, partial eta squared and voxel or f
[... 222 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/001773-fujimoto-2026-01.yaml",
 "offset": 510,
 "limit": 500
}
```

```
510	verifications:
511	- date: '2026-11-03'
512	  kind: agent
513	  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
514	  reviewed: Round 1. The handover of the run after the reader's answer on fig4b-roi-changes-counts, the
515	    executed notebook with the conclusion cells and the summary removed, the helper module and the claims
516	    file, with the paper. The verifier queried the archive's asset list and tested the helper's anova
517	    and tukey_kramer on synthetic data against statsmodels and scipy.stats.tukey_hsd. It gave its own
518	    outcome for each claim; all 32 agree with the record.
519	  results:
520	  - claim: ed1-behavior-increase
521	    agrees: true
522	    outcome: reproduced
523	    reason: 'Cell 18: movement F(1,236)=34.61, ηp²=0.128; foraging F=17.35, ηp²=0.068, all within tolerance.
524	      Reading (b) is also P<0.05. Post is higher than pre in both monkeys for both behaviors. Problem
525	      5: the behavior sheet''s legend codes foraging as 2/1, but the values are 0/1, and monkey D''s rows
526	      are labeled group 2; the exact match of F confirms reading foraging as 1 = yes.'
527	    response: No change needed. The legend coding is already recorded as a metadata_error finding and
528	      a deviation.
529	  - claim: ed1-monkey-d-no-change
[... 475 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 60,120p claims/001773/*.yaml
```

```
#   which family it covers is not stated. The reading is all pairwise comparisons among the
#   cells of the three named factors (MATLAB multcompare on the three factor dimensions), with
#   the pre against post pair of each side and tract/ROI read off; the author should check
#   whether the deposited code settles it. Exact P values printed as 0 in Supplementary Table 9
#   are below MATLAB's precision (the legends write P < 1.00 x 10^-300).
# - Where a criterion says "under both readings" (or "all readings") and the readings give
#   different outcomes, the claim is blocked as methods_underspecified with every result shown
#   (protocol, reader step 3).
# - Effect sizes: partial eta squared = SS_effect / (SS_effect + SS_error) (Supplementary
#   Methods 7).
# - The "one-way ANOVA" with monkey as a fixed effect (behavior, CC1/DAPI, g-ratio) is open:
#   (a) condition, monkey and condition x monkey (4 cells; the reported df 1,236, 1,108, 1,696
#   and 1,76 match this: 240, 112, 700 and 80 values less 4); (b) condition and monkey only
#   (df one larger). Both are run.
# - Seed-based fMRI: seed = area 25 of the D99 atlas in the stimulated (N, T) or sham (D)
#   hemisphere, right SCC for the nonsurgical controls. Fisher Z of the Pearson correlation
#   between the seed's mean time series and every voxel (AFNI 3dTcorr1D), each voxel's Z then
#   divided by the session's maximum Z. Whether runs are correlated one by one and averaged
#   (as the connectome analysis does, "For each run ... averaged within condition") or
#   concatenated is not stated: both are readings. Values are voxels in NMT space; "stimulation
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i "checks\|check:\|claims_check\|confirmed" claims/001773/*.yaml | head -30; tail -30 claims/001773/*.yaml
```

```
918:checks:
924:  - Checker. Its 8 "value not found" reports are printing forms it does not match (7.70E-06, 0.999909913, the garbled "9.10 x 10 -1 3", 0.998895555, "6.20 x 10-7", 1.30 x 10 -8, 8.20 x 10 -8, 7.83e-04); each was confirmed by reading in Supplementary Table 9 or the figure legends. No value was changed.
    corrected: Tukey-Kramer
  depends_on:
  - fig5b-scc-decreases
  criterion: The model of fig5b-scc-decreases for monkey D alone, without the monkey term
    (17 ROIs, df 10106). Reproduced when the interaction has P < 0.05 and, of the eight
    comparisons (four ROIs, two sides), exactly the sham-side vmFC and the control-side
    anterior-dorsal insula have P < 0.05. Directions are reported; the paper does not give them.
checks:
- date: 2026-10-21
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Checker. Its 8 "value not found" reports are printing forms it does not match (7.70E-06, 0.999909913, the garbled "9.10 x 10 -1 3", 0.998895555, "6.20 x 10-7", 1.30 x 10 -8, 8.20 x 10 -8, 7.83e-04); each was confirmed by reading in Supplementary Table 9 or the figure legends. No value was changed.
  - Header. The Tukey-Kramer family (all pairwise among the cells of the three factors) was given as fixed by the paper; the paper only says "post hoc Tukey-Kramer test". Marked it as a reading, for the author to check against the deposited code.
  - Header. Removed the claim that type II and type III sums of squares "cannot differ much in these balanced designs"; cell sizes are unequal (voxel counts per tract and side differ).
  - Header. Added the protocol rule that readings giving different outcomes block the claim as methods_underspecified, since the criteria say "under both readings" without saying what follows when they disagree.
  - fig4b-roi-changes-counts. Removed the statistics entry (rank-sum, P < 0.01 Bonferroni); it is the threshold used to count significant ROIs, a method, not a result (protocol, reader step 3). It stays in the crit
[... 12 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/001773-fujimoto-2026-01.md",
 "content": "# 001773, Fujimoto et al. 2026\n\nTwenty-seven claims reproduced (11 on an assumption), none partially, one not\nreproduced and four blocked, two as methods underspecified and two for missing\ndata. All 32 claims are on the dandiset. The first verification round agreed\nwith all 32 outcomes as they stood and so did the second, and nothing was\nproposed after the second, so there was no third round. It pins version\n0.260416.1939, the version the paper cites; the latest version, 0.260615.1838,\nhas identical asset ids. The paper, Fujimoto, Fujimoto, Elorette et al., \"Deep\nbrain stimulation induces white matter remodeling and functional changes to\nbrain-wide networks\" in Nature Neuroscience, implants an SCC-DBS lead in\nmonkeys N and T, stimulated for 6 weeks, and in monkey D, never stimulated, with\nnonsurgical controls B, W and H, and reports home-cage behaviour (Extended Data\nFig. 1), FA of the white matter tracts (Fig. 2, Extended Data Fig. 2),\nCC1-positive oligodendrocytes and EM g-ratios (Fig. 3, Extended Data Figs. 5\nand 6), the whole-brain connectome (Fig. 4), seed connectivity of area 25 by\nROI and network (Fig. 5, Extended Data Figs. 7 and 9) and the same measures in\nmonkey D (Fig. 6, Extended Data Fig. 10). The claims were written from the\nversion of record in Europe PMC (PMC13337501) and the Supplementary\nInformation, without a PDF of the main article or the Source Data; the paper's\nMATLAB code is deposited in the dandiset, so the readers did not read it. The\ncheck made twelve changes and left four points open. With the scripts' models\nalmost every F value, partial eta squared and voxel or field count matches the\npaper to the printed digits: `ed1-behavior-increase` (movement F(1,236) =\n34.61, foraging 17.35), `fig2a-cb-fa-increase` (F(1,3187) = 4.64, P = 0.031),\n`fig2b-mcc-cb-fa-increase`, `fig3c-cc1-dapi-ratio` (F(1,108) = 9.00),\n`ed5-cc1-count-dapi-unchanged`, `ed6-dacc-ufm-no-oligodendrocyte-change`,\n`fig3f-g-ratio-decrease` (F(1,696) = 58.98), the connectome claims of Fig. 4a\nand 4b (69 and 44 ROIs, the reported counts), `fig6a-monkey-d-cb-fa-decrease`,\n`fig6b-monkey-d-dacc-cb-decrease`, `fig6c-monkey-d-cc1-no-change` (paired\nt(27) = -0.9888, P = 0.332, the reported values) and\n`ed10c-monkey-d-subcortical-decrease` are reproduced. The 11 seed-connectivity\noutcomes, the Fig. 5a, 5b and 5c claims, both Extended Data Fig. 9 claims,\n`ed7-decreases-both-monkeys` and `ed10d-monkey-d-roi-changes`, are reproduced on\nthe assumption that the deposited seed maps, one per session, are the maps the\npaper analysed, which the matching interaction F values (186.48, 51.09, 7.36,\n4.58) support. `ed1-monkey-d-no-change` is not reproduced: by the criterion's\none-way ANOVA monkey D's foraging falls from 0.183 to 0.050 (F(1,118) = 5.32,\nP = 0.023), while the deposited FigE1 script runs no test for monkey D, so the\ntest is the claims file's reading of the Methods. `fig4c-network-sorted-reduction`\nis blocked as methods underspecified because no ROI is assigned to a network,\nand `fig6e-monkey-d-no-network-reduction` because its readings disagree: with\nthe script's LIM no sham-side DMN, LIM or CEN decrease is significant, but over\nboth sides the control-side CEN decreases (P = 0.0089). `fig5a-nonsurgical-no-reduction`\nand `fig6d-monkey-d-scc-local-increase` are blocked for missing data. The\nauthor's first run gave the same outcomes, with `fig4b-roi-changes-counts`\nreproduced on the assumption that the Fig. 4 script's test and threshold are\nthe paper's. The author asked a reader whether the criterion should use them and\nwhether \"of the 122 ROIs\" was right; the reader answered yes to both and\namended the claim to the script's rank-sum against zeros at P < 0.05/123 and\n123 ROIs, and the author-answers run kept the outcome, no longer on an\nassumption. Round 1 agreed with all 32 and found that the \"LIM without area 25\"\nreading is ruled out by the legend's voxel counts, that SciPy's studentized\nrange loses accuracy in the far tail, that the file name \"concatenated\" was\nread as concatenated runs without a check, and that the outputs did not show\nwhether the FigE1 script tests monkey D, whether the Fig. 4 script or workbook\nassigns networks, or how the Fig. 6c rows pair; in reply these outputs were\nprinted, the inference was removed, a `methods_unavailable` finding was added\nand a question on the LIM reading was filed in `questions/001773.yaml`, after\nthe reader's run. Round 2 agreed with all 32, asked that the seed-map outcomes\nbe marked as resting on an assumption, and found sentences the outputs did not\nsupport (the stated Tukey-Kramer accuracy of \"1.1 to 3 times\", \"the paper\ntherefore ran no test for monkey D\" and \"next to the lead\" in the fig6d notes);\nin reply `assumed` was set on all 11, a table of 15 reported against computed\nP values was added and the text was corrected, and printing the whole FigE1\nscript brought a new `code_mismatch` finding. The author's run took about 25\nminutes (16:09 to 16:33 UTC); one notebook run broke on a string escape in the\nauthor's generator and was fixed, and the notebook ran in 32 s at first, 24 s\nafter the author-answers run, 41 s after round 1 and about 32 s at the end.\nUntracked dotfiles and a `scripts` entry, sandbox device placeholders created\nbefore the run, were left alone.\n\nThe Data availability statement says the functional MRI data are deposited in\nthe dandiset, but it holds no NWB and no images, only 34 Excel sheets of\nderived values and 18 MATLAB scripts: seed connectivity of the voxels of 17\ntarget ROIs for monkeys N, T and D and three group-average connectomes. There\nare no fMRI or DWI images, no whole-brain seed maps, no seed connectivity for\nthe nonsurgical controls B, W and H and no per-monkey connectomes, so the\nvoxelwise cluster maps of Fig. 5a, Fig. 6d and Extended Data Figs. 7, 8 and 10d\ncannot be tested, and the lead location is not given. The connectomes in\n\"Source Data FC matrix.xlsx\" (123 x 123) carry no ROI names; the Fig. 4 script\nreads them from atlas key and reorder files (CHARM_key_4.txt, SARM_key_4.txt,\nreorder_rois.txt) that are not deposited, so the network sorting of Fig. 4c\ncannot be repeated. The seed connectivity tables hold one value per voxel and\nsession, and the paper does not say whether a session's map was computed on\nconcatenated runs or averaged over per-run maps. The legend in\ndbs_behavior_data_a.xlsx codes foraging as yes 2 and no 1, but every foraging\nvalue is 0 or 1, and read as 1 yes the values give the paper's statistics; the\nsame legend gives group codes 1 and 0, while monkey D's rows carry group 2. In\nCC1_MCC_CB_data_a.xlsx two fields of monkey T's control side (section T423,\nfields 3 and 4) carry CC1/DAPI ratios that do not match their counts (44.9 and\n35.4 % against 35.4 and 44.2 %), and two MCC-CB fields have more CC1-positive\nthan DAPI-positive cells; with the ratio from the counts the side effect\nchanges from F = 9.00 to 9.03. In dbs_EMgratio_MCC_CB_data_a.xlsx the column\nheaded \"diameter of axon(pixel)\" holds half the mean of the long and short\ndiameters, a radius. The dandiset's metadata names the paper only in its title,\nwith no related resource, species, approach, measurement technique or variables\nmeasured, and the sheets have no data dictionary beyond the legends inside\nsome of them; two scripts are deposited twice under two names with identical\ntext. Of the code, the Fig. 4 script counts an ROI as changed at P <\n0.05/nrois (nrois = 123), while the Methods and the Fig. 4b legend give \"P <\n0.01 with Bonferroni correction\"; the script's threshold reproduces the 69 and\n44 ROIs of Supplementary Tables 1 and 2, whose largest listed P is 3.9e-4, above\n0.01/122. The FigE1 script computes the foraging standard errors from the\nmovement column (lines 91 to 96), so the foraging error bars of Extended Data\nFig. 1 are those of movement. Of the paper itself, the Fig. 6a legend gives the\nPrePost x side x tract interaction as F(1,1238) = 6.02, P = 0.0025, which the\ndata give with 2 numerator df, as three tracts imply. A question is put to the\npaper's authors: whether \"the widespread reductions ... were not observed\" in\nmonkey D covers the control hemisphere, where their own Fig. 6e legend lists a\nsignificant CEN difference.\n\nThe author's points on the protocol: the DANDI reading rules assume NWB read\nwith remfile and h5py, so each xlsx asset was fetched into memory through the\nAPI's download endpoint; the clock and stream-alignment check has nothing to act\non in derived tables, so the side labels were checked against the hemispheres\ninstead; the paper's code sits inside the dataset, which readers may not open,\nso details the code settles fell to the author, and the rule \"Methods first,\ncode as variant\" conflicts with the paper's own tables following the code, so\nthe code's procedure for fig4b was adopted as an assumption and a reader asked;\na criterion asked for a seed-map reading the deposit cannot support, which was\nrecorded as a deviation; the protocol says the several-readings rule does not\napply to absence claims while the fig6e criterion says to block when its\nreadings disagree, and the criterion was followed; and SciPy's studentized\nrange tail stops at about 1e-11, where MATLAB prints 0, which was stated as it\ncannot change an outcome at P < 0.05.\n"
}
```

```
File created successfully at: docs/pilot-notes/001773-fujimoto-2026-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  git status --short; grep -n -i "rather\|—" docs/pilot-notes/001773-fujimoto-2026-01.md
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
?? docs/pilot-notes/001773-fujimoto-2026-01.md
?? scripts
```

**Agent**

I wrote the note at `docs/pilot-notes/001773-fujimoto-2026-01.md` and changed no other file. The untracked dotfiles, `.idea`, `.vscode` and `scripts` were in the checkout before I started, and I left them alone. Nothing is committed. The full text is below.

# 001773, Fujimoto et al. 2026

Twenty-seven claims reproduced (11 on an assumption), none partially, one not reproduced and four blocked, two as methods underspecified and two for missing data. All 32 claims are on the dandiset. The first verification round agreed with all 32 outcomes as they stood and so did the second, and nothing was proposed after the second, so there was no third round. It pins version 0.260416.1939, the version the paper cites; the latest version, 0.260615.1838, has identical asset ids. The paper, Fujimoto, Fujimoto, Elorette et al., "Deep brain stimulation induces white matter remodeling and functional changes to brain-wide networks" in Nature Neuroscience, implants an SCC-DBS lead in monkeys N and T, stimulated for 6 weeks, and in monkey D, never stimulated, with nonsurgical controls B, W and H. It reports home-cage behaviour (Extended Data Fig. 1), FA of the white matter tracts (Fig. 2, Extended Data Fig. 2), CC1-positive oligodendrocytes and EM g-ratios (Fig. 3, Extended Data Figs. 5 and 6), the whole-brain connectome (Fig. 4), seed connectivity of area 25 by ROI and network (Fig. 5, Extended Data Figs. 7 and 9) and the same measures in monkey D (Fig. 6, Extended Data Fig. 10). The claims were written from the version of record in Europe PMC (PMC13337501) and the Supplementary Information, without a PDF of the main article or the Source Data; the paper's MATLAB code is deposited in the dandiset, so the readers did not read it. The check made twelve changes and left four points open. With the scripts' models almost every F value, partial eta squared and voxel or field count matches the paper to the printed digits: `ed1-behavior-increase` (movement F(1,236) = 34.61, foraging 17.35), `fig2a-cb-fa-increase` (F(1,3187) = 4.64, P = 0.031), `fig2b-mcc-cb-fa-increase`, `fig3c-cc1-dapi-ratio` (F(1,108) = 9.00), `ed5-cc1-count-dapi-unchanged`, `ed6-dacc-ufm-no-oligodendrocyte-change`, `fig3f-g-ratio-decrease` (F(1,696) = 58.98), the connectome claims of Fig. 4a and 4b (69 and 44 ROIs, the reported counts), `fig6a-monkey-d-cb-fa-decrease`, `fig6b-monkey-d-dacc-cb-decrease`, `fig6c-monkey-d-cc1-no-change` (paired t(27) = -0.9888, P = 0.332, the reported values) and `ed10c-monkey-d-subcortical-decrease` are reproduced. The 11 seed-connectivity outcomes, the Fig. 5a, 5b and 5c claims, both Extended Data Fig. 9 claims, `ed7-decreases-both-monkeys` and `ed10d-monkey-d-roi-changes`, are reproduced on the assumption that the deposited seed maps, one per session, are the maps the paper analysed, which the matching interaction F values (186.48, 51.09, 7.36, 4.58) support. `ed1-monkey-d-no-change` is not reproduced: by the criterion's one-way ANOVA monkey D's foraging falls from 0.183 to 0.050 (F(1,118) = 5.32, P = 0.023), while the deposited FigE1 script runs no test for monkey D, so the test is the claims file's reading of the Methods. `fig4c-network-sorted-reduction` is blocked as methods underspecified because no ROI is assigned to a network, and `fig6e-monkey-d-no-network-reduction` because its readings disagree: with the script's LIM no sham-side DMN, LIM or CEN decrease is significant, but over both sides the control-side CEN decreases (P = 0.0089). `fig5a-nonsurgical-no-reduction` and `fig6d-monkey-d-scc-local-increase` are blocked for missing data. The author's first run gave the same outcomes, with `fig4b-roi-changes-counts` reproduced on the assumption that the Fig. 4 script's test and threshold are the paper's. The author asked a reader whether the criterion should use them and whether "of the 122 ROIs" was right; the reader answered yes to both and amended the claim to the script's rank-sum against zeros at P < 0.05/123 and 123 ROIs, and the author-answers run kept the outcome, no longer on an assumption. Round 1 agreed with all 32. It found that the "LIM without area 25" reading is ruled out by the legend's voxel counts, that SciPy's studentized range loses accuracy in the far tail and that the file name "concatenated" was read as concatenated runs without a check. It also found that the outputs did not show whether the FigE1 script tests monkey D, whether the Fig. 4 script or workbook assigns networks, or how the Fig. 6c rows pair. In reply these outputs were printed, the inference was removed, a `methods_unavailable` finding was added and a question on the LIM reading was filed in `questions/001773.yaml`, after the reader's run. Round 2 agreed with all 32, asked that the seed-map outcomes be marked as resting on an assumption, and found sentences the outputs did not support (the stated Tukey-Kramer accuracy of "1.1 to 3 times", "the paper therefore ran no test for monkey D" and "next to the lead" in the fig6d notes). In reply `assumed` was set on all 11, a table of 15 reported against computed P values was added and the text was corrected, and printing the whole FigE1 script brought a new `code_mismatch` finding. The author's run took about 25 minutes (16:09 to 16:33 UTC); one notebook run broke on a string escape in the author's generator and was fixed, and the notebook ran in 32 s at first, 24 s after the author-answers run, 41 s after round 1 and about 32 s at the end. Untracked dotfiles and a `scripts` entry, sandbox device placeholders created before the run, were left alone.

The Data availability statement says the functional MRI data are deposited in the dandiset, but it holds no NWB and no images, only 34 Excel sheets of derived values and 18 MATLAB scripts: seed connectivity of the voxels of 17 target ROIs for monkeys N, T and D and three group-average connectomes. There are no fMRI or DWI images, no whole-brain seed maps, no seed connectivity for the nonsurgical controls B, W and H and no per-monkey connectomes, so the voxelwise cluster maps of Fig. 5a, Fig. 6d and Extended Data Figs. 7, 8 and 10d cannot be tested, and the lead location is not given. The connectomes in "Source Data FC matrix.xlsx" (123 x 123) carry no ROI names; the Fig. 4 script reads them from atlas key and reorder files (CHARM_key_4.txt, SARM_key_4.txt, reorder_rois.txt) that are not deposited, so the network sorting of Fig. 4c cannot be repeated. The seed connectivity tables hold one value per voxel and session, and the paper does not say whether a session's map was computed on concatenated runs or averaged over per-run maps. The legend in dbs_behavior_data_a.xlsx codes foraging as yes 2 and no 1, but every foraging value is 0 or 1, and read as 1 yes the values give the paper's statistics; the same legend gives group codes 1 and 0, while monkey D's rows carry group 2. In CC1_MCC_CB_data_a.xlsx two fields of monkey T's control side (section T423, fields 3 and 4) carry CC1/DAPI ratios that do not match their counts (44.9 and 35.4 % against 35.4 and 44.2 %), and two MCC-CB fields have more CC1-positive than DAPI-positive cells; with the ratio from the counts the side effect changes from F = 9.00 to 9.03. In dbs_EMgratio_MCC_CB_data_a.xlsx the column headed "diameter of axon(pixel)" holds half the mean of the long and short diameters, a radius. The dandiset's metadata names the paper only in its title, with no related resource, species, approach, measurement technique or variables measured, and the sheets have no data dictionary beyond the legends inside some of them; two scripts are deposited twice under two names with identical text. Of the code, the Fig. 4 script counts an ROI as changed at P < 0.05/nrois (nrois = 123), while the Methods and the Fig. 4b legend give "P < 0.01 with Bonferroni correction"; the script's threshold reproduces the 69 and 44 ROIs of Supplementary Tables 1 and 2, whose largest listed P is 3.9e-4, above 0.01/122. The FigE1 script computes the foraging standard errors from the movement column (lines 91 to 96), so the foraging error bars of Extended Data Fig. 1 are those of movement. Of the paper itself, the Fig. 6a legend gives the PrePost x side x tract interaction as F(1,1238) = 6.02, P = 0.0025, which the data give with 2 numerator df, as three tracts imply. A question is put to the paper's authors: whether "the widespread reductions ... were not observed" in monkey D covers the control hemisphere, where their own Fig. 6e legend lists a significant CEN difference.

The author's points on the protocol: the DANDI reading rules assume NWB read with remfile and h5py, so each xlsx asset was fetched into memory through the API's download endpoint; the clock and stream-alignment check has nothing to act on in derived tables, so the side labels were checked against the hemispheres instead; the paper's code sits inside the dataset, which readers may not open, so details the code settles fell to the author, and the rule "Methods first, code as variant" conflicts with the paper's own tables following the code, so the code's procedure for fig4b was adopted as an assumption and a reader asked; a criterion asked for a seed-map reading the deposit cannot support, which was recorded as a deviation; the protocol says the several-readings rule does not apply to absence claims while the fig6e criterion says to block when its readings disagree, and the criterion was followed; and SciPy's studentized range tail stops at about 1e-11, where MATLAB prints 0, which was stated as it cannot change an outcome at P < 0.05.

## End of run

16 turns, 2 minutes, $1.03 at API prices, result: success.
