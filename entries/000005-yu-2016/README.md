# Yu, Gutnisky, Hires & Svoboda (2016) from dandiset 000005

Tests the claims of [Yu et al. (2016)](https://doi.org/10.1038/nn.4412), written by a reader from
the full text and its supplement, on [DANDI:000005](https://dandiarchive.org/dandiset/000005/0.220126.1853)
version 0.220126.1853, the only published version: 18 silicon probe sessions in VPM (29 units) and
130 single L4 cells recorded whole-cell or cell-attached, during pole localization with whisker
tracking. The current record is [`attempts/000005-yu-2016-02.yaml`](../../attempts/000005-yu-2016-02.yaml);
it replaces [`attempts/000005-yu-2016-01.yaml`](../../attempts/000005-yu-2016-01.yaml), whose claims
were written from the abstract.

| Claim | Outcome |
|---|---|
| `behavior-touches` | Partially reproduced |
| `vpm-touch` | Not reproduced |
| `vpm-whisking` | Partially reproduced |
| `vpm-whisking-phase` | Reproduced |
| `exc-vm-touch-whisking` | Partially reproduced |
| `exc-threshold-touch-vs-whisking` | Partially reproduced |
| `exc-effective-reversal` | Reproduced |
| `exc-inhibition-timing`, `exc-inhibition-whisking` | Blocked: data missing |
| `fs-touch-response` | Partially reproduced |
| `fs-vm-touch-whisking` | Not reproduced |
| `fs-whisking-rate` | Partially reproduced |
| `fs-whisking-phase` | Reproduced |
| `fs-touch-and-whisking` | Reproduced |
| `exc-mainly-touch` | Not reproduced |
| `vpm-photoinhibition` | Blocked: data missing |
| `exc-thalamus-photoinhibition` | Partially reproduced |
| `thalamus-drives-fs` | Blocked: too few cells |
| `rabies-vpm-input` | Blocked: data missing |
| the seven ION-cut claims | Blocked: metadata insufficient |
| `pv-enphr-suppression` | Partially reproduced |
| `fs-suppress-movement-spiking` | Partially reproduced |
| `fs-enhance-touch-selectivity` | Partially reproduced |
| `exc-touch-spikes-enphr` | Not reproduced |
| `auc-weak-strong` | Reproduced |
| `auc-groups` | Blocked: methods underspecified |
| `behavior-false-alarms` | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files give no cell type for the L4 neurons and do not mark the mice whose infraorbital nerve was
cut. Cell classes are built by the claims file's rules (light tag, the waveform boundary of
Supplementary Fig. 6, PV inactivation, spike width), and every group holds the cells of all mice; a
variant leaves out four mice flagged as lacking touch input. Open method details were asked in
[`questions/000005.yaml`](../../questions/000005.yaml) and answered by a reader on 2026-10-20; the
claims they bear on were re-run under the updated criteria, which moved `behavior-false-alarms`
from blocked to reproduced and left the other outcomes as they were.

- `reproduce_yu_2016.ipynb`: the analysis. The recorded run took 302 s from a clean environment,
  most of it streaming the files.
- `yu2016.py`: loading the files with range requests and reducing them as they load (spikes, the
  whisking epochs of the principal whisker under both filter readings and, for whole-cell cells,
  under each whisking-onset and touch reading (O10, O11), touches, licks, light
  epochs, spike-removed membrane potential and event-aligned averages), and the paper's measures as
  the claims file gives them. Other notebooks on this dandiset can import it.
