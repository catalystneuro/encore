# kim-2022, Kim et al. 2022 (second attempt)

Six claims reproduced, three partially, three not reproduced and 13 blocked,
12 as `dataset_missing` and one as `data_missing`; all 12 tested outcomes rest
on an assumption. The first verification round agreed with 23 of the 25
outcomes and the second with all 25, so there was no third round. This is the
second attempt on the paper and the first under pilot-14, which files records
by paper: the earlier attempt, `kim-2022-01`, tested 000489 alone under
pilot-12, and this one also uses 000448, now among the paper's datasets in the
registry, pinning versions 0.230518.1811 and 0.230421.1844. The claims file was
written again for the paper, with 25 claims against 22. The paper, Kim,
Semenov, Kiester, Keppler, Ibey, Bixler and Pakhomov, exposes monolayers of
bovine pulmonary artery endothelial cells to unipolar and bipolar pulses from
two needle electrodes, measures YO-PRO-1 (YP) uptake against the field strength
along the line bb' between them, and reports how far a second phase of opposite
polarity cancels electroporation as its amplitude, the pulse number, duration
and repetition rate change, with strobe imaging of membrane charging at the
poles of CHO cells loaded with FluoVolt. The claims were written from the
accepted author manuscript in PubMed Central (PMC9729435); the paper has no
supplement and links no code or data deposit. The six claims on Fig. 2 were
tested on 000489 and the six on Fig. 7 on 000448. The 12 claims on Figs. 3 to 6
are blocked because their dishes are not in either dandiset; 000548, 000549 and
000550 name the paper and match those figures by title, but they are not among
the paper's datasets in the registry and were listed under `missing_datasets`.
`fig1e-heating` is blocked as the thermometry is in neither. On Fig. 2,
`fig2a-uptake-rises-with-field` is reproduced under the unpaired t-test (5 of 5
amplitudes, p = 0.0001 to 0.044; the paired test passes 3 of 5), and
`fig2c-inhibition-flat-above-8-7` is reproduced with ROI on both sides of the
centre, though with one side only it would not be.
`fig2b-exponential-same-slope` is partially reproduced, as the exponential
beats a line for 3 of 5 amplitudes and no slope differs; `fig2c-weaker-at-6-7`
is partially reproduced, as 100% pulses pass and 50% pulses give p = 0.049
against the p < 0.01 required. `fig2a-vertical-scales` is not reproduced (the
largest 75% mean plus s.e.m. is 339 a.u., above the 250 a.u. axis), and
`fig2c-max-inhibition-50-75` is not reproduced, as the 50% second phase leaves
49.3% of the unipolar mean against 20 +- 2% and the p < 0.01 test holds at
most at 7 of 10 fields. On Fig. 7, the mirror-image polarization of the two
poles (+22.1% and -20.7% at 600 ns), the bipolar overshoot, the alternation in
833 kHz trains and the summation without build-up are reproduced;
`fig7-charging-time-constant` is not reproduced, as the charging tau of 191 ns
matches but the amplitude of 23.2% (expected 31 +- 3.1) and the discharge tau
of 613 ns (expected 520 +- 52) do not; and
`fig7-later-pulses-same-tau-difference` is partially reproduced. Round 1
disagreed on `fig2b-exponential-same-slope`, which it held not reproduced, and
on `fig2c-weaker-at-6-7`, first recorded as reproduced, where 50% passed only
by pooling every dish and ROI value as independent; the author moved
`fig2c-weaker-at-6-7` to partially reproduced with one value per dish, moved
`fig2c-max-inhibition-50-75` from partially to not reproduced by requiring the
test at every field, and kept the fig2b outcome, recording the disagreement,
as the criterion names no outcome when the slopes agree and the exponential
fails. Round 2 agreed with all 25; on its points the record now says that the
criterion's literal pooling would make `fig2c-weaker-at-6-7` reproduced and
that the 100% pass rests on a unipolar mean of 19 a.u. from 2 dishes, and a
pole-region variant leaving out membrane that faces a neighbouring cell was
added, which changes no outcome. The author asked a reader no questions, so
the answer and author-answers runs changed nothing. The author's run took
about 2 h (03:20 to 05:20 UTC); about 1 h was lost when a footprint search by
direct convolution hit its 60-minute timeout and was replaced by FFT
convolution, and a background download was killed when its shell call ended
and was run again in the foreground. The notebook ran in 494 s at first, 798 s
after round 1, 755 s after round 2 and 514 s in the reconcile run. The
reconciliation with `kim-2022-01` was blind; it traces the Fig. 2 changes of
outcome to the rewritten claims file (the unpaired test, one Fig. 2B reading)
and to differences in method (0.2 mm footprint discs against 0.5 mm, the high
field ROI), and the Fig. 7 outcomes to the change of protocol. `tools/entry.py
check` still reports 3 errors, as the earlier record has no outcomes for the
three Fig. 7 claims added to the claims file.

