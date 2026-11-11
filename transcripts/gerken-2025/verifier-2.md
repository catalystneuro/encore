# 001616 · verifier-2 · run 38670659680

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; wc -c *
```

```
Exit code 1
total 336
drwxr-xr-x 5 runner runner    4096 Oct 15 03:20 .
drwxr-xr-x 7 runner runner    4096 Oct 15 03:20 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 15 02:21 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 15 02:21 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 15 03:20 .claude
-rw-r--r-- 1 runner runner       0 Oct 15 03:20 .env
-rw-r--r-- 1 runner runner       0 Oct 15 03:20 .env.development
-rw-r--r-- 1 runner runner       0 Oct 15 03:20 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 15 03:20 .env.local
-rw-r--r-- 1 runner runner       0 Oct 15 03:20 .env.production
-rw-r--r-- 1 runner runner       0 Oct 15 03:20 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 15 03:20 .env.test
-rw-r--r-- 1 runner runner       0 Oct 15 03:20 .env.test.local
drwx------ 2 runner runner    4096 Oct 15 03:20 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 15 02:21 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 15 02:21 .github
-rw-r--r-- 1 runner runner       0 Oct 15 03:20 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 15 02:21 .idea
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat round-1-report.md; echo ======; cat README.md
```

```
A. Outcomes by claim

The claims file holds 20 claims. 16 have a criterion, and 4 (the last four) do not.

