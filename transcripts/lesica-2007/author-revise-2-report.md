No outcome changed, but the re-run you asked for failed. `tools/entry.py all` stopped when the main-pass cell ran past its 3600 s limit, with the notebook at 3968 s. The code is the same as in the verified run, where that cell took 1990 s. This machine is about twice as slow (the penalty-choice cell took 231 s against 115 s). A second try with a 7200 s cell limit had not finished after 100 minutes and was stopped. So there is no new executed copy, and every number cited is from the verified run. `tools/entry.py check` passes.

**Proposed changes for a third round** (each verified outcome is kept; the change is written under `proposed`):
- **fig3b-spatial-width-correlations and fig3c-surround-correlations:** reproduced → not reproduced. At 1000 × variance the effects are 5.1% (p = 0.11) and 2.7% (p = 0.67). The penalty-selection rule barely separates the penalties (held-out r 0.420 against 0.437). The estimator-bias evidence is the verifier's own synthetic check; I could not run one here.
- **fig3d-temporal-width-contrast:** partially reproduced → not reproduced. The noise test fails (p = 0.011), and the criterion's "partial" requires the tests to hold.
- **surround-temporal-correlation:** partially reproduced → reproduced, marked assumed. I adopted the reading that takes both measures from the 128 Hz RFs, as the paper takes both from the same RF. That gives r = −0.466 and −0.480, inside the tolerance.

**Added or corrected:**
- **Newly marked `assumed: true`:**
  - fig5: the contrast readings, and the full-data penalty used on each third of the frames.
  - fig7d and fig8de: they pass under opposite stimulus readings (12 s clips against long segments).
  - methods-spherical-asymmetry: the movie estimate is regularized 2.8 to 3.8 times more heavily relative to its data. Each has a deviation saying why.
- **Round 2 in `verifications`:** all 38 claims, with the verifier's reasons in its words and my responses. It also notes that the round-1 reasons cite cell numbers that no longer match the notebook.
- **`questions/lesica-2007.yaml`:** asks a reader about the claims-file header, which says 50 Hz frames where the files show 60 Hz. It affects no criterion.
- **Notebook and README:** text-only changes. The conclusion cells and the summary now give the proposals, the assumptions and the variants not run. The README notes the failed run.

**Not done:** three variants the verifier asked for. I wrote and tested each on a subset, then took them out:
- **A second penalty for the 128 Hz RFs.** With it, the main pass alone ran past 3600 s. The 128 Hz results therefore still rest on one penalty, which affects fig3d, surround-temporal-correlation and methods-latency-biphasic.
- **A noise penalty scaled to its frame count, a 1000× penalty and a same-RF bias check in the spherical-asymmetry simulation.** There was no time for a run that would include them.
- **A penalty scaled to each third's frames in fig5.** Same reason.

The record says why for each.
