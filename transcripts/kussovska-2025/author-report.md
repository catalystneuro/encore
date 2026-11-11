I've finished steps 1 to 6 of the Author protocol for kussovska-2025. The entry passes `python tools/entry.py all` in a clean environment (0 errors, notebook ran in 19.6 min), and the handover is built in `executed/kussovska-2025/handover/`. Nothing is committed.

## 1. Outcomes (45 claims: 27 reproduced, 9 partially reproduced, 6 not reproduced, 3 blocked)

| Claim | Outcome |
|---|---|
| units-by-region, behavior-accuracy, fig1c-accuracy-load1-vs-load3, behavior-rt, rt-in-vs-out-memory, rt-correct-vs-incorrect | reproduced |
| fig1e-load-modulated-neurons | reproduced |
| fig1f-rt-modulation-not-significant | not reproduced |
| concept-cells-count, fig2ab, fig2c, ext1bc, fig2d, ext1de | reproduced |
| fig2e-maintenance-decoding-amy-mtl | reproduced |
| ext1f-maintenance-decoding-load2 | partially reproduced |
| fig2f-bin-width-decoding | partially reproduced |
| fig2f-bin-width-pairwise | not reproduced |
| ext1g-bin-width-load2 | reproduced |
| fig3abc, fig3d, fig3h (dPCA) | blocked, too_large (one split takes about 45 to 50 s, so 100 splits take about 75 to 82 min, over the 60 min limit) |
| fig4c, fig4d, ext2 | reproduced (each under one of the readings the criterion names; marked assumed) |
| fig4-acg-group-differences, fig4f, fig4hj | partially reproduced |
| acg-fit-yield, fig5c, fig5dfh, fig5gh, fig5kl | reproduced |
| supp4-rodent-validation | reproduced, using the feature table shipped with the paper's code (`data: elsewhere`) |
| fig6ab, fig6cd, fig6e, fig6j | partially reproduced |
| ext5bd, fig6kl, ext5ij | reproduced |
| fig6f, fig6gh, ext5gh, fig6i | not reproduced |

## 2. Dataset, assumptions, questions

**Version.** I pinned 0.231213.2047, the version the paper cites. All published versions hold the same 41 assets. The 21 Sternberg files hold exactly the paper's 902 units with its region counts. The code's trial tables link to the dataset's trials exactly.

**What was found:**
- The paper says 16 participants did 135 trials and 5 did 108. The data have 15 and 6.
- One trial in subject 9 has a maintenance of 0 s.
- The first encoding image lasts 1.0, 1.2, 1.5 or 2.5 s depending on the session; the paper does not say.
- Fixation runs about 0.91 to 1.2 s in most sessions, against the paper's 0.9 to 1.0 s.
- The Fig. 1f percentages come out exactly only with the code's predictor, which gives every neuron subject 1's reaction times. With each trial's own reaction time, three regions are significant, which is why that claim is not reproduced.
- The code splits maintenance into M1 to M3 by thirds of the trials, not by 1 s windows as the Methods say.
- What the code reports as CV2 is the plain coefficient of variation.
- The paper does not say how the matched trial sets were chosen.
- The clock could not be checked by contrast in 7 sessions (subjects 1, 3, 6, 10, 17, 19, 20), which have no image-selective neurons.

**Assumptions:**
- For cell types and ACG groups downstream, I used every spike of each unit (reading a of acg-fit-yield). The code's shipped table matches this exactly in firing rate and ISI CV. This was my choice, so dependent outcomes are marked assumed.
- Concept cells use the code's bootstrap with seed 0, a standard choice since the code sets no seed. This set shares 57 of 58 cells with the code's list.
- My Python port of the ACG fit gives 317 well-fit units against the paper's 294, and 102 pyramidal cells against 92.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- Which peak rule detects bursts, what threshold the surrogates use, and the spacing (70 or 140 ms).
- What the "label-shuffled null" of Fig. 6a,b is.
- Which decay constants are compared in Extended Data Fig. 5g,h.
- How cluster extent is measured, and whether the binomial test is one- or two-sided.

I asked a reader no questions.

## 3. Where the protocol was unclear
1. When a criterion only defines "reproduced" and the result holds in part, the protocol does not say how to judge it. I used the criterion's own partial clause where it has one (so fig2f-pairwise is not reproduced), and otherwise the general definition.
2. For `measured`, the first reading listed matched for only 2 of 10 seeds in concept-cells-count. I recorded the reading that matched for every seed, and said so.
3. When an upstream claim has several readings (which spikes feed the ACG), the protocol does not say whether downstream claims must run each one. I picked one, stated it as an assumption, and marked those outcomes assumed.
4. There is no category for outside inputs used only for comparison (the code's concept-cell list and ACG table). I listed them under `inputs` and said no outcome rests on them.
5. The example entry uses bold labels in its notebook header, but the instructions forbid bold. I removed them.
6. The protocol's advice to develop on a subset does not say to run the full notebook cell by cell with saved progress. Not doing so cost me a run (see 4).

## 4. Runtime and failures
- About 2 h 55 min in total. The final notebook takes 19.6 min.
- My first full development run was killed at 66 min with nothing saved. The cause was a slow two-sided binomial test in the cross-temporal shuffles; I replaced it with a lookup table and switched to a runner that saves after each cell.
- My fast SVM wrapper had a bug: it gave wrong predictions when labels were not coded 0 to k-1. I fixed it before the final run and checked it against sklearn under both trial readings. It had made the within-participant and rank-aligned decoding look below chance.
