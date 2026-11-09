I did steps 1 to 5 of the Author protocol and built the handover with `python tools/entry.py handover`. The entry passes `check` and `run` from a clean environment, and nothing is committed. The new files are `entries/001687-xiao-2026/`, `attempts/001687-xiao-2026-01.yaml` and `questions/001687.yaml`.

**The main risk:** the claims file makes the Methods' uncorrected responsiveness test (p < 0.05 at any distance) the main reading. That test cannot give the paper's own counts: it marks 1,061 of 1,160 units responsive, against 768 in the paper. The code's BH-FDR test gives 782, matches the deposit's labels unit for unit, and would turn several outcomes below into reproduced. Every claim is shown under both tests, and the question is filed for a reader.

## 1. Outcomes (41 claims)

| Claim | Outcome |
|---|---|
| si-unit-yield | reproduced (1,160 units against 1,141; SNR criterion not applicable) |
| fig2-wall-responsive-counts, fig2-distance-tuned-counts, fig2f-tuning-categories | not reproduced under the Methods' test; code's BH-FDR variant reproduces 1 and 3 |
| figs4a-baseline-activated-lower, figs4a-baseline-suppressed-similar, figs4c-untuned-no-change | reproduced |
| fig2de-preferred-distances-span, figs4ef-crossvalidated-stability, figs4j-ventral-location | reproduced |
| fig3a-decoding-above-controls, fig3-overall-decoding-accuracy | reproduced |
| fig6-model-telc-loses-map (the paper's model code, `elsewhere`) | reproduced |
| figs4b, figs4l, fig3c-decoding-by-distance, fig3c-decoding-error, figs5c, figs5de | partially reproduced (directions hold; some values or tests are off under the Methods' test) |
| 6 whisker-cutting claims | blocked, metadata_insufficient |
| 3 S1 whisker-kinematics, 2 tungsten, 1 GtACR, 10 TeLC claims | blocked, data_missing |

Totals: 10 reproduced, 6 partially reproduced, 3 not reproduced, 22 blocked. No outcome rests on an assumption.

## 2. Dataset, assumptions and questions

**Version.** I pinned 0.260821.2126, the latest published version. The paper cites none, and this version holds the same 191 assets as 0.260805.1529.

**What is there.** 67 processed sessions from 36 wild-type C57 mice, 1,358 units. My rates equal the deposit's stored tuning curves, apart from 48 units, almost all in the two 1-mm-step sessions. No recording is deposited twice. Missing: tungsten, TeLC, GtACR, anesthetized and single-row sessions, and tracked whisker kinematics, although the dandiset's description names the inhibition perturbations.

**Findings recorded in the attempt:**
- The processed files have no SNR, isolation flag or waveforms. Unit depth was therefore computed from 16 raw chunks per session, as a stated deviation.
- In the 25 whisker-cutting sessions, the post-cut passes exist only in the raw pass epochs and have no wall distance. The raw wall-actuator line has the same two levels at every distance, so distance cannot be recovered.
- The paper's 195 stable units from 18 mice cannot be identified; the deposit has 445 units from 25 mice.
- In two cutting sessions the full-array trials table includes 20 and 50 passes recorded after the gap where the notes place the cut.
- In the two 1-mm-step sessions, the stored tuning curves use one distance per 2-mm bin, while the Methods pool all of them.
- In the decoder script, the combined-group branch does not update the variable that selects the units it saves.
- The text's 656 tuned units conflict with Figure 2F; the data side with Figure 2F (600 tuned under the code's test).

**Assumptions and questions for the paper's authors:** none.

**Questions to a reader:** one, in `questions/001687.yaml`: whether BH-FDR should be the main reading of the responsiveness test.

## 3. Where the protocol was unclear

1. It puts the Methods first even when the Methods' reading cannot produce the paper's own expected values. I tested as written and filed the question.
2. It does not say what to do when a claim's population cannot be formed but a larger set can be analysed (the cutting claims). I blocked them as metadata_insufficient and put the results on the larger set in the notes.
3. The suggested clock check, decoding with shifted labels, fails when the shift is the same for every unit: the decoder simply learns the relabelling (70.0% against 70.6%). Shifting pass times by 30 s does work (11.8%), so I used that.
4. The rule "record the first reading the criterion lists" is ambiguous when readings vary on two axes (window and cross-validation). I recorded window (i) with 15 splits.
5. Two criteria have no partial rule (fig3c-decoding-error, figs5de-svm-robust). I applied the protocol's general definition of partially reproduced.
6. The protocol does not say whether a cut-down version of the paper's method is a deviation or a `too_large` block. I tested depth and SVM in reduced form (raw-chunk waveforms, every third time bin) and recorded both as deviations.
7. It does not say how dependent claims inherit a population when the upstream classification's main reading fails. I ran both classifications throughout.

## 4. Runtime and failures

- The agent run took about 1 h 50 min (08:24 to 10:14 UTC).
- The notebook runs in about 22 min; the SVM (8 min) and unit depth (7 min) are the largest parts.
- Two development runs failed on code errors and were fixed: a pandas column name clash, and a name defined after its first use.
- The final run passed, and its numbers are identical to the development run.
