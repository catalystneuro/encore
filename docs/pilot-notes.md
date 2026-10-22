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

### 001075, Randi et al. 2023

Four claims reproduced, four partially and seven blocked on the dandiset.
With outside data, counted apart: one partially reproduced and one not
reproduced. Two claims on data in the paper's OSF repository: one reproduced
and one blocked. Round 1 gave its own outcome for each claim from the notebook
with its conclusions removed and agreed with 15 of the 19. It found that
`osf-link` passed on 87.4% agreement only because all 2,812 manually located
targets agree by construction, while targets found from the position, which
the claim states, agree in 1,101 of 1,667 (66.0%), and the author changed the
claim from reproduced to partially reproduced. Round 1 also asked for a check
of RID labels, which showed the earlier blocking notes wrong: the dandiset
labels 11 ROIs RID and 8 stimulations in 5 animals target one, and the unc-31
export labels RID in 28 stimulations in 8 of its 18 recordings, so the author
wrote criteria before computing any RID response and moved `fig4-rid-wt` from
blocked to partially reproduced and `fig4-rid-unc31` from blocked to
reproduced. The author kept `not_runnable` for `edfig6-kernel-stereotypy` and
`fig6-spontaneous`, where round 1 would have given `other` and `data_missing`,
and round 2 accepted both, the first with a reservation as no
reimplementation of the kernel fits was tried. Round 2 agreed with all 19 and
nothing was proposed, so there was no third round. The paper builds a signal
propagation atlas of the C. elegans head by stimulating single neurons in 113
WT-background animals during whole-brain calcium imaging, and compares the
measured functional connections with the connectome, with a
connectome-constrained model and with unc-31 mutants, screening for
extrasynaptic-dependent propagation. The recording protocol, the pair counts, the three
example responses of Fig. 1, spatial specificity, the link to the paper's
Source Data and OSF export, the inhibitory fraction and the RID responses were
tested. Every claim that needs q values is blocked as `data_missing`, as they
rest on unstimulated control recordings that are public nowhere, and so is the
model comparison, whose predictions are not public. Some outcomes rest on weak
ground: `fig1f-aver-avar` rests on 7 trials (Wilcoxon p = 0.22);
`fig1g-saadl-ollr` on 5 trials (p = 0.44), and the code's decaying correction
flips its sign to +0.014; and `fig4-rid-unc31` is met barely, with URX 0.031
in unc-31 against 0.032 from a single WT trial and Mann-Whitney p of 0.31 or
higher. The author used the open access full text (PMC10632145) with its
Source Data, and took the head neurons, the response classifier and other
parameters from the paper's code.

The dandiset was converted by CatalystNeuro (catalystneuro/leifer_lab_to_nwb).
The unc-31 recordings, the spontaneous recordings of Fig. 6 and the
unstimulated control recordings are not in the dandiset, and the controls,
which every q value in the paper needs, are not on OSF either, so the paper's
central statistics cannot be recomputed. For about half of the stimulations
the files give only a target position, not the stimulated ROI; the paper's
assignment uses tracking matches that are not in the dandiset, and from the
position 66% of these stimulations get the paper's ROI. The paper's export
marks 950 stimulations as excluded, which the dandiset does not mark. Three of
the 113 subjects (20, 23, 33) have only the raw imaging file, without traces
or stimulation table. In five recordings the labels reached through
`neuropal_ids` and the NeuroPAL table differ from the export for every named
ROI: subjects 64, 76 and 77 have almost no labels (4, 0 and 15 distinct names
against 70, 102 and 87 exported), and in 86 and 91 most names are shared but
sit on other ROIs; in subject 11 the ROI count (161) differs from the export
(200). The traces have unit "n.a." with no description of their processing,
and nine recordings hold values down to -196,646; 3,173 of 433,216 observation
rows have F0 at or below zero, and 897 of 14,039 traces cannot be corrected
for photobleaching with the paper's fit, though the variants without them
change no outcome. Even so, the inhibitory fraction of `fig2d` is 15.1% from
the dandiset against the 11.5% the Source Data means give for the same pairs,
and every variant gives 13.4% to 15.8%. Other findings: `neuropal_ids` holds
"merge" in 63 recordings and "check", "I4" or "RIAR" in others, and 49 ROIs in
21 recordings carry the label "target"; `depth_in_um` runs from -0.875 to
0.875, which cannot be micrometres in a volume imaged from 2.5 to 37.5 um, and
122 stimulations have the target position (0, 0); every stimulation is stored
as 0.5 s at 1.2 mW, constants written by the conversion, so the 0.1 to 0.5 s
AFD pulses of the Methods are not represented; the red channel is described
with the indicator GCaMP6s though it images tagRFP-T, two subjects have strain
"none", every age is P1D and one label confidence is 11; and thirteen
recordings last longer than the paper's "up to 40 min" (up to 48.7 min) and
three have timestamp gaps of up to 8.4 s.

The notebook ran in 404 s in the first clean run, 721 s after round 1 and
634 s after round 2. The paper's pumpprobe package would not install, and a
cell added after round 2 shows that it builds once the numpy headers are added
by hand but cannot be imported, as mistofrutta, wormbrain and wormdatamodel do
not build; OSF returned HTTP 429 for files fetched one at a time, so the
notebook streams a single tarball checked by its md5. Round 2 found statements
the outputs did not support, among them that every variant of
`sourcedata-link` falls in the partial band, which fails for the
detected-responses-only variant, and a deviation of `edfig2ij` that missed
reading (c); these were corrected, while counts differing by one between the
verifier's copy and the re-run were kept, with the Summary stating the
difference. The author's points on the protocol: no rule for the paper's own
published results such as Source Data q values and means; claims that need
data on OSF and data public nowhere, which the rule that elsewhere is never
`data_missing` does not fit; no guidance for an identifier that is absent but
can be inferred from the dandiset; whether a list of head neurons from the
paper's code is an input; a legend percentage that does not say which
neighbours it refers to; a default 10% tolerance meaningless for a count of
113 animals; block reasons resting on checks run outside the notebook; two
published versions with the same files, all re-uploaded; a clock check by
stimulated-neuron response rate in place of decoding; and no rule for outside
services that rate-limit.

### 001084, Vu et al. 2024

Ten claims reproduced, ten partially and one blocked on the dandiset, none
not reproduced. With outside data, counted apart: one reproduced. Four claims
on data in other archives are blocked. Round 1 gave its own outcome for each
claim from the notebook with its conclusions removed and agreed with all 26,
giving `data_missing` as the reason for the five blocked claims; the author
kept `other` (not attempted) for the four whose data are on Zenodo, and changed
`figs3-targeting-errors` to `data_missing` after a new data check showed that
no file's fiber table holds a planned target and the paper's code reads the
targets from calibration files in none of the Zenodo archives. After round 1
the author also added variants that rank AP and the response within each mouse
and permute within mice, under which the light amplitude gradient (r = 0.152,
p = 0.013) and the light and tone latency gradients (r = -0.223, p = 0.0014;
r = 0.214, p = 0.003) remain, and a refit of DL18 with its 14 tones of 12 kHz
identified from the paper's published results. Round 2 agreed with all 26 and
nothing was proposed, so there was no third round. The paper records D1 SPN
calcium and dopamine release through micro-fiber arrays across the mouse
striatum, and reports that light and tone evoke dopamine release with distinct
spatial patterns and latency gradients, and that stimulating dopamine axons
through one fiber evokes release at other sites that falls with distance. The
isosbestic control, the pairwise correlations and bundle cross-talk, the
chronic reward responses, the link to the paper's published GLM results on
Zenodo, the light and tone patterns and their consistency across mice and
against movement, the 415 nm control, the latencies and their gradients, and
the optogenetic counts, spread with distance and tdTomato and photoswitching
controls were tested. The histology, the freely moving recordings and the two
D1-cre jaw claims are blocked as `other`, as their data are on Zenodo and were
not tested in this attempt. Some outcomes rest on weak ground:
`fig5ab-response-latencies` is partially reproduced only because the Methods
count latency from the onset frame, while the code's count, one frame later,
gives the paper's means within 2 ms; `figs4eh-patterns-not-movement` fails
under the code's raw DF/F because of the level before onset in the
deceleration trials, and a baseline-subtracted variant holds the tone pattern
in both splits; `fig1d-chronic-reward-stability` can be tested only to week 8;
and in `fig4e-light-increases-widespread` the paper gives p < 1e-6 for its
significance test where the chance rate per fiber is 0.024, which the author
did not block on, since the raw averages are identical to the paper's and
significance agrees with its published calls for 93.6 to 94.5% of pairs. The
author used the NIH author manuscript in PubMed Central (PMC10957316), whose
supplement was blocked by a captcha, so the supplementary figure legends were
not read, and took method choices where the Methods are silent from the
paper's code on Zenodo (doi:10.5281/zenodo.10272874).

The dandiset was converted by CatalystNeuro (catalystneuro/howe-lab-to-nwb).
The 280 fibers of the 7 salient-stimulus mice are the paper's, and their raw
triggered averages equal the paper's published values (largest difference
0.0). The optogenetic sessions (Opto2, Opto4, Opto9, UG21) hold no stimulation
times and no record of which fiber was stimulated, and the trigger line the
paper's code uses is not in the files; both can be recovered only from the
laser artefact in the DF/F, which is unambiguous in Opto2 and UG21 but spreads
over many fibers in the tdTomato mice. The event table gives tones without
their frequency, so DL18's 44 tones cannot be reduced to the 14 at 12 kHz the
paper analysed, and the tone start times are the trigger times, 11 frames
before the sound according to the paper's code, which the dandiset does not
say. DL15's sessions from 2021-09-10 (44 to 70 rewards) were run in a ViRMEn
task whose variables are not in the files, so unpredicted rewards cannot be
separated and Figure 1D can be tested only to week 8. The FiberPhotometryTable
column `included` is described as "whether this fiber has been successfully
implanted", but it marks fibers within the striatum, and in Opto2 two fibers
labelled Caudoputamen are not included; with them the counts match the paper's
24 locations. UG21's indicator is given as tdTomato, while its 3 sessions, 22
included fibers and stimulated fibers 12, 18 and 24 match the paper's rDAm3.0
mouse without opsin. In DL31 and DL32 the fiber photometry series store a
regular rate, but the frame timestamps of the behaviour drift from it by up to
0.43 and 0.54 s over the session. The data of Figures 2, 3, 7, S1 and S5A-D
are not in the dandiset and are on Zenodo, and Opto9 has 12 sessions, so one
of the paper's 26 tdTomato stimulations is missing; the planned fiber targets
behind Figure S3 are neither in the dandiset nor on Zenodo. Other findings: the
paper gives p < 1e-6 for its test of a significant response, the value for
independent frames, while with the same test three given consecutive frames
are all outside the band at a rate of 0.0037; the paper's latency code divides
the 1-based index of the half-maximum frame by the frame rate, so its
latencies are one frame (33 ms) longer than the Methods' definition; its
cross-correlation of DF/F with locomotion does not shift negative lags; the
Figure 1C legend describes 23 example fibers of a 93-fiber array, while the
code plots 33 fibers of mouse 842, whose recording has 82 fibers; and the
archive's summary gives the approach as "cell population imaging" and lists
only NWB container types as variables measured.

The notebook ran in 827 s in the first clean run, in about 10 minutes in two
runs after round 1 and in 12.2 minutes after round 2. Zenodo returned "429 Too
Many Requests" during preparation, handled with retrying range requests, and
early runs failed on a column named `tail` that clashed with a pandas method,
windows running past the end of the recording and event placement in the
18 Hz sessions. Round 2 found sentences the outputs did not support, among
them that none of the 405 nm traces has frames above the threshold (11 of 61
have none), an exact match of the data to the paper's analysis claimed for
mice beyond the 7 where it was shown, and the README run time, and these were
corrected; a slip in the verifier's own round-1 reason for fig1d was left as
given and corrected in the round-2 entry. The author's points on the protocol:
no blocking reason for a claim on data elsewhere that could be tested but was
not attempted; a reported number that matches code disagreeing with the
Methods, where the rule for several readings and the rule for Methods against
code point different ways; no guidance for criteria on supplementary figures
whose legends are unavailable; whether the stated spread in the tolerance rule
includes an SD across fibers; facts seen only while preparing that matter but
may not supply numbers; a duplicate check that needs data from every file; and
a 10-minute runtime aim that the Methods' 10,000 null refits exceed.

### 001170, Ling et al. 2023

Two claims reproduced, four partially, four not reproduced and three blocked
on the dandiset. With outside data, counted apart: one reproduced. Five claims
on the locust recordings in the paper's Figshare record: three reproduced and
two partially reproduced. Round 1 gave its own outcome for each claim from the
notebook with its conclusions removed and agreed with 18 of the 19; it would
call `figs7e-ibi-chance` not reproduced, as the Methods' k = 50 classifier on
60 one-minute bins gives 3.8% and meets the criterion by construction while
k = 20 classifies the gaps between blocks at 73 to 95%. The author kept it
blocked as `methods_underspecified` under the chance-level rule, since that
procedure's own null averages 10.8% against the paper's 25%, and round 2
accepted this. Round 2 agreed with all 19 and nothing was proposed, so there
was no third round. The paper, a bioRxiv preprint later published in iScience
under a new title, compares mouse olfactory bulb glomeruli imaged with two
photons and locust recordings, and reports that ON and OFF responses point in
opposite directions and are anticorrelated, that the anticorrelation persists
after offset, that a preceding odor enhances contrast, and that the odor can
be decoded from activity in the intervals between trials. The session counts,
the link to the paper's deposited array, the ON-OFF angles, correlations,
reference-odor comparisons and clustering, the contrast of pairs ending in
methyl salicylate, the persistence after offset, the classifiers on the
intervals between trials and between blocks, and the random-order sessions
were tested on the dandiset. The acetophenone contrast panel and the
photoionization detector recordings of Figure S2 are blocked as
`data_missing`. Some outcomes rest on weak ground: `fig7j-iti-timebin-mouse`
and `fig7f-iti-knn-locust` are reproduced on the criterion only, as all trials
of one odor lie in one block, and in the mouse pseudo-trials within the 15 min
after each block, where no odor is given, are classified by the preceding
block at 69.6% to 96.9%, nearly as high as the intervals between trials; the
ON-OFF angles above 90 degrees of `fig2h-onoff-angle-mouse` and
`fig1g-onoff-angle-locust` follow from the code's centring, which makes the
mean ON and OFF vectors opposite (the two halves of one ON window come out at
101.1 and 96.0 degrees), and uncentred the mouse mean is 71.8; and in
`fig7h-iti-knn-mouse` k = 20 leaves only 9 of 39 other trials of the own odor,
so the null mean is 16.7%, while k = 5 gives 90.0% in sub-148 ses-3. The author used the full
text of preprint v2, whose Table S1 is an image and was not read, took the
session assignments from Table 1 of the published version (PMC13066794), and
took method choices from the paper's code on Figshare
(doi:10.6084/m9.figshare.31435543.v2) and the conversion code at commit
ac8f120.

The dandiset was converted by CatalystNeuro
(catalystneuro/reimer-arenkiel-lab-to-nwb). The fluorescence traces are raw F
(unit "n.a.") with no description of how they were extracted or of the
normalisation the paper applied, and the paper's deposited arrays are close to
F z-scored within each 57-s trial window. With that normalisation the contrast
enhancement and the negative correlations between the ON response and
activity from 5 s after offset appear, and they do not with dF/F relative to
the 2 s before each odor or with F z-scored on those 2 s; on synthetic
glomeruli with excitation only the whole-window z-score gives such
anticorrelations by itself, and the time-averaged ON and OFF vectors are not
anticorrelated with any normalisation tried (median r 0.068, 12 of 28 below
0). No sequential pair ends in acetophenone and no PID recordings are
included; the published version's Table 1 assigns the acetophenone panel to
the 73-, 210-, 153- and 198-glomerulus sessions, which in the dandiset hold
only pairs ending in methyl salicylate. The random-order session of Figure S8D
and S8E (286 glomeruli) is not in the dandiset, and of the eight random-order
sessions Table 1 lists only two (323 and 306) match a dandiset session by ROI
count. The dandiset holds the paper's seven block-protocol sessions from four
mice and five random-order sessions from five mice (four not in the block
sessions), apparently from a second study whose conference paper it also
names, and neither the metadata nor the description, which is that of the
second study, says which sessions belong to which paper. No identifier links
the paper's datasets to the sessions; they match by ROI count (198, 219, 318),
and session names in the paper's code (m149_3_1, m129_1_2) do not all exist in
the dandiset. The trials table has one undescribed row per second of valve
opening, so presentations, blocks and pairs have to be rebuilt from timing;
five block sessions fill the gaps with "Empty" rows and two do not, and the
concentration column has no unit, gives 0.0 to two odorants in three
random-order sessions and 0.1 to the Empty rows of sub-141 ses-5. In sub-134
ses-22, sub-141 ses-5 and sub-141 ses-8 the raw TwoPhotonSeries holds half the
frames of the fluorescence traces (91000 against 182000 in sub-134 ses-22) at
twice the frame interval. Other findings: the dandiset puts the 318-ROI
session under sub-148 with the 286-ROI session, while Table 1 puts it under
mouse 4 with the 219-glomerulus session; the files have 2-ethylphenol and
anisaldehyde where the Methods list 2-ethylpyrizine and isoamyl acetate,
"Anisole" and "anisole" are both used, and "2-methypyrazine" is misspelled;
the genotype (Thy1-GCaMP6f) and ages are not stated, every session starts at
00:00, and in sub-124 ses-3 the last trial ends 8.9 s after the last imaging
frame; the paper's code counts windows in frames at a nominal 16 per second
while the sessions are imaged at 13.7 to 17.8 Hz, so a nominal 57-s window
lasts 51.2 to 66.4 s, and in sub-141 ses-8 the deposited trial windows match
the dandiset only when counted in frames (r 0.968, against 0.307 in seconds);
the Methods give k = 50 for the classifier of Figure 7H, which has 40 vectors,
while the legend and code use k = 20; and the Figure 5E legend states a
one-tailed t-test where the code's is two-tailed (p = 0.011 against 0.0055).

The notebook ran in about 2.5 minutes in the first clean run,
`tools/entry.py all` took 2.0 minutes after round 1 and 183 s after round 2.
Figshare returned HTTP 500 to rapid downloads, handled with retries and md5
checks, and bioRxiv refused the preprint download to the round-1 verifier,
which read the published version. Round 1 also found that analysis windows
past the last frame were filled by linear extrapolation, which the author
fixed. Round 2 found statements the outputs did not support, among them that
the ON/OFF anticorrelation appears with the whole-window z-score, a window
drift of up to about 2 s, and a block-relabelling null for fig7j that repeats
the observed accuracy by construction, and these were corrected or removed.
Untracked files in the repository root that the author did not create were
left alone. The author's points on the protocol: a preprint later published
under a new title, with nothing saying which version is the target; code and
data in a Figshare record that neither the preprint nor the dandiset links; a
standalone link claim with no dependent claims; data from another species and
lab that the dandiset was never expected to hold; a criterion that passes
against the chance-level rule; no place for arrays the paper deposited as a
source for method choices; no rule for disclosing variants added after seeing
results; an SEM as tolerance, which becomes very tight; a 10% tolerance that
cannot apply to a count of 5; a clock check by shifted labels in a block
design; and a criterion that passes where the reading fails.

### 001172, Lohani et al. 2022

Thirteen claims reproduced, seven partially, one not reproduced and five
blocked on the dandiset. Round 1 gave its own outcome for each claim from the
notebook with its conclusions removed and agreed with all 26, but noted that
the wheel predictor of the Figure 2 regressions was signed speed while the
paper says locomotion speed. The author then made |speed| the main predictor,
under which wheel speed beats face PC1 in grabAM06 (0.147 against 0.142), and
lowered `fig2c-face-best-predictor-calcium` to partially reproduced. Round 2
agreed with 25 of the 26 and disputed that reason: the Methods define speed as
a differential of distance, which keeps the sign, and the paper's
`wheel_changepoints.m` uses a signed `db1SpeedMpS`. The author returned to
signed speed, added a comparison with the paper's own per-mouse R2 values in
`Fig2RawData.mat`, where the row matched to grabAM05 gives a calcium wheel R2
of 0.0246 against 0.0253 here with signed speed and 0.0483 with |speed|, and
proposed reproduced. A third round reviewed only that proposal and agreed, and
the claim is reproduced. The paper images ACh (ACh3.0) and calcium (jRCaMP1b)
together across the dorsal neocortex of awake mice, and reports that facial
movement and locomotion relate to both signals with opposite
anterior-posterior gradients, that transients and sustained states differ
across areas, and that correlations between areas and the coupling of ACh and
calcium change with behavioural state. The link to the paper's Allen parcel
masks, the regressions of Figure 2, the transients at face and locomotion
onsets, the sustained states, the correlations between areas and the
ACh-calcium coupling were tested. The ECoG, scopolamine, hemodynamic
correction, sensor validation and cholinergic axon claims are blocked as
`data_missing`. `fig5-coupling-down-frontal-with-locomotion` is not
reproduced: coupling is lower with locomotion in all 23 parcels but no parcel
decreases significantly at q = 0.01, and the largest decreases are in PTLp and
SSp-tr, not frontal cortex. Some outcomes rest on weak ground:
`allen-parcel-link` is partially reproduced under a per-session reading of its
mask criterion chosen after one movie was seen to fail it per movie (0.996
against 0.999), which would make it not reproduced; the claims of Figures 3 to
5 rest on 3 mice, and without grabAM06, which contributes 2 epochs per state,
the LSD p of `fig3c-ach-sustained-face` is 0.207 and the paired t p of
`fig3d-ach-frontal-above-visual` is 0.247; `fig3c-ach-locomotion-no-further-increase`
is an absence result where locomotion exceeds high face in all 3 mice; and
the ACh mean of `s7-face-onset-transients` is inside tolerance by 0.002. The
author used the author manuscript in PubMed Central (PMC10661869) and took the
parcel masks and the procedures the Methods leave open from the paper's code
at commit c337686.

The dandiset was converted by CatalystNeuro (catalystneuro/higley-lab-to-nwb).
It holds 4 of the 6 ACh3.0 and jRCaMP1b mice of the paper's code (grabAM05 to
grabAM08) and no ECoG, drug sessions, control mice or ChAT-GCaMP6s mice, so
five of the paper's findings cannot be tested. The ΔF/F series are given the
starting time of raw frame 0 while their frame 0 is raw frame 499, so their
times are 49.9 s early in every session. The FaceMap, pupil, eye and video
timestamps are spaced 111 ms where the camera pulses are 100 ms apart, span
about 10% longer than the session and end with two values equal to the first
camera pulse; with them face movement and wheel speed are misaligned by 23 to
60 s, and with frame i at camera pulse i, as the paper's code does, they
align. RoiResponseSeriesParcellated holds the calcium ΔF/F but its
segmentation is linked to the ACh imaging plane, its image masks are
transposed relative to the ΔF/F images, and its starting time is 64.9 s before
its first frame. The ΔF/F descriptions mention detrending only, while the blue
and green ΔF/F are also hemodynamically corrected and registered to the Allen
atlas, rotated by 180 degrees; the Allen parcels the paper analyses are not in
the files, and the parcellation that is there is a functional one with 89 to
107 ROIs per session and no area names. Other findings: in the VisualStimulus
tables the columns from `stimulus_size` on are shifted by one, and the tables
do not say where the monitor stood relative to the mouse; the air-puff session
grabAM07 11262019 has no Airpuff table, and no puff in the other tables (29
puffs) is followed by a locomotion onset within 5 s, which fits the code
keeping only puffs without running, a selection the files do not state;
WheelSpeed and pupil_area have the unit "unknown", and WheelSpeed is signed,
which its description does not say; and in the calcium ΔF/F of grabAM08
11232019 spont 263 pixels inside the brain mask, all in the right AUD parcel,
are zero in every frame.

