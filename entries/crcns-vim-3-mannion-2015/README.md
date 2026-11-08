# Mannion (2015) from CRCNS vim-3

Tests the findings of [Mannion (2015)](https://doi.org/10.7717/peerj.1038) on
[CRCNS vim-3](https://doi.org/10.6080/K0JS9NC2), which holds the raw functional runs, event
sequences and central-task records of the seven participants, and the stimulus screenshots. The V1,
V2 and V3 definitions, cortical surfaces and anatomical images are not in it, and every response
measure of the paper is taken in V1 to V3, so the response claims cannot be tested.

| Claim | Outcome |
|---|---|
| Central task performance does not differ across conditions (Figure S2) | Reproduced |
| Localiser masks, presentation by source interaction, lower and upper field effects, Figure 4, residuals (Figure S3) (9 claims) | Blocked: data missing (V1 to V3) |
| Image statistics against responses (Figure 5) (5 claims) | Blocked: data missing (V1 to V3 responses; monitor calibration) |
| No radial bias in the image patches | Blocked: metadata insufficient (monitor calibration); under two assumed calibrations no test reaches p < 0.05 |

The notebook also fits the paper's GLM in the volume to check that the event sequences share the clock
of the volumes, that the NIfTI series are the runs in order, and that the upper and lower field
responses fall on the ventral and dorsal sides; this holds for six participants and could not be
established for p1011. A last section repeats the response analysis on a volume localiser region that
is not V1 to V3, for information only, and the radial-bias test is run on the stimulus screenshots
under two assumed monitor calibrations, also for information only.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/crcns-vim-3-mannion-2015-01.yaml`](../../attempts/crcns-vim-3-mannion-2015-01.yaml).
