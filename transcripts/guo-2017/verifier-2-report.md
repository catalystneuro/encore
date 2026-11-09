## Round-2 verification: Guo et al. 2017 on DANDI:000009 (version 0.220126.1903)

### 1. Outcomes

The attempt record and claims file list 39 claims: 7 reproduced, 11 partially reproduced, 4 not reproduced and 17 blocked. The Summary in cell 92 and the README match the record.

**I agree with 30 outcomes:**
- **Reproduced:** fig1c-alm-photoinhibition-bias, vgat-thalamus-reduction, fig2e-alm-contra-ipsi-balance, fig3-onset-latencies, wc-contra-alm-small-effect, thalamus-stronger-than-cortex, selectivity-time-course. fig3-onset-latencies and selectivity-time-course are fragile, as the record says.
- **Partially reproduced:** fig3-alm-collapse, fig6c-unmodulated-less-selective. Both criteria have a partial clause, and it is met.
- **Not reproduced:** task-performance (now changed from partially reproduced), wc-near-threshold, fig6c-vmval-reduced, fig6e-onset-latencies.
- **Blocked, all 17:** I agree with every blocked outcome. I also checked the archive metadata for the 137 extracellular assets: each lists only ElectrodeGroup and Units, with no OptogeneticSeries. That supports the notebook's statement that the extracellular files hold no laser trace, so the onset used for the fig3 and fig6e latencies stands.

**I disagree with 9.** I would give not reproduced to alm-unit-classes, fig2e-alm-selectivity, thalamus-unit-classes, fig2f-vmval-selectivity, fig3f-thalamus-silenced, wc-thalamus-hyperpolarization, wc-m1-small-effect, fig6d-localized and snr-photoinhibition.
- None of these criteria has a partial clause. Each says "Reproduced when …" and nothing else, and no reading meets it (cells 25, 28, 34, 37, 49, 67, 73, 88).
- The record itself says "The criterion has no partial clause" for wc-thalamus-hyperpolarization and wc-m1-small-effect.
- wc-thalamus-hyperpolarization is firmly not reproduced. Under the claims file's readings, E gives +0.31 mV and M gives −16.83 mV, outside −18.7 ± 1.1. The 73% figure that supports "partial" comes from reading L, which is not in the claims file (question 7 is open). Even under L the Vm change (−13.68 mV) is out of tolerance.
- wc-m1-small-effect: the spike-rate change is out of tolerance under every reading (+0.94, +0.76 and −0.01 spikes/s against −1.4 ± 0.6).

I found no place where the claims file misreads the paper.

### 2. Sentences the printed numbers do not support

The numbers in the "**Result:**" cells, the Summary, the README and the record notes otherwise match the outputs. The exceptions:

- **Cell 20:** "changed on the verifier's reading that no reading meets the criterion and only the percent correct holds". My reason did not say only percent correct holds. Cell 19 shows the whole-cell pooled reading with two values within tolerance (77.42% correct, 9.65% lick early).
- **README:** "its 181 putative GABAergic SNr units". Cell 17 counts 171 putative GABAergic units under P1 and 146 under P2, out of 181. The record hedges this with "apparently"; the README states it as fact.
- **Cell 68 and fig6d notes:** "The group counts (240 to 286 …) match the paper's 250 near the centre". The value 286 (u2, T1, cell 67) is outside 250 ± 25.
- **Cell 15, cell 89 and wc-thalamus notes:** "M … 27 ms after [the laser onset]". Cell 14 gives the laser onset as 0.0716–0.0720 s after `pole_out_time`, so M (`pole_out_time` + 0.1 s) is 28 ms after it. This is trivial.
- **Cell 92:** "the onset latency is judged under L only", while the record says L is "shown pending question 7". The claims file says the 7.9 ms onset cannot be judged under any reading it lists.
- **wc-thalamus measured value:** it lists 9.05 ms, the onset under M, which the notes call "not judged".

**My round-1 reasons in the record** are close to verbatim and fair. Two gaps:
- Problem 2 (spike storage) appears in no reason, only in the responses to fig2e-alm-selectivity and fig2f-vmval-selectivity.
- The vm1-photoinhibition-no-effect reason omits my note that, if the (0.5, 0.5) site is vM1, part (b) holds and part (a) holds in some readings.

### 3. Round-1 points

**Resolved:**
1. **Laser trace in the whole-cell files.** The OptogeneticSeries is now read and shown as reading L. The outcomes are the same under M and L.
2. **Where spike storage ends.** It is fixed relative to pole onset (median 4.81–4.84 s after it), and every kept trial has a 1.3 s delay. Windows past the stored spikes are now counted as missing; this affects 221 of 8991 kept ALM trials.
3. **SNr rates.** A rate over the stored part of each trial is added as a variant.
4. **Onset rule.** It is checked on simulated data and the record calls the pass fragile. The rule follows convention O as written.
5. **VGAT delay lengths.** All delays are 1.3 s, so W1 contains no time after the laser; the 100 ms bins are shown.
6. **SNr P2.** It now uses the 'Narrow width spiking' label (146 units).
7. **fig3d Welch's test.** Added.
8. **Kink placement.** The kink is the first sample searched in 1.7% of spikes; leaving them out gives 7.23 mV.
9. **snr-unit-properties header.** Now states both the block and the tested selectivity part.

From my "could not check" list: the missing ALM sessions cannot be identified, because `session_start_time` is the conversion date for every session. Whether `unit_y` is depth below the pia remains unknown and is recorded as a finding.

**Still bearing on a conclusion:**
- The 9 outcomes above that are given as partially reproduced under criteria with no partial clause.
- wc-thalamus-hyperpolarization depends on reading L, which awaits question 7. It is not reproduced under any reading, whatever the answer.

**Not bearing on a conclusion:**
- A trial's stored span ends at the last spike of any unit in it. Masking windows that end later therefore depends on activity, but it touches about 2.5% of kept trials.
