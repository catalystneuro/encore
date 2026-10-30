# 000402, MICrONS et al. 2025

Eight claims reproduced, three partially, none not reproduced and five blocked
on the dataset, and the three claims that pair the functional data with the
co-registration tables are blocked too; the 17 claims on the EM data held
elsewhere are counted apart (two reproduced, two partially, 13 blocked). It
pins version 0.230307.2132, which the paper cites and which is the only
published version. The paper, by the MICrONS Consortium in Nature, records one
mouse with a two-photon random access mesoscope in 14 of 19 completed scans
over 6 days, showing natural videos and the parametric Monet2 and Trippy
stimuli with treadmill and eye tracking, then images the tissue by serial
section EM, reconstructs it, co-registers the imaged cells to the EM somata
and describes the resulting connectivity. The claims were written from the
version of record in Europe PMC (PMC11981939) and from the paper's code
(AllenInstitute/MicronsFunctionalConnectomics at commit be24e51); the cells of
Extended Data Table 1 are not in that text and were read from the table's
image in PubMed Central. The scan, mask, stimulus, oracle, Monet2 and
behaviour claims were tested, the oracle reliability and direction tuning on
fluorescence as the deconvolved traces are missing, and so were the nucleus,
cell class, synapse and EM section counts from the public BossDB tables and
imagery. `unique-neurons-75909`, `z-drift-under-10um` and `structural-stack`
are blocked as `data_missing`, as the structural stack is not in the dataset,
`photodiode-89pct` as `data_missing` and `area-split-half-visp` as
`metadata_insufficient`; the three `with_inputs` claims and 13 elsewhere
claims are blocked as `other`, as the CAVE tables they test, or that choose
their neurons, need an account token. The partial outcomes are
`stimulus-conserved-across-scans` (Trippy seed 6831 is shown in both scans 6-4
and 7-5), `spontaneous-periods` (the longest period before the stimulus over
the 14 scans is 4.841 min, outside 5.5 +- 0.55 min, while all four bounds are
within tolerance over the 19 files), `behaviour-recorded` (the eye tracking of
scan 4-7 ends 968 s before the last imaging frame), `em-sections` (the imagery
holds data from section 7,931 to 27,882, 19,952 sections against 19,974 with
tolerance 0, while the share of subvolume 35, 34.47% to 34.67%, passes) and
`synapse-detection` (337,312,429 and 186,268,895 synapses, both within
tolerance, with precision, recall and F1 untested as no manual annotations
were found). `cell-classification` passes on the tolerance only, as the
released SVM table calls 89,056 neurons where the paper's 82,247 equals 69,957
plus 12,290, and `fig3f-oracle-reliability` and `fig3g-direction-tuning` have
criteria that test little: the 10,041 artifact masks score as high as the
somatic masks (0.235, 0.402 and 0.650 at the three percentiles) and pass the
split-half tuning test as often (65.9% against 62.9%). The author's run went
from 01:37 to about 04:12 UTC; a notebook counting the 20 GB synapse export,
which had counted it in 10 minutes while preparing, stalled in the entry's run
at the 60 minute cell limit and was removed, and `synapse-detection` and
`em-sections` were blocked as `too_large`. The author asked no questions, so
the answer run and the following author run changed nothing. Round 1, which
did not have the attempt record and could not check the blocked elsewhere
claims, agreed with 34 of 36 outcomes: the author took its partially
reproduced for `spontaneous-periods` and kept `monet2-directions` reproduced
after replacing the phase correlation measure of the directions, under which 4
of 560 trials had 15 directions, with global optical flow, under which all 560
have 16. Its points also led to the artifact-mask scores, a reference for the
tuning count, a variant of `ed4-matched-higher-signal-correlation` on the
dataset's own EM matches (71.9% of 538 pairs above both controls) and a
question to a reader on whether the stack claims should be data elsewhere.
Round 2 agreed with all but `em-sections` and `synapse-detection`, found that
`too_large` was not supported, and found statements on the artifact masks and
the 80 units shown in fig3g that the outputs did not support, which were
corrected; the author then wrote a second notebook, em_volume_counts.ipynb,
which resumes a broken stream, and proposed partially reproduced for both, a
change a third round reviewed and agreed with, adding two questions for a
reader on how the claims file reads the paper's section range and partner
accuracy. The analysis notebook ran in 644 s at first and in 594 s in the last
run, with em_volume_counts.ipynb in 708 s.

The dataset holds fluorescence traces only: the deconvolved traces the paper's
analyses use, and which the paper says can be read from the NWB files, are not
in it, nor are the oracle scores. It holds all 19 completed scans, while the
paper describes 14, and nothing in the files or the metadata marks which 14
(the other five are 4-9, 4-10, 5-3, 8-7 and 8-9), so its counts (125,413
masks, 115,372 somatic) can be matched only after reading the table's image.
The structural stack, the registration of each field into it and the stack
coordinates of the masks are not in the dataset, so masks imaged in more than
one scan cannot be grouped and the z drift cannot be measured; BossDB serves a
structural stack of this mouse, which the claims file's limit to the dandiset
left unused. No mask or field has a visual area, as every imaging plane's
location is the same list of four areas. The EM columns are in only one of the
two fields at each depth (52 of the 104 fields of the 14 scans, 8,863 ROIs
with a root id) and in no field of files 4-9, 4-10, 8-7 and 8-9, and
pt_root_id and pt_supervoxel_id are stored as 64-bit floats, which hold
integers exactly only up to 2**53; of 538 pairs of masks in different scans
that share a root id, 50 have EM cell body points more than 10 um apart. The
Monet2 table gives num_directions but not the direction or onset of each
period, which were measured from the stimulus video. The imaging_rate of every
imaging plane is NaN, the subject age is the range P75D/P81D in every file
though each scan was recorded on one day, and all fields of a scan share one
array of frame time stamps though they are imaged one after another. The eye
tracking ends 54 to 76 minutes early in files 4-10, 5-3 and 8-7 and 3.9 and
6.2 s early in 4-9 and 8-9, and several files have missing time stamps in the
treadmill and eye series (up to 190). The EM imagery of subvolume 65 on BossDB
holds data up to section 27,882, while the paper gives the processed region as
sections 7,931 to 27,904, and 27,904 is the metadata's exclusive end of
subvolume 65. No questions are put to the paper's authors.

The author's points on the protocol: no category fits public data behind a
free login such as CAVE, and `other` was used; outside inputs must be pinned
by a DOI or a commit, which the BossDB objects lack, so their URL, ETag and
modification date were recorded; using the 2021 BossDB releases of the CAVE
tables the claims file names was recorded as a deviation; the protocol says to
read the PDF only for a garbled table, and with no PDF the table image was
fetched from PubMed Central; nothing covers an external stream that runs in
preparation but stalls in the entry's run; nothing covers deriving missing
metadata from raw data, such as directions from the stimulus video; and there
is no rule for an outcome when some expected values cannot be measured.
