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

### 000019, Bouchard et al. 2013

One claim reproduced, one partially, four not reproduced and sixteen blocked,
all on the dandiset. It pins version 0.220126.2148, the only published
version, as the paper cites none. The claims were written from the NIH author
manuscript with its supplement, without a PDF of the main text, so the main
figures were read from their legends and the Results; the claims check made
ten changes and left the file at 22 claims. The author put five questions to a
reader; four answers were that the paper does not say, which added readings
(both z-scorings and two inputs to project for the state-space claims, every
CV or only those with 15 or more renditions, the rest period as baseline
reading (c)), and the fifth was that positions cannot be derived from grid
geometry, unlabelled coordinates or atlas labels. The answers moved
`active-electrodes` and `fig4a-consonant-clusters` from not reproduced to
blocked as `methods_underspecified`; the author's reports give the totals as 7
and 13 before and 5 and 15 after, which their own per-claim tables do not add
up to. Round 1 gave its own outcome for each claim from the notebook with its
conclusions and summary removed and agreed with all 22, and round 2 agreed
with all 22, so there was no third round. The paper, "Functional organization
of human sensorimotor cortex for speech articulation" in Nature, records
high-density ECoG over ventral sensorimotor cortex (vSMC) of three subjects
reading consonant-vowel syllables aloud, and reports a dorsal-to-ventral
layout of the lips, jaw, tongue and larynx representations, a staggered
timing of articulator activity, and a cortical state-space whose clusters
follow the articulators and phonetic features. The data composition, active
electrode counts, the phonetic contrasts at single electrodes, mixed tuning,
timing, the state-space analyses and the PC articulator weights were tested.
`fig1c-e-articulator-electrodes` and the seven spatial claims are blocked as
`metadata_insufficient`, and the seven state-space claims and
active-electrodes as `methods_underspecified` because their readings disagree.
`fig1f-h-phonetic-contrasts` is not reproduced because no lips-positive GLM
electrode has /ju/ above 2 with /ja/ and /ji/ below 2 under any of 96
readings, `fig3d-timing-sequence` because tongue onsets are -26 to +290 ms
and none of the three order conditions holds in any of 96 readings,
`fig5c-separability-timing` because the consonant peak is at -155 to +15 ms
against -200, and `suppfig9-pc-articulator-weights` because tongue weights
are not above lips (corrected p = 1) and jaw and larynx differ at p = 5e-11 in
all 288 readings. Some outcomes rest on weak ground: `suppfig6-mixed-tuning`
is reproduced under a criterion that holds on weights permuted across
electrodes in 94 of 96 readings; the one active-electrodes reading within
tolerance (rest, 15+ CVs, 27.0) rests on trials the files mark as ECoG
artifacts, and without them GP31's count falls from 31 to 2; the split there
comes from GP31's /thi/, with 2 renditions; and `suppfig13-consonant-vowel-distance`
stays blocked only because the attempt counts a reading where the orderings
hold but the pair count is 4677 or 4567 against 4623 as partial, while read
strictly every reading is not reproduced. Three questions on suppfig13,
suppfig6 and suppfig9, where round 2 thought the claims file may misread the
paper, are unanswered.

No electrode has a position relative to the central sulcus or the Sylvian
fissure, the frame of the paper's spatial analyses: EC2 and GP31 have x, y, z
coordinates with no unit or frame, GP33 and EC9 have none, and no electrode is
labelled as on the guenon, so seven spatial findings cannot be tested. The
microphone recordings were removed, so the acoustic onset, peak and offset of
each syllable cannot be computed and the hand-marked syllable start stands in
for the onset as a recorded deviation; there is no high gamma either, so it is
computed from the raw 256-channel ECoG at 3051.76 Hz. Subjects GP31 and GP33
do not carry the paper's names (EC31, EC33) and nothing links them; the
subject fields hold only species and id, the electrode group of EC2 and GP31
is `L256Grid electrodes` and that of GP33 `auto_group`, with location
`location`, so the right hemisphere of EC33 cannot be checked. A fourth
subject, EC9 (7 blocks, 1653 trials), is not in the paper. Renditions per
syllable range from 2 to 107 against the paper's 15 to 100, GP31 lacks /tha/
and /thu/, and the three subjects have 169 distinct syllables against 168,
with nothing saying which trials or syllables the paper used. The raw
ElectricalSeries gives unit volt with a conversion factor of 0.001, but the
stored values are consistent with being already in volts. Other findings: two
syllable labels are misspelt (`she` for `shee`, `ha` for `haa`); electrode ids
start at 0 in EC2 and GP31 and at 1 in GP33 and EC9; bad-channel flags differ
between blocks of one subject; 162 of 9370 analysed trials overlap intervals
marked as ECoG artifacts; and one file (EC2 block 1) holds a power spectrum of
the 256 channels in a processing module. The paper links no code, and the
articulator and phonetic feature matrices, which exist only as supplement
figures, were transcribed and listed under `inputs`.

