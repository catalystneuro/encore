**Verification report, round 2: Kaku, Liu et al. 2025 (doi:10.1101/2025.01.27.635041) on DANDI:001619 v0.251027.1953**

The claims file has 48 claims and the attempt record has 48 outcomes, with matching IDs:
- reproduced: 15
- partially reproduced: 4
- not reproduced: 6
- blocked: 23 (data_missing 18, other 2, methods_underspecified 1, too_large 1, metadata_insufficient 1)

Three outcomes are marked `assumed: true`: fig2f, ed8bc and fig4f. Cell numbers below refer to the re-executed notebook, whose numbering differs from round 1.

### 1. Outcomes

**I agree, with no comment:** code-dataset-link, region-spike-rates, fig1i, fig1f-licking-mode-switch, fig1k, both fig1l claims, both fig1n claims, fig2-licking-breathing-tuned-counts, fig2-swallow-modulated-counts, fig2g, fig2h (blocked, methods_underspecified), ed6e, ed8e, ed8i, ed4c, and the 18 data_missing blocks (including fig4d, fig4g, fig4g-symmetric-lags and fig4h).

**I agree, with qualifications:**
- **fig1d (partially reproduced).** This follows the criterion. Under reading (b), though, bouts are built from runs of lick intervals between 3 and 9 Hz (`kaku.movement_timing`). The licking mean and 95% range within bouts (6.07 Hz, 3.77 to 8.40) are therefore largely fixed by that definition.
- **fig1f-inspiration-between-licks (not reproduced).** The outcome holds under both readings, but the alignment question is still open (section 3).
- **fig1g (partially reproduced) and fig4e (reproduced).** Both follow the criterion, which compares with 0.
  - fig1g: the data do not exceed the random-split null (+9.1 ms, paired p = 0.17; above the null in 10 of 20 mice; cell 27).
  - fig4e: units with MI > 0.6 do not exceed the null either (p 0.076 to 0.15), and under O2(b) the difference is negative (cell 69).
  - The record states this.
- **ed1 (reproduced).** This holds by the letter of the criterion. The licking model gives a Fig 1g value in 1 of 172 sessions, so "not significant" holds by default; the record says so. The model draws inter-lick intervals independently from the pooled distribution, so the simulated licks are not rhythmic. That follows the criterion's method, and it is one reason the measure is missing.
- **ed1bc (not reproduced).** This follows the criterion. Whether the criterion's window misreads the paper is now with a reader.
- **ed7 (blocked, too_large).** I accept this, given the measured cost: at least 9 CPU hours for O8(a) alone (cell 58). The stated numbers are wrong (section 2).
- **fig3a and fig3b (blocked, other).** The claims file marks the data as held elsewhere, so `other` is more accurate than my round-1 data_missing. Both claims are testable from the eLife source data and were not run.

**I disagree:**
- **units-count (partially reproduced).** The criterion defines no partial level. P, MY and the insertion count (exact tolerance) are outside it, and CB is outside unless the arbor vitae is counted. The record changed region-spike-rates and fig1f-licking-mode-switch to not reproduced because their criteria define no partial outcome. The same reasoning gives not reproduced here. My round-1 call of "partially" had the same inconsistency, and I withdraw it.

**Assumptions:**
- **fig2f and ed8bc.** The assumption is stated. The whole-nucleus box is the literal reading of "inside AMB's AP and ML extent". It is not clearly better than the per-AP-step reading:
  - The box takes AMB's deepest point (DV 6,750 µm) and its full ML range (1,225 to 1,525 µm) across all AP levels.
  - A unit can therefore count as within 300 µm ventral of AMB at an AP level where it lies more than 300 µm below the local nucleus.
  - The outcome flips between the two readings (36 or 41 units, p < 0.0001, against 12 or 15 units, p 0.04 to 0.27; cell 49). For ed8bc only 2 units remain under the per-step reading (cell 60).
  - The header blocks a claim whose region readings disagree. I recommend blocked, methods_underspecified for both claims.
  - At the least, the record should show how many mice the 36 to 41 units, and the 18 or 19 ed8bc units, come from. The notebook does not show this.
- **fig4f.** The assumption is stated and reasonable. The header treats O2 as a choice of which subset the paper used, where one reading suffices, and O2(b) has only 2 units, too few for a test.

### 2. Statements the printed outputs do not support

