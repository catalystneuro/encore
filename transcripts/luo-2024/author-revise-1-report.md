The round-1 revision is done. The notebook ran cleanly from a fresh environment (`python tools/entry.py all`, 100 s), `entry.py check` reports 0 errors, and the attempt record passes its schema.

**The main fix (problem 1).** The verifier was right. In 8 files (six mouse cholinergic neurons and two macaque neurons of M#11), a 100 ms, -20 pA test pulse starts at 0.3 s and the step at 1.0 s. Taking the first non-zero stimulus sample as the onset put the analysis window on the test pulse. The onset is now the start of each sweep's longest run of non-zero current. That moves exactly those 170 sweeps. Every other test pulse starts 1.3 s or more after the step, outside the window. The 8 "non-responsive" neurons were an error of this attempt: every neuron now depolarises, and the old tau outliers (401 ms) are gone. I removed that finding and the variant built on it.

**Outcome changes:**
- **fig2-mouse-c-nc-15-of-18:** not reproduced → reproduced. 13 of 17 features differ, within the 13 to 15 range. The notes say that one of the 13, AHP width, differs in the opposite direction to the paper; without it the count would be 12.
- **fig7-macaque-mouse-feature-count:** not reproduced → reproduced. 14 of 17 differ, at the lower edge of the criterion's 14 to 16.
- **figs2-2-mouse-amplitude-cv-sag:** partially → reproduced. The claims file's rule for a saturated sag step is now implemented (problem 8). Seven mouse neurons have -60 pA responses clipped at -100 or -105.5 mV. Sag p = 1.8e-3; on the plain -60 pA step, shown as a variant, p = 0.011.
- **fig2d-mouse-ahp, fig2d-mouse-passive, fig7-macaque-spike-width:** partially → not reproduced. These now follow the criterion, as the verifier argued: a test that fails does not count as partial.
- The other 22 outcomes are unchanged, with the numbers updated.

**Other corrections:**
- **AHP width (problem 3):** now measured within the 100 ms window, as the claims file's F14 says; the old reading is a variant. Both give the same direction.
- **Rank-sum test (problem 6):** now uses MATLAB's tie and continuity corrections.
- **Cross-validation leak (problem 7):** imputation and scaling are fitted on the training folds only.
- **Direction check (problem 9):** the feature counts now list any feature that differs against the paper's direction.
- **Rescaled macaque file (problem 4):** added as a variant, divided by 20. No outcome changes.
- **ChAT-unknown label (problem 10):** the notebook prints the four group labels and states that none marks ChAT-unknown neurons.

**Outputs the verifier asked for:**
- A per-file table of step onset against first non-zero sample, and a whole-sweep plot of voltage and stimulus.
- Tau fit R² for every neuron, and plots of the mouse traces with tau above 100 ms.
- The `general/notes` contents, which hold only a bregma position.
- A UMAP sensitivity check (n_neighbors 5 and 30, min_dist 0.1 and 0.5). Neither UMAP outcome changes.

**Findings added:** a code_mismatch for tau (the code's step gives the paper's values, the -20 pA step does not), plus the test-pulse placement and the clipped -60 pA responses. Other findings are updated to the new numbers.

**Not changed:** I did not change the AHP claims (problem 2). The claims file makes the Methods' window decide, and the paper's values match the code's window. As the protocol says, I added this to `questions/001261.yaml` for a reader and kept testing the claim as written.

The round-1 verification is recorded in the attempt record. For each claim it notes whether the verifier agreed, its outcome and reason, and my response. It disagreed on fig2d-mouse-ahp, fig2d-mouse-passive and fig7-macaque-spike-width, and I changed those to its outcome. Nothing is committed.
