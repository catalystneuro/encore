I've addressed every point in the verifier's report. No outcome changed: the verifier's outcome matched the record on all 18 claims, and the new analyses are variants that the claims file's criteria don't use. The final `python tools/entry.py all` run passes: the main notebook takes 6.6 minutes and the new one 21 minutes. Nothing is committed.

**Outcomes:** 3 reproduced (fig1c, fig2bc, fig2ef), 2 not reproduced (fig1e, fig3b), 2 partially reproduced (fig4c, fig4cd), 11 blocked for missing data.

**Added in reply to the report**
- **fig1e:** 149 of 899 movement onsets fall at or before the stimulus and 346 within 0.08 s after it. Measured as stimulus onset to choice registration, the response time is shorter at higher contrast (rho -0.134, p = 5.2e-05). The outcome stays, because the criterion and the paper's "time to first movement" use the movement onset. The text now says the result depends on these fast onsets.
- **fig2ef:** I added a bootstrap over switches: B is above A in every draw, tau's 95% interval is 6.4 to 38.4 trials, and tau is 40 or more in 1.8% of draws. A single-trial maximum-likelihood fit gives the same values as the original fit.
- **fig3b:** I added a test on the 27 trials with no movement before 0.4 s, using a brain mask taken from the mean image. On these trials the difference at the all-trial masked peaks points the same way (p = 0.02 and 0.091). But searching for peaks on these trials alone puts them on the opposite sides. I also added time courses aligned to stimulus and to movement onset. The conclusion now says the variants do not show the lateralization is visual.
- **Encoding model:**
  - The intercept-only model now has only the time-point columns. Full minus intercept is 0.123, 0.133 and 0.078 under the three readings.
  - Folds now have a variant that keeps each trial's frames together and uses each frame once. Full cvR2 drops to 0.422, 0.363 and 0.047. Movement ΔR² over components becomes -0.005 against 0.017 for task, which the criterion would count as not reproduced. This is recorded in the notes; the outcome stays because the criterion's design uses the lab's (chiCa) folds.
  - Also added: reading (b) over brain pixels only (0.434), and the spread of ridge penalties (none at either end of the grid for the full model).
- **Side cameras:** a second notebook, `encoding_all_cameras.ipynb`, adds the left and right camera video components, as the paper does.
  - Full cvR2 is then 0.574 and 0.525 under readings (a) and (b), inside the claimed range.
  - With trial-grouped folds it falls to 0.472 and 0.405, back below the range.
  - Movement ΔR² is 0.22, still below 0.297.
  - The outcome stays, because the claims file fixed the body-camera-only design.
- **ROI check:** the data check compares each motion-energy region against the camera's nose-tip and pupil positions. They agree with whisker pads and body.

**Corrected**
- "Twelve" blocked claims is now "eleven" in the README and the finding.
- The helper now reduces video frames by area averaging, which is twice as fast. The main notebook's numbers changed by at most 0.0001.
- The attempt record has updated notes and the round-1 `verifications` entry.

**Not done**
- I couldn't compare the reaction-time distribution with the paper's Figure 1E, or check the paper's methods text. bioRxiv refused requests from this host (error 1015), so nothing was saved under `paper/`.
- The action-kernel form of the subjective prior is still an assumption and is recorded as one.
