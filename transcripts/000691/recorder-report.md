I ran `python tools/readme_row.py 000691 --write`. It replaced the 000691 row in README.md, which had been marked deprecated, with 2 reproduced, 0 partially, 1 not reproduced and 15 blocked. I then added the subsection below to the end of docs/pilot-notes.md. Nothing is committed.

The README counts cover 18 of the 23 claims. The other five use bead and dye images from the paper's code repository, and the tool leaves claims on outside data out of the counts. The first sentence gives their outcomes separately.

The `catalystneuro` field names a contributor, not a repository, so I followed the 000582 subsection's wording for that opening sentence. The earlier first attempt already has a subsection headed "### 000691, Scherrer et al. 2023", so this one is headed "second attempt".

### 000691, Scherrer et al. 2023, second attempt

Two claims reproduced, none partially, one not reproduced and fifteen blocked
on the dandiset; of five more claims on the bead and dye images in the paper's
code repository, three are reproduced, one partially and one blocked. The
attempt replaces the deprecated 000691-scherrer-2023-01, whose claims were
written from the abstract and public figure legends only; the claims file was
written again from the full text and the paper's code, so it has 23 claims,
nine of them new or restored, and several criteria that rested on the earlier
author's thresholds now use the paper's numbers. It pins the same version,
0.260827.1358, the only published version, whose draft holds the same files,
so every difference from `-01` comes from the claims file. The author put no
questions to a reader, and the answer run found no questions file, so nothing
changed. Round 1 gave its own outcome for 22 of the 23 claims from the
notebooks with their conclusion cells and summaries removed (none for
`ed3-adc`) and agreed with 20 of them; it gave reproduced for
`fig2-quadrant-direction-decoding` and `ed9b-octant-decoding`, on the null of
one fit per shuffled decoder (n1) alone, and called `ed7-motion-small`
tentative because nothing checked that the movie is raw. The author kept both
decoding claims blocked as `not_runnable`, and round 2 agreed with all 23
outcomes; nothing was proposed, so there was no third round. The paper, "An
optical design enabling lightweight and large field-of-view head-mounted
microscopes", describes two head-mounted microscopes, the Kiloscope (about 4
mm field of view, 1.4 g) and the Featherscope (1.0 mm, 1.0 g), used in four
mice and three juvenile zebra finches, and reports thousands of neurons
recorded at once in a freely moving mouse, from whose activity linear decoders
read the mouse's combined quadrant and movement direction at least three times
above chance. The footprint count, the field of view, the bead PSFs, field
curvature, the flat illumination of both microscopes and the motion of the
movie were tested, and the decoding claims were run under the (n1) null.
`ed7-motion-small` is not reproduced (0.037 px RMS against 0.13), and
`fig1f-kiloscope-psf` is partially reproduced because no reading puts both
values within tolerance. The decoding claims hold under (n1) (median accuracy
0.437 and 0.326 against the largest of 1000 shuffled decoders at 0.227 and
0.229), but the criterion also needs (n2), 200 fits per shuffled decoder,
which is 200,000 fits, measured for the quadrant claim at 33.3 hours in this
run (24.6 hours in the run of round 2) against 30 minutes per notebook, so
fig2 and ed9b are blocked as `not_runnable`, and `fig2k-decoder-size`,
`fig2l-local-decoding-map` and `ed9c-local-decoding-map` also, as they depend
on them and need 4.4 to 12.8 hours each on four cores. The other mice, the
songbirds, the weights, the USAF target images and the ADC recordings are not
deposited, `ed6a-curated-footprints` is blocked as `metadata_insufficient`,
and `fig2d-lman-sparse-bursting`, `ed8-coactive-distributed` and
`ed10-localized-activity` as `methods_underspecified`, ed8 because all four
quarters are covered in 8 of 8 events under one reading of the event times and
7 of 8 under the other. Compared with `-01`, abstract-kiloscope-fov moved from
blocked to reproduced, the two flat-illumination claims from partially
reproduced to reproduced, and ed8, ed9b, ed9c and ed10 from reproduced to
blocked. Some outcomes rest on weak ground: in abstract-kiloscope-fov both
pixel sizes come from the paper's code, the reading at 5.35 um per pixel only
just within tolerance (4.323 against a lower bound of 4.32) and the test close
to circular at 5.94 um per pixel; and the Kiloscope PSF fits depend on the
optimizer and differ between runs on different machines (4.467 um at the
centre under reading (a) in this run, 4.422 um in the run of round 2).

