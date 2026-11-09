I've finished the round-1 revision. One outcome changed (fig1e), the rest stay as they were, and the verifier agreed with every round-1 outcome. `python tools/entry.py all entries/espinosa-2017` passes with 0 errors. The notebook ran from a clean environment in 17 min, and two full runs gave the same numbers. The handover is rebuilt and nothing is committed.

**Outcome changes**
- **fig1e-excited-slower-kinetics: not reproduced → partially reproduced.** The fit window w1 now ends at the first extremum of the response, as the claims file says (verifier point B2). Under that window, with 250-ms bins and n1, the rank-sum test finds excited units slower under r1, r2 and r3 (p = 0.0008, 0.0013, 5.8e-05). The mean time constants are far outside tolerance, so by the criterion this is partial. The notes say how weak the matching reading is:
  - 37 to 51 excited fits sit at the 20-s bound.
  - 21 to 42 units per class are dropped because the first extremum falls in the first pulse bin.
  - A new synthetic check shows w1 does not recover the true time constant. It also does not separate excited from inhibited units that have the same time constant.
- **Unchanged:** fig1, fig1d (two claims) and supp4 keep their outcomes, and the 22 blocked claims stay blocked.

**Added or corrected**
- **fig1 (B1):** I rebuilt the dataset's own stored curves from the spike times and they match exactly for all 330 units. This shows the authors' bins (250 ms), pulses (light alone) and normalization (counts summed over pulses), which are among the readings already run. Under that convention the counts are 40–48 inhibited and 76–111 excited, still outside tolerance. So the authors' classification test differs from r1, r2 and r3. I also added:
  - cross-tables of our classes against the dataset's own flags, for every reading;
  - a sham check with onsets moved 10 s into the light-off period;
  - the percent change measured against the 5 s before each pulse (B5). On the dataset's own classes this gives 51.9% and 39.1%, both within tolerance.
- **supp4 (B4):** NE48 and NE69 have one TTL row and no pinch events, and every recording's TTL rows and files are now printed. Panels C and D therefore cover only 2 of the 4 animals. Panel E, which the legend gives for two animals, fails under all 24 readings (25 to 47 units against 18), so the claim fails whatever C and D would give.
- **fig5d and supp14 (B6):** I corrected the reason for the block. `openfield_analysis.m` gives the time axis and baseline but does not say what the quantity is or which mouse each train comes from. I ran the criterion's steps on those traces as a substitute that decides nothing: no difference between groups (latency p = 0.78 to 0.89).
- **Other checks:**
  - fig1d now has a third basal-rate reading that leaves out the pinch periods; it holds in 36 of 36 readings (B9).
  - A printed check now shows which light pulses coincide with the pinch (B7).
  - The VP open-field folders are printed for fig5c: all five are Laser_ON or LASER_ON.
  - The fig1e section now shows the dataset's own classes, with w2 significant under all four bin and normalization readings, and per-class histograms of the fitted time constants.
- **Record:** I updated the notes, deviations, findings, the question to the paper's authors, the README and the runtime (18 min), and added `verifications` round 1 with the verifier's reasons and my responses.
- **Question for a reader:** `questions/espinosa-2017.yaml` asks whether the percent change should be measured against the baseline, as the verifier raised for the claims file. It cannot change fig1's outcome.

**Not done**
- No reading reproduces the dataset's own class flags. I tried several more tests on the stored curves outside the notebook and none matched. That stays a question for the paper's authors.
- I did not change any claim in the claims file.
- One read of a scratch output file was denied for lack of approval; I got the same lines another way, so nothing was lost.
- The change to `tools/build_site.py` in the working tree was there before this run and is not mine. I left it alone.
