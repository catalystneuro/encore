I wrote `claims/001642/10.1523-jneurosci.1962-14.2015.yaml`, and the quote checker passes it: 32 claims, 32 quotes, 40 statistical values, 0 problems.

**Text read.** I read the version of record (J Neurosci 2015, open access on PMC as PMC4339358): Methods, Results, Discussion and figure legends. The paper has no supplement and links no code, so I read no code, and there was no PDF.

**What is missing from the text.** All the display equations in the Methods are images on PMC and did not come through. That covers the decision-tree probability, the normalized likelihood, the Markov and DFQ update and choice equations, parameter drift, mutual information, BIC and regression model (2). I could not read figure panels either, in particular the windows drawn in Fig. 6A. Where a criterion needs one of these, it names the readings the surrounding text allows.

**Claims.**
- **Quotes:** all 32 claims have one.
- **Statistics:** 21 claims record them, mostly χ2, Mann–Whitney, "paired-Mann–Whitney", binomial and Wilcoxon signed-rank tests.
- **Expected numbers:** 6 claims (trial counts, trials per block, neuron counts, the >60% proportions and the actor-critic likelihood of 0.5080).
- **Criteria:** all 32 have one.
- **Data:** every claim uses the dataset's own recordings; the paper relies on no outside data.

**Details the paper leaves open, with the readings named:**
- **Mutual information:** how firing is cut into four levels, and whether there is a bias correction, are referred to Ito & Doya 2009. Readings: quartile levels with no correction, or the same minus the shuffle mean.
- **Fig. 4 EASH smoothing:** 10 ms, 30 ms or none.
- **Trials in "whole trials":** with or without the extinction trials.
- **χ2 tests:** with or without Yates correction.
- **"Mann–Whitney" on proportions:** read as the test on per-neuron 0/1 coding indicators.
- **Fig. 8 regression windows:** real time or the EASH time axis.
- **Trials in the regression:** free-choice trials only, or all choice trials.
- **Regression model size:** the text says six variables and 2^6 models but lists eight terms, so the full set of eight is named as a reading.
- **FQ model:** the update and choice equations are written out from the text's description; initial values and particle-filter priors are open.
- **Model comparison:** how the 101/101 session split was made (alternate sessions, or a seeded random half), and whether the normalized likelihood is taken per session.
- **Trial counts:** whether error trials are counted. The four categories sum to 74,216, not the 78,107 stated. For trials per block, whether the last unfinished block of a session counts.
- **Extinction test:** which contingency table the χ2 uses (per tone, or pooled).
- **Fig. 6:** the state-coding window (only drawn in Fig. 6A), and the chance level for the binomial tests (read as 0.01).
- **Figs. 9 and 10:** how the last 20 trials of several blocks are combined (pooled, or averaged per block); "500 ms before cue presentation" (read as before cue offset, with cue onset as a variant); how fixed and free blocks are combined; and whether "paired-Mann–Whitney" means a signed-rank or an unpaired test.
- **Stay/switch analysis:** last 20 trials per block, or all free-choice trials.
- **Actor-critic model:** the paper does not specify it, so that claim may be blocked as `methods_underspecified`.

**Other gaps a claim needed.** The model comparison used 202 sessions, more than the 86 recording sessions, and the paper does not say where the rest come from. The ">60%" proportions are stated only as bounds. Fig. 6E states no result, so it has no claim.

**Paper errors noted in the file's opening comment:**
- The Results cite "Fig. 7F" for state-value neurons; this should be Fig. 8F.
- The Discussion cites "Fig. 8C" for action-value neurons; this should be Fig. 8E.
- The Methods define E7 as "2 s after E8"; this should be E6.

Nothing is committed.
