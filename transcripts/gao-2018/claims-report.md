I've written `claims/gao-2018.yaml` with 44 claims. The quote checker passes with 0 problems; nothing was committed.

**Text read**
- **Main paper:** the NIH author manuscript (PMC6212318) from Europe PMC: main text, Methods, and the legends of Figs. 1–4 and Extended Data Figs. 1–10.
- **Supplement 1:** the Supplementary Information, including Supplemental Table 1, which lists the mice and manipulated hemispheres.
- **Supplement 2:** the reporting summary.
- **No PDF of the main paper**, so anything shown only inside the figures (values, which bar a significance mark belongs to) could not be read. Claims rest on the text and legends.
- **No code:** the paper links none. It says code is "available ... upon reasonable request" and "will be deposited on CRCNS.org", with no identifier.
- **Dataset:** its archive description reads "Extracellular recording in ALM".

**Counts**
- All 44 claims have quotes; none needed `inferred`.
- 16 claims carry statistics (21 values), 18 have expected values with tolerances, and all 44 have criteria.
- The claims cover lesions, photo-activation and photo-inhibition behavior, ALM and CN selectivity, the cross-area perturbations, anatomy, coding-direction analyses and the Extended Data Fig. 10 experiments.

**Details the paper leaves open, with the readings named**
- **Response epoch window:** 1.3 s from the go cue, or the 1.5 s answer window.
- **Trials in the selectivity test:** correct trials only, or all trials grouped by instructed direction.
- **Preferred trial type:** whether the 10 or 20 trials that fix it are counted in total or per type, and which epoch fixes it.
- **Trials in photostimulation tests:** all trials, or correct trials only.
- **Neurons entering the latency estimate:** modulated during the photostimulus, or over the whole delay.
- **Denominator for 59%/35% preparatory and 67%/66% peri-movement:** all neurons, or selective neurons.
- **CN n = 197 in Fig. 2d:** all 416 selective neurons, or only those with sample or delay selectivity.
- **Window for "selectivity abolished":** the whole delay, or the last 500 ms. "Collapse" along the coding direction is read as either indistinguishable from zero or lower than control.
- **Fig. 4f "persists >1 s":** compared against the 1% chance level, or against the fraction before the photostimulus.
- **Mean rate of 4.15 vs 4.39 spikes/s:** over all 454 neurons or the 197 modulated ones, and with a paired or unpaired t-test.
- **Lick-modulation t-test:** paired or unpaired.
- **"Captured fraction" of selectivity:** a ratio of RMS values or of their squares. The baseline window is also not given.
- **VGAT performance percentages:** pooled over trials, or averaged over mice.

**Choices I made where the paper gives none**
- Several absence claims have no test in the paper (licking unaffected, Extended Data Fig. 10d). I used the Methods' hierarchical bootstrap or a logistic regression and labelled each as a choice in the criterion.
- How trials are split for the coding direction is not given. I used a random half split as a standard choice.

**Gaps that affect claims**
- Two legends give p-values without the figure to show which bar each belongs to (Extended Data Fig. 2h: p = 0.04 and 0.0002; Extended Data Fig. 10f–g). Both values are recorded.
- It is not clear which mice carried bilateral ALM photo-inhibition during ALM recording (Extended Data Fig. 10c, n = 690 trials). Supplemental Table 1 lists no such mice.
- The number of ALM-recorded mice disagrees: the Methods add up to 12 (10 left, 2 right) but the table lists 13.
- The CN, anatomy and behavior-only claims are kept as findings, but the dataset described as ALM recordings likely does not hold their data.

Nothing the claims needed was missing from the text itself.