The notebook ran in about 14.5 minutes in the first run, 17.2 minutes after
the answers, 21 minutes after round 1 and 20.7 minutes after round 2, and
`entry.py all` passed with 0 errors each time. Streaming with remfile was too
slow, so each file was fetched whole into memory with parallel range
requests, 39.0 GB in all, and a bootstrap rewritten as one matrix product,
about 20 times faster, kept the notebook under 30 minutes; the author could not
remove an empty `.claude/.cc-writes` directory the harness created in the
entry. Round 1's points led to a listing of every file's objects in place of a
hard-coded line, a fix to the separability bootstrap, which had paired tokens
with their own copies, a corrected artifact trial count of 162 in place of
177, outcome counts per reading factor, artifact-free variants for
active-electrodes and fig3d, a permutation null for suppfig6 and the
transcribed matrices drawn for checking. Round 2 found statements the outputs
did not support, among them a GP31 comparison in fig2a where GP31 has no
tongue window, fig5d's split put down to the four reading details where it
comes from the readings of R and of the clusters, a README run time with 42
GB streamed where 39.0 GB is printed, and 24 consonant labels for EC9 where
there are 23, and these were corrected. Untracked dotfiles and a `scripts`
folder in the repository root that the author did not create were left alone.
The author's points on the protocol: blocking a claim that depends on a
blocked claim does not fit fig1f-h, suppfig6 and suppfig9, which use only
fig2a's position-free weights; readings added through a question multiply all
the others, so several claims are blocked only because readings disagree; a
baseline taken from the dataset and not the paper's text fits only as a
variant; the notebook header template uses bold labels against the no-bold
rule; the archives doc's advice to stream with remfile is too slow for these
files; the articulator and phonetic feature matrices exist only as figures
and were transcribed from the PDF into the helper module; and there is
no format for a claims file that leaves "pre-epoch level" undefined.

### 000034, Buccino et al. 2020

No claim reproduced, one partially, none not reproduced and 22 blocked, all
on the dandiset; the link claim `recordings-as-described`, which the table
does not count, reproduced with all 15 of its checks holding. It pins version
0.211030.0713, the only published version, with the same six files as the
draft, which is all the paper cites. The claims check required every
reading to agree in five claims where the draft had accepted any one, and
left the file at 24 claims. The author asked no questions, as the one tested
claim was fully specified, so the answer steps changed nothing. Round 1 gave
its own outcome for each claim from the notebook with its conclusions and
summary removed and agreed with 23 of 24; it gave `fig4a-curators-agree` as
at least partially reproduced where the author had blocked it as dependent on
the blocked `fig1b-unit-counts`, and the author changed it. Round 1 also held
that `not_runnable` is not an allowed reason and gave the blocked claims as
`other`; the author kept `not_runnable`, which the schema and protocol define
for software that cannot be installed in a locked environment, and round 2
withdrew the point. Round 2 agreed with all 24, so there was no third round.
The paper, "SpikeInterface, a unified framework for spike sorting" in eLife,
runs six spike sorters on a Neuropixels recording from mouse 412804, a
simulated MEArec recording with 250 ground-truth units, a rat cortex
recording and a mouse retina recording, and reports that the sorters agree
poorly, that Kilosort2 scores highest on the simulation, that almost all
false positive units are found by a single sorter, and that consensus units
match the two experts' curations of the Kilosort2 output. Only the recordings
and the agreement of the two curators could be tested: the curators share 226
of 351 units (64.39%), within tolerance of the paper's 226, 351 and 64.2%,
while the 174 Kilosort2 units both discarded need the paper's Kilosort2 run
and are untested. The ratio leaves its tolerance at a minimum score of 0.8
(56.79%), which does not decide the outcome, as the criterion fixes the
default of 0.5. Every other claim needs the sorters' output, and Kilosort2,
IronClust and HDSort are MATLAB programs (Kilosort2 also needs a CUDA GPU)
that cannot be installed from a lock file on a runner with no MATLAB, GPU or
MPI.

