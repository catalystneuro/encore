# 000939, Duszkiewicz et al. 2024

Eighteen claims reproduced (one on an assumption), three partially, one not
reproduced and none blocked. The 12 claims on data elsewhere are left out of
these counts: of them seven reproduced, two partially and three are blocked, two
as `methods_underspecified` and one as `other`. The first verification round
agreed with 30 of the 34 outcomes as they stood and the second with 33, and
because the second proposed a change of outcome for
`ed8cd-multiplicative-detectable`, a third round reviewed that claim alone and
agreed with it. It pins version 0.261016.2310, the latest published version, as
the paper cites none; every file has the same unit, spike and head-direction
sample counts as 0.250207.0025. The paper, Duszkiewicz, Orhan, Skromne Carrasco
et al., "Local origin of excitatory–inhibitory tuning equivalence in a cortical
network" in Nature Neuroscience, records postsubiculum (PoSub) with 64-channel
H5 linear probes and the anterodorsal thalamic nucleus (ADN) in mice and shows
that PoSub fast-spiking (FS) cells carry stable head-direction (HD) tuning
anchored to landmarks, compares the Fourier signatures of PoSub-FS, PoSub-HD and
ADN-HD tuning curves, relates FS tuning to HD-FS connections with a simulation
and a model fit, silences the TRN input to ADN with ArchT, and finds the HD-FS
coupling and an Isomap ring preserved in REM sleep. The dataset holds the PoSub
H5 recordings in 31 NWB files; the ADN, cue rotation, Neuropixel and ADN
optogenetic sessions are on figshare (doi:10.6084/m9.figshare.24921252, version
3) and were used as inputs, with the paper's MATLAB code, read and not run. The
claims were written from the version of record served by Europe PMC
(PMC11001581) with both supplements, without the figures; the Python code of the
simulations and the model fit is not deposited. Reproduced are the cell classes
(1,661 excitatory, 430 FS and 1,512 HD cells, and the paper's 1,999 parallel
units once the one missing session's 239 are added), the FS HD information,
decoding, geometry, stability and cue rotation claims, the FS spectral
heterogeneity and phase independence, `fig4f-synaptic-weights-dispersed` (CV
1.90 over 1,176 connections), the optogenetic claims `fig5b`, `ed7gj`, `ed7` and
`ed8e`, the Isomap and ring claims and the GLM coupling claims;
`fig6c-coupling-preserved-wake-rem` rests on the assumption that a Python mirror
of glmfit flags the pairs MATLAB would, as keeping the flagged pairs gives a
pooled HD-HD Pearson r of 0.000 against 0.641. Partial are
`fig3-ten-components-power` (0.989 with squared-modulus power, 0.872 with
root-mean-square power), `fig3g-first-three-components` (components 1 and 2
above control under squared modulus, component 3 at p = 0.064, and 1 to 4 under
root mean square) and `fig5e-hd-multiplicative-fs-additive`, which fails only
under exclusion reading (b) (HD additive against control p = 0.015), a reading
that excludes 31 of 62 HD cells and is put to a reader.
`fig3h-dominant-component` is not reproduced, 47 FS cells peaking in component 3
against 55 +- 6. On figshare data `fig3e-fourier-signatures-differ` is partial
(the interaction gives F(9,18333) = 1.09, p = 0.365 with the code's numeric cell
type), as is `fig3f-posub-hd-closer-to-fs` (p below 1e-9 under one of four
readings); `fig4-random-connectivity-simulation` and `fig4h-model-fit` are
blocked as `methods_underspecified`, and `ed6-trn-innervates-adn` as `other`,
its tracing images being deposited nowhere. The author's first run gave
`cell-classes-counts`, `ed3k-robust-to-controls` and `fig3h` partially, `fig3e`
not reproduced and `fig3g` and `ed8cd` reproduced, the last three on
assumptions. The author asked a reader whether ADN-HD multipeak scores are
higher, as the claims file said, while the paper's counts imply they are lower;
the reader amended the claim to say only that they differ, and `ed3k` moved to
reproduced. Round 1 disagreed with four outcomes and found that the
time-reversed control reversed only the used samples, that the decoder's chance
level was scored against the reversed HD, that the GLM filter was the helper's
own approximation of glmfit's warnings and that the three ArchT mice on figshare
were dropped without the choice being stated; in reply `cell-classes-counts`
moved to reproduced, `fig3e` and `fig3g` to partially and `fig3h` to not
reproduced, `ed8cd` to partially, the GLM fits were rewritten to mirror glmfit,
the cell selection followed `Figure_GLMRemWake.m`, REM was restricted to the
home-cage epochs and the five-mouse optogenetic results were added as a variant
that decides nothing. Round 2 found sentences the outputs did not support (99.9%
label agreement where HD agreement is 99.7%, a cumulative signature above the
others at every component where only 1 to 9 are tested, depth ranges read from
every fourth bin, and series shapes and REM epochs no cell printed), all
corrected, and the revision added a check of four more GLM lags in 9 of the 27
sessions (60 more HD-HD pairs of 10,507 flagged, 0.6%). The author's run took
from 18:23 to 20:04 UTC with the notebook at 25.5 minutes, 10 of them in the GLM
fits, and nothing failed in the final run; three markdown result cells were
edited after it and copied into the executed copy without a second run. The
notebook ran in about 40 minutes after the reader's answer, 2,075 s and 2,199 s
after rounds 1 and 2 and about 34 minutes at the end; changes to `tools/`
already there were left untouched.

The dandiset holds 31 of the paper's 32 PoSub sessions, all 14 vertical ones
(931 units, the paper's number) and 17 of the 18 parallel ones (1,760 units
against 1,999); the missing one is A8603-210602, the Neuropixel recording, with
239 units, only in figshare Dataset_4. Of the five ArchT mice of the PoSub
optogenetic experiment it holds two (A1813, A1815); the other three (A1801,
A1804, A1806, six sessions) are only in figshare Dataset_6, so the paper's 83 HD
and 47 FS ArchT cells cannot be reached from the dandiset (62 and 33 here; 102
and 50 with the figshare mice added). In eight files
`processing/ogen/optogenetic_stim` holds four channels interleaved in one
dimension, so its length at the stated 20 kHz is four times the session's (in
A1813, 933,367,680 samples against 233,341,920 of the ElectricalSeries, an
11,667 s session), with only every fourth sample carrying the light, as 0 and
16368; in A1808 it holds one channel of 0 and 1. The pulses are recoverable and
match the figshare Opto_TS.csv tables within 0.1 ms, but the series' shape and
units (watts) do not describe it. The files hold no speed series, though every
analysis restricts tuning curves by speed, and no table of light pulse times,
and the probe orientation is stated only in the free-text device description.
The sleep states of A3711, A3717 and A3723 run to about twice the session's
length (to 24,351 s in a 12,177 s session), so that 298, 518 and 223 s of their
REM lie after the recording ends, and in A1821 (16 s in the square epoch and 41
s in the optogenetic epoch), A3712 (12 s in the square epoch) and A3701 (0.3 s
in the triangle epoch) REM lies inside exploration epochs; the REM intervals are
the same in version 0.250207.0025. The units' `is_excitatory` and
`is_fast_spiking` labels follow the code's 0.35 ms trough-to-peak cut (agreement
99.9%), not the Methods' 0.4 ms, and the column descriptions give no criterion.
`Figure_Fourier.m` computes the KL divergence in the reverse of the Methods'
direction, which gives p = 1e-7 against 0.008 for the PoSub-HD against ADN-HD
test. Questions are put to the paper's authors: whether the Fourier power is the
squared modulus, which decides `fig3-ten-components-power`, `fig3g` and the
significance of the Fig. 3e interaction; whether cell type was meant to enter
the Fig. 3e ANOVA as a numeric covariate (p = 0.365, against 5e-82 as a factor);
whether the gain analysis excludes a cell when both tests fail or either;
whether the gain simulation's noise was titrated or fixed at 1.8 x 1.8 Hz, and
against which control; which glmfit warnings removed a pair, and at how many
lags; and how the speed series and the cue rotation exclusion were defined.

The author's points on the protocol: the protocol forbids `data_missing` for
claims with data elsewhere, though the data of `ed6` are public nowhere, so
`other` was used and the two simulation claims became `methods_underspecified`;
the protocol keeps dataset claims on the dandiset though figshare holds the
missing ArchT mice, which were not used and whose absence was recorded as a
finding; criteria leave cases undefined, as `fig3h` defines a partial outcome
only when all counts hold; and result cells are markdown, so three were edited
after the run and the edits copied into the executed copy.
