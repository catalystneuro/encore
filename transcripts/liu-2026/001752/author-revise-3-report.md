Round 3 is recorded. The verifier agreed with all three proposed changes, so all three outcomes changed and no proposal is left open. `python tools/entry.py all entries/001752-liu-2026` passes with 0 errors, and both notebooks ran.

**Outcomes changed:**
- **fig5b-sipsc-frequency:** not_reproduced → blocked (`methods_underspecified`). At 5 pA the detector cannot tell events from noise in these files, and the paper gives no other detection setting.
- **fig5c-sipsc-amplitude:** reproduced → blocked (`methods_underspecified`). It uses the same detection as the sIPSC frequency claim. The notes now include the verifier's point that noise near the threshold biases the test towards "no difference".
- **fig4ac-ap-width-amplitude:** partially_reproduced → not_reproduced. Neither feature reaches p < 0.001, and the criterion has no partial case.

**Other changes:**
- In the attempt record, `proposed` is gone from all three claims and the notes match the new outcomes.
- Round 3 is recorded under `verifications`: one result per claim, with the verifier's reasons and my response.
- The notebooks' conclusions and summaries, the README table and the text are updated to match. The "failure to reproduce" sentence stays, since mEPSC frequency and fig4ac are still not reproduced.
- The verifier reported that the claims file may misread the paper for fig4ac. The Results call the 281 VENs and 306 PCs "additional" recordings, so they may not be the Patch-seq cells in DANDI:001746. As the protocol says, I left the claim unchanged and added this as a question for a reader in `questions/001752.yaml`. The notes no longer call the deposited cells "a quarter of the paper's".

Nothing is committed. `tools/build_site.py` and `tools/site_assets/app.css` were already modified before this run, and I did not touch them.
