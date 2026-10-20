# Protocol for an attempt

Version: `pilot-10`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. It is written from the pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dandiset's data.
- The **author** tests the claims on the dandiset. It reads the paper to
  understand the claims, but the claims file binds it: it cannot change a
  claim, and it asks a reader for any method detail the file lacks.
- The **verifier** checks the author's work and must not be the author.

So every claim and its method are fixed from the paper before anyone analyses
the data, and no method is chosen by the agent that runs the analysis.

Reader runs are made with the [Paper run](../.github/workflows/papers.yml)
workflow (roles `claims`, `claims-check` and `answer`), the only runs that
write the claims file. The other runs are made with the
[Agent run](../.github/workflows/attempt.yml) workflow, one role at a time:
`author`, `author-answers` when questions were answered, `verifier-1`,
`author-revise-1`, `verifier-2`, `author-revise-2`, and, when the last of these
proposes changes of outcome, `verifier-3` and `author-revise-3`. Each run's
transcript and final report are kept in
[`transcripts/<dandiset>/`](../transcripts). The pipeline is described in
[pipeline.md](pipeline.md).

## Reader

### 1. Get the paper

The workflow puts the paper's full text, and its PDF where there is one, under
`paper/`: the main text, the Methods, and the supplement. Read the text; open
the PDF only to read a figure or a table the text garbles. If the full text is
not there, or lacks the Methods or a supplement the results rest on, stop:
write no claims, and end with a report that names what is missing, so that it
can be supplied. Never write claims from the abstract. Do not copy figures.
Do not look at the dandiset's data: its title and description on the archive
are enough to know which paper and which experiments it is meant to hold.

### 2. Read the paper's code

Read the code the paper links to before writing criteria. Say what it holds,
and record the repository and commit read. Where the Methods leave a choice
open and the code settles it, follow the code and say so. Where they disagree,
follow the Methods for the main result and name the code's choice as a
variant. When more sources disagree (the Methods, the analysis code, the
stimulus software), the Methods come first, then the paper's analysis code,
then other software.

### 3. Write the claims file

Write `claims/<dandiset>/<doi with / replaced by ->.yaml`. Its opening comment
says which text was read (the version of record or a preprint version, and the
supplement), and describes the data the paper used: the subjects, sessions,
conditions and measured variables, as the paper reports them, so that the
author can find them in the dandiset.

   - One claim per finding, at the level of a figure panel or a reported
     number when the full text is available. Cover the paper's main findings,
     including those the dandiset cannot test.
   - `statement`: the finding in words. `source`: where the paper shows it,
     precise enough to find without searching: a figure panel, or a section
     and paragraph ("Results, Place fields, paragraph 3").
   - `quote`: the sentence at `source` that states the finding, copied word
     for word from the full text, cut with "..." where it runs long. It lets a
     reader check the statement against the paper without opening it. For a
     finding shown only in a figure, quote the legend or the sentence of the
     Results that cites the panel.
   - `inferred`: every finding has a quote or, when no sentence of the paper
     states it (numbers only in a table, a result spread over several
     legends), a short note under `inferred` saying so. The statement is
     then a reading of the paper, and the note says what it was
     read from.
   - `statistics`: the statistical support the paper reports for the
     finding, one entry per test or interval: what it compares (`about`,
     when there is more than one), the `test` and `statistic` as named, the
     `p`-value as a number (a bound such as "p < 0.05" is `p: 0.05` with
     `p_relation: "<"`; a printed "P = 0" is recorded as 0), any `corrected`
     for multiple comparisons, a confidence interval (`ci`), and `n` in
     words. It records the paper; the
     numbers the attempt must match, with tolerances, stay in `expected`.
     Record only tests whose result is the finding. A significance threshold
     used to select or count units, cells or pairs ("238 of 288 neurons were
     better fit, p < 0.05") is a method, not a result, and is left out.
     Leave the field out when the paper reports no test or interval for the
     finding.
   - `expected`: each reported number the claim rests on, with a tolerance.
     Use the paper's own uncertainty when it gives one (a confidence
     interval, or the stated spread); otherwise 10% of the reported value.
     For a reported range ("2 to 13%"), the claim holds inside the range
     widened by 10% of each bound. Give the reason for any other tolerance.
   - `criterion`: how the claim will be judged, for any claim that is not
     settled by its expected values alone ("similar", "many", "tended to").
     It is written from the paper alone, before anyone analyses the data.
   - When a reported number can be read in more than one way (which trials
     form the denominator, which subset is meant), list in the criterion the
     readings the paper's text plausibly allows, before the analysis. The
     claim is reproduced if the result matches under any of them. The
     notebook shows every reading, the notes say which ones match, and the
     ambiguity is recorded as a deviation.
   - Methods come from the paper, never from the author. Every part of a
     criterion's method (the selection, the measure, the test, windows,
     bins, thresholds, what a measure is compared with) is taken from the
     Methods, the figure legends, the supplement, or the code the paper
     links, and the criterion says which. Search all of them before
     treating a detail as open.
   - A detail none of them fixes is recorded as a deviation that says so.
     If it cannot change the outcome (a plotting bin, a random seed), use a
     standard choice and say that it is one. If it could change the outcome
     (how folds are formed, what a measure is compared with, how a penalty
     is chosen), the criterion names the readings the paper's text allows,
     before the analysis, and the notebook runs each of them. The outcome is
     the one they all give; when they give different outcomes, the claim is
     blocked as `methods_underspecified`, with every result shown. A choice
     made by an agent is never the basis of an outcome.
   - For a claim of absence ("no difference", "did not change"), the
     criterion names the test and threshold the paper used. The claim is
     reproduced when that test does not find the effect and not reproduced
     when it does; give the size of the effect either way. The rule for
     several readings does not apply: absence is judged on the paper's test
     alone, as written, even when the test mixes in a condition that does
     not belong (show the cleaner test as a variant).
   - If a criterion turns out unable to decide (two candidates tied), break
     the tie as the paper's methods or code imply, record it as a deviation,
     and show the other result.
   - `data`: what the paper's test of the finding uses, from the paper:
     `dandiset` (the default: the data the paper describes recording),
     `with_labels`, `with_inputs` or `elsewhere` (step 4, and author, step
     4). Whether the dandiset holds those data is the author's to find.
   - `depends_on`: the claims whose result this one uses, such as the cells
     another claim selects.

