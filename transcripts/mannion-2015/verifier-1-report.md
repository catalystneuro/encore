**A. Outcomes**

The claims file has 16 claims. The notebook tests one and treats 15 as blocked.

| Claim | My outcome | Reason |
|---|---|---|
| localiser-masks-ventral-dorsal | blocked (data_missing) | The criterion needs cortical surfaces and V1–V3 definitions. The archive has only `crcns_vim-3.tar.gz` plus docs (filelist.txt), and descriptor line 17 says area definitions and anatomicals are not included. Cell 9's volume S-I check is a proxy, not the criterion. |
| presentation-source-interaction | blocked (data_missing) | No V1–V3 definitions. Cell 15's whole-slab volume variant (interaction p = 0.137) is correctly kept out of the outcome. |
| interaction-not-area-dependent | blocked (data_missing) | Needs the area factor, which needs V1–V3 definitions. |
| lower-field-below-greater | blocked (data_missing) | Needs V1–V3. |
| upper-field-no-source-difference | blocked (data_missing) | Needs V1–V3. |
| fig4-top-five-matching-source | blocked (data_missing) | The ranking needs V1–V3 responses. The volume variant's 4/5 count is not the criterion. |
| fig4-qualitative-content | blocked (data_missing) | It depends on the ten pairs from the blocked ranking. |
| fig5a-mean-luminance | blocked (data_missing) | Needs the V1–V3 difference term. A calibration substitute would not unblock it. |
| fig5-no-other-pixel-relations | blocked (data_missing) | Same reason as fig5a. |
| fig5bc-spatial-frequency | blocked (data_missing) | Same reason as fig5a. |
| fig5def-orientation | blocked (data_missing) | Same reason as fig5a. |
| fig5-no-other-filter-relations | blocked (data_missing) | Same reason as fig5a. |
| no-radial-bias-in-patches | blocked (metadata_insufficient), partly testable | It needs no responses, only the 120 screenshots, which are in the archive (cell 5). The only thing missing is the monitor's CIE coordinates, and the claims file leaves the choice of a substitute to the author. The luminance-only variant (4 tests, 45° against 135°) could have been run under a stated calibration, but it was not. |
| figs2-task-no-condition-difference | reproduced | Cell 12, criterion window 0.4–0.9 s: reading (a) gives presentation p = 0.158, source p = 0.979, interaction p = 0.529; reading (b) gives 0.987, 0.947, 0.347. No effect reaches p < 0.05 under either reading the claims file requires. I checked `rm_anova_2x2` against statsmodels AnovaRM on synthetic data and it matches exactly. |
| figs3-residual-no-condition-difference | blocked (data_missing) | The residuals are defined in V1–V3. |
| figs3-residual-upper-larger | blocked (data_missing) | Same reason. |

The paper states no chance level for any selection. I found no place where the claims file misreads the paper.

**B. Problems**

1. [affects a conclusion] Summary in cells 0 and 16, no-radial-bias-in-patches. The notebook labels it "blocked: data missing", but the summary text itself says only 14 claims need V1–V3. This claim needs only the screenshots, which are present, plus a calibration. The reason should be metadata_insufficient, and the luminance-channel variant (with a stated assumed monitor) was left untried. The claims file explicitly gave the author this choice (author, step 4), and the notebook does not argue against a substitute beyond cell 6.
2. [does not affect a conclusion] `task_performance`. A target is assigned only when an event onset falls strictly between 0 and 2 s after its bin. Digits arrive at multiples of 1/3 s, so every target on an even second lands exactly on an event onset and is dropped. That is about 1/6 of targets: 918 unassigned in reading (b), 1023 in (a). The loss is the same for all conditions. Whether task.py has the same strict inequalities is not shown.
3. [does not affect a conclusion] `task_performance`, assignment direction. A target goes to the event starting 0–2 s after it. The helper attributes this to task.py; the claims file criterion does not specify it, and the legend says only "near to". No reading assigns to the event in progress, which starts up to 2 s before the target. Three timing readings, (a), (b) and (c), are all null, so this is unlikely to change the outcome.
4. [does not affect a conclusion] Cell 13, author-added windows. Under reading (a), the 0.6–0.9 s window gives presentation p = 0.034. The criterion's window is null, so the outcome stands, but the null depends somewhat on the window, and the notebook prints this number without comment.
5. [does not affect a conclusion] Readings (a) and (b) put every press and target after 300 s into the last bin, as task.py does; the totals show about 590 targets lost this way. Variant (c) covers this and is also null.
6. [does not affect a conclusion] `stream_participants` and cell 3 never list every member of the tar archive. Members outside `data/<pid>/` and `stim/` are skipped silently, so the absence of ROI, surface or anatomical files rests on the descriptor, not on the stream.
7. [does not affect a conclusion] Cell 6. The R≠G≠B count covers the whole screen, overlays included, so it does not show that the patches themselves are in colour. The conclusion that calibration is needed rests on the paper, not on this check.
8. [does not affect a conclusion] The volume variant (cells 7–15) is unaligned, not motion-corrected and fitted by OLS, and p1011's run order and clock are unconfirmed. The notebook labels it correctly and no outcome rests on it.

**C. What I could not check**

- task.py itself. The p1004 rule's polarity coding (1 = white), the `>` against `>=` bin edges, the 0–2 s assignment direction, and "any key counts as a response" all depend on it. A cell quoting the relevant task.py lines, or running task.py's own function on one participant next to `task_performance`, would settle these.
- Whether the tar holds anything beyond what is parsed. A cell printing all member paths, or at least the path prefixes and their counts, would confirm this from the data and not from the descriptor alone.
- The radial-bias claim. A cell computing the 12 (or the 4 luminance) paired t-tests under an explicit calibration would have tested it, ideally with a second calibration to show sensitivity, plus a crop of each patch location to confirm the patch geometry.
- Per-condition target counts. Only totals are printed; a breakdown by participant and condition would show whether any condition is under-sampled.
