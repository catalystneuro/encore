**Verifier report, round 2: garud-2026-01 (Garud & Morris 2026, DANDI:001552 0.250828.1728)**

**1. Outcomes**

The claims file has 18 claims and the attempt record has 18 outcomes. I agree with all 18.

| Claim | Outcome | Agree | Basis |
|---|---|---|---|
| floeder-subjects-sessions | reproduced | yes | Cell 14: 18 mice, 16 to 24 sessions, both classes in every mouse |
| fig4a-lick-short-above-long | reproduced | yes | Cell 17: t(17)=4.15, p=6.7e-4, short higher in 16 of 18 |
| fig4b-long-iti-dip-below-baseline | partially_reproduced | yes | Cell 20: long-ITI part below 0 under all 8 readings; short-ITI last bin −0.0067 / −0.0056 |
| fig4d-dip-deepens-with-training | partially_reproduced | yes | Cell 24: 0 of 16 readings reproduced, 10 of 16 partial |
| fig4c-lick-rate-rises-with-training | reproduced | yes | Cell 28: r 0.648, p=1.2e-5 |
| krausz-included-observations | reproduced | yes | Cell 31: 264,042 rows |
| fig2a-ramp-toward-goal | reproduced | yes | Cell 34: −0.68 per distance, −0.30 per hex, both p<0.001 |
| fig2b-ramp-scales-with-reward | reproduced | yes | Cell 37 |
| fig2c-ramp-similar-early-late | reproduced | yes | Cell 40: p=0.52 |
| fig2d-ramp-scales-with-velocity | reproduced | yes | Cell 43 |
| fig2e-velocity-covaries-with-distance | reproduced | yes | Cell 46 |
| fig2f-coupling-grows-near-goal | reproduced | yes | Cell 49, reading (a); depends on taking distances 1 to 20, which is stated |
| fig2gh-stationary-dip | reproduced, assumed | yes | Cell 52 (b1): t=−4.274 |
| fig3-recovered-value-increases | partially_reproduced, assumed | yes | Cell 55: 7 of 10 under both row sets |
| fig3cd-gaussian-shape-wins | partially_reproduced | yes | Cell 58: 9/1/0, and mean R² is never above 0.8 for all four shapes |
| fig5bc-gaussian-ct-td-best | reproduced | yes | Cell 61: lowest summed BIC, 8 of 10 rats |
| fig5d-tonic-term-and-gaussian-contribute | reproduced | yes | Cell 64 (a): 1201.0 / 665.0, within tolerance with a margin of about 30 |
| figs2-no-velocity-coupling-without-goal | blocked (methods_underspecified) | yes | Supplement not available |

