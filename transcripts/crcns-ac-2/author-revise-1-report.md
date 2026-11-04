I've dealt with every point in the round-1 report, and the entry re-runs cleanly: `entry.py all` reports 0 errors and the notebook passes in 82 s. The record now has 14 claims reproduced, 7 partially reproduced and 2 not reproduced, with 13 outcomes marked assumed. Nothing is committed.

**Outcome changes**
- **mepsp-size:** blocked → partially reproduced (assumed), which is the outcome the verifier gave. The verifier's detector concerns were right. The traces are recorded in 0.049 mV steps, so the noise estimate collapsed, and the smoothing zero-padded the sweep edges. I fixed both and added a false-positive check: each detector is also run on the sign-inverted trace. Template matching finds 55 to 80% as many events there as on the real trace, so its events are mostly noise. The derivative detector is the main reading, with each recording's threshold set where the inverted trace gives at most 10% as many events. It gives a mean size of 0.602 mV, outside 0.39 ± 0.08, and a CV of 0.354, inside 0.36 ± 0.03. No reading that bounds false positives gets both values.
- **anesthesia-comparison:** partially reproduced → reproduced (assumed). The paper's Figure 6 legend says LFP-based culling is repeated after PSP-based culling, so I made that order the main reading in place of my earlier intersection of the two cullings. That moves the pentobarbital private value from 0.98 to 1.01 mV, and every value now holds. The margins are 0.01 and 0.03 mV, and several readings would make it partial again; the notes say so.
- **"Assumed" flags:** now set wherever any reading of an open detail would change the outcome. Added on psp-culling, fig7b, fig7d, cv-large-responses and overfitting-correction-example; removed from fig4c, where every reading now gives the same outcome.

**Added or corrected**
- **Spike rule:** the claims file's rule was wrong in my earlier variant. It is now run as written: a fast rise (above 10 mV/ms) to above −20 mV after the 12 mV junction correction. A new per-neuron table and example traces show what each rule removes. The data set's per-neuron threshold also removes slow regenerative events (31 trials in 102800md02 with rises of 1.5 to 2.9 mV/ms) and spikes that peak just below −20 mV. I kept the per-neuron threshold as the main reading, as an assumption. The claims file's rule gives a total variability of 5.35 mV against 4.58.
- **Culling order:** sequential culling is now the main reading, with the intersection shown beside it. The best private estimate is 1.48 mV, largest reduction 84.6%.
- **Outputs the verifier asked for:**
  - the culling-window reading and response onsets for fig2;
  - the per-tone table behind fig7a's 80% outlier;
  - the tones the random control drops per neuron, and the control run without re-applying the 10-trial rule;
  - for fig8, a window that avoids the 15-ms baseline and a run without trials that spike in the window (the correlations stay negative);
  - every reading for anesthesia, CV and private-shared;
  - TTX sampling rates, noise, event-triggered averages, histograms, stimulus-locking and sweep-mapping checks.
- **Overfitting per-tone variant:** removed. It equals the per-neuron correction by algebra, which the notebook now prints.
- **Question for a reader:** `questions/crcns-ac-2.yaml` now asks whether the paper's random-culling control re-applies the 10-trial tone rule (3.82 mV with it, 4.83 without, against the paper's 4.5). The claim is unchanged and still tested as the claims file has it.
- **New finding:** the documentation doesn't say which sweep file is trial k in the TTX recordings, and its own Matlab code lists them in name order. Three earlier findings were updated.
- **Record:** the round-1 verification is recorded with all 23 claims. The verifier agrees on 22 and disagrees on mepsp-size. The README, header and summary tables match the new numbers.

**Not done**
- I didn't render the PDF figure panels, the one item the verifier couldn't check by eye. The 9.2-kHz Figure 4 example isn't found in the data in any case.
- The untracked dotfiles in the repo root were already there before this run; I left them alone.
