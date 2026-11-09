No outcome changed and no change is proposed. The verifier agreed with all 51 outcomes in round 2. The final run of `python tools/entry.py all` passed in 663 s, and `check` reports 0 errors. Nothing is committed.

**Corrected or added**
- **3 M DEG counts (fig4b):** I did not change these numbers, because the verifier misread them. The verifier said cell 13 prints 98/137 and 91/45 when filtering at alpha 0.1. The re-run prints 95/136 and 88/45 at alpha 0.1. The 98/137 and 91/45 figures belong to the alpha 0.05 variant table, which were also the round-1 numbers. I fitted the 3 M separate model twice in the locked environment and got the same counts both times. The conclusion, notes, finding and README now say which alpha each count uses, and give 91/45 for the variant.
- **Mmp2:** I did not change this either. The re-run prints an adjusted p of 0.03787, so 0.038 is right.
- **fig4fg (ECM terms):**
  - The verifier asked for `assumed: true`, but the schema does not allow it on a blocked outcome. A new deviation says instead that running the term-size limit as a reading goes beyond the readings in the claims file, and that the outcome depends on it.
  - The notebook now shows how marginal the deciding 0.048 is: with one DEG fewer in the term it would be 0.113.
  - A new cell runs the ECM test on two other GO releases. With 2024-01-17 the deciding reading gives 0.046, the same split as the pinned release. With 2025-03-16 it gives 0.052, and all 16 readings give not reproduced. This confirms the verifier's concern. Taken over all three releases the readings still disagree, so the claim stays blocked as methods_underspecified. Both releases are added as inputs with their Zenodo DOIs.
- **fig4d:** the cell 22 wording is fixed. The top 10 without a size limit is filled by broad terms such as "behavior" and "system process", not by synaptic signalling.
- **fig4h:** the check now covers all 12 PNN genes under all four readings, and none is a DEG at 3 or 7 M under any of them. The notes and conclusion now say exactly that.
- **fig4c:** the notes now say that the 0.6 tolerance on the down count only allows exactly 6, which is how the claims file has it; the claims file is unchanged. The round-1 `reviewed` paragraph now mentions this point.
- **Record:** round 2 is added under `verifications`, with the verifier's reason and my response for each of the 51 claims.

**Not done**
- I did not compare against R DESeq2/apeglm, because R cannot be pinned in the entry's locked environment.
- No questions were added to `questions/001702.yaml`, because the verifier reported no new place where the claims file misreads the paper.
