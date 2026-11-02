I wrote the note in `docs/pilot-notes/001260-le-merre-2026-01.md` and changed no other file. Some untracked files in the repository root (`.bashrc`, `.profile`, `.idea`, `scripts` and others) were not created by me; I left them alone, and they should be checked before the workflow commits.

# 001260, Le Merre et al. 2026

Seven claims reproduced (four on an assumption), five partially (four on an
assumption), four not reproduced and four blocked, all four as
`methods_underspecified`. With outside data, counted apart: four reproduced,
one partially and nine blocked, seven as `methods_underspecified` and two as
`too_large`. The link claim `zenodo-unit-link` is reproduced, and the five
claims on the IBL Brain Wide Map, data in another archive, are blocked as
`too_large`. The first verification round agreed with 32 of the 40 outcomes as
they stood and the second with all 40, and nothing was proposed after the
second, so there was no third round. It pins version 0.250911.0744, the only
published version. The paper, Le Merre, Heining et al., "A prefrontal cortex
map based on single-neuron activity" in Nature Neuroscience, records
Neuropixels units in 66 mice across 99 recordings in passive listening and
auditory tasks (dataset KI), sorts wide-waveform (ww) and narrow-waveform (nw)
units by firing rate, burstiness (B) and memory (M) of their spontaneous
activity on a self-organizing map (SOM) into categories, and maps the
enrichment of these categories, and of tone responses, across the subregions
of the prefrontal cortex (PFC), relating it to the cortical hierarchies of
Harris et al. and Gao et al.; it replicates parts on the IBL Brain Wide Map.
The claims were written from the version of record, which was read without
its Supplementary Information, and from the paper's code (pfcmap at commit
9ae52edd), which runs on intermediate files from Zenodo 14205018; the attempt
used those files and dandiset 000473 as inputs. The counts of dataset KI and
of the waveform classes (24,898 units, 52.4% in the PFC, 99 recordings, 13,040
PFC units; 19,731 ww, 4,247 nw and 920 unclassified), `fig1i-nw-higher-metrics`,
`fig2b-pfc-regular-territory`, `fig2e-category-stability` (58.0% against 16.7%
from the marginals, on assumed blocks), `fig2g-pfc-regular-enrichment`,
`fig5b-tone-categories`, the dataROI parcellation (39 dataROIs against 42 ± 4),
`fig4cd-dataroi-enrichment`, `fig5e-tone-responsive-patches` and
`extfig9e-tone-responsive-no-hierarchy` reproduce. Partial are
`extfig1d-sleep-like-differ` (B and M differ, log10FR does not, p = 0.14),
`fig2a-som-memory-burstiness`, `fig2f-low-rate-less-stable`,
`extfig3f-layer-enrichment`, `extfig5g-nw-enrichment` and
`fig5cd-tone-maps-cross-subregions`. Not reproduced are
`extfig1-epoch-counts` (a median 9.9% of sleep-like time against 6%, and 73.5
sleep-like epochs against 19), `extfig1f-burstiness-memory-uncorrelated` (slope
-0.197, p = 7.0e-75, marginal R2 0.025), `fig2j-nw-ww-correspondence` and
`fig5j-tone-responsive-high-rate`. Eight enrichment and hierarchy claims are
blocked because their outcome differs between the claims file's two readings
of how a retrained SOM's clusters take the paper's category numbers (G2), as
is `supptable5-no-hierarchy-within-pfc` through its dependency on
`fig3a-harris-regular-positive`, `fig4e-activity-modules` because its two
readings of "ILA-specific" disagree, and `methods-settings-no-difference`
because the paper names no test; the six other IBL claims and
`fig5i-map-similarity`, through its IBL dependency, were not started in the
run's time. The author's first run gave 10 reproduced, 6 partially, 5 not
reproduced and 19 blocked. The author asked a reader nothing at first, so the
answer and author-answers runs changed nothing. Round 1 disagreed with eight
outcomes and found that the sleep-like detector, run per probe, marked 100% of
the time in Poisson populations of 10 to 20 units at 3 Hz, that the counts
followed a rule of 12 active epochs where the unit quality control passage
says 12 epochs, and that the analyses used 001260 alone; in reply detection
was pooled per session and skipped where a Poisson null is marked 1% of the
time or more, the counts followed the quality control passage, variants on the
paper's 42 dataROI polygons, on all of dataset KI and on the paper's own
trained SOM were added, and a question was put to a reader on the GaoROI
numbering of `fig4g-pl-orbl-extremes`. The change of detector alone moved the
outcomes of several SOM claims, two of them from blocked to partially
reproduced and `fig4g-gao-category1` from not reproduced to blocked. Round 2
agreed with all 40 and asked that the session-skip rule be labelled as the
attempt's own and not the paper's, found three sentences the outputs did not
support (the fig2i notes, the p-value of the settings finding and the files
with a Block column), all corrected, and asked for the claims that moved with
the detector to be run on the paper's own sleep-like periods; on them
`fig2g-pfc-regular-enrichment` would be blocked and `extfig5g-nw-enrichment`
and `fig4g-gao-category1` not reproduced, and a second question to a reader
asks how G2 should number the categories. The author's run took about 1 h 55
min (12:31 to about 14:26 UTC) with nothing failing in the final runs, two bugs
of development runs having been fixed; the notebook ran in 970 s at first, 585
s after the author-answers run and 17 minutes after round 1 and at the end.
Untracked files appeared in the repository root and edits to
`tools/build_site.py` and `tools/site_assets/progress.js` were found, none of
them the runs' own, and were left untouched.

