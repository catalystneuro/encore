# vijayan-2022 · claims · run 45514661848

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/ claims/ tools/; cat claims/fouke-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -60; ls paper/ claims/ tools/
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 1,
 "limit": 200
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-18`. Record this version in the attempt's provenance.
4	
5	This is what agents, or people, do to attempt a target and deposit the
6	result. A target is a dataset in a public archive and a paper it names. How
7	each archive's datasets are named, versioned and read is in
8	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
9	([pilot notes](https://github.com/encorescience/encore-registry/blob/main/docs/pilot-notes.md)); the reasons for the rules are there.
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
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/fouke-2025.yaml; head -c 3000 paper/10.1126-sciadv.abn3852.txt; wc paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1126-sciadv.abn3852.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
s=open('paper/10.1126-sciadv.abn3852.txt').read()
print(s[52300:90000])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-runner-encore-runner/12d80045-2550-43ee-8fef-e9d8b8b1960e/tool-results/bgdm8xm0u.txt"
}
```

```
1	nts one fly. ( G ) Eggs laid per fly. Each dot represents one fly. ( H and I ) Mean locomotor speed aligned to egg deposition. In total, 1862, 498, 586, and 323 eggs for CS, Dop1R1 − , Dop1R2 attP , and Dop1R2 − , respectively. ( J and K ) Fraction of eggs on 200 mM (J) or 0.8% (K) with 95% confidence interval. Each dot represents one fly. Flies laid an average of 45, 15, 12, 17, 6, 38, 6, 3, 11, and 2 eggs per fly, respectively. P values as in (A). These genotypes lay fewer eggs, overnight, in chambers without a food source (e.g., sucrose) but still lay a large fraction of their eggs on 0.8%. DDC > Kir flies have tubulin promoter driving Gal80 ts . In (A) and (F) to (I), CS data are from ( 16 ). We performed more detailed experiments on all three of the putative null mutants for either Dop1R—Dop1R1 − , Dop1R2 attP , and Dop1R2 − . When starved, all three mutant genotypes initiate feeding after touching sucrose with their front tarsi, indicating that they retain the ability to generally sense sucrose ( Fig. 8B ). Dop1R1 mutant flies showed similar egg-laying rate curves on 0 and 200 mM, highlighting an inability to compare the two options ( Fig. 8C ). Likewise, Dop1R2 mutant flies showed similar rate curves on 0 and 200 mM sucrose ( Fig. 8, D and E ). However, the egg-laying rate curves for Dop1R1 and Dop1R2 mutants appear qualitatively different. Both the 0 and 200 mM rate curves for Dop1R1 mutants look more like the 0 mM rate curve for CS flies ( Fig. 8C , light gray shaded curve), while both the 0 and 200 mM rate curves for Dop1R2 mutants look more like the 200 mM rate curve for CS flies ( Fig. 8C , dark gray shaded curve). This difference might hint at different roles for these receptors in expectation-related calculations. The fact that Dop1R1 − and Dop1R2 attP flies laid more eggs on 200 mM than on 0 mM is consistent with them spending more time, overall, on the 200 mM side ( Fig. 8F ) alongside their roughly similar egg-laying rates for both substrates ( Fi
[... 1 more lines not kept]
```

**Agent**

Now the supplement portion (after references).

**Agent calls Bash**

```bash
python3 -c "
s=open('paper/10.1126-sciadv.abn3852.txt').read()
i=s.find('Fig. S1')
import re
for m in re.finditer('(SUPPLEMENT|Supplementary|=====|Fig. S1\b)',s): print(m.start(), s[m.start():m.start()+80].replace('\n',' '))
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
s=open('paper/10.1126-sciadv.abn3852.txt').read()
print(s[112800:])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -rl "000212" --include=*.yaml --include=*.json --include=*.md . 2>/dev/null | head; ls papers/datasets/ | grep vijayan; cat papers/datasets/vijayan-2022.yaml 2>/dev/null
```

```
./transcripts/kim-2026/author-revise-1.md
./transcripts/liu-2026/001746/author-revise-1.md
./transcripts/kalugin-2026/author.md
./attempts/kim-2026-01.yaml
./papers/manifest.yaml
./papers/triage.yaml
./papers/renamed.yaml
./papers/datasets/vijayan-2022.yaml
./targets/contributors.yaml
./targets/dandisets.json
vijayan-2022.yaml
vijayan-2023.yaml
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.1126/sciadv.abn3852
datasets:
- archive: dandi
  id: '000212'
  relation: primary
```

**Agent calls Bash**

```bash
python3 -c "
import json
d=json.load(open('targets/dandisets.json'))
it = d if isinstance(d,list) else d.get('dandisets', d)
if isinstance(it,dict): it=list(it.values())
for x in it:
  if '000212' in json.dumps(x)[:300]: print(json.dumps(x,indent=1)[:3000])
"; cat papers/datasets/vijayan-2023.yaml
```

```
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.1038/s41586-023-06271-6
datasets:
- archive: dandi
  id: '000247'
  relation: primary
- archive: dandi
  id: '000250'
  relation: primary
```

**Agent calls Bash**

```bash
grep -n -A8 '"000212"' targets/dandisets.json | head -40
```

```
1440:   "dandiset": "000212",
1441-   "name": "Tracking of Drosophila during egg-laying decisions",
1442-   "published_version": null,
1443-   "asset_count": 1013,
1444-   "size_gb": 9.0,
1445-   "data_standards": [
1446-    "Neurodata Without Borders (NWB)"
1447-   ],
1448-   "species": [
```

**Agent calls Bash**

```bash
grep -l "written by an agent" claims/*.yaml | head -3; f=$(grep -l "written by an agent" claims/*.yaml | head -1); head -60 $f; grep -n "inferred\|kind:\|open\b" $f | head; sed -n 1,80p tools/claims_check.py
```

```
claims/dijk-2018.yaml
claims/dvali-2025.yaml
claims/payne-2020.yaml
# Claims for van Dijk & Fenton (2018), "On How the Dentate Gyrus Contributes to Memory
# Discrimination", Neuron 98, 832-845, on CRCNS hc-17.
#
# Provenance: written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub
# Actions"), 2026-11-10, protocol pilot-14 as stated in docs/protocol.md (Reader, steps 1 to 4).
#
# Text read: the version of record (paper/10.1016-j.neuron.2018.04.018.txt, supplied by a
# person, extracted from the PDF), the main text, figure legends, STAR Methods (e1 to e5) and
# the Supplemental Information (Figures S1 and S2 with legends, Tables S1 and S2). No figure
# was read from a PDF page. The CRCNS data descriptor (hc-17.data-description.txt) was read
# only to know which experiments the dataset holds; no claim comes from it.
#
# Code read: the Data and Software Availability section links
# https://github.com/FentonLab/Mcode_DG-MemoryDiscrimination-NeuronMS. At commit
# 3542a85bb44a1739425e63eb4d16f9dc30ce7f54 (2018-04-01, the only commit) it holds a one-line
# README and a file "vanDijkFenton2018Neuron-AnalysisCode" that is a macOS alias (a pointer to
# a folder on the authors' computer), not code. No analysis code could be read, so no method
[... 129 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"
```

```
{
 "$schema": "https://json-schema.org/draft/2020-12/schema",
 "title": "Claims proposed for one target (a dataset and one of its papers)",
 "description": "Draft. To be revised after the pilot.",
 "type": "object",
 "additionalProperties": false,
 "required": [
  "schema_version",
  "paper",
  "claims"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "dataset": {
   "description": "Before the cutover to paper-first records, the dataset a per-dataset claims file was read for. A paper's own claims file (claims/<paper>.yaml) leaves it out.",
   "type": "object",
   "additionalProperties": false,
   "required": [
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)[:4000]); print([k for k in s['properties']])"
```

```
{
 "expected": {
  "type": "object",
  "additionalProperties": false,
  "required": [
   "quantity",
   "value"
  ],
  "properties": {
   "quantity": {
    "type": "string"
   },
   "value": {
    "type": "number"
   },
   "tolerance": {
    "type": "number",
    "minimum": 0
   },
   "unit": {
[... 83 more lines not kept]
```

**Agent**

