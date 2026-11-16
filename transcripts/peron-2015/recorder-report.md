# peron-2015, Peron et al. 2015

One claim reproduced, none partially, one not reproduced and 40 blocked, 22
for missing data and 18 for insufficient metadata; the validation of the event
detector, which uses data from elsewhere, is also blocked, as methods
underspecified, and is left out of those counts, and no outcome rests on an
assumption. The first verification round agreed with 42 of the 43 outcomes and
held `results-whisking-amplitude` partially reproduced, and the second agreed
with all 43, withdrawing that disagreement; nothing was proposed after the
second, so there was no third round. CRCNS does not version data sets, so the
version is recorded as unversioned with the data set's DOI (10.6080/K0TB14TN),
and the MD5 of each file read matches the data set's `checksums.md5`; the
registry's CRCNS target list gives the DOI as 10.6080/K000001D. The paper,
Peron, Freeman, Iyer, Guo and Svoboda in Neuron (86:783-799), images L1 to L3
of vibrissal S1 in subvolumes of three planes 15 um apart at 7 Hz in eight
mice performing a pole localization task with one spared whisker, and reports
a core data set of 82,732 L2/3 excitatory neurons, 777 L1 neurons, 3,806 L2/3
GABAergic neurons and 2,469 L5 apical dendrites, that about 40% of neurons are
task related, that in the principal column L2/3 neurons encode touch and
whisking about equally while whisking dominates in surround columns, that touch
neurons are concentrated in the principal column while whisking neurons are
spread uniformly and intermingled, that individual representations stabilize
during learning while ensemble discrimination stays flat, and that touch
neurons are directionally tuned, with a map of direction along the row likely
inherited from L4 and distinct neurons responding to passive deflection under
anesthesia; the data set holds per-session MATLAB files with ROI masks, dF/F
and whisker and trial variables, and archives of registered imaging TIFFs. The
claims were written from the version of record with its Supplemental
Information as PyMuPDF text, as the PDF could not be rendered, so numbers
printed only inside Figures 3, 6 and 8 were not read; the paper links no code,
and the claims check corrected the third mouse's spared whisker in the opening
comment (C2), the cell count of `discussion-principal-exclusive-classes`
(13,308, not the neuropil's 14,165) and the tolerance of
`fig3d-population-encoding` (2.5 widened to 5 points), and named the gap
between the core counts (89,784 ROIs) and Table S1 (108,374), for 43 claims.
Only two claims, both behavioural, could be tested. Reproduced is
`results-trials-per-session` (290.2 pooled and 272.5 as the mean of per-mouse
means, against 245 +/- 71), weak evidence as the five deposited sessions may
not represent the paper's imaging sessions. Not reproduced is
results-whisking-amplitude: the three readings the criterion lists give 74.7
degrees (per-trial range), 29.0 (range over the sample epoch) and 26.9 (peak
Hilbert amplitude) against 55.5 +/- 13.3 (42.2 to 68.8); removing only tracking
errors brings the range to 69.2, 0.4 above the bound, a 21-sample running
median brings it inside (68.6) but also cuts real whisk peaks, measures the
criterion does not list fall inside (twice the peak Hilbert amplitude 53.7,
the 1st to 99th percentile range 49.2), and the untested part, movements larger
than about 20 degrees, holds. Blocked are the 18 comparisons between layers,
cell classes and columns, as no ROI carries such a label (shared method M6 of
the claims file) and no calcium events are deposited, and, for missing data,
Table S1's ROI counts (26,761 of 108,374 ROIs are in the data set), the
GABAergic fraction, the learning claims of Figures 6 and S7, the anesthetized
claims of Figure 8, the L4 axon and neuropil claims, training, trimming and the
L5 soma and dendrite pairs. The author's first run had the same outcomes. The
author asked no questions of a reader, so the answer and author-answers runs
changed nothing. Round 1 held that reading (a) was inflated by tracking errors
at +/-90 degrees and reading (c) by filter edge effects, that the label fields
were never printed, that the raw TIFFs offered a route for
`figs3d-neuropil-correction`, that one session's clock was unconfirmed and that
the five sessions may not be representative; in reply error masks and an
edge-trimmed Hilbert peak were added, which left the outcome as it was, the
label fields and trial ids were printed, the caveats were written in, and a
question on the length of the sample epoch (1 s in the claims file's opening
comment, 1 to 2 s in the Figure 1C legend) went to `questions/peron-2015.yaml`;
`methods-event-detection` stayed methods underspecified where the verifier
would have put data missing, which round 2 accepted. Round 2 asked for reading
(a) without tracking jumps of three samples or more and found sentences the
outputs did not support, among them "71.7 to 74.1", which left out 70.3, and
"45 TIFFs and nothing else"; in reply jump masks and running medians were run
(69.2 to 70.1 for the cleanings that remove only errors) and the sentences
were corrected. The author's run took about 20 min; the notebook ran in 29 s
at first, with peak memory 0.86 GB, 100 s after the author-answers run, 26 s
after round 1 and 33 s after round 2. One run failed, as a regex that stripped
bold text also broke a `**` dict unpacking in a code cell, and was fixed.

The data set holds 5 imaging sessions from 3 of the paper's 8 volume-imaging
mice (an197522, an229717, an229719), with 20% to 72% of their Table S1 ROIs
(26,761 of 108,374 for all eight mice), although the paper says the data set
includes the imaging data of Table S1; the other five mice, among them the
Gad2 mouse with labelled GABAergic neurons, the imaging during learning, the L4
axon mice, the anesthetized mice, the L5 soma and dendrite pairs, the training
sessions and the high-resolution reference stacks are not in it. No ROI carries
a layer, cell-class or barrel-column label and no plane a depth or position
relative to the others: idStrs repeats the ROI id, idStrsDetailed is empty and
the ROI ids number planes, and the laminar boundaries the description says
were drawn in the reference stack are not deposited. The description lists raw
fluorescence, extracted calcium events and multi-session vol_xxx files, but the
session files hold only dF/F (dffTSA) and whisker variables and no vol_xxx file
exists. The whisker angle holds tracking errors the description does not
mention: samples at the tracker's +/-90 degree limit for one or two samples,
jumps to a distant value for three samples or more (in an229717 a step over 30
degrees that returns within 25 samples in 116 of 183 trials, its 99.9th
percentile step 34.5 degrees against 4.5 to 7.0 in the other sessions), and
protractions past 90 degrees that wrap to the other sign; the largest
per-trial range, 179.8 degrees, spans these limits. In an197522 on 2013-03-10
the dF/F response to the first touch is not larger with the true touch times
than with times shifted by 3 s (3 of 9 subvolumes; median 0.0009 against
0.0083 dF/F), so that session's imaging could not be shown to share the trial
clock, while in the other four sessions the true alignment gives the largest
response in 21 of 25 subvolumes; no tested claim uses dF/F. One subvolume
(an197522, 2013-03-08, dffTSA 10) is a single plane at 29 Hz, not three planes
at 7 Hz, and many 7 Hz subvolumes have ROIs on only one or two of their planes,
neither described. The event series structure is named eventSeriesArrayHash,
not eventSeriesHash, one file is named an229717_2013_12_01_sesssion.mat, and
the description cites the paper with a placeholder. Questions are put to the
paper's authors: which measure, epoch and band gave the whisking amplitude of
55.5 +/- 13.3 degrees and how tracking errors were handled, and which Chen et
al. (2013) recordings, degradation, Savitzky-Golay window and matching window
the event detector's validation used.

The author's points on the protocol: for a per-mouse count claim when most of
each mouse's sessions are not deposited, neither testing what is there nor
`data_missing` clearly fits, so `data_missing` was chosen with the counts in
the notes; the CRCNS imaging tarballs (165 GB) can be listed only by streaming
through them, which the guide does not cover, so one was listed in full while
preparing; `entry.py check` requires the string `unversioned` in the notebook
or helper, which `docs/archives.md` does not say; and it is unclear where the
numbers of a blocked claim belong, so they went into an untagged data-check
cell.

---

None of the paper's main findings could be tested in this data. The map of touch and whisking coding across layers, cell types and barrel columns, the concentration of touch neurons in the principal column, the stability of representations during learning and the map of directional tuning all need layer, cell-type or column labels that the data set does not carry. It also holds only a few sessions from three of the paper's eight mice, with no imaging during learning or under anesthesia. Of two minor behavioural details, the number of trials per session matched, while whisking amplitude fell outside the paper's range under every measure the claim names, a measure the paper does not define.
