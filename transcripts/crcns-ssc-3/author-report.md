All 14 claims were tested and none is blocked. The entry passes `check`, ran clean under `entry.py all` in 28.8 minutes (limit 60), and the handover package is built. Nothing is committed.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| data-recordings | reproduced |
| fig4ac-te-lognormal | partially reproduced: the values do span orders of magnitude, but the log-normal fit to the distribution averaged over recordings has R² 0.08 to 0.61, below the required 0.9 |
| fig4bd-heavy-tailed-degree | reproduced |
| fig4bd-out-tail-longer | reproduced, rests on an assumption (sub-networks) |
| fig5a-in-degree-uncorrelated | partially reproduced, rests on an assumption (sub-networks, Pearson): the negative skew is significant, 41 of 50 negative |
| fig5b-out-degree-positive | reproduced, rests on an assumption (sub-networks): 44 of 50 positive |
| fig5ab-correlations-beyond-null | reproduced, rests on an assumption (sub-networks) |
| fig5cd-pooled-trends | not reproduced: the out-degree rise is not significant at both time scales, and synergy falls steeply with in-degree |
| fig6-information-gain-not-rising | reproduced: all exponents negative, though none of the intervals overlaps zero as the paper says one does |
| table1-pid-examples | reproduced |
| fig7b-connectivity-patterns | reproduced |
| fig7c-degree-modified-rule-matches | partially reproduced, rests on an assumption (sub-networks, Pearson): the firing-rate rule fits the data more closely than the degree rule |
| fig7d-degree-rule-highest-conditioned-mi | not reproduced: the random model has the highest conditioned MI and the degree rule the lowest |
| figs1-larger-model | not reproduced |

**2. Dataset, assumptions and questions**

- **Dataset:** the files match the paper: 25 recordings, 7735 neurons all with at least 100 spikes, 2.10 Hz mean rate, spike times on the 20 kHz grid, and no recording deposited twice.
  - DataSet19 lasts 48 min, not 60, and the first ten recordings have no spikes in their first 8 s.
  - The paper's TE networks (taken from its reference [44], Timme et al. 2014) are not deposited, so I rebuilt them from the spike times.
- **Version:** CRCNS does not version data sets, so it is recorded as `unversioned`, with the MD5 of `data.tar.gz`. The notebook checks the streamed bytes against that sum. The paper cites the DOI with no version, and the bucket holds only `live/`.
- **Method sources:** the flattened paper text had lost every equation (Eqs 1 to 24), so I read them from the version of record's XML on Europe PMC. The TE details (1.6 and 3.5 ms bins, a 7-bin jitter, the sub-network procedure) come from [44]. Both are listed under `inputs`.
- **Assumptions:**
  - The past state of each neuron is the OR of bins t-2 and t-3. That matches the delay windows both papers state; [44]'s own text implies bins t-1 and t-2.
  - The degree and synergy analyses use the 500 sub-networks per recording, not the full networks.
  - Correlations are Pearson. Every other reading is shown in the notebook.
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings):
  - Which bins form the TE past state?
  - Were Fig 4 and Fig 5 computed on the sub-networks or the full networks, and with Pearson or Spearman correlations?
  - Fig 5 says N data = 40, but 25 recordings at two time scales give 50 correlations. Which 40?
  - How was the model's synergy computed, given that its runs have no past to condition on?
- **Questions to a reader:** none.

**3. Where the protocol was unclear, wrong or missing something**

1. The paper text under `paper/` had no equations and the claims file said the model claims needed them. The protocol does not say whether fetching the version of record counts as "the paper". I fetched it and recorded it as an input.
2. The method lives in a cited earlier paper ([44]), not in this paper or any linked code. Step 1.6 only mentions "the methods it cites" for assumptions. I took the details from [44], cited the passages, and listed it under inputs.
3. The protocol has no way to approximate a method that is too expensive to run in full. The paper's 5000 jittered surrogates per pair, run exactly, would take more than an hour. For pairs whose jitter moves more than 50 relevant spikes, I drew the surrogate counts from a normal distribution with their exact moments. On two recordings the significant connections agree 99.5% with the full jitter. Recorded as a deviation.
4. The "Time" rule covers the run's deadline but not the notebook's 60-minute limit applying to a part of the method. I sampled at fixed sizes and recorded each as a deviation: full-network triples (3000 per recording and time scale), and for the information gain 30 receivers and up to 20 input combinations per n. The paper used every receiver and 100 combinations.
5. The clock check in step 2 assumes trial tables or other data streams. This data set has spike times only, so I stated that the check does not apply.
6. CRCNS has no versions, but the prompt asked for "a pinned published version". I followed archives.md (`unversioned` plus the MD5).
7. Conclusion cells are written after the run, but the executed copy must match the committed notebook. I inserted the same Result cells into the executed copy without re-running; they are markdown only, so no output changed.
8. When several readings match, the record keeps the first one listed. For the firing rate that gave 2.132 Hz (reading a) even though reading b gives 2.103 Hz, closer to the paper's 2.10.

**4. Runtime and what failed**

- The notebook runs in 28.8 minutes on 4 cores: about 14 for the TE networks, 8 for the sub-network and synergy analysis, 5 for the model.
- One development command (an early full TE pass) ran into its one-hour timeout and printed nothing because of output buffering. That cost about an hour of the run.
- After the executed run I made one edit to `hdn.py`, a docstring note only, so the code that ran is unchanged.
- Nothing else failed.

Files are in `entries/crcns-ssc-3-timme-2016/`:
- reproduce_timme_2016.ipynb
- hdn.py
- README.md

The record is `attempts/crcns-ssc-3-timme-2016-01.yaml`.
