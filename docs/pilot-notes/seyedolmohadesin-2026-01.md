# seyedolmohadesin-2026, Seyedolmohadesin et al. 2026

Twenty-one claims reproduced on the dandiset, none partially, three not
reproduced and four blocked, two for missing data and two because the
methods are underspecified; of the claims that also use the published
connectomes, three reproduced, one was not reproduced and one is blocked,
and the link claim `connectome-link`, which the author added to match the
traces' neuron names to the connectomes, reproduced and is counted apart.
The first verification round agreed with 33 of the 34 outcomes as they
stood and gave `fig2-awa-awb-nociceptive` as not reproduced, which the
author adopted; the second agreed with all 34, and nothing was proposed
after it, so there was no third round. It pins version 0.260910.1747. The
paper, Seyedolmohadesin et al., "Whole-brain chemosensory responses of both
C. elegans sexes" (Current Biology 36, 4803-4816), images the head neurons
of 22 hermaphrodites and 25 males of the NeuroPAL GCaMP6s strain OH16230
while ten chemical cues and controls are delivered to the nose, and reports
that most head neurons, and the sensory neurons most of all, respond
differently in the two sexes, that functional connectivity is similar
between the sexes, and that functional and synaptic dimorphisms are
distinct. The claims were written from the version of record (text
extracted from a PDF supplied by a person, no figure rendered, without Data
S1 to S4) and from the paper's code at commit b0dbdbf, which lacks the
files it reads: the class-to-layer file, the spreadsheet of time ranges and
ganglia to ignore, the identification confidences and the connectome table;
the connectomes were rebuilt from the supplements of Cook et al. 2019 and
Witvliet et al. 2021. Reproduced are, among others, the animal counts (22
and 25), the responsive and dimorphic class counts of Figure 5B (86 and 83
under the Methods' exclusion, against 84 and 80), all eight per-layer
counts, the sensory layer as the most dimorphic, the Figure 2 and 3
examples for AWA, AWB, ASH, BAG, I2, ADF and M2, the similar functional
connectivity of the sexes (R2 = 0.806 over 5995 subclass pairs), and the
absence of a relation between functional and synaptic dimorphism (slope p =
0.641 with Cook's counts, 0.905 with sections). Not reproduced are
`sensory-dimorphic-and-monomorphic` (21 and 20 of 24 sensory classes
against at least 22), `fig3a-aser-salt-concentration` (low salt p = 0.055
and 0.059), `fig2-awa-awb-nociceptive` (AWA does not respond to CuSO4,
smallest p 0.077) and `connectome-normalization-sem` (no reading puts all
four values within tolerance; the mean SEM before normalization with
sections is 1.143 against 1.14, but it rises after normalization).
`figs2e-no-order-effect`, `figs3fg-state-dependence-interneurons` and
`fig4g-functional-top-not-synaptic` are blocked because their method
readings disagree: an ANOVA finds an order effect under one exclusion only,
the interneurons are highest in 36 of 48 motor-state combinations at q <
0.05, and Figure 4G holds with Cook's synapse counts and not with his EM
sections under one order of exclusions. `tail-unresponsive` and
`figs1-behavior` are blocked for missing data. The fig5b-responsive-classes
count is weakly diagnostic: with 32 uncorrected tests per class, about 72 of
89 classes could be expected by chance. The author's first run gave 24
reproduced, 2 partially, 3 not reproduced and 5 blocked, counting the link
claim. Round 1 found that only the author's own layer assignment had been
run, that the AVA motor state was not fitted to its baseline, that the
sections' SEM match was not drawn out, that no listing showed whether a tail
trace table exists, that the band-pass helper had not been compared with the
code and that the link used only Cook's sections; in reply the layers were
read from the column groups of Figure 3A, which moved `fig5b-layer-counts`
from partially reproduced to reproduced and removed the assumption from four
claims, a baseline fit was added (48 combinations), every group of two files
was listed, the code's filter was copied in and matched the helper exactly,
and both Cook forms were run with known connections printed from every
sheet. Round 2 found sentences the outputs did not support (a RESPONSIVE p
bound of 9.2e-09 where ASER's is 3.7e-06, Figure 4G called blocked whichever
form is taken, the zero tracked positions generalised from one sampled file,
the male counts matrix given 185 names for 165, and the README's loading
time), all corrected; the name colours of Figures 3A and 3B were then read
from the PDF and give exactly the Figure 5B counts with the Figure 3A
layers. The author asked a reader nothing, so the answer and author-answers
runs changed nothing. The author's run took about 2 h 40 min, of which an
hour was lost when `tools/entry.py check` hung on a regular expression that
backtracks on a 30-number list literal; a first survey of a file timed out
after 10 minutes, and `tools/entry.py lock` wrote a `python:` field that the
schema rejects, which was deleted after each lock. The notebook ran in 363 s
at first, 206 s after the author-answers run, 394 s after round 1 and 594 s
at the end.

Files sub-20220403-h3 and sub-20220403-m3 hold the same 382-row trace
table, h3's 187 traces followed by m3's 195, with nothing saying which rows
belong to which animal; it was split where its first label recurs, and each
block matches the other animals when read with its own file's stimulus order
(mean r 0.58 and 0.54, against 0.32 and 0.31). The trace tables hold head
neurons only: the NeuroPAL segmentations identify tail neurons, which the
paper says were recorded, but none has a trace, and the tracked ROIs that
would let them be extracted from the raw volumes are (0, 0, 0) in 99.75% of
the 44,677,593 ROIs of the 47 files, with no coordinate above 2 and all
284,479 tail-neuron ROIs zero. The drop-test behaviour of Figure S1 is not
in the dandiset. The identification confidences the paper's code uses to
keep only confident identities are not in it, and the code's other inputs
(the connectome table prepared by S.J. Cook, neuron_classes.json and the
spreadsheet of time ranges and ganglia to ignore) are not public. The
subject sex is "O" in all 47 files, given only in the subject description
and id, and the strain field is "[]" though the paper names OH16230. The
StimulusInfo timestamps are labelled seconds but hold frame numbers (up to
4980), and the stimulus annotations lie 1 to 3 frames after the fixed onset
frames the code uses. The traces carry no unit and no description beyond
"list of reading at each frame", and blocks of frames are blank (the first
96 frames in 13 recordings, other ranges of 29 to 514 frames in seven)
without a note of why. The traces have 4979 frames against 4981 image
volumes, the stated rate is 2.66 volumes/s where the Methods give 2.67, and
the traces cover 189 distinct sex-shared neuron names where the paper says
196. Cook's two forms of the White connectome differ: the counts give no
AVAL synapse onto VA05, VA07, VA08 or VA09 where the sections give 7 each,
which the supplements' legends explain as connections added by
extrapolation. Questions are put to the paper's authors: which AVA trace,
change measure and exponential fit define the motor state; which form of the
Cook connectomes went into Figure 4 and over which values the 95% quantile
is taken; and which test and neurons support the absence of an order effect
in Figure S2E.

The author's points on the protocol: the claims file blocks a claim when
method readings disagree while the protocol allows adopting the
best-supported reading, and the claims file was followed; it does not say how
readings the author adds combine with the claims file's, and all were
required to agree; there is no code for a claim not yet attempted within the
time limit; `tools/entry.py check` hung for an hour on a list literal and
`lock` writes a field the schema rejects; the handover drops markdown cells
that start with `**Result:` without saying the conclusion must be in its own
cell; and for a criterion judged only as reproduced or not, partially
reproduced was first used as the protocol defines it.
