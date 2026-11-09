I ran `python tools/readme_row.py 001172 --write`. It added the row to README.md: 13 reproduced, 7 partially, 1 not reproduced, 5 blocked. I then appended the subsection below to the end of `docs/pilot-notes.md`. Nothing is committed. The repository root has untracked files I didn't create, such as `.bashrc`, `.idea` and `scripts`, and I left them alone.

Two judgement calls:
- The last five subsections all end with a paragraph on run times and failed steps before the protocol points. I followed that shape, so the run times and the denied directory deletion are in the last paragraph.
- In the protocol sentence I left out the author's figure of about 85 GB streamed. The author later dropped a similar size (110 GB) because no output supported it.

### 001172, Lohani et al. 2022

Thirteen claims reproduced, seven partially, one not reproduced and five
blocked on the dandiset. Round 1 gave its own outcome for each claim from the
notebook with its conclusions removed and agreed with all 26, but noted that
the wheel predictor of the Figure 2 regressions was signed speed while the
paper says locomotion speed. The author then made |speed| the main predictor,
under which wheel speed beats face PC1 in grabAM06 (0.147 against 0.142), and
lowered `fig2c-face-best-predictor-calcium` to partially reproduced. Round 2
agreed with 25 of the 26 and disputed that reason: the Methods define speed as
a differential of distance, which keeps the sign, and the paper's
`wheel_changepoints.m` uses a signed `db1SpeedMpS`. The author returned to
signed speed, added a comparison with the paper's own per-mouse R2 values in
`Fig2RawData.mat`, where the row matched to grabAM05 gives a calcium wheel R2
of 0.0246 against 0.0253 here with signed speed and 0.0483 with |speed|, and
proposed reproduced. A third round reviewed only that proposal and agreed, and
the claim is reproduced. The paper images ACh (ACh3.0) and calcium (jRCaMP1b)
together across the dorsal neocortex of awake mice, and reports that facial
movement and locomotion relate to both signals with opposite
anterior-posterior gradients, that transients and sustained states differ
across areas, and that correlations between areas and the coupling of ACh and
calcium change with behavioural state. The link to the paper's Allen parcel
masks, the regressions of Figure 2, the transients at face and locomotion
onsets, the sustained states, the correlations between areas and the
ACh-calcium coupling were tested. The ECoG, scopolamine, hemodynamic
correction, sensor validation and cholinergic axon claims are blocked as
`data_missing`. `fig5-coupling-down-frontal-with-locomotion` is not
reproduced: coupling is lower with locomotion in all 23 parcels but no parcel
decreases significantly at q = 0.01, and the largest decreases are in PTLp and
SSp-tr, not frontal cortex. Some outcomes rest on weak ground:
`allen-parcel-link` is partially reproduced under a per-session reading of its
mask criterion chosen after one movie was seen to fail it per movie (0.996
against 0.999), which would make it not reproduced; the claims of Figures 3 to
5 rest on 3 mice, and without grabAM06, which contributes 2 epochs per state,
the LSD p of `fig3c-ach-sustained-face` is 0.207 and the paired t p of
`fig3d-ach-frontal-above-visual` is 0.247; `fig3c-ach-locomotion-no-further-increase`
is an absence result where locomotion exceeds high face in all 3 mice; and
the ACh mean of `s7-face-onset-transients` is inside tolerance by 0.002. The
author used the author manuscript in PubMed Central (PMC10661869) and took the
parcel masks and the procedures the Methods leave open from the paper's code
at commit c337686.

The dandiset was converted by CatalystNeuro (catalystneuro/higley-lab-to-nwb).
It holds 4 of the 6 ACh3.0 and jRCaMP1b mice of the paper's code (grabAM05 to
grabAM08) and no ECoG, drug sessions, control mice or ChAT-GCaMP6s mice, so
five of the paper's findings cannot be tested. The ΔF/F series are given the
starting time of raw frame 0 while their frame 0 is raw frame 499, so their
times are 49.9 s early in every session. The FaceMap, pupil, eye and video
timestamps are spaced 111 ms where the camera pulses are 100 ms apart, span
about 10% longer than the session and end with two values equal to the first
camera pulse; with them face movement and wheel speed are misaligned by 23 to
60 s, and with frame i at camera pulse i, as the paper's code does, they
align. RoiResponseSeriesParcellated holds the calcium ΔF/F but its
segmentation is linked to the ACh imaging plane, its image masks are
transposed relative to the ΔF/F images, and its starting time is 64.9 s before
its first frame. The ΔF/F descriptions mention detrending only, while the blue
and green ΔF/F are also hemodynamically corrected and registered to the Allen
atlas, rotated by 180 degrees; the Allen parcels the paper analyses are not in
the files, and the parcellation that is there is a functional one with 89 to
107 ROIs per session and no area names. Other findings: in the VisualStimulus
tables the columns from `stimulus_size` on are shifted by one, and the tables
do not say where the monitor stood relative to the mouse; the air-puff session
grabAM07 11262019 has no Airpuff table, and no puff in the other tables (29
puffs) is followed by a locomotion onset within 5 s, which fits the code
keeping only puffs without running, a selection the files do not state;
WheelSpeed and pupil_area have the unit "unknown", and WheelSpeed is signed,
which its description does not say; and in the calcium ΔF/F of grabAM08
11232019 spont 263 pixels inside the brain mask, all in the right AUD parcel,
are zero in every frame.

The notebook ran in 716 s in the first clean run, 12.1 minutes after round 1,
17.1 minutes after round 2 and 1047 s after round 3. One development run
failed because the helper module was missing from the scratch directory, and a
request to delete an empty harness directory in the entry was denied. Round 2
also found statements the outputs did not support, among them that the tests
across mice lose significance without grabAM06, where calcium locomotion above
high face stays at p = 0.019 and the calcium sustained-state gradient becomes
significant (p = 0.037), a runtime of 13 minutes and a data size of 110 GB,
and these were corrected or removed. Untracked files in the repository root
that the author did not create were left alone. The author's points on the
protocol: a link criterion found ambiguous after the analysis, with no rule
for a link claim that fails on one movie when 21 claims depend on it; parcel
masks that name pixels but bring no measurements, which `with_labels` does not
exactly cover; signed-rank tests that cannot reach p < 0.05 with 4 mice; the
paper's uncertainty given as mean ± SEM; no rule for leaving out a session
whose event table is missing or for how few mice is too few; no rule for whose
timing convention to use once the file times are shown wrong; and a 10-minute
runtime aim the streamed data volume rules out.
