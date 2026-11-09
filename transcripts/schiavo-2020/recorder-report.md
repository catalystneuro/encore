I wrote `docs/pilot-notes/000249-schiavo-2020-01.md` and changed no other file. The untracked dotfiles and folders at the repository root were there before this run, and I left them alone. Nothing is committed.

# 000249, Schiavo et al. 2020

No claims reproduced, none partially, none not reproduced and 32 blocked on
the dataset, with one more blocked that also needs outside data. It pins
version 0.230423.1416. The paper, Schiavo, Valtcheva, Bair-Marshall, Song,
Martin and Froemke in Nature, studies maternal behaviour in mouse auditory
cortex: pup retrieval by dams and by virgin females cohoused with them, two-photon
imaging of responses to pup calls whose inter-syllable intervals (ISIs) were
varied, whole-cell recordings of excitation and inhibition, and oxytocin's
role in the plasticity. The claims were written from the NIH author manuscript
in PubMed Central (PMC7677212), not the version of record; the paper's code and
data DOI (10.35092/yhjc.c.5037737) does not resolve, no analysis code was
found, and the claims check made 20 corrections before the attempt. The
dandiset holds only the two-photon imaging, so the 20 imaging claims and
`fig3-retrieval-onset-range` are blocked as `metadata_insufficient`, and
`fig1a-isi-distribution`, the behaviour claims and
`ed4d-response-tracks-isi-probability` as `data_missing`. The link claim
`subject-group-link` is partially reproduced: every subject has a figshare
item titled with its mouse id (54 of 54) and 7 of the 9 group counts match the
paper, but no file says which call each trial played. Ten claims use the
whole-cell, slice and operant recordings of the figshare collection the
dandiset links (doi:10.6084/m9.figshare.c.5043830.v6) and are left out of the
counts: `ed9b-oxytocin-enhances-spiking` is reproduced and
`fig1g-ipsc-depress-faster` not reproduced, each resting on an assumption;
`fig1i-operant-prototypes` and `ed5b-press-count-unchanged` are blocked as
`methods_underspecified`, as the readings disagree; `ed6h-dams-evs-epsc-similar`
is blocked as `metadata_insufficient`; and the five in vivo whole-cell claims
are blocked as `other`. The author's first run had three of those five as not
reproduced, `fig2h-epsc-enhanced-ev` as partially reproduced and
`fig2i-ipsc-weaker-nv` as blocked as `methods_underspecified`. Round 1 found
that the measure failed its own positive control (only 1 of 12 EV and 2 of 14
NV EPSC cells showed a call-evoked current of the expected sign) and that the
pre-call window gave the same experienced against naive differences, and the
author found the call onset fell a median 193 ms late in 51 of 83 files, fixed
it, and moved the five claims to blocked; its points also led to the groups
read from the figshare titles, per-cell traces aligned to onset, the
inclusion-rule counts, the slice pulse times checked against the stimulus
artefacts (91.8% within 1 ms) and the oxytocin labels printed. Round 2 agreed
with all 44 outcomes, so there was no third round; it found wording the
numbers did not support, among them "no current that follows the calls" where
13 of 110 files show a sweep-locked deflection against 5.5 expected, an
out-of-date imaging sentence in all 20 imaging notes and a call rate recorded
as a metadata error where 10.24 s is 0.098 Hz, which were corrected. No
questions were put to a reader, so the answer run and the following author
run changed nothing. The author's run took about 33 minutes (03:32 to 04:05
UTC) and nothing failed; in the last revision a run failed once on a dropped
figshare connection and the downloads now retry. The notebook ran in 89 s at
first and in 356 s in the last run.

The NWB files hold only raw, unaligned two-photon movies, with no ROIs or
fluorescence traces, no stimulus times, no trial tables and no record of which
call each trial played, so none of the paper's 20 imaging findings can be
tested; the movies recur every 40 frames (10.24 s, 0.098 Hz) and in 31 of 38
three-call movies folding at three trial periods stands above two and four, as
a fixed cycle of three calls would, though the Methods say the order was
pseudorandom and no file says which call sits at which position. The pup
retrieval, latency and y-maze data and the vocalization recordings are in
neither the dandiset nor the figshare collection. Groups are given only in
free-text experiment descriptions, the indicator and location fields are
"unknown" in every file, and the start of cohousing is not recorded. Three
recordings (sessions of 2018-03-08 named plus24hrs_postexp1) are deposited
under both sub-NV58 and sub-NV63 with the same start times and frames, and
EV56 and EV62 are described as NV56 and NV62 in their own experiment
descriptions. In the in vivo whole-cell recordings the current almost never
follows the played calls: the evoked measure is in the expected direction at
p < 0.05 in 2 of 39 cell recordings (3 of 39 before the call), 3 of the 13
files with a sweep-locked deflection, from two cells (190326_e1 and
190313_e2), carry an inward current from about 0.4 s after onset, the Methods'
inclusion rule keeps at most 1 of 39, and the experienced recordings are about
twice as noisy as the naive ones (baseline s.d. 11.4 against 5.3 pA). The
microphone channel shows the morph ISIs as 125, 275 and 575 ms with the
prototype, as the figure legends say, played in a fixed order, where the
Methods give 125, 225 and 575 ms. The whole-cell spreadsheet of experienced
females does not say which cells come from dams; file 19424013 is listed at
-70 mV but carries about +560 pA throughout; two listed files (193260007 and
19o11005) are not deposited; and the operant touch-time files print five
significant digits, so after 1000 s of a session they step by 0.1 s. Two
questions are put to the paper's authors: which gap between touch samples ends
a lever press and which sessions were compared, and how a significant PSC was
defined for the inclusion rule, how many of the "largest 5-10 evoked trials"
were averaged and how ranked, and which Dunn comparison family Extended Data
Fig. 9b used.

The author's points on the protocol: the claims file says to block when
readings disagree while step 1.6 allows adopting the best-supported reading as
an assumption; the clock check does not fit files with no stimulus times, so
the microphone channel was used to time the calls; the protocol has no rule
for a measure taken exactly as the Methods define it that turns out to track
noise; and `docs/archives.md` has no figshare section, and its ABF files cannot
be streamed with the usual tools.
