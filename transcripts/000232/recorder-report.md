I added the README row for 000232 (19 reproduced, 7 partially, 2 not reproduced, 1 blocked) and appended the subsection below to the end of `docs/pilot-notes.md`. Nothing is committed.

The `catalystneuro` field for this dandiset lists two contributors, Luiz Tauffer and Benjamin Dichter, and names no repository. So the opening sentence names the contributors, as the 000226 subsection does, in place of a repository.

### 000232, Chang et al. 2023

Nineteen claims reproduced, seven partially, two not reproduced and one
blocked, all on the dandiset. Round 1 gave its own outcome for each claim
from the notebook with its conclusions removed and agreed with 28 of the 29;
it gave not reproduced for `fig5b-first-hit-switches`, where both block counts
fail, and the author changed that claim from partially reproduced to not
reproduced, as the criterion allows a partial outcome only when one condition
fails. Round 2 agreed with all 29 and nothing was proposed, so there was no
third round. The paper reports that in mice switching between a
respond-to-touch and a respond-to-light rule, neurons and populations in MM
and ALM encode the rule before the stimulus more than those in S1 and S2,
that this pre-stimulus state shapes the touch response and tracks rule
switches, and that inhibiting MM or ALM before the stimulus lowers tactile
sensitivity. The recording and optogenetic session counts, task performance,
the fractions of selective neurons, rule and stimulus decoding with LDA, SVMs
and random forests, trajectory distances, subspace overlap, coding
dimensions, the first hits after a switch, state tracking across transitions
and the optogenetic effects on sensitivity, hit rate and laser-only licks were
tested; the claim on the histological probe locations is blocked as
`data_missing`. Some outcomes rest on weak ground: `fig1h-thit-tcr-selective`
and `fig2c-rule-prestim-units` are judged on the main seed, and on the means
over five seeds all four areas of both would be within tolerance, while on
single seeds fig1h MM is within tolerance in 3 of 5 and fig2c S1 in none; in
`fig6c-pre-inhibition-tactile` the ALM upper bound is 0.005, averages -0.001
(SD 0.003) over ten other seeds and is below 0 in 7 of 10, and the code's
resampling gives the paper's interval; `fig4c-prestim-distance-predicts-divergence`
gives p = 0.004 with the Methods' normalization and p = 0.001 with the
code's, and the units of the offset are not stated; in
`figs4h-choice-right-left` S2 is 0.422 against 0.32 and within tolerance in 1
of 5 seeds; the absence in `figs5-sensory-states-no-tracking` rests on wide
intervals; and in `fig6ij-laser-only-licks` the one failing interval, detection
task, MM, short laser, [0.045, 0.483], excludes 0 in all ten other seeds, but
the paper's detection intervals match none of the short, long or pooled rows.
The author read the full text of preprint version 2 from eLife's copy of the
reviewed preprint, as bioRxiv refused the download, and read the paper's
analysis code at commit 227631e for method choices the Methods leave open,
taking no data from it.

The dandiset was converted by CatalystNeuro (Luiz Tauffer and Benjamin
Dichter of CatalystNeuro are contributors). Sessions, mice and units per area
match the paper exactly, as do all 24 optogenetic session and mouse counts,
but the ephys files hold only the trials and units the paper analysed: no
trial has a lick between -1 and 0.1 s of the stimulus, gaps of 8 to 64 per
session remain in the trial times, the units are those passing the quality
filter and the 50 Hz cut, and the dandiset does not say that trials or units
were removed. Units carry only spike times and observation intervals, with no
quality metrics, waveforms, channel or depth, and ids that run from 0, so
units the paper names by cluster number cannot be identified; electrode x, y
and z are NaN in all 49 ephys files, locations are "unknown", and the
histology of Figure 1E is not deposited. The trials table columns have no
descriptions, and `response`, `blockType` ("Change" for the cue trial), the
opto trial types and the indicator columns are explained only by the paper's
code. In the 130 behaviour files `start_time` equals the stimulus onset, so
trial intervals overlap, and in the tactile detection files trials without a
whisker stimulus are labelled "Stim_Vis" and "Stim_Vis_NoCue" with a visual
stimulus type. Figure 5B's 88 and 91 switches equal the touch and light
blocks of the 40 recording sessions when each session's first block is
counted, against 63 and 75 non-first blocks with a hit. Other findings: the
Methods' soft normalization differs from the code's in the trajectory
distance, subspace overlap, coding dimensions and decoding, and the Methods
exclude sessions with fewer than ten units from the subspace analysis where
the code requires more than ten; the code's optogenetic bootstrap resamples
only hits; the coding-dimension code keeps 8, 7, 5 and 11 sessions where
Figure S4 reports 10, 8, 9 and 13; two laser trials start 1.6 and 2.7 s
before the reference time and one lasts 9.5 s; the stimulus-decoding check
could not establish a shared clock for three sessions, YT084 2020-02-02 and
2020-02-03 (AMM, 2 and 5 units) and YT086 2020-03-20 (MM, 5 units), which are
kept; and one of the 28 cross-modal sham sessions fails the code's own
performance check as ported here. The draft version has identical files and
differs only in contributor metadata.

Two test runs before the final one failed or gave wrong values, from a
pandas duplicate-index error, a string column in a median and a light-block
mask bug, all fixed before the final run. Untracked files in the repository
root that the author did not create were left alone. The author's points on
the protocol: a paper download that bioRxiv refused; a Methods rule that
leads the analysis although the reported numbers fit the code; no guidance
for a Methods step that may already have been applied to the files; a
criterion that could not decide, whose tie was broken after one area's result
had been seen; a reading not listed before the analysis that matches the
paper's numbers; an absence claim whose test in the paper is ambiguous; no
slot for code that is read but supplies no data; and no rule on whether the
main seed or the spread over seeds decides a bootstrap result.
