All 40 claims were tested and none are blocked: 35 reproduced, 4 partially reproduced, 1 not reproduced. The entry's checks pass (`python tools/entry.py all`, 0 errors), and the handover is built in `executed/hunt-2018/handover/`. I did not verify my own work and did not commit anything.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| sessions-and-trials, neuron-counts, choice-accuracy-ev, chose-on-partial-information, choice-accuracy-observed | reproduced |
| figs1ab-cue-weights | partially: monkey M weights probability and magnitude unequally (ratio about 1.11, Wald p about 1e-6) |
| figs1cd-fewer-cues-more-accurate | not reproduced under the criterion's measure; it holds under the paper's script measure (question to a reader) |
| fig2a, fig2b | reproduced |
| fig4d to fig4h, figs2, figs4, figs11 (RSA templates) | reproduced |
| fig4-t75-latencies | reproduced; at 1 ms steps all nine t75 values equal the paper's exactly |
| figs5c-latency-order | partially: the order holds, but the simulated t75 ranges overlap in every reading |
| fig5a to fig5k, figs67 | reproduced; the Fisher p-values equal the paper's (0.040, 0.067, 0.011, 0.003, 0.0003) |
| fig6a to fig6d | reproduced |
| fig6e | reproduced, but only under 2 of 48 readings (peak timing); the ramp itself holds in all |
| fig7a | partially: the criterion needs both significance levels in one time bin, which no bin gives (question to a reader) |
| fig7b, fig7c | reproduced |
| fig8 value, spatial (2 of 24 readings), attribute | reproduced |
| fig8-action-value-acc-dlpfc | partially: the tests hold, but no reading has both fractions within 18 ± 1.8% |
| figs9-ev16-correlation | reproduced (mean over neurons) |

**2. The dataset, assumptions and questions**
- **What it holds:** what the paper describes. The behaviour files give 25 F and 32 M sessions, with exactly 9,863 and 14,251 trials. There are 549 units in ACC, DLPFC and OFC across 24 and 29 sessions. Every unit file agrees with the units table, and the spikes line up with the trial events (the clock check passed).
- **The paper's code is in the dataset** (`scripts.zip`). I followed it where the claims file left a detail open. My GLM matches the T-statistics the authors stored to within 1.6e-6.
- **Findings about the data:**
  - The `average_firing_rate` field that selects units is undocumented. Neither whole-session nor trial rates reproduce 189/135/183; only the stored field does.
  - Unit files 681 to 724 store the subject as lower-case "m".
  - The docs name the folder `LTH_preprocessed_data`, but the archive holds `LTH_processed_data.zip`.
- **Findings about the paper:**
  - The scripts silently drop unit 87, so DLPFC analyses use 134 units, not 135; Figures 5 and 7 also drop unit 653.
  - The text describes the Figure 7a cue-3 tests as attribute trials, but they use option trials.
  - The Figure 6 script differs from the Methods (random halves, a 4-column design, fixed RT bins).
- **Assumptions:** none. No outcome is marked `assumed`.
- **Question for the paper's authors** (a `methods_unavailable` finding): please confirm the two thresholds the text omits, the |T| > 1.64 used in Figure 7 and the "pictures seen" accuracy measure behind Supplementary Figure 1c.
- **Questions to a reader** (`questions/hunt-2018.yaml`): two, on figs1cd (which accuracy measure) and fig7a (which significance threshold).
- **Version:** CRCNS is unversioned. I pinned `live/` and printed the MD5 sums of the files read.

**3. Where the protocol was unclear**
1. The claims reader did not read the paper's code because it is part of the dataset, so several criteria list readings that differ from what the code does (the firing-rate definition, the RT bins, thresholds, the variable set for Supplementary Figure 5C). I ran the criterion's readings, added the code's choice as a further reading, and judged by the criterion. The exception is neuron-counts, which I judged on the code's rate; that is recorded as a deviation.
2. The criterion's rule "reproduced under one reading" conflicts with step 1.6, which says the outcome is what all readings give. I followed the criterion and reported the reading counts in the notes (fig6e 2 of 48, fig8-spatial 2 of 24).
3. There is no rule for "partially reproduced" when a criterion has no partial clause but holds in part. I used it for figs1ab, figs5c and fig7a and explained each.
4. Reading a 1.1 to 1.7 GB HDF5 file over HTTP range requests was too slow (about 0.6 s per trial). I read each file into memory instead, as `archives.md` permits, and noted it.

**4. Runtime and failures**
- The notebook runs in about 13.3 minutes with 4.4 GB peak memory. The session ran from 18:36 to about 20:15 UTC.
- Nothing failed in the final runs. One development run crashed on a lower-case subject letter; I fixed that.
