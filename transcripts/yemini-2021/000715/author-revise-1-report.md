I've revised the attempt for every point in the round-1 report, re-run the entry twice with `python tools/entry.py all entries/000715-yemini-2021`, and checked the conclusions against the second run. All three notebooks pass and `check` reports 0 errors. Nothing is committed.

**What changed in the outcomes**
- **fig2cd-variability-differs:** reproduced → partially_reproduced. The criterion needs the difference in both head and tail, and only heads are in the dandiset.
- **ms1-uncertain-first-faster:** reproduced → partially_reproduced, for the same reason.
- **fig6de-asj-ric-stimulus-specific:** not_reproduced → blocked (methods_underspecified). The paper says similar neurons "were deemed too similar and removed" but not whether both members of a pair went. The claim holds with no removal or with one member removed, and fails with both removed. No reading is better supported, so every result is shown.
- All other outcomes are unchanged. `verifications` records 13 agreements and 3 disagreements, with each response.

**Main finding from the orientation check (verifier problem 1)**
- The five heads imaged in dorsal-ventral view are stored rotated by 92.6 to 102.7 degrees about the long axis relative to the atlas. The five left-right heads are within 1.8 to 12.9 degrees.
- Algorithm 5's identity start gets 9.6% on average on the dorsal-ventral heads, against 68.5% on the left-right heads.
- The CELL_ID rotation search gives only 4 distinct starts from its 52 candidates, because it undoes each rotation. I recorded this as a `code_mismatch` finding.
- I added a variant that starts Algorithm 5 from four rotations and keeps the lowest-cost run. It is not the paper's method and uses no annotations.
  - Identification accuracy rises to 74.7 to 77.4%. The highest value is 77.38%, just under the 77.4% bound, so fig7bc stays not_reproduced.
  - Even aligning each worm by its true correspondences gives only 77.7 to 80.2%.
  - The variant is shown for every identification claim and changes no outcome. Position-only accuracy reaches 43.1 to 44.0%, still below 45%.

**Other outputs added or corrected**
- **fig7de:** sparsity 2000 got 7,500 runs and sparsities 1000 and 3000 got 1,000 each. The best 3-reporter values are 8.38%, 7.83% and 12.36%, all outside 9.45 to 11.55%, so the sparsity choice does not change the outcome. To stay within the time limit, the reference runs on the paper's own adjacency dropped to 1,000 per setting.
- **Ventral ganglion (head part):** with ganglia from the CELL_ID tables, it is the least accurate of the seven head ganglia under every alignment (12.9 to 31.6%). Accuracy does not follow density across the head ganglia.
- **Detection:** the optimiser reported success in 2,046 of 2,065 fits.
- **Sinkhorn shortcut:** it differs from a port of CELL_ID's log-space version by 0.0001 to 0.0013 per worm.
- **Data check:** the annotations of all ten heads now match the Zenodo annotation files, names and positions, within 0.5 voxel. This also shows the stored voxels are 0-based.
- **Forward regression (equation 4.11):** now run as an atlas variant.
- **Text fixes:**
  - The helper's false claim that removing both members "removes few traces" is replaced: it removes 647 of 3,550 head traces and 161 of 797 tail traces.
  - The median filter is described as 3 samples (0.75 s).
  - The ridge's effect on the all-neuron table is noted.
- README, `entry.yaml` runtimes, findings and inputs (the CELL_ID ganglion table, the Zenodo annotation files) are updated.

**Not done, and why**
- **Detection optimiser:** I did not measure how the switch from MATLAB's fmincon to SLSQP affects the detections. The alternative I tried (trust-constr) was too slow for the notebook, and the record says the effect is not measured. Accuracy is 71.0%, one point under its 72% bound, so this could matter.
- **No new reader question:** the fig7de misreading the verifier raised (problem 5) was already in `questions/000715.yaml` and is still unanswered. Its point that the color-violation measure was picked for agreeing with 3.5% (problem 6) came from a reader's earlier amendment, which I may not change.
- **Stale executed copies:** after the final run I changed one sentence of notebook markdown (the rotation angles, to the exact printed values), so the executed copies show the earlier rounded wording. No numbers are affected.
- **Notebook runtime:** `optimal_coloring.ipynb` now takes about 24 minutes, close to the 30-minute CI limit.
