I've done steps 1 to 5 for DANDI:000633 and ran the handover (step 6). The checks pass with 0 errors, and the notebook ran from a clean environment in 184 s. Nothing is committed.

The dataset holds only the two images of Figure 4, so three claims could be tested. All three came out reproduced, and two of them rest on an assumption. The other nine are blocked because their data are not deposited.

**1. Outcome per claim**

| Claim | Outcome |
|---|---|
| fig2-cancellation-at-180, fig2-crossover-angle, fig2-facilitation-plateau, fig2-60-fold-co-counter | Blocked: data missing |
| fig3-1hz-co-cross-same, fig3-770khz-co-enhanced, fig3-770khz-cross-same-as-1hz | Blocked: data missing |
| fig4a-single-pulse-follows-field | Reproduced, assumed (which base electrode was pulsed) |
| fig4bc-paired-pulse-focal-apex | Reproduced (apex/base uptake 2.7 to 8.1 with paired pulses; 0.05 to 0.20 with single pulses) |
| fig4-comet-shape | Reproduced, assumed (a maximum that ignores one isolated bright object) |
| fig5-base-sawtooth, fig5-apex-larger-polarization | Blocked: data missing |

**2. What was found about the dataset**
- **What it holds:** version 0.231013.2226, the only published one; the paper cites no version. Two NWB files, each one stitched whole-dish image of about 1 GB in two channels (MemBrite, then YO-PRO-1). These are Figures 4A and 4B. The data behind Figures 2, 3 and 5 and the field simulation are not deposited.
- **Format error:** the image is stored as an `ImageSeries` whose first axis NWB reads as time, at a rate of 2 Hz. A standard reader sees 22323 frames instead of one image.
- **Missing metadata:** no pixel size, channel names or intensity unit. The scale comes from the 1.5 mm needles: 0.654 µm per pixel, which matches the camera and objective named in the file. Nothing records which base electrode was pulsed (E1).
- **Metadata errors:**
  - The single-pulse file's description gives Figure 3's settings (770 kHz, 10 kV/cm, co-directional pairs), but its image shows the triangular array of Figure 4A.
  - The paired-pulse file says 2 kV where the paper says 4 kV. My field model gives 4.2 to 9.7 kV/cm along the bisecting line at 4 kV, close to the paper's "5 to 10 kV/cm".
  - The description mentions a six-well plate (the paper used 35 mm dishes), the age is "P1D" for a cell line, and each "subject" is a condition.
- **Field map:** the paper's Sim4Life map isn't available, so I computed it with a 2D finite-difference solve. It uses the paper's geometry (Methods 4.2 and 4.3) and the electrode positions measured in the images. This is recorded as a deviation.
- **Assumptions:**
  - fig4a: E1 is the right-hand base electrode. This assumption is partly circular, and the record says so. Under the other assignment the correlation is still positive (rho 0.42 to 0.51) but the order of the electrode neighbourhoods does not match.
  - Comet: the literal maximum sits on one object about 9 times brighter than the dish's 99.9th percentile, and under it the region vanishes. I used the 99.5th percentile and a median-filter maximum instead; both give the comet.
- **Questions for the paper's authors** (recorded as a `methods_unavailable` finding): which electrode is E1 in the deposited image, and how agreement with the field map and the comet region were judged.
- **Questions to a reader:** none.
- **For information only:** the notebook computes an 833 kHz angle curve from the two Figure 4 images. It gives 5.8-fold cancellation near 169°, against the paper's 20-fold, and a 100% crossing near 128°. It decides no outcome.

**3. Where the protocol was unclear**
1. A claim needing two conditions where only one condition's kind of data exists (833 kHz but no 1 Hz). Also, the rule that blocks claims depending on blocked claims hides fig2-60-fold, which needs only 833 kHz. I blocked all Figure 2 claims as data missing, because the deposited images are Figure 4's experiment, not Figure 2's. The 833 kHz numbers from them are in the notes and the notebook.
2. A `with_inputs` claim whose outside input (the simulation) is not public, but can be recomputed from the paper's stated geometry. The protocol only says to block it as `data_missing`. I recomputed it and recorded it as a substituted model, listing the paper's DOI under `inputs`.
3. A missing label that leaves a criterion's readings disagreeing (which electrode is E1). It is unclear whether that is `metadata_insufficient` or an assumption. I adopted the assumption, set `assumed: true`, and showed both assignments.
4. The step 2 check that every data stream shares one clock does not apply to still images. I said so in the notebook.
5. The criterion's "maximum" is broken by one outlier. The protocol has no rule for robustness choices inside a criterion. I treated it as a reading under step 1.6 and showed all three versions.

**4. Runtime and failures**
- About 31 minutes of work, 05:47 to 06:18 UTC. The notebook runs in about 3 minutes, mostly streaming 2.1 GB into memory with nothing written to disk.
- Only small failures during development: one NaN-rounding error and one YAML quoting error, both fixed.
- `git status` shows untracked files I did not create and left alone: `.bashrc`, `.profile`, `.zshrc`, `.idea`, `.vscode`, `scripts` and others.

Files are in `entries/000633-kim-2023/`:
- reproduce_kim_2023.ipynb
- swing.py
- README.md
- entry.yaml
- requirements.in
- requirements.lock.txt

The record is `attempts/000633-kim-2023-01.yaml`, and the verifier's package is in `executed/000633-kim-2023/handover/`.
