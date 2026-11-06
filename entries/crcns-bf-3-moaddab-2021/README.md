# Moaddab, Ray & McDannald (2021) from CRCNS bf-3

Tests the findings of [Moaddab, Ray and McDannald (2021)](https://doi.org/10.1038/s42003-020-01554-4)
on [CRCNS bf-3](https://doi.org/10.6080/K0HH6H8V), which holds the spike times, mean waveforms and
behavioral events of 435 ventral pallidum units recorded from 14 rats during fear discrimination,
with the authors' MATLAB analysis scripts.

Of the 45 claims, 28 are reproduced, 15 partially reproduced and 2 not reproduced; none is blocked.
Most outcomes rest on two assumptions: the neuron groups and the k-means clusters are those the
authors' scripts produce, which match every count the paper reports. Firing is normalized as the
Methods describe it; the scripts normalize single trials differently, and their normalization gives
the paper's printed values. Ten of the 15 partial outcomes meet the criterion under the scripts'
variant (four failed on values alone, six on p values or intervals); five do not meet it under
either. In the normalization, the element that matters is Z-scoring single trials in place of
trial-averaged firing.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Found about the data set: recording was paused between trials, so the files hold only the 51.5 s
around each cue; the data descriptor does not name the event channels and misdescribes some cube
fields; there are 195 sessions where the paper reports 194; four pairs of units share most of their
spikes; and the paper's k-means clusters are a local optimum of k-means.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/crcns-bf-3-moaddab-2021-01.yaml`](../../attempts/crcns-bf-3-moaddab-2021-01.yaml).
