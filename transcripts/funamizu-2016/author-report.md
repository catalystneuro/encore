I finished steps 1 to 5 and ran the handover (step 6). The final clean run passed `entry.py all` in 24.6 min, the handover is in `executed/001605-funamizu-2016/handover/`, and the entry check reports 0 errors. Nothing is committed. Finished at 05:59 UTC, well before the 07:38 cut-off.

## 1. Outcomes (pinned version 0.251007.0553)

| Claim | Outcome |
|---|---|
| session-counts, neuron-counts | reproduced (exact) |
| behaviour-timing | not reproduced (9.30 s to reward against 7.4 ± 0.1) |
| lick-goal-correlation | partially reproduced (all sessions P < 0.01; lowest r 0.218, criterion floor 0.232) |
| fig1c-licking-without-sound, supp1-licking-speed | reproduced |
| fig1d, fig1e, fig1fg, supp2d, muscimol-locomotion, sound-responsive-layer3 | blocked, `data_missing` |
| neuron-classes, fig2d-task-relevant-proportions | not reproduced (counts 12 to 41% high) |
| fig2d-goal-distance-ppc-more | reproduced |
| fig2d-after-vs-before, fig2d-layer-distance-preference | reproduced, assumed |
| fig3b-distance-over-time | blocked, `too_large` (about 14 h) |
| supp6-distance-not-sound | partially reproduced (23 of 24 comparisons) |
| tuning-similar-ppc-pm | blocked, `methods_underspecified` (readings disagree; the criterion says to block) |
| fig3c-continuous-ramp, fig3c-ppc-ramp-without-sound | reproduced |
| supp8a, supp8b, supp9 | reproduced, assumed |
| supp8c-ppc-steeper-than-pm | partially reproduced, assumed |
| fig4-above-chance, fig4c, fig4d, fig4e | reproduced, assumed |
| supp11, fig5a-map-follows-continuous, fig5b, fig5cd, fig5c | reproduced |
| fig5a-map-decreases-without-sound | partially reproduced (13 of 16 tests in PPC layers 3 and 5) |
| fig5-layer3-steeper-than-layer2, supp13-map-speed, lognormal-decoder-better | not reproduced |
| svm-correlations | blocked, `too_large` (about 1.4 h per reading) |

## 2. Dataset, assumptions and questions

**What the dataset holds**
- It matches the paper's counts exactly: 94 sessions, the sessions per mouse, area and layer, and 41,031 ROIs, which equal the paper's active-neuron counts.
- dF/F equals (R − mean R)/mean R to within 3e-5, as the Methods define dR/R.
- No recording is deposited twice.

**What is missing or misdescribed**
- The muscimol mice and the sound-mapping trials are not in it. The paper's data page names no other deposit.
- `sound_on_off` and the speaker table hold only the start tone, one frame per trial, despite the description. Sound and no-sound zones had to be computed from the condition and the distance.
- Licks are stored only as a lick frequency capped at 10 Hz, not as lick times.
- Times to reward (9.3 s) and the share of trials over 20 s (0.48%) differ from the Methods (7.4 s, 2.71%).

**Assumptions** (all marked `assumed: true`, with every reading shown in the notebook)
- O1, the t-test baseline, is taken as zero. Under it 91 of 94 sessions have goal-distance neurons, the paper's own count; the other baseline gives 94.
- Chance level is the flat prior's error.
- Fig. 4c-e use 4.2 cm bins.
- Supp. Fig. 9 groups are equal quarters, which match the figure's group sizes.
- Activity traces have no moving average, as Methods eq. 5 implies.

Two details came from the paper and needed no assumption: the Supp. Fig. 1 zone (from its panel titles) and the trace reading. The open questions for the authors are recorded as `methods_unavailable` findings.

**Question to a reader** (`questions/001605.yaml`): the claims file reads the Supp. Fig. 9b "difference" as absolute, but the figure's axis (+37.7 to −58.6 cm) looks signed.

## 3. Where the protocol was unclear
1. The claims header says to block when readings disagree, while step 1.6 allows adopting the best-supported reading. I adopted assumptions, except where the criterion itself says to block (tuning-similar).
2. Criteria without a "partially reproduced" clause: I used partially reproduced where the effect held in part.
3. A choice forced by how the data are stored (licks as a capped frequency) is not a method reading. I treated it as a standard choice and showed a variant.
4. A `too_large` block needs a time estimate, but numbers from outside the notebook may not enter the record. I timed fits on synthetic data of the same size and said so in the record.
5. The claims file's permuted-distance "chance" does not measure chance. I adopted the other reading and did not ask a reader.
6. The clock check: I used the reward-to-goal lag and the decoder against the flat prior, not a decoder with shifted labels.
7. The per-animal breakdown is given only for the behaviour and neuron-class claims.

## 4. Runtime and failures
- The notebook runs in 24.6 min, about 21 of them streaming the 94 files with 4 worker processes.
- One thing is left undone: an empty harness directory, `entries/001605-funamizu-2016/.claude/.cc-writes`, sits inside the entry. Removing it needed approval and was denied, so it should be removed before the commit.
