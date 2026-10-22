I couldn't check anything, because there is no claims file for DANDI:001028.

- **Checker:** not run. `claims/001028/` doesn't exist. It isn't on this branch or in any commit in the history.
- **Why:** the last commit (`4c2c5e3c`, "claims (success)") added only `transcripts/001028/claims.md` and `claims-report.md`. That report says a safety classifier blocked the earlier agent's write to `claims/001028/10.1016-j.bioelechem.2023.108437.yaml`, and that it didn't try again. So the run is labelled a success but produced no claims.
- **Changes:** none. I didn't write a claims file myself. Writing claims is step 3 of the Reader procedure, and doing it here would make me both the writer and the checker. I also couldn't add a `checks` entry, since there is no file to add it to.
- **Open:** the claims step has to be run again. The earlier report has notes the next run can use:
  - **Text read:** the accepted manuscript on PubMed Central (PMC10247516). It has no supplement, and the paper links no code.
  - **Dataset:** it covers only the Fig. 9 experiment.
  - **Details the paper leaves open:** how the regions of interest are defined, background handling, normalization, the smoothing settings, what "near the electrodes" and "center" mean, and the test behind Fig. 4.
  - **Inconsistencies in the paper:** section 3.4 gives "~120 a.u." for Packet 1 where the paper's own argument points to Packet 2. Its "4–5-fold" cancellation doesn't match its 4-phasic numbers (126/20.8 is about 6-fold).
- **Ready:** no.
