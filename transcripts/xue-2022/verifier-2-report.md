**Round 2 verifier report: 000223-xue-2022-01 (Xue et al. 2022, DANDI:000223 v0.260528.0906)**

The claims file has 13 claims and the attempt record has 13 outcomes. The main problem in this round is that the re-executed notebook prints different numbers from the ones in the conclusions, the Summary, the README and the record's notes. The text appears to describe an earlier run. This changes one outcome's stated basis (fig5d). The other outcomes still hold on the printed numbers, but many of the quoted values are wrong.

## 1. Outcomes and assumptions

| claim | record outcome | agree? |
|---|---|---|
| data-scale | reproduced | Yes (cell 11). |
| table1-best-r | partially_reproduced, assumed | Yes: 18 of 20 match (cell 14). The assumption (ties in the row-to-file mapping broken by spike contrast) is stated and reasonable. The outcome does not depend on it: swapping 2748/2765 gives 17 of 20, swapping the 3112 pair gives 16, both still in the 15 to 19 band. So "resting on an assumption" overstates it. |
| fig1e-best-r-gap | reproduced | Yes: 7 of 20 (cell 18). |
| table1-optimal-thresholds | partially_reproduced | Yes: 15 of 19 under the Methods reading and 17 under the code reading, in every region (cell 28). |
| mean-max-fscore | partially_reproduced | Yes. Methods SD is 0.119 to 0.120, outside 0.136 ± 0.0136 (cell 33). |
| acceptance-9-of-20 | partially_reproduced | Yes, but the band is reached differently from what the record says. Reading (a), region 0 gives 6 accepted and 17 agreeing, because row 12 is rejected at 0.584 against a test threshold of 0.588. Regions 1 and 2 give 7 and 18 (cell 24). Reading (b) gives 6/7/6 accepted and 17/18/17 agreeing (cell 36). All of these are in the 17 to 19 band. |
| best-r-accepted-vs-rejected | partially_reproduced | Yes. Region 0, reading (a): accepted mean 0.628, rejected 0.354, both within tolerance; U = 6, not 12 ± 1.2 (cell 39). |
| best-r-not-predictive | partially_reproduced | Yes (cell 42). |
| fig5a-rejection-scenarios | reproduced | Yes (cell 45). |
| fig5a-threshold-order | reproduced | Yes (cell 45). |
| table1-network-measures | not_reproduced | Yes. OUT/IN matches 7 of 19 at best, against the 10 the criterion needs (cell 48). |
| fig5c-spike-contrast-vs-fscore | reproduced | Yes. R is -0.712 to -0.768, all within tolerance, with P at most 0.0006 (cell 52). |
| fig5d-out-in-vs-fscore | partially_reproduced, assumed | I now agree with the outcome, but not with the assumption it is said to rest on (see below). |

**fig5d in detail.** In cell 52, the Methods classification gives R = 0.571 (region 0), 0.594 (region 1) and 0.577 (region 2) over 20 rows, and 0.574, 0.598 and 0.580 over 19. All six are below the 0.605 lower bound. Only the code classification falls inside (0.612 to 0.621 over 20 rows).

- The outcome therefore no longer depends on the noise region. The region-0 assumption decides nothing and should be removed.
- What the outcome does rest on is the claims file's ranking of the Methods classification as the main reading. That ranking is prescribed by the claims file, not assumed by the attempt.
- My round-1 disagreement rested on region 1 being inside tolerance (0.615). That no longer holds, so I withdraw it.
- The criterion defines only "reproduced". "Partially" is a reasonable judgment because the correlation is positive and significant under every combination (R 0.571 to 0.741, P at most 0.0102).

## 2. Sentences the printed outputs do not support

**Cell 16 (table1-best-r)**
- "The code's default pair (97, pc) matches 14 of 20." Cell 14 prints 15 of 20. The same error is in the record's table1-best-r notes and in the p_thresh finding.
- "with subjects 2748 and 2765 the other way round, rows 16 and 20 would both miss". This is true, but row 16 already misses, so the count only drops to 17.

**Cell 31 (table1-optimal-thresholds)**
- "about 0.06 to 0.13 for rows 1 to 5". Row 3 in region 1 is 0.142. The same error is in the record.
- The record says "max F changes by at most 0.002" without the empty unit. Under the code classification row 18 changes by 0.003 (cell 30).

**Cell 34 (mean-max-fscore)**
- "SD 0.121 … (0.120 to 0.121)" and "code … mean 0.666 and SD 0.133". Cell 33 prints 0.120 for region 0, 0.119 to 0.120 over regions, and 0.665 / 0.132 for the code reading. The same errors are in the record's measured value (0.121) and notes. The outcome is unchanged.

**Cell 37 (acceptance-9-of-20)**
- "7 spines are accepted with each region, and 18 decisions agree". Region 0 gives 6 and 17.
- "Row 3 has the Table 1 best-R (0.222) but a test threshold of 0.251". The carried-forward best-R is 0.214 and the test threshold is 0.265 to 0.270 (cells 24 and 26).
- "its test-Rs … reach 0.247 to 0.256 at Table 1's Q_test". Cell 26 prints 0.265 to 0.270.
- "With the optimal quantiles found here, 7, 7 and 6 are accepted (18, 18 and 17 agree)". Cell 36 prints 6, 7, 6 and 17, 18, 17.
- "The stored release probabilities and a Bernoulli draw per spike give the same 7 accepted". Cell 25 prints 6 accepted and 17 agreeing for both.
- The record repeats all of these. Its measured value of 7 should be 6 for region 0.

