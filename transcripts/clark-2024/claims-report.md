I wrote the claims file at `claims/000943/10.7554-elife.89356.yaml`, and the quote checker passes it with 0 problems.

**Text read.** I read the version of record: the eLife reviewed preprint, version 3 (RP89356), as full text from Europe PMC (PMC10977970). That covers the Results, the figure and figure-supplement legends, the Methods, and the reviews with the author response. Supplementary file 1 (the per-mouse table of cells) and the MDAR checklist were also there. No PDF was supplied.

**Code read.**
- The paper's code, `MattNolanLab/eLife_Grid_anchoring_2024`, at commit 670c45a. The v1.0.0.0 tag differs from it only in the README and LICENSE.
- The preprocessing repo that code's README points to, `in_vivo_ephys_openephys`, at f913080. The paper pins no version of it, so I ranked it below the paper's own code.

**Claims.** There are 31: 30 have quotes, and 1 (the Supplementary file 1 table) is marked inferred. 21 record the paper's statistics (44 values), all 31 have criteria, and 7 have expected values. They cover:
- the grid cell counts and properties;
- the session-level and trial-level classifications (Figures 2 and 3, and Figure 3 supplements 4 to 7);
- the agreement between simultaneously recorded cells and the spatial information of non-grid cells (Figure 4);
- the behaviour results (Figure 6 A to F, and Figure 6 supplements 1 and 2).

**Details the paper leaves open, and the readings named:**
- **">85% of trials":** the code counts this over rolling windows (≥0.85), the text says trials. Both are run. Which modes count as stable is also open: task-anchored or task-independent only, or aperiodic as well.
- **Third group in Figure 3 supplement 4:** the legend reads it as stable aperiodic cells; the code uses every other grid cell. Both are run.
- **Response variable in Figure 3 supplement 7:** either task-anchored against any other class, or task-anchored against task-independent. No code for this test exists, and none for the tests in Figure 3 supplement 5.
- **Random effects for the Figure 4E data-against-shuffle test:** session within mouse, or with the two cells' identities nested as well. The R notebook fits both.
- **"Similar" in Figure 2E (non-grid against grid proportions):** no test is reported. The readings are a relative size of the differences, or a Fisher exact test.
- **"Spatial" stopping in Figures 6A and 6C:** either the reward-zone density is above baseline by more than its SEM, or the profile's peak lies in the reward zone.
- **Hit/try/run split:** the Methods use the 95th percentile of hit trials' reward-zone speeds; the code uses mean ± 1.96 SD. Both are run for Figure 6E.
- **Field size and grid spacing:** the Methods don't define them; the preprocessing repo's definitions are used.

Where the code differs from the Methods, I follow the Methods and show the code's choice as a variant:
- stop smoothing (SD 2 bins in the code, 1 cm in the Methods);
- grid-cell criteria (the preprocessing repo uses spatial information and a mean + 2.326 SD threshold);
- ties in the grid consensus (the code resolves them to task-anchored, the Methods pick at random);
- trial subsampling for spatial information;
- units with under 15% task-anchored trials in the template method (the code keeps them, the Methods discard them).

**Gaps that affect claims.**
- **Figure-only values:** without the PDF, I couldn't read values shown only in figures: the Figure 2E percentages, the Figure 6 hit percentages and Ns, and the Figure 6F odds ratios. Those claims are judged on direction and on the reported p-values.
- **Probe-trial claim (Figure 6D):** the text says hits fell, but the legend's test gives p=0.19. It is judged on direction only.
- **Sign of the Figure 4E contrasts:** the printed T values are all negative although grid pairs are reported higher. The direction is taken from the text.

I left out the simulation validations, which are not tests on data.
