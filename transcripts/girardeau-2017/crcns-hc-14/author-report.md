I've completed authoring steps 1 to 6 for CRCNS hc-14. Of 38 claims, 26 are reproduced, 4 partially reproduced, 5 not reproduced and 3 blocked. The final run of `tools/entry.py all` passed (0 check errors, notebook ran in 17 min), and the handover is built in `executed/crcns-hc-14-girardeau-2017/handover/`. Nothing is committed. I asked no reader questions. Twenty outcomes rest on a stated assumption (`assumed: true`).

**1. Outcomes**

| Claim | Outcome |
|---|---|
| units-recorded | partial: 61 sessions, 2,038 BLA and 1,260 hippocampus match; CeN and piriform fall short because Rat08's shanks for them are only colour-coded |
| fig1b-dz-speed-anova, fig1b-dz-speed-posthoc | partial (assumption) |
| fig1b-speed-ratio, figs1b-ratio-each-rat, fig1c-slower-in-dz-post-run | reproduced (assumption) |
| figs1c-habituation | reproduced |
| airpuff-location-no-bias | not reproduced (assumption) |
| fig2c-bla-pyr-higher-in-sleep, fig2c-bla-interneurons | reproduced (assumption: which column is REM) |
| fig2c-skewed-rates | reproduced |
| fig3c-hpc-bla-ev-nrem, fig3c-hpc-bla-ev-rem-absent | reproduced (EV − REV 3.14 ± 0.73%, paper 3.13 ± 0.73%) |
| fig4, figs5b, run-correlated-pairs, fig5a, figs6b, figs9, fig5b, fig7b strong, fig7b weak, fig7c | reproduced, most of them to the paper's printed numbers (2,521 of 37,660 pairs; F = 29.08; 63 cells; r = 0.27 over 866 pairs) |
| bla-rates-safe-airpuff-absent | reproduced (assumption) |
| fig3c-decay, fig3d-pir-weaker-than-bla, fig6a-safe-trajectory-no-reactivation, fig6b-airpuff-greater-than-safe | not reproduced (substitute NREM) |
| figs5a-hpc-bla-all-cells | partial: second 20-min window p = 0.051 (substitute NREM) |
| figs4-intra-structure-nrem, ripple-rate, fig6a-airpuff, figs11a, figs11b, figs11c | reproduced (substitute NREM) |
| fig3d-pir-reactivation, fig3e-cen-no-reactivation, figs4-intra-structure-rem-absent | blocked, `data_missing` (they need REM) |

**2. The dataset, assumptions and questions**

- **What it holds:** sorted spikes, positions and events for 65 sessions; the paper's 61 are listed only in `sessionindexing.mat`.
- **Summary tables:** the authors' tables (`AllRats-Variables`) are undocumented. I identified their columns against the raw spikes:
  - the units agree in 60 of 61 sessions; Rat08-20130722 has 25 more units in the raw files;
  - the pair table's run correlations match the raw ones exactly in 17 of 29 sessions and at r = 0.58 to 0.98 in the other 12;
  - the EV formula reproduces the deposited pooled EV exactly.
- **Sleep states are not deposited.** Rescoring them from the LFP would mean streaming about 430 GB of tar.gz.
- **Structure lists** come in four formats, one per rat.
- **Air puff location:** only 6 of 55 behaviour sessions have a file giving it.
- **Assumptions:**
  - Column 5 of the state-rate table is REM. Column 8 is shown as a variant; with it, the two REM claims would partly fail.
  - The air puff location is the median head position at the air puffs.
  - The substitute NREM is any period of at least 30 s in pre- or post-sleep with head speed below 4 cm/s. It matches the authors' NREM firing rates (median r = 0.99) but gives weaker EV (1.96% against 3.21%). I re-ran every claim that depends on it at 2 cm/s.
- **Questions for the authors** (recorded as `methods_unavailable` findings): which state column is REM, and where the air puff location comes from.

**3. Protocol gaps**

1. `archives.md` only describes zip files. These are tar.gz files with no index, so I streamed each one in full (requests plus `isal`) and recorded this in the helper.
2. The protocol has no rule for undocumented derived tables in the dataset. I tested claims on them after checking them against the raw data, and stated this in each claim's deviations.
3. When sleep scoring is missing, the claims file allows "a substitute", but the protocol doesn't say whether that is an assumption or a block. I treated it as an assumption, validated it against the authors' tables, and showed its sensitivity to the speed threshold.
4. There is no outcome for a claim where only some parts of the criterion can be tested (the REM halves). I blocked those claims and reported the NREM halves in their notes.
5. There is no rule for whether an estimated input, like the air puff location, makes an outcome "assumed". I marked those outcomes as assumed.

**4. Runtime and failures**

The run took about 2 h 50 min of the 5 h. Streaming all 61 sessions takes about 11 min; the notebook takes 17 min end to end with a peak memory of 1.7 GB. One bug turned up between executed runs and I fixed it before the final run: the run epoch was taken as a single span, which pulled in the sleep between two run subsessions in one session. Nothing failed in the final run.
