# fujisawa-2008, Fujisawa et al. 2008, third attempt

Five claims reproduced (one on an assumption), 12 partially (five on an
assumption), 14 not reproduced (three on an assumption) and one blocked for
missing data, plus the link claim `channel-region-link`, not reproduced, as
the CRCNS channel map does not fit the nose-poke sensors of rat GG. The first
verification round agreed with 31 of the 33 outcomes as they stood and the
second with all 33; nothing was proposed after the second, so there was no
third round. It uses both datasets, under the pilot-14 rule that records are
filed by paper, with one claims file of 33 claims that replaces the two
per-dataset files; fujisawa-2008-02 used CRCNS pfc-2 alone. DANDI:000067 is
pinned at 0.261106.2004, the most recent published version, which the paper
does not cite; CRCNS pfc-2 is unversioned, with the MD5 sums printed in the
notebook. The paper, Fujisawa,
Amarasingham, Harrison and Buzsaki in Nature Neuroscience (11, 823-833),
records units with one 8-shank, 64-site silicon probe per rat in anterior
cingulate and dorsal prelimbic cortex of four rats in an odor-based delayed
matching-to-sample task on a figure-eight T-maze, three in layer 2/3 and one
in layer 5, and reports trajectory-specific firing along the maze, putative
monosynaptic connections found from cross-correlograms with a jitter test,
transmission that depends on the rat's position, depression and facilitation
with spike repetition, and a supralinear effect of coincident inputs. The
claims were written from the version of record and its supplement, opening
the PDF pages only for figures the text garbles; the paper links no analysis
code. Spike times were taken from the NWB files, matched to the lab's cells by
shank and cluster, and trials, positions and cell lists from CRCNS, with
`EE188_example.mat`, the paper's 117-cell session, streamed from inside
`EE.188.tar.gz`. Reproduced are `fig2-field-size` (0.241 +/- 0.169),
`retrospective-coding-rare` (4.3% of EE.188 cells), `speed-not-correlated`
(median -0.022), `no-spatial-clustering` (in the layer 2/3 session only) and
`thinning-preserves-dependence` (7 of 34 pairs, on M = 5,000 surrogates).
Partial are, among others, `rats-and-units` (627 units in three rats, within
633 +/- 63.3, but no rat holds 222), `side-arm-selectivity-by-layer` (61.0% and
52.6% against 40% and 22%, layer 5 higher at p = 0.046), `central-arm-selectivity`
(30.4% and 29.5% against 16% and 18%), `traj-diverge` (the path at 0.30, head
direction from 0.02), `fig4-position-dependence` (6.4% against 19.5%, above
the null rates) and `population-vector-width` (layer 2/3 0.282 against the
limit 0.267 with peak-normalised rates; z-scored rates would reproduce it).
Not reproduced are, among others, `fig3-connection-rates` (1.449% connected and
1.173% excitatory, the excitatory rate 1.6 to 2.1 times the paper's),
`fig3-cell-classes` (23 interneurons, 3.7%), `fig3d-hub` (86 of 117 cells
against 39), `fig3b-session-connections`, `fig5a-session-selective-connections`,
`fig6-facilitation-depression` (no combination with both fractions above 5%,
under either labelling) and `fig7-supralinear` (transmission below the linear
prediction in every satellite). The outcomes of `rats-and-units` and
`central-arm-selectivity` rest on taking the lab's cell lists as the paper's
units: with every NWB mPFC unit (1,373) the first would be
not reproduced and the second would have both values within tolerance under
one rat reading. Round 1 disagreed on `fig2c-active-fraction`, which it gave
as not reproduced, and on `population-vector-width`, which moved to partially
reproduced as it proposed, and asked for the NWB unit variant, peaks under both
rate readings, the shared jitter and a tail labelling in the facilitation and
depression test, a check of head direction and the one-cell jitter, all done;
a question on the claims file's literal "first above later" went to a reader
in `questions/fujisawa-2008.yaml`, written after the answer run, so it is
unanswered. Round 2 agreed with all 33, withdrew its fig2c disagreement and
asked that `rats-and-units` be marked assumed and that the literal labelling be
run with the shared jitter, which gives the same outcome; it also found
sentences the outputs did not support, which were corrected, though one unit
variant moves by one unit between the verifier's copy and the author's runs of
the same seeded code (409 against 408 of 1,211), a cause not confirmed. The
reconciliation with fujisawa-2008-02, run blind, finds all 12 of its findings
still present and 7 of the 19 shared claims with a changed outcome, three from
partial outcomes the merged claims file adds, three from differences in
method (`task-performance` was tested there from the sensor channels of one
session, and `population-vector-width` used rate curves built differently)
and one, `fig4-pair-156-136`, graded differently on nearly the same numbers. The
author's run took about 3 h 36 min; two full runs failed, one on a variable
name reused across cells and one on an array reshape, both fixed, and peak
memory was brought from 12.1 to 9.0 GB with identical results. The notebook
ran in 29 min at first, 42 min after round 1, 40 min after round 2 and 2117 s
after the reconciliation, whose own notebook ran in 108 s.

The dataset was converted by CatalystNeuro (catalystneuro/buzsaki-lab-to-nwb).
Only correct trials are listed, in SessionNP, the whl trial numbers and the NWB
trials tables, so task performance and any analysis of error trials cannot be
made from either dataset. Neither dataset gives the layer of each rat's probe
or links the rats EE, FF and GG to the paper's E to H, no rat holds the paper's
222 layer 5 units and no session the 142 cells of the layer 5 session of
Figure 2a and Supplementary Figure 11. The CRCNS description documents a 1 Hz
'Cells' list that the files do not hold and does not describe CellsInfo, the
per-session cell list (627 units with EE.188's example file, against 1,373
sorted mPFC units); CellsInfo is consistent with the 1 Hz rule (98.9% of listed
units reach 1 Hz in the trials, 28.7% of those left out), and neither dataset
marks the paper's well-isolated units. In 11 of 13 working memory sessions of
DANDI:000067 every unit has cell_type 'not classified in the source' and
lab_cell_number -1, so the NWB units can be linked to the lab's cells only
through shank and cluster_id, and then their spike times are identical for 615
of the 627 used. The EE.088 file has no wideband signal, and EE.188 and EE.210
have no trials table or linearised position, though CRCNS holds them. In the
three GG sessions channels 97 and 98, the nose-poke sensors in the CRCNS
description, carry no poke signal, nor does any channel from 97 to 101, which
the NWB files label 'neural'; the FF files have 104 channels labelled as rat
EE's layout, where the description gives FF 101. The two CRCNS lists of
EE.188's cells disagree (105 cells, 87 pyramidal and 18 interneurons, against
117, 33 pyramidal, 15 interneurons and 69 unknown, with types agreeing for 42
of the 105 common cells), and DANDI:000067 uses the 105-cell list; the example
file codes cells 32 and 72 as interneurons, though Figure 7a names them
presynaptic pyramidal cells, and cell 136, the interneuron of Figure 4, as
unknown. Its pairs_all list holds 43 connections, against the paper's 48 and
30 for the session, and its largest component is the 39-cell circuit of Figure
3d; which selection it is, is not said. Ten of the 13 sessions track a single
LED, so head direction exists only for EE.152, EE.165 and EE.188. The
linearised position is nonzero through each trial's nose poke, and the spikes'
trial labels and positions start at the first nose-poke while the description
defines the trial start as the end of the last (269071 of 676892 labelled
spikes fall between the two). `EE188_example.mat` is not in folder EE0708 or
in filelist.txt but is member 62 of 75 of EE.188.tar.gz, 1.99 GB into the 2.41
GB gzip stream. The trial table of EE.188 leaves out 3 trials that the sensor
channels and the position file show as correct and 1 error trial. Questions
are put to the paper's authors: how the rates enter the population vectors,
how many permutations or jitter surrogates each test used, how Figure 7
defines coincident events and the transmission window, which rat is layer 5
and which units make the 633, whether the global band of the jitter test was
the minimal band or 1% on each side and whether the cross-correlograms were
binned at 1 or 0.5 ms (1.449% and 1.091% of directed pairs connected here,
against 0.79%), and how the connections of Figure 3d were chosen.

The author's points on the protocol: the claims file says the number of
permutations should not change the outcome, but at level 0.01 it does, so more
were used and the claims marked assumed; no rule says how to combine two
datasets for one claim, and spikes were taken from DANDI and trials and cell
lists from CRCNS; `entry.py check` asks for an `inputs` entry for a
`with_labels` claim even when the labels come from the dataset's own
description; the `fig2c-active-fraction` criterion defines only reproduced,
and partial was used; the data fix some of the claims file's open readings,
recorded as a deviation; small members were cached on disk during
development, against "do not download to disk", and deleted afterwards; and
the blinded checkout still held the old per-dataset claims files and reader
transcripts, which were not read.
