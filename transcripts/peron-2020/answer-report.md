There were no questions to answer. `questions/peron-2020.yaml` doesn't exist, and git history on every branch (local and remote) shows it never has. No other file under `questions/` mentions peron-2020 either; the closest is `peron-2015.yaml`, which belongs to a different paper.

So I changed nothing. `claims/peron-2020.yaml` is untouched, and I didn't create a questions file.

As a sanity check, I ran `python tools/claims_check.py` on the claims file against the paper text:
- **Quotes:** all 30 were found in the text.
- **Values:** 7 statistical values weren't found, all in two claims: one in `distance-dependence-whisking-absent` and six in `behaviour-unchanged`. The file's header says these P values were read from the PDF figure pages because the text extraction garbles or omits them, so the misses are expected. I didn't check them against the PDF myself.

If an author or verifier meant to file questions, they need to be written to `questions/peron-2020.yaml`, and then this reader step can be run again.