The dataset was converted by CatalystNeuro (Szonja Weigl of CatalystNeuro is a
contributor). The files are unchanged, so the nine findings of `-01` were
checked again, and all are still present. The dandiset holds one of the
paper's four mice and none of the songbird recordings, and the USAF target
images and ADC recordings are not public. The mouse's position, which the
paper's decoding and place analyses use, is not in the dandiset (its only
processing module is ophys), and the opening of the behaviour video that the
paper's code skips is not marked. The 2948 footprints are the EXTRACT output
before curation; the paper analyses the 2,382 it kept, and nothing marks them
or says the footprints are uncurated. The device description reads
"Head-mounted microscope (Kiloscope) optimized for weight (1.0 mm FOV; 1.0
g)", and the dandiset description also names the microscope optimized for
weight, where the data are from the large-FOV Kiloscope (4 mm window, 2948
footprints, 808 x 608 pixel frames). The imaging is stored as a
TwoPhotonSeries and two-photon microscopy is listed among the techniques,
though the microscope is a one-photon head-mounted epifluorescence microscope.
Nothing says whether the movie is the raw video or the motion-corrected one
the paper extracted footprints from; its values are consistent with the raw
video, and its rigid shifts against a template have an RMS of 0.037 pixels,
about a quarter of the 0.13 pixels the paper reports. Other findings: the
behaviour video is described as about 30 fps and its AVI header says 30
frames/s, but its 15521 timestamps run at a median 12.5 frames/s over 1234 s;
the imaging plane gives no pixel size, its indicator and location are
"unknown" and its excitation wavelength is NaN, although general/virus says
GCaMP7f; ROICentroids equal the mask's peak pixel for 84% of footprints and
the rounded weighted centroid for only 43%; both local decoding map scripts
use 64 footprints within 50 pixels where the paper describes the 32 closest
within 270 um; the Extended Data Fig. 8 legend refers to a Figure 3 and a
ridgeline plot in Fig. 2d, where the paper has two figures and the ridgeline
plot is Fig. 2h; the paper's tracking code unwraps position with MATLAB's
unwrap, which gains an error of up to pi cm at every lap of the 147.1 cm loop
and changes about 1% of the running and direction labels; and the paper's bead
scripts order the images by file date, which the repository does not keep, so
the Kiloscope stack's slice order is not recorded.

The notebooks, four at first, ran in 7 min, 19 min, 19 min and 22 min in the
first clean run and 497 s, 1122 s, 1124 s and 1237 s after the answer run.
`entry.py check`, and so `entry.py all`, failed throughout on 11 errors, all
in the deprecated record, which has no outcomes for the new claims and must
stay as it is, and the notebooks were run with `entry.py run`. Round 1's
points led to a check of whether the movie is raw (histogram roughness 0.740
to 0.745, which sub-pixel shifts of 0.13 px RMS lower to 0.052, and a known
jitter of 0.132 px RMS recovered with correlation 0.996), so ed7 is no longer
tentative, PSF readings with the lower-cost fit for each bead, the lines of
each illumination script that load the images, ed8 counts with the quarters
split at the image midlines, the real decoders' single fits compared with the
(n1) null, nine (n2) null decoders per decoding claim, and three new
notebooks, two of (n2) null decoders and one of reduced runs of fig2k, fig2l
and ed9c that decide nothing, none changing an outcome;
`fig2d-lman-sparse-bursting` changed its block reason from `data_missing` to
`methods_underspecified`. In both revisions the 2-hour command limit cut the
run of seven notebooks, and the last, `decoding_reduced.ipynb`, was run on its
own. Round 2 found numbers in the prose that its run did not print, among them
the fig1f margins, the run times and 5 of 56 significant points in the reduced
ed9c run where its run printed 0; the run made for the second revision printed
the prose's fig1f numbers, and the PSF fits, the reduced runs and the timings
turned out to differ between runs on different machines even with every seed
fixed (in the reduced ed9c run, 7 of 56 points significant in one run and 0 in
the other). The cause was not found, and the record gives both runs' values.
Untracked files in the repository root that the author did not create were
left alone. The author's points on the protocol: `entry.py check` fails on the
deprecated `-01` record, which must stay unchanged, so `entry.py all` cannot
pass; the section on repeat attempts assumes the claims file is kept and the
dataset changed, where here the claims file was rewritten and the data were
not; and the claims file sets decoding methods that need 10^5 fits, which a
30-minute limit per notebook cannot decide whatever the data.
