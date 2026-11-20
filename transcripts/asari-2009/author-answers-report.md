The reader answered the one question, and I re-ran the affected claim on the amended claims file. Its outcome stays reproduced, but now rests on a recorded assumption about how the example cell is matched. Lock, check and the full run all passed (0 errors, notebook ran in 1817 s), and the handover is built in `executed/asari-2009/handover/`. Nothing was committed or pushed, and I did not verify my own work.

**Question (fig2-example-long-context): does the Figure 2 legend identify the example cell and probe?**

The reader amended the claim, which changed two things:
- **Which probe is tested:** the claim used to accept any of the candidate probes. It now tests only the probe of the cell whose reliability values match the Figure 2 legend within 10%: 0.61 ± 0.07 over the cell's seven fragments and 0.74 ± 0.08 for the probe.
- **The time windows:** these now allow 10%. The probe passes if it has significant periods before 2 s, none between 2.2 and 3.6 s, and one starting after 3.6 s.

| claim | earlier outcome | outcome now |
|---|---|---|
| fig2-example-long-context | reproduced | reproduced (`assumed: true`) |

- **Earlier:** I had already tested the same probe, 20051222-ha1-001 probe 4. It passed only because I counted a significant period starting at 3.97 s as the paper's "after about 4 s". Read strictly, that period overlaps the 2 to 4 s window by 30 ms and the probe fails.
- **Now:** of the 40 candidate probes with six or more trials per context, only that one matches: the cell averages 0.611 ± 0.081 and the probe 0.737 ± 0.075. Its significant periods run to 1.60 s, there are none from 1.60 to 3.97 s, and they resume from 3.97 to 4.60 s. That meets the amended windows directly, so the 30 ms question no longer arises.
- **Why it is marked assumed:** I matched on the two mean correlations, since the criterion asks for "the closest to both". Two other readings find no matching cell, which would make the claim not testable:
  - the leave-one-out correlation (the cell's mean is 0.732);
  - also requiring the SDs to match within 10% (the cell's SD is 0.081 against 0.07, 16% above).

  I chose the pairwise mean because it is the reading that reproduces the population value in fig2-example-reliability (0.310 against 0.31; leave-one-out gives 0.437). The deviation explains this, and a new `methods_unavailable` finding asks the authors to confirm the example recording and the correlation measure.

What I changed:
- **Notebook:** the section now picks the matched probe, applies the amended windows, and shows both alternative readings. The old strict windows are printed for reference.
- **`asari.py`:** it also reports the spread of the pairwise trial correlations, so the probe's SD can be printed. No other claim's numbers changed; for example, fig3a still finds 183 of 305 probes significant.
- **Attempt record:** the claim's notes say what the answer changed, and the summary table marks the assumption.

The entry ran in full twice, because the first run used a placeholder conclusion.