| Claim | Outcome | Reason |
|---|---|---|
| dataset-composition | partially_reproduced | Cell 5 gives 29 patients, 2286 units, 17 female and 30 to 137 units per patient, all exact. A (559) and H (846) are within tolerance. EC 493 (allowed 396–484), PHC 293 (336–410) and PIC 68 (89–109) are outside it. |
| fig2b-phc-camera-cuts | blocked (methods_underspecified) | The test as specified flags 72.35% of PHC units (68.33% of all units) at random event times (cell 18, cell 20), so the 75.77% for camera cuts says nothing. The calibrated ZETA variant gives 12.63% / 22.18% against 51.74% (cell 21). With this test Summer comes out at 44% of units where the paper has 2%, so the paper must have used a different, unknown implementation. |
| tables1-camera-cuts-regions | blocked (methods_underspecified) | Same test. A 73.7%, EC 74.0% and H 64.4% (cell 23) are no higher than the 62–73% each region shows at random times (cell 18). |
| fig2b-phc-scene-cuts | blocked (methods_underspecified) | 47.44% at alpha 0.001 against 6.70%, from an uncalibrated test (cell 25). The ZETA variant gives 2.73% / 10.24%, outside 4.16–9.24% at both alphas. The cluster p (1.000, or 0.048 with per-trial z-scoring) rests on the same split. |
| tables1-few-semantic-responses | blocked (methods_underspecified) | Summer 1017 and Tom 1168 against 46 and 216 (cell 27). Camera cuts at 70.7% sit at the random-time level of 68.3%, so the contrast cannot be judged. |
| tables1-no-indoor-response | blocked (methods_underspecified) | 279 units at 0.001 (cell 29). This is literally not_reproduced, but a test that flags 68% of units at random times can neither support nor refute an absence claim. |
| results-cluster-regions | blocked (methods_underspecified) | Only 9/32 and 13/32 cells agree (cell 31), but the responsive/non-responsive split is uninformative. For camera cuts, 548 of the 669 "non-responsive" un
[... 80 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat 10.7554-elife.106758.1.yaml
```

```
# Claims for Gerken, Darcher et al., "Decoding movie content from neuronal population activity in
# the human medial temporal lobe", eLife reviewed preprint 106758 version 1, on dandiset 001616.
# Source: the full text of the reviewed preprint (open access, from the eLife API) and its
# supplementary file 598791_file03.pdf (Tables S1 and S2).
#
# When these criteria were written, the author had seen the data check only: the file list and
# metadata of both published versions, the contents of every file, the units per patient and per
# brain region, the subjects' sex and age, the annotations and watchlogs, and the label counts.
# While timing the logistic regression on one fold for the label Summer, the author also saw that
# fold's validation and test kappa (validation 0.26 to 0.30, test 0.42 to 0.48 over four values
# of C). No other claim's analysis had been run. The author had read the dataset's code (GitHub
# mormannlab/SUMMER at commit 59fc242), including the values its plotting notebooks hold for the
# LSTM results by region and by gap size.
#
# Method choices fixed here, where the Methods leave them open:
# - Time base. Spikes (milliseconds, recording clock) are mapped to movie time through the cleaned
#   watchlog of each patient; spikes during pauses (repeated presentation timestamps) are dropped.
# - Responsive neurons (Methods, after Mormann et al. 2008). Pseudo-trials are label onsets in the
#   movie annotations preceded by at least 1000 ms without the label; for labels with a duration
#   (not camera or scene cuts) the label must also last at least 1000 ms (Results). Baseline is
[... 316 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat 001616-gerken-2025-01.yaml
```

```
<persisted-output>
Output too large (31.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/c7608a42-95db-4612-a885-19d0ee76a667/tool-results/b88a7zyc1.txt

Preview (first 2KB):
schema_version: 1
id: 001616-gerken-2025-01
dandiset: '001616'
dandiset_version: 0.260702.0824
paper: doi:10.7554/elife.106758.1
date: '2026-10-14'
entry: 001616-gerken-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
    protocol: pilot-6
inputs:
[... 35 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/c7608a42-95db-4612-a885-19d0ee76a667/tool-results/b88a7zyc1.txt"
}
```

```
1	schema_version: 1
2	id: 001616-gerken-2025-01
3	dandiset: '001616'
4	dandiset_version: 0.260702.0824
5	paper: doi:10.7554/elife.106758.1
6	date: '2026-10-14'
7	entry: 001616-gerken-2025
8	provenance:
9	  kind: agent
10	  accountable:
11	    name: CatalystNeuro
12	  agent:
13	    harness: Claude Code (GitHub Actions)
14	    model: claude-opus-5-5
15	    protocol: pilot-6
16	inputs:
17	- what: Method choices read from the dataset's code (the fold layout and table of repeated parts per gap,
18	    the grouping of hippocampal subregions, the onset rule and the ZETA test for responsive units), and
19	    the LSTM results per gap and per region its plotting notebooks hold, printed for comparison only.
20	  source: https://github.com/mormannlab/SUMMER at commit 59fc2424615150481494edf3e31d707729d395ea
[... 493 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/dump.py <<'EOF'
import json,sys
nb=json.load(open(sys.argv[1]))
for i,c in enumerate(nb['cells']):
    print(f"\n######## CELL {i} [{c['cell_type']}]")
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--- out:'); print(''.join(o['text']))
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--- out:'); print(''.join(d['text/plain']))
            else: print('--- out: [', list(d.keys()), ']')
        elif o.get('output_type')=='error': print('--- ERROR', o['ename'], o['evalue'])
EOF
for f in *.ipynb; do python3 $TMPDIR/dump.py $f > $TMPDIR/${f%.ipynb}.txt; wc -l $TMPDIR/${f%.ipynb}.txt; done
```

```
1770 /tmp/claude-1001/reproduce_gerken_2025.txt
235 /tmp/claude-1001/responsive_zeta_cuts.txt
196 /tmp/claude-1001/responsive_zeta_labels.txt
195 /tmp/claude-1001/top_ranked_units.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/reproduce_gerken_2025.txt"
}
```

```
1	
2	######## CELL 0 [markdown]
3	# Reproducing Gerken, Darcher et al. (2025) from dandiset 001616
4	
5	Paper: Gerken F, Darcher A, Gonçalves PJ, Rapp R, Elezi I, Niediek J, Kehl MS, Reber TP, Liebe S,
6	Macke JH, Mormann F, Leal-Taixé L (2025). Decoding movie content from neuronal population activity in
7	the human medial temporal lobe. eLife reviewed preprint 106758, version 1.
8	[doi:10.7554/eLife.106758.1](https://doi.org/10.7554/eLife.106758.1). This attempt used the full
9	text, which is open access, and the supplementary file with Tables S1 and S2.
10	
11	Dandiset: [DANDI:001616](https://dandiarchive.org/dandiset/001616/0.260702.0824), version
12	0.260702.0824 (SUMMER). The paper cites no DANDI version; its data statement says the data will be
13	published separately. This is the most recent published version. The earlier published version,
14	0.260519.1133, holds the same 29 files (same blobs) and 28 older copies of the same recordings with
15	identical spike times (shown in the data check), so the analysis would read the same data from
16	either; the pinned version holds each recording once.
17	
18	Code read: the dataset's repository [mormannlab/SUMMER](https://github.com/mormannlab/SUMMER) at
19	commit 59fc242 (Zenodo 10.5281/zenodo.21165561 archives it). It holds the NWB conversion, the
20	responsive-unit and cluster code behind Figure 2, plotting notebooks that hold the paper's LSTM
[... 802 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/reproduce_gerken_2025.txt",
 "offset": 822,
 "limit": 500
}
```

```
822	Its false-positive rate is far from its alpha, so the procedure here is not the one that produced
823	the paper's counts, and the claim cannot be judged. The ZETA test of the dataset's code
824	(`responsive_zeta_cuts.ipynb`) is calibrated (none of 400 units at random times at alpha 0.001,
825	1.0% at 0.01); it finds 35 of 293 PHC units (11.95%) responsive at 0.001 and 67 (22.87%) at 0.01,
826	well below the paper's 51.74%, so the paper's count does not come from that test as run here either.
827	
828	######## CELL 23 [markdown]
829	## tables1-camera-cuts-regions
830	
831	> Camera cuts evoked responses in a large share of neurons in every region (amygdala 46.90%,
832	> entorhinal cortex 45.68%, hippocampus 38.92%).
833	
834	######## CELL 24 [code]
835	paper_cc = {"A": 46.90, "EC": 45.68, "H": 38.92, "PHC": 51.74}
836	rows = []
837	for region in ("A", "EC", "H", "PHC", "PIC", "other"):
838	    idx = units.index[units.region == region]
839	    for alpha in summer.ALPHAS:
840	        n = int((P.loc[idx, "Camera Cuts"] <= alpha).sum())
841	        rows.append({"region": region, "alpha": alpha, "units": len(idx), "responsive": n,
[... 480 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/reproduce_gerken_2025.txt",
 "offset": 1322,
 "limit": 460
}
```

```
1322	
1323	
1324	######## CELL 50 [markdown]
1325	**Result: reproduced.** With samples assigned to training, validation and test at random, the
1326	logistic regression decodes Summer with kappa 0.948 (5 draws, 0.942 to 0.953). With gaps of 4, 8, 16
1327	and 32 s it gives 0.555, 0.524, 0.451 and 0.301, close to the LSTM values the dataset's code holds
1328	for the same gaps (0.987 random, then 0.584, 0.539, 0.429 and 0.309).
1329	
1330	######## CELL 51 [markdown]
1331	## fig4-patients-below-pooled
1332	
1333	> Decoding from a single patient's neurons is lower than from the pooled population; no patient
1334	> matches the pooled performance, for Summer, Scene Cuts or Indoor/Outdoor.
1335	
1336	######## CELL 52 [code]
1337	rng_pat = np.random.default_rng(33)
1338	started = time.time()
1339	PAT_LABELS = ("Summer", "Scene Cuts", "Indoor/Outdoor")
1340	Yp = {k: Y[k] for k in PAT_LABELS} | {"Summer shifted 300 s": shifted}
1341	pats = sorted(units.patient.unique())
[... 430 more lines not kept]
```

**Agent calls Bash**

```bash
cat /tmp/claude-1001/responsive_zeta_cuts.txt
```

```
######## CELL 0 [markdown]
# Responsive units by the ZETA test of the dataset's code: camera cuts and scene cuts

Paper: Gerken, Darcher et al. (2025), eLife reviewed preprint 106758 v1,
[doi:10.7554/eLife.106758.1](https://doi.org/10.7554/eLife.106758.1), full text and Table S1.
Dandiset: [DANDI:001616](https://dandiarchive.org/dandiset/001616/0.260702.0824), version 0.260702.0824.

The main notebook (`reproduce_gerken_2025.ipynb`) tests the responsive-unit claims with the test the
Methods describe (Wilcoxon signed-rank on 19 bins, Simes), finds it far from calibrated on this
data, and blocks those claims. The dataset's code ([mormannlab/SUMMER](https://github.com/mormannlab/SUMMER)
at commit 59fc242, `calc_responsive_units.py`) uses the ZETA test (zetapy) in its place. This notebook
runs that test for every unit and camera cuts and scene cuts, to show whether the counts of Table S1 could come from it;
`responsive_zeta_labels.ipynb` does the same for the character, person and location labels. It is a variant and decides no outcome.

As in the code: spike times and onsets on the recording clock (patient-aligned annotations),
onsets preceded by at least 1 s without the label, a window of 1 s after the onset. The code uses
1000 resamplings; here 100, for time. Chance is checked with the same test at random event times,
as many as the label's onsets, for 400 random units. The notebook takes about 22 minutes.

######## CELL 1 [code]
[... 213 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,400p /tmp/claude-1001/responsive_zeta_labels.txt | grep -v "^import\|^from"
```

```
######## CELL 0 [markdown]
# Responsive units by the ZETA test of the dataset's code: the character, person and location labels

Paper: Gerken, Darcher et al. (2025), eLife reviewed preprint 106758 v1,
[doi:10.7554/eLife.106758.1](https://doi.org/10.7554/eLife.106758.1), full text and Table S1.
Dandiset: [DANDI:001616](https://dandiarchive.org/dandiset/001616/0.260702.0824), version 0.260702.0824.

The main notebook (`reproduce_gerken_2025.ipynb`) tests the responsive-unit claims with the test the
Methods describe (Wilcoxon signed-rank on 19 bins, Simes), finds it far from calibrated on this
data, and blocks those claims. The dataset's code ([mormannlab/SUMMER](https://github.com/mormannlab/SUMMER)
at commit 59fc242, `calc_responsive_units.py`) uses the ZETA test (zetapy) in its place. This notebook
runs that test for every unit and the character, person and location labels, to show whether the counts of Table S1 could come from it;
`responsive_zeta_cuts.ipynb` does the same for camera and scene cuts. It is a variant and decides no outcome.

As in the code: spike times and onsets on the recording clock (patient-aligned annotations),
onsets preceded by at least 1 s without the label, a window of 1 s after the onset. The code uses
1000 resamplings; here 100, for time. Chance is checked with the same test at random event times,
as many as the label's onsets, for 800 random units. The notebook takes about 14 minutes.

######## CELL 1 [code]
[... 165 more lines not kept]
```

**Agent calls Bash**

```bash
grep -v "^import\|^from" /tmp/claude-1001/top_ranked_units.txt
```

```
######## CELL 0 [markdown]
# Top-ranked units (Gerken, Darcher et al. 2025, dandiset 001616)

Paper: Gerken, Darcher et al. (2025), eLife reviewed preprint 106758 v1,
[doi:10.7554/eLife.106758.1](https://doi.org/10.7554/eLife.106758.1), full text.
Dandiset: [DANDI:001616](https://dandiarchive.org/dandiset/001616/0.260702.0824), version 0.260702.0824.

Companion to `reproduce_gerken_2025.ipynb`, with the same loading, samples, folds and logistic
regression (`summer.py`). It holds two claims:

| Claim | Status |
|---|---|
| fig7b-top500-overlap | tested |
| fig7a-500-neurons | tested, with the logistic regression in place of the LSTM |

The notebook takes about 9 minutes.

######## CELL 1 [code]
for var in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(var, "1")
[... 168 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "def onsets" -A22 summer.py; grep -n "def sample_windows" -A25 summer.py; grep -n "1.8\|l1_ratio\|sklearn" summer.py
```

```
222:def onsets(annotations: pd.DataFrame, label: str, value: int, min_absence: float = 1.0,
223-           min_presence: float | None = 1.0) -> np.ndarray:
224-    """Onsets of a feature preceded by at least `min_absence` (s) without it and, if
225-    `min_presence` is given, lasting at least that long. Times as in `annotations`."""
226-    a = annotations[(annotations.label == label) & (annotations.value == value)].sort_values("start")
227-    start, stop = a.start.to_numpy(), a.stop.to_numpy()
228-    keep = start - min_absence > np.r_[-np.inf, stop[:-1]]
229-    if min_presence is not None:
230-        keep &= (stop - start) >= min_presence
231-    return start[keep]
232-
233-
234-# --- responsive units (Methods) ----------------------------------------------------------------
235-
236-def _counts_in(t: np.ndarray, starts: np.ndarray, width: float) -> np.ndarray:
237-    return np.searchsorted(t, starts + width, side="left") - np.searchsorted(t, starts, side="left")
238-
239-
240-def wilcoxon_simes(spikes_s: np.ndarray, events_s: np.ndarray) -> tuple[float, float]:
241-    """Simes-combined p of 19 overlapping 100 ms bins (0 to 1000 ms) against the baseline rate
[... 33 more lines not kept]
```

**Agent**

**Round 2 verification: Gerken, Darcher et al. 2025 on DANDI 001616 (0.260702.0824)**

The claims file has 20 claims and the attempt record has 20 outcomes:
- reproduced: 6
- partially_reproduced: 5
- blocked (methods_underspecified): 9

**1. Do I agree with each stated outcome?**

I agree with all 20.
- **dataset-composition (partially_reproduced):** Agree. Cell 5 gives 29 patients, 2286 units and 17 female patients, all exact. EC 493, PHC 293 and PIC 68 fall outside their tolerances.
- **The six responsive-unit claims (blocked):** Agree. These are fig2b-phc-camera-cuts, tables1-camera-cuts-regions, fig2b-phc-scene-cuts, tables1-few-semantic-responses, tables1-no-indoor-response and results-cluster-regions. Cell 18 now shows the null rate at each label's own number of onsets. The observed counts sit at that rate: Summer 44.31% observed against 44.05% at random times, Tom 51.36% against 50.26%, scene cuts 49.04% against 48.25%.
- **fig3b, fig3c-logreg-characters-location, fig3c-logreg-cuts-lower, fig3e, fig4-patients-below-pooled, fig4-named-patients (reproduced):** Agree. Cells 41, 44, 49, 52 and 55 meet each criterion.
  - Camera Cuts at 0.0961 clears its lower bound of 0.095 by only 0.001.
  - fig4-named-patients still assumes the subject ids are the paper's patient numbers.
- **fig5-region-decoding (partially_reproduced):** Agree. Three of four orderings hold (cell 58).
- **fig5-faces-presence (partially_reproduced):** Agree. One of three conditions holds (cell 61). The criterion was written before these labels were decoded.
- **fig6-responsive-subsets (blocked):** Agree. The subsets come from the uncalibrated test. The variant with only the non-responsive units that spike gives drops of 0.062 for camera cuts and 0.060 for Summer (cell 64).
- **fig7b-top500-overlap (partially_reproduced):** Agree. 95 common units against 78 ± 7.8, which is about 83 times chance (top_ranked_units cell 4).
- **fig7a-500-neurons (partially_reproduced):** Agree. The top 500 units give 0.375 against 0.357 for all units, but 229 units give a higher 0.394 (top_ranked_units cell 7).
- **fig3c-lstm-decoding and fig3d-temporal-shuffle (blocked):** Agree.

**2. Does the text match the printed numbers?**

Every "**Result:**" conclusion, the Summary and the attempt record's notes match the outputs, apart from these:
- **Main notebook, cell 21:** "now run for every unit and the 11 labels of Table S1 in the companion notebook `responsive_zeta.ipynb`".
  - No notebook has that name; the ZETA test is in `responsive_zeta_cuts.ipynb` and `responsive_zeta_labels.ipynb`.
  - Those two notebooks cover 9 labels. Tom Faces and Summer Faces are not run.
- **Main notebook, cell 65:** "so with active units alone the drop is no larger for camera cuts than for Summer". The printed drops are 0.062 and 0.060, so it is 0.002 larger. "About the same" would match the numbers.
- **ZETA notebooks (cuts cell 10, labels cell 8), cell 22, the README and the record call the ZETA test "calibrated".**
  - At alpha 0.01 the labels notebook flags 0.12 to 0.38% of units at random times, and 0.21% over all labels. That is conservative, not calibrated.
  - At 0.001, zero hits in 400 or 800 units cannot show calibration (0.4 to 0.8 would be expected).
  - "Conservative" or "not anticonservative" is what the outputs support.
- **README:**
  - "counts about 70% of units responsive even at random event times". That holds only with as many events as camera cuts (68.4%). With each other label's number of onsets the rate is 9.5 to 55.5% (cell 18).
  - "counts far fewer units than the paper". This is false for Outdoor (8 against 4), Indoor (2 against 0) and McKenzie (1 against 0) (labels notebook, cell 7).
  - It gives run times of about 22 and 14 minutes. The runs printed 15.2 and 9.7 minutes; minor.

My round-1 reasons are reported faithfully. Most are verbatim with the cell references removed. Several have accurate third-person summaries of my problem and not-checked lists appended ("It found…", "It asked…").

fig5-faces-presence and fig7a are recorded as agrees: false, although my own round-1 outcome was also blocked. The response explains this: I held the blocks avoidable and listed them as affecting a conclusion. I accept that reading.

**3. Which round-1 points are resolved?**

Resolved:
- **Point 1 (Wilcoxon test miscalibrated):** Handled. The claims stay blocked, and the record now gives the null rates by number of onsets plus the synthetic check.
- **Point 2:** The per-label null is now shown (cell 18).
- **Point 3:** The active and inactive split and the active-only variant were added (cell 64).
- **Point 4:** fig5-faces-presence and fig7a now have stand-ins with criteria written before the fits.
- **Point 6:** First segments are kept, and cell 16 asserts the onset rule.
- **Point 7:** `sample_windows` now extends the edges.
- **Point 8:** The scikit-learn ≥ 1.8 requirement is documented in `fit_logreg`. I could not see `requirements.in`.
- **Point 9:** The weak per-patient clock check is now stated (11 of 29) and backed by the per-patient shifted-label check (18 of 29).
- **Not-checked items:** Per-fold permutation p-values were added for fig4 and fig5.

Partly resolved:
- **Point 5:** ZETA now covers every unit and 9 labels, but still with 100 resamplings. 1000 were compared only for PHC and scene cuts (11 and 31 against 12 and 29).

Not resolved:
- The subject-id to patient-number mapping (the Figure 4 image could not be retrieved).

What remains that bears on a conclusion:
- **fig4-named-patients:** It still rests on the unconfirmed id mapping, and patient 15 is at 0.197, just under 0.2.
- **fig3c-logreg-cuts-lower:** It is reproduced by a 0.001 margin for Camera Cuts, and one Scene Cuts fold is at chance (p = 0.89). The notes state both; the outcome is fragile but follows the criterion.
- **fig7a-500-neurons:** The 500-unit advantage (0.018) is smaller than either SEM (0.026, 0.029). The criterion uses means, so the outcome stands.
- **ZETA as a test of the paper's counts:** Its conservatism at 0.01 means its counts are lower bounds. That does not change any outcome: the gap is 79 against 1025 for camera cuts, and ZETA is only a variant.

## End of run

14 turns, 2 minutes, result: success.
