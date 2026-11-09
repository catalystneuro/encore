# 001170 · recorder · run 39151680898

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
python tools/readme_row.py 001170 --write; git diff; ls claims/001170 transcripts/001170; grep -n '^### ' docs/pilot-notes.md | tail -6; wc -l docs/pilot-notes.md
```

```
diff --git a/README.md b/README.md
index 740fadd..0fffd8b 100644
--- a/README.md
+++ b/README.md
@@ -93,6 +93,7 @@ please [open an issue](https://github.com/catalystneuro/reproduction-registry/is
 | [001038](https://dandiarchive.org/dandiset/001038) | [Azcorra et al. 2023](https://doi.org/10.1038/s41593-023-01401-9) | 16 | 7 | 1 | 0 | [`001038-azcorra-2023`](entries/001038-azcorra-2023) |
 | [001075](https://dandiarchive.org/dandiset/001075) | [Randi et al. 2023](https://doi.org/10.1038/s41586-023-06683-4) | 4 | 4 (+1) | 0 (+1) | 7 | [`001075-randi-2023`](entries/001075-randi-2023) |
 | [001084](https://dandiarchive.org/dandiset/001084) | [Vu et al. 2024](https://doi.org/10.1016/j.neuron.2023.12.011) | 10 (+1) | 10 | 0 | 1 | [`001084-vu-2024`](entries/001084-vu-2024) |
+| [001170](https://dandiarchive.org/dandiset/001170) | [Ling et al. 2023](https://doi.org/10.1101/2023.04.24.538157) | 2 (+1) | 4 | 4 | 3 | [`001170-ling-2023`](entries/001170-ling-2023) |
 
 Counts are of claims that rest on the dandiset, including those that take
 names for its own codes from elsewhere. Claims that also use data from
claims/001170:
10.1101-2023.04.24.538157.yaml

transcripts/001170:
author-report.md
author-revise-1-report.md
author-revise-1.md
author-revise-2-report.md
[... 13 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/pilot-notes.md",
 "offset": 3039
}
```

```
3039	### 000947, Schwab et al. 2020
3040	
3041	Six claims reproduced, four partially, seven not reproduced and one blocked
3042	on the dandiset. With outside data, counted apart: one reproduced. Two claims
3043	on data in other archives are blocked. Round 1 gave its own outcome for each
3044	claim from the notebook with its conclusions removed and agreed with all 21 as
3045	they then stood, but found that the reaction-time test of `behavior-rt-mt` ran
3046	on all 250 pre-MPTP files with trials, including files with motor cortex, SMA
3047	or VLp units only; restricted to the 165 files with units of the dandiset
3048	rule, reaction times differ neither between the animals (p = 0.89) nor between
3049	directions (p = 0.41), and the author changed the claim from partially
3050	reproduced to reproduced. Round 2 agreed with all 21 and nothing was proposed,
3051	so there was no third round. The paper reports single units in GPi and VLa of
3052	two macaques (NHP G and NHP I) during reaching, compares the onset and sign of
3053	their peri-movement changes with what gating of thalamus by GPi predicts, and
3054	tests correlations between simultaneously recorded GPi and VLa units, the VLa
3055	rate after GPi bursts and pauses, and a model thalamocortical cell. The link
3056	to the paper's unit list, the unit counts, rest rates, spike widths,
3057	hold-period ramps, responsive fractions, response forms, integrated change,
3058	onset latencies, the gating conflict fraction, directional units, spike and
[... 464 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,95p README.md | grep -n -i -A3 'columns\|reproduced\|(+' | head -40
```

```
19:with the methods available to it. **A "not reproduced" or "partially
20:reproduced" outcome is not a finding that the paper is wrong.** It can come
21-from a mistake or a limitation in the agent's analysis, from methods the paper
22-does not describe fully, from data that is not in the dandiset, or from a
23-dandiset that differs from what the paper analysed. Most attempts here are
--
49:| Dandiset | Paper | Reproduced | Partially | Not reproduced | Blocked | Entry |
50-|---|---|---|---|---|---|---|
51-| [000582](https://dandiarchive.org/dandiset/000582) | [Sargolini et al. 2006](https://doi.org/10.1126/science.1125572) | 2 | 1 | 0 | 0 | [`000582-sargolini-2006`](entries/000582-sargolini-2006) |
52-| [000127](https://dandiarchive.org/dandiset/000127) | [Chowdhury et al. 2020](https://doi.org/10.7554/eLife.48198) | 4 | 2 | 0 | 4 | [`000127-chowdhury-2020`](entries/000127-chowdhury-2020) |
--
54:| [000147](https://dandiarchive.org/dandiset/000147) | [Guan et al. 2022](https://doi.org/10.7554/eLife.74478) | 9 (+3) | 0 | 1 | 4 (+3) | [`000147-guan-2022`](entries/000147-guan-2022) |
55-| [001097](https://dandiarchive.org/dandiset/001097) | [Liu et al. 2024](https://doi.org/10.1038/s41586-024-07916-w) | 7 | 2 | 3 | 12 | [`001097-liu-2024`](entries/001097-liu-2024) |
56-| [000625](https://dandiarchive.org/dandiset/000625) | [Geiller et al. 2020](https://doi.org/10.1016/j.neuron.2020.09.013) | 4 | 4 | 6 | 12 | [`000625-geiller-2020`](entries/000625-geiller-2020) |
57:| [000035](https://dandiarchive.org/dandiset/000035) | [Scala et al. 2021](https://doi.org/10.1038/s41586-020-2907-3) | 3 (+2) | 1 (+1) | 0 | 9 (+1) | [`000035-scala-2021`](entries/000035-scala-2021) |
58-| [001453](https://dandiarchive.org/dandiset/001453) | [Fouke et al. 2025](https://doi.org/10.1016/j.cub.2025.04.027) | 7 | 1 | 2 | 10 | [`001453-fouke-2025`](entries/001453-fouke-2025) |
59-| [000006](https://dandiarchive.org/dandiset/000006) | [Economo et al. 2018](https://doi.org/10.1038/s41586-018-0642-
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/001170-ling-2023-01.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'))
it=d if isinstance(d,list) else d.get('dandisets',d)
for e in (it if isinstance(it,list) else it.values()):
  if '001170' in json.dumps(e): print(json.dumps(e,indent=1))
"; wc -c claims/001170/* transcripts/001170/*report.md
```

```
<persisted-output>
Output too large (214.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/ac2a8141-2de2-4ca2-99a4-49d7e4e6add5/tool-results/by5zyw3v5.txt

Preview (first 2KB):
schema_version: 1
id: 001170-ling-2023-01
dandiset: "001170"
dandiset_version: 0.260528.1016
paper: doi:10.1101/2023.04.24.538157
date: 2026-10-18
entry: 001170-ling-2023
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
    protocol: pilot-7
inputs:
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
wc -c attempts/001170-ling-2023-01.yaml claims/001170/* transcripts/001170/*report.md; python -c "
import json;d=json.load(open('targets/dandisets.json'))
it=d if isinstance(d,list) else d.get('dandisets',d)
for e in (it if isinstance(it,list) else it.values()):
  if '001170' in json.dumps(e)[:300]: print(json.dumps(e,indent=1)[:3000])
"
```

```
42750 attempts/001170-ling-2023-01.yaml
20009 claims/001170/10.1101-2023.04.24.538157.yaml
 6925 transcripts/001170/author-report.md
 3589 transcripts/001170/author-revise-1-report.md
 2688 transcripts/001170/author-revise-2-report.md
10054 transcripts/001170/verifier-1-report.md
 5203 transcripts/001170/verifier-2-report.md
91218 total
```

**Agent calls Bash**

```bash
python -c "
import json;d=json.load(open('targets/dandisets.json'))
print(type(d)); 
s=json.dumps(d); i=s.find('001170'); print(s[i-200:i+1500])
"
```

```
<class 'dict'>
"JournalArticle", "preprint": false}], "catalystneuro": ["conversion code at https://github.com/catalystneuro/constantinople-lab-to-nwb", "contributor Weigl, Szonja of CatalystNeuro"]}, {"dandiset": "001170", "name": "Mesoscale Two-Photon Calcium Imaging of Population Level Odor Responses from the Mouse Olfactory Bulb", "published_version": "0.260528.1016", "asset_count": 12, "size_gb": 352.08, "data_standards": ["Neurodata Without Borders (NWB)"], "species": ["Mus musculus - House mouse"], "approaches": ["behavioral approach", "microscopy approach; cell population imaging"], "papers": [{"doi": "10.1101/2023.04.24.538157", "title": "Conserved neural dynamics and computations across species in olfaction", "relation": "IsDescribedBy", "resource_type": "Preprint", "preprint": true}], "catalystneuro": ["conversion code at https://github.com/catalystneuro/reimer-arenkiel-lab-to-nwb", "contributor Trapani, Alessandra of CatalystNeuro"]}, {"dandiset": "001172", "name": "Dual-color mesoscopic imaging of both ACh and calcium across the neocortex of awake mice.", "published_version": "0.260129.0829", "asset_count": 32, "size_gb": 700.01, "data_standards": ["Neurodata Without Borders (NWB)"], "species": ["Mus musculus - House mouse"], "approaches": ["microscopy approach; cell population imaging", "behavioral approach"], "papers": [{"doi": "10.1038/s41593-022-01202-6", "title": "Dual color mesoscopic imaging reveals spatiotemporally heterogeneous coordination of cholinergic and neocortical activity", "relation": "IsDescribedBy", "resource_type": "JournalArticle", "preprint": false}], "catalystneuro": ["conversion code at https://github.com/catalystneuro/higley-lab-to-nwb", "contribut
```

**Agent**

Read the README row; now reading the attempt record, claims and reports.

**Agent calls Read**

```json
{
 "file_path": "attempts/001170-ling-2023-01.yaml"
}
```

```
1	schema_version: 1
2	id: 001170-ling-2023-01
3	dandiset: "001170"
4	dandiset_version: 0.260528.1016
5	paper: doi:10.1101/2023.04.24.538157
6	date: 2026-10-18
7	entry: 001170-ling-2023
8	provenance:
9	  kind: agent
10	  accountable:
11	    name: CatalystNeuro
12	  agent:
13	    harness: Claude Code (GitHub Actions)
14	    model: claude-opus-5-5
15	    protocol: pilot-7
16	inputs:
17	- what: The paper's Figshare record (version 2), read for method choices (Script_Fig1.m to
18	    Script_Fig6.m, metaData.mat, medAngles.mat, wrtTheta.mat, contrastCorr.mat). The deposited mouse
19	    array data1_mouse_glom198.mat is used by the link claim only. The locust files
20	    data2_locust_PN66.mat, data4_locust_PN85.mat and data5_locust_PN85.mat are used by the locust
[... 653 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "transcripts/001170/author-report.md"
}
```

```
1	I've done steps 1 to 5 for dandiset 001170 and ran the step 6 handover. The entry passes `check` and runs from a clean environment, and the handover package is in `executed/001170-ling-2023/handover/`. Nothing is committed.
2	
3	Paper: I used the open-access full text of bioRxiv v2 (2024-02-23), saved under `paper/`. Two tables in it are images I couldn't fetch. The preprint was later published in iScience (2026) as "Conserved post-odor dynamics in the olfactory systems of mice and locusts"; the claims are the preprint's, since that is what the dandiset names. Pinned version: 0.260528.1016, the latest published. The paper cites no version, and the other published version holds identical assets.
4	
5	### 1. Outcome per claim
6	
7	| Claim | Data | Outcome |
8	|---|---|---|
9	| mouse-sessions (7 sessions, 4 mice, median 215 ROIs) | dandiset | reproduced (7, 4, 210) |
10	| figshare-trace-link | with_inputs | reproduced (within-trial r 0.968, same ROI order) |
11	| fig2h-onoff-angle-mouse | dandiset | partially (mean 127.9 against 121.8 ± 2.98; all 28 above 90°) |
12	| fig2f-onoff-anticorrelated-mouse | dandiset | not reproduced (median r +0.48, 0 of 28 negative) |
13	| fig4b-reference-odor-mouse | dandiset | partially (holds for ace only; als goes the other way) |
14	| fig4d-clustering-mouse | dandiset | not reproduced (0 of 7 sessions) |
15	| fig6e-contrast-msc | dandiset | not reproduced (p = 0.39) |
16	| fig6e-contrast-ace | dandiset | blocked: data_missing |
17	| fig7d-persistent-anticorrelation | dandiset | not reproduced (r positive in every bin) |
18	| fig7h-iti-knn-mouse | dandiset | partially (45%, above the null but below 50%) |
19	| fig7j-iti-timebin-mouse | dandiset | reproduced (72 to 89%); a control undercuts the odor-memory reading |
20	| figs7e-ibi-chance | dandiset | blocked: methods_underspecified |
[... 47 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "transcripts/001170/verifier-1-report.md"
}
```

```
1	**A. Outcomes** (19 claims, from the claims file; I had no attempt record, see C)
2	
3	| Claim | Outcome | Reason |
4	|---|---|---|
5	| mouse-sessions | reproduced | 7 block sessions, 4 mice, median 210 ROIs across the block sessions (215 ± 21.5) (cell 19). |
6	| figshare-trace-link | reproduced | Median within-trial r is 0.968 with windows counted in frames. All 198 deposited glomeruli match the same-index ROI (cell 21). With windows placed in seconds the median r is 0.307, so the paper's code counted frames. |
7	| fig2h-onoff-angle-mouse | partially_reproduced | All 28 values and every odor mean are above 90°, but the mean is 127.88°, outside 121.8 ± 2.98 (cell 25). The >90° result is mostly produced by the centring (problem 2). |
8	| fig2f-onoff-anticorrelated-mouse | not_reproduced | Median r is +0.481, with 0 of 28 values below 0. Every odor median is positive (cell 28). |
9	| fig4b-reference-odor-mouse | partially_reproduced | Reading (a) holds for ace only (p = 0.018, ON-ON smaller). For als the difference is significant in the opposite direction (ON-OFF 59.6° vs ON-ON 112.1°). Reading (b) holds in 0 of 28 cases (cell 30). |
10	| fig4d-clustering-mouse | not_reproduced | ON and OFF separate in 0 of 7 sessions, including the 198-ROI session. This holds with dF/F and with z-scored traces (cell 32). |
11	| fig6e-contrast-msc | not_reproduced | Solitary r 0.229 vs sequential r 0.219, one-tailed p = 0.39 over 21 pairs (cell 34). On the paper's own three sessions (see problem 6), cell 34's values give p = 0.082. |
12	| fig6e-contrast-ace | blocked: data_missing | In every block session each sequential block is X→msc (cell 10). The random-order sessions have no pairs 1 s apart, and the archive holds only these 12 files. Nothing is testable. |
13	| fig7d-persistent-anticorrelation | not_reproduced | The median r is positive in every bin from 0 to 50 s (0.48 down to 0.09), and positive with pre-block F0 too (cell 36). |
14	| fig7h-iti-knn-mouse | partially_reproduce
[... 42 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "transcripts/001170/author-revise-1-report.md"
}
```

```
1	No outcome changed in this round. I answered each point in the round-1 report, re-ran the entry (`tools/entry.py all` passes, 2.0 min), and recorded the round under `verifications`. The outputs match between the last two runs apart from timings, and the conclusions were checked against them.
2	
3	**Outcomes.** The verifier agreed with 18 of 19 claims. The one disagreement is figs7e-ibi-chance, which the verifier would call not reproduced. I kept it as blocked (methods underspecified) and recorded the disagreement. My reason is the protocol's chance-level rule: the procedure the Methods describe has a chance level of 10.8% under its own null, against the paper's 25%. The above-chance rates the verifier cites come from settings the paper does not use, and, as the verifier says, they may reflect slow drift. Each odor has only one inter-block interval per session, so a test that holds out a whole block cannot be run.
4	
5	**Fixed in the helper:** analysis windows that ran past the first or last imaging frame were filled by linear extrapolation. They are now left empty, and a new data-check cell shows no window falls outside the imaging span.
6	
7	**Added outputs the verifier asked for:**
8	- **ON-OFF angles (mouse fig2h, locust fig1g).** The centring in the paper's code pushes angles above 90° on its own. The two halves of a single ON window come out at about 101° (mouse) and 96° (locust), and a synthetic check shows the same. The conclusions now say the angles above 90° do not show that ON and OFF responses are inverted.
9	- **Normalisation (fig2f, fig6e, fig7d).**
10	  - With z-scores based only on the 2 s before odor onset, ON and OFF stay positively correlated (median r 0.53) and there is no contrast enhancement (p = 0.58).
11	  - On synthetic data, z-scoring each trial over its whole window turns pure excitation into negative correlations (r about −0.9).
12	  - Counting windows in frames, as the paper's code does, gives the same conclusions.
13	- **Classifiers in
[... 15 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "transcripts/001170/verifier-2-report.md"
}
```

```
1	**1. Outcomes**
2	
3	The claims file has 19 claims. The attempt record gives 6 reproduced, 6 partially reproduced, 4 not reproduced and 3 blocked.
4	
5	- **18 outcomes:** I agree with these, the same as in round 1. For fig7j-iti-timebin-mouse and fig7f-iti-knn-locust, "reproduced" holds on the criterion only, and the record and notebook now say so.
6	- **figs7e-ibi-chance:** the record has blocked (methods_underspecified); my round-1 outcome was not_reproduced. I now accept blocked.
7	  - With the Methods' k = 50, the procedure's own null averages 10.8% (cell 57), so the 3.8% cannot count as meeting the criterion. The paper's 34.8% cannot come from the procedure its Methods describe.
8	  - My not_reproduced rested on k = 20, which the criterion does not specify.
9	  - Every working variant gives 35% to 98% (k = 20, 10, 5), well above 34.8%. If a working method were ever fixed, the outcome would be not_reproduced.
10	
11	**2. Statements the printed outputs do not support**
12	
13	- **Whole-window z-score and fig2f.** Three statements say the ON/OFF anticorrelation appears when traces are z-scored over each trial window:
14	  - README: "With traces z-scored within each trial window … they appear as the paper reports".
15	  - Summary (cell 79), first bullet: "The mouse ON/OFF anticorrelation (fig2f, fig7d) and the contrast enhancement (fig6e) appear with that z-scoring".
16	  - The record's first metadata_insufficient finding: "the paper's ON/OFF anticorrelation … appear[s] … with that normalisation".
17	
18	  Cell 34 prints r_zscored median +0.068, 12 of 28 below 0, p = 0.33, and the odor medians are mixed. Only fig7d from 5 s on (cell 47) and fig6e (cell 44) show the effect with that z-score.
19	- **Window drift.** Summary (cell 79), third bullet: frame counting "drifts by up to about 2 s over a 57-s trial at the sessions' 13.7 to 17.8 Hz". Using the frame rates in cell 4, 912 frames last 66.4 s at 13.73 Hz and 51.2 s at 17.83 Hz, so the drift is 6 to 9 s at the ex
[... 26 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "transcripts/001170/author-revise-2-report.md"
}
```

```
1	No outcomes changed. The round-2 verifier agreed with all 19, including figs7e-ibi-chance, which it now accepts as blocked (methods underspecified). That leaves 6 reproduced, 6 partially reproduced, 4 not reproduced and 3 blocked. Nothing went under `proposed`.
2	
3	I re-ran `python tools/entry.py all entries/001170-ling-2023` and it passed (183 s), as did `tools/entry.py check`. The numbers are the same as before, and the corrected text matches the new outputs.
4	
5	**What I corrected, one item per point in the report:**
6	- **fig2f and the whole-window z-score:** the README, the Summary and the first `metadata_insufficient` finding said the ON/OFF anticorrelation appears with that z-score. They now say only the fig6e contrast and the fig7d negative correlations from 5 s on appear with it. The time-averaged ON and OFF vectors are not anticorrelated with any normalisation tried (median r 0.068, 12 of 28 below 0).
7	- **Window drift:** the Summary said up to about 2 s. It now says 912 frames last 51.2 to 66.4 s, a drift of 6 to 9 s at the extremes and about 1.8 s in sub-141 ses-8. The `code_mismatch` finding gives the same range.
8	- **"Only because of the centring":** the README now limits this to the mouse (uncentred mean 71.8). It gives the locust figure without centring, after subtracting the pre-odor baseline: 91.9, with 9 of 11 odors above 90. The Summary says the same.
9	- **fig7h null mean:** corrected from 17.1% to 16.7% in the cell 51 conclusion and in the notes.
10	- **fig7j block-relabelling null:** I removed it from the code (cell 53), from the cell 55 conclusion and from the notes, and dropped the `itertools` import it alone used. The text now says why no permutation that keeps whole blocks can serve as a null.
11	- **fig7j pseudo-trials:** these now read "nearly as high as" the ITIs, "within the 15 min after each block". I checked against the new outputs that the pseudo-trial maximum is below the ITI minimum in 4 of 7 sessions.
12	- **fig7d synthetic
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
head -60 claims/001170/*.yaml; grep -n 'data:\|^- id\|  id:' claims/001170/*.yaml
```

```
# Claims for Ling, Moss, Smith, Deng, Kroeger, Reimer, Raman & Arenkiel, "Conserved neural
# dynamics and computations across species in olfaction", bioRxiv doi:10.1101/2023.04.24.538157.
# Source: the full text of version 2 of the preprint (2024-02-23, CC BY-ND), read from its JATS
# XML; its Results, figure legends and Methods. Table S1 and the key resources table are images
# that could not be fetched, so the list of datasets per figure was not read. The paper was later
# published as "Conserved post-odor dynamics in the olfactory systems of mice and locusts"
# (iScience 2026, doi:10.1016/j.isci.2026.115373); the claims are those of the preprint, which
# the dandiset names.
#
# When these criteria were written, the author had seen the data check only: the file list and
# metadata of both published versions, the trials tables (odors, concentrations, timing, block
# structure), ROI counts, frame counts and frame rates of every file, and the conversion code.
# The author had also read the paper's MATLAB code on Figshare (doi:10.6084/m9.figshare.31435543.v2,
# Script_Fig1.m to Script_Fig6.m) and the small summary files it holds (medAngles.mat,
# wrtTheta.mat, contrastCorr.mat). One comparison had been run while preparing, the one the
# figshare-trace-link claim states: the raw traces of sub-141 ses-8 against the deposited array
# data1_mouse_glom198.mat, which gave a median within-trial r of about 0.97 when the windows are
# counted in frames as the code does, and about 0.4 when they are placed in seconds. No claim's
# analysis on the paper's findings had been run.
#
[... 66 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> docs/pilot-notes.md <<'EOF'

### 001170, Ling et al. 2023

Two claims reproduced, four partially, four not reproduced and three blocked
on the dandiset. With outside data, counted apart: one reproduced. Five claims
on the locust recordings in the paper's Figshare record: three reproduced and
two partially reproduced. Round 1 gave its own outcome for each claim from the
notebook with its conclusions removed and agreed with 18 of the 19; it would
call `figs7e-ibi-chance` not reproduced, as the Methods' k = 50 classifier on
60 one-minute bins gives 3.8% and meets the criterion by construction while
k = 20 classifies the gaps between blocks at 73 to 95%. The author kept it
blocked as `methods_underspecified` under the chance-level rule, since that
procedure's own null averages 10.8% against the paper's 25%, and round 2
accepted this. Round 2 agreed with all 19 and nothing was proposed, so there
was no third round. The paper, a bioRxiv preprint later published in iScience
under a new title, compares mouse olfactory bulb glomeruli imaged with two
photons and locust recordings, and reports that ON and OFF responses point in
opposite directions and are anticorrelated, that the anticorrelation persists
after offset, that a preceding odor enhances contrast, and that the odor can
be decoded from activity in the intervals between trials. The session counts,
the link to the paper's deposited array, the ON-OFF angles, correlations,
reference-odor comparisons and clustering, the contrast of pairs ending in
methyl salicylate, the persistence after offset, the classifiers on the
intervals between trials and between blocks, and the random-order sessions
were tested on the dandiset. The acetophenone contrast panel and the
photoionization detector recordings of Figure S2 are blocked as
`data_missing`. Some outcomes rest on weak ground: `fig7j-iti-timebin-mouse`
and `fig7f-iti-knn-locust` are reproduced on the criterion only, as all trials
of one odor lie in one block, and in the mouse pseudo-trials within the 15 min
after each block, where no odor is given, are classified by the preceding
block at 69.6% to 96.9%, nearly as high as the intervals between trials; the
ON-OFF angles above 90 degrees of `fig2h-onoff-angle-mouse` and
`fig1g-onoff-angle-locust` follow from the code's centring, which makes the
mean ON and OFF vectors opposite (the two halves of one ON window come out at
101.1 and 96.0 degrees), and uncentred the mouse mean is 71.8; and in
`fig7h-iti-knn-mouse` k = 20 leaves only 9 of 39 other trials of the own odor,
so the null mean is 16.7%, while k = 5 gives 90.0%. The author used the full
text of preprint v2, whose Table S1 is an image and was not read, took the
session assignments from Table 1 of the published version (PMC13066794), and
took method choices from the paper's code on Figshare
(doi:10.6084/m9.figshare.31435543.v2) and the conversion code at commit
ac8f120.

The dandiset was converted by CatalystNeuro
(catalystneuro/reimer-arenkiel-lab-to-nwb). The fluorescence traces are raw F
(unit "n.a.") with no description of how they were extracted or of the
normalisation the paper applied, and the paper's deposited arrays are close to
F z-scored within each 57-s trial window. With that normalisation the contrast
enhancement and the negative correlations between the ON response and
activity from 5 s after offset appear, and they do not with dF/F relative to
the 2 s before each odor or with F z-scored on those 2 s; on synthetic
glomeruli with excitation only the whole-window z-score gives such
anticorrelations by itself, and the time-averaged ON and OFF vectors are not
anticorrelated with any normalisation tried (median r 0.068, 12 of 28 below
0). No sequential pair ends in acetophenone and no PID recordings are
included; the published version's Table 1 assigns the acetophenone panel to
the 73-, 210-, 153- and 198-glomerulus sessions, which in the dandiset hold
only pairs ending in methyl salicylate. The random-order session of Figure S8D
and S8E (286 glomeruli) is not in the dandiset, and of the eight random-order
sessions Table 1 lists only two (323 and 306) match a dandiset session by ROI
count. The dandiset holds the paper's seven block-protocol sessions from four
mice and five random-order sessions from five mice (four not in the block
sessions), apparently from a second study whose conference paper it also
names, and neither the metadata nor the description, which is that of the
second study, says which sessions belong to which paper. No identifier links
the paper's datasets to the sessions; they match by ROI count (198, 219, 318),
and session names in the paper's code (m149_3_1, m129_1_2) do not all exist in
the dandiset. The trials table has one undescribed row per second of valve
opening, so presentations, blocks and pairs have to be rebuilt from timing;
five block sessions fill the gaps with "Empty" rows and two do not, and the
concentration column has no unit, gives 0.0 to two odorants in three
random-order sessions and 0.1 to the Empty rows of sub-141 ses-5. In sub-134
ses-22, sub-141 ses-5 and sub-141 ses-8 the raw TwoPhotonSeries holds half the
frames of the fluorescence traces (91000 against 182000 in sub-134 ses-22) at
twice the frame interval. Other findings: the dandiset puts the 318-ROI
session under sub-148 with the 286-ROI session, while Table 1 puts it under
mouse 4 with the 219-glomerulus session; the files have 2-ethylphenol and
anisaldehyde where the Methods list 2-ethylpyrizine and isoamyl acetate,
"Anisole" and "anisole" are both used, and "2-methypyrazine" is misspelled;
the genotype (Thy1-GCaMP6f) and ages are not stated, every session starts at
00:00, and in sub-124 ses-3 the last trial ends 8.9 s after the last imaging
frame; the paper's code counts windows in frames at a nominal 16 per second
while the sessions are imaged at 13.7 to 17.8 Hz, so a nominal 57-s window
lasts 51.2 to 66.4 s, and in sub-141 ses-8 the deposited trial windows match
the dandiset only when counted in frames (r 0.968, against 0.307 in seconds);
the Methods give k = 50 for the classifier of Figure 7H, which has 40 vectors,
while the legend and code use k = 20; and the Figure 5E legend states a
one-tailed t-test where the code's is two-tailed (p = 0.011 against 0.0055).

The notebook ran in about 2.5 minutes in the first clean run,
`tools/entry.py all` took 2.0 minutes after round 1 and 183 s after round 2.
Figshare returned HTTP 500 to rapid downloads, handled with retries and md5
checks, and bioRxiv refused the preprint download to the round-1 verifier,
which read the published version. Round 1 also found that analysis windows
past the last frame were filled by linear extrapolation, which the author
fixed. Round 2 found statements the outputs did not support, among them that
the ON/OFF anticorrelation appears with the whole-window z-score, a window
drift of up to about 2 s, and a block-relabelling null for fig7j that repeats
the observed accuracy by construction, and these were corrected or removed.
Untracked files in the repository root that the author did not create were
left alone. The author's points on the protocol: a preprint later published
under a new title, with nothing saying which version is the target; code and
data in a Figshare record that neither the preprint nor the dandiset links; a
standalone link claim with no dependent claims; data from another species and
lab that the dandiset was never expected to hold; a criterion that passes
against the chance-level rule; no place for arrays the paper deposited as a
source for method choices; no rule for disclosing variants added after seeing
results; an SEM as tolerance, which becomes very tight; a 10% tolerance that
cannot apply to a count of 5; a clock check by shifted labels in a block
design; and a criterion that passes where the reading fails.
EOF
grep -c '—' docs/pilot-notes.md; tail -110 docs/pilot-notes.md | grep -n -i 'rather\|—'; git status --short
```

```
0
 M README.md
 M docs/pilot-notes.md
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
?? scripts
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes.md",
 "old_string": "so the null mean is 16.7%, while k = 5 gives 90.0%.",
 "new_string": "so the null mean is 16.7%, while k = 5 gives 90.0% in sub-148 ses-3."
}
```

```
The file docs/pilot-notes.md has been updated successfully. (note: the file had been modified on disk since you last read it — the edit applied cleanly, but the file contains other changes not in your context. Read it before edits that depend on surrounding content.)
```

**Agent**

I ran `tools/readme_row.py 001170 --write`, which added this row to README.md: 2 (+1) reproduced, 4 partially, 4 not reproduced, 3 blocked. I added the subsection below at the end of docs/pilot-notes.md and checked it for em dashes and "rather". Nothing is committed. The untracked dotfiles and `scripts` folder in the repository root were already there, and I left them alone.

### 001170, Ling et al. 2023

Two claims reproduced, four partially, four not reproduced and three blocked
on the dandiset. With outside data, counted apart: one reproduced. Five claims
on the locust recordings in the paper's Figshare record: three reproduced and
two partially reproduced. Round 1 gave its own outcome for each claim from the
notebook with its conclusions removed and agreed with 18 of the 19; it would
call `figs7e-ibi-chance` not reproduced, as the Methods' k = 50 classifier on
60 one-minute bins gives 3.8% and meets the criterion by construction while
k = 20 classifies the gaps between blocks at 73 to 95%. The author kept it
blocked as `methods_underspecified` under the chance-level rule, since that
procedure's own null averages 10.8% against the paper's 25%, and round 2
accepted this. Round 2 agreed with all 19 and nothing was proposed, so there
was no third round. The paper, a bioRxiv preprint later published in iScience
under a new title, compares mouse olfactory bulb glomeruli imaged with two
photons and locust recordings, and reports that ON and OFF responses point in
opposite directions and are anticorrelated, that the anticorrelation persists
after offset, that a preceding odor enhances contrast, and that the odor can
be decoded from activity in the intervals between trials. The session counts,
the link to the paper's deposited array, the ON-OFF angles, correlations,
reference-odor comparisons and clustering, the contrast of pairs ending in
methyl salicylate, the persistence after offset, the classifiers on the
intervals between trials and between blocks, and the random-order sessions
were tested on the dandiset. The acetophenone contrast panel and the
photoionization detector recordings of Figure S2 are blocked as
`data_missing`. Some outcomes rest on weak ground: `fig7j-iti-timebin-mouse`
and `fig7f-iti-knn-locust` are reproduced on the criterion only, as all trials
of one odor lie in one block, and in the mouse pseudo-trials within the 15 min
after each block, where no odor is given, are classified by the preceding
block at 69.6% to 96.9%, nearly as high as the intervals between trials; the
ON-OFF angles above 90 degrees of `fig2h-onoff-angle-mouse` and
`fig1g-onoff-angle-locust` follow from the code's centring, which makes the
mean ON and OFF vectors opposite (the two halves of one ON window come out at
101.1 and 96.0 degrees), and uncentred the mouse mean is 71.8; and in
`fig7h-iti-knn-mouse` k = 20 leaves only 9 of 39 other trials of the own odor,
so the null mean is 16.7%, while k = 5 gives 90.0% in sub-148 ses-3. The author used the full
text of preprint v2, whose Table S1 is an image and was not read, took the
session assignments from Table 1 of the published version (PMC13066794), and
took method choices from the paper's code on Figshare
(doi:10.6084/m9.figshare.31435543.v2) and the conversion code at commit
ac8f120.

The dandiset was converted by CatalystNeuro
(catalystneuro/reimer-arenkiel-lab-to-nwb). The fluorescence traces are raw F
(unit "n.a.") with no description of how they were extracted or of the
normalisation the paper applied, and the paper's deposited arrays are close to
F z-scored within each 57-s trial window. With that normalisation the contrast
enhancement and the negative correlations between the ON response and
activity from 5 s after offset appear, and they do not with dF/F relative to
the 2 s before each odor or with F z-scored on those 2 s; on synthetic
glomeruli with excitation only the whole-window z-score gives such
anticorrelations by itself, and the time-averaged ON and OFF vectors are not
anticorrelated with any normalisation tried (median r 0.068, 12 of 28 below
0). No sequential pair ends in acetophenone and no PID recordings are
included; the published version's Table 1 assigns the acetophenone panel to
the 73-, 210-, 153- and 198-glomerulus sessions, which in the dandiset hold
only pairs ending in methyl salicylate. The random-order session of Figure S8D
and S8E (286 glomeruli) is not in the dandiset, and of the eight random-order
sessions Table 1 lists only two (323 and 306) match a dandiset session by ROI
count. The dandiset holds the paper's seven block-protocol sessions from four
mice and five random-order sessions from five mice (four not in the block
sessions), apparently from a second study whose conference paper it also
names, and neither the metadata nor the description, which is that of the
second study, says which sessions belong to which paper. No identifier links
the paper's datasets to the sessions; they match by ROI count (198, 219, 318),
and session names in the paper's code (m149_3_1, m129_1_2) do not all exist in
the dandiset. The trials table has one undescribed row per second of valve
opening, so presentations, blocks and pairs have to be rebuilt from timing;
five block sessions fill the gaps with "Empty" rows and two do not, and the
concentration column has no unit, gives 0.0 to two odorants in three
random-order sessions and 0.1 to the Empty rows of sub-141 ses-5. In sub-134
ses-22, sub-141 ses-5 and sub-141 ses-8 the raw TwoPhotonSeries holds half the
frames of the fluorescence traces (91000 against 182000 in sub-134 ses-22) at
twice the frame interval. Other findings: the dandiset puts the 318-ROI
session under sub-148 with the 286-ROI session, while Table 1 puts it under
mouse 4 with the 219-glomerulus session; the files have 2-ethylphenol and
anisaldehyde where the Methods list 2-ethylpyrizine and isoamyl acetate,
"Anisole" and "anisole" are both used, and "2-methypyrazine" is misspelled;
the genotype (Thy1-GCaMP6f) and ages are not stated, every session starts at
00:00, and in sub-124 ses-3 the last trial ends 8.9 s after the last imaging
frame; the paper's code counts windows in frames at a nominal 16 per second
while the sessions are imaged at 13.7 to 17.8 Hz, so a nominal 57-s window
lasts 51.2 to 66.4 s, and in sub-141 ses-8 the deposited trial windows match
the dandiset only when counted in frames (r 0.968, against 0.307 in seconds);
the Methods give k = 50 for the classifier of Figure 7H, which has 40 vectors,
while the legend and code use k = 20; and the Figure 5E legend states a
one-tailed t-test where the code's is two-tailed (p = 0.011 against 0.0055).

The notebook ran in about 2.5 minutes in the first clean run,
`tools/entry.py all` took 2.0 minutes after round 1 and 183 s after round 2.
Figshare returned HTTP 500 to rapid downloads, handled with retries and md5
checks, and bioRxiv refused the preprint download to the round-1 verifier,
which read the published version. Round 1 also found that analysis windows
past the last frame were filled by linear extrapolation, which the author
fixed. Round 2 found statements the outputs did not support, among them that
the ON/OFF anticorrelation appears with the whole-window z-score, a window
drift of up to about 2 s, and a block-relabelling null for fig7j that repeats
the observed accuracy by construction, and these were corrected or removed.
Untracked files in the repository root that the author did not create were
left alone. The author's points on the protocol: a preprint later published
under a new title, with nothing saying which version is the target; code and
data in a Figshare record that neither the preprint nor the dandiset links; a
standalone link claim with no dependent claims; data from another species and
lab that the dandiset was never expected to hold; a criterion that passes
against the chance-level rule; no place for arrays the paper deposited as a
source for method choices; no rule for disclosing variants added after seeing
results; an SEM as tolerance, which becomes very tight; a 10% tolerance that
cannot apply to a count of 5; a clock check by shifted labels in a block
design; and a criterion that passes where the reading fails.

## End of run

16 turns, 1 minutes, result: success.
