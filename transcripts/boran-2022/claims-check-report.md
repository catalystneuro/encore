The claims file is ready for an attempt (`ready: true`). I made eleven changes. Two problems are still open: I couldn't check the numbers read from figures, and the paper doesn't give its permutation schemes.

**Checker result** (the same before and after my edits): `17 claims, 16 quotes, 18 statistical values, 0 problems`

**Changes, by claim**
- **behavior-accuracy-by-set-size**:
  - The source pointed to Discussion 4.1 paragraph 3. I changed it to paragraph 2, where the 89% average is printed.
  - The F value was listed in `expected` but never judged. The criterion now requires it to be within tolerance.
- **behavior-rt-set-size**: added the reported F(3,45) = 48.47 to `expected`. The criterion now judges F and the 2678-trial count.
- **table1-capacity-and-neurons**:
  - The 13 Kmax values were in the statement but not in `expected`. I added them.
  - I removed the "at least 11 of 13 Kmax" pass threshold, which the paper doesn't give. Every value must now be within tolerance.
- **spike-sorting-quality**: the writer had decided without a source which spikes count toward the ISI percentage. It is now named as open, with two readings: the whole recording, or trials only.
- **firing-rates-by-period**: the criterion judged the ten printed quartiles, but `expected` lacked them. I added them.
- **maintenance-neurons-correct-vs-incorrect**: the criterion now says the paper never mentions equalizing trial numbers, and that 100 subsamples is a standard choice, not the paper's.
- **fig4a-dpca-separates-set-sizes**: the statement says set sizes separated early in the trial. The criterion now says this is shown and not judged, because the paper gives no measure for it.
- **fig4b-speed-lowest-in-maintenance** and **fig4c-distance-largest-in-maintenance**: averaging speed and distance over set sizes, pairs and time is now marked as a reading. The paper doesn't define it.

All the quotes, statistics and the other expected values match the paper. Every main finding has a claim, and none of them comes from outside this paper.

**Still open** (recorded under `checks`)
- **Figure numbers**: I couldn't render the PDF in this run, so these values, which the writer read from figures, are unchecked:
  - amygdala 16 (Figure 2c)
  - 17, 19 and 10 (Figure 3b)
  - entorhinal decrease 2 and amygdala increase 1 (Figure 2d)
  - p = .006 for hippocampus, and the amygdala accuracy of about 62% (Figure 4d)

  The counts do agree with the totals in the text: 46 test neurons, half of 92 maintenance neurons.
- **Permutation details**: the paper doesn't give the scrambling schemes, the number of permutations, or the permuted ANOVA's scheme. The file states one reading for each. The two papers the Methods cite for these methods, Boran et al. 2019 and Kaminski et al. 2017, are not available here and weren't read.

Nothing was committed or pushed.
