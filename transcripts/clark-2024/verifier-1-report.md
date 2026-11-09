**A. Outcomes** (31 claims in the claims file; the notebook blocks all 31)

| Claim id | My outcome | Reason |
|---|---|---|
| grid-cell-count | blocked, too_large | Cell 4 shows 0 of 734 files hold a units, processing or intervals table. I checked the archive API myself: every asset's `variableMeasured` lists only ElectrodeGroup and ElectricalSeries, so units would have to be re-sorted from about 638 GB of raw signal. Reading that alone takes 2.4 h at the measured 73.5 MB/s (cell 19), and sorting comes on top. |
| supp1-recording-summary | blocked, too_large | It needs cell and grid-cell counts. The parts that need no units are only partly consistent: cell 8 gives 242 sessions against the paper's 215 (difference 27, tolerance 21.5), and 4 of 9 mice are off by more than 10% (M3 30/26, M7 28/23, M10 25/16, M12 28/21). The mean of per-mouse mean trials is 183.9 against 179.1, inside tolerance. The paper counts only sessions with kept units, so this mismatch does not decide anything. |
| grid-field-size-spacing | blocked, too_large | Needs sorted grid cells; same reason as grid-cell-count. |
| fig2-session-level-classes | blocked, too_large | Needs sorted units. |
| fig2e-nongrid-classes | blocked, too_large | Same. |
| fig2f-spatial-information | blocked, too_large | Same. |
| fig2f-firing-rate-similar | blocked, too_large | Same. |
| fig2f-periodogram-features-similar | blocked, too_large | Same. |
| fig2f-aperiodic-low-rate | blocked, too_large | Same. |
| fig3f-switching-within-session | blocked, too_large | Same. |
| fig3f-session-class-bias | blocked, too_large | Same. |
| fig3g-trial-spatial-information | blocked, too_large | Same. |
| fig3g-trial-firing-rate-similar | blocked, too_large | Same. |
| fig3s4-stable-cells | blocked, too_large | Same. |
| fig3s5-grid-vs-nongrid-modes | blocked, too_large | Same. |
| fig3s6-block-lengths | blocked, too_large | Same. |
| fig3s7-trial-type-ratio | blocked, too_large | Same. The trial types are in the position series (cell 6), but the response variable is the trial-level class of grid cells. |
| fig4e-grid-agreement-higher | blocked, too_large | Same. |
| fig4e-agreement-above-shuffle | blocked, too_large | Same. |
| fig4f-nongrid-spatial-information | blocked, too_large | Same. |
| fig6b-stable-beaconed-similar | blocked, too_large | Hit, try and run could be derived from the VR position (cell 6), but sessions are chosen by stable grid cells, which need sorted units. |
| fig6b-stable-uncued-reduced | blocked, too_large | Same. |
| fig6a-stable-stop-density | blocked, too_large | Same. |
| fig6d-epochs-beaconed-similar | blocked, too_large | Same: needs trial-level grid classes. |
| fig6d-epochs-nonbeaconed-reduced | blocked, too_large | Same. |
| fig6d-epochs-probe | blocked, too_large | Same. |
| fig6c-epoch-stop-density | blocked, too_large | Same. |
| fig6e-hit-try-run | blocked, too_large | Same. |
| fig6f-odds-ratio | blocked, too_large | Same. |
| fig6s1-speed-profiles | blocked, too_large | Same. |
| fig6s2-template-method | blocked, too_large | Same. |

On step 4: the archive bears out the notebook's statement. The version metadata, and the asset metadata of all 734 assets, list only raw ElectricalSeries and ElectrodeGroup. No processed or units data exist, and no other version exists. The paper's data statement points to Edinburgh DataShare, not DANDI.

No claim can be tested in part without units. Every claim's selection runs through grid-cell classification. The only units-free parts are the session and trial counts of supp1-recording-summary, and the notebook already reports those.

Could `data_missing` be argued instead? The paper's curated MountainSort output is not deposited, and a re-sort would not give the same units. Still, the raw data needed to re-derive them are present, so `too_large` is defensible. Either way the claims are blocked.

No chance levels apply.

**B. Problems**

1. [does not affect a conclusion] Cell 19, `streaming_rate`: the `too_large` estimate is a lower bound from read time only. It takes the "notebook limit 1 h" as given and cites no source for it. The bound already exceeds 1 h, and the uncosted sorting would only add to it, so the conclusion holds.
2. [does not affect a conclusion] Cells 8–9: the notebook says it compares the session counts with the summary table. It does not say that the 242-session total is outside the claim's 21.5 tolerance, nor that M10 differs by 56%. Its markdown reports only the per-mouse 10% matches.
3. [does not affect a conclusion] Cells 10–11: the nine open-arena position columns are undescribed, and M1 and M2 span about 70 cm rather than the 100 cm arena. Even with units, the open-arena rate maps, and so grid classification, would rest on inferred column meanings and a possible scaling issue (`metadata_insufficient` risk). M1 is one of the nine mice in the paper.
4. [does not affect a conclusion] Helper module docstring: it says the multi-unit check uses "1 s bins", but `mua_and_speed` uses `bin_s=0.1` and cell 14 says 100 ms.
5. [does not affect a conclusion] `shifted_contrast` uses `np.roll`, which wraps labels around the window ends. `lagged_corr` and `shifted_contrast` use opposite sign conventions: on synthetic input where MUA leads speed by 5 bins, I got peak lag +5 and best shift −5. Cell 16 compares absolute values only, so this is harmless. The clock check is inconclusive for the M3 and M12 VR sessions (cell 15), but no claim rests on it.
6. [does not affect a conclusion] Cell 0 summary table versus the claims file: the count matches (31 claims). The claims file itself did not misread the paper in any way that affects these blocks.

**C. What I could not check**

- I could not check the 1 h compute limit the notebook assumes, since docs/protocol.md is not among my materials. A cell printing the protocol's limit, or a timed MountainSort run on one recording day, would turn the read-time lower bound into a direct cost estimate.
- I could not confirm the files' notes that the paper used only 200 cm tracks. The notebook quotes them in the helper but never prints them. Printing `general/notes` or `experiment_description` for one VR file and one open-arena file would let me check that, and the claimed 100 × 100 cm arena.
- I could not check the per-file contents beyond API metadata, because I did not stream the files. The notebook's cell 4 output (0 units tables) agrees with the asset-level `variableMeasured` I retrieved.
