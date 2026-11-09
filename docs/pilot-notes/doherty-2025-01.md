# 001444, Doherty et al. 2025

Eighteen claims reproduced (eight on an assumption), three partially (one on an
assumption), 13 not reproduced (one on an assumption) and six blocked, two for
missing data and four as `methods_underspecified`. All 40 claims are on the
dandiset. The first verification round agreed with 33 of the 40 outcomes as
they stood and the second with 39, and because two changes of outcome were
proposed after the second, for `fig1-network-size` and
`fig2c-control-it23-rate-activated`, a third round reviewed those two claims
alone and agreed with both. It pins version 0.250805.2002, the only published
version; the paper cites none. The paper, Doherty, Chen, Smith, Wichmann, Chu
and Lytton, "Enhanced beta power emerges from simulated parkinsonian primary
motor cortex" in npj Parkinson's Disease, simulates in NetPyNE a 300 um
diameter cylinder of mouse M1 with 10,073 neurons in 15 populations, in four
sets of four 4.3 s simulations (control or parkinsonian PT5B conductances, in
the rest and activated states), and reports its results from set
sM1_12-12-2023: the beta and gamma peaks of the PT5B spike count histogram
(SCH), population rates, CV of the ISI, duty cycles, LFP spectrograms,
coincident spikes and unitary events. The claims were written from the version
of record served by Europe PMC (PMC12325672), without the supplement; the code
the paper cites (github.com/suny-downstate-medical-center/pd_m1_6ohda, commit
0a1f0e8) holds the simulation and four plotting notebooks and no code for the
analyses, and the Morlet spectrogram of NetPyNE 1.0.5 was copied into the
helper as an input. Rates are taken over the last 2.3 s (W) under three
readings of the cells averaged over: R1 all cells, R2 the cells with a spike in
W, and R3, added by a reader's answer, the cells that fired at least once in
the 4.3 s simulation, which are the cells the files hold. Reproduced are the
SCH peaks at 19 Hz (control rest), 44 Hz (control activated) and 15 Hz
(parkinsonian rest), the PT5B rate claims (11.69 +/- 9.40 and 26.76 +/- 18.17
spikes/s in control, 14.24 +/- 7.13 and 29.68 +/- 12.67 parkinsonian), the CV
claims, the more negative parkinsonian activated potential (-5.62 mV by the
mean, all 20 recorded cells lower), the higher 20 to 35 Hz power, and, on R3,
`fig2c-control-it6-rate-activated`, `control-it5-silenced-activated`,
`control-it4-rate-activated`, `pd-it5-silenced-activated`,
`pd-it6-rate-unchanged` (6.00 and 5.99 spikes/s, which also rests on pairing
the cells kept in both files, the union pairing giving Wilcoxon 0.0025),
`rest-it5a-rate-pd-vs-control` and `activated-it6-rate-pd-vs-control`;
`rest-synchrony-increase` rests on the assumption that coincidences are counted
as pairs of cells, the one count of four that can exceed its expectation on
these data (3.8 to 3.98 s against 0.8 to 1.65 s). Partial are
`activated-pt5b-rate-pd-vs-control` (Mann-Whitney 0.0052 where the criterion
asks p < 0.001), `rest-beta-power-order-of-magnitude` (ratios of 65 to 129,
above the criterion's 3.16 to 31.6, with no outcome given for a larger ratio)
and, on R3 and the both-files pairing, `fig2c-control-it23-rate-activated`
(1.203 +/- 1.649 and 6.662 +/- 8.858, two of four tests above 0.001 on 25
paired cells). Not reproduced are `fig5-pd-activated-gamma` (27 Hz against 43
+/- 4.3), the two duty cycles, the four spectrogram claims (burst rates such as
1.30 Hz against 1.53 to 1.87 Hz, and 1.74 Hz against 4.5 to 5.5 Hz), the two
coincident-spike claims (99.95% to 100% of PT5B spikes against 1% to 3%), the
unitary events of Figs. 4 and 7, `fig5c-pd-it23-rate-activated` and
`rest-it4-rate-pd-vs-control`, whose parkinsonian mean rests on 2 cells and
where no test reaches p < 0.05. Blocked are `fig1-network-size` and
`model-pt5b-excitability-decrease` for missing data, and `robustness-four-sets`
(no measures in the claims file), `pt5b-highest-rate` (PV5A fires faster than
PT5B, so the two readings of "any population" disagree) and the two
subthreshold oscillation claims (no detection rule) as
`methods_underspecified`. The author's first run gave 10 reproduced, 2
partially, 23 not reproduced and 5 blocked, with no outcome on an assumption.
The author asked a reader whether R3, under which every IT value matches the
paper to the printed decimal, is allowed; the reader added it to the claims
file from the paper's text, and the author-answers run moved seven rate claims
to reproduced and the two IT2 claims to partially reproduced, all on R3. Round
1 disagreed with seven outcomes and found that the paired tests were run only
on the cells kept in both files, that the bin count of coincidences saturates
at the window length and cannot exceed its expectation, that the claims file's
coincidence reading looks like a misreading of the paper and its burst and
duty cycle conventions are its reader's own, and that the 250 ms S2
window has no bin between 1 and 3 Hz; in reply both IT2 claims moved to not
reproduced and `rest-synchrony-increase` to reproduced on the pair count, three
more coincidence counts with chance levels on independent cells were added,
the S2 test was run with 1 s and 2 s windows, S2 burst rates were taken per 2.3
s, and readers were asked about the coincidence measure and the burst and duty
cycle conventions, while `fig1-network-size`, `activated-pt5b-rate-pd-vs-control`
and the two unitary-event claims were kept with the disagreement recorded.
Round 2 agreed with 39, asked for `fig1-network-size` to be blocked as
`data_missing`, gave two caveats for `rest-synchrony-increase` (the pair nulls
take spikes as spread evenly over a window, so the excess partly tracks the
PT5B rhythm, and the count-preserving null is at its ceiling), and found
sentences the outputs did not support (nine IT outcomes resting on R3 where the
record marked seven, 95% of 1 ms bins where 99.1% to 100% is printed, 551 ms
for 552 ms, one or two clusters for two, the diverged run stated as fact, and
R1 values in `measured` for `rest-it4`), all corrected; the author then
proposed blocked for `fig1-network-size` and, having found that the IT2 test
giving no increase (Wilcoxon 0.69) came from the union pairing,
partially reproduced for `fig2c-control-it23-rate-activated`, both of which
round 3 accepted, asking that the second be marked as assumed. The author's run
took about 40 minutes (16:58 to 17:37 UTC) and nothing failed; the notebook ran
in about 320 s at first, nearly all of it streaming the files, 279 s after the
author-answers run, 342 s and 362 s after rounds 1 and 2 and 450 s at the end.
Untracked dotfiles in the repository root, which the author did not create,
were left alone.

The units tables hold only the cells that fired, 2,917 to 4,480 M1 cells per
file in set sM1_12-12-2023 and 2,765 to 4,714 in the others, where the
dandiset description says each file holds all 10,073 neurons; input generators
that did not fire are missing too, no population size is stated, and the sizes
can be recovered only from the gid blocks in the unit names (24 gids between
blocks are never seen), so the network size cannot be counted and R1 rests on
those blocks. The four files of the paper's set hold 20 PT5B membrane
potentials each (gids 5201 to 6502), where the description says 400 and the
other twelve hold 400 (gids 5130 to 5529), and in the paper's set the
potentials do not belong to the run whose spikes are stored: their 0 mV
crossings match the same gid's spikes in the first 0.5 s (94.8% to 100%) but
only 1.5% to 5.6% of spikes in 2.0 to 4.3 s, while in set sM1-04-22-2024 they
match throughout. Each file holds one LFP trace, "Segment 0 LFP 0", with no
electrode position, where the model records 11 electrodes at 200 to 1200 um
depth, so which electrode it is cannot be told and the mean over electrodes
cannot be computed. The single-cell current-injection simulations behind the
64% decrease in PT5B excitability are not in the dandiset. sub-001/sub-001.nwb
is the same blob as sub-001/sub-001_ses-sM1-04-22-2024-01.nwb. The files name
the bioRxiv preprint as their related publication, the dandiset lists no
related resource for the published paper, and the archive's summary gives
"spike sorting technique" as the measurement technique of a simulation, with
"Units" as the only variable measured. Of the paper itself, the Results report
a significant increase in PT5B rate from control to parkinsonian in the
activated state (p < 0.001), while the Discussion says there was no
significant change; counting all PT5B cells three tests give p below 1e-06 and
the Mann-Whitney test 0.0052. Questions are put to the paper's authors: over
which cells a population's mean rate is taken and which test gave the rate
p-values, on which eight IT outcomes rest; which PT5B cells and definition gave
1% to 3% of spikes coincident and the unitary-event durations, since over all
1,435 PT5B cells nearly every spike has another within 1 ms; how LFP bursts
were defined, with which spectrogram parameters and electrode, and whether the
spike count histogram was smoothed for the duty cycle; whether "highest spike
rate of any neuron population" covers interneurons; and how subthreshold
oscillations were detected and over which cells the 57.4% is taken, 57.4% of
20 not being a whole number.

The author's points on the protocol: it does not say what to do when the data
show a reading the claims file missed that matches the paper exactly, and a
reader was asked while the outcomes were kept on the file's readings; the
rest-beta-power criterion gives no outcome for a ratio above 31.6, and
partially reproduced was chosen with the reason recorded; there is no rule for
readings the dataset cannot support, such as the mean over 11 electrodes, so
the readings that could be run were run and a deviation recorded; when a
result shows the paper's procedure must differ (100% coincident against 1%),
the protocol only says `methods_underspecified` for chance levels, and not
reproduced was recorded with a question for the authors; and to learn the
questions-file format the author opened `questions/000005.yaml`, outside the
files the prompt pointed to.
