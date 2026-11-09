I've finished the round-1 revision. The entry passes `python tools/entry.py all entries/000233-tingley-2021` (0 errors, notebook ran in 373 s), and every conclusion now matches the outputs of that run. Nothing is committed.

**Outcome changes**
- **edfig1-glucose-rhythm**: changed from partially_reproduced to not_reproduced, as the verifier gave. Neither part of the criterion holds. I added the 12 fit variants it asked for (three fit axes, two fit ranges, 24-h and 12-h segments); none puts the peak in 54–66 min or keeps the residual positive over 15–90 min.
- **edfig9-dorsal-ventral**: still blocked, but `blocked_by` is now data_missing (was other), as the verifier gave.
- **edfig1-glucose-circadian-meals**: kept as blocked, with the disagreement recorded (the verifier gave not_reproduced). Both expected values are about meals, which can't be tested. The circadian half fails only under the criterion's pooled test; a new within-rat variant finds hour of day significant (ANOVA p = 0.024, Friedman p = 5.2e-05).
- All other outcomes are unchanged. edfig5 (partially reproduced) rests on new numbers, below.

**Fixes and added output**
- **edfig5**: rate is no longer filled across stretches without recording. Both signals are filtered only where both exist, with 100 shuffles per rat instead of 20, the hours used per rat printed, and a circular-shift null for the Rayleigh test.
  - With stretches of at least 12 h (16 rats) or 6 h, both tests pass (power-power p = 0.021, Rayleigh p = 3.2e-09), but the comodulogram peak is on the diagonal, so the outcome stays partially reproduced.
  - With 24-h stretches only 3 rats remain and neither test passes; the record says so.
- **fig2**: the record now states that the match is fragile. Only one combination still passes with at least 6 h per rat, and "R negative in most rats" holds by construction. It also says CNO days and stimulation periods can't be excluded because neither is labelled. Added per-rat lags and the median lag for each combination.
- **edfig2**: added start-to-start, stop-to-stop and stop-to-next-start intervals. The stop-to-next-start gap bottoms out at exactly 20.0 ms in 19 of 22 rats. That matches the detector's merging of neighbouring events (Methods), so the paper's "20-ms refractory period" may be that rule. The outcome stays not reproduced under the criterion's peak-to-peak reading.
- **Data check**: now prints the full description strings, every group under `/intervals`, `/stimulus`, `/analysis`, `/processing` and `/general`, the electrode columns and channel names, and the SPW-R table attributes. No file holds condition, stimulation or TTL data. The detection parameters the Methods mention are not stored in the NWB files; this is now a finding.
- **Smaller additions**:
  - edfig4-ripple-features: a bootstrap over rats.
  - fig2h: a variant using the mean instead of the minimum.
  - edfig3: peak prominences (the 3.8-h peak ranks 12th of 45).
  - edfig4-no-hour: empty rat-hours now count as missing, not as 0.
  - CGM32: its leftover swapped dates are documented.
  - supp-ripples-stable: CGM30's infinite deviation and the near-automatic "or" in the criterion are noted.
- **edfig6 (three claims)**: the text now matches the printed timing. I added a 4-process timing scaled to all 18 rats (203 min), the 8 rats with the most hours (172 min) and the 3 rats with stored brain states (66 min). Every estimate is over the 30-min notebook limit, so the claims stay blocked as too_large.
- Added `questions/000233.yaml` with the edfig2 question: should it use the legend's auto-correlograms, and which time point of each ripple? Added round 1 under `verifications` for all 35 claims (33 agree), and updated the README and `entry.yaml` (runtime now 7 min).

**Not done**
- I did not attempt the edfig6 predictor models, for the timing reasons above.
- The verifier asked for an independent check of the glucose and ephys clock alignment. The data hold no shared event to check it against, and the notebook says so.
- My first survey command hung and cost an hour of the run; I used timeouts after that. One later run hit a temporary 503 from the DANDI API and passed on retry.
- Untracked dotfiles and `scripts`/`.idea` entries in the repo root are device files the sandbox mounted before the run started. I left them alone.
