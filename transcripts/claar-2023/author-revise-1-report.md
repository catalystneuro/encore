Round 1 is answered. I re-ran the entry twice with `python tools/entry.py all`. Both notebooks pass: the EEG notebook in 816 s and the spikes notebook in 1166 s, under the 30-minute limit. The two runs gave the same numbers, the notebook conclusions now match them, and `entry.py check` reports 0 errors. Nothing is committed.

**Outcome changes (allowed in this revision; round 2 reviews them)**

Fixing the artifact mask (problem 1) moved the EEG results. The stimulus artifact peaks one sample before the onset sample in 24 of 30 sites, so the mask now starts one sample earlier.
- **fig1e-erp-duration:** reproduced → partially_reproduced. The best reading gives 0.33 and 0.49 s with p = 0.081, against the paper's p = 0.0843; the superficial mean is 0.02 s below tolerance.
- **fig7c-erp-duration-state:** reproduced → partially_reproduced. No reading puts all three means within tolerance.
- **fig7d-erp-magnitude-state:** reproduced → partially_reproduced. Same reason.
- **fig8b-pcist-awake-anesthesia:** partially_reproduced → reproduced. At the medium current PCIst is 43.26 awake against 14.93 anesthetized, higher awake in 30 of 30 sites.
- **fig1f-erp-magnitude** stays reproduced but no longer rests on an assumption. It now passes on reading (a), the area above z = 3: 3.03 against 5.86 with p = 0.035, against the paper's p = 0.0354. Reading (b), my own divisor, is dropped as the basis (problem 4).
- **fig1-supp1-example** stays reproduced. At the medium current with all awake trials it gives 1.011 s and 11.133 SD·s, the paper's 1.01 and 11.13. That near-exact match points to the medium current as the paper's choice, and the README and record now say so.

**Added or corrected**
- **Fig 4 counts (problem 2):** counting each unit once per current gives 870, 4110, 2559 and 9486. These are the legend's first three counts exactly. Run with the three currents pooled, the Figure 4 fractions still don't match, so no Figure 4 outcome changes.
- **Fig 3 spiking magnitudes (problem 3):** now computed in every reading. They are far below the paper's values (example session 3.96 for MO against 30.9). The LFP and CSD parts are still not run, so both claims stay blocked, with the spiking results in their notes.
- **"First" trial matching (problem 7)** now takes the earliest awake trials in time.
- **fig8e outlier (problem 8):** it comes from site 546655, whose stages at the high current are matched on a single trial (PCIst 306.6).
- **Other notebook additions:**
  - an artifact profile for every site (problem 12), shown as a table and a −20 to +20 ms GFP plot;
  - the PCIst check against the original code on all 30 sites, with a largest difference of 0;
  - EEG electrode coordinates and electrode-table columns;
  - a quiescence measure that ignores short gaps, and a triphasic flag that needs at least 10 ms below baseline;
  - fig8d analysed per animal, with the matched trial counts;
  - per-session pooled fractions for fig4ad;
  - confidence intervals for fig7f;
  - full tables, no longer truncated.
- **Reader questions:** a new `questions/000458.yaml` asks whether fig4-unit-counts should count unit × current, and whether fig5c should use the printing precision as its tolerance. I did not change either claim.
- **Record:** `verifications` lists all 37 claims. The verifier agreed with every outcome except fig3abc and fig3d. I also updated the findings and the README, and added a finding on the artifact timing.

**Not done**
- The LFP and CSD parts of Figure 3 were not run. The CSD needs cortical layers, which the files don't have, and reading every probe's LFP was earlier estimated at over 80 minutes.
- stim-depths keeps `data_missing`, although the verifier named `metadata_insufficient`.
- After masking, some sites still show an artifact residue before the onset (up to |z| = 21.8). The paper's 2 ms mask would leave it too, so I describe it in the notebook and do not remove it.
