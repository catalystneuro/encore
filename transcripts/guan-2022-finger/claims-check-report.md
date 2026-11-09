I checked the claims file for DANDI:000252 against the paper, made eight corrections and logged three open problems. The file is ready for an attempt.

**Checker result** (same before and after my edits): `19 claims, 19 quotes, 12 statistical values, 0 problems`

**Changes, by claim**
- **Header:** added open item O11. The paper never says which time window its ten-finger analyses use. The Go window is the only one the text supports, and the file now says that.
- **tenfinger-discriminative-fraction:** removed "in the Go window" from the statement, because the paper does not say it. The criterion now points to O11.
- **tenfinger-decoding-accuracy:** the rule for "partially reproduced" used a one-sided binomial test the paper never uses. It is now "one or two of the three accuracies within tolerance".
- **fig8a-npcc-index-distinct:** removed a Pearson r > 0 test over ten distances, which the paper does not use. The check now covers only the index, middle and ring fingers, as the Results do.
- **figs11-jppc-lower-matched-size:**
  - Removed the hand CCGP clause from the statement, since neither the quote nor the criterion covers it (fig8e-hand-ccgp does).
  - The comparison sizes now stop at the smallest of the three pooled populations. J-MC (about 260 neurons) is smaller than J-PPC (about 320), so the old rule could not compare them at the J-PPC size.
  - The 50-neuron steps are now labelled a standard choice.
- **fig4e-plan-vs-move:** added two readings of the denominator. The paper's N-PPC 43% "strongly tuned" in the Go window is larger than its 40% with η² > 0.14, which should be a superset, so the two numbers cannot use the same denominator.
- **fig5a-contra-decoding:** how errors involving No-Go count was a choice made by the earlier agent, not the paper. It is now two named readings.
- **figs6-single-array-retrospective:** extended the quote to include the J-MC sentence that gives 87% ± 8%.

**Still open** (logged in the `checks` entry)
- **O9:** the paper gives no margin for "close to standard accuracy". Of the two readings, "at least 0.9 of standard accuracy" is a convention, not from the paper. Only the other one rests on the paper's own J-PPC contrast.
- **fig8a:** the paper gives no measure for "similar across hands"; the criterion reads it as the index pattern holding in both hands.
- **fig4c:** the legend's 466 pooled N-PPC neurons do not match 118 × 4 = 472 from the per-session mean. The per-session counts may have been taken before the 0.5 Hz exclusion (O1).

Every claim checks out against the paper apart from these, and each main finding has a claim. Nothing is committed.
