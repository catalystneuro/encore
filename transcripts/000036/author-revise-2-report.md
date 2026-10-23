I made the round-2 fixes and re-ran the entry. **No outcome changed and none is proposed.** The verifier agreed with all 27 outcomes, so there is nothing for a third round to review.

The re-run (`python tools/entry.py all entries/000036-mayner-2022`) passed all three notebooks with 0 errors, and `entry.py check` passes. Every number the outcomes rest on is the same as in round 2. One conclusion sentence (ext3-2) was edited after that run; it is markdown only, so no output changes, but the executed copy still shows the old wording.

**Text corrected and output added, point by point:**
- **Main cell 21:** decoding with the windows moved one presentation back now "falls to chance (mean 0.085, chance 0.083)". It no longer says "below chance (about 0.04)".
- **Main cell 46 (ext3-2-sensitivity):** this is the output the verifier asked for. The cell now prints which layers and areas are significant in each set of the paper's own `stats.parquet`:
  - L2/3 is the only significant layer in all 108 sets.
  - AL and AM are both significant in 28 sets, AL alone in 50, AM alone in 24, and neither in 6.

  The conclusion, the notes and the code_mismatch finding now cite these numbers. The finding gains "neither in 6".
- **fig3b (cell 40, notes, finding):** these no longer cite "the code's printed Figure 3 output 0.128". They now cite what the notebook prints from the paper's own per-trial values: 0.128 with the code's pooled SD (cell 39), and the 0.0048 lower bound from the post hoc test (cell 26).
- **L0 detector (cell 79, header, ext1-3 notes):** I dropped the claim that a current compiler rejects the C++, because the notebook doesn't show it. The text now says only what cell 78 prints: the `<limits>` include is missing. The record also now says what the earlier build outside the notebook found. With `<limits>` added and the Python 2 prints rewritten, the package built and `arfpop` ran on a synthetic trace. `l0_analysis.py` was not ported and no events were computed. The claims stay blocked as `not_runnable`, because the software cannot be installed as published.
- **fig4-locomotion:** "210 s" is replaced by the actual times: 217 s in the run the verifier reviewed and 176 s in this one. The round-1 response now says "about three minutes".
- **Round-1 record:** the fig4-locomotion reason now includes the verifier's problem 3 on the effect size, which it had pointed out was missing.
- **Round 2 under `verifications`:** recorded with all 27 claims, using the verifier's own reasons and my response to each.

**Not done:**
- **Patched detector build:** I did not move it into the notebook. It needs patched sources and g++ outside the locked environment, and it would no longer be the paper's software. It is described in the record as not run here and decides nothing.
- **Open points left as they are:** two items still wait for a reader's answer: the agreement rule for ext3-2-sensitivity and which pooled SD discussion-session-effect-sizes means. The verifier accepted both outcomes, so I left the outcomes and the questions in `questions/000036.yaml` unchanged.

Nothing was committed or pushed.
