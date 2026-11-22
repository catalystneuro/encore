# Yang (2026) from dandiset 000020

Tests the findings of [Yang (2026)](https://doi.org/10.1523/eneuro.0275-26.2026), "Flexible
Cellular Phenotypes Retain a Shared Type-Level Organization across Response Regimes", on
[DANDI:000020](https://dandiarchive.org/dandiset/000020/0.210913.1639), the Allen Institute
Patch-seq recordings of 4,435 interneurons of mouse visual cortex (Gouwens et al. 2020), which the
paper reuses.

The notebook extracts the IPFX cell-level features of every file for the long-square, ramp and
short-square regimes, builds the paper's three phenotype spaces, and repeats its cell-level and
type-level analyses with the t-type labels of the paper's metadata join (from its code at commit
61a5a41). The transcriptomic analyses of Figure 4 and the WGCNA analysis need the NeMO Patch-seq
count matrix, whose server did not answer during the attempt; they are blocked.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The outcomes, the reasons and the differences from the paper's method are in the attempt record,
[`attempts/yang-2026-flexible-01.yaml`](../../attempts/yang-2026-flexible-01.yaml), and in the
notebook's summary.

- `reproduce_yang_2026.ipynb`: the analysis. It takes about 45 minutes, most of it the one pass
  that streams the 142 GB of the dandiset and runs IPFX on each file, in six processes.
- `patchseq.py`: streaming a file into memory, the IPFX feature extraction per regime and for split
  halves of the long squares, and the values of the data check. Other notebooks on this dandiset
  can import it.
- `geometry.py`: the phenotype spaces and the paper's cell-level and type-level measures.
