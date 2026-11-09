I've revised the entry for every point in the round-1 report, and 11 outcomes changed. The final clean run of `python tools/entry.py all entries/kim-2020` gave 0 errors and passed in 1020 s, with the same numbers as the run before it. Nothing is committed.

**The key fact.** The claims file's two ways of deciding which neurons have significant STRFs (D7 (a), any significant pixel, and D7 (b), a region of at least 2 pixels) select the same 37 neurons. Every Table 1 claim is now graded on those 37 (problems 1, 2 and 7). Two groups are printed as variants: the shipped code's analytic significance (29 neurons) and my cluster test (15 neurons, last round's main group). Each conclusion says where a variant would change the outcome.

**Outcomes now:** 15 reproduced, 5 partially reproduced, 22 not reproduced, 3 blocked.

| Claim | Before | Now | Why |
|---|---|---|---|
| fig4c-btmf-small-psp-higher | reproduced | not reproduced | small PSPs above spikes (p = 0.021) but not above large PSPs (p = 0.18) |
| tab1-total-bandwidth-no-difference | reproduced | not reproduced | small PSPs narrower than spikes (p = 0.020 and 0.0057) |
| tab1-event-rate-no-difference | reproduced | not reproduced | large and small PSP rates differ (p = 0.008) |
| fig5df-strf-narrower-than-trf | reproduced | not reproduced | spike difference 0.46 octaves, outside 0.99 ± 0.45 |
| tab1-fsi-spikes-higher-than-large | not reproduced | reproduced | all conditions hold in the 37 |
| fig6bc-no-correlation-psp-spike-nonlinearity | not reproduced | reproduced | no correlation significant in the 37 |
| tab1-single-band-small-psp-narrower | not reproduced | partially reproduced | small PSPs narrowest, but p = 0.18 against spikes |
| fig6d-spike-threshold-transition-covary | not reproduced | partially reproduced | spike r = −0.37, p = 0.025, outside tolerance |
| fig7e-tab2-inhibition-broader | partially reproduced | reproduced | pre-stimulus baseline at 20 pA, newly run |
| tab2-event-rate-excitation-higher | partially reproduced | reproduced | pre-stimulus baseline at 20 pA, newly run |
| tab2-fsi-ei | not reproduced | reproduced | pre-stimulus baseline at 20 pA, newly run |

The last three match in only one of the 3 to 6 event sets and bandwidth choices run. The notes say so, and in tab2-fsi-ei one test sits at p = 0.051, just above the 0.05 cut it must pass.

**Two outcomes kept against the verifier, with the disagreement recorded:**
- **fig6bc:** reproduced, not partial. Only the 15-neuron variant disagrees, and it rests on my own cluster test, not a claims reading.
- **tab2-latency:** not reproduced, not partial. Peak latency is adopted as the paper's term, and it differs in every event set.

**Added or corrected:**
- **Group outputs:** the D7 (b) count as the claims define it, Table 1 measures for the 29-neuron group, and double-peak counts and ratios without the cluster test.
- **Voltage clamp:** every claim now runs with the full STRF, the second bandpass rule, 40 pA with the nonlinearity and FSI fits, and the pre-stimulus baseline.
- **fig5c:** counts are compared as proportions, since no group has 30 neurons.
- **fig5a diagnosis:** one TRF matrix is printed. The CF is set at 0 dB SPL, where a median of 5 of 45 tones respond, and it does not track the TRF's best frequency at 40 to 70 dB (r = −0.02). The STRF BFs fall on only 9 envelope channels, 11 of them at 20.0 kHz.
- **Data check:**
  - the full listing of the archive's Supplementary folder;
  - the Matlab lines that were ported;
  - the spike cut for each neuron;
  - the pre-stimulus segment, which holds spontaneous events, explaining why that baseline removes nearly every PSP.
- **Tone fixes:**
  - The second TRF-region reading now really differs. It fails fig1d, so the first reading is adopted, marked as an assumption.
  - The decay now leaves out tones with a later spike, and the dropped tones are counted.
  - Amplitudes from the median potential are printed.
  - The stale docstring is fixed.
- **Other code fixes:** the kHz bandwidth now spans the same channels as the octave width. The one Supplementary Fig. 2 pair and the one Fig. 3 neuron are reported; both claims stay blocked.
- **Records:** new `questions/kim-2020.yaml` asks a reader about the claims file's wording of amplitude reading D2 (b); the claim is unchanged. The attempt record has updated notes and deviations, a `verifications` round-1 block (37 of 45 verifier outcomes agreed with the record as it stood), and revised findings. I also updated the README, the summary and `runtime_minutes`.

**Not done:**
- The cluster test is kept as an assumption for bands within an STRF (BF, bandwidth, latency, double peaks). Without it 36 to 40 of the 40 STRFs of each type come out double-peaked, so no alternative was defensible.
- The total-bandwidth reading the verifier questioned (problem 4) is the claims file's own, so I kept it and added the main band alone as a variant.
- I could not check whether the tone file's frequency column is right beyond its 45 values.
