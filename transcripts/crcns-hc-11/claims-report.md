I wrote `claims/crcns-hc-11/10.1126-science.aad1935.yaml`. All quotes pass the checker. The only problems it reports are 9 p-values I read from supplementary figure panels, which the text file does not contain; I checked each against the rendered page.

**Text read:** the NIH author manuscript in PMC (PMC4919122), with the main text, the legends of Figures 1 to 4, and the full supplement (Materials and Methods, Figures S1 to S22 with legends, references). I rendered the supplement PDF to read numbers printed inside panels of Figures S5, S9, S12, S13, S14 and S16 to S19. The paper links no analysis code; it only says the data are at CRCNS.org.

**Claims:** 29 in total.
- 28 have quotes. One (`figs14-plastic-ripple-bursting`) is marked `inferred`, because its numbers appear only in Figure S14 panel titles.
- 9 have statistics, 16 have expected values, and all 29 have criteria.
- They cover:
  - the replay increase from PRE to POST, and the scores against the shuffled null
  - per-cell contribution scores (PCC), the strongly contributing cells, the 73% overlap, and the 105 rigid and 105 plastic cells
  - the shuffle and exclusion analyses of the highest-ΔPCC cells
  - spatial coding of rigid against plastic cells, and specificity changes within the session
  - firing rate, ripple gain and bursting
  - the low and high firing-rate split, coactivity by firing rate, and replay restricted to slow-firing or high-gain cells
  - ripple incidence, preservation of coactivity and temporal bias, and cluster quality

**Details the paper leaves open, and the readings named for each:**
- **Yoking PRE and POST to the shorter epoch:** (a) the last part of PRE and the first part of POST; (b) the first part of each; (c) time counted only in offline states.
- **LFP ripple detection threshold:** (a) mean + 3 SD; (b) mean + 5 SD, both in the 150 to 250 Hz band.
- **Sleep and state scoring thresholds:** (a) the lab's own state epochs; (b) a recomputed scoring.
- **Linear-track events:** (a) each event scored with both direction templates; (b) each event assigned to one direction by the direction decoder.
- **Test for a strongly contributing cell:** the Methods name a rank-sum test and the Figure S19B legend a signed-rank test. Readings: (a) signed-rank test of per-event PCC against zero; (b) rank-sum test of observed against cell-shuffled scores.
- **Low and high firing-rate split:** the Figure S16 legend refers to the Methods, which do not describe it. Readings: median split within session and direction, within session, or pooled; rate from offline PRE and POST together or from PRE alone.
- **"Session-wide" firing rate:** (a) offline time of PRE and POST together; (b) the whole recording.
- **MAZE rate:** (a) all maze time; (b) running only.
- **Place-field stability:** (a) first against second half of the maze epoch; (b) odd against even laps.
- **Event set for the duration claim:** (a) all ripple events; (b) only the events used for Bayesian replay.
- **Tests the paper does not name:**
  - for the replay comparisons of slow against fast cells and high against low gain: rank-sum test, or a bootstrapped confidence interval
  - for the similar track distribution of rigid and plastic fields: Kolmogorov-Smirnov test, or a rank-sum test of distance from the track ends
  - for the ripple-triggered rate change: mean rate over 0 to 100 ms, or the peak bin
  - for the rate-window ranking in the coactivity analysis: ranks within session, or pooled
- **Standard choices that cannot change the outcome:** the Gaussian kernels are read as SDs, and the shuffle analyses use 5% steps.

**Missing from the paper:** the images of the main Figures 1 to 4 are not under `paper/`. So the Figure 1C sequence scores and their significance marks, the Figure 3A values, and the Figure 4A to 4E values are not recorded. Those claims rest on direction and the named tests, without expected numbers. The main text also cites some supplementary figures one number off (S16 and S17 for what the supplement numbers S17 and S18); the file follows the supplement's own numbering.
