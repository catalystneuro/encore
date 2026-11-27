I've made the round-1 revision: the record, notebook, helpers, README and questions file are updated. The entry re-ran cleanly with `python tools/entry.py all entries/jarzebowski-2026` (0 check errors, 19 min), and every conclusion matches the new numbers. Nothing is committed.

**Outcomes changed** (now 22 reproduced, 4 partially reproduced, 5 not reproduced)
- **fig3b**: partially reproduced → reproduced, and no longer seed-sensitive. I re-estimated the omission probability from 800 runs per gain instead of 80, because 80 runs cannot measure a probability near 0.03. It now rises 0 → 0.026 → 0.948, and all five seeds meet the criterion. The verifier gave reproduced too.
- **fig6b and fig6c**: not reproduced → partially reproduced, resting on an assumption. They now use both spontaneous blocks, as the verifier suggested; the reasons are in the deviation. Against the 10 s block alone (block 1, the one used before), both claims fail, and the notebook shows that variant.
- **fig5c-fsb-highest**: partially reproduced → reproduced. The verifier had agreed with partially reproduced; round 2 reviews this change. The verifier asked for the other cell selections. On two of the 16 under O9 (b), one analysis reading puts both intercepts inside the paper's CIs, but only by 0.0002 to 0.0003, and the record says so.
- **figs1-novel-firing-rate-unchanged**: still not reproduced, but no longer an assumption. The O9 (a) result (p = 0.059) came from a fit that had not converged. Refitted, it gives p = 0.015, so the claim fails under both O9 readings and all 16 selections.

**Outcome kept despite the verifier's disagreement**
- **fig2d** stays reproduced, with a new test. I resampled the largest step at 1 nS with 4000 runs: no single 1 nS step carries more than 0.43 of the change, so the large 5 nS steps the verifier saw are sampling noise, not a jump. The disagreement is recorded.

**What I added or corrected**
- **Model fits:** fits that don't converge are refitted with other optimizers, and every table names the one used. All fits in the tables now converge.
- **Data check:** it now prints:
  - the timing of every block: block 1 starts 18 to 29 s after the task, except in one wild-type session;
  - optotagged units by genotype and O3 reading;
  - the repetition ordinals around an omission: omitted flashes don't advance the count;
  - running state per session: 26 of the 104 O9 (b) sessions have no stationary Repetition 1 presentation.
- **Cell selections:** a new section runs every intercept claim on all 16 O1–O3 selections, under both O9 readings, and again without the 10 sessions with a weak clock check. Only fig5c-fsb-highest depends on the selection.
- **Model outputs:**
  - Noise-free traces for fig2a: the release spike fires for L4 up to 10 nS and is silent from 12 nS.
  - Late spikes are now counted at every L4 for model-positive.
  - 800-run latencies for fig3c.
  - A note on how much of fig4d's result comes from L5 IT alone.
- **Questions file:** three questions for a reader: which spontaneous block O5 means, how the Figure 7 cell counts arise, and how "weaker" is measured in fig2a.
- **Findings:** I updated findings 3, 5, 6 and 9 and added a twelfth, on the Figure 7 cell counts.
- **Verification record:** round 1 is recorded for all 31 claims.

**Not done**
- I couldn't check the tests for Figures S1 and S2 against the paper, because their legends are not in the text.
- No finding is rated critical, so there was nothing for the verifier to review there.
