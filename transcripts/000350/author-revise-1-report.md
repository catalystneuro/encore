No outcome changed. The verifier agreed with all 19 outcomes in round 1. Five blocked claims now have a different blocking reason. The entry passes `check` and the final run passed in 881 s, with every conclusion matching the new numbers.

**Blocking reasons changed, as the verifier argued:**
- **fig2dg-nmf-components:** now `methods_underspecified` (was `data_missing`). The claim is about consistency across fish, and the paper's cross-fish clustering was tuned by hand. The notes now name the per-fish NMF that could be run and say why it would not test the claim.
- **fig1k, fig1f, fig7-ne-mismatch, fig7-glia-accumulate:** now `metadata_insufficient` (were `data_missing`). The protocol codes are not described, so these protocols cannot be identified even if they are in the files.

**Added or corrected:**
- **New data check on the protocol codes,** with the plot of gain, velocity and code the verifier asked for:
  - Code 33 is a 0.3 to 0.5 s speed-up of the grating in open loop, not the Figure 1K probe.
  - Code 52 is a randomised gain.
  - Codes 51 and 53 do not consistently mean closed and open loop.
  - `TotalStimulusVelocitySignal` stays between -0.002 and 0.008, so it does not hold the velocity it describes. This is recorded as a new finding.
  - A table gives the closed-to-open switches in the two-colour files.
- **Variant that keeps the epochs cut by a period's edges** (the verifier's problem 1), with a synthetic check and the onsets dropped per fish (0 to 8). fig1h, fig1i, fig2c and fig2h come out the same as before.
- **fig1j:** passive fraction by gain level, before and after the first open loop, with protocol codes. Passivity does not fall with the gain.
- **fig2c:** tests on the first five onsets after each open-loop start, a 300 s stretch of the raw traces with behaviour, and the correlation between glial and neuronal traces. In the two failing fish it is 0.58 and 0.59, against 0.06 and 0.15 in the others. This is recorded as a finding.
- **figs2a:** SD measured within each period, raw and detrended. It is higher in open loop in 8 of 8 neuron fish and 4 of 4 glia fish.
- **fig2h:** variants requiring the gain above 0 over the whole window. Still 2 of 4.
- **Bug fix in fig1c:** the bouts counted after a switch are now limited to that open-loop period, with a synthetic check. No number changed.
- **Records:** the attempt record now has round 1 under `verifications`, and the notes and findings are updated. I also updated the header, summary, README and `entry.yaml` (runtime now 15 minutes).

**Not done:**
- **Figure 7H part of fig7-glia-accumulate:** not tested. Only one two-colour fish (20170203-1) has more than 4 switches from closed loop to open loop, which is not enough for a claim made over fish.
- **Weighting by events for fig1c and fig1i:** not added. The criterion fixes the per-fish median, and the event counts and the strict variant are already printed.
- **Supplemental Information:** not read. It is not in the lab-site PDF (saved under `paper/`), the paper is not in PubMed Central, and the author run found Cell's site blocked the download.

Untracked files I did not create appeared in the repo root (`.bashrc`, `.gitconfig`, `.idea`, `scripts` and others). I left them as they are; the workflow should not commit them.
