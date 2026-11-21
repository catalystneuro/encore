**A. Outcomes**

The claims file has 30 claims. The notebook tests 3 and treats 27 as blocked.

| Claim | My outcome | Reason |
|---|---|---|
| link-authors-deposit | reproduced | Cell 16: all 16 of the 16 areas in `area2anno.json` have at least one dataset `anno_name` (162 of the 294 dataset annotations appear in the map). All 106 authors' sessions match by mouse and date (21 mice). The 5 SC038 days with two sessions each have exactly two dataset files. Both conditions of the criterion hold. |
| data-scale | partially_reproduced | Neuron count holds (cell 18): 154,948 units with `unit_quality` good, 88,647 of them above 2 Hz. Of those that carry a CCF annotation (`classification` good), there are 69,453. The structure count does not hold as computed: "17 areas" counts nested structures twice (superior colliculus, MRN and SNr inside midbrain; VM, VAL and MD inside thalamus). Without the nesting, the listed groups give about 10, not more than 12. |
| fig6e-marker-clustering | partially_reproduced (strictly, not_reproduced) | CH is 5.92 on the main set, 7.63 on the authors' 106, and at most 9.22 across seeds and variants (cells 20, 22, 23). Every value is outside 12.57 ± 1.26. Null mean 1.02–1.07 (paper 1.05 ± 0.54). Permutation p = 0/1000, i.e. below 0.001. Nose-type mice (3) and jaw-type mice (11) both occur. The criterion defines no partial outcome, so read literally it fails. |
| fig2b-medulla-vs-midbrain, fig2b-area-ordering, edfig3-epochs, fig2e-method-improvement, edfig1-reliable-unpredicted | blocked (data_missing for most sessions; too_large for the rest) | They need the per-session autoencoder embedding, and fig2e also the end-to-end networks. Neither is in the pinned version. Raw video exists only in 71 files of version 0.231012.2129 (see B3). |
| fig2-ordering-across-methods | blocked (same) | The marker-method ranking alone could be tested (see B4). |
| fig3-thalamus-nonuniform, fig3e-nearest-neighbor, fig3f-thalamic-nuclei, thalamus-ev-not-rate, supfig2-noise-injection | blocked (same) | The neuron selection depends on embedding explained variance above 0.01. |
| fig4b-medulla-leads, edfig6-offset-ev-correlation, fig5a-somatosensory-vs-alm, fig5b-po-vs-vm, fig5c-pretectal-vs-scm, fig5-significant-offsets, fig4e-alm-depth | blocked (same) | They need embedding explained variance at each time shift. |
| fig6a-choice-from-video, fig6d-mouse-clustering, edfig7-performance-correlation | blocked (same) | They need the embedding decoder. |
| fig6-marker-vs-embedding-decoding | blocked (same) | The marker half (0.88 response-epoch AUC) is testable from the markers but was not run (see B4). |
| fig7b-jaw-differs, fig7c-modulation-nonuniform, fig7d-alm-midbrain-vs-medulla, edfig10-subtraction-consistent, supp-session-independent-autoencoder | blocked (same) | They need the embedding decoder's single-trial predictions or the embedding itself. |

**B. Problems**

1. **[affects a conclusion]** Cell 18, data-scale. `areas_with_units` = 17 is the 16 overlapping groups of `area2anno.json` plus ALM. Six of the 16 are nested inside larger ones, so it is not a count of distinct structures at area level. About 132 dataset annotations fall outside the map (likely other isocortex, pallidum and so on) and were never grouped. The "more than a dozen" half of the claim is therefore not shown. The 17 cannot support "reproduced".
2. **[does not affect a conclusion]** Cell 12/18, data-scale.
   - The 200,922 units with an empty `anno_name` are exactly the `classification` "unlabelled" units. So the 154,948 `unit_quality` good units include 92,769 that have no CCF location.
   - The count tied to locations is `classification` good: 69,453, or 46,658 above 2 Hz. In the authors' 106 sessions those figures are 42,259 and 28,606, both below 50,000.
   - The criterion (all sessions, either filter) is still met, but the notebook does not point out that many of the units it counts have no CCF location.
