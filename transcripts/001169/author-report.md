I've finished steps 1 to 5 for dandiset 001169 and run `handover` (step 6); nothing is committed. `entry.py check` reports 0 errors, and `entry.py all` passed both notebooks from a clean environment. I used the full text, which is open access (PMC10663503), saved under `paper/`.

The dandiset is pinned at 0.260825.1909. The paper cites no DANDI version, and this is the only published one; the draft has the same assets and size. The header of `reproduce_mah_2023.ipynb` says so.

### 1. Outcome per claim (26)

| Claim | Outcome |
|---|---|
| dataset-counts | reproduced |
| zenodo-link (with inputs) | partially reproduced |
| fig1f-wait-time-block | reproduced |
| fig1i-initiation-block | reproduced |
| figs2-unrewarded-drive | reproduced |
| figs12-no-sex-difference | reproduced |
| fig2a-wait-time-converges | reproduced |
| fig2b-initiation-previous-block | not reproduced (wrong sign in my criterion, see point 1 below) |
| fig2cd-regression-kernels | reproduced |
| fig2e-tau-differ | reproduced |
| fig2f-tau-uncorrelated | reproduced |
| fig2gh-fast-slow-groups | reproduced |
| fig2j-wait-time-previous-reward | reproduced |
| fig2k-initiation-previous-reward | reproduced |
| fig2l-sensitivity-differs | reproduced |
| fig3c-catch-probability | reproduced |
| fig3j-model-comparison | reproduced |
| figs9-misinference | reproduced |
| fig3l-inference-quality | reproduced |
| fig3h-dynamic-learning-rate | blocked, methods_underspecified |
| fig4a-wait-ratio-learning (Zenodo data) | partially reproduced |
| fig4bc-regression-learning (Zenodo data) | reproduced |
| fig4de-overshoot-learning | blocked, data_missing |
| fig5b-precue-offer | reproduced |
| fig5c-precue-previous-reward | reproduced (fragile) |
| fig5d-precue-previous-block | not reproduced (same wrong sign as fig2b) |

Several numbers match the paper exactly, for example 38 rats in Fig 2j, p = 1.82e-49 in Fig 1i and p = 0.003 in Fig 3l.

### 2. What was found about the dandiset
- **Completeness:** it holds 291 rats and 23,034 sessions, converted from the paper's processed data on Zenodo. 273 of 291 rats match that data exactly, trial by trial.
- **Missing sessions:** 9 sessions (3,645 trials, 0.035%) in 8 rats are missing.
- **Duplicate:** one session of rat L011 is deposited twice (a second copy with a `-x` suffix).
- **Session order:** 10 rats have their sessions in a different order from the Zenodo data.
- **Raw events:** the raw Bpod events agree with the processed initiation and wait times to about 1e-11 s.
- **Missing catch probability:** the processed table has no catch probability, because the conversion code misspells `prob_catch` as `prob_cacth`. The raw trials table has the same values.
- **Pre-cue sessions:** the 762 sessions of the Figure 5 pre-cue task are mixed into the main data. Only a task argument, `center_port_cue`, marks them, and the Methods don't mention it. Sounds are stored without their identity, so the raw data can't confirm that flag.
- **Metadata:** training stage is coded 9 without saying it is the paper's stage 8, ages are missing for 275 rats, and 456 sessions start with a high or low block although the Methods say every session starts mixed.
- **Data elsewhere:** the early sessions behind Figure 4 are only on Zenodo. The raw per-session structs behind Fig 4d, 4e and Fig 5 are not public anywhere.
- **Paper and code:** I recorded paper inconsistencies (two different male/female counts, two different r values for Fig 2f) and several places where the code differs from the Methods.

### 3. Where the protocol was unclear, wrong or missing something
1. **A criterion written wrong before the analysis.** For fig2b and fig5d I assumed the dependence on the previous block keeps its sign. The data show it reversed, which is the incentive-contrast effect the paper itself describes. The protocol only covers ties, not a criterion that turns out mis-specified. I judged by the letter (not reproduced), explained it in the notes, and left any change to the revision after verifier round 1.
2. **Methods versus code versus "several readings".** For fig2k the Methods say trials offering 20 uL, the code uses all mixed-block trials, and the paper's p-values match the code. The two rules point different ways. I used the Methods as the main result and showed the code as a variant.
3. **The paper's own deposit as outside data.** The Zenodo data is what the dandiset was converted from. I made a standalone `with_inputs` link claim that nothing depends on, and tested Figure 4 as `elsewhere`, although that data partly overlaps the dandiset.
4. **Tolerances.** I used 0 for exact counts and ±2.5 points for "~10 percent", each with a reason given in the claims file.
5. **"Stream, do not download".** Range-request streaming took about 5 s per file, too slow for 23k files. Each ~1 MB file is read whole into memory instead, never to disk; the notebook header says so.
6. **Runtime.** The 10-minute aim isn't reachable: reading 23k files alone takes 9 minutes. The main notebook takes 18 minutes, under the 30-minute limit.
7. **Clock check.** The suggested decoding check doesn't fit behaviour-only data. I compared the processed times against the raw events on 24 random sessions instead.
8. **Ties at a percentile cut.** Fitting lambda on a grid left many rats tied at 0 and 1, so the 20th/80th percentile cut fell on the ties. I included the tied rats in each group and recorded it as a deviation.
9. **MATLAB optimiser not available.** I replaced fmincon with scipy and a grid search, and recorded it as a deviation rather than calling the method not runnable.

### 4. Runtime and failures
`entry.py all` took 20.5 minutes: 1,081 s for the main notebook and 141 s for the Figure 4 notebook.

Failures during development, all fixed before the final run:
- Zenodo returned 429 (too many requests) to parallel range reads, so the loader now reads them with one range request.
- A pickling error in the raw-event check.
- A NaN bug in the exponential fit.
- An empty percentile split before I handled the ties.

My first draft of the conclusions had placeholder numbers. All of them were rewritten from the executed outputs.

Two markdown corrections were applied identically to the source notebooks and the executed copies, without re-running, since markdown cells carry no outputs.

The root-level untracked entries (`.bashrc`, `scripts`, and others) are sandbox device mounts, not files I created. They should stay out of the commit.
