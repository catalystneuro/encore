I wrote the notes in `docs/pilot-notes/grosmark-2016-02.md` and the summary in `summaries/grosmark-2016-02.md`, and changed no other file. Nothing is committed. Before I started, `git status` already showed some untracked files I did not create, such as `.bashrc`, `.gitconfig`, `.idea`, `.vscode` and `scripts/`. The workflow may pick these up when it commits.

# grosmark-2016, Grosmark et al. 2016, second attempt

Fifteen claims reproduced, five partially, sixteen not reproduced and none
blocked, each tested on DANDI:000044 and CRCNS hc-11 together, which hold the
same recording; every outcome but `sessions-and-tracks` rests on an assumption.
The first verification round agreed with 26 of the 36 outcomes. The author took
its not reproduced for `place-cell-count`, `fig4a-rigid-faster`,
`figs14-plastic-ripple-gain`, `figs16ab-plastic-synchrony-increase`,
`fig4c-slow-replay`, `figs17d-rigid-plastic-coactivity` and
`figs18-temporal-bias`, kept `rigid-plastic-counts` not reproduced where the
verifier had partially, since the criterion has no partial outcome, streamed
the 11.7 GB of feature tarballs the verifier found for
`figs11-cluster-quality-similar`, which went from blocked to reproduced, and
averaged 100 shuffled templates for `fig2d-shuffle-high-dpcc`, which went from
partially to reproduced; against the verifier it moved
`fig2b-strong-contributors` to not reproduced by using one direction reading
for every claim. The second round agreed with 34 and gave
`fig4e-gain-sequences` and `figs16de-more-ripples-post` as not reproduced, for
the rule the author had applied to the others; the author proposed both, and a
third round agreed on fig4e and left figs16de undetermined until its ripple
event intervals are run under the other LFP threshold and sleep scoring, so it
stays partially reproduced with the proposal standing. It pins version
0.261106.0236 of the dandiset. The paper, Grosmark and Buzsáki, "Diversity in
neural firing dynamics supports both rigid and learned hippocampal sequences"
(Science 351:1440-1443), records CA1 in four rats in sleep before (PRE) and
after (POST) a novel linear or circular track, and reports that place-cell
sequences replay above chance in PRE, MAZE and POST, more in POST, that a
minority of strongly contributing cells splits at each session's median change
of contribution from PRE to POST (dPCC) into rigid and plastic cells, that
removing the plastic cells removes the POST increase, that plastic cells are
more spatially specific, with specificity rising over laps, and rigid cells fire
faster offline, and that the PRE to POST increase comes from slow-firing cells
and is limited to cells with a high within-ripple gain. The claims were written
from the NIH author manuscript with its supplement; the paper links no analysis
code. The replay claims of Figure 1, the rate split and the figs12, fig2e and
fig4d reruns reproduce under every reading tried, and fig2d under the adopted
yoking reading and reading (a) of "eliminated"; the place-cell count (573
against 491), the strongly contributing and rigid and plastic counts (246 and
120 against 216 and 105) and most of the group comparisons do not, and three of
the counts fall within tolerance with the 5 cm kernel read as its full width
(507, 232 and 112), a question now put to a reader in
`questions/grosmark-2016.yaml`. The notebook uses 200 null templates and 100
per-cell shuffles where the paper uses 1,000, since the full counts took over an
hour for five sessions; one session rescored with 1,000 of each agrees closely
(rZ r 0.996, PCC r 0.995). The attempt was blind, and against
`grosmark-2016-01` eleven outcomes differ, all because the claims file was
rewritten from the supplement. One preparation run failed on a Gatsby spike
beyond the stated session end, and the code was fixed. The author's first
notebook ran in 2105 s with peak memory 4.6 GB and the last in 1717 s; the
replay reruns differ in the third significant digit between executions, the
cause was not found, and no outcome changes.

The dataset was converted by CatalystNeuro (catalystneuro/buzsaki-lab-to-nwb).
The paper's derived data are not in the NWB files (major): no candidate or
ripple events, place-cell list, sequence scores, per cell contributions or rigid
and plastic labels, so every selection has to be rebuilt, and neither the paper
nor the dandiset links the analysis code. In Gatsby_08022013 the session
duration and the end of POST are 30413.6 s, but 263,976 spikes, the LFP and the
lab's state epochs continue to 32002.4 s. Position is sampled at 39.06 Hz where
the Methods state 39.69 Hz. On the circular maze the files do not say whether
the 30 cm reward area is excluded, and the NWB lap directions exist only for the
linear tracks; the lab's states have no quiet waking label, and Drowsy was taken
for it. The two datasets hold identical units, cell types, spike times and
states, and the hc-11 feature tarballs agree with the spikes, by a unit id rule
the data description does not state. Of the earlier attempt's findings, the
position rate, the missing EMG and accelerometer, the unknown electrode
locations and the undocumented circular running direction are fixed, the
Gatsby epoch end and the missing derived data remain, and the supplement was
available this time while the code is still not linked. In the paper, the
Methods test strongly contributing cells with a rank-sum test and the Figure
S19B legend with a signed-rank test, which give 13 to 24 and 217 to 249 cells.
Questions are put to the paper's authors on which part of the longer epoch the
yoking keeps, whether linear-track events are scored with both direction
templates, the LFP ripple detector, the Figure 2D shuffle, the width of the
5 cm kernel and which session firing rate Figures 4B and 4C sort by.

The author's points on the protocol: the hc-11 files are `.tar.gz`, not zip as
`docs/archives.md` assumes, and were streamed with `tarfile`; there is no rule
for cutting shuffle counts to fit the 60-minute limit, which was recorded as a
deviation; the five-seed rule cannot apply to a 35-minute pipeline and was run
only for the cheap random steps; running every reading through the chain of
dependent claims was not feasible, so one main reading was adopted as an
assumption; criteria that require both readings, when only one held, were
recorded as partially reproduced; quoting numbers from the run needs a second
full run that the protocol does not mention; and the schema's need for
`deviations` whenever `assumed: true` is not stated in the protocol.

---

The paper's replay findings hold up in this data: place-cell sequences replay above chance in sleep before and after the novel maze, more so after, removing the plastic cells removes that increase, and slow-firing cells carry it. The split into rigid and plastic cells does not reproduce as counted (120 of each against 105), a count that turns on how the smoothing kernel and running directions are read, which the paper leaves open. Several group properties also fail: rigid cells are not faster in every offline epoch, plastic cells do not sharpen over laps, and low-gain cells replay too. Plastic cells are more spatially specific on most measures. Supplementary findings on ripples and coactivity hold in part.
