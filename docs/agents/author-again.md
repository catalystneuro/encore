You are the author of a new attempt on dataset {dataset} in the reproduction registry, checked out in the current directory. Follow docs/protocol.md exactly; read it first. The dataset already has an attempt, `{earlier}` (entry `entries/{entry}`, claims in `claims/{folder}/`), made on version {earlier_version} under protocol {earlier_protocol}. {why}

Paper: doi:{paper}, "{title}". The paper's full text is under `paper/`: read it to understand the claims. The claims file, which a reader wrote from the paper and a second reader checked, decides what is tested and how: do not change a claim's statement, expected values or criterion. Take a method detail it lacks from the paper, citing the passage, as step 1.6 of the Author section says; ask a reader only when you believe the claims file misreads the paper. {access}

{version_rule}

1. Keep the claims file as it is: only a reader changes a claim. If a claim misreads the paper or does not follow the current protocol, ask a reader, as step 1.6 of the Author section says.
2. Update the entry in place: if the version changed, the helper's version constant, `entry.yaml`'s relation to the dataset (`dandi:<id>/<version>` on DANDI), the notebook header and README. The earlier attempt record stays as it is.
3. Re-run every check of the data and every claim. For each finding of `{earlier}`, say in the notebook's data check and in the new record whether it is fixed, partly fixed or still present, with the output that shows it. Record new findings too.
4. Lock, check and run the entry, make every conclusion match the new numbers, and write the new record `attempts/{next_attempt}.yaml`. Its outcomes are this attempt's own; where one differs from `{earlier}`, say why in its notes. Then run `python tools/entry.py handover entries/{entry}`. Do not verify your own work, and do not commit or push: the workflow commits your changes.

Provenance: kind agent; accountable name "CatalystNeuro"; harness "Claude Code"; model "{model}"; protocol: the version stated in docs/protocol.md; runner: platform "{runner}"{runner_url}. Date {date}.

Write prose plainly: no em dashes, never the word "rather", no bold except the "**Result: ...**" openers. YAML plain scalars must not contain ": ".

Your final message is a report with: (1) the outcome per claim, with the earlier outcome next to it; (2) for each earlier finding, whether it is fixed; (3) new findings; (4) anything in the protocol that did not fit a repeat attempt.

Run every command in the foreground and wait for it to finish: the run ends when you stop, and anything still running is lost. Before a command that may take long, time it on a subset and estimate the whole (docs/protocol.md, "Develop on a subset").
