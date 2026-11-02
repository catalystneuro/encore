I've finished the author steps 1 to 5 and the handover (step 6). Of the 27 claims, 18 are reproduced, 1 partially, 1 not, and the 7 Figure 2 claims are blocked. `entry.py check` reports 0 errors and `entry.py all` passes; the notebook runs in 95 s.

The new files are:
- `entries/001249-ishii-2025/` (notebook, `mpoa.py`, README, `entry.yaml`, requirements and lock)
- `attempts/001249-ishii-2025-01.yaml`
- `questions/001249.yaml`

The handover package is in `executed/001249-ishii-2025/handover/`. Nothing is committed.

## 1. Outcomes

| Claim | Data | Outcome |
|---|---|---|
| fig2-density-link, fig2c, fig2ei, fig2-mpn-higher, fig2f, fig2gh, fig2s (7 claims) | dandiset | blocked, `too_large` |
| fig1gh, fig1i, fig1jm, fig1nt, fig1s1, fig1s2 | Figshare | reproduced |
| fig3d, fig3i, fig3jm | Figshare | reproduced |
| fig4h, fig4i, fig5, fig5c, fig6k | Figshare | reproduced |
| fig6c-decay-length | Figshare | not reproduced |
| fig7fg-activation-suppresses | Figshare | partially reproduced |
| fig7kl, fig7s1, fig7s2, fig7s3 | Figshare | reproduced |

- **fig6c:** neither of the claims file's two readings gives Vgat a longer decay. A third reading, from the peak to the first sample below 0, matches the deposited values for 207 of 219 cells and gives the paper's result (t = 3.037, p = 0.0027).
- **fig7fg:** with the rank-sum test the legend names (the claims file's main reading), the consummatory group's transitions also drop (corrected p = 0.016), so "only post-ejaculatory" fails. The code's paired signed-rank test gives the paper's values exactly.
- **Figure 2:** the measured streaming rate was 56 MB/s, so reading the TRAP channels once would take 205 min and both channels 410 min. That is before any registration or segmentation, and the ilastik classifier the segmentation needs is not deposited. Nothing past the data check was run.

## 2. The dataset, assumptions and questions

**Version.** I pinned 0.241109.2357, the only published version; the paper cites none. It holds 14 brains: Sniff 4, Mount 5, Ejaculation 5.

**Dandiset findings:**
- Each file holds only two raw volumes (TRAP and background), uint16, uncompressed and unchunked: 1.38 TB in all. There is no registration, no cell counts and no atlas.
- The z planes are stored as ImageSeries frames with a "rate" of 4.0, which is the z step. There is no voxel size, no channel description, and the unit is "lumen".
- The consummatory (Mount) brains have session dates of 2024-02-07, a year after the others, and lower TRAP intensities. This could be a separate imaging batch.
- All 14 brains are distinct; there are no duplicate deposits.

**Figshare findings:**
- `Time_in_Isolation_zone_per_10min` actually holds the mean visit duration.
- In the Figure 7 table, `Average_Isolation_zone_duration` is in frames for three of the four groups.
- The arrays named `*_norm_zscore_*` are rescaled and do not give the table's magnitudes. Only the ejaculation trace can be recomputed per the Methods; the other five behaviors' magnitudes come from the table.
- Clustering: the Methods say 55 neighbours and silhouette 0.405; the code and the deposited labels are 30 neighbours and 0.474.
- Figure 5 counts: the Results say 177/46, the legend and data 178/48.
- Figure 7-S1G reports paired-test t values labelled with unpaired degrees of freedom and doubled p. The post-ejaculatory group has 15 mice against the legend's 14, and its ISH panel mixes eYFP and hM3Dq mice although the legend names only hM3Dq.
- The HCR Vgat and Vglut2 populations silently exclude cells called both; this is not stated in the paper.

**Assumptions.** None of the outcomes is marked `assumed`. Where the Methods were silent and the code settled it (exclusive HCR populations), I followed the code and ran the inclusive reading too; both give the same outcome.

**Question for the paper's authors** (`methods_unavailable` finding): how is the decay length defined, from the peak?

**Question to a reader** (`questions/001249.yaml`): should fig6c's readings include the from-the-peak reading? The Results' wording, "the time for the increased calcium signal to return to baseline", supports it.

## 3. Where the protocol was unclear

1. **`data: elsewhere` covers most of the paper here.** The claims file sends 20 of 27 claims to Figshare, which reads as a dandiset finding although the dandiset only lacks them by design. I tested them and listed Figshare under `inputs`.
2. **A criterion's "main reading" against the paper's own numbers.** The claims file made the legend's rank-sum test the main reading. The reported p-values (0.03125 for 8 mice) can only come from the signed-rank test. I kept the claims file's main reading as decisive and asked no question, since the reader followed the "Methods first" rule. A test the paper's numbers rule out deserves a rule.
3. **A criterion's readings that miss the reading matching the authors' values (fig6c).** The protocol forbids adding readings, so the result is not reproduced plus a question to the reader. I showed the third reading as a labelled variant.
4. **`too_large` when a single transfer exceeds the limit.** It is unclear whether "how far it got" asks for a partial run, for example one brain. I ran only the data check and the timing, since even one brain's registration needs the undeposited classifier.
5. **No partial rule in some criteria.** Some criteria give only a "reproduced" rule (fig7fg). I used the protocol's general definition of partially reproduced.

## 4. Runtime and failures

The run took about 37 minutes (11:14 to 11:51 UTC). Nothing failed. The streaming rate in the record (56.2 MB/s) is from the final executed copy; it varies between runs. Untracked character-device files (`.bashrc`, `.gitconfig`, `scripts` and others) in the repository root date from 11:12, before this run started, and appear to be sandbox mounts; I left them alone.
