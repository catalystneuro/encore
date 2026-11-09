## Check of claims/000336 (Gillon, Lecoq et al. 2023)

**Checker result:** `18 claims, 18 quotes, 0 statistical values, 0 problems`. I ran it before and after my edits.

All 18 statements, sources and quotes match the paper. I checked every number against the text and Tables 1 and 2: the counts of mice and sexes, the 50 sessions, the ROI ranges, the tracked counts (the four per-plane sums of Table 2 over the 11 analysed mice), and the example mice (136 and 47). I also cloned the paper's code at the cited commits. The windows, the example mice (mouse 6 is 413663, mouse 4 is 411771), the QC and sessions 1 to 3 filter, `calculate_snr` and the correlation rolling window all match what the file says. The file has no statistics entries, which is right: the paper says it runs no statistical tests.

**Changes, by claim**
- **session-schedule:** Session dates are now taken as local dates, as in Table 2. In the paper's own session table, some start times stored in UTC fall on the next day (418779, 412933), which could shift the spans. How the 70-minute duration is measured was a hidden choice, so it is now open with two readings: first to last two-photon frame, or first to last stimulus in the stimulus table.
- **fig5-stimulus-responses:** Added a note that the criterion only judges the consistent versus inconsistent difference. The "increased fluorescence at onset" part of the statement is tested by fig9-onset-offset-transients.
- **fig7b-signal-stable:** Added the missing "not reproduced" outcome, and the reporting of medians and quartiles to match fig7a.
- **high-correlation-pairs:** Dropped "Only" from the statement, because the paper gives the 0.01% as an example without that emphasis.

**Still open (recorded in `checks`)**
- **QC failures:** The text says two mice had failed sessions, but Table 2 shows three. table2-sessions names both readings.
- **Tracked-ROI percentages:** The paper never defines the "theoretical maximum" behind the 32 to 75% figure.
- **Tests not in the paper:** The paper gives no test for fig5, fig7a, fig7b, fig7c or fig9, so their criteria rely on named readings.
- **ROI matching:** The Fig. 8 conflict counts and the variation across session orders can only be tested with the paper's modified matching code, which is not public.
- **Stimulus design:** The Gabor and visual flow parameters have no claim. They describe methods, not findings, so I did not add one.
- **Which dandiset:** All findings are marked as tested on DANDI:000037. The opening comment says dandiset 000336 is a different project, based on the archive's description; I did not check that against the data. The link claim leaves the question to the author.

**Ready:** yes (`ready: true`). Only the claims file is modified, and nothing is committed.
