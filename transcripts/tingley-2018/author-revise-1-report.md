I've revised the attempt against every point in the round-1 report, re-run it with `python tools/entry.py all entries/tingley-2018`, and recorded the round under `verifications`. The run took 2,331 s with 0 check errors, and its outputs are identical to the run the conclusions were written from. Nothing is committed.

**The main change: how bins with no spike enter phase decoding.** I agreed with the verifier's first point (B1). Leaving those samples out lets the phase decoder read where the cell fires. The new decoder calibration in the notebook shows it on real data: each trial's spike phases were shifted among its spikes, with positions kept. Under the left-out treatment those shifted phases beat rate in 0.21 to 0.54 of conditions. Setting undefined phase to 0 gives 0.03 to 0.06, close to the real data's 0.04 to 0.08, so that is now the adopted assumption. Leaving bins out is kept as a variant. Ties between equally near template bins are now broken at random (B5); sending them to the lowest bin is shown as a variant.

One thing the calibration also shows: the paper's phase-against-chance test passes the shifted phases almost as often as the real ones (0.380 against 0.405 of neurons). Under either treatment that test mostly detects where the cell fires, not its phase. This is in the notes.

**Outcome changes**
- **To not_reproduced:**
  - fig2-ls-phase-vs-shuffle: 0.39 to 0.50, against 0.89.
  - fig2-ls-phase-beats-rate: phase better for under a third of neurons.
  - fig2e-ls-phase-lower-mse: phase MSE is above rate MSE.
  - figs1f-trial-counts: the criterion has no partial rule.
- **Partially reproduced to reproduced:**
  - fig1g-phase-more-info-fine-scale: passes under one reading (37 of 44 smoothings). The shifted-phase null gives the same fine-scale excess, so the notes say the match does not show phase information.
  - fig4d-depth-gradient: holds only under the samples-split, 1.5 cm reading, by a bare majority (26 of 47 sessions). It also depends on which way sites run along a shank, which the files do not store.
- **Reproduced to partially reproduced:** fig4e-onset-mediolateral. The correlation is below 0.8 under every reading. Watson-Williams, now run, does not apply because the onsets are too dispersed.
- **No longer blocked.** I agreed the cost estimate did not support blocking (B9). Peer prediction now runs at about 0.5 s per pair, on a random 7% of LS unit-conditions (7,098 pairs).
  - fig5-assemblies: not_reproduced (0.266 or 0.075 of pairs; best window 4 or 20 ms).
  - fig5g-assembly-neurons-stronger-phase: not_reproduced.
  - figs5-assembly-independent-of-locking: reproduced.
  - fig6e-assembly-position: partially_reproduced.
- **Disagreement kept and recorded:** fig1i-hpc-rate-phase-equivalent stays not_reproduced. The verifier read it as reproduced from one rate-map reading. That came from the lowest-bin tie rule. With random ties, the KS test finds a difference for both rate maps.

**Other fixes**
- The best-smoothing curve is now smoothed as MATLAB's `smooth`, so the 49-bin drop rule works (B4).
- Phase information uses the same set-to-0 treatment as the decoder, with a shifted-phase reference printed beside it (B3).
- fig4d and fig4e run under every decoder reading, both session depths and both site directions (B6, B8).
- figs7 now uses 10 ensemble draws.
- The trial-count division of makeFig1.m is shown as a variant.
- The "ballistic only" statement is now read from the files.
- A null calibration of the speed test was added; it passes 0.2 to 0.5% of conditions, so the test is conservative.
- DT8 is flagged as having hippocampal channels but no hippocampal units.
- The header no longer lists outcomes.

New findings ask the paper's authors about tie-breaking and the peer-prediction fit. Two findings are about the data: DT8's missing hippocampal units, and the unstored probe depths and site order.

**Not done**
- figs3 and fig7 stay blocked: I had no time to run them.
- figs6 is unchanged. Its conditions per session and the columns of the position table were not checked further.
- The verifier found no misreading of the claims file, so no questions were added.
- The position-clock check is weaker with random ties: recorded positions beat positions 1 s later in only 30 of 47 sessions. It is reported as consistent with aligned clocks, not as proof for every session. The spike-to-LFP clock is still clear in all 47.