### 4. Data from outside the paper's own recordings

Say, for each claim, what data the paper's test uses (`data`, above). When the
paper relies on outside data (a model, a reference dataset, measurements of
the same cells made by another method), or deposited part of its data in
another archive, name it and where it is, as the paper gives it. The author
pins it and decides whether it can be used (author, step 4).

### 5. Check

A second reader, in a separate run, checks the claims file against the paper:
that each statement says what the paper says, no more and no less; that each
quote is word for word (the quote checker, `tools/claims_check.py`, does this
mechanically); that each source points at the place; that the statistics are
the paper's and are results, not thresholds; that every part of every
criterion's method is taken from the paper or its code, as cited; and that the
paper's main findings each have a claim. The checker corrects what it can
show is wrong, and records each change, with its reason, under `checks` at
the end of the file. A claims file is ready for an attempt when its last check
says so.

### 6. Answer questions

When an attempt needs something the claims file does not give, the author asks
(author, step 6). A reader answers each question from the paper, in the claims
file, and marks it answered in `questions/<dandiset>.yaml`. An answer
the paper does not give is said to be that: the claim stays as it is, and the
author treats the detail as open (step 3, on details none of the sources fix).

## Author

The workflow puts the paper under `paper/`, as for the reader. Read it to
understand the claims, their data and their figures. The claims file still
decides what is tested and how: do not change a claim's statement, expected
values or criterion, and do not apply a method detail the claims file lacks,
even one the paper gives. Ask for it (step 6).

### 1. Establish what can be tested

Do this before any analysis.

1. List the dandiset's files and read its metadata from the archive. Open a
   file and list everything it holds, including every column of every table.
2. Work out which of the subjects, sessions, conditions and measured
   variables that the claims file describes are in the dandiset. A dandiset
   that names a paper may hold only part of its data. Check for recordings
   deposited more than once (identical traces, frame counts or annotations),
   report each pair, and count each recording once. Where the analysis treats
   a unit as the same across sessions, show that it is, or state it as an
   assumption and also give results per session.
3. Choose the version to pin. Pin the version the paper cites, as the claims
   file gives it. If it cites none, pin the most recent published version,
   unless an earlier one matches the claims file's description better. Say
   why in the notebook's header. If versions differ in content the analysis
   uses, show the difference.
