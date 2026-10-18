# Pilot notes

What each pilot attempt taught about the process. These feed the revision of
the schemas and the design after the pilot (docs/design.md, "Phasing").

## 000582, Sargolini et al. 2006 (2026-10-13)

Outcome: two claims reproduced, one partially. See
[`attempts/000582-sargolini-2006-01.yaml`](../attempts/000582-sargolini-2006-01.yaml).

### What happened

1. An agent wrote the claims from the paper's abstract, explored the dandiset,
   wrote a helper module and a notebook, and recorded three outcomes.
2. A second agent, which had not seen the first one's conclusions, reviewed the
   executed notebook and the code. It disagreed on one claim and listed ten
   questionable choices.
3. One of them was a real error: the analysis assumed a 1 m enclosure because
   every file says so, but 23 sessions used larger ones. Fixing it changed the
   disputed result substantially.
4. The verifier reviewed the corrected version, agreed with all three
   outcomes, and flagged three sentences that overstated the numbers. Those
   were corrected.

### Lessons

- **Verification by an independent agent is worth its cost.** It found an
  error that changed a result, and through it a metadata error in the
  dandiset. It took two rounds and about as much effort as the attempt.
- **Withholding the author's conclusions in the first round worked.** The
  verifier formed its own view and disagreed. In the second round it checked
  the written conclusions against the outputs, which caught overstatements.
  Both passes are useful and they are different jobs.
- **The verifier needs data-sanity outputs it cannot produce itself.** It
  could not check position ranges, units or layer labels from the executed
  notebook. Every reproduction notebook should print a standard set: ranges
  and units of each variable used, counts by group, and anything the analysis
  assumes from the metadata, checked against the data.
- **Do not trust descriptive metadata; check it against the data.** The
  enclosure size in the session description was wrong for a fifth of the
  sessions. This belongs in the agent protocol as a rule.
- **A closed-access paper limits claims to the abstract.** Figure-level claims
  and the paper's analysis criteria were not available, and the one partial
  outcome turns on a criterion that could not be read. The queue should record
  whether a target's paper is open, and closed ones should be expected to give
  coarser results.
- **"Partially reproduced" is carrying two meanings.** Here it means "the
  direction holds, the stated magnitude depends on an unknown criterion".
  Elsewhere it may mean "some panels yes, some no". The pilot should show
  whether an `inconclusive` outcome is needed.
- **Verification refers to a version.** The attempt changed between rounds, so
  each verification now records what it reviewed. The last edit after the
  second round (a per-rat table) has not been verified; the schema has no way
  to say "verified up to here" other than that note.
- **Statistics on cell-sessions are fragile.** Cells come from few animals and
  may repeat across sessions. A per-animal breakdown should be standard
  whenever the unit of analysis is a cell.
- **Provenance has a gap.** The agent that ran this attempt may not write its
  own model identifier into a repository, so the `model` field says "not
  recorded". The harness or the person running it has to supply it.

### Findings about the dandiset

These are the data-quality output for 000582:

- The enclosure size in the session description (1 x 1 m) is wrong for 23 of
  118 sessions, where positions span 1.5 to 2.5 m.
- No identifier links a cell across sessions.
- The dandiset is described as a sample of the paper's cells without saying
  how they were chosen.
- 47 sessions have one tracking LED although the description says two.

### Cost

About five minutes of compute per run of the notebook; the attempt, two
verification rounds and the fixes took one working session with a person
watching.

## 000127, Chowdhury, Glaser & Miller 2020 (2026-10-13)

Outcome: four claims reproduced, two partially, four blocked. See
[`attempts/000127-chowdhury-2020-01.yaml`](../attempts/000127-chowdhury-2020-01.yaml).

### What happened

1. The paper is open access, so the agent read the full results and methods
   and wrote ten figure-level claims.
2. The dandiset turned out to hold one of the paper's twelve sessions, repackaged
   for a machine-learning benchmark. Four claims could not be tested at all,
   and the main model had to be built from a substitute for data that is not
   included.
3. The first model fits were unusable: with a 120 ms window many neurons have
   almost no spikes. A firing-rate threshold, a small ridge penalty and a more
   stable way of scoring one trial type fixed that; all three are recorded as
   deviations.
4. The verifier, with the conclusions withheld, agreed on five of six outcomes
   and found no error that changes one. In the second round it agreed on all
   six and flagged ten sentences that overstated or were not backed by an
   output.

### Lessons

- **The link from a dandiset to a paper does not mean the dandiset holds the
  paper's data.** This one holds a twelfth of it. The first step of an attempt
  should be to establish which of the paper's sessions, subjects and variables
  are present, and to mark every claim that depends on the rest as blocked
  before any analysis. The queue cannot know this in advance.
- **Blocked claims are a large part of the output.** Four of ten here. They
  are what tells a data owner what is missing, and they need verifying like
  any other outcome: the verifier has to check the archive, not the notebook.
- **Outcome and method had to be separated.** Every claim here was tested on
  one session of four with a substituted model. Calling all of them "partially
  reproduced" would say nothing, so the outcome now describes the result only,
  and differences in method are listed as deviations (schema and design
  updated).
- **Full-text access changes the quality of the claims.** They name figures,
  carry numbers that can be checked (89% against 90%), and come with methods
  that can be followed. Compare 000582, where only the abstract was available.
- **Qualitative claims need a stated reading.** "Similar" speed with a 13%
  difference was the one disagreement between author and verifier. The claim
  file should say how a qualitative claim will be judged before the analysis
  is run.
- **Results at the edge move with the random split.** Counts changed by one or
  two, and one p-value from 0.047 to 0.018, when the cross-validation split
  changed. Notebooks should fix their seeds, and conclusions should not rest
  on a value that close to a threshold.
- **The second verification round is mostly about prose.** Ten flags, none
  changing an outcome: an appendix paraphrased too generously, a value called
  "slightly positive" that was not distinguishable from zero, statements with
  no output behind them. A rule for the author would prevent most: every
  sentence in a conclusion cites an output in the notebook.
- **Diagnostics the verifier asked for should be standard.** Counts of fits
  that failed or had nothing to fit, the range of every plotted quantity so
  clipped points cannot hide, and a table of trial types.

### Findings about the dandiset

- It holds one of the twelve sessions analysed in the paper, and none from the
  two-workspace experiment.
- The arm marker positions that the paper's main model uses are not included.
- The descriptions of hand position and velocity give a different unit from
  the stated one.
- The metadata names the paper without saying which part of it the data
  covers.

- **A notebook that is fast locally can be thirty times slower in CI.** The
  first CI run of this entry took 49 minutes against under four locally,
  nearly all of it in thousands of small model fits, each using several
  linear-algebra threads on a runner with few cores. Limiting those fits to one
  thread fixed it. The runtime that counts is the one in CI, and the check
  should fail an entry that comes close to the time limit.

### Cost

One to four minutes of compute per run locally. The attempt and two
verification rounds took one working session; the verifier used roughly as
many tokens as the attempt.

## 000207, Zheng et al. 2022 (2026-10-13): first attempt by an agent following the protocol

Outcome after verification: five claims reproduced, one partially, fourteen
blocked. Before verification it was five reproduced, two partially, two not
reproduced and eleven blocked. See
[`attempts/000207-zheng-2022-01.yaml`](../attempts/000207-zheng-2022-01.yaml).

This attempt was made by an agent given only the repository and
[`protocol.md`](protocol.md), to test whether the protocol can be followed by
someone who did not write it. It could: the entry passed the checks first
time. Notes for when the pilot resumes:

- **Open question on the main outcome.** The paper reports 42 of 580 boundary
  cells against a chance level of 2.11%. Following the Methods literally gives
  1 of 549 with a chance level near 0.03%. Chance levels that far apart mean
  the two procedures are not the same, so `blocked` with
  `methods_underspecified` may describe this better than `not_reproduced`.
  Settled in verification; see below.
- **The lab's linked code did not contain the analysis.** It plots rasters.
  The protocol should have the author check what a linked repository holds,
  consult it before writing criteria, and record the commit read.
- **Which dandiset version to pin is not in the protocol**, and it decided
  whether three sessions were usable: the latest version has spike times
  shifted against the events in three subjects.
- **Criteria written "before the analysis" were in practice written after the
  data check**, which already shows results. The protocol should either accept
  that and require disclosure, or have claims written before data is opened.
- **Tolerances are invented by the author.** One claim landed at 0.049 against
  a self-set 0.05. A default rule is needed.
- **Claims that depend on another claim's result** (analyses of cells that
  were not found) have no defined outcome.
- **Schema gaps:** one expected value per claim where papers report several;
  one blocking reason per outcome; no finding kind for a data error or for
  published code and data that disagree.
- **Tooling gaps:** `check` does not confirm every claim has an outcome, that
  versions agree across files, or that nothing reads local paths. A `handover`
  command to build the verifier's package would replace ad hoc scripts.
- **Cost.** About 400,000 tokens for the author across two rounds, several
  times the first two targets: twenty claims and a dandiset with real problems.

The full feedback from the agent, twenty points, was not saved with the
repository and could not be recovered. The points above are the ones
recorded.

### Verification (resumed 2026-10-13)

The two rounds were run with `tools/entry.py handover`, added for this.

1. Round 1, without the conclusions, agreed with the four behavioural
   outcomes, the state shift and the blocked claims. It disagreed on the three
   cell-count claims. In simulation, the paper's five-test definition under
   label shuffling stayed near or below 1% chance for every response profile
   tried, so the paper's 2.11% cannot come from the procedure as written. It
   also found that the spike clock was not established for 12 of 18 sessions,
   which bore on every claim about neurons.
2. The author added the outputs it asked for. A clock scan on each kind of
   clip alone showed the late peak in hard-boundary clips only, a response
   on an aligned clock, in 17 of the 18 sessions. Chance levels for the looser
   readings (0.10% and 0.55%) were also far from the paper's. The three
   cell-count claims became `blocked`, `methods_underspecified`.
3. Round 2 agreed with all twenty outcomes. It flagged one sentence the
   numbers contradicted (regional ordering under the pooled reading), two
   that overstated the clock check, stale p-values, a header that still
   counted the old outcomes, and round-1 reasons recorded in words it had not
   used. All were corrected.

### Lessons from the verification

- **A chance level the stated procedure cannot reach shows the paper used
  another procedure.** When the paper states a chance level for a selection, the
  attempt should compute its own. If they are far apart, the procedures
  differ, and the outcome is `blocked` with `methods_underspecified` even
  though the analysis ran. Added to the protocol.
- **Clock checks need a condition contrast.** An overall onset scan could not
  tell a response to hard boundaries from an onset response displaced by a
  wrong clock. The same scan by condition could. Every stream should be
  shown to share the trial tables' clock, with the sessions where this could
  not be established named.
- **One random stream for the whole notebook makes numbers drift.** Adding
  cells early in the notebook changed p-values in the last section, which
  left the conclusions stale. Each claim's section now gets its own
  generator. Added to the protocol.
- **The record has to keep the verifier's words apart from the author's
  answers.** Paraphrased reasons with the author's responses mixed in were
  the one thing the verifier objected to in the record. Verification results
  now have a `response` field.
