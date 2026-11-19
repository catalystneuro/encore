I wrote the two new files and changed nothing else; nothing is committed. The summary is 115 words.

One thing needed a call. The `catalystneuro` field for 000218 names a contributor ("contributor Baker, Cody of CatalystNeuro"), not a repository. So I opened the dataset paragraph the way `tingley-2019-01` and other notes do when only a contributor is listed.

The record also contradicts itself on waveforms. One finding says units in the DT5, DT7 and DT9 files have no waveform. The reconciliation's own check found waveforms for 5968 of 6236 units, including files from those animals, and left the finding as it was. The notes report both statements.

`docs/pilot-notes/tingley-2019-02.md`:

# tingley-2019, Tingley et al. 2019, second attempt

Nine claims reproduced, eleven partially, nine not reproduced and nine
blocked on the dandiset; `fig8-model`, the network model in the paper's
code (`data: elsewhere`), was not attempted for time and is counted apart.
Seven outcomes rest on an assumption. The first verification round agreed
with 37 of the 39 outcomes; it gave reproduced for
`fig1c-post-burst-suppression` and partially reproduced for
`ls-spikes-not-locked-to-ca1-ripples`, the author kept both with the
disagreement recorded, and the second round agreed with all 39, so there
was no third round. The paper, Tingley and Buzsaki, "Routing of
hippocampal ripples to subcortical structures via the lateral septum"
(Neuron 105, 138-149), reports high-frequency oscillations (HFOs) in the
lateral septum (LS) of rats, their relation to LS firing and to CA1
ripples across sleep and waking, LS correlations around behaviour, which
ripple features predict LS firing, optogenetic HFOs and a network model.
The HFO counts, durations, frequencies and lag behind CA1 ripples, their
NREM preference, the excess correlations and their temporal bias reproduce
on the lab's deposited detections, phase locking, compression, state
coupling and the Figure 7E predictions of LS firing reproduce in part, and
confinement to LS, participation, ripple-triggered firing and the absence
of CA1-LS phase coherence do not; depth within
LS, travelling waves and CA1 neuron depth are blocked as
`metadata_insufficient`, the optogenetic HFOs as `data_missing`, and
replay, seqNMF, the content-independent comparisons that depend on them
and the model as `other`, not attempted in the run's five hours. This
attempt pins 0.261110.1911, a re-conversion whose release notes say it
fixes problems found by a reproduction attempt (issue #82); the author read
those notes to choose the version, did not open the issue and saw none of
`tingley-2019-01`'s outcomes, and the reconciliation records the attempt as
blind. A reader rewrote the claims file under the current rules (39 claims
against 31), adding the paper's sample sizes as expected values. Of the
outcomes that changed, `fig1c-hfo-each-animal`, `fig1g-slower-than-ripples`,
`fig5b-nrem-and-rates` and `fig5d-lag` moved because the new version holds
the lab's events (the earlier median lag of 0.00 ms came from its own
same-sample detections, against 6.20 ms now), five Figure 4 and 5 claims
moved with the rewritten claims file, and `fig1h` turns on whether the
amplitude is the stored peak normalized power (r = -0.000, p = 0.96) or the
maximum NSS recomputed from the LFP (r = 0.081, p = 1.3e-38). After round 1
`fig5e-state-coupling` moved from not reproduced to partially reproduced on
the pooled reading (NREM 0.302 against WAKE 0.091), and the block reason of
the two content-independent claims became `other`; round 2 asked that
`dataset-composition` be marked assumed, since without the attempt's two
choices only 3 of 6 counts are within tolerance. The author's final run
took about 76 minutes, 45 of them for the LFP notebook, with peak memory
about 7.4 GB, and no job failed; in the round-1 revision the LFP notebook
took 51 minutes, which needed pilot-13's 60-minute limit.

