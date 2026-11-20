I've finished steps 1 to 5 of the Author section and run the handover; outcomes are in `attempts/saez-2018-01.yaml`. Of the 28 claims, 8 are reproduced, 4 partially reproduced, 10 not reproduced and 6 blocked because the data are missing. `entry.py all` passed with 0 errors and the notebook ran in 909 s. The handover package is in `executed/saez-2018/handover/`. Nothing is committed.

**1. Outcomes**

| claim | outcome |
|---|---|
| methods-electrode-trial-counts | partially reproduced (192 electrodes and 10 patients match; timeouts are 5.1%, not 9.98%) |
| behavior-risk-neutral | reproduced (54.9%) |
| fig1c-choice-win-probability | reproduced |
| figs2a-choice-gamble-ev | reproduced |
| fig1c-patients-like-controls | blocked, data_missing |
| figs2b-rt-conflict | not reproduced (p = 0.165 and 0.104) |
| regressors-past-current-uncorrelated | not reproduced (R2 lower than the paper's) |
| figs6a-regressor-collinearity | reproduced (mean R2 0.155) |
| fig3-present-encoding | not reproduced (counts above Table S2; chosen value not above chance) |
| fig3-latency-duration-similar | reproduced, rests on an assumption |
| hfa-more-than-fp | blocked, data_missing |
| figs4b-power-at-buttonpress | blocked, data_missing |
| fig4-past-encoding | partially reproduced |
| fig5-past-sustained | partially reproduced |
| behavior-past-no-effect | not reproduced (past risk p = 0.015) |
| fig6-past-short-lived | reproduced |
| figs5d-sharp-boundary | reproduced |
| mixed-effects-robust | not reproduced (14 of 16 regressors at best) |
| figs6b-stepwise-similar | partially reproduced, rests on an assumption |
| figs3a-risk-all-trials | not reproduced |
| figs3b-no-motor-encoding | reproduced |
| anatomy-brodmann-counts | blocked, data_missing |
| fig7-all-areas-similar | blocked, data_missing |
| no-anatomical-gradient | blocked, data_missing |
| tables2-patients-coverage | not reproduced (8.62 against 7.41) |
| fig7f-multiplexing | not reproduced, rests on an assumption |
| figs7-present-past-overlap | not reproduced, rests on an assumption |
| fig2-example-electrodes | reproduced |

**2. Dataset, assumptions and questions**

- **Version:** CRCNS does not version data sets, so this is `unversioned`, with the MD5 sums in the notebook header.
- **Duplicated electrodes:** the files hold 199 electrodes. In s03, electrodes 52 to 58 are exact copies of 45 to 51; without them the per-patient counts match Table S2 (192). Electrode 42 has no data of its own: its 1-kHz trace copies electrode 34 and its window averages copy electrode 41. The analysis uses 191 electrodes.
- **Epoch timing:** the epoch described as centred on the button press is centred 470 to 600 ms after the csv's button-press time. The gamble outcome is encoded from about 200 ms after its time 0, so it behaves as locked to the outcome reveal, as Figure 3C labels it.
- **Behaviour file timings:** the csv's reveal time is 31 to 47 ms after the button press in most rounds, not 550 ms.
- **Trial matching:** HFA trials carry no round number and are 86 fewer than the non-timeout rounds, with no documented reason. I matched every trial to its round through the authors' regressor file.
- **s10:** it has 138 rounds and reaction times up to 80 s, with no timeouts.
- **Other mismatches:** prizes are $15 to $30, not $10 to $30. Some columns, the HFA units and the baseline subtraction are not described.
- **Data missing:** there is no broadband signal, no electrode locations and no data from the healthy participants.
- **Readings the data settled:** the authors' regressor file gives win probability as (10 - shown number)/10 and risk as p(1-p). For the previous trial after a timeout, it uses 0 for the choice and outcome regressors. The game epoch is already baseline-corrected.
- **Assumptions:**
  - The second epoch is reveal-locked (fig3-latency).
  - In the stepwise procedure, the longest stretch is taken in each epoch and models are compared at the base regressor's peak window. figs6b, fig7f and figs7 rest on this.
- **Four questions for the paper's authors**, recorded as findings:
  - How the 1,000 shuffles enter the electrode selection. The rule as written labels 18% of electrodes as encoding under shuffled labels, more than Table S2 reports for some regressors.
  - The stepwise details.
  - The mixed-model specification.
  - How the delays and durations are defined.
- I asked no reader any question.

**3. Where the protocol was unclear**

1. The protocol had no case for a dataset whose event label contradicts the data (the second epoch). I kept both timings, used the data's in the main analysis, marked the latency claim `assumed`, and recorded a finding.
2. The protocol does not say whether a reproduced outcome with an assumption should depend on reading the data's timing rather than a method choice. I used `assumed: true`.
3. "Count each recording once" conflicts with matching the paper's total (192 against 191). I analysed 191 and reported 192 for the count claim, recorded as a deviation.
4. The chance-level rule only applies when the paper states a level. Here the paper gives none, but the computed level (18%) is above several of the paper's own counts. I tested as written and recorded a question for the authors without blocking.
5. For figs2b, the criterion defines the outcome for patients only. I judged it on patients and said the healthy-subject part is untestable.

**4. Runtime and failures**

- The notebook takes about 15 to 16 minutes: 5 minutes to stream about 820 MB, and 7 minutes for the 1,824 per-window mixed models.
- The full nested model takes about 20 s per fit. For the per-window reading of the mixed models I therefore used an electrode random intercept only, recorded as a deviation.
- Nothing failed in the final run. Untracked dotfiles and a `scripts` folder in the checkout are not mine; I left them alone.
