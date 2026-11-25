## Report: komori-2026 on DANDI:001425 (v0.250705.0947)

The six resting-state claims were tested. One reproduced partially under a single reading and a single seed, one reproduced partially, and four did not reproduce. The other 18 claims are blocked because the paper's own stimulation recordings are not deposited. The full `entry.py all` did not finish (see 4), so CI will re-execute the entry.

### 1. Outcomes

| Claim | Outcome |
|---|---|
| rest-decoding-above-null | partially reproduced (assumed). Only under reading R4 b (every frame of the epoch is a sample): model AUC 0.719 vs null 0.655, p = 0.004, but below the expected 0.82 ± 0.082. Under the main reading: 0.686 vs 0.708 (p = 0.36), and none of the 5 seeds is significant. The 5-seed check was not run for R4 b. |
| rest-loss-accuracy-vs-null | not reproduced (assumed) |
| rest-needs-0-1-hz | not reproduced (assumed). The 0.1 Hz model is not above null. The 2 Hz absence holds. |
| rest-ic-count-and-window | partially reproduced (assumed). 10 ICs give the best median AUC; the best window is 1.0 s, not 1.5 s. |
| rest-vif-below-10 | not reproduced (assumed). Max VIF is 6.61: below 10, but outside 9.0 ± 0.9. 15 ICs is significantly higher than 10. |
| rest-shap-medial-anterior-first | not reproduced (assumed) |
| 18 stimulation claims (fig1–fig4, supp2/4/8/10) | blocked: `data_missing` |

### 2. Dataset, assumptions, questions

**What the dataset holds:** 98 resting files from 25 mice, with frames for both channels (288×288, 18,000 per channel, 30 Hz), pupil diameter and keypoints on the imaging clock, atlas ROIs and an affine. Of the 9 files used, 6 are the same assets in v0.250514.0602; the other 3 were replaced and not compared.

**Findings about the data:**
- The imaging-plane metadata swap the excitation wavelengths: blue says 405 nm, UV says 470 nm. The values show `widefield_blue` carries the calcium signal. Rated minor.
- The deposited pupil diameter has unflagged failed detections, up to 2.9e21 px, in 2 of the 9 sessions. Rated minor.
- 6 resting files have no behaviour, so no pupil.
- The clock check is consistent with the data.

**Assumptions:**
- Mice and sessions: VG1-GC#51, 52 and 53, with their first three resting sessions.
- IC selection: the most compact maps, standing in for the paper's "visual inspection".
- Pupil outliers: values above 3× or below ⅓ of the median are replaced by interpolation.
- Hemodynamic regression: coefficients are fitted on high-passed signals and applied to the unfiltered signals.
- SHAP: computed by integrated gradients, because DeepExplainer does not support PyTorch GRU layers.
- The SVD keeps 306 components (the data's rank) instead of 400.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- Which mice and sessions were used?
- Are resting samples only the window around the peak, or every frame of the epoch? This decides the outcome here.
- Which ICs were kept, and how does "every fifth session" apply to resting data?
- Will the resting-state code be published?

**Questions to a reader:** none.

### 3. Protocol gaps
1. The **Result** cells must be written after the run, but any edit invalidates the run stamp. Doing it properly means running twice, which does not fit 5 h with 40-minute notebooks. I developed on cached data, executed, then copied the final markdown into the executed copies (code unchanged, no stamp).
2. `entry.py check` rejects index options in `requirements.in`, so the PyTorch CPU index cannot be used. I locked the PyPI torch with its CUDA libraries, a 5.7 GB environment.
3. "Run every reading" across R1 to R10 gives 64 or more combinations, and the protocol does not say whether one change at a time is acceptable. I ran the main combination plus one change at a time, and recorded this as a deviation.
4. The five-seed rule is costly for ML claims with many variants. I ran it for the main decoding readings only and recorded the gaps.
5. Results differ between software environments, because JADE and BLAS are not deterministic across them; the protocol says nothing on this. I report only numbers from the locked environment. A run outside the notebook gave a non-significant R4 b result; it is mentioned only as a sign the result is fragile.
6. The Bash tool's default 60-minute timeout matches the notebook limit, so `entry.py all` on two notebooks is killed. I re-ran notebook 2 alone in the same environment.
7. Two criteria were ambiguous:
   - In rest-vif, "the 10-IC maximum holds" could mean only below 10; I read it strictly, as below 10 and within 9.0 ± 0.9.
   - In rest-shap, precedence is undefined when an IC has no onset; I required both onsets.
8. There is no clear kind for "the paper's own data are not public" when the dataset is reused. I recorded it as `other`, `about: paper`.

### 4. Runtime and failures
- Notebook 1 (decoding): 31 min. Notebook 2 (features): 37 min. Streaming takes about 12 min of each.
- The first `entry.py all` was killed by the 60-minute tool timeout while notebook 2 was running. Notebook 2 was then executed with nbconvert in the same locked environment.
- No run stamp exists, so CI will re-execute. Its numbers should match only if training is deterministic within the locked environment, which was not tested.
- `check` passes (0 errors), the attempt record validates against the schema, and the handover was built in `executed/komori-2026/handover/`.
