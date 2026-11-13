I've finished steps 1 to 5 for the CRCNS v1v2-1 attempt and run the handover (step 6). The notebook runs cleanly from a fresh environment in 12.5 minutes with a peak of 2.8 GB of memory. `entry.py check` reports 0 errors. Nothing is committed.

The entry is in `entries/zandvakili-2015/` (notebook, helper `v1v2.py`, entry.yaml, README, requirements and lock). The record is `attempts/zandvakili-2015-01.yaml`, and the verifier's package is in `executed/zandvakili-2015/handover/`. I did no verification of my own.

**(1) Outcome per claim**

| claim | outcome |
|---|---|
| fig4c-broad-ccg-peaks | reproduced (31 of 31 sites) |
| fig4c-narrow-peak-sites | not reproduced (16 of 31 = 0.516, expected 0.206) |
| fig4-narrow-peak-depth | blocked, data_missing |
| fig5a-rf-alignment | blocked, metadata_insufficient |
| fig5-narrow-pairs-rare | not reproduced (0.0105 of pairs, expected 0.003) |
| fig5b-v1v2-latency | partially reproduced (offset is significant; median 2.0 ms, width 3.89 ms) |
| fig5b-intra-areal-zero-lag | not reproduced, rests on an assumption (V1-V1 Wilcoxon p = 0.016) |
| figs3-efficacy | not reproduced (median 0.324%, mean 0.496%) |
| fig6a-coordination-before-v2 | reproduced (6 of 6 windows under every reading) |
| fig7a-threefold | partially reproduced (ratio about 1.9, expected 3) |
| fig7a-above-shuffle | reproduced |
| fig6b-not-after-v2 | not reproduced (raised at 80 ms after the spike) |
| fig6-slow-both-sides | reproduced |
| fig7d-time-course | partially reproduced (peak 2.5 to 3 ms before; some epochs after or far before are significant) |
| figs4-partner-not-needed | reproduced |
| fig7b, fig7e, fig7c, figs2a, figs2b, figs5 | blocked, data_missing |
| rf-sizes | blocked, metadata_insufficient |
| fig1, fig3, figs1, fig8 (simulations) | blocked, not_runnable |

**(2) Dataset, assumptions and questions**
- **What it holds:** 5 sessions from 3 animals, with 564 V1 and 147 V2 units. Spike times are stored in 1 ms bins; the paper used 0.1 ms. Each session has one recording per V2 tetrode.
- **What it lacks:** V2 depth, penetration identity, unit SNR and waveforms. RF positions are in pixels, with no scale or fixation point anywhere in the data set or the paper.
- **Unexplained selection:** narrow V1-V2 peaks appear at half the sites, against a fifth in the paper. The deposited sessions look like a selection the documentation does not describe; I recorded this as `selection_undocumented`.
- **Small metadata errors:** the descriptor gives 112.2 V1 units per session where the files hold 112.8. Its stimulus-code list is wrong for session 105l001p16, where code 7 is 180 deg; the sessions description says so, and the responses agree with it.
- **Clock check passes:** orientation decodes at chance before 30 ms and in the preceding blank, and at 0.94 to 0.99 from 60 ms. No duplicate units or sessions.
- **Assumption:** the paper's test of median offsets is taken to be the Wilcoxon signed-rank test (MATLAB `signrank`). The sign test reverses the V1-V1 result.
- **Questions for the authors** (as `methods_unavailable` findings):
  1. Which test gave the p-values for the median peak offsets?
  2. Were the bootstrap p-values paired or independent?
  3. Was the 10 ms CCG jitter window used for all significance tests?
- **Questions to a reader:** none. I don't believe the claims file misreads the paper.

**(3) Where the protocol was unclear or did not fit**
1. Reading e-b of the claims file (one 1 ms bin centred 2.5 ms before the spike) cannot be formed from 1 ms data. I ran the bins at 2 and 3 ms, which bracket it, and said so in the deviations.
2. The protocol has no blocking reason for simulations with no code that were left undone for time. I used `not_runnable` and said they were not attempted.
3. The claims file leaves reading j-b ("another window") unnamed. I chose 25 ms as a variant and recorded it as my choice.
4. A claim of absence is "judged on the paper's test alone", but the paper names no test, so the claims file lists two. I treated the disagreement as a step 1.6 case: I adopted one test, set `assumed: true`, and recorded the question for the authors.
5. The criterion for fig7d is ambiguous about whether "no significant distant epoch" applies per window or across all windows. Its "partially reproduced" wording settles it, giving the same outcome under both bootstrap readings.
6. The repository's `entry.py check` needs the dataset version string to appear in the code. For CRCNS that is `unversioned`, so I added a `VERSION` constant to the helper.

**(4) Runtime and failures**
- The work took about 1 h 40 min (16:25 to 18:04 UTC). The full notebook takes 12.5 minutes per run, and I ran it four times.
- Nothing failed in the final run. The only development error was a dtype bug, which I fixed.
