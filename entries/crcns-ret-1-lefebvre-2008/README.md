# Lefebvre, Zhang, Meister, Wang & Sanes (2008) from CRCNS ret-1

Tests the findings of [Lefebvre et al. (2008)](https://doi.org/10.1242/dev.027912) that can be
tested on [CRCNS ret-1](https://doi.org/10.6080/K0RF5RZT), which holds multielectrode recordings
of 325 units from 16 Pcdh-gamma mutant and control mouse retinas, stimulated with flickering bars
and checkerboards (Figure 9D to 9H). The histology of Figures 1 to 8 and the flash, spot and
grating experiments of Figure 9A to 9C are not in it.

| Claim | Outcome |
|---|---|
| Figure 9 counts, 115 mutant and 143 control cells | Not reproduced (200 and 122) |
| Receptive field centre size similar in mutant and control | Blocked: methods underspecified (17 of 18 readings separate, mutant smaller) |
| Some mutant and control cells have surrounds | Reproduced by the criterion, which noise also meets |
| Slower time course in mutants | Reproduced |
| Lower firing rate in mutants | Reproduced |
| LN threshold unaltered in mutants | Not reproduced (mutant higher) |
| LN gain reduced in mutants | Blocked: methods underspecified |
| Figure 9A to 9C and rod and cone responses (four claims) | Blocked: data missing |
| Figures 1 to 8 and Supplementary Figure 1, histology (15 claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The data set's unit counts and control genotypes differ from the paper's, many mutant units have
weak or no receptive fields, the spike trains of four retinas hold a segment out of time order
(consistent with a misplaced last minute, which is not proven), and the frame length stated for
the bar stimulus of two retinas is wrong (the notebook rebuilds it with the frame of the other
recordings). The outcomes for firing rate and LN threshold hold on all units, as the claims file
reads the groups; among units with clear STAs both would be blocked. The blocked outcome for
centre size rests on one borderline combination and on the frame correction. The attempt record, with
the reasons and the differences from the paper's method, is
[`attempts/crcns-ret-1-lefebvre-2008-01.yaml`](../../attempts/crcns-ret-1-lefebvre-2008-01.yaml).

- `reproduce_lefebvre_2008.ipynb`: the analysis. It takes about eight minutes (the last code cell prints the run time), streaming the
  data set's zip from the CRCNS S3 bucket.
- `ret1.py`: loading the zip in place, rebuilding the white-noise stimulus from `ran1.bin`, and
  the spike-triggered average, its separation, the LN fit and the 95% bands of the cumulative
  histograms. Other notebooks on this data set can import it.
