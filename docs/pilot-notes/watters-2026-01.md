# 000620, Watters et al. 2026

Seven claims reproduced (one on an assumption), five partially (one on an
assumption), none not reproduced and fourteen blocked, thirteen as too large
and one as methods underspecified. The first verification round agreed with
25 of the 26 outcomes as they stood and the second with all 26; nothing was
proposed after the second, so there was no third round. It pins version
0.261019.2000, the latest published one; the paper cites none, and all
published versions hold the same 142 assets. The paper, Watters, Gabel,
Tenenbaum and Jazayeri, "Working Memory of Multi-Object Scenes in Primate
Frontal Cortex", a bioRxiv preprint, records two rhesus macaques (Monkey P and
Monkey E) that hold 1 to 3 fruit images over a 1 s delay and saccade to the
remembered location of the cued one, with a Neuropixels probe in DMFC and
V-probes in FEF, in a Triangle dataset of 24 sessions and a Ring dataset of
22, and compares Slot, Switching and Gain models of the population activity;
the dandiset holds 47 spike sorting, 48 behaviour and task and 47 raw ecephys
files. The claims were written from version 1 of the preprint as bioRxiv JATS
XML, without a PDF, so no figure panel could be looked at, and from the
paper's code (github.com/jazlab/multi_object_memory_2025 at commit 6e4b333),
whose method details the notebooks cite without using its data or fitted
results. The check amended seven claims, among them a pooled Triangle and Ring
reading of the reaction times and the Ring sessions of the decoder
orthogonality claim, and left open the statistics of the Gain model
comparisons, which rest on the figure's brackets, and those of Extended Data
Fig. 8a, which the text garbles. The behaviour, unit count, selectivity, noise
correlation and decoding claims could be tested; the thirteen claims that need
the paper's encoding models fitted could not. Reproduced are
`fig1b-performance-load` (P 0.953, 0.930, 0.692 and E 0.928, 0.759, 0.561,
equal to the values the paper's notebook printed), `fig1c-reaction-times`
(interquartile ranges 52.0 and 69.8 ms), `ext1-misbinding-errors` (84.5 to
99.4% of errors at a non-target object's vertex), `triangle-unit-counts`
(4,688 units, 2,937 DMFC and 1,751 FEF, exactly the paper's numbers),
`ring-unit-counts` (3,052, 1,712 and 1,340 against 3,051, 1,712 and 1,339),
`ext2-stimulus-delay-activity` (Pearson r 0.898 and 0.971) and
`fig5ab-ring-behavior` (2-object fraction correct P 0.903 and E 0.756).
Partial are `fig2b-selectivity-range` (position AUCs meet the rule, identity
AUCs only for P under the code's p-value), `fig5cd-ring-tuning` (receptive
fields vary as claimed, the AUC part fails), `fig5e-signal-noise-ring` (P and
pooled pass, E's highest bin 0.0238 overlaps its lowest 0.0174),
`ext3ab-decoding` (position 82.5 to 99.2% against 32.1 to 33.8% shuffled,
identity above control in 0 of 3 sessions) and `ext3c-decoder-orthogonality`
(Ring and Receptive Field data near 90 degrees, Triangle neural medians 106.7
and 106.6); for the first four the criterion defines only the reproduced case,
so partially reproduced is the attempt's label. `fig2d-signal-noise-triangle`
is blocked as methods underspecified, as the Methods' signal correlation
reproduces the claim in both monkeys and the code's gives Monkey E a lowest bin
of 0.0245 (-0.0296 to 0.0786). The thirteen model-fitting claims are blocked as
too large: one step at the paper's sizes took 0.436 s in the latest run, so one
fit of 10,000 steps takes about 1.2 h and each claim 6 to 116 days, and at 100
times the speed 1.5 to 27.9 h, each over the 60-minute notebook limit; no fit
was started. `ext1-misbinding-errors` rests on the code's correctness radius of
0.2 arena widths (4.8 degrees), as with the Methods' 2.4 degrees Monkey P's
2-object errors are mostly at no vertex (249 against 207), and
`ext3c-decoder-orthogonality` on the code's sigmoid output for the Ring
decoders, as with the linear output the Methods describe the Ring neural
medians are 140.2 and 142.1 and fail. The author's first run gave the same
outcomes except that `ext3c-decoder-orthogonality` was not reproduced. The
author asked no questions of a reader, so the answer and author-answers runs
changed nothing. Round 1 disagreed on `ext3c-decoder-orthogonality`, giving
partially reproduced, and found that the decoders got rates in Hz with no
per-unit normalisation, that the simultaneity filter kept 20 of 116 units in
Triangle 2022-06-04, that the Ring decoders' sigmoid cannot reach the negative
Ring targets, that ordered pairs made the noise correlation intervals too
narrow and that the cost estimate considered no GPU; in reply each point was
checked against the paper's code (its normalisation commented out, the same
greedy filter, the sigmoid on the Ring decoders too), a variants notebook with
z-scored inputs and a linear Ring output was added, with intervals clustered by
pair and per-session medians, ext3c became partially reproduced and whether
the ext3ab identity test matches the paper, whose Methods say identity was
poorly decodable on single trials, went to a reader in `questions/000620.yaml`.
Round 2 asked that ext3c be marked assumed and that the four other partial
outcomes say the label is the attempt's, and found numbers the outputs did not
support in the decoding prose, the cost cell and the record, among them
identity above control in 1 of 3 sessions where the outputs show 0 of 3; in
reply a re-run gave identical decoding outputs, so the old prose came from a
development run, the text was rewritten from the saved outputs, ext3c was
marked assumed and whether the claim needs the neural decoders near orthogonal
went to a reader as a second question. The author's run took about 2 h 30 min
(18:25 to 20:51 UTC); the first decoding run failed on an identity-label dtype,
and the Ring noise correlation method took 17 min until it was changed to one
neighbour sort per session. The main and decoding notebooks ran in about 9 and
16 min at first, 753 s and 1595 s after the author-answers run, 10.5 and 24.5
min after round 1, with 31 min for the variants notebook, and 8, 13 and 16 min
at the end; after round 1 two markdown cells edited after the run were copied
into the executed copies by hand instead of a 66-minute re-run. Removing an
empty `.claude` directory the harness left in the entry was refused for lack of
approval, and the untracked files in the repository root were left alone.

The Methods say a response was correct within 2.4 degrees (0.1 arena widths)
of the target, but every completed trial with a closed-loop response error
under 0.2 arena widths was rewarded (49,185) and none at 0.2 or more (12,469),
so the task scored at 4.8 degrees, as the paper's code does. The paper's
counts of "well-isolated neurons" (4,688 Triangle, 3,051 Ring) are recovered
only with multi-units included, as 1,563 of the 4,688 Triangle units and 1,123
of the Ring units are labelled good, and they do not apply the Methods' rule of
at least 500 stable trials (4,473 with it). The Methods give a cue phase of
180 ms and the Fig. 1c legend counts saccades earlier than 180 ms as broken
fixation, while in the trials tables the response phase begins 250 ms after cue
onset (0.2498 to 0.3167 s), 47.9% of completed trials have a response time
under 250 ms and 1.1% are under 180 ms without being marked as broken
fixation. The column response_time does not say which event it marks; it
precedes closed_loop_response_time by 134 ms at the median and in some
completed trials precedes cue onset (earliest 12.5 ms before), so it reads as
saccade onset. The electrodes tables of all spike sorting files give the
location 'unknown', and the area of each probe (s0 in DMFC, vprobe0 and
vprobe1 in FEF) is stated only in the paper's code. The dandiset holds two
Perle sessions the paper does not count, 2022-06-06 (spike sorting, 2,378
trials, all with 2 objects, 77 units) and 2022-06-08 (behaviour only, 1,517
trials), which neither the dandiset nor the paper describes, and the code's
Ring model comparison leaves out Elgar 2022-09-18 and 2022-09-19, which the
paper's 22 Ring sessions include. The code's AUC p-value draws labels with
replacement 5,000 times where the Methods shuffle 1,000 times, and more units
pass the modeling threshold under it (172 against 98 for Elgar 2022-08-20).
The code's 2-object decoder passes the Ring decoders through a sigmoid, with
outputs in 0 to 1, while their targets lie in -0.7 to 0.7 and the Methods
describe linear decoders. The Methods place the decoder orthogonality angles
in Extended Data Figure 3b, while its legend gives them as panel (c). No
problems were found with duplicate recordings, spike-time order or spikes
outside stable intervals, and the clock check passes in every session, for
Elgar 2022-08-23 through the delay window only. Questions are put to the
paper's authors: which signal correlation Fig. 2d shows, the Methods' or the
code's; whether a response was counted correct within 2.4 or 4.8 degrees; and
how the Fig. 2b AUCs were cross-validated.

The author's points on the protocol: the fig2d criterion says differing
methods block the claim while step 1.6 allows adopting the best-supported
reading as an assumption, so the criterion was followed; several criteria
(fig2b, fig5cd, fig5e, ext3ab) give no rule for a partial result, so the
protocol's general definition was used; T2 leaves the correctness radius open
with no rule for disagreeing readings, so step 1.6 was applied and backed with
the reward data; "every sentence backed by a printed number" does not fit
timings that vary between runs, so they were written as "about"; the protocol
does not say how to treat a clock check that fails in one window and passes in
another; estimating the cost of PyTorch models without torch in the locked
environment is not covered, so a numpy step of the same sizes was timed as a
lower bound; it is unclear whether reference values printed by the paper's
code may be cited in a Result when they appear only in the claims text; and
changing markdown after a run means a full re-run of about 26 min to keep the
executed copy matching.
