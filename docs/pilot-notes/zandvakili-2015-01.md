# zandvakili-2015, Zandvakili et al. 2015

Five claims reproduced, one partially, seven not reproduced and nine blocked on
the CRCNS data set v1v2-1, plus four simulation claims with no published code,
which were not attempted and are blocked as `other`. Round 1 disagreed with
three outcomes, the record took its outcome on all three, and round 2 agreed
with every outcome but found that the partial outcome of
`fig5b-intra-areal-zero-lag` did not follow from the assumed test; the change
to not reproduced was proposed, and a third round, on that claim alone, agreed.
The paper, Zandvakili and Kohn, "Coordinated Neuronal Activity Enhances
Corticocortical Communication" in Neuron, records V1 with a Utah array and V2
with tetrodes in anesthetized macaques, finds narrow V1-V2 CCG peaks at a
minority of V2 sites, and shows with a divergence measure that V1 population
coordination is stronger in the few milliseconds before spikes of middle-layer
V2 neurons. The claims were written from the text of the version of record and
its supplement, as the PDF pages could not be rendered, and the paper links no
analysis code. Reproduced are the broad V1-V2 CCG peaks (31 of 31 sites), the
higher divergence before middle-layer V2 spikes at all six jitter windows, its
excess over shuffled data, the elevation on both sides of the spike at 1280 ms
and the elevation before spikes of V2 neurons with and without a V1 partner.
`fig7d-time-course` is partial: the largest difference is 2.5 to 3.5 ms before
the spike at every window, but epochs after the spike or far before it are also
significant. Not reproduced are the fraction of sites with a narrow peak (16 of
31, 0.516 against 0.206 +/- 0.021), the fraction of pairs (0.0105 against 0.003
or 0.00355), the V1-V2 peak offset (median 2.0 ms against 2.8 +/- 0.28, though
it is positive and significant), the zero offset within areas (on the assumed
Wilcoxon test, V1-V1 p = 0.016), the efficacy (median 0.324% against 0.39 +/-
0.039), the threefold ratio (about 1.9) and the absence of an effect after V2
spikes (raised at 80 ms). The spike times are in 1 ms bins where the paper used
0.1 ms, which limits the offset and width measures. The depth, layer-group,
single-unit and receptive field claims are blocked. The author's first run gave
5 reproduced, 3 partially, 5 not reproduced and 13 blocked; the author asked a
reader nothing, so the answer and author-answers runs changed nothing. In reply
to round 1 the three outcomes moved, the simulation claims went from
`not_runnable` to `other`, and a null check of the bootstrap p-values, the time
course and the partner split under every reading, four more shuffle
realizations and a check of the RF row mapping were added. Round 2 found that
the record said the deposited sessions caused the excess of narrow-peak sites
and that the paired bootstrap was near its nominal level; both were corrected.
The run for the third revision found its changes already made by an earlier run
of the same step and changed nothing. The author's run took about 1 h 40 min
(16:25 to 18:04 UTC), and the notebook ran in 12.5 minutes at first, 26 minutes
after round 1 and 1379 s after round 2.

The data set holds no V2 recording depth, penetration identity, unit SNR or
waveforms, so the paper's layer groups, the depth of the narrow-peak sites, its
offset-RF group and its single-unit analyses cannot be repeated; 7 of the
paper's claims on the recordings are blocked for this. It holds 5 sessions in 3
animals of the paper's recordings in 7 animals (31 V2 sites of 223), and its
documentation does not say how they were chosen; a significant narrow V1-V2
peak appears at 16 of 31 sites (0.52, against 46 of 223 in the paper) and in
1.05% of V1-V2 pairs (against 0.3%), in every session, which may come from the
deposited sessions or from this attempt's method, and the data cannot separate
the two. Receptive field centres and variances are in pixels, and neither the
data set nor the paper gives the pixel-to-degree scale or the fixation point; in
four sessions each channel has fits for two eyes, with V1 RF centres a median of
244 to 266 pixels apart horizontally. The spike rasters are at 1 ms resolution,
which the description does not say. The data description lists stimulus code 7
as a 135 deg grating, where the sessions description gives 180 deg for session
105l001p16, and the responses agree with the sessions description; it gives an
average of 112.2 V1 units per session where the files hold 112.8. The clock
check passes, and no unit or session is deposited twice. Three questions are
put to the paper's authors: which test gave the p-values for the median peak
offsets, whether the bootstrap p-values were paired or independent, and whether
the 10 ms CCG jitter window was used for all significance tests.

The author's points on the protocol: a reading of the claims file (one 1 ms bin
centred 2.5 ms before the spike) cannot be formed from 1 ms data, and the bins
that bracket it were run; there is no blocking reason for simulations left
undone for lack of time; the claims file leaves the second jitter window
unnamed, and 25 ms was chosen; a claim of absence is judged on the paper's
test, but the paper names none, so one test was adopted as an assumption; the
fig7d criterion is ambiguous about whether distant epochs are judged per window
or across windows; and `entry.py check` needs the dataset version in the code,
which for CRCNS is `unversioned`.
