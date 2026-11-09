The claims file for DANDI:001785 is fit for an attempt, and its last `checks` entry says `ready: true`.

**Checker result:** `32 claims, 32 quotes, 51 statistical values, 8 problems`. All 8 problems are "VALUE NOT FOUND" notices for numbers the paper prints with different spacing or digits (for example "7.70E-06" and "9.10 × 10 −1 3"). I found each one by reading, in Supplementary Table 9 and the legends of Fig. 5c, Fig. 6b, Fig. 6e and Extended Data Fig. 10d, so none is a real error. Every quote matched the text word for word.

I also downloaded the paper's own scripts from DANDI:001773 (not the dataset) to check the method details the file takes from the code. They match: the ANOVA models, the 0.05/122 threshold, the 0.15 cutoff for the circular plots, area 25 included in the limbic network, and the paired t-test for monkey D. The error degrees of freedom of every reported ANOVA also come out right from the reported voxel and field counts.

**Changes, by claim**
- **fig4b-dbs-widespread-roi-changes:** I removed the statistics entry ("rank-sum p < 0.01, Bonferroni"). It is the threshold used to count significant ROIs, which is a method, and the counts are already in `expected`. The test is now fixed as each ROI's changes against zeros, as the Fig. 4b legend and the code have it; pre against post is shown only as a variant. Header block [MATRIX] is updated to match and notes that the code's circular plots use only the 54 cortical ROIs.
- **fig4a-cortical-decrease-subcortical-increase:** the per-run matrices from the Methods are now the main analysis, with the code's one matrix per session as a variant. The criterion had accepted either one. The mean and median summaries must now agree.
- **fig2a-cb-fa-increase, fig2b-mcc-cb-increase, fig5b-scc-decreases, ed10c-sham-subcortical-decrease:** these criteria said "reproduced under one reading" of details the paper leaves open (lead-track exclusion, how CB subregions are assigned, the seed-map runs and maximum, the summary statistic). The protocol requires all readings to agree, and the claim is blocked as `methods_underspecified` when they don't. I reworded them and added a header note.
- **fig4-control-no-systematic-pattern:** I dropped a condition the paper never states (that the control group has fewer circular-plot pairs beyond 0.1 than the DBS group). Those counts are now reported but not judged.
- **fig3f-gratio-decrease:** "thicker myelin" is now "a greater degree of myelination", the paper's words.
- **fig6b-sham-dacc-cb-decrease:** the statement now adds "although diffuse reductions were seen across the CB", as the quoted sentence says.
- **disc-no-motor-roi-change (new):** the Discussion says connectivity between the SCC and the motor cortex or supplementary motor area did not change (Supplementary Table 9). No claim covered it. It is judged as a claim of absence, on the paper's post hoc test at p < 0.05.

**Still open (recorded in the file)**
- The paragraph numbers in the sources can't be checked, because the text file has no paragraph breaks. The behavior claim's "paragraph 2" may really be paragraph 1. The figure references in each source are enough to find the place.
- For ed10c, the claim reads the paper's "more random" cortico-cortical changes as a share of negative pairs closer to one half than in the DBS group. The paper gives no measure for this, so it is the claim writer's reading.

Nothing is committed or pushed.
