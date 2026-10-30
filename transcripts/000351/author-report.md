The attempt is complete: the entry passes `check` and a clean-environment `run` (96 s, outputs identical to the run the conclusions were written from), and the handover package is built in `executed/000351-jeong-2022/handover/`. Nothing is committed and nothing was verified by me.

## 1. Outcomes (38 claims)

| Claim | Outcome |
|---|---|
| session-day-link | partially reproduced |
| methods-session-counts | reproduced |
| exp1-excluded-rewards, fig3e, fig3g, figs8k, figs8b, figs8d, figs8g, figs8h, figs8l | reproduced (9) |
| figs8e-lick-bout-responses | partially reproduced |
| fig4ef, figs10c, fig4hi (both), figs10b, fig4kl, fig4jl, fig6b | reproduced (8) |
| fig4p-background-faster-decay | partially reproduced |
| fig5d (both), figs11de | reproduced (3) |
| fig6d (both), fig6g, fig6i-learning, fig6i-last-session-licking, figs12f | reproduced (6) |
| fig6i-lower-cs1-asymptote | not reproduced |
| 7 simulation claims (fig2, fig3cf, fig5b, fig6h, figs5, figs6, figs13) | blocked, not_runnable (Matlab model code, nothing in the dandiset) |

Most of the paper's Table S1 statistics come out to the second decimal, for example Test 1 t = 4.41 and Test 2 t = 5.95. The misses:
- **Fig S8E:** the dry-lick response is negative but significant only in the 0 to 0.5 s window.
- **Fig 4P:** t = -2.40, p = 0.053, against the paper's -3.51.
- **Lower CS1 asymptote with inhibition:** t = 1.70, p = 0.117, against the paper's 2.80.

## 2. Dataset

- **Version:** I pinned 0.260828.1905, the only published version; the paper cites none.
- **Missing sessions:** seven sessions inside the code's day ranges are not in the dandiset (M2 Day23, M3 Day16 and 31, M4 Day30 and 38, F2 Day16, M6 Day49). The paper's session means for Experiments 2, 4 and 5 equal the counts that include them. M4 Day38 is that animal's first background-reward session, which bears on Fig 4P.
- **Metadata errors:**
  - Event times are in seconds but labelled milliseconds.
  - In 65 of 101 Experiment 7 files the raw photometry timestamps are in thousands of seconds.
  - The DAT-Cre mouse datHT-M7 is labelled genotype `wt`.
- **Conditions not labelled:** the condition of each session is not labelled, and the per-figure session lists exist only in the paper's code and an unversioned Google spreadsheet.
- **Photometry coverage:** in 13 sessions dF/F does not cover the whole event log (WT-M2 Day6 has none for its first 1117 s).
- **Integrity:** no recording is deposited twice. dF/F is in percent, as stated. The dF/F and event-log clocks are consistent in every experiment.
- **Assumptions:** none adopted. Choices that cannot change an outcome are recorded as deviations.
- **Question for the paper's authors:** which window the Fig S8E tests used. It is recorded as a `methods_unavailable` finding.
- **Questions to a reader:** none. The claims file attributes the Fig 6G baseline to the code. In fact the code averages before every code-15 event, CS1 and CS2 alike. Both readings give the same outcome, and the code's matches the paper exactly, so I recorded this as a deviation.

## 3. Protocol points

1. Seven simulation claims need no dataset data, and the protocol has no category for them. I blocked them as `not_runnable`.
2. The link claim's "every Day number from startday to endday" can mean the listed days or every integer day. I ran both and judged on the listed days (117 of 119), with every integer day also reported (320 of 331).
3. The clock-check guidance is written for spikes and trial tables. For photometry, my first check (the response to the reward lick) was confounded by the cue response in Pavlovian sessions. I switched to unpredicted events and a CS+ against CS- contrast, with lags of ±2 s so the window does not reach the reward 3 s after the cue.
4. Two criteria (figs8e, fig4p) define only "reproduced". I used `partially_reproduced` where part of the claim held, following the protocol's general definition.
5. A question to a reader requires saying "why the misreading could change the outcome". The protocol does not say what to do with a misreading that cannot change the outcome. I recorded the Fig 6G one as a deviation.

## 4. Runtime and failures

The run took about 45 minutes, from 01:10 to 01:55 UTC. The notebook runs in about 1.5 minutes. Two development runs failed and were fixed: an all-NaN clock profile in extinction sessions, and a pyPhotometry scale check that ignored the 15 s offset between the raw and dF/F clocks.

The working tree also shows untracked dotfiles (`.bashrc`, `.idea` and so on) and `scripts/`. These are not from this run; `scripts/` was already there when I started.
