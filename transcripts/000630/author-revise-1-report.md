I've worked through every point in the round-1 report and re-run the entry. `entry.py all` passes all three notebooks and `check` reports 0 errors. Nothing is committed.

**Outcome changes**

| Claim | Before | Now | Why |
|---|---|---|---|
| dandiset-cell-link | reproduced | partially reproduced | Not every record agrees: one file says sex "unknown" where the table says M, and two files give an age of 0 days where the table has none. The one age mismatch the verifier found came from my rounding; the files store whole years × 365 days, and on that basis all 208 known ages agree. |
| fig4b-adarb2-irregular-firing | partially reproduced | not reproduced | The criterion has no partial level, and the two parts that fail (i, ii) are the claim's point that only ADARB2 MC4R fires irregularly. |
| fig6a-ephys-dprime-subclass-structure | reproduced (assumption) | partially reproduced | The criterion needs both readings of "high", and the second one fails. I removed the assumption. |
| fig4d-mouse-no-rosehip-ephys | partially reproduced | not reproduced | Both failing parts fail under both readings, and the criterion has no partial level. Using all 272 mouse cells doesn't change this. |
| fig5d-mouse-pax6-doublets | partially reproduced | not reproduced | The criterion has no partial level. |
| fig3d-ephys-species | blocked (methods underspecified) | partially reproduced | It now runs on mouse VISp, as the claims file says. AP height is FDR p 3.4e-33 and 3.3e-34, above 1e-38 under both ANOVA readings, so the readings agree. Using every visual area, as the code does, is shown as a variant; there the readings still disagree. |
| fig1e-subclass-proportions | blocked (other) | blocked (metadata insufficient) | The public mouse table holds only cells of mouse L1 t-types. The test also needs the deeper t-types, so it can't be built from public data. |

**Outputs added for the verifier's questions**
- **Initial firing rate at rheobase + 40 pA:** the notebook lists the 31 cells where my value and the paper's differ, with sweep amplitudes from both sides. In 10 the sweep I used is another repeat of the paper's amplitude, 6 use another amplitude, 13 have no sweep here that gives the paper's value, and 2 have a value on one side only. This is the gap behind the fig2c partial result. The "agrees for at least half the cells" rule for using a computed feature is now stated as my own assumption.
- **Layer rule:** both rules match the paper's code. The classifier code uses the depth-table layer only (164 core cells, 177 for the mixture search); the cross-species code fills gaps from the LIMS layer (176). Each notebook says which rule it follows and shows the other. The mixture-model and classifier results now run on both feature readings and the filled layer, and all stay within tolerance.
- **fig3g** now runs on VISp (205 mouse cells), and still reproduces.
- **All 272 mouse cells** (using the paper's values) are a variant for fig3d, fig4d and fig5d. The 22 cells without a file are listed by specimen id. The missing fourth Lamp5 Krt73 cell is 710346584; it has no file and no values in the paper's table.
- **figs3a:** the slope sign and its meaning are printed. More sag means more change in upstroke, the opposite of the criterion's wording.
- **fig2c-lamp5-gradient:** the paper's code passes `filter_dropouts=False`, as I did; the default setting is shown as a variant.
- **figs6:** the low-power limits are now stated, with an age test without the dropout filter. No feature reaches significance either way.
- **Data availability for blocked claims:** nucleated-patch sweeps are in 38 human files and 25 mouse files. None of the 15 mouse TEa cells has a file in 000020. For figs8b, DANDI 000228 holds files from donors of 15 of the 17 held-out Szeged cells but has no cell identifier; no 000337 file matches a held-out Amsterdam cell.

**Questions added for a reader** (`questions/000630.yaml`): whether the figs3a direction misreads the paper's "inverse relationship", and whether the claims file should name DANDI 000228 as an input for figs8b.

**Record** (`attempts/000630-chartrand-2023-01.yaml`): updated notes and deviations, two new findings (the code uses all visual areas where the paper says VISp; the patch areas the conductance densities need are not deposited), and the round recorded under `verifications` (5 outcome disagreements). The README, `entry.yaml` runtimes and the helper docstring are updated to match.

**Not done**
- fig3f conductances are not computed. The densities need patch surface areas that aren't public.
- Linking the 000228 files to the held-out cells is not done. It would mean matching features within each donor, so figs8b stays blocked as the criterion requires.
- The `elsewhere` claims that were never attempted stay blocked as "not attempted". Their notes now say their inputs are public.
