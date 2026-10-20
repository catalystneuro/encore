**Round 2 verification: Economo et al. 2018 on DANDI 000006 (0.220126.1855)**

The claims file has 9 claims, and the attempt record gives 9 outcomes: 4 blocked (data_missing), 3 reproduced, 1 partially_reproduced and 1 not_reproduced. I saved the public Nature article page as `paper/nature_page.html` and `paper/nature_page.txt`. Its Extended Data legends match what cell 36 quotes: 15 of 61 against 3 of 69, 64.4 ± 1.0% against 58.9 ± 0.6% with p = 1e-4, and rectified 0 of 69 with p = 9e-7. Its Data availability statement matches the attempt record.

**1. Do I agree with the stated outcomes?**

| Claim | Stated | Agree |
|---|---|---|
| pt-types-transcriptomic | blocked: data_missing | yes |
| pt-types-shared-targets | blocked: data_missing | yes |
| pt-upper-thalamus-projection | blocked: data_missing | yes |
| pt-lower-medulla-projection | blocked: data_missing | yes |
| pt-preparatory-activity | reproduced | yes. Cells 19–20: 72/100, p = 0.001. It also holds on one session per animal (26/36) and on the paper's 130 units (89/130). |
| pt-upper-early-preparatory | reproduced | yes. Cells 23–24: 27/44, p = 0.001. Also 8/20 and 40/61, each p = 0.001. |
| pt-upper-persistent | reproduced | yes. Cells 27–28: (a) p = 0.001; (b) cosine 0.495, p = 0.016. Both parts hold in every variant, and on the paper's units (b) gives p = 0.002. |
| pt-lower-late-and-motor | partially_reproduced | yes. Cells 31–32: (a) p = 0.0096, (b) p = 0.088. The same split appears on one session per animal and on the paper's 69 units. It is still threshold-dependent (see section 3). |
| pt-types-differ-in-timing | not_reproduced | yes, by the stated criterion. Cells 35–36: (a) p = 0.134 and (b) reversed, on the dandiset units, the paper's units and one session per animal. The paper's own Extended Data Fig. 9 measure supports part (a): 7/44 against 1/56, p = 0.012; 12/61 against 1/69, p = 0.0005. So the outcome rests on the criterion's reading of part (a). |

**2. Sentences the printed outputs do not support**

Almost every number in the Result cells (21, 25, 29, 33, 39), the Summary, the README and the record's notes matches the outputs. The exceptions:

- Attempt record, pt-types-differ-in-timing notes: "part (b) is reversed under every variant." Cell 31 contradicts this. The attempt's own variant reading of "motor commands" (response rate changed from baseline) gives PTlower 0.946 (53/56) against PTupper 0.841 (37/44). That is the claim's direction. From those counts I get a one-sided Fisher p of 0.080, which is not significant, but it is not reversed either. Cell 39's "none supports part (b)" is literally true, but it leaves out this variant.
- Cell 39: "The code's coding-direction comparison goes the way the abstract describes." The direction is right, but PTupper is higher in only 83 of 100 bootstraps (cell 37), which is not a significant difference. The sentence should say so.
- README: "The paper is not open access, so only its abstract was used." Cell 0 and the claims file header say the Extended Data legends 5–10 were also read, and variants use them. The deviations in the record still begin "Abstract only;" for the same reason.
- Attempt record inputs: "all 14 processed data files were read." No output prints a file count. Cell 13 prints only "150 tagged units in 64 sessions".
- Minor wording, consistent with the outputs: the finding text and the Summary say "trial starts are 6.4 s apart." That is the median. Cell 5 gives 5.4 to 7.9 s from the 1st to the 99th percentile.

**Are my round-1 reasons stated in my own words?** Yes, for all 9 results, and they are faithful. The cross-claim problems are folded into the pt-preparatory-activity reason, and the fragility, count and pooling points into pt-lower-late-and-motor. Two small omissions in the pt-types-differ-in-timing reason: the PTlower cosine shuffle p = 0.43, and the fact that problems 1–3 also bear on that claim. The "reviewed" field describes my round-1 materials accurately.

**3. Status of my round-1 points**

Resolved:
- **B1, unit counts.** Cell 13: the code's rule on the processed data gives 61/69. All 117 dandiset units get the same label, decision and reasons, and the gap is 11 sessions missing from the dandiset.
- **B2, repeated neurons across days.** Cells 16–17 and the variants: the one-session-per-animal variant gives the same outcomes. 44 of 100 units lie within 20 µm of a unit recorded on another day. Repeats cannot be ruled out, but they no longer decide any outcome.
- **B4, overlapping trials.** Unchanged, and still no outcome effect.
- **B5, unverified clock in 7 sessions.** Cell 13: 1149 of 1149 units equal the processed spike times. Cell 16 lists the 5 units in those sessions.
- **B6, spikes per trial.** It follows the paper's code (`alm.py:202`). Accepted.
- **B7, decoding leakage.** Fixed (`alm.py:280`). The median is 0.893.
- **B8, baseline fraction.** Left as stated, with no outcome effect.
- **B9, outcomes in the header.** Removed.
- **C: inclusion list, all-session clock check, per-unit p-values and the Extended Data Fig. 9 test.** All done.

Remaining, and bearing on a conclusion:
- **pt-lower-late-and-motor.** The partial outcome still flips with the selectivity threshold, on the dandiset units and on the paper's units alike. Part (a) on the paper's units is marginal (p = 0.049). The rise comes mostly from one animal (anm369962).
- **pt-types-differ-in-timing.** The not_reproduced outcome depends on reading "early" as the fraction with rank-sum p < 0.01. The paper's measure supports part (a). For part (b), the attempt's "motor commands" variant goes the claim's way (p ≈ 0.08), and the paper's evidence for PTlower motor signals appears to rest on movement-related population dynamics (Extended Data Fig. 10). So the reversal of part (b) shows that PTlower units are less often direction-selective in the response epoch. It does not show that they lack motor-command activity. The record's wording should reflect this.
- **Type and animal confounding.** Still unresolvable: each animal holds one type, 8 PTupper animals against 4 PTlower.
- **Extended Data Fig. 9 counts.** This attempt gets 12 of 61 and 1 of 69, where the legend gives 15 and 3, and nothing explains the difference. The means match (0.638 and 0.586 against 0.644 and 0.589), so it does not change any outcome.
