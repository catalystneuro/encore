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

