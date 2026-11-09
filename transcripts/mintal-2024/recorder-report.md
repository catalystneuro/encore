I wrote `docs/pilot-notes/figshare-24949470-mintal-2024-01.md` and changed no other file. The `catalystneuro` field for this item is empty, which is in `targets/figshare.json`, not `targets/dandisets.json`. So the second paragraph does not open with a CatalystNeuro sentence. The tracker row counts only claims on the dataset, which gives 12, 4, 0, 0, so the two blocked claims on outside data are described in the note but not counted.

# figshare-24949470, Mintal et al. 2024

Twelve claims reproduced and four partially, all on the dataset, with none
not reproduced; the two claims on data held elsewhere are blocked and not
counted. It pins version 1, the item's only version, which holds 8 files: the
user responses (data_without_email.csv), the party workbook, the recoded party
positions, Supplementary Table 1, a census CSV, a data dictionary, a README and
the paper's R code. The paper, in Scientific Data, describes the Volebny Kompas
voting advice application for the 2023 Slovak parliamentary election: 134,699
responses to 39 statements gathered from 5 September 2023 to election day, and
the positions of 11 parties on those statements, coded by two experts and
self-placed by 4 parties. The claims were written from the version of record in
Europe PMC (PMC11374779) without its figures or the R code, so the party
placements of Figures 2 and 3 and the dendrogram of Figure 7 were read from the
publisher's images, by pixel position, by a separate agent that had not seen
the computed values, and are listed under `inputs`. The response count, the
collection window, the party workbook, the parties and self-placements, the
coders' kappa, the uni-dimension and landscape placements, the clustering,
Table 2, the age and education inconsistencies, the statistics of S2 to S5 and
the factor analysis were tested. `selected-parties-top-vote` is blocked as
`other`, as the official 2023 results have no pinned source (the ParlGov 2024
release ends its Slovak elections with 2020), and `website-views` as `other`,
as the platform's usage records are public nowhere.
`uni-and-landscape-placements` is partially reproduced: with No opinion as 50
every party is within 0.8 of Fig. 2 and within 0.3 of Fig. 3's cultural axis,
but PS scores 47.7 on the economic axis where Fig. 3 places it at 54.5, so PS
and DEMOKRATI are ordered differently. `collection-window` holds in part, as
432 of 134,699 rows (0.32%) are dated 1 to 9 October 2023;
`age-education-inconsistencies` gives 27 and 378 against 40 and 400, so only
the 18-20 count is within tolerance; and `efa-loadings-consistent` holds on the
Pearson matrix (35 of 39 statements matched) but not on the polychoric one (32
of 39). The author put no questions to a reader, so the answer run changed
nothing. Round 1 gave its own outcome for each claim and agreed with 15 of 18;
the author took its outcomes for `collection-window` and
`age-education-inconsistencies` (from not reproduced to partially reproduced)
and `efa-loadings-consistent` (from reproduced to partially reproduced), and
kept `other` for the two blocked claims where round 1 gave `data_missing`, as
the check does not allow it for data held elsewhere. Round 1 judged that the
first figure readings matched the computed values too closely to have been
made blind, which led to the blind re-reading by pixel position; its points
also led the notebook to print the R code lines it relies on, add psych's
resampled-data reference for the polychoric parallel analysis (11 factors
again), report convergence by kind of fit and check the MD5 of every file; and
a question was put to a reader on whether the 40 and 400 describe an earlier
state of the data, unanswered, as it was added after the answer step. Round 2
agreed with all 18, so there was no third round; it found statements the
outputs did not support, among them a 461-row count for the R code's date
filter, counted on the raw rows where the code filters data_cleaned_corrected
(451), and an unshown note that a looser optimiser tolerance gave 12 factors,
and these were corrected or withdrawn. Some outcomes rest on weak ground:
`coder-agreement-kappa` holds only under the one reading of four that gives
0.842 (quadratic weights, No opinion left out), the others giving 0.620 to
0.745; `efa-eleven-factors` with psych's defaults holds under reading (a) only,
as reading (b) gives 12 Pearson factors; `efa-loadings-consistent` rests on the
claims file's own thresholds; and the placements and the clustering rest on
figure readings the verifiers could not check, as the registry's check refuses
code that reads an image. psych could not be installed in the entry's Python
environment, so its parallel analysis, polychoric correlations and factor
extraction were reimplemented in Python. The author's run took about 35
minutes; a first run failed on a synthetic test matrix that was not positive
definite, which was fixed, and `factor_analyzer` would not run with the current
scikit-learn, so no cross-check against it was made. The notebook ran in 7.5
minutes at first and about 9.5 minutes in the last run.

In "VAA_party_positions coded.xlsx" the "Statement no." column disagrees with
the statement's wording in 99 of 429 rows: for every party the rows worded as
statements 16 to 24 are numbered 22, 23, 24, 16, 17, 18, 19, 20, 21, while the
recoded CSV and Figures 2 and 3 follow the wording, so a user who joins
positions to the responses by "Statement no." gets the wrong statements. The R
code removes 330 responses that give the same answer to all 39 statements (204
of them all "no opinion"), a step the paper's Data cleaning does not mention;
with it Table 2 and the S4 and S5 counts are reproduced exactly, and without it
they differ by up to 2.5%. The paper says the responses were gathered up to and
including election day, but 432 rows are timestamped 1 to 9 October 2023,
among them Table 1's sample entry (2023-10-09 08:57:38), the file's first row
and latest timestamp; the R code has an optional filter that drops 451 of the
rows it is applied to, and the paper does not say the deposited file keeps
them. Figure 3 places PS at 54.5 on the economic axis while the deposited final
positions give 47.7 by the calculation that reproduces every other placement
of Figures 2 and 3 to within 0.8. The paper does not state the weights of the
kappa or how "No opinion" enters it, and the deposited data give 27 and 378 (or
34 and 505 with applied higher education) for its 40 and 400 age and education
inconsistencies, which the R code does not check; both are put to the paper's
authors. Other findings: "no opinion" answers are the string "NA" (183,459
values in S1 to S39), not empty strings as the paper says; the README calls
each row a unique respondent while EMAIL_ID repeats (30,775 distinct ids over
32,009 rows with an id), as the paper says it may; and the data dictionary
lists no categories for GENDER, AGE and EDUCATION, gives no time zone for
TIME.STAMP, and lists a "Self-placement source" column that is empty in all 429
rows.

The author's points on the protocol: no blocked reason fits a claim on data
held elsewhere that is public nowhere, or public but with no DOI or versioned
release, so `other` was used for both; the `with_labels` check asks for
outside inputs and a `metadata_insufficient` finding where the labels are in
the dataset itself (Supplementary Table 1); there is no rule for expected
values read by eye from published figures; it does not say how to treat
analysis code that disagrees with the Methods when the claims file has not
read the code, so the paper's reading was kept as the main result and the
code's shown as variants; the clock check has no meaning for survey data; and
it assumes an environment without R, so psych had to be reimplemented in
Python.
