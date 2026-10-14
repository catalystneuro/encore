You are the author of a new attempt on dandiset {dandiset} in the reproduction registry, checked out in the current directory. Follow docs/protocol.md exactly; read it first. The dandiset already has an attempt, `{earlier}` (entry `entries/{entry}`, claims in `claims/{dandiset}/`), made on version {earlier_version}. Since then the dandiset has changed, and this attempt tests what it holds now.

Paper: doi:{paper}, "{title}". Save any text of the paper you download under `paper/` and read it from there. Stream the NWB files from the DANDI API; do not download them to disk.

{version_rule}

1. Keep the claims file as it is unless a claim is wrong about the paper; if you change one, say why in the file's opening comment.
2. Update the entry in place to stream the new version: the helper's version constant, `entry.yaml`'s `dandi:` relation, the notebook header and README. The earlier attempt record stays as it is.
3. Re-run every check of the data and every claim. For each finding of `{earlier}`, say in the notebook's data check and in the new record whether it is fixed, partly fixed or still present, with the output that shows it. Record new findings too.
4. Lock, check and run the entry, make every conclusion match the new numbers, and write the new record `attempts/{next_attempt}.yaml`. Its outcomes are this attempt's own; where one differs from `{earlier}`, say why in its notes. Then run `python tools/entry.py handover entries/{entry}`. Do not verify your own work, and do not commit or push: the workflow commits your changes.

Provenance: kind agent; accountable name "CatalystNeuro"; harness "Claude Code (GitHub Actions)"; model "{model}"; protocol: the version stated in docs/protocol.md. Date {date}.

Write prose plainly: no em dashes, never the word "rather", no bold except the "**Result: ...**" openers. YAML plain scalars must not contain ": ".

Your final message is a report with: (1) the outcome per claim, with the earlier outcome next to it; (2) for each earlier finding, whether it is fixed; (3) new findings; (4) anything in the protocol that did not fit a repeat attempt.

Run every command in the foreground and wait for it to finish, however long it takes: the run ends when you stop, and anything still running is lost.