4. Decide what comes from outside the dandiset. Data from elsewhere may be
   used only when the claims file says the paper relies on it, it is public,
   and it is pinned: a DOI, or a repository at a commit. Record each under
   `inputs` in the attempt. A claim whose outside input is not public is
   blocked with `data_missing`, and its notes say where you looked.

   The registry judges the dandiset, so claims that use outside data are
   kept apart:
   - Each claim says what its test uses: `data: dandiset` (the default),
     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
     `with_inputs` and `elsewhere` claims are counted apart, each group on
     its own; the others count towards what is said about the dandiset.
   - `with_labels` is for outside sources that only name or map codes the
     dandiset already holds, such as stimulus names for its stimulus codes.
     They bring in no measurements. A link claim must confirm the names, and
     the missing names are recorded as a finding (`metadata_insufficient`).
   - When outside data has to be matched to the dandiset's cells, sessions
     or subjects, a claim of its own (`kind: link`) tests the link. Link
     claims are the registry's checks, not findings of the paper, so the
     author adds them to the claims file; they are the only claims the
     author writes. A link claim says how
     records are matched (an identifier, or, where there is none, summary
     values the paper or its code published, such as per-condition medians),
     what fraction match, and whether the matched records agree on what both
     describe, such as counts, layers, or the paper's own per-cell tables. A
     dandiset that cannot be linked to the data it was published with is a
     finding about the dandiset. Every claim that needs the match lists the
     link claim in `depends_on`, so it is blocked when the link fails. When
     the link holds only in part, the dependent claims are still tested, and
     their notes say how the partial link bears on them. A label that
     differs only in spelling (one cell type named two ways) is the same
     label: criteria compare identity, not spelling.
   - Outside data supplies only what the dandiset lacks, such as a label for
     each cell. The analysis runs on the dandiset's data.
   - `elsewhere` is for a claim whose data the dandiset does not hold at
     all, because the paper deposited them in another public archive (for
     example imaging in the BioImage Archive, proteomics in PRIDE, blots on
     Zenodo). Give the archive and the pinned identifier under `where`.
     Test the claim on those data, listing them under `inputs`, as for any
     other claim. If it cannot be tested here, block it for the reason that
     applies (`too_large`, `not_runnable`, `data_unreadable` and so on),
     never `data_missing`. Data the paper names but that are not public
     anywhere stay `data: dandiset`, blocked with `data_missing`.
   - The notes of a `with_inputs` claim say which side a difference comes
     from as far as the outputs show: whether the dandiset's measures match
     the paper's per-cell values where those are published, and whether the
     outside labels match the paper's counts.