- **The blocking categories overlap.** Author and verifier disagreed on eight
  blocked claims between `metadata_insufficient` and `data_missing` (a
  missing identifier linking trials to clips) or `other` (too few cells
  under the claim's own rule). Neither changes what is missing; the
  categories need definitions.
- **Edits after round 1 are of the same kind as in the earlier attempts.**
  Round 2 found no new analysis problem, only text that the new numbers had
  overtaken.

### Cost

The verifier used about 210,000 tokens over the two rounds. Each run of the
notebook takes about five minutes locally.

## 000147, Guan et al. 2022 (2026-10-13): second attempt by an agent following the protocol

Outcome: twelve claims reproduced, one not reproduced, seven blocked, the
same before and after verification. See
[`attempts/000147-guan-2022-01.yaml`](../attempts/000147-guan-2022-01.yaml).

The agent was given the repository and protocol `pilot-2`, and told not to
read these notes or other attempts. It ran as a subagent of a person's local
session, before the Actions workflow existed, so its transcript holds that
person's configuration and is not published. Its report on the protocol is
recorded here in full, so it is not lost as the 000207 feedback was.

### What the author reported about the protocol

1. The protocol does not say whether comparison data from outside the
   dandiset may be used. The agent read the fMRI model RDMs from the authors'
   repository at the commit the paper archived, and recorded it as a
   deviation.
2. No blocking category fits a missing external input, such as model RDMs
   that are not published anywhere. It used `data_missing`.
3. The protocol does not say what the outcome is when a number matches under
   only one reasonable reading. The paper's 70% of errors matches only when
   errors involving No-Go trials are left out. It called the claim reproduced,
   showed all three readings, and listed it as a deviation.
4. It does not say whether the claim's statement or its criterion governs
   when the statement includes a p-value the criterion does not. It followed
   the criterion and recorded the difference.
5. The outcomes fit a claim of absence poorly. A small but significant gaze
   effect, where the paper reports none, becomes `not_reproduced`.
6. The clock check's "contrast between conditions" had to be invented for a
   dataset with only spikes and a trial table. It decoded the finger in time
   windows around the trial start.
7. The per-animal breakdown does not apply to one participant. It broke
   results down by session.
8. The protocol does not say how to choose between published versions with
   identical files. It took the later one, because that names the paper.
9. `tools/entry.py run` is not isolated: it executes with the first Jupyter
   kernel named `python3` it finds, which on the machine used was miniconda,
   not the locked environment. The first run failed on a missing package. It
   worked around this; the tool needs fixing.
10. No finding kind fits a file-format error (spike times stored out of
    order) or an inconsistency inside the paper. It used `other`.
11. The handover command does not include the paper's text.
12. The paper leaves out some methods the authors' code supplies, and the code
    differs from the paper in places (OAS against Ledoit-Wolf shrinkage,
    8-fold against leave-one-out cross-validation). Each is a deviation.
13. Its own gap: the notebook does not count features dropped for zero
    variance.

### Findings about the dandiset

The dandiset holds the main task of all ten sessions, with counts matching the
paper, but not the calibration or control tasks, waveforms or sorting
metrics. The model RDMs the main comparisons need are not in it; two are in
the authors' repository and the rest were found nowhere. Spike times are out
of order in nearly every unit, with the first seconds of each run stored
before the end of the previous one. `cue_location`, `Run` and `TrialNumber`
have no descriptions, and electrode coordinates and impedances are NaN.

### Verification, in GitHub Actions

Both verification rounds and both revisions ran in the
[Agent run](../.github/workflows/attempt.yml) workflow, and their transcripts
and reports are in [`transcripts/000147/`](../transcripts/000147).

1. Round 1 agreed with all twenty outcomes. It tested the helpers on
   synthetic data and found no leakage. It raised that the 70% figure holds
   under one of three denominators, that per-run distances are inflated
   about fivefold by small-sample noise estimates, and that the gaze result
   could come from the structure of the task's screens.
2. The first revision added the outputs asked for. Cue location stays
   decodable with folds that never split a screen or a run, against nulls
   that shuffle within them. It also found that one model file's condition
   order had never been checked, and corrected a finding.
3. Round 2 agreed with all twenty and quoted four sentences that went
   further than the numbers, including one that called the trial start the
   cue where the data show only that it is consistent with it.
4. The second revision fixed them and decoded position within the screen,
   which does not explain the location signal.

### Lessons from running in Actions

- **A first run in a new environment fails in ways a local run does not.**
  Six runs failed before one completed: a missing sandbox dependency twice
  (bubblewrap, then socat), a mistyped token twice, and the credential scrub
  forcing permission mode `default`. A one-turn preflight now checks the
  token, the mode, that the agent's shell starts, and that its commands
  cannot see the token, so each of these fails in two minutes.
- **One run went through without a shell and still looked successful.** The
  verifier worked around the missing shell by reading the notebook with
  Grep, and its report was good, but it could not run the synthetic tests
  round 1 requires. A run that succeeds is not a run that could do its job.
  Kept as `verifier-1-no-shell.md`.
- **The author's prose still overreaches in the same ways.** Round 2 found
  the same kind of overstatement as in every earlier attempt: an inference
  stated as a fact, a bound quoted for one variant only.

### Cost

About 280,000 tokens and 25 minutes for the author. The revisions took 10
and a few minutes, the verification rounds 4 and 2. The notebook runs in
about 90 seconds.

## Protocol pilot-3 (2026-10-13)

Revised from the open points above, before the fifth attempt. Each change and
what prompted it:

- **Version to pin**: the cited version, else the latest unless an earlier
  one matches the paper better (000207 notes; 000147 point 8).
- **Linked code** is read before criteria are written, with the commit
  recorded. The Methods decide the main result and the code's choice is shown
  as a variant when they disagree (000207 notes; 000147 point 12).
- **Outside inputs** are allowed only when the paper itself compares with
  them, they are public and pinned, and they are listed under a new `inputs`
  field (000147 points 1 and 2).
- **Tolerances** default to the paper's own uncertainty, else 10% of the
  value, and `expected` may hold several numbers (000207 notes).
- **Criteria** are written before each claim's analysis, after the data check
  if need be, with what had been seen stated (000207 notes).
- **Several readings** of a number: the criterion lists the plausible readings
  beforehand, a match under any of them counts as reproduced, and the
  notebook shows all of them (000147 point 3). Decided after review: being
  generous here is preferred to letting the paper's wording turn a result
  into a partial one.
- **Claims of absence** are judged by the paper's own test (000147 point 5).
- **Criterion against statement**: the criterion decides; the notes say
  whether the rest of the statement holds (000147 point 4).
- **Dependent claims** are declared with `depends_on` and inherit a blocking
  reason (000207 notes).
- **Blocking categories** are defined, with one main reason and others in
  the notes (000207 verification; 000147 point 2).
- **New finding kinds**: `format_error`, `code_mismatch`,
  `paper_inconsistency` (000207 notes; 000147 point 10).
- **Clock check** example for data with spikes and a trial table only, and
  "consistent with" for what a check supports without proving (000147 point
  6; 000147 round 2).
- **Notebook outputs**: a null for every comparison with chance, counts of
  everything dropped, and bounds quoted for every variant (000147 point 13;
  000147 round 2). Breakdown by session when there is one subject (point 7).
- **Handover**: the verifier fetches the paper itself (000147 point 11).

Point 9 (the notebook kernel) was a tool bug and is fixed.

## 001097, Liu et al. 2024 (2026-10-14): first attempt under pilot-3, entirely in Actions

Outcome: seven claims reproduced, two partially, three not reproduced and
twelve blocked. See
[`attempts/001097-liu-2024-01.yaml`](../attempts/001097-liu-2024-01.yaml)
and the transcripts in [`transcripts/001097/`](../transcripts/001097).

Every run, the author's included, was made in the Agent run workflow. Ten of
the twelve blocked claims need fits of the paper's switching linear
dynamical system, which the `ssm` package could not be built for in the
locked environment and which take about 7.5 minutes each.

### What happened

1. The first author run was cancelled after 78 minutes, to see whether it
   was stuck, and lost everything: the transcript check took a matrix
   product in the agent's code (`Xd@np.ones`) for an e-mail address,
   refused the transcript, and stopped before the author's changes were
   collected. The check also printed what it matched to the public log.
2. The second author run finished in about 55 minutes.
3. Round 1 agreed with every tested outcome and raised three problems: the
   model weights were never checked to line up with the session files, the
   GLM's cross-validation gives negative R² on data with no signal, and the
   tuned-cell comparison differs from the paper's.
4. The first revision answered all three (the weights line up; an
   intercept-only baseline scores −0.086; the paper's pairwise comparison
   tunes more cells, not fewer) and fixed an off-by-one-frame bug in the
   behaviour raster.
5. Round 2 agreed with every outcome and quoted six sentences the numbers
   did not support.
6. The first try at the second revision ended after two minutes: its
   notebook run went to the background, it scheduled a wakeup and ended its
   turn, which ends a headless run. The rerun finished the revision.

### An outcome changed after the last verification

In the second revision, `fig2e-glm-behaviour-explains-little` changed from
not reproduced to partially reproduced. Round 2 had suspected the ridge
penalty choice broke the ordering of the three models; with the penalty
chosen by cross-validation the ordering holds, by 0.0003. The author says
the choice was not made in advance and the test is still weak. No verifier
has seen the change. As in 000582, the record could not say "verified up to
here". Protocol pilot-4 made the rule that an outcome may not differ from
the last round's agreed outcome, and this claim was set back to not
reproduced, with the change recorded as proposed.

### What the author reported about the protocol

1. No blocking reason covers a method whose software cannot be built, or
   fitted in time, in the registry's environment. It used `other`.
2. No rule covers analyses run while preparing that are not in the notebook
   (fit timing, a rejected stand-in model). It stated them as not run.
3. "Reproduced under any plausible reading" is lenient: the male-to-female
   ratio matched on 1 of 6 readings, and for a claim of absence any reading
   can make reproduction easy.
4. No rule says what to do when a pre-stated criterion cannot decide (two
   factors tied at the code's cap). It broke the tie and recorded it.
5. Some choices are not readings of a number (the GLM fold scheme, the
   comparison set), so the reading rule does not apply to them.
6. Findings have no `metadata_insufficient` kind.
7. `measured` holds one number, which does not fit claims with several
   expected values.
8. The 10% tolerance does not fit a stated range ("approximately 2 to
   13%").
9. The clock-check example assumes trials; these sessions are continuous.
10. No guidance covers duplicated recordings when counting trials.
11. The paper cites no version; it pinned the latest.
12. Criteria were written after some data inspection, as recorded.

### Lessons

- **A check that refuses must not discard the run.** The transcript check
  now removes what it suspects, reports kind and line only, and runs after
  the author's changes are saved; cancelled runs keep their work.
- **Headless agents must not schedule.** Background tasks and the
  scheduling tools are now off in agent runs, and the shell's timeout is an
  hour.
- **A run cannot be watched from outside unless it prints.** The live log
  now shows each step on the run's page; the API serves it only afterwards.
- **The verifier caught the important problems again,** including one the
  author had not seen at all (the penalty choice), and in round 2 the same
  kind of overstated prose as before.
- **Agents can miscount.** The round-2 verifier counted 25 claims where
  there are 24. Totals should come from the record, not from a report.

### Cost

The author took about 55 minutes, the revisions 43 and 30, and the
verification rounds 5 and 3. The notebook runs in about 8 minutes.


## Protocol pilot-4 (2026-10-14)

Revised after 001097. Each change and what prompted it:

- **Outcomes cannot change after the last verification.** `tools/entry.py
  check` fails when an outcome differs from the one the last round agreed
  with; the final revision records a proposed change in the notes instead.
  001097's `fig2e` was set back to its verified outcome under this rule
  (001097, 000582).
- **Method choices that can change the outcome are fixed beforehand**, and
  other choices are variants (001097 point 5; the `fig2e` penalty).
- **Claims of absence are judged on the paper's test alone**, outside the
  rule for several readings (001097 point 3).
- **Ties** are broken as the methods or code imply, and recorded (point 4).
- **Ranges** as tolerances: the range widened by 10% of each bound (point 8).
- **`not_runnable`**, a blocking reason for methods whose software cannot be
  installed or run in time (point 1).
- **Analyses outside the notebook** never decide an outcome (point 2).
- **`measured`** may hold one value per expected value (point 7).
- **`metadata_insufficient`** as a finding kind (point 6).
- **Duplicate recordings** are checked and counted once (point 10).
- **Clock check** for continuous sessions (point 9).
- **Verifiers take counts from the record** (the round-2 miscount).

The ten 001097 claims blocked as `other` for want of the paper's model
fitting are left as they are; new attempts use `not_runnable`.

## 000625, Geiller et al. 2020 (2026-10-14): first attempt under pilot-4

Outcome: four claims reproduced, four partially, six not reproduced and
twelve blocked, unchanged through both rounds. See
[`attempts/000625-geiller-2020-01.yaml`](../attempts/000625-geiller-2020-01.yaml)
and [`transcripts/000625/`](../transcripts/000625).

The target was chosen to test `data_missing`, and did: the dandiset holds one
of the paper's 16 mice in three random-foraging sessions, so the depth, ripple,
novel-context, reward and VIP claims are blocked for data that is not there.
Every run was made in Actions, and none failed.

### What the verification found

- **A method artifact explains part of a not-reproduced result.** Round 1
  showed on synthetic data that the paper's place-field rule flags a cell
  with only a positive field as negative too, which is why both fractions
  come out near 0.66. Round 2 then found the explanation overstated: cells
  without a positive field still have negative fields at 3.5 times the
  surrogate rate. The final notebook demonstrates the coupling itself.
- **A reproduced claim rests on averaging.** The fraction of negatively
  modulated cells is in range only after averaging over sessions; no single
  session is. The record now says so.
- **The stated sampling rate is wrong for two of three sessions.** The
  author fitted it from the population's relation to running, which is
  partly circular; the verifier accepted it on independent evidence (all
  sessions then last about 898 s, within the paper's 3 to 5 Hz).
- Round 1's synthetic tests checked every helper. Round 2 again found
  prose that went further than the numbers, and again miscounted the claims
  (28 for 26); the verifier prompts now carry the counting rule.

### What the author reported about the protocol

1. Testing the helper module before writing criteria is in effect running
   the analysis; results seen then are recorded in the claims file.
2. Nothing covers a wrong sampling rate; it fitted one and recorded it.
3. A clock check on a fitted clock is circular; it added independent support.
4. No rule says whether cell identity across sessions must be shown before
   averaging over sessions.
5. "Decide now which claims are blocked" conflicts with `other` for too few
   units, which is known only after a selection.
6. A reading that selects almost no cells needs a fallback, fixed in the
   criterion.
7. It is unclear when a criterion that holds in part is partial or not
   reproduced.
8. Whether code that was only read counts under `inputs`.
9. Nothing says to add the attempt to the README table.

The author and verifier disagreed on the blocking reason for the claim with
too few BiC cells (`other` against `data_missing`); the record keeps both.

### Cost

The author took 65 minutes, the revisions 27 and 11, and the rounds 4 and 2.
The notebook runs in about 7.5 minutes.

## Protocol pilot-5 (2026-10-14)

Before 000035, whose paper rests on transcriptomic data that is not on
DANDI. The registry judges the dandiset, and an outcome that combines the
dandiset with outside data cannot say which of them failed. So:

- Each claim says whether its test uses the dandiset alone or the dandiset
  with outside data (`data: dandiset` or `with_inputs`), and the dashboard
  and README count the two apart. Only the first counts towards what is
  said about the dandiset.
- When outside data must be matched to the dandiset's cells, sessions or
  subjects, a claim of its own tests the link, and every claim that needs
  the match depends on it. A dandiset that cannot be linked to the data it
  was published with is itself a finding.
- Outside data supplies only what the dandiset lacks, such as a label per
  cell, and the notes of a joint claim say which side a difference comes
  from.

000147's six claims that use the authors' model RDMs, or need fMRI or model
RDMs that are not public, are now marked `with_inputs`, and its attempt
lists the repository under `inputs`. Its outcomes are unchanged.

## 000035, Scala et al. 2021 (2026-10-14): first attempt under pilot-5

Outcome, on the dandiset alone: three claims reproduced, one partially and
nine blocked. With outside data, counted apart: two reproduced, one
partially and one blocked. No outcome changed through either round. See
[`attempts/000035-scala-2021-01.yaml`](../attempts/000035-scala-2021-01.yaml)
and [`transcripts/000035/`](../transcripts/000035).

### What the attempt showed about the dandiset

The dandiset holds only the paper's 185-cell follow-up at 34 °C. The main
data set, about 1,300 neurons with their transcriptomes, is in dandiset
000008, which names the same paper; 000035's description still speaks of
"over 1300 neurons". The paper's central claims are therefore blocked here
as `data_missing` and could be tested on 000008. Voltage and current are
stored in mV and pA under labels of volts and amperes, every series has an
undefined start time, and the published metadata has a placeholder
contributor carrying another author's ORCID.

### How pilot-5 worked

- The link claims did their job. One matched all 185 cells to the paper's
  per-cell table (layer, depth and mouse agree for every cell); the other
  checked the attempt's own features against the published ones (16 of 17
  at a correlation of 0.9 or more). Both would have blocked the joint
  claims had they failed.
- The author and verifier disagreed on the first: the files call 12 cells
  "L5 PT" where the paper's table says "L5 ET", a one-to-one renaming. The
  author kept "partially reproduced" because its criterion compared names;
  the verifier would say reproduced. The record keeps both.
- Round 2 caught the record contradicting its own notebook: it called a
  public reference file too slow to fetch, where the run it reviewed
  measured about 10 minutes. The final revision corrected the text and,
  under pilot-4, kept the verified outcome and recorded testing the claim as
  a proposed change for another round. The rule worked as intended.

### What the author reported about the protocol

1. A criterion did not foresee renamed labels (PT and ET).
2. No category covers an outside input that is public but slow to fetch; it
   used `not_runnable`.
3. Whether a link claim is needed when outside data is matched by label,
   not by cell.
4. Nothing covers re-implementing a method whose published code cannot be
   redistributed.
5. What a dependent claim gets when its link claim is only partly
   reproduced; it ran them and said so.
6. The paper gives no classifier result at 34 °C; it applied the paper's
   classifier and recorded the deviation.
7. Whether an entry is named for the online or the print year.

### Cost

The author took 45 minutes, the revisions 20 and 7, and the rounds 4 and 1.
The notebook runs in about 2.5 minutes.

## 001453, Fouke et al. 2025 (2026-10-14): the last pilot target

Outcome, on the dandiset alone: two claims reproduced and ten blocked. With
outside data, counted apart: five reproduced, one partially and two not
reproduced. No outcome changed through either round. See
[`attempts/001453-fouke-2025-01.yaml`](../attempts/001453-fouke-2025-01.yaml)
and [`transcripts/001453/`](../transcripts/001453).

The dandiset holds only the freely swimming tracking behind Figure 1 and
Figure S1; the imaging and head-fixed tail tracking of Figures 2 to 4 are not
in it, which blocks ten claims. The verification rounds and revisions ran as
one chain of Agent runs, each starting when the one before succeeded.

### Stimulus names as outside data

The dandiset stores each trial's stimulus as a code from 0 to 20 with no
names. The names come from the paper's analysis code and the protocol file
of its stimulus software, which swap two of them (lateral left and right).
Under pilot-5 that makes the names an outside input, so eight of the ten
tested claims are `with_inputs`, and the dandiset is judged on two. A link
claim tested the names: 17 of 18 per-stimulus speed medians match the
values the paper's code printed. The author's first point on the protocol
is that a table of names is a label, not data, and that treating it as an
outside input leaves almost nothing judged on the dandiset alone. The
missing names are themselves the main finding about this dandiset.

### What the verification found

- The angular-acceleration result (Danionella higher, against the paper)
  may reflect noisier heading tracking: Danionella values are twice the
  zebrafish ones even when still. The record no longer says this
  "suggests a noise floor", only that the data cannot separate the two.
- One static trial at 106.5 mm/s, probably a tracking artefact, alone makes
  the "Danionella do not modulate speed" claim not reproduced; the paper's
  own code finds the same three pairs.
- The new time courses favour the stimulus software's assignment of the two
  swapped codes, under which the monocular claim would be partially
  reproduced. The claim stays reproduced under the assignment fixed
  beforehand, and the verifier's view is recorded.
- Other findings: velocities stored per frame and labelled per second, 19
  files at 32 to 35 Hz where the Methods say above 150 Hz, subject IDs
  reused across species, and a code bug behind Figure 1H that divides by a
  frame interval including the gaps between trials.

### What the author reported about the protocol

1. A table of stimulus names is a label; counting it as outside data leaves
   the dandiset judged on almost nothing.
2. A link claim without an identifier to match on (the names were checked
   by comparing per-stimulus medians with the paper's printed outputs).
3. The clock check does not fit labels stored on the data's own timestamps.
4. Methods, analysis code and stimulus software disagree with each other;
   the protocol covers only Methods against code.
5. An absence claim whose test mixes conditions (static is not a
   direction).
6. No category for numbers from representative trials.
7. Which reading to put in `measured` when every reading matches.
8. The example entry (000127) predates the newer fields.

### Cost

The author took 37 minutes, the revisions 20 and 8, and the rounds 3 and 2.
The notebook runs in about 4 minutes.

## Protocol pilot-6 (2026-10-14), at the end of the pilot

- **A third round settles proposed changes.** A change of outcome found
  after the last round goes under a new `proposed` field. When there is one,
  the attempt sequence runs `verifier-3`, which reviews only the proposals,
  and `author-revise-3`, which applies those it agreed with. `check` holds
  each claim to the latest round that reviewed it. 001097's `fig2e` carries
  such a proposal now; 000035's untested claim needs an analysis that was
  never run and waits for a new attempt.
- **Names for the dandiset's own codes count as the dandiset.** A new kind,
  `data: with_labels`, for outside sources that only name or map codes the
  dandiset holds. A link claim confirms the names, and the missing names
  are a finding. 001453's eight claims of this kind count on the dandiset:
  seven reproduced, one partially, two not reproduced and ten blocked.
- **From the authors' reports** (000625, 000035 and 001453): unit identity
  across sessions shown or stated as an assumption; Methods first, then the
  paper's code, then other software when they disagree; links matched on
  published summary values where there is no identifier; a partial link
  still lets dependent claims run, with a note; labels compared by identity,
  not spelling; a slow outside input is `not_runnable` only when the
  notebook shows it does not fit; blocks that depend on a selection decided
  after it; absence claims judged on the paper's test as written; the first
  listed reading recorded under `measured`; and the author prompt points at
  the newest entry as its example.

## After the pilot: the first batch (2026-10-14)

Four dandisets run under pilot-6 through the attempt pipeline: 000006,
001754, 000130 and 001616. The first pipeline run mixed results between
dandisets because every agent run in it named its artifact `agent-run`; it
was cancelled, the branches were rebuilt from each dandiset's own artifact,
and artifacts are now named for the dandiset and role. The four in parallel
then used up the subscription's session limit after about two and a half
hours; the runs it cut short were restarted from where they began.

### 000006, Economo et al. 2018

Three claims reproduced, one partially, one not reproduced and four blocked,
all on the dandiset alone; both rounds agreed with every outcome. The paper
is paywalled, so the claims come from the abstract. The transcriptomic and
anatomical data are not in the dandiset. Spike times are stored unsorted in
1,120 of 1,149 units, written trial by trial as trial start plus time from
the cue, so neighbouring trials overlap on the file's clock; `stop_time` is
NaN in every file, and the two PT types are not described in the files.
Each mouse has only one PT type, so comparing the types also compares
animals.

The author's points on the protocol: abstract-only claims carry no numbers,
so every criterion is the author's own; whether other public parts of a
paywalled paper may be read; whether background sentences in an abstract
are claims; how to treat linked code that ships processed data; a clock
check for data whose trials overlap; one neuron counted in several
sessions; sessions too short for the clock check; and comparisons where
each animal belongs to one group.

### 001754, Knierim, McNaughton and Poe 2000

Two claims reproduced, two not reproduced and three blocked, all on the
dandiset alone. This was the first attempt to need the third round: the
final revision found that the lookup of positions did not drop spikes at
the tracker's "position lost" value, as the claims file requires; with them
dropped, 12 of 25 cells of one rat are spatially selective (0.48 against the
criterion's 0.5), and it proposed moving the main claim from partially to
not reproduced. The third-round verifier checked that the change follows
the criterion and was not chosen for its result (it moves the result against
the claim), and agreed; the record says the call sits on the bound.

The dandiset was converted by CatalystNeuro (catalystneuro/mcnaughton2000-to-nwb),
so its findings are about our own conversion: the two rats' files from the
same flight day hold the same position trace, so whose position it is during
the second rat's sessions cannot be established; position is stored only at
spike times; rate maps cannot be linked to units, because the cell number
was read from old Windows short file names; eight rate maps are copies of
another; units merge per-epoch spike files without saying they are one
neuron; the unit table lacks columns the conversion README lists; and the
description reports theta and ripples, but there is no EEG.

The author's points on the protocol: other summaries of a paper with a
three-sentence abstract as claim sources; "the paper's own test" when the
test cannot be read; a clock check with neither trials nor continuous
annotations; a broken identifier inside the dandiset; one trace shared by
two subjects as a kind of duplicate; and conversion code read in place of
paper code.

### 000130, Sohn, Narain, Meirhaeghe and Jazayeri 2019

Nine claims reproduced, four partially, seven not reproduced and three
blocked, all on the dandiset alone; both rounds agreed with every outcome
and nothing was proposed. The dandiset is the Neural Latents Benchmark copy
of one session of monkey H, out of the paper's 29 sessions over two
monkeys; the recurrent network claims are blocked for lack of the model.
Its `iti` description has Short and Long reversed, `tp` is a median 18 ms
longer than the event times give, the 283 test trials have no task
variables, and the outlier flags could not be reproduced with the paper's
mixture model.

The author's first point is a flaw in the pilot-4 rule for claims of
absence: judged on the paper's own test, a signed-rank test over the 4 of 8
datasets in the dandiset can never reach p < 0.05, so two absence claims
were reproduced automatically, one against clear evidence. The other points:
adapting the paper's statistics to a subset; the 10% tolerance for R2 near
1 or small proportions; no blocking reason for claims about a model; no
place to record code that was read but holds none of the analyses; a clock
check that confounds response latency with offset; GPFA fits that vary in
the third digit with fixed seeds; a bug fixed after seeing outputs; and an
ambiguous one-tailed test in the paper.

### 001616, Gerken et al. 2025

Six claims reproduced, five partially and nine blocked, all on the dandiset
alone. Totals match the paper (29 patients, 2,286 units), but the counts by
region do not, with no mapping between them. The paper's test of which
neurons respond is not calibrated on these data (it flags about as many
units at random times as at real onsets), and the dataset's own ZETA test,
which is calibrated, flags far fewer than the paper reports (79 against
1,025 for camera cuts), so the claims built on responsive units are
blocked as `methods_underspecified`. The decoding claims with the paper's
logistic regression reproduce; those about its LSTM were blocked or tested
with the logistic regression as a stand-in. Findings: spike times are
stored in milliseconds, which NWB does not allow; the face labels lack the
"excluded" state the Methods use; an earlier version held 28 recordings
twice; and the dataset's training code selects no hippocampal units,
because no unit is labelled `H`.

The author's first revision took 3 hours 24 minutes, mostly running the
ZETA test on every unit, and moved two blocked claims to partially
reproduced, as the protocol allows after round 1. `check` then held those
claims to round 1's "blocked", a flaw now fixed (the rule starts at round
2); to pass it the author recorded the round-1 verifier as disagreeing,
explaining why in its response, and round 2 accepted that reading. The
author's points on the protocol: an alpha as the paper's stated
false-positive rate; claims blocked by dependence though their analyses
ran; a stand-in model for claims about one that cannot be run; reference
values taken from code; tolerances for small proportions; and regions that
differ from the paper's.

Two lessons for running the batch. A chain script edited while a chain was
running broke that chain after its last step (bash reads a script as it
runs), and the queue waiting on it stalled for eight hours; the scripts are
not to be edited while a queue is running them. And an attempt's branch keeps the tools it started with, so
a fix to the tooling reaches a running attempt only if its branch is
rebased.


### 001754 again, on the fixed draft (2026-10-15)

The first repeat attempt, under the rules added for it (docs/agents/author-again.md).
The conversion was redone (`mcnaughton2000-to-nwb` at commit `7346882`) and
the draft re-uploaded on 2026-10-14, and the attempt pins `draft`. Three
claims reproduced, one not reproduced and three blocked, against two, two
and three before; both rounds agreed with every outcome and nothing was
proposed, so there was no third round.

The one change of outcome, `fd4-abnormal-selectivity` from not reproduced to
reproduced (one-sided p 0.024 against 0.055), comes from the data, not the
analysis: the draft drops every copy of each group of identical rate maps,
which removes three near-empty Rat2 maps the first attempt counted, and a
notebook cell runs the same test on the earlier maps to show it. Dropping
every copy instead of keeping one also removed six maps from the dandiset.
`flight-spatial-code` stays not reproduced (Rat1 10 of 25 significant on
flight day 9, Rat2 2 of 28); the rounds added tests of the shuffle null on
real spike trains cut off from position, which give fewer false positives
than the 0.05 the test assumes, and the record now calls a low fraction weak
evidence against a spatial code, since the test's power is unmeasured.

Of the eleven earlier findings, five are fixed (rate maps linked to units,
-999 and lost positions documented, duplicate maps gone, units' spike files
and windows listed, spike-time resolution documented), four partly fixed
(shared position trace, smoothing kernel, EEG, age and camera view) and two
still present (position only at spike times, and the description's flat
track). One is new: Rat2's preflight and flight units are on tetrodes with no
overlap, unlike the other two rats. The dandiset description was corrected
for the flat track and the EEG during the final revision, after round 2 had
read it, so the record still lists both; the next attempt will see the new
text.

The earlier attempt's transcripts are now in `transcripts/001754/attempt-01/`,
since the workflow writes every attempt's transcripts to the same paths. The
author's points on the protocol: the attempt schema has no field for an
earlier finding's status, so it marked each statement "Still present",
"Partly fixed" or "New" and listed the fixed ones in a comment; pinning
`draft` does not stop the attempt if the draft changes during it, which
happened here; and the protocol has no rule for an outcome that changes
because the data owner changed the data.

### 002014, Choi et al. 2025

Four claims reproduced, one partially and eight blocked, all on the
dandiset; both rounds agreed with every outcome. This is a methods paper on
a cranial chamber for monkeys, and most of its findings (electrode yields,
cultures, drainage, bone growth) rest on data the dandiset does not hold:
it has one session of one monkey. The five claims that could be tested are
the demonstrations in Figures 8 and 9.

The dandiset was converted by CatalystNeuro (catalystneuro/schwerdt-lab-to-nwb).
The main finding is about the clocks: the raw ephys and the spike times
start at 0 s, not on the clock of the trials, LFP and FSCV, and the author
placed them by locating the raw signal in the stored LFP (raw time 0 at
11812.11 s), so `fig9a-spikes-task-aligned` reproduces only after a
correction the file does not record. Other findings: stored spike times sit
about 7.1 ms after the spike troughs; the LFP series called beta-band is
broadband and carries a conversion factor that would scale it 3e7 times too
small; spike waveforms labelled volts hold microvolts and the raw FSCV
labelled amperes holds nanoamperes; the event table stores each event about
five times, once per overlapping trial window; trial types are not tagged
(they can be rebuilt from the events and match the paper's Zenodo lists
except one trial); the target position that sets the reward size is not in
the dandiset; and the subject and session descriptions describe a
different study from the same lab.

The author's points on the protocol: whether a claim that passes only
after a correction derived from the data counts as reproduced; a clock
check that needs the raw signal when spikes share no clock with the
trials; criteria for demonstration figures with no stated effect; outside
data used only as a check, which fits neither `inputs` nor a link claim;
two sortings of the same channel; stored values seen before the criteria
were written; and the 10% tolerance applied to proportions.

### 001933, Chen et al. 2026

Six claims reproduced, two partially, one not reproduced and eight blocked
on the dandiset, plus one claim using outside data, not reproduced; both
rounds agreed with every outcome. The dandiset holds only the fiber
photometry of Figure 6 and Supplementary Figures 7 and 8; the imaging,
proteomics and blots behind Figures 1 to 5 are in other archives, so those
eight claims are blocked. The paper's source data and analysis code are
public, and the author used the source data in one link claim that checks
the dandiset against the published traces.

The dandiset was converted by CatalystNeuro (catalystneuro/dombeck-lab-to-nwb).
The Anxa1 data match the paper, and its main claims reproduce. The Calb1
data do not: none of the 384 published Calb1 traces or integrals match the
dandiset's dF/F, so the Calb1 claims were tested on data that differ from
what the paper analysed, which is why the link claim is not reproduced.
Other findings: the optogenetics table's description gives one stimulation
pattern, while the files hold eight powers and two kinds of train, and two
mice received the shorter train without either the paper or the dandiset
saying so; dF/F is labelled a.u. but holds percent; the archive's summary
lists behaviour and not photometry; the four mice excluded on histology are
left out without a note; one mouse's series ends early. The paper's code
also differs from its figures in three places (a window that starts 1 s
after onset instead of before, a power code for the wrong power, and a
spontaneous measure that is a duration-normalized integral, not the
integral the Methods give), and the Methods, legends and code name three
different t-tests.

The author's points on the protocol: a link claim that no other claim
depends on; source data that show the paper used a measure or window
other than the Methods' (it kept the Methods' choice as the main result);
code with a bug that was evidently not what was run; `measured` when no
reading matches; the 10% tolerance for p-values like 1e-20; no category
for data present but not the version the paper analysed; and a clock
check that shows genotype differences before the criteria are written.

## Protocol pilot-7 (2026-10-15): data in other archives

001933 showed that a blocked claim can mean two different things. Eight of
its claims rest on imaging, proteomics and blots that the paper deposited
in the BioImage Archive, PRIDE and Zenodo; they were blocked with
`data_missing`, the same reason as data that are public nowhere. pilot-7
adds a fourth data kind, `elsewhere`, for a claim whose data the dandiset
does not hold because the paper put them in another public archive. The
claim names the archive and a pinned identifier under `where`, is tested on
those data like any other claim, and is counted on its own, apart from the
dandiset's claims and from `with_inputs` claims. It is never blocked with
`data_missing`; if it cannot be tested here, the reason is the one that
applies, such as `too_large` or `not_runnable`. `data_missing` now means
public nowhere. The README table leaves these claims out, and each
dandiset's page shows them in a line of their own.

Attempts recorded under pilot-6 keep their claims as they are.

### 000004, Chandravadia et al. 2020

Ten claims reproduced, eight partially, four not reproduced and one blocked
on the dandiset, plus two claims using the earlier release (Faraut et al.
2018), both partially reproduced; both rounds agreed with every outcome.
The paper is a data descriptor, so most claims are about what the files
hold (counts, tables, codes, dates); the rest are the Figure 5 analyses of
visually and memory selective cells, which reproduce for the visually
selective cells and the ROC measures.

The dandiset was converted with CatalystNeuro's involvement (Ben Dichter
is a contributor). The most consequential finding is that the
`new_old_labels_recog` column is described, in every file and in the
paper, as 0 for old and 1 for new, while the data use 1 for old; the
paper's own code reads it correctly, but a user who follows the
description inverts every recognition analysis. Others: two pairs of
sessions hold identical spike trains for all their units, so 55 of 1864
units are repeats; eight sessions have fewer encoding trials than the 100
the paper describes; the spike times of 13 units are out of order and two
units hold every spike twice; electrode impedance is empty and some MNI
coordinates missing; age or sex differ from the paper's table for three
subjects; one session keeps the real day of the experiment, which the
paper says was removed; and the new sessions hold 325 units where the
paper says 288 were added. The memory selective and dual cell counts are
not reproduced under the Methods' test, but the paper's code, which uses a
different window and correct trials only, reproduces them exactly
(`code_mismatch`).

The author's points on the protocol: Methods that disagree with code that
reproduces the paper exactly; a stated spread used as a tolerance; the 10%
default on record counts in a data descriptor; claims for a paper that
describes data instead of reporting findings; counting a unit once when two
sessions share spike trains; a public input that refuses automated
download (Dryad); criteria written after a data check that is itself the
test; no default threshold for partial outcomes; and whether tables copied
from the paper count as inputs.

### 002013, Amjad et al. 2025

Seven claims reproduced, one partially and five blocked on the dandiset,
plus one claim linking the dandiset to the paper's Zenodo deposit,
reproduced (trial lists agree for 99.8 to 100% of trials); both rounds
agreed with every outcome. The paper describes microinvasive probes for
recording dopamine and electrical activity in monkeys; the beta burst,
reward and unit isolation claims reproduce, the dopamine reward effect
weakly (p = 0.023, and not in the stored trial-aligned `da`).

The dandiset was converted by CatalystNeuro (catalystneuro/schwerdt-lab-to-nwb,
the same conversion as 002014), and many findings are the same: each event
is stored about five times, once per overlapping trial window; trial
conditions are not in the trials table; the FSCV table columns carry no
units and the raw FSCV current is labelled amperes with values in the
thousands; the bipolar LFP is stored in volts with a conversion factor that
makes it picovolts; and the raw ephys of one session and the spike times of
Monkey P are on different clocks from the rest of the file, by 9831.35 s and
6800.666 s, with nothing saying so. In addition, one session's trial-aligned
FSCV covers only the first half of its trials, the second recording site of
Figure 3A is missing, the raw FSCV times are an interpolated grid that
cannot be matched to the trials, Monkey P's file has no trials or events,
and no implantation dates are given.

The author's run succeeded, but its commit failed: the commit job switched
to the attempt's branch, made before `tools/archive_transcripts.sh`
existed, and then called that script (fixed by running it from the
workflow's own ref). It was committed from the run's artifact. The run had
also started from the files of an earlier run that the subscription's
session limit cut short, because the chain's reset of the branch did not
take. It started from a branch made before pilot-7 and followed
pilot-6; the first revision, which saw pilot-7, changed the record's
protocol to pilot-7 after checking that no claim needed the `elsewhere`
kind. The author's points on the protocol: the data kind of a link claim
whose source holds both labels and measurements; clock checks when the
contrast is the claim itself; a criterion written after its result was
seen in the data check; and linked code that holds none of the analysis.

### 001636, Pasquereau et al. 2013

Four claims reproduced, three partially, three not reproduced and eighteen
blocked, all on the dandiset. Round 1 called `false-positive-rate` not
reproduced where the author had it blocked; the author kept it blocked under
the protocol's rule for a computed false-positive rate far from the paper's,
and round 2 accepted that and agreed with all 28 outcomes, so there was no
third round. The paper reports how pyramidal tract and corticostriatal
neurons in the primary motor cortex of two monkeys respond to torque
perturbations before and after MPTP. Only monkey V can be tested. The cell
counts, resting rates, antidromic latencies, kinematics and EMG were tested;
17 claims are blocked as `methods_underspecified`, because the response
detection as described gives a false-positive rate of 0.22 against the 0.01
its threshold implies, which blocks that claim and the 15 that use the
detected responses, and because the paper does not define the single-trial
latencies of `trial-correlations`.

The dandiset was converted by CatalystNeuro (catalystneuro/turner-lab-to-nwb).
No monkey L file marks a torque perturbation, the monkey L torque command is
NaN in every pre-MPTP file, and 15 of 51 post-MPTP monkey L files have no
analog data, so the monkey L half of the paper (115 and 73 cells) cannot be
tested. The torque command's 50 ms pulse has three sizes (about 46, 91 and
183 units above rest), the smallest in most pre-MPTP sessions (108 of 157)
and the largest in most post-MPTP sessions (129 of 141), where the paper
describes one 0.1 Nm impulse; the kinematic and EMG outcomes therefore
compare different stimuli and cannot be attributed to MPTP, and post-MPTP
movements are faster and larger, the opposite of the paper. The analog
streams are not on the clock of the trials and spikes and fall behind by up
to 365 ms within a session; moving each trial's segment to its start puts
the command step 4 to 7 ms after every labelled onset. Other findings: the
angle's reference frame says positive is extension where the data show
flexion; four monkey V files repeat a block of another file's trials, and in
two of them the same unit is stored twice with different projection types;
`unit_also_in_session_id` uses the wrong prefixes, 35 of its 43 references
name files not in the dandiset, and the others point to a different unit;
the dandiset description gives systemic MPTP, elbow movements for both
monkeys and 1993 for Leu, where the files and paper say intracarotid MPTP,
the wrist for monkey L and August 1992; monkey L analog is sampled at 100 Hz
against the paper's 200 Hz, and the EMG is stored in uncalibrated A/D units;
the torque onset comes 1.70 to 1.73 s after `center_target_appearance_time`
in 90% of monkey V perturbations, where the Methods put it 1 to 2 s after
center capture at random; and no analysis code is published. The paper
itself gives different pre-MPTP PTN and CSN resting rates in the text (16.3
and 3.6 spikes/s) and Table 1 (18.3 and 3.2), and Table 1 marks the CSN
change in the fraction of excitatory responses p < 0.01, where its own
counts give p = 0.54.

An earlier author run, cut short by the session limit, had left a draft
helper and its transcript on the branch; the author read the end of that
transcript, replaced the helper, and flagged it as possible contamination of
the protocol-alone test. The author's other points on the protocol: the
paper states a per-comparison threshold, not a false-positive rate, and the
block that follows from treating it as one spreads to latency results that
match the paper; no rule for how to compute a false-positive rate; "the
stated spread" for a mean and SD over cells; supplementary material and a
dandiset that holds one of two subjects; counting each recording once
against matching counts that include duplicated units; a stimulus that
differs between conditions, which fits no finding kind; absence claims with
many tests; and no field in the attempt schema for the code repository and
commit read.

### 001933 again, Chen et al. 2026, under pilot-7 (2026-10-15)

The second attempt, made because pilot-7 changed the protocol; the dandiset
(0.260825.1457), the paper's code and the paper are unchanged. Six claims
reproduced, two partially and one not reproduced on the dandiset, plus the
link claim using the paper's source data, not reproduced, and eight claims
on data in other archives, of which four reproduced, three partially and
one not reproduced; before, the dandiset's counts were the same and the
eight were blocked. Round 1 disagreed on one outcome,
`fig3d-rim-binds-unphosphorylated`, which the author had decided with an
imputation the criterion lists as a variant, because RILPL2 is found only
in the p-RAB3A pulldowns and the paired test has no pairs for it; the
author changed it to partially reproduced (3 of 4), round 2 agreed with all
18 outcomes and nothing was proposed, so there was no third round. The
paper reports that LRRK2 impairs the release sites of dopamine axons
vulnerable in Parkinson's disease, in G2019S mice. The ten photometry claims of Figure 6 and
Supplementary Figures 7 and 8 were tested on the dandiset as before, and the
eight claims of Figures 1 to 5 on Zenodo, PRIDE and BioImage Archive data,
starting from the deposited per-section and per-blot values, since the
Imaris analyses and the blot quantification cannot be rerun. Two outcomes
rest on weak ground: `supp8c-calb1-spontaneous-not-reduced` has p = 0.0509
and would be below 0.05 in 59 of 121 nearby exclusion windows, and part B
of `fig4d-fewer-active-zones` fails on a re-implementation of the FIJI
analysis that keeps a median of 183 VAMP2 particles per image against the
legend's about 1000.

The dandiset was converted by CatalystNeuro (catalystneuro/dombeck-lab-to-nwb).
None of the earlier findings is fixed. The most consequential is still that
the Calb1 dF/F is not the trace behind Supplementary Figure 8 (0 of 384
published traces match, and recomputing dF/F from the raw signal with the
published code gives the dandiset's series, not the paper's), so the Calb1
claims are results on the dandiset's processing. The finding that Figures 1
to 5 are not in the dandiset is now that the dandiset's description and
related resources do not name the deposits that hold them. The published
spontaneous values are now known exactly: 0.005 times the trapezoid
integral divided by the number of samples in the transient, to 2.2e-15 in
every Anxa1 mouse, where the Methods give the integral. The new findings
concern the other archives. In PRIDE PXD065006 the RAB3 T86 phosphopeptide
is higher in the samples labelled MLi-2, and the paper's volcano table
holds MLi-2 minus vehicle (to within 1.6e-06 up to a constant) while the
Figure 2B legend reads a positive difference as higher with vehicle, so
either the labels or the figure's direction is swapped; with swapped labels
`fig2b-rab3-phosphorylation` would reproduce. That table gives 254
phosphopeptides at the legend's thresholds where the text gives 289; the
Figure 3 counts of 69 and 16 are those at adjusted p < 0.05; the Figure 1D
p = 0.0008 matches a paired test or a test of mouse means, not the legend's
test (4.65e-06); one WT section appears twice in the Figure 5D and 5E source
data, and counted once one comparison moves from p = 0.0344 to 0.058;
counts in the source data and legends differ (51 G2019S areas against 57 in
Figure 4E); the G2019S animals of Figures 5G, 5H and 5J are not identified
in the source data; the image studies hold images the figures do not use
without saying which were used; and three synaptosome images give 488 nm
for all channels in their OME metadata.

`tools/entry.py all` stopped at its check in every run, on 8 errors in the
earlier record `001933-chen-2026-01.yaml`, whose blocks with `data_missing`
fail the pilot-7 rule; the record was left unchanged and the notebook run
with `entry.py run`. The author's points on the protocol: the check applies
the current claims file to every attempt of an entry, with no exemption by
protocol version; one claims file serves both attempts, so updating it
changes the claims the earlier attempt points to; the rules for a repeat
attempt assume a changed dandiset and have none for an earlier finding
whose kind a new protocol makes invalid; findings are defined as about the
dandiset, and the schema has no field for the archive a finding concerns;
and the criteria for the eight new claims were written after seeing the
deposited values, though before any statistic, and for `fig2b` the
criterion did not fix the normalisation that decided the outcome.

### 000041, Watson et al. 2016

Eight claims reproduced, nine partially, fifteen not reproduced and seven
blocked, all on the dandiset; both rounds agreed with all 39 outcomes and
nothing was proposed, so there was no third round. The paper reports how
the firing rates of putative pyramidal cells and interneurons in the
frontal cortex of rats change across waking, nonREM and REM sleep, and
within and between sleep episodes. The rate distributions, burst index,
autocorrelogram peaks, packet durations and the rate changes over sleep
were tested, the microarousal claims on microarousals derived from short
Awake epochs. Six claims are blocked as `methods_underspecified`, because
the UP/DOWN state and spindle detection and the autocorrelogram decay fit
are described only in the Supplemental Experimental Procedures, which could
not be retrieved (PubMed Central and the publisher answer with a browser
check), and one, on movement in WAKE, as `data_missing`. Some outcomes rest
on weak ground: the last-packet mean of `fig3-first-last-packet` is 0.9679
against a bound of 0.968, and it and the nonREM peak of `fig2c-acg-peaks`
would fail without the seven sessions whose LFP could not be checked
against the spikes; `fig3d-first-last-slope` is reproduced, but its reading
that fast cells slow down and slow cells speed up is weakly supported;
`fig5c-delta-change` does not hold per session (p = 0.43); and
`fig5b-ma-between-packets` would meet its partial condition under a looser
microarousal rule picked after seeing the counts.

The dandiset was converted by CatalystNeuro (catalystneuro/buzsaki-lab-to-nwb).
It holds 22 sessions from 10 rats and 945 units (826 excitatory, 96
inhibitory, 23 unknown), where the paper and the dandiset's own description
report 27 sessions from 11 rats and the paper analysed 995 putative
pyramidal cells and 126 interneurons; which sessions and units were left
out, and why, is not stated. Two sessions are corrupt: in Dino-072114 the
spike times are whole seconds divided by 20000, because the conversion read
them from a CellExplorer file with a hard-coded 20 kHz rate, so its spikes
cannot be used; and the LFP of Dino-061914 has 125 columns for 128
electrodes, lasts 331.7 min against 291.9 min of states and spikes, and its
samples are scrambled. The state table holds only Awake, Non-REM and REM,
without the paper's microarousals, WAKE-SLEEP episodes, packets, UP/DOWN
states or spindles, and microarousals derived from short Awake epochs are
fewer than the paper reports (391 in 21 sessions, against 790 in 27). The
dandiset does not say how the states were scored, and the table may not be
the paper's scoring: it yields 30 WAKE-SLEEP cycles in 21 sessions, 3 of
them with none, though the paper kept only sessions with a full cycle, and
only 49 of 534 REM epochs are followed directly by Non-REM. Other findings:
the description gives 11 animals, 27 sessions, 1360 units and an age of
4-7 months, where the files hold 10 animals, 22 sessions and 945 units aged
3-7 months; the LFP is stored as int16 with unit volts and conversion NaN;
every electrode's location is "unknown" and every unit's region "CTX" or
"unknown", though the paper records from medial prefrontal, orbitofrontal,
anterior cingulate and secondary motor cortex; 23 units of one session have
cell type and region "unknown" with no description of the label; there are
no movement, accelerometer or EMG data, though the paper uses EMG to score
states and movement to define WAKE; and in 14 sessions the state labels
agree best with the spikes when shifted 5 to 60 s earlier, while the LFP
agrees with the spikes to within 50 ms in 14 of 21 sessions, three others
have a clear extreme 56 to 64 ms from zero lag, and in three agreement is
not established.

The author's points on the protocol: "open access" is not defined, and a
free-to-read author manuscript was taken as full text; no rule for a main
text available without its supplement, whose claims were blocked as
`methods_underspecified` though that reason is defined for a procedure
neither the paper nor its code fixes; no guidance on looking for code when
none is linked (the author read the conversion code, which explained both
corrupt files); a clock check by decoding shifted labels that is coarse for
states lasting minutes and does not apply to LFP; no guidance on a label the
paper uses and the dandiset lacks, or on corruption of single sessions; the
10% tolerance for correlations that depend on binning the paper does not
give, and fixed p-value thresholds that become stricter with fewer cells;
`measured` when no reading matches; no way to act on a check that shows a
criterion is not diagnostic; and a corrupt stream found after the criteria
were written and some results seen.

### 000003, Senzai et al. 2017

Fifteen claims reproduced, eleven partially, three not reproduced and two
blocked, all on the dandiset. Round 1 gave its own outcome for each claim
without seeing the record and agreed with all 31; round 2 agreed again and
nothing was proposed, so there was no third round. The paper reports the
physiological properties and behavioral correlates of granule cells and
mossy cells in the mouse dentate gyrus. The unit counts and classification,
firing rates across wake, NREM and REM, theta and gamma modulation,
recruitment by dentate spikes, monosynaptic granule to mossy cell pairs,
place fields and remapping in the T-maze and open field, and depth (on the
17 files that give each unit's shank) were tested. `gc-mc-distance` and
`gc-backpropagation` are blocked as `metadata_insufficient`, because no file
gives site coordinates; the second revision found the stored channel order
consistent with depth, which makes them testable on the 17 files, but left
that to a new attempt. Some outcomes rest on weak ground: the phase part of
`theta-modulation` holds on one cut of the cycle only, and the spike-count
corrected comparison gives P = 0.00056 against the paper's P < 0.0001; the
permutation test for `pv-remap` gives P = 0.32; the overlap of 0.31 in
`inheritance-tmaze` is at chance (median 0.38); `gc-narrower-waveform` on all
files is mostly driven by truncated waveforms, and on the wide-band signal of
the 17 files gives P = 0.017 unfiltered and P = 0.4 after a 300 Hz
high-pass; and the pair-based claims rest on automatic detections, 65 pairs
against the paper's 32.

The dandiset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is
a contributor). In 24 files the end index of the first unit is short by a
multiple of 65,536 spikes (k = 1 to 7), and the missing spikes open the
second unit's train, which looks like an integer overflow at conversion; the
loader moves them back and reports each repair. In the 17 files with the
wide-band signal, the electrodes table's map of columns to shanks and sites
disagrees with the data: a unit's largest spike lies on the shank the units
table gives for 45% of units and on the table's own site for 9%, and the DS2
amplitude along the table's site numbers crosses zero more than once on 43
of 64 shanks; the units' `electrode_group` and stored waveform channels fit
one fixed map in all 4 mice, so the error is in the table. The authors'
curated monosynaptic connections (`MonoSynConvClick.mat`) were not
converted, so Figures 3, 4 and 7 cannot be checked on their pairs. Other
findings: the genotypes in the files (6 SST-Cre, 5 Drd2-Cre::Ai35, 4
POMC-Cre::Arch, 1 POMC-Cre::Ai35) do not match the paper's (7 SST-Cre, 5
DRD2-Cre::Ai35, 3 POMC-Cre::Ai35 and 1 wild type); 83 of 101 files do not say
which shank each unit was on and no file gives site coordinates, and the
units table has two layouts; the stored waveforms are about 5 times larger
than the same spikes in the wide-band signal, consistent with ADC counts read
as microvolts, and their 1.6 ms window cuts off the peak of 43% of GC, 67%
of MC and 78% of CA3 waveforms; the dandiset holds 568 mossy cells and 609
granule cells against the paper's 500 and 586, and 237 units labelled
`missing`; the T-maze position series and the states `quiet` and `transit`
are not described; the interneuron labels do not say whether a unit is in
the dentate gyrus or CA3; one light-pulse series holds 24,286 duplicate
times among 89,086; seven dates hold two files of one mouse that are
separate recordings, without saying what they are; and the paper gives a
burst index threshold of 1.2 in the Methods and 1.8 in the Figure 1A legend.

The electrodes-table finding came in the first revision, after the verifier
asked whether waveform channels map to the shank's electrodes; the criteria
of `mc-deeper` and `gc-mc-classification` were then changed to take each
unit's site from the wide-band signal, with what had been seen recorded in
the claims file, and both stayed reproduced. Untracked dotfiles and a
`scripts/` directory that the author did not create appeared in the
repository during the run and were left alone. The author's points on the
protocol: preliminary results printed while building the helper before the
criteria were written; no rule on deposited labels against re-running the
paper's classification; where to record conversion code read when no
analysis code is linked; whether to repair a detectable format error; the
10% rule giving zero tolerance for a reported zero; dependents of partially
reproduced claims, which the `depends_on` rule does not cover; metadata
found after the criteria were written; multiple readings that make ambiguous
claims pass easily; clock checks for continuous sessions without trial
tables; counting the same unit across days; and claims citing supplementary
figures that were not available.

### 000044, Grosmark et al. 2016

Three claims reproduced, three partially, six not reproduced and eight
blocked, all on the dandiset. Round 1 disagreed on eight outcomes: it found
that `fig2d-shuffle-high-dpcc` ranks all place cells by dPCC and does not use
the strong-contributor selection, and the author changed it from blocked to
partially reproduced; for the six claims built on the rigid and plastic
classes the author kept the block under the rule for dependents of a blocked
claim, and round 2 accepted that and agreed with all 20 outcomes, so there
was no third round. The paper reports that diversity in the firing dynamics
of hippocampal cells supports both rigid and learned sequences, in rats
recorded in sleep before and after running on linear and circular tracks.
The sessions, place-cell count, PRE, MAZE and POST replay, coactivation by
firing rate, the rate split and the replay of low-rate and high-gain cells
were tested; the place-cell count is 417 at the 1 Hz threshold against 491,
and 480 at 0.5 Hz. `fig2b-strong-contributors` is blocked as
`methods_underspecified`, because the fixed test calls 56.1% of cells
significant with every rate map shifted, which shows it is not the paper's
procedure, and seven claims that depend on it are blocked with it. The
pooled replay test the criteria fix finds no replay before any manipulation
(p = 0.916), because the three circular-track sessions score lower in every
epoch and supply 11161 of 23801 POST events, so `fig1c-post-gt-pre`,
`fig4d-slow-sequences`, `fig4e-gain-sequences` and the informative half of
`fig2d-shuffle-high-dpcc` say little about the paper; POST exceeds PRE in 8
of 8 sessions and on each kind of track separately.

The dandiset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is
a contributor). It holds 8 sessions from 4 rats, with 562 pyramidal units and
128 interneurons, on one clock. The paper's derived data are not deposited:
there are no candidate or ripple events, no place-cell list, no sequence
scores and no PCC values or rigid and plastic labels, so every selection must
be rebuilt, and neither the paper nor the dandiset links analysis code, while
the supplementary Materials and Methods that define them are served only
behind a browser check. In versions 0.210812.1516 and 0.250624.0426 every
position series stores its sampling period (0.0256 s) as its rate, so the
positions span about 880 to 2360 hours; version 0.261005.2101 stores 39.06
Hz. Other findings: the description lists neck EMG and head-mounted
accelerometer signals, and the files hold neither, nor any wide-band data,
only the LFP at 1250 Hz; in Gatsby_08022013 the POST epoch ends at 30413.6 s
while the LFP, spikes and sleep states run to about 32000 s; every
electrode's location is "unknown", units carry only the hemisphere and
subject age is "/"; and on the circular track the animals ran toward
decreasing linearized position, which the metadata does not say.

