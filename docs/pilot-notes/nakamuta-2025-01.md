# 002020, Nakamuta et al. 2025

Two claims reproduced (both on an assumption), none partially, three not
reproduced (one on an assumption) and 15 blocked, 14 as methods_underspecified
and one for insufficient metadata. The first verification round agreed with 17
of the 20 outcomes as they stood and the second with 19; the second disagreed on
`fig3c-avalanches-emerge`, whose change from blocked to not reproduced was
proposed and, in a third round that reviewed only this claim, agreed and made.
The version pinned is 0.261004.1410, the only published version, identical to
the draft. The paper, a bioRxiv preprint, cultures dissociated cortical neurons
from E18 rat embryos on MaxOne high-density multi-electrode arrays, records 30
minutes of spontaneous activity a day on up to 1,024 of 26,400 electrodes, and
reports that firing changes from asynchronous to bursting as the cultures
mature, that the variance spectrum of PCA comes to follow a power law around 15
DIV with an exponent of about 1.2, that dominant PCs become spatially local,
that neuronal avalanches emerge with an exponent of about 1.5 and co-occur with
the power law, that PCs lack the in vivo temporal structure, and that a binary
threshold network with Cauchy connections gives a power law where Gaussian
connections do not; the data set holds 129 recordings of unsorted spike
detections with electrode positions from seven dishes. The claims were written
from version 1 of the preprint as text flattened from the bioRxiv JATS XML,
without a PDF and without the supplement (Figures S1 and S2), with the Methods
equations (the fitted function, local Moran's I, the model) lost from the text,
and without code, as the paper links none; the data set points at version 2,
which was not read, and the claims check made six corrections, among them the
continuity rule of `dishes-analysed` and an onset of 2.55 +- 0.75 DIV, for 20
claims. Reproduced are `dishes-analysed` (7 dishes, fragile, as 6 do if a day
with no recording breaks a run and 4 or 2 under S2) and
`fig1b-async-to-bursts` (Spearman 0.487 under S1 and 0.384 under S2, failing
only under d0 = 1, which would put activity at 1 DIV). Not reproduced are
`fig3c-avalanches-emerge` (under none of 56 readings are both the shift DIV and
the exponent within tolerance; wherever the shift is reached the exponent is
1.13 to 2.53), `fig3d-decay-rates-correlated` (no reading of 8 gives both
correlations positive at p < 0.05) and `no-temporal-structure`, as dominant PCs
have longer time scales in most recordings from 15 DIV (25 of 44 under (a),
S1), though the effect is small. The power-law claims of Figures 1 and 3 and
Figures S1 and S2 are blocked on the scale of the fitted b: on the claims
file's reading it has a median of 0.0055 (S1, F1), independent Poisson counts
at the recorded rates give the same b (0.0114 against 0.0131 in the data), and
b of at least 0.1 would need lambda_1/lambda_100 above about 19,930 where the
largest is 5,503, so the paper's 0.1 boundary puts nearly every recording in
the Power-law group. The locality claims of Figure 2 are blocked because the
readings of local Moran's I and of the slope axis disagree (12 of 56 hold for
`fig2c-locality-spectrum`), `activity-onset` for the missing days in vitro, and
the two model claims of Figure 4 were not run, as the model is not specified.
The author's first run had 3 reproduced, 2 partially, 3 not reproduced and 12
blocked. The author asked no questions of a reader, so the answer and
author-answers runs changed nothing. Round 1 disagreed on
`fig2b-spatial-structure`, `fig2c-locality-spectrum` and
`fig2d-locality-slope`, raised the b scale, an incomplete fig3c analysis, a
single DIV offset for all dishes and readings that were not computed; in reply
`fig2c-locality-spectrum` went from reproduced to blocked, the three claims
that depend on it were blocked with the disagreements recorded, d0 = 4 and 5
and two per-dish offsets were added, and a question on the fit went to a reader
in `questions/002020.yaml`, written after the answer run, so it is unanswered.
Round 2 asked for fig3c to be not reproduced, as the missing DIV does not decide
it, and found sentences the outputs did not support, among them b far below 0.1
"in every active recording", which holds only under F1; in reply the text was
corrected, a second question on the fit error went to a reader, and the fig3c
change was proposed. The author's run went from 23:37 to about 00:18 UTC; the
notebook ran in 396 s at first, 431 s after the author-answers run, 362 s
after round 1 and 408 s after round 3, and nothing failed. The untracked
dotfiles and `scripts` device node in the repository root were left alone.

The files give no days in vitro and no plating date, only recording dates;
their experiment description says "Days in vitro are unknown to this converter
and are not inferred from the date list", and the subject age, P18D in every
file, is the donor's age at dissection, so no result can be placed on the
paper's DIV axis and every analysis that compares early and late cultures rests
on an assumed offset (DIV as days since a dish's first recording plus 2).
Spike times run from the first detected spike, not from the recording start,
whose frame is not stored, so time bins can only be aligned to the first spike.
The data set holds 129 recordings, 17 of them with a mean rate at or below 0.03
Hz, the paper's exclusion rate, some within a dish's series (23317 on days 3
and 4, 23312 on day 22, 23302 on days 7 and 8) and at the ends of 23282 and
23302, and nothing marks which recordings the paper analysed; it appears to
hold only the seven selected dishes, so the selection itself cannot be tested.
Six recordings of dish 23311 (days 8 to 13) hold 338 to 702 electrodes and one
of 23280 (day 6) holds 525, where the others hold 956 to 1012, and the data set
does not say why. The electrode positions match the MaxOne grid, and no
recording is deposited twice (dishes recorded at the same moments have
population counts that correlate at most 0.225). Questions are put to the
paper's authors: how the exponential decay rate b of the variance spectrum is
computed (the formula, what x is, which ranks are fitted and whether the error
is on log or raw values); whether local Moran's I is normalized by the variance
of the PC weights, whether w_ii counts and which axis of the locality slope is
logarithmic; whether avalanche spikes are pooled over electrodes for the mean
inter-spike interval, whether cascade size counts spikes or electrodes, and
what the Figure S1 threshold and the Figure S2 shuffle and measure are; and
what the network size, weight distributions, run length, initial state, inputs
and binning of the Figure 4 model are.

The author's points on the protocol: the claims file says to block a claim
whose readings disagree while step 1.6 allows adopting the best-supported
reading as an assumption, and step 1.6 was followed at first for M2 with L1;
nothing covers a fitted quantity whose scale cannot match a threshold the paper
states, so the chance-level rule was applied by analogy and claims that need
the threshold were blocked; nothing covers a time axis with an unknown offset,
so an offset was assumed for early and late comparisons and claims whose result
is a DIV were blocked; the step-2 clock check does not apply to a single spike
stream with no annotations; the rule that a claim depending on a blocked claim
is blocked applied to `fig1f-exponent-1p2` though its transition is the same
recordings whatever the offset; "reproduced under any reading" and "the outcome
is the one they all give" pull against each other, so each criterion's own
wording was followed; and building the analyses meant extracting from all files
once outside the notebook (6 minutes), with every recorded number taken from
the notebook run.
