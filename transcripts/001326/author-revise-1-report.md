The revision is finished. The entry check passes with 0 errors, all three notebooks run (main 522 s, behavior 336 s, the new iEEG one 35 s), and the handover is rebuilt. Nothing is committed.

**Outcome changes (round 1)**

| Claim | Before | Now | Why |
|---|---|---|---|
| fig4de | partially | not reproduced | The 3 persistent clusters and the cluster sizes fail under all ten Leiden seeds |
| figs31b | reproduced | partially | VPM falls in a faster-half cluster in only 3 of 10 seeds |
| fig5e-late | not reproduced | partially | Ketamine is lower in every reading, but significant only under the code's windows and variance |
| figs32c | reproduced | partially | Under the criterion's interval wording, 4 to 6 of 7 areas pass, not all |
| figs29 | partially | reproduced | sub-7 has no value and no longer counts in the denominator (7 of 9 and 5 of 9) |
| fig4b, fig5b | reproduced, resting on an assumption | partially | The reduction holds only under the code's per-condition normalization |
| fig2g, fig2i, fig3b | blocked | reproduced | Tested in a new notebook, `reproduce_kauvar_2025_ieeg.ipynb` |

The new iEEG results:
- **fig2g:** 0.466 of the held-out variance is explained at six factors, within 0.47 ± 0.047. This rests on an assumption: I put the elbow where the gain from adding factors drops most, which gives six; another standard rule gives eight, and the paper picked it by eye.
- **fig2i:** my factorization gives back the deposited loadings exactly, and factors 1 and 2 both fall under ketamine (corrected p 2.6e-05 and 5.5e-08).
- **fig3b:** the limbic, ventral attention and somatomotor networks are significant (corrected p 0.0039), the other three networks are not, and the deposited cluster masks mark the same three.

Totals are now 31 reproduced, 11 partially, 3 not reproduced and 9 blocked.

**Kept, with the verifier's disagreement recorded**
- **fig5e-rapid:** a claim of absence is judged on the paper's own test, with the Methods window.
- **figs33:** I now score the Ketamine series only, as the criterion asks. The persistence-timescale model is best in 23 of 24 readings. I marked it as resting on the Methods reading where readings disagree.
- **fig6d and fig6h:** these rest on the assumption that sub-5 is the animal the paper excluded.
- **figs30:** the within-region rise is present and the between-region fall is absent, under either start of the ketamine window.

**Added or corrected**
- **Clustering:** the verifier's numbers for the clustering claims came from a different Leiden partition. I added a ten-seed stability table, and fig4g fails under every seed.
- **fig4i and fig4h:**
  - Clusters without a value make up 0.24 of a region's weight under ketamine against 0.06 before it.
  - I added variants that renormalize the weights, use a Pre set of the same size, or both.
  - Rise times are unchanged in all of them. Decay still shortens, but by -0.06 to -0.12 s instead of -0.17 s.
- **fig6h and figs34g:** I count the degenerate fits and added fits that are bounded, with the mean removed first, or summarized by the median.
- **Contaminated windows:** tone or light onsets fall in the 30 s before 14 of the 30 puff series used. Two sessions also have lights inside their post-series windows. fig6j, fig6h and fig5d now also show results without the affected windows.
- **Ketamine epochs:** series 23 starts at least 235 s after the file's infusion time in every session, so the verifier's concern about early Ketamine series is resolved.
- **Other new checks:**
  - figs30 is also run from the file's infusion time.
  - fig6d is also run with weights from half the Pre series and scored on the other half; this does not inflate Pre.
  - The hard-coded "only eye_closure" message is replaced by a computed search of 66 files. No lick, report or CADSS data are in any of them.
- **Question for a reader:** whether figs30's window should start at the infusion. It is in `questions/001326.yaml`.
- **Findings:** three new ones, and the README, both summaries and the round-1 `verifications` block are updated.
- **Dependencies:** `mne` and `scikit-learn` are added to the requirements and the lock file.

**Not done**
- fig6c, fig6e, fig6g, fig6i and figs12 stay blocked as `too_large`, for time. They need the paper's full pipeline on about 16 GB of raw LFP (band power, coding dimensions, phase locking, blink-locked ERPs). I judged that too risky to build in this run, and the notes now say the data are there.
- The per-region cluster test for fig3b is not run. The criterion is decided by the networks.

`tools/build_site.py` was already modified before this run and I left it alone.
