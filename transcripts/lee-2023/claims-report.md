I wrote `claims/000636/10.1126-science.adf6484.yaml`. The quote checker reports 39 claims, 38 quotes and 0 problems, both against the version-of-record text alone and with the preprint added. Nothing was committed.

**Text read**
- **Main text:** the author manuscript of the version of record (PMC12229143). It has the main text, the Materials and Methods and the legends of Figs. 1 to 6.
- **Supplement:** not supplied. The legends of figs. S1 to S9 and Data S1 and S2 are missing, and there is no PDF, so no figure could be read.
- **Preprint:** I also read the bioRxiv preprint (10.1101/2022.11.08.515739). It has an earlier set of supplementary legends (S1 to S5), and I used it only for test names and the direction of the sag change. Every quote is from the version of record.
- **Decision to go ahead:** the protocol says to stop when a supplement the results rest on is missing. I went ahead because the Methods are in the main text and every finding that cites a supplementary figure is stated in a main-text sentence. Earlier claims files in the repo did the same. Those claims rest on that sentence, and the file says so.
- **Code:** I read github.com/AllenInstitute/human_patchseq_gaba at commit 5eb357a. It holds one R notebook for the gene-expression analyses and per-cell tables: metadata with `nwb_id`, IPFX features, morphology features, DBC calls and donors. I read only the tables' column headers. There is no code for the electrophysiology or morphology statistics; the Methods say those were run in Prism or Python.

**Claims**
- 39 claims: 1 link claim, which matches the NWB files to the repo tables by `nwb_id` and checks recomputed IPFX features, and 38 findings.
- All 38 findings have quotes, 12 have reported statistics, and all 39 have criteria.
- By data: 18 `with_labels` (the dataset plus cell labels from the repo), 17 `elsewhere` (transcriptomes, morphology, MERFISH, snRNA-seq) and 4 `with_inputs` (the mouse comparison).

**Details left open, and the readings named**
- **The "84 features":** (a) the 84 non-chirp columns of the repo's feature table (93 columns minus 9 chirp), or (b) all 93.
- **Which sweep a feature comes from** (AP width, upstroke/downstroke ratio, peak, latency): rheobase, rheobase + 40 pA, 3 ms short square or ramp. ISI is read as `mean_isi_rheo` or `mean_isi_hero`; adaptation ratio as `isi_adapt_ratio` or `adapt_hero`.
- **Subclass counts:** with SST FRZB revised into PVALB, or the original subclass label.
- **"Supragranular" in the human vs mouse comparison:** L2 or L3 only, or all layers.
- **Comparison group for "DBCs have higher sag":** non-DBCs of SST CALB1 and SST ADGRG6 (Fig. 5C), or MC and sparse SST cells (Fig. 4C).
- **Depth-matching of the 9 culture and 10 acute PVALB WFDC2 cells:** the method is open.
- **UMAP claims:** no UMAP parameters or overlap measure are given anywhere, so I fixed nearest-neighbour measures in the criteria and said so in each.
- **Tests the code settles:** the ion-channel gene test is a per-gene linear model adjusted with R's default, which is Holm, though the code comment says FDR. I followed the code.
- **Tests the missing legends would give:** for figs. S6, S9 and the bouton-density claim I read the tests from the Methods and the Results.

**Missing from the paper**
- The supplementary materials: figs. S1 to S9 legends and Data S1 and S2.
- Which features Fig. 2H and fig. S8B show.
- The directions of the human vs mouse differences, which the Results don't state.
- Where the MERFISH data are.
- Where the mouse data are: Gouwens et al. 2020 is cited as ref. 16, with no location given.
