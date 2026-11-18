# McGuire et al. (2016) on CRCNS ssc-4

Tests the claims in `claims/mcguire-2016.yaml` on the CRCNS data set ssc-4 (doi:10.6080/K06D5QXN),
the file `AllRats.mat`, streamed from the public CRCNS bucket and pinned by its MD5 sum. Three claims
use the paper's supporting data (S1 and S2 Data).

- `reproduce_mcguire_2016.ipynb`: data checks, behaviour, units, regression classes and the
  responses of each class (Figures 2 to 8, S2 to S7).
- `decoders.ipynb`: the population decoders of Figure 9.
- `ssc4.py`: loading and the shared measures.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.
