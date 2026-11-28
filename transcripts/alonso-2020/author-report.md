I've finished steps 1 to 5 of the Author section and run the handover (step 6). `entry.py all` passed: 0 check errors and all three notebooks ran in about 58 min. The handover package is in `executed/alonso-2020/handover/`. Nothing is committed.

The dataset is code, not recordings: one zip with the authors' Java model, their Python scripts and one parameter file per model network. So every claim is tested by simulating the deposited models. I ported the Java to Python with numba (`pyloric.py`), and it matches the deposited Java to within 3e-9 mV.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| deposit-models | not reproduced (3 of 38 models within tolerance at 10 °C) |
| fig1c-frequency-q10-phase-constant | partially reproduced (Q10 1.93 to 1.98; LP duty cycle not constant) |
| fig1s1-three-models | not reproduced (constancy fails in all three) |
| all-models-compensated | partially reproduced (36 of 38), assumed |
| intermediate-temperature-failures | blocked, data_missing |
| figs2-ramp-largest-isi | reproduced |
| figs3-duty-cycle-variable-across-models | reproduced, on the criterion's 16-temperature variant |
| fig2-lp-spike-amplitude-threshold | partially reproduced (amplitude falls; threshold reading (a) does not rise; (b) not computed) |
| fig2s1-peak-voltage-diverse | reproduced |
| fig3-current-amplitudes | partially reproduced (4 of 5 parts; KCa ratio 8.9, expected 6 ± 0.6) |
| fig4-currentscapes-reorganize | not reproduced |
| currentscapes-dominant-currents | reproduced |
| fig5-a-to-kca-tradeoff | reproduced (FGFKQS) |
| fig6-crash-different-mechanisms | not reproduced (FGFKQS PD still spikes at 30 °C), assumed |
| fig6s1-crash-mechanisms | not reproduced (7 of 8 models; 5 distinct patterns), assumed |
| fig7-high-temperature-slow-timescales | blocked, data_missing (3 of 5 models absent) |
| fig8a-hysteresis-quiescence | reproduced (1.94 °C) |
| fig8-up-down-ramps | blocked, too_large (first reading gives 22 of 38; second reading not run) |
| fig8b-pathological-attractor | not reproduced (17.1 °C and 11.3 s), assumed |
| fig9a-remove-a-current | partially reproduced, assumed |
| fig9b-remove-kca-current | reproduced (FGFKQS), assumed |
| fig10a-graded-removal | partially reproduced (3 of 5), assumed |
| fig10b-complete-removal-differs | not reproduced (H same and quiescent in 31 of 38, criterion asks 33), assumed |

## 2. Dataset, assumptions and questions

**Dataset** (Dryad version 94811, the only published version, so the one pinned):
- It holds 38 models, where the paper says 36. Nothing in the files says which 36 the paper studied. The 38 share 27 distinct sets of maximal conductances.
- Four models named in the Methods are absent: Q8FBN1, G81PUL, G7EOZ8 and SAXT8Y.
- Four are filed under other spellings: 0SHNMD (OSHNMD in the Methods), B7SD0L (B7SDOL), KMNLBC (KNMLBC) and 4X6W66 (printed with a symbol in its second place).
- At 10 °C the models burst at 1.25 Hz on average, against the Methods' 1 Hz target.
- The deposited integrator returns NaN for 6 models at some temperatures from 26 to 35 °C. The deposited Java does the same.

**Assumptions**, recorded as deviations:
- A spike is an upward crossing of -20 mV.
- "Fired in the right order" for the triphasic class is tested on the median LP and PY burst onset phases. Requiring the order in every cycle gives 35 of 38 compensated models instead of 36.
- The lag d of the classification scheme is the median time from the last -50 mV crossing to each spike.
- The deposit has no ramp code, so I implemented the ramps myself (linear, starting from the deposited initial conditions).

**Questions for the paper's authors** are recorded as a `methods_unavailable` finding: the spike threshold, the order test, how d is formed, how the ramps and the high-temperature states were run, and which 36 models are the paper's.

**Questions for a reader:** none. I found no place where the claims file misreads the paper.

## 3. Where the protocol was unclear or did not fit

1. Step 2's checks of clocks and trial alignment have nothing to apply to in a deposit of code and parameters. I checked the port against the deposited Java instead, inside the notebook, when a Java compiler is present.
2. archives.md asks for the SHA-256 that Dryad's file list gives, but the list gives only an MD5. I check the MD5 and print a SHA-256 that I computed.
3. The entry's hash covers markdown cells, so writing the conclusions after a run forces another full run, about 60 min here. Because the simulations are deterministic, I ran the notebooks once while preparing, wrote the conclusions from those numbers, and then made a single official run. The numbers came out identical.
4. When the criterion says "reproduced under any reading" and one reading is too large to run, the protocol does not say whether to report the reading that ran or to block. I blocked fig8-up-down-ramps as too_large and gave the first reading's result (22 of 38) in the notes.
5. The protocol describes the runner as 4 CPUs, but 4 processes gave only about 2 times the single-process throughput. I measured this on a subset and used it for the time estimates. Because of it, three things were cut down or left out:
   - the ramp reading of figs3, which I recorded as a deviation;
   - fig2, which ran 26 of the Methods' 101 temperatures;
   - the second ramp reading of fig8-up-down.
6. Several claims say "all 36 models" while the deposit holds 38. I used all 38 and noted it in the deviations.

## 4. Runtime and failures

- The session took about 2 h 45 min. The official run took 13, 32 and 13 min for the three notebooks.
- During development, the first runs of the main notebook failed in three places, all fixed before the official run:
  - an empty slow-wave crossing list in the classification;
  - numba raising on a division by zero, which I set to follow IEEE arithmetic as the Java does;
  - a NaN model mask in fig6s1.
- Nothing failed in the official run.
- Untracked dotfiles that I did not create (`.bashrc`, `.vscode` and others) are in the repository root. I left them alone; the workflow should not commit them.
