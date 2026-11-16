I answered nothing and changed no files, because there are no questions to answer.

- **No questions file:** `questions/peyrache-2015.yaml` does not exist in the working tree, and git history has no version of it on any branch. No other file under `questions/` mentions `peyrache-2015`, and the attempt record `attempts/peyrache-2015-02.yaml` has no questions section.
- **Claims file:** I left `claims/peyrache-2015.yaml` as it is. Nobody has challenged a claim, and setting `answered` dates needs questions to put them on. The `tools/claims_check.py` quote check is only needed after an edit, so I did not run it.
- **What I did find:** `attempts/peyrache-2015-02.yaml` lists three "Question for the authors" findings: how the OLE decoders were built, which sessions gave the ADn cells, and how the decoded angular speed was computed. These are method details the paper leaves open. They are questions for the paper's authors, not for the reader, so they don't belong in the questions file.

If the questions file should exist, it was probably not committed or copied in when this run was set up. Once it is supplied, I can answer it.
