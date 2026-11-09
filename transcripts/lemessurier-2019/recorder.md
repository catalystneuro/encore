# crcns-ssc-10 · recorder · run 42521306388

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; ls claims/crcns-ssc-10/ transcripts/crcns-ssc-10/; python tools/readme_row.py crcns-ssc-10; cat attempts/crcns-ssc-10-lemessurier-2019-01.yaml; ls docs/pilot-notes | grep ssc-10
```

```
<persisted-output>
Output too large (76.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/f57ad030-7ac5-43d6-8084-19edbddf1437/tool-results/b1zqgoi8u.txt

Preview (first 2KB):
docs/pilot-notes/crcns-hc-28-jadhav-2016-01.md
docs/pilot-notes/crcns-hc-13-yu-2017-01.md
docs/pilot-notes/crcns-vim-3-mannion-2015-01.md
docs/pilot-notes/crcns-ssc-8-goncalves-2013-01.md
docs/pilot-notes/crcns-hc-14-girardeau-2017-01.md
claims/crcns-ssc-10/:
10.7554-elife.46321.yaml

transcripts/crcns-ssc-10/:
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
author-revise-1.md
[... 64 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/crcns-ssc-10-lemessurier-2019-01.yaml; for f in crcns-hc-28-jadhav-2016-01 crcns-hc-13-yu-2017-01 crcns-vim-3-mannion-2015-01 crcns-ssc-8-goncalves-2013-01 crcns-hc-14-girardeau-2017-01; do echo "=== $f"; cat docs/pilot-notes/$f.md; done; head -20 docs/pilot-notes/001754-knierim-2000-02.md
```

```
<persisted-output>
Output too large (115.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/f57ad030-7ac5-43d6-8084-19edbddf1437/tool-results/brqs4h1de.txt

Preview (first 2KB):
schema_version: 2
id: crcns-ssc-10-lemessurier-2019-01
dataset:
  archive: crcns
  id: ssc-10
  version: unversioned
  doi: 10.6080/K0DB801M
paper: doi:10.7554/elife.46321
date: '2026-11-08'
entry: crcns-ssc-10-lemessurier-2019
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
[... 49 more lines not kept]
```

**Agent**

The files are large; let me read them via Read.

**Agent calls Read**

```json
{
 "file_path": "attempts/crcns-ssc-10-lemessurier-2019-01.yaml"
}
```

```
1	schema_version: 2
2	id: crcns-ssc-10-lemessurier-2019-01
3	dataset:
4	  archive: crcns
5	  id: ssc-10
6	  version: unversioned
7	  doi: 10.6080/K0DB801M
8	paper: doi:10.7554/elife.46321
9	date: '2026-11-08'
10	entry: crcns-ssc-10-lemessurier-2019
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
[... 755 more lines not kept]
```

**Agent calls Bash**

```bash
cd docs/pilot-notes; wc -w crcns-hc-28-jadhav-2016-01.md crcns-hc-13-yu-2017-01.md crcns-vim-3-mannion-2015-01.md crcns-ssc-8-goncalves-2013-01.md crcns-hc-14-girardeau-2017-01.md; cat crcns-ssc-8-goncalves-2013-01.md crcns-hc-14-girardeau-2017-01.md crcns-vim-3-mannion-2015-01.md; head -5 001754-knierim-2000-02.md
```

```
1423 crcns-hc-28-jadhav-2016-01.md
 1333 crcns-hc-13-yu-2017-01.md
 1201 crcns-vim-3-mannion-2015-01.md
 1394 crcns-ssc-8-goncalves-2013-01.md
 1320 crcns-hc-14-girardeau-2017-01.md
 6671 total
# crcns-ssc-8, Goncalves et al. 2013

Five claims reproduced, three partially (all three on an assumption), three not
reproduced (one on an assumption) and 17 blocked, 16 for missing data and one
for insufficient metadata. The first verification round agreed with all 28
outcomes and the second with all 28; nothing was proposed after the second, so
there was no third round. CRCNS does not version data sets, so the version is
recorded as unversioned with the data set's DOI (10.6080/K0X63K3X). The paper,
Goncalves, Anstey, Golshani and Portera-Cailliau in Nature Neuroscience
(16:903-909), images layer 2/3 barrel cortex of unanesthetized wild-type (WT)
and Fmr1 -/- (KO) mice at P9-11, P14-16 and P30-40 with two-photon calcium
imaging at 3.9 Hz, and reports that pairwise correlation falls with age and
with distance, that it is higher in KO mice pooled over ages and most of all at
P14-16, that more KO neurons take part in peaks of synchrony, that firing rates
[... 309 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/crcns-ssc-10-lemessurier-2019-01.yaml",
 "offset": 776,
 "limit": 410
}
```

```
776	  - claim: figs3-1-l4-nh-tuning
777	    agrees: false
778	    outcome: partially_reproduced
779	    reason: 'Cell 47 (Methods, C1-C3, E1): L4 63.2% and 73.7% are within tolerance, the BW test is not significant (p
780	      0.43), and eBW is lower in all three 150–375 µm bins. But the eBW test at 0-75 µm is significant (p = 0.022), because
781	      L2/3 eBW is inflated to 91.7%.'
782	    response: 'Changed from not_reproduced to partially_reproduced, as the verifier gives: every part of the claim holds
783	      except the eBW absence test, which fails through the L2/3 eBW fraction, so the claim holds in part, though the
784	      criterion''s own partial clause is not met.'
785	  - claim: fig3a-l23-enrichment-more-cw-tuned
786	    agrees: true
787	    outcome: not_reproduced
788	    reason: 'Cell 49: NH 0-75 µm is 91.7% (paper 67 ± 6.7) and EN is not higher (p 0.03–0.80, and in the wrong direction).
789	      Within columns EN and NH are equal (84.7 and 84.8%, p = 1).'
790	    response: No change. Under the exploratory responsive-whisker eBW reading EN is still not higher (77.4% against 75.0%,
791	      p = 0.84), so the eBW definition does not account for the failure.
792	  - claim: fig3c-l4-enrichment-more-cw-tuned
793	    agrees: true
794	    outcome: reproduced
795	    reason: 'Cell 51 (Methods, C1-C3, E1): 97.0/73.7% at 0-75 µm and 93.2/76.8% within columns, all within tolerance,
[... 386 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "assum" attempts/crcns-ssc-10-lemessurier-2019-01.yaml | head; python -c "
import json;d=json.load(open('targets/dandisets.json'));
items=d if isinstance(d,list) else d.get('targets',d)
import sys
for x in (items if isinstance(items,list) else items.values()):
  if 'ssc-10' in json.dumps(x): print(json.dumps(x,indent=1))
"; head -60 claims/crcns-ssc-10/10.7554-elife.46321.yaml; wc -w transcripts/crcns-ssc-10/*-report.md
```

```
# Claims for LeMessurier, Laboy-Juarez, McLain, Chen, Nguyen & Feldman (2019), eLife 8:e46321,
# "Enrichment drives emergence of functional columns and improves sensory coding in the whisker
# map in L2/3 of mouse S1", on CRCNS data set ssc-10 (doi:10.6080/K0DB801M).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-08,
# protocol as stated in docs/protocol.md (Reader), version pilot-13.
#
# Text read: the version of record, PMC6697414 (Europe PMC JATS XML, flattened), as supplied
# under paper/: Results, Discussion, Materials and methods, Table 1, and the legends of Figures 1
# to 7 and their figure supplements (Figure 1 S1, Figure 2 S1 and S2, Figure 3 S1, Figure 4 S1
# and S2, Figure 5 S1 and S2). The paper has no other supplementary text. Table 1 is flattened
# to one cell per line and was read in that form. No PDF of the paper was supplied; no figure
# was read.
#
# Code read: github.com/alemessurier/imaging_analysis_pipeline, commit 5a21c9fef839fbc8eb79fa24f16662426e36904f
# (2019-07-10), the repository the paper links. rawDataPipeline/ holds the reduction from movies
# to ROI time series, dF/F, trial-aligned traces (traceByStim, sponTrace) and the responsiveness
# test (permuteTest_whisk_2016.m). plotting_2017/ holds the figure scripts. Many functions those
# scripts call are not in the repository, among them find_sigROIs, the computation of whiskPref
# (the equivalent best whiskers), find_CWtuned_byRad, find_rankedRFs, find_corr_simple,
# find_corrInBarrelvsAcross, decoder_PandPos and permutationTest_mean. What the code fixes:
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -B3 -A12 '"ssc-10"\|ssc-10' targets/dandisets.json | head -40; cd transcripts/crcns-ssc-10; ls -tr --full-time *-report.md; cat author-report.md answer-report.md author-answers-report.md
```

```
-rw-r--r-- 1 runner runner  1150 2026-11-08 20:41:20.776521114 +0000 answer-report.md
-rw-r--r-- 1 runner runner  3751 2026-11-08 20:41:20.777253975 +0000 author-revise-1-report.md
-rw-r--r-- 1 runner runner  7693 2026-11-08 20:41:20.777253975 +0000 author-report.md
-rw-r--r-- 1 runner runner  1867 2026-11-08 20:41:20.777253975 +0000 author-answers-report.md
-rw-r--r-- 1 runner runner  2092 2026-11-08 20:41:20.777521133 +0000 author-revise-3-report.md
-rw-r--r-- 1 runner runner  3109 2026-11-08 20:41:20.777521133 +0000 author-revise-2-report.md
-rw-r--r-- 1 runner runner  3575 2026-11-08 20:41:20.778521153 +0000 claims-report.md
-rw-r--r-- 1 runner runner  3636 2026-11-08 20:41:20.778521153 +0000 claims-check-report.md
-rw-r--r-- 1 runner runner  6989 2026-11-08 20:41:20.779521172 +0000 verifier-2-report.md
-rw-r--r-- 1 runner runner 13391 2026-11-08 20:41:20.779521172 +0000 verifier-1-report.md
-rw-r--r-- 1 runner runner  3386 2026-11-08 20:41:20.780521192 +0000 verifier-3-report.md
I finished steps 1 to 5 and ran the handover (step 6), all well before the 16:10 cutoff. All 34 claims have an outcome: 33 were tested and 1 is blocked. The entry passes `tools/entry.py check` with 0 errors, and `all` ran the notebook from a clean environment without failures. I did not commit or verify.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| table1-mice-and-fields | reproduced |
| l23-cell-counts | reproduced |
| l4-cell-counts | not reproduced |
[... 110 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i "ssc" targets/dandisets.json | head; grep -n -A15 'ssc-8\|"ssc' targets/dandisets.json | head -40
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  ls targets; grep -rln "ssc-10" targets; head -c 600 targets/dandisets.json; grep -c catalystneuro targets/dandisets.json
```

```
crcns.json
dandisets.json
description_papers.yaml
dryad.json
ebrains.json
figshare.json
openneuro.json
pilot.yaml
targets/crcns.json
{
 "schema_version": 1,
 "generated": "2026-11-05T14:39:45+00:00",
 "source": "https://api.dandiarchive.org/api",
 "counts": {
  "public_dandisets": 672,
  "with_a_paper": 295,
  "with_a_published_version": 254,
  "papers": 312,
  "converted_by_catalystneuro": 51
 },
[... 12 more lines not kept]
```

**Agent**

The dataset is not in `targets/dandisets.json`; it is listed in `targets/crcns.json`, so I check its `catalystneuro` field there.

**Agent calls Bash**

```bash
cd  python -c "
import json;d=json.load(open('targets/crcns.json'))
for x in d['targets']:
  if 'ssc-10' in json.dumps(x): print(json.dumps(x,indent=1))
"; cd transcripts/crcns-ssc-10; cat verifier-1-report.md author-revise-1-report.md
```

```
{
 "id": "ssc-10",
 "name": "2-photon calcium imaging in S1 of enriched and normally housed mice during individual deflection of 9 whiskers",
 "url": "http://crcns.org/data-sets/ssc/ssc-10",
 "doi": "10.6080/K0DB801M",
 "published_version": null,
 "asset_count": 4,
 "size_gb": 4.75,
 "data_standards": [
  "compressed archives"
 ],
 "species": [
  "House mouse"
 ],
 "approaches": [
  "microscopy approach"
 ],
 "papers": [
  {
   "doi": "10.7554/elife.46321",
[... 114 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/crcns-ssc-10; cat verifier-2-report.md author-revise-2-report.md verifier-3-report.md author-revise-3-report.md
```

```
**Round 2 verification: LeMessurier et al. 2019 (eLife 46321) on CRCNS ssc-10**

**1. Outcomes and assumptions**

The claims file has 34 claims and the attempt record has 34 outcomes: 13 reproduced, 13 partially reproduced, 7 not reproduced and 1 blocked. No outcome in the record carries `assumed: true`, so there are no assumptions to judge.

I agree with 32 outcomes. I disagree with two:

- **figs3-1-l4-nh-tuning (record says partially reproduced; I now say not reproduced).** The criterion's own partial clause needs both 0-75 µm values within tolerance and both absence tests non-significant.
  - Under E1 and E2 the eBW test is significant (p = 0.036 and 0.0051; cell 61).
  - Under E3 the test is not significant, but the L4 value is 82.1% against 73 ± 7.3.
  - So no reading meets the partial clause. figs2-1 and fig4ae fail their partial clauses in the same way and are scored not reproduced.
  - I retract my round-1 recommendation of partial for this claim. The author adopted it, so the change is my error, not theirs.
- **fig5eh-l23-correlation-gradient-at-edge (record says partially reproduced; by the criterion it is reproduced).** After the re-run every condition of the criterion holds in both responsiveness readings (cell 110):
  - EN is lower outside the column for signal and noise (p ≤ 0.0016).
  - Signal inside is not lower (p = 0.39 and 0.19).
  - The EN − NH difference is more negative outside, for noise −0.0454 against −0.0450 and −0.0430 against −0.0409.
  - My round-1 reason was that the Methods reading failed by 0.0002, which is no longer true.
  - The author's added permutation test (p = 0.96 and 0.81) is a fair caveat for the notes. But it is not in the criterion, and the claims file decides the outcome. The criterion's weakness, comparing two differences without a test, should be reported against the claims file.

[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 60,90p claims/crcns-ssc-10/10.7554-elife.46321.yaml; grep -n -i "check\|corrected" claims/crcns-ssc-10/10.7554-elife.46321.yaml | head; grep -c "^- id:\|^  - id:" claims/crcns-ssc-10/10.7554-elife.46321.yaml; grep -n "^- id\|^  - id\|^- claim\|^  id:" claims/crcns-ssc-10/10.7554-elife.46321.yaml | head -3
```

```
# or the barrel radii, is the author's to find.
#
# Methods common to the criteria below, from the Methods unless said otherwise:
#   - Evoked response of a trial: mean dF/F in the 1 s after train onset minus mean dF/F in the
#     0.5 s before (Methods, Quantification of whisker responses).
#   - Responsive ROI: for some whisker, the per-trial evoked responses exceed those of blank
#     trials by a permutation test of the difference in means (10,000 shuffles, one-sided at the
#     95th percentile), p-values Benjamini-Hochberg corrected over the nine whiskers at 0.05.
#     Variant: the p-values stored per ROI by the pipeline (two-sided, mean or median per the
#     field's permTestType), BH corrected. ROIs with nuclear GCaMP were excluded by the authors.
#   - Which responsive ROIs enter. Methods: for L2/3 "all whisker-responsive ROIs located within
#     any of the nine columns"; for L4 only responsive ROIs in columns C1, C2 and C3. Open for
#     L2/3: whether ROIs over septa enter the point representation and tuning-by-distance
#     analyses. Readings (A) all responsive ROIs of the field; (B) only ROIs over one of the nine
#     barrels. The counts favour (A) for Figures 2 and 3 (475 NH responsive cells, of which 344 lie
#     within a column). Correlations use only ROIs over (L2/3) or in (L4) a barrel (Methods).
#   - Receptive field: the median evoked response to each whisker over its trials (Methods).
#     Response normalised to spontaneous activity: that median z-scored to the distribution of
#     evoked-window responses on blank trials, read as (median - mean of blank) / SD of blank,
#     the standard z-score; centring on the blank median is a variant (Methods, Quantification).
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1130,1160p claims/crcns-ssc-10/10.7554-elife.46321.yaml; sed -n 95,110p claims/crcns-ssc-10/10.7554-elife.46321.yaml
```

```
not given; readings (a) enrichment and ensemble size within each distance bin, (b) enrichment
    and distance bin with per-bin comparisons. Reproduced when, under one reading, performance
    is highest in the 0-77 um bin, EN exceeds NH with p < 0.05 in the 0-77 and 77-154 um bins, and
    NH exceeds EN with p < 0.05 in the 308-385 um bin; partially reproduced when the near bins hold
    but not the reversal.
checks:
- date: 2026-11-08
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig4c-spontaneous-activity, fig4d-l23-cw-stronger, fig4d-l23-across-row-sharpening, fig4d-l23-within-row-broadening, fig4ae-l4-weaker-responses, source paragraph numbers corrected (the section has three Results paragraphs; Figure 4D is paragraph 2 and L4 is paragraph 3).
  - figs2-1-column-frame, statement and quote now include the reduced bias toward higher-arc columns, which the same sentence reports; the criterion names a reading for it and says the paper reports no test for this figure, so the home-column test is borrowed from Figure 2A.
  - figs3-1-l23-salt-and-pepper, the 1% value had tolerance 0.1 while the criterion accepted 2 to 10 cells; tolerance set to one percentage point and the criterion made to match.
  - figs3-1-l4-nh-tuning, the paper says the L4 against L2/3 difference was significant at the bins from 150 to 375 um, so full reproduction now needs all three bins, not two of three.
  - fig3a-l23-enrichment-more-cw-tuned, the statistics entry for p = 0.00008 now says the test is not named for that value and is read as Fisher's exact test.
  - fig5a-l23-signal-correlation-boundary, fig6-l4-within-column-correlations, removed the rule that let some values fall outside tolerance and still count as reproduced (six of eight, three of four), which has no basis in the paper; those cases are now partial, as in the other claims.
  - fig5b-l23-noise-correlation-boundary, same tolerance change; the criterion now tests the statement's "pairs 100 um apart" with a 
[... 25 more lines not kept]
```

**Agent**

Now I have every source. Writing the notes.

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/crcns-ssc-10-lemessurier-2019-01.md",
 "content": "# crcns-ssc-10, LeMessurier et al. 2019\n\nFourteen claims reproduced, eleven partially, eight not reproduced and one\nblocked, for missing data; no outcome rests on an assumption. The first\nverification round agreed with 31 of the 34 outcomes as they stood and the\nsecond with 32; the second proposed two changes, so a third round reviewed\nthose two and agreed with both. CRCNS does not version data sets, so the\nversion is recorded as unversioned with the data set's DOI (10.6080/K0DB801M).\nThe paper, LeMessurier, Laboy-Juarez, McLain, Chen, Nguyen and Feldman in eLife\n(8:e46321), images GCaMP6s in L2/3 (Drd3-Cre) and L4 (Scnn1a-Cre) excitatory\ncells of mouse S1 under anaesthesia while nine whiskers are deflected one at a\ntime, in mice raised from weaning either enriched (EN) or normally housed (NH),\nand reports that enrichment strengthens the response to a column's own whisker\nin L2/3 and suppresses it in neighbouring columns, makes more L2/3 cells tuned\nto the column whisker, sharpens ranked receptive fields, sharpens the drop in\nsignal and noise correlation at column boundaries and improves the decoding of\nwhisker identity, while in L4 it weakens responses; the data set holds the\npopulation imaging of all four groups as one 4.7 GB tar.gz, with raw and\nneuropil traces, dF/F, stimuli, trial-aligned traces, stored responsiveness\np-values and ROI positions relative to each barrel. The claims were written\nfrom the version of record (PMC6697414) as text flattened from the Europe PMC\nXML, with the figure legends and figure supplements but without a PDF or any\nfigure, and from the paper's pipeline code at commit 5a21c9f, from which many\nfunctions the figure scripts call are missing, among them the computation of\nthe equivalent best whiskers (eBWs); the claims check made eleven changes,\namong them rewriting the criterion of `fig5eh-l23-correlation-gradient-at-edge`\nand removing a rule that let some values fall outside tolerance in\n`fig5a-l23-signal-correlation-boundary` and `fig6-l4-within-column-correlations`,\nfor 34 claims. All but `fig1f-gcamp-matches-spikes` could be tested, as the\ncell-attached recordings with simultaneous imaging are not in the data set.\nReproduced are, among others, `table1-mice-and-fields` (the mouse and field\ncounts of Table 1, exact), `l23-cell-counts` (998 NH and 1147 EN ROIs against\nthe paper's 998 and 1257), `fig2b-2d-point-representation`,\n`fig3c-l4-enrichment-more-cw-tuned` (EN 97.1% against NH 75.0% at 0-75 um, p =\n0.0003), `fig4a-l23-ranked-rf-sharper`, `fig7c-population-decoder` and\n`fig7d-clustered-ensemble-topography`. Several outcomes rest on one reading:\n`fig2a-l23-point-representation-stronger`, `fig4b-l23-cw-and-best-sw-stronger`\nand `fig4d-l23-cw-stronger` hold only with the stored responsiveness p-values,\n`fig4c-spontaneous-activity` only under the claims file's variant without\nbaseline subtraction (under the main reading the L2/3 effect is reversed), and\n`fig7c-population-decoder` only with ensembles pooled as units (per-field means\ngive p = 0.024 to 0.42), while the fig7d ANOVA treats overlapping ensembles as\nindependent. Partial are, among others, `fig2a-l23-flanks-suppressed` (three of\nfive bins significant), the correlation claims of Figures 5 and 6, where every\ntest holds and the values fall below the paper's (0.035 to 0.078 with the\nMethods' test in fig5a), and `fig7b-single-roi-decoder` (NH 0.615, EN 0.634, p =\n0.0009, outside the tolerances). Not reproduced are `l4-cell-counts` (NH 362\nagainst 322), `fig2c-l4-point-representation-weaker` (NH 0.991 and EN 0.886 at\n0-75 um, p = 0.39), `figs2-1-column-frame`, `figs3-1-l4-nh-tuning`,\n`fig3a-l23-enrichment-more-cw-tuned` (EN lower than NH at 0-75 um, 82.7% of 133\nagainst 91.7% of 48, with the NH values far above the paper's 67),\n`figs4-1-absolute-dff` (the EN slope higher, not lower, interaction p < 1e-15),\n`fig4ae-l4-weaker-responses` (CW test p = 0.35) and\n`figs5-2-neuropil-robustness`. The author's first run had 15 reproduced, 10\npartially, 8 not reproduced and 1 blocked. The author asked no questions of a\nreader, so the answer and author-answers runs changed nothing. Round 1 agreed\nwith every outcome but three and raised the eBW gap, the L4 neuropil rebuild,\nthe reading of Figure 4C, the outcomes resting on the stored p-values, the\npooled decoder units, the untested comparison in fig5eh and the barrel-radius\nproxy; in reply `figs3-1-l4-nh-tuning` and `figs5-1-row-and-arc-boundaries`\nmoved to partial and fig5eh from reproduced to partial, the L4 rebuild was\nredone in the descriptor's order (within 0.012 of the stored dF/F), which\nuncovered three L4 fields with shifted blank traces, a counting bug was fixed,\nand an exploratory eBW reading was added. Round 2 retracted its own round-1\nrecommendation for `figs3-1-l4-nh-tuning`, as no reading meets the criterion's\npartial clause, held that fig5eh now meets every condition of its criterion,\nand found sentences the outputs did not support, among them the run time, the\nfig5a gaps and an unstated drop to 815 and 460 responsive L2/3 ROIs in the\nneuropil rebuild; the two changes went to a third round, which agreed with\nboth, noting that the noise half of fig5eh rests on differences of 0.0004 to\n0.002 that cannot be told from zero and failed by 0.0002 in round 1. The fix of\nthe shifted blank traces changed the random stream, so every p-value of the\nMethods' test moved slightly after round 1, and fig4b came to rest on the\nstored p-values alone (CW p = 0.056). The author's run took about 2 h 20 min\n(11:55 to about 14:15 UTC); the notebook ran in about 24 min at first, 9.7 of\nthem streaming, 831 s after the author-answers run, 23 min after round 1, and\nabout 19 min after round 3. During development the first full streams crashed\non inconsistent movie names and on the missing E-row whiskers in DNH13b, and\nthe reader was fixed to handle both.\n\nThe paper's test of equivalent best whiskers is in neither the Methods nor the\nlinked code, and every reading the claims file names puts 89.6-96.5% of NH L2/3\ncells near a column centre among those tuned to the column whisker, against\nthe paper's 67%, while the NH L4 value matches (75.0%, paper 73%); this gap\ndecides the eBW parts of five claims, though an exploratory reading that also\nrequires each eBW to be a responsive whisker gives 72.9-75.0% and still no\nhigher tuning in EN L2/3 (77.4% against 75.0%, p = 0.84). The stored\npermTestResults come from a two-sided permutation test on medians, not the\nMethods' one-sided test on means; the two give the same call for 86% of ROIs,\nand the L2/3 point representation, the CW and surround responses and the CW\nresponse of Figure 4D are significant only with the stored p-values. The\ncell-attached recordings of Figure 1F (10 L2/3 cells in 5 C57BL/6 mice) are not\ndeposited. processed_data.mat holds more ROIs than reduced_data.mat in 21 of 36\nfields (1044 against 998 NH L2/3, 1276 against 1147 EN L2/3, 464 against 362 NH\nL4, 782 against 615 EN L4) with no list of the excluded ROIs or the reason, and\nthe paper's 1257, 322 and 586 match neither count. No barrel areas or radii are\nstored, and ROI_pos_barrel_norm divides each position by a radius along the\nROI's direction that varies by a median 37% within a barrel, so the barrel-size\nclaim rests on a proxy. The stored dF/F is reproduced by a 5-frame moving\nmedian and F0 at the 5th percentile, as the pipeline code does, not by the\nMethods' 4 frames and 20th percentile, and the stored L4 dF/F only by filtering\nbefore subtracting 0.3 of the neuropil, as the descriptor says and the Methods\ndo not. In three L4 fields (ScENR10c/20180104/f1, ScENR10c/20180110,\nScENR10b/20180105/f2) sponTrace holds 76-frame segments starting 0.5 s after\neach blank onset, where every other field holds 106 frames starting 0.5 s\nbefore, and sponTrace keeps fewer blank trials than Stimuli marks blank (51 of\n61 in DNH15b/20170502/f1) with no stated rule. The code of Stimuli.Label is not\ndescribed (label k is whisk{k+1} for k = 0 to 8 and 9 a blank trial). Field\nDNH13b/20161208/f2 has no trials for whiskers E1, E2 and E3 and lacks positions\nfor three barrels, which the descriptor does not mention. Movie names carry a\nleading m in Stimuli and not in deltaF in some fields and the other way in\nothers, and three fields have one dF/F movie with no Stimuli entry. The\nstreamed tar.gz matches its MD5 in checksums.md5, and a clock check with\nshifted onsets supports a shared clock in 30 of 36 fields and does not\nestablish it in the other six. Questions are put to the paper's authors: how\nthe equivalent best whiskers were tested, which responsiveness test gave the\ncells analysed, and whether the spontaneous activity of Figure 4C is the\nmedian dF/F on blank trials with or without the baseline subtracted; two\nquestions on the claims file, on the reading of Figure 4C and on the sign\ncomparison in fig5eh, are in `questions/crcns-ssc-10.yaml`.\n\nThe author's points on the protocol: `docs/archives.md` describes zip files\nread by range requests, while this data set is one 4.7 GB tar.gz that every\nrun streams in full; a single tar.gz offers no cheap subset for development,\nso reduced arrays were cached in `$TMPDIR`; the ten-minute target cannot be met\nwhen streaming alone takes ten; the protocol does not say whether a variant\nnamed in the claims file counts as a reading for \"reproduced under any\nreading\", and the author counted it as one; it does not say what to do when a\ncriterion has no partial clause or the result misses its own partial clause;\nit does not place the data set's own sample code in the order of sources; the\nclock check by decoding shifted labels does not fit trial-aligned imaging, so a\nwhisker-minus-blank contrast with shifted onsets was used; it does not say what\nto record as `measured` when no reading matches; and for unversioned data the\ndata set was pinned by its MD5.\n"
}
```

```
File created successfully at: docs/pilot-notes/crcns-ssc-10-lemessurier-2019-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/crcns-ssc-10-lemessurier-2019-01.md",
 "old_string": "the paper's 67%, while the NH L4 value matches (75.0%, paper 73%); this gap\ndecides the eBW parts of five claims, though an exploratory reading that also\nrequires each eBW to be a responsive whisker gives 72.9-75.0% and still no\nhigher tuning in EN L2/3 (77.4% against 75.0%, p = 0.84).",
 "new_string": "the paper's 67%, while the NH L4 value matches (75.0%, paper 73%); this gap\nbears on five claims, though an exploratory reading that also requires each\neBW to be a responsive whisker gives 72.9-75.0% and still no higher tuning in\nEN L2/3 (77.4% against 75.0%, p = 0.84), so fig3a does not hinge on it."
}
```

```
The file docs/pilot-notes/crcns-ssc-10-lemessurier-2019-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  wc -w docs/pilot-notes/crcns-ssc-10-lemessurier-2019-01.md; grep -n "—\|rather" docs/pilot-notes/crcns-ssc-10-lemessurier-2019-01.md
```

```
1574 docs/pilot-notes/crcns-ssc-10-lemessurier-2019-01.md
```

**Agent**

Slightly longer than the recent notes (1200 to 1420 words); trimming.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/crcns-ssc-10-lemessurier-2019-01.md",
 "old_string": "the paper's 998 and 1257), `fig2b-2d-point-representation`,\n`fig3c-l4-enrichment-more-cw-tuned` (EN 97.1% against NH 75.0% at 0-75 um, p =\n0.0003), `fig4a-l23-ranked-rf-sharper`, `fig7c-population-decoder` and\n`fig7d-clustered-ensemble-topography`. Several outcomes rest on one reading:",
 "new_string": "the paper's 998 and 1257), `fig3c-l4-enrichment-more-cw-tuned` (EN 97.1%\nagainst NH 75.0% at 0-75 um, p = 0.0003) and `fig4a-l23-ranked-rf-sharper`.\nSeveral outcomes rest on one reading:"
}
```

```
The file docs/pilot-notes/crcns-ssc-10-lemessurier-2019-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/crcns-ssc-10-lemessurier-2019-01.md",
 "old_string": "partial clause, held that fig5eh now meets every condition of its criterion,\nand found sentences the outputs did not support, among them the run time, the\nfig5a gaps and an unstated drop to 815 and 460 responsive L2/3 ROIs in the\nneuropil rebuild; the two",
 "new_string": "partial clause, held that fig5eh now meets every condition of its criterion,\nand found sentences the outputs did not support, among them the run time and\nthe fig5a gaps; the two"
}
```

```
The file docs/pilot-notes/crcns-ssc-10-lemessurier-2019-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/crcns-ssc-10-lemessurier-2019-01.md",
 "old_string": "others, and three fields have one dF/F movie with no Stimuli entry. The\nstreamed tar.gz matches its MD5 in checksums.md5, and a clock check with\nshifted onsets supports a shared clock in 30 of 36 fields and does not\nestablish it in the other six. Questions",
 "new_string": "others, and three fields have one dF/F movie with no Stimuli entry. A clock\ncheck with shifted onsets supports a shared clock in 30 of 36 fields and does\nnot establish it in the other six. Questions"
}
```

```
The file docs/pilot-notes/crcns-ssc-10-lemessurier-2019-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/crcns-ssc-10-lemessurier-2019-01.md",
 "old_string": "`fig3a-l23-enrichment-more-cw-tuned` (EN lower than NH at 0-75 um, 82.7% of 133\nagainst 91.7% of 48, with the NH values far above the paper's 67),\n`figs4-1-absolute-dff` (the EN slope higher, not lower, interaction p < 1e-15),",
 "new_string": "`fig3a-l23-enrichment-more-cw-tuned` (EN lower than NH at 0-75 um, 82.7% of 133\nagainst 91.7% of 48, with the NH values far above the paper's 67),\n`figs4-1-absolute-dff` (the EN slope higher, not lower),"
}
```

```
The file docs/pilot-notes/crcns-ssc-10-lemessurier-2019-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/crcns-ssc-10-lemessurier-2019-01.md",
 "old_string": "the eBW gap, the L4 neuropil rebuild,\nthe reading of Figure 4C, the outcomes resting on the stored p-values, the\npooled decoder units, the untested comparison in fig5eh and the barrel-radius\nproxy; in reply",
 "new_string": "the eBW gap, the L4 neuropil rebuild,\nthe reading of Figure 4C, the outcomes resting on the stored p-values and the\nuntested comparison in fig5eh; in reply"
}
```

```
The file docs/pilot-notes/crcns-ssc-10-lemessurier-2019-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  wc -w docs/pilot-notes/crcns-ssc-10-lemessurier-2019-01.md
```

```
1537 docs/pilot-notes/crcns-ssc-10-lemessurier-2019-01.md
```

**Agent**

Now the summary.

**Agent calls Write**

```json
{
 "file_path": "summaries/crcns-ssc-10-lemessurier-2019-01.md",
 "content": "The paper's findings that enrichment sharpens L2/3 receptive fields, steepens the drop in correlations at column boundaries and improves decoding of whisker identity held up in this data, though some correlation and decoder values fall below the paper's. The stronger L2/3 response to a column's own whisker held only with the responsiveness p-values stored in the data set, which come from a different test than the Methods describe. The rise in L2/3 cells tuned to the column whisker did not reproduce: the paper does not describe its test of equivalent best whiskers, and the main reading puts 91.7% of normally housed cells near the column centre in that group, against the paper's 67%. In L4, weaker surround responses held, but a weaker response to the column whisker did not.\n"
}
```

```
File created successfully at: summaries/crcns-ssc-10-lemessurier-2019-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  wc -w summaries/crcns-ssc-10-lemessurier-2019-01.md; ls summaries | head -3; git status --short
```

```
129 summaries/crcns-ssc-10-lemessurier-2019-01.md
000003-senzai-2017-01.md
000004-chandravadia-2020-01.md
000005-yu-2016-01.md
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
?? docs/pilot-notes/crcns-ssc-10-lemessurier-2019-01.md
?? scripts
?? summaries/crcns-ssc-10-lemessurier-2019-01.md
```

**Agent calls Write**

```json
{
 "file_path": "summaries/crcns-ssc-10-lemessurier-2019-01.md",
 "content": "The findings that enrichment sharpens L2/3 receptive fields, steepens the drop in correlations at column boundaries and improves decoding of whisker identity held up in this data, though some correlation and decoder values fall below the paper's. The stronger L2/3 response to a column's own whisker held only with the data set's stored responsiveness p-values, which come from a test other than the Methods describe. The rise in L2/3 cells tuned to the column whisker did not reproduce: the paper does not describe its test of equivalent best whiskers, and the main reading puts 91.7% of normally housed cells near the column centre in that group, against 67%. In L4, weaker surround responses held, but a weaker column-whisker response did not.\n"
}
```

```
The file summaries/crcns-ssc-10-lemessurier-2019-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  wc -w summaries/crcns-ssc-10-lemessurier-2019-01.md
```

```
121 summaries/crcns-ssc-10-lemessurier-2019-01.md
```

**Agent calls Write**

```json
{
 "file_path": "summaries/crcns-ssc-10-lemessurier-2019-01.md",
 "content": "The findings that enrichment sharpens L2/3 receptive fields, steepens the drop in correlations at column boundaries and improves decoding of whisker identity held up in this data, though some correlation and decoder values fall below the paper's. The stronger L2/3 response to a column's own whisker held only with the data set's stored responsiveness p-values, which come from a test other than the Methods describe. The rise in L2/3 cells tuned to the column whisker did not reproduce: the paper does not describe its test of equivalent best whiskers, and the main reading puts 91.7% of normally housed cells near the column centre in that group, against 67%. In L4, weaker surround responses held; a weaker column-whisker response did not.\n"
}
```

```
The file summaries/crcns-ssc-10-lemessurier-2019-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  wc -w summaries/crcns-ssc-10-lemessurier-2019-01.md; cat docs/pilot-notes/crcns-ssc-10-lemessurier-2019-01.md
```

```
120 summaries/crcns-ssc-10-lemessurier-2019-01.md
# crcns-ssc-10, LeMessurier et al. 2019

Fourteen claims reproduced, eleven partially, eight not reproduced and one
blocked, for missing data; no outcome rests on an assumption. The first
verification round agreed with 31 of the 34 outcomes as they stood and the
second with 32; the second proposed two changes, so a third round reviewed
those two and agreed with both. CRCNS does not version data sets, so the
version is recorded as unversioned with the data set's DOI (10.6080/K0DB801M).
The paper, LeMessurier, Laboy-Juarez, McLain, Chen, Nguyen and Feldman in eLife
(8:e46321), images GCaMP6s in L2/3 (Drd3-Cre) and L4 (Scnn1a-Cre) excitatory
cells of mouse S1 under anaesthesia while nine whiskers are deflected one at a
time, in mice raised from weaning either enriched (EN) or normally housed (NH),
and reports that enrichment strengthens the response to a column's own whisker
in L2/3 and suppresses it in neighbouring columns, makes more L2/3 cells tuned
to the column whisker, sharpens ranked receptive fields, sharpens the drop in
signal and noise correlation at column boundaries and improves the decoding of
whisker identity, while in L4 it weakens responses; the data set holds the
population imaging of all four groups as one 4.7 GB tar.gz, with raw and
neuropil traces, dF/F, stimuli, trial-aligned traces, stored responsiveness
[... 111 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "summaries/crcns-ssc-10-lemessurier-2019-01.md",
 "old_string": "held up in this data, though",
 "new_string": "held up here, though"
}
```

```
The file summaries/crcns-ssc-10-lemessurier-2019-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  wc -w summaries/crcns-ssc-10-lemessurier-2019-01.md; grep -c "—\|rather" summaries/crcns-ssc-10-lemessurier-2019-01.md docs/pilot-notes/crcns-ssc-10-lemessurier-2019-01.md
```

```
118 summaries/crcns-ssc-10-lemessurier-2019-01.md
summaries/crcns-ssc-10-lemessurier-2019-01.md:0
docs/pilot-notes/crcns-ssc-10-lemessurier-2019-01.md:0
```

**Agent**

I wrote both files and committed nothing. Two things you should know:

- **Dataset entry location:** CRCNS:ssc-10 is not in `targets/dandisets.json`. I used its entry in `targets/crcns.json` instead. Its `catalystneuro` field is empty, so the notes do not open with the CatalystNeuro sentence.
- **Length:** the notes come to about 1,530 words, while the five most recent run 1,200 to 1,420. This paper has 34 claims, more than those had.

The outcome counts (14, 11, 8, 1) match what `python tools/readme_row.py crcns-ssc-10` prints.

**docs/pilot-notes/crcns-ssc-10-lemessurier-2019-01.md**

# crcns-ssc-10, LeMessurier et al. 2019

Fourteen claims reproduced, eleven partially, eight not reproduced and one blocked, for missing data; no outcome rests on an assumption. The first verification round agreed with 31 of the 34 outcomes as they stood and the second with 32; the second proposed two changes, so a third round reviewed those two and agreed with both. CRCNS does not version data sets, so the version is recorded as unversioned with the data set's DOI (10.6080/K0DB801M). The paper, LeMessurier, Laboy-Juarez, McLain, Chen, Nguyen and Feldman in eLife (8:e46321), images GCaMP6s in L2/3 (Drd3-Cre) and L4 (Scnn1a-Cre) excitatory cells of mouse S1 under anaesthesia while nine whiskers are deflected one at a time, in mice raised from weaning either enriched (EN) or normally housed (NH), and reports that enrichment strengthens the response to a column's own whisker in L2/3 and suppresses it in neighbouring columns, makes more L2/3 cells tuned to the column whisker, sharpens ranked receptive fields, sharpens the drop in signal and noise correlation at column boundaries and improves the decoding of whisker identity, while in L4 it weakens responses; the data set holds the population imaging of all four groups as one 4.7 GB tar.gz, with raw and neuropil traces, dF/F, stimuli, trial-aligned traces, stored responsiveness p-values and ROI positions relative to each barrel. The claims were written from the version of record (PMC6697414) as text flattened from the Europe PMC XML, with the figure legends and figure supplements but without a PDF or any figure, and from the paper's pipeline code at commit 5a21c9f, from which many functions the figure scripts call are missing, among them the computation of the equivalent best whiskers (eBWs); the claims check made eleven changes, among them rewriting the criterion of `fig5eh-l23-correlation-gradient-at-edge` and removing a rule that let some values fall outside tolerance in `fig5a-l23-signal-correlation-boundary` and `fig6-l4-within-column-correlations`, for 34 claims. All but `fig1f-gcamp-matches-spikes` could be tested, as the cell-attached recordings with simultaneous imaging are not in the data set. Reproduced are, among others, `table1-mice-and-fields` (the mouse and field counts of Table 1, exact), `l23-cell-counts` (998 NH and 1147 EN ROIs against the paper's 998 and 1257), `fig3c-l4-enrichment-more-cw-tuned` (EN 97.1% against NH 75.0% at 0-75 um, p = 0.0003) and `fig4a-l23-ranked-rf-sharper`. Several outcomes rest on one reading: `fig2a-l23-point-representation-stronger`, `fig4b-l23-cw-and-best-sw-stronger` and `fig4d-l23-cw-stronger` hold only with the stored responsiveness p-values, `fig4c-spontaneous-activity` only under the claims file's variant without baseline subtraction (under the main reading the L2/3 effect is reversed), and `fig7c-population-decoder` only with ensembles pooled as units (per-field means give p = 0.024 to 0.42), while the fig7d ANOVA treats overlapping ensembles as independent. Partial are, among others, `fig2a-l23-flanks-suppressed` (three of five bins significant), the correlation claims of Figures 5 and 6, where every test holds and the values fall below the paper's (0.035 to 0.078 with the Methods' test in fig5a), and `fig7b-single-roi-decoder` (NH 0.615, EN 0.634, p = 0.0009, outside the tolerances). Not reproduced are `l4-cell-counts` (NH 362 against 322), `fig2c-l4-point-representation-weaker` (NH 0.991 and EN 0.886 at 0-75 um, p = 0.39), `figs2-1-column-frame`, `figs3-1-l4-nh-tuning`, `fig3a-l23-enrichment-more-cw-tuned` (EN lower than NH at 0-75 um, 82.7% of 133 against 91.7% of 48, with the NH values far above the paper's 67), `figs4-1-absolute-dff` (the EN slope higher, not lower), `fig4ae-l4-weaker-responses` (CW test p = 0.35) and `figs5-2-neuropil-robustness`. The author's first run had 15 reproduced, 10 partially, 8 not reproduced and 1 blocked. The author asked no questions of a reader, so the answer and author-answers runs changed nothing. Round 1 agreed with every outcome but three and raised the eBW gap, the L4 neuropil rebuild, the reading of Figure 4C, the outcomes resting on the stored p-values and the untested comparison in fig5eh; in reply `figs3-1-l4-nh-tuning` and `figs5-1-row-and-arc-boundaries` moved to partial and fig5eh from reproduced to partial, the L4 rebuild was redone in the descriptor's order (within 0.012 of the stored dF/F), which uncovered three L4 fields with shifted blank traces, a counting bug was fixed, and an exploratory eBW reading was added. Round 2 retracted its own round-1 recommendation for `figs3-1-l4-nh-tuning`, as no reading meets the criterion's partial clause, held that fig5eh now meets every condition of its criterion, and found sentences the outputs did not support, among them the run time and the fig5a gaps; the two changes went to a third round, which agreed with both, noting that the noise half of fig5eh rests on differences of 0.0004 to 0.002 that cannot be told from zero and failed by 0.0002 in round 1. The fix of the shifted blank traces changed the random stream, so every p-value of the Methods' test moved slightly after round 1, and fig4b came to rest on the stored p-values alone (CW p = 0.056). The author's run took about 2 h 20 min (11:55 to about 14:15 UTC); the notebook ran in about 24 min at first, 9.7 of them streaming, 831 s after the author-answers run, 23 min after round 1, and about 19 min after round 3. During development the first full streams crashed on inconsistent movie names and on the missing E-row whiskers in DNH13b, and the reader was fixed to handle both.

The paper's test of equivalent best whiskers is in neither the Methods nor the linked code, and every reading the claims file names puts 89.6-96.5% of NH L2/3 cells near a column centre among those tuned to the column whisker, against the paper's 67%, while the NH L4 value matches (75.0%, paper 73%); this gap bears on five claims, though an exploratory reading that also requires each eBW to be a responsive whisker gives 72.9-75.0% and still no higher tuning in EN L2/3 (77.4% against 75.0%, p = 0.84), so fig3a does not hinge on it. The stored permTestResults come from a two-sided permutation test on medians, not the Methods' one-sided test on means; the two give the same call for 86% of ROIs, and the L2/3 point representation, the CW and surround responses and the CW response of Figure 4D are significant only with the stored p-values. The cell-attached recordings of Figure 1F (10 L2/3 cells in 5 C57BL/6 mice) are not deposited. processed_data.mat holds more ROIs than reduced_data.mat in 21 of 36 fields (1044 against 998 NH L2/3, 1276 against 1147 EN L2/3, 464 against 362 NH L4, 782 against 615 EN L4) with no list of the excluded ROIs or the reason, and the paper's 1257, 322 and 586 match neither count. No barrel areas or radii are stored, and ROI_pos_barrel_norm divides each position by a radius along the ROI's direction that varies by a median 37% within a barrel, so the barrel-size claim rests on a proxy. The stored dF/F is reproduced by a 5-frame moving median and F0 at the 5th percentile, as the pipeline code does, not by the Methods' 4 frames and 20th percentile, and the stored L4 dF/F only by filtering before subtracting 0.3 of the neuropil, as the descriptor says and the Methods do not. In three L4 fields (ScENR10c/20180104/f1, ScENR10c/20180110, ScENR10b/20180105/f2) sponTrace holds 76-frame segments starting 0.5 s after each blank onset, where every other field holds 106 frames starting 0.5 s before, and sponTrace keeps fewer blank trials than Stimuli marks blank (51 of 61 in DNH15b/20170502/f1) with no stated rule. The code of Stimuli.Label is not described (label k is whisk{k+1} for k = 0 to 8 and 9 a blank trial). Field DNH13b/20161208/f2 has no trials for whiskers E1, E2 and E3 and lacks positions for three barrels, which the descriptor does not mention. Movie names carry a leading m in Stimuli and not in deltaF in some fields and the other way in others, and three fields have one dF/F movie with no Stimuli entry. A clock check with shifted onsets supports a shared clock in 30 of 36 fields and does not establish it in the other six. Questions are put to the paper's authors: how the equivalent best whiskers were tested, which responsiveness test gave the cells analysed, and whether the spontaneous activity of Figure 4C is the median dF/F on blank trials with or without the baseline subtracted; two questions on the claims file, on the reading of Figure 4C and on the sign comparison in fig5eh, are in `questions/crcns-ssc-10.yaml`.

The author's points on the protocol: `docs/archives.md` describes zip files read by range requests, while this data set is one 4.7 GB tar.gz that every run streams in full; a single tar.gz offers no cheap subset for development, so reduced arrays were cached in `$TMPDIR`; the ten-minute target cannot be met when streaming alone takes ten; the protocol does not say whether a variant named in the claims file counts as a reading for "reproduced under any reading", and the author counted it as one; it does not say what to do when a criterion has no partial clause or the result misses its own partial clause; it does not place the data set's own sample code in the order of sources; the clock check by decoding shifted labels does not fit trial-aligned imaging, so a whisker-minus-blank contrast with shifted onsets was used; it does not say what to record as `measured` when no reading matches; and for unversioned data the data set was pinned by its MD5.

**summaries/crcns-ssc-10-lemessurier-2019-01.md** (118 words)

The findings that enrichment sharpens L2/3 receptive fields, steepens the drop in correlations at column boundaries and improves decoding of whisker identity held up here, though some correlation and decoder values fall below the paper's. The stronger L2/3 response to a column's own whisker held only with the data set's stored responsiveness p-values, which come from a test other than the Methods describe. The rise in L2/3 cells tuned to the column whisker did not reproduce: the paper does not describe its test of equivalent best whiskers, and the main reading puts 91.7% of normally housed cells near the column centre in that group, against 67%. In L4, weaker surround responses held; a weaker column-whisker response did not.

## End of run

31 turns, 3 minutes, $1.50 at API prices, result: success.
