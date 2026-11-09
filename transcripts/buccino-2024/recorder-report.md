I wrote the notes to `docs/pilot-notes/000294-buccino-2024-01.md` and changed no other file. The `catalystneuro` field for 000294 in `targets/dandisets.json` is empty, so the dataset paragraph does not open with the CatalystNeuro sentence. Here is the text:

# 000294, Buccino et al. 2024

Four claims reproduced, one partially, none not reproduced and one blocked on
the dataset, with five more blocked that also need outside data; the other
twelve claims use data elsewhere and are left out of the counts. It pins
version 0.260528.0854, the only published version; the paper cites none, and
the draft holds the same two files. The paper, Buccino, Damart, Bartram and
colleagues in Neural Computation, fits single-neuron models with BluePyOpt on
intracellular features alone (the soma strategy) or with extracellular
features added (all, sections and single), first on a ground-truth model
(hay_ais) and then on two neurons of rat cortical cultures recorded at once by
whole-cell patch clamp and a high-density microelectrode array (HD-MEA) during
the eCode protocols. The claims were written from the version of record
(Neural Computation 36, 1286-1331) and from the paper's code
(alejoe91/multimodalfitting at commit 24e8e61). The runs, the eCode protocols,
the holding potential, the extracellular spike amplitude, the electrode counts
and sampling rates and the culture age were tested on the dandiset:
`mea-electrodes-and-rates` is partially reproduced, as 678 and 675 electrodes
are recorded at 20 kHz but the patch is at 20.41 kHz for six protocols and 125
kHz for APWaveform, and `culture-age` is blocked as `metadata_insufficient`.
The five claims on the repository's models and morphologies are reproduced:
the AIS leaves a dendrite in both cells, the ground-truth rheobase is 150 pA,
the AP starts in the distal AIS, the largest channel is the one nearest the
AIS, and the feature counts are 76, 87, 109 and 153. `fig3b-ap-initiates-distal-ais`
rests on an assumption, as on the code's 0.05 ms cut-outs the distal and
middle AIS tie, and the order is read between samples (leads of 0.0042 and
0.0202 ms) and on a fixed-step run at 0.005 ms, where it holds in 12 of 12
spikes. Every model fit is blocked as `too_large`: 480,000 evaluations per set
of fits, at 12.2 s per evaluation intracellularly and 20.5 s with the
extracellular signals in the run recorded, need at least 2457 CPU hours for
the ground-truth fits and 2182 for those of the two cells, which blocks the
seven ground-truth fit claims and the five on the recordings. The author asked
a reader no questions, so the answer run and the following author run changed
nothing. Round 1 agreed with all 23 outcomes; it found that the AIS placement
behind fig3a was never checked (nearest electrode 23.3 um away against 26.8 um
for the next) and that the fig3b lead of 0.005 ms lay below the code's
resolution, and asked for each spike's alignment within its sweep. The
author's first run had said that BluePyOpt's LFPy simulator does not run in the
locked environment, which was wrong, as BluePyOpt 1.14.26 provides it, and the
revision ran the code's own pipeline: the recomputed template matches the
repository's (correlation 0.99992, RMS difference 1.3%), which places the AIS
midpoint at (12.6, -13.7) um, 16.8 um from channel 43 against 39.3 um for the
next; all 1616 spikes have their MEA trough 0.15 to 0.70 ms before the patch
peak; the feature counts come from the code's evaluators; and parts of the
blocked claims are computed, among them the ground truth firing 0 spikes at
HyperDepol -160% and 1 at -40%. Round 2 agreed with all 23, so there was no
third round, with a reservation on `mea-electrodes-and-rates`, whose criterion
has no partial clause, so that read strictly it is not reproduced. It found
that the revision's cost figures (16.8 s, 27.9 s, 3350 and 2980 CPU hours)
matched no printed output, a mean-template difference given as 13.3 uV where
13.6 uV was printed, an inference that the voltages are not corrected for the
junction potential, and an overstated `code_mismatch` finding on 796
extracellular features, where the 800 finite features are within the claim's
tolerance of 80; these were corrected, the finding removed, and the record now
says the timing varies with the runner's load (8.0 and 14.3 s, 1699 and 1487
CPU hours in the run round 2 reviewed). Two questions were put to a reader
during the revisions, after the answer step: whether APWaveform at 125 kHz fits
the paper's "typically 200 kHz", and whether the holding-potential window
should end at the code's ton or at the stimulus onset in the files, which agree
to within 0.1 mV. The author's run took about 56 minutes (23:05 to 00:01 UTC)
and nothing failed in the final run; getting the simulator to work took several
tries, ending with NEURON 9. The notebook ran in 382 s at first and in 743 s in
the last run.

