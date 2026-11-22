# Gable, Newman, Young, Scheib, Bliese, Miller & Kerlin (2026) from dandiset 000010

Tests the findings of [Gable et al. (2026)](https://doi.org/10.1523/jneurosci.0974-26.2026) that
can be tested on [DANDI:000010](https://dandiarchive.org/dandiset/000010/0.220126.1905), the ALM
silicon-probe recordings of Li et al. (2015) that the paper reanalyses for Figure S4 and Table 5.
The paper's own two-photon imaging of tuft synapses and dendrites is not public.

| Claim | Outcome |
|---|---|
| The reanalysis includes 11 mice, 20 sessions, 753 same-range and 6,586 different-range pairs | Not reproduced |
| The lowest coupling bin is more correlated within than across bins | Partially reproduced (assumed reading) |
| The three highest coupling bins are more correlated within than across bins | Not reproduced (assumed reading) |
| The three middle coupling bins show no such excess | Reproduced (assumed reading) |
| 30 claims on the paper's imaging | Blocked (data missing): the data are not public |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper's code does not hold the step that builds its per-session arrays from the dandiset, so
the unit filter, the firing-rate measure and the trial set are run under every reading the paper
allows, and one reading is adopted where the outcomes differ. No reading selects the paper's 11
mice and 20 sessions. Half of the files store some units twice under a repeated id; they are
counted once. The attempt record, with the reasons and the differences from the paper's method,
is [`attempts/gable-2026-01.yaml`](../../attempts/gable-2026-01.yaml).

- `reproduce_gable_2026.ipynb`: the analysis. It takes about four minutes, most of it streaming
  the files.
- `alm_coupling.py`: loading the files, the session selection, trial-specific activity,
  population coupling, pair correlations and the session bootstrap. Other notebooks on this
  dandiset can import it.
