I wrote the claims file at `claims/crcns-apl-1/10.7554-elife.27342.yaml`. It has 30 claims, and the quote checker passes: 30 quotes, 0 problems. Nothing was committed.

**Text read.** I read the version of record (PMC5546814), flattened from its JATS XML: main text, Methods, and the legends of Figures 1 to 8 and all twelve figure supplements. The paper has no other supplementary file, and no PDF of it was supplied; no claim needed one. I read the data descriptor only to see what the dataset holds.

**Code read.** github.com/mdhumphries/AplysiaAttractorAnalysis at commit e5f28e98. It holds the MATLAB scripts for every analysis and figure. Where the Methods are silent, the code settles: the recurrence settings, the local linear fits, how rotation period and contraction rate are computed, the cut-offs for the Figure 4B regions, the 0.2 cut-off for "same manifold", the ensemble and similarity measures, and the left and right preparation lists for the maps.

**Claims.**
- 30 claims, all with a quote and none `inferred`. All use the dataset itself.
- 29 have criteria; 16 have expected values.
- One statistics entry: Figure 5B, weighted Spearman with a permutation test, P < 0.01. The paper prints no other test result.
- I made no claim for the three-neuron model (Figure 1, figure supplement 1), which is a simulation, or for Figure 2, figure supplement 1, which is descriptive.

**Where the code differs from the Methods.** Following the protocol, the Methods are the main reading and the code's choice is a variant:
- **Gaussian width:** the Methods print median ISI/12, which may be a square root lost in extraction. The code uses the median ISI itself, pooled over all recordings of that stimulation number read so far.
- **Number of PCs:** the Methods say "at least 80%" of variance. The recurrence code keeps the PCs whose cumulative variance is at most 80%; the manifold code uses at least 80%.
- **Dominant period:** the Methods say the mean recurrence time of the dominant peak; the code uses the median.
- **P10 decoding windows:** the Methods use a 40 s fit stepped by 1 s with 50 to 200 ms histories. The code trains on 50% of the series, steps 0.2 s, and tries histories up to 250 ms.
- **Permutation test:** 10,000 permutations in the Methods; 100,000 in the code, which permutes the pooled values and is one-sided.
- **Point sets for the Hausdorff distance:** recurrent points in the Methods; windows with at least 90% recurrence in the code.
- **Noise model for participation:** all pairs of programs in the Methods; consecutive pairs only in the code.
- **Participation dimensions:** each program's own count, or the count from the PCA of the three programs together (the code).
- **Return after a perturbation:** recurrences counted after the end of the divergent period (Methods) or after its divergent point (code).
- **Rate behind participation (Fig. 7, figure supplement 1):** spikes counted from stimulus offset (legend) or onset (code). The code also mismatches two of the three pairs when it compares changes in rate with changes in participation.

**Open details and the readings named.**
- Decay of the population rate: the Methods' 20 s window R < -0.2 rule, or a negative regression slope.
- Robustness to the recurrence threshold: Spearman agreement, or the median difference.
- Similarity correlation: Spearman or Pearson, and which program's control a pair is compared with.
- "Most strongly participating" neurons: the top neuron or the top 10%.
- "Quintile" in Figure 8: the code's equal-width bins or true quintiles.

**Rules I fixed because the paper gives none, each stated as such in the criterion:**
- the counts behind "generally" and "almost all" (27 of 30);
- the comparison for initial conditions;
- "accurately" for P10 decoding (mean forecast R minus 2 s.e.m. above 0);
- "close to 1" for motorneuron locking (0.9);
- what counts as long-tailed;
- the invariant-core cut-off;
- the Wilcoxon test for "no improvement at 90%";
- p < 0.05 for the claims of absence in Figures 5C and 7G/H, where the paper prints neither a threshold nor a statistic.

**Missing from the paper, or not reconcilable:**
- **Figure 8 orientation:** neither the paper nor the code says which quadrant of the array is caudo-lateral. It has to come from the dataset's map files, or that claim is blocked.
- **Neuron counts:** the paper gives 120 to 180 neurons per recording; the dataset description gives 75 to 160. The 1131 total matches.
- **Forecast windows:** the paper's 173 forecast windows match neither the Methods' windowing nor the code's, so it is reported and not judged.
