I wrote `claims/watson-2016.yaml`, one file covering both datasets. The quote checker reports 53 claims, 52 quotes, 64 statistical values and 0 problems, and the file passes `schemas/claims.schema.json`. It is not committed, as asked.

**Text read.** I read the accepted author manuscript (PMC4873379, NIHMS776601), not the version of record. That covers the main text, Experimental Procedures, legends of Figs. 1 to 6, and supplement 1: Table S1, legends of Figs. S1 to S5, and the Supplemental Experimental Procedures. Supplement 2 holds only the Figure 1 artwork. I rendered one page of the supplement PDF (Fig. S5) to tie its printed R and p values to the right panels. The paper links no analysis code. Every claim lists both `000041` and `crcns-fcx-1`, since both archive descriptions say they hold the paper's full 27 sessions.

**Counts.**
- 53 claims; 52 have a quote. `tables1-state-durations` has an `inferred` note instead, because its values appear only in Table S1.
- 33 claims carry statistics, 58 entries in all. The checker's count of 64 also includes p-values.
- All 53 have a criterion; 20 have expected values.
- Ids come from the two earlier files. Where those files named the same finding differently, a mapping in the header lists the id kept and the one dropped.
- Two claims are new: `tables1-state-durations` and `fig4-late-packet-sigma-delta`.

**Details the paper leaves open, and the readings named for each:**
- **Sampling unit for correlations against normalized time:** one point per packet, per 10 s bin, or 50 bins averaged. I checked that the R and p printed in Fig. S5A/B match exactly 50 points. Fig. S3C matches about 873 points, roughly one per packet.
- **Cells in two WAKE-SLEEP cycles:** one entry per cell and episode, or one per cell averaged over episodes.
- **"General WAKE rate" for sextiles:** session-wide WAKE or each cycle's WAKE. For the rate groups of Fig. 2F: WAKE or nonREM sextiles.
- **Sextile numbering** runs in opposite directions in Fig. S2 (1 lowest) and the Fig. S5 legend (1 highest), so criteria name sextiles by rate.
- **"Wilcoxon test":** signed-rank or rank-sum.
- **Fig. 5B per-sextile test:** Wilcoxon signed-rank or t-test.
- **Fig. 4E within-UP comparison:** first against second third, or first against last third. The rank-sum unit is UP states or cells.
- **WAKE after SLEEP:** the next scored WAKE, or the >120 s arousal that ends SLEEP. **"WAKE" between packets:** scored WAKE, or any arousal over 40 s.
- **Definitions the paper never gives:**
  - The UP/DOWN ratio (duration ratio or time ratio).
  - REM theta power (scoring ratio or 5 to 10 Hz power).
  - The WAKE movement measure (motion mean, fraction above threshold, or EMG).
  - "Proportionally larger" for REM duration (three readings).
  - The final portion of a packet (last 20 s or last tenth).
  - Spindle "from ... to" (first and last tenth or third).
- **Autocorrelogram decay model:** power law to 100 or 500 ms, or exponential.
- **Synchrony per-cell measure:** firing together with another cell, or the cell's own firing fraction.
- **Range for "spans 0.05 to 5 Hz":** three percentile ranges.
- **Within-WAKE sextile trends:** the Pearson trend printed in Fig. S5A, or the change at entry to WAKE. The printed Fig. S5A values contradict the Results sentence.
- **Absences with no named test** are judged on the paper's correlation at p ≥ 0.05. Several tests the paper doesn't name use a standard choice, labelled as one.

**Inconsistencies inside the paper** (recorded in the claims, not fixed):
- Spindle incidence is 1.94/min in the Results but 0.049 Hz (2.94/min) in Table S1. The claim is judged on the Results value.
- The packet spindle-incidence R is printed as 0.7, read as a likely misprint for 0.07.
- The WAKE slope interval is printed as "0.801 – 0.0856"; the S3A legend's 0.80 to 0.86 is used.
- "0.05 to 5 Hz" is called three orders of magnitude.
- The "other" fraction is said to increase with R = −0.04.

**Missing from what was supplied.** There is no PDF of the main paper. Values printed only inside Figs. 2 to 5 could not be read:
- per-sextile R and p of Figs. 3B and 4A-B iv;
- the triplet n per class and the asterisks of Fig. 5B;
- the significance marks of Fig. 2F.

Those claims rest on the Results and legends. The Supplementary Methods that Fig. 2F cites for its significance test do not describe it.
