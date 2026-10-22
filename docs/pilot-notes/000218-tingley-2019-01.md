# 000218, Tingley et al. 2019

Four claims reproduced, seven partially, ten not reproduced and ten blocked,
all on the dandiset. Round 1 gave its own outcome for each claim from the
notebook with its conclusions removed and agreed with 30 of the 31; it gave
not reproduced for `fig5d-lag`, which the author kept at partially
reproduced because the coupling part of the claim holds and the lag part
does not. Round 2 disagreed on the same claim, since the criterion defines no
partial outcome, the author proposed not reproduced, and a third round agreed.
The paper reports high-frequency oscillations (HFOs) in the lateral septum
(LS) of rats, their relation to LS firing and to CA1 ripples across sleep and
waking, LS correlations before, during and after behaviour, which features of
ripples predict LS firing, optogenetic experiments and a network model. The
dataset counts, the HFOs in each animal and their count, participation and
phase locking, HFO duration and frequency against ripples, the link between
amplitude and frequency, confinement to LS, the excess correlations and their
compression, the rise in LS rates after behaviour, HFO rates by state, the
lag and coupling with CA1 ripples, ripple-triggered firing, phase coherence,
and the prediction of LS firing from CA1 spikes, state and duration were
tested on events detected anew, as the files hold none, with `hpc` taken as
CA1. Depth within LS and travelling waves are blocked as
`metadata_insufficient`, the optogenetic HFOs and the CA1 depth of neurons as
`data_missing`, replay, seqNMF and the content-independent comparison as
`methods_underspecified`, and the model and two per-session claims, which have
7 and 4 recordings against 53 because this attempt's events hold few LS
spikes, as `other`. Some outcomes rest on weak ground: the event count of
`fig1c-event-count` matches at 31,984 against 29,955 but is probably a
coincidence, as DT7 contributes most events and the count depends on the
channel; the two `fig4b` claims rest on 106 pairs in 10 recordings against
7,172 in 53 sessions; the `fig7e` outcomes come largely from counting spikes
from ripple start to stop, and with a fixed +-25 ms window the CA1-spike and
duration values are 24.7% and 17.8%; and the tolerances of
`fig1f-shorter-than-ripples` are the paper's SDs, which makes them wide.
After round 1 the HFO analyses were repeated on the LS channel re-referenced
within its shank, and apart from the share of events on the same sample as a
ripple no result moved towards the paper. The author used the
author manuscript in PubMed Central (PMC6952543), whose supplementary figures
were not available.

The dandiset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is
a contributor). The files hold no detected LS HFOs or hippocampal ripples,
nor the detection channels and parameters, which the Methods say are stored
with each event structure, so every analysis of events has to detect them
anew and the channels cannot be matched to the paper's. In this attempt's
detection 35% of LS HFOs within 50 ms of a CA1 ripple fall on the same 0.8 ms
sample as the ripple (71% in DT8, 62% in DT2, 7% in DT9), and the CA1-LS
phase difference is consistent even at random times (median phase-locking
value 0.134 against about 0.021 for random phases); re-referencing the LS
channel lowers the same-sample share to 4.1%, which points to a signal
common to the LS and hippocampal channels, such as the reference, which the
files do not document. The units carry no waveforms, no channel and no
quality metric, so the CA1 depth of each neuron cannot be estimated and
single units cannot be told from multi-unit clusters; 11 units fire above 50
Hz on average, and wide-band data are in 27 of the 98 files, with 1579 of
2778 hippocampal units having none. Electrode x, y and z are NaN in every
file, and neither the probe geometry and its orientation nor the relative
depth of each recording within LS is given. The 10 files with `ca3`
electrodes hold no CA1 channel, which the paper's CA3 recordings used to
detect ripples, and the paper reports 25 CA3 and LS recordings against 10
here. Other findings: nine files store units without a location column, so
their 268 units cannot be assigned to a region; `hpc` does not say whether a
site is in CA1, and four DT7 files label all electrodes `unknown`; the two
rats of the optogenetic experiments are not in the dandiset; 25 units in 10
files have spike times out of order (1 to 2782 inversions each); the paper's
Key Resources point to a repository that holds only the Figure 8 model and
the code of the 2018 paper; and the paper gives the HFO band as both 120-180
and 120-200 Hz and cites wrong figure numbers in its Methods. Spikes, LFP,
sleep states and trials are consistent with one clock, and no recording is
deposited twice.

The run took about 18 minutes against the 10-minute aim, as loading each
file's chunk index takes about 33 s, and the date rolled over during the run,
so the given date was kept. Untracked files in the repository root, which the
author took to be sandbox placeholders, were left alone. The author's points
on the protocol: no guidance for a dandiset that lacks the intermediate
products the results depend on; a paper's stated SD used as tolerance, which
gives wide bounds; no threshold for too few units under a claim's own rule;
clock-check examples that do not fit continuous sleep recordings; an `inputs`
field framed around data, used here for code read only for parameters; no
block reason for a model claim; no rule on whether `measured` should use one
reading for all quantities; a step that assumes linked code exists; a
two-part criterion with no partial outcome; a runtime aim that a 1.5 TB
dandiset cannot meet; and a date that rolled over during the run.
