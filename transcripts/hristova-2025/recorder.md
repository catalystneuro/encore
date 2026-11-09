# 001888 · recorder · run 39245401272

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
python tools/readme_row.py 001888 --write; git diff; ls claims/001888 transcripts/001888; cat attempts/001888-hristova-2025-01.yaml
```

```
<persisted-output>
Output too large (46.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/41f5d397-0093-4cd6-a6a3-f1b53220a6ed/tool-results/bdcltphpu.txt

Preview (first 2KB):
diff --git a/README.md b/README.md
index 844b950..6ddf675 100644
--- a/README.md
+++ b/README.md
@@ -102,6 +102,7 @@ please [open an issue](https://github.com/catalystneuro/reproduction-registry/is
 | [001699](https://dandiarchive.org/dandiset/001699) | [Moore et al. 2025](https://doi.org/10.1101/2025.01.09.632139) | 14 | 7 | 5 | 1 | [`001699-moore-2025`](entries/001699-moore-2025) |
 | [001878](https://dandiarchive.org/dandiset/001878) | [Sun et al. 2021](https://doi.org/10.22002/d1.1991) | 4 (+1) | 2 (+1) | 0 | 0 | [`001878-sun-2021`](entries/001878-sun-2021) |
 | [001712](https://dandiarchive.org/dandiset/001712) | [Davatolhagh et al. 2025](https://doi.org/10.1101/2025.09.12.675910) | 3 | 2 | 2 | 11 | [`001712-davatolhagh-2025`](entries/001712-davatolhagh-2025) |
+| [001888](https://dandiarchive.org/dandiset/001888) | [Hristova et al. 2025](https://doi.org/10.1111/epi.18606) | 13 | 9 | 2 | 10 | [`001888-hristova-2025`](entries/001888-hristova-2025) |
 
 Counts are of claims that rest on the dandiset, including those that take
 names for its own codes from elsewhere. Claims that also use data from
claims/001888:
10.1111-epi.18606.yaml

transcripts/001888:
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
git diff --stat; grep -n "^| \[001888\|^| Dandiset\|^| ---" README.md | head; sed -n 80,100p README.md; cat attempts/001888-hristova-2025-01.yaml
```

```
<persisted-output>
Output too large (49.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/41f5d397-0093-4cd6-a6a3-f1b53220a6ed/tool-results/bx8zi9aw3.txt

Preview (first 2KB):
 README.md | 1 +
 1 file changed, 1 insertion(+)
49:| Dandiset | Paper | Reproduced | Partially | Not reproduced | Blocked | Entry |
105:| [001888](https://dandiarchive.org/dandiset/001888) | [Hristova et al. 2025](https://doi.org/10.1111/epi.18606) | 13 | 9 | 2 | 10 | [`001888-hristova-2025`](entries/001888-hristova-2025) |
| [000226](https://dandiarchive.org/dandiset/000226) | [Severson et al. 2017](https://doi.org/10.1016/j.neuron.2017.03.045) | 12 (+2) | 2 (+1) | 0 | 11 | [`000226-severson-2017`](entries/000226-severson-2017) |
| [000232](https://dandiarchive.org/dandiset/000232) | [Chang et al. 2023](https://doi.org/10.1101/2023.08.21.554194) | 19 | 7 | 2 | 1 | [`000232-chang-2023`](entries/000232-chang-2023) |
| [000239](https://dandiarchive.org/dandiset/000239) | [Xu et al. 2022](https://doi.org/10.1038/s41586-022-04478-7) | 20 | 5 | 3 | 11 | [`000239-xu-2022`](entries/000239-xu-2022) |
| [000350](https://dandiarchive.org/dandiset/000350) | [Mu et al. 2019](https://doi.org/10.1016/j.cell.2019.05.050) | 2 | 3 | 4 | 10 | [`000350-mu-2019`](entries/000350-mu-2019) |
| [000409](https://dandiarchive.org/dandiset/000409) | [Ibl et al. 2025](https://doi.org/10.1038/s41586-025-09235-0) | 17 | 3 | 3 | 7 | [`000409-ibl-2025`](entries/000409-ibl-2025) |
| [000552](https://dandiarchive.org/dandiset/000552) | [Huszar et al. 2022](https://doi.org/10.1038/s41593-022-01138-x) | 5 | 4 | 3 | 23 | [`000552-huszar-2022`](entries/000552-huszar-2022) |
| [000568](https://dandiarchive.org/dandiset/000568) | [Valero et al. 2022](https://doi.org/10.1126/science.abm1891) | 4 | 6 | 6 | 6 | [`000568-valero-2022`](entries/000568-valero-2022) |
| [000559](https://dandiarchive.org/dandiset/000559) | [Markowitz et al. 2023](https://doi.org/10.1038/s
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^### " docs/pilot-notes.md | tail -6; python -c "
import json;d=json.load(open('targets/dandisets.json'))
it=d if isinstance(d,list) else d.get('dandisets',d)
import sys
for e in (it if isinstance(it,list) else it.values()):
  if '001888' in json.dumps(e): print(json.dumps(e,indent=1))
"
```

```
<persisted-output>
Output too large (172.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/41f5d397-0093-4cd6-a6a3-f1b53220a6ed/tool-results/bknpdnkw1.txt

Preview (first 2KB):
3803:### 001538, Zhai et al. 2025
3902:### 001550, Pagan et al. 2025
4011:### 001692, Bouabid et al. 2026
4116:### 001699, Moore et al. 2025
4228:### 001878, Sun et al. 2021
4320:### 001712, Davatolhagh et al. 2025
[
 {
  "dandiset": "000003",
  "name": "Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells",
  "published_version": "0.260218.2052",
  "asset_count": 101,
  "size_gb": 2559.25,
  "data_standards": [
   "Neurodata Without Borders (NWB)"
  ],
[... 59 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;d=json.load(open('targets/dandisets.json'))
for e in d:
  if e['dandiset']=='001888': print(json.dumps(e,indent=1))
" > $TMPDIR/t.txt 2>&1; wc -l docs/pilot-notes.md attempts/001888-hristova-2025-01.yaml transcripts/001888/*report.md claims/001888/*.yaml > $TMPDIR/w.txt
```

```
(Bash completed with no output)
```

**Agent calls Read**

```json
{
 "file_path": "docs/pilot-notes.md",
 "offset": 3900
}
```

```
File content (287.2KB) exceeds maximum allowed size (256KB). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Bash**

```bash
cat $TMPDIR/t.txt $TMPDIR/w.txt; awk 'NR>=3902' docs/pilot-notes.md | wc -c
```

```
Traceback (most recent call last):
  File "<string>", line 4, in <module>
    if e['dandiset']=='001888': print(json.dumps(e,indent=1))
       ~^^^^^^^^^^^^
TypeError: string indices must be integers, not 'str'
  4418 docs/pilot-notes.md
   869 attempts/001888-hristova-2025-01.yaml
    69 transcripts/001888/author-report.md
    34 transcripts/001888/author-revise-1-report.md
    18 transcripts/001888/author-revise-2-report.md
    69 transcripts/001888/verifier-1-report.md
    49 transcripts/001888/verifier-2-report.md
   339 claims/001888/10.1111-epi.18606.yaml
  5865 total
37161
```

**Agent calls Read**

```json
{
 "file_path": "docs/pilot-notes.md",
 "offset": 3902
}
```

```
File content (287.2KB) exceeds maximum allowed size (256KB). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Bash**

```bash
grep -n -B2 -A30 '"dandiset": "001888"' targets/dandisets.json
```

```
6290-  },
6291-  {
6292:   "dandiset": "001888",
6293-   "name": "EEG recordings from a Grin2b+/- rat model of GRIN2B neurodevelopmental disorder: absence seizures and sleep-wake abnormalities",
6294-   "published_version": null,
6295-   "asset_count": 17,
6296-   "size_gb": 21.3,
6297-   "data_standards": [
6298-    "Neurodata Without Borders (NWB)"
6299-   ],
6300-   "species": [
6301-    "Rattus norvegicus - Norway rat"
6302-   ],
6303-   "approaches": [
6304-    "electrophysiological approach"
6305-   ],
6306-   "papers": [
6307-    {
6308-     "doi": "10.1111/epi.18606",
6309-     "title": "Absence seizures and sleep-wake abnormalities in a rat model of GRIN2B neurodevelopmental disorder",
[... 13 more lines not kept]
```

**Agent**

README row is written (13 / 9 / 2 / 10). Now reading the prior pilot-notes subsections and the run reports.

**Agent calls Bash**

```bash
sed -n '3902,4418p' docs/pilot-notes.md
```

```
<persisted-output>
Output too large (36.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/41f5d397-0093-4cd6-a6a3-f1b53220a6ed/tool-results/bcla6kxkl.txt

Preview (first 2KB):
### 001550, Pagan et al. 2025

Eleven claims reproduced and two partially on the dandiset, none not
reproduced or blocked. With outside data, counted apart: two reproduced and
one not reproduced. Seven claims on the paper's neural data and RNNs in its
GitHub repositories: two reproduced, one not reproduced and four blocked.
Round 1 gave its own outcome for each claim from the notebook with its
conclusions removed and agreed with all 23, giving `other` as the reason for
the three blocks the author gave as `not_runnable`; the author kept
`not_runnable` and round 2 accepted it. Round 1 also found that the port of
`ExtDataFigure5ag.m` took the full-space angle, which the code computes first
and overwrites, and not the projected, folded angle the code plots; with the
plotted angle `choice-axes-parallel` went from a mean of 40.34 to 4.73
degrees, still outside 1.44 to 1.76, and its criterion was corrected after
round 1 and again after round 2. Round 2 agreed with all 23 and nothing was
proposed, so there was no third round. The paper studies rats that weigh
[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/41f5d397-0093-4cd6-a6a3-f1b53220a6ed/tool-results/bcla6kxkl.txt",
 "offset": 200
}
```

```
200	a shuffle test of the hotspot procedure, which were added. Round 2 found
201	statements the outputs did not support, among them fig2d values kept from the
202	first run, a README run time of about fifteen minutes, and that the AND
203	exclusion keeps most stimulation responses, and these were corrected. Untracked
204	files in the repository root that the author did not create were left alone.
205	The author's points on the protocol: a count above the reported value, which
206	"partially reproduced" does not cover; a tolerance for means reported as mean ±
207	SD across sites; no rule whether to simplify or block a method too heavy for
208	the time limit; code with evident bugs; whether code read for parameters is an
209	input; whether to infer labels from the data or take them from outside the
210	dandiset; per-slice summary data classed as `data: elsewhere`; a clock check
211	for continuous sessions, where the contrast at locomotion initiations is weak
212	(ratio 1.28 for UG28); fitting the time limit by using 15 of the control mice's
213	114 sessions; and getting the paper when bioRxiv blocked downloads.
214	
215	### 001699, Moore et al. 2025
216	
217	Fourteen claims reproduced, seven partially, five not reproduced and one
218	blocked on the dandiset. Round 1 gave its own outcome for each claim from the
219	notebook with its conclusions removed and agreed with 24 of the 27; it would
[... 299 more lines not kept]
```

**Agent calls Bash**

```bash
cat transcripts/001888/author-report.md transcripts/001888/verifier-1-report.md
```

```
I've finished steps 1 to 5 and run the handover (step 6) for dandiset 001888; the entry passes `tools/entry.py all` with 0 errors. Of 34 claims, 12 are reproduced, 9 partially reproduced, 3 not reproduced and 10 blocked. I used the open-access full text and supplement (CC BY, PMC12779324), saved under `paper/`. The dandiset has no published version, so I pinned the draft as modified 2026-07-31 09:37 UTC; the notebook stops if the draft changes.

## 1. Outcomes per claim

| Claim | Outcome |
|---|---|
| fig2b-swd-hourly | reproduced (genotype p = 0.0045, hour p = 0.069) |
| fig2c-swd-number | reproduced (p = 0.047) |
| fig2c-swd-mean-duration | partially reproduced (only one WT rat has SWDs, p = 0.16) |
| fig2c-swd-total-duration | reproduced (p = 0.033) |
| disc-het-swd-minutes | partially reproduced (Het 57.8 min matches; WT 1.37 min is not under 1 min) |
| figs5a-swd-light-dark | reproduced |
| figs8-swd-sex | reproduced |
| fig2d-swd-spectrum-peak | reproduced (all 15 rats checked, including the WT) |
| fig3d-rem-hourly, fig3g-rem-total | reproduced, both at p = 0.048 |
| fig3g-rem-bouts | reproduced (p = 0.001) |
| fig3g-rem-bout-duration, fig3h-nrem-bouts, fig3i-wake-total, fig3i-wake-bouts | partially reproduced (right direction, not significant) |
| fig3h-nrem-total, fig4a-rem-spectrum | reproduced (both are "no difference" claims, tested with two WT rats) |
| fig4b-nrem-beta, fig4c-wake-power | not reproduced (effect goes the other way) |
| fig5a-swd-state-distribution | partially reproduced (wake 94.2% matches; NREM and REM shares do not) |
[... 118 more lines not kept]
```

**Agent calls Bash**

```bash
cat transcripts/001888/author-revise-1-report.md transcripts/001888/verifier-2-report.md transcripts/001888/author-revise-2-report.md
```

```
I changed one outcome: figs5b-transition-percent goes from not reproduced to reproduced. I worked through every point in the round-1 report and recorded each in the `verifications` block of the attempt record. The entry re-runs cleanly with `python tools/entry.py all` (336 s, check passes), and I checked every conclusion against the new outputs. Nothing is committed.

**Outcome changes**
- **figs5b-transition-percent:** now reproduced, measured 22.93% against 24.2 ± 2.42. The Supplementary Methods judge whether an SWD started in NREM using the six epochs before it (wake and REM use only the one epoch before). The claims file had used the one-epoch rule for NREM too, which gave 36.3%. I corrected the criterion, and the claims file and a deviation both say this was done after the analysis had been seen. The verifier itself gave not_reproduced under the old criterion, so round 2 will review this change. The claim's wild-type part still can't be tested.
- **fig2e and fig5a-het-more-nrem-swds:** still blocked, but the reason is now `data_missing` instead of `other`, as the verifier gave. The paper's other seven wild-type rats are not in the dandiset.
- **All other outcomes are unchanged.** The verifier agreed with all 34 as they stood.

**Added outputs**
- **Two doubtful rats:** every genotype test is also run without GRIN2B-228 (a Grin2b+/- rat with almost no SWDs), without GRIN2B-238 (a wild-type rat with none), and without both. What changes:
  - Without 228, fig5c would meet its criterion (13 of 13, p = 0.0095).
  - Without 228, fig3d and fig3g-rem-total lose significance (p = 0.060).
  - Without 238, fig3d's interaction becomes significant.
- **How SWDs are taken out of the sleep states:**
  - Removing only the SWD time keeps fig5f at R = −0.74.
  - With bouts that SWDs do not split, the wake-bout differences reverse and none of the eight fig5def correlations is significant.
- **Mixed model check:** a fitted random-intercept model gives the same genotype and interac
[... 85 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/001888-hristova-2025-01.yaml"
}
```

```
1	schema_version: 1
2	id: 001888-hristova-2025-01
3	dandiset: "001888"
4	dandiset_version: draft
5	paper: doi:10.1111/epi.18606
6	date: 2026-10-19
7	entry: 001888-hristova-2025
8	provenance:
9	  kind: agent
10	  accountable:
11	    name: CatalystNeuro
12	  agent:
13	    harness: Claude Code (GitHub Actions)
14	    model: claude-opus-5-5
15	    protocol: pilot-7
16	outcomes:
17	- claim: fig2b-swd-hourly
18	  outcome: reproduced
19	  notebook: reproduce_hristova_2025.ipynb
20	  output: claim:fig2b-swd-hourly
[... 850 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,60p claims/001888/10.1111-epi.18606.yaml
```

```
# Claims for Hristova, Fasol et al. (2025), Epilepsia 66:4996-5013, on dandiset 001888.
# Source: the open-access full text (CC BY, PMC12779324) and its Supporting Information
# (Supplementary Methods, Tables S1-S2, legends of Figures S1-S12).
#
# When these criteria were written, the author had seen the data check only: the file list, the
# subject metadata, the recording lengths and baseline windows, the codes present in the sleep
# scores and the per-epoch SWD file, the number and total duration of SWD events per animal and
# day, the minutes of each stored sleep state per animal and day (without SWD epochs removed),
# the ranges of the stored spectra, the raw values, and the clock checks. No bout, hourly,
# spectral-band or SWD-onset measure had been seen. A first execution of the notebook ran the
# claim cells; their outputs were not read before this file was revised after the data check
# (genotype taken from the files, where an earlier draft took it from the conversion
# repository; SWD epochs taken from the events, where an earlier draft took the scorer's
# flags), and no criterion was changed after any claim output was read, with one exception: after
# the first verification round, the NREM rule of figs5b-transition-percent was corrected to the
# Supplementary Methods (see that claim). Its first rule gave 36.3%, outside tolerance; the
# corrected rule gives 22.9%, inside it.
#
# The dandiset holds the 73 to 99 h EEG/EMG recordings of 17 rats (two 24-h baseline windows
# each), not the western blots, the development measures, the visual scoring or the pharmacology recordings. The files give 14
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -A4 "^- id:\|^  - id:" claims/001888/10.1111-epi.18606.yaml | grep -E "id:|statement" ; grep -n "statement:" -A3 claims/001888/10.1111-epi.18606.yaml | grep -E "fig6b|fig7c|fig4b|fig4c|ETX|ethosux|nRT|beta|wake power"
```

```
61:- id: fig2b-swd-hourly
62-  statement: Grin2b+/- rats have more SWDs than WT across the 24-h day; hour of day has no
71:- id: fig2c-swd-number
72-  statement: Grin2b+/- rats have more SWDs over 24 h than WT (Wilcoxon rank-sum, W = 4.5, p =
77:- id: fig2c-swd-mean-duration
78-  statement: SWDs are longer on average in Grin2b+/- rats than in WT (two-sample t test, df =
84:- id: fig2c-swd-total-duration
85-  statement: The total time in SWDs over 24 h is higher in Grin2b+/- rats than in WT (Wilcoxon
90:- id: disc-het-swd-minutes
91-  statement: Over 24 h, Grin2b+/- rats spend on average 59.97 min in SWDs, while WT littermates
102:- id: figs5a-swd-light-dark
103-  statement: The number of SWDs does not differ between the light and dark phases, and
112:- id: figs8-swd-sex
113-  statement: Sex does not affect the number, mean duration or total duration of SWDs (two-way
120:- id: fig2d-swd-spectrum-peak
121-  statement: The EEG spectrum during SWDs has a clear peak in the theta range with a harmonic,
130:- id: fig2e-swd-delta-power
131-  statement: Delta power during SWDs is higher in Grin2b+/- rats than in WT (two-way ANOVA
137:- id: fig3d-rem-hourly
138-  statement: Grin2b+/- rats have less REM sleep per hour than WT across the day, and the
[... 56 more lines not kept]
```

**Agent**

I've read all the sources. Next I'll write the subsection.

**Agent calls Bash**

```bash
cat >> docs/pilot-notes.md <<'EOF'

### 001888, Hristova et al. 2025

Thirteen claims reproduced, nine partially, two not reproduced and ten blocked
on the dandiset. Round 1 had no attempt record and gave its own outcome for
each claim from the notebook with its conclusion cells and summary removed, and
agreed with all 34. It found that reading (i) of `figs5b-transition-percent`
judged an SWD initiated in NREM on the one epoch before it, where the
Supplementary Methods use the six epochs before, and that rule gives 22.93%
against 24.2 ± 2.42. The author corrected the criterion, recording that this
was done after the analysis had been seen, and changed the outcome from not
reproduced to reproduced (the first rule gave 36.31%); the reason for blocking
`fig2e-swd-delta-power` and `fig5a-het-more-nrem-swds` went from `other` to
`data_missing`, as the verifier gave. Round 2 agreed with all 34, including the
change, and nothing was proposed, so there was no third round. The paper, in
Epilepsia, records EEG and EMG from Grin2b+/- and wild-type rats, and reports
that Grin2b+/- rats have more spike-wave discharges (SWDs), mostly in wake and
at wake-NREM transitions, less REM sleep in fewer and longer bouts, less time
awake, higher NREM beta power and lower wake power, and that ethosuximide given
systemically or into the reticular thalamic nucleus reduces SWDs. The number,
duration, timing, sex dependence and spectrum of SWDs, the amount and bouts of
each sleep state, the state spectra, the states in which SWDs start and the
correlations of SWD time with sleep measures were tested; the western blots,
development measures, scorer validation and the four pharmacology claims are
blocked as `data_missing`, and fig2e and fig5a-het-more-nrem-swds because only
one wild-type rat has SWDs. `fig4b-nrem-beta` (Het beta lower by 0.078) and
`fig4c-wake-power` (Het higher on average, +0.081) are not reproduced. Some
outcomes rest on weak ground: `fig3d-rem-hourly` and `fig3g-rem-total` give p
= 0.048 and drop to p = 0.060 without GRIN2B-228, a Grin2b+/- rat with 1 SWD
per day, without which `fig5c-transition-swds` (13 of 13, p = 0.0095) and
`fig5def-no-other-correlations` would meet their criteria; and the wake
results depend on whole SWD epochs being taken out of wake, so that with the
stored scores the wake bout differences reverse and `fig5f-swd-wake-correlation`
gives R = -0.06 in place of -0.81.

The dandiset was converted by CatalystNeuro
(catalystneuro/gonzalez-sulser-lab-to-nwb). It holds 2 of the paper's 9
analysed wild-type rats (14 or 15 of its 15 Grin2b+/-), so genotype comparisons
rest on two wild-type rats, one of which (GRIN2B-238) has no SWDs, and it does
not say which of its rats the paper analysed; GRIN2B-132 has no genotype and
sex U, which the conversion repository marks as still to be confirmed by the
lab. The pharmacology and intrathalamic infusion recordings, western blots,
development measures and the visual scoring used to validate the scorer are
not in it, and the paper says raw data are available on request. The
processed tables are misdescribed: the `sleep_states` description gives code 4
for SWD epochs, but no file holds it; `swd_epoch_counts` holds the scorer's
flags (6 for an SWD epoch, 4 otherwise) and not counts, and the flags cover a
median of 51% (0 to 73%) of the epochs SWD events overlap, mostly the last
epoch of each SWD; in `seizure_totals_by_zt` the per-hour counts are in
`spike_wave_discharge` while the two count columns hold the day's total in the
first row; and `sleep_state_power_spectra`, described as a baseline-corrected
PSD, holds the scorer's mean log10 multitaper amplitude referenced to each
frequency's 5th percentile. The raw EEG and EMG are stored as unsigned 12-bit
codes with offset 0, so every channel reads about +8 mV of DC, and signal loss
is written as 32767, undocumented; 21 to 73% of 5-s epochs per rat in the
windows read contain such samples (73% for GRIN2B-238). The Methods exclude SWD
times from the sleep states while the lab's scorer replaces only the flagged
epochs, and the paper's wake results depend on this. Other findings: the
dandiset has no published version, and the attempt pinned the draft as
modified 2026-07-31 09:37 UTC; the assets summary counts 16 files and 16
subjects where the draft holds 17; the dandiset does not record which EEG and
EMG channels the lab chose by eye for scoring; the paper does not give its
band limits, Welch segment length, bout definition or transition rule, and
neither linked repository holds the statistics or figure code; and the Figure
5 legend gives statistics that contradict each other (NREM time T = -1.47 with
R = -0.13 and df = 13, which implies T = -0.47), while the Figure 3 legend
reports no net wake difference next to a genotype effect on hourly wake time
(F = 7.14, p = 0.014).

The notebook ran in 278 s in the first clean run and 246 s after round 2. The
author first opened only GRIN2B-132 and took genotypes from the conversion
repository, then switched to the genotypes in the other 16 files and to SWD
epochs taken from the events before reading any claim output, though a first
run had executed the claim cells; a bug in the SWD peak rule was fixed before
the conclusions were written and changed fig2d's outcome. Round 1's points led
to runs without GRIN2B-228, GRIN2B-238 and both for every genotype test, a
fitted mixed model that matched the split-plot ANOVA, and checks of spectral
coverage, the slope rejection and a cleaner channel, none changing an outcome
beyond figs5b. Round 2 found statements the outputs did not support, among
them that the paper's 59.97 min of SWDs does not fit the scorer's flags, which
give 60.2 min, and a run time of about six minutes, and these were corrected.
The author's points on the protocol: no published version, where the protocol
allows a draft only for repeat attempts; opening one file, which is not enough
to find metadata held across all files; whether criteria may be revised after a
run that executed the claim cells; Methods and the lab's code that disagree on
SWD epochs, where the data show the code's input is incomplete; no minimum group
size for blocking a claim; claims of no difference tested with two wild-type
rats; one claim spanning eight tests under a binary absence rule; a variant
that matches but cannot rescue a claim; trading fidelity to the Methods'
spectra for speed; and method choices the paper leaves undefined.
EOF
git diff --stat
```

```
README.md           |  1 +
 docs/pilot-notes.md | 90 +++++++++++++++++++++++++++++++++++++++++++++++++++++
 2 files changed, 91 insertions(+)
```

**Agent**

I added the 001888 row to README.md and appended the subsection to `docs/pilot-notes.md`. Nothing is committed. The README row reads 13 reproduced, 9 partially, 2 not reproduced and 10 blocked. Here is the subsection:

### 001888, Hristova et al. 2025

Thirteen claims reproduced, nine partially, two not reproduced and ten blocked
on the dandiset. Round 1 had no attempt record and gave its own outcome for
each claim from the notebook with its conclusion cells and summary removed, and
agreed with all 34. It found that reading (i) of `figs5b-transition-percent`
judged an SWD initiated in NREM on the one epoch before it, where the
Supplementary Methods use the six epochs before, and that rule gives 22.93%
against 24.2 ± 2.42. The author corrected the criterion, recording that this
was done after the analysis had been seen, and changed the outcome from not
reproduced to reproduced (the first rule gave 36.31%); the reason for blocking
`fig2e-swd-delta-power` and `fig5a-het-more-nrem-swds` went from `other` to
`data_missing`, as the verifier gave. Round 2 agreed with all 34, including the
change, and nothing was proposed, so there was no third round. The paper, in
Epilepsia, records EEG and EMG from Grin2b+/- and wild-type rats, and reports
that Grin2b+/- rats have more spike-wave discharges (SWDs), mostly in wake and
at wake-NREM transitions, less REM sleep in fewer and longer bouts, less time
awake, higher NREM beta power and lower wake power, and that ethosuximide given
systemically or into the reticular thalamic nucleus reduces SWDs. The number,
duration, timing, sex dependence and spectrum of SWDs, the amount and bouts of
each sleep state, the state spectra, the states in which SWDs start and the
correlations of SWD time with sleep measures were tested; the western blots,
development measures, scorer validation and the four pharmacology claims are
blocked as `data_missing`, and fig2e and fig5a-het-more-nrem-swds because only
one wild-type rat has SWDs. `fig4b-nrem-beta` (Het beta lower by 0.078) and
`fig4c-wake-power` (Het higher on average, +0.081) are not reproduced. Some
outcomes rest on weak ground: `fig3d-rem-hourly` and `fig3g-rem-total` give p
= 0.048 and drop to p = 0.060 without GRIN2B-228, a Grin2b+/- rat with 1 SWD
per day, without which `fig5c-transition-swds` (13 of 13, p = 0.0095) and
`fig5def-no-other-correlations` would meet their criteria; and the wake
results depend on whole SWD epochs being taken out of wake, so that with the
stored scores the wake bout differences reverse and `fig5f-swd-wake-correlation`
gives R = -0.06 in place of -0.81.

The dandiset was converted by CatalystNeuro
(catalystneuro/gonzalez-sulser-lab-to-nwb). It holds 2 of the paper's 9
analysed wild-type rats (14 or 15 of its 15 Grin2b+/-), so genotype comparisons
rest on two wild-type rats, one of which (GRIN2B-238) has no SWDs, and it does
not say which of its rats the paper analysed; GRIN2B-132 has no genotype and
sex U, which the conversion repository marks as still to be confirmed by the
lab. The pharmacology and intrathalamic infusion recordings, western blots,
development measures and the visual scoring used to validate the scorer are
not in it, and the paper says raw data are available on request. The
processed tables are misdescribed: the `sleep_states` description gives code 4
for SWD epochs, but no file holds it; `swd_epoch_counts` holds the scorer's
flags (6 for an SWD epoch, 4 otherwise) and not counts, and the flags cover a
median of 51% (0 to 73%) of the epochs SWD events overlap, mostly the last
epoch of each SWD; in `seizure_totals_by_zt` the per-hour counts are in
`spike_wave_discharge` while the two count columns hold the day's total in the
first row; and `sleep_state_power_spectra`, described as a baseline-corrected
PSD, holds the scorer's mean log10 multitaper amplitude referenced to each
frequency's 5th percentile. The raw EEG and EMG are stored as unsigned 12-bit
codes with offset 0, so every channel reads about +8 mV of DC, and signal loss
is written as 32767, undocumented; 21 to 73% of 5-s epochs per rat in the
windows read contain such samples (73% for GRIN2B-238). The Methods exclude SWD
times from the sleep states while the lab's scorer replaces only the flagged
epochs, and the paper's wake results depend on this. Other findings: the
dandiset has no published version, and the attempt pinned the draft as
modified 2026-07-31 09:37 UTC; the assets summary counts 16 files and 16
subjects where the draft holds 17; the dandiset does not record which EEG and
EMG channels the lab chose by eye for scoring; the paper does not give its
band limits, Welch segment length, bout definition or transition rule, and
neither linked repository holds the statistics or figure code; and the Figure
5 legend gives statistics that contradict each other (NREM time T = -1.47 with
R = -0.13 and df = 13, which implies T = -0.47), while the Figure 3 legend
reports no net wake difference next to a genotype effect on hourly wake time
(F = 7.14, p = 0.014).

The notebook ran in 278 s in the first clean run and 246 s after round 2. The
author first opened only GRIN2B-132 and took genotypes from the conversion
repository, then switched to the genotypes in the other 16 files and to SWD
epochs taken from the events before reading any claim output, though a first
run had executed the claim cells; a bug in the SWD peak rule was fixed before
the conclusions were written and changed fig2d's outcome. Round 1's points led
to runs without GRIN2B-228, GRIN2B-238 and both for every genotype test, a
fitted mixed model that matched the split-plot ANOVA, and checks of spectral
coverage, the slope rejection and a cleaner channel, none changing an outcome
beyond figs5b. Round 2 found statements the outputs did not support, among
them that the paper's 59.97 min of SWDs does not fit the scorer's flags, which
give 60.2 min, and a run time of about six minutes, and these were corrected.
The author's points on the protocol: no published version, where the protocol
allows a draft only for repeat attempts; opening one file, which is not enough
to find metadata held across all files; whether criteria may be revised after a
run that executed the claim cells; Methods and the lab's code that disagree on
SWD epochs, where the data show the code's input is incomplete; no minimum group
size for blocking a claim; claims of no difference tested with two wild-type
rats; one claim spanning eight tests under a binary absence rule; a variant
that matches but cannot rescue a claim; trading fidelity to the Methods'
spectra for speed; and method choices the paper leaves undefined.

## End of run

17 turns, 1 minutes, result: success.
