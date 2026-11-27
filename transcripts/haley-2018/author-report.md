I've completed steps 1 to 5 and the step-6 handover for haley-2018. Of 30 claims, 11 are reproduced, 6 partially reproduced, 7 not reproduced and 6 blocked. Every tested outcome is marked `assumed`, because the analysis depends on choices the paper left to hand work. Nothing is committed: the workflow will commit `entries/haley-2018/` and `attempts/haley-2018-01.yaml`.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig2a-stg1-traces, fig2bcd-stg1-measures | reproduced (assumed) |
| fig3a-stg-variability-examples | blocked, metadata_insufficient |
| fig3c-stg-rhythmic-fraction | partially reproduced (assumed): 5.5 significant, 10.4 not (p = 0.31) |
| stg-state-transitions | blocked, metadata_insufficient |
| fig3d-stg-frequency | partially reproduced (assumed): the acid ANOVA is significant, where the paper says invariant |
| fig3e-stg-spikes-per-burst | reproduced (assumed) |
| fig3f-stg-duty-cycle | partially reproduced (assumed): no increase at 6.1 |
| fig3s2-stg-control-variability | reproduced (assumed), under reading (b) |
| fig4a-ptx-example, fig4bc-membrane-potential | reproduced (assumed) |
| fig4de-spike-amplitude, fig4fg-ptx-frequency | partially reproduced (assumed) |
| gastric-like-rhythm-counts, gastric-conditions-co-occur, fig5-gastric-recovery-example | blocked, methods_underspecified |
| fig6-cg1-measures | partially reproduced (assumed) |
| fig6a-cg2-less-rhythmic | reproduced (assumed) |
| fig7b-cg-rhythmic-fraction, fig7c-cg-frequency, fig7d-cg-spikes-per-burst | not reproduced (assumed) |
| cg-state-transitions | blocked, metadata_insufficient |
| fig7e-cg-duty-cycle, fig7s2-cg-control-variability | reproduced (assumed) |
| fig8a-ganglion-difference, fig8b-individual-preparations, fig8b-cross-predictive, baseline-frequency-correlations | not reproduced (assumed) |
| robust-6-1-to-8-8, intact-depolarize-in-acid | reproduced (assumed) |

## 2. Dataset, assumptions and questions

**What the dataset holds.** OSF Storage has 408 files: 385 raw .abf and 23 READMEs, all at their pinned versions. I checked the 274 STG and CG files I read whole against their SHA-256 and all match; the live listing shows no changes.

**Findings about the data:**
- Two experiments the paper's code uses are absent: 877_127 (STG) and 887_017 (CG) (major).
- Seven experiments lack one pH step (minor).
- The nine PTX folders have no README, so each file's pH had to be inferred from the recorded bath pH signal (major).
- In 903_058 and 903_060 that signal shows the 9.3 solution was applied before 8.8 (minor).
- In 903_046_0002 the PD and LP channel names are swapped relative to the other ten files of that experiment (major).
- Several READMEs disagree with their folders; for example, 887_145's README lists its files as 887_149_* (minor).
- 877_101 has no pdn channel, so its PD unit can't be isolated (minor).
- The state annotations, Spike2 burst output and gastric annotations behind the figures are not deposited (major).
- The project links a GitHub add-on that returns 403 to an anonymous reader (minor).

**Findings about the paper:**
- The code's 8-minute window is in fact the 480 s after the first burst of each file, not the last 8 minutes. With the code's window, the acid ANOVA on PD frequency gives p = 0.061 (as the paper reports); with the Methods' window it gives p = 1.6e-07.
- The paper's "15 CG preparations" are 15 units from 10 experiments.

**Assumptions:**
- Spike thresholds are set automatically (the authors set them by hand).
- CG bursts use a 1.0 s / 1-spike rule, with the code's 0.3 s / 2-spike values shown as a variant.
- Rhythmic states come from a proxy based on pacemaker bursting, shown with gap factors 2, 3 and 5.
- PTX pH comes from the recorded pH signal.
- The intracellular measures use the code's starting parameters.
- A missing pH step counts as 0, as the code does; leaving it out is shown as a variant.

**Questions for the paper's authors** (one `methods_unavailable` finding): the per-file thresholds; how missing steps entered the statistics; which PTX file is which pH; which file stands for a condition where there are duplicate controls or repeated steps; whether 877_101's PD came from the lvn; and the criteria for a gastric rhythm.

I asked a reader no questions.

## 3. Protocol gaps

1. "Check the sha256 of what you read" can't apply to partial reads. I read the STG and CG files whole (57 GB) and checked them; I read only the last minute of each PTX file and did not hash those.
2. The target list names OSF Storage as the only provider, but the API also lists a GitHub add-on that refuses anonymous access. I recorded it as a minor finding.
3. The OSF API returned 500 errors and timeouts. Since the listing only checks the pin and feeds no result, I added retries and made the cell print "not checked" on failure. One run did time out; I re-ran until the listing succeeded.
4. `assumed: true` ends up on every tested outcome, so it no longer separates outcomes. The deviations say which assumption each one rests on.
5. Where a criterion defines its own "partially" condition I applied it strictly (fig7b and fig8a are therefore not reproduced). Where it has none, I used the protocol's general definition.
6. `measured` is awkward when the expected value is a sample size (fig3c expects 15 preparations); I recorded 13.
7. The 903_046 label swap sits between critical and major in the severity table. I chose major, because the other ten files show the correct names.
8. Clean-run time varied from 10 to 16.5 minutes with network speed; `runtime_minutes` is left at 13.

## 4. Runtime and failures

The work ran from 01:05 to about 02:37 UTC, roughly 1.5 h. The final clean run (`tools/entry.py all`) passed with 0 errors in 989 s at 3.4 GB peak memory. The handover is in `executed/haley-2018/handover/`. One run's OSF listing timed out, as above; nothing else failed.
