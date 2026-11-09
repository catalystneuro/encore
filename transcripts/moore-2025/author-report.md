I'm done with steps 1 to 6 and the entry passes `check` and `run`. Of the 27 claims, 14 are reproduced, 10 partially reproduced, 2 not reproduced and 1 blocked. I used the paper's full text: the bioRxiv preprint is open access (CC BY-NC). The claims come from version 1, whose title you named and which the dandiset links. I also read the revised version 2 (January 2026), used its Methods only where version 1 says nothing, and put its numbers in the notes. Nothing is committed.

## 1. Outcomes per claim

| Claim | Outcome |
|---|---|
| unit-counts | partially reproduced (3 of 4 groups exact) |
| units-per-recording | partially reproduced |
| figs1c-juvenile-behaviour-similar | reproduced (speed while active p = 0.0504) |
| figs2c-adult-behaviour-similar | reproduced |
| figs1-juvenile-cell-metrics-similar | reproduced |
| figs2-adult-cell-metrics-similar | reproduced |
| fig1ef-juvenile-sharper-tuning | partially reproduced (HD information p = 0.033; half-width no) |
| fig1g-juvenile-halves-correlation | partially reproduced (r 0.76 and 0.84 against the paper's 0.90 and 0.95) |
| fig1h-juvenile-smaller-offset | reproduced (p = 0.0125) |
| fig1j-juvenile-less-drift | not reproduced (p = 0.079, same direction) |
| figs1j-juvenile-epochs-correlation | partially reproduced |
| figs1k-juvenile-epoch-drift-similar | reproduced |
| fig2c-juvenile-isomap-wake-correlation | reproduced |
| fig2d-juvenile-isomap-wake-sharper | reproduced (p = 0.046) |
| fig2g-juvenile-isomap-rem-correlation | partially reproduced |
| fig2h-juvenile-isomap-rem-sharper | not reproduced (p = 0.056, same direction) |
| fig3ef-adult-tuning-similar | reproduced |
| fig3g-adult-halves-correlation | partially reproduced |
| fig3h-adult-larger-offset | reproduced (p = 0.040) |
| fig3j-adult-more-drift | reproduced (t(9) = 2.75, p = 0.022) |
| figs2j-adult-epochs-correlation | partially reproduced |
| figs2k-adult-epoch-drift-larger | reproduced |
| fig4c-adult-isomap-wake-correlation | partially reproduced |
| fig4d-adult-isomap-wake-similar | reproduced |
| fig4g-adult-isomap-rem-correlation | partially reproduced |
| fig4h-adult-isomap-rem-similar | reproduced |
| figs1d-probe-in-posub | blocked (other: histology images with no annotation) |

## 2. What was found about the dandiset

- **Version:** I pinned 0.260917.2322, the most recent published version. The paper cites no version. The two published versions hold the same 98 assets (36 NWB files) and differ only in title and description.
- **Group labels:** with the archive's labels, the paper's unit counts cannot be reproduced. They match exactly (406, 372 and 543 units in 7, 5 and 6 rats) only if H3026, labelled wild type, is a juvenile Fmr1-/y rat and H3029, whose birth date makes it 97 days old, is a juvenile wild type. The main analysis uses that grouping and shows the archive's labels as a variant. Under the archive's labels the juvenile effects weaken.
- **Duplicate file:** H4825's file is H4824's recording, re-timed onto H4825's epochs and clipped at its end (131,373 spikes share the last timestamp). H4825's own data are missing, so the adult Fmr1-/y group has 5 rats and 440 units where the paper has 6 and 507.
- **Birth dates and age:** H3023 and H3026 have birth dates after their recordings, and no file sets the subject's age.
- **Units table:** it holds only spike times and mean waveforms, with no cell type, quality metric or depth. The paper's exclusion of cells re-recorded on the next day therefore cannot be repeated.
- **Epoch tables:** they mislabel or merge the exploration sessions in several files, and H4823 has a single epoch. I took the sessions from the tracking instead. A cue-rotation session in most files is not described in version 1.
- **Position units:** two files state centimetres but hold pixels, and their head direction uses a different range.
- **Format errors:** one unit has spike times out of order, and 22 of 24 juvenile files repeat tracking timestamps.
- **Archive metadata:** the `about` field lists "Fmr1 protein, rat" as anatomy with the disorder's MeSH identifier.
- **Clock check:** spikes and tracking share a clock in 32 of 35 recordings. In the other three the cells are too weakly tuned to show it.
- **Code:** the linked repository, woodcode at commit 61ee178, is the lab's general library, not the paper's analysis code.

## 3. Points where the protocol was unclear, wrong or missing something

1. **Two preprint versions under one DOI.** The protocol says nothing about this. I used version 1 for the claims and version 2's Methods only where version 1 says nothing, and recorded this in the claims file's opening comment.
2. **Correlation values outside tolerance.** My criteria said nothing for values outside tolerance when the effect is present but weaker. I applied the protocol's definition of partially reproduced and recorded it as a deviation. The protocol could say how expected-value claims become partial.
3. **Group labels that conflict with the paper.** The protocol does not say which grouping to treat as main when the archive's labels contradict the paper's own counts. I used the count-matched grouping, fixed it before any claim analysis, and showed the archive's labels as a variant.
4. **Counting the duplicate file.** "Count each recording once" conflicts with a count claim that only matches if the duplicate is counted. I counted it once and reported the double count as a variant.
5. **Linked code that is not the paper's code.** Step 1.5 assumes the linked code is the paper's analysis. Here it is a general library; I used it only for choices the Methods leave open.
6. **Absence claims with several tests.** The protocol gives no rule for claims of absence that rest on several tests (four cell metrics). I set my own rule in the criterion.
7. **Blocking reason for histology.** No category fits images that need expert judgement. I used `other`.
8. **Contamination threshold.** The Methods' "units below 0.5 excluded" would remove almost every unit. I read it as "above 0.5" and recorded this as a paper inconsistency.

## 4. Runtime and failures

- **Runtime:** `entry.py all` passed with the notebook running in 154 to 162 s. The handover is in `executed/001699-moore-2025/handover/`.
- **Mixed model:** the statsmodels fits failed to converge on several measures, one giving p = 1.0. I replaced them with an exact profile-likelihood fit of the same random-intercept model. It matched statsmodels to 8 digits on a synthetic case.
- **Speed-up:** Isomap is fitted on at most 3000 bins per session to keep the run short, recorded as a deviation.
- **Stray files:** `git status` shows untracked entries at the repo root (`.bashrc`, `.gitconfig`, `.idea`, `scripts` and others). I did not create them: they are read-only placeholders put there by the sandbox. Make sure the workflow does not commit them.

Files are in `claims/001699/`, `entries/001699-moore-2025/` and `attempts/001699-moore-2025-01.yaml`:
- 10.1101-2025.01.09.632139.yaml
- reproduce_moore_2025.ipynb
- hdfx.py
- entry.yaml
- README.md
- 001699-moore-2025-01.yaml
