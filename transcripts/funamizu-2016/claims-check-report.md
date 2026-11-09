I checked the claims file against the paper, fixed what was wrong, and added the new `checks` entry. The file is ready for an attempt (`ready: true`). Nothing is committed.

**Checker:** `40 claims, 40 quotes, 78 statistical values, 6 problems`. All six are p-values where the text extraction garbled the "× 10⁻ⁿ" (supp1 ×2, supp2d, supp8c, supp13, supp8a). I found each one printed in the paper. The quotes all pass.

PyMuPDF wasn't installed and the system install failed, so I installed it into `$TMPDIR` to render figures. The untracked files in the repo root were already there; I didn't touch them.

**Changes, by claim**
- **Sources (about 25 claims):** many paragraph numbers were off by one. The PDF's indentation shows "During sound omissions" continues paragraph 2, and the 41,031-neuron sentence is in paragraph 1 of its section. The Methods references for behaviour timing (now paragraph 5) and the SVM (now paragraph 8) are also fixed.
- **fig1c-licking-without-sound:**
  - The statement put intermittent 2's no-sound zone around the goal, where that condition actually has sound. It now names each condition's no-sound zones.
  - The criterion's bin and comparison readings were invented and didn't match the figure. Fig. 1c compares 4.2-cm bins 8.4 cm apart. This layout makes the text's no-sound P range (4.87e-8 to 1.22e-15) come out exactly. The criterion now uses it and also tests intermittent 2.
- **fig1fg-muscimol-no-sound-licking:** the statement said PBS licking rose "in every condition", but two PBS comparisons have P > 0.01. Rewritten to what the paper supports, and the criterion now uses the Fig. 1c layout (the muscimol no-sound range matches it too).
- **fig1d-muscimol-correlation** and the header: n is 12 muscimol and 12 PBS sessions, not 12 in total. Fig. 1f's signed-rank w reaches 78 = 12×13/2 for both groups.
- **supp2d-muscimol-overrun:** added the trial numbers (n).
- **muscimol-locomotion:** the speed and lick measures were made up; they are now listed as open, with readings.
- **lick-goal-correlation:** now says the Results don't name what r correlates, and why the Methods' session-selection correlation is the reading.
- **fig2d-task-relevant-proportions:** the note said pooled counts fit "within 2%"; they differ by up to 1.5 percentage points. Corrected.
- **fig2d-goal-distance-ppc-more:** whether counts or proportions were compared is now an open reading.
- **fig2d-layer-distance-preference:** removed "layers 3 and 5 did not differ" from the statement. The paper never states it and the criterion doesn't test it.
- **neuron-classes:** added the Fig. 2d goal-distance-or-reward counts, shown but not judged.
- **supp8a-pm-no-sound:** the criterion was weaker than the paper. Supplementary Fig. 8a marks all three PM layers significant in intermittent 2 and none in intermittent 1; the criterion now requires that. I also added the Results' P range for PM.
- **supp8c-ppc-steeper-than-pm:** noted that the figure confirms the order of P values the criterion assumed.
- **supp9-preserved-representation:** "absolute difference" was presented as given; it is now marked as a reading, with the reason.
- **supp11-sound-reduces-error:** Supplementary Fig. 11c compares slopes of the RMSE difference, not RMSE levels, so the statement is restated. The legend's n = 68 allows two readings, and both are now named.
- **svm-correlations:** the shuffle method was stated as fact; it is now a named reading.
- **New claim, fig5c-uncertainty-decreases-with-sound:** PPC uncertainty falls with sound between 8.4 and 0 cm (Fig. 5c). This was a main updating finding with no claim.

**Still open**
- The Fig. 1c and 1f bins and the pairs compared come from the figures. The paper's P ranges support that reading, but no sentence states it.
- Fig. 1d plots sessions 1 to 10, while Fig. 1f implies 12 sessions per injection type. The paper doesn't settle which sessions the Fig. 1d test used.
- For PM no-sound slopes, the Results give z up to 9.59 and Supplementary Fig. 8a up to 6.11; the two can't both be right. The criterion follows the figure's per-layer marks, and the header records the conflict.