Paper text and supplement (Figs. S1 to S7) are present; Tables S1 and S2 are not in the text, the main-text PDF is absent, and the paper links no code. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/vijayan-2022.yaml",
 "content": "# Claims for Vijayan, Wang, Chandra, Chakravorty, Li, Sarbanes, Akhlaghpour & Maimon (2022),\n# \"An internal expectation guides Drosophila egg-laying decisions\", Science Advances 8,\n# eabn3852, on DANDI 000212 (\"Tracking of Drosophila during egg-laying decisions\").\n#\n# Provenance: written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub\n# Actions\"), 2026-11-25, protocol pilot-18 as stated in docs/protocol.md (Reader, steps 1 to 4).\n#\n# Text read: the version of record as served by Europe PMC (PMC9616500), in\n# paper/10.1126-sciadv.abn3852.txt, with the main text, figure legends, Materials and Methods,\n# and the supplement PDF (sciadv.abn3852_sm.pdf, Figs. S1 to S7 with legends and the legends of\n# Tables S1 and S2 and Movies S1 to S3), extracted into the same file. No page of a PDF was\n# opened. Not available here: Tables S1 (summary of all tracking data) and S2 (the Gal4 screen),\n# which are separate spreadsheets, and the main-text PDF, so numbers printed only inside main\n# figures (most bin p-values, merge-arrow positions, bar heights) could not be read. The Methods\n# defer the chamber design, tracking and egg annotation to ref. 16 (Vijayan et al., the\n# rise-to-threshold study), which is not under paper/.\n#\n# Code read: none. The paper links no code; \"All data analyses were done using MATLAB\" (Data\n# analysis software). No method detail below is settled by code.\n#\n# Data the paper used (Results; Materials and Methods). Single mated females, overnight in dark\n# egg-laying choice chambers, agarose islands (1% agarose, 1.6% ethanol, 0.8% acetic acid, with\n# sucrose at 0, 200 or 500 mM; 1.2% agarose for D. suzukii; 0.8% or 1.4% agarose in Fig. 6)\n# separated by 2.5-mm plastic barriers (fig. S1). Video at 2 frames per second; measured\n# variables are the xy position of the fly's centroid, the island the fly is on, and the times\n# of egg deposition events. Chamber types: two-choice 0/200, 0/500, 200/500 mM (CS data from\n# ref. 16); three- and five-island chambers 0/200/200 and others (Fig. 2B, C); 0/500/200 (Fig.\n# 2D, E); 0/500/500/500/200 (Fig. 2F); 0/500/200/500/200 (Fig. 2G to I); 0/200 mM with a 4-mm\n# tunnel, a 2-mm tunnel, and a 2-mm tunnel with bounce walls (Fig. 3); 500/0/500, 500/0/200,\n# 0/500/500 (Fig. 4); 0.8% against 1.4% agarose with and without sucrose, and 0.8/0.8 and\n# 1.4/1.4 (Fig. 6). Genotypes: wild-type Canton-S (CS), DL and TUT D. melanogaster strains, D.\n# suzukii (Fig. 5); DDC-Gal4 with tub-Gal80ts and UAS-Kir2.1, pretreated at 18, 27, 29/29.5 or\n# 31 C for 23 h before the assay at 24 C, with TH-Gal80, R58E02-Gal80, TSH-Gal80 or OTD-FLP\n# with TUB-FRT-Gal80-FRT (Fig. 7); 115 Gal4 lines in a screen (Fig. 7A, Table S2); dopamine\n# and serotonin receptor mutants (Fig. 8). Other experiments: chambers with movable boundaries\n# (Fig. 1D, E), glued sensory organs (Fig. 1F), and the latency to feeding assay, groups of\n# three to six food-deprived flies filmed at 15 frames per second and scored by hand (Figs. 7B,\n# 8B). The archive says the dandiset holds \"All fly tracking data used in the paper\" (Data and\n# materials availability); whether it holds the untracked or hand-scored experiments, and the\n# ref. 16 CS data, is the author's to find.\n#\n# Shared methods, cited once here and named in the criteria by label.\n# M1 Island assignment. The fly is on a substrate by whether its centroid is above or below the\n#   chamber midline in two-choice chambers (Results, A framework, paragraph 1). For chambers\n#   with more islands the boundaries are not given in the text; they follow from the\n#   dimensions in fig. S1 (open; the author takes the barrier positions from the chamber\n#   geometry the dataset records, or from fig. S1).\n# M2 Locomotor speed. Not defined in the text beyond being from the tracked position;\n#   frame-to-frame centroid displacement times 2 frames per second, in mm/s, is the standard\n#   choice. Speed traces in figures are smoothed with a 5-s boxcar (Fig. 1 legend).\n# M3 Search period. For each egg, the speed before deposition smoothed with an 18.5-s boxcar;\n#   the search starts at the first frame before the egg where the smoothed speed is below 0.1\n#   mm/s, and ends at deposition; minimum 9 s (Methods, Automated determination of egg-laying\n#   search). \"First frame before\" is read as the last frame, going back from the egg, where the\n#   smoothed speed is below 0.1 mm/s; the 9-s minimum implies a centred filter. For rate\n#   functions, searches shorter than 30 s are set to 30 s (Methods, Calculation of egg-laying\n#   rate); extending the start back to 30 s before the egg is the reading taken.\n# M4 Egg-laying rate function. All flies of a chamber type pooled. For each bin of time since\n#   leaving the other (indicated) substrate, while the fly is on the current substrate during a\n#   search period, rate = (# eggs in bin)/(# frames in bin) x 120 eggs/min; 90% CI by\n#   Clopper-Pearson on # eggs/# visits, scaled by 120 x # visits/# frames (Methods, Calculation\n#   of egg-laying rate). Bin edges are not stated in the text; the x-axis ticks of fig. S2 read\n#   0, 5, 10, 15, 20, 25, 30, 45, 60, 90, 150, 300, 600, 1200, 7200 s, taken as the edges (a\n#   reading; the Methods say other binnings do not change the conclusions).\n# M5 Bin test. Two-sided Wilcoxon rank sum test on 0/1 trials, a trial with an egg being 1\n#   (Methods, Statistics). What a trial is is open; readings (a) one visit to the bin during a\n#   search, the unit of the CI; (b) one search period that enters the bin. Merge point, as\n#   Fig. 5A legend defines it, is the first bin past 5 s for which P > 0.05.\n# M6 Choice fraction. Eggs on the named option over all eggs, pooled over flies, with a 95%\n#   Clopper-Pearson CI; group comparisons are two-sided Wilcoxon rank sum tests on per-fly\n#   fractions of flies that laid at least 5 eggs (Fig. 1F and Fig. 7 legends; Methods,\n#   Statistics).\n# M7 Pause time. Time from the last moment before deposition that the 1-s boxcar smoothed\n#   speed rose above 0.1 mm/s to the deposition, compared between groups of eggs with the\n#   two-sided Wilcoxon rank sum test (Methods, Statistics). Read as the duration of the final\n#   stop before the egg.\n# M8 Egg-aligned speed. Mean locomotor speed (M2) aligned to egg deposition; eggs within the\n#   first or last few minutes of a video left out to avoid partial traces (Fig. 3F legend; the\n#   window is not given, the plotted window from the figure is a standard choice).\nschema_version: 2\npaper: doi:10.1126/sciadv.abn3852\nclaims:\n- id: leave-higher-stay-lower\n  statement: In two-choice sucrose chambers, flies leave the higher sucrose substrate in 964 of\n    1205 (80%) searches that start on it, and leave the lower sucrose substrate in only 918 of\n    2744 (33%) searches that start on it.\n  source: Results, A framework for understanding how previous substrate experiences guide\n    egg-laying choices, paragraph 4\n  quote: flies leave higher sucrose in 964 of 1205 or 80% of searches initiated on higher\n    sucrose), whereas flies that start a search on lower sucrose know to stay (flies leave lower\n    sucrose in only 918 of 2744 or 33% of searches initiated on lower sucrose) ( P < 0.001,\n    two-sided Wilcoxon rank sum test\n  statistics:\n  - test: two-sided Wilcoxon rank sum test on searches as 0/1 trials\n    p: 0.001\n    p_relation: \"<\"\n    n: 1205 searches started on higher sucrose and 2744 on lower sucrose\n  expected:\n  - quantity: searches started on higher sucrose\n    value: 1205\n    tolerance: 120.5\n  - quantity: fraction of searches started on higher sucrose that leave it\n    value: 0.80\n    tolerance: 0.08\n  - quantity: searches started on lower sucrose\n    value: 2744\n    tolerance: 274.4\n  - quantity: fraction of searches started on lower sucrose that leave it\n    value: 0.33\n    tolerance: 0.033\n  criterion: Searches by M3 (the 30-s minimum not applied, as this is not a rate function), CS\n    flies in two-choice sucrose chambers; island at search start and whether the fly crosses to\n    the other island before the egg, by M1. Which chambers are pooled is open; readings (a) the\n    0/200, 0/500 and 200/500 mM chambers of ref. 16, as for fig. S3; (b) those three with any\n    CS two-choice sucrose chamber of this paper. Reproduced when, under one reading, both\n    fractions are within tolerance and the two-sided Wilcoxon rank sum test on 0/1 trials\n    (Methods, Statistics) gives p < 0.001; partially reproduced when the fractions differ in the\n    stated direction at p < 0.001 but are out of tolerance.\n- id: fig1d-no-substrate-marking\n  statement: When a previously preferred 200 mM island carrying eggs from earlier flies is paired\n    with 0 mM, new flies lay eggs normally on 0 mM, and likewise for a nonpreferred option, so\n    flies do not rely on previously laid eggs or other lasting chemical marks.\n  source: Results, Flies continuously make sucrose assessments, paragraph 2; Figure 1D and 1E\n  quote: Flies laid eggs normally on 0 mM, although 200 mM had many eggs from the start ...\n    Thus, our flies did not seem to rely on previously laid eggs, or other long-lasting chemical\n    cues, which mark either the preferred ( Fig. 1D ) or nonpreferred ( Fig. 1E ) option\n  criterion: Fraction of eggs on the lower sucrose option, M6. Reproduced when, in the second\n    assay of each pair (Fig. 1D right bar, Fig. 1E second bar), the pooled fraction on the\n    lower sucrose option is above 0.5 with its 95% Clopper-Pearson CI above 0.5. The paper\n    reports no test; the first-night fractions are reported alongside.\n- id: fig1f-tarsi-proboscis\n  statement: Gluing the front tarsi or the proboscis significantly reduces the bias to lay eggs\n    on 0 over 200 mM, gluing both leaves no detectable population preference, and gluing the\n    back tarsi does not significantly affect choice.\n  source: Results, Flies continuously make sucrose assessments, paragraph 3; Figure 1F\n  quote: When we applied glue to the front tarsi (front leg tips) or proboscis, the bias to\n    laying eggs on 0 mM was significantly reduced, and when both these body parts had glue, we\n    could not detect a population-level preference for 0 over 200 mM\n  statistics:\n  - about: three displayed comparisons, top to bottom\n    test: two-sided Wilcoxon rank sum test, flies that laid at least 5 eggs\n    p: 0.005\n    p_relation: \"<\"\n    corrected: Bonferroni for seven comparisons (P < 0.05/7 = 0.007)\n    n: 18, 13, 12, 41, 20, 13, 28 and 9 flies with at least 5 eggs in the eight groups\n  - about: third displayed comparison\n    test: two-sided Wilcoxon rank sum test, flies that laid at least 5 eggs\n    p: 0.001\n    p_relation: \"<\"\n  expected:\n  - quantity: mean eggs per fly in the eight groups (25, 24, 29, 25, 29, 18, 23, 14)\n    value: 25\n    tolerance: 2.5\n    unit: eggs per fly, first group\n  criterion: M6 on the eight groups of Fig. 1F. The group names and which pairs the three\n    p-values compare are shown only in the figure, which could not be read; readings (a) each\n    glued group against the unglued control; (b) each glued group against its own control.\n    Reproduced when front tarsi, proboscis, and front tarsi with proboscis each differ from\n    their control at p < 0.007 with a lower fraction on 0 mM, the fraction with both glued has\n    a 95% CI that includes 0.5, and back tarsi does not differ at p < 0.007. The eight mean\n    egg counts and the eight counts of flies with at least 5 eggs are reported against the\n    legend.\n- id: fig2bc-larger-chambers-two-options\n  statement: In three- and five-island chambers with two sucrose concentrations, flies choose\n    the low sucrose option with egg-laying rate dynamics similar to standard two-choice chambers.\n  source: Results, Flies lay eggs on the best of three options, paragraph 1; Figure 2B and 2C\n  quote: flies effectively chose the low sucrose option when presented with two sucrose\n    concentrations, and they did so with similar egg-laying rate dynamics to those observed in\n    standard two-choice chambers\n  criterion: Rate functions M4 for each chamber (0/200/200 mM for Fig. 2B as Fig. 4B legend\n    names it; Fig. 2C's five-island layout is not named in the text and is taken from Table S1\n    or the dataset). Reproduced when, in each chamber, the rate on the higher sucrose option\n    since leaving the lower one is below the rate on the lower option since leaving the higher\n    one in the bins from 5 to 60 s, with at least one bin significant by M5 at p < 0.05, as for\n    two-choice chambers (Fig. 2A). The paper gives no test of similarity to two-choice\n    dynamics; the merge point M5 of each chamber is reported.\n- id: fig2d-three-choice-inhibit-200\n  statement: In a 0/500/200 mM chamber flies inhibit egg laying upon entering 200 mM from 500\n    mM, although 200 mM is strongly preferred after the same transition in two-choice chambers.\n  source: Results, Flies lay eggs on the best of three options, paragraphs 2 and 3; Figure 2D\n  quote: However, we observed that flies inhibited egg laying upon entering 200 mM in this\n    chamber\n  criterion: M4 in the 0/500/200 chamber, rate on 200 mM since leaving 500 mM, against the rate\n    on 200 mM since leaving 500 mM in the CS 200/500 two-choice chamber (ref. 16 data), bins 5\n    to 60 s. Reproduced when the three-choice rate is lower in most of these bins and at least\n    one bin differs by M5 at p < 0.05. The paper prints no test for this comparison; the\n    criterion uses the Methods' bin test.\n- id: fig2e-200-recovers-with-time\n  statement: In the 0/500/200 mM chamber, the egg-laying rate on 200 mM rises gradually with time\n    since the last visit to 0 mM.\n  source: Results, Flies lay eggs on the best of three options, paragraph 2; Figure 2E\n  quote: As time passed since the last visit to 0 mM, the egg-laying rate on 200 mM gradually\n    increased\n  criterion: M4, rate on 200 mM by time since leaving 0 mM. The paper gives no test; the measure\n    fixed here is the pooled rate over bins from 300 s onward against the pooled rate over bins\n    5 to 30 s, compared by M5. Reproduced when the later rate is higher at p < 0.05 and the\n    rate is non-decreasing across most successive bins.\n- id: fig2efg-inhibit-200-after-0\n  statement: In all three-choice chambers flies inhibit egg laying on 200 mM nearly completely if\n    they visited 0 mM in the last ~30 s, and this holds with a larger distance between 0 and 200\n    mM (0/500/500/500/200) and with several 500 to 200 mM transitions along the path\n    (0/500/200/500/200).\n  source: Results, Flies lay eggs on the best of three options, paragraph 2; Figure 2E to 2G\n  quote: In all these three-choice chambers, flies inhibited egg laying nearly completely on 200\n    mM if they had visited 0 mM in the last ~30 s\n  criterion: M4 in the 0/500/200, 0/500/500/500/200 and 0/500/200/500/200 chambers, rate on 200\n    mM and on 0 mM by time since leaving the other of the two, pooled over 5 to 30 s.\n    \"Nearly completely\" has no threshold in the paper; readings (a) the 200 mM rate at most 10%\n    of the 0 mM rate over that window; (b) at most 20%. Reproduced when, under one reading, it\n    holds in all three chambers and the difference is significant by M5 at p < 0.05 in each;\n    partially reproduced when it holds in two. Bins below 5 s are left out as the paper\n    describes a low rate for every curve in the first seconds after a transition.\n- id: fig2-earlier-merge-three-choice\n  statement: The 0 and 200 mM rate functions merge at an earlier time in three-choice chambers\n    than in two-choice chambers.\n  source: Results, Flies lay eggs on the best of three options, paragraph 3; Figure 2A to 2G\n  quote: the 0 and 200 mM egg-laying rate functions did appear to merge at an earlier time point\n    in three-choice ( Fig. 2, E to G ) compared to two-choice chambers\n  criterion: Merge point by M5 (first bin past 5 s with P > 0.05) of the 0 mM and 200 mM curves\n    (each since leaving the other) in each three-choice chamber of claim fig2efg against the CS\n    0/200 two-choice chamber. Reproduced when the merge bin is earlier in at least two of the\n    three three-choice chambers.\n- id: fig3ab-2mm-tunnel-faster\n  statement: With a 2-mm tunnel between 200 mM and 0 mM, flies lay eggs at a higher rate in the\n    5 to 10 s after entering 0 mM than with a 4-mm tunnel.\n  source: Results, Flies lay eggs more rapidly on high-quality substrates that they visit rarely\n    or briefly, paragraph 1; Figure 3A and 3B\n  quote: In chambers with a tiny (2 mm) tunnel between substrates, flies laid eggs at a higher\n    rate in the 5- to 10-s window after a transition to 0 mM compared to very similar chambers\n    with a 4-mm tunnel\n  criterion: M4, rate on 0 mM since leaving 200 mM in the 5 to 10 s bin; 2-mm against 4-mm\n    tunnel chambers by M5. The paper's p-value is shown only in Fig. 3B. Reproduced when the\n    2-mm rate is higher at p < 0.05.\n- id: fig3c-bounce-faster\n  statement: With angled walls that bounce flies away from the 2-mm tunnel, flies lay eggs even\n    more rapidly on entering 0 mM than in the 2-mm and 4-mm tunnel chambers.\n  source: Results, Flies lay eggs more rapidly on high-quality substrates, paragraph 1; Figure 3C\n  quote: In this chamber, flies laid eggs even more rapidly upon entering the 0 mM side\n  criterion: As fig3ab-2mm-tunnel-faster, the bounce chamber's 5 to 10 s bin against the same\n    bin of each tunnel chamber by M5 (Fig. 3 legend). Reproduced when it is higher than both at\n    p < 0.05; partially reproduced when it is higher than the 4-mm chamber only. Methods,\n    Statistics notes that the second p-value of Fig. 3C is 0.058 by Fisher's exact test, so a\n    weak second comparison is expected.\n- id: fig3d-dwell-before-fast-eggs\n  statement: Across the 4-mm, 2-mm and 2-mm bounce chambers, flies spend progressively more time\n    on 200 mM before entering 0 mM and laying a fast egg (within 10 s), with medians of 54, 96 and\n    576 s over 36, 44 and 23 eggs.\n  source: Results, Flies lay eggs more rapidly on high-quality substrates, paragraph 2; Figure 3D\n  quote: Medians are 54, 96, and 576 s for increasing shades of gray. Thirty-six, 44, and 23 eggs\n    for increasing shades of gray.\n  expected:\n  - quantity: median time on 200 mM before a fast egg, 4-mm tunnel\n    value: 54\n    tolerance: 5.4\n    unit: s\n  - quantity: median, 2-mm tunnel\n    value: 96\n    tolerance: 9.6\n    unit: s\n  - quantity: median, 2-mm tunnel with bounce\n    value: 576\n    tolerance: 57.6\n    unit: s\n  - quantity: fast eggs, 4-mm tunnel\n    value: 36\n    tolerance: 3.6\n  - quantity: fast eggs, 2-mm tunnel\n    value: 44\n    tolerance: 4.4\n  - quantity: fast eggs, 2-mm tunnel with bounce\n    value: 23\n    tolerance: 2.3\n  criterion: A fast egg is laid on 0 mM within 10 s of entering it from 200 mM; its dwell time is\n    the duration of the preceding visit to 200 mM (M1). The order of shades is read as Fig. 3A,\n    B, C (4-mm, 2-mm, bounce), from \"progressively more time\" in the text. Whether \"within 10 s\"\n    counts from crossing the midline or from leaving 200 mM is open; both are run. Dwell times\n    compared between chambers by the two-sided Wilcoxon rank sum test (Methods, Statistics);\n    the paper's p-values are only in the figure. Reproduced when all six values are within\n    tolerance under one reading and the medians increase in that order.\n- id: fig3e-rate-after-long-absence\n  statement: Pooling the three tunnel chambers, the egg-laying rate in the 10 s after entering 0\n    mM rises when flies have not experienced 0 mM for more than about 4 min.\n  source: Results, Flies lay eggs more rapidly on high-quality substrates, paragraph 2; Figure 3E\n  quote: we observe that flies increase their egg-laying rate upon entering 0 mM specifically if\n    they have not experienced 0 mM for >~4 min\n  criterion: Rate during search (M4 counting) in the first 10 s on 0 mM, binned by the time spent\n    on 200 mM in the preceding visit, all eggs of the three chambers pooled. Bin edges for the\n    x-axis of Fig. 3E are not in the text; the M4 edges are used as a standard choice.\n    Reproduced when the pooled rate for previous visits longer than 240 s is higher than for\n    shorter visits by M5 at p < 0.05, and the bins below 240 s show no rising trend.\n- id: fig3f-motor-program-not-faster\n  statement: The delay between the dip in locomotor speed and egg deposition is similar for fast\n    eggs and for all eggs in the three tunnel chambers, so the decision and not the deposition\n    motor program is faster.\n  source: Results, Flies lay eggs more rapidly on high-quality substrates, paragraph 2; Figure 3F\n  quote: is similar for fast eggs ( Fig. 3F , pink) and all eggs in these three chambers\n  expected:\n  - quantity: eggs in the egg-aligned average, 4-mm tunnel\n    value: 979\n    tolerance: 97.9\n  - quantity: eggs, 2-mm tunnel\n    value: 918\n    tolerance: 91.8\n  - quantity: eggs, 2-mm tunnel with bounce\n    value: 675\n    tolerance: 67.5\n  criterion: Egg-aligned speed M8 and pause time M7. The paper gives no test; a claim of\n    similarity is judged by M7 pause times of fast eggs against all eggs of each chamber with\n    the two-sided Wilcoxon rank sum test. Reproduced when no chamber differs at p < 0.05 and\n    the median pause times differ by less than 10%; the egg counts are reported against the\n    legend.\n- id: fig4a-shorter-middle-transits\n  statement: Because flies follow the walls, transits through middle islands are shorter (median\n    ~4.5 s) than through edge islands (median ~13 s).\n  source: Results, Flies lay eggs more rapidly on high-quality substrates, paragraph 3; Figure 4A\n  quote: they had shorter transit times through the middle islands of rectangular chambers\n    (median, ~4.5 s) compared to the edge islands (median, ~13 s)\n  expected:\n  - quantity: median transit time, middle islands\n    value: 4.5\n    tolerance: 0.45\n    unit: s\n  - quantity: median transit time, edge islands\n    value: 13\n    tolerance: 1.3\n    unit: s\n  - quantity: transits on 0, 500 and 200 mM in the 0/500/200 chamber (2637, 5694, 2903), the 0 mM count\n    value: 2637\n    tolerance: 263.7\n  criterion: Transit time is the duration of a visit to an island during a search period (M1,\n    M3), in the 0/500/200, 500/0/500 and 500/0/200 chambers. Whether a transit is every visit or\n    only a pass from one neighbour to another is open; readings (a) every visit; (b) visits that\n    enter from one side and leave by the other (middle islands) or return (edges). Whether the\n    medians pool chambers is open; readings (i) pooled over the three chambers; (ii) each\n    chamber. Reproduced when, under one reading, both medians are within tolerance; the eight\n    transit counts of the legend are reported.\n- id: fig4b-faster-middle-preferred\n  statement: When the preferred 0 mM substrate is in the middle island, flies lay eggs more\n    quickly after entering it than in three-island chambers with the preferred substrate at an\n    edge.\n  source: Results, Flies lay eggs more rapidly on high-quality substrates, paragraph 3; Figure 4B\n  quote: We found that flies lay eggs more quickly after a transition to the preferred substrate\n    in these chambers\n  statistics:\n  - about: indicated bin against a 0/500/500 chamber (Table S1)\n    test: two-sided Wilcoxon rank sum test\n    p: 0.001\n    p_relation: \"<\"\n  criterion: M4, rate on 0 mM since leaving the other substrate in the 500/0/500 and 500/0/200\n    chambers, against the pooled 0/200/200, 0/500/200 and 0/500/500 chambers. The indicated bin\n    is shown only in the figure; readings (a) 5 to 10 s, as in Fig. 3; (b) 0 to 5 s; (c) 10 to\n    15 s. Reproduced when, under one reading, the middle-preferred rate is higher by M5 at p <\n    0.05 against the pooled edge chambers and at p < 0.001 against 0/500/500.\n- id: fig4d-anomalous-eggs-alternative\n  statement: With 0 mM in the middle (500/0/200), flies also have a higher egg-laying rate than\n    in other three-choice chambers on the closest alternative, 200 mM, from 0 to 90 s after\n    leaving 0 mM.\n  source: Results, Flies lay eggs more rapidly on high-quality substrates, paragraph 3; Figure 4D\n    against Figure 2E\n  quote: flies also had a higher egg-laying rate than expected (from our other three-choice\n    experiments) on the closest alternative\n  criterion: M4, rate on 200 mM since leaving 0 mM pooled over 0 to 90 s, 500/0/200 against\n    0/500/200 (Fig. 2E) by M5. The paper gives no test. Reproduced when the 500/0/200 rate is\n    higher at p < 0.05.\n- id: fig4e-inter-egg-not-longer\n  statement: The interval between eggs is not increased when the preferred substrate is in the\n    middle island (medians 5.1, 4.1 and 4.4 min over 2262, 922 and 1901 intervals), so flies are\n    not abandoning searches there.\n  source: Results, Flies lay eggs more rapidly on high-quality substrates, paragraph 4; Figure 4E\n  quote: Medians are 5.1, 4.1, and 4.4 min. In total, 2262, 922, and 1901 inter-egg intervals,\n    respectively.\n  expected:\n  - quantity: median inter-egg interval, first chamber\n    value: 5.1\n    tolerance: 0.51\n    unit: min\n  - quantity: median, second chamber\n    value: 4.1\n    tolerance: 0.41\n    unit: min\n  - quantity: median, third chamber\n    value: 4.4\n    tolerance: 0.44\n    unit: min\n  - quantity: intervals, first chamber\n    value: 2262\n    tolerance: 226.2\n  - quantity: intervals, second chamber\n    value: 922\n    tolerance: 92.2\n  - quantity: intervals, third chamber\n    value: 1901\n    tolerance: 190.1\n  criterion: Intervals between successive eggs of the same fly. Which chamber is which shade is\n    shown only in the figure; reading taken, the order of Fig. 4A (0/500/200, 500/0/500,\n    500/0/200), with the counts of Fig. 4F (2312, 943, 1946 eggs) as a check that the order is\n    the same; all six orders are shown if that one fails. Reproduced when the values are within\n    tolerance under one order and neither middle-preferred chamber has a longer median than\n    the edge-preferred chamber.\n- id: fig4f-motor-program-not-accelerated\n  statement: With the preferred substrate in the middle, the egg deposition motor program, proxied\n    by the dip in locomotor speed, is not clearly accelerated.\n  source: Results, Flies lay eggs more rapidly on high-quality substrates, paragraph 4; Figure 4F\n  quote: As in our previous experiments, the egg deposition motor program (as proxied by the dip\n    in locomotor speed) is not clearly accelerated\n  expected:\n  - quantity: eggs in the egg-aligned average, first chamber (2312, 943, 1946)\n    value: 2312\n    tolerance: 231.2\n  criterion: M7 and M8 in the three chambers of Fig. 4E. The paper gives no test. Reproduced when\n    the median pause time in each middle-preferred chamber is not shorter than in 0/500/200 by\n    the two-sided Wilcoxon rank sum test at p < 0.05, or is shorter by less than 10%.\n- id: fig5ab-strains-release-faster\n  statement: The DL and TUT wild-type strains release inhibition of egg laying on 200 mM faster\n    than CS in 0/200 mM chambers; TUT shows no detectable effect of substrate history after about\n    20 s on a new substrate, while the CS curves do not merge within the plotted interval.\n  source: Results, Different Drosophila strains and species, paragraph 1; Figure 5A and 5B\n  quote: found that both released inhibition of egg laying on 200 mM faster than did CS flies\n    ... the TUT strain showed no statistically detectable evidence of substrate history after\n    only ~20 s of being on a new substrate\n  expected:\n  - quantity: TUT merge point\n    value: 20\n    tolerance: 5\n    unit: s\n  criterion: Merge point by M5 for 0 against 200 mM rate functions (M4) per strain. Tolerance of\n    one bin of M4 near 20 s (15 to 25 s), as the merge point is a bin edge. Reproduced when the\n    TUT merge point is within tolerance, the DL merge point is earlier than the CS one, and CS\n    does not merge within the plotted interval (up to 7200 s by M4).\n- id: fig5c-suzukii-no-preference\n  statement: D. suzukii shows no measurable egg-laying preference for lower sucrose; its rates on\n    0 and 200 mM are similar in a two-choice chamber.\n  source: Results, Different Drosophila strains and species, paragraph 2; Figure 5C\n  quote: D. suzukii did not exhibit a measurable egg-laying preference for lower sucrose\n    substrates in our paradigm, i.e., the egg-laying rates on 0 and 200 mM were similar in a\n    two-choice chamber\n  criterion: A claim of absence, judged on the paper's bin test M5 at p < 0.05. Reproduced when no\n    bin past 5 s shows a significantly higher rate on 0 than on 200 mM; not reproduced when any\n    does. The size of the difference in each bin is reported.\n- id: fig5de-suzukii-more-on-200\n  statement: D. suzukii lays slightly more eggs on 200 mM than on 0 mM, consistent with spending\n    more time on high sucrose.\n  source: Results, Different Drosophila strains and species, paragraph 2; Figure 5D and 5E\n  quote: D. suzukii actually laid slightly more eggs on the higher (200 mM) sucrose substrate (\n    Fig. 5D ), consistent with their overall preference toward spending more time on high\n    sucrose\n  criterion: Pooled fraction of eggs on 0 mM (M6) below 0.5, and per-fly fraction of time on 0\n    mM (M1, whole recording) with a median below 0.5. No test is reported; \"slightly\" is not\n    judged.\n- id: fig5f-egg-numbers-differ\n  statement: Different strains and species lay different numbers of eggs.\n  source: Results, Different Drosophila strains and species, paragraph 3; Figure 5F\n  quote: different strains/species laid a different number of eggs\n  criterion: Eggs per fly for D. suzukii, TUT, DL and CS. No test is reported; the paper's test\n    for groups of flies is the two-sided Wilcoxon rank sum test (Methods, Statistics), used\n    pairwise. Reproduced when at least one pair differs at p < 0.05.\n- id: fig5gh-search-and-pause\n  statement: All strains and species raise their locomotor speed before pausing to lay an egg,\n    and they differ from one another in the delay between the speed dip and egg deposition.\n  source: Results, Different Drosophila strains and species, paragraph 3; Figure 5G and 5H\n  quote: they exhibit different time delays between the dip in average locomotor speed and egg\n    deposition ( P < 0.001 all comparisons, two-sided Wilcoxon rank sum test\n  statistics:\n  - test: two-sided Wilcoxon rank sum test on pause times, all pairwise comparisons\n    p: 0.001\n    p_relation: \"<\"\n    n: 214, 1184, 766 and 1862 eggs for D. suzukii, TUT, DL and CS\n  expected:\n  - quantity: eggs, D. suzukii\n    value: 214\n    tolerance: 21.4\n  - quantity: eggs, TUT\n    value: 1184\n    tolerance: 118.4\n  - quantity: eggs, DL\n    value: 766\n    tolerance: 76.6\n  - quantity: eggs, CS\n    value: 1862\n    tolerance: 186.2\n  criterion: M7 pause times compared in all six pairs; M8 for the rise in speed, judged as the\n    mean speed over the 60 s before the pause higher than the mean over the preceding 60 s (a\n    window fixed here; the paper gives none). Reproduced when all six pairs differ at p <\n    0.001 and the speed rises in all four groups; partially reproduced when four or five pairs\n    differ.\n- id: fig6b-softer-preferred\n  statement: Flies prefer to lay eggs on 0.8% over 1.4% agarose (about 80% of eggs); sucrose on\n    the softer option shifts preference to the harder one, equal sucrose on both has little\n    effect, and 500 mM on the softer with 200 mM on the harder gives about 50%.\n  source: Results, Flies do not strongly modulate their egg-laying rates in all substrate choice\n    environments, paragraph 2; Figure 6B\n  quote: found that, as expected, flies prefer to lay eggs on the softer option ( Fig. 6B , first\n    bar). Adding sucrose to the softer option shifts the preference to the harder option ( Fig.\n    6B , bars 2 and 3), and adding equal amounts of sucrose to both options has little effect\n  expected:\n  - quantity: fraction of eggs on 0.8% agarose, 0.8% against 1.4% without sucrose\n    value: 0.8\n    tolerance: 0.08\n  - quantity: fraction on the softer option, 500 mM on 0.8% against 200 mM on 1.4%\n    value: 0.5\n    tolerance: 0.05\n  - quantity: mean eggs per fly, six groups (38, 36, 38, 36, 30, 33), first group\n    value: 38\n    tolerance: 3.8\n  criterion: M6 per condition, fraction on the softer (0.8%) option. The sucrose levels of bars 2\n    to 5 are shown only in the figure and are taken from the dataset's condition labels. The\n    ~80% is from Results, paragraph 4 (\"they lay ~80% of their eggs on the softer option\").\n    Reproduced when both fractions are within tolerance, bars 2 and 3 are below 0.5, and bars 4\n    and 5 are within 0.1 of bar 1; the six mean egg counts are reported.\n- id: fig6cd-hardness-fast-merge\n  statement: Unlike sucrose, flies do not strongly repress egg laying for minutes on the harder\n    option; the 0.8% and 1.4% rate curves merge within about 20 s, also with equal sucrose on\n    both.\n  source: Results, Flies do not strongly modulate their egg-laying rates, paragraph 2; Figure 6C\n    and 6D\n  quote: The egg-laying rates on 0.8 and 1.4% agarose merge within just ~20 s of being on a new\n    substrate ( Fig. 6C , filled arrow), and this result is robust to adding equal amounts of\n    sucrose to both options\n  expected:\n  - quantity: merge point, 0.8% against 1.4% agarose\n    value: 20\n    tolerance: 5\n    unit: s\n  criterion: Merge point by M5 of the 0.8% and 1.4% rate functions (M4) in the chamber without\n    sucrose and in the chambers with equal sucrose on both sides. Tolerance of one bin, as for\n    fig5ab. Reproduced when every chamber merges at or before 25 s.\n- id: fig6ef-pause-longer-hard\n  statement: Flies pause longer to lay eggs on harder substrates, and egg-laying rates are lower\n    for about 15 s after crossing the boundary in a 1.4%/1.4% chamber than in a 0.8%/0.8% chamber.\n  source: Results, Flies do not strongly modulate their egg-laying rates, paragraph 3; Figure 6E\n    and 6F\n  quote: We noticed that flies pause for a longer duration to lay eggs on harder substrates ( P <\n    0.001, two-sided Wilcoxon rank sum test\n  statistics:\n  - about: pause times, 1.4% against 0.8% agarose\n    test: two-sided Wilcoxon rank sum test\n    p: 0.001\n    p_relation: \"<\"\n    n: 831 and 795 eggs for 0.8% versus 0.8% and 1.4% versus 1.4%\n  expected:\n  - quantity: eggs, 0.8% versus 0.8% chamber\n    value: 831\n    tolerance: 83.1\n  - quantity: eggs, 1.4% versus 1.4% chamber\n    value: 795\n    tolerance: 79.5\n  criterion: M7 pause times of eggs in the 1.4%/1.4% against the 0.8%/0.8% chambers, and M4 rates\n    since crossing the barrier in both. Reproduced when pause times are longer on 1.4% at p <\n    0.001 and the 1.4% rate is lower than the 0.8% rate in the bins up to 15 s, with at least one\n    of them significant by M5 at p < 0.05.\n- id: fig6g-more-time-softer\n  statement: Flies spend more time on the softer option in 0.8% against 1.4% chambers.\n  source: Results, Flies do not strongly modulate their egg-laying rates, paragraph 4; Figure 6G\n  quote: At least part of the answer is that flies simply spend more time on the softer option\n  criterion: Per-fly fraction of recording time on 0.8% (M1). Whether time is all frames or only\n    search frames is open; both are run. Reproduced when the median over flies is above 0.5\n    under one reading. No test is reported.\n- id: fig7a-screen-ddc-hits\n  statement: Of 115 Gal4 lines in a Kir2.1 screen of 0 against 200 mM choice, 110 controls (96%)\n    laid more eggs on 0 mM and 111 (97%) laid at least five eggs per fly, and the top 8 hits had\n    Gal4 driven by a Ddc-related enhancer.\n  source: Results, Dopa decarboxylase-expressing neurons are a strong candidate, paragraph 2;\n    Figure 7A; fig. S5; Table S2\n  quote: Of the 115 Gal4 lines tested, in the control condition, 110 (96%) laid more eggs on 0\n    than 200 mM (fig. S5A) and 111 (97%) laid five or more eggs per fly\n  expected:\n  - quantity: Gal4 lines tested\n    value: 115\n    tolerance: 0\n  - quantity: control lines with more eggs on 0 than 200 mM\n    value: 110\n    tolerance: 11\n  - quantity: control lines laying at least 5 eggs per fly\n    value: 111\n    tolerance: 11.1\n  criterion: Per line, pooled fraction of eggs on 0 mM (M6) in experimental (31 C pre) and control\n    (18 C pre) flies; fold change is experimental over control fraction, and p is the two-sided\n    Wilcoxon rank sum test between groups (Fig. 7A legend). Ranking of hits is open; readings\n    (a) by fold change, lowest first; (b) by p, lowest first. The line identities and enhancers\n    come from Table S2, not available here, so the Ddc part needs those labels from the\n    dataset. Reproduced when the counts are within tolerance and, under one reading, the top 8\n    lines are Ddc-related. The count of 115 is exact as it counts lines.\n  data: with_labels\n- id: fig7b-ddc-kir-sense-sucrose\n  statement: Food-deprived DDC>Kir (31 C pre) flies extend the proboscis or enter a feeding\n    posture soon after crossing onto 200 mM, so they can still sense sucrose; flies not food\n    deprived show no proboscis extension.\n  source: Results, Dopa decarboxylase-expressing neurons, paragraph 3; Figure 7B; fig. S6\n  quote: DDC > Kir (31°C pre) food-deprived flies either extended their proboscis or, in cases\n    where our camera could not see their proboscis clearly, entered an obvious feeding posture\n    quickly after crossing onto 200 mM\n  criterion: Latency from the first tarsus crossing to proboscis extension or feeding posture,\n    scored by hand from 15 frames per second video (Methods, Latency to feeding assay). The\n    paper reports no threshold for \"quickly\"; fig. S6 shows all pictured flies within 10.93 s.\n    Reproduced when the latencies of food-deprived DDC>Kir (31 C pre) flies are similar to\n    those of controls (median within a factor of 2, as a working bound fixed here) and all are\n    finite. Needs video or annotations of this assay; if the dataset holds only tracking, the\n    claim cannot be tested.\n- id: fig7cf-kir-merge-earlier\n  statement: The more Kir2.1 is expressed in DDC-Gal4 neurons (pretreatment at 18, 27, 29/29.5 and\n    31 C), the earlier the 0 and 200 mM rate curves merge; at 31 C they are nearly superimposable\n    throughout, while at the two intermediate temperatures rates stay properly biased just after\n    a transition.\n  source: Results, Dopa decarboxylase-expressing neurons, paragraphs 4 and 5; Figure 7C to 7F\n  quote: The more Kir2.1 we expressed, the earlier in time after a substrate transition did the 0\n    and 200 mM egg-laying rate curves begin to merge\n  criterion: Merge point by M5 for each pretreatment temperature, rate functions M4.\n    \"Nearly superimposable throughout\" has no threshold; readings (a) the merge point at 31 C is\n    the first bin past 5 s; (b) at most one bin past 5 s differs at p < 0.05. Reproduced when the\n    merge point does not move later with temperature (18 >= 27 >= 29/29.5 >= 31 C, strictly\n    earlier at 31 than at 18 C), the 31 C curves satisfy one reading, and at 27 and 29/29.5 C\n    the 0 mM rate exceeds the 200 mM rate at p < 0.05 in at least one bin between 5 and 30 s.\n- id: fig7df-overall-rate-drops\n  statement: The overall egg-laying rate during search tends to fall as Kir2.1 expression\n    increases, meaning flies search longer before laying an egg.\n  source: Results, Dopa decarboxylase-expressing neurons, paragraph 5; Figure 7D to 7F\n  quote: The overall egg-laying rate during search tended to drop as Kir2.1 expression was\n    increased\n  criterion: Overall rate during search as all eggs over all search frames (M3, M4 counting over\n    all bins) times 120, per temperature. No test is reported. Reproduced when the rate at 31 C\n    is below that at 27 C and 27 C is not below... the rule taken is that the rate decreases\n    from 27 to 29/29.5 to 31 C, as the legend points to Fig. 7D to F; the 18 C value and the\n    median search duration per temperature are reported.\n- id: fig7gh-choice-falls\n  statement: Increasing Kir2.1 induction progressively lowers the fraction of eggs on 0 mM, and\n    DDC>Kir (31 C pre) flies lay more eggs on 200 than on 0 mM, consistent with spending more\n    time on the 200 mM side.\n  source: Results, Dopa decarboxylase-expressing neurons, paragraph 6; Figure 7G and 7H\n  quote: we found that increased induction of kir2.1 resulted in a progressive decrease in the\n    fraction of eggs laid on 0 mM\n  criterion: M6 per temperature; per-fly fraction of time on 0 mM (M1). Reproduced when the pooled\n    fraction decreases from 18 to 27 to 29/29.5 to 31 C, is below 0.5 at 31 C, and the median\n    time fraction on 0 mM at 31 C is below 0.5. The p-values of Fig. 7G are shown only in the\n    figure.\n- id: fig7ik-not-egg-number-or-motor\n  statement: The loss of preference in DDC>Kir flies is unrelated to the number of eggs laid or to\n    changes in the egg deposition motor program.\n  source: Results, Dopa decarboxylase-expressing neurons, paragraph 6; Figure 7I to 7K\n  quote: The decrease in egg-laying preference of DDC > Kir flies ( Fig. 7, C to F ) was\n    unrelated to the number of eggs laid ( Fig. 7I ) or to changes in the egg deposition motor\n    program\n  expected:\n  - quantity: eggs in the egg-aligned average at 18, 27, 29/29.5 and 31 C (1029, 761, 540, 533), 18 C\n    value: 1029\n    tolerance: 102.9\n  - quantity: eggs at 31 C\n    value: 533\n    tolerance: 53.3\n  criterion: Eggs per fly per temperature (Fig. 7I) and M7, M8 (Fig. 7J, K). No test is reported.\n    Reproduced when the Spearman correlation across flies between eggs laid and fraction on 0\n    mM within the 31 C group is not significant at p < 0.05 (a measure fixed here for\n    \"unrelated\"), and median pause times at 31 C are within 20% of 18 C (a working bound).\n- id: fig7l-dopamine-gal80-rescue\n  statement: Gal80 driven by TH or by R58E02 partially rescues the choice defect of DDC>Kir (31 C\n    pre) flies, and both together rescue it fully.\n  source: Results, Dopamine neurons within the Ddc-expressing population may be important,\n    paragraph 1; Figure 7L\n  quote: Expression of Gal80 by either of the abovementioned enhancers partially rescued the\n    choice defect in DDC > Kir (31°C pre) flies. With both enhancers driving Gal80, the choice\n    defect was fully rescued\n  statistics:\n  - test: two-sided Wilcoxon rank sum test, flies that laid at least 5 eggs, all displayed values\n    p: 0.001\n    p_relation: \"<\"\n  criterion: M6 for each genotype at 18 and 31 C pretreatment. \"Rescue\" is read as the 31 C\n    fraction relative to its 18 C sibling control. Reproduced when the 31 C fraction with TH-Gal80\n    or R58E02-Gal80 alone lies between that of DDC>Kir 31 C and its control, lower than its own\n    control at p < 0.001, and with both Gal80s does not differ from its control at p < 0.05.\n- id: fig7mn-brain-neurons\n  statement: Biasing Kir2.1 to DDC-Gal4 neurons in the brain (TSH-Gal80, or OTD-FLP with\n    TUB-FRT-Gal80-FRT) still leaves a choice defect, though smaller.\n  source: Results, Dopamine neurons within the Ddc-expressing population may be important,\n    paragraph 2; Figure 7M and 7N\n  quote: Flies still retain an egg-laying choice defect after Kir2.1 expression in the ventral\n    nerve cord is minimized with TSH-Gal80\n  statistics:\n  - test: two-sided Wilcoxon rank sum test, flies that laid at least 5 eggs, all displayed values\n    p: 0.001\n    p_relation: \"<\"\n  criterion: M6, 31 C against 18 C pretreatment within each genotype. Reproduced when both\n    brain-biased genotypes show a lower fraction on 0 mM at 31 C at p < 0.001, and the drop is\n    smaller than in DDC>Kir without the restricting transgene.\n- id: fig8a-d1-receptor-mutants\n  statement: Mutants of either dopamine D1-like receptor, Dop1R1 or Dop1R2, lower the fraction of\n    eggs on 0 mM below 0.5, as in DDC>Kir (31 C pre); mutants of the other dopamine and\n    serotonin receptors do not bring choice below 0.5.\n  source: Results, Dopamine signaling via Dop1R1 and Dop1R2, paragraph 1; Figure 8A\n  quote: decreased the fraction of eggs laid on 0 mM below 0.5 similar to the effect observed in\n    DDC > Kir (31°C pre) flies ( Fig. 7G , last bar). Mutants of other receptors did not bring\n    choice below 0.5.\n  statistics:\n  - test: two-sided Wilcoxon rank sum test, flies that laid at least 5 eggs, all displayed values\n    p: 0.001\n    p_relation: \"<\"\n  expected:\n  - quantity: mean eggs per fly for the 13 genotypes (40, 14, 7, 10, 10, 11, 12, 23, 15, 25, 19, 2, 16), CS\n    value: 40\n    tolerance: 4\n  criterion: M6 per genotype (Dop1R1-, Dop1R1 f02676, Dop1R2 attP, Dop1R2-, DopEcR-, DopEcR c02142,\n    Dop2R-, 5HT1a-, 5HT1b-, 5HT2a-, 5HT2b-, 5HT7-, and CS). Reproduced when the pooled fraction\n    on 0 mM is below 0.5 for all four Dop1R1 and Dop1R2 alleles and at or above 0.5 for the\n    others. The order of genotypes for the mean egg counts is shown only in the figure.\n- id: fig8b-mutants-sense-sucrose\n  statement: Starved Dop1R1-, Dop1R2 attP and Dop1R2- flies start feeding after touching sucrose\n    with their front tarsi, so they can sense sucrose.\n  source: Results, Dopamine signaling via Dop1R1 and Dop1R2, paragraph 2; Figure 8B\n  quote: When starved, all three mutant genotypes initiate feeding after touching sucrose with\n    their front tarsi\n  criterion: As fig7b-ddc-kir-sense-sucrose, for the three mutants.\n- id: fig8ce-mutants-flat-rates\n  statement: Dop1R1 and Dop1R2 mutants show similar egg-laying rate curves on 0 and 200 mM; the\n    Dop1R1 curves resemble the CS 0 mM curve and the Dop1R2 curves the CS 200 mM curve.\n  source: Results, Dopamine signaling via Dop1R1 and Dop1R2, paragraph 2; Figure 8C to 8E\n  quote: Dop1R1 mutant flies showed similar egg-laying rate curves on 0 and 200 mM, highlighting\n    an inability to compare the two options ( Fig. 8C ). Likewise, Dop1R2 mutant flies showed\n    similar rate curves on 0 and 200 mM sucrose\n  criterion: M4 and M5 per mutant. Similarity is judged, as for fig7cf reading (b), as at most one\n    bin past 5 s with the 0 mM rate above the 200 mM rate at p < 0.05. The resemblance to CS is\n    judged by the mean rate over bins 5 to 300 s; reproduced in full when, in addition, both\n    Dop1R1- curves are nearer the CS 0 mM curve and both Dop1R2 curves nearer the CS 200 mM\n    curve (a measure fixed here; the paper says \"look more like\").\n- id: fig8fg-time-and-eggs\n  statement: Dop1R1- and Dop1R2 attP flies spend more time on 200 mM, and the three mutants lay a\n    similar number of eggs and raise their speed before pausing to lay.\n  source: Results, Dopamine signaling via Dop1R1 and Dop1R2, paragraph 2; Figure 8F to 8I\n  quote: All three mutants, on average, lay a similar number of eggs ( Fig. 8G ) and increase\n    their locomotor speed (search) before pausing to deposit an egg\n  expected:\n  - quantity: eggs in the egg-aligned average, CS, Dop1R1-, Dop1R2 attP, Dop1R2- (1862, 498, 586, 323), Dop1R1-\n    value: 498\n    tolerance: 49.8\n  - quantity: eggs, Dop1R2 attP\n    value: 586\n    tolerance: 58.6\n  - quantity: eggs, Dop1R2-\n    value: 323\n    tolerance: 32.3\n  criterion: Per-fly fraction of time on 0 mM (M1) with median below 0.5 for Dop1R1- and Dop1R2\n    attP; eggs per fly compared among the three mutants by pairwise two-sided Wilcoxon rank sum\n    tests with no pair at p < 0.05 (a claim of similarity; no test is reported); speed rise as\n    in fig5gh.\n- id: fig8j-200-500-defect\n  statement: Dop1R1 and Dop1R2 mutants and DDC>Kir (31 C pre) flies are also defective in 200\n    against 500 mM choice.\n  source: Results, Dopamine signaling via Dop1R1 and Dop1R2, paragraph 3; Figure 8J\n  quote: Dop1R1 mutant, Dop1R2 mutant, and DDC > Kir (31°C pre) flies are, as expected, also\n    defective in 200 mM versus 500 mM sucrose choice\n  statistics:\n  - test: two-sided Wilcoxon rank sum test, flies that laid at least 5 eggs (P values as in Fig.\n      8A)\n    p: 0.001\n    p_relation: \"<\"\n  expected:\n  - quantity: mean eggs per fly in Fig. 8J and 8K (45, 15, 12, 17, 6, 38, 6, 3, 11, 2), first group\n    value: 45\n    tolerance: 4.5\n  criterion: Fraction of eggs on 200 mM (M6) against CS (mutants) or 18 C sibling controls (DDC>Kir).\n    Reproduced when each is lower than its control at p < 0.001.\n- id: fig8k-agarose-intact\n  statement: The same flies are not defective in 0.8% against 1.4% agarose choice, still laying a\n    large fraction of their eggs on 0.8%.\n  source: Results, Dopamine signaling via Dop1R1 and Dop1R2, paragraph 3; Figure 8K\n  quote: these flies are not defective in 0.8% versus 1.4% agarose choice\n  criterion: A claim of absence on the paper's test, M6 per-fly two-sided Wilcoxon rank sum test\n    against the control at p < 0.001 (the level printed for Fig. 8 P values). Reproduced when no\n    genotype has a lower fraction on 0.8% at that level; the fractions and the effect sizes are\n    reported. Few eggs were laid (as low as 2 per fly), so flies with fewer than 5 eggs are left\n    out of the test, as M6 says.\n- id: dop1r1-84714-no-defect\n  statement: A Dop1R1 mutant whose exon 1 is replaced by Gal4 (BDSC 84714) had no appreciable\n    choice defect, laying 87% of eggs on plain substrate over 90 flies, and was excluded from Fig.\n    8A.\n  source: Materials and Methods, Flies, paragraph 2\n  quote: A single Dop1R1 mutant (BDSC #84714) ( 41 ) assayed did not have an appreciable choice\n    defect (87% of eggs laid on plain; n = 90 flies)\n  expected:\n  - quantity: fraction of eggs on 0 mM\n    value: 0.87\n    tolerance: 0.087\n  - quantity: flies\n    value: 90\n    tolerance: 9\n  criterion: M6 for that genotype in 0 against 200 mM chambers, pooled fraction on 0 mM.\n- id: figs2-search-definition-robust\n  statement: The conclusions drawn from the rate functions hold under alternative definitions of\n    the search period (no 30-s minimum; 90 s before each egg; 15 min before each egg, each cut\n    at the previous egg plus 1 min).\n  source: Results, A framework, paragraph 3; fig. S2\n  quote: That said, all our conclusions are robust to varying definitions of the search period\n    (fig. S2).\n  depends_on:\n  - fig3ab-2mm-tunnel-faster\n  - fig4b-faster-middle-preferred\n  - fig5ab-strains-release-faster\n  - fig7cf-kir-merge-earlier\n  criterion: The rate-function claims listed are rerun under the three alternate definitions of\n    fig. S2's legend. Reproduced when each claim that is reproduced under the working\n    definition keeps its outcome under all three; partially reproduced when it keeps it under\n    two.\n- id: figs3-long-searches\n  statement: Flies still lay most eggs on low sucrose even after long searches with many\n    transitions (3979 eggs from 95 flies in 0/200, 0/500 and 200/500 mM chambers).\n  source: Results, A framework, paragraph 5; fig. S3\n  quote: flies still lay eggs on low sucrose even after very long searches that have many\n    transitions (fig. S3)\n  expected:\n  - quantity: eggs\n    value: 3979\n    tolerance: 397.9\n  - quantity: flies\n    value: 95\n    tolerance: 9.5\n  criterion: Searches M3 (no 30-s minimum), binned by duration (0, 30, 60, 90, 120, 240, 360, 1500\n    s, the ticks of fig. S3A) and by number of transitions (0, 1, 2, 3, 4, 5 to 9, 10 to 24, 25+),\n    fraction of eggs on the lower option with 95% Clopper-Pearson CI. Reproduced when the\n    fraction is above 0.5 in the longest-duration bin and the 25+ transitions bin, and the\n    counts are within tolerance.\n- id: figs4-models-fail\n  statement: Models that map sucrose history to egg-laying rate without a comparison to an\n    internal expectation (a history kernel, or an integral controller with a set point) fail to\n    reproduce key features of the rate functions.\n  source: Results, Flies lay eggs more rapidly on high-quality substrates, last paragraph;\n    Materials and Methods, Mathematical models; fig. S4\n  quote: Models that attempt to explain the observed behavior as a function of sucrose\n    concentration alone, without a comparison to an internal expectation, fail to reproduce\n    important aspects of the data\n  criterion: The kernel is fit with code and concepts from ref. 82 (not given here) and neither\n    the fit procedure nor the constants k1, k2 of model 2 are stated, and the failure is\n    described in words (model 1 overestimates the rate on transition from 500 to 0 mM in a\n    0/500 chamber when fit to 0/200). The method is not fixed by the paper; the author fits a\n    zero-area kernel to the 0/200 rate functions by least squares as one reading and judges\n    whether it overestimates the 500 to 0 mM rate in 0/500, and blocks the claim if no fit is\n    defensible.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/vijayan-2022.yaml",
 "old_string": "all bins) times 120, per temperature. No test is reported. Reproduced when the rate at 31 C\n    is below that at 27 C and 27 C is not below... the rule taken is that the rate decreases\n    from 27 to 29/29.5 to 31 C, as the legend points to Fig. 7D to F; the 18 C value and the\n    median search duration per temperature are reported.",
 "new_string": "all bins) times 120, per temperature. No test is reported. The text points to Fig. 7D to F,\n    so the comparison is over 27, 29/29.5 and 31 C. Reproduced when the rate decreases from 27\n    to 29/29.5 to 31 C; the 18 C value and the median search duration per temperature are\n    reported."
}
```

```
The file claims/vijayan-2022.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/vijayan-2022.yaml paper/10.1126-sciadv.abn3852.txt; grep -n -i "rather\|—" claims/vijayan-2022.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/vijayan-2022.yaml",
 "old_string": "  quote: A single Dop1R1 mutant (BDSC #84714) ( 41 ) assayed did not have an appreciable choice\n    defect (87% of eggs laid on plain; n = 90 flies)",
 "new_string": "  quote: \"A single Dop1R1 mutant (BDSC #84714) ( 41 ) assayed did not have an appreciable choice\n    defect (87% of eggs laid on plain; n = 90 flies)\""
}
```

```
The file claims/vijayan-2022.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
grep -n " #" claims/vijayan-2022.yaml | grep -v "^[0-9]*:#"; python tools/claims_check.py claims/vijayan-2022.yaml paper/10.1126-sciadv.abn3852.txt 2>&1 | tail -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
import yaml;d=yaml.safe_load(open('claims/vijayan-2022.yaml'))
c=d['claims'];print(len(c),sum('statistics' in x for x in c),sum(len(x.get('statistics',[])) for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c), [x['id'] for x in c if x.get('data')])
import re
for x in c:
  for k,v in x.items():
    if isinstance(v,str) and ': ' in v: print('colon',x['id'],k)