The notebook ran in 716 s in the first clean run, 12.1 minutes after round 1,
17.1 minutes after round 2 and 1047 s after round 3. One development run
failed because the helper module was missing from the scratch directory, and a
request to delete an empty harness directory in the entry was denied. Round 2
also found statements the outputs did not support, among them that the tests
across mice lose significance without grabAM06, where calcium locomotion above
high face stays at p = 0.019 and the calcium sustained-state gradient becomes
significant (p = 0.037), a runtime of 13 minutes and a data size of 110 GB,
and these were corrected or removed. Untracked files in the repository root
that the author did not create were left alone. The author's points on the
protocol: a link criterion found ambiguous after the analysis, with no rule
for a link claim that fails on one movie when 21 claims depend on it; parcel
masks that name pixels but bring no measurements, which `with_labels` does not
exactly cover; signed-rank tests that cannot reach p < 0.05 with 4 mice; the
paper's uncertainty given as mean ± SEM; no rule for leaving out a session
whose event table is missing or for how few mice is too few; no rule for whose
timing convention to use once the file times are shown wrong; and a 10-minute
runtime aim the streamed data volume rules out.

### 001528, Hadjas et al. 2025

Twelve claims reproduced, five partially, three not reproduced and five
blocked on the dandiset. Round 1 gave its own outcome for each claim from the
notebook with its conclusions removed and agreed with 24 of the 25; it would
call `fig5-anxa1-dls-inhibited` not reproduced. The author kept it blocked as
`data_missing`, since at the deposited 5 and 4 mice three of its six Wilcoxon
tests cannot reach p < 0.05 and the paper's own W of -36 and -55 fix its n at
8 and 10, and round 2 accepted this. Round 2 agreed with all 25 and nothing was
proposed, so there was no third round. The paper, a bioRxiv preprint, reports
that STN and PPN inputs excite SNr GABA neurons and Vglut2+ dopamine neurons,
which are resilient in Parkinson's disease, while they inhibit dopamine release
in DLS and the DLS terminals of the vulnerable Anxa1+ neurons, and that
TH+/ANXA1+ neurons are reduced in human PD tissue. The group sizes, the SNr
GABA and pan-DA responses to train duration and frequency, the opposite TS and
DLS responses, the DLS rebound and 5 Hz increase, and the Vglut2 and Anxa1
terminal and cell-body responses were tested on the fiber photometry
recordings. The four human tissue claims are blocked as `data_missing`.
`cohort-sizes` is not reproduced (10 of 16 counts match, 11 with the Vglut2
STN count explained, against the 12 needed), `fig3g-da-ppn-duration` is not
reproduced (p 0.26, 0.25 and 0.46 under three readings, a Friedman 4.07 where
the paper gives F 11.5), and `fig4eh-dls-5hz-increase` is not reproduced on the
1 s trains its criterion fixed, while the 4 s panels the same sentence cites
would give partially reproduced. `fig3b-da-stn-250ms-peak` is partially
reproduced: the latency is 0.786 s in the window fixed beforehand, raised by
two mice with a slow rise past it, and a narrower window gives the paper's
0.492 ± 0.033 s. The author used the full text of preprint v1 and filled gaps
the Methods leave from the conversion repository's description of the lab's
MATLAB scripts, which are not public.

The dandiset was converted by CatalystNeuro (catalystneuro/hnasko-lab-to-nwb).
It has no published version, and the attempt used the draft as modified on
2026-09-01T15:27:47Z. For the Anxa1 mice it holds DLS terminal recordings for 5
(STN) and 4 (PPN) mice where the paper analyses 8 and 10. Nine mice have only
recordings labelled SNc, without a site suffix in the file name; their signals
resemble SNc recordings, and the paper's cell-body statistics are reproduced
closely by the other nine mice's SNc recordings (p to two digits, t within
0.08), so the DLS recordings of these nine mice appear not to be deposited, and
the dandiset does not say which SNc recordings the paper used. Every Anxa1 file
lists both an SNc and a DLS fiber, so the site rests on the name of the dF/F
series alone. Three Vglut2 PPN mice have no 5 Hz trains while the paper's
Friedman statistic of 24.8 needs at least 9 mice with all four frequencies, DA
terminals in DLS have 8 mice where Figure S3 gives 9, subject C4608 has no 4 s
trains, and the human counts and histology are not in the dandiset. The dF/F
series are stated in a.u. but hold percent, and a recomputation from the
stored signals agrees with a median correlation of 0.9999 (durations) and
0.9988 (frequencies). Other findings: every session start time carries the
offset -00:01, so the true offset is lost; the frequencies protocol's
description gives 10 s between trains where the epochs and the Methods give
20 s; the modulation frequencies are described inconsistently within the
files; thirteen mice have 10 trials per condition where the Methods state 5,
and 30 mice have 16 s trains the paper does not mention; eight subject ids are
lower case; the conversion code names a 5 mW block s1s10mW, and its Python dF/F
forces the fit through the origin while its description of the MATLAB scripts
includes an intercept; and in the paper the Figure 5 legend gives 10 Vglut2
STN mice where its Wilcoxon statistics are the exact values for 9, F1,11 =
12.8 is given for both STN and PPN with different p-values, two Friedman
entries do not fit their p-values, and the Figure 5 legend and the Results
disagree on the Anxa1 STN frequency effect.

The notebook ran in 290 s in the first clean run, about 5.5 minutes after
round 1 and 425 s after round 2. Loading first took about 10 minutes because
h5py serializes threads, and the author switched to a process pool; two bugs
found while preparing, timestamps stored in place of a sampling rate and
shifted onsets falling outside the recording, were fixed before the final run.
Round 2 found statements the outputs did not support, among them that
`fig5-anxa1-dls-inhibited` could not be tested by its criterion, where
partially reproduced was reachable and not reached (2 of 6), that the
cell-body statistics match exactly, and a runtime of five minutes, and these
were corrected. Untracked files in the repository root that the author did not
create were left alone. The author's points on the protocol: no published
version, where drafts are allowed only for repeat attempts; a 10% tolerance
that does not suit test statistics whose windows the paper does not state, nor
counts of animals; a block that depends on the selection where data are
missing, which the protocol would call `other`; site labels that the paper's
counts contradict and the signals support; a data check that ran into claim
territory; no recipe for a clock check on evoked photometry; a source
hierarchy that does not fit a conversion repository describing unpublished
analysis code; test choice after a Shapiro-Wilk test; and CatalystNeuro being
both the curator of the dandiset and the accountable party for the attempt.

### 001538, Zhai et al. 2025

Fifteen claims reproduced, three not reproduced and fifteen blocked on the
dandiset, none partially. With outside data, counted apart: one reproduced,
two partially reproduced and one not reproduced. Nine claims on the paper's
per-cell tables on Zenodo are reproduced. Round 1 gave its own outcome for
each claim from the notebook with its conclusions removed and agreed with 44
of the 45; it would call `fig1i-dspn-dendritic-sch-lower` not reproduced, as
its criterion defines only the reproduced case and P is 0.066, and the author
changed it from partially reproduced. The author also changed the reason for
the six spine blocks from `not_runnable` to `methods_underspecified`, as round
1 proposed. Round 2 agreed with all 45 and nothing was proposed, so there was
no third round. The paper reports, in a mouse model of levodopa-induced
dyskinesia, that dSPNs are more excitable in the on-state than in the
off-state and iSPNs less, at the soma and in dendrites, that evoked ACh
release is elevated in the off-state, that M1 receptors and CDGI underlie the
off-state rise in iSPN dendritic excitability, and that deleting CDGI or iSPN
M1 receptors attenuates dyskinesia. The links to the paper's tables, the
somatic and dendritic excitability of dSPNs and iSPNs with SCH 23390,
sulpiride, M1R antagonism, CDGI KO and M1R deletion, and two GRAB-ACh
comparisons were tested on the dandiset. The four Sr2+-oEPSC claims, three
GRAB-ACh claims and the two AIM claims are blocked as `other`, as the
dandiset holds so few cells, regions or mice that the paper's test cannot
reach P < 0.05 whatever the data, and the six spine claims are blocked as
`methods_underspecified`, as counting used AutoQuant, NeuronStudio or Imaris
with manual steps. `fig1i-dspn-dendritic-sch-lower` (P = 0.0662) and
`fig3f-ispn-dendritic-sul-no-change` (P = 0.0097, paper 0.0545) are not
reproduced, and each turns on one cell the dandiset holds only in part: with
the paper's value for that cell the paper's P is recovered (0.0133 and
0.0545). Some outcomes rest on weak ground: under the stricter basal-ratio
rule (0.8 to 1.25) `fig3f-ispn-dendritic-on-lower` gives P = 0.0774 and the
sulpiride claim P = 0.0663, which would reverse both; `fig5f-ach-off-elevated`
is met at P = 0.0357, the smallest attainable for 3 against 5 mice; and the
absence claims `fig3d-ispn-sul-no-change`, `fig5f-ach-off-like-6ohda` and
`fig9d-m1r-crispr-somatic-unchanged` pass with little power. The author used
the full text of the version of record in PubMed Central (PMC12674127), the
paper's per-cell tables on Zenodo (doi:10.5281/zenodo.17307059) and its
analysis scripts on Zenodo, read for method choices and not run.

