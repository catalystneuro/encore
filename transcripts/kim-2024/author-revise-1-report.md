I've revised the attempt in reply to the round-1 report and re-run the entry. `entry.py all` passes with 0 errors and the notebook runs in 137 s. Every conclusion matches the new outputs. Nothing is committed.

**Outcome changed**
- **figs12a-sag-higher** goes from partially reproduced to **not reproduced**, still marked as resting on an assumption. I took the verifier's view:
  - The criterion needs both APP and AV above ALL, and AV fails under every reading on all 44 cells (p = 0.087; mixed model p = 0.24).
  - The APP half only holds under the parametric tests. It fails under the rank tests (Kruskal-Wallis p = 0.12, Mann-Whitney p = 0.10) and when the next unsaturated step replaces the saturated ones (p = 0.053).

The other 30 outcomes are unchanged, and the verifier agreed with all of them. The new numbers change none of them.

**Added or corrected, by point in the report**
- **Non-parametric tests (problem 1):** every results table now shows the Mann-Whitney p for each pair beside the Kruskal-Wallis and Shapiro-Wilk p, and each conclusion says whether the rank tests agree. For figs12-other-features-shared the Kruskal-Wallis count is 7 of 10 on all cells and 6 of 10 without the `_FL` cells, still more than half.
- **Question for a reader:** the claims file's tests leave out the paper's rule of switching to non-parametric tests when normality fails. I added this to `questions/001544.yaml` and did not change the claim.
- **Saturated sag traces (problem 2):**
  - The notebook now runs the paper's code's saturation test on every -60 pA sweep. It never fires: it always counts 1 against a limit of 1000.
  - It plots the five saturated sweeps.
  - It shows that -105.62 mV is not a floor in every file, since one other file has a single sample at -112.88 mV.
  - A new variant leaves the five cells out: APP is then above ALL (p = 0.016) and AV still is not (p = 0.092).
- **Small-sample p for the mixed model (problem 3):** pairs are also tested against t on mice minus 3 degrees of freedom. The downstroke result in figs12-app-differs-from-all is now called marginal (p = 0.039 on all cells, 0.057 without the `_FL` cells); the outcome stays reproduced.
- **Membrane potential (problem 4):** the conclusion and notes now say that this measure is taken under the DC holding current and may not be what Figure 6G plots. A new data-check table shows the injected current is 0 before the step in every file. The 0 pA sweep sits at the same level as the pre-step baseline (-61.2 to -76.9 mV), so no sweep is free of the holding current.
- **20% change rule (problem 5):** a per-sweep table of test-pulse resistance and pre-step potential is added. Reading the rule as the largest change from the first sweep would remove 30 of 44 cells, so that reading cannot be the paper's rule.
- **Cell counts (problem 6):** any 8 of the 11 home-cage mice hold 14 to 20 cells, never 21. So the paper's 21 cells from 8 mice cannot be the deposited cells less some whole mice. This is now in the notebook and in the `selection_undocumented` finding.
- **AHP window (problem 7):** the shortened 100 ms window of reading (a) is now stated in the helper. The two affected cells are listed, and their minima fall inside the shortened window.
- **Record:**
  - Notes and deviations updated for all seven tested claims, and the `code_mismatch` finding and the finding on the five saturated recordings corrected.
  - Round 1 recorded under `verifications`: 31 results with the verifier's reasons and my responses.
  - The README's sag row changed to "Not reproduced".

**Not done**
- I could not settle which three home-cage cells the paper excluded, or provide series resistance. Neither is in the files; the existing question to the paper's authors stands.
- `git status` lists some untracked entries (`.bashrc`, `scripts` and others). They are sandbox device mounts created when the run started, not files I wrote, so I left them alone.
