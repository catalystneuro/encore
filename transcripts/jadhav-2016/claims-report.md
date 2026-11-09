I wrote the claims file at `claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml`. The quote checker passes except for 3 p-values, which are printed correctly in the paper but garbled in the extracted text.

**What I read.** The version of record with its full Supplemental Information, as text extracted from the journal PDF under `paper/`: Results, Discussion, Experimental Procedures, the legends of Figures 1 to 8 and S1 to S7, Tables S1 to S3, and the Supplemental Experimental Procedures. The paper links no code; it only says the analysis used custom Matlab routines. I could not render the PDF (no renderer is installed), so no value was read from a figure, and values shown only in figures are not recorded. The main one is the ensemble-size groups of Figure 6E.

**Counts.** 39 claims, all 39 with quotes, 25 with statistics (61 statistical values in all), and 39 with criteria. The 3 values the checker could not find are p < 10^-11, p < 10^-7 and p < 10^-7. The extracted text prints their minus signs as a replacement character; I confirmed each by reading it in context.

**Scope of the dataset.** By its description, hc-28 holds only the three W-track rats (HPa, HPb, HPc). Most results pool these with three Y-track rats that are not in the dataset. The opening comment fixes a rule for those claims: the direction and test must hold on the W-track data, and a pooled value outside its tolerance makes the claim partial. Where the paper gives W-track numbers (Tables S1 and S2, Figure S2, Figure 8), those are the expected values. Two claims need the Y-track rats and are recorded as untestable: Y-track learning and the both-tracks results of Figure S7. The dataset also holds later novel/familiar sessions used by a 2017 paper; the author is to keep only the 8 learning days.

**Details the paper leaves open, with the readings named:**
- **SWR detection:** the paper defers to Karlsson and Frank (2009), which is not under `paper/` and was not read. Readings are a threshold crossing on any one CA1 tetrode, or on the power averaged over tetrodes. Minimum duration and the definition of onset are not given.
- **Unit of analysis:** a cell on one day (the reading the paper supports best) or a unique unit across days. The span of the SWR-aligned raster is ±500 ms or ±1 s. PSTH bin and jitter range are given standard choices.
- **Peak and trough search window:** 0 to 200 ms or 0 to 500 ms. For onset, the mean and SD come from the baseline or from the whole PSTH. Return to baseline for the transient-response claim: within 1 SD of baseline, or within the 95% interval of the baseline bins.
- **Theta cross-covariance normalization:** a Poisson z-score, or division by the expected count. "Maximum zero lag" (Figure 5G) is the peak within ±200 ms or the value at zero lag. Same-tetrode pairs are shown both included and excluded.
- **SWR correlation:** Pearson over all SWRs, or over the SWRs where both cells spiked; Spearman is a variant.
- **"SWR modulation index" (Figure 4C):** the measure divided by the mean shuffled measure, a z-score against the shuffles, or the raw measure.
- **Theta phase:** convention and polarity of the reference tetrode. Theta lag: best mean kappa, or the median of each cell's best shift; shift range and step are a standard choice.
- **Mean rate "during movement":** speed above 5 cm/s with no SWR, speed above 4 cm/s, or the whole run epoch.
- **Rate-speed correlation:** over time bins (200 ms and 1 s) or over speed bins, plus the form of the shuffle for the median.
- **Spatial maps:** bin size, smoothing and speed filter are standard choices. Arm and direction indices use mean or peak rate. Matched subsample in Figure S5: all pairs in range, or subsampled to equal size.
- **Reward well and reward time:** zone radius 10, 15 or 20 cm. Reward time is arrival in the zone, or the first drop below 4 cm/s. W-track scoring and "chance": 50% correct, or a binomial test.
- **GLM:** the test of above-chance performance (signed-rank across cells, or per cell over the splits). Ensemble-size groups: tertiles or equal-width bins, since they are shown only in the figure.
- **Replay analysis:** how R is formed (Pearson or Spearman over events), and which replay score is used.

**Missing from the paper.**
- **"Data not shown":** the theta-lag result (about 15 ms) has no data or method beyond shifting the time of theta.
- **Pooled results:** most numbers have no W-track-only values.
- **Inconsistencies:**
  - The text calls the SWR-excited phase distribution narrower than both other groups, but reports p > 0.1 against SWR-inhibited. The statement follows the tests.
  - Figure 5F gives p < 0.001 in the text and p < 0.01 in the legend. The criterion uses p < 0.01.
