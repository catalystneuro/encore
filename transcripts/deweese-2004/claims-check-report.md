The claims file for CRCNS:ac-2 is ready for an attempt, after corrections. The last check entry has `ready: true`. Nothing is committed.

**Checker:** before my edits it read `23 claims, 23 quotes, 3 statistical values, 0 problems`. After them it reads `23 claims, 23 quotes, 1 statistical values, 0 problems`.

**How I settled the garbled signs:** the paper's text file turns <, >, =, ±, ≥ and similar signs into a replacement character, and the file's author had guessed them from context. The PDF could not be rendered here, so I decompressed it and read each sign from its font encoding. Several of the guesses were wrong; the header now lists the signs as read from the PDF.

**Changes, by claim**
- **header:** sign readings replaced with the decoded ones.
- **fig2-stereotyped-shape:** added the Figure 2 legend's "20 presentations" to how the example neuron is identified. Marked the 50 ms latency bound as a choice made here, since the paper gives no number.
- **fig3a-reliable-neuron:** cited the Results sentence calling the 0.88 mV neuron "The most reliable neuron", which supports picking it as the neuron with the lowest tone-averaged q.
- **fig3b-total-variability-distribution:** the PDF says "from < 1 to > 10 mV", not about 1 to about 10; statement corrected. The Figure 3B bins are strict, so the "bounds open" wording was dropped. Added a second reading of the 7/33 as q < 2 mV, because the Results count the 0.88 mV neuron as "comparably low (1-2 mV)".
- **fig7a-lfp-culling-estimation:** the criterion never judged the statement's "little effect when total variability is small" part. It is now shown, not scored, against the PDF's "already small (≈1 mV)", with a 1.5 mV bound named as a choice.
- **culling-controls:** the criterion ignored the 29% and 38% fractions it lists as expected values; they now count toward the outcome.
- **fig7d-large-responses, large-responses-controls, cv-large-responses:** the PDF says "≥ 15 mV", so "above 15 mV" became "at least 15 mV" throughout.
- **cv-large-responses, anesthesia-comparison:** removed the `statistics` entries. The paper names no test and gives no p-value; the p < 0.05 was assumed. That assumption stays in the criteria.
- **lfp-cv-not-different:** the paper prints "P = 0.5", not "P > 0.5"; the statement and `p_relation` are corrected.
- **access-resistance-depth-no-effect:** the file had the groups reversed. The 4.2 mV group (17 cells) is above the median access resistance and the 4.9 mV group (16 cells) is below it. Labels and criterion corrected.

**Still open** (recorded under `checks`)
- No figure was looked at as an image. Two glyphs were read as ≤ and ≥ from the font's naming pattern, not from a rendering. The reading fits the text ("≤ 85%" next to "as much as 85%").
- Several criteria put numbers on words the paper leaves vague: the 0.9 correlation in fig2, "many" in fig5b, 80% in private-shared-ranges, and "about 3 mV" in psp-culling-reduction. Each is named as a choice, and outcomes on those parts depend on it.

Each main finding has a claim, and every claim comes from this paper.
