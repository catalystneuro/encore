No outcome changed: all 21 match what the verifier gave in round 1. The entry passes `check` and ran from a clean environment in 541 s, and the final numbers match the run before it except for timings.

**What I added or corrected, by verifier point**
- **B1, Mouse12-120808 clock (hd-cell-fraction):** I re-ran that session with position realigned by the best shift of each quarter, which gives 13 HD cells. One constant shift of -2.6 s gives 12. The total becomes 391 (or 390), above the 388.3 bound. I kept partially reproduced, because the criterion counts the sessions as deposited. The conclusion and notes now say the count match is fragile.
- **B2/C, extra unit rows and electrode groups:** I added a data check of the unit rows:
  - Unit ids are 0 to N-1 with no shank or cluster number.
  - Every electrode group says only "shankN electrodes" with location "unknown".
  - 1826 rows fire at 0.05 Hz or more and 1526 at 0.5 Hz or more, so the paper's 1077 cells cannot be recovered from the files.
  
  The finding about the unit selection was updated to say this.
- **B3/B4, fig2f-sws-tenfold-faster:** I added three outputs:
  - **Reading (b):** median ratio 8.02.
  - **Fit quality:** median R² is 0.84 in waking, 0.55 in REM and 0.78 in SWS. Keeping only pairs with R² of at least 0.25 or 0.5 gives 8.46 and 8.56.
  - **Known-speed check:** Poisson surrogates driven by the measured head direction. The estimator returns 0.37 of the true waking speed, and for the trajectory played ten times faster it gives a median ratio of 4.99.
  
  So my estimator compresses ratios, and the 8.33 shortfall from tenfold may come from it. I kept partially reproduced, as the criterion decides on the data's ratio, and the text now says this. For the REM claim, reading (b) gives 0.85.
- **B5/B4, fig4b-noise-correlations:**
  - The lagged products now use only times where head direction is known at both ends of the lag. The main numbers barely moved.
  - Reading (b) gives the same signs.
  - Poisson surrogates, with tuning curves re-estimated from their own spikes, show a bias of +0.64 Hz² at 0° and -0.37 Hz² at 60°. That is about a tenth of the observed effect. The data still exceed the surrogates in 110 of 118 pairs at 0° and fall below them in 223 of 256 at 60°.
- **B6, decoding-tracks-hd:** Selecting HD cells on the training half alone keeps the same 28 sessions and the same 11.7° pooled median error.
- **B7, fig3a-packet-60-degrees:** The text now also says the reading (b) waking crossing, 54.1°, falls just outside the tolerance.
- **B9, blocked count:** Corrected to 13 blocked of 21 claims in the notebook, README, summary and findings.
- **ensemble-sizes:** I added HD cells per session by mouse group: 7.4 ± 6.2 in the mice that appear thalamus only, against the ADn's 8.4 ± 5.1. The claim stays blocked because the mouse assignment is not shown by the files.
- **Other:** The header now says which sections use random numbers, each with a fixed seed. The README runtime is now about nine minutes. The verification round is recorded in the attempt record for all 21 claims.

**Not done, and why**
- **fig3b-packet-coherence, pooled version:** Not run. The Methods do not say how the actual and expected packets are compared, or how the probability is formed from the 5,000 random waking vectors.
- **fig6b-adn-synchrony in the thalamus-only mice:** Not run. Without shanks, same-shank pairs cannot be removed, and spike sorting distorts their 1 to 5 ms synchrony. The mouse assignment is also unverified.

The record notes give both reasons.

The paper text I downloaded is in `paper/`. Nothing is committed. The stray untracked dotfiles at the repo root (.bashrc, .idea, `scripts` and others) were there before this run and are not mine.
