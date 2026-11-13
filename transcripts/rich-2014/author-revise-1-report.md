I've revised the attempt for every point in the round-1 report and re-run the entry. `python tools/entry.py all entries/rich-2014` passes with 0 errors; the notebook takes 266 s and its outputs are the same from one run to the next. The round is recorded under `verifications` in `attempts/rich-2014-01.yaml`. Nothing is committed.

**The main fix (problem 2).** The verifier was right: my pass rule P-a threw away every field that reaches the end of a track section, because a run cannot go past that end. P-a now counts such a field's edge as reached when the run gets within 20 cm of the end, a standard choice I recorded as a deviation. P-a now finds 852 fields instead of 791. The data set's own detection has 887 fields, and P-a now overlaps 842 of them, against 787 for the other pass rule (P-b).

**Outcomes that changed**
- **figs7a-mean-fields-per-animal:** partially reproduced → reproduced. All five per-animal means are within 10% under P-a.
- **fig3d-uniform-density:** partially reproduced → reproduced. The KS statistic under P-a is 0.0315 (tolerance 0.03 ± 0.003), p 0.360.
- **figs10-no-track-or-speed-influence:** stays not reproduced, but no longer rests on an assumption. With a separate random generator for each field set, both pass rules put 3 of 12 track-angle bins outside the interval (p 0.020). Five further shuffle sets give 3 or 4 bins under P-a and 3 under P-b, so the panel fails under both rules.

**Outcomes I kept against the verifier (disagreement recorded)**
- **figs6-few-field-cells-uniform:** kept reproduced, resting on P-a. The case for P-a is now stronger. It recovers 95% of the data set's own fields against 89% for P-b, and gets all five per-animal means within 10% against three. Its pass counts are also closer to the data set's.
- **figs11-no-boundary-remapping:** kept not reproduced, resting on P-a. After the fix, P-a still gives p 0.026 to 0.045 at the boundary between sections 3 and 4.
- **fig4c-active-subsets:** kept not reproduced, resting on the assumption that the simulated environment sizes are spaced logarithmically.

**Added or corrected**
- **figs3-cluster-quality (problem 7):** each recording period's own cluster info, RUN1 included, is also empty (0 of 253 units have a value). The claim stays blocked as data missing.
- **Missing fields (problem 3):** of the data set's fields that P-a misses, 29 fail the pass rule and 16 the 15 cm width rule. Using 1-inch bins, as the data set's own maps do, gives the same 852 fields, so bin width is not the cause.
- **Panel A test (problem 4):** the second test is now shown as not applicable to panel A, not scored as a pass.
- **Corners (problem 5):** a plot of each reconstructed track with its corners, their spacing (a corner every 1.20 to 1.55 m), and the number of 1 m distance bins the shuffle fills (3 or 8). The notes say the distance panel has little power.
- **figs12-pairs-uncorrelated (problem 6):** two variants. Pairs on different tetrodes show the same pattern. Against a null that keeps each animal's field locations, the observed correlation is within chance at every scale. The paper's test still finds it, so the outcome stays not reproduced.
- **figs11-propensity-stationary (problem 9):** the simulation now uses each animal's own section lengths.
- **figs5-silent-cells-low-rate:** added the silent-cell rate over all RUN1 time with no speed threshold, 0.021 to 0.027 Hz. That is further from the paper's 0.006 Hz, so this does not explain the gap.
- **Notes:** the fig3c-lomax-recruitment notes now say its ±0.005 tolerance is narrow against the statistic's spread (problem 10). The figs8 notes now say the open-field scale does not decide that claim (problem 8).
- Updated the conclusions, summary, README, findings and the runtime in `entry.yaml` to match the new numbers.

**Not done.** I added no questions to `questions/rich-2014.yaml`: the report names no place where the claims file misreads the paper. The track layout of Fig. 1 is not in the text I had, so the corner plot shows the reconstruction alone, with nothing to compare it to.
