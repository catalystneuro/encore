## Verifier report, round 3: DANDI:001272 (Semenov et al. 2025)

The claims file has 19 claims and the attempt record has 19 outcomes. Only one outcome has a `proposed` change: figs1-near-threshold-delayed-aps (record line 88). No other outcome has a proposal, so this report covers that claim only.

| Claim | Proposed outcome | Agree? | My outcome if different | Reason |
|---|---|---|---|---|
| figs1-near-threshold-delayed-aps | not_reproduced (assumed: true) | Yes | — | See below. |

**The criterion.** The claims file's criterion is a single test per neuron. The median near-threshold session must have 1 to 3 APs *and* its first AP must be delayed (O5). The claim is reproduced when more than half of the neurons with APs pass. The criterion has no partial outcome for meeting one half of the test, so not_reproduced is the outcome when most neurons fail it. I said the same in round 2.

**The numbers come from the data (di8 cell 20).**
- Under the adopted readings (whole frame, F0 (a), height (b) read as prominence, O5 (a)), 1 of 3 neurons passes with O4 (a), and also 1 of 3 with O4 (b).
- With O4 (a), the per-neuron table gives a median of 1 AP for all three neurons. The median first-AP latencies are 5.7 ms (subject 2), 62.8 ms (subject 3) and 137.3 ms (subject 4). Only subject 4 reaches the 100 ms that O5 (a) requires.
- The proposal also says the criterion is met in 0 of 24 combinations under O5 (a) with prominence, and in 6 of 24 with the dF value. Both counts match the printed tables (the "by O5" lines).
- The function counts a neuron only if it is in both `few & delayed`, and it applies the threshold `n_ok > len(nt)/2`. That is the criterion as written.

**The choices were not made to reach this result.**
- Prominence was adopted after the round-1 null test, and on grounds unrelated to this claim (cell 11). Under whole/a/b, detections after the stimulus run at 0.91 per 100 ms with the dF value, against 0.02 per 100 ms with prominence.
- O5 (a) is one of the claims file's own readings. It comes from the paper's FluoVolt delay of 100 to 200 ms, together with the paper's statement that the Di-8-ANEPPS effects did not differ. I checked both passages in `paper/`.
- Both choices push this claim toward failure. Under O5 (b) with prominence the criterion is met in 20 of 24 combinations. So neither choice favours the claim.

**What remains open.** The outcome depends on O5. "Increasing the electric field strength reduced the delay" could support reading "delayed" relative to the neuron's own higher fields, which is O5 (b). Under that reading, every neuron's near-threshold AP is later than its APs at higher fields. The record states this, keeps `assumed: true`, and puts the meaning of "delayed" to the authors. That is the right way to handle it.

**Claims file.** On this claim it does not misread the paper. The quote ("Stimulation near the threshold elicited one or a few delayed APs") and the source of O5 (Results, paragraph 1 on 2- and 20-kHz unmodulated sine waves) match the text.

**The proposal agrees with the notebook and README.** The conclusion in cell 21 states the proposal and its numbers. The README and the cell 37 summary list the change as proposed. The notes on figs1-effects-same-as-fluovolt say the change leaves that outcome as it is. That is correct: its pattern condition already fails on figs1-culminates-in-sustained-depolarization.

One wording point, which does not bear on the outcome: cell 35 prints "near-threshold partially reproduced" as a hard-coded string. If the proposal is accepted, that string will be out of date.
