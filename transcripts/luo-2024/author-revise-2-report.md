No outcome changed and I proposed none. The round-2 verifier agreed with all 29 outcomes. The entry re-ran cleanly with `python tools/entry.py all`: 0 check errors, notebook passed in 117 s. Every number I cite below appears in the new outputs.

**Outcomes**
- `figs2-2-mouse-amplitude-cv-sag` stays reproduced but is now marked `assumed: true`. It rests on reading "saturated" as 1000 or more consecutive identical samples, because the code's own test cannot fire as written. Without that rule the sag p is 0.011, which misses the figure's 0.01. A deviation states the assumption, and a new `methods_unavailable` finding asks the paper's authors about it.
- **AHP width:** the verifier suspected why the cholinergic/noncholinergic AHP width comes out reversed, and the new output confirms it. In 43 of 47 cholinergic and 35 of 43 noncholinergic neurons, the potential never recrosses the half-amplitude level within the 100 ms window. Their measured width therefore runs to the end of the step, so it mostly measures the time left after the first spike:
  - spike latency plus width averages 495.5 and 495.6 ms;
  - width falls almost exactly as latency rises (Spearman rho -0.996 and -0.990);
  - noncholinergic neurons spike earlier, so they get the longer widths.

  In the 12 neurons that do recross, the width is 9.9 against 54.8 ms (p = 0.051). I added this as a second question for a reader in `questions/001261.yaml`. `fig2d-mouse-ahp` is still tested as the claims file has it.

**Outputs added to the notebook**
- All four amplifier fields per sweep: one set of values in all 152 files.
- The largest step in each file.
- For the 8 files where a test pulse comes before the step: the sweep counts and subjects. The pulse comes first in all 170 sweeps that hold a step.
- The per-neuron table of AHP width against latency asked for, with a flag for neurons that do not recross, and a macaque/mouse summary of the same.
- Tau using only fits with R² of 0.9 or more, as a variant: p = 5.1e-3, so it still fails.

**Text corrected**
- Every sentence the verifier quoted is fixed in the notebook, README and record:
  - the step range is now -100 to 1200 pA;
  - step spacing is now 5 to 100 pA;
  - "in every sweep" is now "in every sweep that holds a step";
  - the runtime is now "under five minutes".
- The species feature-count conclusion now says that, with the code's AHP window, AHP latency and width do differ, and drops "counting F1 would not raise the count".
- The record notes now say:
  - the macaque sample-size count also fails if read strictly;
  - both feature counts sit at the lower edge of their range, and the 200 pA reading puts each below it;
  - the tau outcome may reflect noisy fits on a small step.
- In the round-1 record, I added the two points the verifier said were missing: its problem 4 (the dropped files) and its note that the onset error likely changed the species feature count.
- Round 2 is recorded under `verifications` for all 29 claims. The verifier's points about the notebook's data-check text concern no one claim, so I recorded them under `sample-sizes`.

**Not done**
- I did not change the claims file. The AHP window and the F14 measurement span are with a reader.
- I did not commit or push.
