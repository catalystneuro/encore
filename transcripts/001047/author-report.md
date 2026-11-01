I finished steps 1 to 6: the entry is locked, checked and run, and the handover is built. Of the 20 claims, 1 is reproduced, 1 partially reproduced, 7 not reproduced and 11 blocked. The dandiset holds only part of the paper's data, and what it holds does not show the paper's main effect.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig2-heating | Blocked (data_missing) |
| fig3a-centre-enhanced | Not reproduced (assumed) |
| fig3bc-rate-suppresses-off-target | Not reproduced (assumed) |
| fig3-lorentzian-profile | Not reproduced (assumed) |
| fig3-tail-deviation-falls-with-rate | Partially reproduced (assumed; holds at burst label x1 only) |
| fig4b-centre-no-rate-effect | Reproduced (assumed; p = 0.93 and 0.54) |
| fig4b-near-electrode-decline | Not reproduced (assumed) |
| fig4b-40-fold-ratio | Not reproduced (ratio −0.29 to 2.48 against 40) |
| fig4c-fwhm-falls-with-rate, fig4c-log-trend | Blocked (data_missing) |
| fig5-raised-electrodes-weaken-centre | Blocked (data_missing) |
| fig5ab-yp-spot-slightly-larger-than-pr | Not reproduced (assumed; YP/Pr width ratio 0.65 to 0.76) |
| fig5b-gaussian-pr-lorentzian-yp | Not reproduced (assumed) |
| fig5c-nuclear-yp-centre | Blocked (data_missing) |
| fig6b, fig6c, fig6d | Blocked (data_missing) |
| fig7be, fig7cf, fig7-sharpest-one-burst | Blocked (data_missing) |

## 2. The dataset

**Version.** I pinned 0.250701.1609, the latest published version. The paper cites none. It has the same 88 assets as the draft; the first version had only the 54 CT26 files.

**Contents.**
- CT26 cells at 1 Hz and 0.2 MHz, CANCAN and control, with burst labels x1, x2, x3 and x5. Each file holds one stitched image of one or two wells.
- CHO cells with a single burst label. These images are 13 mm across, too small to show the electrode array.
- Missing entirely: 1 kHz and 10 kHz, 300- and 900-ns pulses, raised electrodes, film thermometry, and a CHO series over burst numbers.

**Metadata problems.**
- The dandiset description and every file's protocol text say 3.8-mm electrode spacing and a 3.2-kV first pulse. The CT26 images show the paper's 15.3-mm array instead.
- The CT26 files state no pixel size. I inferred 1.625 µm for whole-well images and 3.25 µm for two-well images from the array geometry.
- The burst number appears only in the subject label; most descriptions say "Unknown repetitions".
- The CHO files' start time is the conversion date, not the acquisition date.
- I found no well deposited twice.

**Result against the paper.** At the burst labels both rates share, the 0.2 MHz CANCAN wells are either unstained (x1) or broadly stained (x5). Neither shows the paper's sharp central spot. The dandiset's images may be other experiments than the paper's figures.

**Assumptions** (each recorded with `assumed: true`):
- The rates are compared at each burst label both share (x1 and x5), because the paper's "2 bursts (x4)" cannot be identified among the labels.
- The wells imaged for propidium had the electrodes touching the monolayer.
- Background is the mean of the four electrode footprints.
- The array centre is located from the electrode footprints, or from the stain's centroid in faint images.

The questions for the paper's authors are recorded as a `methods_unavailable` finding. I asked a reader nothing.

## 3. Protocol issues

1. No rule says how to judge a claim whose condition (here, the burst number) cannot be matched to the dataset's labels. I tested at every shared label and set the rule before computing: reproduced at both, partial at one.
2. Several claims ("every rate", a trend over rates) can only be partly tested when some conditions are missing, and it is unclear whether that is blocked or a deviation. I tested the rates present and recorded the missing ones as deviations. For the claims whose required comparisons were all at missing rates, I blocked them.
3. Step 2's clock check does not fit single time-point images. I checked the condition labels and the left/right sides against what each condition does to the stain pattern instead.
4. Image data with no annotations need a way to place regions of interest. I automated it with a template match plus a fallback, and show every placement in a figure for the verifier.

## 4. Runtime and failures

- The notebook runs in 10.2 minutes, most of it streaming 42 images (11.5 GB).
- The run took about 2 h 40 min; I finished at 05:18 UTC.
- One development run timed out after an hour because my duplicate check compared every pair of images; I cut it to pairs of the same condition. That cost an hour but changed no result.
- Three areas were dropped because their centre fell at the image edge.
- There are untracked dotfiles (`.bashrc`, `.idea`, `.vscode` and others) in the repository root. I did not create them and left them alone.

Files are in `entries/001047-silkuniene-2025/`:
- reproduce_silkuniene_2025.ipynb
- cancan.py
- README.md
- entry.yaml

The attempt record is `attempts/001047-silkuniene-2025-01.yaml`.
