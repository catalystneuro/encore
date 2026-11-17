There was nothing to answer, so I changed nothing.

**The questions file `questions/watson-2016.yaml` doesn't exist.** It isn't in the working tree, on either branch (`attempt/watson-2016`, `main`), or anywhere in git history. There is no per-dataset version under `questions/watson-2016/` either. With no questions, I left `claims/watson-2016.yaml` untouched, created no questions file, set no `answered` dates, and had no edited quotes to run `tools/claims_check.py` on.

There is a sign that a question was meant to be filed and wasn't. In `attempts/watson-2016-02.yaml` (around line 1104), the response for claim `post-sleep-wake-lower` says the post-sleep WAKE window "stays with a reader (questions file)". Nothing was written for it. If that question should come to a reader, the author or a revision run needs to add it to `questions/watson-2016.yaml` first, and then an answer run can take it up.
