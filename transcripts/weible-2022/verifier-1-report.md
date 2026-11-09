**Verifier report, round 1: Weible & Wehr 2022 on DANDI:002035 at 0.261022.1829**

I counted 33 claims from the claims file. No attempt record was among my materials, so the notebook's statuses come from its cell 0, and I checked them against the archive myself. I queried the manifest, README, `samples.tsv`/`.json`, `scans.json`, `participants.tsv` and all 62 `sub-*_scans.tsv` tables. I downloaded no images.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| a1-first-in-pathway | blocked (metadata_insufficient) | Only 864 of 12,394 images have a region (cell 7). The 9 ACtx-labelled images are all DAPI, with no Abeta42, so nothing places label in A1 or in any other region by age. |
| fig1a-a1-onset-p21 | blocked (metadata_insufficient) | No Abeta42 image is labelled A1. The laminar bins and the pia/white-matter geometry are not recorded. |
| fig1c-a1-cells-age | blocked (metadata_insufficient) | Same as fig1a. |
| fig1d-a1-cells-layer-5a | blocked (metadata_insufficient) | Same as fig1a. |
| fig1e-l5a-peak | blocked (metadata_insufficient) | Same as fig1a. |
| fig1f-l5a-dapi-stable | blocked (metadata_insufficient) | Same as fig1a. |
| fig1g-dapi-layers | blocked (metadata_insufficient) | Same as fig1a. |
| fig2b-a1-plaques-age | blocked (metadata_insufficient) | Same as fig1a. |
| fig2c-a1-plaques-layer | blocked (metadata_insufficient) | Same as fig1a. |
| fig2d-a1-plaques-sex | blocked (metadata_insufficient) | Same as fig1a. |
| wt-no-label | blocked (data_missing) | The README says wild-type controls "were not imaged", and `participants.tsv` lists 62 mice, all 5XFAD (cell 3). I confirmed both on the archive. |
| fig3a-subiculum-onset | blocked (metadata_insufficient) | Only 1 of the 5 p14 mice has subiculum-labelled images, so "every p14 mouse" can't be tested. Part of the claim could be tested: 5 p60 mice (0215, 0216, 0217, 0245, 0251) have 200X Abeta42 subiculum images, which bear on "plaques present at p60". Images from 9 younger mice could only disprove "no plaques before p60". The notebook did not look at either. |
| fig3bc-subiculum-cells-plaques-age | blocked (metadata_insufficient) | Subiculum images exist for 17 mice (1–5 per age). There is no DAPI count or area for the region. |
| fig3d-subiculum-dapi-stable | blocked (metadata_insufficient) | Same as fig3bc. |
| subiculum-no-sex | blocked (metadata_insufficient) | Same as fig3bc. |
| mgb-cells-rare | blocked (metadata_insufficient) | The "5 of 61 mice" count needs every mouse's MGB, and only 3 mice are labelled. The "at most 1–2 cells per mouse" part could be disproved by looking at 71 MGB 200X Abeta42 images (mice 0173, 0218, 0136). The notebook did not do this. |
| mgb-dapi-subregions | blocked (metadata_insufficient) | The MGd/MGv/MGm boundaries are not recorded. |
| fig4b-mgb-plaques-age | blocked (metadata_insufficient) | MGB is labelled only at p90, p120 and p150, one mouse each, with no area. |
| fig4c-mgb-plaques-subregion | blocked (metadata_insufficient) | Same as fig4b. |
| mgb-sex-trend | blocked (metadata_insufficient) | Same as fig4b. |
| ic-cells-low | blocked (metadata_insufficient) | IC is labelled in 3 mice (p30, p60, p150). The eIC/dIC/cIC subdivisions are not recorded. |
| ic-cells-subregion | blocked (metadata_insufficient) | Same as ic-cells-low. |
| fig5b-ic-plaques-age | blocked (metadata_insufficient) | Same as ic-cells-low. |
| fig5c-ic-plaques-subregion | blocked (metadata_insufficient) | Same as ic-cells-low. |
| ic-no-sex | blocked (metadata_insufficient) | Same as ic-cells-low. |
| fig6b-soc-cells | blocked (metadata_insufficient) | SOC is labelled in 5 mice, with no SOC DAPI denominator and no subdivision. |
| soc-plaques-rare | blocked (metadata_insufficient) | Same as fig6b. Finding more than 3 plaques, or plaques in more than 2 mice, in the labelled SOC images would disprove the claim, but this was not checked. |
| fig6cd-nll-cn-none | blocked (metadata_insufficient) | No image is labelled nLL. Two mice could disprove the CN part: 0136 (p150, 7 CN-labelled 200X Abeta42 images) and 0215 (p60, 23 200X Abeta42 images labelled "IC;VCN"). The notebook did not look at either. |
| fig7b-prnc-cells | blocked (metadata_insufficient) | Overall the claim can't be tested: there is no 800 µm circle centre, and no DAPI count of a known area. One sub-condition can be: 3 p14 mice (BrTNR, LTN, NN) have 25 PRNc 200X Abeta42 images, enough to check for a >40 µm and a smaller Abeta42+ cell at p14 (pixel size is 0.3225 µm). The p21 "consistently" condition can't be tested, since only 3 of 8 p21 mice are labelled. |
| fig7c-prnc-plaques | blocked (metadata_insufficient) | PRNc is labelled at p14–p30 and p150 only, with no p90 or p120 mouse. |
| prnc-no-sex | blocked (metadata_insufficient) | Same as fig7c. |
| cells-before-plaques | blocked (metadata_insufficient) | Every claim it depends on is blocked. |
| l5-pyramidal-fraction | blocked (metadata_insufficient) | It depends on fig1e, which is blocked. |

