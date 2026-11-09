No outcome changed and none is proposed. The verifier agreed with all 24 outcomes, and nothing in the new run gives a reason to change one. The final `python tools/entry.py all` passed: 0 check errors, and all six notebooks ran from a clean environment in 58 minutes. Nothing is committed.

**The main problem: the text described a different run from the printed outputs**
- **Cause and fix:** the two runs most likely differed because the multithreaded BLAS library sums in a different order depending on how many CPU cores the machine has. Every notebook now uses one BLAS thread. The re-run prints exactly the verifier's numbers: 485 selected cells, 165 passing the shuffled control, 202/67/1150 cells per class, V = 743.5.
- **Rewritten from the printed outputs:** every "Result" cell, every Summary, the README, the record's `measured` values, notes and round-1 responses, and the numbers quoted in `questions/000483.yaml`.
- **The four statements that contradicted the printed numbers are fixed:**
  - fig5-three-classes: the centred variant does peak at k = 3 for selective cells (0.114, 0.393, 0.004). The outcome stays not reproduced, because the criterion decides on readings (a) and (b) and only reports the variant.
  - fig6b-landmark-cells: the spikes interval includes 0.18.
  - fig6a-population-light-off: the HeadingDecoder intervals lie between 0.10 and 0.18, so they include neither.
  - somata fig5e: the heading-like and landmark-like shares are 0.677 and 0.230.
- **Header tables:** the out-of-date claim tables at the top of `axons.ipynb` and `somata.ipynb` are corrected.

**Added**
- **Decoder checks in `decoding.ipynb` (point 4):**
  - **HeadingDecoder:** my reimplementation decodes synthetic cells at 0.908 to 0.999, so the algorithm as written works. On the real data it gives 0.20 to 0.22, close to a Bayes decoder trained and tested on different trials (0.24 to 0.26). I no longer describe it as decoding "near chance".
  - **Leakage:** the Methods themselves resample each trial to 200 bins and then split even and odd time points, so the shared frames the verifier flagged are part of the paper's own procedure. Two Bayes variants with no shared frames now appear under every claim. They lower light-on accuracy for all tuned cells from 0.708 to 0.532 (dF/F) and from 0.712 to 0.296 (spikes). This is recorded as a finding, since the paper's accuracies may be raised the same way.
  - **Effect on outcomes:** none changes. fig6b-180-errors is now called fragile: without shared frames it holds for dF/F but fails for spikes. I kept it as reproduced because the variants are not readings in the claims file.
- **fig2f:** the text now says the mirroring and the choice of 5 of 7 pairs cannot be checked against the data, and that the clock is not established. The chamber-rotation file `SKKS112-PlatformRotation-002` barely rotates (median step 0.12° per frame), which is now a finding.
- **figs5:** the text now calls the pass fragile, since only one mouse passes and the pooled random pairs mix files.
- **Questions file:** a new question for a reader on the claims file's paraphrase of the trial rule. The question on the shuffled-control criterion was already there.
- **Record:** round 2 is recorded under `verifications`, with the verifier's reasons in its own words and my responses.

**Not done**
- **Selection test passes noise (B1):** I did not change it, because it is the paper's own procedure. The notes still say about a third of the selected cells could pass by chance.
- **fig2f checks:** derotation artefacts and the head-versus-chamber heading definitions cannot be checked from the files.
- **fig1h:** where the cue sits in the heading frame is in neither the files nor the code, so the overrepresentation part stays open.
- **fig5k:** kept as `metadata_insufficient` instead of `data_missing`, because the files exist and what is missing is the ROI matching and which blocks are standard rotation.
- **Risk for the next round:** the one-thread fix brought this machine's numbers in line with the verifier's. If round 3 runs on a machine with a different kind of CPU, small differences could still appear.
