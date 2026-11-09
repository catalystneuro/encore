I've checked and corrected the claims file for 001199, and it is ready for an attempt. Nothing is committed.

**Checker:** `claims/001199/10.1523-jneurosci.2218-24.2025.yaml: 35 claims, 35 quotes, 84 statistical values, 0 problems`. It gave the same result before and after my edits.

**Changes, by claim**
- **Header D (dSTTC):**
  - The dSTTC tests had picked up Bonferroni correction through the shared test rule. The Methods name that correction only for the spiking tests; for dSTTC they say only "Post hoc one-tail two-sample Wilcoxon tests were employed". Correction is now open: C1 uncorrected, C2 Bonferroni. `fig10a-dsttc-3000-during` runs both.
  - The paper gives no window length for dSTTC. The header now says the 67 ms windows are borrowed from the spiking analysis.
- **fig4-no-fsu-change:**
  - The source said paragraphs 1 and 2. It now says paragraphs 1 and 3 and the Fig. 4 legend, which is where the "S1 FSUs at 3,000 Hz" part comes from.
  - The outcome rule called the claim not reproduced if only a decrease appeared. Under the increase-only reading it would hold, so the two readings disagree. The rule now blocks the claim as `methods_underspecified` in that case, as the protocol requires.
- **fig5a-sham-no-response** (and fig5b, which refers to it):
  - The writer had fixed the test direction to "increase". The paper doesn't state a direction, so both "increase only" and "either direction" are now read, with the same outcome rule as above.
  - One statistics entry covers all four groups at 201 to 268 ms, but its n listed only the two POm groups. It now lists all four.
- **fig7b-s1-fsu-dc-3000:** The criterion required 30% to be above 0.6%. The legend says only that they differ, so both directions are now read.
- **fig9a-s1-rsu-60dc:** The criterion called B1 "the ten pairs", which is B2 in the header. It now reads B1 as the five PRFs and B2 as the ten pairs.
- **fig10d-sttc-60dc, fig10e-sttc-30hz-dc:** The PRF and DC rankings used means only. The paper names neither means nor medians, so medians are added as a second reading.

**Coverage:** Every main finding in Results, Figs. 2 and 4 to 11, has a claim. All 35 claims come from this paper.

**Still open** (recorded under `checks`):
- The paper says its data are in dandiset 000946, and 001199's description differs from the paper. The author must find out which 001199 sessions, if any, match the paper's conditions.
- The text lost the dSTTC equation. The Cutts and Eglen form in header D is a reading; the text names no other.

**Ready:** yes (`ready: true`).
