The claims file needed corrections and five missing findings. Both are now done, and I've marked it ready for an attempt. Nothing is committed.

**Checker result:**
- Before my changes: `claims/masset-2025.yaml: 23 claims, 23 quotes, 26 statistical values, 0 problems`
- After: `claims/masset-2025.yaml: 28 claims, 28 quotes, 44 statistical values, 0 problems`. The YAML also loads cleanly.

I downloaded the paper's MATLAB scripts from Mendeley and the simulation repository at commit 37f11c6, and checked the cited code details against them.

**Changes, by claim:**
- **M4, the shared decoding method:** the subtracted baseline followed the code, which takes it from the half that gives the discount factors. The Methods take it from the same half as the responses. The Methods are now the main reading and the code a variant. This affects every decoding claim.
- **ed2e-branching-myopic-bias:** the source said paragraph 3; the quoted sentences are in paragraph 4.
- **ed2-myopic-bias-maze-lunar:** the paper never says where "close to" and "far from" the landing site divide. The code splits at the median lander height, now cited. I also noted that the Methods say 10,000 sets of trajectories and the figure legend says 300.
- **session-trial-counts:** the Methods count sessions "in which neurons were recorded". That can mean any recorded dopamine neuron or only analysed ones, so both are now readings.
- **fig2b-anticipatory-licking:** the source paragraph was wrong (it is paragraph 2). The averaging now follows the legend and code: one lick average per recorded neuron, then averaged over neurons. Whether that means the 78 recorded or the 50 analysed neurons is open, so both are run.
- **fig2c-mean-cue-response-decreases:** the inset uses the 0 to 0.5 s window, not the 0.1 to 0.4 s window of later analyses. Both are readings.
- **fig2k-reward-timing-decoded:** I removed a made-up requirement that the median decoded time rise with delay. The paper judges decoding only by the Wasserstein test against shuffle.
- **fig3-common-value-fit:** the convexity rule and the "spread over 0.2 to 0.8" rule were not from the paper. Convexity is now named as open with two readings. The partial-success rule now uses the 20th, 70th and 90th percentiles the Methods report (0.25, 0.56, 0.88).
- **ed5-behavioral-neural-discount-uncorrelated:** the neurons per mouse were unstated. The code's set skips the 2 spikes/s cut, so the selected set and the code's set are both readings.
- **Added five claims**, each a finding stated in the Results that had no claim:
  - ed5g: decoding in single mice
  - ed6g: decoding is comparable to simulated data
  - ed7de: gain and baseline are not related to medio-lateral position
  - ed8cd: VR licking is not related to the discount factor
  - ed8ej: single-mouse VR fits match the full fit

**Still open (recorded under `checks`):**
- The cued delay exclusion counts don't add up: 17 + 11 + 4 removed does not give 78 minus 50, and the Extended Data give 23 and 13.
- `DecodeTime` is not in the code deposit, so the number of singular components in the main decoder keeps two readings.
- The mixing model's sharing parameter is lost from the text and its code is not deposited, so `mixing-model-accuracy` cannot be run as published.
- In ed8ej the printed p-values look inconsistent with the r values. The claim reports p but does not compare it.
- A few robustness panels have no claim (Extended Data Fig. 5h-i, 3g-j, 6b), since the Results don't state them as findings.

**Ready:** yes. The last check says `ready: true`.
