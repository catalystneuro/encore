I've worked through every point in the round-2 report and re-run the entry. No outcome changed and nothing is under `proposed`: none of the new analyses supports a different outcome. `python tools/entry.py all entries/zhang-2021` passes (0 errors, about 23 min). Nothing is committed.

**Stale numbers (point 1).** The text had been written from an earlier run on a different machine. I ran the entry three times here and the attention results came out identical each time, so this setup is deterministic. The notebook, the summary and the record now match this run:
- **fig1-csi-s2:** 0.739, 0.717, 0.676.
- **att-csi-group:** 0.663, 0.730, 0.525.
- **supp-csi-per-subject:** all 12 measured values replaced from cell 24; S3 passive under reading (b) is now p = 0.039.
- **att-passive-lower:** "2 or 3" is now 2 (S3 and S5) everywhere, with the null quantiles and p-values updated.
- **att-classification:** 53.3%, and a per-subject range of 40.4 to 60.6%.
- **README:** the runtime now says about 25 minutes, not 55.

**S7 not normalized (point 2).** The paper's Methods say responses were "normalized to zero mean and unit variance", so the video game data are now z-scored per voxel over the session. This is recorded as a deviation on all five game claims, citing that passage. A new variant cell repeats the S7 analyses on the data as stored. Results with S7 z-scored:
- **game-csi:** 0.582, against 0.581 as stored.
- **game-mutual-negative-projection:** -0.190 and -0.550.
- **fig3b-state-relations:** 21 to 26 significant pairs in S7.
- **game-classification:** S7 is 26.9 to 34.1% with contiguous folds.
- **game-weights-two-groups:** 3 to 5 dimensions still fail in S7.

Every outcome holds either way.

**att-weights-cortex margin (point 3).** The notebook now prints the mean weights under threshold (ii) and the EBA margin for each subject. Under (ii), S2 fails by -0.041, and S1 and S3 pass by 0.079 and 0.044.
- I added a much stricter threshold as a variant: Bonferroni over each subject's region voxels. The pattern then holds in 5 of 5 subjects for the OLS (B) and denoised (B_L) weights, and 4 of 5 for the state directions (Q_S).
- The conclusion now says the outcome depends on filtering voxels by the encoding model (3 of 5 without that filter). It does not depend on the liberal t test.

**Coarse prefrontal region (point 4).** I added a variant using only the medial prefrontal areas (12,185 vertices, against 57,895 for the whole region). The same dimensions fail under every reading. The notes now also say the game-weights outcome rests on S7 alone.

**Round 2 in the record.** It is under `verifications`, with the verifier's reasons quoted or closely paraphrased and my responses. For game-weights-two-groups I recorded `agrees: true`, with the reason starting "Agrees only conditionally", as the report puts it.

**Not done:**
- **Questions file:** I added nothing to `questions/zhang-2021.yaml`, because the report names no place where the claims file misreads the paper.
- **Problem 9:** the report notes that the round-1 permutation-bound point is not tied to a claim. I left it as it was, since the verifier says it affects no conclusion.
