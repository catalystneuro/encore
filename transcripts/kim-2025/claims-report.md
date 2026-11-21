I wrote `claims/kim-2025.yaml`, and the quote checker passes: 28 claims, 27 quotes, 0 problems. Nothing is committed.

**Text read.** The file under `paper/` is the bioRxiv preprint posted July 4, 2025, under an earlier title: "Neural variability structure in primary visual cortex is optimal for robust representation of visual similarity". The registry's title ("Intrinsic geometry of trial-to-trial variability…") belongs to a later version, which was not supplied. Every claim comes from the July 2025 text. That text includes the Results, Discussion, Methods and the legends of Figures 1–4 and S1–S6. The supplementary figures are part of it, so there is no separate supplement. There was no PDF.

**Code read.** The linked repository is jhk4839/Neural_variability_robustness. I read it at commit ac3300b (2025-07-03), the last commit before the preprint was posted; its figure numbers match this text. The head of the repository belongs to the 2026 version and was not used.

**What DANDI:000248 holds for this paper.** It is the OpenScope Illusion dataset, and the paper uses it only for the Isomap pictures in Figures 1C (bottom), 3A, 3E (left) and 3F (left). All the quantitative results are on the Allen Visual Coding Neuropixels data, which is not in this dandiset. So 24 claims are `data: elsewhere`. The four claims this dandiset can test are:
- a link claim: the ICwcfg1 block, its 12 stimuli with 400 repeats, the example session sub_630506 named in the code, and V1 units;
- the Figure 1C geometry: continuous with little overlap as-is, discontinuous at slope 0, heavily overlapping at slope 2;
- the Figure 3A example: orthogonal variance larger toward the faraway stimulus than the nearby one;
- the Methods sentence saying the geometric changes are "qualitatively similar across datasets".

**Counts.**

| | Number |
|---|---|
| Claims | 28 (27 findings, 1 link) |
| With a quote | 27 (all but the link claim) |
| With statistics | 10 |
| With a criterion | 28 |
| With expected values | 6 |

**Details the paper leaves open, and the readings named:**
- **O1, "peaks near slope 1".** No window is given. Readings: the slope with the highest across-session mean lies in (a) 0.8–1.2 or (b) 0.7–1.3. In both, slopes 0 and 2 must be lower than as-is and differ from it by a Wilcoxon signed-rank test, uncorrected, as in the code.
- **O2, "increases or decreases with slope".** Read as slope 0, 1 and 2 in that order, with the ends differing from as-is. "Monotonically" in Figure 2B is read strictly: a change in the stated direction at every 0.1 step.
- **O3, which Illusion units.** Readings: (a) all units located in VISp (not VISpm), as the code does, with no quality filter; (b) the same units with the Allen quality criteria from the Methods.
- **O4, the example session.** The text says only "one example session". The code uses sub_630506; the other sessions are a variant.
- **Figure 2C, "continuous starting around 1".** Same two windows as O1.
- **"Near 1" for the behavioural-state, higher-area and movie slopes.** No bound is given, so I used 0.9–1.1 (the protocol's 10% default). For the movie I added 0.85–1.15, because the paper's own code printed a median of 1.11.
- **Figure S6, "near maximal".** Read as the value at slope 1 within one SEM of the curve's maximum and not differing from it by the test.
- **Which "geometric changes" were compared across datasets.** Read as falling effective dimensionality and rising overlap.
- **Figures 1C and 3A.** These are pictures, and the 3A arrow lengths are set by hand in the code. They are judged with the paper's own overlap, connected-component and orthogonal-variance measures, computed in the full neuron space.

**Missing from the paper:**
- The Methods equations (slope manipulation, effective dimensionality, orthogonal component, number of trial pairs in the similarity analysis, the modulated Poisson model) are lost in the text. They were taken from the code.
- The legends of Figures 2 and 3 are cut before the p threshold. It was taken from the code, so no statistics are recorded for those claims.
- No p-values are printed for Figure S2 or for the positive correlation in Figure 3B and 3C.
- The paper gives no AllenSDK or data release.
- The code reads the Illusion data from a post-processed MATLAB copy that is not in the repository, so it cannot be checked whether its units were already filtered.
