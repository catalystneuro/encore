I ran `tools/readme_row.py 001712 --write`, which added this row to README.md: 3 reproduced, 2 partially, 2 not reproduced, 11 blocked. I then added the subsection below to the end of `docs/pilot-notes.md`. Nothing is committed, and the attempt, its claims and its entry are unchanged.

### 001712, Davatolhagh et al. 2025

Three claims reproduced, two partially, two not reproduced and eleven blocked
on the dandiset. Round 1 had no attempt record and gave its own outcome for
each claim from the notebook with its conclusion cells and summary removed, and
agreed with all 18. Round 2 agreed with all 18 and nothing was proposed, so
there was no third round. The paper, a bioRxiv preprint, compares Nrxn1a
knockout and wild-type mice (8 against 11 mice, 10 sessions each) in the IBL
visual decision task with biased blocks, with widefield calcium imaging of
cortex and a linear encoding model, and reports that knockout mice shift their
choices less between blocks and adapt more slowly after a switch, and show
elevated cortical activity, higher correlations and variance, and a larger loss
of explained variance when movement predictors are shuffled. The psychometric
curve, the dependence of reaction time on contrast, the prior shift and
adaptation after block switches, the response to contralateral stimuli and the
encoding model's full cvR2 and movement contribution were tested on the one
session; the eleven claims that need mice of both genotypes are blocked as
`data_missing`. `fig1e-rt-contrast` is not reproduced (rho -0.053, p = 0.15),
while with reaction times above 0.15 s only the correlation is -0.226 (p =
0.00062) and 149 of 899 onsets fall at or before the stimulus.
`fig3b-contralateral-visual` is not reproduced because the criterion's peak
search found frame corners outside the brain; a masked variant puts the peaks
on opposite sides of the midline (p = 8.1e-15 and 1.6e-17) but does not show
the lateralization is visual, as paw speed, wheel velocity and motion energy
differ by stimulus side in the same window. `fig4c-full-cvr2` (0.471 against
0.486 to 0.660) and `fig4cd-movement-dominates` (movement drop 0.104 against
0.297 to 0.440) are partially reproduced on a design with the body camera's
video components only; with the side cameras added the full cvR2 is 0.574 and
0.525, within the range, and with folds that keep each trial's frames together
0.472 and 0.405, below it, and the paper's Results give 0.60 and 0.54 while its
Figure 4C legend says the trial time regressor was subtracted, under which
reading the values here are 0.123 and 0.133 (0.226 and 0.236 with all cameras).
Some outcomes rest on weak ground: in `fig2ef-block-adaptation` B sits at its
bound and tau is poorly determined (25.12 trials, SE 16.14, bootstrap interval
6.41 to 38.37), and in fig4cd, with folds by trial and the body camera only,
task exceeds movement over components (0.012 against -0.005), which the
criterion would count as not reproduced.

The dandiset was converted by CatalystNeuro
(catalystneuro/IBL-widefield-to-nwb). It holds one session of one mouse
(sub-FD-28), where the paper analyses 10 sessions from each of 11 wild-type and
8 Nrxn1a knockout mice, so eleven of the paper's findings, all comparisons
between genotypes, cannot be tested. The mouse's genotype is not given in the
NWB files, the dandiset metadata or the public IBL database (subject FD_28 has
an empty genotype list, from a query made by hand during the attempt); the
subject description is the paper's general description of the cross, and a
comment in the conversion script lists the session under knockout sessions,
next to a note that the list is a placeholder. Neither NWB file holds the
cortical landmarks or the registration to the Allen atlas that the conversion
code's documentation describes for the processed file, so no pixel can be
assigned to a cortical area, and the SVD spatial components cover the whole 540
x 640 frame with no brain mask, with large values at the corners in
stimulus-evoked maps. Both imaging planes give the indicator as GCaMP6f, where
the Methods and the file's keywords give GCaMP6s; the raw file's imaging planes
state an imaging rate of 15 Hz, where the timestamps give 31.2 Hz per channel
(32.03 ms intervals) and the Methods 30 Hz; and the dandiset's keywords and
description name "CNTNALP2", which is neither the gene of the paper and the
files (Nrxn1a) nor a correct spelling of Cntnap2. The wheel series state that
counter-clockwise is positive, but trials whose choice is labelled
counter_clockwise turn the wheel with negative velocity (95.5% of them 0.1 to
0.3 s after movement onset), while the choice labels agree with the rewards,
and the wheel movement onset is described as the first movement after the go
cue, but 151 of 899 onsets precede the go cue (by up to 0.18 s). Other
findings: the ROI motion energy series give the ROI position in pixels but not
the body part it covers; the dandiset has no published version; the paper's
analysis code is to be made public on publication, and the encoding code it
links (churchlandlab/chiCa) implements the model for single-cell data in
another task; and in the Figure 3 legend the correlation panel is labelled (E)
twice and (D) is missing, the correlation panel's legend says the KO minus WT
matrix shows reduced correlations where the Results say they are increased, and
the legend of panel C describes variance difference maps, as does panel E.

The notebook ran in 380 s in the first clean run, 6.6 minutes after round 1,
when a second notebook (`encoding_all_cameras.ipynb`) taking 21 minutes was
added for the side cameras, and 6.4 and 20.7 minutes after round 2. bioRxiv
returned rate limits for several minutes before the author got the PDF, refused
both verifiers and the first revision, and answered in the second revision,
whose full text confirmed the Figure 3 legend finding and gave reaction time as
the time to first movement without saying how that movement is detected. PyAV
could not open S3 URLs directly and the video was streamed through remfile, and
the author's first imaging clock check had no power and was replaced, while the
15 Hz rate, the wheel sign and the onsets before the go cue showed up only
during analysis and were added to the data check. Round 1's points led to
variants for fig1e, fig2ef, fig3b and the encoding model, none changing an
outcome, and the count of blocked claims in the README and a finding was
corrected from twelve to eleven. Round 2 found statements the outputs did not
support, among them the openalyx genotype result, a count of 17 sessions for 19
mice, where the IBL places its side-camera ROI, and "brain pixels" for a
brightness and margin mask, and these were labelled, removed or corrected.
Untracked files in the repository root that the author did not create were left
alone. The author's points on the protocol: no published version, where the
protocol allows a draft only for repeat attempts; a genotype that is unknown
while the paper reports values per group, so tolerances span both group means
and the schema takes a single value; outside data in a live database without a
pinned version; a time-shifted label check that fails where shifted windows
land in other lateralized task periods and block structure correlates labels
across trials; a criterion fixed in advance that hits an artefact; linked code
that does not implement the paper's analysis; and leaving out part of a model
for runtime, which the protocol does not cover.
