# costabile-2023, Costabile et al. 2023

Two claims reproduced on the dandisets, none partially, none not reproduced and
13 blocked, with 6 more blocked that also use outside inputs, the Z-Brain
centroids on Zenodo; the 14 simulation and mouse claims (`data: elsewhere`) are
counted apart, all blocked as not attempted. Both reproduced outcomes rest on an
assumption. The first verification round agreed with all 35 outcomes but not
with every reason: it gave the simulation claims other (not attempted) where the
record had too_large, which the author took, and the mouse, anatomical and
reticulospinal claims data_missing; the author took it for
`fig6f-reticulospinal-behavior`, changed the mouse claims to other, as the CSHL
data are public, and kept too_large for the anatomical claims, whose centroids
are public on Zenodo. The second round agreed with all 35 and accepted those
reasons, and nothing was proposed after it, so there was no third round. Each
dandiset is pinned at its only published version (000235/0.230316.1600,
000236/0.230316.2031, 000237/0.230316.1655, 000238/0.230316.1519); the paper
cites none. The paper, Costabile, Balakrishnan, Schwinn and Haesemeyer, "Model
discovery to link neural activity to behavioral tasks" (eLife 12:e83289),
presents MINE, which fits a CNN to each neuron's activity and uses Taylor
analysis to say which predictors drive it and how nonlinearly, tests it on
simulations (Figures 1 to 4) and mouse widefield data of Musall et al. 2019
(Figure 5), and applies it to whole-brain imaging of larval zebrafish under
random heat stimuli, where it reports more neurons identified than by a linear
model, 33 functional classes with mixed selectivity, 15 temperature receptive
field clusters and their anatomy, and a backfill control on reticulospinal
neurons. The claims were written from the version of record and the paper's
code at commit 368d756; the figure supplements are online only and not under
`paper/`, so the claims on them rest on the Results and the code, and the claims
check corrected 11 claims and added 3, for 35. `data-zebrafish-coverage`
reproduces: 25 fish, 750 planes and 706,543 CaImAn components, exactly, and
434,651 components pass the brightness cut, recomputed from the raw movie,
against the paper's 432,882. `figs6-train-test-uncorrelated` reproduces with
median inter-trial correlations of -0.051 for temperature and -0.009 to -0.001
for the behavior traces under every bout reading, though the temperature
correlations range from -0.909 to 0.873 and a stricter variant on their median
absolute value (0.266) fails; the round-1 verifier noted that the criterion
passes any distribution centred on zero, and this went to a reader in
`questions/costabile-2023.yaml`. The 12 claims on the zebrafish fits and the 6
anatomical claims that depend on them are blocked as too_large: one fit takes a
median 2.14 s on one thread, and the 432,882 real-data fits come to 141 h on the
runner's four CPUs and 283 h with the rotated controls, against a run of five
hours. Estimates that decide nothing were added in reply to round 1: the linear
model fit to every bright component finds 26,328 at sqrt(0.5) against about
25,300 implied by the paper, and a seeded subsample of 600 MINE fits gives a
union of about 54,491 (95% interval over planes 26,711 to 86,594), with 0.374
only by MINE, 0.514 by both and 0.113 only by the linear model, against the
paper's 40%, 54% and 6%; at cutoff 0 MINE's point estimate is below the linear
model's (362,580 against 371,878). `fig6f-reticulospinal-behavior` is blocked
for missing data. The simulations and models were not ported and the mouse data
were not fetched. Round 1 also found that the clock check was misread, which
came from a wrap-around in the author's circular shift and was fixed, asked for
start times, the red channel of 000238, the channel descriptions and more timed
fits, all of which were printed, and found the 10 planes with odd tail
timestamps, which became a finding. Round 2 found timing figures copied from an
earlier run, the claim that the subsample estimate met the every-cutoff
criterion and a statement that the misplaced side of the tail jump could not be
told, which were corrected, and asked that `data-zebrafish-coverage` be marked
assumed. The author's session took about 2 h 25 min, ending at 01:50 UTC; the
notebook ran in 40 min with peak memory about 1.3 GB, then 57.6 min with 14.8
min for the subsample notebook after round 1, and 49 min and 15 min at the end.
One subset run failed on a matplotlib argument and was fixed. The subsample is
600 fits, not the 2,000 planned, as the first try's worker pool was killed while
it ran beside the main notebook and a wait loop then cost about an hour; fit
times vary between runs by tens of percent, and after round 1 two timing
sentences were corrected by hand in the executed notebooks, which voided the
run stamp.

