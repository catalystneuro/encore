# 000019, Bouchard et al. 2013

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