3. **[affects a conclusion: block reason]** Cells 0, 13, 14. The notebook says the raw video "is only in the later version" and blocks everything as too_large. I checked the archive API:
   - Only 71 of the 174 files in 0.231012.2129 carry `+image`. They come from 16 of 28 subjects (66 from 2019). Subjects sub-479121 through sub-484677 have no video in any version, except a single file for sub-484676 (SC066).
   - Matching subjects to mice by session counts, only about 35–40 of the authors' 106 sessions have video in the archive. For the other ~2/3, the right reason is data_missing, not too_large.
   - The notebook prints the 71 but never relates it to the 106.
4. **[affects a conclusion]** Cell 14 / blocked list. Parts of some blocked claims need only the markers, which are in the dataset:
   - the marker arm of fig2-ordering-across-methods (ridge regression from five-frame jaw, nose and tongue features);
   - the marker AUC of fig6-marker-vs-embedding-decoding (0.88, response epoch).
   
   Neither was run, and the notebook does not say these parts could be tested. The claims file also names the authors' go-cue-aligned embeddings (Google Drive) as the alternative input. The notebook rejects them as "not pinned" without trying them; that is a judgment call and should be stated as one.
5. **[could affect a conclusion]** `mapvideo.decode_auc_fast` and `decode_auc`. The session AUC pools decision values from 20 differently fitted fold models into one ROC per bin. The paper leaves this open; the Methods describe averaging test-fold AUCs for the single-neuron analyses. Pooling versus averaging over folds can shift session AUCs around the 0.65 inclusion threshold, and so change the CH score. Only one reading was run, and it is not stated as an assumption.
6. **[does not affect a conclusion]** Cell 20, fig6e session set.
   - The main set is the 167 clock-checked sessions, the author's own choice. The paper's analysis uses the 106 sessions identified by the link claim, so that set should be primary.
   - It is run as a variant. Its CH (7.6–9.2) is still out of tolerance, so the outcome does not change.
7. **[does not affect a conclusion]** `mapvideo` module docstring. It says decoding uses "every 10th frame (34 ms)", but `STRIDE = 20` (68 ms) is what runs. Subsampling time bins is an undeclared author choice, although its effect on a mean over bins is small.
8. **[does not affect a conclusion]** `clean_marker`.
   - Velocity is computed across the whole concatenated session, including jumps between trial videos.
   - A single bad frame also flags the next, genuine frame (on synthetic data, 2 frames were flagged for 1 spike).
   - Both effects are minor (about 9 frames per 10,000).
9. **[does not affect a conclusion]** Synthetic checks:
   - `decode_auc_fast` agrees with sklearn `LogisticRegressionCV` to within 0.015 AUC across separations from 0 to 5.
   - `marker_epoch` aligns bins and the centre frame (reading (b), columns 4:6) correctly.
   - There is no train/test leakage: the penalty is chosen by inner cross-validation inside each outer training set.
10. **[does not affect a conclusion]** Cell 0 calls link-authors-deposit "added by this attempt", but it is in the claims file. The notebook also implies the later version's size growth (53.6 GB to 65.7 TB) is video. The asset metadata lists ElectricalSeries (raw ephys) in those files, and only 28.9 TB is in video files.

The clock check in cells 8–11 holds up: 5 sessions are on a 2× time base, 1 has trial videos likely attached to the wrong trials, and 1 is truncated, and none of them is in the authors' 106. I found no misreading of the paper in the claims file for the tested claims. The Fig. 6e legend's 0.6 display threshold and the Methods' 0.65 were both run.

**C. What I could not check**

- **Number of structures (data-scale).** I could not get a non-overlapping count. The notebook would need units per top-level Allen division (or per the paper's area list including "other isocortex"), counting each unit once, and the annotations that fall outside `area2anno.json`.
- **Which of the 106 sessions have video in 0.231012.2129.** My figure of about 35–40 comes from matching session counts. A cross-tab of the authors' 106 keys against `+image` paths would settle it.
- **Sensitivity of fig6e to the AUC definition.** It needs a run with fold-averaged AUC alongside the pooled AUC, with the resulting CH score and the sessions kept.
- **Marker-only checks.** The marker response-epoch choice AUC (fig6-marker-vs-embedding-decoding) and the marker-ridge area ranking (fig2-ordering-across-methods) were not computed, so those parts could not be judged.
- **The Zenodo deposit's member list.** It is not printed, so I could not confirm that no per-frame embeddings or per-neuron explained-variance files exist there. Printing `ZipFile.namelist()` with sizes would settle it.
