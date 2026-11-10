I've written `claims/zhong-2026.yaml`. It has 12 claims, all with quotes. The quote checker reports no problems and the file validates against the claims schema. Nothing is committed.

**Text read.** `paper/10.7554-elife.109538.txt`. Its header says "version of record", but the page it holds is the eLife Reviewed Preprint v1 (doi:10.7554/eLife.109538.1, 9 Jan 2026, "Not revised"). It has the main text, Methods A to E, the legends of Figs 1 to 4, the supplementary legends S1 to S3, and the Data availability statement. There is no PDF. The paper links no code: it says the simulation code "will be made available in a Github repository at a later stage", so no repository was read.

**Claims.**
- **Statistics:** none. The paper reports no statistical test anywhere.
- **Expected values:** 7 claims have them (11 values in all).
- **Criteria:** all 12 claims have one.
- **Testable on DANDI:000207 (5):** the subject count (18 subjects, 14 kept); the dip in non-boundary neurons about 130 ms after the boundary-neuron peak, then a ramp (Fig. 3a); the same pattern in individual subjects, except P64CS and TWH120 (Fig. 3b, S3); and the control showing no dip at clip onset (Fig. 3c).
- **Simulation or theory (4):** basic capacity of 4 (Fig. 1d top); chunking retrieves all 6 items (Fig. 1d bottom); the new limit M* = 2^(C-1), which is 8 for C = 4 (Eq. 1); hierarchical retrieval (Fig. 2b).
- **Model variant (1):** delayed Hebbian binding as a replacement for the imposed chunking inhibition (Fig. S2).
- **`data: elsewhere` (3):** the Fig. 4 claims rest on the published recall tables of Miller and Selfridge (1950) and its Danish and Hindi replications. These are in no archive.
- **No `data` field:** the schema has no value for simulation, so those claims keep the default, which implies the dataset. Each criterion says the dataset cannot test it.

**Details left open, with the readings named.**
- **Boundary-neuron selection:** (a) the classification of the earlier paper on these data (Zheng et al. 2022), or (b) re-selection by that paper's own method.
- **Onset-neuron selection:** the same two readings.
- **Trials:** clips with a cut (soft and hard) only. This is the one reading the text supports.
- **Bins and smoothing:** 10 or 25 ms bins, each with no smoothing or a 50 ms Gaussian kernel.
- **Window:** -1 to 2 s around the cut, a standard choice.
- **Z-score reference:** (a) the whole window, or (b) the pre-cut part only.
- **Dip, ramp and lag:** the paper gives no measures, so I fixed them and labelled them as such. The dip is the minimum within 500 ms after the boundary peak, below the pre-cut mean. The ramp is a positive slope from the dip to 1 s after the cut. The lag tolerance is widened to one bin when the bin is wider than 13 ms.
- **"Most subjects":** read as more than half of the 14.
- **Fig. 4a common slope:** (a) one least-squares fit with a shared slope, or (b) the mean of the separate slopes.
- **"Within the region predicted" (Fig. 4b):** (a) within 10% of 8, or (b) at or below 8.

**Missing from the text.**
- **Equations and parameters:** Eqs. (1) to (15) and the Table I simulation parameters did not survive extraction. Eq. (1) is recovered from the words in the text. These gaps block rerunning the simulation claims, but they are not on the dataset.
- **Figure values:** with no PDF, figure axes and plotted values could not be read.

None of the Fig. 3 claims needs any of this.
