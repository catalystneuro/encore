I judged the one paper `partial`. The match file `papers/match/001525.yaml` passes validation.

**doi:10.1016/j.bioelechem.2026.109283** ("Sub-microsecond optical measurements of cell membrane charging and lesioning…")
- **What decided it:** the dataset's title, "Characterization of Plasma Membrane Recovery in Cells After 1-µs Electroporation Using Strobe Fluorescence Microscopy". That matches one of the paper's experiments: the two-pulse recovery test in Section 3.7 and Fig. 7 ("Membrane recovery was probed by a 2-pulse protocol").
- **What is probably not in the dataset:** the paper's other findings, which come from dye calibration, azimuthal charging, Gd³⁺, Ca²⁺ uptake and 0.3-µs pulse experiments. The paper doesn't name any dataset; its data statement says only "Data will be made available on request."
- **What is uncertain:** the dataset has 10 cells, all recorded on 2025-03-18, but Fig. 7 reports n = 5. So the dataset may not line up exactly with that figure.
- **Supporting evidence:** the authors overlap (Semenov, Silkuniene, Pakhomov), and both the dataset and the paper use CHO cells.

I didn't set `data_in`, because the paper names no other dataset.
