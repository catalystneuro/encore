I wrote the claims file at `claims/crcns-hc-13/10.7554-elife.27621.yaml`. The quote checker reports 32 claims, 32 quotes, 31 statistical values and 0 problems. Nothing is committed.

**Text read:** the version of record (PMC5576488, from the Europe PMC full-text XML): main text, figure legends, the legends of all 22 figure supplements, and the Methods. eLife has no other supplement. There is no PDF of the paper under `paper/`, so I could read no figure panels. The paper links no analysis code; it names only MatClust and Chronux. The data descriptor was used only to know what hc-13 holds: the five foraging-task rats, with CA1 and PFC recordings.

**Claims:**
- **Counts:** all 32 claims have quotes, and none is inferred. 28 have statistics. 9 have expected values with tolerances (cell counts, SWR counts and fractions, the 6.4 to 6.6 s transition interval, cells and spikes per SWR, PFC unit counts and groups, and the R² of 0.73). 32 have criteria.
- **Where the data are:** 23 claims use tests the paper ran on both tasks pooled, or appears to have (the cell counts imply it). I marked these `with_inputs`, because the W-track rats are not in hc-13. The paper names CRCNS hc-6 (doi:10.6080/K0NK3BZJ) as that data. Each of these claims states its foraging-only test as a variant. The 9 claims that use only the foraging data (two per-task panels, the transition interval, and the 6 PFC claims) are `dataset`.

**Details the paper leaves open, and the readings named:**
- **"At a reward well" (O1):** beam-break entry and exit times, or immobility periods assigned to wells found as clusters of immobile positions. No well positions or radius are given.
- **Excluding SWR activity from IAP rates (O2):** remove the spikes only (as the Methods say), or remove both the spikes and the time. The rate is pooled over the day's sessions, with the maximum over sessions as a variant.
- **Speed (O3):** the paper doesn't say how speed is computed from position. I used a standard smoothing and named unsmoothed speed as a variant.
- **Unit counts (O4):** each unit counted once per day, or unique units.
- **SWR threshold (O5):** "envelope power" read as the envelope or its square. The histogram bin is a standard choice, and normalization uses task-session immobility only.
- **Coactivity permutations (O6):** all SWRs of the day pooled, or per session and then averaged.
- **Pair selection by cross-correlation peak (O7):** the window is not given; read as ±5 s or ±10 s.
- **Other open points:**
  - how the foraging maze is linearized for field size;
  - whether the PFC 1 s window is centred on SWR start or midpoint;
  - the PETH bin and shift range;
  - pooled spikes or first spike per cell for spike timing;
  - how subsamples are matched;
  - Pearson or Spearman for the theta-scale correlation;
  - which 15 units enter the regression;
  - how the PFC index pairs are formed;
  - the test for "no more than chance" coactivity.
- **Choices I fixed myself and labelled as choices:** "close to 1" for well specificity (median ≥ 0.8, with 0.9 as a stricter reading), how far the Figure 2C tail must reach (0.5 s), the theta peak window (0.1 to 0.16 s), and the lag range for SWR timing (±2 s).

**Gaps in the paper that the claims needed:**
- **Unassigned significance marks:** several legends (Figure 3 supplement 3, Figure 4B, Figure 4 supplement 2C, Figure 1 supplement 4E) give significance marks without saying which comparison carries which. Without the PDF I recorded them as unassigned.
- **MAP count mismatch:** the per-task MAP counts (244 + 435 = 679) don't add up to the stated n = 659. The claim accepts either number.
- **SWR counts per task:** these are given only in a figure panel I couldn't read.
- **Kay et al. 2016 W-track data:** the paper names no separate deposit for them, only hc-6.
