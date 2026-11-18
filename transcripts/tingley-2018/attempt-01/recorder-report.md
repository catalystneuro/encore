I added the README row for 000213 (3 reproduced, 8 partially, 9 not reproduced, 5 blocked) and the subsection below at the end of `docs/pilot-notes.md`. Nothing is committed.

The `catalystneuro` field gives a contributor, not a repository. So the opening sentence of the second paragraph names the contributor, as the 000061 and 000114 notes do.

### 000213, Tingley et al. 2018

Three claims reproduced, eight partially, nine not reproduced and five
blocked. Round 1 gave its own outcome for each claim from the notebook with
its conclusions removed and agreed with all 25, though for the three assembly
claims it gave `too_large` as the reason for the block, and it said that
`fig5-assemblies` and `ls-information-lower` could have been tested. The
author then changed six outcomes: `fig5-assemblies` from blocked to not
reproduced on a random 1% of pairs, `ls-information-lower` from blocked to
partially reproduced, `ls-few-place-fields` from not reproduced to partially
reproduced, `fig1i-hpc-rate-phase-equivalent` and `fig6d-cfc-stronger-ca3`
from reproduced to not reproduced, and `ls-place-fields-unstable` from
partially reproduced to not reproduced, after place fields were found on the
Gaussian rate map the paper's code uses and sessions were grouped as the
criterion states. Round 2 agreed with all 25, accepting the two blocked
assembly claims with a reservation, and nothing was proposed, so there was no
third round. The paper reports that lateral septum (LS) neurons in rats
encode position in the theta phase of their spikes more than in their rate,
while hippocampal place fields carry it equally in both, and relates this to
recording depth in the LS, to hippocampal-LS assemblies, to theta coherence
and theta-gamma coupling with CA1 and CA3, and to a spiking model. The unit
counts, phase and rate decoding of position, place-field fractions,
properties and stability, information across smoothing scales, the depth
gradient and onset phase, coherence and coupling with CA1 and CA3, ensemble
decoding, peak information and assemblies were tested on the five rats, with
the linearized position, trial conditions and theta channel rebuilt. The two
claims that need the assembly strength of every pair are blocked as
`not_runnable` (about 12 process-hours), speed independence as
`methods_underspecified`, the maze rotation of Figure S6 as
`metadata_insufficient`, since nothing marks a rotation, and the spiking
model as `other`. Some outcomes rest on weak ground:
`fig1i-hpc-rate-phase-equivalent` fails on KS p = 0.044 over 531 fields,
against the paper's 1,820; the hippocampal field fraction is 10.5% against
31.7%, and the code's rule dropping peaks whose SD across trials exceeds
their mean accounts for most of the shortfall; `fig4d-depth-gradient` and
`fig4e-onset-depth` assume that the first depth in the session name is the
LS depth; and `fig2-ls-phase-beats-rate` is not reproduced although phase
beats rate in 58 of 58 sessions. The author used the full text of the NIH
author manuscript (PMC6605060) and did not read the supplementary figures.

The dandiset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is
a contributor). The paper's processed behaviour is not in it: the linearized
position, the trial conditions used for every rate and phase map, and the
CA1 pyramidal layer channel used as the theta reference in each session must
be rebuilt, and several outcomes depend on how. Units have no waveform,
recording site or channel of largest amplitude, so the within-session depth
analyses of Figure 4 cannot be repeated. The two depths in each session name
are not described, so which is the LS probe cannot be told, and the `hpc`
unit label is not defined as CA1. In every session the hippocampal channels
and units carry one label, hpc or ca3, where the paper's Figure 6A counts 63
CA1 and 19 CA3 sessions, more than the 67 files. The dandiset holds 1,696 LS
units and 3,217 hippocampal units (2,593 hpc, 624 ca3) against the paper's
1,647 LS and 2,951 hippocampal units, and 20,979 pairs of active
hippocampal and LS units against 11,264 examined, and which units the paper
left out is not documented. Other findings: eight DT8 files state position
in mm but hold metres; in all 67 files the z column of position is a copy of
y; in eight of the eleven DT2 files the position timestamps repeat or go
back; 11 units in six files hold spike times out of order; every DT2
electrode, and those of two DT9 files, is labelled `unknown`, and DT2
positions are in pixels with no scale; DT7 20170317 has 43 units with no
region or group and DT7 20170324 has no units; trials on the linear track
and in two DT8 alternation files carry no type or direction; in DT9 20170501
the trials do not match the positions, and DT2 20160221 suggests an offset of
up to a second; the head-orientation quaternion in
`allocentric_frame_tracking` states its unit as meters; the paper's code
names its place-field file for a 20% threshold but applies the 1% default,
where the Methods state 20%; the functions for phase binning, information and
assembly detection and the session files the figure scripts read are not
public; and 42 files chunk the LFP across all channels, so reading one
channel means reading the whole LFP.

During exploration a script that scanned the HDF5 chunk index hung and hit a
30-minute timeout, and the run crossed midnight, so the given date was used.
Untracked dotfiles in the repository root, which the author took to be
sandbox placeholders, were left alone. The author's points on the protocol:
a clock check where a constant offset between spikes and positions cannot be
seen by analyses that are consistent with themselves; count claims whose
criteria can only be written after the data check; no rule on whether to
rebuild missing derived data or block the claims; no word on trying a
reduced subset before blocking a claim as not runnable; no category for a
claim about a model that uses no recorded data; a 10% tolerance that means
little for a value near 100%; no guidance on designing the partial-outcome
rule; following code that calls unpublished functions; and which date to
give a run that crosses midnight.
