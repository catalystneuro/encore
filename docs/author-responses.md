# Author responses

An author of a paper can respond to an attempt on it with the issue form
[Respond to an attempt](https://github.com/catalystneuro/encore/issues/new?template=author-response.yml).
A response is to a paper's attempt: the claims and their outcomes belong to the paper. So the link to the form
is on the paper's page and on each attempt's page (`papers/<paper>/<attempt>/`), filled in for the paper and the
attempt; a paper with several current attempts leaves the attempt to the writer. A dataset's page has no link:
what an attempt found about the data is for the dataset's owner and the archive. The form's issues carry the
label `author-response`.

## What a maintainer does with one

1. **Confirm the author.** The paper's page lists its authors, each with an ORCID iD where OpenAlex has one
   (`papers/authors.yaml`). Check that the ORCID iD on the form is one of them (or, without one, write to the
   author at their institution). Then add the label `author-confirmed`. An iD typed into a form is a claim, not
   proof, so the label is a person's decision: where it matters, ask the author to confirm from the email on
   their ORCID record. Only confirmed responses are shown; the paper's page counts the others as awaiting
   confirmation. A response from someone who is not an author (a maintainer of the dataset, say) is shown once
   it has the label `confirmed`, as a response, not as an author's.
2. **Act on it**, by what the author says:
   - **The outcomes look right:** add a verification of kind `paper_author` to the attempt's record
     (`attempts/<attempt>.yaml`, schemas/attempt.schema.json): `date`, `by` (the author's name and the issue's URL)
     and `results`, one `{claim, agrees}` for each claim the author speaks to. The
     attempt's tier becomes `author_endorsed` (docs/design.md, "Trust tiers"). Close the issue.
   - **Some outcomes are wrong, or the attempt misread the claims:** reply with what will change. A misread claim is
     corrected in the claims file and the attempt run again (a run request, docs/queue.md); an outcome the author
     shows to be wrong is a reason to run the attempt again, and the author's points go into the request. Label the
     issue `disputed` until the new attempt has merged.
   - **The dataset differs from what the paper used:** this is a finding about the data. Open an issue on the
     conversion, or tell the archive, and link it here.
3. **Keep it public.** The response stays on the site after the issue is closed: it is part of the attempt's
   record.

## Where a response is shown

- On the paper's page, under the attempts' summaries: every confirmed response to the paper's attempts.
- On an attempt's page: the responses to that attempt, and those to the paper's attempts in general.
- On the writer's own page (`authors/<ORCID>/`), in a Responses tab, when the form gave an ORCID iD the registry
  knows.