The author's first draft assumed the circular track was run the other way;
the bug was fixed and the claims re-run, with the fix recorded in the
notebook. In round 2 the verifier's executed copy printed slightly different
values for the best-template variant (190 cells against 188) from the same
code and seeds; the cause was not found, and no conclusion rests on it. The
author's points on the protocol: the chance-level rule applies only when the
paper states a chance level, and "significant" was read as a 5%
false-positive rate; dependents of a blocked claim are blocked even when they
do not use the blocked result; no rule for a main text available without its
supplement; no guidance for a pre-registered test confounded by pooling
across sessions; no rule for code bugs found after claim analyses were run;
criteria that define no partial outcome; figures that could not be read, so
Figure 1D got no claim; and the rule to show how a result changes with a
threshold, which covers many choices here.

### 000056, Peyrache et al. 2015

Six claims reproduced, two partially and thirteen blocked, all on the
dandiset. Round 1 gave its own outcome for each claim without seeing the
record and agreed with all 21; round 2 agreed again and nothing was
proposed, so there was no third round. The paper reports that
head-direction cells in the antero-dorsal thalamic nucleus (ADn) and the
post-subiculum (PoS) of mice keep their coordination in sleep, with the
represented direction moving about ten times faster in slow-wave sleep. The
HD cell count, the preservation of rates and pair correlations across
waking, REM and SWS, the 60 degree packet, the angular velocity in each
state, the noise correlations and decoding were tested on the HD cells of
each session pooled over regions; the 13 claims that separate the ADn from
the PoS are blocked as `metadata_insufficient`. Some outcomes rest on weak
ground: the count of 378 HD cells passes only with Mouse12-120808 as
deposited, and with that session realigned it is 391 (390 with one
constant shift), above the upper bound of 388.3; the estimator of angular
velocity returns 4.99 for a trajectory played ten times faster, and scaled
by that the data's 8.33 becomes 16.69, so the fold is not determined; and
the waking crossing of `fig3a-packet-60-degrees` is 0.2 degrees inside the
tolerance, with reading (b) at 54.1 degrees just outside it. The
supplementary files could not be downloaded, as PubMed Central served a
browser check in their place.

