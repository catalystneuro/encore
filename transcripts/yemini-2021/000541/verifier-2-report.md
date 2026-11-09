**Verifier report, round 2: Yemini et al. 2021 (NeuroPAL) on DANDI:000541 0.241009.1457**

The claims file has 29 claims: 27 from the paper and 2 links. The attempt record has 29 outcomes, one per claim. 18 are tested and 11 are blocked.

## 1. Outcomes

| Claim | Outcome in record | Agree? | Comment |
|---|---|---|---|
| link-zenodo-traces | partially_reproduced | Yes | 81.7% of traces reach r ≥ 0.9, or 85.8% with the constant one-frame lag. Both are below 90% (cell 18). |
| link-connectome-names | reproduced | Yes | 190 of 193 names match. The 3 that don't are not neurons (cell 69). |
| fig6-sample-sizes | partially_reproduced | Yes, with a gap | The head median of 19 is in tolerance only under the "one" and "both" readings. Under "deposit" and "none" it is 21 (cell 21). So the outcome rests on the trace-selection reading, but the record does not mark it `assumed: true`. |
| fig6-all-heads-responsive | not_reproduced | Yes | Best result is 19 of 21 (cell 24). |
| fig6d-ase-nacl | reproduced | Yes | Holds under every selection reading, on dF/F0, and under min-max scaling (cell 32). |
| fig6-nacl-unknown-interneurons | reproduced, assumed | Yes, conditionally | See below. |
| fig6c-odors-more-inhibitory | reproduced | Yes | Reading (b) holds, 0.234 < 0.245 < 0.362. The NaCl to 2-butanone margin is about one class of 94 (cell 38). |
| fig6d-awc-asymmetric | blocked (metadata_insufficient) | Yes | The CyOFP1 side is inferred from the image, not labelled, so the criterion still blocks the claim. No variant reaches p < 0.05 (smallest 0.056, cell 41). |
| fig6-asj-ric | partially_reproduced, assumed | Yes | See below. |
| fig6-interneurons-downstream | reproduced | Yes | 5 of 5 classes under every reading (cell 47). |
| fig6-tail-responses | blocked (data_missing) | Yes | No tail recordings in the dandiset. |
| fig6f-pharyngeal | reproduced | Yes | Holds under every reading (cell 52). |
| fig6-stimulus-sets-distinct | reproduced | Yes | A weak test, as the record says. |
| figs1h-avf-cyclic | not_reproduced | Yes | Medians of 0.121 to 0.205 Hz, against 0.27 to 0.33 Hz. |
| fig6gi-stimulus-specific-correlations | partially_reproduced, assumed | Yes | See below. |
| figs2a-pca-trajectories | not_reproduced | Yes | No reading or normalisation separates all three pairs (cell 66). |
| fig6jk-connectome-correlation | partially_reproduced | Yes | Head values only, all R² < 5%, none in tolerance (cell 72). |
| fig6-connectome-variations | reproduced | Yes | 1.51% on the first-listed reading (cell 75). |
| 8 data_missing claims (fig1 ×2, figs1, fig2, fig4c, fig5 ×2, fig7bc) | blocked | Yes | |
| fig7de-optimal-coloring | blocked (not_runnable) | Yes | |
| fig4bd-gaba-network, fig4e-extrasynaptic | blocked (`other`) | Agree they are blocked | The notes give a real block: the paper does not name the transmitter map or the connectome for this figure. They also say "the inputs are public, so a later attempt can", which makes it sound like a choice. The block should be stated as the unnamed inputs. |

**The three assumed outcomes:**
- **fig6-nacl-unknown-interneurons.** The claims file's criterion measures "the mean dF/F0", which gives 4 of 6, a partial reproduction (cell 35).
  - The claims file misreads the paper here. The STAR Methods say "When comparing neuronal activity across animals, we used dNMF to normalize activity traces per neuron class", and the claims file's summary of the processing leaves this sentence out.
  - The assumption is stated, and Table S6 supports per-trace scaling: rank correlation of log p is 0.90 to 0.96, against 0.62 to 0.73 on dF/F0 (cell 29). Min-max scaling also gives 6 of 6.
  - I accept "reproduced (assumed)". The record is right to say that the criterion as written gives 4 of 6.
