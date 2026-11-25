**Verifier report: kim-2026-learning, round 2 (DANDI:001868 v0.260715.2016)**

The claims file has 39 claims. The attempt record has 39 outcomes: 8 reproduced, 7 partially reproduced, 6 not reproduced and 18 blocked. I read the re-executed notebook's outputs and did not re-run it. Cell numbers below are those of this notebook; they have moved since round 1.

### 1. Outcomes

**figs3-modulation-all-cells: the record contradicts itself and the other documents.**
- The record's `outcome` field says `partially_reproduced`.
- Its notes ("so all three parts hold"), its round-1 response ("changed to reproduced"), cell 36, the Summary (cell 92) and the README all say reproduced, resting on an assumption.
- I agree with `partially_reproduced`, so the notebook, README and response should change, not the field. The claims criterion sets the population as "4 to 6 uA", and the attempt's own fig2a deviation reads the Methods' 4–6 µA limit as applying to the neural analyses. Under 4–6 µA the at-threshold modulation rises (p = 2.59e-05 and 4.96e-06, cell 35).
- One reading was not tried: taking the nearest of 4, 5 and 6 µA, so that a 3.x µA threshold maps to 4 µA instead of being dropped.

**fig4ij-pyramidal-drive (reproduced, assumed): the assumption is stated, but I am not convinced it is reasonable.**
- The criterion says trough-to-peak at 0.45 ms. Under that rule the pyramidal latency at 6 µA gives p = 0.0587, which makes the claim partial (cell 41).
- Calling the stored label "the authors' application" of the rule is not supported by the outputs. The paper's counts lie closer to the recomputed rule than to the stored label:
  - recorded units: 724/275 recomputed and 732/260 stored, against 672/301 (cell 31);
  - interneuron n: 63/228, 94/164, 92/76 recomputed and 55/221, 90/158, 90/76 stored, against 69/254, 113/180, 122/86 (cell 41).
- I would record it as partially reproduced, or as reading-dependent at most.

**fig4h-unit-counts (not reproduced):** I agree. It is marked `assumed: true`, but it fails under every pre-window and every cell-type variant, so the outcome does not rest on an assumption.

**Agreed, with each assumption stated and reasonable:**
- **reproduced:** fig2a, figs1e, figs5-movement-onset (assumed), fig5d, fig6f-npl-higher-coupling;
- **reproduced, seed-sensitive:** figs4de, fig6f-pl-coupling-increase;
- **not reproduced:** fig4g (assumed), figs4b, figs2ef, fig6d (assumed);
- **partially reproduced:** fig5e, fig5fg, fig5h, figs5-pre-movement-window (assumed), fig6c;
- **blocked:** all 18.

**Agreed, but the stated assumption is a judgement call:**
- **figs7-control-no-change (not reproduced):** taking the 3 tabled bursts is defensible. Cell 6, though, shows the spikes following untabled bursts in at least 4 sessions.
- **figs9-coupling-controls (partially reproduced):** part (C) rests on the same 3-burst choice, yet the outcome has no `assumed: true`. Under the 10-burst reading, NPL n is 19/24 at 5 µA (cell 67), so (C) might become testable. It was not run.

**Paper misreading in the claims file:** none found.

### 2. Sentences the printed numbers do not support

**Record notes on blocked claims:**
- fig2b: "the catch-trial pattern across samples is the same as at 6 uA". Cell 10 shows otherwise: the catch-trial −1 positions (3, 7) match 4 µA, while 6 µA has −1 at 0, 3 and 4.
- fig3b–figs6: "53 to 1019 ROIs per session", while cell 89 says "172 to 1019". Neither range is printed anywhere, and the two disagree.
- fig3b–figs6: "the per-session mean images … are not in the files". No output shows this, and the planar segmentation tables carry a `reference_images` column (cell 10).

