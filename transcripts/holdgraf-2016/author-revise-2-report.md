I left all 26 outcomes as the round-2 verifier agreed them. For two claims I wrote a proposed change to not_reproduced under `proposed`, for round 3 to review. The entry re-ran cleanly with `python tools/entry.py all` (about 30 minutes, 0 errors), the checks pass, and the handover is built.

**Proposed changes**
- **supp6a-connectivity-increase and supp6a-after-closer-to-middle** (both now `reproduced`): proposed `not_reproduced`.
- The verifier's minor point was that the coherence is integrated from 2.5 Hz. With NW = 4 on 400 ms windows the tapers average the spectrum over ±10 Hz, so the bins below 10 Hz include 0 Hz. The claims file says to integrate "from the lowest resolved frequency", which here is 10 Hz.
- I added a variant that integrates from that half-bandwidth (10 Hz at NW = 4, 5 Hz at NW = 2):
  - **Connectivity:** no increase in either target region (frontal P = 0.46, temporal P = 0.72 at NW = 4; 0.23 and 0.41 at NW = 2). Of the frontal increase of 0.27 bits/s, 0.22 sits in the bins below 10 Hz.
  - **After-closer:** AFTER is not closer to MIDDLE in either region at either bandwidth.
- fig4a and fig4b still hold under this variant (late window P = 0.019 and 0.0099; fig4a P = 0.013 and 0.0019). supp7 isn't affected, since it uses 3 s windows.

**Added and corrected**
- **Drift check for strf-r-count:** I split each subject's MIDDLE trials into halves and searched shifts from −1 to +1 s.
  - S01, S02, S04 and S13 have the same best shift in both halves.
  - S03, S07 and S08 differ between halves. But no shift in either half gives more than 4 electrodes a positive held-out R2, and S07 gives none.
  - On the wider grid, S07's best shift over all trials is −0.6 s, still with no electrode above 0. No offset or drift I found raises the count.
- **Wording the verifier flagged:**
  - supp3a: the speech and pink-noise data have equal triplet counts, means and s.e.; they differ in the time course.
  - supp5b: under the per-trial baseline, the "no change" result holds only with the grouped bootstraps.
  - fig4a: removed "mostly the bias of single-trial coherence", since nothing measures the bias.
  - Summary and README now name supp6a-connectivity-increase, supp6a-after-closer-to-middle and supp7-envelope-coherence as resting on the bandwidth, in place of fig4b.
- **Record:**
  - Round 2 is recorded under `verifications`, with the verifier's reasons for all 26 claims and my response to each.
  - The alpha note that was missing from the round-1 strf-r-count reason is now in.
  - The integration lower bound is listed as an assumption on fig4a and supp6a.
  - `runtime_minutes` is now 30.

**Not done**
- No new reader questions: round 2 found no new misreading of the paper, and the seed-set and RMS-unit questions are already in `questions/crcns-ac-4.yaml`.
- I didn't touch the existing changes in `tools/build_site.py`, which were already there when I started.
- I didn't verify MNE-connectivity's default lower frequency (5 cycles per window, 12.5 Hz here) because the package isn't installed, so it is cited nowhere.
