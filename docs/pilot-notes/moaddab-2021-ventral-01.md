# crcns-bf-3, Moaddab et al. 2021

Twenty-eight claims reproduced (24 on an assumption), fifteen partially (14 on
an assumption), two not reproduced (both on an assumption) and none blocked.
The first verification round agreed with 42 of the 45 outcomes as they stood
and the second with all 45; nothing was proposed after the second, so there was
no third round. The version is recorded as unversioned with the data set's DOI
(10.6080/K0HH6H8V). The paper, Moaddab, Ray and McDannald, "Ventral pallidum
neurons dynamically signal relative threat" in Communications Biology (4:43),
records 435 ventral pallidum (VP) single units in 194 sessions from 14 male
Long Evans rats during fear discrimination, in which danger, uncertainty and
safety cues predict foot shock with probability 1.00, 0.25 and 0.00 while the
rats nose poke for food; it screens 257 cue-responsive neurons from 153
sessions, splits them into cue-excited and cue-inhibited neurons, clusters the
cue-inhibited ones by k-means into Low, Intermediate and High firing neurons
and regresses their firing on relative threat and fear output. The data set
holds the 435 units with spike, cue, shock, nose-poke and pellet times, a cube
of trial-ordered measures and the authors' MATLAB scripts (cubeScriptPR25.m and
vpAnalysis.m), which the paper does not link. The claims were written from the
version of record (PMC7794503, Europe PMC full-text XML) without a PDF and
without the Supplementary Information, so four claims (supp5, supp6, supp8 and
supp9) rest on supplementary figures nobody read and the High firing neurons
have no claim; the paper's code link, http://mcdannaldlab.org/resources,
returned 404. The author used the scripts in the data set as the paper's code,
with the Methods' version as the main result and the scripts' as a variant.
Every claim could be tested. Most outcomes rest on three assumptions: A1, that
the neuron groups are those of the scripts, whose screen on rates floored to
integers gives the paper's 257 neurons from 153 sessions and whose split gives
its 131 cue-excited and 126 cue-inhibited neurons; A2, that the clusters are
those of one Matlab k-means++ start after rng(1), which gives the paper's Low
74, Intermediate 34 and High 18; and A3, that a nose-poke pause is a gap of
more than 2 s between pokes 18 to 2 s before a cue onset, as cubeScriptPR25.m
defines it. Reproduced are, among others, `cue-responsive-screen` (271 of 435
neurons from 160 sessions with the Methods' rates, within tolerance of 257 and
153), `fig1f-suppression-cue-effect` (F(2,26) = 75.80 against the paper's
75.34), `kmeans-three-clusters` (the paper's F values to the printed digits
with the authors' features), `clusters-by-rat` (11 of the 18 High firing
neurons from rat pa02), `fig4b-low-dynamic-shift` (F(13,949) = 2.34 to 2.44,
p = 0.003 to 0.0045, for model (a) only) and `supp9-excited-nosepoke-pauses`
(no post interval above zero under the authors' pauses, resting on A3).
Partial are, among others, `recorded-units` (195 sessions against 194),
`clusters-differ-in-cue-firing` (Low against Intermediate p = 0.035 against
the paper's p < 0.005), `fig3b-low-inhibited-to-threat-cues` and
`fig3d-intermediate-inhibition` (the pattern holds with means about twice the
paper's), `fig5d-f-low-reward-cue-correlations` and
`fig6g-excited-reward-cue-correlations` (signs and significance hold, R2 outside
the claims file's 10% tolerance) and `supp6-low-nosepoke-pauses`. Not
reproduced are `supp5-low-cue-correlations` (a positive onset
uncertainty-safety correlation of Low neurons, r = 0.36, p = 0.001; with the
authors' first 5 s of cue r = 0.03, p = 0.82) and `fig4g-int-early-late-betas`
(no reading with the Methods' normalization gives the pattern; the authors'
per-trial firing gives -0.76, 0.07, 0.12, -0.44 against the paper's -0.77,
0.07, 0.13, -0.43). Ten of the 15 partial outcomes meet the criterion under
the scripts' variant; recorded-units, fig3b-low-differential, supp6, fig6b and
fig6g do not. The author's first run had 29 reproduced, 14 partially, 2 not
reproduced and none blocked, with supp6 reproduced. The author asked no
questions of a reader, so the answer and author-answers runs changed nothing.
Round 1 disagreed on fig2-excited-inhibited-split, supp6 and supp9 (each
partially reproduced) and found that A1 reverses the rule that the Methods give
the main reading, that the Methods' normalization gives means 1.7 to 2x the
paper's while the scripts' matches them, that only 98 of 300 single k-means
starts reach the paper's partition, against the claims file's statement that
the seed cannot change a conclusion, and that 10 s pauses leave Intermediate
neurons a median of 0 events; it also noted that the notebook's header table
of outcomes had not been removed before its review. In reply supp6 was changed
to partially reproduced, fig2 and supp9 were kept as reproduced on A1 and A3
with the disagreements recorded, a section varying one element of the
normalization at a time, a cluster membership check (adjusted Rand index
1.000), a group crosstab, per-neuron pause counts and a chance level for the
cue screen were added, and five questions went to a reader in
`questions/crcns-bf-3.yaml` (the R2 tolerance, the supp5 onset window, the
fig6b safety requirement, the one-start k-means reading and scaling (i) of
fig6-excited-peak-cue-vs-reward), a file written after the answer run, so the
questions are unanswered. Round 2 agreed with all 45 outcomes and found text
the outputs did not support, among them a cell saying two of four fig2
readings are within tolerance where three are, a statement that the baseline
length moves the means by at most 0.06 where one moves by 0.15, and a summary
saying most partial outcomes are values out of tolerance; in reply the text
was corrected. The author's run went from about 04:00 to 04:29 UTC, though the
start was given as 03:55; the notebook ran in 16 s at first and 35 s, 24 s and
33 s after the later runs, and two bugs fixed during development (a pause table
judging a different bootstrap draw than it printed, and a t-test handling zero
variance unlike Matlab's) were the only failures.

The Methods and the authors' scripts disagree on the firing normalization: the
Methods average trials of each type, subtract that type's mean firing in the 10
s before cue onset and Z-score over trial types, while cubeScriptPR25.m
subtracts from each trial its firing in the 2 s before cue onset, floored to an
integer rate, and Z-scores single trials. The paper's printed means, intervals
and betas match the scripts (Low firing danger onset -0.364 against the
paper's -0.37), the Methods' version gives values about twice as large, and
Z-scoring single trials in place of trial means accounts for the gap; this
decides most of the partial outcomes. The Methods screen neurons on mean rates
in Hz, while vpAnalysis.m floors each trial's rate first; the floored screen
gives the paper's 257 neurons from 153 sessions and the unfloored one 271 from
160, on which ancova-excited-no-baseline-effect and
fig4f-int-no-assignment-interval reverse. The paper's clusters are a local
optimum: with more starts k-means finds a partition with lower within-cluster
sum of squares (58/46/22, SSE 7254 against 7997), which moves 20 of the 126
neurons. Spikes, nose pokes and pellets were recorded only from 20 s before
each cue onset to 31.5 s after it, where an EVT14 event ends each window, so
the rest of each 3.5 min inter-trial interval is not in the files (177497 of
177598 pokes and 5871 of 5877 pellets fall in these windows), which the data
descriptor does not say. The descriptor does not say what the event channels
EVT01 to EVT14 hold or which carries which cue in each behavior program; only
cubeScriptPR25.m gives them, and its mapping agrees with the shocks (all 780
danger trials and 390 of 1560 uncertainty trials shocked 12 s after onset, no
safety trial), while EVT08 repeats EVT01 in every file and is not described.
The descriptor says VPcube.poke.base is the nose-poke rate over the 2 s before
the cue, where the cube holds the rate over the 20 s before it; it lists half
duration and amplitude ratio among the cube's fields, which the cube lacks; and
it describes mean waveforms for each trial type where each unit file has one
32-sample waveform. The files hold 195 sessions, one more than the paper's 194.
Four pairs of units recorded in one session share 70 to 88% of their spikes
within 0.1 ms and a fifth pair 49%, so they may be one neuron recorded on two
wires; they are counted as the paper counts them. The Methods subtract the mean
firing of the 1 s before reward delivery, while cubeScriptPR25.m takes 2 s to
1 s before it and only pellets delivered 18 to 2 s before or 14 to 28 s after a
cue onset. Questions are put to the paper's authors: whether the single
k-means start was intended and the cluster results hold on the lowest-SSE
partition, and whether the scripts' pause definition and the first 5 s of cue
used for the cue-cue correlations are those of Supplementary Figs. 5, 6, 8 and
9.

The author's points on the protocol: scripts in the data set that the paper
does not link have no defined status, so they were treated as the paper's code
with the Methods first; the rule that the Methods give the main result left
the main normalization unable to give the paper's numbers, which the scripts
give exactly, so the Methods' version was kept and a code_mismatch finding
recorded; there is no guidance on choosing the analysis groups the claims
depend on, so the scripts' groups were used as assumptions A1 and A2 with the
Methods' groups as a variant; the claims file called 100 k-means restarts a
choice that cannot change the outcome, which it does, so Matlab's one-start
default with the scripts' seed was followed and marked assumed; the rule to
count each recording once does not fit units that share only part of their
spikes, so they were kept with a finding; the per-rat breakdown is hard to
apply to about 45 claims, so one by-rat table was added; and the suggested
clock check of shifting events into the inter-trial interval cannot work when
those periods were not recorded, so a danger against safety contrast in time
bins was used.