- **fig6-asj-ric.** The result is 5 of 6 parts under reading (a) and 4 of 6 under (b) and (c), so partial under every FDR reading of the main selection. "deposit" and "none" give 6 of 6; dF/F0 gives 3 of 6. The assumption is stated and reasonable.
  - Under (a), the ASJ inhibition by 2,3-pentanedione part passes only because q = 0.040 while p = 0.082. That happens because Storey's pi0 is 0.222 here.
- **fig6gi-stimulus-specific-correlations.** The assumption is stated, and the outcome would be reproduced under "both".
  - The null window starts 30 s after onset, so it sits 20 to 50 s after each pulse ends. The paper reports post-stimulus responses in that period. So the window does not separate recording time from lingering stimulus effects.
  - The conclusion's "may drive part of the effect" is suitably hedged. The outcome is unaffected.

## 2. Text against the printed outputs

Almost every number checks against the outputs. These sentences do not:
- **Cell 79 (Summary):** "Three claims change with this choice (fig6-nacl-unknown-interneurons, fig6-asj-ric and, through the selection reading, fig6gi-stimulus-specific-correlations)". This sits under the normalisation bullet. fig6gi uses Pearson correlations, which normalisation does not change (cell 64 says so). fig6-sample-sizes, which does depend on the selection reading, is left out.
- **Cell 79 (Summary)**, "101 named traces are not in the paper's deposit", and the same sentence in the record's `selection_undocumented` finding. Cells 11 and 18 show 101 is only the count of empty slots. 113 finite named traces are missing from the deposit (126 counting the all-NaN ones). The record's `methods_unavailable` finding uses 126.
- **Cell 65:** "Classes present in all 21 heads (class-averaged dF/F0 per head)". The main run in cell 66 uses z-scored traces.
- **README:** "Both choices are the ones closest to the paper's own Table S6". For the selection reading this is true only of the per-class trace counts. Agreement on p is about the same for all four readings (260, 261, 259 and 257 class agreements at 0.05, cell 29).
- **Cell 56:** "With sets of 20 to 50 classes out of 94". The printed set sizes run from 16 to 55.

The record states my round-1 reasons faithfully and in my wording, with only minor trimming of numbers and cell references. The figs2a entry merges my problem 3 into the reason, which is fair. For the three with_inputs claims, the entry keeps my "blocked" but not my blocked_by (data_missing). That is acceptable, since the author changed the reason.

## 3. Round-1 points

**Resolved:**
1. Near-duplicate readings. The deposit reading and the cross-tab are now run, the main reading is now "one", and the spacing has been corrected. The procedure is resolved; the remaining issue is listed below.
2. The cell 12 misreport is corrected (now cell 16), and an ASE time-shift check is added.
3. The PCA now runs on z-scored traces, with variants.
4. Storey q has been checked against the paper's own q values: agreement at 0.05 in 273 of 285 tests.
5. AMSO and HMC are left out of the tests.
6. The frame alignment is shown. The lag is a constant +1 in all files; I was wrong in round 1 to say it varied by file.
7. The ON/OFF search now covers all 21 files, and the image colours have been checked.

My round-1 "not checked" items are all addressed: distances, the cross-tab, the deposit medians, the ASJ and RIC rows for every reading, and the reasons for the blocked claims.

**Remaining, bearing on a conclusion:**
- **Selection reading.** "one" matches Table S6 only in aggregate counts. Only 20 of its 338 removed traces are among the 126 the deposit lacks (cell 11). Three outcomes switch with this reading:
  - fig6-asj-ric (partial or reproduced);
  - fig6gi (partial or reproduced);
  - the fig6-sample-sizes median (19 or 21).

  fig6-sample-sizes should be marked `assumed: true`.
- **Normalisation.** The fig6-nacl-unknown-interneurons outcome rests on a per-trace scaling that the claims file's criterion ("mean dF/F0") does not name. The claims file omits the paper's normalisation sentence; this is reported, not corrected.
- **Low pi0.** Storey's pi0 here is 0.222, against 0.42 to 0.48 on the paper's p values, so reading (a) is more lenient than the paper's. It decides one part of fig6-asj-ric under (a), but not the outcome.
- **Round-1 point 8.** Whether the median of 18 covers heads and tails together is still open; the author has passed it to a reader as a question. The deposit's own head median is 21, which makes a heads-only reading of 18 less likely.
