I've answered every point in the round-2 report and the entry passes its checks. The final run of `python tools/entry.py all entries/souza-2026` took 41 min and printed the same numbers as before. Nothing is committed.

**Outcomes.** None changed and none is proposed for change: 17 reproduced, 14 partially reproduced, 7 not reproduced.
- **data-sessions-units:** the verifier still gives not reproduced; the record keeps partially reproduced. The disagreement is recorded in round 2. In reply: protocol step 1.6 lets an author adopt the best-supported choice when the paper does not settle a detail, and the verifier found that assumption reasonable.
- **layer4-suppression:** the verifier noted it would be partially reproduced if the paper used the stricter visual-area layer rule (median +0.089). I kept the outcome because that rule is in neither the Methods nor the criterion. It is already asked of the paper's authors (finding 9).

**Output added to the notebook.**
- **Atlas:** cell 72 now loads the Allen Institute's files next to BrainGlobe's when GIN answers. In this run the two volumes are identical (77,045,760 voxels, 672 structures), and all 54,045 units get the same area, layer and boundary distance from both. The record's inputs, the deviation, cell 71 and the Summary now say only what this run printed.
- **Counts the verifier saw unprinted:** cell 72 now shows that all 1,508 units with a non-positive coordinate have no layer, and cell 47 that each stored waveform has 82 samples.
- **RW- draws:** a second variant forms the correlations on each of the 20 RW- draws, then averages them. The paper's order is lost (0.304 / 0.322 / 0.354) and the block excess is -0.038. This is in the notes, the conclusions and the Summary.

**Corrected.**
- **Missing assumption:** fig2d-cv-correlations and cv-correlation-block-excess now carry a deviation saying they rest on correlating the averaged RW- series, citing Materials and methods 2.6.
- **Sentences the verifier quoted:**
  - the p range for fig1gi now runs to 2.3e-198;
  - the layer4-within-waveform sentence now says every excess is below the paper's, and only +0.124 is within tolerance;
  - the layer4-controls sentence on the unmatched value is rewritten;
  - cell 29 and the Summary now say 8 units differ between the null readings (net 4);
  - cell 48 gives both log-likelihoods (24,671 and 24,662).
- **Record:** round 2 is under `verifications`, with all 38 claims, the verifier's reasons and my responses. There is no round-2 `findings` list because no finding is rated `critical`; the verifier found the existing ratings right.
- **README:** the run time now says about 45 minutes.

**Not done.**
- **fig1e checks:** I did not run null 1b on all 104 sessions. It took 342 s for 12 sessions, so it would add about 50 min to a 41 min notebook, over the 60 min limit. I also did not run 1,000 permutations for all units, which is about nine CPU hours. The fig1e outcome therefore still rests on 100 permutations and null 1a; the response says why.
- **Questions file:** no question was added, because the verifier found no place where the claims file misreads the paper.
