# dryad-bvq83bkk9, Dias et al. 2025

Eleven claims reproduced, two partially and 18 blocked, with none not
reproduced, all on the dataset, and the link claim `sample-sizes` also
reproduced, as every sample size of the paper comes out exactly from the data
as deposited. It pins version 333377, which holds Data.zip and README.md. The
paper, in Proc. R. Soc. B, models wing length allometry in 27 366 specimens of
five migratory passerines killed in building collisions in Chicago from 1981
to 2016 (Field Museum), with a hierarchical Stan model for each of three
classes (HY, spring AHY and autumn AHY) and MCMCglmm preliminary models that
select the climate variables, and concludes that climate explains little of
the long-term increase in wing length. The claims were written from the
version of record in Europe PMC (PMC11750374) with its supplement and from the
paper's code (Zenodo, doi:10.5281/zenodo.14226724), read for lm_mod.stan and
for the columns and rows the scripts select and drop. MCMCglmm cannot be
installed in the entry's Python environment, so the preliminary models were
run with a Gibbs sampler of the same model and priors written in Python, and
lm_mod.stan was run with CmdStan 2.40 in place of rstan. The preliminary
models of Tables S4 to S7, the VIFs, the phylogenetic signal, the climate
trends of Table S8 and the autumn AHY model of Table 3 were tested. Sixteen
claims are blocked as `too_large`: the HY and spring AHY Stan fits are
estimated at 87 and 72 minutes per filtering reading (about 51 to 58 and 42 to
48 scaled by the autumn AHY fits, which took 13.1, 12.3 and 14.0 minutes),
over the 30-minute notebook limit, and three readings are needed; Tables 1
and 2, Table S1, the expanded ranges of Tables S9 to S11 and the two
conclusions built on them are among these. The autumn AHY parts of the
blocked claims that could be computed agree with the paper, among them a year
effect on the intercept of 0.192, 0.197 and 0.193 per decade against 0.19.
`table3-autumn-ahy-recent-autumn-temperature` is partially reproduced, as
under filtering reading (d) the slope pd over chains 1 to 3 is 83.32%, below
the 90% line, and `table3-autumn-ahy-prior-wintering-precipitation` is
partially reproduced, with one effect on the wrong side of 90% under each
reading; both rest on pd values within a few Monte Carlo errors of the line,
and the (a) call of the first changed between runs (89.98% in round 1, 90.48%
in the last run). The author asked one question, on how to judge a 95% bound
within Monte Carlo error of 0 when the paper's code sets no seed; the answer
added two seed readings, the recorded run and the majority over ten seed sets,
and the rule that a claim is blocked as `methods_underspecified` when they
differ, which moved `s4-s6-spring-migration-temperature-none` and
`s6-autumn-ahy-recent-wintering-prebreeding-precipitation-none` from not
reproduced to blocked, each resting on one chain-4 HPD bound (-0.0002 and
-0.0003) that excludes 0 in at most 2 of 10 seed sets. Round 1 agreed with
every outcome it listed, 31 of the 32 claims, leaving out
`table1-hy-breeding-temperature`; its points led the fits to print R-hat, ESS
and the Monte Carlo error and per-chain value of every pd, the pooled-chain
lambda modes, the ten seed sets for the near-zero bounds of
`s4-s6-climate-variable-selection` and `s4-s5-climate-size-interactions`, the
scaled timings and the autumn AHY part of `climate-explains-little`. Round 2
agreed with all 32, so there was no third round; it found statements the
outputs did not support, among them stale timings and a (d) slope pd said to
be 6.4 Monte Carlo errors above 90%, an error computed with the stuck chain
4, and these were corrected, with the (d) calls resting on chains 1 to 3.
Three questions remain open with the reader: the outcome when both effects of
`table3-autumn-ahy-prior-wintering-precipitation` fall on the wrong side, as
in round 1's (d) fit; whether the seed rule applies to
`s4-s5-climate-size-interactions`, which would then be blocked as
`methods_underspecified`; and whether `s7-low-phylogenetic-signal` should
depend on `s4-s6-spring-migration-temperature-none`. Some outcomes rest on
weak ground: in `s7-low-phylogenetic-signal` the lambda modes (0.056, 0.062
and 0.087) are larger than the paper's 0.02, 0.02 and 0.04 and the HPD
intervals wider, which the pooled chains show to come from the Gibbs sampler.
The Stan model is compiled with -march=native, as Script01 does, so the
draws depend on the CPU and the Table 3 fits gave other values with the same
seeds between rounds; the last run gave the same draws as the run round 2
reviewed. The author's run took about 2 h 10 min; one early cell failed on a
variable-name clash and was fixed, and the five notebooks took 56 minutes at
first and 60 after the first revision, with the conclusion cells written
after the run and copied into the executed copies.

The README says some specimens in morphdata.csv were filtered out before
analysis and that the filtering steps are in the code, but the code applies no
filter and the file gives every sample size of the paper exactly without one,
so the file appears to be the filtered data; the Methods' 5-MAD filter would
remove 0 to 70 more specimens depending on how it is read. The paper's 27 366
specimens are the birds in the three main models, while morphdata.csv holds
27 486, the other 120 being in species-years without climate data, which neither
the README nor the paper says. morphdata.csv has no catalogue number or other
specimen identifier, so its measurements cannot be linked to catnodata.csv,
which has 26 436 rows, 1050 fewer, with 5061 rows without a catalogue number
and 945 repeated catalogue numbers, and for 44 catalogue numbers the repeated
rows differ in species, sex, age, year or season. The published Stan model
converges poorly on the autumn AHY data with the code's seed and settings
(13.8% to 33.5% of draws divergent, largest R-hat 1.083 to 1.596, and under
one filtering reading a chain stuck with every draw divergent), while the
Methods say convergence was confirmed with R-hat and trace plots and report
no diagnostic values. The code selects climate columns by number and drops
species-years by hand-coded row numbers, which the notebook shows match the
deposited files, and the Table S8 code reads an object (envdata3) that no
script defines, so its input was built from the deposited climate files under
two readings. ed_FHY.csv and ed_AHYfall.csv are identical files and
ed_AHYspring.csv is the same table shifted by one year, which fits the
README's description of their use but is not stated in it.

The author's points on the protocol: it covers `not_runnable` but not
reimplementing a method, as MCMCglmm and PyStan could not run here; it assumes
a seed cannot change an outcome, while here it does at bounds on the line; it
is unclear how filtering readings combine for claims of absence; the entry
check rejects strings starting with `/tmp/` while docs/archives.md has
notebooks read the staged path; it does not cover conclusion cells written
after a run too long to repeat; and a claim fitted in several notebooks, as
each filtering reading of the autumn AHY fit is, can cite only one in its
`output`.
