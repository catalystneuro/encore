Round 2 is answered. No outcome changed and nothing is proposed for a third round. The final `python tools/entry.py all entries/001260-le-merre-2026` passes in 17 minutes with 0 check errors, and the main numbers are the same as in round 2. Nothing is committed.

**Outcomes.** The verifier agreed with all 40. The one change to an outcome entry is that I removed `assumed: true` from extfig1-epoch-counts: the verifier called it unnecessary, since that claim fails under every detector.

**The new variant: the paper's own sleep-like periods (Zenodo).** The verifier suggested re-running the claims that moved when the detector changed between rounds. A new notebook section before the Summary retrains the ww and nw SOMs from the paper's periods and re-runs those claims:
- **Same outcome as the main detector:** fig2f (partially reproduced), extfig3f (partially reproduced), fig3a (still blocked, G2 readings disagree) and fig4e (still blocked, the two "ILA-specific" readings disagree).
- **Different outcome:**
  - fig2g-pfc-regular-enrichment: G2 a gives partially reproduced and G2 b reproduced, so it would be blocked.
  - extfig5g: not reproduced.
  - fig4g-gao-category1: not reproduced under every reading, r = 0.04 to 0.27, p ≥ 0.16.

I kept the main detector. The paper's periods come out of a visual review whose rejections the Methods don't describe, so they stay a variant, as they already are for extfig1d. The dependence on the detector is now stated in each affected claim's result, in the record notes, the Summary and the README.

**Corrections from the report:**
- **Session-skip rule:** it is now labelled as this attempt's own rule, not the paper's, in notebook cell 10, the `pfcki.py` docstrings and the 10 deviations in the record. Each quotes the Methods sentence in full.
- **fig2i notes:** fig2g-pfc-regular-enrichment is now given as reproduced, not blocked.
- **Settings finding:** p corrected from 9e-05 to 0.0021.
- **Cell 40:** the files with a `Block` column are the 6 Aversion and 14 Context files; no Opto or Passive file has one.
- **fig4e notes:** they now say the variants lean towards not reproduced while the criterion blocks the claim.

**Added:**
- The round-2 entry under `verifications`, with all 40 claims, each giving the verifier's reason and my response.
- A question for a reader in `questions/001260.yaml` on the G2 category numbering. The paper's own SOM matches reading (b) for 27.7% of units and reading (a) for 19.9%, and the 8 claims blocked under G2 depend on the answer. The claims file is unchanged.

**Not done:** fig4e stays blocked even though the variants lean towards not reproduced, because the criterion blocks it on the main analysis and the verifier accepted that. The open GaoROI ID question for fig4g-pl-orbl-extremes stays with a reader.
