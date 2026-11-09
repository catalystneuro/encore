# crcns-ofc-4, Schuck et al. 2016

Ten claims reproduced (four on an assumption), six partially (two on an
assumption), five not reproduced (one on an assumption) and eight blocked,
three as metadata insufficient and five for missing data. The first
verification round agreed with 27 of the 29 outcomes as they stood and the
second with all 29; nothing was proposed after the second, so there was no
third round. CRCNS does not version data sets, so the version is recorded as
unversioned with the data set's DOI (10.6080/K0FN14CH), and the zip's MD5,
which matches `checksums.md5`, is recorded for change detection. The paper,
Schuck, Cai, Wilson and Niv in Neuron, scans 30 adults (27 analysed) in a
face-house age-judgment task whose 16 hidden states combine the previous and
current category and age, and decodes these states from the orbitofrontal
cortex with a linear SVM on per-state beta maps; the data set holds the 24
participants of the paper's trial-wise analysis, with fMRI time series inside
each participant's OFC mask in native space, AFNI design matrices, drift and
motion nuisance terms and per-state event files. The claims were written from
the PyMuPDF text of the version of record with its Supplemental Information;
the paper links no analysis code. The check changed ten claims, among them
the time-out reading of the error rate, a bootstrap reading for the hidden
components and all four components of the permutation control, and left open
the location of the searchlight peak, which the main text and Table S1 give
differently, the paper's 26 cardiac regressors and Figure S3B, which has no
claim. The behavioural claims on reaction times and on errors, the OFC
decoding, similarity and error-trial claims could be tested; the training,
whole-brain, searchlight, other-region, motor and synthetic-data claims could
not. Reproduced are `supp-errors-stable-over-blocks`,
`supp-errors-not-by-age-category`, `supp-rt-stable-over-blocks` (chi2(1) =
1.74, p = 0.19 against the paper's 1.7, p = .18), `supp-rt-faces-faster`
(945.8 and 1012.5 ms), `supp-rt-by-trial-class`, `fig2b-current-age-absent`,
`fig2b-two-back-absent`, `figs2c-8way-decoding` (15.89% with maps z-scored by
voxel, 14.79% and outside tolerance by map), `fig2c-enter-cluster` (p =
0.0097, 20 of 24 participants) and `figs5-euclidean-distance`, where with each
state's correct-trial count held constant distance and error rate are not
related, so the result may come from trial counts. Partial are
`supp-errors-by-trial-class` (Enter 4.79% against 3.4 +/- 0.34, Exit and
Internal together 0.60%), `fig2a-16way-decoding` (8.93%, above chance but
outside 10.98 to 13.42%), `fig2-two-back-state-space`,
`fig2b-hidden-components` (previous category only),
`figs2a-permutation-control` and `fig4a-decoding-error-correlation` (r =
-0.268, p = 0.21). Not reproduced are `fig2d-enter-nonenter-decoding`, the
three fig4b error-trial claims and `fig5-similarity-predicts-errors`. Most
error claims rest on counting one error per block, a lower bound, and on
reconstructing the state of Enter errors from the neighbouring trials (39
under a strict rule, 98 under a span rule); the decoding claims rest on
z-scoring the beta maps by voxel, as the Princeton MVPA toolbox's zscore_runs
does, with the per-map reading shown throughout. The author's first run had
11 reproduced, 4 partially, 6 not reproduced and 8 blocked: it called
`supp-errors-by-trial-class` and `fig2-two-back-state-space` not reproduced
and `fig4b-error-vs-matched` reproduced. The author asked no questions of a
reader, so the answer and author-answers runs changed nothing. Round 1
disagreed on the first two and found that the trials inside an error block
lay in no regressor, neither reading of how post-error trials were left out
(O3), that errors were undercounted, that the error-trial comparison was
confounded by trial class, that the Euclidean result was coupled to trial
counts and that the decoded signal may be slow; in reply both O3 readings
were built from the error blocks (16-way 8.10 to 9.38%), the block composition
and a trial-count control were added, a class-matched comparison was adopted,
which made `fig4b-error-vs-matched` not reproduced on an assumption, and the
paper's conflict on which trial is repeated after an error went to a reader
in `questions/crcns-ofc-4.yaml`. Round 2 noted that this outcome goes against
the criterion as written, which passes under voxel z-scoring, asked that
`supp-errors-stable-over-blocks` be marked assumed and found numbers and
sentences the outputs did not support; in reply the text was corrected and a data-check cell showed
that correct Enter trials decode at 0.90% because the voxel-z-scored
classifier names an Enter state on 5.60% of labelled volumes, not because of
signal lag. The author's session ran from 18:44 to 20:10 UTC; two development
runs failed on statsmodels mixed-model errors (a missing attribute and a
singular matrix), which were fixed. The notebook ran in about 5.5 minutes at
first, 258 s after the author-answers run, 3.4 minutes after round 1 and 5.1
minutes at the end. The untracked files in the repository root were left
alone.

Each 'err' event is a block that starts at an error trial and runs over its
repetitions and often the trials after it (spans 6.8 to 41 s), which the data
descriptor does not say, so the number of errors, time-outs, error reaction
times and the state of most error trials cannot be read from the files; one
error per block gives 1.92 or 1.98% and every designed trial in a block 3.10%,
bracketing the paper's 2.3%. The 'err' column of the design matrices follows
a short event at each block onset (r 0.83 to 0.98), not the boxcar from
stimulus onset to button press that the descriptor describes. The OFC time
series carry no voxel coordinates or mask, so no smoothing, searchlight or
other spatial analysis can be done. The data set holds 24 of the paper's 27
participants and the OFC only, with no training session, whole-brain data,
hippocampus, DLPFC or PPA/FFA, cardiac regressors or per-trial response
mapping and side. Enter errors are 181 of 225 error blocks after a run's first
trial (79% of all blocks, where the paper's class rates imply 48%), which
points to Internal and Exit errors being undercounted or merged into blocks.
In Subj-01 run 4 a 'HoHy' trial follows a 'HoHy' trial, which the task rules do
not allow, and three runs (Subj-11 run 3, Subj-18 runs 4 and 5) have no
'first' event or column, which the descriptor does not mention. The Figure 1B
legend and the Methods disagree on which trial is repeated after an Internal
error. Questions are put to the paper's authors: how the beta maps were
z-scored within each run and with what kernel they were smoothed; and how
errors were counted and error-trial states labelled, given that the shared
event files merge each error with its repetitions.

The author's points on the protocol: when a criterion has no clause for a
partial outcome it does not say whether an effect that holds in part may be
called partially reproduced, so not reproduced was recorded; the data-check
step assumes trial tables carry correct labels and says nothing on
reconstructing them, so the reconstruction became a helper rule with two
readings and its outcomes were marked assumed; the clock check's shifted-label
decoding is written for spike data, so for fMRI the regressors were shifted and
the volume lag swept, which shows the clocks consistent only to about two TRs;
the protocol is silent on mixed models that do not converge or are singular, so
a random-intercept model was used and one singular fit left out; and the
archive notes give no way to check the version beyond the zip's MD5, so the
whole zip was streamed to compute it.
