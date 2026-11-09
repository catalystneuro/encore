I filled in verdicts for the three papers that had none and kept the checks' `primary` for the first. `papers/match/001603.yaml` passes validation.

| Paper | Verdict | Deciding evidence |
|---|---|---|
| 10.1038/s41593-025-02111-0, Van der Molen 2025 | **primary** (by checks, kept) | Its Data availability says: "Raw and curated electrophysiology recordings can be found here https://dandiarchive.org/dandiset/001603". The dataset description says the dataset "contains all data used for" this paper. |
| 10.1038/s41467-022-32115-4, Sharf 2022 | **partial** | The archive metadata says "Sourced data came from: Sharf et al. 2022 Nat. Comm. (HO1-4)". The dataset only has spike-sorted data from those four organoid slice recordings. The raw recordings are in Dryad (doi:10.25349/D9031Z) and the scRNA-seq data in GEO (GSE207749). |
| 10.1038/s42003-025-08632-5, Alam El Din 2025 | **partial** | The archive metadata says "Alam El Din et al. 2025 Comm. Bio. (HO5-8)". These are spike-sorted data from four whole-organoid HD-MEA recordings. The paper's calcium imaging, plasticity, stimulation and RNA-seq (GEO GSE301725) findings rest on data not in the dataset. How much of its MEA work those four recordings cover is unclear, so this one leans toward `other_data`. |
| 10.1038/s41467-020-18620-4, Yuan 2020 | **partial** | The archive metadata says "Yuan et al. 2020 Nat. Comm. (Pr1-4)". These are spike-sorted rat primary-culture recordings, which bear on the paper's network burst analysis. Its findings on the recording platform, axon tracing, retina and spheroids rest on raw data in the ETH Research Collection (doi:10.3929/ethz-b-000431730). |

Three sourced papers are only thinly covered: the dataset holds spike-sorted data from four recordings of each. An attempt should use the primary paper.

The Pr5-8 recordings come from Bartram et al. 2024 eLife, which the archive does not list among its related papers.
