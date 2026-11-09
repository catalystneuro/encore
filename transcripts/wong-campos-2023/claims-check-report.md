The claims file is ready for an attempt. I made seven changes to it and left two problems open, both recorded in the file.

**Checker result**
- Before my changes: `18 claims, 18 quotes, 0 statistical values, 0 problems`.
- After: `19 claims, 19 quotes, 4 statistical values, 2 problems`. The two problems are the lower bounds of the confidence intervals I added (212 μm and 0.07 m/s). The checker can't find them because the paper prints the intervals as "± 30" and "± 0.02". I confirmed both by reading. The schema validates and all quotes match word for word.

**Changes, by claim**
- **fig2e-half-amplitude-distance**: added the paper's 95% confidence interval for the 50% decay distance (242 ± 30 μm, recorded as 212 to 272) under `statistics`. The file had left it out.
- **fig2f-conduction-speed**: added the paper's 95% confidence interval for conduction speed (0.09 ± 0.02 m/s, recorded as 0.07 to 0.11) under `statistics`, for the same reason.
- **figs11-dendritic-spikes-rare**:
  - The criterion accepted 1 to 3 trials but the expected count had tolerance 0; it now requires exactly 2.
  - It names two readings of what the 40 trials are: all strong stimuli (Fig. S11e shows ones that evoked only subthreshold events), or only the trials with a spike.
  - It now tests the "usually corresponded to bAPs" part of the statement.
  - It says the 10 ms window is not in the paper.
- **fig4d-accelerating-amplifies**: added a third reading taken from the Methods' wording (the normalized amplitude of the third spike, compared with the compartment mean). The paper does not say which quantity its signed-rank test pairs.
- **fig4fg-opto-first-bap-attenuated**: the paper says the first bAP is attenuated "relative to the soma", but the criterion never compared with the soma. I added a reading based on the dendrite-to-soma amplitude ratio. I also noted that Fig. 4g shows one neuron (10 trials), and that the 150 ms window is not in the paper.
- **fig4ijk-sensory-first-fails**: the paper says all detected dendritic spikes start as bAPs from the soma. The criterion only checked the first spike; it now requires every detected dendritic spike to follow a somatic spike. I also marked "9 of 13 trials" as a bound the paper does not give.
- **figs12-spontaneous-failures-both-states** (new claim): the Fig. S12 finding, spontaneous bAP failures in both anesthetized and awake recordings, had no claim.

**What remains open**
- **fig2c-no-trial-variation**: the paper says "at any of the recording sites" but defines no measure or test. The bounds in the criterion (90% of sites, 1.5 times the baseline variation, failures under 10%) are not from the paper.
- **Several claims**: these parts are not in the paper; each criterion names them as readings or bounds:
  - the spike detection thresholds (5 and 4 robust standard deviations);
  - the bAP amplitude windows (0 to 5 and 0 to 8 ms);
  - the bounds standing in for "most" and "typically".
- **Figs. 3i, 4d and 4h**: no PDF was available, so the distance and time bins and the p-values printed only inside these figures could not be read.

All other claims match the paper. Every main finding has a claim, and none draws on another paper. Nothing was committed or pushed.
