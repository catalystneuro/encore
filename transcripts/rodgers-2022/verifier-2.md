# 000231 · verifier-2 · run 40964075362

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 344
drwxr-xr-x 6 runner runner    4096 Oct 29 22:23 .
drwxr-xr-x 7 runner runner    4096 Oct 29 22:23 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 29 22:12 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 29 22:12 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 29 22:23 .claude
-rw-r--r-- 1 runner runner       0 Oct 29 22:23 .env
-rw-r--r-- 1 runner runner       0 Oct 29 22:23 .env.development
-rw-r--r-- 1 runner runner       0 Oct 29 22:23 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 29 22:23 .env.local
-rw-r--r-- 1 runner runner       0 Oct 29 22:23 .env.production
-rw-r--r-- 1 runner runner       0 Oct 29 22:23 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 29 22:23 .env.test
-rw-r--r-- 1 runner runner       0 Oct 29 22:23 .env.test.local
drwx------ 2 runner runner    4096 Oct 29 22:23 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 29 22:12 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 29 22:12 .github
-rw-r--r-- 1 runner runner       0 Oct 29 22:23 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 29 22:12 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 29 22:12 .mcp.json
[... 107 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; cat 000231-rodgers-2022-01.yaml
```

```
<persisted-output>
Output too large (43.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/1821069e-2fcc-4bd3-ba3e-7131b88873d8/tool-results/bsi51mnw7.txt

Preview (first 2KB):
# Rodgers (2022) from dandiset 000231

Tests the statements of the data descriptor [Rodgers (2022)](https://doi.org/10.1038/s41597-022-01728-1)
on [DANDI:000231](https://dandiarchive.org/dandiset/000231/0.220904.1554), version 0.220904.1554, the
version the paper cites. The dandiset holds 115 sessions of 15 mice doing whisker-based shape
discrimination or detection, with whisker tracking from 200 frames/s video and, in 44 sessions,
recordings from barrel cortex.

| Claims | Outcome |
|---|---|
| Neural sessions and hours, task rules, "nothing" only in detection, one task per mouse, servo positions, outcome logic, forced alternation, video timebase, blackout gaps, bend on interpolated frames, neural sampling rate, unit depths and layers, electrode order, recording columns, observation intervals, pose structure, C0 contacts, contacts structure, NWB structure, file layout, video format, subjects (23 claims) | Reproduced |
| Dataset size (trials do not match), choice time as the first lick, ignore_trial definition, trials table stop and start times, unit firing-rate criterion, session labeling quality (6 claims) | Not reproduced |
| Reward and timeout, sessions with at least 90 trials (2 claims) | Blocked: methods underspecified (the criterion's readings disagree) |
| Response window timing, neural to video alignment, Arduino clock drift, three tracking-accuracy claims (6 claims) | Blocked: data missing |
| Two findings of earlier papers (2 claims) | Blocked: methods underspecified |

[... 11 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "README.md"
}
```

```
1	# Rodgers (2022) from dandiset 000231
2	
3	Tests the statements of the data descriptor [Rodgers (2022)](https://doi.org/10.1038/s41597-022-01728-1)
4	on [DANDI:000231](https://dandiarchive.org/dandiset/000231/0.220904.1554), version 0.220904.1554, the
5	version the paper cites. The dandiset holds 115 sessions of 15 mice doing whisker-based shape
6	discrimination or detection, with whisker tracking from 200 frames/s video and, in 44 sessions,
7	recordings from barrel cortex.
8	
9	| Claims | Outcome |
10	|---|---|
11	| Neural sessions and hours, task rules, "nothing" only in detection, one task per mouse, servo positions, outcome logic, forced alternation, video timebase, blackout gaps, bend on interpolated frames, neural sampling rate, unit depths and layers, electrode order, recording columns, observation intervals, pose structure, C0 contacts, contacts structure, NWB structure, file layout, video format, subjects (23 claims) | Reproduced |
12	| Dataset size (trials do not match), choice time as the first lick, ignore_trial definition, trials table stop and start times, unit firing-rate criterion, session labeling quality (6 claims) | Not reproduced |
13	| Reward and timeout, sessions with at least 90 trials (2 claims) | Blocked: methods underspecified (the criterion's readings disagree) |
14	| Response window timing, neural to video alignment, Arduino clock drift, three tracking-accuracy claims (6 claims) | Blocked: data missing |
15	| Two findings of earlier papers (2 claims) | Blocked: methods underspecified |
16	
17	A failure to reproduce here may be a failure of this attempt, not of the paper: see the
18	reasoning and the differences from the paper's method.
19	
20	The attempt record, with the reasons and the differences from the paper's method, is
[... 8 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "000231-rodgers-2022-01.yaml"
}
```

```
1	schema_version: 2
2	id: 000231-rodgers-2022-01
3	dataset:
4	  archive: dandi
5	  id: "000231"
6	  version: 0.220904.1554
7	  doi: 10.48324/dandi.000231/0.220904.1554
8	paper: doi:10.1038/s41597-022-01728-1
9	date: 2026-10-29
10	entry: 000231-rodgers-2022
11	provenance:
12	  kind: agent
13	  accountable:
14	    name: CatalystNeuro
15	  agent:
16	    harness: Claude Code
17	    model: claude-opus-5-5
18	    protocol: pilot-12
19	  runner:
20	    platform: GitHub Actions
[... 721 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -c "^- id:" 10.1038-s41597-022-01728-1.yaml; python3 -c "
import yaml,collections
a=yaml.safe_load(open('000231-rodgers-2022-01.yaml'))
c=yaml.safe_load(open('10.1038-s41597-022-01728-1.yaml'))
print(len(a['outcomes']), collections.Counter((o['outcome'],o.get('blocked_by')) for o in a['outcomes']))
ids=[x['id'] for x in c['claims']] if isinstance(c,dict) and 'claims' in c else None
print(ids and set(ids)^set(o['claim'] for o in a['outcomes']))
print(len(a['verifications'][0]['results']))
for o in a['outcomes']:
  if 'assumed' in str(o): print(o['claim'])
"; grep -n "assumed" 000231-rodgers-2022-01.yaml 10.1038-s41597-022-01728-1.yaml | head
```

```
39
39 Counter({('reproduced', None): 23, ('not_reproduced', None): 6, ('blocked', 'data_missing'): 6, ('blocked', 'methods_underspecified'): 4})
set()
39
```

**Agent calls Bash**

```bash
cd  python3 - <<'E' > $TMPDIR/nb.txt
import json
nb=json.load(open('reproduce_rodgers_2022.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f"\n=== cell {i} [{c['cell_type']}] ===")
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--\n'+''.join(o['text']))
        elif 'data' in o and 'text/plain' in o['data']: print('--OUT--\n'+''.join(o['data']['text/plain']))
        elif o.get('output_type')=='error': print('--ERR--', o['ename'], o['evalue'])
E
wc -l $TMPDIR/nb.txt; grep -n "^=== cell" $TMPDIR/nb.txt | wc -l
```

```
1855 /tmp/claude-1001/nb.txt
112
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "limit": 700
}
```

```
1	
2	=== cell 0 [markdown] ===
3	# Reproducing Rodgers (2022) from dandiset 000231
4	
5	Paper. Chris C. Rodgers, "A detailed behavioral, videographic, and neural dataset on object recognition in mice", *Scientific Data* 9, 620 (2022), doi:10.1038/s41597-022-01728-1. It is a data descriptor: its findings are statements about the deposited data (counts, file layout, the NWB contents, the trial logic, the alignment of the streams, the quality criteria) and two findings of earlier papers on the same data.
6	
7	Dataset. DANDI:000231, version `0.220904.1554` (doi:10.48324/dandi.000231/0.220904.1554), streamed from the archive. This is the version the paper cites (its reference 11, as the claims file records), and the only published version; the draft (modified 2023-06-20) has the same 4228 assets and size. The version is pinned for that reason.
8	
9	Text read. The claims file `claims/000231/10.1038-s41597-022-01728-1.yaml` was written from the version of record (Europe PMC full text, no supplement exists), with the bioRxiv preprint compared for the counts.
10	
11	Method. Every NWB file (115) is opened over HTTP and reduced as it loads to per-session summaries (helper `rodgers.py`): the trials table, lick and reward times, for each whisker the timestamps, interpolation flags and bend of the processed series, the shapes and conversion of the pose series and the contacts tables, and for the 44 ecephys files the recording's shape and rate, the electrodes and the units with their spike times. The 115 videos are read only to their container headers. Sizes of the raw Open Ephys files come from the archive's asset list. No result uses data from outside the dandiset. Nothing here is random, so no seed is needed.
12	
13	| Claim | Tested or blocked |
14	|---|---|
15	| dataset-size, neural-sessions, neural-hours | tested |
16	| task-rules, nothing-detection-only, one-task-per-mouse, servo-positions | tested |
17	| response-window-timing | blocked: no motor times in the dataset (the d
[... 683 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 700,
 "limit": 600
}
```

```
700	print(f"  first lick minus choice_time: median {ns.d.median() * 1000:.2f} ms, 1st to 99th percentile "
701	      f"{ns.d.quantile(0.01) * 1000:.1f} to {ns.d.quantile(0.99) * 1000:.1f} ms; no lick after the window on {ns.d.isna().sum()} trials")
702	print(f"spoiled trials: {len(sp)}; choice_time 45 s after the window (within 5 ms): {sp.ok_time.mean():.4f}; "
703	      f"choice nogo: {sp.ok_side.mean():.4f}; choice_time NaN on {sp.d.isna().sum()} of them")
704	# where the first lick in the window is not at choice_time: where is choice_time, and was the mouse already licking?
705	mis = []
706	for s in S:
707	    lt, _ = all_licks(s)
708	    for r in s["trials"][s["trials"].outcome != "spoil"].itertuples():
709	        i = np.searchsorted(lt, r.response_window_open_time)
710	        if i < len(lt) and abs(lt[i] - r.choice_time) > 0.005:
711	            mis.append(dict(c_minus_w=r.choice_time - r.response_window_open_time,
712	                            lick_before=bool(((lt > r.response_window_open_time - 0.1) & (lt < r.response_window_open_time)).any()),
713	                            any_lick_at_choice=bool((np.abs(lt - r.choice_time) <= 0.005).any())))
714	mis = pd.DataFrame(mis)
715	print(f"mismatched trials {len(mis)}: choice_time within 5 ms after the window opening on {(mis.c_minus_w.between(0, 0.005)).mean():.3f}; "
716	      f"a lick in the 100 ms before the opening on {mis.lick_before.mean():.3f}; any lick within 5 ms of choice_time on {mis.any_lick_at_choice.mean():.3f}")
717	print(f"  choice_time minus window opening on mismatched trials: median {mis.c_minus_w.median() * 1000:.1f} ms, "
718	      f"95th percentile {mis.c_minus_w.quantile(0.95) * 1000:.1f} ms")
719	per = ns.groupby("path").apply(lambda d: (d.ok_time & d.ok_side).mean(), include_groups=False)
[... 580 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1299,
 "limit": 560
}
```

```
1299	## electrodes-order
1300	
1301	> The NWB electrodes are ordered from superficial to deep, broken channels are excluded, the raw data columns follow the electrodes table, and the sites are 20 um apart over 1280 um.
1302	
1303	=== cell 74 [code] ===
1304	rows = []
1305	pat = re.compile(r"layer (\S+), Intan channel (\d+), OpenEphys channel (\d+).*channel (\d+) starting with 0 = most superficial and including.*channel (\d+) starting with 0 = most superficial and excluding")
1306	for e in E:
1307	    x = e["ecephys"]
1308	    y = x["el_y"]
1309	    dy = np.diff(y)
1310	    parsed = [pat.search(l) for l in x["el_location"]]
1311	    incl = np.array([int(p.group(4)) for p in parsed if p])
1312	    excl = np.array([int(p.group(5)) for p in parsed if p])
1313	    rows.append(dict(path=e["path"], n=len(y), n_data=x["n_channels"], increasing=bool((dy > 0).all()),
1314	                     multiple20=bool(np.allclose(dy / 20, np.round(dy / 20))), steps_over_20=int((dy > 20.001).sum()),
1315	                     region_ok=bool((x["electrodes_region"] == np.arange(len(y))).all()),
1316	                     parsed=sum(p is not None for p in parsed), excl_ok=bool((excl == np.arange(len(y))).all()),
1317	                     y_vs_incl=float(np.ptp(y - 20 * incl)) if len(incl) == len(y) else np.nan,
1318	                     oe_intan=all(int(p.group(3)) == int(p.group(2)) + 1 for p in parsed if p),
[... 538 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "def \|contact_missing\|inclusive\|exclusive" rodgers.py | head -80
```

```
53:def list_assets() -> list[dict]:
66:def version_metadata() -> dict:
72:def retry(fn, *args, tries: int = 4, wait: float = 5.0):
83:def s3_url(asset_id: str) -> str:
84:    def head():
91:def open_nwb(asset_id: str) -> h5py.File:
95:def _str(x):
103:def parse_name(path: str) -> dict:
111:def max_true_run(b: np.ndarray) -> int:
120:def grid_offset(t: np.ndarray) -> float:
128:def _trials(f) -> pd.DataFrame:
139:def _whisker(f, w: str, trials: pd.DataFrame) -> dict:
219:            # is stop_time the last frame of the contact (inclusive) or one past it?
221:            out["contact_duration_inclusive"] = int((du == fe - fs + 1).sum())
222:            out["contact_duration_exclusive"] = int((du == fe - fs).sum())
229:            out["contact_missing"] = (nlab < full) | (a < 0) | (b >= len(labeled))
230:            # variant: stop exclusive, frames start to stop - 1 (at least the start frame)
234:            out["contact_missing_excl"] = (nlab2 < b2 - a + 1) | (a < 0) | (b2 >= len(labeled))
238:def _ecephys(f, trials: pd.DataFrame) -> dict:
288:def summarize_session(asset: dict) -> dict:
[... 19 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "rodgers.py",
 "offset": 200,
 "limit": 40
}
```

```
200	        out["pose_n_steps_short"] = int((dtp < FRAME - GRID_TOL).sum())
201	        out["pose_n_steps_not_frame"] = int((np.abs(dtp - FRAME) >= GRID_TOL).sum())
202	        out["pose_t_first"] = float(tp[0]) if tp.size else np.nan
203	        out["pose_t_last"] = float(tp[-1]) if tp.size else np.nan
204	    # contacts
205	    pc = f"processing/behavior/contacts_by_whisker_{w}"
206	    if pc in f:
207	        g = f[pc]
208	        out["contact_columns"] = [_str(c) for c in g.attrs["colnames"]]
209	        st, sp = g["start_time"][:], g["stop_time"][:]
210	        out["contact_start"] = st
211	        out["n_contacts"] = int(st.size)
212	        out["contact_start_after_stop"] = int((st > sp).sum())
213	        out["contact_grid_offset"] = max(grid_offset(st), grid_offset(sp)) if st.size else np.nan
214	        if "frame_start" in g:
215	            fs = g["frame_start"][:]
216	            out["contact_frame_vs_time"] = float(np.abs(fs * FRAME - st).max()) if st.size else np.nan
217	        if {"frame_start", "frame_stop", "duration_frames"} <= set(g.keys()) and st.size:
218	            fs, fe, du = g["frame_start"][:], g["frame_stop"][:], g["duration_frames"][:]
219	            # is stop_time the last frame of the contact (inclusive) or one past it?
[... 20 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "rodgers.py",
 "offset": 400,
 "limit": 115
}
```

```
400	    return float((c / dur < 0.05 * mean).mean())
401	
402	
403	def task_from_metadata(s: dict) -> str | None:
404	    """The task the session metadata names: the experiment description, and the keywords only
405	    when the description names no task (the keywords say "shape discrimination" in every file,
406	    detection sessions included, so they cannot decide the task where the description does)."""
407	    for text in ((s.get("experiment_description") or "").lower(), " ".join(s.get("keywords") or []).lower()):
408	        det, dis = "shape detection" in text, "shape discrimination" in text
409	        if det and not dis:
410	            return "detection"
411	        if dis and not det:
412	            return "discrimination"
413	    return None
414	
415	
416	def assign_trials(times: np.ndarray, trials: pd.DataFrame) -> np.ndarray:
417	    """Row index of the trial whose [start_time, stop_time) holds each time, or -1."""
418	    st = trials["start_time"].to_numpy()
419	    sp = trials["stop_time"].to_numpy()
[... 93 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import yaml
c=yaml.safe_load(open('10.1038-s41597-022-01728-1.yaml'))
print(list(c.keys()))
for x in c['claims']:
  if x['id'] in ('session-labeling-quality','neural-hours','trials-table-structure','unit-quality-isi','reward-and-timeout','choice-time-first-lick','forced-alternation-start','nothing-detection-only'):
    print('-----',x['id']); print(yaml.dump(x, width=120))
"
```

```
['schema_version', 'dataset', 'paper', 'claims', 'checks']
----- neural-hours
criterion: The paper does not say which recording is timed. Readings are (a) the summed duration of the "extracellular array
  recording" timestamps in the NWB files (last minus first), (b) the summed duration of the main Open Ephys recordings under
  sourcedata/ (test recordings of a few seconds left out, Data Records, Raw data, neural acquisition files). Tolerance 0.05
  h, the rounding of the printed value. Reproduced when one reading is within it; partially reproduced when one is within
  10%. The channel count of the raw files (64) is checked; the NWB files exclude broken channels and may hold fewer.
expected:
  quantity: hours of neural recording
  tolerance: 0.05
  unit: h
  value: 33.8
id: neural-hours
quote: includes 88.9 hours of behavioral video at 200 frames per second and 33.8 hours of 64-channel neural recording at 30
  kHz
source: Background & Summary, paragraph 5
statement: The dataset includes 33.8 hours of 64-channel neural recording at 30 kHz.

----- nothing-detection-only
criterion: Using the session metadata's task where it is given (experiment description or keywords), reproduced when no discrimination
[... 97 more lines not kept]
```

**Agent**

**Verifier report, round 2: Rodgers 2022 (Sci Data 9, 620), DANDI:000231 v0.220904.1554**

The claims file has 39 claims (`grep -c "^- id:"`) and the attempt record has 39 outcomes, one for each claim. They are 23 reproduced, 0 partially reproduced, 6 not reproduced, 6 blocked (data_missing) and 4 blocked (methods_underspecified). The README table gives the same counts (23 / 6 / 2 + 6 + 2).

A correction to my round-1 report: its totals line ("24 reproduced, 7 not reproduced, 8 blocked") was miscounted. My own per-claim table gives 23 / 6 / 10, which is what the record holds. The record does not repeat my wrong totals.

### 1. Outcomes

I agree with all 39 stated outcomes. No outcome in the attempt record carries `assumed: true`, so there are no assumptions to judge.

- **neural-hours:** the main recordings give 33.770 h and the whole files 33.782 h. Both are within 0.05 h of 33.8 (cell 17), so the outcome no longer depends on how the test recordings are handled.
- **session-labeling-quality:** not_reproduced is now firm.
  - The stop frame is inclusive. `duration_frames` equals `frame_stop − frame_start + 1` on all 290,345 contacts (cell 92).
  - All four readings in the claims file fail (cell 92).
  - Pooling contacts over the whiskers of a session is not a reading in the claims file. It also exceeds 2%: 2.007% and 2.008%.
- **trials-table-structure:** not_reproduced is correct for the claims file as written. Problem 6 below could still change it.

### 2. Sentences the printed numbers do not support

- **Cell 44:** "the other 5 sessions begin at trial 61 or later". Cell 43 prints only the first *random* trial of those 5 sessions (61, 76, 88, 102, 124), not the first trial in each table. The output only shows that those tables start after trial 44. The attempt record says this correctly ("begin after trial 44; their first random trials are 61…").
- **Cell 111 (Summary), last sentence:** "Seven Open Ephys files begin with a short separate segment …, the test recordings the paper mentions."
  - Six of the seven are 14–15 records (0.48–0.51 s) with the same recording number (0) as the main segment (cell 17).
  - The paper describes test recordings as "a few seconds long". Nothing printed shows these segments are test recordings.
  - Leaving them out is a reasonable choice, but here it is stated as a finding. The neural-hours note and cell 18 ("left out as the test recordings") have the same problem.
  - This does not affect the outcome, since both totals fall within 0.05 h.
- **Cell 111 (Summary) and the record's `choice_time` finding:** "on 22% of other trials it falls 0 to 5 ms after the window opening". The 22% is the share of mismatched trials (7,185 of 32,085). Cell 34 does not print how many of *all* non-spoiled trials have `choice_time` 0–5 ms after the opening; matched trials can fall there too. It should read "on the 22% where it is not the first lick in the window, it falls…".
- **README:** "It takes about five minutes". Cell 110 prints a run time of 6.5 min.
- **Attempt record, behavior-clock-drift note:** "the dataset's other files are videos and Open Ephys and Kilosort files". Cell 66 lists 44 `.log`, 88 `.mat`, 88 `.m` and 44 `.py` files, and the notebook never identifies the `.log` files. My round-1 asset query found them to be sorting and acquisition logs. Since there are only 44 of them, in ecephys sourcedata only, they cannot be per-session behavioral logs for all 115 sessions. The statement is right, but the printed output does not back it.
- **Outside the scope of the check:** the cell 0 Method paragraph is out of date. It says Open Ephys sizes come from the asset list, but the notebook now also streams the CH1 record headers, the `.openephys` indexes and the Kilosort `.npy` files.

Every other Result, Summary, README and notes sentence matches the printed outputs. I checked each number: the frame and trial counts, the hours, the reward fractions, the per-session ranges, the unit counts and thresholds, the layer crosstab, the contact fractions, the C0 fractions, the conversions, the ages and the video sizes.

The `verifications` block states my round-1 reasons faithfully. They are close paraphrases of my table, with my problem points attached where they concern a claim. Nothing is misattributed and nothing is softened.

### 3. Round-1 points

| # | Status |
|---|---|
| 1 Contact stop inclusive / pooled reading | **Resolved.** Stops are inclusive (cell 92), and every reading plus the pooled variant exceeds 2%. |
| 2 Open Ephys test recordings | **Resolved for the outcome.** Record headers are read, and 33.770 h is within tolerance. The labelling of the 0.5 s segments is in §2. |
| 3 Right reward = right licks; verdict line | **Resolved.** The verdict line, the conclusion and a metadata_error finding now state it. |
| 4 Layer label disagreement | **Resolved.** It is a case difference only: 999 of 999 agree once case is ignored (cell 71). |
| 5 Keywords constant; reading not stated | **Resolved.** The reading is stated, with a crosstab, and `task_from_metadata` now uses the description first. |
| 6 trials-table-structure: "next trial" reading | **Open.** The question is with a reader (questions/000231.yaml), and the variant holds on all 32,230 consecutive-number pairs. If the reader adopts the next-trial-run reading, the outcome would become reproduced. |
| 7 Container frame count overwritten | **Resolved.** It is now printed: no video stream reports a frame count (0 of 115). |
| 8 Amplitude criteria | **Resolved.** Amplitude drift is reported outside the outcome (max 1.47%/min over 893 matched units). The rest are correctly stated as not runnable. |
| 9 KF134 2018-02-09 clock | **Resolved.** Leaving out its 16 units changes no count. |
| 10 Table 4 columns | **Resolved.** They are checked in all 44 files. |

**What still bears on a conclusion:**
- **Problem 6 (trials-table-structure):** the outcome depends on how the claims file reads "next trial", and the reader's answer is still pending.
- **A claims-file reading in session-labeling-quality (reported, not corrected):**
  - The claims file takes the 2% bound per whisker. The paper's "≤2% of the contact events" of a session reads more naturally as pooled over whiskers.
  - Under the pooled reading the outcome would still be not_reproduced. But it would rest on one contact in one session: 54 of 2,691 contacts is 2.007%, and 53 would be 1.97%. It also depends on the helper's rule that a frame absent from the processed series counts as missing.
  - The per-whisker reading fails clearly at 7.7%, so the outcome stands as tested.

## End of run

14 turns, 2 minutes, result: success.
