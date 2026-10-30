I've finished the whole author run for DANDI:000462: entry, notebook, helper, attempt record and verifier handover. Of the 41 claims, 31 were tested and 10 are blocked; `entry.py check` passes and the notebook runs cleanly in about 11 minutes. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| session-lap-counts, fig1d, fig1e, fig1g, supp4-lickstop-definition-robust, supp6b, disengaged-laps-uniform, fig2a, fig2c, fig2d, fig3b-reliability, fig3b-out-in-ratio, fig4m | reproduced (13) |
| lick-persistence-ur, fig1f, supp4-lapwise-r2, supp5, engaged-lap-counts, fig3c, fig3d, supp13, supp16, fig4f, fig4h | partially reproduced (11) |
| approach-ratio, fig2e, fig3a, fig3b-width-intensity, supp11, reward-zone-field-turnover, supp18 | not reproduced (7) |
| supp2, controls-no-change-over-time, supp6-pupil, supp15-tdtomato, the five fig5/supp20/supp21 axon claims | blocked, data missing (9) |
| supp14-reward-cells | blocked, methods underspecified |

Almost every tested outcome is marked `assumed`, because the files hold raw fluorescence only and dF/F, transients and place fields had to be computed with rules the paper does not give.

## 2. Dataset, assumptions, questions

**Version.** I pinned 0.230416.2132, the only published version (the paper cites none). It holds 10 of the 12 wild-type mice (5 of the 6 with RR and a novel session) and 4 of the 6 DREADD mice.

**What I found in the data:**
- **sub-014 is misaligned.** It has 6000 fewer behaviour rows than fluorescence frames. Decoding position from the fluorescence shows the gap is at the start of BeforeCNO, so every later behaviour row in the file is 6000 frames early. The helper corrects for this.
- **DREADD fluorescence offset.** All four DREADD files carry an undocumented offset of about 17000 counts; without removing it, dF/F comes out about 10 times too small.
- **Rewarded first UR lap.** In 4 mice, a reward is delivered at the end of the first lap of the Unrewarded condition as the frame counts define it.
- **Missing labels.** Conditions are given only as frame counts in a free-text description. Position is in volts with no scale. The indicator is listed as "GFP", and all files share one session start time.
- **Smaller mismatches.** sub-NR6 has 8 extra behaviour rows and sub-CFC4 one fewer, at the end. The paper's code silently keeps only part of some sessions (for example, the first 11100 of 20000 R frames for NR6).

**Main assumptions:**
- dF/F, transients and candidate place fields follow ref. 75 (8th percentile in a 15 s window; transients from 2 to 0.5 robust SD lasting at least 0.5 s; bins above 25% of baseline to peak). The resulting fields are about twice as wide as the paper's.
- The top of the position voltage range is 200 cm. With this, lap times and speeds come out longer and slower than the paper's (12.2 s against 7.34 s per R lap).
- The approach ratio is taken over the whole lap. This reading gives the paper's 70% engaged laps and its 3 qualifying mice; the ratios themselves still don't match.
- The reward zone ignores licks in the first 20 cm after the teleport.
- The DREADD offset is removed as the file minimum.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings): the dF/F and transient rules; the volts-to-cm conversion and how lap time is defined; the approach-ratio window; the reward-cell definition; how stable and remapped fields were told apart, and which mice form Figures 2 and 3.

**Questions to a reader:** none.

## 3. Where the protocol was unclear or missing something

1. The fig2c criterion requires readings S1 and S2 to agree, but S1 needs the control mice, which are not in the dataset. The protocol doesn't say what to do when a required reading cannot run. I judged on S2 alone and recorded it as a deviation.
2. Thresholds written as counts of mice ("9 of 12") don't fit a dataset with fewer mice. I applied them as proportions (8 of 10 mice) and recorded that.
3. `measured` needs one number per expected value, but approach-ratio's dark value cannot be measured. I left `measured` out and gave the numbers in the notes.
4. I blocked supp14 as `methods_underspecified` without running any readings, because any reward-cell threshold would decide the count of 43. Step 1.6 asks for every reading to be run first, which I did not do.
5. The clock check the protocol describes assumes trial tables or annotations; these files have neither. I used a decoder with labels shifted 10 s for the wild-type mice, a lag scan for sub-014, and the place fields found in every condition for the other DREADD mice.
6. The protocol doesn't cover datasets that hold only raw signals where the paper analysed processed ones, which forces assumptions onto nearly every outcome. I marked those outcomes `assumed` and gave the reason in a deviation.
7. To keep every command in the foreground, I ran per-mouse processing two at a time inside one command; the notebook does the same.

## 4. Runtime and failures

The run went from about 08:06 to 10:15 UTC, about 2 h 10 min. The final notebook execution took 646 s, and the last three full runs gave identical numbers. Nothing failed. The approach-ratio definition was changed twice during development, and the field-parameter rule once, each followed by a full rerun.

Files are in `entries/000462-krishnan-2022/` (notebook `reproduce_krishnan_2022.ipynb`, helper `krishnan.py`); the record is `attempts/000462-krishnan-2022-01.yaml`.
