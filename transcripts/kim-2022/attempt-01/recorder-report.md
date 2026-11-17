I wrote the notes in `docs/pilot-notes/000489-kim-2022-01.md` and changed no other file. The other untracked files at the repository root (`.bashrc`, `.vscode`, `scripts` and others) were not created by me. Here is the subsection:

# 000489, Kim et al. 2022

No claim reproduced, one partially, four not reproduced and 17 blocked, and
the second verification round agreed with all 22 outcomes. It pins version
0.230518.1811; the paper cites no version, and the draft holds the same files.
The paper, Kim, Semenov, Kiester, Keppler, Ibey, Bixler and Pakhomov, exposes
monolayers of bovine pulmonary artery endothelial cells to trains of unipolar
and bipolar nanosecond and microsecond pulses from two needle electrodes,
measures YO-PRO-1 (YP) uptake against the field strength along a line between
them, and reports how much a second phase of opposite polarity cancels
electroporation as its amplitude, the pulse number, duration and repetition
rate change, with strobe imaging of membrane charging in CHO cells. The claims
were written from the accepted author manuscript in PubMed Central
(PMC9729435); the paper links no code and no data deposit. Only the six claims
on Figure 2 were analysed, as the dandiset holds only that experiment, and
four outcomes rest on assumptions: the ROI positions, the footprints for YP_0
and MB_0, a pixel size of 0.65 um, camera counts taken as the paper's units and
the field per ROI, recomputed in closed form for two cylinders from the
geometry of Methods 2.3, which gives 15.38 kV/cm at the centre against the
paper's 15.1. `fig2a-uptake-rises-with-field` is partially reproduced: mean YP
rises with field for all five amplitudes (Spearman rho 0.98 to 0.99), and the
strongest ROI exceeds the weakest at p < 0.05 for 50, 75 and 100% but not for
unipolar (2 dishes) or 25%. `fig2a-vertical-scales` is not reproduced, as the
largest 75% mean plus s.e.m. is 283.2 a.u., above the 250 limit;
`fig2b-exponential-same-slope` is not reproduced, as none of 12 readings meets
both parts of the criterion; `fig2c-max-inhibition-50-75` is not reproduced,
as the 50% second phase leaves 54.5% of the unipolar mean averaged over the
range and 31.6% at its lowest, against about 20%, with p < 0.01 reached in only
one of 36 per-ROI tests; and `fig2c-inhibition-flat-above-8-7` is not
reproduced under every variant, as the percent of unipolar rises towards 8.94
kV/cm for every amplitude. `fig2c-weaker-at-6-7` is blocked as `other`, as the
unipolar mean at 6.75 kV/cm is -8.6 a.u. (s.e.m. 19.6), at background, so the
ratio measures nothing; with the bottom side alone or the left footprint alone
it is reproduced. The 15 claims on Figures 3 to 7 are blocked as `other`, as
their data are in dandisets 000548, 000549, 000550 and 000448, which name the
paper but which the claims file does not name as sources, and `fig1e-heating`
is blocked as `data_missing`. The author's first run gave one partially
reproduced, four not reproduced, one blocked as `methods_underspecified` and
16 as `data_missing`. The author asked a reader no questions, so the answer run
and the following author run changed nothing. Round 1 agreed with 20 of 22
outcomes; it found that the fig2b reading labelled partially reproduced, a
category the criterion does not define, was the only source of the
disagreement, and that fig2c-weaker divided by a unipolar mean at background,
and the author moved fig2b to not reproduced and fig2c-weaker to blocked. Its
points also led to the sibling dandisets being named in each blocked claim, a
per-ROI p-value table and two more placements of the fig2c-max test, a check
that 000548 holds the missing unipolar image, variants with the field scaled
to 15.1 kV/cm and with the weakest ROI at 2.0 and 2.4 mm, and the removal of an
invalid variant that counted a 25% image as unipolar. Round 2 agreed with all
22, so there was no third round; it found sentences the outputs did not fully
support, among them largest p values given for 50% alone and polynomial fits
said to cross zero at both cutoffs, which were corrected, and noted that the
Figure 2C outcomes still rest on 2 unipolar dishes. The author's run took
about 1 h 20 min (15:31 to 16:51 UTC) and nothing failed in the final runs;
during development a range request was reset, and retries were added, and a
newline escape broke a notebook cell. The notebook ran in 519 s at first, in
10.7 min after round 1 and in 559 s in the last run.

The dandiset holds only the Figure 2 experiment (17 dishes, 5 pulses at 1 Hz
with a second phase of 0 to 100%) and a sample image named for Figure 1F, so
16 of the 22 claims cannot be tested on it; those of Figures 3 to 7 are in
000548, 000549, 000550 and 000448, but nothing in 000489's metadata or files
points to them, and 000448 holds 9 cells (5 unipolar, 4 bipolar) against the
paper's 18 unipolar and 17 bipolar. The YP channel of the unipolar dish
sub-Fig2-0-03 is identical to that of the 25% dish sub-Fig2-25-04, while their
MemBrite channels differ; it registers with 25-04's MemBrite channel (peak
0.454) and not with its own (0.028), so the unipolar group has 2 dishes, and
000548 holds the true image as sub-Fig3-Uni5-03 (peak 0.301), which was not
measured as it is outside this dandiset. The files give no pixel size,
electrode positions, ROI, field per ROI, footprint values or pulse voltage, and
name the channels only in free text; the data are consistent with 0.65 um per
pixel (electrode centres 4.54 mm apart, footprints 1.49 mm across, against 4.5
and 1.5 mm in the paper). Each stitched two-channel image is stored as an
ImageSeries of shape (22323, 22323, 2) at 2 Hz, so it reads as 22323 frames of
22323 x 2 pixels, the unit is n.a. and the three 25% files share the
acquisition name Fig2_25. The file sub-Fig1F holds the same image in both
channels. The series description gives 144 tiles of a well of a six-well
plate, where the paper gives 216 tiles of 35 mm glass-bottom dishes, and the
images show a 12 x 12 tile grid over a round glass bottom about 14.5 mm across.
Dish numbers run up to 18, so more dishes were exposed than deposited, and
nothing says which form Figure 2; all unipolar dishes are from 2021-07-29 and
all 75% and 100% dishes from 2021-08-24, and the 100% dishes show more uptake
than the unipolar ones (largest mean 761.0 against 571.1 a.u.), which does not
match Figure 2C. Five questions are put to the paper's authors: how the ROI
were placed along bb', which footprints and areas gave YP_0 and MB_0, how the
exponential fits of Figure 2B were made, whether the t-tests were paired and
what the p < 0.01 of Figure 2C compares, and whether the ROI fields came from
the model at nominal electrode positions or were adjusted per dish.

The author's points on the protocol: the Figure 2 dishes had the same 600 ns
exposure as Figure 4 but are other dishes, so Figures 4 and 5 stayed blocked
and their measures were shown in a section that decides no outcome; the clock
check assumes time series and does not apply to single images; the claims
file's readings multiply with the step 1.6 readings, and where they changed the
outcome the best-supported reading was adopted and marked assumed; the
protocol does not say whether a field recomputed from the paper's geometry is
outside data, and it was listed under `inputs`; and the advice to develop on a
subset does not cover a CPU-bound load, so reduced data were cached during
development only.
