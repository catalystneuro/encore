I rewrote `claims/tingley-2018.yaml` to the current protocol. The quote checker passes with 0 problems, and nothing was committed.

**Text read.** The NIH author manuscript in PubMed Central (PMC6605060), not the version of record: main text, figure legends, STAR Methods, and the supplement (Document S1, legends of Figures S1 to S7). Nothing a claim needed was missing.

**Code read.**
- DavidTingley/papers at commit 9f4cd48: the figure scripts `makeFig1.m` to `makeFig6.m`, and the model notebooks with `decodeModelData.m`.
- buzsakilab/buzcode at commit e615663: the functions for firing and phase maps, place fields, Olypher information, peer prediction and circular smoothing.
- The script that made the per-cell decoding tables and the cross-region assembly files is in neither repository.

**Counts.** 31 claims, all 31 with quotes, 10 with statistics (16 values) and 31 with criteria. Two claims are `data: elsewhere`: the Allen connectivity analysis (figs3) and the spiking model (fig7).

**What changed**
- The previous file was written by an author who had seen the dataset (unit label names, counts, sessions with positions in pixels, depths read from session names). I removed those choices, and every criterion is now cited to the Methods, a legend or the code.
- I dropped the `dataset` block, as the schema asks for a paper's own claims file.
- All 21 old ids are kept. ls-information-lower was the only claim with expected values and a criterion; it was left out by mistake when I rewrote the file and is not in it now. It should be restored before an attempt.
- Criteria were added to fig5g, fig6e, speed-independent and figs6. fig5-assemblies is now the full method, not a random sample of pairs.
- 10 new claims: fig3-ls-phase-reliable, fig4e-onset-mediolateral, figs5-assembly-independent-of-locking, fig6-session-counts, figs2-rate-phase-independent, figs3-ls-major-target, figs1f-trial-counts, plus three more not named here.

**Details the paper leaves open, with the readings named**
- **Number of position bins** (sets the MSE scale): 200 bins per condition, or 1.5 cm bins.
- **What a decoding split divides:** whole trials, or pooled trial-by-bin samples (as the model decoder does).
- **Phase feature:** cosine of the smoothed phase (what the figure scripts use), with raw phase as a variant.
- **Spike-phase filter:** 6 to 9 Hz from the code, with the Methods' 4 to 12 Hz as a variant.
- **Rate map passed to the place-field rule:** Gaussian-smoothed or box-smoothed.
- **CA1 versus CA3:** labelled by session (as the code does) or by each unit's own label.
- **Information levels (Fig 1E):** 7 equal-width or 7 equal-count levels; buzcode's rounding is a variant. **Fig 1G test:** t test (Results) or KS test (legend).
- **"Coefficient of variance" of field stability:** SD in Hz (as the code computes it) or SD over mean.
- **The 1,425 neurons:** they are not the 2,951 hippocampal units of Figure 3A, and the paper does not say which neurons they are.
- **LS activity count:** per condition or per session.
- **Condition-level counting (Fig 2):** t test at p < 0.01, or simply a lower mean MSE.
- **Fig 3 "more reliable":** measured on the anti-diagonal or on the off-diagonal correlations.
- **Fig 4E onset:** which condition gives a neuron's value, how the mean phase is taken, and which depth is used.
- **Assemblies:** Methods rule alone, or with the code's extra filters; timescale as half-width or full width.
- **Fig 5G:** one value per pair or per neuron, and t test or KS test.
- **Fig 6E:** assembly pairs only or all pairs with a field, and whether the curves are smoothed.
- **Ensembles (Fig S7):** how ensembles of each size are drawn.
- **Fig S2:** how a condition is called significant.
- **Allen ratio:** taken over target medians or per injection.
- **Speed analyses:** not described in the Methods at all; readings are named for both.
- **Tests the paper does not name:** for the Fig 6C/D increases, the Fig 4D gradient, the Fig S5 independence, the Fig S6 "many" and the model, I state the tests used as standard choices the paper does not make.

**Missing from the paper**
- The Allen experiment ids, so the figs3 claim cannot be pinned to specific experiments.
- Any statistics for the model (Fig 7).
- Code for Fig 4E, Fig 6E, the speed analyses and the reference-frame analysis.
- The paper's counts don't agree with each other: CA1 and CA3 place fields sum to 1,811, not the 1,820 used elsewhere; and Fig 5G names a KS test where the text names a t test.
