**Round 2 verification: Park et al. 2019 (Neuron 101:285), CRCNS hc-20, attempt park-2019-01**

**1. Outcomes and assumptions**

The claims file has 22 claims and the attempt record has 22 outcomes: 9 reproduced, 5 partially reproduced, 3 not reproduced and 5 blocked. Six outcomes are marked `assumed: true`.

I now agree with all 22 outcomes. Two of them differ from my round 1 view:

- **fig4c:** the author changed it to not_reproduced, which matches my round 1 outcome.
- **fig5:** I now agree with partially_reproduced. The criterion gives a partial outcome when "the tests hold but not every r". Cell 44 shows that every Rayleigh and Kuiper test holds under readings (b) and (c). That partial branch is weak, because none of the four r values comes near its expected value. The possible misreading of the claims file is now a question for a reader, and the head-direction reading I asked for (cell 44) also stays below tolerance.

The six assumptions:

- **fig1c-speed:** stated and reasonable. The outcome needs either the 100 cm/s filter or the between-groups Tukey test (cell 32), and the record says so.
- **fig1c-directionality:** the repeated-measures Tukey test is stated, with a reason, and the record says the between-groups test would make this claim partially reproduced. It is reasonable, but a reader could defend either test.
- **fig2:** the "majority of seven" threshold comes from the claims file, and the record says the count depends on 1023R029. Stated and reasonable.
- **figs2:** the outcome rests on one reading out of 16; the record states this and shows the margin sensitivity. Stated and reasonable.
- **no-angular-velocity-tuning:** the test comes from the claims file. Stated and reasonable.
- **figs3: stated, but the reason given is weak, and the outcome depends on it.** The record defends n = sum of weights as "the standard n for grouped data with frequencies as weights (Zar)". The weights here are mean ΔIdir values rescaled so the largest is 1, not frequencies, so their sum depends on that arbitrary scaling. The claims file's own check points to reading (a), n = number of bins: at r = 0.17 it gives p ≈ 0.35. Under (a), 1121R157 in the room frame gives p = 0.0134 (cell 56). The criterion requires "every test p ≥ 0.05" and has no partial branch, so under (a) the claim would be not reproduced. I did not raise this in round 1.

**2. Sentences the printed numbers do not support**

- **Cell 45, and the fig5 notes:** "Rayleigh p from 2.66e-10 to 0.00459". The smallest p in readings (b) and (c) is 2.17e-20 (reading b, arena frame, cell 44). The outcome is not affected.
- **Cell 62, and the fig4 notes:** "So the gap follows the passive rotation of head direction in the room frame, a property of the measure". Three outputs in cell 61 work against this:
  - Per pair, the spike gap and the samples-only gap are uncorrelated (r = -0.01).
  - The spike gap (0.214 against 0.156) is about three times the samples-only gap (0.068 against 0.048).
  - In the clean pairs the spike gap shrinks to 0.176 against 0.149, while the samples-only gap stays at 0.070 against 0.047.

  The samples explain the direction of the shift, not the size of the gap. The outcome under the criterion is unchanged.
- **Cell 65, and the fig4c notes:** "The occupancy and after-side variants give the same pattern at 20 to 60 s." Cell 64 shows otherwise:
  - In the occupancy variant the arena frame is below the room frame at 40 to 60 s, and below all three other conditions at 60 s (p vs room = 0.0028).
  - In the after-side variant the room frame is below the arena frame at 20 s (p = 0.0167).

  The test that matters (arena frame below the other three at every interval from 20 to 60 s) fails in both variants, so the outcome stands.
- **Cell 8, and the attempt record's data findings:** cell 8 says each problem is "shown by the cells above", but no printed output shows these:
  - "median 7 to 13 px at the best constant lag"
  - that the .dat files of 1211R039 agree with each other and that its arena-frame TSD track "matches its arena .dat file exactly"
  - "2919 spikes" for 1024R157 P9C1
  - "614 of its spikes lie far from the sample" for 1017R035 P11C2

  None of this bears on a conclusion.
- **Entry README:** "takes about two minutes". Cell 67 prints 2.9 min.

Everything else checks against the printed outputs: the other "**Result:" cells, the Summary, the README's outcome table and its "four outcomes … change or lose their margin" sentence, and the other notes.

The attempt record states my round-1 reasons faithfully and in my own words. It also records my round 1 error on fig5c (63.3 was the neighbouring bin, not a minimum) and corrects it. One sentence of my round-1 fig4c reason is wrong and should be amended: "Under no variant is the arena frame below the room frame at 20 to 60 s." At 60 s the occupancy variant (p = 0.0028) and the clean variant (p = 0.0368) both put the arena frame below the room frame. The outcome does not change, because the ANOVA is already significant at 10 s.

**3. Round-1 points**

Resolved:
- 1 (no clean variants): added for decoding, Idir, proximity, Figure 5 and fig4c.
- 2 (which data governs): the notebook now says outcomes are decided on the files as deposited.
- 3 (repeated-measures Tukey not marked as an assumption): now stated as one.
- 5 (figs2 margins): margin sensitivity and the clean variant are shown.
- 6 (fig2 stable2 decoding at chance): the shifted-reference gaps are printed, and the clean variant gives 3 of 6.
- 7 (fig4 arena-vs-room KLD gap): checked in cell 61, though the conclusion drawn overreaches (section 2).
- 8 to 12 (non-conclusion points): stated where they apply.
- Section C requests: all answered (Table S1 dates, fig5c curve and null, head-direction reading), except the paper's 38 speed units, which cannot be identified from the data.
- 4 (fig5 misreading): handled as well as it can be. It is sent to a reader and run as a variant.

Remaining points that bear on a conclusion:
1. **figs3:** the n of the weighted Rayleigh test decides the outcome, and the stated reason for using the sum of weights does not hold (section 1).
2. **fig2 and figs2:** both reach their counts only with 1023R029, whose rotating tracks are shown wrong. Without it, fig2 gives 3 of 6 below the arena frame and figs2 gives 4 room and 1 arena. Both are disclosed and fragile.
3. **fig1c-directionality:** the outcome depends on which Tukey test is used and on the clean variant; it is disclosed.
4. **fig4:** the outcome flips to reproduced in the clean variant, and the explanation of the arena-vs-room gap is not established (section 2).
5. **fig5:** whether the claims file reads the paper's "polar distribution of directional error" correctly is still open, and is with a reader.
