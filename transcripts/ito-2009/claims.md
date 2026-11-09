# 001641 · claims · run 39609056038

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/001641/ claims/001453/ paper/ 2>&1; grep -n "^#" docs/protocol.md
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "limit": 172
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-10`. Record this version in the attempt's provenance.
4	
5	This is what agents, or people, do to attempt a target and deposit the
6	result. A target is a dataset in a public archive and a paper it names. How
7	each archive's datasets are named, versioned and read is in
8	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
9	([pilot notes](pilot-notes.md)); the reasons for the rules are there.
10	
11	An attempt has three roles, each a separate run with a separate context:
12	
13	- The **reader** reads the paper and writes the claims file: every finding,
14	  and how each is to be tested, taken from the paper. A second reader checks
15	  it against the paper. Readers never see the dataset's data.
16	- The **author** tests the claims on the dataset. It reads the paper to
17	  understand the claims, but the claims file binds it: it cannot change a
18	  claim, and it asks a reader for any method detail the file lacks.
19	- The **verifier** checks the author's work and must not be the author.
20	
[... 152 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/001453/10.1016-j.cub.2025.04.027.yaml"
}
```

```
1	# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.
2	# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read
3	# from its Results, figure legends and STAR Methods. The version of record is not open access.
4	#
5	# When these criteria were written, the author had seen the data check only: the file list,
6	# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and
7	# the extent of positions. No claim's analysis had been run. The author had also read the
8	# outputs printed in the paper's own analysis notebook (Fig1-S1.ipynb, GitLab commit 33a5c29),
9	# which include per-stimulus median speeds and angular velocities and its statistics.
10	#
11	# The dandiset holds only the freely swimming tracking data of Figure 1 and Figure S1. Its
12	# stimulus codes 0 to 20 carry no names. The names come from the paper's code and from the
13	# stimulus software's protocol file (see stimulus-code-link), so the claims that need them
14	# use outside data and depend on that claim.
15	#
16	# Method choices fixed here, from the paper's Fig1-S1.ipynb where the Methods are silent: a
17	# trial is one stim_index; tracked frames only; positions smoothed with a Savitzky-Golay filter
18	# (21 frames, order 2); trials rejected when the absolute cumulative heading change exceeds
19	# 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or the mean speed exceeds
20	# 100 mm/s; measures taken from 3 s to 35 s after the first frame (the 3 s stationary phase is
[... 302 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l paper/*.txt; head -30 paper/*.txt; ls tools; cat tools/claims_check.py | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; grep -n -v "^\[[0-9]*\] \|^$" *.txt | awk -F: '{print $1": "substr($0, index($0,$2), 150)}' | head -400
```

```
1: DOI: 10.1523/jneurosci.6157-08.2009
2: Version: as served by pmc_playwright
3: Source: crossref+pmc_playwright (paper-text-fetcher)
4: Stored: 2026-10-21
5: Extracted: as fetched; with 1 supplement PDF(s), extracted with PyMuPDF (dehyphenated, NFKC)
6: ------------------------------------------------------------------------
7: Validation of Decision-Making Models and Analysis of Decision Variables in the Rat Basal Ganglia
9: Reinforcement learning theory plays a key role in understanding the behavioral and neural mechanisms of choice behavior in animals and humans. Especia
95: Skip to main content
97: An official website of the United States government
99: Here's how you know
100: Search
101: Log in
103: Primary site navigation
105: Search PMC Full-Text Archive
106: Search in PMC
107: Journal List 
108: User Guide
109: As a library, NLM provides access to scientific literature. Inclusion in an NLM database does not imply endorsement of, or agreement with, the content
110: Learn more: PMC Disclaimer | PMC Copyright Notice
[... 380 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1523-jneurosci.6157-08.2009.txt",
 "offset": 120,
 "limit": 350
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1523-jneurosci.6157-08.2009.txt",
 "offset": 120,
 "limit": 170
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1523-jneurosci.6157-08.2009.txt",
 "offset": 289,
 "limit": 180
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; grep -n "=== page\|Supplement\|Data [0-9]\|Figure\|Fig" *.txt | sed -n '1,200p' | grep -v "^\(1[0-9][0-9]\|[2-4][0-9][0-9]\):" ; python3 -c "
import fitz;d=fitz.open('10.1523-jneurosci.6157-08.2009.supp.pdf');print(d.page_count)"
```

```
Exit code 1
559:##### Supplement: supplemental methods (Supplemental_Material.pdf)
561:=== page 1 ===
562:Supplemental Method  
728:=== page 2 ===
927:=== page 3 ===
1240:=== page 4 ===
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import fitz;d=fitz.open('10.1523-jneurosci.6157-08.2009.supp.pdf');print(d.page_count)
    ^^^^^^^^^^^
ModuleNotFoundError: No module named 'fitz'
```

**Agent calls Bash**

```bash
cd paper; awk 'NR>=559' *.txt | awk 'length($0)>25'
```

```
##### Supplement: supplemental methods (Supplemental_Material.pdf)
Applying the particle filter to the estimation of the parameters of DF-Q learning 
The aims of applying the particle filter were, (1) to estimate the model parameter 
 based on past experiences (1:
to obtain the probability distribution
, and (2) to obtain a predictive 
 based on past experiences (1:
The fundamental idea, from Bayes’ theorem, is as follows: first, we determine the 
probability distribution of 
, as prior knowledge. The prediction of the choice 
2h  are the first and the second components of the parameter vector h 
corresponding to QL and QR, respectively. When the experience e(t=1) is given, the 
posterior distribution of the parameters 
 is obtained using Bayes’ theorem 
 is the likelihood that represents the accuracy of the prediction. The 
result is used in the prediction of the parameters at t=2, namely,  
 is the transient probability of the parameters defined by the 
update rule of the parameters. By using 
, the prediction of the choice at 
The posterior distribution of the parameters 
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -rn "001641" --include=*.yaml --include=*.json --include=*.md --include=*.csv . 2>/dev/null | grep -v "^./transcripts" | head; grep -n "http\|github\|code" paper/*.txt | grep -iv "doi\|pubmed\|google\|ncbi\|nlm" | head; which pdftotext pdftoppm
```

Result: not kept, because it reads the paper's text.

**Agent**

No code link in the paper. Checking the dataset metadata and manifest next.

**Agent calls Bash**

```bash
cd  sed -n 6740,6790p targets/dandisets.json; sed -n 135,160p targets/description_papers.yaml; sed -n 2020,2045p papers/manifest.yaml
```

```
"preprint": false
    }
   ],
   "catalystneuro": [
    "conversion code at https://github.com/catalystneuro/turner-lab-to-nwb/tree/main/notebooks",
    "conversion code at https://github.com/catalystneuro/turner-lab-to-nwb",
    "contributor Mayorquin, Heberto of CatalystNeuro"
   ]
  },
  {
   "dandiset": "001641",
   "name": "Neural activity in rat nucleus accumbens and ventral pallidum during probabilistic free-choice decision-making (Ito & Doya 2009)",
   "published_version": "0.260922.0719",
   "asset_count": 70,
   "size_gb": 0.18,
   "data_standards": [
    "Neurodata Without Borders (NWB)"
   ],
   "species": [
    "Rattus norvegicus - Norway rat"
[... 83 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls claims/001642/; head -80 claims/001642/*.yaml; grep -n "open\|equation\|Equation" claims/001642/*.yaml | head -40
```

```
10.1523-jneurosci.1962-14.2015.yaml
# Claims for Ito & Doya (2015), J Neurosci 35(8):3499-3514, on dandiset 001642.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read: the version of record, open access, as served by PMC (PMC4339358), stored in
# paper/10.1523-jneurosci.1962-14.2015.txt: abstract, Introduction, Materials and Methods,
# Results, Discussion and the figure legends. The paper has no supplement. No PDF was available.
# The display equations of the Methods (decision-tree probability, normalized likelihood,
# Markov model, DFQ update and choice rule, parameter drift, mutual information, BIC, and the
# regression model (2)) are images on PMC and are missing from the text; only the words around
# them were read. Where a criterion needs one of them, it is named as open with the readings
# the surrounding text allows. Figure panels (such as the windows drawn in Fig. 6A) could not
# be read. The paper links no code, so no code was read.
#
# Data the paper used, as it reports them. Seven male Long-Evans rats. 86 recording sessions,
# 78,107 trials: 12,185 single fixed-choice, 22,234 double fixed-choice, 36,292 free-choice and
# 3505 extinction-test trials. Each trial starts with a start tone; a center-hole poke of
# 500-1000 ms brings one of three cue tones (left tone 900 Hz, right tone 6500 Hz, choice tone
# white noise, 1000-2000 ms); after cue offset the rat pokes the left or right hole and hears
[... 75 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/001642/10.1523-jneurosci.1962-14.2015.yaml",
 "offset": 80,
 "limit": 300
}
```

```
80	#
81	# Readings and outcomes. Where a criterion lists readings of what a reported number counts
82	# (trial-counts, trials-per-block), the claim holds when it matches under any of them. Where
83	# the readings are of a method (any O above, a window, a test, how trials are combined), the
84	# notebook runs each, the outcome is the one they all give, and when they disagree the claim
85	# is blocked as methods_underspecified.
86	#  - O7, trials in the regression. The values come from the free-choice model, so readings are
87	#    (a) free-choice trials only, (b) all choice trials with QL and QR carried through the
88	#    session. The text says the full model has "six variables (including the constant
89	#    variable for β0)" and "26 models" (2^6 garbled), which does not match the eight terms
90	#    listed; reading (c) of the subset search keeps all eight terms as candidates (2^8 subsets,
91	#    or 2^7 with the constant always in).
92	#  - O8, FQ model. The update and choice equations are missing. The text's description implies
93	#    Q of the chosen action moves toward kappa1 after reward and toward -kappa2 after no reward
94	#    with rate alpha1, the unchosen Q decays toward 0 with rate alpha2 (= alpha1 in FQ), and
95	#    P(left) is a logistic function of QL - QR. Initial values, the priors of the particle
96	#    filter and the search for sigma_alpha and sigma_kappa are referred to Ito and Doya (2009).
97	#    5000 particles; QL and QR are the means of the predictive distribution.
98	#
99	# Paper inconsistencies noted: the Results cite "Fig. 7F" for state-value neurons, meaning
[... 280 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"
```

```
{
 "$schema": "https://json-schema.org/draft/2020-12/schema",
 "title": "Claims proposed for one target (a dataset and one of its papers)",
 "description": "Draft. To be revised after the pilot.",
 "type": "object",
 "additionalProperties": false,
 "required": [
  "schema_version",
  "dataset",
  "paper",
  "claims"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "dataset": {
   "description": "The dataset the claims are tested on: the archive and the dataset's identifier there.",
   "type": "object",
   "additionalProperties": false,
[... 185 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)[:4000])"
```

