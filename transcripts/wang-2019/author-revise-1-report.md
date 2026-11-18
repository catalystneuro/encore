I made the round-1 revision for wang-2019-01. One outcome changed. The entry check and fresh run pass (0 errors, notebook 13 s). Nothing is committed.

**Outcome changes**
- **fig3abc-tyramine-na-mimic-sns**: changed from partially_reproduced to reproduced. The claims file counts a claim reproduced when it holds under any reading, and noradrenaline meets the pattern under monotonic reading (b). The first version had used its own judgement about the noradrenaline heart-rate fall instead of that rule. The notes still record the fall (−26.75 bpm after 30 s) and that reading (b) has little power with 3 or 4 hearts.
- **fig2a-rabbit-monotonic**: kept as partially_reproduced; the verifier would give not_reproduced, and that disagreement is recorded. The criterion has no rule for a partial result. The protocol calls a claim partial when it holds only in part. Here all three variables change significantly from time 0 under every test reading, and APD80 is monotonic, but heart rate and CaTD80 are not.
- **fig8e, fig8f, fig8ij, fig9**: kept blocked as not_runnable, recorded as a disagreement with the verifier. The notebook now lists the model code in `files/code`, prints both instruction files, and checks for MATLAB and Octave; neither is present. Octave can't be installed without root on this runner, and the entry's environment is built from a Python lock file that can't include it.

**Added or corrected**
- **Post hoc test (point 6)**: the helper now also runs SigmaPlot-style Holm-Sidak comparisons on the ANOVA's pooled error, as a variant. For fig3d this answers the fragility the verifier raised (point 2): heart rate now differs from time 0 at 30 to 60 s (p = 0.0048 at 60 s) and APD80 at 25 s (p = 0.036). So not_reproduced no longer rests on one unadjusted test. The notebook also prints the 0.75 chance of at least one false positive among 27 tests. For fig2a, APD80 at 60 s now holds under this variant (p = 6e-5). fig2d is unchanged under it.
- **fig3f pairing (point 3)**:
  - The notebook prints the raw table with all 10 columns.
  - SNS is longer than no-SNS at time 0 in every pair, by 1.65 to 4.84 ms.
  - Pairing by column position is the 4th closest of the 120 possible pairings.
  - Measured as change from time 0, SNS and no-SNS do not differ at any time (p 0.18 to 0.94).

  The outcome stays reproduced and marked as resting on the pairing assumption, with these numbers in the notes.
- **Outputs the verifier asked for**: the whole Fig1 sheet (it says nothing about which part of the 20 s the SNS value is), the raw tyramine, noradrenaline, propranolol and Fig. 3E tables with column B, and a listing of the archive's `revisions/1` folder (a banner, a manifest and the readme, no data).
- **Notes and conclusions**: updated for points 4, 7, 8 and 10 (the substitute hearts behind fig1bc and fig1ef, the 5 s value copied from 0 s in Fig. 3E, the borderline p = 0.048 for fig4g, and weak evidence for "similar" in fig2cf). The README, summary table and the finding about which statistical test the paper used are updated to match the new numbers.
- **Question for a reader**: `questions/wang-2019.yaml` asks whether the four simulation claims should count as dataset claims, since the model code is in the dataset. The claim itself is not changed.
- **Round-1 record**: written under `verifications` in `attempts/wang-2019-01.yaml`, with the verifier's reasons and my responses.

**Not done**
- I did not run the models. That would need Octave, or a Python port, which would be a new implementation and not the paper's method.
- I did not change the fig3d criterion; it belongs to the claims file. I didn't raise it as a question either, because the verifier called the rule fragile, not a misreading of the paper.
- Untracked files such as `.bashrc` and `scripts` show in `git status`. They are sandbox placeholders, not mine, and I left them alone.
