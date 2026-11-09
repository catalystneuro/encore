One outcome changed (ed1-fast-spiking-properties is now not reproduced), and I added every output the verifier asked for. The re-run with `python tools/entry.py all entries/000010-li-2015` passed with 0 errors in 1,200 s, and the conclusions match the new numbers. Round 1 is recorded under `verifications` for all 27 claims. Nothing is committed.

**Outcomes:** 8 reproduced, 4 partially reproduced, 4 not reproduced, 11 blocked.
- **ed1-fast-spiking-properties:** changed from partially reproduced to not reproduced, as the verifier said. The criterion requires both parts under every reading. Fast-spiking neurons do have higher baseline rates, but they are more selective than pyramidal neurons under both readings, not less.
- **imaging-selectivity-counts:** kept as partially reproduced; the disagreement is recorded.
  - Four of the five values match under several readings, and the fifth misses by half a cell (1,417 selective cells against a lower limit of 1,417.5).
  - The selective count is below tolerance with one reading (1,315 to 1,417) and above it with the other (1,844 to 1,957), so the paper's 1,575 lies between them.
- **fig2e-no-contra-bias-spikes:** kept as reproduced. The protocol judges a claim of absence on the paper's test as written ("the overall spike count across the recorded population"), which gives P = 0.82. The text now says the result is fragile: in the 570 ms window before the go cue, all four tests give P = 0.022 to 0.050 with a contralateral excess.
- **All other claims:** unchanged, and the verifier agreed with them.

**Added outputs:**
- **Light balance (fig3f-pt-contra-preferring):** the tagging light is balanced between trial types. It falls in 0.295 of lick-right and 0.307 of lick-left correct trials, and only 4 of 75 sessions show an association, against 3.8 expected by chance. Within the light and no-light trials taken separately, PT neurons are contra-preferring in 26 of 45 each. So the result with the light trials kept is not a bias from the light; it reaches P < 0.05 only with all trials pooled. The outcome stays reproduced.
- **Imaging baselines:** F0 is at or below 0 in only 145 of 305,349 included ROI-trials. Leaving out ROI-trials with F0 near 0 gives 1,416 to 1,419 selective cells in the closest reading. One cut (F0 below a tenth of the ROI's median fluorescence) puts all five values in tolerance. I chose those cuts, so they are shown but decide nothing.
- **Plane depth (fig4h):** I searched every text field and attribute of the 59 imaging files and found no mention of depth, microns or layer. The claim stays blocked.
- **Placeholder trials:** broken down by mouse. 1,502 of 1,540 are in sessions with tagging light, mostly in the first or last tenth of a session, and only 7 are in the Ai32 mouse 218693. So they are not the missing photoactivation trials.
- **Behaviour:** applying the same 2.6 s timing filter used in the other claims drops 103 trials and gives the same outcome (75.8% correct, 11.7% early licks over sessions).
- **fig2d-preparatory-perimovement:** the class totals are now printed: 628 preparatory against the paper's 523, and 681 peri-movement against 693.

**Text corrections:** for the population-dynamics bin choice, the spatial shuffle that mixes planes (28 of 32 within-plane rows still give P < 0.05), the reaction-time reading that only detects rises, and the antidromic window and peak width I chose. Two findings are corrected:
- The `included` flag does have a one-line description.
- The placeholder trials are not the photoactivation trials.

The README, `entry.yaml` (runtime now 20 minutes) and the run link in the record are updated.

**Not done:**
- Early-lick trials cannot be removed from the imaging analyses, because the imaging files hold no lick events.
- Whether `lick_trace` is the photodiode signal still cannot be confirmed from the files.
- The values shown only in figures were not read, as the claims file notes.
