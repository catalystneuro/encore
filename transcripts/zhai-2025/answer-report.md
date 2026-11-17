There was one question to answer, and I changed the claims file for it.

- **fig5f-ach-off-elevated: changed.** The paper counts regions, not mice. The Figure 5F legend gives "n = 13 regions of interest (ROIs) from three mice". The Methods say the stated n is "the number of ROIs (in ACh sensor imaging)". The criterion now runs the test on one value per region (ROI) instead of one region per mouse.
  - I also changed a second claim that uses the same measure, `fig5f-ach-off-like-6ohda`. Its criterion now says one value per region too, so the two match. My answer to the question mentions this.

`python tools/claims_check.py` reports 0 problems, and the questions file loads as valid YAML. I only edited `claims/zhai-2025.yaml` and `questions/zhai-2025.yaml`, and nothing is committed.

There is one related mismatch I left alone because no question raised it. The `link-grab-rois` claim still matches regions using "each mouse's vector" of areas.
