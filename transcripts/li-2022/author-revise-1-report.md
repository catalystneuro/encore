I've addressed every point in the round-1 report and re-run the entry with `python tools/entry.py all`. It passed in 19 minutes, and the entry check reports 0 errors. A second run gave identical numbers. Nothing is committed.

## What changed in the outcomes
| Claim | Before | Now | Why |
|---|---|---|---|
| fig3k (sucrose response rises) | not_reproduced | **partially_reproduced** (rests on an assumption) | Printing the regression coefficients, as the verifier asked, exposed a bug: in Mouse6's late sucrose session the LED labels shift by one frame partway through while the data keep their order. The 470 nm channel had been read from the constant third frame type. Channels now come from the frame order. With all trials, AUC +3.53, t(4) = 5.74, p = 0.0046, 5 of 5 mice up, inside the paper's CI. With the first 16 trials, p = 0.093. So p < 0.05 holds in 2 of the criterion's 4 readings. |
| fig4-recording-count | not_reproduced | **partially_reproduced** | As the verifier said: 31 mice is within tolerance, 1739 or 1902 units is not. |
| fig4c (photoidentification) | blocked | **not_reproduced** | I applied the fake-session test, with block 1 as the fake one as the Methods order them, plus the reverse order and mixed orders as readings. The total tagged is 91 to 256 under every reading. Both projection counts can be within 10% only if the total is 63.9 to 78.1, so the missing projection labels don't matter. |
| fig5dh (behavior clusters) | blocked | **partially_reproduced** (rests on an assumption) | A fitted linear clock (offset plus rate factor) aligns the pose in 21 of 29 sessions. In 20 of them the factor is about 0.988, which looks like a frame rate about 1.2% slow. Under the adopted reading (features z-scored, t-SNE defaults of the paper's 2020 era), sucrose gives 7 clusters in 3 of 5 seeds and shock gives 5 in only 1 of 5. Read literally (raw features, current scikit-learn defaults), the criterion is met for all seeds. The other readings give 3 to 9 clusters. |

fig3l, the early-dip claim and fig4d keep their outcomes. All 32 blocked claims stay blocked. The notebook, README and summary had fig2c listed as data_missing; the record already said metadata_insufficient, and they now match it.

## What I added or corrected
- **New outputs the verifier asked for:**
  - every text field of the 31 files, the units and electrodes columns, and the archive's subject metadata; none holds a group or projection label
  - the photometry regression slope, intercept and correlation for every session, plus a variant fitted on the pooled baseline bins
  - tagged counts under each fake-block order
  - the per-session pose clock fit with its leftover lags
  - frame count, rate and duration of all 32 videos, read from their headers without downloading them
  - for fig4d: the largest share of one mouse in each cluster, and the counts without H22, H27, H34 and H39
- **Text fixes:** the regression direction (470 nm on 415 nm), the paper's airpuff effect (−3.657), and the cue-spacing claim (Mouse1's early airpuff session ends with irregular cues).
- **Question for a reader:** in `questions/000689.yaml`, whether a mean over 2 to 7 s can test a "transient" dip. The lowest point of the trace is below zero for both outcomes (−1.09 and −0.63) even though the airpuff window mean is +0.11. The claim was not changed.
- **Attempt record:**
  - new notes and deviations for each changed claim
  - updated findings: pose clock, the photometry label shift, the light blocks, and the data-missing count corrected to 19
  - two new questions for the paper's authors: which z-score baseline was used, and the feature scaling and t-SNE settings
  - round 1 recorded under `verifications`
- **Dependencies:** added `scikit-learn`, `tsfresh` and `av`, and re-locked. `runtime_minutes` is now 20.

## What I did not do
- **MATLAB smoothing window (fig4d):** I couldn't print the window that "smoothing factor 0.85" produces, because MATLAB can't be installed in the locked environment. It stays a question for the paper's authors.
- **tsfresh 0.16.0:** it doesn't install on Python 3.13, so I used 0.21.2 and recorded that as a deviation.
- **Stray files:** untracked dotfiles in the checkout (`.bashrc`, `.vscode` and others) are not mine. I left them alone.
