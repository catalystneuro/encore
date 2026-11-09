I wrote the notes to `docs/pilot-notes/000541-yemini-2021-01.md` and changed no other file. The dataset's `catalystneuro` field is empty, so the findings paragraph does not open with the conversion sentence. Nothing is committed. The untracked dotfiles that `git status` shows at the repository root are sandbox device nodes, which the author's report also mentions; I did not create them.

```markdown
# 000541, Yemini et al. 2021

Six claims reproduced, three partially, three not reproduced and ten blocked
on the dandiset. With outside data, counted apart: one reproduced, one
partially and three blocked. It pins version 0.241009.1457, the most recent;
the paper cites no version, and all three published versions hold the same 21
assets. The paper, Yemini, Lin, Nejatbakhsh et al. in Cell, presents NeuroPAL,
a multicolor transgene for identifying every neuron in C. elegans, with
receptor expression maps, mutant analyses, a positional atlas and
identification software, and uses it in whole-brain GCaMP6s imaging of heads
of strain OH16230 in a microfluidic chip given 10 s pulses of NaCl,
2-butanone and 2,3-pentanedione. The claims were written from the accepted
author manuscript in PubMed Central (PMC10494711) and from three code
repositories (venkatachalamlab/NeuroPAL-traces at 92b27ed, amin-nejat/CELL_ID
at 759898d and Eviatar/Optimal_Coloring at f01284f), none of which holds the
statistics or the connectome analysis of Figure 6; the author added two link
claims, to the paper's Zenodo deposit and to the Cook et al. 2019 connectome,
and read Tables S1 and S6 from the publisher only to choose between readings.
Only the head imaging of Figure 6, Figure S1H and Figure S2 could be tested.
Under the main reading, one member of each near-duplicate pair removed and
each trace z-scored, both assumptions, ASER rises during NaCl (p = 0.0028),
all six unknown interneuron classes respond to NaCl, both odors give a larger
fraction of negative responses than NaCl (0.234, 0.245 and 0.362), and the
pharyngeal, downstream interneuron and distinct stimulus set claims hold.
`fig6-nacl-unknown-interneurons` rests on the normalisation, as the
criterion as written, on the mean dF/F0, gives four of six.
`fig6-all-heads-responsive` is not reproduced, as 19 of 21 heads pass,
`figs1h-avf-cyclic` gives a median of 0.121 Hz against 0.27 to 0.33 Hz, and
no reading of `figs2a-pca-trajectories` separates all three pairs.
`fig6-asj-ric` holds 5 of 6 parts, `fig6gi-stimulus-specific-correlations`
misses the odor pair (p = 0.17) and gives 91, 96 and 95 of 100 splits, and
`fig6-sample-sizes` and `fig6jk-connectome-correlation` match on heads only,
the latter with all head R2 values below 5% and none within tolerance.
`fig6d-awc-asymmetric` is blocked as `metadata_insufficient`, the tail claim
and eight claims on Figures 1, 2, 4, 5, 7 and S1 as `data_missing`,
`fig7de-optimal-coloring` as `not_runnable`, as the solver needs MATLAB, and
`fig4bd-gaba-network` and `fig4e-extrasynaptic` as `other`, untested here.
The link to the deposit is partially reproduced, as 81.7% of traces reach r
of 0.9 against the 90% the author set. The author's first run, over all 29
claims, gave eight reproduced, five partially, three not reproduced and 13
blocked. The author asked a reader no questions, so the answer run and the
following author run changed nothing. Round 1 agreed with 28 of 29 outcomes,
giving partially reproduced for fig6gi, which passed only with both members
of near-duplicate pairs removed while a window with no stimulus passed too,
and the author took that outcome. Its points also led to a reading that keeps
exactly the deposit's traces, "one" as the main selection reading, z-scored
traces for the response tests and the PCA, which moved
`fig6-nacl-unknown-interneurons` to reproduced, a check of the q values on
the paper's own p values (agreement at 0.05 in 273 of 285 tests), the
corrected grid spacing, and fig7de moved to `not_runnable` and fig4bd and
fig4e to `other`; questions to a reader, on whether the median of 18 covers
heads and tails together and on the normalisation sentence the claims file
leaves out, were put during the revisions after the answer step. Round 2
agreed with all 29; it asked that fig6-sample-sizes be marked assumed and
found sentences the outputs did not support, among them 101 named traces
missing from the deposit where there are 126, which were corrected. The
author then proposed `methods_underspecified` for fig4bd and fig4e, and a
third round disagreed with both: the paper names the transmitter maps and
the Cook et al. connectome in the same paragraph as the claims, so they
should be tested. The outcomes stayed `other`, the wrong statement was
corrected wherever it appeared, and the analysis is left to a new attempt.
The author's run took about 50 minutes (16:01 to 16:51 UTC) and nothing
failed. The notebook ran in 332 s at first, in 286 s after round 1 and in
348 s in the last run.

The dandiset holds only the 21 OH16230 head recordings of Figure 6; the 21
tails, the 7 OH15500 heads and the imaging behind Figures 1 to 5 and 7 are
not in it, and the tails, the OH15500 heads and 10 atlas worms are in the
paper's Zenodo deposit (doi:10.5281/zenodo.3906530). The files do not say
which AWC neuron is ON and which OFF, which the AWC asymmetry result needs;
the NeuroPAL image holds it, as CyOFP1, the srsx-3 fluorophore of Table S1,
is brighter relative to TagRFP-T in the AWC the deposit marks as OFF in 19 of
21 heads. The calcium imaging volume states a grid spacing of 0.267, 0.267
and 1.5 um, as the NeuroPAL volume does, but the calcium segmentation's x and
y coordinates are half those of the same neurons in the NeuroPAL segmentation
(fitted ratio 1.94 to 2.09), and the movie is 256 x 128 pixels against 512 x
256, so it is binned 2 x 2 at 0.533 um. SignalRawFluor and SignalRawFluordNMF
hold the same numbers in all 21 files. NeuronIDs include AMSOL, AMSOR and
HMC, which are not neurons, and DD6, a posterior ventral cord motor neuron,
in head 20190929_06. 126 named traces have no trace in the deposit (AVL in
11 heads, I5 in 8, and others), 113 of them with finite values, and the
dandiset does not mark which traces the paper excluded. The dandiset's
traces are one frame (0.25 s) earlier than the deposit's in all 21 files,
and which of the two is aligned with the stimulus table is not stated. The
stimulus table gives 2-butanone as "10^-4mM" and the order as random, where
the paper gives 10^-4 dilutions and a rotated order, and the files show three
orders, seven heads each. Questions are put to the paper's authors: which
member of a near-duplicate pair was removed and on which traces the
correlation was computed, as the rule removes 338 named traces keeping one
member and 651 removing both while the deposit lacks 126, how traces were
normalised for the response tests, as Table S6's p values cannot be
recomputed from the deposited dF/F0 traces (rank correlation of log p 0.57 to
0.75), and how a head was judged to show the published ASE and AWC responses.

The author's points on the protocol: the tail claims and two atlas claims
are marked as using the dataset though their data are public on Zenodo, and
as the author may not edit the claims file they were blocked as
`data_missing` with the Zenodo location in the notes; the author cannot add a
link claim to a claim's `depends_on`, so the dependence on
link-connectome-names was stated in notes; there is no form for a link
criterion written after the outside data were seen, and this was recorded as
a deviation; `measured` must give one value per expected value even when one
cannot be measured, so fig6jk left it out and fig6-sample-sizes recorded a
tail count of 0; and nothing says how to judge a criterion whose test also
passes a null control, and fig6gi kept the criterion's outcome with the null
result in its notes.
```