**Cell 40 (best-r-accepted-vs-rejected)**
- "(7 accepted, 13 rejected, reading (a), any noise region) … 0.622 ± 0.081 against 0.337 ± 0.137 … U = 5 … two-sided p = 0.0015". This mixes regions. Region 0 is 6/14, 0.628 against 0.354, U = 6, p = 0.0015. Regions 1 and 2 are U = 5 with p = 0.0005, and the rejected mean there is 0.336.
- The record's "one-sided p = 0.0008" belongs to region 0, and its "p = 0.0093" for reading (b) region 2 is printed as 0.0064.
- The measured values [0.622, 0.337, 5] do not correspond to region 0.

**Cell 46 (fig5a-rejection-scenarios)**
- "with Table 1's quantiles and region 0, 5 below the test threshold only". Cell 45 prints 6. The record's measured [5, 4, 4] should be [6, 4, 4].

**Cell 50 (table1-network-measures)**
- "OUT/IN matches for at most 6 of 19 … both measures match for 6". Cell 48 prints 7 (rows 1, 2, 3, 9, 14, 15 and 19).
- "the code's lowess smoothing … changes it by at most 0.35 (row 3); each still matches 6 of 19". Cell 49 prints a largest change of 0.274 (row 3), and 7, 7 and 6 matches.
- The same errors are in the record's notes. The outcome is still not_reproduced.

**Cell 54 (fig5c and fig5d)**
- "R = -0.724 (P = 0.0003) … -0.724 to -0.781". Cell 52 prints -0.712 (P = 0.0004), with a range of -0.712 to -0.768.
- "OUT/IN … R = 0.592 (P = 0.006; 0.598 over 19 recordings)". Cell 52 prints 0.571 (P = 0.0086) and 0.574 (P = 0.010).
- "Region 1 gives 0.615 and the code's classification 0.646 … R is 0.592 to 0.759 … P below 0.05". Cell 52 prints 0.594 for region 1, 0.612 to 0.621 for the code classification, and a range of 0.571 to 0.741.
- The record repeats all of these:
  - fig5c measured -0.724 and "P at most 0.0004";
  - fig5d measured 0.592, its deviation, and "R 0.592 to 0.759, P at most 0.007";
  - the noise-region finding ("region 0 gives R = 0.592 and region 1 gives 0.615").
- The noise-region finding's statement that the regions disagree only on fig5d is also wrong. On the printed numbers they agree on every outcome.

**Summary (cell 55)**
- "merging every chain … leaves the OUT/IN matches at 6 of 19". Cell 49 prints 7.
- "fig5d … (assumption: noise region)" and "region 0 … is used where a choice matters". On the printed outputs no outcome depends on the region.

**README**
- The fig5d row says "(assumption)", which is wrong for the same reason. The table1-best-r "(assumption)" tag overstates, as noted in section 1.

**Round-1 reasons in the record.** They state my reasons faithfully and in my terms, including problems 1 to 7 and the requests from part C. One detail: they correctly record agrees: false for fig5d.

**Why the numbers differ.** The helper seeds every draw, and several printed values have moved since round 1 (row 3's carried-forward best-R, the acceptance counts, the Spearman R values). The record does not say what changed between the run the text describes and this re-execution. That should be explained, and all the text regenerated from the printed outputs.

## 3. Round-1 points

**Resolved**
- **1 (misidentified share):** reported in cell 30 (0.064 to 0.441), tied to max F and to the gap between the two readings, and put to the authors as a finding.
- **2 (carried-forward reading):** disclosed in cell 16 and the record.
- **3 (empty units):** measured; max F changes by at most 0.003.
- **4 (burst merging):** counted and its effect on OUT/IN measured (cell 49), and recorded as a code_mismatch finding.
- **5 (circular spike-contrast match):** disclosed in cell 50.
- **6 (rows 9 and 10):** second-best units printed, and row 10 with row 9's noise estimate gives row 9's thresholds (cell 26).
- **7 (OUT/IN variant):** disclosed.
- **Part C requests:**
  - elephant version printed (1.2.1);
  - GT-R and test-R distributions for rows 3 and 16 printed;
  - figure of the background squares added.

**Remaining, bearing on conclusions**
- **Stale text.** Section 2 lists every sentence that disagrees with the printed outputs, plus the unexplained change between runs. It touches the measured values and notes of acceptance-9-of-20, best-r-accepted-vs-rejected, fig5a-rejection-scenarios, table1-network-measures, fig5c and fig5d, and two findings. No outcome category changes, but the fig5d basis and the noise-region finding are wrong as written.
- **fig5d assumption.** The `assumed: true` flag and the region-0 deviation should go. The outcome rests on the claims file's main (Methods) classification, under which R is outside tolerance in every region.

**Remaining, not bearing on conclusions**
- **Row 10 background squares.** In the cell 22 figure, regions 0 and 2 of row 10 sit on bright processes. Their noise SD is 126 and 96, against 39 for region 1 (cell 21). This contradicts the rule's aim of squares "without visible cell structure". Row 10's decision is the same in every region.
- **Claims file.** I found no misreading of the paper.
