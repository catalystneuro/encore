# LeMessurier et al. (2019) from CRCNS ssc-10

Tests the findings of [LeMessurier et al. (2019)](https://doi.org/10.7554/eLife.46321) on CRCNS
data set [ssc-10](https://doi.org/10.6080/K0DB801M), which holds the 2-photon imaging of L2/3
(Drd3-Cre) and L4 (Scnn1a-Cre) excitatory neurons in enriched (EN) and normally housed (NH) mice
during deflection of nine whiskers: 36 imaging fields in 25 mice.

| Claim | Outcome |
|---|---|
| Mice and fields per group (Table 1) | Reproduced |
| L2/3 cell counts | Reproduced |
| L4 cell counts | Not reproduced |
| Receptive fields from GCaMP and spikes agree (Figure 1F) | Blocked: data missing |
| EN strengthens the L2/3 point representation near the column | Reproduced, with the stored responsiveness p-values and the blank-median z-score |
| EN weakens L2/3 responses at the flanks | Partially reproduced |
| 2D maps of the point representation | Reproduced |
| EN weakens the L4 point representation | Not reproduced |
| L4 point representation sharper than L2/3 | Reproduced |
| Column-frame point representation (Figure 2 S1) | Not reproduced |
| Barrel size unchanged | Partially reproduced |
| Salt-and-pepper tuning in NH L2/3 | Partially reproduced (best whisker yes, equivalent best whiskers no) |
| NH L2/3 in-column tuning (Discussion) | Partially reproduced |
| NH L4 tuning against L2/3 | Not reproduced (best whisker yes, equivalent best whiskers no) |
| EN raises CW tuning in L2/3 | Not reproduced |
| EN raises CW tuning in L4 | Reproduced |
| Ranked receptive fields sharper in EN L2/3 | Reproduced |
| CW and best surround whiskers stronger in EN L2/3 | Reproduced, with the stored responsiveness p-values |
| Spontaneous activity lower in EN L2/3 | Reproduced, without baseline subtraction |
| Absolute dF/F and tuning slopes (Figure 4 S1) | Not reproduced |
| Sharpening larger over barrels than septa | Reproduced |
| CW response stronger in EN L2/3 | Reproduced, with the stored responsiveness p-values |
| Across-row sharpening | Partially reproduced |
| Within-row broadening | Partially reproduced |
| L4 responses weaker in EN | Not reproduced |
| Signal correlations and column boundaries | Partially reproduced |
| Noise correlations and column boundaries | Partially reproduced |
| Correlation gradient at the column edge | Reproduced (noise gradient not significant) |
| Row and arc boundaries | Partially reproduced |
| L4 within-column correlations | Partially reproduced |
| Robustness to neuropil subtraction | Not reproduced |
| Single-ROI decoders | Partially reproduced |
| Random population decoders | Reproduced, with ensembles as units |
| Clustered ensemble decoders | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/crcns-ssc-10-lemessurier-2019-01.yaml`](../../attempts/crcns-ssc-10-lemessurier-2019-01.yaml).

- `reproduce_lemessurier_2019.ipynb`: the analysis. The last three runs took 14 to 24 minutes,
  7 to 10 of them streaming the 4.7 GB tar file.
- `ssc10.py`: streaming and reduction of each field to per-trial evoked responses, the
  responsiveness test, equivalent best whiskers, pair correlations and the decoders. Other
  notebooks on this data set can import it.