The dandiset holds no output of the six sorters, including the Kilosort2 run
the two experts curated, so every comparison of sorters can be repeated only
by running them again, three of them in MATLAB, and a new Kilosort2 run will
not give the units the curators worked on. The two curated files hold a Units
table of ids and spike times only, with no sampling rate, no unit labels, no
curator name and no link to the Kilosort2 clusters, and nothing says which
file is curator 1 (they differ only by session time, 15:55:42 and 15:55:43);
their spike times fall on whole frames at 30 kHz and match the mouse
recording's clock. The retina recording is stored as unsigned 16-bit values
centred near 2048 and reaching 4096, consistent with raw counts of a 12-bit
converter, while the file states a conversion of 1e-6 V per unit and no
offset, which would put every channel near +2 mV. The mouse recording stores
int16 values with a conversion of 1e-6 V and no gain or channel_conversion;
read that way its band-passed noise SD is about 50 uV and the median curated
trough about 455 uV, several times usual Neuropixels levels, and the values
are consistent with raw counts, though the file holds nothing to show which.
Other findings: the electrode tables give location 'unknown' and filtering
'none' for every channel; the mouse recording has 248 channels where the
paper says 246 are active, without marking which; the simulated file does not
say which ground-truth cells are excitatory or inhibitory or what noise was
added; the archive's species summary lists only house mouse though one
recording is from a rat; every raw series is stored in chunks of one channel
by 7911 to 26368 frames, so reading a whole recording chunk by chunk through
h5py would take 6.2 to 16.9 h in this run, against 1.4 to 6.5 min at the 72
MB/s of one bulk ranged read; and the paper gives 226 of 351 as 64.2%, where
it is 64.39%.

The notebook ran in 288 s in the first run; an exploratory listing of the
metadata had timed out at 20 minutes, and targeted reads replaced it;
HerdingSpikes 0.3.7 failed to build and SpyKING Circus had no MPI to run
with, and spikecomparison 0.2.6 and spikeextractors 0.8.4 ran on NumPy 2 with
five removed aliases restored, a recorded deviation. Round 1's points led to
the HDF5 trees of the curated files and the mouse recording, a timed bulk
read so that reading time is no longer part of the block, the mouse electrode
columns with a finding on its conversion, and the MEArec spectrum, which shows
the traces are not band-passed at 300 Hz. Round 2 found statements the
outputs did not support, among them read times from an earlier run, a
Summary that ruled out microvolts for the mouse values, a minimum-score scan
that left out the ratio falling out of tolerance at 0.8, three claims that
need Kilosort2 alone described as needing all six sorters, and a species
summary and pip results that no cell printed; these were corrected, with the
read times taken from the final run, as they vary between runs. Untracked
empty files in the repository root that the author did not create were left
alone. The author's points on the protocol: the rule that blocks a claim
depending on a blocked claim forced fig4a to blocked though its curator
counts were computed, and there is no outcome for a claim tested only in
part; `not_runnable` and `too_large` overlap when sorting software cannot
run; the protocol says nothing about restoring names removed from libraries,
which the paper-era spikecomparison and spikeextractors need on NumPy 2; and
the 10-minute aim is hard to meet when checking the data needs slow raw
reads, so only the first chunk of each recording was read.

### 000128, Churchland et al. 2010