The files hold the tail tracking (segment angles and cumulative tail angle at
250 Hz) but no swim bouts and none of the three behavior predictors the paper
fits, and the paper gives the bout threshold only as "empirically determined"
(major): the lab's bout detection with its default of 2 rad/s finds a median 4.9
bouts per second, inside the tracking noise (segment angles move in steps of
0.0997 rad), while 5 or 10 rad/s give 0.075 to 0.095 per second, and every
analysis of behavior-driven activity depends on the choice. The whole-brain
dandisets hold no registration to the Z-Brain atlas and no anatomical
coordinates beyond each plane's pixel masks and a plane-level location label
such as "Dorsal Forebrain" (major), so the regional analyses of Figures 6 and 7
need the registered centroids in the paper's processed data on Zenodo
(doi:10.5281/zenodo.7737788). 000238 holds no annotation of which components
are the reticulospinal neurons labelled by the backfill (major); the Texas-Red
channel is there only as the raw movie, in 175 of 175 planes. In 10 of 925
planes the tail timestamps hold a single step of 128.004 s, so part of the tail
recording is misplaced by 128 s relative to the imaging; the side can be told
from the time ranges, and moving it by the jump gives the range of the other
planes, so the finding went from minor to major after round 1 and back to minor
after round 2. Each temperature trace is a median 10.5 s longer than its imaging
and every series starts at 0 s; read as starting with imaging, as the paper's
code takes it, temperature predicts the calcium better (median held-out
correlation 0.656 against 0.493, in 98.3% of planes). The imaging rate is 2.384
Hz in every plane where the Methods say 2.5 Hz; one backfill file has 25 planes,
8 planes have 1,181 frames, not 1,182, and in 10 planes the temperature exceeds
the paper's 22 to 30 C, up to 31.57 C; the segmentation's reference images are
empty, so the projection behind the brightness criterion has to be recomputed
from the movie; and the response series are named CaUnitRespones (sic). No plane
is deposited twice, the pixel masks line up with the movie (median correlation
0.834 with CaImAn's traces), and calcium is predicted far better by its own
plane's temperature than by the next plane's (0.656 against 0.393, in 98.5% of
planes) and peaks 1.8 s after swim starts, consistent with shared clocks. Two
questions are put to the paper's authors: which bout threshold, minimum bout
length and angle input were used, and whether the brightness projection was
taken from the raw or the motion-corrected movie.

The author's points on the protocol: too_large mixes a computation that is too
big with the time left in a run; the five-seed rule multiplies the cost of the
simulation claims and allows no reduced seed check; a claim gets one
`blocked_by` while the anatomical claims have two blockers, and the second was
put in the notes; the clock-check recipes do not fit a slow continuous stimulus,
and held-out decoding with the temperature shifted in time was used; the bout
method lives in code the claims file names but did not read, and its default
threshold does not fit these data; the train-test criterion can pass with
strong correlations of both signs, and it was applied as written with the
median absolute value as a variant; a finding needs a cell tag, so one sanity
cell carries two; `runtime_minutes` must be written before the run and editing
it afterwards invalidates the run's stamp; and the backfill annotation may be in
the paper's Zenodo data, which the claims file does not name as an input, so it
was not opened.
