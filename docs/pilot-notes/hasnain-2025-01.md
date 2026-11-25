# hasnain-2025, Hasnain et al. 2025

One claim reproduced, three partially, four not reproduced and eleven
blocked, all eleven for missing data; all eight tested outcomes rest on an
assumption. The first verification round agreed with 18 of the 19 outcomes
and would have given `fig4f-medulla-null-not-spanning-alm` not reproduced;
the author kept partial, and the second round agreed with all 19, so there
was no third round. It pins version 0.231012.2129, the latest published;
the paper cites no version, and the units of the session compared are the
same in 0.230822.0128. The paper, Hasnain, Han and Economo, "Mapping neural
subspace dynamics onto the structure of the mouse descending motor system"
(bioRxiv, doi:10.1101/2025.10.17.682917), records phototagged layer 5
extratelencephalic neurons (L-ETNs) and unidentified neurons (UNs) in ALM
and tjM1 of mice in a delayed-response licking task, and reports that
L-ETNs are as selective as UNs, have the same movement-null and
movement-potent subspace preferences and span both subspaces; in the MAP
recordings of Chen et al. (2024), which it reuses from DANDI:000363, it
reports that the medullary reticular nuclei hold movement-null activity
that explains less variance than the potent activity, is predicted from
ALM, has lower dimension and does not span ALM's patterns. The claims were
written from the text of preprint version 1 (PMC12632980), with no figure
read, and from the linked subspaceID code at commit d593949, which holds
only the subspace optimization; the claims check made seven corrections
and left two points open, the paper's two session and unit counts and a
variance-explained reading that departs from the Methods' formula. The 11
claims on the paper's own recordings are blocked; the 8 on the MAP data
were tested. `fig4c-medulla-null-smaller` is reproduced under one of 15
reading combinations (G1, B2 and V2: 28.4 against 51.9%, p = 0.017), and is
seed sensitive, the potent mean being 52.3% under two seeds, outside its
51.92 bound. Partial are the medulla selectivity (32.4, 49.1 and 85.9%
against 7, 21 and 49%, the order kept), the ALM null against potent
variance (no difference, p = 0.086, with the means 51.3 and 79.6% out of
tolerance) and the UMAP claim (25.7% of ALM units have no medulla
neighbour against 0.1% with labels shuffled within session, while only
59.4% of medulla units have an ALM neighbour). Not reproduced are the
session selection, both decoding claims (held-out R2 of -611.5 to -249.1%
for ALM to medulla against 40%) and the medulla's lower dimension (N1 p =
0.741, N2 p = 0.087). The selection is held at reading G1 while the other
readings are searched; under G2 the ALM claim of Figure 4c would be
reproduced and Figure 4e reproduced under N2, an asymmetry the round-2
verifier asked to have stated, which it now is. Round 1 found that the
electrodes table had not been checked for CCF positions, that the negative
R2 values were not traced, that the UMAP null mixed sessions and one
medulla session has a null dimension of 1, and that no single reading
reproduces both Figure 4c claims; in reply units were given the CCF label
of the nearest classified unit (97.3% agreement), a second notebook
repeated Figure 4 under G2, the R2 values were traced to overfitting of a
nearly unpenalized fit (Spearman -0.61 with predictors per training
trial), the UMAP null was shuffled within session, and printing the sample
cue times found 446 trials with another delay, which were left out. Round
2 found that the text of several cells and of the record had been written
from another execution than the deposited notebooks; the cause was
OpenBLAS choosing other kernels on another processor, which the decoder,
the UMAP embedding and some G2 shuffle dimensions amplify, and the record
now gives both executions' values, with the same outcomes. The kernel was
not pinned, which would have taken about three hours more. The author
asked a reader nothing and no questions file exists. The author's run took
about 2.5 hours (02:02 to 04:33 UTC); the notebook ran in 35 minutes at
first, with peak memory about 3.8 GB, and the two notebooks in 2428 and
3012 s at the end.

The paper's selection cannot be recovered from the files: with the
dataset's CCF labels and `classification` it gives 5 ALM and medulla
sessions from 4 mice with 300 ALM and 340 medullary reticular units, where
the paper reports 16 sessions (or 11 from 7 mice) with 604 and 724 units,
and 17 bilateral ALM sessions from 9 mice where the paper reports 20 from
10; with `unit_quality` and transferred labels it gives 19 ALM and medulla
sessions from 7 mice with 1501 and 1745 units, and 31 bilateral sessions.
The CCF annotation (`anno_name`) is filled only for units whose
`classification` is good (69453 of 272227 units), which its description
does not say, though the electrodes table holds each electrode's CCF
coordinates. Units carry two quality labels, `unit_quality` and
`classification`, with no statement of how they differ, and 1852 units
have no `classification` value. The trial table has no column for the
delay duration, and 446 correct and error trials over 22 sessions (13 to
57 per session) have a 1.8 s or 0.3 s delay in place of 1.2 s, which shows
only in the event times. The jaw, nose and tongue tracking are stored in
'a.u.' but hold pixel positions of the side camera (about 294 Hz). The
baseline z-score reaches 278 s.d. among units classified good and above
50000 among units with `unit_quality` good. The spike, video and trial
clocks agree in all 22 selected sessions. The paper's own recordings are
not public and no dandiset holds them; DANDI:001472 holds the data of the
authors' earlier paper. In the paper, the ALM and medulla sessions are 16
in the Results and 11 in the Methods, the bilateral ALM units 1116 and
2016, and the decoding window 40 and 45 ms. Questions are put to the
paper's authors: how R2 and lambda were computed for the decoding, how the
movement threshold was set, which trials and which 'good' label were used,
how variance explained is normalized and which dimensionality measure
Figure 4e uses, and how near-silent units were handled in the z-score.

The author's points on the protocol: the claims file's readings multiply
into dozens of combinations, and each was run against the main one, one
factor at a time; it does not say whether a variant named in the claims
file can decide an outcome, and the example.m z-score was not allowed to;
a criterion where neither branch applies was judged partial; "reproduced
under any reading" conflicts with adopting the best-supported reading, and
the criterion was followed with `assumed` set; per-claim seeds do not fit
claims that share one computation, and one claim's seed was used; seed
checks for every reading multiply the runtime and were run for the main
and the deciding reading only; it does not say when to mark `assumed` for
an assumption that applies to every claim; and an atlas check tried
outside the notebook was dropped and left out of the record.
