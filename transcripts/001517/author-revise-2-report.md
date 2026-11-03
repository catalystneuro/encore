No outcome changed and none is proposed: 5 reproduced, 3 partially reproduced, 8 not reproduced, 15 blocked. The verifier agreed with all 31 outcomes in round 2, and nothing I added suggests any should change. The final re-run passed (821 s) and `tools/entry.py check` reports 0 errors. Nothing is committed.

**Statements the verifier said the numbers did not support, now corrected**
- **Cell 0:** the header now says three used sets were re-traced, not two.
- **Cell 21 (fig2a):** now says the anodic pole does grow past 570 V/cm, by 2.4 points at 780 V/cm, which is within the tolerance.
- **Cell 75 (fig5b):** the direction is fixed. Eq. (2) gives a smaller reduction at 10-fold (1.33% against 2%), so its curve lies about 0.7 point above the paper's value, not far below it.
- **Summary, cell 81:**
  - The "poles dim before the regions nearer the equator" sentence now says that 16 of 24 equatorial arcs also fall below the calculated IMP, and that the 270° arc is already low at 570 V/cm.
  - The within-set decline is now said to hold from 1000 V/cm; at 780 V/cm it cannot be told from bleaching (net −3.3% against −2.6%).
  - The volts-mapping evidence is now called a single noisy step (per-cell ratios 1.38 to 4.04).
- **Attempt record:** the radius range now matches cell 5 (7.8 to 15.1 µm), and the Pearson values for the local backgrounds now match cell 41 (0.012 to 0.137, and 0.005 and −0.02).
- **README:** it now says which claims get the pixel and volts variants. The table marks fig2b-di8-bleaching as fragile (38 of 56 subsets) and fig7b as holding only with the volts matched in order.

**Outputs added**
- **Side fits without the 43 V/cm sets (cell 45):** the Di-8-ANEPPS cathodic slope rises from 3.13 to 4.59 and the anodic falls from 11.63 to 10.15. So the bleaching points explain only part of the asymmetry, and the anodic side also bends (0.58 to 0.80 of its own line). Cell 47 and the record now say both.
- **Measured against calculated IMP at 43 and 150 V/cm under every background band (cell 51):** in the 14 to 20 px band the anodic pole is below the calculated value at 150 V/cm (−191 against −205 mV, p = 0.019). The cathodic difference is not significant (p = 0.35). Cell 52 and the record now give these numbers.
- **A second outline for the Di-8-ANEPPS cells (new section before the Summary, with overlays):** this answers the verifier's new point that the c7, c10, c12, c13 and c14 outlines cut inside the membrane. The new tracing in `strobe.py` follows the outer membrane and is smoother. Under the adopted far background it changes none of the four affected claims: first-10 maximum 45.5%, anodic value at 1400 V/cm −23.1%, 16 of 24 arcs still differing, and fig4b-di8-limits still failing. The adopted outline is kept.

**Also updated**
- Round 2 is recorded under `verifications` in the attempt record, with the verifier's reasons and my responses for all 31 claims.
- The notes of the four Di-8-ANEPPS claims now include the outline variant's results.
- `runtime_minutes` in `entry.yaml` is now 14, up from 7.

**Not done, and why**
- The volts mapping, the background distance, the pixel size and which five Di-8-ANEPPS cells the paper used are still open. The data cannot settle them, so they stay as stated assumptions, with questions to the authors in the findings. Several not-reproduced outcomes still hold only under the adopted far background band.
- The verifier reported no place where the claims file misreads the paper, so `questions/001517.yaml` is unchanged.
