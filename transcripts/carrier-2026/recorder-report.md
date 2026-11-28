# carrier-2026, Carrier et al. 2026

Seventeen claims reproduced, one partially, two not reproduced and nine
blocked, four for missing data, four as `too_large` and one as
`methods_underspecified`; one outcome, `fig2i-cb-neuron-crash-counts`, rests
on an assumption. The first verification round agreed with 27 of the 29
outcomes as they stood and the second with all 29; nothing was proposed
after the second, so there was no third round. Both Zenodo records are
pinned at their only published version. The paper, Carrier, Romano,
Scaria, Palmer, O'Leary, Marder and Powell in the Journal of
Neurophysiology (135: 797-814), records the pyloric rhythm of the isolated
stomatogastric nervous system (STNS) of the crab C. borealis and the
lobster H. americanus in salines from 0.25x to 1.75x and through
temperature ramps, compares the Q10 and crash temperatures of the two
species in 0.75x, 1x and 1.25x saline, and records the rhythm by PPG in
intact animals moved to altered seawater. The claims were written from the
version of record, whose PDF could not be rendered, so the bar heights of
Figures 1E, 4E and 9 were not read; the paper links no code. Every claim
was tested on the authors' per-preparation tables and Prism files in the
deposit, not on burst detection repeated on the raw recordings, whose
burst criteria the paper does not give, and the mixed models were fitted
with statsmodels and Wald tests, as R is not in the environment.
Reproduced are the crab frequencies in 0.75x and 1.25x saline, the crab
crash temperatures in 0.75x and 1.25x, the crab Q10s by salinity, the crab
mixed model, the neuron crash temperatures and counts (9 of 20 when all
three neurons crashed within one 2 C step, 4 under exactly equal
temperatures), the lobster Q10 and phases, the frequency of the two species
at 10 C, the species Q10s in each saline and the species crash
temperatures in 0.75x and 1.25x; the fits of Figs. 2G, 2H, 3B and 7A to 7C
match the paper's values exactly. The lobster mixed model is partial:
temperature and the interaction are significant under every reading,
salinity under none (P 0.26 to 0.79; paper P = 0.001). Not reproduced are
the lobster Q10 across salinities, where the 0.75x set gives F(1,210) =
4.04, P = 0.046 against the paper's F(1,209) = 3.495, P = 0.063, and left
out one at a time its 214 points give P above 0.05 for 60, and the crash
temperature of the two species in 1x, where 20 crab values give Welch P =
0.060 against 0.047, as does the test stored in the authors' Prism file.
Blocked are the crab crash fractions of Figure 1E, whose 0.5x and 1.75x
outcomes sit in 37 GB of nested raw zips (about 6 h to read at the
measured 1.6 MB/s), the lobster salinity series of Figure 4, the lobster LP
and PY crash temperatures of Figures 5B, 6A and 6B, the in vivo rhythm of
Figure 8 and the 15-h mortality of Figure 9. The author's first run gave
16 reproduced, 2 partially, 3 not reproduced and 8 blocked. Round 1 found
that the in vivo band rule passes shuffled traces in 90 to 99% of windows,
that the author's reading of the neuron crash count counted the wrong
ramps, that the lobster mixed model had not been run on the ramps with a
Crash mark (10, 13 and 8, near the paper's n) and that the extra Fig. 5D
point had not been sought; in reply all 58 spectrograms were shown and
three rules calibrated on shuffled traces added, under which every lobster
exposure keeps its band and the crab result depends on the rule, so the
in vivo claim moved from reproduced to blocked; the crash count moved to
reproduced on the verifier's reading; and the author found a bug that
tested salinity together with the variance of its random slope, whose fix
moved the crab mixed model from partial to reproduced. Round 2 found
sentences without printed support, among them a summary calling the Q10
match exact throughout and a count of 6 preparations with LP and PY burst
files, which is 8, all corrected. The author's run took about 55 min (17:39
to 18:35 UTC); one development read failed with Zenodo HTTP 500, which led
to retried reads, and nothing failed in the final run. The notebook ran in
269 s at first and 524 s at the end.

