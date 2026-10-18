I've addressed all 14 problems and the 9 requested outputs. The entry re-ran cleanly with `python tools/entry.py all` in 798 s, `check` reports 0 errors, and nothing is committed.

**Outcome change**
- **behavior-rt-mt** goes from partially reproduced to reproduced. The verifier pointed out (problem 7) that the reaction-time ANOVA used all 250 pre-MPTP files, including M1, SMA and VLp-only files that are not part of the paper's data. Restricted to the 165 files that hold the GPi/VLa units analysed, reaction times differ neither between animals (p = 0.89) nor between directions (p = 0.41). Movement durations keep both effects. With the paper's own files the animal effect is p = 0.053. The all-files result stays as a variant, and the change is recorded as a deviation.
- The verifier agreed with the other 20 outcomes, and they are unchanged. Counts are now 7 reproduced, 4 partially reproduced, 7 not reproduced, 3 blocked.

**What I added to the notebook**
- **Chance level of the response detection**, measured on the real data with every trial aligned to a random time:
  - 62% of GPi and 71% of VLa units come out responsive by chance, against 98.5% and 97.5% in the data.
  - The hold-period slope test finds a slope in 98 to 99% of units by chance, the same as in the data. The hold-period-ramps notes now say those fractions do not separate ramps from noise. The test is the paper's own.
  - Many VLa decreases may be false positives, which is noted under fig3c.
- **One record per presumed neuron** for every claim, merging units with the same day, channel and sort letter. This merge also joins some units the paper kept apart (47 of the 117 multi-file groups). Onset and slope tests are also shown with one value per neuron. Fig3b keeps its lag, but its GPi median leaves the tolerance, so the notes now call that match fragile.
- **CCF (fig4-ccf-rare)**: an approximate c0 ≤ 0.3 exclusion as a variant, since the paper's simulation is not in its deposit. It gives KS p = 0.003, 0.333 and 0.025. I also added the lags of the significant peaks and the count of identical spike times, which matches chance, so shared artefacts do not explain the result. Spike times turn out to be at sample resolution in every file, so the verifier's binning concern (problem 8) does not apply.
- **Noise correlations**: a drift check, detrended correlations and per-pair-target bands. The excess over shuffled controls remains in all of them.
- **Fig 5**:
  - `Fig5_S14.m` holds no burst detector; it only plots stored averages. I added its band computation as a variant, which also shows no decrease.
  - The per-pair test is at chance here (about 47% of shifted controls cross).
  - Burst durations with log10 (254 ms) are now shown, not only mentioned.
- **Smaller items**: AP-width edge cases (one zero width, nine capped, 15 not measured), a check that no file repeats a channel id, a one-sided p for fig3a, and a rate-criterion variant.
- **Fig 1 proxy** from the electrode coordinates. VLa-labelled electrodes lie anterior of VLp-labelled ones but, by the files' stated convention, ventral of them, where the paper says dorsal. I recorded this as a new `metadata_insufficient` finding. The claim stays blocked.

**Other files**
- `gpivla.py`: reads the electrode coordinates, returns the CCF peak lag, adds the c0 approximation, and gains a log-base option for bursts and pauses and a flag for capped widths.
- The conclusions, summary, README, entry runtime (now 13 min), attempt notes and deviations all match the new numbers. Round 1 is recorded under `verifications`.
- The paper's text is saved under `paper/`.

**Not done**
- fig4 keeps the main pair set the claims file fixed before the analysis. The c0 exclusion is only a variant, so it does not decide the outcome.
- I did not refine the merge rule that over-merges; its limit is stated in the notebook and notes.
- I left the untracked dotfiles in the repository root (`.bashrc`, `.idea`, `scripts` and others). They were there before this run and should not be committed.
