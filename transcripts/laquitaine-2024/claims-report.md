I wrote `claims/001250/10.1101-2024.12.04.626805.yaml`. The quote checker passes on it with 0 problems. Nothing is committed.

**Text read**
- I read `paper/10.1101-2024.12.04.626805.txt`, taken from the bioRxiv JATS XML. Its header says "preprint, version 1". It holds the main text, the Methods, the Discussion and the supplementary figure legends; there is no separate supplement and no PDF.
- **Version caveat:** this text's abstract says "about 15%", but the bioRxiv API gives "about 10%" for both version 1 and version 2. The text may be a later revision than its header says.
- The Methods equations (agreement score, chance score) were lost in extraction. The code fills them in.
- The supplementary figure numbering is inconsistent within the text, so each source cites the legend's title as well.

**Code read**
- The text says only "available on GitHub"; the link was lost. I found the repository, github.com/steevelaquitaine/spikebias, at commit 6e9af03 (2026-01-28, its only commit).
- Some notebooks belong to a later revision. For example, the AP power band is 0.3–1 kHz in the code against 0.3–2 kHz in the text. Where the code and the Methods disagree, the Methods decide and the code's choice is a variant.

**Claims**
- 39 claims, every one with a quote and a criterion.
- 16 claims record statistics, 26 entries in all: chi-square, Kruskal-Wallis, Mann-Whitney, Fisher and t-tests.
- 20 claims use data from outside the dataset (`data: with_inputs`): the in vivo recordings of Marques-Smith and of Horvath, and Buccino's synthetic simulation (which the code reads from DANDI 000034).

**Details the paper and code leave open, with the readings named**
- **Single-unit fraction test** (χ²(4, N=5,241)): neither the paper nor the code holds this test. Readings: the code's form for its other tests (a goodness-of-fit test on percentages) over M, NS, NS-2X, E and S; a contingency test over the same five; a contingency test over M, H, NS, E and DS.
- **The other Fig. 5a and 6b chi-square tests:** the code uses goodness-of-fit on percentages. A contingency test is named as a variant.
- **Which sorted units enter a neuron's best match:** all units (Methods), or single units only (code).
- **Which evoked recording** in Figs 4–5: the 10-minute recording at 40 kHz, or the first 10 minutes of the 1-hour recording at 20 kHz.
- **The ~15% average accuracy:** N = 3,190 implies the code sums the synthetic, spontaneous and evoked ground truths. The biophysical simulations alone are a second reading.
- **Median firing rate over layers 5 and 6:** the pooled median (code), or the mean of the two layer medians.
- **Curation regression:**
  - Split: 80/20 (Methods) or 75/25 (legend and code).
  - Penalty: the legend says lasso, but the Methods and code fit it unpenalized, which is followed.
  - mad_ratio correlation: against the binary good label (code) or against continuous accuracy (text).
- **Fractional regression penalty:** none is given anywhere. The code's statsmodels default (alpha 0) is followed.
- **Selection bias:** a sorted unit's layer is either its matched neuron's layer (text) or its site's layer (code).
- **Fig. 7 capacity:**
  - Bootstraps: 200 (legend and code) or 1000 (Methods).
  - Test: two-sample t-test (code) or one-sample (matching the printed df of 199).
  - "Decrease": the normalized capacity halves, or the excess above the lower bound halves.
- **WaveMap:** the Louvain resolution is open. The code maximizes modularity; its notebook text says 1.5.
- **Qualitative findings** with no stated measure: a fixed rule is named for each and marked as chosen here. These are the depth trends, "within the in vivo range", "power law", "log-normal", "order of magnitude", the ring-like manifold and the slow-wave dominance.

**Missing from the paper that a claim needed**
- The test behind "not significantly different between probes or sorters" (Fig. 5b). Nothing in the paper or the code names one, so that part is reported but does not decide the outcome.
- The "163" in "S: 377 vs 163" is unexplained: the Marques-Smith single-unit count elsewhere is 96.
- The Results' contamination-rate threshold of 0.1 is not applied in the code, which uses Kilosort's own 'good' label.
- The Fig. 3 figures could not be read, as no PDF was stored.

**Possible bugs in the paper's code** (variants named where a claim depends on them)
- The CEBRA notebook may append the quality metrics in a different row order from the waveforms.
- The Fig. 7g resampling drops duplicate units, and its arrays are not reset between the good and degraded classes.

**Security issue in the code:** its DANDI upload scripts contain a hard-coded DANDI API key.

Sources: [steevelaquitaine/spikebias](https://github.com/steevelaquitaine/spikebias), [bioRxiv 2024.12.04.626805](https://www.biorxiv.org/content/10.1101/2024.12.04.626805v1)
