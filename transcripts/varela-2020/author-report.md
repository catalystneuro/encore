I finished the attempt at CRCNS hc-24 against Varela & Wilson (2020). The entry passes its checks (0 errors), the notebook runs from a clean environment in 337 s, and the handover package for the verifier is built. Of the 46 claims, 6 are reproduced, 10 partially reproduced, 3 not reproduced and 27 blocked. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig1s3-spindles-not-theta | Partially reproduced, resting on an assumption |
| fig2-swr-phase-delta-spindle | Reproduced |
| fig2c-swr-around-kc | Partially reproduced (the SWR minimum falls 30–60 ms before the KC, not 10 ms after) |
| fig3s1-ca1-mpfc-at-swrs | Partially reproduced |
| glm-thalamus-anticorrelated-swrs | Not reproduced (1 of 3 units, not 61.7%) |
| fig3e-thalamic-rebound-after-kc | Partially reproduced |
| kc-trough-timing | Reproduced |
| kc-ca1-mpfc-symmetric | Partially reproduced (CA1 matches, mPFC does not) |
| kc-regions-compared | Partially reproduced |
| fig3f-asymmetry-index | Reproduced |
| fig4-units-not-rhythmic | Not reproduced |
| fig5c-delta-phase-locking | Partially reproduced (80% of units locked, not 64.5%) |
| rebound-delta-phase-trend | Reproduced (only because r is about 0 and the criterion asks for any negative r) |
| spindle-cycles-by-ripple-power | Partially reproduced |
| mpfc-units-coupled-swrs | Reproduced |
| fig7c-run-units-in-spindles | Not reproduced (ripple-power effect present, no run effect) |
| maze-ca1-rates-similar | Reproduced |
| fig7d-run-units-peri-swr | Partially reproduced (p = 0.057) |
| fig7b-run-units-spindle-phase | Partially reproduced |
| 5 sleep-before/after-maze claims (maze-swr-kc-increase, maze-ripple-power-in-spindles, fig8-thalamus-unchanged-by-maze, fig8e-ca1-spindle-trend) and maze-control-sessions | Blocked, data missing |
| glm-re-versus-other-nuclei | Blocked, metadata insufficient |
| 21 other claims (thalamic rates, bursts, pairs, spindle modulation and the like) | Blocked, `other`: too few units, pairs or tetrodes for the claim's own test or tolerance |

## 2. The dataset, assumptions and questions

- **Contents:** 3 sessions (S1 to S3, from 3 rats) of the paper's 32. They hold 5 thalamic units, 7 mPFC units, 13 CA1 units, 8 multi-unit (MUA) tetrodes and 2 thalamic pairs. There is no maze epoch, no sleep before the maze, no position data and none of the control sessions.
- **Clock and duplicates:** spikes, LFP and events share one clock in all three sessions. No recording is deposited twice.
- **Missing labels:** no thalamic nucleus per unit, Session 2's units have no region in their folder name, and the LFP has no stated unit. I took S1's nucleus (MD) and S2's region from the titles of the deposited Matlab scripts.
- **Deposited spindle troughs:** there are 3.7 to 6.2 times as many as the Methods' 3 sd rule gives, and they reach -0.7 sd. The deposited S1 ripples (SWRs) are also more than the Methods' rule finds. Every analysis was therefore run on the deposited events and on the two detection rules.
- **Spike timestamps:** they are stored at single precision (0.98 ms steps in Session 3), which creates duplicate timestamps.
- **Unexplained epoch:** in Session 3 the mPFC spikes start 24 min before every other stream.
- **Paper inconsistency:** the Data availability statement names both HC-24 and HC-19.
- **Version:** the dataset is unversioned. I pinned it by the MD5 of `data.zip`, which the notebook recomputes from the stream and which matches. The header says why.
- **One assumption:** for fig1s3, wavelet power is taken relative to the mean power of the same state.
- **Questions for the paper's authors** (recorded as findings): what threshold produced the deposited spindle troughs and SWRs, and how the scalogram in Figure 1, supplement 3 was scaled.
- **Questions to a reader:** none.

## 3. Where the protocol was unclear

1. It does not say what to do when the claim's own test cannot reach significance at the available n (5 units give a smallest Wilcoxon p of 0.0625), or when no possible percentage falls within the tolerance. I blocked these as `other`, gave the reason, and reported every number. I applied the same rule to claims of absence, since a test that cannot reject says nothing.
2. "A claim that depends on a blocked claim is blocked" does not separate a dependence on another claim's method from a dependence on its result. Two claims depend only on the method of a claim that was blocked for too few thalamic units. I tested them and recorded a deviation.
3. Whether the Matlab scripts deposited in the dataset count as "the code the paper links" is not stated. I used them after the Methods, and cited them where they settle a detail.
4. "Record the first reading the criterion lists" does not cover the case where no reading matches. I recorded the first reading. For fig7b I recorded the reading where the values match, and said so.
5. Running every reading the claims file names multiplies quickly. I ran three event readings on every claim, but not the claims file's two extra readings of the sleep periods, and said so.

## 4. Runtime and failures

The work ran from 10:17 to about 11:13 UTC, and the notebook takes about 6 minutes. Nothing failed in the final runs. During development a fast approximate spike-counting method was off by up to 17% in single bins, because of the timestamp precision, so I replaced it with exact counts.

Files are in `entries/crcns-hc-24-varela-2020/`:
- reproduce_varela_2020.ipynb
- sleepcoord.py
- README.md

The record is `attempts/crcns-hc-24-varela-2020-01.yaml`.
