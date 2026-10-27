You reconcile a repeat attempt in the reproduction registry, checked out in the current directory. Read docs/protocol.md, "Repeat attempts", first. Attempt `{attempt}` on dataset {dataset} (entry `entries/{entry}`, dataset version {version}) was made blind: its author did not see `{earlier}` (made on version {earlier_version}). Its record is `attempts/{earlier}.yaml`. Its entry is `entries/{earlier_entry}` as it was when that record was last changed: `c=$(git log -1 --format=%H -- attempts/{earlier}.yaml)`, then `git show $c:entries/{earlier_entry}/<file>`. Both have been through their verification rounds. Your job is to say how the two compare, in a `reconciliation` block of `attempts/{attempt}.yaml` (its schema is in `schemas/attempt.schema.json`). Do not change the outcomes, statements or notes that the blind attempt recorded, its claims file or its notebooks.

1. Run `tools/blind.sh audit {folder}`. It prints the lines of this attempt's author transcripts that point at an earlier attempt. Read each in context. Set `blind: true` if the author never saw an earlier attempt's results, else `blind: false` with what it saw under `blind_note`.
2. For each finding of `{earlier}`, in order (`finding` is its number, from 1), decide whether one of `{attempt}`'s findings reports the same problem: the same files, fields or values, not only the same kind. If so, set `status` to `still_present` or `partly_fixed`, and `now` to that finding's number in `{attempt}`. If not, check the earlier finding directly on version {version}, in a new notebook `entries/{entry}/earlier_findings.ipynb` (add it to `entry.yaml`, one short section per finding, each opening with the earlier statement, and lock, check and run the entry). Then:
   - `fixed`, when the check shows the problem is gone;
   - `still_present`, when it is still there: add it to `{attempt}`'s findings with `found: on_prompt` and a statement in the protocol's usual style, and point `now` at it;
   - `not_checked`, when it cannot be checked on this version, with why.
   Give every one a `note` of one or two sentences with the evidence. A finding of `{attempt}` that no earlier finding points at is new; it needs nothing.
3. Leave `found` unset on the blind attempt's own findings (it means `blind`), and add `found: blind` nowhere.
4. For each claim tested by both attempts (the same `claim` id) whose outcome differs, add an item under `outcomes`, with the earlier outcome and a `note` on the likeliest reason: a change in the dataset, in the protocol, in the claims file, or a difference in method between the two notebooks (name it). Do not change either outcome.
5. {protocol_note}
6. Set `earlier: {earlier}` and `date` in the block, and check the record with `python tools/entry.py check entries/{entry}`. Do not commit or push: the workflow commits your changes.

Write prose plainly: no em dashes, never the word "rather", no bold. YAML plain scalars must not contain ": " (colon space). Keep every number as the records and notebooks give it.

Your final message is a report with: (1) whether the author was blind; (2) a table of the earlier findings with their status; (3) the new findings, as numbers; (4) the outcomes that changed and why; (5) anything in the protocol that did not fit.

Run every command in the foreground and wait for it to finish: the run ends when you stop, and anything still running is lost.
