# Yu, Gutnisky, Hires & Svoboda (2016) from dandiset 000005

Tests the findings of [Yu et al. (2016)](https://doi.org/10.1038/nn.4412) stated in its abstract
and figure titles, on [DANDI:000005](https://dandiarchive.org/dandiset/000005/0.220126.1853): 18
silicon probe sessions in VPM (29 units) and 130 single L4 cells recorded whole-cell or
juxtacellularly, during pole localization with whisker tracking. The paper's full text is not open
access. Its supplementary figure legends and tables are public and were read after the first run;
they are used for the data check and for variants. No number of the paper's main text is tested, and
every method choice is made here.

| Claim | Outcome |
|---|---|
| VPM neurons fire in response to touch | Reproduced |
| VPM neurons fire in response to whisker movement | Reproduced |
| L4 FS interneurons respond to touch and whisker movement | Reproduced |
| L4 excitatory neurons respond mainly to touch | Not reproduced |
| Silencing FS cells increases whisking-related spiking of excitatory cells | Reproduced |
| FS cells enhance the touch selectivity of excitatory cells | Not reproduced |
| Thalamic activity drives L4 FS interneurons | Reproduced |
| FS movement responses come from sensory input, not corollary discharge | Blocked: metadata insufficient |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files give no cell type for the L4 neurons. FS cells are identified here by their spikes to 5 ms
light pulses in VGAT-ChR2 mice, and excitatory cells by broad action potentials in whole-cell
recordings. The files do not mark the mice whose infraorbital nerve was cut (Figure 7 of the paper),
so the test of that figure is blocked and cells from those mice are mixed into the groups; the
notebook flags four mice whose cells have no touch input. The attempt record, with the reasons and
the differences from the paper's method, is [`attempts/000005-yu-2016-01.yaml`](../../attempts/000005-yu-2016-01.yaml).

- `reproduce_yu_2016.ipynb`: the analysis. It takes about four minutes, most of it streaming the
  files.
- `yu2016.py`: loading the files with range requests, spike detection, light epochs, the touch
  and whisking measures, and the mouse lines of the paper's Supplementary Table 1. Other notebooks
  on this dandiset can import it.
