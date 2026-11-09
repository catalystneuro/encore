I fixed every number the verifier flagged and re-ran the entry twice. Both runs passed: the main notebook in 8 min, decoding in 13 min, variants in 16 min, and `check` reports 0 errors. Nothing is committed.

**Outcomes:** none changed. All 26 stay as round 2 verified them: 7 reproduced, 5 partially reproduced, 1 blocked as `methods_underspecified`, 13 blocked as `too_large`. Nothing is under `proposed`.

**Corrected or added:**
- **Prose against outputs.** Re-running gave decoding outputs identical to the ones the verifier read, so the old prose came from a development run, not from machine drift. I rewrote the affected text from the saved outputs:
  - in the notebooks: decoding cells 9 and 12, variants cells 9 and 12, and the variants Summary;
  - in the record: the ext3ab and ext3c notes, their round-1 responses, and the sigmoid `code_mismatch` finding.
  
  The main correction: with the code's inputs, identity decoding is above control in 0 of 3 sessions, not 1 of 3. The ext3ab question in `questions/000620.yaml` now gives the right numbers too.
- **ext3c marked `assumed: true`.** A new deviation sets the Methods' "linear decoder" against the sigmoid in the paper's code (`models.py`) and says the outcome rests on that choice. With a linear output the Ring neural data fail both readings. The Triangle decoders were never run with a linear output, so I say only that the neural data would then fail in both datasets.
- **Cost cell.** Step timing varies with the machine and its load: 0.98, 0.84 and 0.45 s in earlier runs, 0.436 s in the final one. So the cell now prints the conclusion itself: every estimate is over the run's five hours at this speed, and over the 60-minute limit even at 100× (smallest 1.5 h).
  - Cell 45 and the 13 too_large notes now carry the final run's numbers: 1.2 h per fit, 6 to 116 days, 1.5 to 27.9 h at 100×.
  - The nslots note now says that at 100× that sweep alone would fit in five hours but not in the notebook limit.
  - The Summary no longer quotes an exact timing.
- **Label sentence.** The fig2b, fig5cd, fig5e and ext3ab notes and result cells now say that the criterion defines only the reproduced case, and that "partially reproduced" is this attempt's label.
- **Claims-file reading.** I added an ext3c question to `questions/000620.yaml`: does the claim require the neural decoders to be near orthogonal, or only the Receptive Field ones? I also added a `paper_inconsistency` finding: the Methods call the panel Extended Data Fig. 3b, the legend calls it 3c. The claim is unchanged.
- **Round 2 recorded** under `verifications`: all 26 claims agreed, with the verifier's reasons and my responses. I left its round-1 reasons as they were.

**Not done:**
- I changed markdown only after the final run, applied identically to the source and the executed copies. I did not run the entry a third time, because the timing would move again.
- The verifier still cannot check that `wm.py` matches the paper's code on four points: the greedy filter, the Ring sigmoid, the commented-out normalisation and the ordered pairs. This attempt has no way to give it that code, so those points still rest on my word.

**Note:** the working tree has untracked dotfiles and folders I did not create (`.bashrc`, `.idea`, `scripts` and others). I left them alone.
