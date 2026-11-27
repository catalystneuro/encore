**Round 2 verifier report: yang-2025-02 (doi:10.1109/tnsre.2025.3614867, DANDI:001212 v0.241023.0931)**

The claims file has 19 claims. The attempt record gives 19 outcomes: 14 tested and 5 blocked (data_missing). Cell numbers below refer to the re-executed notebook, whose numbering differs from round 1.

### 1. Outcomes and assumptions

I agree with all 19 stated outcomes. Every tested outcome has `assumed: true`. Each states its assumption in its deviations, and each assumption is reasonable given what the dandiset holds:
- seizure onset and end found from the LFP, with thresholds 1.5 and 3 run as variants;
- stimulation trains found from the LFP artifact;
- GC from OLS VAR fits with BIC order;
- for PSD and HFO, a post window that ends at the next train, with the worded window run as a variant;
- the HFO App dialog defaults over the 600 s epoch;
- the 180 s before onset as the IIS threshold baseline.

Agreements with qualifications:
- **tables1-network-stable-short-term (reproduced):** this holds only under reading (d), self-pairs included. Under reading (c) it holds in 5 of 7 rats, which is partial (cell 20). The criterion allows reading (d), and the record states the dependence.
- **fig3a-per-rat-site-differences (partially reproduced):** this rests on the unadjusted Dunn reading and sits exactly at the threshold of 5. Bonferroni gives 4 (cell 32).
- **fig5b-iis-post-seizure (reproduced):** this rests on reading (b), the paired t-test over 30 autocorrelated time bins, which the claims file names. Reading (a) gives p = 0.0013, which is partial.
- **fig6e-ictal-ripples-no-difference (reproduced):** the absence holds under the all-channels reading only, with p = 0.061.
  - The stimulated-channel reading at the main window and threshold gives p = 0.037, and 5 of 12 readings are significant with target lower (cell 51).
  - The measure's magnitudes (+1.46 and +4.22) are far from the paper's (about −0.16 and −0.04).
  - The record states all of this.
- **Blocked claims (5):** data_missing is right for all five, as I confirmed in round 1.
- **The claims file:** I found no misreading of the paper. The R5 and R6 order conflict with Figure S2 is between the data and the paper.

### 2. Sentences the numbers do not support, or state incompletely

Almost every sentence in the conclusions, the Summary, the README and the attempt-record notes matches the printed outputs. The exceptions:

- **Cell 33, and the fig3a-per-rat-site-differences notes:** "R1 has no significant pair, but R6 has one (DG-ANT, Bonferroni p 0.037 …)".
  - This is true only after Bonferroni adjustment.
  - Under the unadjusted reading the outcome rests on, R6 has two significant pairs: DG-ANT (p = 0.006) and DG-CA1 (p = 0.0195) (cell 32).
- **Cell 44, and the fig4b-psd-target-bands notes:** "With the difference measure beta rises … (stimulated channel …), but alpha and gamma do not [differ]."
  - This is correct for 0.5–120 Hz.
  - With 0–500 Hz on the stimulated channel, gamma does hold (unadjusted; KW p = 0.036, Dunn p = 0.011 and 0.022), and cell 43 lists "beta,gamma" as holding in some reading. The conclusion does not mention this.
- **Finding on R7, attempt record and Summary:** "the spectrograms of the seizures without trains show no stimulation comb".
  - Cell 12 shows one example epoch each for R7-05 and R7-07, and none for R7-01 or R7-03.
  - Cell 11 shows 2–4 s runs at the rat's own pulse rate in 2 epochs of R7-01 and 4 of R7-03, against 4 of 267 baseline epochs. These may be trains the 4 s rule misses.
- **Deviation text (several claims):** "[the first version] missed every train of R3-07 and most of R7-01 and R5-07".
  - The R5-07 part cannot be checked here.
  - My round-1 counts did not list R5-07 among the groups with few trains.
- **Cell 43, and "72 readings" (cell 44 and the notes):** the rel and log2 measures are rank-equivalent, so they give identical KW and Dunn p values. A third of the readings are therefore duplicates. This does not change the outcome.

**My round-1 reasons in the attempt record:** they are stated in my words and are faithful. Minor omissions:
- the fig3a-per-rat reason leaves out my R6 Bonferroni p and the R5 and R7 KW p values;
- round-1 point 10 (variants the claims file does not name) appears in no reason. It did not affect a conclusion.

### 3. Round-1 points

**Resolved:**
- 1 (R3-07 order): the date-based variant now gives 5 pairs unadjusted and 4 adjusted, the same as the main reading.
- 3 (post window can include the next train): the window is now cut at the next train (48 of 228 seizures), and variants are run.
- 4 (circular clock check): the check now uses the seizure found without the trains, giving 0.989 at no shift against 0.47 at ±30 s.
- 5 (pre-window length): the distribution is printed, and a 5 s pre-window variant is run.
- 8 (Figure S2 order): the conclusion now says this.
- 9 (HFO parameters): the defaults were read from the HFO App source at commit 1ccff19. I did not verify the source.
- 2 (stimulation groups with few trains), largely resolved:
  - R3-07 now has 8 of 8 seizures with trains;
  - the baseline detections are 7 of 267, all at the rat's own pulse rate;
  - a variant keeping only groups with trains in most seizures is added.

**Remaining that bears on a conclusion:**
- **Point 6, reading (d) for tables1-network-stable-short-term:** "reproduced" holds only with self-pairs; without them the result is partial (5 of 7 rats).
- **Point 7, fig5b-iis-post-seizure:** "reproduced" holds only under the time-bin test. Seizure-channels give p = 0.0013 (partial), and with the rat as the unit p = 0.23.
- **Point 9, fig6e-ictal-ripples-no-difference:** the absence holds under one channel reading. 5 of 12 readings contradict it, and the measure does not resemble Figure 6E.
- **fig3a-per-rat-site-differences:** partial at exactly the threshold, on the unadjusted reading only. Under that reading R6 has two significant pairs.
- **New, VAR misspecification:** the residuals are non-white in 83% of channel-windows, and the median largest eigenvalue modulus is 0.993, close to instability (cell 18). The three network outcomes all rest on these fits (tables1-network-stable-short-term, fig2-r1-target-shifts and figs2-target-assignment).

**Remaining that does not change an outcome:**
- Possible missed trains in R7-01 and R7-03, described above.
- The 7 baseline seizures that carry trains stay in the sham and baseline sets; no variant leaves them out.
- Dunn tests are still run after a non-significant KW (R5, R7).
