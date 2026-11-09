I checked the claims file for DANDI:001545. It is ready for an attempt, and I did not commit anything.

**Checker result (after my changes):** `claims/001545/10.26508-lsa.202403169.yaml: 56 claims, 56 quotes, 68 statistical values, 0 problems`. Before my changes it was 52 claims with 0 problems.

**Changes, by claim**
- **`fig1h`, `fig1j`, `fig1k`, `fig1l`, `fig2ef`:** I removed the one-tailed Mann-Whitney readings. For each reported U and cell count, the exact two-tailed p matches the printed P (for example U = 2 with 11 and 5 cells gives 0.0018 against the printed 0.0023, and U = 31 with 14 and 9 gives 0.046). So the paper's tests are two-tailed.
- **`fig2a`, `figs5a`:** the ANOVA design was not named. The reported degrees of freedom only fit a repeated-measures design: F(1,7) and F(2,12), where an ordinary two-way ANOVA would give 16 and 18. Repeated measures is now the test, with the ordinary ANOVA as a variant.
- **`fig2g`:** added the two readings with and without the PCA step from the Methods' LDA section, as `fig2m` already had.
- **`fig2i`:** added the Discussion as a source, since it supports the "RMP resembles that of SGCs" part of the statement.
- **`fig4b2`:** recorded that the Results and the legend disagree on whether 0.03 is a raw P or an FDR-adjusted one. The judgement still rests on U.
- **`tables4`:** the criterion named Enrichr libraries the paper never names. The tool and library are now listed as open, with readings.
- **`figs9d`:** the statement now says WT mice at 3 months, as the Results do.
- **New claims** for findings that had none: `figs5bc-penk-sorcs3-neg-outside-cluster18`, `figs7-downsampled-pseudotime-robust`, `figs8a-atac-pseudotime-cluster9` and `figs9c-embryonic-sgc-genes` (Allen Brain Atlas images, data elsewhere).

**Open**
- **Fig 2A mouse count:** the legend says 5 mice per genotype, but F(1,7) implies 9 mice in total. The text does not settle this.
- **Figure-only details:** there is no PDF under `paper/`, so I could not check what the first reader took from figure images. That covers the marker gene list for Fig 4b'' and S6, the feature list in Fig S2C, and the confusion-matrix counts in Fig S2G.
- **Code and Key Resources Table:** I did not re-read the two code repositories or the table cited in the opening comment.
- **Thresholds the first reader chose:** some cutoffs were set by the first reader, not taken from the paper. Examples are the 90% bound in `fig2g`, the top decile in `fig5b`, thirds in `fig7bc`, the 1.1 × p rule in `figs1a-f` and the 15-point margin in `figs2g`. Each is labelled as a reading in its criterion, and I left them unchanged.

**Ready:** yes. The `checks` entry is at the end of the file with `ready: true`.
