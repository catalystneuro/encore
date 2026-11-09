I ran `python tools/readme_row.py 000010 --write`, which added the row to README.md: 8 reproduced, 3 partially, 5 not reproduced, 11 blocked. I then added the subsection below at the end of `docs/pilot-notes.md`. The `catalystneuro` field for 000010 is empty, so the second paragraph does not open with the CatalystNeuro sentence. I followed the shape of the earlier subsections, so the run details sit in the last paragraph, ahead of the protocol sentence. Nothing is committed.

### 000010, Li et al. 2015

Eight claims reproduced, three partially, five not reproduced and eleven
blocked on the dandiset. It pins version 0.220126.1905, the only published
version, as the paper cites none. The author put seven questions to a reader;
the answers changed four outcomes. They made all trials (t1) and trials
without the tagging light (t2) readings of every electrophysiology claim of
Figs 2 and 3, either of which may decide, so `fig2c-population-dynamics` and
`fig3f-pt-contra-preferring` moved from blocked to reproduced; they named
three readings for picking out the antidromic spike, so `antidromic-latencies`
moved from blocked to partially reproduced; and they made all labelled cells a
substitute population, not a reading, so `fig4h-pt-contra-imaging` moved from
not reproduced to blocked as `metadata_insufficient`. Round 1 gave its own
outcome for each claim from the notebook with its conclusions and summary
removed and agreed with 25 of 27. `ed1-fast-spiking-properties` moved from
partially reproduced to not reproduced, as fast-spiking neurons have higher
baseline rates but are not less selective (0.750 selective against 0.733,
median absolute rate difference 1.46 against 0.62 spikes/s). The author kept
`imaging-selectivity-counts` as partially reproduced; round 2 agreed with 26
of 27 and gave it as not reproduced, since its criterion has no partial
clause and no reading puts all five values within tolerance (0 of 16). The
author proposed the change, and a third round, which reviewed only that
claim, agreed, so it is not reproduced. The paper, "A motor cortex circuit for
motor planning and movement" in Nature, records units in left ALM, with PT and
IT neurons tagged by antidromic photostimulation, and images ALM with two
photons in mice discriminating pole position with their whiskers in a delayed
licking task, and reports that photoinhibiting ALM in the delay epoch biases
licking to the ipsilateral side, that ALM neurons show preparatory and
movement-related selectivity, that contra-preferring neurons outnumber
ipsi-preferring ones among PT neurons but not among IT neurons, and that
photostimulating PT neurons biases licking contralaterally. The behaviour,
unit classes and tagging counts, selectivity and its time course, population
dynamics, error trials, fast-spiking properties, antidromic latencies, PT and
IT selectivity and the imaging counts were tested.
`fig2d-preparatory-perimovement` is not reproduced because 272 to 294 neurons
are peri-movement only against 389, `fig3f-pt-contra-selectivity` because PT
selectivity never reaches P < 0.05 (P = 0.12 to 0.36),
`fig4f-spatially-intermingled` because 57 of 64 combinations find clustering
of same-preference cells at P < 0.05, and imaging-selectivity-counts because
the closest reading has 1,417 selective cells against a lower limit of
1,417.5. The two photoinhibition claims of Fig. 1, the six photoactivation
claims and the anatomy claim are blocked as `data_missing`, and
`reaction-time` as `methods_underspecified`, because the number of s.d. the
paper does not give moves the mean across mice from 40.2 to 129.1 ms. Some
outcomes rest on weak ground: `behaviour-performance` holds only with the mean
over sessions (early licks 11.6% against 14.3%, but 14.5% pooled and 14.7%
over mice); `fig2e-no-contra-bias-spikes` holds on the paper's test as written
(P = 0.82), but in the 570 ms before the go cue all four tests give P = 0.022
to 0.050 with a contralateral excess, and the criterion sets no rule for a
claim of absence across its readings; fig3f-pt-contra-preferring holds only
with the light trials kept (30 of 45, P = 0.010; 26 of 45, P = 0.14 without
them) and only with light and no-light trials pooled; and
antidromic-latencies has all four measurable values within tolerance in 1 of
18 combinations, in which keeping spikes within 0.5 ms of the peak bounds the
s.d.

