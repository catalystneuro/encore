# Reproduction registry: design

Status: draft for discussion. "Reproduction registry" is a working name.

## Goal

Agents work through the dandisets on the DANDI Archive that have an associated
paper. For each one, an agent tries to reproduce the paper's key findings and
figures from the open data, writes the analysis as a notebook, and registers it
here. People can deposit too, but most deposits are expected to come from
agents.

This serves two purposes:

1. **Check the data.** A finding that can be reproduced shows the dandiset is
   complete and accurate enough to support it. A finding that cannot be
   reproduced, with the reason, tells the data owner and the archive what is
   missing.
2. **Give analysts a starting point.** Someone who wants to test a new
   hypothesis on a dandiset starts from notebooks that already load the data
   and reproduce known results, builds on them, and registers the new
   notebooks here as well.

## What the queue looks like today

`tools/build_targets.py` builds the queue from the public DANDI API. On
2026-10-13:

| | |
|---|---|
| Public, non-empty dandisets | 655 |
| Name at least one paper in their metadata | 231 |
| ...of which have a published version | 200 |
| ...of which use NWB | 219 |
| Distinct papers | 245 |
| Targets whose only papers are preprints | 48 |
| Papers shared by more than one dandiset | 23 |

Median target size is 23 GB; 86 are under 10 GB and 34 are over 1 TB. A paper
here is a related resource with a DOI that is not a dataset, software or
repository record.

The 424 dandisets that name no paper are out of scope for reproduction, but
"this dandiset has a paper and does not link it" is itself something the
campaign can find and report.

## The objects

The registry records **claims that were tested**, not just notebooks that run.

- **Target.** A dandiset and a paper it is associated with. Generated from the
  archive; never edited by hand.
- **Claim.** One finding of the paper that the data should support, usually a
  figure panel or a reported statistic: "Figure 2B: reach-related high-gamma
  power increases over sensorimotor cortex." An agent proposes the claims for a
  target when it starts work.
- **Attempt.** One try at reproducing the claims of a target, by one agent run
  or one person. An attempt always produces a record, whether or not it
  produces a working notebook. Each claim gets an outcome:
  - `reproduced`: the result matches the paper.
  - `partially_reproduced`: the effect is present but weaker, or holds only
    in part.
  - `not_reproduced`: the analysis ran and the result differs.
  - `blocked`: the analysis could not be done, with a reason category:
    `data_missing`, `metadata_insufficient`, `methods_underspecified`,
    `data_unreadable`, `too_large`, `other`.

  The outcome describes the result. How the test differed from the paper's
  method or data (one session of four, a substituted model) is recorded
  separately as the outcome's deviations, so that "partially reproduced" always
  means something about the effect.
- **Entry.** A directory of notebooks with metadata, as in the example-notebooks
  registry. An attempt that produces notebooks produces an entry. Entries that
  are not reproductions (data orientation, new analyses) have no claims.
- **Verification.** A check of an attempt by someone other than its author:
  another agent or a person. It records, per claim, whether the verifier agrees
  with the stated outcome.
- **Dandiset report.** Everything known about one dandiset, rolled up: which
  claims were reproduced, which were blocked and why. This is the data-quality
  output for curators and data owners.

## Entry types and building on each other

- **`orientation`:** how to load this dandiset and what is in it. The first
  entry for a dandiset. Its helper module is the data-access layer that later
  entries import.
- **`reproduction`:** reproduces one or more claims of a paper.
- **`analysis`:** new work on the data, by a person or an agent.

An entry declares what it builds on with a `derived_from` relation to another
entry. That gives the path from "load the data" to "reproduce figure 2" to "my
new analysis" and lets the catalog show it.

## Trust tiers

A single human gate at intake does not scale to agent deposits. Instead each
entry carries the highest tier it has reached:

1. **`runs`:** passes the automated gates below. Agent deposits are merged at
   this tier without a human.
2. **`agent_verified`:** an independent agent agrees with the stated outcomes.
3. **`human_verified`:** a person has checked the comparison with the paper.
4. **`author_endorsed`:** an author of the paper has confirmed it.

Catalog views and badges show the tier. DOIs are minted only from
`human_verified` up (see open decisions).

## Automated gates for a deposit

All of these run in CI on the pull request:

- Metadata validates against the schema; every notebook is listed.
- The environment is locked and the install cell matches the lock file.
- Every notebook executes from a clean environment, streaming the data from
  the archive, inside the time and memory limits.
