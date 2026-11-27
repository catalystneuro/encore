# paula-2026 · recorder · run 46060891787

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; python tools/readme_row.py paula-2026; ls transcripts/paula-2026/; cat attempts/paula-2026-01.yaml; cat claims/paula-2026.yaml
```

```
<persisted-output>
Output too large (163.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/6c769592-e9ae-422c-9583-10010e32d36c/tool-results/bnk7gh56s.txt

Preview (first 2KB):
docs/pilot-notes/allen-2026-01.md
docs/pilot-notes/amjad-2025-01.md
docs/pilot-notes/amjad-2025-02.md
docs/pilot-notes/andreassen-2022-01.md
docs/pilot-notes/andrews-2024-01.md
| [000713](https://dandiarchive.org/dandiset/000713) | [Paula et al. 2026](https://doi.org/10.1103/wndc-k654) | 12 | 5 | 20 | 0 | [`paula-2026`](entries/paula-2026) |
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
[... 37 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/6c769592-e9ae-422c-9583-10010e32d36c/tool-results/bnk7gh56s.txt"
}
```

```
1	docs/pilot-notes/allen-2026-01.md
2	docs/pilot-notes/amjad-2025-01.md
3	docs/pilot-notes/amjad-2025-02.md
4	docs/pilot-notes/andreassen-2022-01.md
5	docs/pilot-notes/andrews-2024-01.md
6	| [000713](https://dandiarchive.org/dandiset/000713) | [Paula et al. 2026](https://doi.org/10.1103/wndc-k654) | 12 | 5 | 20 | 0 | [`paula-2026`](entries/paula-2026) |
7	author-report.md
8	author-revise-1-report.md
9	author-revise-1.md
10	author-revise-2-report.md
11	author-revise-2.md
12	author.md
13	claims-check-report.md
14	claims-check.md
15	claims-report.md
16	claims.md
17	verifier-1-report.md
18	verifier-1.md
19	verifier-2-report.md
20	verifier-2.md
[... 797 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/6c769592-e9ae-422c-9583-10010e32d36c/tool-results/bnk7gh56s.txt",
 "offset": 818,
 "limit": 400
}
```

```
818	    tutorial (snr > 1, ISI violations < 1, firing rate > 0.1 spikes/s; AllenSDK commit a56bd8ea). The paper states no unit
819	    filter. Scaled to the paper''s 102 sessions this filter gives 0.93 to 1.02 times Table I''s area neuron counts and neurons
820	    per population within 5% of Table I''s, against 1.28 to 1.43 times with all units and 0.34 to 0.55 times with ''qc'' (the
821	    claims file''s two readings), which are run as variants for every claim.'
822	  - All 153 ecephys sessions are used, against the paper's 102; the paper does not say how its sessions were chosen, every
823	    session meets both session readings of the claims file, and no grouping by genotype, image set, novelty or probe count
824	    gives 102.
825	  - The visually driven minus spontaneous difference of an area is the median C over its visually driven windows minus that
826	    over its spontaneous windows; the claims file does not fix the form.
827	  assumed: true
828	- claim: fig5-vis-complexity-cv-coupling
829	  outcome: not_reproduced
830	  notebook: reproduce_paula_2026.ipynb
831	  output: claim:fig5-vis-complexity-cv-coupling
832	  measured:
833	  - 0.329
834	  - 4.6
835	  - 0.381
836	  - 2.0
837	  - 0.391
[... 380 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/6c769592-e9ae-422c-9583-10010e32d36c/tool-results/bnk7gh56s.txt",
 "offset": 1218,
 "limit": 250
}
```

```
1218	    response: Same under 'vbn'; qc drops NOT. Outcome unchanged.
1219	  - claim: fig4e-js-complexity-natural-images
1220	    agrees: false
1221	    outcome: not_reproduced
1222	    reason: VIS-VIS, VIS-TH and VIS-MB hold. Only 20% of DG/CA3 pairs lie in 0.27 to 0.55 (median 0.16).
1223	    response: Changed to not_reproduced (no partial rule).
1224	  - claim: fig4fg-js-complexity-active-blanks
1225	    agrees: true
1226	    outcome: not_reproduced
1227	    reason: 'VIS against subcortical pairs above 0.36: 29 to 38%. HP-HP pairs in range: 27 to 33%.'
1228	    response: Same under 'vbn', with natural logs added. Outcome unchanged.
1229	  - claim: fig4h-js-complexity-spontaneous-converges
1230	    agrees: true
1231	    outcome: not_reproduced
1232	    reason: The mean of all spontaneous pairs is not the lowest (0.264 to 0.332 against 0.218 to 0.255 for blanks).
1233	    response: Same under 'vbn', with natural logs added. Outcome unchanged.
1234	  - claim: supp-robustness-parameters
1235	    agrees: true
1236	    outcome: partially_reproduced
1237	    reason: The pattern holds in 4 of 5 combinations; bin 20 ms with D 3, tau 4 fails. This is the claim's partial rule.
[... 230 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^- date\|^  reviewed\|^[a-z_]*:" attempts/paula-2026-01.yaml | head -40; wc -l attempts/paula-2026-01.yaml claims/paula-2026.yaml; grep -n -B2 -A12 '"000713"' targets/dandisets.json | head -40
```

```
1:schema_version: 3
2:id: paula-2026-01
3:datasets:
9:paper: doi:10.1103/wndc-k654
10:date: '2026-11-27'
11:entry: paula-2026
12:provenance:
23:inputs:
33:outcomes:
935:findings:
1000:verifications:
1001:- date: '2026-11-27'
1004:  reviewed: The first executed notebook with the conclusion cells and the summary removed, the helper module and the claims
1252:- date: '2026-11-27'
1255:  reviewed: 'Round 2: the full executed notebook of the first revision, with its conclusions and summary, the attempt record,
  1491 attempts/paula-2026-01.yaml
  1135 claims/paula-2026.yaml
  2626 total
```

**Agent calls Bash**

```bash
sed -n 1440,1491p attempts/paula-2026-01.yaml; grep -n -A12 '000713' targets/dandisets.json | head -30
```

```
response: The two sentences are merged into one.
  - claim: fig4e-js-complexity-natural-images
    agrees: true
    outcome: not_reproduced
    reason: Agrees with the stated outcome, which follows from the claims-file criterion applied to the printed outputs.
    response: No change.
  - claim: fig4fg-js-complexity-active-blanks
    agrees: true
    outcome: not_reproduced
    reason: Agrees with the stated outcome, which follows from the claims-file criterion applied to the printed outputs.
    response: No change.
  - claim: fig4h-js-complexity-spontaneous-converges
    agrees: true
    outcome: not_reproduced
    reason: Agrees with the stated outcome, which follows from the claims-file criterion applied to the printed outputs.
    response: No change.
  - claim: supp-robustness-parameters
    agrees: true
    outcome: partially_reproduced
    reason: Agrees with the stated outcome, which follows from the claims-file criterion applied to the printed outputs.
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;d=json.load(open('targets/dandisets.json'));print(type(d))
items=d if isinstance(d,list) else d.get('dandisets',d)
import itertools
if isinstance(items,dict):
  for k,v in items.items():
    if '713' in str(k) or (isinstance(v,dict) and '000713' in str(v.get('id',''))): print(k,v)
else:
  for v in items:
    if '000713' in json.dumps(v)[:200]: print(v)
"; head -c 600 targets/dandisets.json
```

```
<class 'dict'>
{
 "schema_version": 1,
 "generated": "2026-11-17T15:59:44+00:00",
 "source": "https://api.dandiarchive.org/api",
 "counts": {
  "public_dandisets": 678,
  "with_a_paper": 302,
  "with_a_published_version": 260,
  "papers": 317,
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
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;d=json.load(open('targets/dandisets.json'))
for v in d['targets']:
  if v['dandiset']=='000713': print(json.dumps(v,indent=1))
"
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
grep -n "713" targets/dandisets.json | head; grep -n "catalystneuro\"" targets/dandisets.json | head -3
```

```
483:   "published_version": "0.211030.0713",
856:   "size_gb": 1713.93,
4705:   "asset_count": 713,
5175:     "doi": "10.52202/085713-4642",
10:  "converted_by_catalystneuro": 51
38:   "catalystneuro": [
66:   "catalystneuro": [
```

**Agent**

Dandiset 000713 has no entry in `targets/dandisets.json`, so there is no `catalystneuro` field to report. Next, reading the five model notes and the reports.

**Agent calls Bash**

```bash
for f in allen-2026-01 amjad-2025-01 amjad-2025-02 andreassen-2022-01 andrews-2024-01; do echo "=== $f"; cat docs/pilot-notes/$f.md; done; echo ===; head -5 docs/pilot-notes/knierim-2000-02.md
```

```
<persisted-output>
Output too large (30KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/6c769592-e9ae-422c-9583-10010e32d36c/tool-results/bge40ypvy.txt

Preview (first 2KB):
=== allen-2026-01
# allen-2026, Allen et al. 2026

Fifteen claims reproduced on the dataset, one partially, one not reproduced
and four blocked, all four for missing data; the ten transcriptomic claims,
whose reads and assembly are in NCBI SRA and TSA (`data: elsewhere`), are
counted apart, with seven reproduced, two partially and one not reproduced.
One outcome, `fig4a-pca`, rests on an assumption. The first verification round
agreed with 28 of the 31 outcomes and gave `fig2g-attack-willingness` as
reproduced where the record had not reproduced, and
`sfig3-prey-velocity-unchanged` and `rnaseq-assembly` as partially reproduced
where it had reproduced; the author took all three. The second round agreed
with all 31, and nothing was proposed after it, so there was no third round. It
pins version 439366, the only public version. The paper, Allen, Yan, Kuan et
al., "Neurometabolic rewiring in squid (Sepioteuthis lessoniana) optic lobes
drives behavioral plasticity and visual integration under environmental
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/paula-2026; wc -w *-report.md; cat author-report.md
```

```
778 author-report.md
  658 author-revise-1-report.md
  610 author-revise-2-report.md
  420 claims-check-report.md
  693 claims-report.md
 2236 verifier-1-report.md
 1235 verifier-2-report.md
 6630 total
I've finished steps 1 to 5 for paula-2026 and built the handover with `tools/entry.py handover`; I did not verify the work myself. `tools/entry.py all` passes: 0 errors, and a clean-environment run takes 36.5 minutes, of which 35.7 are spent streaming the 153 sessions. Nothing is committed.

The main caveat: neither of the claims file's unit-selection readings reproduces the paper's counts. I used all 153 sessions and all units, so almost every outcome rests on that assumption.

## 1. Outcomes (38 claims, none blocked)

| Outcome | Claims |
|---|---|
| Reproduced (12) | fig2a-vis-cv-by-condition, fig2a-thalamus-cv-by-condition, fig2b-visually-driven-js-cv-low, fig3b-complexity-levels-by-region, fig3d-th-ch-plane, fig3e-hp-ch-plane, fig3f-mb-ch-plane, fig4b-thalamus-lgd-lp-modulated, fig4b-other-thalamus-not-modulated, fig4c-dg-ca3-complexity, fig4d-midbrain-complexity-invariant, complexity-separates-images-from-spontaneous |
| Partially reproduced (16) | fig1c-cv-above-surrogate, fig1e-positive-cv-modules, fig1e-dg-ca3-anticorrelation-hubs, fig1e-midbrain-weakest-cv-correlations, fig2a-hippocampus-cv-stable, fig2a-midbrain-cv-invariant, fig2b-vis-summed-js-cv, fig2b-dg-ca3-high-js-cv, fig3a-reference-systems, fig3c-vis-ch-plane, fig4a-vis-complexity-by-condition, fig4e-js-complexity-natural-images, supp-robustness-parameters, fig5-vis-complexity-cv-coupling, fig5-th-weaker-coupling, fig5-mb-flat |
| Not reproduced (10) | table1-sample, fig1c-cv-region-medians, fig1d-surrogate-abolishes-cv-correlations, fig2b-hp-mb-summed-js-cv, fig2b-legend-js-cv, fig3-complexity-range-fractions, fig4fg-js-complexity-active-blanks, fig4h-js-complexity-spontaneous-converges, fig5-hp-spontaneous-elevated, supp-fig6-mean-correlation |

[... 46 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/6c769592-e9ae-422c-9583-10010e32d36c/tool-results/bge40ypvy.txt"
}
```

```
1	=== allen-2026-01
2	# allen-2026, Allen et al. 2026
3	
4	Fifteen claims reproduced on the dataset, one partially, one not reproduced
5	and four blocked, all four for missing data; the ten transcriptomic claims,
6	whose reads and assembly are in NCBI SRA and TSA (`data: elsewhere`), are
7	counted apart, with seven reproduced, two partially and one not reproduced.
8	One outcome, `fig4a-pca`, rests on an assumption. The first verification round
9	agreed with 28 of the 31 outcomes and gave `fig2g-attack-willingness` as
10	reproduced where the record had not reproduced, and
11	`sfig3-prey-velocity-unchanged` and `rnaseq-assembly` as partially reproduced
12	where it had reproduced; the author took all three. The second round agreed
13	with all 31, and nothing was proposed after it, so there was no third round. It
14	pins version 439366, the only public version. The paper, Allen, Yan, Kuan et
15	al., "Neurometabolic rewiring in squid (Sepioteuthis lessoniana) optic lobes
16	drives behavioral plasticity and visual integration under environmental
17	acidification" (Communications Biology 9:229), rears bigfin reef squid at pH
18	8.2, with 7 days at pH 7.8 after 90 days (acute-OA) or at pH 7.8 from hatching
19	(chronic-OA), and reports a higher metabolic rate, lower ammonia excretion and
20	higher blood pH, PCO2 and [HCO3-] under chronic-OA, more time in the upper half
[... 415 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,60p claims/paula-2026.yaml; grep -n "^  - id:\|^- id:\|figure:\|location:" claims/paula-2026.yaml | head -100
```

```
# Claims for de Paula, Jungmann, Fontenele, Aguiar, Carelli, Matias, Copelli & de Vasconcelos
# (2026), "Revealing Stimulus-Dependent Dynamics Through Statistical Complexity", PRX Life 4,
# 023018, doi:10.1103/wndc-k654, tested on DANDI:000713.
#
# Provenance: written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub
# Actions"), 2026-11-27, protocol pilot-18 as stated in docs/protocol.md.
#
# Text read: the version of record (published 22 May 2026, corrected 22 July 2026, the
# correction fixing Eq. 9), from paper/10.1103-wndc-k654.txt, which holds the main text
# (Methods, Results, figure legends, Table I) and the Supplemental Material (Secs. I to III,
# supplementary Figs. 1 to 6, dated April 28, 2026). The PDF pages could not be rendered in
# this run, so no figure was read from its image; every value below is from the text and the
# legends. The paper links no analysis code: its Data Availability statement cites only the
# dataset, and the one URL of the supplement (https://bit.ly/4smMnMj) holds the figures of the
# parameter sweep. No code was read.
#
# Data the paper used (Methods II.A, Results III.A, Table I, legends of Figs. 1 to 5). The
# Allen Institute Visual Behavior Neuropixels dataset, cited as DANDI:000713 version
# 0.240702.1725 (Ref. 22). Wild-type and transgenic mice, head fixed, recorded with six
# Neuropixels 1.0 probes targeting visual cortex. 102 sessions. Measured variables used:
[... 78 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 60,84p claims/paula-2026.yaml; grep -n -i "abstract\|  source:\|  where:\|  section:" claims/paula-2026.yaml | head -60; sed -n 1099,1135p claims/paula-2026.yaml
```

```
#   sessions, 1437 populations, Table I neurons) are the check: the reading closer to them is
#   adopted, both shown.
# - Unit selection: no quality filter is stated. Readings (a) all units of the units table;
#   (b) the Allen default filters for this dataset (ISI violations < 0.5, amplitude cutoff <
#   0.1, presence ratio > 0.9). Table I neuron counts decide between them (claim
#   table1-sample); both are run.
# - Natural images and blanks: whether change flashes are included, and how the gray screens
#   around omitted flashes are treated, is not stated. Readings (a) all flashes of the image,
#   omitted flashes giving neither an image nor a blank interval; (b) as (a) but blank
#   intervals only after flashes followed by another flash. Spike times are shifted so that
#   the pieces abut. The "central 100 s" is the 100 s centred on the series midpoint.
# - Spontaneous windows: which two 100-s windows of the ~5 min gray screen is not stated.
#   Readings (a) the first two consecutive windows from its start; (b) two windows centred in
#   the interval.
# - Surrogate ISI shuffling: where the shuffled train starts is not stated; the first spike is
#   kept in place and the shuffled intervals follow it (a standard choice; it cannot change
#   the outcome). Random seed fixed, a standard choice.
# - JS divergence between two distributions of window values (Figs. 2b, 4e to 4h): the
#   histogram bins are not stated. Readings (a) 50 and (b) 100 equal bins over the range of
#   the two pooled distributions. Log base 2, so that JS lies in [0, 1], as the color scale of
[... 81 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/paula-2026; cat claims-report.md claims-check-report.md
```

```
I've written `claims/paula-2026.yaml`. The quote checker reports no problems (38 claims, 37 quotes, 7 statistical values), and the file follows the style rules. Nothing is committed.

**Text read:** the version of record (PRX Life 4, 023018; published 22 May 2026, corrected 22 July 2026, the correction being to Eq. 9). It includes the full Methods, Table I, the figure legends and the Supplemental Material (Secs. I to III, supplementary Figs. 1 to 6). The PDF pages could not be opened as images (no renderer here), so every value comes from the text and legends. The paper links no analysis code, so none was read; its only URL is a link to the parameter-sweep figures.

**Counts:**
- **Claims:** 38. All have a criterion and 22 have expected values.
- **Quotes:** 37. The one without, `table1-sample`, is a count check marked `inferred` and built from Table I and the legend numbers.
- **Statistics:** 7 claims carry them. These are the Mann-Whitney tests against surrogates (p < 0.001) for CV and for each area's complexity, plus two tests the paper does not name (Fig. 4a pairwise comparisons, Fig. 4b LGd/LP modulation).
- **Data:** one claim, `fig3a-reference-systems`, uses no recordings and is marked `data: elsewhere` (synthetic series from the supplement's definitions). Every other claim uses the dataset.

**Details the paper leaves open, with the readings named:**
- **Session selection** (102 sessions, no rule given): (a) every session with a qualifying population, or (b) only sessions that also have the spontaneous epoch. The paper's own counts (sessions, 1437 populations, Table I neurons) pick between them.
- **Unit quality filter:** (a) all units, or (b) the Allen default filters. Table I counts decide.
- **Which flashes count:** whether change and omitted flashes are included, and which gray screens count as blanks; two readings.
- **Spontaneous windows:** the first two consecutive 100-s windows, or two centred in the gray-screen interval.
- **JS divergence histograms
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/paula-2026; cat author-revise-1-report.md author-revise-2-report.md
```

```
/bin/bash: line 1: cd: transcripts/paula-2026: No such file or directory
I've finished the round-1 revision. The entry ran cleanly from a fresh environment in 46 minutes, `entry.py check` reports no errors, and every conclusion and note matches the final run. Nothing is committed.

**Main change: which units are used.** The report was right that choosing all units went against the claims file's own test (Table I's neuron counts). The paper's 102 sessions can't be found among the dataset's 153, so I compared counts per population and scaled to 102 sessions, for six filters. The filter from the Allen Institute's Visual Behavior Neuropixels tutorial (snr > 1, ISI violations < 1, firing rate > 0.1) matches Table I almost exactly: 0.93 to 1.02 times the paper's neuron counts per area, and neurons per population within 5%. All units come out 1.28 to 1.43 times too high and the claims file's quality filter 0.34 to 0.55 times too low. I adopted the tutorial filter as an assumption, citing the AllenSDK file at a pinned commit. Every claim now also runs under the claims file's two filters. Ten claims would come out differently under one of them, and a table at the end of the notebook shows this.

**Outcomes now:** 12 reproduced, 6 partially reproduced, 20 not reproduced (before: 13, 15, 10).
- **To reproduced:**
  - `fig2a-hippocampus-cv-stable`: under the new filter all seven values are within tolerance.
  - `fig1e-positive-cv-modules` and `fig1e-dg-ca3-anticorrelation-hubs`: these hold when the per-session correlations are averaged. I adopted that combination because joining sessions' series mixes in differences between sessions, as the verifier noted.
- **To partially reproduced:**
  - `fig1c-cv-region-medians`: all medians match and only the spreads (IQRs) miss.
  - `fig2b-visually-driven-js-cv-low`: the verifier's outcome.
- **To not reproduced:**
  - `fig4b-thalamus-lgd-lp-modulated`: LP's spontaneous median of 0.098 sits just below the legend's 0.099. Under the other t
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/paula-2026; cat verifier-1-report.md
```

```
**Verifier report, round 1: de Paula et al. 2026 (doi:10.1103/wndc-k654) on DANDI:000713 0.240702.1725**

The claims file has 38 claims. The notebook tests all 38 and treats none as blocked. My outcomes: 10 reproduced, 6 partially reproduced, 22 not reproduced.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| table1-sample | not_reproduced | 153 sessions under every reading, against 102 (cell 8). With all units, the neuron counts are about 2× Table I. With the quality filter (qc), the window counts match but the populations and neurons do not. |
| fig1c-cv-region-medians | not_reproduced | All units: the medians of DG (0.564) and NB (0.564) fall outside the widened ranges, and the TH, HP and MB extremes miss. qc: the TH maximum (0.414) misses (cell 12). |
| fig1c-cv-above-surrogate | partially_reproduced | Every Mann-Whitney test gives p ≤ 1.5e-73 with empirical higher, and the VIS surrogate medians are 0.225 to 0.243. The HP ratios for POST (1.32) and DG (3.01) fall outside 1.35 to 2.42 under all five seeds (cell 14). This is the claim's partial rule. |
| fig1d-surrogate-abolishes-cv-correlations | not_reproduced | Surrogate \|r\| reaches 0.79 under reading (a) and 0.66 under (b). 115 and 213 pairs exceed 0.2 (cell 16). |
| fig1e-positive-cv-modules | not_reproduced | Reading (a): top value 0.772, above 0.737. Reading (b): low end 0.450, just outside 0.50 ± 0.05. Same-area fractions (66% and 81%) do hold (cell 18). |
| fig1e-dg-ca3-anticorrelation-hubs | not_reproduced | Reading (b): CA3 and DG are the hubs, but the most negative r is −0.178 (expected −0.27 ± 0.027). Reading (a): NB is the hub and the most negative r is −0.496 (cell 20). |
| fig1e-midbrain-weakest-cv-correlations | not_reproduced | Reading (a): MB mean \|r\| (0.186) is above HP (0.179). Reading (b): only 2 of 115 MB pairs are near zero (cell 22). |
| fig2a-vis-cv-by-condition | reproduced | 12/12 medians within tolerance under readings a/a and b/a with all units (cell 26). The values 
[... 63 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/paula-2026; cat verifier-2-report.md; ls ../../questions/paula-2026.yaml 2>&1
```

```
**Verifier report, round 2: de Paula et al. 2026 (doi:10.1103/wndc-k654) on DANDI:000713 0.240702.1725**

The claims file has 38 claims, and the attempt record has 38 outcomes: 12 reproduced, 6 partially reproduced and 20 not reproduced. They match the notebook's Summary (cell 137) and its verdict table (cell 136).

### 1. Outcomes and assumptions

I agree with all 38 stated outcomes. Each one follows from the claims-file criterion applied to the printed outputs.

- **Changed since round 1.** The record agrees with my round-1 outcome on 31 claims and moves seven. Six move because of the new unit filter, 'vbn' (snr > 1, ISI violations < 1, firing rate > 0.1 spikes/s):
  - fig1c-cv-region-medians: not reproduced → partially reproduced
  - fig1e-positive-cv-modules: not reproduced → reproduced
  - fig1e-dg-ca3-anticorrelation-hubs: not reproduced → reproduced
  - fig2a-hippocampus-cv-stable: not reproduced → reproduced
  - fig3c-vis-ch-plane: stays not reproduced
  - fig4b-thalamus-lgd-lp-modulated: reproduced → not reproduced

  The seventh, fig4b-other-thalamus-not-modulated, moves from my partially reproduced to not reproduced because of the stricter pairwise test (cell 93). I accept that: Kruskal-Wallis finds MGd, SGN, MGm and MGv, the any-pair Mann-Whitney test finds MGd, SGN and MGv, and the criterion says "not reproduced when the test finds modulation in any".
- **Assumptions.** All 36 claims on the recordings other than table1-sample carry `assumed: true`, and fig3a-reference-systems does too. Each states the 'vbn' unit filter in its deviations, with the evidence for it. That evidence holds:
  - Neurons per population are within 5% of Table I in every area (VIS 92.7 against 92.1, TH 64.7 against 65.6, HP 112.0 against 116.8, MB 98.0 against 98.1; cell 8).
  - It is the closest of the six filters by largest |log ratio| (0.073).
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import yaml;a=yaml.safe_load(open('attempts/paula-2026-01.yaml'))
for v in a['verifications']:
  print(sum(r['agrees'] for r in v['results']),len(v['results']),[r['claim'] for r in v['results'] if not r['agrees']])
print(len(a['findings']));print([ (f['kind'],f.get('severity')) for f in a['findings']])
print(sum(o.get('assumed',False) for o in a['outcomes']))
"; cat questions/paula-2026.yaml | head -30
```

```
24 38 ['fig1e-positive-cv-modules', 'fig1e-dg-ca3-anticorrelation-hubs', 'fig1e-midbrain-weakest-cv-correlations', 'fig2a-hippocampus-cv-stable', 'fig2a-midbrain-cv-invariant', 'fig2b-visually-driven-js-cv-low', 'fig2b-dg-ca3-high-js-cv', 'fig3c-vis-ch-plane', 'fig4a-vis-complexity-by-condition', 'fig4b-other-thalamus-not-modulated', 'fig4e-js-complexity-natural-images', 'fig5-vis-complexity-cv-coupling', 'fig5-th-weaker-coupling', 'fig5-mb-flat']
38 38 []
11
[('selection_undocumented', None), ('methods_unavailable', None), ('methods_unavailable', None), ('methods_unavailable', None), ('methods_unavailable', None), ('methods_unavailable', None), ('methods_unavailable', None), ('other', 'none'), ('other', 'none'), ('methods_unavailable', None), ('paper_inconsistency', None)]
37
dandiset: "000713"
paper: doi:10.1103/wndc-k654
questions:
- claim: table1-sample
  asked: 2026-11-27
  attempt: paula-2026-01
  question: The opening comment gives unit reading (b) as "the Allen default filters for this dataset
    (ISI violations < 0.5, amplitude cutoff < 0.1, presence ratio > 0.9)". The verifier of attempt
    paula-2026-01 reports that the AllenSDK default presence-ratio cutoff is 0.95, not 0.9, and the
    claims file's own check says the defaults were not verified. The Allen Institute's Visual Behavior
    Neuropixels quickstart tutorial filters units by snr > 1, ISI violations < 1 and firing rate > 0.1
    spikes/s instead. Should reading (b) give the defaults that apply to this dataset, and should the
    tutorial's filter be a reading of its own?
  passage: Methods II.A, "local neuronal populations from each brain region with at least 30 recorded
    neurons sampled across a minimum of eight recording sessions"; Table I, "Neurons analyzed". The
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,60p tools/readme_row.py; grep -n -A3 "^- id: fig3a" claims/paula-2026.yaml; sed -n 558,575p claims/paula-2026.yaml
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
[... 62 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/paula-2026-01.md",
 "content": "# paula-2026, de Paula et al. 2026\n\nTwelve claims reproduced on the dandiset, five partially, twenty not reproduced\nand none blocked; `fig3a-reference-systems`, which places synthetic reference\nseries in the complexity-entropy plane (`data: elsewhere`), is counted apart and\npartially reproduced. Every outcome but `table1-sample` rests on an assumption,\nchiefly the unit filter. The first verification round agreed with 24 of the 38\noutcomes. Of the fourteen it gave otherwise, the author took the verifier's not\nreproduced for nine claims whose criteria have no partial rule and its partially\nreproduced for `fig2b-visually-driven-js-cv-low`; `fig1e-positive-cv-modules`,\n`fig1e-dg-ca3-anticorrelation-hubs` and `fig2a-hippocampus-cv-stable`, not\nreproduced for the verifier, became reproduced under a new unit filter, and\n`fig4b-other-thalamus-not-modulated`, partially reproduced for the verifier,\nbecame not reproduced under a stricter test. The new filter also moved\n`fig1c-cv-region-medians` to partially reproduced and\n`fig4b-thalamus-lgd-lp-modulated` to not reproduced. The second round agreed\nwith all 38, and nothing was proposed after it, so there was no third round. It\npins version 0.240702.1725, the one the paper cites and the only published one.\nThe paper, de Paula, Jungmann, Fontenele, Aguiar, Carelli, Matias, Copelli and\nde Vasconcelos, \"Revealing Stimulus-Dependent Dynamics Through Statistical\nComplexity\" (PRX Life 4, 023018), cuts the spiking of local populations in 26\nsubregions of visual cortex, thalamus, hippocampus and midbrain, from 102\nsessions of the Allen Institute's Visual Behavior Neuropixels dataset, into\n100-s windows of natural images, active behavior, blanks and spontaneous\nactivity, and compares the coefficient of variation (CV) of the population rate\nwith Bandt and Pompe permutation entropy H and statistical complexity C across\nareas and conditions. The claims were written from the text of the version of\nrecord and its supplement, as the PDF could not be rendered; the paper links no\ncode. The CV medians by condition in visual cortex, thalamus and hippocampus,\nthe order of complexity by area (VIS 0.158, HP 0.159, TH 0.108, MB 0.098), the\nthalamic, hippocampal and midbrain C-H planes, the DG and CA3 complexity, the\nmidbrain invariance and the separation of natural images from spontaneous\nactivity by complexity reproduce. `table1-sample` is not reproduced, as all\n153 sessions pass the paper's thresholds, against 102. The surrogates do not\nabolish the CV correlations between regions, VISp breaks the order of\ncomplexity across conditions (natural images 0.174 below active 0.187), LP's\nspontaneous median of 0.098 falls just below the legend's range, four of the\nseven \"unmodulated\" thalamic nuclei are modulated, the visual C-H plane misses\nnarrowly (C 2.5th percentile 0.0887 against 0.090), and most Jensen-Shannon\ndivergence claims, the complexity range fractions, the C-CV trajectories of\nFig. 5 and the mean correlations of supplementary Fig. 6 do not reproduce. The\nauthor's first pass used all units, for 12 reproduced, 16 partially and 10 not\nreproduced; round 1 found that this went against the claims file's own test,\nTable I's neuron counts, and in reply six filters were compared and the filter\nof the Allen tutorial (snr > 1, ISI violations < 1, firing rate > 0.1 spikes/s)\nadopted, with both of the claims file's readings run for every claim; ten\noutcomes differ under one of them. Round 1 also found that the Ikeda map was\njudged at an unsourced parameter, that the sine rule could not be met, and\nthat the pairwise test of the absence claim in Fig. 4b was too lenient; in\nreply the Ikeda map was judged at 0.4 + 2 pi and 0.4 + 4 pi, the sine against\nits floor, the pairwise p-values were printed and outputs on sessions, blanks\nand natural-log divergences were added. Two questions went to a reader in\n`questions/paula-2026.yaml`, on the presence-ratio cutoff of the claims file's\nquality filter and on how to read \"H near 0\" for the sine. Round 2 found\nsentences the outputs did not support, among them a p-value, a summary sentence\non omitted flashes, three findings out of date and the README's run time, which\nwere corrected; in reply Fig. 3a was read from the PDF, its labelled parameters\nwere run, and a finding was added. The author's run took about 3 h 36 min (10:00\nto about 13:36 UTC). The first `entry.py all` failed on the 60-minute cell\ntimeout, as each of four worker processes ran several BLAS threads at once, and\nsetting the thread variables in the first cell fixed it; a clean run took 36.5\nminutes, 35.7 of them streaming the 153 sessions, 46 minutes after round 1 and\n43 at the end.\n\nThe paper analyses 102 sessions and 1437 populations without saying how the\nsessions were chosen, and they cannot be identified: the dandiset holds 153\necephys sessions of 81 mice, every one with populations that pass the paper's\nrule and with the gray-screen epoch, and no grouping by genotype (59, 49, 45),\nimage set and novelty (68, 10, 10, 65) or probe count (142 with six probes)\ngives 102, so population and window counts are about 1.5 times the paper's. No\nunit selection is stated: scaled to 102 sessions, all units give 1.28 to 1.43\ntimes Table I's area neuron counts and the Allen quality filters 0.34 to 0.55\ntimes, dropping NOT, while the tutorial filter gives 0.93 to 1.02 times with\nneurons per population within 5% of Table I's. The surrogate is defined per\nanalyzed window, and shuffled within each 100-s window the surrogate CV series\nstay correlated across regions (up to |r| 0.90, 143 to 241 of 325 pairs above\n0.2), because each window keeps its spike count. The JS divergences of Figs. 2b\nand 4e to 4h give no histogram bins or log base, the main diagonal that is\nsummed is zero for a region-pair matrix, and the percentage difference is not\ndefined, and the results depend on these choices (active against blanks 3.1% to\n11.2% in visual cortex under the adopted filter, 0.3% to 9.5% with all units).\nThe test of modulation across conditions is not named; for MGd, SGN, MGm and\nMGv a Kruskal-Wallis test on windows gives p < 0.001, and tests on one median\nper population find the same four. Fig. 5 gives no CV bin width or minimum\ncount, and Fig. 3a no series length, transient or sine sampling; at the\nparameters the figure labels the series here match 16 of its 18 markers within\n0.03. Methods II.A gives the blank series as about 240 s per image, but each\nimage is shown 320 to 1056 times per session (median 572.5), so the series is\nabout 286 s (median; 271 s without change flashes, 275 s when only gray screens\nfollowed by another flash are kept). Fig. 1d and 1e do not say how a region\npair's correlations are combined over sessions: concatenating gives a top-10%\nrange of 0.469 to 0.798, averaging per-session correlations 0.478 to 0.680 with\nDG and CA3 as the hubs, which matches the paper and is adopted. In the paper,\nResults III.C places exponentially correlated processes at C 0.3 to 0.5 and the\nsine at H near 0, but Fig. 3a shows the correlated walk at C 0.22 to 0.35 and\nthe sine at H about 0.11, close to the least H a sine can have at D = 6 (0.105).\nThe checks passed: each session has an active block of 3599 to 3611 s, a 289-s\ngray screen after it, eight images and 1103 to 3388 units, no two sessions\nshare a spike-time fingerprint, and visual cortex spikes rise after flash\nonsets in all 153 sessions (69 to 434 spikes per flash) and not after onsets\nshifted by 375 ms (-371 to 1.6). Some units carry generic labels (TH, MB, HPF)\nor labels outside the paper's list (Eth, LGv, ZI), left out as in Table I. No\nfinding is critical. Eight questions are put to the paper's authors: which 102\nsessions and which units were used, over what span the surrogates were\nshuffled, how the JS divergences were computed, which modulation test was used,\nthe Fig. 5 bins and Fig. 3a series lengths, how the blank intervals were\nchosen, and how sessions were combined in Fig. 1d and 1e.\n\nThe author's points on the protocol: surrogates shared by several claims have\nno seed of their own, and they were drawn once under the seed of\n`fig1c-cv-above-surrogate` with the session and window indices and recorded as\na deviation; several criteria have no partial rule, and partially reproduced\nwas used where the qualitative part held, which round 1 reversed; the check\nrequires `inputs` on a tested `data: elsewhere` claim even when the data are\nsynthetic, and the supplement's definitions were listed; it does not say that\nthread-count settings must come before numpy is first imported, which cost the\nfirst clean run; and the pilot-19 code in `entry.py` reads `notebook` and\n`output` on findings while the attempt schema rejects them, so they were left\noff.\n"
}
```

```
File created successfully at: docs/pilot-notes/paula-2026-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  cat > summaries/paula-2026-01.md <<'EOF'
In this data the paper's hierarchy across areas largely holds up: complexity is highest in visual cortex and hippocampus and lowest in midbrain, each area sits in the complexity-entropy plane much as reported, and CV changes with stimulus condition in visual cortex, thalamus and hippocampus as described. Not reproduced are the loss of cross-regional CV correlations in shuffled surrogates, the ordering of visual complexity across conditions (VISp breaks it), most Jensen-Shannon divergence comparisons and the coupling of complexity with CV. The surrogate result likely depends on the span shuffled, which the paper does not give. Every claim could be tested, but the paper names neither its unit filter nor which 102 of 153 sessions it used, so the results rest on an assumed filter and all sessions.
EOF
wc -w summaries/paula-2026-01.md; ls summaries | head -3; grep -c "—\|rather" summaries/paula-2026-01.md docs/pilot-notes/paula-2026-01.md; git status --short
```

```
127 summaries/paula-2026-01.md
README.md
allen-2026-01.md
amjad-2025-01.md
summaries/paula-2026-01.md:0
docs/pilot-notes/paula-2026-01.md:0
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
?? docs/pilot-notes/paula-2026-01.md
?? scripts
?? summaries/paula-2026-01.md
```

**Agent calls Bash**

```bash
cd  cat summaries/README.md | head -30
```

```
# Attempt summaries

One file per attempt, `summaries/<attempt id>.md`: a paragraph of at most five sentences, written by the recorder (docs/agents/recorder.md, step 2) and shown at the top of the dataset's page.
```

**Agent**

The summary came to 127 words, over the 120-word limit, so I'm cutting it down.

**Agent calls Bash**

```bash
cd  cat > summaries/paula-2026-01.md <<'EOF'
In this data the paper's hierarchy across areas largely holds up: complexity is highest in visual cortex and hippocampus and lowest in midbrain, and CV changes with stimulus condition in visual cortex, thalamus and hippocampus as described. Not reproduced are the loss of cross-regional CV correlations in shuffled surrogates, the ordering of visual complexity across conditions (VISp breaks it), most Jensen-Shannon divergence comparisons and the coupling of complexity with CV. The surrogate result likely depends on the span shuffled, which the paper does not give. Every claim could be tested, but the paper names neither its unit filter nor which 102 of 153 sessions it used. All results rest on an assumed filter and all sessions.
EOF
wc -w summaries/paula-2026-01.md
```

```
116 summaries/paula-2026-01.md
```

**Agent**

I wrote both files and changed nothing else. Nothing is committed. Dandiset 000713 has no entry in `targets/dandisets.json`, so there is no `catalystneuro` field to report and the notes do not open with the CatalystNeuro sentence.

`docs/pilot-notes/paula-2026-01.md`:

# paula-2026, de Paula et al. 2026

Twelve claims reproduced on the dandiset, five partially, twenty not reproduced and none blocked; `fig3a-reference-systems`, which places synthetic reference series in the complexity-entropy plane (`data: elsewhere`), is counted apart and partially reproduced. Every outcome but `table1-sample` rests on an assumption, chiefly the unit filter. The first verification round agreed with 24 of the 38 outcomes. Of the fourteen it gave otherwise, the author took the verifier's not reproduced for nine claims whose criteria have no partial rule and its partially reproduced for `fig2b-visually-driven-js-cv-low`; `fig1e-positive-cv-modules`, `fig1e-dg-ca3-anticorrelation-hubs` and `fig2a-hippocampus-cv-stable`, not reproduced for the verifier, became reproduced under a new unit filter, and `fig4b-other-thalamus-not-modulated`, partially reproduced for the verifier, became not reproduced under a stricter test. The new filter also moved `fig1c-cv-region-medians` to partially reproduced and `fig4b-thalamus-lgd-lp-modulated` to not reproduced. The second round agreed with all 38, and nothing was proposed after it, so there was no third round. It pins version 0.240702.1725, the one the paper cites and the only published one. The paper, de Paula, Jungmann, Fontenele, Aguiar, Carelli, Matias, Copelli and de Vasconcelos, "Revealing Stimulus-Dependent Dynamics Through Statistical Complexity" (PRX Life 4, 023018), cuts the spiking of local populations in 26 subregions of visual cortex, thalamus, hippocampus and midbrain, from 102 sessions of the Allen Institute's Visual Behavior Neuropixels dataset, into 100-s windows of natural images, active behavior, blanks and spontaneous activity, and compares the coefficient of variation (CV) of the population rate with Bandt and Pompe permutation entropy H and statistical complexity C across areas and conditions. The claims were written from the text of the version of record and its supplement, as the PDF could not be rendered; the paper links no code. The CV medians by condition in visual cortex, thalamus and hippocampus, the order of complexity by area (VIS 0.158, HP 0.159, TH 0.108, MB 0.098), the thalamic, hippocampal and midbrain C-H planes, the DG and CA3 complexity, the midbrain invariance and the separation of natural images from spontaneous activity by complexity reproduce. `table1-sample` is not reproduced, as all 153 sessions pass the paper's thresholds, against 102. The surrogates do not abolish the CV correlations between regions, VISp breaks the order of complexity across conditions (natural images 0.174 below active 0.187), LP's spontaneous median of 0.098 falls just below the legend's range, four of the seven "unmodulated" thalamic nuclei are modulated, the visual C-H plane misses narrowly (C 2.5th percentile 0.0887 against 0.090), and most Jensen-Shannon divergence claims, the complexity range fractions, the C-CV trajectories of Fig. 5 and the mean correlations of supplementary Fig. 6 do not reproduce. The author's first pass used all units, for 12 reproduced, 16 partially and 10 not reproduced; round 1 found that this went against the claims file's own test, Table I's neuron counts, and in reply six filters were compared and the filter of the Allen tutorial (snr > 1, ISI violations < 1, firing rate > 0.1 spikes/s) adopted, with both of the claims file's readings run for every claim; ten outcomes differ under one of them. Round 1 also found that the Ikeda map was judged at an unsourced parameter, that the sine rule could not be met, and that the pairwise test of the absence claim in Fig. 4b was too lenient; in reply the Ikeda map was judged at 0.4 + 2 pi and 0.4 + 4 pi, the sine against its floor, the pairwise p-values were printed and outputs on sessions, blanks and natural-log divergences were added. Two questions went to a reader in `questions/paula-2026.yaml`, on the presence-ratio cutoff of the claims file's quality filter and on how to read "H near 0" for the sine. Round 2 found sentences the outputs did not support, among them a p-value, a summary sentence on omitted flashes, three findings out of date and the README's run time, which were corrected; in reply Fig. 3a was read from the PDF, its labelled parameters were run, and a finding was added. The author's run took about 3 h 36 min (10:00 to about 13:36 UTC). The first `entry.py all` failed on the 60-minute cell timeout, as each of four worker processes ran several BLAS threads at once, and setting the thread variables in the first cell fixed it; a clean run took 36.5 minutes, 35.7 of them streaming the 153 sessions, 46 minutes after round 1 and 43 at the end.

The paper analyses 102 sessions and 1437 populations without saying how the sessions were chosen, and they cannot be identified: the dandiset holds 153 ecephys sessions of 81 mice, every one with populations that pass the paper's rule and with the gray-screen epoch, and no grouping by genotype (59, 49, 45), image set and novelty (68, 10, 10, 65) or probe count (142 with six probes) gives 102, so population and window counts are about 1.5 times the paper's. No unit selection is stated: scaled to 102 sessions, all units give 1.28 to 1.43 times Table I's area neuron counts and the Allen quality filters 0.34 to 0.55 times, dropping NOT, while the tutorial filter gives 0.93 to 1.02 times with neurons per population within 5% of Table I's. The surrogate is defined per analyzed window, and shuffled within each 100-s window the surrogate CV series stay correlated across regions (up to |r| 0.90, 143 to 241 of 325 pairs above 0.2), because each window keeps its spike count. The JS divergences of Figs. 2b and 4e to 4h give no histogram bins or log base, the main diagonal that is summed is zero for a region-pair matrix, and the percentage difference is not defined, and the results depend on these choices (active against blanks 3.1% to 11.2% in visual cortex under the adopted filter, 0.3% to 9.5% with all units). The test of modulation across conditions is not named; for MGd, SGN, MGm and MGv a Kruskal-Wallis test on windows gives p < 0.001, and tests on one median per population find the same four. Fig. 5 gives no CV bin width or minimum count, and Fig. 3a no series length, transient or sine sampling; at the parameters the figure labels the series here match 16 of its 18 markers within 0.03. Methods II.A gives the blank series as about 240 s per image, but each image is shown 320 to 1056 times per session (median 572.5), so the series is about 286 s (median; 271 s without change flashes, 275 s when only gray screens followed by another flash are kept). Fig. 1d and 1e do not say how a region pair's correlations are combined over sessions: concatenating gives a top-10% range of 0.469 to 0.798, averaging per-session correlations 0.478 to 0.680 with DG and CA3 as the hubs, which matches the paper and is adopted. In the paper, Results III.C places exponentially correlated processes at C 0.3 to 0.5 and the sine at H near 0, but Fig. 3a shows the correlated walk at C 0.22 to 0.35 and the sine at H about 0.11, close to the least H a sine can have at D = 6 (0.105). The checks passed: each session has an active block of 3599 to 3611 s, a 289-s gray screen after it, eight images and 1103 to 3388 units, no two sessions share a spike-time fingerprint, and visual cortex spikes rise after flash onsets in all 153 sessions (69 to 434 spikes per flash) and not after onsets shifted by 375 ms (-371 to 1.6). Some units carry generic labels (TH, MB, HPF) or labels outside the paper's list (Eth, LGv, ZI), left out as in Table I. No finding is critical. Eight questions are put to the paper's authors: which 102 sessions and which units were used, over what span the surrogates were shuffled, how the JS divergences were computed, which modulation test was used, the Fig. 5 bins and Fig. 3a series lengths, how the blank intervals were chosen, and how sessions were combined in Fig. 1d and 1e.

The author's points on the protocol: surrogates shared by several claims have no seed of their own, and they were drawn once under the seed of `fig1c-cv-above-surrogate` with the session and window indices and recorded as a deviation; several criteria have no partial rule, and partially reproduced was used where the qualitative part held, which round 1 reversed; the check requires `inputs` on a tested `data: elsewhere` claim even when the data are synthetic, and the supplement's definitions were listed; it does not say that thread-count settings must come before numpy is first imported, which cost the first clean run; and the pilot-19 code in `entry.py` reads `notebook` and `output` on findings while the attempt schema rejects them, so they were left off.

`summaries/paula-2026-01.md` (116 words):

In this data the paper's hierarchy across areas largely holds up: complexity is highest in visual cortex and hippocampus and lowest in midbrain, and CV changes with stimulus condition in visual cortex, thalamus and hippocampus as described. Not reproduced are the loss of cross-regional CV correlations in shuffled surrogates, the ordering of visual complexity across conditions (VISp breaks it), most Jensen-Shannon divergence comparisons and the coupling of complexity with CV. The surrogate result likely depends on the span shuffled, which the paper does not give. Every claim could be tested, but the paper names neither its unit filter nor which 102 of 153 sessions it used. All results rest on an assumed filter and all sessions.

## End of run

25 turns, 3 minutes, $1.54 at API prices, result: success.
