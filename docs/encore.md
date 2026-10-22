# Encore

Encore checks a dataset against the paper it came from. AI agents read the paper, write down each of its claims and how to test it, and then test the claims on the data, without being able to change them. You get back what came of each claim and, often more useful, what the run found wrong with the data along the way: units that do not match, metadata that is missing, data the paper describes but the files do not hold.

It runs on your own machine, with your own Claude login, on a dataset in any of three places:

```
pip install encore-science

encore check ./nwb/ --paper paper.pdf                    # a directory of files, before you upload them
encore check s3://bucket/smith-2024/ --paper paper.pdf   # files at a URL
encore check DANDI:001234 --draft --paper paper.pdf      # a dataset in an archive
```

Encore follows the same protocol ([protocol.md](https://github.com/catalystneuro/reproduction-registry/blob/main/docs/protocol.md)) as the [registry](https://encorescience.org/), the public record of these checks on published datasets. A check you run yourself stays on your machine; to put a dataset on the record, ask for a run with `encore request`.

## What you need

- [Claude Code](https://docs.claude.com/en/docs/claude-code), signed in to a Claude account or with an API key. Encore uses whatever login Claude Code has, and the run counts against that account's usage.
- Python 3.10 or later, and git.
- The paper, as a PDF or a text file. Encore takes the DOI from the PDF; give `--doi` when it does not show one. A preprint is fine.

## Checking a dataset

```
encore check DATA --paper PAPER [--doi DOI] [--title TITLE] [--full] [--out DIR]
```

A quick check, the default, has three agents in turn: a reader writes the claims file from the paper, a second reader checks it, and an author tests the claims on the data. It takes one to three hours. `--full` adds two rounds of verification, in which an independent agent checks the author's work, and takes several hours more.

The run and its report go to `./encore-<name>-<date>/`, or `--out`. `report.md` there lists every claim with its outcome (reproduced, partially reproduced, not reproduced, or blocked) and every finding about the data, and points to the notebooks the author wrote. A failure to reproduce may be the agent's, not the paper's or the data's: read the notes and the notebooks before acting on one.

If a run stops, for example when the account reaches a usage limit, run the same command again: it goes on from the role that stopped.

```
encore status [DIR]      # which roles are done, and what the running one is doing
```

## What the agents can do

Each agent is Claude Code, run with the same prompt, tools and limits as in the registry. Its commands run in Claude Code's sandbox: they may write only inside the run's directory (and the package caches), and reach only the archives, Python's package index, GitHub and doi.org. A local dataset is read in place and never changed. `--no-sandbox` turns the sandbox off, for a machine where it cannot run; use it only on data and a machine you are comfortable with.

## The registry's queue

```
encore request DANDI:001234 --draft --why "Fixed the units, see lab-to-nwb#12"
encore queue
```

`request` asks for an attempt on the registry's shared queue ([queue.md](https://github.com/catalystneuro/reproduction-registry/blob/main/docs/queue.md)): a repeat attempt after a conversion was fixed, or a first one on a dataset with a paper. It needs the [GitHub CLI](https://cli.github.com), signed in. `queue` shows the queue in order.
