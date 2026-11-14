I worked through every point in the verifier's report. Three outcomes changed. The final clean `python tools/entry.py all entries/nishimoto-2011` passed, and `check` reports 0 errors. That clean run was made before I edited `README.md` and the `runtime_minutes` values, so the next run will execute the notebooks again. Nothing is committed.

**Outcomes that changed**
- **fig3b-mean-prediction: not reproduced → reproduced (assumed).** The verifier's main point was that the cost of pooling the weights over space had never been measured. I measured it in a new notebook, `finer_pooling.ipynb`, which refits the main model on a finer pooling (1465 regressors instead of 763). Every neuron improves (45 of 45, +0.070 on average), and the mean r goes from 0.448 to 0.518, inside the 0.468–0.572 band. On three neurons, an even finer pooling (3085 regressors, with every simple cell) did not improve further. The outcome rests on the finer pooling, which is still smaller than the paper's model.
- **natural-movie-control: partially reproduced → reproduced.** With the finer pooling, both means are in tolerance (natural 0.523, motion-enhanced 0.563) and p = 0.43.
- **fig7b-pattern-index: not reproduced → reproduced (assumed).** The paper doesn't say how its simulated plaid responses were treated. Treating the model outputs as firing rates, which can't be negative, puts 64% of neurons inside −6.6 to 2.2 and none above 2.2. Adding Poisson noise also passes, in 16 to 20 of 20 random draws per setting. The raw outputs still fail, so I recorded this as an assumption, citing the passages, and added it to the question for the paper's authors. A model output that was exactly a pure component cell used to divide by zero; it now gives a finite index.

Two outcomes were kept, but are now judged on the treated responses: fig7c-hv-pattern-correlation stays not reproduced (r at most 0.298), and fig7c-no-corr-prediction-pattern stays reproduced (p = 0.733).

**Outputs added for the verifier's other points**
- **Boosting:** no fold reached the 20,000-step cap. Raising the patience from 50 to 500 steps leaves the mean r at 0.449.
- **Blocked explainable-variance claim:** the notebook now lists everything in one file, and `trange` is empty in all 45 files. There are no single repeats, so the block stands.
- **Validation sets:** all 59 are contiguous and have no missing responses.
- **ct0028 and ct0030** (the two neurons with 10 repeats): r is 0.278 and 0.409.
- **Repeat counts:** a stricter check gives the same 10 to 33 repeats.
- **ct0133:** the mean r without it is 0.450.
- **Complex vs simple cells:** I reran the complex-only and simple-only fits with the finer pooling, and with all simple cells on three neurons. The outcome stays reproduced.
- **Remaining smaller points:** the backward-looking delay window, the plane tie-breaking and the approximate Gram matrix are now stated in the record.

**Not done**
- **Null model on one neuron's movies, all four combinations.** I ran it, but it pushed the main notebook to 66 minutes, over the 60-minute limit. So it stays at one combination, and the record says why.
- **Figure 2B claims (the 12-model comparison) and Figures 6–8.** These still use the coarser model. Refitting all 12 models with the finer pooling didn't fit in the time, and the record notes their effect sizes may be underestimated.
- **No reader questions.** The verifier reported no place where the claims file misreads the paper, so I added nothing to `questions/nishimoto-2011.yaml`.

The main notebook took 59.1 minutes, just under the 60-minute limit; `finer_pooling.ipynb` took 26.5. The round is recorded under `verifications` in `attempts/nishimoto-2011-01.yaml`.
