The claims file for kussovska-2025 is ready for an attempt. I made six corrections, and three problems remain open.

**Checker:** `claims/kussovska-2025.yaml: 45 claims, 45 quotes, 74 statistical values, 1 problems`. The one problem is the value 9.7e-12 in `fig3h-early-vs-late-maintenance`. The paper prints it as "9.70 × 10−12", and the checker doesn't match the trailing zero. The value itself is correct. The file passes the schema check, and every quote matches the paper word for word.

**Review:** I checked every claim against the paper. I also cloned the paper's code (github.com/dariakussovska/heterogeneitywm at commit 5144fe8) and spot-checked the code the criteria cite: burst parameters, group splits, the GLM window, the Royer burst index, the dPCA split and its tests, and the CV2 script. The citations I checked are accurate. Statements, statistics and expected values match the paper. Selection thresholds are left out of the statistics, as they should be. Every main finding has a claim, and none comes from another source.

**Changes, by claim:**
- **`fig4c-encoding-bursts-vs-poisson`:**
  - The criterion used a 140 ms minimum gap between bursts without noting a conflict. The Methods and the code say 140 ms, which stays the main reading. The Results say 70 ms, now run as a variant.
  - In the code, the "all neurons" group only keeps participants with at least 10 neurons; the criterion now says so.
- **`fig4f-all-cells-epochs`:** The Results say burst rates rose across successive maintenance windows but report no test for it. Those comparisons are now reported without deciding the claim.
- **`fig6cd-celltype-epochs`:** The paper says pyramidal burst rates were stable "across task epochs and load", but the claim only tested load 1. The statement and criterion now cover loads 2 and 3. Holding at load 1 alone counts as partly reproduced.
- **`fig6gh-in-concept-cv2`:** The paper's sentence on stable pyramidal CV2 can mean two different comparisons. Both are now named: encoding against maintenance within each trial type (what the code runs), and preferred against nonpreferred trials within each epoch.
- **`ext5gh-py-decay-preferred`:** The paper never defines the "decay time constants" in this test. Using the autocorrelogram fit's decay constant is now marked as an assumption the result rests on.

**Still open:**
- The checker flag on 9.7e-12 above; the value is correct.
- `ext2-bursts-loads23` cites Extended Data Fig. 2b–m for bursting results, as the paper does. But the paper also uses Extended Data Fig. 2 for dPCA details, so the citation may be a mislabel in the paper. It can't be confirmed because the Extended Data aren't in the text.
- The Extended Data figures and their legends aren't in the text. The nine claims that rely on them depend only on the main-text sentences that cite them, and they name their measures as open.

I recorded all of this under `checks` in the file. Nothing was committed or pushed.
