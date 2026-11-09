# 001785, Fujimoto et al. 2026

Seven claims reproduced, none partially, one not reproduced and two blocked,
one as methods underspecified and one as other; the claims that also use
outside inputs are counted apart, 14 reproduced and six blocked for missing
data. No outcome rests on an assumption. Of the 35 claims, three are link
checks added by the author, `link-fc-voxels` and `link-fa-voxels` reproduced
and `link-if-counts` partially reproduced, and two have their data elsewhere,
the behaviour bins in DANDI:001773, and are counted apart:
`ed1-behavior-increase` reproduced and `ed1-sham-no-behavior-change` not
reproduced. The first verification round agreed with 34 of the 35 outcomes as
they stood, not with `fig6c-sham-cc1-no-change`, and the second with all 35,
and nothing was proposed after the second, so there was no third round. It
pins version 0.260615.1835, the latest published version, with the same files
as 0.260522.2215 and 13 more EM images than the April versions; the paper cites
no version of this dandiset, and its Data availability statement names only
DANDI:001773. The paper, Fujimoto, Fujimoto, Elorette et al., "Deep brain
stimulation induces white matter remodeling and functional changes to
brain-wide networks" in Nature Neuroscience, is the paper of DANDI:001773,
which holds its MATLAB scripts and source-data sheets; this dandiset holds the
FA and T1w maps of monkeys N and T, stimulated, and D, implanted and never
stimulated, one seed connectivity map per animal and session for them and the
nonsurgical controls B, W and H, and the CC1 immunofluorescence and EM images.
The claims were written from the version of record in Europe PMC (PMC13337501)
and the Supplementary Information, without a PDF of the article, and from the
scripts in DANDI:001773, after an earlier reader run had stopped because the
supplement was missing; the check made nine changes, one of them a new claim,
and left two points open. The seed maps equal the paper's normalized seed maps
at all 5087 listed voxels once the AFNI coordinates are read as RAI, and 6332
of 6332 FA values of the paper's sheets are found in the FA maps, so with the
tracts, CB subregions and target ROIs taken from the paper's source data the FA
and seed claims re-run the paper's statistics on its own data. All of them are
reproduced, with the interaction F values the paper reports (F(1,3187) = 4.64
for `fig2a-cb-fa-increase`, 186.48 for `fig5b-scc-decreases`, 51.09 for
`fig5c-network-decreases`, 4.58 for `fig6d-sham-scc-little-change` and 7.36 for
`fig6e-sham-no-network-reduction`), and `fig6a-sham-cb-fa-decrease` gives
F(2,1238) = 6.02, which bears out the claims file's reading of the printed F
1,1238 as a misprint. The cells were counted here from the images, with one
automatic threshold per section and channel (IsoData or Otsu) and a smallest
object of 10 or 50 pixels, which the paper does not give; the counts match the
paper's in three of the four regions, under different size filters, and under
no single reading in all four. `fig3c-cc1-dapi-ratio-mcc` (side F(1,108) = 9.5
to 14.4, where the paper's counts give 9.00), `ed5-cc1-count-dapi` and
`ed6b-uf-fm-no-change` (smallest p = 0.0685, on counts that fail the link in
that region) are reproduced under all four readings. `ed6a-dacc-cb-no-change`
is not reproduced: the dACC-CB ratio is lower on the stimulated side by 3.4 to
4.0 points (p = 0.0058 to 0.013), while the paper's own counts give p = 0.090,
so the difference may come from the method of counting, not the tissue.
`fig6c-sham-cc1-no-change` is blocked as methods underspecified, as the size
filter decides it (p = 0.31 at 10 pixels, 0.044 at 50).
`ed1-sham-no-behavior-change` is not reproduced because monkey D's foraging
falls from 0.18 to 0.05 (F(1,118) = 5.32, p = 0.023) by the test the claims
file applies; the paper reports no test for D. `fig3f-gratio-decrease` is
blocked as other, as the g-ratio rests on hand measurements of axons the raters
chose; the four Fig. 4 connectome claims and `ed10c-sham-subcortical-decrease`
are blocked for missing data, as no EPI time series is deposited, and so is
`fig5a-control-group-no-reduction`, as its reading (a) needs per-run maps,
while reading (b), run without the cluster-level correction, finds no negative
cluster above 20 voxels (at most 3). The author's first run gave the same
outcomes except that `fig6c-sham-cc1-no-change` was reproduced, it and
`ed6b-uf-fm-no-change` on the assumption of a smallest object of 10 pixels, and
`fig3f-gratio-decrease` was blocked as not runnable. The author asked no
questions of a reader, so the answer and author-answers runs changed nothing.
Round 1 disagreed on `fig6c-sham-cc1-no-change`, which it gave blocked, and
found that the main test of `ed6b-uf-fm-no-change` included a sixth field,
N122 RW6, with no row in the paper's sheet, with which the ratio under Otsu
with 50 pixels reaches p = 0.04997, that the counting only approximates the
paper's FIJI counts, that the record said two of four regions where three pass
the link, that the nearest-value matching undercounted ambiguous FA values,
that reading (b) of the control-group claim could be run, and that the
lead-site increase of `fig6d-sham-scc-little-change` was not reported; in
reply fig6c was blocked, ed6b was tested on the paper's 40 fields per
hemisphere and no longer rests on an assumption, fig3f's reason became other,
and scatter plots, a channel check, the match paths, reading (b) and the
unthresholded change of monkey D's map were added. Round 2 agreed with all 35,
found the support of `ed6b-uf-fm-no-change` weak and the counting still bearing
on it and on `ed6a-dacc-cb-no-change`, and found sentences the outputs did not
support (a Tukey-Kramer p "below the floor" that could not be computed, "in
none under one reading", the README's three of four regions read as one
procedure, the ed6a percentages without their reading, repeats across tracts
never examined and an interpretation of the lead-site increase); in reply the
text was corrected, the check of voxels shared across tracts was added and the
counting was left as it was. Nothing was filed in `questions/001785.yaml`. The
author's run took about 40 minutes (18:07 to 18:47 UTC) and nothing failed; an
automatic EM segmentation, tried outside the notebook, found few of the paper's
axons and was dropped. The notebook ran in 351 s at first, 222 s after the
author-answers run, 293 s after round 1 and 213 s at the end.
`tools/build_site.py` and `tools/site_assets/app.css`, modified before the run,
and an untracked `scripts/` folder were left alone.

No EPI data are deposited, although the archive's description lists
"Functional MRI (EPI; FC) data": the files in MRI/FC are single volumes, the
paper's normalized seed maps on a 1.5 mm grid in NMT space, one per animal and
session, so the whole-brain connectivity findings (Fig. 4, Extended Data Fig.
10c) and the voxel-wise test of the control group cannot be tested. Nothing in
the dandiset says what the MRI files hold, which was found only by matching the
values to the paper's source data in DANDI:001773; the files in MRI/FA are FA
maps, each in its own session's space, the normalizing maximum is not in the
seed maps (their maxima are 0.55 to 1.38), and the seed of the control animals
is not stated in the files. No tract, CB subregion or target ROI masks are
deposited, so which voxels the paper analysed can be recovered only from those
source data, by position for the seed maps and by matching FA values for the FA
maps, where 641 values have more than one candidate voxel. The dandiset holds
the immunofluorescence and EM images but not the cell counts or the per-axon
measurements behind them, and the paper's per-axon sheet gives no axon
position, so the measured axons cannot be found in the images. The
immunofluorescence TIFFs carry no pixel size (the resolution tag is the default
72 per inch) and no channel names, red holding CC1 and blue DAPI being inferred
from the paper's labels, and the sections differ in bit depth (8-bit for N603,
N613, N623; 16-bit elsewhere). dataset_description.json is not valid JSON, as
the second author name is in typographic quotes and a comma is missing after
the Description value, and the archive's metadata gives no species or
approach. EM/TR-1-8r.tif is a byte-identical copy of EM/TR-1-8.tif;
IF/IF_CC1_UF_FM_overlap_mkNT holds six fields for section N122, right
hemisphere, where the design has five per section, and two other file names
carry a suffix (N112 LW1B, N453-RW-6r) the paper's sheets do not explain. All
six FA maps reach 1.21 to 1.22, above the bound of 1 that FA has by definition,
in voxels outside the paper's tract lists. The paper's per-voxel FA lists
repeat voxels: within one tract, side and session the same value is listed
twice (99 times in the whole-tract list of N and T, 44 in its subregion list,
40 and 18 in the lists of D), so the voxel n of the FA tests counts some voxels
twice, and other voxels are listed in two or more tracts of one session (233 in
the whole-tract list of N and T; 71, 1 and 18 in the other lists). Of the paper
itself, the Extended Data Fig. 6b legend gives the UF-FM DAPI side effect as P
= 0.9611, where the paper's own counts give F(1,76) = 0.0038, p = 0.9511, which
its stated partial eta squared fits; Supplementary Tables 3, 4 and 11 hold
identical values; and Extended Data Fig. 10d calls monkey D's post scan "10
weeks after implantation", where the Methods give 6 weeks without stimulation
after the 4-week recovery. A question is put to the paper's authors: how cells
were counted in FIJI, with which threshold method, background subtraction,
size filter and watershed split.

The author's points on the protocol: it does not say whether an author may
change a claim's `data` field when the labels come from outside the dataset,
and it was changed on four FA claims, each recorded as a deviation; it gives no
rule for when a link claim's criterion is written relative to the analysis, and
the link-if-counts criterion was written after the counts were first computed,
as it says; the clock check has no counterpart for static images and maps, so
it was skipped; it does not settle which outside data count as measurements,
and the group-average matrices and per-axon measurements of DANDI:001773 were
treated as the paper's outputs, though the `elsewhere` rule could be read the
other way; and it has no block reason for a method done by hand, such as
manual g-ratio measurement, so `not_runnable` was used, which round 1 later had
changed to `other`.