The dataset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is
a contributor). Electrode positions are not stored, nor the probe model of
each recording, nor the estimated relative depth of each recording within
LS, so travelling-wave speeds, CA1 neuron depths and Figure 2E, F cannot be
computed; session names carry drive depths only. The two rats of the
optogenetic experiments, with their light stimulation times and waveforms,
are not in the dandiset, whose 98 files hold six rats (DT1, DT2, DT5, DT7,
DT8, DT9). This version holds the lab's detections, LSRipples in 77 files
(27014 events) and CA1Ripples in 47 (101217), made with parameters that
differ from the Methods (LS 120-180 Hz, durations up to 100 ms, peak
thresholds of 4 to 6 SD in some files, against 120-200 Hz, 15-250 ms and
5 SD; CA1 130-200 Hz), as the files' descriptions say; their counts,
durations and frequencies match the paper's (27014 LS HFOs, 27.8 ms,
147.6 Hz). The DT9 CA3 recordings have no CA1 ripple table, DT7 20170410
has 61 LS units but no LS HFO table, and DT2 20160215-122710 has 37 LS units
and no event table at all. The lab's LS and CA1 detection channels share a
120-200 Hz signal outside any event (median phase-locking value 0.177 at
random times in 45 recordings, against 0.024 with the CA1 phase taken 1 s
later), and the files do not say how the channels are referenced. Most
hippocampal units are labelled `hpc`, so CA1 and CA3 cannot be told apart
reliably: 10 recordings have units labelled ca3 and 19 a ca3_channel flag,
against the paper's 25 CA3 recordings. The PRE, BEHAV and POST periods are
not marked and were taken from the first and last trials, and under the
claims file's inclusion rule only 361 to 503 pairs pass, against 7172 in
the paper, as the pairs are lost in the HFO epochs. On the septal shank of
the DT7 recordings the region labels ls, ms, acg and cc alternate along the
channel order, four DT7 files label all 128 electrodes "unknown", and the
36 units of DT7 20170407-936um-1152um-merge have an empty region label. In
three files less than half of the trial time is scored WAKE (12.5%, 20.3%
and 31.6%). The record says the units hold at most one waveform, none in
the DT5, DT7 and DT9 files listed; the reconciliation's check finds a
32-sample waveform for 5968 of 6236 units, including DT5, DT7 and DT9
files, and left the statement unchanged. Of the eleven earlier findings,
one is fixed (spike times out of order), four partly fixed (event tables,
units without a region, CA3 files without a CA1 channel, waveforms and
quality metrics) and six still present. The paper's repository holds the
scripts of the 2018 paper and the Figure 8 model, not the analyses of
Figures 1 to 7, and the paper gives the HFO band as both 120-180 and
120-200 Hz and cites wrong figure numbers in its Methods. Questions are put
to the paper's authors on the normalization and pair inclusion of the
Figure 4 correlograms, the window of the post-burst suppression, the test
of LS locking to CA1 ripple waves, the epoch boundaries, the Figure 1H
amplitude and whether the Figure 5E fraction is pooled.

The author's points on the protocol: the time rule names only `too_large`,
so claims not attempted within the five-hour limit were given `other`; the
60-minute limit per notebook forced analyses of the whole dataset into
several notebooks, each reloading the data; five seeds did not fit for the
Figure 7E Poisson fits or the fig5f jitter; result cells must rest on
printed numbers that exist only after the run, so they were added after the
first full run and the entry re-run; an expected pair count beside an
absence criterion that does not use it was judged partially reproduced;
and absence claims whose paper names no test had nothing for the rule to
apply to.

`summaries/tingley-2019-02.md`:

Most findings on lateral septum (LS) high-frequency oscillations held up on the lab's deposited detections: they are shorter and slower than CA1 ripples, occur mostly in NREM sleep and follow CA1 ripples with the reported lag. LS neurons lock to the oscillation trough, but fewer than reported (60.6% against 92.5%), and ripple features predict LS firing above chance, not at the paper's rates. Confinement to LS and stronger ripple-triggered LS firing in NREM sleep did not reproduce; the first rests on site labels that alternate along the septal shank. Travelling waves, depth within LS and optogenetic induction could not be tested, as electrode positions, depth estimates and the optogenetic rats are not in the dataset.
