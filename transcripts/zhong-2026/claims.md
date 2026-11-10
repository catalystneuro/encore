# zhong-2026 · claims · run 42747998148

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md; ls paper/ | grep -i zhong; ls claims | head; wc -l claims/fouke-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1,200p docs/protocol.md; ls paper/; ls paper/* | grep -i zhong
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  cat claims/fouke-2025.yaml; cat papers/datasets/zhong-2026.yaml; wc -c paper/*; head -30 paper/10.7554-elife.109538.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.109538.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.109538.txt",
 "offset": 493
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls tools schema* docs 2>/dev/null | head -50; grep -rn "kind" docs/protocol.md | head -20; grep -l "relation: reuses" papers/datasets/*.yaml | head -3
```

```
docs:
agents
archives.md
conversion-tracker.md
design.md
encore.md
fixing-conversions.md
paper-first.md
pilot-notes
pilot-notes.md
pipeline.md
protocol.md
queue.md

schemas:
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json

[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat schemas/claims.schema.json; head -40 claims/kussovska-2025.yaml 2>/dev/null
```

```
Exit code 1
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Claims proposed for one target (a dataset and one of its papers)",
  "description": "Draft. To be revised after the pilot.",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schema_version",
    "paper",
    "claims"
  ],
  "properties": {
    "schema_version": {
      "const": 2
    },
    "dataset": {
      "description": "Before the cutover to paper-first records, the dataset a per-dataset claims file was read for. A paper's own claims file (claims/<paper>.yaml) leaves it out.",
      "type": "object",
      "additionalProperties": false,
[... 334 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -rln "simulat" claims/ | head; grep -rn -B2 -A6 "model simulation\|numerical simulation" claims/*.yaml | head -60
```

```
claims/li-2016/crcns-alm-3.yaml
claims/li-2016/000011.yaml
claims/qu-2025.yaml
claims/bouchard-2013.yaml
claims/kaku-2025.yaml
claims/wang-2014.yaml
claims/najafi-2020.yaml
claims/silkuniene-2025/001276.yaml
claims/silkuniene-2025/001047.yaml
claims/silkuniene-2025/001277.yaml
claims/siegle-2021.yaml-361-    simulated ladder-like hierarchy with feedback (0.88), above a one-to-all (0.15) or
claims/siegle-2021.yaml-362-    three-level (0.38) network and below a strongly feedforward one (1.54).
claims/siegle-2021.yaml:363:  source: Methods, Network model simulation; Extended Data Fig. 8
claims/siegle-2021.yaml-364-  quote: The maximum difference of this trajectory (here between V1 and AM) is defined as the
claims/siegle-2021.yaml-365-    total hierarchy score (THS) of the network, which is 0.89 for the measured functional network
claims/siegle-2021.yaml-366-    in our data ... The resulting DS matrix showed a gradient very similar to the real data, with
claims/siegle-2021.yaml-367-    a THS equal to 0.88
claims/siegle-2021.yaml-368-  data: elsewhere
claims/siegle-2021.yaml-369-  where: DANDI:000021 and DANDI:000022 (the paper's Data availability)
--
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -B3 -A12 "simulat" claims/qu-2025.yaml claims/wang-2014.yaml | head -80
```

```
claims/qu-2025.yaml-14-#
claims/qu-2025.yaml-15-# Code. The paper links github.com/Wilbrecht-Lab/cogmodels, read at commit 589555c ("preliminary
claims/qu-2025.yaml-16-# codebase", 2025-02-20). It holds the cognitive models (RL4p, RLCF, RLFQ3p, RL_meta, PearceHall,
claims/qu-2025.yaml:17:# RFLR, BIfp, BRLfwr, BRLfw, BRLwrp and others), their maximum-likelihood fitting, simulation
claims/qu-2025.yaml-18-# ("generate", a fresh task; "emulate", the model choosing on a mouse's sessions), parameter
claims/qu-2025.yaml-19-# recovery and model identification drivers (utils_test.py), and a plot of stay probability by
claims/qu-2025.yaml-20-# two-trial history. It holds no behavioural preprocessing, no photometry preprocessing, and none
claims/qu-2025.yaml-21-# of the neural analyses (DA-PT, the RPE regressions, cross-validation, the LMER models). Choices
claims/qu-2025.yaml-22-# the code settles, used below:
claims/qu-2025.yaml-23-# - Fits are per mouse over all its sessions (fit_model_per_subject), L-BFGS-B with the code's
claims/qu-2025.yaml-24-#   bounds, tol 1e-6, one start drawn from the Methods' initial distributions; seed 230 is a
claims/qu-2025.yaml-25-#   standard choice that cannot change an outcome. AIC = 2k + 2 NLL per mouse, k the number of
claims/qu-2025.yaml-26-#   fitted parameters.
claims/qu-2025.yaml-27-# - Miss trials (no choice, Decision -1) are left out of the likelihood and give a stickiness
claims/qu-2025.yaml-28-#   term of 0 on the next trial. At each new session the belief returns to 0.5 and Q values and
claims/qu-2025.yaml-29-#   BRL weights to their initial values (gam = 1).
--
claims/qu-2025.yaml-34-#   starts at 1 and Q values at 0. Table 1 lists alpha+, alpha-, phi, alpha_nu and zeta; the
claims/qu-2025.yaml-35-#   code's list is used, as Eq 2 applies beta to every model and Eq 16 names psi.
claims/qu-2025.yaml-36-# - RL_meta has 7 parameters as in Table 1; omega starts at 0 and alpha-_t at alpha-.
[... 60 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/zhong-2026.yaml",
 "content": "# Claims for Zhong, Katkov & Tsodyks (2026), \"Synaptic Theory of Chunking in Working Memory\",\n# eLife, doi:10.7554/elife.109538, tested on DANDI:000207.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"),\n# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md.\n#\n# Text read. paper/10.7554-elife.109538.txt, fetched from eLife's site. Its header says\n# \"version of record\", but the page it holds is the eLife Reviewed Preprint version 1\n# (doi:10.7554/eLife.109538.1, 9 January 2026, \"Not revised\"). It holds the main text, the\n# Methods (sections A to E), the legends of Figures 1 to 4 and of the supplementary Figures S1\n# to S3, and the Data availability statement. No PDF was supplied. The equations (1) to (15)\n# and the values of Table I (simulation parameters) did not survive extraction; Eq. (1) is\n# known from the text as M* = 2^(C-1) (\"M ∗ = 24−1 = 8\" for C = 4, and \"M ∗ = 2C−1\" in the\n# Figure 4 legend, superscripts lost). Figure axes and plotted values could not be read.\n#\n# Code. The paper links none. Data availability says \"The code for simulation will be made\n# available in a Github repository at a later stage\"; no analysis code for Figure 3 or Figure 4\n# is named. No repository or commit was read.\n#\n# Data the paper used.\n# - Figures 1, 2 and S1, S2 are numerical simulations of the rate model of Methods A, with the\n#   parameters of Table I (not in the text read) and the input timings of Methods C. No\n#   recorded data.\n# - Figure 3 and S3 reanalyse the single-neuron recordings of Zheng et al. 2022 (ref. [41],\n#   Nat Neurosci 25:358), downloaded from DANDI at dandiset 000207 version 0.220216.0323\n#   (Methods E). Drug-resistant epilepsy patients with depth electrodes in the medial temporal\n#   lobe watched movie clips, each made of two episodes separated by a cut in the middle. Cuts\n#   are soft boundaries (change of camera position) or hard boundaries (change of movie\n#   content); this paper pools neurons coding either as \"boundary neurons\". \"Onset neurons\"\n#   respond to clip onset. Of the 18 subjects in [41], 4 were left out (no onset-responsive or no\n#   cut-responsive neuron detected), so 14 are analysed. Measured variables are spike times of\n#   sorted units, clip onset times and cut times. Subject IDs named in Fig. S3 include P64CS and\n#   TWH120.\n# - Figure 4 uses behavioural recall data extracted from Miller and Selfridge 1950 (ref. [42],\n#   Am J Psychol 63:176) and its Danish (ref. [46], Maher and Skovengaard 1988) and Hindi\n#   (ref. [47], Sharma and Sen 1977) replications. Variables are the fraction of words\n#   recalled f, the passage length L in words, and the order n of the approximation to the\n#   language. These are published tables, not in any archive and not in DANDI:000207.\n#\n# Method details the paper fixes for Figure 3 (Methods E, Fig. 3 legend, Results paragraph on\n# Fig. 3). Soft and hard boundary neurons are pooled as boundary neurons; all other detected\n# neurons are non-boundary neurons; raw firing rates of all boundary (or non-boundary)\n# neurons of a subject are pooled, then z-scored and averaged across subjects; time zero is the\n# cut (Fig. 3a, b) or the clip onset (Fig. 3c); the shade is one standard deviation; 4 of 18\n# subjects are excluded by the rule above. Details the paper leaves open are named in each\n# criterion (how boundary and onset neurons are selected, bin width and smoothing, the plotted\n# window, the z-score reference, and how a dip and a ramp are judged). The paper reports no\n# statistical test for any finding.\nschema_version: 2\npaper: doi:10.7554/elife.109538\nclaims:\n- id: fig1d-basic-capacity-four\n  statement: In the network model with no chunking, after six items are presented at a uniform\n    pace, four clusters stay active as periodic population spikes and two drop out of working\n    memory, a basic capacity C of 4 for the chosen parameters.\n  source: Results, Chunking increases working memory capacity, paragraph 2; Figure 1D top\n  quote: At the end of the presentation, 4 of the corresponding clusters remain active in the\n    form of periodic population spikes while two other clusters drop out of WM, corresponding to\n    a WM capacity of 4 for the chosen values of parameters\n  expected:\n  - quantity: clusters active after presentation of six items, no chunking\n    value: 4\n    tolerance: 0\n    unit: clusters\n  criterion: A simulation result, not a finding on recorded data; DANDI:000207 cannot test it.\n    It needs the model of Methods A (Eqs. 2 to 8, lost in the text read), the parameters of\n    Table I (values not in the text read) and the timings of Methods C (stimuli from t = 1 s,\n    0.025 s long, every 0.45 s, input 750 Hz, background 10 Hz). The tolerance is 0 because the\n    value is a count of clusters and 10% of it is under one cluster.\n- id: fig1d-chunking-retrieves-six\n  statement: With slight pauses after the third and sixth items activating chunking clusters,\n    the network retrieves all six items chunk by chunk, while never holding more than four\n    active clusters at once.\n  source: Results, Chunking increases working memory capacity, paragraphs 2 and 3; Figure 1D\n    bottom and Figure S1\n  quote: This chunking scenario allows the retrieval of all six memory items while at any given\n    moment in time, the network maintains no more than four active clusters, not exceeding basic\n    WM capacity.\n  expected:\n  - quantity: items retrieved with chunking\n    value: 6\n    tolerance: 0\n    unit: items\n  - quantity: largest number of clusters active at once\n    value: 4\n    tolerance: 0\n    unit: clusters\n  criterion: A simulation result; DANDI:000207 cannot test it. Same model and gaps as\n    fig1d-basic-capacity-four, with the timings of Methods C for the bottom panel (chunking\n    clusters loaded for 0.025 s at 0.3 s intervals, background switching between 10 and -10 Hz\n    for 1.35 s during retrieval) and the chunking inhibition of Eq. (8). Tolerances are 0, as\n    counts.\n- id: eq1-new-magic-number\n  statement: With hierarchical chunking the largest number of items that can be held and\n    retrieved is M* = 2^(C-1), with C the basic capacity; for C = 4 this is 8, reached by a\n    binary tree of three levels (four chunks of two in two meta-chunks).\n  source: Results, Hierarchical chunking predicts a new capacity, paragraphs 1 to 3; Methods B\n  quote: Let us consider the example corresponding to C = 4, with a capacity of M ∗ = 24−1 = 8.\n    In this case, the optimal chunking structure is a binary tree with three levels\n  expected:\n  - quantity: M* for C = 4\n    value: 8\n    tolerance: 0\n    unit: items\n  criterion: A derivation (Methods B), not a finding on data; DANDI:000207 cannot test it.\n    It holds when maximising the number of stimulus clusters in a tree of K levels with integer\n    branching ratios c_k, subject to c_K plus the sum over k < K of (c_k - 1) being at most C,\n    gives 2^(C-1), and 8 for C = 4 with c = 2 at every level. Equations (9) to (14) are lost in\n    the text read; the constraint is taken from the words of Methods B. Tolerance 0, as a count.\n- id: fig2b-hierarchical-retrieval\n  statement: In simulation, eight items loaded as four chunks of two, grouped into two\n    meta-chunks by longer pauses, are maintained as two top-level chunking clusters and are\n    retrieved chunk by chunk with at most four clusters active.\n  source: Results, Hierarchical chunking predicts a new capacity, paragraphs 4 to 6; Figure 2B\n  quote: Eight memories are loaded as four chunks of two into the working memory network ...\n    Now, the first chunk has been retrieved, and the working memory maintains four clusters\n  expected:\n  - quantity: items loaded and retrieved\n    value: 8\n    tolerance: 0\n    unit: items\n  - quantity: clusters active while the first chunk is retrieved\n    value: 4\n    tolerance: 0\n    unit: clusters\n  criterion: A simulation result; DANDI:000207 cannot test it. Needs Table I (not in the text\n    read) and the timings of Methods C for Fig. 2(b) (stimuli from t = 1 s, 0.15 s long, every\n    0.45 s; chunking clusters 0.01 s long at 0.2 s intervals; background switching between 10\n    and -10 Hz for 0.8 s during retrieval), with Eq. (8) extended so that level-k chunking\n    clusters inhibit all lower-level clusters presented before them (Methods A).\n- id: figs2-delayed-hebbian-binding\n  statement: Replacing the imposed chunking inhibition (Eq. 8) by a time-delayed Hebbian\n    strengthening of chunk-to-stimulus inhibitory synapses approximates the activity of\n    Figures 1D and 2B, but needs fine-tuning of the presentation time, the integration window\n    and the threshold.\n  source: Methods D, paragraphs 3 and 4; Figure S2\n  quote: We find that Eq. (6)-(3) with Eq. (15), instead of Eq. (8), is able to approximate the\n    activity traces as in Fig. 1(d) and Fig. 2(b) (see Fig. S2). However, it requires\n    fine-tuning between the presentation time and the integration window τs, as well as the\n    threshold θ0.\n  criterion: A simulation result; DANDI:000207 cannot test it. Methods D gives the extra\n    parameters (tau_J = 75 s, J_min = 0, J_max = 10, kappa_J = 1 Hz; tau_s = 1.8 s and theta_0\n    = 7000 Hz for Fig. S2a, b; for Fig. S2c theta_0 = 25600 Hz, one fifth of it for level 1 to\n    2, tau_s = 1.9 s for adjacent and 3.1 s for skip levels), but Eq. (15) itself and Table I\n    are lost in the text read. \"Approximate\" has no measure in the paper.\n- id: methods-subjects-included\n  statement: Four of the eighteen subjects of Zheng et al. 2022 are left out of the Figure 3\n    analysis, because no onset-responsive or no cut-responsive neuron was detected in them,\n    leaving 14.\n  source: Methods E, paragraph 1\n  quote: We have excluded four subjects out of eighteen in [41] from our analysis, because in\n    those subjects either no neurons responding to the onset of the movie were detected, or no\n    neurons responding to the onset of the cut were detected.\n  data: dataset\n  expected:\n  - quantity: subjects in the dataset's encoding sessions\n    value: 18\n    tolerance: 0\n    unit: subjects\n  - quantity: subjects included after the exclusion\n    value: 14\n    tolerance: 0\n    unit: subjects\n  criterion: Subjects of DANDI:000207 version 0.220216.0323 with movie-watching (encoding)\n    data. A subject is excluded when the selection of fig3a-dip-after-boundary finds no\n    boundary neuron in it, or the selection of fig3c-onset-control finds no onset neuron. The\n    selection rules are open (see those claims); the count is reported under each reading.\n    Reproduced when, under one reading, 18 subjects are found and 14 kept. Counts are exact\n    (tolerance 0). Whether the 14 kept include P64CS and TWH120 (shown in Fig. S3) is\n    reported.\n- id: fig3a-dip-after-boundary\n  statement: Aligned to movie cuts and averaged over subjects and trials, the firing of\n    non-boundary neurons dips about 130 ms after the peak of boundary-neuron firing, then\n    ramps up continuously, as the chunking model predicts.\n  source: Results, Experimental evidence for the existence of chunking clusters, paragraph 2;\n    Figure 3A\n  quote: we find that after the peak in the firing rate of boundary neurons (top panel of Fig. 3\n    (a)), about ~ 130 ms later, there is a dip in the average activities of the rest of the\n    recorded neurons (bottom panel of Fig. 3 (a)). Further-more, there is a continuous ramp-up\n    of activities following the dip.\n  data: dataset\n  depends_on:\n  - methods-subjects-included\n  expected:\n  - quantity: lag from the boundary-neuron peak to the non-boundary dip\n    value: 130\n    tolerance: 13\n    unit: ms\n  criterion: From the paper (Methods E, Fig. 3 legend). The 14 included subjects; trials\n    aligned to the cut (time zero); soft and hard boundary neurons pooled as boundary neurons\n    and all other detected neurons as non-boundary; per subject, the raw firing rates of all\n    boundary (or non-boundary) neurons pooled over neurons and trials, z-scored, and averaged\n    across subjects; the mean is the trace, one standard deviation the shade. Open, with the\n    readings run. (1) Boundary-neuron selection, which the paper takes from [41] without\n    giving the test; (a) the classification of [41] where the dataset or [41] gives it, (b)\n    re-selection by the method in the Methods of [41], cuts of either type. (2) Trials; clips\n    with a cut (soft and hard) only, the reading the text supports (\"each consisting of two\n    episodes separated by a cut\"). (3) Bins and smoothing; 10 ms and 25 ms bins, each with no\n    smoothing and with a Gaussian kernel of 50 ms SD. (4) Window, -1 to 2 s around the cut, a\n    standard choice. (5) Z-score reference; (a) the subject's whole trace in the window, (b)\n    its pre-cut part (-1 to 0 s). Measures fixed here as the paper gives none. Boundary peak\n    is the time of the maximum of the boundary trace after time zero; the dip is the minimum of\n    the non-boundary trace from that peak to 500 ms after it; the lag is the dip time minus\n    the peak time. A dip is present when its value is below the mean of the non-boundary trace\n    from -1 to 0 s; a ramp is present when a line fitted to the non-boundary trace from the dip\n    to 1 s after the cut has positive slope. Reproduced when the dip and the ramp are present\n    and the lag is within tolerance; partially reproduced when dip and ramp are present but the\n    lag is outside it. Tolerance is 10% of 130 ms, widened to one bin when the bin is wider,\n    since the lag cannot be resolved finer than a bin. The paper's \"about ~\" marks the value\n    as approximate.\n- id: fig3b-individual-subjects\n  statement: The dip-then-ramp of non-boundary neurons after a cut is seen in most individual\n    subjects, though not all (P64CS has no ramp and TWH120 has no dip).\n  source: Results, Experimental evidence for the existence of chunking clusters, paragraph 2;\n    Figure 3B; Figure S3 legend\n  quote: While some subjects do not exhibit the qualitative trend as predicted (e.g., the firing\n    rate of subject P64CS does not have a ramp, and TWH120 does not have a dip), most of the\n    subjects’ firing rates follow the same qualitative trend as observed in the average plot in\n    Fig. 3(a).\n  data: dataset\n  depends_on:\n  - methods-subjects-included\n  - fig3a-dip-after-boundary\n  criterion: Per included subject, the non-boundary trace of fig3a-dip-after-boundary\n    (that subject's pooled neurons, all its cut trials), with the dip and ramp tests of that\n    claim and its readings, the boundary peak being that subject's own (the red dashed line of\n    Fig. S3). \"Most\" is read as more than half of the 14 subjects. Reproduced when more than\n    half show both a dip and a ramp under a reading; partially reproduced when they do but\n    P64CS shows a ramp or TWH120 shows a dip under every reading. The count, and the subjects\n    sorted by dip time as in Fig. 3(b), are reported.\n- id: fig3c-onset-control\n  statement: Aligned to movie onset, onset-responsive neurons show a peak, but the remaining\n    neurons (boundary neurons included) show no dip-then-ramp, so the pattern is specific to\n    boundary neurons.\n  source: Results, Experimental evidence for the existence of chunking clusters, paragraph 2;\n    Figure 3C\n  quote: Aligning firing rates to the movie onset, we observe a peak in the on-set neurons as\n    reported in [41]; however, unlike Fig. 3 (a), the remaining neurons (including boundary\n    neurons) do not exhibit the dip-then-ramp pattern (Fig. 3 (c)).\n  data: dataset\n  depends_on:\n  - methods-subjects-included\n  - fig3a-dip-after-boundary\n  criterion: A claim of absence; the paper uses no test, only the traces. The same pooling,\n    z-scoring, bins and window as fig3a-dip-after-boundary, aligned to clip onset; onset\n    neurons against all other neurons. Onset-neuron selection is open; (a) the onset cells of\n    [41] where the dataset or [41] gives them, (b) re-selection by the method in the Methods\n    of [41] for clip-onset responses. Reproduced when the onset trace peaks after time zero\n    and the non-onset trace fails the dip-and-ramp test of fig3a-dip-after-boundary (taken\n    from the onset peak); not reproduced when it passes. The non-onset dip depth and ramp slope\n    are reported either way.\n- id: fig4a-universal-slope\n  statement: Plotted against log2 of passage length, the fraction of recalled words for each\n    order of approximation to English falls on a straight line, and all lines collapse onto one\n    common line by shifting their intercepts.\n  source: Results, Experimental tests of the new magic number, paragraph 2; Figure 4A\n  quote: we replotted the data from [42] in a semi-log plot (with f as a function of log2 L) and\n    observed that all the different n-gram curves are well approximated by straight lines. We\n    hence collapsed all the curves into a common line by adjusting the individual intercepts\n  data: elsewhere\n  where: Miller and Selfridge 1950, Am J Psychol 63:176 (published recall table); not in any\n    archive\n  criterion: Not testable on DANDI:000207. On the data of [42], f against log2 L per order n,\n    one common slope with a separate intercept per n. The fitting method is open; (a) least\n    squares with a shared slope, (b) the mean of the separate slopes. No measure of \"well\n    approximated\" is given.\n- id: fig4b-plateau-near-eight\n  statement: The critical length Lc of perfect recall, found by extrapolating each curve to f = 1\n    with the common slope, increases with the order of approximation and plateaus from about\n    n = 4 at roughly 8 words, the predicted M* for C = 4.\n  source: Results, Experimental tests of the new magic number, paragraph 2; Figure 4B\n  quote: Lc increases with n as expected but starts to plateau around n = 4, saturating at\n    roughly the predicted value of 8.\n  data: elsewhere\n  where: Miller and Selfridge 1950, Am J Psychol 63:176 (published recall table); not in any\n    archive\n  depends_on:\n  - fig4a-universal-slope\n  expected:\n  - quantity: Lc at the plateau\n    value: 8\n    tolerance: 0.8\n    unit: words\n  criterion: Not testable on DANDI:000207. Lc per n is the L at which the fitted line of\n    fig4a-universal-slope reaches f = 1 (Fig. 4 legend). Reproduced when Lc rises with n up to\n    n = 4 and the values from n = 4 on are within tolerance of 8.\n- id: fig4b-three-languages\n  statement: Danish and Hindi replications of the Miller-Selfridge experiment give the same\n    trend, and in all three languages Lc saturates in the region predicted by M* = 2^(C-1) with\n    C = 4.\n  source: Results, Experimental tests of the new magic number, paragraphs 2 and 3; Figure 4B\n  quote: The same analysis of two replicates of the Miller-Selfridge experiment in Danish and\n    Hindi [46, 47] reveals similar trends. ... Notably, in Fig. 4(b) for all three languages, Lc\n    saturates within the region predicted by M ∗ = 2C−1, when substituting for C = 4 [4].\n  data: elsewhere\n  where: Maher and Skovengaard 1988, Scand J Psychol 29:194; Sharma and Sen 1977, Indian J\n    Psychol (published recall tables); not in any archive\n  depends_on:\n  - fig4b-plateau-near-eight\n  criterion: Not testable on DANDI:000207. The analysis of fig4a-universal-slope and\n    fig4b-plateau-near-eight applied to each replication. \"Within the region predicted\" is\n    open; (a) the plateau within 10% of 8, (b) the plateau at or below 8.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Now running the quote checker and schema validation.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/zhong-2026.yaml paper/10.7554-elife.109538.txt; python -c "
import yaml,json,jsonschema
d=yaml.safe_load(open('claims/zhong-2026.yaml'))
jsonschema.validate(d,json.load(open('schemas/claims.schema.json')));print('schema ok',len(d['claims']))"; grep -nP '[^"]\S: ' claims/zhong-2026.yaml | grep -v '^\S*\s*-\? \?[a-z_]*: ' | head; grep -n '—\|rather' claims/zhong-2026.yaml
```

Result: not kept, because it reads the paper's text.

**Agent**

I've written `claims/zhong-2026.yaml`. It has 12 claims, all with quotes. The quote checker reports no problems and the file validates against the claims schema. Nothing is committed.

**Text read.** `paper/10.7554-elife.109538.txt`. Its header says "version of record", but the page it holds is the eLife Reviewed Preprint v1 (doi:10.7554/eLife.109538.1, 9 Jan 2026, "Not revised"). It has the main text, Methods A to E, the legends of Figs 1 to 4, the supplementary legends S1 to S3, and the Data availability statement. There is no PDF. The paper links no code: it says the simulation code "will be made available in a Github repository at a later stage", so no repository was read.

**Claims.**
- **Statistics:** none. The paper reports no statistical test anywhere.
- **Expected values:** 7 claims have them (11 values in all).
- **Criteria:** all 12 claims have one.
- **Testable on DANDI:000207 (5):** the subject count (18 subjects, 14 kept); the dip in non-boundary neurons about 130 ms after the boundary-neuron peak, then a ramp (Fig. 3a); the same pattern in individual subjects, except P64CS and TWH120 (Fig. 3b, S3); and the control showing no dip at clip onset (Fig. 3c).
- **Simulation or theory (4):** basic capacity of 4 (Fig. 1d top); chunking retrieves all 6 items (Fig. 1d bottom); the new limit M* = 2^(C-1), which is 8 for C = 4 (Eq. 1); hierarchical retrieval (Fig. 2b).
- **Model variant (1):** delayed Hebbian binding as a replacement for the imposed chunking inhibition (Fig. S2).
- **`data: elsewhere` (3):** the Fig. 4 claims rest on the published recall tables of Miller and Selfridge (1950) and its Danish and Hindi replications. These are in no archive.
- **No `data` field:** the schema has no value for simulation, so those claims keep the default, which implies the dataset. Each criterion says the dataset cannot test it.

**Details left open, with the readings named.**
- **Boundary-neuron selection:** (a) the classification of the earlier paper on these data (Zheng et al. 2022), or (b) re-selection by that paper's own method.
- **Onset-neuron selection:** the same two readings.
- **Trials:** clips with a cut (soft and hard) only. This is the one reading the text supports.
- **Bins and smoothing:** 10 or 25 ms bins, each with no smoothing or a 50 ms Gaussian kernel.
- **Window:** -1 to 2 s around the cut, a standard choice.
- **Z-score reference:** (a) the whole window, or (b) the pre-cut part only.
- **Dip, ramp and lag:** the paper gives no measures, so I fixed them and labelled them as such. The dip is the minimum within 500 ms after the boundary peak, below the pre-cut mean. The ramp is a positive slope from the dip to 1 s after the cut. The lag tolerance is widened to one bin when the bin is wider than 13 ms.
- **"Most subjects":** read as more than half of the 14.
- **Fig. 4a common slope:** (a) one least-squares fit with a shared slope, or (b) the mean of the separate slopes.
- **"Within the region predicted" (Fig. 4b):** (a) within 10% of 8, or (b) at or below 8.

**Missing from the text.**
- **Equations and parameters:** Eqs. (1) to (15) and the Table I simulation parameters did not survive extraction. Eq. (1) is recovered from the words in the text. These gaps block rerunning the simulation claims, but they are not on the dataset.
- **Figure values:** with no PDF, figure axes and plotted values could not be read.

None of the Fig. 3 claims needs any of this.

## End of run

12 turns, 3 minutes, $1.02 at API prices, result: success.
