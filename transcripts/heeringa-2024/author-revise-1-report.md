All 23 outcomes stay as they were. The verifier agreed with every one and found no place where the claims file misreads the paper, so I added nothing to `questions/001262.yaml`. The entry re-ran cleanly with `python tools/entry.py all` (check: 0 errors, notebook passes in about 5.5 min), and every conclusion in the notebook and the record matches the new numbers.

**What I added or corrected, point by point:**
- **B1, recording-type-counts (CLICK count of 271 or 275 against the paper's 261):** a new cell checks the assumed 7.75 ms click delay against the data.
  - The population response to clicks is flat until 8.25 ms. It rises from 8.25 ms in the 20 ms trials and from 8.75 ms in the 10 ms trials, whose units have lower best frequencies.
  - Latencies from both trial lengths fall on one latency-to-best-frequency line (median residuals −0.032 and −0.027 ms).
  - `click_polarity` is "COND" in every CLICK trial, so it carries no information.
  - Nothing suggests that a 500-trial recording joins two recordings: its two halves agree in latency about as closely as odd and even trials do.
  - The CLICK mismatch does not depend on the delay. Reading 2 (275) uses no latency, and reading 1 gives 270 to 272 for every delay from 5 to 8.25 ms. The outcome stays partially reproduced.
- **B4, isi-exclusion:** I added the histogram of intervals below 0.6 ms in 0.02 ms bins, and checked the voltage trace around every short-interval spike pair.
  - Both spike times lie on a single waveform for all pairs below 0.1 ms, 91% of pairs from 0.1 to 0.3 ms and 39% from 0.3 to 0.6 ms. None of 300 reference pairs at 0.8 to 1.5 ms do.
  - So many short intervals are one spike detected twice. Counting only separate waveforms, 176 units still fail, so the outcome stays not reproduced. I updated the finding.
- **B2, CF level source:** I added the variant that takes stimulus levels from the calibrated level column. It gives the same CF for all 119 units.
- **B3, fig6a:** the notebook now shows that the two sensitive regions are also the two lowest bin means overall, so the choice of regions does not assume the answer.
- **B6, fig6c:** the last histogram bin no longer counts as a mode. The result is unchanged.
- **B7, fig6d:** the main reading now follows the Methods (p-value is NaN when N < 50), because the protocol puts the Methods before the code. The code's N ≤ 50 rule is shown as a variant. Only one level has exactly 50 spikes, and no unit's result changes.
- **Section C requests:**
  - The notebook now prints the analysis-table columns: only `experiment`, `id`, `results_bf`, `results_sr` and `results_threshold`, in every file.
  - It now prints the fig6b bin counts for middle-aged units, old units, all ages, and young units with CF added. The named 2.5 to 3.0 kHz bin is the emptiest only among middle-aged units (0 units). The paper's text names young adults, so the outcome stays not reproduced and the notes record this.
- **B5 and B8:** no change needed. The ABR threshold is already marked as an assumption, and the fig7ab tests come from the claims file.
- **Record and README:** I recorded the round under `verifications` in `attempts/001262-heeringa-2024-01.yaml`, with the verifier's reasons and my responses. I updated the notes, deviations and findings, and the README's description.

**What I did not do:**
- I could not establish the click delay from the voltage traces: averaging them showed no click artefact. The question to the paper's author stays open; it now says the data are consistent with 7.75 ms but do not fix it.
- I did not compare the plots with the paper's figures as images.
- I did not commit.
- The changes to `tools/build_site.py` and `tools/site_assets/` were there before this run, and I left them alone.