Eleven claims reproduced, one partially, three not reproduced and seven
blocked, all on the dandiset. It pins version 0.220113.0400, the only
published version, whose draft holds the same two files with identical
contents. The claims were written from the PubMed Central author manuscript
and its supplement, without a PDF of the main text, so the main figures were
read from their legends; the claims check added
`fig4-no-separate-populations`, so the file has 22 claims. The author put three
questions to a reader, and the answers set aside the proto-trial reading T1
(which kept 73.8% of trials with delay over 400 ms and left two conditions
empty) and the tuning measure S2 (which selected no neuron for the correlation
claims), and named two readings of the normalising maximum in
`suppfig1-population-averages`, both already run. The counts moved from 7, 1, 2
and 12 to 11, 1, 3 and 7: `fig3-maze-most-not-maintained`,
`fig6-peri-movement-space-best`, `fig6-each-dimensionality` and
`fig7a-shuffled-space-poor` moved from blocked as `methods_underspecified` to
reproduced, and `fig6-performance-vs-dimensionality` to not reproduced. Round 1
gave its own outcome for each claim from the notebook with its conclusions and
summary removed and agreed with all 22, and round 2 agreed with all 22, so
there was no third round. The paper, "Cortical preparatory activity:
representation of movement or first cog in a dynamical machine?" in Neuron,
records units in PMd and M1 of three monkeys making delayed reaches in a speed
task and a maze task, with single electrodes and, for monkey J, two
96-electrode arrays, and reports that preparatory and peri-movement tuning are
only weakly correlated and that preparatory tuning is best captured by a
preferred direction in the space of the population's peri-movement response.
Only the J-array maze session could be tested: its counts, the tuning
correlations and their time course, the population averages, the PD spaces,
the controls and the two model simulations. The speed task, single-electrode
and EMG claims are blocked as `data_missing`, and the two anterior-posterior
claims as `metadata_insufficient`. `fig4d-mean-correlation-jarray` is not
reproduced because the mean r is 0.051 and the mean Spearman r 0.072 against
0.13 and 0.11, with no test below p = 0.05 (P1 0.47, P2 0.42, P3 0.61),
`fig6-performance-vs-dimensionality` because performance rises to its best at
k = 14 (0.518) and does not decline, and `prep-dimensionality` because 90% of
the variance needs 15 components (N1) or 18 (N2) against 7 to 11; the main
text says "at least 7-10 dimensions", which 15 and 18 would meet, and whether
the claim is a range or a lower bound is asked in a question. Some outcomes
rest on weak ground: the correlation claims use only 17 neurons that pass the
selection, so their tests have little power; fig3 rests on one neuron, unit
1581 (r 0.765), with the next largest r 0.457; the best k in the PD analyses
is the upper end of the tested range, an edge value and not a peak; the
preparatory separation in suppfig1 is positive by construction; and
`fig8-model-weak-correlation` has a criterion that almost any small value
would pass.

The dandiset holds only the J-array session of monkey Jenkins (2009-09-25),
with no speed task, no single-electrode recordings and no EMG, and the paper
names no other archive for them. Every unit's electrode reference points into
the first 96 rows of the electrodes table, labelled PMd, so by the file all
182 units are in PMd although the electrode groups describe one array in M1
and one in PMd; the reference equals the unit id's channel digits minus one,
which suggests the array offset was dropped in conversion. The electrodes have
no coordinates (x, y and z are NaN), and the leading digit of the unit ids (1
for 92 units, 2 for 90), which may be the array, is not documented, so no unit
can be placed on the anterior-posterior axis or on an array; regressing tuning
correlation on that digit, a variant that decides nothing, gives r of
magnitude 0.432 (p 0.084). The dataset holds 182 units where the paper reports
146 and does not record which units or trials the paper used, or that this
session is the paper's. 574 of the session's successful trials are in the test
file as 0.7 s segments around movement onset, without condition labels or
behaviour and with only the 137 held-in units, so they cannot enter a
condition-mean analysis; the test file has a clock of its own and no delay or
success column, and the train file's trial ids are contiguous, so the files do
not record which session trials the packaging dropped. Reading (a) of
`recordings-jarray` gives 2869 trials with the test file and 2295 without it,
and the 182 units fail under every reading. Other findings: 14 trials have a
negative delay (as low as -3 ms), where the go cue precedes the recorded
target onset.

The notebook ran in 152 s in the first run, 81 s after the answers and 121 s
after round 1, and `entry.py all` passed with 0 errors after round 2. A bug
found during development averaged an empty condition as zero rates and had
made fig4d look reproduced (mean r 0.117); with the fix it is not reproduced.
Round 1's points led to a table labelled by reading for `recordings-jarray`, a
per-neuron table for fig4d, the lost fig6-each-dimensionality comparison (the
2-D initial-velocity space, 0.238 against 0.223) printed, and checks of the
test file's clock and the electrode group descriptions. Round 2 withdrew its
round-1 point that the supplement's T-matrix might be a conditions by
(neurons by times) matrix, as the supplement defines it as c by n, so those
variants were removed; it also found statements the outputs did not support,
among them both fig4d means called below half the paper's where the Spearman
mean is 65% of it, the fig8 interval given as its outer envelope, an ambiguous
"91% of trials kept" for T2, and notes quoting T1 and S2 values the notebook
no longer prints, and these were corrected. Untracked dotfiles in the
repository root that the author did not create were left alone. The author's
points on the protocol: it does not cover a reading that selects no units; it
does not say what to do when a trial reading leaves a condition with no
trials; it has no rule for an undocumented substitute such as the unit-id
digit when the claims file's fallback, the array, is wrong in the data; its
check for a selection is written only for chance levels and false-positive
rates, though the paper's "~90% kept" works like one; the `recordings-jarray`
criterion says only when the claim is reproduced, not when it is partial; and
some details the criteria leave open below their stated readings were run both
ways and recorded as deviations.

