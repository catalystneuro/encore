**Round-2 verifier report: 000034-buccino-2020-01 (Buccino et al. 2020, DANDI:000034 v0.211030.0713)**

**1. Outcomes**

The claims file has 24 claims: 1 link claim (`recordings-as-described`) and 23 findings. The attempt record has 24 outcomes: 1 reproduced, 1 partially_reproduced and 22 blocked.

| Claim | Attempt outcome | Agree? |
|---|---|---|
| recordings-as-described | reproduced | Yes. Cell 18 prints "All hold: True (15 of 15)". |
| fig4a-curators-agree | partially_reproduced | Yes. Cell 24 gives 226 (±22.6), 351 (±35.1) and 64.39% (64.2 ± 6.42). The 174 is untested, so under the criterion the outcome is at least partially reproduced. |
| The 20 other findings, fig1b to fig3s2 (fig1b, fig1c, fig1d, fig1s2, fig1s3-s4, fig2c, fig2s1a, fig2s1b, fig2d, fig2e-ks2-unit-types, fig2e-ks2-curated-unit-types, fig2e-tdc, fig3a, fig3b, fig3c, fig3s1-ks2-ic, fig3s1-pairs, fig3d, fig3s2) | blocked (not_runnable) | Yes, they are blocked. Cell 21 shows no MATLAB, GPU or MPI, and cell 9 shows no sorter output in the dandiset. On the label, see 3. |
| fig4b, fig4c, fig4d | blocked (not_runnable) | Yes, for the same reasons. |

I found no new misreading of the paper in the claims file. The fig4a criterion says "partially reproduced when … 174 is not". The attempt applies it to a 174 that is *untested*, not to one that fails. That is the same lower-bound reading I used in round 1, and the record states it openly.

**2. Statements the printed outputs do not support**

- **The bulk-read numbers in the attempt record are stale.** Cell 21 prints "One ranged GET of the first 512 MB … 6.0 s, **85 MB/s**", and whole-file times of **1.2 to 5.5 min**. The attempt record says "ran at **47 MB/s**, so each recording could be read whole in **2 to 10 min**" in two places:
  - the notes of all 22 blocked outcomes;
  - all 22 round-1 responses.
- **The streaming finding in the attempt record (kind: other) is also stale.** It says "about **0.1 to 0.2 s per chunk** … would take **8 to 20 h**". Cell 21 prints s_per_chunk of 0.080 to 0.142 and hours_whole_file of 5.6 to 15.5.
- **Summary (cell 26), mouse-units bullet, overstates the case.** It says the values are "consistent with raw Neuropixels counts **and not with microvolts**". Cell 16 and the attempt finding say only that they are consistent with raw counts, and that "the file holds nothing to show which". The outputs cannot rule out microvolts.
- **Cell 13's print label still asserts the scale.** It reads "(x conversion 1e-6 = volts, i.e. microvolts)", which contradicts cell 16's "The scale of the mouse values is not checked".
- **Cell 25 is selective about the minimum-score scan.** It says the count stays "inside the tolerance throughout", which is true of the count (231 to 208). But at match_score 0.8 the ratio is **56.37%** (cell 24), which is outside 64.2 ± 6.42 (lower bound 57.78). The attempt notes have the same omission. This does not change the outcome, because the criterion fixes the default score of 0.5.
- **Cell 0 contradicts its own table.** It says "Every finding except the presence of the recordings rests on running six spike sorters". Its own table, and cells 23–25, test part of fig4a from the curations alone.
- **Cell 22 and the notes overgeneralise the six-sorter need.** Cell 22 says "Every sorter claim needs the output of all six sorters". The blocked notes for fig2e-ks2-unit-types, fig2e-ks2-curated-unit-types and fig3s2 say "Needs the six sorters' output". Those three claims need Kilosort2 alone. They are still blocked, because Kilosort2 needs MATLAB and a GPU.
- **Some statements in the attempt record match no printed output:**
  - "the archive's species summary lists only house mouse" (finding, metadata_insufficient);
  - the pip results for Tridesclous, SpyKING Circus and HerdingSpikes, which cell 22 marks "not run here".

The README checks out: every sentence is consistent with the outputs. Apart from the points above, every "**Result:**" sentence (cells 19 and 25), the other Summary sentences and the other notes match the printed numbers. For example: 248 channels, 27,000,000 frames, 600.00 s, 250 units, 270.01 s, 135.73 s, 23199.09 Hz, 258 and 319 units, and 0.88, 0.86 and 0.63 within 3 frames.

The attempt record states my round-1 reasons faithfully, mostly verbatim. "Blocked by other." is appended to each, which matches my table. The fig4a reason combines my B1 with my request in C, which is fair. The cell numbers quoted in my reasons refer to the round-1 notebook, and the cells have since shifted: the link check is now cell 18 and fig4a is cell 24. The record does not say so.

**3. Round-1 points**

- **B1 (fig4a filed as blocked): resolved.** It is now partially_reproduced, with matching text in cell 25, the Summary and the README.
- **B2 (not_runnable is not an allowed reason): resolved by the author's explanation.** The author cites the attempt schema and protocol step 1.5, which define not_runnable as software that cannot be installed in a locked environment. That fits this case. The protocol text was not among my materials, so I cannot check the citation myself, but I withdraw the point. The record already notes the disagreement.
- **B3 (streaming time used as a block): resolved in substance.** A bulk read is now timed, and reading time is no longer a reason. However, the record's numbers do not match this run (see 2).
- **B4 (mouse units): resolved.** Cell 9 shows no gain or channel_conversion column, cell 16 now discusses the scale, and a finding was added. The Summary still overstates it (see 2).
- **B5 (MEArec filtering): resolved.** Cell 14 prints the spectrum by band and the noise after band-pass, and cell 16 concludes the traces are not band-passed.
- **B6 and B7:** no action was needed.
- **C (checks I asked for): all done.** These were the HDF5 trees of both curated files and the mouse file (cell 9), the bulk-read timing (cell 21) and the electrode gain columns (cell 9). The trees confirm that the 174 cannot be obtained without a Kilosort2 run.

**Remaining:** nothing that bears on a conclusion. Two corrections are still needed, but neither changes an outcome:
- Replace the stale numbers in the attempt record (47 MB/s, 2 to 10 min, 0.1 to 0.2 s per chunk, 8 to 20 h) with the printed ones (85 MB/s, 1.2 to 5.5 min, 0.08 to 0.14 s per chunk, 5.6 to 15.5 h).
- Soften the Summary's "not with microvolts", and fix the label in cell 13.