The dandiset was converted by CatalystNeuro (catalystneuro/surmeier-lab-to-nwb).
It holds no patch-clamp recordings from unlesioned control or 6-OHDA-lesioned
mice (10, 12, 11 and 9 dSPNs; 21, 11, 14 and 9 iSPNs in the paper), nor the
oxo-M line scans of Figure 7E or the open-field data of Figure 10, though the
paper's raw data on Zenodo list folders for all of them. The Sr2+-oEPSC files
hold one cell per mouse (14 of the paper's 33 cells), the GRAB-ACh files one
region per mouse (11 of 34) and the AIM tables 7 of the paper's 44 mice plus
two mice (4124, 5871) not in the paper, and the dandiset does not say that it
holds a subset or how it was chosen. Session names state a drug (D1RaSch,
D2RaSul) for files that also hold baseline on-state sweeps; 11 cells in such
files have a baseline condition, 7 of them also recorded with the drug and 4
baseline only, and the condition of each sweep is only in the
RecordingsIndexTable column condition_subfolder. Two dendritic cells lack the
sites the paper's values need: dSPN on+SCH 20190411 cell 1 has only its second
pair of sites (0.584 against the paper's 0.228) and iSPN on+sul 20190508 cell
3 only a distal site; reading these gaps as missing data is an inference from
the recovered P values, as the paper does not list each cell's sites. Three dendritic site series hold
six trials, two sites under one name, and split they give the paper's values
for these cells; one series holds a single trial, one two and one four. The
genotypes of the CDGI behaviour mice contradict each other across the subject
metadata, the session names, the AIM table's genotype column and the video
files, and the AIM session totals of the five Figure 8 mice differ from the
paper's table in 20 of 25 sessions (mouse 1945 session 1, 33.5 against 27.0),
while the two Figure 10 mice agree in all sessions. The raw spine image stacks
and rotation videos are there, but no spine or rotation counts (none of the 86
spine files has a processing module or analysis entry). Other findings: the
stimulus series of every dendritic sweep is all zero, and the index table
gives no kymograph slice for 53 of 997 dendritic sweeps; the Sr2+-oEPSC
light-pulse OptogeneticSeries is all zero in 69 of 140 sweeps and the
intracellular recordings table references no stimulus; the GRAB-ACh
background images, described as taken at zero laser power, have a mean (381
to 525) above the signal (F0 179 to 355); the files cite the bioRxiv preprint
and use its figure numbers for the behaviour data; patch-clamp subjects are
named by recording date with no animal identifier, in 185 subject folders; 18
somatic cells miss one or more current steps between 20 and 300 pA and 14
repeat a step; and on the paper's own tables the oxo-M test in CDGI KO gives
P = 0.47 where the paper reports 0.910, and the rotation test of Figure 8A
0.012 where the text reports 0.0092.

The notebook ran in 248 s in the first clean run, about 10 minutes after round
1 and 640 s after round 2. No run failed; the author's first check for
kymograph slices missed references of -1, and the data check caught three
wrong sentences, all corrected before the final run. Round 2 found statements
the outputs did not support, among them mouse counts the wrong way round for
the Figure 8A rotations, 11 baseline-only cells where 4 are, a sentence that
the sulpiride outcome comes from one cell, which holds under the main
basal-ratio rule only, and a subject count and dendrite count no output
printed; these were corrected or printed. Untracked files in the repository
root that the author did not create were left alone. The author's points on
the protocol: no rule for a dandiset with so few units that the paper's test
cannot reach P < 0.05; no grading for a criterion that defines only
"reproduced"; no rule for raw data without the derived measurement, where the
spine and rotation choices are not fully consistent; whether `elsewhere`
claims may be tested on the paper's tables in place of its raw data; link
claims that gate nothing and only check whether the dandiset holds the
paper's cells; a data check that already showed group medians; clock-check
recipes that assume trial tables or continuous sessions, not sweeps; whether a
conclusion may cite the paper's reported values; and no finding kind for a
reported P that disagrees with the paper's own deposited table.

### 001550, Pagan et al. 2025

Eleven claims reproduced and two partially on the dandiset, none not
reproduced or blocked. With outside data, counted apart: two reproduced and
one not reproduced. Seven claims on the paper's neural data and RNNs in its
GitHub repositories: two reproduced, one not reproduced and four blocked.
Round 1 gave its own outcome for each claim from the notebook with its
conclusions removed and agreed with all 23, giving `other` as the reason for
the three blocks the author gave as `not_runnable`; the author kept
`not_runnable` and round 2 accepted it. Round 1 also found that the port of
`ExtDataFigure5ag.m` took the full-space angle, which the code computes first
and overwrites, and not the projected, folded angle the code plots; with the
plotted angle `choice-axes-parallel` went from a mean of 40.34 to 4.73
degrees, still outside 1.44 to 1.76, and its criterion was corrected after
round 1 and again after round 2. Round 2 agreed with all 23 and nothing was
proposed, so there was no third round. The paper studies rats that weigh
pulses by location or by frequency depending on a context that switches in
blocks, and reports that rats switch within about four trials, that their
differential behavioural kernels mostly converge with shapes that vary across
rats, and that behavioural and neural slope indices from FOF and mPFC are
anti-correlated across rats, as in RNNs engineered across the solution space.
The link to the paper's per-session tables, the subjects, trials, blocks and
durations, the 20 rats of Figure 1c and their context selection, switching
and learning times, the behavioural kernels and their half-split reliability,
bilateral FOF silencing, the link of the paper's units to dandiset sessions,
the unit counts, the neural slope indices, the choice axis angle and the
correlation of Figure 5d were tested. `fig1e-choice-axis` is blocked as
`methods_underspecified`, as `Figure1e.m` computes neither 81.3% nor 73.3%,
and the mTDR claim and the two RNN claims as `not_runnable`, as they need
MATLAB or 1,000 trained RNNs. `neural-link` is not reproduced: 2,371 of 3,495
cells (0.678) match one session as a contiguous run, from 110 sessions
against 199. Some outcomes rest on weak ground: `fig5d-behaviour-neural`
gives r = -0.697 against a tolerance of -0.803 to -0.657 and depends on P049
and P059, whose Methods selection keeps 23,014 and 25,847 trials; with those
two rats from the code's selection r = -0.834, and leaving out one rat at a
time gives -0.655 to -0.895, inside the tolerance for 4 of 7; in
`ed1e-switch-four-trials` the switch to location reaches 0.9 of its plateau
at position 4 in 0.678 of bootstrap resamples, while position 5 is firm; and
`trials-per-session`, `blocks-per-session` and `ed2g-learning-2-5-months`
match on two, two and three of four readings. The author used the full text
in PubMed Central (PMC11903320), took method choices from the paper's code at
commit 0ea8fdb and used its fitted per-neuron kernels without refitting them
from spikes.

The dandiset was converted by CatalystNeuro
(catalystneuro/pagan-lab-to-nwb). It holds only the
behaviour; the electrophysiology behind Figures 1d to 1f, 3h and 5d (3,495
units from 7 rats) is public only in the paper's GitHub repository, as one
MATLAB file per unit with binned spike counts, without raw data or spike
sorting output. Nothing links the units to dandiset sessions: matched by
trial sequence, 3,269 units fall in exactly one session when gaps are allowed
(2,371 without), from 112 sessions where the paper reports 199, and 226 match
none; searching every TaskSwitch protocol gives 3,349 units from 115
sessions, and 146 unmatched. The behaviour matches the paper's tables
closely: 15,277 of its 15,278 sessions with valid trials are in the
dandiset, and in the 14,650 with a per-trial record in the paper's tables
the 7,447,692 valid trials agree on every per-trial field, with 0.99996 of
50 ms pulse bins agreeing. The missing session, P189 TaskSwitch6-210516a with
27 valid trials, is listed in the conversion's notes among aborted sessions
left out, and six P187 and P189 sessions are in the dandiset but not in the
paper's tables, five of them passing the selection and adding 1,442 and 609
trials. Relative weights agree to 1e-6 in 0.898 of sessions, 861 more agree
once capped at 1, and 60 differ with both values present, not explained.
Every optogenetic epoch gives a wavelength of 473 nm, where Extended Data
Figure 4 says 450 nm and the conversion's documentation says the value was
corrected to 450, and epochs are present for four rats (P116, P124, P127,
P131) where the paper reports three, with nothing saying which three. The
dates of birth give ages of 3.0 to 39.1 months at the selected sessions (18
rats younger than 5.4 months at some), where the Methods state 6 to 24; they
put 25 rats at 1.6 to 2.7 months at their first session, and P189's
(2018-02-21) puts it at 14.1 months on the day P187, born 2019-02-21, starts,
and may be a year early. Other findings: thirteen task sessions (1 to 3
trials each) lack HistorySection_result_history or a pulse column, and 95 of
the other 15,400 lack HistorySection_hit_history; HistorySection_gammafreq_history,
a signed strength, is stored as uint8 or int16 in 570 files, with no values
lost; the paper's code requires a per-session `good` flag the Methods do not
describe and the dandiset does not hold, caps relative weights at 1, uses a
fixed penalty of 200 on neighbouring weight differences where the Methods
describe ridge regression with a cross-validated regulariser, and uses looser
selections (0.65 correct and 0.6 index) for Figure 5d and Extended Data
Figure 1e; the paper's own angle code on its own per-context kernels gives
1.1 to 8.0 degrees (mean 4.7), not 1.6, and the permutation test the Methods
describe is not in the code; the Methods put 3,495 units in FOF from 5 rats
while the FOF counts sum to 3,285; the main text calls a converging kernel a
slope index above 0, while the Methods and code give it a negative index, as
the data have; and three neural location slope indices are negative (P049
-0.221, P101 -0.045, P095 -0.007) where the Methods say only positive or zero.

The notebook ran in 642 s in the first clean run, 419 s after round 1 and 856
s after round 2. While preparing, listing assets with one URL call each took 8
minutes and was replaced by one paginated listing (4 s), partial remote reads
took 110 minutes because h5py serialises the reads, so each file was read
whole into memory, sessions lacking columns were skipped by the loader, and
the gh CLI had no token, so the repositories were cloned over HTTPS. Round 2
found statements the outputs did not support, among them a one to one link
with identical trial fields, relative weights equal to the paper's, P127 "not
lower" at 0.603 against 0.634, a README run time of about 7 minutes, and that
the Methods describe no test of the angle against 0, and these were
corrected. The author's points on the protocol: a paper repository that
duplicates the dandiset's behaviour, which the data kinds do not foresee;
fitted per-neuron kernels used in place of refitting the GLM from spikes; a
dependent claim that needs only the match of neurons to rats when its link
claim fails on sessions; a link criterion requiring contiguous trials that
proved too strict; the Methods' "ridge" read as the code's neighbour-difference
penalty; whether reading whole files into memory counts as streaming;
criteria written after the data check had shown the answer; whether
`not_runnable` covers MATLAB code that could in principle be ported; and which
value to record when several readings in two dimensions match.

### 001692, Bouabid et al. 2026

Eighteen claims reproduced, eight partially and three not reproduced on the
dandiset, none blocked. Four claims on the paper's Figure 8 slice data on
Zenodo: three reproduced and one blocked. Round 1 gave its own outcome for each
claim from the notebook with its conclusions removed and agreed with 32 of the
33; it would call `fig8e-cocaine-region` reproduced, as the notebook's Type II
sums of squares give a stimulus F of 47.68 for the unbalanced design (8 DLS and
5 NAcC slices) while Type III, as GraphPad Prism computes them, gives 36.37,
10.75 and 199.86, and the author changed it from partially reproduced. Round 2
agreed with all 33 and nothing was proposed, so there was no third round. The
paper, a bioRxiv preprint, records dopamine (rDA3m) and acetylcholine (ACh3.0)
with multi-fiber photometry across the mouse striatum, and reports an anterior
dorsolateral hotspot where the two signals are anticorrelated, with DA leading,
during spontaneous behaviour, unpredicted reward, Pavlovian cues and
extinction, locomotion initiation and invigoration, and in a stimulation
cohort, together with ex vivo slice experiments in Figure 8. The dominant
polarity and its hotspot, the controls with a mutant sensor and tdTomato, the
directionality and magnitude of paired transients, the reward, cue and
extinction correlations, the responses at locomotion initiation and their
latencies and topography, the invigoration GLM, and the DA release and ACh dips
after stimulation were tested on the dandiset, and the Figure 8 ANOVAs on the
paper's source data. `fig8c-cocaine-da-similar` is blocked as
`methods_underspecified`, as the legend's ANOVA has 8 degrees of freedom for
cocaine and 36 residual, which fits neither a two-level cocaine factor nor the
24 time points. `ed1-controls-no-organization` is not reproduced: the control
mice give a hotspot of 551 voxels with mean +0.33, larger than any of 100
shuffles, and a median absolute r of 0.238 against 0.240 in the sensor mice.
`fig5e-initiation-topography` is not reproduced, as dominant DA dips are more
anterior but more medial (ML 1.88 against 2.30 mm) and ACh-dip sites (148 of
174) are not more anterior or lateral (p = 0.33 and 0.25). Some outcomes rest
on weak ground: `fig4-cue-sequence` is not reproduced only by the wording of
its criterion, which counts only a shortfall as partial, as 58 of 75 sites lie
above the tolerance of 44.1 to 53.9 while the code's percentiles give 52; the
simplified hotspot procedure finds a hotspot in 67 of 100 shuffles of the
values across sites, though none as large as the real one (at most 482 voxels
against 1010); `fig1f-adls-hotspot` is partially reproduced because its
centroid is 0.02 mm medial of the median site; in `fig2-magnitude-correlations`
the second count (69, 3.9 below its bound) moves by several sites with the
random draws; `fig7f-ach-dip-in-out` is reproduced while the claim's second
part, the overlap of the ACh-minimum hotspot with the cohort hotspot, gives p =
0.065 and is treated as a variant; and the paper's 65 cue-responsive sites of
`fig4c-cue-correlation`, where all 75 respond here, remain unexplained. The
author used the full text of the preprint, the paper's Figure 8 source data on
Zenodo (doi:10.5281/zenodo.18202873) and its analysis code at commit 833fa3d,
read for method choices.

The dandiset was converted by CatalystNeuro (catalystneuro/howe-lab-to-nwb).
Every photometry series states a sampling rate of 9 Hz, while each has as many
samples as the behaviour series, which steps at 55.6 ms (18 Hz), and the
Methods and code use 18 Hz, so at the stated rate the recordings would last
twice as long as their timestamps. No field states which experiment or
Pavlovian phase a session belongs to; cohorts can be told only from subject
names and indicators, and phases only by counting rewarded light cues (1.0, 0.8
or 0.2), while the paper's Zenodo record has a table of this mapping. The
Pavlovian files have no tone cue events, although each session has 30 tone
cues, so tone trials cannot be analysed, and session sub-UG27_ses-240313r lacks
the high-pass, artifact-removed green series all other UG sessions hold. The
site counts match the paper exactly (174, 75 and 180). The ex vivo slice data
of Figure 8 are not in the dandiset, and in their source data the Figure 8b DLS
group holds 6 slice labels from 4 mouse labels where the legend states 5 slices
from 5 mice. Other findings: the description of ExcitationSource470 gives 470
nm and 405 nm light alternated at 100 Hz and that of ExcitationSource570 reads
"405 nm", where the Methods alternate 470 and 570 nm at 36 Hz; the mutant
sensor is named ACh4.3mut where the Methods name ACh3.0-mut; the session
description gives 9 uL rewards at 5 to 30 s where the Methods give 5 uL at 10
to 30 s, and stores the micro sign mis-encoded; the code's per-site `sig` flags
are not in the files, though all 174 included sites gave the paper's count; in
`fig4_pav.m` the session loop loads `exp_dirs{d}` in place of `task_dirs{d}`,
so it reads each mouse's first three recordings for every phase, and the
extinction correlation uses the DA peak where the legend and Methods describe
the trough; the code departs from the Methods in its significance percentiles
(0.5th and 99.5th against 2.5th and 97.5th), its minimum locomotion bout (2.2 s
against 2.27 s), its paired-transient magnitude correlations and its AND
exclusion for the stimulation cohort, which keeps 42% of the samples within 3 s
after a stimulation; and in the paper extinction is given as 41 of 74 sites in
the Results and 48 sites in 5 mice in the Figure 4g legend, while the files
hold 75 sites in 3 mice, and the learned-cue counts of 39 and 26 of 75 sum to
65.

The notebook ran in 9.7 minutes in the first clean run, with `tools/entry.py
all` taking 10 minutes, 12.8 minutes after round 1, and 7.7 and 8.7 minutes in
two runs after round 2. A first metadata scan of all 339 files took 29 minutes
because h5py serialises threads, and the helper was switched to processes; one
load failed on the missing series and constant red traces at some control sites
gave undefined correlations, both handled before the final run. bioRxiv blocked
curl and Europe PMC's full-text endpoint returned an error, so the author got
the PDF through the web-fetch tool. Round 1 also found that a NaN next to a
trough could hide it, which the author fixed (fig6a went from 99 sites and
182.4 ms to 98 and 188.8 ms), and asked for a chance-corrected pairing null and
a shuffle test of the hotspot procedure, which were added. Round 2 found
statements the outputs did not support, among them fig2d values kept from the
first run, a README run time of about fifteen minutes, and that the AND
exclusion keeps most stimulation responses, and these were corrected. Untracked
files in the repository root that the author did not create were left alone.
The author's points on the protocol: a count above the reported value, which
"partially reproduced" does not cover; a tolerance for means reported as mean ±
SD across sites; no rule whether to simplify or block a method too heavy for
the time limit; code with evident bugs; whether code read for parameters is an
input; whether to infer labels from the data or take them from outside the
dandiset; per-slice summary data classed as `data: elsewhere`; a clock check
for continuous sessions, where the contrast at locomotion initiations is weak
(ratio 1.28 for UG28); fitting the time limit by using 15 of the control mice's
114 sessions; and getting the paper when bioRxiv blocked downloads.

### 001699, Moore et al. 2025

Fourteen claims reproduced, seven partially, five not reproduced and one
blocked on the dandiset. Round 1 gave its own outcome for each claim from the
notebook with its conclusions removed and agreed with 24 of the 27; it would
call `fig1g-juvenile-halves-correlation`, `fig3g-adult-halves-correlation` and
`figs2j-adult-epochs-correlation` not reproduced, as neither of their two
values is within tolerance. The author applied that rule to all correlation
claims and changed fig3g and figs2j, but after fixes to spike counting and a
cut of every session to its first 20 min, the paper's session length, fig1g
gave a WT r of 0.815 against a bound of 0.81 and stayed partially reproduced.
In the same revision Isomap was fitted on every bin, as the criterion says, and
`fig2d-juvenile-isomap-wake-sharper` went from reproduced to not reproduced (p
= 0.056) and `fig2h-juvenile-isomap-rem-sharper` from not reproduced to
reproduced (p = 0.045). Round 2 agreed with all 27 but noted that the 20 min
cut departs from the claims file's session definition, which keeps blocks
whole and cuts only those over 30 min to 1300 s; under that definition fig1g
gives r = 0.761 and 0.839, neither within tolerance, the author proposed not
reproduced, and a third round reviewed only that proposal and agreed. The
paper, a bioRxiv preprint, records head-direction cells in the postsubiculum
(PoSub) of juvenile and adult Fmr1-/y and WT rats, and reports that juvenile
Fmr1-/y cells have higher HD information, also against the Isomap angle of
waking and REM sleep activity, and drift less relative to the room, while in
adults tuning does not differ and Fmr1-/y tuning curves drift more within and
between sessions. The unit counts, behaviour, cell metrics, HD tuning, its
stability between halves and between sessions, the drift of tuning curves and
of a Bayesian decoder, and the Isomap tuning in waking and REM sleep were
tested. `figs1d-probe-in-posub` is blocked as `other`: all 36 files hold
histology images, but none marks the probe tract or PoSub, and judging them
needs an anatomist. Besides fig1g, `fig3g-adult-halves-correlation` (r = 0.804
and 0.748 against 0.94) and `figs2j-adult-epochs-correlation` (0.787 and 0.562
against 0.90 and 0.76) are not reproduced, `fig1j-juvenile-less-drift` gives
the paper's direction at t(10) = -1.91, p = 0.085, and fig2d gives p = 0.056.
Some outcomes rest on weak ground: the main grouping counts H3026, labelled WT,
as a juvenile Fmr1-/y rat and H3029, whose date of birth makes it an adult, as
a juvenile WT rat, chosen because it matches the paper's unit counts, and with
H3026 left out the HD information of `fig1ef-juvenile-sharper-tuning`, fig1h
and fig2h give p = 0.072, 0.068 and 0.095; fig2h is at the threshold, with p
= 0.16 on the first day alone; `fig1h-juvenile-smaller-offset` gives p = 0.060
for cells with half-width below 120 degrees; cells re-recorded on later days
are counted on each day, as the files give no probe depth per day; and the
active speed of `figs1c-juvenile-behaviour-similar` differs on the first day
alone (p = 0.034). The author used the full text of version 1 of the preprint,
which the dandiset links, and version 2's Methods only where version 1 leaves
a procedure out (the decoder and the speed smoothing); bioRxiv refused
downloads in round 2 and its revision, so the version-2 numbers in the notes
were not checked by a verifier.

The dandiset was converted by CatalystNeuro (Paul Adkisson-Floro of
CatalystNeuro is a contributor). The paper's unit counts (406 units in 7
juvenile WT rats, 372 in 5 juvenile Fmr1-/y rats, 543 in 6 adult WT rats) and
its range of 8 to 83 units per juvenile recording are matched exactly only if
H3026 and H3029 are regrouped as above; with the archive's labels the juvenile
groups have 5 WT and 4 Fmr1-/y rats, and the juvenile effects weaken (HD
information p = 0.23, offsets p = 0.17). The file of H4825 holds the recording
of H4824 (identical waveforms, unit and spike counts, and spike times up to
1248 s), with its spike and tracking times shifted piece by piece onto H4825's
epoch table and clipped at its end, where 131373 spikes share the last spike
time and 12970 tracking frames repeat a timestamp; H4825's own recording is not
in the dandiset, so the adult Fmr1-/y group has 5 rats and 440 units where the
paper has 6 and 507. The dates of birth of H3023 (2022-08-13) and H3026
(2022-09-13) are after their recordings in 2021, so the archive's asset
metadata give them negative ages (P-366D to P-344D), H3029 shares H4830's date
of birth, and no NWB file sets the subject's age. The units table holds only
spike times, mean waveforms, electrode group and sampling rate, with no cell
type, contamination or depth, so the paper's exclusion of cells recorded in
the part of PoSub already recorded on the previous day cannot be repeated. The
epochs and processing/tasks tables do not mark the exploration sessions
reliably: in H3001 200202 task epoch 1 is called wake but lasts 94 min without
tracking, in H3026 211003 epoch 1 spans 112 min of waking and sleep, in H3023
210813-1 epoch 2 runs from the end of the first session into the second, and
H4823 has a single epoch and no sleep task; every file's session description
mentions a cue rotation, and most files hold a third tracked session
(`wake_cue_rot`) that version 1 of the paper does not describe. Spikes and
tracking share a clock in 32 of 35 recordings, and in the other three the cells
are too weakly tuned to show it. Other findings: in H3015 210417 and H4823
221108 position is stated in centimetres but spans about 300 and 700 units, so
it is in pixels, and head direction runs from -pi to pi where the other files
use 0 to 2 pi; one unit of H3023 210812 has spike times out of order, and 22 of
the 24 juvenile files have one to three tracking frames whose timestamp does
not increase; the dandiset's `about` field lists "Fmr1 protein, rat" as an
anatomy term with the MeSH identifier of Fragile X Syndrome (D005600); the
paper's analysis code is not public, and the repository the dandiset links,
woodcode (commit 61ee178), is the lab's general library; and in the paper the
Methods exclude units with contamination scores "below 0.5", which would remove
1727 of 1761 units, the ranges of units per recording mix counts of all units
(8 to 83, maximum 114) with a count of putative excitatory units (minimum 30),
and version 2 gives the adult counts as 372 and 406 units in 6 rats each, the
juvenile numbers repeated.

The notebook ran in 154 to 162 s in the first clean run, 282 s after round 1,
about 13 minutes after round 2, which repeated every claim's main test under
both session definitions, and 789 s after round 3. The statsmodels mixed-model
fits failed to converge on several measures, one giving p = 1.0, and the author
replaced them with an exact profile-likelihood fit of the same model, which
matched statsmodels to 8 digits on a synthetic case. Round 1 also found that
frame counting on speed-filtered frames lost spikes (2.6% on synthetic data)
and that the decoder error was interpolated before unwrapping, and both were
fixed. Round 2 found statements the outputs did not support, among them
archive-label p values kept from round 1, a cause for the 279 decoded bins of
H3001 200201 that no output showed, and the 20 min cut presented as following
the paper, and these were corrected. Untracked files in the repository root
that the author did not create were left alone. The author's points on the
protocol: two preprint versions under one DOI; no rule for correlation values
outside tolerance; no rule for which grouping is the main one when the
archive's labels contradict the paper's own counts; counting each recording
once where a count claim matches only if the duplicate is counted; linked code
that is the lab's general library and not the paper's analysis; no rule for
claims of absence that rest on several tests; no blocking reason for images
that need expert judgement; and a contamination threshold in the Methods that
would remove almost every unit.

### 001878, Sun et al. 2021

Four claims reproduced and two partially on the dandiset, none not reproduced
or blocked. With outside data, counted apart: one reproduced and one partially
reproduced. Fourteen claims on the CalMS21 files on CaltechDATA: five
reproduced, three partially and six blocked. Round 1 gave its own outcome for
each claim from the notebook with its conclusions removed and agreed with all
22, but would give `data_missing` as the reason for blocking
`fig7-errors-at-transitions` and `fig11-annotator-similarity`; the author kept
`methods_underspecified`, since fig7 depends on the blocked baseline of
`table1-architectures` and fig11's matrix is a model output, named the missing
deposits as a second reason, and round 2 accepted this. Round 2 agreed with all
22 and nothing was proposed, so there was no third round. The target DOI
(10.22002/D1.1991) is the CaltechDATA record of the CalMS21 dataset, so the
author used the paper that describes it, a NeurIPS 2021 Datasets and
Benchmarks paper (arXiv:2104.02710v4), which presents pose and frame-level
behaviour annotations of a resident and an intruder mouse in three tasks, an
unlabeled set and baseline models. The keypoint format, the resident's coat
colour, the behaviour vocabulary, the video, contact during investigation and
mount, and pose errors when the mice are close or fast were tested on the
dandiset's one CalMS21 sequence, the link to CaltechDATA and the
confidence-based pose errors with CaltechDATA's scores, and the counts and
label fractions of Tables 5 to 7 and Figure 4B, the dataset size and the
difficulty of Task 3 behaviours on CaltechDATA. The six model benchmark claims
are blocked as `methods_underspecified`, as the baseline code the paper links
did not answer and the top entries' code is not linked. Both pose-error claims
are partially reproduced: errors are higher in the closest 10% of frames
(difference 0.115, interval 0.064 to 0.179, and confidence -0.091) but lower in
the fastest (difference -0.020, interval -0.033 to -0.008, and confidence
0.018), the reverse of the claim. `table5-task2-counts` is partially reproduced
on one count, 139,122 frames where Table 5 gives 139,112;
`table6-task1-label-fractions` because attack is 2.765009%, 0.000009 outside a
tolerance of half a unit of the last digit, and reproduced under the default
10%; and `table10-task3-difficulty` because the bout-length correlation is not
significant (0.321, p = 0.249; 0.607, p = 0.083). Some outcomes rest on weak
ground: `fig4b-task2-label-fractions` stays within 0.05 for annotator 1 attack
(3.2468% against 3.2) with up to 4 more attack frames, and the pose-error proxy
counts body lengths outside widened quartiles, which a hunched posture in mount
could also produce, though flagged close frames have lower confidence and eight
drawn at random show tracking errors by eye.

The dandiset was converted by CatalystNeuro (Heberto Mayorquin of CatalystNeuro
is a contributor). It has no published version, and the attempt used the draft
as modified on 2026-06-25T18:32:10Z. For CalMS21 it holds one sequence, the
Task 1 test sequence mouse071, out of 574 sequences on CaltechDATA, and its
description presents a collection of datasets without saying that only one
CalMS21 sequence is included or why this one was chosen. Its keypoints are
identical to CaltechDATA's and its labels agree on all 23,810 frames, but the
confidence field of all 14 pose series is present with all 333,340 values NaN,
where CaltechDATA's copy has them (0.03 to 0.98). The behaviour catalogue has
an empty definition for attack, investigation, mount and other; the two mice
are stored as one subject with strain C57BL/6, sex unknown and age P0D/, so the
intruder's strain (BALB/c) and the residents' sex are not recorded; the session
start time is a placeholder (2024-01-01T00:00); and `centroid_speed`, with the
bout columns that reduce it, is the speed of the midpoint of the two mice, which
its description does not make clear. Other findings: the video (184 MB) is a
re-encoding of CaltechDATA's (964 MB), with the same frame count, size and rate,
and the dandiset does not say so; the dandiset links the dataset DOI as
IsDerivedFrom but not the paper; on CaltechDATA the 574 sequences hold 450
distinct recordings, 93 of the 109 Task 3 test sequences are Task 1 training
recordings, five Task 1 test recordings (mouse071 among them) appear as six
Task 3 training sequences, and four Task 2 recordings are in the training set
of one of annotators 3 and 4 and the test set of the other, while the paper
treats each sequence as an independent observation and the CaltechDATA readme
says the sets are split by animal identity; the paper's datasheet says the raw
videos are not included, while Section 3.1 says the Task 1 videos are released,
and gives the licence as CC-BY-NC-SA, where CaltechDATA and the dandiset give
CC-BY 4.0; and the baseline code the paper links
(gitlab.aicrowd.com/aicrowd/research/mab-e/mab-e-baselines) is not reachable
and no archived copy was found.

The notebook ran in 180 s in the first clean run, 247 s after round 1 and 4.4
minutes after round 2. While preparing, PyAV could not open the video URL and
was given a remote file object, and HEAD requests to CaltechDATA's presigned
URLs returned 403, so the helper used GET. After round 2 the first two re-runs
failed when CaltechDATA handed out a signed URL that had already expired, and
the helper now waits for a fresh one. Round 2 found statements the outputs did
not support, among them that most flagged frames fall in mount, where mount
holds 304 of 657, and six Task 1 test recordings where there are five, and
these were corrected. Untracked files in the repository root that the author
did not create were left alone. The author's points on the protocol: a target
DOI that is a dataset and not a paper; no published version to pin; a dandiset
that is a partial copy of the paper's own deposit, tested as `elsewhere`; a
link rule that assumes outside labels mapped onto dandiset units; a default
10% tolerance too loose for counts and percentages of a deposited file, with no
rule for rounding against truncation; a dandiset lacking a variable a claim
needs, so the pose-error claim was split in two; no rule for choosing between
two block reasons; no repository or commit to record for unreachable code;
claims that are themselves data checks; a duplicate check written for the
dandiset and run on the outside data; and the paper's own numbers used in an
analysis.

### 001712, Davatolhagh et al. 2025

Three claims reproduced, two partially, two not reproduced and eleven blocked
on the dandiset. Round 1 had no attempt record and gave its own outcome for
each claim from the notebook with its conclusion cells and summary removed, and
agreed with all 18. Round 2 agreed with all 18 and nothing was proposed, so
there was no third round. The paper, a bioRxiv preprint, compares Nrxn1a
knockout and wild-type mice (8 against 11 mice, 10 sessions each) in the IBL
visual decision task with biased blocks, with widefield calcium imaging of
cortex and a linear encoding model, and reports that knockout mice shift their
choices less between blocks and adapt more slowly after a switch, and show
elevated cortical activity, higher correlations and variance, and a larger loss
of explained variance when movement predictors are shuffled. The psychometric
curve, the dependence of reaction time on contrast, the prior shift and
adaptation after block switches, the response to contralateral stimuli and the
encoding model's full cvR2 and movement contribution were tested on the one
session; the eleven claims that need mice of both genotypes are blocked as
`data_missing`. `fig1e-rt-contrast` is not reproduced (rho -0.053, p = 0.15),
while with reaction times above 0.15 s only the correlation is -0.226 (p =
0.00062) and 149 of 899 onsets fall at or before the stimulus.
`fig3b-contralateral-visual` is not reproduced because the criterion's peak
search found frame corners outside the brain; a masked variant puts the peaks
on opposite sides of the midline (p = 8.1e-15 and 1.6e-17) but does not show
the lateralization is visual, as paw speed, wheel velocity and motion energy
differ by stimulus side in the same window. `fig4c-full-cvr2` (0.471 against
0.486 to 0.660) and `fig4cd-movement-dominates` (movement drop 0.104 against
0.297 to 0.440) are partially reproduced on a design with the body camera's
video components only; with the side cameras added the full cvR2 is 0.574 and
0.525, within the range, and with folds that keep each trial's frames together
0.472 and 0.405, below it, and the paper's Results give 0.60 and 0.54 while its
Figure 4C legend says the trial time regressor was subtracted, under which
reading the values here are 0.123 and 0.133 (0.226 and 0.236 with all cameras).
Some outcomes rest on weak ground: in `fig2ef-block-adaptation` B sits at its
bound and tau is poorly determined (25.12 trials, SE 16.14, bootstrap interval
6.41 to 38.37), and in fig4cd, with folds by trial and the body camera only,
task exceeds movement over components (0.012 against -0.005), which the
criterion would count as not reproduced.

The dandiset was converted by CatalystNeuro
(catalystneuro/IBL-widefield-to-nwb). It holds one session of one mouse
(sub-FD-28), where the paper analyses 10 sessions from each of 11 wild-type and
8 Nrxn1a knockout mice, so eleven of the paper's findings, all comparisons
between genotypes, cannot be tested. The mouse's genotype is not given in the
NWB files, the dandiset metadata or the public IBL database (subject FD_28 has
an empty genotype list, from a query made by hand during the attempt); the
subject description is the paper's general description of the cross, and a
comment in the conversion script lists the session under knockout sessions,
next to a note that the list is a placeholder. Neither NWB file holds the
cortical landmarks or the registration to the Allen atlas that the conversion
code's documentation describes for the processed file, so no pixel can be
assigned to a cortical area, and the SVD spatial components cover the whole 540
x 640 frame with no brain mask, with large values at the corners in
stimulus-evoked maps. Both imaging planes give the indicator as GCaMP6f, where
the Methods and the file's keywords give GCaMP6s; the raw file's imaging planes
state an imaging rate of 15 Hz, where the timestamps give 31.2 Hz per channel
(32.03 ms intervals) and the Methods 30 Hz; and the dandiset's keywords and
description name "CNTNALP2", which is neither the gene of the paper and the
files (Nrxn1a) nor a correct spelling of Cntnap2. The wheel series state that
counter-clockwise is positive, but trials whose choice is labelled
counter_clockwise turn the wheel with negative velocity (95.5% of them 0.1 to
0.3 s after movement onset), while the choice labels agree with the rewards,
and the wheel movement onset is described as the first movement after the go
cue, but 151 of 899 onsets precede the go cue (by up to 0.18 s). Other
findings: the ROI motion energy series give the ROI position in pixels but not
the body part it covers; the dandiset has no published version; the paper's
analysis code is to be made public on publication, and the encoding code it
links (churchlandlab/chiCa) implements the model for single-cell data in
another task; and in the Figure 3 legend the correlation panel is labelled (E)
twice and (D) is missing, the correlation panel's legend says the KO minus WT
matrix shows reduced correlations where the Results say they are increased, and
the legend of panel C describes variance difference maps, as does panel E.

The notebook ran in 380 s in the first clean run, 6.6 minutes after round 1,
when a second notebook (`encoding_all_cameras.ipynb`) taking 21 minutes was
added for the side cameras, and 6.4 and 20.7 minutes after round 2. bioRxiv
returned rate limits for several minutes before the author got the PDF, refused
both verifiers and the first revision, and answered in the second revision,
whose full text confirmed the Figure 3 legend finding and gave reaction time as
the time to first movement without saying how that movement is detected. PyAV
could not open S3 URLs directly and the video was streamed through remfile, and
the author's first imaging clock check had no power and was replaced, while the
15 Hz rate, the wheel sign and the onsets before the go cue showed up only
during analysis and were added to the data check. Round 1's points led to
variants for fig1e, fig2ef, fig3b and the encoding model, none changing an
outcome, and the count of blocked claims in the README and a finding was
corrected from twelve to eleven. Round 2 found statements the outputs did not
support, among them the openalyx genotype result, a count of 17 sessions for 19
mice, where the IBL places its side-camera ROI, and "brain pixels" for a
brightness and margin mask, and these were labelled, removed or corrected.
Untracked files in the repository root that the author did not create were left
alone. The author's points on the protocol: no published version, where the
protocol allows a draft only for repeat attempts; a genotype that is unknown
while the paper reports values per group, so tolerances span both group means
and the schema takes a single value; outside data in a live database without a
pinned version; a time-shifted label check that fails where shifted windows
land in other lateralized task periods and block structure correlates labels
across trials; a criterion fixed in advance that hits an artefact; linked code
that does not implement the paper's analysis; and leaving out part of a model
for runtime, which the protocol does not cover.

### 001888, Hristova et al. 2025

Thirteen claims reproduced, nine partially, two not reproduced and ten blocked
on the dandiset. Round 1 had no attempt record and gave its own outcome for
each claim from the notebook with its conclusion cells and summary removed, and
agreed with all 34. It found that reading (i) of `figs5b-transition-percent`
judged an SWD initiated in NREM on the one epoch before it, where the
Supplementary Methods use the six epochs before, and that rule gives 22.93%
against 24.2 ± 2.42. The author corrected the criterion, recording that this
was done after the analysis had been seen, and changed the outcome from not
reproduced to reproduced (the first rule gave 36.31%); the reason for blocking
`fig2e-swd-delta-power` and `fig5a-het-more-nrem-swds` went from `other` to
`data_missing`, as the verifier gave. Round 2 agreed with all 34, including the
change, and nothing was proposed, so there was no third round. The paper, in
Epilepsia, records EEG and EMG from Grin2b+/- and wild-type rats, and reports
that Grin2b+/- rats have more spike-wave discharges (SWDs), mostly in wake and
at wake-NREM transitions, less REM sleep in fewer and longer bouts, less time
awake, higher NREM beta power and lower wake power, and that ethosuximide given
systemically or into the reticular thalamic nucleus reduces SWDs. The number,
duration, timing, sex dependence and spectrum of SWDs, the amount and bouts of
each sleep state, the state spectra, the states in which SWDs start and the
correlations of SWD time with sleep measures were tested; the western blots,
development measures, scorer validation and the four pharmacology claims are
blocked as `data_missing`, and fig2e and fig5a-het-more-nrem-swds because only
one wild-type rat has SWDs. `fig4b-nrem-beta` (Het beta lower by 0.078) and
`fig4c-wake-power` (Het higher on average, +0.081) are not reproduced. Some
outcomes rest on weak ground: `fig3d-rem-hourly` and `fig3g-rem-total` give p
= 0.048 and drop to p = 0.060 without GRIN2B-228, a Grin2b+/- rat with 1 SWD
per day, without which `fig5c-transition-swds` (13 of 13, p = 0.0095) and
`fig5def-no-other-correlations` would meet their criteria; and the wake
results depend on whole SWD epochs being taken out of wake, so that with the
stored scores the wake bout differences reverse and `fig5f-swd-wake-correlation`
gives R = -0.06 in place of -0.81.

The dandiset was converted by CatalystNeuro
(catalystneuro/gonzalez-sulser-lab-to-nwb). It holds 2 of the paper's 9
analysed wild-type rats (14 or 15 of its 15 Grin2b+/-), so genotype comparisons
rest on two wild-type rats, one of which (GRIN2B-238) has no SWDs, and it does
not say which of its rats the paper analysed; GRIN2B-132 has no genotype and
sex U, which the conversion repository marks as still to be confirmed by the
lab. The pharmacology and intrathalamic infusion recordings, western blots,
development measures and the visual scoring used to validate the scorer are
not in it, and the paper says raw data are available on request. The
processed tables are misdescribed: the `sleep_states` description gives code 4
for SWD epochs, but no file holds it; `swd_epoch_counts` holds the scorer's
flags (6 for an SWD epoch, 4 otherwise) and not counts, and the flags cover a
median of 51% (0 to 73%) of the epochs SWD events overlap, mostly the last
epoch of each SWD; in `seizure_totals_by_zt` the per-hour counts are in
`spike_wave_discharge` while the two count columns hold the day's total in the
first row; and `sleep_state_power_spectra`, described as a baseline-corrected
PSD, holds the scorer's mean log10 multitaper amplitude referenced to each
frequency's 5th percentile. The raw EEG and EMG are stored as unsigned 12-bit
codes with offset 0, so every channel reads about +8 mV of DC, and signal loss
is written as 32767, undocumented; 21 to 73% of 5-s epochs per rat in the
windows read contain such samples (73% for GRIN2B-238). The Methods exclude SWD
times from the sleep states while the lab's scorer replaces only the flagged
epochs, and the paper's wake results depend on this. Other findings: the
dandiset has no published version, and the attempt pinned the draft as
modified 2026-07-31 09:37 UTC; the assets summary counts 16 files and 16
subjects where the draft holds 17; the dandiset does not record which EEG and
EMG channels the lab chose by eye for scoring; the paper does not give its
band limits, Welch segment length, bout definition or transition rule, and
neither linked repository holds the statistics or figure code; and the Figure
5 legend gives statistics that contradict each other (NREM time T = -1.47 with
R = -0.13 and df = 13, which implies T = -0.47), while the Figure 3 legend
reports no net wake difference next to a genotype effect on hourly wake time
(F = 7.14, p = 0.014).

The notebook ran in 278 s in the first clean run and 246 s after round 2. The
author first opened only GRIN2B-132 and took genotypes from the conversion
repository, then switched to the genotypes in the other 16 files and to SWD
epochs taken from the events before reading any claim output, though a first
run had executed the claim cells; a bug in the SWD peak rule was fixed before
the conclusions were written and changed fig2d's outcome. Round 1's points led
to runs without GRIN2B-228, GRIN2B-238 and both for every genotype test, a
fitted mixed model that matched the split-plot ANOVA, and checks of spectral
coverage, the slope rejection and a cleaner channel, none changing an outcome
beyond figs5b. Round 2 found statements the outputs did not support, among
them that the paper's 59.97 min of SWDs does not fit the scorer's flags, which
give 60.2 min, and a run time of about six minutes, and these were corrected.
The author's points on the protocol: no published version, where the protocol
allows a draft only for repeat attempts; opening one file, which is not enough
to find metadata held across all files; whether criteria may be revised after a
run that executed the claim cells; Methods and the lab's code that disagree on
SWD epochs, where the data show the code's input is incomplete; no minimum group
size for blocking a claim; claims of no difference tested with two wild-type
rats; one claim spanning eight tests under a binary absence rule; a variant
that matches but cannot rescue a claim; trading fidelity to the Methods'
spectra for speed; and method choices the paper leaves undefined.

### 000005, Yu et al. 2016

Five claims reproduced, two not reproduced and one blocked on the dandiset,
none partially reproduced. Round 1 had no attempt record and gave its own
outcome for each claim from the notebook with its conclusions and summary
removed, and agreed with all 8 outcomes, but found the reason for blocking
`sensory-input-drives-fs`, `methods_underspecified`, wrong: the paper's public
page carries the legends of all 14 supplementary figures, where Supp. Figs. 6,
11 and 12 test the claim by comparing FS cells in control and ION-transected
mice. The author read the supplement, changed the reason to
`metadata_insufficient` and recorded a second amendment in the claims file
that left the criteria unchanged, as every outcome had been seen. Round 2
agreed with all 8 and nothing was proposed, so there was no third round. The
paper, "Layer 4 fast-spiking interneurons filter thalamocortical signals during
active somatosensation", records VPM units and L4 cells in mice locating
objects with their whiskers, and reports that VPM neurons and L4 FS
interneurons respond to touch and whisking while L4 excitatory neurons respond
mainly to touch, that FS interneurons suppress movement-related spiking in
excitatory neurons and so enhance their touch selectivity, and that thalamic
activity drives FS interneurons, whose movement-related activity comes from
sensory input and not from motor areas. The full text is not open access, so the claims were written
from the abstract and the eight figure titles, no number of the paper is
compared, and every method choice is made here. The touch and whisking
responses of VPM units, tagged FS cells and excitatory cells, the effect of
light in PV-Cre mice and of light at the site labelled VPM were tested;
`sensory-input-drives-fs` is blocked because no file marks the transected
mice. `exc-mainly-touch` is not reproduced (excitatory cells more
touch-selective than FS cells p = 0.074, than VPM units p = 0.090), and
`fs-enhance-touch-selectivity` is not reproduced (selectivity lower with light
in 2 of 6 cells, p = 0.953). Some outcomes rest on weak ground: exc-mainly-touch
passes without the mice flagged as lacking touch input (p = 0.024 and 0.038)
and with the 12 excitatory cells with at least 20 spikes in the touch windows
(p = 0.003 and 0.005), selections that favour the claim, and 8 of its 18
cells sit at selectivity 0 or 1; in fs-enhance-touch-selectivity three cells
sit at selectivity 0 without light on 0 to 13 spikes after touches;
`fs-suppress-movement-spiking` (6 of 7 cells, p = 0.016) gives 3 of 3, p =
0.125, without anm266945, which holds 4 of the cells; and the whisking test
marks 0.12 of VPM units with spikes moved to the next trial, about ten times
its nominal rate. Cell types are inferred from the data: FS cells as
VGAT-ChR2 cells spiking within 6 ms of isolated 5 ms light pulses, and
excitatory cells as untagged whole-cell cells with action potentials at least
0.6 ms wide.

No L4 file names the cell type of its neuron, so the cell types the paper
compares can only be inferred from light tagging and action potential width.
No file marks the mice whose infraorbital nerve was transected (9 VGAT-ChR2
mice in Supplementary Table 2), and the files hold no surgery or notes field,
which blocks the test of Figure 7 and means these cells may be mixed into any
analysis of control cells; 4 mice whose cells have no touch input are probably
among them. The optogenetic conditions are not described: `photo_stim_mode`
has an empty description and its labels do not map to one kind of light
(VPM-site pulse trains are labelled `5ms_pulse` in early files and `shift` in
later ones), `photo_stim_power` is NaN in every L4 file, and no file names the
opsin. The session description gives the wrong recording mode for 24 of 130 L4
files, all from PV-Cre mice, so that by the trace PV-Cre has 9 whole-cell and
39 juxtacellular cells where Supplementary Table 2 has 5 and 42. In the L4
files the trial table's `first_touch_time` is the trial start plus the true
first-touch latency divided by 1000, while in the VPM files it is correct. The
genotype is missing for the 6 VPM mice and for 3 L4 mice, and the 5
SOM-IRES-Cre x Ai32 mice are given as Ai32. Other findings: every L4 file gives
cortical layer 4 (depth 0.42 to 0.62 mm), though the paper's waveform analysis
includes L5 cells; the L4 trace is sampled at 10 kHz in files up to March 2015
and at 20 kHz from late August 2015 on, which only the timestamps state; 8
files name no principal whisker, and the VPM files give one principal whisker
per file though the session description says each unit has its own; the light
at the site labelled VPM in VGAT-ChR2 mice is given as 594 nm, and isolated
594 nm pulses at the site labelled vS1 evoke short-latency spikes in VGAT-ChR2
cells, wavelengths that may be worth checking; and neither the paper nor the
dandiset links analysis code, while the public supplement names the measures
but not their windows, bins or boundaries.

The notebook ran in about 205 s in the first clean run, with `tools/entry.py
all` passing in 219 s after round 1 and the notebook in 201 s after round 2.
Reading the files through h5py and remfile first took 20 minutes, and single
HTTP range requests with a process pool brought loading to about 2.5 minutes.
The whisking test fixed in the claims file, a Rayleigh test, marked 0.88 of
VPM units as modulated with spikes moved to the next trial, so it was replaced
after the first run by an occupancy-corrected test against a trial-shift null,
recorded as an amendment, with both versions shown. Round 1's points led to
reading Supplementary Table 1 at run time, a membrane-potential touch response
to flag mice without touch input, per-cell spike counts, behaviour with and
without light and the paper's r2 measure as a variant, none changing an
outcome, and touch windows crossing a trial boundary (7 of 66,206 touches) were
dropped. Round 2 found statements the outputs did not support, among them 80
other cells where there are 85, sampling-rate text that left out the 5.2 s
trials, ION-transected cells stated as being in both groups, and the
juxtacellular variant presented without its caveat, and these were corrected;
the metadata search was extended to every text value of each file, with no
match. Untracked files in the repository root that the author did not create
were left alone. The author's points on the protocol: an abstract-only paper,
which leaves the rules for expected values and tolerances nothing to work on;
the public figure titles used as a source beside the abstract; cell types
inferred from the data, where the protocol covers labels taken from outside
sources; a criterion's test that fails its own null control; a clock check for
single-cell sessions, where decoding a task variable does not fit; undocumented
optogenetics, tested where the data support the assumption and blocked
elsewhere; and runtime advice that was not enough to keep loading short.

## Protocol pilot-8 (2026-10-19): the paper's own words

A reviewer reading claims to check them found the statements hard to hold
against the paper: a statement is the author's paraphrase, and `source`
often named only a section ("Results, active/passive section"), so checking
a claim meant searching the paper for it. pilot-8 adds `quote`, the
sentence at `source` that states the finding, copied word for word, and asks
that `source` name a figure panel or a section and paragraph. The quote is
written only when the full text was read. The dashboard shows it, with its
source, at the top of each claim's explanation.

pilot-8 also adds `statistics`, the tests and intervals the paper reports
for each finding: the test, its statistic, the p-value as a number with
its relation when it is a bound, any correction, a confidence interval and
the sample. Only tests whose result is the finding are recorded; the
threshold used to count significant units or pairs is left out. The
pipeline finds claims by their p-values, and until now the p-value lived
only in the statement's wording, when at all, so it could not be listed or
compared. Stored as a number it also no longer has to be quoted: a p-value
written as a power of ten does not survive copying from the paper's text.
The dashboard lists them under the quote.

The claims of every attempt recorded so far were then brought up to
pilot-8 from each paper's full text (Europe PMC or PMC, bioRxiv, or the
publisher's open-access page), and every quote and recorded value was
checked against that text. Of 1,280 claims in 56 files, 465 have
statistics (958 entries), and the tightened sources replaced ordinal ones
("Results, first section") that often did not match the paper's own
sections. Six papers whose full text is not open (000005, 000006, 000061,
000582, 000691, 001754) were quoted from the abstract, figure titles and
public Extended Data legends where those state the finding. Three files
were left as they were because their full text could not be downloaded at
the time (000350, 000727, 001699). Thresholds used to count significant
units, cells, pairs or sessions were left out throughout, and a paper that
prints "P = 0" is recorded as 0.

The backfill showed two kinds of claim mixed together. Twenty-four were
not findings of the paper but the registry's own checks that the dandiset
is the data behind the paper's tables, source data, code or deposits (the
link claims of step 6). They now say `kind: link` and are counted apart:
the README table and the dashboard's totals are of the paper's findings
only, and the links have a line of their own. And a finding with no quote
gave no sign of whether the paper states it at all. Every finding now has
either a quote or an `inferred` note saying why the statement is the
author's reading, such as numbers that appear only in a supplementary
table. Abstract-only papers are quoted from the abstract where it states the
finding. Every claim must come from and pertain to its paper, so five
claims that the paper's open text does not state were dropped, with their
outcomes: four of 001754 taken from the dandiset's description, and one of
000691 read from the paper's code (its method is now written out in the
claim that referred to it).

