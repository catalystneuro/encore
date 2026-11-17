# holdgraf-2016, Holdgraf et al. 2016

Ten claims reproduced, two partially, seven not reproduced and seven blocked,
six for missing data and one for too few units under the claim's rule; seven
outcomes rest on an assumption, `supp5b-hfb-stable-over-session`,
`fig4a-coherence-after-higher`, `fig4b-coherence-sentence-specific`,
`fig8-mtf-matches-filter`, `supp6a-connectivity-increase`,
`supp6a-after-closer-to-middle` and `supp7-envelope-coherence`. The first
verification round agreed with 23 of the 26 outcomes and disagreed on
`speech-r-count`, which it held partial, fig8, which it held not reproduced,
and supp6a-connectivity-increase, which it held not reproduced on 6 seeds; the
second agreed with all 26, and a third round, on the two changes proposed after
the second (both supp6a claims to not reproduced), agreed with both. CRCNS does
not version data sets, so the version is recorded as unversioned with the data
set's DOI (10.6080/K08S4N4J) and the MD5 sums in the notebook header. The
paper, Holdgraf, de Heer, Pasley, Rieger, Crone, Lin, Knight and Theunissen in
Nature Communications (7:13654), records subdural ECoG in seven epilepsy
patients listening passively to trials of filtered speech (BEFORE), the
unfiltered sentence (MIDDLE) and the same filtered sentence again (AFTER), with
separate behavioural control groups of students, and reports that the
unfiltered sentence raises the words understood in the filtered one, that high
frequency broadband (HFB) activity of speech-responsive (Speech-R) electrodes
is higher in AFTER than in BEFORE, that AFTER is more coherent with MIDDLE trial
by trial, and that encoding models (eSTRFs) of 41 included electrodes shift
towards the modulations kept by the filter, give larger responses to unfiltered
speech, come closer to the MIDDLE eSTRFs, mostly around the superior temporal
gyrus (STG), and predict AFTER better from MIDDLE; the data set holds the
patients' raw ECoG in BIDS, events, 2-D electrode positions and a stimulus
audio track per subject. The claims were written from the version of record as
PyMuPDF text of the journal PDF with its Supplementary Information, with Figure
4 read from the PDF page, and from the linked ecogtools library at commit
7d1030e, which holds no script that runs the paper's analyses, for 26 claims.
The six behavioural claims are blocked, as the control data are not in the
data set, and `supp3b-pink-noise-no-pcorr-change` is blocked as no included
electrode lies in the pink noise subjects. Reproduced are speech-r-count (101
Speech-R electrodes, under 3 of 12 readings, all with the z-score by non-event
times), `fig3b-hfb-increase-after` (cluster 0.36 to 1.28 s, P = 0.0001), fig4a
(P = 0.0003 and 0.0004 on 84 electrodes), fig4b, `fig9-middle-generalizes-after`
(0.051, P = 0.021), `fig10c-stg-location` (51.7%, a small margin), supp7, which
reverses at NW = 3, and three further supplementary claims. Partial are
`fig9-rms-increase`, whose direction holds while the paper's 0.12 is on a scale
the paper does not define, and `fig10-partial-correlation` (0.308 against
0.18). Not reproduced are `strf-r-count` (9 against 53) and with it
`included-electrode-count` (9 against 41), so every eSTRF claim rests on 9
electrodes from S01, S02 and S04, fig8, where the AFTER minus BEFORE shift has
no cluster in the filter's region, `fig10b-similarity-correlates` (r = 0.63, P
= 0.072), supp5b, whose negative slope rests on the z-score, and the two supp6a
claims, which hold only when the coherence is integrated from 2.5 Hz. The
author's first run had 10 reproduced, 4 partially, 5 not reproduced and 7
blocked by its outcome table, though its report gives 5 partially and 6
blocked. The author asked no questions of a reader, so the answer and
author-answers runs changed nothing. Round 1 held that supp5b was run under one
z-score with too narrow a bootstrap, that the supp6a seeds departed from the
criterion, that the coherence bandwidth departed from the claims file's MNE
default, that the RMS of fig9 is in a unit the paper does not give, and that
the failure of the STRF-R selection had not been separated from a pipeline
problem; in reply all three z-scores and grouped bootstraps were run, NW = 4
became the main reading, which moved supp6a-connectivity-increase to reproduced
and supp7 from not reproduced to reproduced, fig8 moved to not reproduced, a
spectrogram shift check found no offset that raises the count, the data set's
own notebooks were read and found to be a loading tutorial, and three
questions went to `questions/crcns-ac-4.yaml`. Round 2 asked for a drift check,
noted that the integration from 2.5 Hz arguably does not start at the lowest
resolved frequency, and found sentences the outputs did not support, among them
the supp3a and supp5b wording and a bias statement in fig4a; in reply the
drift check found no drift that raises the count, the sentences were
corrected, and integrating from the half-bandwidth W led to the two supp6a
proposals. The author's run took about 65 minutes (07:53 to 08:56 UTC); the
notebook ran in 12.7 min at first, with peak memory about 2.9 GB, 1190 s after
the author-answers run, 1336 s after round 1, about 30 minutes after round 2
and 24 minutes after round 3. Nothing failed in the final runs; one command
reading an output file through sed and grep was denied and the file was read
with the Read tool, pytest was not installed for the repository's tests in the
first revision, and the last check corrected a range the round-3 verifier gave
(8.54 to 8.69 bits/s, not 8.64 to 8.69) in the claim notes.

