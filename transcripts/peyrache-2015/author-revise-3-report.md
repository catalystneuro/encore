I applied both changes the verifier agreed with. No proposals are left open.

**Outcomes changed**
- **fig4d-ole-near-bayesian**: was `not_reproduced`, now `partially_reproduced`. With the hd-b ensembles the covariance decoder beats the signal-only decoder in both structures (p = 0.019 in ADn, p = 0.042 in PoS). But in PoS its error is 1.76 times the Bayesian decoder's, outside the allowed 25%, so only the first part of the claim holds. Under hd-a it is still not reproduced. The notebook's conclusion now also says the ADn gain is only about 1% of the error, far from the paper's "approximately 50%".
- **fig5e-readout-windows**: was `blocked` (`too_large`), now `partially_reproduced`. The SWS median window is the shortest in every variant, but none of the three medians is within tolerance: 168, 178 and 63 ms against the paper's 123, 133 and 79 ms. `blocked_by` is removed, and `measured` now holds those three medians.

**Other updates**
- I removed `proposed` from both outcomes.
- I updated the conclusion and summary cells in `reproduce_peyrache_2015.ipynb` and `glm_windows_peyrache_2015.ipynb`, the entry README and the two outcomes' notes to match.
- Round 3 is recorded under `verifications` with one result per reviewed claim: agreed, the outcome it gave, its reason in its own words, and my response.
- **Run time**: the verifier pointed out that "24.8 minutes" was wrong. The outcome notes no longer give a time and point to the time the notebook prints, which was 19.3 min in this run. I left the round-2 response as it was recorded and noted the error in the round-3 response.
- **New question**: the verifier flagged a possible misreading in the fig4d criterion, which counts any small but significant gain as enough. I added it to `questions/peyrache-2015.yaml` as a question for a reader.

`python tools/entry.py all entries/peyrache-2015` gave 0 check errors, and all three notebooks passed (911 s, 674 s and 1160 s). The printed numbers match the record. Nothing is committed.
