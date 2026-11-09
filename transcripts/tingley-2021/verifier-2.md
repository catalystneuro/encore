# 000233 · verifier-2 · run 40771954557

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 644
drwxr-xr-x 6 runner runner    4096 Oct 28 21:40 .
drwxr-xr-x 7 runner runner    4096 Oct 28 21:40 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 28 21:26 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 28 21:26 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 28 21:40 .claude
-rw-r--r-- 1 runner runner       0 Oct 28 21:40 .env
-rw-r--r-- 1 runner runner       0 Oct 28 21:40 .env.development
-rw-r--r-- 1 runner runner       0 Oct 28 21:40 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 28 21:40 .env.local
-rw-r--r-- 1 runner runner       0 Oct 28 21:40 .env.production
-rw-r--r-- 1 runner runner       0 Oct 28 21:40 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 28 21:40 .env.test
-rw-r--r-- 1 runner runner       0 Oct 28 21:40 .env.test.local
drwx------ 2 runner runner    4096 Oct 28 21:40 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 28 21:26 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 28 21:26 .github
-rw-r--r-- 1 runner runner       0 Oct 28 21:40 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 28 21:26 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 28 21:26 .mcp.json
[... 106 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; cat 000233-tingley-2021-01.yaml
```

```
<persisted-output>
Output too large (53.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/8a75713d-f994-47ac-87ee-6b93ff6aa976/tool-results/boxt2lz2q.txt

Preview (first 2KB):
# Tingley, McClain, Kaya, Carpenter & Buzsáki (2021) from dandiset 000233

Tests the findings of [Tingley et al. (2021)](https://doi.org/10.1038/s41586-021-03811-w) that can
be tested on [DANDI:000233](https://dandiarchive.org/dandiset/000233/0.250624.0414), which holds
CA1 LFP, detected SPW-Rs, the glucose sensor current, a head accelerometer and, for six rats, sleep
states, from 25 rats. It holds no spike units, stimulation times, CNO or vehicle labels, meal times
or cohort labels, so the optogenetic, DREADD, fasting and unit findings cannot be tested.

| Claim | Outcome |
|---|---|
| SPW-R rate predicts later glucose decreases (R -0.21 at 10.7 min) | Reproduced, under 3 of 16 readings, resting on an assumption |
| The correlation at 10 min exceeds circular shuffles | Reproduced |
| Clustered SPW-Rs are followed by a larger glucose decrease | Reproduced |
| Interval, amplitude, duration, frequency rank in that order | Partially reproduced |
| Phase dispersion of glucose drops more after higher SPW-R rates | Not reproduced |
| Power-power and phase-power coupling, SPW-R rhythm faster | Partially reproduced |
[... 13 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "README.md"
}
```

```
1	# Tingley, McClain, Kaya, Carpenter & Buzsáki (2021) from dandiset 000233
2	
3	Tests the findings of [Tingley et al. (2021)](https://doi.org/10.1038/s41586-021-03811-w) that can
4	be tested on [DANDI:000233](https://dandiarchive.org/dandiset/000233/0.250624.0414), which holds
5	CA1 LFP, detected SPW-Rs, the glucose sensor current, a head accelerometer and, for six rats, sleep
6	states, from 25 rats. It holds no spike units, stimulation times, CNO or vehicle labels, meal times
7	or cohort labels, so the optogenetic, DREADD, fasting and unit findings cannot be tested.
8	
9	| Claim | Outcome |
10	|---|---|
11	| SPW-R rate predicts later glucose decreases (R -0.21 at 10.7 min) | Reproduced, under 3 of 16 readings, resting on an assumption |
12	| The correlation at 10 min exceeds circular shuffles | Reproduced |
13	| Clustered SPW-Rs are followed by a larger glucose decrease | Reproduced |
14	| Interval, amplitude, duration, frequency rank in that order | Partially reproduced |
15	| Phase dispersion of glucose drops more after higher SPW-R rates | Not reproduced |
16	| Power-power and phase-power coupling, SPW-R rhythm faster | Partially reproduced |
17	| Glucose oscillates at about 60 min | Not reproduced |
18	| Glucose is circadian and rises after meals | Blocked: data missing |
19	| The sensor current decays over days, its fluctuations do not | Reproduced |
20	| 9.5 SPW-Rs per minute, about 14,000 a day | Reproduced |
[... 26 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "000233-tingley-2021-01.yaml"
}
```

```
1	schema_version: 2
2	id: 000233-tingley-2021-01
3	dataset:
4	  archive: dandi
5	  id: "000233"
6	  version: 0.250624.0414
7	  doi: 10.48324/dandi.000233/0.250624.0414
8	paper: doi:10.1038/s41586-021-03811-w
9	date: 2026-10-28
10	entry: 000233-tingley-2021
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
[... 840 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF' > $TMPDIR/nb.txt
import json
nb=json.load(open('reproduce_tingley_2021.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f"\n######## CELL {i} [{c['cell_type']}]")
    src=''.join(c['source'])
    if c['cell_type']=='code' and len(src)>3000: src=src[:3000]+'\n...[src truncated]'
    print(src)
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--'); print(''.join(o['text']))
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d and 'image/png' not in d: print('--OUT--'); print(''.join(d['text/plain']))
            elif 'image/png' in d: print('--IMG--')
        elif o.get('output_type')=='error': print('--ERR--', o.get('ename'), o.get('evalue'))
EOF
wc -l $TMPDIR/nb.txt; grep -n "######## CELL" $TMPDIR/nb.txt | head -80
```

```
2388 /tmp/claude-1001/nb.txt
2:######## CELL 0 [markdown]
48:######## CELL 1 [code]
65:######## CELL 2 [code]
77:######## CELL 3 [markdown]
83:######## CELL 4 [code]
163:######## CELL 5 [markdown]
179:######## CELL 6 [code]
256:######## CELL 7 [markdown]
261:######## CELL 8 [code]
307:######## CELL 9 [markdown]
319:######## CELL 10 [code]
354:######## CELL 11 [markdown]
361:######## CELL 12 [code]
445:######## CELL 13 [markdown]
462:######## CELL 14 [code]
517:######## CELL 15 [markdown]
525:######## CELL 16 [markdown]
544:######## CELL 17 [code]
588:######## CELL 18 [code]
[... 53 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "limit": 830
}
```

```
File content (26149 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "limit": 560
}
```

```
1	
2	######## CELL 0 [markdown]
3	# Reproducing Tingley et al. (2021) from dandiset 000233
4	
5	**Paper.** Tingley D, McClain K, Kaya E, Carpenter J, Buzsáki G (2021). A metabolic function of
6	the hippocampal sharp wave-ripple. *Nature* 597, 82-86.
7	[doi:10.1038/s41586-021-03811-w](https://doi.org/10.1038/s41586-021-03811-w). The claims file was
8	written from the accepted author manuscript in PubMed Central (PMC9214835) with its Methods,
9	Extended Data legends and Supplementary Information.
10	
11	**Dandiset.** [DANDI:000233](https://dandiarchive.org/dandiset/000233/0.250624.0414), version
12	0.250624.0414. The paper cites no DANDI version (its data statement points to the lab's server).
13	This is the most recent published version; the earlier one, 0.230223.0815, lists the same 345
14	files with the same sizes, so the choice does not change the data.
15	
16	**What the dandiset holds.** 345 NWB files from 25 rats: CA1 LFP at 1,250 Hz, tables of detected
17	SPW-Rs, the iPro2 glucose sensor current, a head accelerometer, and sleep states for six rats. It
18	holds no spike units, no optogenetic stimulation times, no CNO or vehicle labels and injection
19	times, no meal times, and no cohort labels, so the optogenetic, DREADD, fasting and unit claims
20	cannot be tested.
[... 540 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 560,
 "limit": 420
}
```

```
560	    return out
561	
562	LAG_MIN = S.LAGS * 5
563	CC = {}
564	for s in RATS:
565	    d = SUBJ[s]
566	    for dname, bb in (("raw", d["b"]), ("highpass", highpass(d["b"]))):
567	        for m in ("pearson", "spearman"):
568	            CC[(s, dname, m, "rat")] = S.xcorr(bb, method=m)
569	            sess = per_session(bb, d["iv"])
570	            CC[(s, dname, m, "session")] = (np.nanmean([S.xcorr(x, method=m) for x in sess], axis=0)
571	                                            if sess else np.full(len(S.LAGS), np.nan))
572	
573	def peak(cc, lag_range):
574	    sel = LAG_MIN >= 0 if lag_range == "0..+100" else np.ones(len(LAG_MIN), bool)
575	    if np.all(np.isnan(cc[sel])):
576	        return np.nan, np.nan
577	    i = np.nanargmin(np.where(sel, cc, np.nan))
578	    return cc[i], LAG_MIN[i]
579	
[... 400 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 979,
 "limit": 400
}
```

```
979	    ok = idx < len(b)
980	    idx = np.where(ok, idx, 0)
981	    inside = ok & (b.t.values[idx] - e.t.values < S.STEP)
982	    e["delta_10"] = np.where(inside, b.delta_10.values[idx], np.nan)
983	    e["rat"] = s
984	    evs.append(e[np.isfinite(e.delta_10)])
985	evs = pd.concat(evs)
986	evs["duration_ms"] = 1000 * evs.duration
987	print(f"{len(evs)} SPW-Rs from {evs.rat.nunique()} rats with a delta current 10 min later")
988	feats = {"interval": "interval", "amplitude": "peak_normed_power", "duration": "duration_ms", "frequency": "peak_frequency"}
989	res = []
990	for nb, label in ((10, "a: deciles"), (20, "b: 5-percentile bins")):
991	    for f, col in feats.items():
992	        x = evs[[col, "delta_10"]].dropna()
993	        q = pd.qcut(x[col].rank(method="first"), nb, labels=False)
994	        m = x.groupby(q).delta_10.mean()
995	        res.append({"bins": label, "feature": f, "n": len(x), "range_nA": m.max() - m.min(),
996	                    "lowest_bin_mean": m.iloc[0], "highest_bin_mean": m.iloc[-1], "min_bin": int(m.idxmin()), "max_bin": int(m.idxmax())})
997	R4 = pd.DataFrame(res)
998	print(R4.round(4).to_string())
[... 380 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1378,
 "limit": 420
}
```

```
1378	        ac.append(c)
1379	    ac_rows.append(np.mean(ac, axis=0)); used.append(s)
1380	F1 = f[1:]; period = 1 / F1 / 60
1381	resid = []
1382	for p in psd_rows:
1383	    lp = np.log10(p[1:]); coef = np.polyfit(np.log10(F1), lp, 1)
1384	    resid.append(lp - np.polyval(coef, np.log10(F1)))
1385	resid = np.array(resid); mres = resid.mean(axis=0)
1386	print(f"{len(used)} subjects: {used}")
1387	tbl = pd.DataFrame({"period_min": period, "mean_residual_log10": mres, "rats_positive": (resid > 0).sum(axis=0)})
1388	print(tbl[(tbl.period_min >= 10) & (tbl.period_min <= 300)].round(3).to_string())
1389	band = (period >= 15) & (period <= 90)
1390	print(f"residual over 15-90 min: mean {mres[band].mean():.3f}, positive at {np.sum(mres[band] > 0)} of {band.sum()} frequencies")
1391	ipk = np.argmax(np.where((period >= 10) & (period <= 300), mres, -np.inf))
1392	print(f"peak of the mean residual at {period[ipk]:.1f} min")
1393	mac = np.mean(ac_rows, axis=0); lags_min = np.arange(37) * 5
1394	pk, _ = signal.find_peaks(mac)
1395	print("mean autocorrelogram:", dict(zip(lags_min[:25], np.round(mac[:25], 3))))
1396	print("first side peak of the mean autocorrelogram at", lags_min[pk[0]] if len(pk) else None, "min",
1397	      f"(value {mac[pk[0]]:.3f})" if len(pk) else "")
[... 400 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1797,
 "limit": 600
}
```

```
1797	up to 258 in a minute; minutes with more than 40 occur in 18 of 22 subjects. With all stored events
1798	the mean is 11.07 per minute and 15,941 per day, outside the tolerances; CGM1 alone gives 10.76 per
1799	minute and 15,494 per day.
1800	
1801	######## CELL 49 [markdown]
1802	## supp-ripples-stable-across-days
1803	
1804	> In each rat the shape, amplitude and rate of SPW-Rs are consistent across days.
1805	
1806	Per rat and calendar day (days with at least 6 h of CA1 recording, a standard choice), the median
1807	amplitude (`peak_normed_power`, the Methods' maximum normalized squared signal; `peak_amplitude`
1808	shown as a variant), median duration and mean rate; Spearman correlation with day, and whether
1809	every daily value stays within 20% of the rat's overall median (claims file).
1810	
1811	######## CELL 50 [code]
1812	rows = []
1813	for s, d in SUBJ.items():
1814	    if d["ev"] is None:
1815	        continue
1816	    e = d["ev"].copy(); e["day"] = S.clock(d["ref"], e.t).normalize()
[... 573 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import yaml
c=yaml.safe_load(open('10.1038-s41586-021-03811-w.yaml'))
print(c.keys() if isinstance(c,dict) else type(c))
cl=c['claims']; print(len(cl), 'claims')
a=yaml.safe_load(open('000233-tingley-2021-01.yaml'))
o=a['outcomes']; print(len(o),'outcomes')
from collections import Counter; print(Counter(x['outcome'] for x in o))
print(set(x['id'] for x in cl)^set(x['claim'] for x in o))
print([x['claim'] for x in o if x.get('assumed')])
print(len(a['verifications'][0]['results']))
"
python3 -c "
import yaml
c=yaml.safe_load(open('10.1038-s41586-021-03811-w.yaml'))
for x in c['claims']:
  if x['id'] in ('edfig1-glucose-circadian-meals','edfig1-glucose-rhythm','edfig6-ripple-rate-best-predictor','supp-ripples-stable-across-days','edfig9-dorsal-ventral'):
    print(yaml.safe_dump(x, width=150, sort_keys=False))
"
```

```
dict_keys(['schema_version', 'dataset', 'paper', 'claims', 'checks'])
35 claims
35 outcomes
Counter({'blocked': 21, 'reproduced': 7, 'not_reproduced': 4, 'partially_reproduced': 3})
set()
['fig2-ripple-rate-predicts-glucose']
35
id: edfig1-glucose-rhythm
statement: Interstitial glucose fluctuations show an approximately 60-min oscillation, with power elevated above a linear best fit to the spectrum at periods
  of 15 to 90 min.
source: Results, SPW-Rs phase reset glucose oscillations, paragraph 2; Extended Data Fig. 1g-i
quote: Because interstitial glucose fluctuations displayed an approximately 60-min oscillation
expected:
- quantity: period of the glucose oscillation
  value: 60
  tolerance: 6
  unit: min
criterion: As in Extended Data Fig. 1g-h, power spectral density of delta current per rat, a linear best fit subtracted, averaged across rats (8 rats in
  the legend). OPEN, the axes of the fit are not given; log-log axes are used as the standard choice. Reproduced when the residual power is positive over
  15 to 90 min and its peak, or the first side peak of the mean autocorrelogram (Extended Data Fig. 1i), lies within tolerance of 60 min.
[... 48 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "def time_read" -A 15 sprglu.py; grep -n "def repaired_glucose" -A 30 sprglu.py | head -45
```

```
370:def time_read(asset_id, seconds=1800):
371-    """Seconds taken to read the first `seconds` of LFP (all channels) and of accelerometer of one file.
372-
373-    Used only to estimate the cost of predictors computed from these signals."""
374-    import time
375-    with open_h5(asset_id) as h:
376-        t0 = time.time()
377-        h["processing/ecephys/LFP/ElectricalSeriesLFP/data"][: int(LFP_RATE * seconds), :]
378-        t1 = time.time()
379-        acc = h["acquisition/Accelerometer"]
380-        acc["data"][: int(acc["starting_time"].attrs["rate"] * seconds), :]
381-        return t1 - t0, time.time() - t1
326:def repaired_glucose(reference, glu):
327-    """Glucose readings with dates repaired when swapping day and month leaves fewer breaks.
328-
329-    Returns (DataFrame of runs, whether the swap was applied, breaks as stored, breaks swapped).
330-    """
331-    t2 = swap_day_month(reference, glu["t"])
332-    b1, b2 = breaks(glu["t"]), breaks(t2)
333-    use = b2 < b1
[... 23 more lines not kept]
```

**Agent**

**Verifier report, round 2: Tingley et al. 2021 (doi:10.1038/s41586-021-03811-w) on DANDI:000233 v0.250624.0414**

The claims file holds 35 claims, and the attempt record has 35 outcomes: 7 reproduced, 3 partially reproduced, 4 not reproduced and 21 blocked. One outcome is marked `assumed: true` (fig2-ripple-rate-predicts-glucose).

### 1. Outcomes

I agree with all 35 outcomes.

- **fig2-ripple-rate-predicts-glucose (reproduced, assumed).** I agree. The assumption is stated in the deviations and is reasonable: the SPW-R count of a 5-min interval is paired with the glucose change over that same interval. The two alignments one reading either side are shown, and the outcome depends on which is used. The match remains fragile (see 3).
- **edfig1-glucose-circadian-meals (blocked, data_missing).** In round 1 I said not reproduced. I now agree with blocked:
  - both expected values concern meals, which cannot be tested;
  - the criterion's pooled ANOVA fails (cell 41, p = 0.986), but a within-subject version of the same data finds an hour-of-day effect (ANOVA p = 0.024, Friedman p = 5.2e-05).
  - Claims-file note: the pooled test is the reader's own choice ("a choice made here"), not something the paper misread. With subject offsets left in, it can hardly detect a circadian effect.
- **edfig1-glucose-rhythm (not reproduced).** I agree. It is now changed from partially reproduced, and none of the 12 variants (cell 38) meets either condition of the criterion.
- **All other outcomes** match my round-1 outcomes.
- **Assumptions not marked as such:**
  - fig2ef, fig2g, edfig4-ripple-features, edfig4-nrem-wake and edfig4-no-hour-differs all use the same alignment, but none is marked `assumed` and none has an alignment variant (see 3).
  - The supp-ripple-rate outcome depends on keeping only events of at least 5 s.d.:
    - with that threshold: 10.19 per minute, inside the tolerance;
    - with all stored events: 11.07 per minute, outside it.
  - The threshold comes from the Methods and the record states the dependence, but it has the same status as an assumption and could be flagged `assumed: true`.

### 2. Statements the numbers do not support

1. **Cell 69, and the record's notes for edfig6-ripple-rate-best-predictor.**
   - Cell 69 says: "The timing above puts the reading alone at about 6 h of LFP and 2 h of accelerometer one file at a time."
   - The notes say: "5.7 h of LFP and 2.1 h of accelerometer for 1717 h, one file at a time."
   - Cell 68 printed "LFP 77.9 h, accelerometer 23.2 h of reading".
   - The round-1 response, "The markdown now matches the printed timing", is therefore not true of this run.
   - Cell 68 also shows that the single 30-min read took 106 s, while the 8 parallel pieces took 72.5 s in total, about 9 s each. The two timings disagree by about a factor of ten, and this is not discussed.
2. **Cell 39, and the record's notes for edfig1-glucose-rhythm:** "An oscillation of about 50 min is present." The printed numbers do not show one:
   - the residual is positive over a broad hump from 22 to 131 min;
   - the mean autocorrelogram at a 50-min lag is −0.06;
   - its first side peak is at 70 min, with a value of 0.013.
3. **Cell 51, and the record's notes for supp-ripples-stable-across-days:** "With 3 to 5 days a Spearman test rarely reaches p < 0.05." Cell 50 shows the opposite:
   - every perfectly monotone 3- or 4-day series gets p = 0.000: CGM46 and CGM51 for amplitude in µV, and CGM49, CGM51 and CGM52 for rate;
   - this comes from scipy's asymptotic p; with exact p, n = 4 with rho = −1 gives 0.083;
   - so with 3 days, p < 0.05 occurs one time in three by chance.
   - Both rate "failures" are artefacts of this: CGM52 (n = 4, p = 0.000) and CGM2 (n = 5, rho 0.9, p = 0.037, exact p about 0.08).
   - The outcome does not change. My own round-1 point B14 made the same error.
4. **The record's notes for edfig9-dorsal-ventral:** "In CGM37 and CGM48 the glucose readings cover other days than the electrophysiology." Cell 14 gives CGM48 2.2 h with both signals, and CGM48 is one of the 18 rats. The outcome does not change.
5. **README:** "It takes about seven minutes." Cell 70 printed 8.4 min.
6. **Cell 36 (minor wording):** "Above the diagonal" is used for "glucose period longer than SPW-R period". In the printed matrix, with glucose periods in the rows, those cells are below the diagonal.

I checked every other sentence of the Result conclusions, the Summary, the README and the record's notes against cells 2–68, and they match the printed outputs. That includes the counts, ranges, p values, lag ranges, the 13 failing fig2 combinations (15.8–33.1 min), the 7–10 rats peaking at +5 to +15 min, and the 19 other blocked claims.

The record's round-1 reasons restate my report faithfully, merging each B-point into the claim it concerns. Nothing is misattributed.

### 3. Round-1 points

**Resolved**
- **B2:** the reading (a) exclusion of CNO days and stimulation periods is now stated.
- **B4:** 12 fit variants were added.
- **B5:** start-to-start, stop-to-stop and stop-to-next-start intervals were added, and the 20-ms floor of the merging rule is shown.
- **B6:** both signals are now filtered only where both are recorded, with 100 shuffles and the hours per rat printed.
- **B7:** a bootstrap over rats was added.
- **B8:** missing rat-hours are now left out.
- **B9:** the within-subject test was added, and I accept the blocked outcome.
- **B10:** the CGM32 dates are documented.
- **B11:** the high-pass reading is now stated to nearly repeat the raw one.
- **B12:** the mean-over-offsets variant was added.
- **B13:** prominence and rank of the peaks were added.
- **B14:** the dependence on the criterion's "or" is stated, though the reasoning given is wrong (2.3).
- **C, condition groups and detector parameters:** checked and absent.
- **C, clock alignment:** stated as unverifiable (cell 15).

**Remaining, bearing on a conclusion**
1. **fig2 fragility (B1).** It is now reported in full, but the substance stands:
   - the match holds in 3 of 16 combinations, and in 1 of 16 once rats with less than 6 h of both signals are dropped;
   - per-rat lags spread from −100 to +80 min;
   - the outcome flips with the alignment.
   The "reproduced" outcome rests on a minority of readings.
2. **The alignment assumption reaches further than fig2.** fig2ef, fig2g, edfig4-ripple-features, edfig4-nrem-wake and edfig4-no-hour-differs use the same +10-min pairing, with no variant shown and no `assumed` flag. fig2g is the most exposed to a one-reading shift:
   - Welch p = 0.059;
   - the curve is not monotonic;
   - 3 of 13 rats are not negative.
3. **edfig6 blocking (B3), partly resolved.**
   - The timing text contradicts the printed timing (2.1).
   - The scaling assumes 4 processes, although the reading is network-bound and `read_all` already runs 16.
   - At 7.1 s per hour, the 3-rat subset with stored brain states (557 h, about 66 min) could come in under 30 min with about 3 times more parallelism. That would allow a partial test of three claims that are now blocked.
4. **Not checked by me:** the figures. I read only the text outputs.

## End of run

14 turns, 3 minutes, result: success.
