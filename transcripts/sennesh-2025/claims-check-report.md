I checked the 37 claims and corrected 12 of them. The file is ready for an attempt.

**Checker result:** `claims/sennesh-2025.yaml: 37 claims, 37 quotes, 19 statistical values, 0 problems` (same result before and after my edits).

**Changes, by claim:**
- **fig2e-dd-alphabeta-laminar:** the expected values were 1.75 ± 0.45 and 1.3 ± 0.4, which don't match the criterion's own ranges. They are now 1.775 ± 0.425 and 1.275 ± 0.375.
- **fig4c-ssa-v1-contrast:** same kind of error. The expected values are now −1.05 ± 0.6 and 1.275 ± 0.375, from the paper's 0.5–1.5 and 1–1.5 dB ranges widened by 10%.
- **fig2ab-dd-condition-spectra:** I removed the expected value 5 ± 0.5 dB. The legend says "over 5 dB", so the entry wrongly capped it at 5.5 dB; the criterion keeps the 4.5 dB lower bound. The 150 ms, 250 ms and 1 dB bounds are now labelled as choices made here.
- **fig2d-dd-gamma-laminar:** the statement said "L1 to L2/3". The quoted text says layers 1–4 and the legend says the L1 and L2/3 boundary, so the statement now gives both.
- **dd-gamma-peak-frequency-lm:** "(35 against 41 Hz)" read as oddball against control, the reverse of the criterion's reading. It now says "control 35 Hz, oddball 41 Hz".
- **dd-aperiodic-no-difference** (and **suppfig1-aperiodic-no-difference-all**, which uses its test): the main test used the code's choices, a 20 ms window margin and a FOOOF fit over 2 to 150 Hz. The protocol puts the paper first, so the main test now uses the paper's 50 ms margin (Results) and its 2 to 90 Hz range (Methods). The code's choices become a variant.
- **dd-gamma-peak-frequency-v1:** the window and FOOOF range now have two readings: the paper's text and the code's. The six claims that reuse these spectra inherit both.
- **suppfig2-alphabeta-peaks:** the source pointed at paragraph 4; the quoted passage is paragraph 3.
- **suppfig3-fastsweep-aperiodic:** the criterion said the Results list different areas from the legend. They agree, except one sentence in the SSA section.
- **trial-counts, fig2f, fig3ab, fig3c, fig3d, suppfig4-pupil:** thresholds and windows the paper doesn't give are now labelled as choices made here.
- **fig5-l23-gamma-by-area:** added a note that another notebook writes a bar plot under the same file name, but it is not the figure the legend describes.

**Code check:** I read the linked code at commit cee2e6f. The windows, bands, tests, Figure 5 averaging and trough-locked CSD settings the criteria cite all match it. There is no pupil analysis in the code. The one disagreement with the paper is the FOOOF fitting range (2 to 150 Hz in the code, 2 to 90 Hz in the Methods), which I handled as above.

**Coverage:** every main finding has a claim, and all claims come from this paper.

**Still open (recorded under `checks`):**
- The grading counts (such as 11 of 13) and the rules for partial reproduction are the claim writer's choices; the paper gives no basis for them.
- The rule for calling a CSD pattern feedforward or feedback (the order of the first sinks) is also a choice made here. The paper judges these patterns by eye.

Only `claims/sennesh-2025.yaml` was changed, and nothing was committed or pushed.
