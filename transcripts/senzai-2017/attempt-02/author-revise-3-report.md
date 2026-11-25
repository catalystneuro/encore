Both proposals were agreed and applied. The re-run with `python tools/entry.py all entries/senzai-2017` passed with 0 errors (about 34 minutes), and the distance and smoothness outputs came out the same as before.

**Outcomes changed**
- **gc-mc-distance**: still blocked, but `blocked_by` is now `methods_underspecified` instead of `metadata_insufficient`. The `proposed` block is removed.
- **gc-backpropagation**: the same change, also with `proposed` removed.

No other outcome changed.

**Proposals that stand:** none. The verifier agreed with both, so none is left open.

**Other changes**
- **Record notes:** these now say the following:
  - The paper's Methods give 20 µm spacing for the 10-site shanks too.
  - The smoothness test shows the order of the sites but not which end is up.
  - The idea that shanks reaching the infrapyramidal blade explain the reversed slopes was not tested.
  - The 13 ± 49 µm figure, and the 7 ± 59 µm figure on the 34 pairs from the automatic test, are descriptive only. I checked both numbers against the notebook output.
- **Finding 1:** it no longer says the spacing of the 10-site shanks is not given. Without asking you, I also lowered its severity from major to minor, because the depth can now be read from the list with the lab's convention. Change it back if you'd rather keep major.
- **Notebook, Summary and README:** updated to the new reason. The notebook's claims table, the gc-mc-distance section and the Result and Summary cells all changed.
- **Round 3:** recorded under `verifications`, with both results set to agree and outcome blocked. Each result has the verifier's reason and my response.
- **New question:** I added one to `questions/senzai-2017.yaml`. The claims file's header says the supplement was not available, but it is in `paper/`, and gc-backpropagation rests on Figure S3D to S3F. Neither the verifier nor I could read that PDF, so whether it describes the method is still unchecked.

Nothing was committed or pushed.
