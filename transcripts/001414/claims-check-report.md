There is nothing to check: no claims file for DANDI:001414 exists.

- **Checker result:** not run. `claims/001414/` does not exist on this branch, and no file under that path appears in any branch's git history.
- **Why:** the claims run's own report (`transcripts/001414/claims-report.md`) says a safety classifier stopped its write and it did not retry. It wrote no claims file and committed only its transcript and report. It had planned about 50 claims from the Fig. 1–6 and S1–S6 legends and Tables S1–S4. Its report also lists method details it found open, such as how to read the "80% decay time", the start of the post-LED window, the units of the area under the curve and the maximum dilation rate, and how to measure the delay between cAMP and dilation.
- **Changes:** none. A `checks` entry needs a file to go in, so I added none. I did not write the claims myself either, because writing them belongs to the claims run, not to this check.
- **What remains open:** all of it. The claims role needs to run again on 001414 and produce the file before a check can be made. The paper is there for that run (`paper/10.1073-pnas.2422069122.txt` and the supplement PDF). The claims report says the main-text PDF was not supplied, so the main figures could only be read from their legends.
- **Ready:** no.
