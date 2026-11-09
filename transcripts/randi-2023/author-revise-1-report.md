I've worked through every point in the verifier's round-1 report and changed three outcomes. The entry re-ran cleanly with `python tools/entry.py all` (0 check errors, notebook passes in 721 s), and every number in the conclusions comes from that run. Nothing is committed.

**Outcome changes**
- **osf-link: reproduced → partially reproduced.** The verifier was right: the 87.4% overall agreement is inflated because all 2,812 manually located targets agree by construction. For the targets found from the target position, which is what the claim states, agreement is 66.0%, inside the partial band.
- **fig4-rid-wt: blocked → partially reproduced.** The check the verifier asked for showed the old blocking note was wrong. The dandiset labels 11 ROIs as RID, and 8 stimulations in 5 animals target one of them. Only AWB meets the criterion (mean 0.076 over 12 trials, 3 detected responses). URX is observed once and ADL never.
- **fig4-rid-unc31: blocked → reproduced, on thin evidence.** The unc-31 export on OSF does label RID: 28 stimulations in 8 of its 18 recordings. Every neuron observed in both strains has a lower mean in unc-31, so the criterion holds. But the differences are small (Mann-Whitney p = 0.31 to 0.54), the WT URX value rests on one trial, and AWB responses are still detected in 17 of 50 unc-31 trials.
- I wrote the criteria for both RID claims into the claims file before computing any RID response. Its header says which RID counts I had seen at that point.

**Added or corrected**
- **fig2d (still not reproduced):** the verifier suspected baselines (F0) at or below zero and failed photobleaching fits. They are not the cause: 3,173 rows have F0 ≤ 0 and 2,037 rows use uncorrected traces, and removing them leaves the inhibitory fraction at 15.1%. I also ran it with the export's 950 excluded stimulations removed, without the nine poorly linked recordings, without the nine recordings with negative traces, and on the export's own assignment. Every variant gives 13.4% to 15.8%, all outside 11% ± 1.1%.
- **sourcedata-link (still partial):** under the same variants the correlation of mean responses stays between 0.534 and 0.601.
- **Shortened photobleaching fit:** re-running 12 recordings with the full fit gives a median correlation of 0.997 and 99.5% of classifier calls agreeing, so I kept the shortened fit.
- **osf-link outputs:**
  - Agreement per recording against the fitted z slope: only 3 recordings have a slope of exactly 0, not about half as the verifier read.
  - The nine low-agreement recordings, listed with their slopes.
  - The six label mismatches side by side. They have three causes, not one ROI-order problem:
    - The export has no labels for subject 11.
    - The dandiset has almost no labels for subjects 64, 76 and 77.
    - In subjects 86 and 91, shared names sit on different ROIs.
- **Other changes:**
  - New outputs: the two head neurons never labelled (AIAR, I5).
  - Text fixes: the text errors the verifier listed (depth range, imaging depth, the (0, 0) targets, the docstring).
  - Findings, README and entry.yaml updated to match.
  - The round is recorded under `verifications`, one result per claim.

**Not done, with the disagreement recorded**
- **edfig6:** I kept `not_runnable`. The protocol lists it as a valid reason, and the notes say the paper's package failed to install. I did not reimplement the kernel fits without the package.
- **fig6:** I kept `not_runnable` and made it depend on edfig6 in the claims file. The verifier's `data_missing` isn't allowed for a claim whose data are on OSF.
- **fig3:** I kept `data_missing`, because the model predictions it needs are not public.

I saved the paper text under `paper/`, which git ignores.
