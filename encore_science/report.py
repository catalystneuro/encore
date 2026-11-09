"""The report at the end of `encore check`: what came of each claim, and what the run found about the data."""

from __future__ import annotations

from collections import Counter
from pathlib import Path

import yaml

LABELS = {"reproduced": "reproduced", "partially_reproduced": "partially reproduced",
          "not_reproduced": "not reproduced", "blocked": "blocked"}
ORDER = list(LABELS)
KINDS = {"metadata_error": "Metadata error", "data_missing": "Data missing", "identifier_missing": "Identifier missing",
         "metadata_insufficient": "Metadata insufficient", "selection_undocumented": "Selection undocumented",
         "methods_unavailable": "Methods unavailable", "format_error": "Format error", "code_mismatch": "Code mismatch",
         "paper_inconsistency": "Paper inconsistency", "other": "Other"}


def files_in(directory: Path, pattern: str) -> list[Path]:
    """The files in a directory that match a pattern, sorted, leaving out hidden ones. On a drive that is not
    formatted for macOS (exFAT, FAT32, a network share), macOS writes a "._" file beside every file it writes,
    and "._c.yaml" matches "*.yaml" but is not YAML."""
    return sorted(p for p in directory.glob(pattern) if not p.name.startswith("."))


def latest_attempt(registry: Path, folder: str) -> dict | None:
    found = files_in(registry / "attempts", f"{folder}-*.yaml")
    return yaml.safe_load(found[-1].read_text()) if found else None


def claims_of(registry: Path, folder: str) -> dict[str, dict]:
    out = {}
    for path in files_in(registry / "claims" / folder, "*.yaml"):
        for c in (yaml.safe_load(path.read_text()) or {}).get("claims") or []:
            out[c["id"]] = c
    return out


def open_questions(registry: Path, folder: str) -> list[dict]:
    path = registry / "questions" / f"{folder}.yaml"
    if not path.is_file():
        return []
    q = yaml.safe_load(path.read_text()) or []
    q = q.get("questions", []) if isinstance(q, dict) else q
    return [x for x in q if not x.get("answered")]


def one_line(text: str, width: int = 300) -> str:
    text = " ".join(str(text or "").split())
    return text if len(text) <= width else text[:width - 1] + "…"


def summary(record: dict | None) -> str:
    if not record:
        return "no attempt record"
    counts = Counter(o["outcome"] for o in record.get("outcomes", []))
    return ", ".join(f"{counts[k]} {LABELS[k]}" for k in ORDER if counts[k])


def write_report(out: Path, registry: Path, state: dict) -> Path:
    folder = state["folder"]
    record = latest_attempt(registry, folder)
    claims = claims_of(registry, folder)
    d = state["dataset"]
    lines = [f"# Encore report: {state['title']}", "",
             f"- **Dataset:** `{d['location']}`" + (f" (fingerprint `{d['fingerprint']}`)" if d.get("fingerprint") else ""),
             f"- **Paper:** doi:{state['doi']}",
             f"- **Run:** {state['mode']} ({', '.join(r for r, v in state['roles'].items() if v.get('status') == 'success')}), "
             f"model {state['model']}, protocol {state['protocol']}, finished {state.get('finished', '')[:16]}",
             "", "Encore's agents read the paper, wrote down its claims and how to test each, and then tested them "
             "on the dataset. A failure to reproduce may be the agent's, not the paper's or the data's: read the "
             "notes and the notebooks before acting on one."
             + ("" if state["mode"] == "full" else " This was a quick run, with no verification rounds: an "
                "independent agent has not checked the author's work. Run with --full for that."), ""]
    if record is None:
        lines += ["**The author wrote no attempt record**, so there are no outcomes to report. Its report is in "
                  f"`registry/transcripts/{folder}/author-report.md`.", ""]
    else:
        lines += [f"## Claims: {summary(record)}", "", "| Claim | Outcome | Notes |", "|---|---|---|"]
        for o in sorted(record.get("outcomes", []), key=lambda o: ORDER.index(o["outcome"])):
            c = claims.get(o["claim"], {})
            outcome = LABELS[o["outcome"]] + (f" ({o['blocked_by'].replace('_', ' ')})" if o.get("blocked_by") else "")
            lines.append(f"| **{o['claim']}**<br>{one_line(c.get('statement'), 200)} | {outcome} | "
                         f"{one_line(o.get('notes')).replace('|', '/')} |")
        findings = record.get("findings") or []
        lines += ["", f"## Findings about the data: {len(findings)}", ""]
        if findings:
            lines += [f"- **{KINDS.get(f['kind'], f['kind'])}.** {one_line(f['statement'], 600)}" for f in findings]
        else:
            lines.append("None.")
        lines.append("")
    questions = open_questions(registry, folder)
    if questions:
        lines += [f"## Open questions: {len(questions)}", "",
                  "The author or a verifier believes the claims file misreads the paper on these claims, and "
                  "asked a reader. The claims were tested as the file has them." + ("" if state["mode"] == "full" else
                                                                     " A --full run has a reader answer them."), ""]
        lines += [f"- {one_line(q.get('question') or q.get('text') or q, 400)}" for q in questions]
        lines.append("")
    entry = record.get("entry") if record else None
    lines += ["## Where everything is", "",
              f"- The claims and how each was tested: `registry/claims/{folder}/`"]
    if entry:
        lines.append(f"- The notebooks: `registry/entries/{entry}/`")
        lines.append(f"- The attempt record: `registry/attempts/{record['id']}.yaml`")
    lines += [f"- What each agent did: `registry/transcripts/{folder}/`", ""]
    path = out / "report.md"
    path.write_text("\n".join(lines))
    return path
