I've finished steps 1 to 6 of the Author section. The entry `entries/000129-makin-2018/` passes `entry.py check`, both notebooks ran from a clean environment, and the handover package is in `executed/000129-makin-2018/handover/`. The record is `attempts/000129-makin-2018-01.yaml`. Of 31 claims, 10 are reproduced, 2 partially reproduced, 6 not reproduced and 13 blocked. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| units-monkey-i | not reproduced: 111 units, and the file has no hash units |
| fig2-velocity-boost | not reproduced, assumed: KFobs ratio 1.92, needs more than 2; the code's kinematics give 2.05 |
| fig2-kflatent-dynamic-little-effect | reproduced |
| fig2-refh-static-vel-acc | reproduced (velocity margin only 0.05 dB) |
| fig2-position-dynamic-gain | not reproduced: 4.45 dB against 3 ± 0.5 |
| fig2-sagittal-better | partially reproduced: 23 of 24 pairs (24 of 24 with one other rEFH seed) |
| fig2-linear-worst | reproduced |
| fig2-gross-failures | reproduced, but only because no R2 is negative at 64 ms |
| fig4-vel-acc-every-session | reproduced for the per-session part; the bootstrap can't run on one session |
| fig4-best-variable | not reproduced: the rEFH (+KF) decodes position best |
| kflatent-modest | reproduced (holds under one reading with either kinematics) |
| fig8-velocity-variants | not reproduced: losses of 0.11 and −0.08 dB against 0.7 and 0.4 |
| fig8-gaussian-still-beats-ukf | reproduced, assumed (standardized counts); fails with the code's transform |
| fig5-advantage-with-binwidth | reproduced |
| fig5-derivative-order | partially reproduced: 3 of 4 widths, fails at 16 ms |
| advantage-grows-with-derivative | reproduced |
| fig7-affine-position | not reproduced: correlations within tolerance, but static KFlatent is not the lowest |
| fig7-kinematic-model-saturates | reproduced under reading b only |
| 13 claims needing the bootstrap or regression across 49 sessions, plus fig4-task-similar | blocked, `too_large` |

## 2. Dataset, assumptions, questions

**Dataset**
- Only one published version exists, 0.241017.1444, so I pinned it. The draft holds the same two assets and differs only in its title.
- It holds one monkey I session, M1 only. The file dates it 2017-02-02, which is not in the paper's session list (`Indy_HC_Sessions.csv` ends 2017-01-31).
- The units are sorted only; the hash units the paper counted are missing.
- Three 0.1 s gaps in the training file have NaN kinematics and no spikes, and nothing documents them.
- The test file (190 s) has no kinematics, so only the 649 s training file is usable.
- The test file does not repeat the training file. Spikes and kinematics share one clock: velocity decodes best from spikes 64 ms earlier.

**Assumptions** (both are the main readings the claims file already chose; the alternative changes the outcome, so the outcome is marked `assumed`)
- Kinematics: the Methods' filtered fingertip position, not the code's unfiltered cursor position. This decides fig2-velocity-boost.
- Standard-normal rEFH input: standardized counts as the Results say, not the code's 2√(R+3/8). This decides fig8-gaussian-still-beats-ukf.

**Questions for the paper's authors** (recorded as findings)
- Which kinematics were decoded: filtered fingertip or unfiltered cursor?
- Which input did the standard-normal variant use?
- Can Li's UKF2 fitting code be published? It is called by the repository but not in it, so I re-implemented the UKF.

I asked no reader any questions.

## 3. Where the protocol was unclear

1. **Blocked reason for claims needing the other sessions.** The paper's sessions are public on Zenodo, so `data_missing` doesn't fit, and the claims are `data: dataset`, not `elsewhere`. I used `too_large`, with an estimate scaled from timing this one session, not a timed run on a larger one.
2. **A criterion where only one part can be tested** (per-session plus bootstrap, in fig4-vel-acc-every-session). The protocol doesn't say how to grade this. I graded the testable part and listed the untested part as a deviation.
3. **A criterion that holds trivially** (fig2-gross-failures, no failures at all). I recorded it as reproduced and said so in the notes.
4. **Several claims share one costly fit**, so "each claim's section its own generator" doesn't fit. I seeded each fit configuration instead and showed two extra rEFH seeds as a variant.
5. **Seeds can change an outcome** (fig2-sagittal-better), but the protocol treats a seed as a detail that can't. I kept seed 0 and reported the others.

## 4. Runtime and failures

- **Clean run:** 604 s for the 64 ms notebook and 1301 s for the bin-width/training/neuron notebook. The second is under the 30-minute limit, but not by much.
- **Background run lost:** my first background development run was killed with its sandbox, costing about 20 minutes; everything after ran in the foreground.
- **Small fixes:** one code bug (the SNR helper returned an array) was fixed before the clean run.
- **Not run:** the tapped decoders for fig9-taps (that claim is blocked anyway).

The run finished at 21:00 UTC.
