# Protocol for an attempt

Version: `pilot-3`. Record this version in the attempt's provenance.

This is what an agent, or a person, does to attempt a target and deposit the
result. It is written from the first four pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

There are two roles. The **author** makes the attempt. The **verifier** checks
it and must not be the author: for agents, a separate run with a separate
context that has not seen the author's reasoning.

Agent runs are made with the [Agent run](../.github/workflows/attempt.yml)
workflow, one role at a time: `author`, `verifier-1`, `author-revise-1`,
`verifier-2`, `author-revise-2`. Each run's transcript and final report are
kept in [`transcripts/<dandiset>/`](../transcripts).

## Author

### 1. Establish what can be tested

Do this before any analysis.

1. Get the paper. Use the full text when it is open access; otherwise the
   abstract, and say so. Keep any text you download under `paper/`, which is
   not committed. Do not copy figures.
2. List the dandiset's files and read its metadata from the archive. Open a
   file and list everything it holds, including every column of every table.
3. Work out which of the paper's subjects, sessions, conditions and measured
   variables are in the dandiset. A dandiset that names a paper may hold only
   part of its data.
4. Choose the version to pin. Pin the version the paper cites. If it cites
   none, pin the most recent published version, unless an earlier one matches
   the paper better. Say why in the notebook's header. If versions differ in
   content the analysis uses, show the difference.
5. Read the code the paper or the dandiset links to, before writing criteria.
   Say what it holds, and record the repository and commit read. Where the
   Methods leave a choice open and the code settles it, follow the code and
   say so. Where they disagree, follow the Methods for the main result and
   show the code's choice as a variant. Record both as deviations or
   findings.
6. Decide what comes from outside the dandiset. Data from elsewhere may be
   used only when the paper itself compares its data with something taken
   from elsewhere (a model, a reference dataset), it is public, and it is
   pinned: a DOI, or a repository at a commit. Record each under `inputs` in
   the attempt. A claim whose outside input is not public is blocked with
   `data_missing`, and its notes say where you looked.
7. Write the claims file, `claims/<dandiset>/<doi with / replaced by ->.yaml`.
   - One claim per finding, at the level of a figure panel or a reported
     number when the full text is available. Cover the paper's main findings,
     including those the dandiset cannot test.
   - `statement`: the finding in words. `source`: where the paper shows it.
   - `expected`: each reported number the claim rests on, with a tolerance.
     Use the paper's own uncertainty when it gives one (a confidence
     interval, or the stated spread); otherwise 10% of the reported value.
     Give the reason for any other tolerance.
   - `criterion`: how the claim will be judged, for any claim that is not
     settled by its expected values alone ("similar", "many", "tended to").
     Write it before running the analysis of that claim. The data check may
     come first; say in the file's opening comment what results you had seen
     when you wrote the criteria.
   - When a reported number can be read in more than one way (which trials
     form the denominator, which subset is meant), list in the criterion the
     readings the paper's text plausibly allows, before the analysis. The
     claim is reproduced if the result matches under any of them. The
     notebook shows every reading, the notes say which ones match, and the
     ambiguity is recorded as a deviation.
   - For a claim of absence ("no difference", "did not change"), the
     criterion names the test and threshold the paper used. The claim is
     reproduced when that test does not find the effect and not reproduced
     when it does; give the size of the effect either way.
   - `depends_on`: the claims whose result this one uses, such as the cells
     another claim selects.
8. Decide now which claims are blocked, and why. Give the main reason under
   `blocked_by` and any others in the notes:
   - `data_missing`: something the claim needs is not in the dandiset, or for
     an outside input, not public. Say whether it exists elsewhere.
   - `metadata_insufficient`: the data are there but cannot be interpreted or
     linked, for lack of a description, label, identifier or mapping.
   - `methods_underspecified`: neither the paper nor its code fixes the
     procedure well enough to repeat it (see also chance levels, under
     "Record the attempt").
   - `data_unreadable` and `too_large`.
   - `other`: say what, for example too few units under the claim's own rule.

   A claim that depends on a blocked claim is blocked for the same reason.

### 2. Check the data against its description

Descriptive metadata is often wrong. For every quantity the analysis uses,
check the description against the values: units and ranges, sampling rates,
counts of subjects, sessions, trials and cells, the size of an arena, which
conditions exist. Show that every data stream shares the clock of the trial
tables, using a contrast between conditions where an overall check cannot
tell a response from an offset (with spikes and a trial table only, decoding
a task variable in windows around the trial start does this), and name any
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
  from: the paper's methods, or a common choice when the methods were not
  available.
- **Keep it fast.** Reduce the data to what the analysis needs as it loads.
  Aim for under ten minutes; CI fails a notebook over thirty. If the analysis
  runs many small model fits, limit linear-algebra threads to one.

The notebook has these parts, in this order:

1. **Header.** The paper, the dandiset and version, whether the full text was
   used, and a table of the claims saying which are tested and which blocked.
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
     in it must be backed by a number printed above it.
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
- **`inputs`**: everything used that is not in the dandiset, each with where
  it came from (a DOI, or a repository at a commit).
- **`findings`**: what the attempt found about the dandiset, whatever the
  outcomes. These are for the data owner and the archive. The kinds are
  `metadata_error`, `data_missing`, `identifier_missing`,
  `selection_undocumented`, `methods_unavailable`, `format_error` (files that
  break their own format, such as unsorted spike times), `code_mismatch`
  (published code that disagrees with the paper or the data),
  `paper_inconsistency` (the paper disagrees with itself) and `other`.
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
`executed/<name>/handover/` from the executed copy. The verifier gets the
paper itself, from its DOI.

After the first round, fix what it found, re-run, and hand over the full
executed notebook for the second round. Record each round under
`verifications`, saying what was reviewed. Give the verifier's reasons in its
own words, and what you changed in reply under `response`. An outcome the verifier disagrees
with is either changed, with the reason, or left with the disagreement
recorded.

## Verifier

Be skeptical. Do not assume the analysis is right.

### Round 1: without the author's conclusions

1. Read the notebook, the helper module and the relevant parts of the paper.
2. Check the code: that every number derives from the loaded data; that
   selection, conditions and analysis windows follow the paper; units; leakage
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

The verifier does not edit the entry. It does not download the dandiset or
re-run the whole notebook; if a check needs that, it asks for the output to be
added.
