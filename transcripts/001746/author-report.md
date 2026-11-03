I finished steps 1 to 6: the entry is locked, checked and run, the attempt record is written, and the handover is built. Nothing is committed.

## 1. Outcomes (33 claims: the file's 32 plus one link claim I added)

| Claim | Outcome |
|---|---|
| patchseq-cell-table-link | Partially reproduced |
| morph-table-link (added) | Reproduced |
| patchseq-sample | Partially reproduced (10 subjects, not 12) |
| patchseq-mapping | Partially reproduced (inhibitory 30, not 34) |
| fig2a-subclass-counts | Partially reproduced (L5 IT FEZF2 125, not 143) |
| ven-map-et-ct | Reproduced (14 and 15) |
| fig6f-ven-subtype-mapping | Partially reproduced (12 VEN-L, not 10) |
| fig2d-l23it-small-tau | Reproduced, rests on an assumption |
| fig2f-l23it-narrow-ap | Partially reproduced (second-lowest median) |
| supp11-rm-itrorb-l6pc | Partially reproduced, rests on an assumption |
| supp11-l5it-threshold-latency | Reproduced |
| supp11-ven-broad-ap | Not reproduced |
| ven-firing-rate-variability | Not reproduced |
| l5et-vs-l5it-sag-rm-rate | Reproduced, rests on an assumption |
| supp9-venl-more-distinct-from-ct | Reproduced, rests on an assumption |
| morph-more-distinct-than-ephys | Reproduced, rests on an assumption |
| supp11-l5et-deep-sag, fig3e-phase-peak-index, fig3d-saddle-phase-plane | Blocked: methods underspecified |
| fig4ac, ext9cd, supp8 (recordings without RNA) | Blocked: data missing |
| fig4i-peak-index-ais-distance-real | Blocked: metadata insufficient |
| fig7c-tau-rna-distance | Blocked: too large (cluster labels only in a 23 GB tar.gz on GEO) |
| 9 `elsewhere` claims | Blocked: other |

## 2. What was found

**Dataset.** I pinned 0.260825.0222, the only published version; the draft lists the same files.
- The 462 files hold Patch-seq step recordings with no cell type, subtype or transcriptomic type. Those come only from the code's table `metaInfo_ephysio_patchSeq.csv`.
- Five pairs of files hold identical traces under different cell IDs, four of them under different subjects. One pair has two different clusters in the table.
- The table names one file twice (cell n172) and has no row for the file of cell s172.
- There are 10 subjects against the paper's 12.
- Every file has the same placeholder session start, and two session IDs carry another subject's date.
- The stimulus is stated in amperes but holds pA, and its starting time is NaN.
- Five files have a device name that does not fit their sampling rate.

**Assumptions.**
- The claims file's FDR family is the 39 features of the code's table, but 19 of them are defined neither in the Methods nor in the paper's package PatchAnaLab. I bounded the 39-feature FDR, and where the bounds do not decide, the 20 Methods features decide.
- For l5et-vs-l5it I read "deeper sag" as sag ratio, the only sag measure in the code's table.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- Which measure does "deeper sag" use?
- How are the 19 undefined features computed?
- How were the phase peaks placed by hand? An automatic reading agrees with the code's hand-read values only loosely (Spearman 0.55). The hand-read values themselves do reproduce the Fig. 3e result.

**Questions asked of a reader:** none.

## 3. Where the protocol was unclear or did not fit
1. Taken literally, the link criterion fails over one row's subject, a duplicate row with no type that no analysis uses. Taken that way, 18 dependent claims would be blocked. I recorded partially reproduced and put the strict reading in a deviation.
2. Some criteria define only "reproduced" (fig2f, fig6f, mapping). Where the effect held in part I used partially reproduced.
3. The supplement was under `paper/` for me but not for the reader. The protocol does not cover an author with more text than the reader. I used it only for method details, citing the passages.
4. No `blocked_by` reason fits "tested under another dandiset's claims file", so I used `other` for the nine `elsewhere` claims.
5. The schema forbids `inferred` on link claims, and an author-added link has no paper quote. I put the provenance in the criterion. I also added the new link to the morphology claim's `depends_on`.
6. It is not said whether the header table may give outcomes; `handover` does not strip it. I first wrote outcomes there, then changed it to tested/blocked only and re-ran.
7. "Count each recording once" does not say what to do when the two copies carry different labels. I kept both files and reported the pair.

## 4. Runtime and failures
- The notebook runs in about 166 s and reads all 15 GB, each file whole into memory.
- `tools/entry.py all` passes with 0 errors, and the handover is built in `executed/001746-liu-2026/handover/`.
- The work took about 40 minutes of the 5 hours.
- Nothing failed in the final run. The untracked dotfiles and `scripts` in the repository root are sandbox device mounts, not my files.

Files are in `entries/001746-liu-2026/`:
- reproduce_liu_2026.ipynb
- aic.py
- README.md
- entry.yaml
- requirements.in
- requirements.lock.txt

The record is `attempts/001746-liu-2026-01.yaml`, and the link claim was added to `claims/001746/10.1038-s41556-026-02009-4.yaml`.
