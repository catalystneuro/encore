# crcns-hc-10, Lee et al. 2014

Four claims reproduced, one partially, none not reproduced and 27 blocked, all
27 for missing data; the two claims on the network model, which need the
model's code from outside the data set, are blocked as too large and counted
apart. The first verification round agreed with all 34 outcomes as they stood
and the second with all 34; nothing was proposed after the second, so there was
no third round. CRCNS does not version data sets, so the version is recorded as
unversioned with the data set's DOI (10.6080/K00P0WXQ), and the notebook checks
the zip's MD5 against the data set's `checksums.md5` while streaming it. The
paper, Lee, Marchionni, Bezaire, Varga, Danielson, Lovett-Barron, Losonczy and
Soltesz in Neuron (82:1129-1144), studies how PV+ basket cells (PVBCs) of mouse
CA1 innervate superficial (sPC) and deep (dPC) pyramidal cells, with paired
recordings, anatomy, optogenetics, in vivo two-photon imaging of PV+ axons in
running mice and a NEURON network model of 1,000 sPCs, 1,000 dPCs and 36 PVBCs;
the data set holds ATF files of current-step sweeps, for this paper 8 sPCs, 9
dPCs and 6 PVBCs, its other cells belonging to other papers. The claims were
written from the PyMuPDF text of the version of record and its Supplemental
Information, with the values of Figures S1E to S1H and S3F read from the
rendered PDF pages, and from the model code the paper links (ModelDB 153280);
the lab page the paper also links is now a parked domain and the Open Source
Brain page returns 404. The intrinsic property claims of Figures S1E, S1F, S1H,
S3F and Table S1 could be tested; the resting potential of Figure S1G, the
paired recording, anatomy, optogenetic, imaging and retrograde labelling claims
and the model claims could not. No outcome rests on an assumption. Reproduced
are `figs1e-if-curves` (two-way ANOVA group p = 0.411 under reading (a), at
+550 pA sPC 31.62 and dPC 30.56 Hz), `figs1f-input-resistance` (118.7 and 124.9
MOhm against 117 and 124), `figs1h-sag` (8.71 and 5.69 mV at -400 pA, p =
0.0020) and `figs3f-pvbc-firing` (PV34 silent up to +300 pA, then 2, 17, 36 and
52 Hz, the four expected values, though the paper does not name the figure's
cell and taking the best match of six is permissive). Partial is
`tables1-rheobase` (the median gives sPC 200 and dPC 150 pA, the rounded mean
200 pA for both, against +150 pA for both; no cell's rheobase changes with a
spike threshold of -20 or +10 mV or under the definition of SimTracker's
CellData tool). The model claims `fig4d-model-feedforward` and
`fig4ef-model-pvbc-rates` need 39 simulations of 5,000 ms; in the notebook a 20
ms run of one network on one core took 509.9 s to build the cells and then 8.20
s per simulated millisecond, about 11.5 hours per 5 s run and about 450
core-hours for the 39 runs. The author's first run had the same outcomes, with
the model's cost, about 670 core-hours, estimated from a 20 ms run timed
outside the notebook (808 s); the first try of that timing failed with a hoc
error, as setting `PrintVoltage=0` leaves `objref f` undeclared. The claims
file cites the ModelDB download, which now returns 404/504, so the GitHub
mirror (ModelDBRepository/153280 at commit 5314d07) was used. The author asked
no questions of a reader, so the answer and author-answers runs changed
nothing. Round 1 agreed with all 34 outcomes and noted that the input
resistance window includes sweeps with spikes at +100 pA in three cells, that
the second firing rate reading is unreliable near rheobase (PV34 at +350 pA,
14.9 against 2.0 Hz), that each cell's rheobase under other thresholds was not
shown, that taking the best of six PVBCs is permissive and that the model
timing was not run in the notebook; it also named SimTracker's CellData tool,
which the data descriptor gives for these files, as a possible source of the
rheobase definition. In reply the notebook was made to download, compile and
time the model, which lengthened its run to about 15 minutes, per-cell
rheobases under three thresholds and CellData's definition were added, and the
ATF header was printed. Round 2 agreed with all 34 outcomes and found text the
outputs did not support, among them timing numbers (808 s, 537 s, 12.39 s/ms,
677 core-hours) from another run than the one printed (11.43 s/ms, 625
core-hours), a PV37 sweep order break placed between -300 and -250 pA, and a
note that sh108_BC is from Lee et al. (2010); in reply the text was corrected
and the NEURON version (9.0.2) and the job scripts' 64 cores were printed. The
timing varied between runs, from 11.4 to 12.4 s per simulated millisecond in
the earlier runs to 8.01, 8.24 and 8.20 in the last three, so the record gives
the final run's numbers. The author's run went from 03:35 to 04:16 UTC; the
notebook ran in about 15 s at first and 20 s after the author-answers run, the
entry in 13.8 minutes after round 1 and about 12 minutes after round 2, and a
few notebook bugs (header parsing, a pingouin column name) were fixed during
development. The untracked dotfiles in the repository root were left alone.

The data set holds only the current-step sweeps of 17 PCs and 6 PVBCs behind
Figures S1E to S1H, S3F and Table S1: the paired recordings, optogenetics,
imaging, anatomy and retrograde labelling behind the paper's main figures are
not in it, and the paper names no other deposit, so 26 of its 34 claims cannot
be tested. The model's simulation results, which its README says are available
on request, are not public. The ATF files record only the membrane voltage,
with no injected and no holding current, and their header holds only sweep
start times, 5 s apart in every file; the step levels can be taken only from
the descriptor's table, with which the voltage responses are consistent in
sweep order. Because the PCs were held at -70 mV with an unrecorded current
(every PC's 0 pA baseline is between -72.2 and -67.4 mV), their resting
potential cannot be measured. No file or the descriptor gives a cell's animal,
slice, sex, hippocampal region or soma distance from the Pyr/Rad border, so the
sublayer assignment rests on the file names alone and results cannot be grouped
by animal. PV34 is deposited twice, as PVBC_PV34.atf and PV34_PVBC_mouse.atf,
with identical bytes, and was counted once; the descriptor lists 36 cells and
the zip holds 37 files. In PV37 the sweep order breaks between the sweeps the
descriptor gives as -250 and -200 pA (steady-state deflection -8.7 then -9.1
mV; -13.1 mV at -300 pA). The one CCK+ basket cell file, sh108_BC, is a cell
from another paper. No questions are put to the paper's authors.

The author's points on the protocol: the clock check of step 2 does not fit
single-cell sweeps with no trial table and no current channel, so the voltage
deflection was checked to rise with sweep order and to be near 0 on the 0 pA
sweep; the protocol does not say whether a timing estimate behind a `too_large`
block is a number from an analysis run outside the notebook; it is unclear
whether code used only to estimate cost belongs under `inputs`, so the model
repository was listed at its commit as deciding no outcome; and the model
download the claims file cites now fails, so the GitHub mirror was used.
