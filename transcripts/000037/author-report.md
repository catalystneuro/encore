I've finished steps 1 to 5 of the Author section and ran the handover (step 6). The entry is `entries/000037-gillon-2023/`, with the record in `attempts/000037-gillon-2023-01.yaml` and three questions in `questions/000037.yaml`. `entry.py check` and `all` both pass, and the notebook ran in 431 s. Nothing is committed.

**(1) Outcomes (35 claims)**

| Claim | Outcome |
|---|---|
| table1-subjects, cohorts-by-plane, sex-split, sessions-total | reproduced |
| table2-sessions | not reproduced: 43 of 50 sessions agree in every recorded field; 45 were needed for partial |
| qc-failures | blocked, metadata_insufficient (the files hold no QC status) |
| session-schedule, acquisition-rates, roi-noise-rejection, roi-count-ranges | reproduced |
| imaging-depths | not reproduced: 433414 is at 60 µm, and the criterion admits only 50 or 75 |
| tracked-roi-totals, tracked-sessions-overlap | reproduced |
| fig8a and fig8b final matches and conflicts (4 claims) | reproduced |
| fig8-somata-less-order-dependent | blocked, data_missing |
| gabor-sequence-structure | partially reproduced: 13 of 340,000 images in 4 sessions fall outside 300 ms ±10% |
| visual-flow-structure, session-stimulus-durations, inconsistent-fractions, inconsistent-blocks | reproduced |
| fig5-example-responses | blocked, methods_underspecified (question asked) |
| fig5-consistent-vs-inconsistent | blocked through its dependency on the claim above (its own test gives partial) |
| fig6-behaviour-all-mice, fig7a-snr-above-1, fig7a-source-link, fig9-onset-offset-transients | reproduced |
| fig7a-snr-stable, fig7b-signal-stable, fig7c-correlations-similar | blocked, methods_underspecified: the criteria's two readings disagree |
| fig7c-high-correlation-fraction | blocked through its dependency (0.0178% measured, outside the 0.005 to 0.015% band) |
| file-sizes, download-33-files | reproduced |

Totals: 23 reproduced, 1 partially reproduced, 2 not reproduced, 9 blocked.

**(2) The dataset**

- **Version:** I pinned 0.230426.0054. The paper's reference 13 cites it by DOI in the Crossref record; the Europe PMC text prints the reference without the DOI. Version 0.240209.1623 has the same blobs plus a CHANGES file.
- **Start times:** they carry a Pacific offset, but their clock values are what Supplementary Table 1 calls UTC. This puts four session dates a day after Table 2.
- **Depth:** mouse 433414 is recorded at 60 µm; Table 2 gives 75.
- **Missing metadata:** the files hold no QC result, local session number, stimulus seed or plane. The plane follows from the depth. The paper's 33 analysed sessions had to be selected using Supplementary Table 1, which matches the paper's Tables 1 and 2.
- **Flow stimulus units:** square size and speed are in pixels with no geometry to convert to degrees. Their ratio, 6.09 per second, is within 3% of the paper's 6.25.
- **Storage:** the 28 dendritic files store dF/F gzip-chunked, which is slow to stream through h5py.
- **Clock alignment:** shown in 48 sessions; it could not be shown in 777496949 (15 ROIs) or 838633305 (failed QC).
- **Fig. 8 inputs:** the paper's repository has per-ordering matching counts for only 2 of 13 mice.
- **No duplicates:** no recording is deposited twice.

**Questions asked:**
- fig5-example-responses: which Gabor panel the per-plane rule uses. Panel a or b alone gives partial; both panels give not reproduced.
- fig7c-high-correlation-fraction: what reading (c) means. Also, the analysed set has two L2/3 dendritic mice, not the three the criterion assumes.
- imaging-depths: does "any of 50, 75" exclude 60 µm, which lies inside the paper's 50 to 75 µm range?

**(3) Where the protocol was unclear or did not fit**

1. Step 1.3 says to pin the version the paper cites "as the claims file gives it"; the claims file gives none. I took the DOI from the Crossref reference and said so in the notebook header.
2. The rule "a claim that depends on a blocked claim is blocked" also blocks dependents whose own test is fully specified, when the parent is blocked only on its decision rule. I applied it literally and put the dependents' results in their notes.
3. Step 1.6 covers missing method details, not an ambiguous decision rule inside a criterion. For Fig. 5 I asked a question and blocked the claim.
4. An author has no channel for a criterion stricter than the claim's own statement (imaging-depths). I followed the criterion and asked a question.
5. gabor-sequence-structure's criterion has no partial rule. I used partially_reproduced, based on the protocol's definition.
6. The several-readings rule covers the paper's text, not ambiguous metadata in the dataset. For the time-zone problem I used the dates as the files state them and showed the UTC reading as a variant. This decides table2-sessions: 43 agreeing sessions gives not reproduced, 47 would give partial.
7. Streaming through remfile and h5py was too slow for the chunked files. I stream each whole basic file into memory with parallel HTTP range requests; nothing touches disk.
8. The `data` categories have no slot for the paper's own supplementary table being used to select sessions. I listed it under `inputs` and in the deviations.
9. The notebook may not read local paths, so it cannot check that Supplementary Table 1 matches the paper text. I checked this while preparing and stated that it was not run in the notebook.
10. The suggested clock checks (decoding, shifted labels) don't fit this design directly. I compared the population response at grey-screen transitions against 500 time-shifted copies.

**(4) Runtime and failures**

The notebook takes 417 to 431 s and streams 25.2 GB. Peak memory was about 9 GB, measured in a development run outside the notebook. My first loader took 16 minutes because of the chunked dendritic files; the in-memory streaming fixed it. Nothing fails in the final run.
