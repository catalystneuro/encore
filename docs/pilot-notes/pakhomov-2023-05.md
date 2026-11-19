# pakhomov-2023, Pakhomov et al. 2023, fifth attempt

One claim reproduced, six partially, five not reproduced and 12 blocked, six
for missing data and six as `methods_underspecified`; one outcome,
`fig6a-more-packets-more-uptake`, rests on an assumption. The first
verification round agreed with 21 of the 24 outcomes as they stood and the
second with 23; the author then proposed blocking `fig6-peak-narrower` and
`fig7cd-holds-for-large-array`, and a third round reviewed those two claims and
agreed. It is the first attempt on the paper under pilot-14, which files
records by paper: the earlier attempt, `pakhomov-2023-04` under pilot-13, tested
001027 alone with its own claims file, and the new claims file of 24 claims
replaces four written one per dataset under pilot-10. This one uses all five
dandisets, pinned at 0.240515.1909 (000686), 0.240515.1925 (000875),
0.240605.1826 (001025), 0.240605.1859 (001027) and 0.240605.1954 (001028).
The paper, Pakhomov, Gudvangen, Mangalanathan, Kondratiev, Redondo and Semenov,
"Next generation CANCAN focusing for remote stimulation by nanosecond electric
pulses" (Bioelectrochemistry 152, 108437), measures electroporation as
YO-PRO-1 (YP) uptake in CHO-K1 cells; it reports that bipolar signals cancel
uptake in single cells (Fig. 4), that packets of 600-ns unipolar pulses from
the four needles of a quadrupole array target uptake to the array's centre in
monolayers, more so with rotation, more packets, Packet 2 and electrodes lifted
above the cells, independently of pulse amplitude and array size (Figs. 5 to
9), and it gives field simulations (Fig. 3). The claims were written from the
accepted author manuscript (PMC10247516), not the version of record, with no
figure read; the paper has no supplement and links no code or data, and the
claims check made five corrections to how claims are worded or tested.
Reproduced is the targeting boost with a 2 mm gap (541% at 2 mm, inside 540 to 660%). Partial are the packet-centre
enhancement of Fig. 5A, the rise with packet number, the peak against the
periphery (128, 70 and 64%), the trough against the centre (1.59, 1.99 and
3.70), the amplitude ratios (6.66, 5.71 and 7.33 against 15.5, 16.2 and 16.8)
and the larger fall near the electrodes than in the centre with electrode
height. Not reproduced are the trains against packets of Fig. 5A (0.75 times the packets at the e3 end, p = 0.40), the three
Fig. 8 claims (centres 692, 378 and 401 a.u. for Packets 1, 2 and 3, and Packet
3 with the highest normalized centre in every reading) and the restriction to
the centre with lifted electrodes. The Fig. 3 and Fig. 4 claims and
`fig8-cancellation-predicts-targeting` are blocked for missing data; the Fig.
5B void, the peak width, amplitude independence on the small and the large
array, and the claims depending on them are blocked because the readings with a
basis in the paper disagree on the ROI count, the end ROI or the diagonals. The
attempt ran every reading the claims file lists, up to 576 per claim. The
author's first run gave 7 reproduced, 7 partially, 4 not reproduced and 6
blocked. Round 1 found that the e3 end ROIs might lie off the monolayer, that
readings were adopted by a convention of the notebook, that unpaired tests
were used inside a dish, that the Fig. 7 group sizes differ from the legend,
and that the ANOVA variant counted ROIs as independent; in reply a check showed
every end ROI inside the image at 2.0 to 4.2 times the cell-free level in the
train dishes, comparisons inside a dish became paired, readings were adopted
only with a basis in the paper or the claims file, `fig5a-trains-stronger` moved
to not reproduced and `fig5b-rotation-center-peak` and
`fig7b-targeting-independent-of-amplitude` to blocked, and three questions were
put to a reader in `questions/pakhomov-2023.yaml`. Round 2 found that the
adopted readings fixed both diagonals for Figs. 6 to 9, where the claims file
says the paper is silent, asked that `fig6a-more-packets-more-uptake` be marked
assumed, and found sentences the outputs did not support, all corrected; with
the diagonals varied, the two proposals followed. The reconciliation with
`pakhomov-2023-04` was blind, and its two changes of outcome,
`fig6a-more-packets-more-uptake` and `fig9b-gap-boosts-targeting` from blocked,
come from the change of protocol and claims file, not the data. The author's
run took about 1 h 11 min (14:14 to 15:25 UTC); the notebook ran in 11.5 min at
first, with peak memory 7.0 GB, 16 min after round 1, 16.5 min after round 2
and 968 s after round 3. A read-only `sed` command was denied by the
permission system, and the first check failed because a blocked claim's output
was not a cell tag, which was fixed.

