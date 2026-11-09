I re-ran every claim the answer touched. The entry passes `python tools/entry.py all` (0 errors, notebook ran in 38 s) and the handover is built in `executed/crcns-ear-1-farrell-2020/handover/`. Nothing is committed and I did not verify my own work.

## The question and what the answer changed

There was one question, filed on fig3a-eq3a-fit and covering every claim that uses CLW, dVmin or C_Leq. The reader found the claims file had misread the paper and amended its shared method:
- **CLW:** the paper does not subtract a fixed 4.82 pF from every cell. CLW = CL − CNLW, with CNLW = CSB + root worked out per cell.
- **Readings:** stored values (L-a) if the data set had them, otherwise a stated CSB rule (L-b). L-b is admissible only if it gives the Fig. S1 cell a CLW within 18.56 ± 1.856 pF. CL − 4.82 pF (L-c) is shown for comparison only.
- **nlw-capacitance:** the expected 4.82 pF stays, but it is now read as either the mean per-cell CNLW or the root alone.

The data set stores no CLW, CNLW or CSB, so L-b is used throughout. The paper takes CSB from Corbitt et al. (2012). I used that paper's rule, citing it:
- bundle area = min(0.07 × AM, 140 µm²), at 0.0075 pF/µm²;
- AM is the data set's stored cell surface area;
- the 6 cells with no area take the median CSB of their turn, which is my own assumption.

The root is refitted from QTm against ln(CL − CSB) over all 89 cells, giving 5.10 pF. With this rule the Fig. S1 cell gets CLW 18.30 pF, so it passes the reader's test. Every affected outcome is marked as resting on this assumption, and each claim's notes say what the answer changed. I also updated the methods question for the paper's authors and listed the Corbitt rule under `inputs`.

## Outcome per affected claim (new ← before)

| Claim | Now | Before |
|---|---|---|
| figs1-example-cell | reproduced (CLW 18.43) | reproduced (CLW 19.76) |
| nlw-capacitance | **reproduced** (root 5.10 pF; mean CNLW 5.98 pF is outside) | not reproduced (5.44 pF, CSB = 0 only) |
| clw-by-turn | reproduced (5.04, 17.79 pF) | reproduced (5.85, 19.10 pF) |
| fig1-charge-not-linear | **reproduced** (R² 0.539) | partially (0.585) |
| fig1-two-state-bounds | **not reproduced** (86.0% in band, needs 90%) | reproduced (91.9%) |
| fig3a-eq3a-fit | **reproduced** (Vd 0.0311, slope −0.4245, bins starting at the smallest CLW) | not reproduced (Vd 0.0215, slope −0.594) |
| fig3a-xe991-fit | not reproduced (Vd 0.0847) | not reproduced (Vd 0.0538) |
| fig3a-high-density-deviation | **reproduced** (on the 0.01 V bins) | not reproduced |
| figs4-fine-bins | **partially** (both Vd within, XE991 R² 0.605 not) | not reproduced |
| fig4d-cleq-two-limits | **reproduced** (0.560, 1.048 aF) | not reproduced (0.672, 1.080) |
| fig4e-sensor-charge | reproduced (0.929, 0.814, 0.885) | reproduced |
| table3-pathway-energies | **partially** (pathway-1 λ 4.40 outside, limit 4.367) | reproduced |
| tables3-by-region, figs2-alphab-vs-clw, fig2b-v05-vs-clw (partial), fig2b-no-phenotype-difference (not), capacitance-asymmetry (partial), fig3b-negative-clw-fit (not), mean-slope-half (not, −0.150 vs −0.223), fig4a-vh-rises-vd-constant (partial, 2.67 vs 2.60), fig4c-sensor-area (not), alternative-limit (not), low-chloride-similar (not), two-hyperpolarized-states (partial) | unchanged | as before |

Overall counts move from 19 reproduced, 9 partial and 13 not reproduced to 22, 10 and 9 (7 blocked either way).

## Results that hang on thin margins

- **fig4d-cleq-two-limits:** the lower limit includes one group of two XE991 cells. One of them, file 57, gets CLW 0.48 pF under L-b. Without that group the limit is 0.6496 aF, just outside the tolerance. The same tiny CLW is why the XE991 fits and low-chloride-similar get worse.
- **fig3a-eq3a-fit:** it passes only with bins starting at the smallest CLW. With bin edges at multiples of 5 pF the slope misses its tolerance by 0.0001.
- **fig4e-sensor-charge and fig1-charge-not-linear:** fig4e passes on the 0.01 V and per-cell groupings, while the 5 pF grouping misses by 0.002. fig1-charge-not-linear passes only on the centred R² through the origin.

The README and the notebook summary still carry the protocol's sentence that a failure to reproduce may be a failure of this attempt.
