I've revised the attempt for every point in the verifier's report and re-run the entry. `python tools/entry.py all entries/000253-siegle-2021` passes with 0 check errors: `reproduce_siegle_2021.ipynb` took 12 min and `ccg_siegle_2021.ipynb` 21 min. The conclusions match the new numbers, and round 1 is recorded under `verifications`, where the verifier's outcome agrees with the round-1 record for 34 of the 36 claims. Nothing is committed.

**Outcomes that changed**
- **fig2-sharp-peak-pairs, reproduced → not_reproduced.** With the CCG jitter bug fixed (B1), no reading is within tolerance. With 2 s windows and all units, the possible pairs match (2,116,259), but there are 21,962 sharp peaks against 16,119 ± 1,612, and 1.18% per mouse against 0.96 ± 0.13%.
- **fig2f-directionality-vs-anatomy, reproduced → partially_reproduced (rests on an assumption).** r = 0.827 with p < 1e-5, just above the tolerance of 0.666 to 0.814.
- **fig3-unit-counts, reproduced → not_reproduced; ed10b-layers, partially_reproduced → not_reproduced.** These now follow the verifier. The earlier assumption rested on `get_flash_PSTH.py` having written the paper's latency table. It actually reads that table and writes a different file, so the claims file's windows from the Methods are judged:
  - fig3-unit-counts: 13,344 or 24,459 units, and 5,842 for the decay timescale.
  - ed10b-layers: 1 of 4 parts within tolerance.
  - The scripts' windows are shown as variants.
- **No longer rest on an assumption:** fig2-neighbour-offsets-across-mice (still partial, 4 of 5 pairs), ed7c-v1-leads-am-follows (still partial, 9 of 10) and ed8-total-hierarchy-score (still reproduced, THS 0.839). Every reading now gives the same outcome for each.
- **ed7fg-absent-in-spontaneous** stays not_reproduced but is now marked as resting on an assumption. With all units the correlation is still significant (p = 0.022 and 0.026). With the Extended Data Fig. 1j filters it disappears (p = 0.54 and 0.46).

**What I fixed or added**
- **B1, jitter bug:** fixed in `siegle.ccg_group` (G[-k] = G[k].T). A new notebook cell checks it against a direct count of spike pairs on synthetic trains. The old helper fails that check (error 8.9e-2) and the fixed one passes (5e-9).
- **B2, duplicated within-area pairs:** the within-area reference now counts each pair once, with a random orientation. File order and the old double count are shown as variants.
- **B3, consistent readings:** the dependent CCG claims are judged under one reading, labelled "judged" in the outputs. Since no reading reproduces the parent claim, it is the one whose pair count matches the paper's and whose peak count is nearest (2 s, all units).
- **B4, latency table:** I compared it unit by unit on one session, printing each flash's first-spike time, and tried 60 procedures. None brings more than 14.5% of units within 1 ms of the table, so no cause is found; this is recorded as a finding.
- **B5, 26 mice against 25:** a leave-one-mouse-out check changes neither the peak-count outcome nor the fig2f correlation outcome.
- **B6, intrinsic timescale:** 8,834 of the 15,958 kept units sit at the 1 ms bound. Without them r = 0.082, p = 0.85, so ed9fg-intrinsic-timescale-not-correlated is still reproduced; its notes and conclusion now say the test is weak.
- **AllenSDK receptive-field p-value:** in AllenSDK v2.0.0 it uses spike counts and gives no p-value below 10 Gabor spikes. I adopted that rule, with a citation; fig1g becomes 60.7% and 1.58%, still partially reproduced. The variant without units lacking a p-value (B8) is shown.
- **Other outputs asked for:** the raw-MI result for ed10b (0.587) is added.
- **ed7e, verifier's point D:** I checked all 325 probe files. Every channel has y equal to z, so the claim stays blocked. The 2D distance is shown as a variant only.
- **Findings and record:** the findings, README and record notes are updated.

**What I did not do**
- **One-resample jitter variant:** not run. The `jitter` function that `get_ccgjitter` imports is in neither repository the paper links. I added this to the question for the paper's authors in the findings.
- **Which mouse the paper left out:** not identified. Nothing in the files names it.
- **No reader question added:** the verifier reported no misreading of the claims file. Its note on ed10b (log10 MI) matches the claims file, which follows the paper's code and lists raw MI as a variant.
- **B7, decay time axis:** left as it is. It follows the paper's script, whose timescale table this attempt reproduces at 99.3%.
