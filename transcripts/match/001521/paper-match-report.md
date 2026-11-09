I judged the one paper `partial`. The match file `papers/match/001521.yaml` now passes `python tools/paper_match.py validate`.

**doi:10.1016/j.bioelechem.2026.109283** ("Sub-microsecond optical measurements of cell membrane charging and lesioning by pulsed electric fields"): **partial**.

- **What decided it:** the archive metadata describes a single experiment, "This experiment aimed to determine the threshold for calcium uptake in CHO cells subjected to 1-µs electric pulses." That matches only the paper's Fluo-4 calcium imaging with single pulses (Methods 2.4, Fig. 6A). The archive's own contributors (Silkuniene, Semenov, Pakhomov) are among the paper's authors.
- **What the dataset lacks:** the paper's main findings come from pulsed laser imaging of membrane voltage in CHO cells, using the FluoVolt and Di-8-ANEPPS dyes. The archive metadata does not describe that imaging. The 15 subjects come from two recording dates, 20250203 and 20250502.
- **Where the rest of the data are:** the paper names no dataset. Its data statement says only "Data will be made available on request," so `data_in` is left empty.
- **What is uncertain:** I could not tell, without opening files, whether the dataset also holds the 60-pulse 6-Hz train experiment (Fig. 6B).