The behavioural control data (three groups of 5, 9 and 15 listeners) behind
Figure 2b and Supplementary Figures 1 and 5A are not in the data set, and the
paper names no other place for them, so six claims cannot be tested. The paper
does not say how the ridge parameter's mode and the STRF-R bound were computed:
over Speech-R electrodes a quarter of the per-split best values sit at the top
of any grid, the held-out coefficient of determination passes only 9
electrodes against the paper's 53, and Figure 6b plots mean model scores near
or above 0 for nearly all electrodes where the held-out coefficient of
determination here is below 0 for most, which suggests a different score. The
data set holds 416 channels (377 marked good) for its 7 subjects, at most 64
per subject, while the paper reports grids of 48, 64, 68, 68, 62, 110 and 104
channels and 468 electrodes kept, and it does not say which channels were left
out or why. The subjects are named S01, S02, S03, S04, S07, S08 and S13 with no
mapping to the paper's S1 to S7. channels.tsv gives the unit as milliV and the
header a resolution of 0.1, but the stored float32 values have a median
absolute value of about 315 in S01 and 1.7e8 to 6.2e8 in the other six
subjects. The data set's explore_data notebook says the audio files are not
available for privacy reasons and the README names subject folders like ir-07,
while the zip holds a stimulus track per subject and folders named sub-S01; the
tracks are on the recording's clock, but S07's is 1015 s for a 989 s recording
and S13's is at 20 kHz against 16 kHz in the others. The stimulus tracks of
S02, S04, S07 and S13 are not silent before the sound onsets (0.43 to 0.66 of
the first 0.5 s of the sound, against 0.02 to 0.14 in S01, S03 and S08), and
the data set does not say what they hold. The events tables of S01, S03, S04
and S07 hold spans with trial_type 'bad' (1 to 12 per subject) that events.json
does not describe, and 22 sounds overlap them; one triplet in S02 and one in
S03 lack a sound, and S01 to S04 each have six unfiltered sentences outside any
triplet. Questions are put to the paper's authors: how HFB was z-scored to
select Speech-R electrodes, how the ridge mode and the STRF-R bound were
computed and which R2 was used, what multitaper bandwidth and frequency range
the coherence used, and on what scale the RMS of Figure 9c is.

The author's points on the protocol: the `methods_unavailable` finding kind is
for the data set while these questions are about the paper; it does not say
what to do with claims that depend on a selection that is not reproduced but
not blocked, so they were tested on the 9 electrodes found; when a criterion's
readings give different outcomes, the first matching reading in the
criterion's order was carried into later claims; `other` is only an example for
too few units, and was used for supp3b; and it does not say how to report a
selection whose data set total differs from the paper's (377 against 468
electrodes), so the total was reported and not judged.
