# Su et al. (2026), Patch-seq of LC-NE neurons, on dandiset 001893

The notebook `reproduce_su_2026.ipynb` tests the Patch-seq claims of Su, Kosillo, Jung et al.,
"Topographic structure and function of locus coeruleus noradrenaline neurons", Nature (2026),
doi:10.1038/s41586-026-11026-0, on DANDI:001893 version 0.260817.1647. The NWB files are
streamed from DANDI and the FASTQ files from the NeMO Archive; nothing is written to disk.

`lcne.py` reads the recordings and computes the waveform PC1 (as the paper's code
LCNE-patchseq-figures at 79fa20a does), the Methods' sweep rule and IPFX's membrane time
constant. `rna.py` counts marker-gene reads in the Patch-seq FASTQ files.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The claims and their outcomes are in `claims/001893/` and `attempts/su-2026-01.yaml`.
