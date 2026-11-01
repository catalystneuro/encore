**Verification report, round 2: Daume et al. 2024 on DANDI:000673 (0.240118.2135)**

The claims file has 57 claims and the attempt record gives one outcome for each: 12 reproduced, 5 partially reproduced, 8 not reproduced and 32 blocked (26 for another reason, 6 as too large). Eight outcomes are marked as resting on an assumption.

### 1. Outcomes and assumptions

**Agreed.** I agree with every outcome except those listed under "Not agreed".
- I now agree with five outcomes I disputed in round 1:
  - **pac-category-overlap, fig4c, fig4e, fig4g, fig4-amygdala (blocked, other).** This follows from my own problem 1: 8 and 5 neurons cannot test the paper's populations.
  - **fig3c (not reproduced).** My round-1 "partially reproduced" was wrong under the criterion: in Hz the claim reproduces fully, so the outcome depends only on the units chosen.
- I also accept the record's reasons for **edf7a, fig5cd and fig6g**. Each needs PAC neurons or cross-regional spike-field coherence.

**Not agreed.**
- **fig2f-rt-single-trial-pac and fig3h-pac-category-firing (both not reproduced): not established.**
  - The models code load with load 1 as the reference level (`pac:load[T.3]` and `sc:load[T.3]`, lfp cells 27 and 44). The PAC or spike-count (SC) term therefore estimates the slope in load 1 trials.
  - Tables S2 and S3 name their terms "Load1" and "PAC : Load1", so in the paper load 1 is the indicator and load 3 the reference, or the coding is by effects. Either way the paper's term is not the load 1 slope.
  - This matters because the interaction is significant here: p = 0.0075 for fig2f under (a, O5 a), and p ≤ 0.0025 for fig3h under every reading.
  - From Table S3, the paper's own load 1 slope is 0.002 − 0.004 = −0.002. That has the same sign as the notebook's −0.0045 (preferred trials, O5 b).
  - The same coding applies to fig4c, which is blocked anyway.
- **fig3f, fig3g, edf5c, edf5d, edf5fg and edf8fgh: blocked, but not as too large.**
  - By the record's own timing, the one-subsample surrogate form takes about 45 CPU minutes and would fit; the record says its cluster tests "were not written in this run for lack of time". The honest reason is "other: not run".
  - No notebook output shows the timings.

**Assumptions.** All eight assumed outcomes state their assumption.
- **fig3c and fig3d (rates as % of baseline, O6 b): reasonable.** Only this reading gives the paper's frontal n exactly: 201, 180 and 201 (nb1 cell 42).
- **edf2b, edf3f and edf3 (artefact reading a): reasonable but thin.**
  - The only evidence is one channel: of the paper's 17 rejected trials, reading (a) removes 4, all among them; reading (b) removes 5 that the paper kept (lfp cell 5).
  - All three outcomes flip under reading (b).
- **edf3e (windows aligned on gamma peaks): plausible, but departs from the Methods' words.** The question to the authors is filed.
- **methods-spectral-slope (2–150 Hz): reasonable.**
- **fig3h (reading a): not decisive.** Reading (b) gives the same result.

**Unstated assumption.** The load reference level in fig2f, fig3h and fig4c is an assumption that is neither stated nor consistent with Tables S2 and S3.

**Claims-file problems (reported, not corrected).**
- O5 reading (a), raw single-trial MI, cannot be the paper's measure. Table S3 gives a hippocampal intercept of −0.044, and Tort's MI is never negative.
- The criteria for fig2f and fig3h ask for the "PAC term" and "SC term" without fixing how load is coded.

### 2. Sentences the printed outputs do not support

**Bear on a conclusion:**
- **lfp cell 45 and the fig3h notes:** "negative, the opposite sign to the paper's (0.002, t = 2.40…)". This compares the notebook's load 1 slope with the paper's load 3 (or average) slope; the paper's implied load 1 slope is also negative.
- **lfp cell 28 and the fig2f notes:** "The claim's test is on RT itself (Table S2 gives the estimate in ms)".
  - Table S2 gives no unit. Its intercept of 0.38 and Load1 term of −0.48 cannot be raw RT in seconds or milliseconds; they would put load 1 RT near −0.1.
  - So the log10 RT variant cannot be dismissed on this ground. That variant gives a negative hippocampal term, p = 0.0066 under O5 (b).
