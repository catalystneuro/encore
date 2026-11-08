# Goncalves, Anstey, Golshani & Portera-Cailliau (2013) from CRCNS ssc-8

Tests the findings of [Goncalves et al. (2013)](https://doi.org/10.1038/nn.3415) that can be tested
on CRCNS data set [ssc-8](https://doi.org/10.6080/K0X63K3X), which holds the estimated firing rates,
cell-to-cell distances and raw movies of two-photon calcium imaging in L2/3 barrel cortex of 53
unanesthetized WT and Fmr1 -/- mice at P9-11, P14-16 and P30-40. The whole-cell recordings, EEG,
isoflurane imaging and 15.6 Hz imaging of the paper are not in it.

| Claim | Outcome |
|---|---|
| Group sizes of Fig. 1e (12, 9, 8 WT and 9, 10, 8 KO mice) | Not reproduced |
| In WT mice the drop in correlation from P9-11 to P14-16 is largest for nearby cells | Partially reproduced |
| Correlation decreases with age in both genotypes | Reproduced |
| Correlation is higher in KO mice, pooled over ages | Partially reproduced |
| The same with Pearson correlation | Partially reproduced |
| The genotype difference is largest, and significant, at P14-16 | Not reproduced |
| No significant genotype difference at P30-40 | Reproduced |
| Frequency of peaks of synchrony does not differ at P14-16 | Reproduced |
| More neurons take part in peaks of synchrony in KO mice at P14-16 | Not reproduced |
| Firing rates do not differ between genotypes at any age | Reproduced |
| Firing rates and WT correlation at P14-16 (Fig. 6, unanesthetized) | Reproduced |
| Whole-cell recordings (seven claims) | Blocked: data missing |
| EEG with imaging (five claims) | Blocked: data missing |
| Firing rate against correlation across the EEG subset's recordings (Suppl. Fig. 4a) | Blocked: metadata insufficient |
| Imaging at 15.6 Hz | Blocked: data missing |
| Isoflurane imaging (three claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The data set's groups differ from the paper's (53 mice against 56), and it deposits estimated firing
rates, not the dF/F traces the paper may have correlated. The attempt record, with the reasons and
the differences from the paper's method, is
[`attempts/crcns-ssc-8-goncalves-2013-01.yaml`](../../attempts/crcns-ssc-8-goncalves-2013-01.yaml).