The dandiset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is
a contributor). The units tables hold only spike times, with no electrode,
shank, brain region, waveform or quality measure, and every electrode's
location is "unknown", which blocks 13 of the paper's 21 claims; the
electrode groups and ripple annotations are consistent with Mouse24,
Mouse25 and Mouse28 being the three dual-site mice, but the files do not
say so. The files hold 1959 unit rows (103 with no spikes) in 40 sessions,
against the paper's 1077 recorded cells in 42 sessions; Mouse12-120809
alone has 292 units, 167 of them firing below 0.5 Hz, unit ids run from 0
to N-1 with no shank or cluster number, 1526 rows fire at 0.5 Hz or more,
and nothing marks which units or sessions the paper analysed. In 36 of 40
files one unit's spike times are two sorted runs, the first ending at an
index of the form k x 65536 - 1, and in 10 of them 821 to 22281 times of
the second run also appear in the first, which suggests an error in the
conversion. In Mouse12-120808 the position and the spikes do not share a
clock (the best shift is -1.5 s at the start of the exploration and -3.4 s
at its end, against -0.2 to 0 s in all other sessions), and no unit passes
the HD criteria as deposited. Other findings: the open-field exploration,
the paper's waking epoch, is not marked, and the "Awake" state also covers
waking in the home cage; the raw LED positions are stated in meters with a
conversion of NaN but hold camera pixels; Mouse32-140820 has no sleep-state
table and no processed position, Mouse17-130201 has no processed position,
and in three Mouse20 sessions the position series ends 11 to 109 minutes
before the recording; the annotation series `dow`, `hdD` and `rip` have no
description; the related resource for the paper gives its name as
"nternally organized mechanisms of the head direction sense" and the title
in place of a DOI; and neither the paper nor the dandiset links analysis
code.

The first criterion of `fig4b-noise-correlations` used a Pearson scaling
that contradicts the Methods' formula; after the first run it was changed to
that formula before the outcome was recorded, with the first version kept as
a variant. The author's points on the protocol: step 5 assumes there is code
to read; no rule for a criterion found wrong after a run; a clock check that
does not fit continuous sessions of spikes, position and sleep states; no
rule for a condition the paper uses that the data do not mark; whether a
region assignment inferred indirectly may decide an outcome; one expected
value across several conditions; reported counts that do not decide a
claim; the default 10% tolerance, which gives 9 to 11 for "approximately
tenfold"; open-access supplements that cannot be downloaded; where
descriptive statements go; and the rule on seeds when no step uses random
numbers.

### 000059, Petersen et al. 2020

Twelve claims reproduced, fifteen partially, ten not reproduced and one
blocked, all on the dandiset. Round 1 disagreed on one outcome,
`fig5-speed-control-cooling`, whose criterion needs both speeds within
tolerance under one reading and states no partial case; the author changed it
from partially reproduced to not reproduced, round 2 agreed with all 38
outcomes and nothing was proposed, so there was no third round. The paper
reports that cooling the medial septum (MS) of rats slows hippocampal theta
and raises choice errors, while the theta phase lags between place cells are
kept. The cooling time course, theta frequency and power against temperature,
choice errors and speed, place cell and interneuron rates and oscillation
frequencies, waveforms, field size and information, phase precession and the
pair correlogram, compression and lag claims were tested, on session lists
and parameters taken from the paper's MATLAB code, read and not run.
`suppl1-hippocampal-temperature` is blocked as `data_missing`, because the
control experiment that measured temperature in the MS and both hippocampi is
not in the dandiset. The supplement could not be obtained, so supplementary
figures were tested only where the main text states their result. Some
outcomes rest on weak ground: `fig3c-field-size-correlated` has R = 0.8197
against a bound of 0.819; the error peak of `fig6c-worst-trials-4-to-8` at
trial 7 is narrow, and within single rats the mean peaks at trials 14 to 26;
and in `fig5d-ccg-period` the criterion's estimator often takes the second
neighbouring peak, so its 109.2 ms is biased upward, while the nearest-peak
variant gives 91.0 ms but is biased downward.

The dandiset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is
a contributor). The temperature series of the nine MS10 sessions and of the
two control sessions of 2018-07-19 is not a recording: the paper's code lists
no temperature channel for them, ten run from 17.0 to 37.0 C (exactly in
nine; MS10-170313 reaches 16.98 C) and sit at exactly 37.0 C for 16% to 35%
of samples, MS10-170307 is a constant 37.0 C, and nothing in the files says
the series is modelled. The two 2018-07-19 sessions, which the code lists as
controls without cooling, have trials labelled with the cooling states and a
temperature dip, and their theta frequency during 'Cooling on' differs from
pre by -0.20 and +0.44 Hz, against a median of -0.82 Hz in the cooled
sessions. Six of the paper's 53 behavioural sessions are not in the dandiset,
four of them were in version 0.210812.1514 as files without behaviour, and
MS21-180627 has trials without the cooling state and MS21-180712 has no
trials. Other findings: the files hold no cell types, no place field
definitions and no electrode locations (every location is 'unknown'); the
trial state 'Cooling off' (a median 14 trials per session) is not described
in the files or the paper; in seven sessions every unit has quality
'unsorted', so MS10 has no usable units; in MS21-180621 and MS22-180621 the
units carry no spatial information (0.23 and 0.12 bits/spike), so the clock
of spikes and position could not be established there; the dandiset holds
three sessions that are not in the paper's behavioural analysis without
saying so; the first published version (0.210812.1514) has no trials table;
the Methods give position tracking at 120 Hz, while the MS10 sessions are
sampled at 40 Hz (six), 30 Hz (one) and 120 Hz (two); the Figure 5H legend
gives P = 8.0e-5 by a sign rank test with N = 10 sessions, which an exact
test over 10 sessions cannot give; and the Discussion's 12% decrease of theta
frequency does not match the Results' 8.4 and 7.7 Hz, about 8%.

The `fig5d-ccg-period` criterion was revised after a pilot session and before
any analysis across sessions, as the summed correlogram's spectrum followed
its envelope, and the two 2018-06-21 sessions were left out of the unit
claims at the data check. The author's points on the protocol: a criterion
revised after a pilot; no rule on using sessions the paper's code leaves out,
or modelled data; no rule on excluding sessions that fail the clock check
after the claims are written; no input kind for outside code that only
selects sessions and parameters; tolerances from a stated spread across
fields, which are very loose on a mean; criteria with no partial rule;
absence claims with no named test, where rank-sum tests over about 10,000
theta cycles are nearly always significant; per-rat tests that cannot reach
0.05 with 5 sessions; a continuous value on the tolerance edge; full text
available without its supplement; `measured` when no reading matches; and
bold labels in the example entry and notebook outline that conflict with the
instructions.

### 000061, Girardeau et al. 2017

Four claims reproduced, one not reproduced and one blocked, all on the
dandiset. Round 1 gave its own outcome for each claim without seeing the
record and agreed with all six, though it gave a different reason for the
block; round 2 agreed again and nothing was proposed, so there was no third
round. The paper reports that joint hippocampus and basolateral amygdala
(BLA) patterns from an aversive run are reactivated in later sleep in rats,
peaking at sharp-wave ripples and involving a subgroup of BLA cells that
fire more at ripples. The paper is not open access, so the claims were taken
from the abstract alone, none has a reported number, and every method was
chosen and fixed in the claims file. Post-sleep reactivation, its peak at
ripples, the ripple-up BLA subgroup and its weight in the patterns were
tested on 15 sessions from 3 rats, and stronger reactivation of the air-puff
direction does not hold (p = 0.11). `rats-learn-puff-location` is blocked as
`too_large`, changed from `data_missing` after round 1: the dandiset holds no
position tracking, and tracking the 1920573 raw run frames (1328 GB
uncompressed) would take about 190 hours to stream. Some outcomes rest on
weak ground: in `hpc-bla-reactivation-post-sleep` Rat10 is positive in 5 of
8 patterns (p = 0.74); much of the ripple peak is already present in
pre-sleep, so only the post minus pre contrasts speak to reactivation; and
in `reactivation-involves-ripple-up-cells` the up units fire faster (1.66
against 0.41 Hz), and the rate-matched difference does not hold at session
level (9 of 13, p = 0.22).

The dandiset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is
a contributor). In ten files the spike_times_index is wrong at the first
units: unit 1's spike times fall back once, after 65536 times k spikes, and
the first part of unit 1 is the end of unit 0, so units 0 and 1 of these
files were left out. The epochs table is stored in milliseconds although its
columns say seconds, its last stop time exactly 1000 times the LFP duration
in all 40 files, and the video timestamps are also in milliseconds and not
on the session clock (the first timestamp matches the start of its epoch in
1 of 114 videos). Seven files have no units table, sixteen have no sleep
states and fourteen have no ripple events, and Rat09 has no hippocampal
units and no ripples, so it cannot enter a hippocampus and BLA analysis.
There is no position tracking, only the raw video frames, so run direction
can only be inferred from reward times. Other findings: unit region labels
are undescribed short codes, some in two cases for the same region,
Rat09-20140328 has no location column and every electrode's location is
unknown, so which labels make up the paper's BLA cannot be told; the
`trials` table of the Rat08 and Rat09 files is described only as
"experimental trials" and its intervals of 3 to 5 s are not laps; the ripple
annotations carry an undescribed number in each label; and neither the paper
(as far as the abstract shows) nor the dandiset links analysis code.

Round 2 found five passages the printed outputs did not support, among them
a video streaming time left over from an earlier run, and all were
corrected without changing an outcome. Untracked dotfiles and a `scripts/`
directory that the author did not create appeared in the repository during
the run and were left alone. The author's points on the protocol: an
abstract alone gives no reported numbers or tolerances; step 5 assumes there
is code to read; the rule on blocking a claim for its unit selection does
not cover dropping a whole animal; no guidance on an abstract sentence that
describes the task setup; whether to repair broken data or leave it out; a
lap-direction clock check where shifting by whole laps only flips the
labels; how to count a lap that starts before the run; and a chance level
for the BLA selection computed with the author's own procedure when the
paper reports none.

### 000067, Fujisawa et al. 2008

No claims reproduced, five partially, seven not reproduced and four blocked,
all on the dandiset. Round 1 gave its own outcome for each claim from the
notebook with its conclusions removed and agreed with all 16. The author then
changed `fig4-position-dependence` from not reproduced to blocked as
`methods_underspecified`, because the calibration the verifier asked for
showed that the criterion's test flags 30.0% and 75.0% of synthetic pairs
with constant efficacy, and wrote a criterion for `traj-diverge` that moved
it from blocked to partially reproduced; round 2 disagreed with that change,
the author proposed blocked as `data_missing`, and a third round agreed. The
paper reports the firing of neurons in the medial prefrontal cortex of rats
during an odor-place matching task on a maze, and the monosynaptic
connections between them. The channel map, the counts of rats and units, the
active fraction, field size, trajectory and odor selectivity, connection
rates, cell classes, the fall of connection probability with distance,
position dependence, facilitation and depression, and supralinear summation
were tested on eight working memory sessions from three rats, with units
placed on the prefrontal probe from their waveforms; task performance, the
divergence of trajectories and the example session EE.188 are blocked as
`data_missing`. Some outcomes rest on weak ground: in
`fig3-connection-rates` only the inhibitory rate is within tolerance, and
without the 34 of 74 inhibitory connections that mirror a peak in the other
direction none of the three rates is; `fig3f-distance` fails on a Spearman
test over eight bins that the 1400 micrometre bin (2 of 310 pairs) breaks,
with rho = -0.964 over 0 to 1200 micrometres; and with EE.088's units placed
by the conversion's block order the unit count is 631, within tolerance, so
`rats-and-units` fails on the count of rats. The author used the author
manuscript in PubMed Central, the verifiers could not fetch the full text,
and the supplement, which defines the measures of Figures 6 and 7 and the
thinning step of Figure 4, could not be retrieved.

The dandiset was converted by CatalystNeuro (catalystneuro/buzsaki-lab-to-nwb).
It holds three rats (EE, FF, GG) of the paper's four, and of the 13 working
memory sessions in the CRCNS session table EE.152, EE.165 and EE.188, the
paper's example session, are not in it, while EE.210 has no trial table or
position. The units table holds spike times only, with no channel, shank,
brain region, cell type or quality label, and mixes prefrontal units, CA1
units, multi-unit clusters and clusters of the sensor signals; units can be
placed only from their waveforms in the wideband signal, which EE.042 and the
ten sessions of 2008-06-27 (EE.080 to EE.089, among them EE.088) do not have.
The two position series are the x coordinates of the two head LEDs, in pixels
although stated in metres, the second is zero in every file and there is no y
coordinate, and the trial table lists only correct trials without saying so,
so task performance and where the trajectories diverge cannot be tested. In
rat GG the nose-poke sensors are on channels 65 and 66 and the CA1 probe on 70
to 101, where the CRCNS description gives 97 and 98 and 65 to 96, and the
sensor on 66 is active on trials labelled Right, so either the sensors or the
side labels of GG are swapped. Other findings: electrode locations are
"unknown", coordinates are missing, impedances are -1, and the electrode
groups are cuts of eight consecutive channels that do not identify the
probes; the layer recorded in each rat is not stated; the trial table's
stop_time is the paper's trial start, and left_or_right carries the
description of reward_time; the linearized position is stated in metres but
runs from 1 to 2, with 0 outside trials; in six files the spike times of unit
1 are not in ascending order; GG.063, a spontaneous alternation session in the
CRCNS table, has a trial table with left and right trials; every file's
session description is the paper's abstract and session start times are dates
at midnight; and no code of the paper's analysis is published.

The Methods' rank band for `fig4-position-dependence` was replaced by a mean
plus c times s.d. band after a first run of the rank version gave 1.0% and a
synthetic test showed that it could not detect a strong position-limited
coupling, with the rank result kept as a variant. Untracked files in the
repository root, which the author took to be sandbox placeholders, were left
alone. The author's points on the protocol: a channel map from outside
documentation that the paper does not rely on; a stated spread across
neurons used as the tolerance of a mean; values given by layer with no layer
known for each rat; three criteria written after a timing run printed
connection counts; a Methods test that cannot reach significance, which the
tie-break rule does not cover; no paper code, so the conversion code was read
to interpret the files; no rule for when the unavailable supplement defines
the methods; a label link that holds only after a correction; a per-rat
criterion that one rat cannot meet; and units that sessions of one day may
share.

### 000070, Churchland et al. 2012

Five claims reproduced, seven partially, four not reproduced and six blocked,
all on the dandiset. Round 1 gave its own outcome for each claim without
seeing the record and agreed with all 22; round 2 agreed again and nothing was
proposed, so there was no third round. The paper reports that the population
activity of premotor (PMd) and motor (M1) cortex in monkeys making reaches in
a maze task rotates in the plane found by jPCA, and that a rotational dynamics
matrix (M_skew) fits it nearly as well as an unconstrained one, while
simulated kinematic populations and muscle activity show no consistent
rotations. The direction of rotation across conditions and reach curvature,
the prediction of the phase from the preparatory state, the variance captured
by the jPCA planes and by PC2 and PC3, the angle between the state and its
derivative, the fit of M_skew, the rotation frequency, the shuffle controls,
the two arrays analysed separately and the two kinematic models were tested on
the J-array and N-array datasets, with the 192 per-electrode units each file
holds in place of the paper's sorted isolations. The six claims on the leech
and walking-monkey data, the single-electrode datasets, the EMG, the generator
model and the speed task are blocked as `data_missing`. Some outcomes rest on
weak ground: in `fig3ef-same-direction` jPCA orients the plane so that the net
rotation is counter-clockwise, so the fraction is also 0.963 to 0.991 after
shuffles 2 and 3; `suppfig3-shuffle-controls` fails on R2(M_skew), which the
supplement does not expect shuffles 2 and 3 to reduce; in
`fig3-phase-from-prep-state` shuffle 1, which has no rotation, scores 0.82 to
0.91; in `rotation-frequency` J-array reaches the range with windows starting
at -150 or -100 ms (1.31 and 1.45 Hz), where the paper chose a window per
dataset; and the angle peak of the two kinematic models depends on choices the
Methods leave open, with the velocity model peaking at 0.028 pi only with no
lead and no preparatory tuning. The lab's jPCA download page returned HTTP
403, so the method choices it leaves open were taken from a Python port, and
the Supplementary Information was taken from the publisher's site, as PubMed
Central served a bot page.

The dandiset was converted by CatalystNeuro (catalystneuro/shenoy-lab-to-nwb).
It holds the paper's two array datasets but not the sorted isolations the
paper analysed (146 for J-array, 218 for N-array): its Units table has 192
units per file, one per electrode, and the seven single-electrode datasets,
the EMG, the leech and the walking-monkey data are not in it either, so six of
the paper's main findings cannot be tested. In nine of the ten files, all
written by the first conversion, the first entry of units/spike_times_index is
the true end of unit 0 modulo 65536, so unit 0 is cut short (in J-array 61030
of its 257638 spikes) and its remaining spikes open unit 1. In five Nitschke
files (ses-20090812, 20090819, 20090910, 20090920 and 20100923) the clock
restarts at recording segments after the first, as the conversion offsets only
one segment; trials overlap in time (2094 overlapping pairs in N-array) and
spike times go backwards at each restart, so spikes can be placed in trials
only by their storage order, which decodes reach direction in every segment.
Other findings: hand position is stated in metres with a conversion of NaN but
its values span about -220 to +165 and are in mm; the hand ends a median 35 mm
(Jenkins) and 52 to 53 mm (Nitschke) below the reached target in y while the
cursor lands on it, an offset the files do not describe; the Units table
carries only the default description and does not say whether its units are
sorted neurons, multi-unit activity or threshold crossings, and their number
and rates (8.8 to 300 spikes/s over trial time) are consistent with
channel-level activity; the dandiset does not say which of its ten sessions
are the paper's datasets, and the other eight are not described; and the first
conversion's code sets the year of every session date to 2009, so
sub-Nitschke ses-20090910, which is consistent with the N-9-10-2010 dataset of
Supplementary Figure 5, may be dated a year early.

In round 2 the verifier's copy printed 0.614 and 0.726 and 6 of 10 shuffle 3
runs reaching the J-array value for the cross-validated phase prediction,
against 0.615, 0.727 and 8 of 10 in the author's runs from the same code and
seeds; the source of the difference was not found, and the text now says the
count can move between runs. Untracked files in the repository that the author
did not create were left alone. The author's points on the protocol: criteria
that need values given only in figures; no rule on whether code read for
method choices, when the paper links none, belongs in `inputs`; no category
for control populations simulated from the data, whose free choices decide an
outcome; reported averages over datasets of which the dandiset holds only two;
whether an analysis may repair a format error; and a session that may be one
of the paper's datasets under the wrong date, used only as a variant.

### 000121, Even-Chen et al. 2019

Six claims reproduced, seven partially, six not reproduced and one blocked,
all on the dandiset. Round 1 gave its own outcome for each claim from the
notebook with its conclusions removed and agreed with 19 of the 20; it
disagreed on `pca-variance`, where R's PC1 is 72.8% against a lower bound of
72.9%, and the author changed that claim from partially reproduced to not
reproduced, following the criterion's letter. The author also changed
`plane-timecourse` from reproduced to partially reproduced, because R's
divergence cannot be told from baseline noise; round 2 accepted this as a
judgment beyond the criterion and agreed with all 20 outcomes, and nothing
was proposed, so there was no third round. The paper reports the structure
and variability of delay activity in the dorsal premotor cortex (PMd) of two
monkeys, J and R, reaching to targets in four configurations: a plane in the
population activity that maps target position, its time course, how trial to
trial deviations along and off the plane relate to reach kinematics, and SVM
decoding of target direction and distance. The session configurations, trial
counts, delays and reaction times, the task-correlated channels, the PCA and
plane variance, the plane's time course, the on- and off-axis deviations, the
speed and distance axes, the ellipse orientation and the decoding errors were
tested on all 7 of R's sessions and 5 of J's 16; the claim that J's sessions
are complete is blocked as `data_missing`. Some outcomes rest on weak ground:
in `distance-error-and-plane-projection` R's full error is inside its bound by
0.001 cm, and projection brings the error to the level of the direction
errors for 1 of 6 rings, or 2 of 6 with the Figure 4d inset's restriction; in
`delays-and-times` R's mean reaction time matches only with the 5.9% of trials
whose onset precedes the go cue kept; the pooled counts of
`speed-axis-within-distance` rest on pooling sessions; and
`relative-deviation-decreases` comes mainly from dividing by distance, so the
test discriminates little.

The dandiset was converted by CatalystNeuro (catalystneuro/shenoy-lab-to-nwb).
In every file the units' electrode_group labels are swapped: units 0 to 95 are
labelled PMd but point to electrode rows of the M1 group, and units 96 to 191
are labelled M1 but point to the PMd rows; the data agree with the electrodes
column, and in R the array labelled PMd has 29 silent channels and carries
almost no target information, as expected of the M1 array the paper calls
unusable, so units 96 to 191 were analysed as PMd. In every J file the
boundary between units 0 and 1 in units/spike_times_index is misplaced, so
unit 0 stops 1323 to 3120 s into sessions of 3083 to 8106 s and unit 1 holds
two to five times the median number of spikes, with spike times that restart
near 0. The dandiset holds 5 of the 16 sessions the paper uses for J, with all
four horizontal sessions missing, and the paper's own data link returns HTTP
403. Hand, cursor, eye and decoded positions are stated in meters with
conversion NaN but are in mm; task_id is 2 in every trial, so the target
configuration must be inferred from target_pos, which has no unit; electrode
positions are NaN and impedances -1. The files place R's horizontal targets on
2017-01-15 and 16 and vertical targets on 2017-01-17 and 18, the reverse of
the Methods, and R's trial counts match the Methods better when grouped by the
files' geometry. Other findings: the description of is_successful is wrong;
the dandiset description says sorted spikes, but the units are threshold
crossings, one per electrode; the archive's assetsSummary gives 15 files and
187.5 GB for a version of 12 files and 39.5 GB; R's horizontal targets lie at
5.2 + 10.4 k mm, and R's 2017-01-17 session holds 69 successful trials to ring
targets outside its layout; R's delays run to 1000 ms and R has 26 trials
without a delay, against 900 ms and 10% in the Methods; R's 3-rings session
holds 1340 successful delayed trials where the paper used 912, with no
selection stated; in R's 2017-01-19 the cursor differs from the hand by more
than 1 m in over 1% of samples; the paper prints R's distance errors in an
order that contradicts its text; and the paper names no analysis code and
reports neither its SVM hyperparameters nor the nulls of its p-values.

