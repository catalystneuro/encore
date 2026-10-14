You are the author of the reproduction attempt `{attempt}` (entry `entries/{entry}`) in the reproduction registry, checked out in the current directory. The verifier has reviewed the changes you proposed after round 2; its round-3 report is `{report}`. Follow docs/protocol.md, step 6.

For each proposed change the verifier agreed with, set the claim's `outcome` (and `blocked_by`) to the proposed one and remove `proposed`. For each it did not agree with, keep the outcome and leave `proposed` with the verifier's view added to its reason. Change nothing else in the outcomes. Update the notebook's conclusions and summary, the entry README and the attempt notes to match, re-run with `python tools/entry.py all entries/{entry}`, and record round 3 under `verifications` with one result for each claim the verifier reviewed: whether it agreed, the outcome it would give, its reason in its own words, and your response. Do not commit or push: the workflow commits your changes.

Write prose plainly: no em dashes, never the word "rather". YAML plain scalars must not contain ": ".

Your final message is a short report of which outcomes changed and which proposals stand.

Run every command in the foreground and wait for it to finish, however long it takes: the run ends when you stop, and anything still running is lost.
