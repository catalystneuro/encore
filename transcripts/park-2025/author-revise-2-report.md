I've answered every point in the round-2 report and re-run the entry with `python tools/entry.py all`. Both notebooks pass (reproduce 26 min, simulations 34 min) and `check` reports 0 errors. Nothing is committed.

**Outcomes.** None changed, as round 2 requires. On fig3d-distal-first-bap I agree with the verifier and put a change to `blocked` (`methods_underspecified`) under `proposed`, for round 3 to review:
- The criterion picks the threshold whose counts match the legend. File D4 has exactly the legend's 84 bAPs only at 5 s.d.; at 4 s.d. it has 85 to 88.
- At 5 s.d. the two filters disagree: 32 of 54 (inside 31.5 to 38.5) and 31 (just outside).
- The 4 s.d. threshold the outcome rests on does not reach the legend's totals in the burst files either (161 to 165 against 167, and 167 against 170).

A new notebook table shows this, and I took back my round-1 claim that the verifier had endorsed 4 s.d.

**Added:**
- **figs2:** the paper's pixel-weighting method and a noise window away from the first second. Noise falls to 1.9 ± 0.6 mV at 1 kHz (still outside 1.2 ± 0.5) and 2.5 ± 0.5 mV at 2 kHz (now inside). Optical spikes are still missed and added in every reading, so not_reproduced holds.
- **figs15:** the question to a reader in `questions/001266.yaml` (across-trial spike times or regularity within a train). I added a within-train regularity measure as a variant; the paper gives no bound for "regular", so it decides nothing.
- **figs23:** a version that counts only a positive difference. It leaves the longest persistence unchanged.
- **dSpike threshold:** the verifier was right that the code does not follow the written rule. I corrected the description to match the code instead of changing the code: a stricter rule would also drop the 8 real dSpikes of Fig. 2, since 8 among 100 failures make a bump only 0.08 as high on synthetic data. The notebook now shows, per recording, how many amplitudes sit above each threshold. Fig. 4d's 0 to 3 dSpikes rest on 1 to 6 outlying values; its notes say so.

**Corrected:** every unsupported sentence the report quoted, in the notebooks, summary, README and record:
- the 4 s.d. "legend totals" wording;
- the D4+soma dSpikes being on the third bAP, and 44 to 48%;
- 7 or 8 of 12 (fig4d);
- the Ni²⁺ file: 7 of 8 readings without a threshold, one reading defined, 2.0 or 2.5;
- the 20 ms smoothing creating new 0 ms returns;
- fig5d's (b) ratios being undefined, not lower;
- fig2e-f's +dSpike threshold being met beyond 300 µm;
- the fig2h counts, with `measured` now 1457.0;
- figs17e's "disagree" wording and the 4 dSpikes it left out;
- the summary's one-neuron sentence.

The phase-diagram runtime varies between runs (22 to 31 min), so the record, README and `entry.yaml` now give a range.

**Recorded:** round 2 is under `verifications`, with all 55 claims, the verifier's reasons in its own words and my responses.

**Not done:**
- **Somatic spike counts in the wide-field and drug files** (they swing up to threefold with the settings): not validated. Those files have no patch channel to check against; the notes say so.
- **Single-cell parts of blocked claims:** still not run. This changes no blocked outcome.
- **Minor points without effect on any conclusion** (B6 and B16 to B19, including the clock check for file 184232): left as they were.
