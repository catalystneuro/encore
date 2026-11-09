# 000959 · verifier-2 · run 41264267467

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 452
drwxr-xr-x 6 runner runner    4096 Nov  1 02:27 .
drwxr-xr-x 7 runner runner    4096 Nov  1 02:27 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  1 02:10 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  1 02:10 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov  1 02:27 .claude
-rw-r--r-- 1 runner runner       0 Nov  1 02:27 .env
-rw-r--r-- 1 runner runner       0 Nov  1 02:27 .env.development
-rw-r--r-- 1 runner runner       0 Nov  1 02:27 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov  1 02:27 .env.local
-rw-r--r-- 1 runner runner       0 Nov  1 02:27 .env.production
-rw-r--r-- 1 runner runner       0 Nov  1 02:27 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov  1 02:27 .env.test
-rw-r--r-- 1 runner runner       0 Nov  1 02:27 .env.test.local
drwx------ 2 runner runner    4096 Nov  1 02:27 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  1 02:10 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  1 02:10 .github
-rw-r--r-- 1 runner runner       0 Nov  1 02:27 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  1 02:10 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  1 02:10 .mcp.json
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; cat 000959-fan-2024-01.yaml
```

```
<persisted-output>
Output too large (49.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/7b8098f8-46a9-46d3-98e7-b0dcf685dc62/tool-results/b0qkh8vpe.txt

Preview (first 2KB):
# Fan, Dal Monte, Nair, Fagan & Chang (2024) from dandiset 000959

Tests the findings of [Fan et al. (2024)](https://doi.org/10.1016/j.neuron.2024.05.004) on
[DANDI:000959](https://dandiarchive.org/dandiset/000959/0.261020.0242). The dandiset holds one file
per 300-s run for every day of the paper: 81 Eyes stimulation days (OFC, dmPFC and ACCg; 15 per area
from monkey L, 12 from monkey T) and 15 Mouth stimulation days of monkey T. Each file has the gaze and
pupil of both monkeys at 1 kHz, the stimulation and sham times, the day's ROIs and the fixation events.

| Claim | Outcome |
|---|---|
| Days per area, runs per day | Reproduced; partially reproduced (monkey L has 6.0 control runs per day, not 5) |
| Stimulation and sham counts comparable across areas and monkeys (social, control) | Reproduced |
| More fixations on the Eyes than on the non-eye Face | Reproduced |
| Eyes fixations comparable to RDM fixations | Not reproduced under the Methods' day total; comparable under the code's mean per run (asked of a reader) |
| OFC density map more clustered around the partner | Reproduced |
| OFC lowers social gaze distance, not dmPFC or ACCg; stronger contralaterally; none in the control condition; longer windows | Reproduced |
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'E'
import json
nb=json.load(open('reproduce_fan_2024.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(f"===== CELL {i} [{c['cell_type']}]")
    if c['cell_type']=='markdown': print(src)
    else:
        print(src[:3000] + ('\n...[src truncated]' if len(src)>3000 else ''))
        for o in c.get('outputs',[]):
            t=o.get('text') or o.get('data',{}).get('text/plain','')
            t=''.join(t)
            print('--- OUT:'); print(t[:6000])
E
```

```
<persisted-output>
Output too large (122KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/7b8098f8-46a9-46d3-98e7-b0dcf685dc62/tool-results/bg5qivypv.txt

Preview (first 2KB):
===== CELL 0 [markdown]
# Reproducing Fan et al. (2024) from dandiset 000959

**Paper.** Fan, Dal Monte, Nair, Fagan & Chang (2024), "Closed-loop microstimulations of the
orbitofrontal cortex during real-life gaze interaction enhance dynamic social attention",
Neuron 112, 2631-2644, doi:10.1016/j.neuron.2024.05.004.

**Claims.** `claims/000959/10.1016-j.neuron.2024.05.004.yaml`, written from the accepted author
manuscript (PMC11309918) with its supplement, and the paper's code
(github.com/changlabneuro/microstim-ofc-social-attention at cc0bf994).

**Dataset.** DANDI:000959, version 0.261020.0242. The paper cites the dandiset without a
version. Two versions are published, 0.260531.2104 and 0.261020.0242; the most recent is pinned,
as the protocol asks when the paper cites none. The data check below compares the two asset
lists: both hold the same 1705 assets with the same identifiers, paths and sizes, so the choice
does not change the data.
[... 19 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/7b8098f8-46a9-46d3-98e7-b0dcf685dc62/tool-results/b0qkh8vpe.txt"
}
```

```
1	# Fan, Dal Monte, Nair, Fagan & Chang (2024) from dandiset 000959
2	
3	Tests the findings of [Fan et al. (2024)](https://doi.org/10.1016/j.neuron.2024.05.004) on
4	[DANDI:000959](https://dandiarchive.org/dandiset/000959/0.261020.0242). The dandiset holds one file
5	per 300-s run for every day of the paper: 81 Eyes stimulation days (OFC, dmPFC and ACCg; 15 per area
6	from monkey L, 12 from monkey T) and 15 Mouth stimulation days of monkey T. Each file has the gaze and
7	pupil of both monkeys at 1 kHz, the stimulation and sham times, the day's ROIs and the fixation events.
8	
9	| Claim | Outcome |
10	|---|---|
11	| Days per area, runs per day | Reproduced; partially reproduced (monkey L has 6.0 control runs per day, not 5) |
12	| Stimulation and sham counts comparable across areas and monkeys (social, control) | Reproduced |
13	| More fixations on the Eyes than on the non-eye Face | Reproduced |
14	| Eyes fixations comparable to RDM fixations | Not reproduced under the Methods' day total; comparable under the code's mean per run (asked of a reader) |
15	| OFC density map more clustered around the partner | Reproduced |
16	| OFC lowers social gaze distance, not dmPFC or ACCg; stronger contralaterally; none in the control condition; longer windows | Reproduced |
17	| No change in fixation number; longer whole Face looking after OFC stimulation | Reproduced; partially reproduced (tests hold, values in part) |
18	| No effect of Mouth stimulation | Reproduced (5 days per area cannot reach p < 0.05) |
19	| Eyes against Mouth bootstrap | Not reproduced |
20	| Inter-looking interval and reciprocation latency (day and trial level, 41% and 86%) | Reproduced |
[... 794 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/7b8098f8-46a9-46d3-98e7-b0dcf685dc62/tool-results/bg5qivypv.txt"
}
```

```
1	===== CELL 0 [markdown]
2	# Reproducing Fan et al. (2024) from dandiset 000959
3	
4	**Paper.** Fan, Dal Monte, Nair, Fagan & Chang (2024), "Closed-loop microstimulations of the
5	orbitofrontal cortex during real-life gaze interaction enhance dynamic social attention",
6	Neuron 112, 2631-2644, doi:10.1016/j.neuron.2024.05.004.
7	
8	**Claims.** `claims/000959/10.1016-j.neuron.2024.05.004.yaml`, written from the accepted author
9	manuscript (PMC11309918) with its supplement, and the paper's code
10	(github.com/changlabneuro/microstim-ofc-social-attention at cc0bf994).
11	
12	**Dataset.** DANDI:000959, version 0.261020.0242. The paper cites the dandiset without a
13	version. Two versions are published, 0.260531.2104 and 0.261020.0242; the most recent is pinned,
14	as the protocol asks when the paper cites none. The data check below compares the two asset
15	lists: both hold the same 1705 assets with the same identifiers, paths and sizes, so the choice
16	does not change the data.
17	
18	Each file is one 300-s run (a "session" in the paper) and holds M1's gaze and pupil at 1 kHz,
19	M2's gaze and pupil in social runs, the stimulation and sham times, the day's ROIs, and
20	fixation events as interval tables (M1-only, M2-only and mutual events by ROI). Files are read
[... 756 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/7b8098f8-46a9-46d3-98e7-b0dcf685dc62/tool-results/bg5qivypv.txt",
 "offset": 777,
 "limit": 700
}
```

```
777	region subject  n  median_diff  mean_diff      p  median_diff_deg
778	 dmPFC    both 27       -6.042     -5.587 0.2901          -0.2377
779	 dmPFC       L 15       -6.728     -10.19 0.2078          -0.2648
780	 dmPFC       T 12       -1.273     0.1655      1         -0.05011
781	  ACCg    both 27       -3.908     -4.089 0.2901          -0.1538
782	  ACCg       L 15        -5.52     -12.23  0.073          -0.2172
783	  ACCg       T 12        3.172      6.081 0.7334           0.1248
784	
785	===== CELL 34 [markdown]
786	**Result: reproduced.** dmPFC gives p = 0.21 and ACCg p = 0.39 (paper 0.361 and 0.374); the code's reading gives 0.29 and 0.29.
787	===== CELL 35 [markdown]
788	## fig2e-ofc-contralateral and fig2e-dmpfc-accg-no-hemifield-effect
789	
790	> The OFC effect on social gaze distance was stronger for fixations in the hemifield
791	> contralateral to the stimulated hemisphere; it was significant for contralateral fixations,
792	> not for ipsilateral ones, and the contralateral effect exceeded the ipsilateral one.
793	
794	> For dmPFC and ACCg there was no stimulation effect on social gaze distance in either
795	> hemifield, and no difference between hemifields.
796	===== CELL 36 [code]
[... 680 more lines not kept]
```

**Agent**

Through cell 86 the printed numbers support the conclusions, apart from one small mismatch in the record (dmPFC density sum −0.0026 there, −0.0027 printed). Reading the rest.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/7b8098f8-46a9-46d3-98e7-b0dcf685dc62/tool-results/bg5qivypv.txt",
 "offset": 1476,
 "limit": 600
}
```

```
1476	 M2 reciprocation latency (a)    OFC    both 27      0.06506    0.01443  0.5619
1477	 M2 reciprocation latency (a)  dmPFC    both 27       0.1144     0.1287 0.04356
1478	 M2 reciprocation latency (a)   ACCg    both 27     -0.02447    0.01002  0.9906
1479	 M2 reciprocation latency (b)    OFC    both 27       0.1052    0.09665  0.4553
1480	 M2 reciprocation latency (b)  dmPFC    both 27       -0.141     0.0258  0.9529
1481	 M2 reciprocation latency (b)   ACCg    both 27     0.006837    0.03378  0.9153
1482	trials with a value: {'ili2a': 2104, 'ili2b': 2104, 'rec2a': 2798, 'rec2b': 2797} of 19474
1483	tests with p < 0.05: [{'measure': 'M2 reciprocation latency (a)', 'region': 'dmPFC', 'p': 0.04355788230895996}]
1484	
1485	===== CELL 87 [markdown]
1486	**Result: partially reproduced.** M2's social gaze distance (OFC p = 0.12, dmPFC 0.47, ACCg 0.062; paper 0.118, 0.302 and 0.064) and M2's inter-looking interval under both readings (smallest p 0.19) do not change. M2's reciprocation latency does not change under reading (b) (smallest p 0.46), but under reading (a), from the start of the M1 look, dmPFC gives p = 0.044 (median 0.11 s longer after stimulation). The criterion asks that no test give p < 0.05 under every reading; 1 of the 21 tests does.
1487	===== CELL 88 [markdown]
1488	## epoch-days-76-of-81
1489	
1490	> 76 of the 81 days had at least 90 microstimulations and entered the epoch analysis; the five
1491	> excluded were 1 OFC day of monkey L and, of monkey T, 1 OFC, 2 dmPFC and 1 ACCg day.
1492	===== CELL 89 [code]
1493	allsoc = trials[(trials.cond == "Social") & (trials.roi == "Eyes")]
1494	ns = pd.DataFrame({
1495	    "a_kept": allsoc[allsoc.kept & (allsoc.type == "stim")].groupby("date").size(),
[... 576 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "assumed" 000959-fan-2024-01.yaml | head; echo ---; grep -n "^- id:\|^  - id:\|id: " 10.1016-j.neuron.2024.05.004.yaml | head -50; grep -n -i "xlabel\|ipsi <-\|contra <-" reproduce_fan_2024.ipynb | head
```

```
---
78:  id: "000959"
81:- id: design-days-per-area
102:- id: design-sessions-per-day
131:- id: fig1e-stim-counts-comparable
152:- id: figs1d-stim-counts-nonsocial
164:- id: figs1e-eyes-more-than-face
188:- id: figs1e-eyes-vs-rdm-comparable
204:- id: fig2a-density-map-ofc
224:- id: fig2c-ofc-social-gaze-distance
257:- id: fig2c-dmpfc-accg-no-distance-effect
275:- id: fig2e-ofc-contralateral
323:- id: fig2e-dmpfc-accg-no-hemifield-effect
354:- id: fig2f-nonsocial-no-distance-effect
376:- id: fig2gh-nonsocial-no-hemifield-effect
419:- id: methods-ofc-distance-longer-windows
448:- id: methods-ofc-no-change-in-fixation-number
488:- id: methods-ofc-longer-face-looking
549:- id: methods-mouth-stimulation-no-effect
593:- id: methods-eyes-vs-mouth-bootstrap
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import yaml
r=yaml.safe_load(open('000959-fan-2024-01.yaml'));c=yaml.safe_load(open('10.1016-j.neuron.2024.05.004.yaml'))
ids=[x['id'] for x in c['claims']] if 'claims' in c else None
print(len(ids), len(r['outcomes']), set(ids)^{o['claim'] for o in r['outcomes']})
from collections import Counter; print(Counter(o['outcome'] for o in r['outcomes']))
print(len(r['verifications'][0]['results']))
"; sed -n 1,80p 10.1016-j.neuron.2024.05.004.yaml
```

```
36 36 set()
Counter({'reproduced': 23, 'blocked': 6, 'partially_reproduced': 5, 'not_reproduced': 2})
36
# Claims for Fan, Dal Monte, Nair, Fagan & Chang (2024) on dandiset 000959.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read: the accepted author manuscript in PubMed Central (PMC11309918, NIHMS1994226),
# main text, figure legends and STAR Methods, with its one supplement
# (NIHMS1994226-supplement-1.pdf, Table S1 and the legends of Figures S1 to S4). The version of
# record (Neuron 112(15) 2631-2644.e6) was not read. The Results point to "Supplementary
# Results" for the Mouth stimulation experiments and the post-gaze window; the supplement holds
# no such section, and these results are given in the STAR Methods of the manuscript
# ("Gaze distance analyses" and "Gaze distance analyses (Mouth stimulation)"), which were read.
#
# Code read: github.com/changlabneuro/microstim-ofc-social-attention, commit cc0bf994 (2024-10-15),
# the analysis code named in Data and code availability (also Zenodo doi:10.5281/zenodo.11110139).
# It holds MATLAB scripts for every analysis of the paper ("Scripts for social attention":
# Get data, Overall gaze behavior and number of stims, Heatmap, Spatial dimension, Temporal
# dimension, Inter-individual dynamics, Saccade kinematics) and older scripts (stim/, script/).
[... 63 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 188,204p 10.1016-j.neuron.2024.05.004.yaml; echo ....; sed -n 488,549p 10.1016-j.neuron.2024.05.004.yaml; echo ....; sed -n 794,900p 10.1016-j.neuron.2024.05.004.yaml; echo ....; sed -n 1046,1200p 10.1016-j.neuron.2024.05.004.yaml
```

```
- id: figs1e-eyes-vs-rdm-comparable
  statement: The number of fixations on the partner's Eyes per day was comparable to the number of
    fixations on the RDM stimulus, for days of all three areas.
  source: Results, opening section, paragraph 2; Figure S1E
  quote: the total number of fixations on partner's Eyes per day was comparable to fixations on the
    RDM stimulus for days involving the three stimulated regions (Fig. S1E, top, all p > 0.30)
  statistics:
  - test: Wilcoxon signed rank, two-sided
    p: 0.3
    p_relation: ">"
    corrected: FDR
  criterion: A claim of absence, judged on the paper's test. Per day, M1 fixations in the Eyes ROI
    in social sessions against fixations in the RDM ROI in control sessions, paired by day,
    two-sided signed-rank test per area, FDR-corrected as in figs1e-eyes-more-than-face, under
    the same two readings of the day count. Reproduced when no corrected p is below 0.05 under
    the paper's reading (a); reading (b) is shown as the code's variant.
- id: fig2a-density-map-ofc
....
- id: methods-ofc-longer-face-looking
  statement: With OFC microstimulations the stimulated monkey spent more time looking within the
[... 290 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "def \|filter\|smooth\|validat\|MATLAB" microstim.py | head -80
```

```
22:  (claims file, opening comment). Indices in the files are 1-based (MATLAB); this module
64:def list_assets(version: str = DANDISET_VERSION) -> pd.DataFrame:
76:def file_layout(asset_id: str) -> dict:
87:def _dec(x):
91:def _table(f, name):
96:def _centre(r):
100:def _in_rect(xy, r):
106:def read_run(asset_id: str, session: requests.Session | None = None) -> dict:
184:                warnings.simplefilter("ignore", RuntimeWarning)
215:def load_all(assets: pd.DataFrame, workers: int = 16) -> list[dict]:
227:def tables(runs: list[dict]):
246:def day_rois(runs: list[dict]) -> dict:
255:def add_hemifield(events: pd.DataFrame, droi: dict) -> pd.DataFrame:
265:def window_pairs(trials: pd.DataFrame, events: pd.DataFrame, t0: float, t1: float) -> pd.DataFrame:
288:def roi_centre(droi: dict, date: str, name: str) -> np.ndarray:
292:def day_means(trial_values: pd.DataFrame, value: str, by=("date",)) -> pd.DataFrame:
299:def in_rect(xy, r):
303:def run_centres(runs: list[dict]) -> pd.DataFrame:
323:def prepare(runs: list[dict]):
336:def m1_fixations(events: pd.DataFrame, reading: str = "methods") -> pd.DataFrame:
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i "otero\|microsaccade\|macrosaccade" paper/*.txt | head -20
```

Result: not kept, because it reads the paper's text.

**Agent**

# Verifier report, round 2: Fan et al. 2024 (DANDI:000959, version 0.261020.0242)

The claims file holds 36 claims, and the attempt record gives 36 outcomes: 23 reproduced, 5 partially reproduced, 2 not reproduced and 6 blocked. **Correction to my round-1 report:** its headline counts were wrong. My own table there gives 22 reproduced, 4 partially reproduced, 2 not reproduced and 8 blocked, not 23 and 7.

## 1. Outcomes and assumptions

**Outcomes I agree with.** I agree with 34 of the 36 outcomes as recorded:
- **Unchanged since round 1 (33):** these keep the outcome and the reasons I gave then.
- **fig5a-trigger-duration-unchanged:** now partially reproduced, the outcome I gave in round 1. Cell 95 holds it up: OFC p = 0.61 and 0.36; dmPFC p = 0.019 and 0.028, and 0.020 in the variant.

**The six causal-decomposition claims (blocked, too_large): I agree.** Cell 92 now times the decomposition directly. At the claims file's reading (a), 1,000 ensembles:
- One EEMD takes 13.1 s on one core, which is 209 CPU s per trial.
- The smallest subset any of the six claims needs, the 2,250 OFC epoch trials, costs 130.7 CPU hours, or 55 hours of wall time on four processes.
- The spline floor for any implementation is 12 CPU hours for that subset.

Reading (a) alone is enough to block the claims, so how reading (b)'s settings are chosen does not matter here.

**The two saccade claims: I agree with them as computed, but they rest on an assumption that is not stated.** fig5cd-saccade-counts-unchanged is partially reproduced: cell 101 gives 1 of 4 tests failing under reading (a), OFC macrosaccades p = 0.044. fig5e-h-saccade-kinematics-unchanged is reproduced: cell 105 gives 0 of 14 failing under (a). The problem is the detector:
- **Its output is not physiological.** Cell 101: median saccade duration 147 ms, 95th percentile 1,062 ms, median amplitude 13.7°, 386 saccades per run. Cell 102: gaze velocity inside fixations has a median of 19.7 deg/s and is under the 5 deg/s limit for only 5.4% of samples.
- **The micro/macro labels may not mean much.** The record says itself that many detected "saccades" span several fixations.
- **The outcome depends on the labelling.** Reading (b) gives 0 of 4 and 3 of 14 failing tests, against 1 of 4 and 0 of 14 under (a).
- **The port was never checked against the MATLAB code** on any sample (`microstim.py` has no such check).

Both outcomes depend on this detection standing in fairly for the paper's, including that the paper did not filter the gaze first. No outcome is marked `assumed: true`. These two should be, with the assumption stated. It is not clearly reasonable given the notebook's own diagnostics.

**Other unstated choices.** No other outcome carries `assumed: true`. The remaining choices are recorded as deviations, and I find them reasonable:
- fig5a: the offline Eyes event in progress stands in for the trigger.
- Causal-decomposition reading (b): the example's settings, 0.35 noise and 1,000 ensembles.

## 2. Statements the printed numbers do not support

**Cells 92 and 93 against the attempt record (affects the blocked notes).** The causal-decomposition figures in the record were not updated after the re-run:

| Quantity | Record (figs4a notes and response) | Cell 92 |
|---|---|---|
| One EEMD, one core | 18.3 s | 13.1 s |
| One EEMD, four processes | 9.2 s | 5.5 s |
| CPU time per trial | 293 s | 209 s |
| Every social trial | about 1,590 CPU hours (about 790 hours of wall time) | 1,131.6 CPU hours (475.8 hours of wall time) |

The same holds for the epoch subsets:
- **The record** (ofc-slope, fig4c, fig4d and dmpfc-slope-positive, and the responses) says "2,250 trials ... about 183 CPU hours (92 hours of wall time) ... ACCg about 191".
- **Cell 92** prints 130.7 CPU hours (55.0 hours of wall time) for OFC and dmPFC, and 136.0 for ACCg.

The outcome stands, but every one of these figures is wrong.

**Cell 27 against the record (fig2a notes).** The record has "dmPFC (whole Face -2.46 and -0.0026)". Cell 27 prints −2.5599 and −0.0027, and cell 28's text agrees with cell 27.

**Cells 86 and 87, and the record (partner-monkey-unchanged).** The text says "1 of the 21 tests does". Cell 86 prints 18 tests: 6 distance tests, then 3 each for interval (a), interval (b), latency (a) and latency (b).

**Cell 90.** It says the five excluded days are "the days the paper names". The paper gives only their composition. The dates come from the code, as cell 89 and the record say.

**Cell 107, the Summary.** "6% of the M1 Eyes events have a mean position outside the Eyes rectangle" is true only of social runs. Cell 3 gives 6.3% for social runs and 10.7% for Dot runs, about 8% over both. The record's finding states both figures correctly.

**Cell 93.** "would still exceed it for every subset" compares CPU hours with a wall-time limit. 12 CPU hours spread over enough cores would fit in an hour. At four processes it does not, so the conclusion holds, but the sentence should say so.

**Minor.** In the figs1d notes, monkey T's control trials per day are 71 to 77 (cell 16), not 71 to 76.

**Everything else matches.** Every other "**Result:**" sentence, the rest of the Summary, the entry README and the other notes and findings agree with the printed outputs.

**My round-1 reasons in the record.** The record states them faithfully and in substance in my own words. Some entries fold my B points into the reason, which is acceptable. For both saccade claims my blocked reason was "other". The record keeps the outcome, blocked, and quotes my objection to not_runnable, which the author disputes. I cannot check that against the protocol here.

## 3. Round-1 points

**Resolved:**
- **B2:** both saccade claims are now tested with the outside detector.
- **B3:** the cost is now timed directly and per subset; too_large is shown. Only the stale figures in the record remain (section 2).
- **B4:** the bootstrap is run under the code's reading too; still not reproduced.
- **B6:** the trials with no Eyes event are broken down and spread evenly; the dmPFC result holds in the variant.
- **B7:** the axis label is corrected.
- **B8:** the ROI squares are the intersection over each day's runs; the recalibrated days are dmPFC and ACCg days.
- **B12:** times run up to 9,955 s, below the 10⁶ s offset.
- **B13:** the tie rule is recorded as a standard choice.

**Resolved as far as my round-1 questions go:**
- The mutual tables are shown (cell 3).
- The control-run listing is added (cell 10).
- The groups of one file are printed (cell 3). That file is a Dot run, so the absence of saccade tables is shown only for one control file, not for a social one.

**Acknowledged, nothing more needed:** B9, B10 and B11.

**Still open, bearing on a conclusion:**
1. **figs1e-eyes-vs-rdm-comparable (B1).** It is not reproduced only because of the claims file's deciding reading (a), which I still take to misread the paper. That is referred to a reader and is pending.
2. **fig3b-ofc-inter-looking-interval (B5).** p = 0.044 becomes 0.058 when the 91 events that start on the trial sample are counted. The question is put to the paper's authors; the outcome stays fragile.
3. **Saccade claims (new).** Both outcomes rest on a detector whose output, by the notebook's own diagnostics, is not physiological. The port is unvalidated, and the outcome changes with the micro/macro labelling. This assumption should be marked and stated (section 1).
4. **Causal-decomposition figures in the record (new).** They do not match cell 92. The outcome is not affected, but the notes and responses need correcting.
5. **partner-monkey-unchanged test count (new).** "1 of 21 tests" should read "1 of 18" in cell 87 and in the record. The outcome is not affected.

## End of run

13 turns, 2 minutes, result: success.
