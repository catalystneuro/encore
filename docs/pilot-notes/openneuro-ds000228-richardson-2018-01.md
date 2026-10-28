# openneuro-ds000228, Richardson et al. 2018

Fifteen claims reproduced, eight partially, twelve not reproduced and none
blocked on the dataset alone. With outside data, counted apart: one
reproduced, one partially, three not reproduced and one blocked;
`replication-sample`, on data deposited nowhere, is left out of the counts
and blocked as `other`. It pins snapshot 1.1.1, its latest, whose CHANGES
file says it only updated the citation. The paper, Richardson, Lisandrelli,
Riobueno-Naylor and Saxe in Nature Communications, scans 122 children aged
3.5 to 12 years and 33 adults during one viewing of Pixar's "Partly Cloudy"
and reports that the theory of mind (ToM) and pain networks are distinct from
age 3, that their within-network correlations rise and their across-network
anti-correlation grows with age, with events found by reverse correlation,
a functional maturity measure and the children's false-belief performance.
The claims were written from the version of record with its supplement,
whose four tables are images and were read from the PDF; the analysis code
is available only on request, so no code was read. A first claims run
stopped because the supplement was missing. The behaviour, motion,
inter-region correlations, reverse-correlation events, functional maturity
and the face-network controls were tested. The independent sample of 20
adults is not deposited, and the hand-coded events of Jacoby et al. 2016
exist only in an unpinned Saxe lab script (movloc.zip), so `hand-coded-events`
is blocked as `other`. The four claims on the face and scene parcels count as
outside data in the claims file, but the parcels were taken from the dataset,
which holds them. The author's first run gave 15 reproduced, 12 partially, 13
not reproduced and 2 blocked. The author asked a reader no questions, so the
answer run and the following author run changed nothing. In round 1 the
summary cell was not removed by the handover, and the verifier read it after
forming most of its outcomes. Round 1 agreed with 39 of 42 outcomes, and the
author took its outcomes for `irc-williams`, `rc-child-adult-timecourse` and
`maturity-across` (each from partially reproduced to not reproduced); its
points led to the adult and 3-year-old mean matrices, the ROI centroids (the
masks are in MNI mm), the image scaling (int16, no scaling), diagnostic
pipeline variants, a stated rule for absence claims that change outcome
between readings, 159-TR timecourses for reading (b) of `rc-overlap`, and a
check of the replicated events the README lists. Round 2 agreed with 41 of 42,
disagreeing on `rc-overlap`, which it judged not reproduced as its criterion
has no partial clause; the author kept partially reproduced, as the claim's
test holds and only its expected count (0 overlapping timepoints against 1)
misses. It found statements the outputs did not support, among them a summary
saying every behavioural number is recovered exactly, a within-ToM t of -6.23
called out of tolerance, and an offset stated for all groups that holds for
adults, which were corrected. Nothing was proposed, so there was no third
round. Some outcomes rest on weak ground: `irc-tom-behavior-age` and
`irc-fb-across` are not reproduced under the assumed O2a and O3a readings and
would be reproduced under O3b; `maturity-within` is reproduced and would not
be under O2b with O3b; `rc-fb-no-difference` is reproduced under O7a, while
under O7b T05 has p = .0497; `rc-3yo-events` is partially reproduced under
O6b and not reproduced under O6a, and uses the best-matching rc-events
reading (O5a), an extension of the criterion; and `beh-fb-tom` holds under
reading (a) only. The author's run took about 32 minutes (16:10 to 16:42 UTC)
and nothing failed; the notebook ran in 147 s at first, and the entry's README
gives 146 s and 183 s for the last runs.

With the paper's own deposited preprocessed images, artifact and CompCor
regressors and ROI masks, and the pipeline of the Methods, the inter-region
correlations differ from the paper's: in adults .604, .398 and -.051 against
.48, .35 and -.17, while in the 3-year-olds within-ToM is higher (.326 against
.21) and within-Pain lower (.179 against .23; non-bilateral Pain .146 against
.17). No variant within the described method closes the gap; only a shared
ToM and Pain signal added as a regressor, outside the paper's method, moves
the across value past the paper's, and it takes both within-network values
to .286 and .258. Several downstream results, the within-ToM difference
between false-belief passers and failers, the age effects at event peaks and
the T04 effect of ToM score, do not come out as reported, so either the
deposited data or the described pipeline differs from what produced the
paper's numbers. The behavioural counts match exactly from participants.tsv,
and FB_Group is also filled for 57 children aged 6 and over (54 pass, 3 inc),
which the paper does not use. participants.tsv lists 2 seven-year-olds and 21
8-12-year-olds with 3.13 mm voxels and no slice gap, where the Methods say 3
and 20; the voxel-size column is misspelled "Voxel slize", and the no-gap
level is stored as an empty value where participants.json defines "None". 19
participants have face-ROI voxels without data at some timepoint, where
Supplementary Fig. 4 counts 17 with incomplete ventral coverage, so the
coverage criterion may differ. The independent sample of 20 adults that
defined the ToM and pain ROIs is not deposited anywhere, though the ROIs it
produced are in the dataset, and the README's list of replicated events
overlaps all Supplementary Table 3 events except P08, P09 and P11. Two
questions are put to the paper's authors: which timepoints entered the
inter-region correlations and whether each artifact timepoint had its own
regressor; and over which timepoints each ROI timecourse was z-normalized
before the reverse correlation, whether child event magnitudes came from the
z-normalized timecourse, and at what alpha the reverse-correlation t-tests
were run. The high-pass filter implementation is also not stated.

The author's points on the protocol: `replication-sample` is public nowhere,
but the checker rejects `data_missing` for an `elsewhere` claim, so `other`
was used; no block reason fits an input that is public but cannot be pinned,
as for the hand coding; the claims file treats the face and scene parcels as
outside input though the dataset holds them; Rule S counts a test that misses
the paper's p bound as failed even when the effect is significant in the same
direction, which made three claims not reproduced; some criteria, as for
irc-williams and face-rc, define only the reproduced outcome; the data-check
rule assumes trial tables, which this movie study lacks, so timing was checked
on the ROI signal at artifact timepoints and by shifting the event labels;
absence claims whose outcome changes between readings fall between the rule
that absence is judged on the paper's test and Author step 1.6, which was
followed; and the repository root has untracked dotfiles from the sandbox.
