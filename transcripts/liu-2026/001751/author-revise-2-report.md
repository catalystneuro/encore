No outcome changed this round, and nothing is under `proposed`. The verifier agreed with 34 of the 35 outcomes. The entry re-ran in full (`python tools/entry.py all`, 304 s), and the checks pass with 0 errors.

**Outcomes**
- **patchseq-mapping:** the only disagreement. The verifier still leans to partially_reproduced. I kept it blocked (`metadata_insufficient`) and recorded the disagreement: no tested part fails, and the count of inhibitory types cannot be tested from the saved tables. I did not propose a change.

**Corrected or added, each claim now backed by an output**
- **code-table-link:** the table names 288 files, all in the dandiset, not 296. Its presynaptic channel is the one that fires in 286 of those 288 files, or 281 under the −30 mV rule. A new line in cell 11 prints this. The text now says that the 8 files matched by their firing channel agree by construction, so 294 of 296 counts them twice over. I updated cell 13 and the notes.
- **Stimulated-electrode finding:** it still gave the stale 281 of 288. It now gives 286 of the 288 files the table names.
- **fig4d:**
  - Cell 53 and the notes now say the agreement with the code's values (r = 0.99) holds for steps up to 0 mV. With steps up to +85 mV, r is 0.77 to 0.94; cell 52 now prints this.
  - Cell 52 also prints the lines of the paper's code that call a filter. `Fig4d_plotNaCurrent.m` calls none. `extFig9ad_plotVENsubtypeAP_Cmp.m` applies `filter_1000Lowpass` to first-AP traces at line 35. The deviation now says exactly that.
- **"Only published version" / "only revision":** the first code cell now prints the DANDI versions of 001751 and 001750. For each, the draft and the pinned version have the same file count and bytes. Cell 58 prints the MetaboLights revision listing, which holds only MTBLS13927_01. I reworded cells 0, 51 and 57 to match.
- **README run time:** it now gives the measured 4.9 min, 175 s of it streaming. The last code cell prints the total.
- **Supplementary Table 5:** I rendered every PDF in `paper/` with PyMuPDF, installed in a temporary directory. supp1 is the Supplementary Information, supp2 the Reporting Summary, supp3 the Peer Review File, and supp4 to supp9 unprocessed images. None holds Supplementary Tables 1 to 12. I added this to the existing question in `questions/001751.yaml`; a reader will need the tables from the journal's site.
- **Round 2 record:** added under `verifications`, one result for each of the 35 claims, with the verifier's reasons and my responses.

**Other changes**
- `ftp.ebi.ac.uk` refused connections during the first re-run, so I added a retry to the MetaboLights download.

**Not done**
- I did not change the claims file.
- Supplementary Table 5 is still unread, because it is not in `paper/`.
- The 3 annotated connections that peak on the first sample of the window stay descriptive only. The verifier said no outcome depends on them.
