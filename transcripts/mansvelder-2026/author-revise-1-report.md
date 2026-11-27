I've revised the attempt for every point in the round-1 report. The entry re-runs cleanly (`python tools/entry.py all entries/mansvelder-2026` passes, about 18 minutes) and the checks report 0 errors. Every conclusion was checked against the new outputs.

**What changed in the outcomes**

The biggest change comes from the report's main point (problem 1). DANDI:000636 and DANDI:000020 are now read as pinned outside inputs:
- **000636** holds the Lee, Dalley et al. 2023 recordings: human acute cells of all four subclasses, plus slice-culture cells. Its per-cell labels come from the authors' repository at a fixed commit.
- **000020** holds 461 of the paper's 628 mouse cells (Table S2b). They are found through a pinned copy of the Allen metadata. None of the paper's mouse PV or SST cells are among them, so no PV or SST species comparison can be run. A quick search of the later Allen mouse dandisets, done outside the notebook, found only 1 candidate for the 167 missing cells.

Outcomes now:
- **Reproduced (8):** chartrand-label-link, lee-label-link, fig2b, fig2d-pv-highest, figs2a, fig3jl, fig6b, figs1.
- **Partially reproduced (11):** mouse-specimen-link (73% of the mouse cells found), fig2d-subclass, fig2e, fig2e-lamp5-sst, fig2f, fig3c, fig3d, fig3ik (was not reproduced), fig5g, fig5i, fig5jk.
- **Not reproduced (8):** sample-size, fig2ab, fig2c, fig2g, fig3eg (was partially reproduced), fig3fh, fig5l, fig6c, figs4.
- **Blocked (19):**
  - Depth claims (7) and fig2d-sst-similar: `data_missing`. No public source gives pia-soma distances; the Chartrand table's depth column is 0 for every cell.
  - ZD7288 claims (2): unchanged.
  - fig6a and four model claims: `other`, under the protocol's time rule.
  - fig7-model-ca and the three fig8 claims: `methods_underspecified`, unchanged.

fig3eg is not reproduced because, with all four subclasses, neither interaction is significant and the LAMP5 input-resistance slope misses p < 0.05 under every reading.

Several outcomes rest on the choice of chirp reading. I made reading (b), with the profile starting at 0.4 Hz, the main reading. Three things support it: Table S3's medians of exactly 0.40 Hz, the mouse LAMP5 medians (which it matches), and the Allen Institute's own chirp features. Reading (a) is shown throughout, and it would reproduce fig2c and fig5i. Those outcomes are marked assumed.

**Added or corrected**
- **Two new link claims** in the claims file, `lee-label-link` and `mouse-specimen-link`, with `depends_on` added to the claims that need them. No statement, expected value or criterion was changed.
- **Satterthwaite tests** (O5 reading a) are now computed in the helper. Convergence is printed for every fit.
- **Chirp checks** in the notebook: Table S3 medians and resonant fractions set against both readings, fres and Q histograms, and a comparison with the Allen chirp features. The LOWESS smoothing fraction turns out to matter a lot (human LAMP5 resonant fraction 31.0% at 0.02, 19.5% at 0.04), and this is recorded.
- **Sweep drops** are tabulated per file, with a count of chirp sweeps that had zeros only before the chirp. There are none, so no recording was dropped for a leading zero.
- **Duplicates:** 4 cells are in both 000630 and 000636; they are counted once.
- **Expression data** from both labs' repositories, read in memory, for fig6b, fig6c and figs4. This added `rdata` to the lock file.
- **Questions file:** `questions/mansvelder-2026.yaml` asks a reader the three misreadings the verifier reported.
- **Attempt record:** the round is recorded under `verifications`, the findings are updated and three new ones added at the end, and the README and `entry.yaml` are updated.

**Not done, and why**
- **Problem 7:** no change. Input resistance under reading (a) uses the peak deflection because that is how IPFX computes it, as the claims file's reading names it. Reading (b), which uses the steady state, is shown in every model.
- **fig6a, the mouse half of figs4, and the four model claims:** not attempted in the time available.
- **Mouse-only claims (fig3fh, fig3jl, fig4i, fig4km):** their `data` field is still `dataset`, though they use none of 000630's recordings. I asked a reader instead of changing it.
- **Listing 000636 on the paper:** 000636 holds the data of the paper's reference 2, so the registry may want to list it with the relation `reuses`. I didn't add it, because the paper doesn't name the dandiset.