- **fig3f notes:** the SFC timings appear in no output, and they argue against "too_large".

**Minor:**
- **fig2f deviation, "RTs … up to 16.8 s among these trials" (lfp cell 27).** The printed maximum comes from the last data frame of the loop (artefact reading b, vmPFC), not the hippocampal trials. The hippocampal reading (a) set loses 87 trials when RTs above 10 s are dropped (16,103 → 16,016). I repeated this error in round 1.
- **lfp cell 16 and the fig2c-no-load-effect-other-areas notes:** "sub-4 (session 37)" and "sub-11 (session 3)". 37 and 3 are list indices of the files; both patients have only session 1 (nb1 cell 3).
- **pac cell 6:** "exceed every shuffled count but one". The output (p = 0.005; shuffle maxima 1 against 8 and 5) shows they exceed every shuffled count, as the record correctly says.
- **Findings:** "unit 10 steps back 24 times". Only the largest step is printed (nb1 cell 7).
- **tables1 notes:** "−3.26". The output is −3.2656, which rounds to −3.27.
- **README:** "about 8 minutes" for the PAC-neuron notebook, against 9.5 min printed (pac cell 24); "about 4 minutes" for the first notebook, against 3.1 min (nb1 cell 45).

Every other number in the "**Result:**" cells, the Summaries, the README table and the record's notes matches the outputs. The README counts add up to 12, 5, 8 and 32.

**My round-1 reasons in the record.** The record states my reasons faithfully for all 57 claims, in substance and close to my own words. The fig3b and fig3c entries fold in my problem 3 correctly. The 16 disagreements are counted and split correctly (6 judged from printed results, 9 testable from the archive, plus fig3c).

### 3. Round-1 points

**Resolved:**
- **Problem 2:** fig3h is now tested.
- **Problem 3:** O6 reading (b) is adopted for fig3c and fig3d, with the evidence given.
- **Problem 5:** the missing controls were run and the V-test misreading is filed as a question.
- **Problem 6:** there is now a tie-break for O1, though it rests on one channel.
- **Problem 8:** the reading (b) comodulogram is shown.
- **Problem 9:** the pre-SMA channels were inspected; the result holds without the three largest channels (p = 0.0045).
- **Problems 10 and 11:** the pre-SMA boundary and the 20th test are now stated.
- **Waveforms:** they are in the files.
- **Released LFP:** a removed-trials histogram was added, though it does not settle whether the release is pre-cleaned.

**Partly resolved:**
- **Problem 4 (nesting):** a window sweep was added; the outcome still rests on the alignment, as stated.
- **Problem 7 (RT trimming):** the variants were run, but they are dismissed on an unsupported premise (the "ms" sentence above).
- **Problem 1 (PAC-neuron counts):** per-area uncorrected counts were added. I cannot check the record's reading of plot_PAC_neuron.m.

**What remains that bears on a conclusion:**
1. **GLM reference level (fig2f, fig3h, fig4c).** Refit with load 3 as the reference, or print the interaction estimates, before deciding these outcomes.
2. **Response scales in Tables S2 and S3.** RT appears to be transformed and PAC is not raw MI. The O5 (a) results and the dismissal of the log-RT variant rest on readings the tables contradict.
3. **SFC claims recorded as too large.** The record's own numbers do not support it; they are not run.
4. **The PAC-neuron gap (8 and 5 against 79 and 163) is unexplained.** Every claim on PAC neurons is blocked on it.
5. **Artefact reading (a) rests on one channel.** edf2b, edf3f and edf3 flip under reading (b).
6. **edf3e rests on the gamma-peak alignment.**

One robustness note, not affecting a recorded outcome: in % of baseline the sign-flip permutation p-values are much smaller than the t values suggest. For example, edf4b hippocampus has t = 1.64 with p = 0.019, and fig3b has t = 2.26 with p = 0.0013 (nb1 cells 27 and 30). The % values are heavy-tailed, so the statements that "reading (b) alone reproduces in full" lean on a few neurons.
