I wrote the claims file at `claims/000897/10.1038-s41586-024-07557-z.yaml`. `tools/claims_check.py` reports 22 claims, 22 quotes, 24 statistical values and 0 problems. Nothing is committed.

**Text read:** the version of record (open access, from Europe PMC, PMC11224022). It has the main text, the Methods and the Extended Data legends, and includes the 4 July 2024 correction. Three supplementary items were not in `paper/`:
- the Supplementary Information, which is discussion only;
- the Supplementary Tables, which give recording sites and probe layouts;
- the Source Data.

No claim depends on them, so I went ahead.

**Code read:** jazlab/Neupane_Fiete_Jazayeri_mental_navigation at commit 4bee109. It is MATLAB that starts from preprocessed tensors kept on Dropbox. Several steps load saved results instead of computing them: the null distribution for the periodicity index, Extended Data Fig. 3, the firing-rate versus slope comparison, and the Bayesian fits.

**Claims:** 22, all with quotes; 11 have statistics, 8 have expected values, and all 22 have criteria. Two are model simulations (Fig. 4b and 4d). The rest cover:
- **Behaviour:** Fig. 1b,c and the generalization result in Fig. 1e.
- **Periodicity:** the proportion of periodic neurons (231/614, 311/864), the peak lag near 0.65 s, and no periodicity in eye or hand.
- **Periodicity and behaviour:** navigation vs ITI, error vs correct trials, peak phases, and overshoot vs undershoot trials.
- **Distance coding:** onset/offset coding in single neurons and in the population, rate vs slope, and distance vs landmark.
- **Cross-correlations:** conserved between navigation and ITI, and across the other epochs.
- **Fano factor:** periodic in 341/614 and 378/864 neurons, and also present in neurons that are not periodic in rate.
- **Other:** motor-preparation neurons (Extended Data Fig. 10) and the Bayesian reset model (Fig. 4g).

**Details left open, with the readings named for each:**
- **What counts as periodic:** (a) the code's single threshold on the max-minus-mean score, or (b) the Methods' per-lag test at mean plus 2 SD. Surrogate trial lengths are either matched to each neuron's own trials or one global null.
- **Lag range for the periodicity index:** 0 to 1300 ms per the Methods (main reading), with the code's 100 to 1600 ms as a variant. The Gaussian-process null also differs: the code adds a mean rate and has no Poisson step.
- **ITI segments:** whether each starts at the beginning of the ITI or ends at the next trial.
- **Neurons for the error vs correct test:** periodicity within a 100 ms window around 0.65 s, or the code's index at the 650 ms lag.
- **Error trials:** the Methods' first attempt of trials with more than one attempt, with the code's `succ == 0` as a variant.
- **Phase bootstrap:** 100 subsamples (legend and Methods), with the code's 1,000 as a variant. The direction used per monkey is also a variant.
- **Onset/offset windows:**
  - Single neurons (Fig. 3b): 100 ms (Results) or 200 ms (Methods).
  - Population analysis (Fig. 3d): the Methods' windows, with the code's time-warped windows and its PCA denoising step as variants.
- **Distance ANOVAs:** the Methods' or the legend's windows, and a one-sample t-test on differences or a two-sample t-test.
- **Cross-correlation:** which session (the code's index in its session list, read as chronological order), and 20 or 25 neurons.
- **Fano factor:** the selection test (the legend's 300 to 900 ms window at p < 0.0001/20, or the code's test at 650 ms) and which direction counts.
- **Eye/hand bootstrap:** the code for it is missing, so two readings are named.
- **Bayesian fits:** with the Methods' lapse exclusion, or without it as the code does.

**Missing data or code a claim needed:**
- Fig. 1c,e and the Bayesian fits in Fig. 4g rest on behavioural training sessions. These came before the recordings, and the code says they are shared on request. The Fig. 4g degrees of freedom imply 78 and 102 sessions, against 17 and 15 recorded.
- The code never computes the Fano factor counts or the eye/hand result.
- The rodent data behind Extended Data Fig. 7 were shared privately, so I wrote no claim for it.

**Paper vs code:**
- The paper says the cross-correlation analysis used 20 neurons; the code uses 25.
- The Methods' ANOVA window is -500 to -300 ms; the code uses -400 to -300 ms.
- For monkey A, the printed Z(161) = -3.3 corresponds to p of about 0.001, not the stated p <<< 0.0001.
