I ran `tools/readme_row.py 001038 --write`, which added the 001038 row to README.md (16, 7, 1, 0), and added the subsection below to the end of docs/pilot-notes.md. Nothing is committed; those are the only two files I changed. The untracked dotfiles and `scripts` directory in the repository root were already there and I left them alone.

### 001038, Azcorra et al. 2023

Sixteen claims reproduced, seven partially and one not reproduced on the
dandiset, none blocked. Five claims on data in other archives: two
reproduced, on the snRNA-seq count matrices in GEO (GSE222558), and three
blocked. Round 1 gave its own outcome for each claim from the notebook with
its conclusions removed and agreed with all 29, giving other reasons only for
the three blocked claims; the author kept `not_runnable` for the two claims
that need Seurat and LIGER in R and `other` for the histology claim, which
rests on manual cell counts that are not deposited, as the images are public
on Zenodo. After round 1, `fig5ab-transient-scaling` uses the recomputed onsets
that are also stored, which carry the code's exclusion after every reward
(241, 246 and 232% against 239, 266 and 222% before), and stays partially
reproduced. Round 2 agreed with all 29 and nothing was proposed, so there was
no third round. The paper reports that genetic subtypes of dopamine neurons
signal differently: Vglut2 and Calb1 axons in striatum show transients after
decelerations and respond to rewards and air puffs, Anxa1 axons show
transients after accelerations, have almost no reward response and decrease
to air puffs, the subtypes can be clustered from these responses, and somas in
SNc track their axons. The recording counts, the cross-correlations with
acceleration and their lags, PCA and angles, triggered averages and transient
scaling, the reward and air puff responses, the k-means clustering, the soma
and axon correlations, the SNc responses, Aldh1a1 heterogeneity, the overlap
region and two snRNA-seq claims were tested; the snRNA-seq clustering and the
integration of four published datasets are blocked as `not_runnable`.
`recording-counts-locomotion` is not reproduced: the Methods' criteria select
50, 28, 82, 89 and 85 striatal recordings for Vglut2, Calb1, Anxa1, DAT and
Aldh1a1, against 42, 22, 47, 74 and 75, and no variant gives the paper's
counts. Some outcomes rest on weak ground: the 18 claims that use the
locomotion selection are tested on this larger set; `fig2jk-pca-variance` is
inside tolerance by 0.5 and 0.02 points; in `fig2l-pc-angles` the Anxa1 mean
depends on where the circle is cut (circular mean 301.3 against 233.3
degrees); `fig4g-reward-response` is partially reproduced with the Methods'
windows, while the code's windows give the paper's 7.90, 12.40 and 5.88; the
cause of the Vglut2 peak timing in `ed6f-dec-peak-timing` and of the DAT air
puff mean (2.69 against 5.3) is not found; and the deep band of
`ed1h-aldh1a1-depth` holds 5 recordings. The author used the open access full
text (PMC10545540) and took what the Methods leave open from the paper's code
at commit fad12b2.

The dandiset was converted by CatalystNeuro (catalystneuro/dombeck-lab-to-nwb).
The files carry the signal-to-noise ratio and 405 nm cross-correlation but not
the other exclusion flags (running time, 405 nm artifacts) or which recordings
each figure uses; recomputed with the paper's code, the stimulus analyses give
the paper's counts exactly, but the locomotion criteria select more striatal
recordings than Figure 2 reports (Anxa1 82 against 47, Vglut2 50 against 42).
The Events table lists consumed rewards only, and rewards the mouse did not
lick for are only in the raw 4 kHz Reward trace, so 911 acceleration and 767
deceleration onsets recomputed from the processed data are not in the stored
WheelEvents. The `coordinates` column of the fiber table is described as (AP,
ML, DV) but holds (ML, AP, DV), and 785 of 790 SNc fibers and 1281 of 2137
fibers overall have no coordinates. The column
`cross_correlation_with_acceleration` holds the peak cross-correlation of the
405 nm control with acceleration, not of dF/F, and is missing where running
was under 100 s. The dF/F series are normalized so that the largest transient
is 1, which the files do not state, and the normalization factor in
`normalized_fluorescence` holds two values per row in 123 files. Other
findings: three subject ids ending in L are left-hemisphere recordings of mice
that also have ids without it, so the archive's 105 subjects are 102 mice, and
the age is a range (P8W/P16W) in every file; the published version's link to
the paper is malformed (fixed in the draft) and its asset summary lists only
"analytical technique" and "ProcessingModule"; the code integrates responses
over windows that differ from the Methods', and the paper's reward means equal
those of the code's windows to the decimal, as do its Vglut2, Calb1 and Anxa1
air puff means within tolerance, while its DAT air puff mean (5.3) does not
(2.46); the code reports trough and peak times 0.02 and 0.01 s later than the
Methods define, prints uncorrected p-values for Figures 2i and 7f, whose
legends state Bonferroni correction, and marks 405 nm artifacts from the last
noisy section to the end of a recording and from the start to the first; and
the paper swaps the Calb1 and Vglut2 reward P-values between the Results and
the Figure 4g legend, gives 10 Anxa1 mice in the Figure 2f legend and 9 in the
Methods, and gives different SNc variance values in Extended Data Figure 9k
and the Methods. No recording is deposited twice.

The notebook ran in 182 s in the first clean run, `tools/entry.py all` took
107 s after round 1 and 2.3 minutes after round 2. The first metadata scan
took 30 minutes, as h5py serializes calls across threads and every download
URL needed its own API request, and was sped up with a process pool, the bulk
asset listing and BLAS limited to one thread; early runs crashed on the files
with two `normalized_fluorescence` values per row; and the paper's 4.4 GB
MATLAB table on Zenodo, which carries the exclusion flags, was not practical
to parse. Round 2 found statements the outputs did not support, among them
that the Calb1 trough lag with the code's timing equals the paper's, that the
response means match to the decimal, which fails for the DAT air puff mean,
and that the overlap recordings come from the same mice, as well as findings
with no output behind them, and these were corrected. Untracked files in the
repository root that the author did not create were left alone. The author's
points on the protocol: Methods and code that disagree where the code gives
the paper's numbers; a count claim that fails while other claims use its
selection; whether analysis parameters taken from the paper's code count as
inputs; `not_runnable` for software in R and no category for manual cell
counting; a 10% tolerance for a value near zero and for angles; a MATLAB
k-means seed that cannot be repeated; and selection counts and one session's
values seen before the criteria were written.
