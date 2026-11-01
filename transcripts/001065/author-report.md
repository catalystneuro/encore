I finished steps 1 to 6 and wrote the handover. The entry's checks pass and the notebook runs clean in a fresh environment (8.1 min). Nothing is committed.

The entry is `entries/001065-dembrow-2024/`, the attempt record is `attempts/001065-dembrow-2024-01.yaml`, and I added the link claim `link-cells` to the claims file. No claim's statement, expected values or criterion was changed. The one other edit to that file adds `depends_on: link-cells` to each claim that uses outside labels, as protocol step 1.4 asks.

## 1. Outcomes (42 claims: 41 from the reader plus the link claim)

| Outcome | Claims |
|---|---|
| Reproduced (21) | link-cells, cohort-animals, cohort-recordings (reading b only: 294 cells vs 300), fig3e (assumed), fig3-spc, fig3h, fig4c, fig4e, fig4g, tcx-et-types-no-difference, fig5-tap-root, fig6a, fig6b, fig6d, figs6b-lower-rin, figs6b-avg-gain-no-difference, fig6h, figs6c, figs6d, fig6k, figs7g (assumed) |
| Partially reproduced (8) | fig5c, fig5e (assumed), fig6-depolarization-block, figs7-cv-isi, fig7-oscillation-frequency-vm (assumed), figs7-oscillations-with-blockers (assumed), fig7l (assumed) |
| Not reproduced (6) | fig3a, fig4a, fig4-interaction-small, species-no-effect, figs6b-higher-rheobase, fig6j |
| Not reproduced, assumed (1) | fig7k |
| Blocked, `other` (7) | patchseq-qc-177, cs-map-to-l5et, fig4h, patchseq-genes-area, fig1-snrna-genes-et, fig1-snrna-genes-area, fig5b |

The 7 blocked claims rely on data held elsewhere: Patch-seq reads in SRA, snRNA-seq in NeMO, and layer-aligned reconstructions in the Brain Image Library. I did not attempt them within the time limit. Two results sit on a margin:
- **fig3e:** the 50% held-out score is 79.2%, only 0.1 point above its tolerance bound, and it passes only with stratified splits.
- **fig7-oscillation-frequency-vm:** the criterion has no "partially" rule. I used partially reproduced because three of its four conditions hold.

## 2. Dataset, assumptions, questions

**What the dataset holds**
- I pinned 0.241028.1559 because it is the only published version and the paper cites no version.
- There are 294 MIES NWB files, one per cell, from 57 subjects.
- The files have no area, preparation, subclass or drug labels. These come from the Zenodo tables, matched by `cell_id`. Every file matches a table row, and the features I computed agree with the table's values (median Spearman 0.952 over 39 features).

**Findings recorded in the attempt**
- 47 of the code table's 341 cells are absent from the dataset.
- One file names a different donor from the table (Q19.26.009 vs Q19.26.012).
- Two files say *M. mulatta* where the table says *M. nemestrina*.
- One subject has sex U, and one has age `P1Y/`, below the 2 to 19 years the paper reports.
- Five files have current commands up to 16 nA, beyond the 4 nA the Methods give as the limit.
- Files hold several runs of each protocol, and nothing marks which ones the paper used.
- The table stores SFA as the inverse of the Methods' ratio.
- The Figure 6D/E legend contradicts the Results.
- The deposited morphology table has 19 reconstructions where the paper reports 23.

**Assumptions**
- The classifier's random splits are stratified by class (fig3e, fig5e).
- The rebuilt Figure 7 oscillation pipeline: the R code was not deposited, so I followed the Methods with standard choices for the gaps.
- Figure S7G uses only sweeps with at most 200 spikes. Without that limit the claim fails.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings)
- Were the classifier splits stratified?
- How were the oscillations computed (baseline fit, filter, spline, strength measure, which sweeps)?
- Which sweeps feed the features, and how was the half-width of late spikes measured?

I asked a reader nothing; I found no misreading in the claims file.

## 3. Where the protocol was unclear or missing something

1. **Elsewhere claims not tried for lack of time.** Step 4 lists `too_large`, `not_runnable` and so on, but none fits data that simply wasn't attempted in the time. I used `other` and said so in the notes.
2. **The paper's own derived tables.** The protocol doesn't say whether the paper's deposited per-cell features may stand in for raw data held elsewhere. I used the morphology table for fig5 and recorded that as a deviation.
3. **Adding `depends_on` to the reader's claims.** Step 1.4 says dependent claims list the link claim, which means editing claims the author can't otherwise change. I added only the `depends_on` entries.
4. **Criteria with no "partially" rule.** When some of a criterion's conditions hold, it isn't clear whether partially reproduced is allowed. I used it only where most conditions hold, and explained each case.
5. **When the link claim's criterion is written.** Step 1.4 doesn't say. I wrote it after a first look at how my features compared with the table, and recorded that as a deviation.
6. **Clock check.** The suggested methods (trial tables, decoding) don't fit intracellular sweeps. I checked instead that spikes fall inside the current step: 11,925 inside, 11 outside, first-spike latency 4.2 ms.

## 4. Runtime and failures

- The run took about 1 h 50 min (04:29 to 06:17 UTC).
- The first metadata survey was slow (25 min). After that, a full feature extraction took about 7 min.
- No file failed to load. The final notebook passed with no errors or warnings.
- Untracked dotfiles (`.bashrc`, `.idea` and others) are in the working tree. They were not there at the start, and I did not create them deliberately.
