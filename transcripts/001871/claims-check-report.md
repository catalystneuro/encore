There was nothing to check: no claims file exists for DANDI:001871.

- **Checker:** it did not run. `claims/001871/` does not exist, so there was no `<file>.yaml` to pass to `tools/claims_check.py`.
- **Why there is no file:** the previous reader run (`transcripts/001871/claims-report.md`) wrote no claims because the paper's text was missing. I confirmed this. `paper/` holds only `10.1073-pnas.2608896123.txt` and its PDF. That is "Fly navigational responses exploit plume-specific odor motion and gradient cues" (Brudner et al., PNAS 2026). It cites the target paper as reference 30 and uses its plumes, but it does not report that paper's Methods or findings, so no claims can be taken from it.
- **Changes:** none. I created no file, because a `checks` entry has to be added to an existing claims file. Writing claims myself would also be the reader's job, not the checker's, and could only be done from a paper that is not here.
- **Still missing:** the full text of doi:10.1007/s00348-018-2591-3 (Connor, McHugh and Crimaldi, Exp. Fluids 59, 2018), with its Methods and any supplement. It needs to go under `paper/` as a `.txt`, plus the PDF if there is one. Once it is there, the reader run should be started again, and then the check.
- **Ready:** no.
