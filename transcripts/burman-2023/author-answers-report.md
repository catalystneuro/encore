There were no questions to answer, so I changed nothing and no claim was re-run.

**Questions.** `questions/burman-2023.yaml` doesn't exist, and no commit in the repository's history ever created it. My first author run asked no questions (its report says "Questions to a reader: none"). The reader's answer run found nothing to answer and left `claims/burman-2023.yaml` as it was. Nothing in `claims/`, `attempts/`, `entries/` or `questions/` has changed since the author commit (00af702325). With no amended claim, there were no notes to add and the notebooks, conclusions and attempt record stay as they were.

**Outcomes per claim** (unchanged, so each earlier outcome equals the current one):

| Claim | Earlier | Now |
|---|---|---|
| Dataset holds the 17 files and their fields | reproduced | reproduced |
| Unit counts: 721 kept, 144 excluded, against 662 and 203 | partially reproduced | partially reproduced |
| Synchrony lower awake, 0.3188 against 0.3862 | partially reproduced | partially reproduced |
| Entropy higher awake, 1.389 against 1.150 nats | partially reproduced | partially reproduced |
| Evoked rate higher awake, 14.0 against 7.59 Hz | reproduced | reproduced |
| Synchrony and entropy hold with evoked rate regressed out | reproduced | reproduced |
| Network model: synchrony lower with shunting inhibition | partially reproduced | partially reproduced |
| Network model: entropy higher with shunting inhibition | partially reproduced | partially reproduced |
| Network model: firing rate lower with hyperpolarizing inhibition | reproduced | reproduced |
| Network model: decoding better with shunting inhibition | reproduced | reproduced |
| The remaining claims | blocked | blocked (reasons as recorded) |

**Entry runs.**
- **Lock:** the lock file came out the same as before (Python 3.13).
- **Check and run:** the check reported 0 errors. Both notebooks passed: `reproduce_burman_2023.ipynb` in 201 s and `network_model.ipynb` in 1585 s.
- **Numbers:** the conclusions in the executed copies print the same numbers the record has, such as 721 and 144 units, synchrony 0.3188 and 0.3862, and model entropy 0.4516 and 0.2014.
- **Handover:** written to `executed/burman-2023/handover/`.

I did not verify the work, commit or push.
