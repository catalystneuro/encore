I've written the claims file: `claims/001641/10.1523-jneurosci.6157-08.2009.yaml`. The quote checker passes it with 0 problems.

**Text read**
- **Main text:** the version of record, open access on PMC (PMC6666589), stored in `paper/10.1523-jneurosci.6157-08.2009.txt`. It includes the Methods, Results, Discussion, figure legends and Tables 1 to 3.
- **Supplement:** only the supplemental Methods (4 pages, the particle filter). Its equations are garbled in the extraction, so I used only its words.
- **Code:** the paper links none, so none was read.
- **PDF:** there is no PDF of the main text, so no figure panel could be read.

**What the file holds**
- 46 claims: 43 have quotes and 3 have an `inferred` note (Tables 1 to 3).
- All 46 have a criterion, and 28 have expected values.
- 13 claims carry statistics, 23 tests in all.
- All claims use the dataset's own data; the paper uses no outside data.

**Details the paper leaves open** (O1 to O15 in the opening comment; each criterion says which ones it uses)
- **O1, Q-learning update:** the equation is missing. Either κ1 and κ2 are scaled by α1, or they are added without it. The choice rule is the logistic of QL − QR, taken from equation (1) of the supplement.
- **O2, normalized likelihood:** read as the geometric mean of the per-trial likelihood.
- **O3, training/test split:** alternate sessions over all rats, alternate sessions within each rat, or a seeded random half. Checked against the reported 19,986 and 19,186 trials.
- **O4, parameter search:** a grid on the step sizes seen in Table 2, or a continuous optimizer.
- **O5, parameter drift:** α left unbounded, or clipped to [0, 1].
- **O6, first d trials of a session in the Markov model:** predicted at 0.5, or left out of the score.
- **O7, choice histories:** confined to one block, or running across blocks within a session.
- **O8, what the Mann-Whitney tests of choice probabilities rank:** each trial's 0/1 choice, or per-session probabilities.
- **O9, Mann-Whitney tests of neuron percentages:** run on each neuron's 0/1 coding indicator. This is the only reading the text allows.
- **O10, chance level of the binomial test:** 0.01, or 0.01 × 0.99.
- **O11, Wilcoxon test of preferences against 50%:** signed-rank on each neuron's difference in spike counts, or a sign test.
- **O12, mutual-information windows:** centred on, ending at, or starting at each time point. The shuffled events for the significance threshold are drawn with p = 0.5, or with the real event's frequency.
- **O13, which QL and QR estimates:** predictive mean or posterior mean, with the median split taken per session or over all sessions.
- **O14, error trials in the state-coding test:** excluded or included.
- **O15, the firing-rate period:** the whole recording, or the task span.

Some criteria also name readings for denominators, the residual-error definition, and whether mirrored sequences are summed or averaged.

**Choices to know about**
- **Tolerances:** the Fig. 5 normalized likelihoods get ±0.005 instead of the default 10%, because 10% would accept any model at chance. Neuron percentages are judged within ±2 neurons where 10% is less than one neuron. Both reasons are written in the file.
- **Fig. 4 representative sessions:** the paper does not identify them, so the claim is tested as whether such episodes exist. The run lengths and the 25% margin are mine because the paper gives none, and the criterion says so.
- **Inconsistencies in the paper,** noted in the opening comment:
  - It says the constant-parameter Q models are worse than the first-order Markov model, but its own numbers put F-Q and DF-Q above it (0.531 against 0.528).
  - The training and test trials sum to three fewer than the reported choice trials.
  - One sentence about Fig. 9 cites Fig. 8C,D.

**Missing from the paper**
- **Equations:** every display equation in the Methods is an image and is absent from the text, which produced O1, O2 and the regression and mutual-information forms.
- **Supplemental Data 1 to 3:** cited but not supplied. Two claims rest on them:
  - `suppdata1-choice-vs-q-difference`: its bins and model versions are unknown.
  - `core-shell-no-difference`: its tests are unknown, and it can only be tested if the dataset labels core and shell.

I did not commit anything; the other untracked files in the working tree were there before this run.