The paper's dataset KI is split across two dandisets: 001260 holds 74
recordings, 41 mice and 20,374 units, and the other 25 recordings (25 mice,
9,408 units) are in 000473, whose title and metadata name a different paper
(Esr1+ hypothalamic-habenula neurons), and neither says it holds part of
dataset KI. Together they hold 29,782 units, the paper's count before its unit
quality control, and no field marks the 24,248 units the paper kept; the
paper's quality flags, the flatmap position of each unit and the paper's ww/nw
labels are only in its Zenodo metrics files, which match all 20,374 units by
recording and unit id. The units table's two-column `quality` is described
only as "ISI violation, false positive rate", and its column 0 runs from 0 to
1.15e5 (median 2), so it is not the ISI violation ratio of the Methods'
threshold of 0.1. Following the Methods, sleep-like periods take a median
9.9% of each recording (6% in the paper; per-probe detection gives 20.0%),
while the paper's own detection files on Zenodo give a median 5.3% over 73
recordings and mark 19 recordings as not using the detection (off_used = no),
a selection step the Methods do not describe; the code's detector differs from
the Methods (off periods of more than 50 ms where the Methods say 5 ms, among
other parameters) and gives 8.7%. The Methods' "at least six spikes
(corresponding to at least four ISIs)" counts five ISIs as four, and the
Methods say 99 probes were lowered and 24 recordings excluded while Data
availability gives 99 recorded sessions, the number the two dandisets hold.
The behavioral setting of a recording is not a field and can be read only from
the session description and keywords. In Detection and Context files the trials
columns `lick` and `valve` are described as "sound amplitude", in Detection
files `Block` holds the trial outcome (miss, hit, correct rejection, false
alarm), in a Context file `sound` is False for all 524 trials though 524 tones
were played, and every electrodes column is described as "my description". For
283 of 20,374 units the location label differs from the paper's Zenodo files
(207 of them in PL064_20200422-probe0), and the ww/nw label differs for 3.0%
of units. Questions are put to the paper's authors: what rule carries the
category numbering to a retrained SOM, or whether a reanalysis should project
units on the trained SOM (on which 4 of the 8 claims blocked under G2 hold),
which test supports "not significantly different across behavioral settings",
where a mixed model finds differences (Aversion against Passive in B, p =
0.0021), which recordings had an inherent block structure and how it is
stored, and what decided that a recording's sleep-like detection was not used.

The author's points on the protocol: the rule that a claim depending on a
blocked claim is blocked for the same reason blocks `fig3a`, `supptable5` and
`fig5i` although parts of them were computed, and it was followed with the
results in the notes; some criteria define no partial outcome, and partially
reproduced was used where part of a claim held under every reading; there is no
case for a paper's dataset split across two dandisets, one filed under another
paper, and 000473 was used as a pinned input for the counts and the dataROI
count only; the protocol does not say whether the author may add a link claim
and edit `data` and `depends_on`, which was done; `too_large` is defined for a
computation stopped part-way, not for IBL claims never started for lack of
time; the claims file's rule to block when the two category numberings
disagree overrides step 1.6, and it was followed, blocking 8 claims; the fig4e
criterion is ambiguous when both readings fail; and the clock check compared the
post-minus-pre spike rate at true tone onsets with onsets shifted by 1.5 s, on
10 files, in place of decoding.
