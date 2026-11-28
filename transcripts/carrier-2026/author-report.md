I've finished steps 1 to 5 and run the handover (step 6). The entry passes `entry.py check` with 0 errors, and its notebook runs from a clean environment in 269 s. Of the 29 claims, 16 are reproduced, 2 partially reproduced, 3 not reproduced and 8 blocked.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| fig1b, fig1d (crab frequency unchanged in 0.75x and 1.25x) | reproduced |
| fig1e (crab crash fractions) | blocked, too_large |
| fig2b, fig2e (crab crash temperatures) | reproduced |
| fig2f-125-rises, fig2g, fig2h (crab Q10) | reproduced |
| fig2f-cb-mixed-model | partially_reproduced |
| fig2i-neuron-crash-counts | not_reproduced, rests on an assumption |
| fig2i-neuron-crash-temps-similar | reproduced |
| fig3b, species-frequency-at-10c, fig3c (lobster Q10, both species at 10 C, lobster phases) | reproduced |
| fig4b, fig4d, fig4e (lobster salinity series) | blocked, data_missing |
| fig5b, fig6a, fig6b (lobster LP and PY crashes) | blocked, too_large |
| fig5c-ha-mixed-model | partially_reproduced |
| fig5d (lobster Q10 by salinity) | not_reproduced (0.75x set P = 0.046; the paper has 0.063) |
| fig7a, fig7b, fig7c (Q10 between species) | reproduced |
| fig7e (crash temperature between species, 1x) | not_reproduced (P = 0.060; the paper has 0.047) |
| fig7df (crash temperature between species, 0.75x and 1.25x) | reproduced |
| fig8 (in vivo rhythm kept) | reproduced, rests on an assumption |
| fig9 (15-h mortality) | blocked, data_missing |

**2. The dataset**

Both records are pinned at their only published version (17624449 and 17794764). They hold the authors' tables and Prism files. My semi-log fits on those tables match the paper's Q10 statistics to every printed digit. I did not repeat burst detection on the roughly 51 GB of raw Spike2 recordings: the paper gives no burst criteria.

What I found in the data:
- **Two critical problems:**
  - Lobster 111122's 0.75x ramp in the tables, the Prism file, the MATLAB file and the burst workbook is a copy of 120722's. The two raw recordings differ.
  - In the in vivo data, 7 exposures are byte-identical to 7 others filed under another animal or salinity.
- **Major problems:**
  - Crab 963_106's 1.25x crash temperature is 36 C in the Prism file and 26 C in the unit table. These are the source of the paper's two crab 1.25x means (26.2 C and 27.28 C).
  - The lobster salinity series and the lobster LP/PY crash temperatures are not deposited.
  - Every "1Hour" in vivo exposure holds only about 32 min, and there are no survival records.
  - One crab 1x crash temperature is missing (20 values against the paper's 21). The authors' own stored Prism Welch test gives P = 0.0603 on these data.
- **Minor problems:** no analysis scripts are deposited, though the paper says they are. Lobster 888_156 has no raw recording. One lobster value is 4.68 Hz, far above the rest. The crab tables label 10 C with a date, list 888_136 twice and leave 888_145 out of the Animals sheet.

Assumptions:
- **fig2i:** I counted "all three neurons crashed at the same temperature" literally, which gives 4 of 20. Counting only the neurons that crashed gives the paper's 9 of 20, and then all ten counts match.
- **fig8:** the claims file's band rule, as its criterion says. That rule also passes 90 to 99% of windows of shuffled noise, so it cannot show a crash. With a stricter threshold set from the shuffled traces, 52 of the 58 exposures keep a band.

I recorded three questions for the paper's authors as `methods_unavailable` findings: the fig2i count definition, the in vivo crash criterion, and the specification of the mixed models and the Fig. 5D point sets. I asked a reader nothing.

**3. Where the protocol was unclear or did not fit**
1. "Compute every result from the data": I used the authors' per-preparation tables in the deposit, not the raw recordings, and recorded this as a deviation on every such claim.
2. `docs/archives.md` does not say that Zenodo serves about 1 MB/s per connection and answers HTTP 500 under load. I read in parallel (8 threads, about 16 MB/s) and retry failed reads.
3. "Opening a zip in place" does not work for zips nested inside a zip. I read the in vivo inner zips into memory and left the 37 GB of nested raw-crab zips unopened.
4. pyabf only opens file paths. To avoid writing to disk I parse the header with pyabf and read the samples from memory.
5. The protocol has no rule for a criterion that cannot tell a result from its null (only for ties). I kept the fig8 outcome under the criterion, marked it assumed, and showed the stricter variant.
6. The protocol says to adopt the "best-supported" reading but not how to weigh the paper's wording against the reading that fits the data. For fig2i I followed the wording.
7. "Count each recording once" conflicts with reproducing the paper's numbers, which include the 111122 copy. The main analyses include it and each has a variant without it. For fig8 the outcome is the same either way.
8. The paper's mixed models need R (lme4/lmerTest), which is not in the environment. I substituted statsmodels with Wald tests and recorded that as a deviation, without blocking those claims as `not_runnable`.

**4. Runtime and failures**

The run took about 55 min, from 17:39 to 18:35 UTC. One development read failed with Zenodo HTTP 500, which led to the retry logic. Nothing failed in the final run.

Files are in `entries/carrier-2026/`:
- `stns.py`
- `reproduce_carrier_2026.ipynb`

The attempt record is `attempts/carrier-2026-01.yaml`; the handover package is in `executed/carrier-2026/handover/`. The untracked dotfiles at the repository root were there before I started and are not mine.
