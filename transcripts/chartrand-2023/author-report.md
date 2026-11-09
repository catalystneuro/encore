I've finished steps 1 to 5 of the Author section for DANDI:000630 (version 0.230915.2257) and built the handover (step 6) in `executed/000630-chartrand-2023/handover/`. Nothing is committed.

**Pinned version.** I pinned 0.230915.2257 because it is the version the paper cites and the only published one. The draft holds the same 210 assets.

**What I wrote.**
- An entry with three notebooks and a helper module, `entries/000630-chartrand-2023/`.
- The record, `attempts/000630-chartrand-2023-01.yaml`.
- Two added link claims (`dandiset-cell-link`, `mouse-cell-link`) in the claims file, plus `depends_on` entries on the claims that use them. No claim's statement, expected values or criterion was changed.
- One question for a reader, `questions/000630.yaml`.

### 1. Outcomes (41 claims)

| Claim | Outcome |
|---|---|
| dandiset-cell-link (added) | reproduced |
| patchseq-counts | reproduced (194, 96, 35, 33, 15, 15; exactly Table S2) |
| fig2c-subclass-ephys-differences | partially reproduced: initial firing rate FDR p 4.7e-7 on features computed here (1.7e-8 on the paper's own values), against the claim's 1e-7 |
| fig2b-subclass-ephys-profiles | not reproduced: L1 VIP, not PAX6, has the highest initial rate; asked of a reader |
| figs3a-sag-adaptation | not reproduced: R² 0.33 here, 0.36 on the paper's own values, against 0.74 |
| fig2c-lamp5-gradient | partially reproduced (sag gradient too weak) |
| figs6-donor-condition-ephys | reproduced |
| figs6c-region-ephys | reproduced |
| fig4b-mc4r-sag-irregularity | reproduced |
| fig4b-adarb2-irregular-firing | partially reproduced |
| fig5b-tnfaip8l3-ephys | reproduced |
| fig6a-ephys-dprime-subclass-structure | reproduced, resting on an assumption |
| fig6d-gmm-subclass-f1 | reproduced |
| figs8a-classifier-cv | reproduced (83.5%) |
| figs8b-classifier-holdout | blocked, data_missing |
| mouse-cell-link (added) | partially reproduced (250 of 272 mouse cells found in DANDI:000020) |
| fig3d-ephys-species | blocked, methods_underspecified: the criterion requires this when the two ANOVA readings (O2) disagree |
| fig3g-variability-dimensions | reproduced |
| fig4d-mouse-no-rosehip-ephys, fig5d-mouse-pax6-doublets | partially reproduced |
| fig2d-subclass-morphology, fig4b-mc4r-axon, fig5b-tnfaip8l3-dendrites | partially reproduced, on the paper's deposited morphology features |
| figs6a-tumor-dendrite-branching, fig3b-l1-cytoarchitecture | blocked, metadata_insufficient |
| fig3e-tea-validation, fig3f-a-type-conductance | blocked, data_missing |
| fig6b plus 13 transcriptomic and other `elsewhere` claims | blocked, `other` (not attempted) |

Totals: 10 reproduced, 9 partially reproduced, 2 not reproduced, 20 blocked.

### 2. The dataset, assumptions and questions

**What the dataset holds.**
- It holds exactly the paper's primary set: the 210 Seattle cells of the strict L1 set whose features were extracted. The Amsterdam and Szeged recordings are not in it.
- The files carry no t-type, subclass, layer, region or medical condition. They link to the paper's cell table only through the LIMS number in `session_id`.
- 6 files carry a timestamp in place of the cell name.

**Format and metadata problems.**
- 2,586 sweeps that stopped early (in 145 files) hold zeros where IPFX expects missing values. IPFX then reads a spurious spike, so I left those sweeps out.
- `bias_current` is stored in pA, where the NWB schema fixes amperes.
- Two files give age P0D where the donor's age is unknown, and one gives sex "unknown" where the paper's table says M.
- The public table gives a medical condition for only 86 of 194 cells.

**Features.** Features I computed with IPFX agree with the paper's table within 1% for 71 to 98% of cells, feature by feature. Code for 55 of the paper's 94 features was never released, so for those I used the paper's own values, as the claims file allows. I added a `methods_unavailable` finding asking for that code.

**Assumption.** For fig6a I took "high d'" as d′ ≥ 2.2, the Methods' threshold for grouping t-types. This is put to the paper's authors in a finding.

**Other questions for the paper's authors.** Which ANOVA Fig. 3D used. Also, the paper's own per-cell values with its own regression code give R² 0.36, not the 0.74 of Fig. S3A; this is recorded as a `code_mismatch` finding.

**Question to a reader.** In fig2b, does a "high initial firing rate" mean the highest of the four subclasses, or above LAMP5 and MC4R? Under the narrower reading the claim would be reproduced.

### 3. Where the protocol was unclear or did not fit

1. The protocol says outside data supply only labels, but the claims file allows judging on the paper's per-cell features. I followed the claims file, ran every analysis both ways, and recorded it as a deviation.
2. Nothing says when recomputed features count as agreeing. I used a feature if it was within 1% for at least half the cells, and stated this.
3. The fig3d criterion forces methods_underspecified when readings disagree, while step 1.6 allows adopting the best-supported reading. I followed the criterion.
4. There is no `blocked_by` reason for claims not attempted because time went to the dataset claims. I used `other`.
5. The protocol says only reader runs write the claims file, yet authors add link claims there. I added them.
6. Some `elsewhere` claims have no criterion. I took the threshold from the figure legends and recorded it as a deviation.
7. There is no place for findings about an outside input (22 mouse cells missing from DANDI:000020). I used `other`.
8. The clock check is written for trial tables. I used a stimulus-onset contrast instead: −24 mV at the true onset, about 0 with the onset shifted.

### 4. Runtime and failures

The run took about 2 h 25 min (01:28 to 03:54 UTC). In the final clean run all three notebooks pass:

| Notebook | Runtime |
|---|---|
| `reproduce_chartrand_2023.ipynb` | 14.8 min |
| `mouse_comparison.ipynb` | 7.6 min |
| `morphology_tables.ipynb` | 6 s |

`entry.py check` reports 0 errors. Nothing failed in the final run.

The repository root has untracked dotfiles and a `scripts` entry. They are /dev/null mounts from the sandbox, created before the run, and should not be committed.