The dandiset holds none of the photoinhibition (Figure 1) or photoactivation
(Figure 5, Extended Data Figures 3, 6 and 7) data and no histology, so nine of
the paper's findings cannot be tested, and the Ai32 mice that are in it have
no record of light; it holds 23 of the paper's 42 task mice. Every unit
labelled PT (45) or IT (27) is a second copy of a unit labelled Pyr in the
same file, with an identical spike train, so the 1,441 units are 1,369
distinct units. The 39 units of intermediate spike width that the paper
recorded and excluded are not in the dandiset, which does not say so, and the
activated neurons that failed the collision test (22 from the pons, 106 from
ALM) and the 7 that could not be tested carry no label. In 75 sessions the
antidromic tagging light was delivered during behavioural trials (4,332 of
14,388 correct trials in those sessions); the trial tables do not flag these
trials, which can be found only from the laser traces, whose series have the
description 'no description'. The laser power series are labelled 'watts' but
hold the milliwatts of the Methods (47.1 and 82 at the pulses). The
extracellular trial tables hold 1,540 trials with a lick instruction and no
behavioural events, 1,447 of them marked 'right', 'hit' and 'no early' and
lasting exactly 5.5 s, and 1,345 with no spike from any unit; they look like
placeholders for removed trials, would raise performance if taken as given,
and are not the photoactivation trials (1,502 are in the sessions with
tagging light and 7 in the Ai32 mouse 218693). The imaging files flag no
trial as an early lick, so early-lick trials cannot be excluded there, and no
imaging plane gives its depth, so the layer 5 populations of Figure 4g, h
cannot be selected (the files label 843 included cells IT against the paper's
542 in layer 5). Other findings: the imaging mice are given the genotype
'Rosa-lsl-tdtomato' (one) or none (three), where the Methods use C57Bl/6Crl
mice; the ROI labels include 'Pyr' and 'interneuron', which the paper does not
describe, and the `included` flag does not state its rule, with 424 included
ROIs not 5% brighter than their neuropil; the `lick_trace` series is not
described as the photodiode signal used for reaction times, and its level and
direction differ between sessions (median baselines 0.069 to 4.83 a.u.; it
falls after the go cue in 15 of 99 sessions); 66 extracellular trials without
an early lick have a go cue that is not 2.6 s after the sample event and 75
have none; spikes are stored almost only within 5.5 s trial windows, so
baselines before the trial cannot be measured in most sessions; and the paper
links no analysis code.

The notebook ran in 711 s in the first clean run, 665 s after the answers,
1,200 s after round 1 and 1,062 s after round 3, and `entry.py check`
reported no errors. After round 2 the first run failed on a dropped
connection to DANDI and the second passed. The author listed the groups of
only the first file at first and missed the laser traces of the 75 sessions,
which the extra analysis and slower streaming then came from. Round 1's
points led to a check that the tagging light is balanced between trial types
(0.295 of lick right and 0.307 of lick left correct trials), an F0 check of
the imaging baselines, a search of every text field of the 59 imaging files
for a depth, a breakdown of the placeholder trials by mouse and the timing
filter applied to the behaviour. Round 2 found statements the outputs did not
support, among them 4,332 light trials given as part of 18,385 correct
trials, spikes said to be stored only within trial windows where two sessions
have 24% and 30% between trials, a measured value for fig2e taken from a
reading where the absence test fails, and an untested explanation of the PT
result, and these were corrected. Untracked files in the repository root that
the author did not create were left alone. The author's points on the
protocol: it says to judge a claim of absence on the paper's test alone, yet
the fig2e criterion names readings; its rule that any matching reading
reproduces a claim and its rule that disagreeing readings block one leave
unclear how readings the author finds combine with those of the claims file;
it has no outcome for a claim part of whose data is absent; step 1.1 could
say to list every group in every file; and streaming the laser traces pushed
the run past the 10-minute aim.
