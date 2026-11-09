There was one question, on `position-examples-invariant`, and I left the claims file unchanged.

**The claim stands.** The question asked whether 16 and 55 are the neuron counts of the similarity matrices, or only the neurons with a measured receptive-field center.

Figure 11 has two pairs of n:
- **Receptive-field panels (B and D):** n = 8 and n = 26. These are the neurons "with quantified RF centers" that the legend means.
- **Similarity matrices (panels A and C):** n = 16 (M2p9) and n = 55 (M2p28).

Two things in the paper confirm this:
- The legend says "Eight neurons that failed to yield an RF estimate are not depicted". The 8 neurons shown plus those 8 make the 16 in the M2p9 matrices.
- Figure 12A shows only similarity matrices for the same two penetrations, and labels them n = 16 and n = 55 again.

So the criterion's rule (counts within 10% of 16 and 55) uses the right numbers. Which dataset session matches them is for the author to decide from the data. The answer in `questions/001357.yaml` explains this, with `answered: 2026-11-02`.

`python tools/claims_check.py` reports 27 claims, 27 quotes and 0 problems. Nothing is committed.
