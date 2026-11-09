**Verifier report, round 3: Ito & Doya (2015) on DANDI:001642 (0.260205.0153)**

The claims file has 32 claims. Before this round the attempt record gives 11 reproduced, 9 not reproduced and 12 blocked. The author proposes 13 changes, all to blocked (data_missing): neuron-counts and 12 claims that depend on it. I agree that all 13 should be blocked. If every change is accepted the totals are 6 reproduced, 1 not reproduced (fig2g-fq-variable-best) and 25 blocked.

One point is open. For three claims (fig6-above-chance, fig8f-state-value-vs, no-policy-coding) I agree they are blocked, but I am not sure the reason should be data_missing alone; see the note after the table.

| Claim | Proposed | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| neuron-counts | blocked (data_missing) | yes | — | The numbers in cell 30 come from the units table and the spike times. The PETHs use 100 ms bins from −4 to 4 s around event columns 2, 4 and 5 of `real` (cue onset, centre-hole exit, L/R entry), and the EASH uses 10 ms bins with a 10 ms Gaussian, as in the Methods. With condition (3), reading (4i) and no duplicate check, 265 / 224 / 169 units and 213 / 163 / 143 rule PANs remain. None of these is below the lower end of its tolerance (234 / 160.2 / 161.1; 171 / 94.5 / 107.1). These are upper limits of the paper's counts, because the conditions that cannot be applied, (1), (2), (5) and the PETH-similarity part of the duplicate rule (Methods), can only remove units. The files hold no waveforms or recording sites (cell 31), so the claim cannot be decided from the dandiset. Reading (4ii) misses everywhere (49 / 62 / 22 units; 2 / 7 / 4 PANs). The claims file does not name it, and it cannot produce the paper's 190 / 105 / 119 PANs from this dandiset. Even if it were counted as a reading, the readings would disagree, so the claim would still be blocked and not not_reproduced. This decision does not rest on a choice made to reach the result. |
| fig4b-vs-phase1 | blocked (data_missing) | yes | — | `depends_on: [neuron-counts]` in the claims file. The analysis (cells 35–37) runs only on the two unit sets built in cell 33 from cell 30, neither of which can be the paper's set. |
| fig5e-action-info-rises-dls | blocked (data_missing) | yes | — | Depends directly on neuron-counts. Same unit sets (cells 51–52). |
| fig5e-action-info-cue-offset-dls | blocked (data_missing) | yes | — | Depends directly on neuron-counts (cells 54–55). |
| fig5e-action-info-center-exit | blocked (data_missing) | yes | — | Depends directly on neuron-counts (cells 57–58). |
| fig5d-action-info-phase5-dms | blocked (data_missing) | yes | — | Depends directly on neuron-counts (cells 60–61). |
| fig5g-reward-info | blocked (data_missing) | yes | — | Depends directly on neuron-counts (cells 63–64). The claims-file reading of part (1) that I reported in round 2 is still with a reader. |
| fig6-above-chance | blocked (data_missing) | yes (blocked) | blocked; reason see note | The claims file has `depends_on: [fig6-event-coding-proportions]`, and that claim is already blocked (methods_underspecified) and has no proposed change (cells 69–70). The author is right that this claim should already have been blocked; I missed this in rounds 1 and 2. The proposal's reason says a change to blocked (data_missing) is proposed on fig6-event-coding-proportions, but none is. |
| fig8f-state-value-vs | blocked (data_missing) | yes (blocked) | blocked; reason see note | The claims file has `depends_on: [fig8a-d-action-reward-coding]`, which is already blocked (methods_underspecified) and has no proposed change, though the reason says one is proposed (cells 74, 81–82). It should already have been blocked; I missed this earlier. |
| no-policy-coding | blocked (data_missing) | yes (blocked) | blocked; reason see note | Same parent and the same misstatement as fig8f (cells 83–84). It should already have been blocked; I missed this earlier. |
| fig9-temporal-order-all-blocks | blocked (data_missing) | yes | — | Depends directly on neuron-counts (cells 86–88). |
| fig10a-dls-fixed-above-free | blocked (data_missing) | yes | — | Depends on fig9-temporal-order-all-blocks, which is proposed blocked (data_missing) (cells 93–94). |
| fig10b-dms-fixed-above-free | blocked (data_missing) | yes | — | Depends on fig9-temporal-order-all-blocks, which is proposed blocked (data_missing) (cells 95–96). |

**Note on fig6-above-chance, fig8f-state-value-vs and no-policy-coding.** The claim each one depends on directly is recorded as blocked (methods_underspecified). If "blocked for the same reason" (Author step 1.5) means the reason of that direct parent, these three would be methods_underspecified. Their chains also reach neuron-counts, so data_missing is defensible too. Either the record should give both reasons, or the parents should also be marked as reaching data_missing through neuron-counts.

**Other checks.**
- **No dependent claim is missed.** Every claim that depends on neuron-counts, directly or through other claims, is either already blocked or among the 12 proposed. actor-critic-near-chance depends only on fig2g-fq-variable-best, which is not reproduced, so it rightly stays as it is.
- **Claims-file readings to report:** none new. The three still pending are the fig4b first-crossing reading, the single-test rule of fig9-dms-never-above-dls and fig5g part (1).
