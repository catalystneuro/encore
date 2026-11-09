I ran `readme_row.py`, which added the row to README.md (30 reproduced, 4 partially, 10 not reproduced, 13 blocked). I added the subsection below at the end of docs/pilot-notes.md. Nothing is committed, and the attempt, claims and entry are unchanged.

`targets/dandisets.json` has no entry for this dataset. It is listed in `targets/ebrains.json` instead, and its `catalystneuro` field there is empty, so the dataset paragraph does not open with the CatalystNeuro sentence. The repository root also has untracked files I did not create (`.bashrc`, `.gitconfig`, `.idea`, `scripts` and others); I left them alone, and they should be kept out of the commit.

### ebrains-q0fg-1x8, Nagelhus et al. 2023

Thirty claims reproduced, four partially, ten not reproduced and thirteen
blocked on the dataset, which is on EBRAINS and holds MATLAB files. It pins
version v1, the only published version, whose DOI is the one the paper cites.
The author put eight questions to a reader; the answers made the rate-map
method of the paper's calculateRateMap.m (the rate per bin, unvisited bins 0,
then smoothed) the one reading for every rate map, took the vector-map bins of
`ovs-method-extra-cells` from the paper's reference 12, which the reader looked
up outside the paper and its code, and named as readings the details the paper
does not give. This moved ten claims from blocked and the totals from 25
reproduced, 2 partially, 7 not reproduced and 23 blocked to 30, 7, 7 and 13;
among them `fig1c-object-tuned-fraction` became partially reproduced (222 of
1189 CA1 cells, 0.1867, within 0.199 +/- 0.0199). Round 1 gave its own outcome
for each claim from the notebooks with their conclusions and summaries removed
and agreed with 41 of 57. `fig1e-object-cells-and-object-vector-cells` and
`fig7-slope-variant` moved from partially reproduced to not reproduced and
`figs5d-control-sessions` from blocked as `other` to `data_missing`, as round 1
gave. The author kept seven claims blocked as `methods_underspecified` where
round 1 gave an outcome, as readings of the claims file give different
outcomes, kept ovs-method-extra-cells blocked because its pass rests on an
exclusion rule the claims file does not give, and kept fig1c,
`fig1d-field-distances`, `figs4-object-traces` and
`fig7-single-cell-properties` partially reproduced. Round 1 also found that
`figs7e-downsampled-words` chose the words of each trial separately, which
leaks the trial label; the words are now chosen once per session and distance
bin, as the criterion says, and the claim stays reproduced (80 of 80 pairs, p =
7.9e-15). Round 2 agreed with 56 of 57, now accepting the three kept partial
outcomes, and would record figs4-object-traces as not reproduced, as its trace
fraction is 0.061 to 0.098 against 0.183 +/- 0.0183 under every reading; the
author proposed the change, and a third round, which reviewed only that claim,
agreed, so it is not reproduced. The paper, "Object-centered population coding
in CA1 of the hippocampus" in Neuron, records CA1 and CA3 cells with tetrodes
and Neuropixels probes in rats foraging in an open field without an object,
with one, with it moved and without it again, and reports that 19.9% of CA1
cells are object-tuned, that a Bayesian decoder tells the trials with and
without the object apart from population activity, with accuracy falling with
the rat's distance from the object, and that population words carry more
information than spike counts. The cell counts, object tuning and fields, the
changes between trials, the decoders and their controls, the words, single-cell
distance tuning and the cell subsets were tested. `fig1g-no-experience-effect`
and `fig1h-cross-day-stability` are blocked as `data_missing` because no cell
identities across days are deposited, `figs2c-no-proximodistal-effect` because
no implant sites are, figs5d because the control populations are not and
`figs6hij-behaviour-matched` because there is no head direction; eight claims
are blocked as `methods_underspecified` because their readings disagree.
`figs3a-ca3-object-tuned` is not reproduced (0.191 and 0.326 of the 341 CA3
cells against 0.23 +/- 0.023), `fig6ef-least-tuned-cells` because the 124
least-tuned cells of the 620-cell session give a bin 1 minus bin 5 difference
of -0.346 and -0.344 against 0.121, so accuracy rises with distance, and
`figs6-behaviour-decoders-flat` because the occupancy decoder depends on
distance (H = 22.8, p = 0.0001), though the same decoders show the same
dependence between the halves of the trial without the object, so the failure
may be the attempt's. Some outcomes rest on weak ground: fig1c misses only on
the control level, 9 of 219 (0.0411) against 0.0503 +/- 0.00503, which does not
differ from the paper's 11 of 219 (p = 0.64); fields are taken as the regions
above 3 x MAD, not the Methods' iterative contour from the peak, and the
failures of fig1d, fig1e and figs4 may depend on it; and in
`figs8eh-least-tuned-smaller-datasets` the kept fraction of 0.4 is at the edge
of 0.6 +/- 0.2.

