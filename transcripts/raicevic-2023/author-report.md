The attempt for DANDI:000491 is done through step 6. It is pinned to version 0.230602.1307, the latest published one: the earlier 0.230427.1809 has no PVS masks for locations L, M and N, so it cannot support the analysis. Lock, check and the clean run all passed, the run taking 1,600 s (27 min). The handover package has been built, and nothing is committed.

**1. Outcomes per claim**

| Claim | Outcome |
|---|---|
| cross-section-counts | not reproduced |
| segmentation-validation-overlap | blocked: data missing |
| fig5a-pvs-area-scales-with-vessel-area | not reproduced |
| fig5e-area-ratio-distribution | partially reproduced |
| fig5bc-area-intersegment-variation | reproduced (rests on an assumption) |
| area-ratio-per-location | not reproduced |
| fig5d-polynomial-closest-area-ratio | partially reproduced (assumption) |
| table2-fit-area-ratio-peaks | partially reproduced (assumption) |
| fig6a-resistance-power-law | partially reproduced |
| fig6b-resistance-segmentation-peak | partially reproduced |
| resistance-per-location | not reproduced |
| fig5b-polynomial-closest-resistance | partially reproduced (assumption) |
| ellipse-annulus-underestimate | partially reproduced |
| spline-resistance-five-times | reproduced (only under the P4 a or P1 b readings) |
| fig7-velocity-profiles | reproduced (assumption) |
| vessel-radius-peak | reproduced |
| fig8-ellipse-parameters | not reproduced |
| fig9c-pvs-two-lobes | reproduced |
| fig9e-pvs-width-asymmetry | not reproduced |
| left-right-no-difference | blocked: methods underspecified (the readings split 2 against 1) |
| fig9a-heights-taper | partially reproduced |
| fig9f-pvs-concave | partially reproduced |

**2. What was found about the dataset**
- **Missing data:** the 2D time series used to validate the segmentation are not in the dandiset.
- **Mask overlaps:** the vessel and PVS masks still overlap in 11 of 14 files (up to 344,565 voxels at E), although the Methods say overlaps were removed.
- **E and F:** the PVS mask fills 98 to 99% of the deepest plane. E, F and G have median area ratios of 7.8 to 9.6, against 0.7 to 2.2 at the other segments.
- **Depth step of L, M, N:** the files state 0.648 µm per plane, but their session descriptions say 1 µm. The vessel cross sections are round at 0.648 µm, which supports the stated value.
- **Wavelengths:** the vessel (FITC) channel is given 698 nm emission, where the Methods say 525 nm.
- **ChanB:** it is described as "microspheres", which the paper never mentions.
- **Ages:** the files give 573 to 603 days for mice 1 and 2, and 76 to 113 days for most others, against the paper's "8 to 12 weeks".
- **Versions:** the first version lacks the L, M and N masks. No duplicate recordings (all 14 mask digests differ).

**Assumptions:**
- **Edge exclusion width (P4):** adopted reading (b), the polynomial width, for fig5bc. Reading (a) leaves 5 of the 14 segments with no cross section, while the paper analysed all 14.
- **Overlap pixels:** pixels in both masks are counted as vessel. The share exceeds 5% of the PVS in 258 of 7,568 cross sections, 239 of them at J. The other assignment was not run.
- **Polynomial region across the vessel:** I closed it at the vessel centre height. The alternative was not run, which is why fig5d, table2, fig5b and fig7 are marked as resting on an assumption.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings): which left/right test was used; how the median width for the edge exclusion was measured; and the code, which is not public.

**Question for a reader** (`questions/000491.yaml`, fig8): is the ellipse fitted to the PVS alone, as the claims file says, or to the PVS and vessel together? Together gives R3 29.9 µm, R3/R1 0.951, R2/R1 2.743 and R3/R2 0.431, close to the paper's values. The PVS-only fit gives R3 13 to 21 µm.

**3. Where the protocol was unclear, wrong or missing something**
1. Running "every reading" multiplies the work: up to 128 combinations per claim, and with them more chances of a match by luck. I ran them all and printed the counts of matching combinations.
2. Two of the claims file's readings could not be run in full here:
   - P2 (b), all skeleton points, gives 438,100 points, more than 30 h of work. I ran it for the counts only and recorded this as a deviation, not as `too_large`.
   - The fits' resistances were solved for erosion 3 only.
3. The protocol does not say how to report `measured` when nothing matches. I recorded a stated reference combination.
4. For left-right-no-difference, the claims file's own rule (methods_underspecified when the readings disagree) clashes with the protocol's rule that a claim of absence is judged on the paper's test. Here the paper names no test, so I followed the claims file.
5. When a claim depends on peaks from two other claims that bin differently (log bins allowed in one, not the other), the protocol gives no rule. I paired both peaks under the same bins.
6. The "**Result**" cells and the summary are markdown. I wrote them after the run and copied them into the executed copy; the code cells are identical to what ran.

**4. Runtime and failures**
- The clean run took 27 minutes. The first development version took 44 minutes and was restructured.
- Nothing failed in the final run.
- Deleting my development pickles in the session's temporary folder was refused for lack of approval. They are outside the repository.
- The untracked dotfiles at the repository root (`.bashrc`, `.idea`, `scripts` and others) are sandbox device mounts, not mine; I left them alone.
