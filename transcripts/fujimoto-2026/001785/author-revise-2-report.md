## Report

**Outcomes:** none changed and nothing is proposed. The round-2 verifier agreed with all 35 outcomes (24 reproduced, 1 partially reproduced, 2 not reproduced, 8 blocked), and no new analysis pointed to a change. I re-ran the entry with `python tools/entry.py all`. It passed in 213 s with 0 check errors, and every number is the same as before.

**Corrections, one per item in the report:**
- **2.1, fig5c variant:** the "p printed as 0, below the floor" claim is gone. Cell 35 and the record now say the LIM still falls (−0.029, interaction F = 61.6) but its Tukey-Kramer p could not be computed: it prints as 0 for every network, with scipy's "integral is probably divergent" warning.
- **2.2, Summary:** now reads "under no single reading in all four", and names the size filter each region needs: 10 pixels for the MCC-CB and dACC-CB of N and T, 50 for the MCC-CB of D.
- **2.3, README:** now says the three regions where the counts match need different size filters, and that no single setting matches in all four.
- **2.4, ed6a notes:** now name the setting. The counts run 8 to 14% higher than the paper's at 10 pixels and 9 to 21% lower at 50 (r = 0.94 and 0.98), and the link holds in this region only at 10 pixels.
- **2.5, repeated FA voxels:** the verifier said voxels shared between different tracts or sides had never been examined, so I added that check to cell 9.
  - In the N and T whole-tract list, 233 voxels appear in two or more tracts of one session, mostly UF with FM or CB with UF on the same side. Two of them span both sides.
  - Each carries the same value in every tract, and no voxel is matched by two different values.
  - 23 of them have more than one candidate voxel, so they may be two voxels with equal values. The rest are single voxels where the paper's tract lists overlap.
  - The other three lists have 71, 1 and 18 such voxels.
  - Cell 59, the link-fa-voxels notes and the finding now describe both kinds of repeat (within one tract, and across tracts).
- **2.6, cell 50:** removed "this fits a local increase at the implantation site". The cell now only reports the ten largest increases and the mean change.

**Recorded:** a round-2 entry under `verifications`, with all 35 claims marked as agreed. Each reason paraphrases the report and each response says what changed.

**Not done:**
- **B3, the cell-counting method:** unchanged. The paper does not give its FIJI parameters, so there is no better-founded method to switch to; the question stays with the paper's authors in the `methods_unavailable` finding. The verifier's view that ed6a (not reproduced) may reflect the counting method and that ed6b's support is weak is recorded under those claims. Both outcomes are kept as verified.
- **Questions file:** nothing added to `questions/001785.yaml`, since the verifier reported no place where the claims file misreads the paper.
- **Not mine:** I did not touch the existing changes to `tools/build_site.py` and `tools/site_assets/app.css`, or the untracked `scripts/` folder.

Nothing is committed, as instructed.
