# Round-2 verifier report for dvali-2025-01: Dvali et al. 2025 on DANDI:001075

## 1. Outcomes and assumptions

The claims file has 39 claims and the attempt record has 39 outcomes, one per claim. They are 10 reproduced, 5 partially reproduced and 24 blocked (21 `not_runnable`, 3 `data_missing`).

- **Agreement.** I agree with all 39 outcomes. The two outcomes with the narrowest margins are:
  - **fig5a-signaling-rich-club (partially reproduced):** it fails only on the one-SD rule at k = 4. There the null SD prints as 0.000 and φ minus the null mean is 4.19e-05 (cell 52).
  - **ave-most-connected-both (reproduced):** it holds only under reading (b) and the main anatomy.
- **The `not_runnable` reason.** In round 1 I said `not_runnable` was not an allowed reason. The record cites protocol step 1.5 and the schema, and cell 15 prints 0 graph-tool files on PyPI. I cannot check the protocol from my materials, so I withdraw that objection.
- **The three claims marked `assumed: true`.** These are anatomy-network-properties, fig5b-degree-correlation and ave-most-connected-both. Each states its assumption: the four EM sources from pumpprobe, with gap junctions in both directions. The assumption is reasonable because it is the senior author's lab code and it matches the paper's control densities (0.0330 and 0.0288, cell 59). In each of the three claims the outcome changes under a variant (cells 32, 62, 71).
- **One assumption not flagged.** ed6-anatomy-feedforward has no criterion in the claims file, so its outcome rests on a criterion the author wrote. That criterion is stated in the deviations but the claim is not marked `assumed`. The outcome is the same under all variants (cell 42), so this is a bookkeeping point.

## 2. Sentences the printed numbers do not support

- **Record, anatomy-network-properties:** "three of four outside tolerance" (White N2U variant). Cell 32 prints density 0.0823, which is below the lower bound of 0.0828 (0.092 − 0.0092). All four values are outside. Cell 33 lists edges, clustering and sigma as outside and leaves out density.
- **Record, fig5a-signaling-rich-club:** "local maxima at k = 3, 23, 25, 29, 42 and 48 (1000 rewired networks; the same with 500 and 100)". With 100 networks cell 52 prints `[1, 3, 23, 25, 29, 42, 48]`, which adds k = 1.
- **Cell 40:** "nor for the code's fraction measure, under all five seeds". Cell 39 prints the fraction measure only for the claim's seed. The other-seeds table covers the count measure only.
- **Record, ed6-signaling-not-feedforward:** "smallest p 0.0063 to 0.0149". Cell 39 prints 0.014828, which rounds to 0.0148. This is trivial.
- **README:** "It takes about eight minutes". Cell 74 prints a runtime of 5.1 min.

I checked every other sentence of the Result conclusions (cells 24 to 72), the Summary (cell 73), the README and the record's notes against the outputs, and they are supported.

The record states my round-1 reasons in my own words and faithfully, including my "Not checked" items. Two small points:
- It says I "found no place where the claims file misreads the paper". That is a fair inference, but my report did not say it.
- The fig5c response answers a point (the "code's list" of 15 neurons) that my report did not raise. That response is harmless and agrees with the legend of Extended Data Fig. 12a (paper line 2294).

## 3. Round-1 points

**Resolved:**
- **P1 (21 SBM claims blocked).** The block is accepted as `not_runnable` (see section 1). The author declines to use the memberships printed in Tables 1 and 2 because the protocol forbids embedding the paper's results. That is a defensible reading, and the outcomes are blocked either way.
- **P2 (rich-club-controls partly testable).** The one buildable pair is now run (cell 59). Its overlap is empty under (a) and AVEL/AVER under (b), with 8 of 14 neurons kept and 5 new, against the legend's 9 of 15 and 4 new. The outcome stays blocked, which is correct because the criterion needs all three pairs.
- **P4 (stimulation counts are a subset).** This is now stated in cell 49 and in the notes.
- **"Not checked" items:**
  - Cell 15 shows that no pinned source holds q-values.
  - Cell 17 shows the neuron lists are identical to those in the paper's code.
  - Cell 59 prints the 1.25-contact network.
- **P5 to P8.** These needed no action.

**Remaining, bearing on a conclusion:**
- **P3, the EM source assumption.** It is stated and flagged, but three outcomes hold only under the main reading:
  - anatomy-network-properties: with the White N2U adult, C = 0.233.
  - fig5b-degree-correlation: with the White N2U adult, r = 0.169.
  - ave-most-connected-both: AIB leads under both variants.
- **fig5a-signaling-rich-club.** The partial outcome turns on a one-SD test that is degenerate at small k, where N_k ≈ N, and on a rewiring written to replace graph-tool's. This is the claims file's choice; I report it and do not correct it.

**New, not bearing on a conclusion:**
- The `swapping_edges` port printed in cell 17 counts every draw toward `max_tries` (4000). The original does not count the `continue` cases (a repeated source, an empty neighbour list, or v == y).
- The notebook does not print how many swaps each null network received.
- The edge-swap z-scores in cell 42 are far from the threshold, except anatomy S→I at 0.35 and I→M at 0.58, which are clearly non-significant. So this is unlikely to change ed6-anatomy-feedforward.

I found no new place where the claims file misreads the paper.

## 4. Critical findings

None of the 12 findings is rated `critical`. Findings 1 to 4 are `major`, 5 to 8 `minor`, finding 9 `none`, and 10 to 12 are `methods_unavailable` or `paper_inconsistency` with no severity.

Finding 2, the unmarked interpolated frames in the cited version's GreenSignal (17% to 68% of frames per file, mean 42%; cell 11), is the closest to critical: the data differ from their description and the cited files do not mark it. `major` is defensible, because the next version marks those frames and the effect is a smoothing of the signal. It does not mix up recordings, subjects, units or clocks. Cell 19 shows the stimulation times are on the signals' clock in 108 of 108 recordings, and cell 9 shows no recording is deposited twice.