The CurrentClampSeries are stated in volts with conversion 1 but hold
millivolts (-100 to +46), and the CurrentClampStimulusSeries are stated in
amperes with conversion 1 but hold picoamperes (holding levels of 12 and -37,
steps up to about 1000). The patch timestamps are at 20.41 kHz (49 us) for
every protocol except IDthres (20 kHz) and APWaveform (125 kHz, 8 us), where
the paper states 20 kHz and, for APWaveform, typically 200 kHz; the intervals
are regular and agree with the nominal step durations. The dandiset's metadata
name the paper by its title but link it to doi:10.1162/neco_a_01676, which
Crossref gives as "Energy Complexity of Convolutional Neural Networks"; the
paper is doi:10.1162/neco_a_01672. The icephys sequential recordings table
leaves out the first sweep of every protocol after IDthres in each run and
every PosCheops sweep (35 of 300 recordings for cell 1, 28 of 240 for cell 2),
while the protocol_name and run columns of the intracellular recordings table
are complete. Cell 2's file holds runs 3 to 6 of the recording, renamed run1 to
run4, which only the descriptions of its MEA series and the paper's export
notebook say, and the dandiset does not say why runs 1 and 2 are not
deposited. In the deposited sweeps the stimulus starts 50 ms earlier than the
timings of the paper's feature code (350 ms against ton 400 ms for IDrest, 450
against 500 for firepattern), so those timings cannot be applied to the files
as they are. In every run 117 to 132 of the 675 to 678 MEA channels are
constant for at least one of ten one-second segments, the channels the code
removes before computing templates, with nothing marking them. The electrodes
table's x, y and z are NaN, location is "unknown" and impedance -1, with
positions only in the custom columns rel_x and rel_y, whose frame is not
described, and no culture age, plating date or days in vitro is given in the
files or the metadata. The paper describes IV as 11 steps from -140 to 20% by
20%, which is 9 steps, where the data hold 11 steps from -140 to 60%, and gives
79 intracellular features in Methods 5.4 and 76 in Table 1, the code's count
before and after it drops three sag features of IV -20%. No duplicate
recordings were found, and the patch and MEA share a clock: with the spike
times shifted by 100 ms the largest channel falls from 159 to 189 uV to about
20 uV, and the per-run slopes of the spike alignment are -0.003 to 0.023 ms per
s against the 20.4 ms per s a clock mismatch would give. One question is put to
the paper's authors: whether the AIS order of Figure 3B was read from a finer
simulation than the plotted cut-outs.

The author's points on the protocol: the entry's Python is fixed at 3.13, where
the paper's simulator stack (BluePyOpt 1.13.88 with LFPy) was taken not to run,
so BluePyOpt's NEURON simulator was used and recorded as a deviation;
`measured` takes one number where a claim covers two cells; a 10% relative
tolerance is undefined for the IV 0% step; the clock check's examples do not
fit patch-plus-MEA data, and spike-triggered templates against spike times
shifted by 100 ms were used; it does not say whether fits blocked both by cost
and by the simulator are `too_large` or `not_runnable`; the rule against
writing to disk covers dataset files only, and the repository was fetched and
its mechanisms compiled in a temporary directory; and it does not say how to
present a cost estimate shared by blocked claims.
