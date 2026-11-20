I made all the round-2 fixes and re-ran the entry with `python tools/entry.py all entries/silkuniene-2025`. It passed with 0 errors and took 40.7 min. The conclusions match the new numbers. Nothing is committed.

**Outcomes**
- No outcome changed, since round 2 doesn't allow it.
- **fig6d-longer-pulses-sharper-peak** stays reproduced (assumed). I recorded a proposed change to not_reproduced for round 3, because the verifier was right:
  - Leaving out B2 alone (n = 6 at 600 ns), the slope p is 0.51 to 0.77 on individual experiments and 0.63 to 0.83 on group means. With all seven wells it is 0.86 to 0.99.
  - B2 has a reason to be excluded that doesn't depend on the result: its spot is 5.39 mm from the array centre, against at most 1.21 mm in every other well.
  - B3 has no such reason. It peaks at the centre, so my earlier statement that it had "no central peak" was wrong. What sets it apart is high uptake 3 to 5 mm out (46% and 35% of the centre, against at most 13% and 9% in the other 001277 wells). That is the breadth the claim tests, and the 001276 CT26 wells at 6 bursts show the same shape.
- **fig7be-center-linear-with-bursts**: I removed `assumed: true`, since it is partial under both readings of how the regression points are taken.

**Added to the notebook**
- The fit with only B2 left out, for fig6b, fig6d-longer and fig6d-600-900. fig6b stays reproduced and fig6d-600-900 stays partial under it.
- A per-well table of peak measures that don't use the FWHM, for every 0.2-MHz CANCAN well.
- `cancan.py` now reads the packet count from each file's description, and the data check prints it by pulse duration. This puts computed output behind the "9 packets" finding.
- The total size of the files read (46.7 GB), and for fig7be the share of draws per cell line on group means (CT26 0%, CHO 12.4%).

**Text corrected** (all seven sentences the verifier flagged)
- fig7be: on group means CHO has p < 0.001 in some draws; only CT26 never does.
- fig6c: with all seven 600-ns wells, 600 against 900 ns also differ at ±0.81 mm under contiguous ROIs.
- fig6d-longer: the "no central peak" wording is removed from the notebook, the deviation and the finding.
- fig7cf: the argument from group means now covers panel B only.
- Summary: it now names the two FWHM claims actually shown with the geometry difference removed.
- fig5 October note: values are now given relative to the 0-mm mean of all wells.
- README: run time and data size now point to printed outputs. The README table no longer marks fig7be as assumed and notes the proposed change for fig6d-longer.

**Records**
- I added the round-2 verification to the attempt record: the verifier's reasons in its own words, a response for each claim, and a note on the points not tied to one claim.
- For fig7-offtarget I added that the evidence is weak, as the verifier said.
- I added a question to `questions/silkuniene-2025.yaml`: whether assumption O1 is wrong to call the background footprint "any one, a standard choice". For CT26 at 1 burst and 6 mm, the ratio runs from 23.6 to 57.0 depending on the footprint and ROI reading.

**Not done**
- The 001047 assignment question (B1) was already asked of a reader in round 1, so I added nothing for it.
- The README gives the run time as "about 39 minutes", but runs took 38.3 to 40.7 min, so the printed time varies a little.
