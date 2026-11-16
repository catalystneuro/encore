# kalogriopoulos-2024, Kalogriopoulos et al. 2024

No claim reproduced, none partially, none not reproduced and all 32 blocked,
4 as `metadata_insufficient` and 28 for missing data. The first verification
round agreed with all 32 outcomes and the second with all 32; nothing was
proposed after the second, so there was no third round. It pins version
0.250312.0036, the only published version; the paper cites neither a version
nor the dandiset. The paper, Kalogriopoulos, Tei et al., "Synthetic GPCRs for
programmable sensing and control of cell behaviour" (Nature 637, 230-239),
builds antigen-gated G-protein-coupled receptors (PAGER) and tests them mostly
in cell culture, imaging and biochemical assays, with one acute slice
experiment in which PAGER-Gi-expressing CA1 neurons are recorded during DCZ
alone or DCZ plus soluble mCherry; the dandiset holds only that slice
experiment (Fig. 4e-j and Extended Data Fig. 12a-h). The claims were written
from the version of record as served by Europe PMC (PMC11666456) with its
Supplementary Information, without the figure panels; the paper's scripts are
available only on request. The 24 claims on culture, imaging and biochemistry
are blocked because those data are not deposited. The slice claims, among them
the larger hyperpolarization (Fig. 4i) and rheobase increase (Fig. 4j) with
DCZ plus mCherry, are blocked because no file says which condition a cell was
in or when DCZ was applied, and the mEGFP correlations of Extended Data
Fig. 12 and the preincubation times because the files hold no such values.
The author asked a reader nothing, so the answer and author-answers runs
changed nothing. Round 1 found that the scan behind "no condition recorded"
skipped `/intervals`, every sweep after the first and long string datasets,
that the outputs did not say the totals rule out reproduced for
`methods-slice-sample`, that the second spike rule (A2) was never compared
with the first, that the Methods' age range had been read too strictly and
that the sampling-rate test could not exclude interpolation; in reply the scan
was made to read every object in every file and found no intervals group and
no condition, drug, onset or expression field, the totals were printed against
41, the two rules were compared (within 1 pA in 10,335 of 10,675 sweeps), the
finding that two mice were older than the Methods allow was withdrawn and an
interpolation test was added. Round 2 asked for wording fixes (fields absent,
not empty; the ramp duration; a table column) and that the assumption that
every deposited cell belongs to one of the two conditions be stated, and
showed that the interpolation baseline had not been run; the author upsampled
each file's first sweep three ways and stated the assumption. The author's
run took about 1 h 50 min (07:36 to about 09:24 UTC) and no run failed; the
metadata survey took 16 minutes, and the notebook ran in 969 s at first, with
peak memory 0.49 GB, 784 s after round 1 and 732 s at the end.

No file records which cells received DCZ alone and which DCZ plus mCherry, or
when DCZ was applied: no file has an intervals group or a notes or
pharmacology field, every sweep's description is the same generic text, and
the conditions are named only in the dandiset's description, so the paper's
slice comparisons cannot be made. The mEGFP intensity of each cell (or the
widefield images and soma ROIs behind it) and each cell's mCherry
preincubation time are not in the dandiset, and the culture, imaging and
biochemical data are deposited nowhere; the paper's Data availability says
all data are within the paper and its Supplementary Information. The files
hold 50 cells from 8 mice where the paper analysed 41 (15 with DCZ, 26 with
DCZ plus mCherry) from 7 and 6 mice; the paper's initial Rin exclusion removes
one cell (PK-113, 525 megaohms), leaving 49, and nothing marks which cells
were analysed. Channel 1 of every sweep is a CurrentClampSeries in volts that
holds the injected current in amperes, and the stimulus series gives the ramp
as a step to +500 pA from 1.1 to 3.1 s in every sweep, while the delivered
current is a ramp from -150 pA. In 10 of 50 cells the ramp reaches +500 pA at
2.7 s (407.5 pA/s) or 2.5 s (465.7 pA/s), where the Methods state -150 to +500
pA across 2 s (326 pA/s), so their absolute rheobase is not comparable with
the other cells, and every sweep holds -150 pA for 100 ms before the ramp,
which the Methods do not describe. The files are sampled at 20 kHz where the
Methods say 10 kHz; residuals of 0.87 to 1.58 ADC counts against 0.30 to 0.57
for the same sweeps upsampled from their even samples are consistent with
acquisition at 20 kHz, though an upsampling that adds noise is not excluded.
Experimenter, lab and institution are "_" in every file, and the holding
current is not recorded (the current monitor reads about 0.5 pA before any
injection). Voltage and current share the sweep clock, 49 of 50 cells start
within 3 mV of -65 mV, and no recording is deposited twice. The text cites the
T-cell chemotaxis panels as Fig. 4l,m and the expression histogram as Extended
Data Fig. 12h, which the legends label Fig. 4k,l and Extended Data Fig. 12i.
One question is put to the paper's authors: which change windows,
mixed-model unit, spike detection rule and Rin window were used, and which 41
of the 50 deposited cells were analysed, in which group.

The author's points on the protocol: it does not say what the notebook should
hold when every claim is blocked; "blocked for the same reason" clashes when a
dependent claim has its own reason, and `data_missing` was given for the ed12
claims with the dependency in the notes; it does not cover a source named in
the criterion, here the stored stimulus, being wrong in the data, so rheobase
was read from the current channel as a deviation; questions for the authors
normally come out of testing, but one was added though nothing was tested;
condition labels held only by the authors fall between
`metadata_insufficient` and `data_missing`; and surveying metadata was slow
with about 600 series per file.