- **Data-derivation checks.** The notebook reads the dandiset it names, does
  not embed large literal arrays or images, and does not fetch figures from
  elsewhere. This is the guard against a result that only looks right.
- Each claim names the notebook and the output cell that shows it.

## Verification

The verifier is given the paper, the executed notebook and the claims. It was
not involved in writing the notebook. For each claim it:

1. finds the figure or statistic in the paper;
2. compares it with the notebook's output against a rubric (same quantity,
   same conditions, same direction and rough size of effect);
3. reads the code that produces it for shortcuts;
4. records agree / disagree with a short reason.

Where the paper reports numbers, the claim can carry an expected value and
tolerance, and the check is done in CI rather than by judgment.

A sample of verified attempts is audited by a person to measure how often the
verifier is right. That number is published.

## Provenance

Every attempt records who produced it: for an agent, the agent harness, model,
protocol version and the person or organisation that ran it; for a person,
their name and ORCID. The accountable party is always a person or
organisation, never the agent alone.

## Feedback to data owners

A `blocked` or `not_reproduced` outcome is a finding about the data or the
paper. The registry rolls these up per dandiset and can open an issue or send
a report. Whether and how owners are contacted is an open decision; the pilot
contacts no one.

## Maintenance

Entries are re-run on a schedule. When an agent-deposited entry breaks, the
failure dispatches an agent to repair it, and the repair goes through the same
gates and verification. A person is only pulled in when the repair fails.

## Repository layout

```
targets/dandisets.json            generated queue
claims/<dandiset>/<doi-slug>.yaml the claims proposed for one target
attempts/<id>.yaml                one record per attempt, including failures
entries/<slug>/                   notebooks, entry.yaml, lock files, helpers
reports/<dandiset>.json           generated per-dandiset roll-up
schemas/                          JSON Schemas for the files above
tools/                            queue builder, checks, harness
```

Where an entry sits carries no meaning; relations are in its metadata.

## What is reused from the example-notebooks registry

That work (in the CatalystNeuro fork of `dandi/example-notebooks`) stays as it
is. The parts that carry over, adapted:

- the notebook test harness and the locked-environment tooling;
- metadata linting and the unit-test setup;
- per-entry health from scheduled re-runs;
- the merge bot, for entries with human maintainers;
- releases with DOIs;
- container images per entry.

Not carried over: the DANDI index page, Colab-first conventions, the old
`<dandiset>/<lab>/` layout, and the 47 existing entries. Existing example
notebooks can be registered later as `orientation` or `reproduction` entries
if their authors want.

## Phasing

1. **Pilot, by hand.** The eight targets in `targets/pilot.yaml`, chosen to be
   small and varied. An
   agent attempts each with a person watching. The purpose is to learn which
   outcomes and blocking reasons actually occur and what a verifier needs.
   The schemas below are revised from what the pilot shows. Lessons from
   each attempt are collected in [`pilot-notes.md`](pilot-notes.md). The steps an author and a
   verifier follow are in [`protocol.md`](protocol.md).
2. **Deposit path.** Schemas, the automated gates, the agent contributor kit
   (one command that locks, lints and runs an entry locally, and a guide to
   the conventions).
3. **Verification.** The verifier, its rubric, and the human audit.
4. **Scale.** The queue with claiming, the per-dandiset reports, scheduled
   re-runs and repair.
5. **Catalog.** Per-dandiset lookup for archive pages, the browsable catalog,
   and releases with DOIs for the verified tiers.

## Open decisions

Each has a proposed default, used until decided otherwise.

1. **Are failed attempts public?** Proposed: yes. They are the data-quality
   result. Wording is factual and names the reason category.
2. **Who is the author of an agent-written notebook?** Proposed: the person or
   organisation that ran the agent is the accountable party in provenance; the
   agent is recorded but is not an author. No DOI below `human_verified`, and
   the DOI's creators are the people who verified and take responsibility.
3. **Are paper authors and data owners contacted?** Proposed: not during the
   pilot. Afterwards, a report per dandiset that owners can opt into.
4. **Copyright of paper figures.** Proposed: store references (DOI and figure
   number) and the claim in words, not copies of figures. The verifier fetches
   the paper at check time.
5. **Home and name.** Which organisation hosts the repository, what it is
   called, and whether it is public from the start.
6. **Scope beyond DANDI.** The model does not depend on DANDI, but the queue
   builder does. Other archives would each need a queue builder.
