**A. Outcomes** (45 claims in the claims file, including the author's link claim)

| Claim | Outcome | Reason |
|---|---|---|
| chartrand-label-link | reproduced | Cell 9: all 210 files match a row, and NWB subjects map one-to-one to donor names. Sex agrees (one NWB "unknown"), age differs by −0.06 to −0.01 y over 208 files, and all 53 donors are in Table S1. |
| sample-size | not_reproduced | Cell 11: 210 cells from 53 donors, against 542 ± 54.2 and 170 ± 17. This is the outcome the criterion itself expects on the dandiset alone. |
| fig3eg-human-fres-sag-rin | partially_reproduced | Cell 17, main reading (a,a): LAMP5 sag b = 3.70, p = 3.7e-4 (outside 3.31 ± 0.331); VIP sag 4.40, p = 0.024 (inside); LAMP5 Rin −0.0037, p = 0.023 (outside ±0.0002). PV is absent, so the paper's 3-df interactions cannot be tested; the LAMP5-vs-VIP interactions are p = 0.82 and 0.34. Under chirp reading (b), one of the three testable effects fails: LAMP5 Rin p = 0.058, or VIP sag p = 0.228. |
| fig3ik-human-q-sag-rin | not_reproduced | Cell 19: sag slope is 0.10 to 0.15 in all 8 fits, against 0.47 ± 0.047. In the main reading sag p = 0.0046 (criterion needs < 0.001) and Rin p = 0.239. Rin reaches p < 0.05 only under (b,a) LMM/GEE, p = 0.047/0.016, and the LMM 0.047 would be about 0.05 with t df. The sag×subclass interaction is ≥ 0.05 except GEE (a,a), p = 0.034. Only LAMP5 and VIP cells are in the test. |
| figs1-region-pathology | reproduced (weak) | Cell 21: fres, Q, f3dB and Rin give KW p ≥ 0.225 and MWU p ≥ 0.066 under both readings and both label sources. Only 3 lobes are present (74/8/1 cells, no occipital), so the region test has little power. Sag: KW p = 0.044, but epilepsy vs tumour p = 0.94 against the paper's p < 0.001 (reported, not part of the criterion). |
| fig2b, fig2ab, fig2c, fig2d-subclass-proportion, fig2d-sst-similar, figs2a, fig2e-fres-species-subclass, fig2e-lamp5-sst-fres-similar, fig2f, fig2g, fig3c, fig3d | blocked (other) | The notebook says mouse recordings are missing. The archive appears to hold them: DANDI:000020 matches 451 of the 505 Table S2b rows I parsed from the PDF (same sex, age and Cre line; session id 14 to 1494 below the specimen id). Human PV/SST cells are on DANDI:000636. Chirp sweeps in these files are not checked. |
| fig3fh-mouse-fres, fig3jl-mouse-q-sag-rin | blocked (other) | Same as above: the mouse cells appear to be on DANDI:000020. |
| fig4i-mouse-sag-depth, fig4km-mouse-no-depth | blocked (metadata_insufficient?) | Mouse recordings are on 000020. I did not check where mouse pia-soma distances come from. |
| fig2d-pv-highest | blocked (other) | DANDI:000636 ("human neocortical interneurons from acute and slice culture", 706 files, 109 subjects, 45 shared with 000630) should hold PV and SST cells. Not used. |
| fig4c-human-sag-depth, fig4df-human-no-depth, fig4g-human-q-decreases-depth | blocked (other); partly testable | The Chartrand table has `Depth_from_Pia_microns` for all 419 rows, so an L1-only partial test was possible. Other layers would come from 000636 with its labels. |
| figs2-l23-no-depth | blocked (other) | Needs L2/3 cells, which 000636 should hold. Layer labels not checked. |
| fig4b-tdl-depth | blocked (data_missing) | No morphologies on DANDI. |
| fig5be-zd7288-human, figs3-zd7288-mouse | blocked (data_missing) | Confirmed: no ZD7288 data found on DANDI. |
| fig5g, fig5i, fig5jk, fig5l | blocked (other) | DANDI:000636 describes slice-culture recordings from Lee, Dalley et al. 2023, the paper's "PublishedLD_Cultured" set. Not used. |
| fig6a-hcn1-pex5l-human | blocked (other) | Wrongly blocked as "transcriptomes not in the dandiset". The claim is `data: elsewhere` on public Allen Brain Map data. |
| fig6b, fig6c, figs4-culture-mouse-genes | blocked (data_missing) | Patch-seq transcriptomes are not on DANDI. The Chartrand repository has `ps_human.RData` and `ps_mouse.RData`; I did not check them. |
| fig7-model-ca | blocked (methods_underspecified) | Calcium conductance density is missing from Table S5 (claims file). |
| fig8bc, fig8eg, fig8hk | blocked (methods_underspecified) | They depend on fig7-model-ca. |
| fig7ae-model-ih, figs5-model-gpas, fig7fj-model-morphology, figs5-model-normalized-morphology | blocked (other) | "Not attempted" is not an allowed reason. The base model is named as public (DataverseNL). |

**B. Problems**

1. [affects a conclusion] Cell 0: about 30 claims are blocked as "data not in the dandiset", but the archive was not searched. The mouse recordings (DANDI:000020, matched to Table S2 specimen IDs) and the Lee/Dalley acute and cultured human recordings (DANDI:000636) are on DANDI. The claims file had told the author to look ("unless the author finds them public; Table S2 gives the mouse cell specimen IDs").
2. [affects a conclusion] Cell 0: fig6a is blocked for the wrong reason (its data are public Allen Brain Map). Four model claims are marked "not attempted" with no reason from the allowed list.
3. [affects a conclusion] Cell 13, `resonance`: the chirp readings are never compared with Table S3's human medians, and neither reading matches them.
   - LAMP5 median fres is 0.20 Hz (a) or 0.40 Hz (b), against 1.09 Hz in the paper; median Q is 1.000 against 1.013.
   - Table S3's 0.40 Hz medians (SST, mouse VIP) point to a 0.4 Hz floor, which is reading (b). But (b) gives resonant fractions of 20.9% and 16.7%, against 31.25% and 25%.
   - 42 of 85 cells sit at the floor (Q = 1), so fres is a censored outcome inside a linear model. This bears on fig3eg and figs1.
4. [affects a conclusion] Cell 17: reading (a) is called "main" with its reason removed. Under chirp reading (b) the fig3eg pattern does not hold (see table).
5. [affects a conclusion] Cells 14–19: O5 reading (a), Satterthwaite F/t, was not run ("not available in this Python environment"). The statsmodels Wald p-values use z and are anti-conservative here; for example VIP has 18 cells from 15 donors. Converting with t df: VIP sag p 0.024 → about 0.04; fig3ik (b,a) Rin p 0.047 → 0.050 to 0.056, which crosses 0.05.
6. [does not affect a conclusion] Cells 17 and 19: the main-reading full LMM reports `converged=False` (rows 0 and 2 of cell 17, row 2 of cell 19). Convergence of the per-subclass fits is not reported. The per-subclass VIP GEE returns NaN in every reading, with no explanation.
7. [does not affect a conclusion] `sag_rin`: Rin under reading (a) uses peak deflection, so rin_a = R_ss/(1 − sag). I confirmed this on synthetic steps: 312.5 against 250 MOhm at sag 0.2. Sag and Rin are therefore built-in collinear in the Fig. 3 models.
8. [does not affect a conclusion, but affects the fig3ik slope] `impedance`: LOWESS with frac 0.04 on a linear frequency axis is about a 1.6 Hz window. On a synthetic slow resonance (true fres 1.65 Hz, Q 1.34) the helper gives Q 1.19 (a) or 1.09 (b). Q is compressed, which may explain part of the threefold smaller sag slope. On strong resonances the helper is accurate (fres within 0.1 Hz, Q within 2%), and impedance units (MOhm) are correct.
9. [does not affect a conclusion] Cell 4: `soma_depth_um` is merged, which is filled for only 22 rows. `Depth_from_Pia_microns` is filled for all 419 rows.
10. [does not affect a conclusion] Places where the claims file misreads the paper (reported, not corrected):
    - The sample-size criterion and header say the dandiset holds Table S1's "Chartrand" donors. In fact 43 of the 53 dandiset donors are listed as "AcuteLDPublished". I checked the helper's `TABLE_S1` against the PDF text layer: dataset and disease match for every donor.
    - The header says the Lee et al. 2023 and cultured recordings have no public source; DANDI:000636 holds them.
    - Table S1 has both "Area" and "Structure" columns; the helper reads only Area. This affects 2 cells with no lobe.

**C. Not checked**

- Whether the DANDI:000020 and 000636 files contain 20 s chirp sweeps. An output listing the stimulus names in a sample of those files would settle it.
- The sweep exclusions: 50 chirp sweeps and 211 long squares were dropped for exact-zero voltage, and 8 cells lost all their chirps. A per-file table of dropped sweeps and reasons would show whether recordings with a leading zero are falsely excluded.
- How the paper's fres distribution is reached. A histogram of fres/Q per reading next to Table S3, plus the count of cells with fres > 1 Hz and Q ≤ 1.05, would show whether a third reading is needed.
- Satterthwaite-df p-values (for example via lmerTest), and convergence flags for every per-subclass fit.
