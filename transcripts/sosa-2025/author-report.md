I've finished the author steps and run the handover. The entry passes its checks with 0 errors and the full notebook ran clean from a fresh environment in 39 minutes. Of 50 claims, 27 are reproduced, 11 partially reproduced, 5 not reproduced and 7 blocked. Nothing is committed.

The biggest finding: the dataset version the paper cites (0.250406.0045) can't be used. In it, every file of a mouse carries the behaviour of one and the same session (11 distinct behaviour series across 152 files), so imaging and behaviour can't be aligned. I pinned the latest version, 0.251124.0550, where this is fixed, and the notebook header explains why. The protocol says to pin the cited version, so this is a departure you may want to confirm.

**1. Outcomes per claim**

| Outcome | Claims |
|---|---|
| Reproduced (27) | fig1h (reading b), ed2cd, ed2f, fig2e, fig2h, fig2eg, fig2i, ed2n, ed2pq, fig4c (75/77), fig4f (76/77), fig4i (62/77), ed5f, fig4m, fig4no, fig4p (reading a), fig4qr, fig5b, fig5h, fig5i, fig5jkl, ed6a, ed6-across-day-drift, ed8k, ed8df, ed3mo, ed3p |
| Partially reproduced (11) | place-cell-fraction, remap-category-fractions, rr-cell-fractions, ed2jl, ed2m, ed5a, fig4j, ed4hij, ed4l, ed7, fig6e |
| Not reproduced (5) | fig5d, fig5f, ed6c, ed3d, ed3fg |
| Blocked (7) | fig3b, fig3c, glm-well-fit-cells, fig7de (too_large); fig8e, ed10, ed5-teleport-fractions (other: not attempted in the run's time) |

**2. Dataset, assumptions, questions**

What the dataset holds and lacks:
- **Holds:** the 11 switch mice, 152 sessions; trial counts, scene names, the 81 lick-sensor error trials and the sessions imaged through the teleport all agree with the paper.
- **The files' "Deconvolved" series is not the paper's signal.** It correlates 0.47 (median) with OASIS run on dF/F. I rebuilt dF/F and the deconvolved activity from the raw fluorescence and neuropil, using the paper's code defaults for values the Methods leave out.
- **Even so, too many place cells.** 60% of cells are place cells here against the paper's 48.5%, so pooled cell counts run 13 to 50% above the paper's, though most fractions and every directional test agree.
- **Missing:** cross-day ROI matching, depth (z-stack) estimates, omission labels, and the 3 fixed-condition mice.
- **Metadata errors:** in the ROI masks, "x" indexes image rows. `reward_zone` is described as binary but takes values 0 to 6.

Assumptions (marked `assumed: true` on the affected outcomes):
- I matched cells across days myself, by IoU after rigidly aligning the days' mean images. About 59% of cells match.
- Omissions are unrewarded trials with licks in the zone. This gives exactly the paper's per-mouse day counts.
- Place fields use 10 cm binned events instead of the raw events the Methods name.
- For ed4hij and ed4l I chose which pre- or post-switch peak to use; the legends don't say.

There are three `methods_unavailable` questions for the paper's authors in the record:
- the OASIS time constant and the shuffle details that live in the unpublished TwoPUtils package;
- how cells were registered across days and how the matching threshold was chosen;
- how the active-trial threshold for place fields is defined.

I asked a reader no questions.

**3. Where the protocol was unclear or missing something**
1. It has no rule for a cited version that is broken. I pinned the latest version, said why in the header, and recorded it as a deviation on every claim and as a finding.
2. Its only time-related block reason is `too_large`. For claims I skipped for time that weren't computationally too large, I used `other` and said so.
3. "Fix every random seed" isn't enough for affinewarp, whose random search runs in parallel numba threads. Seeding alone didn't make it repeat, so I seeded numba and ran the warp on one thread.
4. When a criterion is met but a listed expected count is out of tolerance, the protocol doesn't say what happens. I followed each criterion as written: reproduced where it judges on tests or percentages alone, partial where it includes the counts (ed2jl).
5. It forbids numbers from preparatory runs in the record. So for fig6e and ed8k I said only that the earlier, unseeded runs varied, without giving their counts.
6. After the run I removed bold from markdown cells only. I copied those markdown changes into the executed notebook instead of re-running, since the code cells are identical; the protocol doesn't cover this.
7. The ten-minute target can't be met for a 92 GB dataset; the run took 39 minutes, under the 60-minute limit.

**4. Runtime and failures**
- About 3 h 20 min of wall time; two full notebook runs of 38 and 39 minutes.
- Fixed along the way:
  - the ROI-mask row/column bug, which broke the cross-day matching;
  - affinewarp failing with scikit-learn 1.6, so I pinned scikit-learn below 1.6;
  - the first executed run's time-warp results not repeating, which needed the second full run.

Files are in `entries/001361-sosa-2025/` and `attempts/001361-sosa-2025-01.yaml`.
