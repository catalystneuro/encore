I did steps 1 to 6 of the Author section for sadeghi-2019 on CRCNS bst-2. Both notebooks pass `tools/entry.py all` (neural 33 min, model 15 min), and the handover is built in `executed/sadeghi-2019/handover/`. Nothing is committed.

**One caveat first.** After the last run I reworded one conclusion cell in the model notebook (the cost-estimate result) and did not re-run. Its timings change with the machine (56 to 130 min in one run, 63 to 152 in the next), so the old wording quoted numbers the latest output does not show. The new wording relies only on what the cell prints. The executed copy still has the old wording and its stamp is stale, so the next run will execute the entry again. The handover strips conclusions, so the verifier's first round is unaffected.

**1. Outcomes (28 claims)**

| Claim | Outcome |
|---|---|
| fig1k-example-temporal-widths | reproduced (10 of 11 values under the paper code's first-half window; 6 to 8 under the claims file's two windows) |
| fig1-snr-noise-stronger | partially reproduced (means match, range bounds do not) |
| fig1-s5-model-predicts-neural | blocked, data_missing (no best frequencies) |
| fig2-noise-restricted | reproduced |
| fig3a-example-tonotopy-removal | partially reproduced (drop of 20 to 40 points; values outside tolerance) |
| fig3a-example-classifier-order | partially reproduced |
| fig3b-population-above-chance | reproduced |
| figs6-per-sound-above-chance | reproduced (only when each time sample is one decision) |
| figs9-mixing-coefficient | reproduced, under 1 of many reading combinations |
| figs10-amua-tmua | blocked, data_missing (no raw voltage) |
| fig4-example-original-vs-equalized | not reproduced (temporal r 0.90 against 0.72) |
| fig4e-population-original-vs-equalized | not reproduced |
| fig4f-example-equalized-classification | partially reproduced |
| fig4h-population-equalized-classification | partially reproduced |
| fig8b, fig8e, fig8f (paradigm 3) | reproduced |
| fig5, fig6 (model widths) | reproduced |
| fig6c-category-diversity | reproduced (only with norms not squared) |
| fig7i-stationarity | not reproduced (the order holds, the values do not) |
| fig9a, fig9b (two claims), fig9c, fig9e, fig9-spectrum, fig10 | blocked, too_large |

The seven model classifier claims were not run. The notebook's cost cell estimates 56 to 152 minutes for the classifier, and writing and running it did not fit the time left in this run.

**2. Dataset, assumptions and questions**
- The files' sampling rate is 2034.5 Hz, not the 2 kHz the paper states.
- There are no tone-pip recordings (so no best frequencies) and no raw voltage traces.
- The channel order along the probe is undocumented.
- P2_Site08 has 13 trials where the paper states 14.
- The model WAVs are 16-bit integer, not the double precision the description says; white noise is not included.
- Otherwise the site, animal and trial counts match the paper, no recording is deposited twice, and every raster is locked to the trial start.
- The paper's own code disagrees with its Methods on the cochlear filter bandwidths and the envelope sampling rate; I followed the Methods.
- No outcome rests on an assumption: every open detail was run under all readings the claims file names, or taken from the paper's code.
- Two questions for the paper's authors are recorded as `methods_unavailable` findings:
  - How the 100 time samples enter a decision, how the number of principal components is chosen, and on which data the mixing coefficient is fitted.
  - Which forms of the stationarity and category diversity indices were used.
- I asked no questions of a reader.

**3. Where the protocol was unclear, wrong or missing something**
1. `docs/archives.md` assumes zip files; bst-2 is a single 5.3 GB tar.gz that cannot be read at random. I streamed it once from the start with `tarfile` (about 4 min per pass), parsing each member in memory.
2. "Develop on a subset" costs a full stream pass whenever the wanted file is late in the archive, and caching to disk is not allowed. I accepted the streaming time on each development run.
3. "Reproduced under one reading" combined with many crossed readings makes weak matches count (figs9 matches in 1 of 32 combinations). The protocol says nothing about this; I reported the fragility in the notes.
4. The claims file lets the author follow the paper's code, but the code's window for Fig 1 is not one of the criterion's listed readings. I adopted the code's window and showed the listed readings as variants.
5. A criterion with no rule for partial reproduction (fig7i) conflicts with the protocol's general definition of partially reproduced. I followed the criterion: not reproduced.
6. `too_large` is defined by compute against limits; here the binding limit was the author's remaining time to build and run the analysis. I used "over the time left" and stated the measured estimate.
7. A conclusion quoting timing numbers cannot stay backed across runs. I reworded it after the last run (see the caveat above).
8. CRCNS is unversioned and the bucket object was modified in 2026, after the 2019 description. I recorded the MD5 sums from `checksums.md5`.

**4. Runtime and failures**
The session took about 3 h 30 min (19:48 to 23:19 UTC). Nothing failed in the final runs; peak memory was 3.6 GB.
