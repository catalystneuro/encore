I worked through the round-1 report, changed two outcomes, re-ran the entry with `python tools/entry.py all entries/crcns-alm-1-li-2015`, and updated the record. The run passed in 324 s with 0 check errors. Nothing is committed.

**Outcome changes**
- **antidromic-latency-jitter: reproduced → partially_reproduced (still marked as assumed).** The verifier was right that the window decided the match. I counted, per neuron, how many spikes the spontaneous firing would put near each neuron's usual response latency. Between 0.5 and 1 ms from it, IT neurons have 783 spikes against 69.7 expected from spontaneous firing. So the ±0.5 ms window I had used cuts off real responses, and I switched to ±1 ms. PT values and the PT-before-IT order still hold. IT jitter is 0.310 ms against 0.2 ± 0.05, and the tagged mean is 0.184 ms against 0.15. A robust s.d. gives 0.289 ms for IT.
- **reaction-time: not_reproduced → blocked, `methods_underspecified`.** I added a second detector (the first sustained move away from the pre-cue baseline by 3, 5 or 10 times its noise). I also added example traces for every mouse with onsets marked, per-mouse histograms and a pre-cue false-trigger check. At 3 times the noise the mean across mice is 65.0 ms, within 61.1 ± 10.5. At 5 and 10 times it is 77.7 to 103.7 ms, outside. The paper gives no basis for picking a threshold. The spread across mice is 21 to 36 ms, against the paper's 10.5.

**Disagreements I kept**
For ed1-fast-spiking-properties and contra-ipsi-selectivity-forms the verifier gives not_reproduced. I kept partially_reproduced and recorded the disagreement. In each claim one part holds under every reading and the other fails, which fits the protocol's "holds only in part".

**Other additions and corrections**
- **Spike widths (B3):** the waveform arrays are read the right way round, and the cellType labels split the deposited widths cleanly. The FS boundary in the labels falls between 0.256 and 0.307 ms (5 and 6 samples), not at the stated 0.35 ms. unit-counts stays partially_reproduced.
- **Lick early trials kept and 1.5 s response epoch (B2):** fig3f-late, ed2, fig2e, ed1 and contra-ipsi now run under all four readings of the shared methods, and no outcome moves. For fig3f-late, all task-selective neurons give P = 0.022 to 0.024 under every reading, and none of 32 combinations matches the paper's pattern.
- **Counts versus rates (B5):** a t-test on spike counts gives 912 again under the main readings.
- **MATLAB scripts:** the notebook now streams and prints the cited lines, so those citations can be checked. They confirm the "stable trials" span, the trial thresholds, the test on rates and the performance formula.
- **NaN-type trials (B6, B8):** task-performance's second reading now leaves them out. A new table breaks the NaN-type light trials down by mouse and session, and a new finding records their undocumented settings. ed7 stays blocked: the only sample-epoch PT candidate is one mouse with 3 sessions, and ED Fig. 7 used two mice and eight sessions.
- The notes, conclusions, summary, README and the round-1 `verifications` block now match the new numbers.

**Not done**
- I did not re-run the two Fig. 2c time-course claims under the other shared-method readings, since the verifier judged a flip unlikely.
- I did not re-derive the collision test (B7); it needs about 750 GB of raw traces.
- The fixed 1 V lick count (B9) is now described as a clock check only.
- Nothing went into `questions/crcns-alm-1.yaml`, because the verifier reported no place where the claims file misreads the paper.