The author read the conversion code to interpret the files, as no analysis
code is published. Untracked files in the repository root that the author
did not create were left alone. The author's points on the protocol: a
criterion that names no outcome for a result it does not cover; a paper
uncertainty (SEM over cross-validation folds) that does not fit a repeat; no
guidance when the data contradict a label that every claim depends on; no
rule for one subject's data being partial; p-values with no stated null; no
finding kind for the Methods disagreeing with the data; a step that assumes
analysis code exists; a clock check that needed adapting to variable delays;
results per session that pooled analyses cannot give; and no mention of an
empty draft version.

### 000114, Carcea et al. 2021

One claim reproduced, three partially, three not reproduced and twelve
blocked, all on the dandiset. Round 1 gave its own outcome for each claim
from the notebook with its conclusions removed and agreed with all 19; round
2 agreed again and nothing was proposed, so there was no third round. The
paper reports that oxytocin neurons of the paraventricular nucleus (PVN) in
virgin mice co-housed with a dam and litter are activated by shepherding by
the dam, by nest entry and by the dam's pup retrievals, that silencing them
delays pup retrieval, and that virgins can learn to retrieve by watching
dams, which depends on oxytocin in the auditory cortex. The naming of the behaviour labels, the fractions of units activated
during nest entry, shepherding and dam retrieval, firing after shepherded
against voluntary nest entries, and the rates of shepherding and of
retrieval by the dam were tested on 194 units from 4 virgins in 7 sessions,
with oxytocin and other PVN units pooled. The ten claims on optically tagged
oxytocin units, the behavioural cohorts, unit recordings during observation,
the auditory cortex and the colliculus are blocked as `data_missing`, and
virgin chasing of the dam and the projection photometry of Fig. 4i as
`metadata_insufficient`. Some outcomes rest on weak ground: in
`ed7a-nest-entry-fraction` leaving out the 20 units above the code's limit
of 1,048,500 spikes gives 24.1%, inside tolerance, and counting V111 once
gives 28.8 to 30.3%; `fig2j-shepherded-entry` would pass without V116
03102018, whose clock is not known (p = 0.0237); in
`ed7a-dam-retrieval-fraction` 9 of the 13 activated units come from the
single retrieval of V111 03032018, share a median 71% of their spikes
pairwise within 0.1 ms, and the retrieval falls on one of the session's
largest synchronous bursts; and `fig1j-shepherding-rate` passes its t-test
over sessions (p = 0.0292) but not over mice (p = 0.193). The author used
the full text in PubMed Central, the Source Data for reported numbers only,
and the paper's code on GitHub for the label names and the parameters of the
shuffle test.

The dandiset was converted by CatalystNeuro (Benjamin Dichter of
CatalystNeuro is a contributor). It holds units for 4 of the paper's 17
recorded virgins (228 units in 8 sessions, against 541 in the paper) and
does not say which recordings were deposited or why; the optical tagging
recordings and the identity of the 21 OT-PVN units are not in it, so no
oxytocin-specific result can be tested, and the paper's code reads that
identity from a spreadsheet that is not public. The behaviour labels have no
description, and shepherding, nest entry and dam retrieval can be named only
from the paper's code; one file (V116 03122018) carries both the code's
labels and the paper's names. No test established that spikes and
annotations share a clock in any session, and in V116 03102018 the raw
voltage lasts 4.46 h while spike times and annotations run to 13.4 h. Units
in V110 and V111 have a median 7.0 to 9.2% of inter-spike intervals under 2
ms and 79 to 90% of their spikes within 0.1 ms of another unit's, although
the Methods say such spikes were removed, and V111's three sessions hold 31
units each with spike counts correlated 0.93 to 0.97, with nothing saying
whether they are the same units. The Methods cap nest entries at 40 s, which
the code does not, and on this data the cap changes the fraction activated
from 1.0% to 21.6%. Other findings: session start times disagree with the
dates in the session ids; the units table holds spike times and a name only,
and every electrode location is "unknown"; every subject is described as
co-housed, including the six photometry animals of the observation
experiment; photometry fibre location, fluorophore, wavelengths and gain are
"unknown" or NaN, the trace is stated in watts with values near 1000, and
commanded_voltage varies from 0.07 to 482 within sessions; and which
photometry animals learned to retrieve is known for 2 of 6, so the groups of
Fig. 4i cannot be formed.

In exploration, h5py's visititems hung on the large ecephys files, and a
first survey of all files hit the one-hour timeout before a plain group walk
replaced it. Untracked files in the repository root, which the author took
to be sandbox mounts, were left alone. The author's points on the protocol:
no rule for when the clock check fails to settle alignment; a data check that
showed counts and durations deciding some claims before the criteria were
written; fractions split by a label the dandiset lacks; whether
reference-only sources belong in `inputs`; a claim blocked for two reasons;
the choice between `data_missing` and `metadata_insufficient` for a label
that is absent while the units are present; units probably the same across
days, which the duplicate rule does not cover; and content comparison of
versions at 387 GB.

### 000213, Tingley et al. 2018

Three claims reproduced, eight partially, nine not reproduced and five
blocked. Round 1 gave its own outcome for each claim from the notebook with
its conclusions removed and agreed with all 25, though for the three assembly
claims it gave `too_large` as the reason for the block, and it said that
`fig5-assemblies` and `ls-information-lower` could have been tested. The
author then changed six outcomes: `fig5-assemblies` from blocked to not
reproduced on a random 1% of pairs, `ls-information-lower` from blocked to
partially reproduced, `ls-few-place-fields` from not reproduced to partially
reproduced, `fig1i-hpc-rate-phase-equivalent` and `fig6d-cfc-stronger-ca3`
from reproduced to not reproduced, and `ls-place-fields-unstable` from
partially reproduced to not reproduced, after place fields were found on the
Gaussian rate map the paper's code uses and sessions were grouped as the
criterion states. Round 2 agreed with all 25, accepting the two blocked
assembly claims with a reservation, and nothing was proposed, so there was no
third round. The paper reports that lateral septum (LS) neurons in rats
encode position in the theta phase of their spikes more than in their rate,
while hippocampal place fields carry it equally in both, and relates this to
recording depth in the LS, to hippocampal-LS assemblies, to theta coherence
and theta-gamma coupling with CA1 and CA3, and to a spiking model. The unit
counts, phase and rate decoding of position, place-field fractions,
properties and stability, information across smoothing scales, the depth
gradient and onset phase, coherence and coupling with CA1 and CA3, ensemble
decoding, peak information and assemblies were tested on the five rats, with
the linearized position, trial conditions and theta channel rebuilt. The two
claims that need the assembly strength of every pair are blocked as
`not_runnable` (about 12 process-hours), speed independence as
`methods_underspecified`, the maze rotation of Figure S6 as
`metadata_insufficient`, since nothing marks a rotation, and the spiking
model as `other`. Some outcomes rest on weak ground:
`fig1i-hpc-rate-phase-equivalent` fails on KS p = 0.044 over 531 fields,
against the paper's 1,820; the hippocampal field fraction is 10.5% against
31.7%, and the code's rule dropping peaks whose SD across trials exceeds
their mean accounts for most of the shortfall; `fig4d-depth-gradient` and
`fig4e-onset-depth` assume that the first depth in the session name is the
LS depth; and `fig2-ls-phase-beats-rate` is not reproduced although phase
beats rate in 58 of 58 sessions. The author used the full text of the NIH
author manuscript (PMC6605060) and did not read the supplementary figures.

The dandiset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is
a contributor). The paper's processed behaviour is not in it: the linearized
position, the trial conditions used for every rate and phase map, and the
CA1 pyramidal layer channel used as the theta reference in each session must
be rebuilt, and several outcomes depend on how. Units have no waveform,
recording site or channel of largest amplitude, so the within-session depth
analyses of Figure 4 cannot be repeated. The two depths in each session name
are not described, so which is the LS probe cannot be told, and the `hpc`
unit label is not defined as CA1. In every session the hippocampal channels
and units carry one label, hpc or ca3, where the paper's Figure 6A counts 63
CA1 and 19 CA3 sessions, more than the 67 files. The dandiset holds 1,696 LS
units and 3,217 hippocampal units (2,593 hpc, 624 ca3) against the paper's
1,647 LS and 2,951 hippocampal units, and 20,979 pairs of active
hippocampal and LS units against 11,264 examined, and which units the paper
left out is not documented. Other findings: eight DT8 files state position
in mm but hold metres; in all 67 files the z column of position is a copy of
y; in eight of the eleven DT2 files the position timestamps repeat or go
back; 11 units in six files hold spike times out of order; every DT2
electrode, and those of two DT9 files, is labelled `unknown`, and DT2
positions are in pixels with no scale; DT7 20170317 has 43 units with no
region or group and DT7 20170324 has no units; trials on the linear track
and in two DT8 alternation files carry no type or direction; in DT9 20170501
the trials do not match the positions, and DT2 20160221 suggests an offset of
up to a second; the head-orientation quaternion in
`allocentric_frame_tracking` states its unit as meters; the paper's code
names its place-field file for a 20% threshold but applies the 1% default,
where the Methods state 20%; the functions for phase binning, information and
assembly detection and the session files the figure scripts read are not
public; and 42 files chunk the LFP across all channels, so reading one
channel means reading the whole LFP.

During exploration a script that scanned the HDF5 chunk index hung and hit a
30-minute timeout, and the run crossed midnight, so the given date was used.
Untracked dotfiles in the repository root, which the author took to be
sandbox placeholders, were left alone. The author's points on the protocol:
a clock check where a constant offset between spikes and positions cannot be
seen by analyses that are consistent with themselves;
count claims whose criteria can only be written after the data check; no
rule on whether to rebuild missing derived data or block the claims; no word
on trying a reduced subset before blocking a claim as not runnable; no
category for a claim about a model that uses no recorded data; a 10%
tolerance that means little for a value near 100%; no guidance on designing
the partial-outcome rule; following code that calls unpublished functions;
and which date to give a run that crosses midnight.

### 000218, Tingley et al. 2019

Four claims reproduced, seven partially, ten not reproduced and ten blocked,
all on the dandiset. Round 1 gave its own outcome for each claim from the
notebook with its conclusions removed and agreed with 30 of the 31; it gave
not reproduced for `fig5d-lag`, which the author kept at partially
reproduced because the coupling part of the claim holds and the lag part
does not. Round 2 disagreed on the same claim, since the criterion defines no
partial outcome, the author proposed not reproduced, and a third round agreed.
The paper reports high-frequency oscillations (HFOs) in the lateral septum
(LS) of rats, their relation to LS firing and to CA1 ripples across sleep and
waking, LS correlations before, during and after behaviour, which features of
ripples predict LS firing, optogenetic experiments and a network model. The
dataset counts, the HFOs in each animal and their count, participation and
phase locking, HFO duration and frequency against ripples, the link between
amplitude and frequency, confinement to LS, the excess correlations and their
compression, the rise in LS rates after behaviour, HFO rates by state, the
lag and coupling with CA1 ripples, ripple-triggered firing, phase coherence,
and the prediction of LS firing from CA1 spikes, state and duration were
tested on events detected anew, as the files hold none, with `hpc` taken as
CA1. Depth within LS and travelling waves are blocked as
`metadata_insufficient`, the optogenetic HFOs and the CA1 depth of neurons as
`data_missing`, replay, seqNMF and the content-independent comparison as
`methods_underspecified`, and the model and two per-session claims, which have
7 and 4 recordings against 53 because this attempt's events hold few LS
spikes, as `other`. Some outcomes rest on weak ground: the event count of
`fig1c-event-count` matches at 31,984 against 29,955 but is probably a
coincidence, as DT7 contributes most events and the count depends on the
channel; the two `fig4b` claims rest on 106 pairs in 10 recordings against
7,172 in 53 sessions; the `fig7e` outcomes come largely from counting spikes
from ripple start to stop, and with a fixed +-25 ms window the CA1-spike and
duration values are 24.7% and 17.8%; and the tolerances of
`fig1f-shorter-than-ripples` are the paper's SDs, which makes them wide.
After round 1 the HFO analyses were repeated on the LS channel re-referenced
within its shank, and apart from the share of events on the same sample as a
ripple no result moved towards the paper. The author used the
author manuscript in PubMed Central (PMC6952543), whose supplementary figures
were not available.

The dandiset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is
a contributor). The files hold no detected LS HFOs or hippocampal ripples,
nor the detection channels and parameters, which the Methods say are stored
with each event structure, so every analysis of events has to detect them
anew and the channels cannot be matched to the paper's. In this attempt's
detection 35% of LS HFOs within 50 ms of a CA1 ripple fall on the same 0.8 ms
sample as the ripple (71% in DT8, 62% in DT2, 7% in DT9), and the CA1-LS
phase difference is consistent even at random times (median phase-locking
value 0.134 against about 0.021 for random phases); re-referencing the LS
channel lowers the same-sample share to 4.1%, which points to a signal
common to the LS and hippocampal channels, such as the reference, which the
files do not document. The units carry no waveforms, no channel and no
quality metric, so the CA1 depth of each neuron cannot be estimated and
single units cannot be told from multi-unit clusters; 11 units fire above 50
Hz on average, and wide-band data are in 27 of the 98 files, with 1579 of
2778 hippocampal units having none. Electrode x, y and z are NaN in every
file, and neither the probe geometry and its orientation nor the relative
depth of each recording within LS is given. The 10 files with `ca3`
electrodes hold no CA1 channel, which the paper's CA3 recordings used to
detect ripples, and the paper reports 25 CA3 and LS recordings against 10
here. Other findings: nine files store units without a location column, so
their 268 units cannot be assigned to a region; `hpc` does not say whether a
site is in CA1, and four DT7 files label all electrodes `unknown`; the two
rats of the optogenetic experiments are not in the dandiset; 25 units in 10
files have spike times out of order (1 to 2782 inversions each); the paper's
Key Resources point to a repository that holds only the Figure 8 model and
the code of the 2018 paper; and the paper gives the HFO band as both 120-180
and 120-200 Hz and cites wrong figure numbers in its Methods. Spikes, LFP,
sleep states and trials are consistent with one clock, and no recording is
deposited twice.

The run took about 18 minutes against the 10-minute aim, as loading each
file's chunk index takes about 33 s, and the date rolled over during the run,
so the given date was kept. Untracked files in the repository root, which the
author took to be sandbox placeholders, were left alone. The author's points
on the protocol: no guidance for a dandiset that lacks the intermediate
products the results depend on; a paper's stated SD used as tolerance, which
gives wide bounds; no threshold for too few units under a claim's own rule;
clock-check examples that do not fit continuous sleep recordings; an `inputs`
field framed around data, used here for code read only for parameters; no
block reason for a model claim; no rule on whether `measured` should use one
reading for all quantities; a step that assumes linked code exists; a
two-part criterion with no partial outcome; a runtime aim that a 1.5 TB
dandiset cannot meet; and a date that rolled over during the run.

### 000226, Severson et al. 2017

Twelve claims reproduced, two partially and eleven blocked on the dandiset.
With outside data, counted apart: two reproduced and one partially. Round 1
gave its own outcome for each claim from the notebook with its conclusions
removed and agreed with all 28; round 2 agreed again and nothing was
proposed, so there was no third round. The paper reports how
Merkel cell-associated afferents and other slowly (SA) and rapidly (RA)
adapting afferents of the mouse whisker follicle respond to active touch and
to whisking: touch responses explained by the bending moment (M0) and its
rate of change in statistical and viscoelastic models, direction selectivity,
a subset (WT*) tuned to whisk phase with preferred phases spanning the cycle,
responses that remain or vanish after progressive whisker cutting, and
comparisons with whisking EMG. The link to Table S1, frame counts, Merkel
minutes, baseline, touch and WT* rates, direction selectivity, the spline
models in place of the paper's GAMs, the viscoelastic fit, phase modulation
and its span and invariance, the kinematic models, nasolabialis motor units
and curvature noise were tested, with experiment groups taken from Table S1
as labels and afferent type and Merkel identity from it as outside data. The
claims on the progressive cutting experiment are blocked as
`metadata_insufficient`, and those needing the intrinsic protractor EMG, the
remaining whisker length, the optogenetic tagging, the histology and the
manually curated contact frames as `data_missing`. Some outcomes rest on weak
ground: `fig5e-phase-span` turns on a Rayleigh p of 0.047, which is 0.062
with the circular mean of the tuning curve; in `fig3d-gam-best-pair` M0 and
M0' ranks second of 45 pairs, at 0.622 against 0.633 for M0 and velocity,
also with lambda 100 and on held-out frames; `figs6-kinematic-gam` uses 15 of
the paper's 28 afferents; `fig5-phase-modulation` and `sigma-kappa` pass on
the paper's spreads while the non-preferred rate is 16% and curvature noise
28% above the paper's values; and `fig3a-direction-selective` reaches 65%
against the criterion's 80%. The author used the accepted manuscript in
PubMed Central (PMC5528144) and took the supplement holding Table S1 from the
publisher's file server, as PubMed Central and Europe PMC returned a
challenge page.

The dandiset was converted by CatalystNeuro (Benjamin Dichter and Luiz
Tauffer of CatalystNeuro are contributors). Its 60 files match Table S1 one
to one, but they do not say which experiment each recording belongs to, the
afferent type, which afferents were identified as Merkel afferents or the
whisking and touch class, and the three recordings the paper excludes (227C,
214A, 271A) are held without saying so. In the 13 progressive cutting
recordings every trial has cuttingGroup "intact" and MOI has one value per
file, although the whisking-in-air rate falls over most sessions (last fifth
below half the first in 10 of 13), so the cut conditions appear to be in the
files under the wrong label and Figure 6 and parts of Figure 7 are blocked.
The EMG files 7A, 8A and 9A hold tracked whisker series but no EMG signal,
11A holds nasolabialis spike times but not the EMG, and the optogenetic
tagging data, the histology, the whisker geometry and the curated contact
frames are not deposited. Velocity, acceleration, jerk, dM0, dFaxial and
dFlateral are stated per second but are per millisecond (median ratios 0.467
to 0.502), and the stored whisk phase is the negative of the Hilbert phase,
so phases from -pi to 0 are retraction, which neither the files nor the
paper describe. Other findings: every series has the description "no
description", distanceToPoleCenter has unit "unknown" and fits the Methods'
distance from whisker to pole in mm, and Mi, dMi and other series are not
explained; trial stop_time is 6.998 s after start_time while each trial holds
5 s of frames; the spike times of KS0277A are not sorted; KS0125_ and KS0128_
lack the unit letter of 125B and 128D, and all session start times are
12:00; some series hold extreme values, such as whisker position from -985 to
596 degrees, that are not flagged; the cut-whisker recordings 199B and 209A
hold distance-to-pole series and contact frames (5,014 and 32) that the files
do not explain; and the paper's analysis code is available only on request.
No recording is deposited twice.

Streaming the files by range requests took 22 minutes for the metadata
alone, so the notebook reads each file whole into memory. The first two runs
gave wrong model results from a diverging spline fitter and a badly
conditioned viscoelastic fit, both fixed without changing a criterion, and
in the last revision the viscoelastic results moved slightly from round 2
(difference -0.030 against -0.029) with the same code, data and locked
packages, for a cause not found; refits from three other sets of random
starts keep the outcome. The round 1 verifier could not download the
supplement and round 2 found the Table S1 check unshown, so the notebook now
fetches and parses Table S1 on every run, which needs access to the
publisher's file server. The author's points on the protocol: no case for a
table from the paper itself as input; the paper's stated spread as tolerance,
which makes median and IQR claims nearly untestable; streaming that is slow
for files of many small datasets; a step that assumes public code exists; no
rule for fixing bugs in the attempt's own code after seeing outputs; whether
to block or test a subset when a model can be fitted on 15 of 28 afferents;
and small ambiguities in the link rule for the EMG ids and in a blocked claim
with two reasons.

### 000232, Chang et al. 2023

Nineteen claims reproduced, seven partially, two not reproduced and one
blocked, all on the dandiset. Round 1 gave its own outcome for each claim
from the notebook with its conclusions removed and agreed with 28 of the 29;
it gave not reproduced for `fig5b-first-hit-switches`, where both block counts
fail, and the author changed that claim from partially reproduced to not
reproduced, as the criterion allows a partial outcome only when one condition
fails. Round 2 agreed with all 29 and nothing was proposed, so there was no
third round. The paper reports that in mice switching between a
respond-to-touch and a respond-to-light rule, neurons and populations in MM
and ALM encode the rule before the stimulus more than those in S1 and S2,
that this pre-stimulus state shapes the touch response and tracks rule
switches, and that inhibiting MM or ALM before the stimulus lowers tactile
sensitivity. The recording and optogenetic session counts, task performance,
the fractions of selective neurons, rule and stimulus decoding with LDA, SVMs
and random forests, trajectory distances, subspace overlap, coding
dimensions, the first hits after a switch, state tracking across transitions
and the optogenetic effects on sensitivity, hit rate and laser-only licks were
tested; the claim on the histological probe locations is blocked as
`data_missing`. Some outcomes rest on weak ground: `fig1h-thit-tcr-selective`
and `fig2c-rule-prestim-units` are judged on the main seed, and on the means
over five seeds all four areas of both would be within tolerance, while on
single seeds fig1h MM is within tolerance in 3 of 5 and fig2c S1 in none; in
`fig6c-pre-inhibition-tactile` the ALM upper bound is 0.005, averages -0.001
(SD 0.003) over ten other seeds and is below 0 in 7 of 10, and the code's
resampling gives the paper's interval; `fig4c-prestim-distance-predicts-divergence`
gives p = 0.004 with the Methods' normalization and p = 0.001 with the
code's, and the units of the offset are not stated; in
`figs4h-choice-right-left` S2 is 0.422 against 0.32 and within tolerance in 1
of 5 seeds; the absence in `figs5-sensory-states-no-tracking` rests on wide
intervals; and in `fig6ij-laser-only-licks` the one failing interval, detection
task, MM, short laser, [0.045, 0.483], excludes 0 in all ten other seeds, but
the paper's detection intervals match none of the short, long or pooled rows.
The author read the full text of preprint version 2 from eLife's copy of the
reviewed preprint, as bioRxiv refused the download, and read the paper's
analysis code at commit 227631e for method choices the Methods leave open,
taking no data from it.

The dandiset was converted by CatalystNeuro (Luiz Tauffer and Benjamin
Dichter of CatalystNeuro are contributors). Sessions, mice and units per area
match the paper exactly, as do all 24 optogenetic session and mouse counts,
but the ephys files hold only the trials and units the paper analysed: no
trial has a lick between -1 and 0.1 s of the stimulus, gaps of 8 to 64 per
session remain in the trial times, the units are those passing the quality
filter and the 50 Hz cut, and the dandiset does not say that trials or units
were removed. Units carry only spike times and observation intervals, with no
quality metrics, waveforms, channel or depth, and ids that run from 0, so
units the paper names by cluster number cannot be identified; electrode x, y
and z are NaN in all 49 ephys files, locations are "unknown", and the
histology of Figure 1E is not deposited. The trials table columns have no
descriptions, and `response`, `blockType` ("Change" for the cue trial), the
opto trial types and the indicator columns are explained only by the paper's
code. In the 130 behaviour files `start_time` equals the stimulus onset, so
trial intervals overlap, and in the tactile detection files trials without a
whisker stimulus are labelled "Stim_Vis" and "Stim_Vis_NoCue" with a visual
stimulus type. Figure 5B's 88 and 91 switches equal the touch and light
blocks of the 40 recording sessions when each session's first block is
counted, against 63 and 75 non-first blocks with a hit. Other findings: the
Methods' soft normalization differs from the code's in the trajectory
distance, subspace overlap, coding dimensions and decoding, and the Methods exclude sessions with fewer than ten units from the
subspace analysis where the code requires more than ten; the code's
optogenetic bootstrap resamples only hits; the coding-dimension code keeps 8,
7, 5 and 11 sessions where Figure S4 reports 10, 8, 9 and 13; two laser
trials start 1.6 and 2.7 s before the reference time and one lasts 9.5 s; the
stimulus-decoding check could not establish a shared clock for three
sessions, YT084 2020-02-02 and 2020-02-03 (AMM, 2 and 5 units) and YT086
2020-03-20 (MM, 5 units), which are kept; and one of the 28 cross-modal sham
sessions fails the code's own performance check as ported here. The draft
version has identical files and differs only in contributor metadata.

