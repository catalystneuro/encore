I worked through every point in the round-1 report. The entry ran clean with `tools/entry.py all`: all four notebooks pass, the longest taking 50 minutes. The conclusions match the executed outputs, and `entry.py check` reports no errors.

**What changed in the outcomes**
- **fig2-neuron-beta-stable:** now `not_reproduced` (was `partially_reproduced`), as the verifier gave. The criterion has no partial outcome and neither of its readings holds.
- **fig2-neuron-merging-collapse:** now `not_reproduced` (was `reproduced`), resting on an assumption (`assumed: true`). Without the cap no fit stays within the 0.5 band: the closest misses at 0.538, against 0.490 with the cap.
- **fig2-other-neurons-similar:** now `reproduced` (was `not_reproduced`), as the verifier gave. The criterion counts a pass under any one fit reading, and my round-1 choice of the discrete KS fit overrode that. Only the continuous fit from xmin = 1 passes (0.883 to 0.906), so the notes call it fragile.
- **fig2-neuron-merging-heavy-tail:** kept `reproduced`, with the verifier's disagreement recorded. Without the cap, the discrete KS fit still keeps the γ IQR below 0.5 (0.378 and 0.415).
- **The two blocked claims:** kept as they were, with the disagreements recorded.
  - Wikipedia stays `too_large`: the claim is "data elsewhere", for which the protocol does not use `data_missing`.
  - Earthquakes stay `other`: the catalog has no versioned release, and the protocol only allows pinned outside data.
- **The other seven:** unchanged. fig2-neuron-burst-size-heavy-tail no longer needs an assumption, because every KS reading gives it.

**What I added or corrected**
- **The cap on the exponent (problem 1):** the verifier was right. The locked powerlaw 2.0.0 caps the exponent at 3 by default, and the cap also moves the choice of xmin. The fits now leave the exponent unbounded, as in the method the paper cites (Clauset et al.). The capped fits run beside them as a variant, and the notebooks print the powerlaw version and how many fits hit the cap.
- **Other neurons (problem 2):** all 690 units are now fitted. Inhibitory units and all units are shown beside the claim's pyramidal sets. A new notebook, `other_neurons_cap3.ipynb`, holds the capped variant on grid (a) only, to keep each notebook under 60 minutes.
- **Decremental model (problem 4):** a test calibrated across runs is added as a variant. It finds no difference between two runs of one algorithm, and a difference in all three series under the literal set-up. It does not decide the outcome.
- **Fig. 4 heavy tails:** the model notebook now prints the result for each series and fit reading under every seed.
- **Questions and findings:** added `questions/hiraoka-2025.yaml`. It asks a reader whether "pyramidal" misreads the paper, since the paper's own representative unit is labelled inhibitory. Under the KS fits the inhibitory units show the pattern in 0.68 to 0.74 of units, against 0.08 to 0.45 for pyramidal ones. I added a finding at the end that asks the paper's authors which powerlaw release they used and whether the exponent was bounded.
- **Record:** round 1 is recorded under `verifications`, with the verifier's reasons for all 14 claims and my responses. All notes and conclusions are rewritten to the new numbers.

**What I did not do**
- I did not count the earthquake south cluster from the current SCEDC catalog. That would rest on unpinned outside data, which the protocol does not allow.
- The verifier's other unanswered item, which circles in Figures 2 and 4 are filled, needs the paper's PDF, which was not supplied.
- I made no commits, as instructed.
