I worked through the round-2 report and re-ran the entry with `python tools/entry.py all entries/daste-2025`. Both notebooks pass (passive 1390 s, Go/NoGo 621 s), the numbers are the same as the verifier reviewed, and `check` reports 0 errors. Nothing is committed.

## Outcomes
No outcome changed. The verifier disagreed with two, and I agree with it on both. Each keeps its verified outcome, with a change to blocked (`methods_underspecified`) written under `proposed` for a third round:
- **fig4ij-valence-correct-trials** (stays reproduced, assumed). Neither correct-trial table looks like the one the paper used:
  - The matched table's shuffled level is 65 to 69%, where the paper's chance is 50%.
  - The balanced table has only 3 trials per CS, too few for the identity decoding on correct trials that the Methods describe.
  - On the balanced table, mPFC-p odor accuracy is 27.8% and 31.4% against a shuffled mean of about 51% (Mann-Whitney p = 3e-14 and 1.4e-11). The decoder predicts systematically below chance, so this does not show mPFC-p at chance. The notebook now prints this comparison.
- **fig2b-lifetime-sparseness-similar** (stays not reproduced, assumed). The criterion's n counts every neuron, and the two readings that keep every neuron disagree: setting never-active neurons to 0 reproduces the claim, setting them to 1 does not. The notebook now prints whether the claim's condition holds under each reading.

## Added or corrected
- **fig2f-latency and fig2g-early-peaks: projection is confounded with mouse.** This was the verifier's new point.
  - A new output compares each mouse's projection neurons with its own untagged neurons. OB-p is not faster than untagged in any OB mouse, and slower in two of them.
  - mPFC-p is as slow as its own mouse's untagged neurons, or slower.
  - The conclusions and notes now say this. The outcomes stand because the criteria pool neurons.
- **Sentences the outputs did not support**, corrected in the notebooks, record or README:
  - Clock-check text and fig4def notes: the traces already rise before onset, the accuracy ranges of the two slow mice overlap with sub-2400 day 1, and no per-session shuffled null was run.
  - fig4def: mPFC-p odor accuracy is now compared with the shuffled 95th percentile, not only the shuffled mean.
  - fig5e leave-one-out: the identity part holds in 5 of 6 sets under the mean aggregate and 4 of 6 under the maximum. I did not edit the round-1 response, which is wrong on this; the round-2 response says so.
  - fig3bc notes: only the concentration and interaction fractions are near 5%, not identity.
  - fig2j notes: removed the development-run number that had no printed output behind it.
  - dataset-neuron-counts: the Go/NoGo untagged mean, 1623.3, is now stated as outside 1690 ± 35.
  - Passive Summary: replaced the "within 2%" sentence with the actual differences (2.1% and 4.5%).
  - README: the counts rows now match the record.
- **Round-1 reason for fig4def**: now gives the verifier's own figure, "(59 of 93)".
- **Findings**: the two questions for the paper's authors now include the Figure 2B disagreement and the below-chance result.
- **Round 2** is recorded under `verifications` for all 36 claims.

## Not done
- No per-session shuffled null for the Go/NoGo clock check. The text now says the pooled-table nulls are only a rough reference.
- No new questions for a reader: the verifier found no new place where the claims file misreads the paper.
- The verifier still could not check the plot images. I added nothing for that.

Untracked dotfiles and `.idea`, `.vscode` and `scripts` directories are at the repo root. I did not create them and did not touch them.
