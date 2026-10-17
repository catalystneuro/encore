I did steps 1 to 6 for dandiset 000350 and handed over for verification. The entry passes `check`, and the notebook ran from a clean environment in 609 s. The handover package is in `executed/000350-mu-2019/handover/`. I did not verify my own work and did not commit.

The paper is open access (CC BY-NC-ND), so I used the full text: main text and STAR Methods, from the PDF on the first author's lab site (Cell's own site blocked the download). It is saved under `paper/`. The Supplemental Information was not read.

## 1. Outcome per claim

| Claim | Outcome |
|---|---|
| fig1h-epoch-durations (passive 24.4 s, active 36.1 s, 29 bouts per active epoch) | partially reproduced: 20.5 s and 19.1 bouts within tolerance, active 22.4 s outside |
| methods-isi (1.2 s closed loop, 1.19 s in active epochs) | partially reproduced: 1.143 s within, 1.332 s outside |
| fig1j-open-loop-passivity | not reproduced (median 0.551 open against 0.546 closed, p = 0.285) |
| fig1c-vigor-open-loop-onset | reproduced (9 fish, median power ratio 3.49, p = 0.0195) |
| fig1i-isi-before-passivity | not reproduced (p = 0.103 and 0.16; holds with a different minimum epoch length) |
| fig2bc-neurons-lower-in-passivity | reproduced (8 of 8 fish, p = 0.0039) |
| fig2c-glia-rise-at-passivity | not reproduced (2 of 4 fish; the criterion needed 3) |
| figs2a-open-loop-higher | partially reproduced (neurons both measures; glia 3 of 4 fish) |
| fig2h-glia-weaker-closed-loop-pauses | not reproduced (2 of 4 fish) |
| fig2dg-nmf-components | blocked: data_missing |
| fig2kl-lmo-glia-most-consistent, fig6a-ne-ramp | blocked: metadata_insufficient |
| fig1k, fig1f, fig4, fig5, fig6-ne-drives-glia, fig7-ne-mismatch, fig7-glia-accumulate | blocked: data_missing |

## 2. What was found about the dandiset

- **Contents:** 12 light-sheet sessions (150 to 940 GB each), all with swim and stimulus signals. Only 8 have cell traces: 4 with neurons and glia imaged together, 4 with neurons only. The other 4 are raw images only, and they include the only 3 glia-only GCaMP6f fish (the paper's glial analysis used 6). Nothing from Figures 4 to 7 is in it.
- **Mislabelled indicator:** the glial plane of the two-colour files says GCaMP6f, but it is excited at 561 nm and detected at 660 nm, which is jRGECO1b. The raw images are typed `TwoPhotonSeries`, but the microscope is a one-photon light sheet.
- **`DfOverF` is not ΔF/F:**
  - In 4 files each ROI's trace is divided by its own mean (mean 1).
  - In the other 4 the traces are centred on 0 and the first 60 s are held constant.
  - `Fluorescence` looks like a slow baseline, and has the same description as `DfOverF`.
- **Missing imaging:**
  - sub-20170113-2 has 7616 imaging volumes against 9751 camera triggers.
  - Raw images are missing for part of sub-20170113-4 (3065 of 12050 volumes) and sub-20170228-4 (5776 of 7200).
- **Undocumented tables and signals:**
  - `ActivityStates` does not follow the Methods' definition: many "active" rows last 5 s or less, the "transient" rows duplicate active rows, and the glia-only files have only 3 rows.
  - The stimulus protocol codes, gain and velocity signals have no units or descriptions.
- **No anatomy:** there is no registration to a reference brain and no region labels, so L-MO and NE-MO cannot be located.
- **Clock:** imaging timestamps equal the camera-trigger edges, and the neuronal signal follows swimming with a 0.3 to 5 s lag. This is consistent with one shared clock.
- **Version pinned:** 0.240822.1759. The paper cites no version. Compared with 0.221219.1506, it renames the imaging series and fixes the plane name of the 3 glia-only files. The behaviour and traces are identical in both.

## 3. Where the protocol was unclear, wrong or missing something

1. **SEM as tolerance.** The protocol says to use "the paper's own uncertainty", but the paper gives SEMs over 74 fish. I used 1.96 × SEM and gave the reason in the claims file.
2. **Code that does not cover the analysis.** The linked code (segmentation only, commit 54d1907) covers none of the behaviour or onset analyses. The protocol assumes the code settles open choices; here I could only follow the Methods and record my own choices.
3. **No rule for normalisation.** The protocol has no rule for traces whose scaling differs between files. I compared only within each fish, scaled by that fish's trace SD.
4. **No rule for reading a subset.** The full trace tables (6 to 10 GB per series, gzip) do not fit the time limit. I used a fixed 8 to 15% subset of ROIs, and showed two disjoint subsets agree (correlation 0.98 and 1.00).
5. **Sample size of a subset.** The paper's behavioural numbers come from 74 fish; the dandiset has 12 of them. I recorded this as a deviation without changing tolerances.
6. **Untested criterion choices.** The fig1i result flips with the minimum epoch length (10 bouts fails, 8 bouts passes). The protocol fixes the choice before analysis, which I followed. It gives no way to say a criterion was fragile except to show variants, which I did.
7. **Which blocking reason to choose.** For the NMF claim several apply: part of the data is missing (3 of 6 fish), the rest is raw only (too large), and the clustering was tuned by hand. I recorded data_missing and named the others in the notes.

## 4. Runtime and what failed

- The notebook takes 609 s; 424 s of that is reading traces.
- About an hour was lost when a version-comparison script that walked every dataset of 24 remote files hung until the 60-minute timeout. I redid it with targeted reads and a hard timeout.
- Two notebook runs needed fixes before the final run:
  - a ragged-array error in the 8-bout variant;
  - the open/closed-loop comparison counted stationary-grating changes as switches and divided an uncentred mean by the SD.

Both are fixed in the final run.
