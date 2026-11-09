**Round 2 verifier report: Gu et al. 2026 on DANDI:001836 (0.261030.0428)**

The claims file has 29 claims. The attempt record has 29 outcomes:
- 6 reproduced, all from the behavioural set;
- 5 partially reproduced: fig1d-switch-bias-declines and the 4 Figure 3 claims;
- 2 not reproduced;
- 1 reproduced with `assumed: true`: figs7b-no-swr;
- 15 blocked as too_large.

fig3d-distant-vs-inbound is partially reproduced and also has `assumed: true`. In round 1, 20 claims were blocked. In round 2, 5 of them are tested: fig3b ×2, fig3c, fig3d and figs7b.

## 1. Outcomes

| Claim | Agree? | Comment |
|---|---|---|
| fig1c, fig1e, fig1d ×2, figs1f, fig1g ×2, fig1h ×2 (9) | Yes | The numbers match the criteria (cells 12–36). For fig1h-less-switching, the "+1 to both counts" variant gives 3 rats at p < 0.01 (E has p = 0.0101). The record correctly does not let this override the criterion's rule that undefined days are dropped. |
| fig3b-extended-before-stopping, partial | Yes | Cell 41: COM is greater at p < 0.01 in M, J, K and L. E has p = 0.053. Only reading (b)(i) can be run, as stated. |
| fig3b-distance-predicts-com, partial | Yes, but borderline | Cell 44, reading (b): 1.079 is within tolerance and p = 2.65e-20, a factor of 2.6 short of the 1e-20 bar. The control arm ranges come from a single random draw (one fixed seed per day), so the outcome may depend on the seed (see §3). |
| fig3c-distant-after-stopping, partial | Yes, with a reservation | Cell 47: 4 of 5 rats pass under both decode bounds. J fails with only 26 events. That number depends on excluding the "other" tables (see §3). |
| fig3d-distant-vs-inbound, partial (`assumed: true`) | Yes | The assumption is stated: of the two decodes, keep the smaller. As a conservative choice it is reasonable. Two caveats: (i) "smaller/larger" is picked per event, so neither bound is a single decoder. (ii) The decoder could probably be identified (see §3). |
| figs7b-no-swr, reproduced (`assumed: true`) | Yes, under the criterion's reading (iii) | Cell 57: in all four window × reference combinations, the COM coefficient is < 0 and both end coefficients are > 0, each at p < 0.05. The three assumptions are stated and are reasonable given the files: all tetrodes, the `ref_elect_id` reference, and a sampled baseline. The result is fragile: see §3. |
| 15 claims blocked as too_large | Yes | The posterior, state probabilities and events are not deposited. The triggered tables hold only MAP windows. |

I found no new place where the claims file misreads the paper. One deviation, though: the fig3d criterion asks for "the same measure" on inbound trials. The attempt instead compares the whole-track maze distance (COM) with a within-arm distance taken from arm-restricted tables (inbound). It says the code does the same, which I cannot check. This favours COM (see §3).

## 2. Sentences the printed numbers do not support

- **Cell 42, and the fig3b-extended notes:** "Without matching the arm range the control distances are larger (p = 0.85 to 1.0)". Cell 41 prints `p_greater_unmatched` as 1.0 for all five rats.
- **Cell 48:** "p from 4e-12 to 8e-32 for the smaller bound". Rat K is 1.827e-11, which is outside that range. The attempt-record notes give the values correctly.
- **Cell 51:** "since the tables hold only the 5 s after the poke, when the rat is mostly still at the well". No output shows where the rat is. This is a conjecture.
- **Cell 58:** "The values are smaller than the paper's". The z-scored COM coefficient is −0.22, larger in magnitude than the paper's −0.18.
- **Attempt record, fig1e notes:** "rats K and L have the 8 and 6 days of Figure 1C (319 to 456 trials a day)". Cell 15 shows L at 265–337. Only K is 319–456.
- **Attempt record, fig4e-next-choice notes:** "at the 60 MB/s the notebook measures on an LFP file would take about 2.4 days". Cell 60 prints 42 MB/s, which gives about 3.4 days.
- **Cell 0, and the record's first data_missing finding:** "12.7 TB of raw voltage". Cell 60 gives 12.5 TB for the raw files. 12.73 TB is the whole dandiset (cell 1). Cell 59 and the fig4e notes correctly say 12.5.
- **README:** "The Figure 3 effects hold in four of the five rats." For fig3d under the kept (smaller) bound, only 3 rats reach the claim's p < 0.0001 (cell 50); 4 rats reach only p < 0.05. fig3b-distance is a pooled fit, not a per-rat result.
- **README:** "about 15 minutes … 5 for the triggered tables, and 4 for ripple detection". Cells 1, 39, 54 and 60 print 219 s, 365 s, 226 s and 1092 s in total, so about 18 minutes, with 6 for the triggered tables.
- **README:** "For Figure 1H the effect is in every rat". This is true only as a direction (initial > final). Rat M has p = 0.42 and fails both sign tests (cell 33).

All other sentences of the conclusions, the Summary, the README and the notes match the outputs.

**My round-1 reasons in the record:** they are faithful paraphrases, in my terms, including B-point references and the folded-in C items for fig1h and fig1e. One claim in the verification block cannot be checked from the outputs: that the B4 fix "left every count unchanged". No before/after output is printed.

## 3. Round-1 points

**Resolved:**
- **B1:** figs7b is now tested.
- **B3:** reading (b) now uses 0.1 × 96 cm.
- **B4:** in `detect_com`, the reversal must now end after the head passes the threshold.
- **B5:** sessions with fewer than 20 trials are dropped, and both thresholds are run in the matches-run-through test.
- **B6:** the triggered tables are identified and used.
- **B7:** the 1/3 chance level is reported.
- **B8:** no change was needed.
- **C items:** all were addressed.
- **B2:** resolved as far as the files allow. Rat M's missing sixth day explains its shortfall. For K and L the cause cannot be found in the files, and it is recorded as a finding.

**What remains that bears on a conclusion:**
1. **"Other" triggered tables are excluded without being looked into (fig3c, fig3d; partly fig3b).**
   - There are 146 such files. As a group, 44% of their rows fall within 20 ms of this entry's COM times (cell 39).
   - 81 of them belong to rat J, which is the failing rat in fig3c (26 events) and fails in fig3d (p = 0.06).
   - Matching them against other COM definitions, or keeping their COM-aligned rows, could change J and so the fig3c outcome.
2. **Which decoder made the fig3d tables was not checked.** The 142 arm-restricted COM tables covering both windows share the triggers of the whole-track pairs. Comparing decodes at shared samples would likely show which of the pair matches them. fig3d's outcome rests on this.
3. **fig3d compares unlike measures.** The inbound distance is capped within the arm, while the COM distance can reach other arms (up to 155 cm, cell 47). This favours a COM > inbound result.
4. **fig3b-distance is a single random draw.** p = 2.65e-20 against the 1e-20 bar, from one seed's draw of control arm ranges. Fits over several seeds would show whether "partial" is stable.
5. **figs7b is fragile:**
   - Adding the reference changes end-of-trial rates up to about 50-fold (L, unrewarded, window a: 0.197 → 0.004 per s).
   - With the reference, M, E, J and L have end rates of 0.008 per s or less in window a. So that combination is driven largely by rat K: it has no reference channel, the weakest theta–speed coupling (−0.06 to 0.18), and per the claims file some CA3 tetrodes.
   - Reading (ii) fails with the reference.
   - The outcome holds under the criterion's reading (iii), but a fit leaving out rat K would show whether it still does.
