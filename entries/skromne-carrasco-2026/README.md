# Skromne Carrasco, Viejo & Peyrache (2026) from dandiset 001676

Tests the findings of [Skromne Carrasco et al. (2026)](https://doi.org/10.1038/s41586-025-10096-w),
"Months-long stability of the head-direction system", on
[DANDI:001676](https://dandiarchive.org/dandiset/001676/0.251205.2137). The dandiset holds 402
Miniscope sessions of the postsubiculum in ten mice (four weeks in one environment, two weeks in each
of four environments, four weeks of visits in random order, and five weeks with a single visit to one
environment), and one silicon probe recording in each of four mice.

Of 32 claims, 18 are reproduced, 6 partially reproduced, 3 not reproduced and 5 blocked. The probe
trials of Fig. 3 cannot be matched to earlier sessions, because each protocol has its own cell
registration and nothing links them. The probe recordings have no spike waveforms. The decoders across
all session pairs of Fig. 1k were not run, as their 1,883 fits are estimated at 80 minutes, over the
60 minute limit of a notebook. The outcomes, with
the reasons and the differences from the paper's method, are in the attempt record
[`attempts/skromne-carrasco-2026-01.yaml`](../../attempts/skromne-carrasco-2026-01.yaml).

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper's code is not public. Several method details are therefore assumptions, stated in the
notebooks: HD information on the smoothed tuning curve (it gives the paper's numbers of compared
sessions; raw HD information is shown for every HD cell claim but the ring of Extended Data Fig. 1h), unsigned pairwise offsets (they give the
paper's shuffle medians), the sign of a change in preferred direction (the earlier session minus the
later one) and the drift rate as a least-squares slope.

- `reproduce_skromne_carrasco_2026.ipynb`: the data check and every tested claim except the decoders.
  It took 35 to 41 minutes in recent runs, most of it streaming 402 files.
- `decoding.ipynb`: the head-direction decoders (Fig. 4e, Extended Data Fig. 8) and the estimate that
  blocks Fig. 1k, each under three variants. About 40 minutes, 19 of them opening the files.
- `hdstab.py`: loading, tuning curves, the HD cell rule, preferred-direction changes, pairwise
  offsets, circular tests and decoder features. Other notebooks on this dandiset can import it.
