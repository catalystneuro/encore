I wrote `claims/elie-2019.yaml`, uncommitted as asked. It has 25 claims, every one with a quote. The checker passes the schema and all 25 quotes. It flags one p-value, `fig9b-cii-tau-ratio` 2.37e-7, which the paper prints as "p = 2.37 10 −7" (Results, Analysis of the categorical information, paragraph 3); the checker does not recognise that format. I confirmed the value by reading and left the checker alone, but its exit code is still non-zero.

**Text read.** The version of record, PMC6762074 (open access), from the publisher's XML: main text, Methods, Table 1, and the legends of Figs 1 to 10 and S1 to S7. The supplement is only those seven figures. No PDF was supplied. The data description was read only to see what the dataset holds.

**Code read.** github.com/julieelie/PoissonTimeVaryingInfo at commit 97802032 (2019-04-01). It settles:
- which nine call types are used;
- the 10 ms bins and the Monte Carlo settings;
- how categories are weighted;
- the random-category floor (one shuffle of the call-type labels per unit);
- the fixed-rate control.

It does not contain the rate estimate (KDE) itself, the coherence function, the multiple-comparison (FDR) step, the selection of the 404 and 337 units, the exponential fits, the expected categorical information or the categorical index (CII), or any population or anatomical statistics.

**Content.**
- **Claims:** 25 findings and no link claims. One, the model neurons of Fig 1, is a simulation (`data: elsewhere`, using the tutorial file in the code repository). One, the 404-unit selection, needs outside information (`with_inputs`).
- **Statistics:** 10 tests recorded, across 8 claims.
- **Criteria:** every claim has one, and 22 have expected values.

**Open details and the readings named:**
- **Rates:** used as estimated, or low-pass filtered at 50 Hz first.
- **Exponential fit:** the equation is lost from the text. The reading given is I(t) = k·I_Max·(1 − exp(−(t−dt)/τ)). "Well fitted" is not defined; readings are (a) fits converge with parameters in range, or (b) the 214 lowest-error fits.
- **CII:** the formula is lost. The reading given is a piecewise linear map through 0 (floor), 1 (expected) and 2 (ceiling).
- **Population averages for units whose cumulative curve ends early:** leave them out from that point, or carry the last value forward.
- **Poisson test:** the Methods say two-tailed; the code is one-tailed and has no FDR step. The Methods are followed and the code is a variant. Cut-offs read as "at most 10% / at least 40%" or "under 10% / over 40%".
- **Fano factor:**
  - Stimuli with no spikes in a bin are set to 1 (as the code does) or left out.
  - No test is named; readings are a t-test or a Wilcoxon test against 1.
- **Stimulus correlation:** computed across stimuli at each pair of bins, or across bins within each stimulus.
- **Fixed-rate fraction:** a ratio of population means, or the mean of each unit's ratio.
- **Average firing rate in the k300 regression:** KDE rate over 0 to 600 ms, spike-count rate over 0 to 600 ms, or KDE rate over 0 to 300 ms.
- **Significance of the mean CII:** the 2-SEM band, or a t-test in each bin.
- **Distance to the L2 axis:** perpendicular distance, or rostro-caudal distance. Which units enter the regressions and the ANOVA is also open.
- **Degrees of freedom:** the text gives 214 units but t(214) and F(1,213) imply 215. The printed F(2,195) values match their p-values only as F(1,195).
- **Thresholds I fixed myself:** for "small", "almost constant", "relatively constant" and "unimodal" (Hartigan's dip test), the paper gives no rule, so each criterion says the threshold is my choice.
- **Example neurons (Figs 3 to 5):** the paper does not identify these units in the data. The claim is blocked unless the rasters in S4 to S6 Fig identify them.

**Missing from what was supplied:**
- **Equations:** all the displayed equations were lost in extraction, and no PDF was supplied. Those that matter are the exponential model, the CII formula, the coherence formula and the bias correction. The author can read them in the published article.
- **404-unit selection:** this rests on the decoding analysis of Elie & Theunissen 2015 (Eur J Neurosci 41:546), which this paper does not describe.
- **Anatomy:** the anatomical claims need area labels and coordinates for each unit. The data description does not mention them.
