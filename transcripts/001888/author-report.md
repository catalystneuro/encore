I've finished steps 1 to 5 and run the handover (step 6) for dandiset 001888; the entry passes `tools/entry.py all` with 0 errors. Of 34 claims, 12 are reproduced, 9 partially reproduced, 3 not reproduced and 10 blocked. I used the open-access full text and supplement (CC BY, PMC12779324), saved under `paper/`. The dandiset has no published version, so I pinned the draft as modified 2026-07-31 09:37 UTC; the notebook stops if the draft changes.

## 1. Outcomes per claim

| Claim | Outcome |
|---|---|
| fig2b-swd-hourly | reproduced (genotype p = 0.0045, hour p = 0.069) |
| fig2c-swd-number | reproduced (p = 0.047) |
| fig2c-swd-mean-duration | partially reproduced (only one WT rat has SWDs, p = 0.16) |
| fig2c-swd-total-duration | reproduced (p = 0.033) |
| disc-het-swd-minutes | partially reproduced (Het 57.8 min matches; WT 1.37 min is not under 1 min) |
| figs5a-swd-light-dark | reproduced |
| figs8-swd-sex | reproduced |
| fig2d-swd-spectrum-peak | reproduced (all 15 rats checked, including the WT) |
| fig3d-rem-hourly, fig3g-rem-total | reproduced, both at p = 0.048 |
| fig3g-rem-bouts | reproduced (p = 0.001) |
| fig3g-rem-bout-duration, fig3h-nrem-bouts, fig3i-wake-total, fig3i-wake-bouts | partially reproduced (right direction, not significant) |
| fig3h-nrem-total, fig4a-rem-spectrum | reproduced (both are "no difference" claims, tested with two WT rats) |
| fig4b-nrem-beta, fig4c-wake-power | not reproduced (effect goes the other way) |
| fig5a-swd-state-distribution | partially reproduced (wake 94.2% matches; NREM and REM shares do not) |
| fig5c-transition-swds | partially reproduced (13 of 14 Het, p = 0.025) |
| figs5b-transition-percent | not reproduced (36.3% against 24.2%) |
| fig5f-swd-wake-correlation | reproduced (R = -0.81) |
| fig5def-no-other-correlations | partially reproduced (2 of 8 measures do correlate) |
| fig2e-swd-delta-power, fig5a-het-more-nrem-swds | blocked, other (only one WT rat has SWDs) |
| western blots, development, scorer validation, 4 pharmacology claims (8) | blocked, data missing |

The wake results depend on removing SWD epochs from wake: with the stored scores, the wake-bout differences reverse and the SWD-wake correlation disappears (R = -0.06).

## 2. What I found about the dandiset

- **Animals:** 17 rats: 14 Grin2b+/- (Het), 2 wild type (WT), and GRIN2B-132 with no genotype and sex "U". The paper analysed 9 WT, so the dandiset holds only 2 of them. It does not say which rats the paper analysed.
- **Missing data:** the pharmacology recordings, western blots, development measures and visual scoring are not in the dandiset. A search of the archive found no other dandiset for this paper.
- **`sleep_states`:** the description lists code 4 for SWD epochs, but no file holds it.
- **`swd_epoch_counts`:** it holds flags (4 or 6), not counts. The flags cover about half of the epochs that SWD events overlap, mostly the last epoch of each SWD.
- **`seizure_totals_by_zt`:** the columns are mislabelled. Per-hour counts sit in `spike_wave_discharge`, and the day's total is in the first row of the other two count columns.
- **Stored spectra:** the description is wrong. They hold the lab scorer's log amplitude, not the baseline-corrected power the description and Methods state.
- **Raw EEG:**
  - Values are unsigned 12-bit codes with offset 0, so every channel reads about +8 mV of DC.
  - Signal loss is written as 32767, which is not documented.
  - 21 to 73% of the 5-s epochs read per rat contain such bad samples.
- **Archive summary:** it says 16 files, but there are 17.
- **Paper:** its Figure 3 and Figure 5 legends contain some statistics that contradict each other.
- **Checks that passed:**
  - The sleep scores and SWD events line up in time with the raw EEG and EMG.
  - The recordings are not duplicated.
  - Every day has more sleep in its first 12 h, which fits lights-on at the window start.

## 3. Where the protocol was unclear, wrong or missing something

1. **No published version.** The protocol only covers drafts for repeat attempts. I pinned the draft and made the notebook check its modification time and file count.
2. **"Open a file" is not enough.** I first opened only GRIN2B-132, the one file without a genotype, and took genotypes from the conversion repository as an outside input. The other 16 files do hold them. I switched the source to the files and changed the SWD-epoch choice, both before reading any claim output. A first run had executed the claim cells, though; the protocol doesn't say whether criteria may be revised after that. I recorded it in the claims file. The protocol should ask for metadata across all files.
3. **Methods and code disagree on SWD epochs.** Following the protocol, the main analysis uses the Methods (epochs overlapped by SWD events) and the lab's flags are a variant. The protocol doesn't cover the case where the data show the code's own input is incomplete.
4. **Small groups.** There is no rule for how small a group can be before a claim is blocked. I set a minimum of two animals per group, and called a result partial when the direction holds without p < 0.05.
5. **"No difference" claims with little power** (2 WT) count as reproduced under the absence rule. I flagged the low power in the notes.
6. **One claim spanning eight tests** (fig5def) doesn't fit the binary absence rule. I graded it: one or two significant tests gives partial.
7. **A matching variant cannot rescue a claim.** For figs5b, an NREM rule I only ran as a variant gives 22.9%, within tolerance. The outcome stays not reproduced because the protocol only accepts readings listed beforehand.
8. **Speed against fidelity to the Methods.** Following the Methods' spectra means processing raw EEG, so I used about 4.8 h per rat to stay fast. The clock check uses a contrast with shifted labels, not a decoder, on the same sampled windows. Two rats without SWDs could not be checked for SWD timing.
9. **Undefined method choices.** The paper does not give band limits, Welch segment length, a bout definition or a transition rule. I fixed these before analysis and recorded them as deviations.

## 4. Runtime and failures

The notebook takes 4.6 to 4.8 minutes (278 s on the final run). Executed outputs are identical to my draft run apart from timings. The only failures were scratch-script errors during exploration, all fixed. One code bug against a written criterion (the SWD peak rule checked only the first 5-10 Hz peak) was fixed before I wrote the conclusions; it changed fig2d's outcome. Nothing is committed.

Files are in the repository root:
- `entries/001888-hristova-2025/`
- `claims/001888/10.1111-epi.18606.yaml`
- `attempts/001888-hristova-2025-01.yaml`
- `executed/001888-hristova-2025/handover/` (the verifier's package)