The two Neuropixels population files (populationanalyses_27012.mat and
populationanalyses_27207.mat) give a tracking y equal to x in every sample,
while singlecellanalyses_CA1.mat holds the same recordings with the same
timestamps, x and spike trains and a y of their own, which the decoding
notebooks use. No cell identities across days and no day of exposure to the
object are deposited, nor the implant sites (the data descriptor says histology
is not shared) or head direction, as tracking holds timestamp, x and y only. Of
the 425 tetrode units of the population files, 283 have no match in the CA1
single-cell file and carry no identifier, so they have no Object Moved or No
Object' trial and no object-tuning status. The population files hold the No
Object and Object trials only; the other two trials of the decoding sessions
exist only for the 3 to 15 cells per tetrode session that the single-cell file
gives, and the control file gives each cell once, so only one control session
has 25 or more cells. The CA3 file holds 341 cells from 4 rats (221 of them
Neuropixels) where the paper counts 313, and which cells the paper used is not
documented. The paper's code holds no single-cell rate maps, field detection,
object-vector score, population vector correlation or sampling analysis, and
the object-vector method does not say which cells its exclusion removes (28.8%
of CA1 cells). Other findings: in CA3 session 3 (rat 25987) the Object trial's
object is 61.4 cm from the centre and the Object Moved trial's 9.0 cm, the
reverse of the protocol; three units of singlecellanalyses_CA1.mat have spike
times out of order within the Object Moved trial; 4 of 1189 CA1 units have more
than 1% of ISIs under 2 ms and 7 rates outside 0.05 to 10 Hz as computed from
the trials; 26 of 273 gaps between trials exceed 10 min (up to 4.1 h), where
the Methods describe 1 to 3 min, and trials last 913 to 2334 s, not the 1800 s
the Methods assume; the Methods use 15 tetrode decoding sessions and the
legends 14, and the dataset holds 14, with the two Neuropixels sessions 16 in
all; and the tracking unit is stored as a MATLAB string object that non-MATLAB
readers return as an opaque object, its value (centimeters) recoverable only
from the raw bytes. The 1,189 CA1 cells and 219 control cells match the paper.

The full clean run took 66 minutes over six notebooks (4, 19, 8, 19, 10 and 6
min), after notebook 2 was cut from 37 minutes, and the first decoder runs,
made on the copied tracking, were run again. A run on the answers was cancelled
partway; the next run checked and finished its code and ran everything again,
with notebook 01 the longest at 12 minutes and a second full run giving the
same numbers, and `entry.py check` reported no errors throughout. Round 1's
points led to a count of the fig1d fields beyond the bound (2 to 19 cells), a
field variant joining bins only along edges, per-session occupancy decoder
accuracies and the control without the object, 100 subsets per size for
`fig6c-subsets-decline`, per-session CA3 counts, a figs2c variant using the
cell counts' proximodistal order in the Supplementary Figure 2C legend and a
listing of every field of every file, none changing an outcome beyond those
above. Round 2 found three loose sentences, a miscopied p bound for
`figs3f-ca3-changes`, figs8 trends said to hold at every size and a range of c
given for one subset reading only, and these were corrected. Questions on field
detection, the figs7e word selection, the figs2c legend order and the
ovs-method-extra-cells exclusion are open. Untracked files in the repository
root that the author did not create were left alone. The author's points on the
protocol: it does not say whether readings the author adds must agree, which
first blocked 18 claims as `methods_underspecified`; the dependency rule blocks
claims whose result is the same under every reading, such as fig1f; it does not
say how to combine a criterion's readings when it does not say "under one
reading"; it does not cover correcting a data error in one file from another
file of the same dataset; it assumes a random seed cannot change an outcome,
where the t tests of figs5e can flip; it has no rule for a criterion that
passes when a value it expects is outside tolerance, as with H in
`tables1-without-bin-1`; it has no rule for criteria without a partial case;
the 10-minute aim does not fit 57 claims run under four combinations of
readings; archives.md gives no way to list EBRAINS versions, does not suggest
recording file hashes and does not mention MATLAB string objects; and its
suggested clock check does not fit when trial membership comes from the file
structure, so spikes were shifted against positions instead.
