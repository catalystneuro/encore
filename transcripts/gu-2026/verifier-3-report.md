**Round 3 verifier report: Gu et al. 2026 on DANDI:001836 (0.261030.0428)**

I took the counts from the attempt record. It has 29 outcomes, and only one carries a `proposed` change: fig3d-distant-vs-inbound, from partially_reproduced to not_reproduced. No other claim has a `proposed` key, so that is the only claim reviewed here.

| Claim | Proposed outcome | Agree? | My outcome if different | Reason |
|---|---|---|---|---|
| fig3d-distant-vs-inbound | not_reproduced | Yes | — | See below. |

**The numbers come from the data**

- **Cell 42, which decoder made which table:** all 353 pairs of arm-restricted tables that share samples agree on 1.0000 of those samples. Of 162 comparable pairs of whole-track tables, 157 have exactly one member that agrees with the arm-restricted tables at 0.99 or more. So "decoder A" is identified from the files, as the record says. The inbound rows come from arm-restricted tables, so they are decoder A.
- **Cell 56, decoder A, first draw:** p_greater is 2.4e-8 (M), 0.053 (E), 0.064 (J), 1.4e-16 (K) and 9.1e-9 (L). That is 3 rats at p < 0.05.
- **Cell 56, adding rows from the tables that match neither trigger:** with only the rows within 20 ms of a COM time, E has 0.090 and J 0.20. With all their rows, E has 0.16 and J 0.23. Each gives 3 rats at p < 0.05.
- **Cell 56, within-arm measure on both sides:** E has 0.90 and J 0.13, so 3 rats at p < 0.05.
- **Cell 57, the 20 further draws:**
  - Decoder A with only the COM-classed tables meets the partial bar in 13 of 20 draws and the full bar in none.
  - Either addition of the unmatched tables meets the partial bar in 0 of 20.
  - The within-arm measure meets it in 3 of 20.
  - The smaller bound meets it in 17 of 20.
- Every figure in the proposed reason matches these outputs, and its cell references (56, 57) are correct.

**The choice it rests on was not made to reach the result**

- Decoder A was identified in answer to my round-2 point 2, before its result was known. It is the only decoder that pairs the COM decodes with the decoder of the deposited inbound rows, and the record says the code takes all the decodes of a figure from one decoder.
- I agreed with the "smaller bound" in round 2, but it is not a single decoder: it is picked per event (cell 52 `bounds`). So it has no claim to precedence over A.
- The first draw is the same seed as before, not a new choice.

**The criterion is applied as written**

- The partial bar is "p < 0.05 in at least four rats". Under the one-decoder reading that pairs the COM and inbound decodes correctly, the first draw gives 3 rats.
- Every way of using all of the paper's COM tables, including the conservative one that adds only rows at this entry's own COM times, gives 0 of 20 draws.
- The criterion's "same measure" reading gives 3 of 20 draws.
- The one remaining deviation favours COM. The legend of Figure 3D (paper, lines 644–646) uses "2D maze distance" for both sides, but the deposited inbound tables are restricted to the arm, which caps the inbound distances. Even with that bias towards COM, the bar is not met.

**Caveats, which do not change my outcome**

1. The result is borderline. Under decoder A with only the COM-classed tables, the median fourth-smallest p over the 20 draws is 0.044, and 13 of 20 draws pass (cell 57). The outcome rests on the first draw and on counting the unmatched tables as COM tables. That second step is reasonable but not proven: those tables could come from a parameter set the paper did not use for Figure 3D.
2. Rat J, one of the two failing rats, has only 26 COM events against 105 in fig3b. That points to how this attempt classified the tables, so a failure of the attempt rather than of the paper is possible. Adding J's unmatched rows (47 to 52 events) makes J's p larger, not smaller.
3. That decoder A is the paper's run_time decoder is likely but not shown by the files, as the record says.

**Whether the claims file misreads the paper:** I found no misreading. The paper reports "p<0.0001 for all rats but E" (line 646), and the criterion requires p < 0.0001 in at least four rats.
