I checked `claims/kim-2025.yaml` against the paper text and against the paper's code at the commit the file cites (ac3300b). The file is ready for an attempt. I edited only that file and did not commit or push.

**Checker:** `claims/kim-2025.yaml: 28 claims, 27 quotes, 10 statistical values, 0 problems`. It passed both before and after my edits.

**Changes, by claim** (each is also recorded under `checks`):
- **Header M3 (overlap percentage):** the Methods take the 5th-percentile threshold over pairs of distinct trials. The code also counts each trial's zero distance to itself and uses <=. I made the Methods version the main reading and the code's a variant, because it can change which overlaps are above zero (and so the Figure 2C network).
- **fig2a-overlap-rises-with-slope:** the criterion said the code sets the diagonal to 0 for this figure. It doesn't: it does that only for Figure 2C, and for 2A it averages the full matrix including each stimulus's overlap with itself. The criterion now averages over pairs of distinct stimuli, as the Methods say, with the code's average as a variant.
- **fig4a-overlap-consistency-within-mice, fig4d-overlap-consistency-across-mice:** the Methods don't say whether that self-overlap diagonal enters the Spearman correlation. The code includes it, so the criteria follow the code, with the off-diagonal correlation as a variant.
- **fig1b-across-stimulus-slope:** with a loose tolerance on the mean and a two-sided test, nothing required the direction the statement gives. Added that the across-stimulus slopes must be larger than the across-neuron slopes.
- **figs1-gain-variance:** the statement says "more spread" but no spread was checked. Added the paper's SDs (0.92 and 0.15) as expected values.
- **figs2-behavioral-state:** the pupil tertiles are taken over all sessions pooled in the code; the Methods don't say. The criterion now follows the code, with per-session tertiles as a variant.
- **figs6-higher-areas-consistency:** removed a Wilcoxon test against the peak slope that the paper never runs. Replaced it with two readings of "near maximal".
- **figs4ab-noise-correlation-under-manipulation:** "most stimuli" is not from the paper. It is now marked as an open reading (more than half).
- **illusion-fig1c-isomap-geometry:** the finding is about the 2D Isomap picture, but the criterion judged it only in the full neuron space. Added the same tests on the 2D Isomap coordinates as a second reading.

The other code details the file cites matched the code: the slope-manipulation formula, no multiple-comparison correction, the one-sided test, the example session and stimuli, and the 1.11 movie median.

**Open:**
- Figures S5B and S5D (the movie trajectory and the natural-scene UMAP) have no claim. They are qualitative example pictures on the Allen data, not on DANDI:000248, so I didn't add them.
- The code divides orthogonal variance by the mean per-neuron variance where the Methods say the sum. The difference is a constant factor within a session and doesn't change the Spearman correlations or the Figure 3A comparison, so I left the criteria as they are.
- No PDF was supplied, and the Figure 2 and 3 legends are cut off in the text. The p < 0.05 threshold for Figures 2A to 2D and 3D to 3F therefore comes only from the code, and no figure panel could be read.

**Ready:** yes (`ready: true`).

`git status` also lists untracked dotfiles and folders (`.bashrc`, `.idea`, `scripts` and others). They weren't there in the clean status at the start of the session, and I didn't create or touch them.
