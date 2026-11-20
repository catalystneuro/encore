I stopped without writing any claims, because the version of record's main text and Methods are missing from `paper/`. `claims/clark-2026.yaml` does not exist.

**What's in `paper/`**

`10.1038-s41593-026-02452-4.txt` says it is the version of record, but it is a mix of three things:
- **Reference list:** the version of record's, 73 references, with DANDI:000939 as reference 39 and the code on Zenodo as reference 73.
- **Main text:** the bioRxiv preprint (doi:10.1101/2025.01.26.634933, posted 26 January 2025), not the published article. Every page carries the bioRxiv license footer. This part runs from the Introduction to the Discussion and the preprint's own Supplementary Information, with Figures 1 to 8 and a softplus activation.
- **Supplement:** from line 2673, the version of record's supplement ("Supplementary Notes 1 to 4"). It matches the PDF `...MOESM1_ESM.pdf`.

**Why I stopped**

- **The published Methods are missing.** The version of record has a Methods section that is not in the file. Its supplement depends on it throughout: it cites "Methods Eq. 13", "Eq. 18", "Eqs. 26 and 27", and "Methods, 'Model settings'".
- **The published paper was revised.** For example, its "Setting 3" uses an erf activation, φ(x) = 1 + erf(β√πx/2), and the supplement cites figure panels such as Fig. 6f. So the preprint text can't stand in for the published main text, and its numbers may differ.
- **Claims from a preprint would be thrown out.** docs/pipeline.md says that once a paper is published, an attempt whose claims were read from the preprint is deprecated and its claims file removed.

**What's needed:** the version of record's full text, meaning the main text with its Methods, from Nature Neuroscience (doi:10.1038/s41593-026-02452-4). The store's text header should also be corrected, since it labels the preprint body as the version of record.

**Not done:** with no claims written, there are no quotes, statistics or criteria, and no open details or readings to report. I did not read the paper's code (Zenodo 10.5281/zenodo.21829584) or run the quote checker, and I did not look at the dataset.
