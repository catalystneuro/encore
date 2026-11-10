Round 1 is answered and the entry has been re-run with `python tools/entry.py all`: all four notebooks pass and `check` reports 0 errors. Nothing is committed.

**Outcome changes**
- **fig5e-fc-pmr-onset: blocked → reproduced, resting on an assumption.** The verifier was right that the time limit was not established. Eight parallel streams read all 27 fcx-1 archives in 691 s. With the data set's own UP states (`UPInts`) and EX units (`EAll`), tau = -0.221 (p = 2.3e-20, 986 units, 27 sessions), within 0.022 of -0.22. The spike-based ON intervals give -0.162, outside the tolerance. The data set lacks the files Figure5E.py reads, so this rests on taking `UPInts` for the code's UP states.
- **fig1j-down-resets-hd: blocked → not reproduced.** Tested in a new notebook, `posub_ring_000939.ipynb`, following makeRing.py. The angles before and after the DOWN state are nearly unrelated (resultant length 0.020, against 0.078 for the 99th percentile of shuffles). But one of 20 histogram bins falls outside the shuffle range, a deficit and not an excess near 0, and the criterion decides. This test fails by chance 3.5% of the time; on the 14 sessions whose ring follows head direction, no bin falls outside.
- **fig1k-hd-stable-at-onset: blocked → not reproduced, resting on an assumption.** p = 0.28 with below-threshold steps left out, which the Methods imply. Keeping them gives the paper's result (p = 0.027).

**Disagreements kept and recorded**
- **fig1b** stays reproduced (assumed). Figure 1B's axis (log10 HD info, -2 to 1, most cells near 0) fits bits per spike (median 0.12, 5 cells off the axis), not bits per second (median 0.54, 31 cells off). I added a question for a reader in `questions/mehrotra-2024.yaml`, because the verifier read "as the Methods define them" as the printed bits-per-second formula.
- **fig2f** stays not reproduced. Every reading fails the criterion, on different parts, and the outcome is the one all readings give. The verifier would block it as methods_underspecified.

**Fixes and outputs added**
- **Odd/even halving bug** (figs1i) fixed: spikes are now counted from all UP states and divided by the half's own rate. figs1i stays blocked, because first/second-half Pearson still fails (p = 0.43).
- **LFP sessions:** A3705, A3708 and A3711 show no gamma rise after DU, so their LFP is not shown to share the spikes' clock. They are now left out of the main LFP reading, with all 16 sessions as a variant. figs2d stays blocked and figs2e stays not reproduced.
- **Depth convention** now comes from the file: the probe description says "Channels sorted top to bottom of shank", and electrode 0 has the largest `rel_y` in every session.
- **Event-file alignment:** cross-correlograms for every session peak at -2.5 to -17.5 ms, so no event file is offset by tens of ms.
- **A3708 identity:** its NWB file matches the event file's session (session_id 200317b), but the event file fits no session's spikes.
- **Smaller points:** fig1g is now described as fragile, the NREM epochs past the last spike are discussed, and the notebook header tables are corrected.

**Not done**
- No outcome is under `proposed`: this is the revision after round 1, when outcomes may still change.
- fig3 keeps not_runnable where the verifier wrote other; the outcome, blocked, is the same.
- The delta-peak detection was not changed, since the verifier said it does not affect a conclusion; it is noted as noisy.
- The executed copies of `posub_ring_000939.ipynb` (re-run alone after adding the chance-rate check) and the markdown of the other notebooks were patched to match the sources after the full run, so their text is newer than that run. Outputs are unchanged.