The full texts of the nine remaining papers were obtained on 2026-10-20 as
PDFs (the six abstract-only papers with their supplements where they have
one, the Cell paper of 000350, and version 1 of the two preprints), and
their claims were quoted from them; the manuscript quotes of 000067 were
also checked against the publisher's PDF. Of the 1,280 claims, 24 are
links, 1,248 findings are quoted and 8 are inferred; 509 have statistics
(1,040 entries). The six papers first written from the abstract had their
method choices fixed by the author without the paper's Methods; reviewing
them against the full text found several criteria that test a different
measure from the paper's, which is taken up separately.

## Protocol pilot-9 (2026-10-20): the full text or nothing

Six attempts had their claims written from the paper's abstract, because
the full text was not open: 000005, 000006, 000061, 000582, 000691 and
001754 (both of its attempts). With no Methods to read, their authors chose
the measures themselves. Once the full texts were obtained, a review of
each file against them found that the statements mostly held, but that
several criteria tested a measure the paper does not use, and that each
paper had findings on the dandiset with no claim. Four of the five outcomes
of not reproduced among these attempts rested on such a measure: 001754's
flight-spatial-code (a shuffle test, where the paper compares spatial
information with preflight), 000006's pt-types-differ-in-timing, and
000005's exc-mainly-touch and fs-enhance-touch-selectivity. The fifth,
000061's aversive-direction-stronger, agrees with the paper's own result on
the units the attempt used, as its supplement shows.

These attempts are now marked `deprecated`, with the reason, in their
records. The records and entries stay as they were; the dashboard shows
them with the reason and counts none of their outcomes, and their README
rows have no counts. Each is queued to be run again: the new attempt
writes the claims file again from the full text, keeping a claim's id where
its finding is the same so that the outcomes can be compared.

Step 1 of the protocol now requires the full text, with the Methods and
any supplement the results rest on. An author who cannot read it stops
before writing claims and reports what is missing, so that the paper can be
supplied. Claims are never written from the abstract.

The same review showed where the guessed methods came from: step 7 let an
author fix a method choice the paper leaves open and judge the claim on it.
With only an abstract, nearly every choice was open, so the outcomes rested
on the author's choices. Step 7 now says that methods come from the paper,
never from the author: every part of a criterion's method is taken from the
Methods, legends, supplement or the paper's code, and the criterion says
which. A detail none of them fixes is recorded as such; if it could change
the outcome, every reading the paper allows is run, and the claim is
blocked as `methods_underspecified` when they disagree. The verifier now
checks that no method choice is the author's own.

## Protocol pilot-10 (2026-10-20): the reader and the author

An attempt is now made by two kinds of agent that see different things. A
reader reads the paper and writes the claims file, with every claim's method
taken from the paper and cited; a second reader checks it against the paper
and records the check in the file. Readers never see the dandiset's data. The
author then tests the claims on the dandiset without the paper: the claims
file is its only account of it, and it may not change a claim's statement,
expected values or criterion. When it needs something the claims file does
not give, it asks, in `questions/<dandiset>.yaml`, and a reader answers from
the paper. The verifiers, like the author, check the analysis against the
claims file.

This does three things. The criteria are fixed from the paper by an agent that
has not seen the data, which is close to registering them in advance. No
method can come from the agent that runs the analysis, which is the failure
pilot-9 was written against. And only the reader's runs need the paper, so
papers that are not open access can be used without putting them where every
run can read them: they are kept in a private repository,
catalystneuro/registry-papers, that only jobs in the `papers` environment can
read, from main, with a read-only key. The steps from a target to a merged
attempt, and the Pipeline page that shows where each target stands, are in
[pipeline.md](pipeline.md).

The paper store started with 181 papers: 151 fetched (Europe PMC, PubMed
Central, bioRxiv, eLife), 2 from arXiv, and 28 supplied by hand as PDFs,
with supplements where the results rest on them. Which papers it holds, and which are missing, is in
`papers/manifest.yaml`, without their text.

The same day, before any attempt ran under it, the author and the verifiers
were given the paper again. Hiding it was meant to let them run on a model
without verified status, and to stop the author from trying readings of a
method until one reproduced. The second is already covered by running every
reading the paper allows; the first is untried, and the author's work is the
part that most needs the strongest model. Without the paper, everything the
claims file left out (a figure, the reason for a step) would have become a
question and two more runs. The claims file still binds the author: it may not
change a claim, and a method detail the file lacks, even one it finds in the
paper, goes to a reader as a question, with the passage, while the attempt runs
every reading, that one among them. The verifiers check the analysis against
the claims file, and report where it misreads the paper.

### 001754, Knierim et al. 2000, third attempt

One claim reproduced, two partially, two not reproduced and five blocked on
the dandiset. The attempt replaces the deprecated 001754-knierim-2000-02,
whose claims were written from the abstract and figure titles; the claims file
was written again from the full text, so most criteria are new. It pins
version 0.260728.1352, the most recent published version, as the draft, which
holds a new conversion that fixes several findings, is unpublished and changed
after the second attempt read it; the three published versions hold the same
blobs, so the files are those the first attempt read. The author put five
questions to a reader, whose answers were written into the criteria; they
changed the reason for blocking `direction-selectivity` from `data_missing` to
`methods_underspecified` and changed no number. Round 1 gave its own outcome
for each claim from the notebook with its conclusion cells and summary removed
and agreed with all 10, but found that the check admitting the deposited maps
(reading M-a) for `fig3-stability-across-sessions` kept the better match when
two units chose one map, so it did not test the criterion's condition that the
pairing be one to one. Tested as the criterion states it, the pairing fails in
session 3, where four units are each tied to two maps, so M-a is not run and
fig3 moved from blocked to not reproduced (6 of 16 and 1 of 16 cells keep
their field on recomputed maps, where more than 8 are needed), and
`three-orthogonal-surfaces`, whose criterion follows it, moved with it. Round 2
agreed with all 10 and nothing was proposed, so there was no third round. The
paper, a two-page brief communication in Nature Neuroscience with no Methods
section, records hippocampal place cells of three rats on a three-dimensional
track, the Escher staircase, during the Neurolab Space Shuttle mission, and
reports that after an initial period they fired normally in flight, with
spatial information per spike not different from the same rats' preflight
cells, that on flight day 4 the cells of rats 1 and 2 showed abnormal
selectivity, that most of rat 3's fields were kept between two sessions, that
some cells were direction selective, and that the EEG showed normal theta and
ripples. The spatial information of each rat in flight against preflight, the
flight day 4 selectivity and the stability across sessions were tested.
`si-rat3-fd4-vs-preflight` is reproduced (p = 0.28 and 0.77, both means within
tolerance under the ES reading); `si-comparable-to-preflight` finds no
difference (p = 0.88 and 0.66) but its means (1.377 and 1.320) are above
tolerance, so it is partially reproduced; and `fd4-abnormal-selectivity` holds
for rat 2 (p = 0.00063 and 0.0015) and for rat 1 under neither reading (p =
0.077 and 0.36). `si-rat1-fd9-vs-preflight` is blocked as
`methods_underspecified` because its two preflight epochs disagree (p = 0.50
against ES, 0.0055 against MC, with flight higher) and the paper does not say
on which track rat 1's preflight cells were recorded, and `flight-spatial-code`
is blocked through it; it was not reproduced in the second attempt, which used a
shuffle test the paper does not use. `direction-selectivity` is blocked as
`methods_underspecified`, and `theta-normal` and `ripples-normal` as
`data_missing`. Some outcomes rest on weak ground: fd4-abnormal-selectivity
rests on Rat 2's flight day 4 maps, in a window where the position trace could
not be attributed to either rat (0 of 17 and 1 of 16 units), so the low
information may come from tracking and not firing; fig3 and
three-orthogonal-surfaces rest on unsmoothed recomputed maps with few spikes
per 4-pixel bin, on which reading (b) passes for 2, 1, 0 and 0 cells at
thresholds of 0.1 to 0.5; and the cell counts differ from the paper's (11 maps
or 16 units against 7, 38 against 24), so the reproduced and partial outcomes
come from cell sets that are not the paper's.

The dataset was converted by CatalystNeuro
(catalystneuro/mcnaughton2000-to-nwb). Most of its findings are still present
in the published version, and several are fixed or partly fixed in the
unpublished draft. The Rat1 and Rat2 files of each flight day hold one
tracker's trace over the whole session (98.6 to 98.8% of positions at shared
timestamps within 2 pixels), each presented as that rat's position; the trace
behaves as Rat2's position in Rat2's flight day 9 ES window (12 of 28 Rat2
units, 0 of 36 Rat1 units), and in its flight day 4 ES window whose position
it is is not established. Position is given only at spike times, so occupancy
cannot be computed from it, and the preflight files have no position at all.
The rate-map table says cell_number matches the cluster id on the same
tetrode, but the link exists for 98 of 211 flight unit-epochs and names the
best-matching map for 84, and every one of Rat3's 42 flight day 4 ES maps has
cell_number -1, so its session 2 and session 3 maps cannot be paired by cell.
The dandiset holds more active cells than the paper counts in most
comparisons, and the selection behind the paper's counts is not recorded. The
rate maps are smoothed (91% of the positive-rate bins of a well-matched map
hold no spike of the unit) with no stated kernel, use -999 for unvisited bins,
which the column description does not state, and count the lost position (0,
255) in one bin, up to 19% of a flight occupancy map. Other findings: six
groups of identical rate maps are stored in three files, some under different
tetrodes; the description reports normal theta, sharp waves and ripples, but
no file holds EEG; the description puts the preflight recordings on a flat
rectangular track, while the files hold ES and MC epochs, and the files'
experiment description puts baseline sessions on a rectangular track, where
the paper puts them in the sleeping pouch; spike times are resolved to 1 ms or
finer below 1000 s, 10 ms to 10000 s and 0.1 s beyond, which is not stated,
Rat1's flight day 4 file has two overlapping baseline epochs, and 1 to 14
spikes per file lie outside every epoch; the age is "/" for every subject and
the pixel scale and camera view are not described; Rat2's preflight and flight
units share no tetrode, so nothing confirms the preflight files are assigned
to the right rats; and position ends before two MC epochs end (41 s early in
Rat3's flight day 4 file, 7 s in Rat2's flight day 9 file).

