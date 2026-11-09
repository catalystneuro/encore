# crcns-fcx-2, Johnson et al. 2018

Five claims reproduced, none partially, seven not reproduced and nine blocked,
all for methods underspecified; three outcomes rest on an assumption,
`behavior-no-difficulty-difference`, `erp-no-condition-difference` and
`psi-theta-shift`. The first verification round agreed with 19 of the 21
outcomes and disagreed on behavior-no-difficulty-difference and psi-theta-shift,
both of which it held partial, and the second agreed with all 21, though it
questioned the label of the nine blocked claims; nothing was proposed after the
second, so there was no third round. CRCNS does not version data sets, so the
version is recorded as unversioned with the data set's DOI (10.6080/K0VX0DQD)
and the MD5 sums in the notebook header. The paper, Johnson, Adams, Solbakk,
Endestad, Larsson, Ivanovic, Meling, Lin and Knight in PLoS Biology (16,
e2004274), records intracranial EEG from the medial temporal lobe (MTL), lateral
prefrontal cortex (PFC) and orbitofrontal cortex (OFC) in ten adults with
epilepsy during a visuospatial working memory task of 120 trials split between
identity, spatial and temporal conditions, and reports that accuracy and
response time do not differ by condition, that ERPs do not either, that theta
power is sustained over encoding and delay, that phase locking peaks in theta
within the MTL and between MTL and frontal electrodes, that theta phase slope
index (PSI) shifts from frontal leads before the test cue towards MTL leads
after it, that theta phase comes to lead higher-frequency amplitude after the
test cue in counts of electrodes and pairs, and that theta phase-amplitude
coupling (PAC) carries spatial and temporal information from the MTL to frontal
cortex; the data set holds, per subject, the filtered continuous data, the
preprocessed bipolar segments with trial information, electrode MNI
coordinates, a per-trial table, a behaviour table, the channels analysed per
region and the analysis scripts. The claims were written from the version of
record (PMC5895055) as flattened Europe PMC XML with the legends of Figures 1
to 8 but without a PDF, the contents of S1 to S4 Table or the analysis
scripts, for 21 claims. Reproduced are `behavior-proficient` (0.792 to 0.967),
`electrode-counts` (36, 116 and 102, exact), `correct-trial-counts`,
`plv-theta-peak`, on a rule one subject per group satisfies, and
behavior-no-difficulty-difference, which holds only with the response times of
`docs/summary_file.csv` (F(1,28) = 2.41, p = 0.13), while the trial tables'
response times give F(1,28) = 12.33, p = 0.0015. Not reproduced are
erp-no-condition-difference (1 of 254 electrodes significant, 0 with a
per-trial baseline), `power-theta-sustained` (theta sustained in 1 of 10, 0 of
9 and 0 of 9 subjects), `power-condition-exclusions` (7 electrodes in 4
subjects against 8 in 4), psi-theta-shift, which would be partial in the
deposited code's windows, `crossspectral-shift` (1 of 7 systems),
`phase-directing-counts` (0, 0, 0, 0, 1, 3 and 2 units) and `theta-peak-bands`
(overlap 4 of 10). Blocked are `crossspectral-equal-strength` and the eight PAC
claims, as no defensible selection of phase-directing units is left. The
author's first run had 4 reproduced and 17 not reproduced by its outcome table,
though its report gives 5 and 16. The author asked one question of a reader,
whether the behaviour criterion should include condition as one numeric term;
the reader judged the claim on that reading, which the printed F(1,28) fits,
and the author-answers run moved behavior-no-difficulty-difference to
reproduced on it. Round 1 held that every neural outcome rested on an unchecked
time axis, that the response times of summary_file.csv were of unknown
provenance, that the code's form of PSI gave z SD 27 on independent pink noise,
that cross-spectral PSI had not been run with sliding windows and that the ERP
baseline was unclear; in reply a delay-jitter test made the trial table's
window placement the main reading, a trial-shuffle calibration showed the
code's form passing 57% of units against 56% on real data, which moved the
nine claims from not reproduced to blocked, the deposited scripts were quoted,
the source of the response times was searched (9 of 30 values matched) and the
sliding-window reading was run. Round 2 raised edge effects under the table's
placement, asked the record to say that the paper's numbers would come from the
code's windows if the deposited scripts produced them, and found sentences the
outputs did not support, among them one on the PAC direction patterns; in reply
an edge check on joined traces left the outcomes as they were, the model was
run on the 5 MTL-OFC pairs the sliding windows select (not judged), and the
sentences were corrected. The notebook ran in 35.5 min at first, with peak
memory 5.9 GB, 31.6 min after the author-answers run, 47 min after round 1 and
53.6 min after round 2. Nothing failed in the final runs; after the last run one
sentence of the notebook's text was filled in by hand in the source and the
executed copy.

The data set's derived time axes put each segment's first sample at -1.5 s,
and that sample is the trial table's epoch start, so the task events lie 1.5 s
earlier than 0 s suggests; the deposited scripts cut their windows as if 0 s
were the event, and the 900 and 1150 ms delay trials part where the table puts
the first delay-dependent event (proc ERPs from -0.25 to 0.75 s, p down to
0.005) and not where the scripts' windows put it (p 0.29 to 0.94). The deposited
psianalysis.m multiplies the Fourier coefficients without conjugating one of
them and z-scores per-trial PSI against a null built from trial-averaged
coherency; with the conjugate added it passes z > 1.96 for 57% of units with
trials shuffled, as many as on the real data (56%), while the Methods' PSI
passes 0% to 0.1%. subtracterp.m selects the temporal trials by the delay
column, so that condition is empty, pacanalysis.m uses an undefined variable
and dirpac_compute.m calls it with six arguments where it takes four, so the
PAC scripts cannot run as given. The response times of docs/summary_file.csv,
described as calculated on all correct trials, differ from the trial tables'
mean over correct trials in 7 of 10 subjects (s1 identity 1948 against 2348
ms), and the paper's condition means are those of the file; its accuracies do
equal the trial tables. For s10 the trial table's epoch columns are not on the
derived data's sample grid, and its trialinfo does not equal the table's
columns. The descriptor gives fsample 1000 for the derived structures, where s8
and s9 are at 512 Hz. The Methods' sliding 3-cycle PSI windows cannot fit a 900
ms segment at 3 Hz, and the behavioural models are described with 3 condition
fixed effects but reported as F(1,28). Questions are put to the paper's authors:
how the behavioural models coded condition and on which response times they
were fitted, and which form of PSI and which spectral window produced the
reported PSI values and phase-directing counts, and whether the analysis windows
were cut 1.5 s later on the derived time axes than the trial table places the
events.

The author's points on the protocol: the clock check does not say what to do
when the time axes and the trial table disagree and the data have no
task-locked response; it does not say what to do when the Methods describe a
method that cannot run and the code differs; it does not say whether a claim
whose selection is empty under the main reading is blocked or may take another
reading; `docs/archives.md` says to use fsspec, while the files are tar.gz,
which streamed about 5 times faster with requests (46 against 10 MB/s); "do not
download to disk" does not address development caches, which were kept in
`$TMPDIR`, and one 210 MB member was briefly saved while exploring and deleted;
and judging absence on "the paper's test alone" does not help when the paper's
test is unclear, so a reader was asked.
