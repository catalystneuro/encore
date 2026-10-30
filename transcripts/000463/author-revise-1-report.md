No outcome changed. The main finding is that the verifier was handed the wrong claims file. It reviewed against `claims/000946/10.1523-jneurosci.2218-24.2025.yaml` (33 claims, readings N1/N2, B1/B2, C1/C2), but this attempt is written against `claims/000463/...` (37 claims, readings O2 to O4). Its claim ids, partial rule and readings come from the other file, so I checked each of its points against this attempt's claims file. The workflow that builds the verifier's inputs should be looked at.

The entry re-ran with `python tools/entry.py all`: 0 errors, and the notebook passes in 246 s.

**Outcomes, all kept**
- **fig11-ac-unit-counts**: not reproduced. The verifier's numbers (633 against 453, and every per-PRF count outside 10%) give the same result.
- **fig11b-ac-prf-responses**: still partially reproduced, resting on the O2a normalization. The verifier would block it as `methods_underspecified`; I kept the outcome and recorded the disagreement.
  - Under this claims file, `judge()` uses this file's own rules ("at least 4 of 6", 300 Hz lowest in both windows, ×2 and O3c are listed readings). All six O3 × O4 readings under O2a give partially reproduced.
  - The verifier's point that the per-trial ratio (O2b) is biased by firing rate holds. A new synthetic check confirms it: with no stimulus effect, O2a gives 99.9 to 101.6% at 2 to 40 Hz, while O2b gives 13% to 127% depending on the rate. That is why O2a is kept as the assumption.
  - Because the header rule (disagreeing readings block a claim) hinges on whether O2b counts as a reading, I asked a reader in `questions/000463.yaml`.
- **fig4-unit-counts**: still blocked. The verifier would say not reproduced, using the other file's rule on per-area totals. This file compares 12 counts by type, and the new bound shows at most 6 of 12 could match under any typing. So the claim cannot be reproduced, but partially versus not reproduced still depends on the missing types.
- **All other blocked claims**: the verifier agrees with them.

**Added or corrected in the notebook**
- The recording labelled both S1 and POm (BH499_300_200_67_5_POM_S1) is now left out of all counts. The S1 total over five PRFs moves from 1648 to 1630, and the celltype_label count from 22617 to 22599.
- Spike times are checked to be in increasing order in every loaded file; none is out of order.
- The identifier's voltage field is 5 V in every recording that parses, so there is no 0 V sham. The 14 files whose notes name no main area are listed, with their identifiers and notes.
- One STTC file is opened and listed. Its pairs are indexed by unit, with no cell type.
- The S1 and POm counts are broken down by subject and PRF.
- Untyped AC by S1 pair counts are added for fig11c and fig11d: 15430 in all, 3760 at 30 Hz and 4303 at 3000 Hz. They are an upper bound only.
- fig11b is re-judged with each subject left out: partially reproduced or reproduced under every O2a reading, never not reproduced.
- Conclusions and record notes are updated to match the new numbers. Round 1 is recorded under `verifications`, with the claims-file mix-up stated in `reviewed`.

**Not done**
- I added no reader question for the verifier's point 8 (fig11b restricted to PD 200 µs). This attempt's claims file does not make that restriction, and the all-PD variant is shown.
- `methods-insitu-pressure` has no counterpart in the verifier's file, so it has no verification result.
- Nothing was committed. The untracked dotfiles in the repository root (`.bashrc`, `.idea` and others) are not mine and I left them alone.
