**Verifier report, round 2: Russo et al. 2025 on DANDI:000458 (0.230317.0039)**

Counts are from the files. The claims file has 39 claims. The attempt record has 39 outcomes: 20 reproduced, 5 partially reproduced, 7 not reproduced and 7 blocked. Its verification block has 39 results. The claims file has an explicit "partially reproduced" clause for only some claims: source-data-link, figs4, triphasic, fig3b and figs13. I found no new misreading of the paper in the claims file.

### 1. Outcomes and assumptions

I agree with the outcomes for 33 claims: the 5 human claims, fig5a, fig1c, fig1d, fig1e, figs1b, figs4, figs5, figs6, triphasic, fig2b, figs7a, figs7b, fig3a, figs9, fig3b, figs11d, figs12, the three fig3e claims, figs13, figs13d, discussion, figs8b, fig2h, and the 5 model claims. Notes on some of them:
- **fig3a:** "Reproduced" follows the criterion, which accepts reading (c). The record now says plainly that the session-stratified test gives p = 0.19 (cell 48).
- **figs5:** This passes only because CSD gives p = 0.048 under reading (b). The record says so.
- **Model claims:** Blocked as `not_runnable` is reasonable, since the re-executed timing in cell 101 shows the runs take longer than the 1 h limit.

I disagree with three, because of how "partially reproduced" is used. In round 1 I rejected "partially reproduced" for fig3e-lf because its criterion has no partial clause, and the author accepted that. These three criteria have no partial clause either, so the same rule applies:
- **speed-threshold-robust → not reproduced.** LFP fails at 5 cm/s and CSD fails from 0.5 cm/s (cell 27), and the criterion needs all three signals at every threshold. I accepted "partial" here in round 1, which was inconsistent with my fig3e-lf ruling.
- **fig2fg → not reproduced.** The criterion needs all six signed-rank tests to pass. SM-TH Opto75 against Opto125 gives p = 0.20 (cell 8 of the opto notebook). The LFP part cannot be tested, but that does not change the result.
- **figs10a.** As written, the criterion gives "reproduced" under reading (c), with FS p = 0.35 and TRN p = 0.88 (cell 54).
  - The author's assumption, that the pooled per-trial test does not show an absence of modulation, is stated and sound on its merits: the session-stratified FS test gives p = 1.3e-08 (cell 55).
  - But the record does not apply it to fig3a. The same check sinks fig3a (p = 0.19), yet fig3a stays "reproduced".
  - The record should either follow the criterion for both claims (fig3a and figs10a both reproduced, both flagged as fragile) or apply the within-session check to both (fig3a not reproduced; figs10a not reproduced, since its FS part fails and there is no partial clause).
  - I recommend following the criterion for both.

The `assumed: true` outcomes:
- **CSD row averaging** (fig1e, figs1b, figs4, speed-threshold, figs5, fig2b) and the **GFP baseline window** (fig2b, figs7a, figs7b): stated and reasonable.
- **fig2h, light-alone alignment:** stated, and now supported by the PSTH in cell 16.
- **figs10a:** stated, but applied inconsistently with fig3a, as above.
- **speed-threshold:** marked as assumed, but its only stated assumption is the CSD row averaging. That is fine.

### 2. Sentences the printed outputs do not support

- **Model timing.** Cell 102 says "one simulated second takes about 120 s on one thread and 80 s on four … about 2.3 h with four single-thread runs at once". The re-executed cell 101 prints 158 s and 113 s per simulated second, 3.0 h for four single-thread runs, and 4.9 h for the 15 s trials.
  - The record's notes for all five model claims and its responses to round 1 say 123 s, 83 s, 2.3 h and 3.8 h. These figures appear nowhere in the outputs.
  - The conclusion (longer than 1 h) still holds, with more margin.
- **Opto notebook cell 13 and the figs8b notes:** "no choice of two mice changes the outcome". The by-mouse table (cell 12) shows the MOs means of 673553 at 150.4, 159.6 and 162.4 ms. These are below the tolerance floors of 169, 173 and 176 ms. A pair in which 673553 supplies all the MOs units, for example 673553 with 671439, puts all three MOs means outside tolerance. The sentence holds only for the shift part of the criterion.
- **Opto notebook cell 17:** the rising VPM units are described "as expected of GABAergic units driven by the light". Nothing in the outputs shows these units are GABAergic. They are located in VPM, and they could also be mislocated TRN units or a light artifact. This phrase is not in the record.
- **Main notebook cell 103 (Summary) and finding 4:** they say the stimulation artifact "sits within one sample of every trial onset". Cell 5 prints an LFP artifact lag of 0.6 ms in 7 sessions, against a 0.4 ms sample, which is 1.5 samples. The lag is also measured on the trial-averaged signal, not per trial. The shared-clock conclusion still holds.
- **Main notebook cell 8:** it gives `waveform_duration` values of "about 0.15 to 1.5". Cell 7 prints 0.110 to 2.074. Finding 2 gives the correct range.
- **Main notebook cell 56:** it does not say that FS is significantly higher during running in 569069 (p = 0.0033, cell 55). This is an omission, not an error.
- **Formatting:** a stray "**" in opto notebook cell 17 ("What was found about the deposit.**").

Every other "Result:" sentence, both Summary sections, the README and the record's notes match the printed numbers.

On whether the record states my round-1 reasons in my own words: it does, faithfully. One exception is the five model claims. They are recorded as `agrees: true`, but in round 1 I gave blocked (other) and called the blocking unsupported. The reason text records this correctly; the `agrees` flag overstates the agreement.

### 3. Round-1 points

Resolved:
- **2 (fig3a pooling):** the within-session and van Elteren tests are now shown.
- **3 (triphasic reading b):** baselines and smoothed versions are shown. I agree the outcome stays partial: only the RS value at 20 ms smoothing falls in range, and no width brings the relay value close.
- **4 (opto unit pairing):** 1432 of 1432 units match across folders.
- **5 (fig2h alignment):** PSTH and rising units are shown.
- **7 (TRN with RT units):** the RT variant has been run.
- **9 (GFP over valid channels):** the variant has been run.
- **11 (HF/LF group sizes):** now stated in the text.
- **12:** no change was needed.

Resolved in substance:
- **1 (model claims):** the model is now built and timed, which supports the blocking. The quoted timings are stale.
- **6 (figs8b, two mice):** the by-mouse results are shown, but the conclusion overstates them.
- **10 (borderline p-values):** stated in the notes.

Not addressed: point 8 (artifact mask span), which does not affect any result.

What remains and bears on a conclusion:
- (a) "Partially reproduced" is used without a criterion clause for speed-threshold, fig2fg and figs10a.
- (b) fig3a and figs10a are handled differently under the same within-session evidence.
- (c) The model timing numbers in cell 102 and in the record do not match cell 101.
- (d) The figs8b robustness sentence is overstated.

### 4. Critical findings

No finding in the record's `findings` list is rated `critical`, and I see none that should be. Finding 4 is about the shared clock, and the outputs support it (cells 5 and 7), apart from the "one sample" wording noted above. Finding 1 (data missing, `major`) is rated correctly.
