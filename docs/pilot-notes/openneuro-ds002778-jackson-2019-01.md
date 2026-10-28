# openneuro-ds002778, Jackson et al. 2019

Nine claims reproduced, nine partially and six not reproduced, with none
blocked, all on the dataset. It pins version 1.0.5, the latest snapshot, which
holds 46 BDF files at 512 Hz from 15 patients with Parkinson's disease recorded
off and on medication and 16 controls; the paper cites no snapshot, and the
change log shows no change to the EEG files across snapshots. The paper, in
eNeuro, measures the sharpness and steepness asymmetry of beta waveforms and
beta to gamma phase-amplitude coupling (PAC) in resting scalp EEG, and reports
that all three are higher off than on medication at C3 and C4, with mu/alpha
results in Tables 1 and 2 and the shape quadrants of Figure 4. The claims were
written from the version of record in Europe PMC (PMC6553574) and from the
paper's code at SwannLab/Jackson_2019 commit a7c89f50, which starts from
preprocessed MATLAB files that are not public, so every measure was computed
from the BDF files with the Methods' preprocessing. The off against on tests
of shape and PAC, the bipolar and temporalis controls, the topographies, the
off against control tests with the average reference and with CSD, the UPDRS
change, the spectral peaks of Figure 1C, the alpha tests of Tables 1 and 2,
the correlations of Figure 3, the Q4 counts and the effect sizes of Table 3
were tested. The three main off against on tests hold after FDR correction
but each has one value outside tolerance: sharpness d 0.73 against 0.86 +/-
0.086, steepness W 16 against 9 +/- 0.9, and PAC W 13 or 12 against 15 +/- 1.5.
`offctrl-steepness` and `table2-alpha-offctrl` are not reproduced, as z and d
are within tolerance but the FDR corrected p is 0.0531 under every filter
reading, and Holm, Bonferroni and Benjamini-Yekutieli are further from 0.05;
`offctrl-pac-csd` is not reproduced (p = 0.075 against 0.022), and no spline
variant reaches 0.05; `fig1c-beta-alpha-peaks` is not reproduced, as only the
controls' mean spectrum has both peaks; `table1-alpha-pac-null` is not
reproduced, as the null holds under two of the three phase filter readings;
and `q4-patient-counts` gives 10, 10, 7 and 13 against 9, 8, 8 and 9 (+/- 1).
`updrs-improvement` gives the paper's W = 3.5, p = 0.0033 exactly. The author
asked a reader no questions, so the answer run changed nothing. Round 1 gave
its own outcome for each claim and agreed with 21 of 24; the author took its
outcomes for `offctrl-steepness` and `table2-alpha-offctrl` (from partially
reproduced to not reproduced) and `table1-alpha-pac-null` (from reproduced,
resting on an assumed 192-tap filter, to not reproduced), and its points led
to the correction procedure sensitivity, CSD spline variants, a PAC variant
that drops the filtered edges, per-patient Q4 values and variants without
sub-pd6 and sub-pd16. Round 2 agreed with all 24, so there was no third round;
it found statements the outputs did not support, among them a summary calling
the statistics close to the paper's, a 5% that is 5.1%, and pd9 listed among
the near-axis points that decide Q4 membership where pd5 and pd11 do, and
these were corrected. Two questions were put to a reader, on whether the
expected statistic counts in `fig2-pac-off-on`, whose criterion contradicts
itself, and on the missing partial clause of `pac-beta-larger-than-alpha`;
both are unanswered, as they were added after the answer step. Some outcomes
rest on weak ground: `fig2-pac-off-on` would be reproduced if the criterion's
last sentence governs; `offctrl-pac-csd` uses MNE's spherical spline on the
BioSemi 32 template positions, not compared with the MATLAB CSD toolbox; and
in `q4-patient-counts` 16 of 60 points lie within 0.01 of an axis. The
author's run took about 26 minutes and its only failure was a YAML colon-space
in the attempt record, which was fixed; the notebook ran in 100 s at first and
133 s in the last run.

The manual artifact marks and the list of excluded noisy electrodes that the
paper's preprocessing used are not in the dataset: every channels.tsv marks all
channels good, the events files hold only a start trigger, and the paper's code
loads the marks from rejectscombined.mat, which is not public, so all analyses
ran without rejection; round 2 judged this the likely cause of the
out-of-tolerance W and d values and of the Q4 count gap. The sub-pd16 ses-on
recording, which participants.tsv says was exported from a preprocessed EEGLAB
file, has electrode standard deviations about six times those of every other
recording after the same preprocessing (median 62.6 uV), about 100 times their
power, and no alpha peak; its channels are not average referenced, and the
dataset does not say how it was processed or scaled. The sub-pd6 ses-on file,
also exported from EEGLAB, is average referenced and lasts 289 s. Without
these two patients the steepness and PAC correlation falls within tolerance
both off and on medication. The questionnaire fields of the beh JSON files
(Total UPDRS, UPDRS 18-26 and others) have no description, so "Total UPDRS"
was taken as the motor examination from its values, which exceed "UPDRS 18-26"
by 1 to 14. The events files hold one trigger (value 1) a few seconds into
most recordings, and other values in sub-pd16 ses-on (130817) and sub-pd17
ses-off (a second 65536), and what the trigger marks is not described. The
dataset holds no digitized electrode positions. The paper gives no filter
length for the mu/alpha phase filter of PAC, and alpha PAC off against on is
not significant after FDR correction with 192 or 231 taps (0.061, 0.078) but
is with 118 samples (0.036); this is put to the paper's authors. Table 2 gives
FDR corrected p = 1 for three tests where Benjamini-Hochberg over its six
tests gives about 0.36, and Table 3 gives d = 0.75 for PAC in all patients
where Table 1 gives 0.83.

The author's points on the protocol: it gives no rule for a result that falls
in a case the criterion does not name, as for the two Table 2 steepness claims
with z and d in tolerance and corrected p 0.053; it is unclear which governs
when a criterion's last sentence names fewer values than its expected list;
the clock check does not apply to continuous rest data with no trial table, so
the Status channel was checked against events.tsv instead; it does not say
what to do when a reading the claims file names has no data, as the dataset's
own artifact marks here; and step 1.6 does not say how to choose among
readings when two of three agree.
