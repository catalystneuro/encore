I've worked through all 12 points in the round-1 report and re-ran the entry. The final run passed in 126 s with no errors, `tools/entry.py check` reports 0 errors, and every conclusion matches the new outputs.

**Outcome changes**
- **fig4c-arena-registration-short-lived: partially reproduced → not reproduced**, as the verifier said. The criterion's partial outcome needs the arena frame to fall below the others after 10 s and not before. That fails twice: the conditions already differ at 10 s (p = 0.0106), and at 20 to 60 s the room frame drops below the arena frame.
- **fig5-error-inhomogeneous: kept as partially reproduced**, with the verifier's disagreement recorded. The criterion gives partial when "the tests hold but not every r". Under readings (b) and (c) every Rayleigh and Kuiper test holds, even though no r is near the paper's.
- **No other outcome changed.**

**Added or corrected**
- **Which data decide outcomes (problem 2):** the notebook now says outcomes are decided on the files as deposited, since the paper's counts imply it used them.
- **Clean variants (problem 1):** added for fig2, figs2, fig2c, figs3, fig5, fig5c and fig4c. The notes now say where outcomes depend on files shown wrong:
  - fig2: without session 1023R029, stable2 beats the arena frame in only 3 of 6 ensembles.
  - figs2: without 1023R029, no reading gives 4 room and 2 arena.
  - fig1c-directionality and fig4 change outcome without the bad files.
- **Tukey test (problem 3):** using the repeated-measures error term is now stated in the notebook as an assumption, with its reason. With the between-groups test, fig1c-directionality would be partially reproduced.
- **Tables and sensitivity checks:**
  - fig2: stable2 error against the shifted reference shows decoding at chance in 1026R157 and 1117R157.
  - figs2: the 4-and-2 count holds only for margins from 0.04 to 0.05.
- **fig4 gap (problems 7 and 8):** I added a check of why the arena frame scores lower than the room frame. The room-frame histograms are shifted by the arena's rotation. The tracker samples alone, with no spikes, show the same shift and the same order (room 0.068, arena 0.048, p = 7.55e-08). The text also says the main normalization leaves the raw displacement histogram.
- **fig5c:** I added the full 36-bin curve, the third-deepest minimum (325°), a shuffled null and a clean variant. The minima are deeper than every one of 1000 shuffles, and the clean variant puts them at 115° and 345°. I also corrected a value in the earlier notes: the second minimum is 63.9, not 63.3.
- **Question for a reader (problem 4):** the possible misreading of the fig5 claim is in `questions/park-2019.yaml`; the claim itself is unchanged. The head-direction reading is run as a variant: r is 0.104 to 0.550, every test is significant, and none reaches the paper's values.
- **cell-counts:** the 1001R029 and 1001R523 sessions were recorded on 1 October 2013 and 1 October 2014. The files carry no rat ID, so they can't explain the Table S1 differences.
- **Speed filter:** now called an assumption. The notes give exactly which readings and tests the result holds under.
- **Bin-start bias:** the decoder's labelling by bin start, which biases errors by about −5°, is documented in the helper and the deviations.
- **Record and README:** the round is recorded under `verifications` for all 22 claims, and the README is updated.

**Not done**
- I couldn't identify the paper's 38 speed units; no output in the data identifies them.
- I kept the shock-zone centre-point assumption, because the paper gives no other definition of relative proximity.
- Untracked dotfiles and folders I didn't create (`.bashrc`, `.vscode`, `scripts`, and others) appeared at the repo root. I left them alone; they shouldn't be committed.
