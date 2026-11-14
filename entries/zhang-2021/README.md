# Zhang et al. (2021) on CRCNS vim-4

Tests the findings of Zhang, Gao, Cukur and Gallant (2021), "Voxel-Based State Space Modeling
Recovers Task-Related Cognitive States in Naturalistic fMRI Experiments", Frontiers in Neuroscience
14:565976, on CRCNS data set vim-4 (doi:10.6080/K0668BDF), streamed from the public CRCNS bucket.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

- `reproduce_zhang_2021.ipynb`: the data check and one section per claim.
- `statespace.py`: loading, the state space of the paper's code (computed in the space of the 24
  principal components), the cluster separation index, the classifiers, and the atlas regions and
  encoding models of the two cortical claims.

The two cortical claims use two public fsaverage atlases in place of the paper's ROIs, which are
not deposited: visfAtlas (Rosenke et al. 2021, doi:10.1093/cercor/bhaa246) and HCP-MMP1.0 on
fsaverage (doi:10.6084/m9.figshare.3498446.v2). Both are read into memory and checked against
their checksums.

The notebook streams about 16 GB and runs in about 55 minutes with 6 GB of memory.
