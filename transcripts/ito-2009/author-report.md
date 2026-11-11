I did steps 1 to 5 and ran the handover. The entry is `entries/001641-ito-2009/`, the record is `attempts/001641-ito-2009-01.yaml`, and nothing is committed. `tools/entry.py all` passes with 0 errors and the notebook runs in 18 minutes from a clean environment.

## 1. Outcomes (46 claims)

| Claim | Outcome |
|---|---|
| trial-counts, block-structure, reaction-time | reproduced |
| tone-discrimination-errors | not reproduced |
| fig2b-reward-stronger-than-noreward, fig2c-sequence-frequencies, fig2c-reward-effects-fade, fig2d-switching, fig2e-persevering | reproduced |
| fig2b-two-back-history | reproduced (assumption) |
| fig3-lsq-switching | partially reproduced |
| table1-lsq-parameters | not reproduced |
| fig5-markov-accuracy, fig5-constant-models, fig5-variable-models-best | reproduced (assumption) |
| fig5-fq-dfq-beat-all-models, fig5-fq-dfq-no-difference | not reproduced (assumption) |
| binary-prediction-accuracy | reproduced |
| table2-ml-parameters | partially reproduced (assumption) |
| table3-parameter-averages | reproduced (assumption) |
| fig4-strategy-tracking, suppdata1-choice-vs-q-difference | reproduced |
| neuron-counts, firing-rates, fig8b-action-coding, fig8b-reward-coding, fig8b-qr-no-region-difference, preference-balance, fig8-above-chance | reproduced |
| fig8b-state-coding | reproduced (assumption) |
| fig8b-action-value-psth, fig8b-ql-vp-higher, nac-noreward-preference, fig8d-policy | partially reproduced |
| fig8b-action-command-coding, fig8b-nac-vp-same-event-coding | not reproduced |
| core-shell-no-difference | blocked (metadata_insufficient) |
| fig8c-regression-action-value, fig8d-state-value-vp-higher | not reproduced |
| fig8c-ql-vp-higher, fig8c-regression-detects-more | reproduced |
| fig9-state-information, fig9-action-information, fig9-action-value-information-low, action-information-outlasts-reward-peak | reproduced |
| fig9-reward-information | partially reproduced |

Totals: 29 reproduced, 7 partially reproduced, 9 not reproduced, 1 blocked. Many numbers match the paper to the last digit: 39,175 / 12,707 / 8329 trials, 148 NAc and 66 VP units, 80 and 33 state-coding units, and normalized likelihoods 0.5304 / 0.5374 / 0.5369 against the paper's 0.5304 / 0.5375 / 0.5368.

## 2. Dataset, assumptions, questions

**Version.** Only one version is published, 0.260922.0719, and the paper cites none, so I pinned that one.

**Findings about the dataset:**
- The trial `result` codes are not described anywhere in the files, so the error types cannot be told apart. This is why the tone-discrimination error rates could not be recounted.
- The no-reward tone is stored in the `SpTone Err` series together with the error tone. The two differ only by duration, and the error tone lasts about 2 s where the paper says 1 s.
- Units are labelled only NAc or VP. There is no core or shell assignment, which is what blocks that claim.
- 18 of the 70 files have no units table.
- Three choice trials have negative reaction times, and one error trial has no `state`.
- No recording appears twice.
- The paper contradicts itself in two places: its total of 60,221 trials is 10 more than its own parts (60,211, which is what the dataset holds), and its Results text conflicts with its own Markov numbers.

**Assumptions.** Each is a `methods_unavailable` finding with a question for the paper's authors:
- **Q update form (O1 a):** the only form whose fitted parameters match Tables 2 and 3.
- **Training/test split (O3 a):** alternate sessions; the only split that gives the paper's 19,986 training trials exactly.
- **Local matching law starting value:** it needs a non-zero initial value; with Qi(1) = 0 it is undefined.
- **What the Fig. 2 Mann-Whitney tests rank (O8 a):** the choices of all following trials; this is the reading that gives the paper's p = 0.94.
- **State-coding trials (O14 a):** error trials excluded, which gives exactly 80 and 33 units.
- **How sigma_alpha and sigma_kappa were searched:** asked only. The training likelihood is nearly flat over the grid, so the fitted sigmas and the Fig. 5 paired tests depend on the search.

**Questions to a reader:** none. I found no place where the claims file misreads the paper.

## 3. Where the protocol was unclear, wrong or missing something

1. **Which rule decides when readings disagree.** The claims file's opening comment says disagreeing readings mean `methods_underspecified`; protocol step 1.6 (and the prompt) allow adopting the best-supported reading as an assumption. I followed step 1.6 and marked those outcomes `assumed: true`.
2. **No partial rule in some criteria.** fig9-reward-information has no partial clause, but two of its three parts hold. I used the protocol's definition ("holds only in part") and said so in the notes.
3. **Unidentifiable parameters.** The criterion counts the F-Q Q0 of Table 1 as a value to match, but it cancels out of the fit, so any value is optimal. I reported this and kept the count as written.
4. **Clock check per session.** The spike-clock check could not be shown in 15 sessions, which have few units. I reported those as "consistent with the data", not shown.
5. **Time budget against "run every reading".** A full sigma search at 5000 particles for every reading did not fit the notebook limit. I searched with 1000 particles on a 4 × 4 grid, then ran the chosen sigmas with 5000, and recorded this as a deviation.

## 4. Runtime and failures

The run took about 1 h 45 min of the 5 h. The final notebook executes in 1092 s. One development run was wasted on a harness bug that re-ran the 13-minute model fits; it did not affect the entry. Nothing in the final runs failed.
