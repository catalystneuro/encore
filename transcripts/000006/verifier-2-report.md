**Round 2 verification: Economo et al. 2018, attempt 000006-economo-2018-02**

Cell numbers below are from the current notebook, which has been renumbered since round 1.

**1. Outcomes (31 claims in the claims file and the attempt record)**

I agree with all 31 stated outcomes.

- **28 claims where I agreed in round 1.** The re-executed outputs give the same numbers.
- **pt-upper-persistent, pt-cohort-control, pt-types-differ-in-timing (blocked).** In round 1 I gave each claim the outcome of its own test. I now accept blocked:
  - The claims file lists `depends_on: pt-upper-early-preparatory` for all three, and that claim is blocked.
  - The author cites a protocol rule that a claim depending on a blocked claim is also blocked. docs/protocol.md is not among my materials, so I am taking the rule as the author states it.
  - Each claim's own test is reported fully:
    - persistent: not reproduced (68 and 160 of 420 bins; p = 0.053 and 0.058; cell 76).
    - cohort-control: partially reproduced (cell 115).
    - timing: partially reproduced if the dependency rule is not applied (cell 120).
- **pt-types-account-for-all-pt (partially reproduced).** I still agree, but its criterion has no outcome rule at all, so "partial" is a judgement.

**2. Sentences the outputs do not support**

- **Cell 124 (Summary):** "the unidentified pools are about half the paper's". This holds only for the PTupper cohort (232 of 495). The PTlower cohort has 430 of 511, which is 84% (cells 11 and 13).
- **README:** "the notebook shows this and rebuilds the trials from the stored order". Spikes are given to trials by time window on the file's clock, not by stored order (cell 10). The author's own response to my problem 3 says spikes are not reassigned. Only the last licks and the bursting trial boundaries use stored order.
- **README:** "Run on the processed data for only the 100 units the dandiset holds, the code gives the dandiset's counts and test results". Cell 122 shows several differences:
  - selective units: 97 against 99
  - rectified PTupper units at 70%: 9 against 8
  - PTupper units in the top 21: 15 against 16
  - PTlower decay p: 0.474 against 0.348
  - rule (ii) under projection (a): holds, against fails
  - PTupper CDgo onset: 82.5 against 77.5 ms

  "Most counts and test results" would be accurate.
- **README:** "raises every unit's baseline rate by about 1 Hz". Every unit's rate is higher, but the rise ranges from 0.14 to 6.47 Hz. About 1 Hz is the median (cell 122). Cell 123 states this correctly.
- **README:** "Where the remaining open readings give different outcomes, the claim is blocked." This leaves out the three claims blocked through a dependency, whose own readings agree with each other.
- **Cell 112 and the record's notes for pt-lower-movement-termination:** "The paper's units, with their own last licks, give the same pattern as the dandiset with all trials." This is true for PTlower only. For PTupper, CDgo selectivity on the dandiset is significant before the last lick (0.825 to 1.0 of bins) and after it (4 to 10 bins). On the paper's units it is significant at 0 bins (cell 108).
- **Cell 92, cell 124 and the record's notes for pt-upper-decoding-rectified:** the PTlower mean leaves tolerance "with the files, whose baseline rates … are higher". The notebook shows that the files and the processed data differ on the same units (56.20% against 56.84%). It does not isolate the baseline as the cause, so this is plausible but untested.
- **README:** "about twelve minutes". The run took 591 s (cell 125). This is minor.

Every other "**Result:**" sentence, the rest of the Summary, and all the outcome notes and findings in the record agree with the printed outputs. I checked every number against the tables in cells 26 to 123.

The record states my round-1 reasons faithfully and in my words, including problems 1–10 and the section C gaps. There are two small points:
- It attaches problem 3 to pt-spike-rates-similar without saying that I rated it "does not affect a conclusion".
- It does not record my caveat that I did not download the Figshare Seq and Axons files myself.

**3. Round-1 points**

Resolved:
- **Problem 1 (missing sessions):** confirmed as the cause by the same-unit variant (cell 122) and recorded as a finding.
- **Problem 3 (spikes from neighbouring trials):** quantified. Baseline rates are a median 0.97–0.99 Hz higher. The files change only the rectified PTlower mean, rule (ii) under projection (a) and the decay p, and no outcome changes.
- **Problem 4 (rebuilt last lick):** the False result is now stated in the conclusion.
- **Problem 5 (truncated lick-aligned rates):** 0.16% and 0.17% of unit-trials.
- **Problem 6:** now in the notes.
- **Problem 9:** the one-bin difference with no uncertainty is stated.
- **Problem 10:** reconciled as 143 good-quality units plus 7 Fair PTlower units.
- **AA0134:** the structures of its axon nodes are listed (cell 31).
- **BL648 images:** image counts and sizes are given. The pixel size was read outside the notebook.
- **The three outcome disagreements:** settled by the dependency rule.

Partly resolved:
- **Problem 8 (onset offset):** narrowed down. PTlower's onset is the 37.5 ms bin in the files, in the same units processed, and in all the paper's units (cell 95), so the gap comes from the method here. What in the method causes it is not found. It does not change the outcome.
- **Problem 7 (cohort-control direction):** reported and asked in questions/000006.yaml. It is still a claims-file issue, but the outcome is blocked anyway.

Still open and bearing on a conclusion:
- **Problem 2 (claims file):** count criteria that 100 units cannot reach. This is pending the reader's answer in questions/000006.yaml. It decides:
  - pt-selective-any-epoch (not reproduced; the fraction is 0.99 against 0.94)
  - the count parts of pt-preparatory-activity, pt-lower-bursting, pt-upper-decoding and pt-upper-decoding-rectified (each partially reproduced)

  The same-unit variant shows that the processed data give the same counts on the same units.
- **The dependency rule:** I could not read it in docs/protocol.md. If it differs from how the author states it, pt-upper-persistent would be not reproduced, and pt-cohort-control and pt-types-differ-in-timing would be partially reproduced.
