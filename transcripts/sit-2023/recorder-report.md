I wrote `docs/pilot-notes/000483-sit-2023-01.md` and changed no other file. The `catalystneuro` field for 000483 is empty, so the second paragraph has no CatalystNeuro opening. Some untracked files are in the repo root (`.bashrc`, `.idea`, `scripts` and others); I didn't create them, and an earlier author run had already reported them. Nothing is committed.

# 000483, Sit et al. 2023

Five claims reproduced, 11 partially, six not reproduced and two blocked. The
first verification round agreed with 9 of the 16 outcomes it could judge and
the second with all 24, so there was no third round. It pins version
0.230421.2321, the only published version. The paper, Sit and Goard in Nature
Communications, images retrosplenial cortex (RSC) somata and axons from the
anterodorsal thalamic nucleus (ADN) and visual cortex with two photons in mice
head-fixed in an air-floated chamber, and reports that RSC heading cells
coregister to visual cues: a share of cells is heading selective under
controlled rotation, preferences remap coherently between contexts, and
somata fall into heading, landmark and alignment classes that differ in light
and dark and in how well they decode heading. The claims were written from the
version of record, without the Supplementary Information, and from the lab's
repository Neurotar-HD-Experiments at commit c6344f5, whose analysis classes
the attempt reimplemented in Python; the lab's HeadingDecoder at ca9842e was
used only as a named variant. 22 of the 24 claims were tested.
`fig1-free-heading-fraction` is blocked as `data_missing`, as the dandiset
holds no free-chamber recording, and `fig5k-visual-cue-only` as
`metadata_insufficient`, as its two recordings share no ROIs with any other
file and do not mark standard rotation. `fig1g-rotation-heading-fraction`
reproduces with the tuning curve centred before the Gaussian fit, an
assumption: 485 of 3179 ROIs (15.26%) pass, while the fit as the code calls
it passes 345 (10.85%), 93.6% of them in one quadrant. The test is liberal, as
synthetic untuned cells pass at 4.7% and real cells with each trial shifted
once at 5.19%, so `selection-shuffled-control` is not reproduced and about a
third of the selected cells could pass by chance. The axon light-on shape and
the rotation direction claims reproduce, the latter fragile, as by mouse only
SKKS125 passes. `figs6-arena-control` is not reproduced once the pair whose
animal-controlled file visits 6 of 60 heading bins is left out (p = 0.9).
Clustering finds the silhouette highest at k = 2, and the classes do not match
the paper's (landmark-like 7.6%, alignment-like 78.9% and heading-like 13.5%,
with all three light-on archetypes bimodal), so the Figure 5 claims built on
them are partial at best. Decoding rests on the naive Bayes decoder of the
Methods, an assumption: all tuned cells give 0.708 in light-on against 0.82,
and `fig6b-180-errors` and `fig6-heading-below-population` reproduce, the
first fragile. The author's first run gave 11 reproduced, two partially, two
not reproduced and nine blocked, the seven decoding claims as `other` because
the time ran out. The author asked a reader no questions, so the answer run
and the following author run changed nothing; that re-run took 66 minutes and
gave the same numbers. Round 1 gave no outcome for fig5k and the seven
decoding claims, which had no notebook output; it found that the selection
test passes untuned noise, that shuffling the trials afresh in every
iteration can pass no cell, that the fig5e measure gives a large V under
random peaks, that matched ROIs in fig2f do no better than random pairs, and
that figs6 rests on the 6-bin pair. In reply selection-shuffled-control moved
to not reproduced, fig2f, fig3c, fig5e, fig5f, fig5gh and fig5i to partially
reproduced and figs6 to not reproduced, a new notebook tested the decoding
claims, and questions to a reader were put during the revision. Round 2 agreed
with all 24 and found that most conclusions, Summaries and the record quoted
another run than the printed one, two statements reversed by the printed
output; the likeliest cause was multithreaded BLAS, every notebook now sets one
thread, and the re-run printed the verifier's numbers exactly, from which the
text was rewritten. It also found that the Methods' even and odd split of
resampled bins lets test bins share frames with training bins. The author's
run took about 3 hours, ending at 16:16 UTC, and nothing failed; the five
notebooks took about 69 minutes, directions.ipynb was run with nbconvert
outside `entry.py all`, and the six notebooks of the last run took 58
minutes.

The dataset holds the raw fluorescence of each ROI but no neuropil trace, dF/F
or inferred spikes, so the neuropil-corrected signals cannot be rebuilt
without reprocessing the raw video (about 695 GB), and the axon recordings
lack the Suite2P traces the paper used; every tested outcome rests on spikes
inferred here without neuropil correction. The free-chamber recordings of
Figure 1D and E (4 recordings over 3 mice, 2665 neurons) are not in it, and
the files hold 20 mice where the paper used 26. The experiment a file belongs
to is given only inside its identifier string, the session description being
"floating air cage experiment" for every file, and light-on and light-off
periods are not marked, so the code's hard-coded segments were used. The
heading is relative to "cage door dead north" with no position for the cues,
so the overrepresentation near the cue in Figure 1H cannot be judged, and in
5 of 7 head-rotation pairs the stored headings run in opposite directions in
the two conditions with neither defined. The heading and position series
state 0.1 Hz where they have one sample per imaging frame, at 10 Hz, and the
two-photon series states about 20 Hz with the same number of frames; every
imaging plane, the 24 axon recordings included, is described as "soma
recording from retrosplenial cortex", and four files of mouse SKKS089 carry
identifiers naming SKKS088. The dandiset holds 7 head-rotation pairs over 5
mice (paper 5 over 4), 35 dual-cue soma recordings (paper 36), 4 recordings in
both rotation directions over 3 mice (paper 4 over 2) and 5 animal-controlled
recordings over 4 mice (paper 7 over 3), and which recordings the paper used
is not stated. The chamber-rotation file 210526 SKKS112-PlatformRotation-002
barely rotates, with a median heading step of 0.12 degree per frame against
about 2 in the other chamber-rotation files. Removing the shared frames of the
decoding procedure lowers the light-on accuracy of all tuned cells from 0.708
to 0.532 (dF/F) and from 0.712 to 0.296 (spikes), so the paper's accuracies
may be raised in the same way. The code that aligns light-off to light-on
trials (leaveOneOutAligner) and the code for the clustering, V-tests,
decoding and statistics are not in the linked repository. Questions are put
to the paper's authors: whether the tuning curve was centred before the
Gaussian fit, how the head-rotation and chamber-rotation headings are defined
and which 5 of the 7 pairs were used, whether the pre-shuffled data of the
selection control were shifted once or afresh in every iteration, and which
decoder, on which input and with what binarization, gave Figure 6.

The author's points on the protocol: there is no blocking category for a
claim not tested in time, and `other` was used; a clock check that shifts
heading against activity cannot detect an offset in a recording that rotates
one way at constant speed, so only the files that rotate both ways were used;
the protocol does not say what to do when a criterion passes but its expected
value does not match and a null gives a larger value, as in fig2f; the
handover strips only conclusion cells that begin exactly with `**Result:`, a
format rule not written in the protocol; and the rule against numbers from
outside the notebook is unclear for archive metadata in the notes of blocked
claims, so such numbers were removed.
