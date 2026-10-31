All four testable claims ran. Two reproduced, two partially reproduced, and the other 13 are blocked because the data are not in the dataset. The entry passes `tools/entry.py check` and `run` (notebook 140 s), and the handover package is in `executed/000875-pakhomov-2023/handover/`. Nothing is committed.

**1. Outcome per claim** (pinned version 0.240515.1925)

| Claim | Outcome |
|---|---|
| fig6a-more-packets-more-uptake | reproduced: order 4 < 20 < 40 packets in all 108 reading combinations; all three t-tests pass in 48 |
| fig6b-peak-relative-to-periphery | partially reproduced: main reading gives 124 / 87 / 59%; 1Px4 reaches 180–220% only with a background subtracted (7 of 72 combinations) |
| fig6-trough-half-of-center | partially reproduced: 1.40 / 2.16 / 2.80; 10Px4 is never within 1.8–2.2 |
| fig6-peak-narrower | reproduced: half-height width 1.05 / 0.55 / 0.49 mm; order holds in 121 of 144 combinations |
| fig4 (2 claims), fig5 (2), fig7 (3), fig8 (3), fig9 (2) | blocked: data missing |
| fig3-field-simulation (with inputs) | blocked: data missing (the Sim4Life model is not public) |

**2. The dataset, assumptions and questions**
- **What it holds:** only the Fig. 6 experiment. That is 9 stitched images, 3 dishes each of 1Px4, 5Px4 and 10Px4, at 3.2 kV. The paper's legend says 3 to 4 dishes per treatment.
- **No spatial information:** the files have no pixel size, electrode positions, ROIs, or statement of which array was used.
  - I assumed 0.65 µm per pixel (the camera pixel through the 10x objective). At that scale the electrode layout fits the small array's ±1.65 mm and cannot fit the large array's.
  - The dark electrode footprints measure 1.66–2.09 mm, wider than the 1.5 mm needles.
  - A variant that places the ROIs from the footprints alone, with no pixel size, gives the same outcomes. So no outcome is marked as resting on the assumption.
- **Metadata errors:**
  - The species is given as *Bos taurus* (cattle), but the cells are CHO (Chinese hamster).
  - The age is "P1D", which means nothing for a cell line.
  - The archive's summary counts 18 subjects for 9 files.
  - Two pairs of dishes share a session start time, one pair across treatments. The images all differ, so no recording was deposited twice.
  - The image series has unit "n.a." and a 2 Hz rate for a single frame, and "200ms" in the file names is unexplained.
- **Question for the paper's authors** (recorded as a `methods_unavailable` finding): which ROI layout, ROI size, background subtraction and normalization order were used for Fig. 6? The fig6b result depends on them.
- **Questions to a reader:** none.

**3. Where the protocol was unclear or did not fit**
1. "Show every stream shares the clock of the trial tables" does not apply to a single image per dish. I said so in the notebook and used the contrast between treatments as the label check.
2. The claims file says a claim holds under any combination of readings. Step 1.6 says the outcome is the one all readings give, or else an assumption. I followed the claims file, since it binds, and reported in each claim's notes how many combinations gave each outcome.
3. The fig6-trough claim has one expected value for three treatments, and "measured" (one number per expected value) cannot express that. I left `measured` out and gave all three values in the notes.
4. It was unclear whether an assumption about a dataset property (the pixel size), as opposed to a method, needs `assumed: true`. I recorded it as a deviation, showed a variant free of it, and did not set `assumed`, because no outcome changes.
5. For `with_inputs` claims whose outside input does not exist publicly, it was unclear whether to also add a link claim. I added none and blocked fig3 as `data_missing`.

**4. Runtime and failures**
- About 33 minutes of the 5-hour budget (17:03 to 17:36 UTC); the notebook takes about 140 s.
- Nothing failed in the final run. The first executed copy had a wrong overlay scale in the thumbnail figure; I fixed it and re-ran.
- The untracked dotfiles at the repository root (`.bashrc`, `scripts` and others) are sandbox device files, not created by this run.

Files are in `entries/000875-pakhomov-2023/`, plus the attempt record:
- `cancan.py`
- `reproduce_pakhomov_2023.ipynb`
- `entry.yaml`
- `README.md`
- `requirements.in`
- `requirements.lock.txt`
- `attempts/000875-pakhomov-2023-01.yaml`
