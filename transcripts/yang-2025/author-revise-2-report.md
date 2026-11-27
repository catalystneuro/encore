No outcome changed and nothing is proposed for round 3. The verifier agreed with all 19 outcomes, and none of the new outputs gave a reason to change one. I re-ran the entry with `python tools/entry.py all entries/yang-2025`: the check gives 0 errors and the notebook runs cleanly in 496 s. I recorded round 2 under `verifications` in `attempts/yang-2025-02.yaml`, with the verifier's reasons in its own words and my replies under `response`.

**Corrections to the text**
- **fig3a-per-rat-site-differences:** the conclusion and notes now say that R6 has two significant pairs without adjustment (DG-ANT p = 0.006, DG-CA1 p = 0.020), and one after Bonferroni. They said one before. I also fixed a print bug, so the notebook now lists both pairs.
- **fig4b-psd-target-bands:**
  - The text now names the one reading where gamma holds: the difference measure on the stimulated channel, 0-500 Hz, unadjusted Dunn (KW p = 0.036; Dunn p = 0.011 and 0.022). Alpha holds in no reading.
  - A printed check shows the relative-change and log2 measures give the same p values in all 72 cases, so only 48 of the 72 readings are distinct tests. The text now says so.
- **R7 finding (record and Summary):** the old sentence said the seizures without trains show no stimulation comb, which only one example epoch each from R7-05 and R7-07 supported. The new text says:
  - in R7-05 and R7-07, none of those seizures has a comb run of 2 s or more;
  - in R7-01 and R7-03, 3 of 5 and 3 of 10 have runs of 2 to 3.75 s inside the seizure. These are shorter than the paper's 5 s trains and may be trains the 4 s rule misses.
- **The R5-07 remark:** "missed most of … R5-07" could not be checked, so I removed it from the three deviations. They now give the checkable counts: R3-07 had trains in 0 of 8 seizures before the detector fix and 8 of 8 after; R7-01 went from 1 of 12 to 7 of 12.
- **Round-1 reasons:** I added the parts the verifier said were missing: the R6 Bonferroni p = 0.021, the R5 and R7 Kruskal-Wallis p values, and round-1 point 10.

**New outputs**
- **Model fit behind the three network claims:** at the order chosen by BIC, the fits' errors are not white noise. I added a variant at a fixed order of 40. There the errors are close to white (median share failing the test 0.00, against 0.83), but the fits sit at the edge of stability: 54 of 266 seizures have an unstable window. The outcomes hold under this variant:
  - tables1-network-stable-short-term: 7 of 7 rats with self-pairs included, 12 of 14 means within tolerance;
  - fig2-r1-target-shifts: 4 of 4 nodes match;
  - figs2-target-assignment: 19 baseline groups match.
- **The 7 baseline seizures that carry trains:** I added a variant that leaves them out, for the network, duration, PSD and fast-ripple claims. No outcome changes. In the PSD comparison of other bands, beta stops differing (p = 0.062), but delta and high gamma still do.
- **Dunn tests only after a significant Kruskal-Wallis:** this gives the same 5 listed pairs.
- **Spectrograms:** a new cell lists the comb runs and shows a spectrogram for each of R7's four stimulation groups.

**Not done, and why**
- **Claims file:** the verifier found no misreading of the paper, so I added nothing to `questions/yang-2025.yaml`.
- **Disputed readings:** tables1-network-stable-short-term, fig5b-iis-post-seizure and fig6e-ictal-ripples-no-difference each rest on one reading the criterion allows. The verifier agreed with all three outcomes, so I kept them, and the record already states how each depends on its reading.
- **Possible missed trains in R7-01 and R7-03:** I showed the short runs but did not count them as trains. They are shorter than the paper's 5 s trains, and the existing variant that keeps only seizures with trains already covers this. The verifier said it does not change an outcome.

Nothing is committed or pushed.
