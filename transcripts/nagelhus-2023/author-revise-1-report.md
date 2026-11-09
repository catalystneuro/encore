I've worked through the round-1 report, re-run the whole entry (all six notebooks pass, and `check` shows 0 errors), and recorded the round under `verifications` in the attempt record. Nothing is committed.

**Outcome changes**
- **fig1e-object-cells-and-object-vector-cells**: partially reproduced → **not reproduced**, as the verifier gave. No reading has the object-cell and object-vector fractions within tolerance at the same time.
- **fig7-slope-variant**: partially reproduced → **not reproduced**, as the verifier gave. Two of the four correlations miss, and spatial correlation has the opposite sign.
- **figs5d-control-sessions**: still blocked, but the reason is now data missing instead of "other", as the verifier gave. The control populations are not deposited.
- **Totals:** 30 reproduced, 5 partially reproduced, 9 not reproduced, 13 blocked.

**Fixed and added**
- **figs7e (point B1):** the verifier was right that each trial picking its own top words leaks the trial label. The words are now picked once per session and distance bin over both trials, as the claims file says. The claim still holds: words beat counts in 80 of 80 pairs (p = 7.9e-15), at 0.053 to 0.064 bits against about 0.001 for counts. The old selection is kept as a labelled variant, and a question asks about the paper's "In a given trial" wording.
- **fig1d:** the range fails on a few cells. Between 2 and 19 tuned cells lie beyond 88.8 cm, and without them the largest distance is 80.4 to 87.9 cm.
- **Field detection (point B7):** I added a variant that joins field bins only along edges. It changes the field count by under 1% and changes no outcome.
- **figs6 (occupancy decoder):** I added per-session accuracies and a control that tells the first half of the no-object trial from its second half. The control shows the same dependence on distance (p = 3.8e-5), so the failure comes from the decoder as I built it, not from the object. The notes now say so.
- **fig6c:** I added a run with 100 subsets per size. With 20 subsets, sizes 5 and 10 are significant in only 0 to 3 of 5 groups.
- **CA3 (figs3a):** I added per-session counts. Several sets of sessions add up to the 28 extra cells, so the paper's 313 can't be identified. Dropping the session with reversed object positions doesn't change the outcome.
- **figs2c:** I added a variant using the proximodistal order of the cell counts in the Supplementary Figure 2C legend. It gives p = 0.18 to 0.37 under the Methods' template widths and 0.022 to 0.065 under the code's.
- **Data check:** it now lists every field name in every file. The tracking holds only timestamp, x and y, and no unit has a probe, depth or channel, so the head-direction block is confirmed from the files themselves.
- **Questions:** two new ones in `questions/ebrains-q0fg-1x8.yaml`, on figs7e (which words to keep) and figs2c (whether the legend order may stand for the implant sites).

**Where I kept my outcome against the verifier**
- **Blocked claims:** fig2d-rate-overlap, figs3f, figs2d, fig4e, figs5e, fig6c and fig6d stay blocked as methods underspecified. Each has readings allowed by the claims file that give different outcomes. The protocol blocks such a claim, and picking one reading would be my own choice.
- **ovs-method-extra-cells:** stays blocked. Its pass rests on an exclusion rule the claims file doesn't give, and the question about it is still open.
- **figs6hij:** stays blocked as data missing, because the head-direction test can't be run.
- **Partially reproduced:** fig1c, fig1d, figs4 and fig7 keep this outcome. In each the effect is present and only part of the criterion misses.

Each of these disagreements is recorded with the verifier's reason in its own words and my response.

**Not done**
- I didn't use the legend order to decide figs2c, because the claims file doesn't give it; it waits on the new question.
- I didn't try to decide which 313 CA3 cells the paper used, because the files can't tell.

The text changes are in the six notebooks, `objcode.py`, `README.md`, the attempt record and the questions file.
