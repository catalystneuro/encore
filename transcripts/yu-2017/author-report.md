The entry, record and handover are done, with the entry's checks passing (0 errors). I did not verify my own work, and nothing is committed.

## 1. Outcomes (32 claims)

**Totals:** 12 reproduced, 6 partially reproduced, 11 not reproduced, 3 blocked.

| Claim | Outcome |
|---|---|
| fig1-iap-map-counts | blocked, `not_runnable` (pooled count needs the W-track rats, hc-6) |
| fig1s4b-foraging-counts | not reproduced (14 IAPs and 180 MAPs, against 33 and 244) |
| fig1d-well-specificity | reproduced on the foraging rats (median 0.998) |
| fig1e-iap-lower-speed | reproduced on the foraging rats |
| fig1s4d-foraging-speed | reproduced (p = 2e-05) |
| fig1f-iap-smaller-coverage | not reproduced |
| fig1s1d-transition-interval | not reproduced (peak at 14.3 s, against 6.5 s) |
| fig2c-continuous-transition | reproduced on the foraging rats |
| fig2s1cd-theta-autocorrelation | reproduced on the foraging rats |
| fig2s1ij-theta-behavior-correlation | not reproduced |
| fig2s2-fewer-coincident-spikes | not reproduced |
| fig3c-iap-swr-activation | partially reproduced |
| fig3s3-iap-same-well-coactivity | blocked, `other` (only 2 IAP pairs) |
| fig4a-swr-counts | partially reproduced (0.720, 0.238 and 0.042; the last is out of tolerance) |
| fig4b-coactivity | partially reproduced |
| fig4s1b-offset-matched-coactivity | reproduced on the foraging rats |
| fig4s2c-spatial-proximity-control | not reproduced |
| fig4s3-overlapping-pairs | partially reproduced |
| fig4c-iap-swr-shorter | reproduced on the foraging rats |
| fig4d-iap-swr-lower-power | partially reproduced |
| fig4s5-cells-spikes-per-swr | not reproduced |
| fig4s67-matched-subsamples | reproduced on the foraging rats |
| fig4s8-interspersed | reproduced on the foraging rats (exactly at the 5% bound) |
| fig4e-iap-spike-earlier | reproduced on the foraging rats |
| pfc-unit-selection | partially reproduced (732 units against 712; 94 selected against 112) |
| fig5-pfc-modulated-fraction | not reproduced (0.33, against 0.63) |
| fig5dg-pfc-groups | not reproduced |
| fig5s1d-shuffle-control | not reproduced |
| pfc-regression-joint-swr | not reproduced |
| fig6c-similarity-index | blocked, `data_missing` (no beam-break times) |
| fig6e-coincidence-index | reproduced (the IAP-SWR+ side rests on 2 units) |
| fig6s2-no-proximity-difference | reproduced |

## 2. The dataset, assumptions and questions

**What the dataset holds:**
- The archive is one 8.7 GB `data.tar.gz`, and its MD5 matches `checksums.md5`. It holds the five foraging rats with the days the paper analysed (4, 9, 9, 11 and 12).
- Only the task sessions are included; the rest sessions are not.
- There are no beam-break or well-entry times, no well positions and no reward contingencies.
- No corpus callosum reference channel is included.

**Problems found:**
- **Spike widths:** in R1 and N2 the stored widths run about 0.2 ms longer than in the other rats, for CA1 and PFC units alike. The paper's < 0.4 ms rule therefore removes every R1 CA1 cell and all but 7 of N2's. Without the width rule in those two rats, the MAP count (250) and the PFC selection (113) fall within tolerance.
- **LFP alignment:** in R1 and N2, the tetrodes of one session start up to 45 ms apart. The notebook aligns them.
- **Descriptor error:** the data descriptor's summary calls the data set "hc-7".

**Version pinned:** `unversioned`. CRCNS does not version data sets, the paper cites none, and `live/` is the only copy of the data. The notebook header records the MD5.

**Assumptions** (outcomes marked `assumed: true`):
- **Wells:** located as the peak of immobile occupancy in each quadrant of the maze, pooled over an animal's days (claims-file reading O1 (b)). Entries and exits are the starts and ends of immobility periods.
- **SWR envelope:** the amplitude reading (O5 a). The squared reading puts the threshold below the mean on all 45 days, so it is shown but not used.
- **Coactivity z-scores:** taken from the exact permutation distribution, the limit of the paper's 5000 permutations.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- What envelope, histogram and SWR rate does the threshold use? The method as described gives about 2 SWRs per second of immobility here.
- How was the width rule applied in R1 and N2?
- Without beam-break times, which definition of a well visit reproduces the paper's entries, exits and 6.5 s interval?

I asked a reader no questions.

## 3. Protocol issues

1. archives.md says CRCNS data come as zip files opened with `zipfile`. hc-13 is one `tar.gz`, which can only be read from its start. I streamed it once, reduced each animal as it arrived, and computed the MD5 on the fly.
2. The `with_inputs` claims need hc-6, which is public but more than 28 GB, and the paper does not say which of its animals and days were used. No outcome category covers "input public but too big to process in this run". I tested these claims on the foraging rats, as their criteria allow, and blocked the pooled count as `not_runnable`.
3. The rule that a claim depending on a blocked claim is blocked conflicts with criteria that allow a foraging-only test. I tested the dependents of fig1-iap-map-counts on the foraging cell selection.
4. Partial outcomes: where a criterion defines its own narrow partial clause I followed it strictly (fig4s5, fig4s2c → not reproduced). Where it defines none I used the protocol's "holds only in part" (fig3c, fig4b, fig4d, fig4s3, pfc-unit-selection).
5. The protocol does not say what to do when a reading the claims file lists turns out degenerate. I showed O5 (b) in the data check and recorded why it was not used.
6. "Do not download to disk" does not address derived development caches. During development I kept pickled reductions in `$TMPDIR`; the notebook itself only streams.
7. `assumed` does not distinguish choices forced by missing data (wells without beam breaks) from open methods. As a result almost every tested claim carries `assumed: true`.

## 4. Runtime and failures

- **Run time:** the session ran from 12:31 to 14:18 UTC. The final notebook ran in 13 minutes (779 s, 6.1 GB peak). Three full runs gave identical numbers.
- **Failures:** none in the final runs. Development bugs fixed along the way were a MATLAB struct conversion, a missing import, empty groups, misplaced day-wise wells, and the 45 ms tetrode misalignment.
- **Stray files:** untracked device files (`.bashrc`, `scripts`, `.idea` and others) appeared at 12:27, before this run started. They are sandbox artifacts and I left them alone.
