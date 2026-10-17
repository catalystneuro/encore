# 000568 · verifier-2 · run 39073423645

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 456
drwxr-xr-x 5 runner runner    4096 Oct 17 22:09 .
drwxr-xr-x 7 runner runner    4096 Oct 17 22:09 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 17 22:02 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 17 22:02 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 17 22:09 .claude
-rw-r--r-- 1 runner runner       0 Oct 17 22:09 .env
-rw-r--r-- 1 runner runner       0 Oct 17 22:09 .env.development
-rw-r--r-- 1 runner runner       0 Oct 17 22:09 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 17 22:09 .env.local
-rw-r--r-- 1 runner runner       0 Oct 17 22:09 .env.production
-rw-r--r-- 1 runner runner       0 Oct 17 22:09 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 17 22:09 .env.test
-rw-r--r-- 1 runner runner       0 Oct 17 22:09 .env.test.local
drwx------ 2 runner runner    4096 Oct 17 22:09 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 17 22:02 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 17 22:02 .github
-rw-r--r-- 1 runner runner       0 Oct 17 22:09 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 17 22:02 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 17 22:02 .mcp.json
[... 96 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; echo ======; cat 000568-valero-2022-01.yaml
```

```
<persisted-output>
Output too large (35.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/b9b52738-0b5e-46ff-b3ff-a9b6783f3b2f/tool-results/b8l120xpd.txt

Preview (first 2KB):
# Valero, Zutshi, Yoon & Buzsaki (2022) from dandiset 000568

Tests the findings of [Valero et al. (2022)](https://doi.org/10.1126/science.abm1891) that can be
tested on [DANDI:000568](https://dandiarchive.org/dandiset/000568/0.230705.1633). The dandiset holds
28 sessions of CA1 units recorded with uLED probes in four mice. Light pulse times and laps are in
two of these sessions only, so most claims rest on those two sessions of one mouse. Even there the
files hold only about a third of the pulses, so control time is limited to the windows the stated
protocol keeps dark.

| Claim | Outcome |
|---|---|
| Four mice, 822 pyramidal neurons, 43.3 per session | Partially reproduced |
| 20 ms pulses, 20 to 40 ms offsets, each site every 0.3 to 0.6 s | Partially reproduced |
| 611 of 822 pyramidal neurons respond to light | Reproduced |
| Light responses decrease during sharp-wave ripples | Reproduced |
| Ripple rate change correlates negatively with baseline rate (rho -0.19) | Partially reproduced |
[... 15 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/b9b52738-0b5e-46ff-b3ff-a9b6783f3b2f/tool-results/b8l120xpd.txt"
}
```

```
1	# Valero, Zutshi, Yoon & Buzsaki (2022) from dandiset 000568
2	
3	Tests the findings of [Valero et al. (2022)](https://doi.org/10.1126/science.abm1891) that can be
4	tested on [DANDI:000568](https://dandiarchive.org/dandiset/000568/0.230705.1633). The dandiset holds
5	28 sessions of CA1 units recorded with uLED probes in four mice. Light pulse times and laps are in
6	two of these sessions only, so most claims rest on those two sessions of one mouse. Even there the
7	files hold only about a third of the pulses, so control time is limited to the windows the stated
8	protocol keeps dark.
9	
10	| Claim | Outcome |
11	|---|---|
12	| Four mice, 822 pyramidal neurons, 43.3 per session | Partially reproduced |
13	| 20 ms pulses, 20 to 40 ms offsets, each site every 0.3 to 0.6 s | Partially reproduced |
14	| 611 of 822 pyramidal neurons respond to light | Reproduced |
15	| Light responses decrease during sharp-wave ripples | Reproduced |
16	| Ripple rate change correlates negatively with baseline rate (rho -0.19) | Partially reproduced |
17	| Light gain is largest at the theta trough | Not reproduced |
18	| Place cells are as common among responsive as non-responsive cells | Partially reproduced |
19	| Light gain is higher inside than outside the place field | Reproduced |
20	| In-field gain correlates with out-of-field and home-cage rates | Not reproduced |
[... 547 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat 10.1126-science.abm1891.yaml; grep -c "^- id:\|^  - id:" 10.1126-science.abm1891.yaml
```

```
# Claims for Valero, Zutshi, Yoon & Buzsaki (2022), Science 375, 570-574, on dandiset 000568.
# Source: the NIH author manuscript in PubMed Central (PMC9632609), full text of the main report
# and its figure legends. The Materials and Methods and figures S1 to S15 are in the supplement,
# which could not be obtained (the PMC file is behind a captcha and Science's copy is not open),
# so method details below come from the legends, from buzcode (the code the paper names) and
# from the first author's later lab code, as stated per claim.
#
# When these criteria were written the author had seen the data check only: the file list,
# every group and table of the files, unit counts and baseline-epoch firing rates per session,
# the epoch names, the number of laps and ripples per session, the stored values of the pulse
# series, and the first few pulse timestamps of one session (which showed 20 ms pulses and
# gaps of 1 to 2 s between the first pulses of a uLED). No claim's analysis had been run.
#
# What the data check showed and the criteria take as given: 28 sessions from 4 mice, each
# deposited twice (a full file and a no-raw-data file with the same units); the pulse times of
# the uLEDs are in 2 sessions only (fCamk1 sess9 and sess12), and only these 2 sessions have
# laps. Every claim that needs light pulses or place fields is tested on these 2 sessions. The
# files carry no cell type; pyramidal cells are taken as units whose rate in the first
# (baseline) epoch is below 5 Hz.
#
[... 288 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF' > $TMPDIR/nb.txt
import json
nb=json.load(open('reproduce_valero_2022.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f"\n######## CELL {i} [{c['cell_type']}]")
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--- OUT:\n'+''.join(o['text']))
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d and 'image/png' not in d: print('--- OUT:\n'+''.join(d['text/plain']))
            elif 'image/png' in d: print('--- [image]')
        elif o.get('output_type')=='error': print('--- ERROR', o.get('ename'), o.get('evalue'))
EOF
wc -l $TMPDIR/nb.txt; echo $TMPDIR
```

```
2010 /tmp/claude-1001/nb.txt
/tmp/claude-1001
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
2	######## CELL 0 [markdown]
3	# Reproducing Valero et al. (2022) from dandiset 000568
4	
5	Paper. Valero M, Zutshi I, Yoon E, Buzsaki G (2022). Probing subthreshold dynamics of hippocampal
6	neurons by pulsed optogenetics. Science 375, 570-574.
7	[doi:10.1126/science.abm1891](https://doi.org/10.1126/science.abm1891). This attempt used the full
8	text of the NIH author manuscript in PubMed Central (PMC9632609): the main report and its figure
9	legends. The Materials and Methods and figures S1 to S15 are in the supplement, which could not be
10	obtained (PMC's copy is behind a captcha and the publisher's is not open access). Claims about
11	supplementary figures are taken from the main text's statements of them, and method details come
12	from the code named below.
13	
14	Dandiset. [DANDI:000568](https://dandiarchive.org/dandiset/000568/0.230705.1633), version
15	0.230705.1633, streamed. The paper cites no DANDI version; its data statement points to the Buzsaki
16	Lab Databank, whose page lists this dandiset for the paper (its other copy is on Globus, which needs
17	an account and has no pinned identifier, so it was not used). This is the only published version.
18	The draft holds the same 138 assets (paths, sizes and asset ids, printed below), so nothing the
19	analysis uses differs.
20	
[... 680 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 700,
 "limit": 650
}
```

```
700	between pulses of one uLED is 0.281 to 0.383 s for the four uLEDs with at least 1000 pulses, both as
701	the paper states. The median offset from the end of one pulse to the start of the next is 60.4 ms
702	in sess9 and 80.0 ms in sess12, outside 18 to 44 ms. Of these offsets 31.8% and 30.2% fall within
703	20 to 40 ms, and the 95th percentiles are 241 and 328 ms. The data check shows that most pulses are
704	not in the files (5.76 and 7.50 deposited pulses per s in PreStim, and offsets in sess9 near
705	multiples of 20 ms only), so the longer offsets span missing pulses, and the protocol's offsets
706	cannot be measured from the files. Measured onset to onset, the same 31.8% and 30.2% fall within
707	the 40 to 60 ms of the file's description, so the paper's range and the file's agree if the
708	file's is onset to onset.
709	
710	######## CELL 22 [markdown]
711	## Claim fig1e-responsive-fraction
712	
713	> Of 822 pyramidal neurons, 611 responded to light from the uLEDs.
714	
715	######## CELL 23 [code]
716	rows = []
717	for s in opto:
718	    for label, t in (("(a) PreStim", s["resp_table"]), ("(b) all stimulation epochs", s["resp_table_all"])):
719	        resp = t[t.tested].groupby("unit").responsive.any().reindex(range(len(s["spikes"])), fill_value=False).values
[... 630 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1350,
 "limit": 670
}
```

```
1350	    grid = s["grid"]
1351	    b = v.bin_index(grid["x"])
1352	    for u in np.flatnonzero(s["responsive"] & s["pyr"] & s["place"]):
1353	        for d in (0, 1):
1354	            for (a, z, peak) in s["ctrl_fields"][u][d]:
1355	                infield = (grid["dir"] == d) & (b >= a) & (b < z)
1356	                outfield = (grid["dir"] == d) & ~((b >= a) & (b < z))
1357	                li, lt = rate_where(s["spikes"][u], grid, s["light_mask"][u] & infield)
1358	                ci, _ = rate_where(s["spikes"][u], grid, s["ctrl_mask"] & infield)
1359	                lo, _ = rate_where(s["spikes"][u], grid, s["light_mask"][u] & outfield)
1360	                co, _ = rate_where(s["spikes"][u], grid, s["ctrl_mask"] & outfield)
1361	                rows.append({"session": s["key"].split("_ses-")[1], "unit": u, "dir": d, "start": a, "stop": z,
1362	                             "light_in": li, "ctrl_in": ci, "light_out": lo, "ctrl_out": co, "light_s_in_field": lt,
1363	                             "home_rate": s["base_rate"][u]})
1364	inf = pd.DataFrame(rows)
1365	inf["gain_in"] = inf.light_in - inf.ctrl_in
1366	inf["gain_out"] = inf.light_out - inf.ctrl_out
1367	print("Place fields of responsive putative pyramidal cells:", len(inf), "from", inf.groupby(["session", "unit"]).ngroups,
1368	      "cells; light time in field per field, median", round(inf.light_s_in_field.median(), 1), "s")
1369	print(inf[["light_in", "ctrl_in", "light_out", "ctrl_out", "gain_in", "gain_out"]].median().round(2).to_string())
[... 642 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^def \|^[A-Z_]* = " valero.py | head -80
```

```
66:DANDISET_ID = "000568"
67:DANDISET_VERSION = "0.230705.1633"
69:PULSE_WINDOW_S = 0.020      # paper: 20 ms pulses
70:CONTROL_WINDOW_S = 0.020    # paper: random 20 ms intervals between pulses
71:MIN_PULSES = 1000           # sites with fewer pulses are not tested (code: 2000 over a whole session)
72:N_BOOT = 500                # HippoCookBook getuLEDResponse.m
73:BOOT_PERCENTILE = 0.999     # getuLEDResponse.m bootsTrapCI [0.001 0.999]
74:Z_THRESHOLD = 1.96          # getuLEDResponse.m
75:KS_ALPHA = 0.01             # getuLEDResponse.m
76:PYR_MAX_RATE_HZ = 5.0       # putative pyramidal cells: baseline rate below this (common choice)
77:TRACK_CM = 110.0            # file description: PVC linear track, 110 cm long
78:N_BINS = 50                 # bz_firingMapAvg default
79:SMOOTH_BINS = 2.0           # bz_firingMapAvg default
80:FIELD_THRESHOLD = 0.2       # bz_findPlaceFields1D default
81:FIELD_MIN_SIZE = 0.05       # bz_findPlaceFields1D default, fraction of the track
82:FIELD_MAX_SIZE = 0.60       # bz_findPlaceFields1D default
83:FIELD_MIN_PEAK_HZ = 2.0     # bz_findPlaceFields1D default (minPeak)
85:GRID_S = 0.002              # time grid for occupancy, light and control masks
86:THETA_BAND = (6.0, 10.0)
87:RIPPLE_BAND = (130.0, 200.0)
[... 34 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "valero.py",
 "offset": 270,
 "limit": 310
}
```

```
270	    return np.array(out)
271	
272	
273	def all_light_intervals(s: dict) -> np.ndarray:
274	    """Merged on-intervals of every uLED."""
275	    iv = np.concatenate([np.column_stack([p["on"], p["off"]]) for p in s["pulses"].values()])
276	    return merge_intervals(iv)
277	
278	
279	def control_onsets(s: dict) -> np.ndarray:
280	    """Starts of the 20 ms windows before each pulse onset during which no uLED is on."""
281	    on = np.unique(np.concatenate([p["on"] for p in s["pulses"].values()]))
282	    light = all_light_intervals(s)
283	    starts = on - CONTROL_WINDOW_S
284	    # a window is free of light when no light interval overlaps [start, start + 20 ms)
285	    j = np.searchsorted(light[:, 0], starts + CONTROL_WINDOW_S, side="left") - 1
286	    ok = np.ones(len(starts), bool)
287	    has = j >= 0
288	    ok[has] = light[j[has], 1] <= starts[has]
289	    return starts[ok]
[... 289 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import numpy as np, valero as v
m=np.full(50,1.5); m[20:28]=6.0
print(v.find_fields(m), v.find_fields_simple(m))
m2=np.full(50,0.2); m2[5:12]=5; m2[30:38]=4
print(v.find_fields(m2))
" 2>&1 | tail -5
```

```
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import numpy as np, valero as v
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
cd  mkdir -p paper; curl -sS -m 60 -o paper/PMC9632609_bioc.json "https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/PMC9632609/unicode"; ls -la paper; head -c 300 paper/PMC9632609_bioc.json
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  python3 -c "
import json
d=json.load(open('paper/PMC9632609_bioc.json'))
out=[]
for p in d[0]['documents'][0]['passages']:
    out.append('['+p['infons'].get('section_type','')+'/'+p['infons'].get('type','')+'] '+p['text'])
open('paper/PMC9632609.txt','w').write('\n\n'.join(out))
"; grep -n -i "random\|control epoch\|stab\|spatial information\|trough\|chi" paper/PMC9632609.txt | cut -c1-600
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n '7,13p;135p' paper/PMC9632609.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

# Verifier report, round 2: Valero et al. 2022 (doi:10.1126/science.abm1891) on DANDI 000568 v0.230705.1633

The claims file has 22 claims and the attempt record has 22 outcomes: 5 reproduced, 5 partially reproduced, 6 not reproduced and 6 blocked. I agree with 21 of them; I disagree with fig3g. The paper text (PMC author manuscript, PMC9632609) is saved as `paper/PMC9632609_bioc.json` and `paper/PMC9632609.txt`. Cell indices below are those of the current notebook. I read the new `find_fields` in `valero.py` but could not run it, because numpy is not installed here.

## 1. Outcomes

| Claim | Record | My view |
|---|---|---|
| cohort-counts | partially_reproduced | Agree (cell 17). |
| fig1c-pulse-protocol | partially_reproduced | Agree (cell 20). |
| fig1e-responsive-fraction | reproduced | Agree (cell 23): reading (b), 66/91 = 72.5%. |
| fig1i-swr-decrease | reproduced | Agree (cell 27). |
| figs10-swr-gain-vs-baseline-rate | partially_reproduced | Agree (cell 30). |
| fig2b-theta-trough-gain | not_reproduced | Agree (cell 33). |
| figs11-place-cell-fraction | partially_reproduced | Agree (cell 37): p = 0.20; 84.2% is outside 73 ± 7.3 and 70.6% is within 71 ± 7.1. |
| fig2e-infield-gain | reproduced | Agree (cell 40). |
| figs12-gain-rate-correlations | not_reproduced | Agree (cell 43). |
| fig3a-place-cells-more-excitable | not_reproduced | Agree (cell 46), p = 0.19. This outcome flipped with the new place-cell calls, so it is fragile. |
| fig3c-unmasked-fields | not_reproduced | Agree under the criterion (cell 49). In practice it is undecided: reading (a) has n = 9 and its interval runs 40.0 to 97.2%. |
| fig3e-ghost-fields | partially_reproduced | Agree (cell 53). |
| fig3f-light-stability | not_reproduced | Agree (cell 56). |
| fig3g-spatial-information | reproduced | **Disagree: partially_reproduced.** Part 2 rests on p = 0.039 (cell 59) with dark-window control maps. Against time-matched control the increase is negative in both groups and does not differ (p = 0.3). The paper says "Random intervals (20 ms) between the light pulses served as control epochs" (`paper/PMC9632609.txt`, Results paragraph 2), which the time-matched variant follows most closely. The response says "the criterion fixed the control maps before the analysis", but the criterion fixed "time when no uLED is on", and the revision already replaced that. So the main control maps are not the pre-registered ones either, and the selection bias still favours part 2. |
| fig4c-swr-cofiring-place-pairs | reproduced | Agree under the criterion (cell 62). It is weak: p = 0.032, carried by sess9 alone, and the participation variant gives p = 0.056. The coefficient for place/non-place pairs (0.062) equals that for place pairs (0.060), so the contrast the claim describes is absent. |
| fig4d-light-unmasked-cofiring | not_reproduced | Agree (cell 65). |
| fig1j, fig1km, figs9, fig3h, fig4ef, fig4gh | blocked | Agree. The figs9 proxy (cell 68) is shown, and the reason it stays blocked is sound. |

## 2. Statements the numbers do not support, or overstate

- **Cell 54, and the fig3e notes in the record:** "For 70 control fields of light-responsive place cells" / "For 70 place fields", and "14 light fields" / "14 unmasked fields". Cell 53 prints "n = 70 field directions" (fig2e has 80 fields), and the 14 are field directions from 7 cells.
- **Record, figs10 notes:** "is negatively correlated with the baseline rate … in every subject (-0.37 to -0.71) and every session." The sign is negative in every session, but 3 sessions are not significant (cell 30: fCamk1 sess13 p = 0.12, fCamk3 sess13 p = 0.29, fCamk5 sess14 p = 0.81). Cell 31 words this correctly ("negative").
  - **Cells 31 and 30, and the record:** "Without the three sessions whose ripples fail the clock check". Only two of the three are in the analysis (fCamk5 sess10 has under 50 first-epoch ripples). n drops by 111 = 70 + 41.
- **Cell 24:** "none of the 364 tests passes, so false positives do not inflate these fractions." The sham tests were run on PreStim only (cell 23), so they cover reading (a). The outcome rests on reading (b), which has no sham test.
- **Cell 57:** "Leaving the laps without stimulation out of the control maps changes little (p = 0.059 and 0.39)". Also the record's fig3f response that this variant was added. The variant cannot differ: dark windows exist only next to deposited pulses, so unstimulated laps already contribute no control time. The control medians are identical (0.714 and 0.527, cell 56).
- **README row:** "Ripple cofiring tracks spatial overlap for place cell pairs only | Reproduced". Cell 62 contradicts "only": place/non-place pairs give rho 0.062 against 0.060 for place pairs.
- **README row:** "Spatial information, control against light | Reproduced" and the Summary row for fig3g: see my disagreement above.
- I checked every other sentence of the Result cells, the Summary, the README and the record's notes against the printed outputs, and they are supported.
- **My round-1 reasons:** the record states them faithfully, close to my own words. It adds the relevant problem numbers (fig1e: 5; fig2b: 4; figs11: 1 and 2; fig3c: 3; fig3f: 10 and 7; fig3g: 7; figs9: 11). It drops the round-1 cell numbers, which would be stale now anyway.

## 3. Round-1 points

**Resolved:**
- **1 (missing pulses).** The device lists 12 uLEDs, the files hold 6 series, and deposited pulses come at 5.76 and 7.50 per s. Control time is now restricted to the dark windows.
- **2 (field rule).** `find_fields` now has the sub-field and dip rules; changing the rule alone moves 1 cell.
- **4 (theta).** The LFP rate and start are now read from the file and checked, the ripple-power check is repeated inside the Maze epoch, control-window spikes have a circular mean of 128 and 130°, and the theta-band light artifact is small.
- **5 (chance level).** N_BOOT is now 500, and 0 of 364 sham tests pass.
- **6 (fig2e ratio).** Now stated in the notes.
- **8 (fig4d).** Moot, since the outcome is now not_reproduced.
- **9 (figs10 unlabelled first epoch).** The variant restricted to labelled sessions gives -0.450.
- **10 (fig3f halves).** Resolved by construction, as above.
- **11 (figs9).** The proxy and the units columns are now printed.
- **12 (paper's counts).** Now recorded as a finding.
- **Section C items.** All answered except the Methods.

**Remaining, bearing on a conclusion:**
1. **fig3g (problem 7).** The outcome should be partially_reproduced, as argued above.
2. **No chance level for reading-(a) light fields.** This affects fig3c reading (a), and the unmasked groups in fig3e to fig3g. Reading-(a) light maps use only the uLEDs each cell responds to, so they have less time than the all-uLED light maps (12.1% and 10.7% of lap time, cell 35). Yet the thinned null (15.8%, cell 49) is matched to the all-uLED time of reading (b). All 7 unmasked cells have light fields in both directions (14 field directions, cell 51), against 70 directions for 48 place cells. Noise fields from sparse maps may explain part of the 77.8%.
3. **Problem 3 (two sessions, one mouse).** The record now states it, with intervals. Still, fig3a and fig4c changed outcome with the place-cell calls alone, and fig4c rests on sess9.
4. **Minor: the dark-window premise.** It assumes every offset is at least 20 ms. In PreStim, 3 to 4% of deposited end-to-start offsets are under 10 ms or negative (cell 11), so the stated protocol does not hold exactly.
5. **Methods.** The supplement is still unavailable, so the response test, field rule and control rule remain unchecked against the paper.

## End of run

15 turns, 3 minutes, result: success.
