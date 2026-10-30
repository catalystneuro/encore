I've finished steps 1 to 6: the entry `entries/000467-hart-2023/` (three notebooks plus the helper `al_imaging.py`), the record `attempts/000467-hart-2023-01.yaml` and the handover in `executed/000467-hart-2023/handover/`. `entry.py all` passed, `check` reports 0 errors after the final edits, and nothing is committed. The dandiset is pinned at 0.261004.1655, the only published version (the paper cites none).

**1. Outcomes (32 claims)**

| Claim | Outcome |
|---|---|
| fig3f-general-odorants-unique | not reproduced |
| fig3fg-hexanone-broad | partially reproduced |
| figs4a-bilateral-symmetry | partially reproduced |
| fig4b-vehicle-no-response | not reproduced |
| fig4-no-decreases | not reproduced |
| fig4-large-lasting-responses | partially reproduced (assumed) |
| figs5a-sparse-median-6 | reproduced (assumed) |
| figs5a-concentration-more-glomeruli | reproduced (assumed) |
| figs5b-shared-glomerulus | partially reproduced (assumed) |
| figs5c-mho-rarely-overlaps | reproduced (assumed) |
| fig6-shared-panic-pathway (imaging half) | partially reproduced (assumed) |
| fig5ab-focal-glomeruli | not reproduced |
| fig5d-stereotyped-positions | not reproduced |
| fig5c-s6-tuning | partially reproduced (assumed) |
| fig5c-6g-slow | partially reproduced (assumed) |
| figs7a-6g-extended | not reproduced (assumed) |
| figs7c-temporal-lme | blocked (other): no PGa found, so the models cannot be fitted |
| 8 behaviour, transgenesis and pupae-image claims | blocked (data_missing) |
| 4 Brain Image Library claims (fig2cd, figs1, fig2e, fig2f) | blocked (other): stacks not located in this run |
| figs2ab, ablation volume (manual segmentation); figs3 (17 Gbases of reads to align) | blocked (not_runnable) |

**2. Dataset, assumptions, questions**
- **Contents:** all three imaging experiments are there, matching the paper's subject and concentration groups, plus the five 144 s recordings. There are 14,685 files, one plane of one trial each, 1.26 TB of uncompressed float64 holding 13-bit values. No file or trial is deposited twice.
- **Timing metadata disagree:** the planes' start times imply 1.105 s per volume. The files' imaging rate says 1.205 s, and the paper says 1.2 s.
- **Missing structure:** stimulus timing is only in free text, and the bilateral files don't say which lobe is left.
- **Odorants:** only the 5 analysed general odorants are deposited, though the paper presented 7 to 9.
- **Main assumption:** the paper drew its ROIs by eye, and the eight ROI readings in the claims file disagree. I adopted the "bix" reading: glomerulus-sized ROIs (b), each ROI's mean value (i) and the Methods' trial-mean rule (x). The readings that keep every thresholded region give dozens to hundreds of ROIs per ant.
- **Consequence for the focal glomeruli:** under bix, PGb is found in 7 of 13 ants, 6G in 4 and PGa in none. So the PGa parts of the claims that depend on them are untested.
- **Questions for the paper's authors** (filed as `methods_unavailable` findings): the ROI drawing rule, the ROI value, the counting rule, the motion-artifact exclusion rule, how the centre plane was chosen and what ROI was measured on it, and the distance that makes two glomeruli adjacent.
- **Questions to a reader:** none.

**3. Where the protocol was unclear**
1. Archives.md says to read with remfile and h5py, which was too slow for 1.26 TB. I used HTTP range reads at the byte offset h5py reports, checked against h5py reads on a sample, and checked every read for values in the detector's integer range.
2. The claims file says M2 claims are judged "under each reading", while step 1.6 says to adopt the best-supported reading when readings disagree. I followed step 1.6, ran every reading and marked those outcomes `assumed`.
3. There is no rule for claims that depend on a claim that was tested but not reproduced and that only partly identifies the glomeruli. I tested what could be identified and blocked figs7c.
4. For `elsewhere` data that cannot be located (the BIL retrieve API answered "no entry found"), no `blocked_by` category fits. I used `other`.
5. Conclusions can only be written after the run. I edited the Result markdown in both the entry and the executed copies without re-running.
6. The 30-minute notebook limit meant splitting the work into three notebooks. One of them recomputes the higher-concentration maps.

**4. Runtime and failures**
- The run took about 1 h 50 min, ending at 13:01 UTC. The notebooks ran in 7.3, 19.6 and 20.8 min (`entry.py all` took 47.7 min).
- **Failed:** a variant that identified the glomeruli under a second reading was tried during development and dropped. It found PGa, but the PGa traces never crossed the onset threshold, and running it in the notebook would have pushed it to about 27 of the 30 minutes allowed. It is not in the notebook.
- **Failed:** the figs7c model fits fail with only one glomerulus level, as the notebook shows.
