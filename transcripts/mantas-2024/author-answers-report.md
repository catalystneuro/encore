I took up all six answered questions. Two claims change outcome (fig6j and fig1b's MitoPark half); the other four keep theirs. The entry is locked, passes the check, runs from a clean environment in 329 s, and the handover package is built. Nothing is committed, and I have not verified my own work.

| Question | What the answer changed | Claim | Before | Now |
|---|---|---|---|---|
| 1. Which events are the "water drop touch" | Names the two readings already run: correct only, or every contact with a drop; empty-spout events excluded | fig3d-anxa1-ramp-to-touch | not reproduced | not reproduced |
| | | fig3e-dlight-dcp-ccp-reward | partially reproduced | partially reproduced |
| | | fig3fg-auc-change-from-baseline | blocked (methods underspecified) | blocked (methods underspecified) |
| 2. Which water drop recordings enter | Every recording with at least one event, as already run; the n used and a per-mouse summary are now shown | same three claims | as above | as above |
| 3. Evoked release: powers, unit, baseline | Two judged readings, all powers pooled per session (a) and each power alone (b); 1 s and 2 s baselines | figs2-evoked-da-dcp-ccp | reproduced | reproduced |
| 4. Reaching: grasp attempts and preferred limb | Names two event sets and two limb rules, all of which were run | fig6j-reaching-accuracy | blocked (methods underspecified) | partially reproduced |
| 5. Reaching: which days and which mice | Days 1 and 4 are the first and fourth training sessions; the main run is the mice recorded before the preprint | fig6j-reaching-accuracy | (same claim) | (same claim) |
| 6. RNA-seq: cMfn2KO counts and libraries | No deposit for the cMfn2KO counts; libraries summed per mouse; the MitoPark half is run and reported | fig1b-anxa1-downregulated-rnaseq | blocked (other), MitoPark counts not analysed | blocked (other), MitoPark half holds |

**Questions 1 and 2 (fig3d, fig3e, fig3fg).** The answers confirmed the readings already run, so no number changed. The notebook now shows the recordings used against the legend's counts: 15 against 10 for Anxa1, 8 against 4 for DAT, 21 against 13 for dLight-dCP and 15 against 11 for dLight-cCP. It also adds a per-mouse summary that is reported but not judged. fig3fg stays blocked because its two z-scorings still give different outcomes, and the answers do not address that.

**Question 3 (figs2).** It stays reproduced because reading (a), the first one the criterion lists, holds under every z-scoring, baseline and window (p = 0.0010 to 0.0043). Reading (b) compares 2 sessions against 2 at each power and holds at only 3 or 4 of the 5 powers. It fails at 2 mW under every combination, though dCP is above cCP in both mice at every power. A verifier could argue for partially reproduced on reading (b).

**Questions 4 and 5 (fig6j).** The main run has 17 mice: 8 controls, 4 TeTx and 5 Arch, which fits the paper's F(2,14).
- **What holds:** controls improve (Sidak p = 0.010) and exceed TeTx on day 4 (p = 0.0014), with no TeTx difference on day 1. The group by day interaction is significant (p = 0.034).
- **What fails:** Arch mice never fall below controls on day 4 in any of the eight readings (p = 0.044 to 0.34).
- **The legend's degrees of freedom:** choosing the preferred limb per session gives exactly the legend's (2, 14), but there the interaction just misses (p = 0.060).
- **All mice (variant):** every reading at 0.2 cm meets the criterion.

**Question 6 (fig1b).** I tested the MitoPark half on the GEO counts, which I've added to the attempt record as an outside input, pinned by md5.
- **DESeq2:** Anxa1 log2 fold change -1.02, FDR 2.9e-5.
- **edgeR:** -0.99, FDR 7.5e-4. This uses a Python port, because R isn't in the environment and the port lacks TMM normalisation, so I wrote that into the helper.
- **Each library as a sample:** both tools agree.

The claim stays blocked because the cMfn2KO counts are public nowhere. The deposit holds 5 MitoPark mice, not the 6 the earlier record said; I corrected that.

**New finding.** In the Arch cohort, all 17 day-1 reaching files, controls and the 2024 mice included, say the laser came on after the first reach. The Methods say it was off on day 1. The earlier finding blamed only the 2025 cohort, so I recorded this as a metadata error.

Every affected claim's notes in `attempts/001828-mantas-2024-01.yaml` say what the answer changed. The notebook, helper, README, entry description and lock file are updated; the new packages are pydeseq2 and inmoose.
