I finished steps 1 to 6 of the Author section. Of the 22 claims, 15 are reproduced, 1 is partially reproduced and 6 are blocked; none is not reproduced and no outcome rests on an assumption. The entry passes `tools/entry.py all` (0 errors, the notebook runs in about 18 to 20 minutes) and the handover is built in `executed/001425-kondo-2025/handover/`. Nothing is committed.

The entry is `entries/001425-kondo-2025/` (notebook, helper `bdbc.py`, README) and the record is `attempts/001425-kondo-2025-01.yaml`. I pinned version 0.250705.0947: the paper cites no version, and this most recent one is the only one with the day-0 resting-state sessions of all 25 mice, which one claim needs. The earlier version lacks those six sessions; the notebook shows the difference.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| cohort-sex-age | reproduced |
| task-sessions-collected | reproduced |
| imaging-frame-counts | reproduced |
| training-breaks | reproduced |
| fig3c-response-rate-increase | reproduced (0.556 in session 1, 0.856 in session 15) |
| fig3c-success-rate-constant | blocked, methods_underspecified: no trend (Spearman p 0.36), but session 15 is 27% above session 1, and the criterion blocks the claim when its two readings disagree |
| fig3d-tpull-clusters | reproduced (7 and 18 mice, on the 15 values; not on the differences) |
| fig3e-cluster-a-high-tpull | reproduced |
| fig3e-cluster-b-similar-rates | reproduced, but only when successes are counted from reward pulses over sessions 11 to 15; counted from the outcome labels, the success rates differ by more than 10% |
| methods-no-signal-degradation | reproduced |
| fig4ab-landmark-validation | blocked, data_missing |
| fig4d-visual-map, fig4d-tactile-map, fig4d-auditory-map | reproduced (from the 44 ROI series only) |
| figs2b-no-aberrant-transients | reproduced |
| fig5abc-dlc-error | blocked, data_missing |
| fig5f-lever-tip-correlation | reproduced (R 0.981) |
| fig5f-forepaw-correlation | partially reproduced: the correlations match, but 356 sessions qualify against an exact 354 |
| fig6b-movement-order | blocked, methods_underspecified (the claims file's rule when no reading holds) |
| fig6b-motor-somatosensory-after-reward | reproduced |
| fig6b-sensory-areas-track-pupil | blocked, methods_underspecified (only the olfactory bulb follows the pupil) |
| fig6b-variability-decrease | reproduced |

**2. What was found about the dataset**
- In all 495 files the excitation wavelengths of the blue and violet imaging planes are swapped.
- The lever and other sensor channels are stored with unit "a.u." and "no description". The paper's code gives mm for the lever.
- The sensory-mapping stimulus codes 1 to 3 are not described anywhere in the files.
- Six sessions of the earliest cohort have no visual-stimulus channel. In them the visual flashes are recorded on the whisker channel and the touch stimulus on the auditory channel, and there is no third stimulus.
- In the other sensory sessions the trial order, by channel name, is visual, auditory, touch; the Methods say visual, touch, auditory.
- Reward pulses outnumber trials labelled "success" in 205 of 364 task sessions.
- The down-sampled keypoint likelihood arrays keep the 100 Hz length next to 30 Hz data.
- Some pupil diameters are infinite or larger than 1e5 pixels.
- The dataset has 357 task sessions with body keypoints; the paper says 355.
- The starting pull-duration rule in the Methods (previous final minus 100 ms) holds in 219 of 332 consecutive session pairs.
- Four sensory-mapping sessions last 20 minutes, not the stated 15.
- The paper describes TIFF files; the stacks are inside the NWB files instead.
- The manual annotations behind the landmark and DeepLabCut validations are not deposited.
- No recording was found deposited twice.
- Assumptions: none. The keypoint that tracks the lever tip (`rightbartip`) is named "The tip of the lever" in the paper's linked code (bdbc-nwb-explorer at 309c5fb). That file is listed under `inputs`.
- Questions for the paper's authors, recorded as `methods_unavailable` findings:
  - Which session is the Figure 6 example, and how were the movement onsets and the match with the pupil judged?
  - What test or bound supports "the success rate seemed to be constant"?
- Questions to a reader: none.

**3. Where the protocol was unclear or did not fit**
1. "A claim that depends on a blocked claim is blocked" does not separate depending on a claim's measure from depending on its result. Both fig3e claims list the blocked fig3c-success-rate-constant only for the definition of the success rate. I tested them and said so in their notes.
2. "Reproduced under any reading" conflicts with fig3e-cluster-b's own rule to block when the readings of "similar" differ. I recorded reproduced, because one set of readings satisfies every part, and gave the result of every reading.
3. When an exact expected value (a session count) fails but the criterion's test passes, the protocol does not say what the outcome is. I chose partially_reproduced.
4. The criterion's movement-onset rule fires almost at once (baseline window ends at -0.5 s); the protocol has no way to flag a claims-file method that cannot discriminate. I recorded it in the notes and the authors' question.
5. Reading the raw image frames (needed for the full baseline-fluorescence reading and the pixel-map reading) does not fit the time limit. For the fluorescence I used 8 frames per session and recorded it as a deviation. I did not run the pixel-map reading, because the ROI reading already reproduces those claims; I recorded it as not run, not as a block.

**4. Runtime and failures**
- About 2 hours in total, of which three full notebook runs took about 18 to 20 minutes each.
- One development pass over all task sessions took 14 minutes.
- Nothing failed in the final run.
- The harness created an empty `entries/001425-kondo-2025/.claude/.cc-writes` folder. Removing it was denied (it needs approval, which this session cannot give), so it is still there and should be left out of the commit. The untracked dotfiles at the repository root (`.bashrc`, `.idea`, `scripts` and others) are not mine.
