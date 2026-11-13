I've worked through every point in the round-1 report and re-run the entry; `python tools/entry.py all entries/brudner-2026` passes with 0 check errors. It ran in 19 minutes, and a second run gave identical numbers. Nothing is committed.

**Outcomes changed**
- **fig5e-cue-betas: reproduced → not_reproduced** (still resting on an assumption), agreeing with the verifier. I now take the smoke-1a files as the paper's complex plume. The dandiset's description says smoke_1a_orig "was analyzed throughout the paper", and only the smoke-1a session descriptions name that movie. With the claims file's turn onset (the SI's 20% rule), no reading passes (0 of 24). With the code's smoke-2a files, per-trajectory z-scoring fails, so not every reading passes there either.
- **fig5f-cue-dominance: reproduced → partially_reproduced** (resting on an assumption). This disagrees with the verifier, and the disagreement is recorded. With smoke-1a and the SI onset the signs hold, but the two values are never both within tolerance (0.937 and -0.492). Both readings the verifier cited still give both values within tolerance, and they are reported.
- The other 20 outcomes are unchanged, and the verifier agreed with each of them.

**What I added or corrected**
- **Onset rule (problem 2):** it now follows rotation in the turn's own direction. The old rule ran into a turn the other way in only 0.2% of turns, and the results barely moved.
- **Which complex files (problem 1):**
  - I fitted the models separately for flipped and unflipped projections. Each file set keeps its sign in both, so the two sets don't differ by a flip convention.
  - I compared every reading with the code's published Fig. 5 tables, read from the pinned commit and listed under `inputs`. Only smoke-1a with the files' own turn start and the 160 to 200 degree window matches them: within 0.1 SE on the coefficients and 0.001 per turn on the log-likelihoods. The code's own stated choice (smoke-2a, 150 to 210 degrees) is 3.5 SE away. I recorded this as a code_mismatch finding.
- **Question for a reader:** in `questions/brudner-2026.yaml` I asked whether the dataset's turn start should count as the SI's onset. If a reader agrees, the fig5e and fig5f outcomes could change.
- **figs1fg (problem 4, item 9):** I added smoothing of the frames for every map, plus a centered-difference motion cue. Motion still fails under all six readings; the gradient part passes only with smoothing.
- **fig2 (problems 3, 7, 8):** I added mirror sampling split by location, so no test window is also a training window; the AUCs are the same. I added row 571 as an alternative centerline. Outcomes unchanged, with the mirror-sampling assumption and the not_reproduced result under the claims file's own samplings both recorded.
- **figs1 antisymmetry and temporal statistics (problem 5):**
  - I tested the parts that don't need the smooth plume, using the deposited freestream maps and points and the complex movie.
  - Both hold: the index rises with wind speed and the complex plume is highest, and the complex plume has the highest encounter frequency.
  - Both claims stay blocked, because they also need the smooth plume.
- **methods-intensity-right-bias (problem 6):** the claim holds under every reading if -1 is a right turn, and fails under every reading if +1 is. It stays blocked.
- The round is recorded under `verifications`. I also updated the notes, deviations, findings, notebook conclusions, summary, README, helper docstrings and runtime.

**Not done**
- **Smooth plume:** still not read. Dryad needs a token.
- **Complex-only network and agent parts:** not attempted. They would need training a network and an agent simulation the paper's code doesn't contain.
- **Item 10** (heading read at onset minus 50 ms, position at the event start): left as is, since that is what the code does. The deviation now says so.
- **Item 7** (background-subtracted movie): this preprocessing can't be undone; I noted it.
