# Verifier report, round 2: Azcorra, Gaertner et al. 2023 on DANDI 001038 (0.241111.1719)

The claims file has 29 claims. The attempt record gives 18 reproduced, 7 partially reproduced, 1 not reproduced and 3 blocked. I checked everything against the notebook's printed outputs. I did not re-download the paper, so the values the record attributes to the paper beyond the claims file are not re-checked here.

## 1. Agreement with the stated outcomes

I agree with all 29 outcomes.

- **fig5ab-transient-scaling:** the main result changed in response to my round-1 point. It now uses the recomputed onsets that are also stored. The outcome is still partial (cell 43): Vglut2 241.3% and Anxa1 231.9% are outside tolerance, Calb1 246.2% is inside, and all three have p×3 ≤ 0.002.
- **The three blocked claims:** I accept the record's categories. `not_runnable` covers Seurat and LIGER not being installable, and `other` covers histology that rests on manual counts that were never deposited. I cannot see docs/protocol.md to confirm the category rules. The record also points out that snrna-anxa1-within-aldh1a1 is the partial snRNA test I proposed in round 1.

## 2. Statements the numbers do not support

1. **Cell 93, Summary:** "with them the reward responses and the Calb1 trough lag equal the paper's numbers". The Calb1 code-timing lag is 0.160 s against the paper's 0.17 (cell 25). That is within tolerance but not equal.
2. **Cell 93:** "with the code's windows its response means to the decimal". The DAT air puff mean is 2.46 against 5.3 (cell 52), and the DAT large-minus-small difference is 1.83 against 1.9 (cell 58).
3. **Attempt record, code_mismatch finding:** "The paper's reward and air puff means equal those of the code's windows". The DAT air puff mean (2.46 against 5.3, cell 52) contradicts it. This should be limited to rewards and to the Vglut2, Calb1 and Anxa1 air puff means.
4. **Cell 41 and the ed6f notes:** "the per-recording medians are 0.5 and 0.25 s, so a few recordings at the window edges ... do not explain the difference". For Calb1 the numbers point the other way (cell 40):
   - The median of 0.25 s is within the paper's tolerance (0.207 to 0.253 s).
   - The mean of 0.320 s equals the upper quartile (0.32), so the distribution is strongly right-skewed.
   - The Calb1 gap is therefore a tail of late peaks, not a shift of the whole distribution. Only Vglut2 is clearly later than the paper (median 0.5 s, peak of the mean 0.44 s, against 0.35 s).
5. **Cell 83:** "the same mice, more recordings". The output gives Anxa1 6 mice against the paper's 5. The notebook only shows matching counts and cannot show that the mice are the same ones.
6. **Cell 62 and the ed8f notes:** "The Calb1 n is 8 against the paper's 10". This implies Calb1 is the only mismatch. Cell 61 also prints Anxa1 36 against 42 and DAT 33 against 42, and Vglut2 comes from 3 mice.
7. **Cell 47 and the fig4g-reward-response notes:** "the paper's numbers come from the code's windows" is stated as a fact. The output supports it strongly for rewards (7.90, 12.40, 5.88). It is still an inference, and it does not hold for the DAT air puff mean.
8. **README and cell 0:** "about three minutes". Cell 94 reports 2.1 min. This is minor.
9. **Cell 17 and the locomotion notes:** "the excess is spread over locations, single- and dual-fiber files and sessions with and without stimuli". Cell 16 shows only our counts per split, not the paper's, so where the excess sits cannot be measured. All Anxa1 recordings are dual-fiber and all Calb1 recordings are DS, so for those groups the excess sits in one category. This is weakly supported at best.
10. **Findings not backed by printed output:** none of these appears in the notebook's outputs:
    - the 123 files with two `normalized_fluorescence` values,
    - the malformed DOI link and the asset-summary fields,
    - the paper_inconsistency items.

All other "**Result:**" sentences, the README table, and the remaining notes and measured values match the outputs.

**My round-1 reasons in the record:** the attempt record restates them faithfully and in substance in my words. One omission: for ed8f the reason leaves out the Anxa1 and DAT count differences (36 against 42, 33 against 42) that I raised under problem 6, and the response does not address them.

## 3. Round-1 points

**Resolved:**
- 5, ed9k denominator: the 160 components capture 100.00% of trace(XsᵀXs), so the percentages are unchanged (cell 73).
- 6, RewardNoRest: the rest rows start exactly 0.01 s after their rewards and have the same durations. 2647 onsets equal rewards minus rest rewards in every file (cell 61).
- 7: the 1-bin offset is the code's own.
- 9 and 11: documented, and a one-to-one mapping variant gives 92.6%.
- 10: the paired ratio is identical, and the onset choice is now explicit.
- 12: deep-band variants added (cell 76).
- 13: categories named.
- Depth meaning: depth tracks DV with ρ 0.92.
- 2, response windows: the explanation is settled, and the outcomes follow the pre-set Methods rule.

**Remaining, bearing on conclusions:**
1. **Locomotion overcount (problem 1), unresolved.** All 18 locomotion-dependent claims rest on 50/28/82/89/85 recordings against 42/22/47/74/75. No variant reproduces the paper's counts, and the record says the paper's manual exclusions cannot be repeated. fig2jk passes by 0.02 points on PC2 and 0.54 on PC1, so its "reproduced" depends on this selection.
2. **ed6f peak timing (problem 3), partly explained.** Calb1's gap comes from a skewed tail, since its median matches the paper (item 4 above). Vglut2 is about 0.1 to 0.15 s late by every summary, and the cause is not found.
3. **DAT air puff (problem 4), unresolved.** 2.69 against 5.3 with the same n of 69. Per-mouse means range from −3.83 to 6.03, and Dat-G557 (15 recordings, −0.60) pulls the mean down. The cause is not found.
4. **Count mismatches that do not change an outcome, unexplained:**
   - fig4i: Anxa1 37 and DAT 50 against 42 and 55.
   - ed8f: Calb1 8, Anxa1 36 and DAT 33 against 10, 42 and 42.
   - SNc locomotion: Vglut2 26 and Anxa1 30 against 28 and 34.

The summary and the code_mismatch finding should be corrected as in items 1 to 3 of section 2.
