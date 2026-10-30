I've finished the round-1 revision. The entry was re-run from a clean environment and passes in 22 minutes, inside the 30-minute limit. `entry.py check` reports 0 errors, and the record's conclusions match the final numbers.

**What changed in the outcomes.** Before this revision 7 claims were tested and 40 were blocked. Now 41 are tested: 9 reproduced, 9 partially reproduced, 23 not reproduced, and 6 are still blocked.

The verifier's main point was right. About 33 claims had been blocked as "methods underspecified, inherited" from fig1g, which the claims file does not support, so I removed those blocks and ran the claims:
- **Gamma ICA:** fig2c partially reproduced. ica-volume-conduction-fraction and fig2d not reproduced.
- **Coherence clusters:** fig2b reproduced, but only under the reading where six clusters are imposed and boundaries are compared with the across-mouse median. That comparison can hardly fail, and left free the clustering gives 8 to 20 clusters. fig2b-clusters-same-across-states reproduced.
- **LFP power by layer:** fig3c-slow-oscillation-nrem-deep partially reproduced. fig3c-3-6hz-layer4 and slow-gamma-superficial-wake reproduced.
- **3-6 Hz rhythm:** figs2c not reproduced. fig3f reproduced.
- **Cross-frequency coupling:** both fig3d claims partially reproduced (the coupling frequencies match, some index values do not).
- **Unit clusters:** fig5b not reproduced, because the silhouette favours 2 to 6 clusters, never 8. fig5a partially reproduced.
- **Layer claims on the eight clusters:** fig6b-deep-wake-higher and fig6g reproduced, fig6h partially reproduced. fig6a, fig6b-superficial, fig6c to fig6f, fig7-within-layer-fractions, fig7eg, figs8b and fig7d/e/h/g are not reproduced.
- **DOWN state-active neurons:** fig8-down-active-neurons and fig8-down-up-rates not reproduced (25 units in 13 mice against 5 in 4). fig8cd partially reproduced. fig8eh reproduced.

No earlier outcome changed. I kept figs7 as partially reproduced; the verifier would give not reproduced. I recorded that disagreement, since under the adopted reading 3-6 Hz is still the strongest band.

**What I added or corrected:**
- **Channel order (B2):** the data columns are in depth order; the best-correlated site is an adjacent one for 50 to 63 of the 64 sites in each file. `max_channel` holds the electrode table's `id` (a hardware channel number) for the unit's peak site, not the column index. I rewrote those two findings.
- **Landmark rule (B3):** fig1g now shows CSD maps with the placed landmarks for all 19 mice, lists the mice where the rule takes probe-edge values, and has the corrected "not placed" message.
- **Genotypes (B4):** the fig4de conclusion now flags that the file genotypes contradict the paper's.
- **IC reading for figs7 (B5):** it now runs, and does not change the outcome.
- **Diagnostics (B6, C):** the notebook now prints connection counts per state and lists every group in every file.
- **Wavelet edge (B8):** the edge is now 8 s and the 600 s cap applies to the total.
- **I-E reading (B9):** the notes now say the main reading includes inhibitory connections onto I cells.
- **Record:** the round is recorded under `verifications` with the verifier's reasons and my responses, and I added two `methods_unavailable` questions for the paper's authors (how the eight clusters were obtained, and which components count as volume conducted). `scikit-learn` is added and the environment re-locked.

**Assumptions the new outcomes rest on**, all stated in the record and marked `assumed: true`:
- Depth is measured in sites relative to the MUA power peak c, in place of the paper's normalized depth, because the other landmarks can't be placed by any rule the paper gives.
- scikit-learn's FastICA stands in for runica, which isn't available in Python.
- The layer 4 site is the peak of the third gamma IC by depth, and the layer 6 site is 15 sites below c.
- The layer claims use an eight-cluster solution that the silhouette does not favour, as the fig5b criterion instructs.

**What I did not do:**
- The ICA was fitted on waking only; the whole-session reading was not run.
- The waking-immobility reading of fig3d-3-6hz was not run, because the dataset has no movement signal.
- The fig8-down-active-neurons notebook also shows a stricter rule (DOWN rate more than twice the UP rate). It finds 5 units in 4 mice, which matches the paper, but it is not a reading in the criterion, so it decides nothing.
- No questions were added to `questions/000166.yaml`, since the verifier reported no place where the claims file misreads the paper.
- `tools/runner/chain.sh` was already modified before this run, and I left it alone.

Nothing is committed.
