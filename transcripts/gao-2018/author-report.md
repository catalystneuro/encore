I finished steps 1 to 5 and ran `handover`. Of the 45 claims, 18 were tested and 27 are blocked. The entry check passes with 0 errors and the notebook runs from a clean environment in 465 s (about 7.8 min). Nothing is committed.

## 1. Outcomes

| claim | outcome |
|---|---|
| fig1g-fastigial-activation-early-sample-no-effect | reproduced |
| fig1g-fastigial-activation-delay-errors | reproduced (0.873 to 0.630, p < 0.0001) |
| fig1h-fastigial-activation-delay-bias | reproduced (reading a; 2 mice biased contra, 3 ipsi) |
| fig1g-dentate-activation-little-effect | reproduced (p = 0.108; 3 of the paper's 8 mice) |
| fig1k-inhibition-delay-bias | partially reproduced (CD12 and CD13 are biased the same way) |
| fig2-alm-selective-fraction | reproduced (0.739 and 0.753, at the edge of the tolerance) |
| fig2cd-selectivity-emerges-gradually | blocked, methods_underspecified |
| fig3d-alm-altered-by-cn-inhibition | partially reproduced (fraction 0.395 matches; latency 15 to 23 ms against 7.1) |
| fig3e-alm-mean-rate-unchanged | partially reproduced (rates 22% below the paper's; paired and unpaired tests disagree) |
| fig3e-alm-increase-decrease | reproduced (increase fraction 0.592) |
| fig3f-alm-selectivity-abolished-by-cn-inhibition | reproduced, `assumed` |
| fig4-fastigial-activation-alm-latency | partially reproduced (latency 2.1 to 5.6 ms matches; fraction modulated 0.29 against 0.51) |
| fig4e-fastigial-activation-abolishes-alm-selectivity | reproduced |
| fig4f-fastigial-effect-persists | reproduced |
| fig4g-dentate-effect-recovers | not reproduced (3.4% to 5.3% of neurons stay significant more than 1 s after offset) |
| fig4i-cd-control-separation | reproduced |
| fig4i-fastigial-collapses-cd | reproduced (reading b) |
| cd-captures-selectivity | reproduced, `assumed` |
| ed10d-fastigial-endpoints-no-prediction | not reproduced (slope 0.42, p = 0.005) |
| 26 others: lesions, CN recordings, licking, other stimulation epochs, VGAT-ChR2 mice, anatomy | blocked, data_missing |

## 2. The dataset, assumptions and questions

**What the dataset holds.**
- I pinned 0.220126.1903. The paper cites no version, and this is the only published one; the draft has the same assets.
- It holds 54 ALM sessions in the 13 ALM-recorded mice of Supplemental Table 1. No recording appears twice.
- It has no CN recordings, no lick times, no behaviour-only sessions and no anatomy.

**Findings about the data.**
- `photo_stim_id` is undocumented. I read the codes from the timing of the ALM response: 1 and 3 are early-sample photo-activation, 2 and 4 early-delay photo-activation, 5 and 6 delay photo-inhibition.
- The event-time columns are described as relative to trial start but are on the session clock.
- The hemispheres in the files disagree with Supplemental Table 1 for CD12, CD13 and CD14.
- The anm subjects cannot all be matched to the paper's AN105 to AN109.
- The files' `cell_type` labels 60 narrow-waveform units "pyramidal".
- The files hold more units than the paper reports (1082 against 912, and 676 against 454), and nothing says what the paper left out.
- In 5 sessions I could not show that spikes share the trial clock.

**Assumptions** (each is a deviation with `assumed: true`):
- fig3f: the 10 preference trials are 10 in all, the literal reading of the Methods.
- cd-captures-selectivity: measured on trials independent of those that estimated the cd, with single-trial variance. Only 1 of 8 combinations of these choices matches both numbers.

**Questions for the paper's authors** (`methods_unavailable` findings):
- Which epoch, and how many trials, fix each neuron's preferred trial type (E3)?
- How is a latency bin labelled, and is a pre-onset baseline subtracted?
- How is the fraction captured by the cd computed?

**Questions to a reader:** none.

## 3. Where the protocol was unclear

1. **Partial testability.** fig2cd covers ALM and CN, and only ALM is in the dataset. The protocol does not say how to judge a claim only half of whose data exist. Its method question decided the outcome, so this did not matter here.
2. **"Count, or the fraction where the dataset holds fewer neurons."** Here the dataset holds more neurons. I judged the fraction and recorded it as a deviation.
3. **Reading rules.** Readings the criterion lists count if any of them matches; readings of a method detail must all agree. A shared method (E3) that names a detail as open falls between the two. I applied the method-detail rule.
4. **Inferring undocumented codes from the data.** Link claims cover only outside data, so the protocol has no form for this. I made it a deviation on each claim and a finding.
5. **Behaviour claims tested on recording sessions.** The protocol does not say whether these may stand in for the paper's behaviour sessions. I tested them and recorded it as a deviation.

## 4. Runtime and failures

- The notebook runs in 465 s; the first run took 469 s. Peak memory was about 0.5 GB.
- Nothing failed. The run took about 50 of the 300 minutes.
- Files are in `entries/gao-2018/` and `attempts/gao-2018-01.yaml`.
