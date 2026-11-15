# Petersen & Buzsaki (2020) from dandiset 000059

Tests the findings of [Petersen and Buzsaki (2020)](https://doi.org/10.1016/j.neuron.2020.05.023)
on [DANDI:000059](https://dandiarchive.org/dandiset/000059/0.261115.0311), which holds 51 sessions
of 5 rats running a figure-8 maze while the medial septum was cooled: CA1 LFP, curated units,
head tracking and, in 31 sessions, the measured septal temperature.

Of 46 claims, 17 are reproduced, 18 partially reproduced, 10 not reproduced and 1 blocked; the 21
outcomes on place fields rest on an assumption about the maps the fields are found on. Cooling slows theta and lowers its power, raises choice errors, and
slows the theta oscillation of place cells with the LFP (Figures 2, 4B and 6). The place field
features of Figure 3 and the stability of fp - fLFP, information and the fraction of active
cells are not reproduced as the paper states them. Theta time lags of place cell pairs lengthen
while phase lags do not change. The hippocampal temperature of the control experiment is not in
the dandiset.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper's place fields were drawn by hand, so the fields here follow the paper's automatic rule
of Figure 5, found on the maps over all trials (an assumption the place field outcomes rest on),
which gives more fields than the paper's 365. The attempt record, with the reasons
and the differences from the paper's method, is
[`attempts/petersen-2020-02.yaml`](../../attempts/petersen-2020-02.yaml).