None of the five dandisets holds the single-cell time lapse of Fig. 4 or the
field simulations of Fig. 3, so six of the paper's claims cannot be tested;
the 70 files each hold one stitched monolayer image. The files give no pixel
size (ImageSeries resolution is -1 in 000686 and 000875 and 1 or 96 in the
other three, with no field of view), no electrode positions, no ROIs, no array
size and no position of electrode e1, so all were inferred from the images; an
assumed 0.65 um pixel gives a large-array diagonal of 8.25 mm between needle
edges (paper 8.4 mm), and for electrodes lifted 2 and 3 mm, which leave no
footprint, the square was completed from needle marks in the second channel.
In 001027 the dishes labelled Protocol3, which the session descriptions define
as 8 phases with 5-us delays (Packet 3), give the highest normalized centre of
the three packets in every reading, where the paper reports it for Packet 2.
The files record no exposure or gain, and the background inside the electrode
footprints of the three Packet 1 dishes, imaged on 24 March 2021, is 308.9
a.u., 1.94 times that of the other seven (161.1 and 150.0 a.u. on 17 and 18
March), so a.u. values may not be comparable between imaging days. 001025
holds 4 small-array dishes at 2.4 kV and 2 large-array dishes at 4.8 kV, where
the paper gives n = 3 for Fig. 7, without saying which dishes it used. Six
dishes are deposited twice with identical pixel data, in two dandisets each,
consistent with their use in two figures. 17 files of 001025 and 001028 hold a
second frame (described as Channels FITC, DAPI) that no description explains.
The subject species of 000686 and 000875 is Bos taurus for CHO cells; the
assets summary of 001027 names "Cricetulus griseus - Cricetulus aureus", each
subject is a dish with age P1D, and the description of dish 10 gives an
unknown microscope, detector and objective, with its session on 18 March 2021
at 18:50 where the other Packet 2 and 3 dishes start on 17 March. In the
paper, "~120 a.u. for packet 1" contradicts its own sentence and was read as
Packet 2, the paper's own Fig. 4 means give 6.1-fold for the 4-phasic signal
against its stated 4 to 5-fold, and array size is confounded with packet
number in Fig. 7. Questions are put to the paper's authors: how the ROIs were
laid out and along which diagonals, how the most peripheral value and the
centre were found, whether a background was subtracted and whether the a.u. of
the text are raw pixel values, whether tests inside a dish were paired, which
needle is e1, and whether values were read from ROI means or LOESS fits.

The author's points on the protocol: expected values may match under one
combination of readings, which here number up to 576, and the main reading and
the share of matching readings were reported; adopting "the reading the paper
best supports" is unclear with eight independent reading dimensions; the
partial outcome of `fig6a-more-packets-more-uptake` does not cover a rise at
all three places with the peak test failing, read as partial; streaming
through remfile was too slow for 0.4 to 1 GB images, so files were read into
memory by HTTP range requests; "count each recording once" does not fit a dish
reused across figures, and each was used in its own figure; the protocol does
not say a blocked claim's `output` must be a cell tag; the clock check does not
apply to still images; and `measured` takes one value per group where an
expected value covers several groups, with the order stated in the notes.
