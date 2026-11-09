I wrote the note in `docs/pilot-notes/crcns-ia-1-eyherabide-2008-01.md` and changed no other file. `targets/dandisets.json` lists only DANDI datasets and has no entry for CRCNS:ia-1, so it has no `catalystneuro` field to report and the second paragraph does not open with the CatalystNeuro sentence. The claims file and the reports I was allowed to use say nothing about the claims check, so the note leaves that check out. Nothing is committed.

# crcns-ia-1, Eyherabide et al. 2008

Eleven claims reproduced (ten on an assumption), five partially (all five on
an assumption), seven not reproduced (three on an assumption) and three
blocked, all three for missing data. The first verification round agreed with
25 of the 26 outcomes as they stood and the second with 25; one change of
outcome was proposed after the second, and a third round agreed with it. CRCNS
does not version data sets, so the version is recorded as unversioned and the
zip is pinned by the MD5 in `checksums.md5`, which the helper checks against
the S3 ETag. The paper, Eyherabide, Rokem, Herz and Samengo, "Burst firing is a
neural code in an insect auditory system" in Frontiers in Computational
Neuroscience, records auditory receptor axons in the tympanal nerve of
Locusta migratoria intracellularly, 37 cells from 23 animals stimulated with
Gaussian amplitude-modulated tones in seven protocols, identifies bursts from
the spike-train correlation function and measures what bursts of each length
encode; the data set holds Data1 (2003), which its description names as
analysed in this paper, with the stimulus files, and Data2 (2004), unpublished.
The claims were written from the version of record in PubMed Central
(PMC2525941) as Europe PMC XML, without a PDF, so values shown only in figures
could not be read; the paper has no supplement and links no code. The burst,
correlation, information and burst-triggered average claims could be tested;
`threshold-population` and the two model claims could not, as Data1 holds no
threshold s_TH. Reproduced are `firing-rate-uniform` (107.1 Hz, SD 14.5 Hz,
ANOVA p = 0.814), `fig5-burst-probability-vs-stimulus` (P(n = 1) lowest at
100 Hz and 12 dB), `fig3-correlation-shape`, `method-correlation-error`
(2.63% of the span of C_s), `fig6-bursts-less-correlated` (ratio 1.99),
`fig7ef-jitter-independent-of-n` (86.9% of 61 sessions),
`fig8-latency-decreases` (5.80, 4.23, 3.32 and 2.67 ms),
`sigma-n-below-sta-sigma` (98.1%, ratio 1.596), `fig9-nbta-not-concatenated-1bta`,
`fig9c-population-nbta` (3.13, 7.03 and 8.46 dB over 7 sessions from 7
distinct cells) and `firing-rate-no-effect-on-limit`. Partial are
`data-sessions-and-trials` (37 cells, 23 dates, 503 most trials, mean 160.3
and SD 6.48 Hz match; 115 kept sessions and 69 fewest trials do not),
`fig7ab-information-per-burst-increases` (mean slope 2.22 bits, significant in
63 of 64 sessions), `fig7cd-occurrence-decreases` (-2.82, significant in 63 of
64), `direct-method-comparison` (R = 0.967, but 10.2% lost and the direct
method higher in 74 of 89) and `fig8-nbta-differ` (the ANOVA holds in 53 of
53, the time-domain count is 38 against 50 +/- 5). Not reproduced are the
three Table 1 count claims, `table1-isolated-spikes` (4 of 7 within
tolerance), `table1-burst-length` (8 of 19), `fig7gh-information-rate` (slope
-46.5 bits/s, 35.5% carried by bursts with n > 1), `fig8e-sigma-minimum`
(2.37 ms against 0.4 +/- 0.7) and `fig10-burst-n-vs-height` (7 sessions,
10.9%). Most outcomes rest on two assumptions: the first peak of C_s taken as
its largest value below 5 ms, as the first local maximum falls on the
refractory plateau, and a main population, selection (c), of 89 sessions that
leaves out sessions under 98 trials and those sorted off-line. The author's
first run gave the same outcomes except that `table1-isolated-spikes` was
partially reproduced, and it used the 115 sessions of selection (a). The
author asked no questions of a reader, so the answer and author-answers runs
changed nothing. Round 1 disagreed on `table1-isolated-spikes` and found that
115 sessions were kept against 86 with no exclusion tried, that the nBTA
maximum was searched up to +15 ms, giving a negative mean tau_4, that the
minimum of two bursts per n was not stated, that sigma_n could be biased by
sample size, that the plug-in information had no shuffle control, and that the
fig10 counts were identical under both widths T; in reply the exclusions were
tabulated and selection (c) adopted, which made `table1-bursting-sessions`
partially reproduced, `table1-isolated-spikes` became not reproduced, the
maximum was searched before onset, results with 20 and 50 bursts, a
size-matched control (94.3%) and a shifted-onset baseline were added, and a
peak reading after the plateau (61 of 89 bursting) was added. Round 2
disagreed on `table1-bursting-sessions`, as selection (c) was fitted partly to
its own expected values, and found sentences the outputs did not support (all
of `data-sessions-and-trials` within tolerance under selection (c), which comes
from 29 cells on 18 dates, the rise of I_n(1) called estimator bias, and the
spike-triggered average peaking before the spike in every session); in reply
the text was corrected, the 17 tau_n values on the 0 ms edge were printed, and
the change to not reproduced was proposed, which round 3 accepted. The
author's run went from 18:18 to about 19:00 UTC; two development runs failed on
bugs that were fixed (an array size and a plot-range count). The notebook ran
in 248 s at first, 358 s after the author-answers run, about 9 minutes after
rounds 1 and 2 and 410 s at the end. The untracked files in the repository root
were left alone.

