Round-1 revision is done. The full entry run (`python tools/entry.py all`) passed: the main notebook took 10.5 min, the decoding notebook 24.5 min and the new variants notebook 31 min, and `check` reports 0 errors. Nothing is committed.

**Outcome change**
- **ext3c-decoder-orthogonality**: changed from `not_reproduced` to `partially_reproduced`, as the verifier proposed. It holds for the Ring and for the Receptive Field data in both datasets. It fails only for the Triangle neural data (median 106.6° in both phases, outside 75 to 105°). The criterion's "not reproduced" case, neither reading holding, does not fit a result that holds in one dataset and not the other.

All other outcomes are unchanged, and the verifier agreed with them.

**What I checked or added, by problem**
- **Problems 1–3, fidelity to the paper's code.** I cloned the code at the cited commit and checked each point:
  - `dataset.py` has its per-unit normalisation commented out, so the decoders get rates in Hz.
  - `get_simultaneous` is the same greedy rule as ours.
  - `models.py` puts a sigmoid on the Ring decoders too, though the Ring targets run from -0.7 to 0.7, so it cannot reach the negative half. I recorded this as a new `code_mismatch` finding.

  The analysis keeps the code's method. The variants are in a new notebook, `decoding_variants_watters_2026.ipynb`, kept separate so each notebook stays under the 60-minute limit:
  - **z-scored inputs:** identity decoding is still above control in only 1 of 3 sessions, so ext3ab does not change. Input scale does not explain the identity result.
  - **Ring decoders without the sigmoid:** the Ring neural angles rise to about 140°.
  - These variants move the ext3c angles by up to 51°, and the notes now say the result depends on the decoder's details.
- **Outputs the verifier asked for**, now in the decoding notebook:
  - units and trials after each of the code's filters (Triangle 2022-06-04 keeps 20 of 116 units)
  - decoder training accuracy
  - median angle per session
  - the Triangle result without 2022-06-04
- **Problem 4.** The code itself uses ordered pairs. I added intervals that count each pair once, for fig2d (code variant) and fig5e. No conclusion changes: Monkey E's lowest fig2d bin is 124 rows from 98 pairs.
- **Problem 6.** The cost cell now cites the model configs and prints that this machine has no GPU. Even at 100 times the speed the fits would take 3.5 to 62.9 h. The re-run timed one step at 0.98 s, so I updated all 13 blocked claims' estimates (now 15 to 262 days).
- **Problem 7.** Added `questions/000620.yaml` with one question for a reader. The ext3ab criterion requires identity decoding above control, but the Methods say identity "was poorly decodable on single trials". The claim is unchanged.
- **Record.** Round 1 is recorded under `verifications` (26 claims, the verifier's reasons with my responses). The README also now carries the required "failure to reproduce" sentence, which it lacked.

**Things to know**
- **ext3ab numbers moved.** The decoding code is unchanged, but some numbers differ slightly from round 1 (2022-05-31 shuffled identity is 30.5% where it was 32.4%). Identity decoding now passes in one session under each reading, where round 1 had none; the outcome stays `partially_reproduced`. I think the cause is floating-point differences between machines over the 10,000 training steps, but I have not confirmed it. On this machine two runs gave identical numbers.
- **Executed copies.** After the full run I edited two markdown cells in the main notebook (the cost conclusion and a header sentence). I copied those edits into the executed copies by hand instead of re-running for 66 minutes; no code cell changed.

**Not done**
- No reduced model fit was tried, since a partial fit tests no claim.
- No questions were filed about the verifier's other claims-file remarks (the 0.6 / 0.7 decile cut-offs and T2 leaving the radius open). Neither is a misreading of the paper.