Assumptions (`assumed: true`):
- **fig2gh, "non-approach" read as all rows off the ports.** It is stated, and it is reasonable given the Figure 2G-H legend. It was picked after the fact because it is the only row set that matches the paper (the Methods' set (a) gives t=−2.81, and adding the port rows gives −1.46). The notes say this openly.
- **fig3, no minimum count per position.** It is stated and reasonable, since it is the literal Methods reading. Two smaller points:
  - fig3 records the approach rows (a), while fig2gh adopts (b1) for the same moving/stationary split. The record does not reconcile this, but both row sets give 7, so the outcome does not change.
  - fig4b needs no `assumed` flag, because all 8 readings give the same outcome.

**2. Sentences the printed numbers do not support**

- **Attempt record, fig3 notes:** "One fit (IM-1292, minimum of 5) has A = -9e10 at σ near 0.8". Cell 55 prints A = −2.59e+11 under (a) and −2.44e+12 under (b1).
- **Attempt record, fig5bc notes, and cell 62:**
  - "lower their SSE by 0.5 to 21": the narrow-search SSEs are never printed. Cell 61 prints only the summed ΔBICs (473→412 and 1679→1623).
  - "its SSE within 0.2 of the fit at σ = 100": no σ=100 SSE is printed for IM-1322.
- **Attempt record, fig3 notes:** "Widening the profile scale search leaves the counts unchanged". No narrow-search fig3 run is printed in this notebook. The claim agrees with my round-1 counts, but cell 55 does not show it.
- **Finding 2, the Summary (cell 66), and the "start at 0" part of the README:** "Every photometry series starts at time 0", and the TTL2 description "raw photometry channel ttl2". Neither is printed (the first is stated only in the `ctd.py` docstring). Cell 7 shows only the start on the event clock (−251.3 to −3.6 s).
- **Cells 8 and 66:** the misstated JF-FP files are sampled at "about 120.3 Hz". Cell 7 prints a mean of 120.41 Hz and a median of 120.41 Hz (range 120.29 to 120.53). Finding 3's "120.3 to 120.5" is correct.
- **Cell 66:** "blocks of 8 long-ITI and 8 short-ITI sessions (then 7 or 8 long)". Cell 5 shows the first long block is 7 sessions for dLight-ramp2 F2, F4 and M2. Cell 6 and the record's notes have this right.
- **Cell 50 and fig2f notes:** reading (b) "p = 0.0075". Cell 49 prints p = 0.007. This is precision beyond the printed output, not a contradiction.
- **fig4d notes:** "p 0.11 to 0.14". Cell 24 prints 0.113 to 0.133.
- **fig4b notes:** "Both corrections ... session mean ΔF/F is zero (median 2e-08, largest 0.003)". Cell 20 prints this for the fit reading only.

Everything else I checked agrees with the printed outputs: every other "**Result:**" sentence, the Summary, the README table, and the notes.

Round-1 reasons in the record: they are stated faithfully and in my terms. Problems 1 to 8 and the could-not-check items are spread across the claims they apply to. One item is not carried over: my could-not-check point about an alternative fig4b baseline (a pre-cue window).

**3. Round-1 points**

Resolved:
- **1:** Fig 3 was run on (b1); it gives 7 and 6.
- **2:** λ is now searched from −5 to 5 and σ up to 10,000, with a Nelder-Mead check from each optimum. fig5bc winners are unchanged, and fig5d stays in tolerance.
- **4:** cue-locked trace, 143 of 144 short sessions.
- **5:** the cell 48 text is corrected, and the extra reading is shown.
- **6:** the per-hex reading is added.
- **7:** all 144 VR-FP files are now opened.
- **8:** the ITI-from-reward reading is adopted.
- Could-not-check items resolved: there is no depositor ΔF/F, and `nom_rwd` is reward probability in percent.

Remaining, bearing on a conclusion:
- **fig4b long-ITI part and fig4d (problem 3).** This is disclosed but cannot be resolved. Mean ΔF/F is zero by construction, and the cue-locked pre-cue level (cell 9: about −0.0047 long, −0.006 to −0.008 short) is close to the late-ITI tonic value. Measured against a pre-cue baseline there would be essentially no dip. So the part of fig4b that "holds" rests on the claims file's zero baseline, not on the data.
- **The claims file's short-ITI test.** Reading "does not resolve" as "above ΔF/F 0" under session-wide centering may misread the paper; its most likely comparison is with the long-ITI late level. Under that comparison the short-ITI part still fails (−0.0067 against −0.0046), so the outcome stands.
- **fig3 and fig3cd fits at the edge of the search.** In cell 55, 5 of 10 winning Gaussian fits (a, min 1) sit at σ = 10,000, where the profile is effectively quadratic. Under min 5, IM-1532's winning power-law sits at k = 1e-6 with A = 2e4, and IM-1292 has A = −2.6e11. The Gaussian "wins" therefore partly measure a quadratic against nearly linear shapes. This does not change either partial outcome.

**4. Critical findings**

- **Finding 1 (duplicate recordings): shown, and `critical` is right.** Cell 9 shows identical 470 hashes, sample counts (381,921 and 330,189), cue counts and lick counts for F2 Day3/Day4 and F4 Day5/Day6. Cue and lick identity is shown only through the counts, because the hash_cues print leaves these pairs out. Cell 5 is consistent with Day4 and Day6 having no other recording. One recording deposited as two, labelled as different days, is critical by definition.
- **Finding 2 (separate clocks): shown in substance, and `critical` is right.** Cell 7 shows TTL2 edges fitting cue times within 0.094 s, and the photometry starting 3.6 to 251.3 s before the event-log zero. As noted in section 2, "starts at time 0" and the TTL2 description are not printed. Signals on different clocks with no stated link are critical. The 64 files with the wrong rate (finding 3) would make the problem visible, but the other 292 sessions would not.
