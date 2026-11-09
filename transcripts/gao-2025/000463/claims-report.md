I wrote the claims file at `claims/000463/10.1523-jneurosci.2218-24.2025.yaml`. The quote checker reports 0 problems: every quote matches word for word, and all 84 recorded statistical values were found in the text.

**Text read.** I read the version of record as PubMed Central serves it (PMC12139594), with the full Methods, Results, figure legends and Discussion. The paper has no supplement. No PDF was provided. The paper links no code, so I read none.

**Which dataset.** The paper says its data are in DANDI **000946**, not 000463. The 000463 description cites this paper but describes only S1 recordings, with "different intensities and PRFs", and lists 4 subjects. The paper reports 16 rats recorded in S1 and POm, plus 12 more in S1 and auditory cortex (AC). The opening comment records this, names 000946, and leaves it to the author to find what 000463 holds.

**Counts.**
- **Claims:** 37, all with quotes, none marked `inferred`.
- **Coverage:** Figures 4 to 11 at panel level, sham and control, the synthesis in the Discussion, unit and pair counts, and the in situ pressure from the Methods.
- **Statistics:** 27 claims carry 84 entries.
- **Criteria and expected values:** all 37 have a criterion, and 12 have expected values.
- **Not covered:** Figure 3 shows example units the paper does not identify, so it is tested through the Figure 4 claims. Figure 2, the target check, is a method.

**Details the paper leaves open, with the readings named:**
- **O1, RSU/FSU k-means:** inputs from each unit's mean waveform, or per spike with a majority vote. Features in raw ms or z-scored. Units pooled across all regions or per region, with k = 2.
- **O2, normalizing to the 67 ms before stimulation:** ratio of trial means, or mean of per-trial ratios.
- **O3, baseline sample for the post hoc Wilcoxon:** the pre-stimulation window itself (100% for every unit), the window from −134 to −67 ms, or a one-sample signed-rank test against 100%.
- **O4, Bonferroni factor:** the number of windows, or the number of parameter levels. I read the printed p-values as already corrected, since several are printed as p = 1.0.
- **O5, one-tailed direction for claims of absence:** greater only, or both directions.
- **O6, dSTTC equation:** missing from the text. The reading named is the Cutts and Eglen form with the directional terms the Methods define.
- **O7, normalizing dSTTC:** a difference from pre-stimulation, or a relative difference. A pair's value is the mean of per-trial values, or one value from concatenated trials.
- **O8, which pairs:** all cross-area pairs recorded in the same session.
- **Smaller ambiguities, handled inside the claims:**
  - The window for Figure 4's post-sonication results (134–268, 134–201 or 201–268 ms).
  - "Higher than 1,500 Hz", read as including 1,500 Hz or not.
  - An unlabelled duty-cycle entry in the Figure 7C list, read as 30%.
  - The direction of the 30 Hz differences in Figure 9A.
  - The post-sonication window for the auditory cortex results.
  - Figure 11 panel labels that disagree between text and legend.
  - The text and legend disagree on the direction of the AC to S1 FSU correlation at 30 Hz, so both directions are named.

**Missing from the paper:**
- The dSTTC equation; the PDF should be read to confirm O6 before the attempt.
- No analysis code.
- No p-values for the post-sonication dSTTC decreases in Figure 10A.
- No statement that the hydrophone scans or the sham trial times were deposited.

Nothing was committed.
