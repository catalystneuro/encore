The entry is written, locked, checked (0 errors) and run from a clean environment. Both notebooks pass: `reproduce_asari_2009.ipynb` in 3 min and `strf_asari_2009.ipynb` in 21 min. The record is `attempts/asari-2009-02.yaml` and the handover is built. I did not come across any earlier attempt's results.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| methods-recording-counts | partially reproduced: 305 natural probes in 39 cells and 93 MGB probes in 14 cells match exactly; 132 A1 cells meet the rule against 123; voltage-clamp counts can't be tested |
| a1-mgb-firing-rates | partially reproduced, rests on an assumption (A1 spike detector) |
| fig2-example-reliability | reproduced (0.310 ± 0.098) |
| fig2-example-long-context | reproduced (2 matching probes) |
| fig3a-proportion-significant | reproduced (187 of 305, late fraction 0.251) |
| fig3a-significance-decay | partially reproduced |
| fig3b-fractional-power-decay | partially reproduced (size 0.47 matches; time constant 1.3–1.8 s against 1.04 s) |
| timescale-longer-than-membrane | reproduced (72 and 78 ms) |
| fig4-predictability-upper-bound | partially reproduced (bound 0.49–0.50 matches; time constant longer) |
| fig4-strf-performance-low | partially reproduced, rests on an assumption: performance is low, but the Wilcoxon test finds a small improvement with longer windows |
| fig5, fig6 | blocked: data_missing |
| fig8a, fig8b, fig8a-significance-fits, fig8c, fig8-natural-synthetic | blocked: metadata_insufficient |
| fig7-example-frequency-context | blocked: data_missing |
| fig9-mgb-fast-decay | reproduced (tau 0.058–0.080 s) |
| fig9-example-first-bin | reproduced |
| figs1-silence-probe | reproduced |

## 2. Dataset, assumptions, questions

**What was found about the dataset:**
- There are no voltage-clamp recordings at all.
- It holds 145 of the 194 A1 current-clamp cells and 14 of the 16 MGB cells. Every cell used in the natural-sound and MGB analyses is there.
- For the synthetic recordings, only 6 of 105 say which conditioning stimuli form the paper's five property groups (amplitude, frequency, AM, FM, higher-order). That is why the Figure 8 claims are blocked.
- No recording has the Figure 7 design.
- Summary.mat lists two cells in both the natural and the synthetic group.
- Four MGB cells come from an animal stored as 29 days old, outside the paper's 20–28 days; one cell has no age.
- Sequence numbers in some trigger descriptions don't match the numbering in the file notes; the fragment lists agree.
- The data set contains the authors' own analysis code (`CxtDep.m`). The paper doesn't mention it. I ported it, and it reproduces the paper's sample sizes exactly.

**Assumptions:**
- A1 spike detector: a peak at least 15 mV above the median-filtered trace, with 10 and 20 mV also shown. The paper detected A1 spikes by hand.
- STRF: the 16 of 25 Wehr cells that have the repeated trials Eq. 52 needs, plus the claims file's Wilcoxon test.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- How A1 spikes were detected, and which periods and recordings count as spontaneous and evoked.
- Over what time range the Eq. 44 fits were made, and how probes of different lengths were combined.
- Which 20 Wehr cells were used.

I also recorded a `paper_inconsistency`: the paper gives 73/110 as 64.6%; it is 66.4%.

I asked no questions of a reader.

## 3. Protocol gaps
1. The analysis code ships inside the dataset, and the paper doesn't link it. The protocol only covers "code the paper links". I treated it as the paper's code and cited it.
2. `measured` cannot hold a missing value. The counts claim has two untestable expected values (the voltage-clamp counts), so I left `measured` out for that claim.
3. Several criteria define only "reproduced" (fig3b, fig4, STRF). I used the protocol's general definition of "partially reproduced" for the cases in between.
4. A "not testable when no cell matches" criterion has no matching `blocked_by` value. I used `data_missing` for fig7.
5. The duplicate check compares recordings by length and trace statistics. Comparing full traces would have meant streaming everything twice.

## 4. Runtime and failures
The run took about 1.5 h of the 5 h. The clean-environment runs take 3 min and 21 min, with peak memory of 6.0 GB and 3.8 GB. Nothing failed.
