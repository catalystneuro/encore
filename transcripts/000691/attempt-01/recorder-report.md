I ran `python tools/readme_row.py 000691 --write`, which added the README row (6 reproduced, 0 partially, 0 not reproduced, 7 blocked), and I added the subsection below at the end of `docs/pilot-notes.md`. Nothing is committed. The repository root has untracked files I did not create (`.bashrc`, `.idea`, `scripts` and others), and I left them alone.

The table counts only claims that rest on the dandiset. The attempt's two partially reproduced claims use dye images from the paper's code repository, so the README row leaves them out. The first paragraph gives them separately, following the wording of an earlier subsection.

### 000691, Scherrer et al. 2023

Six claims reproduced and seven blocked on the dandiset, plus two claims on
data in other archives, both partially reproduced. Round 1 gave its own
outcome for each claim from the notebook with its conclusions removed and
agreed with all 15 as they then stood, but suspected that the SGD solver
explained why no point of the local decoding map was significant (0 of 151);
the 32-footprint decoders stop at objectives of 19.8 to 68.9 where the
optimum is 1.976 to 2.000, so the author fit them with liblinear, as
MATLAB's default for 100 or fewer predictors is BFGS run to convergence, and
`ed9c-local-decoding-map` moved from not reproduced to reproduced. Round 2
agreed with all 15 and nothing was proposed, so there was no third round.
The paper reports two head-mounted microscopes with axicon correction
optics, one optimized for weight (1.0 g, 1.0 mm FOV) and one for field of
view (1.4 g, about 4 mm), that image hundreds of neurons in juvenile
songbirds and thousands in a freely behaving mouse, whose position and
direction in a looped maze can be decoded from the imaged activity. The
footprint count and the mouse's coverage of the maze, decoding of quadrant
with direction and of octant, the local decoding map, localized activity
and the spread of coactive footprints in 8 NMF components were tested on the
one deposited mouse, with position tracked from the behaviour video, and the
flat illumination of both microscopes on dye images in the paper's code
repository. The 2382 curated footprints and the field of view are blocked as
`metadata_insufficient`, and the other mice, the songbirds, the weights, the
resolution targets and the analog-to-digital converter as `data_missing`.
Some outcomes rest on weak ground: `ed9c-local-decoding-map` gives 1
significant point with SGD and 18 of 150 with liblinear, the solver was
changed after round 1, liblinear reached its limit of 10,000 iterations in
2268 of 3000 fits, and the smallest significant z, 2.53, is below the 3.40 a
point needs alone; in `ed8-coactive-distributed` random sets of footprints of
the same size have spread ratios of 0.951 to 1.042, so any set this large
passes the criterion's half; `ed2c-kiloscope-flat-illumination` misses the
0.8 level the author chose by 0.003 and is above it for one of four 100 um
moves of the centre; and every analysis uses all 2948 footprints in place
of the 2382 curated ones. The version of record is not open access, so the
author used its abstract, figure titles, Extended Data legends and data and
code statements, read the bioRxiv preprint (version 2) for its Methods only,
and took the parameters of every analysis from the paper's code at commit
d596646; the legend of Figure 2 and the main text's numbers were not tested.

The dandiset was converted by CatalystNeuro (Szonja Weigl of CatalystNeuro
is a contributor). It holds one of the paper's four mice and none of the
songbird recordings or optical test data, and the Academic Torrents deposit
the paper names for its imaging data holds files of the same mouse session
only, so the other mice and the birds are not public. The 2948 footprints
are the EXTRACT output before curation, and nothing in the dandiset marks
the 2382 the paper kept or says that the footprints are uncurated; the
curation is in the Academic Torrents deposit, where no peer connected in two
attempts of 2.5 and 4 minutes. The mouse's position, which the decoding and
place analyses use, is not in the dandiset and must be tracked from the
behaviour video, and the first 64 s of the video (by its nominal rate), which
the paper's code drops because the experimenter is in view, are not marked.
The device description reads "Head-mounted microscope (Kiloscope) optimized
for weight (1.0 mm FOV; 1.0 g)" and the dandiset description also names the
microscope optimized for weight, while the data are from the large-FOV
microscope (a 4 mm window, 2948 footprints and 808 x 608 pixel frames). The
imaging is stored as a TwoPhotonSeries and listed as two-photon microscopy,
though the microscope is a one-photon epifluorescence microscope. Other
findings: the behaviour video is described as about 30 fps and its AVI
header says 30 frames/s, but its 15521 timestamps run at a median 12.5
frames/s over 1234 s, and at 30 frames/s it would cover only 517 s of the
1234 s of imaging; the imaging plane gives no pixel size, and its indicator
and location are "unknown" with no excitation wavelength, although
general/virus says GCaMP7f; the Extended Data Fig. 9c legend describes
decoders on the 32 closest footprints within 270 um, where the code uses 64
within 50 pixels, which at the code's own 5.94 um per pixel is 297 um; and
the title of Extended Data Fig. 8 refers to the Kiloscope data "shown in
Figure 3", while the version of record has two figures. The masks, the movie
and the traces line up, and position decoding peaks within about a second
of zero shift, so the clocks are reported as consistent, though offsets of
1 to 2 s could not be told apart.

The notebook ran in 18 minutes in the first clean run and in 25.2 minutes
after round 2. Streaming the behaviour video with PyAV over HTTPS and
through remfile failed, so the notebook reads the 105 MB file into memory;
liblinear's coordinate order was seeded after round 1, as unseeded the
exact map's count of significant points changed between runs; and the code's
64-footprint variant of the local map stays on a 60 pixel grid where the
criterion says 40, since on 40 the notebook took 32 minutes, over the
30-minute limit. Round 2 found numbers in the text that the executed
notebook contradicted (19 significant points against 18, 2264 fits at the
limit against 2268); the copy it read came from another machine, three runs
on four cores gave the stated numbers, and the text now says the counts can
differ slightly between machines. The author's points on the protocol: a
paper that is not open access whose legends and preprint are public; outside
data on a torrent with no peers, which the blocking categories do not fit;
whether data derived from the dandiset's own video, such as position, count
as dandiset data; an image-reading check that forbids reading measurement
images that are data; hardware claims with no data anywhere; a clock check
that cannot resolve offsets of 1 to 2 s; an outcome 0.003 from a threshold
the author chose, as the legend gives no number for flat; and a prototype
decoder run before the criteria were written.
