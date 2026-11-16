I've finished steps 1 to 5 and the handover (step 6). The entry is `entries/hazon-2022/` (two notebooks plus the helper `hc30.py`) and the record is `attempts/hazon-2022-01.yaml`. `entry.py check` and `all` passed, `handover` built `executed/hazon-2022/handover/`, and nothing was committed.

**(1) Outcomes**

| Claim | Outcome |
|---|---|
| data-sessions-and-neurons | reproduced |
| single-cell-variability | reproduced (0.7263 +/- 0.6117, exactly the paper's numbers) |
| suppl-table1-place-field-properties | not reproduced (2 of 7 values match) |
| fig1d-noise-correlation-by-field-distance | reproduced |
| noise-correlation-not-physical-distance | blocked, data_missing (no cell positions) |
| position-measurement-noise | reproduced (mean 0.277 cm, range 0.118 to 1.001) |
| fig3cd-signal-and-noise-growth | reproduced |
| suppl10-asymptotic-snr-lower-with-correlations | reproduced |
| fig3f-signal-slope-beginning-vs-end | partially reproduced, assumed (the effect runs the way the code tests, opposite to the legend) |
| fig3g-noise-slope-decreases-over-run | reproduced |
| fig3h-snr-higher-at-run-end | reproduced |
| fig4a-snr-along-noise-pcs-peaks-at-6 | partially reproduced (peak at the 7th component) |
| fig4b-correlations-increase-noise-signal-overlap | reproduced |
| fig4c-overlap-predicts-asymptotic-snr | reproduced (r = -0.743, p = 0.0139) |
| fig5f-pf-width-variance-vs-nsv | reproduced (r = -0.658, p = 0.0385) |
| fig5hi-nsv-predicts-noise-correlation-effect | reproduced |
| suppl-table2-nsv-best-predictor | reproduced |
| pf-width-variance-not-predictive | not reproduced (p = 0.041 on 73 sessions) |
| fig5cd-synthetic-narrow-widths-broader-nsv | reproduced, assumed (legend's width distributions) |
| fig2d-rms-error-ensemble-vs-shuffled | reproduced, assumed (SVM C = 1); 9.36 vs 4.80 cm |
| fig2cd-shuffle-better-in-all-bins | reproduced |
| fig2ef-imse-saturates-with-correlations | reproduced |
| suppl7b-initial-slope-lower-with-correlations | reproduced |
| saturation-ensemble-size | not reproduced |
| suppl11b-i0-vs-single-cell-snr | not reproduced |
| suppl11c-asymptotic-imse-vs-asymptotic-snr | reproduced (log-scale reading) |
| suppl8-task-performance-and-accuracy | not reproduced |
| suppl6-twenty-bins-near-optimal | reproduced |
| suppl9-fit-recovers-saturation | reproduced (simulation) |

**(2) What was found about the dataset**
- **Contents and version:** one MATLAB file (142 MB, MD5 matches `checksums.md5`) holding only the 110 working sessions. It holds event onsets, not the convolved trace the paper decodes, and has no cell positions, frame times, spatial scale or reward record. The version is pinned as `unversioned` because CRCNS has only one published version, and the notebook header records the MD5.
- **Misaligned sessions:** in six sessions the event trace does not track position at lag 0.
  - Two (Mouse2012 141832, Mouse2011 142436) line up at a lag of 80 to 90 frames.
  - Two (Mouse2011 105556 and 104511) line up at no lag within 200 frames.
- **Positions off the track:** four sessions have position values far off the track, down to -3.7e7 pixels.
- **Joined sessions:** two session IDs join two recordings; one of them has 6 times the usual event rate.
- **Session length:** sessions last about 30 min at 20 Hz, where the paper and the descriptor say about 20.
- **Paper inconsistencies:**
  - The Fig. 3f legend says the signal slope decreases over the run, but the code tests (and the data show) an increase.
  - The width distributions in the Fig. 5 legend and in the Methods give opposite simulation results.
- **Assumptions:** SVM C = 1 with voting (C = 0.1 and 10 change the median error by less than 0.4 cm), the code's test direction for Fig. 3f, and the legend's widths for Fig. 5a to 5d.
- **Questions for the paper's authors** (recorded as a `methods_unavailable` finding): the Fig. 3f direction, the width distributions, the decoder regularisation, and how the Supplementary Table 1 values were computed.
- **Questions to a reader:** none.

**(3) Where the protocol was unclear or missing something**
1. archives.md covers zip files; hc-30 is a plain `.mat`. I streamed it whole into memory with fsspec.
2. The protocol does not say what to do with sessions that fail the clock check when the paper's own selection includes them. I kept them and showed variants without them.
3. It is unclear whether a variant the author adds (dropping degenerate fits or misaligned sessions) may decide an outcome when the criterion does not list it. I let only the criterion's readings decide and reported the variants in the notes.
4. For the absence claim, "the paper's test as written" was ambiguous: the table header says 73 sessions, but its notes add a filter. I followed the criterion's 73 sessions.
5. The fig3f criterion says an outcome that holds only in the code's direction "rests on that reading" but names no outcome label. I chose partially_reproduced with `assumed: true`.
6. The protocol describes a single notebook. I split the work into two for time, each with its own header and summary.
7. Conclusions can only be written after seeing the outputs, but any edit forces a full re-run. For a 50-minute entry that doubled the compute. Three variant numbers that appeared only in the second run are in the record's notes but not in the notebook's conclusions.
8. There is no rule for using fewer repetitions than the paper instead of blocking as `too_large`. I used fewer and recorded each as a deviation:
   - signal and noise: 20 subsets instead of 80;
   - decoding: 10 full-ensemble repetitions and 4 subsets per size, in steps of 25, instead of 80 in steps of 10;
   - bin-count variant: 2 repetitions per bin count.
9. `check` requires the version string to appear in the code, so I added `VERSION = "unversioned"` to the helper.
10. It is unclear whether the paper's code, read only for method details, is an `input`. I listed it.

**(4) Runtime and failures**
- About 3 h 05 min wall time.
- The notebooks take 8 min and 42 min in the clean environment. Each was run twice; the results matched apart from the added variant cells.
- The IMSE fits are often degenerate: 7 unshuffled and 78 shuffled fits give N below 0 or above 1e6. This is the likeliest cause of the three failed claims built on I0 and N (saturation range, I0 against single-cell SNR, performance and accuracy).
- Nothing failed to run.
- Untracked `.bashrc`/dotfiles and a `scripts` device node at the repo root are sandbox artefacts I did not create or touch.