Two test runs before the final one failed or gave wrong values, from a
pandas duplicate-index error, a string column in a median and a light-block
mask bug, all fixed before the final run. Untracked files in the repository
root that the author did not create were left alone. The author's points on
the protocol: a paper download that bioRxiv refused; a Methods rule that
leads the analysis although the reported numbers fit the code; no guidance
for a Methods step that may already have been applied to the files; a
criterion that could not decide, whose tie was broken after one area's result
had been seen; a reading not listed before the analysis that matches the
paper's numbers; an absence claim whose test in the paper is ambiguous; no
slot for code that is read but supplies no data; and no rule on whether the
main seed or the spread over seeds decides a bootstrap result.

### 000239, Xu et al. 2022

Twenty claims reproduced, five partially, three not reproduced and eleven
blocked, all on the dandiset. Round 1 gave its own outcome for each claim from
the notebook with its conclusions removed and agreed with all 39; round 2
agreed again and nothing was proposed, so there was no third round. The paper
reports mice licking a port that moves through seven positions in standard,
backtracking and zigzag sequences, how population activity in S1TJ, M1TJ, ALM
and S1BF encodes tongue length, velocity and angle, sequence identity and
relative sequence time, and how optogenetic inhibition of these regions
changes licking. The unit and session counts, decoding of the five variables
and the relations among their coding axes, canonical correlation, decoding of
backtracking, zigzag context and the upcoming target position, the counts of
active neurons, initiation tuning, lick rhythmicity and the drop at water
contact, and the behavioural claims on sequence duration, learning,
backtracking, missed and consummatory licks and the starting side were tested.
The five optogenetic claims, the earplug, odour masking and tongue numbing
controls and the lick force are blocked as `metadata_insufficient`, inhibition
efficiency by cell type as `data_missing`, and the NNMF clustering as
`methods_underspecified`. Some outcomes rest on weak ground:
`fig3-units-per-session` is reproduced only on all 57 recording sessions, as
the 35 Figure 3 sessions the claim refers to give an SD of 14.4 against a
limit of 14.3; `ed5e-variance-explained` is 0.454 against a lower bound of
0.45 (0.453 to 0.455 over other seeds); in `ephys-unit-counts` three variants
of the unit classification put the multi-units inside tolerance (331, 309 and
295 against 339); the expected values of the five `fig3c` claims were read
from the Figure 3b image, which the verifiers could not check; in
`ed1l-proficiency-1500` proficiency had to be defined in the criterion and the
learning files may not start at the first day of training; and for
`ed2-backtracking-counts` a variant built after seeing the results, leaving
out 8 sessions with touches of a few ms, gives the paper's 47 sessions but 8
mice against 9. The author used the accepted author manuscript in PubMed
Central (PMC9109820), fetched through NCBI efetch after Europe PMC, BioC and
the PMC page failed, and read the Figure 3b values from the figure on Nature's
page.

The dandiset was converted by CatalystNeuro
(catalystneuro/oconnor-lab-to-nwb). The opto sessions do not name the
inhibited region: the 35 sessions at 4 mW and 25 at 2 mW, five per mouse,
carry only the light times and LED drive, the `opto` column (0, 1 and 2) and
the opto1 and opto2 series have no description, and no file has optogenetics
metadata, so Figure 2 and Extended Data Fig. 3j-m cannot be tested. The
control sessions do not mark the condition, which earplug session had
earplugs, which half of each air session had the air flow on, or which
numbing session was lidocaine; without the labels the paper's test finds an
earplug effect under 4 of 32 assignments and an air flow effect under 1 of 15.
The recorded area and the kind of session are given only by the session
description, the name of the lab's data folder, which is cut short ("... se")
in the files themselves; there is no electrodes table, unit location, depth or
quality label, and the area of the zigzag and "ephys others" sessions is not
given. Spike waveforms are not included, so units cannot be classified as
putative pyramidal or FS cells, and the fibre distance of the efficiency
recordings is not given. 1446 spike times in 35 files are duplicated within a
unit, which the Methods say were removed before analysis. Other findings: the
MX181003 learning file of 2018-10-02 15:30:57 repeats all 4028 touches of the
MX181002 file with the same start time and then continues, so it is unclear
which mouse it belongs to; in the 574 learning files start_time and stop_time
count from 0 while event times are on another clock (around 10^6 s); seqId in
the learning files holds the text of an unconverted MATLAB categorical object;
force sensor and lick port series are in volts without a calibration, tongue
landmarks are in pixels without a scale, and every trial column is described
as "no description"; the 8 sessions the Methods leave out for unregistered
touch offsets are not marked; and the paper says its MATLAB code is available
at GitHub but gives no address, and no repository was found. The session
groups of Figure 3, the 57 recording sessions, the 6 zigzag sessions from 3
mice and the 15 learning mice match the paper.

Threaded streaming was slow under h5py's global lock (15 minutes for an early
scan of all files), so the notebook uses processes, and an early trial filter
that wrongly required video before the cue was fixed before any claim was
judged; the seed and search variants added after round 1 raised the run time
to about 21 minutes, over the protocol's ten-minute aim. Untracked files in
the repository root that the author did not create were left alone. The
author's points on the protocol: nothing that stops outcomes being put in the
header table, which `handover` would not strip; whether numbers printed only
in a figure may serve as expected values; the paper's SD as tolerance for an
across-session mean, which is generous; a step that assumes the paper links
its code; an absence rule that assumes the paper names a test; whether an
undefined term like proficiency should be blocked or defined and tested; a
suggested clock check that is weak when sequences alternate direction; no rule
for a duplicate recording whose owner is unknown; a variant outside the
pre-registered readings that matches the paper; and a figure's p < 0.001 that
an exact paired permutation cannot reach with 8 sessions.

### 000350, Mu et al. 2019

Two claims reproduced, three partially, four not reproduced and ten blocked,
all on the dandiset. Round 1 gave its own outcome for each claim from the
notebook with its conclusions removed and agreed with all 19, but gave a
different reason for five blocked claims, and the author changed them:
`fig2dg-nmf-components` to `methods_underspecified` and `fig1k`, `fig1f`,
`fig7-ne-mismatch` and `fig7-glia-accumulate` to `metadata_insufficient`.
Round 2 agreed with all 19 and nothing was proposed, so there was no third
round. The paper reports that larval zebrafish in virtual reality give up
swimming when swims produce no visual feedback, that radial astrocytes
accumulate evidence of this futility and suppress swimming, and that
noradrenergic neurons in NE-MO drive them, with perturbation experiments.
The epoch durations, swim intervals, passivity in open loop, swim vigor
after a switch to open loop, intervals before passivity, the whole-brain
neuronal and glial signals at passivity, in open against closed loop and at
closed-loop pauses were tested. The NMF components are blocked as
`methods_underspecified`, the L-MO and NE-MO claims, the probe, replay and
Figure 7 protocols as `metadata_insufficient`, and the ablation,
activation and noradrenergic experiments as `data_missing`. Some outcomes
rest on weak ground: `fig1j-open-loop-passivity` is decided by the
closed-loop blocks after the first open loop, and closed loop before the
first open loop, a variant closer to the paper's comparison, gives median
0.104 and p = 0.0137, which meets the criterion for partially reproduced;
`fig1c-vigor-open-loop-onset` gives p = 0.0195 in 9 fish, but requiring 30 s
of uninterrupted closed loop leaves 4 fish (p = 0.125); `fig1i` depends on
the minimum epoch length, which the paper does not state, and with 8 or more
bouts both parts hold; and `fig2c` and `fig2h` fail on two fish whose traces
are questionable. The author used the full text from the PDF on the first
author's lab site, as Cell's site blocked the download, and did not read the
Supplemental Information; the paper's segmentation code at commit 54d1907
was read for its censoring and baseline settings only.

The dandiset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is
a contributor). It holds the 12 light-sheet sessions behind Figure 2 and its
supplement, with behaviour, but none of the perturbation or noradrenergic
imaging experiments of Figures 4 to 6, nor the behavioural recordings of the
other 62 of the 74 fish of Figure 1. Four files have raw images only and no
cell traces, among them the only three glia-only GCaMP6f recordings (the
paper's glial NMF used 6); raw images cover only part of 20170113-4 (3065 of
12050 volumes present) and 20170228-4 (5776 of 7200 present), and 20170113-2
holds 7616 imaging volumes against 9751 camera triggers. The DfOverF series
are not ΔF/F: in the four single-colour files each ROI trace is divided by
its mean, and in the four two-colour files traces are centred near 0 with
the first 60 s held constant, while the Fluorescence series are consistent
with baselines and carry the same description. The glial imaging plane of
the two-colour files is labelled GCaMP6f but excited at 561 nm and detected
at 660 nm, the jRGECO1b channel, and the raw images are typed
TwoPhotonSeries though the microscope is a one-photon light sheet. The ROIs
have no registration to a reference brain and no region labels, so L-MO and
NE-MO cannot be located. The protocol codes in StimulusParameterSignals (12,
22, 23, 32, 33, 51, 52, 53) are not described, so the probe, replay and
Figure 7 protocols cannot be identified; from the signals, code 33 is a 0.3
to 0.5 s speed-up of the grating and code 52 a randomised gain, and
TotalStimulusVelocitySignal lies between -0.002 and 0.008 in every file,
against baseline velocities of 0.5 to 2, so the visual feedback of each bout
is not recorded. Other findings: the ActivityStates table does not follow
the Methods' definition, its transient rows duplicate active rows, and it
holds 3 rows in the glia-only files; in 20161109-2 and 20170203-1 the glial
trace has an SD of 0.0016 and 0.0011, against 0.0097 and 0.0072, and
correlates with the neuronal trace at 0.58 and 0.59 (0.06 and 0.15 in the
others), and in 20170203-1 the neuronal trace also has a low SD, which the
files do not allow to be checked; the two groups of files were processed
differently, and the volume rate is 1.6 to 2.9 Hz against the 3 volumes per
second of the Methods; and the SwimIntervals width column equals the bout
duration in seconds. Imaging timestamps equal the camera-trigger edges,
consistent with one shared clock, and against version 0.221219.1506 the
behaviour and traces are identical.

About an hour was lost when a version-comparison script that walked every
dataset of 24 remote files hung until the 60-minute timeout, and two
notebook runs needed fixes before the final one. The notebook reads a fixed
8 to 15% subset of ROIs, as the full trace tables do not fit the time limit,
and the final run took 881 s. The round 2 verifier could not download the
paper text. Untracked files in the repository root that the author did not
create were left alone. The author's points on the protocol: a paper that
gives SEMs over 74 fish where the protocol asks for its own uncertainty;
linked code that covers none of the behaviour or onset analyses; no rule for
traces whose scaling differs between files; no rule for reading a subset of
a dataset too large for the time limit; a dandiset holding 12 of the paper's
74 fish; no way to mark a criterion choice as fragile except by showing
variants; and no guidance on which blocking reason to choose when several
apply.

### 000409, International Brain Laboratory et al. 2025

Seventeen claims reproduced, three partially, three not reproduced and seven
blocked, all on the dandiset. Round 1 gave its own outcome for each claim
from the notebook with its conclusions removed and agreed with 29 of the 30;
it gave not reproduced for `behav-zero-contrast`, whose mean of 58.26% misses
58.7 +/- 0.4 by 0.04 points while t138 = 19.68 is within tolerance, and the
author kept partially reproduced. Round 1 also found that
`traj-stim-regions`, left as not attempted, fits the time limit, so the
author wrote a criterion for it and tested it. Round 2 disagreed on the same
claim, since the criterion defines no partial outcome, the author proposed
not reproduced, and a third round agreed. The paper reports a brain-wide map
of neural activity in mice performing a visual decision task with a block
prior, from 459 sessions of 139 mice in 12 labs: the dataset and its
canonical set of 201 regions, task behaviour, decoding of stimulus, choice
and feedback, single-cell selectivity, neural trajectories and their
latencies, and a feedback oscillation tied to licking. The dataset counts,
mice, probes and trials, behaviour, decoding, trajectory latencies, the
number of regions with significant stimulus trajectories and the oscillation
were tested, the neural claims on VISp, GRN, IRN and seven regions drawn at
random, with one run of nested cross-validation and 100 null sessions
against the paper's 10 and 200. Receptive-field mapping is blocked as
`data_missing`; the two single-cell claims as `methods_underspecified`,
because the null run selects 2.7e-3 and 2.5e-3 of units against the paper's
5e-5, although all 14 regional stimulus fractions are within 0.02 of the
paper's table; and wheel-speed decoding, the encoding model, the video
correlates and the Granger interactions as `other`, not attempted. The
visual latencies are not reproduced (VISam 59.2 ms is not later than VISpm
61.3 ms), nor are the 104 +/- 10.4 regions with significant stimulus
trajectories (46 here). Some outcomes rest on weak ground:
`behav-performance` passes only on the mean over sessions, 81.58%, and not
on the mean over mice, whose s.e.m. of 0.43 matches the paper's +/- 0.4;
`fig1g-block-switch` passes only under reading (b), at 9.9 trials on the
point estimate, with 75.9% of resamples within 4.5 to 11; the stimulus
against choice margin of `dec-stim-restricted` and `dec-choice-widespread`
is one region and rests on CL, whose choice p of 0.0010 sits at the
2-session floor; `traj-latency-late` rests on the criterion's 0 to 150 ms
window, as in the paper's 0 to 100 ms window IRN has no latency and GRN is
at 100.0 ms; and `dec-feedback-nearly-all` could not reach the criterion's 9
of 10 regions, as the paper's own table marks 8 of these 10 significant. The
author used the open access version of record and took the paper's
per-region results and inclusion tables from its repository at commit
118fc36 as reported values only.

The dandiset was converted by CatalystNeuro (catalystneuro/IBL-to-nwb). It
holds every session, mouse, probe and unit the paper reports and every count
of its inclusion table, and no recording is deposited twice. In 64 sessions,
all with the protocol name `_iblrig_tasks_ephysChoiceWorld` without a
version, `probability_left` alternates between 0.2 and 0.8 on every trial
after the first 90, so `block_index` and `block_type` change on every trial,
and the stimulus falls on the stated block's likely side in 47.5% to 57% of
biased trials against 75.9% to 82.8% in the other 395 sessions; these
sessions were left out of every analysis of the block prior. No session holds
the receptive-field mapping phase or its stimulus sequence, which the paper
ran in 504 of 699 insertions, and the saturation intervals of the IBL
aggregate trials table are not in the dandiset. The quality score and the
paper's 75,708 well-isolated units follow a noise cutoff below 5, where the
Methods give below 20 uV, which would give 95,430. Other findings:
`wheel_movement_onset_time` is described as after the go cue but precedes it
in 11.97% of trials; `reward_volume_uL` is 1.5 on every one of the 242,628
rewarded trials, against the Methods' 3 uL; the units description refers to
a `label` column that does not exist and calls all probes Neuropixels 1.0,
though four insertions used NP2010; subject weight is one value per mouse in
all its sessions; the paper's code takes age and weight from the IBL
database, while the ages at recording in the files are 13.1 to 65.9 weeks
against the Methods' 13 to 178, and it swaps the mean and median labels for
weight; the 81.4 +/- 0.4% correct is given as mean +/- s.d. but the 0.4 is
an s.e.m. (s.d. 5.12); the two single-cell tests are not independent, so the
paper's stated false-positive rate of 5e-5 understates it; `region_info.csv`
marks 210 regions canonical against 201; the paper's results table gives
visual latencies of 34.0, 44.7, 46.8, 59.6 and 66.0 ms against the text's
34, 42, 42, 57 and 78; the code's trajectory permutation classes and
Benjamini-Yekutieli correction differ from the Methods, though neither
brings the count near 104 (46 to 53); and the files hold spike sorting
revision 2025-05-06 where the code loads 2024-05-06, with identical counts.
The spikes share the trials' clock in 448 of the 454 canonical sessions, and
it could not be shown in 6.

Development runs failed on files without an `epochs` group, on mixed time
zones under pandas 3 and on a decoder that was not reproducible until the
liblinear seed was fixed, all fixed before the final run. Testing
`traj-stim-regions` raised the run time from about 11 to about 25 minutes
(1513 s in the last run), close to the 30-minute limit, so the nested null
was run only for VISp stimulus. Round 2 found the README run time and some
sentences of the notebook and record unsupported by the outputs, and these
were corrected. The author's points on the protocol: nothing covers a paper
whose own analysis cannot fit the time limit; no line between
`not_runnable` and not attempted; claims the criterion did not cover, one
with no measure in the paper and one whose criterion defined only the
reproduced case; no definition of a null rate far from the paper's, which
here blocks claims whose regional values match; whether the paper's results
tables count as outside inputs; no rule for data found wrong after the
criteria were written; a clock check that sessions with few loaded units
cannot pass; and a first author that is a consortium.

### 000552, Huszar et al. 2022

Five claims reproduced, four partially, three not reproduced and twenty-three
blocked, all on the dandiset. Round 1 gave its own outcome for each claim
from the notebook with its conclusions removed and agreed with 34 of the 35;
it gave reproduced for `cohort-birthdates`, as the sex field differs between
files of the same mouse and each mouse's majority value gives the paper's 12
males and 5 females, and the author changed that claim from not reproduced
to reproduced. Round 1 also disputed the reason for blocking
`fig7fg-convergence-cofiring`, which the author changed to
`methods_underspecified`, and found a bug in the running rate, where a
running stretch could span the gap between trials; with the fix
`fig6d-rate-lower-novel` moved from partially reproduced to reproduced.
Round 2 agreed with all 35 and nothing was proposed, so there was no third
round. The paper reports that CA1 neurons of mice electroporated at E13.5 to
E16.5 differ in firing, burst index, theta and SPW-R participation, assembly
expression, spatial information and convergence onto interneurons according
to their embryonic birthdate, that same-birthdate pairs cofire and share
ratemaps more than different-birthdate pairs, and that a model with a
bell-shaped rate of neurogenesis reproduces the assembly expression rates.
The cohort, session counts and durations, ripple duration, unit count, maze
cohort and task, novel explorations, population-vector decorrelation on the
figure-eight maze and the firing rates, ratemap correlations and spatial
information of all putative pyramidal cells on familiar and novel mazes were
tested. The claims that compare same- and different-birthdate neurons or
light-responsive neurons across birthdates, the histology and the model, 22
in all, are blocked as `data_missing`, and the convergence claim as
`methods_underspecified`, since the Methods' connection test as implemented
here detects connections in 0.448 and 0.407 of possible pairs (0.405 and
0.394 peak-centred) against the paper's 0.173. Some outcomes rest on weak
ground: in `fig5e-pv-decorrelation` the medians depend strongly on the 5 Hz
rate rule for putative pyramidal cells, which classes 87.8% of units against
the paper's 78.3%, and a 2.59 Hz rule chosen after the results puts all four
medians within tolerance; `fig6d-rate-lower-novel` passes with rank-sum p =
0.041, while the paired test gives p = 0.19 and one of three mice goes the
other way; `fig6c-novel-ratemap-corr-higher` fails on the pooled test the
criterion names (p = 0.67), though the novel median is higher in all 9
sessions (sign test p = 0.0039); and the theta-related rates are a running
rate, as the LFP was not used. The author used the author manuscript in
PubMed Central (PMC10807234), fetched through PMC's OAI service after the
Europe PMC full-text API returned a server error, did not read the
Supplementary Tables, and read the paper's code at commit 51320d4 for method
parameters only.

The dandiset was converted by CatalystNeuro (Garrett Flynn and Cody Baker of
CatalystNeuro are contributors). No unit is labelled light-responsive and no
optogenetic pulse times are stored in the processed or the 13 raw files, so
22 of the 35 claims cannot be tested; the labels exist in the lab's
CellExplorer files, which the paper's data link reaches only through the lab
databank and Globus, at no pinned identifier. In the raw file of
e16_3m2_211213 the wideband signal ends 2 s after the processed session and
holds no flat or zeroed stretch over its last 30 min, so if clipped samples
are flat or zero the stimulation period is not in the deposited recording;
the other 10 wideband files (54 to 184 GB each) were not scanned. Units carry
no putative cell type and no waveforms, though the paper classifies 7,411
pyramidal cells and 2,060 interneurons. Six of the 17 mice (39 files) have
sleep states and ripples but no units and no position, so the dandiset holds
8,201 units where the paper reports 9,471, and of the 16 novel environment
explorations only 9 have position and trials, with no open field; 7 further
epochs of 10 to 50 min without position or video may be the missing
explorations. Units have no link to the electrodes table and their group_id
values ("Group3") do not match the electrode group names ("Group 3") in 64 of
65 files, so a unit's shank cannot be recovered. Other findings: the subject
sex differs between files of e13_1f1 (Female in 3, Male in 2) and e13_1m1
(Male in 9, Female in 3); is_familiar_maze is True only for the first two
trials of sessions with a single maze recording (112 True, 1,182 False); in
several novel recordings x and y lie between 0 and 1 though stated in cm;
twelve of the 13 raw files give a session start of 2011-08-18 for sessions
recorded in 2021 and 2022; the processed file of e16_3m1_210201 holds a copy
of the 1250 Hz LFP labelled 30,000 Hz with a conversion factor of 3.05e-13 V;
the embryonic day of electroporation is stored only as the prefix of each
subject id, with age P3M/P6M for every mouse; two files of e13_1f1 hold a
single Awake interval for the whole session; only 38 of 65 familiar-maze
sessions have ten or more trials on each visited arm and 19 of 1,942 trials
have no start or stop time; the Methods give 92 sessions while Figure 1e and
Figure 7f give 96, and the files of the 15 homecage mice are 96 sessions that
match Figure 1e by birthdate and the Methods' duration bounds exactly; and the
paper calls the novel cohort separate, but e13_26m1 is also among the nine
figure-eight mice. No duplicate recordings were found.

The notebook ran in 356 s in the first clean run and in about 8 minutes after
the revisions. Round 2 found sentences the outputs did not support, among them
31 sessions without units where the count is 39 and a statement on
stimulation channels resting on 1 of 13 raw files, and these were corrected,
the round-1 response that also gave 31 being left as recorded. An empty
`.claude/` directory in the entry could not be removed, and untracked files in
the repository root that the author did not create were left alone. The
author's points on the protocol: outside data must be public and pinned while
the paper's own data link reaches only an unpinned lab server; no rule on
whether a label held in the lab's derived files but not the dandiset is
`data_missing` or `metadata_insufficient`; no guidance on when to stop trying
to recover missing data from large raw files; using the paper's code to choose
subsets lies between following the code and an outside input; a criterion
condition with no stated outcome when it fails; a default 10% tolerance that
does not work for values near zero; no rule for a criterion whose literal
reading gives a result that is probably a metadata typo; and data-description
claims that the protocol does not address.

