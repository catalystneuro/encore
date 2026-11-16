I've worked through every point in the round-1 report and re-run the entry. The checks pass, and the notebook runs in 16 min, up from 7, because the second-dataset analyses now run on both windows. Nothing is committed.

**Outcome changes.** Seven outcomes now match the verifier's:
- **fig1ijk and modulation-absolute-not-rate-dependent:** not reproduced. No reading meets either criterion.
- **fig1m, fig1no, us-pause-declines-with-training, fig6h:** partially reproduced. The criterion's tests hold, but some expected values are out of tolerance.
- **fig7b:** partially reproduced. The correlation holds; the slope and the count don't.

The tally over the paper's 55 claims is now 21 reproduced, 21 partially reproduced, 6 not reproduced and 7 blocked. The link claim is reproduced.

**One disagreement kept.** I left fig2n at partially reproduced, where the verifier gives not reproduced. The negative trial correlations and the negative slope appear in every combination, only weaker than the paper's. The disagreement is recorded in the `verifications` block.

**What I added or corrected:**
- **Lag estimator (B1):** I adopted the standard cross-covariance of the two traces (as MATLAB's `xcov`) and marked it as an assumption. The round-1 estimator is kept as a variant, and the notebook prints how many cells sit at the ±100 ms edge or are flat at their best lag. With the new estimator no cell sits at the edge, and all four lag outcomes stay the same. fig2h's mean lag is now 28 ms (expected 33.4 ± 3.3).
- **CS-transient readings (B2):** a new table holds each reading fixed across the eight CS tests. No single reading meets all of them; the best, drop/mean at 50–125 ms, meets five. cs-pause-cells-have-us-pause is marked as resting on my 50 ms rebound span.
- **Reading (a+) (B3):** it is now labelled my own variant. fig2a and fig5cd report claims-file readings; fig5cd under class (b) has rates of 44.4 and 15.4 Hz, both within tolerance.
- **Second-dataset window (B4, B5):**
  - fig2n now runs fully on 0–212 ms as a variant: 16 cells, but 5 significant cells and a slope of −0.60, so the outcome doesn't change.
  - I added a question to `questions/brinke-2017.yaml` asking whether 0–212 ms should be a reading. I did not change the claim.
  - 0–200 ms now runs in every second-dataset claim.
- **Mixed models (B7):** each table row now shows the fit's warnings and an ok flag. Most fig2n fits are singular.
- **Smaller points (B6, B8, B10, B11):** I corrected the docstrings, noted the velocity scale, explained why the trial exclusions aren't applied again, added sections for fig7s1c and fig7fg, and removed the no-op loop.
- **Comparison with Source data 1 (section C):**
  - The authors' CR flags give 103 recordings with behavior; my rule gives 111, with 102 in both.
  - Their per-cell facilitation equals reading (b) (r = 0.998) but gives 84 cells at 5 Hz, not the paper's 60. I recorded this as a new finding.
  - An undocumented US-Cluster code gives the paper's Fig. 6B counts exactly.
  - The 26 recordings whose stored mean trace differs from the trial mean are now listed.

**Not done:** the fig2f bootstrap runs only on the adopted 12–212 ms window, to keep the run short; the 0–200 ms counts are shown without it. The edit to the attempt record reflowed the line breaks of the whole YAML file, but its content is otherwise unchanged.
