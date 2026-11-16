**Verifier report, round 2: Tingley & Buzsáki 2018 on DANDI:000213 (0.261109.2219)**

I counted from the files. The claims file has 32 claims and the attempt record has 32 outcomes: 8 reproduced, 9 partially_reproduced, 12 not_reproduced and 3 blocked. Cell 0 now has a "tested" table, not an outcome table, so round-1 point B15 is resolved.

### 1. Outcomes and assumptions

| claim | agree? | note |
|---|---|---|
| ls-neuron-count, hpc-unit-count, ls-active-neurons | yes | |
| fig2-ls-phase-vs-shuffle | yes (assumed) | aa1 0.405; the four "undefined = 0" readings give 0.394–0.499. Cell 19 shows the test is not calibrated under either treatment of undefined phase: shifted phases pass 0.380 against 0.405 real. So the fraction does not measure phase coding, and the record says so. |
| fig2-ls-phase-beats-rate, fig2e, fig2fg | yes (assumed) | Under "undefined = 0" phase is never better than rate. Under the left-out variant the shifted-phase null matches the real data (cells 22, 25, 28). |
| fig1i-hpc-rate-phase-equivalent | yes (assumed) | Judged on the adopted aa1, where both KS tests give p < 0.05. Note that ab1 with fields (b) gives p = 0.066 and 0.82, and "ties to lowest bin" with fields (b) gives 0.18 and 0.82; both of those pass (cell 31). The criterion has no "under one reading" clause, so using the adopted reading for a claim of absence is reasonable. But see point 3c on consistency. |
| ls-lower-peak-info, ls-few-place-fields, hpc-place-field-properties, ls-place-fields-unstable, speed-independent | yes | |
| fig1e-phase-info-smaller-scale | yes (assumed) | Partial by the criterion's wording. Shifted phases give the same smaller scale (null medians 12.5–21, cell 44). |
| fig1g-phase-more-info-fine-scale | yes, by the criterion's wording only (assumed) | Holds under 1 of 4 field × level readings: fields a, equal-count levels, KS test, 37/44 = 0.841. The t-test version (35/44 = 0.795) and box fields (0.750/0.795) fail. The fine-scale excess is the same with shifted phases (0.695 against 0.684, cell 47). Under phase = 0, a bin with no nearby spike becomes cos = 1, so at 2–3 bins the "phase" information measures whether a spike is near, not its phase. The assumption itself produces the match. The record says the match does not show phase information; it should also say that the phase-0 fill causes it. |
| fig3-ls-phase-reliable | yes | |
| fig4d-depth-gradient | yes, by the criterion's wording only (assumed) | Holds in 1 of 24 combinations (decoder reading × depth × site direction): bb1, first depth, sites deepening. The per-animal r are all negative but small (DT9 −0.14). Pooled r = −0.209, p = 0.11. Within sessions 26/47 are negative, which is no more than chance. The adopted aa1 fails (cell 56). bb1 has no shifted-phase null (`NULL_READINGS` covers only aa1, ba1, aa0, ba0). Both assumptions (LS depth, site direction) are stated, and the record calls the result a bare majority. |
| fig4e-onset-depth | yes (assumed) | |
| fig4e-onset-mediolateral | yes (assumed) | The between-animal difference holds: Watson-Williams p < 1e-5 under every reading, which the criterion allows; Kruskal-Wallis p = 0.040 under bb1. \|r\| ≥ 0.8 is reached only under the ba0 variant. |
| fig5-assemblies | yes (assumed) | Fraction 0.266 or 0.075; median timescale 4/9 or 20/41 ms. The assumptions (7 % sample, fit per trial, trials cut to the shorter in shuffles, zero-lag rule dropped) are stated. |
| fig5g-assembly-neurons-stronger-phase | yes (assumed) | Weak test: under the Methods rule only 13 neuron-conditions are outside an assembly. |
| figs5-assembly-independent-of-locking | yes, by the criterion's wording (assumed) | Fragile. The assembly set does not reproduce fig5 (0.266 against 0.185). Under rule (b) Pearson p = 0.056 and 0.081, and Spearman is significant (0.019, 0.036). |
| **fig6-session-counts** | **no → not_reproduced** | The criterion has no partial rule ("Reproduced when all three counts are within tolerance"). The LS-with-CA1 count is 25 or 33 against 63 ± 6.3. The 57 from flagged CA1 channels is a variant, not the criterion's reading, because the claim is about CA1 *neurons*. The record applies this same logic to figs1f but not here. I agreed with partial in round 1; that was my error. |
| fig6c-ca3-coherence-increases, fig6d-cfc-stronger-ca3 | yes | |
| fig6e-assembly-position | yes (assumed) | The partial rule needs only the signs. The signs hold under fields (a) with assembly pairs; the curve correlation turns positive under fields (b) with the session reading (cell 86). |
| figs7-ensemble-ls-phase-best | yes (assumed) | The ensemble decoder leaves undefined phase out, unlike the adopted phase 0. That is stated, and it would favour LS, which still loses. |
| figs2-rate-phase-independent, figs1f-trial-counts | yes | |
| figs3, figs6, fig7 (blocked) | yes | |

