I've worked through all of the round-1 verifier's points. The entry was re-run with `python tools/entry.py all entries/asari-2009`: both notebooks pass and `check` reports 0 errors. Every conclusion, the summary and the record now match the numbers from that run.

**Outcome changes (allowed in this round):**
- **fig4-predictability-upper-bound: reproduced → partially reproduced.** I agree with the verifier. Removing one mean per probe is not centering the paper gives. `CxtDep.m` removes each trial's mean (line 346) and leaves the per-probe line commented out (line 347); the notebook now prints both lines. Under the 16 readings the claims file names, none puts both values within tolerance. The bound near onset is about half (1 + α within tolerance in 10 of 14 fits), but τ is 1.60 to 2.83 s against 1.04 s. Fits that hit the 100-s bound are now flagged and not used, and the assumption flag is dropped.
- **fig8c-relative-effects: partially reproduced → not reproduced.** The point estimates for amplitude and frequency (0.67 and 0.58) are below 1, so even the partial pattern fails. I added a trial-resampling reading that leaves out pairs of draws repeating the same trial, which is what biased the old one. Its intervals contain all five point estimates and put amplitude (0.38–0.95) and frequency (0.42–0.75) below 1 under all five seeds. The uncorrected reading is shown and set aside as biased.
- **fig8a-proportion-by-property: not reproduced → partially reproduced (resting on an assumption).** The verifier gave not reproduced and asked for the colored-noise alternatives, which change the result:
  - Testing each natural sound against its own noise, as Table 1's legend describes, gives higher-order 64/131 (0.489), within tolerance of the paper's 59.
  - Each fragment as its own context gives 0.573.
  - With either, AM (0.692) > FM (0.640) > higher-order holds, and amplitude > frequency also holds, so the partial rule is met.
  - It fails only under the old pooling of all natural sounds against all noises (88/137).

**Added or corrected:**
- **AM/FM shortfall:** a per-file table of experiment 2. The notes parser drops nothing. The 27 MHT files hold only 14 MHT probes with two or more MHT contexts, against 178 in Table 1, so the probes are missing from the files. Counted by their synthetic probes, the cells are TORC 14, DMR 6, colored noise 26 and MHT 2 (paper 14, 6, 27, 39).
- **Experiment 3 (fig7):** none of its 27 files has a sequence and no sound follows another within 50 ms, so it holds no context-probe pairs. The block stands.
- **CxtDep.m:** the lines `asari.py` follows are printed in the notebook. Its run rule is last index minus first ≥ 50 samples, which is 51 points, so `_runs` matches the code and is unchanged.
- **Ties:** on average 3.3% of values at a time point are tied. Midranks with the tie correction give the same 187 of 305 significant probes.
- **STRF:**
  - I applied the missing shift that centres each spectrogram frame on its 4-ms bin, and stated that 17 bands at 3 per octave end at 16 kHz, not 22 kHz.
  - The window gain is still significant over all 16 cells (p = 0.0046), but it comes from the six 2003 cells (p = 0.016); over the ten 2002 cells p = 0.12. The outcome therefore depends on which cells the paper used, which it doesn't say; the record now says so.
  - A per-cell table shows the LN model's loss comes from 6 of 16 cells.
- **figs1:** I added the curve in 100-ms bins and its peak (12.75 mV² at 0.16 s). Only 4 of 18 late bins stay below 10% of the onset value, so the outcome is still reproduced but rests on the criterion's first-crossing wording.
- **Smaller additions:** both noise-floor windows for fig8a-significance-fits; the higher-order natural-vs-synthetic test under the new pairing (p = 0.86, no difference).
- **Record:** findings revised, and round 1 recorded under `verifications` with the verifier's reasons and my responses.

**Not done:**
- No question was added to `questions/asari-2009.yaml`, because the verifier found no place where the claims file misreads the paper.
- I didn't edit the entry README after the run. Its runtimes are approximate, and any edit would have forced another full run.
- The new pairing for higher-order was run for significance only. fig8b, fig8c and fig8a-significance-fits still use the pooled grouping for higher-order, and their notes say so.

Nothing was committed.
