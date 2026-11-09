# 000055 · author-revise-2 · run 42354570315

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/000055/verifier-2-report.md; ls entries/000055-peterson-2021 entries/000055-peterson-2021/*
```

```
Sat Nov  7 08:17:38 UTC 2026
**Round 2 verification: Peterson et al. 2021 on DANDI:000055**

**1. Outcomes and assumptions**

The claims file has 25 claims and the attempt record has 25 outcomes, one per claim. I agree with all 25:

- 15 reproduced: subject-days, roi-projection-link, fig2-features-differ-across-subjects, fig2-bimanual-skew, extfig2-1c-contralateral-larger, fig3-group-lfb-decrease-hfb-increase, fig3-sensorimotor-largest, fig4-precentral-subject-variability, fig5-band-power-differs-across-subjects, fig5-recording-day-effects, extfig5-1-baseline-reduces-day-variability, discussion-day-changes-small, fig6-r2-at-most-025, fig6b-best-models-sensorimotor, fig6c-angle-and-day-most-informative.
- Also reproduced: fig6d-upward-reaches-enhance-pattern and fig6d-angle-and-day-largest-coefficients (17 in all).
- 6 partially reproduced: cohort, fig2-reach-shape, extfig2-2-feature-correlations, fig2-days-and-waking, table1-subject-band-power-ci, extfig6-2-angle-most-retained.
- 1 not reproduced: fig2-event-counts.
- 1 blocked as methods_underspecified: fig3-lfb-more-widespread.

The six regression outcomes now rest on outputs (cells 88–106) and each matches its criterion:
- **fig6-r2-at-most-025:** largest R2 is 0.189, against a limit of 0.275.
- **fig6b-best-models-sensorimotor:** in LFB, 22 of 22 electrodes with R2 > 0.05 are in the five frontoparietal regions. In HFB it is 13 of 14. The projected top three are all frontoparietal.
- **fig6c-angle-and-day-most-informative:** angle and day have the two largest median Delta R2 in LFB under every variant.
- **extfig6-2-angle-most-retained:** the angle part holds; the order of the next four fails under both readings.
- **fig6d-upward-reaches-enhance-pattern:** median angle coefficient is −1.027 in LFB and +0.535 in HFB.
- **fig6d-angle-and-day-largest-coefficients:** angle and the day SD are the two largest under both readings in both bands.
[... 58 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -80; ls attempts 2>/dev/null | grep 000055; find . -path ./node_modules -prune -o -name "*000055*" -print | grep -v "^./transcripts" | head
```

```
1:# Protocol for an attempt
40:## Reader
42:### 1. Get the paper
56:### 2. Read the paper's code
66:### 3. Write the claims file
151:### 4. Data from outside the paper's own recordings
159:### 5. Check
172:### 6. Answer questions
185:## Author
201:### 1. Establish what can be tested
328:### 2. Check the data against its description
343:### 3. Write the entry
401:### 4. Lock, check and run
412:### 5. Record the attempt
463:### 6. Hand over for verification
501:## Repeat attempts
543:## Local and remote datasets
566:## Verifier
570:### Round 1: without the author's conclusions
595:### Round 2: with the author's conclusions
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 185,200p docs/protocol.md; sed -n 401,500p docs/protocol.md; sed -n 595,640p docs/protocol.md
```

````
## Author

The workflow puts the paper under `paper/`, as for the reader. Read it to
understand the claims, their data and their figures. The claims file still
decides what is tested: do not change a claim's statement, expected values or
criterion. A method detail the claims file lacks is taken from the paper
(step 6).

**Time.** An author run is stopped five hours after it starts, and whatever
is not recorded by then is lost. The prompt says when the run started and the
time by which to finish. Check the clock (`date -u`) between steps. When that
time comes, stop analysing and finish: record each claim not yet tested as
blocked, `too_large` where the computation is what stopped it, saying how far
it got, then write the attempt record and run the entry's checks. A record
with some claims blocked for time is worth more than a run that is cut off.

### 4. Lock, check and run

```bash
python tools/entry.py lock entries/<name>
[... 117 more lines not kept]
````

**Agent calls Bash**

```bash
cat attempts/000055-peterson-2021-01.yaml
```

```
<persisted-output>
Output too large (39.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/c44ac5e9-1ed9-4358-a99a-f9b46fb2fd08/tool-results/byxo4zys7.txt

Preview (first 2KB):
schema_version: 2
id: 000055-peterson-2021-01
dataset:
  archive: dandi
  id: "000055"
  version: 0.220127.0436
  doi: 10.48324/dandi.000055/0.220127.0436
paper: doi:10.1523/eneuro.0007-21.2021
date: 2026-11-07
entry: 000055-peterson-2021
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
[... 32 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/c44ac5e9-1ed9-4358-a99a-f9b46fb2fd08/tool-results/byxo4zys7.txt"
}
```

```
1	schema_version: 2
2	id: 000055-peterson-2021-01
3	dataset:
4	  archive: dandi
5	  id: "000055"
6	  version: 0.220127.0436
7	  doi: 10.48324/dandi.000055/0.220127.0436
8	paper: doi:10.1523/eneuro.0007-21.2021
9	date: 2026-11-07
10	entry: 000055-peterson-2021
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
[... 635 more lines not kept]
```

**Agent calls Bash**

```bash
ls executed/000055-peterson-2021/ 2>/dev/null; python - <<'EOF'
import json
nb=json.load(open('entries/000055-peterson-2021/reproduce_peterson_2021.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    print(i,c['cell_type'],repr(s[:150]))
EOF
```

```
0 markdown '# Reproducing Peterson et al. (2021) from dandiset 000055\n\n**Paper.** Peterson SM, Singh SH, Wang NXR, Rao RPN, Brunton BW (2021). Behavioral and neur'
1 code 'import os\nimport time\nimport warnings\n\nos.environ["OMP_NUM_THREADS"] = "1"\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nfrom'
2 code 'started = time.time()\nassets = ajile.list_assets()\nsessions = ajile.load_sessions(assets)\n# LOAD-BEH-END\nprint(f"{len(sessions)} files of dandiset {aj'
3 code '# One table of events. Time of day from the midnight clock of the files (see the helper).\nrows = []\nfor s in sessions:\n    e = s["events"].copy()\n    '
4 markdown '## Data check\n\nCounts by subject and day, units and ranges of every variable used, and the clocks of the\ndata streams. Each check of the metadata agai'
5 code 'info = pd.DataFrame([{\n    "subject": s["subject"], "day": s["day"], "subject_id": s["subject_id"], "session_id": s["session_id"],\n    "session_start_'
6 code '# Columns of the reaches table in every file: is any event marked as a false positive or verified?\nrc = pd.Series({f"S{s[\'subject\']} day {s[\'day\']}": '
7 code "# Electrode groups and their descriptions in each subject's first file, beside the data\n# descriptor's Table 2 (Peterson et al. 2022, Sci Data 9:184, "
8 markdown 'The files hold 12 subjects and 55 subject-days, ECoG at 500 Hz and pose at 30 frames per\nsecond. The ECoG is stored with a conversion of 1e-6 to volts'
9 code 'desc = {c: None for c in ["start_time", "stop_time", "duration", "magnitude", "angle_file", "angle", "speed",\n                          "speech", "bim'
10 code "# Reach angle convention: angle and magnitude from the wrist trace (onset to the largest\n# displacement within the reach), compared with the files' va"
11 markdown "The files' reach angle is the angle of the reach in image coordinates (y pointing down), not yet\nnegated, so upward reaches have negative values; the "
12 code '# Clock of the pose 
[... 96 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000055-peterson-2021; python - <<'EOF'
import json
nb=json.load(open('reproduce_peterson_2021.ipynb'))
for i in [0,57,59,86,88,90,91,93,94,96,97,102,103,105,106,107,108]:
    print('=====',i); print(''.join(nb['cells'][i]['source']))
EOF
```

```
===== 0
# Reproducing Peterson et al. (2021) from dandiset 000055

**Paper.** Peterson SM, Singh SH, Wang NXR, Rao RPN, Brunton BW (2021). Behavioral and neural
variability of naturalistic arm movements. *eNeuro* 8(3), ENEURO.0007-21.2021.
[doi:10.1523/ENEURO.0007-21.2021](https://doi.org/10.1523/ENEURO.0007-21.2021). The claims file was
written from the version of record in Europe PMC (PMC8225404): main text, Methods, legends, Tables 1
and 2 and the legends of the Extended Data figures.

**Dataset.** [DANDI:000055](https://dandiarchive.org/dandiset/000055/0.220127.0436) (AJILE12),
version 0.220127.0436. The paper cites no DANDI version: its data statement points to the curated
epochs on Figshare, and the dandiset was published later. This is the only published version, and
the draft lists the same 55 files with the same total size, so the published version is pinned.
The files are streamed; nothing is downloaded.

**What the dataset holds.** 12 subjects and 55 subject-days of preprocessed ECoG (500 Hz), pose of
nine key points (30 frames per second), 8088 contralateral wrist movement events with the paper's
ten features, coarse behaviour labels, and an electrode table with MNI positions, a `good` flag and
the paper's regression R2 per electrode. Sex and age are not in it.

[... 331 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "def \|coef_all\|std(" ajile.py | sed -n 1,200p
```

```
102:def asset_url(asset_id: str) -> str:
107:def list_assets() -> pd.DataFrame:
122:def _open(asset_id):
126:def _s(v):
130:def read_session(asset_id: str) -> dict:
190:def load_sessions(assets: pd.DataFrame, workers: int = 8) -> list[dict]:
198:def fold_angle(a):
208:def roi_files() -> dict:
213:def read_roi_matrix(subject: str, files: dict) -> pd.DataFrame:
218:def roi_weights(df: pd.DataFrame, good: np.ndarray, normalise: bool = True) -> np.ndarray:
242:def _band_idx(band):
246:def _tidx(lo, hi):
253:def _wavelet_fft(n_fft: int) -> np.ndarray:
270:def segment_power(x: np.ndarray) -> np.ndarray:
296:def segment_quality(x: np.ndarray, good: np.ndarray) -> tuple[float, float, float]:
313:def band_values(p: np.ndarray) -> dict:
325:def ecog_session(args) -> dict:
372:def load_ecog(jobs: list, workers: int = 8) -> list[dict]:
380:def boot_sig_mask(curr_power: np.ndarray, baseidx: np.ndarray, rng: np.random.Generator,
411:def ecog_offset(session: dict) -> float:
[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "entries/000055-peterson-2021/ajile.py",
 "offset": 600,
 "limit": 80
}
```

```
600	def electrode_model(args) -> dict:
601	    """One electrode and band: forward selection on all events, then a Huber fit per split of
602	    the full model and, per selected feature, of a refit with that feature's columns shuffled
603	    among the training events (all day columns together, all time-of-day columns together, as
604	    the code shuffles them). Unselected columns are set to 0 (code), which is the same as
605	    leaving them out, as their coefficients are then 0; a feature with no selected column gets
606	    Delta R2 0 (code).
607	
608	    Returns the split-averaged withheld R2 of the full model; per feature the Delta R2 of the
609	    Methods (refit scored on the unshuffled withheld events) and of the code (refit scored on
610	    withheld events whose columns are shuffled among them; the code shuffles the column over
611	    all events before splitting, here the refit is shared with the Methods' version); the
612	    split-averaged coefficients per feature (for day and time of day the SD of their one-hot
613	    coefficients, code); and the fraction of each feature's columns selected (code,
614	    feat_select_prob). With `full_only`, only the full model is fitted.
615	    """
616	    X, groups, y, tr, te, seed, full_only = args
617	    rng = np.random.default_rng(seed)
618	    names = list(groups)
619	    if not np.std(y) > 0:
[... 48 more lines not kept]
```

**Agent**

Adding to the helper the second definition of the day and time-of-day SD (SD of the split-averaged one-hot coefficients), so both readings can be printed.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000055-peterson-2021/ajile.py",
 "old_string": "    coefs = {}\n    for g in names:\n        ci = col_of[g]\n        coefs[g] = float(coef_all[:, ci].std(1).mean() if len(ci) > 1 else coef_all[:, ci[0]].mean())\n    out = {\"selected\": [X.columns[c] for c in sel], \"r2\": float(r2_full.mean()), \"coef\": coefs,",
 "new_string": "    coefs, coefs_sdm = {}, {}\n    for g in names:\n        ci = col_of[g]\n        coefs[g] = float(coef_all[:, ci].std(1).mean() if len(ci) > 1 else coef_all[:, ci[0]].mean())\n        coefs_sdm[g] = float(coef_all[:, ci].mean(0).std() if len(ci) > 1 else coefs[g])\n    out = {\"selected\": [X.columns[c] for c in sel], \"r2\": float(r2_full.mean()), \"coef\": coefs,\n           \"coef_sd_of_mean\": coefs_sdm,"
}
```

```
The file entries/000055-peterson-2021/ajile.py has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000055-peterson-2021/ajile.py",
 "old_string": "    split-averaged coefficients per feature (for day and time of day the SD of their one-hot\n    coefficients, code); and",
 "new_string": "    split-averaged coefficients per feature (for day and time of day the SD of their one-hot\n    coefficients within each split, averaged over splits, code; `coef_sd_of_mean` gives\n    instead the SD of the split-averaged one-hot coefficients); and"
}
```

```
The file entries/000055-peterson-2021/ajile.py has been updated successfully.
```

**Agent**

Now the notebook edits: store the new coefficient in cell 88, fix cells 0 and 59, and add the stored-R2 check cell with its result text.

**Agent calls Bash**

```bash
python - <<'EOF'
import json
p='reproduce_peterson_2021.ipynb'
nb=json.load(open(p))
C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def setsrc(i,s): C[i]['source']=s.splitlines(keepends=True)
s=src(88)
old='        row.update({f"coef:{f}": v for f, v in out["coef"].items()})\n'
assert old in s
s=s.replace(old, old+'        row.update({f"coefsdm:{f}": v for f, v in out["coef_sd_of_mean"].items()})\n')
setsrc(88,s)
s=src(0)
old="that step takes\nabout 22 minutes."
assert old in s
s=s.replace(old,"that step took\n19.8 minutes in the last run (printed below).")
setsrc(0,s)
s=src(59)
old="Middle frontal and supramarginal show the same pattern."
assert old in s
s=s.replace(old,"Over 0 to 0.5 s, middle frontal, supramarginal and middle temporal show the same pattern (middle temporal only weakly, -0.005 and +0.003 dB); at the onset bin supramarginal's high-frequency value is 0.000, so there it holds only over 0 to 0.5 s.")
setsrc(59,s)
code = r'''# The fig6b-d criteria on the electrodes the stored R2 select (the paper's own per-electrode R2 in
# the files, low_freq_R2 and high_freq_R2, above 0.05), and the overlap of those sets with the
# sets selected by the R2 here. Delta R2 refits are run for the stored-selected good electrodes
# that lack them, with the seeds of the main fit.
st = pd.concat([stored[["subject", "electrode", col]].rename(columns={col: "r2_stored"}).assign(band=band)
                for band, col in [("lfb", "low_freq_R2"), ("hfb", "high_freq_R2")]])
Gs = G.merge(st, on=["subject", "electrode", "band"], how="left")
for band in ["lfb", "hfb"]:
    d = Gs[Gs.band == band]
    ours = set(map(tuple, d[d.r2 > 0.05][["subject", "electrode"]].values))
    theirs = set(map(tuple, d[d.r2_stored > 0.05][["subject", "electrode"]].values))
    print(f"{band.upper()}: R2 > 0.05 here {len(ours)} electrodes ({len({s_ for s_, _ in ours})} subjects), stored {len(theirs)} "
          f"({len({s_ for s_, _ in theirs})} subjects), in both {len(ours & theirs)}; by subject here "
          f"{dict(pd.Series([s_ for s_, _ in ours]).value_counts().sort_index())}, stored "
          f"{dict(pd.Series([s_ for s_, _ in theirs]).value_counts().sort_index())}")
need = Gs[(Gs.r2_stored > 0.05) & Gs["dr2:angle"].isna()][["subject", "electrode"]].drop_duplicates()
extra = fit([(s_, e, band) for s_, e in need.itertuples(index=False) for band in ["lfb", "hfb"]], "mean", 0.9, False, 0)
print(f"refits for stored-selected electrodes without them: {len(need)} electrodes")
if len(extra):
    ix = ["subject", "electrode", "band"]
    chk = Gs.set_index(ix).loc[extra.set_index(ix).index]
    assert np.allclose(chk.r2, extra.r2)
    Gs = Gs.set_index(ix)
    dcols = [c for c in extra if c.startswith("dr2")]
    Gs.loc[extra.set_index(ix).index, dcols] = extra.set_index(ix)[dcols].values
    Gs = Gs.reset_index()
# Select by the stored R2: ranked() and the angle medians select on the column r2.
S_ = Gs.assign(r2_here=Gs.r2, r2=Gs.r2_stored)
print("\nfig6b reading a with the stored selection (share of selected electrodes in the five frontoparietal regions):")
for band in ["lfb", "hfb"]:
    hi = S_[(S_.band == band) & (S_.r2 > 0.05)]
    print(f"  {band.upper()}: {hi.region.isin(FP5).sum()} of {len(hi)} ({hi.region.isin(FP5).mean():.3f}); regions "
          f"{dict(hi.region.value_counts())}")
print("For reference only (the paper's own values): median stored R2 sensorimotor against temporal, and the three "
      "highest projected stored R2:")
for band in ["lfb", "hfb"]:
    d = S_[S_.band == band]
    proj, _ = project(d, "r2")
    print(f"  {band.upper()}: {d[d.region.isin(SM3)].r2.median():.4f} against {d[d.region.isin(TEMP)].r2.median():.4f}; "
          f"{list(proj.sort_values(ascending=False).index[:3])}")
print("\nfig6c with the stored selection, median Delta R2:")
for band in ["lfb", "hfb"]:
    for prefix in ["dr2:", "dr2code:"]:
        v, n = ranked(S_, band, prefix)
        print(f"  {band.upper()} {prefix} ({n} electrodes): {v.round(4).head(4).to_dict()}; angle and day the two largest: "
              f"{set(v.index[:2]) == {'angle', 'day'}}")
print("\nfig6d with the stored selection:")
for band in ["lfb", "hfb"]:
    x = S_[(S_.band == band) & (S_.r2 > 0.05)]["coef:angle"]
    va, n = ranked(S_, band, "coef:", fn=lambda v: np.median(np.abs(v)))
    vb, _ = ranked(S_, band, "coef:", fn=lambda v: abs(np.median(v)))
    print(f"  {band.upper()} ({n} electrodes): median angle coefficient {x.median():+.4f} ({(x < 0).mean():.3f} negative); "
          f"reading a {va.round(4).head(3).to_dict()}; reading b {vb.round(4).head(3).to_dict()}; "
          f"angle and day the two largest: a {set(va.index[:2]) == {'angle', 'day'}}, b {set(vb.index[:2]) == {'angle', 'day'}}")
# The day and time-of-day coefficient: the mean over splits of the SD of the one-hot coefficients
# (used above) against the SD of the split-averaged one-hot coefficients, on both selections.
print("\nDay and time-of-day value under the two definitions (reading a, median |value|):")
for lab, d in [("selection here", G), ("stored selection", S_)]:
    for band in ["lfb", "hfb"]:
        va, n = ranked(d, band, "coef:", fn=lambda v: np.median(np.abs(v)))
        vs, _ = ranked(d, band, "coefsdm:", fn=lambda v: np.median(np.abs(v)))
        print(f"  {lab}, {band.upper()} ({n}): mean of per-split SD day {va['day']:.4f}, time of day {va['time_of_day']:.4f}; "
              f"SD of mean day {vs['day']:.4f}, time of day {vs['time_of_day']:.4f}; two largest with the SD of mean "
              f"{list(vs.index[:2])}")
'''
cell={"cell_type":"code","execution_count":None,"metadata":{},"outputs":[],"source":code.splitlines(keepends=True)}
md={"cell_type":"markdown","metadata":{},"source":["**Electrodes selected by the stored R2 (sensitivity, not the criterion).** TO FILL\n"]}
C.insert(107,cell); C.insert(108,md)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
git diff --stat
```

```
entries/000055-peterson-2021/ajile.py              |  7 +-
 .../reproduce_peterson_2021.ipynb                  | 86 +++++++++++++++++++++-
 tools/build_site.py                                | 15 ++++
 tools/runner/run_requests.py                       |  4 +-
 tools/site_assets/app.css                          |  3 +
 5 files changed, 109 insertions(+), 6 deletions(-)
```

**Agent calls Bash**

```bash
git diff reproduce_peterson_2021.ipynb | head -40; git diff reproduce_peterson_2021.ipynb | tail -5
```

```
diff --git a/entries/000055-peterson-2021/reproduce_peterson_2021.ipynb b/entries/000055-peterson-2021/reproduce_peterson_2021.ipynb
index 74f3ea0149..89174804be 100644
--- a/entries/000055-peterson-2021/reproduce_peterson_2021.ipynb
+++ b/entries/000055-peterson-2021/reproduce_peterson_2021.ipynb
@@ -43,8 +43,8 @@
     "| fig5-recording-day-effects, extfig5-1-baseline-reduces-day-variability, discussion-day-changes-small | tested |\n",
     "| fig6b-best-models-sensorimotor, fig6-r2-at-most-025, fig6c-angle-and-day-most-informative, extfig6-2-angle-most-retained, fig6d-upward-reaches-enhance-pattern, fig6d-angle-and-day-largest-coefficients | tested |\n",
     "\n",
-    "The notebook reads about 8000 ECoG segments of 10 s from 55 files of 8 to 20 GB each; that step takes\n",
-    "about 22 minutes. The regression models take a few minutes."
+    "The notebook reads about 8000 ECoG segments of 10 s from 55 files of 8 to 20 GB each; that step took\n",
+    "19.8 minutes in the last run (printed below). The regression models take a few minutes."
    ]
   },
   {
@@ -1233,7 +1233,7 @@
    "id": "7f7dffa6",
    "metadata": {},
    "source": [
-    "**Result: reproduced.** After masking, the mean over 4-30 Hz is negative and over 50-120 Hz positive in precentral (-0.885 and 0.496 dB), postcentral (-0.890, 0.507) and inferior parietal (-0.663, 0.277) over 0 to 0.5 s, and also at the time bin of onset (reading b). Middle frontal and supramarginal show the same pattern."
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json,uuid
p='reproduce_peterson_2021.ipynb'
nb=json.load(open(p))
for c in nb['cells']:
    if 'id' not in c: c['id']=uuid.uuid4().hex[:8]
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
git diff reproduce_peterson_2021.ipynb | tail -3; date -u; grep -n "def cmd_\|add_parser" ../../tools/entry.py | head -20
```

```
{
    "cell_type": "code",
    "execution_count": null,
Sat Nov  7 08:18:53 UTC 2026
```

**Agent**

Syntax-check the new cell, then the full run.

**Agent calls Bash**

```bash
python - <<'EOF'
import json,ast
nb=json.load(open('reproduce_peterson_2021.ipynb'))
for i in (88,107): ast.parse(''.join(nb['cells'][i]['source']))
print('ok')
EOF
cd ../.. && python -c "import ast;ast.parse(open('entries/000055-peterson-2021/ajile.py').read())" && (time python tools/entry.py all entries/000055-peterson-2021) > $TMPDIR/run.log 2>&1; tail -30 $TMPDIR/run.log
```

```
ok
Installed kernelspec registry-000055-peterson-2021 in executed/000055-peterson-2021/.venv/share/jupyter/kernels/registry-000055-peterson-2021
0 error(s)
pass  reproduce_peterson_2021.ipynb  (2434 s)

real	40m44.626s
user	143m18.210s
sys	8m3.576s
```

**Agent**

The run passed in 41 min. Reading the new outputs.

**Agent calls Bash**

```bash
ls executed/000055-peterson-2021/; python - <<'EOF'
import json,glob
f=[x for x in glob.glob('executed/000055-peterson-2021/*.ipynb')][0]
nb=json.load(open(f))
for i in [19,57,88,90,93,96,102,105,107]:
    c=nb['cells'][i]
    print('=====',i)
    for o in c.get('outputs',[]):
        t=''.join(o.get('text',''))or ''.join(o.get('data',{}).get('text/plain',''))
        print(t[-6000:])
EOF
```

```
reproduce_peterson_2021.ipynb
result.json
===== 19
ECoG segments of 8087 events read and reduced in 34.6 min

===== 57
           region  a_0-0.5s_LF4-30  a_0-0.5s_HF50-120  b_t0_LF4-30  b_t0_HF50-120  unmasked_a_LF  unmasked_a_HF  significant_bins
   middle frontal           -0.405              0.223       -0.363          0.215         -0.405          0.223              1436
       precentral           -0.885              0.496       -0.748          0.460         -0.885          0.496              1353
      postcentral           -0.890              0.507       -0.742          0.477         -0.890          0.507              1434
inferior parietal           -0.663              0.277       -0.592          0.278         -0.663          0.277              1337
    supramarginal           -0.304              0.014       -0.201          0.000         -0.304          0.049               700
superior temporal           -0.143             -0.003       -0.114         -0.007         -0.156         -0.008               380
  middle temporal           -0.005              0.003        0.000          0.004         -0.027          0.011               233
inferior temporal            0.000              0.012        0.000          0.006         -0.011          0.034               205
reading a_0-0.5s: pattern holds in 3 of 3 named regions {'precentral': np.True_, 'postcentral': np.True_, 'inferior parietal': np.True_}
reading b_t0: pattern holds in 3 of 3 named regions {'precentral': np.True_, 'postcentral': np.True_, 'inferior parietal': np.True_}
Regions with the pattern under reading a: ['middle frontal', 'precentral', 'postcentral', 'inferior parietal', 'supramarginal', 'middle temporal']

===== 88
[... 215 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000055-peterson-2021 && python - <<'EOF'
import json
p='reproduce_peterson_2021.ipynb'
nb=json.load(open(p))
C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def setsrc(i,s): C[i]['source']=s.splitlines(keepends=True)
def rep(i,a,b):
    s=src(i); assert a in s,(i,a); setsrc(i,s.replace(a,b))
rep(0,"that step took\n19.8 minutes in the last run (printed below).","that step took\n20 to 35 minutes in recent runs (the time is printed below).")
rep(59,"at the onset bin supramarginal's high-frequency value is 0.000, so there it holds only over 0 to 0.5 s.",
 "at the onset bin supramarginal's high-frequency value and middle temporal's low-frequency value are 0.000, so for those two it holds only over 0 to 0.5 s.")
assert src(108).startswith("**Electrodes selected by the stored R2")
setsrc(108,"**Electrodes selected by the stored R2 (sensitivity, not the criterion).** The electrodes with R2 > 0.05 here and those with stored R2 > 0.05 overlap in 18 electrodes in LFB (22 here, 23 stored) and 12 in HFB (14 here, 22 stored). The stored sets come from 5 subjects in LFB and 8 in HFB, against 4 and 6 here. With the stored selection, 22 of 23 LFB and 18 of 22 HFB electrodes are in the five frontoparietal regions (fig6b, reading a, share part). Angle (0.063) and day (0.013) have the two largest median Delta R2 in LFB, and day (0.050) and angle (0.019) in HFB, with the code's Delta R2 too (fig6c). The median angle coefficient is -1.026 in LFB and +0.498 in HFB (fig6d, upward reaches). Angle and the day SD are the two largest coefficient values under both readings in both bands (fig6d, largest coefficients). The fig6b-d results are the same on either set of electrodes. Taken as the SD of the split-averaged one-hot coefficients, not the mean over splits of the per-split SD, the day value is 0.658 against 0.660 in LFB and 0.729 against 0.733 in HFB, and angle and day stay the two largest.\n")
s=src(110)
assert s.startswith("## Summary")
a="The code's log(x + 1) transforms"
assert a in s
s=s.replace(a,"The day and time-of-day coefficient is the mean over splits of the SD of their one-hot coefficients; the SD of the split-averaged coefficients changes it by at most 0.004. On the electrodes selected by the R2 stored in the files, the fig6b-d results are the same. "+a)
a="marks none as false positives, so all are kept."
assert a in s
s=s.replace(a,"marks none as false positives, so all are kept, for the behavioural claims and for every ECoG claim.")
setsrc(110,s)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
grep -n "false positive\|22 minutes\|minutes" README.md | head
```

```
41:shifts it (`ecog_offset`). The files hold 8088 events with no false positives marked, more than the
43:Figure 6 take a few minutes, as `ajile.huber_fit` solves many Huber fits at once. The attempt
```

**Agent calls Bash**

```bash
sed -n 30,60p README.md
```

```
| All regression R2 at most 0.25 | Reproduced |
| Best models over frontoparietal sensorimotor areas | Reproduced |
| Reach angle and day most informative (Delta R2) | Reproduced |
| Reach angle most often retained, then four features in order | Partially reproduced |
| Upward reaches enhance the movement pattern | Reproduced |
| Reach angle and day have the largest coefficients | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

In three files the ECoG starts after midnight but is stored with a start time of 0; `ajile.py`
shifts it (`ecog_offset`). The files hold 8088 events with no false positives marked, more than the
paper analysed. The notebook reads about 8000 ECoG segments and takes about half an hour; the regression models of
Figure 6 take a few minutes, as `ajile.huber_fit` solves many Huber fits at once. The attempt
record, with the reasons and the differences from the paper's method, is
[`attempts/000055-peterson-2021-01.yaml`](../../attempts/000055-peterson-2021-01.yaml).
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='README.md'; s=open(p).read()
a="The files hold 8088 events with no false positives marked, more than the\npaper analysed. The notebook reads about 8000 ECoG segments and takes about half an hour;"
assert a in s
s=s.replace(a,"The files hold 8088 events with no false positives marked, more than the\npaper analysed; all are kept, in the behavioural and in the ECoG analyses. The notebook reads about 8000 ECoG segments and takes 30 to 45 minutes;")
open(p,'w').write(s)
EOF
date -u
```

```
Sat Nov  7 09:00:21 UTC 2026
```

**Agent**

Now the attempt record: notes and deviations, then the round-2 verification entry.

**Agent calls Bash**

```bash
cd ../.. && python - <<'EOF'
p='attempts/000055-peterson-2021-01.yaml'; s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1,a; s=s.replace(a,b)
rep("""    -0.592 and 0.278). Middle frontal and supramarginal show the same pattern over 0 to 0.5 s.
""","""    -0.592 and 0.278). Middle frontal, supramarginal and middle temporal (-0.005 and 0.003 dB) show
    the same pattern over 0 to 0.5 s; at the onset bin supramarginal's high-frequency value and middle
    temporal's low-frequency value are 0.000.
""")
rep("""  - ECoG times in three files (S01 day 7, S04 day 3, S06 day 3) are shifted by 29241 to 30682 s, the
    ECoG missing at the start of the day (see findings).
""","""  - ECoG times in three files (S01 day 7, S04 day 3, S06 day 3) are shifted by 29241 to 30682 s, the
    ECoG missing at the start of the day (see findings).
  - The events include the false positives the paper removed (Methods, 17.8% of events removed as
    false positives or occlusions), as the files do not mark them (fig2-event-counts). This holds for
    every ECoG claim that refers to this one.
""")
rep("""    projected R2 are precentral, postcentral and inferior parietal in both bands. Few electrodes exceed
    0.05, from 4 subjects in LFB and 6 in HFB.
""","""    projected R2 are precentral, postcentral and inferior parietal in both bands. Few electrodes exceed
    0.05, from 4 subjects in LFB and 6 in HFB. These sets overlap the electrodes whose stored R2 (the
    paper's own, in the files) exceeds 0.05 in 18 electrodes in LFB (22 here, 23 stored, 5 subjects)
    and 12 in HFB (14 here, 22 stored, 8 subjects). Selected by the stored R2, 22 of 23 LFB and 18 of
    22 HFB electrodes are in the five frontoparietal regions (a sensitivity output, not the
    criterion).
""")
rep("""    inclusion of bad electrodes all give angle and day as the two largest in both bands.
""","""    inclusion of bad electrodes all give angle and day as the two largest in both bands. Over the
    electrodes whose stored R2 exceeds 0.05 (23 LFB, 22 HFB; a sensitivity output), angle (0.063) and
    day (0.013) are the two largest in LFB and day (0.050) and angle (0.019) in HFB, also with the
    code's Delta R2.
""")
rep("""    the HFB medians 0 to 0.730 (6 subjects).
""","""    the HFB medians 0 to 0.730 (6 subjects). Over the electrodes whose stored R2 exceeds 0.05 (a
    sensitivity output), the median is -1.026 in LFB (23 electrodes) and 0.498 in HFB (22).
""")
rep("""    readings. The day SD is the second largest value in LFB and the largest in HFB, which bears on the
    statement's "large" SD.
  deviations:
  - As for fig6-r2-at-most-025.
""","""    readings. The day SD is the second largest value in LFB and the largest in HFB, which bears on the
    statement's "large" SD. Over the electrodes whose stored R2 exceeds 0.05 (a sensitivity output),
    angle and the day SD are also the two largest under both readings in both bands (LFB 1.026 and
    0.635, HFB day 0.668 and angle 0.498).
  deviations:
  - As for fig6-r2-at-most-025.
  - The day (and time-of-day) value is the mean over splits of the SD of the one-hot coefficients in
    each split (helper electrode_model). Taken as the SD of the split-averaged coefficients it is
    0.658 against 0.660 in LFB and 0.729 against 0.733 in HFB, and angle and day stay the two largest.
""")
open(p,'w').write(s)
EOF
grep -n "R2 > 0.05" attempts/000055-peterson-2021-01.yaml | head -3
```

```
343:  notes: Reading a, all 22 good electrodes with LFB R2 > 0.05 and 13 of 14 (0.929) with HFB R2 > 0.05
362:  notes: Over the 22 good electrodes with LFB R2 > 0.05, reach angle (median Delta R2 0.066) and
394:  notes: The median split-averaged reach-angle coefficient over good electrodes with R2 > 0.05 is
```

**Agent calls Bash**

```bash
cat >> attempts/000055-peterson-2021-01.yaml <<'EOF'
- date: '2026-11-07'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: Round 2. The full executed notebook after the round-1 revision, with the conclusion cells,
    the summary, the README and this record, the helper module and the claims file, with the paper and
    the data descriptor. The verifier checked huber_fit, forward_select, day_balanced_splits and
    electrode_model against sklearn's Huber objective and statsmodels' rank-based adjusted R2. It agreed
    with all 25 outcomes and found every number in the conclusions matching the outputs.
  results:
  - claim: subject-days
    agrees: true
    outcome: reproduced
    reason: Agrees with the outcome.
    response: No change needed.
  - claim: roi-projection-link
    agrees: true
    outcome: reproduced
    reason: Agrees with the outcome.
    response: No change needed.
  - claim: cohort
    agrees: true
    outcome: partially_reproduced
    reason: Agrees. Cell 7 lists the groups and cell 31 gives the descriptor's counts; the "five" fails
      either way (B6 resolved). 8 male and 4 female are in the data descriptor, as stated.
    response: No change needed.
  - claim: fig2-event-counts
    agrees: true
    outcome: not_reproduced
    reason: Agrees. The claim is judged on reading a in full, and on reading b without its false-positive
      step, which the files make impossible. This is a data limitation and is disclosed (B3 resolved as
      far as the data allow).
    response: No change needed.
  - claim: fig2-features-differ-across-subjects
    agrees: true
    outcome: reproduced
    reason: Agrees with the outcome.
    response: No change needed.
  - claim: fig2-reach-shape
    agrees: true
    outcome: partially_reproduced
    reason: Agrees. A boundary-reflected KDE puts the peaks within 15 degrees of +-90 in 6 of 12 subjects,
      not more than half, so the partial outcome holds under either KDE. The bias remains in the criterion
      and is reported there (B2 resolved as a sensitivity check).
    response: No change needed.
  - claim: fig2-bimanual-skew
    agrees: true
    outcome: reproduced
    reason: Agrees with the outcome.
    response: No change needed.
  - claim: extfig2-1c-contralateral-larger
    agrees: true
    outcome: reproduced
    reason: Agrees with the outcome.
    response: No change needed.
  - claim: extfig2-2-feature-correlations
    agrees: true
    outcome: partially_reproduced
    reason: Agrees with the outcome.
    response: No change needed.
  - claim: fig2-days-and-waking
    agrees: true
    outcome: partially_reproduced
    reason: Agrees with the outcome.
    response: No change needed.
  - claim: fig3-group-lfb-decrease-hfb-increase
    agrees: true
    outcome: reproduced
    reason: Agrees; the assumed reading of the bad-segment rule is stated and reasonable, and cell 107
      shows it changes no outcome. Every ECoG outcome includes the false-positive events the files do not
      mark, which is stated under fig2-event-counts and fig6 but not under fig3 or fig5. Cell 59 says
      middle frontal and supramarginal show the same pattern, but cell 57 also lists middle temporal
      (-0.005 and +0.003 dB), and supramarginal's high-frequency value at the onset bin is 0.000, so the
      pattern holds there only over 0 to 0.5 s.
    response: Added a deviation that the events include the paper's false positives, which carries to
      every ECoG claim that refers to this one, and said so in the summary and the README. Cell 59 and the
      notes now name middle temporal and say that at the onset bin supramarginal's high-frequency value
      and middle temporal's low-frequency value are 0.000.
  - claim: fig3-sensorimotor-largest
    agrees: true
    outcome: reproduced
    reason: Agrees; the assumption is stated and reasonable.
    response: No change needed.
  - claim: fig3-lfb-more-widespread
    agrees: true
    outcome: blocked
    reason: Agrees. Under ten seeds the readings give 7 against 7 regions and 35.0 to 35.6 against 25.5
      to 25.8 bins per frequency every time (B4 resolved).
    response: No change needed.
  - claim: fig4-precentral-subject-variability
    agrees: true
    outcome: reproduced
    reason: Agrees; the tie-break is stated with the strict reading (partial) recorded. Part 4 depends on
      the tie-break, and this is disclosed (B5 resolved by disclosure).
    response: No change needed.
  - claim: fig5-band-power-differs-across-subjects
    agrees: true
    outcome: reproduced
    reason: Agrees. The false-positive events are not stated under fig5 (see fig3-group).
    response: The false-positive deviation of fig3-group-lfb-decrease-hfb-increase carries to this claim.
  - claim: table1-subject-band-power-ci
    agrees: true
    outcome: partially_reproduced
    reason: Agrees with the outcome.
    response: As for fig5-band-power-differs-across-subjects.
  - claim: fig5-recording-day-effects
    agrees: true
    outcome: reproduced
    reason: Agrees with the outcome.
    response: As for fig5-band-power-differs-across-subjects.
  - claim: extfig5-1-baseline-reduces-day-variability
    agrees: true
    outcome: reproduced
    reason: Agrees; the assumption is stated and reasonable.
    response: As for fig5-band-power-differs-across-subjects.
  - claim: discussion-day-changes-small
    agrees: true
    outcome: reproduced
    reason: Agrees; the microvolt unit is stated and reasonable.
    response: As for fig5-band-power-differs-across-subjects.
  - claim: fig6-r2-at-most-025
    agrees: true
    outcome: reproduced
    reason: Largest R2 is 0.189, against a limit of 0.275. The batched Huber fit agrees with sklearn to
      4.4e-05 in R2, and refits only where R2 > 0.05 are the only electrodes the criteria use (B1
      resolved).
    response: No change needed.
  - claim: fig6b-best-models-sensorimotor
    agrees: true
    outcome: reproduced
    reason: In LFB, 22 of 22 electrodes with R2 > 0.05 are in the five frontoparietal regions, in HFB 13 of
      14; the projected top three are all frontoparietal. The attempt's R2 matches the stored R2 only
      moderately (Spearman 0.718 LFB, 0.643 HFB), and the claim rests on small sets (22 LFB electrodes
      from 4 subjects, 11 from S01; 14 HFB from 6 subjects). The notebook does not show how far these
      sets overlap the paper's; the overlap with the stored R2 > 0.05 sets and the criteria applied to
      electrodes selected by the stored R2 would settle it. The outcome stands on present evidence.
    response: Added both outputs. The sets overlap in 18 electrodes in LFB (22 here, 23 stored) and 12 in
      HFB (14 here, 22 stored); the stored sets come from 5 and 8 subjects. Selected by the stored R2, 22
      of 23 LFB and 18 of 22 HFB electrodes are frontoparietal. Outcome kept.
  - claim: fig6c-angle-and-day-most-informative
    agrees: true
    outcome: reproduced
    reason: Angle and day have the two largest median Delta R2 in LFB under every variant. Rests on the
      same small sets as fig6b-best-models-sensorimotor, whose overlap with the paper's is not shown.
    response: Added the stored-R2 selection, with Delta R2 refits for the 12 stored-selected electrodes
      that lacked them. Angle and day are the two largest in both bands, with both Delta R2 versions.
      Outcome kept.
  - claim: extfig6-2-angle-most-retained
    agrees: true
    outcome: partially_reproduced
    reason: The angle part holds; the order of the next four fails under both readings.
    response: No change needed.
  - claim: fig6d-upward-reaches-enhance-pattern
    agrees: true
    outcome: reproduced
    reason: Median angle coefficient is -1.027 in LFB and +0.535 in HFB. Rests on the same small sets as
      fig6b-best-models-sensorimotor, whose overlap with the paper's is not shown.
    response: Added the stored-R2 selection; the median is -1.026 in LFB and 0.498 in HFB. Outcome kept.
  - claim: fig6d-angle-and-day-largest-coefficients
    agrees: true
    outcome: reproduced
    reason: Angle and the day SD are the two largest under both readings in both bands. The day coefficient
      is taken as the mean over splits of the per-split SD, not the SD of the split-averaged coefficients,
      and the record does not state this. It can only raise the day value a little, and the margins are
      large (day 0.660 against the next feature at 0.188 in LFB).
    response: Added a deviation stating the definition and an output with the other one. The SD of the
      split-averaged coefficients gives 0.658 against 0.660 in LFB and 0.729 against 0.733 in HFB, and
      angle and day stay the two largest, also with the stored-R2 selection. Outcome kept.
EOF
date -u
```

```
Sat Nov  7 09:01:02 UTC 2026
```

**Agent**

Text cells changed after the run, so I'll re-run so the executed copy holds the final text. Running the checks first.

**Agent calls Bash**

```bash
python tools/entry.py check entries/000055-peterson-2021 2>&1 | tail -15
```

```
0 error(s)
```

**Agent calls Bash**

```bash
(time python tools/entry.py all entries/000055-peterson-2021) > $TMPDIR/run2.log 2>&1; tail -6 $TMPDIR/run2.log; date -u
```

```
0 error(s)
pass  reproduce_peterson_2021.ipynb  (2484 s)

real	41m34.959s
user	145m45.462s
sys	8m13.518s
Sat Nov  7 09:42:49 UTC 2026
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('executed/000055-peterson-2021/reproduce_peterson_2021.ipynb'))
for i in [19,57,88,90,107]:
    for o in nb['cells'][i].get('outputs',[]):
        t=''.join(o.get('text',''))
        print('==',i); print(t[:1500] if i!=107 else t)
EOF
```

```
== 19
ECoG segments of 8087 events read and reduced in 35.4 min

== 57
           region  a_0-0.5s_LF4-30  a_0-0.5s_HF50-120  b_t0_LF4-30  b_t0_HF50-120  unmasked_a_LF  unmasked_a_HF  significant_bins
   middle frontal           -0.405              0.223       -0.363          0.215         -0.405          0.223              1436
       precentral           -0.885              0.496       -0.748          0.460         -0.885          0.496              1353
      postcentral           -0.890              0.507       -0.742          0.477         -0.890          0.507              1434
inferior parietal           -0.663              0.277       -0.592          0.278         -0.663          0.277              1337
    supramarginal           -0.304              0.014       -0.201          0.000         -0.304          0.049               700
superior temporal           -0.143             -0.003       -0.114         -0.007         -0.156         -0.008               380
  middle temporal           -0.005              0.003        0.000          0.004         -0.027          0.011               233
inferior temporal            0.000              0.012        0.000          0.006         -0.011          0.034               205
reading a_0-0.5s: pattern holds in 3 of 3 named regions {'precentral': np.True_, 'postcentral': np.True_, 'inferior parietal': np.True_}
reading b_t0: pattern holds in 3 of 3 named regions {'precentral': np.True_, 'postcentral': np.True_, 'inferior parietal': np.True_}
Regions with the pattern under reading a: ['middle frontal',
== 88
main (90/10, band mean, all electrodes): 2368 full models, 86 with refits, 1.5 min; 80/20 (good electrodes): 2192 and 84, 1.2 min; band median: 2192 full models; total 3.8 min
main: models with nothing to fit (flat power) 32, of which good 0; models with no feature selected 9
80/20: models with nothing to fit (flat power) 0, of which good 0; models with no feature selected 9
[... 56 more lines not kept]
```

**Agent**

No outcome changed. All 25 stay as verified in round 2, and nothing was proposed for a third round. I re-ran the entry twice with `python tools/entry.py all entries/000055-peterson-2021`. Both runs passed the checks with 0 errors and printed the same numbers as before; the full run takes about 41 min.

**Added or corrected, point by point:**
- **Overlap with the paper's own R2 (fig6b-d).** I added the two outputs the verifier asked for in a new cell, with refits for the 12 electrodes it needed. The electrodes above R2 0.05 here and those above 0.05 by the R2 stored in the files share 18 in LFB (22 here, 23 stored) and 12 in HFB (14 here, 22 stored).
  - With the stored selection, the fig6b-d results still hold. 22 of 23 LFB and 18 of 22 HFB electrodes are frontoparietal, angle and day have the two largest median Delta R2 in both bands, and the median angle coefficient is -1.026 in LFB and +0.498 in HFB. Angle and the day SD remain the two largest coefficient values.
  - These are recorded in the notes as a sensitivity check, not the criterion.
- **Day coefficient definition.** The record now states it is the mean over splits of the per-split SD. The helper and notebook also print the other definition, the SD of the split-averaged coefficients: 0.658 against 0.660 in LFB and 0.729 against 0.733 in HFB, with the same top two.
- **False positives in the ECoG claims.** The fig3 claim has a new deviation saying the events include the paper's false positives, and every ECoG claim that refers to fig3 carries it. The summary and README now say this too.
- **Cell 59 and the fig3 notes.** They now name middle temporal (-0.005 and +0.003 dB). They also say that at the onset bin, supramarginal's high-frequency value and middle temporal's low-frequency value are 0.000. The verifier only flagged supramarginal; the new run shows middle temporal is also 0.000 there.
- **Run-time wording.** The ECoG step took 34.6 and 35.4 min in these runs, against 19.8 min before, so no single figure is right. Cell 0 now says 20 to 35 minutes, and the README says 30 to 45 minutes for the whole notebook.
- **Round 2 record.** It is under `verifications` with all 25 claims marked as agreed, the verifier's reasons, and my responses.

**Not done:**
- I added no question to `questions/000055.yaml`, because the report names no place where the claims file misreads the paper.
- I made no changes for the points the verifier listed as disclosed and not bearing on outcomes: fig2-event-counts reading b, the fig4 tie-break and the fig2 KDE criterion.
- The unrelated edits already in the working tree under `tools/` were left untouched.
- Nothing was committed, as instructed.

## End of run

25 turns, 85 minutes, $1.34 at API prices, result: success.
