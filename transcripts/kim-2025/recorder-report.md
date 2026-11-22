I wrote the two new files, `docs/pilot-notes/kim-2025-01.md` and `summaries/kim-2025-01.md`, and changed nothing else. Nothing is committed. `tools/readme_row.py kim-2025` prints 3 | 0 | 0 | 0 because it counts only the three claims tested on dandiset 000248 itself. The link claim and the 24 claims on the Allen data in dandisets 000021 and 000022 are left out, so the notes give those separately.

# kim-2025, Kim et al. 2025

Three claims reproduced on the dandiset, none partially, none not reproduced
and none blocked, plus the claim linking the dandiset to the paper's example
session, reproduced; the 24 claims on the Allen Visual Coding Neuropixels data
(`data: elsewhere`, read from dandisets 000021 and 000022) are counted apart,
21 reproduced and 3 blocked. Eighteen outcomes rest on an assumption. The
first verification round agreed with every outcome as it stood, though it
would have given `fig2b-decoding-falls-with-slope` the reason other, and the
second agreed with all 28; nothing was proposed after the second, so there was
no third round. The paper, Kim and Shin, "Neural variability structure in
primary visual cortex is optimal for robust representation of visual
similarity" (bioRxiv preprint of July 2025), fits the log variance of V1 spike
counts against the log mean across neurons, finds a slope near 1, and by
rescaling the trial residuals to slopes from 0 to 2 reports that
dimensionality falls and manifold overlap rises with the slope, while
continuity, alignment of manifolds with visual similarity and the consistency
of representations within and across mice are best near slope 1. Dandiset
000248, the OpenScope Illusion data, serves only the Isomap pictures of one
example session (sub-630506); the claims were written from a text extraction
of the preprint without figure panels, with the equations taken from the
paper's code at commit ac3300b. The Illusion claims reproduce in the example
session under every reading run (the three stimuli at slope 0 form a component
of 1, 3 as-is). On the Allen data the unit counts (66.9 +- 25.5, 2008 in all)
and the across-neuron slope (1.0489) match only with AllenSDK's default units,
those labelled good, and this was assumed for every Allen claim; the slope
manipulation, overlap, continuity, geodesic, alignment and consistency claims,
the behavioural state, higher-area and movie checks and the shuffle comparison
reproduce. `figs6-higher-areas-consistency` passes only the criterion's first
reading, which within sessions cannot tell slope 0 from slope 1, and this went
to a reader in `questions/kim-2025.yaml`. Blocked are the decoding claim of
Figure 2B as `too_large` (run at as-is and slopes 0 and 1 over 30 sessions and
at slope 2 in four, with the 22 conditions estimated at about 5.4 hours), and
the gain variance fits and the tangent space angle as other, not ported within
the time of the runs. The author's first run gave 23 reproduced, 1 partially
and 4 blocked. Round 1 found that the good units were used for two claims
only, that the movie session count was 24 against the paper's 23, and that
the decoding and shuffle claims could be tested in part; in reply the good
units were used throughout, the paper's code was found to skip
sub-769319621 for invalid movie presentations, which moved
`figs5a-movie-slope-near-1` from partial to reproduced, and
`figs4c-shuffling-alters-dependence` was tested in a third notebook and moved
from blocked to reproduced. The verifier of round 1 saw the Allen notebook's
conclusion cells, which the handover had not removed, and based its outcomes
on the code outputs. Round 2 asked that the movie outcome be marked assumed,
that the shuffled and original decodings share trial order and folds, and
that the slope-2 timing be run in the entry, and found sentences the outputs
did not support, all corrected. The author's run took about 3 h 32 min (23:36
to 03:08 UTC); the Allen notebook first ran in 2698 s and took 61 minutes,
over the limit, before the first revision, and the three notebooks ran in 14,
41 and 49 minutes at the end.

The ICwcfg1 presentations table lists every 400 ms frame of the block,
including the gray inter-trial frames, under one column; the gray frames show
the same image as the Blank stimulus, nothing marks which of them are Blank
trials, and the image codes 0 to 21 have no names in the files or the
dandiset metadata, so the names come only from the paper's code. The trials
can be recovered from the sequence (60 leading gray frames, then trial and
gray frame alternating, 400 Blank trials in every session), and the templates
agree in kind with the code's names; the code read a post-processed copy
(v240130) that is not public. The units table describes none of its columns.
The spikes share the clock of the ICwcfg1 table: the V1 population rate rises
75 ms after image onsets and not after Blank onsets, and image identity is
decoded from the 400 ms after onset (0.576, chance 0.083) and not from the
400 ms before (0.089). No session is deposited twice, and all 11 sessions the
code lists are present, with a twelfth, sub-619293, that it does not list. In
dandiset 000021 the pupil area is labelled Pixels ^ 2 but ranges from 0.0002
to 0.012. Two questions are put to the paper's authors: whether the units
were those of AllenSDK's default units table, and which third Functional
Connectivity session was excluded, since no session in dandiset 000022 has an
incomplete movie repeat and the paper's code names sub-769319621, whose movie
block overlaps an invalid_times interval, which the Methods' word truncated
does not describe.

The author's points on the protocol: claims on data elsewhere made up most of
the paper and the protocol gives no priority between them and the dataset's
own claims; the rule of five seeds is too costly for the overlap halves and
the decoding; no block reason fits a claim not attempted within the time
limit; a finding about an input dataset, here the pupil area units, has no
place in the record; the protocol does not say whether to apply defaults of
the software the paper used to read the data, here AllenSDK's good filter;
and timings printed in a notebook change from run to run, so a conclusion
that quotes them exactly breaks on re-run.

---

The paper's main findings held up, tested mostly on the Allen Neuropixels sessions it analysed, since dandiset 000248 (OpenScope Illusion) holds only its example Isomap pictures, which reproduced too. Across V1 neurons, log variance rose with log mean at a slope near 1 (1.0489 against 1.048), and when that slope was rescaled, manifold overlap rose while alignment and the consistency of representations within and across mice peaked near 1. These results assume the paper used AllenSDK's default units labelled good, which the Methods do not state. The fall of decoding accuracy with slope was too slow to run in full, and the tangent space angle was not implemented in time, so neither was tested.
