I finished steps 1 to 6 on DANDI:001518, pinned at version 0.261006.1957: the entry, the attempt record and the handover. `entry.py all` passes with 0 errors. The notebook runs in 898 s, most of it streaming the 190 files. Nothing is committed.

The main problem is the field strength. The files give the pulse in volts (25 to 250 V); the paper gives V/cm (43 to 1400 V/cm), and no source gives the factor between them. The voltages span a factor of 10 and the paper's levels a factor of 33, so the dataset cannot hold the paper's full escalation. I ran two readings: 25 V = 43 V/cm (`bottom`) and 250 V = 1400 V/cm (`top`). Using the paper's dye sensitivities, the low-field response of each dye gives 1.5 to 1.6 V/cm per volt, close to `bottom` (1.72) and far from `top` (5.6). I adopted `bottom` as a stated assumption; it puts the dataset at 43 to 430 V/cm and shows `top` as a variant. This check uses the paper's own calibration, so it supports the reading without proving it.

**(1) Outcomes**

| Claim | Outcome |
|---|---|
| fig3-dye-sensitivity | partially reproduced: FluoVolt 23.98 (26 ± 2.6), Di-8-ANEPPS 10.52 (9.1 ± 0.91), both r within tolerance; no single reading passes both slopes |
| fig3-fluovolt-nonlinear | not reproduced: FluoVolt departs from the line from 220 mV as stated, but Di-8-ANEPPS departs too |
| fig2a-fluovolt-saturation | not reproduced: 25.5% against 66% at 360 V/cm |
| fig2a-fluovolt-stable | not reproduced: one baseline drift of −2.65%, p = 0.010 |
| fig4a-fluovolt-limits | not reproduced: maxima 35.3% and −49.5% against 71% and −83.5% |
| fig4a-fluovolt-cathodic-decline | not reproduced |
| fig5b-conductivity-calibration | partially reproduced: Eq. (2) gives 1.33% (paper: about 2%) and 11.87% (paper: 12%) |
| fig1, fig2b ×2, fig4b ×3, fig4c, fig7b (8 claims) | blocked, data_missing: no sets at 570 V/cm or above under the adopted mapping. The `top` results are in the notes; most of them fail |
| fig2cd, fig2c-1000, fig2d, fig4d, fig5a ×4, fig5c, fig6a, fig6b ×2, fig7ab, fig7c ×2 (15 claims) | blocked, data_missing: the experiments are not in the dandiset |

**(2) Dataset, assumptions and questions**
- **What it holds:** ten escalations of 1-us pulses in 19 steps each, 5 with FluoVolt (the paper has n = 4) and 5 with Di-8-ANEPPS, all recorded on 2025-01-24. None of the alternating, 0.3-us, Gd3+, Ca2+ or two-pulse experiments are in it.
- **Electrode distance:** the files say 1.00 mm; the paper says 1.6 mm.
- **Several cells per image:** each field holds 3 to 6 cells, while the paper analysed one per experiment and does not say which. I ran three readings: the mean of each experiment's cells, the cell nearest the image centre, and every cell.
- **Missing from the files:** pixel size, field direction, field strength. The field direction (cathode side at the bottom of the image) and the pulse onset at image 41 are clear from the data.
- **Dark frames:** frame 0 is dark in 175 of 190 sets, plus 51 other dark frames; these are laser misfires and are left out.
- **No duplicate recordings** were found.
- **Assumptions:** the `bottom` mapping; a pixel size of 0.267 um (16-um camera pixel over the 60x objective); background subtraction from a cell-free region.
- **Outside input:** tau = 44.5 ns/um × R, taken from reference [20] (doi:10.1016/j.bioelechem.2025.109143, open access).
- **Questions for the paper's authors** (recorded as a methods_unavailable finding): what V/cm each voltage corresponds to; which cell was analysed; whether background was subtracted; the pixel size.
- **Paper inconsistency:** Eq. (2) with the Methods constants gives 1.3% for a 10-fold rise, not the stated 2%.
- **Questions to a reader:** none.

**(3) Where the protocol was unclear**
1. The volts-to-V/cm gap is missing metadata, not a method, and step 1.6 covers methods. I handled it as readings plus an assumption, with a check against the data.
2. The schema forbids `assumed: true` on blocked outcomes, and requires deviations wherever `assumed` is set. The 8 blocks that rest on the mapping say so in their notes instead.
3. When the claims file names many readings that cross (32 combinations for fig3), it does not say whether "under one reading" means any single combination. I took it to mean that.
4. It does not say what to do when a criterion fails on the data present but needs levels that are missing. I used not_reproduced when the failure held under both mappings, and blocked when the deciding levels were absent.
5. Absence claims are "judged on the paper's test alone", but the claims file still names readings (time windows, which cell). I ran all of them and decided on the adopted one.
6. The data check of the mapping relies on the paper's calibration, which is itself a claim (fig3). The protocol does not address this circularity; the notes state it.

**(4) Runtime and failures**
- The run went from 21:02 to about 22:21 UTC.
- The first `all` failed the schema check (17 errors, the issue in point 2). I fixed it and reran, and everything passes.
- The harness left an `entries/001518-semenov-2026/.claude/.cc-writes` directory in the entry. Removing it needed approval and was denied, so it is still there and should be removed before commit.
- The untracked dotfiles in the repository root are sandbox mounts, not files I created.
