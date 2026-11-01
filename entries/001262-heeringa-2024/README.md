# Heeringa (2024) from dandiset 001262

Tests the findings of [Heeringa (2024)](https://doi.org/10.1038/s41597-024-03259-3), a data
descriptor, on [DANDI:001262](https://dandiarchive.org/dandiset/001262/0.241205.0959), which holds
1160 single auditory nerve fibres from 104 gerbils, one NWB file per fibre.

| Claim | Outcome |
|---|---|
| Table 1 counts of animals, females and units | Reproduced |
| Table 1 mean age, ABR threshold and weight | Reproduced (ABR read from a character code) |
| Table 1 best-frequency ranges | Reproduced |
| ABR thresholds rise with age, widest spread in old animals | Reproduced |
| Fewer females among old animals | Reproduced |
| 78 of 104 animals received oxygen | Reproduced |
| Experiments with NOISE, SPS and CVC (21, 5, 17) | Reproduced |
| Units per recording type (Fig. 7) | Partially reproduced (CLICK 271, not 261) |
| No SR, SPS or CVC in middle-aged animals | Reproduced |
| Units with short inter-spike intervals were excluded | Not reproduced |
| Example fibre of Fig. 5b | Reproduced |
| Fig. 6a highest young-adult thresholds at 3.5 kHz | Reproduced |
| Fig. 6b fewest young-adult BFs at 2.5 to 3.0 kHz | Not reproduced |
| Fig. 6c spontaneous rate distributions | Reproduced |
| Fig. 6d phase locking up to 4.6 kHz; highest in low-BF low-SR fibres | Reproduced (two claims) |
| Fig. 7a CF matches BF | Reproduced |
| Fig. 7b click latency falls with BF | Reproduced (click delay assumed) |
| Fig. 7a,b CF and CLICK units represent the full BF distribution | Not reproduced |
| Prepotentials, rate-level shapes, PSTH shapes (visual checks) | Blocked: methods underspecified |
| Success rate of recordings in old and young animals | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The NWB files keep only best frequency, spontaneous rate and threshold of the paper's analysed
outcomes, so characteristic frequency, vector strength and click latency are recomputed from the
spike times with the paper's own MATLAB functions (Zenodo 10.5281/zenodo.10370064). The ABR
threshold is stored as a character whose code point is the threshold. The attempt record, with
the reasons and the differences from the paper's method, is
[`attempts/001262-heeringa-2024-01.yaml`](../../attempts/001262-heeringa-2024-01.yaml).

- `reproduce_heeringa_2024.ipynb`: the analysis. It takes about four minutes, most of it reading
  the 1160 files' metadata and spike times (the voltage traces are not read).
- `gerbil_an.py`: loading the files in parallel, parsing the animal metadata, and the measures of
  the paper's code (vector strength, CF, 2-bin click latency, inter-spike intervals). Other
  notebooks on this dandiset can import it.
