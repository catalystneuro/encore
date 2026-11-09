I've worked through every point in the round-2 report. No outcome changed, and nothing needed a `proposed` change. The re-run (`python tools/entry.py all entries/000139-churchland-2010`) passes with 0 errors in 620 s. Its numbers match the previous run, and every conclusion now matches the printed numbers.

**Outcomes:** all 23 are as the verifier agreed in round 2.

**What I added or corrected**
- **j-array-recordings:** the outcome is now marked `assumed: true`, with a deviation saying it assumes the 27 conditions are among the paper's 108. I corrected the trial count: the 100 unlabelled test segments cover only the 114 held-in units, so the 38 held-out units have just the 250 trials. I removed the sentence about dandiset 000128, since nothing in the notebook prints it.
- **fig4e:**
  - The notebook now prints that the go-locked part of the splice is the preparatory window itself (go cue −200 to +100 ms, placed at −554 to −254 ms from movement onset). It also counts the passing selection readings for each combination of neurons and time range: 7, 3, 6 and 6 out of 8.
  - The conclusion, record notes, deviation, Summary and README now say the splice sets the decline time in the main selection. Without the splice, the outcome holds through the movement-locked trace: in 6 of 8 selection readings with all preparatory neurons, and 3 of 8 with the Figure 4D neurons. In those readings the decline falls at −283 to −300 ms, the early edge of the criterion's window.
- **Cell 37 and the fig6d notes:**
  - The threshold sentence no longer says "Only 59". It now says a median of 59 units pass on shuffled labels, so noise accounts for most of the 75 that pass.
  - The chance statement covers only the spaces where chance was computed. It names the ones where it was not: kinematic window b, replication b and the upper limits.
- **Cell 72 and the fig7c notes:** the upper limits without the fitted neuron are now given as −0.107 to 0.170, at or below zero in 2 of 8 (the old text said all were).
- **Summary:** the best performance is now given as 0.117 with S fixed and 0.226 with S recomputed, in place of "about 0.1 to 0.2".
- **README:**
  - Added the caveats the Summary table carries: for suppfig1, cross-validation; for the dimensionality peak, S fixed; for Figure 8, the full-cycle reading; and the fig4e and j-array caveats above.
  - The list of open readings now includes where the Figure 4E trace is spliced and the length of the Figure 8 gray interval.
- **`questions/000139.yaml`:** I added a question for a reader about the fig7c criterion. Its "within 10% of random halves" band (±0.046) is narrower than the spread of the random halves themselves (SD 0.153). The claim is unchanged.
- **Attempt record:** round 2 is recorded under `verifications`, with the verifier's reasons for all 23 claims and my response to each.

**Not done:** the two points the verifier listed as unresolved but not affecting any conclusion. Velocity in the kinematic space is still unsmoothed, and the SD tuning reading still leaves no neurons. Both are disclosed from round 1, and the verifier said neither changes a conclusion. Nothing is committed, as instructed.
