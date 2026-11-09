I wrote the notes to `docs/pilot-notes/001174-martel-2025-01.md` and changed no other file. Nothing is committed. The repository root has other untracked files (`.bashrc`, `.idea`, `scripts` and others) that I did not create; the first revision report mentions them too. I left them alone, so check them before the workflow commits.

# 001174, Martel et al. 2025

Nine claims reproduced, none partially, one not reproduced and ten blocked on
the dataset, with two more blocked that are on data elsewhere; the link claim
`zenodo-descriptors-link` is not reproduced. The first verification round
agreed with all 23 outcomes and the second with all 23, so there was no third
round. It pins version 0.250331.2218, the version the paper cites and the only
published one; the draft has the same 45 assets with the same sizes. The paper,
Martel, Pittard, Devergnas, Risk, Nassi, Yu, Downer, Wichmann and Galvan in
iScience, images four rhesus macaques (F, Q, U and V) with a nVista3 miniscope
through a GRIN lens in SMA and a prism in M1, compares event rate, IEI CV and
amplitude of CNMFe cells between spontaneous imaging and an arm-reaching task
(Figure 1), classifies cells by their response to target and movement onset
(Figure 2 and Figure S1), measures pairwise synchrony with a Z-Jaccard index
(Figure 3) and detects sequences of activity (Figure 4). The claims were
written from the version of record in Europe PMC (PMC12192352) without its
supplement, and from the paper's code on Zenodo, whose parameter values for
the sequence detection are not recorded. The dandiset gives no cross-session
cell identity, so each cell's first occurrence was taken from the paper's
Zenodo descriptors table; the link claim finds the cells match (565 of 626
table rows matched, 93.8% of matched cells with both centroid coordinates
within 3 pixels) but not their descriptors, only 86 of 313 cells (27.5%)
having rate and amplitude within 1% in every condition, below the 50% the
criterion asks. `cell-counts` reproduces under reading (i), Q 129, F 60, U SMA
63, U M1 37 and V 23, though these count the rows of the paper's own table;
under reading (ii), the only count the dandiset gives by itself, only V is
within tolerance. The Figure 1 claims were run only under reading D (i), a
cell's value in its first session. `fig1d-rate-no-change` (smallest
uncorrected p 0.0666) and `fig1e-ieicv-no-change` (0.0841) reproduce,
`fig1f-amplitude-u-sma-spont-higher` reproduces (p = 0.0017, q = 0.0204 and
0.0068; the paper gives p = 0.032) and `fig1d-rate-m1-above-sma-u` reproduces
(p below 1e-5 in both conditions). `fig1f-amplitude-m1-above-sma-u-task` is not
reproduced, p = 0.0988 uncorrected and q = 0.1976 against the paper's p =
0.03, while the same test on the paper's per-cell table gives p = 0.0138, so
the gap comes from the dandiset's event amplitudes; without U SMA 2023-03-07
and 2023-03-14 it gives p = 0.041 and q = 0.082. The three Figure 3 claims
reproduce: every site and condition has sessions with pairs of |Z-Jaccard| >
1.96 (542 of 6089 defined pairs, eight SMA session-conditions at or below
0.05), 4 U SMA and all 4 U M1 sessions show no significant correlation of
Z-Jaccard with centroid distance under Pearson in either condition, and the
change between conditions gives SMA p = 0.1514 and M1 p = 0.2188.
`fig4d-sequence-measures-vary` reproduces on a criterion met by any measure
that is not constant. `fig4a-example-sequences-q` and
`fig4b-example-three-segments-q` are blocked as `methods_underspecified`,
departing from the criterion's rule, which gives not reproduced when every
reading fails: under 32 settings of the Python port of identify_sequences.m
the best puts 21.4% of the 56 slices of the paper's Figure 4D table within 10%
of the paper's own counts, and in the two slices whose events match the
paper's table no setting gives the paper's 7 and 9, so the readings of method
S do not include the procedure behind the paper's numbers.
`fig4c-sequence-cells-not-clustered` is blocked as `methods_underspecified`,
the pooled test of reading (ii) finding sequence pairs closer (medians 284 to
296 against 320 um) where the within-session test, chosen after the first
verification, finds no session that differs. `cells-tracked-18pct` is blocked
as `metadata_insufficient`, the data bounding the tracked fraction between
14.1% and 28.1%, the six Figure 2 and Figure S1 claims as `data_missing`, and
the two histology claims, on whole-slide scans on Zenodo, as `other`, since
judging them needs an anatomist's reading. The author's first run gave fig4a
and fig4b as not reproduced and the histology claims as blocked as
`not_runnable`. The author asked a reader no questions, so the answer run and
the following author run changed nothing. Round 1 agreed with every outcome,
gave `other` for the histology, and asked for the cell ids of all 45 files to
be printed, the two far-off U SMA sessions to be examined and the Figure 1
tests rerun without them, the Zenodo aligned-activity record to be opened, a
sweep of the sequence parameters against the Figure 4D table, and fig4c's
reading (ii) to be tested within sessions; in reply fig4a and fig4b were
blocked, the histology reason changed, the checks were added and a question
put to a reader on whether method S should name other readings. Round 2 agreed
with every outcome, asked that the departure from the criterion's rule be
listed as a deviation and that a reader be asked why method Z run on the
paper's own z-scored windows finds 20 modulated Q SMA cells against the
paper's 43, and found sentences the outputs did not support (four sessions
where the Figure 4D table has fewer cells than the dandiset in three, a
summary leaving out V 2023-03-16, "most of the gap" without saying for which
measure, events said to be lost when put on the frame grid, and a run time of
about twenty-two minutes), which were corrected; the sequences notebook now
downloads identify_sequences.m and prints its double-counting lines, MATLAB and
Octave not being installed to run them. The author's run took from 06:48 to
08:25 UTC, a correlation bug and slow sequence code being fixed during
development. The two notebooks ran in about 1.5 and 13.5 minutes at first, 93
s and 805 s after the answer, 81 s and 1301 s after round 1, and the sequences
notebook in 915 s after round 2.

