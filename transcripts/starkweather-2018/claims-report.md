I wrote `claims/starkweather-2018.yaml`. The quote checker passes on every quote. It still lists 16 p-values as "not found": in each case the extracted text garbles the exponent (it prints "× 10⁻¹⁶" as "3 10�16"), and I checked all 16 against the text by reading. Nothing is committed.

**Text read.** The version of record (supplied by a person), with the STAR Methods and the supplement (legends of Figures S1 to S8). Nothing the claims need is missing. The PDF could not be rendered because poppler isn't installed, so the numbers that appear only inside figures were read from the extracted text:
- **Figure S4B cell-type counts:** these sum to the reported 761 neurons.
- **Figure 5 slope variances:** I assigned them to task and drug by their ratios, which match the reported F-ratios of 0.51 and 0.59.

**Code.** The paper links github.com/cstarkweather; its repository for this paper (Starkweather2018, commit d667730) holds only the belief-state TD model, with no code for analysing the recordings. Where the code and the Methods differ, I followed the Methods and named the code's setting as a variant:
- 50 simulations (code: 10).
- 60% of simulations with an impaired belief state (code: all intact as committed).

**Claims.**
- 31 claims, all with quotes, carrying 46 statistical values.
- 30 have a written criterion. The exception is `fig2-kord-suppresses-mpfc`, which is judged on its expected value alone.
- Expected values are given for 15 claims. Neuron counts have zero tolerance, and counts of 0 to 9 have a tolerance of one neuron.
- 8 claims are absences, judged on the paper's own test.
- 3 claims are about the model. They need no recordings, and I left them at the default `data: dataset` because the schema has no value for model-only claims.
- 7 claims rest on data the vta-1 description does not list (mPFC units, licks, non-dopamine VTA neurons, the two mice without KORD).

**Details left open, with the readings named**
- **Pre-reward window:** 0–400 ms before reward (Methods) or 0–200 ms (Figure 4A legend).
- **Baseline subtraction for slopes:** trial by trial, by the neuron's mean baseline, or none.
- **Free-water lick criterion (≥4 licks):** applied where lick data exist, or all free-water deliveries used. For normalised responses, I made the ratio of spike counts the main reading and the ratio of rates a variant.
- **Time × task × drug ANOVA (error df 1347):** the df fits neither neuron counts nor trials. Readings are one mean per neuron and ISI, or single trials.
- **Odor C vs latest odor A (F(1,41)):** with 41 neurons one would expect F(1,40). Readings are the test on neuron means or on trials.
- **Timing-impaired model:** Weber fraction drawn from 0.5–1.5 (Methods) or fixed at 0.56 (Figure S7D).
- **Belief-impaired model:** impair task 2 only, or every task as the code's flag does.
- **Standard choices where the paper is silent:** auROC bin width and baseline (Figure S1E, S4), the sigmoid form for the lick halfway time, the lick baseline, the cell-type test (chi-square), and the test in Figure S5D (rank-sum, Bonferroni).
- **No threshold given** for "flattened" or "abolished" in the model; those are judged against the intact model's run.

**Inconsistencies in the paper, recorded in the claims**
- For the effect of task on slopes, F(1,163) = 2.2 cannot give p = 1.7e-5, so that claim is judged on p.
- Task 1 saline post-reward F is 12.6 in the Results and 13 in the legend.
- For the SalB odor C vs B comparison and the omission dips, the legends print F(1,40) although 47 neurons were recorded under SalB; the Results give F(1,47) for the dips.
- The task 1 vs task 2 licking test is F(1,77) in the Results and F(1,76) in Figure S3.
