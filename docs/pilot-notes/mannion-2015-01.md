# crcns-vim-3, Mannion et al. 2015

One claim reproduced, none partially, none not reproduced and eight blocked,
all eight for missing data; the seven claims that also need outside data,
counted apart, are blocked too, six for missing data and
`no-radial-bias-in-patches` for insufficient metadata. The first verification
round agreed with 15 of the 16 outcomes as they stood and disagreed on the
reason for blocking `no-radial-bias-in-patches`, and the second agreed with all
16; nothing was proposed after the second, so there was no third round. CRCNS
does not version data sets, so the version is recorded as unversioned with the
data set's DOI (10.6080/K0JS9NC2). The paper, Mannion in PeerJ (3:e1038),
measures fMRI responses in V1, V2 and V3 of seven participants to natural image
patches taken from above or below fixation and shown in the upper or lower
visual field, and reports an interaction between presentation and source
location (F(1,6) = 11.19, p = 0.016) that does not depend on the area, larger
lower-field responses to patches from below than from above (0.80 against 0.72
psc) and no difference in the upper field, that the most upper-preferred patch
pairs are mostly from above and the most lower-preferred mostly from below
(Figure 4), that the upper minus lower response difference rises with mean
luminance and with the output of some luminance Gabor filters (Figure 5), that
the patches show no radial bias, and that task performance (Figure S2) and GLM
residuals (Figure S3) do not differ across conditions; the data set holds the
raw functional runs of a 35-slice occipital slab, the event sequences, the task
records and 120 stimulus screenshots. The claims were written from the version
of record (PMC4485252) as text from the Europe PMC XML, without a PDF and
without the supplementary files, and from the paper's analysis code at commit
571e931 on GitHub, as its Bitbucket link is dead; the claims check made four
corrections, among them marking the "largely confined" rule for the localiser
masks as an assumption and naming the two possible filter scales (about 78.7
and 78.2 pixels per degree), for 16 claims. Only `figs2-task-no-condition-difference`
could be tested, and it reproduced: in the window 0.4 to 0.9 s no effect
reaches p < 0.05 under the code as written (smallest p 0.158) or with
assignment by absolute run time (smallest p 0.347), nor under three variants
(p >= 0.053), though under the code as written the window 0.6 to 0.9 s gives a
presentation effect (p = 0.034). Every other claim needs responses in V1 to V3,
or the monitor calibration, or both. A volume variant on all localiser voxels,
which decides nothing, gives lower-field responses of 0.997 psc for patches
from below and 0.870 from above (p = 0.034) and an interaction of p = 0.137.
The author asked no questions of a reader, so the answer and author-answers
runs changed nothing. Round 1 agreed with every outcome but held that
`no-radial-bias-in-patches` needs only the screenshots and a calibration and
should be blocked for insufficient metadata, with a luminance variant run under
a stated calibration, and raised targets dropped on event onsets, assignment to
the event in progress and the unprinted lines of `task.py`; in reply the
reason was changed, the radial-bias test was run as `imstats.py` runs it under
sRGB and Adobe RGB primaries (none of the 12 tests below p = 0.05, smallest p
0.063), variants (d) and (e) were added and the `task.py` lines printed. The
notebook that round 1 reviewed still held a table of outcomes in its
introduction, which the verifier saw and quoted. Round 2 agreed with all 16 and
found sentences the outputs did not support, among them a filter match of
1.3e-15 where 8.9e-16 is printed and labels called close to random without an
output to show it; in reply the text was corrected and the peak lag printed for
every reading, which showed a 0.7 s peak for lower/above under two readings.
No outcome changed in either round. The notebook ran in 158 to 243 s at first
and 386 s after the author-answers run. In one development run S3 reset the
connection, so the reader now reconnects, and most of the helper module was
deleted by accident during editing and restored from an earlier draft.

The data set holds the raw functional runs, event sequences, task records and
stimulus screenshots, but not the anatomical images, cortical surfaces,
retinotopic mapping or V1, V2 and V3 definitions that every response measure of
the paper uses; its descriptor says so and asks users to request them on the
CRCNS forum, and 14 of the 16 claims are blocked for this reason. The monitor's
measured CIE coordinates, needed to put the screenshots in the DKL space of
Figure 5 and the radial-bias test, are in neither the data set, the paper nor
its code, and the patches are in colour (R, G and B differ in most pixels of
118 of the 120 patches). The data set's README.txt says it contains fMRI
measurements in areas V1, V2 and V3, but the files are whole volumes of the
occipital slab with no area labels. The NIfTI files are named by scanner
series number and the sequence and task files by run, with no mapping given;
the paper's code takes the series in order as runs 1 to 10, which a
leave-one-run-out fit supports for six participants and could not confirm for
p1011. For p1011 the timing of the event sequences and the run order could not
be confirmed without motion correction (held-out runs at mean t 0.7 and 1.1
against 2.6 to 4.9 in the others, a coarse motion index of 3.6 mm by run 10
against at most 1.8 mm), and its upper-field voxels lie above its lower-field
ones, the reverse of the other six. For p1004 runs 1 to 5 the target column of
the task lookup does not describe the task performed, which the paper's code
redefines, and the descriptor does not say so or describe the four button keys.
The Figure S2 legend describes performance near each condition, while `task.py`
labels each target by the event starting about 32 s after it; with assignment
by absolute time the conclusion of no difference is unchanged. No question is
put to the paper's authors.

The author's points on the protocol: `docs/archives.md` assumes CRCNS data come
as zips, while this one is a tar.gz with no index, so it was streamed once with
an md5 check and reconnection; the derivation check rejects `Image.open(`,
which blocks reading stimulus images that are part of the data, so they were
decoded with `pypng`; it is unclear whether a `depends_on` that is only
methodological should block a claim, and both reasons were recorded for the
radial-bias claim; the protocol does not say whether a substitute analysis may
be shown for claims blocked for missing data, so the volume version went in a
separate section labelled as deciding nothing; and it is unclear whether the
"several readings" rule or the "absence is judged on the paper's test alone"
rule applies to a claim of absence with no test in the paper, which did not
matter here as every reading gave the same outcome.
