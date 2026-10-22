I've written `claims/001354/10.1038-s41586-024-08282-3.yaml`. The quote checker passes it: 32 claims, 32 quotes, 5 statistical values, 0 problems. Nothing is committed.

**Text read**
- **Version:** the version of record from Europe PMC (PMC11666456, marked "corrected publication 2025"): main text, Methods, figure and Extended Data legends, and the Supplementary Information PDF (MOESM1).
- **Not read:** the Reporting Summary (MOESM2) gave no text when extracted. I did not read the correction notice (doi:10.1038/s41586-025-08607-w) on its own.
- **No main-article PDF:** so I couldn't see the figure panels. That means the plotted mean changes in Fig. 4i,j and the correlation table in Extended Data Fig. 12h are not available.
- **Code:** the paper links none; its scripts are "available upon request". Its Data availability statement says no separate datasets were generated, and the paper does not cite the dandiset.

**Claims**
- **Quotes:** all 32 claims have one; none needed `inferred`.
- **Statistics:** 6 claims carry them.
  - Three mixed linear model results: resting membrane potential (RMP) Z = 3.17, P = 0.0015; rheobase Z = 2.60, P = 0.0093; input resistance Z = 1.84, P = 0.0653.
  - Two p < 0.0001 bounds, from Extended Data Fig. 3a and 5c, where each legend defines only that one significance level. Those two are my reading of the legends.
  - A sixth claim records a test with no p-value.
- **Criteria:** 8 claims have one. All are slice-electrophysiology claims, the part of the paper the dataset holds: sample counts, mCherry preincubation, Fig. 4i, Fig. 4j, Extended Data 12b, 12c–d, 12e–f and 12g.
- **Untestable on this dataset:** the other 24 claims are on cell culture, imaging and biochemistry. They are kept as findings with quotes and numbers.

**Details the paper leaves open, with the readings named**
- **Window for the change "upon 2-min DCZ addition":**
  - W1: sweeps from onset to 2 min after, minus the pre-onset sweeps.
  - W2: sweeps from onset to the end of the recording, minus the pre-onset sweeps.
- **Unit of the mixed model** (treatment as fixed effect, random intercept per mouse):
  - M1: one change per cell.
  - M2: every sweep, with cell nested in mouse.
- **Action potential detection:**
  - A1: upward crossing of 0 mV.
  - A2: dV/dt above 20 V/s.
- **Steady-state window for input resistance:** the last 50 ms or the last 100 ms of the −100 pA step.
- **Sample counts:** whether they are taken before or after the exclusion of cells with initial input resistance above 500 MΩ. Both readings are named.
- **Preincubation mean:** whether it is over all recorded cells or the 26 analysed. Both readings are named.
- **Holding current in rheobase:** not stated whether it is included; it cancels in a change if constant, and the author is asked to check.
- **Unit typo:** the paper prints the exclusion threshold as "500 mΩ"; I read it as megaohms.

**Missing from the paper**
- **mEGFP intensities:** the Extended Data 12c–g claims need each cell's intensity, measured in freehand soma outlines that the paper does not publish. These claims can only be tested if the dataset holds the intensities or the outlines.
- **Effect sizes:** with no figure available, the expected values for Fig. 4i,j and Extended Data 12b rest on the reported Z values only.
- **Panel letters:** the text cites the T-cell results as Fig. 4l–o and the expression histogram as Extended Data Fig. 12h. The legends label them Fig. 4k–n and Extended Data Fig. 12i. I noted this in the sources.
