# Petersen & Buzsaki (2020) from dandiset 000059

Tests the findings of [Petersen and Buzsaki (2020)](https://doi.org/10.1016/j.neuron.2020.05.023)
on [DANDI:000059](https://dandiarchive.org/dandiset/000059/0.261115.0311), which holds 51 sessions
of 5 rats running a figure-8 maze while the medial septum was cooled: CA1 LFP, curated units,
head tracking and, in 31 sessions, the measured septal temperature.

Of 46 claims, 17 are reproduced, 19 partially reproduced, 8 not reproduced and 2 blocked; the 20
outcomes on place fields rest on an assumption about the maps the fields are found on. Cooling
slows theta and lowers its power, raises choice errors, and slows the theta oscillation of place
cells with the LFP (Figures 2, 4B and 6). Of the place field features of Figure 3, the
correlation of field size across states, the size predicted from fp and fLFP and the stability of
information are not reproduced, the size against fp is partially reproduced and the population
vector scale is reproduced. The stability of fp - fLFP and of the fraction of active cells is not
reproduced as the paper states it. With the slope range assumed here, phase precession flattens
during cooling against pre but not post; the comparison against pre is not significant without
the slopes at the bound of the search, or with the other ranges tried. Theta time lags of place cell pairs lengthen with cooling; phase
lags do not change when a pair's lag is read as the largest peak within pi of zero, and do when it
is read as the peak nearest zero. The distance-time compression of Figure 5 is blocked, as the
surface fit of the Methods fails on the data. The hippocampal temperature of the control
experiment is not in the dandiset.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper's place fields were drawn by hand, so the fields here follow the paper's automatic rule
of Figure 5, found on the maps over all trials (an assumption the place field outcomes rest on),
which gives more fields than the paper's 365. The attempt record, with the reasons
and the differences from the paper's method, is
[`attempts/petersen-2020-02.yaml`](../../attempts/petersen-2020-02.yaml).
