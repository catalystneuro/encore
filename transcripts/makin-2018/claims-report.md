I wrote `claims/000129/10.1088-1741-2552-aa9e95.yaml`, and the quote checker passes it: 29 claims, 29 quotes, 12 statistical values, 0 problems. Nothing is committed.

**Text read:** the version of record, from a PDF supplied by a person. It has Methods, Results, Discussion and figure legends, and the paper has no supplement. Two equations are garbled in the extracted text: the ridge penalty in eq. 10 and the Wiener filter order sweep. No PDF renderer was available here, so I used the paper's code to settle both.

**Code read:** github.com/jgmakin/rbmish at commit 700062f (MATLAB). It has all the decoders, the data loading, the session lists and the statistics code. Its session list gives exactly 37 and 10 sessions for monkeys I and L, matching the paper.

**Claims:** all 29 have quotes, and none uses `inferred`.
- 13 claims carry statistics: bootstrap tests, one F-test, and stated non-significance bounds.
- 7 claims carry expected values with 10% tolerances.
- Every claim has a criterion except `fig2-position-dynamic-gain`, which rests on its expected value alone.
- One claim, `fig4-task-similar`, uses data from elsewhere: monkey C's sessions from Dyer et al., which the paper cites only as a bioRxiv preprint.

**What the dataset can test:** the archive describes one M1-only session of monkey I, with sorted units, and does not name the session. Nearly all the paper's findings are averages or bootstrap tests over 49 sessions from three monkeys. Only `fig4-vel-acc-every-session`, `units-monkey-i` and the per-session parts of a few others can be checked on one session. The paper's unit counts include an unsorted "hash" unit per channel; the archive describes sorted units only. The rest of the Sabes lab data is deposited at Zenodo (doi:10.5281/zenodo.583331).

**Details the paper leaves open, with the readings named:**
- **Kinematics:** the Methods use fingertip position, low-pass filtered at 10 Hz and subsampled per bin. The code uses cursor position, has the filter commented out, and averages within each bin. The Methods reading is the main one and the code's is a variant.
- **Bootstrap sidedness:** the Methods say only "the location of zero". The code is one-sided, and I followed it.
- **Bootstrap pooling:** the Methods describe 49 session differences, with x and y averaged per session. The code pools x and y as 98 entries. The Methods reading is the main one and the code's is a variant.
- **"Nearest competitor"** (the 0.14, 1.60 and 1.2 dB gains): (a) the best other decoder for each variable, or (b) the UKF throughout.
- **The correlations in Figure 7** (ρ = 0.999, 0.95, 0.98, 1.000): the code does not compute them. Readings are a Pearson correlation of mean SNR against (a) the fraction of neurons or (b) log2 of that fraction.
- **"Leading decoders" in Figure 5:** read as rEFH (+KF), UKF and KFobs, shown with and without KFobs.
- **Standard-normal rEFH variant:** the Results say counts were standardized; the code applies 2√(R + 3/8). The Results version is the main one and the code's a variant.
- **Garbled equations:** the code gives the ridge penalty as (N_units/N_samples)^(10/3), and the Wiener filter sweep as 1 to 0.4 s of history bins with penalty 0 to 4000 in steps of 800.
- **Thresholds I set where the paper gives words only:** "little effect", "about equal", "nearly twice" and "rise with bin width" have numeric bounds that I chose, and each criterion says so.
- **Random seeds:** none are given; I specified one training run per session with a recorded seed.

**Missing from the paper that a claim needed:**
- The paper does not say how ρ in Figure 7 was computed (the readings are above).
- The 10% tolerance on correlations near 1 extends past 1, so the ordering condition in that criterion does most of the work.
- Monkey C's data has no archive identifier, only the preprint.
