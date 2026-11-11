**Verifier report, round 2: Moaddab, Wright & McDannald 2020 on CRCNS pag-2**

The claims file has 20 claims and the attempt record has 20 outcomes. Three carry `assumed: true`: fig5abc, fig5d and figs4. Cell indices below are those of the re-executed notebook.

### 1. Outcomes

I agree with all 20 stated outcomes.

- **Blocked (fig1bc, fig1ef):** agree.
- **fig2b, fig2c, fig2d counts, fig2d proportion, fig2ef:** agree (cells 10, 13, 16, 19, 22).
- **fig4ab and fig4de, partial:** agree. The script has no occurrence of "bregma" (cell 3), so the bregma part cannot be tested, and the first part holds (cells 27 and 33).
- **fig4c, fig4f danger decrease, fig4f discrimination:** agree (cells 30, 36, 39).
- **fig5abc, partial (assumed):** agree. Under the adopted reading (d, one) the interaction has p = 0.055 and the threat t test p = 0.037. The claims file's own rule gives the same result, through (b, drop) and (b, one) (cell 50). The assumption is stated, but the outcome does not depend on it.
- **fig5d, reproduced (assumed):** agree, conditionally.
  - The outcome holds only under (d, drop) and (d, one), with group p = 0.046 and 0.045. Under readings a to c, group p is 0.070 to 0.238 (cell 54).
  - The assumption is stated. It is reasonable because (d, one) is closest to the paper's statistics (cell 47). I checked that this ranking holds even without the small-denominator "5ABC FO t" term: by my hand calculation, about 0.08 for (d, one), 0.12 for (d, drop) and 0.22 for (a, zero).
  - Its grounding in script lines 2161–2170 is not shown in any output.
- **figs4, reproduced (assumed):** agree. The outcome does not rest on the assumption: readings a and c give "same: True" (cell 57), so the claims file's rule also gives reproduced. Under a to c the test is met vacuously, because the threat difference is not significant at either uncertainty value. `assumed: true` is unnecessary here.
- **fig5efg:** agree. Readings a and c meet all three parts (cell 60).
- **fig6, partial:** I now agree, which changes my round-1 outcome. The Methods Z-score the trial-averaged differential firing ("Mean differential firing was Z score normalized … standard deviation in firing = 1"). That is the claims file's normalization. I withdraw my round-1 view that the wording allows the SD to be taken over trial-level bins. Under the Methods' normalization, the danger part holds and the uncertainty part fails under all 12 readings (cell 65).
- **figs5:** agree (cell 68).
- **fig7, not reproduced:** agree. The uncertainty part fails under all 12 readings and both normalizations (cell 71). The claims file follows the legend and Results ("last 5 s", "last half"), so this is not a misreading.
- **figs6:** agree (cell 74).

I found no place where the claims file misreads the paper.

### 2. Sentences the outputs do not support

- **Record, fig6 notes:** "EAA safety firing correlates negatively with the beta (p = 0.03 to 0.04 in all readings)". Cell 65 gives EAA safety p from 0.0084 to 0.040: the (b) readings give 0.0084–0.0095, and (a, zero) and (c, zero) give 0.025 and 0.023.
- **Summary, cell 76:** "the outcomes of Figs. 5D and S4 rest on it, as the claims file's readings give a different outcome". This is false for S4 (cell 57, readings a and c). The same applies to the README row "Same pattern with the peak assignment … Reproduced, on an assumption" and to `assumed: true` on figs4.
  - By the rule in cell 41 ("where the two differ, the outcome is marked"), fig5abc should not be marked either: cell 52 says both rules give partial. Its README row still says "on an assumption".
- **Cell 7 and the record finding on storage windows:** cell 7 says "Nose pokes are stored only from 20 s before to 30 s after each cue onset, and the spikes only from about 20 s before to 33 s after". The finding says "Spikes and nose pokes are stored only from about 20 s before to about 33 s after each cue onset".
  - Cell 3 prints that 94.58% of pokes fall within −20 to +30 s, so 5.4% fall outside.
  - No output prints the extent of the spikes, although cell 5 says it is "printed below and above".
- **Cell 72 and the record's fig7 notes:** "Under every reading the Control uncertainty firing correlates strongly and positively". Under reading c, r is only 0.35–0.40 (p = 0.005–0.015, cell 71). It is significant, but not strong.
- **Cell 72 and the record's fig7 notes:** "With firing over the first 5 s … every part holds under both normalizations". Cell 71 ran this only under the adopted regression reading, and the sentence should say so.
- **Cell 41 and the fig5abc deviation:** "fixed before the outcomes were seen" / "fixed from the script before outcomes were compared". Nothing in the outputs can confirm this.
  - Statements about the script's content are also unprinted: the regress inputs at lines 2161–2170, and that it "computes cue-inhibited firing only over the first 5 s and the whole cue". Cell 3 prints only word counts.

Every other "**Result:**" sentence, the rest of the Summary, the README and the record notes match the printed numbers.

**My round-1 reasons in the record** are stated faithfully in my own words, with one error that was mine. The fig7 reason gives "r = 0.56 to 0.73 under the Methods' normalization"; cell 71 shows 0.35 to 0.73. The fig6 reason restates my trial-level-SD argument, which I withdraw above.

### 3. Round-1 points

**Resolved:**
- **B1 (normalization):** the script's normalization now runs as a full variant under all 12 readings for Figs. 6, S5, 7 and S6 (cells 65, 68, 71, 74). The fig6 outcome follows the Methods, and I accept it.
- **B2 (reading rule):** a single rule is stated in cell 41 and applied to every regression claim, with the comparison table in cell 47.
- **B3 (bregma):** the script contains no bregma (cell 3).
- **B9 (helper checks):** unchanged.
- **C, normalization as a full reading:** done.
- **B5 to B8** need no change. They are disclosed and do not bear on a conclusion.

**Remaining, bearing on a conclusion:**
1. **fig5d rests on reading d and a group p of 0.045.** The justification (script lines 2161–2170, `cer.cue` with empty trials set to 1) is still not printed. Printing those lines (C1 of round 1) would settle it.
2. **B4, the paper's smaller degrees of freedom:** partly addressed. Cell 44 counts candidates, but no exclusion rule was found, and about 13 cue-excited neurons are unaccounted for. The fig5abc interaction (p = 0.055) could change with the paper's neuron set. It is filed as a question for the authors.
3. **Text flags:** the figs4 `assumed` flag and the S4 sentence in the Summary contradict cell 57. The fig6 safety p range in the record is wrong.
4. **The fig7 outcome depends on the firing window.** It is correct as the claims file defines it. The paper's statistics match first-5 s firing (cell 71), which is recorded as a code_mismatch finding with a question to the authors. This confirmation rests on the adopted reading only.

**New point, does not affect a conclusion:** one cue-inhibited design is not of full rank (cell 44). `lstsq` returns minimum-norm betas for it, where Matlab `regress` would zero a coefficient. This touches 1 of 132 neurons in fig5efg, fig7 and figs6.
