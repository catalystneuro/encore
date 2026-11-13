I've done steps 1 to 6 of the Author section for martinez-conde-2019. The entry passes `check` with 0 errors, the clean run of `all` passes in 276 s, and the handover is built in `executed/martinez-conde-2019/handover/`. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| neuron-counts | not reproduced |
| spikes-per-condition | blocked (data_missing) |
| s4-baseline-no-difference | not reproduced, assumed |
| fig4a-above-baseline | reproduced, assumed |
| fig4b-spike-rate-difference | partially reproduced, assumed (P180 is 6.47 against 4.87 ± 1.15) |
| fig4b-pairwise-significance | reproduced |
| fig5-average-maps | reproduced, assumed |
| table1-edge / table1-s90 / table1-s40 | reproduced, assumed |
| table1-s52 | partially reproduced, assumed |
| table1-p180 | not reproduced |
| fig6-midpoint-representative | reproduced |
| fig7a-rms-contrast-fit | not reproduced |
| fig7c-fold-edge-equivalence | not reproduced, assumed |
| fig7c-fold-edge-significance | reproduced under the two BH readings, assumed; fails under Bonferroni |
| fig7d-nonlinear | reproduced, assumed |
| fig7d-dog-similar | blocked (data_missing) |
| s3-latency-peak | blocked (data_missing) |

## 2. Dataset, assumptions and questions

**Version.** CRCNS has no versions, so it is recorded as `unversioned`. The notebook checks that the zip's ETag on the bucket equals its MD5 in `checksums.md5` (e1301fe4…, last modified 2026-02-11), as the header explains.

**What the files hold:**
- **Fewer neurons.** 53 neurons, not 58. The spreadsheet has 58 rows, but five have no data. Per condition there are 22 Square and Edge, 27 Star and 26 Corners recordings, against the paper's 25, 30 and 28.
- **Two mislabelled files.** `ABS042700J2` and `ABS051000J3`, in the Star folder, are Corners-type recordings.
- **The descriptor is wrong about the fields.** `image` is a spike rate per 1 ms sample, not a count. `smoothed_image_norm` is often missing and its meaning varies. Most files hold an undocumented `Standard` struct: the authors' map aligned to the stimulus, the stimulus polygons, and sometimes a `BaseActivity` value.
- **15 Star files can't be used.** The maps are in gaze coordinates, and no file gives the receptive-field offset that places them on the stimulus. Only 12 of the 27 Star files have the aligned map, so the Star claims rest on those 12.
- **Raw data are absent.** No spike times, eye positions or spike-count maps, and only one eye-time map, so the spike counts and the latency analysis cannot be done.
- **Edge off screen.** In four files the 100% end of the Edge is off the screen, which the Methods say never happened.
- **Alignment check.** Across the Edge, the mean response peaks on the Edge itself; 16 of 22 neurons peak within 8 DU of it. That is consistent with the authors' alignment.

**Assumptions:**
- **Corners fold.** The pattern has one bright and one dark 40° fold. I took the bright one, citing Methods, Corners paragraph 2 ("we only analyzed symmetric bright corner-folds"). Averaging the two breaks the fold order.
- **Baseline squares.** I centred them on the corners of the circumscribing square. For Corners, I put them at the bottom corners of the region of interest, since Fig 2C is not in the text. The files' own `BaseActivity` matches no placement the text allows. The baseline test and several Table 1 counts change with this choice; every placement is shown in the notebook.

**Questions for the authors** (recorded as `methods_unavailable` findings):
- Where the baseline squares are, and how `BaseActivity` was computed.
- Whether the Corners response uses the bright fold alone.
- How the RMS contrast of Fig 7A was defined. From luminance in percent, neither reading gives 0.61 to 0.943.

**Questions to a reader** (`questions/martinez-conde-2019.yaml`): for fig4b-spike-rate-difference and table1-s40. The criterion's Corners readings average a bright and a dark fold, or take "the fold at the ROI centre". In the data neither fold sits at the centre.

## 3. Where the protocol was unclear or did not fit

1. Step 2's "shares the clock of the trial tables" does not fit data that are spatial maps with no time base. I used a spatial contrast instead: the response profile across the Edge.
2. The protocol assumes data close to the recordings. Here the dataset is the authors' processed maps. I used their aligned frame and recorded that the eye-signal correction and registration cannot be redone.
3. Two rules for several readings sit side by side. A claim is reproduced if any of the criterion's readings matches. For a method detail left open (author step 1.6), the readings must agree, or the best-supported one is adopted as an assumption. I applied the first to the criterion's readings and the second to the baseline placement.
4. A claim of absence is to be judged on "the paper's test", but the paper names none, and the outcome flips with an open method detail. I recorded the main reading's result and marked it assumed.
5. `measured` says which reading to record when several match, not when none do. I recorded the main reading.
6. When a claims-file reading does not fit the data's geometry (the "ROI centre" fold), it is not clear whether that counts as a misreading. I asked a reader.
7. "Pinned published version" does not map onto unversioned CRCNS. I used the ETag-to-MD5 check.

## 4. Runtime and failures

The notebook takes about 4.6 minutes, with peak memory about 1.1 GB; the whole session took about 45 minutes. Nothing failed. The whole dataset runs in 5 minutes, so I developed on all of it, not on a subset.

One cleanup was refused: removing an empty `.claude/` directory inside the entry needed approval. It holds no files, so git will not pick it up. Stray dotfiles at the repository root (`.bashrc` and others) were not created by me and I left them alone.
