# henze-2000 · author-revise-2 · run 42709042266

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/henze-2000/verifier-2-report.md; ls entries/henze-2000 entries/henze-2000/*;
```

```
Mon Nov  9 22:14:11 UTC 2026
**Round-2 verification: Henze et al. (2000) on CRCNS hc-1, attempt henze-2000-01**

**1. Outcomes and assumptions** (21 claims in the claims file, 21 outcomes in the attempt record)

| Claim | Record | I agree? | Comment |
|---|---|---|---|
| sample-cells | not_reproduced | yes | Cell 21. |
| fig1c-start-end-timing | not_reproduced | yes | Cell 26: the start lead is never in tolerance, under any of the four site rules (S1 to S4). |
| ap-duration-match | reproduced | yes | Cell 29: 1, 6, 1 and 2 readings pass under S3, S1, S2 and S4. Under S3 the extracellular duration SD is 0.59 against the paper's 0.19, but the criterion tests means only. |
| duration-correlation | reproduced, assumed | yes, with a reservation | The assumption (rule S3) is stated. It is reasonable in that it agrees with the paper's own label of D53. The reservation is that the result rests on D12821, a cell S3 adds. Its intracellular duration is 5.70 ms against the paper's 1.28 ± 0.18 (cell 29). From cell 29's per-cell durations (all spikes, both starts by dV/dt, end at threshold) I get R = 0.742, which matches cell 32. Without D12821 it drops to R = 0.02, and without D12821 and D8131 to 0.46. The reproducing readings share D12821's intracellular duration, so they are probably driven the same way, but cell 32 does not print the per-cell values that would show it. The record should say this. |
| neg-peak-precedes-intra-peak | reproduced | yes | Cell 35. |
| fig1c-derivative-mismatch | reproduced | yes | Cell 38. |
| notch-and-ahp-landmarks | not_reproduced | yes | Cell 42. |
| fig2-interneuron-narrow | blocked (metadata_insufficient) | yes | |
| fig3b-latency-vs-amplitude | reproduced | yes | Cell 45: holds under all four rules. |
| fig3a-example-pair | not_reproduced, assumed | yes | The pair identification is stated and reasonable. Cell 45 shows the 0.975 ms latency of D11222 is not a window-edge artefact. |
| fig3c-backprop-velocity | not_reproduced | yes | Cell 52: 0
[... 51 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "" docs/protocol.md | sed -n '1,400p' | grep -n -i -E "step 6|round 2|proposed|verifications|Hand over|Time" | head -50; wc -l docs/protocol.md
```

```
31:31:[Agent run](../.github/workflows/attempt.yml) workflow, one role at a time:
184:184:not say what the paper says (author, step 1.6, and "Hand over for
199:199:(step 6).
201:201:**Time.** An author run is stopped five hours after it starts, and whatever
203:203:time by which to finish. Check the clock (`date -u`) between steps. When that
204:204:time comes, stop analysing and finish: record each claim not yet tested as
207:207:with some claims blocked for time is worth more than a run that is cut off.
286:286:     (step 6; see also chance levels, under "Record the attempt").
293:293:     within the time limit. Say what was tried. For an outside input that is
336:336:     claims file (reader, step 6), and a later run, `author-answers`,
348:348:sessions, decoding the annotations with the labels shifted in time), and name any
379:379:  file's contents at a time; and run in parallel only as many as fit. A run
381:381:  2026-11-06 an author run was killed nine times this way, each time on its
386:386:  works; do not re-run whole notebooks to test a change. Time the subset and
389:389:  notebook limit, over the time left (see "Time" above), or over 12 GB of
647 docs/protocol.md
```

**Agent calls Bash**

```bash
sed -n 395,647p docs/protocol.md
```

```
1. **Header.** The paper, the dataset and version, the text the claims file
   was written from, and a table of the claims saying which are tested and which blocked.
2. **Data check.** A cell tagged `sanity` that prints what was loaded: counts
   by subject, session and condition, and the ranges and units of every
   variable used. State each check of the metadata against the data.
3. **One section per tested claim.** Quote the claim. The cells that show the
   result carry the tag `claim:<id>`.
   - Print the numbers the conclusion rests on; a figure alone is not enough.
   - Give the range of every plotted quantity, or say how many points fall
     outside the axes.
   - When cells or trials come from several animals, break the result down by
     animal, or by session when there is one subject.
   - When a threshold or criterion is a choice, show how the result changes
     with it. Give every number its null or reference where the conclusion
     compares it with chance.
   - Report how much was dropped: units, trials, features, and fits that
     failed, did not converge or had nothing to fit.
   - Quote a bound or an effect size for every variant you show, not only the
     main one.
   - End with a short conclusion beginning "**Result: ...**". Every sentence
[... 232 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 170,394p docs/protocol.md
```

```
that each statement says what the paper says, no more and no less; that each
quote is word for word (the quote checker, `tools/claims_check.py`, does this
mechanically); that each source points at the place; that the statistics are
the paper's and are results, not thresholds; that every part of every
criterion's method is taken from the paper or its code, as cited; and that the
paper's main findings each have a claim. The checker corrects what it can
show is wrong, and records each change, with its reason, under `checks` at
the end of the file. A claims file is ready for an attempt when its last check
says so.

### 6. Answer questions

A reader is asked only when the author or a verifier believes the claims file
misreads the paper: a wrong expected value, the wrong panel, a claim that does
not say what the paper says (author, step 1.6, and "Hand over for
verification"). A method detail the claims file lacks is not asked: the author
takes it from the paper. The reader, who has not seen the data, checks each
question against the paper and decides whether the claims file is to change.
Where it is, the reader amends the claim, and the question's `answer` says
what changed and why, citing the passage; where it is not, the answer says why
[... 205 more lines not kept]
```

**Agent calls Bash**

```bash
ls attempts | grep henze; wc -l attempts/henze-2000-01.yaml; ls executed/henze-2000/ 2>/dev/null; cat questions/henze-2000.yaml 2>/dev/null | head -50
```

```
henze-2000-01.yaml
578 attempts/henze-2000-01.yaml
```

**Agent calls Read**

```json
{
 "file_path": "attempts/henze-2000-01.yaml"
}
```

```
1	schema_version: 3
2	id: henze-2000-01
3	datasets:
4	- archive: crcns
5	  id: hc-1
6	  version: unversioned
7	  doi: 10.6080/K02Z13FP
8	  relation: primary
9	paper: doi:10.1152/jn.2000.84.1.390
10	date: 2026-11-09
11	entry: henze-2000
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-14
20	  runner:
[... 559 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/henze-2000; python - <<'E'
import json
nb=json.load(open('reproduce_henze_2000.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    print(f"--- cell {i} [{c['cell_type']}] tags={c.get('metadata',{}).get('tags')} len={len(s)}")
    print(s[:300])
E
wc -l hc1.py; cat entry.yaml
```

```
--- cell 0 [markdown] tags=None len=2602
# Henze et al. (2000) on CRCNS hc-1

Paper: Henze, Borhegyi, Csicsvari, Mamiya, Harris and Buzsaki (2000), "Intracellular features
predicted by extracellular recordings in the hippocampus in vivo", J Neurophysiol 84:390-400,
doi:10.1152/jn.2000.84.1.390. The claims file `claims/henze-2000.yaml` was 
--- cell 1 [code] tags=None len=613
import io
import re
import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

import hc1

pd.set_option("display.width", 200)
pd.set_option("display.max_rows", 200)
[... 494 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'E'
import json
nb=json.load(open('reproduce_henze_2000.ipynb'))
for i in [24,29,30,32,33,41,54,55,56,57,58,59,60,61,62]:
    c=nb['cells'][i]
    print(f"=== cell {i}"); print(''.join(c['source']))
E
```

```
=== cell 24
def timing(fo, group, ch=None):
    w = hc1.cell_waves(R[fo]["files"], group, DROP)
    if w is None:
        return []
    im = hc1.ic_measures(w["ic"])
    best = T.loc[fo, "best"] if ch is None else ch
    best = int(best)
    em = hc1.ec_measures(w["ec"][best], w["noise"][best])
    out = []
    for ics in ("a", "b"):
        for ecs in ("a", "b"):
            for end in ("thr", "base"):
                ti0 = im[f"t_start_{ics}"]
                ti1 = im[f"t_end_{end}_{ics}"]
                te0 = em[f"t_start_{ecs}"]
                te1 = em["t_pos"]
                out.append(dict(folder=fo, spikes=group, channel=best, ic_start=ics, ec_start=ecs, ic_end=end, n=w["n"],
                                lead_start=ti0 - te0, lead_end=ti1 - te1, dur_ic=ti1 - ti0, dur_ec=te1 - te0,
                                latency=im["t_peak"] - em["t_neg"]))
[... 276 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import yaml
c=yaml.safe_load(open('claims/henze-2000.yaml'))
for cl in c['claims']:
    if cl['id'] in ('fig4d-amplitude-correlation','fig4bc-burst-attenuation','duration-correlation'):
        print(yaml.safe_dump(cl, sort_keys=False, width=110))
E
grep -n "def per_spike_ic" -A40 entries/henze-2000/hc1.py | grep -n -i "base"
```

```
id: duration-correlation
statement: Across somatic cells, intracellular and extracellular spike durations are linearly related (R = 0.66,
  P < 0.03).
source: Results, Temporal relationship between extracellularly and intracellularly recorded action potentials, paragraph
  2
quote: As expected, there was a linear relationship between the intracellular and extracellular spike durations
  across individual cells
statistics:
- test: not named (a linear relationship with its R)
  statistic: R = 0.66
  p: 0.03
  p_relation: <
  n: 11 somatic pyramidal cells
expected:
  quantity: correlation coefficient R between intracellular and extracellular durations
  value: 0.66
  tolerance: 0.066
depends_on:
- ap-duration-match
criterion: The per-cell durations of ap-duration-match; a least-squares linear regression of one on the other, R
[... 58 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -A8 "O6" claims/henze-2000.yaml | head -40; sed -n 335,400p entries/henze-2000/hc1.py; grep -n "amp_base_a\|base_a\b\|\"base_a\"" entries/henze-2000/hc1.py
```

```
85:# at that band are used as they are. (O6) Action potential amplitude; readings (a) peak minus
86-# threshold (start), (b) peak minus the mean membrane potential in the 2 ms before the start.
87-# (O7) Extracellular spike amplitude; readings (a) negative to positive peak (the measure of the
88-# Fig. 5 analysis), (b) the initial negative peak against the pre-spike baseline (the measure
89-# the abstract and Fig. 4 discuss).
90-#
91-# Discrepancies in the paper: the back-propagation velocity is 1.61 m/s in the Results and
92-# Discussion and 1.68 m/s in the abstract; Figure 3B's legend counts "all 20 pyramidal cells" and
93-# the Results "all 21" (11 somatic plus 9 dendritic is 20, with the atypical cell 21); the Fig. 5
--
288:    amplitude (O6); dendritic and somatic as the Results define them. The paper reports no test;
289-    readings (a) Pearson, (b) Spearman correlation. Reproduced when, under one reading, the
290-    correlation is negative with two-sided P < 0.05 and the dendritic cells' median latency
291-    exceeds the somatic cells'; partially reproduced when only one of the two holds.
292-- id: fig3a-example-pair
293-  statement: In two cells impaled on the same track, a dendrite 240 um deeper than a soma, the
294-    extracellular peak led the intracellular peak by 0.55 ms in the dendritic recording and by
295-    0.28 ms in the somatic one.
296-  source: Results, Temporal relationship between extracellularly and intracellularly recorded action
--
[... 85 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/henze-2000; grep -n "def ic_measures" -A60 hc1.py | grep -n -i "base\|def \|start_a" | head -30; grep -n "per_spike_ic(" hc1.py
```

```
1:462:def ic_measures(v, t=GRID):
3:464-    start_a: first point of the run before the peak where dV/dt > 10 V/s (O4 a);
6:467-    end_base: return to the mean Vm of the 2 ms before the start (O4, "return to baseline");
7:468-    amp_thr: peak minus threshold (O6 a); amp_base: peak minus that baseline (O6 b);
30:491-                        f"t_end_base_{key}": np.nan, f"base_{key}": np.nan,
31:492-                        f"amp_thr_{key}": np.nan, f"amp_base_{key}": np.nan})
35:496-        base = v[bmask].mean()
38:499-        after2 = np.flatnonzero(v[pk:] <= base)
41:502-                    f"t_end_base_{key}": e2, f"base_{key}": base,
42:503-                    f"amp_thr_{key}": v[pk] - thr, f"amp_base_{key}": v[pk] - base})
57:518-def ec_measures(e, noise_sd, t=GRID, win=NEG_WIN):
59:520-    negative peak: the most prominent trough in `win` (ms); baseline: mean over `base_window`;
60:521-    start_a: last point before the negative peak within 2 SD of the baseline noise (O4 a);
328:    res["spike_ic"] = per_spike_ic(t, icw, sr)
345:def per_spike_ic(t, icw, sr):
```

**Agent calls Bash**

```bash
cd entries/henze-2000; python - <<'E'
import json
nb=json.load(open('reproduce_henze_2000.ipynb'))
for i in [0,67,68,69,71]:
    c=nb['cells'][i]
    print(f"=== cell {i}"); print(''.join(c['source']))
E
cat README.md
```

```
=== cell 0
# Henze et al. (2000) on CRCNS hc-1

Paper: Henze, Borhegyi, Csicsvari, Mamiya, Harris and Buzsaki (2000), "Intracellular features
predicted by extracellular recordings in the hippocampus in vivo", J Neurophysiol 84:390-400,
doi:10.1152/jn.2000.84.1.390. The claims file `claims/henze-2000.yaml` was written from the
version of record (Introduction, Methods, Results, Discussion and the legends of Figures 1 to 8;
the paper has no supplement and links no code).

Dataset: CRCNS hc-1, "Simultaneous intracellular and extracellular recordings in the
hippocampus of anesthetized rats", doi:10.6080/K02Z13FP, read anonymously from the public S3
bucket `crcnsarchive` under `hc-1/live/`. CRCNS data sets are not versioned
(docs/archives.md), so the version is recorded as `unversioned`, pinned by the MD5 sums of the
data set's `checksums.md5`, which the next cell prints for every file read. The `live` folder is
the only copy of the data; `hc-1/orig/ver_1_0/` holds only the documentation of version 1.0.
The data descriptor read is version 1.1 (April 21, 2021), which adds only a note that the
recording times in IntraExtra.xls are wrong in many cases. So the published files under
`live/` are the version used: there is no other.

| Claim | Tested or blocked |
[... 178 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/henze-2000; python - <<'E'
p='hc1.py'; s=open(p).read()
old='''    """Per-spike IC measures: peak (mV), pre-spike baseline (mean -3 to -1.5 ms), threshold
    (the potential at the first point of the run of dV/dt > 10 V/s that holds the maximal rate
    of rise in the 1.5 ms before the peak, as `ic_measures` start_a; NaN when the maximal rate is
    not above 10 V/s), maximal rising and falling slopes (V/s)."""
    dv = np.diff(icw, axis=1) * sr / 1000.0
    pk = np.argmin(np.abs(t))
    lo = max(pk - int(round(sr * 0.0015)), 0)
    peak = icw[:, pk]
    base = icw[:, (t >= -3) & (t <= -1.5)].mean(1)
    thr = np.full(len(icw), np.nan)
    kmax = lo + np.argmax(dv[:, lo:pk], axis=1)
    for i in range(len(icw)):
        k = kmax[i]
        if dv[i, k] <= 10:
            continue
        while k > lo and dv[i, k - 1] > 10:
            k -= 1
        thr[i] = icw[i, k]
'''
new='''    """Per-spike IC measures: peak (mV), threshold (the potential at the first point of the run
    of dV/dt > 10 V/s that holds the maximal rate of rise in the 1.5 ms before the peak, as
    `ic_measures` start_a; NaN when the maximal rate is not above 10 V/s), pre-spike baseline
    (mean of the 2 ms before that start, as the claims file's O6 b defines it; NaN with the
    threshold), maximal rising and falling slopes (V/s)."""
    dv = np.diff(icw, axis=1) * sr / 1000.0
    pk = np.argmin(np.abs(t))
    lo = max(pk - int(round(sr * 0.0015)), 0)
    n2 = int(round(sr * 0.002))
    peak = icw[:, pk]
    base = np.full(len(icw), np.nan)
    thr = np.full(len(icw), np.nan)
    kmax = lo + np.argmax(dv[:, lo:pk], axis=1)
    for i in range(len(icw)):
        k = kmax[i]
        if dv[i, k] <= 10:
            continue
        while k > lo and dv[i, k - 1] > 10:
            k -= 1
        thr[i] = icw[i, k]
        base[i] = icw[i, max(k - n2, 0):k].mean()
'''
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
E
grep -n "t = \|np.arange" hc1.py | head; grep -n "\[\"base\"\]\|\['base'\]" hc1.py reproduce_henze_2000.ipynb | head
```

```
66:GRID = np.round(np.arange(WIN[0] + 0.5, WIN[1] - 0.5 + GRID_DT / 2, GRID_DT), 6)
103:    out = []
110:            t = z.read(xml).decode("latin1")
263:        dist = np.min(np.abs(peaks[:, None] - edges[None, :]), axis=1) if len(peaks) else np.zeros(0)
289:    idx = peaks[:, None] + np.arange(i0, i1 + 1)[None, :]
292:    shift = int(round(0.025 * sr))
293:    ok_shift = peaks + shift + i1 < len(v)
319:        order[m] = np.arange(1, len(m) + 1)
321:    isi_next = np.r_[np.diff(peaks) / sr * 1000, np.inf]
322:    t = np.arange(i0, i1 + 1) / sr * 1000
```

**Agent calls Bash**

```bash
cd entries/henze-2000; grep -n "^WIN" hc1.py; python -c "
import json;nb=json.load(open('reproduce_henze_2000.ipynb'));print(''.join(nb['cells'][15]['source']));print(''.join(nb['cells'][14]['source']))"
```

```
64:WIN = (-4.0, 8.0)  # ms around the AP peak
for sr in (10000.0, 20000.0):
    ts = np.arange(-4, 8 + 1e-9, 1000 / sr)
    vs = -60 + 80 * np.exp(-(ts / 0.35) ** 2) * (ts <= 0) + 80 * np.exp(-ts / 0.6) * (ts > 0)
    r_ = hc1.per_spike_ic(ts, np.vstack([vs, vs + 5]), sr)
    print(f"{sr / 1000:.0f} kHz: threshold {np.round(r_['thr'], 2)} mV (resting -60 and -55 mV), peak {r_['peak']} mV")
for tn in (-0.3, -1.1, -1.3, -1.8):
    es = -100 * np.exp(-((GRID - tn) / 0.15) ** 2) + 30 * np.exp(-((GRID - tn - 0.6) / 0.4) ** 2)
    print(f"trough at {tn} ms: found at {hc1.ec_measures(es, 1.0)['t_neg']:.3f} ms (window -2 to +0.6), "
          f"{hc1.ec_measures(es, 1.0, win=(-1.0, 0.6))['t_neg']:.3f} ms (window -1 to +0.6)")
Checks of the helper's measures on synthetic waveforms. The per-spike threshold (`hc1.per_spike_ic`)
on a synthetic AP rising from -60 mV, sampled at 10 and 20 kHz; and the negative peak of
`hc1.ec_measures` on synthetic troughs at -0.3 to -1.8 ms from the AP peak, with the window used
here (-2 to +0.6 ms) and with the -1 to +0.6 ms window of the first round.
```

**Agent**

Now the notebook edits. I'll script them.

**Agent calls Bash**

```bash
cd entries/henze-2000; python - <<'E'
import json
p='reproduce_henze_2000.ipynb'
nb=json.load(open(p))
C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def setsrc(i,s): C[i]['source']=s.splitlines(keepends=True)
def rep(i,old,new):
    s=src(i); assert old in s,(i,old); setsrc(i,s.replace(old,new))
# cell 14/15 synthetic: baseline
rep(14,"on a synthetic AP rising from -60 mV, sampled at 10 and 20 kHz;","and pre-spike baseline (mean of the 2 ms before the threshold point) on a synthetic AP rising\nfrom -60 mV, sampled at 10 and 20 kHz;")
rep(15,"mV (resting -60 and -55 mV), peak {r_['peak']} mV\")","mV, baseline {np.round(r_['base'], 2)} mV \"\n          f\"(resting -60 and -55 mV), peak {r_['peak']} mV\")")
# cell 32: per-cell durations and leave-out
s=src(32)+'''
# Per-cell durations of the readings that reproduce, and R without D12821, whose intracellular duration
# is far above the paper's 1.28 +/- 0.18 ms, and without D12821 and D8131
rep_r = RRS[RRS.reproduced]
for _, r_ in rep_r.iterrows():
    tm = TMS[r_.rule]
    g = tm[(tm[keys] == r_[keys].values).all(axis=1)].dropna(subset=["dur_ic", "dur_ec"])
    print(f"rule {r_.rule}, reading {'/'.join(r_[keys])}:")
    print(g.set_index("folder")[["dur_ic", "dur_ec"]].T.round(3).to_string())
lo_rows = []
for k, tm in TMS.items():
    for kk, g in tm.groupby(keys):
        g = g.dropna(subset=["dur_ic", "dur_ec"])
        for drop_name, drop in (("none", []), ("D12821", ["d12821"]), ("D12821 and D8131", ["d12821", "d8131"])):
            h = g[~g.folder.isin(drop)]
            if len(h) < 3 or len(h) == len(g) and drop:
                continue
            lr = stats.linregress(h.dur_ic, h.dur_ec)
            lo_rows.append(dict(rule=k, **dict(zip(keys, kk)), left_out=drop_name, n=len(h), R=lr.rvalue, p=lr.pvalue))
LO = pd.DataFrame(lo_rows)
LO["reproduced"] = (LO.R > 0) & (LO.p < 0.03) & ((LO.R - 0.66).abs() <= 0.066)
LO["positive_sig"] = (LO.R > 0) & (LO.p < 0.03)
print("readings that reproduce with all cells, with D12821 and D8131 left out:")
idx = RRS[RRS.reproduced][["rule"] + keys]
print(LO.merge(idx, on=["rule"] + keys).round(4).to_string())
print("counts over all 16 readings per rule, by cells left out:")
print(LO.groupby(["rule", "left_out"]).agg(n=("n", "max"), readings=("R", "count"), reproduced=("reproduced", "sum"),
                                           positive_sig=("positive_sig", "sum"), R_min=("R", "min"), R_max=("R", "max")).round(3).to_string())
print("R of the readings positive with P < 0.03, all cells:")
print(RRS[RRS.positive_sig].groupby("rule").agg(readings=("R", "count"), R_min=("R", "min"), R_max=("R", "max")).round(3).to_string())
'''
setsrc(32,s)
# cell 41 stale text
rep(41,"local maximum of the second derivative within 3 ms after the late positive peak","first local maximum or minimum of the second derivative within 3 ms after the late positive\npeak")
# cell 58: step duration selection
s=src(58)+'''
# Steps of at least 100 ms, against the 350 ms steps of Fig. 4A: the criterion's "depolarizing current
# steps that evoke accommodating trains" read with the step length (median step per cell). Also the
# criterion's selection without D8131, whose median step is shorter than 1 ms.
for name, sel in (("median step >= 100 ms", TP[(TP.electrode == "tetrode") & (TP.step_ms >= 100)].index),
                  ("median step >= 100 ms, accommodating", TP[(TP.electrode == "tetrode") & (TP.step_ms >= 100) & TP.accommodating].index),
                  ("accommodating, first ISI 5 to 15 ms, without D8131",
                   TP[(TP.electrode == "tetrode") & TP.accommodating & TP.first_isi_ms.between(5, 15)].index.drop("d8131", errors="ignore"))):
    x = FB[FB.folder.isin(sel)]
    a = x.groupby(["reading", "O6", "O7"]).agg(cells=("folder", "count"), all_parts=("all_parts", "sum"),
                                                amplitude_parts=("amplitude_parts", "sum")).reset_index()
    a["majority"] = a.all_parts > a.cells / 2
    a["amplitude_majority"] = a.amplitude_parts > a.cells / 2
    print(f"tetrode cells, {name}: {list(sel)}")
    print(a.to_string())
'''
setsrc(58,s)
rep(60,"(b) peak minus the mean of -3 to\n-1.5 ms;","(b) peak minus the mean of the 2\nms before the threshold point (claims file, O6 b);")
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
E
git diff --stat
```

```
entries/henze-2000/hc1.py                     |  13 +-
 entries/henze-2000/reproduce_henze_2000.ipynb |  62 ++++++-
 tools/build_site.py                           | 248 +++++++++++++++++++++++++-
 tools/entry.py                                | 112 +++++++++++-
 tools/notify.py                               |   5 +-
 tools/runner/chain.sh                         |   5 +-
 tools/site_assets/app.css                     |  31 ++++
 tools/site_assets/list.js                     |  33 +++-
 8 files changed, 476 insertions(+), 33 deletions(-)
```

**Agent calls Bash**

```bash
cd  date -u; time python tools/entry.py all entries/henze-2000 2>&1 | tail -30; date -u
```

```
Mon Nov  9 22:15:27 UTC 2026
Installed kernelspec registry-henze-2000 in executed/henze-2000/.venv/share/jupyter/kernels/registry-henze-2000
0 error(s)
pass  reproduce_henze_2000.ipynb  (566 s)

real	9m33.642s
user	8m31.977s
sys	1m19.999s
Mon Nov  9 22:25:01 UTC 2026
```

**Agent calls Bash**

```bash
cd  ls executed/henze-2000/; python - <<'E'
import json,glob
p=glob.glob('executed/henze-2000/*.ipynb')[0]
nb=json.load(open(p))
for i in [15,32,58,61]:
    c=nb['cells'][i]
    print(f"=== cell {i}")
    for o in c.get('outputs',[]):
        t=''.join(o.get('text',''))
        print(t[-6000:] if i!=61 else t)
E
```

```
reproduce_henze_2000.ipynb
result.json
=== cell 15
10 kHz: threshold [-59.57 -54.57] mV, baseline [-59.99 -54.99] mV (resting -60 and -55 mV), peak [20. 25.] mV
20 kHz: threshold [-59.19 -54.19] mV, baseline [-59.98 -54.98] mV (resting -60 and -55 mV), peak [20. 25.] mV
trough at -0.3 ms: found at -0.305 ms (window -2 to +0.6), -0.305 ms (window -1 to +0.6)
trough at -1.1 ms: found at -1.105 ms (window -2 to +0.6), -1.000 ms (window -1 to +0.6)
trough at -1.3 ms: found at -1.305 ms (window -2 to +0.6), 0.600 ms (window -1 to +0.6)
trough at -1.8 ms: found at -1.805 ms (window -2 to +0.6), 0.600 ms (window -1 to +0.6)

=== cell 32
alse
10  spont        a        b   base  13 -0.1209  0.6939     False  False
11  spont        a        b    thr  13 -0.0581  0.8503     False  False
12  spont        b        a   base  13 -0.0373  0.9038     False  False
13  spont        b        a    thr  13  0.4982  0.0832     False  False
14  spont        b        b   base  13 -0.1135  0.7120     False  False
15  spont        b        b    thr  13  0.3434  0.2507     False  False
readings reproduced: 4 ; positive with P < 0.03: 5 of 16
by somatic/dendritic rule (16 readings each):
[... 206 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json,glob,re
nb=json.load(open('executed/henze-2000/reproduce_henze_2000.ipynb'))
t=''.join(nb['cells'][58]['outputs'][0]['text'])
print(t[:3500])
t=''.join(nb['cells'][55]['outputs'][0]['text'])
for l in t.splitlines():
    if re.search(r'\s[ab]\s+[ab]\s+[ab]\s', l) and ('a  b' in l or True):
        pass
# print FB rows for reading a O6 a O7 b
for l in t.splitlines():
    if re.match(r'\s*\d+\s+d\d+\s+\S+( probe)?\s+a\s+a\s+b\s',l): print(l)
E
```

```
trains_to_5th  first_isi_ms  fourth_isi_ms  step_ms  step_size_raw      electrode  accommodating
folder                                                                                                  
d11221            339         13.10          75.10   500.20          603.0        tetrode           True
d11222            225         53.10          61.20   399.30          203.0        tetrode           True
d12821             32          4.85          13.00    25.45          605.0        tetrode           True
d13522            501          2.75           6.20   500.10          807.0        tetrode           True
d13711             24          3.47           5.85    20.40         1509.0        tetrode           True
d13921             37         13.60          14.40   300.10          403.0        tetrode           True
d14531             16          6.75          11.95   500.10          403.0        tetrode           True
d15121            239          3.60           5.70    40.30         1008.0        tetrode           True
d17013            450         18.27          35.72    13.82           13.0  silicon probe           True
d17111            600         11.62          17.23   289.60         8049.0  silicon probe           True
d17211            300         14.35          25.33     9.90           12.0  silicon probe           True
d17212            176         20.60          56.15     8.55           12.0  silicon probe           True
d18011             11         34.35          11.60   150.35         1295.0  silicon probe          False
d18021             45         24.45          36.60    12.10           10.0  silicon probe           True
d18712            131          9.15          17.05   101.20         6452.0  silicon probe           True
d5611              33          8.30          12.80    15.40            5.0        tetrode           True
d6111             366          6.25          25.05   349.95           32.0        tetrode           True
d6811        
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json,re
nb=json.load(open('executed/henze-2000/reproduce_henze_2000.ipynb'))
t=''.join(o.get('text','') for o in nb['cells'][55]['outputs'])
lines=t.splitlines()
hdr=[l for l in lines if 'amplitude_parts' in l and 'folder' in l]
print(hdr[0])
for l in lines:
    if re.search(r'tetrode\s+a\s+a\s+b\s',l): print(l)
E
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
TypeError: sequence item 0: expected str instance, list found
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json,re
nb=json.load(open('executed/henze-2000/reproduce_henze_2000.ipynb'))
t=''.join(''.join(o.get('text','')) for o in nb['cells'][55]['outputs'])
lines=t.splitlines()
hdr=[l for l in lines if 'amplitude_parts' in l and 'folder' in l]
print(hdr[0])
for l in lines:
    if re.search(r'tetrode\s+a\s+a\s+b\s',l): print(l)
E
```

```
folder      electrode reading O6 O7  ic_amp   rise   fall  ec_amp  ec_slope  base_rises  peak_less_than_base  amplitude_parts  all_parts
1    d11221        tetrode       a  a  b    True   True   True    True      True        True                 True             True       True
9    d11222        tetrode       a  a  b    True   True   True    True      True        True                 True             True       True
17   d12821        tetrode       a  a  b    True  False  False   False     False        True                False            False      False
25   d13522        tetrode       a  a  b    True  False   True    True      True        True                 True             True      False
33   d13711        tetrode       a  a  b    True  False  False    True      True        True                False             True      False
41   d13921        tetrode       a  a  b    True   True   True   False      True        True                False            False      False
49   d14531        tetrode       a  a  b    True   True   True   False      True        True                 True            False      False
57   d15121        tetrode       a  a  b    True   True   True    True      True        True                 True             True       True
121   d5611        tetrode       a  a  b   False  False   True   False     False       False                 True            False      False
129   d6111        tetrode       a  a  b   False  False  False   False     False        True                False            False      False
137   d6811        tetrode       a  a  b    True   True   True    True      True        True                 True             True       True
145   d7111        tetrode       a  a  b    True   True   True    True      True        True                 True             True       True
153   d7211        tetrode       a  a  b    True   True   True    True      True        True                 True             True       True
161   d7212      
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/henze-2000; python - <<'E'
import json
p='reproduce_henze_2000.ipynb'
nb=json.load(open(p))
C=nb['cells']
s=''.join(C[58]['source'])
i=s.index('\n# Steps of at least 100 ms')
s=s[:i]+'''
# The step length of Fig. 4A (350 ms) as a third part of the criterion's selection: cells whose median
# depolarizing step lasts at least 50, 100, 200 or 300 ms, with and without the accommodating, first ISI
# 5 to 15 ms condition; and the criterion's selection without D8131, whose median step is 0.1 ms.
rows = []
crit = TP[(TP.electrode == "tetrode") & TP.accommodating & TP.first_isi_ms.between(5, 15)].index
sels = {"criterion's, without D8131": crit.drop("d8131", errors="ignore")}
for min_ms in (50, 100, 200, 300):
    long_ = TP[(TP.electrode == "tetrode") & (TP.step_ms >= min_ms)].index
    sels[f"step >= {min_ms} ms"] = long_
    sels[f"criterion's and step >= {min_ms} ms"] = long_.intersection(crit)
for name, sel in sels.items():
    x = FB[FB.folder.isin(sel)]
    for (rd, o6, o7), y in x.groupby(["reading", "O6", "O7"]):
        rows.append(dict(selection=name, reading=rd, O6=o6, O7=o7, cells=len(y), all_parts=int(y.all_parts.sum()),
                         amplitude_parts=int(y.amplitude_parts.sum())))
    print(f"{name}: {list(sel)}")
SL = pd.DataFrame(rows)
SL["majority"] = SL.all_parts > SL.cells / 2
SL["amplitude_majority"] = SL.amplitude_parts > SL.cells / 2
print(SL.to_string())
print("by selection, the best reading:")
print(SL.groupby("selection", sort=False).agg(cells=("cells", "max"), all_parts=("all_parts", "max"), amplitude_parts=("amplitude_parts", "max"),
                                              any_majority=("majority", "any"), any_amplitude_majority=("amplitude_majority", "any")).to_string())
'''
C[58]['source']=s.splitlines(keepends=True)
s=''.join(C[32]['source'])
s=s.replace('''print("counts over all 16 readings per rule, by cells left out:")''','''print("readings that reproduce with cells left out:")
print(LO[LO.reproduced & (LO.left_out != "none")].round(4).to_string())
print("counts over all 16 readings per rule, by cells left out:")''')
C[32]['source']=s.splitlines(keepends=True)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
E
git diff reproduce_henze_2000.ipynb | head -5
```

```
diff --git a/entries/henze-2000/reproduce_henze_2000.ipynb b/entries/henze-2000/reproduce_henze_2000.ipynb
index cc35bd1dfb..ca265ab345 100644
--- a/entries/henze-2000/reproduce_henze_2000.ipynb
+++ b/entries/henze-2000/reproduce_henze_2000.ipynb
@@ -287,7 +287,8 @@
```

**Agent calls Bash**

```bash
cd  date -u; python tools/entry.py all entries/henze-2000 2>&1 | tail -3; python - <<'E'
import json
nb=json.load(open('executed/henze-2000/reproduce_henze_2000.ipynb'))
for i in [32,58]:
    t=''.join(''.join(o.get('text','')) for o in nb['cells'][i]['outputs'])
    k=t.find('readings that reproduce with cells left out') if i==32 else t.find("criterion's, without D8131:")
    print(t[k:])
E
date -u
```

```
Mon Nov  9 22:26:03 UTC 2026
Installed kernelspec registry-henze-2000 in executed/henze-2000/.venv/share/jupyter/kernels/registry-henze-2000
0 error(s)
pass  reproduce_henze_2000.ipynb  (481 s)
readings that reproduce with cells left out:
   rule spikes ic_start ec_start ic_end          left_out   n       R      p  reproduced  positive_sig
73   S3    all        b        a    thr  D12821 and D8131  11  0.6542  0.029        True          True
counts over all 16 readings per rule, by cells left out:
                        n  readings  reproduced  positive_sig  R_min  R_max
rule left_out                                                              
S1   none               8        16           0             4  0.274  0.945
S2   D12821            13        14           0             0 -0.226  0.168
     D12821 and D8131  12        14           0             0 -0.163  0.224
     none              14        16           1             1 -0.210  0.631
S3   D12821            12        14           0             0 -0.122  0.559
     D12821 and D8131  11        14           1             1  0.101  0.654
     none              13        16           4             5 -0.121  0.742
S4   none               9        16           0             4  0.091  0.945
R of the readings positive with P < 0.03, all cells:
      readings  R_min  R_max
[... 102 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "\[\\\\\"base\\\\\"\]\|spike_ic" entries/henze-2000/reproduce_henze_2000.ipynb | head; grep -n "spike_ic\|\[\"base\"\]" entries/henze-2000/hc1.py; python - <<'E'
import json
nb=json.load(open('executed/henze-2000/reproduce_henze_2000.ipynb'))
for i in [67]:
    t=''.join(''.join(o.get('text','')) for o in nb['cells'][i]['outputs'])
    print(t[-700:])
E
```

```
289:    "Checks of the helper's measures on synthetic waveforms. The per-spike threshold (`hc1.per_spike_ic`)\n",
304:    "    r_ = hc1.per_spike_ic(ts, np.vstack([vs, vs + 5]), sr)\n",
367:    "               initial_pos_uV=w[\"ec\"][best][(GRID >= em[\"t_neg\"] - 1) & (GRID <= em[\"t_neg\"])].max() - em[\"base\"])\n",
889:    "        sd = em[\"base\"] + nd * scale\n",
1564:    "        si, se = f[\"spike_ic\"], f[\"spike_ec\"]\n",
1565:    "        ica_.append((si[\"peak\"] - si[\"thr\"])[m]); icb_.append((si[\"peak\"] - si[\"base\"])[m])\n",
328:    res["spike_ic"] = per_spike_ic(t, icw, sr)
345:def per_spike_ic(t, icw, sr):
            3  0.179  0.179         False         False    [-1.365, -0.815, 0.16, -0.16, -0.275, -0.44]
9   d18911    pyramidal  assumed (channel / 2)              4   -inf   -inf         False         False    [-1.425, -1.4, -1.33, -0.925, -1.19, -1.215]
10  d17212  interneuron  assumed (channel / 2)              6  0.641  0.481          True          True        [0.17, 0.175, 0.165, 0.16, 0.155, -0.09]
interneuron: 1 cells; in range, fit pairing: 1; farthest-site pairing: 1
pyramidal: 10 cells; in range, fit pairing: 2; farthest-site pairing: 1
finite velocities, fit pairing (m/s): [0.54, 0.19, 0.45, 0.18, 0.64]
finite velocities, farthest-site pairing (m/s): [0.33, 0.19, 0.6, 0.18, 0.48]
```

**Agent calls Bash**

```bash
cd entries/henze-2000; python - <<'E'
import json
for i in [33,59,62,68]:
    pass
nb=json.load(open('reproduce_henze_2000.ipynb'))
for i in [62]:
    print(''.join(nb['cells'][i]['source']))
E
```

```
**Result: reproduced.** With the per-spike threshold now taken from the run of dV/dt > 10 V/s
that holds the maximal rate of rise, D15121 gives R within 0.36 to 0.44 with P < 0.0001 under
both intracellular amplitude readings with the baseline-to-negative extracellular amplitude
(O6 a, R = 0.408, n = 958; O6 b, R = 0.374, n = 973). D15121's trains start at a first interval of
3.6 ms (median), high-frequency bursts like those of Fig. 4D. The relationship is not general: of
64 cell and reading rows over 16 cells, 15 are positive with P < 0.0001 (R 0.374 to 0.774), and
D11222, D13522, D17111 and D17211 give negative correlations with P < 0.0001.
```

**Agent calls Bash**

```bash
cd entries/henze-2000; python - <<'E'
import json
p='reproduce_henze_2000.ipynb'
nb=json.load(open(p))
C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def setsrc(i,s): C[i]['source']=s.splitlines(keepends=True)
def rep(i,old,new):
    s=src(i); assert old in s,(i,old); setsrc(i,s.replace(old,new))
rep(33,"so they would give partially reproduced.","so they would give partially reproduced.\nThe result rests on one cell, D12821, which S2 and S3 add and whose intracellular duration\n(5.700 ms from the dV/dt start, 2.985 ms from the second-derivative start) is far above the\npaper's 1.28 +/- 0.18 ms. Without it no reading under S2 or S3 gives a positive R with P < 0.03\n(S3, R -0.122 to 0.559; the five reproducing readings fall to R 0.042 to 0.545). Without\nD12821 and D8131, one S3 reading reproduces (second-derivative start, extracellular start at\n2 SD, end at threshold, R = 0.654, P = 0.029, n = 11).")
rep(62,"(O6 a, R = 0.408, n = 958; O6 b, R = 0.374, n = 973).","(O6 a, R = 0.408; O6 b, peak minus the mean of the 2 ms before the threshold point, R = 0.376;\nn = 958 for both).")
rep(62,"15 are positive with P < 0.0001 (R 0.374 to 0.774)","16 are positive with P < 0.0001 (R 0.142 to 0.869)")
rep(68,"their finite velocities are\n0.18 to 0.54 m/s,","the pyramidal cells' finite\nvelocities are 0.18 to 0.54 m/s by the fit pairing and 0.18 to 0.60 m/s by the farthest-site\npairing,")
s=src(59)
s=s.rstrip('\n')+'''

The criterion's selection ignores step length, and the steps found range from a median of 0.1
ms (D8131) to 500 ms per cell, against the 350 ms steps of Fig. 4A. Without D8131 the criterion's
selection gives all parts in 5 of 10, not a majority. With the step length as a third condition,
no selection gives the full set in a majority (at most 5 of 10 cells). The amplitude parts hold in
a majority with steps of at least 50 to 300 ms alone (7 of 10, 5 of 8, 4 of 7, 4 of 7) and with
the criterion's selection and steps of at least 50 ms (5 of 8), but not with the criterion's
selection and steps of at least 100 ms (3 of 6) or 200 and 300 ms (2 of 5). The selection that
applies every feature of Fig. 4A that the criterion names (accommodating trains, first interval
5 to 15 ms, steps of 100 ms or more) therefore gives not reproduced. The outcome verified in
round 2 is kept, and not reproduced is proposed for a third round.
'''
setsrc(59,s)
s=src(71)
for old,new in [
 ("| duration-correlation | reproduced, resting on the somatic/dendritic rule (R = 0.644, P = 0.0175 under S3) |",
  "| duration-correlation | reproduced, resting on the somatic/dendritic rule (R = 0.644, P = 0.0175 under S3; without D12821 no S3 reading has P < 0.03) |"),
 ("| fig4bc-burst-attenuation | partially reproduced, resting on the selection of cells |",
  "| fig4bc-burst-attenuation | partially reproduced, resting on the selection of cells; not reproduced proposed (with steps of 100 ms or more in the criterion's selection, 3 of 6 cells) |"),
 ("The spreadsheet IntraExtra.xls covers 18 of the 39 cells, none of the 19\nearliest tetrode cells,","The spreadsheet IntraExtra.xls covers 18 of the 39 cells and only 2 of the 21\ntetrode cells (D14521, D14921), so for 19 of the 21 tetrode cells"),
]:
    assert old in s,old; s=s.replace(old,new)
setsrc(71,s)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
print(src(71)[src(71).find('What was found'):][:700])
E
```

```
What was found about the data set. Only 5 of 39 folders have a README naming the channels, and
the intracellular channel moves between files of one cell (channel 5 or 6 in D112); two binary
formats (12-bit and 16-bit) are mixed without a note. The README of d6811 lists three
extracellular channels, and that of d13521 gives 10 kHz where its xml gives 20 kHz (the AP
durations fit 20 kHz). The spreadsheet IntraExtra.xls covers 18 of the 39 cells and only 2 of the 21
tetrode cells (D14521, D14921), so for 19 of the 21 tetrode cells so the paper's cell types, impalement sites, electrode offsets and
tetrode-to-soma distances are not in the data set; Fig. 6A labels a cell D107 that has no folder.
W
```

**Agent calls Bash**

```bash
cd entries/henze-2000; python - <<'E'
import json
p='reproduce_henze_2000.ipynb'
nb=json.load(open(p))
C=nb['cells']
def rep(i,old,new):
    s=''.join(C[i]['source']); assert old in s,(i,old); C[i]['source']=s.replace(old,new).splitlines(keepends=True)
rep(71,"so for 19 of the 21 tetrode cells so the paper's","and for the other 19 the paper's")
rep(33,"(S3, R -0.122 to 0.559; the five reproducing readings fall to R 0.042 to 0.545)","(S3, R -0.122 to 0.559; the four S3 readings that reproduce fall to R 0.042 to 0.545, the\nS2 one to -0.197)")
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
E
date -u
```

```
Mon Nov  9 22:34:51 UTC 2026
```

**Agent calls Bash**

```bash
cd  grep -rln "proposed:" attempts | head -3; f=$(grep -rln "^  proposed:" attempts | head -1); grep -n -A6 "^  proposed:" $f | head -20; grep -n "proposed" -A15 schemas/*attempt* 2>/dev/null | head -40; ls schemas 2>/dev/null
```

```
attempts/liu-2024-01.yaml
attempts/varela-2020-01.yaml
attempts/watson-2016-01.yaml
116:  proposed:
117-    outcome: partially_reproduced
118-    reason: With the ridge penalty chosen by fivefold cross-validation within each training set, a
119-      selection added after the second round, the ordering of the criterion holds (both above male
120-      by 0.0003 over cells) and all three values are below 0.25, which meets the partial rule.
121-  notebook: reproduce_liu_2024.ipynb
122-  output: claim:fig2e-glm-behaviour-explains-little
303:          "proposed": {
304-            "description": "A change of outcome found after the last verification round, held until a further round agrees with it.",
305-            "type": "object",
306-            "additionalProperties": false,
307-            "required": [
308-              "outcome",
309-              "reason"
310-            ],
311-            "properties": {
312-              "outcome": {
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
def find(o,k):
    if isinstance(o,dict):
        for a,b in o.items():
            if a==k: print(json.dumps(b,indent=1)[:2500]); return True
            if find(b,k): return True
    elif isinstance(o,list):
        for b in o:
            if find(b,k): return True
find(s,'verifications')"
```

```
{
 "type": "array",
 "items": {
  "type": "object",
  "additionalProperties": false,
  "required": [
   "date",
   "kind",
   "by",
   "results"
  ],
  "properties": {
   "date": {
    "type": "string",
    "format": "date"
   },
   "kind": {
    "enum": [
     "agent",
     "person",
[... 49 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
p='attempts/henze-2000-01.yaml'; s=open(p).read()
def rep(old,new):
    global s
    assert s.count(old)==1,old; s=s.replace(old,new)
# duration-correlation notes
rep("""    no reading reaches P < 0.03. The outcome rests on the site rule - S2 (14 cells) reproduces under one
    reading (R = 0.631, P = 0.0155), while S1 (8 cells) and S4 (9 cells) give positive R with P < 0.03
    under 4 readings each, R 0.76 to 0.95, outside tolerance, which would be partially reproduced.
""","""    no reading reaches P < 0.03. The outcome rests on the site rule - S2 (14 cells) reproduces under one
    reading (R = 0.631, P = 0.0155), while S1 (8 cells) and S4 (9 cells) give positive R with P < 0.03
    under 4 readings each, R 0.759 to 0.945, outside tolerance, which would be partially reproduced. It
    also rests on one cell, D12821, which S2 and S3 add and whose intracellular duration (5.700 ms from
    the dV/dt start, 2.985 ms from the second-derivative start) is far above the paper's 1.28 +/- 0.18
    ms. Without D12821 no reading under S2 or S3 gives a positive R with P < 0.03 (S3, R -0.122 to 0.559;
    the four S3 readings that reproduce fall to R 0.042 to 0.545, the S2 one to -0.197). Without D12821
    and D8131 one S3 reading reproduces (second-derivative start, extracellular start at 2 SD, end at
    threshold, R = 0.654, P = 0.029, n = 11).
""")
# fig4bc
rep("""- claim: fig4bc-burst-attenuation
  outcome: partially_reproduced
  assumed: true
""","""- claim: fig4bc-burst-attenuation
  outcome: partially_reproduced
  assumed: true
  proposed:
    outcome: not_reproduced
    reason: The selection verified in round 2 ignores the length of the depolarizing steps, whose median
      per cell runs from 0.1 ms (D8131) to 500 ms against the 350 ms steps of Fig. 4A. Applying every feature
      of Fig. 4A the criterion names (accommodating trains, first interval 5 to 15 ms, median step of 100
      ms or more) leaves 6 tetrode cells; the full set and the amplitude parts each hold in at most 3 of
      6 (2 of 5 with steps of 200 or 300 ms), not a majority, so neither the reproduced nor the partial
      rule is met. With step length alone (50 to 300 ms) the amplitude parts hold in a majority (5 of 8
      at 100 ms) and the full set in none.
""")
rep("""    than one cell (12 of 17, 9 of 13, 7 of 8, 7 of 11; O7 b). In the silicon-probe cells all parts hold
    in 1 of 7. The notch was not scored.
""","""    than one cell (12 of 17, 9 of 13, 7 of 8, 7 of 11; O7 b). In the silicon-probe cells all parts hold
    in 1 of 7. The notch was not scored. The median step per cell runs from 0.1 ms (D8131) to 500 ms;
    without D8131 the criterion's selection gives the full set in 5 of 10. With a median step of at least
    50, 100, 200 or 300 ms added as a condition, no selection gives the full set in a majority; the amplitude
    parts hold in a majority with step length alone (7 of 10, 5 of 8, 4 of 7, 4 of 7) and with the criterion's
    selection at 50 ms (5 of 8), and not with the criterion's selection at 100 ms (3 of 6), 200 or 300
    ms (2 of 5). Not reproduced is proposed for a third round.
""")
rep("""    trains are not.
""","""    trains are not. The step length of Fig. 4A (350 ms) is shown as a further condition (median step at
    least 50 to 300 ms).
""")
# fig4d
rep("""  notes: D15121 gives R within 0.36 to 0.44 with P < 0.0001 under both intracellular amplitude readings
    with the baseline-to-negative extracellular amplitude (O6 a, R = 0.408, n = 958; O6 b, R = 0.374,
    n = 973); its trains start at a median first interval of 3.6 ms, bursts of high frequency as in Fig.
    4D. The relationship is not general - over 16 candidate cells and four readings, 15 of 64 rows are
    positive with P < 0.0001 (R 0.374 to 0.774), and D11222, D13522, D17111 and D17211 give negative correlations
""","""  notes: D15121 gives R within 0.36 to 0.44 with P < 0.0001 under both intracellular amplitude readings
    with the baseline-to-negative extracellular amplitude (O6 a, R = 0.408; O6 b, R = 0.376; n = 958);
    its trains start at a median first interval of 3.6 ms, bursts of high frequency as in Fig. 4D. The
    relationship is not general - over 16 candidate cells and four readings, 16 of 64 rows are positive
    with P < 0.0001 (R 0.142 to 0.869), and D11222, D13522, D17111 and D17211 give negative correlations
""")
rep("""  - Burst spikes are those inside depolarizing steps""","""  - Intracellular amplitude O6 b of each spike is the peak minus the mean of the 2 ms before its threshold
    point, as the claims file defines it; until round 2 it used the mean of -3 to -1.5 ms from the peak.
  - Burst spikes are those inside depolarizing steps""")
# propagation
rep("""    1 by the farthest-site pairing; the finite velocities are 0.18 to 0.54 m/s, and 6 cells give a zero
    or negative delay.""","""    1 by the farthest-site pairing; the finite velocities of the pyramidal cells are 0.18 to 0.54 m/s by
    the fit pairing and 0.18 to 0.60 m/s by the farthest-site pairing, and 6 cells give a zero or negative
    delay.""")
rep("    Six of the paper's 21 findings cannot be tested for this reason.","    Seven of the paper's 21 claims are blocked for this reason.")
rep("""    mV for the offset gives 13 and calls D53 somatic. Whether the intracellular and extracellular durations
    correlate within tolerance (R = 0.66) depends on this choice.""","""    mV for the offset gives 13 and calls D53 somatic. Whether the intracellular and extracellular durations
    correlate within tolerance (R = 0.66) depends on this choice, and on D12821, a cell the 10 mV allowance
    adds, whose intracellular duration (5.7 ms) is far above the paper's 1.28 +/- 0.18 ms.""")
rep("""    with 20 or 50 trains 6 of 13 and 5 of 8, and with accommodating trains whose first interval is 5 to
    15 ms, 6 of 11.""","""    with 20 or 50 trains 6 of 13 and 5 of 8, and with accommodating trains whose first interval is 5 to
    15 ms, 6 of 11, but 3 of 6 when the steps must also last 100 ms or more. How long were the steps?""")
open(p,'w').write(s)
E
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  cat >> attempts/henze-2000-01.yaml <<'E'
- date: '2026-11-09'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: Round 2. The full executed notebook of the author-revise-1 revision, with its conclusions and
    summary, the attempt record, the README, the helper module and the claims file, with the paper. The
    verifier agreed with all 21 outcomes, with a reservation on duration-correlation and calling fig4bc-burst-attenuation
    fragile. It quoted five sentences the outputs did not support (the summary's spreadsheet coverage,
    the R 0.76 bound in the duration-correlation notes, the count of six blocked findings, the velocity
    range of propagation-velocity-range and the stale slope-change text of the notch section), all now
    corrected, and noted that the intracellular amplitude reading (b) of fig4d-amplitude-correlation used
    -3 to -1.5 ms where the claims file gives the 2 ms before the start; the helper now follows the claims
    file.
  results:
  - claim: sample-cells
    agrees: true
    outcome: not_reproduced
    reason: Cell 21.
    response: Outcome kept.
  - claim: fig1c-start-end-timing
    agrees: true
    outcome: not_reproduced
    reason: Cell 26 - the start lead is never in tolerance, under any of the four site rules (S1 to S4).
    response: Outcome kept.
  - claim: ap-duration-match
    agrees: true
    outcome: reproduced
    reason: Cell 29 - 1, 6, 1 and 2 readings pass under S3, S1, S2 and S4. Under S3 the extracellular duration
      SD is 0.59 against the paper's 0.19, but the criterion tests means only.
    response: Outcome kept.
  - claim: duration-correlation
    agrees: true
    outcome: reproduced
    reason: The assumption (rule S3) is stated and reasonable in that it agrees with the paper's own label
      of D53. The reservation is that the result rests on D12821, a cell S3 adds, whose intracellular duration
      is 5.70 ms against the paper's 1.28 +/- 0.18. From cell 29's per-cell durations R = 0.742; without
      D12821 it drops to R = 0.02, and without D12821 and D8131 to 0.46. Cell 32 does not print the per-cell
      values of the reproducing readings. The record should say this. It also found that the notes' bound
      R 0.76 for S1 and S4 is not printed.
    response: Outcome kept. Cell 32 now prints the per-cell durations of every reproducing reading and R
      with D12821, and D12821 and D8131, left out. Without D12821 no S2 or S3 reading has a positive R with
      P < 0.03 (the four S3 readings that reproduce fall to R 0.042 to 0.545, the S2 one to -0.197); without
      both cells one S3 reading reproduces (R = 0.654, P = 0.029, n = 11). The conclusion, the notes and
      the methods_unavailable finding on the site rule now state this dependence. The range of the positive
      significant readings is now printed per rule (S1 and S4, R 0.759 to 0.945), and the notes give it.
  - claim: neg-peak-precedes-intra-peak
    agrees: true
    outcome: reproduced
    reason: Cell 35.
    response: Outcome kept.
  - claim: fig1c-derivative-mismatch
    agrees: true
    outcome: reproduced
    reason: Cell 38.
    response: Outcome kept.
  - claim: notch-and-ahp-landmarks
    agrees: true
    outcome: not_reproduced
    reason: Cell 42. The method text of cell 41 still says the slope change is a local maximum of the second
      derivative, where the code and the conclusion use the first local maximum or minimum; the text is
      stale, the conclusion is correct.
    response: Outcome kept. The method text now says the first local maximum or minimum.
  - claim: fig2-interneuron-narrow
    agrees: true
    outcome: blocked
    response: Outcome kept.
  - claim: fig3b-latency-vs-amplitude
    agrees: true
    outcome: reproduced
    reason: Cell 45 - holds under all four rules.
    response: Outcome kept.
  - claim: fig3a-example-pair
    agrees: true
    outcome: not_reproduced
    reason: The pair identification is stated and reasonable. Cell 45 shows the 0.975 ms latency of D11222
      is not a window-edge artefact.
    response: Outcome kept.
  - claim: fig3c-backprop-velocity
    agrees: true
    outcome: not_reproduced
    reason: Cell 52 - 0 of 96 readings in tolerance.
    response: Outcome kept.
  - claim: fig4bc-burst-attenuation
    agrees: true
    outcome: partially_reproduced
    reason: Yes, but fragile. Cell 58 now prints step durations but the selection ignores them. They range
      from 0.1 to 500 ms, against the 350 ms steps of Fig. 4A. The 6 of 11 majority under the criterion's
      selection includes D8131, whose median step is 0.1 ms; without it the count is 5 of 10, not a majority.
      Taking only those 11 cells with steps of at least 100 ms leaves 6 cells. Full set and amplitude parts
      then each hold in 3 of 6 (reading (a), extracellular amplitude baseline to negative peak), not a
      majority, so the outcome would fall from partial to not reproduced.
    response: Outcome kept, as round 2 verified it, and not_reproduced proposed for a third round. Cell
      58 now adds the median step length (at least 50, 100, 200 or 300 ms) as a condition, alone and with
      the criterion's selection, and the criterion's selection without D8131. It confirms the verifier's
      counts (5 of 10 without D8131; 3 of 6 for both parts with steps of 100 ms or more) and shows 2 of
      5 with steps of 200 or 300 ms. The selection that applies every feature of Fig. 4A the criterion names
      is the best supported, so not reproduced is proposed; the notes, the conclusion and the methods_unavailable
      finding give the dependence on step length.
  - claim: fig4d-amplitude-correlation
    agrees: true
    outcome: reproduced
    reason: With the corrected threshold, D15121 gives R = 0.408 and 0.374 with P < 0.0001 (cell 61). The
      per-spike threshold now passes the synthetic check (cell 15, -59.6 against a -60 mV rest). Minor - cell
      60 defines intracellular amplitude reading (b) as peak minus the mean of -3 to -1.5 ms, where the
      claims file defines it as the 2 ms before the start, and the record does not list this as a deviation.
    response: Outcome kept. The per-spike baseline is now the mean of the 2 ms before the threshold point,
      as the claims file defines O6 b, checked on the synthetic APs of cell 15 (-60.0 against a -60 mV rest).
      D15121 gives R = 0.376 under O6 b (n = 958) and 0.408 under O6 a, so the outcome is unchanged; the
      change is recorded as a deviation.
  - claim: fig5-theta-smaller-spikes
    agrees: true
    outcome: blocked
    response: Outcome kept.
  - claim: theta-higher-rates
    agrees: true
    outcome: blocked
    response: Outcome kept.
  - claim: fig6-amplitude-vs-distance
    agrees: true
    outcome: blocked
    response: Outcome kept.
  - claim: tetrode-cell-count-estimate
    agrees: true
    outcome: blocked
    response: Outcome kept. The data_missing finding said six of the paper's findings cannot be tested for
      this reason, where the record has seven blocked by data_missing; it now says seven.
  - claim: silent-cells-inference
    agrees: true
    outcome: blocked
    reason: Yes on the outcome. The verifier gave blocked_by other; the author's reason (a claim that depends
      on a blocked claim is blocked for the same reason) is acceptable. It cannot check the protocol step
      cited.
    response: Outcome kept.
  - claim: fig7-vertical-spread
    agrees: true
    outcome: not_reproduced
    reason: Cell 64 - 4 of 10 cells.
    response: Outcome kept.
  - claim: propagation-velocity-range
    agrees: true
    outcome: blocked
    reason: Changed from round 1. The claims file's criterion itself says the counts point to reading (b).
      Reading (a) is reported in the notes. Cell 68 and the notes give finite velocities of 0.18 to 0.54
      m/s, the fit pairing only; the farthest-site pairing gives up to 0.60 m/s (D18712, cell 67).
    response: Outcome kept. The conclusion and the notes now give both pairings (0.18 to 0.54 m/s by the
      fit, 0.18 to 0.60 m/s by the farthest site).
  - claim: fig8-neighbouring-shanks
    agrees: true
    outcome: blocked
    response: Outcome kept.
E
python -c "import yaml;yaml.safe_load(open('attempts/henze-2000-01.yaml'))" && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd  python - <<'E'
p='entries/henze-2000/README.md'; s=open(p).read()
old="| APs and extracellular spikes attenuate during evoked trains | Partially reproduced, resting on an assumption |"
assert old in s
s=s.replace(old,"| APs and extracellular spikes attenuate during evoked trains | Partially reproduced, resting on an assumption (not reproduced proposed for review) |")
open(p,'w').write(s)
E
date -u; python tools/entry.py all entries/henze-2000 2>&1 | tail -3; date -u
```

```
Mon Nov  9 22:35:53 UTC 2026
Installed kernelspec registry-henze-2000 in executed/henze-2000/.venv/share/jupyter/kernels/registry-henze-2000
0 error(s)
pass  reproduce_henze_2000.ipynb  (529 s)
Mon Nov  9 22:44:52 UTC 2026
```

**Agent**

Now a quick check that the key numbers in the new run match what I wrote, and that the repository checks pass.

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
nb=json.load(open('executed/henze-2000/reproduce_henze_2000.ipynb'))
def out(i): return ''.join(''.join(o.get('text','')) for o in nb['cells'][i].get('outputs',[]))
t=out(61); print(t[t.find('cells:'):])
t=out(32); print(t[t.find('readings that reproduce with cells left out'):][:300])
t=out(58); print(t[t.find('by selection'):])
print(out(15)[:250])
E
python tools/entry.py check entries/henze-2000 2>&1 | tail -3; ls tools | grep -i -E "check|valid"
```

```
cells: 16 ; rows with R in 0.36-0.44 and P < 0.0001: [['d15121', 'a', 'b', 0.408], ['d15121', 'b', 'b', 0.376]]
rows with R > 0 and P < 0.0001: 16 of 64

readings that reproduce with cells left out:
   rule spikes ic_start ec_start ic_end          left_out   n       R      p  reproduced  positive_sig
73   S3    all        b        a    thr  D12821 and D8131  11  0.6542  0.029        True          True
counts over all 16 readings per rule, by cells le
by selection, the best reading:
                                cells  all_parts  amplitude_parts  any_majority  any_amplitude_majority
selection                                                                                              
criterion's, without D8131         10          5                6         False                    True
step >= 50 ms                      10          5                7         False                    True
criterion's and step >= 50 ms       8          4                5         False                    True
step >= 100 ms                      8          4                5         False                    True
criterion's and step >= 100 ms      6          3                3         False                   False
step >= 200 ms                      7          3                4         False                    True
criterion's and step >= 200 ms      5          2                2         False                   False
step >= 300 ms                      7          3                4         False                    True
criterion's and step >= 300 ms      5          2                2         False                   False

[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "attempts/\|proposed" tools/entry.py | head; grep -n "—\|rather" attempts/henze-2000-01.yaml entries/henze-2000/README.md | head; python - <<'E'
import json
nb=json.load(open('entries/henze-2000/reproduce_henze_2000.ipynb'))
print(sum(len(c.get('outputs',[])) for c in nb['cells']), "outputs in committed notebook")
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    if '—' in s or ' rather' in s: print('bad', i)
E
```

```
335:                                    f"verification agreed with {verified!r}; record the change under `proposed`, "
0 outputs in committed notebook
```

**Agent**

I've worked through every point in the round-2 report. No outcome changed. I proposed one change for a third round: fig4bc-burst-attenuation from partially_reproduced to not_reproduced. The entry re-ran cleanly (`python tools/entry.py all entries/henze-2000`: 0 errors, notebook passes in 529 s), and every conclusion matches the new numbers.

**Proposed outcome change (fig4bc-burst-attenuation)**
- I kept partially_reproduced and wrote not_reproduced under `proposed`.
- The verifier was right that my selection ignored step length. The median step per cell runs from 0.1 ms (D8131) to 500 ms, against the 350 ms steps of Fig. 4A.
- Cell 58 now also selects on step length (at least 50, 100, 200 or 300 ms), alone and together with the criterion's selection, and runs the criterion's selection without D8131.
- It confirms the verifier's counts: 5 of 10 without D8131, and 3 of 6 for both the full set and the amplitude parts when steps must be 100 ms or more. With steps of 200 or 300 ms it is 2 of 5.
- The selection that uses every feature of Fig. 4A the criterion names is the best supported, and it meets neither the reproduced nor the partial rule. The notes, the conclusion, the README and the question to the authors now say this.

**duration-correlation: dependence on one cell stated, outcome kept**
- Cell 32 now prints each cell's durations for the readings that reproduce, and R with D12821 and D8131 left out.
- Without D12821, no S2 or S3 reading gives a positive R with P < 0.03. The reproducing readings fall to R between -0.197 and 0.545.
- Without both D12821 and D8131, one S3 reading still reproduces (R = 0.654, P = 0.029, n = 11).
- The verifier found the S3 rule reasonable, so I proposed no change. The conclusion, the notes and the question to the authors now state this dependence.

**fig4d-amplitude-correlation: intracellular baseline fixed in `hc1.per_spike_ic`**
- Reading (b) used the mean of -3 to -1.5 ms before the peak. It now uses the mean of the 2 ms before the threshold point, as the claims file defines it.
- The synthetic check in cell 15 gives -60.0 mV against a -60 mV rest.
- D15121 gives R = 0.376 under reading (b) (it was 0.374) and 0.408 under reading (a), both on 958 spikes, so the outcome stands.
- 16 of 64 rows are now positive with P < 0.0001 (R 0.142 to 0.869). The change is recorded as a deviation.

**Text corrections the verifier quoted**
- **Summary:** the spreadsheet covers 18 of the 39 cells and only 2 of the 21 tetrode cells.
- **duration-correlation notes:** the S1 and S4 range is now printed and quoted as R 0.759 to 0.945.
- **First finding:** "six" blocked claims is now "seven".
- **propagation-velocity-range:** the conclusion and notes give both pairings, 0.18 to 0.54 m/s by the fit and 0.18 to 0.60 m/s by the farthest site.
- **Cell 41:** the slope-change description now says first local maximum or minimum, matching the code.

**Record:** the round is in `attempts/henze-2000-01.yaml` under `verifications`. The verifier agreed with all 21 outcomes; each claim has its reason in its own words and my reply under `response`.

**Not done**
- I added nothing to `questions/henze-2000.yaml`, because the report found no place where the claims file misreads the paper.
- Nothing is committed, as instructed.

## End of run

34 turns, 31 minutes, $2.00 at API prices, result: success.
