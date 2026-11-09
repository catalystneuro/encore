I've finished steps 1 to 5 of the Author section and built the handover with `python tools/entry.py handover entries/000632-kim-2023`. The entry passes `lock`, `check` and `all`. Nothing is committed, and I did not verify my own work.

**(1) Outcomes**

| claim | outcome |
|---|---|
| fig3-1hz-co-equals-cross | reproduced: co/cross ratio 0.68, p = 0.32, n = 5 and 6 |
| fig3-770khz-co-enhanced | not reproduced: 1.96-fold higher at 770 kHz, but p = 0.16 |
| fig3-770khz-cross-same-as-1hz | reproduced: ratio 0.84, p = 0.56 |
| fig3-770khz-co-above-cross | not reproduced: 1.59-fold, p = 0.20 |
| fig3-no-area-dependence | reproduced (follows the first claim) |
| fig2-180-cancellation, fig2-crossover-angle, fig2-facilitation-plateau, fig2-60-fold-co-counter, fig4-unipolar-pattern, fig5-base-sawtooth, fig5-apex-larger-polarization | blocked, `data_missing` |

These are the numbers with the footprint background subtracted, using two-tailed Student's t-tests. Every variant gives the same outcome: raw values, Welch's test, a whole-disc footprint background, YO-PRO-1 over MemBrite, centre ROIs 25% smaller and larger, dropping dishes where the footprints may be misplaced, and the deposit as labelled. In all four comparisons the two experiment days point in opposite directions.

**(2) The dataset, assumptions and questions**
- **What it holds:** I pinned version 0.231012.1930, the only published version; the paper cites none. It holds only the Figure 3 square-array experiment: 24 stitched whole-dish images, 1.8 GB each, with a MemBrite and a YO-PRO-1 channel. There are no data for Figures 2, 4 or 5, and the paper says its data are available on request.
- **Duplicate:** `sub-BPAE-8unipolar-1Hz-04` (labelled co-directional) is byte-identical to `sub-BPAE-8bipolar-1Hz-600ns-04` (cross-directional). I counted it once, as cross-directional, based on its start time and its uptake pattern.
- **Group sizes:** with the copy counted once there are 23 dishes, split 5/6/5/7 (co 1 Hz, cross 1 Hz, co 770 kHz, cross 770 kHz). The paper reports n = 6 per group.
- **Metadata:** the dataset and session descriptions say "triangular array", but the images show a square of four electrodes. The files give no pixel size, and subject-name tokens such as "8bipolar" and "600ns" are not explained.
- **Assumptions:** 0.65 µm per pixel, taken from the camera and objective the paper names; the footprints then measure 1.59 mm against the 1.5 mm needles. The footprint background is a 200 µm ROI at each footprint centre. Because every reading gives the same outcome, no outcome is marked `assumed`.
- **Question for the paper's authors** (recorded as a `methods_unavailable` finding): how the footprint background was measured and applied, and which pairs of groups the Figure 3 p-values compare.
- **Questions to a reader:** none.

**(3) Where the protocol was unclear or missing something**
1. Step 2's shared-clock check assumes time series, and these are single images. I checked the condition labels against the images instead: an uptake anisotropy index separates co from cross dishes (Mann-Whitney p = 5.7e-05).
2. "Break down by animal or session" doesn't fit a cell line. I broke the results down by experiment day.
3. The protocol says to count a twice-deposited recording once, but not which of its two condition labels to keep. I chose from the evidence and showed the as-deposited data as a variant.
4. There is no guidance for a missing pixel size. I inferred it, checked it against the footprint size, and ran ROI-size variants.
5. It isn't clear whether an outcome needs `assumed: true` when every reading of an open detail agrees. I left it unset.
6. "Not significant but in the paper's direction" could be read as partially reproduced. I followed the binary criterion and recorded not reproduced.
7. archives.md says to read with remfile, which would take about 15 minutes per file here. I read the HDF5 chunk index and fetched the chunks with parallel HTTP range requests, still streaming with nothing written to disk. archives.md could mention this for large files.
8. Nothing covers the two days pointing in opposite directions. I reported it in the notes.

**(4) Runtime and failures**
- The run took about 55 minutes (04:25 to 05:18 UTC), and the notebook runs in about 290 seconds.
- During development, footprint detection initially failed on some dishes and was fixed. One dish (unipolar-770kHz-600ns-02) still has a probably misplaced footprint, so the variant that drops such dishes covers it.
- Untracked dotfiles that I did not create (`.bashrc`, `.profile`, `.idea`, `scripts` and others) are in the repo root. The workflow should not commit them.

Files are in `entries/000632-kim-2023/`:
- reproduce_kim_2023.ipynb
- epimg.py
- entry.yaml
- README.md
- requirements.in
- requirements.lock.txt

The attempt record is `attempts/000632-kim-2023-01.yaml`.
