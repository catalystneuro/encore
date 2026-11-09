**DANDI:001516, one paper**

- **doi:10.1016/j.bioelechem.2026.109283** (Semenov et al., *Bioelectrochemistry* 2026). **Verdict: `partial`.**
  - **Deciding evidence:** The dataset is titled "Plasma Membrane Recovery…". Its description says it holds "40 exposures with one or two 1-us pulses of varying amplitudes and interval between pulses". That matches the paper's Section 3.7, which tests membrane recovery with a conditioning pulse followed by a test pulse ("Membrane recovery was probed by a 2-pulse protocol", Fig. 7). The dataset is 12 CHO cells, the same cell type, and the authors overlap (Semenov, Silkuniene, Pakhomov).
  - **Why not `primary`:** The dataset describes only 1-µs pulses. The paper also rests on 0.3-µs pulses, FluoVolt imaging, and Ca²⁺ imaging in 224 cells, none of which the dataset describes.
  - **Uncertain:** The image counts differ. The dataset has 20 sham plus 40 pulsed exposures per cell; the paper describes sets of 40 baseline plus 60 images. So it is not certain which figures the dataset holds: possibly Fig. 7 and the 1-µs single-pulse series.
  - **`data_in`:** Left empty. The paper's data statement says only "Data will be made available on request", so it names no other dataset.

The verdict is written to `papers/match/001516.yaml` with `by: agent`, and the file passes `tools/paper_match.py validate`.
