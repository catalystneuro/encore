# Pilot notes

What each pilot attempt taught about the process. These feed the revision of
the schemas and the design after the pilot (docs/design.md, "Phasing").

The notes on each attempt are in [`pilot-notes/`](pilot-notes), one file per
attempt, named by its record. The lists below link those written before
2026-10-22, under the protocol version they ran under; the recorder adds a file
for each attempt since, and does not change this page.

- [000582, Sargolini et al. 2006 (2026-10-13)](pilot-notes/000582-sargolini-2006-01.md)
- [000127, Chowdhury, Glaser & Miller 2020 (2026-10-13)](pilot-notes/000127-chowdhury-2020-01.md)
- [000207, Zheng et al. 2022 (2026-10-13): first attempt by an agent following the protocol](pilot-notes/000207-zheng-2022-01.md)
- [000147, Guan et al. 2022 (2026-10-13): second attempt by an agent following the protocol](pilot-notes/000147-guan-2022-01.md)

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

- [001097, Liu et al. 2024 (2026-10-14): first attempt under pilot-3, entirely in Actions](pilot-notes/001097-liu-2024-01.md)

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

- [000625, Geiller et al. 2020 (2026-10-14): first attempt under pilot-4](pilot-notes/000625-geiller-2020-01.md)

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

- [000035, Scala et al. 2021 (2026-10-14): first attempt under pilot-5](pilot-notes/000035-scala-2021-01.md)
- [001453, Fouke et al. 2025 (2026-10-14): the last pilot target](pilot-notes/001453-fouke-2025-01.md)

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

- [000006, Economo et al. 2018](pilot-notes/000006-economo-2018-01.md)
- [001754, Knierim, McNaughton and Poe 2000](pilot-notes/001754-knierim-2000-01.md)
- [000130, Sohn, Narain, Meirhaeghe and Jazayeri 2019](pilot-notes/000130-sohn-2019-01.md)
- [001616, Gerken et al. 2025](pilot-notes/001616-gerken-2025-01.md)
- [001754 again, on the fixed draft (2026-10-15)](pilot-notes/001754-knierim-2000-02.md)
- [002014, Choi et al. 2025](pilot-notes/002014-choi-2025-01.md)
- [001933, Chen et al. 2026](pilot-notes/001933-chen-2026-01.md)

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