"
```

```
45 9 10 45 19 ['fig7a-screen-ddc-hits']
```

**Agent**

I wrote `claims/vijayan-2022.yaml`, and the quote checker passes: 45 claims, 45 quotes, 10 statistical values, 0 problems. Nothing was committed.

**Text read:** the version of record from Europe PMC (PMC9616500), `paper/10.1126-sciadv.abn3852.txt`. That covers the main text, figure legends, Materials and Methods, and the supplement PDF (Figs. S1 to S7, plus the legends for Tables S1 and S2 and Movies S1 to S3). I opened no PDF pages. The paper links no code (the analysis was done in MATLAB), so no method detail is settled by code.

**Claims:**
- **Quotes:** all 45 have one; none needed an `inferred` note.
- **Statistics:** 9 claims carry 10 entries. All tests are two-sided Wilcoxon rank sum; the p-values are bounds of < 0.001 or < 0.005, and Fig. 1F's are Bonferroni-corrected for seven comparisons.
- **Expected values:** 19 claims, at 10% tolerance. The exceptions are the line count of 115 (exact) and the merge points of about 20 s (one bin, ±5 s).
- **Criteria:** all 45 have one.
- **Data:** one claim, the Fig. 7A screen, is `with_labels`, because the line identities are in Table S2. All others use the dataset.
- **Shared methods:** eight are defined once in the opening comment and named by label in the criteria: island assignment, speed, search period, rate function, bin test, choice fraction, pause time, and egg-aligned speed.

**Details the paper leaves open, with the readings named:**
- **Island boundaries in multi-island chambers:** taken from the fig. S1 geometry.
- **Locomotor speed:** frame-to-frame displacement at 2 frames per second, as a standard choice.
- **Search start:** going back from the egg, the first frame where the 18.5-s smoothed speed is below 0.1 mm/s, with a centred filter (the 9-s minimum implies one). Searches under 30 s are padded back to 30 s.
- **Rate-function bin edges:** read from the fig. S2 axis ticks (0, 5, 10, 15, 20, 25, 30, 45, 60, 90, 150, 300, 600, 1200, 7200 s).
- **"Trial" in the bin test:** (a) each visit to the bin; (b) each search that enters the bin.
- **Which two-choice chambers are pooled for the 964/1205 and 918/2744 counts:** (a) the ref. 16 chambers only; (b) those plus this paper's.
- **Fig. 1F:** which pairs the three p-values compare (each glued group against the unglued control, or against its own control).
- **Fig. 2E to G, "nearly completely":** the 200 mM rate at most 10% or at most 20% of the 0 mM rate.
- **Fig. 3D, the "fast egg" clock:** counted from crossing the midline or from leaving 200 mM.
- **Fig. 4A transits:** every visit, or pass-through visits only; medians pooled or per chamber.
- **Fig. 4B:** the indicated bin (5 to 10 s, 0 to 5 s, or 10 to 15 s).
- **Fig. 4E:** which chamber each shade is; the Fig. 4A order is taken, with all six orders shown if it fails.
- **Fig. 6G:** time on 0.8% over all frames or only search frames.
- **Fig. 7A:** hits ranked by fold change or by p.
- **Fig. 7F, "nearly superimposable":** the merge point is the first bin past 5 s, or at most one bin differs.
- **Claims with no test in the paper:** where a claim says "gradually increased", "similar", "unrelated" or "look more like", I fixed a working measure in its criterion and said so.
- **Fig. S4 models:** the kernel fitting comes from ref. 82 and is not described here. I named one reading (a least-squares fit of a zero-area kernel to the 0/200 rate functions), with a block if no fit is defensible.

**Missing from the paper:**
- **Tables S1 and S2:** these are separate spreadsheets, not in the text. S1 summarises all tracking data and holds a p-value the Fig. 4B claim cites; S2 has the screen's line identities.
- **The main-text PDF:** numbers printed only inside main figures could not be read. That includes most bin p-values, the merge-arrow positions, the order of groups in Fig. 8A, and the sucrose levels of the Fig. 6B bars.
- **Ref. 16:** the Methods defer chamber design, tracking and egg annotation to it, and it is not under `paper/`.
- **Two claims probably need hand-scored video:** the latency-to-feeding claims (Figs. 7B and 8B). The dataset is described as holding tracking data, so these may not be testable.

## End of run

22 turns, 6 minutes, $1.90 at API prices, result: success.