- **Cell 0, "about 40 minutes", and README, "about 42 minutes".** Cell 73 prints 50.4 min, and cell 2 alone takes 45.5 min.
- **Cell 12, "lags of 88 to 112 ms, within the range of the others"; cell 26, "peaks at similar lags in the subjects with low and high fractions, so the fraction is not explained by a clock offset"; record fig1f notes, "at similar lags".** Cell 11 shows the opposite.
  - In the 22 other subjects that peak within the first cycle, the tongue lag is 54.4 to 95.2 ms (median about 78).
  - In DL029 to DL034, the low-fraction subjects, it is 88.4 to 112.2 ms (median about 104), and 5 of the 6 lie above every one of the 22.
  - The jaw lags show the same pattern: 91.8 to 108.8 ms against at most 95.2 ms.
- **Cell 24, "because the code's tongue onsets include onsets a few milliseconds apart".** Cell 23 shows that without those intervals the reading (a) mean is still 21.36 Hz (97.5th percentile 98 Hz), so they do not explain the high frequency.
- **Cell 59 and the record's ed7 notes: "about 20 s ... 0.11 s per unit ... about 7 CPU hours, about 14 ... over 80".** Cell 58 prints 25.8 s, 0.147 s per unit, 9.0, 18.0 and 108.1 CPU hours. The text itself says the printed timing "varies a little between runs", so it was not written from this run.
- **Cell 70 and the record's fig4e notes: under O2(b), "53.3 to 72.0 ms".** The printed means are 53.3 to 68.0 ms. The 72.9 ms value is the code-selection column.
- **Record, fig2-swallow-modulated-counts: V4(b) "62 to 85".** The breathing-and-swallowing counts printed in cell 47 run from 62 to 84.
- **Record finding (data_missing): "15 of the 48 claims are blocked for missing data".** The outcomes give 18. The README row gives 14 for the autoencoder, rat, photostimulation and cued-task claims, plus 4 for the fig4d group.

The other "Result:" cells, the Summary, the other README sentences and the other notes match the printed outputs.

The verification entry states my round-1 reasons faithfully and in my own words. Each one merges my table entry with the matching B point. I cannot check the `agrees` flags, since they compare with pre-round-1 outcomes I did not see.

### 3. Round-1 points

**Resolved:**
- B2: within-bout pairs only. The 13,498 between-bout pairs are counted and shown.
- B4: the port matches the code's cycle-1 definition, and the cycle distributions are shown.
- B7: the 40 fastest and 40 slowest cycles are used, with the code's selection shown beside them.
- B8: the dead line is removed, the reason the measure is missing is shown, and the mix of readings is stated.
- B9: filter order 2 is run.
- B10: recorded as a finding.
- B12: the cost is measured, though the text quotes the wrong numbers.
- B13: the between-hemisphere test is run.
- B14: the reasons now appear after fig4d.
- B1: the random-split null is added, and a question on the windows goes to the authors.
- C items: 3D idx offsets, ed1 diagnostics, the ed1bc trace and the fig1d diagnostics are done.

**Remaining points that bear on a conclusion:**
1. **fig2f and ed8bc (from B3).** Building the regions from the annotation volume, as I asked, shows that the outcome depends on how AMB's extent is read. See section 1.
2. **fig1f and the other lick-breath timing claims (from B6).** The lag check shows a later airflow lag in exactly the subjects with fewer inspirations inside a protrusion. Two other outputs are also consistent with a subject-dependent offset between airflow and video of tens of milliseconds, though they do not show one:
   - Around in-bout expirations the lick probability is flat (0.018 to 0.024 per bin; cell 35), which would not be expected if licks were tightly locked to breathing.
   - Around swallows, licking pauses before the detected onset, from -90 to 0 ms, and resumes after it.

   This is not settled. Per-subject results for fig1f and fig1g with DL029 to DL034 separated would help.
3. **Peak-difference windows (B1, a claims-file method).** fig1g and fig4e (MI > 0.6) cannot be told apart from the window artefact, while fig1i and fig4f can. The outcomes follow the criterion.
4. **units-count (B11).** The arbor-vitae question is with a reader, and the outcome is inconsistent with the record's own rule (section 1).
5. **ed1.** The licking-model result holds by default.
6. **fig1d.** Under reading (b) the licking values are constrained by the bout definition.
7. **fig3a and fig3b.** The data are public and the claims were not tested.
8. **ed1bc (B5).** The criterion's window question is with a reader.
9. **Text errors in section 2.** The fig1f and ed7 sentences bear on how those conclusions read.

**Not checkable from my materials:** whether any of the 162 two-probe sessions are among the paper's 43 simultaneous recordings.
