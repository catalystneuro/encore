I checked `claims/peron-2020.yaml` and made nine corrections; it is ready for an attempt.

**Checker result line:** `claims/peron-2020.yaml: 31 claims, 30 quotes, 33 statistical values, 7 problems`. All quotes match the text. The 7 "problems" are P values that appear only inside figures, which the text extraction drops. I read all seven in the PDF and they are correct: Ext. Data Fig. 5, P = 0.098; Ext. Data Fig. 6, P = 0.863, 0.666, 0.065, 0.721, 0.710 and 0.620. From the PDF I also confirmed which pairs of ablation types the Fig. 2j and 2k P values compare, and the Ext. Data Table 1 averages the file quotes.

I cloned both code repositories at the commits the file names. Its descriptions of the analysis code are accurate: the 10 by 30 µm exclusion zone around ablated cells, the percentile rules, the counts that skip the shuffle test, the per-mouse means in the distance analysis, and the bug that drops the left-trial responses in the similarity measure.

**Changes, by claim**
- **Opening comment:** the paper tuned the model's input to match recordings from its ref. 7 (Peron et al. 2015), not to this paper's own data. I said so and added a third reading for that tuning: the 17% fraction the Methods take from ref. 7.
- **model-amplification-increases:** the test across connectivity steps of 0.05 was invented. Input strengths between 0.2 and 0.4 are interpolated from the two end points, so the claim now just requires a lower matched input at 0.4 than at 0.2.
- **model-all-or-none-robust:** removed an invented "may not fall by more than half" threshold. Those numbers are now reported instead.
- **model-slow-input-sensitive:** added the equal-connectivity (0.2) case, which the Ext. Data Fig. 8 title and the Methods include.
- **model-response-similarity, response-similarity-example, -touch-ablation, -whisking-ablation:**
  - The Methods and the Fig. 3e legend fit each slope to the individual neurons.
  - The code fits it to the binned means instead.
  - Following the protocol, the Methods fit is now the main test and the code's fit a variant. Before, they counted as equal readings.
- **touch-ablation-whisking-unchanged:** dropped "materially"; the paper only reports the counts.
- **ablation-type-specificity:** "changed Rtouch more" became "significantly different changes", which is the paper's wording.
- **per-mouse-table:** removed the invented "20 of 24 rows" rule. Every row must now match, and the number of matching rows is reported.

**Still open**
- **Tolerances:** the file uses 10% of each value, not the spread across mice the paper gives. Its stated reason is sound, but the protocol's default is the stated spread.
- **Model settings:** the paper does not give the input strengths, the reset-pulse strength at connectivity 0.44, or the slow-input strength. The model claims rest on the readings named for these.
- **Neuron counts:** the counts in the Results (901 touch neurons; 932 before touch ablation) are higher than Ext. Data Table 1's (about 780 and 788 on average). The paper does not say which counting rule each uses, so both readings stay.

Nothing was committed or pushed.
