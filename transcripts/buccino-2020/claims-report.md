I wrote `claims/000034/10.7554-elife.61834.yaml`. The quote checker reports 24 claims, 24 quotes, 0 statistical values and 0 problems. Nothing is committed.

**Text read.** The version of record (eLife 2020;9:e61834), full text from Europe PMC (PMC7704107): main text, figure and figure-supplement legends, Methods, decision letter and author response. The only supplement is the transparent reporting form, which says "The manuscript does not contain any statistical analysis".

**Code read.** The paper's notebooks in `SpikeInterface/spikeinterface.github.io`. The repository's latest commit is 657c6d8; the four notebooks last changed at ee08fb6 (2020-09-29), before publication. They cover Figures 1–4 and Figure 1 supplements 3 and 4. I also read the library defaults in spikecomparison 0.2.6 and spikesorters 0.3.3, the versions the notebooks ran. Two things the code settles:
- **Sorter parameters:** the notebooks pass a SpyKING Circus setting under the key `spyking_circus`, which never matches the sorter name `spykingcircus`. So every sorter ran on its defaults, as the Methods say.
- **True and false positives in Figure 3C:** the Methods do not define them for that figure; the notebook's rule is used.

**Claims.**
- 24 claims: 23 findings and one link claim (the dandiset holds the six files with the properties the paper and notebooks give).
- 24 quotes, no `inferred` notes.
- 0 statistics: the paper reports no tests.
- 24 criteria; 13 claims have expected values, each at 10% tolerance. The exception is counts under 5 (false positives found by two or more sorters, overmerged units), which get ±1 unit, with the reason given.

**Details left open, and the readings named:**
- **Total detected units (Fig 1C):** the paper says 2031, but its own per-sorter counts sum to 2021. Read as that sum, which is within tolerance.
- **Agreement-score histogram (Fig 1 supp 2):**
  - Which recording: the real one (where the Results cite it) or the simulated one (its legend and the author response).
  - Which scores: all matched-pair scores, or each agreement unit's average score.
- **"Similar disagreement" on the rat and retina recordings:** the Figure 1D measure (over 50% of units found by one sorter), or the Figure 1C measure (units found by all sorters at most 8% of detected units).
- **Precision/recall bias:** medians over all 250 ground-truth units, or over matched units only.
- **Accuracy versus SNR:** "low-SNR" read as below the median SNR, or below the mode. "Modulated" read as a Spearman correlation, since the paper reports no test.
- **"Higher scores" for Kilosort2:** accuracy alone, or each of accuracy, precision and recall. Judged on "most units"; "significantly" has no test behind it.
- **Kilosort2's own curation:** applied to the same run, or to a fresh run with `keep_good_only`.
- **Sorter subsets (Fig 3 supp 1):** removed units' nodes dropped and components recomputed, or the full components kept. Rates pooled over the sorters, or averaged per sorter.
- **Kilosort2 false-positive SNR (Fig 3 supp 2):**
  - Unmatched units: the Methods' false-positive class, or the Figure 3C rule.
  - "Many": more than half, or at least a quarter.
- **Curator agreement (Fig 4A):** the notebook's three-way Venn, or a pairwise comparison of the two curators.
- **"Average above 70%" (Fig 4C):** the mean of the two curators, or each curator separately.
- **Version variants:** spikeinterface 0.10.0 (paper) against 0.9.9 (notebooks); HDSort 1.0.1 against 1.0.2; 246 channels against the notebook file's 248.

**What claims needed but the paper lacks:**
- There is no PDF of the main text, so numbers drawn only in figures (Fig 1 supplements 3 and 4, Fig 3 supplement 1) could not be read.
- No code exists for Figure 3 supplements 1 and 2; those methods come from the legends.
- The sorter outputs are not said to be deposited, so the author must re-run all six sorters. That needs MATLAB and a GPU for Kilosort2. Sorters don't give the same output twice, and the curators worked on the paper's own Kilosort2 run, so a re-run won't match it exactly.
