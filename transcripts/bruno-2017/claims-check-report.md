The claims file is ready for an attempt. I made eight changes and left two points open, and a `checks` entry at the end of the file records all of them.

**Checker result** (after my changes): `30 claims, 30 quotes, 0 statistical values, 0 problems`. Before my changes it read the same, except for 1 statistical value, which I removed (see fig5b below).

I checked the claims against the full text and against the paper's code (mdhumphries/AplysiaAttractorAnalysis, commit e5f28e9, cloned to a temporary folder). Most of the code details the claims cite are accurate: the kernel and PCA settings, the recurrence parameters, the eigenvalue bands and period formula, the permutation and weighting code, the 0.2 threshold for returning to the same manifold, the noise-model threshold, and the mismatched pairs in the rate-change analysis.

**Changes, by claim**
- **fig5b-period-changes**: removed the statistics entry (p < 0.01). In the Figure 5B legend that p-value only marks which responses count as changing, so it is a counting threshold, not a result. The criterion still uses it.
- **fig1d-slow-oscillation**: the expected quantity now says 0.1 Hz is an upper bound (the paper says "≤ 0.1 Hz"). It was written as a point value, which disagreed with the criterion.
- **fig3c-same-manifold**: the control now follows the Methods formula, max{min d(A,B*), min d(B,A*)}, which shuffles both programs in turn, as the code does. The file had said only one program is shuffled.
- **fig3c-same-manifold, fig3f-pairwise-similarity**: the required count went from 25 to 26 of 30. The expected value is 28 with a tolerance of 2.8, so 25 fell outside it.
- **fig3s1a-common-axes**: also 26 of 30, since the legend says the results are the same as Figure 3C.
- **fig2ef-periodic-recurrence, fig4bc-stable-spiral**: the criteria now say their counting rules are set by the claims file, not the paper ("more than half" for "many"; two of three responses per preparation).
- **fig6d-decode-p10**: added histories up to 100 ms as a variant. The Results say "up to 100 ms", while the Methods say 50 to 200 ms.
- **fig6s1-no-p10-motorneurons**: the criterion only tested consistent locking across two programs. The paper also says no neuron comes close to 1 at any delay, so it now requires that no neuron reaches 0.9 in any program.

**Open**
- **fig2b-dimensions and fig6s2-dimensions-p10**: the paper gives 4 to 8 dimensions for all 30 responses, but 3 to 5 for the nine recordings with P10 activity. The paper's "generally" allows this, so both claims stand as written.
- **Gaussian width**: the extracted text reads median ISI / 12, and with no PDF of the paper I could not check whether a square root was lost. The criteria already list both readings and the code's choice (the median ISI itself).

Nothing was committed or pushed, and only the claims file changed.