The paper keeps 86 of 132 sessions by a trial-to-trial rate SD below 35 Hz and
a rate near 100 Hz, but in Data1 the SD rule keeps 115 of the 116 sessions of
the paper's seven protocols, and nothing marks which sessions the paper kept;
leaving out also the 9 sessions with fewer than 98 trials and the off-line
sorted sessions keeps 89, with 47, 6, 7, 7, 8, 7 and 7 per protocol against
Table 1's 43, 6, 7, 7, 8, 7 and 8, which suggests the paper used only on-line
sorted sessions, though the paper does not say so. Data1 holds no threshold,
best frequency or f-I measurement, though the paper's model uses the measured
threshold and the descriptor says the best frequency was determined from f-I
curves. Data1 does not record the animal, so the paper's 23 animals can be
matched to the 23 recording dates only by assuming one animal per date, and two
experiments (03-01-15-aa, 03-06-27-ae) are missing from singlecells.txt. 28
sessions use the stimuli gaussModality_co200 and lmd_co200 and 6 use cutoffs of
50 and 1600 Hz, which the descriptor does not describe and the paper does not
use. 28 sessions sorted off-line have no header, so their target rate and pause
are not recorded, and in 25 of them each trial block runs on into the pause
(spikes up to 2.76 s). The file Data1/firing_rates is not described, and its
+/- value of 57 to 189 Hz is not the trial-to-trial SD of the rate. The
descriptor gives 98 to 533 trials, where the files hold 69 to 503; the
intensity in three trial headers differs from cell.dat by more than 1 dB (up
to 6.6 dB), and six sessions of 03-01-30-ad, 03-02-25-ac and 03-02-25-aj had
450 ms pauses where the paper states 700 ms. The paper counts bursting
sessions three ways, 63 with n > 1 in Table 1, 59 bursting cells for Figure 7B
and 58 bursting sessions for Figure 8, without saying why. Questions are put
to the paper's authors: which maximum is the first peak of C_s and what sigma
and N are in its error bar; which rule besides the rate SD removed the sessions
not among the 86; how events were formed for the jitter; whether the mean
stimulus was subtracted before summing 1BTAs in Eq. 15; what separates a peak
of C_s for the shapes of Figure 3; whether the nBTA maximum giving tau_n was
searched before burst onset and how many bursts of each n a session needed;
and whether I_n(1) was corrected for the bias of the plug-in estimate.

The author's points on the protocol: "pin the most recent published version"
does not fit an unversioned archive, so `unversioned` was recorded and the MD5
checked against the ETag; it does not say whether the author may add a reading
the claims file does not list, so a third reading of sigma and N and the
exclusion of tau = 0 were added and marked as assumptions; many criteria define
only "reproduced", so "partially" was given when the effect held and some
expected values matched; there is no rule for expected session counts when the
dataset keeps more sessions than the paper did; it is unclear whether picking
one of the claims file's own readings counts as an assumption, so `assumed`
was set wherever the outcome depends on the burst reading; and the data-check
examples assume a task with trials and labels, so for stimulus-driven data the
spike-triggered average against a 100 ms-shifted stimulus was used as the
contrast.
