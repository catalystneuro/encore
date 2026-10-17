I added the 000409 row to README.md and appended the subsection below to the end of docs/pilot-notes.md. Nothing is committed, and the attempt, claims and entry are unchanged.

The README row names the paper "Ibl et al. 2025", because the first author is a consortium. For the heading I used the name the claims file gives, "International Brain Laboratory". There are also untracked files in the repository root that I didn't create (`.bashrc`, `.idea`, `scripts` and others); I left them alone.

### 000409, International Brain Laboratory et al. 2025

Seventeen claims reproduced, three partially, three not reproduced and seven
blocked, all on the dandiset. Round 1 gave its own outcome for each claim
from the notebook with its conclusions removed and agreed with 29 of the 30;
it gave not reproduced for `behav-zero-contrast`, whose mean of 58.26% misses
58.7 +/- 0.4 by 0.04 points while t138 = 19.68 is within tolerance, and the
author kept partially reproduced. Round 1 also found that
`traj-stim-regions`, left as not attempted, fits the time limit, so the
author wrote a criterion for it and tested it. Round 2 disagreed on the same
claim, since the criterion defines no partial outcome, the author proposed
not reproduced, and a third round agreed. The paper reports a brain-wide map
of neural activity in mice performing a visual decision task with a block
prior, from 459 sessions of 139 mice in 12 labs: the dataset and its
canonical set of 201 regions, task behaviour, decoding of stimulus, choice
and feedback, single-cell selectivity, neural trajectories and their
latencies, and a feedback oscillation tied to licking. The dataset counts,
mice, probes and trials, behaviour, decoding, trajectory latencies, the
number of regions with significant stimulus trajectories and the oscillation
were tested, the neural claims on VISp, GRN, IRN and seven regions drawn at
random, with one run of nested cross-validation and 100 null sessions
against the paper's 10 and 200. Receptive-field mapping is blocked as
`data_missing`; the two single-cell claims as `methods_underspecified`,
because the null run selects 2.7e-3 and 2.5e-3 of units against the paper's
5e-5, although all 14 regional stimulus fractions are within 0.02 of the
paper's table; and wheel-speed decoding, the encoding model, the video
correlates and the Granger interactions as `other`, not attempted. The
visual latencies are not reproduced (VISam 59.2 ms is not later than VISpm
61.3 ms), nor are the 104 +/- 10.4 regions with significant stimulus
trajectories (46 here). Some outcomes rest on weak ground:
`behav-performance` passes only on the mean over sessions, 81.58%, and not
on the mean over mice, whose s.e.m. of 0.43 matches the paper's +/- 0.4;
`fig1g-block-switch` passes only under reading (b), at 9.9 trials on the
point estimate, with 75.9% of resamples within 4.5 to 11; the stimulus
against choice margin of `dec-stim-restricted` and `dec-choice-widespread`
is one region and rests on CL, whose choice p of 0.0010 sits at the
2-session floor; `traj-latency-late` rests on the criterion's 0 to 150 ms
window, as in the paper's 0 to 100 ms window IRN has no latency and GRN is
at 100.0 ms; and `dec-feedback-nearly-all` could not reach the criterion's 9
of 10 regions, as the paper's own table marks 8 of these 10 significant. The
author used the open access version of record and took the paper's
per-region results and inclusion tables from its repository at commit
118fc36 as reported values only.

The dandiset was converted by CatalystNeuro (catalystneuro/IBL-to-nwb). It
holds every session, mouse, probe and unit the paper reports and every count
of its inclusion table, and no recording is deposited twice. In 64 sessions,
all with the protocol name `_iblrig_tasks_ephysChoiceWorld` without a
version, `probability_left` alternates between 0.2 and 0.8 on every trial
after the first 90, so `block_index` and `block_type` change on every trial,
and the stimulus falls on the stated block's likely side in 47.5% to 57% of
biased trials against 75.9% to 82.8% in the other 395 sessions; these
sessions were left out of every analysis of the block prior. No session holds
the receptive-field mapping phase or its stimulus sequence, which the paper
ran in 504 of 699 insertions, and the saturation intervals of the IBL
aggregate trials table are not in the dandiset. The quality score and the
paper's 75,708 well-isolated units follow a noise cutoff below 5, where the
Methods give below 20 uV, which would give 95,430. Other findings:
`wheel_movement_onset_time` is described as after the go cue but precedes it
in 11.97% of trials; `reward_volume_uL` is 1.5 on every one of the 242,628
rewarded trials, against the Methods' 3 uL; the units description refers to
a `label` column that does not exist and calls all probes Neuropixels 1.0,
though four insertions used NP2010; subject weight is one value per mouse in
all its sessions; the paper's code takes age and weight from the IBL
database, while the ages at recording in the files are 13.1 to 65.9 weeks
against the Methods' 13 to 178, and it swaps the mean and median labels for
weight; the 81.4 +/- 0.4% correct is given as mean +/- s.d. but the 0.4 is
an s.e.m. (s.d. 5.12); the two single-cell tests are not independent, so the
paper's stated false-positive rate of 5e-5 understates it; `region_info.csv`
marks 210 regions canonical against 201; the paper's results table gives
visual latencies of 34.0, 44.7, 46.8, 59.6 and 66.0 ms against the text's
34, 42, 42, 57 and 78; the code's trajectory permutation classes and
Benjamini-Yekutieli correction differ from the Methods, though neither
brings the count near 104 (46 to 53); and the files hold spike sorting
revision 2025-05-06 where the code loads 2024-05-06, with identical counts.
The spikes share the trials' clock in 448 of the 454 canonical sessions, and
it could not be shown in 6.

Development runs failed on files without an `epochs` group, on mixed time
zones under pandas 3 and on a decoder that was not reproducible until the
liblinear seed was fixed, all fixed before the final run. Testing
`traj-stim-regions` raised the run time from about 11 to about 25 minutes
(1513 s in the last run), close to the 30-minute limit, so the nested null
was run only for VISp stimulus. Round 2 found the README run time and some
sentences of the notebook and record unsupported by the outputs, and these
were corrected. The author's points on the protocol: nothing covers a paper
whose own analysis cannot fit the time limit; no line between
`not_runnable` and not attempted; claims the criterion did not cover, one
with no measure in the paper and one whose criterion defined only the
reproduced case; no definition of a null rate far from the paper's, which
here blocks claims whose regional values match; whether the paper's results
tables count as outside inputs; no rule for data found wrong after the
criteria were written; a clock check that sessions with few loaded units
cannot pass; and a first author that is a consortium.
