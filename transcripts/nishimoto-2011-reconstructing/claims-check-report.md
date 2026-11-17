I checked the claims file against the paper and its supplement and made eight corrections. The file is ready for an attempt (`ready: true`), with three problems I could not settle.

**Checker result:** `claims/nishimoto-2011-reconstructing.yaml: 10 claims, 10 quotes, 5 statistical values, 0 problems`, both before and after my edits.

**Changes, by claim:**
- **fig2de-prediction-accuracy:** I removed the reading that averages only the 2,000 selected voxels. The supplement's Voxel Selection section applies that selection only to reconstruction and identification. Figure 2 uses every voxel in the stimulated parts of V1 to V3B. How subjects are combined is still listed as open.
- **fig2e-directional-gain-small:** The paper says the result "suggests" BOLD signals carry mostly nondirectional motion information; it does not state it. The statement now says "suggests".
- **figs1a-motion-better-every-area:** The criterion assumed the directional model for the "best in V1" test, but the Figure S1A legend doesn't say which model. That is now listed as open, with two readings: the directional model alone, or each of the three models.
- **fig2fgh-retinotopic-receptive-fields:** The statement applied the far-periphery exception to both maps. The Figure 2H and 2I legends give it for the eccentricity map only, because the multifocal mapping stimulus was coarse there. Statement corrected.
- **fig3ab-identification-s1:** I added as open whether the observed test signal is the average of the ten repeats or each repeat taken separately. The paper doesn't say, and the choice can change the count.
- **fig4d-reconstruction-accuracy:**
  - Reading (b), "the larger of MAP and AHP", always equals reading (a) once the criterion requires AHP to beat MAP. I replaced it with the AHP mean over the three subjects.
  - I added as open how many random prior clips make up the chance distribution, since that number moves the rank-sum p-value.
  - The AHP rescaling now matches the Figure S2D legend: mean and s.d. of the average of the top 100 clips.
- **discussion-color-no-gain:** The paper's sentence covers identification as well as prediction. Identification with the color model is now reported too, but it doesn't decide the outcome because the paper gives no test for it. I added `fig3ab-identification-s1` to `depends_on`.
- **Header, motion-energy features:** I noted that the paper's total of 6,555 filters, together with the grid spacing of 3.5 s.d., pins down the spatial envelope size the paper leaves open.

**Still open (recorded in the checks entry):**
- The retinotopy claim is judged without the multifocal mapping data, on a test set in this file, not in the paper. The paper only compares the maps by eye, so the outcome rests on that test.
- Several thresholds were set in this file because the paper gives no number:
  - the bound for "small" (a tenth of the motion models' gain over the static model);
  - the partial-reproduction thresholds in figs1a and fig2j.
- fig3c, fig4 and fig4d need the 1,000,000-clip identification set and the prior of about 18,000,000 s of movie clips. The paper neither deposits these nor says where they are.

The file is modified and not committed.