On the main assumption (undefined phase set to 0): it is stated and backed by the calibration, so it is reasonable. But neither treatment gives a working hippocampal phase decoder. Under aa1, real phase MSE is 6,573 against 6,641 for shifted phases and 6,707 for chance (cells 4 and 16). The decoding outcomes therefore show what this decoder does, not what the paper's data contain. The finding addressed to the authors covers this.

I found no place where the claims file misreads the paper.

### 2. Statements the printed numbers do not support

- **README:** "It runs in about 40 minutes on 4 CPUs." Cell 97 prints 50.4 min.
- **Record, fig5-assemblies notes:** "The fits took 1,071 s on 4 CPUs." Cell 68 prints 1227 s. The verification response's "about 0.5 s per pair" does not match either: 1227 s × 4 CPUs / 7,098 pairs ≈ 0.69 CPU-s per pair.
- **Cell 63 and record, fig4e-onset-mediolateral:** "0.075 to 0.739". Cell 62 prints 0.074 to 0.740. "p = 0.13 to 0.69" should be 0.13 to 0.68 (largest printed value 0.678574).
- **Record, fig2fg notes:** "the hippocampal ones (-859 to -2,305) are larger in magnitude". This holds only for conditions. For ba0 sessions, LS −1,804 is larger than hippocampal −1,448 and −1,603 (cell 28). Cell 29 correctly says "at the condition level". The outcome does not change.
- **Record, finding on undefined phase:** "Set to phase 0, the shifted-phase check is near its nominal rate." Shifted phases beat rate in 0.028–0.059 of conditions, 3–6 times the nominal 1 % (cell 16).
- **Record, fig6-session-counts:** "accounts for much of the shortfall". Cell 78 says "part". Adding all 17 DT8 sessions would still leave 42 or 50, short of 63.
- **Record, speed-independent:** "fewer than five trials with five or more spikes". The threshold is not printed; cell 65 only says "too few trials of 5+ spikes".

All other sentences I checked in the conclusions, the Summary, the README and the record notes match the outputs.

The record's verification entries put my round-1 reasons in my own words, adding the relevant B items. That is accurate. Every `agrees` flag matches the round-1 outcome against the earlier record.

### 3. Round-1 points

**Resolved:**
- B1: phase 0 adopted, and the synthetic and real-data nulls were run.
- B2: the samples-split leak is disclosed.
- B4: MATLAB-style smoothing now used for the best scale.
- B5: ties broken at random; `chance_rate` printed.
- B6: all decoder readings run for fig4d/fig4e.
- B7: Watson-Williams run.
- B8: both depths and both site directions shown, with a metadata finding.
- B9: fig5 run on a sample.
- B10 to B15.

**Remaining that bears on a conclusion:**
1. **fig6-session-counts** should be not_reproduced (no partial rule).
2. **B3 is disclosed but not fixed.** The information measure under phase 0 still produces the fig1g match and the fig1e phase scale, with the null equal to the real values. There is no shuffle-subtracted information and no minimum sample count. fig1g's "reproduced" rests on this, and on one passing reading out of four.
3. **Readings are chosen inconsistently.**
   - fig4d is reproduced on whichever of six decoder readings passes (bb1).
   - fig1i is judged on the adopted aa1 only, though ab1 with fields (b) passes both tests.
   - The record should apply one rule to both, and run the shifted-phase null under ab1/bb1 if bb1 carries a conclusion.
4. **The decoder is weak.** Hippocampal rate MSE is 6,329 against 6,733 for uniform guessing. Recorded positions beat positions 1 s later in only 30 of 47 sessions (cell 4). This bounds every decoding outcome. It is disclosed in the Summary but not in the notes of the decoding claims.
5. **fig5 cluster:**
   - The zero-lag rule was not applied.
   - 874 of 7,098 pairs have their best window at 1 ms.
   - The assemblies match neither the paper's fraction nor its timescale.
   
   So figs5 "reproduced" (absence) and fig6e "partial" are tested on assemblies that do not reproduce the paper's. Their notes should say so.
