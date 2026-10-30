I've answered every point in the round-1 report and re-run the entry. `python tools/entry.py all entries/000447-tang-2023` passes: 0 errors, the notebook runs in about 23 minutes, and a second run gave the same numbers. The round is recorded under `verifications` in the attempt record: the verifier disagreed with four of my outcomes and agreed with the other 28.

**What changed in the outcomes**
- **fig2f-switch-dynamics**: reproduced → partially reproduced. I fixed the labelling bug (problem 1): reading (b) now labels only the first ten N trials. Under it, CA1 does not rise at the switch (p = 1). The criterion requires both readings, and CA1 rises only under (a).
- **figs3d-pfc-similarity-over-trials**: reproduced → partially reproduced. The criterion requires every reading, and CA1 falls under N alone and N' alone. I added each animal's own final kept trial as "last" and the session each kept trial comes from (problem 3).
- **Blocked as methods underspecified because of the smoothing width (problem 4)**: figs5e, fig3d and fig3e, and also **figs4d**. The claims file gives a rule for fig2d: when 8, 4 and 2 cm give different outcomes, the claim is methods underspecified. I now apply that rule to every claim that uses the linearized maps. The new 2-cm run of figs4d finds an outlier (Grubbs p = 0.007), so figs4d changes too.
- **fig4d-pfc-ccgp**: blocked, methods underspecified. With 8-cm single-trial maps, 10 of 16 decoders pass once ties are counted. At 4 cm 15 of 16 pass, and at 2 cm all 16 pass. The Methods give no smoothing for these maps.
- **fig4d-ca1-ccgp-chance, figs7b and figs7d**: blocked, because they depend on fig4d-pfc-ccgp and the protocol blocks a dependent claim with the claim it depends on. Their results are in the notes. fig4d-ca1 would be not reproduced at every width and filling variant.
- **fig3h and fig3j** are now marked as resting on the gap filling, and fig3fg with them. Without filling, at 2 cm, the PFC part fails.

**What I added or corrected**
- **CCGP ties (problem 2)**: ties with the shuffles are now counted, and the fraction of test points predicted as class 1 is printed for each decoder. 8 of the 16 CA1 decoders predict a single class for every test point.
- **Decoder check (problem 7)**: cross-validated N' decoding gives a median error of 12 cm, with 64% of CA1 bins on the right trajectory. I also print the fractions decoded onto the current trajectory and the current arm in N and F. The large errors come from decodes onto the other trajectory on the same arm, which the criterion counts as far.
- **ZT2's trial count (problem 8)**: counted from position, ZT2 made 22 well-to-well transits in F against 24 rows in the trials table, so the table is complete.
- **Manifold variants (problem 5)**: the manifold tests and CCGP are re-run with unfilled maps and with 4 and 2 cm smoothing. The distance helpers moved into their own cell so these results print above the conclusions that use them.
- **Smaller additions**: a native-map peak variant for fig2d (problem 10), CA1 shuffle tests at 4 and 2 cm for figs3a, and 4 and 2 cm runs for figs4d and fig2f.
- **Stale numbers**: many conclusion and record numbers came from an earlier run; they now match the current outputs.
- **Text and findings**: the header, summary and README now describe the smoothing-width rule. One new methods question went to the authors, on how the single-trial maps were smoothed and gap-filled, and the existing width and fig2f questions were updated.

**What I did not do**
- I kept figs4-ramping-generalization blocked for too few cells (problem 6), which the verifier also gave. A population vector over 1 or 2 cells is undefined or always ±1, so the 3-cell floor stays.
- I could not compare the error scale with Figure 2E: the figure image is not in `paper/`.
- The geometric null (figs7b) and the dichotomy test (figs7d) were not re-run at 4 and 2 cm, and unsmoothed single-trial maps were not tried.
- No question went to `questions/000447.yaml`: the verifier reported no place where the claims file misreads the paper.
