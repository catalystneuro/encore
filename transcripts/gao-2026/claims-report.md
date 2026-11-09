I wrote `claims/001683/10.1109-tnsre.2025.3644273.yaml`. The quote checker passes with 0 problems. The earlier run stopped because the supplement was missing; it is now under `paper/`, so this run could write the claims.

**Text read**
- The NIH author manuscript (PMC12848950, from Europe PMC): main text, Methods, Results, Discussion and the legends of Figs. 1 to 6.
- The supplement (supp1-3644273, 8 pages): the ex-vivo pressure scan, the target confirmation procedure, and Figs. S1 to S7. I looked at Figs. S4, S5 and S7 as images, by rendering those pages of the supplement PDF.
- The paper links no code, so I read none.

**Claims:** 22 in all.
- 21 have quotes. One (`fig5b-tfus-evoked-potentials`) is marked inferred, because only the Fig. 5B legend and a passing phrase in the Results support it.
- 20 claims carry statistics. Every one is a bound, mostly two-way ANOVA with Bonferroni post hoc tests; Fig. S5 adds one-sample t-tests.
- All 22 have criteria.
- 4 have expected values: 22 numbers in all, the percent changes of Fig. 3A to 3C, each with a 10% tolerance.

**Details the paper leaves open, and the readings named.** Shared methods M1 to M6 are defined in the opening comment, and the criteria cite them.
- **Seizure labels (M1):** the threshold was set by hand, and the paper does not say which ICA components were removed. If the dataset holds the paper's own labels, those are used. Otherwise I named three thresholds: 2, 3 and 5 times the median of the summed 30 to 80 Hz power, in 1 s windows, on CAR-referenced EEG without ICA. A claim's outcome must be the same under all three.
- **Statistics (M3):** ordinary two-way ANOVA, or repeated measures on time block. The Bonferroni correction is applied either within each set of comparisons or across all of them together.
- **Percent change (M4):** the ratio of the group means, or the mean of each rat's own change.
- **Power and asymmetry index (M5):**
  - Segment analysed: the whole time block, or the seizure periods only.
  - Total power: 3 to 300 Hz, or up to Nyquist.
  - Normalizing the asymmetry index: dividing by the group's baseline, or subtracting it. When the baseline index is negative, "increased" means opposite things under the two.
- **Phase lag index (M6):** the change is a difference or a ratio. It is computed per trial and averaged, or pooled over all trials; and per seizure, or over the seizures joined together.
- **Per-claim readings:**
  - Which hemisphere is meant (Fig. 3A between groups, Fig. 4C).
  - What "sham" means in Fig. 2F: the condition block or the baseline block.
  - The test unit in Fig. 2C: one seizure or one rat.
  - Which comparisons "significantly decreased" covers in Fig. 3B.
  - Fig. 5B: the onsets for the sham recording, the channel, and the test at each time point.
  - The windows meant by "during the tFUS conditions" (Fig. 5G to I).
  - Which rats, and which pre-4-AP recording, Figs. S5 and S7 use.

**Missing from what was read**
- There is no PDF of the main paper. The significance marks and values drawn inside Figs. 2 to 6 could not be read, so the statistics record only the P < 0.05 levels given in the legends.
- The text does not list:
  - the EEG channels used for seizure labelling (encircled in Fig. 1A);
  - the S1 and non-S1 channel sets (drawn in Fig. 5A).
- The test behind the seizure against pre-4-AP comparison in Fig. S5 is not named.
- The paper contradicts itself on one point, noted in the file: the Methods give a 20 ms tFUS window, but the target confirmation bursts the evoked potentials come from last 67 ms. The windows are used as printed.
