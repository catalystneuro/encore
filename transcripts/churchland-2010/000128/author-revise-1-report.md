No outcome changed. The verifier agreed with all 22 outcomes (11 reproduced, 1 partially reproduced, 3 not reproduced, 7 blocked). I re-ran the entry with `python tools/entry.py all entries/000128-churchland-2010`: it passed in 121 s and every earlier number came out the same. Round 1 is recorded under `verifications` in `attempts/000128-churchland-2010-01.yaml`, with the verifier's reason and my response for each claim. Nothing is committed.

**Corrected**
- **recordings-jarray table:** each row is now labelled with its reading. The 137 held-in units and the 1967 trials with delay over 400 ms are marked as not readings, since the first is a Neural Latents Benchmark split. Reading (a) now shows both 2869 trials (with the test file) and 2295 (train file alone). The conclusion and notes now say that the 182 units fail under every reading.
- **Conclusions and notes** now carry the verifier's caveats:
  - The correlation claims (fig4d, fig3, fig4-no-separate) rest on only 17 neurons, so their tests have little power, and fig3 rests on one neuron, unit 1581 (r = 0.765).
  - The preparatory separation in suppfig1 is positive by construction.
  - In the PD analyses (fig6-best, fig7b, fig7d) the best k sits at the top of the tested range, so it is not a true peak.

**Added outputs the verifier asked for**
- **fig4d:** a per-neuron table of unit id, id digit, preparatory and peri-movement tuning, r and Spearman r.
- **fig6-each-dimensionality:** the lost comparisons are printed. As the verifier inferred, it is the 2-D initial-velocity space, 0.238 against 0.223. The margins at k = 1 are 0.0024 to 0.0041.
- **Data check, test file:** it has its own clock, with ids and times restarting at 0, and no delay or success column. The train trial ids run without gaps, so the files do not record which trials the packaging dropped. I added this to the matching finding.
- **Data check, arrays:** the electrode-group descriptions name one array in M1 and one in PMd. No unit column other than the electrode reference ties a unit to an array, so the id digit still cannot be mapped and the two AP claims stay blocked.
- **prep-dimensionality:** variants on conditions × (neurons × times) matrices need 55 to 61 components. They do not decide the outcome.

**Not done, and why**
- **prep-dimensionality reading:** I did not change the claim. The main text says "at least 7-10 dimensions", while the claims file reads it as a range, and the supplement's "This T-matrix" is ambiguous. Both points are now a question in `questions/000128.yaml`. The claim stays not reproduced as the claims file states it; read as a lower bound, it would be met.
- **Which trials reading (a) covers:** I did not ask about this, because the outcome is partially reproduced however it is answered.
- **Supplement text:** I could not extract it here either, so the open T-matrix question rests only on the sentence quoted in the claims file.
