# Zhang et al. (2021) on CRCNS vim-4

Tests the findings of Zhang, Gao, Cukur and Gallant (2021), "Voxel-Based State Space Modeling
Recovers Task-Related Cognitive States in Naturalistic fMRI Experiments", Frontiers in Neuroscience
14:565976, on CRCNS data set vim-4 (doi:10.6080/K0668BDF), streamed from the public CRCNS bucket.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

- `reproduce_zhang_2021.ipynb`: the data check and one section per claim.
- `statespace.py`: loading, the state space of the paper's code (computed in the space of the 24
  principal components), the cluster separation index and the classifiers.

The notebook streams about 7 GB and runs in about 20 minutes with 4 GB of memory.
