I added the README row and appended the subsection to `docs/pilot-notes.md`. Nothing is committed.

The README row reads 12 reproduced, 5 partially, 3 not reproduced, 5 blocked. The author's first report gave different totals (12, 6, 3, 4), but its own per-claim table adds up to the README counts. The subsection uses the README figures and does not mention the old totals.

### 001528, Hadjas et al. 2025

Twelve claims reproduced, five partially, three not reproduced and five
blocked on the dandiset. Round 1 gave its own outcome for each claim from the
notebook with its conclusions removed and agreed with 24 of the 25; it would
call `fig5-anxa1-dls-inhibited` not reproduced. The author kept it blocked as
`data_missing`, since at the deposited 5 and 4 mice three of its six Wilcoxon
tests cannot reach p < 0.05 and the paper's own W of -36 and -55 fix its n at
8 and 10, and round 2 accepted this. Round 2 agreed with all 25 and nothing was
proposed, so there was no third round. The paper, a bioRxiv preprint, reports
that STN and PPN inputs excite SNr GABA neurons and Vglut2+ dopamine neurons,
which are resilient in Parkinson's disease, while they inhibit dopamine release
in DLS and the DLS terminals of the vulnerable Anxa1+ neurons, and that
TH+/ANXA1+ neurons are reduced in human PD tissue. The group sizes, the SNr
GABA and pan-DA responses to train duration and frequency, the opposite TS and
DLS responses, the DLS rebound and 5 Hz increase, and the Vglut2 and Anxa1
terminal and cell-body responses were tested on the fiber photometry
recordings. The four human tissue claims are blocked as `data_missing`.
`cohort-sizes` is not reproduced (10 of 16 counts match, 11 with the Vglut2
STN count explained, against the 12 needed), `fig3g-da-ppn-duration` is not
reproduced (p 0.26, 0.25 and 0.46 under three readings, a Friedman 4.07 where
the paper gives F 11.5), and `fig4eh-dls-5hz-increase` is not reproduced on the
1 s trains its criterion fixed, while the 4 s panels the same sentence cites
would give partially reproduced. `fig3b-da-stn-250ms-peak` is partially
reproduced: the latency is 0.786 s in the window fixed beforehand, raised by
two mice with a slow rise past it, and a narrower window gives the paper's
0.492 ± 0.033 s. The author used the full text of preprint v1 and filled gaps
the Methods leave from the conversion repository's description of the lab's
MATLAB scripts, which are not public.

The dandiset was converted by CatalystNeuro (catalystneuro/hnasko-lab-to-nwb).
It has no published version, and the attempt used the draft as modified on
2026-09-01T15:27:47Z. For the Anxa1 mice it holds DLS terminal recordings for 5
(STN) and 4 (PPN) mice where the paper analyses 8 and 10. Nine mice have only
recordings labelled SNc, without a site suffix in the file name; their signals
resemble SNc recordings, and the paper's cell-body statistics are reproduced
closely by the other nine mice's SNc recordings (p to two digits, t within
0.08), so the DLS recordings of these nine mice appear not to be deposited, and
the dandiset does not say which SNc recordings the paper used. Every Anxa1 file
lists both an SNc and a DLS fiber, so the site rests on the name of the dF/F
series alone. Three Vglut2 PPN mice have no 5 Hz trains while the paper's
Friedman statistic of 24.8 needs at least 9 mice with all four frequencies, DA
terminals in DLS have 8 mice where Figure S3 gives 9, subject C4608 has no 4 s
trains, and the human counts and histology are not in the dandiset. The dF/F
series are stated in a.u. but hold percent, and a recomputation from the
stored signals agrees with a median correlation of 0.9999 (durations) and
0.9988 (frequencies). Other findings: every session start time carries the
offset -00:01, so the true offset is lost; the frequencies protocol's
description gives 10 s between trains where the epochs and the Methods give
20 s; the modulation frequencies are described inconsistently within the
files; thirteen mice have 10 trials per condition where the Methods state 5,
and 30 mice have 16 s trains the paper does not mention; eight subject ids are
lower case; the conversion code names a 5 mW block s1s10mW, and its Python dF/F
forces the fit through the origin while its description of the MATLAB scripts
includes an intercept; and in the paper the Figure 5 legend gives 10 Vglut2
STN mice where its Wilcoxon statistics are the exact values for 9, F1,11 =
12.8 is given for both STN and PPN with different p-values, two Friedman
entries do not fit their p-values, and the Figure 5 legend and the Results
disagree on the Anxa1 STN frequency effect.

The notebook ran in 290 s in the first clean run, about 5.5 minutes after
round 1 and 425 s after round 2. Loading first took about 10 minutes because
h5py serializes threads, and the author switched to a process pool; two bugs
found while preparing, timestamps stored in place of a sampling rate and
shifted onsets falling outside the recording, were fixed before the final run.
Round 2 found statements the outputs did not support, among them that
`fig5-anxa1-dls-inhibited` could not be tested by its criterion, where
partially reproduced was reachable and not reached (2 of 6), that the
cell-body statistics match exactly, and a runtime of five minutes, and these
were corrected. Untracked files in the repository root that the author did not
create were left alone. The author's points on the protocol: no published
version, where drafts are allowed only for repeat attempts; a 10% tolerance
that does not suit test statistics whose windows the paper does not state, nor
counts of animals; a block that depends on the selection where data are
missing, which the protocol would call `other`; site labels that the paper's
counts contradict and the signals support; a data check that ran into claim
territory; no recipe for a clock check on evoked photometry; a source
hierarchy that does not fit a conversion repository describing unpublished
analysis code; test choice after a Shapiro-Wilk test; and CatalystNeuro being
both the curator of the dandiset and the accountable party for the attempt.
