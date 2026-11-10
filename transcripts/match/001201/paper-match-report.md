I gave the one unsettled paper a verdict and left the checks verdict on the other as it was. `papers/match/001201.yaml` passes validation.

- **doi:10.52202/085713-4642 (Temmar et al., the LINK NeurIPS paper): `primary`, set by the checks, left as is.** The paper says "The dataset is publicly available on the DANDI archive, dandiarchive.org/dandiset/001201". Its subject (Monkey N), its 312 sessions over 1,242 days and its 96 motor cortex channels match the archive metadata.

- **doi:10.1016/j.neuron.2021.08.009 (Nason et al. 2021, Neuron): `partial`, by agent.**
  - **What decided it:** the paper's Data and code availability section points to another repository: "A subset of the data used in this study can be found online ... (https://doi.org/10.7302/jnkz-az17)". I listed that DOI in `data_in`.
  - **Why only partial:** the paper uses monkeys N and W, and its main findings come from closed-loop brain-machine interface control. The dataset holds only Monkey N, and the LINK paper says it left out closed-loop trials.
  - **Where they overlap:** Monkey N's recordings in the paper fall on days 117 to 708 after implant, and the dataset's run from day 349 to 1591. Some of the paper's offline Monkey N analyses of hand-controlled movement might be testable on the dataset.
  - **What is uncertain:** whether the paper's exact sessions are in the dataset. The archive itself cites this paper only for "details on the experimental setup".