The notebook ran in 84 s in the first clean run, 1.3 minutes after the
answers and 97 s after round 1. `entry.py check` failed on 14 errors in the two
earlier records until round 1's revision, after which it reported none. Round
2 found four sentences the printed numbers did not support, among them a p
value of the M-b variant given as below 1e-6 where only four decimals were
printed (it is 6.2e-07 and 2.5e-07) and a statement that the NASA record
OSD-968 lists no continuous position, which no output searched for, and these
were corrected. The author's points on the protocol: `entry.py check` requires
every claim of the current claims file to have an outcome in every record of
the entry, deprecated ones included; the repeat-attempt rule assumes the claims
file is kept and the dataset changed, where here the claims changed and the
pinned version is older than the one the second attempt read; the second
attempt's record no longer lists four of its outcomes, which were taken from
git history; and the instruction to pin a published version conflicts with the
repeat-attempt section's use of the draft.

### crcns-ret-1, Lefebvre et al. 2008

Three claims reproduced, two not reproduced and twenty-one blocked on the
data set, none partially reproduced. The data set is on CRCNS and has no
versions, so it is recorded as unversioned; the notebook checks the zip's MD5
against `checksums.md5` and lists each member's CRC-32. The author put one
question to a reader, which flickering-bar recording of a retina to use; the
paper does not say, so the claims file now names three readings (A, the first
vertical-bar recording; B, all vertical-bar recordings pooled; C, the
horizontal-bar recording where the retina has one, otherwise A), which the
first run had already used, and the answer changed the text of six claims and
no outcome. Round 1 gave its own outcome for each claim from the notebook with
its conclusion cells and summary removed and agreed with all 26, and asked for
the frame and onset search of 20080702_R4 to be run in the notebook. The search
showed that the stated frame lengths of two vertical-bar recordings are wrong,
and with the corrected frame the DKW bands overlap under reading B with the svd
separation, so `fig9d-rf-size-similar` separates in 17 of 18 combinations and
moved from not reproduced to blocked as `methods_underspecified`. Round 2
agreed with all 26, including the change, and nothing was proposed, so there
was no third round. The paper, "Gamma-Protocadherins regulate neuronal
survival but are dispensable for circuit formation in retina" in Development,
removes the Pcdh-gamma cluster from mouse retina with Chx10-Cre or
Pax6alpha-Cre, and reports from histology that the mutant retina is properly
laminated but its INL and IPL are thinned, with increased apoptosis, that
deleting Bax rescues the neurons that die, and that their processes reach the
appropriate IPL sublaminae, and from multielectrode recordings of retinal
ganglion cells that mutant cells have a similar variety of responses, similar
receptive field sizes and an unaltered threshold, with a slower time course, a
lower firing rate and a reduced gain. The 15 histology claims and the four on
flashing spots, flashes, moving bars and gratings are blocked as
`data_missing`; the cell counts and the six claims on the white-noise responses
were tested. `fig9-cell-counts` is not reproduced (200 mutant and 122 control
units against 115 and 143), and `fig9g-threshold-unaltered` is not reproduced
(36 of 36 combinations separate, with mutant thresholds higher).
`fig9e-slower-time-course` (36 of 36, mutant medians longer by 16.7 to 33.3
ms) and `fig9f-lower-firing-rate` (9 of 9, reading A median 3.82 against 9.02
Hz) are reproduced, and `fig9h-gain-reduced` is blocked as
`methods_underspecified` because the printed and continuous forms of the
nonlinearity disagree. `s3-receptive-field-surrounds` is reproduced under its
criterion, but null STAs meet the rule in 194 to 198 of 200 mutant and 119 to
121 of 122 control units, so the result is no evidence for or against
surrounds. Some outcomes rest on weak ground: fig9d rests on one borderline
combination and on the frame correction, and with the frames as deposited all
18 separate; among units with an STA peak above twice the null's (103 mutant,
107 control), fig9f and fig9g would be blocked, as no DKW band separates, so
their outcomes hold only on all units, as the claims file's header reads the
groups; and in fig9-cell-counts a threshold of STA strength between 1.5 and 2
could put the mutant count inside its tolerance, so the outcome rests on the
control count, which no reading can bring inside.

The data set holds only the white-noise recordings behind Figure 9D to 9H. The
histology of Figures 1 to 8 and Supplementary Figure 1, and the flashing-spot,
flash, moving-bar and grating recordings of Figure 9A to 9C, are not in it, and
the paper names no other deposit, so 19 of the 26 claims cannot be tested. It
holds 200 mutant and 122 control units (and 3 from a Bax -/- mutant), where the
paper's Figure 9 has 115 mutant and 143 control cells, and it does not say how
its units relate to the paper's, which were kept, or why the counts differ. 95
of the 122 control units are labelled "WT (chx10 het)", while the paper's
Figure 9 legend gives the controls as Pax6-Cre;Pcdh-gamma +/f-del or
Pcdh-gamma f-del/f-del without Cre. In the 8 recordings of 20080628_R4,
20080628_R6, 20080702_R1 and 20080702_R4, 82 of 86 spike trains are not in time
order: each runs to 1440 s and then holds a second segment between 720 and 780
s, though the stimulus runs to 1500 s, which is consistent with the last minute
stored with a 720 s offset in place of 1440 s. The frame lengths stated for the
vertical-bar recordings of 20080702_R1 and 20080702_R4 (16.6691 and 16.6653 ms)
are not those of the stimulus; rebuilt with the stated frame, the bars of
20080702_R4 give no STA above the null in any of its 12 units (median ratio
0.96), and with 16.6718 ms, the frame of every other bar recording, the median
ratio is 2.57 and 10 of the 12 units have peaks above twice the null's. 16
pairs of units share 70 to 100% of their spikes within 0.5 ms in every
recording of their retina (12 pairs in mutant retinas, 4 in a control retina),
most likely single neurons sorted twice, and the data set does not mark them.
The files do not give the age of the mice, the Pcdh-gamma allele (the paper's
Results say fcon3 and its Figure 9 legend f-del), the region recorded in the
Pax6-Cre retinas, whose periphery alone the paper used, or the cell type of the
units. Other findings: 97 of 200 mutant and 15 of 122 control units have an STA
peak less than twice the null's, and much of the fig9d difference comes from
them; all 5 retinas recorded with 8.3 um bars are mutant, and every control
retina was recorded with 16.6 um bars; and one checkerboard recording
(20080628_R5) has 1 or 2 spikes near 2 s out of order in 15 units.

The notebook ran in 277 s in the first clean run, 251 s after the answer,
about 8 minutes after round 1 and 500 s after round 2. Two string-escaping
errors in the author's notebook generator were fixed along the way. Round 1's
points led to a label-shuffle calibration of the bands (the binomial band
separates in 35% of shuffles, the bootstrap band in 37% and DKW in 0 of 1600),
counts of LN fits at the grid edge, a synthetic check of the LN fit, a table of
units per retina and example STAs; with the corrected frame the mutant count
above an STA ratio of 1.5 went from 126 to 138. Round 2 found statements the
outputs did not support, among them the README stating the misplaced last
minute as fact, a summary sentence saying the results hold with the 16.6 um
bars alone, which is false for fig9d, and grid-edge counts described as fits
at the top of the grid where both ends were counted, and these were corrected;
the author then added every claim's combinations under all three readings for
the frames as deposited, units with clear STAs and the 16.6 um bars alone.
Untracked files in the repository root that the author did not create were
left alone. The author's points on the protocol: "units with a flicker
response" in fig9-cell-counts is undefined; the protocol says how to count
recordings deposited twice but not units sorted twice; the criteria do not say
what to do when bands separate in both directions; a criterion can be met by
noise, with no rule for when its own null meets it; the clock check assumes
trial tables, which continuous white noise does not have; the schema has no
kind for disagreement between the paper and the data set's labels; and
`archives.md` asks for MD5s of the files read, where only the zip has one.

### 000005, Yu et al. 2016, second attempt

Five claims reproduced, nine partially, six not reproduced and thirteen
blocked on the dandiset. The attempt replaces the deprecated
000005-yu-2016-01, whose claims were written from the abstract and figure
titles; the claims file was written again from the full text, with its
supplement, so it has 33 claims where the earlier one had 8, and the eight
kept ids have new criteria. It pins the same version, 0.220126.1853, the only
published version, whose draft holds the same 148 assets. The author put
seven questions to a reader; the answers added readings to several criteria
and changed one outcome, `behavior-false-alarms`, from blocked to reproduced
(6 of 9 mice per session without the continuity correction, where the other
readings give 5, 4 and 5). Round 1 gave its own outcome for each claim from
the notebook with its conclusions and summary removed and agreed with 32 of
33. It disagreed on `fs-touch-response`, whose FS readings give different
outcomes (2 of 3 values within tolerance with the waveform boundary, 1 of 3
without it), and the claim moved from partially reproduced to blocked as
`methods_underspecified`. A seed check it asked for moved `auc-weak-strong`
from reproduced to not reproduced (reading b holds in 8 of 20 seeds) and
`auc-groups` from blocked to not reproduced, under a rule of the attempt's
own, recorded as a deviation, that a reading matches only when it matches
under most of 20 seeds. Round 2 agreed with all 33, including the changes,
and nothing was proposed, so there was no third round. The paper, "Layer 4
fast-spiking interneurons filter thalamocortical signals during active
somatosensation" in Nature Neuroscience, records VPM units with silicon
probes and L4 neurons by whole-cell and cell-attached recording in mice
locating a pole with their whiskers, and reports that VPM neurons and L4 FS
interneurons respond to touch and whisking while L4 excitatory neurons
respond mostly to touch, that thalamic photoinhibition hyperpolarizes
excitatory neurons and reduces FS firing, that ION transection removes touch
responses and reduces whisking responses, and that suppressing PV
interneurons raises excitatory firing during whisking, improves touch
detection for weakly responding neurons and makes most mice report touch
with the pole out of reach. The touch, whisking and phase responses of VPM
units, excitatory cells and FS cells, the effects of thalamic
photoinhibition and of PV suppression, the AUC claims and two behaviour
claims were tested. The depolarized recordings behind `exc-inhibition-timing`
and `exc-inhibition-whisking`, the thalamic multiunits of
`vpm-photoinhibition` and the histology of `rabies-vpm-input` are blocked as
`data_missing`, the seven ION-cut claims as `metadata_insufficient`, and
`thalamus-drives-fs` as `other`, because only 5 FS cells qualify and a
two-sided test of 5 cells cannot go below p = 0.0625. `exc-mainly-touch` is
not reproduced because the paper's test finds a difference (p = 9.1e-07)
where the paper found none (P = 0.20), `vpm-touch` because spikes per touch
average 0.403 against 0.6, `fs-vm-touch-whisking` because the touch latency
averages 1.88 ms against 4.0, and `exc-touch-spikes-enphr` because the light
raises spikes per touch from 0.339 to 0.448 (p = 0.044).
`fs-enhance-touch-selectivity` went from not reproduced to partially
reproduced: with the light whisking rates exceed nonwhisking rates, as the
paper reports, but they do in control trials too (p = 6.7e-06 to 0.00013,
paper P = 0.55). Some outcomes rest on weak ground: without the 8 cells of
the flagged mice, `exc-vm-touch-whisking` has its amplitude (5.54 mV) and
latency (4.97 ms) within tolerance; the latency rule on unsmoothed dVm/dt is
crossed by noise, 1 and 3 of 250 baseline samples, and by single-sample
transients at light onset (0.10 ms in `exc-thalamus-photoinhibition`); the
r2 > 0.25 rule of the two phase claims still passes for 16 of 29 VPM units
and 9 of 17 FS cells with spikes moved to the next trial; and excitatory
rates are 2 to 6 times the paper's, which drives the rate failures of
exc-mainly-touch, `fs-suppress-movement-spiking` and auc-groups.

All 11 findings of the earlier attempt are still present, as the dandiset is
unchanged. No file marks the 9 ION-transected mice, and the files hold no
surgery or notes field, so the ION-cut claims cannot be tested and their
cells sit in every control group; the 4 mice flagged here leave at most 7
candidates for the 9. No L4 file names the cell type of its neuron, so the
cell types the paper compares can only be inferred from light tagging,
waveforms and light inactivation, and 26 VGAT-ChR2 cells with fewer than 10
short pulses at any cortical site cannot be tagged and count as excitatory.
The dandiset lacks the 6 L4 excitatory neurons recorded with depolarizing
current (Fig. 3), the 17 thalamic multiunit recordings during
photoinhibition (Fig. 6b,c) and the rabies tracing histology (Supplementary
Fig. 10). The optogenetic conditions are not described: photo_stim_mode and
type have empty descriptions and the mode labels do not map to one kind of
light, photo_stim_power is NaN in every L4 file, and no file names the opsin.
The injected current has unit amperes and conversion 1e-6, but the test
pulse, -0.1 nA in the Methods, is stored as about -0.1, so the stored values
are in nA and the conversion is wrong by a factor of 1,000, and 17
cell-attached files of VGAT-ChR2 mice carry a constant stored current of
about 1.9 that no description explains. The session description gives the
wrong recording mode for 24 of 130 L4 files, all from PV-IRES-Cre mice, and
in the L4 files the trial table's first_touch_time is the trial start plus
the first-touch latency divided by 1000. The genotype is missing for the 6
VPM mice and 3 L4 mice, and the 5 SOM-IRES-Cre x Ai32 mice are given as
Ai32. Other findings: every L4 file gives cortical layer 4 (depth 0.42 to
0.62 mm); the L4 trace is sampled at 10 kHz (92 files) or 20 kHz (38
files), which only the timestamps state; 8 files name no principal whisker,
and the VPM files give one per file, though 11 of 20 units in files with
several tracked whiskers respond most to another whisker; the light at the
site labelled VPM in VGAT-ChR2 mice is given as 594 nm, and 594 nm pulses at
the site labelled vS1 drive 13 VGAT-ChR2 cells, so the wavelengths look
wrong; the pulse trains at the site labelled VPM run at 50 Hz in 12 of 33
files, where the Methods give 100 Hz; the no-lick trial type is spelled Nogo
in some files and NoGo in others; and neither the paper nor the dandiset
links analysis code.

The notebook ran in 281 s in the first clean run, 302 s after the answers
and 296 s after round 1. `entry.py check`, and so `entry.py all`, failed
throughout on 25 errors, all in the deprecated record, which has no outcomes
for the new claims and must stay as it is; the new record had none, and the
notebook was run with `entry.py run`. Round 1's points led to a tag test that
counts every pulse of the 5 and 10 Hz trains (it drives the same 24 cells),
the whisking readings applied to every claim that uses them, the held trials
of the PV-ChR2 cell left out, checks of spike detection, the near-zero
latencies, the injected current and the pole times, and a cross-tab of mice
by VPM fibre site. Round 2 found statements the outputs did not support,
among them that the thalamic latency is still not the longer one past the
onset transient, which rested on thresholds that differ between the two
averages, three mice described as lacking touch input that each have a cell
with spike touch input, and a measured whisking change of 0.87 mV that was
the best of 16 readings, and these were corrected; the author then put three
questions on the claims file to a reader, on one-sample latency crossings,
on a criterion that passes under one reading, and on a chance level for the
r2 rule. The author's points on the protocol: `entry.py check` requires every
attempt of the entry, the deprecated one included, to have an outcome for
every claim, so `entry.py all` cannot pass; the findings schema cannot say
whether an earlier finding is fixed, and the earlier record cannot get a
`superseded_by` without being edited; and the repeat-attempt section assumes
a new version and a kept claims file, where here the version is the same and
the claims file was rewritten, so kept ids compare different tests.

### 000061, Girardeau et al. 2017, second attempt

Six claims reproduced, one partially, three not reproduced and twenty-two
blocked on the dandiset. The attempt replaces the deprecated
000061-girardeau-2017-01, whose claims were taken from the abstract alone; the
claims file was written again from the full text, its supplement and the
paper's code (buzsakilab/papers, GGirardeau-BLAHpcInteractions-Package), so it
has 32 claims where the earlier one had 6, and the six kept ids now use the
paper's own measures (EV/REV, the Poisson ripple-modulation test and
reactivation strength R). It pins the same version, 0.250624.0426, as no later
version has been published and the draft holds the same 40 assets. The author
put three questions to a reader; the answers confirmed lap reading c and the
identified cells for the firing-rate claims, and removed the dependencies of
three claims so their all-cell tests are judged alone, which moved
`direction-all-cell-pairs` from blocked to reproduced,
`reactivation-peaks-at-ripples` to partially reproduced (11 of 15 sessions,
one-tailed p = 0.0042) and `ripple-modulated-cells-larger-reactivation` to not
reproduced (p = 0.27 and 0.3). Round 1 gave its own outcome for each claim
from the notebook and agreed with all 32, but found that
`bla-rate-same-across-directions` misread its criterion: the all-cell test
already has p < 0.05 under both session readings (p = 0.022 and 0.0048), and
only O7 reading b, which needs position, keeps it from not reproduced, so its
reason changed from `metadata_insufficient` to `too_large` (round 1 gave
`other`). Round 2 agreed with all 32 and nothing was proposed, so there was no
third round. The paper, in Nature Neuroscience, records the hippocampus and
basolateral amygdala (BLA) of rats running a linear track with an air puff at
one location, and reports that joint hippocampus and BLA patterns of the run
are reactivated in later NREM sleep, peak at sharp-wave ripples, involve a
subgroup of BLA cells that fire more at ripples, and are stronger for the
aversive direction. The unit counts, habituation, BLA sleep firing rates,
all-pair reactivation, the central nuclei, the ripple rate and the all-cell
ripple and direction tests were tested. `unit-counts` is not reproduced (40
sessions and 4702 units against 61 and 7,390), and `bla-int-sleep-firing`
because the REM/wake ratio of the 36 identified inhibitory BLA units changes
(p = 0.020) and the NREM decrease has p = 0.26. Seventeen claims on putative
pyramidal cells, four of the ids kept from the earlier attempt among them,
are blocked as `metadata_insufficient`, and the four behaviour claims and
bla-rate-same-across-directions as `too_large`, as they need position from
about 222 hours of streaming video. Some outcomes rest on weak ground:
`bla-pyr-sleep-firing-increase` and bla-int-sleep-firing rest on 152 and 36
cells from one rat, against 675 and 175 from four; `cen-no-reactivation` (9
and 8 sessions against 19) and `ripple-rate-unchanged` (23 against 41) hold
only on the paper's p threshold, the bootstrap interval of the central nuclei
NREM median (-2.4 to 4.1%) including the hippocampus-BLA median of 1.96%; and
in direction-all-cell-pairs the reward-to-reward laps hold platform time and
stops, and with each lap cut to its last 10 s the safe test misses p < 0.05 (p
= 0.052), while the air puff result rests mostly on Rat08 (7 of 8 sessions).

