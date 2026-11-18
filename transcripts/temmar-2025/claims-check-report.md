The file is fit for an attempt (`ready: true`). I made four corrections; the rest is open but labelled in the file.

**Checker result:** `claims/temmar-2025.yaml: 24 claims, 24 quotes, 0 statistical values, 0 problems` (the same before and after my edits).

I read the main text, the supplement and the paper's code (`chesteklab/LINK_dataset` at the cited commit). The code details the criteria rely on are in the repository as described. These include the 0.25 SBP and ×50 TCR scales, tuning lags of 0 to 10 bins, ridge regression with no input scaler, the 74-trial test set, the 2-SD onset variant, the curve-fit starting values, and the fine-tuning sample counts and iterations. The paper reports no statistical tests, and the file records none.

**Changes, by claim:**
- **fig2b-active-channels-decrease:** the criterion said the RD session is used on single-session days. The code uses CO when it exists and otherwise RD, so it now says the day's only session is used.
- **fig3cd-tuning-stable:** I narrowed the statement to tuning angle. Section 4.2 says strengths look consistent, but the Figure 3 legend and the Discussion say strength varied, and the criterion only tested angle. The criterion now names this inconsistency.
- **suppc1-shuffle-baseline:** the paper doesn't say what is shuffled for decoders that use time history, and the choice could change the R2. I added two readings: shuffle the raw bins before the history windows are built, or shuffle whole input samples.
- **fig5b-finetune:** the criterion followed the code, which refits input normalization on each fine-tuning day, without saying so. Appendix C.1 says normalization for Figure 5 was held at "the training day", which for a fine-tuned decoder could mean the seed day or the latest fine-tuning day. Both readings are now named and both are to be run.

**Still open (recorded under `checks`):**
- **figs2-throughput-improves:** the throughput formula is only cited to Nason et al., which I did not read. The readings in the file stand.
- **Claims the paper judges by eye** (fig2a-irregular-shifts, fig2d, fig2e, fig3b, fig3d, fig3e): the pass/fail rules are choices the paper doesn't make. They are labelled as such, but an author could dispute them.
- **figs4 and figs5:** the code for Figures S4 and S5 is not in the repository. What the line is fit to, and the unit of SBP, remain readings.
- **fig5a-multiday-short-term:** the multi-day trainer depends on an outside library (`neuraldecoding`) that isn't in the repository. I could not check the code variant's details (90/10 split, no noise).

Every main finding has a claim, and every claim comes from this paper.
