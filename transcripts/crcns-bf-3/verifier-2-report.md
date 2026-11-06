**Round 2 verification: Moaddab, Ray & McDannald (2021), CRCNS bf-3**

**1. Outcomes and assumptions**

The attempt record has 45 outcomes: 28 reproduced, 15 partially reproduced, 2 not reproduced, 0 blocked. The README and the Summary (cell 170) give the same counts.

I agree with all 45 outcomes. Three differ from my round-1 position:

- **supp6-low-nosepoke-pauses:** now partially_reproduced, as I gave in round 1.
- **fig2-excited-inhibited-split:** I now agree with reproduced, but only under A1. The claim's statement names the 257 neurons. On those, the claims-file reading "Hz, two window means" gives 130/127 (cell 29). On the Methods' 271 neurons, every claims-file reading fails (142 to 155 inhibited). My round-1 range of "139 to 155" was wrong.
- **supp9-excited-nosepoke-pauses:** I now agree with reproduced, but only under A3. With the code's pause definition, no post or post − pre interval lies above zero under any scaling, on 3367 events with 9 to 46 per neuron (cell 96). The margin is thin: lower bounds are −0.013 and −0.001. Under the claims file's own 5 s/(ii) reading, firing rises after the pause, so the claim fails there.

All three assumptions are stated, attached to every outcome that uses them (`assumed: true`), and reasonable:

- **A1 (neuron groups from the authors' code):** reasonable because the code reproduces 257/153 and 131/126 exactly (cells 20 and 29). The script lines are now printed in cell 15.
- **A2 (one k-means start after rng(1)):** reasonable because the Methods name Matlab `kmeans`, whose default is one start, and the code does `rng(1)` (cell 15, lines 1485-1487). It is fragile: only 98 of 300 seeds reach the paper's partition (cell 44).
- **A3 (the code's pause definition):** reasonable because it is the only definition in any source (cell 15, lines 170-193).

No outcome that depends on an assumption is missing its flag. ancova-inhibited-baseline-effect and the two Fig. 1f claims also hold on groups B, so it is right that they are not flagged.

**2. Sentences the printed numbers do not support**

- **Cell 32:** "On those neurons two of the criterion's four readings give counts within tolerance". Cell 29 shows three of four within tolerance with the three-cue pool (Hz two means 130/127, normalized two means 125/132, normalized pooled 121/136), plus the four-type pool with two means (124/133). Cell 0 repeats the implication: "the claims-file reading of the split that gives counts within tolerance (Hz, two window means, 130/127)".
- **Cell 59:** "The baseline length and flooring move the means by at most 0.06." This fails for one of the seven means. In cell 58, Intermediate uncertainty onset moves from −0.592 to −0.442 (0.15) under trial means, and from −0.330 to −0.253 (0.077) under single trials. The record's round-1 response for fig3b-low-inhibited-to-threat-cues says the same thing and is wrong for the same reason. The fig3b notes are correct, because they cover only the four Low means, which move at most 0.054.
- **Cell 150:** "With scaling (ii) … the pre intervals exclude zero." Under events (a)/(ii), the Low pre interval is [−0.044, 0.150] (cell 149), which contains zero. The record's version ("the Intermediate pre interval excludes zero") is correct.
- **Summary (cell 170) and README:** "Most of the partial outcomes are values outside tolerance under the Methods' normalization that are within tolerance under the code's." From the record, 10 of the 15 partial outcomes meet the criterion under the code variant. Only four of those failed on values alone (fig3b-low-inhibited-to-threat-cues, fig3d-intermediate-inhibition, fig5d-f, fig6-excited-peak-cue-vs-reward). The others failed on p values or on intervals. Some partials still fail under the code variant:
  - fig6g: R² values 0.084/0.113/0.098 are still outside tolerance (cell 162).
  - fig3b-low-differential: the delay interval reaches zero (cell 67).
  - fig6b: the safety intervals still exclude zero (cell 85).
- **Summary (cell 170):** "All rest on assumptions A1 and A2 except …". fig2, ancova-excited and the cue-excited claims rest on A1 only, as the record itself marks them.
- **Record, fig3d-intermediate-inhibition notes:** the list of means outside tolerance leaves out safety onset under the three-cue pool (−0.337 against −0.21 ± 0.10, cell 73). This does not change the outcome.
- **Record, `reviewed` field:** it says the conclusion cells and summary were removed from what I reviewed in round 1. The header summary table in cell 0 was still present then, as my round-1 report noted.

Every other "**Result:**" sentence, the remaining Summary and README sentences, and the record notes match the printed outputs.

**How the record states my round-1 reasons:** they are faithful close paraphrases. One gap: for fig3b-low-inhibited-to-threat-cues, the reason keeps only "never isolates which element causes the gap" from Problem 2. It drops the main point, that the Methods may not describe the computation the figures were made with, and that this decides fig3b, 3d, 4c, 4g, 6b, 6c and fig6-excited-assignment-050. The finding on the code mismatch covers the substance.

**3. Round-1 points**

Resolved:

- **1:** A1 is now stated as an exception, with its reasons. A crosstab shows 25 of the 257 neurons fall in the other group (cell 31).
- **2:** Cell 58 isolates the cause: Z-scoring single trials, not trial means, explains the gap.
- **3:** The membership check is done; the claims-file reading and the authors' features give the same clusters (adjusted Rand index 1.000, cell 46).
- **4:** supp6 is downgraded and the pause event counts are printed.
- **5, 9, 10:** stated as I asked.
- **11:** the dead expression is removed.
- **Part C:** the cited script lines are printed (cell 15).

Remaining, and bearing on conclusions:

- **Clusters:** about 25 cluster claims rest on a single-start partition reached by 98 of 300 seeds. The claims file's statement that the seed cannot change a conclusion beyond the edge of an interval is wrong here. A question is filed.
- **Neuron groups:** fig2, ancova-excited and all cue-excited claims rest on A1. ancova-excited (p ≤ 0.0006) and fig4f-int-no-assignment-interval (models a and b) reverse on groups B.
- **Possible claims-file misreadings (points 6 to 8):** the 10% tolerance on R² (fig5d-f, fig6g), the 1 s onset window in supp5, the safety requirement in fig6b, and scaling (i) in fig6-excited-peak-cue-vs-reward. Questions are filed; the outcomes would change if they are answered differently.
- **supp9:** rests on A3 and fails under the claims file's 5 s/(ii) reading.
- **Text errors:** cells 32, 59, 150, the Summary and README sentence on partial outcomes, and the record's fig3b round-1 response still need correcting.
