I wrote `claims/crcns-hc-9/10.1523-jneurosci.5680-12.2013.yaml`, and `tools/claims_check.py` reports 0 problems: 26 claims, 26 quotes, 25 statistical values.

**Text read:** the version of record (journal PDF text), including Methods, Results, Discussion and the legends of Figures 1 to 13. The paper has no supplement and links no code, so no code was read. Nothing a claim needed was missing.

**What the dataset holds:** by its description, only the current-step firing recordings of three O-LM cells from Figure 7. Only claim `fig7a-olm-sag` uses them. The other 25 claims cover the paper's main findings from Figures 1, 4 to 6 and 8 to 12, plus a statement in the Methods.

**Counts:** 15 claims carry statistics (Wilcoxon, Kruskal-Wallis with Dunn, Mann-Whitney, Friedman with Dunn), 22 have expected values, and all 26 have criteria. Tolerances are the paper's standard errors, and counts get 0 or 1 cell.

**Comparison signs:** the text extraction prints =, <, > and ± as a replacement character, and I could not open the PDF pages here. So each p < or p > is read from what the sentence says ("significantly", "did not change", "similar"). The opening comment says this, and a later check against the PDF would be worthwhile.

**Details the paper leaves open, with the readings named:**
- **O-LM sag (`fig7a-olm-sag`):** the paper never defines a sag. The readings are (a) the relaxation during the -100 pA step is larger than 2 SD of baseline noise, or (b) a sag ratio of at least 0.1. Both are common choices, not the paper's, so the outcome rests on an assumption.
- **Dunn post hoc pairs (Figures 11 and 12):** the paper does not say which windows were compared. They are read as each window against prestimulus, with early against late shown as a variant.
- **Gabazine baseline window (`gabazine-baseline-firing`):** either 40 to 60 ms or 0 to 60 ms; both are run. The paper uses an unpaired Mann-Whitney test even though the gabazine cells are a subset of the control cells, so a paired test is shown as a variant.
- **Age correlation (`no-age-dependence`):** the test is not named. The readings are Pearson and Spearman.
- **Figure 11 counts (12 of 21 inhibited, 9 of 21 excited):** the paper drops "a few cases" with faster kinetics without giving a rule, so these counts may not be reproducible from the recordings alone.
- **Typo:** the paper prints "01.3 Hz", which is read as 1.3 Hz.

I did not commit anything.