000489 holds only the 17 dishes of Fig. 2 and one sample image named for Fig.
1F, and 000448 the strobe images of Fig. 7; the dishes of Figs. 3 to 6 and the
thermometry of Fig. 1E are in neither, and the registry's list of the paper's
datasets and the 000489 title, which the claims file follows, do not point to
000548, 000549 and 000550. 000448 holds 5 unipolar and 4 bipolar cells, where
the paper reports 18 and 17, without saying how the 9 were chosen, and it counts
18 subjects because each cell's forward and reverse trials have different
subject ids (for example 001_F and 001_R for cell09). The YO-PRO-1 channel of
sub-Fig2-0-03 (unipolar) and sub-Fig2-25-04 (25% bipolar) is the same image,
value for value, while their MemBrite channels differ and the two files give
session dates of 2021-07-29 and 2021-07-26; with it left out the unipolar and
25% groups have 2 dishes each. Dish numbers run up to 18 while 17 dishes are
deposited, and nothing says which dishes were left out or why; all unipolar
dishes are from 2021-07-29 and all 75% and 100% dishes from 2021-08-24, and the
100% dishes take up more YP than the unipolar ones (largest mean 750.5 against
650.8 a.u.; higher at 9 of 11 ROI within 2 mm of the centre), where Fig. 2C
shows every second phase inhibiting uptake. The 000489 images give no pixel
size (resolution -1), electrode positions or polarity, ROI positions or values,
or field per ROI, so 0.65 um per pixel was assumed, which the electrode spacing
supports (4.44 to 4.66 mm against 4.5 mm in Methods), and the field was
recomputed for two cylinders and scaled to the paper's 15.1 kV/cm at the
centre. The 000448 files give no pole regions, field direction or delay of each
frame, and the reverse-trial files store frames in acquisition order with a
response offset of 74 frames (1.85 us) from the forward trial (75 for cell24),
neither documented; the darkest frame is the first in 10 of 18 files, and 5
files have frames below half their median frame mean, consistent with failed
laser flashes. The series description of the Fig. 2 files names "Channel1" for
both filter sets and describes 144 images (12 x 12) of a well of a six-well
plate, where Methods 2.5 describes 216 images of 35 mm dishes, and three files
share the series name Fig2_25. Each 000489 file stores its stitched
two-channel image as one ImageSeries of shape (22323, 22323, 2) at 2.0 Hz with
unit n.a., so it reads as 22323 frames of 22323 x 2 pixels, and the two
channels of sub-Fig1F are the same image. Two questions are put to the
paper's authors: how the ROI were placed along bb' and whether the t-test was
paired, and how the pole regions were drawn, where the cathode was relative to
the image and whether the poles of a group of cells were taken on its outline
or on each cell.

The author's points on the protocol: the claims file lists the Fig. 3 to 6
claims under 000489 although other public datasets of the paper hold them, and
neither `data_missing` nor `dataset_missing` fits exactly; the protocol says to
count duplicated recordings once but not what to do with a channel shared by
two files of different conditions; some criteria give no outcome for some
cases, such as fig2b when the slopes agree and the exponential fails, or
fig2c-max, which does not say at how many fields the test must hold; and the
advice to develop on a subset says nothing about caching data during
development.

---

Summary (`summaries/kim-2022-02.md`, 118 words):

In this data the paper's membrane charging results mostly held up, its results on how a second phase cancels electroporation held only in part, and its findings on pulse number, duration and repetition rate could not be tested, as those dishes are in other dandisets. Strobe imaging reproduced the mirror-image polarization of the cell poles, the bipolar overshoot and alternation, and summation without build-up, but not the fitted charging amplitude or discharge time constant, possibly because few of the paper's cells were deposited. Uptake rose with field and its inhibition was flat at high fields, but a 50% second phase left 49.3% of unipolar uptake, not about 20%. The exponential rise and weaker low-field inhibition held in part.

---

Notes on the run:
- Four of the five most recently added notes have since been renamed or removed. I matched the shape of `shi-2013-01.md`, the one still there, and of the earlier `kim-2022-01.md`.
- The `catalystneuro` field is empty for both dandisets, so the second paragraph does not open with the conversion sentence.
- I wrote only the two new files. `git status` also lists some untracked files that I did not create or touch: dotfiles, `.idea`, `.vscode` and `scripts`.
