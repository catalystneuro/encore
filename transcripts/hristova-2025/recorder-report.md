I added the 001888 row to README.md and appended the subsection to `docs/pilot-notes.md`. Nothing is committed. The README row reads 13 reproduced, 9 partially, 2 not reproduced and 10 blocked. Here is the subsection:

### 001888, Hristova et al. 2025

Thirteen claims reproduced, nine partially, two not reproduced and ten blocked
on the dandiset. Round 1 had no attempt record and gave its own outcome for
each claim from the notebook with its conclusion cells and summary removed, and
agreed with all 34. It found that reading (i) of `figs5b-transition-percent`
judged an SWD initiated in NREM on the one epoch before it, where the
Supplementary Methods use the six epochs before, and that rule gives 22.93%
against 24.2 ± 2.42. The author corrected the criterion, recording that this
was done after the analysis had been seen, and changed the outcome from not
reproduced to reproduced (the first rule gave 36.31%); the reason for blocking
`fig2e-swd-delta-power` and `fig5a-het-more-nrem-swds` went from `other` to
`data_missing`, as the verifier gave. Round 2 agreed with all 34, including the
change, and nothing was proposed, so there was no third round. The paper, in
Epilepsia, records EEG and EMG from Grin2b+/- and wild-type rats, and reports
that Grin2b+/- rats have more spike-wave discharges (SWDs), mostly in wake and
at wake-NREM transitions, less REM sleep in fewer and longer bouts, less time
awake, higher NREM beta power and lower wake power, and that ethosuximide given
systemically or into the reticular thalamic nucleus reduces SWDs. The number,
duration, timing, sex dependence and spectrum of SWDs, the amount and bouts of
each sleep state, the state spectra, the states in which SWDs start and the
correlations of SWD time with sleep measures were tested; the western blots,
development measures, scorer validation and the four pharmacology claims are
blocked as `data_missing`, and fig2e and fig5a-het-more-nrem-swds because only
one wild-type rat has SWDs. `fig4b-nrem-beta` (Het beta lower by 0.078) and
`fig4c-wake-power` (Het higher on average, +0.081) are not reproduced. Some
outcomes rest on weak ground: `fig3d-rem-hourly` and `fig3g-rem-total` give p
= 0.048 and drop to p = 0.060 without GRIN2B-228, a Grin2b+/- rat with 1 SWD
per day, without which `fig5c-transition-swds` (13 of 13, p = 0.0095) and
`fig5def-no-other-correlations` would meet their criteria; and the wake
results depend on whole SWD epochs being taken out of wake, so that with the
stored scores the wake bout differences reverse and `fig5f-swd-wake-correlation`
gives R = -0.06 in place of -0.81.

The dandiset was converted by CatalystNeuro
(catalystneuro/gonzalez-sulser-lab-to-nwb). It holds 2 of the paper's 9
analysed wild-type rats (14 or 15 of its 15 Grin2b+/-), so genotype comparisons
rest on two wild-type rats, one of which (GRIN2B-238) has no SWDs, and it does
not say which of its rats the paper analysed; GRIN2B-132 has no genotype and
sex U, which the conversion repository marks as still to be confirmed by the
lab. The pharmacology and intrathalamic infusion recordings, western blots,
development measures and the visual scoring used to validate the scorer are
not in it, and the paper says raw data are available on request. The
processed tables are misdescribed: the `sleep_states` description gives code 4
for SWD epochs, but no file holds it; `swd_epoch_counts` holds the scorer's
flags (6 for an SWD epoch, 4 otherwise) and not counts, and the flags cover a
median of 51% (0 to 73%) of the epochs SWD events overlap, mostly the last
epoch of each SWD; in `seizure_totals_by_zt` the per-hour counts are in
`spike_wave_discharge` while the two count columns hold the day's total in the
first row; and `sleep_state_power_spectra`, described as a baseline-corrected
PSD, holds the scorer's mean log10 multitaper amplitude referenced to each
frequency's 5th percentile. The raw EEG and EMG are stored as unsigned 12-bit
codes with offset 0, so every channel reads about +8 mV of DC, and signal loss
is written as 32767, undocumented; 21 to 73% of 5-s epochs per rat in the
windows read contain such samples (73% for GRIN2B-238). The Methods exclude SWD
times from the sleep states while the lab's scorer replaces only the flagged
epochs, and the paper's wake results depend on this. Other findings: the
dandiset has no published version, and the attempt pinned the draft as
modified 2026-07-31 09:37 UTC; the assets summary counts 16 files and 16
subjects where the draft holds 17; the dandiset does not record which EEG and
EMG channels the lab chose by eye for scoring; the paper does not give its
band limits, Welch segment length, bout definition or transition rule, and
neither linked repository holds the statistics or figure code; and the Figure
5 legend gives statistics that contradict each other (NREM time T = -1.47 with
R = -0.13 and df = 13, which implies T = -0.47), while the Figure 3 legend
reports no net wake difference next to a genotype effect on hourly wake time
(F = 7.14, p = 0.014).

The notebook ran in 278 s in the first clean run and 246 s after round 2. The
author first opened only GRIN2B-132 and took genotypes from the conversion
repository, then switched to the genotypes in the other 16 files and to SWD
epochs taken from the events before reading any claim output, though a first
run had executed the claim cells; a bug in the SWD peak rule was fixed before
the conclusions were written and changed fig2d's outcome. Round 1's points led
to runs without GRIN2B-228, GRIN2B-238 and both for every genotype test, a
fitted mixed model that matched the split-plot ANOVA, and checks of spectral
coverage, the slope rejection and a cleaner channel, none changing an outcome
beyond figs5b. Round 2 found statements the outputs did not support, among
them that the paper's 59.97 min of SWDs does not fit the scorer's flags, which
give 60.2 min, and a run time of about six minutes, and these were corrected.
The author's points on the protocol: no published version, where the protocol
allows a draft only for repeat attempts; opening one file, which is not enough
to find metadata held across all files; whether criteria may be revised after a
run that executed the claim cells; Methods and the lab's code that disagree on
SWD epochs, where the data show the code's input is incomplete; no minimum group
size for blocking a claim; claims of no difference tested with two wild-type
rats; one claim spanning eight tests under a binary absence rule; a variant
that matches but cannot rescue a claim; trading fidelity to the Methods'
spectra for speed; and method choices the paper leaves undefined.
