# Sargolini et al. (2006) from dandiset 000582

Tests the claims of [Sargolini et al. (2006)](https://doi.org/10.1126/science.1125572)
on [DANDI:000582](https://dandiarchive.org/dandiset/000582/0.251111.2151), version 0.251111.2151,
the only published version (the draft holds the same assets).

The claims file, `claims/000582/10.1126-science.1125572.yaml`, was written from the full text and
its Supporting Online Material. It replaces a file written from the abstract only, on which the
earlier attempt, `000582-sargolini-2006-01`, was based; that attempt is deprecated.

| Claim | Outcome | Earlier attempt |
|---|---|---|
| `layer2-grid` | Partially reproduced | Partially reproduced |
| `grid-all-layers` | Reproduced | |
| `gridness-range-similar` | Blocked: methods underspecified | |
| `grid-stable` | Blocked: methods underspecified | |
| `spacing-dorsoventral` | Blocked: data missing | |
| `fieldsize-dorsoventral` | Blocked: data missing | |
| `grid-phase-orientation` | Partially reproduced | |
| `hd-layers` | Not reproduced | |
| `hd-with-grid-colocalized` | Blocked: methods underspecified | |
| `hd-tuning-breadth-layers` | Blocked: methods underspecified | |
| `hd-full-range` | Reproduced | |
| `hd-colocalized-distributed` | Reproduced | |
| `hd-stable-trials` | Reproduced | |
| `hd-rates` | Not reproduced | |
| `deep-hd-conjunctive` | Not reproduced | Reproduced |
| `gridness-hd-continuous` | Reproduced | |
| `conj-tuning-similar` | Blocked: methods underspecified | |
| `cue-rotation-coherent` | Blocked: data missing | |
| `speed` | Blocked: methods underspecified | Reproduced |
| `speed-slope-steeper` | Blocked: methods underspecified (depends on `speed`) | |
| `speed-intercept` | Blocked: methods underspecified (depends on `speed`) | |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons, is
[`attempts/000582-sargolini-2006-02.yaml`](../../attempts/000582-sargolini-2006-02.yaml); the
questions it asked about the claims file are in [`questions/000582.yaml`](../../questions/000582.yaml). A reader
answered all five on 2026-10-20, and the claims file carries the answers; the notebook follows the
updated criteria. The answers changed one outcome, `grid-phase-orientation`, from blocked to
partially reproduced.

- `reproduce_sargolini_2006.ipynb`: the analysis. It streams all 118 files and takes about five
  minutes on four cores.
- `sargolini.py`: loading the dandiset, and the rate maps, autocorrelograms, gridness,
  head-direction tests and speed regressions of the paper's Supporting Online Material, under every
  reading the claims file names. Other notebooks on this dandiset can import it.

## Found about the dandiset

Still present from the earlier attempt:

- Every file says the enclosure was 1 x 1 m, but in 22 files the positions span 150 or 200 cm.
- 47 of the 118 files have one tracking LED, though the descriptions say two; rat 11084 has files
  of both kinds.
- No identifier links a cell across files, so the same cell may be counted more than once.
- The dandiset is described as a sample; how it was selected is not stated. It holds 620
  cell-sessions from 15 rats, against 627 cells from 17 rats in the paper, with fewer layer II cells.
- The analysis methods are not in the dandiset and no code is public (this attempt read them in the
  paper's supplement).

New:

- The positions are rescaled to span exactly 100, 150 or 200 cm, without saying so.
- The 20-minute files hold two trials joined near 600 s, with no trial table.
- The distance of the recording sites from the postrhinal border is not given.
- No file names its enclosure, condition or cue-card position.
- Six cells have no layer, 36 no depth and 230 no hemisphere.
- The descriptions say the files hold grid cells, or conjunctive and head-direction cells of
  layers III and V; they hold cells of every class from layers II, III, V and VI.
- The files do not say which LED is the red one.
