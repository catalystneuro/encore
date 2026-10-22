I've written `claims/001357/10.1523-jneurosci.1893-23.2024.yaml`. The quote checker reports 0 problems (27 claims, 27 quotes, 12 statistical values). Nothing is committed.

**Text read:** the version of record, from the PDF supplied by a person and extracted as text: main text, Materials and Methods, and figure legends. The paper has no supplement, so none was needed, and I didn't need to open the PDF.

**Code:** the paper links no analysis code and has no code or data availability statement. The analyses were in the authors' own MATLAB code, which is not public. The only link is to the stimulus software, pype (github.com/mazerj/pype3, HEAD 49056d6f). It settles no analysis detail.

**Claims:** 27 in all.
- **Quotes:** all 27 have one; none needed an `inferred` note.
- **Statistics:** 10 claims record the paper's tests.
- **Criteria:** all 27 have one.
- **Outside data:** 4 claims are `with_inputs` because they need the shape images and curvature descriptions of Pasupathy & Connor (2001), which this paper neither prints nor deposits. They are the Gabor (orientation × spatial frequency) fits, the two angular position × curvature model claims, and the simulation. The simulation is recorded so the finding is covered but can't be tested on the dataset.
- **Recorded data:** the other 23 use the recordings.

**Details the paper leaves open, with the readings named for each:**
- **Reliability cut-off:** "confidence limit >0.5" is read as (a) the full width of the bootstrap interval or (b) its half-width. The interval's level isn't given; I used 95%, the level the paper uses for its regressions.
- **Which contrast gives the population Isimilarity:** dark, bright, or significant at either.
- **Whether the 344 neurons also need a negative slope:** yes or no. The counts (344 + 1,504 = 1,848) suggest the count is of significant intercepts alone.
- **Isimilarity–Ssimilarity correlation type:** Pearson or Spearman.
- **Median invariance of 0.64:** the median over all neurons, or the median of per-penetration medians (the Methods and the Results say different things); unreliable values either left out or counted as 0.
- **Welch's test (same versus different sessions):** Pearson or noise-corrected correlation; dark, bright or both contrasts; cross-session pairs from all sessions or within one monkey only.
- **Recording density (Fig. 5E):** neurons per µm (the axis label) or µm per neuron (the legend). This is an inconsistency within the paper.
- **The ~20% level (shape and texture):** the median of per-penetration percentages, or the pooled percentage, over penetrations with more than 30 neurons.
- **Gabor filter bank:** frequencies, envelope, phase and pooling aren't given. Readings: a steerable pyramid, or quadrature Gabor energy.
- **Angular position × curvature model:** the fitting procedure and the contrast used aren't given; significance as one- or two-sided; a session counted when both its mean and standard deviation fall below the null limit, or either.
- **Position test (Fig. 12B):** the comparison is with the position test's center position (the Results text) or with the main shape test (the figure's axis).
- **CSD:** the smoothing width, which column of contacts, and how the sink is picked. Readings: the earliest sink, or the largest one.
- **Peak responses in M1p12:** baseline-subtracted or raw.
- **Penetration names (M2p6, M1p12, M2p9, M2p28, M2p51, M1p5):** how the numbers are assigned isn't said. Readings: order among shape sessions, order among all sessions, or the dataset's own label. Each is accepted only when the neuron count matches the paper's.

**Missing from the paper that claims need:**
- **The 18 gyral penetrations:** they are identified only in figures (Fig. 5A, Fig. 8B), with no session list or grid coordinates. "Consistent" also has no test; I named two readings.
- **Position-invariance examples (Fig. 11):** the paper gives no measure of similarity across positions, so the criterion's measure is a stated reading, not the paper's.
- **The simulation (Fig. 13):** peak amplitudes and step sizes aren't given.
- **CSD claim:** it needs the LF signal. The archive's summary lists only units and electrode groups, so the dataset may not hold it.
