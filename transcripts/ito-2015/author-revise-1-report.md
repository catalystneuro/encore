The round-1 revision is finished. I re-ran the entry with `python tools/entry.py all entries/001642-ito-2015`: 0 check errors, and the notebook passed in 2058 s (about 34 minutes). Every conclusion, the summary, the README and the attempt record now match the new outputs. `tools/entry.py check` passes and the handover is rebuilt. Nothing is committed.

**Outcome changes** (now 11 reproduced, 9 not reproduced, 12 blocked). The main change: where a criterion names readings, the outcome now follows the claims file's rule that every reading must hold. The notebook no longer picks one adopted reading. Both unit sets count as readings: the dandiset's `PANs` flag and the set rebuilt from the Methods' rule.
- **Now blocked (methods_underspecified):** fig4b-dms-phase5, fig4b-vs-phase7, fig4c, fig5b, fig6-event-coding, fig6bc, fig8a-d, fig8e-action-value, fig8e-qr, fig9-dms-never-above-dls, fig10d.
- **Now not reproduced:**
  - fig5e-cue-offset: the Panzeri-Treves correction is now shown as a variant only, and under the claims file's two MI readings all 8 fail.
  - fig5g: part 1 now tests the first threshold crossing over the whole trial, as the criterion words it, and fails in every reading.
  - fig8f: fails in all 16 readings.
- **No longer flagged as resting on an assumption:** every outcome except fig2g, since no adopted reading is used any more.
- All of these now match the verifier's outcomes, except neuron-counts.

**Disagreement kept: neuron-counts stays not reproduced.** The verifier would block it for missing data. My reasons, recorded with its view under `verifications`:
- Every count the dataset allows to be computed misses at least one region, including the dataset's own PAN flag (VS 138 against 119 ± 11.9).
- Blocking it would, by protocol step 1.5, also block every neural claim that depends on it, even though those claims run on PAN sets the dataset provides.

**Outputs added at the verifier's request:**
- **File contents:** a printout of what the files hold. There are no waveforms, amplitudes or depths.
- **Regression:** the Fig. 8 regression is now also run on the Methods-rule unit set.
- **Particle filter:**
  - Three more seeds, plus a finer 5 × 5 grid of drift settings.
  - FQ variable stays below Markov 4 throughout (0.5757 to 0.5764 against 0.5785 and 0.5797).
- **Alternative shuffle threshold:** for the Fig. 5 action and reward information and for Fig. 9, the threshold is also built from labels shuffled within blocks. It shows alongside the paper's threshold and changes no outcome.

**Corrections:**
- fig10a now orders the block types by first crossing, as the criterion says.
- Fixed the wrong comment on the shifted reward labels (they are the previous trial's, not the next).
- The notebook now notes that 100 ms bins can straddle an event, and which phase such a bin counts to.
- The actor-critic conclusion now says the test has little power: the fits sit at the bounds where the model predicts 0.5.
- One side effect I caught and fixed: the new within-block shuffles first shared a random stream with the Fig. 9/10 shuffles, which shifted those numbers. They now have their own stream, so the earlier numbers are unchanged.

**Questions for a reader** (new file `questions/001642.yaml`; I changed no claim):
1. Fig. 4B: is "first crossing in the phase" a reading the paper allows?
2. Should the Panzeri-Treves correction be one of the readings for the mutual information?
3. fig9-dms-never-above-dls: should one uncorrected test out of eight decide a reading?
4. no-policy-coding: is 0.01 the right chance level for a joint event?

**Not done:** the verifier's synthetic actor-critic check is only cited in the notes, not added to the notebook. It only bears on how much the test can show, not on the outcome.
