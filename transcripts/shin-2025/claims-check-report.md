The file is fit for an attempt; the last check marks it `ready: true`. Nothing was committed, and only `claims/000248/` was changed.

**Checker result:** `40 claims, 40 quotes, 79 statistical values, 1 problems`. The one problem is the fig2d p-value 7e-06. The paper prints it as "P = 7.0 × 10 −6", so the recorded value is correct and I left it.

**Changes, by claim**
- **fig2d-npx-ccg-hva-input:** the Gaussian smoothing reading now also gives the s.d. of 5 ms, taken from the 25 ms kernel the paper uses for PSTHs (Extended Data Fig. 4b legend).
- **ed2b-npx-fixed-gaze:**
  - The 8-degree threshold was called the main method, but the paper gives no way to convert camera pixels to degrees. The 8 degrees and the code's 20 pixels are now two equal readings.
  - The 95th-percentile shuffle cut-off was written as if it were the paper's test. The paper shows the shuffle null with no threshold, so the cut-off is now recorded as a standard choice and a deviation, and the match is also compared with fig1g's 78.6%.
- **ed2a-npx-gaze-confined:** the paper names no test. The old rule needed 20 or more per-session tests all to fail, a rule the first reader made up that would likely fail by chance. It now decides on a Friedman test across sessions (the test the paper uses for pupil area in Extended Data Fig. 2g). The per-session tests are kept as a variant, and the criterion says any test here is a reader's choice.
- **ed4c-2p-ic-encoder-rf-anywhere:** the comparison is borrowed from Extended Data Fig. 4g, which covers different sessions (images scaled up 1.5 times). The criterion now says so and records it as a deviation.
- **ed7b-2p-xre-inference:** added the non-significant results for AL, PM and AM to the statement and statistics (p = 0.5, 0.4375, 1.0), and gave the criterion its own rule.
- **fig4b-2p-ic-encoders-only:** the statement says both decoders tell IC from LC images, but the accuracy-against-chance tests were missing. I added them (p = 1.8e-5, 1.8e-5, 5.6e-5) and put them in the criterion.
- **New claim, ed6cd-npx-ic-encoders-all-areas:** the paper finds IC-encoders in every visual area (Extended Data Fig. 6c,d), and no claim covered that.

**Still open** (each recorded in `checks`)
- **supp3-decoder-types:** it rests on Supplementary Fig. 3, which is not in `paper/`, so its criterion cannot be checked against the paper.
- **ed3-2p-robust-gap-mapping-contrast:** it uses the same 95th-percentile cut-off, which the paper doesn't give. I left it because those 2p data are not in this dandiset.
- **The paper's code:** neither the first reader nor I could read the Code Ocean capsule the paper links. The criteria that cite the GitHub repositories (github.com/hs13) remain unverified against that code.
- **fig1e-npx-exclusive-center:** the receptive field mapping block has no gray-screen gaps between trials, so the paper's comparison against gray-screen trials cannot be run as written. The two readings in the criterion stand.

The other claims match the paper: statements, sources, statistics, expected values and the main findings are covered, and nothing comes from the preprint.
