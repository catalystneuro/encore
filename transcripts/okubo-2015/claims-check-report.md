The file is ready for an attempt, with the open points below.

**Checker result:** `claims/okubo-2015.yaml: 42 claims, 42 quotes, 21 statistical values, 0 problems`, both before and after my edits.

**Changes, by claim:**
- **Header, model code:** the bout-onset run uses seed 1009 (code line 284), not 9038. The other model details in the header match the code: participation thresholds 12, 4, 2 and 4/6, iterations 992 and 2,500, and 130 and 600 for bout-onset.
- **counts-neurons-birds:** the 1,117 juvenile neurons are in Results paragraph 3, not 4.
- **fig1fg-rhythm-increases:** the total of rhythmic juvenile neurons was wrong. It is 3 + 70 + 356 + 298 = 727, not 729; tolerance now 72.7, and the quantity is labelled as a total.
- **ed1c-burst-width-rate:** the Methods do not name the post-hoc test, but the criterion used Dunn's test as if they did. It is now OPEN, with two readings: Dunn's test or rank-sum, each Bonferroni-corrected. Whether both measures carry significance stars is also now OPEN.
- **skipping-cycles:** the paper gives no rule for skipping cycles, so the rule is now marked OPEN. The two readings are kept.
- **fig4h-bird2-shared-early and ed4bd-shared-latency-other:** the cutoff of 0.95 for "r > 0.99" had no basis in the paper or the protocol. It is replaced by the protocol's rule for a reported bound, the bound widened by 10%, which gives 0.891.
- **ed7-bird1-bd-shared-persist:** the paper reports no test for B/D against B/C, so the chi-square test the criterion required was made up. The test is now reported but not judged.

**Verified and left unchanged:**
- The header's choice of chi-square without continuity correction reproduces the paper's P values: 0.031 against 0.03, and 0.0005 against 5 × 10⁻⁴. With Yates' correction they would be 0.049 and 0.0012.
- All other counts, sums, tolerances, quotes and method details agree with the Methods, legends and code.
- Each main finding has a claim, and every claim comes from this paper. The adult data from ref. 20 are marked `with_inputs`.

**What remains open (recorded in `checks`):**
- I could not view the figures because no PDF renderer is installed. So it is still unknown which stages carry the stars in Fig. 1f, 1g and Extended Data Fig. 1c, and which way burst width changes. Those parts are reported, not judged.
- The paper does not list the 8 syllable pairs (185 shared, 496 specific neurons) or the 20 syllables in the coverage analysis. Whoever runs the attempt must record their choices.
- The motif-strategy and new-chain model claims depend on the unpinned GitHub repository github.com/emackev/HVCModelCode. The Methods give no iteration counts or participation thresholds for the motif strategy.

I only edited `claims/okubo-2015.yaml`, and nothing is committed.