The dataset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is a
contributor). The files are unchanged, so every finding of the earlier attempt
is still present except the missing methods, which the full text and the
paper's code now supply, though the dandiset still links no code. The
putative cell types the paper uses are not in the dandiset and there are no
spike waveforms; five of the 33 files with units (Rat08-20130709 to 20130713)
have a `cell_type` column, described only as "Type of cell this has been
classified as.", marking 152 excitatory and 36 inhibitory BLA units and 9
excitatory hippocampal units, consistent with the paper's monosynaptic
identification alone, and a cross-correlogram check supports this reading
(99.3% and 94.4% at p < 1e-6, against 44% and 7.9% of unclassified units).
The dandiset holds 40 recording days with 4702 units, where the paper reports
61 sessions with 7,390 units (2317, 515, 440 and 1430 units for Rat08 to
Rat11 against 2,444, 1,294, 1,138 and 2,514), and does not say which rat is
which of the paper's rats 1 to 4. The archive's asset metadata is wrong for
all 40 files: it lists ElectricalSeries for the 24 files that hold no raw
voltage and not for the 16 that do, and ProcessingModule for the 16 files
without a behavior module and not for the 24 with one. Still present from the
earlier attempt: the epochs table is stored in milliseconds although its
columns say seconds; video timestamps are in milliseconds and not on the
session clock (the first matches its epoch's start in 1 of 114 videos); in
ten files the spike_times_index is wrong at the first units, so units 0 and 1
were left out; seven files have no units table, sixteen no sleep states and
fourteen no ripple events, and the Rat09 files have no hippocampal units and
no ripples; there is no position tracking and no air puff location; unit
region labels are undescribed short codes, which the paper's Supplementary
Fig. 3 now lets this attempt read; the trials table of the Rat08 and Rat09
files is described only as "experimental trials" and its intervals are not
laps; and the ripple annotations carry an undescribed number in each label.

The notebook ran in 6.8 minutes in the first clean run, 454 s after the
answers and 10.2 minutes in the final run. `entry.py check`, and so
`entry.py all`, failed throughout on 29 errors, all in the deprecated record,
which has no outcomes for the new claims and must stay as it is, and the
notebook was run with `entry.py run`. A run in round 1 timed out after 60
minutes because the new listing of each file's groups walked whole files over
the network, and was limited and run again. Round 1's points led to effect
sizes, bootstrap intervals and power for the absence claims, a
cross-correlogram check of the `cell_type` column, a listing of every file's
groups, per-rat and left-out-unit tables and a BLA-only variant of the
all-pair test (4 of 5 sessions, p = 0.44). Round 2 found statements the
outputs did not support, among them streaming and run times that did not match
the printed outputs, a sentence saying the inhibitory cells differ from the paper's in
REM, which no test compares, and a power figure given as an exclusion bound,
and these were corrected; the author then added lap variants limiting
platform time to direction-all-cell-pairs and bla-rate-same-across-directions,
where the difference in rate disappears with each lap cut to its last 10 s (p
= 0.75 and 0.82). Untracked dotfiles that the author did not create were left
alone. The author's points on the protocol: `entry.py check` holds the
deprecated record to the current claims file, so `entry.py all` cannot pass;
the repeat-attempt section assumes the claims file is kept and the dandiset
changed, where here the dandiset is unchanged and the claims file was
rewritten, so no earlier finding could be fixed; and the rule for dependencies
blocks claims whose all-cell tests could run.

### 000582, Sargolini et al. 2006, second attempt

Five claims reproduced, one partially, three not reproduced and twelve blocked
on the dandiset. The attempt replaces the deprecated 000582-sargolini-2006-01,
whose claims were written from the abstract alone; the claims file was written
again from the full text and its Supporting Online Material (SOM), so it has 21
claims where the earlier one had 3, and the three kept ids (`layer2-grid`,
`deep-hd-conjunctive`, `speed`) now carry the paper's numbers and criteria. It
pins the same version, 0.251111.2151, the only published version, whose draft
holds the same 118 assets. The author put five questions to a reader; the
answers added readings to several criteria, among them both centres and both
radii of an autocorrelogram peak (56 grid readings where there had been 32),
and changed one outcome, `grid-phase-orientation`, from blocked to partially
reproduced. Round 1 gave its own outcome for each claim from the notebook with
its conclusion cells and summary removed and agreed with 18 of 21. It found
that partially reproduced is not an outcome the criterion of
grid-phase-orientation names, and the claims file blocks a claim that holds
under some readings and not others, so the claim moved back to blocked as
`methods_underspecified`. It would call `speed-slope-steeper` partially
reproduced and `speed-intercept` not reproduced; both stay blocked because
they depend on `speed`, which is blocked, and the protocol (Author, step 1.5)
blocks such a claim for the same reason. Round 2 agreed with 19 of 21, and
with the two dependent claims only if the protocol blocks them, which it could
not see, adding that `blocked_by: methods_underspecified` does not name the
dependency; nothing was proposed, so there was no third round. The paper,
"Conjunctive Representation of Position, Direction, and Velocity in Entorhinal
Cortex" in Science, records cells of layers II, III, V and VI of the medial
entorhinal cortex in 17 rats foraging in open enclosures, and reports that
grid cells occur in every layer and most in layer II, that head-direction
cells occur in layers III to VI and not in layer II, that many deeper grid
cells are conjunctive grid and head-direction cells, and that the rate of most
cells rises with running speed. The fractions of grid, head-direction and
conjunctive cells by layer, gridness, stability, phase and orientation,
directional tuning and rates, and the speed regressions were tested;
`spacing-dorsoventral` and `fieldsize-dorsoventral` are blocked as
`data_missing` because no file gives the recording sites' distance from the
postrhinal border, and `cue-rotation-coherent` because no file marks the
cue-rotation trials. Nine claims are blocked as `methods_underspecified`, seven
because their readings disagree and the two that depend on speed.
`hd-layers` is not reproduced because layer II has cells passing both
head-direction criteria (9, 7, 4 and 2 of 43), `deep-hd-conjunctive` because
layer II has conjunctive cells under all 112 readings (1 to 8), and `hd-rates`
because only 65.5% to 71.2% of head-direction cells peak between 4.5 and 44 Hz
where the criterion needs 90%. Some outcomes rest on weak ground: gridness
above 0, the paper's criterion, makes 277 to 329 of 614 cells grid cells
against 203 of 627, 0.297 of maps with spike trains shifted in time pass it,
and above the 95% or 99% point of the shifted gridness layer III is above
layer II, so the layer order behind layer2-grid's partial outcome does not
hold; the layer II cells that sink hd-layers and deep-hd-conjunctive all come
from two files of rat 11265 whose tracking looks normal; and in
`hd-stable-trials` the circular correlation falls to 0.538 and 0.645 under the
first-trial readings without sub-11025_ses-06050501, outside tolerance.

The dataset was converted by CatalystNeuro (Szonja Weigl of CatalystNeuro is a
contributor). The files are unchanged, so the five findings of the earlier
attempt were checked again: four are still present, and the missing methods
are partly fixed, as the SOM was supplied for this attempt, though the
dandiset states no analysis parameter and no analysis code is public. The
dandiset is described as a sample of the paper's data without saying how it
was selected; it holds 620 cell-sessions from 15 rats against the paper's 627
cells from 17, with 71 layer II cell-sessions against 108 while layers III, V
and VI hold slightly more than table S1A (227, 118 and 198 against 223, 110
and 186). No identifier links a cell across files: of 584 cell-sessions with a
depth there are 425 distinct (rat, depth, hemisphere, name), 99 of which
appear in 2 to 7 files. The positions are rescaled without saying so: in all
118 files they span exactly 100, 150 or 200 cm on the larger axis, and the 19
circular files spanning 200 cm are most likely the paper's 180 cm circle,
about 11% too large. No file gives the recording sites' distance from the
postrhinal border (`depth` is the depth the electrodes were lowered to, and
the electrodes table has one row per file, location "MEC", with no
coordinates), and no file names its enclosure, condition or the position of
the cue card. Every file says the enclosure was 1 x 1 m, but the positions
span 150 cm in 2 files and 200 cm in 20, and every file says position is given
for two LEDs, but 47 of 118 files have one, so head direction cannot be
computed for 167 of 620 cell-sessions. The 23 twenty-minute files hold two
10-minute trials joined near 600 s, with no trial table. Other findings: in
sub-11265_ses-09020601 and sub-11278_ses-31080502 the two LEDs are more than
15 cm apart in 71% and 62% of samples (median 36.0 and 22.7 cm, against 2.6 to
8.4 cm in the other 69 two-LED files and 7 cm in the paper), which nothing
flags; six cells have no layer, 36 no depth and 230 no hemisphere; the
experiment description says the sample holds conjunctive and head-direction
cells from layers III and V, and the dandiset description that it holds grid
cells, where the files hold cells of layers II, III, V and VI and of every
class; and the files do not say which LED is the red one the paper uses. Spikes
and positions share a clock, as both test measures peak at zero time shift for
29 and 28 of 30 cells.

The notebook ran in 375 s in the first clean run, 230 s after the answers,
461 s after round 1 and 328 s after round 2. `entry.py check`, and so
`entry.py all`, failed throughout on 18 errors, all in the deprecated record,
which has no outcomes for the new claims and must stay as it is, and the
notebook was run with `entry.py run`. Round 1's points led to a time-shifted
gridness control, four claims run with each (rat, depth, hemisphere, name)
counted once (after round 2, every tested claim but the two that depend on
speed), LED separation for every two-LED file, the speed sign test entering
the outcome (the split becoming 119 reproduced, 325 partially
reproduced and 4 not reproduced of 448 combinations) and a print of the
electrodes table, none changing an outcome beyond grid-phase-orientation.
Round 2 found statements the outputs did not support, among them that the
Kruskal-Wallis difference of `gridness-range-similar` lies among the deeper
layers, a count-once variant described as covering every claim, and a
deep-hd-conjunctive variant called partially reproduced on one chi-square
reading only, and these were corrected; two counts that rest on p-values near
0.05 differed between machines (90 and 98 here, 88 and 96 in the verifier's
run) with unchanged code, and the cause was not found. Untracked files in the
repository root that the author did not create were left alone. The author's
points on the protocol: `entry.py check` does not skip deprecated records, so
the kept `-01` record fails it; the findings schema has no field for whether an
earlier finding is fixed, and with no new version a repeat attempt can only
confirm the earlier findings again; the dependency rule blocks
speed-slope-steeper and speed-intercept although their analyses ran and agree
under every reading; and many criteria give 32 to 64 combinations of readings
that must all agree, which at the time blocked eight claims as
`methods_underspecified`.

### 000009, Guo et al. 2017

Seven claims reproduced, two partially, thirteen not reproduced and seventeen
blocked on the dandiset. It pins version 0.220126.1903, the only published
version, as the paper cites none. The author put six questions to a reader,
who did not have Supplementary Table 1; the answers made the computed spike
width (P1) the rule for unit classes, kept the files' labels (P2) as a reading
and added all units (P3) for the thalamic claims of Fig. 2 and 6, and allowed
both whole-cell photostimulus onsets the claims file names (E and M). This
moved four whole-cell claims from blocked and `selectivity-time-course` from
partially reproduced to reproduced. Round 1 gave its own outcome for each
claim from the notebook with its conclusion cells and summary removed and
agreed with 29 of 39. `task-performance` moved from partially reproduced to
not reproduced, as no reading puts percent correct, lick-early and
no-response rates within tolerance together. Round 1 also found that the
whole-cell files hold the laser trace in an OptogeneticSeries the loader never
read; its onset is now shown as reading L, with a seventh question to a
reader, and changes no outcome. For nine claims the author kept partially
reproduced where round 1 gave not reproduced. Round 2 agreed with 30 of 39 and
pointed out that none of the nine criteria has a partial clause; the author
proposed changing them, and a third round, which reviewed only those nine,
agreed with all of them, so they are not reproduced. The paper, "Maintenance
of persistent activity in a frontal thalamocortical loop", records units in
ALM, thalamus and SNr and whole-cell ALM neurons in mice performing a delayed
licking task with optogenetic photoinhibition, and reports that thalamus
photoinhibition reduces ALM activity to 6% of control and hyperpolarizes ALM
neurons by 18.7 mV, more than photoinhibition of M1 or contralateral ALM, and
that ALM photoinhibition reduces VM/VAL activity to 25% of control. The
behaviour, unit classes, selectivity, the effects and latencies of
photoinhibition in ALM, thalamus and SNr and the whole-cell claims were
tested. `fig3-alm-collapse` is partially reproduced (activity falls to 2.1 to
2.5% of control on 230 to 261 units against 314 +/- 31), and the unit-class,
selectivity and SNr claims are not reproduced mostly because the dandiset
holds fewer units than the paper, while the fractions often agree (P2
fractions 0.839 and 0.125 against 0.829 and 0.137). `wc-thalamus-hyperpolarization`
is not reproduced (-16.83 +/- 1.24 mV under M against -18.7 +/- 1.1), and
`fig6c-vmval-reduced` because VM/VAL activity falls to about half of control
where the paper gives 25%. Ten claims are blocked as `data_missing`, two as
`metadata_insufficient` and five as `methods_underspecified`, three of them
because their readings disagree and two because they rest on the
Supplementary Information. Some outcomes rest on weak ground:
`fig3-onset-latencies` passes under one reading of four, and its onset rule
reports an onset below 10 ms in 30 to 48% of simulated runs with no effect;
and in selectivity-time-course the VM/VAL increase holds in 3 of 12 VM/VAL
readings, all under P3.

The dandiset holds 966 of the paper's 1214 ALM units (47 of 57 sessions), 789
of 790 thalamic units (72 of 73 sessions) and 181 of 227 SNr units (18 of 23
sessions), apparently only the putative GABAergic ones, and the behaviour-only
sessions, the muscimol experiments, the 0.5 mW thalamus photoinhibition of
Fig. 5, the non-behaving whole-cell recordings with current injection, the M1
whole-cell recordings, the Olig3-cre recordings and the histology are not
deposited. Spikes are stored only from each trial's start to about 4.8 s after
pole onset, although trials last about 9 s, so rates over whole trials or
sessions cannot be computed. Most units hold spikes over only part of their
session (median 70% of its trials; 1358 of 1936 units below 90%) and the Units
table gives no observation interval. The mean waveforms are cut short (29 to
38 samples at 25 kHz), so widths above about 0.5 ms cannot be measured, and the
`cell_type` labels have no stated rule, though they give class sizes close to
the paper's. In the whole-cell files every photostimulus column of the trial
tables is empty and the laser time is held only in an OptogeneticSeries
described as 'no description', starting 1.40 s after pole onset in mouse
anm300476 and 1.47 s in the others. Thalamic units have no nucleus label, so
VM/VAL can be selected only by distance from a centre the paper does not give
in coordinates. Other findings: in the whole-cell file of cell_21_1 the trial
start and stop times are shifted by one row against the pole and cue times;
the Vm series state unit 'mV' with conversion 0.001, though the values are
already in mV; every electrode group carries the ALM coordinates, and the SNr
units of anm00261336 are placed at AP -1.56 mm, outside SNr; the 9 Gad2
thalamic sessions give the genotype 'Ai35D x GAD2_Cre' and mark no
photostimulus trial, though their 84 units match the optrode units of Extended
Data Fig. 2c; the VGAT-ChR2-EYFP thalamic sessions give 2.23 mW where the paper
gives 10 mW; unit_y has no stated reference, session_start_time is the
conversion date (2017-06-27) for every session and no sorter is named, so the
missing ALM sessions cannot be identified; photostimulation at galvo position
(0.5, 0.5) mm in mouse anm00264943 is not named; and the dandiset holds data
the paper does not describe, 21 ALM sessions of PV-Cre x Ai32 mice with
thalamic photostimulation at 10, 22.5 and 45 mW and 12 thalamic sessions of
C57BL6 mice without photostimulation.

The notebook ran in 330 s in the first clean run, 576 s after the answers,
about 11 minutes after round 1 and 669 s after round 3, and `entry.py check`
reported no errors. Round 1's points led to the laser trace being read, spike
windows past the stored spikes counted as missing, a check of the onset rule
on simulated data, the delay lengths and 100 ms bins of the VGAT thalamic
sessions, the SNr label reading set to 'Narrow width spiking', and Welch's
test for the depth bins. Round 2 found sentences the outputs did not support,
among them the README calling all 181 SNr units putative GABAergic and a group
count of 286 described as within 250 +/- 25, and these were corrected.
Untracked files in the repository root that the author did not create were
left alone. The author's points on the protocol: it gives no outcome rule when
the data contradict a claims-file convention; it does not say how the
author's own readings combine with each criterion's; criteria without a
partial clause do not say what counts short only because the dataset holds
fewer units are; it has no rule for missing per-unit observation intervals;
it does not say what `measured` holds when no reading matches; criteria can
block on trivial disagreement, such as 0-against-0 ties in bins of 1 to 4
neurons; questions of data interpretation cannot be answered from the paper;
and it does not say how to record a claim testable only in part.

### 000008, Scala et al. 2021

Eleven claims reproduced, four partially, one not reproduced and none blocked
on the dandiset, with nine more reproduced and two blocked that also use the
paper's data from outside the dandiset. It pins version 0.211014.0809, the
latest published version, as the paper cites none; version 0.211014.0808 has
the same 1,328 assets. The author put one question to a reader, on reading (b)
of `fig5d-sst-pvalb-calb2-firing`, where with 1,000 permutations the random
seed decided the result. The answer, which notes that the paper has no test
for Fig. 5d, made the p-value exact when there are at most 1,000,000 subsets
and otherwise estimated from 100,000, with the upper bound of the 95%
Clopper-Pearson interval also below 0.05, and the claim moved from blocked to
reproduced (p = 0.0485, bound 0.0499 with seed 55; exact p = 0.0497), though
with any of five other seeds (56 to 60) it would have stayed blocked. Round 1
gave its own outcome for each claim from the notebooks with their conclusions
and summaries removed and agreed with 32 of 35. It gave `cohort-cells-mice` as
reproduced, which the author accepted, as the three duplicated recordings
belong to six distinct cells; it gave `ed6-physiological-temperature` and
`fig4e-pvalb-axon-shape` as blocked for `data_missing`, where the author kept
`methods_underspecified` because their data are public elsewhere and the paper
gives no measure to test, which round 2 accepted. Round 2 agreed with all 35
and nothing was proposed, so there was no third round. The paper,
"Phenotypic variation of transcriptomic cell types in mouse motor cortex" in
Nature, records 1,329 neurons from 266 mice in primary motor cortex by
Patch-seq, with 29 electrophysiological features, a transcriptomic type
(t-type) and family for each cell and a morphology for 646, and reports that
many t-types vary in their features and that within some the variation
follows the transcriptomic landscape. The cohort, stimulus protocol, depths,
feature counts and family features, the family and t-type predictions, the
normalized variances and Leiden entropies, the distance correlations, the
reduced-rank regressions and the within-type gradients of Fig. 4 and 5 were
tested, those that need gene counts or reference data with the paper's code
repository and Zenodo record 5118962. `ed8-leiden-entropy` is not reproduced
(rho 0.266, one-sided p 0.061); `fig1a-ttype-coverage` is partially reproduced
because the one cell missing from the dandiset is the only L6 CT Gpr139 cell,
leaving 76 t-types against 77, and `fig1b-depth-layers` because L5 IT_4 has a
median depth of 0.757, in L6 (18 of 19 t-types agree). `fig4a-vip-tau` and
`fig5c-vip-mybpc1-rebound` are blocked as `methods_underspecified` because
their readings disagree. Some outcomes rest on weak ground: the fig5d outcome
depends on the seed; in `fig5b-ttype-variability` the share of t-types above
the band runs from 22% to 56% across k-means n_init and membership variants,
and 2 of the 8 variants fall below 25%; and ed8-leiden-entropy flips with the
membership handling (p = 0.061 under the Methods' handling, 0.031 under the
code's, both with duplicates removed).

All 1,328 cells of the dandiset match a row of the paper's metadata table, and
the table's 1,329th cell (20190211_sample_10) is not in the dandiset. Three
pairs of files hold identical voltage recordings although each pair is two
different cells of one mouse, with different depths and read counts, two of
the pairs from different slices and one pair with different t-types; the
paper's feature table has identical values for each pair, so the paper
analysed each recording twice, and which cell each recording belongs to is not
recorded. Three files hold other traces than the ones the paper's features
were computed from, one with 41 sweeps, while the features of 1,320 files
reproduce the published table on every feature but the rheobase, which the
paper fits with an unseeded random procedure. The field
cortical_thickness_4x holds the soma depth and cortical_thickness_um the
cortical thickness, both in 4x image units, soma_depth_um is empty in all 43
files that have it, and the paper's µm soma depths and cortical thicknesses
are not in the dandiset. Voltage series are labelled volts with conversion 1
but hold millivolts, and stimulus series are labelled amperes but hold
picoamperes. No series has a start time (starting_time is NaN in all 104,409
voltage series) and there are no timestamps, so the 1.3 or 1.4 s intervals
the Methods give are lost, and each file holds a single series of current
steps, where the Methods say the series was repeated for most neurons. Other
findings: the five cells with a t-type that the paper excludes are not marked
in the files, and the files use the older name PT for the ET subclass; the
hold time and cDNA yield of each cell are not in the files, so
`hold-time-yield` rests on the paper's table alone; 145 of 1,328 cells
(10.9%) do not start at -200 pA (90 start at -100 pA, and 87 of these end at
1,480 pA), and 112 go above 1,380 pA, up to 1,780 pA; one file
(20190625_sample_13) has voltages of about +-1,025 mV in some sweeps; one
mouse has the genotype Scnn1a-Tg3-Cre/wt; Ai9/wt, which the paper does not
list, and the paper counts 27 wild-type mice where the files have 26; and the
Extended Data Fig. 4 legend gives an AP threshold of -40.18 mV for the example
cell where the paper's feature table and the file give -43.18 mV, and the sag
time in ms where the value is in seconds.

The notebooks ran in 1,269 s, 1,066 s and 230 s in the first run and in 15.8
min, 16.1 min and about 5 minutes after round 2, and `entry.py check` reported
no errors. `glmnet_python` cannot be installed on Python 3.13, so
scikit-learn's estimator of the same objective was used and recorded as a
deviation, and `morph-reconstructions` is blocked as `data_unreadable`
because the Brain Image Library server timed out on every try, the last on
2026-10-21. After the author's final run they corrected a few lines of
conclusion text without running the notebooks again, checking that every code
cell was unchanged. Round 1's points led to the layer being taken from depth
with the Nissl boundaries as the claims file specifies (fig4b r = 0.339, p =
0.0113, where it was 0.347, p = 0.0094), an exact comparison with the metadata
table, a list of the files' metadata fields, a cross-tabulation of first and
largest current step, two library-size normalizations for fig5c reading (b),
the cross-validation folds of the reduced-rank regression and a second
question to a reader, on whether the allowance for the missing cell in fig1a
covers the t-type only that cell represents. Round 2 found statements the
outputs did not support, among them a voltage range of -150 to +80 mV that
nothing printed, exon sums said to be higher in most cells where only the
median ratio (1.035) is, and README labels that read as though 1,329 cells and
1,284 depths were reproduced, and these were corrected. Untracked files in the
repository root that the author did not create were left alone. The author's
points on the protocol: "count each recording once" gives no rule for which
cell of a duplicated pair to keep; exclusion flags taken from the paper's
table are neither `with_labels` nor `with_inputs`; it only implies that the
author edits other claims' `depends_on` when adding a link claim; it has no
outcome for a claim testable only in part; it has no block reason for an
archive that does not respond; streaming with `remfile` took about 6 s per
file, so whole files were read into memory; the 10-minute aim cannot be met
when each notebook must redo a 15-minute feature extraction; the substitute
for `glmnet_python` was recorded as a deviation, not a block; "scikit-learn
defaults" is ambiguous because the k-means default changed in 2024; and it
says a random seed cannot change an outcome, where in fig5d it does.

### 000010, Li et al. 2015

Eight claims reproduced, three partially, five not reproduced and eleven
blocked on the dandiset. It pins version 0.220126.1905, the only published
version, as the paper cites none. The author put seven questions to a reader;
the answers changed four outcomes. They made all trials (t1) and trials
without the tagging light (t2) readings of every electrophysiology claim of
Figs 2 and 3, either of which may decide, so `fig2c-population-dynamics` and
`fig3f-pt-contra-preferring` moved from blocked to reproduced; they named
three readings for picking out the antidromic spike, so `antidromic-latencies`
moved from blocked to partially reproduced; and they made all labelled cells a
substitute population, not a reading, so `fig4h-pt-contra-imaging` moved from
not reproduced to blocked as `metadata_insufficient`. Round 1 gave its own
outcome for each claim from the notebook with its conclusions and summary
removed and agreed with 25 of 27. `ed1-fast-spiking-properties` moved from
partially reproduced to not reproduced, as fast-spiking neurons have higher
baseline rates but are not less selective (0.750 selective against 0.733,
median absolute rate difference 1.46 against 0.62 spikes/s). The author kept
`imaging-selectivity-counts` as partially reproduced; round 2 agreed with 26
of 27 and gave it as not reproduced, since its criterion has no partial
clause and no reading puts all five values within tolerance (0 of 16). The
author proposed the change, and a third round, which reviewed only that
claim, agreed, so it is not reproduced. The paper, "A motor cortex circuit for
motor planning and movement" in Nature, records units in left ALM, with PT and
IT neurons tagged by antidromic photostimulation, and images ALM with two
photons in mice discriminating pole position with their whiskers in a delayed
licking task, and reports that photoinhibiting ALM in the delay epoch biases
licking to the ipsilateral side, that ALM neurons show preparatory and movement-related selectivity, that
contra-preferring neurons outnumber ipsi-preferring ones among PT neurons but
not among IT neurons, and that photostimulating PT neurons biases licking
contralaterally. The behaviour, unit classes and tagging counts, selectivity
and its time course, population dynamics, error trials, fast-spiking
properties, antidromic latencies, PT and IT selectivity and the imaging
counts were tested. `fig2d-preparatory-perimovement` is not reproduced
because 272 to 294 neurons are peri-movement only against 389,
`fig3f-pt-contra-selectivity` because PT selectivity never reaches P < 0.05
(P = 0.12 to 0.36), `fig4f-spatially-intermingled` because 57 of 64
combinations find clustering of same-preference cells at P < 0.05, and
imaging-selectivity-counts because the closest reading has 1,417 selective
cells against a lower limit of 1,417.5. The two photoinhibition claims of
Fig. 1, the six photoactivation claims and the anatomy claim are blocked as
`data_missing`, and `reaction-time` as `methods_underspecified`, because the
number of s.d. the paper does not give moves the mean across mice from 40.2
to 129.1 ms. Some outcomes rest on weak ground: `behaviour-performance` holds
only with the mean over sessions (early licks 11.6% against 14.3%, but 14.5%
pooled and 14.7% over mice); `fig2e-no-contra-bias-spikes` holds on the
paper's test as written (P = 0.82), but in the 570 ms before the go cue all
four tests give P = 0.022 to 0.050 with a contralateral excess, and the
criterion sets no rule for a claim of absence across its readings;
fig3f-pt-contra-preferring holds only with the light trials kept (30 of 45, P
= 0.010; 26 of 45, P = 0.14 without them) and only with light and no-light
trials pooled; and antidromic-latencies has all four measurable values within
tolerance in 1 of 18 combinations, in which keeping spikes within 0.5 ms of
the peak bounds the s.d.

The dandiset holds none of the photoinhibition (Figure 1) or photoactivation
(Figure 5, Extended Data Figures 3, 6 and 7) data and no histology, so nine of
the paper's findings cannot be tested, and the Ai32 mice that are in it have
no record of light; it holds 23 of the paper's 42 task mice. Every unit
labelled PT (45) or IT (27) is a second copy of a unit labelled Pyr in the
same file, with an identical spike train, so the 1,441 units are 1,369
distinct units. The 39 units of intermediate spike width that the paper
recorded and excluded are not in the dandiset, which does not say so, and the
activated neurons that failed the collision test (22 from the pons, 106 from
ALM) and the 7 that could not be tested carry no label. In 75 sessions the
antidromic tagging light was delivered during behavioural trials (4,332 of
14,388 correct trials in those sessions); the trial tables do not flag these
trials, which can be found only from the laser traces, whose series have the
description 'no description'. The laser power series are labelled 'watts' but
hold the milliwatts of the Methods (47.1 and 82 at the pulses). The
extracellular trial tables hold 1,540 trials with a lick instruction and no
behavioural events, 1,447 of them marked 'right', 'hit' and 'no early' and
lasting exactly 5.5 s, and 1,345 with no spike from any unit; they look like
placeholders for removed trials, would raise performance if taken as given,
and are not the photoactivation trials (1,502 are in the sessions with
tagging light and 7 in the Ai32 mouse 218693). The imaging files flag no
trial as an early lick, so early-lick trials cannot be excluded there, and no
imaging plane gives its depth, so the layer 5 populations of Figure 4g, h
cannot be selected (the files label 843 included cells IT against the paper's
542 in layer 5). Other findings: the imaging mice are given the genotype
'Rosa-lsl-tdtomato' (one) or none (three), where the Methods use C57Bl/6Crl
mice; the ROI labels include 'Pyr' and 'interneuron', which the paper does not
describe, and the `included` flag does not state its rule, with 424 included
ROIs not 5% brighter than their neuropil; the `lick_trace` series is not
described as the photodiode signal used for reaction times, and its level and
direction differ between sessions (median baselines 0.069 to 4.83 a.u.; it
falls after the go cue in 15 of 99 sessions); 66 extracellular trials without
an early lick have a go cue that is not 2.6 s after the sample event and 75
have none; spikes are stored almost only within 5.5 s trial windows, so
baselines before the trial cannot be measured in most sessions; and the paper
links no analysis code.

The notebook ran in 711 s in the first clean run, 665 s after the answers,
1,200 s after round 1 and 1,062 s after round 3, and `entry.py check`
reported no errors. After round 2 the first run failed on a dropped
connection to DANDI and the second passed. The author listed the groups of
only the first file at first and missed the laser traces of the 75 sessions,
which the extra analysis and slower streaming then came from. Round 1's
points led to a check that the tagging light is balanced between trial types
(0.295 of lick right and 0.307 of lick left correct trials), an F0 check of
the imaging baselines, a search of every text field of the 59 imaging files
for a depth, a breakdown of the placeholder trials by mouse and the timing
filter applied to the behaviour. Round 2 found statements the outputs did not
support, among them 4,332 light trials given as part of 18,385 correct
trials, spikes said to be stored only within trial windows where two sessions
have 24% and 30% between trials, a measured value for fig2e taken from a
reading where the absence test fails, and an untested explanation of the PT
result, and these were corrected. Untracked files in the repository root that
the author did not create were left alone. The author's points on the
protocol: it says to judge a claim of absence on the paper's test alone, yet
the fig2e criterion names readings; its rule that any matching reading
reproduces a claim and its rule that disagreeing readings block one leave
unclear how readings the author finds combine with those of the claims file;
it has no outcome for a claim part of whose data is absent; step 1.1 could
say to list every group in every file; and streaming the laser traces pushed
the run past the 10-minute aim.

### 000691, Scherrer et al. 2023, second attempt

Two claims reproduced, none partially, one not reproduced and fifteen blocked
on the dandiset; of five more claims on the bead and dye images in the paper's
code repository, three are reproduced, one partially and one blocked. The
attempt replaces the deprecated 000691-scherrer-2023-01, whose claims were
written from the abstract and public figure legends only; the claims file was
written again from the full text and the paper's code, so it has 23 claims,
nine of them new or restored, and several criteria that rested on the earlier
author's thresholds now use the paper's numbers. It pins the same version,
0.260827.1358, the only published version, whose draft holds the same files,
so every difference from `-01` comes from the claims file. The author put no
questions to a reader, and the answer run found no questions file, so nothing
changed. Round 1 gave its own outcome for 22 of the 23 claims from the
notebooks with their conclusion cells and summaries removed (none for
`ed3-adc`) and agreed with 20 of them; it gave reproduced for
`fig2-quadrant-direction-decoding` and `ed9b-octant-decoding`, on the null of
one fit per shuffled decoder (n1) alone, and called `ed7-motion-small`
tentative because nothing checked that the movie is raw. The author kept both
decoding claims blocked as `not_runnable`, and round 2 agreed with all 23
outcomes; nothing was proposed, so there was no third round. The paper, "An
optical design enabling lightweight and large field-of-view head-mounted
microscopes", describes two head-mounted microscopes, the Kiloscope (about 4
mm field of view, 1.4 g) and the Featherscope (1.0 mm, 1.0 g), used in four
mice and three juvenile zebra finches, and reports thousands of neurons
recorded at once in a freely moving mouse, from whose activity linear decoders
read the mouse's combined quadrant and movement direction at least three times
above chance. The footprint count, the field of view, the bead PSFs, field
curvature, the flat illumination of both microscopes and the motion of the
movie were tested, and the decoding claims were run under the (n1) null.
`ed7-motion-small` is not reproduced (0.037 px RMS against 0.13), and
`fig1f-kiloscope-psf` is partially reproduced because no reading puts both
values within tolerance. The decoding claims hold under (n1) (median accuracy
0.437 and 0.326 against the largest of 1000 shuffled decoders at 0.227 and
0.229), but the criterion also needs (n2), 200 fits per shuffled decoder,
which is 200,000 fits, measured for the quadrant claim at 33.3 hours in this
run (24.6 hours in the run of round 2) against 30 minutes per notebook, so
fig2 and ed9b are blocked as `not_runnable`, and `fig2k-decoder-size`,
`fig2l-local-decoding-map` and `ed9c-local-decoding-map` also, as they depend
on them and need 4.4 to 12.8 hours each on four cores. The other mice, the
songbirds, the weights, the USAF target images and the ADC recordings are not
deposited, `ed6a-curated-footprints` is blocked as `metadata_insufficient`,
and `fig2d-lman-sparse-bursting`, `ed8-coactive-distributed` and
`ed10-localized-activity` as `methods_underspecified`, ed8 because all four
quarters are covered in 8 of 8 events under one reading of the event times and
7 of 8 under the other. Compared with `-01`, abstract-kiloscope-fov moved from
blocked to reproduced, the two flat-illumination claims from partially
reproduced to reproduced, and ed8, ed9b, ed9c and ed10 from reproduced to
blocked. Some outcomes rest on weak ground: in abstract-kiloscope-fov both
pixel sizes come from the paper's code, the reading at 5.35 um per pixel only
just within tolerance (4.323 against a lower bound of 4.32) and the test close
to circular at 5.94 um per pixel; and the Kiloscope PSF fits depend on the
optimizer and differ between runs on different machines (4.467 um at the
centre under reading (a) in this run, 4.422 um in the run of round 2).

The dataset was converted by CatalystNeuro (Szonja Weigl of CatalystNeuro is a
contributor). The files are unchanged, so the nine findings of `-01` were
checked again, and all are still present. The dandiset holds one of the
paper's four mice and none of the songbird recordings, and the USAF target
images and ADC recordings are not public. The mouse's position, which the
paper's decoding and place analyses use, is not in the dandiset (its only
processing module is ophys), and the opening of the behaviour video that the
paper's code skips is not marked. The 2948 footprints are the EXTRACT output
before curation; the paper analyses the 2,382 it kept, and nothing marks them
or says the footprints are uncurated. The device description reads
"Head-mounted microscope (Kiloscope) optimized for weight (1.0 mm FOV; 1.0
g)", and the dandiset description also names the microscope optimized for
weight, where the data are from the large-FOV Kiloscope (4 mm window, 2948
footprints, 808 x 608 pixel frames). The imaging is stored as a
TwoPhotonSeries and two-photon microscopy is listed among the techniques,
though the microscope is a one-photon head-mounted epifluorescence microscope.
Nothing says whether the movie is the raw video or the motion-corrected one
the paper extracted footprints from; its values are consistent with the raw
video, and its rigid shifts against a template have an RMS of 0.037 pixels,
about a quarter of the 0.13 pixels the paper reports. Other findings: the
behaviour video is described as about 30 fps and its AVI header says 30
frames/s, but its 15521 timestamps run at a median 12.5 frames/s over 1234 s;
the imaging plane gives no pixel size, its indicator and location are
"unknown" and its excitation wavelength is NaN, although general/virus says
GCaMP7f; ROICentroids equal the mask's peak pixel for 84% of footprints and
the rounded weighted centroid for only 43%; both local decoding map scripts
use 64 footprints within 50 pixels where the paper describes the 32 closest
within 270 um; the Extended Data Fig. 8 legend refers to a Figure 3 and a
ridgeline plot in Fig. 2d, where the paper has two figures and the ridgeline
plot is Fig. 2h; the paper's tracking code unwraps position with MATLAB's
unwrap, which gains an error of up to pi cm at every lap of the 147.1 cm loop
and changes about 1% of the running and direction labels; and the paper's bead
scripts order the images by file date, which the repository does not keep, so
the Kiloscope stack's slice order is not recorded.

