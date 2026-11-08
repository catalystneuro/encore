# Yu et al. (2017) on CRCNS hc-13

Tests the findings of Yu, Kay, Liu, Grossrubatscher, Loback, Sosa, Chung, Karlsson, Larkin and Frank
(2017), "Distinct hippocampal-cortical memory representations for experiences associated with
movement versus immobility" (eLife 6:e27621), on CRCNS data set hc-13
([doi:10.6080/K0H41PK8](https://doi.org/10.6080/K0H41PK8)), which holds the five foraging rats.

- `reproduce_yu_2017.ipynb` streams the data set's single archive, `hc-13/live/data.tar.gz`, from
  the public bucket `crcnsarchive` once (about 14 minutes in all, 6.2 GB of memory at peak), checks its MD5
  against the data set's `checksums.md5`, and tests each claim of
  `claims/crcns-hc-13/10.7554-elife.27621.yaml`.
- `yu2017.py` reads the archive in place and reduces each animal (position and speed, units, SWRs
  under both readings of the envelope, per-SWR spectral power), and holds the reusable measures
  (well finding, IAP and MAP classification, correlograms, SWR coactivity).

The W-track rats the paper pools with the foraging rats are not in hc-13; claims on both tasks are
tested on the foraging rats. The data set has no beam-break well entry times, so wells are inferred from immobile positions,
and well entries and exits from immobility periods at a well (well visits, an assumption). The attempt record is `attempts/crcns-hc-13-yu-2017-01.yaml`.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.