The dandiset holds no TTL or trial data and no raw traces, so the Figure 2 and
Figure S1 analyses, which align raw traces to TTL-marked target and movement
onsets, cannot be run, and the paper's Zenodo table of aligned activity holds
its z-scored windows, not the event times. No cross-session cell identity is
deposited: every file gives its cells ids 0 to n-1, the Zenodo table gives a
global id only at a cell's first session, and the spreadsheet the code reads
for identity (Metadata_all_monkeys.xlsx) is not public. The dandiset's events
differ from the paper's per-cell table: event rates agree within 1% for only
40.9% of cell-conditions and the table's are a median 4.2% higher, one-frame
inter-event intervals are rarer in the dandiset (3.9% against 11.9% of cells
with a one-frame median IEI), and U SMA 2023-03-07 and 2023-03-14 differ by
factors of 0.04 to 20, with far fewer spontaneous events and a higher
amplitude in every cell, which is not a swap of conditions and looks like a
different event detection; with the dandiset's amplitudes the U task M1
against SMA difference is not significant (p = 0.099), with the table's it is
(p = 0.014). The trace in RoiResponseSeries is the CNMFe denoised trace,
described only as "Fluorescence data associated with spatial footprints",
EventAmplitude holds the deconvolved events as a dense frame by cell array
without saying that zero means no event, and ImagingPlane indicator and
location are "N/A" in every file. U SMA 2023-03-14 is sampled at 20 Hz where
the Methods give 10 Hz, the dandiset has arm-reaching files for monkey V, which
the paper's Jaccard and sequence code treat as task while the text says only Q
and U performed the task, and the spontaneous file of Q's 2022-09-15 session
is named sub-Q/sub-Q_ophys.nwb, without a session label. The paper's tables
leave out cells the dandiset holds (17, 11, 10 and 13 cells in the Jaccard
table and 17, 11, 11 and 13 in the Figure 4D table, against 18, 13, 11 and 14
accepted cells in Q 2022-10-03, Q 2022-12-01, V 2023-03-09 and V 2023-03-16),
without saying which or why, and the Figure 4D table gives n.a. for the first
spontaneous 10 min of Q 2022-09-15 and 13 sequences for the second, while the
deposited spontaneous file lasts 10.05 min. The paper's Jaccard table dates
one F session "20-Feb-23", where F was imaged in 2024. The paper's code
differs from its description: the double-counting step of identify_sequences.m
writes 2 into a logical array, so its test for 2 never succeeds and it removes
no repetition, and 1_JaccardIndexAnalysisAllSessions.R runs the SMA sessions
with 10 shifts where the Methods give 1000, which gives p = 0.077 on the
dandiset against 0.151 with 1000. Questions are put to the paper's authors:
which values were passed to identify_sequences.m for Figure 4 and what the
0.05 s of the Results applies to; and which distributions were compared for
Figure 4C and Figure S2, and with which test.

The author's points on the protocol: claims that need the cross-session
identity from Zenodo keep `data: dataset` and do not list the link claim under
`depends_on`, which the author may not edit, so they were tested with the
reliance explained in their notes; the link claim judges descriptor values
while the dependent claims need only the cells' identity, and the two were
treated separately; for fig4c the criterion says to block when readings
disagree while step 1.6 allows adopting a reading as an assumption, and the
criterion was followed; no block reason fits a visual anatomical judgement of
histology, and `not_runnable` was used at first; and the sequences notebook
exceeds the ten-minute aim because every reading the claims file lists is run,
and all were kept with the runtime recorded.
