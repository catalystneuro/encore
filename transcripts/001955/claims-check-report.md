I couldn't check anything for DANDI:001955, because the claims file does not exist.

**Checker result:** none. `python tools/claims_check.py claims/001955/10.64898-2026.02.17.706301.yaml paper/10.64898-2026.02.17.706301.txt` stopped with `FileNotFoundError` (exit 1). There is no `claims/001955/` directory on this branch, and no commit has ever added one.

**Why it's missing:** the last commit (`a7e71f89`, "claims (success)") only adds the transcript under `transcripts/001955/`. That run's own report, `transcripts/001955/claims-report.md`, says a safety classifier stopped its Write call partway through, so it never wrote the file and never ran the checker. The workflow marked the run a success anyway.

**Changes, by claim:** none. With no claims to check, I made no corrections. I also didn't add a `checks` entry: a file holding only that entry would not validate and would not be a claims file. I didn't write the claims myself, because the protocol keeps writing claims (Reader, step 3) and checking them (step 5) in separate runs.

**What remains open:**
- **Next step:** the claims run (Paper run workflow, role `claims`) needs to be run again, then this check.
- **Gaps the next writer must settle:** the failed run's report lists gaps it found, and the new file will need to deal with each one:
  - photometry baseline: the Methods say −1.0 to −0.1 s, the code uses −3.0 to −0.1 s;
  - opto-tagging: the code skips the waveform-correlation check the Methods require;
  - acute activation: the Methods give three bins, the Results say six windows;
  - open-field 1-s bins: the legend corrects post hoc tests by FDR, the Methods by Holm;
  - frequency screen: the Results say 8 mice, the Methods say three;
  - chronic inter-trial interval: 3 to 15 s in the Results, 4 to 35 s in the Methods;
  - the Supplementary Figure 2f legend says "higher" where its own numbers say lower;
  - several measures are never defined (latency, spike width, CV2, bursts, speed, the DA peak and centroid, response magnitude).

**Ready:** no.
