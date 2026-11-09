I wrote `claims/001425/10.1101-2025.02.03.631599.yaml`. The quote checker passes it with 22 claims, 22 quotes and 0 problems. Nothing is committed.

**Text read:** the bioRxiv preprint, version 1, taken from its JATS XML. It has the main text, the Methods, the legends of Figures 1 to 6 and the legends of Supplementary Figures S1 to S4. There is no PDF.

**Code read:** `BraiDyn-BC/bdbc-data-pipeline` at commit ab50b17, plus the submodule commits it pins:
- bdbc-nwb-packager 426f07c
- bdbc-session-explorer 58089f2
- bdbc-nwb-explorer 309c5fb
- bdbc-batch-scripts 763cf80
- ks-pupilfitting dc14b36

The code builds the NWB files, registers the atlas, fits the pupil and runs sanity-check plots. The only detail it settles is the likelihood cut-off of 0.2 for keypoints. None of the analyses behind Figures 3 to 6 or Figure S2b are in it, so every method detail comes from the Methods and legends or is named as open.

**Counts:**
- **Claims:** 22, all quoted.
- **Statistics:** none. The paper reports no tests.
- **Expected values:** 9 claims. Session and subject counts have a tolerance of 0, and the reason is given. The correlations and break statistics use the paper's stated s.d. as the tolerance.
- **Criteria:** all 22 claims have one.

**Details the paper leaves open, and the readings named for each:**
- **Response rate:** valid pulls counted from the trial outcome labels, or from the lever trace crossing 1 mm within 1 s of the tone.
- **"Constant" success rate:** session 15 within 10% of session 1, or no Spearman trend across sessions.
- **Clustering:**
  - Feature: the 15 raw T_pull_final values, or the differences between consecutive sessions.
  - Missing sessions: linear interpolation, carrying the previous value forward, or the next session's starting T_pull plus 100 ms.
- **Cluster A and B comparisons:**
  - "Early" sessions: sessions 1–5, or session 5 alone.
  - "Late" sessions: sessions 11–15, or session 15 alone.
  - "High" T_pull_final: 400 ms, or above the median.
  - "Similar": Mann-Whitney p ≥ 0.05, or group medians within 10%.
- **Training breaks:** mean pooled over all breaks or over mice; how sessions that were not deposited are treated.
- **No signal degradation:** raw blue fluorescence or dF/F s.d. against session number.
- **Sensory maps:**
  - Data: ROI series or pixel maps from the image files.
  - Baseline: none, or the 2 s before the stimulus.
  - The "parietal multimodal area": VISa, VISrl or PTLp.
- **Figure S2b (aberrant transients):**
  - Peak detection: no threshold, or a 0.01 minimum prominence.
  - Which ROIs count as frontal, retrosplenial and visual.
  - K-means features raw or z-scored.
- **Keypoint–lever correlations:**
  - Sampling: 100 Hz or 30 Hz.
  - Likelihood filter applied or not.
  - Trial window: from the trial table, or tone to tone + 1 s + T_pull.
  - Mean taken over sessions or over mice.
  - Sign as computed, or absolute value.
- **Figure 6 example session:** the paper does not say which session it is. The readings are the grand average over sessions, or the majority of sessions. Each Figure 6 claim also has readings for which pulls, which hemisphere and which windows are used.

**Where the criterion uses my own rule:** these are labelled in the file as standard choices or as my reading of the paper's contrast.
- The movement-onset threshold (2 s.d., also shown at 3 s.d.).
- The pupil-versus-lever correlation contrast in the Figure 6 sensory-area claim.

**Missing from the paper:**
- The contents of Tables 1 to 4 are absent; only their legends are in the text. That means no per-animal session counts and no keypoint names.
- Figure values (the Figure 5a–c error percentiles, the Figure 3 curves) could not be read without a PDF.
- The manual annotations used to validate the atlas landmarks and the DeepLabCut keypoints are not described as deposited. Those two claims will likely be blocked.
- The paper does not say plainly whether the sensory-mapping sessions are in the dataset. The three sensory-map claims are blocked if they are not.
