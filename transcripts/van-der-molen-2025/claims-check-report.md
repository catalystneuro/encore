The claims file for DANDI:001603 is ready for an attempt (`ready: true`). Nothing was committed or pushed.

**Checker:** `50 claims, 50 quotes, 71 statistical values, 0 problems` (it was 48 claims before I added two).

I read the whole paper, including the Methods, all figure legends and the supplement. I also cloned the paper's code (Protosequences at e9a79c4) to check the details the file says come from the code. Those checks all agree with the file, including the 70% unit rule in fig2e, which I first thought was wrong.

**Changes, by claim:**
- **fig7d-lag-times:** the statement said human organoid lags are *longer* than in murine organoids and slices. The paper only says they *differ*, so the statement now says "differ" and the criterion accepts either direction for those two contrasts.
- **fig7b-normalized-b2b:** the quote now includes the Results sentence behind the "organoids and slices above primary cultures" half of the statement. Supplementary Fig. 9B describes the normalization differently from the Methods (subtracting the shuffle mean); that is now a variant.
- **fig7c-normalized-pairwise:** the same subtraction variant, from Supplementary Fig. 12B.
- **fig7e-pca-backbone-variance:** the legend's "Differences were significant" does not say which groups are compared. The criterion now has two readings: backbone against non-rigid units, and backbone against all units.
- **supp8-backbone-stable-4h:** added the legend's second finding (most non-rigid units are still non-rigid 4 h later) to the statement, quote and criterion.
- **New claim fig4c-similarity-variance:** a finding stated in the Results that had no claim. The paper does not say which frames count as inside a burst, so the criterion names two readings.
- **New claim supp24d-backbone-non-poisson:** a finding stated in the Results that had no claim. The method comes from the Supplementary Methods and the code.

**Still open (recorded under `checks`):**
- **ed4b-nbqx-cpp-abolish-bursts:** "bursting disappears" is read as at most one burst per recording; zero would be the stricter reading.
- **fig5d-backbone-more-states:** the paper reports no test and does not define the "pool" of states. The 0.5 bound and the random effect for the number of states are the claims writer's choices, not the paper's.
- **fig7a-backbone-higher-rate:** the legend gives 1048 units for both human organoids and primary cultures, possibly a typo that the paper cannot settle.