### 000568, Valero et al. 2022

Four claims reproduced, six partially, six not reproduced and six blocked, all
on the dandiset. Round 1 gave its own outcome for each claim from the notebook
with its conclusions removed and agreed with all 22 as they then stood, but
found that most light pulses are not in the files and that the place-field
rule differed from buzcode's; the revision restricted control time to windows
dark under the stated protocol and ported `bz_findPlaceFields1D`, which moved
11 cells between place and non-place and changed five outcomes:
`figs11-place-cell-fraction` to partially reproduced,
`fig3a-place-cells-more-excitable` and `fig4d-light-unmasked-cofiring` to not
reproduced, and `fig3g-spatial-information` and
`fig4c-swr-cofiring-place-pairs` to reproduced. Round 2 agreed with 21 of the
22 and disagreed on `fig3g-spatial-information`, whose larger increase for
unmasked fields (p = 0.039) does not hold against time-matched control maps,
where the increase is negative in both groups (p = 0.3); the author proposed
partially reproduced and a third round agreed. The paper reports pulsed
optogenetics with uLEDs in CA1 pyramidal neurons of four CaMKIIa-Cre::Ai32
mice: light-induced spiking falls during sharp-wave ripples, rises in the
place field and at the theta trough, unmasks place fields in non-place cells,
and with these fields ripple cofiring tracks spatial overlap for pairs that
include non-place cells. The cohort, the pulse protocol, the responsive
fraction, ripple gain, theta phase, place-cell fractions, in-field gain,
unmasked and ghost fields, stability, spatial information and ripple cofiring
were tested, all claims that need light pulses or place fields on two sessions
of one mouse (91 putative pyramidal cells, against the paper's 822). The light
intensity and intracellular claims are blocked as `data_missing`, the
excitatory against inhibitory comparison as `metadata_insufficient`, and the
position decoding, assemblies and replay as `methods_underspecified`, since
the Materials and Methods are in a supplement that could not be obtained.
Some outcomes rest on weak ground: `fig1e-responsive-fraction` is reproduced
only under reading (b), all stimulation epochs (72.5%), as the PreStim epoch
gives 62.6%; `fig4c-swr-cofiring-place-pairs` passes at p = 0.032, in sess9
only, with the same coefficient for place and non-place pairs (0.062) as for
place cell pairs (0.060); `fig3a-place-cells-more-excitable` changed outcome
with the new place-cell calls alone; and reading (a) of
`fig3c-unmasked-fields` rests on 9 cells, 7 of which have a light field
(77.8%, 95% interval 40.0 to 97.2%, including the paper's 69.3%). The author
used the NIH author manuscript in PubMed Central (PMC9632609), took method
details from buzcode and the first author's later lab code (HippoCookBook
getuLEDResponse.m), and used pyramidal cells as units with a baseline rate
below 5 Hz.

The dandiset was converted by CatalystNeuro (catalystneuro/buzsaki-lab-to-nwb).
Light pulse times are deposited for 2 of 28 sessions (fCamk1 sess9 and
sess12), and only these have laps; twenty other sessions name uLED stimulation
in their epochs but hold no pulse series. In those two sessions the files hold
pulse series for 6 of the probe's 12 uLEDs (Site3 to Site8), two of them with
only 120 to 221 pulses, and in PreStim the deposited pulses come at 5.76 and
7.50 per s, where the stated protocol implies about 17 to 25; in sess9 the
offsets between deposited pulses fall only near multiples of 20 ms, no
putative pyramidal cell on shank Group3 responds to any deposited uLED, and
time without a deposited pulse therefore cannot be taken as dark. The
OptogeneticSeries are stated in watts but hold one value per uLED, 19 in sess9
and 62623 to 63599 in sess12, so the paper's three intensities cannot be
recovered. Units carry no cell type and the no-raw-data files no waveforms.
The dandiset holds 28 sessions and 1351 units with a baseline rate below 5 Hz,
where the paper reports 822 pyramidal neurons at 43.3 per session (about 19
sessions), without saying which sessions the paper used, and 14 sessions
include CNO or DMSO epochs that the paper does not describe. Other findings:
every session is deposited twice, as a full file and a no-raw-data file with
the same units, spike times, ripples and position, and the full file of
fCamk3 sess20 is named without its session; the full file of fCamk3 sess17
holds 378 s of raw signal and 6850 s of LFP of a 34621 s session, and the six
full files of fCamk1 sess13 to sess19 hold no raw signal; session_start_time
is 2016-03-15 in every file, while the session ids date the recordings to 2020
and 2021; the linearized position holds 0 to 110 cm with a conversion factor
of 100; six sessions name their epochs only by a time stamp; in fCamk3 sess13,
fCamk3 sess17 and fCamk5 sess10 the deposited ripple intervals mark population
bursts weakly (1.2 to 1.98 times the rate 1 s later); the units table of some
files lacks the shank column; the paper gives 20 to 40 ms offsets between
pulses and the files' description 40 to 60 ms; and the paper's 822 pyramidal
neurons with 73% and 71% place cells leave about 230 non-place cells, against
its 289 of 417.

The notebook ran in 272 s in the first clean run and in 289 s after round 3.
The author's own choice of control maps as all time without light, made
before noticing that the paper's control epochs are 20 ms intervals between
pulses, was kept with time-matched windows as a variant, and that variant
decided `fig3g-spatial-information`. After round 1 the paper could not be
downloaded again (PMC returned 429 and 503 errors and Europe PMC a 500), the
round-2 verifier could not run the new field rule as numpy was not installed,
and untracked files in the repository root that the author did not create
were left alone. The author's points on the protocol: no rule for when the
paper's Methods cannot be obtained; reading the code the paper links to does
not fit a general toolbox without scripts for the paper; no guidance for data
a claim needs that exist for only a few sessions; the duplicate check does not
cover every session deposited twice as a full and a no-raw-data file; a 10%
tolerance narrower than sampling error for correlations; no category for a
named data location without a pinned identifier; and no rule for what to
record as measured when only a later reading of the criterion matches.

### 000559, Markowitz et al. 2023

Seven claims reproduced, three partially, two not reproduced and twelve
blocked, all on the dandiset. Round 1 gave its own outcome for each claim from
the notebook with its conclusions removed and agreed with 23 of the 24; it gave
not reproduced for `fig3e-learner-count`, whose criterion defines only the
reproduced case of nine learners, and the author changed that claim from
partially reproduced to not reproduced. Round 1 also found that the shuffle in
`fig2e-dlight-predicts-future-usage` permuted missing dLight peaks, which made
the null conservative; with the fix the claim stayed partially reproduced,
significant at 6 of 10 values of n up to 190. Round 2 agreed with all 24 and
nothing was proposed, so there was no third round. The paper reports that
dopamine in the dorsolateral striatum of freely moving mice relates to the use
of behavioural syllables and their sequences, and that pairing a syllable with
optogenetic dopamine release (Opto-DA) increases its use. The relation of
dLight to speed across timescales, dLight differences across syllables and
their decoding, the across-syllable relations to syllable count and transition
entropy, the prediction of future usage, the DMS transient rate and usage
prediction, Opto-DA learning, the cumulative counts, the learner count and the
correlation between stimulation and post sessions were tested. The four claims
that compare stimulation with catch trials are blocked as
`metadata_insufficient`, the food-reward transients as `data_missing`, and
seven claims as `other`, not attempted for time, though their data are in the
dandiset. Some outcomes rest on weak ground: in
`fig1h-syllable-dlight-differs` H = 266.40 against the paper's 209.29 while n =
518 matches, and neither the quality filter nor the post-session rule explains
the gap; `ed7-dms-no-usage-prediction` is not reproduced by this attempt's
lagged test, which finds DMS stronger than DLS and probably differs from the
paper's, while Extended Data Fig. 7 has no lagged test and the attempt's DMS
across-syllable count test agrees with the paper (r = 0.026, P = 0.170); the 7
learners against 9 are all among the nine the paper's code printed, with no
single cause found; and for `fig3l-no-kinematic-effect` and
`fig3m-long-stim-velocity` the criterion taken literally gives not reproduced
and partially reproduced. The author used the open access full text, and took
analysis parameters where the Methods are silent and the nine learner mice,
for comparison only, from the paper's code at commit 14ed714.

The dandiset was converted by CatalystNeuro (catalystneuro/datta-lab-to-nwb).
The closed-loop files mark stimulation onsets but not catch trials; the
conversion kept only the stimulated detections, so Fig. 3i, 3l, 3m and 4f
cannot be tested, and a substitute selection shows stimulation-catch
differences in 9 of 12 no-opsin controls, with stimulations a median 0.593 of
detections per mouse where the Methods give 75 %. No file states the genotype
or opsin of a mouse: Opto-DA (Ai32) and no-opsin control mice are told apart
only by the stimulation site, and the dLight+ChrimsonR mice only by their
subject names. Session type and session number are not stored and must be
inferred from free-text descriptions, dates and stimulation pulses, and five
files with stimulation are described as recording sessions. The re-referenced,
z-scored dLight trace used by every photometry analysis is not stored, nor the
regression fit needed to recompute it. The dandiset holds 224 DLS photometry
files without stimulation (210 with syllables, 193 of them not habituation
sessions, 177 of those passing the quality criteria), where the Methods give
379 experiments; for the dLight+ChrimsonR mice only the 250-ms closed-loop
sessions are present; and the food-reward sessions and consumption times of
Fig. 2a are missing. Other findings: every closed-loop file states a 635-nm
stimulator, including the Ai32 (ChR2) mice, which the Methods say were
stimulated with 470-nm light; the dLight-only mice carry the subject
description "wild-type DAT-IRES-Cre and Ai32 mice"; in 28 photometry and 547
closed-loop files the syllable timestamps are not ascending, in 573 of these
575 because the rows are rotated with one backward step, which is at least
0.95 of the session length in 558 files, and sorting restores a regular 30-Hz
clock; two closed-loop files of mouse 3155 store every syllable frame twice
(53,822 and 53,862 repeated timestamps); 14 files of dLight+ChrimsonR mice
hold empty syllable series; and 111 behaviour-only files and the sessions that
fail the paper's quality criteria (16 DLS and 11 DMS) are included with no
flag saying which were excluded from the paper.

A first survey of metadata in all files timed out after an hour and a second
took 46 minutes, as h5py serializes threads, so the notebook uses processes;
it ran in 763 s in the first clean run and 13.3 minutes after round 2. Round 1
also led to leaving habituation sessions out of every photometry analysis,
which moved most DLS numbers but no outcome. Round 2 found the README run time
and some statements unsupported by the outputs, and in checking them the
author found the rotated-clock finding inexact and corrected it, adding the
finding on repeated frames. Untracked files in the repository root that the
author did not create were left alone. The author's points on the protocol: no
blocking reason for a claim not attempted for time; no rule for which reason
to give when a selection fails a control check; a criterion that defines only
the reproduced case; a clock check whose contrast assumed a direction and came
out reversed because dLight dips at syllable onset; whether the paper's own
data deposit may fill what the conversion dropped; a default 10% tolerance on
a test statistic that grows with sample size; whether a reference list used
only for comparison makes a claim `with_inputs`; and a notebook that streams
1,723 files and takes about 13 minutes, over the 10-minute aim.

### 000718, Zaki et al. 2024

Two claims reproduced, two not reproduced and twenty-one blocked on the
dandiset. With outside data, counted apart: one reproduced. Round 1 gave its
own outcome for each claim from the notebook with its conclusions removed and
agreed with 25 of the 26; it gave not reproduced for
`offline-bursts-above-shuffle`, as the criterion is written, and suggested
blocking it as `methods_underspecified`, which the record already did, as
round 1 had not seen the record. Round 1 agreed that
`fig5c-wake-overlap-neutral-coburst` was partially reproduced by the letter of
the criterion, but argued that the Methods' scoring has no quiet-wake class;
applied to Ca_EEG2-1's EMG it puts 94.1% of quiet-wake frames and all 87
bursts in wake, and under that reading the overlap ensemble co-bursts less
with the neutral than with the aversive ensemble (26.4 against 35.6%, McNemar
p = 0.13), so the author changed the claim to not reproduced and recorded the
departure from the criterion as a deviation. Round 2 agreed with all 26 and
nothing was proposed, so there was no third round. The paper reports that a
strong aversive experience links fear to a neutral context experienced two
days before, that neutral and aversive ensembles in CA1 co-reactivate in
offline population bursts, mostly during wake, and that this co-bursting of
the overlap ensemble with the neutral ensemble goes with the linking. The link
to the paper's per-mouse source data, aversive freezing of the high- against
the low-shock mouse, bursts and skew against shuffled data, the pause in
movement before bursts and wake co-bursting were tested, the last four on the
EEG/EMG cohort where the paper shows three of them in another cohort. The
bursts claim is blocked as `methods_underspecified`, since surrogate over true
burst rate is 1.26 to 1.60 against the paper's 0.72 to 0.96, and a synthetic
control shows the criterion's test cannot detect coordination (5.6 true
against 34.98 surrogate bursts per min); the other 20 blocked claims are
`data_missing`. Some outcomes rest on weak ground:
`ed9b-aversive-freezing-high-vs-low` compares one mouse per group over 30 s
bins that are not independent; in `offline-skew-above-shuffle` both arms are
below the paper's Extended Data Figure 3o values, so the chance level is not
shown to match the paper's; `burst-locomotion-pause` uses the telemetry
activity signal as a proxy for the paper's webcam tracking, and the test gives
p = 0.016 at 300 random times in Ca_EEG2-1; and
`fig5c-wake-overlap-neutral-coburst` rests on one 10 min recording of one
mouse, z-scored within it, and on a log EMG RMS measure chosen after the data
were seen. The author used the open access full text (PMC11666460).

The dandiset was converted by CatalystNeuro (catalystneuro/cai-lab-to-nwb). It
holds two of the nine mice of the calcium imaging and EEG/EMG experiment
(Ca_EEG2-1, high shock; Ca_EEG3-4, low shock) and, of each offline period,
only the first 10 min recording of the 24 the Methods describe; Ca_EEG2-1 has
no offline-day-1 recording and no neutral or novel recall session, and the
mice of the one-hour imaging and offline experiments, the behaviour-only
experiments and the inhibitory tagging and no-shock experiments are not
deposited, so twenty of the 26 claims cannot be tested. Ca_EEG3-4 has no cell
registration, so its ensembles cannot be formed, and the Week file of
Ca_EEG2-1 holds 19 registration tables for offline-day-2 recordings, of which
only the first recording is deposited, and none for offline day 1. The
dandiset does not say why these two mice and only the first offline recording
of each period were deposited, nor that the paper analysed more. The session
start times of the Ca_EEG2-1 behaviour sessions, and the Week epochs built
from them, are about 1 h later than the telemetry and Miniscope clock, so that
OfflineDay2Session1 starts 47 min before the FC session it follows; the
telemetry is absent in windows that contain each of these epochs moved 1 h
earlier. Other findings: the OnePhotonSeries timestamps of three files run at
16.7 ms and end at half the recording's length, while their frame counts fit
30 Hz over the full length; the sleep states include `quiet wake`, which the
paper neither uses nor maps to its states, and the three offline recordings
hold no NREM or REM epochs; the telemetry is sampled at 500 Hz where the
Methods say 100 Hz; the offline session description speaks of an hour of
recording with a webcam, where the deposited recordings last 10 min and hold
telemetry and no video; the fluorescence series carry placeholder
descriptions and unit "n.a.", the FC session descriptions give the shock
amplitude without a unit, and the Week file has an empty session
description; and the analysis code repository the paper names returns 404.
The registration tables agree with the ROI centroids, no recording is
deposited twice, and calcium, behaviour and telemetry are consistent with a
shared clock except in Ca_EEG3-4 offline day 1, where it could not be
established.

The notebook ran in 81 s in the first clean run, and `tools/entry.py all`
took about 2 minutes after round 1. `git clone` from GitHub asked for
credentials, so the source-data and conversion repositories were fetched as
tarballs at pinned commits; removing `__pycache__` and an empty `.claude/`
directory in the entry was denied, and untracked files in the repository root
that the author did not create were left alone. Round 2 found sentences the
outputs did not support, among them that the skew values lie in the range of
the paper's, and a wrong grouping of `fig1ef` and `fig1g`, and these were
corrected. The author's points on the protocol: general claims shown only in a
cohort that is not deposited; a chance level the paper states only in its
source data, for another cohort at another frame rate; whether the lab's
repository of per-mouse figure values counts as data deposited elsewhere; a
link claim on which no claim depends; across-mouse claims with one mouse per
group; a clock check that covers streams within a session but not start times
across sessions; a value seen in the data check before the criteria were
written; and which year to use in the entry name for a paper online in 2024
and in an issue of 2025.

### 000691, Scherrer et al. 2023

Six claims reproduced and seven blocked on the dandiset, plus two claims on
data in other archives, both partially reproduced. Round 1 gave its own
outcome for each claim from the notebook with its conclusions removed and
agreed with all 15 as they then stood, but suspected that the SGD solver
explained why no point of the local decoding map was significant (0 of 151);
the 32-footprint decoders stop at objectives of 19.8 to 68.9 where the
optimum is 1.976 to 2.000, so the author fit them with liblinear, as
MATLAB's default for 100 or fewer predictors is BFGS run to convergence, and
`ed9c-local-decoding-map` moved from not reproduced to reproduced. Round 2
agreed with all 15 and nothing was proposed, so there was no third round.
The paper reports two head-mounted microscopes with axicon correction
optics, one optimized for weight (1.0 g, 1.0 mm FOV) and one for field of
view (1.4 g, about 4 mm), that image hundreds of neurons in juvenile
songbirds and thousands in a freely behaving mouse, whose position and
direction in a looped maze can be decoded from the imaged activity. The
footprint count and the mouse's coverage of the maze, decoding of quadrant
with direction and of octant, the local decoding map, localized activity
and the spread of coactive footprints in 8 NMF components were tested on the
one deposited mouse, with position tracked from the behaviour video, and the
flat illumination of both microscopes on dye images in the paper's code
repository. The 2382 curated footprints and the field of view are blocked as
`metadata_insufficient`, and the other mice, the songbirds, the weights, the
resolution targets and the analog-to-digital converter as `data_missing`.
Some outcomes rest on weak ground: `ed9c-local-decoding-map` gives 1
significant point with SGD and 18 of 150 with liblinear, the solver was
changed after round 1, liblinear reached its limit of 10,000 iterations in
2268 of 3000 fits, and the smallest significant z, 2.53, is below the 3.40 a
point needs alone; in `ed8-coactive-distributed` random sets of footprints of
the same size have spread ratios of 0.951 to 1.042, so any set this large
passes the criterion's half; `ed2c-kiloscope-flat-illumination` misses the
0.8 level the author chose by 0.003 and is above it for one of four 100 um
moves of the centre; and every analysis uses all 2948 footprints in place
of the 2382 curated ones. The version of record is not open access, so the
author used its abstract, figure titles, Extended Data legends and data and
code statements, read the bioRxiv preprint (version 2) for its Methods only,
and took the parameters of every analysis from the paper's code at commit
d596646; the legend of Figure 2 and the main text's numbers were not tested.

The dandiset was converted by CatalystNeuro (Szonja Weigl of CatalystNeuro
is a contributor). It holds one of the paper's four mice and none of the
songbird recordings or optical test data, and the Academic Torrents deposit
the paper names for its imaging data holds files of the same mouse session
only, so the other mice and the birds are not public. The 2948 footprints
are the EXTRACT output before curation, and nothing in the dandiset marks
the 2382 the paper kept or says that the footprints are uncurated; the
curation is in the Academic Torrents deposit, where no peer connected in two
attempts of 2.5 and 4 minutes. The mouse's position, which the decoding and
place analyses use, is not in the dandiset and must be tracked from the
behaviour video, and the first 64 s of the video (by its nominal rate), which
the paper's code drops because the experimenter is in view, are not marked.
The device description reads "Head-mounted microscope (Kiloscope) optimized
for weight (1.0 mm FOV; 1.0 g)" and the dandiset description also names the
microscope optimized for weight, while the data are from the large-FOV
microscope (a 4 mm window, 2948 footprints and 808 x 608 pixel frames). The
imaging is stored as a TwoPhotonSeries and listed as two-photon microscopy,
though the microscope is a one-photon epifluorescence microscope. Other
findings: the behaviour video is described as about 30 fps and its AVI
header says 30 frames/s, but its 15521 timestamps run at a median 12.5
frames/s over 1234 s, and at 30 frames/s it would cover only 517 s of the
1234 s of imaging; the imaging plane gives no pixel size, and its indicator
and location are "unknown" with no excitation wavelength, although
general/virus says GCaMP7f; the Extended Data Fig. 9c legend describes
decoders on the 32 closest footprints within 270 um, where the code uses 64
within 50 pixels, which at the code's own 5.94 um per pixel is 297 um; and
the title of Extended Data Fig. 8 refers to the Kiloscope data "shown in
Figure 3", while the version of record has two figures. The masks, the movie
and the traces line up, and position decoding peaks within about a second
of zero shift, so the clocks are reported as consistent, though offsets of
1 to 2 s could not be told apart.

The notebook ran in 18 minutes in the first clean run and in 25.2 minutes
after round 2. Streaming the behaviour video with PyAV over HTTPS and
through remfile failed, so the notebook reads the 105 MB file into memory;
liblinear's coordinate order was seeded after round 1, as unseeded the
exact map's count of significant points changed between runs; and the code's
64-footprint variant of the local map stays on a 60 pixel grid where the
criterion says 40, since on 40 the notebook took 32 minutes, over the
30-minute limit. Round 2 found numbers in the text that the executed
notebook contradicted (19 significant points against 18, 2264 fits at the
limit against 2268); the copy it read came from another machine, three runs
on four cores gave the stated numbers, and the text now says the counts can
differ slightly between machines. The author's points on the protocol: a
paper that is not open access whose legends and preprint are public; outside
data on a torrent with no peers, which the blocking categories do not fit;
whether data derived from the dandiset's own video, such as position, count
as dandiset data; an image-reading check that forbids reading measurement
images that are data; hardware claims with no data anywhere; a clock check
that cannot resolve offsets of 1 to 2 s; an outcome 0.003 from a threshold
the author chose, as the legend gives no number for flat; and a prototype
decoder run before the criteria were written.

### 000727, Brezovec et al. 2022

