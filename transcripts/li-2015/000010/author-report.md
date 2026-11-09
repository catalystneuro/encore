I've finished steps 1 to 6 for DANDI:000010, version 0.220126.1905, the only published version (the paper cites no DANDI version). The entry is `entries/000010-li-2015/`, and `python tools/entry.py check` passes with 0 errors. The final clean run took 711 s and executed without errors. The handover package is built in `executed/000010-li-2015/handover/`, and nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| behaviour-performance | reproduced (holds only when the mean is formed over sessions) |
| fig1d-delay-inhibition-ipsi-bias, fig1d-sample-inhibition-smaller | blocked: data_missing |
| units-classification | partially_reproduced (5 of 6 counts match; no intermediate-width units in the dandiset) |
| fig2-selective-fraction | reproduced (912 of 1,245 under the main reading, exactly the paper's count) |
| fig2d-preparatory-perimovement | not_reproduced (peri-movement only 272 to 294, paper 389) |
| fig2c-selectivity-time-course | reproduced |
| fig2c-population-dynamics | blocked: methods_underspecified (39 of 40 readings hold, one fails) |
| ed2c-error-trials-predict-choice | reproduced |
| fig2e-no-contra-bias-spikes | reproduced (but ipsi-preferring neurons are the majority) |
| ed1-fast-spiking-properties | partially_reproduced (higher baseline holds; "less selective" does not) |
| tagging-counts | partially_reproduced (45 PT and 27 IT match; the failed-collision neurons have no label) |
| antidromic-latencies | blocked: methods_underspecified (a variant is shown: PT 2.68 ms, IT 5.11 ms) |
| fig3e-pt-it-both-activity-types | reproduced |
| fig3f-pt-contra-preferring | blocked: methods_underspecified (holds only if trials with tagging light are kept) |
| fig3f-pt-contra-selectivity | not_reproduced (PT P = 0.12 to 0.36) |
| imaging-selectivity-counts | partially_reproduced (selective count 1,417 at best, against a lower limit of 1,417.5) |
| fig4f-spatially-intermingled | not_reproduced (clustering at P < 0.05 in 57 of 64 combinations) |
| fig4h-pt-contra-imaging | not_reproduced (chi-squared test never reaches P < 0.001) |
| reaction-time | blocked: methods_underspecified |
| fig5b (2), ed6b, ed6d, ed3e, ed7, ed3-anatomy | blocked: data_missing |

## 2. The dataset and the questions

**What it holds:** the paper's 99 sessions from 19 mice and 59 imaging planes from 4 mice (4,706 included cells). The unit labels match the width rule: 1,245 putative pyramidal and 124 fast-spiking.

**Problems found:**
- **Duplicated units:** every PT and IT unit is a second copy of a Pyr unit, with an identical spike train. The 1,441 units are 1,369 distinct ones.
- **Missing units:** the 39 intermediate-width units are not in the dandiset.
- **Unflagged tagging light:** in 75 sessions the antidromic tagging light was delivered during behavioural trials (4,332 of 18,385 correct trials). Only the laser traces show it; the trial tables don't flag these trials. The traces are labelled watts but hold milliwatts.
- **Placeholder trials:** 1,540 trials have a lick instruction but no events. Most are marked right/hit/no early, and 1,345 of these hold no spikes. Taken at face value they inflate performance.
- **Missing data:** no photoinhibition or photoactivation data. The Ai32 mice have no light record, and the two Tlx×Ai32 tagging mice have none either.
- **Imaging metadata:** the files flag no early licks, give no plane depth, and label the mice "Rosa-lsl-tdtomato" where the paper uses C57Bl/6Crl.
- **Undocumented lick trace:** `lick_trace` looks like the reaction-time signal but is not documented as such.

**Questions asked (seven, in `questions/000010.yaml`):**
1. The rule for reading a reaction time from the lick trace.
2. Whether no-response ("ignore") trials count in per cent correct.
3. Three open details of the population-dynamics method (normalization, the 10 trials, the go-cue bin).
4. The length of the response epoch for imaging.
5. Whether layer 5 can be identified without a plane depth.
6. Whether trials with tagging light belong in the Figure 2 and 3 analyses.
7. The rule for picking out the antidromic spike.

## 3. Where the protocol was unclear

1. **Absence claims whose criterion lists readings.** The protocol says to judge absence on the paper's test alone, but the fig2e criterion names readings anyway. I judged on the paper's wording ("overall spike count across the recorded population") and showed the other readings.
2. **Readings from the claims file versus open details I found.** The protocol has two rules: "reproduced if any reading matches" and "blocked if readings disagree". I applied the first to readings named in the claims file. Where outcomes differed across an open detail I found (light trials, normalization), I blocked as methods_underspecified.
3. **Part of a claim's data absent.** For tagging-counts, half the counts are untestable because the labels are missing. The protocol has no outcome for this, so I used partially_reproduced and said why.
4. **Step 1.1 is easy to under-do.** I listed groups only in the first file, which had no `stimulus/presentation` series, and missed the laser traces present in 75 sessions. The protocol could say to list every group in every file. The extra analysis this forced, and the slower streaming, came from that.
5. **Runtime aim.** Streaming the laser traces pushed the run to 12 minutes, past the 10-minute aim. I accepted this, as it is well under the 30-minute CI limit.

## 4. Runtime and failures

- **Runtime:** a full clean run took 572 s before the laser traces were added and 711 s after. Loading takes about 8 minutes of that.
- **Failures:** none in the final run. During development, two code bugs failed dry runs and were fixed.
- **Post-run edits:** after the final run I changed some markdown wording: removed bold labels and corrected the version note, two sentences of the summary and two of the data check. I made the same edits to the executed copy and rebuilt the handover. No code or number changed.
- **Stray files:** the untracked dotfiles and `scripts` at the repository root are sandbox device mounts, not mine.
