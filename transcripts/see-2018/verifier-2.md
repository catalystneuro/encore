# see-2018 · verifier-2 · run 43402374160

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 440
drwxr-xr-x 6 runner runner    4096 Nov 13 10:37 .
drwxr-xr-x 8 runner runner    4096 Nov 13 10:37 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 13 09:33 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 13 09:33 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 13 10:37 .claude
-rw-r--r-- 1 runner runner       0 Nov 13 10:37 .env
-rw-r--r-- 1 runner runner       0 Nov 13 10:37 .env.development
-rw-r--r-- 1 runner runner       0 Nov 13 10:37 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 13 10:37 .env.local
-rw-r--r-- 1 runner runner       0 Nov 13 10:37 .env.production
-rw-r--r-- 1 runner runner       0 Nov 13 10:37 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 13 10:37 .env.test
-rw-r--r-- 1 runner runner       0 Nov 13 10:37 .env.test.local
drwx------ 2 runner runner    4096 Nov 13 10:37 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 13 09:33 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 13 09:33 .github
-rw-r--r-- 1 runner runner       0 Nov 13 10:37 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 13 09:33 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 13 09:33 .mcp.json
[... 104 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; diff see-2018-01.yaml see-2018.yaml | head -50; head -80 see-2018.yaml
```

```
# See, Atencio, Sohal & Schreiner (2018) from CRCNS ac-3

Tests the findings of [See et al. (2018)](https://doi.org/10.7554/eLife.35587) that can be tested
on [CRCNS ac-3](https://doi.org/10.6080/K09021X1). The data set holds the 16 columnar recordings
(655 units) made in rat primary auditory cortex with the 10-min dynamic moving ripple and ripple
noise, and the stimuli. It does not hold the 5-s repeats (Figure 9), the 15 repeats of the 10-min
ripple noise (Figure 11A, B) or the 64-channel recordings (Figure 8).

| Claim | Outcome |
|---|---|
| 16 penetrations, 655 neurons, 104 cNEs, 6.5 per penetration | Reproduced |
| Example recording: 9 cNEs of 2 to 6 neurons | Reproduced |
| Number of cNEs grows with the number of neurons (R2 0.74, about 15%) | Reproduced |
| Mean cNE size 7.4 neurons, R2 0.33 against neurons | Not reproduced |
| 9 cNEs with a negative-weight member | Not reproduced |
| 68% of neurons in one cNE, 9% in none, 23% in several | Not reproduced |
| 82% of cNE pairs within 200 um | Reproduced |
| No depth bias of cNE members | Reproduced (on an assumed test) |
| 70% of cNEs span 200 um or less | Not reproduced |
| PWC sharpness and delay explain about 50% of the variance of the correlation | Not reproduced |
[... 161 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat see-2018-01.yaml
```

```
<persisted-output>
Output too large (47.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/cd361a45-74e7-4a41-a693-2a672d25f93a/tool-results/bu7slts5d.txt

Preview (first 2KB):
schema_version: 3
id: see-2018-01
datasets:
- archive: crcns
  id: ac-3
  version: unversioned
  doi: 10.6080/K09021X1
  relation: primary
paper: doi:10.7554/elife.35587
date: '2026-11-13'
entry: see-2018
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
[... 32 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/cd361a45-74e7-4a41-a693-2a672d25f93a/tool-results/bu7slts5d.txt"
}
```

```
1	schema_version: 3
2	id: see-2018-01
3	datasets:
4	- archive: crcns
5	  id: ac-3
6	  version: unversioned
7	  doi: 10.6080/K09021X1
8	  relation: primary
9	paper: doi:10.7554/elife.35587
10	date: '2026-11-13'
11	entry: see-2018
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-14
20	  runner:
[... 732 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -c '^- id:' see-2018.yaml; grep -c '^- claim:' see-2018-01.yaml; grep '^- id:' see-2018.yaml | sed 's/- id: //' > $TMPDIR/a; grep '^- claim:' see-2018-01.yaml | sed 's/- claim: //' > $TMPDIR/b; diff $TMPDIR/a $TMPDIR/b && echo same
python3 - <<'EOF' > $TMPDIR/nb.txt
import json
nb=json.load(open('reproduce_see_2018.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f"\n######## CELL {i} [{c['cell_type']}]")
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--\n'+''.join(o['text']))
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT--\n'+''.join(d['text/plain'])[:3000])
        if o.get('output_type')=='error': print('ERROR',o.get('ename'),o.get('evalue'))
EOF
wc -l $TMPDIR/nb.txt; grep -c 'CELL' $TMPDIR/nb.txt
```

```
31
31
same
2031 /tmp/claude-1001/nb.txt
101
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
3	# Reproducing See et al. (2018) from CRCNS ac-3
4	
5	**Paper.** See JZ, Atencio CA, Sohal VS, Schreiner CE (2018). Coordinated neuronal ensembles in
6	primary auditory cortical columns. *eLife* 7:e35587,
7	[doi:10.7554/eLife.35587](https://doi.org/10.7554/eLife.35587). The claims file
8	(`claims/see-2018.yaml`) was written from the version of record (PMC6017807) with its figure
9	legends, Materials and methods, and Supplementary file 1.
10	
11	**Data set.** [CRCNS ac-3](https://doi.org/10.6080/K09021X1) (See, Atencio & Schreiner 2018),
12	read from the public bucket `crcnsarchive` under `ac-3/live/`, zip files opened in place.
13	CRCNS data sets are not versioned, so the version is recorded as `unversioned`, the only one
14	published; the paper cites the data set by its DOI and no version. The files read have these MD5
15	sums in the data set's `checksums.md5`: `Data.zip` 3140d6178de9c044932901795a4cc817,
16	`Stimulus.zip` ce43beade196882598cecddff5520d7b (the notebook prints the listing it read).
17	The data descriptor is version 0.6 (March 28, 2018).
18	
19	**What the data set holds.** 16 recordings (`site1` to `site16`), 8 with the DMR (`rn1`) and 8
20	with the RN (`rn16`), 655 units, the 10-min stimuli and their triggers: the 32-channel columnar
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
700	
701	For every pair of units of a recording: the PWC (1-ms lag bins, +-100 ms and its central
702	+-50 ms), its sharpness and absolute peak delay, the correlation coefficient of the 10-ms binned
703	trains, the depth difference and Euclidean distance of the channels, and whether the pair shares
704	a cNE (sign reading a). The PWCs use the spikes inside the stimulus period, on the stimulus clock,
705	as the correlation coefficient does. As variants the claims file does not name, the sharpness is
706	also given with a baseline subtracted (the count per bin expected from the two rates, or the mean
707	of the outer +-50 to 100 ms of the histogram, the rest clipped at zero) and over +-10 and +-20 ms.
708	
709	######## CELL 40 [code]
710	t0 = time.time()
711	pairs = pd.DataFrame([r for rows in pmap(cne.run_pairs, IDX, [main[s] for s in SITE_IDS]) for r in rows])
712	print(f"{len(pairs)} pairs in {time.time() - t0:.0f} s; pairs without any spike difference within +-50 ms: "
713	      f"{(pairs.count_50 == 0).sum()}")
714	print(pairs[["r", "sharp_50", "delay_50", "sharp_100", "delay_100", "depth_diff", "euclid"]].describe().round(3).to_string())
715	print("\nsharpness variants (not readings of the claims file): baseline subtracted, from the two rates (ind) or the "
716	      "outer +-50 to 100 ms (flank), and narrower windows")
717	print(pairs[["sharp_50_ind", "sharp_50_flank", "sharp_100_ind", "sharp_100_flank", "sharp_20", "sharp_10"]]
718	      .describe().round(3).to_string())
719	--OUT--
[... 630 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1350,
 "limit": 700
}
```

```
1350	      2   177 0.357   0.328
1351	      5   139 0.512   0.475
1352	      8   116 0.629   0.602
1353	     10   104 0.679   0.658
1354	     15    89 0.718   0.707
1355	     20    82 0.723   0.709
1356	     35    65 0.730   0.732
1357	     50    60 0.709   0.696
1358	   peak of the mean at 35 ms, of the median at 35 ms
1359	projection quadratic, events (b):
1360	    bin  cnes  mean  median
1361	      2   177 0.151   0.121
1362	      5   139 0.119   0.087
1363	      8   116 0.097   0.078
1364	     10   104 0.085   0.073
1365	     15    89 0.081   0.071
1366	     20    82 0.064   0.058
1367	     35    65 0.056   0.056
1368	     50    60 0.075   0.070
1369	   peak of the mean at 2 ms, of the median at 2 ms
[... 663 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import yaml
c=yaml.safe_load(open('see-2018.yaml'))
for cl in c['claims']:
    if cl['id'] in ('fig10c-strf-mi-higher','fig6c-spike-pwc-narrower-than-strf-pwc','fig11s3b-pr-strf-similarity','fig7e-no-depth-bias','fig10b-ptd-higher','fig5a-mi-peaks-10-15ms'):
        print('==',cl['id']); print(yaml.safe_dump({k:cl[k] for k in cl if k not in ('statement','quote','source')},width=120))
EOF
```

```
== fig5a-mi-peaks-10-15ms
criterion: Method from Materials and methods, STRF mutual information. cNE detection at bin sizes 2, 5, 8, 10, 15, 20, 35
  and 50 ms; activity interpolated to 1 ms; per cNE a threshold giving 5000 events; STRF by event-triggered average; MI between
  STRF projections and events, from P(x|event) and P(x) of the projections z-scored, extrapolated to infinite data by a line
  through the means of 20 subsamples at 90, 95, 97.5, 99 and 100% of events against the inverse fraction. Open are the STRF
  time window, the number of projection bins, and how MI is summarised over cNEs at a bin size. Readings for the summary (a)
  mean over all cNEs; (b) median over all cNEs; the window and bins are taken as standard choices and stated. Reproduced when,
  under one summary reading, the largest value falls at 10 or 15 ms.
id: fig5a-mi-peaks-10-15ms

== fig6c-spike-pwc-narrower-than-strf-pwc
criterion: The paper shows one example of each kind and reports no population test. The STRF temporal profile is the STRF
  averaged over frequency at each delay (Figure 6B, E legend); the STRF PWC is the cross-correlation of the two profiles;
  its sharpness is measured as for spike PWCs. Read over all pairs of the 16 penetrations, the claim holds when the spike
  PWC is sharper than the STRF PWC for more than half of cNE pairs, and the ratio of spike to STRF PWC sharpness is lower
  for cNE pairs than for non-cNE pairs (Mann-Whitney U, p < 0.05, the test of Figure 6J). "Most" and the ratio comparison
  are readings of "much narrower" and "often as wide", not the paper's.
depends_on:
- fig6j-sharpness-cne-pairs
id: fig6c-spike-pwc-narrower-than-strf-pwc
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "def \|rng\|default_rng\|random" cne.py | head -120
```

```
26:  independent sources) and the random seeds are standard choices that the paper does not fix.
48:  events, both normalised by the mean and SD of P(z), MI extrapolated from 20 random subsamples at
87:def _zip(name: str) -> zipfile.ZipFile:
91:def load_sites() -> list[dict]:
115:def load_stimulus(name: str) -> np.ndarray:
124:def load_params(name: str) -> dict:
130:def downsample(stim: np.ndarray, bin_ms: float) -> np.ndarray:
139:def to_stim_ms(site: dict, spikes_ms: np.ndarray) -> np.ndarray:
149:def stim_duration_ms(site: dict) -> float:
153:def binned(site: dict, bin_ms: float, units=None, t_range=None) -> np.ndarray:
167:def prepare(site: dict) -> None:
175:def zscore(counts: np.ndarray) -> np.ndarray:
182:def mp_bound(n: int, t: int) -> float:
186:def fastica(x: np.ndarray, seed: int, max_iter: int, tol: float, info: dict | None = None) -> np.ndarray:
190:    rng = np.random.default_rng(seed)
192:    w = _sym_decorrelate(rng.standard_normal((n, n)))
207:def _sym_decorrelate(w: np.ndarray) -> np.ndarray:
213:def _ica_weights(z: np.ndarray, vals: np.ndarray, vecs: np.ndarray, seed: int,
229:def orient(w: np.ndarray, reading: str) -> np.ndarray:
238:def pcs(z: np.ndarray):
[... 86 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "cne.py",
 "offset": 651,
 "limit": 55
}
```

```
651	def cne_events_10ms(det: dict, z: np.ndarray, projection: str, reading: str) -> list[np.ndarray]:
652	    """Event times (ms, stimulus clock, the centre of the 10-ms bin) of each cNE: activity above the
653	    99.9th percentile threshold; reading (a) every bin, (b) the peak bin of each run."""
654	    act = activity(z, orient(det["w"], "a"), projection)
655	    thr = det["act_threshold"][projection]
656	    return [(events_from_activity(act[j], thr[j], reading) + 0.5) * BIN_MS for j in range(det["n"])]
657	
658	
659	def _strf_measures(times: np.ndarray, stim: np.ndarray, rng) -> tuple[float, float, int]:
660	    idx = segment_index(times, STRF_BIN_MS, stim.shape[1], STRF_LAGS)
661	    strf = sta(stim, idx, STRF_LAGS)
662	    zall = projections(stim, strf)
663	    return float(strf.max() - strf.min()), strf_mi(zall[STRF_LAGS - 1:], zall[idx], rng), len(idx)
664	
665	
666	def run_cne_vs_members(i: int, det: dict, seed: int, heldout: bool = True) -> list[dict]:
667	    """Figure 10B, C: STRF PTD and MI of each cNE and each of its members, after subsampling the
668	    larger of the event and spike trains to equal counts. Also the MI with the STRF from held-out
669	    events (`strf_mi_heldout`), on the same subsampled trains."""
670	    site = SITES[i]
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import yaml
c=yaml.safe_load(open('see-2018.yaml'))
for cl in c['claims']:
    if cl['id'] in ('fig10s1-random-group-strfs','fig11c-models-number'): print(cl['id'], cl['criterion'])
"
```

```
fig10s1-random-group-strfs Random groups, summed spikes and equal-count subsampling as in fig9s1-cne-mi-above-random-groups; PTD and MI as in fig10b-ptd-higher and fig10c-strf-mi-higher. Reproduced when both signed-rank tests give p < 0.001 with cNEs higher and both KS tests give p < 0.001; partially reproduced when the PTD or the MI part holds alone.
fig11c-models-number Models from Materials and methods, Simulated spike trains. Shuffled, each unit's binned train shifted circularly by a random number of bins. PR, the full range of each unit's STRF projection values split into 15 equal bins, and spikes moved at random to time bins of the same projection bin. DG, binary 5-ms trains fitted for means and covariances and sampled with CorBinian (findLatentGaussian01, sampleDichGauss01), then rebinned to 10 ms. 200 iterations per model and penetration, mean number of cNEs per penetration. Open are the bin width of the PR shuffle and the STRF used for it; readings (a) 10-ms bins; (b) 5-ms bins; with the STRF of the same recording. Bonferroni over the three model comparisons of the panel, a reading, as the paper does not name the family (Figure 11 legend; Supplementary file 1 lists three comparisons per panel). Reproduced when, under one reading, all three corrected p < 0.05 with shuffled and PR fewer and DG more; partially reproduced when two of the three hold.
```

**Agent**

**Round 2 verification: See et al. 2018 (doi:10.7554/elife.35587) on CRCNS ac-3, attempt see-2018-01**

The claims file has 31 claims and the attempt record has 31 outcomes with the same IDs: 14 reproduced, 2 partially reproduced, 10 not reproduced and 5 blocked by missing data. I agree with 30 of them. The exception is fig10c. Its stated p-values, and those of fig10b, do not match the re-executed notebook. In this run the fig10c criterion is not met under any reading.

## 1. Outcomes

| Claim | Record | Agree? | Note |
|---|---|---|---|
| fig2bd, fig2eg, fig4s3, fig5a, fig6-member, fig7b, fig7-negative-weights, fig7c, fig7f, fig11d | not_reproduced | yes | Each follows from its printed output. For fig5a, the held-out check (cell 65) shows the miss does not come from in-sample MI bias. |
| fig4, fig4s2, fig5b, fig5c, fig7-totals, fig7a, fig7d, fig10b, fig11c | reproduced | yes | fig10b passes under all four readings in this run (p 8.0e-12 to 5.6e-4, cell 76), although the stated p-values are wrong (section 2). |
| fig10s1 | reproduced | yes | Passes with 500 groups (PTD p 3.7e-4). The PTD part fails with 100 groups on one other seed (p 0.0023, cell 82), which the notes say. |
| fig6j, fig11ef | partially_reproduced | yes | |
| fig8, fig9c, fig9s1, fig9s2, fig11ab | blocked (data_missing) | yes | |
| fig6c | reproduced, assumed | yes, changed from round 1 | The assumption (STRF PWC made non-negative by subtracting its minimum) is stated. It is reasonable: two more readings, absolute value (iii) and overlap-normalised (iv, which removes the taper I raised), agree. Rejecting clipping (i) rests on the paper's description of STRF PWCs as "broad". Both criterion parts pass under (ii) to (iv): 58.4 to 76.2% of cNE pairs, MWU p ≤ 1.1e-39 (cell 54). |
| fig7e | reproduced, assumed | yes | The assumption is the claims file's choice of test. It is stated and reasonable. |
| fig11s3b | reproduced, assumed | yes | The 5-ms PR bin is stated and reasonable. The notes also report that 10-ms bins fail (0.645). |
| fig10c | reproduced, assumed | **no** | In this execution the linear projection with event reading (a) gives p = 0.00153 (cell 79), above the 0.001 bound. The other three readings give 0.0076, 0.049 and 0.185, so none passes. Across all five subsampling draws, the reading passes in 2 (cell 79 prints `'linear, a': 2` for the four extra seeds). The held-out MI passes clearly (p ≤ 1.6e-8), but the criterion asks for the in-sample MI. On the printed output the outcome is not_reproduced. Choosing the linear projection because it is the reading that passes is also a weak basis for the assumption. |

## 2. Sentences the printed numbers do not support

These cells and record notes appear to have been written from an earlier execution:

- **Cell 77 and the fig10b record note:** "signed-rank p = 3.5e-12 … 1.9e-09 … 5.0e-04 … 1.3e-05". Cell 76 prints 8.01e-12, 3.75e-09, 0.000559 and 2.43e-05. The outcome holds.
- **Cell 80 and the fig10c record note:**
  - "only the linear projection with event reading (a) reaches p < 0.001 (p = 6.4e-04); the others give 0.0098 …, 0.044 … and 0.15". Cell 79 prints 0.00153, 0.00757, 0.0485 and 0.185.
  - "with four other seeds the linear (a) reading gives p = 4.2e-06, 0.012, 0.0029 and 4.9e-06, so it passes in 3 of 5 draws". Cell 79 prints 7.7e-06, 0.0012, 0.0036 and 1.5e-05, which is 2 of 5.
  - "59 to 65% of pairs, p = 2.2e-15 to 6.7e-08". Cell 79 prints 59.7 to 63.1% and p = 2.67e-14 to 1.6e-08.
- **Summary (cell 99), README and record:** "fig10c … reproduced, resting on an assumption (linear projection; 3 of 5 draws)" and "cNE STRFs have a higher MI than members' | Reproduced (on an assumption)" are not supported, for the reasons above.
- **The record's response to my fig10c reason:** "this run 6.4e-4". The re-executed notebook gives 1.53e-3. That is the same value as the author's first run, so the result changes from one execution to the next with fixed seeds. The record does not mention this.
- **Cell 66 and the fig5a record note:** "0.074 bits against 0.073 at 8 to 15 ms". Cell 65 prints 0.075 at 5 ms against 0.072 to 0.074. "2857 or 3362 at 2 ms": cell 65 prints 3360. "0.059 to 0.082 bits": the printed range is 0.058 to 0.082. "a tenth to a fifth as large" holds roughly for reading (a). Under (b) the ratio runs from about 0.04 to 0.27. None of these change the outcome.
- **Cell 55 and the fig6c record note:** "p = 2.0e-76". Cell 54 prints 2.43e-76. This is minor.
- **fig11c record note:** "a sampled run reproduces the real 5-ms covariances (… slope 0.66 to 1.04)". The covariance slopes are 0.657 at site 1 and 0.712 at site 16 (cell 86), so the DG sample under-reproduces covariances by about a third there. "Reproduces" overstates this. The outcome does not depend on it.

Everything else in the conclusions, the summary, the README and the record notes matches the outputs.

The verification block states my round-1 reasons accurately and in my own terms. It includes the fig6c and fig10c disagreements, and it folds in the relevant problems from my round-1 list and the "not checked" items.

## 3. Round-1 points

**Resolved:**
- Point 1, PWC sharpness scale: the mismatch is stated, variants are added and it is raised as a finding.
- Point 2, fig6j pair set: the both-members variant gives the same 14 and 12 of 16. I still think the claims file probably misreads the paper's non-cNE pair set. The record now raises this as a question for a reader.
- Point 3, fig6c: covered by readings (iii) and (iv).
- Point 4, fig5a: the held-out MI and the distinct-bin counts are added.
- Points 6 to 11: point 7 now uses 500 groups, point 10 now uses stimulus-period spikes, and the rest are stated.
- Section C checks: the DG fit, the PR spikes dropped and the ICA iteration counts are all printed now.

**Still open, and bearing on a conclusion:**
- **fig10c (round-1 point 5, now worse).** The printed run fails the criterion. The result also depends on the execution, not only on the seed. Either change the outcome to not_reproduced, or find and remove the source of the run-to-run variation and rewrite cells 77, 80 and 99, the README and the record against a single execution.
- **fig10b.** The outcome is unaffected, but its stated p-values must be replaced with the printed ones.
- **fig6c and fig6-member.** Spike PWC sharpness on the raw ±50 ms histogram remains off the paper's scale (12 ms against about 2). The fig6c comparison is therefore between two measures that are both off scale. The record states this as a question for the authors. It is a caveat on fig6c, not a reason to change its outcome.

## End of run

13 turns, 2 minutes, $1.36 at API prices, result: success.
