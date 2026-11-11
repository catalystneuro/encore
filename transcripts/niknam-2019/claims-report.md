I wrote `claims/niknam-2019.yaml`. It passes the quote checker (34 claims, 33 quotes, 0 problems) and the claims schema. Nothing is committed.

**Text read.** The version of record (PMC6759185, Europe PMC full-text XML) was used. It includes the Methods, all figure legends, and the legends for S1–S6 Fig and S1–S3 Movie. There was no PDF, so no figure could be read. The supplement figures exist only as legends, but every number the claims use is in the Results or a legend.

**Code read.** github.com/nnategh/SFA-Models at commit 1438dde. It contains the S-, F- and A-model fits, the ΔLL/spk calculation, and `main_lists.mat`, which lists each neuron's RF, FF and ST probe. It has no code for the N-model, any statistical test, the partial models, the prevalence maps or the ROC detectability analysis.

**Claims.**
- **34 claims:** 1 link claim (the code's RF/FF/ST probe list checked against the dataset) and 33 findings. All 33 findings have quotes.
- **12 claims have statistics**, 28 entries in total: Wilcoxon signed-rank and rank-sum tests, one-tailed mid-P McNemar tests, and Pearson correlations.
- **All 34 have a criterion.** 30 have expected values; the tolerance is the paper's SE where it gives one and 10% otherwise.
- **Coverage:** Fig 1 (effect counts and normalized responses, latency, example neurons), Fig 3, Fig 5A–C, Fig 6A–D plus its example neurons, Fig 7 (two claims), Fig 8C/D/E, S1, S4 and S5, and the neuron counts from the Methods.
- **Data:** most claims are `with_labels`, because they need the RF/FF/ST probes from the code repository. The S1 claim (RF centres in dva) is `with_inputs`, because it needs each session's grid geometry, which the dataset description does not list.

**Open details and the readings named for each.** These are O1–O8 in the opening comment, plus a few within single claims.
- **O1, pairing for the signed-rank test on recorded data:** per trial, per condition, or an unpaired rank-sum test.
- **O2, what counts as a presentation:** the onset millisecond of each probe (the Methods), or every millisecond the probe is on (what the code does, kept as a variant).
- **O3, RF/FF/ST probes:** the code's `probe_list`, or recomputed from the Methods. Only RF can be recomputed from the dataset alone.
- **O4, subpopulation normalized value:** the mean over the effect's response window, or the peak of the smoothed curve.
- **O5, NULL model for ΔLL/spk:** the session mean rate or the mean rate over test trials. The code's `get_fr0` (offset and post-spike kernels only) is a variant.
- **O6, the 1000 stimulus sequences:** resampled recorded conditions, or new pseudorandom sequences.
- **O7, nulling a source in the partial F-models:** a fixation-period time drawn per time point, or one drawn per model.
- **Code that disagrees with the Methods:** the code averages kernels for the A-model and makes only one fit; I followed the Methods (ten fits, averaged Gaussian parameters). The code fixes r_max at 1000 spk/s, which I followed because the Methods don't say how the empirical maximum is measured. The 1.5 SD parameter-selection threshold comes from the code, because the equation for it was lost.
- **Fig 7 maps:** the time grid (1 ms or 7 ms steps) and which pixels are correlated (the full model span, or −50 to 150 ms around the saccade).
- **Fig 8 synthetic neurons:** whether the kernels the paper doesn't state are averaged over neurons or the fixation kernel is set to zero.
- **S4:** which period the "~60%" refers to (fixation, perisaccadic, or both pooled).
- **Example neurons (Figs 1, 6, 8):** the paper doesn't identify them, so each criterion searches all 41 neurons for a match.

**Missing from the paper.**
- **The reference list** is absent from the text. So ref [48] (the N-model), [49] (the McNemar mid-P test) and [73] (Chen et al., algorithm 2) are known only by number. The N-model is not described in this paper and is not in the code, so the 5 claims comparing against it (2 on Fig 5A, 3 on Fig 5B) depend on finding ref [48] (O8). If it can't be found, they are blocked.
- **All displayed equations** were lost in extraction. That includes Eq 10, the classification measures, and the prevalence-map indicator; I read these from the surrounding text and the code's README.
- **Grid geometry in dva** is not among the dataset's listed variables, which the S1 claim needs.

One typo in the paper: it prints "F-model vs. N-model" twice in the Fig 5B sentences, and I read the third comparison as the A-model.
