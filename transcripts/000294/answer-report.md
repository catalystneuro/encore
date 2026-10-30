I had no questions to answer: `questions/000294.yaml` doesn't exist. It isn't in the working tree, and no branch in the git history has ever had it.

That matches the author run. Its report (`transcripts/000294/author-report.md`, line 35) says it "asked no reader anything." The only DANDI:000294 run so far is that author run (`470a80484`). No verifier has run, so no verifier questions exist either.

So I changed nothing in `claims/000294/` and didn't create a questions file. As a check, `python tools/claims_check.py` against the paper text found no problems: 23 claims, 23 quotes, 3 statistical values.

The author report does note three choices it made where the protocol was unclear, but it didn't raise any of them as a question:
- **Simulator stack:** it swapped the paper's simulators for a different setup that runs on the entry's Python, and recorded that as a deviation.
- **Two cells, one value:** where the paper gives values for two cells, it entered a single expected value.
- **Tolerance at the 0% step:** a 10% relative tolerance is undefined there, so it changed how that step is judged.

The second and third concern how claims are scored. If a verifier later turns either into a question, I can answer it then.
