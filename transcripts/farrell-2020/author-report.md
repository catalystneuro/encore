I've done steps 1 to 5 of the Author section on CRCNS ear-1 and built the handover (step 6). The entry is `entries/crcns-ear-1-farrell-2020/`, the record `attempts/crcns-ear-1-farrell-2020-01.yaml`, and one question for a reader is in `questions/crcns-ear-1.yaml`. `entry.py all` passes from a clean environment (0 errors, notebook 32 s). Nothing is committed.

**(1) Outcomes** (48 claims: 19 reproduced, 9 partially reproduced, 13 not reproduced, 7 blocked)

| Outcome | Claims |
|---|---|
| Reproduced | cohort, figs1-example-cell, clw-by-turn, fig1-two-state-bounds, alpha-pigmented-vs-albino, alpha-gradient-pigmented, table1-albino-no-gradient, figs2-alphab-vs-clw*, v05-by-turn, table2-xe991-v05-shift, table2-pigmented-xe991, table2-pigmented-no-xe991, table2-albino, v05-not-correlated-voltage-drop*, tables3-by-region, figs5-specific-capacitance*, fig4e-sensor-charge, table3-pathway-energies, recording-time* |
| Partially reproduced | fig1-charge-not-linear, table1-pigmented-xe991, table1-pigmented-no-xe991, table1-xe991-no-effect-alpha, fig2b-v05-vs-clw, xe991-voltage-clamp, capacitance-asymmetry*, fig4a-vh-rises-vd-constant, two-hyperpolarized-states* |
| Not reproduced | nlw-capacitance, fig2b-no-phenotype-difference, v05-gradient-length, fig3a-eq3a-fit, fig3a-xe991-fit, fig3a-high-density-deviation*, figs4-fine-bins, fig3b-negative-clw-fit*, mean-slope-half*, fig4d-cleq-two-limits, fig4c-sensor-area, alternative-limit, low-chloride-similar |
| Blocked, data missing | splice-isoform-x1, molecular-model |
| Blocked, other (values in other papers, not supplied and not fetched) | fig3a-other-rodents, fig3c-engineered-mice, fig4f-all-rodents, figs7-hearing-loss, v05-temperature-corrected |

\* marked `assumed`: the outcome rests on a test or rule the paper does not give.

**(2) The dataset, assumptions and questions**
- **Version:** pinned `ear-1/live/data_and_scripts.zip` as `unversioned` (MD5 9955733f…). It is the copy the file list names, and its description (v0.62) cites this paper. The copy under `old/ver1` was not read.
- **Contents:** all 89 cells, with the paper's eight group counts exactly. The stored per-cell CL, QTm, V0.5 and alphaB equal the Fig. S1 legend for cell 99, so I used them. No recording is deposited twice.
- **Not stored:** CLW, CLn, the stereocilia capacitance CSB, and which cells form each table. Counts differ slightly from the paper's: 27 against 28, 5/12 against 4/11, 69 against 70.
- **Findings recorded in the attempt:**
  - The HDF5 `I_mean` array stores its values in column order under a (N, 2) shape (format error).
  - File 52 holds at +0.06 V where the description says -0.06 V.
  - The stored surface area follows two formulas.
  - The MATLAB `toxins` field labels 5 of the 20 XE991 cells `yes`.
  - 13 original cell numbers are used twice.
  - The conductance at V0.5 is about 8.5 nS, not the paper's 335 pS.
- **Assumption:** CLn is the mean C of the two most negative ramp points (this gives the legend's 25.94 pF). The plateau threshold is the one whose count matches the paper's 62 cells; every threshold is shown.
- **Question for the paper's authors** (`methods_unavailable` finding): how CLn and the per-cell CSB were computed.
- **Question for a reader:** the claims file takes CLW = CL - 4.82 pF. Fig. S1 implies 5.89 pF (24.45 - 18.56), which fits Eq. 8c adding a per-cell CSB. With 5.89 pF the Fig. 3a fit matches the paper on all four values (Vd 0.032 V, slope -0.37 to -0.41), along with Fig. 1's R² and Fig. 4a's threefold rise. Outcomes stay as tested on the claims file, and the variant is shown throughout.

**(3) Where the protocol was unclear**
1. No `blocked_by` fits outside values that are public in published papers but not supplied to the run. I used `other` and explained it.
2. Several criteria have no partial tier (fig1-charge, xe991-voltage-clamp, capacitance-asymmetry, fig4a), and two-hyperpolarized-states fits none of its tiers. I picked the closest tier and said so in the notes.
3. The "same clock" check assumes trial tables. This dataset has voltage ramps, so I checked that the capacitance peak lies at the stored V0.5 (79 of 89 within one ramp step).
4. archives.md does not say which of two copies of a CRCNS dataset to pin. I chose the live copy and gave the reason in the header.
5. The protocol does not say whether analysis scripts deposited inside a dataset count as "the paper's code". I cited them only to explain how the stored values were computed, and took no method from them.

**(4) Runtime and failures**
The work took about 30 minutes (11:49 to 12:19 UTC). The notebook runs in 32 s. Two mid-run failures, both fixed:
- Ramp detection broke on file 52, which holds at +0.06 V.
- The first handover attempt failed because my test venv was still active, so `tools/entry.py` could not import yaml.

The harness left untracked dotfiles at the repository root and an empty `entries/crcns-ear-1-farrell-2020/.claude/` folder. They are not mine and I left them.
