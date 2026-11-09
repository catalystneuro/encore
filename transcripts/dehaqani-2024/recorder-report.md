I added the note at `docs/pilot-notes/000931-dehaqani-2024-01.md` and changed no other file; nothing is committed. `git status` also lists some empty untracked files in the repository root (`.bashrc`, `scripts` and others). The sandbox created them, as the author's report says; I didn't make them and left them alone.

# 000931, Dehaqani et al. 2024

No claim reproduced, none partially, none not reproduced and 37 blocked, all
37 for missing data. The first verification round agreed with all 37 outcomes
as they stood and the second with all 37, and nothing was proposed after the
second, so there was no third round. It pins version 0.261011.1559; the paper
cites none, and all three published versions and the draft hold the same file
(same SHA-256), `sub-001/sub-001.nwb`, 177,095,408 bytes. The paper, Dehaqani,
Michelon, Patella, Petrucco, Piasini and Iurilli, "A mechanosensory feedback
that uncouples external and self-generated sensory responses in the olfactory
cortex" in Cell Reports, records Neuropixels 1.0 units in the anterior
piriform cortex (PCx) of 22 head-fixed mice in six groups, with the nasal
airflow, odor delivery and inhalation onsets, and sets the responses to slow
and fast inhalations against those to odor concentration, and the dataset
holds the spike times of one mouse. The
claims were written from the version of record with the legends of its
supplemental figures and the paper's code (iurillilab/mechano-olfactory_code,
tag v1.1, commit 3bec502, from Zenodo 10.5281/zenodo.10381293). Every claim
needs the breathing signal or inhalation times, odor trials, airflow pulses,
unit waveforms, brain areas or the other mice, so no claim could be tested,
and all 37 are blocked as `data_missing`; with none testable, a single cell
tagged `blocked-claims` sets each claim's needs against what the file holds.
The author asked a reader nothing, so the answer and author-answers runs
changed nothing. Round 1 asked whether odor trials are needed for the claims
on the ten control mice, and the author kept them, the Methods defining
odorless inhalations as those 13 to 4 s before an odor delivery; it also found
that `figs1b-speed-decoding-single-mice` left out the other five mice of
Figure 1, that the claim-id check read a claims file outside the bundle, that
the spectral peak could be a harmonic and that the depth convention was
unchecked, and in reply a subharmonic check was added (a synthetic 3 Hz train
giving 6.01 Hz before and 2.98 Hz after), which leaves the 0 to 1000 band at
2.78 Hz and moves the 2000 to 3000 band from 2.93 to 1.51 Hz, and the depths
were checked against the standard Neuropixels 1.0 channel map, the probe type
being assumed. Round 2 found all six round-1 points resolved and found
sentences the outputs did not support (a depth range of 80 to 3840 printed
only for all units, "deepest" units resting on the assumed channel map, "not a
harmonic", summary rows naming less missing data than the notes, "seven
groups" for six and the README placing the mouse in the concentration-series
experiment as fact), all corrected. The author's run took about 15 minutes
(17:20 to 17:34 UTC) with nothing failing; the notebook ran in 21 s at first,
22 s after the author-answers run, 23 s after round 1 and 28 s at the end. The
sandbox left empty placeholder files in the repository root, which the author
did not create.

The dandiset holds one NWB file from one of the paper's 22 mice, with the
spike times of 1013 sorted units and their labels; the nasal airflow, the odor
signal of the photo-ionization detector, the odor-trial TTL and the
inhalation-onset TTL that the Methods say were recorded, the artificial
airflow pulses, the unit waveforms, the brain area of each unit and the other
21 mice are not in it, and no dataset is stored outside `/units` and
`/general`. The paper says its processed data are available from the lead
contact on request, and its code deposit loads preprocessed files it does not
hold. The file has no electrodes table and gives no brain area for its units;
the 359 units curated good in Phy lie along the whole probe (depth 80 to 3840,
with 97, 127, 53 and 82 of them in the four 1000-um bands), so they include
structures above the PCx and the paper's selection of PCx layer 2 and 3 units
cannot be repeated. Only the keyword "Concentration Series" places the mouse
in an experiment, and the odors given are not stated. KSLabel is "good" for
all 1013 units and ContamPct is 100 for all of them, which contradict each
other, and the Phy curation (quality) is good for 359 units, mua for 10 and
missing for 644. Of the unit table's columns only quality, spike_times and
unit_name have a description, depth, Amplitude and amp have no unit, and the
session description is the converter's default. The file's
related_publications names the bioRxiv preprint (10.1101/2023.04.04.535405),
and the two 2024 versions (0.240305.0939 and 0.240305.0945) do not name the
paper. What could be checked is consistent with the paper: the good units have
ISI violation rates (median 0.0066, Q1 0, Q3 0.029) and presence ratios (1 in
every quartile) in the ranges the Methods report, all fire above the 0.5 Hz
threshold, no unit is duplicated, and the summed activity of the good units
nearest the probe tip, by the assumed Neuropixels 1.0 channel map, peaks at
2.78 Hz, within the range of mouse breathing. With one data stream the clock
check could not be made. No question is put to the paper's authors.

The author's points on the protocol: nothing covers a dataset where no claim
can be tested, and the required notebook parts were kept with one cell for all
blocked claims; the clock-alignment check assumes a second data stream; "stream,
do not download" says nothing about reading the claims file from a notebook;
and writing the record with PyYAML left `id: 000931` unquoted, which other
YAML parsers would read as the number 931, and `entry.py check` did not catch
it.
