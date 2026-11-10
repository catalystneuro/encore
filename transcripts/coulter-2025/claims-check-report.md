## Coulter 2025 claims check

**Checker result:** `claims/coulter-2025.yaml: 35 claims, 35 quotes, 54 statistical values, 3 problems`. The three problems are `VALUE NOT FOUND` for 3.9e-11, 3.6e-11 and 1.3e-11. The extracted text garbles their minus signs ("e�11"). I read them in the text and they are the paper's values.

**Changes, by claim:**
- **fig3b-trajectory-fraction:** I replaced the quote. The old one used "..." to join "65%–75% of detected representations" to "were sequential trajectories", which misstates the paper. The new quote is the 1%–4% sentence.
- **fig6e-target-assemblies-at-detection:**
  - Added the two rat 1 p-values from Table S1 (1.6e-4 and 2.8e-7).
  - The session set now drops the Figure 6 sessions that Data inclusion lists as missing.
  - How activity is taken at detection and at random times is now marked as a reading, because the paper does not define it.
- **fig6g-target-vs-nontarget-outside-detection:** The p-values were labelled "1 rat", "2 rats" and "2 rats, second". They are now tied to rats from Table S1: rat 1 0.005, rat 6 0.40, rat 4 0.45, and rats 2, 3 and 5 below 0.001.
- **fig7c-swr-target-no-consistent-increase:** Added the five non-significant per-rat p-values from Table S1.
- **figs6d-no-consistent-remapping:** The statement now gives the legend's split: 3 rats center port above target, 2 rats target above center port.
- **figs6ef-similarity-to-exploration:** Which arm visits Figure S6E uses is now named as open. Its legend says only "exploration arm visit".
- **fig7b-swr-fraction:** Added a session reading with no reward selection, since the Figure 7B legend names none.
- **figs7c-multiunit-peak:** The 10 ms rate bin and the 30 ms peak window were stated as fixed choices. They are now readings, with 6 ms bins as the alternative bin.

The other claims match the paper: statements, sources, p-values, Table S1 n's, the 148-session total, and the tolerances from widening each range by 10%. The main findings are covered, and nothing comes from outside the paper.

**Still open (recorded in `checks`):**
- I could not check the details cited from the analysis code repository (bin indices, notebook cells, the mixed-model form, the assembly code), because the code is not available here.
- No claim covers decoding accuracy during movement (Figure 1B, Figure S2C), because the paper gives no number for it.

**Ready:** yes. The `checks` entry is added with `ready: true`. Nothing was committed.
