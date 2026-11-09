The claims file for DANDI:001027 is ready for an attempt: I set `ready: true` and recorded every change in a new `checks` entry. Nothing was committed or pushed.

**Checker result:** `claims/001027/10.1016-j.bioelechem.2023.108437.yaml: 18 claims, 18 quotes, 2 statistical values, 0 problems`.

**Changes, by claim**
- **Header:** notes that the paper does not say which array Fig. 5 used. Section 3.2 compares its control profile with the field of Fig. 3C, which points to the large array.
- **fig4-bipolar-weaker:** Section 2.2 names no test for Fig. 4. The criterion now says the Student's t-test from Section 2.4 is applied as a choice the paper leaves open.
- **fig4-sham-no-uptake:** the one-sample t-test against 0 is not from the paper. It is now described as the Section 2.4 test applied by our reading, and recorded as open.
- **fig4-twenty-fold-cancellation:** the "4 to 5-fold" figure in the statement comes from Section 3.4, which the quote did not cover. I added it to the quote, placed first because the checker needs the parts in text order.
- **fig5a-trains-stronger-throughout** and **fig6a-more-packets-more-uptake:** the outcome rule only said when the claim is reproduced. It now follows the protocol: both readings hold, neither holds, or they differ and the claim is blocked as `methods_underspecified`. It also says where the t-test is applied under each reading, and notes that the paper reports no test for these findings.
- **fig7bd-targeting-independent-of-amplitude:** comparing the center and half-way ROIs was the previous agent's own choice. The measure judged is now the normalized center value, which is the paper's own targeting index (Section 3.3, paragraph 1). Tests at the half-way ROI and at every ROI are shown as variants.
- **fig9b-gap-boosts-targeting:** I removed the clause "restricted almost exclusively to the center". It rests on the sample images in Fig. 9C, was not in the quote, and the criterion did not judge it.

**What remains open**
- **fig4-twenty-fold-cancellation:** the paper's 4 to 5-fold range does not match its own means for the 4-phase signal (126/20.8 = 6.1). The range is judged as the protocol requires, so data equal to the paper's own means would give only a partial result.
- **fig8a-more-uptake-near-electrodes:** the text says "~120 a.u. for packet 1", which I read as Packet 2. The 183% for Packet 2 in Fig. 8B and the center values support this, but the paper never corrects it.
- **Not fixed by the paper:** each of these stays as a named set of readings:
  - which array Figs. 5, 6 and 8 used;
  - whether monolayer intensities are background-subtracted;
  - which ROI counts as the center and which as most peripheral;
  - how peak width is measured for fig6-peak-narrower.
