All five Author steps and the handover are done for doi:10.1038/s41586-019-1235-y on CRCNS vta-2. The entry check reports 0 errors and a clean run of the notebook passes in 226 s. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig1b-latency-scales-with-reward-rate | reproduced |
| fig2-tagged-dopamine-cells | partially reproduced |
| fig2d-dopamine-firing-rates | reproduced (7.77 Hz, range 3.77 to 12.93) |
| ed5-pavlovian-dopamine-click-responses | partially reproduced |
| ed5-pavlovian-dopamine-cue-responses | partially reproduced |
| ed5a-pavlovian-behavior | reproduced |
| fig2efgh-tonic-firing-indifferent-to-reward-rate | not reproduced, rests on an assumption |
| fig2i-burst-rate-no-change | reproduced |
| fig2i-no-inactive-states | reproduced |
| retro-tagged-cells-resemble-others | not reproduced, rests on an assumption |
| fig4ac-dopamine-cue-responses | partially reproduced, rests on an assumption |
| fig4a-no-dopamine-firing-ramp-before-approach | reproduced |
| fig4e-light-on-alignment | partially reproduced (16 cells, not 25) |
| fig5a-early-trial-firing-not-reward-rate | not reproduced |
| fig5a-positive-rpe-reward-cue | reproduced |
| fig5ab-weak-negative-rpe | reproduced, rests on an assumption |
| ed8-other-reward-expectation-estimates | partially reproduced |
| The other 20 claims (microdialysis, dLight, in vitro, CTb, untagged units) | blocked, `data_missing` |

Totals: 8 reproduced, 6 partially reproduced, 3 not reproduced, 20 blocked.

## 2. Dataset, assumptions, questions

**What the data set holds.**
- **Contents:** one zip with `VTA_data.mat` (MATLAB 7.3) and three of the authors' scripts. It holds only the 29 tagged cells and their behaviour, with bandit, Pavlovian, laser and sleep segments.
- **Version:** CRCNS does not version data sets, so it is recorded as `unversioned`. The notebook checks that the bucket's ETag equals the MD5 in `checksums.md5`; the header gives the reason.

**What was found about it (all in the record's findings).**
- **Wrong rat count:** the descriptor says 4 rats; the cells come from 5.
- **Clipped latencies:** the `CNIlatency` field is stored as 65535 ms for every latency over 65.5 s (120 trials). A few other values also disagree with the event times.
- **Unsorted spike times:** spike times are out of order in 13 units.
- **Paper counts:** the Methods' per-rat counts add up to 28, not 27. The data hold 8 IM1037 cells and an 8/19 split between the two Pavlovian tone sets, where the paper gives 9/18.
- **Undocumented fields:** what `FR` means, the names of the event rows, and what the food-port window is aligned to.
- **Identification criteria:** 4 cells fail the paper's waveform r > 0.9 test, and 2 cells never got 5 or 10 ms pulses.
- **Authors' scripts:** they group trials differently from Fig. 5a and use a 20 ms SD kernel.
- **Duplicates:** none; no recording is deposited twice.

**Assumptions** (each is a deviation with `assumed: true`, and each is asked of the authors as a `methods_unavailable` finding):
1. **Tonic test, Fig. 2f:** I used per-cell rank-sum tests on 1 min bins, because the Methods count tonic spikes in 1 min bins. Under this reading 18 of 27 cells differ. Using block means instead, 2 cells differ (0 if the median block is put with the low blocks).
2. **Cue-response window:** 0.5 s after the event, Bonferroni-corrected over its bins.
3. **Pause measure:** only intervals between spikes inside the 2 s window. This gives the paper's 2 of 29 cells; counting the window edges gives 8.

**Questions to a reader:** none.

## 3. Where the protocol was unclear or did not fit

1. Claims of absence are to be judged on "the paper's test alone", but the legends that name those tests were missing. I ran the readings in the claims file and, where they disagreed, adopted one as an assumption under step 1.6.
2. The data set includes the authors' own code, which the protocol's order of method sources does not mention. I treated it as the paper's code (ranked after the Methods) and cited it.
3. With only the selected cells deposited, the selection count in fig2 cannot be repeated. I tested whether each deposited cell meets the criteria and said so in the notes.
4. The protocol does not say what `measured` should be when no reading matches. I gave the closest reading (largest wire) and explained it in the notes.
5. The requirement for a contrast-based clock check could not be met for 3 units with the reward contrast. I said so and pointed to their Go-cue responses.

## 4. Runtime and failures

- **Run time:** about 50 minutes (07:20 to 08:08 UTC). The notebook takes 226 s, with about 1 GB peak memory.
- **Failure during development:** one missing latency first broke the learning-rate fit. Fixed by leaving trials without a latency out of all fits.
- **Leftover files:** there are untracked dotfiles at the repository root (`.bashrc`, `scripts` and others). They are sandbox device files and I left them alone.
