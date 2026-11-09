**DANDI:001517 gets one verdict: `partial`** for doi:10.1016/j.bioelechem.2026.109283, "Sub-microsecond optical measurements of cell membrane charging and lesioning by pulsed electric fields". The file passes validation.

- **What the dataset holds:** the paper's Di-8-ANEPPS imaging of CHO cells. The dataset description says the cells were "loaded with 5 µM Di-8-ANEPPS … replacing FluoVolt", which matches the paper's Methods. The authors are the same (Semenov, Silkuniene, Pakhomov), and so are the NIH grants (R21EY034803 and R21EY034258).
- **What it lacks:** the paper's findings also rest on FluoVolt imaging and on Fluo-4 Ca2+ imaging. Neither appears in the dataset's metadata.
- **Deciding evidence:** the abstract reports results for two dyes ("FluoVolt and Di-8-ANEPPS dyes changed emission by 26% and 9.1% per 100 mV"), while the dataset covers only the Di-8-ANEPPS one.
- **Where the rest is:** no other dataset is known. The paper's data statement says only "Data will be made available on request", so I left `data_in` empty.

I didn't commit anything; the workflow does that.
