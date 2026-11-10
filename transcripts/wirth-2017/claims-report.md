I wrote `claims/wirth-2017.yaml`. The quote checker reports 28 claims, 28 quotes, 25 statistical values and 0 problems.

**Text read**
- The version of record, PMC5328243 (Europe PMC full text). It includes the Results, Discussion, Methods, and the legends of Figs 1–7 and S1–S7. No PDF was read.
- **Missing:** the S1 Appendix (supplementary methods A1–A5) and the S2 Appendix are DOCX files and are not under `paper/`. The reference list is also absent, so reference 60, the learning-curve method, is not named.
- I went ahead anyway, because the core results (Figs 3–7) rest on the main Methods, which are present. Four claims need S1 Appendix and say so: `gaze-anticipates-action`, `gaze-anticipates-landmarks`, `fields-per-cell` and `dimensionality-control`. The last two are flagged as likely `methods_underspecified`: the text read never defines a "field" and does not describe the dimensionality control.
- **Code:** the paper links no repository. Its Matlab scripts are stored with the dataset on CRCNS, so I did not read them.

**Claims:** 28 in all. Every one has a quote and a criterion, 16 have statistics and 17 have expected values. They cover behaviour (gaze anticipation, learning, probe transfer), cell counts, information content and sparsity by coding space, direction tuning, state-space selectivity, the landmark ANOVAs, path selectivity, the gaze-aligned dynamics and latencies, eccentricity, foveation selectivity, place fields and population maps.

**Details left open, with the readings named**
- **Trial span:** whether the return path after a correct trial counts as part of it.
- **Surrogates:** whether the 5 s chunks are permuted in order or each shifted at random.
- **Binomial chance rate:** 0.05 or 0.025. The paper's own p-values fit 0.05 for state-space selectivity and 0.025 for the direction correlations. Neither rate gives p = 0.37 for the single path-invariant cell.
- **Point of gaze:** which eye (left, right or the mean), eye calibration, and how bin resolution is stepped in each space.
- **Unnamed tests and cell sets:** which cells enter, and which test, for centre against periphery, the gaze-aligned rise and the latencies.
- **Two conflicts within the paper:**
  - The gaze-before-action window is 500 ms in the Results and 300 ms in the S2 legend.
  - The path-selectivity offset is 120 ms in the Results while the Methods window starts at onset, and the Methods give 150 ms for landmark selectivity.
- **Landmarks:** how entry into the field of view and the "most informative landmark" are defined.
- **Behaviour:** which sessions count for learning, whether the probe test pools the two monkeys, and how trials to criterion are counted after new entries.
- **Landmark ANOVA:** whether "both factors" excludes cells with an interaction, and how a landmark view at the centre is delimited.
- **Spatial selectivity:** what "approximately 50%" counts (position-responsive cells or all responsive cells).
- **Gaze map:** how the area around a landmark is delimited.

**For the author:** the dataset's description says it holds 101 cells, each with a familiar and a new maze, and asks to be cited as doi 10.6080/K0GX48R9. The paper analysed 189 cells, describes only new mazes, and gives its data as doi 10.6080/K0R49NQV. I recorded this in the opening comment and did not try to resolve it.
