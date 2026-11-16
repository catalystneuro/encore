I've finished the attempt on CRCNS aa-5 (steps 1 to 6). The entry passes `entry.py all`: the notebook ran end to end from a clean environment with no errors. The handover package is built in `executed/robotka-2023/handover/`. Nothing is committed.

## 1. Outcomes per claim

| claim | outcome |
|---|---|
| stimulus-set-link | reproduced (110 stimuli, per-call-type counts exactly the paper's, 4 birds) |
| paper-good-units-link (link claim I added) | partially reproduced: 91 of the paper's 100 listed good units are in the dataset |
| auditory-units | reproduced: 287 of 726 (39.5%); paper 292 of 730 (40.1%) |
| inhibited-units | reproduced: 47 of 287 (16.4%) |
| table1-snr | reproduced: mean 6.84, median 6.07 |
| pcs-variance | reproduced: 92.4% |
| fig3c-peak-call-types | reproduced, assumed (rests on the code's definition of the per-call-type response) |
| fig4a-unit-z-vs-zt | reproduced: 10.75% vs 12.17%, t(186) = 8.99 |
| good-units-100 | not reproduced: 89, one below the tolerance of 90 to 110 |
| fig4b-ensemble-20 | reproduced, assumed: 43.2% vs 30.4% |
| fig4b-top-ensembles | reproduced, assumed: 48.8% |
| fig4b-confusions | reproduced: all 4 error pairs among the two largest of their rows |
| figs4-per-bird-and-sex | blocked (other): ZF6M has only 10 good units, fewer than the 15 the test needs |
| fig5e-volume | partially reproduced, assumed: R2adj 0.120 against 0.1 ± 0.01 |
| fig5f-si-unrelated | reproduced: p = 0.85 |
| fig5g-entropy-selectivity | reproduced: negative slope, p = 0.031 |
| fig5h-neural-noise | partially reproduced: R2adj 0.21 |
| fig5-multiple-regression | partially reproduced, assumed: R2adj 0.252 against 0.22 ± 0.022 |
| figs6, figs5-region-anova, figs9 | blocked (metadata_insufficient): no brain area per unit |
| fig6a, acoustic-labels-decoding, both fig6c claims, figs10 | blocked (data_missing): the lab's vocalization database is not public |
| four claims on the anesthetized dataset (CRCNS aa-4) | blocked (other): aa-4 not analysed in this run |

## 2. Dataset, assumptions, questions

**What the dataset holds:**
- 50 site files (164 GB of tar.gz) holding 872 unit pickles. 34 pickles are empty and 112 hold song stimuli only.
- No unit carries a brain area, so the claims by area cannot be tested.
- Nine of the paper's good units come from a site sorting named `ZF4F_2t_190613_101015.old`, which is not deposited. The deposited site of that name holds 18 other clusters.
- The data descriptor gives `KDE_BW` in seconds, but its values (0.2 to 10) can only be milliseconds.
- Each tar holds a macOS `._` resource-fork file for every pickle, and the pickles were written with pandas 1.x, so they need pandas' pickle compatibility layer.
- No recording was deposited twice. Spike times lock to stimulus onset: decoding from the pre-onset window gives chance, the post-onset window does not.

**Assumptions:**
- The decoder's cross-validation. The Methods hold out one exemplar per call type; the paper's code holds out one random trial per stimulus. I judged the ensemble claims on the code's scheme, because only it gives the paper's numbers (43.2% against 32.0% under the Methods' scheme). Both are shown in the notebook.
- For fig3c, the per-call-type response is the code's definition, which is what Figure 3C plots (`SummaryStatistics.ipynb`). Under the Methods' definition the claim would not be reproduced.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- Which cross-validation scheme produced Figures 4 and 5?
- How was a stable count of exactly 100 good units obtained, when here the count moves from 87 to 101 between random seeds?

**Questions to a reader:** none.

## 3. Where the protocol was unclear or did not fit

1. `archives.md` covers CRCNS zip files only, but this dataset is tar.gz, which cannot be read out of order. I stream every site in full, decompressing with isal, four sites at a time (17 min).
2. Developing on a subset does not fit a dataset where every claim needs a full pass. I streamed the whole dataset once and developed on a reduced copy kept in `$TMPDIR`, outside the entry.
3. The protocol treats a random seed as a choice that cannot change an outcome, but here the good-unit count crosses the tolerance edge depending on the seed. I judged it on the first seed, as the criterion says, and reported the range over 10 other seeds (8 of 10 within tolerance).
4. It is not clear whether one assumption (the cross-validation scheme) may be adopted across many claims. I adopted it consistently and marked each affected outcome `assumed`.
5. No `blocked_by` value fits claims on public outside data (aa-4, 6.9 GB) that were not run for lack of time; `too_large` is for a computation that stops. I used `other`.
6. The paper's code prints the names of its 100 good units, but the claims file does not name that list as an input. I added a link claim and listed the code repository under `inputs`.
7. The link claim's evidence spans two cells, one of them a data-check cell, while the protocol expects one tagged output.

## 4. Runtime and failures

The notebook runs in 35.5 min (16.9 min of it streaming), with peak memory of 4.2 GB. It ran in full twice; the second run followed a text fix and the added link claim. Nothing failed.
