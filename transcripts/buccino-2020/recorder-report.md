I added the README row for 000034 (0 reproduced, 1 partially, 0 not reproduced, 22 blocked) and put the subsection below at the end of `docs/pilot-notes.md`. The dataset's `catalystneuro` field is empty, so the findings paragraph doesn't open with the CatalystNeuro sentence. Nothing is committed.

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