Lobster preparation 111122's 0.75x ramp in Sheet4, the Prism file and the
MATLAB file is a copy of preparation 120722's: the burst tables are equal in all 4730
numbers and both name 0.75x_ramp.smr from 329.541 s, while the two
recordings differ (910 MB and 703 MB) and 111122's own 28 C burst file
gives 1.13 Hz where the table gives 1.66 Hz, so one recording enters the
lobster 0.75x fits of Figs. 5D and 7A twice. Seven in vivo exposures are
the same recordings as seven others filed under another animal or
salinity, every ABF file with the same MD5, so the 59 exposures hold 52
distinct recordings and the per-salinity counts of animals are lower than
the names suggest. Every in vivo exposure labelled 1Hour holds 16
two-minute ABF files, about 32 min, and the one labelled 15Hours (Lobster
9, 0.25x) the same 32 min; the second half of each hour, the 2.5-h
exposures, the other 15-h exposures and any record of the 15-h deaths are
not deposited. The lobster salinity series of Fig. 4 is in neither record,
though the Part I description says it holds the raw data of all dissected
lobster nervous systems, and the lobster LP and PY crash temperatures are
not tabulated; LP and PY burst files exist for 8 of the 19 preparations.
Crab 963_106's 1.25x crash temperature is 36.0 C in
CanboVsHomam_CrashTemps.prism and 26.0 C in Crab Metadata.xlsx, and the
paper's two crab 1.25x means, 26.2 C (Fig. 2E) and 27.28 C (Fig. 7F), are
the two versions. The deposit holds 20 crab 1x crash temperatures (963_109
has none) where Fig. 7E has n = 21. No analysis script was found in the
files read, though the paper says all custom analysis scripts are in the
two records (the 21 inner raw crab zips were read only at their start),
and lobster 888_156 has frequencies in the table but no recording. Lobster
020723's 1x ramp has 4.68 Hz at 30 C, where the next largest lobster value
is 2.83 Hz. In Crab Metadata.xlsx the 10 C rows of the Burst Frequency
sheet are labelled with a date, 888_136 appears as two preparations in the
salinity series and 888_145 is not in the Animals sheet. Three questions
are put to the paper's authors: whether "the same temperature" in the
neuron crash count means the same ramp step, how a crashed rhythm was
recognised on the in vivo spectrograms and over what part of each
exposure, and which ramps, salinity coding and response entered the mixed
models of Figs. 2F and 5C and which points were left out of the Fig. 5D
fits.

The author's points on the protocol: "compute every result from the data"
was met with the authors' per-preparation tables, recorded as a deviation
on every such claim; `docs/archives.md` does not say that Zenodo serves
about 1 MB/s per connection and answers HTTP 500 under load, so reads ran
in parallel with retries; opening a zip in place does not work for zips
nested in a zip; pyabf opens only file paths, so headers were parsed with
it and samples read from memory; it has no rule for a criterion that cannot
tell a result from its null; it does not say how to weigh the paper's
wording against a reading that fits the data; counting each recording once
conflicts with reproducing numbers that include the 111122 copy, and each
analysis has a variant without it; and the mixed models need R, which is
not in the environment, so statsmodels with Wald tests was used as a
deviation without blocking the claims as `not_runnable`.

---

Most of the paper's findings on isolated crab and lobster stomatogastric nervous systems held up on the authors' tables. In crab, 0.75x and 1.25x saline left pyloric frequency and its Q10 unchanged while 1.25x lowered the crash temperature, and lobster rhythms were less temperature sensitive than crab rhythms in altered saline. Two lobster results failed: the mixed model found no salinity effect, and the Q10 differed between 0.75x and normal saline (P = 0.046), depending on one unidentified point. The species difference in crash temperature in normal saline missed significance, with one crab value missing. The lobster salinity series and neuron crash temperatures are not deposited, and the in vivo rhythm could not be judged without the paper's criterion.
