# Johnson et al. (2017) on CRCNS pfc-5

Tests the claims in `claims/johnson-2017.yaml` on CRCNS data set pfc-5 (doi:10.6080/K0ZC811B),
streamed from the public bucket `crcnsarchive`. The notebook `reproduce_johnson_2017.ipynb`
streams each subject's archive once, reduces it with `frontoparietal.py` and runs every test.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.
