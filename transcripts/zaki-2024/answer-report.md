There was one question, about **offline-bursts-above-shuffle**, and I changed the claims file to answer it.

The attempt asked whether each shuffled surrogate trace is z-scored again before the z = 2 burst threshold is applied. The paper does not say. The Methods z-score the true population trace and call frames above z = 2 bursts. The Extended Data Fig. 3l legend says only that "the mean population activity was re-computed each time" and that "The burst frequency was computed for each of these shuffles". The analysis code is not public, so nothing else decides it.

The old criterion said the surrogate was "z-scored as for the data", which is a choice the paper does not make, and the attempt reports that the two readings give opposite outcomes. So the criterion now lists both readings, as reader step 3 requires:
- **(a)** each surrogate trace is z-scored again and thresholded at z = 2;
- **(b)** each surrogate trace is thresholded at the level that defines a burst in the true trace (its mean plus 2 SD).

The claim counts as reproduced under either reading, and the outcome is marked as resting on the reading that gives it. The answer also notes that the skew claim (offline-skew-above-shuffle) is not affected, because skewness does not depend on the scale of the trace. The question is marked `answered: 2026-11-25`.

`python tools/claims_check.py` reports 0 problems across 26 claims and both YAML files parse. Only `claims/zaki-2024.yaml` and `questions/zaki-2024.yaml` were modified, and nothing was committed. Some untracked files I did not create (`.bashrc`, `.idea`, `scripts` and others) are in the working tree; I left them alone.
