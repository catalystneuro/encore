I've made the round-2 revisions and re-run the entry with `python tools/entry.py all`. Its checks pass with 0 errors and the notebook runs in 261 s. Nothing is committed.

**Outcomes:** none changed and none is proposed. The verifier agreed with all 27 outcomes, and under the main reading none of the new checks gives a different result. Round 2 is recorded under `verifications` for all 27 claims, with the verifier's reasons and my responses.

**Added to the notebook**
- **Trace window:** the verifier said the 8 px window had no variant. A new section reruns the four Fig. 7 claims with windows of 4, 6, 10 and 12 px, with all six cells and without c5.
  - fig7a holds under every window from 4 to 12 px.
  - fig7b-reduced stays partial under every window and never meets the whole criterion.
  - fig7b-unchanged and the reseal/residual part of fig7c hold from 6 to 12 px but fail at 4 px (anodic pole at 760 V/cm, p 0.028).
  - The notes now also say that the 19 holding variants are not independent: the outcome turns on the edge trace.
- **c5 notch:** a new data-check cell shows where the trace sits in the pole arcs and where it dips.
  - The notch the verifier saw in c5's first file lies 22 to 35° from the cathodic pole, outside its ±5° arc.
  - In c5's 760 and 1000 V/cm files, though, a notch does reach the cathodic arc (8.8 and 8.2 px). Those low values push the cathodic pole towards a difference from control, and none is found (p 0.74 and 0.21).
- **fig7b-reduced:** the anodic reading alone is now counted. It meets the whole criterion in none of 22 variants, so under that reading the claim would be not reproduced.
- **fig7c:** a variant leaves out 1400 V/cm. With it, the test pulse finds no pole difference in 21 of 22 variants (smallest p 0.12).
- **fig7b-unchanged:** the mean-of-poles tests are now printed.

**Questions for a reader:** I added two to `questions/001525.yaml` and did not change the claims.
- Whether fig7b-reduced should allow only the anodic reading, given the paper's negative cathodic value at 1400 V/cm. That would turn the outcome to not reproduced. The paper's wording doesn't settle whether the omitted value is the test-pulse or the conditioning-pulse value, so the question asks which.
- Whether the fig7c pole comparison should leave out 1400 V/cm. This would not change that outcome.

**Text corrected**
- The clock finding now says 56 files, not 54.
- The dark-frame shift is now 2.17 points under the main reading and 1.33 without background subtraction, with amplitude shifts of 0.0 to 0.3.
- Bleaching is no longer said to account for the offset: the sign matches the paper's description, the size does not, and the source is called not established.
- The fig7b-reduced sentence on cathodic values now holds only for 1200 V/cm.
- The fig7b-unchanged paired-test sentence now includes the mean-of-poles values (p 0.018 and 0.016).
- The README's fig7c row now says the test pulse finds a pole difference after 1400 V/cm.

**Not done:** I could not confirm Eq. (2) on the rendered page 3 of the PDF, because this run has no PDF renderer either. The notebook and the record now say it was checked against the PDF's text layer only.
