The claims file for DANDI:001515 is ready for an attempt: the checker passes and nothing I found is wrong enough to block it.

**Checker:** `claims/001515/10.1016-j.bioelechem.2026.109283.yaml: 34 claims, 34 quotes, 9 statistical values, 0 problems` (same result before and after my edits).

I checked each claim's source, expected values and tolerances, and statistics against the paper. All of them hold. The statistics are the paper's own test results; none is a threshold used to count cells. I also recomputed Eq. (2) myself and got 1.3% for a 10-fold rise and 11.9% for a 100-fold rise, which matches what the file's header says.

**Changes:**
- **Header:** `fig4b-poles-alike-570-780` was cited as Results 3.4, paragraph 3. The quote is in paragraph 4, which is what the claim itself says.
- **fig1-schwan-pattern:** the criterion now says the paper defines no arc at the equator, and that the ±5° width is borrowed from the pole arcs in Methods 2.3.
- **fig3-fluovolt-nonlinear:** the 10% departure band was credited to "the protocol's default tolerance", but that rule is for expected values. The criterion now says the smoothing spans and the band are not from the paper.
- **fig5a-gd-linear:** the Discussion puts linearity at about −700 mV, while Results 3.5 says −780 mV. I added −700 mV as a variant; the outcome is still judged on −780 mV.

**Still open** (all recorded under `checks`):
- **fig3-fluovolt-nonlinear:** the smoothing spans and the 10% band are an agent's choice. The paper judges the departure by eye.
- **fig6b-ca-train-responders:** the thresholds for a "strong" response and the 90% used for "nearly all" are not from the paper. I could not read the Fig. 6B cell counts because no PDF renderer is installed here.
- **fig5a-gd-cathodic:** the one-standard-error margin used for "prevented the progressive decline" is not from the paper.
- **fig1-pole-dimming:** condition (2) is tested only at 1400 V/cm, though the text covers 1000 to 1400 V/cm. The paper also doesn't say whether the Fig. 1 cell is one of the Fig. 4B cells.
- **fig2d-lasting-reduction:** the text says "about 20%" and the figure legend says "≤20%"; the claim keeps the text's value.
- **fig5b-conductivity-calibration:** the claim keeps the paper's ~2%, though Eq. (2) gives 1.3%.
- **fig7c-fast-conductivity-drop:** the paired t-test between the two poles is borrowed from the Fig. 7 legend; the paper names no test for that comparison.
- **fig4c-equator-follows-cosine:** the ±15° and ±30° equator arcs are not from the paper, and the legend and Results place the equator at different angles.

Every main finding of the paper has a claim, and every claim comes from this paper. I did not commit or push anything.
