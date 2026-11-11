I wrote `claims/bittner-2017.yaml`. The quote checker reports 26 claims, 26 quotes and 0 problems. Nothing is committed.

**Text read:** the version of record, PMC5560553 (open access, Europe PMC full-text XML). That covers the main text, Methods and figure legends, plus the legends of S1 to S6 Fig. The supplement has nothing beyond those legends. There was no PDF, so I read no figure.

**Code read:**
- **Network code:** `sbittner12/litwin-kumar_doiron_cluster_2012` at commit `4382893`. It holds the clustered network only. It adds a stimulus in the last 500 ms, and its same-cluster E-E weight is 0.0448 where the Methods give 0.0456.
- **Classification code:** `adam-neuro/waveformClassification` at commit `062762678`. It fixes the three waveform features, the training on the top 75% of neurons by SNR within each file, a waveform-shape exclusion and its SNR formula.
- **Factor analysis code:** the paper links none.

**Claims:**
- **Totals:** 26 claims (1 is a link check that identifies the arrays), all with quotes, 26 with criteria, 0 with `statistics`. The paper reports no statistical tests.
- **Data:** 17 claims are on the model networks (`data: elsewhere`, rerun from the network code). 7 are on V1 recordings in the dataset. 2 compare the dataset with the models (`with_inputs`).
- **Tolerances:** 9 claims carry expected values. Where the ± is a standard error I used it as the tolerance; where it is a spread over neurons or samplings, I used 10%. Correlations printed near zero are judged as an absolute value below 0.01; I set that threshold, with the reason given.

**Details the paper leaves open, and the readings named:**
- **Which arrays:** the dataset holds 6 spontaneous arrays; the paper used 4, from 3 monkeys. They are identified by the paper's median SNRs.
- **SNR definition:** (a) the dataset's SNR field, or (b) the code's amplitude over twice the standard deviation.
- **Classifier training:** (a) top 75% by SNR within each array (the code), or (b) pooled across arrays (the Methods). The excluded waveforms are either (a) the code's shape-correlation rule or (b) the Methods' four neurons excluded by inspection.
- **Which 1,200 trials:** the first 1,200, or 1,200 drawn at random.
- **Sampling grids:** neuron-count and trial-count grids for Fig 3 and Fig 7 are not given. I used standard grids.
- **Factor analysis:** the grid of candidate dimensions (I used every value from 0 to n−1) and how trials are assigned to the four folds (contiguous or random; both run).
- **Simulations:** duration, whether the 20,000-trial sets overlap, the transient discarded, and the network seed.
- **Fig 6:** how many blind samplings were drawn, and on which trial sets.
- **Undefined words:** "saturate", "plateau", "nearly zero", "mostly independent" and "nearly all same sign" have no thresholds in the paper. I set explicit ones and say so in each criterion.
- **Conflicting numbers in the paper:**
  - The blind-sampling spreads differ between two paragraphs (1.8 and 2.0, 1.4 and 2.3, 5.3 and 5.2).
  - The non-clustered E-E correlation spread is printed as 0.11 in the Fig 1D legend and 0.011 in the S2 Fig legend.

  In each case both values are named as readings.
- **Mislabels in the paper:** the Fig 7 legend letters A to D while the Results cite 7A to 7F. The Methods and Discussion cite Fig 6 where Fig 7 is meant.

**Missing, which claims need:**
- **Waveforms:** the dataset's description lists no average waveforms. Without them the classification, and every V1 claim that depends on it, cannot be redone. The author should check; if there are none, `v1-classification-counts` is blocked as data missing.
- **Simulations and factor analysis code:** the simulations are not deposited, the factor analysis code is not linked, and the non-clustered network must be built from the Methods.
- **Fig 7 readings:** with no PDF, the values in the Fig 7 panels could not be read.