```
{
 "expected": {
  "type": "object",
  "additionalProperties": false,
  "required": [
   "quantity",
   "value"
  ],
  "properties": {
   "quantity": {
    "type": "string"
   },
   "value": {
    "type": "number"
   },
   "tolerance": {
    "type": "number",
    "minimum": 0
   },
   "unit": {
[... 82 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/001641/10.1523-jneurosci.6157-08.2009.yaml",
 "content": "# Claims for Ito & Doya (2009), J Neurosci 29(31):9861-9874, on dandiset 001641.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-21,\n# protocol pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the version of record, open access, as served by PMC (PMC6666589), stored in\n# paper/10.1523-jneurosci.6157-08.2009.txt: abstract, Introduction, Materials and Methods,\n# Results, Discussion, figure legends and Tables 1 to 3. Supplement read: the supplemental\n# Methods (Supplemental_Material.pdf, 4 pages, the particle filter), extracted in the same\n# file; its equations are garbled in the extraction and were read only for what the words say.\n# Not available: supplemental Data 1 (left-choice probability against QL - QR), Data 2 (rasters\n# of the Fig. 7 neurons and tone responses) and Data 3 (NAc core against shell). The main\n# findings do not rest on them; the claims that cite them (suppdata1-choice-vs-q-difference,\n# core-shell-no-difference) say so. No PDF of the main text was available, so the figure panels\n# could not be read. The display equations of the Methods (conditional probability, Markov\n# prediction, Q update, choice rule, likelihood, normalized likelihood, parameter drift,\n# regression models, class borders and mutual information) are images on PMC and are missing\n# from the text; only the words around them were read. The paper links no code, so no code was\n# read.\n#\n# Data the paper used, as it reports them. Six male Long-Evans rats; 70 recording sessions;\n# 60,221 trials: 39,175 choice trials (tone A, 4700 Hz), 12,707 no-choice trials (tone B,\n# 2000 Hz) and 8329 error trials. A trial starts with a start tone (2300 Hz, 1 s); a center-hole\n# poke of 500-1000 ms brings tone A (75%) or tone B (25%), 1000-2000 ms, which must be held\n# through. After tone A the rat pokes the left or right hole within 1 min and hears a reward\n# tone (500 Hz, 1 s, then a sucrose pellet) or a no-reward tone (500 Hz, 250 ms). After tone B\n# it must not poke L or R; a reward tone and pellet follow 1 s after center-hole exit. Error\n# trials end with an error tone (9500 Hz). Reward probabilities (left, right) per block are one\n# of (90, 50), (50, 90), (50, 10), (10, 50) %, all four in every four blocks, never the same\n# twice running; a block lasts at least 20 choice trials and ends when the more advantageous\n# side was chosen in 80% of the last 20 choice trials. Units: spike-sorted single units from\n# bundles of eight microwires, two bundles in the right NAc and one or two in the right VP,\n# advanced 125 um per session; 148 NAc and 66 VP neurons. Measured variables used: event times\n# (center-hole entry and exit, cue onset and type, L/R entry, reward or no-reward tone, pellet\n# pick-up), choices, outcomes, block reward probabilities, spike times, recording region (NAc\n# core or shell, VP).\n#\n# Methods fixed by the paper and used throughout (Materials and Methods unless named):\n#  - Behavioural sequences: no-choice and error trials removed; the remaining choice trials\n#    form the sequence; e(t) is one of L1, L0, R1, R0. Conditional left-choice probability is\n#    NL / (NL + NR) after a given experience sequence, with a 99% interval from\n#    betainv([0.005 0.995], NL, NR) (Model-free behavioral analysis).\n#  - Fig. 2C to 2E plot, for a four-trial sequence, the left-choice probability after each of\n#    its prefixes in time order (P(L|R0), P(L|R0 L1), ... ; Fig. 2B and 2C legends and Results,\n#    History dependence, paragraph 2).\n#  - Markov model of order d: P(a | last d experiences) = (Na + 1) / (NL + NR + 2), counts from\n#    the training data.\n#  - Q models: Qi(1) = 0 for fixed parameters; F-Q has alpha1 = alpha2, standard Q has\n#    alpha2 = kappa2 = 0; the local matching law is alpha1 = alpha2, kappa1 = 1, kappa2 = 0 with\n#    P(L) = QL / (QL + QR). Time-varying models: alpha1, alpha2, kappa1, kappa2 drift by\n#    Gaussian noise of SD sigma_alpha and sigma_kappa per trial; particle filter with 5000\n#    particles (supplemental Methods), initial QL, QR, alpha1, alpha2 uniform on [0, 1] and\n#    kappa1, kappa2 uniform on [0, 4]; the prediction is the mean of P(L) over the predictive\n#    distribution. Free parameters fitted by maximum likelihood on 35 training sessions, scored\n#    by the normalized likelihood of 35 test sessions.\n#  - Neural time bins (Fig. 8A legend): phase 1, 1 s before center-hole entry; phase 2, 1 s\n#    after cue onset; phase 3, 1 s before center-hole exit; phase 4, 1 s after center-hole\n#    exit; phase 5, 1 s after reward or no-reward tone onset. Spike counts in these bins.\n#  - Coding neurons by PETH comparison: two-sided Mann-Whitney U test at p < 0.01 of per-trial\n#    spike counts. State, phase 2, choice against no-choice trials. Action command, phase 3,\n#    and action, phase 4, left against right choice trials. Reward, phase 5, rewarded against\n#    unrewarded choice trials. Action value (phases 1 to 3, last 20 choice trials of each\n#    block) QL-coding when (90, 50) differs from (10, 50) and (50, 90) does not differ from\n#    (50, 10); QR-coding the converse.\n#  - Regression (Fig. 8C, 8D): spike count in phases 1 to 3 of the last 20 choice trials of each\n#    block, on the block's reward probabilities QL and QR, or on QL + QR and QL - QR; a\n#    coefficient is significant at p < 0.01 (t test); a neuron codes one regressor when that one\n#    is significant and the other is not.\n#  - Mutual information (Fig. 9): spike count in a 500 ms window, step 100 ms, aligned to cue\n#    onset or center-hole exit; four firing classes whose borders are chosen per neuron by\n#    exhaustive search to minimize the variance of the class counts; binary event; plug-in\n#    estimate minus the first-order bias term (Panzeri and Treves, 1996) built from M and the\n#    numbers of nonzero cells UFX, UF, UX; divided by the window length for per-second values;\n#    averaged over all neurons of a region. Action and reward use choice trials, state uses\n#    choice and no-choice trials, QL and QR are the F-Q (time-varying) estimates binarized at\n#    the median. Threshold (p < 0.01) is the second largest of 100 region averages with random\n#    binary events.\n#\n# Details the paper leaves open and that bear on several claims (each criterion names those\n# it needs):\n#  - O1, Q update. The equation is missing. Its words (alpha1 learning rate of the chosen\n#    action, alpha2 forgetting rate of the unchosen one, kappa1 strength of reinforcement by\n#    reward, kappa2 strength of aversion from no reward; equivalence with Barraclough et al.\n#    (2004) when alpha1 = alpha2) allow (a) chosen Q <- (1 - alpha1) Q + alpha1 kappa1 after\n#    reward, (1 - alpha1) Q - alpha1 kappa2 after no reward, unchosen Q <- (1 - alpha2) Q;\n#    (b) as (a) with kappa1 and -kappa2 added without the factor alpha1. Choice rule P(L) =\n#    1 / (1 + exp(-(QL - QR))), as the supplemental Methods, equation (1), writes it for the\n#    first two components of h. The readings give the same fits under a reparameterization\n#    with fixed parameters but different parameter values, and different fits when parameters\n#    drift.\n#  - O2, normalized likelihood. The equation is missing; read as the geometric mean of the\n#    per-trial likelihood of the observed choice over all trials of the sessions scored (0.5 at\n#    chance, 1 for exact deterministic prediction, as the Methods state). Per session for the\n#    paired Wilcoxon tests.\n#  - O3, training and test split. Not given. Readings are (a) alternate sessions in recording\n#    order over all rats; (b) alternate sessions in recording order within each rat; (c) a\n#    seeded random half. The reading whose choice-trial counts give 19,986 training and\n#    19,186 test trials, if any, is reported; the outcomes are judged under every reading.\n#  - O4, parameter search. Not given. Table 2 values lie on steps of 0.05 (alpha, kappa) and\n#    0.005 or 0.01 (sigma), so readings are (a) a grid on those steps; (b) a continuous\n#    optimizer started from the grid optimum.\n#  - O5, drift bounds. Whether alpha is kept in [0, 1] (and kappa in any range) during the\n#    random walk is not given. Readings are (a) no bounds; (b) alpha clipped to [0, 1].\n#  - O6, Markov predictions for the first d trials of a session, whose history is incomplete.\n#    Readings are (a) predicted with P(L) = 0.5; (b) left out of the score of every model.\n#  - O7, histories. The Methods count conditional probabilities \"during a block of choice\n#    trials\". Readings are (a) histories lying within one block; (b) histories within one\n#    session, across block borders.\n#  - O8, Mann-Whitney tests of conditional probabilities (Fig. 2B, 2C). What is ranked is not\n#    given. Readings are (a) the 0/1 left-choice indicators of the trials that follow each of\n#    the two histories, pooled over sessions; (b) per-session conditional probabilities.\n#    Two-sided.\n#  - O9, Mann-Whitney tests of percentages of coding neurons between regions (and between core\n#    and shell). Read as a two-sided Mann-Whitney U test on per-neuron 0/1 coding indicators,\n#    normal approximation with tie correction. This is the only reading the words give.\n#  - O10, binomial test against chance (Fig. 8). The chance level is not given. Readings are\n#    (a) 0.01, the test level; (b) 0.01 x 0.99, a significant result in one comparison and none\n#    in the other, for action-value, state-value and policy neurons. One-sided.\n#  - O11, Wilcoxon signed-rank test of preferences against 50%. What is tested is not given.\n#    Readings are (a) the signed-rank test, across the coding neurons of a type, of each\n#    neuron's difference of mean spike counts between the two conditions in the coding bin;\n#    (b) the same test on the signs alone (+1 or -1), which is a sign test. Two-sided.\n#  - O12, MI window placement. Windows are \"set based on\" the alignment time. Readings are\n#    (a) a window centred on each time point; (b) a window ending at it; (c) a window starting\n#    at it. Random events for the threshold are drawn (a) with probability 0.5; (b) with the\n#    frequency of the real event in the session.\n#  - O13, QL and QR for MI and Table 3. Readings are (a) the predictive mean at trial t, given\n#    e(1:t-1); (b) the posterior mean after e(t). Medians for binarization are taken (a) per\n#    session; (b) over all sessions.\n#  - O14, error trials in the state-coding test. Readings are (a) successful choice and\n#    no-choice trials only; (b) all trials in which tone A or tone B was presented, counting\n#    the 1 s after cue onset.\n#  - O15, firing rate \"during the task\". Readings are (a) spikes over the whole recording of\n#    the session; (b) spikes from the first trial start to the last trial end.\n#\n# Readings and outcomes. Where a criterion lists readings of what a reported number counts\n# (trial-counts, block-structure, tone-discrimination-errors, fig2c-sequence-frequencies), the\n# claim holds when it matches under any of them. Where the readings are of a method (any O\n# above, a window), the notebook runs each, the outcome is the one they all give, and when\n# they disagree the claim is blocked as methods_underspecified. Claims of absence are judged on\n# the paper's test as written.\n#\n# Tolerances. The default is 10% of the reported value, or the reported SD for a mean. For the\n# normalized likelihoods (Fig. 5) the tolerance is 0.005: the values lie between 0.508 and\n# 0.5375, close to chance (0.5), and 10% of the value (about 0.05) would accept any model at\n# chance; 0.005 is about a sixth of the reported span. Their order is judged by the criteria.\n#\n# Paper inconsistencies noted: the Results say the constant-parameter Q models are \"poorer than\n# that of the first- or second-order Markov models\", but F-Q and DF-Q (constant), 0.531, exceed\n# the first-order Markov model, 0.528; the Results cite \"previous reward shown in Fig. 8C,D\"\n# for Fig. 9; training and test choice trials (19,986 + 19,186 = 39,172) are three fewer than\n# the 39,175 choice trials; \"44/2 = 128\" is 4^4/2 garbled.\n#\n# All claims use the dataset's own recordings and behaviour (data: dataset, the default). The\n# paper relies on no outside data.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001641\"\npaper: doi:10.1523/jneurosci.6157-08.2009\nclaims:\n- id: trial-counts\n  statement: The analysis covers 60,221 trials in 70 recording sessions from six rats, of which\n    39,175 are choice trials, 12,707 no-choice trials and 8329 error trials.\n  source: Results, Behavioral data, paragraph 1\n  quote: Here, we report the results of all 60,221 trials in 70 recording sessions performed by\n    six rats, consisting of 39,175 choice trials (65.1%), 12,707 no-choice trials (21.1%), and\n    8329 error trials (13.8%)\n  expected:\n  - quantity: trials\n    value: 60221\n    tolerance: 6022.1\n  - quantity: recording sessions\n    value: 70\n    tolerance: 7\n  - quantity: rats\n    value: 6\n    tolerance: 0\n  - quantity: choice trials\n    value: 39175\n    tolerance: 3917.5\n  - quantity: no-choice trials\n    value: 12707\n    tolerance: 1270.7\n  - quantity: error trials\n    value: 8329\n    tolerance: 832.9\n  criterion: The rat count must match exactly. Choice trials are successful tone-A trials,\n    no-choice trials successful tone-B trials, and error trials those ended by the error tone\n    (Behavioral task). Readings of the total are (a) all trials started; (b) trials in which a\n    cue tone was presented. Reproduced when, under one reading, every count is within\n    tolerance.\n- id: block-structure\n  statement: A block took 105.6 trials on average, and a session held 8.1 blocks on average, from\n    5 to 12.\n  source: Results, Behavioral data, paragraph 1\n  quote: On average, 105.6 trials were required in one block, and 8.1 blocks (from 5 to 12\n    blocks) were performed in one session\n  depends_on:\n  - trial-counts\n  expected:\n  - quantity: mean trials per block\n    value: 105.6\n    tolerance: 10.56\n  - quantity: mean blocks per session\n    value: 8.1\n    tolerance: 0.81\n  - quantity: fewest blocks in a session\n    value: 5\n    tolerance: 0.5\n  - quantity: most blocks in a session\n    value: 12\n    tolerance: 1.2\n  criterion: The paper does not say which trials a block counts or whether a session's last,\n    possibly unfinished, block counts. Readings are (a) all trials, including no-choice and\n    error trials, every block; (b) as (a), completed blocks only; (c) choice trials only, every\n    block; (d) as (c), completed blocks only. Reproduced when, under one reading, all four\n    values are within tolerance (the range bounds as whole numbers, so 5 and 12 exactly).\n- id: reaction-time\n  statement: In choice trials the time from center-hole exit to L or R hole entry was under 1 s\n    in 72% of trials, with a median of 0.75 s.\n  source: Results, Reaction time and tone discrimination, paragraph 2\n  quote: The reaction time in the choice trials, the time period from the exit of the center\n    hole to the entry of the left or right hole, was <1 s in 72% of the trials and had a median\n    of 0.75 s\n  expected:\n  - quantity: fraction of choice trials with reaction time under 1 s\n    value: 72\n    tolerance: 7.2\n    unit: percent\n  - quantity: median reaction time\n    value: 0.75\n    tolerance: 0.075\n    unit: s\n  criterion: Over all choice trials of the 70 sessions, pooled. Reproduced when both values are\n    within tolerance.\n- id: tone-discrimination-errors\n  statement: Rats rarely failed to poke after tone A (0.39% of choice trials) or poked wrongly\n    after tone B (0.73% of no-choice trials), so they discriminated the tones well.\n  source: Results, Reaction time and tone discrimination, paragraph 2\n  quote: The errors in the choice trials, in which rats did not perform any nose pokes within 1\n    min for tone A presentation, were only 0.39% of the choice trials. The errors in no-choice\n    trials, in which rats performed a nose poke at the left or right hole within 1 s for tone B\n    presentation, were 0.73% of the no-choice trials\n  expected:\n  - quantity: no-response errors after tone A\n    value: 0.39\n    tolerance: 0.039\n    unit: percent\n  - quantity: L or R poke errors after tone B\n    value: 0.73\n    tolerance: 0.073\n    unit: percent\n  criterion: The denominators are not fixed. Readings are (a) the error count over the\n    successful trials of that tone (39,175 and 12,707); (b) the error count over the\n    successful trials of that tone plus those errors. Errors from leaving the center hole\n    during the cue are not counted in either. Reproduced when, under one reading, both values\n    are within tolerance.\n- id: fig2b-reward-stronger-than-noreward\n  statement: Both L1 and R0 in the previous trial raise the left-choice probability (0.68 and\n    0.62), more after L1; both R1 and L0 lower it (0.30 and 0.39), more after R1. So rewarded\n    experience modulates choice more than unrewarded experience.\n  source: Results, History dependence of action choice, paragraph 1; Figure 2B\n  quote: Both the experience L1 and R0 in the previous trial increased the probability of a left\n    choice in the current trial [Fig. 2B, green arrow, P(L|L1) = 0.68; green arrowhead, P(L|R0) =\n    0.62]. The left choice probability after L1 was significantly higher than after R0\n    (Mann–Whitney U test, p < 0.0001) ... The left probability after R1 was significantly lower\n    than after L0 [Fig. 2B, brown arrow, P(L|R1) = 0.30; brown arrowhead, P(L|L0) = 0.39]\n    (Mann–Whitney U test, p < 0.0001)\n  statistics:\n  - about: P(L|L1) against P(L|R0)\n    test: Mann–Whitney U test\n    p: 0.0001\n    p_relation: \"<\"\n  - about: P(L|R1) against P(L|L0)\n    test: Mann–Whitney U test\n    p: 0.0001\n    p_relation: \"<\"\n  expected:\n  - quantity: P(L|L1)\n    value: 0.68\n    tolerance: 0.068\n  - quantity: P(L|R0)\n    value: 0.62\n    tolerance: 0.062\n  - quantity: P(L|R1)\n    value: 0.30\n    tolerance: 0.030\n  - quantity: P(L|L0)\n    value: 0.39\n    tolerance: 0.039\n  criterion: Conditional probabilities as the Methods define them (opening comment), pooled over\n    all sessions; histories as O7; tests as O8. Reproduced when, under every reading, the four\n    values are within tolerance, P(L|L1) > P(L|R0) > 0.5 > P(L|L0) > P(L|R1), and both tests\n    give p < 0.0001.\n- id: fig2b-two-back-history\n  statement: The experience two trials back still affects choice; P(L|R0 L1) = 0.66 differs from\n    P(L|L1 L1) = 0.72.\n  source: Results, History dependence of action choice, paragraph 2; Figure 2B and 2C\n  quote: the conditional probability P(L|R0 L1) = 0.66 (Fig. 2B,C, blue arrowhead), which is the\n    probability of a left choice (at trial t) after R0 (at trial t − 2) and L1 (at trial t − 1),\n    significantly differs from P(L|L1 L1) = 0.72 (Fig. 2B,C, blue arrow) ... (Mann– Whitney U\n    test, p < 0.0001)\n  statistics:\n  - test: Mann–Whitney U test\n    p: 0.0001\n    p_relation: \"<\"\n  expected:\n  - quantity: P(L|R0 L1)\n    value: 0.66\n    tolerance: 0.066\n  - quantity: P(L|L1 L1)\n    value: 0.72\n    tolerance: 0.072\n  criterion: As fig2b-reward-stronger-than-noreward (O7, O8). Reproduced when, under every\n    reading, both values are within tolerance, P(L|L1 L1) > P(L|R0 L1), and the test gives\n    p < 0.0001.\n- id: fig2c-sequence-frequencies\n  statement: Of the 128 mirror-paired four-trial sequences, L1 L1 L1 L1 (with R1 R1 R1 R1) is the\n    most frequent (6.87%), R0 L1 L1 L1 (with L0 R1 R1 R1) the second (2.87%), R0 L0 R0 L0 (with\n    L0 R0 L0 R0) the third (2.55%), and L0 L0 L0 L0 with R0 R0 R0 R0 make 1.28%.\n  source: Results, History dependence of action choice, paragraphs 2 and 3\n  quote: the sequence L1 L1 L1 L1 and R1 R1 R1 R1 was observed most frequently (6.87% of all\n    observed sequences of four trials). The sequence R0 L1 L1 L1 and L0 R1 R1 R1 was observed\n    second most frequently (2.87%) ... The sequences R0 L0 R0 L0 and L0 R0 L0 R0 were observed\n    third most frequently (2.55%) ... L0 L0 L0 L0 and R0 R0 R0 R0, which consisted of 1.28% of\n    all observed sequences across the four trials\n  expected:\n  - quantity: L1 L1 L1 L1 with R1 R1 R1 R1\n    value: 6.87\n    tolerance: 0.687\n    unit: percent\n  - quantity: R0 L1 L1 L1 with L0 R1 R1 R1\n    value: 2.87\n    tolerance: 0.287\n    unit: percent\n  - quantity: R0 L0 R0 L0 with L0 R0 L0 R0\n    value: 2.55\n    tolerance: 0.255\n    unit: percent\n  - quantity: L0 L0 L0 L0 with R0 R0 R0 R0\n    value: 1.28\n    tolerance: 0.128\n    unit: percent\n  criterion: All windows of four consecutive choice trials, histories as O7. Whether a pair's\n    percentage is the sum of the two mirror sequences or each one's share is not fixed;\n    readings are (a) the sum; (b) the mean of the two. Reproduced when, under one reading, all\n    four values are within tolerance and the first three are the three most frequent pairs in\n    that order.\n- id: fig2c-reward-effects-fade\n  statement: After repeated L1 the left-choice probability rises and converges near 0.75, and the\n    effect of an earlier R0 fades under following L1s, so P(L|L1 L1 L1 L1) and P(L|R0 L1 L1 L1)\n    do not differ (both 0.74).\n  source: Results, History dependence of action choice, paragraph 2; Figure 2C\n  quote: increased with the number of L1 experiences and converged around 0.75 ... There was no\n    significant difference between P(L|L1 L1 L1 L1) = 0.74 and P(L|R0 L1 L1 L1) = 0.74\n    (Mann–Whitney U test, p = 0.94)\n  statistics:\n  - test: Mann–Whitney U test\n    p: 0.94\n  expected:\n  - quantity: P(L|L1 L1 L1 L1)\n    value: 0.74\n    tolerance: 0.074\n  - quantity: P(L|R0 L1 L1 L1)\n    value: 0.74\n    tolerance: 0.074\n  criterion: Prefix probabilities as the opening comment, histories as O7. The absence is judged\n    on the paper's test, a Mann-Whitney U test at p < 0.05 (two-sided), under reading O8 (a),\n    the 0/1 choices that follow each history; reading O8 (b) is shown as a variant. Reproduced\n    when the test does not find a difference, both values are within tolerance, and\n    P(L|L1) < P(L|L1 L1) < P(L|L1 L1 L1) <= P(L|L1 L1 L1 L1) + 0.02 with the last within 0.05 of\n    0.75; the difference is reported either way.\n- id: fig2d-switching\n  statement: After an unrewarded choice rats tended to choose the other action (switching), as\n    seen in the alternating unrewarded sequences R0 L0 R0 L0 and L0 R0 L0 R0.\n  source: Results, History dependence of action choice, paragraph 3; Figure 2D\n  quote: These results illustrate that there was a “switching” behavior in which rats tended to\n    choose the other action after one action was not rewarded\n  criterion: Prefix probabilities for R0 L0 R0 L0 and L0 R0 L0 R0 (O7), with 99% intervals.\n    Reproduced when, under every reading, after each prefix ending in L0 the left-choice\n    probability is below 0.5 and after each prefix ending in R0 it is above 0.5, with the 99%\n    interval excluding 0.5 in at least six of the eight prefixes.\n- id: fig2e-persevering\n  statement: After two or more unrewarded left choices the left-choice probability gradually\n    rises, and P(L|L0 L0 L0) and P(L|L0 L0 L0 L0) are both above 0.5, so rats sometimes persevere\n    after repeated non-reward.\n  source: Results, History dependence of action choice, paragraph 3; Figure 2E\n  quote: The probability of a left choice gradually increased after two or more left choices with\n    no reward. In particular, P(L|L0 L0 L0) and P(L|L0 L0 L0 L0) were both >0.5\n  criterion: Prefix probabilities for L0 L0 L0 L0 (and mirrored for R0 R0 R0 R0, as 1 - P(L)),\n    O7. The paper gives no test. Reproduced when, under every reading, P(L|L0 L0) <\n    P(L|L0 L0 L0) <= P(L|L0 L0 L0 L0) (the last within 0.02 allowed) and both P(L|L0 L0 L0)\n    and P(L|L0 L0 L0 L0) exceed 0.5 for the left sequence; partially reproduced when this\n    holds for the probabilities above 0.5 but not for the rise.\n- id: fig3-lsq-switching\n  statement: Fitted by least squares to the six four-trial sequences of Fig. 2C and 2D, the local\n    matching law and standard Q-learning cannot represent switching, while F-Q and DF-Q can;\n    the averaged residual errors are 0.0102, 0.0073, 0.0010 and 0.0002.\n  source: Results, Modeling rats' strategies with a reinforcement learning model, paragraph 3;\n    Figure 3; Table 1\n  quote: The results showed that the local matching law (Fig. 3A) and the standard Q-learning\n    model (Fig. 3B) were not able to represent switching behavior, whereas the F-Q- and\n    DF-Q-learning models were (Fig. 3C,D). The averaged residual errors of the local matching\n    law, the standard Q, F-Q, and DF-Q models were 0.0102, 0.0073, 0.0010, and 0.0002,\n    respectively\n  depends_on:\n  - fig2c-reward-effects-fade\n  - fig2d-switching\n  expected:\n  - quantity: averaged residual error, local matching law\n    value: 0.0102\n    tolerance: 0.00102\n  - quantity: averaged residual error, standard Q\n    value: 0.0073\n    tolerance: 0.00073\n  - quantity: averaged residual error, F-Q\n    value: 0.0010\n    tolerance: 0.0001\n  - quantity: averaged residual error, DF-Q\n    value: 0.0002\n    tolerance: 0.00002\n  criterion: Data are the prefix probabilities of L1 L1 L1 L1, R1 R1 R1 R1, R0 L1 L1 L1,\n    L0 R1 R1 R1, R0 L0 R0 L0 and L0 R0 L0 R0 (24 points). Each model starts from QL = QR = Q0\n    (a free parameter), applies the sequence and predicts P(L) after each prefix; parameters\n    minimize the squared error (Results, paragraph 3; Table 1). Model equations as O1. The\n    \"averaged residual error\" is not defined; readings are (a) the mean squared error over the\n    24 points; (b) the mean squared error over the 12 points of the three left-ending\n    sequences with each mirror pair averaged. \"Represents switching\" is read from Fig. 3 as\n    the model's P(L) after each L0 of R0 L0 R0 L0 below 0.5 and after each R0 above 0.5.\n    Reproduced when, under every reading, the residuals are in the order local matching >\n    standard Q > F-Q > DF-Q, each within tolerance, and switching is represented by F-Q and\n    DF-Q but not by the local matching law and standard Q. Partially reproduced when the order\n    and the switching hold but a value is out of tolerance.\n- id: table1-lsq-parameters\n  statement: The least-squares fits give the parameters of Table 1 (alpha1, alpha2, kappa1,\n    kappa2, Q0) for each model.\n  source: Table 1\n  inferred: Numbers only in Table 1; no sentence states them.\n  depends_on:\n  - fig3-lsq-switching\n  expected:\n  - quantity: standard Q alpha1\n    value: 0.37\n    tolerance: 0.037\n  - quantity: standard Q kappa1\n    value: 2.37\n    tolerance: 0.237\n  - quantity: standard Q Q0\n    value: 1.00\n    tolerance: 0.10\n  - quantity: F-Q alpha1\n    value: 0.96\n    tolerance: 0.096\n  - quantity: F-Q kappa1\n    value: 0.99\n    tolerance: 0.099\n  - quantity: F-Q kappa2\n    value: 0.64\n    tolerance: 0.064\n  - quantity: F-Q Q0\n    value: 0.00\n    tolerance: 0.05\n  - quantity: DF-Q alpha1\n    value: 0.52\n    tolerance: 0.052\n  - quantity: DF-Q alpha2\n    value: 0.88\n    tolerance: 0.088\n  - quantity: DF-Q kappa1\n    value: 1.18\n    tolerance: 0.118\n  - quantity: DF-Q kappa2\n    value: 1.44\n    tolerance: 0.144\n  - quantity: DF-Q Q0\n    value: 0.71\n    tolerance: 0.071\n  - quantity: local matching law alpha1\n    value: 0.05\n    tolerance: 0.005\n  - quantity: local matching law Q0\n    value: 0.07\n    tolerance: 0.007\n  criterion: As fig3-lsq-switching. A reported 0.00 cannot take 10% of itself, so it is given\n    0.05, the step of the table's other values. Readings as O1 (the parameter values depend on\n    the form of the update). Reproduced when, under one reading of O1, all values are within\n    tolerance; partially reproduced when at least 10 of the 14 are. The O1 reading that gives\n    the match is reported.\n- id: fig5-markov-accuracy\n  statement: The first- to fourth-order Markov models reach normalized likelihoods of 0.528,\n    0.532, 0.534 and 0.532 on test data; the third order is best and the fourth is lower,\n    presumably by overfitting its 256 parameters.\n  source: Results, Prediction of choices by models, paragraph beginning \"Figure 5 shows\"; Figure 5\n  quote: The normalized likelihood of the first-order Markov model was 0.528 ... The normalized\n    likelihood for the second- and third-order Markov models increased to 0.532 and 0.534,\n    respectively ... The performance of the fourth-order model was 0.532, lower than that of the\n    third-order model\n  expected:\n  - quantity: normalized likelihood, Markov order 1\n    value: 0.528\n    tolerance: 0.005\n  - quantity: normalized likelihood, Markov order 2\n    value: 0.532\n    tolerance: 0.005\n  - quantity: normalized likelihood, Markov order 3\n    value: 0.534\n    tolerance: 0.005\n  - quantity: normalized likelihood, Markov order 4\n    value: 0.532\n    tolerance: 0.005\n  criterion: Markov prediction as the Methods give it, counts from the 35 training sessions,\n    scored on the 35 test sessions with the normalized likelihood (O2); split O3; first trials\n    O6; histories over choice trials within a session. Reproduced when, under every reading,\n    all four values are within tolerance and order 3 is the highest. Partially reproduced when\n    order 3 is highest but a value is out of tolerance.\n- id: fig5-constant-models\n  statement: With constant parameters, standard Q, F-Q and DF-Q (0.527, 0.531, 0.531) predict much\n    better than the local matching law (0.508), but worse than the first- or second-order Markov\n    models.\n  source: Results, Prediction of choices by models, paragraph beginning \"Predictions by the\n    standard Q-\"; Figure 5; Table 2\n  quote: Predictions by the standard Q-, F-Q-, and DF-Q-learning models with constant parameters\n    (α and κ) were much better (0.527, 0.531, and 0.531, respectively) than the predictions of\n    the local matching law (0.508), but poorer than that of the first- or second-order Markov\n    models\n  depends_on:\n  - fig5-markov-accuracy\n  expected:\n  - quantity: normalized likelihood, standard Q (constant)\n    value: 0.527\n    tolerance: 0.005\n  - quantity: normalized likelihood, F-Q (constant)\n    value: 0.531\n    tolerance: 0.005\n  - quantity: normalized likelihood, DF-Q (constant)\n    value: 0.531\n    tolerance: 0.005\n  - quantity: normalized likelihood, local matching law\n    value: 0.508\n    tolerance: 0.005\n  criterion: Parameters constant across sessions, fitted by maximum likelihood on the training\n    sessions (O4), Qi(1) = 0 in each session, scored on the test sessions (O2, O3); equations\n    O1; local matching law with P(L) = QL / (QL + QR). Reproduced when, under every reading,\n    all four values are within tolerance and the three Q models exceed the local matching law.\n    The comparison with the Markov models is reported; the paper's own numbers place F-Q and\n    DF-Q (constant) above the first-order Markov model (opening comment), so it is not part of\n    the outcome.\n- id: fig5-variable-models-best\n  statement: With time-varying parameters standard Q, F-Q and DF-Q improve to 0.5304, 0.5375 and\n    0.5368, and F-Q with time-varying parameters predicts best of all models.\n  source: Results, Prediction of choices by models, paragraph beginning \"With time-varying\n    parameters\"; Figure 5\n  quote: With time-varying parameters, the performance of the standard Q, F-Q, and DF-Q models\n    improved (0.5304, 0.5375, and 0.5368, respectively). The F-Q-learning model with\n    time-varying parameters produced the best prediction performance\n  depends_on:\n  - fig5-markov-accuracy\n  - fig5-constant-models\n  expected:\n  - quantity: normalized likelihood, standard Q (variable)\n    value: 0.5304\n    tolerance: 0.005\n  - quantity: normalized likelihood, F-Q (variable)\n    value: 0.5375\n    tolerance: 0.005\n  - quantity: normalized likelihood, DF-Q (variable)\n    value: 0.5368\n    tolerance: 0.005\n  criterion: Particle filter as the supplemental Methods and the opening comment give it, 5000\n    particles, sigma_alpha and sigma_kappa fitted on the training sessions (O4), drift O5,\n    equations O1, scored on the test sessions (O2, O3). Each variable model is reported against\n    its constant version. Reproduced when, under every reading, the three values are within\n    tolerance, each exceeds its constant version, and F-Q (variable) has the highest normalized\n    likelihood of all models of Fig. 5; partially reproduced when F-Q or DF-Q (variable) is\n    highest and the values are in tolerance but F-Q is not first.\n- id: fig5-fq-dfq-beat-all-models\n  statement: Per test session, the F-Q and DF-Q models with time-varying parameters predict\n    significantly better than every other model, including the third-order Markov model.\n  source: Results, Prediction of choices by models, paragraph beginning \"A statistical test\";\n    Figure 5 legend\n  quote: the prediction accuracies of both the F-Q- and DF-Q-learning models with time-varying\n    parameters were significantly higher than those of all other models (paired-sample\n    Wilcoxon's signed rank test, p < 0.05 for third Markov model, p < 0.01 for other models)\n  statistics:\n  - about: F-Q and DF-Q (variable) against the third-order Markov model\n    test: paired-sample Wilcoxon's signed rank test\n    p: 0.05\n    p_relation: \"<\"\n    n: 35 test sessions\n  - about: F-Q and DF-Q (variable) against the other models\n    test: paired-sample Wilcoxon's signed rank test\n    p: 0.01\n    p_relation: \"<\"\n    n: 35 test sessions\n  depends_on:\n  - fig5-variable-models-best\n  criterion: Per-session normalized likelihoods of the 35 test sessions (O2), two-sided paired\n    Wilcoxon signed-rank tests of F-Q (variable) and of DF-Q (variable) against each of the\n    other nine models of Fig. 5 (standard Q variable, three constant Q models, local matching\n    law, Markov orders 1 to 4). Readings O1, O3 to O6. Reproduced when, under every reading,\n    both models exceed every other model with p < 0.05 against the third-order Markov model and\n    p < 0.01 against the rest; partially reproduced when all comparisons give p < 0.05 with the\n    F-Q and DF-Q medians higher.\n- id: fig5-fq-dfq-no-difference\n  statement: The F-Q and DF-Q models with time-varying parameters do not differ in prediction\n    accuracy (p = 0.067), so F-Q, with fewer parameters, is regarded as the better model.\n  source: Results, Prediction of choices by models, paragraph beginning \"A statistical test\"\n  quote: There was no significant difference between these two models (paired-sample Wilcoxon's\n    signed rank test, p = 0.067)\n  statistics:\n  - test: paired-sample Wilcoxon's signed rank test\n    p: 0.067\n    n: 35 test sessions\n  depends_on:\n  - fig5-variable-models-best\n  criterion: A claim of absence, judged on the paper's test, a two-sided paired Wilcoxon\n    signed-rank test of per-session normalized likelihoods of F-Q (variable) against DF-Q\n    (variable) over the 35 test sessions at p < 0.05, under every reading of O1, O3 to O5.\n    Reproduced when the test does not find a difference; the median difference is reported\n    either way.\n- id: binary-prediction-accuracy\n  statement: Taking left when the predicted P(L) exceeds 0.5 and right otherwise, the best model\n    predicts 68% of choices correctly, averaged over the 35 test sessions.\n  source: Results, Prediction of choices by models, paragraph beginning \"With time-varying\n    parameters\"\n  quote: If we take binary predictions from the choice probability [left for PL(t) > 0.5, right\n    for PL(t) < 0.5], the average percentage of correct predictions over 35 test sessions is 68%\n  depends_on:\n  - fig5-variable-models-best\n  expected:\n  - quantity: correct binary predictions, mean over test sessions\n    value: 68\n    tolerance: 6.8\n    unit: percent\n  criterion: The sentence follows the statement that F-Q (variable) is best and does not name\n    the model; read as F-Q (variable). Percentage correct per test session, averaged over the\n    35 sessions; trials with P(L) = 0.5 exactly count as half correct. Readings O1, O3 to O5.\n    Reproduced when, under every reading, the value is within tolerance.\n- id: table2-ml-parameters\n  statement: The maximum-likelihood parameters on the training data are those of Table 2 (for\n    example F-Q constant alpha 0.55, kappa1 1.25, kappa2 0.55; F-Q variable sigma_alpha 0.005,\n    sigma_kappa 0.07).\n  source: Table 2\n  inferred: Numbers only in Table 2; no sentence states them.\n  depends_on:\n  - fig5-constant-models\n  - fig5-variable-models-best\n  expected:\n  - quantity: standard Q (constant) alpha1\n    value: 0.45\n    tolerance: 0.045\n  - quantity: standard Q (constant) kappa1\n    value: 1.25\n    tolerance: 0.125\n  - quantity: F-Q (constant) alpha1\n    value: 0.55\n    tolerance: 0.055\n  - quantity: F-Q (constant) kappa1\n    value: 1.25\n    tolerance: 0.125\n  - quantity: F-Q (constant) kappa2\n    value: 0.55\n    tolerance: 0.055\n  - quantity: DF-Q (constant) alpha1\n    value: 0.60\n    tolerance: 0.060\n  - quantity: DF-Q (constant) alpha2\n    value: 0.45\n    tolerance: 0.045\n  - quantity: DF-Q (constant) kappa1\n    value: 1.20\n    tolerance: 0.120\n  - quantity: DF-Q (constant) kappa2\n    value: 0.45\n    tolerance: 0.045\n  - quantity: local matching law alpha1\n    value: 0.01\n    tolerance: 0.001\n  - quantity: standard Q (variable) sigma_alpha\n    value: 0.005\n    tolerance: 0.0005\n  - quantity: standard Q (variable) sigma_kappa\n    value: 0.10\n    tolerance: 0.010\n  - quantity: F-Q (variable) sigma_alpha\n    value: 0.005\n    tolerance: 0.0005\n  - quantity: F-Q (variable) sigma_kappa\n    value: 0.07\n    tolerance: 0.007\n  - quantity: DF-Q (variable) sigma_alpha\n    value: 0.010\n    tolerance: 0.0010\n  - quantity: DF-Q (variable) sigma_kappa\n    value: 0.07\n    tolerance: 0.007\n  criterion: As fig5-constant-models and fig5-variable-models-best. The parameter values depend on\n    O1 and O3 to O5, and a grid step (O4 a) is coarser than 10% for the smallest values.\n    Reproduced when, under one reading, at least 13 of the 16 values are within tolerance;\n    partially reproduced for 8 to 12. The reading that matches is reported.\n- id: table3-parameter-averages\n  statement: Across all data the time-varying estimates average, for F-Q, alpha1 0.47 ± 0.25,\n    kappa1 1.61 ± 0.77, kappa2 1.10 ± 0.87, and for DF-Q, alpha1 0.45 ± 0.19, alpha2 0.46 ± 0.19,\n    kappa1 1.69 ± 0.77, kappa2 1.24 ± 0.92; standard Q alpha1 0.45 ± 0.23, kappa1 1.86 ± 0.68.\n  source: Table 3\n  inferred: Numbers only in Table 3; no sentence states them.\n  depends_on:\n  - fig5-variable-models-best\n  expected:\n  - quantity: standard Q (variable) alpha1 mean\n    value: 0.45\n    tolerance: 0.23\n  - quantity: standard Q (variable) kappa1 mean\n    value: 1.86\n    tolerance: 0.68\n  - quantity: F-Q (variable) alpha1 mean\n    value: 0.47\n    tolerance: 0.25\n  - quantity: F-Q (variable) kappa1 mean\n    value: 1.61\n    tolerance: 0.77\n  - quantity: F-Q (variable) kappa2 mean\n    value: 1.10\n    tolerance: 0.87\n  - quantity: DF-Q (variable) alpha1 mean\n    value: 0.45\n    tolerance: 0.19\n  - quantity: DF-Q (variable) alpha2 mean\n    value: 0.46\n    tolerance: 0.19\n  - quantity: DF-Q (variable) kappa1 mean\n    value: 1.69\n    tolerance: 0.77\n  - quantity: DF-Q (variable) kappa2 mean\n    value: 1.24\n    tolerance: 0.92\n  criterion: Per-trial estimates (O13) from the time-varying models with the Table 2 sigmas,\n    over all 70 sessions; mean and SD over all choice trials. The tolerance of each mean is\n    its SD (protocol); each SD is also reported against the table. Readings O1, O5, O13.\n    Reproduced when, under every reading, all nine means are within tolerance.\n- id: fig4-strategy-tracking\n  statement: With time-varying parameters, F-Q and DF-Q capture win-stay-lose-switch behaviour by\n    raising kappa2 close to kappa1, and persevering behaviour by a negative kappa2, which the\n    standard Q model cannot.\n  source: Results, Prediction of choices by models, paragraphs beginning \"Figure 4A–F\" and\n    \"Figure 4, B, D, and F\"; Figure 4\n  quote: This behavior was captured by the F-Q- and DF-Q-learning models, with both models showing\n    an increase in the nonreward aversion parameter κ2 close to the reward reinforcement\n    parameter κ1 ... The F-Q and DF-Q models captured this behavior by exhibiting a negative\n    value for the aversion parameter κ2 (Fig. 4H)\n  depends_on:\n  - fig5-variable-models-best\n  criterion: The paper shows representative sessions and does not identify them, so the claim is\n    tested as existence of such episodes. Win-stay-lose-switch episode, a run of at least 10\n    choice trials in which the rat repeated every rewarded choice and switched after every\n    unrewarded one, as Results describe it. Persevering episode, a run of at least 5\n    consecutive unrewarded choices of the less advantageous side in a (10, 50) or (50, 10)\n    block (Fig. 4B, D, F). Reproduced when, under every reading of O1, O5 and O13, some\n    win-stay-lose-switch episode has F-Q (variable) kappa2 within 25% of kappa1 at its end, some\n    persevering episode has F-Q (variable) kappa2 below 0, and over all such episodes the F-Q\n    (variable) mean per-trial likelihood exceeds that of standard Q (variable). The 25% and\n    the run lengths are fixed here because the paper gives none; the results for 5, 10 and 15\n    trials are shown.\n- id: suppdata1-choice-vs-q-difference\n  statement: The actual left-choice probability, plotted against QL - QR from the standard Q, F-Q\n    and DF-Q models, confirms that the models' predictions are meaningful.\n  source: Results, Prediction of choices by models, paragraph beginning \"With time-varying\n    parameters\"; supplemental Data 1 (not available)\n  quote: the meaningful performances of the standard Q, F-Q, and DF-Q models were also conformed\n    by plotting the actual left-choice probability for the difference between QL and QR\n    (supplemental Data 1\n  depends_on:\n  - fig5-variable-models-best\n  criterion: Supplemental Data 1 is not in the text read, so its bins and models (constant or\n    variable) are not known. Readings are the variable and the constant versions of each\n    model, with QL - QR (O13 a) in ten equal-count bins over all choice trials. Reproduced\n    when, under every reading, the left-choice fraction rises with QL - QR (Spearman correlation\n    of bin centres and fractions above 0.9) for all three models.\n- id: neuron-counts\n  statement: Analysis used 148 NAc neurons and 66 VP neurons from six rats in 70 sessions.\n  source: Results, Neuronal recording data, paragraph 1\n  quote: Subsequent analysis was performed for a total of 148 NAc neurons and 66 VP neurons from\n    six rats during 70 sessions\n  expected:\n  - quantity: NAc neurons\n    value: 148\n    tolerance: 14.8\n  - quantity: VP neurons\n    value: 66\n    tolerance: 6.6\n  criterion: Units whose estimated position lies in the NAc or VP (Histology). Reproduced when\n    both counts are within tolerance.\n- id: firing-rates\n  statement: VP neurons fire faster than NAc neurons during the task (10.2 ± 9.1 against 2.6 ±\n    2.6 Hz, mean ± SD).\n  source: Results, Neuronal activity in the NAc and VP, paragraph 1\n  quote: VP neurons showed a higher firing rate than NAc neurons overall. The average and SD of\n    the firing rate of VP neurons and NAc neurons during the task were 10.2±9.1 and 2.6±2.6 Hz,\n    respectively\n  depends_on:\n  - neuron-counts\n  expected:\n  - quantity: mean VP firing rate\n    value: 10.2\n    tolerance: 9.1\n    unit: Hz\n  - quantity: mean NAc firing rate\n    value: 2.6\n    tolerance: 2.6\n    unit: Hz\n  - quantity: SD of VP firing rates\n    value: 9.1\n    tolerance: 0.91\n    unit: Hz\n  - quantity: SD of NAc firing rates\n    value: 2.6\n    tolerance: 0.26\n    unit: Hz\n  criterion: Per neuron, spikes over the task period divided by its duration (O15); mean and SD\n    over neurons per region. The paper gives no test. Reproduced when, under every reading, the\n    VP mean exceeds the NAc mean and the two means are within tolerance; the SDs are reported\n    and partially reproduced is given when a mean holds but an SD is outside 10%.\n- id: fig8b-state-coding\n  statement: After cue onset (phase 2), 54% of NAc neurons (80 of 148) and 50% of VP neurons (33\n    of 66) fire differently for the choice and the no-choice tone (state-coding neurons).\n  source: Results, Neuronal activity in the NAc and VP, paragraph 4; Figure 8B\n  quote: After the onset of the cue tone (phase 2), 54% (80 of 148) of NAc neurons and 50% (33 of\n    66) of VP neurons showed different firing patterns in response to the choice tone and the\n    no-choice tone\n  depends_on:\n  - neuron-counts\n  expected:\n  - quantity: NAc state-coding neurons\n    value: 80\n    tolerance: 8\n  - quantity: VP state-coding neurons\n    value: 33\n    tolerance: 3.3\n  criterion: Mann-Whitney U test at p < 0.01 of phase-2 spike counts, choice against no-choice\n    trials (opening comment), trials O14. Reproduced when, under every reading, both counts\n    are within tolerance.\n- id: fig8b-action-value-psth\n  statement: By block comparison of firing, few neurons code an action value; QL-coding neurons\n    are 6, 8 and 7% of NAc neurons and 11, 18 and 21% of VP neurons in phases 1 to 3, and\n    QR-coding neurons 7, 8 and 5% (NAc) and 11, 9 and 11% (VP).\n  source: Results, Neuronal activity in the NAc and VP, paragraph 4; Figure 8B; Figure 7E and 7F\n  quote: Before the onset of the nose poke action at the center hole (phase 1), the percentage of\n    QL-coding neurons in the NAc was 6% (9 of 148), and 11% (7 of 66) in the VP ... The\n    percentage of QR-coding neurons in the NAc was 7% (11 of 148), and 11% (7 of 66) in the VP\n    ... The percentage of QL-coding neurons in the NAc was 8% (12 of 148) and 18% (12 of 66) in\n    the VP. The percentage of QR-coding neurons in the NAc was 8% (12 of 148) and 9% (6 of 66) in\n    the VP. Before the initiation of action (phase 3), QL-coding neurons represented 7% (11 of\n    148) of the neurons in the NAc and 21% (14 of 66) of those in the VP. QR-coding neurons\n    represented 5% (8 of 148) of the neurons in the NAc and 11% (7 of 66) of those in the VP\n  depends_on:\n  - neuron-counts\n  expected:\n  - quantity: NAc QL-coding, phase 1\n    value: 9\n    tolerance: 0.9\n  - quantity: VP QL-coding, phase 1\n    value: 7\n    tolerance: 0.7\n  - quantity: NAc QR-coding, phase 1\n    value: 11\n    tolerance: 1.1\n  - quantity: VP QR-coding, phase 1\n    value: 7\n    tolerance: 0.7\n  - quantity: NAc QL-coding, phase 2\n    value: 12\n    tolerance: 1.2\n  - quantity: VP QL-coding, phase 2\n    value: 12\n    tolerance: 1.2\n  - quantity: NAc QR-coding, phase 2\n    value: 12\n    tolerance: 1.2\n  - quantity: VP QR-coding, phase 2\n    value: 6\n    tolerance: 0.6\n  - quantity: NAc QL-coding, phase 3\n    value: 11\n    tolerance: 1.1\n  - quantity: VP QL-coding, phase 3\n    value: 14\n    tolerance: 1.4\n  - quantity: NAc QR-coding, phase 3\n    value: 8\n    tolerance: 0.8\n  - quantity: VP QR-coding, phase 3\n    value: 7\n    tolerance: 0.7\n  criterion: Block comparisons by Mann-Whitney U test at p < 0.01 on the last 20 choice trials\n    of each block (opening comment). Several blocks of one type in a session are pooled. The\n    10% tolerance is under one neuron for most counts, so each count is also judged within\n    ±2 neurons. Reproduced when, under that rule, all 12 counts match; partially reproduced\n    when at least 9 do and every count is below 25% of its region.\n- id: fig8b-action-command-coding\n  statement: Before action initiation (phase 3), 11% of NAc neurons (17 of 148) and 18% of VP\n    neurons (12 of 66) code the action to be chosen (action command-coding neurons).\n  source: Results, Neuronal activity in the NAc and VP, paragraph 4; Figure 8B\n  quote: Neurons encoding the action to be chosen before execution represented 11% (17 of 148) of\n    the neurons in the NAc and 18% (12 of 66) of those in the VP (action command-coding neurons)\n  depends_on:\n  - neuron-counts\n  expected:\n  - quantity: NAc action command-coding neurons\n    value: 17\n    tolerance: 1.7\n  - quantity: VP action command-coding neurons\n    value: 12\n    tolerance: 1.2\n  criterion: Mann-Whitney U test at p < 0.01 of phase-3 spike counts, left against right choice\n    trials. Reproduced when both counts are within tolerance.\n- id: fig8b-action-coding\n  statement: After action onset (phase 4), 41% of NAc neurons (61 of 148) and 39% of VP neurons\n    (26 of 66) code the selected action.\n  source: Results, Neuronal activity in the NAc and VP, paragraph 4; Figure 8B\n  quote: After the action onset (phase 4), the proportion of action-coding neurons increased to\n    41% (61 of 148) in the NAc and 39% (26 of 66) in the VP\n  depends_on:\n  - neuron-counts\n  expected:\n  - quantity: NAc action-coding neurons\n    value: 61\n    tolerance: 6.1\n  - quantity: VP action-coding neurons\n    value: 26\n    tolerance: 2.6\n  criterion: Mann-Whitney U test at p < 0.01 of phase-4 spike counts, left against right choice\n    trials. Reproduced when both counts are within tolerance.\n- id: fig8b-reward-coding\n  statement: After the reward or no-reward tone (phase 5), 63% of NAc neurons (93 of 148) and 68%\n    of VP neurons (45 of 66) code reward availability.\n  source: Results, Neuronal activity in the NAc and VP, paragraph 4; Figure 8B\n  quote: After the onset of the reward tone or no-reward tone (phase 5), 63% (93 of 148) of NAc\n    neurons and 68% (45 of 66) of VP neurons coded reward availability\n  depends_on:\n  - neuron-counts\n  expected:\n  - quantity: NAc reward-coding neurons\n    value: 93\n    tolerance: 9.3\n  - quantity: VP reward-coding neurons\n    value: 45\n    tolerance: 4.5\n  criterion: Mann-Whitney U test at p < 0.01 of phase-5 spike counts, rewarded against unrewarded\n    choice trials. Reproduced when both counts are within tolerance.\n- id: fig8b-nac-vp-same-event-coding\n  statement: The NAc and VP do not differ in the percentages of neurons coding trial type, action\n    command, chosen action and reward outcome.\n  source: Results, Neuronal activity in the NAc and VP, paragraph 5; Figure 8B\n  quote: Comparison of the percentages of coding neurons in the NAc and VP revealed no\n    differences with trial type, action command, chosen action, and reward outcome (Mann–Whitney\n    U test, p = 0.59, p = 0.19, p = 0.80, and p = 0.45, respectively)\n  statistics:\n  - about: state-coding, NAc against VP\n    test: Mann–Whitney U test\n    p: 0.59\n  - about: action command-coding, NAc against VP\n    test: Mann–Whitney U test\n    p: 0.19\n  - about: action-coding, NAc against VP\n    test: Mann–Whitney U test\n    p: 0.80\n  - about: reward-coding, NAc against VP\n    test: Mann–Whitney U test\n    p: 0.45\n  depends_on:\n  - fig8b-state-coding\n  - fig8b-action-command-coding\n  - fig8b-action-coding\n  - fig8b-reward-coding\n  criterion: A claim of absence, judged on the paper's test, a Mann-Whitney U test as O9 at\n    p < 0.05, for each of the four types. Reproduced when none of the four finds a difference;\n    not reproduced when any does. The four differences of percentages are reported either way.\n- id: fig8b-ql-vp-higher\n  statement: QL-coding neurons are a larger share of VP than of NAc neurons after cue onset\n    (phase 2) and before action initiation (phase 3).\n  source: Results, Neuronal activity in the NAc and VP, paragraph 5; Figure 8B\n  quote: Surprisingly, the percentages of QL-coding neurons both after cue onset (phase 2) and\n    before action initiation (phase 3) were significantly higher in the VP than in the NAc\n    (Mann–Whitney U test, p = 0.03 < 0.05, p = 0.004 < 0.01, respectively)\n  statistics:\n  - about: phase 2\n    test: Mann–Whitney U test\n    p: 0.03\n  - about: phase 3\n    test: Mann–Whitney U test\n    p: 0.004\n  depends_on:\n  - fig8b-action-value-psth\n  criterion: Mann-Whitney U test as O9 on QL-coding indicators, NAc against VP, per phase.\n    Reproduced when, in both phases, the VP percentage is higher with p < 0.05; partially\n    reproduced when this holds in one phase.\n- id: fig8b-qr-no-region-difference\n  statement: QR-coding neurons do not differ in share between the VP and NAc in phases 2 and 3.\n  source: Results, Neuronal activity in the NAc and VP, paragraph 5; Figure 8B\n  quote: whereas those of QR-coding neurons were not significantly different between areas at the\n    two different times (Mann–Whitney U test, p = 0.81, and 0.17)\n  statistics:\n  - about: phase 2\n    test: Mann–Whitney U test\n    p: 0.81\n  - about: phase 3\n    test: Mann–Whitney U test\n    p: 0.17\n  depends_on:\n  - fig8b-action-value-psth\n  criterion: A claim of absence, judged on the paper's test, a Mann-Whitney U test as O9 at\n    p < 0.05 on QR-coding indicators, NAc against VP, in phases 2 and 3. Reproduced when\n    neither finds a difference; the differences are reported either way.\n- id: preference-balance\n  statement: Among state-coding neurons (48% NAc, 36% VP preferring tone A), action\n    command-coding neurons (53%, 50% preferring left) and action-coding neurons (57%, 50%\n    preferring left), the share with each preference does not differ from 50%.\n  source: Results, Neuronal activity in the NAc and VP, paragraph 6\n  quote: Of the state-coding neurons, 48% (38 of 80) in the NAc and 36% (12 of 33) in the VP\n    showed a greater response to tone A than to tone B. Of the action command-coding neurons, 53%\n    (9 of 17) in the NAc and 50% (6 of 12) in the VP showed greater activity in left-selected\n    trials than in right-selected trials. In the action-coding neurons, 57% (35 of 61) in the NAc\n    and 50% (13 of 26) in the VP showed greater activity in left-selected than in right-selected\n    trials. All of these populations were not significantly different from 50% (Wilcoxon's\n    signed rank test, p > 0.05)\n  statistics:\n  - test: Wilcoxon's signed rank test\n    p: 0.05\n    p_relation: \">\"\n  depends_on:\n  - fig8b-state-coding\n  - fig8b-action-command-coding\n  - fig8b-action-coding\n  expected:\n  - quantity: NAc state-coding neurons preferring tone A\n    value: 48\n    tolerance: 4.8\n    unit: percent\n  - quantity: VP state-coding neurons preferring tone A\n    value: 36\n    tolerance: 3.6\n    unit: percent\n  - quantity: NAc action command-coding neurons preferring left\n    value: 53\n    tolerance: 5.3\n    unit: percent\n  - quantity: VP action command-coding neurons preferring left\n    value: 50\n    tolerance: 5.0\n    unit: percent\n  - quantity: NAc action-coding neurons preferring left\n    value: 57\n    tolerance: 5.7\n    unit: percent\n  - quantity: VP action-coding neurons preferring left\n    value: 50\n    tolerance: 5.0\n    unit: percent\n  criterion: A claim of absence, judged on the paper's test, a Wilcoxon signed-rank test at\n    p < 0.05 within each of the six populations. The test as written is reading O11 (a); the\n    sign test, O11 (b), is shown as a variant. Preference is the sign of the difference of mean\n    spike counts in the coding bin. Reproduced when none of the six tests finds a departure\n    from 50%; the six percentages are reported against the expected values either way.\n- id: nac-noreward-preference\n  statement: 73% of NAc reward-coding neurons (68 of 93) respond more to the no-reward than to\n    the reward tone, more than the 50% of chance, while the VP share (56%, 25 of 45) does not\n    differ from 50%.\n  source: Results, Neuronal activity in the NAc and VP, paragraph 6\n  quote: However, 73% (68 of 93) of the reward-coding neurons in the NAc showed a larger response\n    to the no-reward than to the reward tone. This percentage of cells was significantly larger\n    than the 50% predicted by chance (Wilcoxon's signed rank test, p < 0.0001). The percentage\n    of reward-coding neurons in the VP (56%; 25 of 45), however, was not significantly different\n    from 50% (Wilcoxon's signed rank test, p > 0.05)\n  statistics:\n  - about: NAc\n    test: Wilcoxon's signed rank test\n    p: 0.0001\n    p_relation: \"<\"\n  - about: VP\n    test: Wilcoxon's signed rank test\n    p: 0.05\n    p_relation: \">\"\n  depends_on:\n  - fig8b-reward-coding\n  expected:\n  - quantity: NAc reward-coding neurons preferring no reward\n    value: 73\n    tolerance: 7.3\n    unit: percent\n  - quantity: VP reward-coding neurons preferring no reward\n    value: 56\n    tolerance: 5.6\n    unit: percent\n  criterion: Preference by the sign of the phase-5 difference of mean spike counts. For the NAc,\n    under both readings of O11, the NAc percentage is above 50% and the test gives p < 0.0001.\n    The VP part is a claim of absence judged on O11 (a) at p < 0.05, with O11 (b) as a variant.\n    Reproduced when the NAc part holds under every reading and the VP test finds no departure;\n    partially reproduced when one part holds.\n- id: core-shell-no-difference\n  statement: Splitting NAc neurons into tentative core and shell groups by electrode position, the\n    same analyses find no difference between core and shell neurons.\n  source: Results, Neuronal activity in the NAc and VP, paragraph 7; supplemental Data 3 (not\n    available)\n  quote: The same analysis described above found no significant differences between core and\n    shell neurons (supplemental Data 3\n  depends_on:\n  - fig8b-nac-vp-same-event-coding\n  criterion: Supplemental Data 3, which holds the tests, is not in the text read. A claim of\n    absence, read as the analysis of fig8b-nac-vp-same-event-coding and fig8b-ql-vp-higher\n    (Mann-Whitney U test as O9 at p < 0.05 on per-neuron coding indicators) with core and shell\n    in place of NAc and VP, for state, action command, action, reward, and QL and QR coding in\n    phases 1 to 3. Core and shell as assigned in the dataset from Fig. 6; if the dataset does not\n    assign them, the claim cannot be tested. Reproduced when no test finds a difference.\n- id: fig8c-regression-action-value\n  statement: By regression on the block reward probabilities, QL-coding neurons are 9, 10 and 7%\n    of NAc neurons and 15, 24 and 26% of VP neurons in phases 1 to 3, and QR-coding neurons 11, 9\n    and 6% (NAc) and 9, 17 and 14% (VP).\n  source: Results, Neuronal activity in the NAc and VP, paragraph 8; Figure 8C\n  quote: QL-coding neurons, which were found to have a significant regression coefficient to QL (t\n    test, p < 0.01) but not to QR, were present in percentages of 9, 10, and 7% in the NAc, and\n    15, 24, and 26% in the VP for different time bins (Fig. 8A, phases 1–3) ... QR-coding neurons,\n    which were found to have a significant regression coefficient to QR (t test, p < 0.01) but\n    not to QL, were present in percentages of 11, 9, and 6% in the NAc, and 9, 17, and 14% in the\n    VP\n  depends_on:\n  - neuron-counts\n  expected:\n  - quantity: NAc QL-coding, phase 1\n    value: 9\n    tolerance: 0.9\n    unit: percent\n  - quantity: NAc QL-coding, phase 2\n    value: 10\n    tolerance: 1.0\n    unit: percent\n  - quantity: NAc QL-coding, phase 3\n    value: 7\n    tolerance: 0.7\n    unit: percent\n  - quantity: VP QL-coding, phase 1\n    value: 15\n    tolerance: 1.5\n    unit: percent\n  - quantity: VP QL-coding, phase 2\n    value: 24\n    tolerance: 2.4\n    unit: percent\n  - quantity: VP QL-coding, phase 3\n    value: 26\n    tolerance: 2.6\n    unit: percent\n  - quantity: NAc QR-coding, phase 1\n    value: 11\n    tolerance: 1.1\n    unit: percent\n  - quantity: NAc QR-coding, phase 2\n    value: 9\n    tolerance: 0.9\n    unit: percent\n  - quantity: NAc QR-coding, phase 3\n    value: 6\n    tolerance: 0.6\n    unit: percent\n  - quantity: VP QR-coding, phase 1\n    value: 9\n    tolerance: 0.9\n    unit: percent\n  - quantity: VP QR-coding, phase 2\n    value: 17\n    tolerance: 1.7\n    unit: percent\n  - quantity: VP QR-coding, phase 3\n    value: 14\n    tolerance: 1.4\n    unit: percent\n  criterion: Regression as the opening comment, y = b0 + b1 QL + b2 QR with QL and QR the block's\n    reward probabilities as fractions; the equation is missing, and the text names no other\n    regressor, so none is added. The 10% tolerance is under one neuron for most values, so each\n    is also judged within ±2 neurons of the reported percentage. Reproduced when, under that\n    rule, all 12 values match; partially reproduced when at least 9 do.\n- id: fig8c-ql-vp-higher\n  statement: In the regression analysis, QL-coding neurons are a larger share of VP than of NAc\n    neurons in phases 2 and 3.\n  source: Results, Neuronal activity in the NAc and VP, paragraph 8; Figure 8C\n  quote: In phases 2 and 3, there were significant differences in the size of the population of\n    QL-coding neurons in the NAc, and in the VP (p = 0.007 and 0.0001 < 0.01, Mann–Whitney U test)\n  statistics:\n  - about: phase 2\n    test: Mann–Whitney U test\n    p: 0.007\n  - about: phase 3\n    test: Mann–Whitney U test\n    p: 0.0001\n  depends_on:\n  - fig8c-regression-action-value\n  criterion: Mann-Whitney U test as O9, NAc against VP, on regression QL-coding indicators.\n    Reproduced when, in both phases, the VP share is higher with p < 0.01; partially reproduced\n    when both give p < 0.05 or one gives p < 0.01.\n- id: fig8c-regression-detects-more\n  statement: Regression detects slightly more action value-coding neurons (Fig. 8C) than the\n    block comparison (Fig. 8B), and the two are consistent.\n  source: Results, Neuronal activity in the NAc and VP, paragraph 8\n  quote: These regression analysis results were consistent with those obtained by comparing the\n    perievent time histograms (Fig. 8B). However, the number of the detected action value-coding\n    neurons was slightly larger in Figure 8C than in Figure 8B\n  depends_on:\n  - fig8b-action-value-psth\n  - fig8c-regression-action-value\n  criterion: Total QL- plus QR-coding neurons over phases 1 to 3 and both regions, regression\n    against block comparison. Reproduced when the regression total is larger, and the region\n    with the larger QL share in phases 2 and 3 is the VP in both analyses.\n- id: fig8d-state-value-vp-higher\n  statement: State value-coding neurons are 12, 8 and 8% of NAc neurons and 18, 20 and 20% of VP\n    neurons in phases 1 to 3, with the VP share larger in phases 2 and 3.\n  source: Results, Neuronal activity in the NAc and VP, paragraph 8; Figure 8D\n  quote: State value-coding neurons, which were found to have a significant regression\n    coefficient to [QL(t) + QR(t)] but not to [QL(t) − QR(t)], were present in percentages of 12,\n    8, and 8% in the NAc, and 18, 20, and 20% in the VP (Fig. 8D). In phases 2 and 3, these\n    differences between the sizes of the populations in the NAc and VP were significant (p =\n    0.02 and 0.02 < 0.05, respectively; Mann–Whitney U test)\n  statistics:\n  - about: phase 2\n    test: Mann–Whitney U test\n    p: 0.02\n  - about: phase 3\n    test: Mann–Whitney U test\n    p: 0.02\n  depends_on:\n  - neuron-counts\n  expected:\n  - quantity: NAc state value-coding, phase 1\n    value: 12\n    tolerance: 1.2\n    unit: percent\n  - quantity: NAc state value-coding, phase 2\n    value: 8\n    tolerance: 0.8\n    unit: percent\n  - quantity: NAc state value-coding, phase 3\n    value: 8\n    tolerance: 0.8\n    unit: percent\n  - quantity: VP state value-coding, phase 1\n    value: 18\n    tolerance: 1.8\n    unit: percent\n  - quantity: VP state value-coding, phase 2\n    value: 20\n    tolerance: 2.0\n    unit: percent\n  - quantity: VP state value-coding, phase 3\n    value: 20\n    tolerance: 2.0\n    unit: percent\n  criterion: Regression y = b0 + b1 (QL + QR) + b2 (QL - QR) on the last 20 choice trials of each\n    block (Methods, Regression analysis); t test at p < 0.01; Mann-Whitney U test as O9.\n    Percentages judged within ±2 neurons where 10% is under one neuron. Reproduced when the six\n    values match and the VP share is higher in phases 2 and 3 with p < 0.05; partially\n    reproduced when the test result holds and at least four values match.\n- id: fig8d-policy\n  statement: Policy-coding neurons are 10, 9 and 7% of NAc neurons and 11, 15 and 14% of VP neurons\n    in phases 1 to 3.\n  source: Results, Neuronal activity in the NAc and VP, paragraph 8; Figure 8D\n  quote: Policy-coding neurons, which were found to have a significant regression coefficient to\n    [QL(t) − QR(t)] but not to [QL(t) + QR(t)], were present in percentages of 10, 9, and 7% in\n    the NAc, and 11, 15, and 14% in the VP (Fig. 8D)\n  depends_on:\n  - neuron-counts\n  expected:\n  - quantity: NAc policy-coding, phase 1\n    value: 10\n    tolerance: 1.0\n    unit: percent\n  - quantity: NAc policy-coding, phase 2\n    value: 9\n    tolerance: 0.9\n    unit: percent\n  - quantity: NAc policy-coding, phase 3\n    value: 7\n    tolerance: 0.7\n    unit: percent\n  - quantity: VP policy-coding, phase 1\n    value: 11\n    tolerance: 1.1\n    unit: percent\n  - quantity: VP policy-coding, phase 2\n    value: 15\n    tolerance: 1.5\n    unit: percent\n  - quantity: VP policy-coding, phase 3\n    value: 14\n    tolerance: 1.4\n    unit: percent\n  criterion: As fig8d-state-value-vp-higher, for the QL - QR coefficient. Reproduced when the six\n    values match (±2 neurons where 10% is under one neuron); partially reproduced when at least\n    four do.\n- id: fig8-above-chance\n  statement: Every coding population of Figure 8 is larger than expected by chance.\n  source: Results, Neuronal activity in the NAc and VP, paragraph 8; Figure 8 legend\n  quote: All percentages shown in Figure 8 were significantly larger than those predicted by\n    chance (p < 0.01, binomial test)\n  statistics:\n  - test: binomial test\n    p: 0.01\n    p_relation: \"<\"\n  depends_on:\n  - fig8b-state-coding\n  - fig8b-action-value-psth\n  - fig8b-action-command-coding\n  - fig8b-action-coding\n  - fig8b-reward-coding\n  - fig8c-regression-action-value\n  - fig8d-state-value-vp-higher\n  - fig8d-policy\n  criterion: One-sided binomial test of each count of Fig. 8B to 8D against the chance level O10.\n    Reproduced when, under every reading, every population gives p < 0.01; partially reproduced\n    when at least 90% of them do.\n- id: fig9-state-information\n  statement: Information about the trial type (state) in the NAc and VP rises right after cue onset\n    and again after center-hole exit.\n  source: Results, Neuronal activity in the NAc and VP, paragraph 9; Figure 9A and 9B\n  quote: The information coding state in the NAc and VP (green lines) increased immediately after\n    the onset of the cue tone, and again after exiting from the center hole\n  depends_on:\n  - neuron-counts\n  criterion: MI as the opening comment, tone A against tone B, choice and no-choice trials,\n    averaged per region, windows O12. \"Immediately after\" is read as within 0.5 s of cue onset.\n    Reproduced when, under every reading and in both regions, the state MI exceeds the threshold\n    within 0.5 s after cue onset and is higher there than in the 0.5 s before it, and the curve\n    aligned to center-hole exit has a local maximum above threshold after the exit that\n    exceeds its value at the exit.\n- id: fig9-action-information\n  statement: Information about the chosen action is very weak before center-hole exit, rises\n    rapidly after it, and peaks around entry to the L or R hole.\n  source: Results, Neuronal activity in the NAc and VP, paragraph 9; Figure 9B\n  quote: Information related to action choice was very weak in both the NAc and VP before the\n    onset of the choice (before the exit of the center hole), but increased rapidly after the\n    choice onset, and showed a peak around the time of entry to the left or right hole\n  depends_on:\n  - neuron-counts\n  - reaction-time\n  criterion: MI between firing and left or right choice, choice trials, aligned to center-hole\n    exit, windows O12. Reproduced when, under every reading and in both regions, the mean MI over\n    windows before the exit is below a fifth of the peak, and the peak lies after the exit\n    within 0.5 s of the median reaction time (L or R entry).\n- id: fig9-reward-information\n  statement: Information about reward rises when the reward or no-reward tone is presented at L or\n    R entry, then decreases gradually but lasts until the next trial.\n  source: Results, Neuronal activity in the NAc and VP, paragraph 9; Figure 9B; Discussion,\n    Information coding in NAc and VP, paragraph 1\n  quote: Information related to the reward started to increase at the presentation of\n    reward/no-reward tone, which was presented at the time of entry to the left or right hole.\n    The reward information gradually decreased, but was sustained until the subsequent trial\n  depends_on:\n  - neuron-counts\n  criterion: MI between firing and reward outcome, choice trials, aligned to center-hole exit\n    (Fig. 9B) and, for the next trial, to the next cue onset (Fig. 9A, \"previous reward\"), with\n    the previous trial's outcome as the event; windows O12. Reproduced when, under every reading\n    and in both regions, reward MI is below threshold before the L or R entry, rises above it\n    after, and the previous-trial reward MI is above threshold around the next cue onset.\n- id: fig9-action-value-information-low\n  statement: Information about the action values QL and QR is above the significance threshold in\n    the NAc and VP but low and without clear peaks, while state, action and reward information\n    are robust.\n  source: Results, Neuronal activity in the NAc and VP, paragraph 10; Figure 9; Discussion,\n    Information coding in NAc and VP, last paragraph but one\n  quote: Information regarding action values QL and QR in the NAc and VP were found to be larger\n    than the threshold values, indicating a significant level of information (p < 0.01) (see\n    Materials and Methods). However, this level of information was still relatively low and\n    without clear peaks, whereas information about state, action, and reward was robustly\n    represented in the NAc and VP\n  depends_on:\n  - fig5-variable-models-best\n  - fig9-state-information\n  - fig9-action-information\n  - fig9-reward-information\n  criterion: QL and QR from F-Q with time-varying parameters (Table 2 sigmas), binarized at the\n    median (O13), MI as the opening comment, windows O12. Reproduced when, under every reading\n    and in both regions, QL and QR MI exceed the threshold in most windows (over half), their\n    peak is below the peaks of state, action and reward MI, and their maximum is less than\n    twice their median over windows (no clear peak); partially reproduced when the comparison\n    with the other events holds but the above-threshold or flatness part does not.\n- id: action-information-outlasts-reward-peak\n  statement: Information about the chosen action in the NAc and VP lasts beyond the peak of reward\n    information.\n  source: Discussion, Information coding in NAc and VP, paragraph 3; Figure 9\n  quote: In particular, we showed that a representation of information regarding action in the\n    NAc and VP lasted beyond the peak of information regarding reward (Fig. 9)\n  depends_on:\n  - fig9-action-information\n  - fig9-reward-information\n  criterion: On the curves of Fig. 9B (O12). Reproduced when, under every reading and in both\n    regions, action MI is above threshold at the time of the reward MI peak and in the window\n    0.5 s after it.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/001641/10.1523-jneurosci.6157-08.2009.yaml paper/10.1523-jneurosci.6157-08.2009.txt; grep -nP "\x{2014}|\brather\b" claims/001641/*.yaml; python3 - <<'E'
import yaml,re
d=yaml.safe_load(open('claims/001641/10.1523-jneurosci.6157-08.2009.yaml'))
def walk(x,p=''):
    if isinstance(x,dict):
        for k,v in x.items(): walk(v,p+'.'+str(k))
    elif isinstance(x,list):
        for i,v in enumerate(x): walk(v,p+f'[{i}]')
    elif isinstance(x,str) and ': ' in x: print('colon',p,x[:60])
walk(d)
E
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
import yaml;d=yaml.safe_load(open('claims/001641/10.1523-jneurosci.6157-08.2009.yaml'))['claims']
print(sum('criterion' in c for c in d), sum('statistics' in c for c in d), sum(len(c.get('statistics',[])) for c in d), sum('expected' in c for c in d))"; git status --short
```

```
46 13 23 28
?? .bash_profile
?? .bashrc
?? .gitconfig
?? .idea
?? .mcp.json
?? .profile
?? .ripgreprc
?? .vscode
?? .zprofile
?? .zshrc
?? claims/001641/
?? scripts
```

**Agent**

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

## End of run

20 turns, 8 minutes, result: success.
