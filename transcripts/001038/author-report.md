I did steps 1 to 6 for dandiset 001038 and ran the handover. The entry passes `check` and runs in 182 s from a clean environment, and the executed numbers match the conclusions. I used the paper's full text (open access, PMC10545540), saved under `paper/`. I pinned version 0.241111.1719: it is the only published version, the paper cites none, and the draft has the same files and differs only in metadata.

**1. Outcomes per claim**

| Claim | Outcome |
|---|---|
| recording-counts-locomotion | not reproduced (50/28/82/89/85 vs 42/22/47/74/75) |
| recording-counts-stimuli | reproduced (all 8 counts exact) |
| fig2f-xcorr-direction | reproduced |
| fig2i-trough-lag | partially reproduced (Calb1 0.140 s; the code's timing gives 0.160 s) |
| fig2jk-pca-variance | reproduced (58.32 / 22.09%, both just inside tolerance) |
| fig2l-pc-angles | reproduced |
| fig2g-event-counts | reproduced |
| ed7f-prob-transient-after-event | reproduced |
| ed6f-dec-peak-timing | partially reproduced |
| fig5ab-transient-scaling | partially reproduced |
| fig4g-reward-response | partially reproduced (the code's windows give the paper's 7.90 / 12.40 / 5.88 exactly) |
| fig4g-anxa1-no-reward | reproduced |
| fig4g-airpuff-response | partially reproduced (DAT 2.69 vs 5.3) |
| fig4h-reward-vs-airpuff | reproduced |
| fig4i-reward-size | partially reproduced |
| ed8f-rest-reward-same | reproduced |
| fig6c-kmeans | reproduced (92.6%) |
| fig7f-soma-axon-correlation | reproduced |
| ed9c-snc-stimulus-responses | reproduced |
| ed9k-snc-variance-explained | reproduced |
| ed1h-aldh1a1-depth | partially reproduced |
| ed1i-aldh1a1-reward-locomotion | reproduced |
| fig3a-overlap-locomotion | reproduced |
| fig4l-overlap-stimuli | reproduced (counts exact) |
| snrna-nuclei-qc (GEO data, counted apart) | reproduced (12,065 nuclei exactly) |
| snrna-anxa1-within-aldh1a1 (GEO data, counted apart) | reproduced |
| snrna-clusters, scrna-meta-integration | blocked: not_runnable (the paper's pipeline is Seurat/LIGER in R) |
| histology-anxa1-cre | blocked: other (needs manual cell counting on images) |

**2. What was found about the dandiset**

- **Contents:** it holds the paper's photometry. The stimulus analyses recover the paper's recording and mouse counts exactly, and no recording is deposited twice.
- **Exclusion flags:** the running-time and 405 nm artifact flags are not in the files. I recomputed them with the paper's code. The stimulus counts then match, but the locomotion criteria select more striatal recordings than Fig. 2 reports (for example Anxa1 82 against 47), and I could not find out why.
- **`coordinates` column:** described as (AP, ML, DV), but the data and the paper's code show it holds (ML, AP, DV).
- **`cross_correlation_with_acceleration` column:** holds the 405 nm control's peak correlation with acceleration, not that of dF/F.
- **dF/F series:** normalized so the largest transient is 1, which the files do not say.
- **Events table:** lists consumed rewards only.
- **Subjects:** three subject ids ending in "L" are mice that also have ids without it, so the archive's 105 subjects are 102 mice.
- **Archive metadata:** the published version has a malformed DOI link to the paper (fixed in the draft) and a thin asset summary.
- **Code against Methods:** the code's response windows (0 to 0.5 s minus −0.55 to −0.05 s) differ from the Methods' (+0.05 to +0.55 s minus −0.5 to 0 s), and the paper's numbers come from the code's. The code also reports peak and trough times one or two bins late.
- **Paper inconsistencies:** the Results text swaps the Vglut2 and Calb1 reward p-values relative to the Fig. 4g legend. The Fig. 2f legend gives 10 Anxa1 mice where the Methods give 9. Extended Data Fig. 9k and the Methods give different variance values.

**3. Where the protocol was unclear, wrong or missing something**

1. **Methods and code disagree, and the code reproduces the paper's numbers.** I followed the protocol: the Methods give the main result and the code a variant. This turns several claims into "partially reproduced" even though the code's windows match the paper exactly. The protocol does not say whether this deserves its own outcome.
2. **A count claim fails, and other claims use its selection.** I listed `depends_on` and still tested the dependent claims on the larger selection, with a deviation on each. The protocol only covers a link that "holds in part" for outside data.
3. **Analysis parameters taken from the paper's code** (the overlap-region circle centres, pixel-to-mm offsets). I did not treat them as `inputs`, which I read as outside data, and recorded the repository and commit in the notebook header instead.
4. **`not_runnable` for R-only software.** I applied it to the Seurat/LIGER claims without trying an install, since R packages cannot go into the entry's Python lock file. Manual cell counting fit no category, so I used `other`.
5. **The "10% of the reported value" tolerance** is meaningless for a value near zero (Anxa1 −0.5) and odd for angles. I made the Anxa1 part a separate absence claim and kept 10% for the angles.
6. **Random seed:** MATLAB's k-means seed cannot be repeated, so I fixed the criterion as the median accuracy over 100 seeds.
7. **"Delete or overwrite, look first":** not applicable here.
8. **Before writing the criteria,** I saw the selection counts and, while debugging the loader, one test session's values. I stated this in the claims file header.

**4. Runtime and failures**

- The notebook runs in about 3 minutes.
- My first metadata scan took 30 minutes. h5py serializes calls across threads and every download URL needed its own API request. I fixed it with a process pool, the bulk asset listing, and BLAS limited to one thread.
- Early runs crashed on files that store two values per row in `normalized_fluorescence`, which I then handled.
- Nothing fails now. I could not trace why the locomotion counts are larger: the paper's 4.4 GB MATLAB table on Zenodo, which carries the exclusion flags, was not practical to parse.

Files are in the repository root:
- `claims/001038/10.1038-s41593-023-01401-9.yaml`
- `attempts/001038-azcorra-2023-01.yaml`
- `entries/001038-azcorra-2023/`