None of the claims gives a chance level, so there is nothing to compare.

### B. Problems

1. **[affects a conclusion] Cell 0 / cell 8: the reason given for blocking is asserted, not shown.** The notebook says the images "cannot be assigned to a region… from anything in the dandiset". But the README says each image sequence "begins with low-magnification coronal overviews used to locate the high-magnification fields". I sorted the scans tables by run number and they bear this out: within a mouse, 12.5X overviews alternate with runs of 100X/200X fields, and each mouse has 4–78 overviews. The paper itself identified regions by aligning sections to CCFv3 on DAPI landmarks. The notebook never tests whether fields can be tied to their preceding overview by run order or time, then placed in it by DAPI template matching (a 200X field is about 87×65 px at overview scale). Whether that would work is unknown. Until it is checked, the block is not fully supported, though the quantitative claims probably stay blocked because region areas and coverage are also missing. I keep "blocked".
2. **[affects a conclusion] Cell 7: claim parts that the region-labelled images could test were never looked at.** For six claims, an existence or upper-bound condition could be checked by eye on the 561 region-labelled 200X Abeta42 images:
   - fig7b: both cell types at p14;
   - fig3a: plaques at p60;
   - fig6cd: label in CN/VCN;
   - mgb-cells-rare: more than 2 cells in one mouse;
   - soc-plaques-rare: more than 3 plaques;
   - fig3a: plaques before p60.

   None of these would change a whole claim to reproduced, but most could disprove one, and fig6cd would be not_reproduced if CN label were found. Saying they were "considered and not done" would be acceptable; saying nothing is not.
3. **[does not affect a conclusion] Cell 7: the coverage table counts mice with *any* image of a region, including DAPI-only ones.** For example, A1 shows "2 mice", but neither has an Abeta42 image. A count of Abeta42 images per region and age would describe what can be tested more accurately.
4. **[does not affect a conclusion] Cell 7: the check for position metadata uses 20 of 12,394 images and sidecars.** Since `scans.json` and `samples.json` define the full sidecar schema ("individual sections are not tracked"), the conclusion holds. Citing `samples.json` would have been the stronger evidence.
5. **[does not affect a conclusion] Cells 5–6 / `nucleus_diameter_um`: this is a scale check only and is not used for any claim.** The median diameters differ by about 20% between the 100X and 200X classes (4.2 vs 5.1 µm), and the field-count ratio is 3.6 against an expected 4. That is consistent with the stated scales, and the notebook says correctly that it does not prove them. The 7,125 images assigned 200X by rule were left unchecked, as the notebook admits.
6. **[does not affect a conclusion] Cell 3: the mouse counts are reported correctly.** The dandiset has 62 mice (30 F, 32 M), against the paper's 61, with differences at p45 (3F/5M) and p120 (9 mice). The notebook does not say which mouse is the extra one, but nothing is tested, so this doesn't matter.

I found no misreading of the paper in the claims file that would affect any of these outcomes. Because every claim is blocked, I did not audit the claims' criteria line by line.

### C. What I could not check, and which outputs would have let me

- **Whether fields can be placed in their overviews.** A per-mouse listing of run order and acq_time grouped into overview→field blocks, plus one worked attempt at registering a 200X DAPI field into its overview, would settle problem 1.
- **What the region-labelled Abeta42 images show.** A per-image table for the 561 region-labelled 200X Abeta42 images, giving mouse, age, region and an eye-scored presence of cells and plaques with cell diameters, would settle the testable parts in problem 2 (fig7b p14, fig3a p60, fig6cd CN/VCN, mgb max, SOC count).
- **Possible region cues outside the labelled column.** I did not view the 21 follow-up subfolders that have no region label, such as "0329 extra 1/2" and "173 follow-up". A listing of their images by magnification and stain would show whether they could hold region-identifiable fields.
