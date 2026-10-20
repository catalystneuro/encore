The claims file is ready for an attempt. I edited only `claims/crcns-ret-1/10.1242-dev.027912.yaml`, with nothing committed or pushed.

**Checker:** `claims/crcns-ret-1/10.1242-dev.027912.yaml: 26 claims, 26 quotes, 6 statistical values, 0 problems`. This is the same result before and after my edits.

**Changes, by claim:**
- **Header:** it said the supplement "holds figures only, not methods". Nobody has read the supplement, so that is unsupported. It now says the supplement's legends may hold method details.
- **fig5-increased-apoptosis:** the criterion quoted the Figure 5 legend as "NBL". The legend prints "NBL/IPL", and it is now quoted as printed.
- **fig6f-amacrine-loss-central:**
  - The recorded p < 0.0001 was a guess. The legend defines three significance marks and the text does not say which one this bar carries, so it is now p < 0.05, the weakest mark, with a note explaining why.
  - The criterion now names the tests from the Figure 6F legend and the Methods.
  - It also says the paper gives no test for comparing central against peripheral retina, so that comparison is marked open.
  - `expected` is now a list, like the other claims.
- **fig6f-neighbours:** `expected` is now a list.
- **fig9a-response-variety:** the statement covers mutant and control retinas ("similar variety"), but the criterion only tested the mutant group. It now requires both groups to have every response class.
- **fig9b-direction-selective:** the Results say the retina was probed with "moving bars and gratings", not gratings alone. Moving-bar recordings are now included, and the claim is blocked only when neither kind is in the data set.

No claim ids changed. No main finding lacks a claim, and none comes from outside the paper.

**What remains open:**
- **Supplement:** Supplementary Figures 1 to 3 are not in the text. Their legends may give the test used in fig8el (synapse density) and the surround measure for s3.
- **Figure 9 method details the paper does not give:**
  - cut-offs for the response classes (fig9a)
  - a direction selectivity index (fig9b)
  - the surround measure (s3)
  - the flash intensities and how a response is judged (fig9-rod-cone)
  - how the 95% bands are built (fig9c to fig9h)
  - how the model behind the threshold and gain was fitted (fig9g, fig9h)

  The readings named in those criteria were chosen by the first reader, because the paper fixes none. When the readings disagree, the claim is blocked as underspecified.
- **Mutant allele:** the Results name fcon3 and the Figure 9 legend names f-del. The paper does not say which is right.
- **fig5-postnatal-onset:** the criterion requires that the thinning "does not grow" after P14, from the paper's "changed little". The paper gives no test for this.
