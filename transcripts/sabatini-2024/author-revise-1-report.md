I've worked through the round-1 report. One outcome changed, the questions file now exists, and `python tools/entry.py all entries/sabatini-2024` passes: 0 check errors, notebook 1 ran in 27 min and notebook 2 in 13.5 min. I ran it a second time after the last text edits and every printed number came out the same, and the conclusions match them.

**Outcome changed**
- **fig7f-decoder-beats-standard: blocked → partially_reproduced.** The Methods say the single-trial kernel decoders were "trained on a subset of single-trial data", so they fit in memory after all. All decoders except GPFA now run, on the same folds as the LDR decoder. LDR wins all 56 comparisons with p < 0.001. Its trial averages are 88.9% to 93.3%; the best standard decoder reaches 75.1% to 89.4% depending on the dataset. Under the criterion, beating everything except GPFA counts as partial. The outcome is marked `assumed`, because two details are mine: the subset size (I ran 4,000 and 12,000 samples) and how velocity predictions are turned into positions. The code for both is not in the repository.

**Reviewed again, outcome kept**
- **fig3i:** I now run both the per-trial duration the criterion names and the code's per-condition duration. Both are not reproduced: the M1-N unwarped correlation is −0.008 or 0.013, against the paper's −0.26. The warp window was right: `warpTrial.m` adds a 100 ms lag, as the notebook did. Only the notebook's wording was wrong, and I corrected it. The window the verifier proposed (to the end of the reach) is shown as a variant.
- **Offline movement onset:** the claims that depend most on the alignment event are recomputed on the file's offline onset in a new variant section. None changes outcome.
- **fig4d / fig4f:** the main reading now re-extracts the basis from normalised, mean-subtracted data, as the Methods say; the code's version is a variant. fig4d stays not reproduced (5 of 6 planes significant) and fig4f stays partial (4 of 6 under the Methods reading, 5 of 6 under the code's).
- **suppfig3:** stays not reproduced on the claims file's reading. When both models are scored on held-out data over the same window, as the verifier asked, the TBF beats the single-condition LDS in all four datasets. I added this to `questions/sabatini-2024.yaml` as a question for a reader.
- **Kernel length scales (fig6e, fig7c):** a sweep shows neither outcome depends on the length scale. Refitting the targets inside each fold for fig6e gives the same counts.
- **suppfig8:** the "transposed mean" the verifier suspected is what `removePotent.m` does. I print the map's inputs now, and the alternative centring gives the same outcome.

**Smaller additions:** the straight/curved condition pairs are printed (members end within about 5 mm of each other). suppfig2 now also shows each conjugate pair counted once. The repeat count in the fig3c text is corrected. The notes of the dimensionality claims now say how the unsorted units bear on them.

**Numbers corrected to match the run:** some figures in the old record did not match what the current code prints. These were the fig2c variance explained (now 83.4% to 94.4%), the fig3c AUCs, one fig3a frequency, the fig6b null range, and the fig7f-ldr-decoding skew-normal and null ranges. The notes now give the printed values.

**Recorded:** `verifications` round 1 for all 34 claims, with the verifier's reason and my response for each. The verifier agreed with every outcome as it stood before this revision. Its fig3g count of 5 of 14 frequencies within 10% is noted against the printed 6. The two `methods_unavailable` findings now also ask about the decoder subset size and the missing decoder code; the findings stay in their order. Nothing is committed.

**Not done**
- The GPFA decoders: there is no GPFA implementation in the environment, and the paper gives neither the number of latent dimensions nor the bin size.
- `runtime_minutes` for notebook 1 in `entry.yaml` says 50, though it now runs in 27. Changing it would invalidate the executed copies, so I left it.
