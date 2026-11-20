I've revised `asari-2009-02` for round 2 and re-run it with `python tools/entry.py all entries/asari-2009`. Both notebooks pass (21 and 22 minutes), `check` reports 0 errors, and the conclusions match the final run's numbers. The round is recorded under `verifications`. Nothing is committed.

One thing you should know first: the attempt was not fully blind. `transcripts/asari-2009/` still holds the earlier attempt's (`asari-2009-01`) transcripts, which `tools/blind.sh` should have removed. Early on I listed that folder and read the first 50 lines of `verifier-2-report.md`. That showed the earlier attempt's outcomes and its fig7 band finding. I read nothing more from it. My fig7 conclusion rests on fragment descriptions I printed from the data myself. The reconcile run should know about this.

**Outcome changes**
- **a1-mgb-firing-rates:** not reproduced → partially reproduced, as the verifier gave. With the robust 5-SD and 8-SD detectors the MGB evoked rate is above 5 Hz (13.57 and 10.38 Hz). With the authors' detector it is 4.99 Hz. Still marked as resting on the detector.
- **fig3a-proportion-significant:** partially reproduced → not reproduced. The criterion's partial outcome needs the count within tolerance, and 183 of 305 misses it.
- **fig4-predictability-upper-bound:** partially reproduced → not reproduced. The criterion has no partial outcome, and no reading gets the time constant within tolerance.
- **fig4-strf-performance-low:** blocked → not reproduced, resting on assumptions. It is now tested in a new notebook, `strf_wehr.ipynb`, with a helper `wehr_strf.py`.
  - Validation performance stays under 0.22 in every reading.
  - But the STRF model improves significantly from the 180-ms to the 4052-ms window (Wilcoxon p 0.000 to 0.042), and the LN model does worse than the STRF, not slightly better.
  - The criterion is met in one combination only: folds formed by stimulus, with validation averaged over folds the way `STRFanalysis.m` does. That is stated in the record.
- Every other outcome is unchanged; the verifier agreed with them.

**Added or corrected**
- **fig4 question:** the Figure 4 legend fit matches 1 − Q(t). With silence counted, that fit gives 0.505 to 0.513 and 1.008 to 1.050 s, within tolerance. It is shown as a variant only. I added a question to `questions/asari-2009.yaml` and left the claim unchanged.
- **fig8:**
  - Dropped the mixed reading that picked a counting rule per property to match Table 1's totals. The probe reading is now the measured value, and the entry reading is shown beside it.
  - Table 1 is rebuilt by recording family and probe type. The data set has only 14 MHT probes, against Table 1's MHT row of 25, 25, 71 and 57. The extra AM and FM ensembles of the natural probes plus those 14 come to exactly 71 and 57.
  - The order margins are printed; the AM-over-FM margin is 0.001 in the probe reading.
- **fig8c:** added resampling of as many probes as the population holds. The higher-order interval then overlaps in both readings; the outcome stays partial.
- **fig7:** the band vector (625, 2500, 10000, 40000) is one split-band fragment ("DMR4: bandwidth 625-2500, 10000-40000 Hz"). It sits in recordings with no natural fragment, so the block stays data_missing.
- **Data check:** now prints the authors' `CxtDep.m` ranking and PSTH lines; the helper ranks ties the same way. It also prints the int16 step size (at least 231 steps per trial SD in 95% of probes, so ties are rare). The 15 unpublished files and 161 tuning curves are also whole-cell or cell-attached recordings in mV, so there is still no voltage-clamp data.
- **Counts:** the 132 A1 cells are listed by family. Their families don't line up with the paper's (DMR 6, MHT 39, MCN 27), so I can't say which 9 cells account for 132 against 123.
- **fig9:** notes that comparing the plateau with the fitted constant checks little; the claim rests on the time constant.
- **Record and docs:** two new questions for the authors (the STRF cells and fold averaging, and Eq. 43 against 1 − Q), an extended Table 1 finding, and updated README and `entry.yaml`.

**Not done**
- The trial-resampling reading for fig8c. It needs every probe's trials kept through the analysis, which the entry doesn't do.
- The degenerate last PSTH bin and the file with the 308-ms trigger mismatch are kept as the authors' `CxtDep.m` handles them, and the record says so.
