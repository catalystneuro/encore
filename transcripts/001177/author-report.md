I've finished protocol steps 1 to 6 for dandiset 001177 and Zhuang et al. 2025. The entry passes `check` and runs clean in a fresh environment (246 s). The handover is in `executed/001177-zhuang-2025/handover/`. Nothing is committed.

The paper is open access (CC BY), so I used the full text and its Supplementary material from Europe PMC; they are saved under `paper/`. I pinned 0.250902.2127 because it is the only published version and the paper cites the dandiset without a version. The notebook checks that the draft has the same 56 files and sizes.

## 1. Outcomes

| Claim | Data | Outcome |
|---|---|---|
| fig4bc, fig4dg, fig4hk, figs5d, figs5ef, fig6fg, fig6hi (unit level) | dandiset | blocked: data_missing |
| mua-ppx-park-vs-ctrl | dandiset | partially_reproduced |
| mua-saline-no-change | dandiset | blocked: other (only 1 of 4 saline sessions is long enough) |
| mua-response-shift-first-fourth | dandiset | partially_reproduced (control mice shift too) |
| fig1b-th-depletion | Zenodo | reproduced (under one of three background readings) |
| fig1c-rotarod | Zenodo | reproduced |
| fig1fg-baseline-similar | Zenodo | reproduced |
| fig1f-ctrl-ppx-no-change | Zenodo | reproduced (10 of 16 mice) |
| fig1g-park-ppx-impulsive | Zenodo | reproduced |
| fig1ik-a-k-auc | Zenodo | partially_reproduced (K not significant) |
| figs2ik-washout | Zenodo | partially_reproduced |
| fig2d, fig2e, fig2fh (A77636) | Zenodo | reproduced (fig2fh matches the paper's p-values) |
| fig2bc and fig5cf (locomotion) | Zenodo | blocked: metadata_insufficient (no injection time) |
| fig3a-a-correlates-dms | Zenodo | not_reproduced (r = 0.31, p = 0.14, 24 of 28 animals matched) |
| fig3b-k-no-correlation | Zenodo | reproduced |
| fig5g-mcherry-no-change | Zenodo | reproduced |
| fig5hi-dreadd-impulsive | Zenodo | partially_reproduced (hM4Di: no single delay significant) |
| fig5jl-dreadd-a-k-auc | Zenodo | partially_reproduced (8 of 9 tests match) |
| fig6bc-ppx-progression | Zenodo | not_reproduced (p = 0.053) |
| fig6de-a77636-no-progression | Zenodo | reproduced |

The three `mua-` claims are my own: they test the paper's unit-level effects on the threshold crossings of each channel, since sorted units are missing. In both groups most channels decrease at 4 to 5 h, so a slow decline over the session dominates that test.

## 2. What was found about the dandiset

- **No sorted units for the main analyses.** Sorted units exist in only 2 of 56 files, with no electrode, cell type or optogenetic label. The other 54 hold unsorted threshold crossings. There are no laser times, injection times or behaviour, so Figures 4, 6F-K and S5 cannot be recomputed.
- **Misplaced timestamps.** In C3-2 day 1 and E5 day 2 the threshold-crossing timestamps are offset by about 30 h from the recording. In C9 day 1 they stop at 42 min of a 414-min recording.
- **Wrong start dates.** Three sessions start in 2025, after the paper was submitted, and H0-2 day 4 starts before day 3.
- **Other metadata problems.** Electrode locations are "unknown" everywhere, genotype is spelled three ways, and subject descriptions contain mis-encoded characters.
- **Animal counts.** The subjects match the paper's counts for Fig. S5 and Fig. 6F. They do not match Fig. 4C (2 control A2a-Cre mice against 4 animals in the paper) or Fig. 6G (7 parkinsonian day-4 sessions against 8).
- **Short saline recordings.** Three of the four saline recordings end before the 240-300 min window the paper uses.
- **Zenodo deposit:**
  - The control mice P1 to P7 ran blocks labelled 0, 6, 12 and 18 s, and most of their sessions have only three free-choice blocks. The task code has four blocks at 0, 3, 6 and 9 s.
  - The rotarod sheet has 40 control mice where the paper reports 31.
  - The histology sheets have 45 parkinsonian animals where the paper reports 44, and 61 rows where RawIntDen does not equal Area × Mean.
  - It does not say which session files were used for each condition.

## 3. Where the protocol was unclear or did not fit

1. **Some sessions have no usable clock check.** Step 2 assumes a trial table or annotations to shift. This dataset has neither, so I used the acute drop in firing after the inferred injection time, compared with shifted times and with the saline sessions. I named the sessions where this failed and left them out.
2. **No rule for testing at a different level.** Nothing in the protocol covers testing a claim at a coarser level than the paper's (multi-unit activity instead of identified units). I added separate `mua-` claims with `data: dandiset` and kept the unit-level claims blocked.
3. **Many tests needed outside data.** Most testable claims needed the Zenodo data. The protocol says to test `elsewhere` claims "as for any other claim", which meant most of the work went into data the registry does not judge. I tested them, but blocked the locomotion claims rather than guess injection times.
4. **Data surprises found after the criteria were written.** The P animals' different delays turned up after the criteria were written. I kept the criteria, recorded deviations, and showed variants.
5. **Outside sources that need matching to each other.** The link-claim rule covers outside data matched to the dandiset, not two outside sources matched to each other (behaviour and histology IDs for Fig. 3). I stated the ID match and its rate in the criterion instead of adding a link claim.
6. **What counts as "the code the paper links to".** The Supplementary material links two code records. I read both (analysis code at commit 5528e22, task code at f7cff8b) and the Arduino code settled the block mapping.
7. **Two equally valid labels for the saline claim.** "A block that depends on a selection" fits it, but whether too few long-enough sessions is `other` or `data_missing` is a judgement call. I used `other`.

## 4. Runtime and failures

- The notebook takes about 4 to 5 min (305 s on the first full run, 246 s on the final one). Most of it is streaming 6.5 GB of spike timestamps as byte ranges, which match h5py reads.
- Nothing failed in the final run.
- During development I fixed: a key collision in the helper, metadata reads that were slow because h5py serialises threads (now run in separate processes, 36 s), and windows that counted as recorded after the spike events had stopped.
- `git status` lists untracked `.bashrc`, `.idea`, `scripts` and similar entries. They are sandbox device mounts, not files I created, and the workflow's commit should skip them.
