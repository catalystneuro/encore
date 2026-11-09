I've written `claims/okubo-2015.yaml` with 42 claims. The quote checker reports no problems: every quote matches the paper word for word and all 21 statistical values were found in the text. Nothing was committed.

**Text read.** The version of record (`paper/10.1038-nature15741.txt`): main text, figure legends, Methods and the legends of Extended Data Figs 1–10. The Supplementary Information is the model code (`paper/10.1038-nature15741.code.m`), which I read; its two videos were not supplied, and no claim rests on them alone. No code for analysing the recordings is linked, so every data method comes from the Methods and legends. The model code agrees with the Methods. Where the Methods leave something open for the model, the code settles it and I followed it: the participation thresholds, the iterations shown in Fig. 5c and 5d, and the random seed.

**Counts.**
- 42 claims, all with a quote and none marked `inferred`.
- 14 claims carry statistics (21 entries); all 42 have a criterion.
- 34 claims are on the recordings: 4 of them use the adult stage and are marked `with_inputs`, and 30 use the dataset alone.
- 8 claims are on the model and are marked `elsewhere`.

**Details the paper leaves open, with the readings named:**
- **Syllable locking:** the smoothing kernel (a 20-bin moving average, as a standard choice); whether shifted spikes wrap around the window (circular shift, or shift from a wider window); and, in stages with several syllable types, whether syllables are pooled or each type is tested separately.
- **Rhythmicity:** the bin widths of the inter-burst-interval histogram and the autocorrelation (1 ms smoothed over 20 bins, or 10 ms); and whether the cepstrum comes from the mean spectrum or from each window.
- **Shared/specific neurons:** whether to align to syllable onset or offset (each figure's own choice, the other as a variant). The paper's visual adjustment of the analysis window can't be repeated exactly.
- **Fig. 2c latencies:** one peak latency per neuron (which fits 63% and 43%) or all bursts pooled.
- **"Participated in a protosequence" (14/16 in bird 1, 28/35 in bird 2):** locked, rhythmic, or both.
- **Pooled tests:** the 8 syllable pairs and the early/late split for the Cochran–Mantel–Haenszel test, with and without continuity correction. Plain chi-square without correction reproduces the printed P = 0.03 and 5×10⁻⁴, so that variant is used.
- **Stage–age correlation:** the unit is a day, a neuron or a bird-stage.
- **Neuron sets and denominators:** which neurons enter the bias measure, and the denominators for the 19% vs 28% comparison.
- **Unspecified rules:** how a neuron is assigned 10 Hz or 5 Hz; a rule for "skipping cycles"; the post-hoc tests; the sound-amplitude envelope used for phase; and the acoustic-feature implementation.
- **Model:** the breadth measure (interquartile range or s.d.); the period measure (autocorrelation peak or most common interval); and the iterations and threshold for the motif strategy.

**Missing from the paper or this run:**
- **Significance stars:** the PDF couldn't be rendered (no renderer installed), so I couldn't see which stages carry the stars in Fig. 1f, Fig. 1g and Extended Data Fig. 1c. Those post-hoc results are reported, not judged.
- **Adult neurons:** the 3 adult birds (32 neurons) include recordings published earlier (ref. 20, Kozhevnikov & Fee 2007). The data descriptor lists only juvenile birds, so they may not be in the dataset.
- **Model code:** the motif-strategy model (Extended Data Fig. 10e–h) and the new-chain model (10i–k) are only in github.com/emackev/HVCModelCode, which I didn't read and which has no pinned commit.
- **Neuron count:** Extended Data Fig. 2l gives 149 bout-offset neurons, but the Results counts give 98 + 50 = 148.
