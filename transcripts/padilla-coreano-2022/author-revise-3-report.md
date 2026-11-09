The verifier agreed with the one proposal, so **ed5k-hmmglm-generalizes-across-rank** changes from not reproduced to **reproduced**. It is still marked as resting on an assumption, as the verifier asked, and its `proposed` block is removed. No proposals are left standing, and no other outcome changed.

The outcome rests on reading "4 standard deviations from the mean" as threshold crossings in either direction. On that reading all four train and test combinations give 9 of 9 labels above chance (sign test p = 0.0039), with and without the shift. With negative crossings only, training on subordinates and testing on dominants gives 7 of 9 (p = 0.18), so that reading fails one combination.

What I changed:
- **Attempt record:**
  - The ed5k notes now lead with the either-direction result.
  - The deviations say the reading was chosen after the result was seen, and that the paper's own counts support it without settling it.
  - A new deviation says ed5k uses either-direction crossings while fig1i and ed5j keep negative crossings; those two get the same outcome under both readings.
  - Round 3 is recorded under `verifications`: agrees, reproduced, the verifier's reason in its words, and my response.
  - The finding asking the authors which threshold direction they used stays.
- **Notebook:** the ed5k conclusion (cell 61) and the Summary table row are rewritten to match.
- **Entry README:** the ed5k row is rewritten to match.

The full run (`python tools/entry.py all`) passed with 0 errors in about 50 minutes. The executed ed5k cell prints the numbers the text quotes (for example medians 0.821 and 0.788, lowest AUCs 0.780 and 0.582). The sentence about a failure to reproduce stays, because ed5d and ed5j are still not reproduced.

Nothing is committed. The changes already in `tools/build_site.py` and `tools/site_assets/app.css`, and the untracked files in the repository root, are not mine and I left them alone.
