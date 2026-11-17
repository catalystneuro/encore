**Verifier report, round 2: gao-2018-01**

I checked the outcomes against the claims file (45 claims) and the attempt record (45 outcomes). The record counts 11 reproduced, 5 partially reproduced, 3 not reproduced and 26 blocked. The notebook Summary (cell 87) and the README count 10, 6, 3 and 26. The whole difference is `cd-captures-selectivity`, covered in 1a.

### 1. Outcomes and assumptions

I agree with 44 of the 45 outcomes as recorded: all 26 blocked ones and every tested outcome except the one in 1a. On the disputed ones:

- **fig3d** (not reproduced): agree.
- **fig3e-alm-increase-decrease** (partially reproduced): agree.
- **fig2cd** (partially reproduced): agree. The CN half is missing, so it cannot be fully reproduced in any case.
- **fig3e-alm-mean-rate-unchanged** (partially reproduced): I now accept this. The claim's two parts are the absence test and the rate level; the absence test passes under the unpaired test and the rate level fails under every reading. But see 1b.
- **fig4-fastigial-activation-alm-latency** (partially reproduced): I now accept this. The latency is in tolerance by bin start and by bin centre (cell 57); the count fails under every reading.
- **fig3f** (reproduced): agree. Judging by most of 20 draws is a stated deviation.
- **fig4e** (reproduced): agree, with the power caveat in section 3.

**a. `cd-captures-selectivity` has the wrong outcome in the record.** The `outcomes` entry says `outcome: reproduced`. Its own verification response says "Changed from reproduced to partially_reproduced". Cell 81, the Summary and the README all say partially reproduced. The numbers support partially reproduced (cell 80):
- Under the chosen reading (independent trials, trial-type means, squared ratio) the selectivity is 62.1%, inside tolerance.
- The variance is 34.2%, outside 22.8 to 31.2%.

The `assumed: true` flag and its stated assumption are correct and reasonable for a partially reproduced outcome.

**b. fig3e-alm-mean-rate-unchanged is missing `assumed: true`.** The claims file's criterion says "the outcome is marked as resting on the reading when paired and unpaired disagree". They disagree here: unpaired p = 0.214, paired p = 0.022 (cell 47). The author's case for the unpaired test is reasonable: the paper's p = 0.58 for a 0.24 spikes/s change fits an unpaired test. But the record has to state it as an assumption.

**c. No other outcome rests on an unstated assumption.**

### 2. Text against the printed outputs

Almost every number checks out. These are the exceptions:

- **Attempt record, cd-captures-selectivity:** `outcome: reproduced` contradicts cell 80 and every other text (see 1a).
- **Cell 48 and the fig3e notes:** "The rates are about 19% below the paper's 4.15 and 4.39 spikes/s." Only the control rate is about 19% below (3.379 against 4.15). The photo-inhibition rate, 3.767 against 4.39, is about 14% below.
- **Cell 39 and the fig2cd notes:** "The paper says the epoch gave qualitatively similar results, so the peak's place holds under one of the three epochs only." The paper's sentence is about *preparatory* activity: "yielded qualitatively similar preparatory activity". On these data the preparatory part is similar under every epoch (cell 38: sample-epoch intervals above 0 and delay mean above sample mean in all six rows). The peak's position is outside what that sentence covers, so there is no conflict with the paper.
  - The claims file's E3 paraphrase ("the paper says the epoch choice gave qualitatively similar results") drops "preparatory activity". I am reporting that as a misreading, not correcting it.
  - My own round-1 reason for fig2cd made the same overstatement.
  - The outcome does not change.
- **Cell 67 and the fig4g notes:** "much of the late dentate effect follows the mix of lick directions." Cell 66 supports the comparison with the pre-onset level (4 of 15 bins above it). It leaves out that all 15 bins of that variant still exceed the 1% chance level. This is a minor omission and does not decide the outcome.
- **Finding on `photo_stim_id`:** "to code 6 does not (2.8 to 2.9)". Cell 9 shows 2.95 to 3.00 early in the delay and 2.93 at its end. The point that code 6 does not fade holds, but the numbers are loose.
- **Two findings have no printed output behind them:**
  - The BAYLORCD8 20171020 finding ("end at 7221 s … last 127 of 462 trials, to 8481 s"). Cell 6 prints only the 120 trials left out.
  - The 25 kHz finding ("including the 32-channel recordings … 25 kHz"). Cell 5 prints only the 20 kHz rate.

Everything else in the "**Result:**" cells, the Summary, the README and the record's notes matches the outputs. This includes the sensitivity figures in cell 86, the fig3f draw counts and ranges in cell 54, the fig4f and fig4g bin fractions in cells 63 and 66, and the latencies in cells 43, 57 and 60.

**My round-1 reasons in the record:** they are in my own words. They are close to my round-1 table, with the relevant problem text added. The only slight misplacement is that problems 5 and 6, which I had marked as not affecting a conclusion, are attached to the fig4f and fig3d reasons. Problem 6 does bear on the fig3d latency, so that is acceptable.

### 3. Round-1 points: what is resolved and what remains

**Resolved:**
- **B2:** fig3f is now judged over 20 draws (15 and 13 of 20 pass in the last 500 ms).
- **B3:** resolved in the notebook and README, but not in the record (see 1a).
- **B4:** a split-half selection variant gives the same pattern; the outcome was changed.
- **B5:** a within-trial-type variant and the last-pre-onset-bin comparison were added.
- **B7:** hemispheres are handled.
- **B9:** the run without the five clock-check sessions changes no outcome.
- **B10:** the fig1l early-lick test was added.
- From my "could not check" list:
  - unit-table columns and file groups: cell 6;
  - the per-code time course: cell 9;
  - the onset time course: cell 44;
  - the lick-early crosstab: cell 7.
- Also resolved: the count/fraction fallback is now applied correctly, and the observation-interval bug was fixed.

**Remaining, where it bears on a conclusion:**
1. **B1, the unit-count excess, is still unexplained.** The units table has no quality field, and there are 195 inhibition-session neurons under 0.5 spikes/s. It decides:
   - the fig3d count;
   - the fig3e-alm-increase-decrease counts;
   - the rate level in fig3e-alm-mean-rate-unchanged;
   - the fig4 count.
2. **The fig3d latency is unstable (B6).** The bootstrap s.d. is 11.5 to 14.7 ms, against 3.8 in the paper. Without the five clock-check sessions the bin-start mean is 9.89 ms, inside tolerance (cell 86). So fig3d's not reproduced holds on the latency only with those sessions included, and on the count, which depends on B1. The time of photostimulus onset still cannot be checked, because the files hold no laser trace.
3. **Two record fixes are needed:** set the cd-captures-selectivity outcome to partially reproduced (1a) and mark fig3e-alm-mean-rate-unchanged as assumed (1b).
4. **fig4e:** only part of the per-neuron loss of significance is due to the effect itself. 86–88% of neurons lose significance, but 65–75% would lose it from trial count alone (cell 69). The low photo-activation trial count also holds down the "gain" count. So the outcome rests mainly on the population difference interval, which is solid.
5. **Not addressed, outcomes unaffected:** B8 (the bootstrap is conservative, which favours the absence claims; fig1g-dentate has p = 0.108, and its ipsi trials give 0.041) and B11 (recording sessions instead of the paper's behaviour sessions; stated).
