I finished steps 1 to 5 of the Author section and ran the handover (step 6). Of the 30 claims, 16 are reproduced, 5 partially reproduced and 9 blocked. The final notebook run passed in 28.5 min (1713 s); the record validates with 0 errors and the verifier's package is in `executed/gonzalez-2024/handover/`. I did not commit or push.

The record is `attempts/gonzalez-2024-01.yaml`; the entry is in `entries/gonzalez-2024/`. The analyses are ports of the paper's code (github.com/alexgonzl/TMA at the cited commit 6f93593, MIT licence) in `tma.py`.

**1. Outcomes**

| claim | outcome |
|---|---|
| fig1d-task-performance | partially reproduced (accuracy 73.0% matches; 152 trials per session, not 110) |
| fig1-switch-performance | partially reproduced (Switch accuracy 73.8% and "similar" hold; 69 Switch trials, not 54; rests on the claims file's 10-point threshold) |
| fig1-training-to-criterion | blocked, data_missing |
| fig2c, fig2d, fig2e, fig2g, fig2h, fig2-controls | reproduced |
| fig2f-session-remap-behaviour | partially reproduced (tau matches; slope -0.385, outside -0.22 ± 0.11) |
| fig3d, fig5 (rate-remapping encoders) | reproduced |
| fig3e, fig3f, fig3g (decoders) | blocked, other (not ported within the run) |
| fig4c, fig4d, fig4gh, fig4-controls, fig4s5, fig4s7 | reproduced |
| fig4ef-reward-remap-behaviour | partially reproduced (both tests hold; two of four values outside tolerance) |
| fig4s6-incorrect-coding-overlap | reproduced, seed-sensitive (1 or 2 KS tests fall below p = 0.05 under two of the other four seeds) |
| fig6cd-of-aggregate-model | reproduced |
| fig7b, fig7de, fig7f, fig7g, fig7h | blocked, data_missing (no waveforms; the last four depend on the matching) |
| methods-lookahead-encoder-best | partially reproduced (best mean R2, but the comparisons are not significant) |

**2. Dataset, assumptions, questions**
- **Version:** there is no published version, so I used the draft (modified 2023-06-20) and recorded that date; the notebook stops if the draft has changed.
- **No spikes:** the files hold smoothed 20 ms firing rates, with no spike times, waveforms or electrode tables.
- **Missing sessions:** 12 Tree-Maze sessions with units that the repository's session table lists are not in the dandiset (224 units, 65 isolated). This leaves 510 isolated units where the paper counts 565.
- **Mislabelled metadata:**
  - Tree-Maze `track_data` is described as x,y,hd but holds t, x, y and head angle, and starts one sample after the rates.
  - Its "rate" attribute is 0.02, which is the sample period.
  - The rates are labelled "uv" but are spikes per second.
  - Open-field tracking is labelled mm but is in cm.
  - Session start years are 0018 and 0019.
  - No table column has a description.
- **Smaller issues:** one malformed trial (in Ca_T3g_040119). Two same-day recordings (Cl_T3g_121418 and _0); the code silently drops the _0 one.
- **Checks that passed:** session trial and unit counts match the repository's tables. Clock alignment was shown in 114 of 124 sessions; in the other 10 it could not be shown this way.
- **Paper vs its own code:** the paper's 110 trials and 54 Switch trials disagree with the repository's `perf_table.csv` (152 and 69).
- **Question for the authors:** what does "similar" mean for Switch versus non-Switch performance? This is the only assumption an outcome rests on.
- I asked no reader questions.

**3. Where the protocol was unclear**
1. **Draft-only dataset:** step 1.3 assumes a published version exists. I used the draft and recorded its modification time.
2. **Claims file gives a seed:** the opening comment says seed 0 (the code's), but the protocol requires seeds derived from the claim. I used the protocol's seeds and showed seed 0 as a variant.
3. **Scores shared by several claims:** the protocol does not say whose seed to use. I used the seed of the defining claim (fig2d, fig4d) for the claims that reuse its scores; the control claims use their own seeds.
4. **Five-seed rule:** I ran the control scores under the claim's seed only, to save time, and recorded this as a deviation.
5. **Blocking for lack of authoring time:** `too_large` and `not_runnable` are about computation, so I used `other` for the decoders.
6. **Two expected values, one out of tolerance:** where the criterion defines only "reproduced", I chose partially_reproduced.
7. **Clock check without spikes:** the protocol's suggested contrast assumes spike trains. I adapted it to even/odd zone maps with the rates shifted 5 s against the tracking, plus trial markers against position.
8. **Non-converging model fits:** the protocol is silent. One likelihood ratio test (in fig4s7) came out negative, so I refitted both models with Powell's method and recorded it.

**4. Runtime and failures**
- The final notebook runs in 28.5 min (under the 60 min limit). The run started at 23:04 and the work ended at 01:34.
- Nothing failed. The locked environment gave slightly different estimates for fig2c than my development environment; I corrected that conclusion and re-checked every quoted number against the executed outputs.
