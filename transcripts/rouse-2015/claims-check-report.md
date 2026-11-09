The claims file is ready for an attempt. I edited only `claims/000941/10.1152-jn.00686.2015.yaml`.

**Checker:** `26 claims, 26 quotes, 3 statistical values, 1 problems`. The one problem is `VALUE NOT FOUND` for p = 0.001 in table2-movement-time. The text garbles the bound as "P �10�3", and I read it as P < 0.001 from the sentence around it. The PDF could not be rendered here, so I couldn't confirm the "<" glyph. All quotes, including the two I extended, match the text word for word.

**Changes, by claim:**
- **fig2-hand-opening-two-phases:** the list of angles was wrong. It included LittlePIP and gave eleven angles; the paper lists ten and puts LittlePIP with the angles that decrease, increase and decrease again. I corrected the statement and criterion, and the threshold is now 8 of 10.
- **fig7-mean-eta-30 and fig7-mean-eta-90:** these counted as reproduced if any one combination of sum of squares type and error-term (SSError) placement matched. Both are method details the paper leaves open, so the protocol requires all combinations to agree, or else the claim is blocked as methods_underspecified. I changed both criteria to that.
- **Common methods (SSError placement):** the second placement was called a "variant". Neither placement comes from the paper, so both are now readings that must agree.
- **fig5-location-early-object-late:** part (4) only counted angles whose location effect at contact was already below its peak, so it depended on its own outcome. It now covers all 18 wrist and digit angles, and the bounds are named as readings.
- **fig5-hand-object-predominates:** the paper uses "proximal" in two ways, so the criterion now lists both: shoulder and elbow, or those plus the wrist. The measure of "predominate" is named as a reading.
- **fig5-shoulder-object-effects:** the quote now covers the "beginning quite early" part of the statement, and the 30% bound for "early" is named as a reading.
- **fig5-shoulderier-location:** the 0.9 bound is named as a reading, not a number from the paper.
- **fig8a-lda-location:** part (2) said both "at C" and "from 50% to C". It is now the mean accuracy from 50% to C. The 30% and 50% points are named as readings.
- **fig10-forearm-trajectory-object:** the quote now includes the Discussion sentence on vertical order (sphere highest, coaxial cylinder next, button lowest), which the statement and criterion use.
- **elbow-point-trajectory-object:** the comparison of accuracy above chance is named as a reading.
- **New claim, fig8-hand-shape-invariant-to-location:** the abstract's finding that grasp shape varies little with location had no claim. It comes from the Discussion and Fig. 8.

**Still open:**
- The Kruskal-Wallis bound's glyph, as above.
- Many criteria depend on how qualitative words are read ("early", "comparable", "similar", "nearly 100%"). The paper gives no numbers for them. They are all labelled as readings, so outcomes close to those bounds are weak evidence either way.
- Fig. 10 and the elbow-point plots don't name the monkey. The claims are judged on monkey L, and the other monkeys are reported.

The checks entry records each of these with `ready: true`. Nothing was committed.
