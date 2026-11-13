I've finished steps 1 to 6 for `entries/asari-2009`. `entry.py all` passes: 0 check errors, and the notebook ran from a clean environment in 23.4 min. The record is `attempts/asari-2009-01.yaml` and the handover package is in `executed/asari-2009/handover/`. Nothing is committed.

**(1) Outcomes**

| Claim | Outcome |
|---|---|
| methods-recording-counts | partially reproduced (305/39 and 93/14 match exactly; 133 A1 cells meet the rule, not 123; no voltage-clamp data) |
| a1-mgb-firing-rates | partially reproduced |
| fig2-example-reliability | reproduced (0.310 ± 0.092 over cells; one cell gives 0.611 ± 0.081 and 0.737, matching the example) |
| fig2-example-long-context | partially reproduced (the late divergence starts at 3.97 s, 30 ms inside the criterion's 2 to 4 s window) |
| fig3a-proportion-significant | reproduced (186/305, late fraction 0.252, cumulative peak at 4.78 s) |
| fig3a-significance-decay | partially reproduced |
| fig3b-fractional-power-decay | partially reproduced (size 0.47 matches; time constant 1.3 to 1.8 s against 1.04 s) |
| timescale-longer-than-membrane | reproduced (73 and 78 ms) |
| fig4-predictability-upper-bound | partially reproduced (bound about 0.50 near onset; time constant 1.5 to 2.8 s) |
| fig4-strf-performance-low | blocked, `other`: not attempted in the time limit |
| fig5-example-conductances, fig6-conductance-decay | blocked, `data_missing` |
| fig7-example-frequency-context | blocked, `data_missing` |
| fig8a-proportion-by-property | partially reproduced (assumed) |
| fig8a-significance-fits | not reproduced (assumed) |
| fig8b-decay-by-property, fig8c-relative-effects | partially reproduced (assumed) |
| fig8-natural-synthetic-probes-alike | reproduced (assumed) |
| fig9-mgb-fast-decay | reproduced (time constant 0.080 s; the fitted sizes are smaller than the paper's) |
| fig9-example-first-bin | reproduced |
| figs1-silence-probe | reproduced |

**(2) What I found about the dataset**

- **No version to pin.** CRCNS data sets are unversioned, so I recorded `unversioned` and printed the MD5 sums from `checksums.md5` in the notebook header.
- **The paper's own analysis code is in the dataset** (`asari/Tools/CxtDep.m`). Where the Methods leave a step open, I followed it and cited it in `asari.py`.
- **Voltage clamp is missing.** All 346 of Asari's files are current clamp or cell-attached, so the Figure 5 and 6 claims and the voltage-clamp counts cannot be tested.
- **Cell counts.** The dataset holds 145 A1 and 14 MGB cells, against the 194 and 16 the paper recorded.
- **Figure 7.** No recording has the paper's three DMR frequency bands.
- **Figure 8 property sets.** Which conditioning stimuli vary which property is written down only in the notes of the 19-stimulus MHT recordings.
- **Summary.mat.** Two cells are listed in both the natural and the synthetic group. No two files hold identical traces.

**Assumptions.**
- For all five Figure 8 claims, I rebuilt the property sets from each recording's stimulus parameters. This recovers the paper's amplitude and higher-order probe counts (95 and 137) but only 39 AM and 25 FM probes, against 96 and 82.
- The natural-against-synthetic test comes from the claims file, not the paper.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- How are probes of different lengths averaged after a probe has ended?
- Which stimuli form each property set in Figure 8?
- How were A1 spikes detected, and which periods count as spontaneous and evoked?

I also recorded a `paper_inconsistency` (73/110 is printed as 64.6%) and a `code_mismatch` (CxtDep.m centres each trial over the probe, and counts silence as a context). I asked the readers no questions.

**(3) Where the protocol was unclear**

1. A claim with an expected value that cannot be measured (the voltage-clamp counts) still needs one number per expected value in `measured`. I recorded 0, the count in the dataset, and explained it in the notes.
2. Some criteria (fig3b, fig4) define only "reproduced", but the result holds in part. I used `partially_reproduced` and said so in the notes.
3. A claim not attempted for lack of time, where computation was not what stopped it, has no matching block reason. I used `other`.
4. The paper links no code, but its analysis code ships inside the dataset. I treated it as the paper's code and followed the ordering in reader step 2.
5. The protocol gives no tolerance for a criterion's time-window boundary (the 3.97 s against 4 s case). I applied the boundary strictly and recorded partial.
6. The requirement to break results down by animal is hard to apply to every claim. I added per-animal tables for the main A1 and MGB results.

**(4) Runtime and failures**

- The run took about 2 h 15 min, from 17:16 to 19:30 UTC.
- The notebook takes 23 min, with a peak memory of 2.9 GB. Most of that is streaming 2.8 GB of recordings once and running the 1000-shuffle significance tests.
- No run failed.
- I did not do the STRF analysis. Its data and the code `wehr/Tools/STRFanalysis.m` are in the dataset, but I estimated that the robust lowess fits alone would not fit in the time left.
