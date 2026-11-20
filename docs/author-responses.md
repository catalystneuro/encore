# Author responses

Authors of a paper can respond to a reproduction attempt with the
[Respond to an attempt](https://github.com/catalystneuro/encore/issues/new?template=author-response.yml)
issue form. Each submission opens a GitHub issue with the label `author-response`.

## Links to the form

The form is linked from two kinds of page:

- **A paper's page.** If the paper has one current attempt, the link fills in the paper and that attempt. If it
  has several, the link fills in the paper only, and the author chooses the attempt.
- **An attempt's page** (`papers/<paper>/<attempt>/`). The link fills in the paper and the attempt.

Dataset pages do not link to the form. A response is about a paper's claims and their outcomes. Findings about
the data are for the dataset's owner and the archive.

## Maintainer steps

### 1. Confirm the author

The paper's page lists its authors with their ORCID iDs, where OpenAlex has them. The list is stored in
`papers/authors.yaml`.

- If the form includes an ORCID iD, check that it belongs to one of the paper's authors.
- If it does not, email the author at their institution.

An ORCID iD typed into a form does not prove who wrote it. When the response has consequences, such as an
endorsement or a dispute, ask the author to confirm by email from the address on their ORCID record.

Then add one of these labels to the issue:

| Label | Meaning |
|---|---|
| `author-confirmed` | The writer is an author of the paper. |
| `confirmed` | The writer's identity is confirmed, but they are not an author. For example, they maintain the dataset. |

The site shows only responses that have one of these labels. A `confirmed` response is shown as coming from
someone who is not an author. Responses without a label are not shown; the paper's page gives only their number,
as awaiting confirmation.

### 2. Act on the response

The next step depends on the view the author chose in the form.

**The outcomes look right.** Add a verification of kind `paper_author` to the attempt's record
(`attempts/<attempt>.yaml`, described in `schemas/attempt.schema.json`) with these fields:

- `date`
- `by`: the author's name and the issue's URL
- `results`: one `{claim, agrees}` entry for each claim the author addresses

This moves the attempt to the `author_endorsed` tier (see "Trust tiers" in `docs/design.md`). Then close the
issue.

**Some outcomes are wrong, or the attempt misread the claims.** Reply on the issue to say what will change, and
add the label `disputed`.

- If a claim was misread, correct the claims file and run the attempt again with a run request
  (`docs/queue.md`).
- If the author shows that an outcome is wrong, run the attempt again and include the author's points in the
  run request.

Remove `disputed` when the new attempt is merged.

### Notes for the next attempt

A response often holds what an attempt lacked: how something was computed, a link to the paper's code, or where
some data are. To give that to the next attempt:

1. Confirm the writer (step 1). Only a confirmed response is taken.
2. Run `python tools/author_notes.py add <issue number>`. It copies the response's text, its links and the claims
   it names into `papers/author-notes/<paper>.yaml`. Read the file before you commit it.
3. Commit the file to `main`.
4. Queue the paper again with a run request (`docs/queue.md`).

The next attempt's author reads the notes with the paper (`docs/protocol.md`, "Notes from the paper's authors").
The author stays blind to the earlier attempts, so take out of the notes anything that says what an earlier attempt
found. The new attempt's record lists the notes it used, and the paper's page links to them.

A note can settle a method the paper leaves open, and it can point to code or data. It cannot set an outcome: the
claim is tested all the same, against the same criterion.

**The dataset differs from what the paper used.** Treat this as a finding about the data. Open an issue on the
conversion or notify the archive, and link to it from the response's issue.

### 3. Keep the response public

A response stays on the site after its issue is closed. It is part of the attempt's record.

## Where responses appear

| Page | What it shows |
|---|---|
| Paper page | Every confirmed response to the paper's attempts, below the attempt summaries. |
| Attempt page (`papers/<paper>/<attempt>/`) | Confirmed responses to that attempt, and responses that named no attempt. |
| Author page (`authors/<ORCID>/`) | A Responses tab with the author's confirmed responses, if the form included an ORCID iD that the registry knows. |
