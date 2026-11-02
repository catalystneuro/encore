# 001273, Semenov et al. 2025

Two claims reproduced on the dataset (one on an assumption), none partially,
one not reproduced and three blocked. Of the 11 claims on data elsewhere,
other dandisets of the same paper, one partially reproduced on an assumption,
one not reproduced and nine blocked. The first verification round agreed with
16 of the 17 outcomes as they stood and the second with all 17, and nothing was
proposed after the second, so there was no third round. It pins version
0.250805.1356; the paper cites none, and the two published versions have the
same 181 blobs and differ only in an added grant. The paper, Semenov, Kim,
Silkuniene and Pakhomov, "Excitation and polarization of isolated neurons by
high-frequency sine waves for temporal interference stimulation" in Cell
Reports Physical Science, stimulates cultured rat hippocampal neurons stained
with FluoVolt with sine waves and records optical APs by fast imaging, and
images membrane charging under 2-us pulses at 140 V/cm by pulsed laser strobe
imaging at 50-ns steps (Figure 4), the experiment of 001273. The claims were
written from the NIH author manuscript (PMC12320893) with its supplement; the
paper reports no original code. On the dataset,
`fig4-polarized-poles-face-electrodes` reproduces on reading "Up and Bottom"
in the session description as the image's vertical axis: in 13 of the 14
experiments that name the electrode axis the extreme pixels lie on opposite
sides of the soma centroid within 45 degrees of the field axis (median 13.8
degrees), and 1 of 14 with the axes swapped. `fig4-no-pole-difference`
reproduces, none of the 16 unscaled readings finding a difference at p < 0.05,
but weakly: 7 to 10 of 22 experiments per reading lose a pair to a failed fit,
and the |dF| over the last 0.5 us of the pulse, which needs no fit, is larger
at the anodic pole in set A (p = 0.014, ROI a). `fig4-pooled-time-constants`
is not reproduced, no reading putting all four means within the paper's SEMs
(cathodic discharging 1.37 to 4.20 us against 0.91 plus or minus 0.08).
`fig4-orientation-time-constants`, `fig4-discharging-slower` and
`fig4-full-charge-within-3us` are blocked as `metadata_insufficient`, the shape
and orientation groups not being in the dataset. Elsewhere,
`fig3c-sustained-firing-2s` is partially reproduced on DANDI:001030, the
criterion holding in 1 of 4 cells (c7) and its firing part in all 4, an
outcome that rests on judging each cell on its own, and
`figs1-di8-anepps-control` is not reproduced on DANDI:001272, no session
reaching the 5% depolarization level (largest 3.2%). The other nine claims are
blocked as other, not tested for lack of time. The author's first run gave the
same counts, with three of the blocked claims given as `too_large`. The author
asked a reader nothing, so the answer and author-answers runs changed nothing;
a reader question on whether the FluoVolt 5% level suits Di-8-ANEPPS was added
in the round-1 revision, after those runs. Round 1 disagreed only with fig3c,
giving not reproduced by the letter of the criterion, and found that its AP
detector counted noise on a depolarized plateau as APs (197 at c7 2.3 V), that
fits accepted tau up to 50 us from a 2-us window, that the fits used only the
nominal onset though a docstring said otherwise, and that the ROI square was
not clipped to the soma; in reply the detector was revised, after which c7
meets the whole criterion, fig3c was kept as partial with the disagreement
recorded, and variants with the estimated onset, with long-tau fits dropped,
with ROI a clipped to the soma, with the soma mask opened (12 of 14 pass) and
with the fit-free |dF| were added, none changing an outcome. Round 2 asked that
fig3c be marked assumed with its rule stated and that the three `too_large`
reasons be other, both done, and found sentences the outputs did not support
(a streaming time of 1,115 s, the survey of the other dandisets, the README's
file count, the figs1 AP readings and the no-pole wording), which were
corrected, the survey moving into a new notebook,
survey_other_dandisets.ipynb. The author's run took about 3 h 10 min (15:04
to about 18:16 UTC); the first full run exposed a wrong check of
`starting_time` and a wrong count of single files, both fixed. The notebooks
ran in 1349 s, 40 s and 81 s at first, the main one in 1,495 s after round 1,
and the survey notebook in about 9 minutes. `tools/build_site.py` was found
modified before the revisions and left untouched.

The dataset holds only the raw strobe images: the ROIs over the de- and
hyperpolarized poles, the debris ROI used to scale out laser-flash
fluctuations and the shape and orientation group of each experiment are not in
it, so the group comparisons of Figures 4D and 4E cannot be made and the time
constants cannot be recomputed as the paper did. The January 17 files say
"Electrode position not specified", and no file says which electrode was the
cathode or how the camera image is oriented relative to the named directions.
The files form 22 runs of 7 or 8 replicates plus six single files at 100 V,
where the paper reports 19 experiments, with nothing saying which runs were
used; the nominal amplitudes are 40, 60, 80, 100 and 130 V where the paper
gives one field, 140 V/cm, and no file gives the field. Files recorded "in a
backward manner" are stored in acquisition order, so their frames run back in
time, which the files do not say beyond the stepping direction. The time base
(50 ns per frame) is given only in prose, the ImageSeries rate is the camera's
6 Hz, and starting_time holds a Unix time where NWB expects seconds after the
session start. The 13 subjects are cells, with age P18D for neurons dissected
at E18 and cultured about one week. The Results give 180 images per replicate
and the Methods 160; the files hold 160. The first image of 156 of 175 files is
about half as bright as the rest, and 204 frames in all were dropped as dim.
Across the paper's deposits, DANDI:001034 holds the same 178 image arrays as
DANDI:001032 under other subject ids, every session description of 001032 to
001035 names the NaCl solution so the sodium gluconate thresholds of Figure 3B
do not appear to be deposited, DANDI:001272 holds three Di-8-ANEPPS neurons
where the paper reports eight, and DANDI:001030 gives the species as Mus
musculus, with two of its 17 sessions ending at 1.91 s, before the 2-s stimulus
does. The 2-us, 257 V/cm pulse recordings of the nine cells of Figures 5 and 6
are not in 001273, whose files date from January and March 2024. A question is
put to the paper's authors: the size and placement of the pole ROIs, how the
fits were weighted, whether the discharge amplitude was free, and whether the
ROIs, the debris ROI and the list of the 19 experiments with their groups could
be deposited.

The author's points on the protocol: a claim marked elsewhere whose data are
not there cannot be `data_missing`, and `other` was used; `too_large` covers
only a computation that stopped, not a claim never started for lack of time;
no rule covers experiments that cannot be matched to the paper's (22 runs
against 19), and both all 22 and the 15 at 40 V were run; the protocol does not
say whether the author may read another dataset's claims file that a criterion
points to; it does not say whether findings may rest on surveys run outside the
notebooks; the main notebook's 22.5 minutes, nearly all streaming, is over the
10-minute aim; and without the debris ROI the paper's flash correction cannot
be repeated, so unscaled traces were used with whole-frame scaling as a
variant.