**Finding 15:** "the wheel moves more on hits than on misses in every block". Cell 8 is per session, not per block, and it fails in three ICMS83 sessions: 2.715 vs 3.221, 1.521 vs 2.222, and 1.385 vs 2.577.

**Contact mapping (figs4b):**
- The record's "The mapping holds" and cell 51's "The contact mapping holds" overstate the check in cell 50.
- That check compares unit depth with the depth of each unit's own peak channel. It does not test whether the stimulation table's `stim_channel` numbers the same contacts as `channel_name`.
- ICMS92 has no units on a stimulation channel at all.

**Conclusion cells:**
- **Cell 74 and the fig6d notes:** "All five seeds give the same clusters." The NPL onsets (180/70 ms) are the same at every seed, but the clusters are not:
  - PL early onset is 330 ms under three seeds;
  - PL late has 1 cluster rather than 2 under four seeds;
  - NPL early has 2 to 4 clusters (cell 73).
  
  The conclusion is unaffected.
- **Cell 89:** "(172 to 1019 ROIs per session)" is not printed (see above).

**Summary (cell 92):**
- "against 5.5 to 6 ms elsewhere": ICMS83's trains start at 0.0 ms, and maxima reach 37.4 ms (cell 4).
- "the authors' trough-to-peak classification": no output shows this.

**README:**
- The figs3 row, "Reproduced (assumed)", disagrees with the record.
- "the activation tables and recordings of six passive controls": only four controls have recordings (cell 4).
- "about 25 minutes": the run printed 20.1 min.

All other "**Result:**" sentences and record notes match the printed numbers.

**My round-1 reasons:** the record restates them faithfully, and all 13 problems appear against the right claims.

### 3. Round-1 points

**Resolved:**
- 4: figs5-pre-movement-window now uses reading (ii).
- 7: wheel-threshold variants added.
- 8: the fig2a session-threshold fix; reading (a) is now within tolerance.
- 9: per-mouse tests for figs2ef.
- 10: each claim now uses its own seed.
- 11: the sign of r is documented.
- 12: a raw-count variant was added. My round-1 remark that smoothing can only move onsets earlier was wrong: the raw-mean early onset is 100 ms, against 180 ms smoothed.
- From section C: the volumetric description, the segmentation columns and psignifit's threshold parameter.

**Remaining, bearing on a conclusion:**
- **1 (pre-window):** the variants were added. The fig4g outcome rests on the 700 ms window, which is stated. No other claim was run with another window.
- **2 (PL share of about 80% against about 63%):** a blanking-edge artefact and false positives are ruled out (cell 17), but the cause is unknown. It shrinks the NPL samples in figs4de, figs5-pre-movement-window, fig6c, fig6d and figs7.
- **3 (control bursts):** the 10-burst variant flips figs7, and figs9(C) was not re-run under it.
- **5 (cell-type rule):** the label is now consistent across claims, but the choice against the criterion's trough-to-peak decides fig4ij (see 1).
- **6 (figs4b mapping):** the check does not test the `stim_channel` to `channel_name` correspondence. A scrambled mapping would also flatten the slopes.
- **13 (figs3 at threshold):** handled, but the result is the record/notebook contradiction in 1, and the nearest-of-4–6 µA reading is untried.

### 4. Critical findings

No finding in the record is rated `critical`.

One rating I would raise: finding 5 (control stimulation tables list 3 bursts, but the spikes respond every 0.5 s for 5 s; record rating `major`). I would rate it **critical**.
- Cell 6 shows untabled, stimulus-locked responses at 0.5 s slots 4 to 10 in four sessions:
  - ICMS45 2022-02-05 and 2022-03-04 (baseline about 1 spike/s, slots 31–34, gaps 4–6);
  - ICMS54 2022-05-20;
  - ICMS56 2022-06-21.
- In all but ICMS45 2022-02-05, the trial tables agree with the 3 bursts, so nothing in the metadata reveals the gap.
- An analysis that takes the tables as given decides figs7 differently from one that does not (cell 67).
