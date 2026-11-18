I've revised the attempt in reply to the round-2 report, re-run the entry, and both notebooks pass with `tools/entry.py check` at 0 errors. The final run gave the same numbers as the run before it, and every number in the edited text matches the output.

**Outcomes.** None changed. The counts are still 31 reproduced, 11 partially reproduced, 7 not reproduced and 1 blocked.
- **ed4d-gabazine-rank-order and supp10b-rank-order-by-model:** I agree with the verifier. The criterion requires both normalisation readings, and they disagree:
  - For ed4d, the per-recording ratio medians fall in MO14, so the ratio reading has not been shown to carry no information.
  - For supp10b, the claim passes in only one of the four combinations of normalisation and recording length.
  
  Both stay reproduced (assumed). A change to blocked, `methods_underspecified`, is written under `proposed` for round 3.
- I corrected my round-1 response for ed4d. It said the verifier had found the ratio reading uninformative; the verifier had concluded blocked and did not recommend the z-score.

**Added.**
- **A run without MO3.** A new notebook section refits every judged contrast that involves murine organoids without MO3.
  - Without MO3, the fig7b murine contrast holds (p 1e-4), so MO3 alone decides that outcome.
  - The first contrast of fig7d-murine-organoids-slices-same-lag stops being significant (p 0.14), but its second contrast fails as before.
  - The fig7c, fig7e, fig7a-primary and fig7d-lag results are unchanged.
  
  I kept the outcomes as tested on the five murine organoids with bursts, because the paper's code lists backbone units for all nine. The notes of each murine claim, and the murine finding, now say these results may come from burst detection settings the paper does not give for murine organoids.
- **Unit positions across drug conditions.** A printed check shows the ordered positions are identical between baseline and gabazine in MO10, MO11 and MO14, but not in MO13. They never match the NBQX with R-CPP recording. The `identifier_missing` finding and the ed4c conclusion now cite this output.
- **One rule for partial outcomes.** It is now stated in the summary and cited in the notes of fig1e, fig3f, supp26 and fig5f:
  - Where the criterion defines a partial outcome, the criterion decides.
  - Otherwise a claim is partial when its effect is present but falls short in one reading, organoid or contrast.
  - It is not reproduced when its central comparison fails, or when the data contradict part of it.
  
  Applying it changes no outcome.

**Corrected.** These are the sentences the verifier quoted:
- HO7 has 21 bursts, not 24.
- The data-check sentence no longer compares the murine organoids' median rate with other recordings (Pr2's is 0.685), only with their own peaks.
- The section on the second reading of the recording length now lists the fig7b murine sign change.
- The summary now says the 31 main recordings are in the dandiset.
- The claim that HO1 to HO4 match the paper's processed tables is removed from the notes, the summary and the README, because nothing compared them. What remains is that HO1 has the 46 bursts of Fig. 1C.

I recorded round 2 under `verifications`: all 50 claims, with ed4d and supp10b marked as disagreements (verifier's outcome: blocked).

**Not done.** I added nothing to `questions/van-der-molen-2025.yaml`, because the verifier found the claims file reads the paper correctly. Nothing is committed.
