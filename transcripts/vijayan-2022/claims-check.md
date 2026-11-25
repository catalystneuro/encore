# vijayan-2022 · claims-check · run 45514661848

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls paper/ claims/ | head; grep -n "Reader" -A60 docs/protocol.md | head -150; cat claims/vijayan-2022.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
ls paper/; grep -n "Reader" docs/protocol.md | head; wc -l claims/vijayan-2022.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/vijayan-2022.yaml"
}
```

```
1	# Claims for Vijayan, Wang, Chandra, Chakravorty, Li, Sarbanes, Akhlaghpour & Maimon (2022),
2	# "An internal expectation guides Drosophila egg-laying decisions", Science Advances 8,
3	# eabn3852, on DANDI 000212 ("Tracking of Drosophila during egg-laying decisions").
4	#
5	# Provenance: written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub
6	# Actions"), 2026-11-25, protocol pilot-18 as stated in docs/protocol.md (Reader, steps 1 to 4).
7	#
8	# Text read: the version of record as served by Europe PMC (PMC9616500), in
9	# paper/10.1126-sciadv.abn3852.txt, with the main text, figure legends, Materials and Methods,
10	# and the supplement PDF (sciadv.abn3852_sm.pdf, Figs. S1 to S7 with legends and the legends of
11	# Tables S1 and S2 and Movies S1 to S3), extracted into the same file. No page of a PDF was
12	# opened. Not available here: Tables S1 (summary of all tracking data) and S2 (the Gal4 screen),
13	# which are separate spreadsheets, and the main-text PDF, so numbers printed only inside main
14	# figures (most bin p-values, merge-arrow positions, bar heights) could not be read. The Methods
15	# defer the chamber design, tracking and egg annotation to ref. 16 (Vijayan et al., the
16	# rise-to-threshold study), which is not under paper/.
17	#
18	# Code read: none. The paper links no code; "All data analyses were done using MATLAB" (Data
19	# analysis software). No method detail below is settled by code.
20	#
[... 814 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 43,140p docs/protocol.md; python tools/claims_check.py claims/vijayan-2022.yaml paper/10.1126-sciadv.abn3852.txt; wc -c paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 140,230p docs/protocol.md
```

```
when it does; give the size of the effect either way. The rule for
     several readings does not apply: absence is judged on the paper's test
     alone, as written, even when the test mixes in a condition that does
     not belong (show the cleaner test as a variant).
   - If a criterion turns out unable to decide (two candidates tied), break
     the tie as the paper's methods or code imply, record it as a deviation,
     and show the other result.
   - `data`: what the paper's test of the finding uses, from the paper:
     `dataset` (the default: the data the paper describes recording),
     `with_labels`, `with_inputs` or `elsewhere` (step 4, and author, step
     4). Whether the dataset holds those data is the author's to find.
   - `depends_on`: the claims whose result this one uses, such as the cells
     another claim selects.
   - `datasets`: only when the paper is tested on more than one dataset (its
     `papers/datasets/<paper>.yaml` lists several): the folder names of the
     ones the claim rests on. With one dataset, leave it out; every claim
     rests on it. A claim on data in none of them is `data: elsewhere`, or
     rests on a dataset listed as not available.
   - A paper that reuses its datasets (`relation: reuses` in
     `papers/datasets/<paper>.yaml`) is read like any other: its claims are
[... 71 more lines not kept]
```

**Agent**

Now the paper. It's ~120KB; I'll read it fully.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1126-sciadv.abn3852.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; python3 -c "
t=open('10.1126-sciadv.abn3852.txt').read()
print(t[52300:90000])"
```

```
<persisted-output>
Output too large (37KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-runner-encore-runner/844592e6-e4d3-4f9e-b457-5e545954b47d/tool-results/bbeulhxoe.txt

Preview (first 2KB):
nts one fly. ( G ) Eggs laid per fly. Each dot represents one fly. ( H and I ) Mean locomotor speed aligned to egg deposition. In total, 1862, 498, 586, and 323 eggs for CS, Dop1R1 − , Dop1R2 attP , and Dop1R2 − , respectively. ( J and K ) Fraction of eggs on 200 mM (J) or 0.8% (K) with 95% confidence interval. Each dot represents one fly. Flies laid an average of 45, 15, 12, 17, 6, 38, 6, 3, 11, and 2 eggs per fly, respectively. P values as in (A). These genotypes lay fewer eggs, overnight, in chambers without a food source (e.g., sucrose) but still lay a large fraction of their eggs on 0.8%. DDC > Kir flies have tubulin promoter driving Gal80 ts . In (A) and (F) to (I), CS data are from ( 16 ). We performed more detailed experiments on all three of the putative null mutants for either Dop1R—Dop1R1 − , Dop1R2 attP , and Dop1R2 − . When starved, all three mutant genotypes initiate feeding after touching sucrose with their front tarsi, indicating that they retain the ability to generally sense sucrose ( Fig. 8B ). Dop1R1 mutant flies showed similar egg-laying rate curves on 0 and 200 mM, highlighting an inability to compare the two options ( Fig. 8C ). Likewise, Dop1R2 mutant flies showed similar rate curves on 0 and 200 mM sucrose ( Fig. 8, D and E ). However, the egg-laying rate curves for Dop1R1 and Dop1R2 mutants appear qualitatively different. Both the 0 and 200 mM rate curves for Dop1R1 mutants look more like the 0 mM rate curve for CS flies ( Fig. 8C , light gray shaded curve), while both the 0 and 200 mM rate curves for Dop1R2 mutants look more like the 200 mM rate curve for CS flies ( Fig. 8C , dark gray shaded curve). This difference might hint at different roles for these receptors in expectation-related calculations. The fact that 
[... 2 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-runner-encore-runner/844592e6-e4d3-4f9e-b457-5e545954b47d/tool-results/bbeulhxoe.txt"
}
```

```
1	nts one fly. ( G ) Eggs laid per fly. Each dot represents one fly. ( H and I ) Mean locomotor speed aligned to egg deposition. In total, 1862, 498, 586, and 323 eggs for CS, Dop1R1 − , Dop1R2 attP , and Dop1R2 − , respectively. ( J and K ) Fraction of eggs on 200 mM (J) or 0.8% (K) with 95% confidence interval. Each dot represents one fly. Flies laid an average of 45, 15, 12, 17, 6, 38, 6, 3, 11, and 2 eggs per fly, respectively. P values as in (A). These genotypes lay fewer eggs, overnight, in chambers without a food source (e.g., sucrose) but still lay a large fraction of their eggs on 0.8%. DDC > Kir flies have tubulin promoter driving Gal80 ts . In (A) and (F) to (I), CS data are from ( 16 ). We performed more detailed experiments on all three of the putative null mutants for either Dop1R—Dop1R1 − , Dop1R2 attP , and Dop1R2 − . When starved, all three mutant genotypes initiate feeding after touching sucrose with their front tarsi, indicating that they retain the ability to generally sense sucrose ( Fig. 8B ). Dop1R1 mutant flies showed similar egg-laying rate curves on 0 and 200 mM, highlighting an inability to compare the two options ( Fig. 8C ). Likewise, Dop1R2 mutant flies showed similar rate curves on 0 and 200 mM sucrose ( Fig. 8, D and E ). However, the egg-laying rate curves for Dop1R1 and Dop1R2 mutants appear qualitatively different. Both the 0 and 200 mM rate curves for Dop1R1 mutants look more like the 0 mM rate curve for CS flies ( Fig. 8C , light gray shaded curve), while both the 0 and 200 mM rate curves for Dop1R2 mutants look more like the 200 mM rate curve for CS flies ( Fig. 8C , dark gray shaded curve). This difference might hint at different roles for these receptors in expectation-related calculations. The fact that Dop1R1 − and Dop1R2 attP flies laid more eggs on 200 mM than on 0 mM is consistent with them spending more time, overall, on the 200 mM side ( Fig. 8F ) alongside their roughly similar egg-laying rates for both substrates ( Fi
[... 1 more lines not kept]
```

**Agent**

Now the supplement part.

**Agent calls Bash**

```bash
python3 -c "
t=open('10.1126-sciadv.abn3852.txt').read()
i=t.find('Fig. S1')
import re
j=[m.start() for m in re.finditer('Supplementary Materials for|Fig. S2|fig. S2', t)]
print(j)
k=t.rfind('REFERENCES AND NOTES')
print(len(t))
"; python3 -c "
t=open('10.1126-sciadv.abn3852.txt').read()
i=t.find('SUPPLEMENT')
print(i)
import re
for m in re.finditer(r'={3,}|-{5,}', t): print(m.start(), t[m.start():m.start()+200].replace('\n',' '))
"
```

```
[17074, 30588, 77288, 113472, 113969, 114403, 116444]
121815
-1
303 ------------------------------------------------------------------------ pmc Sci Adv Sci Adv 2850 sciadv 101653440 sciadv Science Advances 2375-2548 American Association for the Advancement of Science
113457 === page 1 === Supplementary Materials for An internal expectation guides Drosophila egg-laying decisions Vikram Vijayan et al. Corresponding author: Vikram Vijayan, [removed: an e-mail address]; Gaby Mai
113468 === Supplementary Materials for An internal expectation guides Drosophila egg-laying decisions Vikram Vijayan et al. Corresponding author: Vikram Vijayan, [removed: an e-mail address]; Gaby Maimon, maimon
113944 === page 2 ===           Supplementary Materials for    An internal expectation guides Drosophila egg-laying decisions    Vikram Vijayan*, Zikun Wang, Vikram Chandra, Arun Chakravorty, Rufei Li, Steph
113955 ===           Supplementary Materials for    An internal expectation guides Drosophila egg-laying decisions    Vikram Vijayan*, Zikun Wang, Vikram Chandra, Arun Chakravorty, Rufei Li, Stephanie L.  Sa
114521 === page 3 ===     Table S1. Summary of all tracking data.     Table S2. Summary of screen for egg-laying choice related neurons. All data in Fig. 7A is  reported in increasing order of the x-axis in 
114532 ===     Table S1. Summary of all tracking data.     Table S2. Summary of screen for egg-laying choice related neurons. All data in Fig. 7A is  reported in increasing order of the x-axis in Fig. 7A. Da
115173 === page 4 === 20 mm ~2.5 mm A B D F 20 mm 20 mm 32 mm 20 mm 56 mm 15 mm 61 mm ~2 mm ~1 mm 44 mm E Fig S1.  ~2.5 mm ~2.5 mm 20 mm ~2.5 mm C slideable tab ~2.5 mm 15 mm 61 mm ~4 mm ~1 mm H 61 mm G slid
115184 === 20 mm ~2.5 mm A B D F 20 mm 20 mm 32 mm 20 mm 56 mm 15 mm 61 mm ~2 mm ~1 mm 44 mm E Fig S1.  ~2.5 mm ~2.5 mm 20 mm ~2.5 mm C slideable tab ~2.5 mm 15 mm 61 mm ~4 mm ~1 mm H 61 mm G slideable tab s
115769 === page 5 === 0 2 4 0 5 10 15 20 25 45 60 90 150 300 600 72
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
t=open('10.1126-sciadv.abn3852.txt').read()
print(t[113457:])"
```

```
=== page 1 ===
Supplementary Materials for
An internal expectation guides Drosophila egg-laying decisions
Vikram Vijayan et al.
Corresponding author: Vikram Vijayan, [removed: an e-mail address]; Gaby Maimon, [removed: an e-mail address]
Sci. Adv. 8, eabn3852 (2022)
DOI: 10.1126/sciadv.abn3852
The PDF file includes:
Figs. S1 to S7
Legends for tables S1 and S2
Legends for movies S1 to S3
Other Supplementary Material for this manuscript includes the following:
Tables S1 and S2
Movies S1 to S3

=== page 2 ===
 
 
 
 
[... 660 more lines not kept]
```

**Agent**

Checker passes. Now the edits, from my reading of the paper.

**Agent calls Bash**

```bash
cd .. && python3 - <<'EOF'
p='claims/vijayan-2022.yaml'
s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1, a
    s=s.replace(a,b)
rep("""flies in two-choice sucrose chambers; island at search start and whether the fly crosses to
    the other island before the egg, by M1. Which chambers are pooled is open; readings (a) the
    0/200, 0/500 and 200/500 mM chambers of ref. 16, as for fig. S3; (b) those three with any
    CS two-choice sucrose chamber of this paper. Reproduced when, under one reading, both
    fractions are within tolerance""","""flies in the 0/200, 0/500 and 200/500 mM two-choice chambers of ref. 16 (the sentence cites
    ref. 16, and its 1205 + 2744 = 3949 searches match the 3979 eggs of those three chambers in
    fig. S3); island at search start and whether the fly crosses to the other island before the
    egg, by M1. Reproduced when both fractions are within tolerance""")
rep("""lower sucrose option is above 0.5 with its 95% Clopper-Pearson CI above 0.5. The paper
    reports no test;""","""lower sucrose option is above 0.5 with its 95% Clopper-Pearson CI above 0.5 (a bound fixed
    here from the 0.5 line the legend draws for reference). The paper reports no test;""")
rep("""  - about: three displayed comparisons, top to bottom
    test: two-sided""","""  - about: first and second displayed comparisons, top to bottom
    test: two-sided""")
rep("""p-values compare are shown only in the figure, which could not be read; readings (a) each
    glued group against the unglued control; (b) each glued group against its own control.""","""p-values compare are shown only in the figure, which could not be read. The legend's
    Bonferroni correction for seven comparisons among eight groups fits one control against
    the seven other groups; reading taken, each glued group against the unglued control. If the
    dataset shows a separate control for each glued group, each glued group is compared with
    its own control as a second reading.""")
rep("""  criterion: Merge point by M5 (first bin past 5 s with P > 0.05) of the 0 mM and 200 mM curves
    (each since leaving the other) in each three-choice chamber of claim fig2efg against the CS
    0/200 two-choice chamber. Reproduced when the merge bin is earlier in at least two of the
    three three-choice chambers.""","""  criterion: Merge point by M5 (first bin past 5 s with P > 0.05) of the 0 mM and 200 mM curves
    (each since leaving the other) in each three-choice chamber of claim fig2efg. The text
    compares with Fig. 2, A to C; readings (a) against the CS 0/200 two-choice chamber of ref.
    16, whose curves do not merge within the plotted interval (Fig. 5A legend); (b) against
    that chamber and the 0/200/200 and five-island chambers of Fig. 2B and 2C. Reproduced when,
    under one reading, the merge bin is earlier than in every comparison chamber in at least
    two of the three three-choice chambers.""")
rep("""partially reproduced when it holds in two. Bins below 5 s are left out as the paper
    describes a low rate for every curve in the first seconds after a transition.""","""partially reproduced when it holds in two. Bins below 5 s are left out, as in the merge-point
    definition (Fig. 5A legend); the paper says every rate function starts low for the first 10
    s after a transition (Results, A framework, last paragraph), so a 10 to 30 s window is also
    shown.""")
rep("""  criterion: As fig3ab-2mm-tunnel-faster, the bounce chamber's 5 to 10 s bin against the same
    bin of each tunnel chamber by M5 (Fig. 3 legend).""","""  criterion: As fig3ab-2mm-tunnel-faster, the bounce chamber's indicated bin against the same
    bin of each tunnel chamber by M5 (Fig. 3 legend). The text names the bin for Fig. 3B (5 to
    10 s) but not for Fig. 3C, whose arrow is only in the figure; readings (a) 5 to 10 s; (b) 0
    to 5 s.""")
rep("""The order of shades is read as Fig. 3A,
    B, C (4-mm, 2-mm, bounce), from "progressively more time" in the text.""","""The order of shades is Fig. 3A, B, C
    (4-mm, 2-mm, bounce): the Fig. 3F legend gives the second shade's 918 eggs as "two less than
    (B)", with shades "as colored in (D)".""")
rep("""x-axis of Fig. 3E are not in the text; the M4 edges are used as a standard choice.
    Reproduced when the pooled rate for previous visits longer than 240 s is higher than for
    shorter visits by M5 at p < 0.05, and the bins below 240 s show no rising trend.""","""x-axis of Fig. 3E are not in the text; the M4 edges up to 150 s, then 150 to 240 s and 240 s
    onward, are used, 240 s being the text's ~4 min. Reproduced when the pooled rate for previous
    visits longer than 240 s is higher than for shorter visits by M5 at p < 0.05, and the bins
    below 240 s show no rising trend.""")
rep("""  criterion: Egg-aligned speed M8 and pause time M7. The paper gives no test; a claim of
    similarity is judged by M7 pause times of fast eggs against all eggs of each chamber with
    the two-sided Wilcoxon rank sum test.""","""  criterion: Egg-aligned speed M8 and pause time M7. The paper gives no test; a claim of
    similarity is judged by M7 pause times of fast eggs against all eggs of each chamber with
    the two-sided Wilcoxon rank sum test. The legend gives no count for the pink fast-egg trace,
    so whether it pools the three chambers is open; readings (a) fast eggs of each chamber
    against that chamber's eggs; (b) fast eggs pooled over the three chambers against each
    chamber's eggs.""")
rep("""  statistics:
  - about: indicated bin against a 0/500/500 chamber (Table S1)""","""  statistics:
  - about: indicated bin against the same bins of the gray reference curves (the legend's "also
      <0.001" for the 0/500/500 comparison implies this one is below 0.001 too)
    test: two-sided Wilcoxon rank sum test
    p: 0.001
    p_relation: "<"
  - about: indicated bin against a 0/500/500 chamber (Table S1)""")
rep("""s, as in Fig. 3; (b) 0 to 5 s; (c) 10 to
    15 s. Reproduced when, under one reading, the middle-preferred rate is higher by M5 at p <
    0.05 against the pooled edge chambers and at p < 0.001 against 0/500/500.""","""s, as in Fig. 3; (b) 0 to 5 s; (c) 10 to
    15 s. Whether the gray curves are pooled for the test is open; readings (i) pooled; (ii) each
    of the three. Reproduced when, under one reading, the middle-preferred rate is higher by M5
    at p < 0.001 against the edge chambers and against 0/500/500.""")
rep("""Reproduced when both fractions are within tolerance, bars 2 and 3 are below 0.5, and bars 4
    and 5 are within 0.1 of bar 1;""","""Reproduced when both fractions are within tolerance, bars 2 and 3 are below 0.5, and bars 4
    and 5 are within 0.1 of bar 1 (a bound fixed here for "little effect");""")
rep("""  statement: Of 115 Gal4 lines in a Kir2.1 screen of 0 against 200 mM choice, 110 controls (96%)
    laid more eggs on 0 mM""","""  statement: Of 115 Gal4 lines in a Kir2.1 screen of 0 against 200 mM choice, 110 (96%) laid more
    eggs on 0 mM in the control condition""")
rep("""Ranking of hits is open; readings
    (a) by fold change, lowest first; (b) by p, lowest first.""","""Ranking of hits is open; readings
    (a) by fold change, lowest first, the order of Table S2 and fig. S5 ("increasing order of
    the x-axis in Fig. 7A"); (b) by p, lowest first. The Fig. 7A legend labels the top three
    lines among those with at least 5 eggs per fly in both conditions, so each reading is also
    run on those lines only.""")
rep("""  criterion: Eggs per fly per temperature (Fig. 7I) and M7, M8 (Fig. 7J, K). No test is reported.
    Reproduced when the Spearman correlation across flies between eggs laid and fraction on 0
    mM within the 31 C group is not significant at p < 0.05 (a measure fixed here for
    "unrelated"), and median pause times at 31 C are within 20% of 18 C (a working bound).""","""  criterion: Eggs per fly per temperature (Fig. 7I) and M7, M8 (Fig. 7J, K). No test is reported;
    the figure shows eggs per fly per group, so "unrelated" is read as eggs per fly at 31 C not
    lower than at 18 C by the paper's test for groups of flies, the two-sided Wilcoxon rank sum
    test (Methods, Statistics), at p < 0.05. Reproduced when that holds and median pause times
    at 31 C are within 20% of 18 C (a working bound fixed here). The Spearman correlation across
    31 C flies between eggs laid and fraction on 0 mM is reported as a variant.""")
rep("""and with both Gal80s does not differ from its control at p < 0.05.""","""and with both Gal80s does not differ from its control at p < 0.05. Which pairs the displayed
    P values compare is shown only in the figure; the comparisons used here are a reading.""")
rep("""  - quantity: mean eggs per fly for the 13 genotypes (40, 14, 7, 10, 10, 11, 12, 23, 15, 25, 19, 2, 16), CS""","""  - quantity: mean eggs per fly for the 13 genotypes (40, 14, 7, 10, 10, 11, 12, 23, 15, 25, 19, 2, 16), first group in the figure's order (taken as CS, an assumption; the order is only in the figure)""")
rep("""  criterion: A claim of absence on the paper's test, M6 per-fly two-sided Wilcoxon rank sum test
    against the control at p < 0.001 (the level printed for Fig. 8 P values).""","""  criterion: A claim of absence on the paper's test, M6 per-fly two-sided Wilcoxon rank sum test
    against the control at p < 0.05, the significance level the paper states (Fig. 1F legend);
    the result at p < 0.001, the level printed for Fig. 8 P values, is shown as a variant.""")
rep("""  statement: The conclusions drawn from the rate functions hold under alternative definitions of
    the search period (no 30-s minimum; 90 s before each egg; 15 min before each egg, each cut
    at the previous egg plus 1 min).""","""  statement: The conclusions drawn from the rate functions hold under alternative definitions of
    the search period (no 30-s minimum; 90 s before each egg; 15 min before each egg; the last
    two shortened so as not to reach back past the previous egg plus 1 min).""")
rep("""  - fig3ab-2mm-tunnel-faster
  - fig4b-faster-middle-preferred
  - fig5ab-strains-release-faster
  - fig7cf-kir-merge-earlier""","""  - fig3ab-2mm-tunnel-faster
  - fig3c-bounce-faster
  - fig4b-faster-middle-preferred
  - fig5ab-strains-release-faster
  - fig5c-suzukii-no-preference
  - fig7cf-kir-merge-earlier""")
s=s.rstrip('\n')+"""
checks:
- date: 2026-11-25
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - leave-higher-stay-lower, dropped the reading that pools this paper's chambers; the sentence cites ref. 16 and its 3949 searches match the 3979 eggs of the three ref. 16 chambers in fig. S3.
  - fig1d-no-substrate-marking, marked the CI-above-0.5 bound as fixed here, as the paper gives no test.
  - fig1f-tarsi-proboscis, the first statistics entry covers only the first two comparisons (P < 0.005), the third being P < 0.001.
  - fig1f-tarsi-proboscis, the legend's seven Bonferroni comparisons among eight groups fit one control against seven groups, so that is the reading taken; own controls only if the dataset shows them.
  - fig2-earlier-merge-three-choice, the text compares with Fig. 2A to C, not the 0/200 chamber alone; added the reading with the Fig. 2B and 2C chambers and noted that the CS 0/200 curves do not merge (Fig. 5A legend).
  - fig2efg-inhibit-200-after-0, corrected the reason for leaving out bins below 5 s (the paper says rates start low for the first 10 s) and added a 10 to 30 s window as a shown variant.
  - fig3c-bounce-faster, the indicated bin of Fig. 3C is not named in the text; named it as open with readings.
  - fig3d-dwell-before-fast-eggs, the shade order is fixed by the Fig. 3F legend (918 eggs, two less than (B)), not only by the text's wording.
  - fig3e-rate-after-long-absence, the 240 s split was not an edge of the M4 bins; set the bins so it is.
  - fig3f-motor-program-not-faster, whether the pink fast-egg trace pools chambers is not stated; added both readings.
  - fig4b-faster-middle-preferred, the legend's "also <0.001" implies the gray-curve comparison is P < 0.001; added it as a statistic and raised the criterion from p < 0.05 to p < 0.001; named pooling of the gray curves as open.
  - fig6b-softer-preferred, marked the 0.1 bound for "little effect" as fixed here.
  - fig7a-screen-ddc-hits, the 110 lines are lines in the control condition, not controls; ranking reading (a) is the order of Table S2 and fig. S5; added the legend's at-least-5-eggs subset.
  - fig7ik-not-egg-number-or-motor, replaced the made-up within-group Spearman test with a comparison of eggs per fly at 31 C against 18 C by the paper's test for groups of flies; the correlation stays as a variant.
  - fig7l-dopamine-gal80-rescue, noted that the displayed comparisons are only in the figure, so the ones used are a reading.
  - fig8a-d1-receptor-mutants, the expected value labelled the first mean (40) as CS while the criterion says the order is only in the figure; relabelled it as the first group, CS assumed.
  - fig8k-agarose-intact, an absence claim is judged at the paper's stated significance level (P < 0.05, Fig. 1F legend), not at p < 0.001, which made absence easier to find; p < 0.001 kept as a variant.
  - figs2-search-definition-robust, added fig3c-bounce-faster and fig5c-suzukii-no-preference, whose chambers are in fig. S2; clarified that only the last two definitions are cut at the previous egg plus 1 min.
  - Open, paragraph numbers in sources could not be checked, as the text has no paragraph breaks.
  - Open, fig7a-screen-ddc-hits, the 10% tolerance on 110 and 111 lines allows up to 115 lines, close to meaningless for a count of lines; kept as the protocol's default, since the paper gives no spread.
  - Open, numbers printed only inside figures (bin P values, arrows, group order of Figs. 1F, 7L to N, 8A) could not be read; the main-text PDF is not under paper/.
"""
open(p,'w').write(s)
EOF
python tools/claims_check.py claims/vijayan-2022.yaml paper/10.1126-sciadv.abn3852.txt; grep -n ': .*: ' claims/vijayan-2022.yaml | grep -v '^\s*#' | tail -5
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -i 's/(4-mm, 2-mm, bounce): the Fig. 3F legend/(4-mm, 2-mm, bounce), as the Fig. 3F legend/' claims/vijayan-2022.yaml && python tools/claims_check.py claims/vijayan-2022.yaml paper/10.1126-sciadv.abn3852.txt; grep -nE '[^ ]: [^ ]' claims/vijayan-2022.yaml | grep -vE '^[0-9]+:\s*(#|- )?[a-z_]+: ' | head; grep -nP '—|rather' claims/vijayan-2022.yaml | grep -v '^[0-9]*:#'; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

I checked `claims/vijayan-2022.yaml` against the paper, made 18 corrections, and the file is ready for an attempt.

**Checker result:** `claims/vijayan-2022.yaml: 45 claims, 45 quotes, 11 statistical values, 0 problems`. Before my edits it gave the same line with 10 statistical values; the new one is the `fig4b` p-value below.

**Changes, by claim** (each is also logged under `checks`):
- **leave-higher-stay-lower:** Dropped the reading that pools this paper's own chambers. The sentence cites ref. 16, and its 1205 + 2744 = 3949 searches match the 3979 eggs from the three ref. 16 chambers in fig. S3.
- **fig1d-no-substrate-marking:** Marked the "CI above 0.5" bound as set by the file, since the paper reports no test.
- **fig1f-tarsi-proboscis:** The first statistics entry wrongly covered all three comparisons at P < 0.005. It now covers the first two; the third is P < 0.001. The legend's Bonferroni correction for seven comparisons among eight groups fits one control against seven groups, so that is now the reading taken.
- **fig2-earlier-merge-three-choice:** The text compares against Fig. 2A to C, not the 0/200 chamber alone. I added a reading that includes the Fig. 2B and 2C chambers, and noted that the CS 0/200 curves never merge (Fig. 5A legend).
- **fig2efg-inhibit-200-after-0:** The stated reason for leaving out bins below 5 s misdescribed the paper, which says rates start low for the first 10 s. I corrected it and added a 10 to 30 s window as a variant.
- **fig3c-bounce-faster:** The text does not name the bin marked with an arrow in Fig. 3C. It is now marked open, with readings 5 to 10 s and 0 to 5 s.
- **fig3d-dwell-before-fast-eggs:** The order of the gray shades is settled by the Fig. 3F legend (918 eggs, "two less than (B)"), not just by the text's wording.
- **fig3e-rate-after-long-absence:** The 240 s split was not one of the M4 bin edges. I set the bins so it is.
- **fig3f-motor-program-not-faster:** The legend does not say whether the fast-egg trace pools the three chambers, so both readings are listed.
- **fig4b-faster-middle-preferred:** The legend's "also <0.001" implies the main comparison is also P < 0.001. I added it as a statistic and raised the criterion from p < 0.05 to p < 0.001. Whether the gray reference curves are pooled is now marked open.
- **fig6b-softer-preferred:** Marked the 0.1 bound for "little effect" as set by the file.
- **fig7a-screen-ddc-hits:**
  - The statement now says the 110 are lines tested in the control condition, not "controls".
  - Ranking by fold change matches the order of Table S2 and fig. S5.
  - Each ranking is also run on only the lines with at least 5 eggs per fly, as the Fig. 7A legend does.
- **fig7ik-not-egg-number-or-motor:** Replaced an invented Spearman test with the paper's own test for groups of flies (eggs per fly, 31 C against 18 C). The correlation is kept as a variant.
- **fig7l-dopamine-gal80-rescue:** Noted that which comparisons are displayed is only in the figure, so the ones used are a reading.
- **fig8a-d1-receptor-mutants:** The expected value named the first mean (40) as CS, while the criterion says the order is only in the figure. It is now "first group, CS assumed".
- **fig8k-agarose-intact:** This is a claim that there is no effect, and it was judged at p < 0.001, which makes finding no effect easier. It is now judged at P < 0.05, the level the paper states (Fig. 1F legend); p < 0.001 is kept as a variant.
- **figs2-search-definition-robust:** Added `fig3c` and `fig5c` to `depends_on`, since their chambers are in fig. S2. Clarified that only the last two alternative definitions are cut at the previous egg plus 1 min.

**Still open (logged, not settled):**
- Paragraph numbers in the sources can't be checked, because the text file has no paragraph breaks.
- In `fig7a`, the default 10% tolerance on 110 and 111 lines allows up to 115, which says almost nothing for a count of lines. I kept it because the paper gives no spread.
- Numbers printed only inside the main figures (bin p-values, merge arrows, group order in Figs. 1F, 7L to N and 8A) can't be read, because the main-text PDF is not under `paper/`.

Every main finding has a claim. All claims come from this paper; the leave-higher numbers rest on ref. 16 data, but this paper reports them with its own p-value.

**Ready:** yes (`ready: true`). Nothing is committed or pushed.

## End of run

13 turns, 4 minutes, $1.35 at API prices, result: success.
