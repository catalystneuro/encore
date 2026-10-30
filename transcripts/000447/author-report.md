I did steps 1 to 6 of the Author section. The entry is in `entries/000447-tang-2023/` and the record is `attempts/000447-tang-2023-01.yaml`. `tools/entry.py all` passes with 0 check errors. The notebook runs in about 20 minutes and gives identical outputs on three clean runs. The handover is in `executed/000447-tang-2023/handover/`. Nothing is committed.

## 1. Outcomes (32 claims)

| Claim | Outcome |
|---|---|
| cells-per-session | reproduced (27.5 CA1 and 36.5 PFC cells, against 30.5 and 37.4) |
| fig2d-pv-similarity | reproduced at all three smoothing widths |
| figs3a-ca1-global-remapping | reproduced (p = 0.075; p < 0.05 in 13 of 100 shuffle draws) |
| figs3c, figs4d, figs5d | reproduced |
| fig2f-switch-dynamics | reproduced, resting on an assumption (trial -1 is the last N trial) |
| figs3d-pfc-similarity-over-trials | reproduced, resting on an assumption (trials of N then N') |
| manifold-cell-counts | reproduced (99 and 171 cells, against 98 and 171) |
| fig3fg, fig3h, fig3i | reproduced (UMAP p-values vary with the seed) |
| figs3a-pfc-similar-ca1-lower | partial (CA1 rate overlap does not drop) |
| fig2e-ca1-error-familiar, fig2e-pfc-error-stable | partial (the "no difference" parts fail the paper's tests) |
| figs5e-path-equivalence-stable | partial, resting on the 8-cm smoothing (4 cm would reproduce it) |
| fig3j, figs6 | partial (CA1 F states are also closer than the shuffle) |
| fig4d-pfc-ccgp | partial (9 of 16 decoders at p < 0.001) |
| figs7d-dichotomies-decodable | partial (most decodable, but CA1 accuracy is higher) |
| fig1c-familiar-above-novel | not reproduced (Tukey F vs N p = 0.70; N-F-N' rats only) |
| figs4-ramping-fraction | not reproduced (3 to 4% ramping, against 16 to 18%) |
| fig3d, fig3e | not reproduced, resting on the 8-cm smoothing |
| fig4d-ca1-ccgp-chance, figs7b-geometric-null | not reproduced |
| fig1b, fig1-denovo-final, fig1c-session, figs1b | blocked, data_missing (no de novo sessions) |
| figs4-ramping-generalization | blocked, other (only one population of at least 3 ramping cells per region) |
| figs5f-path-equivalence-vs-selectivity | blocked, methods_underspecified (the criterion's own rule: signed and absolute SI disagree) |

## 2. What was found about the dataset

- **Unit regions:** the units table stores tetrode numbers where NWB expects electrode-table row indices (a format error). Read as tetrode numbers, the regions match the paper's counts; read as rows, up to 32 units per animal land in the wrong region.
- **Missing unit information:** there are no cell numbers, waveforms or interneuron labels, so the paper's interneuron lists cannot be applied. Units clustered only in later epochs are appended to the table without a note.
- **Duplicate LFP:** `acquisition/ElectricalSeries` is a byte-identical second copy of the 1.5 kHz LFP; there is no 30 kHz recording.
- **Other metadata:**
  - The position reference frame says "center well", but the positions are camera coordinates.
  - The session start times are the conversion time.
  - The epochs carry no names.
  - The files hold no linearized positions, ripple times or theta times.
  - The AM2 electrode labels and group names disagree.
- **Missing data:** the de novo sessions and the F-N-F'-N' rats are not in the dandiset.
- **Paper's code:** the Figure 2F batch script's `if ep == 1` never fires on epochs 2 and 4, so it takes the first ten N trials, against its own comment "last 10 trials".
- **Version:** I pinned 0.250724.2224, the latest. The paper cites no version, and 0.230316.2133 holds the same data arrays.

**Assumptions:**
- Linearization onto W-shaped paths built from the well and run positions.
- 8-cm 1D smoothing (the width is garbled in the text).
- Trial -1 is the last N trial; for S3D, trials of N then N'.
- Empty 1-cm bins in single-trial maps are filled linearly. Without this, the PFC embedding split into clusters by which animals' cells were all zero.
- A population vector needs at least 3 cells.
- For the geometric null, a variable's CCGP is the mean over its decoders.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings): the smoothing width, the idealized track paths, the Figure 2F trials, the Figure S3D trial numbering, signed or absolute SI in Figure S5F, the ramping regression and its denominators, and the space of the geometric null model.

**Questions to a reader:** none.

## 3. Where the protocol was unclear

1. Several criteria have no partial clause, yet one part of the claim holds (fig2e, fig3j, fig4d-pfc, figs7d). I used `partially_reproduced` and said which part fails.
2. The open smoothing width affects many claims, but only fig2d's criterion says what to do when the widths disagree. For the others I adopted 8 cm with `assumed: true` and showed 4 and 2 cm.
3. Blocking for "too few units" when the minimum is my own assumption (figs4-ramping-generalization) is not covered. I blocked it as `other` and gave every result in the notes.
4. Protocol step 1.6 says to adopt the best-supported reading, but the figs5f criterion itself prescribes `methods_underspecified`. I followed the criterion.
5. The ten-minute runtime aim does not fit 1,000-shuffle SVM permutation tests. The notebook takes 20 minutes, and I cut the dichotomy shuffles to 100, recorded as a deviation.
6. The two published versions hold identical data arrays; I checked this while preparing and the header says it was not re-run in the notebook.
7. The sandbox's `/dev/null` mounts show up as untracked dotfiles at the repository root. I left them alone; the workflow should not commit them.

## 4. Runtime and failures

The run took about 2 h 05 min (02:59 to 05:04 UTC); each notebook run takes about 20 minutes. Nothing failed in the final runs. During development:
- The first median-path linearization gave 200 to 390 cm tracks, so I replaced it with the W skeleton.
- The first single-trial embeddings were artefacts of empty bins; fixed by the gap filling above.
- One shell append wrote a stray `nfn.py` at the repository root; I moved it into the helper and deleted it.
