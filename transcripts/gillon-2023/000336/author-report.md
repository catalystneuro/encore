I've finished steps 1 to 5 for DANDI:000336 and run the handover (step 6). The target dandiset does not hold the paper's data: 000336 is a different OpenScope project, "Dendritic Coupling". As the claims file directs, every other claim was tested on DANDI:000037 version 0.230426.0054, where the paper deposited its 50 sessions. `entry.py check` gives 0 errors, both notebooks pass `all`, and the handover package is in `executed/000336-gillon-2023/handover/`. Nothing is committed.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| dataset-holds-paper-sessions | not reproduced: 000336 holds none of the 13 subjects or 50 sessions |
| table1-subjects | reproduced |
| table2-sessions | reproduced |
| session-schedule | reproduced, only when the span counts calendar days inclusive |
| imaging-planes | partially reproduced: mouse 433414 is at 60 µm in the files, 75 µm in Table 2 |
| roi-counts-per-session | reproduced |
| tracked-rois-per-plane | reproduced (254/261/516/129; 32.9–75.0% under one definition of the maximum) |
| fig8-example-matches | reproduced (136 and 47) |
| fig8-ordering-variation | reproduced, resting on an assumption (`assumed: true`) |
| stimulus-durations | reproduced |
| inconsistent-event-fraction | reproduced (6.93%, 4.65%, about 31.5 blocks per stimulus) |
| fig5-stimulus-responses | reproduced under all reading pairs |
| fig6-behaviour | reproduced |
| fig7a-snr-high-stable, fig7b-signal-stable | reproduced |
| fig7c-correlations-similar | blocked, `methods_underspecified`: one reading holds in 6 of 6 comparisons, the other in 5 of 6 |
| high-correlation-pairs | not reproduced: 0.0178% of pairs, against 0.01 ± 0.005% |
| fig9-onset-offset-transients | reproduced in all 12 groups |

**2. Dataset findings, assumptions and questions**

Findings:
- 000336 lists the paper as a resource it describes, but holds mesoscope recordings of 16 other mice from 2022–23.
- In 000037, every `session_start_time` is the UTC time with a Pacific offset attached, so it is 7 or 8 hours late. Read as stored, 4 of 50 dates differ from Table 2.
- The three sessions of 433414 give 60 µm; Table 2 and the paper's code table give 75 µm.
- The files have no QC status, no session number and no field of view. QC and session numbers came from the paper's code table (`mouse_df.csv` at commit 046e7fe), listed under `inputs`.
- One failed-QC session (759872185) has 61,134 pupil samples for 127,588 imaging frames.
- I found no duplicated recordings, and the trial-table clock agrees with the imaging timestamps to within about one frame.

Assumption: for the ordering claim, I read the paper's dendritic "overlap of 10–20%" as intersection over union, and used the max projection in place of the average projection the matching package expects. With that reading the dendritic match counts are well below the files' tracked counts, so it is probably stricter than the paper's.

Two questions for the paper's authors are recorded as `methods_unavailable` findings:
- What measure of similarity does Fig. 7c rest on?
- What overlap measure and threshold did the modified matching use, and can that code be published?

I asked a reader nothing.

**3. Where the protocol was unclear**

1. The claims file's criterion for fig7c says to block when its readings disagree, while Author step 1.6 allows adopting the best-supported reading as an assumption. I followed the criterion and blocked. The notes say that the reading closest to the paper's argument (the upper tail of highly correlated pairs) holds in all six comparisons.
2. When the target dandiset holds no data and every claim is `elsewhere`, the protocol does not say how to record it. I recorded `dataset` as 000336 at its only published version, listed 000037 under `inputs` and in `related`, and explained both versions in the notebook header.
3. Several statements are about design durations, while the files give measured times. I judged the stimulus durations on the Methods' sampling grid (1.5 s and 1 s steps) and recorded this as a deviation; measured runs exceed the stated ranges by up to 0.22 s.
4. The 30-minute notebook limit and the "aim for 10" target don't fit the matching rerun. I put it in a second notebook (about 19 minutes), cut the work threefold by reusing each pairwise match across orderings, and checked on two mice that this gives the same counts as full runs.
5. The matching package reads its images from file paths, so it writes temporary PNG files to disk. I took this as allowed, since these are derived images, not downloaded data.

**4. Runtime and failures**

The run took about 2 h 10 min (02:19 to about 04:29 UTC). The main notebook takes about 10 minutes and the matching notebook about 18.

One full run of the matching notebook failed: parallel processes were overwriting each other's temporary mask files. I gave each process its own directory and the re-run passed.

Some files I did not create (`.bashrc`, `.mcp.json`, `scripts`, `.idea` and similar) show as untracked in the repository root. They appear to be left by the sandbox and are dated before the run started. I left them alone; make sure the workflow does not commit them.
