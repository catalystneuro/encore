I wrote `claims/brudner-2026.yaml` with 22 claims. `tools/claims_check.py` reports 22 claims, 22 quotes, 4 statistical values and 0 problems. Nothing is committed.

**Text read.** The version of record (PNAS 123(29), published 14 July 2026) and its SI Appendix: Supplementary Methods, the legends of Figs. S1 to S5 and of Movies S1 and S2. Nothing the claims need is missing from the text. I opened PDF pages only to read bar heights (Figs. 2, 4, 5 and S5) and the upwind-turn formula of the SI agent model, which the text garbles.

**Code read.** github.com/emonetlab/GradientMotionMultiplePlumes at commit effc7b0. It holds the Fig. 5E/F analysis, written to run on this dandiset, plus its published result tables. It also holds the Fig. 1 cue maps, the Fig. 2 models with their plotted values, and a re-implementation of the Fig. 3 training.

**Claims.**
- All 22 have quotes and criteria.
- Statistics: 4 entries in 3 claims (Fig. 4 z-tests, P < 0.001; Fig. 5E coefficients, P < 0.005 and P < 0.01; Fig. S5H, P < 0.005).
- Data:
  - 7 use the dandiset alone: Fig. 2C and 2E (the complex plume), and Figs. 5E, 5F, S5C and the intensity-bias finding (behaviour). The S1 resolution claim (Fig. S1F, G) is also on the complex plume.
  - 13 need the smooth plume from Dryad (doi:10.5061/dryad.g27mq71).
  - 2 (Fig. 2B, 2D) use the smooth plume only.

**Details left open, with the readings named.**
- **Fig. 5E/F filters.** The complex-plume heading window is 160 to 200° in the Methods and 150 to 210° in the code. The code alone drops turns within 15 mm of the arena edges. The Methods z-score the cue signals but the code fits them as stored, so the readings are as stored, z-scored over the plume, or z-scored per trajectory. "Not significant" is read as p ≥ 0.05 or p ≥ 0.01.
- **Fig. 1 and S1 comparisons.**
  - The paper does not say how the z-score maps are compared: mean |z| over the plume mask, over the whole frame, or its 95th percentile.
  - The mask's "bias" could be subtracted from the threshold or be a percentage of it.
  - The S1 index could have its intensity rescaling applied to all five movies or only the freestream ones.
  - The code has two timing versions of the smooth movie.
  - For Fig. S1F/G, the reference map and the correlation threshold are not given (r ≥ 0.5 or r ≥ 0.8), and the S1 legend's delays (33 to 500 ms) do not match a 60 Hz movie.
- **Figs. 2 and 3 models.** The threshold for valid sampling regions and how train and test samples are split are not given. Training settings differ: 1e-4, batch 500 and 500 epochs in the SI against the code's archived values. How response strength is measured, and what "symmetrized filters" means, are not defined.
- **Fig. 4 agents.** The start box is 112 mm wide in the figure legend and ±83 mm in the SI. It is not said whether the complex movie loops over the 90 s runs.
- **Fig. S5.** It is not said which turns are pooled for the turn-angle medians or how displacement is measured. For the cue-smoothing agents, the paper does not say how the cues are computed or what test compares the weights.

**Missing that claims needed.**
- No simulation code or trained networks for Fig. 4, S4 and S5F to H.
- The training arrays, masks and checkpoints for Figs. 2 and 3 were not deposited.
- There is no code for Fig. S1.
- The paper gives no counts of flies, trajectories or turns.
- Most values in Figs. 2, 4 and 5 are printed nowhere in the text. I took them from the code's tables or read them off the bars.
- The log-likelihood levels in Fig. S5D/E (about −0.596 and −0.685) disagree with the code's table (−0.576 and −0.676). Fig. 5F agrees with the table.
