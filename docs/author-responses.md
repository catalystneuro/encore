# Author responses

An author of a paper can respond to an attempt on its data with the issue form
[Respond to an attempt](https://github.com/catalystneuro/encore/issues/new?template=author-response.yml).
Each paper's page links to the form, filled in for the paper's latest attempt and the first dataset it used. The form's issues carry the
label `author-response`.

## What a maintainer does with one

1. **Confirm the author.** Check that the ORCID iD (or, without one, an email from the author's institution)
   belongs to one of the paper's authors. Then add the label `author-confirmed`. Only confirmed responses are
   shown on the paper's page and on the dataset's page; the page counts the others as awaiting confirmation. A response from someone who
   is not an author (a dataset's maintainer, say) is shown once it has the label `confirmed`, as a response, not as
   an author's.
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
3. **Keep it public.** The response stays on the paper's and the dataset's pages after the issue is closed: it is part of the
   attempt's record.
