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
