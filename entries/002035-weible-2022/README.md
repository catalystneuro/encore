# Weible & Wehr (2022) on dandiset 002035

Checks [DANDI:002035](https://dandiarchive.org/dandiset/002035/0.261022.1829) against the findings of
[Weible and Wehr (2022)](https://doi.org/10.3233/JAD-220538), on the onset and spread of Abeta42 label
in the central auditory pathway of 5XFAD mice.

| Claim | Outcome |
|---|---|
| Wild-type mice show no label (wt-no-label) | Blocked: data missing |
| The other 32 claims (A1, subiculum, MGB, IC, SOC, nLL, CN and PRNc counts and densities by age, layer, subregion and sex) | Blocked: metadata insufficient |

The dandiset holds the raw widefield images of 62 5XFAD mice. The region of 93% of the images is not
recorded, no sampled image carries a stage position or section number, and the dandiset holds no
counts, boundaries or atlas alignments, so no per-region value of the paper can be formed. The
wild-type controls were not imaged. The notebook checks the subjects, the files and the stated
image scales, and shows the region coverage. The attempt record is
[`attempts/002035-weible-2022-01.yaml`](../../attempts/002035-weible-2022-01.yaml).