The notebooks, four at first, ran in 7 min, 19 min, 19 min and 22 min in the
first clean run and 497 s, 1122 s, 1124 s and 1237 s after the answer run.
`entry.py check`, and so `entry.py all`, failed throughout on 11 errors, all
in the deprecated record, which has no outcomes for the new claims and must
stay as it is, and the notebooks were run with `entry.py run`. Round 1's
points led to a check of whether the movie is raw (histogram roughness 0.740
to 0.745, which sub-pixel shifts of 0.13 px RMS lower to 0.052, and a known
jitter of 0.132 px RMS recovered with correlation 0.996), so ed7 is no longer
tentative, PSF readings with the lower-cost fit for each bead, the lines of
each illumination script that load the images, ed8 counts with the quarters
split at the image midlines, the real decoders' single fits compared with the
(n1) null, nine (n2) null decoders per decoding claim, and three new
notebooks, two of (n2) null decoders and one of reduced runs of fig2k, fig2l
and ed9c that decide nothing, none changing an outcome;
`fig2d-lman-sparse-bursting` changed its block reason from `data_missing` to
`methods_underspecified`. In both revisions the 2-hour command limit cut the
run of seven notebooks, and the last, `decoding_reduced.ipynb`, was run on its
own. Round 2 found numbers in the prose that its run did not print, among them
the fig1f margins, the run times and 5 of 56 significant points in the reduced
ed9c run where its run printed 0; the run made for the second revision printed
the prose's fig1f numbers, and the PSF fits, the reduced runs and the timings
turned out to differ between runs on different machines even with every seed
fixed (in the reduced ed9c run, 7 of 56 points significant in one run and 0 in
the other). The cause was not found, and the record gives both runs' values.
Untracked files in the repository root that the author did not create were
left alone. The author's points on the protocol: `entry.py check` fails on the
deprecated `-01` record, which must stay unchanged, so `entry.py all` cannot
pass; the section on repeat attempts assumes the claims file is kept and the
dataset changed, where here the claims file was rewritten and the data were
not; and the claims file sets decoding methods that need 10^5 fits, which a
30-minute limit per notebook cannot decide whatever the data.

### 001636, Pasquereau et al. 2013, second attempt

Four claims reproduced, three partially, three not reproduced and eighteen
blocked, all on the dandiset. The attempt was made on the draft of the
dandiset, which holds a new conversion made after 001636-pasquereau-2013-01
reported its findings; the claims file is unchanged, and every claim has the
same outcome as in `-01`. The archive listed 4 uploads in progress on the
draft while it was read, and between 23:00 and 23:10 UTC every asset was
uploaded again; the first good run of the first revision read the draft
mid-upload, with 23 pre-MPTP monkey V files missing and some monkey L files
read twice, so the author waited and ran it twice more, both giving the
numbers already recorded, and the record pins the draft as modified at
2026-10-21T23:10:32Z. The author raised no questions, and the answer run
found no questions file and changed nothing. Round 1 agreed with 27 of 28
outcomes; it gave `false-positive-rate` as not reproduced, where the author
kept it blocked as `methods_underspecified` under the rule that a computed
false-positive rate far from the paper's shows the procedures differ. Round 2
accepted that and agreed with all 28, so there was no third round. The paper,
"Primary motor cortex of the parkinsonian monkey: altered neuronal responses
to muscle stretch", reports how pyramidal tract and corticostriatal neurons
(PTNs and CSNs) in the primary motor cortex of two monkeys respond to torque
perturbations before and after MPTP. Only monkey V can be tested. The cell
counts, resting rates, antidromic latencies, the false-positive rate of the
response detection, kinematics and EMG were tested. The detection gives a
false-positive rate of 0.2279 against the 0.01 its threshold implies, which
blocks that claim and the 15 that use the detected responses;
`trial-correlations` is blocked because the paper defines no single-trial
latency, and `monkey-l-perturbations` as `data_missing`. `cell-counts` is
reproduced with 115 and 157 cells (51 and 54 PTNs, 32 and 48 CSNs), where
`-01` matched the paper's table exactly, as the draft adds the trials of a
second source file for 12 units; counting each unit from its first source
file only gives 112 and 157. `antidromic-latency` is partially reproduced as
the CSN p = 0.019 is just above the paper's 0.05/3 = 0.0167. The kinematic
and EMG outcomes rest on weak ground, as the torque command differs between
the states: `emg-m2-larger` is reproduced on the criterion, but at the one
per-trial command step with enough data the median m2 over the triceps
channels is 44.9 before and 1.8 after MPTP (p = 0.004, 66 and 11
channel-sessions), though on triceps longus 2 it is larger after MPTP (52.2
against 113.0, p = 0.36). In `session-correlations` the m2 correlation now
gives p = 0.023, above the paper's 0.0125, where in `-01` it reached it.

The dataset was converted by CatalystNeuro (catalystneuro/turner-lab-to-nwb).
The monkey L (Leu) files still mark no torque perturbation, the Leu torque
command is NaN in every pre-MPTP file and 15 of 50 post-MPTP Leu files have
no analog data, so the monkey L half of the paper (115 and 73 cells, and its
EMG and kinematics) cannot be tested; the description and the files now say
the Leu source files contain no perturbation times. The torque command's 50
ms pulse still has three session sizes (about 46, 91 and 183 units above
rest), the smallest in most pre-MPTP monkey V sessions (105 of 154) and the
largest in most post-MPTP sessions (125 of 137), with an opposite swing after
the post-MPTP pulses and a step that varies from trial to trial; the torque
description now states this and that no conversion to newton-metres is
available, while the paper describes one 0.1 Nm, 50 ms impulse. Fixed since
`-01`: the analog segments start at their trial's start (lag 0 ms at every
perturbation, the command stepping 4 to 6 ms after the labelled onset); the
reference frame says positive is flexion in all 424 files with an angle and
the monkey L series are WristAngle and WristTorque; no file repeats another's
trials and the two unit copies are stored once (v4527.2 and v5811.2, both
PTNs); `unit_also_in_session_id` is gone and neurons recorded across two
source files are one unit (13 units); and the dandiset description now says
intracarotid MPTP, the wrist for Leu, and Leu from August 1992 to December
1993. The EMG description now gives the paper's processing, but the monkey L
analog streams are still sampled at 100 Hz (the paper says 200 Hz) and the
EMG is in uncalibrated A/D units, now stated in the description. Still
present: the torque onset comes 1.696 to 1.732 s after
center_target_appearance_time in 90% of monkey V perturbations, where the
Methods put it 1 to 2 s after center capture at random; no analysis code is
published, and stationary Poisson spike trains give 0.16 to 0.21 against the
0.23 observed, so most of the excess comes from the detection procedure; and
the paper gives the pre-MPTP PTN and CSN resting rates as 16.3 and 3.6
spikes/s in the text and 18.3 and 3.2 in Table 1, and marks the CSN change in
the fraction of excitatory responses p < 0.01 where its own counts (23 of 24
against 19 of 22) give p = 0.54. New findings: three monkey V sessions
(v1401, v1402, v1501) have 51 labelled perturbations but no pulse in the
torque command, as the torque description says; and the dandiset names
catalystneuro/turner-lab-to-nwb as its code, but the main branch is still at
the commit read for `-01` and the code that built the draft is in open pull
request 33 (https://github.com/catalystneuro/turner-lab-to-nwb/pull/33,
branch fix_errors at 5f9bf6320a0160e4e56301d5409fb9242c1d8cf4). The claims
file's comment that no unit appears in two files no longer holds for the
draft, so the author applied the criteria per unit within its own trials and
showed the first-file reading as a variant.

`entry.py all` passed, the notebook taking 1.8 min in the first run and 4.1
min in the last. Round 1's points led to a per-cell table of the detection,
each antidromic test printed against its threshold, kinematic, latency and
EMG comparisons at the same per-trial command step, a run of the zero-phase
filter on synthetic movements (onsets 14 ms early to 5 ms late), the counts
of channel-sessions with m2 of zero or less, and a check that every spike
window lies inside its trial; none changed an outcome. Round 2 found
sentences the outputs did not support, among them the m2 result at the
matched step stated without its limits, a count of 16 claims blocked by the
false-positive rate that included that claim itself, and 14 cell-directions
said never to respond where near-silent ones with a threshold of about 0 can,
and these were corrected. Round 2 could not check the claims file's expected
values against the supplementary table, as no PDF reader was available, and
the author did not check them either. The author's points on the protocol:
`entry.py check` fails on the `-01` record once `entry.yaml` points at the
new version and passes only after the `-02` record exists, so it cannot be
run before the record is written; the schema has no field for whether an
earlier finding is fixed, so the status of each was put in the record's
header comment as in 001754-knierim-2000-02; the protocol records a draft's
modification time but says nothing about uploads in progress or checking the
draft again at the end; and showing how the versions differ, as step 1.3
asks, means loading the earlier version's units too, which adds streaming
time to every run.

### 000006, Economo et al. 2018, second attempt

Seven claims reproduced, five partially, three not reproduced and eight
blocked on the dandiset, with eight more on data in other archives, of which
five reproduced, one partially and two blocked. The claims file was written
again from the full text, as the earlier one, written from the abstract only,
is deprecated; it has 31 claims, and the dandiset is unchanged at version
0.220126.1855, its only published version. The author put 15 questions to a
reader. The answers made the code's per-unit rule the unit selection when
neither reading gives the paper's counts and each unit's own trial range the
trial range, so `pt-spike-rates-similar` moved from blocked to not reproduced
and `pt-variance-explained` and `pt-single-neuron-early-selectivity` from
blocked to reproduced; they moved the dependency of
`pt-lower-heterogeneous-rates` to `pt-tagged-units`, so it moved from blocked
to reproduced; they named three readings for the reconstruction counts, so
`pt-upper-thalamus-projection` and `pt-lower-medulla-projection` moved from
blocked to reproduced; and they made the test of `pt-types-shared-targets` on
the reconstructions a variant, so it moved from reproduced to blocked. The
commit with the answers had deleted four `- id:` lines from the claims file,
which then parsed to 27 claims, and the author put them back without changing
any statement, expected value or criterion. Round 1 agreed with 28 of 31
outcomes; for `pt-upper-persistent`, `pt-cohort-control` and
`pt-types-differ-in-timing` it gave the outcome of the claim's own test, where
the record blocks them because they depend on the blocked
`pt-upper-early-preparatory`. Round 2 accepted the dependency rule and agreed
with all 31, so there was no third round. The paper, "Distinct descending
motor cortex pathways and their roles in movement" in Nature, describes two
types of pyramidal tract (PT) neurons in mouse ALM, PTupper neurons projecting
to the thalamus and PTlower neurons projecting to the medulla, from
single-cell sequencing, axon reconstructions and units tagged by antidromic
photostimulation in a tactile delayed-response task, and reports that PTupper
populations carry early preparatory activity that persists until movement
while PTlower populations mainly carry late preparatory activity and movement
commands. The transcriptomic clusters, the reconstruction counts and the
fold-change correlation were tested on the paper's Figshare record, and the
unit counts, depths, spike rates, bursting, selectivity, variance explained,
coding directions, decoding and CDgo onsets on the dandiset. `pt-marker-genes`
is blocked as `data_missing` because the smFISH data are in no public file,
`reaction-time` as `data_missing` because no video is deposited, and
`pt-retrograde-sublaminae` and `pt-types-shared-targets` because the paper
gives no method for counting or analysing the anatomy images.
`pt-upper-early-preparatory` is blocked because its two rules for "larger"
give partially reproduced and not reproduced in all 8 combinations,
`pt-cd-change-at-go-cue` because levels 0.5 and 0.75 give reproduced and
partially reproduced, and `pt-lower-movement-termination` because its windows
and readings of a mouse give different outcomes. `pt-tagged-units` is not
reproduced with 44 PTupper and 56 PTlower units against 61 and 69,
`pt-selective-any-epoch` because 99 of the 100 included units the dandiset
holds cannot reach 122 +/- 12.2, and `pt-spike-rates-similar` because peak
rates differ (p = 0.030). Run on the paper's own 130 units from its processed
data, the same code gives the paper's numbers for unit counts, bursting,
late-delay counts, decoding, early selectivity and spike rates, and on the
processed data for the same 100 units it gives most of the dandiset's counts
and test results, so the count failures come from the missing sessions; the
CDgo onsets are out of tolerance even on the paper's units, the PTlower onset
falling in the 37.5 ms bin in the files, in the same units processed and in
all the paper's units, against 24 ms. Two questions added after round 1,
whether count criteria should be judged as fractions when units are missing
and whether the cohort control should count a difference in the opposite
direction as a failure, are unanswered.

The findings of `-01` are all still present, as the version has not changed.
Eleven sessions of the paper's processed data that hold tagged units are not
in the dandiset; they hold 17 of the 61 PTupper and 13 of the 69 PTlower units
the paper analysed, and the dandiset's description says some files were found
to be broken and left out without naming them. Every tagged unit the dandiset
holds is in the processed data with the same label, inclusion decision and
depth. New: the missing sessions also hold unidentified units, the dandiset
holding 232 in the PTupper cohort and 430 in the PTlower cohort against the
495 and 511 the paper analysed. Spike times are not sorted in 1120 of 1149
units, as they were written trial by trial and consecutive trials overlap on
the file's clock, so some spikes of one trial lie in the next trial's early
epochs (11.7% of the spikes counted in the baseline epoch are detectably out
of order); on the same 100 tagged units every unit's baseline rate is higher
in the files than in the processed data (median by 0.99 Hz for PTupper and
0.97 Hz for PTlower units). New: the lick times are stored the same way and
are out of order in 105 of 106 lick series (14,360 backward steps in 180,679
licks), and the files do not assign licks to trials; rebuilt from the stored
order, each trial's last lick matches the processed data's in 98.1% of correct
trials. The trial table's stop_time is NaN in every file, pole_in_time,
pole_out_time and cue_start_time are relative to the trial start without
saying so, and the go cue of a trial falls after the next trial's start_time
in 13,306 of 15,096 trials. The labels PTupper and PTlower are not described,
and their projection targets are stated only in the paper's code. Unit quality
mixes two vocabularies and has undescribed empty values, sex is U and genotype
empty for every mouse, the electrode positions are all zero, and every
electrode group gives layer 5 whatever the depth. The dandiset holds the
electrophysiology only, with the sequencing, axon reconstructions and anatomy
on the Figshare record and at GEO (GSE119182), and the smFISH data behind Fig.
3c in no public file; new, no file holds video or the session manipulator
depth. In the paper's processed data, and so in the files, the spike windows
of the first ten trials of every session start later relative to the pole
than those of the other trials (session medians 1.73 to 5.84 s after the pole
comes in, against -0.97 to -0.16 s), which the paper's code hides by leaving
those trials out.

