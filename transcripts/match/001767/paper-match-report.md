I wrote the verdict to `papers/match/001767.yaml` and the file passes validation.

- **doi:10.1038/s41586-023-06492-9** (Chantranupong et al. 2023, "Dopamine and glutamate regulate striatal acetylcholine in decision-making"): **primary**, `by: agent`.
  - **Deciding evidence:** the dataset is named "Photometry data underlying the analyses in Chantranupong PMID: 37557915". PMID 37557915 is this paper. The dataset's description matches the paper's main experiment: fibre photometry of dopamine and acetylcholine in the striatum of mice doing a two-armed bandit task, with behaviour.
  - **Not in the dataset:** the paper's brain-slice experiments (amperometry and cell-attached recordings) and its histology. I judged these to be control experiments that confirm the manipulations work, so I chose primary over partial. If a reviewer counts them as findings in their own right, partial would also be defensible.
  - **Paper's own data statement:** "available upon request". It names no dataset, so the checks found no dataset name in the text.
