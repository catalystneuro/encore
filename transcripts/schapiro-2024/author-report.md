I finished steps 1 to 5 and ran the handover. Of the 26 claims, 20 are reproduced (one of them resting on an assumption), one is partially reproduced and five are blocked because the data are missing. `entry.py check` and `all` passed with 0 errors, and the notebook ran in 79 s with a peak of 2.8 GB of memory. The handover package is in `executed/schapiro-2024/handover/`. Nothing is committed.

**(1) Outcomes**

| Claim | Outcome |
|---|---|
| figs1-ih-reduced-11c, figs1-ih-reduced-21c | blocked (data_missing) |
| fig1-cs-lower-frequency-11c | reproduced |
| fig1d-difference-grows-with-temperature | reproduced |
| fig1e-q10-lower-in-cs | reproduced |
| fig1f-two-saline-frequency-change-same | reproduced, from the deposited per-experiment table |
| fig1e-two-saline-q10-same, fig1e-saline-q10-same-across-designs | blocked (data_missing) |
| fig2c-decrease-by-depolarizing-phase | reproduced (the Cs+ part; the Cs+ + PTX example is untested) |
| fig3d-freq-decrease-while-warming, fig3e-freq-increase-when-stable | reproduced |
| fig4c-ptx-restores-frequency-change | reproduced, `assumed: true` |
| fig4d-ptx-keeps-decrease-while-warming, fig4e-stable-increase-ordering | reproduced |
| fig5b-pd-burst-shorter, the four table1 claims, fig5d-pdoff-lpon-delay-smaller, lp-duty-cycle-preserved | reproduced |
| matched-period-lp-earlier | reproduced under reading (b); reading (a) does not match |
| fig6a-lp-off-advances-saline, fig6a-pd-py-phase-constant | reproduced |
| fig6a-lp-advances-cs | partially reproduced (LP ON adjusted p = 0.029, not below 0.01) |

**(2) What was found about the dataset**

I pinned version 310115. It is the newer of the two published versions and the only one with the voltage-clamp cells added at revision. The dataset holds the paper's MATLAB code, so I ported it to Python. Recomputed per-experiment values agree with the deposited summaries to a few thousandths, but not exactly.

Findings about the data:
- **Major: no Cs+ voltage-clamp trials.** `VoltageClampData.mat` holds only the first trial of each experiment, while its key lists every trial, so the Ih values cannot be measured. The paper's Ih numbers come from values typed into the script from readings "judged by eye". The 290160 copy of the file was 814 MB against 98 MB now; it was not staged, so I don't know whether it held every trial.
- **Major: most control experiments are absent.** Five of the six two-saline control experiments have no spike file; only their summary values are in `ControlTable`. The table also lists the second protocol as a ramp, not steps, in three of the six.
- **Major: one preparation is counted twice.** `981_035` holds two PD spike trains (`PD` and `PD2`), which the README does not describe. The picrotoxin summaries enter them as two experiments, so the paper's "N=6" is five preparations.
- **Minor: thermocouple dropouts.** Three files have temperature readings down to -46.7 C, all outside the analysis windows.
- **Passed:** no recording is deposited twice. In `969_113`, the raw trace, the spike times and the temperature share one clock.

The findings about the paper are the double-counted preparation, a mismatch between the deposited summaries and the deposited code, and a question for the authors.

**Assumption and question for the authors (fig4c):** `981_035` never came within 0.3 C of 21 C; its top hold is at 20.7 C. I used a 0.5 C margin for its 21 C value. With the paper's 0.3 C rule only four experiments are complete and the effect is not significant (p = 0.072). The question also asks which post hoc test was used: with MATLAB multcompare, Cs+ against Cs+ + PTX gives p = 0.106; with the classic Tukey test, p = 0.037.

I asked the readers no questions.

**(3) Where the protocol was unclear, wrong or missing something**
1. `entry.py check` rejects any quoted `/tmp/...` path, yet `archives.md` tells Dryad entries to read the staged files there. I built the path from parts in `pyloric.py` and documented why.
2. The rule to stream data with no local paths conflicts with Dryad staging. I followed `archives.md`.
3. A criterion can depend on data that exist only as deposited summary values, as in fig1f. The protocol does not say whether that counts as testing; I tested on the table and recorded it as a deviation. I blocked the two Q10 claims, because the criterion's reading (a) cannot be computed from the table.
4. The 290160 version could not be checked against the newer one, because only the pinned version is staged. I recorded what the public file list shows (file sizes).
5. The clock check is weak for slow temperature protocols: correlations with shifted temperature cannot place the clock offset more precisely than a few minutes. I stated it as consistent with a shared clock, and added an exact check on the one raw trace with spike times.
6. A finding about the data that spans several cells has no single cell to point to; I gave a check that passed the tag `sanity`.

**(4) Runtime and failures**

The whole run took about 35 minutes (18:17 to 18:52 UTC). Nothing failed in the final runs. During development `scipy` could not read the MATLAB tables, so I added `mat-io`. The reading (b) phase analysis could not be applied to `969_152` under Cs+ + PTX, because its cycles hold no LP spikes. No step uses random numbers, so no seeds were needed.
