I've worked through every point in the round-1 report and re-run the entry. The final run passed in 50.2 minutes, its numbers match the rewritten conclusions, and `tools/entry.py check` reports 0 errors. Nothing is committed.

**Outcome changes**
- **fig10c-strf-mi-higher** goes from not reproduced to reproduced, and is marked as resting on an assumption (the linear projection). The verifier disagreed with the old outcome. Only that one reading reaches p < 0.001 (6.4e-4 in this run), and in only 3 of 5 subsampling draws, so the notes call the result fragile. The new held-out check (STRF from one half of the stimulus, MI on the other) favours the cNE under all four readings, p = 2.2e-15 to 6.7e-8.
- **fig6c-spike-pwc-narrower-than-strf-pwc** stays reproduced, resting on an assumption. The verifier would give partially reproduced, and the disagreement is recorded. I added two ways of making the STRF PWC non-negative: the absolute value, and dividing by the overlap, which removes the taper the verifier noted. Every reading except setting negative values to zero passes both parts of the criterion, with or without a baseline. Setting them to zero gives 4 ms STRF PWCs, which contradicts the paper's description of them as broad.
- All other outcomes are unchanged, and the verifier agreed with each of them.

**Added or corrected**
- **PWC sharpness:** PWCs now use only spikes inside the stimulus period. I added variants with a baseline subtracted, ±10 and ±20 ms windows, and the width of a flat histogram (25 ms over ±50 ms).
  - None of these brings fig2bd or fig6-member into tolerance. The cNE-pair median stays at 6 to 16 ms.
  - Only a ±10 ms window gets to 3 ms, and there the window itself sets the value.
  - The conclusions now say this.
- **fig6j:** added the verifier's reading where non-cNE pairs must both be cNE members. It gives the same 14 and 12 of 16. The question is in `questions/see-2018.yaml` and the claim is unchanged.
- **fig5a:** added the number of distinct bins the 5000 events fall in (median 230 at 50 ms) and the held-out MI. The MI still does not peak at 10 to 15 ms.
- **fig10s1:** now uses the paper's 500 random groups, plus two more seeds. It stays reproduced; the PTD test is near the bound (p = 0.0023 on one other seed), which the notes say.
- **Further checks:**
  - fastICA iteration counts: all runs converged.
  - DG fit: the clipping changes latent correlations by up to 0.56, but sampled covariances correlate 0.974 to 0.999 with the real ones.
  - PR model: drops 18 to 61 spikes per recording.
- **Record and docs:** notes, measured values, deviations and findings are updated, and round 1 is recorded under `verifications`. The README and summary are updated. The runtime is now 50 minutes, up from 35.

**Not done**
- I did not change the fig5a event readings. The verifier called neither defensible, but reading (a) is the literal reading of the Methods, and the held-out check gives the same outcome.
- I did not change the fig4s3, fig7e or fig11ef points. What the verifier asked for there was already shown or stated.
- `tools/entry.py` and `tools/notify.py` had changes before I started that are not mine; I left them as they were.
