# The run queue

Anyone can ask for an attempt on a dataset by opening a [run request](https://github.com/catalystneuro/reproduction-registry/issues/new?template=run-request.yml): a repeat attempt on a draft after its conversion was fixed ([fixing-conversions.md](fixing-conversions.md), step 6), a first attempt on a dataset the runner has not reached, or a repeat on a new published version. The queue, and each request's place in it, is the open issue labelled `queue-board`, rewritten whenever a request changes.

The record stays where it is: claims, attempts, entries and verifications are files in this repository, and each run is a GitHub Actions job ([pipeline.md](pipeline.md)). The queue is how runs are asked for, ordered and reported on.

## A request's life

| Label | Meaning | What moves it on |
|---|---|---|
| `awaiting-approval` | Asked by someone outside [queue/priority.yaml](../queue/priority.yaml) | Someone in the list adds `approved` |
| `queued` | Waiting its turn | The runner takes it |
| `running` | Being attempted | The attempt ends |
| `needs-you` | The attempt stopped for a person; the dataset's own `needs-you` issue says why | Swap `needs-you` for `queued` to run it again |
| `invalid` | The form cannot be read as a dataset and a version | Edit the request |

A request whose attempt merged is closed, with a link to the pull request. The runner comments on the request when it starts and when it ends.

## Who steers it

[queue/priority.yaml](../queue/priority.yaml) lists the people, the CatalystNeuro team, whose requests are queued without approval, who approve other people's requests, and who can put a request ahead of the others with the `priority` label. Queued requests run with priority first, then oldest first. An `approved` or `priority` label added by anyone else is taken off again. The list is read from `main`, so a branch cannot widen it. Approval is there because every run uses the CatalystNeuro subscriptions: a request costs a few hours of their usage.

## How it runs

`.github/workflows/run-requests.yml` checks a request whenever it is opened, edited or labelled (`tools/runner/run_requests.py check`), labels its state, and rewrites the board. The queue runner (`tools/runner/run_queue.sh`) takes requests after the items in its own `queue.txt` and before the targets it chooses itself; it marks the request `running`, runs the chain, and reports the chain's last line on the request (`run_requests.py next` and `finish`).

The form's text is untrusted. The script reads it, never a shell, and the runner gets only a dataset and a version that match strict patterns, re-checked when the request is taken.

## What comes next

1. **The runner off one person's machine.** The runner is still a process on one Mac, using its owner's GitHub login. The next step moves the chain's logic (`chain.sh`) into a scheduled workflow that advances each running request by one step at each tick: start the next role when the last succeeded, retry after a usage limit, move to the verified account after a flag, finish and merge. Nothing then runs on anyone's machine, and the queue keeps going when that machine sleeps.
2. **Checks for people converting data, outside the queue.** Someone converting a dataset wants feedback before publishing, often before the paper is out. A local command (`registry check <dandiset> --draft --paper paper.pdf`) runs the same protocol on their machine, with their own Claude account or API key, and writes the report locally; the NWB conversion skill calls it when a conversion is done. A `--submit` flag opens a run request, so that the result can go on the record through the queue and its verification. A quicker mode, one author run with no verification rounds, can give a first answer in minutes.
3. **A service, when it is needed.** A hosted queue with its own accounts and workers is worth building once one of these is true: people need quotas or to pay for their own runs on the shared queue, private datasets have to go through the shared queue rather than the local check, or attempts outgrow GitHub Actions' six-hour job limit. Only the queue would change; the record would not.
