I've worked through all 12 points in the verifier's report and re-run the entry. `python tools/entry.py all` passed in 1537 s and `check` reports 0 errors. I read the executed copy, and every conclusion matches its numbers. The round is recorded under `verifications` in `attempts/crcns-hc-28-jadhav-2016-01.yaml`. Nothing is committed.

**Outcome changes**

| Claim | Round 1 | Now | Why |
|---|---|---|---|
| fig3f-swr-cross-covariance-lag | partially | not reproduced | Agreed with the verifier: the inhibited extremum sits at the 200 ms window edge, so no trough is found |
| figs3-arm-and-direction-selectivity | partially | not reproduced | Agreed: part of the criterion fails |
| fig6e-theta-trained-glm | partially | not reproduced | Agreed: the interaction test the criterion names gives p = 0.49 |
| fig8d-glm-epoch-specific | partially | not reproduced | Agreed: pre-rest to pre-rest does not exceed pre-rest to task (p = 0.49) |
| fig4-theta-locked-fraction | partially | reproduced | 91 of 167 (0.545) now, inside the tolerance by 0.005, after the theta-phase fix |
| figs5-matched-selectivity | not reproduced | reproduced | After the rate-map fix the excited relation is r = 0.379, p = 0.047. The notes call it fragile: p is just under 0.05 and the matching range comes from 7 cells |
| figs6-replay-content | blocked | not reproduced | Now run: 206 of 685 events are significant, and modulated cells (8) do not exceed unmodulated (33), p = 0.45 |

New totals: 9 reproduced, 7 partially reproduced, 21 not reproduced, 2 blocked.

I kept fig4a-preferred-phases as not reproduced and recorded the disagreement. The verifier left the PFC part undecided because of a binning artifact. With the artifact removed, the PFC modal bin is 45–90° or 90–135° under every reading, never the bin with 180°.

**Fixes and added output**
- **Phase binning:** preferred phases now use 15° histogram bins, with 45° bins and circular means as readings. The phase-concentration claim adds circular-mean tests, which have no ties.
- **Rate maps:** wtr2 runs now get their own bins, since wtr2 is a different track. A wtr1-only coverage variant is added.
- **Theta phase:** a spike's phase is now interpolated between the 150 Hz samples. theta-lag-past now gives −15 ms under reading (b).
- **Position scale:** the files carry `cmperpixel` (the description says `cmperpix`), and the track geometry shows positions are already in cm. This is added to the findings.
- **SWR detection checks:** the CA1 rate gain after SWR onset is printed per reading: 1.36 for the any-tetrode reading, 1.64 for the mean envelope, against 0.90 at random slow times. Events per tetrode show the any-tetrode reading finds 2.7 to 4.1 times the events of the busiest single tetrode.
- **Classification checks:** Table S2 per-animal counts are printed beside ours, and every animal has fewer modulated cells. The test flags 0.066 of PFC cells when SWR onsets are shifted by 10 s (nominal 0.05).
- **New section:** cells are classified again under the mean-envelope reading (17 excited, 3 inhibited of 136) and without wtr2 (11 and 6 of 161), and the downstream tests are repeated. No failing claim meets its criterion under either. fig6ab, fig6c and fig6e weaken under the mean envelope, so their notes say the outcomes rest on the main reading.
- **Smaller points:** the fig6e-theta cell now prints group sizes, showing why groups (a) and (b) give identical results. The summary now says the PFC group failures follow from the small groups. The record's findings, the README counts and the helper docstrings are updated.

**Not done**
- The movement-trained GLM, figs4c, figs5, fig8bc and fig8d are not repeated under the alternative readings. The notebook says so.
- The overlap of neighbouring SWR rasters in fig3f is unchanged. The verifier marked it as not affecting a conclusion.
- No reader questions were added, since the verifier found no misreading in the claims file.
