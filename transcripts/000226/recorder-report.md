I ran `python tools/readme_row.py 000226 --write`, which added this row to README.md: 12 (+2) reproduced, 2 (+1) partially reproduced, 0 not reproduced, 11 blocked. I then added the subsection below at the end of `docs/pilot-notes.md`. Nothing is committed, and the attempt, its claims and its entry are unchanged.

### 000226, Severson et al. 2017

Twelve claims reproduced, two partially and eleven blocked on the dandiset.
With outside data, counted apart: two reproduced and one partially. Round 1
gave its own outcome for each claim from the notebook with its conclusions
removed and agreed with all 28; round 2 agreed again and nothing was
proposed, so there was no third round. The paper reports how
Merkel cell-associated afferents and other slowly (SA) and rapidly (RA)
adapting afferents of the mouse whisker follicle respond to active touch and
to whisking: touch responses explained by the bending moment (M0) and its
rate of change in statistical and viscoelastic models, direction selectivity,
a subset (WT*) tuned to whisk phase with preferred phases spanning the cycle,
responses that remain or vanish after progressive whisker cutting, and
comparisons with whisking EMG. The link to Table S1, frame counts, Merkel
minutes, baseline, touch and WT* rates, direction selectivity, the spline
models in place of the paper's GAMs, the viscoelastic fit, phase modulation
and its span and invariance, the kinematic models, nasolabialis motor units
and curvature noise were tested, with experiment groups taken from Table S1
as labels and afferent type and Merkel identity from it as outside data. The
claims on the progressive cutting experiment are blocked as
`metadata_insufficient`, and those needing the intrinsic protractor EMG, the
remaining whisker length, the optogenetic tagging, the histology and the
manually curated contact frames as `data_missing`. Some outcomes rest on weak
ground: `fig5e-phase-span` turns on a Rayleigh p of 0.047, which is 0.062
with the circular mean of the tuning curve; in `fig3d-gam-best-pair` M0 and
M0' ranks second of 45 pairs, at 0.622 against 0.633 for M0 and velocity,
also with lambda 100 and on held-out frames; `figs6-kinematic-gam` uses 15 of
the paper's 28 afferents; `fig5-phase-modulation` and `sigma-kappa` pass on
the paper's spreads while the non-preferred rate is 16% and curvature noise
28% above the paper's values; and `fig3a-direction-selective` reaches 65%
against the criterion's 80%. The author used the accepted manuscript in
PubMed Central (PMC5528144) and took the supplement holding Table S1 from the
publisher's file server, as PubMed Central and Europe PMC returned a
challenge page.

The dandiset was converted by CatalystNeuro (Benjamin Dichter and Luiz
Tauffer of CatalystNeuro are contributors). Its 60 files match Table S1 one
to one, but they do not say which experiment each recording belongs to, the
afferent type, which afferents were identified as Merkel afferents or the
whisking and touch class, and the three recordings the paper excludes (227C,
214A, 271A) are held without saying so. In the 13 progressive cutting
recordings every trial has cuttingGroup "intact" and MOI has one value per
file, although the whisking-in-air rate falls over most sessions (last fifth
below half the first in 10 of 13), so the cut conditions appear to be in the
files under the wrong label and Figure 6 and parts of Figure 7 are blocked.
The EMG files 7A, 8A and 9A hold tracked whisker series but no EMG signal,
11A holds nasolabialis spike times but not the EMG, and the optogenetic
tagging data, the histology, the whisker geometry and the curated contact
frames are not deposited. Velocity, acceleration, jerk, dM0, dFaxial and
dFlateral are stated per second but are per millisecond (median ratios 0.467
to 0.502), and the stored whisk phase is the negative of the Hilbert phase,
so phases from -pi to 0 are retraction, which neither the files nor the
paper describe. Other findings: every series has the description "no
description", distanceToPoleCenter has unit "unknown" and fits the Methods'
distance from whisker to pole in mm, and Mi, dMi and other series are not
explained; trial stop_time is 6.998 s after start_time while each trial holds
5 s of frames; the spike times of KS0277A are not sorted; KS0125_ and KS0128_
lack the unit letter of 125B and 128D, and all session start times are
12:00; some series hold extreme values, such as whisker position from -985 to
596 degrees, that are not flagged; the cut-whisker recordings 199B and 209A
hold distance-to-pole series and contact frames (5,014 and 32) that the files
do not explain; and the paper's analysis code is available only on request.
No recording is deposited twice.

Streaming the files by range requests took 22 minutes for the metadata
alone, so the notebook reads each file whole into memory. The first two runs
gave wrong model results from a diverging spline fitter and a badly
conditioned viscoelastic fit, both fixed without changing a criterion, and
in the last revision the viscoelastic results moved slightly from round 2
(difference -0.030 against -0.029) with the same code, data and locked
packages, for a cause not found; refits from three other sets of random
starts keep the outcome. The round 1 verifier could not download the
supplement and round 2 found the Table S1 check unshown, so the notebook now
fetches and parses Table S1 on every run, which needs access to the
publisher's file server. The author's points on the protocol: no case for a
table from the paper itself as input; the paper's stated spread as tolerance,
which makes median and IQR claims nearly untestable; streaming that is slow
for files of many small datasets; a step that assumes public code exists; no
rule for fixing bugs in the attempt's own code after seeing outputs; whether
to block or test a subset when a model can be fitted on 15 of 28 afferents;
and small ambiguities in the link rule for the EMG ids and in a blocked claim
with two reasons.
