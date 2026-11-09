I answered all 15 questions, recorded the answers in `claims/000006/10.1038-s41586-018-0642-9.yaml` and set `answered: 2026-10-20` on each. `tools/claims_check.py` reports 0 problems, and nothing is committed.

Sources I added beyond the paper text: the code in the Figshare archives (Ephys, Seq and Axons). I also listed Anatomy.zip, read the Supplementary Information PDF from the publisher, and checked which trials carry rates in the paper's own processed files (not the dandiset).

1. **pt-tagged-units:** The other claims use the code's per-unit rule, with the Methods' session rule as a variant. The attempt reports that this rule gives the paper's 61, 69 and 130 kept on the paper's processed data; I did not run it myself.
2. **pt-single-neuron-early-selectivity:** Each unit uses its own range of trials, reading (a). Your premise held for that one session but not across the files: units in the same session often start and end on different trials (WR29.5 session 2 starts at trial 12 for one unit and 41 for another).
3. **pt-upper-early-preparatory:** The paper gives no rule for "larger", so both rules stay and the claim stays blocked while they disagree.
4. **pt-cd-change-at-go-cue:** Neither the paper nor `CDCorrelation.m` fixes a level or a measure of speed, so both levels stay.
5. **pt-lower-movement-termination:** The paper gives no windows, so both readings stay. The last lick is the code's (`getLickInfo`). A rebuilt last lick is a deviation, acceptable if the outcome holds with the disagreeing trials left out.
6. **pt-depth:** Yes, judge on the unit depth. Fig. 4e plots that field, and the Methods say unit depths came from manipulator readings.
7. **pt-lower-heterogeneous-rates:** Yes. The dependency is now pt-tagged-units, since the claim uses only the rate definitions of pt-spike-rates-similar.
8. **pt-types-transcriptomic:** The 27 are the 26 clusters named in Fig. 1a plus the Cajal-Retzius cluster, which the legend says was left out. That matches your count of clusters not named for VISp, Cajal-Retzius included.
9. **pt-projection-cluster-mapping:** The paper doesn't say. Its notebook groups the same cells by `inj_roi_label` (IRN, VAL, PG, SC|SCm). That grouping and `inj_primary_label` with the Allen ontology are both readings; the claim holds if both counts match under one.
10. **pt-bulk-sc-fold-change-correlation:** The legend's log2(CPM + 1) decides. The code applies log2(x + 1) to `bulk_data.txt`, which holds raw counts, so the code's version is a variant.
11. **pt-upper-thalamus-projection (and pt-lower-medulla-projection):** Supplementary Table 1 fixes which neurons are in each group, the same as the code's hand grouping. The paper gives no rule for "innervated" or "bypassed", so three readings are named. Each count holds if it matches under one.
12. **pt-types-account-for-all-pt:** Supplementary Table 1 lists the 18 by ID, and AA0134 is one of them.
13. **pt-marker-genes:** Yes, `data: dataset`. The smFISH data are in no archive the paper names, and the old `where` pointing to Anatomy.zip was wrong, so I removed it.
14. **pt-retrograde-sublaminae:** No counting method exists in the paper or its code, so the claim stays blocked. The Anatomy.zip folder names also show no superior colliculus labelling, which the 77.1% needs.
15. **pt-types-shared-targets:** No. The second part comes from the bulk labelling images, which the paper analyses with no stated method. Testing it on the reconstructions is a variant.

Two answers change claim fields other than criteria: pt-lower-heterogeneous-rates now depends on pt-tagged-units, and pt-marker-genes is now `dataset` with no `where`. I also changed the source of pt-types-account-for-all-pt to cite the Supplementary Information.
