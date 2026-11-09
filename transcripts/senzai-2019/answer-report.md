There were no questions to answer for 000166, so I changed nothing.

- **No questions file:** `questions/000166.yaml` doesn't exist in the working tree or on any branch.
- **The author asked none:** the author report (`transcripts/000166/author-report.md`) says "I asked a reader no questions."
- **Where the author's questions went:** the author's three open points are recorded in `attempts/000166-senzai-2019-01.yaml` as `methods_unavailable` findings addressed to the paper's authors, not to a reader. They are how the CSD landmarks were chosen, which LFP site Figure S7 used, and what extra selections the monosynaptic detection applied.
- **Quote check:** `python tools/claims_check.py` on the unchanged claims file matched all 47 quotes. It reported 2 statistical values it couldn't find in the text, and these still need confirming by reading the paper: p = 0.0004 for `fig3c-slow-oscillation-nrem-deep` and p = 2e-06 for `fig3c-3-6hz-layer4`. They are already in the file, and I left them alone because no question raised them.

Nothing was committed or pushed.
