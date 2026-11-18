I answered the one question on DANDI:000785.

**`fig5c-cv-higher-obp`: the claims file changed.** The criterion now uses only reading (b), odor by phase with 16 levels. Reading (a), valence by phase with 8 levels, is kept as a variant only and no longer decides the claim.
- The paper words the two ANOVAs differently. The slope test is "within combinations of odor valence and task phase", while the CV test is "within combinations of odors and task phases", with an effect of "odor–phase combination".
- Figure S10F compares CV "across different odors and phases", the Figure 5C legend ranks CV per "stimulus", and the task has 4 odors (2 CS+, 2 CS−).
- The other open detail stays as it was: whether CV is SD over the absolute mean or SD over the mean. The claim is still judged under both of those, so it can still be blocked if they disagree.

The answer and `answered: 2026-11-05` are in `questions/000785.yaml`, and both YAML files parse. `tools/claims_check.py` found all 36 quotes word for word. It reported two numbers it could not find in the text, both in other claims (0.00039 in `fig2e-reliability` and 2.5e-06 in `fig5f-stability`); I did not check those. Nothing is committed.
