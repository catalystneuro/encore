I've addressed all ten of the verifier's points, re-run the entry, and recorded round 1. The last run passes the checks and the notebook runs in 61 s; nothing is committed.

**Outcome changes:** 20 reproduced, 1 partially reproduced, 4 blocked (it was 19, 2 and 4).
- **fig4c-ptx-restores-frequency-change**: reproduced → partially_reproduced, as the verifier said. Under the criterion's 0.3 °C rule only four experiments are complete and the effect is not significant (p = 0.072). With a 0.5 °C margin the full pattern holds only under classic Tukey (p = 0.036). It fails under the multcompare reading the deposited code uses (p = 0.106).
- **fig6a-lp-advances-cs**: partially_reproduced → reproduced, marked as resting on an assumption. The deposited MATLAB is in the staged data, so I could check the burst code (problem 3). It deletes a removed cycle's start together with its frequency. The cycle before it (1.6% of cycles) then spans two or more bursts while keeping its own period. Leaving those cycles out brings the phases five to twelve times closer to the deposited summary values. LP ON in Cs+ then advances 0.053 per 10 °C with adjusted p = 0.0003; with them kept it is 0.010, p = 0.029, the result the verifier saw. I added a question to the authors about this. Round 2 reviews this change.
- **matched-period-lp-earlier** stays reproduced, but both readings now match, not only reading (b).

**Corrected or added:**
- **981_035 (problem 2):** the verifier was right. Its PD and PD2 trains burst together no more often than chance (14% against 13%) and run at different frequencies. They are two preparations sharing one temperature record, so the paper's N = 6 is correct. I rewrote that data finding (now minor) and the paper finding, and removed the "five preparations" variant.
- **Ih (problem 7):** the steps are placed correctly (12.000 s at -110 mV). The negative values come from a faster inward current that relaxes in the first few hundred ms. A new reading, the least inward current in the first second, gives Cs+ Ih near zero and saline Ih close to the authors' by-eye values for the same cells.
- **Cs+ + PTX example (problem 10):** 969_087 and 969_147 are extracellular only. The deposited script plots the example from 981_037, which has no spike file. On PD spikes detected on that trace, the depolarizing phase carries 0.96 of the period increase, so that part of the statement holds as well, outside the criterion.
- **Smaller points:**
  - The strict versus `<=` 0.3 °C bound comes from the deposited code; it is now stated, with a variant.
  - Reading (b) for the cycles at 11 °C now covers the whole holding period, and the slope reading (b) uses every cycle.
  - The whole-recording reading of the jag measure, including the cooling, now runs, plus a variant that smooths only within the window. All readings agree.
  - The clock check is now called weak. The outliers against the summary file are explained except two at 969_147.
- **New finding:** three raw recordings have no spike file and no documented condition.
- The "two step protocols" wording (problem 9) is now a reader question in `questions/schapiro-2024.yaml`; the claim is unchanged.
- I updated the README (25 preparations) and the description in `entry.yaml`.

**Not done:**
- I did not read the 814 MB `VoltageClampData.mat` of version 290160, because it is not staged here.
- How ControlTable's 11 °C, 21 °C and Q10 values were computed cannot be shown: no deposited code computes them.
- Two differences from the summary file (969_147 at 21 °C, in saline and in Cs+) remain unexplained.
- The attempt record was rewritten through a YAML dump, so its diff includes re-wrapped lines that did not otherwise change.
- `tools/publish_site.py` was already modified before this run and I left it alone.
