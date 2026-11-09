I've done steps 1 to 6. The entry is locked, passes `check` with 0 errors, runs from a clean environment in 233 s, and the verifier's package is in `executed/000041-watson-2016/handover/`. Of 39 claims, 8 are reproduced, 9 partially reproduced, 15 not reproduced and 7 blocked. Nothing is committed.

**Text and version used.** I used the full text of the NIH author manuscript (PMC4873379), which is free to read but not under an open licence. The supplement could not be downloaded: PMC and Cell answer with a browser check. Table 1 is not in the manuscript. The pinned version is 0.250624.0419. The paper cites no dandiset version, and the two published versions hold the same 22 files; they differ only in metadata, so I pinned the most recent and said so in the notebook header.

### (1) Outcomes per claim

| Claim | Outcome |
|---|---|
| dataset-composition | not reproduced |
| fig2a-median-rates | partially (all three pE medians match; the pI medians are low) |
| fig2a-skewed-wide-distribution | partially |
| fig2a-fraction-above-2hz | not reproduced (direction right, p = 3.5e-06, short of the paper's p < 1e-10) |
| fig2b-wake-nrem-slope | reproduced |
| fig2-burst-index-by-state | partially |
| fig2c-acg-peaks | partially (the 8 ms peak is there; no theta peak found) |
| fig2c-acg-decay | blocked, methods underspecified |
| fig2f-rate-group-correlations | partially |
| ma-statistics | not reproduced |
| ma-fraction-over-nrem-episodes | partially |
| packet-duration | reproduced (median 108 s) |
| wake-sleep-cycles | not reproduced |
| fig3b-population-decline | partially |
| fig3-first-last-packet | reproduced (last-packet mean 0.9679 against a bound of 0.968) |
| fig3d-first-last-slope | reproduced, but a split-half check gives the same slope, so regression to the mean can explain it |
| fig3e-wake-before-after | partially |
| fig3b-sextiles-over-sleep | reproduced |
| fig3b-cv-over-sleep | not reproduced |
| fig4iv-sextiles-within-nrem | reproduced (small effects, varying by subject) |
| fig4v-cv-within-nrem, fig4vi-burst-within-nrem | not reproduced |
| fig4i-band-power-within-nrem | not reproduced |
| fig4-delta-packet-length | reproduced |
| fig4cd-packet-rate-lfp | partially |
| fig5b, all four triplet claims | not reproduced |
| fig5c-rem-duration, fig5c-sigma-ma | not reproduced |
| fig5c-delta-change | reproduced |
| figs5-within-wake-rem | not reproduced |
| fig5c-wake-movement | blocked, data missing |
| UP/DOWN-state and spindle claims (5) | blocked, methods underspecified |

### (2) What was found about the dandiset
- **Missing data:** it holds 22 sessions from 10 rats and 945 units. The paper, and the dandiset's own description, report 27 sessions, 11 rats, 995 putative pyramidal cells and 126 interneurons.
- **Dino-072114:** the spike times are whole seconds divided by 20000. The conversion code set a 20 kHz rate on this one session. Its spikes are unusable, so I excluded the session.
- **Dino-061914:** the LFP is scrambled. It has 125 columns for 128 electrodes and runs 40 min longer than the spikes, and its sample-to-sample correlation is 0.28 against 0.99 elsewhere. I kept the session's spikes and dropped its LFP.
- **No microarousal label:** the state table has only Awake, Non-REM and REM. I derived microarousals from short Awake epochs between Non-REM epochs. They come out at about half the paper's count (391 in 21 sessions against 790 in 27).
- **The state scoring may not be the paper's:**
  - It gives 30 wake-then-sleep cycles in 21 sessions, and 3 sessions have none, although the paper kept only sessions that had one.
  - Only 49 of 534 REM epochs are followed directly by Non-REM, so the REM triplet claims rest on 17 triplets.
  - The dandiset does not say how the states were scored.
- **Metadata problems:**
  - The LFP has unit "volts" but a NaN conversion factor, so it cannot be put in volts.
  - Every electrode location is "unknown".
  - 23 units have cell type "unknown" with no description.
  - The description's counts and age range do not match the files.
- **Clocks:** the state labels agree with the spikes in 20 of 21 sessions, and the LFP agrees to within 50 ms in 14 of 21.

### (3) Where the protocol was unclear, wrong or missing something
1. "Open access" is not defined. I treated a free-to-read author manuscript as full text.
2. There is no rule for when the main text is available but the supplement is not. I blocked the claims whose methods are only in the supplement as `methods_underspecified`, although that reason is defined as "neither the paper nor its code fixes the procedure".
3. Neither the paper nor the dandiset links any code. The protocol does not say whether to search for some. I read the NWB conversion code (catalystneuro/buzsaki-lab-to-nwb at 5f6a375) and recorded the commit; it explained both corrupt files.
4. The prescribed clock check (decoding labels shifted in time) is coarse when states last minutes, and it does not apply to LFP, which has no labels. I used a contrast against shifts of ±5 to ±300 s for the labels and a spike-LFP cross-correlation for the LFP, and set my own pass thresholds.
5. There is no guidance on a label the paper uses but the dandiset lacks. I derived microarousals and recorded this as both a deviation and a finding.
6. Session-level corruption inside an otherwise usable dandiset is not covered. I excluded the affected data and recorded findings.
7. The 10% default tolerance is not meaningful for correlation coefficients that depend on binning the paper does not give, so I judged those on sign and significance and stated why. Separately, fixed p-value thresholds become stricter with fewer cells, which made fig2a-fraction-above-2hz "not reproduced" although the effect is there.
8. The `measured` rule covers only the case where some reading matches. When none did, I recorded the first reading listed.
9. A check can show a criterion is not diagnostic (the fig3d slope), but the protocol gives no way to act on that. I kept the outcome the criterion gives and said so in the notes.
10. I found the scrambled Dino-061914 LFP after the criteria were written and after seeing some LFP results. The protocol does not say how to handle that. I recorded the exclusion as a deviation on each claim that uses LFP.

### (4) Runtime and failures
- The notebook takes 233 s in a clean environment; about two minutes of that is streaming the files in 6 parallel processes.
- The final run had no failures.
- Earlier failures:
  - Europe PMC's full-text endpoint returned a server error.
  - PMC and Cell blocked the HTML and supplement downloads with a browser check.
  - GitHub code search needs authentication, so I found the conversion code through the repository tree instead.
- The sandbox mounted about 10 dotfiles and `scripts` at the repository root as `/dev/null` devices, so they show as untracked. They are not real files and git will not add them.
