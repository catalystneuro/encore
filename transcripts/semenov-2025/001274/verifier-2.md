# 001274 · verifier-2 · run 41336207728

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 2388
drwxr-xr-x 6 runner runner     4096 Nov  1 18:39 .
drwxr-xr-x 7 runner runner     4096 Nov  1 18:39 ..
crw-rw-rw- 1 nobody nogroup    1, 3 Nov  1 18:21 .bash_profile
crw-rw-rw- 1 nobody nogroup    1, 3 Nov  1 18:21 .bashrc
drwxr-xr-x 5 runner runner     4096 Nov  1 18:39 .claude
-rw-r--r-- 1 runner runner        0 Nov  1 18:39 .env
-rw-r--r-- 1 runner runner        0 Nov  1 18:39 .env.development
-rw-r--r-- 1 runner runner        0 Nov  1 18:39 .env.development.local
-rw-r--r-- 1 runner runner        0 Nov  1 18:39 .env.local
-rw-r--r-- 1 runner runner        0 Nov  1 18:39 .env.production
-rw-r--r-- 1 runner runner        0 Nov  1 18:39 .env.production.local
-rw-r--r-- 1 runner runner        0 Nov  1 18:39 .env.test
-rw-r--r-- 1 runner runner        0 Nov  1 18:39 .env.test.local
drwx------ 2 runner runner     4096 Nov  1 18:39 .git
crw-rw-rw- 1 nobody nogroup    1, 3 Nov  1 18:21 .gitconfig
crw-rw-rw- 1 nobody nogroup    1, 3 Nov  1 18:21 .github
-rw-r--r-- 1 runner runner        0 Nov  1 18:39 .gitmodules
crw-rw-rw- 1 nobody nogroup    1, 3 Nov  1 18:21 .idea
crw-rw-rw- 1 nobody nogroup    1, 3 Nov  1 18:21 .mcp.json
[... 87 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; cat 001274-semenov-2025-01.yaml
```

```
<persisted-output>
Output too large (38.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/e49dbc54-1bc2-4bab-a3f8-da8963b1728e/tool-results/bytsyixhg.txt

Preview (first 2KB):
# Semenov, Kim, Silkuniene & Pakhomov (2025) from dandiset 001274 and the paper's other dandisets

Tests the findings of [Semenov et al. (2025)](https://doi.org/10.1016/j.xcrp.2025.102660) that can be
tested on [DANDI:001274](https://dandiarchive.org/dandiset/001274/0.250805.1401), which holds the strobe
images of membrane polarization by 2-us pulses and 2-kHz sine waves (Figures 5, 6 and S3), and on the
other dandisets the paper deposited: the fast optical recordings of action potentials in 001032, 001033
and 001035 (Figures 1 and 2), 001030 (Figure 3C), 001271 (Figure S2) and 001272 (Figure S1). 001034 is a
second deposit of 001032.

| Claim | Outcome |
|---|---|
| Unmodulated 2- and 20-kHz sine waves excite every neuron | Not reproduced |
| Near-threshold APs come 100 to 200 ms after onset; stronger fields shorten the delay | Not reproduced |
| The maximum firing rate reaches a ceiling of 60 to 90 Hz | Not reproduced (resting on an assumption) |
| The highest fields give an excitation block | Not reproduced |
| 20-kHz thresholds are about twice the 2-kHz ones | Not reproduced |
[... 13 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/e49dbc54-1bc2-4bab-a3f8-da8963b1728e/tool-results/bytsyixhg.txt"
}
```

```
1	# Semenov, Kim, Silkuniene & Pakhomov (2025) from dandiset 001274 and the paper's other dandisets
2	
3	Tests the findings of [Semenov et al. (2025)](https://doi.org/10.1016/j.xcrp.2025.102660) that can be
4	tested on [DANDI:001274](https://dandiarchive.org/dandiset/001274/0.250805.1401), which holds the strobe
5	images of membrane polarization by 2-us pulses and 2-kHz sine waves (Figures 5, 6 and S3), and on the
6	other dandisets the paper deposited: the fast optical recordings of action potentials in 001032, 001033
7	and 001035 (Figures 1 and 2), 001030 (Figure 3C), 001271 (Figure S2) and 001272 (Figure S1). 001034 is a
8	second deposit of 001032.
9	
10	| Claim | Outcome |
11	|---|---|
12	| Unmodulated 2- and 20-kHz sine waves excite every neuron | Not reproduced |
13	| Near-threshold APs come 100 to 200 ms after onset; stronger fields shorten the delay | Not reproduced |
14	| The maximum firing rate reaches a ceiling of 60 to 90 Hz | Not reproduced (resting on an assumption) |
15	| The highest fields give an excitation block | Not reproduced |
16	| 20-kHz thresholds are about twice the 2-kHz ones | Not reproduced |
17	| Modulated sine waves have higher thresholds | Partially reproduced |
18	| The 2-kHz threshold is 57.7 V/cm | Not reproduced |
19	| Firing locks to the 20-Hz beats, with no sustained depolarization | Not reproduced |
20	| Pure sine waves give more APs than modulated ones at the same field | Reproduced |
[... 596 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF' > $TMPDIR/nb.txt
import json
nb=json.load(open('reproduce_semenov_2025.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f"\n######## CELL {i} [{c['cell_type']}] id={c.get('id')}")
    src=''.join(c['source'])
    print(src)
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--\n'+''.join(o['text']))
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d and 'image/png' not in d: print('--OUT--\n'+''.join(d['text/plain']))
            if 'image/png' in d: print('--IMG--')
        if o.get('output_type')=='error': print('--ERR--',o.get('ename'),o.get('evalue'))
EOF
wc -l $TMPDIR/nb.txt; grep -c "######## CELL" $TMPDIR/nb.txt
```

```
1754 /tmp/claude-1001/nb.txt
75
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "limit": 600
}
```

```
1	
2	######## CELL 0 [markdown] id=6683eacf
3	# Semenov, Kim, Silkuniene & Pakhomov (2025): sine waves and temporal interference stimulation
4	
5	Paper. Semenov I, Kim V, Silkuniene G, Pakhomov AG (2025). Excitation and polarization of isolated
6	neurons by high-frequency sine waves for temporal interference stimulation. *Cell Reports Physical
7	Science* 6, 102660. doi:10.1016/j.xcrp.2025.102660. The claims file was written from the NIH author
8	manuscript (PMC12320893) with its STAR Methods and supplement.
9	
10	Dataset. DANDI:001274, version 0.250805.1401 (the most recent published version). The paper names
11	no version. The dandiset has two published versions, 0.250701.1622 and 0.250805.1401, with the same 232
12	assets and the same number of bytes; the later one is pinned as the protocol asks (author, step 1.3), and
13	the notebook checks below that the asset lists are the same. DANDI:001274 holds the strobe images of
14	Figures 5, 6 and S3. The claims file assigns the other figures to other dandisets of the paper, read at
15	their most recent published versions, for the same reason: 001030 (0.240520.1924), 001032
16	(0.240527.1432), 001033 (0.240527.1432), 001035 (0.240527.1432), 001271 (0.250805.1352), 001272
17	(0.250805.1358) and 001273 (0.250805.1356). 001034 (0.240527.1431) is checked and found to be a second
18	deposit of 001032.
19	
20	Claims (claims/001274/10.1016-j.xcrp.2025.102660.yaml):
[... 580 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 600,
 "limit": 600
}
```

```
600	######## CELL 20 [code] id=bfd1f961
601	mod = fast[fast.carrier.isin(["2k", "20k"]) & fast.modulated]
602	def in_peak_window(times_s, shift_s=0.0):
603	    ph = ((times_s - shift_s) * 1000) % 50
604	    return (ph >= 12.5) & (ph <= 37.5)
605	for key in ["whole/a", "whole/b"]:
606	    t = np.concatenate(mod[f"aps/{key}"].values)
607	    print(f"{key}: {len(t)} APs in {len(mod)} modulated sessions; in the middle half of the beat: "
608	          f"{in_peak_window(t).mean():.2f} with beats from the 50-ms onset, "
609	          f"{in_peak_window(t, 0.025).mean():.2f} with beats shifted by 25 ms (chance 0.5)")
610	--OUT--
611	whole/a: 225 APs in 84 modulated sessions; in the middle half of the beat: 0.96 with beats from the 50-ms onset, 0.04 with beats shifted by 25 ms (chance 0.5)
612	whole/b: 227 APs in 84 modulated sessions; in the middle half of the beat: 0.96 with beats from the 50-ms onset, 0.04 with beats shifted by 25 ms (chance 0.5)
613	
614	
615	######## CELL 21 [markdown] id=b3bd38f8
616	The whole-frame trace gives APs of the size the Methods report, so it is adopted as the soma reading
617	(assumption); the bright-pixel trace is shown as a variant throughout. Reading (b) on the bright-pixel
618	trace finds more than one AP per 250 ms in the pre-stimulus windows, so it is the noisiest of the four.
619	
[... 580 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1199,
 "limit": 560
}
```

```
1199	--IMG--
1200	--OUT--
1201	modulated sessions with the most APs, and the one ending above 5%: 4 traces, dF from -4.4 to 14.8% (all inside the axes); x is ms from stimulus onset
1202	
1203	
1204	######## CELL 52 [markdown] id=c6a1dc6c
1205	**Result: not reproduced.** Firing locks to the beats: of the APs in modulated sessions with 5 APs or more,
1206	0.96 (reading a) and 0.98 (reading b) fall in the middle half of a beat, and 0.04 do in every modulated session
1207	when the beats are shifted by 25 ms, so (ii) holds. (i) holds under both readings (at most 8 and 6 APs; under
1208	the first version of reading a, 12). (iii) fails under both: one session (001032/sub-2-1, 198 V/cm) ends with a
1209	last-100-ms dF of 5.9%, above its near-threshold modulated session (-0.2% at 144 V/cm), and its trace shows
1210	the plateau after the third beat. The criterion asks all three parts.
1211	
1212	######## CELL 53 [markdown] id=49120f16
1213	## 10. fig2c-pure-more-aps
1214	
1215	> In the same neuron at the same field strength, pure sine waves trigger more APs than modulated ones.
1216	
1217	Pairs are a neuron's modulated and unmodulated sessions at one carrier and one field (counts averaged over
1218	repeats). Reproduced when the unmodulated count is higher in more pairs than the reverse, with a two-sided
[... 537 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^  - id:\|^- id:\|id: " 10.1016-j.xcrp.2025.102660.yaml | head -60; sed -n 1,200p 10.1016-j.xcrp.2025.102660.yaml
```

```
80:  id: "001274"
83:- id: fig1-pure-sine-excites-all
104:- id: fig1-onset-delay
122:- id: fig1-max-rate-ceiling
138:- id: fig1-excitation-block
154:- id: fig2d-20khz-twofold-threshold
184:- id: fig2d-modulated-thresholds-higher
213:- id: threshold-2khz-unmodulated
230:- id: fig2-modulated-locks-to-beats
247:- id: fig2c-pure-more-aps
259:- id: fig3b-low-conductivity-halves-threshold
278:- id: fig3c-sustained-firing-2s
296:- id: figs1-di8-anepps-control
314:- id: figs2-ttx-blocks-depolarization
327:- id: fig4-orientation-time-constants
366:- id: fig4-no-pole-difference
383:- id: fig4-discharging-slower
404:- id: fig4-pooled-time-constants
440:- id: fig5-carrier-antiphasic
457:- id: fig5-whole-cell-depolarization
[... 207 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 200,330p 10.1016-j.xcrp.2025.102660.yaml
```

```
test: two-tailed unpaired t test
    p: 0.0037
  data: elsewhere
  where: DANDI:001032, 001033, 001034 and 001035 (assigned from their titles)
  depends_on:
  - fig2d-20khz-twofold-threshold
  criterion: Thresholds as in fig2d-20khz-twofold-threshold. For each of the three pairs, a
    two-tailed unpaired t test of modulated against unmodulated thresholds, as the Results and the
    Figure 2D legend name it, although the same neurons were often tested with both; the paired
    test on neurons with both is shown as a variant. Reproduced when all three have the modulated
    mean higher with p < 0.05 (the Methods' level; the legend marks p < 0.02); partially
    reproduced when one or two do. The 2-kHz 1-AP pair, for which the paper reports no
    difference, is reported.
- id: threshold-2khz-unmodulated
  statement: The AP threshold for unmodulated 2-kHz sine waves was 57.7 plus or minus 3.6 V/cm.
  source: Results, Asymmetric and less-efficient membrane charging by sine waves compared to pulses,
    paragraph 6; Figure 2D
  quote: the AP threshold of 57.7 ± 3.6 V/cm for unmodulated 2-kHz sine waves ( Figure 2D )
  data: elsewhere
  where: DANDI:001032, 001033, 001034 and 001035 (assigned from their titles)
[... 111 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import yaml,collections
c=yaml.safe_load(open('10.1016-j.xcrp.2025.102660.yaml'));a=yaml.safe_load(open('001274-semenov-2025-01.yaml'))
print(len(c['claims']),len(a['outcomes']))
print(collections.Counter(o['outcome'] for o in a['outcomes']))
print(set(x['id'] for x in c['claims'])^set(o['claim'] for o in a['outcomes']))
print([o['claim'] for o in a['outcomes'] if o.get('assumed')])
"; grep -n "def detect_aps" -A45 ti_sine.py | head -80
```

```
26 26
Counter({'blocked': 14, 'not_reproduced': 10, 'partially_reproduced': 1, 'reproduced': 1})
set()
['fig1-max-rate-ceiling']
187:def detect_aps(dF, rate, reading="a", level=AP_LEVEL, invert=False, prominence=PROMINENCE,
188-               min_width_s=MIN_WIDTH_S):
189-    """Frame indices of AP peaks under reading (a) or (b) (module docstring). `prominence`
190-    and `min_width_s` apply to reading (a); at levels other than 5% (the SD readings of
191-    Di-8-ANEPPS) the prominence follows the level."""
192-    x = -dF if invert else dF
193-    w = int(round(AP_WIDTH_S * rate))
194-    dist = int(round(AP_MERGE_S * rate))
195-    if reading == "a":
196-        prom = prominence * level / AP_LEVEL
197-        p, _ = find_peaks(x, height=level, distance=dist, prominence=prom,
198-                          width=(min_width_s * rate, None))
199-    else:
200-        p, _ = find_peaks(x, distance=dist)
201-        p = np.array([i for i in p if i >= w and x[i] - x[i - w:i].min() >= level], dtype=int)
202-    return p
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json,base64,os
nb=json.load(open('reproduce_semenov_2025.ipynb'))
d=os.environ['TMPDIR']
for i,c in enumerate(nb['cells']):
    k=0
    for o in c.get('outputs',[]):
        if 'data' in o and 'image/png' in o['data']:
            open(f"{d}/c{i}_{k}.png",'wb').write(base64.b64decode(o['data']['image/png'])); k+=1
print(sorted(os.listdir(d)))
EOF
```

```
['-home-runner-work--temp', '-home-runner-work--temp-work', 'bash-edit-diff', 'c24_0.png', 'c24_1.png', 'c28_0.png', 'c29_0.png', 'c33_0.png', 'c37_0.png', 'c51_0.png', 'c58_0.png', 'c69_0.png', 'nb.txt']
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/c58_0.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/c29_0.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/c37_0.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/c24_0.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/c51_0.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd  grep -n -i "2-fold\|100% of neurons\|57.7\|60-90\|100-200 ms\|fully blocked\|ramp-up" paper/*.txt | head -20
```

Result: not kept, because it reads the paper's text.

**Agent**

**Round-2 verifier report: Semenov et al. 2025 (DANDI:001274 and related dandisets)**

Counts come from the files. The claims file has 26 claims and the attempt record has 26 outcomes, with the same IDs. Of these, 14 are blocked, 10 not_reproduced, 1 partially_reproduced and 1 reproduced. Only one outcome is marked `assumed: true`: fig1-max-rate-ceiling. I found no place where the claims file misreads the paper.

## 1. Outcomes

| Claim | Record | Agree? |
|---|---|---|
| fig1-pure-sine-excites-all | not_reproduced | Yes, by the criterion. It is marginal: the 20-kHz count is 15/17 under all four readings (cell 23). In cell 24, sub-10-4 at 324 V/cm shows about 8 regularly spaced events of about 3% on a falling trace, which look like small APs. Counting them would give 16/17 (94%) and a pass. The record states this. |
| fig1-onset-delay | not_reproduced | Yes. The median is 64 ms under reading a and 67 ms under reading b; the bracketed-threshold variant also gives 67 ms (cell 27). |
| fig1-max-rate-ceiling | not_reproduced, assumed | Yes. The assumption is stated and reasonable. The claims file's literal reading (a) counts about 18 noise "APs" per 250 ms on a plateau (cell 18). The unchanged reading (b) gives 42.9 Hz, also outside 54–99 Hz. The revised (a) does miss low-amplitude oscillations (cell 37: sub-12-1 a1 vs b23, sub-8-2 a2 vs b21). Reading (b) covers those cases, and its median is still out of range. |
| fig1-excitation-block | not_reproduced | Yes: 3 of 42 under every reading (cell 36). |
| fig2d-20khz-twofold-threshold | not_reproduced | Yes. The calibration sentence is wrong (section 2), and correcting it makes the outcome stronger. |
| fig2d-modulated-thresholds-higher | partially_reproduced | Yes: 2 of 3 pairs reach p < 0.05 under both readings (cell 43). |
| threshold-2khz-unmodulated | not_reproduced | Yes, as pooled: 75.6 / 74.8 V/cm, and 151 under the full-voltage reading (cell 46). The result depends on pooling the three dandisets (section 3). |
| fig2-modulated-locks-to-beats | not_reproduced | Yes. Part (iii) fails on 001032/sub-2-1 at 198 V/cm, which ends at 5.9% against −0.2% at its near-threshold session; the plateau is visible in cell 51. |
| fig2c-pure-more-aps | reproduced | Yes (cell 54). |
| fig3c-sustained-firing-2s | not_reproduced | **No, I now disagree; this reverses my round-1 view.** Parts (i) and (ii) hold for c7. Part (iii) fails only on 5 events under (a) and 1 under (b) on the 6.7% plateau over 0.25–2 s (cells 57–58). The notebook's own test (cell 18) gives 1.2 (a) and 0.8 (b) false APs per 250 ms on a 6% plateau at 0.83% noise. That predicts about 8 and 6 such events over 1.75 s, and more on a bleaching-corrected (differenced, so noisier) trace. In cell 58 the events are isolated and irregular. I would score c7 reproduced. At the least, the outcome should be marked `assumed: true`, since it rests on treating noise-level detections as APs. |
| figs1-di8-anepps-control | not_reproduced | Yes: block is 0/3 under every reading (cell 61). blocked (data_missing) would also be defensible, as the record says. |
| figs2-ttx-blocks-depolarization | not_reproduced | Yes: before tetrodotoxin, last-100-ms dF is above 5% in only 1 of 6 neurons (cell 64). |
| fig3b and the 12 strobe claims (Figures 4, 5, 6, S3) plus threshold-depolarization-estimate (14 blocked in all) | blocked | Yes. |

## 2. Sentences the numbers do not support

- **fig2d calibration.** The record (fig2d-20khz notes and response), cell 41 and cell 47 all say: "the 20-kHz factor would have to be 0.64 to 0.97 times the 2-kHz one for the ratios to fall within tolerance". No single factor puts all four ratios in 1.8–2.2:
  - under reading (a) it would need to be at least 1.8/2.27 = 0.79 and at most 2.2/2.82 = 0.78;
  - under reading (b) the bounds are 0.79 and 0.78 again.
  The ratios differ among themselves by a factor of 2.82/2.27 = 1.24, more than the 2.2/1.8 = 1.22 the tolerance band allows. So calibration cannot rescue this claim, and the record should say so.
- **Cell 30 and the fig1-onset-delay notes:** "the other five, at 10 to 16 ms, are isolated APs". In cell 29, sub-11-1, sub-14-1 and sub-10-1 each show the first of 4 regular APs, not isolated APs. Their lowest tested field was already above threshold.
- **Cell 25 and the fig1-pure notes:** "Neither neuron is dimmer than the others (bright half over dim half 1.68 and 1.52, median 1.47)". That ratio measures contrast, not brightness.
- **Cell 52:** "0.04 do in every modulated session when the beats are shifted". The 0.04 is pooled over all modulated sessions (cell 20), not true of every session.
- **fig2-modulated notes and cell 52:** "under the first version of reading a, 12". This number does not appear in this notebook's outputs; it is a round-1 figure.
- **README:** "ROIs rebuilt from the paper's RATIO image". They are rebuilt from a RATIO image the notebook computes by the Methods' recipe, not from the paper's own image.
- **Finding on frame counts:** "2 have 1,400 and 1,800" should read one each (cell 14).

Everything else I checked against the outputs is supported. That covers the remaining Result cells, the Summary (cell 73), the README table and the record's notes and findings.

The record states my round-1 reasons faithfully. The reasons for the four Figure 5 / S3 claims are expanded from "Same as above" but are accurate.

## 3. Round-1 points

**Resolved:**
- Problems 1 (reading (a) counts plateau noise), 3 (summary scoring), 4 (full block test in part iii), 5 (001034 duplicate), 6 (TTX disclosure), 7 (strobe variants), 8 (redundant variant) and 10 (bleaching note).
- Problem 2 (calibration) is addressed, but the fig2d estimate is wrong, as shown in section 2.
- Problem 9 (c7's trace used as the bleaching reference for the other neurons) is unchanged; it does not bear on a conclusion.
- All six "could not check" items now have outputs: AP overlays, short-latency traces, the field cross-check, the traces of the two neurons never excited at 20 kHz, the gluconate series check, and the strobe frame timing.

**What still bears on a conclusion:**
1. **fig3c (iii):** the failure rests on detections at the detectors' own false-positive rate (section 1).
2. **fig2d calibration:** the statement must be corrected. The corrected version strengthens not_reproduced.
3. **Pooling across dandisets:**
   - 001035 alone gives a 2-kHz threshold of 58.3 V/cm, inside 57.7 ± 3.6 (cell 46), and a near-threshold latency median of 101 ms, inside 90–220 ms (cell 27).
   - So the outcomes of threshold-2khz-unmodulated and fig1-onset-delay depend on pooling 001032, 001033 and 001035. That pooling follows the claims file's "where".
   - 001035 has no modulated sessions (cell 14), so Figure 2D cannot come from 001035 alone. Which neurons the paper used therefore cannot be settled.
   - The fig1-onset-delay notes should say the outcome depends on pooling.
4. **fig1-pure-sine-excites-all:** the outcome turns on one neuron, sub-10-4, whose events at 324 V/cm look like attenuated APs (cell 24). It is disclosed, and the outcome is correct under the criterion.

## End of run

18 turns, 4 minutes, result: success.
