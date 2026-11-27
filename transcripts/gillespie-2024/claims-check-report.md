I've checked and corrected the claims file, and it is ready for an attempt (`ready: true`). Nothing is committed.

**Checker:** `claims/gillespie-2024.yaml: 35 claims, 34 quotes, 126 statistical values, 6 problems`. The six problems are p-values it reports as not found (6.790e-7, 6.100e-10, 5.820e-9, 6.180e-4, 1.260e-7, 8.60e-9). I found each one in the text as printed; the checker doesn't match their trailing zeros. All 14 values I added were found. Every quote passes.

I also read the paper's code at the commit the file cites (ad5801a) to check the criteria. Most of the code details in the file hold up. These didn't:

**Changes, by claim**
- **trialwise-pre-post-correlation:** the criterion said the code computes r per epoch and offered three readings. The code pools trials of both types across epochs that have more than 10 NF and 10 delay trials, and computes one r per rat. It prints that value labelled "r2", but it is r. The criterion now follows the code, with NF-only and delay-only as variants.
- **fig3bc-speed-matched-rates:** the code takes control trials of all types below the 25th percentile of the type 1 trials' speeds only. That is why the control counts in the Figure 3B legend aren't a quarter of the trials. The criterion now follows the code, with the other reading as a variant. I also added the Figure 3B speed tests, which back the "much higher mean speeds" part of the quote.
- **fig2b-control-timecourse:** the statement had turned "much higher than the manipulation cohort after reward" into a comparison within the control cohort. It now says only what the paper says of the control rats: they rarely generated SWRs before reward. The criterion now says how "rarely" is judged, since the paper doesn't quantify it. The comparison with the manipulation cohort stays in fig2b-manipulation-timecourse.
- **fig2d-swr-counts:** added the pre-reward and pre-plus-post NF vs delay ranksums from the Figure 2D legend, and added the pre-reward ranksums to the criterion.
- **fig5s1-control-search-efficiency-increases and the header:** the definition of an error trial was wrong. The code marks an error by a task phase whose fractional part is above 0 and below 0.85.

**Still open (recorded in `checks`)**
- The dandiset may not hold the epoch flags the code uses to pick control epochs (ripthresh, forageassist, gooddecode). The two link claims name the readings, and the trial and epoch counts will show which one holds.
- Two method details have both readings named in the claims that use them:
  - whether the offline SWR threshold is computed over the whole epoch or only over immobile times;
  - whether replay is classed by the Methods' 0.8 threshold on the continuous model or by the code's max_state.
- The trigger delay per rat is 75, 100, 50 and 50 ms in the Methods and code, but 100, 50, 75 and 75 ms in the Figure 1-figure supplement 1B legend. No claim rests on these values.
- One sentence in the Results has no claim: that per-trial pre- and post-reward SWR rates and dwell times weren't consistently correlated. The paper gives no values for it.

All of the paper's main findings have a claim, and every claim comes from this paper.
