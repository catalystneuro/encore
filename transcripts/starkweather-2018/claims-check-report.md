I checked the claims file and it is fit for an attempt: the new `checks` entry says `ready: true`. Nothing is committed.

**Checker:** `claims/starkweather-2018.yaml: 32 claims, 32 quotes, 52 statistical values, 16 problems`. All 16 problems are "value not found" flags on p-values. Each one is in the text, where the extraction prints "× 10⁻ᵏ" as "3 10" plus a garbled minus sign. I read and matched every one. All quotes pass word for word.

I also read the paper's model code (github.com/cstarkweather/Starkweather2018 at commit d667730). It confirms the settings the file gives: gamma 0.93, alpha 0.1, 500 training sessions of 50 trials, noise at SNR 12, and slopes as straight-line fits of the reward-time RPE.

**Changes, by claim:**
- **fig3g-anticipatory-licking:** the criterion presented its windows and observation unit as the paper's, and gave odor D a "span to reward" although odor D has no reward. The paper gives neither. I named the readings for the windows (equal-span counts, or rates against the 1 s before odor onset) and set the odor D span to 0–2.8 s as a standard choice. I also noted that the error df (36 and 41) fit no design over the 38 and 40 sessions per task that Figure S3A implies.
- **figs3-task1-licks-more-sooner:** the paper does not say which trials the sigmoid fits use. I named two readings: the 2.8 s trials, or all odor A trials.
- **figs3-salb-spares-licking:** added the tests the criterion relies on but the statistics left out: epoch lick rates, lick slope and sigmoid steepness (Figure S3B, C, F, I).
- **figs5d-omission-unchanged-by-salb:** the paper names neither the test nor the group the Bonferroni correction covers. I named two tests (rank-sum and one-way ANOVA) and two correction groups (all epochs, or each trial type) as readings.
- **figs5c-odorbc-normalized** and **anova-slopes-task-drug:** added that the error df of all five ANOVAs imply 167 of the 172 neurons. That supports leaving out neurons without a free water response.
- **fig7fgh-model-belief-impaired:** the file said the code impairs every task. In the code the impairment changes nothing in task 1, so only task 2 is impaired, as the Methods say. I removed the false second reading.
- **fig7ijk-model-timing-impaired:** the paper says pre-reward RPEs flatten in both tasks, but the statement and criterion had task 1 only. Both now include task 2.
- **New claim figs6ce-kord-task1-animal:** KORD inhibited most mPFC neurons in the task 1 mouse (Figure S6C to S6E). This control finding had no claim. Its baseline is the first 5 min after SalB, as the legend says.

**Still open:**
- **fig5f-task2-significant-slopes-shift:** a Fisher exact test on the printed counts gives p = 0.037, not the reported 0.041. The result is the same at 0.05, so I left the claim as it is.
- **fig2-kord-suppresses-mpfc:** the counts in Figure 2's pie charts (377, 202, 124, 32) can't be assigned to groups from the extracted text, and the PDF could not be rendered here. The claim rests on the Results' "more than 60%".
- **Degrees of freedom:** in fig4b-odorc-below-latest-odora, fig6ab-odorc-above-odorb, fig6cd-omission-dips-intact and anova-time-task-drug-interaction (error df 1347) they don't follow from the neuron counts. The criteria already name the readings and ask for the counts used.
