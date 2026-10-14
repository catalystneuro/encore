# Transcripts of agent runs

One folder per dandiset. Each run of an agent on an attempt (the author, each
verification round, each revision) leaves its transcript, `<role>.md`, and its
final report, `<role>-report.md`. The roles and their order are in
[`docs/agents/`](../docs/agents) and [`tools/agent_run.py`](../tools/agent_run.py).

Runs are made by the [Agent run](../.github/workflows/attempt.yml) workflow on a
fresh GitHub Actions runner, so the agent has no personal configuration and
the verifier sees only its materials. [`tools/transcript.py`](../tools/transcript.py)
turns the raw transcript into these files. It keeps the prompt, every message
and every tool call. It leaves out the session context, thinking, the text of
fetched pages and of the paper, and all but the first lines of each tool
result, and it replaces anything left that looks like an e-mail address, a
token or a home directory path with a note saying what was removed.

The 000207 verifier transcript is from a run on a person's machine before the
workflow existed, exported the same way. The transcripts of the first three
author runs were not kept.