### 000036, Mayner et al. 2022

Fourteen claims reproduced, one partially, one not reproduced and five
blocked on the dandiset, with one more reproduced and four more blocked on the
dandiset together with the paper's Zenodo deposit. It pins version
0.230515.1917. The claims were written from the full text of the version of
record as served by Europe PMC, without the Extended Data images; the claims
check found 0 problems in 26 claims and made the design-sessions criterion
count a dataset of the 44 analysed sessions as reproduced, and the author added
the link claim `session-link`, so the file has 27 claims. The author asked no
questions, so the answer steps changed nothing. Round 1 gave its own outcome
for each claim from the notebooks with their conclusions and summaries removed
and agreed with 26 of 27; it gave `design-sessions` as reproduced, as the
paper's 45 sessions are all present with its counts, and the author changed it
from partially reproduced. Round 1 also gave `other` as the reason for the
five L0 event claims, where the author kept `not_runnable`, which round 2
accepted. Round 2 agreed with all 27, so there was no third round. The paper,
"Measuring Stimulus-Evoked Neurophysiological Differentiation in Distinct
Populations of Neurons in Mouse Visual Cortex" in eNeuro, images excitatory
neurons of L2/3, L4 and L5 in five visual areas of nine mice (Cux2, Rorb and
Rbp4 lines) shown 12 natural and artificial movies, and reports that
unscrambled movies evoke higher neurophysiological differentiation (ND) than
phase-scrambled ones specifically in L2/3 of AL and AM. The session design, cell counts, the layer and
area effects, the sensitivity analysis, the permutation table, the locomotion
correlation, the per-session effect sizes, multivariate ND, decoding, the
stimulus effects and the stimulus differentiation correlations were tested.
The five claims on L0 events are blocked as `not_runnable`, as the named
detector cannot be installed, the three that need the Methods' pupil diameter
as `data_missing`, and `ext8-1-no-low-level-relation` as
`methods_underspecified`, as spectral energy has p = 0.044 and 0.033
one-sided and 0.087 and 0.066 two-sided. `ext3-2-sensitivity` is not
reproduced because 36 of 108 parameter sets (33.3%) meet the agreement rule
against 90% and 80%, but the same rule gives 28 of 108 (25.9%) on the paper's
own outputs, so round 2 read the outcome as reflecting the claims file's
reading of "nearly all" more than the data; `discussion-session-effect-sizes`
is partially reproduced because the largest per-session d is 1.111 against
1.25 +/- 0.125 under the Methods' pooled SD, while the code's SD gives 0.584
to 1.194 and a pooled 0.343, all within tolerance. Some outcomes rest on weak
ground: in `fig3b-area-specific` AM d is 0.132 against the paper's printed
0.268, and the criterion's rule rests on the significance pattern, which
holds; the `session-link` criterion was written after the 7 hour offset was
found; and three questions to a reader, on the ext3-2 agreement rule, the
pooled SD and the AM d of 0.268, are unanswered.

