I've finished steps 1 to 5 of the author protocol and built the handover. The entry runs clean from a fresh environment (`tools/entry.py all`: 0 errors, about 2 minutes). Nothing is committed, and I did not verify my own work.

**Version pinned.** 0.261020.1002 is the only published version, and the paper cites none. The draft has the same 1014 assets with the same paths and sizes, which the notebook checks.

## 1. Outcomes (38 claims)

| Claim | Outcome |
|---|---|
| figs2-evoked-da-dcp-ccp | reproduced |
| fig3d-anxa1-ramp-to-touch | not reproduced |
| fig3e-dlight-dcp-ccp-reward | partially reproduced: cCP part holds, dCP part does not |
| fig3fg-auc-change-from-baseline | blocked, methods underspecified: the two z-scorings disagree |
| fig4b-speed-correlation-dcp | partially reproduced: dLight holds; Anxa1 is positive in 9 of 10 recordings but p = 0.08 |
| fig4b-speed-correlation-ccp-negative | reproduced |
| fig4c-vame-motifs | not reproduced: the dataset has 42 labels, the paper 37 |
| fig4e-anxa1-high-speed-motifs | partially reproduced |
| fig4f-auc-correlations | reproduced: R = 0.692 and -0.571 |
| fig4h-auc-motif-speed | partially reproduced: R up to 0.68 against 0.83 |
| fig5c-tetx-locomotion | reproduced (immobility not testable) |
| fig5e-early-models-locomotion | reproduced |
| fig5g-pc1-stage | reproduced |
| fig5i-pc1-motif-speed | partially reproduced |
| fig6c-maze-locomotion | not reproduced |
| fig6j-reaching-accuracy | blocked, methods underspecified: the result depends on which mice are the paper's |
| fig5h, fig5j (two claims), fig5m | blocked, metadata insufficient: motif numbers and categories |
| fig6d (two claims) | blocked, data missing: no end-zone entries or rewards |
| fig1b (RNA-seq; its data are in GEO) | blocked, other: GSE282753 has only MitoPark counts, no cMfn2KO |
| 13 histology/qPCR claims and 3 nosepoke claims | blocked, data missing |

## 2. What the dataset holds, and the questions asked

**What it holds.** Only behaviour and photometry. The open field groups of Figure 5 are all there, with exactly the legend's numbers of mice.

**What was found:**
- 86 open field sessions are labelled as `tmaze` (arrow maze) sessions.
- Groups, cohorts, days and test phases exist only as free text in `session_description`.
- Subject genotypes conflict across files: dLight mice are WT in some files and Anxa1-flp or Dat_cre in others. Mouse 779575 is a control in one experiment and a TeTx mouse in another.
- The 42 VAME labels cannot be the paper's numbered motifs. Motif 42 is not a label, and motif 28 is never used by the Figure 5 mice.
- The z-scored open field photometry is smoothed and lags the dF/F by about 0.1 s; neither is documented.
- There are more recordings and mice than the figure legends count, plus cohorts recorded after the preprint, with no record of which the paper used.
- Some descriptions are wrong. The evoked release sessions are called nosepoke self-stimulation, but the trains come every 4 s. Some photometry sessions are called SN cell-body recordings, while the fiber table places them in dCP.

**Questions asked** (`questions/001828.yaml`, six):
1. Which annotated event is the "water drop touch".
2. Which water drop recordings the paper kept.
3. Which laser powers, unit and baseline window apply to the evoked release comparison.
4. What counts as a grasp attempt, and how the preferred forelimb is chosen.
5. Which reaching test phases and mice make up Figure 6J.
6. Where the cMfn2KO counts are, and how technical libraries are combined.

## 3. Where the protocol was unclear or missing something

1. **Two conflicting rules for readings.** Reported numbers count as reproduced under any reading; open details must agree across all readings, or the claim is blocked. I applied "any" to the criterion's own readings (windows, thresholds, scaling). I applied "all must agree" to the header's z-score readings ("judged under both") and to readings I added myself. That rule is why fig3fg and fig6j are blocked.
2. **A criterion part the dataset cannot test** (immobility, motif categories) has no stated rule. I judged on the remaining parts and recorded the gap in the notes.
3. **The dataset contains mice recorded after the preprint was posted.** The protocol does not say whether to restrict to data predating the paper. I ran both mouse sets.
4. **The clock check for continuous sessions** with only continuous variables is not covered. I used the lag of the speed-signal cross-correlation, which is a weak check; the notebook says so.
5. **An "elsewhere" claim whose named deposit holds only part of the data.** It cannot be `data_missing`, so I used `other`.
6. **Readings that disagree only on partial against not reproduced** (fig6c). I recorded not reproduced, since the full criterion fails under every reading.
7. **`measured` when no reading matches.** I recorded the value of the first reading the criterion lists, and said so in the notes.
8. **Mixed RM ANOVA post hoc tests.** Prism's pooled-error Sidak tests were approximated by t-tests with Sidak adjustment, recorded as a deviation.

## 4. Runtime and failures

- **Runtime.** The notebook runs in 123 s.
- **Failures.**
  - A first loader using threads took 22 minutes, because h5py does not run in parallel across threads. Switching to processes brought loading to about a minute.
  - Two notebook bugs (duplicate index labels, a NaN median) were found and fixed before the final run.
  - edgeR could not be used because R is not available; this is part of why fig1b is blocked.
- **Untracked files outside my work.** `scripts/` and the repo-root dotfiles were already there; the dotfiles look like sandbox mounts of `/dev/null`. I left them alone.

Files are in `entries/001828-mantas-2024/` and `executed/001828-mantas-2024/handover/`:
- `attempts/001828-mantas-2024-01.yaml`
- `questions/001828.yaml`
- `entries/001828-mantas-2024/` (`reproduce_mantas_2024.ipynb`, `anxa1.py`, `README.md`, `entry.yaml`, requirements and lock)
- `executed/001828-mantas-2024/handover/`
