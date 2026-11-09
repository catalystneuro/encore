I checked the claims file and it is ready for an attempt. I made nine corrections and left two points open.

**Checker result:** `claims/000138/10.1016-j.neuron.2010.09.015.yaml: 15 claims, 15 quotes, 9 statistical values, 0 problems` (same result before and after my edits).

**Changes, by claim**
- **fig4e-correlation-time-course:** The criterion compared the curve against an "early value" it never defined. The reference is now the value 400 ms before movement onset, and the criterion says all its thresholds are set here, since the paper gives no numbers for "began to decline" or "near zero".
- **results-ap-location-no-effect:** The paper reports r and p but names no significance threshold, so the criterion now says p = 0.05 is an assumption.
- **fig6-peri-movement-space-best:** The upper-limit space (the gray line in Figure 6A-D) and the shuffled space of Figure 7A are no longer counted as competing spaces. The paper treats one as a bound and the other as a control.
- **fig6-pd-adequate-all-spaces:** The paper says only "generally", so the criterion now says its "more than half of task spaces" share is set here.
- **fig6e-summary-rank:**
  - The statement said all other spaces are significantly worse than the best. The legend says only that the spaces marked with asterisks are; corrected.
  - The criterion required the kinematic and EMG spaces to beat every task space, but the paper says "largely outcompeted". It now requires more than half, marked as set here.
- **fig7a-shuffled-space-poor:** Added that Figure 7A averages over all datasets, while the criterion judges each dataset on its own.
- **fig7b-window-start-onset:** Following the Figure 7B legend, the best dimensionality is now taken separately for each window start time.
- **fig7c-anterior-posterior:** The 10% bound for "only slightly different" is now marked as set here.

I found no problems in the other claims. The paper's main findings are all covered, and every claim comes from this paper.

**Still open**
- The main-text PDF isn't available, so the per-dataset values in Figures 6 and 7, the range of dimensionalities plotted, and which spaces carry asterisks in Figure 6E couldn't be read.
- **fig8-oscillator-model** is a simulation that uses no recorded data. It is marked `with_inputs`, which keeps it out of the dataset's count, even though no outside input is involved. Other claims files mark simulations both this way and as `elsewhere`, so I left it as is.

The `checks` entry with these changes is at the end of the file. Nothing was committed or pushed.
