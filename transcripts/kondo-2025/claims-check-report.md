I checked the claims file for DANDI:001425 against the paper, made seven corrections in the four groups below, and it is ready for an attempt (`ready: true`).

**Checker result:** `claims/001425/10.1101-2025.02.03.631599.yaml: 22 claims, 22 quotes, 0 statistical values, 0 problems`. I ran it before and after my edits and got the same line both times.

Statements, quotes, sources and expected values all match the paper. The paper reports no statistical tests, so the file correctly records none. Every main finding has a claim, and none comes from outside this paper.

**Changes, by claim:**
- **training-breaks:** The criterion defined a break as a gap of two or more days, then listed one-day gaps as an open reading, which contradicts it. Which gaps count as breaks is now the open detail, with two readings: one or more days, or two or more days. Both come from the text. I also added which day-16 session to use for the 8 mice that had two sensory-mapping sessions: the first, which Figure 4 uses, or the last.
- **fig4d-visual-map, fig4d-tactile-map:** I removed the requirement that the result hold "in more than half of the mice". Nothing in the paper sets it; the finding rests on the map averaged over animals. The number of mice is now only reported.
- **figs2b-no-aberrant-transients:** I added which signal to use as an open detail: the corrected dF/F, or the uncorrected blue-channel ΔF/F. The legend says only ΔF/F, and the band-pass filter in the correction changes how large transients look.
- **The four fig6b claims (movement order, motor/somatosensory after reward, areas tracking the pupil, variability decrease):** The paper states these only for one example session that it does not identify ("at least in this session"). A failure across all sessions therefore cannot contradict it. When no reading holds, the claim is now blocked as `methods_underspecified` instead of being judged not reproduced.

**Still open (recorded in `checks`):**
- **fig6b-movement-order:** the baseline window and the 2 or 3 s.d. onset rule are not from the paper, and they could change the outcome.
- **fig3e-cluster-a-high-tpull:** cluster A is labelled as the cluster with the higher mean T_pull_final, so part of the test follows almost automatically from that label.
- **"Constant", "similar", "not observed" and "decrease":** the paper gives no test or bound for these words. The readings in the criteria are the file's own, run side by side, and the claim is blocked when they disagree.
- **fig4ab-landmark-validation, fig5abc-dlc-error:** the manual annotations these depend on are not described as deposited, so the claims are blocked unless they turn up.
- **Tables 1 to 4:** their contents are not in the text and there is no PDF, so session counts per type and keypoint names could not be checked.

Only the claims file was modified; nothing is committed.
