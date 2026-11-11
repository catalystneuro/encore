I re-ran every claim the answer affects under the amended claims file. Two claims changed outcome and three no longer rest on an assumption. The entry passes `python tools/entry.py all` (0 errors, the notebook runs in 110 s) and the verifier package was built with `handover`. Nothing is committed or pushed, and I did not verify my own work.

## The question and the answer

**fig1c-total-suppression** (baseline windows and the 0/0 ratio): the reader changed the claims file in part, in its opening comment only.
- **Windows (detail 1):** interval fear and total fear now have separate windows. The readings (interval, total) are (a) 2 s and 10 s, (b) 2 s and 20 s, (c) 10 s and 20 s. The plot in Figure 1, figure supplement 1A uses the total fear window. The old single-window readings (2 s or 10 s for both ratios) are gone.
- **0/0 (detail 2):** setting it to 1 is added as reading c.
- **No criterion changed.**

**What the answer changed in the attempt.** The reading I used as primary (2 s / 20 s, 0/0 = 1, trial baseline) was earlier outside the claims file's readings and recorded as a deviation. It is now one of the listed readings. All 18 amended regression readings and every behavioural reading are run. The old same-window readings still appear in the notebook, labelled "former", but no longer count towards outcomes. The notebook, `pag.py` docstring, README, summary and attempt record are updated, and each affected claim's notes say what the answer changed.

## Outcome per affected claim (earlier → now)

| Claim | Earlier | Now | What changed |
|---|---|---|---|
| fig1c-total-suppression | reproduced | reproduced | All 8 readings match. Measured values now use the first reading the criterion lists (0.768, 0.502, -0.002; earlier 0.799, 0.531, 0.030), and the deviation is withdrawn |
| fig1c-nonlinear-scaling | reproduced | reproduced | Holds under all 8 readings |
| fig1d-interval-suppression | reproduced, assumed | reproduced, assumed | The adopted 0/0 = 1 rule is now a listed reading. 4 of 8 readings reproduce, 4 are partial |
| fig1s1a-nose-poke-rates | partially, assumed | partially, assumed | The adopted 20 s window is now readings b and c. The 10 s window (reading a) would reproduce |
| fig1s1b-sr-poke-correlation | reproduced | reproduced | Holds under all readings |
| fig5a | reproduced | reproduced | Holds under 18 of 18 readings |
| fig5bc | reproduced, assumed | reproduced, assumed | Holds under 17 of 18 |
| fig5d | reproduced, assumed | reproduced, assumed | Holds under 7 of 18 (was 10 of 18). Every type-baseline reading fails |
| fig5s1-regressor-combinations | reproduced, assumed | reproduced, assumed | Holds under 9 of 18. It now depends only on the firing baseline (detail 4) |
| fig5e | reproduced, assumed | reproduced, assumed | Holds under 14 of 18. The peak is at 0.375 under all 18 |
| fig5s2-binary-regressor | reproduced, assumed | **reproduced, no longer assumed** | Holds under 18 of 18. The readings that failed were the old 2 s ones |
| fig5f-ramping-last-interval | reproduced, assumed | **reproduced, no longer assumed** | Holds under 18 of 18 |
| fig5gh | reproduced, assumed | reproduced, assumed | Holds under 9 of 18 (was 6 of 18) |
| fig5i | reproduced | reproduced | Holds under 7 of 18, and the criterion asks for one. Measured values now use the first matching reading listed: 0.686, 0.045, -0.062 (earlier 0.577, 0.120, -0.026) |
| fig5s1-ramping-regressor-combinations | partially, assumed | partially, assumed | It held in full only under the old 2 s readings. Total fear alone now differs from zero under all 18 readings. It rests on the trial baseline |
| fig5j-ramping-tuning-curve | reproduced, assumed | **reproduced, no longer assumed** | Peaks at 0.625 under all 18 readings |
| fig6c, fig6d | reproduced | reproduced | Hold under all 18 readings |
| fig6ef | partially, assumed | partially, assumed | Two readings would now be "not reproduced" (earlier one) |

The `methods_unavailable` finding on the poke baselines is still there, reworded to the amended readings. It is still a question for the paper's authors.

Files changed: `attempts/wright-2019-01.yaml`, `entries/wright-2019/reproduce_wright_2019.ipynb`, `entries/wright-2019/pag.py` and `entries/wright-2019/README.md`. The lock file came out unchanged.