Eight claims reproduced, five partially, one not reproduced and six blocked,
all on the dandiset. Round 1 gave its own outcome for each claim from the
notebook with its conclusions removed and agreed with 19 of the 20; it gave
partially reproduced for `fig5c-global-below-threshold`, as the pass under
one reading rests on r = 0.013 with a p-value that treats autocorrelated
samples as independent. The author kept reproduced and added a null of 200
rolls of each fly's behaviour in time, against which the weakest correlation
has p = 0.025 (null 95th percentile 0.010), and round 2 agreed. Round 1 would
also have blocked the four region-level claims as `data_missing`; the author
kept `metadata_insufficient`, as the voxel data are deposited and only their
labels are missing, and round 2 accepted it. Round 1 also found a wrong
denominator in reading (b) of `fig2c-fraction-correlated`, which moved 54.9%
to 53.5% and no outcome. Round 2 agreed with all 20 and nothing was proposed,
so there was no third round. The preprint reports that whole-brain imaging of
nine walking flies shows activity correlated with forward and turning
velocity across much of the brain, organized by neuropil and mirror-symmetric
for forward velocity, that linear models on the principal components predict
behaviour with weights stereotyped across flies, that turning raises activity
on one side and lowers it on the other, and that peak correlation times range
from leading to lagging behaviour, with lagging voxels broader in time. The
dataset structure, the share and tuning of correlated voxels, the symmetry,
the PC structure, the ridge R2 and its relation to movement, the weights, the
unique variance of forward velocity and walking state, the below-threshold
correlations of the demixed regions, the ipsilateral and contralateral
changes, the peak time range, lag against width and the ipsilateral lead were
tested on 12 of 91 planes with 6 x 6 voxel blocks in place of supervoxels.
The four region-level claims are blocked as `metadata_insufficient`, the
tdTomato control as `data_missing` and the supervoxel number sweep as
`too_large`. Some outcomes rest on weak ground: `fig6-peak-time-range` gives
0.32 s with behaviour at the volume midpoint, but 0.58 s at the volume start
and 0.50 s with each plane's median removed, so only the lag of more than 1 s
is robust; `fig5c-global-below-threshold` holds under reading (b) only, with a
left region of 4 blocks; and in `fig2-symmetry` a left-right flip of fly_105
is not excluded. The author used the full text of bioRxiv version 1, as the
Current Biology version is paywalled, and took parameters where the Methods
are silent from the paper's code at commit 8e2b275.

The dandiset was converted by CatalystNeuro (catalystneuro/clandinin-lab-to-nwb).
The processed volumes are registered into the Functional Drosophila Atlas, a
space from a later paper of the lab, while the preprint analyses its data in
its own mean brain, and the dandiset holds no neuropil labels, atlas or
template for that space, nor the paper's mean brain and registered atlas, so
none of the region-level results (Figures 2E to I, 3, 6E to G, 7) can be
tested; nor does it say how the FDA series relates to the preprint's analysis
space. The per-plane acquisition times are not in the files, which give only
a volume rate, and sampling behaviour at the start in place of the middle of
each volume changes the correlated share of the brain from 31.1% to 39.2% and
the 99th percentile of forward-velocity lead from 0.32 to 0.58 s. The
supervoxel labels, the z-depth maps and the motion-corrected tdTomato channel
are not deposited. The processed series has grid spacing 1, 1, 1 in unit
"unknown", and nothing states which half of the volume is the fly's left.
Imaging and FicTrac both start at 0 s, as the conversion code set FicTrac
timestamps to a uniform 50 Hz from 0 because synchronisation data were
missing, which the dandiset does not say; the data are consistent with a
shared start (brain-wide activity follows walking speed by 0.4 to 0.8 s in
every fly) to within a few hundred milliseconds. Every FicTrac SpatialSeries
has unit "meters" and conversion 0.0045 (the ball radius), while most hold
angles in radians, and SpatialSeriesRotationDeltaError, described as an error
in radians, has medians of 6067 to 10,435. Other findings: the paper's code
computes the walking state with np.sqrt(a, b), which reduces it to forward
velocity alone, and the two versions mark 47.2% and 57.3% of time points as
walking; the Methods cite Figure 3F and 3G for panels in Figure 4, and Figure
3G is the Nodulus in the Results and the Ellipsoid Body in the legend; and the
preprint says the data were deposited at Dryad, where no record was found,
while the dandiset links neither Dryad nor the analysis code, which was found
as ClandininLab/brezovec_volition_2023 under a different title.

The notebook ran in 483 s in the first clean run and in 12.3 minutes in the
latest run. h5py over the network read at 2.6 MB/s, so the helper reads the
gzip chunks by HTTP range requests at about 98 MB/s, matching h5py in all
nine files; bioRxiv rate-limited the downloads and after round 1 the paper
could not be fetched again, and the GitHub API reached its limit, so the
repositories were cloned with git. Round 2 found statements the outputs
contradicted (the README run time, the time to stream the 12 planes, and a
round-1 response saying the lag of more than 1 s held in every plane from 38)
and a flip check, the overlap of each brain mask with its mirror, that cannot
detect a flip; these were corrected and the check replaced with leave-one-out
maps. Untracked files in the repository root that the author did not create
were left alone. The author's points on the protocol: a paper that names no
code repository, with the code found by search under another title; outside
resources the dandiset's processed data depend on but the paper does not
use; no rule for testing on a sample of a dataset too large to stream; where
the data check ends when prototypes are needed to find the left-right axis; a
clock check that cannot resolve the sub-volume alignment some claims need;
no definition of partially reproduced for a single expected value; what to
record as measured when no reading matches; following code that tunes on test
data; and a default 10% tolerance, kept for "approximately 0.3", which is
strict.

### 000947, Schwab et al. 2020

Six claims reproduced, four partially, seven not reproduced and one blocked
on the dandiset. With outside data, counted apart: one reproduced. Two claims
on data in other archives are blocked. Round 1 gave its own outcome for each
claim from the notebook with its conclusions removed and agreed with all 21 as
they then stood, but found that the reaction-time test of `behavior-rt-mt` ran
on all 250 pre-MPTP files with trials, including files with motor cortex, SMA
or VLp units only; restricted to the 165 files with units of the dandiset
rule, reaction times differ neither between the animals (p = 0.89) nor between
directions (p = 0.41), and the author changed the claim from partially
reproduced to reproduced. Round 2 agreed with all 21 and nothing was proposed,
so there was no third round. The paper reports single units in GPi and VLa of
two macaques (NHP G and NHP I) during reaching, compares the onset and sign of
their peri-movement changes with what gating of thalamus by GPi predicts, and
tests correlations between simultaneously recorded GPi and VLa units, the VLa
rate after GPi bursts and pauses, and a model thalamocortical cell. The link
to the paper's unit list, the unit counts, rest rates, spike widths,
hold-period ramps, responsive fractions, response forms, integrated change,
onset latencies, the gating conflict fraction, directional units, spike and
noise correlations, the VLa rate after bursts and the behaviour were tested,
on units chosen by a rule built from the dandiset's location labels and the
Methods' criteria, with the paper's unit list shown as a variant only. The
VLa localization is blocked as `data_missing`, since the stimulation mapping
is not public, the EMG onset as `methods_underspecified` and the simulation
as `other`. Some outcomes rest on weak ground: four depend on the selection of
units, as with the paper's records `hold-period-ramps`,
`monophasic-more-in-vla` and `fig3a-vla-leads-gpi` would be reproduced and
`fig3b-gpi-decr-lag-vla-incr` partially reproduced; in
`fig3b-gpi-decr-lag-vla-incr` the GPi median is 0.2 ms inside its tolerance;
the hold-period fractions and the 95.4% of comparisons that conflict with
gating equal their chance levels (98.4% and 99.0% with random alignment, 95.1%
with shuffled onsets); with random alignment the detector finds a decrease in
33.7% of VLa unit-directions (44.2% in the data), which may pull the VLa
decrease onsets of `fig3c-vla-decr-lead-gpi-incr` late; and in
`fig5-vla-decrease-after-gpi-bursts` bursts last 67.1 ms against the paper's
24 ms and the per-pair test is at chance, so that outcome says little about the
paper's finding. The author used the open access full text, and took the
paper's unit list and analysis code from its Dryad deposit, read from the
Zenodo mirror (record 4000719) as the Dryad download API requires a token.

The dandiset was converted by CatalystNeuro (catalystneuro/turner-lab-to-nwb).
It holds more GPi and VLa units than the paper analysed (268 GPi and 279 VLa
units under its own labels and the Methods' rate criteria, against 209 and
185) and does not say which units the paper kept; the paper's unit list is
only in its Dryad deposit. No identifier links a neuron recorded over
consecutive files: 97 of the paper's 394 units span 2 to 5 files, and the
dandiset stores them as separate units. Location labels are inconsistent: GPi
and VLa are written GPI and VLA in some files, 54 Gaia thalamic units are
labelled only "Thalamus" (25 of them are VLa units in the paper), and 33 Isis
units have an empty location and no channel id. 30 of the 394 units the paper
analysed are not among the curated units, and 21 of 254 pre-MPTP files have no
curated units; 13 of them hold sorted clusters in processing/ecephys/units
(124 in all) whose only columns are spike times, unit name and location, and 8
have no such table. The electrode coordinates put the electrodes labelled VLa
ventral of those labelled VLp, if z is ventral positive as the column
description says, where the paper places VLa dorsal of VLp, and the files do
not say how the labels were assigned. Other findings: in all 254 pre-MPTP
files the session_start_time is two days after the date in the session_id;
sort labels are letters in some files and numbers in others, and the unit
quality column is missing from some files and holds free text (for example
"B -> C") in others; error trials are flagged only in the 127 of 253 files
with trials that have an error_onset_time column, and movement ends are
missing from 87 files, all of them Gaia, so the Methods' trial exclusion can
be applied only in part; I-160616-4 has no trials table, though it has 5
curated units and raw data, and one spike train is stored twice in I-170518-2,
as two M1-S units on channels 40 and 43; the pre-MPTP files name the paper only
by its bioRxiv preprint; the EMG of S3 Fig is in the Dryad deposit and not in
the dandiset; and the paper gives 218 VLa units and 94% responsive VLa units
in the Results where Table 1 gives 185 and 88.1%, and Fig 3C onsets of -62 and
-108 ms where Table 1 gives -76 and -95.5 ms.

The notebook ran in 687 s in the first clean run, `tools/entry.py all` took
798 s after round 1, and the notebook ran in 18.9 minutes after round 2. A
first run computed the burst surprise with log10, which gave bursts far longer
than the paper's, and the natural log was then used, with log10 kept as a
variant; a first burst control that did not keep the shifted events in rest
periods was fixed before the conclusions were written. Round 2 found
statements the outputs did not support, among them that two outcomes depend
on the selection of units where four do, the README run time and two findings
with no output behind them, and these were corrected; in the revision the
author also found that I-160616-4 has curated units and raw data, which the
record had said it lacked. A Zenodo search command was denied by the permission
system and rerun without the `rm` it included, and untracked files in the
repository root that the author did not create were left alone. The author's points on
the protocol: whether the paper's unit list, a selection of units, may be used
as an outside input; a Dryad download that needs a token; no null for the
clock check of spikes with a trial table, as shifted labels and offsets both
carry the target's effect; no data category for a simulation; a criterion that
defines only the reproduced case; a method error found after a first run; a
control first run not as the criterion stated; and no rule for a reported
fraction that matches its chance level.

### 000971, Seiler et al. 2022

Seventeen claims reproduced, nine partially, six not reproduced and five
blocked on the dandiset. With outside data, counted apart: one reproduced.
Round 1 gave its own outcome for each claim from the notebook with its
conclusions removed and agreed with 37 of the 38; it would block
`fig6-nphr-learning-dropout`, as the dandiset holds 13 NpHR, 13 NpHR Scrambled
and 16 EYFP mice where Figure 6F counts 16, 15 and 16, so the mice the paper
dropped are, but for one, not deposited, and the author changed the claim from
not reproduced to blocked as `data_missing`. Round 1 also asked for the
training files with no rewards to be inspected; one is a 170 s false start of
mouse 140.306, without which Tukey PS vs DPR in `fig2n-rewards-per-session`
gives p = 0.059, and the author changed that claim from reproduced to
partially reproduced. Round 2 agreed with all 38 and nothing was proposed, so
there was no third round. The paper reports that RI60-trained mice accept more
shocks in shock probes than RR20-trained mice, that RI60 mice split into
punishment resistant (PR), delayed punishment resistant (DPR) and punishment
sensitive (PS) phenotypes, that a DMS dopamine axon score from fiber
photometry differs by phenotype and correlates with shocks while the DLS score
does not, and that stimulating DMS dopamine terminals on rewarded nosepokes
makes mice more likely to be PR and inhibiting them more likely to be PS,
while DLS stimulation has no such effect. The schedule comparisons, the
phenotype rule and the training and omission behaviour of the phenotypes, sex
differences, the DMS and DLS scores against phenotype, shocks and omission
time, and the DMS excitation, DMS inhibition and DLS excitation cohorts were
tested, and the DAT protein claim on the Zenodo densitometry table the
dandiset names. The RI30 photometry peaks, the inhibition dropouts, fear
conditioning, open field and histology are blocked as `data_missing`. Some
outcomes rest on weak ground: `fig4g-dls-score-shock-no-correlation` is not
reproduced (r = 0.326, p = 0.024) only with a dropout step the author added
after seeing per-session scores, which is in neither the Methods nor the
authors' code, and without it r = 0.113, p = 0.45; the same step takes the
phenotype p of `fig3f-dms-score-phenotype` from 0.389 to 0.100;
`fig3g-dms-score-shock-correlation` is partially reproduced on one of three
readings (r = 0.375, p = 0.045, n = 29), with p = 0.13 after correction for the
three; `fig2n-rewards-per-session` gives p = 0.048, 0.059 or 0.044 under three
session-exclusion rules, and the one used, set after round 1, is the only one
above 0.05; `fig5f-dms-chr2-escalation` and `fig7f-dls-escalation-similar`
rest on the pooled fit with no mouse term that the criterion fixed, and a mixed
model with a random slope per mouse would make fig5f partially reproduced but
warns of a boundary fit, while a model with a random intercept only puts ChR2
above neither control; and the claims on Figures S1 to S7 rest on the main
text alone. The author used the author manuscript in PubMed Central
(PMC8930615), whose supplement could not be downloaded, and took the
photometry processing from the authors' MATLAB code at commit 56f1529.

The dandiset was converted by CatalystNeuro (catalystneuro/lerner-lab-to-nwb).
The Methods say photometry was recorded during RI30 and on both shock probes,
but the dandiset holds photometry only for RI60 and RR20 training (62
sessions) and one session described as a probe test. Mice are missing against
the paper: 6 RR20 mice against 9 in Figure 1D (7 in the Methods), 33 DMS
excitatory mice against 39, 42 DMS inhibitory mice against 47 and 35 DLS
excitatory mice against 36, and several mice lack a probe; the NpHR mice
missing are about the number the paper dropped for not learning, and the 'Did
Not Learn' flag marks one NpHR mouse and one EYFP mouse that reached RI60.
Optogenetic mice have no stored phenotype (the notes read 'Punishment Group
nan'), and the DMS inhibitory files do not say whether a mouse is in group 1
or group 2. The fear conditioning, open field and histology are not deposited,
and the paper says data are available on request. Several photometry
recordings hold dropouts where a raw channel falls near zero (6 sessions reach
|z| above 50 after the authors' processing, up to 1758), and in 141.308 on
2019-08-09 the DLS channels drop out through most of the recording, with
nothing marking these or saying which recordings the paper excluded. The 137
files of the group 'Opto-DLS-Excitatory-Unknown' repeat sessions deposited
under a named arm (135 share subject and start time with a named file). Other
findings: 20 RR20 training files of four mice hold port entries only; 11
mouse-days have two or three RI60 files, with nothing saying which is the
day's session (81.236 on 2019-02-06 has 6, 28 and 42 rewards); in 45 of 64
RR20 training files with rewards the reward times coincide with no nosepoke
time; in shock probes on the left nosepoke the reward series is named
right_reward_times (151 files); the stitched photometry session of 332.393 on
2020-07-28 mixes MedPC reward times with TDT nosepoke times; mouse 290.407 is
filed under two experiments; the fiber coordinates are stored without their
signs (DV 2.8 for -2.8, DLS AP 0.1 for -0.1); the authors' MATLAB comments call
Dv1A the control, while the conversion and the files take it as the DMS 465 nm
signal, and the data side with the files in 46 of 61 DMS sessions; 048.392 is
stored as PR with 13 early shocks where the Methods require more than 13, and
the Methods call 13 a median split while the median is 9; the Results give
omission times in seconds that fit minutes, and the Methods give 26 DMS
inhibitory and 7 RR20 mice where the figures count 47 and 9; and the Zenodo
densitometry table holds female samples only, labelled as lanes of one
wild-type and one heterozygous mouse, while the dandiset's blot images include
males.

The notebook ran in 760 s in the first clean run, in about 25 minutes (1407 s)
after round 1, and `tools/entry.py all` took 957 s after round 2. The Europe
PMC full text returned a 500 error and NCBI BioC rate-limited the author, and
the supplement returned a browser check, later a reCAPTCHA page, with the Cell
and Europe PMC copies returning 403. Round 2 found sentences the outputs did
not support, among them that the dropout step had little effect on fig3g and
mixed-model results reported without their convergence and singularity
warnings, and these were corrected. Untracked files in the repository root
that the author did not create were left alone. The author's points on the
protocol: a full text whose supplement cannot be fetched; a tolerance taken
from a stated spread that is the SD across mice, which becomes very wide; no
rule for a data-quality fix found after seeing scores; absence claims for
which the paper gives no test; no outcome for a claim tested on data only
partly deposited; a probe rule refined after the data check; a 10-minute
runtime aim for a dandiset of 4139 files; and version pinning for a paper that
predates its dandiset when all versions hold the same files.

### 001038, Azcorra et al. 2023

Sixteen claims reproduced, seven partially and one not reproduced on the
dandiset, none blocked. Five claims on data in other archives: two
reproduced, on the snRNA-seq count matrices in GEO (GSE222558), and three
blocked. Round 1 gave its own outcome for each claim from the notebook with
its conclusions removed and agreed with all 29, giving other reasons only for
the three blocked claims; the author kept `not_runnable` for the two claims
that need Seurat and LIGER in R and `other` for the histology claim, which
rests on manual cell counts that are not deposited, as the images are public
on Zenodo. After round 1, `fig5ab-transient-scaling` uses the recomputed onsets
that are also stored, which carry the code's exclusion after every reward
(241, 246 and 232% against 239, 266 and 222% before), and stays partially
reproduced. Round 2 agreed with all 29 and nothing was proposed, so there was
no third round. The paper reports that genetic subtypes of dopamine neurons
signal differently: Vglut2 and Calb1 axons in striatum show transients after
decelerations and respond to rewards and air puffs, Anxa1 axons show
transients after accelerations, have almost no reward response and decrease
to air puffs, the subtypes can be clustered from these responses, and somas in
SNc track their axons. The recording counts, the cross-correlations with
acceleration and their lags, PCA and angles, triggered averages and transient
scaling, the reward and air puff responses, the k-means clustering, the soma
and axon correlations, the SNc responses, Aldh1a1 heterogeneity, the overlap
region and two snRNA-seq claims were tested; the snRNA-seq clustering and the
integration of four published datasets are blocked as `not_runnable`.
`recording-counts-locomotion` is not reproduced: the Methods' criteria select
50, 28, 82, 89 and 85 striatal recordings for Vglut2, Calb1, Anxa1, DAT and
Aldh1a1, against 42, 22, 47, 74 and 75, and no variant gives the paper's
counts. Some outcomes rest on weak ground: the 18 claims that use the
locomotion selection are tested on this larger set; `fig2jk-pca-variance` is
inside tolerance by 0.5 and 0.02 points; in `fig2l-pc-angles` the Anxa1 mean
depends on where the circle is cut (circular mean 301.3 against 233.3
degrees); `fig4g-reward-response` is partially reproduced with the Methods'
windows, while the code's windows give the paper's 7.90, 12.40 and 5.88; the
cause of the Vglut2 peak timing in `ed6f-dec-peak-timing` and of the DAT air
puff mean (2.69 against 5.3) is not found; and the deep band of
`ed1h-aldh1a1-depth` holds 5 recordings. The author used the open access full
text (PMC10545540) and took what the Methods leave open from the paper's code
at commit fad12b2.

The dandiset was converted by CatalystNeuro (catalystneuro/dombeck-lab-to-nwb).
The files carry the signal-to-noise ratio and 405 nm cross-correlation but not
the other exclusion flags (running time, 405 nm artifacts) or which recordings
each figure uses; recomputed with the paper's code, the stimulus analyses give
the paper's counts exactly, but the locomotion criteria select more striatal
recordings than Figure 2 reports (Anxa1 82 against 47, Vglut2 50 against 42).
The Events table lists consumed rewards only, and rewards the mouse did not
lick for are only in the raw 4 kHz Reward trace, so 911 acceleration and 767
deceleration onsets recomputed from the processed data are not in the stored
WheelEvents. The `coordinates` column of the fiber table is described as (AP,
ML, DV) but holds (ML, AP, DV), and 785 of 790 SNc fibers and 1281 of 2137
fibers overall have no coordinates. The column
`cross_correlation_with_acceleration` holds the peak cross-correlation of the
405 nm control with acceleration, not of dF/F, and is missing where running
was under 100 s. The dF/F series are normalized so that the largest transient
is 1, which the files do not state, and the normalization factor in
`normalized_fluorescence` holds two values per row in 123 files. Other
findings: three subject ids ending in L are left-hemisphere recordings of mice
that also have ids without it, so the archive's 105 subjects are 102 mice, and
the age is a range (P8W/P16W) in every file; the published version's link to
the paper is malformed (fixed in the draft) and its asset summary lists only
"analytical technique" and "ProcessingModule"; the code integrates responses
over windows that differ from the Methods', and the paper's reward means equal
those of the code's windows to the decimal, as do its Vglut2, Calb1 and Anxa1
air puff means within tolerance, while its DAT air puff mean (5.3) does not
(2.46); the code reports trough and peak times 0.02 and 0.01 s later than the
Methods define, prints uncorrected p-values for Figures 2i and 7f, whose
legends state Bonferroni correction, and marks 405 nm artifacts from the last
noisy section to the end of a recording and from the start to the first; and
the paper swaps the Calb1 and Vglut2 reward P-values between the Results and
the Figure 4g legend, gives 10 Anxa1 mice in the Figure 2f legend and 9 in the
Methods, and gives different SNc variance values in Extended Data Figure 9k
and the Methods. No recording is deposited twice.

The notebook ran in 182 s in the first clean run, `tools/entry.py all` took
107 s after round 1 and 2.3 minutes after round 2. The first metadata scan
took 30 minutes, as h5py serializes calls across threads and every download
URL needed its own API request, and was sped up with a process pool, the bulk
asset listing and BLAS limited to one thread; early runs crashed on the files
with two `normalized_fluorescence` values per row; and the paper's 4.4 GB
MATLAB table on Zenodo, which carries the exclusion flags, was not practical
to parse. Round 2 found statements the outputs did not support, among them
that the Calb1 trough lag with the code's timing equals the paper's, that the
response means match to the decimal, which fails for the DAT air puff mean,
and that the overlap recordings come from the same mice, as well as findings
with no output behind them, and these were corrected. Untracked files in the
repository root that the author did not create were left alone. The author's
points on the protocol: Methods and code that disagree where the code gives
the paper's numbers; a count claim that fails while other claims use its
selection; whether analysis parameters taken from the paper's code count as
inputs; `not_runnable` for software in R and no category for manual cell
counting; a 10% tolerance for a value near zero and for angles; a MATLAB
k-means seed that cannot be repeated; and selection counts and one session's
values seen before the criteria were written.
