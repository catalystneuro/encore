No outcome changed in this round. Four outcomes now carry a proposed change to `not_reproduced` for a third verification round. I re-ran the entry with `python tools/entry.py all entries/000774-hickman-2026` (803 s, 0 errors); the numbers are the same as before and `entry.py check` passes.

**Proposed outcome changes (point N1):** fig4f-responders-within-ep, fig5i-fs-within-ep, figs3e-early-windows and fig6c-modulation-cortex stay `partially_reproduced`. None of their criteria has a partial clause, which is the rule I used to make fig5-fsrs-proportion `not_reproduced`. Under that rule all four would be `not_reproduced`, so each has a `proposed` entry with the numbers behind it. The notebook's Result cells, the Summary and the README say this too.

**Output the verifier asked for:**
- **fig4i (N2):** the paper's code makes the raw `distance` negative from the channel closest to the contact on (figure4_figure5_figure6 cell 7), and the notebook now cites that passage. A new check on the code's `direct_df.csv` shows `distance <= 0` exactly where `norm_distance <= 0`, in every row. I also ran the unsigned distance: it gives 0.0129, 0.0221, 0.0312 and 0.0293 (p = 0.033). The 25 µA value is just outside 0.020 ± 0.002, so the outcome rests on the code's sign, and the notes say so. The outcome stays `reproduced`.
- **Unit counts against `direct_df.csv`:** these are now printed side by side. All four cathodal and all four anodal conditions match. The four bipolar conditions differ by 1 to 5 units. `direct_df.csv` is listed under `inputs` as a check only, and the notes, deviation, finding and Summary were corrected to match.
- **fig6d:** the cell now prints the counts for the seven recordings with cathodal pulses. 273 of the 460 legend subcortical units are CA1. 91 of the 349 units in the code's HVA group are superior colliculus or dentate gyrus; the 151 the record gave is the count over all nine recordings. Notes and finding corrected.

**Text corrected:**
- The claim that "the code's coordinates match the paper exactly" is gone from the notes, Result cell, Summary, README and finding. Two values do not match: the 50 µA extent is 868 against 965 µm, and the 50–100 µA KS p is 0.8245 against 0.083.
- figs9: the values are about a quarter of the paper's at 5 µA and a sixth at 100 µA, not a quarter throughout.
- k-means: the 20 runs are the original run and 19 others, not 20 from other seeds. The stability table now marks which run is the original.
- fig5-fsrs: class p within the evoked potential is 0.983, 0.608 and 0.821 under the three readings, not 0.821 alone.
- fig6e: the Results print F region 40.14 and interaction 15.61 next to F amplitude 175.18 without naming the model; the record no longer calls them cathodal.

Round 2 is recorded under `verifications`: all 42 claims, with the verifier's reasons in its own words and my responses.

**Not done:**
- I did not fit the full three-polarity model for fig6e on recomputed ZETA p-values. It would add about 20 minutes of ZETA, and the outcome is partial either way.
- B5 is left as it was. The contact coordinates of jlh31 and jlh32 differ between the dataset and the paper's code, and only the authors can settle which are right.
- No new reader question was needed: the fig6f width-filter question the verifier raised is already in `questions/000774.yaml`.

Nothing is committed. The changes to `tools/` were already in the working tree before this run, and I did not touch them.
