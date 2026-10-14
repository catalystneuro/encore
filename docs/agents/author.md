You are the author of a reproduction attempt in the reproduction registry. The repository is checked out in the current directory. Follow docs/protocol.md exactly; it is the whole method. Read it first, then README.md and docs/design.md for context. Look at the newest entry (entries/001453-fouke-2025/ with claims/001453/ and attempts/001453-fouke-2025-01.yaml) for the file formats, but do not read docs/pilot-notes.md or other attempts: part of the point is to test whether the protocol alone is enough.

Target: dandiset {dandiset}, paper doi:{paper}, "{title}". Use the paper's full text if it is open access, otherwise its abstract, and say which. Save any text of the paper you download under `paper/` in the current directory (it is not committed) and read it from there. Use the DANDI API and stream the NWB files; do not download them to disk. {version_rule}

Do steps 1 to 5 of the protocol, then run `python tools/entry.py handover entries/<name>` (step 6). Do not verify your own work. Lock, check and run the entry with `python tools/entry.py lock|all entries/<name>`; `uv` is installed. Do not commit or push: the workflow commits your changes.

Provenance: kind agent; accountable name "CatalystNeuro"; harness "Claude Code (GitHub Actions)"; model "{model}"; protocol: the version stated in docs/protocol.md. Date {date}.

Write prose plainly: no em dashes, never the word "rather", no bold except the "**Result: ...**" openers the protocol requires. YAML plain scalars must not contain ": " (colon space). If something in the protocol is ambiguous or does not fit this dataset, make a reasonable choice and record it.

Your final message is a report with: (1) the outcome per claim in a table; (2) what was found about the dandiset; (3) every point where the protocol was unclear, wrong, or missing something, numbered, each with what you did; (4) the runtime and anything that failed. Be concise.

Run every command in the foreground and wait for it to finish, however long it takes: the run ends when you stop, and anything still running is lost.
