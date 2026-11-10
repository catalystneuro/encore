**Verifier report, round 2: Mehrotra, Levenstein et al. 2024 (attempt mehrotra-2024-01)**

The claims file has 22 claims and the attempt record has 22 outcomes: 9 reproduced, 5 not reproduced and 8 blocked. Seven outcomes are marked `assumed: true`: fig5f, fig5c, fig1g, fig1b, figs2e, fig1k and fig5e.

**1. Outcomes**

| Claim | Record | Agree? | Assumption |
|---|---|---|---|
| rsc-dataset | not_reproduced | yes | – |
| fig5f-rsc-pmr-onset | reproduced, assumed | yes | All units enter (reading a). Stated, and supported by exactly 570 units entering. |
| fig5c-posub-pmr-onset | reproduced, assumed | yes | The states of A3708-200317b are re-detected. Stated, and reasonable: the file fails the clock check against every session (posub cell 8). |
| fig5d-isomap-pmr | reproduced | yes | – |
| fig1e-delay-range | reproduced | yes | – |
| fig1g-dv-sequence-du | reproduced, assumed | yes | The A3708 replacement. Stated and called fragile. |
| fig1h-ventral-down-longer | reproduced | yes | – |
| fig1b-no-dv-tuning-gradient | reproduced, assumed | **no**: not_reproduced | See below. |
| figs1j-dorsal-ventral-same-hd | reproduced | yes | – |
| figs1i-du-more-stable | blocked (methods_underspecified) | yes | – |
| figs1kl-not-firing-rate | blocked (methods_underspecified) | yes | – |
| fig2f-gamma-travels | not_reproduced | **yes (changed from round 1)** | See below. |
| figs2d-lfp-spike-agree | blocked (methods_underspecified) | yes | – |
| figs2e-speed-similar | not_reproduced, assumed | yes | Speed is the slope of depth on delay. Stated, and reasonable: it gives the paper's unit speeds. |
| fig1j-down-resets-hd | not_reproduced | yes | See below. |
| fig1k-hd-stable-at-onset | not_reproduced, assumed | yes | Steps below the radius threshold are left out. Stated and decisive (kept, p = 0.040). Reasonable given the Methods wording ("threshold for computing angular direction"). |
| figs2g-adn-synchronous | blocked (metadata_insufficient) | yes | – |
| fig5e-fc-pmr-onset | reproduced, assumed | yes | UPInts stand in for SlowWaves, all 27 sessions are used, and the dated sessions are taken as one rat. All stated and reasonable. ONInts give −0.162, outside tolerance, so the first assumption decides. |
| fig3-other-gradients-fail, fig3f-ih-gradient | blocked (not_runnable) | yes | – |
| fig4d-sag-gradient, figs4-no-other-gradients | blocked (data_missing) | yes | – |

- **fig1b: I still disagree.**
  - The criterion fixes "the measures as the Methods define them". The printed formula gives bits per second, and under it the claim fails (tau = 0.082, p = 5.1e-5, posub cell 34).
  - The bits-per-spike assumption is stated and plausible. Its p = 0.099 and |tau| = 0.034 sit close to the paper's −0.03 and p = 0.13.
  - The claims file does not name the unit as open. This is a gap in the claims file, and the author has correctly sent it to a reader as a question.
- **fig1b: new point, direction of the depth axis.** The record leaves this assumption unstated.
  - In the paper, the three non-significant measures are negative (S1 legend: speed −0.03, AHV −0.02; HD information −0.03). The two significant ones are positive (resultant vector length +0.063, peak rate +0.075).
  - In the notebook all five are positive with dorsal as positive.
  - So no single axis direction matches all five of the paper's signs. The "positively correlated" part of the criterion rests on reading the paper's axis as dorsal-positive.
  - Posub cell 33 says "the opposite direction is reported too", but it is not printed.
- **fig2f: I now agree with not_reproduced.** Every reading fails the criterion, so the readings agree on the outcome and "blocked when the readings disagree" does not apply. The DU-aligned readings fail because UD also depends on position (W = 0, p = 2.4e-4). The delta-peak readings fail on DU (p ≥ 0.27).
- **fig1j: agree, as the criterion's test.**
  - One of 20 bins lies outside the shuffle range. It is a deficit at −0.47 rad, not an excess at zero difference.
  - The test's own chance rate is 3.5%, and the effect is null in size (resultant length 0.020 against a shuffle 99th percentile of 0.078).
  - The outcome hangs on one bin of a subsampled ring (see 2 and 3).

**2. Text against printed outputs**

