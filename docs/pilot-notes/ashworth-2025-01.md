# 001708, Ashworth et al. 2025

Twenty-eight claims reproduced (nine on an assumption), three partially, three
not reproduced (one on an assumption) and none blocked. The first verification
round agreed with 29 of the 34 outcomes as they stood and the second with all
34; nothing was proposed after the second, so there was no third round. It pins
version 0.260604.1023, the version the paper cites and the only published one.
The paper, Ashworth, Martenson, Shi, De Preter, Heinricher and Mancini,
"Multi-timescale dynamics organize descending pain modulation", a bioRxiv
preprint (the dandiset's record gives it the title of its code repository,
"Multi-timescale Rhythmic Dynamics in Rostral Ventromedial Medulla Neurons"),
records ON, OFF and NEUTRAL cells in the rostral ventromedial medulla of lightly
anesthetized rats, in an evoked protocol with heat trials about every 5 min and
an ongoing protocol with about 30 min of unstimulated activity, fits Bayesian
piecewise models to the responses at paw withdrawal and heat onset, finds a
rhythm near 300 s in spike-train spectra and periodic Gaussian-process (GP)
fits, and relates the cells to heart rate; the dandiset holds 101 assets (0.09
GB) of spike, heat-onset, withdrawal, pinch and EKG beat times. The claims were
written from version 4 of the preprint, from a PDF supplied by a person, with
its supplement, and from the paper's code
(nox-lab/multi-timescale-rhythmic-dynamics-in-rvm-neurons at e12f3ee), whose
stored period scan and GP fits were used as reference values only. The check
made the -10 s window start of fig1c-psth-counts a second reading, made the
Methods' full recording period the main reading for NEUTRAL cells in fig5b, set
the NEUTRAL bound of fig4-nlml-minima to 4 cells and added a claim,
`fig5d-phase-profiles`, among other changes, and left open the tests and bounds
of fig3d, figs3, figs2 and fig5d, which the paper judges from plots, the animal
counts on which the Methods and Table S11 disagree, and the partial rule of
fig6c. Every claim could be tested, except the withdrawal temperature of
`methods-withdrawal-latency`, as the files hold no temperature series. Reproduced are, among others, `dataset-composition` (104 cells in 53
animals and 62 in 30, exact), `fig1c-psth-counts` and `fig2-trial-counts`
(within 10%, and exactly the paper's 185, 155, 182, 151 and 195, 170, 197, 172
without pinches), `fig3e-cv-isi` (all six values to the third decimal),
`fig2c-on-time-constants` (0.656, 4.231 and 164.8 s),
`fig2h-off-linear-exponential` (5.08 above the double exponential, dse 3.56;
2.64 without pinches against the paper's 2.4), `fig1c-withdrawal-locked` (8.693
and 11.717 s without pinches against 8.694 and 11.718),
`methods-heart-rate` (397.1 +- 34.2 bpm) and the eight GP claims other than
fig5b-train-no-difference. Partial are `fig3bc-psd-peaks` (periods 286.86 and
298.33 s exact, FWHMs 90.2 and 102.7 s against 16.92 and 16.12),
`fig4-nlml-minima` (25 of 25 ON and 23 of 25 OFF cells have a minimum near 300
s, but so do 25 of 32 NEUTRAL cells against at most 4) and
`fig6c-coherence-counts` (3, 6 and 9 against 5, 4 and 8, OFF 3 away at other
surrogate seeds). Not reproduced are `tables9-s10-sigmoid-over-erf` (the erf
model with linear recovery is higher, as in the paper's own notebook 29),
`fig6d-heart-rate-peaks` (the highest peak below 0.01 Hz at 1243 s on segments
and 2486 s over whole recordings) and `fig5b-train-no-difference` (on whole
recordings ON against NEUTRAL has corrected p 0.036 and Kruskal-Wallis p 0.034;
on the code's 1500 s segments Kruskal-Wallis gives 0.098, the paper 0.117). The
nine GP outcomes rest on the code's settings (100 inducing points, p_noise 0.01,
5000 iterations), which match the stored fits cell by cell (Spearman r 0.95 to
1.00), and `fig5b-test-r2` would be partially reproduced with the criterion's
same-likelihood null (NEUTRAL p 0.052); fig3d rests on a 10% prominence
threshold (it holds at 10% and 20%, not at 5%). The author's first run had 27
reproduced (17 on an assumption), 4 partially and 3 not reproduced. The author
asked a reader whether figs3 should use only 32 NEUTRAL cells; the answer
amended the criterion to the NEUTRAL units of the 'evoked/ongoing' and
'ongoing' files (Table S11's 20 + 12), and the author-answers run moved
`figs3-neutral-unmodulated` from partially reproduced (36, 76, 77) to
reproduced (32, 67, 68). Round 1 disagreed on fig1c-withdrawal-locked,
tables3 and recovery-timing (partially reproduced) and on fig2h and
figs1-completion (not reproduced), all resting on OFF fits that did not
converge on its machine, and found that the with-pinch trial set had been made
the main reading though the set without pinches gives the paper's counts, that
the Methods' GP settings were not run and that the null GP takes a different
contamination range; in reply every chain was started at the best of nine
optimizer runs, after which all fits but one converged, every model was fitted to
both trial sets (without pinches the ELPDs match the paper's notebooks to within
one unit), the five outcomes stayed reproduced with the disagreements recorded,
the assumption flag was removed from eight OFF claims, the Methods' GP settings
were run as a 2500-iteration variant (10000 iterations would take about 92
min) and the fig3bc FFT resolution and FWHM and the fig6d peak rule went to a
reader in `questions/001708.yaml`. Round 2 agreed with all 34 outcomes but
found that the evoked Result cells and the record's model numbers came from an
earlier execution than the one delivered, that OFF_erf_linear_np did not
converge in its execution (r_hat 1.393), and wrong statements for
fig5b-train-no-difference, fig3d and the runtimes; in reply the author found
that the fits repeat exactly on one machine at fixed seeds but differ between
machines and said so, added a convergence column and refits at target_accept
0.95, matched the stored NEUTRAL fits to the code's segments and sent whether
fig5b-train-no-difference should take them to a reader. In both revision runs
the single `entry.py all` call was killed at the 2-hour command limit during
gp_methods.ipynb, which was run on its own with nbconvert (cut from 5000 to
2500 iterations in the first), and in the second the author wrote `result.json`
by hand. During development float32 GP fits were not positive definite and the
first lock failed on numba with numpy 2.5; both were fixed and the final run
had no failures. The notebooks ran in 65 min at first (evoked 12, ongoing 23,
GP 29), about 27, 27, 35 and 27.6 min after round 1 and 31.8, 27.1, 36.7 and
25.6 min at the end.

The paper's training pseudo-R2 result depends on which NEUTRAL data were
fitted: the Methods say the full recording period of every NEUTRAL cell, but the
code's stored fits of the 12 NEUTRAL cells of the ongoing files match fits on
the code's 1500 s segments (median relative difference of the null log
likelihoods 0.0003) and not on whole recordings (1.28), and Kruskal-Wallis p is
0.098 on segments and 0.034 on whole recordings. The GP settings differ between
the Methods (200 inducing points, p_noise 0.001), the code (100 inducing
points, p_noise 0.01, params.json 10000 iterations) and the saved fits (5000
iterations, noise_prob 0.01), and the code's null GP takes its uniform
contamination over 0 to the cell's largest training count where the periodic
model's runs over 0 to 200, so the pseudo-R2 compares two likelihoods. The code
builds its trial-exclusion events from "Keyboard" while its NWB loader renames
the pinches "keyboard", so pinches never truncate a trial, though the Methods
exclude trials truncated by the next event; the paper's trial counts are
reproduced exactly only without pinches, and with them they are 2 to 5% lower.
The Methods give the OFF priors on k and k2, the code on log k and log k2; both
reproduce Table S7 once the chains start at the posterior's main mode, but from
PyMC's default start, as the code samples, chains of the Methods-prior fit stay
in a local mode about 240 log-posterior units lower and the result depends on
the machine. The text says a Gaussian CDF fits OFF cells significantly worse
than the sigmoid, while the fits here and the paper's notebook 29 give the erf
model with linear recovery a slightly higher ELPD (here by 0.42, dse 1.79, with
pinches and by 0.88, dse 1.76, without). No reading gives the spectral FWHMs of
16.92 and 16.12 s: widths at half height give 84 to 106 s, the code's
peak_widths call uses the index within the masked band and gives 8 to 10 s, and
the supplement's rat-level bootstrap gives 58 to 98 s. The four NEUTRAL units of
'evoked' files (sub-rat-6, 7, 9 and 15) are named "NEUT" and the other 32
"Neutral", and the code selects by "Neutral", which agrees with Figure S3's n =
32. Table S11 gives 35, 18 and 50 animals for its three sets, where the dataset
has 35, 18 and 30, matching the Methods' 53 and 30. The EKG beat series hold
20546 inter-beat intervals under 50 ms (of 1105713), double detections that
raise the mean heart rate per recording from 392.4 to 397.1 bpm, and the 11
'evoked' files of sub-rat-25 to sub-rat-35 hold no EKG. The pinch events carry
labels that are not described ('ignore', 'l_hpaw_onset_approx',
'tail_release_post_pinch_slip' and others, some with a leading space). Four ON
cells in two files (sub-rat-70 ses-1, sub-rat-72 ses-1) have 228.6 and 226.5 s
between the preceding heat onset and their 1500 s ongoing segment, under the
Methods' 230 s. The archive lists 83 subjects, 77 male and 6 female, as the
Methods say, and no recording is deposited twice. Questions are put to the
paper's authors: which OFF prior was used and how the chains were started; how
the FWHMs were measured and converted to seconds; and which GP settings
produced the reported results.

The author's points on the protocol: it does not say what to do when a
criterion's main reading is too large to run but a variant fits the limit, so
the code's GP settings were run and marked assumed, with an estimate for the
Methods' settings; a 65-minute run left no time to re-run after writing
conclusions, so the markdown-only Result and Summary cells were inserted into
the source and executed notebooks after the run; there is no rule for MCMC fits
that do not converge, so a sampler-setting variant was used as an assumption;
"compare identity, not spelling" conflicts with a paper whose code selects by
spelling, so the rule was applied (36 cells), the paper's 32 shown as a variant
and a reader asked; it is unclear whether the code's stored outputs count as
`inputs`, so they were listed as inputs used only as reference values; and
there is no guidance on platform-specific packages, as CPU-only torch needed a
direct wheel URL and numpy had to be pinned below 2.4 for numba.
