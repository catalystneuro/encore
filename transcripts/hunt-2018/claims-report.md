I wrote `claims/hunt-2018.yaml`: 40 claims, all with quotes, 39 with criteria and 16 statistics entries. The quote checker passes every quote. It flags two "value not found" problems, which I checked by reading and are not wrong: the extracted text prints "p<1*10 7" for p < 1e-7 (the minus sign was lost). I did not commit.

**Text read.** The version of record (PMC6331040, open access) as text: main text, Discussion and Online Methods. It also had the supplement (Supplementary Figures 1 to 12, Supplementary Table 1 and the Supplementary Note). The data descriptor was read only to learn what the dataset holds.

**Missing from the paper text:**
- **Main figure legends.** The flattened text has no legends for Figures 1 to 8, and no PDF of the main article was supplied. So each figure's tests, significance levels and sample sizes are unknown. Claims on main figures rest on the Results and Methods sentences that cite them, and the gaps are named as open details.
- **Code.** The paper's MATLAB scripts are stored inside the CRCNS dataset, so I did not read them and record no commit. The author may settle open details from them.
- **The Figure 8 cue 1 regression.** The Online Methods do not describe this model.

**Coverage.** The claims cover:
- behaviour: session and trial counts, choice accuracy, cue weights, information sampling biases (Figure 2a/b);
- neuron counts;
- the cue 1 RSA: five templates, consistency across monkeys, the top/bottom split, t75 latencies and their order, the alternative template;
- OFC value subspaces (Figure 5a to 5k, Supplementary Figures 6 and 7);
- the ACC belief-confirmation subspace and the reaction-time, ramp and action projections (Figure 6a to 6e);
- single-neuron fractions (Figures 7 and 8);
- regressor correlations (Supplementary Figure 9).

**Open details and the readings named:**
- **O1, Fisher r-to-Z test:** two-sided, or one-sided in the predicted direction.
- **O2, significance level for counting single neurons:** p < 0.05 or p < 0.01.
- **O3, time bin for single-neuron tests at cues 2 and 3:** 250 ms after the cue (as Figure 5) or 300 ms (as Figure 6a).
- **O4, how trials are split for the Figure 6 projections:** the Methods say odd against even trials; the Results say 100 random half splits.
- **O5, the five reaction-time bins:** quintiles within each session, or quintiles of all of a monkey's sessions.
- **O6, the firing rates projected:** raw rates, or rates z-scored per neuron.
- **O7, the "T-statistics of contrasts" used as weights:** the mean of the T-statistics, or the T-statistic of the mean coefficient.
- **O8, the RSA permutation test:** one-sided or two-sided.
- **O9, trials used for RSA and the Figure 8 regression:** all completed option and attribute trials, or only those with 3 or more cues viewed.

**Open details for single claims:**
- **Figure 8 model:** its regressors (with or without main effects) and its window (100–500 ms, or the bin at 250 ms or 300 ms).
- **Figure 7a trial type:** the text says attribute trials but cites Figure 5d/e, which are option trials. Both are named.
- **Accuracy measures:** how trials of equal value count, and how value is judged from the pictures observed.
- **Cue weights:** what "approximately equal weight" means (overlapping intervals, or a Wald test).
- **Value difference:** true expected value, or that implied by cues 1 and 2.
- **Latencies:** the RSA sliding-window step (10 ms or 1 ms).
- **Supplementary Figure 9:** whether the mean r² is over sessions or over neurons.
- **Figure 6:** the projection windows, and how the action projection is signed.
- **Figure 5g–j:** which pairs of regressors each panel shows.
- **Figure 2b:** whether the monkeys are pooled or analysed separately.

**Inconsistencies recorded in the claims.** Supplementary Table 1 sums to 198 ACC, 195 OFC and 156 DLPFC units, which are the counts before the below-1 Hz exclusion even though its caption says above 1 Hz. It also lists 29 and 24 sessions, against the 32 and 25 behavioural sessions. The Methods and Results label the Figure 6 panels differently.
