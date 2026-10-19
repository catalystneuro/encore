**Verification report, round 2: Davatolhagh et al. 2025 (doi:10.1101/2025.09.12.675910) on DANDI 001712 (draft)**

The claims file lists 18 claims. The attempt record gives 18 outcomes: 3 reproduced (fig1c, fig2bc, fig2ef), 2 not reproduced (fig1e, fig3b), 2 partially reproduced (fig4c, fig4cd) and 11 blocked by missing data. bioRxiv again refused every request from this host (HTTP 429, error 1015), and Europe PMC has no full text (HTTP 500), so nothing is saved under `paper/`. I queried the dandiset's metadata from the DANDI API but downloaded no data.

### 1. Outcomes

I agree with all 18 stated outcomes.

- **fig1c, fig2bc, fig2ef (reproduced).** Agree. For fig2ef, the switch bootstrap (cell 29) supports the criterion: B > A in every draw, and tau ≥ 40 in only 0.018 of draws.
- **fig1e (not reproduced).** Agree under the criterion. In cell 20, rho is -0.053 with p = 0.15. The result depends on the reaction-time floor: p = 0.068 above 0.08 s and p = 0.00062 above 0.15 s. Response time is significant (p = 5.2e-05).
- **fig3b (not reproduced).** Agree. The criterion's peaks are frame corners (cell 33). In the masked variant the peaks are lateralized (cell 34). On the 27 slow trials, however, the masked search puts the peaks on the reverse sides (cell 35). So a visual lateralization is not shown.
- **fig4c (partially reproduced).** Agree. In cell 41, reading (a) is 0.471: above 0.3 but outside 0.486–0.660.
- **fig4cd (partially reproduced).** Agree. In cell 45, movement ΔR² exceeds task ΔR² under every reading (0.104/0.119/0.067 against 0.017/0.015/0.013), and none is in 0.297–0.440.
- **The 11 blocked claims.** Agree. There is one subject and no genotype (cell 3).

### 2. Text against outputs

Nearly every sentence matches the printed outputs. These are the exceptions:

- **Cell 43:** "Three variants do not change the outcome." Four variants follow: masked pixels, trial folds, all cameras, and no body video. This is a wording slip.
- **Attempt record, fig4c notes:** "Over brain pixels (the mask of the fig3b variant) reading (b) is 0.434." The mask is a brightness and margin heuristic (cell 34), not a brain mask. Cell 43 describes it correctly as "the masked pixels of the fig3b variant".
- **Attempt record, fig1e notes:** "161 trials have no movement onset after the stimulus (151 of 899 onsets precede the go cue)." Both numbers are correct, but the 161 is 149 onsets at or before the stimulus plus 12 trials with no onset (cell 20). The 151 counts onsets before the go cue (cell 5), so the parenthesis reads as if it explained the 161.
- **Not backed by any printed output:**
  - Cell 4, the Summary (cell 47) and a finding name "CNTNALP2" in the dandiset's keywords. The notebook prints only the file's keywords. I checked the DANDI API: the draft's keywords and description both say CNTNALP2, so the statement is true.
  - The Summary's "one of the 17 sessions the conversion code lists for 19 mice".
  - The record's openalyx "empty genotype list".
  - Cell 10's "the IBL places its side-camera ROI on the whisker pad".
  - The paper_inconsistency finding, which I cannot check without the paper.
- **README:** consistent with both notebooks. The main notebook ran in 6.5 min, 101 s of it on the body video. The all-cameras notebook ran in 20.7 min, about 15.6 min of it decoding video.
- **Summary (cell 47):** "within 0.08 s of the stimulus or before it on more than half of the trials" holds: 495 of 899 onsets (cell 20).

**My round-1 reasons in the record:** they are restated faithfully and in substance. Two small omissions:
- The fig4c reason lists B5–B7 without my tag that they did not affect a conclusion.
- The fig2ef reason drops the 9-trial last block.

Neither misstates what I said.

### 3. Round-1 points

**Resolved:**
- **B1 (fig3b):** the mask is now fixed from the mean image, and the slow-trial search and movement-aligned time courses are added. The conclusion now says the response is not shown to be visual.
- **B2 (fig1e):** onset counts, histograms and the response-time variant are added.
- **B3 (fig2ef):** a switch bootstrap and a single-trial maximum-likelihood fit are added.
- **B4 (fig4c, fig4cd):** the all-cameras notebook adds the side-camera video components.
- **B5:** the trial-fold variant with duplicate frames removed is added.
- **B6:** reading (b) is now also given over masked pixels.
- **B7:** the intercept-only model is now the time-point columns alone.
- **B8:** the metadata problems are recorded as findings.
- **B9:** partly resolved. The ROI positions are now checked against the nose tip and pupil. The action-kernel prior is still an assumption.
- **Requested outputs:** the penalty distribution (none at either end of the grid for the full model) and the bootstrap intervals.

**Remaining issues that bear on a conclusion:**

1. **B5 matters more than I said in round 1.**
   - With the body camera only and trial folds, reading (c) gives a movement ΔR² of -0.005 against 0.012 for task (cell 45). Under the criterion that would make fig4cd not reproduced.
   - With all three cameras and trial folds, movement exceeds task under every reading (0.109/0.115/0.008 against 0.008/0.008/0.000). Under that design, partially reproduced is the robust outcome.
2. **fig4c depends on fixed choices.**
   - With all three cameras, (a) 0.574 and (b) 0.525 fall in the range, so the claim would be reproduced, but only with the chiCa folds, which share frames of a trial between training and test. With trial folds the values are 0.472/0.405 (encoding_all_cameras cell 6).
   - The outcome therefore rests on the claims file's choice, made for runtime, to use the body camera only.
   - The paper's legend says "with trial time regressor subtracted out". If its 0.54–0.60 are intercept-subtracted, the comparable values here are 0.12–0.13 with the body camera and 0.16–0.24 with all cameras, far below the range. Without the paper I cannot tell which reading it uses.
3. **fig3b:** the reversal on slow trials (columns 550 and 72) is unexplained. The 0.4 s exclusion uses wheel onset only, so paw and whisker movements are not excluded. The lateralization seen on all trials cannot yet be attributed to the stimulus.
4. **fig1e:** the outcome depends on how the trial table's movement onset treats anticipatory movements. The paper's reaction-time definition and its Figure 1E distribution still cannot be checked.
5. **Paper text:** neither the author nor I could read it from this host. The encoding windows, the cvR2 reading and the Figure 3B window all still rest on the claims file's account of the paper.
