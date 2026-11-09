The claims file for 002035 is fit for an attempt (`ready: true`), after eight corrections. One gap: I couldn't open the figures, because the PDF can't be rendered in this environment.

**Checker result, before and after my edits:** `claims/002035/10.3233-jad-220538.yaml: 33 claims, 33 quotes, 33 statistical values, 0 problems`

**Changes, by claim**
- **fig1a-a1-onset-p21:** the criterion now notes that the Fig. 1A legend says cells were "absent at age p14", while the Results report one p14 neuron. The Results are followed.
- **fig1c-a1-cells-age:** "means rise from p14 to p90" was vague. It now requires the p90 mean to be above the p14 and p21 means, and allows a fall after p90, since the Results (Subiculum section) report a modest decrease in A1 at the oldest ages.
- **fig1e-l5a-peak:** the source now cites the Fig. 1E legend, which is where the "L5B by p30" part comes from.
- **mgb-cells-rare:** the paper says "no more than 1-2" cells per mouse, but the file expected exactly 2, so a maximum of 1 would have failed. It is now the range 1 to 2 widened by 10% of each bound (value 1.55, tolerance 0.65).
- **fig5b-ic-plaques-age:** the statement linked the whole-IC value of 106.2 plaques/mm2 to "each subregion". It is reworded: density varies with age overall and in each subregion, with a peak of 106.2 for the whole IC.
- **ic-no-sex:** the paper doesn't say which mice entered the test. The criterion now names two readings (p90 to p150, or all mice) and judges on p90 to p150, as the subiculum sex claim does.
- **fig7b-prnc-cells:** the Results say both giant reticulospinal neurons and smaller cells were seen at p14. The criterion now requires both types at p14, and gives two readings of "consistently by p21".
- **cells-before-plaques:** the expected tolerance (60 ± 6 days) contradicted the criterion's 45 to 70 days. It is now 57.5 ± 12.5. Two readings of "first age" are named (any mouse, or most mice), because the paper puts A1 onset at p21 despite the one cell at p14.

**Still open**
- **Figure readings not checked:** "Fig. 5B shows none at p60", "Fig. 5C is labelled all ages", and the "all layers"/"all ages" labels on Figs. 1C, 1D and 2B. The text supports each claim without them.
- **Sample for ic-cells-subregion:** the opening comment works out sample sizes from the paper's reported effect sizes. Most are consistent, but the two Mann-Whitney pairs for IC cells by subregion fit neither 61 nor 24 mice per group, so this claim's sample stays open.
- **fig1g-dapi-layers:** it records the Results' corrected threshold, p < 0.007, as the bound on the pairwise tests. I kept it, because the Results say every listed pair passed it.

Every main finding has a claim, and none comes from outside the paper. The `checks` entry is added at the end of the file. Nothing is committed.
