# Moaddab, Wright & McDannald (2020) from CRCNS pag-2

Tests the findings of [Moaddab et al. (2020)](https://doi.org/10.1038/s41598-020-74457-3) that can
be tested on CRCNS data set [pag-2](https://doi.org/10.6080/K0833Q7F), which holds 354 single units
recorded in the ventrolateral periaqueductal gray and dorsal raphe of 8 Control and 12 early
adolescent adversity (EAA) rats during fear discrimination, with the authors' cube and analysis
script. The body weights and pre-surgery sessions of Figure 1 are not in it.

| Claim | Outcome |
|---|---|
| Body weight gain slowed by adversity (Fig. 1B, C) | Blocked: data missing |
| Acquisition of discrimination before surgery (Fig. 1E, F) | Blocked: data missing |
| Equal baseline nose poking (Fig. 2B) | Reproduced |
| Discrimination during recording (Fig. 2C) | Reproduced |
| Counts of cue-excited and cue-inhibited neurons (Fig. 2D) | Reproduced |
| More cue-responsive neurons in EAA (Fig. 2D) | Reproduced |
| Baseline firing by type and group (Fig. 2E, F) | Reproduced |
| Temporal pattern of cue-excited firing (Fig. 4A, B) | Partially reproduced (bregma part not testable) |
| Inflated onset firing in EAA cue-excited neurons (Fig. 4C) | Reproduced |
| Temporal pattern of cue-inhibited firing (Fig. 4D, E) | Partially reproduced (bregma part not testable) |
| Greater danger decrease in EAA cue-inhibited neurons (Fig. 4F) | Reproduced |
| Danger and uncertainty discrimination in EAA cue-inhibited neurons (Fig. 4F) | Reproduced |
| Reduced threat probability signaling in EAA cue-excited neurons (Fig. 5A to C) | Partially reproduced |
| Threat tuning curve (Fig. 5D) | Reproduced, on an assumption |
| Same pattern with the peak assignment (Fig. S4) | Reproduced |
| Fear output signaling in cue-inhibited neurons (Fig. 5E to G) | Reproduced |
| Firing and threat signaling decoupled in EAA (Fig. 6) | Partially reproduced |
| Firing and fear output unrelated in cue-excited neurons (Fig. S5) | Reproduced |
| Firing and fear output in cue-inhibited neurons (Fig. 7) | Not reproduced |
| Firing and threat signaling in cue-inhibited neurons (Fig. S6) | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The group of each rat and the meaning of the event codes are given only by the authors' script in
the data set. The paper's counts of responsive neurons follow from the cube's firing rates, which
are truncated to whole Hz, and its statistics for Figs. 4C, 4F and 6 follow from the script's
normalization, which differs from the one the Methods describe. The single-unit regressions are
judged under the script's own inputs, which give the paper's printed statistics more closely than
any other reading. The paper's Fig. 7 statistics follow from firing over the first 5 s of the cue,
where its legend says the last 5 s. The attempt record, with the
reasons and the differences from the paper's method, is
[`attempts/moaddab-2020-01.yaml`](../../attempts/moaddab-2020-01.yaml).

- `reproduce_moaddab_2020.ipynb`: the analysis. It takes about a minute, most of it streaming the
  354 unit files from the zip.
- `pag2.py`: streaming the zip, reading the unit files and the cube, trial tables, suppression
  ratios, the selection, normalized firing, the single-unit regressions, a mixed ANOVA and the
  Fisher r-to-z test. Other notebooks on this data set can import it.
