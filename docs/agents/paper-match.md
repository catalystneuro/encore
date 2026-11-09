You decide, for dataset {dataset} in the reproduction registry, whether each paper the archive links to it is the paper behind its data. The repository is checked out in the current directory. Read docs/pipeline.md, step 1, first. An attempt reproduces a paper's findings from the dataset; a paper whose findings rest on other data cannot be reproduced from it, and an attempt on it is wasted.

The match file is `papers/match/{folder}.yaml`. The cheap checks (tools/paper_match.py) have written it: a paper they settled has a verdict, `by: checks`; give each paper without a verdict one. You may correct a checks verdict when you find it wrong; then set `by: agent` and say why.

Papers the archive names, after papers/triage.yaml:
{papers}

What to read:
- Each paper's full text under `paper/` (`<doi with / as ->.txt`, with the PDF where there is one): the title page, the abstract, the Methods as far as which animals, sessions and recordings, and the Data availability (or Data Records, Code and data) section. When a paper has no text there, read its abstract and its data statement from the publisher or Europe PMC.
- The dataset's archive metadata: {metadata}. Its name, description, contributors, the relation it gives each paper, and its summary of subjects, species, techniques and sizes. You may list its file paths ({files}) to see subject and session names. Do not open or download any data file: the claims are written later by a reader who has not seen the data, and nothing in this run may tell it what the data hold.

Verdicts, one per paper:
- `primary`: the dataset is the paper's data, or the data a paper re-analyses: its findings rest on what the dataset holds.
- `partial`: the dataset holds part of the paper's data (some of its sessions, one of its modalities, one of its experiments) and some of its findings can be tested on it. Say which part in `reason`, and list the other datasets in `data_in` when the paper names them.
- `other_data`: a research paper whose findings rest on data the dataset does not hold: the paper names another dataset as its data, or describes recordings (subjects, areas, stimuli, technique) the dataset does not hold. Say where the data are in `data_in` when the paper says.
- `background`: a paper cited for context: a review, a method, an earlier study.
- `not_a_paper`: a dataset, a protocol, software or a figure carries the DOI.
- `wrong_doi`: the DOI resolves to a paper unrelated to the dataset (a mistyped DOI): say in `reason` which paper the archive seems to mean, with its DOI when you can find it.

Judge by evidence, not by the relation alone: the archive's relations are often loose (`Describes` used for `IsDescribedBy`, a sister project's paper listed as `IsSupplementTo`). The strongest evidence is a dataset the paper itself names as its data; then whether its subjects, sessions, areas, stimuli and technique are what the dataset's metadata describes; then shared authors. A paper that names this dataset among several is `partial` when the others hold data its findings rest on. When the evidence is mixed, choose `partial` over `other_data`, and say what is uncertain.

For every paper you judge, write `verdict`, `by: agent`, `reason` (one or two plain sentences), and `evidence`: one or more `{{source, quote}}` items, the source a section of the paper or "archive metadata", the quote short and exact. Add `data_in` where it applies. Never write `confirmed`: a person sets it. Keep the `checks` the script wrote. Validate with `python tools/paper_match.py validate papers/match/{folder}.yaml` and fix the file until it passes.

Do not commit or push: the workflow commits your changes. Only `papers/match/{folder}.yaml` is kept.

Provenance: you are model "{model}", Claude Code, runner "{runner}", {date}; put it nowhere in the file, the commit records it.

Write prose plainly: no em dashes, never the word "rather". YAML plain scalars must not contain ": " (colon space).

Your final message is a report: each paper's verdict and the one piece of evidence that decided it, and, when no paper is primary or partial, which dataset (if any) holds the paper's data. Be concise.

Run every command in the foreground and wait for it to finish.
