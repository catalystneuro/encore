**Round 3 verification: Pelot et al. (2020), attempt pelot-2020-01**

The attempt record has 35 outcomes for the 35 claims in the claims file. Only one carries a `proposed` change: fascicles-larger-cervical.

| Claim | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| fascicles-larger-cervical | partially_reproduced (from reproduced) | Yes | — | See below. |

**Do the numbers derive from the data?** Yes.
- **Cell 62:** under Kenward-Roger on the observed REML information, cervical fascicles are larger in all three species. The Tukey p values are human 0.000021, pig 0.0552 and rat 0.0445. With the code's rat values they are 0.000032, 0.0599 and 0.0093. Either way two of three species are below 0.05, and the cell's own count prints "2 of 3".
- **Cells 53 and 54:** this test reproduces the paper's F values to within 0.38% and its p values to the digits printed, for all nine effects, using the code's rat values. Its degrees of freedom are within 1 of those the paper's (F, p) pairs imply: 23.3 against 23.0, 23.4 against 23.5, 19.3 against 19.4 and 18.5, 21.2 against 21.1, and 25.4 against 25.6. Kenward-Roger on the expected information is up to 5.1% off in F, with degrees of freedom up to twice the paper's.
- **Cell 18:** the test's code gives the exact split-plot F tests on a balanced design.

**Was the choice made to reach the result?** No.
- The test was chosen because it reproduces the paper's omnibus F and p, a reason independent of this claim. It also makes this claim's outcome worse, not better.
- It also gives the paper's other Tukey p values closely:
  - human against pig nerve diameter: 0.179 against 0.183 (cell 38);
  - cervical fascicle diameter, code's rat values: 0.00039, 0.727 and 0.149 against 0.0002, 0.727 and 0.1707 (cell 56);
  - subdiaphragmatic fascicle diameter, code's rat values: 0.306, 0.899 and 0.995 against 0.3049, 0.896 and 0.9947 (cell 59).
- This addresses my round-2 objection. The paper's implied degrees of freedom now support the assumption, which they did not for the expected-information test.

**Is the criterion applied as written?** Yes. The criterion reads "Tukey's HSD on the species by level groups of the model in fascicle-diameter-anova. Reproduced when each species has cervical larger with p < 0.05; partially reproduced for two species." Cell 62 runs Tukey over the six species by level cells of that model and finds two species with p < 0.05.

**Caveats, which do not change my agreement:**
1. **The within-species level contrasts are the one set of the paper's Tukey p values that the adopted test does not reproduce.**
   - The pig contrast has 3.74 degrees of freedom. The paper's pig p = 0.0009 would need 24.6 at this contrast's t of 4.77 (cell 62).
   - The rat p is 0.045, or 0.0093 with the code's values, against the paper's 0.0234.
   - So the pig failure at p = 0.055 sits close to the threshold, and the gap from the paper is unexplained. Four of the ten printed combinations of test and rat values give two species and six give three, so the outcome stays dependent on the test, which `assumed: true` already records.
2. **I did not recompute the studentized-range p from the printed t and degrees of freedom.** scipy is not available in my environment. The values in cell 62 are internally consistent with the cell's own solve for 24.6 degrees of freedom.
3. **The claims file's criterion follows the Methods text (the largest fascicle).** The paper's statistics come from the code's first-trace rule (cell 54). As in rounds 1 and 2, I am reporting this, not correcting it. Here the outcome is the same under both rules.
