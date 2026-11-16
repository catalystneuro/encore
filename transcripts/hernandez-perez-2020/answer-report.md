There was nothing to answer, so I changed nothing. The file `questions/hernandez-perez-2020.yaml` does not exist, and I found no other questions file for this paper under `questions/`.

The attempt file `attempts/hernandez-perez-2020-01.yaml` (lines 387 to 408) does hold four questions. They are for the paper's authors, though, not for a reader:
- the units of each hc-27 file and the 400 µV theta-amplitude threshold;
- how the Figure 2E phase locking and its slope were computed;
- how Figure 8 defines a cycle's period;
- how cycles were matched across channels for the asymmetry-related delay.

These are method details the paper leaves open. Under `questions/README.md` they belong in the claims' notes and as `methods_unavailable` findings, so they are not mine to settle.

I did not create a questions file, did not edit `claims/hernandez-perez-2020.yaml`, and did not run `tools/claims_check.py`, since there were no edits to check. If an author or verifier meant to ask the reader something, the questions file needs to be written first, and then this step can be run again.