- **Ring cell 10, fig1k "Result":** "lower … in 10 of 16 sessions (median 0.378 against 0.439 per s)", "U = 99, p = 0.28", "in 8 of 14 (p = 0.54)" and "Keeping the steps below the threshold gives the paper's result (14 of 16, U = 69, p = 0.027)".
  - Ring cell 9 prints a traveling median of 0.373, U = 98.0, p = 0.266 and, for the 14 sessions, U = 83, p = 0.505. With the steps kept it prints U = 73, p = 0.040.
  - The same stale values appear in the ring Summary (cell 11, "U = 99, p = 0.28") and the main Summary (cell 23, "p = 0.28").
  - In the attempt record they appear in the fig1k notes and deviations, the Figure 1K finding ("p = 0.28 … p = 0.027") and the verification response ("U = 99, p = 0.28; keeping them gives p = 0.027").
  - The outcomes do not change. But it shows the ring results differ between runs, or the text was not updated after the re-run.
- **Main cell 20, fig5e:** "All 27 archives were read in 691 s." Cell 17 prints "loaded 27 sessions in 831 s". The fig5e notes ("in 691 s in the final run") and the verification response repeat 691 s.
- **Posub cell 35 and the record's fig1b deviation:** both quote "HD information exceeding 0.2 bits/spike". The paper reads "0.2 bins/spike" (Methods, Isomap Projection and Decoding). The misquote is presented as the paper's words.
- **Posub cell 35, the record's fig1b notes and its verification response:** "Figure 1B … its axis of log10(HD info) runs from −2 to 1 with most cells near 0".
  - The paper text supplied has no axis labels, and the claims file says the figures were not read. I could not render the PDF here.
  - The claim is unsupported by the materials, and the fig1b outcome partly leans on it.
- **Posub cell 39 (Summary):** "The DOWN starts of the 15 other event files agree with those re-detected … to within 2.5 to 17.5 ms." That range is only the cross-correlogram peak lag. In A3701, A3710 and A3716 only 423 to 769 file states match within 10 ms (cell 7). The wording overstates the agreement.
- **Main cell 15:** "between −0.26 and −0.24" for the threshold variants. The printed values run from −0.238 to −0.259. This is a rounding slip only.
- **Everything else checks out.** All other "Result" sentences, the Summaries, the README and the record's notes match the printed outputs. Specifically: fig5c, fig5d, fig1e, fig1g, fig1h, figs1i, figs1kl, figs1j, fig2f, figs2d and figs2e; fig1j's 0.020, 0.078, 3.5%, 291 (309 to 423), 434 (381 to 510) and 0.032; and fig5e's tau and counts.
- **My round-1 reasons** in `verifications` are faithful to round 1 in substance and attribution. They are mostly close paraphrases of my wording, with my problem numbers attached to the right claims.

**3. Round-1 points**

Resolved:
- **1** (the odd/even PETH): fixed, and all 16 sessions now enter. The outcome is unchanged.
- **2** (the LFP clock): starting_time and rate are printed, the three sessions are left out of the main reading, and all 16 are run as a variant.
- **3** (A3708 fragility): now reported as fragile, and A3708's identity is confirmed.
- **4** (event-file alignment): per-session cross-correlograms show no offset of tens of ms.
- **6** (the depth convention): "Channels sorted top to bottom of shank" and electrode 0 has the largest rel_y in 16 of 16 sessions. Figure S1A ("top channels corresponded to the dorsal edge") agrees.
- **9, 10 and 11:** noted, printed and fixed respectively.
- **12, and the fig5e time limit:** fig5e was run, and the deviation is recorded.
- **fig1j and fig1k:** both now tested.

What remains and bears on a conclusion:
- **fig1b.** The unit of HD information (bits per second or per spike) is still disputed; it needs a reader's ruling on the claims file. The new point is the axis direction of Figures 1B and S1D to S1F, which no single convention fits for all five signs. The Figure 1B axis-range evidence needs the figure to be checked.
- **fig1k and fig1j: reproducibility of the ring.** The conclusion figures do not match the re-run. Isomap's ARPACK solver is not seeded, and the wake bins and UP states are subsampled. The fig1j outcome turns on a single bin, and a re-run could flip it.
  - To settle it: two executions with identical printed output, or fig1j and fig1k over several seeds.
- **fig1g, and through A3708 fig5c.** Both still rest on the re-detected A3708 states. This is stated and does not need to change.
  - An optional check: A3708's LFP shows no gamma rise even after the spike-re-detected DU states (1.045 against 1.048 shifted, lfp cell 3). Testing the A3708 event file against the A3708 LFP would show which of the spikes or the event file is off-clock.
- **Corrections without an outcome change.** The text in section 2 needs fixing: the fig1k numbers, the 691 s, the "bits/spike" quotation and the agreement wording in the posub Summary.
