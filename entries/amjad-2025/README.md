# Amjad et al. (2025) on DANDI:002013

Tests the claims in `claims/amjad-2025.yaml` on version 0.261120.1306 of
[DANDI:002013](https://dandiarchive.org/dandiset/002013/0.261120.1306), streaming the three NWB
files. `reproduce_amjad_2025.ipynb` holds the analysis; `amjad.py` holds the loading and the
measures, each parameter with its source. The claim `zenodo-link` also reads the paper's Zenodo
deposit (doi:10.5281/zenodo.14826579).

Of 14 claims, 8 are reproduced, 1 partially reproduced (fscv-waveform), 1 not reproduced
(fig3a-redox-peaks) and 4 blocked (the second dopamine channel, the implantation dates and list of
implanted sensors, and a code map for Monkey P's events are not in the dataset).

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

Run with `python tools/entry.py all entries/amjad-2025`; it takes about 4 minutes and 3.5 GB of
memory.