The notebook ran in about 11 minutes in the first run, 628 s after the
answers, about 11 minutes twice after round 1, and 598 s and 611 s after round
2. `entry.py all` stopped at the check in every run on 22 errors in the
deprecated `-01` record, which lacks outcomes for the claims the rewritten
file added, so the author ran `entry.py run` directly; the `-02` record passes
the check. Round 1's points led to a rerun of the measures on the processed
data for the 100 units the dandiset holds, the CDgo 5th percentile from 0 to
0.1 s, the share of unit-trials whose last lick is more than 2.5 s after the go
cue (0.16% and 0.17%), the structures of AA0134's axon nodes, a
reconciliation of the processed data's 150 tagged units with the paper's 143
and the Anatomy.zip image counts; none changed an outcome. Round 2 found
statements the outputs did not support, among them unidentified pools called
about half the paper's where the PTlower cohort has 430 of 511, the processed
data for the same units said to give all of the dandiset's counts and test
results, and a baseline rise of about 1 Hz where it ranges from 0.14 to 6.47
Hz, and these were corrected. Untracked files in the repository root that the
author did not create were left alone. The author's points on the protocol:
`entry.py check` fails on the deprecated `-01` record, which cannot be fixed
without editing it, so `entry.py all` stops at the check; the dependency rule
over-blocks, as `pt-lower-heterogeneous-rates` used only the rates of
`pt-spike-rates-similar` yet was blocked with it; the rule for data elsewhere
forbids `data_missing` for data that are public nowhere; the section on repeat
attempts assumes the dandiset changed, where here the claims file changed and
the data did not; and no selection is designated when neither reading
matches, the gap behind most of the blocks before the answers.

### 000011, Li et al. 2016

Six claims reproduced, five partially, nine not reproduced and eighteen
blocked, all on the dandiset. It pins version 0.220126.1907, the only
published version, as the paper cites none. The author put ten questions to a
reader, and nine of the answers were that the paper does not give the detail,
so each open detail became a set of readings under which the outcome must be
the same; the answers changed two outcomes. `cd-captures-selectivity` moved
from not reproduced to blocked as `methods_underspecified`, as the cd values
are within tolerance with all correct control trials (66.2% and 34.6%) and
outside with the training trials (73.7% to 88.0%), and `ed9f-reaction-time`
stayed blocked but moved from `methods_underspecified` to `data_missing`.
Round 1 gave its own outcome for each claim from the notebook with its
conclusions and summary removed and agreed with 34 of 38. `selective-fraction`
and `ed2b-silencing-strength` moved from partially reproduced to not
reproduced, as with lick-early trials dropped only 1 of 4 counts holds in the
first and with them kept only 1 of 4 parts in the second, and
`cd-stable-over-epochs` moved from reproduced to blocked, since taking w from
all correct control trials (0.563 and 0.588) was the author's choice and the
training subset gives 0.534 to 0.554. The author kept
`ed7e-roc-larger-photoinhibition` and `ed8-roc-during-photoinhibition` as
partially reproduced, where round 1 gave not reproduced, under a rule written
after round 1 for criteria without a partial clause (partial when at least
half the parts hold under every reading that must agree); round 2 accepted it
for consistency and agreed with all 38, so there was no third round. The paper, "Robust neuronal
dynamics in premotor cortex during motor planning" in Nature, records units in
left ALM of mice in a delayed-response task while one or both hemispheres are
photoinhibited, and reports that preparatory activity and behaviour recover
after unilateral but not bilateral silencing, that the recovery needs the
other hemisphere, as shown by callosotomy, and that modular network models
recover where single-module models do not. The unit classes, selective counts,
recovery of rates and selectivity after silencing, the coding direction and
its modes, the session biases and the network models were tested. The
behavioural photoinhibition claims, the photoactivation claims and the spatial
extent of silencing are blocked as `data_missing`, the four callosotomy claims
on the recordings as `metadata_insufficient`, and `fig1g-selectivity-recovery`
and `ed7-larger-photoinhibition` as `methods_underspecified` because their
readings disagree (12, 9 and 3 of 24 combinations with three, two and no
times within tolerance for fig1g). `fig2e-selectivity-recovery-times` is not
reproduced because ipsilateral selectivity does not reach 80% of control
before the go cue under any of the 24 combinations, against the paper's 538
ms, and `fig3d-persistent-mode` and `fig3e-ramping-mode` because both modes
predict the lick on control trials above chance (59% to 62% and 55% to 58%).
Some outcomes rest on weak ground: `fig1f-spike-rate-recovery` holds only on
the reading without exclusion, which tests 248 neurons per condition against
the paper's 168 to 175, while the reading close to the paper's counts fails;
and the partial outcomes of `unit-classification`, `fig2-recordings-recovery`,
ed7e, ed8 and `fig6-modular-models-recover` rest on the author's rule, which
the claims file does not contain and under which, read strictly, they would be
not reproduced. A question asks a reader whether the claims file adopts it.

The dandiset holds only the recording sessions: the behavioural
photoinhibition sessions (Figs 1d, 2b, 5b and Extended Data Fig. 3), the
photoactivation mice (Extended Data Fig. 5), the untrained mice used to map
photoinhibition (Extended Data Fig. 2d) and any session before callosotomy are
not in it, so nine of the paper's findings cannot be tested, and its
genotypes are VGAT-ChR2-EYFP and PV-ires-Cre x ReaChR only. 33 sessions of 7
mice, the callosotomy group by genotype and delay, and 3 experiment-1 sessions
of mouse 255200 have no photostimulus record, though most of them contain
trials whose activity is silenced in the light window of the other sessions,
so their photoinhibition and control trials cannot be told apart; no file
says which mice were callosotomised, on which side or when. The trial table
has no photostimulus column, so the site, number of laser spots and timing of
a trial can be recovered only from the per-site laser power traces and the
photostim_start_time events, and the number of spots is stated nowhere. In
lick-early trials the photostimulus events are logged at the restarted delay,
after the light seen in the laser trace; over all labelled sessions 339
lick-early photostimulus trials have the event more than 0.1 s after the
light, with the light up to 10 s before the logged go cue, so with lick-early
trials kept these trials enter the photoinhibition averages without light (3%
to 16% of each condition's trials in experiment 1, 6.5% to 7.5% in experiment
2). No file holds lick times, only the analogue lick_trace, which in the 24
experiment-2 sessions used for the activity space holds no licks, so reaction
times cannot be computed there. The control mice hold 979 units against the
paper's 1012, with 15 of intermediate spike width against 50, so about 33
intermediate units were not deposited (widths from upsampled waveforms give
11), and the units' cell_type labels intermediate-width units as FS, where the
Methods exclude them (45 units in all). The paper's neuron and session counts
for its selectivity and population analyses (55, 143 and 40 selective
neurons; 16 sessions with 6 to 20 neurons) cannot be reached with the
criteria the paper states, the dataset giving 138 to 173, 221 to 293, 58 to 62
and 24 sessions with 6 to 37 neurons, and experiment 1 holds 4 mice where the
paper reports 6. Other findings: session 258250_20141202 holds two
interleaved sequences of trial ids (1 to 24 and 105 to 160) whose times
overlap (98 overlapping pairs), in 28 units of 3 sessions the spike times are
not in time order and two sessions have trials out of time order; and the
asset sub-255200_ses-20140910_behavior.nwb holds only metadata.

The notebook ran in about 11.5 minutes in the first run, 1042 s after the
answers, 791 s after round 1 and about 19 minutes after round 2, and
`entry.py all` passed with no errors. One run failed after a regex that
stripped bold markup also removed `**` operators from the code; they were
restored and the outputs matched the earlier run. Round 1's points led to
spike widths from waveforms interpolated to ten times the stored rate, the
size of the lick-early artefact, per-neuron trial counts and epoch
selectivity of the included populations (no simple further selection gives
the paper's counts), per-session ROCs of the modes, raw lick-trace levels
above the experiment-2 baseline with the ed9f test run on the 6 experiment-3
sessions as a variant (it holds under 18 of 26 combinations), reference
numbers on the recording sessions for the blocked behaviour and callosotomy
claims, and three more questions to a reader, which are unanswered. Round 2
found statements the outputs did not support, among them a time of 750 ms
called outside a tolerance of 210 to 770 ms in ed7, the event said to be
logged up to about 2 s after the light where the maximum printed is 1587 ms,
and differences within 2 s.e.m. under every reading in fig3e where that holds
for T1 only, and these were corrected; a typo fix in a markdown cell came
after the last run and was applied to the executed copy by hand. Untracked
files in the repository root that the author did not create were left alone.
The author's points on the protocol: it does not say how the claims file's
rule that any reading may reproduce combines with readings of details the
author finds open; it gives no guidance on reporting up to 256 combinations
per claim; the claims file's "trials per condition" could not be left open;
there is no `data` kind for simulations that use no data; unlabelled
photoinhibition trials fit both `data_missing` and `metadata_insufficient`;
there is no channel to pass back a point the data settle in the claims file;
its rule for selections covers only chance levels; it does not say whether a
measured recovery time is the point estimate or the bootstrap mean; the
header table allows only "tested" or "blocked" for claims that ran but are
blocked; and question files name a single claim where questions apply to
many.

### 000013, Hires et al. 2015

Twenty-two claims reproduced, one partially, eight not reproduced and
fourteen blocked, all on the dandiset and all blocked as
`methods_underspecified`. It pins version 0.220126.2143, the only published
version, as the paper predates the dandiset and cites none; the draft holds
the same 52 blobs. The claims check added `example-cell-phase-modulation`, so
the file has 45 claims. The author put seven questions to a reader; the
answers changed four outcomes. They set the start of the touch response
cutoff search at the transition where the curve levels off, keeping the
literal search from 1 ms only as a variant, so `table1-l4-c2` moved from
blocked to reproduced and `table1-l5` from blocked to partially reproduced;
they made the phase decoder use the phase-tuning cycles, so
`fig4c-phase-decoding` moved from not reproduced to blocked; and they made
"median higher" the median of the per-cell differences, so
`whisking-rate-l5-increase` moved from partially reproduced to reproduced.
Round 1 gave its own outcome for each claim from the executed notebook with
its conclusions and summary removed and agreed with 36 of 45.
`behavior-whisking-bouts`, `behavior-touches-reaction` and
`example-cell-touch-window` moved from partially reproduced to not
reproduced, as their criteria need every value within tolerance and give no
rule for a partial match. With the whisking periods corrected,
`whisking-rate-l4-no-change` moved from partially reproduced to blocked (L4
C2 p = 0.595 with touch epochs left out of whisking, p = 1.28e-7 with them
in), and with phase cycles taken from the whole trial fig4c moved from
blocked to not reproduced. The author kept `example-cell-ff-around-touch`,
`table1-l4-outside` and `fig5-modulation-correlations` blocked because their
readings disagree, and `fig3c-touch-spikes-outside`,
`fig3d-touch-phase-outside` and `fig4a-touch-detection-outside` blocked
because they depend on blocked claims; round 2 accepted these and agreed
with all 45, so there was no third round. The paper, "Low-noise encoding of
active touch by layer 4 in the somatosensory cortex" in eLife, describes 52
loose-seal cell-attached recordings from L4 cells in the C2 barrel, L4 cells
outside C2 and L5 cells near C2 in mice trimmed to the C2 whisker and
localizing a pole in a go/no-go task, and reports that L4 C2 touch responses
are temporally precise, that 15 L4 C2 neurons detect 95% of touches, that 200
of them decode the time since touch with a minimum uncertainty of 0.55 ms,
and that the Fano factor after touch lies close to the binomial limit. No
claim is blocked for lack of data, so the recordings, behaviour, the example
cell, Table 1, phase modulation, whisking rates, touch-coupled spikes, the
decoders, modulation indices and Fano factors were all tested.
`recordings-mice` is not reproduced because the files hold 23 subjects
against 21 mice, `latency-determinable` because 7 (first touches) or 10 (all
touches) L4 cells outside C2 have a latency against 4,
`fig4b-touch-time-precision` because the RMS error is 1.09 to 1.40 ms against
0.55 +/- 0.055, `text-whisking-rates` because no reading puts both rates in
tolerance, and fig4c because C2 is far from 24 +/- 2.4 deg and worse than
outside C2 under every reading. `fig3c-touch-spikes-l4c2`, on which the
other Figure 3 claims depend, `fig4a-touch-detection-c2` (12 to 30 neurons,
only one reading at 14 within 15 +/- 1.5) and `fig6d-not-refractory` are
blocked because their readings disagree. Some
outcomes rest on weak ground: table1-l4-c2 sits exactly at its threshold, 15
of 18; the criterion's latency rule gives noise latencies of 0 and 1 ms that
count as determined; fig4c's criterion ends "else methods_underspecified",
which the record reads as its rule for readings that disagree, a reading
round 2 called reasonable but not the literal text; and among the claims
blocked by dependency, the fig3c and fig3d outside claims fail under every
reading and fig4a-touch-detection-outside holds under every reading.

All 52 recordings are present and none is deposited twice. In 36 files the
SpikeTrain timestamps run 10 ms before the CurrentClampSeries timestamps of
the same samples; under the spike timestamps the median L4 C2 touch-response
peak is 8 ms in the files without the offset and 12 ms in those with it (rank
sum p = 0.016), and 8 and 22 ms under the voltage timestamps, so the data are
consistent with the voltage timestamps of the 36 files being 10 ms late, and
a residual 4 ms difference is not explained. In 38 files the
CurrentClampSeries data, with the stated conversion of 0.001 to volts, span
only 2 to 26 microvolts, so the conversion is off by 1000 (the other 14 span
3 to 28 mV). In 38 files theta_filt, described as theta_at_base filtered 6 to
60 Hz, is not the signal the stored amplitude and phase come from (up to 46
deg apart), while in 14 it equals amplitude times cos(phase); the stored
amplitude and phase match a 6 to 60 Hz Butterworth band-pass and Hilbert
transform of theta_at_base. set_point is described as the amplitude of the
Hilbert transform but follows theta minus its band-passed part (r 0.96 to
1.00) and holds missing values in 23 files. pole_position is described in mm,
but its values range from 0.2 to 1.6 in some files, 992 to 13888 (motor
steps) in others, about 1e8 in others and up to 1.4e12 in one. Three subjects
(anm211295, anm215592, anm217330; six cells) have no genotype, the paper's
VGAT-ChR2 mice by their counts, and the files hold 23 subjects where the
paper reports 21 mice, with the C57BL6 and Ai32 x PV-Cre counts off by one
cell each, so the mapping of subjects to the paper's animals is not given.
Other findings: 30 files are named with an ogen suffix, but no file holds an
optogenetic stimulus series and stim_present is 0 in every trial;
first_lick_time disagrees with the lick onset series by up to 3.1 s, with 47
trials having licks and no first_lick_time and 136 a first_lick_time and no
lick; and the paper's analysis code is not public, the repository it links
holding only the contact detection.

The notebook ran in 8.7 minutes (530 s) in three runs through `entry.py all`,
all passing, 8.7 minutes after the answers, 12.1 minutes after round 1 and
7.5 minutes in the last of two runs after round 2. During development the
first loader took 13 minutes, until loading in separate processes cut it to
80 s. Round 1's points led to whisking periods that leave out licking cycles
and the 70 ms after each touch, phase tuning over every phase-analysis cycle
of the trial and not only the sample epoch, a touch detector that reads the
fraction detected at the time point of best percent correct with ties broken
at the middle threshold (the earlier rule counted every sample as a touch),
50 repetitions in place of 20, the zero-median checks counted in Table 1, and
per-file touch-peak latencies by clock offset, per-cell touch windows and the
rows where cell 11 matches. Round 2 could not check the dependency rule, as
the protocol was not among its materials, and found statements the outputs
did not support, among them l5-higher-rates medians from the earlier
whisking mask, p = 0.971 where the output printed 0.798, fig4c medians that
hold only over the 42 and 38 of 100 runs reaching 76% correct, a README run
time of twelve minutes against 8.8 printed, and a synthetic detector value of
0.15 that no output showed, which a new cell now gives as 0.329 at 0.541
percent correct; these were corrected. Untracked dotfiles in the repository
root that the author did not create were left alone. The author's points on
the protocol: one literal reading can block many claims, as ten claims hinge
on two readings of the cutoff rule, one of them degenerate; a blocked
dependency hides a clear failure, as in fig3c-touch-spikes-outside; a
criterion's fallback can conflict with the protocol, as fig4c's does; Table
1's 256 combinations of readings make an agreed outcome nearly impossible;
"any cell" criteria let chance decide, as cell 11 matches in 2 of 394 tries;
`measured` has no slot for a value never reached; the suggested clock check
does not fit continuous trial data; no published version is cited; the
no-download rule left the author caching reduced arrays in `$TMPDIR` while
developing; and the advice that h5py with remfile serialises reads across
threads, so loading needs separate processes, belongs in `docs/archives.md`.

### 000015, Chen et al. 2017

Eleven claims reproduced, three partially, seven not reproduced and eight
blocked on the dandiset, with one more reproduced on the dandiset together with
the Li et al. 2015 units of dandiset 000010; the two claims on the silicon
probe recordings, which the claims file places at CRCNS, are blocked. It pins
version 0.220126.1914, the only published version, whose draft has the same
210 assets. The claims were written from the extracted text of the paper,
which lacks its Supplemental Information, with no figure looked at, so the
five claims on Figures S1, S4, S5, S7 and S9 rest on the main text alone; the
claims check added `alm-pt-it-lick-fraction-below-20` and the author added the
link claim `li2015-tagged-units-link`, so the file has 33 claims. The author
put five questions to a reader, every answer was that the paper does not say,
and each added readings to the criteria; two outcomes changed:
`ephys-pt-it-onset-not-detected` moved from blocked to reproduced, and
`fig8d-pt-earlier-than-it` from not reproduced to reproduced, as the new onset
rule S2 gives 1.801 s. Round 1 gave its own outcome for each claim from the
notebook with its conclusions and summary removed and agreed with 32 of 33; it
gave not reproduced for `fig8d-error-outnumber-correct`, whose reading (b)
reaches only 1.81 bootstrap SD against a bound of 2 and whose criterion names
no partial outcome, and the author changed it from partially reproduced. Round
2 agreed with all 33, so there was no third round. The paper, "A Map of
Anticipatory Activity in Mouse Motor Cortex" in Neuron, images 15,431 neurons
in ALM and MM of six mice in a tactile delayed-response task, and reports that
object location is represented mainly in MM and preparatory lick direction
activity in ALM, and that lick direction selectivity is stronger and earlier
in PT than in IT neurons, labelled in three of the mice. The sample, trial and
neuron counts, the selectivity of single neurons and its timing, the area
comparisons and the PT and IT analyses were tested. Four claims that need
plane depth are blocked as `metadata_insufficient`, the wide-field,
photoinhibition and whisking claims as `data_missing`, and the two silicon
probe claims as `other`, as the registry's check does not allow
`data_missing` for data placed in another archive. `fraction-selective-alm-mm`
is not reproduced because MM is above tolerance under every reading (closest
1,736, 26.3%, against at most 1,675 and 25.3%), `fig4c-outcome-after-lick`
because 41.3% of outcome-selective ROIs are first selective after the go cue
against more than half, `fig6-outcome-response-uniform` because its part (a)
fails in MM, and `fig8d-pt-contra-bias` and `fig8d-mm-posterior-preferring`
because their direction holds but they reach 1.71 and 1.87 bootstrap SD
against 2. `figs4-peak-shift` is not reproduced because over the whole window
MM peaks after ALM (6.09 against 4.52 s), but before the go cue MM peaks first
under every reading (2.08 against 4.16 s, V1, T1); round 2 called the
criterion a misreading of the paper, which places the shift over the delay
epoch, and a question on the window is unanswered. Some outcomes rest on weak
ground: `figs5-single-coefficient`, `fig4a-lick-direction-epochs` and
`fig4b-object-location-memory` are met by permuted trial types as well;
`fig8d-pt-earlier-than-it` passes in 2 of 16 combinations, both with rule S2,
T2 bins interpolated from frames and the bootstrap over cells; and in
`ephys-pt-it-onset-not-detected` the two baselines are the same two windows and
the IT baseline SD is 0.0004, so the test carries little information.

Every one of the 105 image planes is deposited twice, as two files whose
contents are identical except the identifier and creation date, so the 210
files are 105 recordings. The files hold no plane depth, no stereotactic
coordinates and no identifier of the imaging location within a mouse, and no
text value in any plane names a depth, a coordinate or a layer, so four of the
paper's findings and the depth parts of three others cannot be tested, nor can
the 12 imaging locations be counted. The dandiset holds only the two-photon
imaging: the wide-field imaging, the whisker tracking, the lick times, the
photoinhibition behaviour and the silicon probe recordings (567 units) are not
in it, and the CRCNS DOI the paper names, 10.6080/K0S180F9, resolves to a
placeholder record ("CRCNS.org ssc-8TBD", "not yet available"); a search of
DANDI by the paper's DOI and its authors finds only dandiset 000015.
ImagingPlane.location is "ALM" in every file, including the 47 planes whose
experiment_description says left_vm1 (the paper's MM); with
experiment_description as the area, the ROI, area, PT and IT counts, the
trials and the early-lick fraction all match the paper (15,431 ROIs, 8,837 in
ALM and 6,594 in MM, 719 PT and 2,631 IT). With the stored ROI and neuropil
traces and the paper's r = 0.7, the baseline F0 is zero or negative on 0.26% of
ROI-trials, in 1,262 ROIs, and dF/F reaches thousands, dominating the MM mean
dF/F; the paper does not say how these were treated, and two outcomes
(`fig8d-error-outnumber-correct` at 2.20 SD and `fig8d-pt-contra-bias` at 1.97
SD without those ROIs) stay sensitive to them. Other findings: the ROI table's
`included` column marks 8,655 of 15,431 ROIs without saying what excluded the
others, where the paper's counts use all of them; the trial table's start_time
is 0.623 s before the sample event, the paper's trial start, in every trial,
an offset that is not described; early-lick trials do not record the pole
position; and the tagged PT and IT units of Li et al. 2015 that the paper
compares with are on DANDI as dandiset 000010, version 0.220126.1905, which
labels exactly 45 PT and 27 IT units, matched by label and count only.

`entry.py all` passed with 0 errors, the notebook running in 11.2 min in the
first run, about 18 min after the answers, 15 min after round 1 and 20.4 min
after round 2. One preparation script, not part of the entry, crashed on JSON
serialisation and was fixed, and one shell command was refused for lack of
approval and replaced by the search tool. Round 1's points led to a search of
every text value of every plane for depth (none found), a listing of the
behavioural events of all 105 planes (sample, delay and go only, so no lick
times), three duplicate pairs compared in full, the permuted-label null for
figs5 (0.845 to 0.911), the figs4 peak before the go cue and within the delay
with a sixth question to a reader, the PT part of `fig8d-mm-object-location`
(0.623 against 0.033) and the variance explained by area and projection type
for `fig8ef-area-explains-variance` (projection type 0.0013 against area
0.0005, not separated by the bootstrap), and the DataCite record of the CRCNS
DOI; no outcome changed apart from fig8d-error-outnumber-correct. Round 2
found statements the outputs did not support, among them window W1 given as the closest reading in
`fraction-selective-alm-mm` where W3 is closer, a README row that left out the
T2 bins on which fig8d-pt-earlier-than-it rests, a README run time of about fifteen
minutes against 19.7 printed, and silicon probe data called never made public
where the notebook showed only the placeholder DOI, and these were corrected;
the markdown cells were changed after the last run, so the git-ignored
executed copy still shows the old conclusion text. The author's points
on the protocol: it has no rule for a multi-part criterion with an untestable
part; it forbids `data_missing` for an `elsewhere` claim whose data were never
public while the author cannot change the claim's `data` field; blocking every
claim that depends on a blocked claim is coarse; it has no rule for criteria
that chance alone satisfies; its two reading rules, any reading may match and
all readings must agree, are easy to confuse; it does not cover `measured`
when no reading matches; it does not say whether mapping a data event to the
claims file's trial start counts as a method choice; and it does not say
whether to write a link claim when its only dependent is blocked.
