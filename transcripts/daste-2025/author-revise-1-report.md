I've worked through every point in the round-1 report, re-run the entry with `python tools/entry.py all entries/daste-2025` (both notebooks pass: passive in 23.5 min, Go/NoGo in 15.5 min), and rewritten the conclusions to match the new numbers. Round 1 is recorded under `verifications`, with the verifier's reasons in its own words and a `response` for each claim. `tools/entry.py check` reports 0 errors. Nothing is committed.

## Outcome changes

| Claim | Before | Now | Why |
|---|---|---|---|
| fig3de-concentration-decoding | partially reproduced | not reproduced | I took the verifier's outcome: the criterion has no partial outcome, and its "mPFC-p close to chance" condition fails under both window widths. |
| fig5f-stability | partially reproduced | not reproduced | Same reasoning: the criterion needs all three valence schemes to hold. |
| fig4ij-valence-correct-trials | not reproduced | reproduced, resting on an assumption | See below. |
| fig2b-lifetime-sparseness-similar | not reproduced | not reproduced, now marked as resting on an assumption | The result depends on how never-active neurons are handled. |

**The correct-trial tables were not at the paper's chance level (the verifier's point 2).** The day-3 correct-trial table is 77% rewarded-odor trials (17, 6, 4 and 3 per odor). With shuffled labels, valence decoding scores 65–69% on it, not the paper's 50%, so this was not the paper's procedure.
- The paper's figure legend says days 1–2 were dropped because of imbalanced correct-trial counts. That supports a balanced table, so I truncated each odor to 3 trials. Its shuffled level is 42–51%.
- On that balanced table, every condition of fig4ij holds under the maximum aggregate.
- The weakness: it rests on only 12 trials. This is recorded as an assumption, with a question to the paper's authors in the findings.
- figs8 stays not reproduced on both tables.

## What I added or corrected

- **Clock check for the two mPFC mice (sub-2456, sub-2457):** I added a per-session decoding table (1 s windows, days 1–3) and frame-by-frame mean traces around odor onset.
  - The onset frame matches the files' own `stim_onset_frame` in every trial, and decoding before onset stays at the shuffled level.
  - The two mice decode later and less well on all three days. This fits a shared clock with slower or weaker responses, but does not prove it.
  - Decoding each mouse's own tagged cells shows all three mPFC mice weakest in the odor phase, so the fig4def pattern is not carried by those two alone. Its outcome is unchanged.
- **Chance levels:** trial counts per odor and per valence, and shuffled-label accuracy, for every day-3 table.
- **fig2b:** variants that keep never-active neurons. Setting their sparseness to 0 would reproduce the claim; setting it to 1 would not.
- **figs10e:** a 95% interval on the OB-p vs mPFC-p slope difference. It is wide (−0.022 to +0.087 per day), which confirms the low power the verifier flagged; the notes now say so.
- **fig5e:** leaving out one mouse at a time, the distal valence effect holds in all six sets. The identity part fails when sub-2400 is left out.
- **discussion-differences-grow:** prints the OB-p minus mPFC-p difference itself by day. It grows in odor and delay and shrinks in the action phases.
- **tracked-neuron-counts:** counting tagged sessions over days 0–3 only gives 43 and 41→37, both within tolerance.
- **Data checks:** no analysis window runs past the end of a recording in any experiment.
  - Licks and rewards are timed from trial start.
  - In the 30 Hz files, odor onset falls 1–10 ms after a rising edge of the files' sniff signal, so latencies are sniff-aligned as the paper says.
- **fig2e:** the text now says the "correction over 2 tests" variant was my addition, not a reading the criterion names.
- **Other files:** the README table, the notebook summaries, a new methods finding for the authors, and `entry.yaml` (Go/NoGo runtime set to 16 min).

## Questions and what I did not do

- I added one reader question to `questions/daste-2025.yaml`: the discussion-differences-grow criterion never tests whether the gap between the groups grows (the verifier's point 8). I did not change the claim.
- The pre-onset concentration decoding by mPFC-p (37% against 33.3% chance) is still unexplained. The shuffled null confirms 33.3% is the right chance level for this procedure, and the notes say the offset is unexplained.
- After the run I fixed two sentences of conclusion text in the Go/NoGo notebook. I edited the executed copy's markdown to match, so it is not a fresh execution of that text.
