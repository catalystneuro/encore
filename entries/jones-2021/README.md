# Aery Jones et al. (2021) from dandiset 000165

Tests the findings of [Aery Jones et al. (2021)](https://doi.org/10.1016/j.celrep.2021.110159) on
[DANDI:000165](https://dandiarchive.org/dandiset/000165/0.211118.1526), which holds the 1 kHz LFP, MUA
spike times and position of PV-Cre, SST-Cre, PV-Cre/SST-Cre and empty vector mice in home cage and
linear track sessions after vehicle or CNO. `rest_home_cage.ipynb` tests the rest claims (SWRs, CA3
SWRs, dentate spikes, SWR-coincident SG), `run_linear_track.ipynb` the run claims (MUA, theta and gamma
power, coherence, frequency and theta modulation), `csd_cohort1.ipynb` the CSD claim on cohort 1, and
all share the helper `jones2021.py`.

| Claims | Outcome |
|---|---|
| SWR frequency up and SWR size down with PV+ suppression; FG coherence unchanged during run; theta coherence and frequency unchanged except DG frequency with PV+ suppression; baseline genotype differences | Reproduced (5; the last two rest on pooling frequency over a region's sites) |
| Rest SG power with PV+ suppression; FG frequency up with SST+ suppression; FG theta modulation down with PV+ suppression | Partially reproduced (3) |
| Other SWR, CA3 SWR, dentate spike, CSD, SWR-coincident SG, run, double suppression, empty vector, running speed and sex claims | Not reproduced (31) |
| Histology, slice recordings, fast ripples | Blocked: data missing (3) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
the differences from the paper's method.

Three properties of the dandiset bear on most results: the MUA spike times are offset from the LFP by
a session-specific lag (event-locked MUA is tested with each session shifted to its SWRs, an
assumption); four mice have no vehicle sessions; and in cohort 3 all vehicle sessions come before the
CNO sessions, so treatment is confounded with session order, and the empty vector control changes with
CNO (a check within the vehicle sessions explains only part of this). The LMMs are fitted by maximum likelihood from per-mouse, per-treatment sufficient statistics; for
features with millions of observations (frequency per peak) the variance estimates can move between
nearby optima, so p-values of those features are less stable than their coefficients. The attempt
record, with the reasons and the differences from the paper's method, is
[`attempts/jones-2021-01.yaml`](../../attempts/jones-2021-01.yaml).
