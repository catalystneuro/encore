I tested 31 of the 34 claims and blocked 3. `entry.py all` passed: the notebook ran from a clean environment in 25.5 minutes, and the handover is built in `executed/000939-duszkiewicz-2024/handover/`. Nothing is committed.

## 1. Outcomes

| Claim | Data | Outcome |
|---|---|---|
| cell-classes-counts | dandiset | partially reproduced. 1,661 excitatory, 430 FS and 1,512 HD cells, fraction 0.91, all within tolerance; vertical probes give 931 units, exactly the paper's number. Parallel probes give 1,760 units, below the 1,799 floor, because one session is missing. |
| ed2b, fig2a, fig2b, fig2c, ed2hi | dandiset | reproduced |
| fig2f-cue-rotation | figshare Dataset_3 | reproduced (99 FS cells, \|z\| = 8.52) |
| fig3c-adn-broader | figshare Dataset_5 | reproduced |
| fig3-ten-components-power | dandiset | partially reproduced. 0.989 with squared-modulus power; 0.872 with root-mean-square power, which misses. |
| fig3e-fourier-signatures-differ | figshare Dataset_5 | not reproduced, resting on an assumption. With the code's numeric cell-type coding the interaction gives p = 0.365; the direction of the effect holds. |
| fig3f-posub-hd-closer-to-fs | figshare Dataset_5 | partially reproduced. p is below 1e-9 under only one of the four readings. |
| ed3k-robust-to-controls | figshare Dataset_5 | partially reproduced. All three controls hold, but ADN-HD multipeak scores are lower than PoSub-HD, not higher. |
| fig3g-first-three-components | dandiset | reproduced, resting on an assumption (squared-modulus power) |
| fig3h-dominant-component | dandiset | partially reproduced. Counts 237, 146 and 47: the third misses 55 ± 6. |
| ed3g, ed3l, ed4a | dandiset | reproduced |
| ed4cd | figshare Dataset_5 | reproduced |
| fig4f-synaptic-weights-dispersed | dandiset | reproduced (CV 1.90) |
| ed7-adn-disinhibition, ed8e-adn-mixed-gain | figshare Dataset_6 | reproduced |
| fig5b, ed7gj | dandiset | reproduced |
| fig5e-hd-multiplicative-fs-additive | dandiset | partially reproduced. Under the exclusion reading "either test fails", HD additive factors differ from control. |
| ed8cd-multiplicative-detectable | dandiset | reproduced, resting on an assumption (noise titrated as the Methods describe) |
| fig6c-coupling-preserved-wake-rem | dandiset | reproduced, resting on an assumption (how glmfit's warnings are mimicked) |
| ed9d, fig7b, ed10b, fig7d | dandiset | reproduced |
| fig1ac-posub-border | figshare Dataset_4 | reproduced, qualitative |
| fig4-random-connectivity-simulation, fig4h-model-fit | none deposited | blocked: `methods_underspecified` |
| ed6-trn-innervates-adn | none deposited | blocked: `other` |

## 2. Dataset, assumptions and questions

**Version.** I pinned 0.261016.2310, the latest published version, because the paper cites no dandiset version. The notebook shows every file has the same unit, spike and head-direction sample counts as 0.250207.0025.

**What was found about the dataset:**
- It holds 31 of the paper's 32 PoSub sessions: all 14 vertical, 17 of 18 parallel.
- It holds 2 of the 5 ArchT mice of the PoSub optogenetic experiment. The other three (A1801, A1804, A1806) are only on figshare.
- In 8 files the optogenetic stimulus series stores four channels interleaved in one dimension, so its length is four times the session's; in A1808 it is a single 0/1 channel.
- There is no speed series and no table of light pulse times, so both had to be derived.
- The unit labels in the files follow the code's 0.35 ms trough-to-peak cut, not the Methods' 0.4 ms.

**Assumptions:**
- Fourier power is the squared modulus of the coefficient (the code's, and the only reading for which the paper's Parseval check holds).
- Cell type enters the Fig. 3e ANOVA as a numeric covariate, as in the code.
- The gain simulation's noise is titrated to the observed correlations, as the Methods say.
- glmfit's warnings, on which the code removes a pair, are taken as non-convergence or ill-conditioned weights.
- Isomap is fitted on at most 4,000 population vectors per session.
- Speed is computed from position.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings): the power definition, the numeric ANOVA coding, the gain-exclusion "and/or", the simulation noise and its control group, which glmfit warnings removed pairs, and how speed and the cue-rotation exclusion were defined.

**Question to a reader** (in `questions/000939.yaml`): the claims file says ADN-HD multipeak scores are higher. The legend gives no direction, and the paper's own counts of cells kept below 0.05 imply they are lower.

## 3. Where the protocol was unclear or wrong

1. **Elsewhere claims with nothing deposited anywhere.** The protocol forbids `data_missing` for `data: elsewhere` claims, but ed6's data are public nowhere. I used `other`; fig4 and fig4h became `methods_underspecified`.
2. **Claims the dandiset could partly support from figshare.** The figshare item holds the missing PoSub ArchT mice, but the protocol keeps dataset claims on the dandiset. I did not use those mice and recorded their absence as a finding.
3. **Criteria that leave cases undefined.** The fig3h criterion defines "partial" only when all counts hold. Two of three counts held, so I recorded partially reproduced and explained why.
4. **Results notebook text.** Result cells are markdown, so after the run I edited three of them. I copied the same edits into the executed copy and checked that every code cell was identical, so I did not need a second 25-minute run.

## 4. Runtime and failures

- The run took from 18:23 to 20:04 UTC; the notebook alone takes 25.5 minutes, 10 of them in the GLM fits.
- Nothing failed in the final run.
- During development I fixed the A1808 pulse format, the sign of the virtual-HD offset, and the GLM ill-conditioning check.
