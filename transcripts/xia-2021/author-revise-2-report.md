Round 2 is answered: all outcomes are unchanged, and I've proposed one change (figs12) for round 3. The entry re-ran cleanly with `python tools/entry.py all entries/xia-2021` (0 errors, notebook passes in 118 s), and the existing results are the same as before.

**Outcomes**
- **figs12-3v-propagation:** I agree with the verifier. The outcome stays `partially_reproduced`, as verified, with a `proposed` change to `blocked` (`data_missing`). The criterion's partial outcome needs the order in two of three mice, and only one mouse is deposited. The one-mouse results stay in the notes.
- **fig7-peak-timing:** I kept "reproduced" and recorded the verifier's disagreement (it would give partial at most). I did not propose a change. The criterion counts a pass under either reading, and reading (ii) passes in 30 of 36 variants. The criterion's own partial outcome is met under the same reading, so partial would not follow from it either. The verifier's real objection is that reading (ii) does not fit the paper's own times (rostral 8.80 s), so I added it as a reader question in the new `questions/xia-2021.yaml`. If a reader drops reading (ii), this claim would be not reproduced.

**Added to the notebook**
- **fig2d:** it now prints the valley height (5.19) and how much of each peak the passing reading keeps: 54% of the main peak and 30% or 23% of the second. The conclusion now says the share passes only by the letter of reading (b), and that the usual ways of splitting the two peaks give 65.8 to 69.1%.
- **fig7 and figs12:** the frame is now run turned every way. Flipped top to bottom or turned 180 degrees, the order holds in 0 of 18 variants. The frame being rostral up is now recorded as an assumption on all three Fig. 7/S12 claims, and the "decides nothing" wording is gone.
- **fig7-peak-timing:** prints the paper's own times under both readings.
- **figs16:** prints the highest AF647 value after its minimum. It passes the pre-stimulus mean in 3 of 6 readings and the mean + 3 SD in none. The verifier counted 4 of 6, but its own rise-against-drop comparison gives 3, so the record uses 3.

**Text corrected**
- Cell 22: the signal from 21 to 30 min is now 0.055 to 0.250, 1.3 to 5.9 times the pre-injection level.
- Cell 28: the first-rule densities are now 17.8 to 64.4.
- figs16 conclusion and notes: the false "without passing its pre-stimulus level" is replaced with the 3 of 6 count.
- fig6: now gives the main reading's 10 s bin test p of 0.0103, which is not below 0.01.
- The methods_unavailable finding now gives 17.1 to 40.1%, and asks whether rostral is at the top of the deposited frames.
- README: run time and table rows.
- Summary table: rows updated.
- Round 2 is recorded under `verifications` for all 29 claims.

**Not done**
- **LLOD reading (c):** still not run, because it needs the lines of Fig. 4B(ii) and the entry reads no figures. The verifier says this changes no outcome.
- **Orientation:** still not checked in the notebook, for the same reason. It is stated as an assumption, and the notebook shows what each other orientation gives.
- **Housekeeping:** nothing committed. The untracked dotfiles and `scripts/` in the repo root are not mine and I left them alone.
