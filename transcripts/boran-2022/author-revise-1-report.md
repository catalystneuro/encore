I made every change the round-1 report asked for or explained why not, and re-ran the entry. `python tools/entry.py all` passed with 0 errors, the notebook ran in 15.5 min, and the conclusions match the new numbers. Nothing is committed or pushed.

**What changed in the outcomes**

Two outcomes went from partially reproduced to reproduced. Both are marked `assumed: true`.

- **neurons-recorded:** The verifier pointed out that I had placed all 133 units whose tip contact has no MTL label in hippocampus, and never tried anything else. I now print a table of those units by session and bundle, with the atlas labels of contacts 1 to 4.
  - No natural group of 41 exists. But the 28 units on PHR of participant 8 have contacts 2 and 3 labelled PhG.
  - New rule (a2): give each of those units the label of the contact nearest the tip that has an MTL label, and use the electrode name only where no contact has one. This gives 467, 196 and 146 neurons (paper: 454, 209, 146), all within tolerance.
  - I adopted a2 as the rule that keeps reading (a) anatomical. The record says plainly that I chose it after seeing the counts, so round 2 should weigh that.
  - The old rule (a1) and the electrode-name reading (b) are still shown. Every per-region claim is now given under a2, a1 and b.
- **fig2c-maintenance-neurons:** I added the check at 5000 permutations that the claims file promises. The paired counts are 58, 21 and 15 under a2 and 59, 20 and 15 under a1, all within tolerance of 55, 21 and 16.
  - At 1000 permutations the counts depend on the random draw. Ten draws give hippocampus 55 to 59, entorhinal 20 to 22 and amygdala 14 to 16; the draw used for the significance test gave 61, just outside.
  - The outcome takes the 5000-permutation counts.

The other 15 outcomes are unchanged, and the verifier agreed with all of my round-1 outcomes.

**What I added or corrected**

- **Spike and label alignment:** I added a per-session scan against 200 shuffled orders of the set-size labels.
  - No session carries set-size information with the spikes paired to their own trial's label (k = 0).
  - Pooled over the 7 sessions with all 192 trials, the information peaks when spikes are paired with the label three trials later (corrected p = 0.005). The 9 sessions with fewer trials show no peak at any shift.
  - The trial table holds no trial numbering from the source.
  - The finding and the notes on the decoding claims now say those failures may come from the deposited data.
- **behavior-rt-set-size:** I added the verifier's variant as an extra output. Fitting median RT on the condition step (1 to 4) gives 118.1 ms, the paper's number. It is now a question for a reader in `questions/000575.yaml`, and the claim stays partially reproduced on the readings the claims file names.
- **Other outputs the verifier asked for:**
  - fig4a: dPCs 2 to 4 are time components in all 99 shuffled fits.
  - Decoding: the training-set sizes are printed (114 per split under reading c, 190 under d, against the paper's 145 to 169).
  - The regional k = 3 variant now uses 100 scrambled runs, so its smallest possible p is below .0125.
- **Wording:**
  - fig4c and decode-performance-not-significant now say their outcomes carry little weight.
  - Where a criterion has no partial clause, the notes say partial is my judgment.
  - The `welch_t` docstring no longer claims to match statcond. For equal group sizes the two t statistics are the same.
- **Record and docs:**
  - The README, the notebook header and summary, and `entry.yaml` (runtime) are updated.
  - Round 1 is recorded under `verifications` with the verifier's reasons and my responses.

**What I did not do**

- I left the repetition counts below the paper's 500 and 1000 runs (decoding, the cluster reading, fig3b reading (b), fig4b reading (b)). Raising them would roughly double the run time, and none of those results is near a threshold.
- I did not add a decoding reading that uses each session's whole unbalanced set of correct trials. The claims file does not name one, and accuracy is below chance under both readings it does name.
