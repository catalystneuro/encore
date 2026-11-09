No outcome changed and none is proposed. The verifier agreed with all 35 outcomes in round 2, and the new analyses I added do not support moving any of them. `python tools/entry.py all entries/000233-tingley-2021` finished with 0 errors, and the notebook ran in 6.5 min.

**Assumption flags.** The verifier noted that five claims use the same 5-min pairing as fig2 without saying so. I added both pairings one reading apart to all five:
- **fig2g-clustered-ripples, edfig4-ripple-features, edfig4-nrem-wake:** the result changes under one of the two other pairings, so each is now marked `assumed: true` with a deviation. The clearest case is edfig4-nrem-wake: counting SPW-Rs after each reading makes the awake and NREM blocks differ (p = 0.038).
- **fig2ef-correlation-beyond-shuffle and edfig4-no-hour-differs:** the outcome is the same under all three pairings, so I did not flag them, and the notes say why.

**supp-ripple-rate.** I did not flag it as assumed, though the verifier suggested it. The 5 s.d. threshold is the paper's own method (Methods, cited), and the notes already say the outcome depends on it.

**Statements corrected:**
- **edfig6 timing:** the notebook now times 16 pieces read in 4 and in 16 processes and prints the per-piece times. The text no longer quotes one run's numbers as another's. It explains the factor-of-ten gap by network variation: a single piece took about 1 to 22 s, and 106 s once.
- **edfig1-glucose-rhythm:** the claim that a 50-min oscillation is present now reads as a broad hump of excess power with no matching rhythm in the autocorrelogram.
- **supp-ripples-stable-across-days:** I added an exact Spearman p over all orderings of the days. With it, no rat with up to 8 days has a trend, and the two rate failures turn out to be artefacts of scipy's asymptotic p. The wrong sentence is replaced.
- **edfig9-dorsal-ventral:** CGM48 has 2.2 h of glucose with the electrophysiology, too little for a 4-h day. The notebook now prints these hours for the three dorsal and ventral rats.
- **edfig5 wording:** "above the diagonal" now reads "where the glucose period is longer than the SPW-R period".
- **README:** the run time now reads 6.5 to 8.4 min.
- **Summary and tables:** the notebook summary and the README table mark the three newly assumed outcomes.

Round 2 is recorded under `verifications` for all 35 claims, with the verifier's reasons and my responses.

**Not done:**
- **edfig6 test on the 3 rats with stored sleep states.** The verifier suggested a partial test there. Reading alone takes 26 to 28 min in 16 processes, and the seven predictors and 100 model splits at 41 offsets would come on top, for 3 of the paper's 8 rats. The protocol leaves a change that needs a new analysis to a new attempt, so the three claims stay blocked (`too_large`) and nothing is proposed.
- **No question added to `questions/000233.yaml`.** The verifier's note on the circadian claim says the pooled test was the reader's own choice, not a misreading of the paper.
- **Unexpected entries in the repo root.** Untracked entries such as `.bashrc` and `.idea` were already there when the run started, at 21:43, along with the earlier `tools/` changes. I left them alone.
