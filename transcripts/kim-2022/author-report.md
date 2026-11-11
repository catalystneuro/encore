The attempt is written and passes its checks: entry at `entries/kim-2022`, record at `attempts/kim-2022-02.yaml`. `tools/entry.py all` gives 0 errors and the notebook runs in 494 s; `handover` built the verifier package in `executed/kim-2022/handover/`. Of the 25 claims, 12 were tested and 13 are blocked. Nothing was committed, and I did not come across any earlier attempt's results.

**(1) Outcomes**

| Claim | Outcome |
|---|---|
| fig2a-uptake-rises-with-field | reproduced (assumed: unpaired t-test; the paired test passes 3 of 5) |
| fig2a-vertical-scales | not reproduced (75% mean + s.e.m. is 339 a.u., axis says 250) |
| fig2b-exponential-same-slope | partially reproduced (exponential fits better for 3 of 5 at 8 kV/cm; no slope differs) |
| fig2c-max-inhibition-50-75 | partially reproduced (50% gives 49% of unipolar, not 20%) |
| fig2c-inhibition-flat-above-8-7 | reproduced |
| fig2c-weaker-at-6-7 | reproduced (assumed: unpaired) |
| fig7-unipolar-pole-polarization | reproduced (assumed: pole regions, cathode side) |
| fig7-charging-time-constant | not reproduced (charging tau 191 ns matches; amplitudes 23% against 31%, discharge tau 613 against 520 ns) |
| fig7-later-pulses-same-tau-difference | partially reproduced |
| fig7-bipolar-overshoot | reproduced |
| fig7-bipolar-alternation | reproduced |
| fig7-summation-without-buildup | reproduced |
| Figs. 3 to 6 (12 claims) | blocked: dataset_missing |
| fig1e-heating | blocked: data_missing |

**(2) What I found about the datasets**
- **Missing figures:** 000489 holds only the 17 Fig. 2 dishes plus one Fig1F staining sample; 000448 holds the Fig. 7 strobe data.
- **Three more datasets for this paper:** DANDI 000548, 000549 and 000550 name the paper in their metadata and match Figs. 3, 4 and 6 by title. They are not in `papers/datasets/kim-2022.yaml`, so I did not use them. I listed them under `missing_datasets` and blocked those 12 claims; a later attempt could test them.
- **Duplicate image:** the YO-PRO-1 channel of sub-Fig2-0-03 (unipolar) and sub-Fig2-25-04 (25%) is the same image, while their MemBrite channels differ. The main analysis leaves both out, so the unipolar and 25% groups have 2 dishes each; assigning the image to either group is shown as a variant.
- **Missing metadata in 000489:** no pixel size, electrode positions or polarity, or ROIs. The electrode spacing I measured, 4.44 to 4.66 mm against the paper's 4.5 mm, supports 0.65 µm per pixel. The image description's "Channel1" naming does not say which channel holds which dye (the data show index 0 is MemBrite, index 1 YO-PRO-1), and it says "144 images, six-well plate" where the paper says 216 images of 35 mm dishes.
- **000448 has 9 cells, not 18:** 5 unipolar and 4 bipolar, against 18 and 17 in the paper. Each cell is filed as two subjects (forward and reverse trial).
- **Undocumented frame order in 000448:** reverse files store frames in acquisition order and are offset by 74 frames (1.85 µs) from the forward trial. No frame delays, pole regions or field direction are given, and the first frame of most files is dark.
- **Assumptions:**
  - Unpaired t-test where the paper does not say.
  - ROIs tiled every 200 µm from the centre out to 3 mm.
  - A footprint disc of 0.2 mm for the background values.
  - Fields from an exact 2D two-cylinder model, scaled to the paper's 15.1 kV/cm at the centre.
  - The pole regions I drew.
  - The pole that brightens taken as cathode-facing.
  - Pulse onset found from the data.
- **Questions for the authors** (recorded as `methods_unavailable` findings): how the ROIs were placed and whether the t-test was paired; how the pole regions were drawn and where the cathode was relative to the image.
- **Questions to a reader:** none.

**(3) Protocol points**
1. Claims list a dataset the paper does not name for their data. The claims file lists the Fig. 3 to 6 claims under 000489, but they belong to other public datasets of the same paper. Neither `data_missing` nor `dataset_missing` fits exactly; I used `dataset_missing` with `missing_datasets` and noted it.
2. Repeated recordings stored differently. The protocol asks to count duplicated recordings once but says nothing about a channel shared between two files of different conditions. I left both dishes out and showed both assignments.
3. Criteria with no outcome for some cases. fig2b gives no outcome for "slopes agree but the exponential fails", and fig2c-max does not say at how many fields "the test holds". I chose partially reproduced and "most fields", and recorded each as a deviation.
4. "Develop on a subset" says nothing about caching data during development. I cached block-averaged images in the scratch directory for development only; the notebook streams everything.

**(4) Runtime and failures**
- About 2 h (03:20 to 05:20 UTC). The notebook takes about 8 minutes and peaks around 2 GB of memory.
- About 1 h was lost when a footprint-search command with a large direct convolution hit its 60-minute timeout. I replaced it with FFT convolution.
- Earlier, a background download was killed when its shell call ended; I re-ran it in the foreground.
- Nothing else failed.