5. Decide now which claims are blocked, and why; a block that depends on a
   selection (too few units under the claim's own rule) is decided once the
   selection is made. Give the main reason under
   `blocked_by` and any others in the notes:
   - `data_missing`: something the claim needs is not in the dandiset and
     not public anywhere else, or for an outside input, not public. When the
     paper deposited it in another public archive, the claim is
     `data: elsewhere` instead (step 4).
   - `metadata_insufficient`: the data are there but cannot be interpreted or
     linked, for lack of a description, label, identifier or mapping.
   - `methods_underspecified`: neither the paper nor its code fixes the
     procedure well enough to repeat it (see also chance levels, under
     "Record the attempt").
   - `data_unreadable` and `too_large`.
   - `not_runnable`: the paper's method cannot be run here, because its
     software cannot be installed in a locked environment or it cannot run
     within the time limit. Say what was tried. For an outside input that is
     public but slow to fetch, use this only when the notebook itself shows
     the fetch does not fit the limit; otherwise test the claim.
   - `other`: say what, for example too few units under the claim's own rule.

   A claim that depends on a blocked claim is blocked for the same reason.

6. Ask when the claims file does not say. When a claim needs something the
   claims file does not give (which trials, which subset, a window, a
   threshold, what a measure is compared with), do not choose it, even when
   you find it in the paper. Add a question to `questions/<dandiset>.yaml`
   (`claim`, `question`, the passage of the paper that bears on it if you
   found one, and why the answer could change the outcome), and test the claim
   under each reading you can see, the passage's among them, or block it as
   `methods_underspecified` until the question is answered. A reader answers from the paper (reader, step 6), and
   a later run, `author-answers`, takes up the answers.

### 2. Check the data against its description

Descriptive metadata is often wrong. For every quantity the analysis uses,
check the description against the values: units and ranges, sampling rates,
counts of subjects, sessions, trials and cells, the size of an arena, which
conditions exist. Show that every data stream shares the clock of the trial
tables, using a contrast between conditions where an overall check cannot
tell a response from an offset (with spikes and a trial table only, decoding
a task variable in windows around the trial start does this; for continuous
sessions, decoding the annotations with the labels shifted in time), and name any
session where this could not be established. A description that a check
supports but does not prove is reported as consistent with the data, not as
shown. Where they disagree, trust the data, say so in the notebook,
and record it as a finding.

### 3. Write the entry

An entry is a directory `entries/<dandiset>-<first author>-<year>/` holding
`entry.yaml`, `requirements.in`, one or more notebooks, and usually a helper
module.

- **Stream the data** from the archive, at a pinned dandiset version. Do not
  download files to disk or read local paths.
- **Compute every result from the data.** No embedded numbers, arrays or
  images, and no figures read from files.
- **Fix every random seed**, and give each claim's section its own generator,
  so that adding a cell earlier does not change its numbers.
- **Put loading and reusable measures in a helper module**, so later notebooks
  on the dandiset can import it. Say in its docstring where a parameter comes
  from: the claim's criterion (which cites the paper or its code), or a
  standard choice for a detail that cannot change a result (say so).
- **Keep it fast.** Reduce the data to what the analysis needs as it loads.
  Aim for under ten minutes; CI fails a notebook over thirty. If the analysis
  runs many small model fits, limit linear-algebra threads to one.

The notebook has these parts, in this order:

1. **Header.** The paper, the dandiset and version, the text the claims file
   was written from, and a table of the claims saying which are tested and which blocked.
2. **Data check.** A cell tagged `sanity` that prints what was loaded: counts
   by subject, session and condition, and the ranges and units of every
   variable used. State each check of the metadata against the data.
3. **One section per tested claim.** Quote the claim. The cells that show the
   result carry the tag `claim:<id>`.
   - Print the numbers the conclusion rests on; a figure alone is not enough.
   - Give the range of every plotted quantity, or say how many points fall
     outside the axes.
   - When cells or trials come from several animals, break the result down by
     animal, or by session when there is one subject.
   - When a threshold or criterion is a choice, show how the result changes
     with it. Give every number its null or reference where the conclusion
     compares it with chance.
   - Report how much was dropped: units, trials, features, and fits that
     failed, did not converge or had nothing to fit.
   - Quote a bound or an effect size for every variant you show, not only the
     main one.
   - End with a short conclusion beginning "**Result: ...**". Every sentence
     in it must be backed by a number printed above it. Analyses run outside
     the notebook, while preparing, may be mentioned as not run here, but
     never decide an outcome or supply a number in the record.
4. **Summary.** A table of all claims and outcomes, how the analysis differs
   from the paper's, and what was found about the dandiset.

### 4. Lock, check and run

```bash
python tools/entry.py lock entries/<name>
python tools/entry.py all  entries/<name>    # check, then run from a clean environment
```

Commit notebooks without outputs. Read the executed copy in
`executed/<name>/` and confirm the conclusions still match the numbers: counts
near a threshold can move when a random split changes.

### 5. Record the attempt

Write `attempts/<entry name>-<nn>.yaml`.

- **One outcome per claim**, including blocked ones. The outcome describes the
  result, not the method:
  - `reproduced`: the result matches the claim.
  - `partially_reproduced`: the effect is present but weaker, or holds only in
    part.
  - `not_reproduced`: the analysis ran and the result differs.
  - `blocked`: the claim could not be tested; give `blocked_by` and say why.
    When the paper states a chance level or false-positive rate for a
    selection, compute it with your procedure. If yours is far from the
    paper's, the procedures differ, and the outcome is `blocked` with
    `methods_underspecified` even though the analysis ran.

  The criterion decides the outcome. Where the claim's statement says more
  than the criterion tests (a p-value, a second condition), the notes say
  whether that part holds.
- **`deviations`**: every way the test differed from the paper's method or
  data. One session of four, a substituted model, a threshold the paper does
  not state.
- **`notes`**: the numbers behind the outcome, stated factually.
- **`measured`**: the value obtained, or one per expected value in the same
  order. When several readings match, record the first reading the criterion
  lists.
- **`proposed`**: on an outcome, a change of outcome found after the last
  verification round, with its `reason` (see "Hand over for verification").
- **`inputs`**: everything used that is not in the dandiset, each with where
  it came from (a DOI, or a repository at a commit).
- **`findings`**: what the attempt found about the dandiset, whatever the
  outcomes. These are for the data owner and the archive. The kinds are
  `metadata_error`, `data_missing`, `identifier_missing`,
  `selection_undocumented`, `methods_unavailable`, `format_error` (files that
  break their own format, such as unsorted spike times), `code_mismatch`
  (published code that disagrees with the paper or the data),
  `paper_inconsistency` (the paper disagrees with itself),
  `metadata_insufficient` (a variable without a description or a needed
  mapping) and `other`.
- **`provenance`**: who is accountable, and for an agent the harness, model
  and this protocol's version.

If any outcome is `not_reproduced` or `partially_reproduced`, the entry's
`README.md` and the notebook's summary carry this sentence: "A failure to
reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method."

### 6. Hand over for verification

Do not verify your own attempt. Give the verifier:

- the executed notebook with the conclusion cells and the summary removed;
- the helper module;
- the claims file.

`python tools/entry.py handover entries/<name>` builds these in
`executed/<name>/handover/` from the executed copy. The verifier also gets the
paper, under `paper/`, but checks the analysis against the claims file. A place
where the claims file misreads the paper is reported, as a question for a
reader; the author does not change the claim.

After the first round, fix what it found, re-run, and hand over the full
executed notebook for the second round. Record each round under
`verifications`, saying what was reviewed. Give the verifier's reasons in its
own words, and what you changed in reply under `response`. An outcome the verifier disagrees
with is either changed, with the reason, or left with the disagreement
recorded.

After round 1 the revision may change outcomes, and round 2 reviews them.
From round 2 on, an outcome may not differ from the one the latest
verification round of that claim agreed with: `tools/entry.py check` fails
if it does. A verifier's result is recorded as it gave it; never change
`agrees` to get past this check. The final
revision corrects text and adds the outputs the verifier asked for. If it
finds that an outcome should change, it keeps the verified outcome and writes
the change under `proposed` on that outcome, with the analysis behind it in
the notebook. A third round then settles it: `verifier-3` reviews only the
proposed changes, and `author-revise-3` applies those it agreed with and
records the round. A change that needs an analysis not yet run waits for a
new attempt.

## Repeat attempts

When a dandiset changes after an attempt, for example after its owners fix
what an attempt found, a new attempt tests the new version. It keeps the
claims file, updates the entry in place to the new version, re-runs every
check and claim, and says for each finding of the earlier attempt whether it
is fixed. Its record is the next number (`-02`), with its own outcomes and
verification rounds; the earlier record stays as it was. A draft can be
used when the fixes are not yet published, with its modification time
recorded, since a draft can change. The author is started with
`-f version=draft` (or a version number), and `docs/agents/author-again.md`
is its prompt.

## Verifier

Be skeptical. Do not assume the analysis is right.

### Round 1: without the author's conclusions

1. Read the notebook, the helper module and the claims file. The paper is
   under `paper/`; the claims file decides what is tested and how, and a place
   where it misreads the paper is reported, not corrected.
2. Check the code: that every number derives from the loaded data; that
   every method choice is the one the claim's criterion gives, and none is
   the author's own; that selection, conditions and analysis windows follow
   the claims file; units; leakage
   between training and test data; the statistics; anything assumed and never
   checked. Test helper functions on synthetic inputs where that is cheap.
3. For each tested claim, decide your own outcome from the notebook's outputs.
4. For each blocked claim, check the archive itself (its file list and
   metadata), not the notebook, and say whether any part could be tested.
5. Report: your outcome and reason for each claim; a list of problems, each
   marked as affecting a conclusion or not; and what you could not check and
   what output would have let you.

### Round 2: with the author's conclusions

1. Say whether you agree with each stated outcome.
2. Check every sentence of the conclusions and the summary against the
   outputs. Quote any that the numbers do not support.
3. Say which of your earlier points are resolved, and list what remains that
   bears on a conclusion.

Take counts of claims and outcomes from the attempt record, not from a
report or a summary table.

### Round 3: proposed changes

Run only when the final revision proposed changes of outcome. Review each
proposal and the analysis behind it as in round 1, and say whether you agree
with the proposed outcome. Nothing else is reviewed.

The verifier does not edit the entry. It does not download the dandiset or
re-run the whole notebook; if a check needs that, it asks for the output to be
added.
