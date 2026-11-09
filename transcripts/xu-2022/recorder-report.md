I ran `python tools/readme_row.py 000239 --write`, which added the row 20 | 5 | 3 | 11 for Xu et al. 2022 to README.md. I also added the subsection below to the end of docs/pilot-notes.md. Nothing is committed. The repository root has untracked dotfiles and a `scripts` folder that I did not create, and I left them alone.

### 000239, Xu et al. 2022

Twenty claims reproduced, five partially, three not reproduced and eleven
blocked, all on the dandiset. Round 1 gave its own outcome for each claim from
the notebook with its conclusions removed and agreed with all 39; round 2
agreed again and nothing was proposed, so there was no third round. The paper
reports mice licking a port that moves through seven positions in standard,
backtracking and zigzag sequences, how population activity in S1TJ, M1TJ, ALM
and S1BF encodes tongue length, velocity and angle, sequence identity and
relative sequence time, and how optogenetic inhibition of these regions
changes licking. The unit and session counts, decoding of the five variables
and the relations among their coding axes, canonical correlation, decoding of
backtracking, zigzag context and the upcoming target position, the counts of
active neurons, initiation tuning, lick rhythmicity and the drop at water
contact, and the behavioural claims on sequence duration, learning,
backtracking, missed and consummatory licks and the starting side were tested.
The five optogenetic claims, the earplug, odour masking and tongue numbing
controls and the lick force are blocked as `metadata_insufficient`, inhibition
efficiency by cell type as `data_missing`, and the NNMF clustering as
`methods_underspecified`. Some outcomes rest on weak ground:
`fig3-units-per-session` is reproduced only on all 57 recording sessions, as
the 35 Figure 3 sessions the claim refers to give an SD of 14.4 against a
limit of 14.3; `ed5e-variance-explained` is 0.454 against a lower bound of
0.45 (0.453 to 0.455 over other seeds); in `ephys-unit-counts` three variants
of the unit classification put the multi-units inside tolerance (331, 309 and
295 against 339); the expected values of the five `fig3c` claims were read
from the Figure 3b image, which the verifiers could not check; in
`ed1l-proficiency-1500` proficiency had to be defined in the criterion and the
learning files may not start at the first day of training; and for
`ed2-backtracking-counts` a variant built after seeing the results, leaving
out 8 sessions with touches of a few ms, gives the paper's 47 sessions but 8
mice against 9. The author used the accepted author manuscript in PubMed
Central (PMC9109820), fetched through NCBI efetch after Europe PMC, BioC and
the PMC page failed, and read the Figure 3b values from the figure on Nature's
page.

The dandiset was converted by CatalystNeuro
(catalystneuro/oconnor-lab-to-nwb). The opto sessions do not name the
inhibited region: the 35 sessions at 4 mW and 25 at 2 mW, five per mouse,
carry only the light times and LED drive, the `opto` column (0, 1 and 2) and
the opto1 and opto2 series have no description, and no file has optogenetics
metadata, so Figure 2 and Extended Data Fig. 3j-m cannot be tested. The
control sessions do not mark the condition, which earplug session had
earplugs, which half of each air session had the air flow on, or which
numbing session was lidocaine; without the labels the paper's test finds an
earplug effect under 4 of 32 assignments and an air flow effect under 1 of 15.
The recorded area and the kind of session are given only by the session
description, the name of the lab's data folder, which is cut short ("... se")
in the files themselves; there is no electrodes table, unit location, depth or
quality label, and the area of the zigzag and "ephys others" sessions is not
given. Spike waveforms are not included, so units cannot be classified as
putative pyramidal or FS cells, and the fibre distance of the efficiency
recordings is not given. 1446 spike times in 35 files are duplicated within a
unit, which the Methods say were removed before analysis. Other findings: the
MX181003 learning file of 2018-10-02 15:30:57 repeats all 4028 touches of the
MX181002 file with the same start time and then continues, so it is unclear
which mouse it belongs to; in the 574 learning files start_time and stop_time
count from 0 while event times are on another clock (around 10^6 s); seqId in
the learning files holds the text of an unconverted MATLAB categorical object;
force sensor and lick port series are in volts without a calibration, tongue
landmarks are in pixels without a scale, and every trial column is described
as "no description"; the 8 sessions the Methods leave out for unregistered
touch offsets are not marked; and the paper says its MATLAB code is available
at GitHub but gives no address, and no repository was found. The session
groups of Figure 3, the 57 recording sessions, the 6 zigzag sessions from 3
mice and the 15 learning mice match the paper.

Threaded streaming was slow under h5py's global lock (15 minutes for an early
scan of all files), so the notebook uses processes, and an early trial filter
that wrongly required video before the cue was fixed before any claim was
judged; the seed and search variants added after round 1 raised the run time
to about 21 minutes, over the protocol's ten-minute aim. Untracked files in
the repository root that the author did not create were left alone. The
author's points on the protocol: nothing that stops outcomes being put in the
header table, which `handover` would not strip; whether numbers printed only
in a figure may serve as expected values; the paper's SD as tolerance for an
across-session mean, which is generous; a step that assumes the paper links
its code; an absence rule that assumes the paper names a test; whether an
undefined term like proficiency should be blocked or defined and tested; a
suggested clock check that is weak when sequences alternate direction; no rule
for a duplicate recording whose owner is unknown; a variant outside the
pre-registered readings that matches the paper; and a figure's p < 0.001 that
an exact paired permutation cannot reach with 8 sessions.