The dandiset holds 57 sessions where the paper analysed 44 and excluded one:
the 12 extra sessions (second recordings of each area in Cux2 mice 389014 and
389020, and a second PM session in Rbp4 mice 402796 and 405808) are not
described in the paper, nothing in the files or the metadata says which
sessions the paper used or that the L5 AL session 741889312 was excluded, and
run on all 56 complete sessions the area result changes (AL no longer
significant, p = 0.072). The NWB identifier is not the session id the paper
and its code use (for example 717235570 against 717911143), so the sessions
can be linked to the paper only by start time, and session_start_time is 7
hours later than the paper's metadata in all 57 files while labelled -07:00,
which looks like UTC labelled as Pacific time. With that link the dandiset's
dF/F gives the paper's per-trial ND to a relative 1e-6 in all 5280 trials,
and the stimulus movies equal the paper's. Against the 2p frame times the NWB
stimulus and running timestamps run late by an amount that grows through each
session, from about 0 frames in the first minute to 1.3 to 4.4 frames (40 to
146 ms) in the last, so the paper's trials start 0 to 6 frames earlier than
the NWB stimulus times give. The dandiset holds no L0 calcium events, no eye
tracking or pupil data and no sex, age or date of birth; the events and pupil
area are in the paper's Zenodo deposit, the fitted pupil ellipse whose
semi-major axis the Methods define as the diameter is in neither, and the L0
detector the paper names is Python 2 code that needs the compiled
FastLZeroSpikeInference, which is not on PyPI, does not build with pip from
its repository and no longer has the arfpop function the detector calls. 15
ROIs (14 in the paper's sessions) have dF/F that is NaN at every frame with no
flag, and without them the cell counts equal the paper's. Other findings:
every running_velocity series has one sample more than its timestamps, the
first, which in one session is an artifact of -742.7 cm/s; in 39 of 57 files
the dF/F timestamps have one entry more than the data has frames; the imaging
plane states 30.0 Hz where the frames step by 33.17 ms (30.15 Hz), and by
66.33 ms (15.08 Hz) in the excluded session; the paper's AM d of 0.268 looks
like a transcription slip, as its own per-trial values give 0.128 with the
code's pooled SD; the code's pooled SD weights each group's SD by the other
group's n - 1, which gives the paper's 0.57 to 1.25 where the Methods' formula
gives 0.592 to 1.155; and in the paper's own sensitivity statistics AL and AM
are both significant in 28 of 108 sets, AL alone in 50, AM alone in 24 and
neither in 6.

The author's session took about 3.5 hours, and the final entry run 44
minutes, 12, 12 and 20 minutes for the three notebooks; during development
degenerate lbfgs fits gave a NaN chi2 for ext3-1 and changed the sensitivity
count from 33 to 36 until such fits were rejected, an off-by-one in the
running samples broke the first arousal run, and a data-check cell failed on
the half-rate session. The arousal notebook read the 4.5 GB Zenodo deposit as
one gzip tar against a 26-minute deadline; in the run after the answers the
deadline came first (1527 s and 1467 s), so the executed copy lacked reading
(b) of `fig4-locomotion-effect-size`, until after round 1 the deposit was
fetched over parallel byte-range requests (217 s in the run round 2 reviewed,
176 s in the last). Round 1's points led to the code's pooled SD, which
reproduces the paper's effect_size.parquet to 4e-15 in all 44 sessions, a
comparison of the sensitivity spectra with the paper's per-trial ND (relative
1.1e-14 in six sets, r = 0.993 to 0.9999 over all 108), the Figure 7 tests on
the paper's own data, listings of the NWB files and of the deposit's
data/eye/, a section printing why the detector's sources cannot be installed,
and the three questions to a reader. Round 2 found statements the outputs did
not support, among them decoding said to fall below chance (about 0.04) where
0.085 is printed, a compiler rejection no cell showed, a patched build of the
detector outside the notebook that the record did not mention, sensitivity
counts on the paper's outputs that no cell printed, and a deposit time of 210
s against 217 s printed; these were corrected, and the record now says the
patched build ran arfpop on a synthetic trace but computed no events. One
ext3-2 conclusion sentence was edited after the last run, so the executed copy
still shows the old wording. Untracked files in the repository root that the
author did not create were left alone. The author's points on the protocol:
the design-sessions criterion did not anticipate a dataset with more sessions
than the paper; `with_labels` is defined for code names and was used for the
paper's session selection; the protocol does not say when a link criterion
must be fixed; an expected value can fall outside tolerance while the
criterion's rule holds; reading a single gzip tar in order makes one reading's
availability depend on network speed; it does not say which block reason comes
first when one reading's input is not public and the computable readings
disagree; the discussion criterion has no partial rule; it does not cover a
claims-file reading that the paper's own outputs fail; it does not say who
sets a claim's `data` field; the event criteria name a detector that cannot be
installed and not the paper's public events; and it does not say whether a
text edit after the final run needs a re-run.