- [000004, Chandravadia et al. 2020](pilot-notes/000004-chandravadia-2020-01.md)
- [002013, Amjad et al. 2025](pilot-notes/002013-amjad-2025-01.md)
- [001636, Pasquereau et al. 2013](pilot-notes/001636-pasquereau-2013-01.md)
- [001933 again, Chen et al. 2026, under pilot-7 (2026-10-15)](pilot-notes/001933-chen-2026-02.md)
- [000041, Watson et al. 2016](pilot-notes/000041-watson-2016-01.md)
- [000003, Senzai et al. 2017](pilot-notes/000003-senzai-2017-01.md)
- [000044, Grosmark et al. 2016](pilot-notes/000044-grosmark-2016-01.md)
- [000056, Peyrache et al. 2015](pilot-notes/000056-peyrache-2015-01.md)
- [000059, Petersen et al. 2020](pilot-notes/000059-petersen-2020-01.md)
- [000061, Girardeau et al. 2017](pilot-notes/000061-girardeau-2017-01.md)
- [000067, Fujisawa et al. 2008](pilot-notes/000067-fujisawa-2008-01.md)
- [000070, Churchland et al. 2012](pilot-notes/000070-churchland-2012-01.md)
- [000121, Even-Chen et al. 2019](pilot-notes/000121-even-chen-2019-01.md)
- [000114, Carcea et al. 2021](pilot-notes/000114-carcea-2021-01.md)
- [000213, Tingley et al. 2018](pilot-notes/000213-tingley-2018-01.md)
- [000218, Tingley et al. 2019](pilot-notes/000218-tingley-2019-01.md)
- [000226, Severson et al. 2017](pilot-notes/000226-severson-2017-01.md)
- [000232, Chang et al. 2023](pilot-notes/000232-chang-2023-01.md)
- [000239, Xu et al. 2022](pilot-notes/000239-xu-2022-01.md)
- [000350, Mu et al. 2019](pilot-notes/000350-mu-2019-01.md)
- [000409, International Brain Laboratory et al. 2025](pilot-notes/000409-ibl-2025-01.md)
- [000552, Huszar et al. 2022](pilot-notes/000552-huszar-2022-01.md)
- [000568, Valero et al. 2022](pilot-notes/000568-valero-2022-01.md)
- [000559, Markowitz et al. 2023](pilot-notes/000559-markowitz-2023-01.md)
- [000718, Zaki et al. 2024](pilot-notes/000718-zaki-2024-01.md)
- [000691, Scherrer et al. 2023](pilot-notes/000691-scherrer-2023-01.md)
- [000727, Brezovec et al. 2022](pilot-notes/000727-brezovec-2022-01.md)
- [000947, Schwab et al. 2020](pilot-notes/000947-schwab-2020-01.md)
- [000971, Seiler et al. 2022](pilot-notes/000971-seiler-2022-01.md)
- [001038, Azcorra et al. 2023](pilot-notes/001038-azcorra-2023-01.md)
- [001075, Randi et al. 2023](pilot-notes/001075-randi-2023-01.md)
- [001084, Vu et al. 2024](pilot-notes/001084-vu-2024-01.md)
- [001170, Ling et al. 2023](pilot-notes/001170-ling-2023-01.md)
- [001172, Lohani et al. 2022](pilot-notes/001172-lohani-2022-01.md)
- [001528, Hadjas et al. 2025](pilot-notes/001528-hadjas-2025-01.md)
- [001538, Zhai et al. 2025](pilot-notes/001538-zhai-2025-01.md)
- [001550, Pagan et al. 2025](pilot-notes/001550-pagan-2025-01.md)
- [001692, Bouabid et al. 2026](pilot-notes/001692-bouabid-2026-01.md)
- [001699, Moore et al. 2025](pilot-notes/001699-moore-2025-01.md)
- [001878, Sun et al. 2021](pilot-notes/001878-sun-2021-01.md)
- [001712, Davatolhagh et al. 2025](pilot-notes/001712-davatolhagh-2025-01.md)
- [001888, Hristova et al. 2025](pilot-notes/001888-hristova-2025-01.md)
- [000005, Yu et al. 2016](pilot-notes/000005-yu-2016-01.md)

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

- [001754, Knierim et al. 2000, third attempt](pilot-notes/001754-knierim-2000-03.md)
- [crcns-ret-1, Lefebvre et al. 2008](pilot-notes/crcns-ret-1-lefebvre-2008-01.md)
- [000005, Yu et al. 2016, second attempt](pilot-notes/000005-yu-2016-02.md)
- [000061, Girardeau et al. 2017, second attempt](pilot-notes/000061-girardeau-2017-02.md)
- [000582, Sargolini et al. 2006, second attempt](pilot-notes/000582-sargolini-2006-02.md)
- [000009, Guo et al. 2017](pilot-notes/000009-guo-2017-01.md)
- [000008, Scala et al. 2021](pilot-notes/000008-scala-2021-01.md)
- [000010, Li et al. 2015](pilot-notes/000010-li-2015-01.md)
- [000691, Scherrer et al. 2023, second attempt](pilot-notes/000691-scherrer-2023-02.md)
- [001636, Pasquereau et al. 2013, second attempt](pilot-notes/001636-pasquereau-2013-02.md)
- [000006, Economo et al. 2018, second attempt](pilot-notes/000006-economo-2018-02.md)
- [000011, Li et al. 2016](pilot-notes/000011-li-2016-01.md)
- [000013, Hires et al. 2015](pilot-notes/000013-hires-2015-01.md)
- [000015, Chen et al. 2017](pilot-notes/000015-chen-2017-01.md)
- [000019, Bouchard et al. 2013](pilot-notes/000019-bouchard-2013-01.md)
- [000034, Buccino et al. 2020](pilot-notes/000034-buccino-2020-01.md)
- [000128, Churchland et al. 2010](pilot-notes/000128-churchland-2010-01.md)
- [000036, Mayner et al. 2022](pilot-notes/000036-mayner-2022-01.md)
